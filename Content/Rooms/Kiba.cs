using System.Collections.Generic;
using AdventureBot;
using AdventureBot.Messenger;
using AdventureBot.Room;
using AdventureBot.User;

namespace Content.Rooms
{
    [Available(Id, Difficulity.Any, TownRoot.Id)]
    public class Kiba : RoomBase
    {
        public const string Id = "room/kiba";

        public Kiba()
        {
            Buttons = new NullableDictionary<MessageReceived, Dictionary<string, MessageReceived>>
            {
                {
                    null, new Dictionary<string, MessageReceived>
                    {
                        {"Уйти", (user, message) => user.RoomManager.Leave()}
                    }
                }
            };
        }

        public override string Name => "Киба";
        public override string Identifier => Id;

        public override void OnEnter(User user)
        {
            base.OnEnter(user);

            SendMessage(user, "— Я бы привез тебе лису, но отсюда до моей игры слишком дале...");
            SendMessage(user, "Он что, заснул?", GetButtons(user));
        }


        public override void OnMessage(User user, ReceivedMessage message)
        {
            HandleButtonAlways(user, message);
        }
    }
}