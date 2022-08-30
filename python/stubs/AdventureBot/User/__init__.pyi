from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import System
import System.Collections.Generic
import AdventureBot.Item
import AdventureBot
import AdventureBot.User.Stats
import AdventureBot.User
import Microsoft.Data.Sqlite
import System.Data
import System.Linq.Expressions
import System.Runtime.Serialization
import System.Reflection
import AdventureBot.Messenger
import System.Collections.Immutable
import AdventureBot.Quest
import AdventureBot.User.RoomManager
import AdventureBot.Room

T = typing.TypeVar('T')

class ActiveItemsManager(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def ActiveItems(self) -> System.Collections.Generic.IReadOnlyList[AdventureBot.Item.ItemInfo]:
        ...

    @property
    def ActiveProportions(self) -> System.Collections.Generic.IReadOnlyDictionary[AdventureBot.StructFlag[AdventureBot.User.Stats.StatsProperty], System.Int32]:
        ...

    @property
    def ActiveLimit(self) -> System.Int32:
        ...

    # methods
    @typing.overload
    def __init__(self, activeItems: System.Collections.Generic.List[AdventureBot.Item.ItemInfo], activeProportions: System.Collections.Generic.Dictionary[AdventureBot.StructFlag[AdventureBot.User.Stats.StatsProperty], System.Int32], activeLimit: System.Int32, ):
        ...

    @typing.overload
    def __init__(self, user: AdventureBot.User.User, ):
        ...

    @typing.overload
    def ChangeProportion(self, property: AdventureBot.StructFlag[AdventureBot.User.Stats.StatsProperty], count: System.Int32, ) -> None:
        ...

    @typing.overload
    def GetAvailableProportions(self, ) -> System.Collections.Generic.List[AdventureBot.StructFlag[AdventureBot.User.Stats.StatsProperty]]:
        ...

class DbColumnAttribute(System.Attribute):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def Name(self) -> System.String:
        ...

    @property
    def Type(self) -> Microsoft.Data.Sqlite.SqliteType:
        ...

    @property
    def TypeString(self) -> System.String:
        ...

    @property
    def TypeId(self) -> System.Object:
        ...

    # methods
    @typing.overload
    def __init__(self, name: System.String, type: System.Data.DbType, ):
        ...

class DatabaseVariables(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def Level(self) -> System.Int32:
        ...

    @property
    def Experience(self) -> System.Decimal:
        ...

    @property
    def Gold(self) -> System.Decimal:
        ...

    @property
    def Monsters(self) -> System.Int32:
        ...

    @property
    def Rooms(self) -> System.Int32:
        ...

    @property
    def LastMessageReceived(self) -> System.DateTime:
        ...

    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def Fill(self, variables: AdventureBot.User.DatabaseVariables, ) -> None:
        ...

    @typing.overload
    @staticmethod
    def GetColumns() -> list[System.ValueTuple[AdventureBot.User.DbColumnAttribute, System.Func[AdventureBot.User.DatabaseVariables, System.Object]]]:
        ...

    @typing.overload
    @staticmethod
    def GetColumn(getter: System.Linq.Expressions.Expression[System.Func[AdventureBot.User.DatabaseVariables, System.Object]], ) -> AdventureBot.User.DbColumnAttribute:
        ...

class GameEventHandler(System.ICloneable, System.Runtime.Serialization.ISerializable, System.MulticastDelegate):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def Target(self) -> System.Object:
        ...

    @property
    def Method(self) -> System.Reflection.MethodInfo:
        ...

    # methods
    @typing.overload
    def __init__(self, object: System.Object, method: System.IntPtr, ):
        ...

    @typing.overload
    def Invoke(self, user: AdventureBot.User.User, ) -> None:
        ...

    @typing.overload
    def BeginInvoke(self, user: AdventureBot.User.User, callback: System.AsyncCallback, object: System.Object, ) -> System.IAsyncResult:
        ...

    @typing.overload
    def EndInvoke(self, result: System.IAsyncResult, ) -> None:
        ...

class GameEventHandler(System.ICloneable, System.Runtime.Serialization.ISerializable, System.MulticastDelegate, typing.Generic[T]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def Target(self) -> System.Object:
        ...

    @property
    def Method(self) -> System.Reflection.MethodInfo:
        ...

    # methods
    @typing.overload
    def __init__(self, object: System.Object, method: System.IntPtr, ):
        ...

    @typing.overload
    def Invoke(self, user: AdventureBot.User.User, param: T, ) -> None:
        ...

    @typing.overload
    def BeginInvoke(self, user: AdventureBot.User.User, param: T, callback: System.AsyncCallback, object: System.Object, ) -> System.IAsyncResult:
        ...

    @typing.overload
    def EndInvoke(self, result: System.IAsyncResult, ) -> None:
        ...

class ItemManager(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

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

    @typing.overload
    def Add(self, item: AdventureBot.Item.ItemInfo, ) -> None:
        ...

    @typing.overload
    def Remove(self, item: AdventureBot.Item.ItemInfo, ) -> System.Boolean:
        ...

    @typing.overload
    def Get(self, identifier: System.String, ) -> AdventureBot.Item.ItemInfo:
        ...

class ShownStats(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    Health: System.Int32 = Health
    Mana: System.Int32 = Mana
    Stamina: System.Int32 = Stamina
    Default: System.Int32 = Default
    Gold: System.Int32 = Gold
    Intelligence: System.Int32 = Intelligence
    Strength: System.Int32 = Strength
    Defence: System.Int32 = Defence
    Karma: System.Int32 = Karma

class MessageManager(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        self.ShownStats: AdventureBot.User.ShownStats
        ...

    # properties
    @property
    def LastMessages(self) -> System.Collections.Generic.IReadOnlyCollection[AdventureBot.Messenger.SentMessage]:
        ...

    @property
    def LastMessage(self) -> AdventureBot.Messenger.SentMessage:
        ...

    @property
    def LastMessageReceived(self) -> System.DateTime:
        ...

    @property
    def ChatId(self) -> AdventureBot.ChatId:
        ...

    # methods
    @typing.overload
    def __init__(self, user: AdventureBot.User.User, ):
        ...

    @typing.overload
    def __init__(self, queue: System.Collections.Generic.List[AdventureBot.Messenger.SentMessage], buttons: list[list[System.String]], preferToUpdate: System.Boolean, lastMessages: System.Collections.Generic.Queue[AdventureBot.Messenger.SentMessage], chatId: AdventureBot.ChatId, recievedMessage: AdventureBot.Messenger.ReceivedMessage, shownStats: AdventureBot.User.ShownStats, intent: System.String, ):
        ...

    @typing.overload
    def SendMessage(self, message: AdventureBot.Messenger.SentMessage, ) -> None:
        ...

    @typing.overload
    def Finish(self, ) -> None:
        ...

    @typing.overload
    @staticmethod
    def Escape(message: System.String, ) -> System.String:
        ...

class PublicUser(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def Info(self) -> AdventureBot.User.UserInfo:
        ...

    @property
    def ActiveItemsManager(self) -> AdventureBot.User.ActiveItemsManager:
        ...

    @property
    def ItemManager(self) -> AdventureBot.User.ItemManager:
        ...

    @property
    def RoomManager(self) -> AdventureBot.User.RoomManager:
        ...

    @property
    def MessageManager(self) -> AdventureBot.User.MessageManager:
        ...

    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def __init__(self, user: AdventureBot.User.User, ):
        ...

class QuestManager(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def Quests(self) -> System.Collections.Immutable.ImmutableDictionary[System.String, System.Collections.Immutable.ImmutableDictionary[System.Guid, AdventureBot.Quest.QuestInfo]]:
        ...

    # methods
    @typing.overload
    def __init__(self, quests: System.Collections.Generic.Dictionary[System.String, System.Collections.Generic.Dictionary[System.Guid, AdventureBot.Quest.QuestInfo]], ):
        ...

    @typing.overload
    def __init__(self, user: AdventureBot.User.User, ):
        ...

    @typing.overload
    def BeginQuest(self, id: System.String, ) -> System.Guid:
        ...

    @typing.overload
    def FinishQuest(self, id: System.String, questId: System.Guid, ) -> System.Boolean:
        ...

class RoomManager(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def CurrentRootRoom(self) -> System.String:
        ...

    # methods
    @typing.overload
    def __init__(self, currentRoom: AdventureBot.User.RoomManager.StackedRoom, rooms: System.Collections.Generic.Stack[AdventureBot.User.RoomManager.StackedRoom], ):
        ...

    @typing.overload
    def __init__(self, user: AdventureBot.User.User, ):
        ...

    @typing.overload
    def Go(self, roomIdentifier: System.String, leave: System.Boolean, ) -> None:
        ...

    @typing.overload
    def Leave(self, doReturn: System.Boolean, checkLeave: System.Boolean, ) -> None:
        ...

    @typing.overload
    def ChangeRoot(self, rootIdentifier: System.String, ) -> None:
        ...

    @typing.overload
    def GetRoom(self, ) -> AdventureBot.Room.IRoom:
        ...

class User(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        self.Random: System.Random
        ...

    # properties
    @property
    def Info(self) -> AdventureBot.User.UserInfo:
        ...

    @property
    def ActiveItemsManager(self) -> AdventureBot.User.ActiveItemsManager:
        ...

    @property
    def ItemManager(self) -> AdventureBot.User.ItemManager:
        ...

    @property
    def VariableManager(self) -> AdventureBot.User.VariableManager:
        ...

    @property
    def RoomManager(self) -> AdventureBot.User.RoomManager:
        ...

    @property
    def MessageManager(self) -> AdventureBot.User.MessageManager:
        ...

    @property
    def QuestManager(self) -> AdventureBot.User.QuestManager:
        ...

    @property
    def Token(self) -> System.Guid:
        ...
    @Token.setter
    def Token(self, val: System.Guid):
        ...

    # methods
    @typing.overload
    def __init__(self, itemManager: AdventureBot.User.ItemManager, activeItemsManager: AdventureBot.User.ActiveItemsManager, info: AdventureBot.User.UserInfo, variableManager: AdventureBot.User.VariableManager, roomManager: AdventureBot.User.RoomManager, messageManager: AdventureBot.User.MessageManager, questManager: AdventureBot.User.QuestManager, token: System.Guid, linkedTo: System.Tuple[AdventureBot.UserId, System.Guid], ):
        ...

    @typing.overload
    def __init__(self, userId: AdventureBot.UserId, ):
        ...

class UserInfo(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def Dead(self) -> System.Boolean:
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
    def Name(self) -> System.String:
        ...
    @Name.setter
    def Name(self, val: System.String):
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

    @property
    def CurrentStats(self) -> AdventureBot.User.Stats.Stats:
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
    def __init__(self, dead: System.Boolean, userId: AdventureBot.UserId, baseStats: AdventureBot.User.Stats.Stats, currentStats: AdventureBot.User.Stats.Stats, _name: System.String, statistics: AdventureBot.User.Stats.Statistics, level: AdventureBot.User.Stats.UserLevel, ):
        ...

    @typing.overload
    def __init__(self, userId: AdventureBot.UserId, user: AdventureBot.User.User, ):
        ...

    @typing.overload
    def TryDecreaseGold(self, value: System.Decimal, ) -> System.Boolean:
        ...

    @typing.overload
    def ChangeStats(self, property: AdventureBot.User.Stats.StatsProperty, value: System.Decimal, set: System.Boolean, ) -> System.Boolean:
        ...

    @typing.overload
    def Kill(self, ) -> None:
        ...

    @typing.overload
    @staticmethod
    def CalculateDefence(damage: System.Decimal, defence: System.Decimal, ) -> System.Decimal:
        ...

    @typing.overload
    def MakeDamage(self, value: System.Decimal, defence: System.Boolean, kill: System.Boolean, ) -> None:
        ...

    @typing.overload
    def KarmaEffect(self, value: System.Decimal, ) -> System.Decimal:
        ...

class VariableManager(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        self.PersistentVariables: AdventureBot.VariableContainer
        self.UserVariables: AdventureBot.VariableContainer
        ...

    # properties
    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def __init__(self, roomVariables: System.Collections.Generic.Dictionary[System.String, AdventureBot.VariableContainer], itemVariables: System.Collections.Generic.Dictionary[System.String, AdventureBot.VariableContainer], questVariables: System.Collections.Generic.Dictionary[System.String, System.Collections.Generic.Dictionary[System.Guid, AdventureBot.VariableContainer]], persistentVariables: AdventureBot.VariableContainer, userVariables: AdventureBot.VariableContainer, ):
        ...

