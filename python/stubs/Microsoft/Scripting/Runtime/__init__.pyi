from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import System
import System.Reflection
import System.Collections.Generic
import System.Dynamic
import Microsoft.Scripting.Runtime
import System.Linq.Expressions
import System.Text
import Microsoft.Scripting
import System.IO
import System.CodeDom
import System.Runtime.CompilerServices
import Microsoft.Scripting.Utils

T = typing.TypeVar('T')
TService = typing.TypeVar('TService')
TTarget = typing.TypeVar('TTarget')
TResult = typing.TypeVar('TResult')
TOther = typing.TypeVar('TOther')
T1 = typing.TypeVar('T1')
T2 = typing.TypeVar('T2')
T3 = typing.TypeVar('T3')
TSiteFunc = typing.TypeVar('TSiteFunc')

class DynamicStackFrame(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    def __init__(self, method: System.Reflection.MethodBase, funcName: str, filename: str, line: int, ):
        ...

    def GetMethod(self, ) -> System.Reflection.MethodBase:
        ...

    def GetMethodName(self, ) -> str:
        ...

    def GetFileName(self, ) -> str:
        ...

    def GetFileLineNumber(self, ) -> int:
        ...

    def ToString(self, ) -> str:
        ...

class IMembersList(abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    @abc.abstractmethod
    def GetMemberNames(self, ) -> System.Collections.Generic.IList[str]:
        ...

class Scope(System.Dynamic.IDynamicMetaObjectProvider, System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def Storage(self) -> System.Object:
        ...

    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def __init__(self, dictionary: System.Collections.Generic.IDictionary[str, System.Object], ):
        ...

    @typing.overload
    def __init__(self, storage: System.Dynamic.IDynamicMetaObjectProvider, ):
        ...

    def GetExtension(self, languageContextId: Microsoft.Scripting.Runtime.ContextId, ) -> Microsoft.Scripting.Runtime.ScopeExtension:
        ...

    def SetExtension(self, languageContextId: Microsoft.Scripting.Runtime.ContextId, extension: Microsoft.Scripting.Runtime.ScopeExtension, ) -> Microsoft.Scripting.Runtime.ScopeExtension:
        ...

    def GetMetaObject(self, parameter: System.Linq.Expressions.Expression, ) -> System.Dynamic.DynamicMetaObject:
        ...

class ScopeExtension(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields
    EmptyArray: System.Array[Microsoft.Scripting.Runtime.ScopeExtension] = ...

    # properties
    @property
    def Scope(self) -> Microsoft.Scripting.Runtime.Scope:
        ...

    # methods
    def __init__(self, scope: Microsoft.Scripting.Runtime.Scope, ):
        ...

class ContextId(System.IEquatable[Microsoft.Scripting.Runtime.ContextId], System.ValueType):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields
    Empty: Microsoft.Scripting.Runtime.ContextId = ...

    # properties
    @property
    def Id(self) -> int:
        ...

    # methods
    def __init__(self, id: int, ):
        ...

    @staticmethod
    def RegisterContext(identifier: System.Object, ) -> Microsoft.Scripting.Runtime.ContextId:
        ...

    @staticmethod
    def LookupContext(identifier: System.Object, ) -> Microsoft.Scripting.Runtime.ContextId:
        ...

    @typing.overload
    def Equals(self, other: Microsoft.Scripting.Runtime.ContextId, ) -> bool:
        ...

    @typing.overload
    def Equals(self, obj: System.Object, ) -> bool:
        ...

    def GetHashCode(self, ) -> int:
        ...

class LanguageContext(System.Object, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def ContextId(self) -> Microsoft.Scripting.Runtime.ContextId:
        ...

    @property
    def DomainManager(self) -> Microsoft.Scripting.Runtime.ScriptDomainManager:
        ...

    @property
    def CanCreateSourceCode(self) -> bool:
        ...

    @property
    def LanguageVersion(self) -> System.Version:
        ...

    @property
    def DefaultEncoding(self) -> System.Text.Encoding:
        ...

    @property
    def LanguageGuid(self) -> System.Guid:
        ...

    @property
    def VendorGuid(self) -> System.Guid:
        ...

    @property
    def Options(self) -> Microsoft.Scripting.LanguageOptions:
        ...

    @property
    def Operations(self) -> Microsoft.Scripting.Runtime.DynamicOperations:
        ...

    # methods
    def __init__(self, domainManager: Microsoft.Scripting.Runtime.ScriptDomainManager, ):
        ...

    def GetScope(self, path: str, ) -> Microsoft.Scripting.Runtime.Scope:
        ...

    @typing.overload
    def CreateScope(self, ) -> Microsoft.Scripting.Runtime.Scope:
        ...

    @typing.overload
    def CreateScope(self, dictionary: System.Collections.Generic.IDictionary[str, System.Object], ) -> Microsoft.Scripting.Runtime.Scope:
        ...

    @typing.overload
    def CreateScope(self, storage: System.Dynamic.IDynamicMetaObjectProvider, ) -> Microsoft.Scripting.Runtime.Scope:
        ...

    def EnsureScopeExtension(self, scope: Microsoft.Scripting.Runtime.Scope, ) -> Microsoft.Scripting.Runtime.ScopeExtension:
        ...

    def CreateScopeExtension(self, scope: Microsoft.Scripting.Runtime.Scope, ) -> Microsoft.Scripting.Runtime.ScopeExtension:
        ...

    def ScopeSetVariable(self, scope: Microsoft.Scripting.Runtime.Scope, name: str, value: System.Object, ) -> None:
        ...

    def ScopeTryGetVariable(self, scope: Microsoft.Scripting.Runtime.Scope, name: str, value: ref[System.Object], ) -> bool:
        ...

    @typing.overload
    def ScopeGetVariable(self, scope: Microsoft.Scripting.Runtime.Scope, name: str, ) -> T:
        ...

    @typing.overload
    def ScopeGetVariable(self, scope: Microsoft.Scripting.Runtime.Scope, name: str, ) -> System.Object:
        ...

    def GetSourceReader(self, stream: System.IO.Stream, defaultEncoding: System.Text.Encoding, path: str, ) -> Microsoft.Scripting.SourceCodeReader:
        ...

    @typing.overload
    def GetCompilerOptions(self, ) -> Microsoft.Scripting.CompilerOptions:
        ...

    @typing.overload
    def GetCompilerOptions(self, scope: Microsoft.Scripting.Runtime.Scope, ) -> Microsoft.Scripting.CompilerOptions:
        ...

    @abc.abstractmethod
    def CompileSourceCode(self, sourceUnit: Microsoft.Scripting.SourceUnit, options: Microsoft.Scripting.CompilerOptions, errorSink: Microsoft.Scripting.ErrorSink, ) -> Microsoft.Scripting.ScriptCode:
        ...

    def LoadCompiledCode(self, method: System.Delegate, path: str, customData: str, ) -> Microsoft.Scripting.ScriptCode:
        ...

    def ExecuteProgram(self, program: Microsoft.Scripting.SourceUnit, ) -> int:
        ...

    def SetSearchPaths(self, paths: System.Collections.Generic.ICollection[str], ) -> None:
        ...

    def GetSearchPaths(self, ) -> System.Collections.Generic.ICollection[str]:
        ...

    def GenerateSourceCode(self, codeDom: System.CodeDom.CodeObject, path: str, kind: int, ) -> Microsoft.Scripting.SourceUnit:
        ...

    def GetService(self, args: System.Array[System.Object], ) -> TService:
        ...

    def Shutdown(self, ) -> None:
        ...

    def FormatException(self, exception: System.Exception, ) -> str:
        ...

    def GetStackFrames(self, exception: System.Exception, ) -> System.Collections.Generic.IList[Microsoft.Scripting.Runtime.DynamicStackFrame]:
        ...

    @typing.overload
    def CreateSnippet(self, code: str, kind: int, ) -> Microsoft.Scripting.SourceUnit:
        ...

    @typing.overload
    def CreateSnippet(self, code: str, id: str, kind: int, ) -> Microsoft.Scripting.SourceUnit:
        ...

    @typing.overload
    def CreateFileUnit(self, path: str, ) -> Microsoft.Scripting.SourceUnit:
        ...

    @typing.overload
    def CreateFileUnit(self, path: str, encoding: System.Text.Encoding, ) -> Microsoft.Scripting.SourceUnit:
        ...

    @typing.overload
    def CreateFileUnit(self, path: str, encoding: System.Text.Encoding, kind: int, ) -> Microsoft.Scripting.SourceUnit:
        ...

    @typing.overload
    def CreateFileUnit(self, path: str, content: str, ) -> Microsoft.Scripting.SourceUnit:
        ...

    @typing.overload
    def CreateSourceUnit(self, contentProvider: Microsoft.Scripting.StreamContentProvider, path: str, encoding: System.Text.Encoding, kind: int, ) -> Microsoft.Scripting.SourceUnit:
        ...

    @typing.overload
    def CreateSourceUnit(self, contentProvider: Microsoft.Scripting.TextContentProvider, path: str, kind: int, ) -> Microsoft.Scripting.SourceUnit:
        ...

    def GetCompilerErrorSink(self, ) -> Microsoft.Scripting.ErrorSink:
        ...

    @staticmethod
    def ErrorMetaObject(resultType: System.Type, target: System.Dynamic.DynamicMetaObject, args: System.Array[System.Dynamic.DynamicMetaObject], errorSuggestion: System.Dynamic.DynamicMetaObject, ) -> System.Dynamic.DynamicMetaObject:
        ...

    def CreateUnaryOperationBinder(self, operation: int, ) -> System.Dynamic.UnaryOperationBinder:
        ...

    def CreateBinaryOperationBinder(self, operation: int, ) -> System.Dynamic.BinaryOperationBinder:
        ...

    def CreateConvertBinder(self, toType: System.Type, explicitCast: System.Nullable[bool], ) -> System.Dynamic.ConvertBinder:
        ...

    def CreateGetMemberBinder(self, name: str, ignoreCase: bool, ) -> System.Dynamic.GetMemberBinder:
        ...

    def CreateSetMemberBinder(self, name: str, ignoreCase: bool, ) -> System.Dynamic.SetMemberBinder:
        ...

    def CreateDeleteMemberBinder(self, name: str, ignoreCase: bool, ) -> System.Dynamic.DeleteMemberBinder:
        ...

    def CreateCallBinder(self, name: str, ignoreCase: bool, callInfo: System.Dynamic.CallInfo, ) -> System.Dynamic.InvokeMemberBinder:
        ...

    def CreateInvokeBinder(self, callInfo: System.Dynamic.CallInfo, ) -> System.Dynamic.InvokeBinder:
        ...

    def CreateCreateBinder(self, callInfo: System.Dynamic.CallInfo, ) -> System.Dynamic.CreateInstanceBinder:
        ...

    def GetMemberNames(self, obj: System.Object, ) -> System.Collections.Generic.IList[str]:
        ...

    def GetDocumentation(self, obj: System.Object, ) -> str:
        ...

    def GetCallSignatures(self, obj: System.Object, ) -> System.Collections.Generic.IList[str]:
        ...

    def IsCallable(self, obj: System.Object, ) -> bool:
        ...

    def FormatObject(self, operations: Microsoft.Scripting.Runtime.DynamicOperations, obj: System.Object, ) -> str:
        ...

    def GetExceptionMessage(self, exception: System.Exception, message: ref[str], errorTypeName: ref[str], ) -> None:
        ...

class DynamicOperations(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    def __init__(self, lc: Microsoft.Scripting.Runtime.LanguageContext, ):
        ...

    def Invoke(self, obj: System.Object, parameters: System.Array[System.Object], ) -> System.Object:
        ...

    @typing.overload
    def InvokeMember(self, obj: System.Object, memberName: str, parameters: System.Array[System.Object], ) -> System.Object:
        ...

    @typing.overload
    def InvokeMember(self, obj: System.Object, memberName: str, ignoreCase: bool, parameters: System.Array[System.Object], ) -> System.Object:
        ...

    def CreateInstance(self, obj: System.Object, parameters: System.Array[System.Object], ) -> System.Object:
        ...

    @typing.overload
    def GetMember(self, obj: System.Object, name: str, ) -> System.Object:
        ...

    @typing.overload
    def GetMember(self, obj: System.Object, name: str, ) -> T:
        ...

    @typing.overload
    def GetMember(self, obj: System.Object, name: str, ignoreCase: bool, ) -> System.Object:
        ...

    @typing.overload
    def GetMember(self, obj: System.Object, name: str, ignoreCase: bool, ) -> T:
        ...

    @typing.overload
    def TryGetMember(self, obj: System.Object, name: str, value: ref[System.Object], ) -> bool:
        ...

    @typing.overload
    def TryGetMember(self, obj: System.Object, name: str, ignoreCase: bool, value: ref[System.Object], ) -> bool:
        ...

    @typing.overload
    def ContainsMember(self, obj: System.Object, name: str, ) -> bool:
        ...

    @typing.overload
    def ContainsMember(self, obj: System.Object, name: str, ignoreCase: bool, ) -> bool:
        ...

    @typing.overload
    def RemoveMember(self, obj: System.Object, name: str, ) -> None:
        ...

    @typing.overload
    def RemoveMember(self, obj: System.Object, name: str, ignoreCase: bool, ) -> None:
        ...

    @typing.overload
    def SetMember(self, obj: System.Object, name: str, value: System.Object, ) -> None:
        ...

    @typing.overload
    def SetMember(self, obj: System.Object, name: str, value: T, ) -> None:
        ...

    @typing.overload
    def SetMember(self, obj: System.Object, name: str, value: System.Object, ignoreCase: bool, ) -> None:
        ...

    @typing.overload
    def SetMember(self, obj: System.Object, name: str, value: T, ignoreCase: bool, ) -> None:
        ...

    @typing.overload
    def ConvertTo(self, obj: System.Object, ) -> T:
        ...

    @typing.overload
    def ConvertTo(self, obj: System.Object, type: System.Type, ) -> System.Object:
        ...

    @typing.overload
    def TryConvertTo(self, obj: System.Object, result: ref[T], ) -> bool:
        ...

    @typing.overload
    def TryConvertTo(self, obj: System.Object, type: System.Type, result: ref[System.Object], ) -> bool:
        ...

    @typing.overload
    def ExplicitConvertTo(self, obj: System.Object, ) -> T:
        ...

    @typing.overload
    def ExplicitConvertTo(self, obj: System.Object, type: System.Type, ) -> System.Object:
        ...

    @typing.overload
    def TryExplicitConvertTo(self, obj: System.Object, type: System.Type, result: ref[System.Object], ) -> bool:
        ...

    @typing.overload
    def TryExplicitConvertTo(self, obj: System.Object, result: ref[T], ) -> bool:
        ...

    @typing.overload
    def ImplicitConvertTo(self, obj: System.Object, ) -> T:
        ...

    @typing.overload
    def ImplicitConvertTo(self, obj: System.Object, type: System.Type, ) -> System.Object:
        ...

    @typing.overload
    def TryImplicitConvertTo(self, obj: System.Object, type: System.Type, result: ref[System.Object], ) -> bool:
        ...

    @typing.overload
    def TryImplicitConvertTo(self, obj: System.Object, result: ref[T], ) -> bool:
        ...

    @typing.overload
    def DoOperation(self, operation: int, target: TTarget, ) -> TResult:
        ...

    @typing.overload
    def DoOperation(self, operation: int, target: TTarget, other: TOther, ) -> TResult:
        ...

    def GetDocumentation(self, o: System.Object, ) -> str:
        ...

    def GetCallSignatures(self, o: System.Object, ) -> System.Collections.Generic.IList[str]:
        ...

    def IsCallable(self, o: System.Object, ) -> bool:
        ...

    def GetMemberNames(self, obj: System.Object, ) -> System.Collections.Generic.IList[str]:
        ...

    def Format(self, obj: System.Object, ) -> str:
        ...

    @typing.overload
    def GetOrCreateSite(self, siteBinder: System.Runtime.CompilerServices.CallSiteBinder, ) -> System.Runtime.CompilerServices.CallSite[System.Func[System.Runtime.CompilerServices.CallSite, T1, TResult]]:
        ...

    @typing.overload
    def GetOrCreateSite(self, siteBinder: System.Runtime.CompilerServices.CallSiteBinder, ) -> System.Runtime.CompilerServices.CallSite[System.Func[System.Runtime.CompilerServices.CallSite, T1, T2, TResult]]:
        ...

    @typing.overload
    def GetOrCreateSite(self, siteBinder: System.Runtime.CompilerServices.CallSiteBinder, ) -> System.Runtime.CompilerServices.CallSite[System.Func[System.Runtime.CompilerServices.CallSite, T1, T2, T3, TResult]]:
        ...

    @typing.overload
    def GetOrCreateSite(self, siteBinder: System.Runtime.CompilerServices.CallSiteBinder, ) -> System.Runtime.CompilerServices.CallSite[TSiteFunc]:
        ...

    @typing.overload
    def GetOrCreateSite(self, siteBinder: System.Runtime.CompilerServices.CallSiteBinder, factory: System.Func[System.Runtime.CompilerServices.CallSiteBinder, T], ) -> T:
        ...

    def GetOrCreateActionSite(self, siteBinder: System.Runtime.CompilerServices.CallSiteBinder, ) -> System.Runtime.CompilerServices.CallSite[System.Action[System.Runtime.CompilerServices.CallSite, T1]]:
        ...

    def CleanupNoLock(self, ) -> None:
        ...

    def GetInvoker(self, paramCount: int, ) -> System.Func[Microsoft.Scripting.Runtime.DynamicOperations, System.Runtime.CompilerServices.CallSiteBinder, System.Object, System.Array[System.Object], System.Object]:
        ...

    def EmitInvoker(self, paramCount: int, ) -> System.Func[Microsoft.Scripting.Runtime.DynamicOperations, System.Runtime.CompilerServices.CallSiteBinder, System.Object, System.Array[System.Object], System.Object]:
        ...

    @staticmethod
    def GetPregeneratedInvoker(paramCount: int, ) -> System.Func[Microsoft.Scripting.Runtime.DynamicOperations, System.Runtime.CompilerServices.CallSiteBinder, System.Object, System.Array[System.Object], System.Object]:
        ...

class ModuleChangeEventArgs(System.EventArgs):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def Name(self) -> str:
        ...

    @property
    def ChangeType(self) -> int:
        ...

    @property
    def Value(self) -> System.Object:
        ...

    # methods
    @typing.overload
    def __init__(self, name: str, changeType: int, ):
        ...

    @typing.overload
    def __init__(self, name: str, changeType: int, value: System.Object, ):
        ...

class TokenizerService(System.Object, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    @abc.abstractmethod
    def CurrentState(self) -> System.Object:
        ...

    @property
    @abc.abstractmethod
    def CurrentPosition(self) -> Microsoft.Scripting.SourceLocation:
        ...

    @property
    @abc.abstractmethod
    def IsRestartable(self) -> bool:
        ...

    @property
    @abc.abstractmethod
    def ErrorSink(self) -> Microsoft.Scripting.ErrorSink:
        ...
    @ErrorSink.setter
    @abc.abstractmethod
    def ErrorSink(self, val: Microsoft.Scripting.ErrorSink):
        ...

    # methods
    def __init__(self, ):
        ...

    @abc.abstractmethod
    def Initialize(self, state: System.Object, sourceReader: System.IO.TextReader, sourceUnit: Microsoft.Scripting.SourceUnit, initialLocation: Microsoft.Scripting.SourceLocation, ) -> None:
        ...

    @abc.abstractmethod
    def ReadToken(self, ) -> Microsoft.Scripting.TokenInfo:
        ...

    def SkipToken(self, ) -> bool:
        ...

    def ReadTokens(self, characterCount: int, ) -> System.Collections.Generic.IEnumerable[Microsoft.Scripting.TokenInfo]:
        ...

    def SkipTokens(self, countOfChars: int, ) -> bool:
        ...

class DynamicDelegateCreator(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    def __init__(self, languageContext: Microsoft.Scripting.Runtime.LanguageContext, ):
        ...

    def GetDelegate(self, callableObject: System.Object, delegateType: System.Type, ) -> System.Delegate:
        ...

    def GetOrCreateDelegateForDynamicObject(self, dynamicObject: System.Object, delegateType: System.Type, invoke: System.Reflection.MethodInfo, ) -> System.Delegate:
        ...

class BinderType(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    Normal: int = ...
    BinaryOperator: int = ...
    ComparisonOperator: int = ...
    Constructor: int = ...

class IExpressionSerializable(abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    @abc.abstractmethod
    def CreateExpression(self, ) -> System.Linq.Expressions.Expression:
        ...

class ScriptDomainManager(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def Platform(self) -> Microsoft.Scripting.PlatformAdaptationLayer:
        ...

    @property
    def SharedIO(self) -> Microsoft.Scripting.Runtime.SharedIO:
        ...

    @property
    def Host(self) -> Microsoft.Scripting.Runtime.DynamicRuntimeHostingProvider:
        ...

    @property
    def Configuration(self) -> Microsoft.Scripting.Runtime.DlrConfiguration:
        ...

    @property
    def Globals(self) -> Microsoft.Scripting.Runtime.Scope:
        ...
    @Globals.setter
    def Globals(self, val: Microsoft.Scripting.Runtime.Scope):
        ...

    # methods
    def __init__(self, hostingProvider: Microsoft.Scripting.Runtime.DynamicRuntimeHostingProvider, configuration: Microsoft.Scripting.Runtime.DlrConfiguration, ):
        ...

    def GenerateContextId(self, ) -> Microsoft.Scripting.Runtime.ContextId:
        ...

    def GetLanguage(self, providerType: System.Type, ) -> Microsoft.Scripting.Runtime.LanguageContext:
        ...

    def GetLanguageByTypeName(self, providerAssemblyQualifiedTypeName: str, ) -> Microsoft.Scripting.Runtime.LanguageContext:
        ...

    def TryGetLanguage(self, languageName: str, language: ref[Microsoft.Scripting.Runtime.LanguageContext], ) -> bool:
        ...

    def GetLanguageByName(self, languageName: str, ) -> Microsoft.Scripting.Runtime.LanguageContext:
        ...

    def TryGetLanguageByFileExtension(self, fileExtension: str, language: ref[Microsoft.Scripting.Runtime.LanguageContext], ) -> bool:
        ...

    def GetLanguageByExtension(self, fileExtension: str, ) -> Microsoft.Scripting.Runtime.LanguageContext:
        ...

    def LoadAssembly(self, assembly: System.Reflection.Assembly, ) -> bool:
        ...

    def GetLoadedAssemblyList(self, ) -> System.Collections.Generic.IList[System.Reflection.Assembly]:
        ...

class SharedIO(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def InputStream(self) -> System.IO.Stream:
        ...

    @property
    def OutputStream(self) -> System.IO.Stream:
        ...

    @property
    def ErrorStream(self) -> System.IO.Stream:
        ...

    @property
    def InputReader(self) -> System.IO.TextReader:
        ...

    @property
    def OutputWriter(self) -> System.IO.TextWriter:
        ...

    @property
    def ErrorWriter(self) -> System.IO.TextWriter:
        ...

    @property
    def InputEncoding(self) -> System.Text.Encoding:
        ...

    @property
    def OutputEncoding(self) -> System.Text.Encoding:
        ...

    @property
    def ErrorEncoding(self) -> System.Text.Encoding:
        ...

    # methods
    def __init__(self, ):
        ...

    def InitializeInput(self, ) -> None:
        ...

    def InitializeOutput(self, ) -> None:
        ...

    def InitializeErrorOutput(self, ) -> None:
        ...

    def SetOutput(self, stream: System.IO.Stream, writer: System.IO.TextWriter, ) -> None:
        ...

    def SetErrorOutput(self, stream: System.IO.Stream, writer: System.IO.TextWriter, ) -> None:
        ...

    def SetInput(self, stream: System.IO.Stream, reader: System.IO.TextReader, encoding: System.Text.Encoding, ) -> None:
        ...

    def RedirectToConsole(self, ) -> None:
        ...

    def GetStream(self, type: int, ) -> System.IO.Stream:
        ...

    def GetWriter(self, type: int, ) -> System.IO.TextWriter:
        ...

    def GetEncoding(self, type: int, ) -> System.Text.Encoding:
        ...

    def GetReader(self, encoding: ref[System.Text.Encoding], ) -> System.IO.TextReader:
        ...

    def GetStreamProxy(self, type: int, ) -> System.IO.Stream:
        ...

class DynamicRuntimeHostingProvider(System.Object, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    @abc.abstractmethod
    def PlatformAdaptationLayer(self) -> Microsoft.Scripting.PlatformAdaptationLayer:
        ...

    # methods
    def __init__(self, ):
        ...

class Extensible(System.Object, typing.Generic[T]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def Value(self) -> T:
        ...

    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def __init__(self, value: T, ):
        ...

    def Equals(self, obj: System.Object, ) -> bool:
        ...

    def GetHashCode(self, ) -> int:
        ...

    def ToString(self, ) -> str:
        ...

class CallTypes(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    None_: int = ...
    ImplicitInstance: int = ...

class ParserSink(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields
    Null: Microsoft.Scripting.Runtime.ParserSink = ...

    # properties
    # methods
    def __init__(self, ):
        ...

    def MatchPair(self, opening: Microsoft.Scripting.SourceSpan, closing: Microsoft.Scripting.SourceSpan, priority: int, ) -> None:
        ...

    def MatchTriple(self, opening: Microsoft.Scripting.SourceSpan, middle: Microsoft.Scripting.SourceSpan, closing: Microsoft.Scripting.SourceSpan, priority: int, ) -> None:
        ...

    def EndParameters(self, span: Microsoft.Scripting.SourceSpan, ) -> None:
        ...

    def NextParameter(self, span: Microsoft.Scripting.SourceSpan, ) -> None:
        ...

    def QualifyName(self, selector: Microsoft.Scripting.SourceSpan, span: Microsoft.Scripting.SourceSpan, name: str, ) -> None:
        ...

    def StartName(self, span: Microsoft.Scripting.SourceSpan, name: str, ) -> None:
        ...

    def StartParameters(self, context: Microsoft.Scripting.SourceSpan, ) -> None:
        ...

class CompilerContext(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def SourceUnit(self) -> Microsoft.Scripting.SourceUnit:
        ...

    @property
    def ParserSink(self) -> Microsoft.Scripting.Runtime.ParserSink:
        ...

    @property
    def Errors(self) -> Microsoft.Scripting.ErrorSink:
        ...

    @property
    def Options(self) -> Microsoft.Scripting.CompilerOptions:
        ...

    # methods
    @typing.overload
    def __init__(self, sourceUnit: Microsoft.Scripting.SourceUnit, options: Microsoft.Scripting.CompilerOptions, errorSink: Microsoft.Scripting.ErrorSink, ):
        ...

    @typing.overload
    def __init__(self, sourceUnit: Microsoft.Scripting.SourceUnit, options: Microsoft.Scripting.CompilerOptions, errorSink: Microsoft.Scripting.ErrorSink, parserSink: Microsoft.Scripting.Runtime.ParserSink, ):
        ...

class IDebuggableGenerator(abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    @abc.abstractmethod
    def YieldMarkerLocation(self) -> int:
        ...
    @YieldMarkerLocation.setter
    @abc.abstractmethod
    def YieldMarkerLocation(self, val: int):
        ...

    # methods
class ModuleChangeType(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    Set: int = ...
    Delete: int = ...

class DlrConfiguration(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields
    FileExtensionComparer: System.StringComparer = ...
    LanguageNameComparer: System.StringComparer = ...
    OptionNameComparer: System.StringComparer = ...

    # properties
    @property
    def DebugMode(self) -> bool:
        ...

    @property
    def PrivateBinding(self) -> bool:
        ...

    @property
    def Options(self) -> System.Collections.Generic.IDictionary[str, System.Object]:
        ...

    @property
    def Languages(self) -> System.Collections.Generic.IDictionary[Microsoft.Scripting.Utils.AssemblyQualifiedTypeName, Microsoft.Scripting.Runtime.LanguageConfiguration]:
        ...

    # methods
    def __init__(self, debugMode: bool, privateBinding: bool, options: System.Collections.Generic.IDictionary[str, System.Object], ):
        ...

    @typing.overload
    def AddLanguage(self, languageTypeName: str, displayName: str, names: System.Collections.Generic.IList[str], fileExtensions: System.Collections.Generic.IList[str], options: System.Collections.Generic.IDictionary[str, System.Object], ) -> None:
        ...

    @typing.overload
    def AddLanguage(self, languageTypeName: str, displayName: str, names: System.Collections.Generic.IList[str], fileExtensions: System.Collections.Generic.IList[str], options: System.Collections.Generic.IDictionary[str, System.Object], paramName: str, ) -> None:
        ...

    @staticmethod
    def NormalizeExtension(extension: str, ) -> str:
        ...

    def Freeze(self, ) -> None:
        ...

    @typing.overload
    def TryLoadLanguage(self, manager: Microsoft.Scripting.Runtime.ScriptDomainManager, providerName: ref[Microsoft.Scripting.Utils.AssemblyQualifiedTypeName], language: ref[Microsoft.Scripting.Runtime.LanguageContext], ) -> bool:
        ...

    @typing.overload
    def TryLoadLanguage(self, manager: Microsoft.Scripting.Runtime.ScriptDomainManager, str: str, isExtension: bool, language: ref[Microsoft.Scripting.Runtime.LanguageContext], ) -> bool:
        ...

    def LoadLanguageContext(self, manager: Microsoft.Scripting.Runtime.ScriptDomainManager, config: Microsoft.Scripting.Runtime.LanguageConfiguration, ) -> Microsoft.Scripting.Runtime.LanguageContext:
        ...

    @typing.overload
    def GetLanguageNames(self, context: Microsoft.Scripting.Runtime.LanguageContext, ) -> System.Array[str]:
        ...

    @typing.overload
    def GetLanguageNames(self, config: Microsoft.Scripting.Runtime.LanguageConfiguration, ) -> System.Array[str]:
        ...

    @typing.overload
    def GetLanguageNames(self, ) -> System.Array[str]:
        ...

    @typing.overload
    def GetFileExtensions(self, context: Microsoft.Scripting.Runtime.LanguageContext, ) -> System.Array[str]:
        ...

    @typing.overload
    def GetFileExtensions(self, config: Microsoft.Scripting.Runtime.LanguageConfiguration, ) -> System.Array[str]:
        ...

    @typing.overload
    def GetFileExtensions(self, ) -> System.Array[str]:
        ...

    def GetLanguageConfig(self, context: Microsoft.Scripting.Runtime.LanguageContext, ) -> Microsoft.Scripting.Runtime.LanguageConfiguration:
        ...

class ISlice(abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    @abc.abstractmethod
    def Start(self) -> System.Object:
        ...

    @property
    @abc.abstractmethod
    def Stop(self) -> System.Object:
        ...

    @property
    @abc.abstractmethod
    def Step(self) -> System.Object:
        ...

    # methods
class DynamicNull(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    def __init__(self, ):
        ...

