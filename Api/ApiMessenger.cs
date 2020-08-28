using System;
using System.IO;
using AdventureBot;
using AdventureBot.Messenger;
using AdventureBot.ObjectManager;
using AdventureBot.User;
using MessagePack;
using Microsoft.Extensions.Configuration;
using Nancy;
using Nancy.Hosting.Self;

namespace Api
{
    [Messenger]
    public class ApiMessenger : NancyModule, IMessenger
    {
        private const int MessengerId = 3;
        private static Random _random;

        private static string _secret;

        private NancyHost _host;

        public ApiMessenger()
        {
            if (MessageRecievedStatic == null)
            {
                MessageRecievedStatic += message => MessageRecieved?.Invoke(message);
            }

            Post["/api/{token}", true] = async (parameters, _) =>
            {
                (ChatId, UserId)? token = ParseToken(parameters.token);
                if (token == null)
                {
                    return HttpStatusCode.Forbidden;
                }

                var (chat, user) = ((ChatId, UserId)) token;

                var text = new StreamReader(Request.Body).ReadToEnd();

                var message = new RecivedMessage
                {
                    ChatId = chat,
                    Text = text,
                    UserId = user
                };
                MessageRecievedStatic?.Invoke(message);
                return HttpStatusCode.OK;
            };

            Get["/api/{token}", true] = async (parameters, _) =>
            {
                (ChatId, UserId)? token = ParseToken(parameters.token);
                if (token == null)
                {
                    return HttpStatusCode.Forbidden;
                }

                var (_, user) = ((ChatId, UserId)) token;

                using (var context = new UserContext(user))
                {
                    var publicUser = new PublicUser(context.User);
                    var query = (DynamicDictionary) Request.Query;
                    var bytes = MessagePackSerializer.Serialize(publicUser);
                    if (query.ContainsKey("json"))
                    {
                        var response = (Response) MessagePackSerializer.ConvertToJson(bytes);
                        response.ContentType = "application/json";
                        return response;
                    }

                    return new Response
                    {
                        ContentType = "application/x-msgpack",
                        Contents = s => s.Write(bytes, 0, bytes.Length)
                    };
                }
            };

            Get["/api/register", true] = async (parameters, _) =>
            {
                var query = (DynamicDictionary) Request.Query;

                if (
                    !query.TryGetValue("secret", out var secret)
                    || secret != _secret
                )
                {
                    return HttpStatusCode.Forbidden;
                }

                long id;
                if (query.TryGetValue("id", out var dynId))
                {
                    id = (long) dynId;
                }
                else
                {
                    // It can generate existing id!
                    id = LongRandom(_random);
                }

                using (var context = new UserContext(new UserId(MessengerId, id)))
                {
                    return $"{id}:{context.User.Token}";
                }
            };
        }

        public void Send(SentMessage message, RecivedMessage recievedMessage, User user)
        {
            // Do nothing because PublicUser.MessageManager.LastMessages already contains last messages
        }

        public event MessageHandler MessageRecieved;

        public void BeginPolling()
        {
            _random = new Random();
            var hostConf = new HostConfiguration
            {
                RewriteLocalhost = true,
                UrlReservations = {CreateAutomatically = true}
            };
            var url = Configuration.Config.GetValue<string>("ApiHost");
            _secret = Configuration.Config.GetValue<string>("ApiSecret");
            _host = new NancyHost(hostConf, new Uri(url));
            _host.Start();
        }

        private static long LongRandom(Random rand)
        {
            var buf = new byte[8];
            rand.NextBytes(buf);
            var longRand = BitConverter.ToInt64(buf, 0);
            return Math.Abs(longRand);
        }


        private static event MessageHandler MessageRecievedStatic;

        private static (ChatId, UserId)? ParseToken(string token)
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
    }
}