using System;
using System.Collections.Generic;
using System.Linq;
using AdventureBot.Analysis;
using AdventureBot.ObjectManager;
using AdventureBot.User;
using JetBrains.Annotations;
using MessagePack;
using NLog;
using Yandex.Metrica;

namespace AdventureBot.Messenger
{
    public class MessengerManager : IManager<IMessenger>
    {
        private static readonly Logger Logger = LogManager.GetCurrentClassLogger();
        private readonly List<IMessenger> _messengers = new List<IMessenger>();

        public void Register(GameObjectAttribute attribute, Create<IMessenger> creator)
        {
            if (!(attribute is MessengerAttribute))
            {
                return;
            }

            Register(creator());
        }

        private void MessageHandler(RecivedMessage message)
        {
            if (message == null)
            {
                return;
            }

#if DEBUG
            Logger.Debug($"Message from {message.UserId}@{message.ChatId}");
#endif
            using (var context = new UserContext(message.UserId, message.ChatId))
            {
                User.User user = context;

                // Analyzer.Chatbase.ReciveMessage(user, message);

                try
                {
                    user.MessageManager.RecievedMessage = message;
                    message.Action?.Invoke(message, user);

                    switch (message.Text.Split('@')[0])
                    {
                        case "/start":
                        {
                            user.RoomManager.Go("_root", false);
                            break;
                        }
                        case "/debug":
                        {
                            var serialized = MessageManager.Escape(MessagePackSerializer.ToJson(
                                new PublicUser(user)
                            ));
                            user.MessageManager.SendImmediately(new SentMessage
                            {
                                Text = $"Всё про вас:\n```\n{serialized}\n```",
                                Intent = "command-debug"
                            });
                            break;
                        }
                        case "/lag":
                        {
                            user.MessageManager.SendImmediately(new SentMessage
                            {
                                Text =
                                    @"Если бот долго отвечает, то создайте беседу и обязательно пригласите туда @AdventureTownBot.
После этого пригласите туда @PocketTownBot и @MonsterTownBot",
                                Intent = "command-lag"
                            });
                            break;
                        }
                        case "/repeat":
                        {
                            user.MessageManager.SendImmediately(user.MessageManager.LastMessages.Last());
                            break;
                        }
                        default:
                        {
                            user.MessageManager.OnRecieved(message);
                            break;
                        }
                    }

                    user.MessageManager.Finish();
                }
                catch (Exception e)
                {
                    YandexMetrica.ReportError($"Error for user {message.UserId}@{message.ChatId}", e);
                    Logger.Error(e, $"Error for user {message.UserId}@{message.ChatId}");
                    var error = MessageManager.Escape(e.ToString());
                    user.MessageManager.SendImmediately(new SentMessage
                    {
                        Text = $"Вы пошатнули мироздание и произошла ошибка:\n```{error}```",
                        Intent = "error"
                    });
                }
            }
        }

        public void Register(IMessenger messenger)
        {
            messenger.MessageRecieved += MessageHandler;
            _messengers.Add(messenger);
            messenger.BeginPolling();
        }

        public void Reply(SentMessage message, [CanBeNull] RecivedMessage recievedMessage, User.User user)
        {
            message.SentTime = DateTimeOffset.UtcNow;
            Events.Message(user, message, recievedMessage);
            foreach (var messenger in _messengers)
            {
                messenger.Send(message, recievedMessage, user);
            }
        }
    }
}