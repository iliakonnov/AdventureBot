using System.Collections.Generic;
using System.Linq;
using AdventureBot;
using AdventureBot.Messenger;
using AdventureBot.ObjectManager;
using AdventureBot.Room;
using AdventureBot.User;
using RoomManager = AdventureBot.User.RoomManager;

namespace Content.Town
{
    [Room(identifier)]
    public class Town : RoomBase
    {
        private const string identifier = "town";
        public override string Identifier { get; } = identifier;
        public override string Name { get; } = "Город";

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
                        {"Гильдия магов", (user, message) => user.RoomManager.Go("town/guild")},
                        {"Спортзал", (user, message) => user.RoomManager.Go("town/gym")}
                    }
                }
            };
        }

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