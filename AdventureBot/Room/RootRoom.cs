using System.Collections.Generic;
using AdventureBot.Messenger;

namespace AdventureBot.Room
{
    [Room(Id)]
    public class RootRoom : RoomBase
    {
        private const string Id = "_root";

        public RootRoom()
        {
            Routes = new MessageRecived[] {ConfirmRestart};
            Buttons = new NullableDictionary<MessageRecived, Dictionary<string, MessageRecived>>
            {
                {
                    ConfirmRestart, new Dictionary<string, MessageRecived>
                    {
                        {"Да", (user, message) => NewGame(user, "Ну раз вы так хотите, то ладно.")},
                        {
                            "Нет", (user, message) => { user.RoomManager.Leave(false); }
                        }
                    }
                }
            };
        }

        public override string Name { get; } = string.Empty;
        public override string Identifier { get; } = Id;

        public override void OnEnter(User.User user)
        {
            SwitchAction(user, ConfirmRestart);
            SendMessage(user,
                !user.Info.Dead
                    ? "Неужели хотите начать новую игру?"
                    : "Вы оказались в мире мертвых. Хотите играть?",
                GetButtons(user));
        }

        private void NewGame(User.User user, string message = null)
        {
            user.Reset();
            if (message != null)
            {
                SendMessage(user, message);
            }

            user.Info.Dead = false;
            user.RoomManager.ChangeRoot("root/town");
        }

        public override bool OnLeave(User.User user)
        {
            if (user.Info.Dead)
            {
                SendMessage(user, "Вы пытались покинуть мир мертвых, но страж вас не пропускает.");
                return false;
            }

            var buttons = new string[0][];

            var prevRoom = user.RoomManager.Rooms.Peek();
            if (prevRoom?.LastMessage != null)
            {
                buttons = prevRoom.LastMessage.Buttons;
            }

            SendMessage(user, "Вы покидаете мир мертвых и отправляетесь путешествовать.", buttons);
            return true;
        }

        public override void OnMessage(User.User user, RecivedMessage message)
        {
            HandleAction(user, message);
        }

        private void ConfirmRestart(User.User user, RecivedMessage message)
        {
            HandleButtonAlways(user, message);
        }

        public override void OnReturn(User.User user)
        {
            if (user.Info.Dead)
            {
                SendMessage(user, "Ох, вы умерли. Какая неудача!");
            }
            else
            {
                SendMessage(user, "Живых не должно быть в мире метрвых.");
                user.RoomManager.Go(user.RoomManager.CurrentRootRoom);
            }
        }
    }
}