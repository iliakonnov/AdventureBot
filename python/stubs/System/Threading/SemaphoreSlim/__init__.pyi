from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import System
import System.Threading.Tasks
import System.Threading.SemaphoreSlim
import System.Threading.Tasks.Task
import System.Threading


class TaskNode(System.IAsyncResult, System.IDisposable, System.Threading.Tasks.Task[bool]):
    @typing.overload
    def __init__(self, **kwargs):
        self.Prev: System.Threading.SemaphoreSlim.TaskNode
        self.Next: System.Threading.SemaphoreSlim.TaskNode
        self.m_result: bool
        self.m_action: System.Delegate
        self.m_stateObject: System.Object
        self.m_taskScheduler: System.Threading.Tasks.TaskScheduler
        self.m_stateFlags: int
        self.m_contingentProperties: System.Threading.Tasks.Task.ContingentProperties
        ...

    # static fields

    # properties
    @property
    def Result(self) -> bool:
        ...

    @property
    def ResultOnSuccess(self) -> bool:
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
    def __init__(self, ):
        ...

