using System.Collections.Generic;
using AdventureBot;
using AdventureBot.Item;
using AdventureBot.Messenger;
using AdventureBot.Room;
using AdventureBot.User;
using Content.Items;

namespace Content.Rooms
{
    [Available(Id, Difficulity.Any, TownRoot.Id)]
    public class Worms : RoomBase
    {
        public const string Id = "room/worms";

        public Worms()
        {
            Buttons = new NullableDictionary<MessageRecived, Dictionary<string, MessageRecived>>
            {
                {
                    null, new Dictionary<string, MessageRecived>
                    {
                        {
                            "Уйти", (user, message) => { user.RoomManager.Leave(); }
                        }
                    }
                }
            };
        }

        public override string Name => "Террариум";
        public override string Identifier => Id;

        public override void OnEnter(User user)
        {
            base.OnEnter(user);

            SendMessage(
                user,
                "В террариуме оказалось несколько червяков, палящих друг по другу миниатюрными, но ничуть не менее опасными базуками.",
                GetButtons(user)
            );
        }

        public override bool OnLeave(User user)
        {
            base.OnLeave(user);

            user.ItemManager.Add(new ItemInfo(Worm.Id, 3));
            SendMessage(user, "Перед уходом ты подобрал бездыханные тела бравых бойцов.");
            return true;
        }

        public override void OnMessage(User user, RecivedMessage message)
        {
            HandleButtonAlways(user, message);
        }
    }
}