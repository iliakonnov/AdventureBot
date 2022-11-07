from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import IronPython.Runtime.Binding.MetaPythonType
import System.Dynamic
import IronPython.Runtime
import System.Linq.Expressions
import IronPython.Runtime.Types
import IronPython.Runtime.Binding
import System
import System.Runtime.CompilerServices
import System.Collections.Generic
import Microsoft.Scripting.Actions

TResult = typing.TypeVar('TResult')

class MetaGetBinderHelper(IronPython.Runtime.Binding.MetaPythonType.GetBinderHelper[System.Dynamic.DynamicMetaObject]):
    @typing.overload
    def __init__(self, **kwargs):
        self._context: IronPython.Runtime.CodeContext
        ...

    # static fields

    # properties
    @property
    def Expression(self) -> System.Linq.Expressions.Expression:
        ...

    @property
    def Restrictions(self) -> System.Dynamic.BindingRestrictions:
        ...

    @property
    def Value(self) -> IronPython.Runtime.Types.PythonType:
        ...

    # methods
    def __init__(self, type: IronPython.Runtime.Binding.MetaPythonType, member: System.Dynamic.DynamicMetaObjectBinder, codeContext: System.Linq.Expressions.Expression, validationInfo: IronPython.Runtime.Binding.ValidationInfo, metaValidation: IronPython.Runtime.Binding.ValidationInfo, ):
        ...

    def EnsureTmp(self, ) -> None:
        ...

    def AddSlotAccess(self, pt: IronPython.Runtime.Types.PythonType, pts: IronPython.Runtime.Types.PythonTypeSlot, ) -> bool:
        ...

    def AddError(self, ) -> None:
        ...

    def AddMetaGetAttribute(self, metaType: IronPython.Runtime.Types.PythonType, pts: IronPython.Runtime.Types.PythonTypeSlot, ) -> None:
        ...

    def AddMetaSlotAccess(self, metaType: IronPython.Runtime.Types.PythonType, pts: IronPython.Runtime.Types.PythonTypeSlot, ) -> bool:
        ...

    def Finish(self, metaOnly: bool, ) -> System.Dynamic.DynamicMetaObject:
        ...

    def GetFallbackError(self, member: System.Dynamic.DynamicMetaObjectBinder, ) -> System.Dynamic.DynamicMetaObject:
        ...

class DefaultNewAdapter(IronPython.Runtime.Binding.MetaPythonType.NewAdapter):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def PythonContext(self) -> IronPython.Runtime.PythonContext:
        ...

    @property
    def CodeContext(self) -> System.Linq.Expressions.Expression:
        ...

    @property
    def Arguments(self) -> IronPython.Runtime.Binding.MetaPythonType.ArgumentValues:
        ...

    # methods
    def __init__(self, ai: IronPython.Runtime.Binding.MetaPythonType.ArgumentValues, creating: IronPython.Runtime.Types.PythonType, state: IronPython.Runtime.PythonContext, codeContext: System.Linq.Expressions.Expression, ):
        ...

    def GetExpression(self, binder: IronPython.Runtime.Binding.PythonBinder, ) -> System.Dynamic.DynamicMetaObject:
        ...

class ConstructorNewAdapter(IronPython.Runtime.Binding.MetaPythonType.NewAdapter):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def PythonContext(self) -> IronPython.Runtime.PythonContext:
        ...

    @property
    def CodeContext(self) -> System.Linq.Expressions.Expression:
        ...

    @property
    def Arguments(self) -> IronPython.Runtime.Binding.MetaPythonType.ArgumentValues:
        ...

    # methods
    def __init__(self, ai: IronPython.Runtime.Binding.MetaPythonType.ArgumentValues, creating: IronPython.Runtime.Types.PythonType, state: IronPython.Runtime.PythonContext, codeContext: System.Linq.Expressions.Expression, ):
        ...

    def GetExpression(self, binder: IronPython.Runtime.Binding.PythonBinder, ) -> System.Dynamic.DynamicMetaObject:
        ...

class BuiltinInitAdapter(IronPython.Runtime.Binding.MetaPythonType.InitAdapter):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def PythonContext(self) -> IronPython.Runtime.PythonContext:
        ...

    @property
    def CodeContext(self) -> System.Linq.Expressions.Expression:
        ...

    @property
    def Arguments(self) -> IronPython.Runtime.Binding.MetaPythonType.ArgumentValues:
        ...

    # methods
    def __init__(self, ai: IronPython.Runtime.Binding.MetaPythonType.ArgumentValues, method: IronPython.Runtime.Types.BuiltinFunction, state: IronPython.Runtime.PythonContext, codeContext: System.Linq.Expressions.Expression, ):
        ...

    def MakeInitCall(self, binder: IronPython.Runtime.Binding.PythonBinder, createExpr: System.Dynamic.DynamicMetaObject, ) -> System.Dynamic.DynamicMetaObject:
        ...

class InitAdapter(IronPython.Runtime.Binding.MetaPythonType.CallAdapter, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def PythonContext(self) -> IronPython.Runtime.PythonContext:
        ...

    @property
    def CodeContext(self) -> System.Linq.Expressions.Expression:
        ...

    @property
    def Arguments(self) -> IronPython.Runtime.Binding.MetaPythonType.ArgumentValues:
        ...

    # methods
    def __init__(self, ai: IronPython.Runtime.Binding.MetaPythonType.ArgumentValues, state: IronPython.Runtime.PythonContext, codeContext: System.Linq.Expressions.Expression, ):
        ...

    @abc.abstractmethod
    def MakeInitCall(self, binder: IronPython.Runtime.Binding.PythonBinder, createExpr: System.Dynamic.DynamicMetaObject, ) -> System.Dynamic.DynamicMetaObject:
        ...

    def MakeDefaultInit(self, binder: IronPython.Runtime.Binding.PythonBinder, createExpr: System.Dynamic.DynamicMetaObject, init: System.Linq.Expressions.Expression, ) -> System.Dynamic.DynamicMetaObject:
        ...

class CallAdapter(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def PythonContext(self) -> IronPython.Runtime.PythonContext:
        ...

    @property
    def CodeContext(self) -> System.Linq.Expressions.Expression:
        ...

    @property
    def Arguments(self) -> IronPython.Runtime.Binding.MetaPythonType.ArgumentValues:
        ...

    # methods
    def __init__(self, ai: IronPython.Runtime.Binding.MetaPythonType.ArgumentValues, state: IronPython.Runtime.PythonContext, codeContext: System.Linq.Expressions.Expression, ):
        ...

class FastGetBinderHelper(IronPython.Runtime.Binding.MetaPythonType.GetBinderHelper[IronPython.Runtime.Types.TypeGetBase]):
    @typing.overload
    def __init__(self, **kwargs):
        self._context: IronPython.Runtime.CodeContext
        ...

    # static fields

    # properties
    @property
    def Value(self) -> IronPython.Runtime.Types.PythonType:
        ...

    # methods
    def __init__(self, type: IronPython.Runtime.Types.PythonType, context: IronPython.Runtime.CodeContext, binder: IronPython.Runtime.Binding.PythonGetMemberBinder, ):
        ...

    def GetBinding(self, ) -> System.Func[System.Runtime.CompilerServices.CallSite, System.Object, IronPython.Runtime.CodeContext, System.Object]:
        ...

    def GetCachedGets(self, ) -> System.Collections.Generic.Dictionary[str, IronPython.Runtime.Types.TypeGetBase]:
        ...

    def AddSlotAccess(self, pt: IronPython.Runtime.Types.PythonType, pts: IronPython.Runtime.Types.PythonTypeSlot, ) -> bool:
        ...

    def AddError(self, ) -> None:
        ...

    def AddMetaGetAttribute(self, metaType: IronPython.Runtime.Types.PythonType, pts: IronPython.Runtime.Types.PythonTypeSlot, ) -> None:
        ...

    def AddMetaSlotAccess(self, metaType: IronPython.Runtime.Types.PythonType, pts: IronPython.Runtime.Types.PythonTypeSlot, ) -> bool:
        ...

    def Finish(self, metaOnly: bool, ) -> IronPython.Runtime.Types.TypeGetBase:
        ...

class ArgumentValues(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        self.Self: System.Dynamic.DynamicMetaObject
        self.Arguments: System.Array[System.Dynamic.DynamicMetaObject]
        self.Signature: Microsoft.Scripting.Actions.CallSignature
        ...

    # static fields

    # properties
    # methods
    def __init__(self, signature: Microsoft.Scripting.Actions.CallSignature, self: System.Dynamic.DynamicMetaObject, args: System.Array[System.Dynamic.DynamicMetaObject], ):
        ...

class NewAdapter(IronPython.Runtime.Binding.MetaPythonType.CallAdapter):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def PythonContext(self) -> IronPython.Runtime.PythonContext:
        ...

    @property
    def CodeContext(self) -> System.Linq.Expressions.Expression:
        ...

    @property
    def Arguments(self) -> IronPython.Runtime.Binding.MetaPythonType.ArgumentValues:
        ...

    # methods
    def __init__(self, ai: IronPython.Runtime.Binding.MetaPythonType.ArgumentValues, state: IronPython.Runtime.PythonContext, codeContext: System.Linq.Expressions.Expression, ):
        ...

    def GetExpression(self, binder: IronPython.Runtime.Binding.PythonBinder, ) -> System.Dynamic.DynamicMetaObject:
        ...

    def MakeDefaultNew(self, binder: Microsoft.Scripting.Actions.DefaultBinder, function: System.Linq.Expressions.Expression, ) -> System.Dynamic.DynamicMetaObject:
        ...

    def AppendNewArgs(self, args: System.Collections.Generic.List[System.Linq.Expressions.Expression], ) -> None:
        ...

    def GetDynamicNewSignature(self, ) -> Microsoft.Scripting.Actions.CallSignature:
        ...

class BuiltinNewAdapter(IronPython.Runtime.Binding.MetaPythonType.NewAdapter):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def PythonContext(self) -> IronPython.Runtime.PythonContext:
        ...

    @property
    def CodeContext(self) -> System.Linq.Expressions.Expression:
        ...

    @property
    def Arguments(self) -> IronPython.Runtime.Binding.MetaPythonType.ArgumentValues:
        ...

    # methods
    def __init__(self, ai: IronPython.Runtime.Binding.MetaPythonType.ArgumentValues, creating: IronPython.Runtime.Types.PythonType, ctor: IronPython.Runtime.Types.BuiltinFunction, state: IronPython.Runtime.PythonContext, codeContext: System.Linq.Expressions.Expression, ):
        ...

    def GetExpression(self, binder: IronPython.Runtime.Binding.PythonBinder, ) -> System.Dynamic.DynamicMetaObject:
        ...

class DefaultInitAdapter(IronPython.Runtime.Binding.MetaPythonType.InitAdapter):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def PythonContext(self) -> IronPython.Runtime.PythonContext:
        ...

    @property
    def CodeContext(self) -> System.Linq.Expressions.Expression:
        ...

    @property
    def Arguments(self) -> IronPython.Runtime.Binding.MetaPythonType.ArgumentValues:
        ...

    # methods
    def __init__(self, ai: IronPython.Runtime.Binding.MetaPythonType.ArgumentValues, state: IronPython.Runtime.PythonContext, codeContext: System.Linq.Expressions.Expression, ):
        ...

    def MakeInitCall(self, binder: IronPython.Runtime.Binding.PythonBinder, createExpr: System.Dynamic.DynamicMetaObject, ) -> System.Dynamic.DynamicMetaObject:
        ...

class GetBinderHelper(System.Object, abc.ABC, typing.Generic[TResult]):
    @typing.overload
    def __init__(self, **kwargs):
        self._context: IronPython.Runtime.CodeContext
        ...

    # static fields

    # properties
    @property
    def Value(self) -> IronPython.Runtime.Types.PythonType:
        ...

    # methods
    def __init__(self, value: IronPython.Runtime.Types.PythonType, context: IronPython.Runtime.CodeContext, name: str, ):
        ...

    @abc.abstractmethod
    def Finish(self, metaOnly: bool, ) -> TResult:
        ...

    @abc.abstractmethod
    def AddError(self, ) -> None:
        ...

    @abc.abstractmethod
    def AddMetaGetAttribute(self, metaType: IronPython.Runtime.Types.PythonType, pts: IronPython.Runtime.Types.PythonTypeSlot, ) -> None:
        ...

    @abc.abstractmethod
    def AddMetaSlotAccess(self, pt: IronPython.Runtime.Types.PythonType, pts: IronPython.Runtime.Types.PythonTypeSlot, ) -> bool:
        ...

    @abc.abstractmethod
    def AddSlotAccess(self, pt: IronPython.Runtime.Types.PythonType, pts: IronPython.Runtime.Types.PythonTypeSlot, ) -> bool:
        ...

    def MakeTypeGetMember(self, ) -> TResult:
        ...

class SlotInitAdapter(IronPython.Runtime.Binding.MetaPythonType.InitAdapter):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def PythonContext(self) -> IronPython.Runtime.PythonContext:
        ...

    @property
    def CodeContext(self) -> System.Linq.Expressions.Expression:
        ...

    @property
    def Arguments(self) -> IronPython.Runtime.Binding.MetaPythonType.ArgumentValues:
        ...

    # methods
    def __init__(self, slot: IronPython.Runtime.Types.PythonTypeSlot, ai: IronPython.Runtime.Binding.MetaPythonType.ArgumentValues, state: IronPython.Runtime.PythonContext, codeContext: System.Linq.Expressions.Expression, ):
        ...

    def MakeInitCall(self, binder: IronPython.Runtime.Binding.PythonBinder, createExpr: System.Dynamic.DynamicMetaObject, ) -> System.Dynamic.DynamicMetaObject:
        ...

