using System.Collections.Generic;
using AdventureBot;
using AdventureBot.Messenger;
using AdventureBot.Room;
using AdventureBot.User;

namespace Content.Rooms
{
    [Available("room/wedding")]
    public class Wedding : RoomBase
    {
        public Wedding()
        {
            Routes = new MessageRecived[] {TryLeave};
            Buttons = new NullableDictionary<MessageRecived, Dictionary<string, MessageRecived>>
            {
                {
                    null, new Dictionary<string, MessageRecived>
                    {
                        {"Попытаться уйти", (user, message) => SwitchAndHandle(user, TryLeave, message)},
                        {"Выпить с ними", (user, message) => user.RoomManager.Leave()}
                    }
                },
                {
                    TryLeave, new Dictionary<string, MessageRecived>
                    {
                        {"Выпить с ними", (user, message) => user.RoomManager.Leave()}
                    }
                }
            };
        }

        public override string Name => "Грузинская свадьба";
        public override string Identifier => "room/wedding";

        public override void OnEnter(User user)
        {
            SwitchAction(user, null);
            SendMessage(user, "Танцы, песни, вино рекой. Все как положено.");
            SendMessage(user, "Хозяева пригашают тебя на рюмку вина.", GetButtons(user));
        }

        public void TryLeave(User user, RecivedMessage message)
        {
            SendMessage(user, "Ты почувствовал, как мимо твоего уха пролетел нож.", GetButtons(user));
        }

        public override bool OnLeave(User user)
        {
            SendMessage(user, "Ты очнулся в городе. Что случилось на свадьбе — вечная загадка для тебя.");
            return true;
        }

        public override void OnMessage(User user, RecivedMessage message)
        {
            HandleButtonAlways(user, message);
        }
    }
}