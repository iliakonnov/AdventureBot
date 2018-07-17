using System;
using System.Collections.Concurrent;
using System.Collections.Generic;
using JetBrains.Annotations;
using MessagePack;

namespace AdventureBot
{
    [MessagePackObject]
    public class VariableContainer : ISerializable
    {
        [Key("variables")] private readonly ConcurrentDictionary<string, ISerializable> _variables =
            new ConcurrentDictionary<string, ISerializable>();

        [Obsolete("This constructor for serializer only")]
        [UsedImplicitly]
        [SerializationConstructor]
        public VariableContainer(ConcurrentDictionary<string, ISerializable> variables)
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
            _variables.TryRemove(key, out _);
        }
    }
}