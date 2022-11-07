from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import AdventureBot.Room.BetterRoom
import Content.Halls
import System.Collections.Generic
import AdventureBot.Room
import AdventureBot.User
import AdventureBot.Messenger


class BuyOther(AdventureBot.Room.BetterRoom.ActionBase[Content.Halls.Weaponsmith]):
    @typing.overload
    def __init__(self, **kwargs):
        self.Buttons: System.Collections.Generic.Dictionary[str, AdventureBot.Room.MessageReceived]
        self.Room: AdventureBot.Room.BetterRoom.BetterRoomBase
        ...

    # static fields

    # properties
    @property
    def Room(self) -> Content.Halls.Weaponsmith:
        ...

    # methods
    def __init__(self, room: Content.Halls.Weaponsmith, ):
        ...

    def Nothing(self, user: AdventureBot.User.User, message: AdventureBot.Messenger.ReceivedMessage, ) -> None:
        ...

    def HandleButton(self, user: AdventureBot.User.User, message: AdventureBot.Messenger.ReceivedMessage, ) -> None:
        ...

class MainAction(AdventureBot.Room.BetterRoom.ActionBase[Content.Halls.Weaponsmith]):
    @typing.overload
    def __init__(self, **kwargs):
        self.Buttons: System.Collections.Generic.Dictionary[str, AdventureBot.Room.MessageReceived]
        self.Room: AdventureBot.Room.BetterRoom.BetterRoomBase
        ...

    # static fields

    # properties
    @property
    def Room(self) -> Content.Halls.Weaponsmith:
        ...

    # methods
    def __init__(self, room: Content.Halls.Weaponsmith, ):
        ...

    def Stock(self, user: AdventureBot.User.User, message: AdventureBot.Messenger.ReceivedMessage, ) -> None:
        ...

    def Weapon(self, user: AdventureBot.User.User, message: AdventureBot.Messenger.ReceivedMessage, ) -> None:
        ...

    def MirrorAction(self, user: AdventureBot.User.User, message: AdventureBot.Messenger.ReceivedMessage, ) -> None:
        ...

    def LeaveHalls(self, user: AdventureBot.User.User, message: AdventureBot.Messenger.ReceivedMessage, ) -> None:
        ...

    def Leave(self, user: AdventureBot.User.User, message: AdventureBot.Messenger.ReceivedMessage, ) -> None:
        ...

class BuyWeapon(AdventureBot.Room.BetterRoom.ActionBase[Content.Halls.Weaponsmith]):
    @typing.overload
    def __init__(self, **kwargs):
        self.Buttons: System.Collections.Generic.Dictionary[str, AdventureBot.Room.MessageReceived]
        self.Room: AdventureBot.Room.BetterRoom.BetterRoomBase
        ...

    # static fields

    # properties
    @property
    def Room(self) -> Content.Halls.Weaponsmith:
        ...

    # methods
    def __init__(self, room: Content.Halls.Weaponsmith, ):
        ...

    def Nothing(self, user: AdventureBot.User.User, message: AdventureBot.Messenger.ReceivedMessage, ) -> None:
        ...

    def HandleButton(self, user: AdventureBot.User.User, message: AdventureBot.Messenger.ReceivedMessage, ) -> None:
        ...

