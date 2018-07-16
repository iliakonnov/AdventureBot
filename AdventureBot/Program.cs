using System;
using System.IO;
using System.Linq;
using System.Reflection;
using System.Threading;
using AdventureBot.Item;
using AdventureBot.Messenger;
using AdventureBot.ObjectManager;
using AdventureBot.Room;
using AdventureBot.User;
using MessagePack;
using MessagePack.ImmutableCollection;
using MessagePack.Resolvers;
using Microsoft.Extensions.Configuration;
using Microsoft.Extensions.Logging;
using ItemManager = AdventureBot.Item.ItemManager;
using RoomManager = AdventureBot.Room.RoomManager;

namespace AdventureBot
{
    class Program
    {
        private static readonly ILogger Logger = AdventureBot.Logger.CreateLogger<Program>();
        
        static void Main(string[] args)
        {
            Logger.LogInformation("Loading...");

            var metrika = Configuration.Config.GetSection("metrika");
            Yandex.Metrica.YandexMetricaFolder.SetCurrent(metrika.GetValue<string>("folder"));
            Yandex.Metrica.YandexMetrica.Config.CrashTracking = true;
            Yandex.Metrica.YandexMetrica.Activate(metrika.GetValue<string>("token"));
            
            
            ObjectManager<IRoom>.Instance.RegisterManager<RoomManager>();
            ObjectManager<IItem>.Instance.RegisterManager<ItemManager>();
            ObjectManager<IMessenger>.Instance.RegisterManager<MessengerManager>();

            Logger.LogInformation("Loading objects...");
            foreach (var assembly in Configuration.Config.GetSection("assemblies").GetChildren())
            {
                MainManager.Instance.LoadAssembly(assembly.Value);
            }

            MainManager.Instance.LoadAssembly(Assembly.GetExecutingAssembly());

            Logger.LogInformation("Working!");

            Console.CancelKeyPress += (sender, eventArgs) =>
            {
                Exit();
            };
            
            // To allow long strings
            Console.SetIn(new StreamReader(Console.OpenStandardInput(),
                Console.InputEncoding,
                false,
                bufferSize: 16384));

            while (true)
            {
                var command = Console.ReadLine();
                if (command == null)
                {
                    continue;
                }
                
                var splitted = command.Split(' ');
                switch (splitted[0])
                {
                    case "stop":
                    {
                        Exit();
                        break;
                    }
                    case "flush":
                    {
                        UserManager.Instance.Flush();
                        break;
                    }
                    case "dump":
                    {
                        if (
                            splitted.Length == 3
                            && int.TryParse(splitted[1], out var messenger)
                            && long.TryParse(splitted[2], out var uid)
                        )
                        {
                            var userId = new UserId(messenger, uid);
                            var user = UserManager.Instance.Get(userId, safe: false);
                            var filename = $"{userId.Id}@{userId.Messenger}.bin";
                            System.IO.File.WriteAllBytes(filename, MessagePackSerializer.Serialize(user));
                            Console.WriteLine($"Saved to {filename}");
                            break;
                        }

                        goto default;
                    }
                    case "load":
                    {
                        if (splitted.Length == 2)
                        {
                            var bytes = System.IO.File.ReadAllBytes(splitted[1]);
                            var user = MessagePackSerializer.Deserialize<User.User>(bytes);
                            UserManager.Instance.Save(user);
                            Console.WriteLine($"Loaded {user.Info.UserId}");
                            break;
                        }

                        goto default;
                    }
                    case "json":
                    {
                        if (
                            splitted.Length == 3
                            && int.TryParse(splitted[1], out var messenger)
                            && long.TryParse(splitted[2], out var uid)
                        )
                        {
                            var userId = new UserId(messenger, uid);
                            var user = UserManager.Instance.Get(userId, safe: false);
                            var filename = $"{userId.Id}@{userId.Messenger}.json";
                            System.IO.File.WriteAllText(filename, MessagePackSerializer.ToJson(user));
                            Console.WriteLine($"Saved to {filename}");
                            break;
                        }

                        goto default;
                    }
                    case "send":
                    {
                        if (
                            splitted.Length > 3
                            && int.TryParse(splitted[1], out var messenger)
                            && long.TryParse(splitted[2], out var uid)
                        )
                        {
                            var userId = new UserId(messenger, uid);

                            using (var ctx = new UserContext(userId))
                            {
                                User.User user = ctx;
                                if (user.MessageManager.ChatId.Messenger == 0)
                                {
                                    Console.WriteLine("Cannot send message to this user");
                                }
                                else
                                {
                                    user.MessageManager.SendImmediately(new SentMessage
                                    {
                                        Text = string.Join(" ", splitted.Skip(3))
                                    });
                                    Console.WriteLine("Ok");
                                }
                            }
                            break;
                        }

                        goto default;
                    }
                    default:
                    {
                        Console.WriteLine("Unknown command. ");
                        Console.WriteLine("    stop -- stops bot");
                        Console.WriteLine("    flush -- flushes all users to disk");
                        Console.WriteLine("    json <messenger_id> <user_id> -- dumps user to json");
                        Console.WriteLine("    dump <messenger_id> <user_id> -- dumps user to binary");
                        Console.WriteLine("Locking commands:");
                        Console.WriteLine("    send <messenger_id> <user_id> <message -- Sends message to user");
                        Console.WriteLine("Unsafe commands:");
                        Console.WriteLine("    load <path.bin> -- loads user from binary");
                        break;
                    }
                }
            }
        }

        static void Exit()
        {
            Logger.LogInformation("Saving users...");
            UserManager.Instance.Flush();
            Logger.LogInformation("Done!");
            Thread.Sleep(500);  // Finish logging
            Environment.Exit(0);
        }
    }
}