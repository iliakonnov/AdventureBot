from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import System
import System.Runtime.Serialization
import System.Reflection
import AdventureBot.Messenger
import AdventureBot.User


class Handler(System.ICloneable, System.Runtime.Serialization.ISerializable, System.MulticastDelegate):
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
    def Invoke(self, message: AdventureBot.Messenger.ReceivedMessage, user: AdventureBot.User.User, ) -> None:
        ...

    @typing.overload
    def BeginInvoke(self, message: AdventureBot.Messenger.ReceivedMessage, user: AdventureBot.User.User, callback: System.AsyncCallback, object: System.Object, ) -> System.IAsyncResult:
        ...

    @typing.overload
    def EndInvoke(self, result: System.IAsyncResult, ) -> None:
        ...

