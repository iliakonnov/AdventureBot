from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import AdventureBot.Room
import Content.Quests
import AdventureBot
import System.Collections.Generic
import AdventureBot.User
import AdventureBot.Messenger
import System


class MegaMonsterRoom(AdventureBot.Room.IRoom, Content.Quests.IQuestMonster, AdventureBot.Room.IMonster, AdventureBot.Room.RoomBase):
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

    def BeginTalk(self, user: AdventureBot.User.User, ) -> None:
        ...

    def Talk(self, user: AdventureBot.User.User, message: AdventureBot.Messenger.ReceivedMessage, ) -> None:
        ...

    def Artifact(self, user: AdventureBot.User.User, ) -> None:
        ...

    def GiveArtifact(self, user: AdventureBot.User.User, message: AdventureBot.Messenger.ReceivedMessage, ) -> None:
        ...

    def ArtifactNotFound(self, user: AdventureBot.User.User, message: AdventureBot.Messenger.ReceivedMessage, ) -> None:
        ...

    def ConfirmGiveArtifact(self, user: AdventureBot.User.User, ) -> None:
        ...

    def MakeDamage(self, user: AdventureBot.User.User, damage: System.Decimal, ) -> None:
        ...

    def GetCurrentHealth(self, user: AdventureBot.User.User, ) -> System.Decimal:
        ...

    def BeginBattle(self, user: AdventureBot.User.User, ) -> None:
        ...

    def BattleTarget(self, user: AdventureBot.User.User, place: int, ) -> None:
        ...

    def SelectTarget(self, user: AdventureBot.User.User, message: AdventureBot.Messenger.ReceivedMessage, ) -> None:
        ...

    def Battle(self, user: AdventureBot.User.User, messageReceived: AdventureBot.Messenger.ReceivedMessage, ) -> None:
        ...

    def Gold(self, user: AdventureBot.User.User, ) -> None:
        ...

    def GiveGold(self, user: AdventureBot.User.User, message: AdventureBot.Messenger.ReceivedMessage, ) -> None:
        ...

    def NotEnoughGold(self, user: AdventureBot.User.User, message: AdventureBot.Messenger.ReceivedMessage, ) -> None:
        ...

    def ConfirmGiveGold(self, user: AdventureBot.User.User, ) -> None:
        ...

    def Knowledge(self, user: AdventureBot.User.User, ) -> None:
        ...

    def GiveKnowledge(self, user: AdventureBot.User.User, message: AdventureBot.Messenger.ReceivedMessage, ) -> None:
        ...

    def NotEnoughKnowledge(self, user: AdventureBot.User.User, message: AdventureBot.Messenger.ReceivedMessage, ) -> None:
        ...

    def ConfirmGiveKnowledge(self, user: AdventureBot.User.User, ) -> None:
        ...

