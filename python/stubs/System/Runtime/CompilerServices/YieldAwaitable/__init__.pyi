from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import System.Runtime.CompilerServices
import System


class YieldAwaiter(System.Runtime.CompilerServices.ICriticalNotifyCompletion, System.Runtime.CompilerServices.INotifyCompletion, System.Runtime.CompilerServices.IStateMachineBoxAwareAwaiter, System.ValueType):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def IsCompleted(self) -> bool:
        ...

    # methods
    def OnCompleted(self, continuation: System.Action, ) -> None:
        ...

    def UnsafeOnCompleted(self, continuation: System.Action, ) -> None:
        ...

    @staticmethod
    def QueueContinuation(continuation: System.Action, flowContext: bool, ) -> None:
        ...

    def AwaitUnsafeOnCompleted(self, box: System.Runtime.CompilerServices.IAsyncStateMachineBox, ) -> None:
        ...

    @staticmethod
    def OutputCorrelationEtwEvent(continuation: System.Action, ) -> System.Action:
        ...

    @staticmethod
    def RunAction(state: System.Object, ) -> None:
        ...

    def GetResult(self, ) -> None:
        ...

