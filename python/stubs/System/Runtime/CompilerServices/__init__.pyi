from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import System
import System.Runtime.CompilerServices
import System.Linq.Expressions
import System.Runtime.CompilerServices.ConfiguredTaskAwaitable
import System.Runtime.CompilerServices.YieldAwaitable
import System.Collections.ObjectModel
import System.Runtime.CompilerServices.ConfiguredValueTaskAwaitable

T = typing.TypeVar('T')
TResult = typing.TypeVar('TResult')

class DefaultInterpolatedStringHandler(System.ValueType):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    # methods
    @typing.overload
    def __init__(self, literalLength: System.Int32, formattedCount: System.Int32, ):
        ...

    @typing.overload
    def __init__(self, literalLength: System.Int32, formattedCount: System.Int32, provider: System.IFormatProvider, ):
        ...

    @typing.overload
    def __init__(self, literalLength: System.Int32, formattedCount: System.Int32, provider: System.IFormatProvider, initialBuffer: System.Span[System.Char], ):
        ...

    @typing.overload
    def ToString(self, ) -> System.String:
        ...

    @typing.overload
    def ToStringAndClear(self, ) -> System.String:
        ...

    @typing.overload
    def AppendLiteral(self, value: System.String, ) -> None:
        ...

    @typing.overload
    def AppendFormatted(self, value: T, ) -> None:
        ...

    @typing.overload
    def AppendFormatted(self, value: T, format: System.String, ) -> None:
        ...

    @typing.overload
    def AppendFormatted(self, value: T, alignment: System.Int32, ) -> None:
        ...

    @typing.overload
    def AppendFormatted(self, value: T, alignment: System.Int32, format: System.String, ) -> None:
        ...

    @typing.overload
    def AppendFormatted(self, value: System.ReadOnlySpan[System.Char], ) -> None:
        ...

    @typing.overload
    def AppendFormatted(self, value: System.ReadOnlySpan[System.Char], alignment: System.Int32, format: System.String, ) -> None:
        ...

    @typing.overload
    def AppendFormatted(self, value: System.String, ) -> None:
        ...

    @typing.overload
    def AppendFormatted(self, value: System.String, alignment: System.Int32, format: System.String, ) -> None:
        ...

    @typing.overload
    def AppendFormatted(self, value: System.Object, alignment: System.Int32, format: System.String, ) -> None:
        ...

class ITuple(abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @abc.abstractmethod
    @property
    def Length(self) -> System.Int32:
        ...

    @abc.abstractmethod
    @property
    def Item(self) -> System.Object:
        ...

    # methods
class DebugInfoGenerator(System.Object, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    # methods
    @typing.overload
    @staticmethod
    def CreatePdbGenerator() -> System.Runtime.CompilerServices.DebugInfoGenerator:
        ...

    @typing.overload
    @abc.abstractmethod
    def MarkSequencePoint(self, method: System.Linq.Expressions.LambdaExpression, ilOffset: System.Int32, sequencePoint: System.Linq.Expressions.DebugInfoExpression, ) -> None:
        ...

class TaskAwaiter(System.Runtime.CompilerServices.ICriticalNotifyCompletion, System.Runtime.CompilerServices.INotifyCompletion, System.Runtime.CompilerServices.ITaskAwaiter, System.ValueType):
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

class ConfiguredTaskAwaitable(System.ValueType):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    # methods
    @typing.overload
    def GetAwaiter(self, ) -> System.Runtime.CompilerServices.ConfiguredTaskAwaitable.ConfiguredTaskAwaiter:
        ...

class YieldAwaitable(System.ValueType):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    # methods
    @typing.overload
    def GetAwaiter(self, ) -> System.Runtime.CompilerServices.YieldAwaitable.YieldAwaiter:
        ...

class CallSiteBinder(System.Object, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def UpdateLabel(self) -> System.Linq.Expressions.LabelTarget:
        ...

    # methods
    @typing.overload
    @abc.abstractmethod
    def Bind(self, args: list[System.Object], parameters: System.Collections.ObjectModel.ReadOnlyCollection[System.Linq.Expressions.ParameterExpression], returnLabel: System.Linq.Expressions.LabelTarget, ) -> System.Linq.Expressions.Expression:
        ...

    @typing.overload
    def BindDelegate(self, site: System.Runtime.CompilerServices.CallSite[T], args: list[System.Object], ) -> T:
        ...

class TaskAwaiter(System.Runtime.CompilerServices.ICriticalNotifyCompletion, System.Runtime.CompilerServices.INotifyCompletion, System.Runtime.CompilerServices.ITaskAwaiter, System.ValueType, typing.Generic[TResult]):
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
    def GetResult(self, ) -> TResult:
        ...

class ConfiguredTaskAwaitable(System.ValueType, typing.Generic[TResult]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    # methods
    @typing.overload
    def GetAwaiter(self, ) -> System.Runtime.CompilerServices.ConfiguredTaskAwaitable.ConfiguredTaskAwaiter[TResult]:
        ...

class ICriticalNotifyCompletion(System.Runtime.CompilerServices.INotifyCompletion, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    # methods
    @typing.overload
    @abc.abstractmethod
    def UnsafeOnCompleted(self, continuation: System.Action, ) -> None:
        ...

class INotifyCompletion(abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    # methods
    @typing.overload
    @abc.abstractmethod
    def OnCompleted(self, continuation: System.Action, ) -> None:
        ...

class CallSite(System.Runtime.CompilerServices.CallSite, typing.Generic[T]):
    @typing.overload
    def __init__(self, **kwargs):
        self.Target: T
        ...

    # properties
    @property
    def Update(self) -> T:
        ...

    @property
    def Binder(self) -> System.Runtime.CompilerServices.CallSiteBinder:
        ...

    # methods
    @typing.overload
    @staticmethod
    def Create(binder: System.Runtime.CompilerServices.CallSiteBinder, ) -> System.Runtime.CompilerServices.CallSite:
        ...

class ValueTaskAwaiter(System.Runtime.CompilerServices.ICriticalNotifyCompletion, System.Runtime.CompilerServices.INotifyCompletion, System.Runtime.CompilerServices.IStateMachineBoxAwareAwaiter, System.ValueType):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def IsCompleted(self) -> System.Boolean:
        ...

    # methods
    @typing.overload
    def GetResult(self, ) -> None:
        ...

    @typing.overload
    def OnCompleted(self, continuation: System.Action, ) -> None:
        ...

    @typing.overload
    def UnsafeOnCompleted(self, continuation: System.Action, ) -> None:
        ...

class ConfiguredValueTaskAwaitable(System.ValueType):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    # methods
    @typing.overload
    def GetAwaiter(self, ) -> System.Runtime.CompilerServices.ConfiguredValueTaskAwaitable.ConfiguredValueTaskAwaiter:
        ...

class ValueTaskAwaiter(System.Runtime.CompilerServices.ICriticalNotifyCompletion, System.Runtime.CompilerServices.INotifyCompletion, System.Runtime.CompilerServices.IStateMachineBoxAwareAwaiter, System.ValueType, typing.Generic[TResult]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def IsCompleted(self) -> System.Boolean:
        ...

    # methods
    @typing.overload
    def GetResult(self, ) -> TResult:
        ...

    @typing.overload
    def OnCompleted(self, continuation: System.Action, ) -> None:
        ...

    @typing.overload
    def UnsafeOnCompleted(self, continuation: System.Action, ) -> None:
        ...

class ConfiguredValueTaskAwaitable(System.ValueType, typing.Generic[TResult]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    # methods
    @typing.overload
    def GetAwaiter(self, ) -> System.Runtime.CompilerServices.ConfiguredValueTaskAwaitable.ConfiguredValueTaskAwaiter[TResult]:
        ...

class CallSite(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def Binder(self) -> System.Runtime.CompilerServices.CallSiteBinder:
        ...

    # methods
    @typing.overload
    @staticmethod
    def Create(delegateType: System.Type, binder: System.Runtime.CompilerServices.CallSiteBinder, ) -> System.Runtime.CompilerServices.CallSite:
        ...

