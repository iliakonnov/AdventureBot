import MessagePack
import System.Collections.Generic
import System.Data
import Mono.Data.Sqlite
import AdventureBot

public static class Program:
    private LogEnabled as bool

    private def Log[of T](obj as T, comment as string) as T:
        if LogEnabled:
            print(string.Format("[{0}] {1} // {2}", obj.GetType().FullName, obj, comment))
        return obj

    private def GetKey(obj as object, key as string) as object:
        dict = obj cast Dictionary[of object, object]
        for kv in dict:
            if (kv.Key as string) == key:
                return Log(kv.Value, key)
        raise KeyNotFoundException()

    public def Main(args as (string)):
        oldPath = Log(System.IO.Path.GetFullPath(args[0]), "oldPath")
        newPath = Log(System.IO.Path.GetFullPath(args[1]), "newPath")
        LogEnabled = args.Length > 2

        oldDb = SqliteConnection(string.Format("Data Source = {0};Read Only=True", oldPath))  # v5
        oldDb.Open()

        newDb = SqliteConnection(string.Format("Data Source = {0}", newPath))  # v6
        newDb.Open()

        insCmd = newDb.CreateCommand()
        insCmd.CommandText = ("INSERT INTO" +
            " users(messenger, id, data, version, var_level, var_experience, var_gold, var_monsters, var_rooms)" +
            " VALUES (@msg, @id, @dat, @ver, @lvl, @exp, @gld, @mrs, @rms)")
        insCmd.Parameters.Add("@msg", DbType.Int32)
        insCmd.Parameters.Add("@id", DbType.Int64)
        insCmd.Parameters.Add("@dat", DbType.Binary)
        insCmd.Parameters.Add("@ver", DbType.Int32)
        insCmd.Parameters.Add("@lvl", DbType.Int32)
        insCmd.Parameters.Add("@exp", DbType.Decimal)
        insCmd.Parameters.Add("@gld", DbType.Decimal)
        insCmd.Parameters.Add("@mrs", DbType.Int32)
        insCmd.Parameters.Add("@rms", DbType.Int32)


        readCmd = oldDb.CreateCommand()
        readCmd.CommandText = "SELECT messenger, id, data, version FROM users"
        reader = readCmd.ExecuteReader()

        while reader.Read():
            messenger = reader.GetInt32(0)
            uid = reader.GetInt64(1)
            data = reader[2] cast (byte)
            version = reader.GetInt32(3)

            if version != 5:
                print(string.Format("Skipping user {0}/{1} with version {2}", messenger, uid, version))
                continue
            print(string.Format("\nBegin user {0}/{1}", messenger, uid))

            user = MessagePackSerializer.Deserialize[of object](data)

            userInfo = GetKey(user, "Info")
            userLevel = GetKey(userInfo, "Level")
            userStatistics = GetKey(userInfo, "Statistics")

            insCmd.Parameters["@msg"].Value = messenger
            insCmd.Parameters["@id"].Value = uid
            insCmd.Parameters["@dat"].Value = data
            insCmd.Parameters["@ver"].Value = version
            insCmd.Parameters["@lvl"].Value = GetKey(userLevel, "Level") cast int
            insCmd.Parameters["@exp"].Value = decimal.Parse(
                GetKey(userLevel, "ExpirenceCollected") cast string
            )
            insCmd.Parameters["@gld"].Value = decimal.Parse(
                GetKey(userInfo, "_gold") cast string
            )
            insCmd.Parameters["@mrs"].Value = GetKey(userStatistics, "MonsterCount") cast int
            insCmd.Parameters["@rms"].Value = GetKey(userStatistics, "RoomsCount") cast int
            insCmd.ExecuteNonQuery()

public def Main(args as (string)):
    # Entry point
    Program.Main(args)
