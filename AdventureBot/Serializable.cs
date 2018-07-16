using AdventureBot.Item;
using AdventureBot.Messenger;
using AdventureBot.User.Stats;
using MessagePack;

namespace AdventureBot
{
    [Union(0, typeof(Serializable.String))]
    [Union(1, typeof(Serializable.Int))]
    [Union(2, typeof(Serializable.Double))]
    [Union(3, typeof(Serializable.Bool))]
    [Union(4, typeof(VariableContainer))]
    [Union(5, typeof(User.User))]
    [Union(6, typeof(ItemInfo))]
    [Union(7, typeof(RecivedMessage))]
    [Union(8, typeof(SentMessage))]
    [Union(9, typeof(SerializableFlag<ISerializable>))]
    [Union(10, typeof(StatsProperty))]
    public interface ISerializable
    {
    }

    public static class Serializable
    {
        [MessagePackObject]
        public class String : ISerializable
        {
            [Key(0)] private readonly string _value;

            [SerializationConstructor]
            public String(string value)
            {
                _value = value;
            }

            public static implicit operator string(String s)
            {
                return s._value;
            }

            public static implicit operator String(string s)
            {
                return new String(s);
            }
        }

        [MessagePackObject]
        public class Int : ISerializable
        {
            [Key(0)] private readonly int _value;

            [SerializationConstructor]
            public Int(int value)
            {
                _value = value;
            }

            public static implicit operator int(Int i)
            {
                return i?._value ?? default;
            }

            public static implicit operator int?(Int i)
            {
                return i?._value;
            }
        }

        [MessagePackObject]
        public class Double : ISerializable
        {
            [Key(0)] private readonly double _value;

            [SerializationConstructor]
            public Double(double value)
            {
                _value = value;
            }

            public static implicit operator double(Double d)
            {
                return d?._value ?? default;
            }

            public static implicit operator double?(Double d)
            {
                return d?._value;
            }
        }

        [MessagePackObject]
        public class Decimal : ISerializable
        {
            [Key(0)] private readonly decimal _value;

            [SerializationConstructor]
            public Decimal(decimal value)
            {
                _value = value;
            }

            public static implicit operator decimal(Decimal d)
            {
                return d?._value ?? default;
            }

            public static implicit operator decimal?(Decimal d)
            {
                return d?._value;
            }
        }

        [MessagePackObject]
        public class Bool : ISerializable
        {
            [Key(0)] private readonly bool _value;

            [SerializationConstructor]
            public Bool(bool value)
            {
                _value = value;
            }

            public static implicit operator bool(Bool b)
            {
                return b?._value ?? default;
            }

            public static implicit operator bool?(Bool b)
            {
                return b?._value;
            }
        }
    }
}