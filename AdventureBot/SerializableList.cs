using System.Collections;
using System.Collections.Generic;
using MessagePack;

namespace AdventureBot
{
    [MessagePackObject]
    public class SerializableList : ISerializable, IList<ISerializable>
    {
        [Key(0)] private readonly List<ISerializable> _listImplementation;

        public SerializableList()
        {
            _listImplementation = new List<ISerializable>();
        }

        [SerializationConstructor]
        public SerializableList(List<ISerializable> listImplementation)
        {
            _listImplementation = listImplementation;
        }
        
        public IEnumerator<ISerializable> GetEnumerator()
        {
            return _listImplementation.GetEnumerator();
        }

        IEnumerator IEnumerable.GetEnumerator()
        {
            return ((IEnumerable) _listImplementation).GetEnumerator();
        }

        public void Add(ISerializable item)
        {
            _listImplementation.Add(item);
        }

        public void Clear()
        {
            _listImplementation.Clear();
        }

        public bool Contains(ISerializable item)
        {
            return _listImplementation.Contains(item);
        }

        public void CopyTo(ISerializable[] array, int arrayIndex)
        {
            _listImplementation.CopyTo(array, arrayIndex);
        }

        public bool Remove(ISerializable item)
        {
            return _listImplementation.Remove(item);
        }

        [IgnoreMember] public int Count => _listImplementation.Count;

        [IgnoreMember] public bool IsReadOnly => ((IList<ISerializable>) _listImplementation).IsReadOnly;

        public int IndexOf(ISerializable item)
        {
            return _listImplementation.IndexOf(item);
        }

        public void Insert(int index, ISerializable item)
        {
            _listImplementation.Insert(index, item);
        }

        public void RemoveAt(int index)
        {
            _listImplementation.RemoveAt(index);
        }

        public ISerializable this[int index]
        {
            get => _listImplementation[index];
            set => _listImplementation[index] = value;
        }
    }
}