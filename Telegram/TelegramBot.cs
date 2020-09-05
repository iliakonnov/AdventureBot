using System;
using System.Net;
using System.Threading.Tasks;
using AdventureBot;
using AdventureBot.Messenger;
using MessagePack;
using MihaZupan;
using NLog;
using Telegram.Bot;
using Telegram.Bot.Args;
using Telegram.Bot.Exceptions;
using Telegram.Bot.Types.Enums;
using Telegram.Bot.Types.ReplyMarkups;
using ChatId = Telegram.Bot.Types.ChatId;

namespace Telegram
{
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
            Id = int.Parse(Token.Split(':')[0]);
        }

        public TelegramBot(string token, bool reciveMessages, string proxyHost, int proxyPort)
            : this(token, reciveMessages)
        {
            ProxyHost = proxyHost;
            ProxyPort = proxyPort;
        }

        public TelegramBot(string token, bool reciveMessages, string proxyHost,
            int proxyPort, string proxyUser, string proxyPassword)
            : this(token, reciveMessages, proxyHost, proxyPort)
        {
            ProxyUser = proxyUser;
            ProxyPassword = proxyPassword;
        }

        public int Id { get; }
        public string Token { get; }
        public bool ReciveMessages { get; }
        public string ProxyHost { get; }
        public int ProxyPort { get; }
        public string ProxyUser { get; }
        public string ProxyPassword { get; }
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
                        inlineButtons[i][j] = new InlineKeyboardButton
                        {
                            Text = buttons[j],
                            CallbackData = buttons[j],
                        };
                        simpleButtons[i][j] = new KeyboardButton
                        {
                            Text = buttons[j],
                        };
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
            var parseMode = message.Formatted ? ParseMode.Html : ParseMode.Default;

            var text = message.Text;
            if (associatedData?.ReplyMessageId != null)
            {
                text += $"\n<a href=\"tg://user?id={associatedData.ReplyMessageId}\">@</a>";
            }
            
            try
            {
                if (enableInline)
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
                else
                {
                    await _bot.SendTextMessageAsync(
                        message.ChatId.Id,
                        text,
                        parseMode,
                        replyMarkup: buttonsKeyboardMarkup
                    );
                }
            }
            catch (Exception e)
            {
                if (e is ForbiddenException)
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
            if (ProxyHost != null)
            {
                IWebProxy proxy;
                if (ProxyUser != null && ProxyPassword != null)
                {
                    proxy = new HttpToSocks5Proxy(ProxyHost, ProxyPort, ProxyUser, ProxyPassword);
                }
                else
                {
                    proxy = new HttpToSocks5Proxy(ProxyHost, ProxyPort);
                }

                _bot = new TelegramBotClient(Token, proxy);
            }
            else
            {
                _bot = new TelegramBotClient(Token);
            }

            var me = await _bot.GetMeAsync();
            _username = me.Username;
            if (ReciveMessages)
            {
                _bot.OnMessage += MessageReceivedHandler;
                _bot.OnCallbackQuery += CallbackReceivedHandler;
                _bot.StartReceiving(Array.Empty<UpdateType>());
                Logger.Info("Start receiving for @{username}", _username);
            }
            else
            {
                Logger.Info("Start only sending for @{username}", _username);
            }
        }

        private void CallbackReceivedHandler(object sender, CallbackQueryEventArgs args)
        {
            var msgId = $"{_username}/{args.CallbackQuery.Message.Chat.Id}/{args.CallbackQuery.Message.MessageId}";

            // ReSharper disable once SwitchStatementMissingSomeCases
            var message = new ReceivedMessage
            {
                ChatId = new AdventureBot.ChatId(MessengerId, args.CallbackQuery.Message.Chat.Id),
                UserId = new UserId(MessengerId, args.CallbackQuery.From.Id),
                Text = args.CallbackQuery.Data,
                MessengerSpecificData = ReceivedMessageAssociatedData.Inline(args.CallbackQuery.Message.Chat.Id, args.CallbackQuery.Message.MessageId),
                MessageId = msgId,
            };
            OnMessageReceived?.Invoke(message);
        }

        private async void MessageReceivedHandler(object sender, MessageEventArgs args)
        {
            int? replyId;
            if (args.Message.Chat.Type != ChatType.Private)
            {
                replyId = args.Message.From.Id;
            }
            else
            {
                await _bot.SendChatActionAsync(new ChatId(args.Message.Chat.Id), ChatAction.Typing);
                replyId = null;
            }

            var msgId = $"{_username}/{args.Message.MessageId}";

            // ReSharper disable once SwitchStatementMissingSomeCases
            ReceivedMessage message;
            if (args.Message.Type == MessageType.Text)
            {
                if (args.Message.Text == "/remove_keyboard")
                {
                    await _bot.SendTextMessageAsync(args.Message.Chat.Id, "А теперь отправьте /repeat",
                        replyMarkup: new ReplyKeyboardRemove());
                    return;
                }
                else
                {
                    message = new ReceivedMessage
                    {
                        ChatId = new AdventureBot.ChatId(MessengerId, args.Message.Chat.Id),
                        UserId = new UserId(MessengerId, args.Message.From.Id),
                        Text = args.Message.Text,
                        MessengerSpecificData = ReceivedMessageAssociatedData.Reply(replyId),
                        MessageId = msgId
                    };
                }
            }
            else
            {
                return;
            }

            OnMessageReceived?.Invoke(message);
        }
    }

    [MessagePackObject(true)]
    internal class ReceivedMessageAssociatedData
    {
        public readonly bool IsInline;
        public readonly (long, int)? InlineMessageId;
        public readonly long? ReplyMessageId;

        private ReceivedMessageAssociatedData(bool isInline, (long, int)? inlineMessageId, long? replyMessageId)
        {
            IsInline = isInline;
            InlineMessageId = inlineMessageId;
            ReplyMessageId = replyMessageId;
        }

        public static ReceivedMessageAssociatedData Inline(ChatId chatId, int messageId)
        {
            var inlineMessageId = (chatId.Identifier, messageId);
            return new ReceivedMessageAssociatedData(true, inlineMessageId, null);
        }
        
        public static ReceivedMessageAssociatedData Reply(long? messageId)
        {
            return new ReceivedMessageAssociatedData(false, null, messageId);
        }
    }
}