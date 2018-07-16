using System.Collections.Generic;
using AdventureBot;
using AdventureBot.Item;
using AdventureBot.Messenger;
using AdventureBot.Room;
using AdventureBot.User;

namespace Content.Rooms
{
    [Available("room/worms")]
    public class Worms : RoomBase
    {
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
        public override string Identifier => "room/worms";

        public override void OnEnter(User user)
        {
            SendMessage(
                user,
                "В террариуме оказалось несколько червяков, палящих друг по другу миниатюрными, но ничуть не менее опасными базуками.",
                GetButtons(user)
            );
        }

        public override bool OnLeave(User user)
        {
            user.ItemManager.Add(new ItemInfo("worms/worm", 3));
            SendMessage(user, "Перед уходом ты подобрал бездыханные тела бравых бойцов.");
            return true;
        }

        public override void OnMessage(User user, RecivedMessage message)
        {
            HandleButtonAlways(user, message);
        }
    }
}