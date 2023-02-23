using System;
using System.Linq;
using System.Threading;
using System.Threading.Tasks;
using AdventureBot;
using AdventureBot.Messenger;
using JetBrains.Annotations;
using MessagePack;
using Microsoft.Extensions.Configuration;
using NLog;
using Prometheus;
using Telegram.Bot;
using Telegram.Bot.Exceptions;
using Telegram.Bot.Polling;
using Telegram.Bot.Types;
using Telegram.Bot.Types.Enums;
using Telegram.Bot.Types.ReplyMarkups;
using ChatId = Telegram.Bot.Types.ChatId;

namespace Telegram;

internal class TelegramBot
{
    private const int MessengerId = 1;
    private static readonly Logger Logger = LogManager.GetCurrentClassLogger();

    private static readonly Counter ApiRequestsTotal =
        Metrics.CreateCounter("telegram_api_requests_total", "Total number of telegram api requests");

    private static readonly Counter ApiRequestsFailed =
        Metrics.CreateCounter("telegram_api_requests_failed", "Total number of failed telegram api responses");

    private static readonly Counter ErrorCounter =
        Metrics.CreateCounter("telegram_messenger_errors", "Total number of errors in TelegramMessenger");

    private readonly TelegramBotClient _bot;
    private string _username;

    public TelegramBot(string token)
    {
        Token = token;
        Id = long.Parse(Token.Split(':')[0]);

        _bot = new TelegramBotClient(Token);
        _bot.OnMakingApiRequest += async (_, _, _) => ApiRequestsTotal.Inc();
        _bot.OnApiResponseReceived += async (_, args, _) =>
        {
            if (!args.ResponseMessage.IsSuccessStatusCode)
            {
                ApiRequestsFailed.Inc();
            }
        };
    }

    public long Id { get; }
    public string Token { get; }
    public bool EnablePolling { get; }

    public DateTime LastMessageSent { get; private set; }

    private string EncodeButton(int idx, string button)
    {
        var len = Math.Min(32, button.Length);
        var head = button[..len];
        return $"{idx}@{head}";
    }

    [CanBeNull]
    private string DecodeButton(string[] buttons, [CanBeNull] string data)
    {
        if (data == null)
        {
            return null;
        }

        var splitted = data.Split('@', 2);
        if (splitted.Length != 2)
        {
            return null;
        }

        if (!int.TryParse(splitted[0], out var buttonId))
        {
            return null;
        }

        if (buttons == null || buttonId < 0 || buttonId >= buttons.Length)
        {
            return null;
        }

        var text = buttons[buttonId];
        var len = Math.Min(32, text.Length);
        if (text[..len] != splitted[1])
        {
            return null;
        }

        return text;
    }

    public async Task Send(SentMessage message, ReceivedMessage receivedMessage)
    {
        if (message.ChatId.Messenger != MessengerId)
        {
            return;
        }

        var associatedData = (ReceivedMessageAssociatedData)receivedMessage?.MessengerSpecificData;

        LastMessageSent = DateTime.Now;

        InlineKeyboardMarkup inlineKeyboardMarkup = null;
        ReplyKeyboardMarkup buttonsKeyboardMarkup = null;
        if (message.Buttons == null)
        {
            // Should not be here
            Logger.Error("Sending message without buttons. This is bad.");
        }
        else
        {
            var inlineButtons = new InlineKeyboardButton[message.Buttons.Length][];
            var simpleButtons = new KeyboardButton[message.Buttons.Length][];
            var keyboard = false;
            var btnCounter = 0;
            for (var i = 0; i < message.Buttons.Length; i++)
            {
                var buttons = message.Buttons[i];
                inlineButtons[i] = new InlineKeyboardButton[buttons.Length];
                simpleButtons[i] = new KeyboardButton[buttons.Length];
                for (var j = 0; j < buttons.Length; j++)
                {
                    inlineButtons[i][j] = new InlineKeyboardButton(buttons[j])
                    {
                        CallbackData = EncodeButton(btnCounter++, buttons[j])
                    };
                    simpleButtons[i][j] = new KeyboardButton(buttons[j]);
                    keyboard = true;
                }
            }

            if (keyboard)
            {
                inlineKeyboardMarkup = new InlineKeyboardMarkup(inlineButtons);
                buttonsKeyboardMarkup = new ReplyKeyboardMarkup(simpleButtons)
                {
                    OneTimeKeyboard = true
                };
            }
        }

        ParseMode? parseMode = message.Formatted ? ParseMode.Html : null;

        var text = message.Text;
        if (associatedData?.ReplyMessageId != null)
        {
            text += $"\n<a href=\"tg://user?id={associatedData.ReplyMessageId}\">@</a>";
        }

        var inlineId = associatedData?.InlineMessageId;

        try
        {
            if (inlineId != null && message.PreferToUpdate != false)
            {
                // We already had a message and message still allows itself to be inlined. So let's update it.
                var (chatId, messageId) = inlineId.Value;
                try
                {
                    await _bot.EditMessageTextAsync(chatId, messageId, text, parseMode,
                        replyMarkup: inlineKeyboardMarkup);
                }
                catch (ApiRequestException e)
                {
                    if (!e.Message.Contains("message is not modified"))
                    {
                        throw;
                    }
                }

                message.MessengerSpecificData[MessengerId] =
                    new SentMessageAssociatedData(_username, chatId, messageId);
                return;
            }

            if (inlineId != null)
            {
                // We already had a message, but now we do not want inline keyboard. Let's delete old message.
                var (chatId, messageId) = inlineId.Value;
                await _bot.DeleteMessageAsync(chatId, messageId);
            }

            // Otherwise send a new message
            IReplyMarkup replyMarkup = message.PreferToUpdate != false ? inlineKeyboardMarkup : buttonsKeyboardMarkup;
            var sent = await _bot.SendTextMessageAsync(message.ChatId.Id, text, parseMode, replyMarkup: replyMarkup);
            message.MessengerSpecificData[MessengerId] =
                new SentMessageAssociatedData(_username, sent.Chat.Id, sent.MessageId);
        }
        catch (Exception e)
        {
            if (e is ApiRequestException { ErrorCode: 403 })
            {
                Logger.Info(e, "Bot is stopped by user {0}", message.ChatId.Id);
            }
            else
            {
                ErrorCounter.Inc();
                Logger.Error(e, "Error while sending message");
            }
        }
    }

    public event MessageHandler OnMessageReceived;

    public async void BeginPolling()
    {
        var me = await _bot.GetMeAsync();
        _username = me.Username;
        if (!Configuration.Config.GetValue<bool>("telegram_polling"))
        {
            return;
        }
        _bot.StartReceiving(
            HandleUpdateAsync,
            HandlePollingErrorAsync,
            new ReceiverOptions
            {
                AllowedUpdates = new[] { UpdateType.Message, UpdateType.CallbackQuery },
            }
        );
        Logger.Info("Start receiving for @{username}", _username);
    }

    internal Task HandleUpdateAsync(Update update)
    {
        if (update.Message is { } message)
        {
            MessageReceivedHandler(message);
        }
        else if (update.CallbackQuery is { } callbackQuery)
        {
            CallbackReceivedHandler(callbackQuery);
        }

        return Task.CompletedTask;
    }

    private Task HandleUpdateAsync(ITelegramBotClient botClient, Update update, CancellationToken cancellationToken)
    {
        return HandleUpdateAsync(update);
    }

    private Task HandlePollingErrorAsync(ITelegramBotClient botClient, Exception exception,
        CancellationToken cancellationToken)
    {
        var errorMessage = exception switch
        {
            ApiRequestException apiRequestException
                => $"Telegram API Error:\n[{apiRequestException.ErrorCode}]\n{apiRequestException.Message}",
            _ => exception.ToString()
        };

        ErrorCounter.Inc();
        Logger.Error(errorMessage);
        BeginPolling();
        return Task.CompletedTask;
    }

    private void CallbackReceivedHandler(CallbackQuery args)
    {
        var msgId = $"{_username}/{args.Message.Chat.Id}/{args.Message.MessageId}";

        var userId = new UserId(MessengerId, args.From.Id);
        SentMessage inReplyTo;
        using (var context = new UserContext(userId))
        {
            // ReSharper disable once ReplaceWithSingleCallToLastOrDefault
            inReplyTo = context.User.MessageManager.LastMessages
                .Where(msg => msg.ChatId.Messenger == MessengerId)
                .Where(msg => msg.ChatId.Id == args.Message.Chat.Id)
                .Where(msg => msg.MessengerSpecificData != null)
                .Where(msg => msg.MessengerSpecificData.ContainsKey(MessengerId))
                .Where(msg => msg.MessengerSpecificData[MessengerId]["MessageId"] == args.Message.MessageId)
                .LastOrDefault();
        }

        if (inReplyTo == null)
        {
            return;
        }

        var buttons = inReplyTo.Buttons?.SelectMany(x => x).ToArray();
        var text = DecodeButton(buttons, args.Data);
        if (text == null)
        {
            return;
        }

        var message = new ReceivedMessage
        {
            ChatId = new AdventureBot.ChatId(MessengerId, args.Message.Chat.Id),
            UserId = userId,
            Text = text,
            MessengerSpecificData = ReceivedMessageAssociatedData.Inline(args.Message.Chat.Id,
                args.Message.MessageId),
            MessageId = msgId
        };
        OnMessageReceived?.Invoke(message);
    }

    private async void MessageReceivedHandler(Message message)
    {
        long? replyId;
        if (message.Chat.Type != ChatType.Private)
        {
            replyId = message.From.Id;
        }
        else
        {
            await _bot.SendChatActionAsync(new ChatId(message.Chat.Id), ChatAction.Typing);
            replyId = null;
        }

        var msgId = $"{_username}/{message.MessageId}";

        if (message.Type != MessageType.Text)
        {
            return;
        }

        if (message.Text == "/remove_keyboard")
        {
            await _bot.SendTextMessageAsync(message.Chat.Id, "А теперь отправьте /repeat",
                replyMarkup: new ReplyKeyboardRemove());
            return;
        }

        var parsed = new ReceivedMessage
        {
            ChatId = new AdventureBot.ChatId(MessengerId, message.Chat.Id),
            UserId = new UserId(MessengerId, message.From.Id),
            Text = message.Text,
            MessengerSpecificData = ReceivedMessageAssociatedData.Reply(replyId),
            MessageId = msgId
        };

        OnMessageReceived?.Invoke(parsed);
    }
}

[MessagePackObject(true)]
internal class ReceivedMessageAssociatedData
{
    public readonly (long, int)? InlineMessageId;
    public readonly bool IsInline;
    public readonly long? ReplyMessageId;

    private ReceivedMessageAssociatedData(bool isInline, (long, int)? inlineMessageId, long? replyMessageId)
    {
        IsInline = isInline;
        InlineMessageId = inlineMessageId;
        ReplyMessageId = replyMessageId;
    }

    public static ReceivedMessageAssociatedData Inline(ChatId chatId, int messageId)
    {
        var inlineMessageId = (chatId.Identifier.Value, messageId);
        return new ReceivedMessageAssociatedData(true, inlineMessageId, null);
    }

    public static ReceivedMessageAssociatedData Reply(long? messageId)
    {
        return new ReceivedMessageAssociatedData(false, null, messageId);
    }
}

[MessagePackObject(true)]
internal class SentMessageAssociatedData
{
    public readonly string Username;
    public readonly long ChatId;
    public readonly long MessageId;

    public SentMessageAssociatedData(string username, long chatId, long messageId)
    {
        Username = username;
        ChatId = chatId;
        MessageId = messageId;
    }
}