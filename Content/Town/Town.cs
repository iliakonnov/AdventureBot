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
        public const string Id = "town";

        public Town()
        {
            Buttons = new NullableDictionary<MessageRecived, Dictionary<string, MessageRecived>>
            {
                {
                    null, new Dictionary<string, MessageRecived>
                    {
                        {"Приключения", (user, message) => user.RoomManager.Go(Adventures.Id)},
                        {"Зеркало", (user, message) => user.RoomManager.Go(Mirror.Id)},
                        {"Рынок", (user, message) => user.RoomManager.Go(Market.Id)},
                        {"Таверна", (user, message) => user.RoomManager.Go(Tavern.Id)},
                        {"Гильдия магов", (user, message) => user.RoomManager.Go(Guild.Id)},
                        {"Спортзал", (user, message) => user.RoomManager.Go(Gym.Id)},
                        {"Чертоги", (user, message) => user.RoomManager.ChangeRoot("root/halls")}
                    }
                }
            };
        }

        public override string Identifier => Id;
        public override string Name => "Город";

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