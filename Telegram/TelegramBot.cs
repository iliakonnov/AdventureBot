using System;
using System.Net;
using System.Threading.Tasks;
using AdventureBot;
using AdventureBot.Messenger;
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

        public async Task Send(SentMessage message, RecivedMessage recivedMessage)
        {
            if (message.ChatId.Messenger != MessengerId)
            {
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
                    replyMarkup = new ReplyKeyboardMarkup(markup) {Selective = true};
                }
                else
                {
                    replyMarkup = new ReplyKeyboardRemove {Selective = true};
                }
            }

            var parseMode = message.Formatted ? ParseMode.Html : ParseMode.Default;

            var text = message.Text;
            if (recivedMessage?.ReplyUserId != null)
            {
                text += $"\n<a href=\"tg://user?id={recivedMessage.ReplyUserId}\">@</a>";
            }

            try
            {
                await _bot.SendTextMessageAsync(
                    message.ChatId.Id,
                    text,
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
                    Logger.Error(e, "Error while sending message");
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
            _username = me.Username;
            if (ReciveMessages)
            {
                _bot.OnMessage += MessageRecivedHandler;
                _bot.StartReceiving(Array.Empty<UpdateType>());
                Logger.Info("Start receiving for @{username}", _username);
            }
            else
            {
                Logger.Info("Start only sending for @{username}", _username);
            }
        }

        private async void MessageRecivedHandler(object sender, MessageEventArgs args)
        {
            RecivedMessage message = null;

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
            switch (args.Message.Type)
            {
                case MessageType.Text:
                {
                    if (args.Message.Text == "/bots")
                    {
                        message = new RecivedMessage
                        {
                            ChatId = new AdventureBot.ChatId(MessengerId, args.Message.Chat.Id),
                            UserId = new UserId(MessengerId, args.Message.From.Id),
                            Text = "Available bots:",
                            Action = (msg, user) => Messenger.ListBots(user),
                            ReplyUserId = replyId,
                            MessageId = msgId
                        };
                    }
                    else
                    {
                        message = new RecivedMessage
                        {
                            ChatId = new AdventureBot.ChatId(MessengerId, args.Message.Chat.Id),
                            UserId = new UserId(MessengerId, args.Message.From.Id),
                            Text = args.Message.Text,
                            ReplyUserId = replyId,
                            MessageId = msgId
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
                                    ChatId = new AdventureBot.ChatId(MessengerId, args.Message.Chat.Id),
                                    UserId = new UserId(MessengerId, args.Message.From.Id),
                                    Text = $"Hello, bot {member.Username}",
                                    ReplyUserId = replyId,
                                    Action = (msg, user) => Messenger.NewBot(member.Id, args.Message.Chat.Id, user),
                                    MessageId = msgId
                                };
                            }
                        }
                        else
                        {
                            // Looks like new player
                            message = new RecivedMessage
                            {
                                ChatId = new AdventureBot.ChatId(MessengerId, args.Message.Chat.Id),
                                UserId = new UserId(MessengerId, args.Message.From.Id),
                                Text = $"Hello, player {member.Username}",
                                ReplyUserId = replyId,
                                Action = (msg, user) => Messenger.NewUser(args.Message.Chat.Id, user),
                                MessageId = msgId
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
                            ChatId = new AdventureBot.ChatId(MessengerId, args.Message.Chat.Id),
                            UserId = new UserId(MessengerId, args.Message.From.Id),
                            Text = $"Goodbye, {member.Username}",
                            ReplyUserId = replyId,
                            Action = (msg, user) => Messenger.RemoveBot(member.Id, args.Message.Chat.Id, user),
                            MessageId = msgId
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