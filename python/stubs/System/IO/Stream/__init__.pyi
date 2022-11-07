from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import System
import System.Threading.Tasks
import System.IO
import System.Threading.Tasks.Task
import System.Threading


class ReadWriteTask(System.IAsyncResult, System.IDisposable, System.Threading.Tasks.ITaskCompletionAction, System.Threading.Tasks.Task[int]):
    @typing.overload
    def __init__(self, **kwargs):
        self._isRead: bool
        self._apm: bool
        self._endCalled: bool
        self._stream: System.IO.Stream
        self._buffer: System.Array[int]
        self._offset: int
        self._count: int
        self.m_result: int
        self.m_action: System.Delegate
        self.m_stateObject: System.Object
        self.m_taskScheduler: System.Threading.Tasks.TaskScheduler
        self.m_stateFlags: int
        self.m_contingentProperties: System.Threading.Tasks.Task.ContingentProperties
        ...

    # static fields

    # properties
    @property
    def InvokeMayRunArbitraryCode(self) -> bool:
        ...

    @property
    def Result(self) -> int:
        ...

    @property
    def ResultOnSuccess(self) -> int:
        ...

    @property
    def Options(self) -> int:
        ...

    @property
    def IsWaitNotificationEnabledOrNotRanToCompletion(self) -> bool:
        ...

    @property
    def ShouldNotifyDebuggerOfWaitCompletion(self) -> bool:
        ...

    @property
    def IsWaitNotificationEnabled(self) -> bool:
        ...

    @property
    def Id(self) -> int:
        ...

    @property
    def Exception(self) -> System.AggregateException:
        ...

    @property
    def Status(self) -> int:
        ...

    @property
    def IsCanceled(self) -> bool:
        ...

    @property
    def IsCancellationRequested(self) -> bool:
        ...

    @property
    def CancellationToken(self) -> System.Threading.CancellationToken:
        ...

    @property
    def IsCancellationAcknowledged(self) -> bool:
        ...

    @property
    def IsCompleted(self) -> bool:
        ...

    @property
    def IsCompletedSuccessfully(self) -> bool:
        ...

    @property
    def CreationOptions(self) -> int:
        ...

    @property
    def AsyncState(self) -> System.Object:
        ...

    @property
    def ExecutingTaskScheduler(self) -> System.Threading.Tasks.TaskScheduler:
        ...

    @property
    def CompletedEvent(self) -> System.Threading.ManualResetEventSlim:
        ...

    @property
    def ExceptionRecorded(self) -> bool:
        ...

    @property
    def IsFaulted(self) -> bool:
        ...

    @property
    def CapturedContext(self) -> System.Threading.ExecutionContext:
        ...
    @CapturedContext.setter
    def CapturedContext(self, val: System.Threading.ExecutionContext):
        ...

    @property
    def IsExceptionObservedByParent(self) -> bool:
        ...

    @property
    def IsDelegateInvoked(self) -> bool:
        ...

    # methods
    def __init__(self, isRead: bool, apm: bool, function: System.Func[System.Object, int], state: System.Object, stream: System.IO.Stream, buffer: System.Array[int], offset: int, count: int, callback: System.AsyncCallback, ):
        ...

    def ClearBeginState(self, ) -> None:
        ...

    @staticmethod
    def InvokeAsyncCallback(completedTask: System.Object, ) -> None:
        ...

    def Invoke(self, completingTask: System.Threading.Tasks.Task, ) -> None:
        ...

