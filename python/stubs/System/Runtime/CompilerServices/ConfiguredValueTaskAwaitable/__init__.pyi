from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import System.Runtime.CompilerServices
import System

TResult = typing.TypeVar('TResult')

class ConfiguredValueTaskAwaiter(System.Runtime.CompilerServices.ICriticalNotifyCompletion, System.Runtime.CompilerServices.INotifyCompletion, System.Runtime.CompilerServices.IStateMachineBoxAwareAwaiter, System.ValueType):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def IsCompleted(self) -> System.Boolean:
        ...

    # methods
    @typing.overload
    def GetResult(self, ) -> None:
        ...

    @typing.overload
    def OnCompleted(self, continuation: System.Action, ) -> None:
        ...

    @typing.overload
    def UnsafeOnCompleted(self, continuation: System.Action, ) -> None:
        ...

class ConfiguredValueTaskAwaiter(System.Runtime.CompilerServices.ICriticalNotifyCompletion, System.Runtime.CompilerServices.INotifyCompletion, System.Runtime.CompilerServices.IStateMachineBoxAwareAwaiter, System.ValueType, typing.Generic[TResult]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def IsCompleted(self) -> System.Boolean:
        ...

    # methods
    @typing.overload
    def GetResult(self, ) -> TResult:
        ...

    @typing.overload
    def OnCompleted(self, continuation: System.Action, ) -> None:
        ...

    @typing.overload
    def UnsafeOnCompleted(self, continuation: System.Action, ) -> None:
        ...

