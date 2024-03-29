using System;
using System.Text;
using System.Threading.Tasks;
using AdventureBot;
using AdventureBot.Api;
using AdventureBot.Messenger;
using AdventureBot.User;
using EmbedIO;
using EmbedIO.Routing;
using EmbedIO.WebApi;
using JetBrains.Annotations;
using MessagePack;

namespace Api;

[WebApi("/api")]
public class ApiController : WebApiController
{
    private static readonly Random Random = new();
    private static string Secret => Configuration.Config["api_secret"];

    [Route(HttpVerbs.Get, "/register")]
    [UsedImplicitly]
    public string Register([QueryField] string secret, [QueryField] long? id)
    {
        if (secret != Secret)
        {
            throw HttpException.Forbidden();
        }

        var userId = id ?? LongRandom();
        using var context = new UserContext(new UserId(ApiMessenger.MessengerId, userId));
        return $"{userId}:{context.User.Token}";
    }

    [Route(HttpVerbs.Post, "/{tokenArg}")]
    [UsedImplicitly]
    public async Task PostMessage(string tokenArg)
    {
        var token = ApiMessenger.ParseToken(tokenArg);
        if (token == null)
        {
            throw HttpException.Forbidden();
        }

        var (chat, user) = ((ChatId, UserId))token;

        var text = await HttpContext.GetRequestDataAsync<string>();

        var message = new ReceivedMessage
        {
            ChatId = chat,
            Text = text,
            UserId = user
        };
        ApiMessenger.InvokeOnMessageReceived(message);
    }

    [Route(HttpVerbs.Get, "/{tokenArg}")]
    [UsedImplicitly]
    public async Task GetState([QueryField] bool? json, string tokenArg)
    {
        var token = ApiMessenger.ParseToken(tokenArg);
        if (token == null)
        {
            throw HttpException.Forbidden();
        }

        var (_, user) = ((ChatId, UserId))token;

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

        await using var stream = HttpContext.OpenResponseStream();
        await stream.WriteAsync(bytes, 0, bytes.Length);
    }

    private static long LongRandom()
    {
        var buf = new byte[8];
        Random.NextBytes(buf);
        var longRand = BitConverter.ToInt64(buf, 0);
        return Math.Abs(longRand);
    }
}