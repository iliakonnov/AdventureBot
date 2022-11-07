from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import AdventureBot.Room
import Content.Quests
import System
import AdventureBot
import System.Collections.Generic
import AdventureBot.User
import AdventureBot.Messenger
import Content.Rooms
import AdventureBot.Room.BetterRoom


class Camper(AdventureBot.Room.IRoom, AdventureBot.Room.IMonster, Content.Quests.IQuestMonster, AdventureBot.Room.MonsterBase):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields
    Id: str = ...

    # properties
    @property
    def Health(self) -> System.Decimal:
        ...

    @property
    def Name(self) -> str:
        ...

    @property
    def Identifier(self) -> str:
        ...

    @property
    def Routes(self) -> System.Array[AdventureBot.Room.MessageReceived]:
        ...
    @Routes.setter
    def Routes(self, val: System.Array[AdventureBot.Room.MessageReceived]):
        ...

    @property
    def Buttons(self) -> AdventureBot.NullableDictionary[AdventureBot.Room.MessageReceived, System.Collections.Generic.Dictionary[str, AdventureBot.Room.MessageReceived]]:
        ...
    @Buttons.setter
    def Buttons(self, val: AdventureBot.NullableDictionary[AdventureBot.Room.MessageReceived, System.Collections.Generic.Dictionary[str, AdventureBot.Room.MessageReceived]]):
        ...

    # methods
    def __init__(self, ):
        ...

    def GetDamage(self, user: AdventureBot.User.User, ) -> System.Decimal:
        ...

    def Enter(self, user: AdventureBot.User.User, buttons: System.Array[System.Array[str]], ) -> None:
        ...

    def OnRunaway(self, user: AdventureBot.User.User, ) -> bool:
        ...

    def OnWon(self, user: AdventureBot.User.User, ) -> None:
        ...

class Anime(AdventureBot.Room.IRoom, AdventureBot.Room.IMonster, Content.Quests.IQuestMonster, AdventureBot.Room.MonsterBase):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields
    Id: str = ...

    # properties
    @property
    def Health(self) -> System.Decimal:
        ...

    @property
    def Name(self) -> str:
        ...

    @property
    def Identifier(self) -> str:
        ...

    @property
    def Routes(self) -> System.Array[AdventureBot.Room.MessageReceived]:
        ...
    @Routes.setter
    def Routes(self, val: System.Array[AdventureBot.Room.MessageReceived]):
        ...

    @property
    def Buttons(self) -> AdventureBot.NullableDictionary[AdventureBot.Room.MessageReceived, System.Collections.Generic.Dictionary[str, AdventureBot.Room.MessageReceived]]:
        ...
    @Buttons.setter
    def Buttons(self, val: AdventureBot.NullableDictionary[AdventureBot.Room.MessageReceived, System.Collections.Generic.Dictionary[str, AdventureBot.Room.MessageReceived]]):
        ...

    # methods
    def __init__(self, ):
        ...

    def GetDamage(self, user: AdventureBot.User.User, ) -> System.Decimal:
        ...

    def Enter(self, user: AdventureBot.User.User, buttons: System.Array[System.Array[str]], ) -> None:
        ...

    def OnRunaway(self, user: AdventureBot.User.User, ) -> bool:
        ...

    def OnWon(self, user: AdventureBot.User.User, ) -> None:
        ...

class DarthVader(AdventureBot.Room.IRoom, AdventureBot.Room.RoomBase):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields
    Id: str = ...

    # properties
    @property
    def Name(self) -> str:
        ...

    @property
    def Identifier(self) -> str:
        ...

    @property
    def Routes(self) -> System.Array[AdventureBot.Room.MessageReceived]:
        ...
    @Routes.setter
    def Routes(self, val: System.Array[AdventureBot.Room.MessageReceived]):
        ...

    @property
    def Buttons(self) -> AdventureBot.NullableDictionary[AdventureBot.Room.MessageReceived, System.Collections.Generic.Dictionary[str, AdventureBot.Room.MessageReceived]]:
        ...
    @Buttons.setter
    def Buttons(self, val: AdventureBot.NullableDictionary[AdventureBot.Room.MessageReceived, System.Collections.Generic.Dictionary[str, AdventureBot.Room.MessageReceived]]):
        ...

    # methods
    def __init__(self, ):
        ...

    def OnEnter(self, user: AdventureBot.User.User, ) -> None:
        ...

    def OnMessage(self, user: AdventureBot.User.User, message: AdventureBot.Messenger.ReceivedMessage, ) -> None:
        ...

    def PreBattle(self, user: AdventureBot.User.User, message: AdventureBot.Messenger.ReceivedMessage, ) -> None:
        ...

    def Battle(self, user: AdventureBot.User.User, message: AdventureBot.Messenger.ReceivedMessage, ) -> None:
        ...

class Kiba(AdventureBot.Room.IRoom, AdventureBot.Room.RoomBase):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields
    Id: str = ...

    # properties
    @property
    def Name(self) -> str:
        ...

    @property
    def Identifier(self) -> str:
        ...

    @property
    def Routes(self) -> System.Array[AdventureBot.Room.MessageReceived]:
        ...
    @Routes.setter
    def Routes(self, val: System.Array[AdventureBot.Room.MessageReceived]):
        ...

    @property
    def Buttons(self) -> AdventureBot.NullableDictionary[AdventureBot.Room.MessageReceived, System.Collections.Generic.Dictionary[str, AdventureBot.Room.MessageReceived]]:
        ...
    @Buttons.setter
    def Buttons(self, val: AdventureBot.NullableDictionary[AdventureBot.Room.MessageReceived, System.Collections.Generic.Dictionary[str, AdventureBot.Room.MessageReceived]]):
        ...

    # methods
    def __init__(self, ):
        ...

    def OnEnter(self, user: AdventureBot.User.User, ) -> None:
        ...

    def OnMessage(self, user: AdventureBot.User.User, message: AdventureBot.Messenger.ReceivedMessage, ) -> None:
        ...

class GrammarNazi(AdventureBot.Room.IRoom, AdventureBot.Room.IMonster, Content.Quests.IQuestMonster, AdventureBot.Room.MonsterBase):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields
    Id: str = ...

    # properties
    @property
    def Health(self) -> System.Decimal:
        ...

    @property
    def Name(self) -> str:
        ...

    @property
    def Identifier(self) -> str:
        ...

    @property
    def Routes(self) -> System.Array[AdventureBot.Room.MessageReceived]:
        ...
    @Routes.setter
    def Routes(self, val: System.Array[AdventureBot.Room.MessageReceived]):
        ...

    @property
    def Buttons(self) -> AdventureBot.NullableDictionary[AdventureBot.Room.MessageReceived, System.Collections.Generic.Dictionary[str, AdventureBot.Room.MessageReceived]]:
        ...
    @Buttons.setter
    def Buttons(self, val: AdventureBot.NullableDictionary[AdventureBot.Room.MessageReceived, System.Collections.Generic.Dictionary[str, AdventureBot.Room.MessageReceived]]):
        ...

    # methods
    def __init__(self, ):
        ...

    def GetDamage(self, user: AdventureBot.User.User, ) -> System.Decimal:
        ...

    def Enter(self, user: AdventureBot.User.User, buttons: System.Array[System.Array[str]], ) -> None:
        ...

    def OnRunaway(self, user: AdventureBot.User.User, ) -> bool:
        ...

    def OnWon(self, user: AdventureBot.User.User, ) -> None:
        ...

    def NotHandled(self, user: AdventureBot.User.User, message: AdventureBot.Messenger.ReceivedMessage, ) -> None:
        ...

class Thanos(AdventureBot.Room.IRoom, AdventureBot.Room.IMonster, AdventureBot.Room.MonsterBase):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields
    Id: str = ...

    # properties
    @property
    def Name(self) -> str:
        ...

    @property
    def Identifier(self) -> str:
        ...

    @property
    def Health(self) -> System.Decimal:
        ...

    @property
    def Routes(self) -> System.Array[AdventureBot.Room.MessageReceived]:
        ...
    @Routes.setter
    def Routes(self, val: System.Array[AdventureBot.Room.MessageReceived]):
        ...

    @property
    def Buttons(self) -> AdventureBot.NullableDictionary[AdventureBot.Room.MessageReceived, System.Collections.Generic.Dictionary[str, AdventureBot.Room.MessageReceived]]:
        ...
    @Buttons.setter
    def Buttons(self, val: AdventureBot.NullableDictionary[AdventureBot.Room.MessageReceived, System.Collections.Generic.Dictionary[str, AdventureBot.Room.MessageReceived]]):
        ...

    # methods
    def __init__(self, ):
        ...

    def GetDamage(self, user: AdventureBot.User.User, ) -> System.Decimal:
        ...

    def Enter(self, user: AdventureBot.User.User, buttons: System.Array[System.Array[str]], ) -> None:
        ...

    def OnRunaway(self, user: AdventureBot.User.User, ) -> bool:
        ...

    def OnWon(self, user: AdventureBot.User.User, ) -> None:
        ...

class Dormammu(AdventureBot.Room.IRoom, AdventureBot.Room.IMonster, AdventureBot.Room.MonsterBase):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields
    Id: str = ...

    # properties
    @property
    def Name(self) -> str:
        ...

    @property
    def Identifier(self) -> str:
        ...

    @property
    def Health(self) -> System.Decimal:
        ...

    @property
    def Routes(self) -> System.Array[AdventureBot.Room.MessageReceived]:
        ...
    @Routes.setter
    def Routes(self, val: System.Array[AdventureBot.Room.MessageReceived]):
        ...

    @property
    def Buttons(self) -> AdventureBot.NullableDictionary[AdventureBot.Room.MessageReceived, System.Collections.Generic.Dictionary[str, AdventureBot.Room.MessageReceived]]:
        ...
    @Buttons.setter
    def Buttons(self, val: AdventureBot.NullableDictionary[AdventureBot.Room.MessageReceived, System.Collections.Generic.Dictionary[str, AdventureBot.Room.MessageReceived]]):
        ...

    # methods
    def __init__(self, ):
        ...

    def GetDamage(self, user: AdventureBot.User.User, ) -> System.Decimal:
        ...

    def Enter(self, user: AdventureBot.User.User, buttons: System.Array[System.Array[str]], ) -> None:
        ...

    def OnMessage(self, user: AdventureBot.User.User, message: AdventureBot.Messenger.ReceivedMessage, ) -> None:
        ...

    def OnRunaway(self, user: AdventureBot.User.User, ) -> bool:
        ...

    def OnWon(self, user: AdventureBot.User.User, ) -> None:
        ...

class VaderBattle(AdventureBot.Room.IRoom, AdventureBot.Room.IMonster, Content.Quests.IQuestMonster, AdventureBot.Room.MonsterBase):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields
    Id: str = ...

    # properties
    @property
    def Health(self) -> System.Decimal:
        ...

    @property
    def Name(self) -> str:
        ...

    @property
    def Identifier(self) -> str:
        ...

    @property
    def Routes(self) -> System.Array[AdventureBot.Room.MessageReceived]:
        ...
    @Routes.setter
    def Routes(self, val: System.Array[AdventureBot.Room.MessageReceived]):
        ...

    @property
    def Buttons(self) -> AdventureBot.NullableDictionary[AdventureBot.Room.MessageReceived, System.Collections.Generic.Dictionary[str, AdventureBot.Room.MessageReceived]]:
        ...
    @Buttons.setter
    def Buttons(self, val: AdventureBot.NullableDictionary[AdventureBot.Room.MessageReceived, System.Collections.Generic.Dictionary[str, AdventureBot.Room.MessageReceived]]):
        ...

    # methods
    def __init__(self, ):
        ...

    def GetDamage(self, user: AdventureBot.User.User, ) -> System.Decimal:
        ...

    def Enter(self, user: AdventureBot.User.User, buttons: System.Array[System.Array[str]], ) -> None:
        ...

    def OnRunaway(self, user: AdventureBot.User.User, ) -> bool:
        ...

    def OnWon(self, user: AdventureBot.User.User, ) -> None:
        ...

class HardWedding(AdventureBot.Room.IRoom, Content.Rooms.Wedding):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def Name(self) -> str:
        ...

    @property
    def Identifier(self) -> str:
        ...

    @property
    def Routes(self) -> System.Array[AdventureBot.Room.MessageReceived]:
        ...
    @Routes.setter
    def Routes(self, val: System.Array[AdventureBot.Room.MessageReceived]):
        ...

    @property
    def Buttons(self) -> AdventureBot.NullableDictionary[AdventureBot.Room.MessageReceived, System.Collections.Generic.Dictionary[str, AdventureBot.Room.MessageReceived]]:
        ...
    @Buttons.setter
    def Buttons(self, val: AdventureBot.NullableDictionary[AdventureBot.Room.MessageReceived, System.Collections.Generic.Dictionary[str, AdventureBot.Room.MessageReceived]]):
        ...

    # methods
    def __init__(self, ):
        ...

    def OnLeave(self, user: AdventureBot.User.User, ) -> bool:
        ...

class Wedding(AdventureBot.Room.IRoom, AdventureBot.Room.RoomBase):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields
    Id: str = ...

    # properties
    @property
    def Name(self) -> str:
        ...

    @property
    def Identifier(self) -> str:
        ...

    @property
    def Routes(self) -> System.Array[AdventureBot.Room.MessageReceived]:
        ...
    @Routes.setter
    def Routes(self, val: System.Array[AdventureBot.Room.MessageReceived]):
        ...

    @property
    def Buttons(self) -> AdventureBot.NullableDictionary[AdventureBot.Room.MessageReceived, System.Collections.Generic.Dictionary[str, AdventureBot.Room.MessageReceived]]:
        ...
    @Buttons.setter
    def Buttons(self, val: AdventureBot.NullableDictionary[AdventureBot.Room.MessageReceived, System.Collections.Generic.Dictionary[str, AdventureBot.Room.MessageReceived]]):
        ...

    # methods
    def __init__(self, ):
        ...

    def OnLeave(self, user: AdventureBot.User.User, ) -> bool:
        ...

    def OnEnter(self, user: AdventureBot.User.User, ) -> None:
        ...

    def TryLeave(self, user: AdventureBot.User.User, message: AdventureBot.Messenger.ReceivedMessage, ) -> None:
        ...

    def OnMessage(self, user: AdventureBot.User.User, message: AdventureBot.Messenger.ReceivedMessage, ) -> None:
        ...

class Starlight(AdventureBot.Room.IRoom, AdventureBot.Room.IMonster, Content.Quests.IQuestMonster, AdventureBot.Room.MonsterBase):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields
    Id: str = ...

    # properties
    @property
    def Health(self) -> System.Decimal:
        ...

    @property
    def Name(self) -> str:
        ...

    @property
    def Identifier(self) -> str:
        ...

    @property
    def Routes(self) -> System.Array[AdventureBot.Room.MessageReceived]:
        ...
    @Routes.setter
    def Routes(self, val: System.Array[AdventureBot.Room.MessageReceived]):
        ...

    @property
    def Buttons(self) -> AdventureBot.NullableDictionary[AdventureBot.Room.MessageReceived, System.Collections.Generic.Dictionary[str, AdventureBot.Room.MessageReceived]]:
        ...
    @Buttons.setter
    def Buttons(self, val: AdventureBot.NullableDictionary[AdventureBot.Room.MessageReceived, System.Collections.Generic.Dictionary[str, AdventureBot.Room.MessageReceived]]):
        ...

    # methods
    def __init__(self, ):
        ...

    def GetDamage(self, user: AdventureBot.User.User, ) -> System.Decimal:
        ...

    def Enter(self, user: AdventureBot.User.User, buttons: System.Array[System.Array[str]], ) -> None:
        ...

    def OnRunaway(self, user: AdventureBot.User.User, ) -> bool:
        ...

    def OnWon(self, user: AdventureBot.User.User, ) -> None:
        ...

class FirstBoss(AdventureBot.Room.IRoom, AdventureBot.Room.IMonster, AdventureBot.Room.BossBase):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields
    Id: str = ...

    # properties
    @property
    def Name(self) -> str:
        ...

    @property
    def Identifier(self) -> str:
        ...

    @property
    def InitialGold(self) -> System.Decimal:
        ...

    @property
    def Health(self) -> System.Decimal:
        ...

    @property
    def Routes(self) -> System.Array[AdventureBot.Room.MessageReceived]:
        ...
    @Routes.setter
    def Routes(self, val: System.Array[AdventureBot.Room.MessageReceived]):
        ...

    @property
    def Buttons(self) -> AdventureBot.NullableDictionary[AdventureBot.Room.MessageReceived, System.Collections.Generic.Dictionary[str, AdventureBot.Room.MessageReceived]]:
        ...
    @Buttons.setter
    def Buttons(self, val: AdventureBot.NullableDictionary[AdventureBot.Room.MessageReceived, System.Collections.Generic.Dictionary[str, AdventureBot.Room.MessageReceived]]):
        ...

    # methods
    def __init__(self, ):
        ...

    def GetDamage(self, user: AdventureBot.User.User, ) -> System.Decimal:
        ...

class Geek(AdventureBot.Room.IRoom, AdventureBot.Room.IMonster, Content.Quests.IQuestMonster, AdventureBot.Room.MonsterBase):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields
    Id: str = ...

    # properties
    @property
    def Health(self) -> System.Decimal:
        ...

    @property
    def Name(self) -> str:
        ...

    @property
    def Identifier(self) -> str:
        ...

    @property
    def Routes(self) -> System.Array[AdventureBot.Room.MessageReceived]:
        ...
    @Routes.setter
    def Routes(self, val: System.Array[AdventureBot.Room.MessageReceived]):
        ...

    @property
    def Buttons(self) -> AdventureBot.NullableDictionary[AdventureBot.Room.MessageReceived, System.Collections.Generic.Dictionary[str, AdventureBot.Room.MessageReceived]]:
        ...
    @Buttons.setter
    def Buttons(self, val: AdventureBot.NullableDictionary[AdventureBot.Room.MessageReceived, System.Collections.Generic.Dictionary[str, AdventureBot.Room.MessageReceived]]):
        ...

    # methods
    def __init__(self, ):
        ...

    def OnMessage(self, user: AdventureBot.User.User, message: AdventureBot.Messenger.ReceivedMessage, ) -> None:
        ...

    def GetDamage(self, user: AdventureBot.User.User, ) -> System.Decimal:
        ...

    def GetActions(self, user: AdventureBot.User.User, ) -> System.Array[System.Array[str]]:
        ...

    def Enter(self, user: AdventureBot.User.User, buttons: System.Array[System.Array[str]], ) -> None:
        ...

    def OnRunaway(self, user: AdventureBot.User.User, ) -> bool:
        ...

    def OnWon(self, user: AdventureBot.User.User, ) -> None:
        ...

class AppleTree(AdventureBot.Room.IRoom, AdventureBot.Room.RoomBase):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields
    Id: str = ...

    # properties
    @property
    def Name(self) -> str:
        ...

    @property
    def Identifier(self) -> str:
        ...

    @property
    def Routes(self) -> System.Array[AdventureBot.Room.MessageReceived]:
        ...
    @Routes.setter
    def Routes(self, val: System.Array[AdventureBot.Room.MessageReceived]):
        ...

    @property
    def Buttons(self) -> AdventureBot.NullableDictionary[AdventureBot.Room.MessageReceived, System.Collections.Generic.Dictionary[str, AdventureBot.Room.MessageReceived]]:
        ...
    @Buttons.setter
    def Buttons(self, val: AdventureBot.NullableDictionary[AdventureBot.Room.MessageReceived, System.Collections.Generic.Dictionary[str, AdventureBot.Room.MessageReceived]]):
        ...

    # methods
    def __init__(self, ):
        ...

    def OnEnter(self, user: AdventureBot.User.User, ) -> None:
        ...

    def OnMessage(self, user: AdventureBot.User.User, message: AdventureBot.Messenger.ReceivedMessage, ) -> None:
        ...

class Voldemort(AdventureBot.Room.IRoom, AdventureBot.Room.IMonster, AdventureBot.Room.MonsterBase):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields
    Id: str = ...

    # properties
    @property
    def Name(self) -> str:
        ...

    @property
    def Identifier(self) -> str:
        ...

    @property
    def Health(self) -> System.Decimal:
        ...

    @property
    def Routes(self) -> System.Array[AdventureBot.Room.MessageReceived]:
        ...
    @Routes.setter
    def Routes(self, val: System.Array[AdventureBot.Room.MessageReceived]):
        ...

    @property
    def Buttons(self) -> AdventureBot.NullableDictionary[AdventureBot.Room.MessageReceived, System.Collections.Generic.Dictionary[str, AdventureBot.Room.MessageReceived]]:
        ...
    @Buttons.setter
    def Buttons(self, val: AdventureBot.NullableDictionary[AdventureBot.Room.MessageReceived, System.Collections.Generic.Dictionary[str, AdventureBot.Room.MessageReceived]]):
        ...

    # methods
    def __init__(self, ):
        ...

    def GetDamage(self, user: AdventureBot.User.User, ) -> System.Decimal:
        ...

    def Enter(self, user: AdventureBot.User.User, buttons: System.Array[System.Array[str]], ) -> None:
        ...

    def OnRunaway(self, user: AdventureBot.User.User, ) -> bool:
        ...

    def OnWon(self, user: AdventureBot.User.User, ) -> None:
        ...

class Portal(AdventureBot.Room.IRoom, AdventureBot.Room.BetterRoom.BetterRoomBase[Content.Rooms.Portal]):
    @typing.overload
    def __init__(self, **kwargs):
        self._actions: System.Collections.Generic.Dictionary[System.Type, AdventureBot.Room.BetterRoom.ActionBase]
        self._rootAction: AdventureBot.Room.BetterRoom.ActionBase
        ...

    # static fields
    Id: str = ...

    # properties
    @property
    def Name(self) -> str:
        ...

    @property
    def Identifier(self) -> str:
        ...

    @property
    def actions(self) -> System.Array[System.Type]:
        ...

    @property
    def Routes(self) -> System.Array[AdventureBot.Room.MessageReceived]:
        ...
    @Routes.setter
    def Routes(self, val: System.Array[AdventureBot.Room.MessageReceived]):
        ...

    @property
    def Buttons(self) -> AdventureBot.NullableDictionary[AdventureBot.Room.MessageReceived, System.Collections.Generic.Dictionary[str, AdventureBot.Room.MessageReceived]]:
        ...
    @Buttons.setter
    def Buttons(self, val: AdventureBot.NullableDictionary[AdventureBot.Room.MessageReceived, System.Collections.Generic.Dictionary[str, AdventureBot.Room.MessageReceived]]):
        ...

    # methods
    def __init__(self, ):
        ...

    def OnEnter(self, user: AdventureBot.User.User, ) -> None:
        ...

class Hedgehog(AdventureBot.Room.IRoom, AdventureBot.Room.IMonster, Content.Quests.IQuestMonster, AdventureBot.Room.MonsterBase):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields
    Id: str = ...

    # properties
    @property
    def Health(self) -> System.Decimal:
        ...

    @property
    def Name(self) -> str:
        ...

    @property
    def Identifier(self) -> str:
        ...

    @property
    def Routes(self) -> System.Array[AdventureBot.Room.MessageReceived]:
        ...
    @Routes.setter
    def Routes(self, val: System.Array[AdventureBot.Room.MessageReceived]):
        ...

    @property
    def Buttons(self) -> AdventureBot.NullableDictionary[AdventureBot.Room.MessageReceived, System.Collections.Generic.Dictionary[str, AdventureBot.Room.MessageReceived]]:
        ...
    @Buttons.setter
    def Buttons(self, val: AdventureBot.NullableDictionary[AdventureBot.Room.MessageReceived, System.Collections.Generic.Dictionary[str, AdventureBot.Room.MessageReceived]]):
        ...

    # methods
    def __init__(self, ):
        ...

    def GetDamage(self, user: AdventureBot.User.User, ) -> System.Decimal:
        ...

    def Enter(self, user: AdventureBot.User.User, buttons: System.Array[System.Array[str]], ) -> None:
        ...

    def OnRunaway(self, user: AdventureBot.User.User, ) -> bool:
        ...

    def OnWon(self, user: AdventureBot.User.User, ) -> None:
        ...

class SkeletonSwordsman(AdventureBot.Room.IRoom, AdventureBot.Room.IMonster, Content.Quests.IQuestMonster, AdventureBot.Room.MonsterBase):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields
    Id: str = ...

    # properties
    @property
    def Health(self) -> System.Decimal:
        ...

    @property
    def Name(self) -> str:
        ...

    @property
    def Identifier(self) -> str:
        ...

    @property
    def Routes(self) -> System.Array[AdventureBot.Room.MessageReceived]:
        ...
    @Routes.setter
    def Routes(self, val: System.Array[AdventureBot.Room.MessageReceived]):
        ...

    @property
    def Buttons(self) -> AdventureBot.NullableDictionary[AdventureBot.Room.MessageReceived, System.Collections.Generic.Dictionary[str, AdventureBot.Room.MessageReceived]]:
        ...
    @Buttons.setter
    def Buttons(self, val: AdventureBot.NullableDictionary[AdventureBot.Room.MessageReceived, System.Collections.Generic.Dictionary[str, AdventureBot.Room.MessageReceived]]):
        ...

    # methods
    def __init__(self, ):
        ...

    def GetDamage(self, user: AdventureBot.User.User, ) -> System.Decimal:
        ...

    def Enter(self, user: AdventureBot.User.User, buttons: System.Array[System.Array[str]], ) -> None:
        ...

    def OnRunaway(self, user: AdventureBot.User.User, ) -> bool:
        ...

    def OnWon(self, user: AdventureBot.User.User, ) -> None:
        ...

class Sans(AdventureBot.Room.IRoom, AdventureBot.Room.IMonster, Content.Quests.IQuestMonster, AdventureBot.Room.MonsterBase):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields
    Id: str = ...

    # properties
    @property
    def Health(self) -> System.Decimal:
        ...

    @property
    def Name(self) -> str:
        ...

    @property
    def Identifier(self) -> str:
        ...

    @property
    def Routes(self) -> System.Array[AdventureBot.Room.MessageReceived]:
        ...
    @Routes.setter
    def Routes(self, val: System.Array[AdventureBot.Room.MessageReceived]):
        ...

    @property
    def Buttons(self) -> AdventureBot.NullableDictionary[AdventureBot.Room.MessageReceived, System.Collections.Generic.Dictionary[str, AdventureBot.Room.MessageReceived]]:
        ...
    @Buttons.setter
    def Buttons(self, val: AdventureBot.NullableDictionary[AdventureBot.Room.MessageReceived, System.Collections.Generic.Dictionary[str, AdventureBot.Room.MessageReceived]]):
        ...

    # methods
    def __init__(self, ):
        ...

    def MakeDamage(self, user: AdventureBot.User.User, damage: System.Decimal, ) -> None:
        ...

    def GetDamage(self, user: AdventureBot.User.User, ) -> System.Decimal:
        ...

    def Enter(self, user: AdventureBot.User.User, buttons: System.Array[System.Array[str]], ) -> None:
        ...

    def OnRunaway(self, user: AdventureBot.User.User, ) -> bool:
        ...

    def OnWon(self, user: AdventureBot.User.User, ) -> None:
        ...

class GordonRamsey(AdventureBot.Room.IRoom, AdventureBot.Room.IMonster, Content.Quests.IQuestMonster, AdventureBot.Room.MonsterBase):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields
    Id: str = ...

    # properties
    @property
    def Health(self) -> System.Decimal:
        ...

    @property
    def Name(self) -> str:
        ...

    @property
    def Identifier(self) -> str:
        ...

    @property
    def Routes(self) -> System.Array[AdventureBot.Room.MessageReceived]:
        ...
    @Routes.setter
    def Routes(self, val: System.Array[AdventureBot.Room.MessageReceived]):
        ...

    @property
    def Buttons(self) -> AdventureBot.NullableDictionary[AdventureBot.Room.MessageReceived, System.Collections.Generic.Dictionary[str, AdventureBot.Room.MessageReceived]]:
        ...
    @Buttons.setter
    def Buttons(self, val: AdventureBot.NullableDictionary[AdventureBot.Room.MessageReceived, System.Collections.Generic.Dictionary[str, AdventureBot.Room.MessageReceived]]):
        ...

    # methods
    def __init__(self, ):
        ...

    def GetDamage(self, user: AdventureBot.User.User, ) -> System.Decimal:
        ...

    def Enter(self, user: AdventureBot.User.User, buttons: System.Array[System.Array[str]], ) -> None:
        ...

    def OnRunaway(self, user: AdventureBot.User.User, ) -> bool:
        ...

    def OnWon(self, user: AdventureBot.User.User, ) -> None:
        ...

class Jason(AdventureBot.Room.IRoom, AdventureBot.Room.IMonster, Content.Quests.IQuestMonster, AdventureBot.Room.MonsterBase):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields
    Id: str = ...

    # properties
    @property
    def Health(self) -> System.Decimal:
        ...

    @property
    def Name(self) -> str:
        ...

    @property
    def Identifier(self) -> str:
        ...

    @property
    def Routes(self) -> System.Array[AdventureBot.Room.MessageReceived]:
        ...
    @Routes.setter
    def Routes(self, val: System.Array[AdventureBot.Room.MessageReceived]):
        ...

    @property
    def Buttons(self) -> AdventureBot.NullableDictionary[AdventureBot.Room.MessageReceived, System.Collections.Generic.Dictionary[str, AdventureBot.Room.MessageReceived]]:
        ...
    @Buttons.setter
    def Buttons(self, val: AdventureBot.NullableDictionary[AdventureBot.Room.MessageReceived, System.Collections.Generic.Dictionary[str, AdventureBot.Room.MessageReceived]]):
        ...

    # methods
    def __init__(self, ):
        ...

    @staticmethod
    def IsFriday() -> bool:
        ...

    def GetDamage(self, user: AdventureBot.User.User, ) -> System.Decimal:
        ...

    def Enter(self, user: AdventureBot.User.User, buttons: System.Array[System.Array[str]], ) -> None:
        ...

    def OnRunaway(self, user: AdventureBot.User.User, ) -> bool:
        ...

    def OnWon(self, user: AdventureBot.User.User, ) -> None:
        ...

class Merchants(AdventureBot.Room.IRoom, AdventureBot.Room.RoomBase):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields
    Id: str = ...

    # properties
    @property
    def Name(self) -> str:
        ...

    @property
    def Identifier(self) -> str:
        ...

    @property
    def Routes(self) -> System.Array[AdventureBot.Room.MessageReceived]:
        ...
    @Routes.setter
    def Routes(self, val: System.Array[AdventureBot.Room.MessageReceived]):
        ...

    @property
    def Buttons(self) -> AdventureBot.NullableDictionary[AdventureBot.Room.MessageReceived, System.Collections.Generic.Dictionary[str, AdventureBot.Room.MessageReceived]]:
        ...
    @Buttons.setter
    def Buttons(self, val: AdventureBot.NullableDictionary[AdventureBot.Room.MessageReceived, System.Collections.Generic.Dictionary[str, AdventureBot.Room.MessageReceived]]):
        ...

    # methods
    def __init__(self, ):
        ...

    def OnEnter(self, user: AdventureBot.User.User, ) -> None:
        ...

    def OnMessage(self, user: AdventureBot.User.User, message: AdventureBot.Messenger.ReceivedMessage, ) -> None:
        ...

    def Nothing(self, user: AdventureBot.User.User, ) -> bool:
        ...

    def Pay(self, user: AdventureBot.User.User, message: AdventureBot.Messenger.ReceivedMessage, ) -> None:
        ...

    def Shop(self, user: AdventureBot.User.User, message: AdventureBot.Messenger.ReceivedMessage, ) -> None:
        ...

    def Shop2(self, user: AdventureBot.User.User, message: AdventureBot.Messenger.ReceivedMessage, ) -> None:
        ...

class MonsterTemplate(AdventureBot.Room.IRoom, AdventureBot.Room.IMonster, Content.Quests.IQuestMonster, AdventureBot.Room.MonsterBase):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields
    Id: str = ...

    # properties
    @property
    def Health(self) -> System.Decimal:
        ...

    @property
    def Name(self) -> str:
        ...

    @property
    def Identifier(self) -> str:
        ...

    @property
    def Routes(self) -> System.Array[AdventureBot.Room.MessageReceived]:
        ...
    @Routes.setter
    def Routes(self, val: System.Array[AdventureBot.Room.MessageReceived]):
        ...

    @property
    def Buttons(self) -> AdventureBot.NullableDictionary[AdventureBot.Room.MessageReceived, System.Collections.Generic.Dictionary[str, AdventureBot.Room.MessageReceived]]:
        ...
    @Buttons.setter
    def Buttons(self, val: AdventureBot.NullableDictionary[AdventureBot.Room.MessageReceived, System.Collections.Generic.Dictionary[str, AdventureBot.Room.MessageReceived]]):
        ...

    # methods
    def __init__(self, ):
        ...

    def GetDamage(self, user: AdventureBot.User.User, ) -> System.Decimal:
        ...

    def Enter(self, user: AdventureBot.User.User, buttons: System.Array[System.Array[str]], ) -> None:
        ...

    def OnRunaway(self, user: AdventureBot.User.User, ) -> bool:
        ...

    def OnWon(self, user: AdventureBot.User.User, ) -> None:
        ...

class Church(AdventureBot.Room.IRoom, AdventureBot.Room.BetterRoom.BetterRoomBase[Content.Rooms.Church]):
    @typing.overload
    def __init__(self, **kwargs):
        self._actions: System.Collections.Generic.Dictionary[System.Type, AdventureBot.Room.BetterRoom.ActionBase]
        self._rootAction: AdventureBot.Room.BetterRoom.ActionBase
        ...

    # static fields
    Id: str = ...

    # properties
    @property
    def Name(self) -> str:
        ...

    @property
    def Identifier(self) -> str:
        ...

    @property
    def actions(self) -> System.Array[System.Type]:
        ...

    @property
    def Routes(self) -> System.Array[AdventureBot.Room.MessageReceived]:
        ...
    @Routes.setter
    def Routes(self, val: System.Array[AdventureBot.Room.MessageReceived]):
        ...

    @property
    def Buttons(self) -> AdventureBot.NullableDictionary[AdventureBot.Room.MessageReceived, System.Collections.Generic.Dictionary[str, AdventureBot.Room.MessageReceived]]:
        ...
    @Buttons.setter
    def Buttons(self, val: AdventureBot.NullableDictionary[AdventureBot.Room.MessageReceived, System.Collections.Generic.Dictionary[str, AdventureBot.Room.MessageReceived]]):
        ...

    # methods
    def __init__(self, ):
        ...

    def OnEnter(self, user: AdventureBot.User.User, ) -> None:
        ...

class Gumba(AdventureBot.Room.IRoom, AdventureBot.Room.IMonster, Content.Quests.IQuestMonster, AdventureBot.Room.MonsterBase):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields
    Id: str = ...

    # properties
    @property
    def Health(self) -> System.Decimal:
        ...

    @property
    def Name(self) -> str:
        ...

    @property
    def Identifier(self) -> str:
        ...

    @property
    def Routes(self) -> System.Array[AdventureBot.Room.MessageReceived]:
        ...
    @Routes.setter
    def Routes(self, val: System.Array[AdventureBot.Room.MessageReceived]):
        ...

    @property
    def Buttons(self) -> AdventureBot.NullableDictionary[AdventureBot.Room.MessageReceived, System.Collections.Generic.Dictionary[str, AdventureBot.Room.MessageReceived]]:
        ...
    @Buttons.setter
    def Buttons(self, val: AdventureBot.NullableDictionary[AdventureBot.Room.MessageReceived, System.Collections.Generic.Dictionary[str, AdventureBot.Room.MessageReceived]]):
        ...

    # methods
    def __init__(self, ):
        ...

    def OnMessage(self, user: AdventureBot.User.User, message: AdventureBot.Messenger.ReceivedMessage, ) -> None:
        ...

    def GetDamage(self, user: AdventureBot.User.User, ) -> System.Decimal:
        ...

    def Enter(self, user: AdventureBot.User.User, buttons: System.Array[System.Array[str]], ) -> None:
        ...

    def GetActions(self, user: AdventureBot.User.User, ) -> System.Array[System.Array[str]]:
        ...

    def OnRunaway(self, user: AdventureBot.User.User, ) -> bool:
        ...

    def OnWon(self, user: AdventureBot.User.User, ) -> None:
        ...

class Legolas(AdventureBot.Room.IRoom, AdventureBot.Room.IMonster, Content.Quests.IQuestMonster, AdventureBot.Room.MonsterBase):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields
    Id: str = ...

    # properties
    @property
    def Health(self) -> System.Decimal:
        ...

    @property
    def Name(self) -> str:
        ...

    @property
    def Identifier(self) -> str:
        ...

    @property
    def Routes(self) -> System.Array[AdventureBot.Room.MessageReceived]:
        ...
    @Routes.setter
    def Routes(self, val: System.Array[AdventureBot.Room.MessageReceived]):
        ...

    @property
    def Buttons(self) -> AdventureBot.NullableDictionary[AdventureBot.Room.MessageReceived, System.Collections.Generic.Dictionary[str, AdventureBot.Room.MessageReceived]]:
        ...
    @Buttons.setter
    def Buttons(self, val: AdventureBot.NullableDictionary[AdventureBot.Room.MessageReceived, System.Collections.Generic.Dictionary[str, AdventureBot.Room.MessageReceived]]):
        ...

    # methods
    def __init__(self, ):
        ...

    def GetDamage(self, user: AdventureBot.User.User, ) -> System.Decimal:
        ...

    def Enter(self, user: AdventureBot.User.User, buttons: System.Array[System.Array[str]], ) -> None:
        ...

    def OnRunaway(self, user: AdventureBot.User.User, ) -> bool:
        ...

    def OnWon(self, user: AdventureBot.User.User, ) -> None:
        ...

class SpaceMarine(AdventureBot.Room.IRoom, AdventureBot.Room.IMonster, Content.Quests.IQuestMonster, AdventureBot.Room.MonsterBase):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields
    Id: str = ...

    # properties
    @property
    def Health(self) -> System.Decimal:
        ...

    @property
    def Name(self) -> str:
        ...

    @property
    def Identifier(self) -> str:
        ...

    @property
    def Routes(self) -> System.Array[AdventureBot.Room.MessageReceived]:
        ...
    @Routes.setter
    def Routes(self, val: System.Array[AdventureBot.Room.MessageReceived]):
        ...

    @property
    def Buttons(self) -> AdventureBot.NullableDictionary[AdventureBot.Room.MessageReceived, System.Collections.Generic.Dictionary[str, AdventureBot.Room.MessageReceived]]:
        ...
    @Buttons.setter
    def Buttons(self, val: AdventureBot.NullableDictionary[AdventureBot.Room.MessageReceived, System.Collections.Generic.Dictionary[str, AdventureBot.Room.MessageReceived]]):
        ...

    # methods
    def __init__(self, ):
        ...

    def GetDamage(self, user: AdventureBot.User.User, ) -> System.Decimal:
        ...

    def Enter(self, user: AdventureBot.User.User, buttons: System.Array[System.Array[str]], ) -> None:
        ...

    def OnRunaway(self, user: AdventureBot.User.User, ) -> bool:
        ...

    def OnWon(self, user: AdventureBot.User.User, ) -> None:
        ...

class Stormtrooper(AdventureBot.Room.IRoom, AdventureBot.Room.IMonster, Content.Quests.IQuestMonster, AdventureBot.Room.MonsterBase):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields
    Id: str = ...

    # properties
    @property
    def Health(self) -> System.Decimal:
        ...

    @property
    def Name(self) -> str:
        ...

    @property
    def Identifier(self) -> str:
        ...

    @property
    def Routes(self) -> System.Array[AdventureBot.Room.MessageReceived]:
        ...
    @Routes.setter
    def Routes(self, val: System.Array[AdventureBot.Room.MessageReceived]):
        ...

    @property
    def Buttons(self) -> AdventureBot.NullableDictionary[AdventureBot.Room.MessageReceived, System.Collections.Generic.Dictionary[str, AdventureBot.Room.MessageReceived]]:
        ...
    @Buttons.setter
    def Buttons(self, val: AdventureBot.NullableDictionary[AdventureBot.Room.MessageReceived, System.Collections.Generic.Dictionary[str, AdventureBot.Room.MessageReceived]]):
        ...

    # methods
    def __init__(self, ):
        ...

    def GetDamage(self, user: AdventureBot.User.User, ) -> System.Decimal:
        ...

    def Enter(self, user: AdventureBot.User.User, buttons: System.Array[System.Array[str]], ) -> None:
        ...

    def OnRunaway(self, user: AdventureBot.User.User, ) -> bool:
        ...

    def OnWon(self, user: AdventureBot.User.User, ) -> None:
        ...

class Skitties(AdventureBot.Room.IRoom, AdventureBot.Room.RoomBase):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields
    Id: str = ...

    # properties
    @property
    def Name(self) -> str:
        ...

    @property
    def Identifier(self) -> str:
        ...

    @property
    def Routes(self) -> System.Array[AdventureBot.Room.MessageReceived]:
        ...
    @Routes.setter
    def Routes(self, val: System.Array[AdventureBot.Room.MessageReceived]):
        ...

    @property
    def Buttons(self) -> AdventureBot.NullableDictionary[AdventureBot.Room.MessageReceived, System.Collections.Generic.Dictionary[str, AdventureBot.Room.MessageReceived]]:
        ...
    @Buttons.setter
    def Buttons(self, val: AdventureBot.NullableDictionary[AdventureBot.Room.MessageReceived, System.Collections.Generic.Dictionary[str, AdventureBot.Room.MessageReceived]]):
        ...

    # methods
    def __init__(self, ):
        ...

    def OnEnter(self, user: AdventureBot.User.User, ) -> None:
        ...

    def OnMessage(self, user: AdventureBot.User.User, message: AdventureBot.Messenger.ReceivedMessage, ) -> None:
        ...

class BetterTest(AdventureBot.Room.IRoom, AdventureBot.Room.BetterRoom.BetterRoomBase[Content.Rooms.BetterTest]):
    @typing.overload
    def __init__(self, **kwargs):
        self._actions: System.Collections.Generic.Dictionary[System.Type, AdventureBot.Room.BetterRoom.ActionBase]
        self._rootAction: AdventureBot.Room.BetterRoom.ActionBase
        ...

    # static fields
    Id: str = ...

    # properties
    @property
    def Name(self) -> str:
        ...

    @property
    def Identifier(self) -> str:
        ...

    @property
    def actions(self) -> System.Array[System.Type]:
        ...

    @property
    def Routes(self) -> System.Array[AdventureBot.Room.MessageReceived]:
        ...
    @Routes.setter
    def Routes(self, val: System.Array[AdventureBot.Room.MessageReceived]):
        ...

    @property
    def Buttons(self) -> AdventureBot.NullableDictionary[AdventureBot.Room.MessageReceived, System.Collections.Generic.Dictionary[str, AdventureBot.Room.MessageReceived]]:
        ...
    @Buttons.setter
    def Buttons(self, val: AdventureBot.NullableDictionary[AdventureBot.Room.MessageReceived, System.Collections.Generic.Dictionary[str, AdventureBot.Room.MessageReceived]]):
        ...

    # methods
    def __init__(self, ):
        ...

    def OnEnter(self, user: AdventureBot.User.User, ) -> None:
        ...

class Beorn(AdventureBot.Room.IRoom, AdventureBot.Room.IMonster, Content.Quests.IQuestMonster, AdventureBot.Room.MonsterBase):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields
    Id: str = ...

    # properties
    @property
    def Health(self) -> System.Decimal:
        ...

    @property
    def Name(self) -> str:
        ...

    @property
    def Identifier(self) -> str:
        ...

    @property
    def Routes(self) -> System.Array[AdventureBot.Room.MessageReceived]:
        ...
    @Routes.setter
    def Routes(self, val: System.Array[AdventureBot.Room.MessageReceived]):
        ...

    @property
    def Buttons(self) -> AdventureBot.NullableDictionary[AdventureBot.Room.MessageReceived, System.Collections.Generic.Dictionary[str, AdventureBot.Room.MessageReceived]]:
        ...
    @Buttons.setter
    def Buttons(self, val: AdventureBot.NullableDictionary[AdventureBot.Room.MessageReceived, System.Collections.Generic.Dictionary[str, AdventureBot.Room.MessageReceived]]):
        ...

    # methods
    def __init__(self, ):
        ...

    def GetDamage(self, user: AdventureBot.User.User, ) -> System.Decimal:
        ...

    def Enter(self, user: AdventureBot.User.User, buttons: System.Array[System.Array[str]], ) -> None:
        ...

    def OnRunaway(self, user: AdventureBot.User.User, ) -> bool:
        ...

    def OnWon(self, user: AdventureBot.User.User, ) -> None:
        ...

class HiMen(AdventureBot.Room.IRoom, AdventureBot.Room.IMonster, Content.Quests.IQuestMonster, AdventureBot.Room.MonsterBase):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields
    Id: str = ...

    # properties
    @property
    def Health(self) -> System.Decimal:
        ...

    @property
    def Name(self) -> str:
        ...

    @property
    def Identifier(self) -> str:
        ...

    @property
    def Routes(self) -> System.Array[AdventureBot.Room.MessageReceived]:
        ...
    @Routes.setter
    def Routes(self, val: System.Array[AdventureBot.Room.MessageReceived]):
        ...

    @property
    def Buttons(self) -> AdventureBot.NullableDictionary[AdventureBot.Room.MessageReceived, System.Collections.Generic.Dictionary[str, AdventureBot.Room.MessageReceived]]:
        ...
    @Buttons.setter
    def Buttons(self, val: AdventureBot.NullableDictionary[AdventureBot.Room.MessageReceived, System.Collections.Generic.Dictionary[str, AdventureBot.Room.MessageReceived]]):
        ...

    # methods
    def __init__(self, ):
        ...

    def GetDamage(self, user: AdventureBot.User.User, ) -> System.Decimal:
        ...

    def Enter(self, user: AdventureBot.User.User, buttons: System.Array[System.Array[str]], ) -> None:
        ...

    def OnRunaway(self, user: AdventureBot.User.User, ) -> bool:
        ...

    def OnWon(self, user: AdventureBot.User.User, ) -> None:
        ...

class Halls(AdventureBot.Room.IRoom, AdventureBot.Room.BetterRoom.BetterRoomBase[Content.Rooms.Halls]):
    @typing.overload
    def __init__(self, **kwargs):
        self._actions: System.Collections.Generic.Dictionary[System.Type, AdventureBot.Room.BetterRoom.ActionBase]
        self._rootAction: AdventureBot.Room.BetterRoom.ActionBase
        ...

    # static fields
    Id: str = ...

    # properties
    @property
    def Name(self) -> str:
        ...

    @property
    def Identifier(self) -> str:
        ...

    @property
    def actions(self) -> System.Array[System.Type]:
        ...

    @property
    def Routes(self) -> System.Array[AdventureBot.Room.MessageReceived]:
        ...
    @Routes.setter
    def Routes(self, val: System.Array[AdventureBot.Room.MessageReceived]):
        ...

    @property
    def Buttons(self) -> AdventureBot.NullableDictionary[AdventureBot.Room.MessageReceived, System.Collections.Generic.Dictionary[str, AdventureBot.Room.MessageReceived]]:
        ...
    @Buttons.setter
    def Buttons(self, val: AdventureBot.NullableDictionary[AdventureBot.Room.MessageReceived, System.Collections.Generic.Dictionary[str, AdventureBot.Room.MessageReceived]]):
        ...

    # methods
    def __init__(self, ):
        ...

    def OnEnter(self, user: AdventureBot.User.User, ) -> None:
        ...

class Worms(AdventureBot.Room.IRoom, AdventureBot.Room.RoomBase):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields
    Id: str = ...

    # properties
    @property
    def Name(self) -> str:
        ...

    @property
    def Identifier(self) -> str:
        ...

    @property
    def Routes(self) -> System.Array[AdventureBot.Room.MessageReceived]:
        ...
    @Routes.setter
    def Routes(self, val: System.Array[AdventureBot.Room.MessageReceived]):
        ...

    @property
    def Buttons(self) -> AdventureBot.NullableDictionary[AdventureBot.Room.MessageReceived, System.Collections.Generic.Dictionary[str, AdventureBot.Room.MessageReceived]]:
        ...
    @Buttons.setter
    def Buttons(self, val: AdventureBot.NullableDictionary[AdventureBot.Room.MessageReceived, System.Collections.Generic.Dictionary[str, AdventureBot.Room.MessageReceived]]):
        ...

    # methods
    def __init__(self, ):
        ...

    def OnEnter(self, user: AdventureBot.User.User, ) -> None:
        ...

    def OnLeave(self, user: AdventureBot.User.User, ) -> bool:
        ...

    def OnMessage(self, user: AdventureBot.User.User, message: AdventureBot.Messenger.ReceivedMessage, ) -> None:
        ...

class Tiger(AdventureBot.Room.IRoom, AdventureBot.Room.IMonster, Content.Quests.IQuestMonster, AdventureBot.Room.MonsterBase):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields
    Id: str = ...

    # properties
    @property
    def Health(self) -> System.Decimal:
        ...

    @property
    def Name(self) -> str:
        ...

    @property
    def Identifier(self) -> str:
        ...

    @property
    def Routes(self) -> System.Array[AdventureBot.Room.MessageReceived]:
        ...
    @Routes.setter
    def Routes(self, val: System.Array[AdventureBot.Room.MessageReceived]):
        ...

    @property
    def Buttons(self) -> AdventureBot.NullableDictionary[AdventureBot.Room.MessageReceived, System.Collections.Generic.Dictionary[str, AdventureBot.Room.MessageReceived]]:
        ...
    @Buttons.setter
    def Buttons(self, val: AdventureBot.NullableDictionary[AdventureBot.Room.MessageReceived, System.Collections.Generic.Dictionary[str, AdventureBot.Room.MessageReceived]]):
        ...

    # methods
    def __init__(self, ):
        ...

    def GetDamage(self, user: AdventureBot.User.User, ) -> System.Decimal:
        ...

    def Enter(self, user: AdventureBot.User.User, buttons: System.Array[System.Array[str]], ) -> None:
        ...

    def OnRunaway(self, user: AdventureBot.User.User, ) -> bool:
        ...

    def OnWon(self, user: AdventureBot.User.User, ) -> None:
        ...

