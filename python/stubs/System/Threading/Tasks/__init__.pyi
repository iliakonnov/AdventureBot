from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import System
import System.Threading.Tasks
import System.Threading.Tasks.Task
import System.Threading
import System.Collections.Generic
import System.Runtime.CompilerServices
import System.Runtime.ExceptionServices
import System.Threading.Tasks.TaskScheduler
import System.Threading.Tasks.Sources

T = typing.TypeVar('T')
TResult = typing.TypeVar('TResult')
TNewResult = typing.TypeVar('TNewResult')
TAntecedentResult = typing.TypeVar('TAntecedentResult')
TArg1 = typing.TypeVar('TArg1')
TArg2 = typing.TypeVar('TArg2')
TArg3 = typing.TypeVar('TArg3')
TInstance = typing.TypeVar('TInstance')
TArgs = typing.TypeVar('TArgs')

class Task(System.IAsyncResult, System.IDisposable, System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        self.m_action: System.Delegate
        self.m_stateObject: System.Object
        self.m_taskScheduler: System.Threading.Tasks.TaskScheduler
        self.m_stateFlags: int
        self.m_contingentProperties: System.Threading.Tasks.Task.ContingentProperties
        ...

    # static fields
    s_taskIdCounter: int = ...
    s_asyncDebuggingEnabled: bool = ...
    s_cachedCompleted: System.Threading.Tasks.Task[System.Threading.Tasks.VoidTaskResult] = ...
    t_currentTask: System.Threading.Tasks.Task = ...

    # properties
    @property
    def ParentForDebugger(self) -> System.Threading.Tasks.Task:
        ...

    @property
    def StateFlagsForDebugger(self) -> int:
        ...

    @property
    def StateFlags(self) -> int:
        ...

    @property
    def DebuggerDisplayMethodDescription(self) -> str:
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
    def CurrentId(self) -> System.Nullable[int]:
        ...

    @property
    def InternalCurrent(self) -> System.Threading.Tasks.Task:
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
    def AsyncWaitHandle(self) -> System.Threading.WaitHandle:
        ...

    @property
    def AsyncState(self) -> System.Object:
        ...

    @property
    def CompletedSynchronously(self) -> bool:
        ...

    @property
    def ExecutingTaskScheduler(self) -> System.Threading.Tasks.TaskScheduler:
        ...

    @property
    def Factory(self) -> System.Threading.Tasks.TaskFactory:
        ...

    @property
    def CompletedTask(self) -> System.Threading.Tasks.Task:
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
    @typing.overload
    def __init__(self, canceled: bool, creationOptions: int, ct: System.Threading.CancellationToken, ):
        ...

    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def __init__(self, state: System.Object, creationOptions: int, promiseStyle: bool, ):
        ...

    @typing.overload
    def __init__(self, action: System.Action, ):
        ...

    @typing.overload
    def __init__(self, action: System.Action, cancellationToken: System.Threading.CancellationToken, ):
        ...

    @typing.overload
    def __init__(self, action: System.Action, creationOptions: int, ):
        ...

    @typing.overload
    def __init__(self, action: System.Action, cancellationToken: System.Threading.CancellationToken, creationOptions: int, ):
        ...

    @typing.overload
    def __init__(self, action: System.Action[System.Object], state: System.Object, ):
        ...

    @typing.overload
    def __init__(self, action: System.Action[System.Object], state: System.Object, cancellationToken: System.Threading.CancellationToken, ):
        ...

    @typing.overload
    def __init__(self, action: System.Action[System.Object], state: System.Object, creationOptions: int, ):
        ...

    @typing.overload
    def __init__(self, action: System.Action[System.Object], state: System.Object, cancellationToken: System.Threading.CancellationToken, creationOptions: int, ):
        ...

    @typing.overload
    def __init__(self, action: System.Delegate, state: System.Object, parent: System.Threading.Tasks.Task, cancellationToken: System.Threading.CancellationToken, creationOptions: int, internalOptions: int, scheduler: System.Threading.Tasks.TaskScheduler, ):
        ...

    @staticmethod
    @typing.overload
    def WaitAll(tasks: System.Array[System.Threading.Tasks.Task], millisecondsTimeout: int, ) -> bool:
        ...

    @staticmethod
    @typing.overload
    def WaitAll(tasks: System.Array[System.Threading.Tasks.Task], cancellationToken: System.Threading.CancellationToken, ) -> None:
        ...

    @staticmethod
    @typing.overload
    def WaitAll(tasks: System.Array[System.Threading.Tasks.Task], millisecondsTimeout: int, cancellationToken: System.Threading.CancellationToken, ) -> bool:
        ...

    @staticmethod
    @typing.overload
    def WaitAll(tasks: System.Array[System.Threading.Tasks.Task], ) -> None:
        ...

    @staticmethod
    @typing.overload
    def WaitAll(tasks: System.Array[System.Threading.Tasks.Task], timeout: System.TimeSpan, ) -> bool:
        ...

    @staticmethod
    def WaitAllCore(tasks: System.Array[System.Threading.Tasks.Task], millisecondsTimeout: int, cancellationToken: System.Threading.CancellationToken, ) -> bool:
        ...

    @staticmethod
    def AddToList(item: T, list: ref[System.Collections.Generic.List[T]], initSize: int, ) -> None:
        ...

    @staticmethod
    def WaitAllBlockingCore(tasks: System.Collections.Generic.List[System.Threading.Tasks.Task], millisecondsTimeout: int, cancellationToken: System.Threading.CancellationToken, ) -> bool:
        ...

    @staticmethod
    def AddExceptionsForCompletedTask(exceptions: ref[System.Collections.Generic.List[System.Exception]], t: System.Threading.Tasks.Task, ) -> None:
        ...

    @staticmethod
    @typing.overload
    def WaitAny(tasks: System.Array[System.Threading.Tasks.Task], ) -> int:
        ...

    @staticmethod
    @typing.overload
    def WaitAny(tasks: System.Array[System.Threading.Tasks.Task], timeout: System.TimeSpan, ) -> int:
        ...

    @staticmethod
    @typing.overload
    def WaitAny(tasks: System.Array[System.Threading.Tasks.Task], cancellationToken: System.Threading.CancellationToken, ) -> int:
        ...

    @staticmethod
    @typing.overload
    def WaitAny(tasks: System.Array[System.Threading.Tasks.Task], millisecondsTimeout: int, ) -> int:
        ...

    @staticmethod
    @typing.overload
    def WaitAny(tasks: System.Array[System.Threading.Tasks.Task], millisecondsTimeout: int, cancellationToken: System.Threading.CancellationToken, ) -> int:
        ...

    @staticmethod
    def WaitAnyCore(tasks: System.Array[System.Threading.Tasks.Task], millisecondsTimeout: int, cancellationToken: System.Threading.CancellationToken, ) -> int:
        ...

    @staticmethod
    def FromResult(result: TResult, ) -> System.Threading.Tasks.Task[TResult]:
        ...

    @staticmethod
    @typing.overload
    def FromException(exception: System.Exception, ) -> System.Threading.Tasks.Task:
        ...

    @staticmethod
    @typing.overload
    def FromException(exception: System.Exception, ) -> System.Threading.Tasks.Task[TResult]:
        ...

    @staticmethod
    @typing.overload
    def FromCanceled(cancellationToken: System.Threading.CancellationToken, ) -> System.Threading.Tasks.Task:
        ...

    @staticmethod
    @typing.overload
    def FromCanceled(cancellationToken: System.Threading.CancellationToken, ) -> System.Threading.Tasks.Task[TResult]:
        ...

    @staticmethod
    @typing.overload
    def FromCanceled(exception: System.OperationCanceledException, ) -> System.Threading.Tasks.Task:
        ...

    @staticmethod
    @typing.overload
    def FromCanceled(exception: System.OperationCanceledException, ) -> System.Threading.Tasks.Task[TResult]:
        ...

    @staticmethod
    @typing.overload
    def Run(action: System.Action, ) -> System.Threading.Tasks.Task:
        ...

    @staticmethod
    @typing.overload
    def Run(action: System.Action, cancellationToken: System.Threading.CancellationToken, ) -> System.Threading.Tasks.Task:
        ...

    @staticmethod
    @typing.overload
    def Run(function: System.Func[TResult], ) -> System.Threading.Tasks.Task[TResult]:
        ...

    @staticmethod
    @typing.overload
    def Run(function: System.Func[TResult], cancellationToken: System.Threading.CancellationToken, ) -> System.Threading.Tasks.Task[TResult]:
        ...

    @staticmethod
    @typing.overload
    def Run(function: System.Func[System.Threading.Tasks.Task], ) -> System.Threading.Tasks.Task:
        ...

    @staticmethod
    @typing.overload
    def Run(function: System.Func[System.Threading.Tasks.Task], cancellationToken: System.Threading.CancellationToken, ) -> System.Threading.Tasks.Task:
        ...

    @staticmethod
    @typing.overload
    def Run(function: System.Func[System.Threading.Tasks.Task[TResult]], ) -> System.Threading.Tasks.Task[TResult]:
        ...

    @staticmethod
    @typing.overload
    def Run(function: System.Func[System.Threading.Tasks.Task[TResult]], cancellationToken: System.Threading.CancellationToken, ) -> System.Threading.Tasks.Task[TResult]:
        ...

    @staticmethod
    @typing.overload
    def Delay(delay: System.TimeSpan, ) -> System.Threading.Tasks.Task:
        ...

    @staticmethod
    @typing.overload
    def Delay(delay: System.TimeSpan, cancellationToken: System.Threading.CancellationToken, ) -> System.Threading.Tasks.Task:
        ...

    @staticmethod
    @typing.overload
    def Delay(millisecondsDelay: int, ) -> System.Threading.Tasks.Task:
        ...

    @staticmethod
    @typing.overload
    def Delay(millisecondsDelay: int, cancellationToken: System.Threading.CancellationToken, ) -> System.Threading.Tasks.Task:
        ...

    @staticmethod
    @typing.overload
    def Delay(millisecondsDelay: int, cancellationToken: System.Threading.CancellationToken, ) -> System.Threading.Tasks.Task:
        ...

    @staticmethod
    def ValidateTimeout(timeout: System.TimeSpan, argument: int, ) -> int:
        ...

    @staticmethod
    @typing.overload
    def WhenAll(tasks: System.Collections.Generic.IEnumerable[System.Threading.Tasks.Task], ) -> System.Threading.Tasks.Task:
        ...

    @staticmethod
    @typing.overload
    def WhenAll(tasks: System.Array[System.Threading.Tasks.Task], ) -> System.Threading.Tasks.Task:
        ...

    @staticmethod
    @typing.overload
    def WhenAll(tasks: System.Collections.Generic.IEnumerable[System.Threading.Tasks.Task[TResult]], ) -> System.Threading.Tasks.Task[System.Array[TResult]]:
        ...

    @staticmethod
    @typing.overload
    def WhenAll(tasks: System.Array[System.Threading.Tasks.Task[TResult]], ) -> System.Threading.Tasks.Task[System.Array[TResult]]:
        ...

    @staticmethod
    @typing.overload
    def InternalWhenAll(tasks: System.Array[System.Threading.Tasks.Task], ) -> System.Threading.Tasks.Task:
        ...

    @staticmethod
    @typing.overload
    def InternalWhenAll(tasks: System.Array[System.Threading.Tasks.Task[TResult]], ) -> System.Threading.Tasks.Task[System.Array[TResult]]:
        ...

    @staticmethod
    @typing.overload
    def WhenAny(tasks: System.Array[System.Threading.Tasks.Task], ) -> System.Threading.Tasks.Task[System.Threading.Tasks.Task]:
        ...

    @staticmethod
    @typing.overload
    def WhenAny(task1: System.Threading.Tasks.Task, task2: System.Threading.Tasks.Task, ) -> System.Threading.Tasks.Task[System.Threading.Tasks.Task]:
        ...

    @staticmethod
    @typing.overload
    def WhenAny(tasks: System.Collections.Generic.IEnumerable[System.Threading.Tasks.Task], ) -> System.Threading.Tasks.Task[System.Threading.Tasks.Task]:
        ...

    @staticmethod
    @typing.overload
    def WhenAny(tasks: System.Array[System.Threading.Tasks.Task[TResult]], ) -> System.Threading.Tasks.Task[System.Threading.Tasks.Task[TResult]]:
        ...

    @staticmethod
    @typing.overload
    def WhenAny(task1: System.Threading.Tasks.Task[TResult], task2: System.Threading.Tasks.Task[TResult], ) -> System.Threading.Tasks.Task[System.Threading.Tasks.Task[TResult]]:
        ...

    @staticmethod
    @typing.overload
    def WhenAny(tasks: System.Collections.Generic.IEnumerable[System.Threading.Tasks.Task[TResult]], ) -> System.Threading.Tasks.Task[System.Threading.Tasks.Task[TResult]]:
        ...

    @staticmethod
    def CreateUnwrapPromise(outerTask: System.Threading.Tasks.Task, lookForOce: bool, ) -> System.Threading.Tasks.Task[TResult]:
        ...

    def GetDelegateContinuationsForDebugger(self, ) -> System.Array[System.Delegate]:
        ...

    @staticmethod
    def GetDelegatesFromContinuationObject(continuationObject: System.Object, ) -> System.Array[System.Delegate]:
        ...

    @staticmethod
    def GetActiveTaskFromId(taskId: int, ) -> System.Threading.Tasks.Task:
        ...

    def FinishSlow(self, userDelegateExecute: bool, ) -> None:
        ...

    def FinishStageTwo(self, ) -> None:
        ...

    def FinishStageThree(self, ) -> None:
        ...

    def NotifyParentIfPotentiallyAttachedTask(self, ) -> None:
        ...

    def ProcessChildCompletion(self, childTask: System.Threading.Tasks.Task, ) -> None:
        ...

    def AddExceptionsFromChildren(self, props: System.Threading.Tasks.Task.ContingentProperties, ) -> None:
        ...

    def ExecuteEntry(self, ) -> bool:
        ...

    def ExecuteFromThreadPool(self, threadPoolThread: System.Threading.Thread, ) -> None:
        ...

    def ExecuteEntryUnsafe(self, threadPoolThread: System.Threading.Thread, ) -> None:
        ...

    def ExecuteEntryCancellationRequestedOrCanceled(self, ) -> None:
        ...

    def ExecuteWithThreadLocal(self, currentTaskSlot: ref[System.Threading.Tasks.Task], threadPoolThread: System.Threading.Thread = ..., ) -> None:
        ...

    def InnerInvoke(self, ) -> None:
        ...

    def HandleException(self, unhandledException: System.Exception, ) -> None:
        ...

    def GetAwaiter(self, ) -> System.Runtime.CompilerServices.TaskAwaiter:
        ...

    def ConfigureAwait(self, continueOnCapturedContext: bool, ) -> System.Runtime.CompilerServices.ConfiguredTaskAwaitable:
        ...

    def SetContinuationForAwait(self, continuationAction: System.Action, continueOnCapturedContext: bool, flowExecutionContext: bool, ) -> None:
        ...

    def UnsafeSetContinuationForAwait(self, stateMachineBox: System.Runtime.CompilerServices.IAsyncStateMachineBox, continueOnCapturedContext: bool, ) -> None:
        ...

    @staticmethod
    def Yield() -> System.Runtime.CompilerServices.YieldAwaitable:
        ...

    @typing.overload
    def Wait(self, ) -> None:
        ...

    @typing.overload
    def Wait(self, timeout: System.TimeSpan, ) -> bool:
        ...

    @typing.overload
    def Wait(self, cancellationToken: System.Threading.CancellationToken, ) -> None:
        ...

    @typing.overload
    def Wait(self, millisecondsTimeout: int, ) -> bool:
        ...

    @typing.overload
    def Wait(self, millisecondsTimeout: int, cancellationToken: System.Threading.CancellationToken, ) -> bool:
        ...

    @typing.overload
    def WaitAsync(self, cancellationToken: System.Threading.CancellationToken, ) -> System.Threading.Tasks.Task:
        ...

    @typing.overload
    def WaitAsync(self, timeout: System.TimeSpan, ) -> System.Threading.Tasks.Task:
        ...

    @typing.overload
    def WaitAsync(self, timeout: System.TimeSpan, cancellationToken: System.Threading.CancellationToken, ) -> System.Threading.Tasks.Task:
        ...

    @typing.overload
    def WaitAsync(self, millisecondsTimeout: int, cancellationToken: System.Threading.CancellationToken, ) -> System.Threading.Tasks.Task:
        ...

    def WrappedTryRunInline(self, ) -> bool:
        ...

    def InternalWait(self, millisecondsTimeout: int, cancellationToken: System.Threading.CancellationToken, ) -> bool:
        ...

    def InternalWaitCore(self, millisecondsTimeout: int, cancellationToken: System.Threading.CancellationToken, ) -> bool:
        ...

    def SpinThenBlockingWait(self, millisecondsTimeout: int, cancellationToken: System.Threading.CancellationToken, ) -> bool:
        ...

    def SpinWait(self, millisecondsTimeout: int, ) -> bool:
        ...

    def InternalCancel(self, ) -> None:
        ...

    def InternalCancelContinueWithInitialState(self, ) -> None:
        ...

    @typing.overload
    def RecordInternalCancellationRequest(self, ) -> None:
        ...

    @typing.overload
    def RecordInternalCancellationRequest(self, tokenToRecord: System.Threading.CancellationToken, cancellationException: System.Object, ) -> None:
        ...

    def CancellationCleanupLogic(self, ) -> None:
        ...

    def SetCancellationAcknowledged(self, ) -> None:
        ...

    def TrySetResult(self, ) -> bool:
        ...

    def TrySetException(self, exceptionObject: System.Object, ) -> bool:
        ...

    @typing.overload
    def TrySetCanceled(self, tokenToRecord: System.Threading.CancellationToken, ) -> bool:
        ...

    @typing.overload
    def TrySetCanceled(self, tokenToRecord: System.Threading.CancellationToken, cancellationException: System.Object, ) -> bool:
        ...

    def FinishContinuations(self, ) -> None:
        ...

    def RunContinuations(self, continuationObject: System.Object, ) -> None:
        ...

    def RunOrQueueCompletionAction(self, completionAction: System.Threading.Tasks.ITaskCompletionAction, allowInlining: bool, ) -> None:
        ...

    @staticmethod
    def LogFinishCompletionNotification() -> None:
        ...

    @typing.overload
    def ContinueWith(self, continuationAction: System.Action[System.Threading.Tasks.Task], ) -> System.Threading.Tasks.Task:
        ...

    @typing.overload
    def ContinueWith(self, continuationAction: System.Action[System.Threading.Tasks.Task], cancellationToken: System.Threading.CancellationToken, ) -> System.Threading.Tasks.Task:
        ...

    @typing.overload
    def ContinueWith(self, continuationAction: System.Action[System.Threading.Tasks.Task], scheduler: System.Threading.Tasks.TaskScheduler, ) -> System.Threading.Tasks.Task:
        ...

    @typing.overload
    def ContinueWith(self, continuationAction: System.Action[System.Threading.Tasks.Task], continuationOptions: int, ) -> System.Threading.Tasks.Task:
        ...

    @typing.overload
    def ContinueWith(self, continuationAction: System.Action[System.Threading.Tasks.Task], cancellationToken: System.Threading.CancellationToken, continuationOptions: int, scheduler: System.Threading.Tasks.TaskScheduler, ) -> System.Threading.Tasks.Task:
        ...

    @typing.overload
    def ContinueWith(self, continuationAction: System.Action[System.Threading.Tasks.Task], scheduler: System.Threading.Tasks.TaskScheduler, cancellationToken: System.Threading.CancellationToken, continuationOptions: int, ) -> System.Threading.Tasks.Task:
        ...

    @typing.overload
    def ContinueWith(self, continuationAction: System.Action[System.Threading.Tasks.Task, System.Object], state: System.Object, ) -> System.Threading.Tasks.Task:
        ...

    @typing.overload
    def ContinueWith(self, continuationAction: System.Action[System.Threading.Tasks.Task, System.Object], state: System.Object, cancellationToken: System.Threading.CancellationToken, ) -> System.Threading.Tasks.Task:
        ...

    @typing.overload
    def ContinueWith(self, continuationAction: System.Action[System.Threading.Tasks.Task, System.Object], state: System.Object, scheduler: System.Threading.Tasks.TaskScheduler, ) -> System.Threading.Tasks.Task:
        ...

    @typing.overload
    def ContinueWith(self, continuationAction: System.Action[System.Threading.Tasks.Task, System.Object], state: System.Object, continuationOptions: int, ) -> System.Threading.Tasks.Task:
        ...

    @typing.overload
    def ContinueWith(self, continuationAction: System.Action[System.Threading.Tasks.Task, System.Object], state: System.Object, cancellationToken: System.Threading.CancellationToken, continuationOptions: int, scheduler: System.Threading.Tasks.TaskScheduler, ) -> System.Threading.Tasks.Task:
        ...

    @typing.overload
    def ContinueWith(self, continuationAction: System.Action[System.Threading.Tasks.Task, System.Object], state: System.Object, scheduler: System.Threading.Tasks.TaskScheduler, cancellationToken: System.Threading.CancellationToken, continuationOptions: int, ) -> System.Threading.Tasks.Task:
        ...

    @typing.overload
    def ContinueWith(self, continuationFunction: System.Func[System.Threading.Tasks.Task, TResult], ) -> System.Threading.Tasks.Task[TResult]:
        ...

    @typing.overload
    def ContinueWith(self, continuationFunction: System.Func[System.Threading.Tasks.Task, TResult], cancellationToken: System.Threading.CancellationToken, ) -> System.Threading.Tasks.Task[TResult]:
        ...

    @typing.overload
    def ContinueWith(self, continuationFunction: System.Func[System.Threading.Tasks.Task, TResult], scheduler: System.Threading.Tasks.TaskScheduler, ) -> System.Threading.Tasks.Task[TResult]:
        ...

    @typing.overload
    def ContinueWith(self, continuationFunction: System.Func[System.Threading.Tasks.Task, TResult], continuationOptions: int, ) -> System.Threading.Tasks.Task[TResult]:
        ...

    @typing.overload
    def ContinueWith(self, continuationFunction: System.Func[System.Threading.Tasks.Task, TResult], cancellationToken: System.Threading.CancellationToken, continuationOptions: int, scheduler: System.Threading.Tasks.TaskScheduler, ) -> System.Threading.Tasks.Task[TResult]:
        ...

    @typing.overload
    def ContinueWith(self, continuationFunction: System.Func[System.Threading.Tasks.Task, TResult], scheduler: System.Threading.Tasks.TaskScheduler, cancellationToken: System.Threading.CancellationToken, continuationOptions: int, ) -> System.Threading.Tasks.Task[TResult]:
        ...

    @typing.overload
    def ContinueWith(self, continuationFunction: System.Func[System.Threading.Tasks.Task, System.Object, TResult], state: System.Object, ) -> System.Threading.Tasks.Task[TResult]:
        ...

    @typing.overload
    def ContinueWith(self, continuationFunction: System.Func[System.Threading.Tasks.Task, System.Object, TResult], state: System.Object, cancellationToken: System.Threading.CancellationToken, ) -> System.Threading.Tasks.Task[TResult]:
        ...

    @typing.overload
    def ContinueWith(self, continuationFunction: System.Func[System.Threading.Tasks.Task, System.Object, TResult], state: System.Object, scheduler: System.Threading.Tasks.TaskScheduler, ) -> System.Threading.Tasks.Task[TResult]:
        ...

    @typing.overload
    def ContinueWith(self, continuationFunction: System.Func[System.Threading.Tasks.Task, System.Object, TResult], state: System.Object, continuationOptions: int, ) -> System.Threading.Tasks.Task[TResult]:
        ...

    @typing.overload
    def ContinueWith(self, continuationFunction: System.Func[System.Threading.Tasks.Task, System.Object, TResult], state: System.Object, cancellationToken: System.Threading.CancellationToken, continuationOptions: int, scheduler: System.Threading.Tasks.TaskScheduler, ) -> System.Threading.Tasks.Task[TResult]:
        ...

    @typing.overload
    def ContinueWith(self, continuationFunction: System.Func[System.Threading.Tasks.Task, System.Object, TResult], state: System.Object, scheduler: System.Threading.Tasks.TaskScheduler, cancellationToken: System.Threading.CancellationToken, continuationOptions: int, ) -> System.Threading.Tasks.Task[TResult]:
        ...

    @staticmethod
    def CreationOptionsFromContinuationOptions(continuationOptions: int, creationOptions: ref[int], internalOptions: ref[int], ) -> None:
        ...

    def ContinueWithCore(self, continuationTask: System.Threading.Tasks.Task, scheduler: System.Threading.Tasks.TaskScheduler, cancellationToken: System.Threading.CancellationToken, options: int, ) -> None:
        ...

    def AddCompletionAction(self, action: System.Threading.Tasks.ITaskCompletionAction, addBeforeOthers: bool = ..., ) -> None:
        ...

    def AddTaskContinuationComplex(self, tc: System.Object, addBeforeOthers: bool, ) -> bool:
        ...

    def AddTaskContinuation(self, tc: System.Object, addBeforeOthers: bool, ) -> bool:
        ...

    def RemoveContinuation(self, continuationObject: System.Object, ) -> None:
        ...

    @staticmethod
    def AddToActiveTasks(task: System.Threading.Tasks.Task, ) -> bool:
        ...

    @staticmethod
    def RemoveFromActiveTasks(task: System.Threading.Tasks.Task, ) -> None:
        ...

    def TaskConstructorCore(self, action: System.Delegate, state: System.Object, cancellationToken: System.Threading.CancellationToken, creationOptions: int, internalOptions: int, scheduler: System.Threading.Tasks.TaskScheduler, ) -> None:
        ...

    def AssignCancellationToken(self, cancellationToken: System.Threading.CancellationToken, antecedent: System.Threading.Tasks.Task, continuation: System.Threading.Tasks.TaskContinuation, ) -> None:
        ...

    @staticmethod
    def OptionsMethod(flags: int, ) -> int:
        ...

    @typing.overload
    def AtomicStateUpdate(self, newBits: int, illegalBits: int, ) -> bool:
        ...

    @typing.overload
    def AtomicStateUpdate(self, newBits: int, illegalBits: int, oldFlags: ref[int], ) -> bool:
        ...

    def AtomicStateUpdateSlow(self, newBits: int, illegalBits: int, ) -> bool:
        ...

    def SetNotificationForWaitCompletion(self, enabled: bool, ) -> None:
        ...

    def NotifyDebuggerOfWaitCompletionIfNecessary(self, ) -> bool:
        ...

    @staticmethod
    def AnyTaskRequiresNotifyDebuggerOfWaitCompletion(tasks: System.Array[System.Threading.Tasks.Task], ) -> bool:
        ...

    def NotifyDebuggerOfWaitCompletion(self, ) -> None:
        ...

    def MarkStarted(self, ) -> bool:
        ...

    def FireTaskScheduledIfNeeded(self, ts: System.Threading.Tasks.TaskScheduler, ) -> None:
        ...

    def AddNewChild(self, ) -> None:
        ...

    def DisregardChild(self, ) -> None:
        ...

    @typing.overload
    def Start(self, ) -> None:
        ...

    @typing.overload
    def Start(self, scheduler: System.Threading.Tasks.TaskScheduler, ) -> None:
        ...

    @typing.overload
    def RunSynchronously(self, ) -> None:
        ...

    @typing.overload
    def RunSynchronously(self, scheduler: System.Threading.Tasks.TaskScheduler, ) -> None:
        ...

    def InternalRunSynchronously(self, scheduler: System.Threading.Tasks.TaskScheduler, waitForCompletion: bool, ) -> None:
        ...

    @staticmethod
    def InternalStartNew(creatingTask: System.Threading.Tasks.Task, action: System.Delegate, state: System.Object, cancellationToken: System.Threading.CancellationToken, scheduler: System.Threading.Tasks.TaskScheduler, options: int, internalOptions: int, ) -> System.Threading.Tasks.Task:
        ...

    @staticmethod
    def NewId() -> int:
        ...

    @staticmethod
    def InternalCurrentIfAttached(creationOptions: int, ) -> System.Threading.Tasks.Task:
        ...

    def EnsureContingentPropertiesInitialized(self, ) -> System.Threading.Tasks.Task.ContingentProperties:
        ...

    def EnsureContingentPropertiesInitializedUnsafe(self, ) -> System.Threading.Tasks.Task.ContingentProperties:
        ...

    @staticmethod
    def IsCompletedMethod(flags: int, ) -> bool:
        ...

    def SpinUntilCompleted(self, ) -> None:
        ...

    @typing.overload
    def Dispose(self, ) -> None:
        ...

    @typing.overload
    def Dispose(self, disposing: bool, ) -> None:
        ...

    def ScheduleAndStart(self, needsProtection: bool, ) -> None:
        ...

    @typing.overload
    def AddException(self, exceptionObject: System.Object, ) -> None:
        ...

    @typing.overload
    def AddException(self, exceptionObject: System.Object, representsCancellation: bool, ) -> None:
        ...

    def GetExceptions(self, includeTaskCanceledExceptions: bool, ) -> System.AggregateException:
        ...

    def GetExceptionDispatchInfos(self, ) -> System.Collections.Generic.List[System.Runtime.ExceptionServices.ExceptionDispatchInfo]:
        ...

    def GetCancellationExceptionDispatchInfo(self, ) -> System.Runtime.ExceptionServices.ExceptionDispatchInfo:
        ...

    def MarkExceptionsAsHandled(self, ) -> None:
        ...

    def ThrowIfExceptional(self, includeTaskCanceledExceptions: bool, ) -> None:
        ...

    @staticmethod
    def ThrowAsync(exception: System.Exception, targetContext: System.Threading.SynchronizationContext, ) -> None:
        ...

    def UpdateExceptionObservedStatus(self, ) -> None:
        ...

    def Finish(self, userDelegateExecute: bool, ) -> None:
        ...

class Task(System.IAsyncResult, System.IDisposable, System.Threading.Tasks.Task, typing.Generic[TResult]):
    @typing.overload
    def __init__(self, **kwargs):
        self.m_result: TResult
        self.m_action: System.Delegate
        self.m_stateObject: System.Object
        self.m_taskScheduler: System.Threading.Tasks.TaskScheduler
        self.m_stateFlags: int
        self.m_contingentProperties: System.Threading.Tasks.Task.ContingentProperties
        ...

    # static fields
    s_defaultResultTask: System.Threading.Tasks.Task = ...

    # properties
    @property
    def DebuggerDisplayResultDescription(self) -> str:
        ...

    @property
    def DebuggerDisplayMethodDescription(self) -> str:
        ...

    @property
    def Result(self) -> TResult:
        ...

    @property
    def ResultOnSuccess(self) -> TResult:
        ...

    @property
    def Factory(self) -> System.Threading.Tasks.TaskFactory[TResult]:
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
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def __init__(self, state: System.Object, options: int, ):
        ...

    @typing.overload
    def __init__(self, result: TResult, ):
        ...

    @typing.overload
    def __init__(self, canceled: bool, result: TResult, creationOptions: int, ct: System.Threading.CancellationToken, ):
        ...

    @typing.overload
    def __init__(self, function: System.Func[TResult], ):
        ...

    @typing.overload
    def __init__(self, function: System.Func[TResult], cancellationToken: System.Threading.CancellationToken, ):
        ...

    @typing.overload
    def __init__(self, function: System.Func[TResult], creationOptions: int, ):
        ...

    @typing.overload
    def __init__(self, function: System.Func[TResult], cancellationToken: System.Threading.CancellationToken, creationOptions: int, ):
        ...

    @typing.overload
    def __init__(self, function: System.Func[System.Object, TResult], state: System.Object, ):
        ...

    @typing.overload
    def __init__(self, function: System.Func[System.Object, TResult], state: System.Object, cancellationToken: System.Threading.CancellationToken, ):
        ...

    @typing.overload
    def __init__(self, function: System.Func[System.Object, TResult], state: System.Object, creationOptions: int, ):
        ...

    @typing.overload
    def __init__(self, function: System.Func[System.Object, TResult], state: System.Object, cancellationToken: System.Threading.CancellationToken, creationOptions: int, ):
        ...

    @typing.overload
    def __init__(self, valueSelector: System.Func[TResult], parent: System.Threading.Tasks.Task, cancellationToken: System.Threading.CancellationToken, creationOptions: int, internalOptions: int, scheduler: System.Threading.Tasks.TaskScheduler, ):
        ...

    @typing.overload
    def __init__(self, valueSelector: System.Delegate, state: System.Object, parent: System.Threading.Tasks.Task, cancellationToken: System.Threading.CancellationToken, creationOptions: int, internalOptions: int, scheduler: System.Threading.Tasks.TaskScheduler, ):
        ...

    @staticmethod
    @typing.overload
    def StartNew(parent: System.Threading.Tasks.Task, function: System.Func[TResult], cancellationToken: System.Threading.CancellationToken, creationOptions: int, internalOptions: int, scheduler: System.Threading.Tasks.TaskScheduler, ) -> System.Threading.Tasks.Task:
        ...

    @staticmethod
    @typing.overload
    def StartNew(parent: System.Threading.Tasks.Task, function: System.Func[System.Object, TResult], state: System.Object, cancellationToken: System.Threading.CancellationToken, creationOptions: int, internalOptions: int, scheduler: System.Threading.Tasks.TaskScheduler, ) -> System.Threading.Tasks.Task:
        ...

    def TrySetResult(self, result: TResult, ) -> bool:
        ...

    def DangerousSetResult(self, result: TResult, ) -> None:
        ...

    def GetResultCore(self, waitCompletionNotification: bool, ) -> TResult:
        ...

    def InnerInvoke(self, ) -> None:
        ...

    def GetAwaiter(self, ) -> System.Runtime.CompilerServices.TaskAwaiter[TResult]:
        ...

    def ConfigureAwait(self, continueOnCapturedContext: bool, ) -> System.Runtime.CompilerServices.ConfiguredTaskAwaitable[TResult]:
        ...

    @typing.overload
    def WaitAsync(self, cancellationToken: System.Threading.CancellationToken, ) -> System.Threading.Tasks.Task:
        ...

    @typing.overload
    def WaitAsync(self, timeout: System.TimeSpan, ) -> System.Threading.Tasks.Task:
        ...

    @typing.overload
    def WaitAsync(self, timeout: System.TimeSpan, cancellationToken: System.Threading.CancellationToken, ) -> System.Threading.Tasks.Task:
        ...

    @typing.overload
    def WaitAsync(self, millisecondsTimeout: int, cancellationToken: System.Threading.CancellationToken, ) -> System.Threading.Tasks.Task:
        ...

    @typing.overload
    def ContinueWith(self, continuationAction: System.Action[System.Threading.Tasks.Task], ) -> System.Threading.Tasks.Task:
        ...

    @typing.overload
    def ContinueWith(self, continuationAction: System.Action[System.Threading.Tasks.Task], cancellationToken: System.Threading.CancellationToken, ) -> System.Threading.Tasks.Task:
        ...

    @typing.overload
    def ContinueWith(self, continuationAction: System.Action[System.Threading.Tasks.Task], scheduler: System.Threading.Tasks.TaskScheduler, ) -> System.Threading.Tasks.Task:
        ...

    @typing.overload
    def ContinueWith(self, continuationAction: System.Action[System.Threading.Tasks.Task], continuationOptions: int, ) -> System.Threading.Tasks.Task:
        ...

    @typing.overload
    def ContinueWith(self, continuationAction: System.Action[System.Threading.Tasks.Task], cancellationToken: System.Threading.CancellationToken, continuationOptions: int, scheduler: System.Threading.Tasks.TaskScheduler, ) -> System.Threading.Tasks.Task:
        ...

    @typing.overload
    def ContinueWith(self, continuationAction: System.Action[System.Threading.Tasks.Task], scheduler: System.Threading.Tasks.TaskScheduler, cancellationToken: System.Threading.CancellationToken, continuationOptions: int, ) -> System.Threading.Tasks.Task:
        ...

    @typing.overload
    def ContinueWith(self, continuationAction: System.Action[System.Threading.Tasks.Task, System.Object], state: System.Object, ) -> System.Threading.Tasks.Task:
        ...

    @typing.overload
    def ContinueWith(self, continuationAction: System.Action[System.Threading.Tasks.Task, System.Object], state: System.Object, cancellationToken: System.Threading.CancellationToken, ) -> System.Threading.Tasks.Task:
        ...

    @typing.overload
    def ContinueWith(self, continuationAction: System.Action[System.Threading.Tasks.Task, System.Object], state: System.Object, scheduler: System.Threading.Tasks.TaskScheduler, ) -> System.Threading.Tasks.Task:
        ...

    @typing.overload
    def ContinueWith(self, continuationAction: System.Action[System.Threading.Tasks.Task, System.Object], state: System.Object, continuationOptions: int, ) -> System.Threading.Tasks.Task:
        ...

    @typing.overload
    def ContinueWith(self, continuationAction: System.Action[System.Threading.Tasks.Task, System.Object], state: System.Object, cancellationToken: System.Threading.CancellationToken, continuationOptions: int, scheduler: System.Threading.Tasks.TaskScheduler, ) -> System.Threading.Tasks.Task:
        ...

    @typing.overload
    def ContinueWith(self, continuationAction: System.Action[System.Threading.Tasks.Task, System.Object], state: System.Object, scheduler: System.Threading.Tasks.TaskScheduler, cancellationToken: System.Threading.CancellationToken, continuationOptions: int, ) -> System.Threading.Tasks.Task:
        ...

    @typing.overload
    def ContinueWith(self, continuationFunction: System.Func[System.Threading.Tasks.Task, TNewResult], ) -> System.Threading.Tasks.Task[TNewResult]:
        ...

    @typing.overload
    def ContinueWith(self, continuationFunction: System.Func[System.Threading.Tasks.Task, TNewResult], cancellationToken: System.Threading.CancellationToken, ) -> System.Threading.Tasks.Task[TNewResult]:
        ...

    @typing.overload
    def ContinueWith(self, continuationFunction: System.Func[System.Threading.Tasks.Task, TNewResult], scheduler: System.Threading.Tasks.TaskScheduler, ) -> System.Threading.Tasks.Task[TNewResult]:
        ...

    @typing.overload
    def ContinueWith(self, continuationFunction: System.Func[System.Threading.Tasks.Task, TNewResult], continuationOptions: int, ) -> System.Threading.Tasks.Task[TNewResult]:
        ...

    @typing.overload
    def ContinueWith(self, continuationFunction: System.Func[System.Threading.Tasks.Task, TNewResult], cancellationToken: System.Threading.CancellationToken, continuationOptions: int, scheduler: System.Threading.Tasks.TaskScheduler, ) -> System.Threading.Tasks.Task[TNewResult]:
        ...

    @typing.overload
    def ContinueWith(self, continuationFunction: System.Func[System.Threading.Tasks.Task, TNewResult], scheduler: System.Threading.Tasks.TaskScheduler, cancellationToken: System.Threading.CancellationToken, continuationOptions: int, ) -> System.Threading.Tasks.Task[TNewResult]:
        ...

    @typing.overload
    def ContinueWith(self, continuationFunction: System.Func[System.Threading.Tasks.Task, System.Object, TNewResult], state: System.Object, ) -> System.Threading.Tasks.Task[TNewResult]:
        ...

    @typing.overload
    def ContinueWith(self, continuationFunction: System.Func[System.Threading.Tasks.Task, System.Object, TNewResult], state: System.Object, cancellationToken: System.Threading.CancellationToken, ) -> System.Threading.Tasks.Task[TNewResult]:
        ...

    @typing.overload
    def ContinueWith(self, continuationFunction: System.Func[System.Threading.Tasks.Task, System.Object, TNewResult], state: System.Object, scheduler: System.Threading.Tasks.TaskScheduler, ) -> System.Threading.Tasks.Task[TNewResult]:
        ...

    @typing.overload
    def ContinueWith(self, continuationFunction: System.Func[System.Threading.Tasks.Task, System.Object, TNewResult], state: System.Object, continuationOptions: int, ) -> System.Threading.Tasks.Task[TNewResult]:
        ...

    @typing.overload
    def ContinueWith(self, continuationFunction: System.Func[System.Threading.Tasks.Task, System.Object, TNewResult], state: System.Object, cancellationToken: System.Threading.CancellationToken, continuationOptions: int, scheduler: System.Threading.Tasks.TaskScheduler, ) -> System.Threading.Tasks.Task[TNewResult]:
        ...

    @typing.overload
    def ContinueWith(self, continuationFunction: System.Func[System.Threading.Tasks.Task, System.Object, TNewResult], state: System.Object, scheduler: System.Threading.Tasks.TaskScheduler, cancellationToken: System.Threading.CancellationToken, continuationOptions: int, ) -> System.Threading.Tasks.Task[TNewResult]:
        ...

class TaskContinuationOptions(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    None_: int = ...
    PreferFairness: int = ...
    LongRunning: int = ...
    AttachedToParent: int = ...
    DenyChildAttach: int = ...
    HideScheduler: int = ...
    LazyCancellation: int = ...
    RunContinuationsAsynchronously: int = ...
    NotOnRanToCompletion: int = ...
    NotOnFaulted: int = ...
    OnlyOnCanceled: int = ...
    NotOnCanceled: int = ...
    OnlyOnFaulted: int = ...
    OnlyOnRanToCompletion: int = ...
    ExecuteSynchronously: int = ...

class TaskScheduler(System.Object, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields
    s_taskSchedulerIdCounter: int = ...

    # properties
    @property
    def MaximumConcurrencyLevel(self) -> int:
        ...

    @property
    def Default(self) -> System.Threading.Tasks.TaskScheduler:
        ...

    @property
    def Current(self) -> System.Threading.Tasks.TaskScheduler:
        ...

    @property
    def InternalCurrent(self) -> System.Threading.Tasks.TaskScheduler:
        ...

    @property
    def Id(self) -> int:
        ...

    # methods
    def __init__(self, ):
        ...

    @abc.abstractmethod
    def QueueTask(self, task: System.Threading.Tasks.Task, ) -> None:
        ...

    @abc.abstractmethod
    def TryExecuteTaskInline(self, task: System.Threading.Tasks.Task, taskWasPreviouslyQueued: bool, ) -> bool:
        ...

    @abc.abstractmethod
    def GetScheduledTasks(self, ) -> System.Collections.Generic.IEnumerable[System.Threading.Tasks.Task]:
        ...

    def TryRunInline(self, task: System.Threading.Tasks.Task, taskWasPreviouslyQueued: bool, ) -> bool:
        ...

    def TryDequeue(self, task: System.Threading.Tasks.Task, ) -> bool:
        ...

    def NotifyWorkItemProgress(self, ) -> None:
        ...

    def InternalQueueTask(self, task: System.Threading.Tasks.Task, ) -> None:
        ...

    def AddToActiveTaskSchedulers(self, ) -> None:
        ...

    @staticmethod
    def FromCurrentSynchronizationContext() -> System.Threading.Tasks.TaskScheduler:
        ...

    def TryExecuteTask(self, task: System.Threading.Tasks.Task, ) -> bool:
        ...

    @staticmethod
    def PublishUnobservedTaskException(sender: System.Object, ueea: System.Threading.Tasks.UnobservedTaskExceptionEventArgs, ) -> None:
        ...

    def GetScheduledTasksForDebugger(self, ) -> System.Array[System.Threading.Tasks.Task]:
        ...

    @staticmethod
    def GetTaskSchedulersForDebugger() -> System.Array[System.Threading.Tasks.TaskScheduler]:
        ...

    def GetAwaiter(self, ) -> System.Threading.Tasks.TaskScheduler.TaskSchedulerAwaiter:
        ...

class ValueTask(System.IEquatable[System.Threading.Tasks.ValueTask], System.ValueType):
    @typing.overload
    def __init__(self, **kwargs):
        self._obj: System.Object
        self._token: int
        self._continueOnCapturedContext: bool
        ...

    # static fields

    # properties
    @property
    def CompletedTask(self) -> System.Threading.Tasks.ValueTask:
        ...

    @property
    def IsCompleted(self) -> bool:
        ...

    @property
    def IsCompletedSuccessfully(self) -> bool:
        ...

    @property
    def IsFaulted(self) -> bool:
        ...

    @property
    def IsCanceled(self) -> bool:
        ...

    # methods
    @typing.overload
    def __init__(self, task: System.Threading.Tasks.Task, ):
        ...

    @typing.overload
    def __init__(self, source: System.Threading.Tasks.Sources.IValueTaskSource, token: int, ):
        ...

    @typing.overload
    def __init__(self, obj: System.Object, token: int, continueOnCapturedContext: bool, ):
        ...

    @staticmethod
    def FromResult(result: TResult, ) -> System.Threading.Tasks.ValueTask[TResult]:
        ...

    @staticmethod
    @typing.overload
    def FromCanceled(cancellationToken: System.Threading.CancellationToken, ) -> System.Threading.Tasks.ValueTask:
        ...

    @staticmethod
    @typing.overload
    def FromCanceled(cancellationToken: System.Threading.CancellationToken, ) -> System.Threading.Tasks.ValueTask[TResult]:
        ...

    @staticmethod
    @typing.overload
    def FromException(exception: System.Exception, ) -> System.Threading.Tasks.ValueTask:
        ...

    @staticmethod
    @typing.overload
    def FromException(exception: System.Exception, ) -> System.Threading.Tasks.ValueTask[TResult]:
        ...

    def GetHashCode(self, ) -> int:
        ...

    @typing.overload
    def Equals(self, obj: System.Object, ) -> bool:
        ...

    @typing.overload
    def Equals(self, other: System.Threading.Tasks.ValueTask, ) -> bool:
        ...

    def AsTask(self, ) -> System.Threading.Tasks.Task:
        ...

    def Preserve(self, ) -> System.Threading.Tasks.ValueTask:
        ...

    def GetTaskForValueTaskSource(self, t: System.Threading.Tasks.Sources.IValueTaskSource, ) -> System.Threading.Tasks.Task:
        ...

    def ThrowIfCompletedUnsuccessfully(self, ) -> None:
        ...

    def GetAwaiter(self, ) -> System.Runtime.CompilerServices.ValueTaskAwaiter:
        ...

    def ConfigureAwait(self, continueOnCapturedContext: bool, ) -> System.Runtime.CompilerServices.ConfiguredValueTaskAwaitable:
        ...

class ValueTask(System.IEquatable[System.Threading.Tasks.ValueTask], System.ValueType, typing.Generic[TResult]):
    @typing.overload
    def __init__(self, **kwargs):
        self._obj: System.Object
        self._result: TResult
        self._token: int
        self._continueOnCapturedContext: bool
        ...

    # static fields

    # properties
    @property
    def IsCompleted(self) -> bool:
        ...

    @property
    def IsCompletedSuccessfully(self) -> bool:
        ...

    @property
    def IsFaulted(self) -> bool:
        ...

    @property
    def IsCanceled(self) -> bool:
        ...

    @property
    def Result(self) -> TResult:
        ...

    # methods
    @typing.overload
    def __init__(self, result: TResult, ):
        ...

    @typing.overload
    def __init__(self, task: System.Threading.Tasks.Task[TResult], ):
        ...

    @typing.overload
    def __init__(self, source: System.Threading.Tasks.Sources.IValueTaskSource[TResult], token: int, ):
        ...

    @typing.overload
    def __init__(self, obj: System.Object, result: TResult, token: int, continueOnCapturedContext: bool, ):
        ...

    def GetHashCode(self, ) -> int:
        ...

    @typing.overload
    def Equals(self, obj: System.Object, ) -> bool:
        ...

    @typing.overload
    def Equals(self, other: System.Threading.Tasks.ValueTask, ) -> bool:
        ...

    def AsTask(self, ) -> System.Threading.Tasks.Task[TResult]:
        ...

    def Preserve(self, ) -> System.Threading.Tasks.ValueTask:
        ...

    def GetTaskForValueTaskSource(self, t: System.Threading.Tasks.Sources.IValueTaskSource[TResult], ) -> System.Threading.Tasks.Task[TResult]:
        ...

    def GetAwaiter(self, ) -> System.Runtime.CompilerServices.ValueTaskAwaiter[TResult]:
        ...

    def ConfigureAwait(self, continueOnCapturedContext: bool, ) -> System.Runtime.CompilerServices.ConfiguredValueTaskAwaitable[TResult]:
        ...

    def ToString(self, ) -> str:
        ...

class UnobservedTaskExceptionEventArgs(System.EventArgs):
    @typing.overload
    def __init__(self, **kwargs):
        self.m_observed: bool
        ...

    # static fields

    # properties
    @property
    def Observed(self) -> bool:
        ...

    @property
    def Exception(self) -> System.AggregateException:
        ...

    # methods
    def __init__(self, exception: System.AggregateException, ):
        ...

    def SetObserved(self, ) -> None:
        ...

class TaskFactory(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def DefaultScheduler(self) -> System.Threading.Tasks.TaskScheduler:
        ...

    @property
    def CancellationToken(self) -> System.Threading.CancellationToken:
        ...

    @property
    def Scheduler(self) -> System.Threading.Tasks.TaskScheduler:
        ...

    @property
    def CreationOptions(self) -> int:
        ...

    @property
    def ContinuationOptions(self) -> int:
        ...

    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def __init__(self, cancellationToken: System.Threading.CancellationToken, ):
        ...

    @typing.overload
    def __init__(self, scheduler: System.Threading.Tasks.TaskScheduler, ):
        ...

    @typing.overload
    def __init__(self, creationOptions: int, continuationOptions: int, ):
        ...

    @typing.overload
    def __init__(self, cancellationToken: System.Threading.CancellationToken, creationOptions: int, continuationOptions: int, scheduler: System.Threading.Tasks.TaskScheduler, ):
        ...

    @typing.overload
    def ContinueWhenAll(self, tasks: System.Array[System.Threading.Tasks.Task], continuationFunction: System.Func[System.Array[System.Threading.Tasks.Task], TResult], continuationOptions: int, ) -> System.Threading.Tasks.Task[TResult]:
        ...

    @typing.overload
    def ContinueWhenAll(self, tasks: System.Array[System.Threading.Tasks.Task], continuationFunction: System.Func[System.Array[System.Threading.Tasks.Task], TResult], cancellationToken: System.Threading.CancellationToken, continuationOptions: int, scheduler: System.Threading.Tasks.TaskScheduler, ) -> System.Threading.Tasks.Task[TResult]:
        ...

    @typing.overload
    def ContinueWhenAll(self, tasks: System.Array[System.Threading.Tasks.Task[TAntecedentResult]], continuationFunction: System.Func[System.Array[System.Threading.Tasks.Task[TAntecedentResult]], TResult], ) -> System.Threading.Tasks.Task[TResult]:
        ...

    @typing.overload
    def ContinueWhenAll(self, tasks: System.Array[System.Threading.Tasks.Task[TAntecedentResult]], continuationFunction: System.Func[System.Array[System.Threading.Tasks.Task[TAntecedentResult]], TResult], cancellationToken: System.Threading.CancellationToken, ) -> System.Threading.Tasks.Task[TResult]:
        ...

    @typing.overload
    def ContinueWhenAll(self, tasks: System.Array[System.Threading.Tasks.Task[TAntecedentResult]], continuationFunction: System.Func[System.Array[System.Threading.Tasks.Task[TAntecedentResult]], TResult], continuationOptions: int, ) -> System.Threading.Tasks.Task[TResult]:
        ...

    @typing.overload
    def ContinueWhenAll(self, tasks: System.Array[System.Threading.Tasks.Task[TAntecedentResult]], continuationFunction: System.Func[System.Array[System.Threading.Tasks.Task[TAntecedentResult]], TResult], cancellationToken: System.Threading.CancellationToken, continuationOptions: int, scheduler: System.Threading.Tasks.TaskScheduler, ) -> System.Threading.Tasks.Task[TResult]:
        ...

    @typing.overload
    def ContinueWhenAll(self, tasks: System.Array[System.Threading.Tasks.Task], continuationAction: System.Action[System.Array[System.Threading.Tasks.Task]], ) -> System.Threading.Tasks.Task:
        ...

    @typing.overload
    def ContinueWhenAll(self, tasks: System.Array[System.Threading.Tasks.Task], continuationAction: System.Action[System.Array[System.Threading.Tasks.Task]], cancellationToken: System.Threading.CancellationToken, ) -> System.Threading.Tasks.Task:
        ...

    @typing.overload
    def ContinueWhenAll(self, tasks: System.Array[System.Threading.Tasks.Task], continuationAction: System.Action[System.Array[System.Threading.Tasks.Task]], continuationOptions: int, ) -> System.Threading.Tasks.Task:
        ...

    @typing.overload
    def ContinueWhenAll(self, tasks: System.Array[System.Threading.Tasks.Task], continuationAction: System.Action[System.Array[System.Threading.Tasks.Task]], cancellationToken: System.Threading.CancellationToken, continuationOptions: int, scheduler: System.Threading.Tasks.TaskScheduler, ) -> System.Threading.Tasks.Task:
        ...

    @typing.overload
    def ContinueWhenAll(self, tasks: System.Array[System.Threading.Tasks.Task[TAntecedentResult]], continuationAction: System.Action[System.Array[System.Threading.Tasks.Task[TAntecedentResult]]], ) -> System.Threading.Tasks.Task:
        ...

    @typing.overload
    def ContinueWhenAll(self, tasks: System.Array[System.Threading.Tasks.Task[TAntecedentResult]], continuationAction: System.Action[System.Array[System.Threading.Tasks.Task[TAntecedentResult]]], cancellationToken: System.Threading.CancellationToken, ) -> System.Threading.Tasks.Task:
        ...

    @typing.overload
    def ContinueWhenAll(self, tasks: System.Array[System.Threading.Tasks.Task[TAntecedentResult]], continuationAction: System.Action[System.Array[System.Threading.Tasks.Task[TAntecedentResult]]], continuationOptions: int, ) -> System.Threading.Tasks.Task:
        ...

    @typing.overload
    def ContinueWhenAll(self, tasks: System.Array[System.Threading.Tasks.Task[TAntecedentResult]], continuationAction: System.Action[System.Array[System.Threading.Tasks.Task[TAntecedentResult]]], cancellationToken: System.Threading.CancellationToken, continuationOptions: int, scheduler: System.Threading.Tasks.TaskScheduler, ) -> System.Threading.Tasks.Task:
        ...

    @typing.overload
    def ContinueWhenAll(self, tasks: System.Array[System.Threading.Tasks.Task], continuationFunction: System.Func[System.Array[System.Threading.Tasks.Task], TResult], ) -> System.Threading.Tasks.Task[TResult]:
        ...

    @typing.overload
    def ContinueWhenAll(self, tasks: System.Array[System.Threading.Tasks.Task], continuationFunction: System.Func[System.Array[System.Threading.Tasks.Task], TResult], cancellationToken: System.Threading.CancellationToken, ) -> System.Threading.Tasks.Task[TResult]:
        ...

    @staticmethod
    def CommonCWAnyLogic(tasks: System.Collections.Generic.IList[System.Threading.Tasks.Task], isSyncBlocking: bool = ..., ) -> System.Threading.Tasks.Task[System.Threading.Tasks.Task]:
        ...

    @staticmethod
    def CommonCWAnyLogicCleanup(continuation: System.Threading.Tasks.Task[System.Threading.Tasks.Task], ) -> None:
        ...

    @typing.overload
    def ContinueWhenAny(self, tasks: System.Array[System.Threading.Tasks.Task], continuationAction: System.Action[System.Threading.Tasks.Task], ) -> System.Threading.Tasks.Task:
        ...

    @typing.overload
    def ContinueWhenAny(self, tasks: System.Array[System.Threading.Tasks.Task], continuationAction: System.Action[System.Threading.Tasks.Task], cancellationToken: System.Threading.CancellationToken, ) -> System.Threading.Tasks.Task:
        ...

    @typing.overload
    def ContinueWhenAny(self, tasks: System.Array[System.Threading.Tasks.Task], continuationAction: System.Action[System.Threading.Tasks.Task], continuationOptions: int, ) -> System.Threading.Tasks.Task:
        ...

    @typing.overload
    def ContinueWhenAny(self, tasks: System.Array[System.Threading.Tasks.Task], continuationAction: System.Action[System.Threading.Tasks.Task], cancellationToken: System.Threading.CancellationToken, continuationOptions: int, scheduler: System.Threading.Tasks.TaskScheduler, ) -> System.Threading.Tasks.Task:
        ...

    @typing.overload
    def ContinueWhenAny(self, tasks: System.Array[System.Threading.Tasks.Task], continuationFunction: System.Func[System.Threading.Tasks.Task, TResult], ) -> System.Threading.Tasks.Task[TResult]:
        ...

    @typing.overload
    def ContinueWhenAny(self, tasks: System.Array[System.Threading.Tasks.Task], continuationFunction: System.Func[System.Threading.Tasks.Task, TResult], cancellationToken: System.Threading.CancellationToken, ) -> System.Threading.Tasks.Task[TResult]:
        ...

    @typing.overload
    def ContinueWhenAny(self, tasks: System.Array[System.Threading.Tasks.Task], continuationFunction: System.Func[System.Threading.Tasks.Task, TResult], continuationOptions: int, ) -> System.Threading.Tasks.Task[TResult]:
        ...

    @typing.overload
    def ContinueWhenAny(self, tasks: System.Array[System.Threading.Tasks.Task], continuationFunction: System.Func[System.Threading.Tasks.Task, TResult], cancellationToken: System.Threading.CancellationToken, continuationOptions: int, scheduler: System.Threading.Tasks.TaskScheduler, ) -> System.Threading.Tasks.Task[TResult]:
        ...

    @typing.overload
    def ContinueWhenAny(self, tasks: System.Array[System.Threading.Tasks.Task[TAntecedentResult]], continuationFunction: System.Func[System.Threading.Tasks.Task[TAntecedentResult], TResult], ) -> System.Threading.Tasks.Task[TResult]:
        ...

    @typing.overload
    def ContinueWhenAny(self, tasks: System.Array[System.Threading.Tasks.Task[TAntecedentResult]], continuationFunction: System.Func[System.Threading.Tasks.Task[TAntecedentResult], TResult], cancellationToken: System.Threading.CancellationToken, ) -> System.Threading.Tasks.Task[TResult]:
        ...

    @typing.overload
    def ContinueWhenAny(self, tasks: System.Array[System.Threading.Tasks.Task[TAntecedentResult]], continuationFunction: System.Func[System.Threading.Tasks.Task[TAntecedentResult], TResult], continuationOptions: int, ) -> System.Threading.Tasks.Task[TResult]:
        ...

    @typing.overload
    def ContinueWhenAny(self, tasks: System.Array[System.Threading.Tasks.Task[TAntecedentResult]], continuationFunction: System.Func[System.Threading.Tasks.Task[TAntecedentResult], TResult], cancellationToken: System.Threading.CancellationToken, continuationOptions: int, scheduler: System.Threading.Tasks.TaskScheduler, ) -> System.Threading.Tasks.Task[TResult]:
        ...

    @typing.overload
    def ContinueWhenAny(self, tasks: System.Array[System.Threading.Tasks.Task[TAntecedentResult]], continuationAction: System.Action[System.Threading.Tasks.Task[TAntecedentResult]], ) -> System.Threading.Tasks.Task:
        ...

    @typing.overload
    def ContinueWhenAny(self, tasks: System.Array[System.Threading.Tasks.Task[TAntecedentResult]], continuationAction: System.Action[System.Threading.Tasks.Task[TAntecedentResult]], cancellationToken: System.Threading.CancellationToken, ) -> System.Threading.Tasks.Task:
        ...

    @typing.overload
    def ContinueWhenAny(self, tasks: System.Array[System.Threading.Tasks.Task[TAntecedentResult]], continuationAction: System.Action[System.Threading.Tasks.Task[TAntecedentResult]], continuationOptions: int, ) -> System.Threading.Tasks.Task:
        ...

    @typing.overload
    def ContinueWhenAny(self, tasks: System.Array[System.Threading.Tasks.Task[TAntecedentResult]], continuationAction: System.Action[System.Threading.Tasks.Task[TAntecedentResult]], cancellationToken: System.Threading.CancellationToken, continuationOptions: int, scheduler: System.Threading.Tasks.TaskScheduler, ) -> System.Threading.Tasks.Task:
        ...

    @staticmethod
    @typing.overload
    def CheckMultiContinuationTasksAndCopy(tasks: System.Array[System.Threading.Tasks.Task], ) -> System.Array[System.Threading.Tasks.Task]:
        ...

    @staticmethod
    @typing.overload
    def CheckMultiContinuationTasksAndCopy(tasks: System.Array[System.Threading.Tasks.Task[TResult]], ) -> System.Array[System.Threading.Tasks.Task[TResult]]:
        ...

    @staticmethod
    def CheckMultiTaskContinuationOptions(continuationOptions: int, ) -> None:
        ...

    def GetDefaultScheduler(self, currTask: System.Threading.Tasks.Task, ) -> System.Threading.Tasks.TaskScheduler:
        ...

    @staticmethod
    def CheckCreationOptions(creationOptions: int, ) -> None:
        ...

    @typing.overload
    def StartNew(self, action: System.Action, ) -> System.Threading.Tasks.Task:
        ...

    @typing.overload
    def StartNew(self, action: System.Action, cancellationToken: System.Threading.CancellationToken, ) -> System.Threading.Tasks.Task:
        ...

    @typing.overload
    def StartNew(self, action: System.Action, creationOptions: int, ) -> System.Threading.Tasks.Task:
        ...

    @typing.overload
    def StartNew(self, action: System.Action, cancellationToken: System.Threading.CancellationToken, creationOptions: int, scheduler: System.Threading.Tasks.TaskScheduler, ) -> System.Threading.Tasks.Task:
        ...

    @typing.overload
    def StartNew(self, action: System.Action[System.Object], state: System.Object, ) -> System.Threading.Tasks.Task:
        ...

    @typing.overload
    def StartNew(self, action: System.Action[System.Object], state: System.Object, cancellationToken: System.Threading.CancellationToken, ) -> System.Threading.Tasks.Task:
        ...

    @typing.overload
    def StartNew(self, action: System.Action[System.Object], state: System.Object, creationOptions: int, ) -> System.Threading.Tasks.Task:
        ...

    @typing.overload
    def StartNew(self, action: System.Action[System.Object], state: System.Object, cancellationToken: System.Threading.CancellationToken, creationOptions: int, scheduler: System.Threading.Tasks.TaskScheduler, ) -> System.Threading.Tasks.Task:
        ...

    @typing.overload
    def StartNew(self, function: System.Func[TResult], ) -> System.Threading.Tasks.Task[TResult]:
        ...

    @typing.overload
    def StartNew(self, function: System.Func[TResult], cancellationToken: System.Threading.CancellationToken, ) -> System.Threading.Tasks.Task[TResult]:
        ...

    @typing.overload
    def StartNew(self, function: System.Func[TResult], creationOptions: int, ) -> System.Threading.Tasks.Task[TResult]:
        ...

    @typing.overload
    def StartNew(self, function: System.Func[TResult], cancellationToken: System.Threading.CancellationToken, creationOptions: int, scheduler: System.Threading.Tasks.TaskScheduler, ) -> System.Threading.Tasks.Task[TResult]:
        ...

    @typing.overload
    def StartNew(self, function: System.Func[System.Object, TResult], state: System.Object, ) -> System.Threading.Tasks.Task[TResult]:
        ...

    @typing.overload
    def StartNew(self, function: System.Func[System.Object, TResult], state: System.Object, cancellationToken: System.Threading.CancellationToken, ) -> System.Threading.Tasks.Task[TResult]:
        ...

    @typing.overload
    def StartNew(self, function: System.Func[System.Object, TResult], state: System.Object, creationOptions: int, ) -> System.Threading.Tasks.Task[TResult]:
        ...

    @typing.overload
    def StartNew(self, function: System.Func[System.Object, TResult], state: System.Object, cancellationToken: System.Threading.CancellationToken, creationOptions: int, scheduler: System.Threading.Tasks.TaskScheduler, ) -> System.Threading.Tasks.Task[TResult]:
        ...

    @typing.overload
    def FromAsync(self, asyncResult: System.IAsyncResult, endMethod: System.Action[System.IAsyncResult], ) -> System.Threading.Tasks.Task:
        ...

    @typing.overload
    def FromAsync(self, asyncResult: System.IAsyncResult, endMethod: System.Action[System.IAsyncResult], creationOptions: int, ) -> System.Threading.Tasks.Task:
        ...

    @typing.overload
    def FromAsync(self, asyncResult: System.IAsyncResult, endMethod: System.Action[System.IAsyncResult], creationOptions: int, scheduler: System.Threading.Tasks.TaskScheduler, ) -> System.Threading.Tasks.Task:
        ...

    @typing.overload
    def FromAsync(self, beginMethod: System.Func[System.AsyncCallback, System.Object, System.IAsyncResult], endMethod: System.Action[System.IAsyncResult], state: System.Object, ) -> System.Threading.Tasks.Task:
        ...

    @typing.overload
    def FromAsync(self, beginMethod: System.Func[System.AsyncCallback, System.Object, System.IAsyncResult], endMethod: System.Action[System.IAsyncResult], state: System.Object, creationOptions: int, ) -> System.Threading.Tasks.Task:
        ...

    @typing.overload
    def FromAsync(self, beginMethod: System.Func[TArg1, System.AsyncCallback, System.Object, System.IAsyncResult], endMethod: System.Action[System.IAsyncResult], arg1: TArg1, state: System.Object, ) -> System.Threading.Tasks.Task:
        ...

    @typing.overload
    def FromAsync(self, beginMethod: System.Func[TArg1, System.AsyncCallback, System.Object, System.IAsyncResult], endMethod: System.Action[System.IAsyncResult], arg1: TArg1, state: System.Object, creationOptions: int, ) -> System.Threading.Tasks.Task:
        ...

    @typing.overload
    def FromAsync(self, beginMethod: System.Func[TArg1, TArg2, System.AsyncCallback, System.Object, System.IAsyncResult], endMethod: System.Action[System.IAsyncResult], arg1: TArg1, arg2: TArg2, state: System.Object, ) -> System.Threading.Tasks.Task:
        ...

    @typing.overload
    def FromAsync(self, beginMethod: System.Func[TArg1, TArg2, System.AsyncCallback, System.Object, System.IAsyncResult], endMethod: System.Action[System.IAsyncResult], arg1: TArg1, arg2: TArg2, state: System.Object, creationOptions: int, ) -> System.Threading.Tasks.Task:
        ...

    @typing.overload
    def FromAsync(self, beginMethod: System.Func[TArg1, TArg2, TArg3, System.AsyncCallback, System.Object, System.IAsyncResult], endMethod: System.Action[System.IAsyncResult], arg1: TArg1, arg2: TArg2, arg3: TArg3, state: System.Object, ) -> System.Threading.Tasks.Task:
        ...

    @typing.overload
    def FromAsync(self, beginMethod: System.Func[TArg1, TArg2, TArg3, System.AsyncCallback, System.Object, System.IAsyncResult], endMethod: System.Action[System.IAsyncResult], arg1: TArg1, arg2: TArg2, arg3: TArg3, state: System.Object, creationOptions: int, ) -> System.Threading.Tasks.Task:
        ...

    @typing.overload
    def FromAsync(self, asyncResult: System.IAsyncResult, endMethod: System.Func[System.IAsyncResult, TResult], ) -> System.Threading.Tasks.Task[TResult]:
        ...

    @typing.overload
    def FromAsync(self, asyncResult: System.IAsyncResult, endMethod: System.Func[System.IAsyncResult, TResult], creationOptions: int, ) -> System.Threading.Tasks.Task[TResult]:
        ...

    @typing.overload
    def FromAsync(self, asyncResult: System.IAsyncResult, endMethod: System.Func[System.IAsyncResult, TResult], creationOptions: int, scheduler: System.Threading.Tasks.TaskScheduler, ) -> System.Threading.Tasks.Task[TResult]:
        ...

    @typing.overload
    def FromAsync(self, beginMethod: System.Func[System.AsyncCallback, System.Object, System.IAsyncResult], endMethod: System.Func[System.IAsyncResult, TResult], state: System.Object, ) -> System.Threading.Tasks.Task[TResult]:
        ...

    @typing.overload
    def FromAsync(self, beginMethod: System.Func[System.AsyncCallback, System.Object, System.IAsyncResult], endMethod: System.Func[System.IAsyncResult, TResult], state: System.Object, creationOptions: int, ) -> System.Threading.Tasks.Task[TResult]:
        ...

    @typing.overload
    def FromAsync(self, beginMethod: System.Func[TArg1, System.AsyncCallback, System.Object, System.IAsyncResult], endMethod: System.Func[System.IAsyncResult, TResult], arg1: TArg1, state: System.Object, ) -> System.Threading.Tasks.Task[TResult]:
        ...

    @typing.overload
    def FromAsync(self, beginMethod: System.Func[TArg1, System.AsyncCallback, System.Object, System.IAsyncResult], endMethod: System.Func[System.IAsyncResult, TResult], arg1: TArg1, state: System.Object, creationOptions: int, ) -> System.Threading.Tasks.Task[TResult]:
        ...

    @typing.overload
    def FromAsync(self, beginMethod: System.Func[TArg1, TArg2, System.AsyncCallback, System.Object, System.IAsyncResult], endMethod: System.Func[System.IAsyncResult, TResult], arg1: TArg1, arg2: TArg2, state: System.Object, ) -> System.Threading.Tasks.Task[TResult]:
        ...

    @typing.overload
    def FromAsync(self, beginMethod: System.Func[TArg1, TArg2, System.AsyncCallback, System.Object, System.IAsyncResult], endMethod: System.Func[System.IAsyncResult, TResult], arg1: TArg1, arg2: TArg2, state: System.Object, creationOptions: int, ) -> System.Threading.Tasks.Task[TResult]:
        ...

    @typing.overload
    def FromAsync(self, beginMethod: System.Func[TArg1, TArg2, TArg3, System.AsyncCallback, System.Object, System.IAsyncResult], endMethod: System.Func[System.IAsyncResult, TResult], arg1: TArg1, arg2: TArg2, arg3: TArg3, state: System.Object, ) -> System.Threading.Tasks.Task[TResult]:
        ...

    @typing.overload
    def FromAsync(self, beginMethod: System.Func[TArg1, TArg2, TArg3, System.AsyncCallback, System.Object, System.IAsyncResult], endMethod: System.Func[System.IAsyncResult, TResult], arg1: TArg1, arg2: TArg2, arg3: TArg3, state: System.Object, creationOptions: int, ) -> System.Threading.Tasks.Task[TResult]:
        ...

    @staticmethod
    def CheckFromAsyncOptions(creationOptions: int, hasBeginMethod: bool, ) -> None:
        ...

    @staticmethod
    @typing.overload
    def CommonCWAllLogic(tasksCopy: System.Array[System.Threading.Tasks.Task], ) -> System.Threading.Tasks.Task[System.Array[System.Threading.Tasks.Task]]:
        ...

    @staticmethod
    @typing.overload
    def CommonCWAllLogic(tasksCopy: System.Array[System.Threading.Tasks.Task[T]], ) -> System.Threading.Tasks.Task[System.Array[System.Threading.Tasks.Task[T]]]:
        ...

class TaskFactory(System.Object, typing.Generic[TResult]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def DefaultScheduler(self) -> System.Threading.Tasks.TaskScheduler:
        ...

    @property
    def CancellationToken(self) -> System.Threading.CancellationToken:
        ...

    @property
    def Scheduler(self) -> System.Threading.Tasks.TaskScheduler:
        ...

    @property
    def CreationOptions(self) -> int:
        ...

    @property
    def ContinuationOptions(self) -> int:
        ...

    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def __init__(self, cancellationToken: System.Threading.CancellationToken, ):
        ...

    @typing.overload
    def __init__(self, scheduler: System.Threading.Tasks.TaskScheduler, ):
        ...

    @typing.overload
    def __init__(self, creationOptions: int, continuationOptions: int, ):
        ...

    @typing.overload
    def __init__(self, cancellationToken: System.Threading.CancellationToken, creationOptions: int, continuationOptions: int, scheduler: System.Threading.Tasks.TaskScheduler, ):
        ...

    def GetDefaultScheduler(self, currTask: System.Threading.Tasks.Task, ) -> System.Threading.Tasks.TaskScheduler:
        ...

    @typing.overload
    def StartNew(self, function: System.Func[TResult], ) -> System.Threading.Tasks.Task[TResult]:
        ...

    @typing.overload
    def StartNew(self, function: System.Func[TResult], cancellationToken: System.Threading.CancellationToken, ) -> System.Threading.Tasks.Task[TResult]:
        ...

    @typing.overload
    def StartNew(self, function: System.Func[TResult], creationOptions: int, ) -> System.Threading.Tasks.Task[TResult]:
        ...

    @typing.overload
    def StartNew(self, function: System.Func[TResult], cancellationToken: System.Threading.CancellationToken, creationOptions: int, scheduler: System.Threading.Tasks.TaskScheduler, ) -> System.Threading.Tasks.Task[TResult]:
        ...

    @typing.overload
    def StartNew(self, function: System.Func[System.Object, TResult], state: System.Object, ) -> System.Threading.Tasks.Task[TResult]:
        ...

    @typing.overload
    def StartNew(self, function: System.Func[System.Object, TResult], state: System.Object, cancellationToken: System.Threading.CancellationToken, ) -> System.Threading.Tasks.Task[TResult]:
        ...

    @typing.overload
    def StartNew(self, function: System.Func[System.Object, TResult], state: System.Object, creationOptions: int, ) -> System.Threading.Tasks.Task[TResult]:
        ...

    @typing.overload
    def StartNew(self, function: System.Func[System.Object, TResult], state: System.Object, cancellationToken: System.Threading.CancellationToken, creationOptions: int, scheduler: System.Threading.Tasks.TaskScheduler, ) -> System.Threading.Tasks.Task[TResult]:
        ...

    @staticmethod
    def FromAsyncCoreLogic(iar: System.IAsyncResult, endFunction: System.Func[System.IAsyncResult, TResult], endAction: System.Action[System.IAsyncResult], promise: System.Threading.Tasks.Task[TResult], requiresSynchronization: bool, ) -> None:
        ...

    @typing.overload
    def FromAsync(self, asyncResult: System.IAsyncResult, endMethod: System.Func[System.IAsyncResult, TResult], ) -> System.Threading.Tasks.Task[TResult]:
        ...

    @typing.overload
    def FromAsync(self, asyncResult: System.IAsyncResult, endMethod: System.Func[System.IAsyncResult, TResult], creationOptions: int, ) -> System.Threading.Tasks.Task[TResult]:
        ...

    @typing.overload
    def FromAsync(self, asyncResult: System.IAsyncResult, endMethod: System.Func[System.IAsyncResult, TResult], creationOptions: int, scheduler: System.Threading.Tasks.TaskScheduler, ) -> System.Threading.Tasks.Task[TResult]:
        ...

    @typing.overload
    def FromAsync(self, beginMethod: System.Func[System.AsyncCallback, System.Object, System.IAsyncResult], endMethod: System.Func[System.IAsyncResult, TResult], state: System.Object, ) -> System.Threading.Tasks.Task[TResult]:
        ...

    @typing.overload
    def FromAsync(self, beginMethod: System.Func[System.AsyncCallback, System.Object, System.IAsyncResult], endMethod: System.Func[System.IAsyncResult, TResult], state: System.Object, creationOptions: int, ) -> System.Threading.Tasks.Task[TResult]:
        ...

    @typing.overload
    def FromAsync(self, beginMethod: System.Func[TArg1, System.AsyncCallback, System.Object, System.IAsyncResult], endMethod: System.Func[System.IAsyncResult, TResult], arg1: TArg1, state: System.Object, ) -> System.Threading.Tasks.Task[TResult]:
        ...

    @typing.overload
    def FromAsync(self, beginMethod: System.Func[TArg1, System.AsyncCallback, System.Object, System.IAsyncResult], endMethod: System.Func[System.IAsyncResult, TResult], arg1: TArg1, state: System.Object, creationOptions: int, ) -> System.Threading.Tasks.Task[TResult]:
        ...

    @typing.overload
    def FromAsync(self, beginMethod: System.Func[TArg1, TArg2, System.AsyncCallback, System.Object, System.IAsyncResult], endMethod: System.Func[System.IAsyncResult, TResult], arg1: TArg1, arg2: TArg2, state: System.Object, ) -> System.Threading.Tasks.Task[TResult]:
        ...

    @typing.overload
    def FromAsync(self, beginMethod: System.Func[TArg1, TArg2, System.AsyncCallback, System.Object, System.IAsyncResult], endMethod: System.Func[System.IAsyncResult, TResult], arg1: TArg1, arg2: TArg2, state: System.Object, creationOptions: int, ) -> System.Threading.Tasks.Task[TResult]:
        ...

    @typing.overload
    def FromAsync(self, beginMethod: System.Func[TArg1, TArg2, TArg3, System.AsyncCallback, System.Object, System.IAsyncResult], endMethod: System.Func[System.IAsyncResult, TResult], arg1: TArg1, arg2: TArg2, arg3: TArg3, state: System.Object, ) -> System.Threading.Tasks.Task[TResult]:
        ...

    @typing.overload
    def FromAsync(self, beginMethod: System.Func[TArg1, TArg2, TArg3, System.AsyncCallback, System.Object, System.IAsyncResult], endMethod: System.Func[System.IAsyncResult, TResult], arg1: TArg1, arg2: TArg2, arg3: TArg3, state: System.Object, creationOptions: int, ) -> System.Threading.Tasks.Task[TResult]:
        ...

    @staticmethod
    @typing.overload
    def FromAsyncImpl(asyncResult: System.IAsyncResult, endFunction: System.Func[System.IAsyncResult, TResult], endAction: System.Action[System.IAsyncResult], creationOptions: int, scheduler: System.Threading.Tasks.TaskScheduler, ) -> System.Threading.Tasks.Task[TResult]:
        ...

    @staticmethod
    @typing.overload
    def FromAsyncImpl(beginMethod: System.Func[System.AsyncCallback, System.Object, System.IAsyncResult], endFunction: System.Func[System.IAsyncResult, TResult], endAction: System.Action[System.IAsyncResult], state: System.Object, creationOptions: int, ) -> System.Threading.Tasks.Task[TResult]:
        ...

    @staticmethod
    @typing.overload
    def FromAsyncImpl(beginMethod: System.Func[TArg1, System.AsyncCallback, System.Object, System.IAsyncResult], endFunction: System.Func[System.IAsyncResult, TResult], endAction: System.Action[System.IAsyncResult], arg1: TArg1, state: System.Object, creationOptions: int, ) -> System.Threading.Tasks.Task[TResult]:
        ...

    @staticmethod
    @typing.overload
    def FromAsyncImpl(beginMethod: System.Func[TArg1, TArg2, System.AsyncCallback, System.Object, System.IAsyncResult], endFunction: System.Func[System.IAsyncResult, TResult], endAction: System.Action[System.IAsyncResult], arg1: TArg1, arg2: TArg2, state: System.Object, creationOptions: int, ) -> System.Threading.Tasks.Task[TResult]:
        ...

    @staticmethod
    @typing.overload
    def FromAsyncImpl(beginMethod: System.Func[TArg1, TArg2, TArg3, System.AsyncCallback, System.Object, System.IAsyncResult], endFunction: System.Func[System.IAsyncResult, TResult], endAction: System.Action[System.IAsyncResult], arg1: TArg1, arg2: TArg2, arg3: TArg3, state: System.Object, creationOptions: int, ) -> System.Threading.Tasks.Task[TResult]:
        ...

    @staticmethod
    def FromAsyncTrim(thisRef: TInstance, args: TArgs, beginMethod: System.Func[TInstance, TArgs, System.AsyncCallback, System.Object, System.IAsyncResult], endMethod: System.Func[TInstance, System.IAsyncResult, TResult], ) -> System.Threading.Tasks.Task[TResult]:
        ...

    @staticmethod
    def CreateCanceledTask(continuationOptions: int, ct: System.Threading.CancellationToken, ) -> System.Threading.Tasks.Task[TResult]:
        ...

    @typing.overload
    def ContinueWhenAll(self, tasks: System.Array[System.Threading.Tasks.Task], continuationFunction: System.Func[System.Array[System.Threading.Tasks.Task], TResult], ) -> System.Threading.Tasks.Task[TResult]:
        ...

    @typing.overload
    def ContinueWhenAll(self, tasks: System.Array[System.Threading.Tasks.Task], continuationFunction: System.Func[System.Array[System.Threading.Tasks.Task], TResult], cancellationToken: System.Threading.CancellationToken, ) -> System.Threading.Tasks.Task[TResult]:
        ...

    @typing.overload
    def ContinueWhenAll(self, tasks: System.Array[System.Threading.Tasks.Task], continuationFunction: System.Func[System.Array[System.Threading.Tasks.Task], TResult], continuationOptions: int, ) -> System.Threading.Tasks.Task[TResult]:
        ...

    @typing.overload
    def ContinueWhenAll(self, tasks: System.Array[System.Threading.Tasks.Task], continuationFunction: System.Func[System.Array[System.Threading.Tasks.Task], TResult], cancellationToken: System.Threading.CancellationToken, continuationOptions: int, scheduler: System.Threading.Tasks.TaskScheduler, ) -> System.Threading.Tasks.Task[TResult]:
        ...

    @typing.overload
    def ContinueWhenAll(self, tasks: System.Array[System.Threading.Tasks.Task[TAntecedentResult]], continuationFunction: System.Func[System.Array[System.Threading.Tasks.Task[TAntecedentResult]], TResult], ) -> System.Threading.Tasks.Task[TResult]:
        ...

    @typing.overload
    def ContinueWhenAll(self, tasks: System.Array[System.Threading.Tasks.Task[TAntecedentResult]], continuationFunction: System.Func[System.Array[System.Threading.Tasks.Task[TAntecedentResult]], TResult], cancellationToken: System.Threading.CancellationToken, ) -> System.Threading.Tasks.Task[TResult]:
        ...

    @typing.overload
    def ContinueWhenAll(self, tasks: System.Array[System.Threading.Tasks.Task[TAntecedentResult]], continuationFunction: System.Func[System.Array[System.Threading.Tasks.Task[TAntecedentResult]], TResult], continuationOptions: int, ) -> System.Threading.Tasks.Task[TResult]:
        ...

    @typing.overload
    def ContinueWhenAll(self, tasks: System.Array[System.Threading.Tasks.Task[TAntecedentResult]], continuationFunction: System.Func[System.Array[System.Threading.Tasks.Task[TAntecedentResult]], TResult], cancellationToken: System.Threading.CancellationToken, continuationOptions: int, scheduler: System.Threading.Tasks.TaskScheduler, ) -> System.Threading.Tasks.Task[TResult]:
        ...

    @staticmethod
    @typing.overload
    def ContinueWhenAllImpl(tasks: System.Array[System.Threading.Tasks.Task[TAntecedentResult]], continuationFunction: System.Func[System.Array[System.Threading.Tasks.Task[TAntecedentResult]], TResult], continuationAction: System.Action[System.Array[System.Threading.Tasks.Task[TAntecedentResult]]], continuationOptions: int, cancellationToken: System.Threading.CancellationToken, scheduler: System.Threading.Tasks.TaskScheduler, ) -> System.Threading.Tasks.Task[TResult]:
        ...

    @staticmethod
    @typing.overload
    def ContinueWhenAllImpl(tasks: System.Array[System.Threading.Tasks.Task], continuationFunction: System.Func[System.Array[System.Threading.Tasks.Task], TResult], continuationAction: System.Action[System.Array[System.Threading.Tasks.Task]], continuationOptions: int, cancellationToken: System.Threading.CancellationToken, scheduler: System.Threading.Tasks.TaskScheduler, ) -> System.Threading.Tasks.Task[TResult]:
        ...

    @typing.overload
    def ContinueWhenAny(self, tasks: System.Array[System.Threading.Tasks.Task], continuationFunction: System.Func[System.Threading.Tasks.Task, TResult], ) -> System.Threading.Tasks.Task[TResult]:
        ...

    @typing.overload
    def ContinueWhenAny(self, tasks: System.Array[System.Threading.Tasks.Task], continuationFunction: System.Func[System.Threading.Tasks.Task, TResult], cancellationToken: System.Threading.CancellationToken, ) -> System.Threading.Tasks.Task[TResult]:
        ...

    @typing.overload
    def ContinueWhenAny(self, tasks: System.Array[System.Threading.Tasks.Task], continuationFunction: System.Func[System.Threading.Tasks.Task, TResult], continuationOptions: int, ) -> System.Threading.Tasks.Task[TResult]:
        ...

    @typing.overload
    def ContinueWhenAny(self, tasks: System.Array[System.Threading.Tasks.Task], continuationFunction: System.Func[System.Threading.Tasks.Task, TResult], cancellationToken: System.Threading.CancellationToken, continuationOptions: int, scheduler: System.Threading.Tasks.TaskScheduler, ) -> System.Threading.Tasks.Task[TResult]:
        ...

    @typing.overload
    def ContinueWhenAny(self, tasks: System.Array[System.Threading.Tasks.Task[TAntecedentResult]], continuationFunction: System.Func[System.Threading.Tasks.Task[TAntecedentResult], TResult], ) -> System.Threading.Tasks.Task[TResult]:
        ...

    @typing.overload
    def ContinueWhenAny(self, tasks: System.Array[System.Threading.Tasks.Task[TAntecedentResult]], continuationFunction: System.Func[System.Threading.Tasks.Task[TAntecedentResult], TResult], cancellationToken: System.Threading.CancellationToken, ) -> System.Threading.Tasks.Task[TResult]:
        ...

    @typing.overload
    def ContinueWhenAny(self, tasks: System.Array[System.Threading.Tasks.Task[TAntecedentResult]], continuationFunction: System.Func[System.Threading.Tasks.Task[TAntecedentResult], TResult], continuationOptions: int, ) -> System.Threading.Tasks.Task[TResult]:
        ...

    @typing.overload
    def ContinueWhenAny(self, tasks: System.Array[System.Threading.Tasks.Task[TAntecedentResult]], continuationFunction: System.Func[System.Threading.Tasks.Task[TAntecedentResult], TResult], cancellationToken: System.Threading.CancellationToken, continuationOptions: int, scheduler: System.Threading.Tasks.TaskScheduler, ) -> System.Threading.Tasks.Task[TResult]:
        ...

    @staticmethod
    @typing.overload
    def ContinueWhenAnyImpl(tasks: System.Array[System.Threading.Tasks.Task], continuationFunction: System.Func[System.Threading.Tasks.Task, TResult], continuationAction: System.Action[System.Threading.Tasks.Task], continuationOptions: int, cancellationToken: System.Threading.CancellationToken, scheduler: System.Threading.Tasks.TaskScheduler, ) -> System.Threading.Tasks.Task[TResult]:
        ...

    @staticmethod
    @typing.overload
    def ContinueWhenAnyImpl(tasks: System.Array[System.Threading.Tasks.Task[TAntecedentResult]], continuationFunction: System.Func[System.Threading.Tasks.Task[TAntecedentResult], TResult], continuationAction: System.Action[System.Threading.Tasks.Task[TAntecedentResult]], continuationOptions: int, cancellationToken: System.Threading.CancellationToken, scheduler: System.Threading.Tasks.TaskScheduler, ) -> System.Threading.Tasks.Task[TResult]:
        ...

class TaskCreationOptions(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    None_: int = ...
    PreferFairness: int = ...
    LongRunning: int = ...
    AttachedToParent: int = ...
    DenyChildAttach: int = ...
    HideScheduler: int = ...
    RunContinuationsAsynchronously: int = ...

class TaskStatus(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    Created: int = ...
    WaitingForActivation: int = ...
    WaitingToRun: int = ...
    Running: int = ...
    WaitingForChildrenToComplete: int = ...
    RanToCompletion: int = ...
    Canceled: int = ...
    Faulted: int = ...

