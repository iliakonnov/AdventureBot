using AdventureBot.Messenger;
using AdventureBot.Room;
using AdventureBot.Room.BetterRoom;
using AdventureBot.User;

namespace Content.Rooms
{
    // Disabled
    [Room("better_test")]
    public class BetterTest : BetterRoomBase
    {
        public BetterTest() : base(typeof(BetterTest))
        {
        }

        public override string Name => "testing";
        public override string Identifier => "better_test";

        public override void OnEnter(User user)
        {
            base.OnEnter(user);
            SwitchAction(user, typeof(MainHandler));
            SendMessage(user, "Welcome!", GetButtons(user));
        }

        [Action]
        public class MainHandler : ActionBase
        {
            public MainHandler(BetterRoomBase room) : base(room)
            {
            }

            [Button("asdf")]
            public void OnAsdf(User user, RecivedMessage message)
            {
                Room.SwitchAction(user, typeof(Asdf));
                Room.SendMessage(user, "Switched!", Room.GetButtons(user));
            }
            
            [Button("qwer")]
            public void OnQwer(User user, RecivedMessage message)
            {
                Room.SwitchAction(user, typeof(Qwer));
                Room.SendMessage(user, "Switched!", Room.GetButtons(user));
            }

            [Fallback]
            public void Fallback(User user, RecivedMessage message)
            {
                Room.SendMessage(user, "Echo: " + message.Text, Room.GetButtons(user));
            }
        }
            
        [Action(0)]
        public class Asdf : ActionBase
        {
            public Asdf(BetterRoomBase room) : base(room)
            {
            }

            [Button("You are in asdf")]
            public void Hello(User user, RecivedMessage message)
            {
                Room.SendMessage(user, "Hello from asdf!", Room.GetButtons(user));
            }
            
            [Button("Back")]
            public void Back(User user, RecivedMessage message)
            {
                Room.SwitchAction(user, typeof(MainHandler));
                Room.SendMessage(user, "Goodbye", Room.GetButtons(user));
            }
            
            [Fallback]
            public void Fallback(User user, RecivedMessage message)
            {
                Room.SendMessage(user, "Echo (asdf): " + message.Text, Room.GetButtons(user));
            }
        }
        
        [Action(1)]
        public class Qwer : ActionBase
        {
            public Qwer(BetterRoomBase room) : base(room)
            {
            }

            [Button("You are in qwer")]
            public void Hello(User user, RecivedMessage message)
            {
                Room.SendMessage(user, "Hello from qwer!", Room.GetButtons(user));
            }
            
            [Button("Back")]
            public void Back(User user, RecivedMessage message)
            {
                Room.SwitchAction(user, typeof(MainHandler));
                Room.SendMessage(user, "Goodbye", Room.GetButtons(user));
            }
        }
    }
}