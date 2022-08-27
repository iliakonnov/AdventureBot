using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using AdventureBot.User;
using Microsoft.Data.Sqlite;
using NLog;

namespace AdventureBot.UserManager;

public static class DatabaseConnection
{
    private static readonly Logger Logger = LogManager.GetCurrentClassLogger();
    private static readonly SqliteConnection Connection;

    static DatabaseConnection()
    {
        var connectionString = $"Data Source = {Configuration.Config["database"]}";
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
                "SELECT * FROM users WHERE (@messenger is null or messenger = @messenger)";
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

    public static List<UserData> QueryUsers(List<(DbColumnAttribute, bool)> order,
        List<(DbColumnAttribute, string, object)> filter,
        int? limit)
    {
        List<UserData> Query(SqliteCommand command)
        {
            var result = new List<UserData>();

            command.CommandText = "SELECT * FROM users";

            var cmd = new StringBuilder("SELECT * FROM users");
            var param = 0;
            if (filter != null && filter.Count != 0)
            {
                cmd.Append(" WHERE");
                var filterSql = new List<string>();
                foreach (var condition in filter)
                {
                    var paramName = $"@param{param++}";
                    filterSql.Add($" {condition.Item1.Name}{condition.Item2}{paramName}");
                    command.Parameters.AddWithValue(paramName, condition.Item3);
                }

                cmd.Append(string.Join(" AND ", filterSql));
            }

            if (order != null && order.Count != 0)
            {
                cmd.Append(" ORDER BY");
                var orderSql = new List<string>();
                foreach (var kv in order)
                {
                    var direction = kv.Item2 ? "ASC" : "DESC";
                    orderSql.Add($" {kv.Item1.Name} {direction}");
                }

                cmd.Append(string.Join(",", orderSql));
            }

            if (limit != null && limit != 0)
            {
                cmd.Append($" LIMIT {limit}");
            }

            command.CommandText = cmd.ToString();

            using (var reader = command.ExecuteReader())
            {
                var idPos = reader.GetOrdinal("id");
                var dataPos = reader.GetOrdinal("data");
                var messengerPos = reader.GetOrdinal("messenger");
                var versionPos = reader.GetOrdinal("version");
                var deserializer = DatabaseVariables.Deserializer.Create(reader);

                while (reader.Read())
                {
                    result.Add(new UserData(
                        new UserId(reader.GetInt32(messengerPos), reader.GetInt64(idPos)),
                        (byte[]) reader[dataPos],
                        deserializer.Deserialize(reader),
                        reader.GetInt32(versionPos)
                    ));
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
            command.CommandText = "SELECT * FROM users WHERE id=@user_id AND messenger=@messenger";
            command.Parameters.AddWithValue("@messenger", id.Messenger);
            command.Parameters.AddWithValue("@user_id", id.Id);

            using (var reader = command.ExecuteReader())
            {
                var variablesDeserializer = DatabaseVariables.Deserializer.Create(reader);
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

                return new UserData(id,
                    (byte[]) value,
                    variablesDeserializer.Deserialize(reader),
                    reader.GetInt32(versionPos));
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
            var columns = DatabaseVariables.GetColumns();
            var varNames = new List<string>();
            var varValues = new List<string>();
            var parameters = new List<(SqliteParameter, Func<DatabaseVariables, object>)>();
            for (var i = 0; i < columns.Length; i++)
            {
                var column = columns[i];
                varNames.Add($"{column.Item1.Name}");
                var paramName = $"@param{i}";
                varValues.Add(paramName);
                parameters.Add((command.Parameters.Add(paramName, column.Item1.Type), column.Item2));
            }

            command.CommandText =
                $"INSERT OR REPLACE INTO users (messenger, id, data, version, {string.Join(", ", varNames)}) " +
                $"VALUES (@messenger, @user_id, @data, @version, {string.Join(", ", varValues)})";

            var messengerParam = command.Parameters.Add("@messenger", SqliteType.Integer);
            var idParam = command.Parameters.Add("@user_id", SqliteType.Integer);
            var dataParam = command.Parameters.Add("@data", SqliteType.Blob);
            var versionParam = command.Parameters.Add("@version", SqliteType.Integer);

            var cnt = 0;
            foreach (var user in users)
            {
                cnt++;

                foreach (var param in parameters)
                {
                    param.Item1.Value = param.Item2(user.Variables);
                }

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
        var variables = string.Join(
            ", ",
            DatabaseVariables.GetColumns()
                .Select(db => $"`{db.Item1.Name}` {db.Item1.TypeString}")
        );
        command.CommandText =
            "CREATE TABLE IF NOT EXISTS `users` (" +
            "    `messenger`	INTEGER," +
            "    `id`		INTEGER," +
            "    `data`		BLOB," +
            "    `version`	INTEGER," +
            $"    {variables}," +
            "    PRIMARY KEY(`messenger`, `id`)" +
            ");";
        command.ExecuteNonQuery();
        return new Void();
    }

    private struct Void
    {
    }

    private delegate T QueryCallback<out T>(SqliteCommand command);
}