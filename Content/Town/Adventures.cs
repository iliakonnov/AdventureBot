using System.Collections.Generic;
using System.Linq;
using AdventureBot;
using AdventureBot.Messenger;
using AdventureBot.Room;
using AdventureBot.User;
using AdventureBot.User.Stats;

namespace Content.Town
{
    [Room("town/adventures")]
    public class Adventures : RoomBase
    {
        public Adventures()
        {
            Buttons = new NullableDictionary<MessageRecived, Dictionary<string, MessageRecived>>
            {
                {
                    null, new Dictionary<string, MessageRecived>
                    {
                        {"Налево", (user, message) => Go(user, Difficulity.Easy)},
                        {"Направо", (user, message) => Go(user, Difficulity.Medium)},
                        {"Прямо", (user, message) => Go(user, Difficulity.Hard)},
                        {"Назад", (user, message) => user.RoomManager.Leave()}
                    }
                }
            };
        }

        public override string Name => "Приключения";
        public override string Identifier => "town/adventures";

        public override void OnEnter(User user)
        {
            SendMessage(
                user,
                "Ты вышел из города на полянку. Тут стоит указательный камень, который укажет тебе путь к приключениям. Куда пойдешь?",
                GetButtons(user)
            );
        }

        public override bool OnLeave(User user)
        {
            return true;
        }

        public override void OnMessage(User user, RecivedMessage message)
        {
            HandleButtonAlways(user, message);
        }

        public override void OnReturn(User user)
        {
            const decimal k = 0.2m;
            user.Info.ChangeStats(StatsProperty.Mana, user.Info.MaxStats.Effect[StatsProperty.Mana] * k);
            user.Info.ChangeStats(StatsProperty.Stamina, user.Info.MaxStats.Effect[StatsProperty.Mana] * k);
            user.Info.ChangeStats(StatsProperty.Health, user.Info.MaxStats.Effect[StatsProperty.Mana] * k);

            SendMessage(user, "Вы вернулись в город, отдохнули и теперь лучше себя чувствуете.");
            user.RoomManager.Leave();
        }

        private void Go(User user, Difficulity difficulity)
        {
            var roomMgr = GetAllRooms();
            var rooms = roomMgr.Items()
                .Where(room => room.Attribute is AvailableAttribute attr && (attr.Difficulity & difficulity) != 0)
                .Select(room => room.Identificator)
                .ToList();
            if (rooms.Count == 0)
            {
                SendMessage(user, "Ты побродил по лесу, но так ничего и не нашел.");
                user.RoomManager.Leave();
            }
            else
            {
                user.RoomManager.Go(rooms[user.Random.Next(rooms.Count)]);
            }
        }
    }
}