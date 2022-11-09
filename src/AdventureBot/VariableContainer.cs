using System;
using System.Collections.Generic;
using JetBrains.Annotations;
using MessagePack;

namespace AdventureBot;

[MessagePackObject]
public class VariableContainer : ISerializable
{
    [Key("variables")] private readonly Dictionary<string, ISerializable> _variables = new();

    [Obsolete("This constructor for serializer only")]
    [UsedImplicitly]
    [SerializationConstructor]
    public VariableContainer(Dictionary<string, ISerializable> variables)
    {
        _variables = variables;
    }

    public VariableContainer()
    {
    }

    [CanBeNull]
    public ISerializable Get(string key)
    {
        return _variables.GetValueOrDefault(key);
    }

    [CanBeNull]
    public T Get<T>(string key) where T : class
    {
        return _variables.GetValueOrDefault(key) as T;
    }

    public IEnumerable<string> Keys()
    {
        return _variables.Keys;
    }

    public void Set(string key, ISerializable value)
    {
        _variables[key] = value;
    }

    public void Remove(string key)
    {
        _variables.Remove(key);
    }
}