using System;
using System.Reflection;
using AdventureBot.Analysis;
using AdventureBot.Api;
using AdventureBot.Item;
using AdventureBot.Messenger;
using AdventureBot.ObjectManager;
using AdventureBot.Quest;
using AdventureBot.Room;
using AdventureBot.UserManager;
using EmbedIO.WebApi;
using IronPython.Hosting;
using Microsoft.Scripting.Hosting.Shell;
using NLog;
using Prometheus;

namespace AdventureBot;

internal static class Program
{
    private static readonly Logger Logger = LogManager.GetCurrentClassLogger();

    private static void Exit()
    {
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
        ObjectManager<WebApiController>.Instance.RegisterManager<ApiControllerManager>();

        Logger.Debug("Loading objects...");
        MainManager.Instance.LoadAssembly(Assembly.GetExecutingAssembly());
        foreach (var assembly in Configuration.Config.GetSection("assemblies").GetChildren())
        {
            MainManager.Instance.LoadAssembly(assembly.Value);
        }

        foreach (var python in Configuration.Config.GetSection("python").GetChildren())
        {
            MainManager.Instance.LoadPython(python.Value);
        }

        Logger.Debug("Loading other...");

        ObjectManager<IMessenger>.Instance.Get<MessengerManager>().BeginPolling();
        ObjectManager<WebApiController>.Instance.Get<ApiControllerManager>().RunAsync();
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

        var server = new MetricServer(hostname: "*", port: 9100);
        server.Start();

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