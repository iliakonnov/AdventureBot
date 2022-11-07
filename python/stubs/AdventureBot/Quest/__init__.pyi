from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import System
import AdventureBot.Quest
import AdventureBot.ObjectManager
import AdventureBot.User
import AdventureBot
import System.Collections.Immutable


class QuestInfo(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def Identifier(self) -> str:
        ...

    @property
    def QuestId(self) -> System.Guid:
        ...

    @property
    def Quest(self) -> AdventureBot.Quest.IQuest:
        ...

    # methods
    @typing.overload
    def __init__(self, quest: AdventureBot.Quest.IQuest, ):
        ...

    @typing.overload
    def __init__(self, identifier: str, questId: System.Guid, ):
        ...

class QuestManager(AdventureBot.ObjectManager.IManager[AdventureBot.Quest.IQuest], AdventureBot.ObjectManager.StorageManager[AdventureBot.Quest.IQuest, AdventureBot.Quest.QuestAttribute]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    def __init__(self, ):
        ...

class QuestBase(AdventureBot.Quest.IQuest, System.Object, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    @abc.abstractmethod
    def Identifer(self) -> str:
        ...

    # methods
    def __init__(self, ):
        ...

    @abc.abstractmethod
    def GetName(self, user: AdventureBot.User.User, questId: System.Guid, ) -> str:
        ...

    @abc.abstractmethod
    def GetProgress(self, user: AdventureBot.User.User, questId: System.Guid, ) -> System.Decimal:
        ...

    @abc.abstractmethod
    def Finish(self, user: AdventureBot.User.User, questId: System.Guid, ) -> None:
        ...

    @abc.abstractmethod
    def Begin(self, user: AdventureBot.User.User, questId: System.Guid, ) -> None:
        ...

    def GetQuestVariables(self, user: AdventureBot.User.User, questId: System.Guid, ) -> AdventureBot.VariableContainer:
        ...

    def GetQuestInstances(self, user: AdventureBot.User.User, ) -> System.Collections.Immutable.ImmutableDictionary[System.Guid, AdventureBot.Quest.QuestInfo]:
        ...

class IQuest(abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    @abc.abstractmethod
    def Identifer(self) -> str:
        ...

    # methods
    @abc.abstractmethod
    def GetName(self, user: AdventureBot.User.User, questId: System.Guid, ) -> str:
        ...

    @abc.abstractmethod
    def GetProgress(self, user: AdventureBot.User.User, questId: System.Guid, ) -> System.Decimal:
        ...

    @abc.abstractmethod
    def Finish(self, user: AdventureBot.User.User, questId: System.Guid, ) -> None:
        ...

    @abc.abstractmethod
    def Begin(self, user: AdventureBot.User.User, questId: System.Guid, ) -> None:
        ...

class QuestAttribute(AdventureBot.ObjectManager.IdentifiableAttribute):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def Identifier(self) -> str:
        ...

    @property
    def TypeId(self) -> System.Object:
        ...

    # methods
    def __init__(self, identifier: str, ):
        ...

