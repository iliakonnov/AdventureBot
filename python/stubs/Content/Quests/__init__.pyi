from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import AdventureBot.Quest
import Content.Quests
import AdventureBot.Room
import AdventureBot.User
import System


class KillMonster(AdventureBot.Quest.IQuest, Content.Quests.KillMonsterBase):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields
    Id: str = ...

    # properties
    @property
    def Identifer(self) -> str:
        ...

    # methods
    def __init__(self, ):
        ...

class IQuestMonster(AdventureBot.Room.IMonster, AdventureBot.Room.IRoom, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
class KillMonsterBase(AdventureBot.Quest.IQuest, AdventureBot.Quest.QuestBase, abc.ABC):
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

    def GetName(self, user: AdventureBot.User.User, questId: System.Guid, ) -> str:
        ...

    def GetProgress(self, user: AdventureBot.User.User, questId: System.Guid, ) -> System.Decimal:
        ...

    def Finish(self, user: AdventureBot.User.User, questId: System.Guid, ) -> None:
        ...

    def Begin(self, user: AdventureBot.User.User, questId: System.Guid, ) -> None:
        ...

    def GetMonsterId(self, user: AdventureBot.User.User, guid: System.Guid, ) -> str:
        ...

    def GetReward(self, user: AdventureBot.User.User, guid: System.Guid, ) -> System.Decimal:
        ...

    def IsFinished(self, user: AdventureBot.User.User, guid: System.Guid, ) -> bool:
        ...

class KillMonsterFree(AdventureBot.Quest.IQuest, Content.Quests.KillMonsterBase):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields
    Id: str = ...

    # properties
    @property
    def Identifer(self) -> str:
        ...

    # methods
    def __init__(self, ):
        ...

    def GetReward(self, user: AdventureBot.User.User, guid: System.Guid, ) -> System.Decimal:
        ...

    def Finish(self, user: AdventureBot.User.User, questId: System.Guid, ) -> None:
        ...

