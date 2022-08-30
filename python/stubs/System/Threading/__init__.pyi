from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import System
import Microsoft.Win32.SafeHandles
import System.Threading
import System.Threading.Tasks


class WaitHandle(System.IDisposable, System.MarshalByRefObject, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def Handle(self) -> System.IntPtr:
        ...
    @Handle.setter
    def Handle(self, val: System.IntPtr):
        ...

    @property
    def SafeWaitHandle(self) -> Microsoft.Win32.SafeHandles.SafeWaitHandle:
        ...
    @SafeWaitHandle.setter
    def SafeWaitHandle(self, val: Microsoft.Win32.SafeHandles.SafeWaitHandle):
        ...

    # methods
    @typing.overload
    def Close(self, ) -> None:
        ...

    @typing.overload
    def Dispose(self, ) -> None:
        ...

    @typing.overload
    def WaitOne(self, millisecondsTimeout: System.Int32, ) -> System.Boolean:
        ...

    @typing.overload
    def WaitOne(self, timeout: System.TimeSpan, ) -> System.Boolean:
        ...

    @typing.overload
    def WaitOne(self, ) -> System.Boolean:
        ...

    @typing.overload
    def WaitOne(self, millisecondsTimeout: System.Int32, exitContext: System.Boolean, ) -> System.Boolean:
        ...

    @typing.overload
    def WaitOne(self, timeout: System.TimeSpan, exitContext: System.Boolean, ) -> System.Boolean:
        ...

    @typing.overload
    @staticmethod
    def WaitAll(waitHandles: list[System.Threading.WaitHandle], millisecondsTimeout: System.Int32, ) -> System.Boolean:
        ...

    @typing.overload
    @staticmethod
    def WaitAll(waitHandles: list[System.Threading.WaitHandle], timeout: System.TimeSpan, ) -> System.Boolean:
        ...

    @typing.overload
    @staticmethod
    def WaitAll(waitHandles: list[System.Threading.WaitHandle], ) -> System.Boolean:
        ...

    @typing.overload
    @staticmethod
    def WaitAll(waitHandles: list[System.Threading.WaitHandle], millisecondsTimeout: System.Int32, exitContext: System.Boolean, ) -> System.Boolean:
        ...

    @typing.overload
    @staticmethod
    def WaitAll(waitHandles: list[System.Threading.WaitHandle], timeout: System.TimeSpan, exitContext: System.Boolean, ) -> System.Boolean:
        ...

    @typing.overload
    @staticmethod
    def WaitAny(waitHandles: list[System.Threading.WaitHandle], millisecondsTimeout: System.Int32, ) -> System.Int32:
        ...

    @typing.overload
    @staticmethod
    def WaitAny(waitHandles: list[System.Threading.WaitHandle], timeout: System.TimeSpan, ) -> System.Int32:
        ...

    @typing.overload
    @staticmethod
    def WaitAny(waitHandles: list[System.Threading.WaitHandle], ) -> System.Int32:
        ...

    @typing.overload
    @staticmethod
    def WaitAny(waitHandles: list[System.Threading.WaitHandle], millisecondsTimeout: System.Int32, exitContext: System.Boolean, ) -> System.Int32:
        ...

    @typing.overload
    @staticmethod
    def WaitAny(waitHandles: list[System.Threading.WaitHandle], timeout: System.TimeSpan, exitContext: System.Boolean, ) -> System.Int32:
        ...

    @typing.overload
    @staticmethod
    def SignalAndWait(toSignal: System.Threading.WaitHandle, toWaitOn: System.Threading.WaitHandle, ) -> System.Boolean:
        ...

    @typing.overload
    @staticmethod
    def SignalAndWait(toSignal: System.Threading.WaitHandle, toWaitOn: System.Threading.WaitHandle, timeout: System.TimeSpan, exitContext: System.Boolean, ) -> System.Boolean:
        ...

    @typing.overload
    @staticmethod
    def SignalAndWait(toSignal: System.Threading.WaitHandle, toWaitOn: System.Threading.WaitHandle, millisecondsTimeout: System.Int32, exitContext: System.Boolean, ) -> System.Boolean:
        ...

class CancellationToken(System.ValueType):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def None_(self) -> System.Threading.CancellationToken:
        ...

    @property
    def IsCancellationRequested(self) -> System.Boolean:
        ...

    @property
    def CanBeCanceled(self) -> System.Boolean:
        ...

    @property
    def WaitHandle(self) -> System.Threading.WaitHandle:
        ...

    # methods
    @typing.overload
    def __init__(self, canceled: System.Boolean, ):
        ...

    @typing.overload
    def Register(self, callback: System.Action, ) -> System.Threading.CancellationTokenRegistration:
        ...

    @typing.overload
    def Register(self, callback: System.Action, useSynchronizationContext: System.Boolean, ) -> System.Threading.CancellationTokenRegistration:
        ...

    @typing.overload
    def Register(self, callback: System.Action[System.Object], state: System.Object, ) -> System.Threading.CancellationTokenRegistration:
        ...

    @typing.overload
    def Register(self, callback: System.Action[System.Object, System.Threading.CancellationToken], state: System.Object, ) -> System.Threading.CancellationTokenRegistration:
        ...

    @typing.overload
    def Register(self, callback: System.Action[System.Object], state: System.Object, useSynchronizationContext: System.Boolean, ) -> System.Threading.CancellationTokenRegistration:
        ...

    @typing.overload
    def UnsafeRegister(self, callback: System.Action[System.Object], state: System.Object, ) -> System.Threading.CancellationTokenRegistration:
        ...

    @typing.overload
    def UnsafeRegister(self, callback: System.Action[System.Object, System.Threading.CancellationToken], state: System.Object, ) -> System.Threading.CancellationTokenRegistration:
        ...

    @typing.overload
    def Equals(self, other: System.Threading.CancellationToken, ) -> System.Boolean:
        ...

    @typing.overload
    def Equals(self, other: System.Object, ) -> System.Boolean:
        ...

    @typing.overload
    def GetHashCode(self, ) -> System.Int32:
        ...

    @typing.overload
    def ThrowIfCancellationRequested(self, ) -> None:
        ...

class CancellationTokenRegistration(System.IEquatable[System.Threading.CancellationTokenRegistration], System.IDisposable, System.IAsyncDisposable, System.ValueType):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def Token(self) -> System.Threading.CancellationToken:
        ...

    # methods
    @typing.overload
    def Dispose(self, ) -> None:
        ...

    @typing.overload
    def DisposeAsync(self, ) -> System.Threading.Tasks.ValueTask:
        ...

    @typing.overload
    def Unregister(self, ) -> System.Boolean:
        ...

    @typing.overload
    def Equals(self, obj: System.Object, ) -> System.Boolean:
        ...

    @typing.overload
    def Equals(self, other: System.Threading.CancellationTokenRegistration, ) -> System.Boolean:
        ...

    @typing.overload
    def GetHashCode(self, ) -> System.Int32:
        ...

