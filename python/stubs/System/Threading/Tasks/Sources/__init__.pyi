from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import System

TResult = typing.TypeVar('TResult')

class IValueTaskSource(abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    @abc.abstractmethod
    def GetStatus(self, token: int, ) -> int:
        ...

    @abc.abstractmethod
    def OnCompleted(self, continuation: System.Action[System.Object], state: System.Object, token: int, flags: int, ) -> None:
        ...

    @abc.abstractmethod
    def GetResult(self, token: int, ) -> None:
        ...

class ValueTaskSourceOnCompletedFlags(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    None_: int = ...
    UseSchedulingContext: int = ...
    FlowExecutionContext: int = ...

class ValueTaskSourceStatus(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    Pending: int = ...
    Succeeded: int = ...
    Faulted: int = ...
    Canceled: int = ...

class IValueTaskSource(abc.ABC, typing.Generic[TResult]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    @abc.abstractmethod
    def GetStatus(self, token: int, ) -> int:
        ...

    @abc.abstractmethod
    def OnCompleted(self, continuation: System.Action[System.Object], state: System.Object, token: int, flags: int, ) -> None:
        ...

    @abc.abstractmethod
    def GetResult(self, token: int, ) -> TResult:
        ...

