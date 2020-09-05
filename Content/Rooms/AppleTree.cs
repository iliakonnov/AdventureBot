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
    public class AppleTree : RoomBase
    {
        public const string Id = "room/appletree";

        public AppleTree()
        {
            Buttons = new NullableDictionary<MessageReceived, Dictionary<string, MessageReceived>>
            {
                {
                    null, new Dictionary<string, MessageReceived>
                    {
                        {
                            "Залезть наверх", (user, message) =>
                            {
                                SendMessage(
                                    user,
                                    "Ты стал карабкаться по веткам и случайно сбил одно яблоко. Оно упало на голову какому-то чудаковатому англичанина, сидевшему в тени ветвей. Вместо того, чтобы посмотреть наверх, он записал что-то в своей тетради и убежал куда-то в сторону Кембриджа. Тетрадь он оставил под яблоней."
                                );
                                user.ItemManager.Add(new ItemInfo(Notebook.Id, 1));
                                user.RoomManager.Leave();
                            }
                        },
                        {"Уйти", (user, message) => user.RoomManager.Leave()}
                    }
                }
            };
        }

        public override string Name => "Яблоня";
        public override string Identifier => Id;

        public override void OnEnter(User user)
        {
            base.OnEnter(user);

            SendMessage(
                user,
                "У тебя возникло непреодолимое желание отведать яблок, но они висят слишком высоко.",
                GetButtons(user)
            );
        }


        public override void OnMessage(User user, ReceivedMessage message)
        {
            HandleButtonAlways(user, message);
        }
    }
}