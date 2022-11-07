from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import System.Runtime.CompilerServices
import System
import System.Threading.Tasks

TResult = typing.TypeVar('TResult')

class ConfiguredTaskAwaiter(System.Runtime.CompilerServices.ICriticalNotifyCompletion, System.Runtime.CompilerServices.INotifyCompletion, System.Runtime.CompilerServices.IConfiguredTaskAwaiter, System.ValueType, typing.Generic[TResult]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def IsCompleted(self) -> bool:
        ...

    # methods
    def __init__(self, task: System.Threading.Tasks.Task[TResult], continueOnCapturedContext: bool, ):
        ...

    def OnCompleted(self, continuation: System.Action, ) -> None:
        ...

    def UnsafeOnCompleted(self, continuation: System.Action, ) -> None:
        ...

    def GetResult(self, ) -> TResult:
        ...

class ConfiguredTaskAwaiter(System.Runtime.CompilerServices.ICriticalNotifyCompletion, System.Runtime.CompilerServices.INotifyCompletion, System.Runtime.CompilerServices.IConfiguredTaskAwaiter, System.ValueType):
    @typing.overload
    def __init__(self, **kwargs):
        self.m_task: System.Threading.Tasks.Task
        self.m_continueOnCapturedContext: bool
        ...

    # static fields

    # properties
    @property
    def IsCompleted(self) -> bool:
        ...

    # methods
    def __init__(self, task: System.Threading.Tasks.Task, continueOnCapturedContext: bool, ):
        ...

    def OnCompleted(self, continuation: System.Action, ) -> None:
        ...

    def UnsafeOnCompleted(self, continuation: System.Action, ) -> None:
        ...

    def GetResult(self, ) -> None:
        ...

