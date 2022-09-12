using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Reflection;
using IronPython.Hosting;
using IronPython.Runtime;
using IronPython.Runtime.Types;
using Microsoft.Scripting.Hosting;
using Microsoft.Scripting.Runtime;

namespace AdventureBot.ObjectManager;

internal interface IObjectManager
{
    void Register(GameObjectAttribute attribute, Create<object> creator);
}

internal class MainManager : Singleton<MainManager>
{
    private readonly List<IObjectManager> _managers = new();

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

        var ctor = type.GetConstructor(Type.EmptyTypes);
        foreach (var manager in _managers)
        {
            Debug.Assert(ctor != null, nameof(ctor) + " != null");
            manager.Register(attr, () => ctor.Invoke(new object[] { }));
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
        LoadAssembly(Assembly.LoadFrom(path));
    }

    public void LoadPython(string module)
    {
        var engine = Python.CreateEngine();
        engine.Runtime.LoadAssembly(Assembly.GetExecutingAssembly());

        var paths = engine.GetSearchPaths().ToList();
        paths.AddRange(Configuration.Config.GetSection("python_paths").GetChildren().Select(path => path.Value));
        engine.SetSearchPaths(paths);

        var parts = module.Split('.').ToList();
        parts.Add("__all__");
        using var currPart = parts.GetEnumerator();

        currPart.MoveNext();
        var scope = engine.ImportModule(module);
        
        currPart.MoveNext();
        dynamic prev = null;
        var curr = scope.GetVariable(currPart.Current);

        while (currPart.MoveNext())
        {
            prev = curr;
            curr = ((ObjectDictionaryExpando) ((PythonModule) curr).Scope.Storage).Dictionary[currPart.Current];
        }

        foreach (var name in ((IList<object>) curr).Cast<string>())
        {
            var value = ((ObjectDictionaryExpando) ((PythonModule) prev).Scope.Storage).Dictionary[name];
            if (value is not PythonType type)
            {
                continue;
            }

            try
            {
                LoadType(type);
            }
            catch (Exception exception)
            {
                Console.Error.WriteLine(engine.GetService<ExceptionOperations>().FormatException(exception));
                throw;
            }
        }
    }
}