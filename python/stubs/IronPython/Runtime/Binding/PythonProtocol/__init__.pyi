from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import System
import IronPython.Runtime.Binding.PythonProtocol
import System.Dynamic
import IronPython.Runtime
import IronPython.Runtime.Types
import IronPython.Runtime.Binding
import System.Runtime.Serialization
import System.Reflection
import System.Linq.Expressions


class IndexBuilder(System.Object, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def Callable(self) -> IronPython.Runtime.Binding.PythonProtocol.Callable:
        ...

    # methods
    def __init__(self, types: System.Array[System.Dynamic.DynamicMetaObject], callable: IronPython.Runtime.Binding.PythonProtocol.Callable, ):
        ...

    @abc.abstractmethod
    def MakeRule(self, metaBinder: System.Dynamic.DynamicMetaObjectBinder, binder: IronPython.Runtime.PythonContext, args: System.Array[System.Dynamic.DynamicMetaObject], ) -> System.Dynamic.DynamicMetaObject:
        ...

    def GetTypeAt(self, index: int, ) -> IronPython.Runtime.Types.PythonType:
        ...

class SlotCallable(IronPython.Runtime.Binding.PythonProtocol.Callable):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def Binder(self) -> IronPython.Runtime.Binding.PythonBinder:
        ...

    @property
    def PythonContext(self) -> IronPython.Runtime.PythonContext:
        ...

    @property
    def IsSetter(self) -> bool:
        ...

    # methods
    def __init__(self, binder: IronPython.Runtime.PythonContext, op: int, slot: IronPython.Runtime.Types.PythonTypeSlot, ):
        ...

    def CompleteRuleTarget(self, metaBinder: System.Dynamic.DynamicMetaObjectBinder, args: System.Array[System.Dynamic.DynamicMetaObject], customFailure: System.Func[System.Dynamic.DynamicMetaObject], ) -> System.Dynamic.DynamicMetaObject:
        ...

class BuiltinCallable(IronPython.Runtime.Binding.PythonProtocol.Callable):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def Binder(self) -> IronPython.Runtime.Binding.PythonBinder:
        ...

    @property
    def PythonContext(self) -> IronPython.Runtime.PythonContext:
        ...

    @property
    def IsSetter(self) -> bool:
        ...

    # methods
    def __init__(self, binder: IronPython.Runtime.PythonContext, op: int, func: IronPython.Runtime.Types.BuiltinFunction, ):
        ...

    def GetTupleArguments(self, arguments: System.Array[System.Dynamic.DynamicMetaObject], ) -> System.Array[System.Dynamic.DynamicMetaObject]:
        ...

    def CompleteRuleTarget(self, metaBinder: System.Dynamic.DynamicMetaObjectBinder, args: System.Array[System.Dynamic.DynamicMetaObject], customFailure: System.Func[System.Dynamic.DynamicMetaObject], ) -> System.Dynamic.DynamicMetaObject:
        ...

class ComparisonHelper(System.ICloneable, System.Runtime.Serialization.ISerializable, System.MulticastDelegate):
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

    def Invoke(self, bodyBuilder: IronPython.Runtime.Binding.ConditionalBuilder, retCondition: System.Linq.Expressions.Expression, retValue: System.Linq.Expressions.Expression, isReverse: bool, retType: System.Type, ) -> None:
        ...

    def BeginInvoke(self, bodyBuilder: IronPython.Runtime.Binding.ConditionalBuilder, retCondition: System.Linq.Expressions.Expression, retValue: System.Linq.Expressions.Expression, isReverse: bool, retType: System.Type, callback: System.AsyncCallback, object: System.Object, ) -> System.IAsyncResult:
        ...

    def EndInvoke(self, result: System.IAsyncResult, ) -> None:
        ...

class ItemBuilder(IronPython.Runtime.Binding.PythonProtocol.IndexBuilder):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def Callable(self) -> IronPython.Runtime.Binding.PythonProtocol.Callable:
        ...

    # methods
    def __init__(self, types: System.Array[System.Dynamic.DynamicMetaObject], callable: IronPython.Runtime.Binding.PythonProtocol.Callable, ):
        ...

    def MakeRule(self, metaBinder: System.Dynamic.DynamicMetaObjectBinder, binder: IronPython.Runtime.PythonContext, args: System.Array[System.Dynamic.DynamicMetaObject], ) -> System.Dynamic.DynamicMetaObject:
        ...

class Callable(System.Object, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def Binder(self) -> IronPython.Runtime.Binding.PythonBinder:
        ...

    @property
    def PythonContext(self) -> IronPython.Runtime.PythonContext:
        ...

    @property
    def IsSetter(self) -> bool:
        ...

    # methods
    def __init__(self, binder: IronPython.Runtime.PythonContext, op: int, ):
        ...

    @staticmethod
    def MakeCallable(binder: IronPython.Runtime.PythonContext, op: int, itemFunc: IronPython.Runtime.Types.BuiltinFunction, itemSlot: IronPython.Runtime.Types.PythonTypeSlot, ) -> IronPython.Runtime.Binding.PythonProtocol.Callable:
        ...

    def GetTupleArguments(self, arguments: System.Array[System.Dynamic.DynamicMetaObject], ) -> System.Array[System.Dynamic.DynamicMetaObject]:
        ...

    @abc.abstractmethod
    def CompleteRuleTarget(self, metaBinder: System.Dynamic.DynamicMetaObjectBinder, args: System.Array[System.Dynamic.DynamicMetaObject], customFailure: System.Func[System.Dynamic.DynamicMetaObject], ) -> System.Dynamic.DynamicMetaObject:
        ...

