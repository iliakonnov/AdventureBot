from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import System
import System.Runtime.Serialization
import System.Threading
import System.Reflection
import System.Threading.Tasks
import System.Threading.SemaphoreSlim
import System.Runtime.InteropServices
import System.Threading.ReaderWriterLockSlim
import System.Threading.CancellationTokenSource
import Microsoft.Win32.SafeHandles
import System.Runtime.ConstrainedExecution
import System.Globalization
import System.Security.Principal
import System.Collections.Generic
import System.Threading.ThreadLocal

TState = typing.TypeVar('TState')
T = typing.TypeVar('T')

class ExecutionContext(System.IDisposable, System.Runtime.Serialization.ISerializable, System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields
    Default: System.Threading.ExecutionContext = ...

    # properties
    @property
    def HasChangeNotifications(self) -> bool:
        ...

    @property
    def IsDefault(self) -> bool:
        ...

    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def __init__(self, localValues: System.Threading.IAsyncLocalValueMap, localChangeNotifications: System.Array[System.Threading.IAsyncLocal], isFlowSuppressed: bool, ):
        ...

    def GetObjectData(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext, ) -> None:
        ...

    @staticmethod
    def Capture() -> System.Threading.ExecutionContext:
        ...

    @staticmethod
    def CaptureForRestore() -> System.Threading.ExecutionContext:
        ...

    def ShallowClone(self, isFlowSuppressed: bool, ) -> System.Threading.ExecutionContext:
        ...

    @staticmethod
    def SuppressFlow() -> System.Threading.AsyncFlowControl:
        ...

    @staticmethod
    def RestoreFlow() -> None:
        ...

    @staticmethod
    def IsFlowSuppressed() -> bool:
        ...

    @staticmethod
    def Run(executionContext: System.Threading.ExecutionContext, callback: System.Threading.ContextCallback, state: System.Object, ) -> None:
        ...

    @staticmethod
    def RunInternal(executionContext: System.Threading.ExecutionContext, callback: System.Threading.ContextCallback, state: System.Object, ) -> None:
        ...

    @staticmethod
    def Restore(executionContext: System.Threading.ExecutionContext, ) -> None:
        ...

    @staticmethod
    def RestoreInternal(executionContext: System.Threading.ExecutionContext, ) -> None:
        ...

    @staticmethod
    def RunFromThreadPoolDispatchLoop(threadPoolThread: System.Threading.Thread, executionContext: System.Threading.ExecutionContext, callback: System.Threading.ContextCallback, state: System.Object, ) -> None:
        ...

    @staticmethod
    def RunForThreadPoolUnsafe(executionContext: System.Threading.ExecutionContext, callback: System.Action[TState], state: ref[TState], ) -> None:
        ...

    @staticmethod
    def RestoreChangedContextToThread(currentThread: System.Threading.Thread, contextToRestore: System.Threading.ExecutionContext, currentContext: System.Threading.ExecutionContext, ) -> None:
        ...

    @staticmethod
    def ResetThreadPoolThread(currentThread: System.Threading.Thread, ) -> None:
        ...

    @staticmethod
    def OnValuesChanged(previousExecutionCtx: System.Threading.ExecutionContext, nextExecutionCtx: System.Threading.ExecutionContext, ) -> None:
        ...

    @staticmethod
    def ThrowNullContext() -> None:
        ...

    @staticmethod
    def GetLocalValue(local: System.Threading.IAsyncLocal, ) -> System.Object:
        ...

    @staticmethod
    def SetLocalValue(local: System.Threading.IAsyncLocal, newValue: System.Object, needChangeNotifications: bool, ) -> None:
        ...

    def CreateCopy(self, ) -> System.Threading.ExecutionContext:
        ...

    def Dispose(self, ) -> None:
        ...

class AsyncFlowControl(System.IEquatable[System.Threading.AsyncFlowControl], System.IDisposable, System.ValueType):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    def Initialize(self, currentThread: System.Threading.Thread, ) -> None:
        ...

    def Undo(self, ) -> None:
        ...

    def Dispose(self, ) -> None:
        ...

    @typing.overload
    def Equals(self, obj: System.Object, ) -> bool:
        ...

    @typing.overload
    def Equals(self, obj: System.Threading.AsyncFlowControl, ) -> bool:
        ...

    def GetHashCode(self, ) -> int:
        ...

class ContextCallback(System.ICloneable, System.Runtime.Serialization.ISerializable, System.MulticastDelegate):
    @typing.overload
    def __init__(self, **kwargs):
        self._target: System.Object
        self._methodBase: System.Object
        self._methodPtr: System.IntPtr
        self._methodPtrAux: System.IntPtr
        ...

    # static fields

    # properties
    @property
    def Target(self) -> System.Object:
        ...

    @property
    def Method(self) -> System.Reflection.MethodInfo:
        ...

    # methods
    def __init__(self, object: System.Object, method: System.IntPtr, ):
        ...

    def Invoke(self, state: System.Object, ) -> None:
        ...

    def BeginInvoke(self, state: System.Object, callback: System.AsyncCallback, object: System.Object, ) -> System.IAsyncResult:
        ...

    def EndInvoke(self, result: System.IAsyncResult, ) -> None:
        ...

class SemaphoreSlim(System.IDisposable, System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def CurrentCount(self) -> int:
        ...

    @property
    def AvailableWaitHandle(self) -> System.Threading.WaitHandle:
        ...

    # methods
    @typing.overload
    def __init__(self, initialCount: int, ):
        ...

    @typing.overload
    def __init__(self, initialCount: int, maxCount: int, ):
        ...

    @typing.overload
    def Wait(self, ) -> None:
        ...

    @typing.overload
    def Wait(self, cancellationToken: System.Threading.CancellationToken, ) -> None:
        ...

    @typing.overload
    def Wait(self, timeout: System.TimeSpan, ) -> bool:
        ...

    @typing.overload
    def Wait(self, timeout: System.TimeSpan, cancellationToken: System.Threading.CancellationToken, ) -> bool:
        ...

    @typing.overload
    def Wait(self, millisecondsTimeout: int, ) -> bool:
        ...

    @typing.overload
    def Wait(self, millisecondsTimeout: int, cancellationToken: System.Threading.CancellationToken, ) -> bool:
        ...

    def WaitUntilCountOrTimeout(self, millisecondsTimeout: int, startTime: int, cancellationToken: System.Threading.CancellationToken, ) -> bool:
        ...

    @typing.overload
    def WaitAsync(self, ) -> System.Threading.Tasks.Task:
        ...

    @typing.overload
    def WaitAsync(self, cancellationToken: System.Threading.CancellationToken, ) -> System.Threading.Tasks.Task:
        ...

    @typing.overload
    def WaitAsync(self, millisecondsTimeout: int, ) -> System.Threading.Tasks.Task[bool]:
        ...

    @typing.overload
    def WaitAsync(self, timeout: System.TimeSpan, ) -> System.Threading.Tasks.Task[bool]:
        ...

    @typing.overload
    def WaitAsync(self, timeout: System.TimeSpan, cancellationToken: System.Threading.CancellationToken, ) -> System.Threading.Tasks.Task[bool]:
        ...

    @typing.overload
    def WaitAsync(self, millisecondsTimeout: int, cancellationToken: System.Threading.CancellationToken, ) -> System.Threading.Tasks.Task[bool]:
        ...

    def CreateAndAddAsyncWaiter(self, ) -> System.Threading.SemaphoreSlim.TaskNode:
        ...

    def RemoveAsyncWaiter(self, task: System.Threading.SemaphoreSlim.TaskNode, ) -> bool:
        ...

    def WaitUntilCountOrTimeoutAsync(self, asyncWaiter: System.Threading.SemaphoreSlim.TaskNode, millisecondsTimeout: int, cancellationToken: System.Threading.CancellationToken, ) -> System.Threading.Tasks.Task[bool]:
        ...

    @typing.overload
    def Release(self, ) -> int:
        ...

    @typing.overload
    def Release(self, releaseCount: int, ) -> int:
        ...

    @typing.overload
    def Dispose(self, ) -> None:
        ...

    @typing.overload
    def Dispose(self, disposing: bool, ) -> None:
        ...

    @staticmethod
    def CancellationTokenCanceledEventHandler(obj: System.Object, ) -> None:
        ...

    def CheckDispose(self, ) -> None:
        ...

class ThreadPoolBoundHandle(System.IDisposable, System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def Handle(self) -> System.Runtime.InteropServices.SafeHandle:
        ...

    # methods
    def __init__(self, handle: System.Runtime.InteropServices.SafeHandle, ):
        ...

    @staticmethod
    def BindHandle(handle: System.Runtime.InteropServices.SafeHandle, ) -> System.Threading.ThreadPoolBoundHandle:
        ...

    @typing.overload
    def AllocateNativeOverlapped(self, callback: System.Threading.IOCompletionCallback, state: System.Object, pinData: System.Object, ) -> ptr[System.Threading.NativeOverlapped]:
        ...

    @typing.overload
    def AllocateNativeOverlapped(self, callback: System.Threading.IOCompletionCallback, state: System.Object, pinData: System.Object, flowExecutionContext: bool, ) -> ptr[System.Threading.NativeOverlapped]:
        ...

    @typing.overload
    def AllocateNativeOverlapped(self, preAllocated: System.Threading.PreAllocatedOverlapped, ) -> ptr[System.Threading.NativeOverlapped]:
        ...

    def UnsafeAllocateNativeOverlapped(self, callback: System.Threading.IOCompletionCallback, state: System.Object, pinData: System.Object, ) -> ptr[System.Threading.NativeOverlapped]:
        ...

    def FreeNativeOverlapped(self, overlapped: ptr[System.Threading.NativeOverlapped], ) -> None:
        ...

    @staticmethod
    def GetNativeOverlappedState(overlapped: ptr[System.Threading.NativeOverlapped], ) -> System.Object:
        ...

    @staticmethod
    def GetOverlappedWrapper(overlapped: ptr[System.Threading.NativeOverlapped], ) -> System.Threading.ThreadPoolBoundHandleOverlapped:
        ...

    def Dispose(self, ) -> None:
        ...

    def EnsureNotDisposed(self, ) -> None:
        ...

    @staticmethod
    def BindHandleCore(handle: System.Runtime.InteropServices.SafeHandle, ) -> System.Threading.ThreadPoolBoundHandle:
        ...

class IOCompletionCallback(System.ICloneable, System.Runtime.Serialization.ISerializable, System.MulticastDelegate):
    @typing.overload
    def __init__(self, **kwargs):
        self._target: System.Object
        self._methodBase: System.Object
        self._methodPtr: System.IntPtr
        self._methodPtrAux: System.IntPtr
        ...

    # static fields

    # properties
    @property
    def Target(self) -> System.Object:
        ...

    @property
    def Method(self) -> System.Reflection.MethodInfo:
        ...

    # methods
    def __init__(self, object: System.Object, method: System.IntPtr, ):
        ...

    def Invoke(self, errorCode: int, numBytes: int, pOVERLAP: ptr[System.Threading.NativeOverlapped], ) -> None:
        ...

    def BeginInvoke(self, errorCode: int, numBytes: int, pOVERLAP: ptr[System.Threading.NativeOverlapped], callback: System.AsyncCallback, object: System.Object, ) -> System.IAsyncResult:
        ...

    def EndInvoke(self, result: System.IAsyncResult, ) -> None:
        ...

class SynchronizationContext(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def Current(self) -> System.Threading.SynchronizationContext:
        ...

    # methods
    def __init__(self, ):
        ...

    @staticmethod
    def InvokeWaitMethodHelper(syncContext: System.Threading.SynchronizationContext, waitHandles: System.Array[System.IntPtr], waitAll: bool, millisecondsTimeout: int, ) -> int:
        ...

    def SetWaitNotificationRequired(self, ) -> None:
        ...

    def IsWaitNotificationRequired(self, ) -> bool:
        ...

    def Send(self, d: System.Threading.SendOrPostCallback, state: System.Object, ) -> None:
        ...

    def Post(self, d: System.Threading.SendOrPostCallback, state: System.Object, ) -> None:
        ...

    def OperationStarted(self, ) -> None:
        ...

    def OperationCompleted(self, ) -> None:
        ...

    def Wait(self, waitHandles: System.Array[System.IntPtr], waitAll: bool, millisecondsTimeout: int, ) -> int:
        ...

    @staticmethod
    def WaitHelper(waitHandles: System.Array[System.IntPtr], waitAll: bool, millisecondsTimeout: int, ) -> int:
        ...

    @staticmethod
    def SetSynchronizationContext(syncContext: System.Threading.SynchronizationContext, ) -> None:
        ...

    def CreateCopy(self, ) -> System.Threading.SynchronizationContext:
        ...

class SendOrPostCallback(System.ICloneable, System.Runtime.Serialization.ISerializable, System.MulticastDelegate):
    @typing.overload
    def __init__(self, **kwargs):
        self._target: System.Object
        self._methodBase: System.Object
        self._methodPtr: System.IntPtr
        self._methodPtrAux: System.IntPtr
        ...

    # static fields

    # properties
    @property
    def Target(self) -> System.Object:
        ...

    @property
    def Method(self) -> System.Reflection.MethodInfo:
        ...

    # methods
    def __init__(self, object: System.Object, method: System.IntPtr, ):
        ...

    def Invoke(self, state: System.Object, ) -> None:
        ...

    def BeginInvoke(self, state: System.Object, callback: System.AsyncCallback, object: System.Object, ) -> System.IAsyncResult:
        ...

    def EndInvoke(self, result: System.IAsyncResult, ) -> None:
        ...

class LazyThreadSafetyMode(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    None_: int = ...
    PublicationOnly: int = ...
    ExecutionAndPublication: int = ...

class NativeOverlapped(System.ValueType):
    @typing.overload
    def __init__(self, **kwargs):
        self.InternalLow: System.IntPtr
        self.InternalHigh: System.IntPtr
        self.OffsetLow: int
        self.OffsetHigh: int
        self.EventHandle: System.IntPtr
        ...

    # static fields

    # properties
    # methods
class ReaderWriterLockSlim(System.IDisposable, System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def HasNoWaiters(self) -> bool:
        ...
    @HasNoWaiters.setter
    def HasNoWaiters(self, val: bool):
        ...

    @property
    def IsReadLockHeld(self) -> bool:
        ...

    @property
    def IsUpgradeableReadLockHeld(self) -> bool:
        ...

    @property
    def IsWriteLockHeld(self) -> bool:
        ...

    @property
    def RecursionPolicy(self) -> int:
        ...

    @property
    def CurrentReadCount(self) -> int:
        ...

    @property
    def RecursiveReadCount(self) -> int:
        ...

    @property
    def RecursiveUpgradeCount(self) -> int:
        ...

    @property
    def RecursiveWriteCount(self) -> int:
        ...

    @property
    def WaitingReadCount(self) -> int:
        ...

    @property
    def WaitingUpgradeCount(self) -> int:
        ...

    @property
    def WaitingWriteCount(self) -> int:
        ...

    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def __init__(self, recursionPolicy: int, ):
        ...

    def InitializeThreadCounts(self, ) -> None:
        ...

    @staticmethod
    def IsRWEntryEmpty(rwc: System.Threading.ReaderWriterCount, ) -> bool:
        ...

    def IsRwHashEntryChanged(self, lrwc: System.Threading.ReaderWriterCount, ) -> bool:
        ...

    def GetThreadRWCount(self, dontAllocate: bool, ) -> System.Threading.ReaderWriterCount:
        ...

    def EnterReadLock(self, ) -> None:
        ...

    @typing.overload
    def TryEnterReadLock(self, timeout: System.TimeSpan, ) -> bool:
        ...

    @typing.overload
    def TryEnterReadLock(self, millisecondsTimeout: int, ) -> bool:
        ...

    @typing.overload
    def TryEnterReadLock(self, timeout: System.Threading.ReaderWriterLockSlim.TimeoutTracker, ) -> bool:
        ...

    def TryEnterReadLockCore(self, timeout: System.Threading.ReaderWriterLockSlim.TimeoutTracker, ) -> bool:
        ...

    def EnterWriteLock(self, ) -> None:
        ...

    @typing.overload
    def TryEnterWriteLock(self, timeout: System.TimeSpan, ) -> bool:
        ...

    @typing.overload
    def TryEnterWriteLock(self, millisecondsTimeout: int, ) -> bool:
        ...

    @typing.overload
    def TryEnterWriteLock(self, timeout: System.Threading.ReaderWriterLockSlim.TimeoutTracker, ) -> bool:
        ...

    def TryEnterWriteLockCore(self, timeout: System.Threading.ReaderWriterLockSlim.TimeoutTracker, ) -> bool:
        ...

    def EnterUpgradeableReadLock(self, ) -> None:
        ...

    @typing.overload
    def TryEnterUpgradeableReadLock(self, timeout: System.TimeSpan, ) -> bool:
        ...

    @typing.overload
    def TryEnterUpgradeableReadLock(self, millisecondsTimeout: int, ) -> bool:
        ...

    @typing.overload
    def TryEnterUpgradeableReadLock(self, timeout: System.Threading.ReaderWriterLockSlim.TimeoutTracker, ) -> bool:
        ...

    def TryEnterUpgradeableReadLockCore(self, timeout: System.Threading.ReaderWriterLockSlim.TimeoutTracker, ) -> bool:
        ...

    def ExitReadLock(self, ) -> None:
        ...

    def ExitWriteLock(self, ) -> None:
        ...

    def ExitUpgradeableReadLock(self, ) -> None:
        ...

    def LazyCreateEvent(self, waitEvent: ref[System.Threading.EventWaitHandle], enterLockType: int, ) -> None:
        ...

    def WaitOnEvent(self, waitEvent: System.Threading.EventWaitHandle, numWaiters: ref[int], timeout: System.Threading.ReaderWriterLockSlim.TimeoutTracker, enterLockType: int, ) -> bool:
        ...

    def ExitAndWakeUpAppropriateWaiters(self, ) -> None:
        ...

    def ExitAndWakeUpAppropriateWaitersPreferringWriters(self, ) -> None:
        ...

    def ExitAndWakeUpAppropriateReadWaiters(self, ) -> None:
        ...

    def IsWriterAcquired(self, ) -> bool:
        ...

    def SetWriterAcquired(self, ) -> None:
        ...

    def ClearWriterAcquired(self, ) -> None:
        ...

    def SetWritersWaiting(self, ) -> None:
        ...

    def ClearWritersWaiting(self, ) -> None:
        ...

    def SetUpgraderWaiting(self, ) -> None:
        ...

    def ClearUpgraderWaiting(self, ) -> None:
        ...

    def GetNumReaders(self, ) -> int:
        ...

    def ShouldSpinForEnterAnyRead(self, ) -> bool:
        ...

    def ShouldSpinForEnterAnyWrite(self, isUpgradeToWrite: bool, ) -> bool:
        ...

    @staticmethod
    def SpinWait(spinCount: int, ) -> None:
        ...

    @typing.overload
    def Dispose(self, ) -> None:
        ...

    @typing.overload
    def Dispose(self, disposing: bool, ) -> None:
        ...

class LockRecursionPolicy(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    NoRecursion: int = ...
    SupportsRecursion: int = ...

class CancellationToken(System.ValueType):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def None_(self) -> System.Threading.CancellationToken:
        ...

    @property
    def IsCancellationRequested(self) -> bool:
        ...

    @property
    def CanBeCanceled(self) -> bool:
        ...

    @property
    def WaitHandle(self) -> System.Threading.WaitHandle:
        ...

    # methods
    @typing.overload
    def __init__(self, source: System.Threading.CancellationTokenSource, ):
        ...

    @typing.overload
    def __init__(self, canceled: bool, ):
        ...

    @typing.overload
    def Register(self, callback: System.Action, ) -> System.Threading.CancellationTokenRegistration:
        ...

    @typing.overload
    def Register(self, callback: System.Action, useSynchronizationContext: bool, ) -> System.Threading.CancellationTokenRegistration:
        ...

    @typing.overload
    def Register(self, callback: System.Action[System.Object], state: System.Object, ) -> System.Threading.CancellationTokenRegistration:
        ...

    @typing.overload
    def Register(self, callback: System.Action[System.Object, System.Threading.CancellationToken], state: System.Object, ) -> System.Threading.CancellationTokenRegistration:
        ...

    @typing.overload
    def Register(self, callback: System.Action[System.Object], state: System.Object, useSynchronizationContext: bool, ) -> System.Threading.CancellationTokenRegistration:
        ...

    @typing.overload
    def Register(self, callback: System.Delegate, state: System.Object, useSynchronizationContext: bool, useExecutionContext: bool, ) -> System.Threading.CancellationTokenRegistration:
        ...

    @typing.overload
    def UnsafeRegister(self, callback: System.Action[System.Object], state: System.Object, ) -> System.Threading.CancellationTokenRegistration:
        ...

    @typing.overload
    def UnsafeRegister(self, callback: System.Action[System.Object, System.Threading.CancellationToken], state: System.Object, ) -> System.Threading.CancellationTokenRegistration:
        ...

    @typing.overload
    def Equals(self, other: System.Threading.CancellationToken, ) -> bool:
        ...

    @typing.overload
    def Equals(self, other: System.Object, ) -> bool:
        ...

    def GetHashCode(self, ) -> int:
        ...

    def ThrowIfCancellationRequested(self, ) -> None:
        ...

    def ThrowOperationCanceledException(self, ) -> None:
        ...

class IThreadPoolWorkItem(abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    @abc.abstractmethod
    def Execute(self, ) -> None:
        ...

class AsyncLocal(System.Threading.IAsyncLocal, System.Object, typing.Generic[T]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def Value(self) -> T:
        ...
    @Value.setter
    def Value(self, val: T):
        ...

    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def __init__(self, valueChangedHandler: System.Action[System.Threading.AsyncLocalValueChangedArgs[T]], ):
        ...

    def OnValueChanged(self, previousValueObj: System.Object, currentValueObj: System.Object, contextChanged: bool, ) -> None:
        ...

class PreAllocatedOverlapped(System.IDisposable, System.Threading.IDeferredDisposable, System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        self._overlapped: System.Threading.ThreadPoolBoundHandleOverlapped
        ...

    # static fields

    # properties
    # methods
    @typing.overload
    def __init__(self, callback: System.Threading.IOCompletionCallback, state: System.Object, pinData: System.Object, ):
        ...

    @typing.overload
    def __init__(self, callback: System.Threading.IOCompletionCallback, state: System.Object, pinData: System.Object, flowExecutionContext: bool, ):
        ...

    @staticmethod
    def UnsafeCreate(callback: System.Threading.IOCompletionCallback, state: System.Object, pinData: System.Object, ) -> System.Threading.PreAllocatedOverlapped:
        ...

    def AddRef(self, ) -> bool:
        ...

    def Release(self, ) -> None:
        ...

    def Dispose(self, ) -> None:
        ...

    def Finalize(self, ) -> None:
        ...

    def OnFinalRelease(self, disposed: bool, ) -> None:
        ...

class CancellationTokenRegistration(System.IEquatable[System.Threading.CancellationTokenRegistration], System.IDisposable, System.IAsyncDisposable, System.ValueType):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def Token(self) -> System.Threading.CancellationToken:
        ...

    # methods
    def __init__(self, id: int, node: System.Threading.CancellationTokenSource.CallbackNode, ):
        ...

    def Dispose(self, ) -> None:
        ...

    def DisposeAsync(self, ) -> System.Threading.Tasks.ValueTask:
        ...

    def Unregister(self, ) -> bool:
        ...

    @typing.overload
    def Equals(self, obj: System.Object, ) -> bool:
        ...

    @typing.overload
    def Equals(self, other: System.Threading.CancellationTokenRegistration, ) -> bool:
        ...

    def GetHashCode(self, ) -> int:
        ...

class CancellationTokenSource(System.IDisposable, System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields
    s_canceledSource: System.Threading.CancellationTokenSource = ...
    s_neverCanceledSource: System.Threading.CancellationTokenSource = ...

    # properties
    @property
    def IsCancellationRequested(self) -> bool:
        ...

    @property
    def IsCancellationCompleted(self) -> bool:
        ...

    @property
    def Token(self) -> System.Threading.CancellationToken:
        ...

    @property
    def WaitHandle(self) -> System.Threading.WaitHandle:
        ...

    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def __init__(self, delay: System.TimeSpan, ):
        ...

    @typing.overload
    def __init__(self, millisecondsDelay: int, ):
        ...

    @staticmethod
    def TimerCallback(state: System.Object, ) -> None:
        ...

    def InitializeWithTimer(self, millisecondsDelay: int, ) -> None:
        ...

    @typing.overload
    def Cancel(self, ) -> None:
        ...

    @typing.overload
    def Cancel(self, throwOnFirstException: bool, ) -> None:
        ...

    @typing.overload
    def CancelAfter(self, delay: System.TimeSpan, ) -> None:
        ...

    @typing.overload
    def CancelAfter(self, millisecondsDelay: int, ) -> None:
        ...

    @typing.overload
    def CancelAfter(self, millisecondsDelay: int, ) -> None:
        ...

    def TryReset(self, ) -> bool:
        ...

    @typing.overload
    def Dispose(self, ) -> None:
        ...

    @typing.overload
    def Dispose(self, disposing: bool, ) -> None:
        ...

    def ThrowIfDisposed(self, ) -> None:
        ...

    def Register(self, callback: System.Delegate, stateForCallback: System.Object, syncContext: System.Threading.SynchronizationContext, executionContext: System.Threading.ExecutionContext, ) -> System.Threading.CancellationTokenRegistration:
        ...

    def NotifyCancellation(self, throwOnFirstException: bool, ) -> None:
        ...

    def ExecuteCallbackHandlers(self, throwOnFirstException: bool, ) -> None:
        ...

    @staticmethod
    @typing.overload
    def CreateLinkedTokenSource(token1: System.Threading.CancellationToken, token2: System.Threading.CancellationToken, ) -> System.Threading.CancellationTokenSource:
        ...

    @staticmethod
    @typing.overload
    def CreateLinkedTokenSource(token: System.Threading.CancellationToken, ) -> System.Threading.CancellationTokenSource:
        ...

    @staticmethod
    @typing.overload
    def CreateLinkedTokenSource(tokens: System.Array[System.Threading.CancellationToken], ) -> System.Threading.CancellationTokenSource:
        ...

    @staticmethod
    def Invoke(d: System.Delegate, state: System.Object, source: System.Threading.CancellationTokenSource, ) -> None:
        ...

class EventWaitHandle(System.IDisposable, System.Threading.WaitHandle):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

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
    def __init__(self, initialState: bool, mode: int, ):
        ...

    @typing.overload
    def __init__(self, initialState: bool, mode: int, name: str, ):
        ...

    @typing.overload
    def __init__(self, initialState: bool, mode: int, name: str, createdNew: ref[bool], ):
        ...

    @staticmethod
    def OpenExisting(name: str, ) -> System.Threading.EventWaitHandle:
        ...

    @staticmethod
    def TryOpenExisting(name: str, result: ref[System.Threading.EventWaitHandle], ) -> bool:
        ...

    def CreateEventCore(self, initialState: bool, mode: int, name: str, createdNew: ref[bool], ) -> None:
        ...

    @staticmethod
    def OpenExistingWorker(name: str, result: ref[System.Threading.EventWaitHandle], ) -> int:
        ...

    def Reset(self, ) -> bool:
        ...

    @typing.overload
    def Set(self, ) -> bool:
        ...

    @staticmethod
    @typing.overload
    def Set(waitHandle: Microsoft.Win32.SafeHandles.SafeWaitHandle, ) -> bool:
        ...

class EventResetMode(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    AutoReset: int = ...
    ManualReset: int = ...

class ManualResetEventSlim(System.IDisposable, System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def WaitHandle(self) -> System.Threading.WaitHandle:
        ...

    @property
    def IsSet(self) -> bool:
        ...
    @IsSet.setter
    def IsSet(self, val: bool):
        ...

    @property
    def SpinCount(self) -> int:
        ...
    @SpinCount.setter
    def SpinCount(self, val: int):
        ...

    @property
    def Waiters(self) -> int:
        ...
    @Waiters.setter
    def Waiters(self, val: int):
        ...

    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def __init__(self, initialState: bool, ):
        ...

    @typing.overload
    def __init__(self, initialState: bool, spinCount: int, ):
        ...

    def Initialize(self, initialState: bool, spinCount: int, ) -> None:
        ...

    def EnsureLockObjectCreated(self, ) -> None:
        ...

    def LazyInitializeEvent(self, ) -> None:
        ...

    @typing.overload
    def Set(self, ) -> None:
        ...

    @typing.overload
    def Set(self, duringCancellation: bool, ) -> None:
        ...

    def Reset(self, ) -> None:
        ...

    @typing.overload
    def Wait(self, ) -> None:
        ...

    @typing.overload
    def Wait(self, cancellationToken: System.Threading.CancellationToken, ) -> None:
        ...

    @typing.overload
    def Wait(self, timeout: System.TimeSpan, ) -> bool:
        ...

    @typing.overload
    def Wait(self, timeout: System.TimeSpan, cancellationToken: System.Threading.CancellationToken, ) -> bool:
        ...

    @typing.overload
    def Wait(self, millisecondsTimeout: int, ) -> bool:
        ...

    @typing.overload
    def Wait(self, millisecondsTimeout: int, cancellationToken: System.Threading.CancellationToken, ) -> bool:
        ...

    @typing.overload
    def Dispose(self, ) -> None:
        ...

    @typing.overload
    def Dispose(self, disposing: bool, ) -> None:
        ...

    def ThrowIfDisposed(self, ) -> None:
        ...

    @staticmethod
    def CancellationTokenCallback(obj: System.Object, ) -> None:
        ...

    def UpdateStateAtomically(self, newBits: int, updateBitsMask: int, ) -> None:
        ...

    @staticmethod
    def ExtractStatePortionAndShiftRight(state: int, mask: int, rightBitShiftCount: int, ) -> int:
        ...

    @staticmethod
    def ExtractStatePortion(state: int, mask: int, ) -> int:
        ...

class Thread(System.Runtime.ConstrainedExecution.CriticalFinalizerObject):
    @typing.overload
    def __init__(self, **kwargs):
        self._executionContext: System.Threading.ExecutionContext
        self._synchronizationContext: System.Threading.SynchronizationContext
        ...

    # static fields

    # properties
    @property
    def ManagedThreadId(self) -> int:
        ...

    @property
    def IsAlive(self) -> bool:
        ...

    @property
    def IsBackground(self) -> bool:
        ...
    @IsBackground.setter
    def IsBackground(self, val: bool):
        ...

    @property
    def IsThreadPoolThread(self) -> bool:
        ...
    @IsThreadPoolThread.setter
    def IsThreadPoolThread(self, val: bool):
        ...

    @property
    def Priority(self) -> int:
        ...
    @Priority.setter
    def Priority(self, val: int):
        ...

    @property
    def ThreadState(self) -> int:
        ...

    @property
    def OptimalMaxSpinWaitsPerSpinIteration(self) -> int:
        ...

    @property
    def IsThreadStartSupported(self) -> bool:
        ...

    @property
    def CurrentCulture(self) -> System.Globalization.CultureInfo:
        ...
    @CurrentCulture.setter
    def CurrentCulture(self, val: System.Globalization.CultureInfo):
        ...

    @property
    def CurrentUICulture(self) -> System.Globalization.CultureInfo:
        ...
    @CurrentUICulture.setter
    def CurrentUICulture(self, val: System.Globalization.CultureInfo):
        ...

    @property
    def CurrentPrincipal(self) -> System.Security.Principal.IPrincipal:
        ...
    @CurrentPrincipal.setter
    def CurrentPrincipal(self, val: System.Security.Principal.IPrincipal):
        ...

    @property
    def CurrentThread(self) -> System.Threading.Thread:
        ...

    @property
    def CurrentOSThreadId(self) -> int:
        ...

    @property
    def ExecutionContext(self) -> System.Threading.ExecutionContext:
        ...

    @property
    def Name(self) -> str:
        ...
    @Name.setter
    def Name(self, val: str):
        ...

    @property
    def ApartmentState(self) -> int:
        ...
    @ApartmentState.setter
    def ApartmentState(self, val: int):
        ...

    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def __init__(self, start: System.Threading.ThreadStart, ):
        ...

    @typing.overload
    def __init__(self, start: System.Threading.ThreadStart, maxStackSize: int, ):
        ...

    @typing.overload
    def __init__(self, start: System.Threading.ParameterizedThreadStart, ):
        ...

    @typing.overload
    def __init__(self, start: System.Threading.ParameterizedThreadStart, maxStackSize: int, ):
        ...

    @staticmethod
    def BeginCriticalRegion() -> None:
        ...

    @staticmethod
    def EndCriticalRegion() -> None:
        ...

    @staticmethod
    def BeginThreadAffinity() -> None:
        ...

    @staticmethod
    def EndThreadAffinity() -> None:
        ...

    @staticmethod
    def AllocateDataSlot() -> System.LocalDataStoreSlot:
        ...

    @staticmethod
    def AllocateNamedDataSlot(name: str, ) -> System.LocalDataStoreSlot:
        ...

    @staticmethod
    def GetNamedDataSlot(name: str, ) -> System.LocalDataStoreSlot:
        ...

    @staticmethod
    def FreeNamedDataSlot(name: str, ) -> None:
        ...

    @staticmethod
    def GetData(slot: System.LocalDataStoreSlot, ) -> System.Object:
        ...

    @staticmethod
    def SetData(slot: System.LocalDataStoreSlot, data: System.Object, ) -> None:
        ...

    @typing.overload
    def SetApartmentState(self, state: int, ) -> None:
        ...

    @typing.overload
    def SetApartmentState(self, state: int, throwOnError: bool, ) -> bool:
        ...

    def TrySetApartmentState(self, state: int, ) -> bool:
        ...

    def GetCompressedStack(self, ) -> System.Threading.CompressedStack:
        ...

    def SetCompressedStack(self, stack: System.Threading.CompressedStack, ) -> None:
        ...

    @staticmethod
    def GetDomain() -> System.AppDomain:
        ...

    @staticmethod
    def GetDomainID() -> int:
        ...

    def GetHashCode(self, ) -> int:
        ...

    @typing.overload
    def Join(self, ) -> None:
        ...

    @typing.overload
    def Join(self, timeout: System.TimeSpan, ) -> bool:
        ...

    @typing.overload
    def Join(self, millisecondsTimeout: int, ) -> bool:
        ...

    @staticmethod
    def MemoryBarrier() -> None:
        ...

    @staticmethod
    @typing.overload
    def Sleep(timeout: System.TimeSpan, ) -> None:
        ...

    @staticmethod
    @typing.overload
    def Sleep(millisecondsTimeout: int, ) -> None:
        ...

    @staticmethod
    @typing.overload
    def VolatileRead(address: ref[int], ) -> int:
        ...

    @staticmethod
    @typing.overload
    def VolatileRead(address: ref[float], ) -> float:
        ...

    @staticmethod
    @typing.overload
    def VolatileRead(address: ref[int], ) -> int:
        ...

    @staticmethod
    @typing.overload
    def VolatileRead(address: ref[int], ) -> int:
        ...

    @staticmethod
    @typing.overload
    def VolatileRead(address: ref[int], ) -> int:
        ...

    @staticmethod
    @typing.overload
    def VolatileRead(address: ref[System.IntPtr], ) -> System.IntPtr:
        ...

    @staticmethod
    @typing.overload
    def VolatileRead(address: ref[System.Object], ) -> System.Object:
        ...

    @staticmethod
    @typing.overload
    def VolatileRead(address: ref[int], ) -> int:
        ...

    @staticmethod
    @typing.overload
    def VolatileRead(address: ref[float], ) -> float:
        ...

    @staticmethod
    @typing.overload
    def VolatileRead(address: ref[int], ) -> int:
        ...

    @staticmethod
    @typing.overload
    def VolatileRead(address: ref[int], ) -> int:
        ...

    @staticmethod
    @typing.overload
    def VolatileRead(address: ref[int], ) -> int:
        ...

    @staticmethod
    @typing.overload
    def VolatileRead(address: ref[System.UIntPtr], ) -> System.UIntPtr:
        ...

    @staticmethod
    @typing.overload
    def VolatileWrite(address: ref[int], value: int, ) -> None:
        ...

    @staticmethod
    @typing.overload
    def VolatileWrite(address: ref[float], value: float, ) -> None:
        ...

    @staticmethod
    @typing.overload
    def VolatileWrite(address: ref[int], value: int, ) -> None:
        ...

    @staticmethod
    @typing.overload
    def VolatileWrite(address: ref[int], value: int, ) -> None:
        ...

    @staticmethod
    @typing.overload
    def VolatileWrite(address: ref[int], value: int, ) -> None:
        ...

    @staticmethod
    @typing.overload
    def VolatileWrite(address: ref[System.IntPtr], value: System.IntPtr, ) -> None:
        ...

    @staticmethod
    @typing.overload
    def VolatileWrite(address: ref[System.Object], value: System.Object, ) -> None:
        ...

    @staticmethod
    @typing.overload
    def VolatileWrite(address: ref[int], value: int, ) -> None:
        ...

    @staticmethod
    @typing.overload
    def VolatileWrite(address: ref[float], value: float, ) -> None:
        ...

    @staticmethod
    @typing.overload
    def VolatileWrite(address: ref[int], value: int, ) -> None:
        ...

    @staticmethod
    @typing.overload
    def VolatileWrite(address: ref[int], value: int, ) -> None:
        ...

    @staticmethod
    @typing.overload
    def VolatileWrite(address: ref[int], value: int, ) -> None:
        ...

    @staticmethod
    @typing.overload
    def VolatileWrite(address: ref[System.UIntPtr], value: System.UIntPtr, ) -> None:
        ...

    def GetNativeHandle(self, ) -> System.Threading.ThreadHandle:
        ...

    def StartCore(self, ) -> None:
        ...

    @staticmethod
    def StartInternal(t: System.Threading.ThreadHandle, stackSize: int, priority: int, pThreadName: ptr[str], ) -> None:
        ...

    def StartCallback(self, ) -> None:
        ...

    @staticmethod
    def InternalGetCurrentThread() -> System.IntPtr:
        ...

    @staticmethod
    def SleepInternal(millisecondsTimeout: int, ) -> None:
        ...

    @staticmethod
    def UninterruptibleSleep0() -> None:
        ...

    @staticmethod
    def SpinWaitInternal(iterations: int, ) -> None:
        ...

    @staticmethod
    def SpinWait(iterations: int, ) -> None:
        ...

    @staticmethod
    def YieldInternal() -> int:
        ...

    @staticmethod
    def Yield() -> bool:
        ...

    @staticmethod
    def InitializeCurrentThread() -> System.Threading.Thread:
        ...

    @staticmethod
    def GetCurrentThreadNative() -> System.Threading.Thread:
        ...

    def Initialize(self, ) -> None:
        ...

    def Finalize(self, ) -> None:
        ...

    def InternalFinalize(self, ) -> None:
        ...

    @staticmethod
    def InformThreadNameChange(t: System.Threading.ThreadHandle, name: str, len: int, ) -> None:
        ...

    def IsBackgroundNative(self, ) -> bool:
        ...

    def SetBackgroundNative(self, isBackground: bool, ) -> None:
        ...

    def GetPriorityNative(self, ) -> int:
        ...

    def SetPriorityNative(self, priority: int, ) -> None:
        ...

    @staticmethod
    def GetCurrentOSThreadId() -> int:
        ...

    def GetThreadStateNative(self, ) -> int:
        ...

    def GetApartmentState(self, ) -> int:
        ...

    @staticmethod
    def SetApartmentStateUnchecked(state: int, throwOnError: bool, ) -> bool:
        ...

    def DisableComObjectEagerCleanup(self, ) -> None:
        ...

    def Interrupt(self, ) -> None:
        ...

    @staticmethod
    def GetCurrentProcessorNumber() -> int:
        ...

    @staticmethod
    def GetCurrentProcessorId() -> int:
        ...

    def ResetThreadPoolThread(self, ) -> None:
        ...

    @typing.overload
    def Start(self, parameter: System.Object, ) -> None:
        ...

    @typing.overload
    def Start(self, parameter: System.Object, captureContext: bool, ) -> None:
        ...

    @typing.overload
    def Start(self, ) -> None:
        ...

    @typing.overload
    def Start(self, captureContext: bool, ) -> None:
        ...

    @typing.overload
    def UnsafeStart(self, parameter: System.Object, ) -> None:
        ...

    @typing.overload
    def UnsafeStart(self, ) -> None:
        ...

    def RequireCurrentThread(self, ) -> None:
        ...

    def SetCultureOnUnstartedThread(self, value: System.Globalization.CultureInfo, uiCulture: bool, ) -> None:
        ...

    def ThreadNameChanged(self, value: str, ) -> None:
        ...

    def SetThreadPoolWorkerThreadName(self, ) -> None:
        ...

    def ResetThreadPoolThreadSlow(self, ) -> None:
        ...

    @typing.overload
    def Abort(self, ) -> None:
        ...

    @typing.overload
    def Abort(self, stateInfo: System.Object, ) -> None:
        ...

    @staticmethod
    def ResetAbort() -> None:
        ...

    def Suspend(self, ) -> None:
        ...

    def Resume(self, ) -> None:
        ...

class ApartmentState(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    STA: int = ...
    MTA: int = ...
    Unknown: int = ...

class CompressedStack(System.Runtime.Serialization.ISerializable, System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    def __init__(self, ):
        ...

    def GetObjectData(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext, ) -> None:
        ...

    @staticmethod
    def Capture() -> System.Threading.CompressedStack:
        ...

    def CreateCopy(self, ) -> System.Threading.CompressedStack:
        ...

    @staticmethod
    def GetCompressedStack() -> System.Threading.CompressedStack:
        ...

    @staticmethod
    def Run(compressedStack: System.Threading.CompressedStack, callback: System.Threading.ContextCallback, state: System.Object, ) -> None:
        ...

class ThreadStart(System.ICloneable, System.Runtime.Serialization.ISerializable, System.MulticastDelegate):
    @typing.overload
    def __init__(self, **kwargs):
        self._target: System.Object
        self._methodBase: System.Object
        self._methodPtr: System.IntPtr
        self._methodPtrAux: System.IntPtr
        ...

    # static fields

    # properties
    @property
    def Target(self) -> System.Object:
        ...

    @property
    def Method(self) -> System.Reflection.MethodInfo:
        ...

    # methods
    def __init__(self, object: System.Object, method: System.IntPtr, ):
        ...

    def Invoke(self, ) -> None:
        ...

    def BeginInvoke(self, callback: System.AsyncCallback, object: System.Object, ) -> System.IAsyncResult:
        ...

    def EndInvoke(self, result: System.IAsyncResult, ) -> None:
        ...

class ThreadPriority(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    Lowest: int = ...
    BelowNormal: int = ...
    Normal: int = ...
    AboveNormal: int = ...
    Highest: int = ...

class ParameterizedThreadStart(System.ICloneable, System.Runtime.Serialization.ISerializable, System.MulticastDelegate):
    @typing.overload
    def __init__(self, **kwargs):
        self._target: System.Object
        self._methodBase: System.Object
        self._methodPtr: System.IntPtr
        self._methodPtrAux: System.IntPtr
        ...

    # static fields

    # properties
    @property
    def Target(self) -> System.Object:
        ...

    @property
    def Method(self) -> System.Reflection.MethodInfo:
        ...

    # methods
    def __init__(self, object: System.Object, method: System.IntPtr, ):
        ...

    def Invoke(self, obj: System.Object, ) -> None:
        ...

    def BeginInvoke(self, obj: System.Object, callback: System.AsyncCallback, object: System.Object, ) -> System.IAsyncResult:
        ...

    def EndInvoke(self, result: System.IAsyncResult, ) -> None:
        ...

class ThreadLocal(System.IDisposable, System.Object, typing.Generic[T]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def Value(self) -> T:
        ...
    @Value.setter
    def Value(self, val: T):
        ...

    @property
    def Values(self) -> System.Collections.Generic.IList[T]:
        ...

    @property
    def ValuesCountForDebugDisplay(self) -> int:
        ...

    @property
    def IsValueCreated(self) -> bool:
        ...

    @property
    def ValueForDebugDisplay(self) -> T:
        ...

    @property
    def ValuesForDebugDisplay(self) -> System.Collections.Generic.List[T]:
        ...

    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def __init__(self, trackAllValues: bool, ):
        ...

    @typing.overload
    def __init__(self, valueFactory: System.Func[T], ):
        ...

    @typing.overload
    def __init__(self, valueFactory: System.Func[T], trackAllValues: bool, ):
        ...

    def Initialize(self, valueFactory: System.Func[T], trackAllValues: bool, ) -> None:
        ...

    def Finalize(self, ) -> None:
        ...

    @typing.overload
    def Dispose(self, ) -> None:
        ...

    @typing.overload
    def Dispose(self, disposing: bool, ) -> None:
        ...

    def ToString(self, ) -> str:
        ...

    def GetValueSlow(self, ) -> T:
        ...

    def SetValueSlow(self, value: T, slotArray: System.Array[System.Threading.ThreadLocal.LinkedSlotVolatile[T]], ) -> None:
        ...

    def CreateLinkedSlot(self, slotArray: System.Array[System.Threading.ThreadLocal.LinkedSlotVolatile[T]], id: int, value: T, ) -> None:
        ...

    def GetValuesAsList(self, ) -> System.Collections.Generic.List[T]:
        ...

    @staticmethod
    def GrowTable(table: ref[System.Array[System.Threading.ThreadLocal.LinkedSlotVolatile[T]]], minLength: int, ) -> None:
        ...

    @staticmethod
    def GetNewTableSize(minSize: int, ) -> int:
        ...

class ThreadState(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    Running: int = ...
    StopRequested: int = ...
    SuspendRequested: int = ...
    Background: int = ...
    Unstarted: int = ...
    Stopped: int = ...
    WaitSleepJoin: int = ...
    Suspended: int = ...
    AbortRequested: int = ...
    Aborted: int = ...

class AsyncLocalValueChangedArgs(System.ValueType, typing.Generic[T]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def PreviousValue(self) -> T:
        ...

    @property
    def CurrentValue(self) -> T:
        ...

    @property
    def ThreadContextChanged(self) -> bool:
        ...

    # methods
    def __init__(self, previousValue: T, currentValue: T, contextChanged: bool, ):
        ...

class WaitHandle(System.IDisposable, System.MarshalByRefObject, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields
    InvalidHandle: System.IntPtr = ...
    MaxWaitHandles: int = ...
    WaitSuccess: int = ...
    WaitAbandoned: int = ...
    WaitTimeout: int = ...

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
    def __init__(self, ):
        ...

    @staticmethod
    def WaitOneCore(waitHandle: System.IntPtr, millisecondsTimeout: int, ) -> int:
        ...

    @staticmethod
    @typing.overload
    def WaitMultipleIgnoringSyncContext(waitHandles: System.Span[System.IntPtr], waitAll: bool, millisecondsTimeout: int, ) -> int:
        ...

    @staticmethod
    @typing.overload
    def WaitMultipleIgnoringSyncContext(waitHandles: ptr[System.IntPtr], numHandles: int, waitAll: bool, millisecondsTimeout: int, ) -> int:
        ...

    @staticmethod
    def SignalAndWaitCore(waitHandleToSignal: System.IntPtr, waitHandleToWaitOn: System.IntPtr, millisecondsTimeout: int, ) -> int:
        ...

    @staticmethod
    def SignalAndWaitNative(waitHandleToSignal: System.IntPtr, waitHandleToWaitOn: System.IntPtr, millisecondsTimeout: int, ) -> int:
        ...

    @staticmethod
    def ToTimeoutMilliseconds(timeout: System.TimeSpan, ) -> int:
        ...

    def Close(self, ) -> None:
        ...

    @typing.overload
    def Dispose(self, explicitDisposing: bool, ) -> None:
        ...

    @typing.overload
    def Dispose(self, ) -> None:
        ...

    @typing.overload
    def WaitOne(self, millisecondsTimeout: int, ) -> bool:
        ...

    @typing.overload
    def WaitOne(self, timeout: System.TimeSpan, ) -> bool:
        ...

    @typing.overload
    def WaitOne(self, ) -> bool:
        ...

    @typing.overload
    def WaitOne(self, millisecondsTimeout: int, exitContext: bool, ) -> bool:
        ...

    @typing.overload
    def WaitOne(self, timeout: System.TimeSpan, exitContext: bool, ) -> bool:
        ...

    def WaitOneNoCheck(self, millisecondsTimeout: int, ) -> bool:
        ...

    @staticmethod
    def RentSafeWaitHandleArray(capacity: int, ) -> System.Array[Microsoft.Win32.SafeHandles.SafeWaitHandle]:
        ...

    @staticmethod
    def ReturnSafeWaitHandleArray(safeWaitHandles: System.Array[Microsoft.Win32.SafeHandles.SafeWaitHandle], ) -> None:
        ...

    @staticmethod
    def ObtainSafeWaitHandles(waitHandles: System.ReadOnlySpan[System.Threading.WaitHandle], safeWaitHandles: System.Span[Microsoft.Win32.SafeHandles.SafeWaitHandle], unsafeWaitHandles: System.Span[System.IntPtr], ) -> None:
        ...

    @staticmethod
    @typing.overload
    def WaitMultiple(waitHandles: System.Array[System.Threading.WaitHandle], waitAll: bool, millisecondsTimeout: int, ) -> int:
        ...

    @staticmethod
    @typing.overload
    def WaitMultiple(waitHandles: System.ReadOnlySpan[System.Threading.WaitHandle], waitAll: bool, millisecondsTimeout: int, ) -> int:
        ...

    @staticmethod
    def WaitAnyMultiple(safeWaitHandles: System.ReadOnlySpan[Microsoft.Win32.SafeHandles.SafeWaitHandle], millisecondsTimeout: int, ) -> int:
        ...

    @staticmethod
    @typing.overload
    def SignalAndWait(toSignal: System.Threading.WaitHandle, toWaitOn: System.Threading.WaitHandle, millisecondsTimeout: int, ) -> bool:
        ...

    @staticmethod
    @typing.overload
    def SignalAndWait(toSignal: System.Threading.WaitHandle, toWaitOn: System.Threading.WaitHandle, ) -> bool:
        ...

    @staticmethod
    @typing.overload
    def SignalAndWait(toSignal: System.Threading.WaitHandle, toWaitOn: System.Threading.WaitHandle, timeout: System.TimeSpan, exitContext: bool, ) -> bool:
        ...

    @staticmethod
    @typing.overload
    def SignalAndWait(toSignal: System.Threading.WaitHandle, toWaitOn: System.Threading.WaitHandle, millisecondsTimeout: int, exitContext: bool, ) -> bool:
        ...

    @staticmethod
    @typing.overload
    def WaitAll(waitHandles: System.Array[System.Threading.WaitHandle], millisecondsTimeout: int, ) -> bool:
        ...

    @staticmethod
    @typing.overload
    def WaitAll(waitHandles: System.Array[System.Threading.WaitHandle], timeout: System.TimeSpan, ) -> bool:
        ...

    @staticmethod
    @typing.overload
    def WaitAll(waitHandles: System.Array[System.Threading.WaitHandle], ) -> bool:
        ...

    @staticmethod
    @typing.overload
    def WaitAll(waitHandles: System.Array[System.Threading.WaitHandle], millisecondsTimeout: int, exitContext: bool, ) -> bool:
        ...

    @staticmethod
    @typing.overload
    def WaitAll(waitHandles: System.Array[System.Threading.WaitHandle], timeout: System.TimeSpan, exitContext: bool, ) -> bool:
        ...

    @staticmethod
    @typing.overload
    def WaitAny(waitHandles: System.Array[System.Threading.WaitHandle], millisecondsTimeout: int, ) -> int:
        ...

    @staticmethod
    @typing.overload
    def WaitAny(safeWaitHandles: System.ReadOnlySpan[Microsoft.Win32.SafeHandles.SafeWaitHandle], millisecondsTimeout: int, ) -> int:
        ...

    @staticmethod
    @typing.overload
    def WaitAny(waitHandles: System.Array[System.Threading.WaitHandle], timeout: System.TimeSpan, ) -> int:
        ...

    @staticmethod
    @typing.overload
    def WaitAny(waitHandles: System.Array[System.Threading.WaitHandle], ) -> int:
        ...

    @staticmethod
    @typing.overload
    def WaitAny(waitHandles: System.Array[System.Threading.WaitHandle], millisecondsTimeout: int, exitContext: bool, ) -> int:
        ...

    @staticmethod
    @typing.overload
    def WaitAny(waitHandles: System.Array[System.Threading.WaitHandle], timeout: System.TimeSpan, exitContext: bool, ) -> int:
        ...

