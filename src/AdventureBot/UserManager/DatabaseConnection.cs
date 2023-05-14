using System;
using System.Collections.Concurrent;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using AdventureBot.User;
using Npgsql;
using NpgsqlTypes;

namespace AdventureBot.UserManager;

public static class DatabaseConnection
{
    private static readonly string ConnectionString;

    static DatabaseConnection()
    {
        ConnectionString = Configuration.Config["connection_string"];
        QueryHelper(InitailizeTables);
    }

    internal static NpgsqlConnection GetConnection()
    {
        var connection = new NpgsqlConnection(ConnectionString);
        connection.Open();
        return connection;
    }

    private static T QueryHelper<T>(QueryCallback<T> callback, NpgsqlTransaction transaction = null)
    {
        var connection = GetConnection();
        using var command = connection.CreateCommand();
        T result;

        if (transaction == null)
        {
            using var trans = connection.BeginTransaction();
            command.Transaction = trans;
            result = callback(command);
            trans.Commit();
        }
        else
        {
            command.Transaction = transaction;
            result = callback(command);
        }

        return result;
    }

    public static List<UserId> GetUsersList(int? messengerId = null)
    {
        List<UserId> Query(NpgsqlCommand command)
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
        List<UserData> Query(NpgsqlCommand command)
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

    public static UserData LoadUserData(UserId id, NpgsqlTransaction transaction = null)
    {
        UserData Query(NpgsqlCommand command)
        {
            command.CommandText = "SELECT * FROM users WHERE id=@user_id AND messenger=@messenger FOR NO KEY UPDATE";
            command.Parameters.AddWithValue("@messenger", id.Messenger);
            command.Parameters.AddWithValue("@user_id", id.Id);

            using var reader = command.ExecuteReader();
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

            NotFound:
            // User not found in database.
            return new UserData(id);
        }

        return QueryHelper(Query, transaction);
    }

    public static void SaveUser(UserData user, NpgsqlTransaction transaction = null)
    {
        Void Query(NpgsqlCommand command)
        {
            var columns = DatabaseVariables.GetColumns();
            var varNames = new List<string>();
            var varValues = new List<string>();
            var varUpdates = new List<string>();
            var parameters = new List<(NpgsqlParameter, Func<DatabaseVariables, object>)>();
            for (var i = 0; i < columns.Length; i++)
            {
                var column = columns[i];
                varNames.Add($"{column.Item1.Name}");
                var paramName = $"@param{i}";
                varValues.Add(paramName);
                varUpdates.Add($"{column.Item1.Name} = {paramName}");
                parameters.Add((command.Parameters.Add(paramName, column.Item1.Type), column.Item2));
            }

            command.CommandText =
                $"INSERT INTO users (messenger, id, data, version, {string.Join(", ", varNames)}) " +
                $"VALUES (@messenger, @user_id, @data, @version, {string.Join(", ", varValues)}) " +
                "ON CONFLICT (messenger, id) DO UPDATE SET " +
                $" messenger=@messenger, id=@user_id, data=@data, version=@version, {string.Join(", ", varUpdates)}";

            var messengerParam = command.Parameters.Add("@messenger", NpgsqlDbType.Integer);
            var idParam = command.Parameters.Add("@user_id", NpgsqlDbType.Integer);
            var dataParam = command.Parameters.Add("@data", NpgsqlDbType.Bytea);
            var versionParam = command.Parameters.Add("@version", NpgsqlDbType.Integer);
            
            foreach (var param in parameters)
            {
                param.Item1.Value = param.Item2(user.Variables);
            }

            messengerParam.Value = user.Id.Messenger;
            idParam.Value = user.Id.Id;
            dataParam.Value = user.Data;
            versionParam.Value = user.Version;
            command.ExecuteNonQuery();

            return new Void();
        }

        QueryHelper(Query, transaction);
    }

    private static Void InitailizeTables(NpgsqlCommand command)
    {
        var variables = string.Join(
            ", ",
            DatabaseVariables.GetColumns()
                .Select(db => $"{db.Item1.Name} {db.Item1.TypeString}")
        );
        command.CommandText =
            "CREATE TABLE IF NOT EXISTS users (" +
            "    messenger	INTEGER," +
            "    id 		INTEGER," +
            "    data		bytea," +
            "    version	INTEGER," +
            $"    {variables}," +
            "    PRIMARY KEY(messenger, id)" +
            ");";
        command.ExecuteNonQuery();
        return new Void();
    }

    private struct Void
    {
    }

    private delegate T QueryCallback<out T>(NpgsqlCommand command);
}