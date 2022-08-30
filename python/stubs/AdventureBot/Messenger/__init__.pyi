from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import System
import System.Runtime.Serialization
import System.Reflection
import AdventureBot.Messenger
import AdventureBot.User
import System.Threading.Tasks
import AdventureBot.Messenger.ReceivedMessage
import AdventureBot
import System.Collections.Generic
import AdventureBot.ObjectManager


class MessageHandler(System.ICloneable, System.Runtime.Serialization.ISerializable, System.MulticastDelegate):
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
    def Invoke(self, message: AdventureBot.Messenger.ReceivedMessage, ) -> None:
        ...

    @typing.overload
    def BeginInvoke(self, message: AdventureBot.Messenger.ReceivedMessage, callback: System.AsyncCallback, object: System.Object, ) -> System.IAsyncResult:
        ...

    @typing.overload
    def EndInvoke(self, result: System.IAsyncResult, ) -> None:
        ...

class IMessenger(abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    # methods
    @typing.overload
    @abc.abstractmethod
    def Send(self, message: AdventureBot.Messenger.SentMessage, receivedMessage: AdventureBot.Messenger.ReceivedMessage, user: AdventureBot.User.User, ) -> System.Threading.Tasks.Task:
        ...

    @typing.overload
    @abc.abstractmethod
    def BeginPolling(self, ) -> None:
        ...

class ReceivedMessage(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        self.Action: AdventureBot.Messenger.ReceivedMessage.Handler
        self.ChatId: AdventureBot.ChatId
        self.MessageId: System.String
        self.MessengerSpecificData: System.Object
        self.Text: System.String
        self.UserId: AdventureBot.UserId
        ...

    # properties
    # methods
    @typing.overload
    def __init__(self, ):
        ...

class SentMessage(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        self.Buttons: list[list[System.String]]
        self.ChatId: AdventureBot.ChatId
        self.MessengerSpecificData: System.Collections.Generic.Dictionary[System.Int32, System.Object]
        self.Formatted: System.Boolean
        self.PreferToUpdate: System.Nullable[System.Boolean]
        self.Text: System.String
        ...

    # properties
    @property
    def Intent(self) -> System.String:
        ...
    @Intent.setter
    def Intent(self, val: System.String):
        ...

    # methods
    @typing.overload
    def __init__(self, ):
        ...

class MessengerManager(AdventureBot.ObjectManager.IManager[AdventureBot.Messenger.IMessenger], System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def Register(self, attribute: AdventureBot.ObjectManager.GameObjectAttribute, creator: AdventureBot.ObjectManager.Create[AdventureBot.Messenger.IMessenger], ) -> None:
        ...

    @typing.overload
    def Register(self, messenger: AdventureBot.Messenger.IMessenger, ) -> None:
        ...

    @typing.overload
    def BeginPolling(self, ) -> None:
        ...

    @typing.overload
    def Reply(self, message: AdventureBot.Messenger.SentMessage, receivedMessage: AdventureBot.Messenger.ReceivedMessage, user: AdventureBot.User.User, ) -> None:
        ...

