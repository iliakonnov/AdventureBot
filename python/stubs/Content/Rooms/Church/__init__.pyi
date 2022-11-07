from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import AdventureBot.Room.BetterRoom
import Content.Rooms
import System.Collections.Generic
import AdventureBot.Room
import AdventureBot.User
import AdventureBot.Messenger


class Donat(AdventureBot.Room.BetterRoom.ActionBase[Content.Rooms.Church]):
    @typing.overload
    def __init__(self, **kwargs):
        self.Buttons: System.Collections.Generic.Dictionary[str, AdventureBot.Room.MessageReceived]
        self.Room: AdventureBot.Room.BetterRoom.BetterRoomBase
        ...

    # static fields

    # properties
    @property
    def Room(self) -> Content.Rooms.Church:
        ...

    # methods
    def __init__(self, room: Content.Rooms.Church, ):
        ...

    def DonatMinium(self, user: AdventureBot.User.User, message: AdventureBot.Messenger.ReceivedMessage, ) -> None:
        ...

    def Donat750(self, user: AdventureBot.User.User, message: AdventureBot.Messenger.ReceivedMessage, ) -> None:
        ...

    def DonatMaximum(self, user: AdventureBot.User.User, message: AdventureBot.Messenger.ReceivedMessage, ) -> None:
        ...

    def Leave(self, user: AdventureBot.User.User, message: AdventureBot.Messenger.ReceivedMessage, ) -> None:
        ...

class MainHandler(AdventureBot.Room.BetterRoom.ActionBase[Content.Rooms.Church]):
    @typing.overload
    def __init__(self, **kwargs):
        self.Buttons: System.Collections.Generic.Dictionary[str, AdventureBot.Room.MessageReceived]
        self.Room: AdventureBot.Room.BetterRoom.BetterRoomBase
        ...

    # static fields

    # properties
    @property
    def Room(self) -> Content.Rooms.Church:
        ...

    # methods
    def __init__(self, room: Content.Rooms.Church, ):
        ...

    def OnDonat(self, user: AdventureBot.User.User, message: AdventureBot.Messenger.ReceivedMessage, ) -> None:
        ...

    def Leave(self, user: AdventureBot.User.User, message: AdventureBot.Messenger.ReceivedMessage, ) -> None:
        ...

