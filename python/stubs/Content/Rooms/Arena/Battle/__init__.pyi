from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import AdventureBot.Room.BetterRoom
import Content.Rooms.Arena
import System.Collections.Generic
import AdventureBot.Room
import AdventureBot.User
import AdventureBot.Messenger


class MainAction(AdventureBot.Room.BetterRoom.ActionBase[Content.Rooms.Arena.Battle]):
    @typing.overload
    def __init__(self, **kwargs):
        self.Buttons: System.Collections.Generic.Dictionary[str, AdventureBot.Room.MessageReceived]
        self.Room: AdventureBot.Room.BetterRoom.BetterRoomBase
        ...

    # static fields

    # properties
    @property
    def Room(self) -> Content.Rooms.Arena.Battle:
        ...

    # methods
    def __init__(self, room: Content.Rooms.Arena.Battle, ):
        ...

    def OnMessage(self, user: AdventureBot.User.User, message: AdventureBot.Messenger.ReceivedMessage, ) -> None:
        ...

