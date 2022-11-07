from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import System.Runtime.CompilerServices
import System.Collections.Generic
import System
import System.Collections.ObjectModel
import System.Linq.Expressions
import System.Dynamic


class DynamicMetaObjectBinder(System.Runtime.CompilerServices.CallSiteBinder, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        self.Cache: System.Collections.Generic.Dictionary[System.Type, System.Object]
        ...

    # static fields

    # properties
    @property
    def ReturnType(self) -> System.Type:
        ...

    @property
    def IsStandardBinder(self) -> bool:
        ...

    # methods
    def __init__(self, ):
        ...

    @typing.overload
    def Bind(self, args: System.Array[System.Object], parameters: System.Collections.ObjectModel.ReadOnlyCollection[System.Linq.Expressions.ParameterExpression], returnLabel: System.Linq.Expressions.LabelTarget, ) -> System.Linq.Expressions.Expression:
        ...

    @abc.abstractmethod
    @typing.overload
    def Bind(self, target: System.Dynamic.DynamicMetaObject, args: System.Array[System.Dynamic.DynamicMetaObject], ) -> System.Dynamic.DynamicMetaObject:
        ...

    @staticmethod
    def CreateArgumentMetaObjects(args: System.Array[System.Object], parameters: System.Collections.ObjectModel.ReadOnlyCollection[System.Linq.Expressions.ParameterExpression], ) -> System.Array[System.Dynamic.DynamicMetaObject]:
        ...

    def GetUpdateExpression(self, type: System.Type, ) -> System.Linq.Expressions.Expression:
        ...

    @typing.overload
    def Defer(self, target: System.Dynamic.DynamicMetaObject, args: System.Array[System.Dynamic.DynamicMetaObject], ) -> System.Dynamic.DynamicMetaObject:
        ...

    @typing.overload
    def Defer(self, args: System.Array[System.Dynamic.DynamicMetaObject], ) -> System.Dynamic.DynamicMetaObject:
        ...

    def MakeDeferred(self, rs: System.Dynamic.BindingRestrictions, args: System.Array[System.Dynamic.DynamicMetaObject], ) -> System.Dynamic.DynamicMetaObject:
        ...

class UnaryOperationBinder(System.Dynamic.DynamicMetaObjectBinder, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        self.Cache: System.Collections.Generic.Dictionary[System.Type, System.Object]
        ...

    # static fields

    # properties
    @property
    def ReturnType(self) -> System.Type:
        ...

    @property
    def Operation(self) -> int:
        ...

    @property
    def IsStandardBinder(self) -> bool:
        ...

    # methods
    def __init__(self, operation: int, ):
        ...

    @typing.overload
    def FallbackUnaryOperation(self, target: System.Dynamic.DynamicMetaObject, ) -> System.Dynamic.DynamicMetaObject:
        ...

    @abc.abstractmethod
    @typing.overload
    def FallbackUnaryOperation(self, target: System.Dynamic.DynamicMetaObject, errorSuggestion: System.Dynamic.DynamicMetaObject, ) -> System.Dynamic.DynamicMetaObject:
        ...

    def Bind(self, target: System.Dynamic.DynamicMetaObject, args: System.Array[System.Dynamic.DynamicMetaObject], ) -> System.Dynamic.DynamicMetaObject:
        ...

    @staticmethod
    def OperationIsValid(operation: int, ) -> bool:
        ...

class BinaryOperationBinder(System.Dynamic.DynamicMetaObjectBinder, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        self.Cache: System.Collections.Generic.Dictionary[System.Type, System.Object]
        ...

    # static fields

    # properties
    @property
    def ReturnType(self) -> System.Type:
        ...

    @property
    def Operation(self) -> int:
        ...

    @property
    def IsStandardBinder(self) -> bool:
        ...

    # methods
    def __init__(self, operation: int, ):
        ...

    @abc.abstractmethod
    @typing.overload
    def FallbackBinaryOperation(self, target: System.Dynamic.DynamicMetaObject, arg: System.Dynamic.DynamicMetaObject, errorSuggestion: System.Dynamic.DynamicMetaObject, ) -> System.Dynamic.DynamicMetaObject:
        ...

    @typing.overload
    def FallbackBinaryOperation(self, target: System.Dynamic.DynamicMetaObject, arg: System.Dynamic.DynamicMetaObject, ) -> System.Dynamic.DynamicMetaObject:
        ...

    def Bind(self, target: System.Dynamic.DynamicMetaObject, args: System.Array[System.Dynamic.DynamicMetaObject], ) -> System.Dynamic.DynamicMetaObject:
        ...

    @staticmethod
    def OperationIsValid(operation: int, ) -> bool:
        ...

class CallInfo(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def ArgumentCount(self) -> int:
        ...

    @property
    def ArgumentNames(self) -> System.Collections.ObjectModel.ReadOnlyCollection[str]:
        ...

    # methods
    @typing.overload
    def __init__(self, argCount: int, argNames: System.Array[str], ):
        ...

    @typing.overload
    def __init__(self, argCount: int, argNames: System.Collections.Generic.IEnumerable[str], ):
        ...

    def GetHashCode(self, ) -> int:
        ...

    def Equals(self, obj: System.Object, ) -> bool:
        ...

class ConvertBinder(System.Dynamic.DynamicMetaObjectBinder, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        self.Cache: System.Collections.Generic.Dictionary[System.Type, System.Object]
        ...

    # static fields

    # properties
    @property
    def Type(self) -> System.Type:
        ...

    @property
    def Explicit(self) -> bool:
        ...

    @property
    def IsStandardBinder(self) -> bool:
        ...

    @property
    def ReturnType(self) -> System.Type:
        ...

    # methods
    def __init__(self, type: System.Type, explicit: bool, ):
        ...

    @typing.overload
    def FallbackConvert(self, target: System.Dynamic.DynamicMetaObject, ) -> System.Dynamic.DynamicMetaObject:
        ...

    @abc.abstractmethod
    @typing.overload
    def FallbackConvert(self, target: System.Dynamic.DynamicMetaObject, errorSuggestion: System.Dynamic.DynamicMetaObject, ) -> System.Dynamic.DynamicMetaObject:
        ...

    def Bind(self, target: System.Dynamic.DynamicMetaObject, args: System.Array[System.Dynamic.DynamicMetaObject], ) -> System.Dynamic.DynamicMetaObject:
        ...

class InvokeMemberBinder(System.Dynamic.DynamicMetaObjectBinder, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        self.Cache: System.Collections.Generic.Dictionary[System.Type, System.Object]
        ...

    # static fields

    # properties
    @property
    def ReturnType(self) -> System.Type:
        ...

    @property
    def Name(self) -> str:
        ...

    @property
    def IgnoreCase(self) -> bool:
        ...

    @property
    def CallInfo(self) -> System.Dynamic.CallInfo:
        ...

    @property
    def IsStandardBinder(self) -> bool:
        ...

    # methods
    def __init__(self, name: str, ignoreCase: bool, callInfo: System.Dynamic.CallInfo, ):
        ...

    def Bind(self, target: System.Dynamic.DynamicMetaObject, args: System.Array[System.Dynamic.DynamicMetaObject], ) -> System.Dynamic.DynamicMetaObject:
        ...

    @typing.overload
    def FallbackInvokeMember(self, target: System.Dynamic.DynamicMetaObject, args: System.Array[System.Dynamic.DynamicMetaObject], ) -> System.Dynamic.DynamicMetaObject:
        ...

    @abc.abstractmethod
    @typing.overload
    def FallbackInvokeMember(self, target: System.Dynamic.DynamicMetaObject, args: System.Array[System.Dynamic.DynamicMetaObject], errorSuggestion: System.Dynamic.DynamicMetaObject, ) -> System.Dynamic.DynamicMetaObject:
        ...

    @abc.abstractmethod
    def FallbackInvoke(self, target: System.Dynamic.DynamicMetaObject, args: System.Array[System.Dynamic.DynamicMetaObject], errorSuggestion: System.Dynamic.DynamicMetaObject, ) -> System.Dynamic.DynamicMetaObject:
        ...

class GetMemberBinder(System.Dynamic.DynamicMetaObjectBinder, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        self.Cache: System.Collections.Generic.Dictionary[System.Type, System.Object]
        ...

    # static fields

    # properties
    @property
    def ReturnType(self) -> System.Type:
        ...

    @property
    def Name(self) -> str:
        ...

    @property
    def IgnoreCase(self) -> bool:
        ...

    @property
    def IsStandardBinder(self) -> bool:
        ...

    # methods
    def __init__(self, name: str, ignoreCase: bool, ):
        ...

    @typing.overload
    def FallbackGetMember(self, target: System.Dynamic.DynamicMetaObject, ) -> System.Dynamic.DynamicMetaObject:
        ...

    @abc.abstractmethod
    @typing.overload
    def FallbackGetMember(self, target: System.Dynamic.DynamicMetaObject, errorSuggestion: System.Dynamic.DynamicMetaObject, ) -> System.Dynamic.DynamicMetaObject:
        ...

    def Bind(self, target: System.Dynamic.DynamicMetaObject, args: System.Array[System.Dynamic.DynamicMetaObject], ) -> System.Dynamic.DynamicMetaObject:
        ...

class DynamicMetaObject(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields
    EmptyMetaObjects: System.Array[System.Dynamic.DynamicMetaObject] = ...

    # properties
    @property
    def Expression(self) -> System.Linq.Expressions.Expression:
        ...

    @property
    def Restrictions(self) -> System.Dynamic.BindingRestrictions:
        ...

    @property
    def Value(self) -> System.Object:
        ...

    @property
    def HasValue(self) -> bool:
        ...

    @property
    def RuntimeType(self) -> System.Type:
        ...

    @property
    def LimitType(self) -> System.Type:
        ...

    # methods
    @typing.overload
    def __init__(self, expression: System.Linq.Expressions.Expression, restrictions: System.Dynamic.BindingRestrictions, ):
        ...

    @typing.overload
    def __init__(self, expression: System.Linq.Expressions.Expression, restrictions: System.Dynamic.BindingRestrictions, value: System.Object, ):
        ...

    def BindConvert(self, binder: System.Dynamic.ConvertBinder, ) -> System.Dynamic.DynamicMetaObject:
        ...

    def BindGetMember(self, binder: System.Dynamic.GetMemberBinder, ) -> System.Dynamic.DynamicMetaObject:
        ...

    def BindSetMember(self, binder: System.Dynamic.SetMemberBinder, value: System.Dynamic.DynamicMetaObject, ) -> System.Dynamic.DynamicMetaObject:
        ...

    def BindDeleteMember(self, binder: System.Dynamic.DeleteMemberBinder, ) -> System.Dynamic.DynamicMetaObject:
        ...

    def BindGetIndex(self, binder: System.Dynamic.GetIndexBinder, indexes: System.Array[System.Dynamic.DynamicMetaObject], ) -> System.Dynamic.DynamicMetaObject:
        ...

    def BindSetIndex(self, binder: System.Dynamic.SetIndexBinder, indexes: System.Array[System.Dynamic.DynamicMetaObject], value: System.Dynamic.DynamicMetaObject, ) -> System.Dynamic.DynamicMetaObject:
        ...

    def BindDeleteIndex(self, binder: System.Dynamic.DeleteIndexBinder, indexes: System.Array[System.Dynamic.DynamicMetaObject], ) -> System.Dynamic.DynamicMetaObject:
        ...

    def BindInvokeMember(self, binder: System.Dynamic.InvokeMemberBinder, args: System.Array[System.Dynamic.DynamicMetaObject], ) -> System.Dynamic.DynamicMetaObject:
        ...

    def BindInvoke(self, binder: System.Dynamic.InvokeBinder, args: System.Array[System.Dynamic.DynamicMetaObject], ) -> System.Dynamic.DynamicMetaObject:
        ...

    def BindCreateInstance(self, binder: System.Dynamic.CreateInstanceBinder, args: System.Array[System.Dynamic.DynamicMetaObject], ) -> System.Dynamic.DynamicMetaObject:
        ...

    def BindUnaryOperation(self, binder: System.Dynamic.UnaryOperationBinder, ) -> System.Dynamic.DynamicMetaObject:
        ...

    def BindBinaryOperation(self, binder: System.Dynamic.BinaryOperationBinder, arg: System.Dynamic.DynamicMetaObject, ) -> System.Dynamic.DynamicMetaObject:
        ...

    def GetDynamicMemberNames(self, ) -> System.Collections.Generic.IEnumerable[str]:
        ...

    @staticmethod
    def GetExpressions(objects: System.Array[System.Dynamic.DynamicMetaObject], ) -> System.Array[System.Linq.Expressions.Expression]:
        ...

    @staticmethod
    def Create(value: System.Object, expression: System.Linq.Expressions.Expression, ) -> System.Dynamic.DynamicMetaObject:
        ...

class SetIndexBinder(System.Dynamic.DynamicMetaObjectBinder, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        self.Cache: System.Collections.Generic.Dictionary[System.Type, System.Object]
        ...

    # static fields

    # properties
    @property
    def ReturnType(self) -> System.Type:
        ...

    @property
    def CallInfo(self) -> System.Dynamic.CallInfo:
        ...

    @property
    def IsStandardBinder(self) -> bool:
        ...

    # methods
    def __init__(self, callInfo: System.Dynamic.CallInfo, ):
        ...

    def Bind(self, target: System.Dynamic.DynamicMetaObject, args: System.Array[System.Dynamic.DynamicMetaObject], ) -> System.Dynamic.DynamicMetaObject:
        ...

    @typing.overload
    def FallbackSetIndex(self, target: System.Dynamic.DynamicMetaObject, indexes: System.Array[System.Dynamic.DynamicMetaObject], value: System.Dynamic.DynamicMetaObject, ) -> System.Dynamic.DynamicMetaObject:
        ...

    @abc.abstractmethod
    @typing.overload
    def FallbackSetIndex(self, target: System.Dynamic.DynamicMetaObject, indexes: System.Array[System.Dynamic.DynamicMetaObject], value: System.Dynamic.DynamicMetaObject, errorSuggestion: System.Dynamic.DynamicMetaObject, ) -> System.Dynamic.DynamicMetaObject:
        ...

class GetIndexBinder(System.Dynamic.DynamicMetaObjectBinder, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        self.Cache: System.Collections.Generic.Dictionary[System.Type, System.Object]
        ...

    # static fields

    # properties
    @property
    def ReturnType(self) -> System.Type:
        ...

    @property
    def CallInfo(self) -> System.Dynamic.CallInfo:
        ...

    @property
    def IsStandardBinder(self) -> bool:
        ...

    # methods
    def __init__(self, callInfo: System.Dynamic.CallInfo, ):
        ...

    def Bind(self, target: System.Dynamic.DynamicMetaObject, args: System.Array[System.Dynamic.DynamicMetaObject], ) -> System.Dynamic.DynamicMetaObject:
        ...

    @typing.overload
    def FallbackGetIndex(self, target: System.Dynamic.DynamicMetaObject, indexes: System.Array[System.Dynamic.DynamicMetaObject], ) -> System.Dynamic.DynamicMetaObject:
        ...

    @abc.abstractmethod
    @typing.overload
    def FallbackGetIndex(self, target: System.Dynamic.DynamicMetaObject, indexes: System.Array[System.Dynamic.DynamicMetaObject], errorSuggestion: System.Dynamic.DynamicMetaObject, ) -> System.Dynamic.DynamicMetaObject:
        ...

class SetMemberBinder(System.Dynamic.DynamicMetaObjectBinder, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        self.Cache: System.Collections.Generic.Dictionary[System.Type, System.Object]
        ...

    # static fields

    # properties
    @property
    def ReturnType(self) -> System.Type:
        ...

    @property
    def Name(self) -> str:
        ...

    @property
    def IgnoreCase(self) -> bool:
        ...

    @property
    def IsStandardBinder(self) -> bool:
        ...

    # methods
    def __init__(self, name: str, ignoreCase: bool, ):
        ...

    def Bind(self, target: System.Dynamic.DynamicMetaObject, args: System.Array[System.Dynamic.DynamicMetaObject], ) -> System.Dynamic.DynamicMetaObject:
        ...

    @typing.overload
    def FallbackSetMember(self, target: System.Dynamic.DynamicMetaObject, value: System.Dynamic.DynamicMetaObject, ) -> System.Dynamic.DynamicMetaObject:
        ...

    @abc.abstractmethod
    @typing.overload
    def FallbackSetMember(self, target: System.Dynamic.DynamicMetaObject, value: System.Dynamic.DynamicMetaObject, errorSuggestion: System.Dynamic.DynamicMetaObject, ) -> System.Dynamic.DynamicMetaObject:
        ...

class DeleteIndexBinder(System.Dynamic.DynamicMetaObjectBinder, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        self.Cache: System.Collections.Generic.Dictionary[System.Type, System.Object]
        ...

    # static fields

    # properties
    @property
    def ReturnType(self) -> System.Type:
        ...

    @property
    def CallInfo(self) -> System.Dynamic.CallInfo:
        ...

    @property
    def IsStandardBinder(self) -> bool:
        ...

    # methods
    def __init__(self, callInfo: System.Dynamic.CallInfo, ):
        ...

    def Bind(self, target: System.Dynamic.DynamicMetaObject, args: System.Array[System.Dynamic.DynamicMetaObject], ) -> System.Dynamic.DynamicMetaObject:
        ...

    @typing.overload
    def FallbackDeleteIndex(self, target: System.Dynamic.DynamicMetaObject, indexes: System.Array[System.Dynamic.DynamicMetaObject], ) -> System.Dynamic.DynamicMetaObject:
        ...

    @abc.abstractmethod
    @typing.overload
    def FallbackDeleteIndex(self, target: System.Dynamic.DynamicMetaObject, indexes: System.Array[System.Dynamic.DynamicMetaObject], errorSuggestion: System.Dynamic.DynamicMetaObject, ) -> System.Dynamic.DynamicMetaObject:
        ...

class IDynamicMetaObjectProvider(abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    @abc.abstractmethod
    def GetMetaObject(self, parameter: System.Linq.Expressions.Expression, ) -> System.Dynamic.DynamicMetaObject:
        ...

class InvokeBinder(System.Dynamic.DynamicMetaObjectBinder, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        self.Cache: System.Collections.Generic.Dictionary[System.Type, System.Object]
        ...

    # static fields

    # properties
    @property
    def ReturnType(self) -> System.Type:
        ...

    @property
    def CallInfo(self) -> System.Dynamic.CallInfo:
        ...

    @property
    def IsStandardBinder(self) -> bool:
        ...

    # methods
    def __init__(self, callInfo: System.Dynamic.CallInfo, ):
        ...

    @typing.overload
    def FallbackInvoke(self, target: System.Dynamic.DynamicMetaObject, args: System.Array[System.Dynamic.DynamicMetaObject], ) -> System.Dynamic.DynamicMetaObject:
        ...

    @abc.abstractmethod
    @typing.overload
    def FallbackInvoke(self, target: System.Dynamic.DynamicMetaObject, args: System.Array[System.Dynamic.DynamicMetaObject], errorSuggestion: System.Dynamic.DynamicMetaObject, ) -> System.Dynamic.DynamicMetaObject:
        ...

    def Bind(self, target: System.Dynamic.DynamicMetaObject, args: System.Array[System.Dynamic.DynamicMetaObject], ) -> System.Dynamic.DynamicMetaObject:
        ...

class DeleteMemberBinder(System.Dynamic.DynamicMetaObjectBinder, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        self.Cache: System.Collections.Generic.Dictionary[System.Type, System.Object]
        ...

    # static fields

    # properties
    @property
    def Name(self) -> str:
        ...

    @property
    def IgnoreCase(self) -> bool:
        ...

    @property
    def ReturnType(self) -> System.Type:
        ...

    @property
    def IsStandardBinder(self) -> bool:
        ...

    # methods
    def __init__(self, name: str, ignoreCase: bool, ):
        ...

    @typing.overload
    def FallbackDeleteMember(self, target: System.Dynamic.DynamicMetaObject, ) -> System.Dynamic.DynamicMetaObject:
        ...

    @abc.abstractmethod
    @typing.overload
    def FallbackDeleteMember(self, target: System.Dynamic.DynamicMetaObject, errorSuggestion: System.Dynamic.DynamicMetaObject, ) -> System.Dynamic.DynamicMetaObject:
        ...

    def Bind(self, target: System.Dynamic.DynamicMetaObject, args: System.Array[System.Dynamic.DynamicMetaObject], ) -> System.Dynamic.DynamicMetaObject:
        ...

class BindingRestrictions(System.Object, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields
    Empty: System.Dynamic.BindingRestrictions = ...

    # properties
    @property
    def DebugView(self) -> str:
        ...

    # methods
    def __init__(self, ):
        ...

    @abc.abstractmethod
    def GetExpression(self, ) -> System.Linq.Expressions.Expression:
        ...

    def Merge(self, restrictions: System.Dynamic.BindingRestrictions, ) -> System.Dynamic.BindingRestrictions:
        ...

    @staticmethod
    @typing.overload
    def GetTypeRestriction(expression: System.Linq.Expressions.Expression, type: System.Type, ) -> System.Dynamic.BindingRestrictions:
        ...

    @staticmethod
    @typing.overload
    def GetTypeRestriction(obj: System.Dynamic.DynamicMetaObject, ) -> System.Dynamic.BindingRestrictions:
        ...

    @staticmethod
    def GetInstanceRestriction(expression: System.Linq.Expressions.Expression, instance: System.Object, ) -> System.Dynamic.BindingRestrictions:
        ...

    @staticmethod
    def GetExpressionRestriction(expression: System.Linq.Expressions.Expression, ) -> System.Dynamic.BindingRestrictions:
        ...

    @staticmethod
    def Combine(contributingObjects: System.Collections.Generic.IList[System.Dynamic.DynamicMetaObject], ) -> System.Dynamic.BindingRestrictions:
        ...

    def ToExpression(self, ) -> System.Linq.Expressions.Expression:
        ...

class CreateInstanceBinder(System.Dynamic.DynamicMetaObjectBinder, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        self.Cache: System.Collections.Generic.Dictionary[System.Type, System.Object]
        ...

    # static fields

    # properties
    @property
    def ReturnType(self) -> System.Type:
        ...

    @property
    def CallInfo(self) -> System.Dynamic.CallInfo:
        ...

    @property
    def IsStandardBinder(self) -> bool:
        ...

    # methods
    def __init__(self, callInfo: System.Dynamic.CallInfo, ):
        ...

    @typing.overload
    def FallbackCreateInstance(self, target: System.Dynamic.DynamicMetaObject, args: System.Array[System.Dynamic.DynamicMetaObject], ) -> System.Dynamic.DynamicMetaObject:
        ...

    @abc.abstractmethod
    @typing.overload
    def FallbackCreateInstance(self, target: System.Dynamic.DynamicMetaObject, args: System.Array[System.Dynamic.DynamicMetaObject], errorSuggestion: System.Dynamic.DynamicMetaObject, ) -> System.Dynamic.DynamicMetaObject:
        ...

    def Bind(self, target: System.Dynamic.DynamicMetaObject, args: System.Array[System.Dynamic.DynamicMetaObject], ) -> System.Dynamic.DynamicMetaObject:
        ...

