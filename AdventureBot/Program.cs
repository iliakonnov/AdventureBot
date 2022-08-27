using System;
using System.IO;
using System.Reflection;
using AdventureBot.Analysis;
using AdventureBot.Item;
using AdventureBot.Messenger;
using AdventureBot.ObjectManager;
using AdventureBot.Quest;
using AdventureBot.Room;
using AdventureBot.UserManager;
using NLog;

namespace AdventureBot;

internal static class Program
{
    private static readonly Logger Logger = LogManager.GetCurrentClassLogger();

    private static void Exit()
    {
        Logger.Info("Saving users...");
        Cache.Instance.FlushAll();
        Logger.Info("Saving variables...");
        GlobalVariables.Flush();
        Logger.Debug("Done!");
        LogManager.Shutdown();
        Environment.Exit(0);
    }

    public static void Initialize()
    {
        ObjectManager<IRoom>.Instance.RegisterManager<RoomManager>();
        ObjectManager<IRoot>.Instance.RegisterManager<RootManager>();
        ObjectManager<IItem>.Instance.RegisterManager<ItemManager>();
        ObjectManager<IQuest>.Instance.RegisterManager<QuestManager>();
        ObjectManager<IMessenger>.Instance.RegisterManager<MessengerManager>();
        ObjectManager<IMigrator>.Instance.RegisterManager<MigratorManager>();
        
        Logger.Debug("Loading objects...");
        MainManager.Instance.LoadAssembly(Assembly.GetExecutingAssembly());
        foreach (var assembly in Configuration.Config.GetSection("assemblies").GetChildren())
        {
            MainManager.Instance.LoadAssembly(assembly.Value);
        }

        Logger.Debug("Loading other...");

        ObjectManager<IMessenger>.Instance.Get<MessengerManager>().BeginPolling();
    }

    private static void Main()
    {
        Events.Start();

        AppDomain.CurrentDomain.UnhandledException += (sender, args) =>
        {
            Logger.Error(args.ExceptionObject as Exception, "Unhandled error");
            Exit();
        };

        Logger.Debug("Loading...");
        Initialize();

        Logger.Info("Working!");

        // To allow long strings
        Console.SetIn(new StreamReader(Console.OpenStandardInput(),
            Console.InputEncoding,
            false,
            16384));

        Console.CancelKeyPress += (sender, args) =>
        {
            args.Cancel = true;
            Console.Error.WriteLine("\nUse `/q` to quit.");
        };

        while (true)
        {
            Console.WriteLine("Working...");
            var cmd = Console.ReadLine();
            if (cmd != "/q")
            {
                Console.Error.WriteLine("Use `/q` to quit.");
            }
            else
            {
                break;
            }
        }

        Exit();
    }
}