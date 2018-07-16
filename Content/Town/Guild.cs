using System.Collections.Generic;
using AdventureBot;
using AdventureBot.Messenger;
using AdventureBot.Room;
using AdventureBot.User;
using AdventureBot.User.Stats;

namespace Content.Town
{
    [Room("town/guild")]
    public class Guild : RoomBase
    {
        public Guild()
        {
            Buttons = new NullableDictionary<MessageRecived, Dictionary<string, MessageRecived>>
            {
                {
                    null, new Dictionary<string, MessageRecived>
                    {
                        {"Уйти", (user, message) => user.RoomManager.Leave()},
                        {
                            "А насколько вы древний?", (user, message) =>
                            {
                                SendMessage(user, "Маг чуть не треснул вас посохом, но молния всё-таки попала.");
                                user.Info.Kill();
                            }
                        },
                        {
                            "Подучиться", (user, message) =>
                            {
                                if (user.Info.ChangeStats(StatsProperty.Mana, -10))
                                {
                                    user.Info.ChangeStats(StatsProperty.Intelligence, 1.1m);
                                    SendMessage(user, "Вы стали чуточку умнее");
                                }
                                else
                                {
                                    SendMessage(user, "Вот когда будет мана, тогда и приходите");
                                }
                            }
                        }
                    }
                }
            };
        }

        public override string Name => "Гильдия магов";
        public override string Identifier => "town/guild";

        public override void OnEnter(User user)
        {
            if (user.Info.CurrentStats.Effect[StatsProperty.Strength] > 10)
            {
                SendMessage(user, "Вам больше не рады в Гильдии");
                user.RoomManager.Leave();
                return;
            }

            user.MessageManager.ShownStats = ShownStats.Health | ShownStats.Mana | ShownStats.Intelligence;
            SendMessage(user, "Вас встречает древний маг.", GetButtons(user));
        }

        public override bool OnLeave(User user)
        {
            SendMessage(user, "Вы уходите от мага");

            return true;
        }

        public override void OnMessage(User user, RecivedMessage message)
        {
            if (!HandleAction(user, message)) HandleButtonAlways(user, message);
        }
    }
}