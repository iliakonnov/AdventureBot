from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import System


class TimeoutTracker(System.ValueType):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def RemainingMilliseconds(self) -> int:
        ...

    @property
    def IsExpired(self) -> bool:
        ...

    # methods
    @typing.overload
    def __init__(self, timeout: System.TimeSpan, ):
        ...

    @typing.overload
    def __init__(self, millisecondsTimeout: int, ):
        ...

class EnterLockType(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    Read: int = ...
    UpgradeableRead: int = ...
    Write: int = ...
    UpgradeToWrite: int = ...

