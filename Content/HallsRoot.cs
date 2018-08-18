// Just demo for testing of changing between different roots

using System;
using AdventureBot.Messenger;
using AdventureBot.Room;
using AdventureBot.Room.BetterRoom;
using AdventureBot.User;
using Content.Town;

namespace Content
{
    [Root(Id)]
    public class HallsRoot : IRoot
    {
        public const string Id = "root/halls";
        public string Identifier => Id;
        public string RootRoomId => Halls.Id;
    }

    [Room(Id)]
    public class Halls : BetterRoomBase
    {
        public Halls() : base(typeof(Halls))
        {
        }

        public const string Id = "halls";
        public override string Name => "Чертоги";
        public override string Identifier => Id;

        public override void OnEnter(User user)
        {
            SwitchAction<MainAction>(user);
            SendMessage(user, "Добро пожаловать в Чертоги! Рады вас видеть!", GetButtons(user));
        }
        
        [Action]
        public class MainAction : ActionBase {
            public MainAction(BetterRoomBase room) : base(room)
            {
            }
            
            [Button("Привет")]
            public void Hi(User user, RecivedMessage message)
            {
                Room.SendMessage(user, "Привет", Room.GetButtons(user));
            }

            [Button("В город")]
            public void Town(User user, RecivedMessage message)
            {
                Room.SendMessage(user, "Пока!");
                user.RoomManager.ChangeRoot(TownRoot.Id);
            }
        }
        
    }
}