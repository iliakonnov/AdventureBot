from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import AdventureBot.Messenger
import AdventureBot.User
import System.Threading.Tasks
import System
import AdventureBot.Messenger.ReceivedMessage
import AdventureBot
import AdventureBot.ObjectManager
import System.Collections.Generic
import System.Runtime.Serialization
import System.Reflection


class IMessenger(abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    @abc.abstractmethod
    def Send(self, message: AdventureBot.Messenger.SentMessage, receivedMessage: AdventureBot.Messenger.ReceivedMessage, user: AdventureBot.User.User, ) -> System.Threading.Tasks.Task:
        ...

    @abc.abstractmethod
    def BeginPolling(self, ) -> None:
        ...

class ReceivedMessage(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        self.Action: AdventureBot.Messenger.ReceivedMessage.Handler
        self.ChatId: AdventureBot.ChatId
        self.MessageId: str
        self.MessengerSpecificData: System.Object
        self.Text: str
        self.UserId: AdventureBot.UserId
        ...

    # static fields

    # properties
    # methods
    def __init__(self, ):
        ...

class MessengerManager(AdventureBot.ObjectManager.IManager[AdventureBot.Messenger.IMessenger], System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    def __init__(self, ):
        ...

    @typing.overload
    def Register(self, attribute: AdventureBot.ObjectManager.GameObjectAttribute, creator: AdventureBot.ObjectManager.Create[AdventureBot.Messenger.IMessenger], ) -> None:
        ...

    @typing.overload
    def Register(self, messenger: AdventureBot.Messenger.IMessenger, ) -> None:
        ...

    @staticmethod
    def MessageHandler(message: AdventureBot.Messenger.ReceivedMessage, ) -> None:
        ...

    def BeginPolling(self, ) -> None:
        ...

    def Reply(self, message: AdventureBot.Messenger.SentMessage, receivedMessage: AdventureBot.Messenger.ReceivedMessage, user: AdventureBot.User.User, ) -> None:
        ...

class SentMessage(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        self.Buttons: System.Array[System.Array[str]]
        self.ChatId: AdventureBot.ChatId
        self.MessengerSpecificData: System.Collections.Generic.Dictionary[int, System.Object]
        self.Formatted: bool
        self.PreferToUpdate: System.Nullable[bool]
        self.Text: str
        ...

    # static fields

    # properties
    @property
    def Intent(self) -> str:
        ...
    @Intent.setter
    def Intent(self, val: str):
        ...

    # methods
    def __init__(self, ):
        ...

class MessageHandler(System.ICloneable, System.Runtime.Serialization.ISerializable, System.MulticastDelegate):
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

    def Invoke(self, message: AdventureBot.Messenger.ReceivedMessage, ) -> None:
        ...

    def BeginInvoke(self, message: AdventureBot.Messenger.ReceivedMessage, callback: System.AsyncCallback, object: System.Object, ) -> System.IAsyncResult:
        ...

    def EndInvoke(self, result: System.IAsyncResult, ) -> None:
        ...

