﻿using System;
using System.Collections.Generic;

namespace AdventureBot.ObjectManager;

public delegate T Create<out T>();

public interface IManager<in T>
{
    void Register(GameObjectAttribute attribute, Create<T> creator);
}

public class ObjectManager<TObj> : Singleton<ObjectManager<TObj>>, IObjectManager
{
    private readonly Dictionary<Type, IManager<TObj>> _managers = new();

    public ObjectManager()
    {
        MainManager.Instance.Register(this);
    }

    public void Register(GameObjectAttribute attribute, Create<object> creator)
    {
        foreach (var manager in _managers.Values)
        {
            manager.Register(attribute, () => (TObj) creator());
        }
    }

    public void RegisterManager<TMgr>(TMgr manager) where TMgr : IManager<TObj>
    {
        _managers[typeof(TMgr)] = manager;
    }

    public void RegisterManager<TMgr>() where TMgr : IManager<TObj>, new()
    {
        _managers[typeof(TMgr)] = new TMgr();
    }

    public TMgr Get<TMgr>() where TMgr : IManager<TObj>
    {
        return (TMgr) _managers[typeof(TMgr)];
    }

    public void Register<T>(GameObjectAttribute attribute) where T : TObj, new()
    {
        Register(attribute, () => new T());
    }
}