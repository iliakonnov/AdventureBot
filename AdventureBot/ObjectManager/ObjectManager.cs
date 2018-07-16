using System;
using System.Collections.Generic;
using System.Reflection;
using Microsoft.Extensions.Logging;

namespace AdventureBot.ObjectManager
{       
    public delegate T Create<out T>();
    
    public interface IManager<in T>
    {
        void Register(GameObjectAttribute attribute, Create<T> creator);
    }

    public class ObjectManager<TObj> : Singleton<ObjectManager<TObj>>, IObjectManager
    {
        private Dictionary<Type, IManager<TObj>> _managers = new Dictionary<Type, IManager<TObj>>();
        
        public ObjectManager()
        {
            MainManager.Instance.Register(this);
        }
        
        public void RegisterManager<TMgr>(TMgr manager) where TMgr : IManager<TObj>
        {
            _managers[typeof(TMgr)] = manager;
        }
        
        public void RegisterManager<TMgr>() where TMgr : IManager<TObj>, new()
        {
            _managers[typeof(TMgr)] = new TMgr();
        }

        public TMgr Get<TMgr>()
        {
            return (TMgr) _managers[typeof(TMgr)];
        }

        public void Register<T>(GameObjectAttribute attribute) where T : TObj, new()
        {
            Register(attribute, () => new T());
        }

        public void Register(GameObjectAttribute attribute, Create<TObj> creator)
        {
            foreach (var manager in _managers.Values)
            {
                manager.Register(attribute, creator);
            }
        }

        public void LoadType(GameObjectAttribute attribute, Type type)
        {
            if (typeof(TObj).IsAssignableFrom(type))
            {
                Register(
                    attribute,
                    () => (TObj) type.GetConstructor(Type.EmptyTypes).Invoke(new object[] { })
                );
            }
        }
    }
}