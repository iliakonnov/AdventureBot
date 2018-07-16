using System.Collections.Generic;
using AdventureBot;
using AdventureBot.Messenger;
using AdventureBot.ObjectManager;
using AdventureBot.Room;
using AdventureBot.User;
using AdventureBot.User.Stats;

namespace Content.Town
{
    [Room("town/gym")]
    public class Gym : RoomBase
    {
        public override string Name => "Спортзал";
        public override string Identifier => "town/gym";

        public Gym()
        {
            Buttons = new NullableDictionary<MessageRecived, Dictionary<string, MessageRecived>>
            {
                {
                    null, new Dictionary<string, MessageRecived>
                    {
                        {"Уйти", (user, message) => user.RoomManager.Leave()},
                        {
                            "Потренироваться", (user, message) =>
                            {
                                SendMessage(user, "Вы не успели договорить, а уже отлетелии в дальний угол.");
                                user.Info.ChangeStats(StatsProperty.Health, -30);
                            }
                        },
                        {
                            "Подкачаться", (user, message) =>
                            {
                                if (user.Info.ChangeStats(StatsProperty.Stamina, -10))
                                {
                                    user.Info.ChangeStats(StatsProperty.Strength, 1.1m);
                                    SendMessage(user, "Вы стали чуточку сильнее");
                                }
                                else
                                {
                                    SendMessage(user, "Вы слишком устали и не можете сейчас тренироваться");
                                }
                            }
                        }
                    }
                }
            };
        }

        public override void OnEnter(User user)
        {
            if (user.Info.CurrentStats.Effect[StatsProperty.Intelligence] > 10)
            {
                SendMessage(user, "Вам больше не рады в Спортзале");
                user.RoomManager.Leave();
                return;
            }

            user.MessageManager.ShownStats = ShownStats.Health | ShownStats.Strength | ShownStats.Stamina;
            SendMessage(user, "Вас встречает какой-то тренер.", GetButtons(user));
        }

        public override bool OnLeave(User user)
        {
            SendMessage(user, "Вы уходите от тренера");

            return true;
        }

        public override void OnMessage(User user, RecivedMessage message)
        {
            if (!HandleAction(user, message))
            {
                HandleButtonAlways(user, message);
            }
        }
    }
}