using System;
using System.Collections.Generic;
using JetBrains.Annotations;
using MessagePack;

namespace AdventureBot
{
    [MessagePackObject]
    public class VariableContainer : ISerializable
    {
        [Key("variables")]
        private readonly Dictionary<string, ISerializable> _variables = new Dictionary<string, ISerializable>();

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
        public ISerializable Get(string key) => _variables.GetValueOrDefault(key, null);
        
        [CanBeNull]
        public T Get<T>(string key) where T : class => _variables.GetValueOrDefault(key, null) as T;

        public IEnumerable<string> Keys() => _variables.Keys;

        public void Set(string key, ISerializable value) => _variables[key] = value;

        public void Remove(string key) => _variables.Remove(key);
    }
}