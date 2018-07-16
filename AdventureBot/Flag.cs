using System.Collections.Generic;
using System.Collections.Immutable;
using System.Diagnostics.CodeAnalysis;
using System.Linq;
using MessagePack;

namespace AdventureBot
{
    [MessagePackObject(true)]
    public class StructFlag<T> : Flag<T>, ISerializable where T : struct
    {
        public StructFlag(T value) : base(value)
        {
        }

        public StructFlag(IEnumerable<T> values) : base(values)
        {
        }

        public StructFlag(ImmutableHashSet<T> values) : base(values)
        {
        }

        public static StructFlag<T> operator |(StructFlag<T> a, StructFlag<T> b)
        {
            return new StructFlag<T>(a.Values.Union(b.Values));
        }

        public static StructFlag<T> operator &(StructFlag<T> a, StructFlag<T> b)
        {
            return new StructFlag<T>(a.Values.Intersect(b.Values));
        }
    }

    [MessagePackObject(true)]
    public class SerializableFlag<T> : Flag<T>, ISerializable where T : ISerializable
    {
        public SerializableFlag(T value) : base(value)
        {
        }

        public SerializableFlag(IEnumerable<T> values) : base(values)
        {
        }

        public SerializableFlag(ImmutableHashSet<T> values) : base(values)
        {
        }

        public static SerializableFlag<T> operator |(SerializableFlag<T> a, SerializableFlag<T> b)
        {
            return new SerializableFlag<T>(a.Values.Union(b.Values));
        }

        public static SerializableFlag<T> operator &(SerializableFlag<T> a, SerializableFlag<T> b)
        {
            return new SerializableFlag<T>(a.Values.Intersect(b.Values));
        }
    }

    /// <summary>
    ///     Please, do not use. Use <see cref="StructFlag{T}" /> or <see cref="SerializableFlag{T}" />
    /// </summary>
    /// <typeparam name="T">This type must be serializable!</typeparam>
    [MessagePackObject(true)]
    public class Flag<T>
    {
        private int? _hashcode;

        public Flag()
        {
            Values = ImmutableHashSet.Create<T>();
        }

        public Flag(T value)
        {
            Values = ImmutableHashSet.Create(value);
        }

        public Flag(IEnumerable<T> values)
        {
            Values = ImmutableHashSet.Create(values.ToArray());
        }

        public Flag(params T[] values)
        {
            Values = ImmutableHashSet.Create(values);
        }

        [SerializationConstructor]
        public Flag(ImmutableHashSet<T> values)
        {
            Values = values;
        }

        public ImmutableHashSet<T> Values { get; }

        public static Flag<T> operator |(Flag<T> a, Flag<T> b)
        {
            return new Flag<T>(a.Values.Union(b.Values));
        }

        public static Flag<T> operator &(Flag<T> a, Flag<T> b)
        {
            return new Flag<T>(a.Values.Intersect(b.Values));
        }

        public bool Intersects(Flag<T> other)
        {
            return !Values.Intersect(other.Values).IsEmpty;
        }

        public override bool Equals(object obj)
        {
            if (obj == this) return true;

            switch (obj)
            {
                case null:
                    return false;
                case Flag<T> other:
                    return other.Values.SetEquals(Values);
            }

            return false;
        }

        [SuppressMessage("ReSharper", "NonReadonlyMemberInGetHashCode")]
        public override int GetHashCode()
        {
            if (_hashcode != null) return (int) _hashcode;

            // calculate hashcode and save it to cache
            _hashcode = -1138380728;
            foreach (var value in Values) _hashcode ^= value.GetHashCode();

            return (int) _hashcode;
        }

        public override string ToString()
        {
            return string.Join("|", Values);
        }
    }
}