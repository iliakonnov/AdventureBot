using System;
using System.IO;
using System.Reflection;
using System.Threading;
using AdventureBot.Analysis;
using AdventureBot.Item;
using AdventureBot.Messenger;
using AdventureBot.ObjectManager;
using AdventureBot.Quest;
using AdventureBot.Room;
using AdventureBot.UserManager;
using IronPython.Hosting;
using Microsoft.Scripting.Hosting.Shell;
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
            try
            {
                Logger.Error(args.ExceptionObject as Exception, "Unhandled error");
            }
            catch (Exception)
            {
                // ignored
            }

            Exit();
        };
        AppDomain.CurrentDomain.ProcessExit += (sender, args) => { Exit(); };

        Logger.Debug("Loading...");
        Initialize();

        Logger.Info("Working!");

        var repl = new PythonCommandLine();
        var engine = Python.CreateEngine();
        var console = new SuperConsole(new PythonCommandLine(), true, SuperConsole.EditMode.Windows);
        var options = new PythonConsoleOptions
        {
            AutoIndent = true,
        };

        engine.Runtime.LoadAssembly(Assembly.GetExecutingAssembly());
        repl.Run(engine, console, options);
    }
}