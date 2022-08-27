using System;
using System.Threading;
using System.Threading.Tasks;
using AdventureBot;
using AdventureBot.Messenger;
using MessagePack;
using NLog;
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

    private TelegramBotClient _bot;
    private string _username;

    public TelegramBot(string token, bool reciveMessages)
    {
        Token = token;
        ReciveMessages = reciveMessages;
        Id = long.Parse(Token.Split(':')[0]);
    }

    public long Id { get; }
    public string Token { get; }
    public bool ReciveMessages { get; }
    public Messenger Messenger { get; internal set; }

    public DateTime LastMessageSent { get; private set; }

    public async Task Send(SentMessage message, ReceivedMessage receivedMessage)
    {
        if (message.ChatId.Messenger != MessengerId)
        {
            return;
        }

        var associatedData = (ReceivedMessageAssociatedData) receivedMessage?.MessengerSpecificData;

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
            for (var i = 0; i < message.Buttons.Length; i++)
            {
                var buttons = message.Buttons[i];
                inlineButtons[i] = new InlineKeyboardButton[buttons.Length];
                simpleButtons[i] = new KeyboardButton[buttons.Length];
                for (var j = 0; j < buttons.Length; j++)
                {
                    inlineButtons[i][j] = new InlineKeyboardButton(buttons[j])
                    {
                        CallbackData = buttons[j]
                    };
                    simpleButtons[i][j] = new KeyboardButton(buttons[j]);
                    keyboard = true;
                }
            }

            if (keyboard)
            {
                inlineKeyboardMarkup = new InlineKeyboardMarkup(inlineButtons);
                buttonsKeyboardMarkup = new ReplyKeyboardMarkup(simpleButtons);
            }
        }

        const bool enableInline = false;
        ParseMode? parseMode = message.Formatted ? ParseMode.Html : null;

        var text = message.Text;
        if (associatedData?.ReplyMessageId != null)
        {
            text += $"\n<a href=\"tg://user?id={associatedData.ReplyMessageId}\">@</a>";
        }

        try
        {
            if (!enableInline)
            {
                await _bot.SendTextMessageAsync(
                    message.ChatId.Id,
                    text,
                    parseMode,
                    replyMarkup: buttonsKeyboardMarkup
                );
            }
            else
            {
                var inlineId = associatedData?.InlineMessageId;
                if (inlineId != null && message.PreferToUpdate == true)
                {
                    var (chatId, messageId) = inlineId.Value;
                    await _bot.EditMessageTextAsync(
                        chatId,
                        messageId,
                        text,
                        parseMode,
                        replyMarkup: inlineKeyboardMarkup
                    );
                }
                else
                {
                    if (inlineId != null)
                    {
                        // PreferToUpdate is null, but inlineId is not null, so remove old buttons
                        // Also we do not want to wait until they are removed.
#pragma warning disable 4014
                        var (chatId, messageId) = inlineId.Value;
                        _bot.EditMessageReplyMarkupAsync(chatId, messageId,
                            new InlineKeyboardMarkup(new InlineKeyboardButton[0]));
#pragma warning restore 4014
                    }

                    await _bot.SendTextMessageAsync(
                        message.ChatId.Id,
                        text,
                        parseMode,
                        replyMarkup: inlineKeyboardMarkup
                    );
                }
            }
        }
        catch (Exception e)
        {
            if (e is ApiRequestException {ErrorCode: 403})
            {
                Logger.Info(e, "Bot is stopped by user {0}", message.ChatId.Id);
            }
            else
            {
                Logger.Error(e, "Error while sending message");
            }
        }
    }

    public event MessageHandler OnMessageReceived;

    public async void BeginPolling()
    {
        _bot = new TelegramBotClient(Token);

        var me = await _bot.GetMeAsync();
        _username = me.Username;
        if (ReciveMessages)
        {
            _bot.StartReceiving(
                HandleUpdateAsync,
                HandlePollingErrorAsync,
                new ReceiverOptions
                {
                    AllowedUpdates = Array.Empty<UpdateType>()
                },
                new CancellationToken()
            );
            Logger.Info("Start receiving for @{username}", _username);
        }
        else
        {
            Logger.Info("Start only sending for @{username}", _username);
        }
    }

    private Task HandleUpdateAsync(ITelegramBotClient botClient, Update update, CancellationToken cancellationToken)
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

    private static Task HandlePollingErrorAsync(ITelegramBotClient botClient, Exception exception,
        CancellationToken cancellationToken)
    {
        var errorMessage = exception switch
        {
            ApiRequestException apiRequestException
                => $"Telegram API Error:\n[{apiRequestException.ErrorCode}]\n{apiRequestException.Message}",
            _ => exception.ToString()
        };

        Logger.Error(errorMessage);
        return Task.CompletedTask;
    }

    private void CallbackReceivedHandler(CallbackQuery args)
    {
        var msgId = $"{_username}/{args.Message.Chat.Id}/{args.Message.MessageId}";

        var message = new ReceivedMessage
        {
            ChatId = new AdventureBot.ChatId(MessengerId, args.Message.Chat.Id),
            UserId = new UserId(MessengerId, args.From.Id),
            Text = args.Data,
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