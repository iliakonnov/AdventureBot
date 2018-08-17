using System;
using System.Collections.Generic;

namespace AdventureBot
{
    public class SortedByValueDictionary<TKey, TValue> where TValue : IComparable<TValue>
    {
        public IReadOnlyList<KeyValuePair<TValue, TKey>> Sorted => _list;
        private List<KeyValuePair<TValue, TKey>> _list;
        private Dictionary<TKey, int> _dictionary;

        public SortedByValueDictionary()
        {
            _list = new List<KeyValuePair<TValue, TKey>>();
            _dictionary = new Dictionary<TKey, int>();
        }

        public void Add(TKey key, TValue value)
        {
            if (_dictionary.TryGetValue(key, out var idx))
            {
                _list.RemoveAt(idx);
            }
            var kv = new KeyValuePair<TValue, TKey>(value, key);
            var place = _list.BinarySearch(kv,
                Comparer<KeyValuePair<TValue, TKey>>.Create((a, b) => a.Key.CompareTo(b.Key)));
            if (place < 0)
            {
                place = ~place;
            }

            _list.Insert(place, kv);
            _dictionary[key] = place;
        }

        public TValue Get(TKey key)
        {
            return _list[_dictionary[key]].Key;
        }
    }
}