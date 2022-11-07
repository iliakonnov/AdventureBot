from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import System
import System.Threading.CancellationTokenSource
import System.Threading
import System.Threading.Tasks


class CallbackNode(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        self.Registrations: System.Threading.CancellationTokenSource.Registrations
        self.Prev: System.Threading.CancellationTokenSource.CallbackNode
        self.Next: System.Threading.CancellationTokenSource.CallbackNode
        self.Id: int
        self.Callback: System.Delegate
        self.CallbackState: System.Object
        self.ExecutionContext: System.Threading.ExecutionContext
        self.SynchronizationContext: System.Threading.SynchronizationContext
        ...

    # static fields

    # properties
    # methods
    def __init__(self, registrations: System.Threading.CancellationTokenSource.Registrations, ):
        ...

    def ExecuteCallback(self, ) -> None:
        ...

class Registrations(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        self.Source: System.Threading.CancellationTokenSource
        self.Callbacks: System.Threading.CancellationTokenSource.CallbackNode
        self.FreeNodeList: System.Threading.CancellationTokenSource.CallbackNode
        self.NextAvailableId: int
        self.ExecutingCallbackId: int
        self.ThreadIDExecutingCallbacks: int
        ...

    # static fields

    # properties
    # methods
    def __init__(self, source: System.Threading.CancellationTokenSource, ):
        ...

    def Recycle(self, node: System.Threading.CancellationTokenSource.CallbackNode, ) -> None:
        ...

    def Unregister(self, id: int, node: System.Threading.CancellationTokenSource.CallbackNode, ) -> bool:
        ...

    def UnregisterAll(self, ) -> None:
        ...

    def WaitForCallbackToComplete(self, id: int, ) -> None:
        ...

    def WaitForCallbackToCompleteAsync(self, id: int, ) -> System.Threading.Tasks.ValueTask:
        ...

    def EnterLock(self, ) -> None:
        ...

    def ExitLock(self, ) -> None:
        ...

