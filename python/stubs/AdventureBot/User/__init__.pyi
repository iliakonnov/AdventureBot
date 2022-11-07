from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import System
import AdventureBot
import System.Collections.Generic
import AdventureBot.User
import System.Linq.Expressions
import AdventureBot.User.Stats
import AdventureBot.Item
import AdventureBot.User.RoomManager
import AdventureBot.Room
import System.Runtime.Serialization
import System.Reflection
import AdventureBot.Messenger
import System.Collections.Immutable
import AdventureBot.Quest

T = typing.TypeVar('T')

class VariableManager(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        self.PersistentVariables: AdventureBot.VariableContainer
        self.UserVariables: AdventureBot.VariableContainer
        ...

    # static fields

    # properties
    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def __init__(self, roomVariables: System.Collections.Generic.Dictionary[str, AdventureBot.VariableContainer], itemVariables: System.Collections.Generic.Dictionary[str, AdventureBot.VariableContainer], questVariables: System.Collections.Generic.Dictionary[str, System.Collections.Generic.Dictionary[System.Guid, AdventureBot.VariableContainer]], persistentVariables: AdventureBot.VariableContainer, userVariables: AdventureBot.VariableContainer, ):
        ...

    def Reset(self, ) -> None:
        ...

    def GetRoomVariables(self, identifier: str, ) -> AdventureBot.VariableContainer:
        ...

    def GetItemVariables(self, identifier: str, ) -> AdventureBot.VariableContainer:
        ...

    def GetQuestVariables(self, identifier: str, questId: System.Guid, ) -> AdventureBot.VariableContainer:
        ...

class DatabaseVariables(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def Level(self) -> int:
        ...
    @Level.setter
    def Level(self, val: int):
        ...

    @property
    def Experience(self) -> System.Decimal:
        ...
    @Experience.setter
    def Experience(self, val: System.Decimal):
        ...

    @property
    def Gold(self) -> System.Decimal:
        ...
    @Gold.setter
    def Gold(self, val: System.Decimal):
        ...

    @property
    def Monsters(self) -> int:
        ...
    @Monsters.setter
    def Monsters(self, val: int):
        ...

    @property
    def Rooms(self) -> int:
        ...
    @Rooms.setter
    def Rooms(self, val: int):
        ...

    @property
    def LastMessageReceived(self) -> System.DateTime:
        ...
    @LastMessageReceived.setter
    def LastMessageReceived(self, val: System.DateTime):
        ...

    # methods
    def __init__(self, ):
        ...

    def Fill(self, variables: AdventureBot.User.DatabaseVariables, ) -> None:
        ...

    @staticmethod
    def GetColumns() -> System.Array[System.ValueTuple[AdventureBot.User.DbColumnAttribute, System.Func[AdventureBot.User.DatabaseVariables, System.Object]]]:
        ...

    @staticmethod
    @typing.overload
    def GetColumn(expression: System.Linq.Expressions.Expression, ) -> AdventureBot.User.DbColumnAttribute:
        ...

    @staticmethod
    @typing.overload
    def GetColumn(getter: System.Linq.Expressions.Expression[System.Func[AdventureBot.User.DatabaseVariables, System.Object]], ) -> AdventureBot.User.DbColumnAttribute:
        ...

class User(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        self.Random: System.Random
        ...

    # static fields

    # properties
    @property
    def Info(self) -> AdventureBot.User.UserInfo:
        ...
    @Info.setter
    def Info(self, val: AdventureBot.User.UserInfo):
        ...

    @property
    def ActiveItemsManager(self) -> AdventureBot.User.ActiveItemsManager:
        ...
    @ActiveItemsManager.setter
    def ActiveItemsManager(self, val: AdventureBot.User.ActiveItemsManager):
        ...

    @property
    def ItemManager(self) -> AdventureBot.User.ItemManager:
        ...
    @ItemManager.setter
    def ItemManager(self, val: AdventureBot.User.ItemManager):
        ...

    @property
    def VariableManager(self) -> AdventureBot.User.VariableManager:
        ...
    @VariableManager.setter
    def VariableManager(self, val: AdventureBot.User.VariableManager):
        ...

    @property
    def RoomManager(self) -> AdventureBot.User.RoomManager:
        ...
    @RoomManager.setter
    def RoomManager(self, val: AdventureBot.User.RoomManager):
        ...

    @property
    def MessageManager(self) -> AdventureBot.User.MessageManager:
        ...
    @MessageManager.setter
    def MessageManager(self, val: AdventureBot.User.MessageManager):
        ...

    @property
    def QuestManager(self) -> AdventureBot.User.QuestManager:
        ...
    @QuestManager.setter
    def QuestManager(self, val: AdventureBot.User.QuestManager):
        ...

    @property
    def DatabaseVariables(self) -> AdventureBot.User.DatabaseVariables:
        ...
    @DatabaseVariables.setter
    def DatabaseVariables(self, val: AdventureBot.User.DatabaseVariables):
        ...

    @property
    def Token(self) -> System.Guid:
        ...
    @Token.setter
    def Token(self, val: System.Guid):
        ...

    @property
    def LinkedTo(self) -> System.Tuple[AdventureBot.UserId, System.Guid]:
        ...
    @LinkedTo.setter
    def LinkedTo(self, val: System.Tuple[AdventureBot.UserId, System.Guid]):
        ...

    # methods
    @typing.overload
    def __init__(self, itemManager: AdventureBot.User.ItemManager, activeItemsManager: AdventureBot.User.ActiveItemsManager, info: AdventureBot.User.UserInfo, variableManager: AdventureBot.User.VariableManager, roomManager: AdventureBot.User.RoomManager, messageManager: AdventureBot.User.MessageManager, questManager: AdventureBot.User.QuestManager, token: System.Guid, linkedTo: System.Tuple[AdventureBot.UserId, System.Guid], ):
        ...

    @typing.overload
    def __init__(self, userId: AdventureBot.UserId, ):
        ...

    @typing.overload
    def Reset(self, userId: AdventureBot.UserId, ) -> None:
        ...

    @typing.overload
    def Reset(self, ) -> None:
        ...

class PublicUser(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def Info(self) -> AdventureBot.User.UserInfo:
        ...
    @Info.setter
    def Info(self, val: AdventureBot.User.UserInfo):
        ...

    @property
    def ActiveItemsManager(self) -> AdventureBot.User.ActiveItemsManager:
        ...
    @ActiveItemsManager.setter
    def ActiveItemsManager(self, val: AdventureBot.User.ActiveItemsManager):
        ...

    @property
    def ItemManager(self) -> AdventureBot.User.ItemManager:
        ...
    @ItemManager.setter
    def ItemManager(self, val: AdventureBot.User.ItemManager):
        ...

    @property
    def RoomManager(self) -> AdventureBot.User.RoomManager:
        ...
    @RoomManager.setter
    def RoomManager(self, val: AdventureBot.User.RoomManager):
        ...

    @property
    def MessageManager(self) -> AdventureBot.User.MessageManager:
        ...
    @MessageManager.setter
    def MessageManager(self, val: AdventureBot.User.MessageManager):
        ...

    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def __init__(self, user: AdventureBot.User.User, ):
        ...

class UserInfo(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def User(self) -> AdventureBot.User.User:
        ...
    @User.setter
    def User(self, val: AdventureBot.User.User):
        ...

    @property
    def Dead(self) -> bool:
        ...
    @Dead.setter
    def Dead(self, val: bool):
        ...

    @property
    def Gold(self) -> System.Decimal:
        ...
    @Gold.setter
    def Gold(self, val: System.Decimal):
        ...

    @property
    def SellMultiplier(self) -> System.Decimal:
        ...

    @property
    def UserId(self) -> AdventureBot.UserId:
        ...

    @property
    def Name(self) -> str:
        ...
    @Name.setter
    def Name(self, val: str):
        ...

    @property
    def Statistics(self) -> AdventureBot.User.Stats.Statistics:
        ...

    @property
    def Level(self) -> AdventureBot.User.Stats.UserLevel:
        ...

    @property
    def BaseStats(self) -> AdventureBot.User.Stats.Stats:
        ...
    @BaseStats.setter
    def BaseStats(self, val: AdventureBot.User.Stats.Stats):
        ...

    @property
    def CurrentStats(self) -> AdventureBot.User.Stats.Stats:
        ...
    @CurrentStats.setter
    def CurrentStats(self, val: AdventureBot.User.Stats.Stats):
        ...

    @property
    def MaxStats(self) -> AdventureBot.User.Stats.Stats:
        ...
    @MaxStats.setter
    def MaxStats(self, val: AdventureBot.User.Stats.Stats):
        ...

    @property
    def MinStats(self) -> AdventureBot.User.Stats.Stats:
        ...
    @MinStats.setter
    def MinStats(self, val: AdventureBot.User.Stats.Stats):
        ...

    # methods
    @typing.overload
    def __init__(self, dead: bool, userId: AdventureBot.UserId, baseStats: AdventureBot.User.Stats.Stats, currentStats: AdventureBot.User.Stats.Stats, _name: str, statistics: AdventureBot.User.Stats.Statistics, level: AdventureBot.User.Stats.UserLevel, ):
        ...

    @typing.overload
    def __init__(self, userId: AdventureBot.UserId, user: AdventureBot.User.User, ):
        ...

    def RecalculateStats(self, ) -> None:
        ...

    @staticmethod
    def ApplyItems(stats: AdventureBot.User.Stats.StatsEffect, activeItems: System.Collections.Generic.IEnumerable[AdventureBot.Item.ItemInfo], ) -> AdventureBot.User.Stats.Stats:
        ...

    def TryDecreaseGold(self, value: System.Decimal, ) -> bool:
        ...

    @typing.overload
    def ChangeStats(self, changeType: int, property: int, value: System.Decimal, allowLess: bool = ..., ) -> bool:
        ...

    @typing.overload
    def ChangeStats(self, property: int, value: System.Decimal, set: bool = ..., ) -> bool:
        ...

    def Kill(self, ) -> None:
        ...

    @staticmethod
    def CalculateDefence(damage: System.Decimal, defence: System.Decimal, ) -> System.Decimal:
        ...

    def MakeDamage(self, value: System.Decimal, defence: bool = ..., kill: bool = ..., ) -> None:
        ...

    def KarmaEffect(self, value: System.Decimal, ) -> System.Decimal:
        ...

class RoomManager(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        self.User: AdventureBot.User.User
        ...

    # static fields

    # properties
    @property
    def CurrentRoom(self) -> AdventureBot.User.RoomManager.StackedRoom:
        ...
    @CurrentRoom.setter
    def CurrentRoom(self, val: AdventureBot.User.RoomManager.StackedRoom):
        ...

    @property
    def Rooms(self) -> System.Collections.Generic.Stack[AdventureBot.User.RoomManager.StackedRoom]:
        ...

    @property
    def CurrentRootRoom(self) -> str:
        ...

    # methods
    @typing.overload
    def __init__(self, currentRoom: AdventureBot.User.RoomManager.StackedRoom, rooms: System.Collections.Generic.Stack[AdventureBot.User.RoomManager.StackedRoom], ):
        ...

    @typing.overload
    def __init__(self, user: AdventureBot.User.User, ):
        ...

    def Go(self, roomIdentifier: str, leave: bool = ..., ) -> None:
        ...

    def Leave(self, doReturn: bool = ..., checkLeave: bool = ..., ) -> None:
        ...

    def ChangeRoot(self, rootIdentifier: str, ) -> None:
        ...

    def GetRoom(self, ) -> AdventureBot.Room.IRoom:
        ...

class GameEventHandler(System.ICloneable, System.Runtime.Serialization.ISerializable, System.MulticastDelegate, typing.Generic[T]):
    @typing.overload
    def __init__(self, **kwargs):
        self._target: System.Object
        self._methodBase: System.Object
        self._methodPtr: System.IntPtr
        self._methodPtrAux: System.IntPtr
        ...

    # static fields

    # properties
    @property
    def Target(self) -> System.Object:
        ...

    @property
    def Method(self) -> System.Reflection.MethodInfo:
        ...

    # methods
    def __init__(self, object: System.Object, method: System.IntPtr, ):
        ...

    def Invoke(self, user: AdventureBot.User.User, param: T, ) -> None:
        ...

    def BeginInvoke(self, user: AdventureBot.User.User, param: T, callback: System.AsyncCallback, object: System.Object, ) -> System.IAsyncResult:
        ...

    def EndInvoke(self, result: System.IAsyncResult, ) -> None:
        ...

class MessageManager(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        self.ShownStats: int
        self.User: AdventureBot.User.User
        ...

    # static fields

    # properties
    @property
    def LastMessages(self) -> System.Collections.Generic.IReadOnlyCollection[AdventureBot.Messenger.SentMessage]:
        ...

    @property
    def LastMessage(self) -> AdventureBot.Messenger.SentMessage:
        ...

    @property
    def Queue(self) -> System.Collections.Generic.List[AdventureBot.Messenger.SentMessage]:
        ...

    @property
    def Buttons(self) -> System.Array[System.Array[str]]:
        ...
    @Buttons.setter
    def Buttons(self, val: System.Array[System.Array[str]]):
        ...

    @property
    def PreferToUpdate(self) -> bool:
        ...
    @PreferToUpdate.setter
    def PreferToUpdate(self, val: bool):
        ...

    @property
    def ReceivedMessage(self) -> AdventureBot.Messenger.ReceivedMessage:
        ...
    @ReceivedMessage.setter
    def ReceivedMessage(self, val: AdventureBot.Messenger.ReceivedMessage):
        ...

    @property
    def LastMessageReceived(self) -> System.DateTime:
        ...

    @property
    def ChatId(self) -> AdventureBot.ChatId:
        ...
    @ChatId.setter
    def ChatId(self, val: AdventureBot.ChatId):
        ...

    # methods
    @typing.overload
    def __init__(self, user: AdventureBot.User.User, ):
        ...

    @typing.overload
    def __init__(self, queue: System.Collections.Generic.List[AdventureBot.Messenger.SentMessage], buttons: System.Array[System.Array[str]], preferToUpdate: bool, lastMessages: System.Collections.Generic.Queue[AdventureBot.Messenger.SentMessage], chatId: AdventureBot.ChatId, recievedMessage: AdventureBot.Messenger.ReceivedMessage, shownStats: int, intent: str, ):
        ...

    def SendMessage(self, message: AdventureBot.Messenger.SentMessage, ) -> None:
        ...

    def SendImmediately(self, message: AdventureBot.Messenger.SentMessage, ) -> None:
        ...

    def OnReceived(self, message: AdventureBot.Messenger.ReceivedMessage, ) -> None:
        ...

    def AddInfo(self, messages: System.Collections.Generic.IEnumerable[str], ) -> str:
        ...

    def Finish(self, ) -> None:
        ...

    @staticmethod
    def Escape(message: str, ) -> str:
        ...

class GameEventHandler(System.ICloneable, System.Runtime.Serialization.ISerializable, System.MulticastDelegate):
    @typing.overload
    def __init__(self, **kwargs):
        self._target: System.Object
        self._methodBase: System.Object
        self._methodPtr: System.IntPtr
        self._methodPtrAux: System.IntPtr
        ...

    # static fields

    # properties
    @property
    def Target(self) -> System.Object:
        ...

    @property
    def Method(self) -> System.Reflection.MethodInfo:
        ...

    # methods
    def __init__(self, object: System.Object, method: System.IntPtr, ):
        ...

    def Invoke(self, user: AdventureBot.User.User, ) -> None:
        ...

    def BeginInvoke(self, user: AdventureBot.User.User, callback: System.AsyncCallback, object: System.Object, ) -> System.IAsyncResult:
        ...

    def EndInvoke(self, result: System.IAsyncResult, ) -> None:
        ...

class ActiveItemsManager(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        self.User: AdventureBot.User.User
        ...

    # static fields

    # properties
    @property
    def ActiveItems(self) -> System.Collections.Generic.IReadOnlyList[AdventureBot.Item.ItemInfo]:
        ...

    @property
    def ActiveProportions(self) -> System.Collections.Generic.IReadOnlyDictionary[AdventureBot.StructFlag[int], int]:
        ...

    @property
    def Proportions(self) -> System.Collections.Generic.Dictionary[AdventureBot.StructFlag[int], int]:
        ...
    @Proportions.setter
    def Proportions(self, val: System.Collections.Generic.Dictionary[AdventureBot.StructFlag[int], int]):
        ...

    @property
    def ActiveLimit(self) -> int:
        ...
    @ActiveLimit.setter
    def ActiveLimit(self, val: int):
        ...

    # methods
    @typing.overload
    def __init__(self, activeItems: System.Collections.Generic.List[AdventureBot.Item.ItemInfo], activeProportions: System.Collections.Generic.Dictionary[AdventureBot.StructFlag[int], int], activeLimit: int, ):
        ...

    @typing.overload
    def __init__(self, user: AdventureBot.User.User, ):
        ...

    def ChangeProportion(self, property: AdventureBot.StructFlag[int], count: int, ) -> None:
        ...

    def GetAvailableProportions(self, ) -> System.Collections.Generic.List[AdventureBot.StructFlag[int]]:
        ...

    def FindAvailableItems(self, ) -> System.Collections.Generic.IEnumerable[AdventureBot.Item.ItemInfo]:
        ...

    @staticmethod
    def GroupByStats(items: System.Collections.Generic.IEnumerable[AdventureBot.Item.ItemInfo], ) -> System.Collections.Generic.IReadOnlyDictionary[AdventureBot.StructFlag[int], AdventureBot.MustBeOrderedList[AdventureBot.Item.ItemInfo]]:
        ...

    @staticmethod
    def GroupByChangeType(items: AdventureBot.MustBeOrderedList[AdventureBot.Item.ItemInfo], ) -> System.Collections.Generic.IDictionary[int, AdventureBot.MustBeOrderedList[AdventureBot.Item.ItemInfo]]:
        ...

    @staticmethod
    def TakeBest(count: int, items: AdventureBot.MustBeOrderedList[AdventureBot.Item.ItemInfo], ) -> AdventureBot.MustBeOrderedList[AdventureBot.Item.ItemInfo]:
        ...

    def DetectUseSet(self, prop: AdventureBot.StructFlag[int], items: System.Collections.Generic.IDictionary[int, AdventureBot.MustBeOrderedList[AdventureBot.Item.ItemInfo]], ) -> bool:
        ...

    def ActivateItems(self, prop: AdventureBot.StructFlag[int], items: AdventureBot.MustBeOrderedList[AdventureBot.Item.ItemInfo], ) -> System.Collections.Generic.List[AdventureBot.Item.ItemInfo]:
        ...

    def RecalculateActive(self, ) -> None:
        ...

class QuestManager(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        self.User: AdventureBot.User.User
        ...

    # static fields

    # properties
    @property
    def Quests(self) -> System.Collections.Immutable.ImmutableDictionary[str, System.Collections.Immutable.ImmutableDictionary[System.Guid, AdventureBot.Quest.QuestInfo]]:
        ...

    # methods
    @typing.overload
    def __init__(self, quests: System.Collections.Generic.Dictionary[str, System.Collections.Generic.Dictionary[System.Guid, AdventureBot.Quest.QuestInfo]], ):
        ...

    @typing.overload
    def __init__(self, user: AdventureBot.User.User, ):
        ...

    def BeginQuest(self, id: str, ) -> System.Guid:
        ...

    def FinishQuest(self, id: str, questId: System.Guid, ) -> bool:
        ...

class DbColumnAttribute(System.Attribute):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def Name(self) -> str:
        ...

    @property
    def Type(self) -> int:
        ...

    @property
    def TypeString(self) -> str:
        ...

    @property
    def TypeId(self) -> System.Object:
        ...

    # methods
    def __init__(self, name: str, type: int, ):
        ...

class ItemManager(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        self.User: AdventureBot.User.User
        ...

    # static fields

    # properties
    @property
    def Items(self) -> System.Collections.Generic.IReadOnlyList[AdventureBot.Item.ItemInfo]:
        ...

    # methods
    @typing.overload
    def __init__(self, items: System.Collections.Generic.List[AdventureBot.Item.ItemInfo], ):
        ...

    @typing.overload
    def __init__(self, user: AdventureBot.User.User, ):
        ...

    def Add(self, item: AdventureBot.Item.ItemInfo, ) -> None:
        ...

    def Remove(self, item: AdventureBot.Item.ItemInfo, ) -> bool:
        ...

    def Get(self, identifier: str, ) -> AdventureBot.Item.ItemInfo:
        ...

class ShownStats(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    Health: int = ...
    Mana: int = ...
    Stamina: int = ...
    Default: int = ...
    Gold: int = ...
    Intelligence: int = ...
    Strength: int = ...
    Defence: int = ...
    Karma: int = ...

