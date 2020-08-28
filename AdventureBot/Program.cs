using System;
using System.Linq;
using System.Management.Automation.Runspaces;
using System.Reflection;
using System.Text;
using AdventureBot.Analysis;
using AdventureBot.Item;
using AdventureBot.Messenger;
using AdventureBot.ObjectManager;
using AdventureBot.Quest;
using AdventureBot.Room;
using AdventureBot.UserManager;
using Namotion.Reflection;
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

            var iss = InitialSessionState.CreateDefault2();
            var help = new StringBuilder("Welcome to adventure control panel. Here you can:\n");
            foreach (var method in typeof(DebugHelpers).GetMethods().Where(m => m.DeclaringType != typeof(object)))
            {
                var args = new StringBuilder();
                var arg_help = new StringBuilder();
                var parameters = method.GetParameters();
                for (int i = 0; i < parameters.Length; i++)
                {
                    args.Append(i == 0 ? "$args[0]" : $", $args[{i}]");
                    var arg = $"{parameters[i].Name}: {parameters[i].ParameterType.Name}";
                    arg_help.Append(i == 0 ? arg : $", {arg}");
                }
                var definition = $"[AdventureBot.DebugHelpers]::{method.Name}({args})";
                help.AppendLine($"  - {method.Name}({arg_help}): {method.GetXmlDocsSummary()}");
                iss.Commands.Add(new SessionStateFunctionEntry(method.Name, definition));
            }
            Microsoft.PowerShell.ConsoleShell.Start(iss, help.ToString(), "", new string[0]);

            Exit();
        }
    }
}