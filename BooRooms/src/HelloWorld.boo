namespace BooRooms

import AdventureBot.Messenger from AdventureBot
import AdventureBot.Room from AdventureBot
import AdventureBot.Room.BetterRoom from AdventureBot
import AdventureBot.User from AdventureBot

[Room("boo_hello")]
class HelloBoo(BetterRoomBase):
    public Name as string:
        get:
            return "BooHello"

    public Identifier as string:
        get:
            return "boo_hello"

    public def constructor():
        super(typeof(HelloBoo))

    public override def OnEnter(user as User):
        super(user)
        SwitchAction(user, typeof(MainHandler))
        SendMessage(user, "Welcome!", GetButtons(user))

    [Action]
    public class MainHandler(ActionBase):
        public def constructor(room as BetterRoomBase):
            super(room)

        [Button("Hello")]
        public def OnAsdf(user as User, message as RecivedMessage):
            Room.SendMessage(user, "Hello, world!", Room.GetButtons(user))
        
        [Button("Bye")]
        public def OnQwer(user as User, message as RecivedMessage):
            Room.SendMessage(user, "Goodbye!", Room.GetButtons(user))
            user.RoomManager.Leave()

        [Fallback]
        public def Fallback(user as User, message as RecivedMessage):
            Room.SendMessage(user, "Echo: " + message.Text, Room.GetButtons(user))
