using System;
using System.Collections;
using System.Collections.Generic;
using JetBrains.Annotations;

namespace AdventureBot;

// Based on https://github.com/nhibernate/nhibernate-core/blob/master/src/NHibernate/Util/NullableDictionary.cs
public class NullableDictionary<TKey, TValue> : IDictionary<TKey, TValue>
    where TKey : class
{
    private readonly Dictionary<TKey, TValue> _dict;
    private bool _gotNullValue;
    private TValue _nullValue;

    public NullableDictionary()
    {
        _dict = new Dictionary<TKey, TValue>();
    }

    public NullableDictionary(IEqualityComparer<TKey> comparer)
    {
        _dict = new Dictionary<TKey, TValue>(comparer);
    }

    public bool ContainsKey([CanBeNull] TKey key)
    {
        return key == null ? _gotNullValue : _dict.ContainsKey(key);
    }

    public void Add([CanBeNull] TKey key, TValue value)
    {
        if (key == null)
        {
            _nullValue = value;
            _gotNullValue = true;
        }
        else
        {
            _dict[key] = value;
        }
    }

    public bool Remove([CanBeNull] TKey key)
    {
        if (key != null)
        {
            return _dict.Remove(key);
        }

        if (!_gotNullValue)
        {
            return false;
        }

        _nullValue = default;
        _gotNullValue = false;
        return true;
    }

    public bool TryGetValue([CanBeNull] TKey key, out TValue value)
    {
        if (key != null)
        {
            return _dict.TryGetValue(key, out value);
        }

        if (_gotNullValue)
        {
            value = _nullValue;
            return true;
        }

        value = default;
        return false;
    }

    public TValue this[[CanBeNull] TKey key]
    {
        get
        {
            if (key == null)
            {
                return _nullValue;
            }

            _dict.TryGetValue(key, out var ret);

            return ret;
        }
        set
        {
            if (key == null)
            {
                _nullValue = value;
                _gotNullValue = true;
            }
            else
            {
                _dict[key] = value;
            }
        }
    }

    public ICollection<TKey> Keys
    {
        get
        {
            if (!_gotNullValue)
            {
                return _dict.Keys;
            }

            var keys = new List<TKey>(_dict.Keys) {null};
            return keys;
        }
    }

    public ICollection<TValue> Values
    {
        get
        {
            if (!_gotNullValue)
            {
                return _dict.Values;
            }

            var values = new List<TValue>(_dict.Values) {_nullValue};
            return values;
        }
    }

    public IEnumerator<KeyValuePair<TKey, TValue>> GetEnumerator()
    {
        foreach (var kvp in _dict)
        {
            yield return kvp;
        }

        if (_gotNullValue)
        {
            yield return new KeyValuePair<TKey, TValue>(null, _nullValue);
        }
    }

    IEnumerator IEnumerable.GetEnumerator()
    {
        return GetEnumerator();
    }

    public void Add(KeyValuePair<TKey, TValue> item)
    {
        if (item.Key == null)
        {
            _nullValue = item.Value;
            _gotNullValue = true;
        }
        else
        {
            _dict.Add(item.Key, item.Value);
        }
    }

    public void Clear()
    {
        _dict.Clear();
        _nullValue = default;
        _gotNullValue = false;
    }

    public bool Contains(KeyValuePair<TKey, TValue> item)
    {
        return TryGetValue(item.Key, out var val) && Equals(item.Value, val);
    }

    public void CopyTo(KeyValuePair<TKey, TValue>[] array, int arrayIndex)
    {
        throw new NotImplementedException();
    }

    public bool Remove(KeyValuePair<TKey, TValue> item)
    {
        throw new NotImplementedException();
    }

    public int Count
    {
        get
        {
            if (_gotNullValue)
            {
                return _dict.Count + 1;
            }

            return _dict.Count;
        }
    }

    public bool IsReadOnly => false;
}