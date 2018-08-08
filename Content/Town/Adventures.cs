using System.Collections.Generic;
using System.Linq;
using AdventureBot;
using AdventureBot.Item;
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
            Routes = new MessageRecived[] {RoomSelection};
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
            SwitchAction(user, null);
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
            if (!HandleAction(user, message))
            {
                HandleButtonAlways(user, message);
            }
        }

        public override void OnReturn(User user)
        {
            const decimal k = 0.2m;
            user.Info.ChangeStats(StatsProperty.Mana, user.Info.MaxStats.Effect[StatsProperty.Mana] * k);
            user.Info.ChangeStats(StatsProperty.Stamina, user.Info.MaxStats.Effect[StatsProperty.Mana] * k);
            user.Info.ChangeStats(StatsProperty.Health, user.Info.MaxStats.Effect[StatsProperty.Mana] * k);

            SendMessage(user, "Вы вернулись в город, отдохнули и теперь лучше себя чувствуете.");

            foreach (var info in user.ItemManager.Items)
            {
                if (info.Item is IAdventureItem adventureItem)
                {
                    adventureItem.OnAdventureLeave(user, info);
                }
            }

            user.RoomManager.Leave();
        }

        private static List<string> GetRooms(Difficulity difficulity)
        {
            return GetAllRooms().Items()
                .Where(room => room.Attribute is AvailableAttribute attr && (attr.Difficulity & difficulity) != 0)
                .OrderBy(room => room.Identificator)
                .Select(room => room.Identificator)
                .ToList();
        }

        private static string GetRandomRoom(User user, Difficulity difficulity)
        {
            var rooms = GetRooms(difficulity);
            return rooms[user.Random.Next(rooms.Count)];
        }

        private void AskRoom(User user, Difficulity difficulity)
        {
            var selectedRoom = GetRandomRoom(user, difficulity);
            GetRoomVariables(user).Set("room", new Serializable.String(selectedRoom));
            SendMessage(user,
                $"Ты идешь по лесу и видишь на поляне *{GetAllRooms().Get(selectedRoom)?.Name}*",
                new[] {new[] {"Пойти в лес"}, new[] {"Пойти на поляну"}}
            );
        }

        private void RoomSelection(User user, RecivedMessage message)
        {
            var variables = GetRoomVariables(user);
            var difficulity = (Difficulity) (int) variables.Get<Serializable.Int>("difficulity");
            var count = (int) variables.Get<Serializable.Int>("count");
            count--;
            switch (message.Text)
            {
                case "Пойти в лес" when count <= 0:
                {
                    // Last room
                    SendMessage(user, "Дальше идти некуда");
                    break;
                }
                case "Пойти в лес":
                {
                    AskRoom(user, difficulity);
                    variables.Set("count", new Serializable.Int(count));
                    break;
                }
                case "Пойти на поляну":
                {
                    var selectedRoom = (string) variables.Get<Serializable.String>("room");
                    SwitchRoom(user, selectedRoom);
                    break;
                }
            }
        }

        private void Go(User user, Difficulity difficulity)
        {
            var rooms = GetRooms(difficulity);
            if (rooms.Count == 0)
            {
                SendMessage(user, "Ты побродил по лесу, но так ничего и не нашел.");
                user.RoomManager.Leave();
            }
            else if (user.ItemManager.Get("item/slippers") != null)
            {
                GetRoomVariables(user).Set("difficulity", new Serializable.Int((int) difficulity));
                GetRoomVariables(user).Set("count", new Serializable.Int(user.Random.Next(3, 5 + 1)));
                AskRoom(user, difficulity);
                SwitchAction(user, RoomSelection);
            }
            else
            {
                var selectedRoom = GetRandomRoom(user, difficulity);
                SwitchRoom(user, selectedRoom);
            }
        }

        private static void SwitchRoom(User user, string room)
        {
            user.RoomManager.Go(room);
            foreach (var info in user.ItemManager.Items)
            {
                if (info.Item is IAdventureItem adventureItem)
                {
                    adventureItem.OnAdventureEnter(user, info);
                }
            }
        }
    }
}