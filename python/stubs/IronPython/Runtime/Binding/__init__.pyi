from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import Microsoft.Scripting.Actions.Calls
import System.Reflection
import System
import System.Linq.Expressions
import System.Collections.Generic
import IronPython.Runtime
import System.Dynamic
import IronPython.Runtime.Binding

T = typing.TypeVar('T')

class SiteLocalStorageBuilder(Microsoft.Scripting.Actions.Calls.ArgBuilder):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def Priority(self) -> int:
        ...

    @property
    def ConsumedArgumentCount(self) -> int:
        ...

    @property
    def ParameterInfo(self) -> System.Reflection.ParameterInfo:
        ...

    @property
    def Type(self) -> System.Type:
        ...

    @property
    def ByRefArgument(self) -> System.Linq.Expressions.Expression:
        ...

    # methods
    def __init__(self, info: System.Reflection.ParameterInfo, ):
        ...

    def ToExpression(self, resolver: Microsoft.Scripting.Actions.Calls.OverloadResolver, args: Microsoft.Scripting.Actions.Calls.RestrictedArguments, hasBeenUsed: System.Array[bool], ) -> System.Linq.Expressions.Expression:
        ...

class IPythonExpandable(abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    @abc.abstractmethod
    def CustomAttributes(self) -> System.Collections.Generic.IDictionary[System.Object, System.Object]:
        ...

    @property
    @abc.abstractmethod
    def Context(self) -> IronPython.Runtime.CodeContext:
        ...

    # methods
    @abc.abstractmethod
    def EnsureCustomAttributes(self, ) -> System.Collections.Generic.IDictionary[System.Object, System.Object]:
        ...

class MetaExpandable(System.Dynamic.DynamicMetaObject, typing.Generic[T]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def Value(self) -> T:
        ...

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
    def __init__(self, parameter: System.Linq.Expressions.Expression, value: IronPython.Runtime.Binding.IPythonExpandable, ):
        ...

    def BindGetMember(self, binder: System.Dynamic.GetMemberBinder, ) -> System.Dynamic.DynamicMetaObject:
        ...

    def BindInvokeMember(self, binder: System.Dynamic.InvokeMemberBinder, args: System.Array[System.Dynamic.DynamicMetaObject], ) -> System.Dynamic.DynamicMetaObject:
        ...

    def DynamicTryGetMember(self, name: str, fallback: System.Linq.Expressions.Expression, transform: System.Func[System.Linq.Expressions.Expression, System.Linq.Expressions.Expression], ) -> System.Dynamic.DynamicMetaObject:
        ...

    def BindSetMember(self, binder: System.Dynamic.SetMemberBinder, value: System.Dynamic.DynamicMetaObject, ) -> System.Dynamic.DynamicMetaObject:
        ...

    def BindDeleteMember(self, binder: System.Dynamic.DeleteMemberBinder, ) -> System.Dynamic.DynamicMetaObject:
        ...

    def GetDynamicMemberNames(self, ) -> System.Collections.Generic.IEnumerable[str]:
        ...

    def GetRestrictions(self, ) -> System.Dynamic.BindingRestrictions:
        ...

    @staticmethod
    def Convert(expression: System.Linq.Expressions.Expression, type: System.Type, ) -> System.Linq.Expressions.Expression:
        ...

    @staticmethod
    def TryGetMember(target: T, name: str, ) -> System.Object:
        ...

    @staticmethod
    def TrySetMember(target: T, name: str, value: System.Object, ) -> bool:
        ...

    @staticmethod
    def TryDeleteMember(target: T, name: str, ) -> bool:
        ...

class ContextArgBuilder(Microsoft.Scripting.Actions.Calls.ArgBuilder):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def Priority(self) -> int:
        ...

    @property
    def ConsumedArgumentCount(self) -> int:
        ...

    @property
    def ParameterInfo(self) -> System.Reflection.ParameterInfo:
        ...

    @property
    def Type(self) -> System.Type:
        ...

    @property
    def ByRefArgument(self) -> System.Linq.Expressions.Expression:
        ...

    # methods
    def __init__(self, info: System.Reflection.ParameterInfo, ):
        ...

    def ToExpression(self, resolver: Microsoft.Scripting.Actions.Calls.OverloadResolver, args: Microsoft.Scripting.Actions.Calls.RestrictedArguments, hasBeenUsed: System.Array[bool], ) -> System.Linq.Expressions.Expression:
        ...

