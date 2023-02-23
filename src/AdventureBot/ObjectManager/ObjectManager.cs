using System;
using System.Collections.Generic;
using System.Linq.Expressions;

namespace AdventureBot.ObjectManager;

public interface IManager<in T>
{
    void Register(GameObjectAttribute attribute, Func<T> factory);
}

public class ObjectManager<TObj> : Singleton<ObjectManager<TObj>>, IObjectManager
{
    private readonly Dictionary<Type, IManager<TObj>> _managers = new();

    public ObjectManager()
    {
        MainManager.Instance.Register(this);
    }

    public void Register(GameObjectAttribute attribute, Expression ctor)
    {
        var targetType = attribute.Type ?? typeof(TObj);
        if (!targetType.IsAssignableTo(typeof(TObj)))
        {
            return;
        }

        var factory = (Func<TObj>)Expression.Lambda(Expression.Convert(ctor, targetType)).Compile();

        foreach (var manager in _managers.Values)
        {
            manager.Register(attribute, factory);
        }
    }

    public void RegisterManager<TMgr>() where TMgr : IManager<TObj>, new()
    {
        _managers[typeof(TMgr)] = new TMgr();
    }

    public TMgr Get<TMgr>() where TMgr : IManager<TObj>
    {
        return (TMgr)_managers[typeof(TMgr)];
    }
}