using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.IO;
using System.Linq;
using System.Reflection;
using IronPython.Hosting;
using IronPython.Runtime.Types;

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

    internal void LoadAssembly(Assembly assembly)
    {
        foreach (var type in assembly.GetTypes())
        {
            if (!(type.GetCustomAttribute(typeof(GameObjectAttribute)) is GameObjectAttribute attr))
            {
                continue;
            }

            var ctor = type.GetConstructor(Type.EmptyTypes);
            foreach (var manager in _managers)
            {
                Debug.Assert(ctor != null, nameof(ctor) + " != null");
                manager.Register(attr, () => ctor.Invoke(new object[] { }));
            }
        }
    }

    internal void LoadAssembly(string path)
    {
        LoadAssembly(Assembly.LoadFrom(path));
    }

    public void LoadPython(string root, string module)
    {
        var engine = Python.CreateEngine();
        engine.Runtime.LoadAssembly(Assembly.GetExecutingAssembly());

        var paths = engine.GetSearchPaths().ToList();
        paths.Add(root);
        engine.SetSearchPaths(paths);

        var scope = engine.ImportModule(module);
        foreach (var (key, value) in scope.GetItems())
        {
            if (value is not PythonType)
            {
                continue;
            }

            try
            {
                var attrs = (IList<object>) value.__attrs__;
                var attr = attrs.OfType<GameObjectAttribute>().Single();
                foreach (var manager in _managers)
                {
                    manager.Register(attr, () => engine.Operations.CreateInstance(value));
                }
            }
            catch
            {
                // ignored
            }
        }
    }
}