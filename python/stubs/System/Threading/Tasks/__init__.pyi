from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import System
import System.Threading.Tasks
import System.Threading
import System.Collections.Generic
import System.Runtime.CompilerServices
import System.Threading.Tasks.Sources

TResult = typing.TypeVar('TResult')
TAntecedentResult = typing.TypeVar('TAntecedentResult')
TArg1 = typing.TypeVar('TArg1')
TArg2 = typing.TypeVar('TArg2')
TArg3 = typing.TypeVar('TArg3')
TNewResult = typing.TypeVar('TNewResult')

class Task(System.IAsyncResult, System.IDisposable, System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def Id(self) -> System.Int32:
        ...

    @property
    def CurrentId(self) -> System.Nullable[System.Int32]:
        ...

    @property
    def Exception(self) -> System.AggregateException:
        ...

    @property
    def Status(self) -> System.Threading.Tasks.TaskStatus:
        ...

    @property
    def IsCanceled(self) -> System.Boolean:
        ...

    @property
    def IsCompleted(self) -> System.Boolean:
        ...

    @property
    def IsCompletedSuccessfully(self) -> System.Boolean:
        ...

    @property
    def CreationOptions(self) -> System.Threading.Tasks.TaskCreationOptions:
        ...

    @property
    def AsyncState(self) -> System.Object:
        ...

    @property
    def Factory(self) -> System.Threading.Tasks.TaskFactory:
        ...

    @property
    def CompletedTask(self) -> System.Threading.Tasks.Task:
        ...

    @property
    def IsFaulted(self) -> System.Boolean:
        ...

    # methods
    @typing.overload
    def __init__(self, action: System.Action, ):
        ...

    @typing.overload
    def __init__(self, action: System.Action, cancellationToken: System.Threading.CancellationToken, ):
        ...

    @typing.overload
    def __init__(self, action: System.Action, creationOptions: System.Threading.Tasks.TaskCreationOptions, ):
        ...

    @typing.overload
    def __init__(self, action: System.Action, cancellationToken: System.Threading.CancellationToken, creationOptions: System.Threading.Tasks.TaskCreationOptions, ):
        ...

    @typing.overload
    def __init__(self, action: System.Action[System.Object], state: System.Object, ):
        ...

    @typing.overload
    def __init__(self, action: System.Action[System.Object], state: System.Object, cancellationToken: System.Threading.CancellationToken, ):
        ...

    @typing.overload
    def __init__(self, action: System.Action[System.Object], state: System.Object, creationOptions: System.Threading.Tasks.TaskCreationOptions, ):
        ...

    @typing.overload
    def __init__(self, action: System.Action[System.Object], state: System.Object, cancellationToken: System.Threading.CancellationToken, creationOptions: System.Threading.Tasks.TaskCreationOptions, ):
        ...

    @typing.overload
    @staticmethod
    def WaitAll(tasks: list[System.Threading.Tasks.Task], millisecondsTimeout: System.Int32, ) -> System.Boolean:
        ...

    @typing.overload
    @staticmethod
    def WaitAll(tasks: list[System.Threading.Tasks.Task], cancellationToken: System.Threading.CancellationToken, ) -> None:
        ...

    @typing.overload
    @staticmethod
    def WaitAll(tasks: list[System.Threading.Tasks.Task], millisecondsTimeout: System.Int32, cancellationToken: System.Threading.CancellationToken, ) -> System.Boolean:
        ...

    @typing.overload
    @staticmethod
    def WaitAny(tasks: list[System.Threading.Tasks.Task], ) -> System.Int32:
        ...

    @typing.overload
    @staticmethod
    def WaitAny(tasks: list[System.Threading.Tasks.Task], timeout: System.TimeSpan, ) -> System.Int32:
        ...

    @typing.overload
    @staticmethod
    def WaitAny(tasks: list[System.Threading.Tasks.Task], cancellationToken: System.Threading.CancellationToken, ) -> System.Int32:
        ...

    @typing.overload
    @staticmethod
    def WaitAny(tasks: list[System.Threading.Tasks.Task], millisecondsTimeout: System.Int32, ) -> System.Int32:
        ...

    @typing.overload
    @staticmethod
    def WaitAny(tasks: list[System.Threading.Tasks.Task], millisecondsTimeout: System.Int32, cancellationToken: System.Threading.CancellationToken, ) -> System.Int32:
        ...

    @typing.overload
    @staticmethod
    def FromResult(result: TResult, ) -> System.Threading.Tasks.Task[TResult]:
        ...

    @typing.overload
    @staticmethod
    def FromException(exception: System.Exception, ) -> System.Threading.Tasks.Task:
        ...

    @typing.overload
    @staticmethod
    def FromException(exception: System.Exception, ) -> System.Threading.Tasks.Task[TResult]:
        ...

    @typing.overload
    @staticmethod
    def FromCanceled(cancellationToken: System.Threading.CancellationToken, ) -> System.Threading.Tasks.Task:
        ...

    @typing.overload
    @staticmethod
    def FromCanceled(cancellationToken: System.Threading.CancellationToken, ) -> System.Threading.Tasks.Task[TResult]:
        ...

    @typing.overload
    @staticmethod
    def Run(action: System.Action, ) -> System.Threading.Tasks.Task:
        ...

    @typing.overload
    @staticmethod
    def Run(action: System.Action, cancellationToken: System.Threading.CancellationToken, ) -> System.Threading.Tasks.Task:
        ...

    @typing.overload
    @staticmethod
    def Run(function: System.Func[TResult], ) -> System.Threading.Tasks.Task[TResult]:
        ...

    @typing.overload
    @staticmethod
    def Run(function: System.Func[TResult], cancellationToken: System.Threading.CancellationToken, ) -> System.Threading.Tasks.Task[TResult]:
        ...

    @typing.overload
    @staticmethod
    def Run(function: System.Func[System.Threading.Tasks.Task], ) -> System.Threading.Tasks.Task:
        ...

    @typing.overload
    @staticmethod
    def Run(function: System.Func[System.Threading.Tasks.Task], cancellationToken: System.Threading.CancellationToken, ) -> System.Threading.Tasks.Task:
        ...

    @typing.overload
    @staticmethod
    def Run(function: System.Func[System.Threading.Tasks.Task[TResult]], ) -> System.Threading.Tasks.Task[TResult]:
        ...

    @typing.overload
    @staticmethod
    def Run(function: System.Func[System.Threading.Tasks.Task[TResult]], cancellationToken: System.Threading.CancellationToken, ) -> System.Threading.Tasks.Task[TResult]:
        ...

    @typing.overload
    @staticmethod
    def Delay(delay: System.TimeSpan, ) -> System.Threading.Tasks.Task:
        ...

    @typing.overload
    @staticmethod
    def Delay(delay: System.TimeSpan, cancellationToken: System.Threading.CancellationToken, ) -> System.Threading.Tasks.Task:
        ...

    @typing.overload
    @staticmethod
    def Delay(millisecondsDelay: System.Int32, ) -> System.Threading.Tasks.Task:
        ...

    @typing.overload
    @staticmethod
    def Delay(millisecondsDelay: System.Int32, cancellationToken: System.Threading.CancellationToken, ) -> System.Threading.Tasks.Task:
        ...

    @typing.overload
    @staticmethod
    def WhenAll(tasks: System.Collections.Generic.IEnumerable[System.Threading.Tasks.Task], ) -> System.Threading.Tasks.Task:
        ...

    @typing.overload
    @staticmethod
    def WhenAll(tasks: list[System.Threading.Tasks.Task], ) -> System.Threading.Tasks.Task:
        ...

    @typing.overload
    @staticmethod
    def WhenAll(tasks: System.Collections.Generic.IEnumerable[System.Threading.Tasks.Task[TResult]], ) -> System.Threading.Tasks.Task[list[TResult]]:
        ...

    @typing.overload
    @staticmethod
    def WhenAll(tasks: list[System.Threading.Tasks.Task[TResult]], ) -> System.Threading.Tasks.Task[list[TResult]]:
        ...

    @typing.overload
    @staticmethod
    def WhenAny(tasks: list[System.Threading.Tasks.Task], ) -> System.Threading.Tasks.Task[System.Threading.Tasks.Task]:
        ...

    @typing.overload
    @staticmethod
    def WhenAny(task1: System.Threading.Tasks.Task, task2: System.Threading.Tasks.Task, ) -> System.Threading.Tasks.Task[System.Threading.Tasks.Task]:
        ...

    @typing.overload
    @staticmethod
    def WhenAny(tasks: System.Collections.Generic.IEnumerable[System.Threading.Tasks.Task], ) -> System.Threading.Tasks.Task[System.Threading.Tasks.Task]:
        ...

    @typing.overload
    @staticmethod
    def WhenAny(tasks: list[System.Threading.Tasks.Task[TResult]], ) -> System.Threading.Tasks.Task[System.Threading.Tasks.Task[TResult]]:
        ...

    @typing.overload
    @staticmethod
    def WhenAny(task1: System.Threading.Tasks.Task[TResult], task2: System.Threading.Tasks.Task[TResult], ) -> System.Threading.Tasks.Task[System.Threading.Tasks.Task[TResult]]:
        ...

    @typing.overload
    @staticmethod
    def WhenAny(tasks: System.Collections.Generic.IEnumerable[System.Threading.Tasks.Task[TResult]], ) -> System.Threading.Tasks.Task[System.Threading.Tasks.Task[TResult]]:
        ...

    @typing.overload
    def GetAwaiter(self, ) -> System.Runtime.CompilerServices.TaskAwaiter:
        ...

    @typing.overload
    def ConfigureAwait(self, continueOnCapturedContext: System.Boolean, ) -> System.Runtime.CompilerServices.ConfiguredTaskAwaitable:
        ...

    @typing.overload
    @staticmethod
    def Yield() -> System.Runtime.CompilerServices.YieldAwaitable:
        ...

    @typing.overload
    def Wait(self, ) -> None:
        ...

    @typing.overload
    def Wait(self, timeout: System.TimeSpan, ) -> System.Boolean:
        ...

    @typing.overload
    def Wait(self, cancellationToken: System.Threading.CancellationToken, ) -> None:
        ...

    @typing.overload
    def Wait(self, millisecondsTimeout: System.Int32, ) -> System.Boolean:
        ...

    @typing.overload
    def Wait(self, millisecondsTimeout: System.Int32, cancellationToken: System.Threading.CancellationToken, ) -> System.Boolean:
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
    def ContinueWith(self, continuationAction: System.Action[System.Threading.Tasks.Task], ) -> System.Threading.Tasks.Task:
        ...

    @typing.overload
    def ContinueWith(self, continuationAction: System.Action[System.Threading.Tasks.Task], cancellationToken: System.Threading.CancellationToken, ) -> System.Threading.Tasks.Task:
        ...

    @typing.overload
    def ContinueWith(self, continuationAction: System.Action[System.Threading.Tasks.Task], scheduler: System.Threading.Tasks.TaskScheduler, ) -> System.Threading.Tasks.Task:
        ...

    @typing.overload
    def ContinueWith(self, continuationAction: System.Action[System.Threading.Tasks.Task], continuationOptions: System.Threading.Tasks.TaskContinuationOptions, ) -> System.Threading.Tasks.Task:
        ...

    @typing.overload
    def ContinueWith(self, continuationAction: System.Action[System.Threading.Tasks.Task], cancellationToken: System.Threading.CancellationToken, continuationOptions: System.Threading.Tasks.TaskContinuationOptions, scheduler: System.Threading.Tasks.TaskScheduler, ) -> System.Threading.Tasks.Task:
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
    def ContinueWith(self, continuationAction: System.Action[System.Threading.Tasks.Task, System.Object], state: System.Object, continuationOptions: System.Threading.Tasks.TaskContinuationOptions, ) -> System.Threading.Tasks.Task:
        ...

    @typing.overload
    def ContinueWith(self, continuationAction: System.Action[System.Threading.Tasks.Task, System.Object], state: System.Object, cancellationToken: System.Threading.CancellationToken, continuationOptions: System.Threading.Tasks.TaskContinuationOptions, scheduler: System.Threading.Tasks.TaskScheduler, ) -> System.Threading.Tasks.Task:
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
    def ContinueWith(self, continuationFunction: System.Func[System.Threading.Tasks.Task, TResult], continuationOptions: System.Threading.Tasks.TaskContinuationOptions, ) -> System.Threading.Tasks.Task[TResult]:
        ...

    @typing.overload
    def ContinueWith(self, continuationFunction: System.Func[System.Threading.Tasks.Task, TResult], cancellationToken: System.Threading.CancellationToken, continuationOptions: System.Threading.Tasks.TaskContinuationOptions, scheduler: System.Threading.Tasks.TaskScheduler, ) -> System.Threading.Tasks.Task[TResult]:
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
    def ContinueWith(self, continuationFunction: System.Func[System.Threading.Tasks.Task, System.Object, TResult], state: System.Object, continuationOptions: System.Threading.Tasks.TaskContinuationOptions, ) -> System.Threading.Tasks.Task[TResult]:
        ...

    @typing.overload
    def ContinueWith(self, continuationFunction: System.Func[System.Threading.Tasks.Task, System.Object, TResult], state: System.Object, cancellationToken: System.Threading.CancellationToken, continuationOptions: System.Threading.Tasks.TaskContinuationOptions, scheduler: System.Threading.Tasks.TaskScheduler, ) -> System.Threading.Tasks.Task[TResult]:
        ...

    @typing.overload
    @staticmethod
    def WaitAll(tasks: list[System.Threading.Tasks.Task], ) -> None:
        ...

    @typing.overload
    @staticmethod
    def WaitAll(tasks: list[System.Threading.Tasks.Task], timeout: System.TimeSpan, ) -> System.Boolean:
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

    @typing.overload
    def Dispose(self, ) -> None:
        ...

class TaskStatus(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    Created: System.Int32 = Created
    WaitingForActivation: System.Int32 = WaitingForActivation
    WaitingToRun: System.Int32 = WaitingToRun
    Running: System.Int32 = Running
    WaitingForChildrenToComplete: System.Int32 = WaitingForChildrenToComplete
    RanToCompletion: System.Int32 = RanToCompletion
    Canceled: System.Int32 = Canceled
    Faulted: System.Int32 = Faulted

class TaskCreationOptions(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    None_: System.Int32 = None
    PreferFairness: System.Int32 = PreferFairness
    LongRunning: System.Int32 = LongRunning
    AttachedToParent: System.Int32 = AttachedToParent
    DenyChildAttach: System.Int32 = DenyChildAttach
    HideScheduler: System.Int32 = HideScheduler
    RunContinuationsAsynchronously: System.Int32 = RunContinuationsAsynchronously

class TaskFactory(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def CancellationToken(self) -> System.Threading.CancellationToken:
        ...

    @property
    def Scheduler(self) -> System.Threading.Tasks.TaskScheduler:
        ...

    @property
    def CreationOptions(self) -> System.Threading.Tasks.TaskCreationOptions:
        ...

    @property
    def ContinuationOptions(self) -> System.Threading.Tasks.TaskContinuationOptions:
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
    def __init__(self, creationOptions: System.Threading.Tasks.TaskCreationOptions, continuationOptions: System.Threading.Tasks.TaskContinuationOptions, ):
        ...

    @typing.overload
    def __init__(self, cancellationToken: System.Threading.CancellationToken, creationOptions: System.Threading.Tasks.TaskCreationOptions, continuationOptions: System.Threading.Tasks.TaskContinuationOptions, scheduler: System.Threading.Tasks.TaskScheduler, ):
        ...

    @typing.overload
    def ContinueWhenAll(self, tasks: list[System.Threading.Tasks.Task], continuationFunction: System.Func[list[System.Threading.Tasks.Task], TResult], continuationOptions: System.Threading.Tasks.TaskContinuationOptions, ) -> System.Threading.Tasks.Task[TResult]:
        ...

    @typing.overload
    def ContinueWhenAll(self, tasks: list[System.Threading.Tasks.Task], continuationFunction: System.Func[list[System.Threading.Tasks.Task], TResult], cancellationToken: System.Threading.CancellationToken, continuationOptions: System.Threading.Tasks.TaskContinuationOptions, scheduler: System.Threading.Tasks.TaskScheduler, ) -> System.Threading.Tasks.Task[TResult]:
        ...

    @typing.overload
    def ContinueWhenAll(self, tasks: list[System.Threading.Tasks.Task[TAntecedentResult]], continuationFunction: System.Func[list[System.Threading.Tasks.Task[TAntecedentResult]], TResult], ) -> System.Threading.Tasks.Task[TResult]:
        ...

    @typing.overload
    def ContinueWhenAll(self, tasks: list[System.Threading.Tasks.Task[TAntecedentResult]], continuationFunction: System.Func[list[System.Threading.Tasks.Task[TAntecedentResult]], TResult], cancellationToken: System.Threading.CancellationToken, ) -> System.Threading.Tasks.Task[TResult]:
        ...

    @typing.overload
    def ContinueWhenAll(self, tasks: list[System.Threading.Tasks.Task[TAntecedentResult]], continuationFunction: System.Func[list[System.Threading.Tasks.Task[TAntecedentResult]], TResult], continuationOptions: System.Threading.Tasks.TaskContinuationOptions, ) -> System.Threading.Tasks.Task[TResult]:
        ...

    @typing.overload
    def ContinueWhenAll(self, tasks: list[System.Threading.Tasks.Task[TAntecedentResult]], continuationFunction: System.Func[list[System.Threading.Tasks.Task[TAntecedentResult]], TResult], cancellationToken: System.Threading.CancellationToken, continuationOptions: System.Threading.Tasks.TaskContinuationOptions, scheduler: System.Threading.Tasks.TaskScheduler, ) -> System.Threading.Tasks.Task[TResult]:
        ...

    @typing.overload
    def ContinueWhenAny(self, tasks: list[System.Threading.Tasks.Task], continuationAction: System.Action[System.Threading.Tasks.Task], ) -> System.Threading.Tasks.Task:
        ...

    @typing.overload
    def ContinueWhenAny(self, tasks: list[System.Threading.Tasks.Task], continuationAction: System.Action[System.Threading.Tasks.Task], cancellationToken: System.Threading.CancellationToken, ) -> System.Threading.Tasks.Task:
        ...

    @typing.overload
    def ContinueWhenAny(self, tasks: list[System.Threading.Tasks.Task], continuationAction: System.Action[System.Threading.Tasks.Task], continuationOptions: System.Threading.Tasks.TaskContinuationOptions, ) -> System.Threading.Tasks.Task:
        ...

    @typing.overload
    def ContinueWhenAny(self, tasks: list[System.Threading.Tasks.Task], continuationAction: System.Action[System.Threading.Tasks.Task], cancellationToken: System.Threading.CancellationToken, continuationOptions: System.Threading.Tasks.TaskContinuationOptions, scheduler: System.Threading.Tasks.TaskScheduler, ) -> System.Threading.Tasks.Task:
        ...

    @typing.overload
    def ContinueWhenAny(self, tasks: list[System.Threading.Tasks.Task], continuationFunction: System.Func[System.Threading.Tasks.Task, TResult], ) -> System.Threading.Tasks.Task[TResult]:
        ...

    @typing.overload
    def ContinueWhenAny(self, tasks: list[System.Threading.Tasks.Task], continuationFunction: System.Func[System.Threading.Tasks.Task, TResult], cancellationToken: System.Threading.CancellationToken, ) -> System.Threading.Tasks.Task[TResult]:
        ...

    @typing.overload
    def ContinueWhenAny(self, tasks: list[System.Threading.Tasks.Task], continuationFunction: System.Func[System.Threading.Tasks.Task, TResult], continuationOptions: System.Threading.Tasks.TaskContinuationOptions, ) -> System.Threading.Tasks.Task[TResult]:
        ...

    @typing.overload
    def ContinueWhenAny(self, tasks: list[System.Threading.Tasks.Task], continuationFunction: System.Func[System.Threading.Tasks.Task, TResult], cancellationToken: System.Threading.CancellationToken, continuationOptions: System.Threading.Tasks.TaskContinuationOptions, scheduler: System.Threading.Tasks.TaskScheduler, ) -> System.Threading.Tasks.Task[TResult]:
        ...

    @typing.overload
    def ContinueWhenAny(self, tasks: list[System.Threading.Tasks.Task[TAntecedentResult]], continuationFunction: System.Func[System.Threading.Tasks.Task[TAntecedentResult], TResult], ) -> System.Threading.Tasks.Task[TResult]:
        ...

    @typing.overload
    def ContinueWhenAny(self, tasks: list[System.Threading.Tasks.Task[TAntecedentResult]], continuationFunction: System.Func[System.Threading.Tasks.Task[TAntecedentResult], TResult], cancellationToken: System.Threading.CancellationToken, ) -> System.Threading.Tasks.Task[TResult]:
        ...

    @typing.overload
    def ContinueWhenAny(self, tasks: list[System.Threading.Tasks.Task[TAntecedentResult]], continuationFunction: System.Func[System.Threading.Tasks.Task[TAntecedentResult], TResult], continuationOptions: System.Threading.Tasks.TaskContinuationOptions, ) -> System.Threading.Tasks.Task[TResult]:
        ...

    @typing.overload
    def ContinueWhenAny(self, tasks: list[System.Threading.Tasks.Task[TAntecedentResult]], continuationFunction: System.Func[System.Threading.Tasks.Task[TAntecedentResult], TResult], cancellationToken: System.Threading.CancellationToken, continuationOptions: System.Threading.Tasks.TaskContinuationOptions, scheduler: System.Threading.Tasks.TaskScheduler, ) -> System.Threading.Tasks.Task[TResult]:
        ...

    @typing.overload
    def ContinueWhenAny(self, tasks: list[System.Threading.Tasks.Task[TAntecedentResult]], continuationAction: System.Action[System.Threading.Tasks.Task[TAntecedentResult]], ) -> System.Threading.Tasks.Task:
        ...

    @typing.overload
    def ContinueWhenAny(self, tasks: list[System.Threading.Tasks.Task[TAntecedentResult]], continuationAction: System.Action[System.Threading.Tasks.Task[TAntecedentResult]], cancellationToken: System.Threading.CancellationToken, ) -> System.Threading.Tasks.Task:
        ...

    @typing.overload
    def ContinueWhenAny(self, tasks: list[System.Threading.Tasks.Task[TAntecedentResult]], continuationAction: System.Action[System.Threading.Tasks.Task[TAntecedentResult]], continuationOptions: System.Threading.Tasks.TaskContinuationOptions, ) -> System.Threading.Tasks.Task:
        ...

    @typing.overload
    def ContinueWhenAny(self, tasks: list[System.Threading.Tasks.Task[TAntecedentResult]], continuationAction: System.Action[System.Threading.Tasks.Task[TAntecedentResult]], cancellationToken: System.Threading.CancellationToken, continuationOptions: System.Threading.Tasks.TaskContinuationOptions, scheduler: System.Threading.Tasks.TaskScheduler, ) -> System.Threading.Tasks.Task:
        ...

    @typing.overload
    def StartNew(self, action: System.Action, ) -> System.Threading.Tasks.Task:
        ...

    @typing.overload
    def StartNew(self, action: System.Action, cancellationToken: System.Threading.CancellationToken, ) -> System.Threading.Tasks.Task:
        ...

    @typing.overload
    def StartNew(self, action: System.Action, creationOptions: System.Threading.Tasks.TaskCreationOptions, ) -> System.Threading.Tasks.Task:
        ...

    @typing.overload
    def StartNew(self, action: System.Action, cancellationToken: System.Threading.CancellationToken, creationOptions: System.Threading.Tasks.TaskCreationOptions, scheduler: System.Threading.Tasks.TaskScheduler, ) -> System.Threading.Tasks.Task:
        ...

    @typing.overload
    def StartNew(self, action: System.Action[System.Object], state: System.Object, ) -> System.Threading.Tasks.Task:
        ...

    @typing.overload
    def StartNew(self, action: System.Action[System.Object], state: System.Object, cancellationToken: System.Threading.CancellationToken, ) -> System.Threading.Tasks.Task:
        ...

    @typing.overload
    def StartNew(self, action: System.Action[System.Object], state: System.Object, creationOptions: System.Threading.Tasks.TaskCreationOptions, ) -> System.Threading.Tasks.Task:
        ...

    @typing.overload
    def StartNew(self, action: System.Action[System.Object], state: System.Object, cancellationToken: System.Threading.CancellationToken, creationOptions: System.Threading.Tasks.TaskCreationOptions, scheduler: System.Threading.Tasks.TaskScheduler, ) -> System.Threading.Tasks.Task:
        ...

    @typing.overload
    def StartNew(self, function: System.Func[TResult], ) -> System.Threading.Tasks.Task[TResult]:
        ...

    @typing.overload
    def StartNew(self, function: System.Func[TResult], cancellationToken: System.Threading.CancellationToken, ) -> System.Threading.Tasks.Task[TResult]:
        ...

    @typing.overload
    def StartNew(self, function: System.Func[TResult], creationOptions: System.Threading.Tasks.TaskCreationOptions, ) -> System.Threading.Tasks.Task[TResult]:
        ...

    @typing.overload
    def StartNew(self, function: System.Func[TResult], cancellationToken: System.Threading.CancellationToken, creationOptions: System.Threading.Tasks.TaskCreationOptions, scheduler: System.Threading.Tasks.TaskScheduler, ) -> System.Threading.Tasks.Task[TResult]:
        ...

    @typing.overload
    def StartNew(self, function: System.Func[System.Object, TResult], state: System.Object, ) -> System.Threading.Tasks.Task[TResult]:
        ...

    @typing.overload
    def StartNew(self, function: System.Func[System.Object, TResult], state: System.Object, cancellationToken: System.Threading.CancellationToken, ) -> System.Threading.Tasks.Task[TResult]:
        ...

    @typing.overload
    def StartNew(self, function: System.Func[System.Object, TResult], state: System.Object, creationOptions: System.Threading.Tasks.TaskCreationOptions, ) -> System.Threading.Tasks.Task[TResult]:
        ...

    @typing.overload
    def StartNew(self, function: System.Func[System.Object, TResult], state: System.Object, cancellationToken: System.Threading.CancellationToken, creationOptions: System.Threading.Tasks.TaskCreationOptions, scheduler: System.Threading.Tasks.TaskScheduler, ) -> System.Threading.Tasks.Task[TResult]:
        ...

    @typing.overload
    def FromAsync(self, asyncResult: System.IAsyncResult, endMethod: System.Action[System.IAsyncResult], ) -> System.Threading.Tasks.Task:
        ...

    @typing.overload
    def FromAsync(self, asyncResult: System.IAsyncResult, endMethod: System.Action[System.IAsyncResult], creationOptions: System.Threading.Tasks.TaskCreationOptions, ) -> System.Threading.Tasks.Task:
        ...

    @typing.overload
    def FromAsync(self, asyncResult: System.IAsyncResult, endMethod: System.Action[System.IAsyncResult], creationOptions: System.Threading.Tasks.TaskCreationOptions, scheduler: System.Threading.Tasks.TaskScheduler, ) -> System.Threading.Tasks.Task:
        ...

    @typing.overload
    def FromAsync(self, beginMethod: System.Func[System.AsyncCallback, System.Object, System.IAsyncResult], endMethod: System.Action[System.IAsyncResult], state: System.Object, ) -> System.Threading.Tasks.Task:
        ...

    @typing.overload
    def FromAsync(self, beginMethod: System.Func[System.AsyncCallback, System.Object, System.IAsyncResult], endMethod: System.Action[System.IAsyncResult], state: System.Object, creationOptions: System.Threading.Tasks.TaskCreationOptions, ) -> System.Threading.Tasks.Task:
        ...

    @typing.overload
    def FromAsync(self, beginMethod: System.Func[TArg1, System.AsyncCallback, System.Object, System.IAsyncResult], endMethod: System.Action[System.IAsyncResult], arg1: TArg1, state: System.Object, ) -> System.Threading.Tasks.Task:
        ...

    @typing.overload
    def FromAsync(self, beginMethod: System.Func[TArg1, System.AsyncCallback, System.Object, System.IAsyncResult], endMethod: System.Action[System.IAsyncResult], arg1: TArg1, state: System.Object, creationOptions: System.Threading.Tasks.TaskCreationOptions, ) -> System.Threading.Tasks.Task:
        ...

    @typing.overload
    def FromAsync(self, beginMethod: System.Func[TArg1, TArg2, System.AsyncCallback, System.Object, System.IAsyncResult], endMethod: System.Action[System.IAsyncResult], arg1: TArg1, arg2: TArg2, state: System.Object, ) -> System.Threading.Tasks.Task:
        ...

    @typing.overload
    def FromAsync(self, beginMethod: System.Func[TArg1, TArg2, System.AsyncCallback, System.Object, System.IAsyncResult], endMethod: System.Action[System.IAsyncResult], arg1: TArg1, arg2: TArg2, state: System.Object, creationOptions: System.Threading.Tasks.TaskCreationOptions, ) -> System.Threading.Tasks.Task:
        ...

    @typing.overload
    def FromAsync(self, beginMethod: System.Func[TArg1, TArg2, TArg3, System.AsyncCallback, System.Object, System.IAsyncResult], endMethod: System.Action[System.IAsyncResult], arg1: TArg1, arg2: TArg2, arg3: TArg3, state: System.Object, ) -> System.Threading.Tasks.Task:
        ...

    @typing.overload
    def FromAsync(self, beginMethod: System.Func[TArg1, TArg2, TArg3, System.AsyncCallback, System.Object, System.IAsyncResult], endMethod: System.Action[System.IAsyncResult], arg1: TArg1, arg2: TArg2, arg3: TArg3, state: System.Object, creationOptions: System.Threading.Tasks.TaskCreationOptions, ) -> System.Threading.Tasks.Task:
        ...

    @typing.overload
    def FromAsync(self, asyncResult: System.IAsyncResult, endMethod: System.Func[System.IAsyncResult, TResult], ) -> System.Threading.Tasks.Task[TResult]:
        ...

    @typing.overload
    def FromAsync(self, asyncResult: System.IAsyncResult, endMethod: System.Func[System.IAsyncResult, TResult], creationOptions: System.Threading.Tasks.TaskCreationOptions, ) -> System.Threading.Tasks.Task[TResult]:
        ...

    @typing.overload
    def FromAsync(self, asyncResult: System.IAsyncResult, endMethod: System.Func[System.IAsyncResult, TResult], creationOptions: System.Threading.Tasks.TaskCreationOptions, scheduler: System.Threading.Tasks.TaskScheduler, ) -> System.Threading.Tasks.Task[TResult]:
        ...

    @typing.overload
    def FromAsync(self, beginMethod: System.Func[System.AsyncCallback, System.Object, System.IAsyncResult], endMethod: System.Func[System.IAsyncResult, TResult], state: System.Object, ) -> System.Threading.Tasks.Task[TResult]:
        ...

    @typing.overload
    def FromAsync(self, beginMethod: System.Func[System.AsyncCallback, System.Object, System.IAsyncResult], endMethod: System.Func[System.IAsyncResult, TResult], state: System.Object, creationOptions: System.Threading.Tasks.TaskCreationOptions, ) -> System.Threading.Tasks.Task[TResult]:
        ...

    @typing.overload
    def FromAsync(self, beginMethod: System.Func[TArg1, System.AsyncCallback, System.Object, System.IAsyncResult], endMethod: System.Func[System.IAsyncResult, TResult], arg1: TArg1, state: System.Object, ) -> System.Threading.Tasks.Task[TResult]:
        ...

    @typing.overload
    def FromAsync(self, beginMethod: System.Func[TArg1, System.AsyncCallback, System.Object, System.IAsyncResult], endMethod: System.Func[System.IAsyncResult, TResult], arg1: TArg1, state: System.Object, creationOptions: System.Threading.Tasks.TaskCreationOptions, ) -> System.Threading.Tasks.Task[TResult]:
        ...

    @typing.overload
    def FromAsync(self, beginMethod: System.Func[TArg1, TArg2, System.AsyncCallback, System.Object, System.IAsyncResult], endMethod: System.Func[System.IAsyncResult, TResult], arg1: TArg1, arg2: TArg2, state: System.Object, ) -> System.Threading.Tasks.Task[TResult]:
        ...

    @typing.overload
    def FromAsync(self, beginMethod: System.Func[TArg1, TArg2, System.AsyncCallback, System.Object, System.IAsyncResult], endMethod: System.Func[System.IAsyncResult, TResult], arg1: TArg1, arg2: TArg2, state: System.Object, creationOptions: System.Threading.Tasks.TaskCreationOptions, ) -> System.Threading.Tasks.Task[TResult]:
        ...

    @typing.overload
    def FromAsync(self, beginMethod: System.Func[TArg1, TArg2, TArg3, System.AsyncCallback, System.Object, System.IAsyncResult], endMethod: System.Func[System.IAsyncResult, TResult], arg1: TArg1, arg2: TArg2, arg3: TArg3, state: System.Object, ) -> System.Threading.Tasks.Task[TResult]:
        ...

    @typing.overload
    def FromAsync(self, beginMethod: System.Func[TArg1, TArg2, TArg3, System.AsyncCallback, System.Object, System.IAsyncResult], endMethod: System.Func[System.IAsyncResult, TResult], arg1: TArg1, arg2: TArg2, arg3: TArg3, state: System.Object, creationOptions: System.Threading.Tasks.TaskCreationOptions, ) -> System.Threading.Tasks.Task[TResult]:
        ...

    @typing.overload
    def ContinueWhenAll(self, tasks: list[System.Threading.Tasks.Task], continuationAction: System.Action[list[System.Threading.Tasks.Task]], ) -> System.Threading.Tasks.Task:
        ...

    @typing.overload
    def ContinueWhenAll(self, tasks: list[System.Threading.Tasks.Task], continuationAction: System.Action[list[System.Threading.Tasks.Task]], cancellationToken: System.Threading.CancellationToken, ) -> System.Threading.Tasks.Task:
        ...

    @typing.overload
    def ContinueWhenAll(self, tasks: list[System.Threading.Tasks.Task], continuationAction: System.Action[list[System.Threading.Tasks.Task]], continuationOptions: System.Threading.Tasks.TaskContinuationOptions, ) -> System.Threading.Tasks.Task:
        ...

    @typing.overload
    def ContinueWhenAll(self, tasks: list[System.Threading.Tasks.Task], continuationAction: System.Action[list[System.Threading.Tasks.Task]], cancellationToken: System.Threading.CancellationToken, continuationOptions: System.Threading.Tasks.TaskContinuationOptions, scheduler: System.Threading.Tasks.TaskScheduler, ) -> System.Threading.Tasks.Task:
        ...

    @typing.overload
    def ContinueWhenAll(self, tasks: list[System.Threading.Tasks.Task[TAntecedentResult]], continuationAction: System.Action[list[System.Threading.Tasks.Task[TAntecedentResult]]], ) -> System.Threading.Tasks.Task:
        ...

    @typing.overload
    def ContinueWhenAll(self, tasks: list[System.Threading.Tasks.Task[TAntecedentResult]], continuationAction: System.Action[list[System.Threading.Tasks.Task[TAntecedentResult]]], cancellationToken: System.Threading.CancellationToken, ) -> System.Threading.Tasks.Task:
        ...

    @typing.overload
    def ContinueWhenAll(self, tasks: list[System.Threading.Tasks.Task[TAntecedentResult]], continuationAction: System.Action[list[System.Threading.Tasks.Task[TAntecedentResult]]], continuationOptions: System.Threading.Tasks.TaskContinuationOptions, ) -> System.Threading.Tasks.Task:
        ...

    @typing.overload
    def ContinueWhenAll(self, tasks: list[System.Threading.Tasks.Task[TAntecedentResult]], continuationAction: System.Action[list[System.Threading.Tasks.Task[TAntecedentResult]]], cancellationToken: System.Threading.CancellationToken, continuationOptions: System.Threading.Tasks.TaskContinuationOptions, scheduler: System.Threading.Tasks.TaskScheduler, ) -> System.Threading.Tasks.Task:
        ...

    @typing.overload
    def ContinueWhenAll(self, tasks: list[System.Threading.Tasks.Task], continuationFunction: System.Func[list[System.Threading.Tasks.Task], TResult], ) -> System.Threading.Tasks.Task[TResult]:
        ...

    @typing.overload
    def ContinueWhenAll(self, tasks: list[System.Threading.Tasks.Task], continuationFunction: System.Func[list[System.Threading.Tasks.Task], TResult], cancellationToken: System.Threading.CancellationToken, ) -> System.Threading.Tasks.Task[TResult]:
        ...

class Task(System.IAsyncResult, System.IDisposable, System.Threading.Tasks.Task, typing.Generic[TResult]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def Result(self) -> TResult:
        ...

    @property
    def Factory(self) -> System.Threading.Tasks.TaskFactory[TResult]:
        ...

    @property
    def Id(self) -> System.Int32:
        ...

    @property
    def Exception(self) -> System.AggregateException:
        ...

    @property
    def Status(self) -> System.Threading.Tasks.TaskStatus:
        ...

    @property
    def IsCanceled(self) -> System.Boolean:
        ...

    @property
    def IsCompleted(self) -> System.Boolean:
        ...

    @property
    def IsCompletedSuccessfully(self) -> System.Boolean:
        ...

    @property
    def CreationOptions(self) -> System.Threading.Tasks.TaskCreationOptions:
        ...

    @property
    def AsyncState(self) -> System.Object:
        ...

    @property
    def IsFaulted(self) -> System.Boolean:
        ...

    # methods
    @typing.overload
    def __init__(self, function: System.Func[TResult], ):
        ...

    @typing.overload
    def __init__(self, function: System.Func[TResult], cancellationToken: System.Threading.CancellationToken, ):
        ...

    @typing.overload
    def __init__(self, function: System.Func[TResult], creationOptions: System.Threading.Tasks.TaskCreationOptions, ):
        ...

    @typing.overload
    def __init__(self, function: System.Func[TResult], cancellationToken: System.Threading.CancellationToken, creationOptions: System.Threading.Tasks.TaskCreationOptions, ):
        ...

    @typing.overload
    def __init__(self, function: System.Func[System.Object, TResult], state: System.Object, ):
        ...

    @typing.overload
    def __init__(self, function: System.Func[System.Object, TResult], state: System.Object, cancellationToken: System.Threading.CancellationToken, ):
        ...

    @typing.overload
    def __init__(self, function: System.Func[System.Object, TResult], state: System.Object, creationOptions: System.Threading.Tasks.TaskCreationOptions, ):
        ...

    @typing.overload
    def __init__(self, function: System.Func[System.Object, TResult], state: System.Object, cancellationToken: System.Threading.CancellationToken, creationOptions: System.Threading.Tasks.TaskCreationOptions, ):
        ...

    @typing.overload
    def GetAwaiter(self, ) -> System.Runtime.CompilerServices.TaskAwaiter[TResult]:
        ...

    @typing.overload
    def ConfigureAwait(self, continueOnCapturedContext: System.Boolean, ) -> System.Runtime.CompilerServices.ConfiguredTaskAwaitable[TResult]:
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
    def ContinueWith(self, continuationAction: System.Action[System.Threading.Tasks.Task], ) -> System.Threading.Tasks.Task:
        ...

    @typing.overload
    def ContinueWith(self, continuationAction: System.Action[System.Threading.Tasks.Task], cancellationToken: System.Threading.CancellationToken, ) -> System.Threading.Tasks.Task:
        ...

    @typing.overload
    def ContinueWith(self, continuationAction: System.Action[System.Threading.Tasks.Task], scheduler: System.Threading.Tasks.TaskScheduler, ) -> System.Threading.Tasks.Task:
        ...

    @typing.overload
    def ContinueWith(self, continuationAction: System.Action[System.Threading.Tasks.Task], continuationOptions: System.Threading.Tasks.TaskContinuationOptions, ) -> System.Threading.Tasks.Task:
        ...

    @typing.overload
    def ContinueWith(self, continuationAction: System.Action[System.Threading.Tasks.Task], cancellationToken: System.Threading.CancellationToken, continuationOptions: System.Threading.Tasks.TaskContinuationOptions, scheduler: System.Threading.Tasks.TaskScheduler, ) -> System.Threading.Tasks.Task:
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
    def ContinueWith(self, continuationAction: System.Action[System.Threading.Tasks.Task, System.Object], state: System.Object, continuationOptions: System.Threading.Tasks.TaskContinuationOptions, ) -> System.Threading.Tasks.Task:
        ...

    @typing.overload
    def ContinueWith(self, continuationAction: System.Action[System.Threading.Tasks.Task, System.Object], state: System.Object, cancellationToken: System.Threading.CancellationToken, continuationOptions: System.Threading.Tasks.TaskContinuationOptions, scheduler: System.Threading.Tasks.TaskScheduler, ) -> System.Threading.Tasks.Task:
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
    def ContinueWith(self, continuationFunction: System.Func[System.Threading.Tasks.Task, TNewResult], continuationOptions: System.Threading.Tasks.TaskContinuationOptions, ) -> System.Threading.Tasks.Task[TNewResult]:
        ...

    @typing.overload
    def ContinueWith(self, continuationFunction: System.Func[System.Threading.Tasks.Task, TNewResult], cancellationToken: System.Threading.CancellationToken, continuationOptions: System.Threading.Tasks.TaskContinuationOptions, scheduler: System.Threading.Tasks.TaskScheduler, ) -> System.Threading.Tasks.Task[TNewResult]:
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
    def ContinueWith(self, continuationFunction: System.Func[System.Threading.Tasks.Task, System.Object, TNewResult], state: System.Object, continuationOptions: System.Threading.Tasks.TaskContinuationOptions, ) -> System.Threading.Tasks.Task[TNewResult]:
        ...

    @typing.overload
    def ContinueWith(self, continuationFunction: System.Func[System.Threading.Tasks.Task, System.Object, TNewResult], state: System.Object, cancellationToken: System.Threading.CancellationToken, continuationOptions: System.Threading.Tasks.TaskContinuationOptions, scheduler: System.Threading.Tasks.TaskScheduler, ) -> System.Threading.Tasks.Task[TNewResult]:
        ...

class TaskScheduler(System.Object, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def MaximumConcurrencyLevel(self) -> System.Int32:
        ...

    @property
    def Default(self) -> System.Threading.Tasks.TaskScheduler:
        ...

    @property
    def Current(self) -> System.Threading.Tasks.TaskScheduler:
        ...

    @property
    def Id(self) -> System.Int32:
        ...

    # methods
    @typing.overload
    @staticmethod
    def FromCurrentSynchronizationContext() -> System.Threading.Tasks.TaskScheduler:
        ...

class TaskContinuationOptions(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    None_: System.Int32 = None
    PreferFairness: System.Int32 = PreferFairness
    LongRunning: System.Int32 = LongRunning
    AttachedToParent: System.Int32 = AttachedToParent
    DenyChildAttach: System.Int32 = DenyChildAttach
    HideScheduler: System.Int32 = HideScheduler
    LazyCancellation: System.Int32 = LazyCancellation
    RunContinuationsAsynchronously: System.Int32 = RunContinuationsAsynchronously
    NotOnRanToCompletion: System.Int32 = NotOnRanToCompletion
    NotOnFaulted: System.Int32 = NotOnFaulted
    OnlyOnCanceled: System.Int32 = OnlyOnCanceled
    NotOnCanceled: System.Int32 = NotOnCanceled
    OnlyOnFaulted: System.Int32 = OnlyOnFaulted
    OnlyOnRanToCompletion: System.Int32 = OnlyOnRanToCompletion
    ExecuteSynchronously: System.Int32 = ExecuteSynchronously

class TaskFactory(System.Object, typing.Generic[TResult]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def CancellationToken(self) -> System.Threading.CancellationToken:
        ...

    @property
    def Scheduler(self) -> System.Threading.Tasks.TaskScheduler:
        ...

    @property
    def CreationOptions(self) -> System.Threading.Tasks.TaskCreationOptions:
        ...

    @property
    def ContinuationOptions(self) -> System.Threading.Tasks.TaskContinuationOptions:
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
    def __init__(self, creationOptions: System.Threading.Tasks.TaskCreationOptions, continuationOptions: System.Threading.Tasks.TaskContinuationOptions, ):
        ...

    @typing.overload
    def __init__(self, cancellationToken: System.Threading.CancellationToken, creationOptions: System.Threading.Tasks.TaskCreationOptions, continuationOptions: System.Threading.Tasks.TaskContinuationOptions, scheduler: System.Threading.Tasks.TaskScheduler, ):
        ...

    @typing.overload
    def StartNew(self, function: System.Func[TResult], ) -> System.Threading.Tasks.Task[TResult]:
        ...

    @typing.overload
    def StartNew(self, function: System.Func[TResult], cancellationToken: System.Threading.CancellationToken, ) -> System.Threading.Tasks.Task[TResult]:
        ...

    @typing.overload
    def StartNew(self, function: System.Func[TResult], creationOptions: System.Threading.Tasks.TaskCreationOptions, ) -> System.Threading.Tasks.Task[TResult]:
        ...

    @typing.overload
    def StartNew(self, function: System.Func[TResult], cancellationToken: System.Threading.CancellationToken, creationOptions: System.Threading.Tasks.TaskCreationOptions, scheduler: System.Threading.Tasks.TaskScheduler, ) -> System.Threading.Tasks.Task[TResult]:
        ...

    @typing.overload
    def StartNew(self, function: System.Func[System.Object, TResult], state: System.Object, ) -> System.Threading.Tasks.Task[TResult]:
        ...

    @typing.overload
    def StartNew(self, function: System.Func[System.Object, TResult], state: System.Object, cancellationToken: System.Threading.CancellationToken, ) -> System.Threading.Tasks.Task[TResult]:
        ...

    @typing.overload
    def StartNew(self, function: System.Func[System.Object, TResult], state: System.Object, creationOptions: System.Threading.Tasks.TaskCreationOptions, ) -> System.Threading.Tasks.Task[TResult]:
        ...

    @typing.overload
    def StartNew(self, function: System.Func[System.Object, TResult], state: System.Object, cancellationToken: System.Threading.CancellationToken, creationOptions: System.Threading.Tasks.TaskCreationOptions, scheduler: System.Threading.Tasks.TaskScheduler, ) -> System.Threading.Tasks.Task[TResult]:
        ...

    @typing.overload
    def FromAsync(self, asyncResult: System.IAsyncResult, endMethod: System.Func[System.IAsyncResult, TResult], ) -> System.Threading.Tasks.Task[TResult]:
        ...

    @typing.overload
    def FromAsync(self, asyncResult: System.IAsyncResult, endMethod: System.Func[System.IAsyncResult, TResult], creationOptions: System.Threading.Tasks.TaskCreationOptions, ) -> System.Threading.Tasks.Task[TResult]:
        ...

    @typing.overload
    def FromAsync(self, asyncResult: System.IAsyncResult, endMethod: System.Func[System.IAsyncResult, TResult], creationOptions: System.Threading.Tasks.TaskCreationOptions, scheduler: System.Threading.Tasks.TaskScheduler, ) -> System.Threading.Tasks.Task[TResult]:
        ...

    @typing.overload
    def FromAsync(self, beginMethod: System.Func[System.AsyncCallback, System.Object, System.IAsyncResult], endMethod: System.Func[System.IAsyncResult, TResult], state: System.Object, ) -> System.Threading.Tasks.Task[TResult]:
        ...

    @typing.overload
    def FromAsync(self, beginMethod: System.Func[System.AsyncCallback, System.Object, System.IAsyncResult], endMethod: System.Func[System.IAsyncResult, TResult], state: System.Object, creationOptions: System.Threading.Tasks.TaskCreationOptions, ) -> System.Threading.Tasks.Task[TResult]:
        ...

    @typing.overload
    def FromAsync(self, beginMethod: System.Func[TArg1, System.AsyncCallback, System.Object, System.IAsyncResult], endMethod: System.Func[System.IAsyncResult, TResult], arg1: TArg1, state: System.Object, ) -> System.Threading.Tasks.Task[TResult]:
        ...

    @typing.overload
    def FromAsync(self, beginMethod: System.Func[TArg1, System.AsyncCallback, System.Object, System.IAsyncResult], endMethod: System.Func[System.IAsyncResult, TResult], arg1: TArg1, state: System.Object, creationOptions: System.Threading.Tasks.TaskCreationOptions, ) -> System.Threading.Tasks.Task[TResult]:
        ...

    @typing.overload
    def FromAsync(self, beginMethod: System.Func[TArg1, TArg2, System.AsyncCallback, System.Object, System.IAsyncResult], endMethod: System.Func[System.IAsyncResult, TResult], arg1: TArg1, arg2: TArg2, state: System.Object, ) -> System.Threading.Tasks.Task[TResult]:
        ...

    @typing.overload
    def FromAsync(self, beginMethod: System.Func[TArg1, TArg2, System.AsyncCallback, System.Object, System.IAsyncResult], endMethod: System.Func[System.IAsyncResult, TResult], arg1: TArg1, arg2: TArg2, state: System.Object, creationOptions: System.Threading.Tasks.TaskCreationOptions, ) -> System.Threading.Tasks.Task[TResult]:
        ...

    @typing.overload
    def FromAsync(self, beginMethod: System.Func[TArg1, TArg2, TArg3, System.AsyncCallback, System.Object, System.IAsyncResult], endMethod: System.Func[System.IAsyncResult, TResult], arg1: TArg1, arg2: TArg2, arg3: TArg3, state: System.Object, ) -> System.Threading.Tasks.Task[TResult]:
        ...

    @typing.overload
    def FromAsync(self, beginMethod: System.Func[TArg1, TArg2, TArg3, System.AsyncCallback, System.Object, System.IAsyncResult], endMethod: System.Func[System.IAsyncResult, TResult], arg1: TArg1, arg2: TArg2, arg3: TArg3, state: System.Object, creationOptions: System.Threading.Tasks.TaskCreationOptions, ) -> System.Threading.Tasks.Task[TResult]:
        ...

    @typing.overload
    def ContinueWhenAll(self, tasks: list[System.Threading.Tasks.Task], continuationFunction: System.Func[list[System.Threading.Tasks.Task], TResult], ) -> System.Threading.Tasks.Task[TResult]:
        ...

    @typing.overload
    def ContinueWhenAll(self, tasks: list[System.Threading.Tasks.Task], continuationFunction: System.Func[list[System.Threading.Tasks.Task], TResult], cancellationToken: System.Threading.CancellationToken, ) -> System.Threading.Tasks.Task[TResult]:
        ...

    @typing.overload
    def ContinueWhenAll(self, tasks: list[System.Threading.Tasks.Task], continuationFunction: System.Func[list[System.Threading.Tasks.Task], TResult], continuationOptions: System.Threading.Tasks.TaskContinuationOptions, ) -> System.Threading.Tasks.Task[TResult]:
        ...

    @typing.overload
    def ContinueWhenAll(self, tasks: list[System.Threading.Tasks.Task], continuationFunction: System.Func[list[System.Threading.Tasks.Task], TResult], cancellationToken: System.Threading.CancellationToken, continuationOptions: System.Threading.Tasks.TaskContinuationOptions, scheduler: System.Threading.Tasks.TaskScheduler, ) -> System.Threading.Tasks.Task[TResult]:
        ...

    @typing.overload
    def ContinueWhenAll(self, tasks: list[System.Threading.Tasks.Task[TAntecedentResult]], continuationFunction: System.Func[list[System.Threading.Tasks.Task[TAntecedentResult]], TResult], ) -> System.Threading.Tasks.Task[TResult]:
        ...

    @typing.overload
    def ContinueWhenAll(self, tasks: list[System.Threading.Tasks.Task[TAntecedentResult]], continuationFunction: System.Func[list[System.Threading.Tasks.Task[TAntecedentResult]], TResult], cancellationToken: System.Threading.CancellationToken, ) -> System.Threading.Tasks.Task[TResult]:
        ...

    @typing.overload
    def ContinueWhenAll(self, tasks: list[System.Threading.Tasks.Task[TAntecedentResult]], continuationFunction: System.Func[list[System.Threading.Tasks.Task[TAntecedentResult]], TResult], continuationOptions: System.Threading.Tasks.TaskContinuationOptions, ) -> System.Threading.Tasks.Task[TResult]:
        ...

    @typing.overload
    def ContinueWhenAll(self, tasks: list[System.Threading.Tasks.Task[TAntecedentResult]], continuationFunction: System.Func[list[System.Threading.Tasks.Task[TAntecedentResult]], TResult], cancellationToken: System.Threading.CancellationToken, continuationOptions: System.Threading.Tasks.TaskContinuationOptions, scheduler: System.Threading.Tasks.TaskScheduler, ) -> System.Threading.Tasks.Task[TResult]:
        ...

    @typing.overload
    def ContinueWhenAny(self, tasks: list[System.Threading.Tasks.Task], continuationFunction: System.Func[System.Threading.Tasks.Task, TResult], ) -> System.Threading.Tasks.Task[TResult]:
        ...

    @typing.overload
    def ContinueWhenAny(self, tasks: list[System.Threading.Tasks.Task], continuationFunction: System.Func[System.Threading.Tasks.Task, TResult], cancellationToken: System.Threading.CancellationToken, ) -> System.Threading.Tasks.Task[TResult]:
        ...

    @typing.overload
    def ContinueWhenAny(self, tasks: list[System.Threading.Tasks.Task], continuationFunction: System.Func[System.Threading.Tasks.Task, TResult], continuationOptions: System.Threading.Tasks.TaskContinuationOptions, ) -> System.Threading.Tasks.Task[TResult]:
        ...

    @typing.overload
    def ContinueWhenAny(self, tasks: list[System.Threading.Tasks.Task], continuationFunction: System.Func[System.Threading.Tasks.Task, TResult], cancellationToken: System.Threading.CancellationToken, continuationOptions: System.Threading.Tasks.TaskContinuationOptions, scheduler: System.Threading.Tasks.TaskScheduler, ) -> System.Threading.Tasks.Task[TResult]:
        ...

    @typing.overload
    def ContinueWhenAny(self, tasks: list[System.Threading.Tasks.Task[TAntecedentResult]], continuationFunction: System.Func[System.Threading.Tasks.Task[TAntecedentResult], TResult], ) -> System.Threading.Tasks.Task[TResult]:
        ...

    @typing.overload
    def ContinueWhenAny(self, tasks: list[System.Threading.Tasks.Task[TAntecedentResult]], continuationFunction: System.Func[System.Threading.Tasks.Task[TAntecedentResult], TResult], cancellationToken: System.Threading.CancellationToken, ) -> System.Threading.Tasks.Task[TResult]:
        ...

    @typing.overload
    def ContinueWhenAny(self, tasks: list[System.Threading.Tasks.Task[TAntecedentResult]], continuationFunction: System.Func[System.Threading.Tasks.Task[TAntecedentResult], TResult], continuationOptions: System.Threading.Tasks.TaskContinuationOptions, ) -> System.Threading.Tasks.Task[TResult]:
        ...

    @typing.overload
    def ContinueWhenAny(self, tasks: list[System.Threading.Tasks.Task[TAntecedentResult]], continuationFunction: System.Func[System.Threading.Tasks.Task[TAntecedentResult], TResult], cancellationToken: System.Threading.CancellationToken, continuationOptions: System.Threading.Tasks.TaskContinuationOptions, scheduler: System.Threading.Tasks.TaskScheduler, ) -> System.Threading.Tasks.Task[TResult]:
        ...

class ValueTask(System.IEquatable[System.Threading.Tasks.ValueTask], System.ValueType):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def CompletedTask(self) -> System.Threading.Tasks.ValueTask:
        ...

    @property
    def IsCompleted(self) -> System.Boolean:
        ...

    @property
    def IsCompletedSuccessfully(self) -> System.Boolean:
        ...

    @property
    def IsFaulted(self) -> System.Boolean:
        ...

    @property
    def IsCanceled(self) -> System.Boolean:
        ...

    # methods
    @typing.overload
    def __init__(self, task: System.Threading.Tasks.Task, ):
        ...

    @typing.overload
    def __init__(self, source: System.Threading.Tasks.Sources.IValueTaskSource, token: System.Int16, ):
        ...

    @typing.overload
    @staticmethod
    def FromResult(result: TResult, ) -> System.Threading.Tasks.ValueTask[TResult]:
        ...

    @typing.overload
    @staticmethod
    def FromCanceled(cancellationToken: System.Threading.CancellationToken, ) -> System.Threading.Tasks.ValueTask:
        ...

    @typing.overload
    @staticmethod
    def FromCanceled(cancellationToken: System.Threading.CancellationToken, ) -> System.Threading.Tasks.ValueTask[TResult]:
        ...

    @typing.overload
    @staticmethod
    def FromException(exception: System.Exception, ) -> System.Threading.Tasks.ValueTask:
        ...

    @typing.overload
    @staticmethod
    def FromException(exception: System.Exception, ) -> System.Threading.Tasks.ValueTask[TResult]:
        ...

    @typing.overload
    def GetHashCode(self, ) -> System.Int32:
        ...

    @typing.overload
    def Equals(self, obj: System.Object, ) -> System.Boolean:
        ...

    @typing.overload
    def Equals(self, other: System.Threading.Tasks.ValueTask, ) -> System.Boolean:
        ...

    @typing.overload
    def AsTask(self, ) -> System.Threading.Tasks.Task:
        ...

    @typing.overload
    def Preserve(self, ) -> System.Threading.Tasks.ValueTask:
        ...

    @typing.overload
    def GetAwaiter(self, ) -> System.Runtime.CompilerServices.ValueTaskAwaiter:
        ...

    @typing.overload
    def ConfigureAwait(self, continueOnCapturedContext: System.Boolean, ) -> System.Runtime.CompilerServices.ConfiguredValueTaskAwaitable:
        ...

class ValueTask(System.IEquatable[System.Threading.Tasks.ValueTask], System.ValueType, typing.Generic[TResult]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def IsCompleted(self) -> System.Boolean:
        ...

    @property
    def IsCompletedSuccessfully(self) -> System.Boolean:
        ...

    @property
    def IsFaulted(self) -> System.Boolean:
        ...

    @property
    def IsCanceled(self) -> System.Boolean:
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
    def __init__(self, source: System.Threading.Tasks.Sources.IValueTaskSource[TResult], token: System.Int16, ):
        ...

    @typing.overload
    def GetHashCode(self, ) -> System.Int32:
        ...

    @typing.overload
    def Equals(self, obj: System.Object, ) -> System.Boolean:
        ...

    @typing.overload
    def Equals(self, other: System.Threading.Tasks.ValueTask, ) -> System.Boolean:
        ...

    @typing.overload
    def AsTask(self, ) -> System.Threading.Tasks.Task[TResult]:
        ...

    @typing.overload
    def Preserve(self, ) -> System.Threading.Tasks.ValueTask:
        ...

    @typing.overload
    def GetAwaiter(self, ) -> System.Runtime.CompilerServices.ValueTaskAwaiter[TResult]:
        ...

    @typing.overload
    def ConfigureAwait(self, continueOnCapturedContext: System.Boolean, ) -> System.Runtime.CompilerServices.ConfiguredValueTaskAwaitable[TResult]:
        ...

    @typing.overload
    def ToString(self, ) -> System.String:
        ...

