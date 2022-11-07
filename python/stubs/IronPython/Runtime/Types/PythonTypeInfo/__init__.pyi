from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import System
import IronPython.Runtime.Types.PythonTypeInfo
import Microsoft.Scripting.Actions
import System.Collections.Generic
import IronPython.Runtime.Types
import IronPython.Runtime.Binding
import Microsoft.Scripting.Runtime
import System.Reflection
import IronPython.Runtime


class MemberResolver(System.Object, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    def __init__(self, ):
        ...

    @abc.abstractmethod
    def ResolveMember(self, binder: IronPython.Runtime.Types.PythonTypeInfo.MemberBinder, action: int, type: System.Type, name: str, ) -> Microsoft.Scripting.Actions.MemberGroup:
        ...

    def ResolveMembers(self, binder: IronPython.Runtime.Types.PythonTypeInfo.MemberBinder, action: int, type: System.Type, ) -> System.Collections.Generic.IList[IronPython.Runtime.Types.ResolvedMember]:
        ...

    @abc.abstractmethod
    def GetCandidateNames(self, binder: IronPython.Runtime.Types.PythonTypeInfo.MemberBinder, action: int, type: System.Type, ) -> System.Collections.Generic.IEnumerable[str]:
        ...

class OneOffOperatorBinder(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    def __init__(self, methodName: str, pythonName: str, opMap: int, ):
        ...

    def Resolver(self, binder: IronPython.Runtime.Types.PythonTypeInfo.MemberBinder, type: System.Type, ) -> Microsoft.Scripting.Actions.MemberGroup:
        ...

class OneOffResolver(IronPython.Runtime.Types.PythonTypeInfo.MemberResolver):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    def __init__(self, name: str, resolver: System.Func[IronPython.Runtime.Types.PythonTypeInfo.MemberBinder, System.Type, Microsoft.Scripting.Actions.MemberGroup], ):
        ...

    def ResolveMember(self, binder: IronPython.Runtime.Types.PythonTypeInfo.MemberBinder, action: int, type: System.Type, name: str, ) -> Microsoft.Scripting.Actions.MemberGroup:
        ...

    def GetCandidateNames(self, binder: IronPython.Runtime.Types.PythonTypeInfo.MemberBinder, action: int, type: System.Type, ) -> System.Collections.Generic.IEnumerable[str]:
        ...

class LookupBinder(IronPython.Runtime.Types.PythonTypeInfo.MemberBinder):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def Binder(self) -> IronPython.Runtime.Binding.PythonBinder:
        ...

    @property
    def DomainManager(self) -> Microsoft.Scripting.Runtime.ScriptDomainManager:
        ...

    # methods
    def __init__(self, binder: IronPython.Runtime.Binding.PythonBinder, ):
        ...

    def GetInterfaces(self, t: System.Type, ) -> System.Collections.Generic.IList[System.Type]:
        ...

    def GetBaseInstanceMethod(self, type: System.Type, name: System.Array[str], ) -> Microsoft.Scripting.Actions.MemberGroup:
        ...

    def GetContributingTypes(self, t: System.Type, ) -> System.Collections.Generic.IList[System.Type]:
        ...

    def GetMember(self, type: System.Type, name: str, ) -> Microsoft.Scripting.Actions.MemberGroup:
        ...

class ObjectResolver(IronPython.Runtime.Types.PythonTypeInfo.StandardResolver):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    def __init__(self, ):
        ...

    def ResolveMember(self, binder: IronPython.Runtime.Types.PythonTypeInfo.MemberBinder, action: int, type: System.Type, name: str, ) -> Microsoft.Scripting.Actions.MemberGroup:
        ...

class StandardResolver(IronPython.Runtime.Types.PythonTypeInfo.MemberResolver):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    def __init__(self, ):
        ...

    def ResolveMember(self, binder: IronPython.Runtime.Types.PythonTypeInfo.MemberBinder, action: int, type: System.Type, name: str, ) -> Microsoft.Scripting.Actions.MemberGroup:
        ...

    def GetCandidateNames(self, binder: IronPython.Runtime.Types.PythonTypeInfo.MemberBinder, action: int, type: System.Type, ) -> System.Collections.Generic.IEnumerable[str]:
        ...

class _IPythonObject(System.Object, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields
    PythonType: System.Reflection.PropertyInfo = ...
    Dict: System.Reflection.PropertyInfo = ...

    # properties
    # methods
class _Object(System.Object, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields
    GetType: System.Reflection.MethodInfo = ...

    # properties
    # methods
class OneOffPowerBinder(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    def __init__(self, pythonName: str, op: int, ):
        ...

    def Resolver(self, binder: IronPython.Runtime.Types.PythonTypeInfo.MemberBinder, type: System.Type, ) -> Microsoft.Scripting.Actions.MemberGroup:
        ...

class _OperationFailed(System.Object, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields
    Value: System.Reflection.FieldInfo = ...

    # properties
    # methods
class EqualityResolver(IronPython.Runtime.Types.PythonTypeInfo.MemberResolver):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields
    Instance: IronPython.Runtime.Types.PythonTypeInfo.EqualityResolver = ...

    # properties
    # methods
    def __init__(self, ):
        ...

    def ResolveMember(self, binder: IronPython.Runtime.Types.PythonTypeInfo.MemberBinder, action: int, type: System.Type, name: str, ) -> Microsoft.Scripting.Actions.MemberGroup:
        ...

    def GetCandidateNames(self, binder: IronPython.Runtime.Types.PythonTypeInfo.MemberBinder, action: int, type: System.Type, ) -> System.Collections.Generic.IEnumerable[str]:
        ...

class ResolveBinder(IronPython.Runtime.Types.PythonTypeInfo.MemberBinder):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def Binder(self) -> IronPython.Runtime.Binding.PythonBinder:
        ...

    @property
    def DomainManager(self) -> Microsoft.Scripting.Runtime.ScriptDomainManager:
        ...

    # methods
    def __init__(self, binder: IronPython.Runtime.Binding.PythonBinder, ):
        ...

    def GetInterfaces(self, t: System.Type, ) -> System.Collections.Generic.IList[System.Type]:
        ...

    def GetBaseInstanceMethod(self, type: System.Type, name: System.Array[str], ) -> Microsoft.Scripting.Actions.MemberGroup:
        ...

    def GetContributingTypes(self, t: System.Type, ) -> System.Collections.Generic.IList[System.Type]:
        ...

    def GetMember(self, type: System.Type, name: str, ) -> Microsoft.Scripting.Actions.MemberGroup:
        ...

class _PythonOps(System.Object, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields
    SlotTryGetBoundValue: System.Reflection.MethodInfo = ...
    GetTypeVersion: System.Reflection.MethodInfo = ...
    CheckTypeVersion: System.Reflection.MethodInfo = ...

    # properties
    # methods
class _PythonGenerator(System.Object, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields
    Ctor: System.Reflection.ConstructorInfo = ...

    # properties
    # methods
class MemberBinder(System.Object, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def Binder(self) -> IronPython.Runtime.Binding.PythonBinder:
        ...

    @property
    def DomainManager(self) -> Microsoft.Scripting.Runtime.ScriptDomainManager:
        ...

    # methods
    def __init__(self, binder: IronPython.Runtime.Binding.PythonBinder, ):
        ...

    @abc.abstractmethod
    def GetContributingTypes(self, t: System.Type, ) -> System.Collections.Generic.IList[System.Type]:
        ...

    @abc.abstractmethod
    def GetInterfaces(self, t: System.Type, ) -> System.Collections.Generic.IList[System.Type]:
        ...

    @abc.abstractmethod
    def GetBaseInstanceMethod(self, type: System.Type, name: System.Array[str], ) -> Microsoft.Scripting.Actions.MemberGroup:
        ...

    @abc.abstractmethod
    @typing.overload
    def GetMember(self, type: System.Type, name: str, ) -> Microsoft.Scripting.Actions.MemberGroup:
        ...

    @typing.overload
    def GetMember(self, type: System.Type, name: str, flags: int, ) -> Microsoft.Scripting.Actions.MemberGroup:
        ...

class ComparisonResolver(IronPython.Runtime.Types.PythonTypeInfo.MemberResolver):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    def __init__(self, comparable: System.Type, helperPrefix: str, ):
        ...

    def ResolveMember(self, binder: IronPython.Runtime.Types.PythonTypeInfo.MemberBinder, action: int, type: System.Type, name: str, ) -> Microsoft.Scripting.Actions.MemberGroup:
        ...

    def GetCandidateNames(self, binder: IronPython.Runtime.Types.PythonTypeInfo.MemberBinder, action: int, type: System.Type, ) -> System.Collections.Generic.IEnumerable[str]:
        ...

class PrivateBindingResolver(IronPython.Runtime.Types.PythonTypeInfo.MemberResolver):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    def __init__(self, ):
        ...

    def ResolveMember(self, binder: IronPython.Runtime.Types.PythonTypeInfo.MemberBinder, action: int, type: System.Type, name: str, ) -> Microsoft.Scripting.Actions.MemberGroup:
        ...

    def GetCandidateNames(self, binder: IronPython.Runtime.Types.PythonTypeInfo.MemberBinder, action: int, type: System.Type, ) -> System.Collections.Generic.IEnumerable[str]:
        ...

class DocumentationDescriptor(IronPython.Runtime.Types.PythonTypeSlot):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def GetAlwaysSucceeds(self) -> bool:
        ...

    @property
    def IsAlwaysVisible(self) -> bool:
        ...

    @property
    def CanOptimizeGets(self) -> bool:
        ...

    # methods
    def __init__(self, ):
        ...

    def TryGetValue(self, context: IronPython.Runtime.CodeContext, instance: System.Object, owner: IronPython.Runtime.Types.PythonType, value: ref[System.Object], ) -> bool:
        ...

    def TrySetValue(self, context: IronPython.Runtime.CodeContext, instance: System.Object, owner: IronPython.Runtime.Types.PythonType, value: System.Object, ) -> bool:
        ...

class ProtectedMemberResolver(IronPython.Runtime.Types.PythonTypeInfo.MemberResolver):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    def __init__(self, ):
        ...

    def ResolveMember(self, binder: IronPython.Runtime.Types.PythonTypeInfo.MemberBinder, action: int, type: System.Type, name: str, ) -> Microsoft.Scripting.Actions.MemberGroup:
        ...

    def GetCandidateNames(self, binder: IronPython.Runtime.Types.PythonTypeInfo.MemberBinder, action: int, type: System.Type, ) -> System.Collections.Generic.IEnumerable[str]:
        ...

class _PythonDictionary(System.Object, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields
    TryGetvalue: System.Reflection.MethodInfo = ...

    # properties
    # methods
class OperatorResolver(IronPython.Runtime.Types.PythonTypeInfo.MemberResolver):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    def __init__(self, ):
        ...

    def ResolveMember(self, binder: IronPython.Runtime.Types.PythonTypeInfo.MemberBinder, action: int, type: System.Type, name: str, ) -> Microsoft.Scripting.Actions.MemberGroup:
        ...

    @staticmethod
    def FilterAlternateMethods(opInfo: IronPython.Runtime.Types.OperatorMapping, res: Microsoft.Scripting.Actions.MemberGroup, ) -> Microsoft.Scripting.Actions.MemberGroup:
        ...

    @staticmethod
    def FilterObjectEquality(group: Microsoft.Scripting.Actions.MemberGroup, ) -> Microsoft.Scripting.Actions.MemberGroup:
        ...

    def GetCandidateNames(self, binder: IronPython.Runtime.Types.PythonTypeInfo.MemberBinder, action: int, type: System.Type, ) -> System.Collections.Generic.IEnumerable[str]:
        ...

