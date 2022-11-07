from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import System


class DispatchState(System.ValueType):
    @typing.overload
    def __init__(self, **kwargs):
        self.StackTrace: System.Array[int]
        self.DynamicMethods: System.Array[System.Object]
        self.RemoteStackTrace: str
        self.IpForWatsonBuckets: System.UIntPtr
        self.WatsonBuckets: System.Array[int]
        ...

    # static fields

    # properties
    # methods
    def __init__(self, stackTrace: System.Array[int], dynamicMethods: System.Array[System.Object], remoteStackTrace: str, ipForWatsonBuckets: System.UIntPtr, watsonBuckets: System.Array[int], ):
        ...

class ExceptionMessageKind(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    ThreadAbort: int = ...
    ThreadInterrupted: int = ...
    OutOfMemory: int = ...

