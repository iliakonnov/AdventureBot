using System;
using System.Collections.Generic;
using System.Linq;
using AdventureBot.ObjectManager;
using AdventureBot.User;
using JetBrains.Annotations;
using NLog;

namespace AdventureBot.Messenger;

public class MessengerManager : IManager<IMessenger>
{
    private static readonly Logger Logger = LogManager.GetCurrentClassLogger();
    private readonly List<IMessenger> _messengers = new();

    public void Register(GameObjectAttribute attribute, Create<IMessenger> creator)
    {
        if (!(attribute is MessengerAttribute))
        {
            return;
        }

        Register(creator());
    }

    public static event GameEventHandler<ReceivedMessage> OnReceived;

    private static void MessageHandler(ReceivedMessage message)
    {
        if (message == null)
        {
            return;
        }

        using (var context = new UserContext(message.UserId, message.ChatId))
        {
            User.User user = context;
            OnReceived?.Invoke(user, message);

            try
            {
                user.MessageManager.ReceivedMessage = message;
                message.Action?.Invoke(message, user);

                switch (message.Text.Split('@')[0].Split(' ')[0])
                {
                    case "/start":
                    {
                        user.RoomManager.Go("_root", false);
                        break;
                    }
                    case "/repeat":
                    {
                        user.MessageManager.SendImmediately(user.MessageManager.LastMessages.Last());
                        break;
                    }
                    case "/token":
                    {
                        user.MessageManager.SendImmediately(new SentMessage
                        {
                            Text = $@"Ваш токен: `{user.Token}`.
Используйте его чтобы связать другой аккаунт с этим персонажем (`/link {user.Info.UserId.Messenger} {user.Info.UserId.Id} {user.Token}`).
Чтобы сгенерировать новый токен используйте `/revoke`",
                            Intent = "command-token"
                        });
                        break;
                    }
                    case "/revoke":
                    {
                        user.Token = Guid.NewGuid();
                        user.MessageManager.SendImmediately(new SentMessage
                        {
                            Text = $"Ваш новый токен: <code>{user.Token}</code>.",
                            Intent = "command-revoke"
                        });
                        break;
                    }
                    case "/link":
                    {
                        var splitted = message.Text.Split(' ');
                        if (splitted.Length != 4
                            || !int.TryParse(splitted[1], out var messenger)
                            || !long.TryParse(splitted[2], out var id)
                            || !Guid.TryParse(splitted[3], out var token))
                        {
                            user.MessageManager.SendImmediately(new SentMessage
                            {
                                Text =
                                    @"Чтобы связвть этот аккаунт с другим игровым персонажем используйте <code>/link <messenger_id> <user_id> <token></code>",
                                Intent = "command-link-error"
                            });
                            break;
                        }

                        var uid = new UserId(messenger, id);

                        if (uid.Equals(user.Info.UserId))
                        {
                            user.MessageManager.SendImmediately(new SentMessage
                            {
                                Text = @"К сожалению, нельзя связаться с самим собой",
                                Intent = "command-link-self"
                            });
                            break;
                        }

                        using (var linkTo = new UserContext(uid))
                        {
                            if (linkTo.User.Token != token)
                            {
                                user.MessageManager.SendImmediately(new SentMessage
                                {
                                    Text = @"Не удалось связать аккаунты. Проверьте, всё ли правильно вы ввели",
                                    Intent = "command-link-forbidden"
                                });
                                break;
                            }
                        }

                        user.LinkedTo = new Tuple<UserId, Guid>(uid, token);
                        user.MessageManager.SendImmediately(new SentMessage
                        {
                            Text = @"Отлично! Чтобы отвязать аккаунт используйте <code>/unlink</code>",
                            Intent = "command-link"
                        });
                        break;
                    }
                    case "/unlink":
                    {
                        if (context.Unlink())
                        {
                            user.MessageManager.SendImmediately(new SentMessage
                            {
                                Text = @"Готово!",
                                Intent = "command-unlink"
                            });
                        }
                        else
                        {
                            user.MessageManager.SendImmediately(new SentMessage
                            {
                                Text = "Вы и так ни к кому не привязаны",
                                Intent = "command-unlink-fail"
                            });
                        }

                        break;
                    }
                    default:
                    {
                        user.MessageManager.OnReceived(message);
                        break;
                    }
                }

                user.MessageManager.Finish();
            }
            catch (Exception e)
            {
                Logger.Error(e, "Error for user {UserId}@{ChatId}", message.UserId, message.ChatId);
                var error = MessageManager.Escape(e.ToString());
                user.MessageManager.SendImmediately(new SentMessage
                {
                    Text = $"Вы пошатнули мироздание и произошла ошибка:\n<pre>{error}</pre>",
                    Intent = "error"
                });
            }
        }
    }

    public void Register(IMessenger messenger)
    {
        messenger.MessageReceived += MessageHandler;
        _messengers.Add(messenger);
    }

    public void BeginPolling()
    {
        _messengers.ForEach(m => m.BeginPolling());
    }

    public static event GameEventHandler<Tuple<SentMessage, ReceivedMessage>> OnReply;

    public void Reply(SentMessage message, [CanBeNull] ReceivedMessage receivedMessage, User.User user)
    {
        OnReply?.Invoke(user, new Tuple<SentMessage, ReceivedMessage>(message, receivedMessage));
        foreach (var messenger in _messengers)
        {
            messenger.Send(message, receivedMessage, user);
        }
    }
}