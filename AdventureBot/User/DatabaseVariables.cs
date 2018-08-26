using System;
using System.Collections.Generic;
using System.Data;
using System.Linq.Expressions;
using System.Reflection;
using System.Runtime.InteropServices;
using System.Text;
using Mono.Data.Sqlite;

namespace AdventureBot.User
{
    [AttributeUsage(AttributeTargets.Property)]
    public class DbColumnAttribute : Attribute
    {
        public string Name { get; }
        public DbType Type { get; }
        public string TypeString { get; }

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
                default:
                    throw new ArgumentOutOfRangeException();
            }
        }
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

        public void Fill(DatabaseVariables variables)
        {
            Level = variables.Level;
            Experience = variables.Experience;
            Gold = variables.Gold;
            Monsters = variables.Monsters;
            Rooms = variables.Rooms;
        }

        internal class Deserializer
        {
            private Deserializer()
            {
            }

            private int _level;
            private int _experience;
            private int _gold;
            private int _monstersKilled;
            private int _rooms;

            public static Deserializer Create(SqliteDataReader reader)
            {
                return new Deserializer
                {
                    _level = reader.GetOrdinal(GetColumn(v => v.Level).Name),
                    _experience = reader.GetOrdinal(GetColumn(v => v.Experience).Name),
                    _gold = reader.GetOrdinal(GetColumn(v => v.Gold).Name),
                    _monstersKilled = reader.GetOrdinal(GetColumn(v => v.Monsters).Name),
                    _rooms = reader.GetOrdinal(GetColumn(v => v.Rooms).Name)
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
                    Rooms = reader.GetInt32(_rooms)
                };
            }
        }

        public static (DbColumnAttribute, Func<DatabaseVariables, object>)[] GetColumns()
        {
            var getters = new Expression<Func<DatabaseVariables, object>>[]
            {
                v => v.Level,
                v => v.Experience,
                v => v.Gold,
                v => v.Monsters,
                v => v.Rooms
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
    }
}