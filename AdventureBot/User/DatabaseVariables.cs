using System;
using System.Data;
using System.Linq.Expressions;
using System.Reflection;
using Mono.Data.Sqlite;

namespace AdventureBot.User
{
    [AttributeUsage(AttributeTargets.Property)]
    public class DbColumnAttribute : Attribute
    {
        public DbColumnAttribute(string name, DbType type)
        {
            Name = name;
            Type = type;
            switch (Type)
            {
                case DbType.Decimal:
                    TypeString = "INTEGER";
                    break;
                case DbType.Int32:
                    TypeString = "NUMERIC";
                    break;
                case DbType.DateTime:
                    TypeString = "DATETIME";
                    break;
                default:
                    throw new ArgumentOutOfRangeException();
            }
        }

        public string Name { get; }
        public DbType Type { get; }
        public string TypeString { get; }
    }

    public class DatabaseVariables
    {
        [DbColumn("var_level", DbType.Int32)] public int Level { get; internal set; }

        [DbColumn("var_experience", DbType.Decimal)]
        public decimal Experience { get; internal set; }

        [DbColumn("var_gold", DbType.Decimal)] public decimal Gold { get; internal set; } = 100;

        [DbColumn("var_monsters", DbType.Int32)]
        public int Monsters { get; internal set; }

        [DbColumn("var_rooms", DbType.Int32)] public int Rooms { get; internal set; }

        [DbColumn("var_lastMessage", DbType.DateTime)]
        public DateTime LastMessageRecived { get; internal set; }

        public void Fill(DatabaseVariables variables)
        {
            Level = variables.Level;
            Experience = variables.Experience;
            Gold = variables.Gold;
            Monsters = variables.Monsters;
            Rooms = variables.Rooms;
            LastMessageRecived = variables.LastMessageRecived;
        }

        public static (DbColumnAttribute, Func<DatabaseVariables, object>)[] GetColumns()
        {
            var getters = new Expression<Func<DatabaseVariables, object>>[]
            {
                v => v.Level,
                v => v.Experience,
                v => v.Gold,
                v => v.Monsters,
                v => v.Rooms,
                v => v.LastMessageRecived
            };
            var result = new (DbColumnAttribute, Func<DatabaseVariables, object>)[getters.Length];
            for (var i = 0; i < getters.Length; i++)
            {
                var getter = getters[i];
                result[i] = (GetColumn(getter), getter.Compile());
            }

            return result;
        }

        private static DbColumnAttribute GetColumn(Expression expression)
        {
            if (expression is UnaryExpression unaryExpression)
            {
                // Handle v => (object)(v.*); Convert
                return GetColumn(unaryExpression.Operand);
            }

            if (expression is MemberExpression memberExpression && memberExpression.Member is PropertyInfo prop)
            {
                return prop.GetCustomAttribute<DbColumnAttribute>();
            }

            throw new ArgumentException("Incorrect getter", nameof(expression));
        }

        public static DbColumnAttribute GetColumn(Expression<Func<DatabaseVariables, object>> getter)
        {
            return GetColumn(getter.Body);
        }

        internal class Deserializer
        {
            private int _experience;
            private int _gold;
            private int _lastMessageRecived;

            private int _level;
            private int _monstersKilled;
            private int _rooms;

            private Deserializer()
            {
            }

            public static Deserializer Create(SqliteDataReader reader)
            {
                return new Deserializer
                {
                    _level = reader.GetOrdinal(GetColumn(v => v.Level).Name),
                    _experience = reader.GetOrdinal(GetColumn(v => v.Experience).Name),
                    _gold = reader.GetOrdinal(GetColumn(v => v.Gold).Name),
                    _monstersKilled = reader.GetOrdinal(GetColumn(v => v.Monsters).Name),
                    _rooms = reader.GetOrdinal(GetColumn(v => v.Rooms).Name),
                    _lastMessageRecived = reader.GetOrdinal(GetColumn(v => v.LastMessageRecived).Name)
                };
            }

            internal DatabaseVariables Deserialize(IDataRecord reader)
            {
                return new DatabaseVariables
                {
                    Level = reader.GetInt32(_level),
                    Experience = reader.GetDecimal(_experience),
                    Gold = reader.GetDecimal(_gold),
                    Monsters = reader.GetInt32(_monstersKilled),
                    Rooms = reader.GetInt32(_rooms),
                    LastMessageRecived = reader.GetDateTime(_lastMessageRecived)
                };
            }
        }
    }
}