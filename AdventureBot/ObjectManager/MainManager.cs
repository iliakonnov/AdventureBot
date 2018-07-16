using System;
using System.Collections.Generic;
using System.Reflection;

namespace AdventureBot.ObjectManager
{   
    internal interface IObjectManager
    {
        void LoadType(GameObjectAttribute attribute, Type type);
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
                if (type.GetCustomAttribute(typeof(GameObjectAttribute)) is GameObjectAttribute attr)
                {
                    foreach (var manager in _managers)
                    {
                        manager.LoadType(attr, type);
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