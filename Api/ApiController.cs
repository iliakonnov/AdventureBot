using System.Collections.Generic;
using System.Collections.Specialized;
using System.Text;
using System.Threading.Tasks;
using AdventureBot;
using AdventureBot.Messenger;
using AdventureBot.User;
using EmbedIO;
using EmbedIO.Net.Internal;
using EmbedIO.Routing;
using EmbedIO.Utilities;
using EmbedIO.WebApi;
using MessagePack;

namespace Api
{
    public class ApiController : WebApiController
    {
        [Route(HttpVerbs.Get, "/register")]
        public string Register([QueryField] string secret, [QueryField] long? id)
        {
            if (secret != ApiMessenger._secret)
            {
                throw HttpException.Forbidden();
            }

            var userId = id ?? ApiMessenger.LongRandom();
            using var context = new UserContext(new UserId(ApiMessenger.MessengerId, userId));
            return $"{userId}:{context.User.Token}";
        }

        [Route(HttpVerbs.Post, "/{tokenArg}")]
        public async Task PostMessage(string tokenArg)
        {
            (ChatId, UserId)? token = ApiMessenger.ParseToken(tokenArg);
            if (token == null)
            {
                throw HttpException.Forbidden();
            }

            var (chat, user) = ((ChatId, UserId)) token;

            var text = await HttpContext.GetRequestDataAsync<string>();

            var message = new RecivedMessage
            {
                ChatId = chat,
                Text = text,
                UserId = user
            };
            ApiMessenger.InvokeOnMessageReceived(message);
        }

        [Route(HttpVerbs.Get, "/{tokenArg}")]
        public async Task GetState([QueryField] bool? json, string tokenArg)
        {
            (ChatId, UserId)? token = ApiMessenger.ParseToken(tokenArg);
            if (token == null)
            {
                throw HttpException.Forbidden();
            }

            var (_, user) = ((ChatId, UserId)) token;

            using var context = new UserContext(user);
            var publicUser = new PublicUser(context.User);
            var bytes = MessagePackSerializer.Serialize(publicUser);
            if (json ?? false)
            {
                var response = MessagePackSerializer.ConvertToJson(bytes);
                HttpContext.Response.ContentType = "application/json";
                bytes = Encoding.UTF8.GetBytes(response);
            }
            else
            {
                HttpContext.Response.ContentType = "application/x-msgpack";
            }
            using (var stream = HttpContext.OpenResponseStream())
            {
                await stream.WriteAsync(bytes, 0, bytes.Length);
            }
        }
    }
}