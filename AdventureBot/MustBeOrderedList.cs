using System;
using System.Collections;
using System.Collections.Generic;
using System.Linq;

namespace AdventureBot
{
    internal class MustBeOrderedList<T> : IOrderedEnumerable<T>, IList<T>
    {
        private readonly IList<T> _listImplementation;

        public MustBeOrderedList(IOrderedEnumerable<T> enumerable)
        {
            _listImplementation = enumerable.ToList();
        }

        public MustBeOrderedList()
        {
            _listImplementation = new List<T>();
        }

        public void Add(T item)
        {
            _listImplementation.Add(item);
        }

        public void Clear()
        {
            _listImplementation.Clear();
        }

        public bool Contains(T item)
        {
            return _listImplementation.Contains(item);
        }

        public void CopyTo(T[] array, int arrayIndex)
        {
            _listImplementation.CopyTo(array, arrayIndex);
        }

        public bool Remove(T item)
        {
            return _listImplementation.Remove(item);
        }

        public int Count => _listImplementation.Count;

        public bool IsReadOnly => _listImplementation.IsReadOnly;

        public int IndexOf(T item)
        {
            return _listImplementation.IndexOf(item);
        }

        public void Insert(int index, T item)
        {
            _listImplementation.Insert(index, item);
        }

        public void RemoveAt(int index)
        {
            _listImplementation.RemoveAt(index);
        }

        public T this[int index]
        {
            get => _listImplementation[index];
            set => _listImplementation[index] = value;
        }

        public IOrderedEnumerable<T> CreateOrderedEnumerable<TKey>(Func<T, TKey> keySelector,
            IComparer<TKey> comparer, bool descending)
        {
            return descending
                ? _listImplementation.OrderByDescending(keySelector, comparer)
                : _listImplementation.OrderBy(keySelector, comparer);
        }

        public IEnumerator<T> GetEnumerator()
        {
            return _listImplementation.GetEnumerator();
        }

        IEnumerator IEnumerable.GetEnumerator()
        {
            return ((IEnumerable) _listImplementation).GetEnumerator();
        }
    }
}