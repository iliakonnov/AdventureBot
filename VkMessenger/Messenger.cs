using System;
using System.IO;
using System.Linq;
using System.Net.Http;
using System.Threading.Tasks;
using AdventureBot.Messenger;
using AdventureBot.ObjectManager;
using Newtonsoft.Json;
using NLog;
using VkNet;
using VkNet.Model;
using VkNet.Model.Keyboard;
using VkNet.Model.RequestParams;
using VkNet.Utils;
using User = AdventureBot.User.User;

namespace VkMessenger;

[Messenger]
public class Messenger : IMessenger
{
    internal const int MessengerId = 2;

    internal const string AccessToken =
        "SecretSecretSecretSecretSecretSecretSecretSecretSecretSecretSecretSecretSecretSecret";

    internal const ulong GroupId = 169319191;

    private static readonly Logger Logger = LogManager.GetCurrentClassLogger();
    private VkApi _api;

    public async Task Send(SentMessage message, ReceivedMessage receivedMessage, User user)
    {
        if (message.ChatId.Messenger != MessengerId)
        {
            return;
        }

        var parameters = new MessagesSendParams
        {
            Message = message.Text,
            PeerId = message.ChatId.Id,
            Keyboard = new MessageKeyboard
            {
                OneTime = false,
                Buttons = message.Buttons?.Select(row => row.Select(button => new MessageKeyboardButton
                {
                    Action = new MessageKeyboardButtonAction {Label = button}
                }).ToReadOnlyCollection()).ToReadOnlyCollection()
            }
        };
        if (receivedMessage?.MessengerSpecificData != null)
        {
            parameters.ForwardMessages = new[] {(long) receivedMessage.MessengerSpecificData};
        }

        await _api.Messages.SendAsync(parameters);
    }

    public event MessageHandler MessageReceived;

    public void BeginPolling()
    {
        _api = new VkApi();
        _api.Authorize(new ApiAuthParams
        {
            AccessToken = AccessToken
        });

        BeginPoll();

        Logger.Info($"Start listening for {_api.Account.GetProfileInfo().ScreenName}");
    }

    private async void BeginPoll()
    {
        var longpoll = await _api.Groups.GetLongPollServerAsync(GroupId);
        var parameters = new LongpollParameters(longpoll);
        const int timeout = 25;

        using (var client = new HttpClient())
        {
            client.Timeout = TimeSpan.FromSeconds(timeout);

            while (true)
            {
                var request = new HttpRequestMessage(HttpMethod.Get, parameters.GetUrl(timeout));
                using (var response = await client.SendAsync(request, HttpCompletionOption.ResponseHeadersRead))
                using (var body = await response.Content.ReadAsStreamAsync())
                using (var reader = new StreamReader(body))
                {
                    var json = reader.ReadToEnd();
                    var result = JsonConvert.DeserializeObject<LongpollResponse>(json);
                    foreach (var message in result.Updates)
                    {
                        MessageReceived?.Invoke(message.ToReceivedMessage());
                    }

                    await parameters.Update(_api, result);
                }
            }
        }

        // ReSharper disable once FunctionNeverReturns
    }
}