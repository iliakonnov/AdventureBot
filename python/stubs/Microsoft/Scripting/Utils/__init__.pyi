from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import System
import Microsoft.Scripting.Utils.ThreadLocal

T = typing.TypeVar('T')

class ThreadLocal(System.Object, typing.Generic[T]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def Value(self) -> T:
        ...
    @Value.setter
    def Value(self, val: T):
        ...

    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def __init__(self, refCounted: bool, ):
        ...

    def GetOrCreate(self, func: System.Func[T], ) -> T:
        ...

    @typing.overload
    def Update(self, updater: System.Func[T, T], ) -> T:
        ...

    @typing.overload
    def Update(self, newValue: T, ) -> T:
        ...

    @staticmethod
    def GetCurrentThreadId() -> int:
        ...

    @typing.overload
    def GetStorageInfo(self, ) -> Microsoft.Scripting.Utils.ThreadLocal.StorageInfo[T]:
        ...

    @typing.overload
    def GetStorageInfo(self, curStorage: System.Array[Microsoft.Scripting.Utils.ThreadLocal.StorageInfo[T]], ) -> Microsoft.Scripting.Utils.ThreadLocal.StorageInfo[T]:
        ...

    def RetryOrCreateStorageInfo(self, curStorage: System.Array[Microsoft.Scripting.Utils.ThreadLocal.StorageInfo[T]], ) -> Microsoft.Scripting.Utils.ThreadLocal.StorageInfo[T]:
        ...

    def CreateStorageInfo(self, ) -> Microsoft.Scripting.Utils.ThreadLocal.StorageInfo[T]:
        ...

class ConsoleStreamType(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    Input: int = ...
    Output: int = ...
    ErrorOutput: int = ...

