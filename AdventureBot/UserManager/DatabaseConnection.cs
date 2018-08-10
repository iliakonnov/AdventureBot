using System;
using System.Collections.Generic;
using System.Data;
using System.IO;
using MessagePack;
using MessagePack.ImmutableCollection;
using MessagePack.Resolvers;
using Mono.Data.Sqlite;
using NLog;

namespace AdventureBot.UserManager
{
    public static class DatabaseConnection
    {
        private static readonly Logger Logger = LogManager.GetCurrentClassLogger();
        private static readonly SqliteConnection Connection;

        static DatabaseConnection()
        {
            var connectionString = $"Data Source = {Configuration.Config["database"]};";
            Connection = new SqliteConnection(connectionString);
            Connection.Open();
            QueryHelper(InitailizeTables);

            CompositeResolver.RegisterAndSetAsDefault(
                ImmutableCollectionResolver.Instance,
                StandardResolverAllowPrivate.Instance
            );
        }

        private static T QueryHelper<T>(QueryCallback<T> callback)
        {
            lock (Connection)
            {
                using (var command = Connection.CreateCommand())
                using (var transaction = Connection.BeginTransaction())
                {
                    command.Transaction = transaction;

                    var result = callback(command);

                    transaction.Commit();
                    return result;
                }
            }
        }

        public static List<UserId> GetUsersList(int? messengerId = null)
        {
            List<UserId> Query(SqliteCommand command)
            {
                var result = new List<UserId>();

                command.CommandText =
                    "SELECT id, messenger FROM users WHERE (@messenger is null or messenger = @messenger)";
                command.Parameters.AddWithValue("@messenger", messengerId);
                using (var reader = command.ExecuteReader())
                {
                    var idPos = reader.GetOrdinal("id");
                    var messengerPos = reader.GetOrdinal("messenger");
                    while (reader.Read())
                    {
                        result.Add(new UserId(reader.GetInt32(messengerPos), reader.GetInt64(idPos)));
                    }
                }

                return result;
            }

            return QueryHelper(Query);
        }

        public static User.User LoadUser(UserId id)
        {
            User.User Query(SqliteCommand command)
            {
                command.CommandText = "SELECT data FROM users WHERE id=@user_id AND messenger=@messenger";
                command.Parameters.AddWithValue("@messenger", id.Messenger);
                command.Parameters.AddWithValue("@user_id", id.Id);

                using (var reader = command.ExecuteReader())
                {
                    var dataPos = reader.GetOrdinal("data");
                    if (!reader.Read())
                    {
                        goto NotFound;
                    }

                    var value = reader[dataPos];
                    if (value == null || Convert.IsDBNull(value))
                    {
                        goto NotFound;
                    }

                    var userdata = (byte[]) value;
                    try
                    {
                        return MessagePackSerializer.Deserialize<User.User>(userdata);
                    }
                    catch (Exception e)
                    {
                        var filename = $"{id.Messenger}_{id.Id}.userdump";
                        File.WriteAllBytes(filename, userdata);
                        Logger.Error(e, $"Cannot deserialize user {id}. Dump saved to {filename}");
                    }
                }

                NotFound:
                // User not found in database.
                return new User.User(id);
            }

            return QueryHelper(Query);
        }

        public static void SaveUsers(IEnumerable<User.User> users)
        {
            int Query(SqliteCommand command)
            {
                command.CommandText =
                    "INSERT OR REPLACE INTO users (messenger, id, data) VALUES (@messenger, @user_id, @data)";

                var messengerParam = command.Parameters.Add("@messenger", DbType.Int32);
                var idParam = command.Parameters.Add("@user_id", DbType.Int64);
                var dataParam = command.Parameters.Add("@data", DbType.Binary);

                var cnt = 0;
                foreach (var user in users)
                {
                    cnt++;

                    messengerParam.Value = user.Info.UserId.Messenger;
                    idParam.Value = user.Info.UserId.Id;
                    dataParam.Value = MessagePackSerializer.Serialize(user);
                    command.ExecuteNonQuery();
                }

                return cnt;
            }

            var beginTime = DateTimeOffset.Now;
            var count = QueryHelper(Query);
            if (count != 0)
            {
                Logger.Info($"Flushed {count} users in {DateTimeOffset.Now - beginTime}");
            }
        }

        private static Void InitailizeTables(SqliteCommand command)
        {
            command.CommandText =
                @"CREATE TABLE IF NOT EXISTS `users` (
                    `messenger`	INTEGER,
                    `id`	INTEGER,
                    `data`	BLOB,
                    PRIMARY KEY(`id`)
                );";
            command.ExecuteNonQuery();
            return new Void();
        }

        private struct Void
        {
        }

        private delegate T QueryCallback<out T>(SqliteCommand command);
    }
}