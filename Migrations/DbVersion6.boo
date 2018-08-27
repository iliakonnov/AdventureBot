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

    public def Main(args as (string)):
        dbPath = Log(System.IO.Path.GetFullPath(args[0]), "dbPath")
        LogEnabled = args.Length > 1

        dbConn = SqliteConnection(string.Format("Data Source = {0}", dbPath))  # v6
        dbConn.Open()

        cmd = dbConn.CreateCommand()
        cmd.CommandText = "ALTER TABLE users ADD COLUMN var_lastMessage DATETIME"
        cmd.ExecuteNonQuery()

        updateCmd = dbConn.CreateCommand()
        updateCmd.Parameters.Add("@date", DbType.DateTime).Value = System.DateTime.MinValue
        updateCmd.CommandText = 'UPDATE users SET var_lastMessage = @date'
        updateCmd.ExecuteNonQuery()

public def Main(args as (string)):
    # Entry point
    Program.Main(args)
