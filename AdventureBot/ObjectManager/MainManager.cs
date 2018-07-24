using System;
using System.Collections.Generic;
using System.IO;
using System.Reflection;
using IronPython.Hosting;
using IronPython.Runtime.Types;

namespace AdventureBot.ObjectManager
{
    internal interface IObjectManager
    {
        void Register(GameObjectAttribute attribute, Create<object> creator);
    }

    internal class MainManager : Singleton<MainManager>
    {
        private readonly List<IObjectManager> _managers = new List<IObjectManager>();

        internal void Register<TMgr>(TMgr manager) where TMgr : IObjectManager
        {
            _managers.Add(manager);
        }

        internal void LoadPython(string path, string filename)
        {
#if DEBUG
            var engine = Python.CreateEngine(AppDomain.CurrentDomain, new Dictionary<string, object>
            {
                {"Debug", true}
            });
#else
            var engine = IronPython.Hosting.Python.CreateEngine(AppDomain.CurrentDomain);
#endif
            var scope = engine.CreateScope();
            engine.Runtime.LoadAssembly(Assembly.GetExecutingAssembly());

            engine.Execute($"import os\nos.chdir(r'{path}')");

            engine.ExecuteFile(Path.Combine(path, "module_loader.py"), scope);
            var loaded =
                engine.Execute<Tuple<GameObjectAttribute, Type, PythonType>>(
                    $"load_path(r'{Path.Combine(path, filename)}')",
                    scope);
            foreach (var manager in _managers)
            {
                manager.Register(
                    loaded.Item1,
                    () => engine.Operations.CreateInstance(loaded.Item3)
                );
            }
        }

        internal void LoadAssembly(Assembly assembly)
        {
            foreach (var type in assembly.GetTypes())
            {
                if (type.GetCustomAttribute(typeof(GameObjectAttribute)) is GameObjectAttribute attr)
                {
                    var ctor = type.GetConstructor(Type.EmptyTypes);
                    foreach (var manager in _managers)
                    {
                        manager.Register(attr, () => ctor.Invoke(new object[] { }));
                    }
                }
            }
        }

        internal void LoadAssembly(string path)
        {
            LoadAssembly(Assembly.LoadFrom(path));
        }
    }
}