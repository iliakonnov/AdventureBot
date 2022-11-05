using System;
using System.IO;
using System.Linq;
using System.Net.Http;
using System.Text.RegularExpressions;
using System.Threading.Tasks;
using AdventureBot;
using AdventureBot.Messenger;
using AdventureBot.ObjectManager;
using Newtonsoft.Json;
using NLog;
using Prometheus;
using VkNet;
using VkNet.Enums.SafetyEnums;
using VkNet.Model;
using VkNet.Model.Keyboard;
using VkNet.Model.RequestParams;
using User = AdventureBot.User.User;

namespace VkMessenger;

[Messenger]
public class Messenger : IMessenger
{
    internal const int MessengerId = 2;

    private static readonly Logger Logger = LogManager.GetCurrentClassLogger();
    private static readonly Counter ApiRequestsTotal =
        Metrics.CreateCounter("vk_api_requests_total", "Total number of vk api requests");
    private static readonly Counter ApiRequestsFailed =
        Metrics.CreateCounter("vk_api_requests_failed", "Total number of failed vk api responses");
    private static readonly Counter ErrorCounter =
        Metrics.CreateCounter("vk_messenger_errors", "Total number of errors in VkMessenger");

    private readonly string _accessToken;
    private readonly ulong _groupId;
    private VkApi _api;

    public Messenger()
    {
        _accessToken = Configuration.Config.GetSection("vk_token").Value;
        _groupId = ulong.Parse(Configuration.Config.GetSection("vk_group").Value);
    }

    private static string StripHTML(string input)
    {
        return Regex.Replace(input, "<[/a-z]*?>", string.Empty);
    }

    public async Task Send(SentMessage message, ReceivedMessage receivedMessage, User user)
    {
        if (message.ChatId.Messenger != MessengerId)
        {
            return;
        }

        var parameters = new MessagesSendParams
        {
            Message = message.Formatted ? StripHTML(message.Text) : message.Text,
            PeerId = message.ChatId.Id,
            Keyboard = new MessageKeyboard
            {
                OneTime = false,
                Buttons = message.Buttons?.Select(row => row.Select(button => new MessageKeyboardButton
                {
                    Action = new MessageKeyboardButtonAction {Label = button, Type = KeyboardButtonActionType.Text}
                }).ToArray()).ToArray()
            },
            RandomId = Random.Shared.NextInt64()
        };

        if (parameters.Keyboard?.Buttons == null)
        {
            parameters.Keyboard = null;
        }

        if (receivedMessage?.MessengerSpecificData != null)
        {
            parameters.ForwardMessages = new[] {(long) receivedMessage.MessengerSpecificData};
        }

        try
        {
            ApiRequestsTotal.Inc();
            await _api.Messages.SendAsync(parameters);
        }
        catch (Exception e)
        {
            ApiRequestsFailed.Inc();
            ErrorCounter.Inc();
            Logger.Error(e, "Failed to send messager");
            throw;
        }
    }

    public event MessageHandler MessageReceived;

    public void BeginPolling()
    {
        _api = new VkApi();
        _api.Authorize(new ApiAuthParams {AccessToken = _accessToken});

        BeginPoll();

        Logger.Info("Start listening for VK");
    }

    private async void BeginPoll()
    {
        var longpoll = await _api.Groups.GetLongPollServerAsync(_groupId);
        var parameters = new LongpollParameters(_groupId, longpoll);
        const int timeout = 30;

        using var client = new HttpClient();
        client.Timeout = TimeSpan.FromSeconds(timeout);

        while (true)
        {
            try
            {
                ApiRequestsTotal.Inc();
                var request = new HttpRequestMessage(HttpMethod.Get, parameters.GetUrl(timeout - 5));
                using var response = await client.SendAsync(request, HttpCompletionOption.ResponseHeadersRead);
                if (!response.IsSuccessStatusCode)
                {
                    ApiRequestsFailed.Inc();
                }

                await using var body = await response.Content.ReadAsStreamAsync();
                using var reader = new StreamReader(body);
                var json = await reader.ReadToEndAsync();
                var result = JsonConvert.DeserializeObject<LongpollResponse>(json);
                foreach (var message in result.Updates)
                {
                    MessageReceived?.Invoke(message.ToReceivedMessage());
                }

                await parameters.Update(_api, result);
            }
            catch (TimeoutException e)
            {
                Logger.Warn(e, "longpoll timed out");
            }
            catch (Exception e)
            {
                ErrorCounter.Inc();
                Logger.Error(e, "failed to get updates");
            }
        }

        // ReSharper disable once FunctionNeverReturns
    }
}