using System;
using System.IO;
using System.Reflection;
using System.Threading;
using AdventureBot.Analysis;
using AdventureBot.Item;
using AdventureBot.Messenger;
using AdventureBot.ObjectManager;
using AdventureBot.Room;
using NLog;

namespace AdventureBot
{
    internal static class Program
    {
        private static readonly Logger Logger = LogManager.GetCurrentClassLogger();

        private static void Main()
        {
            Events.Start();

            Logger.Debug("Loading...");

            ObjectManager<IRoom>.Instance.RegisterManager<RoomManager>();
            ObjectManager<IItem>.Instance.RegisterManager<ItemManager>();
            ObjectManager<IMessenger>.Instance.RegisterManager<MessengerManager>();

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

            while (true)
            {
                try
                {
                    var console = new Boo.Lang.Interpreter.InteractiveInterpreterConsole();
                    console.ReadEvalPrintLoop();
                }
                catch (Exception e)
                {
                    Console.WriteLine(e);
                    continue;
                }
                break;
            }

            Logger.Info("Saving users...");
            UserManager.Cache.Instance.FlushAll();
            Logger.Debug("Done!");
            Thread.Sleep(500); // Finish logging
            Environment.Exit(0);
        }
    }
}