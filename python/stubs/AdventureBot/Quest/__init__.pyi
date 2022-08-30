from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import System
import AdventureBot.User
import AdventureBot.Quest
import AdventureBot.ObjectManager


class IQuest(abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @abc.abstractmethod
    @property
    def Identifer(self) -> System.String:
        ...

    # methods
    @typing.overload
    @abc.abstractmethod
    def GetName(self, user: AdventureBot.User.User, questId: System.Guid, ) -> System.String:
        ...

    @typing.overload
    @abc.abstractmethod
    def GetProgress(self, user: AdventureBot.User.User, questId: System.Guid, ) -> System.Decimal:
        ...

    @typing.overload
    @abc.abstractmethod
    def Finish(self, user: AdventureBot.User.User, questId: System.Guid, ) -> None:
        ...

    @typing.overload
    @abc.abstractmethod
    def Begin(self, user: AdventureBot.User.User, questId: System.Guid, ) -> None:
        ...

class QuestBase(AdventureBot.Quest.IQuest, System.Object, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @abc.abstractmethod
    @property
    def Identifer(self) -> System.String:
        ...

    # methods
    @typing.overload
    @abc.abstractmethod
    def GetName(self, user: AdventureBot.User.User, questId: System.Guid, ) -> System.String:
        ...

    @typing.overload
    @abc.abstractmethod
    def GetProgress(self, user: AdventureBot.User.User, questId: System.Guid, ) -> System.Decimal:
        ...

    @typing.overload
    @abc.abstractmethod
    def Finish(self, user: AdventureBot.User.User, questId: System.Guid, ) -> None:
        ...

    @typing.overload
    @abc.abstractmethod
    def Begin(self, user: AdventureBot.User.User, questId: System.Guid, ) -> None:
        ...

class QuestInfo(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def Identifier(self) -> System.String:
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
    def __init__(self, identifier: System.String, questId: System.Guid, ):
        ...

class QuestAttribute(AdventureBot.ObjectManager.IdentifiableAttribute):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def Identifier(self) -> System.String:
        ...

    @property
    def TypeId(self) -> System.Object:
        ...

    # methods
    @typing.overload
    def __init__(self, identifier: System.String, ):
        ...

class QuestManager(AdventureBot.ObjectManager.IManager[AdventureBot.Quest.IQuest], AdventureBot.ObjectManager.StorageManager[AdventureBot.Quest.IQuest, AdventureBot.Quest.QuestAttribute]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    # methods
    @typing.overload
    def __init__(self, ):
        ...

