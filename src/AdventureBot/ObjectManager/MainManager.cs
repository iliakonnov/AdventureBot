using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.IO;
using System.Linq;
using System.Linq.Expressions;
using System.Reflection;
using IronPython.Hosting;
using IronPython.Runtime;
using IronPython.Runtime.Types;
using Microsoft.Scripting.Hosting;
using Microsoft.Scripting.Runtime;
using NLog;

namespace AdventureBot.ObjectManager;

internal interface IObjectManager
{
    void Register(GameObjectAttribute attribute, Expression ctor);
}

internal class MainManager : Singleton<MainManager>
{
    private readonly List<IObjectManager> _managers = new();
    private static Logger Logger = LogManager.GetCurrentClassLogger();

    internal void Register<TMgr>(TMgr manager) where TMgr : IObjectManager
    {
        _managers.Add(manager);
    }

    private void LoadType(Type type)
    {
        if (!(type.GetCustomAttribute(typeof(GameObjectAttribute)) is GameObjectAttribute attr))
        {
            return;
        }

        attr.Type = type;

        var ctor = type.GetConstructor(Type.EmptyTypes);
        foreach (var manager in _managers)
        {
            Debug.Assert(ctor != null, nameof(ctor) + " != null");
            manager.Register(attr, Expression.New(ctor));
        }
    }

    internal void LoadAssembly(Assembly assembly)
    {
        foreach (var type in assembly.GetTypes())
        {
            LoadType(type);
        }
    }

    internal void LoadAssembly(string path)
    {
        if (!File.Exists(path))
        {
            Logger.Warn("Skipping assembly {}: not found", path);
            return;
        }

        LoadAssembly(Assembly.LoadFrom(path));
    }

    private void LoadPythonObject(object value)
    {
        switch (value)
        {
            case PythonType type:
                LoadType(type);
                return;
            case PythonModule module:
            {
                var storage = ((ObjectDictionaryExpando)module.Scope.Storage).Dictionary;
                var nested = storage.TryGetValue("__all__", out var all)
                    ? ((IList<object>)all).Cast<string>()
                    : storage.Keys.Cast<string>().Where(var => !var.StartsWith("_"));

                foreach (var name in nested)
                {
                    LoadPythonObject(storage[name]);
                }

                return;
            }
        }
    }

    private void LoadPythonInternal(ScriptEngine engine, string module)
    {
        var scope = engine.ImportModule(module);

        var nested = scope.ContainsVariable("__all__")
            ? ((IList<object>)scope.GetVariable("__all__")).Cast<string>()
            : scope.GetVariableNames().Where(x => !x.StartsWith("_"));
        foreach (var variable in nested.Select(scope.GetVariable))
        {
            LoadPythonObject(variable);
        }
    }

    public void LoadPython(string module)
    {
        var engine = Python.CreateEngine();
        foreach (var assembly in AppDomain.CurrentDomain.GetAssemblies())
        {
            engine.Runtime.LoadAssembly(assembly);
        }

        var paths = engine.GetSearchPaths().ToList();
        paths.AddRange(Configuration.Config.GetSection("python_paths").GetChildren().Select(path => path.Value));
        engine.SetSearchPaths(paths);

        try
        {
            LoadPythonInternal(engine, module);
        }
        catch (Exception exception)
        {
            Console.Error.WriteLine(engine.GetService<ExceptionOperations>().FormatException(exception));
            throw;
        }
    }
}