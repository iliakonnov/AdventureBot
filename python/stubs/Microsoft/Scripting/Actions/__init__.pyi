from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import System
import Microsoft.Scripting.Actions
import System.Linq.Expressions
import System.Collections.Generic
import System.Collections
import System.Reflection
import Microsoft.Scripting.Actions.Calls
import System.Dynamic
import Microsoft.Scripting.Runtime
import Microsoft.Scripting.Actions.EventTracker
import Microsoft.Scripting.Actions.NamespaceTracker
import System.Runtime.CompilerServices
import Microsoft.Scripting.Actions.DefaultBinder


class CallSignature(System.IEquatable[Microsoft.Scripting.Actions.CallSignature], System.ValueType):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def IsSimple(self) -> bool:
        ...

    @property
    def ArgumentCount(self) -> int:
        ...

    # methods
    @typing.overload
    def __init__(self, signature: Microsoft.Scripting.Actions.CallSignature, ):
        ...

    @typing.overload
    def __init__(self, argumentCount: int, ):
        ...

    @typing.overload
    def __init__(self, infos: System.Array[Microsoft.Scripting.Actions.Argument], ):
        ...

    @typing.overload
    def __init__(self, kinds: System.Array[int], ):
        ...

    @typing.overload
    def Equals(self, other: Microsoft.Scripting.Actions.CallSignature, ) -> bool:
        ...

    @typing.overload
    def Equals(self, obj: System.Object, ) -> bool:
        ...

    def ToString(self, ) -> str:
        ...

    def GetHashCode(self, ) -> int:
        ...

    def GetArgumentInfos(self, ) -> System.Array[Microsoft.Scripting.Actions.Argument]:
        ...

    def InsertArgument(self, info: Microsoft.Scripting.Actions.Argument, ) -> Microsoft.Scripting.Actions.CallSignature:
        ...

    def InsertArgumentAt(self, index: int, info: Microsoft.Scripting.Actions.Argument, ) -> Microsoft.Scripting.Actions.CallSignature:
        ...

    def RemoveFirstArgument(self, ) -> Microsoft.Scripting.Actions.CallSignature:
        ...

    def RemoveArgumentAt(self, index: int, ) -> Microsoft.Scripting.Actions.CallSignature:
        ...

    def IndexOf(self, kind: int, ) -> int:
        ...

    def HasDictionaryArgument(self, ) -> bool:
        ...

    def HasInstanceArgument(self, ) -> bool:
        ...

    def HasListArgument(self, ) -> bool:
        ...

    def HasNamedArgument(self, ) -> bool:
        ...

    def HasKeywordArgument(self, ) -> bool:
        ...

    def GetArgumentKind(self, index: int, ) -> int:
        ...

    def GetArgumentName(self, index: int, ) -> str:
        ...

    def GetProvidedPositionalArgumentCount(self, ) -> int:
        ...

    def GetArgumentNames(self, ) -> System.Array[str]:
        ...

    def CreateExpression(self, ) -> System.Linq.Expressions.Expression:
        ...

class MemberGroup(System.Collections.Generic.IEnumerable[Microsoft.Scripting.Actions.MemberTracker], System.Collections.IEnumerable, System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields
    EmptyGroup: Microsoft.Scripting.Actions.MemberGroup = ...

    # properties
    @property
    def Count(self) -> int:
        ...

    @property
    def Item(self) -> Microsoft.Scripting.Actions.MemberTracker:
        ...

    # methods
    @typing.overload
    def __init__(self, members: System.Array[Microsoft.Scripting.Actions.MemberTracker], noChecks: bool, ):
        ...

    @typing.overload
    def __init__(self, members: System.Array[Microsoft.Scripting.Actions.MemberTracker], ):
        ...

    @typing.overload
    def __init__(self, members: System.Array[System.Reflection.MemberInfo], ):
        ...

    @staticmethod
    def CreateInternal(members: System.Array[Microsoft.Scripting.Actions.MemberTracker], ) -> Microsoft.Scripting.Actions.MemberGroup:
        ...

    def GetEnumerator(self, ) -> System.Collections.Generic.IEnumerator[Microsoft.Scripting.Actions.MemberTracker]:
        ...

    def GetEnumerator(self, ) -> System.Collections.IEnumerator:
        ...

class MemberRequestKind(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    None_: int = ...
    Get: int = ...
    Set: int = ...
    Delete: int = ...
    Invoke: int = ...
    InvokeMember: int = ...
    Convert: int = ...
    Operation: int = ...

class EventTracker(Microsoft.Scripting.Actions.MemberTracker):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def DeclaringType(self) -> System.Type:
        ...

    @property
    def MemberType(self) -> int:
        ...

    @property
    def Name(self) -> str:
        ...

    @property
    def Event(self) -> System.Reflection.EventInfo:
        ...

    @property
    def IsStatic(self) -> bool:
        ...

    # methods
    def __init__(self, eventInfo: System.Reflection.EventInfo, ):
        ...

    def GetCallableAddMethod(self, ) -> System.Reflection.MethodInfo:
        ...

    def GetCallableRemoveMethod(self, ) -> System.Reflection.MethodInfo:
        ...

    def GetBoundValue(self, resolverFactory: Microsoft.Scripting.Actions.Calls.OverloadResolverFactory, binder: Microsoft.Scripting.Actions.ActionBinder, type: System.Type, instance: System.Dynamic.DynamicMetaObject, ) -> System.Dynamic.DynamicMetaObject:
        ...

    def BindToInstance(self, instance: System.Dynamic.DynamicMetaObject, ) -> Microsoft.Scripting.Actions.MemberTracker:
        ...

    def ToString(self, ) -> str:
        ...

    def AddHandler(self, target: System.Object, handler: System.Object, delegateCreator: Microsoft.Scripting.Runtime.DynamicDelegateCreator, ) -> None:
        ...

    def RemoveHandler(self, target: System.Object, handler: System.Object, objectComparer: System.Collections.Generic.IEqualityComparer[System.Object], ) -> None:
        ...

    def GetHandlerList(self, instance: System.Object, ) -> Microsoft.Scripting.Actions.EventTracker.HandlerList:
        ...

    def GetComHandlerList(self, instance: System.Object, ) -> Microsoft.Scripting.Actions.EventTracker.HandlerList:
        ...

class ActionBinder(System.Object, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def PrivateBinding(self) -> bool:
        ...

    @property
    def Manager(self) -> Microsoft.Scripting.Runtime.ScriptDomainManager:
        ...

    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def __init__(self, manager: Microsoft.Scripting.Runtime.ScriptDomainManager, ):
        ...

    def Convert(self, obj: System.Object, toType: System.Type, ) -> System.Object:
        ...

    @abc.abstractmethod
    def CanConvertFrom(self, fromType: System.Type, toType: System.Type, toNotNullable: bool, level: int, ) -> bool:
        ...

    @abc.abstractmethod
    def PreferConvert(self, t1: System.Type, t2: System.Type, ) -> int:
        ...

    def ConvertExpression(self, expr: System.Linq.Expressions.Expression, toType: System.Type, kind: int, resolverFactory: Microsoft.Scripting.Actions.Calls.OverloadResolverFactory, ) -> System.Linq.Expressions.Expression:
        ...

    def GetMember(self, action: int, type: System.Type, name: str, ) -> Microsoft.Scripting.Actions.MemberGroup:
        ...

    def MakeContainsGenericParametersError(self, tracker: Microsoft.Scripting.Actions.MemberTracker, ) -> Microsoft.Scripting.Actions.ErrorInfo:
        ...

    def MakeMissingMemberErrorInfo(self, type: System.Type, name: str, ) -> Microsoft.Scripting.Actions.ErrorInfo:
        ...

    def MakeGenericAccessError(self, info: Microsoft.Scripting.Actions.MemberTracker, ) -> Microsoft.Scripting.Actions.ErrorInfo:
        ...

    @typing.overload
    def MakeStaticPropertyInstanceAccessError(self, tracker: Microsoft.Scripting.Actions.PropertyTracker, isAssignment: bool, parameters: System.Array[System.Dynamic.DynamicMetaObject], ) -> Microsoft.Scripting.Actions.ErrorInfo:
        ...

    @typing.overload
    def MakeStaticPropertyInstanceAccessError(self, tracker: Microsoft.Scripting.Actions.PropertyTracker, isAssignment: bool, parameters: System.Collections.Generic.IList[System.Dynamic.DynamicMetaObject], ) -> Microsoft.Scripting.Actions.ErrorInfo:
        ...

    def MakeStaticAssignFromDerivedTypeError(self, accessingType: System.Type, self: System.Dynamic.DynamicMetaObject, assigning: Microsoft.Scripting.Actions.MemberTracker, assignedValue: System.Dynamic.DynamicMetaObject, context: Microsoft.Scripting.Actions.Calls.OverloadResolverFactory, ) -> Microsoft.Scripting.Actions.ErrorInfo:
        ...

    def MakeSetValueTypeFieldError(self, field: Microsoft.Scripting.Actions.FieldTracker, instance: System.Dynamic.DynamicMetaObject, value: System.Dynamic.DynamicMetaObject, ) -> Microsoft.Scripting.Actions.ErrorInfo:
        ...

    def MakeConversionError(self, toType: System.Type, value: System.Linq.Expressions.Expression, ) -> Microsoft.Scripting.Actions.ErrorInfo:
        ...

    def MakeMissingMemberError(self, type: System.Type, self: System.Dynamic.DynamicMetaObject, name: str, ) -> Microsoft.Scripting.Actions.ErrorInfo:
        ...

    def MakeMissingMemberErrorForAssign(self, type: System.Type, self: System.Dynamic.DynamicMetaObject, name: str, ) -> Microsoft.Scripting.Actions.ErrorInfo:
        ...

    def MakeMissingMemberErrorForAssignReadOnlyProperty(self, type: System.Type, self: System.Dynamic.DynamicMetaObject, name: str, ) -> Microsoft.Scripting.Actions.ErrorInfo:
        ...

    def MakeMissingMemberErrorForDelete(self, type: System.Type, self: System.Dynamic.DynamicMetaObject, name: str, ) -> Microsoft.Scripting.Actions.ErrorInfo:
        ...

    def GetTypeName(self, t: System.Type, ) -> str:
        ...

    def GetObjectTypeName(self, arg: System.Object, ) -> str:
        ...

    def GetAllExtensionMembers(self, type: System.Type, name: str, ) -> Microsoft.Scripting.Actions.MemberGroup:
        ...

    def GetExtensionMembers(self, declaringType: System.Type, name: str, ) -> Microsoft.Scripting.Actions.MemberGroup:
        ...

    def GetExtensionOperator(self, ext: System.Type, name: str, ) -> System.Reflection.MethodInfo:
        ...

    def IncludeExtensionMember(self, member: System.Reflection.MemberInfo, ) -> bool:
        ...

    def GetExtensionTypes(self, t: System.Type, ) -> System.Collections.Generic.IList[System.Type]:
        ...

    def ReturnMemberTracker(self, type: System.Type, memberTracker: Microsoft.Scripting.Actions.MemberTracker, ) -> System.Dynamic.DynamicMetaObject:
        ...

    def MakeCallExpression(self, resolverFactory: Microsoft.Scripting.Actions.Calls.OverloadResolverFactory, method: System.Reflection.MethodInfo, parameters: System.Array[System.Dynamic.DynamicMetaObject], ) -> System.Dynamic.DynamicMetaObject:
        ...

class ErrorInfo(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def Kind(self) -> int:
        ...

    @property
    def Expression(self) -> System.Linq.Expressions.Expression:
        ...

    # methods
    def __init__(self, value: System.Linq.Expressions.Expression, kind: int, ):
        ...

    @staticmethod
    def FromException(exceptionValue: System.Linq.Expressions.Expression, ) -> Microsoft.Scripting.Actions.ErrorInfo:
        ...

    @staticmethod
    def FromValue(resultValue: System.Linq.Expressions.Expression, ) -> Microsoft.Scripting.Actions.ErrorInfo:
        ...

    @staticmethod
    def FromValueNoError(resultValue: System.Linq.Expressions.Expression, ) -> Microsoft.Scripting.Actions.ErrorInfo:
        ...

class TrackerTypes(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    None_: int = ...
    Constructor: int = ...
    Event: int = ...
    Field: int = ...
    Method: int = ...
    Property: int = ...
    Type: int = ...
    Namespace: int = ...
    MethodGroup: int = ...
    TypeGroup: int = ...
    Custom: int = ...
    Bound: int = ...
    All: int = ...

class NamespaceTracker(Microsoft.Scripting.Runtime.IMembersList, System.Collections.Generic.IEnumerable[System.Collections.Generic.KeyValuePair[str, System.Object]], System.Collections.IEnumerable, Microsoft.Scripting.Actions.MemberTracker):
    @typing.overload
    def __init__(self, **kwargs):
        self._dict: System.Collections.Generic.Dictionary[str, Microsoft.Scripting.Actions.MemberTracker]
        self._packageAssemblies: System.Collections.Generic.List[System.Reflection.Assembly]
        self._typeNames: System.Collections.Generic.Dictionary[System.Reflection.Assembly, Microsoft.Scripting.Actions.NamespaceTracker.TypeNames]
        ...

    # static fields

    # properties
    @property
    def Name(self) -> str:
        ...

    @property
    def Item(self) -> System.Object:
        ...

    @property
    def Count(self) -> int:
        ...

    @property
    def Keys(self) -> System.Collections.Generic.ICollection[str]:
        ...

    @property
    def PackageAssemblies(self) -> System.Collections.Generic.IList[System.Reflection.Assembly]:
        ...

    @property
    def Id(self) -> int:
        ...

    @property
    def MemberType(self) -> int:
        ...

    @property
    def DeclaringType(self) -> System.Type:
        ...

    # methods
    def __init__(self, name: str, ):
        ...

    def ToString(self, ) -> str:
        ...

    def GetOrMakeChildPackage(self, childName: str, assem: System.Reflection.Assembly, ) -> Microsoft.Scripting.Actions.NamespaceTracker:
        ...

    def MakeChildPackage(self, childName: str, assem: System.Reflection.Assembly, ) -> Microsoft.Scripting.Actions.NamespaceTracker:
        ...

    def GetFullChildName(self, childName: str, ) -> str:
        ...

    @staticmethod
    def LoadType(assem: System.Reflection.Assembly, fullTypeName: str, ) -> System.Type:
        ...

    def AddTypeName(self, typeName: str, assem: System.Reflection.Assembly, ) -> None:
        ...

    def LoadAllTypes(self, ) -> None:
        ...

    def DiscoverAllTypes(self, assem: System.Reflection.Assembly, ) -> None:
        ...

    def GetOrMakePackageHierarchy(self, assem: System.Reflection.Assembly, fullNamespace: str, ) -> Microsoft.Scripting.Actions.NamespaceTracker:
        ...

    def CheckForUnlistedType(self, nameString: str, ) -> Microsoft.Scripting.Actions.MemberTracker:
        ...

    @typing.overload
    def TryGetValue(self, name: str, value: ref[System.Object], ) -> bool:
        ...

    @typing.overload
    def TryGetValue(self, name: str, value: ref[Microsoft.Scripting.Actions.MemberTracker], ) -> bool:
        ...

    def ContainsKey(self, name: str, ) -> bool:
        ...

    def AddKeys(self, res: System.Collections.IList, ) -> System.Collections.IList:
        ...

    def GetEnumerator(self, ) -> System.Collections.Generic.IEnumerator[System.Collections.Generic.KeyValuePair[str, System.Object]]:
        ...

    def GetEnumerator(self, ) -> System.Collections.IEnumerator:
        ...

    def LoadNamespaces(self, ) -> None:
        ...

    def SetTopPackage(self, pkg: Microsoft.Scripting.Actions.TopNamespaceTracker, ) -> None:
        ...

    def GetMemberNames(self, ) -> System.Collections.Generic.IList[str]:
        ...

    def UpdateId(self, ) -> None:
        ...

    def UpdateSubtreeIds(self, ) -> None:
        ...

class TopNamespaceTracker(Microsoft.Scripting.Runtime.IMembersList, System.Collections.Generic.IEnumerable[System.Collections.Generic.KeyValuePair[str, System.Object]], System.Collections.IEnumerable, Microsoft.Scripting.Actions.NamespaceTracker):
    @typing.overload
    def __init__(self, **kwargs):
        self.HierarchyLock: System.Object
        self._dict: System.Collections.Generic.Dictionary[str, Microsoft.Scripting.Actions.MemberTracker]
        self._packageAssemblies: System.Collections.Generic.List[System.Reflection.Assembly]
        self._typeNames: System.Collections.Generic.Dictionary[System.Reflection.Assembly, Microsoft.Scripting.Actions.NamespaceTracker.TypeNames]
        ...

    # static fields

    # properties
    @property
    def DomainManager(self) -> Microsoft.Scripting.Runtime.ScriptDomainManager:
        ...

    @property
    def Name(self) -> str:
        ...

    @property
    def Item(self) -> System.Object:
        ...

    @property
    def Count(self) -> int:
        ...

    @property
    def Keys(self) -> System.Collections.Generic.ICollection[str]:
        ...

    @property
    def PackageAssemblies(self) -> System.Collections.Generic.IList[System.Reflection.Assembly]:
        ...

    @property
    def Id(self) -> int:
        ...

    @property
    def MemberType(self) -> int:
        ...

    @property
    def DeclaringType(self) -> System.Type:
        ...

    # methods
    def __init__(self, manager: Microsoft.Scripting.Runtime.ScriptDomainManager, ):
        ...

    def TryGetPackage(self, name: str, ) -> Microsoft.Scripting.Actions.NamespaceTracker:
        ...

    def TryGetPackageAny(self, name: str, ) -> Microsoft.Scripting.Actions.MemberTracker:
        ...

    def TryGetPackageLazy(self, name: str, ) -> Microsoft.Scripting.Actions.MemberTracker:
        ...

    def LoadAssembly(self, assem: System.Reflection.Assembly, ) -> bool:
        ...

    @staticmethod
    def PublishComTypes(interopAssembly: System.Reflection.Assembly, ) -> None:
        ...

    def LoadNamespaces(self, ) -> None:
        ...

class ErrorInfoKind(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    Exception: int = ...
    Error: int = ...
    Success: int = ...

class PropertyTracker(Microsoft.Scripting.Actions.MemberTracker, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def MemberType(self) -> int:
        ...

    @property
    @abc.abstractmethod
    def IsStatic(self) -> bool:
        ...

    @property
    @abc.abstractmethod
    def PropertyType(self) -> System.Type:
        ...

    @property
    @abc.abstractmethod
    def DeclaringType(self) -> System.Type:
        ...

    @property
    @abc.abstractmethod
    def Name(self) -> str:
        ...

    # methods
    def __init__(self, ):
        ...

    @abc.abstractmethod
    @typing.overload
    def GetGetMethod(self, ) -> System.Reflection.MethodInfo:
        ...

    @abc.abstractmethod
    @typing.overload
    def GetGetMethod(self, privateMembers: bool, ) -> System.Reflection.MethodInfo:
        ...

    @abc.abstractmethod
    @typing.overload
    def GetSetMethod(self, ) -> System.Reflection.MethodInfo:
        ...

    @abc.abstractmethod
    @typing.overload
    def GetSetMethod(self, privateMembers: bool, ) -> System.Reflection.MethodInfo:
        ...

    @typing.overload
    def GetDeleteMethod(self, ) -> System.Reflection.MethodInfo:
        ...

    @typing.overload
    def GetDeleteMethod(self, privateMembers: bool, ) -> System.Reflection.MethodInfo:
        ...

    @abc.abstractmethod
    def GetIndexParameters(self, ) -> System.Array[System.Reflection.ParameterInfo]:
        ...

    def GetValue(self, resolverFactory: Microsoft.Scripting.Actions.Calls.OverloadResolverFactory, binder: Microsoft.Scripting.Actions.ActionBinder, instanceType: System.Type, ) -> System.Dynamic.DynamicMetaObject:
        ...

    def GetError(self, binder: Microsoft.Scripting.Actions.ActionBinder, instanceType: System.Type, ) -> Microsoft.Scripting.Actions.ErrorInfo:
        ...

    def GetBoundValue(self, resolverFactory: Microsoft.Scripting.Actions.Calls.OverloadResolverFactory, binder: Microsoft.Scripting.Actions.ActionBinder, type: System.Type, instance: System.Dynamic.DynamicMetaObject, ) -> System.Dynamic.DynamicMetaObject:
        ...

    def GetBoundError(self, binder: Microsoft.Scripting.Actions.ActionBinder, instance: System.Dynamic.DynamicMetaObject, instanceType: System.Type, ) -> Microsoft.Scripting.Actions.ErrorInfo:
        ...

    def BindToInstance(self, instance: System.Dynamic.DynamicMetaObject, ) -> Microsoft.Scripting.Actions.MemberTracker:
        ...

    def ResolveGetter(self, instanceType: System.Type, privateBinding: bool, ) -> System.Reflection.MethodInfo:
        ...

class TypeGroup(Microsoft.Scripting.Runtime.IMembersList, Microsoft.Scripting.Actions.TypeTracker):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def SampleType(self) -> System.Type:
        ...

    @property
    def Types(self) -> System.Collections.Generic.IEnumerable[System.Type]:
        ...

    @property
    def TypesByArity(self) -> System.Collections.Generic.IDictionary[int, System.Type]:
        ...

    @property
    def MemberType(self) -> int:
        ...

    @property
    def DeclaringType(self) -> System.Type:
        ...

    @property
    def Name(self) -> str:
        ...

    @property
    def Type(self) -> System.Type:
        ...

    @property
    def IsGenericType(self) -> bool:
        ...

    @property
    def IsPublic(self) -> bool:
        ...

    # methods
    @typing.overload
    def __init__(self, t1: System.Type, arity1: int, t2: System.Type, arity2: int, ):
        ...

    @typing.overload
    def __init__(self, t1: System.Type, existingTypes: Microsoft.Scripting.Actions.TypeGroup, ):
        ...

    def ToString(self, ) -> str:
        ...

    def GetMemberNames(self, ) -> System.Collections.Generic.IList[str]:
        ...

    def GetTypeForArity(self, arity: int, ) -> Microsoft.Scripting.Actions.TypeTracker:
        ...

    @staticmethod
    def UpdateTypeEntity(existingTypeEntity: Microsoft.Scripting.Actions.TypeTracker, newType: Microsoft.Scripting.Actions.TypeTracker, ) -> Microsoft.Scripting.Actions.TypeTracker:
        ...

    @staticmethod
    def GetGenericArity(type: System.Type, ) -> int:
        ...

    def GetNonGenericType(self, ) -> System.Type:
        ...

    def TryGetNonGenericType(self, nonGenericType: ref[System.Type], ) -> bool:
        ...

class ILightExceptionBinder(abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    @abc.abstractmethod
    def SupportsLightThrow(self) -> bool:
        ...

    # methods
    @abc.abstractmethod
    def GetLightExceptionBinder(self, ) -> System.Runtime.CompilerServices.CallSiteBinder:
        ...

class MemberTracker(System.Object, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields
    EmptyTrackers: System.Array[Microsoft.Scripting.Actions.MemberTracker] = ...

    # properties
    @property
    @abc.abstractmethod
    def MemberType(self) -> int:
        ...

    @property
    @abc.abstractmethod
    def DeclaringType(self) -> System.Type:
        ...

    @property
    @abc.abstractmethod
    def Name(self) -> str:
        ...

    # methods
    def __init__(self, ):
        ...

    @staticmethod
    @typing.overload
    def FromMemberInfo(member: System.Reflection.MemberInfo, ) -> Microsoft.Scripting.Actions.MemberTracker:
        ...

    @staticmethod
    @typing.overload
    def FromMemberInfo(member: System.Reflection.MemberInfo, extending: System.Type, ) -> Microsoft.Scripting.Actions.MemberTracker:
        ...

    def GetValue(self, resolverFactory: Microsoft.Scripting.Actions.Calls.OverloadResolverFactory, binder: Microsoft.Scripting.Actions.ActionBinder, instanceType: System.Type, ) -> System.Dynamic.DynamicMetaObject:
        ...

    @typing.overload
    def SetValue(self, resolverFactory: Microsoft.Scripting.Actions.Calls.OverloadResolverFactory, binder: Microsoft.Scripting.Actions.ActionBinder, instanceType: System.Type, value: System.Dynamic.DynamicMetaObject, ) -> System.Dynamic.DynamicMetaObject:
        ...

    @typing.overload
    def SetValue(self, resolverFactory: Microsoft.Scripting.Actions.Calls.OverloadResolverFactory, binder: Microsoft.Scripting.Actions.ActionBinder, instanceType: System.Type, value: System.Dynamic.DynamicMetaObject, errorSuggestion: System.Dynamic.DynamicMetaObject, ) -> System.Dynamic.DynamicMetaObject:
        ...

    def Call(self, resolverFactory: Microsoft.Scripting.Actions.Calls.OverloadResolverFactory, binder: Microsoft.Scripting.Actions.ActionBinder, arguments: System.Array[System.Dynamic.DynamicMetaObject], ) -> System.Dynamic.DynamicMetaObject:
        ...

    def GetError(self, binder: Microsoft.Scripting.Actions.ActionBinder, instanceType: System.Type, ) -> Microsoft.Scripting.Actions.ErrorInfo:
        ...

    def GetBoundError(self, binder: Microsoft.Scripting.Actions.ActionBinder, instance: System.Dynamic.DynamicMetaObject, instanceType: System.Type, ) -> Microsoft.Scripting.Actions.ErrorInfo:
        ...

    def GetBoundValue(self, resolverFactory: Microsoft.Scripting.Actions.Calls.OverloadResolverFactory, binder: Microsoft.Scripting.Actions.ActionBinder, instanceType: System.Type, instance: System.Dynamic.DynamicMetaObject, ) -> System.Dynamic.DynamicMetaObject:
        ...

    @typing.overload
    def SetBoundValue(self, resolverFactory: Microsoft.Scripting.Actions.Calls.OverloadResolverFactory, binder: Microsoft.Scripting.Actions.ActionBinder, instanceType: System.Type, value: System.Dynamic.DynamicMetaObject, instance: System.Dynamic.DynamicMetaObject, ) -> System.Dynamic.DynamicMetaObject:
        ...

    @typing.overload
    def SetBoundValue(self, resolverFactory: Microsoft.Scripting.Actions.Calls.OverloadResolverFactory, binder: Microsoft.Scripting.Actions.ActionBinder, instanceType: System.Type, value: System.Dynamic.DynamicMetaObject, instance: System.Dynamic.DynamicMetaObject, errorSuggestion: System.Dynamic.DynamicMetaObject, ) -> System.Dynamic.DynamicMetaObject:
        ...

    def BindToInstance(self, instance: System.Dynamic.DynamicMetaObject, ) -> Microsoft.Scripting.Actions.MemberTracker:
        ...

class DefaultBinder(Microsoft.Scripting.Actions.ActionBinder):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields
    Instance: Microsoft.Scripting.Actions.DefaultBinder = ...

    # properties
    @property
    def PrivateBinding(self) -> bool:
        ...

    @property
    def Manager(self) -> Microsoft.Scripting.Runtime.ScriptDomainManager:
        ...

    # methods
    def __init__(self, ):
        ...

    @typing.overload
    def DoOperation(self, operation: str, args: System.Array[System.Dynamic.DynamicMetaObject], ) -> System.Dynamic.DynamicMetaObject:
        ...

    @typing.overload
    def DoOperation(self, operation: str, resolverFactory: Microsoft.Scripting.Actions.Calls.OverloadResolverFactory, args: System.Array[System.Dynamic.DynamicMetaObject], ) -> System.Dynamic.DynamicMetaObject:
        ...

    @typing.overload
    def DoOperation(self, operation: int, args: System.Array[System.Dynamic.DynamicMetaObject], ) -> System.Dynamic.DynamicMetaObject:
        ...

    @typing.overload
    def DoOperation(self, operation: int, resolverFactory: Microsoft.Scripting.Actions.Calls.OverloadResolverFactory, args: System.Array[System.Dynamic.DynamicMetaObject], ) -> System.Dynamic.DynamicMetaObject:
        ...

    @typing.overload
    def GetIndex(self, args: System.Array[System.Dynamic.DynamicMetaObject], ) -> System.Dynamic.DynamicMetaObject:
        ...

    @typing.overload
    def GetIndex(self, resolverFactory: Microsoft.Scripting.Actions.Calls.OverloadResolverFactory, args: System.Array[System.Dynamic.DynamicMetaObject], ) -> System.Dynamic.DynamicMetaObject:
        ...

    @typing.overload
    def SetIndex(self, args: System.Array[System.Dynamic.DynamicMetaObject], ) -> System.Dynamic.DynamicMetaObject:
        ...

    @typing.overload
    def SetIndex(self, resolverFactory: Microsoft.Scripting.Actions.Calls.OverloadResolverFactory, args: System.Array[System.Dynamic.DynamicMetaObject], ) -> System.Dynamic.DynamicMetaObject:
        ...

    def GetDocumentation(self, target: System.Dynamic.DynamicMetaObject, ) -> System.Dynamic.DynamicMetaObject:
        ...

    def GetMemberNames(self, target: System.Dynamic.DynamicMetaObject, ) -> System.Dynamic.DynamicMetaObject:
        ...

    def GetCallSignatures(self, target: System.Dynamic.DynamicMetaObject, ) -> System.Dynamic.DynamicMetaObject:
        ...

    def GetIsCallable(self, target: System.Dynamic.DynamicMetaObject, ) -> System.Dynamic.DynamicMetaObject:
        ...

    @typing.overload
    def MakeGeneralOperatorRule(self, operation: str, resolverFactory: Microsoft.Scripting.Actions.Calls.OverloadResolverFactory, args: System.Array[System.Dynamic.DynamicMetaObject], ) -> System.Dynamic.DynamicMetaObject:
        ...

    @typing.overload
    def MakeGeneralOperatorRule(self, operation: int, resolverFactory: Microsoft.Scripting.Actions.Calls.OverloadResolverFactory, args: System.Array[System.Dynamic.DynamicMetaObject], ) -> System.Dynamic.DynamicMetaObject:
        ...

    def MakeGeneratorOperatorRule(self, resolverFactory: Microsoft.Scripting.Actions.Calls.OverloadResolverFactory, args: System.Array[System.Dynamic.DynamicMetaObject], info: Microsoft.Scripting.Actions.OperatorInfo, ) -> System.Dynamic.DynamicMetaObject:
        ...

    def MakeComparisonRule(self, info: Microsoft.Scripting.Actions.OperatorInfo, resolverFactory: Microsoft.Scripting.Actions.Calls.OverloadResolverFactory, args: System.Array[System.Dynamic.DynamicMetaObject], ) -> System.Dynamic.DynamicMetaObject:
        ...

    def TryComparisonMethod(self, info: Microsoft.Scripting.Actions.OperatorInfo, resolverFactory: Microsoft.Scripting.Actions.Calls.OverloadResolverFactory, target: System.Dynamic.DynamicMetaObject, args: System.Array[System.Dynamic.DynamicMetaObject], ) -> System.Dynamic.DynamicMetaObject:
        ...

    @staticmethod
    def MakeOperatorError(info: Microsoft.Scripting.Actions.OperatorInfo, args: System.Array[System.Dynamic.DynamicMetaObject], ) -> System.Dynamic.DynamicMetaObject:
        ...

    def TryNumericComparison(self, info: Microsoft.Scripting.Actions.OperatorInfo, resolverFactory: Microsoft.Scripting.Actions.Calls.OverloadResolverFactory, args: System.Array[System.Dynamic.DynamicMetaObject], ) -> System.Dynamic.DynamicMetaObject:
        ...

    def TryInvertedComparison(self, info: Microsoft.Scripting.Actions.OperatorInfo, resolverFactory: Microsoft.Scripting.Actions.Calls.OverloadResolverFactory, target: System.Dynamic.DynamicMetaObject, args: System.Array[System.Dynamic.DynamicMetaObject], ) -> System.Dynamic.DynamicMetaObject:
        ...

    @staticmethod
    def TryNullComparisonRule(args: System.Array[System.Dynamic.DynamicMetaObject], ) -> System.Dynamic.DynamicMetaObject:
        ...

    @staticmethod
    def TryPrimitiveCompare(info: Microsoft.Scripting.Actions.OperatorInfo, args: System.Array[System.Dynamic.DynamicMetaObject], ) -> System.Dynamic.DynamicMetaObject:
        ...

    def MakeOperatorRule(self, info: Microsoft.Scripting.Actions.OperatorInfo, resolverFactory: Microsoft.Scripting.Actions.Calls.OverloadResolverFactory, args: System.Array[System.Dynamic.DynamicMetaObject], ) -> System.Dynamic.DynamicMetaObject:
        ...

    @staticmethod
    def TryPrimitiveOperator(info: Microsoft.Scripting.Actions.OperatorInfo, args: System.Array[System.Dynamic.DynamicMetaObject], ) -> System.Dynamic.DynamicMetaObject:
        ...

    def TryForwardOperator(self, info: Microsoft.Scripting.Actions.OperatorInfo, resolverFactory: Microsoft.Scripting.Actions.Calls.OverloadResolverFactory, args: System.Array[System.Dynamic.DynamicMetaObject], ) -> System.Dynamic.DynamicMetaObject:
        ...

    def TryReverseOperator(self, info: Microsoft.Scripting.Actions.OperatorInfo, resolverFactory: Microsoft.Scripting.Actions.Calls.OverloadResolverFactory, args: System.Array[System.Dynamic.DynamicMetaObject], ) -> System.Dynamic.DynamicMetaObject:
        ...

    @staticmethod
    def TryMakeDefaultUnaryRule(info: Microsoft.Scripting.Actions.OperatorInfo, args: System.Array[System.Dynamic.DynamicMetaObject], ) -> System.Dynamic.DynamicMetaObject:
        ...

    @staticmethod
    def MakeCallSignatureResult(methods: System.Array[System.Reflection.MethodBase], target: System.Dynamic.DynamicMetaObject, ) -> System.Dynamic.DynamicMetaObject:
        ...

    @staticmethod
    def GetArgType(args: System.Array[System.Dynamic.DynamicMetaObject], index: int, ) -> System.Type:
        ...

    def MakeMethodIndexRule(self, oper: int, resolverFactory: Microsoft.Scripting.Actions.Calls.OverloadResolverFactory, args: System.Array[System.Dynamic.DynamicMetaObject], ) -> System.Dynamic.DynamicMetaObject:
        ...

    def MakeArrayIndexRule(self, factory: Microsoft.Scripting.Actions.Calls.OverloadResolverFactory, oper: int, args: System.Array[System.Dynamic.DynamicMetaObject], ) -> System.Dynamic.DynamicMetaObject:
        ...

    def GetMethodsFromDefaults(self, defaults: System.Collections.Generic.IEnumerable[System.Reflection.MemberInfo], op: int, ) -> System.Array[System.Reflection.MethodInfo]:
        ...

    def TryMakeBindingTarget(self, resolverFactory: Microsoft.Scripting.Actions.Calls.OverloadResolverFactory, targets: System.Array[System.Reflection.MethodInfo], args: System.Array[System.Dynamic.DynamicMetaObject], restrictions: System.Dynamic.BindingRestrictions, ) -> System.Dynamic.DynamicMetaObject:
        ...

    def TryMakeInvertedBindingTarget(self, resolverFactory: Microsoft.Scripting.Actions.Calls.OverloadResolverFactory, targets: System.Array[System.Reflection.MethodBase], args: System.Array[System.Dynamic.DynamicMetaObject], ) -> System.Dynamic.DynamicMetaObject:
        ...

    @staticmethod
    def GetInvertedOperator(op: int, ) -> int:
        ...

    def ConvertIfNeeded(self, factory: Microsoft.Scripting.Actions.Calls.OverloadResolverFactory, expression: System.Linq.Expressions.Expression, type: System.Type, ) -> System.Linq.Expressions.Expression:
        ...

    def GetApplicableMembers(self, t: System.Type, info: Microsoft.Scripting.Actions.OperatorInfo, ) -> System.Array[System.Reflection.MethodInfo]:
        ...

    @staticmethod
    def FilterNonMethods(t: System.Type, members: Microsoft.Scripting.Actions.MemberGroup, ) -> System.Array[System.Reflection.MethodInfo]:
        ...

    @typing.overload
    def SetMember(self, name: str, target: System.Dynamic.DynamicMetaObject, value: System.Dynamic.DynamicMetaObject, ) -> System.Dynamic.DynamicMetaObject:
        ...

    @typing.overload
    def SetMember(self, name: str, target: System.Dynamic.DynamicMetaObject, value: System.Dynamic.DynamicMetaObject, resolverFactory: Microsoft.Scripting.Actions.Calls.OverloadResolverFactory, ) -> System.Dynamic.DynamicMetaObject:
        ...

    @typing.overload
    def SetMember(self, name: str, target: System.Dynamic.DynamicMetaObject, value: System.Dynamic.DynamicMetaObject, errorSuggestion: System.Dynamic.DynamicMetaObject, ) -> System.Dynamic.DynamicMetaObject:
        ...

    @typing.overload
    def SetMember(self, name: str, target: System.Dynamic.DynamicMetaObject, value: System.Dynamic.DynamicMetaObject, errorSuggestion: System.Dynamic.DynamicMetaObject, resolverFactory: Microsoft.Scripting.Actions.Calls.OverloadResolverFactory, ) -> System.Dynamic.DynamicMetaObject:
        ...

    def MakeSetMemberTarget(self, memInfo: Microsoft.Scripting.Actions.DefaultBinder.SetOrDeleteMemberInfo, target: System.Dynamic.DynamicMetaObject, value: System.Dynamic.DynamicMetaObject, errorSuggestion: System.Dynamic.DynamicMetaObject, ) -> System.Dynamic.DynamicMetaObject:
        ...

    def MakeSetMemberRule(self, memInfo: Microsoft.Scripting.Actions.DefaultBinder.SetOrDeleteMemberInfo, type: System.Type, self: System.Dynamic.DynamicMetaObject, value: System.Dynamic.DynamicMetaObject, errorSuggestion: System.Dynamic.DynamicMetaObject, ) -> None:
        ...

    @typing.overload
    def MakeGenericBody(self, memInfo: Microsoft.Scripting.Actions.DefaultBinder.SetOrDeleteMemberInfo, instance: System.Dynamic.DynamicMetaObject, target: System.Dynamic.DynamicMetaObject, instanceType: System.Type, tracker: Microsoft.Scripting.Actions.MemberTracker, errorSuggestion: System.Dynamic.DynamicMetaObject, ) -> None:
        ...

    @typing.overload
    def MakeGenericBody(self, getMemInfo: Microsoft.Scripting.Actions.DefaultBinder.GetMemberInfo, instanceType: System.Type, members: Microsoft.Scripting.Actions.MemberGroup, instance: System.Dynamic.DynamicMetaObject, ) -> None:
        ...

    def MakePropertyRule(self, memInfo: Microsoft.Scripting.Actions.DefaultBinder.SetOrDeleteMemberInfo, instance: System.Dynamic.DynamicMetaObject, target: System.Dynamic.DynamicMetaObject, targetType: System.Type, properties: Microsoft.Scripting.Actions.MemberGroup, errorSuggestion: System.Dynamic.DynamicMetaObject, ) -> None:
        ...

    def MakeFieldRule(self, memInfo: Microsoft.Scripting.Actions.DefaultBinder.SetOrDeleteMemberInfo, instance: System.Dynamic.DynamicMetaObject, target: System.Dynamic.DynamicMetaObject, targetType: System.Type, fields: Microsoft.Scripting.Actions.MemberGroup, errorSuggestion: System.Dynamic.DynamicMetaObject, ) -> None:
        ...

    @typing.overload
    def MakeReturnValue(self, expression: System.Dynamic.DynamicMetaObject, target: System.Dynamic.DynamicMetaObject, ) -> System.Dynamic.DynamicMetaObject:
        ...

    @typing.overload
    def MakeReturnValue(self, expression: System.Linq.Expressions.Expression, target: System.Dynamic.DynamicMetaObject, ) -> System.Linq.Expressions.Expression:
        ...

    def MakeOperatorSetMemberBody(self, memInfo: Microsoft.Scripting.Actions.DefaultBinder.SetOrDeleteMemberInfo, self: System.Dynamic.DynamicMetaObject, target: System.Dynamic.DynamicMetaObject, type: System.Type, name: str, ) -> bool:
        ...

    @staticmethod
    def MakeGenericPropertyExpression(memInfo: Microsoft.Scripting.Actions.DefaultBinder.SetOrDeleteMemberInfo, ) -> System.Linq.Expressions.Expression:
        ...

    @typing.overload
    def ConvertTo(self, toType: System.Type, kind: int, arg: System.Dynamic.DynamicMetaObject, ) -> System.Dynamic.DynamicMetaObject:
        ...

    @typing.overload
    def ConvertTo(self, toType: System.Type, kind: int, arg: System.Dynamic.DynamicMetaObject, resolverFactory: Microsoft.Scripting.Actions.Calls.OverloadResolverFactory, ) -> System.Dynamic.DynamicMetaObject:
        ...

    @typing.overload
    def ConvertTo(self, toType: System.Type, kind: int, arg: System.Dynamic.DynamicMetaObject, resolverFactory: Microsoft.Scripting.Actions.Calls.OverloadResolverFactory, errorSuggestion: System.Dynamic.DynamicMetaObject, ) -> System.Dynamic.DynamicMetaObject:
        ...

    @staticmethod
    def TryConvertToObject(toType: System.Type, knownType: System.Type, arg: System.Dynamic.DynamicMetaObject, restrictions: System.Dynamic.BindingRestrictions, ) -> System.Dynamic.DynamicMetaObject:
        ...

    def TryAllConversions(self, factory: Microsoft.Scripting.Actions.Calls.OverloadResolverFactory, toType: System.Type, kind: int, knownType: System.Type, restrictions: System.Dynamic.BindingRestrictions, arg: System.Dynamic.DynamicMetaObject, ) -> System.Dynamic.DynamicMetaObject:
        ...

    @staticmethod
    def TryAssignableConversion(toType: System.Type, type: System.Type, restrictions: System.Dynamic.BindingRestrictions, arg: System.Dynamic.DynamicMetaObject, ) -> System.Dynamic.DynamicMetaObject:
        ...

    @typing.overload
    def TryUserDefinedConversion(self, kind: int, toType: System.Type, type: System.Type, restrictions: System.Dynamic.BindingRestrictions, arg: System.Dynamic.DynamicMetaObject, ) -> System.Dynamic.DynamicMetaObject:
        ...

    @staticmethod
    @typing.overload
    def TryUserDefinedConversion(kind: int, toType: System.Type, type: System.Type, conversions: Microsoft.Scripting.Actions.MemberGroup, isImplicit: bool, restrictions: System.Dynamic.BindingRestrictions, arg: System.Dynamic.DynamicMetaObject, ) -> System.Dynamic.DynamicMetaObject:
        ...

    def TryOneConversion(self, kind: int, toType: System.Type, type: System.Type, fromType: System.Type, methodName: str, isImplicit: bool, restrictions: System.Dynamic.BindingRestrictions, arg: System.Dynamic.DynamicMetaObject, ) -> System.Dynamic.DynamicMetaObject:
        ...

    @staticmethod
    def TryExtensibleConversion(toType: System.Type, type: System.Type, restrictions: System.Dynamic.BindingRestrictions, arg: System.Dynamic.DynamicMetaObject, ) -> System.Dynamic.DynamicMetaObject:
        ...

    @staticmethod
    def TryImplicitNumericConversion(toType: System.Type, type: System.Type, restrictions: System.Dynamic.BindingRestrictions, arg: System.Dynamic.DynamicMetaObject, ) -> System.Dynamic.DynamicMetaObject:
        ...

    def TryNullableConversion(self, factory: Microsoft.Scripting.Actions.Calls.OverloadResolverFactory, toType: System.Type, kind: int, knownType: System.Type, restrictions: System.Dynamic.BindingRestrictions, arg: System.Dynamic.DynamicMetaObject, ) -> System.Dynamic.DynamicMetaObject:
        ...

    @staticmethod
    def TryNullConversion(toType: System.Type, knownType: System.Type, restrictions: System.Dynamic.BindingRestrictions, ) -> System.Dynamic.DynamicMetaObject:
        ...

    def MakeErrorTarget(self, toType: System.Type, kind: int, restrictions: System.Dynamic.BindingRestrictions, arg: System.Dynamic.DynamicMetaObject, ) -> System.Dynamic.DynamicMetaObject:
        ...

    @staticmethod
    def MakeBoxingTarget(arg: System.Dynamic.DynamicMetaObject, restrictions: System.Dynamic.BindingRestrictions, ) -> System.Dynamic.DynamicMetaObject:
        ...

    @staticmethod
    def MakeConversionTarget(kind: int, method: Microsoft.Scripting.Actions.MethodTracker, fromType: System.Type, isImplicit: bool, restrictions: System.Dynamic.BindingRestrictions, arg: System.Dynamic.DynamicMetaObject, ) -> System.Dynamic.DynamicMetaObject:
        ...

    @staticmethod
    def MakeExtensibleConversionTarget(kind: int, method: Microsoft.Scripting.Actions.MethodTracker, fromType: System.Type, isImplicit: bool, restrictions: System.Dynamic.BindingRestrictions, arg: System.Dynamic.DynamicMetaObject, ) -> System.Dynamic.DynamicMetaObject:
        ...

    @staticmethod
    def MakeConversionTargetWorker(kind: int, method: Microsoft.Scripting.Actions.MethodTracker, isImplicit: bool, restrictions: System.Dynamic.BindingRestrictions, param: System.Linq.Expressions.Expression, ) -> System.Dynamic.DynamicMetaObject:
        ...

    @staticmethod
    def WrapForThrowingTry(kind: int, isImplicit: bool, ret: System.Linq.Expressions.Expression, retType: System.Type, ) -> System.Linq.Expressions.Expression:
        ...

    @staticmethod
    def MakeSimpleConversionTarget(toType: System.Type, restrictions: System.Dynamic.BindingRestrictions, arg: System.Dynamic.DynamicMetaObject, ) -> System.Dynamic.DynamicMetaObject:
        ...

    @staticmethod
    def MakeSimpleExtensibleConversionTarget(toType: System.Type, restrictions: System.Dynamic.BindingRestrictions, arg: System.Dynamic.DynamicMetaObject, ) -> System.Dynamic.DynamicMetaObject:
        ...

    @staticmethod
    def MakeExtensibleTarget(extensibleType: System.Type, restrictions: System.Dynamic.BindingRestrictions, arg: System.Dynamic.DynamicMetaObject, ) -> System.Dynamic.DynamicMetaObject:
        ...

    @staticmethod
    def MakeNullToNullableOfTTarget(toType: System.Type, restrictions: System.Dynamic.BindingRestrictions, ) -> System.Dynamic.DynamicMetaObject:
        ...

    @staticmethod
    def MakeTToNullableOfTTarget(toType: System.Type, knownType: System.Type, restrictions: System.Dynamic.BindingRestrictions, arg: System.Dynamic.DynamicMetaObject, ) -> System.Dynamic.DynamicMetaObject:
        ...

    def MakeConvertingToTToNullableOfTTarget(self, resolverFactory: Microsoft.Scripting.Actions.Calls.OverloadResolverFactory, toType: System.Type, kind: int, restrictions: System.Dynamic.BindingRestrictions, arg: System.Dynamic.DynamicMetaObject, ) -> System.Dynamic.DynamicMetaObject:
        ...

    @staticmethod
    def GetTryConvertReturnValue(type: System.Type, ) -> System.Linq.Expressions.Expression:
        ...

    @staticmethod
    def GetExtensibleValue(extType: System.Type, arg: System.Dynamic.DynamicMetaObject, ) -> System.Linq.Expressions.Expression:
        ...

    @staticmethod
    def GetUnderlyingType(fromType: System.Type, ) -> System.Type:
        ...

    @staticmethod
    def MakeNullTarget(toType: System.Type, restrictions: System.Dynamic.BindingRestrictions, ) -> System.Dynamic.DynamicMetaObject:
        ...

    def CanConvertFrom(self, fromType: System.Type, toType: System.Type, toNotNullable: bool, level: int, ) -> bool:
        ...

    def PreferConvert(self, t1: System.Type, t2: System.Type, ) -> int:
        ...

    def MakeUndeletableMemberError(self, type: System.Type, name: str, ) -> Microsoft.Scripting.Actions.ErrorInfo:
        ...

    def MakeNonPublicMemberGetError(self, resolverFactory: Microsoft.Scripting.Actions.Calls.OverloadResolverFactory, member: Microsoft.Scripting.Actions.MemberTracker, type: System.Type, instance: System.Dynamic.DynamicMetaObject, ) -> Microsoft.Scripting.Actions.ErrorInfo:
        ...

    def MakeReadOnlyMemberError(self, type: System.Type, name: str, ) -> Microsoft.Scripting.Actions.ErrorInfo:
        ...

    def MakeEventValidation(self, members: Microsoft.Scripting.Actions.MemberGroup, eventObject: System.Dynamic.DynamicMetaObject, value: System.Dynamic.DynamicMetaObject, resolverFactory: Microsoft.Scripting.Actions.Calls.OverloadResolverFactory, ) -> Microsoft.Scripting.Actions.ErrorInfo:
        ...

    @staticmethod
    @typing.overload
    def MakeError(error: Microsoft.Scripting.Actions.ErrorInfo, type: System.Type, ) -> System.Dynamic.DynamicMetaObject:
        ...

    @staticmethod
    @typing.overload
    def MakeError(error: Microsoft.Scripting.Actions.ErrorInfo, restrictions: System.Dynamic.BindingRestrictions, type: System.Type, ) -> System.Dynamic.DynamicMetaObject:
        ...

    @staticmethod
    def MakeAmbiguousMatchError(members: Microsoft.Scripting.Actions.MemberGroup, ) -> System.Linq.Expressions.Expression:
        ...

    def GetMemberType(self, members: Microsoft.Scripting.Actions.MemberGroup, error: ref[System.Linq.Expressions.Expression], ) -> int:
        ...

    def GetMethod(self, type: System.Type, name: str, ) -> System.Reflection.MethodInfo:
        ...

    @staticmethod
    def GetSpecialNameMethod(type: System.Type, name: str, ) -> System.Reflection.MethodInfo:
        ...

    @staticmethod
    def AmbiguousMatch(type: System.Type, name: str, ) -> System.Exception:
        ...

    @typing.overload
    def DeleteMember(self, name: str, target: System.Dynamic.DynamicMetaObject, ) -> System.Dynamic.DynamicMetaObject:
        ...

    @typing.overload
    def DeleteMember(self, name: str, target: System.Dynamic.DynamicMetaObject, resolutionFactory: Microsoft.Scripting.Actions.Calls.OverloadResolverFactory, ) -> System.Dynamic.DynamicMetaObject:
        ...

    @typing.overload
    def DeleteMember(self, name: str, target: System.Dynamic.DynamicMetaObject, resolutionFactory: Microsoft.Scripting.Actions.Calls.OverloadResolverFactory, errorSuggestion: System.Dynamic.DynamicMetaObject, ) -> System.Dynamic.DynamicMetaObject:
        ...

    def MakeDeleteMemberTarget(self, delInfo: Microsoft.Scripting.Actions.DefaultBinder.SetOrDeleteMemberInfo, target: System.Dynamic.DynamicMetaObject, errorSuggestion: System.Dynamic.DynamicMetaObject, ) -> System.Dynamic.DynamicMetaObject:
        ...

    @staticmethod
    def GetDeclaringMemberType(group: Microsoft.Scripting.Actions.MemberGroup, ) -> System.Type:
        ...

    def MakePropertyDeleteStatement(self, delInfo: Microsoft.Scripting.Actions.DefaultBinder.SetOrDeleteMemberInfo, instance: System.Dynamic.DynamicMetaObject, delete: System.Reflection.MethodInfo, ) -> None:
        ...

    def MakeOperatorDeleteMemberBody(self, delInfo: Microsoft.Scripting.Actions.DefaultBinder.SetOrDeleteMemberInfo, instance: System.Dynamic.DynamicMetaObject, type: System.Type, name: str, ) -> bool:
        ...

    @typing.overload
    def GetMember(self, name: str, target: System.Dynamic.DynamicMetaObject, ) -> System.Dynamic.DynamicMetaObject:
        ...

    @typing.overload
    def GetMember(self, name: str, target: System.Dynamic.DynamicMetaObject, resolverFactory: Microsoft.Scripting.Actions.Calls.OverloadResolverFactory, ) -> System.Dynamic.DynamicMetaObject:
        ...

    @typing.overload
    def GetMember(self, name: str, target: System.Dynamic.DynamicMetaObject, resolverFactory: Microsoft.Scripting.Actions.Calls.OverloadResolverFactory, isNoThrow: bool, errorSuggestion: System.Dynamic.DynamicMetaObject, ) -> System.Dynamic.DynamicMetaObject:
        ...

    @typing.overload
    def GetMember(self, name: str, target: System.Dynamic.DynamicMetaObject, isNoThrow: bool, errorSuggestion: System.Dynamic.DynamicMetaObject, ) -> System.Dynamic.DynamicMetaObject:
        ...

    def MakeGetMemberTarget(self, getMemInfo: Microsoft.Scripting.Actions.DefaultBinder.GetMemberInfo, target: System.Dynamic.DynamicMetaObject, ) -> System.Dynamic.DynamicMetaObject:
        ...

    @staticmethod
    def EnsureTrackerRepresentsNonGenericType(tracker: Microsoft.Scripting.Actions.TypeTracker, ) -> System.Type:
        ...

    def MakeBodyHelper(self, getMemInfo: Microsoft.Scripting.Actions.DefaultBinder.GetMemberInfo, self: System.Dynamic.DynamicMetaObject, propSelf: System.Dynamic.DynamicMetaObject, targetType: System.Type, members: Microsoft.Scripting.Actions.MemberGroup, ) -> None:
        ...

    def MakeSuccessfulMemberAccess(self, getMemInfo: Microsoft.Scripting.Actions.DefaultBinder.GetMemberInfo, self: System.Dynamic.DynamicMetaObject, propSelf: System.Dynamic.DynamicMetaObject, selfType: System.Type, members: Microsoft.Scripting.Actions.MemberGroup, memberType: int, ) -> None:
        ...

    @staticmethod
    def IsTrackerApplicableForType(type: System.Type, mt: Microsoft.Scripting.Actions.MemberTracker, ) -> bool:
        ...

    def MakeTypeBody(self, getMemInfo: Microsoft.Scripting.Actions.DefaultBinder.GetMemberInfo, instanceType: System.Type, members: Microsoft.Scripting.Actions.MemberGroup, ) -> None:
        ...

    def MakeGenericBodyWorker(self, getMemInfo: Microsoft.Scripting.Actions.DefaultBinder.GetMemberInfo, instanceType: System.Type, tracker: Microsoft.Scripting.Actions.MemberTracker, instance: System.Dynamic.DynamicMetaObject, ) -> None:
        ...

    def MakeOperatorGetMemberBody(self, getMemInfo: Microsoft.Scripting.Actions.DefaultBinder.GetMemberInfo, instance: System.Dynamic.DynamicMetaObject, instanceType: System.Type, name: str, ) -> None:
        ...

    def MakeMissingMemberRuleForGet(self, getMemInfo: Microsoft.Scripting.Actions.DefaultBinder.GetMemberInfo, self: System.Dynamic.DynamicMetaObject, type: System.Type, ) -> None:
        ...

    @staticmethod
    def MakeOperationFailed() -> System.Linq.Expressions.MemberExpression:
        ...

    @typing.overload
    def Call(self, signature: Microsoft.Scripting.Actions.CallSignature, target: System.Dynamic.DynamicMetaObject, args: System.Array[System.Dynamic.DynamicMetaObject], ) -> System.Dynamic.DynamicMetaObject:
        ...

    @typing.overload
    def Call(self, signature: Microsoft.Scripting.Actions.CallSignature, resolverFactory: Microsoft.Scripting.Actions.Calls.OverloadResolverFactory, target: System.Dynamic.DynamicMetaObject, args: System.Array[System.Dynamic.DynamicMetaObject], ) -> System.Dynamic.DynamicMetaObject:
        ...

    @typing.overload
    def Call(self, signature: Microsoft.Scripting.Actions.CallSignature, errorSuggestion: System.Dynamic.DynamicMetaObject, resolverFactory: Microsoft.Scripting.Actions.Calls.OverloadResolverFactory, target: System.Dynamic.DynamicMetaObject, args: System.Array[System.Dynamic.DynamicMetaObject], ) -> System.Dynamic.DynamicMetaObject:
        ...

    def MakeMetaMethodCall(self, signature: Microsoft.Scripting.Actions.CallSignature, resolverFactory: Microsoft.Scripting.Actions.Calls.OverloadResolverFactory, targetInfo: Microsoft.Scripting.Actions.DefaultBinder.TargetInfo, ) -> System.Dynamic.DynamicMetaObject:
        ...

    def GetTargetInfo(self, target: System.Dynamic.DynamicMetaObject, args: System.Array[System.Dynamic.DynamicMetaObject], ) -> Microsoft.Scripting.Actions.DefaultBinder.TargetInfo:
        ...

    @staticmethod
    def TryGetMethodGroupTargets(target: System.Dynamic.DynamicMetaObject, args: System.Array[System.Dynamic.DynamicMetaObject], mthgrp: Microsoft.Scripting.Actions.MethodGroup, ) -> Microsoft.Scripting.Actions.DefaultBinder.TargetInfo:
        ...

    @staticmethod
    def TryGetMemberGroupTargets(target: System.Dynamic.DynamicMetaObject, args: System.Array[System.Dynamic.DynamicMetaObject], mg: Microsoft.Scripting.Actions.MemberGroup, ) -> Microsoft.Scripting.Actions.DefaultBinder.TargetInfo:
        ...

    def TryGetBoundMemberTargets(self, self: System.Dynamic.DynamicMetaObject, args: System.Array[System.Dynamic.DynamicMetaObject], bmt: Microsoft.Scripting.Actions.BoundMemberTracker, ) -> Microsoft.Scripting.Actions.DefaultBinder.TargetInfo:
        ...

    @staticmethod
    def TryGetDelegateTargets(target: System.Dynamic.DynamicMetaObject, args: System.Array[System.Dynamic.DynamicMetaObject], d: System.Delegate, ) -> Microsoft.Scripting.Actions.DefaultBinder.TargetInfo:
        ...

    def TryGetOperatorTargets(self, self: System.Dynamic.DynamicMetaObject, args: System.Array[System.Dynamic.DynamicMetaObject], target: System.Object, ) -> Microsoft.Scripting.Actions.DefaultBinder.TargetInfo:
        ...

    def MakeCannotCallRule(self, self: System.Dynamic.DynamicMetaObject, type: System.Type, ) -> System.Dynamic.DynamicMetaObject:
        ...

    @typing.overload
    def CallMethod(self, resolver: Microsoft.Scripting.Actions.DefaultOverloadResolver, targets: System.Collections.Generic.IList[System.Reflection.MethodBase], ) -> System.Dynamic.DynamicMetaObject:
        ...

    @typing.overload
    def CallMethod(self, resolver: Microsoft.Scripting.Actions.DefaultOverloadResolver, targets: System.Collections.Generic.IList[System.Reflection.MethodBase], name: str, ) -> System.Dynamic.DynamicMetaObject:
        ...

    @typing.overload
    def CallMethod(self, resolver: Microsoft.Scripting.Actions.DefaultOverloadResolver, targets: System.Collections.Generic.IList[System.Reflection.MethodBase], restrictions: System.Dynamic.BindingRestrictions, ) -> System.Dynamic.DynamicMetaObject:
        ...

    @typing.overload
    def CallMethod(self, resolver: Microsoft.Scripting.Actions.DefaultOverloadResolver, targets: System.Collections.Generic.IList[System.Reflection.MethodBase], restrictions: System.Dynamic.BindingRestrictions, name: str, ) -> System.Dynamic.DynamicMetaObject:
        ...

    @typing.overload
    def CallMethod(self, resolver: Microsoft.Scripting.Actions.DefaultOverloadResolver, targets: System.Collections.Generic.IList[System.Reflection.MethodBase], restrictions: System.Dynamic.BindingRestrictions, name: str, minLevel: int, maxLevel: int, target: ref[Microsoft.Scripting.Actions.Calls.BindingTarget], ) -> System.Dynamic.DynamicMetaObject:
        ...

    @staticmethod
    def GetTargetName(targets: System.Collections.Generic.IList[System.Reflection.MethodBase], ) -> str:
        ...

    def MakeInvalidParametersRule(self, binder: Microsoft.Scripting.Actions.DefaultOverloadResolver, restrictions: System.Dynamic.BindingRestrictions, bt: Microsoft.Scripting.Actions.Calls.BindingTarget, ) -> System.Dynamic.DynamicMetaObject:
        ...

    @staticmethod
    @typing.overload
    def MakeSplatTests(callType: int, signature: Microsoft.Scripting.Actions.CallSignature, args: System.Collections.Generic.IList[System.Dynamic.DynamicMetaObject], ) -> System.Dynamic.BindingRestrictions:
        ...

    @staticmethod
    @typing.overload
    def MakeSplatTests(callType: int, signature: Microsoft.Scripting.Actions.CallSignature, testTypes: bool, args: System.Collections.Generic.IList[System.Dynamic.DynamicMetaObject], ) -> System.Dynamic.BindingRestrictions:
        ...

    @staticmethod
    def MakeParamsArrayTest(callType: int, signature: Microsoft.Scripting.Actions.CallSignature, testTypes: bool, args: System.Collections.Generic.IList[System.Dynamic.DynamicMetaObject], ) -> System.Dynamic.BindingRestrictions:
        ...

    @staticmethod
    def MakeParamsTest(splattee: System.Dynamic.DynamicMetaObject, testTypes: bool, ) -> System.Dynamic.BindingRestrictions:
        ...

    @staticmethod
    def MakeParamsDictionaryTest(args: System.Collections.Generic.IList[System.Dynamic.DynamicMetaObject], testTypes: bool, ) -> System.Dynamic.BindingRestrictions:
        ...

class DefaultOverloadResolver(Microsoft.Scripting.Actions.Calls.OverloadResolver):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def Factory(self) -> Microsoft.Scripting.Actions.Calls.OverloadResolverFactory:
        ...

    @property
    def Signature(self) -> Microsoft.Scripting.Actions.CallSignature:
        ...

    @property
    def Arguments(self) -> System.Collections.Generic.IList[System.Dynamic.DynamicMetaObject]:
        ...

    @property
    def CallType(self) -> int:
        ...

    @property
    def Binder(self) -> Microsoft.Scripting.Actions.ActionBinder:
        ...

    @property
    def Temps(self) -> System.Collections.Generic.List[System.Linq.Expressions.ParameterExpression]:
        ...

    @property
    def MaxAccessedCollapsedArg(self) -> int:
        ...

    # methods
    @typing.overload
    def __init__(self, binder: Microsoft.Scripting.Actions.ActionBinder, instance: System.Dynamic.DynamicMetaObject, args: System.Collections.Generic.IList[System.Dynamic.DynamicMetaObject], signature: Microsoft.Scripting.Actions.CallSignature, ):
        ...

    @typing.overload
    def __init__(self, binder: Microsoft.Scripting.Actions.ActionBinder, args: System.Collections.Generic.IList[System.Dynamic.DynamicMetaObject], signature: Microsoft.Scripting.Actions.CallSignature, ):
        ...

    @typing.overload
    def __init__(self, binder: Microsoft.Scripting.Actions.ActionBinder, args: System.Collections.Generic.IList[System.Dynamic.DynamicMetaObject], signature: Microsoft.Scripting.Actions.CallSignature, callType: int, ):
        ...

    def MapSpecialParameters(self, mapping: Microsoft.Scripting.Actions.Calls.ParameterMapping, ) -> System.Collections.BitArray:
        ...

    def CompareEquivalentCandidates(self, one: Microsoft.Scripting.Actions.Calls.ApplicableCandidate, two: Microsoft.Scripting.Actions.Calls.ApplicableCandidate, ) -> int:
        ...

    def GetArgument(self, i: int, ) -> System.Dynamic.DynamicMetaObject:
        ...

    def GetNamedArguments(self, namedArgs: ref[System.Collections.Generic.IList[System.Dynamic.DynamicMetaObject]], argNames: ref[System.Collections.Generic.IList[str]], ) -> None:
        ...

    def AllowByKeywordArgument(self, method: Microsoft.Scripting.Actions.Calls.OverloadInfo, parameter: System.Reflection.ParameterInfo, ) -> bool:
        ...

    def CreateActualArguments(self, namedArgs: System.Collections.Generic.IList[System.Dynamic.DynamicMetaObject], argNames: System.Collections.Generic.IList[str], preSplatLimit: int, postSplatLimit: int, ) -> Microsoft.Scripting.Actions.Calls.ActualArguments:
        ...

    def SplatDictionaryArgument(self, splattedNames: System.Collections.Generic.IList[str], splattedArgs: System.Collections.Generic.IList[System.Dynamic.DynamicMetaObject], ) -> None:
        ...

    def GetSplattedExpression(self, ) -> System.Linq.Expressions.Expression:
        ...

    def GetSplattedItem(self, index: int, ) -> System.Object:
        ...

    def MakeInvalidParametersError(self, target: Microsoft.Scripting.Actions.Calls.BindingTarget, ) -> Microsoft.Scripting.Actions.ErrorInfo:
        ...

    def MakeInvalidSplatteeError(self, target: Microsoft.Scripting.Actions.Calls.BindingTarget, ) -> Microsoft.Scripting.Actions.ErrorInfo:
        ...

class MethodTracker(Microsoft.Scripting.Actions.MemberTracker):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def DeclaringType(self) -> System.Type:
        ...

    @property
    def MemberType(self) -> int:
        ...

    @property
    def Name(self) -> str:
        ...

    @property
    def Method(self) -> System.Reflection.MethodInfo:
        ...

    @property
    def IsPublic(self) -> bool:
        ...

    @property
    def IsStatic(self) -> bool:
        ...

    # methods
    @typing.overload
    def __init__(self, method: System.Reflection.MethodInfo, ):
        ...

    @typing.overload
    def __init__(self, method: System.Reflection.MethodInfo, isStatic: bool, ):
        ...

    def ToString(self, ) -> str:
        ...

    def BindToInstance(self, instance: System.Dynamic.DynamicMetaObject, ) -> Microsoft.Scripting.Actions.MemberTracker:
        ...

    def GetBoundValue(self, resolverFactory: Microsoft.Scripting.Actions.Calls.OverloadResolverFactory, binder: Microsoft.Scripting.Actions.ActionBinder, type: System.Type, instance: System.Dynamic.DynamicMetaObject, ) -> System.Dynamic.DynamicMetaObject:
        ...

    def Call(self, resolverFactory: Microsoft.Scripting.Actions.Calls.OverloadResolverFactory, binder: Microsoft.Scripting.Actions.ActionBinder, arguments: System.Array[System.Dynamic.DynamicMetaObject], ) -> System.Dynamic.DynamicMetaObject:
        ...

class MethodGroup(Microsoft.Scripting.Actions.MemberTracker):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def MemberType(self) -> int:
        ...

    @property
    def DeclaringType(self) -> System.Type:
        ...

    @property
    def Name(self) -> str:
        ...

    @property
    def ContainsInstance(self) -> bool:
        ...

    @property
    def ContainsStatic(self) -> bool:
        ...

    @property
    def Methods(self) -> System.Collections.Generic.IList[Microsoft.Scripting.Actions.MethodTracker]:
        ...

    # methods
    def __init__(self, methods: System.Array[Microsoft.Scripting.Actions.MethodTracker], ):
        ...

    def GetMethodBases(self, ) -> System.Array[System.Reflection.MethodBase]:
        ...

    def BindToInstance(self, instance: System.Dynamic.DynamicMetaObject, ) -> Microsoft.Scripting.Actions.MemberTracker:
        ...

    def GetBoundValue(self, resolverFactory: Microsoft.Scripting.Actions.Calls.OverloadResolverFactory, binder: Microsoft.Scripting.Actions.ActionBinder, type: System.Type, instance: System.Dynamic.DynamicMetaObject, ) -> System.Dynamic.DynamicMetaObject:
        ...

    def MakeGenericMethod(self, types: System.Array[System.Type], ) -> Microsoft.Scripting.Actions.MethodGroup:
        ...

    def EnsureBoundGenericDict(self, ) -> None:
        ...

class BoundMemberTracker(Microsoft.Scripting.Actions.MemberTracker):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def MemberType(self) -> int:
        ...

    @property
    def DeclaringType(self) -> System.Type:
        ...

    @property
    def Name(self) -> str:
        ...

    @property
    def Instance(self) -> System.Dynamic.DynamicMetaObject:
        ...

    @property
    def ObjectInstance(self) -> System.Object:
        ...

    @property
    def BoundTo(self) -> Microsoft.Scripting.Actions.MemberTracker:
        ...

    # methods
    @typing.overload
    def __init__(self, tracker: Microsoft.Scripting.Actions.MemberTracker, instance: System.Dynamic.DynamicMetaObject, ):
        ...

    @typing.overload
    def __init__(self, tracker: Microsoft.Scripting.Actions.MemberTracker, instance: System.Object, ):
        ...

    def GetValue(self, resolverFactory: Microsoft.Scripting.Actions.Calls.OverloadResolverFactory, binder: Microsoft.Scripting.Actions.ActionBinder, instanceType: System.Type, ) -> System.Dynamic.DynamicMetaObject:
        ...

    def GetError(self, binder: Microsoft.Scripting.Actions.ActionBinder, instanceType: System.Type, ) -> Microsoft.Scripting.Actions.ErrorInfo:
        ...

    @typing.overload
    def SetValue(self, resolverFactory: Microsoft.Scripting.Actions.Calls.OverloadResolverFactory, binder: Microsoft.Scripting.Actions.ActionBinder, instanceType: System.Type, value: System.Dynamic.DynamicMetaObject, ) -> System.Dynamic.DynamicMetaObject:
        ...

    @typing.overload
    def SetValue(self, resolverFactory: Microsoft.Scripting.Actions.Calls.OverloadResolverFactory, binder: Microsoft.Scripting.Actions.ActionBinder, instanceType: System.Type, value: System.Dynamic.DynamicMetaObject, errorSuggestion: System.Dynamic.DynamicMetaObject, ) -> System.Dynamic.DynamicMetaObject:
        ...

class TypeTracker(Microsoft.Scripting.Runtime.IMembersList, Microsoft.Scripting.Actions.MemberTracker, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    @abc.abstractmethod
    def Type(self) -> System.Type:
        ...

    @property
    @abc.abstractmethod
    def IsGenericType(self) -> bool:
        ...

    @property
    @abc.abstractmethod
    def IsPublic(self) -> bool:
        ...

    @property
    @abc.abstractmethod
    def MemberType(self) -> int:
        ...

    @property
    @abc.abstractmethod
    def DeclaringType(self) -> System.Type:
        ...

    @property
    @abc.abstractmethod
    def Name(self) -> str:
        ...

    # methods
    def __init__(self, ):
        ...

    @typing.overload
    def GetMemberNames(self, ) -> System.Collections.Generic.IList[str]:
        ...

    @staticmethod
    @typing.overload
    def GetMemberNames(type: System.Type, result: System.Collections.Generic.HashSet[str], ) -> None:
        ...

    @staticmethod
    def GetTypeTracker(type: System.Type, ) -> Microsoft.Scripting.Actions.TypeTracker:
        ...

class Argument(System.IEquatable[Microsoft.Scripting.Actions.Argument], System.ValueType):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields
    Simple: Microsoft.Scripting.Actions.Argument = ...

    # properties
    @property
    def Kind(self) -> int:
        ...

    @property
    def Name(self) -> str:
        ...

    @property
    def IsSimple(self) -> bool:
        ...

    # methods
    @typing.overload
    def __init__(self, name: str, ):
        ...

    @typing.overload
    def __init__(self, kind: int, ):
        ...

    @typing.overload
    def __init__(self, kind: int, name: str, ):
        ...

    @typing.overload
    def Equals(self, obj: System.Object, ) -> bool:
        ...

    @typing.overload
    def Equals(self, other: Microsoft.Scripting.Actions.Argument, ) -> bool:
        ...

    def GetHashCode(self, ) -> int:
        ...

    def ToString(self, ) -> str:
        ...

    def CreateExpression(self, ) -> System.Linq.Expressions.Expression:
        ...

class ArgumentType(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    Simple: int = ...
    Named: int = ...
    List: int = ...
    Dictionary: int = ...
    Instance: int = ...

class CustomTracker(Microsoft.Scripting.Actions.MemberTracker, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def MemberType(self) -> int:
        ...

    @property
    @abc.abstractmethod
    def DeclaringType(self) -> System.Type:
        ...

    @property
    @abc.abstractmethod
    def Name(self) -> str:
        ...

    # methods
    def __init__(self, ):
        ...

class FieldTracker(Microsoft.Scripting.Actions.MemberTracker):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def DeclaringType(self) -> System.Type:
        ...

    @property
    def MemberType(self) -> int:
        ...

    @property
    def Name(self) -> str:
        ...

    @property
    def IsPublic(self) -> bool:
        ...

    @property
    def IsInitOnly(self) -> bool:
        ...

    @property
    def IsLiteral(self) -> bool:
        ...

    @property
    def FieldType(self) -> System.Type:
        ...

    @property
    def IsStatic(self) -> bool:
        ...

    @property
    def Field(self) -> System.Reflection.FieldInfo:
        ...

    # methods
    def __init__(self, field: System.Reflection.FieldInfo, ):
        ...

    def ToString(self, ) -> str:
        ...

    def GetValue(self, resolverFactory: Microsoft.Scripting.Actions.Calls.OverloadResolverFactory, binder: Microsoft.Scripting.Actions.ActionBinder, type: System.Type, ) -> System.Dynamic.DynamicMetaObject:
        ...

    def GetError(self, binder: Microsoft.Scripting.Actions.ActionBinder, instanceType: System.Type, ) -> Microsoft.Scripting.Actions.ErrorInfo:
        ...

    def GetBoundValue(self, resolverFactory: Microsoft.Scripting.Actions.Calls.OverloadResolverFactory, binder: Microsoft.Scripting.Actions.ActionBinder, type: System.Type, instance: System.Dynamic.DynamicMetaObject, ) -> System.Dynamic.DynamicMetaObject:
        ...

    def BindToInstance(self, instance: System.Dynamic.DynamicMetaObject, ) -> Microsoft.Scripting.Actions.MemberTracker:
        ...

class ConversionResultKind(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    ImplicitCast: int = ...
    ExplicitCast: int = ...
    ImplicitTry: int = ...
    ExplicitTry: int = ...

