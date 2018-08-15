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
using Boo.Lang.Interpreter;
using NLog;

namespace AdventureBot
{
    internal static class Program
    {
        private static readonly Logger Logger = LogManager.GetCurrentClassLogger();

        private static bool _work = true;

        private static void Exit()
        {
            Logger.Info("Saving users...");
            Cache.Instance.FlushAll();
            Logger.Debug("Done!");
            LogManager.Shutdown();
            _work = false;
        }

        private static void Main()
        {
            Events.Start();

            AppDomain.CurrentDomain.UnhandledException += (sender, args) =>
            {
                Logger.Error(args.ExceptionObject as Exception, "Unhandled error");
                _work = false;
                Exit();
            };

            Logger.Debug("Loading...");

            ObjectManager<IRoom>.Instance.RegisterManager<RoomManager>();
            ObjectManager<IItem>.Instance.RegisterManager<ItemManager>();
            ObjectManager<IQuest>.Instance.RegisterManager<QuestManager>();
            ObjectManager<IMessenger>.Instance.RegisterManager<MessengerManager>();
            ObjectManager<IMigrator>.Instance.RegisterManager<MigratorManager>();

            Logger.Debug("Loading objects...");
            foreach (var assembly in Configuration.Config.GetSection("assemblies").GetChildren())
            {
                MainManager.Instance.LoadAssembly(assembly.Value);
            }

            MainManager.Instance.LoadAssembly(Assembly.GetExecutingAssembly());

            Logger.Info("Working!");

            // To allow long strings
            Console.SetIn(new StreamReader(Console.OpenStandardInput(),
                Console.InputEncoding,
                false,
                16384));

            while (_work)
            {
                try
                {
                    var console = new InteractiveInterpreterConsole();
                    console.ReadEvalPrintLoop();
                }
                catch (Exception e)
                {
                    Console.WriteLine(e);
                    continue;
                }

                break;
            }

            Exit();
        }
    }
}