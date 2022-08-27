using System.Collections.Generic;
using AdventureBot;
using AdventureBot.Messenger;
using AdventureBot.Room;
using AdventureBot.User;
using AdventureBot.User.Stats;

namespace Content.Town;

[Room(Id)]
public class Gym : RoomBase
{
    public const string Id = "town/gym";

    public Gym()
    {
        Buttons = new NullableDictionary<MessageReceived, Dictionary<string, MessageReceived>>
        {
            {
                null, new Dictionary<string, MessageReceived>
                {
                    {"Уйти", (user, message) => user.RoomManager.Leave()},
                    {
                        "Потренироваться", (user, message) =>
                        {
                            SendMessage(user, "Вы не успели договорить, а уже отлетелии в дальний угол.");
                            user.Info.MakeDamage(30);
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

    public override string Name => "Спортзал";
    public override string Identifier => Id;

    public override void OnEnter(User user)
    {
        if (user.Info.CurrentStats.GetStat(StatsProperty.Intelligence) > 10)
        {
            SendMessage(user, "Вам больше не рады в Спортзале");
            user.RoomManager.Leave();
            return;
        }

        user.MessageManager.ShownStats = ShownStats.Health | ShownStats.Strength | ShownStats.Stamina;
        SendMessage(user, "Вас встречает Александр Невский.");
        SendMessage(user, "— Вот так вот! Вот так вот!", GetButtons(user));
    }

    public override bool OnLeave(User user)
    {
        SendMessage(user, "Вы уходите от тренера");

        return true;
    }

    public override void OnMessage(User user, ReceivedMessage message)
    {
        if (!HandleAction(user, message))
        {
            HandleButtonAlways(user, message);
        }
    }
}