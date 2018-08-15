using System;
using System.Collections.Generic;
using System.Linq;
using AdventureBot.Messenger;
using AdventureBot.User;
using Microsoft.Extensions.Configuration;
using NLog;
using Yandex.Metrica;

namespace AdventureBot.Analysis
{
    public static class Events
    {
        private static readonly Logger Logger = LogManager.GetCurrentClassLogger();

        static Events()
        {
            var metrika = Configuration.Config.GetSection("metrika");
            YandexMetricaFolder.SetCurrent(metrika.GetValue<string>("folder"));
            YandexMetrica.Config.CrashTracking = true;
            YandexMetrica.Activate(metrika.GetValue<string>("token"));

            RoomManager.OnEnter += Go;
            User.User.OnReset += Reset;
            UserInfo.OnDead += Dead;
            MessengerManager.OnReply += Message;
        }

        internal static void Start()
        {
            // Needs just to initialize constructor
        }

        private static void Report(User.User user, string eventName, IEnumerable<KeyValuePair<string, string>> dict)
        {
            Logger.Debug($"Sending Yandex event: {eventName}");
            YandexMetrica.ReportEvent(eventName, dict
                .Concat(new[]
                {
                    new KeyValuePair<string, string>("user", user.Info.UserId.ToString()),
                    new KeyValuePair<string, string>("intent", Utils.CurrentIntent(user))
                })
                .ToDictionary(kv => kv.Key, kv => kv.Value)
            );
        }

        private static void Report(User.User user, string eventName)
        {
            YandexMetrica.ReportEvent(eventName, new Dictionary<string, string>
            {
                {"user", user.Info.UserId.ToString()},
                {"userIntent", Utils.CurrentIntent(user)}
            });
        }

        private static void Go(User.User user, string identificator)
        {
            Report(user, "go", new[] {new KeyValuePair<string, string>("room", identificator)});
        }

        private static void Reset(User.User user)
        {
            Report(user, "reset");
        }

        private static void Dead(User.User user)
        {
            Report(user, "dead");
        }

        private static void Message(User.User user, Tuple<SentMessage, RecivedMessage> message)
        {
            Report(user, "message/" + message.Item1.Intent, new[]
            {
                new KeyValuePair<string, string>("botMessage", message.Item1.Text),
                new KeyValuePair<string, string>("userMessage", message.Item2?.Text)
            });
        }
    }
}