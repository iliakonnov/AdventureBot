using System.Collections.Generic;
using AdventureBot;
using AdventureBot.Messenger;
using AdventureBot.Room;
using AdventureBot.User;

namespace Content.Town
{
    [Room(Id)]
    public class Town : RoomBase
    {
        private const string Id = "town";

        public Town()
        {
            Buttons = new NullableDictionary<MessageRecived, Dictionary<string, MessageRecived>>
            {
                {
                    null, new Dictionary<string, MessageRecived>
                    {
                        {"Приключения", (user, message) => user.RoomManager.Go("town/adventures")},
                        {"Зеркало", (user, message) => user.RoomManager.Go("town/mirror")},
                        {"Рынок", (user, message) => user.RoomManager.Go("town/market")},
                        {"Таверна", (user, message) => user.RoomManager.Go("town/tavern")},
                        {"Гильдия магов", (user, message) => user.RoomManager.Go("town/guild")},
                        {"Спортзал", (user, message) => user.RoomManager.Go("town/gym")}
                    }
                }
            };
        }

        public override string Identifier { get; } = Id;
        public override string Name { get; } = "Город";

        public override void OnReturn(User user)
        {
            OnEnter(user);
        }

        public override void OnEnter(User user)
        {
            SendMessage(user, "Добро пожаловать в Город!", GetButtons(user));
        }

        public override bool OnLeave(User user)
        {
            // SendMessage(user, "Вы покидаете Город...", GetButtons(user));
            return true;
        }

        public override void OnMessage(User user, RecivedMessage message)
        {
            HandleButtonAlways(user, message);
        }
    }
}