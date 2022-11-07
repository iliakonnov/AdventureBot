from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import System
import System.Collections.Generic
import Microsoft.Scripting.Hosting
import Microsoft.Scripting.Runtime
import System.Collections.ObjectModel
import System.IO
import Microsoft.Scripting
import System.Text
import System.Dynamic
import System.Linq.Expressions
import System.Reflection
import System.CodeDom

T = typing.TypeVar('T')
TTarget = typing.TypeVar('TTarget')
TResult = typing.TypeVar('TResult')
TOther = typing.TypeVar('TOther')
TService = typing.TypeVar('TService')
TRet = typing.TypeVar('TRet')

class ScriptRuntimeSetup(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def LanguageSetups(self) -> System.Collections.Generic.IList[Microsoft.Scripting.Hosting.LanguageSetup]:
        ...
    @LanguageSetups.setter
    def LanguageSetups(self, val: System.Collections.Generic.IList[Microsoft.Scripting.Hosting.LanguageSetup]):
        ...

    @property
    def DebugMode(self) -> bool:
        ...
    @DebugMode.setter
    def DebugMode(self, val: bool):
        ...

    @property
    def PrivateBinding(self) -> bool:
        ...
    @PrivateBinding.setter
    def PrivateBinding(self, val: bool):
        ...

    @property
    def HostType(self) -> System.Type:
        ...
    @HostType.setter
    def HostType(self, val: System.Type):
        ...

    @property
    def Options(self) -> System.Collections.Generic.IDictionary[str, System.Object]:
        ...
    @Options.setter
    def Options(self, val: System.Collections.Generic.IDictionary[str, System.Object]):
        ...

    @property
    def HostArguments(self) -> System.Collections.Generic.IList[System.Object]:
        ...
    @HostArguments.setter
    def HostArguments(self, val: System.Collections.Generic.IList[System.Object]):
        ...

    # methods
    def __init__(self, ):
        ...

    def ToConfiguration(self, ) -> Microsoft.Scripting.Runtime.DlrConfiguration:
        ...

    def Freeze(self, setups: System.Collections.ObjectModel.ReadOnlyCollection[Microsoft.Scripting.Hosting.LanguageSetup], ) -> None:
        ...

    def CheckFrozen(self, ) -> None:
        ...

    @staticmethod
    @typing.overload
    def ReadConfiguration() -> Microsoft.Scripting.Hosting.ScriptRuntimeSetup:
        ...

    @staticmethod
    @typing.overload
    def ReadConfiguration(configFileStream: System.IO.Stream, ) -> Microsoft.Scripting.Hosting.ScriptRuntimeSetup:
        ...

    @staticmethod
    @typing.overload
    def ReadConfiguration(configFilePath: str, ) -> Microsoft.Scripting.Hosting.ScriptRuntimeSetup:
        ...

    @staticmethod
    def LoadRuntimeSetup(setup: Microsoft.Scripting.Hosting.ScriptRuntimeSetup, configFileStream: System.IO.Stream, ) -> None:
        ...

    @staticmethod
    def LoadRuntimeSetupImpl(setup: Microsoft.Scripting.Hosting.ScriptRuntimeSetup, configFileStream: System.IO.Stream, ) -> None:
        ...

class LanguageSetup(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def TypeName(self) -> str:
        ...
    @TypeName.setter
    def TypeName(self, val: str):
        ...

    @property
    def DisplayName(self) -> str:
        ...
    @DisplayName.setter
    def DisplayName(self, val: str):
        ...

    @property
    def Names(self) -> System.Collections.Generic.IList[str]:
        ...
    @Names.setter
    def Names(self, val: System.Collections.Generic.IList[str]):
        ...

    @property
    def FileExtensions(self) -> System.Collections.Generic.IList[str]:
        ...
    @FileExtensions.setter
    def FileExtensions(self, val: System.Collections.Generic.IList[str]):
        ...

    @property
    def Options(self) -> System.Collections.Generic.IDictionary[str, System.Object]:
        ...
    @Options.setter
    def Options(self, val: System.Collections.Generic.IDictionary[str, System.Object]):
        ...

    @property
    def InterpretedMode(self) -> bool:
        ...
    @InterpretedMode.setter
    def InterpretedMode(self, val: bool):
        ...

    @property
    def NoAdaptiveCompilation(self) -> bool:
        ...
    @NoAdaptiveCompilation.setter
    def NoAdaptiveCompilation(self, val: bool):
        ...

    @property
    def ExceptionDetail(self) -> bool:
        ...
    @ExceptionDetail.setter
    def ExceptionDetail(self, val: bool):
        ...

    @property
    def PerfStats(self) -> bool:
        ...
    @PerfStats.setter
    def PerfStats(self, val: bool):
        ...

    # methods
    @typing.overload
    def __init__(self, typeName: str, ):
        ...

    @typing.overload
    def __init__(self, typeName: str, displayName: str, ):
        ...

    @typing.overload
    def __init__(self, typeName: str, displayName: str, names: System.Collections.Generic.IEnumerable[str], fileExtensions: System.Collections.Generic.IEnumerable[str], ):
        ...

    def GetOption(self, name: str, defaultValue: T, ) -> T:
        ...

    def GetCachedOption(self, name: str, storage: ref[System.Nullable[bool]], ) -> bool:
        ...

    def Freeze(self, ) -> None:
        ...

    def CheckFrozen(self, ) -> None:
        ...

class ScriptSource(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def SourceUnit(self) -> Microsoft.Scripting.SourceUnit:
        ...

    @property
    def Path(self) -> str:
        ...

    @property
    def Kind(self) -> int:
        ...

    @property
    def Engine(self) -> Microsoft.Scripting.Hosting.ScriptEngine:
        ...

    # methods
    def __init__(self, engine: Microsoft.Scripting.Hosting.ScriptEngine, sourceUnit: Microsoft.Scripting.SourceUnit, ):
        ...

    @typing.overload
    def Compile(self, ) -> Microsoft.Scripting.Hosting.CompiledCode:
        ...

    @typing.overload
    def Compile(self, errorListener: Microsoft.Scripting.Hosting.ErrorListener, ) -> Microsoft.Scripting.Hosting.CompiledCode:
        ...

    @typing.overload
    def Compile(self, compilerOptions: Microsoft.Scripting.CompilerOptions, ) -> Microsoft.Scripting.Hosting.CompiledCode:
        ...

    @typing.overload
    def Compile(self, compilerOptions: Microsoft.Scripting.CompilerOptions, errorListener: Microsoft.Scripting.Hosting.ErrorListener, ) -> Microsoft.Scripting.Hosting.CompiledCode:
        ...

    def CompileInternal(self, compilerOptions: Microsoft.Scripting.CompilerOptions, errorListener: Microsoft.Scripting.Hosting.ErrorListener, ) -> Microsoft.Scripting.Hosting.CompiledCode:
        ...

    @typing.overload
    def Execute(self, scope: Microsoft.Scripting.Hosting.ScriptScope, ) -> System.Object:
        ...

    @typing.overload
    def Execute(self, ) -> System.Object:
        ...

    @typing.overload
    def Execute(self, scope: Microsoft.Scripting.Hosting.ScriptScope, ) -> T:
        ...

    @typing.overload
    def Execute(self, ) -> T:
        ...

    def ExecuteProgram(self, ) -> int:
        ...

    @typing.overload
    def GetCodeProperties(self, ) -> int:
        ...

    @typing.overload
    def GetCodeProperties(self, options: Microsoft.Scripting.CompilerOptions, ) -> int:
        ...

    def GetReader(self, ) -> Microsoft.Scripting.SourceCodeReader:
        ...

    def DetectEncoding(self, ) -> System.Text.Encoding:
        ...

    def GetCodeLines(self, start: int, count: int, ) -> System.Array[str]:
        ...

    def GetCodeLine(self, line: int, ) -> str:
        ...

    def GetCode(self, ) -> str:
        ...

    @typing.overload
    def MapLine(self, line: int, ) -> int:
        ...

    @typing.overload
    def MapLine(self, span: Microsoft.Scripting.SourceSpan, ) -> Microsoft.Scripting.SourceSpan:
        ...

    @typing.overload
    def MapLine(self, location: Microsoft.Scripting.SourceLocation, ) -> Microsoft.Scripting.SourceLocation:
        ...

    def MapLinetoFile(self, line: int, ) -> str:
        ...

class ErrorListener(System.Object, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    def __init__(self, ):
        ...

    def ReportError(self, source: Microsoft.Scripting.Hosting.ScriptSource, message: str, span: ref[Microsoft.Scripting.SourceSpan], errorCode: int, severity: int, ) -> None:
        ...

    @abc.abstractmethod
    def ErrorReported(self, source: Microsoft.Scripting.Hosting.ScriptSource, message: str, span: Microsoft.Scripting.SourceSpan, errorCode: int, severity: int, ) -> None:
        ...

class ScriptScope(System.Dynamic.IDynamicMetaObjectProvider, System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def Scope(self) -> Microsoft.Scripting.Runtime.Scope:
        ...

    @property
    def Engine(self) -> Microsoft.Scripting.Hosting.ScriptEngine:
        ...

    # methods
    def __init__(self, engine: Microsoft.Scripting.Hosting.ScriptEngine, scope: Microsoft.Scripting.Runtime.Scope, ):
        ...

    @typing.overload
    def GetVariable(self, name: str, ) -> System.Object:
        ...

    @typing.overload
    def GetVariable(self, name: str, ) -> T:
        ...

    @typing.overload
    def TryGetVariable(self, name: str, value: ref[System.Object], ) -> bool:
        ...

    @typing.overload
    def TryGetVariable(self, name: str, value: ref[T], ) -> bool:
        ...

    def SetVariable(self, name: str, value: System.Object, ) -> None:
        ...

    def ContainsVariable(self, name: str, ) -> bool:
        ...

    def RemoveVariable(self, name: str, ) -> bool:
        ...

    def GetVariableNames(self, ) -> System.Collections.Generic.IEnumerable[str]:
        ...

    def GetItems(self, ) -> System.Collections.Generic.IEnumerable[System.Collections.Generic.KeyValuePair[str, System.Object]]:
        ...

    def GetMetaObject(self, parameter: System.Linq.Expressions.Expression, ) -> System.Dynamic.DynamicMetaObject:
        ...

class CompiledCode(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def ScriptCode(self) -> Microsoft.Scripting.ScriptCode:
        ...

    @property
    def Engine(self) -> Microsoft.Scripting.Hosting.ScriptEngine:
        ...

    @property
    def DefaultScope(self) -> Microsoft.Scripting.Hosting.ScriptScope:
        ...

    # methods
    def __init__(self, engine: Microsoft.Scripting.Hosting.ScriptEngine, code: Microsoft.Scripting.ScriptCode, ):
        ...

    @typing.overload
    def Execute(self, ) -> System.Object:
        ...

    @typing.overload
    def Execute(self, scope: Microsoft.Scripting.Hosting.ScriptScope, ) -> System.Object:
        ...

    @typing.overload
    def Execute(self, ) -> T:
        ...

    @typing.overload
    def Execute(self, scope: Microsoft.Scripting.Hosting.ScriptScope, ) -> T:
        ...

class ScriptRuntime(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def Manager(self) -> Microsoft.Scripting.Runtime.ScriptDomainManager:
        ...

    @property
    def Host(self) -> Microsoft.Scripting.Hosting.ScriptHost:
        ...

    @property
    def IO(self) -> Microsoft.Scripting.Hosting.ScriptIO:
        ...

    @property
    def Setup(self) -> Microsoft.Scripting.Hosting.ScriptRuntimeSetup:
        ...

    @property
    def Globals(self) -> Microsoft.Scripting.Hosting.ScriptScope:
        ...
    @Globals.setter
    def Globals(self, val: Microsoft.Scripting.Hosting.ScriptScope):
        ...

    @property
    def Operations(self) -> Microsoft.Scripting.Hosting.ObjectOperations:
        ...

    @property
    def InvariantEngine(self) -> Microsoft.Scripting.Hosting.ScriptEngine:
        ...

    # methods
    def __init__(self, setup: Microsoft.Scripting.Hosting.ScriptRuntimeSetup, ):
        ...

    @staticmethod
    def CreateFromConfiguration() -> Microsoft.Scripting.Hosting.ScriptRuntime:
        ...

    @typing.overload
    def GetEngine(self, languageName: str, ) -> Microsoft.Scripting.Hosting.ScriptEngine:
        ...

    @typing.overload
    def GetEngine(self, language: Microsoft.Scripting.Runtime.LanguageContext, ) -> Microsoft.Scripting.Hosting.ScriptEngine:
        ...

    def GetEngineByTypeName(self, assemblyQualifiedTypeName: str, ) -> Microsoft.Scripting.Hosting.ScriptEngine:
        ...

    def GetEngineByFileExtension(self, fileExtension: str, ) -> Microsoft.Scripting.Hosting.ScriptEngine:
        ...

    def TryGetEngine(self, languageName: str, engine: ref[Microsoft.Scripting.Hosting.ScriptEngine], ) -> bool:
        ...

    def TryGetEngineByFileExtension(self, fileExtension: str, engine: ref[Microsoft.Scripting.Hosting.ScriptEngine], ) -> bool:
        ...

    def GetEngineNoLockNoNotification(self, language: Microsoft.Scripting.Runtime.LanguageContext, freshEngineCreated: ref[bool], ) -> Microsoft.Scripting.Hosting.ScriptEngine:
        ...

    @typing.overload
    def CreateScope(self, ) -> Microsoft.Scripting.Hosting.ScriptScope:
        ...

    @typing.overload
    def CreateScope(self, languageId: str, ) -> Microsoft.Scripting.Hosting.ScriptScope:
        ...

    @typing.overload
    def CreateScope(self, storage: System.Dynamic.IDynamicMetaObjectProvider, ) -> Microsoft.Scripting.Hosting.ScriptScope:
        ...

    @typing.overload
    def CreateScope(self, languageId: str, storage: System.Dynamic.IDynamicMetaObjectProvider, ) -> Microsoft.Scripting.Hosting.ScriptScope:
        ...

    @typing.overload
    def CreateScope(self, dictionary: System.Collections.Generic.IDictionary[str, System.Object], ) -> Microsoft.Scripting.Hosting.ScriptScope:
        ...

    @typing.overload
    def CreateScope(self, languageId: str, storage: System.Collections.Generic.IDictionary[str, System.Object], ) -> Microsoft.Scripting.Hosting.ScriptScope:
        ...

    def ExecuteFile(self, path: str, ) -> Microsoft.Scripting.Hosting.ScriptScope:
        ...

    def UseFile(self, path: str, ) -> Microsoft.Scripting.Hosting.ScriptScope:
        ...

    def LoadAssembly(self, assembly: System.Reflection.Assembly, ) -> None:
        ...

    def CreateOperations(self, ) -> Microsoft.Scripting.Hosting.ObjectOperations:
        ...

    def Shutdown(self, ) -> None:
        ...

class ScriptHost(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def Runtime(self) -> Microsoft.Scripting.Hosting.ScriptRuntime:
        ...

    @property
    def PlatformAdaptationLayer(self) -> Microsoft.Scripting.PlatformAdaptationLayer:
        ...

    # methods
    def __init__(self, ):
        ...

    def SetRuntime(self, runtime: Microsoft.Scripting.Hosting.ScriptRuntime, ) -> None:
        ...

    def RuntimeAttached(self, ) -> None:
        ...

    def EngineCreated(self, engine: Microsoft.Scripting.Hosting.ScriptEngine, ) -> None:
        ...

class ScriptIO(System.Object):
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

    @property
    def SharedIO(self) -> Microsoft.Scripting.Runtime.SharedIO:
        ...

    # methods
    def __init__(self, io: Microsoft.Scripting.Runtime.SharedIO, ):
        ...

    @typing.overload
    def SetOutput(self, stream: System.IO.Stream, encoding: System.Text.Encoding, ) -> None:
        ...

    @typing.overload
    def SetOutput(self, stream: System.IO.Stream, writer: System.IO.TextWriter, ) -> None:
        ...

    @typing.overload
    def SetErrorOutput(self, stream: System.IO.Stream, encoding: System.Text.Encoding, ) -> None:
        ...

    @typing.overload
    def SetErrorOutput(self, stream: System.IO.Stream, writer: System.IO.TextWriter, ) -> None:
        ...

    @typing.overload
    def SetInput(self, stream: System.IO.Stream, encoding: System.Text.Encoding, ) -> None:
        ...

    @typing.overload
    def SetInput(self, stream: System.IO.Stream, reader: System.IO.TextReader, encoding: System.Text.Encoding, ) -> None:
        ...

    def RedirectToConsole(self, ) -> None:
        ...

class ObjectOperations(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def Engine(self) -> Microsoft.Scripting.Hosting.ScriptEngine:
        ...

    # methods
    def __init__(self, ops: Microsoft.Scripting.Runtime.DynamicOperations, engine: Microsoft.Scripting.Hosting.ScriptEngine, ):
        ...

    def IsCallable(self, obj: System.Object, ) -> bool:
        ...

    def Invoke(self, obj: System.Object, parameters: System.Array[System.Object], ) -> System.Object:
        ...

    def InvokeMember(self, obj: System.Object, memberName: str, parameters: System.Array[System.Object], ) -> System.Object:
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
    def TryExplicitConvertTo(self, obj: System.Object, result: ref[T], ) -> bool:
        ...

    @typing.overload
    def TryExplicitConvertTo(self, obj: System.Object, type: System.Type, result: ref[System.Object], ) -> bool:
        ...

    @typing.overload
    def ImplicitConvertTo(self, obj: System.Object, ) -> T:
        ...

    @typing.overload
    def ImplicitConvertTo(self, obj: System.Object, type: System.Type, ) -> System.Object:
        ...

    @typing.overload
    def TryImplicitConvertTo(self, obj: System.Object, result: ref[T], ) -> bool:
        ...

    @typing.overload
    def TryImplicitConvertTo(self, obj: System.Object, type: System.Type, result: ref[System.Object], ) -> bool:
        ...

    @typing.overload
    def DoOperation(self, operation: int, target: System.Object, ) -> System.Object:
        ...

    @typing.overload
    def DoOperation(self, operation: int, target: TTarget, ) -> TResult:
        ...

    @typing.overload
    def DoOperation(self, operation: int, target: System.Object, other: System.Object, ) -> System.Object:
        ...

    @typing.overload
    def DoOperation(self, operation: int, target: TTarget, other: TOther, ) -> TResult:
        ...

    def Add(self, self: System.Object, other: System.Object, ) -> System.Object:
        ...

    def Subtract(self, self: System.Object, other: System.Object, ) -> System.Object:
        ...

    def Power(self, self: System.Object, other: System.Object, ) -> System.Object:
        ...

    def Multiply(self, self: System.Object, other: System.Object, ) -> System.Object:
        ...

    def Divide(self, self: System.Object, other: System.Object, ) -> System.Object:
        ...

    def Modulo(self, self: System.Object, other: System.Object, ) -> System.Object:
        ...

    def LeftShift(self, self: System.Object, other: System.Object, ) -> System.Object:
        ...

    def RightShift(self, self: System.Object, other: System.Object, ) -> System.Object:
        ...

    def BitwiseAnd(self, self: System.Object, other: System.Object, ) -> System.Object:
        ...

    def BitwiseOr(self, self: System.Object, other: System.Object, ) -> System.Object:
        ...

    def ExclusiveOr(self, self: System.Object, other: System.Object, ) -> System.Object:
        ...

    def LessThan(self, self: System.Object, other: System.Object, ) -> bool:
        ...

    def GreaterThan(self, self: System.Object, other: System.Object, ) -> bool:
        ...

    def LessThanOrEqual(self, self: System.Object, other: System.Object, ) -> bool:
        ...

    def GreaterThanOrEqual(self, self: System.Object, other: System.Object, ) -> bool:
        ...

    def Equal(self, self: System.Object, other: System.Object, ) -> bool:
        ...

    def NotEqual(self, self: System.Object, other: System.Object, ) -> bool:
        ...

    def GetCodeRepresentation(self, obj: System.Object, ) -> str:
        ...

    def Format(self, obj: System.Object, ) -> str:
        ...

    def GetMemberNames(self, obj: System.Object, ) -> System.Collections.Generic.IList[str]:
        ...

    def GetDocumentation(self, obj: System.Object, ) -> str:
        ...

    def GetCallSignatures(self, obj: System.Object, ) -> System.Collections.Generic.IList[str]:
        ...

class ScriptEngine(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def Operations(self) -> Microsoft.Scripting.Hosting.ObjectOperations:
        ...

    @property
    def Setup(self) -> Microsoft.Scripting.Hosting.LanguageSetup:
        ...

    @property
    def Runtime(self) -> Microsoft.Scripting.Hosting.ScriptRuntime:
        ...

    @property
    def LanguageVersion(self) -> System.Version:
        ...

    @property
    def LanguageContext(self) -> Microsoft.Scripting.Runtime.LanguageContext:
        ...

    # methods
    def __init__(self, runtime: Microsoft.Scripting.Hosting.ScriptRuntime, context: Microsoft.Scripting.Runtime.LanguageContext, ):
        ...

    @typing.overload
    def CreateOperations(self, ) -> Microsoft.Scripting.Hosting.ObjectOperations:
        ...

    @typing.overload
    def CreateOperations(self, scope: Microsoft.Scripting.Hosting.ScriptScope, ) -> Microsoft.Scripting.Hosting.ObjectOperations:
        ...

    @typing.overload
    def Execute(self, expression: str, ) -> System.Object:
        ...

    @typing.overload
    def Execute(self, expression: str, scope: Microsoft.Scripting.Hosting.ScriptScope, ) -> System.Object:
        ...

    @typing.overload
    def Execute(self, expression: str, ) -> T:
        ...

    @typing.overload
    def Execute(self, expression: str, scope: Microsoft.Scripting.Hosting.ScriptScope, ) -> T:
        ...

    @typing.overload
    def ExecuteFile(self, path: str, ) -> Microsoft.Scripting.Hosting.ScriptScope:
        ...

    @typing.overload
    def ExecuteFile(self, path: str, scope: Microsoft.Scripting.Hosting.ScriptScope, ) -> Microsoft.Scripting.Hosting.ScriptScope:
        ...

    @typing.overload
    def CreateScope(self, ) -> Microsoft.Scripting.Hosting.ScriptScope:
        ...

    @typing.overload
    def CreateScope(self, dictionary: System.Collections.Generic.IDictionary[str, System.Object], ) -> Microsoft.Scripting.Hosting.ScriptScope:
        ...

    @typing.overload
    def CreateScope(self, storage: System.Dynamic.IDynamicMetaObjectProvider, ) -> Microsoft.Scripting.Hosting.ScriptScope:
        ...

    def GetScope(self, path: str, ) -> Microsoft.Scripting.Hosting.ScriptScope:
        ...

    @typing.overload
    def CreateScriptSourceFromString(self, expression: str, ) -> Microsoft.Scripting.Hosting.ScriptSource:
        ...

    @typing.overload
    def CreateScriptSourceFromString(self, code: str, kind: int, ) -> Microsoft.Scripting.Hosting.ScriptSource:
        ...

    @typing.overload
    def CreateScriptSourceFromString(self, expression: str, path: str, ) -> Microsoft.Scripting.Hosting.ScriptSource:
        ...

    @typing.overload
    def CreateScriptSourceFromString(self, code: str, path: str, kind: int, ) -> Microsoft.Scripting.Hosting.ScriptSource:
        ...

    @typing.overload
    def CreateScriptSourceFromFile(self, path: str, ) -> Microsoft.Scripting.Hosting.ScriptSource:
        ...

    @typing.overload
    def CreateScriptSourceFromFile(self, path: str, encoding: System.Text.Encoding, ) -> Microsoft.Scripting.Hosting.ScriptSource:
        ...

    @typing.overload
    def CreateScriptSourceFromFile(self, path: str, encoding: System.Text.Encoding, kind: int, ) -> Microsoft.Scripting.Hosting.ScriptSource:
        ...

    @typing.overload
    def CreateScriptSource(self, content: System.CodeDom.CodeObject, ) -> Microsoft.Scripting.Hosting.ScriptSource:
        ...

    @typing.overload
    def CreateScriptSource(self, content: System.CodeDom.CodeObject, path: str, ) -> Microsoft.Scripting.Hosting.ScriptSource:
        ...

    @typing.overload
    def CreateScriptSource(self, content: System.CodeDom.CodeObject, kind: int, ) -> Microsoft.Scripting.Hosting.ScriptSource:
        ...

    @typing.overload
    def CreateScriptSource(self, content: System.CodeDom.CodeObject, path: str, kind: int, ) -> Microsoft.Scripting.Hosting.ScriptSource:
        ...

    @typing.overload
    def CreateScriptSource(self, content: Microsoft.Scripting.StreamContentProvider, path: str, ) -> Microsoft.Scripting.Hosting.ScriptSource:
        ...

    @typing.overload
    def CreateScriptSource(self, content: Microsoft.Scripting.StreamContentProvider, path: str, encoding: System.Text.Encoding, ) -> Microsoft.Scripting.Hosting.ScriptSource:
        ...

    @typing.overload
    def CreateScriptSource(self, content: Microsoft.Scripting.StreamContentProvider, path: str, encoding: System.Text.Encoding, kind: int, ) -> Microsoft.Scripting.Hosting.ScriptSource:
        ...

    @typing.overload
    def CreateScriptSource(self, contentProvider: Microsoft.Scripting.TextContentProvider, path: str, kind: int, ) -> Microsoft.Scripting.Hosting.ScriptSource:
        ...

    def GetService(self, args: System.Array[System.Object], ) -> TService:
        ...

    @typing.overload
    def GetCompilerOptions(self, ) -> Microsoft.Scripting.CompilerOptions:
        ...

    @typing.overload
    def GetCompilerOptions(self, scope: Microsoft.Scripting.Hosting.ScriptScope, ) -> Microsoft.Scripting.CompilerOptions:
        ...

    def SetSearchPaths(self, paths: System.Collections.Generic.ICollection[str], ) -> None:
        ...

    def GetSearchPaths(self, ) -> System.Collections.Generic.ICollection[str]:
        ...

    def Call(self, f: System.Func[Microsoft.Scripting.Runtime.LanguageContext, T, TRet], arg: T, ) -> TRet:
        ...

