from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import System
import System.Reflection
import Microsoft.Scripting.Actions.Calls
import System.Collections.Generic
import System.Linq.Expressions
import System.Dynamic
import System.Collections
import Microsoft.Scripting.Actions


class Candidate(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    Equivalent: int = ...
    One: int = ...
    Ambiguous: int = ...
    Two: int = ...

class BindingTarget(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def Result(self) -> int:
        ...

    @property
    def Method(self) -> System.Reflection.MethodBase:
        ...

    @property
    def Overload(self) -> Microsoft.Scripting.Actions.Calls.OverloadInfo:
        ...

    @property
    def Name(self) -> str:
        ...

    @property
    def MethodCandidate(self) -> Microsoft.Scripting.Actions.Calls.MethodCandidate:
        ...

    @property
    def AmbiguousMatches(self) -> System.Collections.Generic.IEnumerable[Microsoft.Scripting.Actions.Calls.MethodCandidate]:
        ...

    @property
    def CallFailures(self) -> System.Collections.Generic.ICollection[Microsoft.Scripting.Actions.Calls.CallFailure]:
        ...

    @property
    def ExpectedArgumentCount(self) -> System.Collections.Generic.IList[int]:
        ...

    @property
    def ActualArgumentCount(self) -> int:
        ...

    @property
    def RestrictedArguments(self) -> Microsoft.Scripting.Actions.Calls.RestrictedArguments:
        ...

    @property
    def ReturnType(self) -> System.Type:
        ...

    @property
    def NarrowingLevel(self) -> int:
        ...

    @property
    def Success(self) -> bool:
        ...

    # methods
    @typing.overload
    def __init__(self, name: str, actualArgumentCount: int, candidate: Microsoft.Scripting.Actions.Calls.MethodCandidate, level: int, restrictedArgs: Microsoft.Scripting.Actions.Calls.RestrictedArguments, ):
        ...

    @typing.overload
    def __init__(self, name: str, actualArgumentCount: int, expectedArgCount: System.Array[int], ):
        ...

    @typing.overload
    def __init__(self, name: str, actualArgumentCount: int, failures: System.Array[Microsoft.Scripting.Actions.Calls.CallFailure], ):
        ...

    @typing.overload
    def __init__(self, name: str, actualArgumentCount: int, ambiguousMatches: System.Array[Microsoft.Scripting.Actions.Calls.MethodCandidate], ):
        ...

    @typing.overload
    def __init__(self, name: str, result: int, ):
        ...

    def MakeExpression(self, ) -> System.Linq.Expressions.Expression:
        ...

class BindingResult(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    Success: int = ...
    AmbiguousMatch: int = ...
    IncorrectArgumentCount: int = ...
    CallFailure: int = ...
    InvalidArguments: int = ...
    NoCallableMethod: int = ...

class NarrowingLevel(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    None_: int = ...
    One: int = ...
    Two: int = ...
    Three: int = ...
    All: int = ...

class RestrictedArguments(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def Length(self) -> int:
        ...

    @property
    def HasUntypedRestrictions(self) -> bool:
        ...

    # methods
    def __init__(self, objects: System.Array[System.Dynamic.DynamicMetaObject], types: System.Array[System.Type], hasUntypedRestrictions: bool, ):
        ...

    def GetObject(self, i: int, ) -> System.Dynamic.DynamicMetaObject:
        ...

    def GetType(self, i: int, ) -> System.Type:
        ...

    def GetAllRestrictions(self, ) -> System.Dynamic.BindingRestrictions:
        ...

    def GetObjects(self, ) -> System.Collections.Generic.IList[System.Dynamic.DynamicMetaObject]:
        ...

    def GetTypes(self, ) -> System.Collections.Generic.IList[System.Type]:
        ...

class OverloadInfo(System.Object, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    @abc.abstractmethod
    def Name(self) -> str:
        ...

    @property
    @abc.abstractmethod
    def Parameters(self) -> System.Collections.Generic.IList[System.Reflection.ParameterInfo]:
        ...

    @property
    def ParameterCount(self) -> int:
        ...

    @property
    @abc.abstractmethod
    def ReturnParameter(self) -> System.Reflection.ParameterInfo:
        ...

    @property
    @abc.abstractmethod
    def DeclaringType(self) -> System.Type:
        ...

    @property
    @abc.abstractmethod
    def ReturnType(self) -> System.Type:
        ...

    @property
    @abc.abstractmethod
    def Attributes(self) -> int:
        ...

    @property
    @abc.abstractmethod
    def IsConstructor(self) -> bool:
        ...

    @property
    @abc.abstractmethod
    def IsExtension(self) -> bool:
        ...

    @property
    @abc.abstractmethod
    def IsVariadic(self) -> bool:
        ...

    @property
    @abc.abstractmethod
    def IsGenericMethodDefinition(self) -> bool:
        ...

    @property
    @abc.abstractmethod
    def IsGenericMethod(self) -> bool:
        ...

    @property
    @abc.abstractmethod
    def ContainsGenericParameters(self) -> bool:
        ...

    @property
    @abc.abstractmethod
    def GenericArguments(self) -> System.Collections.Generic.IList[System.Type]:
        ...

    @property
    def CallingConvention(self) -> int:
        ...

    @property
    def ReflectionInfo(self) -> System.Reflection.MethodBase:
        ...

    @property
    def IsInstanceFactory(self) -> bool:
        ...

    @property
    def IsPrivate(self) -> bool:
        ...

    @property
    def IsPublic(self) -> bool:
        ...

    @property
    def IsAssembly(self) -> bool:
        ...

    @property
    def IsFamily(self) -> bool:
        ...

    @property
    def IsFamilyOrAssembly(self) -> bool:
        ...

    @property
    def IsFamilyAndAssembly(self) -> bool:
        ...

    @property
    def IsProtected(self) -> bool:
        ...

    @property
    def IsStatic(self) -> bool:
        ...

    @property
    def IsVirtual(self) -> bool:
        ...

    @property
    def IsSpecialName(self) -> bool:
        ...

    @property
    def IsFinal(self) -> bool:
        ...

    # methods
    def __init__(self, ):
        ...

    def ProhibitsNull(self, parameterIndex: int, ) -> bool:
        ...

    def ProhibitsNullItems(self, parameterIndex: int, ) -> bool:
        ...

    def IsParamArray(self, parameterIndex: int, ) -> bool:
        ...

    def IsParamDictionary(self, parameterIndex: int, ) -> bool:
        ...

    @abc.abstractmethod
    def MakeGenericMethod(self, genericArguments: System.Array[System.Type], ) -> Microsoft.Scripting.Actions.Calls.OverloadInfo:
        ...

class CallFailure(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def Candidate(self) -> Microsoft.Scripting.Actions.Calls.MethodCandidate:
        ...

    @property
    def Reason(self) -> int:
        ...

    @property
    def ConversionResults(self) -> System.Collections.Generic.IList[Microsoft.Scripting.Actions.Calls.ConversionResult]:
        ...

    @property
    def KeywordArguments(self) -> System.Collections.Generic.IList[str]:
        ...

    @property
    def PositionalArguments(self) -> System.Collections.Generic.IList[int]:
        ...

    # methods
    @typing.overload
    def __init__(self, candidate: Microsoft.Scripting.Actions.Calls.MethodCandidate, results: System.Array[Microsoft.Scripting.Actions.Calls.ConversionResult], ):
        ...

    @typing.overload
    def __init__(self, candidate: Microsoft.Scripting.Actions.Calls.MethodCandidate, keywordArgs: System.Array[str], ):
        ...

    @typing.overload
    def __init__(self, candidate: Microsoft.Scripting.Actions.Calls.MethodCandidate, keywordArgs: System.Array[str], positionalArgs: System.Array[int], ):
        ...

    @typing.overload
    def __init__(self, candidate: Microsoft.Scripting.Actions.Calls.MethodCandidate, reason: int, ):
        ...

class CallFailureReason(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    None_: int = ...
    ConversionFailure: int = ...
    UnassignableKeyword: int = ...
    DuplicateKeyword: int = ...
    TypeInference: int = ...

class ApplicableCandidate(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        self.Method: Microsoft.Scripting.Actions.Calls.MethodCandidate
        self.ArgumentBinding: Microsoft.Scripting.Actions.Calls.ArgumentBinding
        ...

    # static fields

    # properties
    # methods
    def __init__(self, method: Microsoft.Scripting.Actions.Calls.MethodCandidate, argBinding: Microsoft.Scripting.Actions.Calls.ArgumentBinding, ):
        ...

    def GetParameter(self, argumentIndex: int, ) -> Microsoft.Scripting.Actions.Calls.ParameterWrapper:
        ...

    def ToString(self, ) -> str:
        ...

class ParameterMapping(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def Overload(self) -> Microsoft.Scripting.Actions.Calls.OverloadInfo:
        ...

    @property
    def ArgIndex(self) -> int:
        ...
    @ArgIndex.setter
    def ArgIndex(self, val: int):
        ...

    @property
    def Method(self) -> System.Reflection.MethodBase:
        ...

    @property
    def ParameterInfos(self) -> System.Array[System.Reflection.ParameterInfo]:
        ...

    # methods
    def __init__(self, resolver: Microsoft.Scripting.Actions.Calls.OverloadResolver, method: Microsoft.Scripting.Actions.Calls.OverloadInfo, argNames: System.Collections.Generic.IList[str], ):
        ...

    def MapParameters(self, reduceByRef: bool, ) -> None:
        ...

    def IsSpecialParameter(self, specialParameters: System.Collections.BitArray, infoIndex: int, ) -> bool:
        ...

    def AddInstanceBuilder(self, builder: Microsoft.Scripting.Actions.Calls.InstanceBuilder, ) -> None:
        ...

    def AddBuilder(self, builder: Microsoft.Scripting.Actions.Calls.ArgBuilder, ) -> None:
        ...

    def AddParameter(self, parameter: Microsoft.Scripting.Actions.Calls.ParameterWrapper, ) -> None:
        ...

    def MapParameter(self, pi: System.Reflection.ParameterInfo, ) -> None:
        ...

    def MapParameterReduceByRef(self, pi: System.Reflection.ParameterInfo, ) -> None:
        ...

    def CreateParameterWrapper(self, info: System.Reflection.ParameterInfo, ) -> Microsoft.Scripting.Actions.Calls.ParameterWrapper:
        ...

    def AddSimpleParameterMapping(self, info: System.Reflection.ParameterInfo, index: int, ) -> Microsoft.Scripting.Actions.Calls.SimpleArgBuilder:
        ...

    def CreateCandidate(self, ) -> Microsoft.Scripting.Actions.Calls.MethodCandidate:
        ...

    def CreateByRefReducedCandidate(self, ) -> Microsoft.Scripting.Actions.Calls.MethodCandidate:
        ...

    def CreateDefaultCandidates(self, ) -> System.Collections.Generic.IEnumerable[Microsoft.Scripting.Actions.Calls.MethodCandidate]:
        ...

    def CreateDefaultCandidate(self, defaultsUsed: int, ) -> Microsoft.Scripting.Actions.Calls.MethodCandidate:
        ...

    def MakeReturnBuilder(self, specialParameters: System.Collections.BitArray, ) -> Microsoft.Scripting.Actions.Calls.ReturnBuilder:
        ...

    @staticmethod
    def GetBindableMembers(returnType: System.Type, unusedNames: System.Collections.Generic.List[str], ) -> System.Collections.Generic.List[System.Reflection.MemberInfo]:
        ...

    def GetUnusedArgNames(self, specialParameters: System.Collections.BitArray, ) -> System.Collections.Generic.List[str]:
        ...

class InstanceBuilder(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def HasValue(self) -> bool:
        ...

    @property
    def ConsumedArgumentCount(self) -> int:
        ...

    # methods
    def __init__(self, index: int, ):
        ...

    def ToExpression(self, method: ref[System.Reflection.MethodInfo], resolver: Microsoft.Scripting.Actions.Calls.OverloadResolver, args: Microsoft.Scripting.Actions.Calls.RestrictedArguments, hasBeenUsed: System.Array[bool], ) -> System.Linq.Expressions.Expression:
        ...

    def GetCallableMethod(self, args: Microsoft.Scripting.Actions.Calls.RestrictedArguments, method: ref[System.Reflection.MethodInfo], ) -> None:
        ...

class SimpleArgBuilder(Microsoft.Scripting.Actions.Calls.ArgBuilder):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def ConsumedArgumentCount(self) -> int:
        ...

    @property
    def Priority(self) -> int:
        ...

    @property
    def IsParamsArray(self) -> bool:
        ...

    @property
    def IsParamsDict(self) -> bool:
        ...

    @property
    def Index(self) -> int:
        ...

    @property
    def Type(self) -> System.Type:
        ...

    @property
    def ParameterInfo(self) -> System.Reflection.ParameterInfo:
        ...

    @property
    def ByRefArgument(self) -> System.Linq.Expressions.Expression:
        ...

    # methods
    @typing.overload
    def __init__(self, parameterType: System.Type, index: int, isParams: bool, isParamsDict: bool, ):
        ...

    @typing.overload
    def __init__(self, info: System.Reflection.ParameterInfo, index: int, ):
        ...

    @typing.overload
    def __init__(self, info: System.Reflection.ParameterInfo, parameterType: System.Type, index: int, isParams: bool, isParamsDict: bool, ):
        ...

    def MakeCopy(self, newIndex: int, ) -> Microsoft.Scripting.Actions.Calls.SimpleArgBuilder:
        ...

    def Copy(self, newIndex: int, ) -> Microsoft.Scripting.Actions.Calls.SimpleArgBuilder:
        ...

    def ToExpression(self, resolver: Microsoft.Scripting.Actions.Calls.OverloadResolver, args: Microsoft.Scripting.Actions.Calls.RestrictedArguments, hasBeenUsed: System.Array[bool], ) -> System.Linq.Expressions.Expression:
        ...

    def Clone(self, newType: System.Reflection.ParameterInfo, ) -> Microsoft.Scripting.Actions.Calls.ArgBuilder:
        ...

class ActualArguments(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def CollapsedCount(self) -> int:
        ...

    @property
    def SplatIndex(self) -> int:
        ...

    @property
    def FirstSplattedArg(self) -> int:
        ...

    @property
    def ArgNames(self) -> System.Collections.Generic.IList[str]:
        ...

    @property
    def NamedArguments(self) -> System.Collections.Generic.IList[System.Dynamic.DynamicMetaObject]:
        ...

    @property
    def Arguments(self) -> System.Collections.Generic.IList[System.Dynamic.DynamicMetaObject]:
        ...

    @property
    def Count(self) -> int:
        ...

    @property
    def HiddenCount(self) -> int:
        ...

    @property
    def VisibleCount(self) -> int:
        ...

    @property
    def Item(self) -> System.Dynamic.DynamicMetaObject:
        ...

    # methods
    def __init__(self, args: System.Collections.Generic.IList[System.Dynamic.DynamicMetaObject], namedArgs: System.Collections.Generic.IList[System.Dynamic.DynamicMetaObject], argNames: System.Collections.Generic.IList[str], hiddenCount: int, collapsedCount: int, firstSplattedArg: int, splatIndex: int, ):
        ...

    def ToSplattedItemIndex(self, collapsedArgIndex: int, ) -> int:
        ...

    def TryBindNamedArguments(self, method: Microsoft.Scripting.Actions.Calls.MethodCandidate, binding: ref[Microsoft.Scripting.Actions.Calls.ArgumentBinding], failure: ref[Microsoft.Scripting.Actions.Calls.CallFailure], ) -> bool:
        ...

class MethodCandidate(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def ReturnBuilder(self) -> Microsoft.Scripting.Actions.Calls.ReturnBuilder:
        ...

    @property
    def ArgBuilders(self) -> System.Collections.Generic.IList[Microsoft.Scripting.Actions.Calls.ArgBuilder]:
        ...

    @property
    def Resolver(self) -> Microsoft.Scripting.Actions.Calls.OverloadResolver:
        ...

    @property
    def Method(self) -> System.Reflection.MethodBase:
        ...

    @property
    def Overload(self) -> Microsoft.Scripting.Actions.Calls.OverloadInfo:
        ...

    @property
    def Restrictions(self) -> System.Collections.Generic.Dictionary[System.Dynamic.DynamicMetaObject, System.Dynamic.BindingRestrictions]:
        ...

    @property
    def ReturnType(self) -> System.Type:
        ...

    @property
    def ParamsArrayIndex(self) -> int:
        ...

    @property
    def HasParamsArray(self) -> bool:
        ...

    @property
    def HasParamsDictionary(self) -> bool:
        ...

    @property
    def Binder(self) -> Microsoft.Scripting.Actions.ActionBinder:
        ...

    @property
    def ParameterCount(self) -> int:
        ...

    # methods
    def __init__(self, resolver: Microsoft.Scripting.Actions.Calls.OverloadResolver, method: Microsoft.Scripting.Actions.Calls.OverloadInfo, parameters: System.Collections.Generic.List[Microsoft.Scripting.Actions.Calls.ParameterWrapper], paramsDict: Microsoft.Scripting.Actions.Calls.ParameterWrapper, returnBuilder: Microsoft.Scripting.Actions.Calls.ReturnBuilder, instanceBuilder: Microsoft.Scripting.Actions.Calls.InstanceBuilder, argBuilders: System.Collections.Generic.IList[Microsoft.Scripting.Actions.Calls.ArgBuilder], restrictions: System.Collections.Generic.Dictionary[System.Dynamic.DynamicMetaObject, System.Dynamic.BindingRestrictions], ):
        ...

    def ReplaceMethod(self, newMethod: Microsoft.Scripting.Actions.Calls.OverloadInfo, parameters: System.Collections.Generic.List[Microsoft.Scripting.Actions.Calls.ParameterWrapper], argBuilders: System.Collections.Generic.IList[Microsoft.Scripting.Actions.Calls.ArgBuilder], restrictions: System.Collections.Generic.Dictionary[System.Dynamic.DynamicMetaObject, System.Dynamic.BindingRestrictions], ) -> Microsoft.Scripting.Actions.Calls.MethodCandidate:
        ...

    @typing.overload
    def GetParameter(self, argumentIndex: int, namesBinding: Microsoft.Scripting.Actions.Calls.ArgumentBinding, ) -> Microsoft.Scripting.Actions.Calls.ParameterWrapper:
        ...

    @typing.overload
    def GetParameter(self, parameterIndex: int, ) -> Microsoft.Scripting.Actions.Calls.ParameterWrapper:
        ...

    def IndexOfParameter(self, name: str, ) -> int:
        ...

    def PositionOfParameter(self, name: str, ) -> int:
        ...

    def GetVisibleParameterCount(self, ) -> int:
        ...

    def GetParameters(self, ) -> System.Collections.Generic.IList[Microsoft.Scripting.Actions.Calls.ParameterWrapper]:
        ...

    @typing.overload
    def MakeParamsExtended(self, count: int, names: System.Collections.Generic.IList[str], ) -> Microsoft.Scripting.Actions.Calls.MethodCandidate:
        ...

    @typing.overload
    def MakeParamsExtended(self, names: System.Array[str], nameIndices: System.Array[int], parameters: System.Collections.Generic.List[Microsoft.Scripting.Actions.Calls.ParameterWrapper], ) -> Microsoft.Scripting.Actions.Calls.MethodCandidate:
        ...

    def GetConsumedArguments(self, ) -> int:
        ...

    def GetParameterTypes(self, ) -> System.Array[System.Type]:
        ...

    def MakeExpression(self, restrictedArgs: Microsoft.Scripting.Actions.Calls.RestrictedArguments, ) -> System.Linq.Expressions.Expression:
        ...

    def GetArgumentExpressions(self, restrictedArgs: Microsoft.Scripting.Actions.Calls.RestrictedArguments, usageMarkers: ref[System.Array[bool]], spilledArgs: ref[System.Array[System.Linq.Expressions.Expression]], ) -> System.Array[System.Linq.Expressions.Expression]:
        ...

    @staticmethod
    def RemoveNulls(args: System.Array[System.Linq.Expressions.Expression], ) -> System.Array[System.Linq.Expressions.Expression]:
        ...

    def ToString(self, ) -> str:
        ...

class ConversionResult(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def Arg(self) -> System.Object:
        ...

    @property
    def ArgType(self) -> System.Type:
        ...

    @property
    def To(self) -> System.Type:
        ...

    @property
    def Failed(self) -> bool:
        ...

    # methods
    def __init__(self, arg: System.Object, argType: System.Type, toType: System.Type, failed: bool, ):
        ...

    @staticmethod
    def ReplaceLastFailure(failures: System.Collections.Generic.IList[Microsoft.Scripting.Actions.Calls.ConversionResult], isFailure: bool, ) -> None:
        ...

    def GetArgumentTypeName(self, binder: Microsoft.Scripting.Actions.ActionBinder, ) -> str:
        ...

class ParameterWrapper(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def Type(self) -> System.Type:
        ...

    @property
    def ParameterInfo(self) -> System.Reflection.ParameterInfo:
        ...

    @property
    def Name(self) -> str:
        ...

    @property
    def Flags(self) -> int:
        ...

    @property
    def ProhibitNull(self) -> bool:
        ...

    @property
    def ProhibitNullItems(self) -> bool:
        ...

    @property
    def IsHidden(self) -> bool:
        ...

    @property
    def IsByRef(self) -> bool:
        ...

    @property
    def IsParamsArray(self) -> bool:
        ...

    @property
    def IsParamsDict(self) -> bool:
        ...

    # methods
    @typing.overload
    def __init__(self, type: System.Type, name: str, prohibitNull: bool, ):
        ...

    @typing.overload
    def __init__(self, info: System.Reflection.ParameterInfo, type: System.Type, name: str, prohibitNull: bool, isParams: bool, isParamsDict: bool, isHidden: bool, ):
        ...

    @typing.overload
    def __init__(self, info: System.Reflection.ParameterInfo, type: System.Type, name: str, flags: int, ):
        ...

    def Clone(self, name: str, ) -> Microsoft.Scripting.Actions.Calls.ParameterWrapper:
        ...

    @staticmethod
    def IndexOfParamsArray(parameters: System.Collections.Generic.IList[Microsoft.Scripting.Actions.Calls.ParameterWrapper], ) -> int:
        ...

    def Expand(self, ) -> Microsoft.Scripting.Actions.Calls.ParameterWrapper:
        ...

class ParameterBindingFlags(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    None_: int = ...
    ProhibitNull: int = ...
    ProhibitNullItems: int = ...
    IsParamArray: int = ...
    IsParamDictionary: int = ...
    IsHidden: int = ...

class ArgBuilder(System.Object, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields
    AllArguments: int = ...

    # properties
    @property
    @abc.abstractmethod
    def Priority(self) -> int:
        ...

    @property
    def ParameterInfo(self) -> System.Reflection.ParameterInfo:
        ...

    @property
    @abc.abstractmethod
    def ConsumedArgumentCount(self) -> int:
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

    @abc.abstractmethod
    def ToExpression(self, resolver: Microsoft.Scripting.Actions.Calls.OverloadResolver, args: Microsoft.Scripting.Actions.Calls.RestrictedArguments, hasBeenUsed: System.Array[bool], ) -> System.Linq.Expressions.Expression:
        ...

    def UpdateFromReturn(self, resolver: Microsoft.Scripting.Actions.Calls.OverloadResolver, args: Microsoft.Scripting.Actions.Calls.RestrictedArguments, ) -> System.Linq.Expressions.Expression:
        ...

    def ToReturnExpression(self, resolver: Microsoft.Scripting.Actions.Calls.OverloadResolver, ) -> System.Linq.Expressions.Expression:
        ...

    def Clone(self, newType: System.Reflection.ParameterInfo, ) -> Microsoft.Scripting.Actions.Calls.ArgBuilder:
        ...

class ArgumentBinding(System.ValueType):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def PositionalArgCount(self) -> int:
        ...

    # methods
    @typing.overload
    def __init__(self, positionalArgCount: int, ):
        ...

    @typing.overload
    def __init__(self, positionalArgCount: int, binding: System.Array[int], ):
        ...

    def ArgumentToParameter(self, argumentIndex: int, ) -> int:
        ...

class OverloadResolver(System.Object, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
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
    def __init__(self, binder: Microsoft.Scripting.Actions.ActionBinder, ):
        ...

    def GetTemporary(self, type: System.Type, name: str, ) -> System.Linq.Expressions.ParameterExpression:
        ...

    @typing.overload
    def ResolveOverload(self, methodName: str, methods: System.Collections.Generic.IList[System.Reflection.MethodBase], minLevel: int, maxLevel: int, ) -> Microsoft.Scripting.Actions.Calls.BindingTarget:
        ...

    @typing.overload
    def ResolveOverload(self, methodName: str, methods: System.Collections.Generic.IList[Microsoft.Scripting.Actions.Calls.OverloadInfo], minLevel: int, maxLevel: int, ) -> Microsoft.Scripting.Actions.Calls.BindingTarget:
        ...

    def AllowMemberInitialization(self, method: Microsoft.Scripting.Actions.Calls.OverloadInfo, ) -> bool:
        ...

    def AllowKeywordArgumentSetting(self, method: System.Reflection.MethodBase, ) -> bool:
        ...

    def GetByRefArrayExpression(self, argumentArrayExpression: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.Expression:
        ...

    def BindToUnexpandedParams(self, candidate: Microsoft.Scripting.Actions.Calls.MethodCandidate, ) -> bool:
        ...

    def AllowByKeywordArgument(self, method: Microsoft.Scripting.Actions.Calls.OverloadInfo, parameter: System.Reflection.ParameterInfo, ) -> bool:
        ...

    def MapSpecialParameters(self, mapping: Microsoft.Scripting.Actions.Calls.ParameterMapping, ) -> System.Collections.BitArray:
        ...

    def BuildCandidateSets(self, methods: System.Collections.Generic.IEnumerable[Microsoft.Scripting.Actions.Calls.OverloadInfo], ) -> None:
        ...

    def GetCandidateSet(self, ) -> Microsoft.Scripting.Actions.Calls.CandidateSet:
        ...

    def BuildExpandedTargetSet(self, count: int, ) -> Microsoft.Scripting.Actions.Calls.CandidateSet:
        ...

    def AddTarget(self, target: Microsoft.Scripting.Actions.Calls.MethodCandidate, ) -> None:
        ...

    def AddSimpleTarget(self, target: Microsoft.Scripting.Actions.Calls.MethodCandidate, ) -> None:
        ...

    def AddBasicMethodTargets(self, method: Microsoft.Scripting.Actions.Calls.OverloadInfo, ) -> None:
        ...

    @staticmethod
    def IsUnsupported(method: Microsoft.Scripting.Actions.Calls.OverloadInfo, ) -> bool:
        ...

    def GetActualArguments(self, ) -> Microsoft.Scripting.Actions.Calls.ActualArguments:
        ...

    def GetNamedArguments(self, namedArgs: ref[System.Collections.Generic.IList[System.Dynamic.DynamicMetaObject]], argNames: ref[System.Collections.Generic.IList[str]], ) -> None:
        ...

    @abc.abstractmethod
    def CreateActualArguments(self, namedArgs: System.Collections.Generic.IList[System.Dynamic.DynamicMetaObject], argNames: System.Collections.Generic.IList[str], preSplatLimit: int, postSplatLimit: int, ) -> Microsoft.Scripting.Actions.Calls.ActualArguments:
        ...

    def MakeBindingTarget(self, targetSet: Microsoft.Scripting.Actions.Calls.CandidateSet, ) -> Microsoft.Scripting.Actions.Calls.BindingTarget:
        ...

    def EnsureMatchingNamedArgs(self, candidates: System.Collections.Generic.List[Microsoft.Scripting.Actions.Calls.MethodCandidate], failures: ref[System.Collections.Generic.List[Microsoft.Scripting.Actions.Calls.CallFailure]], ) -> System.Collections.Generic.List[Microsoft.Scripting.Actions.Calls.ApplicableCandidate]:
        ...

    def SelectCandidatesWithConvertibleArgs(self, candidates: System.Collections.Generic.List[Microsoft.Scripting.Actions.Calls.ApplicableCandidate], level: int, failures: ref[System.Collections.Generic.List[Microsoft.Scripting.Actions.Calls.CallFailure]], ) -> System.Collections.Generic.List[Microsoft.Scripting.Actions.Calls.ApplicableCandidate]:
        ...

    def SelectCandidatesWithConvertibleCollapsedArgs(self, candidates: System.Collections.Generic.List[Microsoft.Scripting.Actions.Calls.ApplicableCandidate], level: int, failures: ref[System.Collections.Generic.List[Microsoft.Scripting.Actions.Calls.CallFailure]], ) -> System.Collections.Generic.List[Microsoft.Scripting.Actions.Calls.ApplicableCandidate]:
        ...

    @staticmethod
    def AddFailure(failures: ref[System.Collections.Generic.List[Microsoft.Scripting.Actions.Calls.CallFailure]], failure: Microsoft.Scripting.Actions.Calls.CallFailure, ) -> None:
        ...

    def TryConvertArguments(self, candidate: Microsoft.Scripting.Actions.Calls.MethodCandidate, namesBinding: Microsoft.Scripting.Actions.Calls.ArgumentBinding, narrowingLevel: int, failure: ref[Microsoft.Scripting.Actions.Calls.CallFailure], ) -> bool:
        ...

    def TryConvertCollapsedArguments(self, candidate: Microsoft.Scripting.Actions.Calls.MethodCandidate, narrowingLevel: int, failure: ref[Microsoft.Scripting.Actions.Calls.CallFailure], ) -> bool:
        ...

    def GetRestrictedArgs(self, selectedCandidate: Microsoft.Scripting.Actions.Calls.ApplicableCandidate, candidates: System.Collections.Generic.IList[Microsoft.Scripting.Actions.Calls.ApplicableCandidate], targetSetSize: int, ) -> Microsoft.Scripting.Actions.Calls.RestrictedArguments:
        ...

    def RestrictArgument(self, arg: System.Dynamic.DynamicMetaObject, parameter: Microsoft.Scripting.Actions.Calls.ParameterWrapper, ) -> System.Dynamic.DynamicMetaObject:
        ...

    @staticmethod
    def IsOverloadedOnParameter(argIndex: int, argCount: int, overloads: System.Collections.Generic.IList[Microsoft.Scripting.Actions.Calls.ApplicableCandidate], ) -> bool:
        ...

    def IsBest(self, candidate: Microsoft.Scripting.Actions.Calls.ApplicableCandidate, candidates: System.Collections.Generic.List[Microsoft.Scripting.Actions.Calls.ApplicableCandidate], level: int, ) -> bool:
        ...

    def GetPreferredCandidate(self, one: Microsoft.Scripting.Actions.Calls.ApplicableCandidate, two: Microsoft.Scripting.Actions.Calls.ApplicableCandidate, level: int, ) -> int:
        ...

    def CompareEquivalentCandidates(self, one: Microsoft.Scripting.Actions.Calls.ApplicableCandidate, two: Microsoft.Scripting.Actions.Calls.ApplicableCandidate, ) -> int:
        ...

    def CompareEquivalentParameters(self, one: Microsoft.Scripting.Actions.Calls.MethodCandidate, two: Microsoft.Scripting.Actions.Calls.MethodCandidate, ) -> int:
        ...

    @staticmethod
    def Compare(x: int, y: int, ) -> int:
        ...

    @staticmethod
    def FindMaxPriority(abs: System.Collections.Generic.IList[Microsoft.Scripting.Actions.Calls.ArgBuilder], ceiling: int, ) -> int:
        ...

    def GetPreferredParameters(self, one: Microsoft.Scripting.Actions.Calls.ApplicableCandidate, two: Microsoft.Scripting.Actions.Calls.ApplicableCandidate, level: int, ) -> int:
        ...

    def GetPreferredParameter(self, candidateOne: Microsoft.Scripting.Actions.Calls.ParameterWrapper, candidateTwo: Microsoft.Scripting.Actions.Calls.ParameterWrapper, arg: System.Dynamic.DynamicMetaObject, level: int, ) -> int:
        ...

    def SelectBestCandidate(self, candidates: System.Collections.Generic.List[Microsoft.Scripting.Actions.Calls.ApplicableCandidate], level: int, ) -> Microsoft.Scripting.Actions.Calls.ApplicableCandidate:
        ...

    def MakeSuccessfulBindingTarget(self, result: Microsoft.Scripting.Actions.Calls.ApplicableCandidate, potentialCandidates: System.Collections.Generic.List[Microsoft.Scripting.Actions.Calls.ApplicableCandidate], level: int, targetSet: Microsoft.Scripting.Actions.Calls.CandidateSet, ) -> Microsoft.Scripting.Actions.Calls.BindingTarget:
        ...

    def MakeFailedBindingTarget(self, failures: System.Array[Microsoft.Scripting.Actions.Calls.CallFailure], ) -> Microsoft.Scripting.Actions.Calls.BindingTarget:
        ...

    def MakeAmbiguousBindingTarget(self, result: System.Collections.Generic.List[Microsoft.Scripting.Actions.Calls.ApplicableCandidate], ) -> Microsoft.Scripting.Actions.Calls.BindingTarget:
        ...

    def ParametersEquivalent(self, parameter1: Microsoft.Scripting.Actions.Calls.ParameterWrapper, parameter2: Microsoft.Scripting.Actions.Calls.ParameterWrapper, ) -> bool:
        ...

    @typing.overload
    def CanConvertFrom(self, parameter1: Microsoft.Scripting.Actions.Calls.ParameterWrapper, parameter2: Microsoft.Scripting.Actions.Calls.ParameterWrapper, ) -> bool:
        ...

    @typing.overload
    def CanConvertFrom(self, fromType: System.Type, fromArgument: System.Dynamic.DynamicMetaObject, toParameter: Microsoft.Scripting.Actions.Calls.ParameterWrapper, level: int, ) -> bool:
        ...

    def SelectBestConversionFor(self, arg: System.Dynamic.DynamicMetaObject, candidateOne: Microsoft.Scripting.Actions.Calls.ParameterWrapper, candidateTwo: Microsoft.Scripting.Actions.Calls.ParameterWrapper, level: int, ) -> int:
        ...

    def PreferConvert(self, t1: System.Type, t2: System.Type, ) -> int:
        ...

    def Convert(self, metaObject: System.Dynamic.DynamicMetaObject, restrictedType: System.Type, info: System.Reflection.ParameterInfo, toType: System.Type, ) -> System.Linq.Expressions.Expression:
        ...

    def GetDynamicConversion(self, value: System.Linq.Expressions.Expression, type: System.Type, ) -> System.Linq.Expressions.Expression:
        ...

    def GetExpectedArgCounts(self, ) -> System.Array[int]:
        ...

    def MakeInvalidParametersError(self, target: Microsoft.Scripting.Actions.Calls.BindingTarget, ) -> Microsoft.Scripting.Actions.ErrorInfo:
        ...

    @staticmethod
    def MakeIncorrectArgumentCountError(target: Microsoft.Scripting.Actions.Calls.BindingTarget, ) -> Microsoft.Scripting.Actions.ErrorInfo:
        ...

    def MakeAmbiguousCallError(self, target: Microsoft.Scripting.Actions.Calls.BindingTarget, ) -> Microsoft.Scripting.Actions.ErrorInfo:
        ...

    def MakeCallFailureError(self, target: Microsoft.Scripting.Actions.Calls.BindingTarget, ) -> Microsoft.Scripting.Actions.ErrorInfo:
        ...

    def MakeInvalidArgumentsError(self, ) -> Microsoft.Scripting.Actions.ErrorInfo:
        ...

    def MakeNoCallableMethodError(self, ) -> Microsoft.Scripting.Actions.ErrorInfo:
        ...

    def GetSplatLimits(self, preSplatLimit: ref[int], postSplatLimit: ref[int], ) -> None:
        ...

    def GetSplattedItemExpression(self, indexExpression: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.Expression:
        ...

    @abc.abstractmethod
    def GetSplattedExpression(self, ) -> System.Linq.Expressions.Expression:
        ...

    @abc.abstractmethod
    def GetSplattedItem(self, index: int, ) -> System.Object:
        ...

    def GetCollapsedArgumentValue(self, collapsedArgIndex: int, ) -> System.Object:
        ...

    def GetAccessedCollapsedArgTypes(self, ) -> System.Array[System.Type]:
        ...

    def GetCollapsedArgsCondition(self, ) -> System.Linq.Expressions.Expression:
        ...

    def GetGenericInferenceType(self, dynamicObject: System.Dynamic.DynamicMetaObject, ) -> System.Type:
        ...

    def ToString(self, ) -> str:
        ...

class OverloadResolverFactory(System.Object, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    def __init__(self, ):
        ...

    @abc.abstractmethod
    def CreateOverloadResolver(self, args: System.Collections.Generic.IList[System.Dynamic.DynamicMetaObject], signature: Microsoft.Scripting.Actions.CallSignature, callType: int, ) -> Microsoft.Scripting.Actions.DefaultOverloadResolver:
        ...

