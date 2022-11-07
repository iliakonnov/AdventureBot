from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import System.Runtime.Serialization
import System
import Microsoft.Scripting
import System.Reflection
import System.Collections
import Microsoft.Scripting.Runtime
import System.Collections.ObjectModel
import System.Collections.Generic
import System.Linq.Expressions
import System.IO
import System.Text

T = typing.TypeVar('T')
T0 = typing.TypeVar('T0')
T1 = typing.TypeVar('T1')

class SyntaxErrorException(System.Runtime.Serialization.ISerializable, System.Exception):
    @typing.overload
    def __init__(self, **kwargs):
        self._message: str
        ...

    # static fields

    # properties
    @property
    def RawSpan(self) -> Microsoft.Scripting.SourceSpan:
        ...

    @property
    def SourceCode(self) -> str:
        ...

    @property
    def SourcePath(self) -> str:
        ...

    @property
    def Severity(self) -> int:
        ...

    @property
    def Line(self) -> int:
        ...

    @property
    def Column(self) -> int:
        ...

    @property
    def ErrorCode(self) -> int:
        ...

    @property
    def TargetSite(self) -> System.Reflection.MethodBase:
        ...

    @property
    def Message(self) -> str:
        ...

    @property
    def Data(self) -> System.Collections.IDictionary:
        ...

    @property
    def InnerException(self) -> System.Exception:
        ...

    @property
    def HelpLink(self) -> str:
        ...
    @HelpLink.setter
    def HelpLink(self, val: str):
        ...

    @property
    def Source(self) -> str:
        ...
    @Source.setter
    def Source(self, val: str):
        ...

    @property
    def HResult(self) -> int:
        ...
    @HResult.setter
    def HResult(self, val: int):
        ...

    @property
    def StackTrace(self) -> str:
        ...

    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def __init__(self, message: str, ):
        ...

    @typing.overload
    def __init__(self, message: str, innerException: System.Exception, ):
        ...

    @typing.overload
    def __init__(self, message: str, sourceUnit: Microsoft.Scripting.SourceUnit, span: Microsoft.Scripting.SourceSpan, errorCode: int, severity: int, ):
        ...

    @typing.overload
    def __init__(self, message: str, path: str, code: str, line: str, span: Microsoft.Scripting.SourceSpan, errorCode: int, severity: int, ):
        ...

    @typing.overload
    def __init__(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext, ):
        ...

    def GetObjectData(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext, ) -> None:
        ...

    def GetSymbolDocumentName(self, ) -> str:
        ...

    def GetCodeLine(self, ) -> str:
        ...

class CompilerOptions(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    def __init__(self, ):
        ...

class ScriptCode(System.Object, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def LanguageContext(self) -> Microsoft.Scripting.Runtime.LanguageContext:
        ...

    @property
    def SourceUnit(self) -> Microsoft.Scripting.SourceUnit:
        ...

    # methods
    def __init__(self, sourceUnit: Microsoft.Scripting.SourceUnit, ):
        ...

    def CreateScope(self, ) -> Microsoft.Scripting.Runtime.Scope:
        ...

    @typing.overload
    def Run(self, ) -> System.Object:
        ...

    @abc.abstractmethod
    @typing.overload
    def Run(self, scope: Microsoft.Scripting.Runtime.Scope, ) -> System.Object:
        ...

    def ToString(self, ) -> str:
        ...

class ErrorSink(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields
    Default: Microsoft.Scripting.ErrorSink = ...
    Null: Microsoft.Scripting.ErrorSink = ...

    # properties
    # methods
    def __init__(self, ):
        ...

    @typing.overload
    def Add(self, source: Microsoft.Scripting.SourceUnit, message: str, span: Microsoft.Scripting.SourceSpan, errorCode: int, severity: int, ) -> None:
        ...

    @typing.overload
    def Add(self, message: str, path: str, code: str, line: str, span: Microsoft.Scripting.SourceSpan, errorCode: int, severity: int, ) -> None:
        ...

class LanguageOptions(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields
    EmptyStringCollection: System.Collections.ObjectModel.ReadOnlyCollection[str] = ...

    # properties
    @property
    def NoAdaptiveCompilation(self) -> bool:
        ...

    @property
    def CompilationThreshold(self) -> int:
        ...

    @property
    def InterpretedMode(self) -> bool:
        ...
    @InterpretedMode.setter
    def InterpretedMode(self, val: bool):
        ...

    @property
    def ExceptionDetail(self) -> bool:
        ...
    @ExceptionDetail.setter
    def ExceptionDetail(self, val: bool):
        ...

    @property
    def ShowClrExceptions(self) -> bool:
        ...
    @ShowClrExceptions.setter
    def ShowClrExceptions(self, val: bool):
        ...

    @property
    def PerfStats(self) -> bool:
        ...

    @property
    def SearchPaths(self) -> System.Collections.ObjectModel.ReadOnlyCollection[str]:
        ...

    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def __init__(self, options: System.Collections.Generic.IDictionary[str, System.Object], ):
        ...

    @staticmethod
    def GetOption(options: System.Collections.Generic.IDictionary[str, System.Object], name: str, defaultValue: T, ) -> T:
        ...

    @staticmethod
    def GetStringCollectionOption(options: System.Collections.Generic.IDictionary[str, System.Object], name: str, separators: System.Array[str], ) -> System.Collections.ObjectModel.ReadOnlyCollection[str]:
        ...

    @staticmethod
    def GetSearchPathsOption(options: System.Collections.Generic.IDictionary[str, System.Object], ) -> System.Collections.ObjectModel.ReadOnlyCollection[str]:
        ...

class IndexSpan(System.IEquatable[Microsoft.Scripting.IndexSpan], System.ValueType):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def Start(self) -> int:
        ...

    @property
    def End(self) -> int:
        ...

    @property
    def Length(self) -> int:
        ...

    @property
    def IsEmpty(self) -> bool:
        ...

    # methods
    def __init__(self, start: int, length: int, ):
        ...

    def GetHashCode(self, ) -> int:
        ...

    @typing.overload
    def Equals(self, obj: System.Object, ) -> bool:
        ...

    @typing.overload
    def Equals(self, other: Microsoft.Scripting.IndexSpan, ) -> bool:
        ...

class SourceUnit(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def Path(self) -> str:
        ...

    @property
    def HasPath(self) -> bool:
        ...

    @property
    def Kind(self) -> int:
        ...

    @property
    def Document(self) -> System.Linq.Expressions.SymbolDocumentInfo:
        ...

    @property
    def LanguageContext(self) -> Microsoft.Scripting.Runtime.LanguageContext:
        ...

    @property
    def CodeProperties(self) -> System.Nullable[int]:
        ...
    @CodeProperties.setter
    def CodeProperties(self, val: System.Nullable[int]):
        ...

    @property
    def HasLineMapping(self) -> bool:
        ...

    @property
    def EmitDebugSymbols(self) -> bool:
        ...

    # methods
    def __init__(self, context: Microsoft.Scripting.Runtime.LanguageContext, contentProvider: Microsoft.Scripting.TextContentProvider, path: str, kind: int, ):
        ...

    @typing.overload
    def GetCodeProperties(self, ) -> int:
        ...

    @typing.overload
    def GetCodeProperties(self, options: Microsoft.Scripting.CompilerOptions, ) -> int:
        ...

    def GetReader(self, ) -> Microsoft.Scripting.SourceCodeReader:
        ...

    def GetCodeLines(self, start: int, count: int, ) -> System.Array[str]:
        ...

    def GetCodeLine(self, line: int, ) -> str:
        ...

    def GetCode(self, ) -> str:
        ...

    @typing.overload
    def MakeLocation(self, index: int, line: int, column: int, ) -> Microsoft.Scripting.SourceLocation:
        ...

    @typing.overload
    def MakeLocation(self, loc: Microsoft.Scripting.SourceLocation, ) -> Microsoft.Scripting.SourceLocation:
        ...

    def MapLine(self, line: int, ) -> int:
        ...

    @staticmethod
    def BinarySearch(array: System.Array[System.Collections.Generic.KeyValuePair[int, T]], line: int, ) -> int:
        ...

    @typing.overload
    def Compile(self, ) -> Microsoft.Scripting.ScriptCode:
        ...

    @typing.overload
    def Compile(self, errorSink: Microsoft.Scripting.ErrorSink, ) -> Microsoft.Scripting.ScriptCode:
        ...

    @typing.overload
    def Compile(self, options: Microsoft.Scripting.CompilerOptions, errorSink: Microsoft.Scripting.ErrorSink, ) -> Microsoft.Scripting.ScriptCode:
        ...

    @typing.overload
    def Execute(self, scope: Microsoft.Scripting.Runtime.Scope, ) -> System.Object:
        ...

    @typing.overload
    def Execute(self, scope: Microsoft.Scripting.Runtime.Scope, errorSink: Microsoft.Scripting.ErrorSink, ) -> System.Object:
        ...

    @typing.overload
    def Execute(self, ) -> System.Object:
        ...

    @typing.overload
    def Execute(self, errorSink: Microsoft.Scripting.ErrorSink, ) -> System.Object:
        ...

    @typing.overload
    def Execute(self, options: Microsoft.Scripting.CompilerOptions, errorSink: Microsoft.Scripting.ErrorSink, ) -> System.Object:
        ...

    def ExecuteProgram(self, ) -> int:
        ...

    def SetLineMapping(self, lineMap: System.Array[System.Collections.Generic.KeyValuePair[int, int]], ) -> None:
        ...

class ScriptCodeParseResult(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    Complete: int = ...
    Empty: int = ...
    Invalid: int = ...
    IncompleteToken: int = ...
    IncompleteStatement: int = ...

class SourceCodeReader(System.IDisposable, System.IO.TextReader):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields
    Null: Microsoft.Scripting.SourceCodeReader = ...

    # properties
    @property
    def Encoding(self) -> System.Text.Encoding:
        ...

    @property
    def BaseReader(self) -> System.IO.TextReader:
        ...

    # methods
    def __init__(self, textReader: System.IO.TextReader, encoding: System.Text.Encoding, ):
        ...

    def ReadLine(self, ) -> str:
        ...

    def SeekLine(self, line: int, ) -> bool:
        ...

    def ReadToEnd(self, ) -> str:
        ...

    @typing.overload
    def Read(self, buffer: System.Array[str], index: int, count: int, ) -> int:
        ...

    @typing.overload
    def Read(self, ) -> int:
        ...

    def Peek(self, ) -> int:
        ...

    def Dispose(self, disposing: bool, ) -> None:
        ...

class ArgumentTypeException(System.Runtime.Serialization.ISerializable, System.Exception):
    @typing.overload
    def __init__(self, **kwargs):
        self._message: str
        ...

    # static fields

    # properties
    @property
    def TargetSite(self) -> System.Reflection.MethodBase:
        ...

    @property
    def Message(self) -> str:
        ...

    @property
    def Data(self) -> System.Collections.IDictionary:
        ...

    @property
    def InnerException(self) -> System.Exception:
        ...

    @property
    def HelpLink(self) -> str:
        ...
    @HelpLink.setter
    def HelpLink(self, val: str):
        ...

    @property
    def Source(self) -> str:
        ...
    @Source.setter
    def Source(self, val: str):
        ...

    @property
    def HResult(self) -> int:
        ...
    @HResult.setter
    def HResult(self, val: int):
        ...

    @property
    def StackTrace(self) -> str:
        ...

    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def __init__(self, message: str, ):
        ...

    @typing.overload
    def __init__(self, message: str, innerException: System.Exception, ):
        ...

    @typing.overload
    def __init__(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext, ):
        ...

class StreamContentProvider(System.Object, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    def __init__(self, ):
        ...

    @abc.abstractmethod
    def GetStream(self, ) -> System.IO.Stream:
        ...

class MutableTuple(System.Object, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields
    MaxSize: int = ...

    # properties
    @property
    @abc.abstractmethod
    def Capacity(self) -> int:
        ...

    # methods
    def __init__(self, ):
        ...

    @abc.abstractmethod
    def GetValue(self, index: int, ) -> System.Object:
        ...

    @abc.abstractmethod
    def SetValue(self, index: int, value: System.Object, ) -> None:
        ...

    def SetNestedValue(self, size: int, index: int, value: System.Object, ) -> None:
        ...

    def GetNestedValue(self, size: int, index: int, ) -> System.Object:
        ...

    @staticmethod
    def GetTupleType(size: int, ) -> System.Type:
        ...

    @staticmethod
    @typing.overload
    def MakeTupleType(types: System.Array[System.Type], ) -> System.Type:
        ...

    @staticmethod
    @typing.overload
    def MakeTupleType(types: System.Array[System.Type], start: int, end: int, ) -> System.Type:
        ...

    @staticmethod
    def GetSize(tupleType: System.Type, ) -> int:
        ...

    @staticmethod
    @typing.overload
    def MakeTuple(tupleType: System.Type, args: System.Array[System.Object], ) -> Microsoft.Scripting.MutableTuple:
        ...

    @staticmethod
    @typing.overload
    def MakeTuple(tupleType: System.Type, start: int, end: int, args: System.Array[System.Object], ) -> Microsoft.Scripting.MutableTuple:
        ...

    @staticmethod
    @typing.overload
    def GetTupleValues(tuple: Microsoft.Scripting.MutableTuple, ) -> System.Array[System.Object]:
        ...

    @staticmethod
    @typing.overload
    def GetTupleValues(tuple: Microsoft.Scripting.MutableTuple, args: System.Collections.Generic.List[System.Object], ) -> None:
        ...

    @staticmethod
    @typing.overload
    def GetAccessPath(tupleType: System.Type, index: int, ) -> System.Collections.Generic.IEnumerable[System.Reflection.PropertyInfo]:
        ...

    @staticmethod
    @typing.overload
    def GetAccessPath(tupleType: System.Type, size: int, index: int, ) -> System.Collections.Generic.IEnumerable[System.Reflection.PropertyInfo]:
        ...

    @staticmethod
    @typing.overload
    def GetAccessPath(size: int, index: int, ) -> System.Collections.Generic.IEnumerable[int]:
        ...

    @staticmethod
    def CreateTupleInstance(tupleType: System.Type, start: int, end: int, args: System.Array[System.Object], ) -> Microsoft.Scripting.MutableTuple:
        ...

    @staticmethod
    def Create(values: System.Array[System.Linq.Expressions.Expression], ) -> System.Linq.Expressions.Expression:
        ...

    @staticmethod
    def PowerOfTwoRound(value: int, ) -> int:
        ...

    @staticmethod
    def CreateNew(tupleType: System.Type, start: int, end: int, values: System.Array[System.Linq.Expressions.Expression], ) -> System.Linq.Expressions.Expression:
        ...

class Severity(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    Ignore: int = ...
    Warning: int = ...
    Error: int = ...
    FatalError: int = ...

class TextContentProvider(System.Object, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    def __init__(self, ):
        ...

    @abc.abstractmethod
    def GetReader(self, ) -> Microsoft.Scripting.SourceCodeReader:
        ...

class SourceLocation(System.IEquatable[Microsoft.Scripting.SourceLocation], System.ValueType):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields
    None_: Microsoft.Scripting.SourceLocation = ...
    Invalid: Microsoft.Scripting.SourceLocation = ...
    MinValue: Microsoft.Scripting.SourceLocation = ...

    # properties
    @property
    def Index(self) -> int:
        ...

    @property
    def Line(self) -> int:
        ...

    @property
    def Column(self) -> int:
        ...

    @property
    def IsValid(self) -> bool:
        ...

    # methods
    @typing.overload
    def __init__(self, index: int, line: int, column: int, ):
        ...

    @typing.overload
    def __init__(self, index: int, line: int, column: int, noChecks: bool, ):
        ...

    @staticmethod
    def ValidateLocation(index: int, line: int, column: int, ) -> None:
        ...

    @staticmethod
    def ErrorOutOfRange(p0: System.Object, p1: System.Object, ) -> System.Exception:
        ...

    @staticmethod
    def Compare(left: Microsoft.Scripting.SourceLocation, right: Microsoft.Scripting.SourceLocation, ) -> int:
        ...

    @typing.overload
    def Equals(self, other: Microsoft.Scripting.SourceLocation, ) -> bool:
        ...

    @typing.overload
    def Equals(self, obj: System.Object, ) -> bool:
        ...

    def GetHashCode(self, ) -> int:
        ...

    def ToString(self, ) -> str:
        ...

    def ToDebugString(self, ) -> str:
        ...

class MutableTuple(Microsoft.Scripting.MutableTuple[T0], typing.Generic[T0, T1]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def Item001(self) -> T1:
        ...
    @Item001.setter
    def Item001(self, val: T1):
        ...

    @property
    def Capacity(self) -> int:
        ...

    @property
    def Item000(self) -> T0:
        ...
    @Item000.setter
    def Item000(self, val: T0):
        ...

    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def __init__(self, item0: T0, item1: T1, ):
        ...

    def GetValue(self, index: int, ) -> System.Object:
        ...

    def SetValue(self, index: int, value: System.Object, ) -> None:
        ...

class MutableTuple(Microsoft.Scripting.MutableTuple, typing.Generic[T0]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def Item000(self) -> T0:
        ...
    @Item000.setter
    def Item000(self, val: T0):
        ...

    @property
    def Capacity(self) -> int:
        ...

    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def __init__(self, item0: T0, ):
        ...

    def GetValue(self, index: int, ) -> System.Object:
        ...

    def SetValue(self, index: int, value: System.Object, ) -> None:
        ...

class SourceSpan(System.IEquatable[Microsoft.Scripting.SourceSpan], System.ValueType):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields
    None_: Microsoft.Scripting.SourceSpan = ...
    Invalid: Microsoft.Scripting.SourceSpan = ...

    # properties
    @property
    def Start(self) -> Microsoft.Scripting.SourceLocation:
        ...

    @property
    def End(self) -> Microsoft.Scripting.SourceLocation:
        ...

    @property
    def Length(self) -> int:
        ...

    @property
    def IsValid(self) -> bool:
        ...

    # methods
    def __init__(self, start: Microsoft.Scripting.SourceLocation, end: Microsoft.Scripting.SourceLocation, ):
        ...

    @staticmethod
    def ValidateLocations(start: ref[Microsoft.Scripting.SourceLocation], end: ref[Microsoft.Scripting.SourceLocation], ) -> None:
        ...

    @typing.overload
    def Equals(self, other: Microsoft.Scripting.SourceSpan, ) -> bool:
        ...

    @typing.overload
    def Equals(self, obj: System.Object, ) -> bool:
        ...

    def ToString(self, ) -> str:
        ...

    def GetHashCode(self, ) -> int:
        ...

    def ToDebugString(self, ) -> str:
        ...

class TokenInfo(System.IEquatable[Microsoft.Scripting.TokenInfo], System.ValueType):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def Category(self) -> int:
        ...
    @Category.setter
    def Category(self, val: int):
        ...

    @property
    def Trigger(self) -> int:
        ...
    @Trigger.setter
    def Trigger(self, val: int):
        ...

    @property
    def SourceSpan(self) -> Microsoft.Scripting.SourceSpan:
        ...
    @SourceSpan.setter
    def SourceSpan(self, val: Microsoft.Scripting.SourceSpan):
        ...

    # methods
    def __init__(self, span: Microsoft.Scripting.SourceSpan, category: int, trigger: int, ):
        ...

    def GetHashCode(self, ) -> int:
        ...

    @typing.overload
    def Equals(self, obj: System.Object, ) -> bool:
        ...

    @typing.overload
    def Equals(self, other: Microsoft.Scripting.TokenInfo, ) -> bool:
        ...

    def ToString(self, ) -> str:
        ...

class TokenCategory(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    None_: int = ...
    EndOfStream: int = ...
    WhiteSpace: int = ...
    Comment: int = ...
    LineComment: int = ...
    DocComment: int = ...
    NumericLiteral: int = ...
    CharacterLiteral: int = ...
    StringLiteral: int = ...
    RegularExpressionLiteral: int = ...
    Keyword: int = ...
    Directive: int = ...
    Operator: int = ...
    Delimiter: int = ...
    Identifier: int = ...
    Grouping: int = ...
    Error: int = ...
    LanguageDefined: int = ...

class TokenTriggers(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    None_: int = ...
    MemberSelect: int = ...
    MatchBraces: int = ...
    ParameterStart: int = ...
    ParameterNext: int = ...
    ParameterEnd: int = ...
    Parameter: int = ...
    MethodTip: int = ...

class SourceCodeKind(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    Unspecified: int = ...
    Expression: int = ...
    Statements: int = ...
    SingleStatement: int = ...
    File: int = ...
    InteractiveCode: int = ...
    AutoDetect: int = ...

class AssemblyLoadedEventArgs(System.EventArgs):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def Assembly(self) -> System.Reflection.Assembly:
        ...

    # methods
    def __init__(self, assembly: System.Reflection.Assembly, ):
        ...

class PlatformAdaptationLayer(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields
    Default: Microsoft.Scripting.PlatformAdaptationLayer = ...
    IsCompactFramework: bool = ...

    # properties
    @property
    def IsNativeModule(self) -> bool:
        ...

    @property
    def IsSingleRootFileSystem(self) -> bool:
        ...

    @property
    def PathComparer(self) -> System.StringComparer:
        ...

    @property
    def CurrentDirectory(self) -> str:
        ...
    @CurrentDirectory.setter
    def CurrentDirectory(self, val: str):
        ...

    # methods
    def __init__(self, ):
        ...

    @staticmethod
    def _IsNativeModule() -> bool:
        ...

    def LoadAssembly(self, name: str, ) -> System.Reflection.Assembly:
        ...

    def LoadAssemblyFromPath(self, path: str, ) -> System.Reflection.Assembly:
        ...

    def TerminateScriptExecution(self, exitCode: int, ) -> None:
        ...

    def FileExists(self, path: str, ) -> bool:
        ...

    def DirectoryExists(self, path: str, ) -> bool:
        ...

    def OpenFileStream(self, path: str, mode: int = ..., access: int = ..., share: int = ..., bufferSize: int = ..., ) -> System.IO.Stream:
        ...

    def OpenInputFileStream(self, path: str, mode: int = ..., access: int = ..., share: int = ..., bufferSize: int = ..., ) -> System.IO.Stream:
        ...

    def OpenOutputFileStream(self, path: str, ) -> System.IO.Stream:
        ...

    def DeleteFile(self, path: str, deleteReadOnly: bool, ) -> None:
        ...

    def GetFiles(self, path: str, searchPattern: str, ) -> System.Array[str]:
        ...

    def GetDirectories(self, path: str, searchPattern: str, ) -> System.Array[str]:
        ...

    @typing.overload
    def GetFileSystemEntries(self, path: str, searchPattern: str, ) -> System.Array[str]:
        ...

    @typing.overload
    def GetFileSystemEntries(self, path: str, searchPattern: str, includeFiles: bool, includeDirectories: bool, ) -> System.Array[str]:
        ...

    def GetFullPath(self, path: str, ) -> str:
        ...

    def CombinePaths(self, path1: str, path2: str, ) -> str:
        ...

    def GetFileName(self, path: str, ) -> str:
        ...

    def GetDirectoryName(self, path: str, ) -> str:
        ...

    def GetExtension(self, path: str, ) -> str:
        ...

    def GetFileNameWithoutExtension(self, path: str, ) -> str:
        ...

    def IsAbsolutePath(self, path: str, ) -> bool:
        ...

    def CreateDirectory(self, path: str, ) -> None:
        ...

    def DeleteDirectory(self, path: str, recursive: bool, ) -> None:
        ...

    def MoveFileSystemEntry(self, sourcePath: str, destinationPath: str, ) -> None:
        ...

    def GetEnvironmentVariable(self, key: str, ) -> str:
        ...

    def SetEnvironmentVariable(self, key: str, value: str, ) -> None:
        ...

    @staticmethod
    def SetEmptyEnvironmentVariable(key: str, ) -> None:
        ...

    def GetEnvironmentVariables(self, ) -> System.Collections.Generic.Dictionary[str, str]:
        ...

