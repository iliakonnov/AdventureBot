using System;
using System.Collections.Generic;
using System.Linq;

namespace AdventureBot
{
    public class SortedByValueDictionary<TKey, TValue> where TValue : IComparable<TValue>
    {
        private readonly Dictionary<TKey, TValue> _dictionary;
        private readonly object _lock = new object();

        public SortedByValueDictionary()
        {
            _dictionary = new Dictionary<TKey, TValue>();
        }

        public IReadOnlyList<KeyValuePair<TKey, TValue>> Sorted
        {
            get
            {
                lock (_lock)
                {
                    return _dictionary.OrderByDescending(kv => kv.Value).ToList();
                }
            }
        }

        public void Add(TKey key, TValue value)
        {
            lock (_lock)
            {
                _dictionary[key] = value;
            }
        }

        public TValue Get(TKey key)
        {
            lock (_lock)
            {
                return _dictionary[key];
            }
        }
    }
}