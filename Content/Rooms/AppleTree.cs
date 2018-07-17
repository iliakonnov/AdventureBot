using System.Collections.Generic;
using AdventureBot;
using AdventureBot.Item;
using AdventureBot.Messenger;
using AdventureBot.Room;
using AdventureBot.User;

namespace Content.Rooms
{
    [Available("room/appletree", Difficulity.Any)]
    public class AppleTree : RoomBase
    {
        public AppleTree()
        {
            Buttons = new NullableDictionary<MessageRecived, Dictionary<string, MessageRecived>>
            {
                {
                    null, new Dictionary<string, MessageRecived>
                    {
                        {
                            "Залезть наверх", (user, message) =>
                            {
                                SendMessage(
                                    user,
                                    "Ты стал карабкаться по веткам и случайно сбил одно яблоко. Оно упало на голову какому-то чудаковатому англичанина, сидевшему в тени ветвей. Вместо того, чтобы посмотреть наверх, он записал что-то в своей тетради и убежал куда-то в сторону Кембриджа. Тетрадь он оставил под яблоней."
                                );
                                user.ItemManager.Add(new ItemInfo("appletree/notebook", 1));
                                user.RoomManager.Leave();
                            }
                        },
                        {"Уйти", (user, message) => user.RoomManager.Leave()}
                    }
                }
            };
        }

        public override string Name => "Яблоня";
        public override string Identifier => "room/appletree";

        public override void OnEnter(User user)
        {
            SendMessage(
                user,
                "У тебя возникло непреодолимое желание отведать яблок, но они висят слишком высоко.",
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
    }
}