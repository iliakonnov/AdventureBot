using System;
using System.IO;
using System.Linq;
using System.Reflection;
using System.Threading;
using AdventureBot.Item;
using AdventureBot.Messenger;
using AdventureBot.ObjectManager;
using AdventureBot.Room;
using MessagePack;
using Microsoft.Extensions.Configuration;
using Microsoft.Extensions.Logging;
using Yandex.Metrica;

namespace AdventureBot
{
    internal class Program
    {
        private static readonly ILogger Logger = AdventureBot.Logger.CreateLogger<Program>();

        private static void Main(string[] args)
        {
            Logger.LogInformation("Loading...");

            var metrika = Configuration.Config.GetSection("metrika");
            YandexMetricaFolder.SetCurrent(metrika.GetValue<string>("folder"));
            YandexMetrica.Config.CrashTracking = true;
            YandexMetrica.Activate(metrika.GetValue<string>("token"));


            ObjectManager<IRoom>.Instance.RegisterManager<RoomManager>();
            ObjectManager<IItem>.Instance.RegisterManager<ItemManager>();
            ObjectManager<IMessenger>.Instance.RegisterManager<MessengerManager>();

            Logger.LogInformation("Loading objects...");
            foreach (var assembly in Configuration.Config.GetSection("assemblies").GetChildren())
                MainManager.Instance.LoadAssembly(assembly.Value);

            MainManager.Instance.LoadAssembly(Assembly.GetExecutingAssembly());

            Logger.LogInformation("Working!");

            Console.CancelKeyPress += (sender, eventArgs) => { Exit(); };

            // To allow long strings
            Console.SetIn(new StreamReader(Console.OpenStandardInput(),
                Console.InputEncoding,
                false,
                16384));

            while (true)
            {
                var command = Console.ReadLine();
                if (command == null) continue;

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
                            var user = UserManager.Instance.Get(userId, false);
                            var filename = $"{userId.Id}@{userId.Messenger}.bin";
                            File.WriteAllBytes(filename, MessagePackSerializer.Serialize(user));
                            Console.WriteLine($"Saved to {filename}");
                            break;
                        }

                        goto default;
                    }
                    case "load":
                    {
                        if (splitted.Length == 2)
                        {
                            var bytes = File.ReadAllBytes(splitted[1]);
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
                            var user = UserManager.Instance.Get(userId, false);
                            var filename = $"{userId.Id}@{userId.Messenger}.json";
                            File.WriteAllText(filename, MessagePackSerializer.ToJson(user));
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
                    case "cheat":
                    {
                        if (
                            splitted.Length == 3
                            && int.TryParse(splitted[1], out var messenger)
                            && long.TryParse(splitted[2], out var uid)
                        )
                        {
                            var userId = new UserId(messenger, uid);

                            using (var ctx = new UserContext(userId))
                            {
                                User.User user = ctx;
                                user.Info.BaseStats = user.Info.MaxStats;
                                user.Info.RecalculateStats();
                            }

                            break;
                        }

                        goto default;
                    }
                    case "give":
                    {
                        if (
                            splitted.Length == 5
                            && int.TryParse(splitted[1], out var messenger)
                            && long.TryParse(splitted[2], out var uid)
                            && int.TryParse(splitted[4], out var count)
                        )
                        {
                            var userId = new UserId(messenger, uid);

                            using (var ctx = new UserContext(userId))
                            {
                                User.User user = ctx;
                                user.ItemManager.Add(new ItemInfo(splitted[3], count));
                            }

                            break;
                        }

                        goto default;
                    }
                    case "room":
                    {
                        if (
                            splitted.Length == 4
                            && int.TryParse(splitted[1], out var messenger)
                            && long.TryParse(splitted[2], out var uid)
                        )
                        {
                            var userId = new UserId(messenger, uid);

                            using (var ctx = new UserContext(userId))
                            {
                                User.User user = ctx;
                                user.RoomManager.Go(splitted[3]);
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
                        Console.WriteLine("    send <messenger_id> <user_id> <message> -- Sends message to user");
                        Console.WriteLine("    cheat <messenger_id> <user_id> -- All stats to maximum");
                        Console.WriteLine("    give <messenger_id> <user_id> <item_id> <count> -- Gives item to user");
                        Console.WriteLine("    room <messenger_id> <user_id> <room_id> -- Travles user to room");
                        Console.WriteLine("Unsafe commands:");
                        Console.WriteLine("    load <path.bin> -- loads user from binary");
                        break;
                    }
                }
            }
        }

        private static void Exit()
        {
            Logger.LogInformation("Saving users...");
            UserManager.Instance.Flush();
            Logger.LogInformation("Done!");
            Thread.Sleep(500); // Finish logging
            Environment.Exit(0);
        }
    }
}