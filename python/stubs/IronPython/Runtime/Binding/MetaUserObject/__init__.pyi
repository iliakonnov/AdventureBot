from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import IronPython.Runtime.Binding.MetaUserObject
import System.Dynamic
import IronPython.Runtime.Binding
import IronPython.Runtime.Types
import System.Linq.Expressions
import IronPython.Runtime
import System
import System.Runtime.CompilerServices
import System.Collections.Generic

TValue = typing.TypeVar('TValue')
TResult = typing.TypeVar('TResult')

class SetBindingInfo(IronPython.Runtime.Binding.MetaUserObject.MemberBindingInfo):
    @typing.overload
    def __init__(self, **kwargs):
        self.Action: System.Dynamic.SetMemberBinder
        self.Body: IronPython.Runtime.Binding.ConditionalBuilder
        self.Args: System.Array[System.Dynamic.DynamicMetaObject]
        self.Validation: IronPython.Runtime.Binding.ValidationInfo
        ...

    # static fields

    # properties
    # methods
    def __init__(self, action: System.Dynamic.SetMemberBinder, args: System.Array[System.Dynamic.DynamicMetaObject], body: IronPython.Runtime.Binding.ConditionalBuilder, validation: IronPython.Runtime.Binding.ValidationInfo, ):
        ...

class MetaGetBinderHelper(IronPython.Runtime.Binding.MetaUserObject.GetOrInvokeBinderHelper[System.Dynamic.DynamicMetaObject], abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        self._target: IronPython.Runtime.Binding.MetaUserObject
        self._codeContext: System.Dynamic.DynamicMetaObject
        self._value: IronPython.Runtime.Types.IPythonObject
        self._extensionMethodRestriction: bool
        ...

    # static fields

    # properties
    @property
    def IsFinal(self) -> bool:
        ...

    @property
    def Expression(self) -> System.Linq.Expressions.Expression:
        ...

    @property
    def Value(self) -> IronPython.Runtime.Types.IPythonObject:
        ...

    # methods
    def __init__(self, target: IronPython.Runtime.Binding.MetaUserObject, binder: System.Dynamic.DynamicMetaObjectBinder, codeContext: System.Dynamic.DynamicMetaObject, ):
        ...

    def MakeGetAttributeRule(self, info: IronPython.Runtime.Binding.MetaUserObject.GetBindingInfo, obj: IronPython.Runtime.Types.IPythonObject, slot: IronPython.Runtime.Types.PythonTypeSlot, codeContext: System.Dynamic.DynamicMetaObject, ) -> System.Dynamic.DynamicMetaObject:
        ...

    @abc.abstractmethod
    def FallbackError(self, ) -> System.Dynamic.DynamicMetaObject:
        ...

    @abc.abstractmethod
    def Fallback(self, ) -> System.Dynamic.DynamicMetaObject:
        ...

    @typing.overload
    def Invoke(self, res: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.Expression:
        ...

    @typing.overload
    def Invoke(self, res: System.Dynamic.DynamicMetaObject, ) -> System.Dynamic.DynamicMetaObject:
        ...

    def BindGetAttribute(self, foundSlot: IronPython.Runtime.Types.PythonTypeSlot, ) -> System.Dynamic.DynamicMetaObject:
        ...

    def MakeGetAttrAccess(self, getattr: IronPython.Runtime.Types.PythonTypeSlot, ) -> None:
        ...

    def MakeTypeError(self, ) -> None:
        ...

    def FinishRule(self, ) -> System.Dynamic.DynamicMetaObject:
        ...

    def MakeGetAttrRule(self, info: IronPython.Runtime.Binding.MetaUserObject.GetBindingInfo, getattr: System.Linq.Expressions.Expression, codeContext: System.Dynamic.DynamicMetaObject, ) -> None:
        ...

    def MakeGetAttrCall(self, info: IronPython.Runtime.Binding.MetaUserObject.GetBindingInfo, codeContext: System.Dynamic.DynamicMetaObject, ) -> System.Linq.Expressions.Expression:
        ...

    def MaybeMakeNoThrow(self, info: IronPython.Runtime.Binding.MetaUserObject.GetBindingInfo, expr: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.Expression:
        ...

    @typing.overload
    def MakeSlotAccess(self, foundSlot: IronPython.Runtime.Types.PythonTypeSlot, systemTypeResolution: bool, ) -> None:
        ...

    @typing.overload
    def MakeSlotAccess(self, dts: IronPython.Runtime.Types.PythonTypeSlot, ) -> None:
        ...

    def MakeDictionaryAccess(self, ) -> None:
        ...

class FastSetBinderHelper(IronPython.Runtime.Binding.MetaUserObject.SetBinderHelper[IronPython.Runtime.Types.SetMemberDelegates[TValue]], typing.Generic[TValue]):
    @typing.overload
    def __init__(self, **kwargs):
        self._context: IronPython.Runtime.CodeContext
        ...

    # static fields

    # properties
    @property
    def Instance(self) -> IronPython.Runtime.Types.IPythonObject:
        ...

    @property
    def Value(self) -> System.Object:
        ...

    # methods
    def __init__(self, context: IronPython.Runtime.CodeContext, self: IronPython.Runtime.Types.IPythonObject, value: System.Object, binder: IronPython.Runtime.Binding.PythonSetMemberBinder, ):
        ...

    def Finish(self, ) -> IronPython.Runtime.Types.SetMemberDelegates[TValue]:
        ...

    def MakeSet(self, ) -> IronPython.Runtime.Binding.FastBindResult[System.Func[System.Runtime.CompilerServices.CallSite, System.Object, TValue, System.Object]]:
        ...

    def GetCachedSets(self, ) -> System.Collections.Generic.Dictionary[IronPython.Runtime.Types.SetMemberKey, IronPython.Runtime.Binding.FastSetBase]:
        ...

    def MakeSlotSetOrFallback(self, dts: IronPython.Runtime.Types.PythonTypeSlot, systemTypeResolution: bool, ) -> None:
        ...

    def MakeSlotsSetTarget(self, prop: IronPython.Runtime.Types.ReflectedSlotProperty, ) -> None:
        ...

    def MakeFallback(self, ) -> None:
        ...

    def MakeSetAttrTarget(self, dts: IronPython.Runtime.Types.PythonTypeSlot, ) -> None:
        ...

    def MakeDictionarySetTarget(self, ) -> None:
        ...

class DeleteBindingInfo(IronPython.Runtime.Binding.MetaUserObject.MemberBindingInfo):
    @typing.overload
    def __init__(self, **kwargs):
        self.Action: System.Dynamic.DeleteMemberBinder
        self.Body: IronPython.Runtime.Binding.ConditionalBuilder
        self.Args: System.Array[System.Dynamic.DynamicMetaObject]
        self.Validation: IronPython.Runtime.Binding.ValidationInfo
        ...

    # static fields

    # properties
    # methods
    def __init__(self, action: System.Dynamic.DeleteMemberBinder, args: System.Array[System.Dynamic.DynamicMetaObject], body: IronPython.Runtime.Binding.ConditionalBuilder, validation: IronPython.Runtime.Binding.ValidationInfo, ):
        ...

class MetaSetBinderHelper(IronPython.Runtime.Binding.MetaUserObject.SetBinderHelper[System.Dynamic.DynamicMetaObject]):
    @typing.overload
    def __init__(self, **kwargs):
        self._context: IronPython.Runtime.CodeContext
        ...

    # static fields

    # properties
    @property
    def Instance(self) -> IronPython.Runtime.Types.IPythonObject:
        ...

    @property
    def Value(self) -> System.Object:
        ...

    # methods
    def __init__(self, target: IronPython.Runtime.Binding.MetaUserObject, value: System.Dynamic.DynamicMetaObject, binder: System.Dynamic.SetMemberBinder, ):
        ...

    def MakeSetAttrTarget(self, dts: IronPython.Runtime.Types.PythonTypeSlot, ) -> None:
        ...

    def Finish(self, ) -> System.Dynamic.DynamicMetaObject:
        ...

    def MakeFallback(self, ) -> None:
        ...

    def MakeDictionarySetTarget(self, ) -> None:
        ...

    def MakeSlotSetOrFallback(self, dts: IronPython.Runtime.Types.PythonTypeSlot, systemTypeResolution: bool, ) -> None:
        ...

    def MakeSlotsSetTarget(self, prop: IronPython.Runtime.Types.ReflectedSlotProperty, ) -> None:
        ...

    def FallbackSetError(self, action: System.Dynamic.SetMemberBinder, value: System.Dynamic.DynamicMetaObject, ) -> System.Dynamic.DynamicMetaObject:
        ...

class MemberBindingInfo(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        self.Body: IronPython.Runtime.Binding.ConditionalBuilder
        self.Args: System.Array[System.Dynamic.DynamicMetaObject]
        self.Validation: IronPython.Runtime.Binding.ValidationInfo
        ...

    # static fields

    # properties
    # methods
    def __init__(self, args: System.Array[System.Dynamic.DynamicMetaObject], body: IronPython.Runtime.Binding.ConditionalBuilder, validation: IronPython.Runtime.Binding.ValidationInfo, ):
        ...

class FastGetBinderHelper(IronPython.Runtime.Binding.MetaUserObject.GetOrInvokeBinderHelper[IronPython.Runtime.Binding.FastGetBase]):
    @typing.overload
    def __init__(self, **kwargs):
        self._value: IronPython.Runtime.Types.IPythonObject
        self._extensionMethodRestriction: bool
        ...

    # static fields

    # properties
    @property
    def IsFinal(self) -> bool:
        ...

    @property
    def Value(self) -> IronPython.Runtime.Types.IPythonObject:
        ...

    # methods
    def __init__(self, context: IronPython.Runtime.CodeContext, site: System.Runtime.CompilerServices.CallSite[System.Func[System.Runtime.CompilerServices.CallSite, System.Object, IronPython.Runtime.CodeContext, System.Object]], value: IronPython.Runtime.Types.IPythonObject, binder: IronPython.Runtime.Binding.PythonGetMemberBinder, ):
        ...

    def MakeTypeError(self, ) -> None:
        ...

    def MakeSlotAccess(self, foundSlot: IronPython.Runtime.Types.PythonTypeSlot, systemTypeResolution: bool, ) -> None:
        ...

    def GetBinding(self, context: IronPython.Runtime.CodeContext, name: str, ) -> IronPython.Runtime.Binding.FastBindResult[System.Func[System.Runtime.CompilerServices.CallSite, System.Object, IronPython.Runtime.CodeContext, System.Object]]:
        ...

    def GetCachedGets(self, ) -> System.Collections.Generic.Dictionary[IronPython.Runtime.Types.CachedGetKey, IronPython.Runtime.Binding.FastGetBase]:
        ...

    def FinishRule(self, ) -> IronPython.Runtime.Binding.FastGetBase:
        ...

    def FallbackError(self, ) -> System.Func[System.Runtime.CompilerServices.CallSite, System.Object, IronPython.Runtime.CodeContext, System.Object]:
        ...

    def MakeDictionaryAccess(self, ) -> None:
        ...

    def BindGetAttribute(self, foundSlot: IronPython.Runtime.Types.PythonTypeSlot, ) -> IronPython.Runtime.Binding.FastGetBase:
        ...

    def MakeGetAttrAccess(self, getattr: IronPython.Runtime.Types.PythonTypeSlot, ) -> None:
        ...

class GetBinderHelper(IronPython.Runtime.Binding.MetaUserObject.MetaGetBinderHelper):
    @typing.overload
    def __init__(self, **kwargs):
        self._target: IronPython.Runtime.Binding.MetaUserObject
        self._codeContext: System.Dynamic.DynamicMetaObject
        self._value: IronPython.Runtime.Types.IPythonObject
        self._extensionMethodRestriction: bool
        ...

    # static fields

    # properties
    @property
    def IsFinal(self) -> bool:
        ...

    @property
    def Expression(self) -> System.Linq.Expressions.Expression:
        ...

    @property
    def Value(self) -> IronPython.Runtime.Types.IPythonObject:
        ...

    # methods
    def __init__(self, target: IronPython.Runtime.Binding.MetaUserObject, binder: System.Dynamic.DynamicMetaObjectBinder, codeContext: System.Dynamic.DynamicMetaObject, ):
        ...

    def Fallback(self, ) -> System.Dynamic.DynamicMetaObject:
        ...

    def FallbackError(self, ) -> System.Dynamic.DynamicMetaObject:
        ...

class GetBindingInfo(IronPython.Runtime.Binding.MetaUserObject.MemberBindingInfo):
    @typing.overload
    def __init__(self, **kwargs):
        self.Action: System.Dynamic.DynamicMetaObjectBinder
        self.Self: System.Linq.Expressions.ParameterExpression
        self.Result: System.Linq.Expressions.ParameterExpression
        self.Body: IronPython.Runtime.Binding.ConditionalBuilder
        self.Args: System.Array[System.Dynamic.DynamicMetaObject]
        self.Validation: IronPython.Runtime.Binding.ValidationInfo
        ...

    # static fields

    # properties
    # methods
    def __init__(self, action: System.Dynamic.DynamicMetaObjectBinder, args: System.Array[System.Dynamic.DynamicMetaObject], self: System.Linq.Expressions.ParameterExpression, result: System.Linq.Expressions.ParameterExpression, body: IronPython.Runtime.Binding.ConditionalBuilder, validationInfo: IronPython.Runtime.Binding.ValidationInfo, ):
        ...

class GetOrInvokeBinderHelper(System.Object, abc.ABC, typing.Generic[TResult]):
    @typing.overload
    def __init__(self, **kwargs):
        self._value: IronPython.Runtime.Types.IPythonObject
        self._extensionMethodRestriction: bool
        ...

    # static fields

    # properties
    @property
    @abc.abstractmethod
    def IsFinal(self) -> bool:
        ...

    @property
    def Value(self) -> IronPython.Runtime.Types.IPythonObject:
        ...

    # methods
    def __init__(self, value: IronPython.Runtime.Types.IPythonObject, ):
        ...

    def Bind(self, context: IronPython.Runtime.CodeContext, name: str, ) -> TResult:
        ...

    @abc.abstractmethod
    def MakeTypeError(self, ) -> None:
        ...

    @abc.abstractmethod
    def MakeGetAttrAccess(self, getattr: IronPython.Runtime.Types.PythonTypeSlot, ) -> None:
        ...

    @abc.abstractmethod
    def MakeSlotAccess(self, foundSlot: IronPython.Runtime.Types.PythonTypeSlot, systemTypeResolution: bool, ) -> None:
        ...

    @abc.abstractmethod
    def BindGetAttribute(self, foundSlot: IronPython.Runtime.Types.PythonTypeSlot, ) -> TResult:
        ...

    @abc.abstractmethod
    def FinishRule(self, ) -> TResult:
        ...

    @abc.abstractmethod
    def MakeDictionaryAccess(self, ) -> None:
        ...

class SetBinderHelper(System.Object, abc.ABC, typing.Generic[TResult]):
    @typing.overload
    def __init__(self, **kwargs):
        self._context: IronPython.Runtime.CodeContext
        ...

    # static fields

    # properties
    @property
    def Instance(self) -> IronPython.Runtime.Types.IPythonObject:
        ...

    @property
    def Value(self) -> System.Object:
        ...

    # methods
    def __init__(self, context: IronPython.Runtime.CodeContext, instance: IronPython.Runtime.Types.IPythonObject, value: System.Object, ):
        ...

    def Bind(self, name: str, ) -> TResult:
        ...

    @abc.abstractmethod
    def Finish(self, ) -> TResult:
        ...

    @abc.abstractmethod
    def MakeSetAttrTarget(self, dts: IronPython.Runtime.Types.PythonTypeSlot, ) -> None:
        ...

    @abc.abstractmethod
    def MakeSlotsSetTarget(self, prop: IronPython.Runtime.Types.ReflectedSlotProperty, ) -> None:
        ...

    @abc.abstractmethod
    def MakeSlotSetOrFallback(self, dts: IronPython.Runtime.Types.PythonTypeSlot, systemTypeResolution: bool, ) -> None:
        ...

    @abc.abstractmethod
    def MakeDictionarySetTarget(self, ) -> None:
        ...

    @abc.abstractmethod
    def MakeFallback(self, ) -> None:
        ...

class InvokeBinderHelper(IronPython.Runtime.Binding.MetaUserObject.MetaGetBinderHelper):
    @typing.overload
    def __init__(self, **kwargs):
        self._target: IronPython.Runtime.Binding.MetaUserObject
        self._codeContext: System.Dynamic.DynamicMetaObject
        self._value: IronPython.Runtime.Types.IPythonObject
        self._extensionMethodRestriction: bool
        ...

    # static fields

    # properties
    @property
    def IsFinal(self) -> bool:
        ...

    @property
    def Expression(self) -> System.Linq.Expressions.Expression:
        ...

    @property
    def Value(self) -> IronPython.Runtime.Types.IPythonObject:
        ...

    # methods
    def __init__(self, target: IronPython.Runtime.Binding.MetaUserObject, binder: System.Dynamic.InvokeMemberBinder, args: System.Array[System.Dynamic.DynamicMetaObject], codeContext: System.Dynamic.DynamicMetaObject, ):
        ...

    def Fallback(self, ) -> System.Dynamic.DynamicMetaObject:
        ...

    def FallbackError(self, ) -> System.Dynamic.DynamicMetaObject:
        ...

    def Invoke(self, res: System.Dynamic.DynamicMetaObject, ) -> System.Dynamic.DynamicMetaObject:
        ...

