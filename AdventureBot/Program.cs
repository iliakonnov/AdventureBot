using System;
using System.IO;
using System.Reflection;
using System.Threading;
using AdventureBot.Item;
using AdventureBot.Messenger;
using AdventureBot.ObjectManager;
using AdventureBot.Room;
using IronPython.Hosting;
using Microsoft.Extensions.Configuration;
using Microsoft.Scripting.Hosting.Shell;
using NLog;
using Yandex.Metrica;

namespace AdventureBot
{
    internal class Program
    {
        private static readonly Logger Logger = LogManager.GetCurrentClassLogger();

        private static void Main(string[] args)
        {
            Logger.Debug("Loading...");

            var metrika = Configuration.Config.GetSection("metrika");
            YandexMetricaFolder.SetCurrent(metrika.GetValue<string>("folder"));
            YandexMetrica.Config.CrashTracking = true;
            YandexMetrica.Activate(metrika.GetValue<string>("token"));


            ObjectManager<IRoom>.Instance.RegisterManager<RoomManager>();
            ObjectManager<IItem>.Instance.RegisterManager<ItemManager>();
            ObjectManager<IMessenger>.Instance.RegisterManager<MessengerManager>();

            Logger.Debug("Loading objects...");
            foreach (var assembly in Configuration.Config.GetSection("assemblies").GetChildren())
            {
                MainManager.Instance.LoadAssembly(assembly.Value);
            }

            foreach (var python in Configuration.Config.GetSection("python").GetChildren())
            {
                MainManager.Instance.LoadPython(Path.GetDirectoryName(python.Value), Path.GetFileName(python.Value));
            }

            MainManager.Instance.LoadAssembly(Assembly.GetExecutingAssembly());


            Logger.Info("Working!");

            // To allow long strings
            Console.SetIn(new StreamReader(Console.OpenStandardInput(),
                Console.InputEncoding,
                false,
                16384));

            var commandLine = new PythonCommandLine();
            var engine = Python.CreateEngine();
            engine.Runtime.LoadAssembly(Assembly.GetExecutingAssembly());
            commandLine.Run(engine, new SuperConsole(commandLine, true), new PythonConsoleOptions
            {
                AutoIndent = true,
                ColorfulConsole = true,
                TabCompletion = true
            });

            Logger.Info("Saving users...");
            UserManager.Instance.Flush();
            Logger.Debug("Done!");
            Thread.Sleep(500); // Finish logging
            Environment.Exit(0);
        }
    }
}