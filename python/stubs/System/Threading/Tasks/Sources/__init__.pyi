from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import System
import System.Threading.Tasks.Sources

TResult = typing.TypeVar('TResult')

class IValueTaskSource(abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    # methods
    @typing.overload
    @abc.abstractmethod
    def GetStatus(self, token: System.Int16, ) -> System.Threading.Tasks.Sources.ValueTaskSourceStatus:
        ...

    @typing.overload
    @abc.abstractmethod
    def OnCompleted(self, continuation: System.Action[System.Object], state: System.Object, token: System.Int16, flags: System.Threading.Tasks.Sources.ValueTaskSourceOnCompletedFlags, ) -> None:
        ...

    @typing.overload
    @abc.abstractmethod
    def GetResult(self, token: System.Int16, ) -> None:
        ...

class IValueTaskSource(abc.ABC, typing.Generic[TResult]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    # methods
    @typing.overload
    @abc.abstractmethod
    def GetStatus(self, token: System.Int16, ) -> System.Threading.Tasks.Sources.ValueTaskSourceStatus:
        ...

    @typing.overload
    @abc.abstractmethod
    def OnCompleted(self, continuation: System.Action[System.Object], state: System.Object, token: System.Int16, flags: System.Threading.Tasks.Sources.ValueTaskSourceOnCompletedFlags, ) -> None:
        ...

    @typing.overload
    @abc.abstractmethod
    def GetResult(self, token: System.Int16, ) -> TResult:
        ...

class ValueTaskSourceStatus(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    Pending: System.Int32 = Pending
    Succeeded: System.Int32 = Succeeded
    Faulted: System.Int32 = Faulted
    Canceled: System.Int32 = Canceled

class ValueTaskSourceOnCompletedFlags(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    None_: System.Int32 = None
    UseSchedulingContext: System.Int32 = UseSchedulingContext
    FlowExecutionContext: System.Int32 = FlowExecutionContext

