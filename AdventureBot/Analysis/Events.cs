using System.Collections.Generic;
using System.Linq;
using AdventureBot.Messenger;
using JetBrains.Annotations;
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

        public static void Go(User.User user, string identificator)
        {
            Report(user, "go", new[] {new KeyValuePair<string, string>("room", identificator)});
        }

        public static void Reset(User.User user)
        {
            Report(user, "reset");
        }

        public static void Dead(User.User user)
        {
            Report(user, "dead");
        }

        public static void Message(User.User user, SentMessage message, [CanBeNull] RecivedMessage recivedMessage)
        {
            Report(user, "message/" + message.Intent, new[]
            {
                new KeyValuePair<string, string>("botMessage", message.Text),
                new KeyValuePair<string, string>("userMessage", recivedMessage?.Text)
            });
        }
    }
}