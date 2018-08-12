using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Reflection;

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
    }
}