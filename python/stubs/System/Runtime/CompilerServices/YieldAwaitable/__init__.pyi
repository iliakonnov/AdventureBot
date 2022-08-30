from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import System.Runtime.CompilerServices
import System


class YieldAwaiter(System.Runtime.CompilerServices.ICriticalNotifyCompletion, System.Runtime.CompilerServices.INotifyCompletion, System.Runtime.CompilerServices.IStateMachineBoxAwareAwaiter, System.ValueType):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def IsCompleted(self) -> System.Boolean:
        ...

    # methods
    @typing.overload
    def OnCompleted(self, continuation: System.Action, ) -> None:
        ...

    @typing.overload
    def UnsafeOnCompleted(self, continuation: System.Action, ) -> None:
        ...

    @typing.overload
    def GetResult(self, ) -> None:
        ...

