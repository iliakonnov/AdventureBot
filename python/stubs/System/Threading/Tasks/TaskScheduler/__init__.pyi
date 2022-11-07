from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import System.Runtime.CompilerServices
import System
import System.Threading.Tasks


class TaskSchedulerAwaiter(System.Runtime.CompilerServices.ICriticalNotifyCompletion, System.Runtime.CompilerServices.INotifyCompletion, System.ValueType):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def IsCompleted(self) -> bool:
        ...

    # methods
    def __init__(self, scheduler: System.Threading.Tasks.TaskScheduler, ):
        ...

    def GetResult(self, ) -> None:
        ...

    def OnCompleted(self, continuation: System.Action, ) -> None:
        ...

    def UnsafeOnCompleted(self, continuation: System.Action, ) -> None:
        ...

