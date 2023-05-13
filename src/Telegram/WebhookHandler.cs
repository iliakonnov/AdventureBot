using System.IO;
using System.Threading.Tasks;
using AdventureBot.Api;
using AdventureBot.Messenger;
using AdventureBot.ObjectManager;
using EmbedIO;
using EmbedIO.Routing;
using EmbedIO.WebApi;
using JetBrains.Annotations;
using Newtonsoft.Json;
using Telegram.Bot.Types;

namespace Telegram;

[WebApi("/telegram")]
public class WebhookHandler : WebApiController
{
    private readonly TelegramBot _messenger;

    public WebhookHandler()
    {
        _messenger = ObjectManager<IMessenger>.Instance.Get<MessengerManager>().Find<Messenger>().messenger;
    }

    [Route(HttpVerbs.Post, "/webhook")]
    [UsedImplicitly]
    public async Task<string> Register()
    {
        Update update;
        using (var reader = new StreamReader(Request.InputStream))
        using (var jsonReader = new JsonTextReader(reader))
        {
            update = new JsonSerializer().Deserialize<Update>(jsonReader);
        }

        if (update == null)
        {
            return "NO";
        }

        await _messenger.HandleUpdateAsync(update);
        return "OK";
    }
}