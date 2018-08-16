using System.Collections.Generic;
using AdventureBot;
using AdventureBot.Messenger;
using AdventureBot.Room;
using AdventureBot.User;

namespace Content.Rooms
{
    [Available(Id, Difficulity.Any)]
    public class Kiba : RoomBase
    {
        public const string Id = "room/kiba";

        public Kiba()
        {
            Buttons = new NullableDictionary<MessageRecived, Dictionary<string, MessageRecived>>
            {
                {
                    null, new Dictionary<string, MessageRecived>
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


        public override void OnMessage(User user, RecivedMessage message)
        {
            HandleButtonAlways(user, message);
        }
    }
}