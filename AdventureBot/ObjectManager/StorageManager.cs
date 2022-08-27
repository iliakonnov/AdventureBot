﻿using System;
using System.Collections.Generic;
using JetBrains.Annotations;

namespace AdventureBot.ObjectManager;

public class StorageManager<T, TAttribute> : IManager<T> where TAttribute : IdentifiableAttribute
{
    private readonly NullableDictionary<string, T> _cache = new();

    private readonly NullableDictionary<string, Item> _items = new();

    public void Register(GameObjectAttribute attribute, Create<T> creator)
    {
        if (!(attribute is TAttribute identifiableAttribute))
        {
            return;
        }

        var identifier = identifiableAttribute.Identifier;

        _items[identifier] = new Item
        {
            Identificator = identifier,
            Creator = creator,
            Attribute = identifiableAttribute
        };

        Get(identifier);
    }

    internal void InitializeAll()
    {
        foreach (var key in Keys())
        {
            Get(key);
        }
    }

    [CanBeNull]
    public T Get([CanBeNull] string identifier)
    {
        if (_cache.TryGetValue(identifier, out var result))
        {
            return result;
        }

        if (!_items.TryGetValue(identifier, out var item))
        {
            return default;
        }

        var res = item.Creator();
        _cache[identifier] = res;
        item.Creator = () => throw new Exception("This item already initialized!");
        return res;
    }

    public IEnumerable<Item> Items()
    {
        return _items.Values;
    }

    public IEnumerable<string> Keys()
    {
        return _items.Keys;
    }

    public bool Contains(string identifier)
    {
        return _items.ContainsKey(identifier);
    }

    public class Item
    {
        public TAttribute Attribute;
        internal Create<T> Creator;
        public string Identificator;
    }
}