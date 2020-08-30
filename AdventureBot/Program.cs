﻿using System;
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
            Logger.Info("Saving variables...");
            GlobalVariables.Flush();
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

            Logger.Info("Working!");

            // To allow long strings
            Console.SetIn(new StreamReader(Console.OpenStandardInput(),
                Console.InputEncoding,
                false,
                16384));

            var console = GetConsole();
            var forceContinue = false;
            Console.CancelKeyPress += (sender, args) =>
            {
                args.Cancel = true;
                Console.Error.WriteLine("\nUse `/q` to quit.");
            };

            while (_work)
            {
                try
                {
                    console.ReadEvalPrintLoop();
                }
                catch (Exception e)
                {
                    Console.WriteLine(e);
                    continue;
                }

                if (!forceContinue)
                {
                    break;
                }

                Console.WriteLine("Restarting interpreter...");
                forceContinue = false;

                Exit();
            }
        }

        private static InteractiveInterpreterConsole GetConsole()
        {
            var result = new InteractiveInterpreterConsole {DisableAutocompletion = false};
            result.Eval("import AdventureBot as adv; import AdventureBot.DebugHelpers as dbg");
            Console.WriteLine("AdventureBot available as `adv`; DebugHelpers available as `dbg`");
            return result;
        }
    }
}