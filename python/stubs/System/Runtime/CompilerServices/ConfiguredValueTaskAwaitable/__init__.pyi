from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import System.Runtime.CompilerServices
import System
import System.Threading.Tasks

TResult = typing.TypeVar('TResult')

class ConfiguredValueTaskAwaiter(System.Runtime.CompilerServices.ICriticalNotifyCompletion, System.Runtime.CompilerServices.INotifyCompletion, System.Runtime.CompilerServices.IStateMachineBoxAwareAwaiter, System.ValueType, typing.Generic[TResult]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def IsCompleted(self) -> bool:
        ...

    # methods
    def __init__(self, value: ref[System.Threading.Tasks.ValueTask[TResult]], ):
        ...

    def GetResult(self, ) -> TResult:
        ...

    def OnCompleted(self, continuation: System.Action, ) -> None:
        ...

    def UnsafeOnCompleted(self, continuation: System.Action, ) -> None:
        ...

    def AwaitUnsafeOnCompleted(self, box: System.Runtime.CompilerServices.IAsyncStateMachineBox, ) -> None:
        ...

class ConfiguredValueTaskAwaiter(System.Runtime.CompilerServices.ICriticalNotifyCompletion, System.Runtime.CompilerServices.INotifyCompletion, System.Runtime.CompilerServices.IStateMachineBoxAwareAwaiter, System.ValueType):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def IsCompleted(self) -> bool:
        ...

    # methods
    def __init__(self, value: ref[System.Threading.Tasks.ValueTask], ):
        ...

    def GetResult(self, ) -> None:
        ...

    def OnCompleted(self, continuation: System.Action, ) -> None:
        ...

    def UnsafeOnCompleted(self, continuation: System.Action, ) -> None:
        ...

    def AwaitUnsafeOnCompleted(self, box: System.Runtime.CompilerServices.IAsyncStateMachineBox, ) -> None:
        ...

