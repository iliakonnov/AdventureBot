using System;
using System.Collections.Generic;
using System.Data;
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

        public static UserData LoadUserData(UserId id)
        {
            UserData Query(SqliteCommand command)
            {
                command.CommandText = "SELECT data, version FROM users WHERE id=@user_id AND messenger=@messenger";
                command.Parameters.AddWithValue("@messenger", id.Messenger);
                command.Parameters.AddWithValue("@user_id", id.Id);

                using (var reader = command.ExecuteReader())
                {
                    var dataPos = reader.GetOrdinal("data");
                    var versionPos = reader.GetOrdinal("version");
                    if (!reader.Read())
                    {
                        goto NotFound;
                    }

                    var value = reader[dataPos];
                    if (value == null || Convert.IsDBNull(value))
                    {
                        goto NotFound;
                    }

                    return new UserData(id, (byte[]) value, reader.GetInt32(versionPos));
                }

                NotFound:
                // User not found in database.
                return new UserData(id);
            }

            return QueryHelper(Query);
        }

        public static void SaveUsers(IEnumerable<UserData> users)
        {
            int Query(SqliteCommand command)
            {
                command.CommandText =
                    "INSERT OR REPLACE INTO users (messenger, id, data, version) " +
                    "VALUES (@messenger, @user_id, @data, @version)";

                var messengerParam = command.Parameters.Add("@messenger", DbType.Int32);
                var idParam = command.Parameters.Add("@user_id", DbType.Int64);
                var dataParam = command.Parameters.Add("@data", DbType.Binary);
                var versionParam = command.Parameters.Add("@version", DbType.Int32);

                var cnt = 0;
                foreach (var user in users)
                {
                    cnt++;

                    messengerParam.Value = user.Id.Messenger;
                    idParam.Value = user.Id.Id;
                    dataParam.Value = user.Data;
                    versionParam.Value = user.Version;
                    command.ExecuteNonQuery();
                }

                return cnt;
            }

            var beginTime = DateTimeOffset.Now;
            var count = QueryHelper(Query);
            if (count != 0)
            {
                Logger.Info("Flushed {count} users in {time}", count, DateTimeOffset.Now - beginTime);
            }
        }

        private static Void InitailizeTables(SqliteCommand command)
        {
            command.CommandText =
                @"CREATE TABLE IF NOT EXISTS `users` (
                    `messenger`	INTEGER,
                    `id`	    INTEGER,
                    `data`	    BLOB,
                    `version`	INTEGER,
                    PRIMARY KEY(`messenger`, `id`)
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