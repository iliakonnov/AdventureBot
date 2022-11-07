from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import AdventureBot.Room.BetterRoom
import Content.Rooms
import System.Collections.Generic
import AdventureBot.Room
import AdventureBot.User
import AdventureBot.Messenger


class MainAction(AdventureBot.Room.BetterRoom.ActionBase[Content.Rooms.Halls]):
    @typing.overload
    def __init__(self, **kwargs):
        self.Buttons: System.Collections.Generic.Dictionary[str, AdventureBot.Room.MessageReceived]
        self.Room: AdventureBot.Room.BetterRoom.BetterRoomBase
        ...

    # static fields

    # properties
    @property
    def Room(self) -> Content.Rooms.Halls:
        ...

    # methods
    def __init__(self, room: Content.Rooms.Halls, ):
        ...

    def Go(self, user: AdventureBot.User.User, message: AdventureBot.Messenger.ReceivedMessage, ) -> None:
        ...

    def Back(self, user: AdventureBot.User.User, message: AdventureBot.Messenger.ReceivedMessage, ) -> None:
        ...

