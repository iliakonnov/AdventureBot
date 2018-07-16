using System;
using System.Linq;
using System.Net;
using System.Threading.Tasks;
using AdventureBot;
using AdventureBot.Messenger;
using AdventureBot.ObjectManager;
using Microsoft.Extensions.Logging;
using MihaZupan;
using Telegram.Bot;
using Telegram.Bot.Args;
using Telegram.Bot.Exceptions;
using Telegram.Bot.Types.Enums;
using Telegram.Bot.Types.ReplyMarkups;

namespace Telegram
{
    [GameObject]
    internal class TelegramBot
    {
        private const int MessengerId = 1;

        public int Id { get; }
        public string Token { get; }
        public bool ReciveMessages { get; }
        public string ProxyHost { get; }
        public int ProxyPort { get; }
        public string ProxyUser { get; }
        public string ProxyPassword { get; }
        public Messenger Messenger { get; internal set; }

        public TelegramBot(string token, bool reciveMessages)
        {
            Token = token;
            ReciveMessages = reciveMessages;
            Id = int.Parse(Token.Split(':')[0]);
            _logger = Logger.CreateLogger<TelegramBot>();
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

        private TelegramBotClient _bot;
        private readonly ILogger _logger;

        public DateTime LastMessageSent { get; private set; }

        public async Task Send(SentMessage message, RecivedMessage recivedMessage)
        {
            if (message.ChatId.Messenger != MessengerId)
            {
                // This message is for different messenger
                return;
            }
            
            LastMessageSent = DateTime.Now;

            IReplyMarkup replyMarkup;
            if (message.Buttons == null)
            {
                // Leave previous keyboard
                replyMarkup = null;
            }
            else
            {
                var markup = new KeyboardButton[message.Buttons.Length][];
                var keyboard = false;
                for (var i = 0; i < message.Buttons.Length; i++)
                {
                    var buttons = message.Buttons[i];
                    markup[i] = new KeyboardButton[buttons.Length];
                    for (var j = 0; j < buttons.Length; j++)
                    {
                        markup[i][j] = new KeyboardButton(buttons[j]);
                        keyboard = true;
                    }
                }

                if (keyboard)
                {
                    // Requested buttons is not empty
                    replyMarkup = new ReplyKeyboardMarkup(markup);
                }
                else
                {
                    // Requested buttons is empty, so remove keyboard entirely
                    replyMarkup = new ReplyKeyboardRemove();
                }
            }

            var parseMode = message.Formatted ? ParseMode.Markdown : ParseMode.Default;

            try
            {
                await _bot.SendTextMessageAsync(
                    message.ChatId.Id,
                    message.Text,
                    parseMode,
                    replyMarkup: replyMarkup
                    //replyToMessageId: recivedMessage?.ReplyId ?? 0  // Not working, because MessageId is different for each bot
                );
            }
            catch (Exception e)
            {
                if (e is ForbiddenException)
                {
                    // User stopped this bot.
                }
                else
                {
                    Yandex.Metrica.YandexMetrica.ReportError("Error while sending message", e);
                    _logger.LogError(e, "Error while sending message");
                }
            }
        }

        public event MessageHandler MessageRecieved;

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
            if (ReciveMessages)
            {
                _bot.OnMessage += MessageRecivedHandler;
                _bot.StartReceiving(Array.Empty<UpdateType>());
                _logger.LogInformation($"Start receiving for @{me.Username}");
            }
            else
            {
                _logger.LogInformation($"Start only sending for @{me.Username}");
            }
        }

        private void MessageRecivedHandler(object sender, MessageEventArgs args)
        {
            RecivedMessage message = null;

            var replyId = args.Message.Chat.Type != ChatType.Private ? (int?) args.Message.MessageId : null;

            switch (args.Message.Type)
            {
                case MessageType.Text:
                {
                    if (args.Message.Text == "/bots")
                    {
                        message = new RecivedMessage
                        {
                            ChatId = new ChatId(MessengerId, args.Message.Chat.Id),
                            UserId = new UserId(MessengerId, args.Message.From.Id),
                            Text = "Available bots:",
                            Action = (msg, user) => Messenger.ListBots(user),
                            ReplyId = replyId
                        };
                    }
                    else
                    {
                        message = new RecivedMessage
                        {
                            ChatId = new ChatId(MessengerId, args.Message.Chat.Id),
                            UserId = new UserId(MessengerId, args.Message.From.Id),
                            Text = args.Message.Text,
                            ReplyId = replyId
                        };
                    }

                    break;
                }
                case MessageType.ChatMembersAdded:
                {
                    foreach (var member in args.Message.NewChatMembers)
                    {
                        if (member.IsBot)
                        {
                            if (Messenger.MessengerIds.Contains(member.Id))
                            {
                                message = new RecivedMessage
                                {
                                    ChatId = new ChatId(MessengerId, args.Message.Chat.Id),
                                    UserId = new UserId(MessengerId, args.Message.From.Id),
                                    Text = $"Hello, bot {member.Username}",
                                    ReplyId = replyId,
                                    Action = (msg, user) => Messenger.NewBot(member.Id, args.Message.Chat.Id, user)
                                };
                            }
                        }
                        else
                        {
                            // Looks like new player
                            message = new RecivedMessage
                            {
                                ChatId = new ChatId(MessengerId, args.Message.Chat.Id),
                                UserId = new UserId(MessengerId, args.Message.From.Id),
                                Text = $"Hello, player {member.Username}",
                                ReplyId = replyId,
                                Action = (msg, user) => Messenger.NewUser(args.Message.Chat.Id, user)
                            };
                        }
                    }

                    break;
                }
                case MessageType.ChatMemberLeft:
                {
                    var member = args.Message.LeftChatMember;
                    if (member.IsBot && Messenger.MessengerIds.Contains(member.Id))
                    {
                        message = new RecivedMessage
                        {
                            ChatId = new ChatId(MessengerId, args.Message.Chat.Id),
                            UserId = new UserId(MessengerId, args.Message.From.Id),
                            Text = $"Goodbye, {member.Username}",
                            ReplyId = replyId,
                            Action = (msg, user) => Messenger.RemoveBot(member.Id, args.Message.Chat.Id, user)
                        };
                    }

                    break;
                }
                default:
                    return;
            }

            if (message != null)
            {
                MessageRecieved?.Invoke(message);
            }
        }
    }
}