using System;
using AdventureBot;
using AdventureBot.Messenger;
using AdventureBot.ObjectManager;
using AdventureBot.User;
using Microsoft.Extensions.Configuration;
using EmbedIO;
using EmbedIO.Actions;
using EmbedIO.WebApi;
using NLog;

namespace Api
{
    [Messenger]
    public class ApiMessenger : IMessenger
    {
        private static readonly Logger Logger = LogManager.GetCurrentClassLogger();
        internal const int MessengerId = 3;
        internal static string _secret;

        private static Random _random;
        private WebServer _server;

        public ApiMessenger()
        {
            if (OnMessageReceivedStatic == null)
            {
                OnMessageReceivedStatic += message => MessageRecieved?.Invoke(message);
            }
        }

        public void Send(SentMessage message, RecivedMessage recievedMessage, User user)
        {
            // Do nothing because PublicUser.MessageManager.LastMessages already contains last messages
        }

        public event MessageHandler MessageRecieved;

        public void BeginPolling()
        {
            _random = new Random();
            _secret = Configuration.Config.GetValue<string>("ApiSecret");
            var url = Configuration.Config.GetValue<string>("ApiHost");
            _server = new WebServer(o => o
                .WithUrlPrefix(url)
                .WithMode(HttpListenerMode.EmbedIO))
                .WithWebApi("/api", m => m.WithController<ApiController>())
                .WithModule(new ActionModule("/", HttpVerbs.Any, ctx => ctx.SendDataAsync(new { Message = "Error" })));
            _server.StateChanged += (s, e) => Logger.Info("WebServer New State - {0}", e.NewState);
            _server.RunAsync();
        }

        internal static long LongRandom()
        {
            var buf = new byte[8];
            _random.NextBytes(buf);
            var longRand = BitConverter.ToInt64(buf, 0);
            return Math.Abs(longRand);
        }

        internal static event MessageHandler OnMessageReceivedStatic;

        internal static (ChatId, UserId)? ParseToken(string token)
        {
            var splitted = token.Split(':');
            if (splitted.Length != 2)
            {
                return null;
            }

            if (!long.TryParse(splitted[0], out var id))
            {
                return null;
            }

            if (!Guid.TryParse(splitted[1], out var guid))
            {
                return null;
            }

            var user = new UserId(MessengerId, id);

            using (var context = new UserContext(user))
            {
                if (context.User.Token != guid)
                {
                    return null;
                }
            }

            return (new ChatId(MessengerId, id), user);
        }

        internal static void InvokeOnMessageReceived(RecivedMessage message)
        {
            OnMessageReceivedStatic?.Invoke(message);
        }
    }
}