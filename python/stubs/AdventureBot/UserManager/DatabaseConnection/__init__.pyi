from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import System
import System.Runtime.Serialization
import System.Reflection
import Microsoft.Data.Sqlite

T = typing.TypeVar('T')

class Void(System.ValueType):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    # methods
class QueryCallback(System.ICloneable, System.Runtime.Serialization.ISerializable, System.MulticastDelegate, typing.Generic[T]):
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
    def Invoke(self, command: Microsoft.Data.Sqlite.SqliteCommand, ) -> T:
        ...

    @typing.overload
    def BeginInvoke(self, command: Microsoft.Data.Sqlite.SqliteCommand, callback: System.AsyncCallback, object: System.Object, ) -> System.IAsyncResult:
        ...

    @typing.overload
    def EndInvoke(self, result: System.IAsyncResult, ) -> T:
        ...

