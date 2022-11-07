from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import System
import System.Runtime.CompilerServices
import System.Reflection
import System.Linq.Expressions
import System.Threading.Tasks
import System.Runtime.CompilerServices.ConfiguredTaskAwaitable
import System.Runtime.CompilerServices.ConfiguredValueTaskAwaitable
import System.Collections.Generic
import System.Collections.ObjectModel
import System.Runtime.CompilerServices.CallSiteBinder
import System.Runtime.CompilerServices.YieldAwaitable
import System.Collections

T = typing.TypeVar('T')
TResult = typing.TypeVar('TResult')

class ITuple(abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    @abc.abstractmethod
    def Length(self) -> int:
        ...

    @property
    @abc.abstractmethod
    def Item(self) -> System.Object:
        ...

    # methods
class CallSite(System.Runtime.CompilerServices.CallSite, typing.Generic[T]):
    @typing.overload
    def __init__(self, **kwargs):
        self.Target: T
        self.Rules: System.Array[T]
        self._cachedMatchmaker: System.Runtime.CompilerServices.CallSite
        self._binder: System.Runtime.CompilerServices.CallSiteBinder
        self._match: bool
        ...

    # static fields

    # properties
    @property
    def Update(self) -> T:
        ...

    @property
    def Binder(self) -> System.Runtime.CompilerServices.CallSiteBinder:
        ...

    # methods
    @typing.overload
    def __init__(self, binder: System.Runtime.CompilerServices.CallSiteBinder, ):
        ...

    @typing.overload
    def __init__(self, ):
        ...

    def CreateMatchMaker(self, ) -> System.Runtime.CompilerServices.CallSite:
        ...

    def GetMatchmaker(self, ) -> System.Runtime.CompilerServices.CallSite:
        ...

    def ReleaseMatchmaker(self, matchMaker: System.Runtime.CompilerServices.CallSite, ) -> None:
        ...

    @staticmethod
    def Create(binder: System.Runtime.CompilerServices.CallSiteBinder, ) -> System.Runtime.CompilerServices.CallSite:
        ...

    @typing.overload
    def GetUpdateDelegate(self, ) -> T:
        ...

    @typing.overload
    def GetUpdateDelegate(self, addr: ref[T], ) -> T:
        ...

    def AddRule(self, newRule: T, ) -> None:
        ...

    def MoveRule(self, i: int, ) -> None:
        ...

    def MakeUpdateDelegate(self, ) -> T:
        ...

    @staticmethod
    def IsSimpleSignature(invoke: System.Reflection.MethodInfo, sig: ref[System.Array[System.Type]], ) -> bool:
        ...

    def CreateCustomUpdateDelegate(self, invoke: System.Reflection.MethodInfo, ) -> T:
        ...

    def CreateCustomNoMatchDelegate(self, invoke: System.Reflection.MethodInfo, ) -> T:
        ...

    @staticmethod
    def Convert(arg: System.Linq.Expressions.Expression, type: System.Type, ) -> System.Linq.Expressions.Expression:
        ...

class ConfiguredTaskAwaitable(System.ValueType):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    def __init__(self, task: System.Threading.Tasks.Task, continueOnCapturedContext: bool, ):
        ...

    def GetAwaiter(self, ) -> System.Runtime.CompilerServices.ConfiguredTaskAwaitable.ConfiguredTaskAwaiter:
        ...

class ConfiguredTaskAwaitable(System.ValueType, typing.Generic[TResult]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    def __init__(self, task: System.Threading.Tasks.Task[TResult], continueOnCapturedContext: bool, ):
        ...

    def GetAwaiter(self, ) -> System.Runtime.CompilerServices.ConfiguredTaskAwaitable.ConfiguredTaskAwaiter[TResult]:
        ...

class ICriticalNotifyCompletion(System.Runtime.CompilerServices.INotifyCompletion, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    @abc.abstractmethod
    def UnsafeOnCompleted(self, continuation: System.Action, ) -> None:
        ...

class TaskAwaiter(System.Runtime.CompilerServices.ICriticalNotifyCompletion, System.Runtime.CompilerServices.INotifyCompletion, System.Runtime.CompilerServices.ITaskAwaiter, System.ValueType):
    @typing.overload
    def __init__(self, **kwargs):
        self.m_task: System.Threading.Tasks.Task
        ...

    # static fields

    # properties
    @property
    def IsCompleted(self) -> bool:
        ...

    # methods
    def __init__(self, task: System.Threading.Tasks.Task, ):
        ...

    def OnCompleted(self, continuation: System.Action, ) -> None:
        ...

    def UnsafeOnCompleted(self, continuation: System.Action, ) -> None:
        ...

    def GetResult(self, ) -> None:
        ...

    @staticmethod
    def ValidateEnd(task: System.Threading.Tasks.Task, ) -> None:
        ...

    @staticmethod
    def HandleNonSuccessAndDebuggerNotification(task: System.Threading.Tasks.Task, ) -> None:
        ...

    @staticmethod
    def ThrowForNonSuccess(task: System.Threading.Tasks.Task, ) -> None:
        ...

    @staticmethod
    def OnCompletedInternal(task: System.Threading.Tasks.Task, continuation: System.Action, continueOnCapturedContext: bool, flowExecutionContext: bool, ) -> None:
        ...

    @staticmethod
    def UnsafeOnCompletedInternal(task: System.Threading.Tasks.Task, stateMachineBox: System.Runtime.CompilerServices.IAsyncStateMachineBox, continueOnCapturedContext: bool, ) -> None:
        ...

    @staticmethod
    def OutputWaitEtwEvents(task: System.Threading.Tasks.Task, continuation: System.Action, ) -> System.Action:
        ...

class StrongBox(System.Runtime.CompilerServices.IStrongBox, System.Object, typing.Generic[T]):
    @typing.overload
    def __init__(self, **kwargs):
        self.Value: T
        ...

    # static fields

    # properties
    @property
    def Value(self) -> System.Object:
        ...
    @Value.setter
    def Value(self, val: System.Object):
        ...

    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def __init__(self, value: T, ):
        ...

class IStrongBox(abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    @abc.abstractmethod
    def Value(self) -> System.Object:
        ...
    @Value.setter
    @abc.abstractmethod
    def Value(self, val: System.Object):
        ...

    # methods
class ConfiguredValueTaskAwaitable(System.ValueType, typing.Generic[TResult]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    def __init__(self, value: ref[System.Threading.Tasks.ValueTask[TResult]], ):
        ...

    def GetAwaiter(self, ) -> System.Runtime.CompilerServices.ConfiguredValueTaskAwaitable.ConfiguredValueTaskAwaiter[TResult]:
        ...

class DebugInfoGenerator(System.Object, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    def __init__(self, ):
        ...

    @staticmethod
    def CreatePdbGenerator() -> System.Runtime.CompilerServices.DebugInfoGenerator:
        ...

    @abc.abstractmethod
    def MarkSequencePoint(self, method: System.Linq.Expressions.LambdaExpression, ilOffset: int, sequencePoint: System.Linq.Expressions.DebugInfoExpression, ) -> None:
        ...

class ConfiguredValueTaskAwaitable(System.ValueType):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    def __init__(self, value: ref[System.Threading.Tasks.ValueTask], ):
        ...

    def GetAwaiter(self, ) -> System.Runtime.CompilerServices.ConfiguredValueTaskAwaitable.ConfiguredValueTaskAwaiter:
        ...

class ValueTaskAwaiter(System.Runtime.CompilerServices.ICriticalNotifyCompletion, System.Runtime.CompilerServices.INotifyCompletion, System.Runtime.CompilerServices.IStateMachineBoxAwareAwaiter, System.ValueType, typing.Generic[TResult]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def IsCompleted(self) -> bool:
        ...

    # methods
    def __init__(self, value: ref[System.Threading.Tasks.ValueTask[TResult]], ):
        ...

    def GetResult(self, ) -> TResult:
        ...

    def OnCompleted(self, continuation: System.Action, ) -> None:
        ...

    def UnsafeOnCompleted(self, continuation: System.Action, ) -> None:
        ...

    def AwaitUnsafeOnCompleted(self, box: System.Runtime.CompilerServices.IAsyncStateMachineBox, ) -> None:
        ...

class CallSiteBinder(System.Object, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        self.Cache: System.Collections.Generic.Dictionary[System.Type, System.Object]
        ...

    # static fields

    # properties
    @property
    def UpdateLabel(self) -> System.Linq.Expressions.LabelTarget:
        ...

    # methods
    def __init__(self, ):
        ...

    @abc.abstractmethod
    def Bind(self, args: System.Array[System.Object], parameters: System.Collections.ObjectModel.ReadOnlyCollection[System.Linq.Expressions.ParameterExpression], returnLabel: System.Linq.Expressions.LabelTarget, ) -> System.Linq.Expressions.Expression:
        ...

    def BindDelegate(self, site: System.Runtime.CompilerServices.CallSite[T], args: System.Array[System.Object], ) -> T:
        ...

    def BindCore(self, site: System.Runtime.CompilerServices.CallSite[T], args: System.Array[System.Object], ) -> T:
        ...

    def CacheTarget(self, target: T, ) -> None:
        ...

    @staticmethod
    def Stitch(binding: System.Linq.Expressions.Expression, signature: System.Runtime.CompilerServices.CallSiteBinder.LambdaSignature[T], ) -> System.Linq.Expressions.Expression[T]:
        ...

    def GetRuleCache(self, ) -> System.Runtime.CompilerServices.RuleCache[T]:
        ...

class YieldAwaitable(System.ValueType):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    def GetAwaiter(self, ) -> System.Runtime.CompilerServices.YieldAwaitable.YieldAwaiter:
        ...

class INotifyCompletion(abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    @abc.abstractmethod
    def OnCompleted(self, continuation: System.Action, ) -> None:
        ...

class IRuntimeVariables(abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    @abc.abstractmethod
    def Count(self) -> int:
        ...

    @property
    @abc.abstractmethod
    def Item(self) -> System.Object:
        ...
    @Item.setter
    @abc.abstractmethod
    def Item(self, val: System.Object):
        ...

    # methods
class CallSite(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        self._binder: System.Runtime.CompilerServices.CallSiteBinder
        self._match: bool
        ...

    # static fields

    # properties
    @property
    def Binder(self) -> System.Runtime.CompilerServices.CallSiteBinder:
        ...

    # methods
    def __init__(self, binder: System.Runtime.CompilerServices.CallSiteBinder, ):
        ...

    @staticmethod
    def Create(delegateType: System.Type, binder: System.Runtime.CompilerServices.CallSiteBinder, ) -> System.Runtime.CompilerServices.CallSite:
        ...

class RuleCache(System.Object, typing.Generic[T]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    def __init__(self, ):
        ...

    def GetRules(self, ) -> System.Array[T]:
        ...

    def MoveRule(self, rule: T, i: int, ) -> None:
        ...

    def AddRule(self, newRule: T, ) -> None:
        ...

    @staticmethod
    def AddOrInsert(rules: System.Array[T], item: T, ) -> System.Array[T]:
        ...

class TaskAwaiter(System.Runtime.CompilerServices.ICriticalNotifyCompletion, System.Runtime.CompilerServices.INotifyCompletion, System.Runtime.CompilerServices.ITaskAwaiter, System.ValueType, typing.Generic[TResult]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def IsCompleted(self) -> bool:
        ...

    # methods
    def __init__(self, task: System.Threading.Tasks.Task[TResult], ):
        ...

    def OnCompleted(self, continuation: System.Action, ) -> None:
        ...

    def UnsafeOnCompleted(self, continuation: System.Action, ) -> None:
        ...

    def GetResult(self, ) -> TResult:
        ...

class ReadOnlyCollectionBuilder(System.Collections.Generic.IList[T], System.Collections.Generic.ICollection[T], System.Collections.Generic.IEnumerable[T], System.Collections.IEnumerable, System.Collections.IList, System.Collections.ICollection, System.Object, typing.Generic[T]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def Capacity(self) -> int:
        ...
    @Capacity.setter
    def Capacity(self, val: int):
        ...

    @property
    def Count(self) -> int:
        ...

    @property
    def Item(self) -> T:
        ...
    @Item.setter
    def Item(self, val: T):
        ...

    @property
    def IsReadOnly(self) -> bool:
        ...

    @property
    def IsReadOnly(self) -> bool:
        ...

    @property
    def IsFixedSize(self) -> bool:
        ...

    @property
    def Item(self) -> System.Object:
        ...
    @Item.setter
    def Item(self, val: System.Object):
        ...

    @property
    def IsSynchronized(self) -> bool:
        ...

    @property
    def SyncRoot(self) -> System.Object:
        ...

    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def __init__(self, capacity: int, ):
        ...

    @typing.overload
    def __init__(self, collection: System.Collections.Generic.IEnumerable[T], ):
        ...

    def IndexOf(self, item: T, ) -> int:
        ...

    def Insert(self, index: int, item: T, ) -> None:
        ...

    def RemoveAt(self, index: int, ) -> None:
        ...

    def Add(self, item: T, ) -> None:
        ...

    def Clear(self, ) -> None:
        ...

    def Contains(self, item: T, ) -> bool:
        ...

    def CopyTo(self, array: System.Array[T], arrayIndex: int, ) -> None:
        ...

    def Remove(self, item: T, ) -> bool:
        ...

    def GetEnumerator(self, ) -> System.Collections.Generic.IEnumerator[T]:
        ...

    def GetEnumerator(self, ) -> System.Collections.IEnumerator:
        ...

    def Add(self, value: System.Object, ) -> int:
        ...

    def Contains(self, value: System.Object, ) -> bool:
        ...

    def IndexOf(self, value: System.Object, ) -> int:
        ...

    def Insert(self, index: int, value: System.Object, ) -> None:
        ...

    def Remove(self, value: System.Object, ) -> None:
        ...

    def CopyTo(self, array: System.Array, index: int, ) -> None:
        ...

    @typing.overload
    def Reverse(self, ) -> None:
        ...

    @typing.overload
    def Reverse(self, index: int, count: int, ) -> None:
        ...

    def ToArray(self, ) -> System.Array[T]:
        ...

    def ToReadOnlyCollection(self, ) -> System.Collections.ObjectModel.ReadOnlyCollection[T]:
        ...

    def EnsureCapacity(self, min: int, ) -> None:
        ...

    @staticmethod
    def IsCompatibleObject(value: System.Object, ) -> bool:
        ...

    @staticmethod
    def ValidateNullValue(value: System.Object, argument: str, ) -> None:
        ...

class ValueTaskAwaiter(System.Runtime.CompilerServices.ICriticalNotifyCompletion, System.Runtime.CompilerServices.INotifyCompletion, System.Runtime.CompilerServices.IStateMachineBoxAwareAwaiter, System.ValueType):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields
    s_invokeActionDelegate: System.Action[System.Object] = ...

    # properties
    @property
    def IsCompleted(self) -> bool:
        ...

    # methods
    def __init__(self, value: ref[System.Threading.Tasks.ValueTask], ):
        ...

    def GetResult(self, ) -> None:
        ...

    def OnCompleted(self, continuation: System.Action, ) -> None:
        ...

    def UnsafeOnCompleted(self, continuation: System.Action, ) -> None:
        ...

    def AwaitUnsafeOnCompleted(self, box: System.Runtime.CompilerServices.IAsyncStateMachineBox, ) -> None:
        ...

