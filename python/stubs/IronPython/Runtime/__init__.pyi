from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import System
import System.Collections
import System.Collections.Generic
import IronPython.Runtime
import Microsoft.Scripting.Runtime
import IronPython.Runtime.Types
import System.Linq.Expressions
import System.Reflection
import Microsoft.Scripting.Actions
import Microsoft.Scripting.ComInterop
import System.Runtime.CompilerServices
import IronPython.Runtime.LiteralParser
import System.Text
import IronPython.Compiler
import IronPython.Compiler.Ast
import System.Numerics
import System.Buffers
import IronPython.Runtime.Exceptions
import Microsoft.Scripting
import System.Dynamic
import IronPython.Runtime.Binding
import IronPython.Runtime.Method
import System.Runtime.Serialization
import System.ComponentModel
import IronPython.Runtime.Profiler
import IronPython.Runtime.Operations
import System.Collections.ObjectModel
import IronPython.Runtime.FunctionCode
import System.Threading
import System.Collections.Concurrent
import IronPython.Runtime.ClrModule
import System.Globalization
import Microsoft.Scripting.Debugging.CompilerServices
import Microsoft.Scripting.Debugging
import Microsoft.Scripting.Hosting
import IronPython.Hosting
import System.IO
import System.CodeDom
import System.Text.RegularExpressions
import IronPython.Runtime.Slice
import Microsoft.Scripting.Ast
import Microsoft.Scripting.Interpreter

T0 = typing.TypeVar('T0')
T1 = typing.TypeVar('T1')
T2 = typing.TypeVar('T2')
T = typing.TypeVar('T')
T3 = typing.TypeVar('T3')
T4 = typing.TypeVar('T4')
T5 = typing.TypeVar('T5')
T6 = typing.TypeVar('T6')
T7 = typing.TypeVar('T7')
T8 = typing.TypeVar('T8')
T9 = typing.TypeVar('T9')
T10 = typing.TypeVar('T10')
T11 = typing.TypeVar('T11')
K = typing.TypeVar('K')
V = typing.TypeVar('V')
TRet = typing.TypeVar('TRet')
TService = typing.TypeVar('TService')
T12 = typing.TypeVar('T12')

class PythonHiddenBaseClassAttribute(System.Attribute):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def TypeId(self) -> System.Object:
        ...

    # methods
    def __init__(self, ):
        ...

class NameType(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    None_: int = ...
    Python: int = ...
    Method: int = ...
    PythonMethod: int = ...
    Field: int = ...
    PythonField: int = ...
    Property: int = ...
    PythonProperty: int = ...
    Event: int = ...
    PythonEvent: int = ...
    Type: int = ...
    PythonType: int = ...
    BaseTypeMask: int = ...
    ClassMember: int = ...
    ClassMethod: int = ...

class ClassMethodAttribute(System.Attribute):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def TypeId(self) -> System.Object:
        ...

    # methods
    def __init__(self, ):
        ...

class PythonTuple(System.Collections.IList, System.Collections.ICollection, System.Collections.IEnumerable, System.Collections.Generic.IList[System.Object], System.Collections.Generic.ICollection[System.Object], System.Collections.Generic.IEnumerable[System.Object], IronPython.Runtime.ICodeFormattable, Microsoft.Scripting.Runtime.IExpressionSerializable, System.Collections.IStructuralEquatable, System.Collections.Generic.IReadOnlyList[System.Object], System.Collections.Generic.IReadOnlyCollection[System.Object], System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        self._data: System.Array[System.Object]
        ...

    # static fields
    EMPTY: IronPython.Runtime.PythonTuple = ...

    # properties
    @property
    def Item(self) -> System.Object:
        ...

    @property
    def Item(self) -> System.Object:
        ...

    @property
    def Item(self) -> System.Object:
        ...

    @property
    def Item(self) -> System.Object:
        ...

    @property
    def IsSynchronized(self) -> bool:
        ...

    @property
    def Count(self) -> int:
        ...

    @property
    def SyncRoot(self) -> System.Object:
        ...

    @property
    def Item(self) -> System.Object:
        ...
    @Item.setter
    def Item(self, val: System.Object):
        ...

    @property
    def IsReadOnly(self) -> bool:
        ...

    @property
    def IsFixedSize(self) -> bool:
        ...

    @property
    def IsReadOnly(self) -> bool:
        ...

    @property
    def Item(self) -> System.Object:
        ...
    @Item.setter
    def Item(self, val: System.Object):
        ...

    # methods
    @typing.overload
    def __init__(self, o: System.Object, ):
        ...

    @typing.overload
    def __init__(self, items: System.Array[System.Object], ):
        ...

    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def __init__(self, other: IronPython.Runtime.PythonTuple, o: System.Object, ):
        ...

    def __repr__(self, context: IronPython.Runtime.CodeContext, ) -> str:
        ...

    @staticmethod
    @typing.overload
    def __new__(context: IronPython.Runtime.CodeContext, cls: IronPython.Runtime.Types.PythonType, ) -> IronPython.Runtime.PythonTuple:
        ...

    @staticmethod
    @typing.overload
    def __new__(context: IronPython.Runtime.CodeContext, cls: IronPython.Runtime.Types.PythonType, sequence: System.Object, ) -> IronPython.Runtime.PythonTuple:
        ...

    @typing.overload
    def index(self, obj: System.Object, start: System.Object, ) -> int:
        ...

    @typing.overload
    def index(self, obj: System.Object, start: int = ..., ) -> int:
        ...

    @typing.overload
    def index(self, obj: System.Object, start: System.Object, end: System.Object, ) -> int:
        ...

    @typing.overload
    def index(self, obj: System.Object, start: int, end: int, ) -> int:
        ...

    def count(self, obj: System.Object, ) -> int:
        ...

    @staticmethod
    def Make(o: System.Object, ) -> IronPython.Runtime.PythonTuple:
        ...

    @staticmethod
    def MakeTuple(items: System.Array[System.Object], ) -> IronPython.Runtime.PythonTuple:
        ...

    @staticmethod
    def MakeItems(o: System.Object, ) -> System.Array[System.Object]:
        ...

    def ToArray(self, ) -> System.Array[System.Object]:
        ...

    def __len__(self, ) -> int:
        ...

    @staticmethod
    def MultiplyWorker(self: IronPython.Runtime.PythonTuple, count: int, ) -> IronPython.Runtime.PythonTuple:
        ...

    @typing.overload
    def CopyTo(self, array: System.Array, index: int, ) -> None:
        ...

    @typing.overload
    def CopyTo(self, array: System.Array[System.Object], arrayIndex: int, ) -> None:
        ...

    def __iter__(self, ) -> System.Collections.IEnumerator:
        ...

    def GetEnumerator(self, ) -> System.Collections.IEnumerator:
        ...

    def Expand(self, value: System.Object, ) -> System.Array[System.Object]:
        ...

    def __getnewargs__(self, ) -> System.Object:
        ...

    def GetEnumerator(self, ) -> System.Collections.Generic.IEnumerator[System.Object]:
        ...

    def IndexOf(self, item: System.Object, ) -> int:
        ...

    def Insert(self, index: int, item: System.Object, ) -> None:
        ...

    def RemoveAt(self, index: int, ) -> None:
        ...

    def Add(self, item: System.Object, ) -> None:
        ...

    def Clear(self, ) -> None:
        ...

    def Contains(self, item: System.Object, ) -> bool:
        ...

    def Remove(self, item: System.Object, ) -> bool:
        ...

    def AsSpan(self, ) -> System.ReadOnlySpan[System.Object]:
        ...

    @typing.overload
    def Equals(self, other: IronPython.Runtime.PythonTuple, ) -> bool:
        ...

    @typing.overload
    def Equals(self, obj: System.Object, ) -> bool:
        ...

    @typing.overload
    def GetHashCode(self, ) -> int:
        ...

    @typing.overload
    def GetHashCode(self, dlg: IronPython.Runtime.HashDelegate, ) -> int:
        ...

    @typing.overload
    def GetHashCode(self, comparer: System.Collections.IEqualityComparer, ) -> int:
        ...

    def ToString(self, ) -> str:
        ...

    def GetHashCode(self, comparer: System.Collections.IEqualityComparer, ) -> int:
        ...

    def Equals(self, other: System.Object, comparer: System.Collections.IEqualityComparer, ) -> bool:
        ...

    def Add(self, value: System.Object, ) -> int:
        ...

    def Clear(self, ) -> None:
        ...

    def Insert(self, index: int, value: System.Object, ) -> None:
        ...

    def Remove(self, value: System.Object, ) -> None:
        ...

    def RemoveAt(self, index: int, ) -> None:
        ...

    def CreateExpression(self, ) -> System.Linq.Expressions.Expression:
        ...

class ClrModule(System.Object, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields
    IsNetCoreApp: bool = ...
    IsDebug: bool = ...

    # properties
    @property
    def TargetFramework(self) -> str:
        ...

    @property
    def FileVersion(self) -> str:
        ...

    @property
    def FrameworkDescription(self) -> str:
        ...

    @property
    def IsMono(self) -> bool:
        ...

    @property
    def Reference(self) -> IronPython.Runtime.Types.PythonType:
        ...

    @property
    def StrongBox(self) -> IronPython.Runtime.Types.PythonType:
        ...

    # methods
    @staticmethod
    def GetCurrentRuntime(context: IronPython.Runtime.CodeContext, ) -> Microsoft.Scripting.Runtime.ScriptDomainManager:
        ...

    @staticmethod
    @typing.overload
    def AddReference(context: IronPython.Runtime.CodeContext, references: System.Array[System.Object], ) -> None:
        ...

    @staticmethod
    @typing.overload
    def AddReference(context: IronPython.Runtime.CodeContext, reference: System.Object, ) -> None:
        ...

    @staticmethod
    @typing.overload
    def AddReference(context: IronPython.Runtime.CodeContext, assembly: System.Reflection.Assembly, ) -> None:
        ...

    @staticmethod
    @typing.overload
    def AddReference(context: IronPython.Runtime.CodeContext, name: str, ) -> None:
        ...

    @staticmethod
    @typing.overload
    def AddReferenceToFile(context: IronPython.Runtime.CodeContext, files: System.Array[str], ) -> None:
        ...

    @staticmethod
    @typing.overload
    def AddReferenceToFile(context: IronPython.Runtime.CodeContext, file: str, ) -> None:
        ...

    @staticmethod
    @typing.overload
    def AddReferenceByName(context: IronPython.Runtime.CodeContext, names: System.Array[str], ) -> None:
        ...

    @staticmethod
    @typing.overload
    def AddReferenceByName(context: IronPython.Runtime.CodeContext, name: str, ) -> None:
        ...

    @staticmethod
    @typing.overload
    def AddReferenceByPartialName(context: IronPython.Runtime.CodeContext, names: System.Array[str], ) -> None:
        ...

    @staticmethod
    @typing.overload
    def AddReferenceByPartialName(context: IronPython.Runtime.CodeContext, name: str, ) -> None:
        ...

    @staticmethod
    def LoadAssemblyFromFileWithPath(context: IronPython.Runtime.CodeContext, file: str, ) -> System.Reflection.Assembly:
        ...

    @staticmethod
    def LoadAssemblyFromFile(context: IronPython.Runtime.CodeContext, file: str, ) -> System.Reflection.Assembly:
        ...

    @staticmethod
    def LoadAssemblyByPartialName(name: str, ) -> System.Reflection.Assembly:
        ...

    @staticmethod
    def LoadAssemblyByName(context: IronPython.Runtime.CodeContext, name: str, ) -> System.Reflection.Assembly:
        ...

    @staticmethod
    @typing.overload
    def Use(context: IronPython.Runtime.CodeContext, name: str, ) -> System.Object:
        ...

    @staticmethod
    @typing.overload
    def Use(context: IronPython.Runtime.CodeContext, path: str, language: str, ) -> System.Object:
        ...

    @staticmethod
    @typing.overload
    def GetString(bytes: System.Array[int], ) -> str:
        ...

    @staticmethod
    @typing.overload
    def GetString(bytes: System.Array[int], maxCount: int, ) -> str:
        ...

    @staticmethod
    @typing.overload
    def GetBytes(s: str, ) -> System.Array[int]:
        ...

    @staticmethod
    @typing.overload
    def GetBytes(s: str, maxCount: int, ) -> System.Array[int]:
        ...

    @staticmethod
    def SetCommandDispatcher(context: IronPython.Runtime.CodeContext, dispatcher: System.Action[System.Action], ) -> System.Action[System.Action]:
        ...

    @staticmethod
    @typing.overload
    def ImportExtensions(context: IronPython.Runtime.CodeContext, type: IronPython.Runtime.Types.PythonType, ) -> None:
        ...

    @staticmethod
    @typing.overload
    def ImportExtensions(context: IronPython.Runtime.CodeContext, namespace: Microsoft.Scripting.Actions.NamespaceTracker, ) -> None:
        ...

    @staticmethod
    @typing.overload
    def LoadTypeLibrary(context: IronPython.Runtime.CodeContext, rcw: System.Object, ) -> Microsoft.Scripting.ComInterop.ComTypeLibInfo:
        ...

    @staticmethod
    @typing.overload
    def LoadTypeLibrary(context: IronPython.Runtime.CodeContext, typeLibGuid: System.Guid, ) -> Microsoft.Scripting.ComInterop.ComTypeLibInfo:
        ...

    @staticmethod
    @typing.overload
    def AddReferenceToTypeLibrary(context: IronPython.Runtime.CodeContext, rcw: System.Object, ) -> None:
        ...

    @staticmethod
    @typing.overload
    def AddReferenceToTypeLibrary(context: IronPython.Runtime.CodeContext, typeLibGuid: System.Guid, ) -> None:
        ...

    @staticmethod
    def PublishTypeLibDesc(context: IronPython.Runtime.CodeContext, typeLibDesc: Microsoft.Scripting.ComInterop.ComTypeLibDesc, ) -> None:
        ...

    @staticmethod
    @typing.overload
    def AddReferenceToFileAndPath(context: IronPython.Runtime.CodeContext, files: System.Array[str], ) -> None:
        ...

    @staticmethod
    @typing.overload
    def AddReferenceToFileAndPath(context: IronPython.Runtime.CodeContext, file: str, ) -> None:
        ...

    @staticmethod
    def GetClrType(type: System.Type, ) -> System.Type:
        ...

    @staticmethod
    def GetPythonType(t: System.Type, ) -> IronPython.Runtime.Types.PythonType:
        ...

    @staticmethod
    def GetDynamicType(t: System.Type, ) -> IronPython.Runtime.Types.PythonType:
        ...

    @staticmethod
    def accepts(types: System.Array[System.Object], ) -> System.Object:
        ...

    @staticmethod
    def returns(type: System.Object, ) -> System.Object:
        ...

    @staticmethod
    def Self() -> System.Object:
        ...

    @staticmethod
    def Dir(o: System.Object, ) -> IronPython.Runtime.PythonList:
        ...

    @staticmethod
    def DirClr(o: System.Object, ) -> IronPython.Runtime.PythonList:
        ...

    @staticmethod
    def Convert(context: IronPython.Runtime.CodeContext, o: System.Object, toType: System.Type, ) -> System.Object:
        ...

    @staticmethod
    def CompileModules(context: IronPython.Runtime.CodeContext, assemblyName: str, kwArgs: System.Collections.Generic.IDictionary[str, System.Object], filenames: System.Array[str], ) -> None:
        ...

    @staticmethod
    def CompileSubclassTypes(assemblyName: str, newTypes: System.Array[System.Object], ) -> None:
        ...

    @staticmethod
    def GetSubclassedTypes() -> IronPython.Runtime.PythonTuple:
        ...

    @staticmethod
    def BuildPackageMap(filenames: System.Array[str], ) -> System.Collections.Generic.Dictionary[str, str]:
        ...

    @staticmethod
    def SortModules(modules: System.Collections.Generic.List[str], ) -> None:
        ...

    @staticmethod
    def GetProfilerData(context: IronPython.Runtime.CodeContext, includeUnused: bool = ..., ) -> IronPython.Runtime.PythonTuple:
        ...

    @staticmethod
    def ClearProfilerData(context: IronPython.Runtime.CodeContext, ) -> None:
        ...

    @staticmethod
    def EnableProfiler(context: IronPython.Runtime.CodeContext, enable: bool, ) -> None:
        ...

    @staticmethod
    def Serialize(self: System.Object, ) -> IronPython.Runtime.PythonTuple:
        ...

    @staticmethod
    def Deserialize(serializationFormat: str, data: str, ) -> System.Object:
        ...

class ItemEnumerable(System.Collections.IEnumerable, System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    def __init__(self, source: System.Object, getitem: System.Object, site: System.Runtime.CompilerServices.CallSite[System.Func[System.Runtime.CompilerServices.CallSite, IronPython.Runtime.CodeContext, System.Object, int, System.Object]], ):
        ...

    def __iter__(self, ) -> System.Collections.IEnumerator:
        ...

    def GetEnumerator(self, ) -> System.Collections.IEnumerator:
        ...

class staticmethod(IronPython.Runtime.Types.PythonTypeSlot):
    @typing.overload
    def __init__(self, **kwargs):
        self._func: System.Object
        ...

    # static fields

    # properties
    @property
    def GetAlwaysSucceeds(self) -> bool:
        ...

    @property
    def __func__(self) -> System.Object:
        ...

    @property
    def __isabstractmethod__(self) -> bool:
        ...

    @property
    def IsAlwaysVisible(self) -> bool:
        ...

    @property
    def CanOptimizeGets(self) -> bool:
        ...

    # methods
    def __init__(self, context: IronPython.Runtime.CodeContext, func: System.Object, ):
        ...

    def __init__(self, context: IronPython.Runtime.CodeContext, func: System.Object, ) -> None:
        ...

    def TryGetValue(self, context: IronPython.Runtime.CodeContext, instance: System.Object, owner: IronPython.Runtime.Types.PythonType, value: ref[System.Object], ) -> bool:
        ...

    @typing.overload
    def __get__(self, instance: System.Object, ) -> System.Object:
        ...

    @typing.overload
    def __get__(self, instance: System.Object, owner: System.Object, ) -> System.Object:
        ...

class IBufferProtocol(abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    @abc.abstractmethod
    def GetBuffer(self, flags: int = ..., ) -> IronPython.Runtime.IPythonBuffer:
        ...

class DictionaryTypeInfoAttribute(System.Attribute):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def KeyType(self) -> System.Type:
        ...

    @property
    def ValueType(self) -> System.Type:
        ...

    @property
    def TypeId(self) -> System.Object:
        ...

    # methods
    def __init__(self, keyType: System.Type, valueType: System.Type, ):
        ...

class BytesIterator(System.Collections.IEnumerable, System.Collections.Generic.IEnumerator[int], System.IDisposable, System.Collections.IEnumerator, System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def Current(self) -> int:
        ...

    @property
    def Current(self) -> System.Object:
        ...

    # methods
    def __init__(self, bytes: System.Collections.Generic.IList[int], ):
        ...

    def __length_hint__(self, ) -> int:
        ...

    def __reduce__(self, context: IronPython.Runtime.CodeContext, ) -> IronPython.Runtime.PythonTuple:
        ...

    def __setstate__(self, state: int, ) -> None:
        ...

    def Dispose(self, ) -> None:
        ...

    def MoveNext(self, ) -> bool:
        ...

    def Reset(self, ) -> None:
        ...

    def GetEnumerator(self, ) -> System.Collections.IEnumerator:
        ...

class IReversible(abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    @abc.abstractmethod
    def __reversed__(self, ) -> System.Collections.IEnumerator:
        ...

class FunctionCaller(IronPython.Runtime.FunctionCaller, typing.Generic[T0, T1, T2]):
    @typing.overload
    def __init__(self, **kwargs):
        self._compat: int
        ...

    # static fields

    # properties
    # methods
    def __init__(self, compat: int, ):
        ...

    def Call3(self, site: System.Runtime.CompilerServices.CallSite, context: IronPython.Runtime.CodeContext, func: System.Object, arg0: T0, arg1: T1, arg2: T2, ) -> System.Object:
        ...

    def Default1Call3(self, site: System.Runtime.CompilerServices.CallSite, context: IronPython.Runtime.CodeContext, func: System.Object, arg0: T0, arg1: T1, arg2: T2, ) -> System.Object:
        ...

    def Default2Call3(self, site: System.Runtime.CompilerServices.CallSite, context: IronPython.Runtime.CodeContext, func: System.Object, arg0: T0, arg1: T1, arg2: T2, ) -> System.Object:
        ...

    def Default3Call3(self, site: System.Runtime.CompilerServices.CallSite, context: IronPython.Runtime.CodeContext, func: System.Object, arg0: T0, arg1: T1, arg2: T2, ) -> System.Object:
        ...

    def Default4Call3(self, site: System.Runtime.CompilerServices.CallSite, context: IronPython.Runtime.CodeContext, func: System.Object, arg0: T0, arg1: T1, arg2: T2, ) -> System.Object:
        ...

    def Default5Call3(self, site: System.Runtime.CompilerServices.CallSite, context: IronPython.Runtime.CodeContext, func: System.Object, arg0: T0, arg1: T1, arg2: T2, ) -> System.Object:
        ...

    def Default6Call3(self, site: System.Runtime.CompilerServices.CallSite, context: IronPython.Runtime.CodeContext, func: System.Object, arg0: T0, arg1: T1, arg2: T2, ) -> System.Object:
        ...

    def Default7Call3(self, site: System.Runtime.CompilerServices.CallSite, context: IronPython.Runtime.CodeContext, func: System.Object, arg0: T0, arg1: T1, arg2: T2, ) -> System.Object:
        ...

    def Default8Call3(self, site: System.Runtime.CompilerServices.CallSite, context: IronPython.Runtime.CodeContext, func: System.Object, arg0: T0, arg1: T1, arg2: T2, ) -> System.Object:
        ...

    def Default9Call3(self, site: System.Runtime.CompilerServices.CallSite, context: IronPython.Runtime.CodeContext, func: System.Object, arg0: T0, arg1: T1, arg2: T2, ) -> System.Object:
        ...

    def Default10Call3(self, site: System.Runtime.CompilerServices.CallSite, context: IronPython.Runtime.CodeContext, func: System.Object, arg0: T0, arg1: T1, arg2: T2, ) -> System.Object:
        ...

class ClassMethodDescriptor(IronPython.Runtime.ICodeFormattable, IronPython.Runtime.Types.PythonTypeSlot):
    @typing.overload
    def __init__(self, **kwargs):
        self._func: IronPython.Runtime.Types.BuiltinFunction
        ...

    # static fields

    # properties
    @property
    def IsAlwaysVisible(self) -> bool:
        ...

    @property
    def CanOptimizeGets(self) -> bool:
        ...

    @property
    def GetAlwaysSucceeds(self) -> bool:
        ...

    # methods
    def __init__(self, func: IronPython.Runtime.Types.BuiltinFunction, ):
        ...

    def TryGetValue(self, context: IronPython.Runtime.CodeContext, instance: System.Object, owner: IronPython.Runtime.Types.PythonType, value: ref[System.Object], ) -> bool:
        ...

    def CheckGetArgs(self, context: IronPython.Runtime.CodeContext, instance: System.Object, owner: IronPython.Runtime.Types.PythonType, ) -> IronPython.Runtime.Types.PythonType:
        ...

    def __repr__(self, context: IronPython.Runtime.CodeContext, ) -> str:
        ...

    def Equals(self, obj: System.Object, ) -> bool:
        ...

    def GetHashCode(self, ) -> int:
        ...

class LiteralParser(System.Object, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    @staticmethod
    @typing.overload
    def ParseString(text: ref[System.ReadOnlySpan[str]], isRaw: bool, ) -> str:
        ...

    @staticmethod
    @typing.overload
    def ParseString(bytes: ref[System.ReadOnlySpan[int]], isRaw: bool, errorHandler: IronPython.Runtime.LiteralParser.ParseStringErrorHandler[int], ) -> str:
        ...

    @staticmethod
    def TryFetchUnicode(name: str, val: ref[str], ) -> bool:
        ...

    @staticmethod
    def HandleEscape(data: System.ReadOnlySpan[T], i: ref[int], buf: System.Text.StringBuilder, isRaw: bool, isUniEscape: bool, isFormatted: bool, normalizeLineEndings: bool, handleError: IronPython.Runtime.LiteralParser.HandleUnicodeError[T], ) -> None:
        ...

    @staticmethod
    def DoParseString(data: System.ReadOnlySpan[T], isRaw: bool, isUniEscape: bool, normalizeLineEndings: bool, errorHandler: IronPython.Runtime.LiteralParser.ParseStringErrorHandler[T] = ..., ) -> str:
        ...

    @staticmethod
    def TryParseExpression(parser: IronPython.Compiler.Parser, data: System.ReadOnlySpan[str], expression: ref[IronPython.Compiler.Ast.Expression], error: ref[str], ) -> bool:
        ...

    @staticmethod
    def TryReadFStringValue(parser: IronPython.Compiler.Parser, data: System.ReadOnlySpan[str], consumed: ref[int], value: ref[IronPython.Compiler.Ast.Expression], error: ref[str], ) -> bool:
        ...

    @staticmethod
    def TryReadFStringConversion(data: System.ReadOnlySpan[str], consumed: ref[int], conversion: ref[str], error: ref[str], ) -> bool:
        ...

    @staticmethod
    def TryParseFString(parser: IronPython.Compiler.Parser, data: System.ReadOnlySpan[str], isRaw: bool, depth: int, consumed: ref[int], joinedStringExpression: ref[IronPython.Compiler.Ast.JoinedStringExpression], error: ref[str], ) -> bool:
        ...

    @staticmethod
    def DoParseFString(parser: IronPython.Compiler.Parser, data: System.ReadOnlySpan[str], isRaw: bool, ) -> IronPython.Compiler.Ast.JoinedStringExpression:
        ...

    @staticmethod
    def StringBuilderInit(sb: ref[System.Text.StringBuilder], data: ref[System.ReadOnlySpan[T]], toCopy: int, ) -> None:
        ...

    @staticmethod
    def ParseBytes(data: System.ReadOnlySpan[T], isRaw: bool, isAscii: bool, normalizeLineEndings: bool, errorHandler: IronPython.Runtime.LiteralParser.ParseBytesErrorHandler[T] = ..., ) -> System.Collections.Generic.List[int]:
        ...

    @staticmethod
    @typing.overload
    def HexValue(ch: str, value: ref[int], ) -> bool:
        ...

    @staticmethod
    @typing.overload
    def HexValue(ch: str, ) -> int:
        ...

    @staticmethod
    def CharValue(ch: str, b: int, ) -> int:
        ...

    @staticmethod
    def ParseInt(text: str, b: int, ret: ref[int], ) -> bool:
        ...

    @staticmethod
    def TryParseInt(text: ref[System.ReadOnlySpan[T]], start: int, length: int, b: int, value: ref[int], consumed: ref[int], ) -> bool:
        ...

    @staticmethod
    def ParseInteger(text: str, b: int, ) -> System.Object:
        ...

    @staticmethod
    def ParseIntegerSign(text: str, b: int, start: int = ..., ) -> System.Object:
        ...

    @staticmethod
    def TryParseIntegerSign(text: str, b: int, start: int, val: ref[System.Object], ) -> bool:
        ...

    @staticmethod
    def ParseIntegerStart(text: str, b: ref[int], start: ref[int], end: int, sign: ref[int], ) -> None:
        ...

    @staticmethod
    def ParseIntegerEnd(text: str, start: ref[int], end: ref[int], ) -> None:
        ...

    @staticmethod
    def ParseBigInteger(text: str, b: int, ) -> System.Numerics.BigInteger:
        ...

    @staticmethod
    def ParseBigIntegerSign(text: str, b: int, start: int = ..., ) -> System.Numerics.BigInteger:
        ...

    @staticmethod
    def TryParseBigIntegerSign(text: str, b: int, start: int, val: ref[System.Numerics.BigInteger], ) -> bool:
        ...

    @staticmethod
    def TryParseFloat(text: str, res: ref[float], replaceUnicode: bool, ) -> bool:
        ...

    @staticmethod
    def ParseFloat(text: str, ) -> float:
        ...

    @staticmethod
    def ParseFloatNoCatch(text: str, replaceUnicode: bool = ..., ) -> float:
        ...

    @staticmethod
    def ReplaceUnicodeCharacters(text: str, ) -> str:
        ...

    @staticmethod
    def ExnMalformed() -> System.Exception:
        ...

    @staticmethod
    def ParseComplex(s: str, ) -> System.Numerics.Complex:
        ...

    @staticmethod
    def ParseImaginary(text: str, ) -> System.Numerics.Complex:
        ...

class PythonModuleAttribute(IronPython.Runtime.PlatformsAttribute):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def Name(self) -> str:
        ...

    @property
    def Type(self) -> System.Type:
        ...

    @property
    def ValidPlatforms(self) -> System.Array[int]:
        ...
    @ValidPlatforms.setter
    def ValidPlatforms(self, val: System.Array[int]):
        ...

    @property
    def IsPlatformValid(self) -> bool:
        ...

    @property
    def TypeId(self) -> System.Object:
        ...

    # methods
    @typing.overload
    def __init__(self, name: str, type: System.Type, ):
        ...

    @typing.overload
    def __init__(self, name: str, type: System.Type, validPlatforms: System.Array[int], ):
        ...

    @typing.overload
    def __init__(self, name: str, type: System.Type, validPlatformFamily: int, ):
        ...

class PlatformsAttribute(System.Attribute):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields
    WindowsFamily: System.Array[int] = ...
    UnixFamily: System.Array[int] = ...

    # properties
    @property
    def ValidPlatforms(self) -> System.Array[int]:
        ...
    @ValidPlatforms.setter
    def ValidPlatforms(self, val: System.Array[int]):
        ...

    @property
    def IsPlatformValid(self) -> bool:
        ...

    @property
    def TypeId(self) -> System.Object:
        ...

    # methods
    def __init__(self, ):
        ...

    def SetValidPlatforms(self, validPlatformFamily: int, ) -> None:
        ...

class FunctionCaller(IronPython.Runtime.FunctionCaller, typing.Generic[T0, T1, T2, T3, T4, T5]):
    @typing.overload
    def __init__(self, **kwargs):
        self._compat: int
        ...

    # static fields

    # properties
    # methods
    def __init__(self, compat: int, ):
        ...

    def Call6(self, site: System.Runtime.CompilerServices.CallSite, context: IronPython.Runtime.CodeContext, func: System.Object, arg0: T0, arg1: T1, arg2: T2, arg3: T3, arg4: T4, arg5: T5, ) -> System.Object:
        ...

    def Default1Call6(self, site: System.Runtime.CompilerServices.CallSite, context: IronPython.Runtime.CodeContext, func: System.Object, arg0: T0, arg1: T1, arg2: T2, arg3: T3, arg4: T4, arg5: T5, ) -> System.Object:
        ...

    def Default2Call6(self, site: System.Runtime.CompilerServices.CallSite, context: IronPython.Runtime.CodeContext, func: System.Object, arg0: T0, arg1: T1, arg2: T2, arg3: T3, arg4: T4, arg5: T5, ) -> System.Object:
        ...

    def Default3Call6(self, site: System.Runtime.CompilerServices.CallSite, context: IronPython.Runtime.CodeContext, func: System.Object, arg0: T0, arg1: T1, arg2: T2, arg3: T3, arg4: T4, arg5: T5, ) -> System.Object:
        ...

    def Default4Call6(self, site: System.Runtime.CompilerServices.CallSite, context: IronPython.Runtime.CodeContext, func: System.Object, arg0: T0, arg1: T1, arg2: T2, arg3: T3, arg4: T4, arg5: T5, ) -> System.Object:
        ...

    def Default5Call6(self, site: System.Runtime.CompilerServices.CallSite, context: IronPython.Runtime.CodeContext, func: System.Object, arg0: T0, arg1: T1, arg2: T2, arg3: T3, arg4: T4, arg5: T5, ) -> System.Object:
        ...

    def Default6Call6(self, site: System.Runtime.CompilerServices.CallSite, context: IronPython.Runtime.CodeContext, func: System.Object, arg0: T0, arg1: T1, arg2: T2, arg3: T3, arg4: T4, arg5: T5, ) -> System.Object:
        ...

    def Default7Call6(self, site: System.Runtime.CompilerServices.CallSite, context: IronPython.Runtime.CodeContext, func: System.Object, arg0: T0, arg1: T1, arg2: T2, arg3: T3, arg4: T4, arg5: T5, ) -> System.Object:
        ...

class PythonEnumerator(System.Collections.IEnumerator, System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def Current(self) -> System.Object:
        ...

    # methods
    def __init__(self, iter: System.Object, ):
        ...

    @staticmethod
    def TryCastIEnumer(baseObject: System.Object, enumerator: ref[System.Collections.IEnumerator], ) -> bool:
        ...

    @staticmethod
    def TryCreate(baseObject: System.Object, enumerator: ref[System.Collections.IEnumerator], ) -> bool:
        ...

    @staticmethod
    def Create(baseObject: System.Object, ) -> System.Collections.IEnumerator:
        ...

    def Reset(self, ) -> None:
        ...

    def MoveNext(self, ) -> bool:
        ...

    def __iter__(self, ) -> System.Object:
        ...

class MemoryBufferWrapper(IronPython.Runtime.IPythonBuffer, System.IDisposable, System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def Object(self) -> System.Object:
        ...

    @property
    def IsReadOnly(self) -> bool:
        ...

    @property
    def Offset(self) -> int:
        ...

    @property
    def Format(self) -> str:
        ...

    @property
    def ItemCount(self) -> int:
        ...

    @property
    def ItemSize(self) -> int:
        ...

    @property
    def NumOfDims(self) -> int:
        ...

    @property
    def Shape(self) -> System.Collections.Generic.IReadOnlyList[int]:
        ...

    @property
    def Strides(self) -> System.Collections.Generic.IReadOnlyList[int]:
        ...

    @property
    def SubOffsets(self) -> System.Collections.Generic.IReadOnlyList[int]:
        ...

    # methods
    @typing.overload
    def __init__(self, memory: System.ReadOnlyMemory[int], flags: int, ):
        ...

    @typing.overload
    def __init__(self, memory: System.Memory[int], flags: int, ):
        ...

    def Dispose(self, ) -> None:
        ...

    def AsReadOnlySpan(self, ) -> System.ReadOnlySpan[int]:
        ...

    def AsSpan(self, ) -> System.Span[int]:
        ...

    def Pin(self, ) -> System.Buffers.MemoryHandle:
        ...

class FunctionCaller(IronPython.Runtime.FunctionCaller, typing.Generic[T0, T1, T2, T3, T4, T5, T6, T7, T8, T9, T10]):
    @typing.overload
    def __init__(self, **kwargs):
        self._compat: int
        ...

    # static fields

    # properties
    # methods
    def __init__(self, compat: int, ):
        ...

    def Call11(self, site: System.Runtime.CompilerServices.CallSite, context: IronPython.Runtime.CodeContext, func: System.Object, arg0: T0, arg1: T1, arg2: T2, arg3: T3, arg4: T4, arg5: T5, arg6: T6, arg7: T7, arg8: T8, arg9: T9, arg10: T10, ) -> System.Object:
        ...

    def Default1Call11(self, site: System.Runtime.CompilerServices.CallSite, context: IronPython.Runtime.CodeContext, func: System.Object, arg0: T0, arg1: T1, arg2: T2, arg3: T3, arg4: T4, arg5: T5, arg6: T6, arg7: T7, arg8: T8, arg9: T9, arg10: T10, ) -> System.Object:
        ...

    def Default2Call11(self, site: System.Runtime.CompilerServices.CallSite, context: IronPython.Runtime.CodeContext, func: System.Object, arg0: T0, arg1: T1, arg2: T2, arg3: T3, arg4: T4, arg5: T5, arg6: T6, arg7: T7, arg8: T8, arg9: T9, arg10: T10, ) -> System.Object:
        ...

class Zip(System.Collections.IEnumerator, System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def Current(self) -> System.Object:
        ...

    # methods
    def __init__(self, context: IronPython.Runtime.CodeContext, iters: System.Array[System.Object], ):
        ...

    def MoveNext(self, ) -> bool:
        ...

    def Reset(self, ) -> None:
        ...

    def __reduce__(self, ) -> IronPython.Runtime.PythonTuple:
        ...

class Index(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def Value(self) -> System.Object:
        ...

    # methods
    def __init__(self, value: System.Object, ):
        ...

class ModuleOptions(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    None_: int = ...
    ShowClsMethods: int = ...
    Optimized: int = ...
    Initialize: int = ...
    NoBuiltins: int = ...
    ModuleBuiltins: int = ...
    ExecOrEvalCode: int = ...
    SkipFirstLine: int = ...
    Interpret: int = ...
    Verbatim: int = ...
    LightThrow: int = ...
    GeneratorStop: int = ...

class PythonListIterator(System.Collections.Generic.IEnumerable[System.Object], System.Collections.IEnumerable, System.Collections.Generic.IEnumerator[System.Object], System.IDisposable, System.Collections.IEnumerator, System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def Current(self) -> System.Object:
        ...

    # methods
    def __init__(self, l: IronPython.Runtime.PythonList, ):
        ...

    def GetEnumerator(self, ) -> System.Collections.IEnumerator:
        ...

    def GetEnumerator(self, ) -> System.Collections.Generic.IEnumerator[System.Object]:
        ...

    def MoveNext(self, ) -> bool:
        ...

    def Reset(self, ) -> None:
        ...

    def Dispose(self, ) -> None:
        ...

    def __reduce__(self, context: IronPython.Runtime.CodeContext, ) -> IronPython.Runtime.PythonTuple:
        ...

    def __setstate__(self, state: int, ) -> None:
        ...

    def __length_hint__(self, ) -> int:
        ...

class PythonBufferExtensions(System.Object, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    @staticmethod
    def NumBytes(buffer: IronPython.Runtime.IPythonBuffer, ) -> int:
        ...

    @staticmethod
    def EnumerateBytes(buffer: IronPython.Runtime.IPythonBuffer, ) -> IronPython.Runtime.BufferBytesEnumerator:
        ...

    @staticmethod
    def IsCContiguous(buffer: IronPython.Runtime.IPythonBuffer, ) -> bool:
        ...

    @staticmethod
    def ToArray(buffer: IronPython.Runtime.IPythonBuffer, ) -> System.Array[int]:
        ...

    @staticmethod
    def CopyTo(buffer: IronPython.Runtime.IPythonBuffer, dest: System.Span[int], ) -> None:
        ...

    @staticmethod
    def AsUnsafeArray(buffer: IronPython.Runtime.IPythonBuffer, ) -> System.Array[int]:
        ...

class PythonGenerator(System.Collections.IEnumerator, System.Collections.Generic.IEnumerator[System.Object], System.IDisposable, IronPython.Runtime.ICodeFormattable, System.Collections.IEnumerable, IronPython.Runtime.IWeakReferenceable, System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def gi_code(self) -> IronPython.Runtime.FunctionCode:
        ...

    @property
    def gi_running(self) -> int:
        ...

    @property
    def gi_frame(self) -> IronPython.Runtime.Exceptions.TraceBackFrame:
        ...

    @property
    def __name__(self) -> str:
        ...

    @property
    def State(self) -> int:
        ...
    @State.setter
    def State(self, val: int):
        ...

    @property
    def CurrentValue(self) -> System.Object:
        ...
    @CurrentValue.setter
    def CurrentValue(self, val: System.Object):
        ...

    @property
    def FinalValue(self) -> System.Object:
        ...
    @FinalValue.setter
    def FinalValue(self, val: System.Object):
        ...

    @property
    def Context(self) -> IronPython.Runtime.CodeContext:
        ...

    @property
    def Function(self) -> IronPython.Runtime.PythonFunction:
        ...

    @property
    def Closed(self) -> bool:
        ...
    @Closed.setter
    def Closed(self, val: bool):
        ...

    @property
    def Active(self) -> bool:
        ...
    @Active.setter
    def Active(self, val: bool):
        ...

    @property
    def CanSetSysExcInfo(self) -> bool:
        ...

    @property
    def ContainsTryFinally(self) -> bool:
        ...

    @property
    def GeneratorStop(self) -> bool:
        ...

    @property
    def Current(self) -> System.Object:
        ...

    @property
    def Current(self) -> System.Object:
        ...

    # methods
    def __init__(self, function: IronPython.Runtime.PythonFunction, next: System.Func[Microsoft.Scripting.MutableTuple, System.Object], data: Microsoft.Scripting.MutableTuple, ):
        ...

    def __next__(self, ) -> System.Object:
        ...

    @typing.overload
    def throw(self, type: System.Object, ) -> System.Object:
        ...

    @typing.overload
    def throw(self, type: System.Object, value: System.Object, ) -> System.Object:
        ...

    @typing.overload
    def throw(self, type: System.Object, value: System.Object, traceback: System.Object, ) -> System.Object:
        ...

    @typing.overload
    def throw(self, type: System.Object, value: System.Object, traceback: System.Object, finalizing: bool, ) -> System.Object:
        ...

    def send(self, value: System.Object, ) -> System.Object:
        ...

    @typing.overload
    def close(self, ) -> System.Object:
        ...

    @typing.overload
    def close(self, finalizing: bool, ) -> System.Object:
        ...

    def GetDataTuple(self, ) -> Microsoft.Scripting.MutableTuple[int, System.Object]:
        ...

    @staticmethod
    def GetBigData(data: Microsoft.Scripting.MutableTuple, ) -> Microsoft.Scripting.MutableTuple[int, System.Object]:
        ...

    def Finalizer(self, ) -> None:
        ...

    def HandleFinalizerException(self, e: System.Exception, ) -> None:
        ...

    def MoveNext(self, ) -> bool:
        ...

    def SaveFunctionStack(self, done: bool, ) -> None:
        ...

    def RestoreFunctionStack(self, ) -> None:
        ...

    def MoveNextWorker(self, ) -> bool:
        ...

    def NextWorker(self, ) -> System.Object:
        ...

    def CheckSetActive(self, ) -> None:
        ...

    @staticmethod
    def AlreadyExecuting() -> None:
        ...

    def CheckThrowableAndReturnSendValue(self, ) -> System.Object:
        ...

    def CheckThrowable(self, ) -> System.Object:
        ...

    def ThrowThrowable(self, ) -> System.Object:
        ...

    def Close(self, ) -> None:
        ...

    def SuppressFinalize(self, ) -> None:
        ...

    def GetNext(self, ) -> bool:
        ...

    def __repr__(self, context: IronPython.Runtime.CodeContext, ) -> str:
        ...

    def Reset(self, ) -> None:
        ...

    def Dispose(self, ) -> None:
        ...

    def GetEnumerator(self, ) -> System.Collections.IEnumerator:
        ...

    def GetWeakRef(self, ) -> IronPython.Runtime.WeakRefTracker:
        ...

    def SetWeakRef(self, value: IronPython.Runtime.WeakRefTracker, ) -> bool:
        ...

    def SetFinalizer(self, value: IronPython.Runtime.WeakRefTracker, ) -> None:
        ...

class DictionaryValueEnumerator(System.Collections.Generic.IEnumerator[System.Object], System.IDisposable, System.Collections.IEnumerator, System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def Current(self) -> System.Object:
        ...

    @property
    def Current(self) -> System.Object:
        ...

    # methods
    def __init__(self, dict: IronPython.Runtime.DictionaryStorage, ):
        ...

    def MoveNext(self, ) -> bool:
        ...

    def Reset(self, ) -> None:
        ...

    def Dispose(self, ) -> None:
        ...

    def __iter__(self, ) -> System.Object:
        ...

    def __len__(self, ) -> int:
        ...

    def __reduce__(self, context: IronPython.Runtime.CodeContext, ) -> System.Object:
        ...

class DictionaryKeyEnumerator(System.Collections.Generic.IEnumerator[System.Object], System.IDisposable, System.Collections.IEnumerator, System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def Current(self) -> System.Object:
        ...

    @property
    def Current(self) -> System.Object:
        ...

    # methods
    def __init__(self, dict: IronPython.Runtime.DictionaryStorage, ):
        ...

    def MoveNext(self, ) -> bool:
        ...

    def Reset(self, ) -> None:
        ...

    def Dispose(self, ) -> None:
        ...

    def __iter__(self, ) -> System.Object:
        ...

    def __length_hint__(self, ) -> int:
        ...

    def __reduce__(self, context: IronPython.Runtime.CodeContext, ) -> System.Object:
        ...

class WeakRefTracker(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def HandlerCount(self) -> int:
        ...

    # methods
    @typing.overload
    def __init__(self, target: IronPython.Runtime.IWeakReferenceable, ):
        ...

    @typing.overload
    def __init__(self, target: IronPython.Runtime.IWeakReferenceable, callback: System.Object, weakRef: System.Object, ):
        ...

    def ChainCallback(self, callback: System.Object, weakRef: System.Object, ) -> None:
        ...

    def RemoveHandlerAt(self, index: int, ) -> None:
        ...

    def RemoveHandler(self, o: System.Object, ) -> None:
        ...

    def Contains(self, callback: System.Object, weakref: System.Object, ) -> bool:
        ...

    def GetHandlerCallback(self, index: int, ) -> System.Object:
        ...

    def GetWeakRef(self, index: int, ) -> System.Object:
        ...

    def Finalize(self, ) -> None:
        ...

class PythonTypeAttribute(System.Attribute):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def Name(self) -> str:
        ...

    @property
    def TypeId(self) -> System.Object:
        ...

    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def __init__(self, name: str, ):
        ...

class BytesLikeAttribute(System.Attribute):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def TypeId(self) -> System.Object:
        ...

    # methods
    def __init__(self, ):
        ...

class IPythonMembersList(Microsoft.Scripting.Runtime.IMembersList, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    @abc.abstractmethod
    def GetMemberNames(self, context: IronPython.Runtime.CodeContext, ) -> System.Collections.Generic.IList[System.Object]:
        ...

class VersionInfo(System.Collections.IList, System.Collections.ICollection, System.Collections.IEnumerable, System.Collections.Generic.IList[System.Object], System.Collections.Generic.ICollection[System.Object], System.Collections.Generic.IEnumerable[System.Object], IronPython.Runtime.ICodeFormattable, Microsoft.Scripting.Runtime.IExpressionSerializable, System.Collections.IStructuralEquatable, System.Collections.Generic.IReadOnlyList[System.Object], System.Collections.Generic.IReadOnlyCollection[System.Object], IronPython.Runtime.PythonTuple):
    @typing.overload
    def __init__(self, **kwargs):
        self.major: int
        self.minor: int
        self.micro: int
        self.releaselevel: str
        self.serial: int
        self._data: System.Array[System.Object]
        ...

    # static fields

    # properties
    @property
    def Instance(self) -> IronPython.Runtime.VersionInfo:
        ...

    @property
    def Item(self) -> System.Object:
        ...

    @property
    def Item(self) -> System.Object:
        ...

    @property
    def Item(self) -> System.Object:
        ...

    @property
    def Item(self) -> System.Object:
        ...

    @property
    def Count(self) -> int:
        ...

    # methods
    def __init__(self, major: int, minor: int, micro: int, releaselevel: str, serial: int, ):
        ...

    def __repr__(self, context: IronPython.Runtime.CodeContext, ) -> str:
        ...

    def GetHexVersion(self, ) -> int:
        ...

    def GetVersionString(self, ) -> str:
        ...

class ListGenericWrapper(System.Collections.Generic.IList[T], System.Collections.Generic.ICollection[T], System.Collections.Generic.IEnumerable[T], System.Collections.IEnumerable, System.Object, typing.Generic[T]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def Item(self) -> T:
        ...
    @Item.setter
    def Item(self, val: T):
        ...

    @property
    def Count(self) -> int:
        ...

    @property
    def IsReadOnly(self) -> bool:
        ...

    # methods
    def __init__(self, value: System.Collections.Generic.IList[System.Object], ):
        ...

    def IndexOf(self, item: T, ) -> int:
        ...

    def Insert(self, index: int, item: T, ) -> None:
        ...

    def RemoveAt(self, index: int, ) -> None:
        ...

    def Add(self, item: T, ) -> None:
        ...

    def Clear(self, ) -> None:
        ...

    def Contains(self, item: T, ) -> bool:
        ...

    def CopyTo(self, array: System.Array[T], arrayIndex: int, ) -> None:
        ...

    def Remove(self, item: T, ) -> bool:
        ...

    def GetEnumerator(self, ) -> System.Collections.Generic.IEnumerator[T]:
        ...

    def GetEnumerator(self, ) -> System.Collections.IEnumerator:
        ...

class IEnumerableOfTWrapper(System.Collections.Generic.IEnumerable[T], System.Collections.IEnumerable, System.Object, typing.Generic[T]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    def __init__(self, enumerable: System.Collections.IEnumerable, ):
        ...

    def GetEnumerator(self, ) -> System.Collections.Generic.IEnumerator[T]:
        ...

    def GetEnumerator(self, ) -> System.Collections.IEnumerator:
        ...

class PythonList(System.Collections.IList, System.Collections.ICollection, System.Collections.IEnumerable, IronPython.Runtime.ICodeFormattable, System.Collections.Generic.IList[System.Object], System.Collections.Generic.ICollection[System.Object], System.Collections.Generic.IEnumerable[System.Object], IronPython.Runtime.IReversible, System.Collections.IStructuralEquatable, System.Collections.Generic.IReadOnlyList[System.Object], System.Collections.Generic.IReadOnlyCollection[System.Object], System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        self._size: int
        self._data: System.Array[System.Object]
        ...

    # static fields
    __hash__: System.Object = ...

    # properties
    @property
    def Item(self) -> System.Object:
        ...
    @Item.setter
    def Item(self, val: System.Object):
        ...

    @property
    def IsReadOnly(self) -> bool:
        ...

    @property
    def Item(self) -> System.Object:
        ...
    @Item.setter
    def Item(self, val: System.Object):
        ...

    @property
    def Item(self) -> System.Object:
        ...
    @Item.setter
    def Item(self, val: System.Object):
        ...

    @property
    def Item(self) -> System.Object:
        ...
    @Item.setter
    def Item(self, val: System.Object):
        ...

    @property
    def IsFixedSize(self) -> bool:
        ...

    @property
    def IsSynchronized(self) -> bool:
        ...

    @property
    def Count(self) -> int:
        ...

    @property
    def SyncRoot(self) -> System.Object:
        ...

    @property
    def IsReadOnly(self) -> bool:
        ...

    # methods
    @typing.overload
    def __init__(self, e: System.Collections.IEnumerator, ):
        ...

    @typing.overload
    def __init__(self, capacity: int, ):
        ...

    @typing.overload
    def __init__(self, items: System.Array[System.Object], ):
        ...

    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def __init__(self, sequence: System.Object, ):
        ...

    @typing.overload
    def __init__(self, items: System.Collections.ICollection, ):
        ...

    def GetData(self, ) -> System.Array[System.Object]:
        ...

    def RemoveAt(self, index: int, ) -> None:
        ...

    def Contains(self, value: System.Object, ) -> bool:
        ...

    def Clear(self, ) -> None:
        ...

    def IndexOf(self, value: System.Object, ) -> int:
        ...

    def Add(self, value: System.Object, ) -> int:
        ...

    @typing.overload
    def CopyTo(self, array: System.Array, index: int, ) -> None:
        ...

    @typing.overload
    def CopyTo(self, array: System.Array, index: int, arrayIndex: int, count: int, ) -> None:
        ...

    @typing.overload
    def CopyTo(self, array: System.Array[System.Object], arrayIndex: int, ) -> None:
        ...

    def GetEnumerator(self, ) -> System.Collections.IEnumerator:
        ...

    def __repr__(self, context: IronPython.Runtime.CodeContext, ) -> str:
        ...

    def GetHashCode(self, comparer: System.Collections.IEqualityComparer, ) -> int:
        ...

    def Equals(self, other: System.Object, comparer: System.Collections.IEqualityComparer, ) -> bool:
        ...

    def Add(self, item: System.Object, ) -> None:
        ...

    def Remove(self, item: System.Object, ) -> bool:
        ...

    def GetEnumerator(self, ) -> System.Collections.Generic.IEnumerator[System.Object]:
        ...

    def AsSpan(self, ) -> System.Span[System.Object]:
        ...

    def Equals(self, other: IronPython.Runtime.PythonList, comparer: System.Collections.IEqualityComparer = ..., ) -> bool:
        ...

    @typing.overload
    def __init__(self, ) -> None:
        ...

    @typing.overload
    def __init__(self, enumerable: System.Collections.IEnumerable, ) -> None:
        ...

    @typing.overload
    def __init__(self, sequence: System.Collections.ICollection, ) -> None:
        ...

    @typing.overload
    def __init__(self, sequence: IronPython.Runtime.SetCollection, ) -> None:
        ...

    @typing.overload
    def __init__(self, sequence: IronPython.Runtime.FrozenSetCollection, ) -> None:
        ...

    @typing.overload
    def __init__(self, sequence: IronPython.Runtime.PythonList, ) -> None:
        ...

    @typing.overload
    def __init__(self, sequence: str, ) -> None:
        ...

    @typing.overload
    def __init__(self, context: IronPython.Runtime.CodeContext, sequence: System.Object, ) -> None:
        ...

    @staticmethod
    @typing.overload
    def __new__(context: IronPython.Runtime.CodeContext, cls: IronPython.Runtime.Types.PythonType, ) -> System.Object:
        ...

    @staticmethod
    @typing.overload
    def __new__(context: IronPython.Runtime.CodeContext, cls: IronPython.Runtime.Types.PythonType, arg: System.Object, ) -> System.Object:
        ...

    @staticmethod
    @typing.overload
    def __new__(context: IronPython.Runtime.CodeContext, cls: IronPython.Runtime.Types.PythonType, argsø: System.Array[System.Object], ) -> System.Object:
        ...

    @staticmethod
    @typing.overload
    def __new__(context: IronPython.Runtime.CodeContext, cls: IronPython.Runtime.Types.PythonType, kwArgsø: System.Collections.Generic.IDictionary[System.Object, System.Object], argsø: System.Array[System.Object], ) -> System.Object:
        ...

    @staticmethod
    def FromArrayNoCopy(data: System.Array[System.Object], ) -> IronPython.Runtime.PythonList:
        ...

    def GetObjectArray(self, ) -> System.Array[System.Object]:
        ...

    @staticmethod
    def GetAddSize(s1: int, s2: int, ) -> int:
        ...

    @staticmethod
    def GetNewSize(length: int, ) -> int:
        ...

    @staticmethod
    def MultiplyWorker(self: IronPython.Runtime.PythonList, count: int, ) -> IronPython.Runtime.PythonList:
        ...

    def __len__(self, ) -> int:
        ...

    def __iter__(self, ) -> System.Collections.IEnumerator:
        ...

    def __reversed__(self, ) -> System.Collections.IEnumerator:
        ...

    def __contains__(self, value: System.Object, ) -> bool:
        ...

    def ContainsWorker(self, value: System.Object, ) -> bool:
        ...

    def AddRange(self, otherList: System.Collections.Generic.ICollection[T], ) -> None:
        ...

    @staticmethod
    def InPlaceMultiplyWorker(self: IronPython.Runtime.PythonList, count: int, ) -> IronPython.Runtime.PythonList:
        ...

    def GetSliceAsArray(self, start: int, stop: int, ) -> System.Array[System.Object]:
        ...

    @staticmethod
    def ValueRequiresNoLocks(value: System.Object, ) -> bool:
        ...

    @typing.overload
    def SliceNoStep(self, start: int, stop: int, other: IronPython.Runtime.PythonList, ) -> None:
        ...

    @typing.overload
    def SliceNoStep(self, start: int, stop: int, value: System.Object, ) -> None:
        ...

    def SliceAssign(self, index: int, value: System.Object, ) -> None:
        ...

    def SliceAssignNoLock(self, index: int, value: System.Object, ) -> None:
        ...

    @typing.overload
    def __delitem__(self, index: int, ) -> None:
        ...

    @typing.overload
    def __delitem__(self, index: System.Object, ) -> None:
        ...

    @typing.overload
    def __delitem__(self, slice: IronPython.Runtime.Slice, ) -> None:
        ...

    def RawDelete(self, index: int, ) -> None:
        ...

    def EnsureSize(self, needed: int, ) -> None:
        ...

    def append(self, item: System.Object, ) -> None:
        ...

    def AddNoLock(self, item: System.Object, ) -> None:
        ...

    def AddNoLockNoDups(self, item: System.Object, ) -> None:
        ...

    def AppendListNoLockNoDups(self, list: IronPython.Runtime.PythonList, ) -> None:
        ...

    def clear(self, ) -> None:
        ...

    def count(self, item: System.Object, ) -> int:
        ...

    @typing.overload
    def extend(self, seq: IronPython.Runtime.PythonList, ) -> None:
        ...

    @typing.overload
    def extend(self, seq: IronPython.Runtime.PythonTuple, ) -> None:
        ...

    @typing.overload
    def extend(self, seq: System.Object, ) -> None:
        ...

    def ExtendNoLengthCheck(self, seq: System.Object, ) -> None:
        ...

    @typing.overload
    def index(self, item: System.Object, ) -> int:
        ...

    @typing.overload
    def index(self, item: System.Object, start: int, ) -> int:
        ...

    @typing.overload
    def index(self, item: System.Object, start: int, stop: int, ) -> int:
        ...

    @typing.overload
    def index(self, item: System.Object, start: System.Object, ) -> int:
        ...

    @typing.overload
    def index(self, item: System.Object, start: System.Object, stop: System.Object, ) -> int:
        ...

    def insert(self, index: int, value: System.Object, ) -> None:
        ...

    def Insert(self, index: int, value: System.Object, ) -> None:
        ...

    @typing.overload
    def pop(self, ) -> System.Object:
        ...

    @typing.overload
    def pop(self, index: int, ) -> System.Object:
        ...

    def remove(self, value: System.Object, ) -> None:
        ...

    def Remove(self, value: System.Object, ) -> None:
        ...

    @typing.overload
    def reverse(self, ) -> None:
        ...

    @typing.overload
    def reverse(self, index: int, count: int, ) -> None:
        ...

    def sort(self, context: IronPython.Runtime.CodeContext, kwArgs: System.Collections.Generic.IDictionary[str, System.Object], ) -> None:
        ...

    def Sort(self, context: IronPython.Runtime.CodeContext, key: System.Object = ..., reverse: bool = ..., ) -> None:
        ...

    def GetComparisonType(self, ) -> System.Type:
        ...

    def DoSort(self, context: IronPython.Runtime.CodeContext, cmp: System.Collections.IComparer, key: System.Object, reverse: bool, index: int, count: int, ) -> None:
        ...

    def ListMergeSort(self, sortData: System.Array[System.Object], keys: System.Array[System.Object], cmp: System.Collections.IComparer, index: int, count: int, reverse: bool, ) -> System.Array[System.Object]:
        ...

    def DoCompare(self, keys: System.Array[System.Object], cmp: System.Collections.IComparer, p: int, q: int, reverse: bool, ) -> bool:
        ...

    def BinarySearch(self, index: int, count: int, value: System.Object, comparer: System.Collections.IComparer, ) -> int:
        ...

    def FastSwap(self, i: int, j: int, ) -> bool:
        ...

    def copy(self, ) -> IronPython.Runtime.PythonList:
        ...

class DictionaryOps(System.Object, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    @staticmethod
    def __repr__(context: IronPython.Runtime.CodeContext, self: System.Collections.Generic.IDictionary[System.Object, System.Object], ) -> str:
        ...

    @staticmethod
    def get(self: IronPython.Runtime.PythonDictionary, key: System.Object, defaultValue: System.Object = ..., ) -> System.Object:
        ...

    @staticmethod
    def ToList(self: System.Collections.Generic.IDictionary[System.Object, System.Object], ) -> IronPython.Runtime.PythonList:
        ...

    @staticmethod
    @typing.overload
    def pop(self: IronPython.Runtime.PythonDictionary, key: System.Object, ) -> System.Object:
        ...

    @staticmethod
    @typing.overload
    def pop(self: IronPython.Runtime.PythonDictionary, key: System.Object, defaultValue: System.Object, ) -> System.Object:
        ...

    @staticmethod
    def popitem(self: System.Collections.Generic.IDictionary[System.Object, System.Object], ) -> IronPython.Runtime.PythonTuple:
        ...

    @staticmethod
    @typing.overload
    def setdefault(self: IronPython.Runtime.PythonDictionary, key: System.Object, ) -> System.Object:
        ...

    @staticmethod
    @typing.overload
    def setdefault(self: IronPython.Runtime.PythonDictionary, key: System.Object, defaultValue: System.Object, ) -> System.Object:
        ...

    @staticmethod
    def update(context: IronPython.Runtime.CodeContext, self: IronPython.Runtime.PythonDictionary, other: System.Object, ) -> None:
        ...

    @staticmethod
    def SlowUpdate(context: IronPython.Runtime.CodeContext, self: IronPython.Runtime.PythonDictionary, other: System.Object, ) -> None:
        ...

    @staticmethod
    def TryGetValueVirtual(context: IronPython.Runtime.CodeContext, self: IronPython.Runtime.PythonDictionary, key: System.Object, DefaultGetItem: ref[System.Object], value: ref[System.Object], ) -> bool:
        ...

    @staticmethod
    def AddKeyValue(self: IronPython.Runtime.PythonDictionary, o: System.Object, ) -> bool:
        ...

class Method(IronPython.Runtime.IWeakReferenceable, IronPython.Runtime.IPythonMembersList, Microsoft.Scripting.Runtime.IMembersList, System.Dynamic.IDynamicMetaObjectProvider, IronPython.Runtime.ICodeFormattable, IronPython.Runtime.Binding.IFastInvokable, IronPython.Runtime.Types.PythonTypeSlot):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def Name(self) -> str:
        ...

    @property
    def __doc__(self) -> str:
        ...

    @property
    def __func__(self) -> System.Object:
        ...

    @property
    def __self__(self) -> System.Object:
        ...

    @property
    def im_class(self) -> IronPython.Runtime.Types.PythonType:
        ...

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
    @typing.overload
    def __init__(self, function: System.Object, instance: System.Object, class: IronPython.Runtime.Types.PythonType, ):
        ...

    @typing.overload
    def __init__(self, function: System.Object, self: System.Object, ):
        ...

    def DeclaringClassAsString(self, ) -> str:
        ...

    def Equals(self, obj: System.Object, ) -> bool:
        ...

    def GetHashCode(self, ) -> int:
        ...

    def GetWeakRef(self, ) -> IronPython.Runtime.WeakRefTracker:
        ...

    def SetWeakRef(self, value: IronPython.Runtime.WeakRefTracker, ) -> bool:
        ...

    def SetFinalizer(self, value: IronPython.Runtime.WeakRefTracker, ) -> None:
        ...

    def GetMemberNames(self, ) -> System.Collections.Generic.IList[str]:
        ...

    def GetMemberNames(self, context: IronPython.Runtime.CodeContext, ) -> System.Collections.Generic.IList[System.Object]:
        ...

    def TryGetValue(self, context: IronPython.Runtime.CodeContext, instance: System.Object, owner: IronPython.Runtime.Types.PythonType, value: ref[System.Object], ) -> bool:
        ...

    def __repr__(self, context: IronPython.Runtime.CodeContext, ) -> str:
        ...

    def GetMetaObject(self, parameter: System.Linq.Expressions.Expression, ) -> System.Dynamic.DynamicMetaObject:
        ...

    def MakeInvokeBinding(self, site: System.Runtime.CompilerServices.CallSite[T], binder: IronPython.Runtime.Binding.PythonInvokeBinder, context: IronPython.Runtime.CodeContext, args: System.Array[System.Object], ) -> IronPython.Runtime.Binding.FastBindResult[T]:
        ...

    @staticmethod
    def GetMethodBinding(binder: IronPython.Runtime.Binding.PythonInvokeBinder, typeArgs: System.Array[System.Type], binding: IronPython.Runtime.Method.BaseMethodBinding, ) -> IronPython.Runtime.Method.BaseMethodBinding:
        ...

    @staticmethod
    def GetTypeArgs() -> System.Array[System.Type]:
        ...

    @staticmethod
    def GetSelfBinder(binder: IronPython.Runtime.Binding.PythonInvokeBinder, context: IronPython.Runtime.CodeContext, ) -> IronPython.Runtime.Binding.PythonInvokeBinder:
        ...

class PythonEnumerable(System.Collections.IEnumerable, System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    def __init__(self, iterator: System.Object, ):
        ...

    @staticmethod
    def TryCreate(baseEnumerator: System.Object, enumerator: ref[System.Collections.IEnumerable], ) -> bool:
        ...

    @staticmethod
    def Create(baseObject: System.Object, ) -> System.Collections.IEnumerable:
        ...

    def GetEnumerator(self, ) -> System.Collections.IEnumerator:
        ...

class KwCallInfo(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def Arguments(self) -> System.Array[System.Object]:
        ...

    @property
    def Names(self) -> System.Array[str]:
        ...

    # methods
    def __init__(self, args: System.Array[System.Object], names: System.Array[str], ):
        ...

class Symbols(System.Object, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    @staticmethod
    def OperatorToSymbol(op: int, ) -> str:
        ...

    @staticmethod
    def OperatorToReversedSymbol(op: int, ) -> str:
        ...

    @staticmethod
    def OperatorToReverseOperator(op: int, ) -> int:
        ...

class UnboundNameException(System.Runtime.Serialization.ISerializable, System.Exception):
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
    def __init__(self, msg: str, ):
        ...

    @typing.overload
    def __init__(self, message: str, innerException: System.Exception, ):
        ...

    @typing.overload
    def __init__(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext, ):
        ...

class ReversedEnumerator(System.Collections.Generic.IEnumerator[System.Object], System.IDisposable, System.Collections.IEnumerator, System.Collections.Generic.IEnumerable[System.Object], System.Collections.IEnumerable, System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def Current(self) -> System.Object:
        ...
    @Current.setter
    def Current(self, val: System.Object):
        ...

    # methods
    def __init__(self, length: int, obj: System.Object, getitem: System.Object, ):
        ...

    @staticmethod
    @typing.overload
    def __new__(context: IronPython.Runtime.CodeContext, type: IronPython.Runtime.Types.PythonType, o: IronPython.Runtime.IReversible, ) -> System.Object:
        ...

    @staticmethod
    @typing.overload
    def __new__(context: IronPython.Runtime.CodeContext, type: IronPython.Runtime.Types.PythonType, o: System.Object, ) -> System.Object:
        ...

    def __length_hint__(self, ) -> int:
        ...

    def __iter__(self, ) -> IronPython.Runtime.ReversedEnumerator:
        ...

    def __reduce__(self, ) -> IronPython.Runtime.PythonTuple:
        ...

    def __setstate__(self, position: int, ) -> None:
        ...

    def GetEnumerator(self, ) -> System.Collections.IEnumerator:
        ...

    def GetEnumerator(self, ) -> System.Collections.Generic.IEnumerator[System.Object]:
        ...

    def MoveNext(self, ) -> bool:
        ...

    def Reset(self, ) -> None:
        ...

    def Dispose(self, ) -> None:
        ...

class PythonDictionary(System.Collections.Generic.IDictionary[System.Object, System.Object], System.Collections.Generic.ICollection[System.Collections.Generic.KeyValuePair[System.Object, System.Object]], System.Collections.Generic.IEnumerable[System.Collections.Generic.KeyValuePair[System.Object, System.Object]], System.Collections.IEnumerable, System.Collections.IDictionary, System.Collections.ICollection, IronPython.Runtime.ICodeFormattable, System.Collections.IStructuralEquatable, System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        self._storage: IronPython.Runtime.DictionaryStorage
        ...

    # static fields
    __hash__: System.Object = ...

    # properties
    @property
    def Keys(self) -> System.Collections.Generic.ICollection[System.Object]:
        ...

    @property
    def Values(self) -> System.Collections.Generic.ICollection[System.Object]:
        ...

    @property
    def Count(self) -> int:
        ...

    @property
    def IsReadOnly(self) -> bool:
        ...

    @property
    def Item(self) -> System.Object:
        ...
    @Item.setter
    def Item(self, val: System.Object):
        ...

    @property
    def Item(self) -> System.Object:
        ...
    @Item.setter
    def Item(self, val: System.Object):
        ...

    @property
    def IsFixedSize(self) -> bool:
        ...

    @property
    def IsReadOnly(self) -> bool:
        ...

    @property
    def Keys(self) -> System.Collections.ICollection:
        ...

    @property
    def Values(self) -> System.Collections.ICollection:
        ...

    @property
    def IsSynchronized(self) -> bool:
        ...

    @property
    def SyncRoot(self) -> System.Object:
        ...

    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def __init__(self, storage: IronPython.Runtime.DictionaryStorage, ):
        ...

    @typing.overload
    def __init__(self, dict: System.Collections.IDictionary, ):
        ...

    @typing.overload
    def __init__(self, dict: System.Collections.Generic.IDictionary[System.Object, System.Object], ):
        ...

    @typing.overload
    def __init__(self, dict: IronPython.Runtime.PythonDictionary, ):
        ...

    @typing.overload
    def __init__(self, context: IronPython.Runtime.CodeContext, o: System.Object, ):
        ...

    @typing.overload
    def __init__(self, size: int, ):
        ...

    @staticmethod
    def MakeDict(context: IronPython.Runtime.CodeContext, cls: IronPython.Runtime.Types.PythonType, ) -> System.Object:
        ...

    @staticmethod
    def FromIAC(context: IronPython.Runtime.CodeContext, iac: IronPython.Runtime.PythonDictionary, ) -> IronPython.Runtime.PythonDictionary:
        ...

    @staticmethod
    def MakeDictFromIAC(context: IronPython.Runtime.CodeContext, iac: IronPython.Runtime.PythonDictionary, ) -> IronPython.Runtime.PythonDictionary:
        ...

    @staticmethod
    @typing.overload
    def MakeSymbolDictionary() -> IronPython.Runtime.PythonDictionary:
        ...

    @staticmethod
    @typing.overload
    def MakeSymbolDictionary(count: int, ) -> IronPython.Runtime.PythonDictionary:
        ...

    @typing.overload
    def __init__(self, context: IronPython.Runtime.CodeContext, oø: System.Object, kwArgs: System.Collections.Generic.IDictionary[System.Object, System.Object], ) -> None:
        ...

    @typing.overload
    def __init__(self, context: IronPython.Runtime.CodeContext, kwArgs: System.Collections.Generic.IDictionary[System.Object, System.Object], ) -> None:
        ...

    @typing.overload
    def __init__(self, context: IronPython.Runtime.CodeContext, oø: System.Object, ) -> None:
        ...

    @typing.overload
    def __init__(self, ) -> None:
        ...

    @typing.overload
    def Add(self, key: System.Object, value: System.Object, ) -> None:
        ...

    @typing.overload
    def Add(self, item: System.Collections.Generic.KeyValuePair[System.Object, System.Object], ) -> None:
        ...

    def ContainsKey(self, key: System.Object, ) -> bool:
        ...

    @typing.overload
    def Remove(self, key: System.Object, ) -> bool:
        ...

    @typing.overload
    def Remove(self, item: System.Collections.Generic.KeyValuePair[System.Object, System.Object], ) -> bool:
        ...

    def RemoveDirect(self, key: System.Object, ) -> bool:
        ...

    def TryGetValue(self, key: System.Object, value: ref[System.Object], ) -> bool:
        ...

    def TryGetValueNoMissing(self, key: System.Object, value: ref[System.Object], ) -> bool:
        ...

    def Clear(self, ) -> None:
        ...

    @typing.overload
    def Contains(self, item: System.Collections.Generic.KeyValuePair[System.Object, System.Object], ) -> bool:
        ...

    @typing.overload
    def Contains(self, key: System.Object, ) -> bool:
        ...

    def CopyTo(self, array: System.Array[System.Collections.Generic.KeyValuePair[System.Object, System.Object]], arrayIndex: int, ) -> None:
        ...

    def GetEnumerator(self, ) -> System.Collections.Generic.IEnumerator[System.Collections.Generic.KeyValuePair[System.Object, System.Object]]:
        ...

    def GetEnumerator(self, ) -> System.Collections.IEnumerator:
        ...

    def __iter__(self, ) -> System.Object:
        ...

    @typing.overload
    def get(self, key: System.Object, ) -> System.Object:
        ...

    @typing.overload
    def get(self, key: System.Object, defaultValue: System.Object, ) -> System.Object:
        ...

    def SetItem(self, key: System.Object, value: System.Object, ) -> None:
        ...

    def GetItem(self, key: System.Object, ) -> System.Object:
        ...

    @typing.overload
    def __delitem__(self, key: System.Object, ) -> None:
        ...

    @typing.overload
    def __delitem__(self, key: System.Array[System.Object], ) -> None:
        ...

    def __len__(self, ) -> int:
        ...

    def clear(self, ) -> None:
        ...

    @typing.overload
    def pop(self, key: System.Object, ) -> System.Object:
        ...

    @typing.overload
    def pop(self, key: System.Object, defaultValue: System.Object, ) -> System.Object:
        ...

    def popitem(self, ) -> IronPython.Runtime.PythonTuple:
        ...

    @typing.overload
    def setdefault(self, key: System.Object, ) -> System.Object:
        ...

    @typing.overload
    def setdefault(self, key: System.Object, defaultValue: System.Object, ) -> System.Object:
        ...

    def items(self, ) -> IronPython.Runtime.DictionaryItemView:
        ...

    def keys(self, ) -> IronPython.Runtime.DictionaryKeyView:
        ...

    def values(self, ) -> IronPython.Runtime.DictionaryValueView:
        ...

    @typing.overload
    def update(self, ) -> None:
        ...

    @typing.overload
    def update(self, context: IronPython.Runtime.CodeContext, otherø: System.Collections.Generic.IDictionary[System.Object, System.Object], ) -> None:
        ...

    @typing.overload
    def update(self, context: IronPython.Runtime.CodeContext, otherø: System.Object, ) -> None:
        ...

    @typing.overload
    def update(self, context: IronPython.Runtime.CodeContext, otherø: System.Object, otherArgsø: System.Collections.Generic.IDictionary[System.Object, System.Object], ) -> None:
        ...

    @staticmethod
    def fromkeysAny(context: IronPython.Runtime.CodeContext, cls: IronPython.Runtime.Types.PythonType, o: System.Object, value: System.Object, ) -> System.Object:
        ...

    @staticmethod
    @typing.overload
    def fromkeys(context: IronPython.Runtime.CodeContext, cls: IronPython.Runtime.Types.PythonType, seq: System.Object, ) -> System.Object:
        ...

    @staticmethod
    @typing.overload
    def fromkeys(context: IronPython.Runtime.CodeContext, cls: IronPython.Runtime.Types.PythonType, seq: System.Object, value: System.Object, ) -> System.Object:
        ...

    def copy(self, context: IronPython.Runtime.CodeContext, ) -> IronPython.Runtime.PythonDictionary:
        ...

    def __contains__(self, key: System.Object, ) -> bool:
        ...

    def __eq__(self, context: IronPython.Runtime.CodeContext, other: System.Object, ) -> System.Object:
        ...

    def __ne__(self, context: IronPython.Runtime.CodeContext, other: System.Object, ) -> System.Object:
        ...

    def __gt__(self, context: IronPython.Runtime.CodeContext, other: System.Object, ) -> IronPython.Runtime.Types.NotImplementedType:
        ...

    def __lt__(self, context: IronPython.Runtime.CodeContext, other: System.Object, ) -> IronPython.Runtime.Types.NotImplementedType:
        ...

    def __ge__(self, context: IronPython.Runtime.CodeContext, other: System.Object, ) -> IronPython.Runtime.Types.NotImplementedType:
        ...

    def __le__(self, context: IronPython.Runtime.CodeContext, other: System.Object, ) -> IronPython.Runtime.Types.NotImplementedType:
        ...

    def GetHashCode(self, comparer: System.Collections.IEqualityComparer, ) -> int:
        ...

    def Equals(self, other: System.Object, comparer: System.Collections.IEqualityComparer, ) -> bool:
        ...

    def EqualsWorker(self, other: System.Object, comparer: System.Collections.IEqualityComparer, ) -> bool:
        ...

    def ValueEqualsPythonDict(self, pd: IronPython.Runtime.PythonDictionary, comparer: System.Collections.IEqualityComparer, ) -> bool:
        ...

    def GetEnumerator(self, ) -> System.Collections.IDictionaryEnumerator:
        ...

    def Remove(self, key: System.Object, ) -> None:
        ...

    def CopyTo(self, array: System.Array, index: int, ) -> None:
        ...

    def __repr__(self, context: IronPython.Runtime.CodeContext, ) -> str:
        ...

    def TryRemoveValue(self, key: System.Object, value: ref[System.Object], ) -> bool:
        ...

class PythonProperty(IronPython.Runtime.Types.PythonTypeDataSlot):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def GetAlwaysSucceeds(self) -> bool:
        ...

    @property
    def __isabstractmethod__(self) -> bool:
        ...

    @property
    def fdel(self) -> System.Object:
        ...
    @fdel.setter
    def fdel(self, val: System.Object):
        ...

    @property
    def fset(self) -> System.Object:
        ...
    @fset.setter
    def fset(self, val: System.Object):
        ...

    @property
    def fget(self) -> System.Object:
        ...
    @fget.setter
    def fget(self, val: System.Object):
        ...

    @property
    def IsAlwaysVisible(self) -> bool:
        ...

    @property
    def CanOptimizeGets(self) -> bool:
        ...

    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def __init__(self, args: System.Array[System.Object], ):
        ...

    @typing.overload
    def __init__(self, dict: System.Collections.Generic.IDictionary[System.Object, System.Object], args: System.Array[System.Object], ):
        ...

    def __init__(self, fget: System.Object = ..., fset: System.Object = ..., fdel: System.Object = ..., doc: System.Object = ..., ) -> None:
        ...

    def TryGetValue(self, context: IronPython.Runtime.CodeContext, instance: System.Object, owner: IronPython.Runtime.Types.PythonType, value: ref[System.Object], ) -> bool:
        ...

    def TrySetValue(self, context: IronPython.Runtime.CodeContext, instance: System.Object, owner: IronPython.Runtime.Types.PythonType, value: System.Object, ) -> bool:
        ...

    def TryDeleteValue(self, context: IronPython.Runtime.CodeContext, instance: System.Object, owner: IronPython.Runtime.Types.PythonType, ) -> bool:
        ...

    def __get__(self, context: IronPython.Runtime.CodeContext, instance: System.Object, owner: System.Object = ..., ) -> System.Object:
        ...

    def __set__(self, context: IronPython.Runtime.CodeContext, instance: System.Object, value: System.Object, ) -> None:
        ...

    def __delete__(self, context: IronPython.Runtime.CodeContext, instance: System.Object, ) -> None:
        ...

    def getter(self, fget: System.Object, ) -> IronPython.Runtime.PythonProperty:
        ...

    def setter(self, fset: System.Object, ) -> IronPython.Runtime.PythonProperty:
        ...

    def deleter(self, fdel: System.Object, ) -> IronPython.Runtime.PythonProperty:
        ...

class IWeakReferenceableByProxy(abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    @abc.abstractmethod
    def GetWeakRefProxy(self, context: IronPython.Runtime.PythonContext, ) -> IronPython.Runtime.IWeakReferenceable:
        ...

class ByteArray(System.Collections.Generic.IList[int], System.Collections.Generic.ICollection[int], System.Collections.Generic.IEnumerable[int], System.Collections.IEnumerable, System.Collections.Generic.IReadOnlyList[int], System.Collections.Generic.IReadOnlyCollection[int], IronPython.Runtime.ICodeFormattable, IronPython.Runtime.IBufferProtocol, System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields
    __hash__: System.Object = ...

    # properties
    @property
    def UnsafeByteList(self) -> IronPython.Runtime.ArrayData[int]:
        ...

    @property
    def Item(self) -> System.Object:
        ...
    @Item.setter
    def Item(self, val: System.Object):
        ...

    @property
    def Item(self) -> System.Object:
        ...
    @Item.setter
    def Item(self, val: System.Object):
        ...

    @property
    def Item(self) -> System.Object:
        ...
    @Item.setter
    def Item(self, val: System.Object):
        ...

    @property
    def Item(self) -> System.Object:
        ...
    @Item.setter
    def Item(self, val: System.Object):
        ...

    @property
    def Item(self) -> int:
        ...
    @Item.setter
    def Item(self, val: int):
        ...

    @property
    def Item(self) -> int:
        ...

    @property
    def Count(self) -> int:
        ...

    @property
    def IsReadOnly(self) -> bool:
        ...

    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def __init__(self, bytes: IronPython.Runtime.ArrayData[int], ):
        ...

    @typing.overload
    def __init__(self, bytes: System.ReadOnlySpan[int], ):
        ...

    @typing.overload
    def __init__(self, bytes: System.Collections.Generic.IEnumerable[int], ):
        ...

    @staticmethod
    def JoinOne(curVal: System.Object, ) -> IronPython.Runtime.ByteArray:
        ...

    def CopyThis(self, ) -> IronPython.Runtime.ByteArray:
        ...

    def SliceNoStep(self, start: int, stop: int, other: System.Collections.Generic.IList[int], ) -> None:
        ...

    def IndexOf(self, item: int, ) -> int:
        ...

    def Insert(self, index: int, item: int, ) -> None:
        ...

    def RemoveAt(self, index: int, ) -> None:
        ...

    def Add(self, item: int, ) -> None:
        ...

    def Clear(self, ) -> None:
        ...

    def Contains(self, item: int, ) -> bool:
        ...

    def CopyTo(self, array: System.Array[int], arrayIndex: int, ) -> None:
        ...

    def Remove(self, item: int, ) -> bool:
        ...

    def GetEnumerator(self, ) -> System.Collections.Generic.IEnumerator[int]:
        ...

    def GetEnumerator(self, ) -> System.Collections.IEnumerator:
        ...

    @typing.overload
    def __eq__(self, context: IronPython.Runtime.CodeContext, value: IronPython.Runtime.ByteArray, ) -> bool:
        ...

    @typing.overload
    def __eq__(self, context: IronPython.Runtime.CodeContext, value: IronPython.Runtime.MemoryView, ) -> bool:
        ...

    @typing.overload
    def __eq__(self, context: IronPython.Runtime.CodeContext, value: IronPython.Runtime.IBufferProtocol, ) -> bool:
        ...

    @typing.overload
    def __eq__(self, context: IronPython.Runtime.CodeContext, value: str, ) -> bool:
        ...

    @typing.overload
    def __eq__(self, context: IronPython.Runtime.CodeContext, value: Microsoft.Scripting.Runtime.Extensible[str], ) -> bool:
        ...

    @typing.overload
    def __eq__(self, context: IronPython.Runtime.CodeContext, value: System.Object, ) -> IronPython.Runtime.Types.NotImplementedType:
        ...

    @typing.overload
    def __ne__(self, context: IronPython.Runtime.CodeContext, value: IronPython.Runtime.ByteArray, ) -> bool:
        ...

    @typing.overload
    def __ne__(self, context: IronPython.Runtime.CodeContext, value: IronPython.Runtime.MemoryView, ) -> bool:
        ...

    @typing.overload
    def __ne__(self, context: IronPython.Runtime.CodeContext, value: IronPython.Runtime.IBufferProtocol, ) -> bool:
        ...

    @typing.overload
    def __ne__(self, context: IronPython.Runtime.CodeContext, value: str, ) -> bool:
        ...

    @typing.overload
    def __ne__(self, context: IronPython.Runtime.CodeContext, value: Microsoft.Scripting.Runtime.Extensible[str], ) -> bool:
        ...

    @typing.overload
    def __ne__(self, context: IronPython.Runtime.CodeContext, value: System.Object, ) -> IronPython.Runtime.Types.NotImplementedType:
        ...

    @typing.overload
    def Equals(self, other: IronPython.Runtime.ByteArray, ) -> bool:
        ...

    @typing.overload
    def Equals(self, other: System.Collections.Generic.IList[int], ) -> bool:
        ...

    @typing.overload
    def Equals(self, other: System.ReadOnlySpan[int], ) -> bool:
        ...

    def GetBuffer(self, flags: int, ) -> IronPython.Runtime.IPythonBuffer:
        ...

    def isupper(self, ) -> bool:
        ...

    @typing.overload
    def join(self, sequence: System.Object, ) -> IronPython.Runtime.ByteArray:
        ...

    @typing.overload
    def join(self, sequence: IronPython.Runtime.PythonList, ) -> IronPython.Runtime.ByteArray:
        ...

    @typing.overload
    def ljust(self, width: int, ) -> IronPython.Runtime.ByteArray:
        ...

    @typing.overload
    def ljust(self, width: int, fillchar: System.Collections.Generic.IList[int], ) -> IronPython.Runtime.ByteArray:
        ...

    @typing.overload
    def ljust(self, width: int, fillchar: int, ) -> IronPython.Runtime.ByteArray:
        ...

    def lower(self, ) -> IronPython.Runtime.ByteArray:
        ...

    @typing.overload
    def lstrip(self, ) -> IronPython.Runtime.ByteArray:
        ...

    @typing.overload
    def lstrip(self, chars: System.Collections.Generic.IList[int], ) -> IronPython.Runtime.ByteArray:
        ...

    @staticmethod
    def maketrans(from_: System.Collections.Generic.IList[int], to: System.Collections.Generic.IList[int], ) -> IronPython.Runtime.Bytes:
        ...

    def partition(self, sep: System.Collections.Generic.IList[int], ) -> IronPython.Runtime.PythonTuple:
        ...

    @typing.overload
    def replace(self, old: System.Collections.Generic.IList[int], new: System.Collections.Generic.IList[int], ) -> IronPython.Runtime.ByteArray:
        ...

    @typing.overload
    def replace(self, old: System.Collections.Generic.IList[int], new: System.Collections.Generic.IList[int], count: int, ) -> IronPython.Runtime.ByteArray:
        ...

    @typing.overload
    def rfind(self, sub: System.Collections.Generic.IList[int], ) -> int:
        ...

    @typing.overload
    def rfind(self, sub: System.Collections.Generic.IList[int], start: int, ) -> int:
        ...

    @typing.overload
    def rfind(self, sub: System.Collections.Generic.IList[int], start: int, end: int, ) -> int:
        ...

    @typing.overload
    def rfind(self, sub: System.Collections.Generic.IList[int], start: System.Object, ) -> int:
        ...

    @typing.overload
    def rfind(self, sub: System.Collections.Generic.IList[int], start: System.Object, end: System.Object, ) -> int:
        ...

    @typing.overload
    def rfind(self, byte: System.Numerics.BigInteger, ) -> int:
        ...

    @typing.overload
    def rfind(self, byte: System.Numerics.BigInteger, start: int, ) -> int:
        ...

    @typing.overload
    def rfind(self, byte: System.Numerics.BigInteger, start: int, end: int, ) -> int:
        ...

    @typing.overload
    def rfind(self, byte: System.Numerics.BigInteger, start: System.Object, ) -> int:
        ...

    @typing.overload
    def rfind(self, byte: System.Numerics.BigInteger, start: System.Object, end: System.Object, ) -> int:
        ...

    @typing.overload
    def rindex(self, sub: System.Collections.Generic.IList[int], ) -> int:
        ...

    @typing.overload
    def rindex(self, sub: System.Collections.Generic.IList[int], start: int, ) -> int:
        ...

    @typing.overload
    def rindex(self, sub: System.Collections.Generic.IList[int], start: int, end: int, ) -> int:
        ...

    @typing.overload
    def rindex(self, sub: System.Collections.Generic.IList[int], start: System.Object, ) -> int:
        ...

    @typing.overload
    def rindex(self, sub: System.Collections.Generic.IList[int], start: System.Object, end: System.Object, ) -> int:
        ...

    @typing.overload
    def rindex(self, byte: System.Numerics.BigInteger, ) -> int:
        ...

    @typing.overload
    def rindex(self, byte: System.Numerics.BigInteger, start: int, ) -> int:
        ...

    @typing.overload
    def rindex(self, byte: System.Numerics.BigInteger, start: int, end: int, ) -> int:
        ...

    @typing.overload
    def rindex(self, byte: System.Numerics.BigInteger, start: System.Object, ) -> int:
        ...

    @typing.overload
    def rindex(self, byte: System.Numerics.BigInteger, start: System.Object, end: System.Object, ) -> int:
        ...

    @typing.overload
    def rjust(self, width: int, ) -> IronPython.Runtime.ByteArray:
        ...

    @typing.overload
    def rjust(self, width: int, fillchar: System.Collections.Generic.IList[int], ) -> IronPython.Runtime.ByteArray:
        ...

    @typing.overload
    def rjust(self, width: int, fillchar: int, ) -> IronPython.Runtime.ByteArray:
        ...

    def rpartition(self, sep: System.Collections.Generic.IList[int], ) -> IronPython.Runtime.PythonTuple:
        ...

    def rsplit(self, sep: System.Collections.Generic.IList[int] = ..., maxsplit: int = ..., ) -> IronPython.Runtime.PythonList:
        ...

    @typing.overload
    def rstrip(self, ) -> IronPython.Runtime.ByteArray:
        ...

    @typing.overload
    def rstrip(self, chars: System.Collections.Generic.IList[int], ) -> IronPython.Runtime.ByteArray:
        ...

    def split(self, sep: System.Collections.Generic.IList[int] = ..., maxsplit: int = ..., ) -> IronPython.Runtime.PythonList:
        ...

    @typing.overload
    def splitlines(self, ) -> IronPython.Runtime.PythonList:
        ...

    @typing.overload
    def splitlines(self, keepends: bool, ) -> IronPython.Runtime.PythonList:
        ...

    @typing.overload
    def startswith(self, prefix: System.Collections.Generic.IList[int], ) -> bool:
        ...

    @typing.overload
    def startswith(self, prefix: System.Collections.Generic.IList[int], start: int, ) -> bool:
        ...

    @typing.overload
    def startswith(self, prefix: System.Collections.Generic.IList[int], start: int, end: int, ) -> bool:
        ...

    @typing.overload
    def startswith(self, prefix: System.Collections.Generic.IList[int], start: System.Object, ) -> bool:
        ...

    @typing.overload
    def startswith(self, prefix: System.Collections.Generic.IList[int], start: System.Object, end: System.Object, ) -> bool:
        ...

    @typing.overload
    def startswith(self, prefix: IronPython.Runtime.PythonTuple, ) -> bool:
        ...

    @typing.overload
    def startswith(self, prefix: IronPython.Runtime.PythonTuple, start: int, ) -> bool:
        ...

    @typing.overload
    def startswith(self, prefix: IronPython.Runtime.PythonTuple, start: int, end: int, ) -> bool:
        ...

    @typing.overload
    def startswith(self, prefix: IronPython.Runtime.PythonTuple, start: System.Object, ) -> bool:
        ...

    @typing.overload
    def startswith(self, prefix: IronPython.Runtime.PythonTuple, start: System.Object, end: System.Object, ) -> bool:
        ...

    @typing.overload
    def startswith(self, prefix: System.Object, start: System.Object = ..., end: System.Object = ..., ) -> bool:
        ...

    @typing.overload
    def strip(self, ) -> IronPython.Runtime.ByteArray:
        ...

    @typing.overload
    def strip(self, chars: System.Collections.Generic.IList[int], ) -> IronPython.Runtime.ByteArray:
        ...

    def swapcase(self, ) -> IronPython.Runtime.ByteArray:
        ...

    def title(self, ) -> IronPython.Runtime.ByteArray:
        ...

    def ValidateTable(self, table: System.Collections.Generic.IList[int], ) -> None:
        ...

    @typing.overload
    def translate(self, table: System.Collections.Generic.IList[int], ) -> IronPython.Runtime.ByteArray:
        ...

    @typing.overload
    def translate(self, table: System.Collections.Generic.IList[int], delete: System.Collections.Generic.IList[int], ) -> IronPython.Runtime.ByteArray:
        ...

    @typing.overload
    def translate(self, table: System.Collections.Generic.IList[int], delete: System.Object, ) -> IronPython.Runtime.ByteArray:
        ...

    def upper(self, ) -> IronPython.Runtime.ByteArray:
        ...

    def zfill(self, width: int, ) -> IronPython.Runtime.ByteArray:
        ...

    def __alloc__(self, ) -> int:
        ...

    @typing.overload
    def __contains__(self, bytes: System.Collections.Generic.IList[int], ) -> bool:
        ...

    @typing.overload
    def __contains__(self, value: int, ) -> bool:
        ...

    @typing.overload
    def __contains__(self, context: IronPython.Runtime.CodeContext, value: System.Object, ) -> bool:
        ...

    def __iter__(self, ) -> System.Collections.Generic.IEnumerator[int]:
        ...

    def __reduce__(self, context: IronPython.Runtime.CodeContext, ) -> IronPython.Runtime.PythonTuple:
        ...

    def Repr(self, ) -> str:
        ...

    def __mod__(self, context: IronPython.Runtime.CodeContext, value: System.Object, ) -> IronPython.Runtime.ByteArray:
        ...

    @typing.overload
    def __rmod__(self, context: IronPython.Runtime.CodeContext, value: IronPython.Runtime.ByteArray, ) -> IronPython.Runtime.ByteArray:
        ...

    @typing.overload
    def __rmod__(self, context: IronPython.Runtime.CodeContext, value: System.Object, ) -> IronPython.Runtime.Types.NotImplementedType:
        ...

    def __str__(self, context: IronPython.Runtime.CodeContext, ) -> str:
        ...

    def __repr__(self, context: IronPython.Runtime.CodeContext, ) -> str:
        ...

    def ToString(self, ) -> str:
        ...

    @staticmethod
    def TypeErrorForConcat(self: System.Object, other: System.Object, ) -> System.Exception:
        ...

    @staticmethod
    def MultiplyWorker(self: IronPython.Runtime.ByteArray, count: int, ) -> IronPython.Runtime.ByteArray:
        ...

    @typing.overload
    def __init__(self, ) -> None:
        ...

    @typing.overload
    def __init__(self, source: int, ) -> None:
        ...

    @typing.overload
    def __init__(self, source: IronPython.Runtime.IBufferProtocol, ) -> None:
        ...

    @typing.overload
    def __init__(self, context: IronPython.Runtime.CodeContext, source: System.Object, ) -> None:
        ...

    @typing.overload
    def __init__(self, string: str, ) -> None:
        ...

    @typing.overload
    def __init__(self, context: IronPython.Runtime.CodeContext, source: str, encoding: str, errors: str = ..., ) -> None:
        ...

    @typing.overload
    def append(self, item: int, ) -> None:
        ...

    @typing.overload
    def append(self, item: System.Object, ) -> None:
        ...

    @typing.overload
    def extend(self, seq: System.Collections.Generic.IEnumerable[int], ) -> None:
        ...

    @typing.overload
    def extend(self, context: IronPython.Runtime.CodeContext, seq: System.Object, ) -> None:
        ...

    @typing.overload
    def insert(self, index: int, value: int, ) -> None:
        ...

    @typing.overload
    def insert(self, index: int, value: System.Object, ) -> None:
        ...

    @typing.overload
    def pop(self, ) -> int:
        ...

    @typing.overload
    def pop(self, index: int, ) -> int:
        ...

    def RemoveByte(self, value: int, ) -> None:
        ...

    @typing.overload
    def remove(self, value: int, ) -> None:
        ...

    @typing.overload
    def remove(self, value: System.Object, ) -> None:
        ...

    def reverse(self, ) -> None:
        ...

    def capitalize(self, ) -> IronPython.Runtime.ByteArray:
        ...

    @typing.overload
    def center(self, width: int, ) -> IronPython.Runtime.ByteArray:
        ...

    @typing.overload
    def center(self, width: int, fillchar: System.Collections.Generic.IList[int], ) -> IronPython.Runtime.ByteArray:
        ...

    @typing.overload
    def center(self, width: int, fillchar: int, ) -> IronPython.Runtime.ByteArray:
        ...

    def clear(self, ) -> None:
        ...

    def copy(self, ) -> IronPython.Runtime.ByteArray:
        ...

    @typing.overload
    def count(self, sub: System.Collections.Generic.IList[int], ) -> int:
        ...

    @typing.overload
    def count(self, sub: System.Collections.Generic.IList[int], start: int, ) -> int:
        ...

    @typing.overload
    def count(self, sub: System.Collections.Generic.IList[int], start: int, end: int, ) -> int:
        ...

    @typing.overload
    def count(self, sub: System.Collections.Generic.IList[int], start: System.Object, ) -> int:
        ...

    @typing.overload
    def count(self, sub: System.Collections.Generic.IList[int], start: System.Object, end: System.Object, ) -> int:
        ...

    @typing.overload
    def count(self, byte: System.Numerics.BigInteger, ) -> int:
        ...

    @typing.overload
    def count(self, byte: System.Numerics.BigInteger, start: int, ) -> int:
        ...

    @typing.overload
    def count(self, byte: System.Numerics.BigInteger, start: int, end: int, ) -> int:
        ...

    @typing.overload
    def count(self, byte: System.Numerics.BigInteger, start: System.Object, ) -> int:
        ...

    @typing.overload
    def count(self, byte: System.Numerics.BigInteger, start: System.Object, end: System.Object, ) -> int:
        ...

    @typing.overload
    def decode(self, context: IronPython.Runtime.CodeContext, encoding: str = ..., errors: str = ..., ) -> str:
        ...

    @typing.overload
    def decode(self, context: IronPython.Runtime.CodeContext, encoding: System.Text.Encoding, errors: str = ..., ) -> str:
        ...

    @typing.overload
    def endswith(self, suffix: System.Collections.Generic.IList[int], ) -> bool:
        ...

    @typing.overload
    def endswith(self, suffix: System.Collections.Generic.IList[int], start: int, ) -> bool:
        ...

    @typing.overload
    def endswith(self, suffix: System.Collections.Generic.IList[int], start: int, end: int, ) -> bool:
        ...

    @typing.overload
    def endswith(self, suffix: System.Collections.Generic.IList[int], start: System.Object, ) -> bool:
        ...

    @typing.overload
    def endswith(self, suffix: System.Collections.Generic.IList[int], start: System.Object, end: System.Object, ) -> bool:
        ...

    @typing.overload
    def endswith(self, suffix: IronPython.Runtime.PythonTuple, ) -> bool:
        ...

    @typing.overload
    def endswith(self, suffix: IronPython.Runtime.PythonTuple, start: int, ) -> bool:
        ...

    @typing.overload
    def endswith(self, suffix: IronPython.Runtime.PythonTuple, start: int, end: int, ) -> bool:
        ...

    @typing.overload
    def endswith(self, suffix: IronPython.Runtime.PythonTuple, start: System.Object, ) -> bool:
        ...

    @typing.overload
    def endswith(self, suffix: IronPython.Runtime.PythonTuple, start: System.Object, end: System.Object, ) -> bool:
        ...

    @typing.overload
    def endswith(self, suffix: System.Object, start: System.Object = ..., end: System.Object = ..., ) -> bool:
        ...

    @typing.overload
    def expandtabs(self, ) -> IronPython.Runtime.ByteArray:
        ...

    @typing.overload
    def expandtabs(self, tabsize: int, ) -> IronPython.Runtime.ByteArray:
        ...

    @typing.overload
    def find(self, sub: System.Collections.Generic.IList[int], ) -> int:
        ...

    @typing.overload
    def find(self, sub: System.Collections.Generic.IList[int], start: int, ) -> int:
        ...

    @typing.overload
    def find(self, sub: System.Collections.Generic.IList[int], start: int, end: int, ) -> int:
        ...

    @typing.overload
    def find(self, sub: System.Collections.Generic.IList[int], start: System.Object, ) -> int:
        ...

    @typing.overload
    def find(self, sub: System.Collections.Generic.IList[int], start: System.Object, end: System.Object, ) -> int:
        ...

    @typing.overload
    def find(self, byte: System.Numerics.BigInteger, ) -> int:
        ...

    @typing.overload
    def find(self, byte: System.Numerics.BigInteger, start: int, ) -> int:
        ...

    @typing.overload
    def find(self, byte: System.Numerics.BigInteger, start: int, end: int, ) -> int:
        ...

    @typing.overload
    def find(self, byte: System.Numerics.BigInteger, start: System.Object, ) -> int:
        ...

    @typing.overload
    def find(self, byte: System.Numerics.BigInteger, start: System.Object, end: System.Object, ) -> int:
        ...

    @staticmethod
    def fromhex(string: str, ) -> IronPython.Runtime.ByteArray:
        ...

    def hex(self, ) -> str:
        ...

    @typing.overload
    def index(self, sub: System.Collections.Generic.IList[int], ) -> int:
        ...

    @typing.overload
    def index(self, sub: System.Collections.Generic.IList[int], start: int, ) -> int:
        ...

    @typing.overload
    def index(self, sub: System.Collections.Generic.IList[int], start: int, end: int, ) -> int:
        ...

    @typing.overload
    def index(self, sub: System.Collections.Generic.IList[int], start: System.Object, ) -> int:
        ...

    @typing.overload
    def index(self, sub: System.Collections.Generic.IList[int], start: System.Object, end: System.Object, ) -> int:
        ...

    @typing.overload
    def index(self, byte: System.Numerics.BigInteger, ) -> int:
        ...

    @typing.overload
    def index(self, byte: System.Numerics.BigInteger, start: int, ) -> int:
        ...

    @typing.overload
    def index(self, byte: System.Numerics.BigInteger, start: int, end: int, ) -> int:
        ...

    @typing.overload
    def index(self, byte: System.Numerics.BigInteger, start: System.Object, ) -> int:
        ...

    @typing.overload
    def index(self, byte: System.Numerics.BigInteger, start: System.Object, end: System.Object, ) -> int:
        ...

    def isalnum(self, ) -> bool:
        ...

    def isalpha(self, ) -> bool:
        ...

    def isdigit(self, ) -> bool:
        ...

    def islower(self, ) -> bool:
        ...

    def isspace(self, ) -> bool:
        ...

    def istitle(self, ) -> bool:
        ...

class PythonHiddenAttribute(IronPython.Runtime.PlatformsAttribute):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def ValidPlatforms(self) -> System.Array[int]:
        ...
    @ValidPlatforms.setter
    def ValidPlatforms(self, val: System.Array[int]):
        ...

    @property
    def IsPlatformValid(self) -> bool:
        ...

    @property
    def TypeId(self) -> System.Object:
        ...

    # methods
    @typing.overload
    def __init__(self, hiddenPlatforms: System.Array[int], ):
        ...

    @typing.overload
    def __init__(self, hiddenPlatformFamily: int, ):
        ...

    @staticmethod
    def IsHidden(m: System.Reflection.MemberInfo, inherit: bool = ..., ) -> bool:
        ...

class IParameterSequence(abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    @abc.abstractmethod
    def Item(self) -> System.Object:
        ...

    @property
    @abc.abstractmethod
    def Count(self) -> int:
        ...

    # methods
    @abc.abstractmethod
    def Expand(self, initial: System.Object, ) -> System.Array[System.Object]:
        ...

class ModuleGlobalCache(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields
    NotCaching: System.Object = ...
    NoCache: IronPython.Runtime.ModuleGlobalCache = ...

    # properties
    @property
    def IsCaching(self) -> bool:
        ...

    @property
    def HasValue(self) -> bool:
        ...

    @property
    def Value(self) -> System.Object:
        ...
    @Value.setter
    def Value(self, val: System.Object):
        ...

    # methods
    def __init__(self, value: System.Object, ):
        ...

    def Changed(self, sender: System.Object, e: Microsoft.Scripting.Runtime.ModuleChangeEventArgs, ) -> None:
        ...

class MaybeNotImplementedAttribute(System.Attribute):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def TypeId(self) -> System.Object:
        ...

    # methods
    def __init__(self, ):
        ...

class ModuleLoader(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    def __init__(self, sc: IronPython.Compiler.OnDiskScriptCode, parentName: str, name: str, ):
        ...

    def load_module(self, context: IronPython.Runtime.CodeContext, fullName: str, ) -> IronPython.Runtime.PythonModule:
        ...

class DictionaryKeyView(System.Collections.Generic.ICollection[System.Object], System.Collections.Generic.IEnumerable[System.Object], System.Collections.IEnumerable, System.Collections.ICollection, IronPython.Runtime.ICodeFormattable, System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        self._dict: IronPython.Runtime.PythonDictionary
        ...

    # static fields

    # properties
    @property
    def Count(self) -> int:
        ...

    @property
    def IsReadOnly(self) -> bool:
        ...

    @property
    def Count(self) -> int:
        ...

    @property
    def SyncRoot(self) -> System.Object:
        ...

    @property
    def IsSynchronized(self) -> bool:
        ...

    # methods
    def __init__(self, dict: IronPython.Runtime.PythonDictionary, ):
        ...

    def GetEnumerator(self, ) -> System.Collections.Generic.IEnumerator[System.Object]:
        ...

    def GetEnumerator(self, ) -> System.Collections.IEnumerator:
        ...

    def Add(self, key: System.Object, ) -> None:
        ...

    def Clear(self, ) -> None:
        ...

    def Contains(self, key: System.Object, ) -> bool:
        ...

    def CopyTo(self, array: System.Array[System.Object], arrayIndex: int, ) -> None:
        ...

    def Remove(self, item: System.Object, ) -> bool:
        ...

    def CopyTo(self, array: System.Array, index: int, ) -> None:
        ...

    def Equals(self, obj: System.Object, ) -> bool:
        ...

    def __repr__(self, context: IronPython.Runtime.CodeContext, ) -> str:
        ...

    def __reduce__(self, context: IronPython.Runtime.CodeContext, ) -> System.Object:
        ...

    def isdisjoint(self, other: System.Collections.IEnumerable, ) -> bool:
        ...

    def GetHashCode(self, ) -> int:
        ...

class FunctionAttributes(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    None_: int = ...
    ArgumentList: int = ...
    KeywordDictionary: int = ...
    Generator: int = ...
    CanSetSysExcInfo: int = ...
    ContainsTryFinally: int = ...
    GeneratorStop: int = ...

class DictionaryItemEnumerator(System.Collections.Generic.IEnumerator[System.Object], System.IDisposable, System.Collections.IEnumerator, System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def Current(self) -> System.Object:
        ...

    @property
    def Current(self) -> System.Object:
        ...

    # methods
    def __init__(self, dict: IronPython.Runtime.DictionaryStorage, ):
        ...

    def MoveNext(self, ) -> bool:
        ...

    def Reset(self, ) -> None:
        ...

    def Dispose(self, ) -> None:
        ...

    def __iter__(self, ) -> System.Object:
        ...

    def __len__(self, ) -> int:
        ...

    def __reduce__(self, context: IronPython.Runtime.CodeContext, ) -> System.Object:
        ...

class FunctionCaller(IronPython.Runtime.FunctionCaller, typing.Generic[T0]):
    @typing.overload
    def __init__(self, **kwargs):
        self._compat: int
        ...

    # static fields

    # properties
    # methods
    def __init__(self, compat: int, ):
        ...

    def Call1(self, site: System.Runtime.CompilerServices.CallSite, context: IronPython.Runtime.CodeContext, func: System.Object, arg0: T0, ) -> System.Object:
        ...

    def Default1Call1(self, site: System.Runtime.CompilerServices.CallSite, context: IronPython.Runtime.CodeContext, func: System.Object, arg0: T0, ) -> System.Object:
        ...

    def Default2Call1(self, site: System.Runtime.CompilerServices.CallSite, context: IronPython.Runtime.CodeContext, func: System.Object, arg0: T0, ) -> System.Object:
        ...

    def Default3Call1(self, site: System.Runtime.CompilerServices.CallSite, context: IronPython.Runtime.CodeContext, func: System.Object, arg0: T0, ) -> System.Object:
        ...

    def Default4Call1(self, site: System.Runtime.CompilerServices.CallSite, context: IronPython.Runtime.CodeContext, func: System.Object, arg0: T0, ) -> System.Object:
        ...

    def Default5Call1(self, site: System.Runtime.CompilerServices.CallSite, context: IronPython.Runtime.CodeContext, func: System.Object, arg0: T0, ) -> System.Object:
        ...

    def Default6Call1(self, site: System.Runtime.CompilerServices.CallSite, context: IronPython.Runtime.CodeContext, func: System.Object, arg0: T0, ) -> System.Object:
        ...

    def Default7Call1(self, site: System.Runtime.CompilerServices.CallSite, context: IronPython.Runtime.CodeContext, func: System.Object, arg0: T0, ) -> System.Object:
        ...

    def Default8Call1(self, site: System.Runtime.CompilerServices.CallSite, context: IronPython.Runtime.CodeContext, func: System.Object, arg0: T0, ) -> System.Object:
        ...

    def Default9Call1(self, site: System.Runtime.CompilerServices.CallSite, context: IronPython.Runtime.CodeContext, func: System.Object, arg0: T0, ) -> System.Object:
        ...

    def Default10Call1(self, site: System.Runtime.CompilerServices.CallSite, context: IronPython.Runtime.CodeContext, func: System.Object, arg0: T0, ) -> System.Object:
        ...

    def Default11Call1(self, site: System.Runtime.CompilerServices.CallSite, context: IronPython.Runtime.CodeContext, func: System.Object, arg0: T0, ) -> System.Object:
        ...

    def Default12Call1(self, site: System.Runtime.CompilerServices.CallSite, context: IronPython.Runtime.CodeContext, func: System.Object, arg0: T0, ) -> System.Object:
        ...

class CodeContext(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def ModuleContext(self) -> IronPython.Runtime.ModuleContext:
        ...

    @property
    def GlobalScope(self) -> Microsoft.Scripting.Runtime.Scope:
        ...

    @property
    def LanguageContext(self) -> IronPython.Runtime.PythonContext:
        ...

    @property
    def GlobalDict(self) -> IronPython.Runtime.PythonDictionary:
        ...

    @property
    def ShowCls(self) -> bool:
        ...
    @ShowCls.setter
    def ShowCls(self, val: bool):
        ...

    @property
    def Dict(self) -> IronPython.Runtime.PythonDictionary:
        ...

    @property
    def IsTopLevel(self) -> bool:
        ...

    @property
    def Module(self) -> IronPython.Runtime.PythonModule:
        ...

    @property
    def ModuleName(self) -> str:
        ...

    # methods
    def __init__(self, dict: IronPython.Runtime.PythonDictionary, moduleContext: IronPython.Runtime.ModuleContext, ):
        ...

    def TryLookupName(self, name: str, value: ref[System.Object], ) -> bool:
        ...

    def TryLookupBuiltin(self, name: str, value: ref[System.Object], ) -> bool:
        ...

    def TryGetVariable(self, name: str, value: ref[System.Object], ) -> bool:
        ...

    def TryRemoveVariable(self, name: str, ) -> bool:
        ...

    def SetVariable(self, name: str, value: System.Object, ) -> None:
        ...

    def TryGetGlobalVariable(self, name: str, res: ref[System.Object], ) -> bool:
        ...

    def SetGlobalVariable(self, name: str, value: System.Object, ) -> None:
        ...

    def TryRemoveGlobalVariable(self, name: str, ) -> bool:
        ...

    def GetGlobalArray(self, ) -> System.Array[IronPython.Compiler.PythonGlobal]:
        ...

    def GetBuiltinsDict(self, ) -> IronPython.Runtime.PythonDictionary:
        ...

class IEnumeratorOfTWrapper(System.Collections.Generic.IEnumerator[T], System.IDisposable, System.Collections.IEnumerator, System.Object, typing.Generic[T]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def Current(self) -> T:
        ...

    @property
    def Current(self) -> System.Object:
        ...

    # methods
    def __init__(self, enumerable: System.Collections.IEnumerator, ):
        ...

    def Dispose(self, ) -> None:
        ...

    def MoveNext(self, ) -> bool:
        ...

    def Reset(self, ) -> None:
        ...

class MissingParameter(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields
    Value: IronPython.Runtime.MissingParameter = ...

    # properties
    # methods
    def __init__(self, ):
        ...

class ErrorCodes(System.Object, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields
    IncompleteMask: int = ...
    IncompleteStatement: int = ...
    IncompleteToken: int = ...
    ErrorMask: int = ...
    SyntaxError: int = ...
    IndentationError: int = ...
    TabError: int = ...
    NoCaret: int = ...

    # properties
    # methods
class PythonStrIterator(System.Collections.IEnumerable, System.Collections.Generic.IEnumerator[str], System.IDisposable, System.Collections.IEnumerator, System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def Current(self) -> str:
        ...

    @property
    def Current(self) -> System.Object:
        ...

    # methods
    def __init__(self, s: str, ):
        ...

    def __reduce__(self, context: IronPython.Runtime.CodeContext, ) -> IronPython.Runtime.PythonTuple:
        ...

    def __setstate__(self, index: int, ) -> None:
        ...

    def GetEnumerator(self, ) -> System.Collections.IEnumerator:
        ...

    def Dispose(self, ) -> None:
        ...

    def MoveNext(self, ) -> bool:
        ...

    def Reset(self, ) -> None:
        ...

class FunctionCaller(IronPython.Runtime.FunctionCaller, typing.Generic[T0, T1, T2, T3, T4, T5, T6, T7, T8, T9]):
    @typing.overload
    def __init__(self, **kwargs):
        self._compat: int
        ...

    # static fields

    # properties
    # methods
    def __init__(self, compat: int, ):
        ...

    def Call10(self, site: System.Runtime.CompilerServices.CallSite, context: IronPython.Runtime.CodeContext, func: System.Object, arg0: T0, arg1: T1, arg2: T2, arg3: T3, arg4: T4, arg5: T5, arg6: T6, arg7: T7, arg8: T8, arg9: T9, ) -> System.Object:
        ...

    def Default1Call10(self, site: System.Runtime.CompilerServices.CallSite, context: IronPython.Runtime.CodeContext, func: System.Object, arg0: T0, arg1: T1, arg2: T2, arg3: T3, arg4: T4, arg5: T5, arg6: T6, arg7: T7, arg8: T8, arg9: T9, ) -> System.Object:
        ...

    def Default2Call10(self, site: System.Runtime.CompilerServices.CallSite, context: IronPython.Runtime.CodeContext, func: System.Object, arg0: T0, arg1: T1, arg2: T2, arg3: T3, arg4: T4, arg5: T5, arg6: T6, arg7: T7, arg8: T8, arg9: T9, ) -> System.Object:
        ...

    def Default3Call10(self, site: System.Runtime.CompilerServices.CallSite, context: IronPython.Runtime.CodeContext, func: System.Object, arg0: T0, arg1: T1, arg2: T2, arg3: T3, arg4: T4, arg5: T5, arg6: T6, arg7: T7, arg8: T8, arg9: T9, ) -> System.Object:
        ...

class Filter(System.Collections.IEnumerator, System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def Current(self) -> System.Object:
        ...
    @Current.setter
    def Current(self, val: System.Object):
        ...

    # methods
    def __init__(self, context: IronPython.Runtime.CodeContext, function: System.Object, iterable: System.Object, ):
        ...

    def MoveNext(self, ) -> bool:
        ...

    def Reset(self, ) -> None:
        ...

    def __reduce__(self, ) -> IronPython.Runtime.PythonTuple:
        ...

class FunctionCaller(IronPython.Runtime.FunctionCaller, typing.Generic[T0, T1, T2, T3]):
    @typing.overload
    def __init__(self, **kwargs):
        self._compat: int
        ...

    # static fields

    # properties
    # methods
    def __init__(self, compat: int, ):
        ...

    def Call4(self, site: System.Runtime.CompilerServices.CallSite, context: IronPython.Runtime.CodeContext, func: System.Object, arg0: T0, arg1: T1, arg2: T2, arg3: T3, ) -> System.Object:
        ...

    def Default1Call4(self, site: System.Runtime.CompilerServices.CallSite, context: IronPython.Runtime.CodeContext, func: System.Object, arg0: T0, arg1: T1, arg2: T2, arg3: T3, ) -> System.Object:
        ...

    def Default2Call4(self, site: System.Runtime.CompilerServices.CallSite, context: IronPython.Runtime.CodeContext, func: System.Object, arg0: T0, arg1: T1, arg2: T2, arg3: T3, ) -> System.Object:
        ...

    def Default3Call4(self, site: System.Runtime.CompilerServices.CallSite, context: IronPython.Runtime.CodeContext, func: System.Object, arg0: T0, arg1: T1, arg2: T2, arg3: T3, ) -> System.Object:
        ...

    def Default4Call4(self, site: System.Runtime.CompilerServices.CallSite, context: IronPython.Runtime.CodeContext, func: System.Object, arg0: T0, arg1: T1, arg2: T2, arg3: T3, ) -> System.Object:
        ...

    def Default5Call4(self, site: System.Runtime.CompilerServices.CallSite, context: IronPython.Runtime.CodeContext, func: System.Object, arg0: T0, arg1: T1, arg2: T2, arg3: T3, ) -> System.Object:
        ...

    def Default6Call4(self, site: System.Runtime.CompilerServices.CallSite, context: IronPython.Runtime.CodeContext, func: System.Object, arg0: T0, arg1: T1, arg2: T2, arg3: T3, ) -> System.Object:
        ...

    def Default7Call4(self, site: System.Runtime.CompilerServices.CallSite, context: IronPython.Runtime.CodeContext, func: System.Object, arg0: T0, arg1: T1, arg2: T2, arg3: T3, ) -> System.Object:
        ...

    def Default8Call4(self, site: System.Runtime.CompilerServices.CallSite, context: IronPython.Runtime.CodeContext, func: System.Object, arg0: T0, arg1: T1, arg2: T2, arg3: T3, ) -> System.Object:
        ...

    def Default9Call4(self, site: System.Runtime.CompilerServices.CallSite, context: IronPython.Runtime.CodeContext, func: System.Object, arg0: T0, arg1: T1, arg2: T2, arg3: T3, ) -> System.Object:
        ...

class DefaultContext(System.Object, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields
    _default: IronPython.Runtime.CodeContext = ...
    _defaultCLS: IronPython.Runtime.CodeContext = ...

    # properties
    @property
    def Id(self) -> Microsoft.Scripting.Runtime.ContextId:
        ...

    @property
    def Default(self) -> IronPython.Runtime.CodeContext:
        ...

    @property
    def DefaultPythonContext(self) -> IronPython.Runtime.PythonContext:
        ...

    @property
    def DefaultCLS(self) -> IronPython.Runtime.CodeContext:
        ...

    # methods
    @staticmethod
    def CreateDefaultCLSContext(context: IronPython.Runtime.PythonContext, ) -> IronPython.Runtime.CodeContext:
        ...

    @staticmethod
    def InitializeDefaults(defaultContext: IronPython.Runtime.CodeContext, defaultClsCodeContext: IronPython.Runtime.CodeContext, ) -> None:
        ...

class IPythonBuffer(System.IDisposable, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    @abc.abstractmethod
    def Object(self) -> System.Object:
        ...

    @property
    @abc.abstractmethod
    def IsReadOnly(self) -> bool:
        ...

    @property
    @abc.abstractmethod
    def Offset(self) -> int:
        ...

    @property
    @abc.abstractmethod
    def Format(self) -> str:
        ...

    @property
    @abc.abstractmethod
    def ItemCount(self) -> int:
        ...

    @property
    @abc.abstractmethod
    def ItemSize(self) -> int:
        ...

    @property
    @abc.abstractmethod
    def NumOfDims(self) -> int:
        ...

    @property
    @abc.abstractmethod
    def Shape(self) -> System.Collections.Generic.IReadOnlyList[int]:
        ...

    @property
    @abc.abstractmethod
    def Strides(self) -> System.Collections.Generic.IReadOnlyList[int]:
        ...

    @property
    @abc.abstractmethod
    def SubOffsets(self) -> System.Collections.Generic.IReadOnlyList[int]:
        ...

    # methods
    @abc.abstractmethod
    def AsReadOnlySpan(self, ) -> System.ReadOnlySpan[int]:
        ...

    @abc.abstractmethod
    def AsSpan(self, ) -> System.Span[int]:
        ...

    @abc.abstractmethod
    def Pin(self, ) -> System.Buffers.MemoryHandle:
        ...

class Importer(System.Object, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields
    ModuleReloadMethod: str = ...

    # properties
    # methods
    @staticmethod
    def Import(context: IronPython.Runtime.CodeContext, fullName: str, from_: IronPython.Runtime.PythonTuple, level: int, ) -> System.Object:
        ...

    @staticmethod
    def ImportLightThrow(context: IronPython.Runtime.CodeContext, fullName: str, from_: IronPython.Runtime.PythonTuple, level: int, ) -> System.Object:
        ...

    @staticmethod
    def ImportFrom(context: IronPython.Runtime.CodeContext, from_: System.Object, name: str, ) -> System.Object:
        ...

    @staticmethod
    def ImportModuleFrom(context: IronPython.Runtime.CodeContext, from_: System.Object, parts: System.ArraySegment[str], root: System.Object, ) -> System.Object:
        ...

    @staticmethod
    def ImportModule(context: IronPython.Runtime.CodeContext, globals: System.Object, modName: str, bottom: bool, level: int, ) -> System.Object:
        ...

    @staticmethod
    def TryGetNameAndPath(context: IronPython.Runtime.CodeContext, globals: System.Object, name: str, level: int, package: str, full: ref[str], path: ref[IronPython.Runtime.PythonList], parentMod: ref[IronPython.Runtime.PythonModule], ) -> bool:
        ...

    @staticmethod
    def GetParentPackageName(level: int, names: System.Array[str], ) -> str:
        ...

    @staticmethod
    def ReloadModule(context: IronPython.Runtime.CodeContext, module: IronPython.Runtime.PythonModule, ) -> System.Object:
        ...

    @staticmethod
    def GetParentPathAndModule(context: IronPython.Runtime.CodeContext, parentModuleName: str, parentModule: ref[IronPython.Runtime.PythonModule], ) -> IronPython.Runtime.PythonList:
        ...

    @staticmethod
    def ReloadBuiltinModule(context: IronPython.Runtime.CodeContext, module: IronPython.Runtime.PythonModule, ) -> None:
        ...

    @staticmethod
    def TryGetExistingOrMetaPathModule(context: IronPython.Runtime.CodeContext, fullName: str, path: IronPython.Runtime.PythonList, ret: ref[System.Object], ) -> bool:
        ...

    @staticmethod
    def TryLoadMetaPathModule(context: IronPython.Runtime.CodeContext, fullName: str, path: IronPython.Runtime.PythonList, ret: ref[System.Object], ) -> bool:
        ...

    @staticmethod
    def FindAndLoadModuleFromImporter(context: IronPython.Runtime.CodeContext, importer: System.Object, fullName: str, path: IronPython.Runtime.PythonList, ret: ref[System.Object], ) -> bool:
        ...

    @staticmethod
    def TryGetExistingModule(context: IronPython.Runtime.CodeContext, fullName: str, ret: ref[System.Object], ) -> bool:
        ...

    @staticmethod
    def ImportTopAbsolute(context: IronPython.Runtime.CodeContext, name: str, ) -> System.Object:
        ...

    @staticmethod
    def SubArray(t: System.Array[str], len: int, ) -> System.Array[str]:
        ...

    @staticmethod
    def TryGetNestedModule(context: IronPython.Runtime.CodeContext, scope: IronPython.Runtime.PythonModule, parts: System.Array[str], current: int, nested: ref[System.Object], ) -> bool:
        ...

    @staticmethod
    def ImportNestedModule(context: IronPython.Runtime.CodeContext, module: IronPython.Runtime.PythonModule, parts: System.ArraySegment[str], path: IronPython.Runtime.PythonList, scopeModuleName: str, ) -> System.Object:
        ...

    @staticmethod
    def FindImportFunction(context: IronPython.Runtime.CodeContext, ) -> System.Object:
        ...

    @staticmethod
    def ImportBuiltin(context: IronPython.Runtime.CodeContext, name: str, ) -> System.Object:
        ...

    @staticmethod
    def ImportReflected(context: IronPython.Runtime.CodeContext, name: str, ) -> System.Object:
        ...

    @staticmethod
    def MemberTrackerToPython(context: IronPython.Runtime.CodeContext, ret: System.Object, ) -> System.Object:
        ...

    @staticmethod
    def TryImportSourceFile(context: IronPython.Runtime.PythonContext, name: str, ) -> IronPython.Runtime.PythonModule:
        ...

    @staticmethod
    def ExecuteSourceUnit(context: IronPython.Runtime.PythonContext, sourceUnit: Microsoft.Scripting.SourceUnit, ) -> IronPython.Runtime.PythonModule:
        ...

    @staticmethod
    def TryFindSourceFile(context: IronPython.Runtime.PythonContext, name: str, ) -> Microsoft.Scripting.SourceUnit:
        ...

    @staticmethod
    def IsReflected(module: System.Object, ) -> bool:
        ...

    @staticmethod
    def CreateFullName(baseName: str, parts: System.ArraySegment[str], ) -> str:
        ...

    @staticmethod
    def ImportFromPath(context: IronPython.Runtime.CodeContext, name: str, fullName: str, path: IronPython.Runtime.PythonList, ) -> System.Object:
        ...

    @staticmethod
    def ImportFromPathHook(context: IronPython.Runtime.CodeContext, name: str, fullName: str, path: IronPython.Runtime.PythonList, defaultLoader: System.Func[IronPython.Runtime.CodeContext, str, str, str, System.Object], ) -> System.Object:
        ...

    @staticmethod
    def TryImportMainFromZip(context: IronPython.Runtime.CodeContext, path: str, importer: ref[System.Object], ) -> bool:
        ...

    @staticmethod
    def LoadFromDisk(context: IronPython.Runtime.CodeContext, name: str, fullName: str, str: str, ) -> System.Object:
        ...

    @staticmethod
    def FindImporterForPath(context: IronPython.Runtime.CodeContext, dirname: str, ) -> System.Object:
        ...

    @staticmethod
    def LoadModuleFromSource(context: IronPython.Runtime.CodeContext, name: str, path: str, ) -> IronPython.Runtime.PythonModule:
        ...

    @staticmethod
    def GetFullPathAndValidateCase(context: Microsoft.Scripting.Runtime.LanguageContext, path: str, isDir: bool, ) -> str:
        ...

    @staticmethod
    def LoadPackageFromSource(context: IronPython.Runtime.CodeContext, name: str, path: str, ) -> IronPython.Runtime.PythonModule:
        ...

    @staticmethod
    def LoadFromSourceUnit(context: IronPython.Runtime.CodeContext, sourceCode: Microsoft.Scripting.SourceUnit, name: str, path: str, ) -> IronPython.Runtime.PythonModule:
        ...

class FunctionCaller(IronPython.Runtime.FunctionCaller, typing.Generic[T0, T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11]):
    @typing.overload
    def __init__(self, **kwargs):
        self._compat: int
        ...

    # static fields

    # properties
    # methods
    def __init__(self, compat: int, ):
        ...

    def Call12(self, site: System.Runtime.CompilerServices.CallSite, context: IronPython.Runtime.CodeContext, func: System.Object, arg0: T0, arg1: T1, arg2: T2, arg3: T3, arg4: T4, arg5: T5, arg6: T6, arg7: T7, arg8: T8, arg9: T9, arg10: T10, arg11: T11, ) -> System.Object:
        ...

    def Default1Call12(self, site: System.Runtime.CompilerServices.CallSite, context: IronPython.Runtime.CodeContext, func: System.Object, arg0: T0, arg1: T1, arg2: T2, arg3: T3, arg4: T4, arg5: T5, arg6: T6, arg7: T7, arg8: T8, arg9: T9, arg10: T10, arg11: T11, ) -> System.Object:
        ...

class SetIterator(System.Collections.IEnumerable, System.Collections.Generic.IEnumerable[System.Object], System.Collections.IEnumerator, System.Collections.Generic.IEnumerator[System.Object], System.IDisposable, System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def Current(self) -> System.Object:
        ...

    # methods
    def __init__(self, items: IronPython.Runtime.SetStorage, mutable: bool, ):
        ...

    def Dispose(self, ) -> None:
        ...

    def MoveNext(self, ) -> bool:
        ...

    def Reset(self, ) -> None:
        ...

    def GetEnumerator(self, ) -> System.Collections.IEnumerator:
        ...

    def GetEnumerator(self, ) -> System.Collections.Generic.IEnumerator[System.Object]:
        ...

    def __reduce__(self, context: IronPython.Runtime.CodeContext, ) -> IronPython.Runtime.PythonTuple:
        ...

    def __length_hint__(self, ) -> int:
        ...

class SetCollection(System.Collections.IEnumerable, System.Collections.Generic.IEnumerable[System.Object], System.Collections.ICollection, System.Collections.IStructuralEquatable, IronPython.Runtime.ICodeFormattable, IronPython.Runtime.IWeakReferenceable, System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        self._items: IronPython.Runtime.SetStorage
        ...

    # static fields
    __hash__: System.Object = ...

    # properties
    @property
    def Empty(self) -> IronPython.Runtime.SetCollection:
        ...

    @property
    def Count(self) -> int:
        ...

    @property
    def IsSynchronized(self) -> bool:
        ...

    @property
    def SyncRoot(self) -> System.Object:
        ...

    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def __init__(self, items: IronPython.Runtime.SetStorage, ):
        ...

    @typing.overload
    def __init__(self, items: System.Array[System.Object], ):
        ...

    def GetEnumerator(self, ) -> System.Collections.IEnumerator:
        ...

    def GetEnumerator(self, ) -> System.Collections.Generic.IEnumerator[System.Object]:
        ...

    def __repr__(self, context: IronPython.Runtime.CodeContext, ) -> str:
        ...

    def CopyTo(self, array: System.Array, index: int, ) -> None:
        ...

    def GetWeakRef(self, ) -> IronPython.Runtime.WeakRefTracker:
        ...

    def SetWeakRef(self, value: IronPython.Runtime.WeakRefTracker, ) -> bool:
        ...

    def SetFinalizer(self, value: IronPython.Runtime.WeakRefTracker, ) -> None:
        ...

    @typing.overload
    def __init__(self, ) -> None:
        ...

    @typing.overload
    def __init__(self, set: IronPython.Runtime.SetCollection, ) -> None:
        ...

    @typing.overload
    def __init__(self, set: IronPython.Runtime.FrozenSetCollection, ) -> None:
        ...

    @typing.overload
    def __init__(self, set: System.Object, ) -> None:
        ...

    @staticmethod
    @typing.overload
    def __new__(context: IronPython.Runtime.CodeContext, cls: IronPython.Runtime.Types.PythonType, ) -> System.Object:
        ...

    @staticmethod
    @typing.overload
    def __new__(context: IronPython.Runtime.CodeContext, cls: IronPython.Runtime.Types.PythonType, arg: System.Object, ) -> System.Object:
        ...

    @staticmethod
    @typing.overload
    def __new__(context: IronPython.Runtime.CodeContext, cls: IronPython.Runtime.Types.PythonType, argsø: System.Array[System.Object], ) -> System.Object:
        ...

    @staticmethod
    @typing.overload
    def __new__(context: IronPython.Runtime.CodeContext, cls: IronPython.Runtime.Types.PythonType, kwArgs: System.Collections.Generic.IDictionary[System.Object, System.Object], argsø: System.Array[System.Object], ) -> System.Object:
        ...

    @staticmethod
    @typing.overload
    def Make(items: IronPython.Runtime.SetStorage, ) -> IronPython.Runtime.SetCollection:
        ...

    @staticmethod
    @typing.overload
    def Make(set: System.Object, ) -> IronPython.Runtime.SetCollection:
        ...

    def copy(self, ) -> IronPython.Runtime.SetCollection:
        ...

    def __len__(self, ) -> int:
        ...

    def __contains__(self, item: System.Object, ) -> bool:
        ...

    def __reduce__(self, context: IronPython.Runtime.CodeContext, ) -> IronPython.Runtime.PythonTuple:
        ...

    def GetHashCode(self, comparer: System.Collections.IEqualityComparer, ) -> int:
        ...

    def Equals(self, other: System.Object, comparer: System.Collections.IEqualityComparer, ) -> bool:
        ...

    def __eq__(self, other: System.Object, ) -> System.Object:
        ...

    def __ne__(self, other: System.Object, ) -> System.Object:
        ...

    def add(self, item: System.Object, ) -> None:
        ...

    def clear(self, ) -> None:
        ...

    def discard(self, item: System.Object, ) -> None:
        ...

    def pop(self, ) -> System.Object:
        ...

    def remove(self, item: System.Object, ) -> None:
        ...

    @typing.overload
    def update(self, set: IronPython.Runtime.SetCollection, ) -> None:
        ...

    @typing.overload
    def update(self, set: IronPython.Runtime.FrozenSetCollection, ) -> None:
        ...

    @typing.overload
    def update(self, set: System.Object, ) -> None:
        ...

    @typing.overload
    def update(self, sets: System.Array[System.Object], ) -> None:
        ...

    @typing.overload
    def intersection_update(self, set: IronPython.Runtime.SetCollection, ) -> None:
        ...

    @typing.overload
    def intersection_update(self, set: IronPython.Runtime.FrozenSetCollection, ) -> None:
        ...

    @typing.overload
    def intersection_update(self, set: System.Object, ) -> None:
        ...

    @typing.overload
    def intersection_update(self, sets: System.Array[System.Object], ) -> None:
        ...

    @typing.overload
    def difference_update(self, set: IronPython.Runtime.SetCollection, ) -> None:
        ...

    @typing.overload
    def difference_update(self, set: IronPython.Runtime.FrozenSetCollection, ) -> None:
        ...

    @typing.overload
    def difference_update(self, set: System.Object, ) -> None:
        ...

    @typing.overload
    def difference_update(self, sets: System.Array[System.Object], ) -> None:
        ...

    @typing.overload
    def symmetric_difference_update(self, set: IronPython.Runtime.SetCollection, ) -> None:
        ...

    @typing.overload
    def symmetric_difference_update(self, set: IronPython.Runtime.FrozenSetCollection, ) -> None:
        ...

    @typing.overload
    def symmetric_difference_update(self, set: System.Object, ) -> None:
        ...

    @typing.overload
    def isdisjoint(self, set: IronPython.Runtime.SetCollection, ) -> bool:
        ...

    @typing.overload
    def isdisjoint(self, set: IronPython.Runtime.FrozenSetCollection, ) -> bool:
        ...

    @typing.overload
    def isdisjoint(self, set: System.Object, ) -> bool:
        ...

    @typing.overload
    def issubset(self, set: IronPython.Runtime.SetCollection, ) -> bool:
        ...

    @typing.overload
    def issubset(self, set: IronPython.Runtime.FrozenSetCollection, ) -> bool:
        ...

    @typing.overload
    def issubset(self, set: System.Object, ) -> bool:
        ...

    @typing.overload
    def issuperset(self, set: IronPython.Runtime.SetCollection, ) -> bool:
        ...

    @typing.overload
    def issuperset(self, set: IronPython.Runtime.FrozenSetCollection, ) -> bool:
        ...

    @typing.overload
    def issuperset(self, set: System.Object, ) -> bool:
        ...

    @typing.overload
    def union(self, ) -> IronPython.Runtime.SetCollection:
        ...

    @typing.overload
    def union(self, set: IronPython.Runtime.SetCollection, ) -> IronPython.Runtime.SetCollection:
        ...

    @typing.overload
    def union(self, set: IronPython.Runtime.FrozenSetCollection, ) -> IronPython.Runtime.SetCollection:
        ...

    @typing.overload
    def union(self, set: System.Object, ) -> IronPython.Runtime.SetCollection:
        ...

    @typing.overload
    def union(self, sets: System.Array[System.Object], ) -> IronPython.Runtime.SetCollection:
        ...

    @typing.overload
    def intersection(self, ) -> IronPython.Runtime.SetCollection:
        ...

    @typing.overload
    def intersection(self, set: IronPython.Runtime.SetCollection, ) -> IronPython.Runtime.SetCollection:
        ...

    @typing.overload
    def intersection(self, set: IronPython.Runtime.FrozenSetCollection, ) -> IronPython.Runtime.SetCollection:
        ...

    @typing.overload
    def intersection(self, set: System.Object, ) -> IronPython.Runtime.SetCollection:
        ...

    @typing.overload
    def intersection(self, sets: System.Array[System.Object], ) -> IronPython.Runtime.SetCollection:
        ...

    @typing.overload
    def difference(self, ) -> IronPython.Runtime.SetCollection:
        ...

    @typing.overload
    def difference(self, set: IronPython.Runtime.SetCollection, ) -> IronPython.Runtime.SetCollection:
        ...

    @typing.overload
    def difference(self, set: IronPython.Runtime.FrozenSetCollection, ) -> IronPython.Runtime.SetCollection:
        ...

    @typing.overload
    def difference(self, set: System.Object, ) -> IronPython.Runtime.SetCollection:
        ...

    @typing.overload
    def difference(self, sets: System.Array[System.Object], ) -> IronPython.Runtime.SetCollection:
        ...

    @typing.overload
    def symmetric_difference(self, set: IronPython.Runtime.SetCollection, ) -> IronPython.Runtime.SetCollection:
        ...

    @typing.overload
    def symmetric_difference(self, set: IronPython.Runtime.FrozenSetCollection, ) -> IronPython.Runtime.SetCollection:
        ...

    @typing.overload
    def symmetric_difference(self, set: System.Object, ) -> IronPython.Runtime.SetCollection:
        ...

class IProxyObject(abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    @abc.abstractmethod
    def Target(self) -> System.Object:
        ...

    # methods
class OrderedLocker(System.IDisposable, System.ValueType):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    def __init__(self, one: System.Object, two: System.Object, ):
        ...

    def Dispose(self, ) -> None:
        ...

class PythonModule(System.Dynamic.IDynamicMetaObjectProvider, IronPython.Runtime.IPythonMembersList, Microsoft.Scripting.Runtime.IMembersList, System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def __dict__(self) -> IronPython.Runtime.PythonDictionary:
        ...

    @property
    def Scope(self) -> Microsoft.Scripting.Runtime.Scope:
        ...

    @property
    def IsBuiltin(self) -> bool:
        ...

    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def __init__(self, context: IronPython.Runtime.PythonContext, scope: Microsoft.Scripting.Runtime.Scope, ):
        ...

    @typing.overload
    def __init__(self, dict: IronPython.Runtime.PythonDictionary, ):
        ...

    @staticmethod
    @typing.overload
    def __new__(context: IronPython.Runtime.CodeContext, cls: IronPython.Runtime.Types.PythonType, argsø: System.Array[System.Object], ) -> IronPython.Runtime.PythonModule:
        ...

    @staticmethod
    @typing.overload
    def __new__(context: IronPython.Runtime.CodeContext, cls: IronPython.Runtime.Types.PythonType, kwDict0: System.Collections.Generic.IDictionary[System.Object, System.Object], argsø: System.Array[System.Object], ) -> IronPython.Runtime.PythonModule:
        ...

    @typing.overload
    def __init__(self, name: str, ) -> None:
        ...

    @typing.overload
    def __init__(self, name: str, doc: str, ) -> None:
        ...

    def __getattribute__(self, context: IronPython.Runtime.CodeContext, name: str, ) -> System.Object:
        ...

    def GetAttributeNoThrow(self, context: IronPython.Runtime.CodeContext, name: str, ) -> System.Object:
        ...

    def __setattr__(self, context: IronPython.Runtime.CodeContext, name: str, value: System.Object, ) -> None:
        ...

    def __delattr__(self, context: IronPython.Runtime.CodeContext, name: str, ) -> None:
        ...

    def __repr__(self, ) -> str:
        ...

    def __str__(self, ) -> str:
        ...

    def GetMetaObject(self, parameter: System.Linq.Expressions.Expression, ) -> System.Dynamic.DynamicMetaObject:
        ...

    def GetFile(self, ) -> str:
        ...

    def GetName(self, ) -> str:
        ...

    def GetMemberNames(self, context: IronPython.Runtime.CodeContext, ) -> System.Collections.Generic.IList[System.Object]:
        ...

    def GetMemberNames(self, ) -> System.Collections.Generic.IList[str]:
        ...

class FunctionCaller(IronPython.Runtime.FunctionCaller, typing.Generic[T0, T1, T2, T3, T4, T5, T6, T7]):
    @typing.overload
    def __init__(self, **kwargs):
        self._compat: int
        ...

    # static fields

    # properties
    # methods
    def __init__(self, compat: int, ):
        ...

    def Call8(self, site: System.Runtime.CompilerServices.CallSite, context: IronPython.Runtime.CodeContext, func: System.Object, arg0: T0, arg1: T1, arg2: T2, arg3: T3, arg4: T4, arg5: T5, arg6: T6, arg7: T7, ) -> System.Object:
        ...

    def Default1Call8(self, site: System.Runtime.CompilerServices.CallSite, context: IronPython.Runtime.CodeContext, func: System.Object, arg0: T0, arg1: T1, arg2: T2, arg3: T3, arg4: T4, arg5: T5, arg6: T6, arg7: T7, ) -> System.Object:
        ...

    def Default2Call8(self, site: System.Runtime.CompilerServices.CallSite, context: IronPython.Runtime.CodeContext, func: System.Object, arg0: T0, arg1: T1, arg2: T2, arg3: T3, arg4: T4, arg5: T5, arg6: T6, arg7: T7, ) -> System.Object:
        ...

    def Default3Call8(self, site: System.Runtime.CompilerServices.CallSite, context: IronPython.Runtime.CodeContext, func: System.Object, arg0: T0, arg1: T1, arg2: T2, arg3: T3, arg4: T4, arg5: T5, arg6: T6, arg7: T7, ) -> System.Object:
        ...

    def Default4Call8(self, site: System.Runtime.CompilerServices.CallSite, context: IronPython.Runtime.CodeContext, func: System.Object, arg0: T0, arg1: T1, arg2: T2, arg3: T3, arg4: T4, arg5: T5, arg6: T6, arg7: T7, ) -> System.Object:
        ...

    def Default5Call8(self, site: System.Runtime.CompilerServices.CallSite, context: IronPython.Runtime.CodeContext, func: System.Object, arg0: T0, arg1: T1, arg2: T2, arg3: T3, arg4: T4, arg5: T5, arg6: T6, arg7: T7, ) -> System.Object:
        ...

class FunctionCaller(IronPython.Runtime.FunctionCaller, typing.Generic[T0, T1, T2, T3, T4, T5, T6]):
    @typing.overload
    def __init__(self, **kwargs):
        self._compat: int
        ...

    # static fields

    # properties
    # methods
    def __init__(self, compat: int, ):
        ...

    def Call7(self, site: System.Runtime.CompilerServices.CallSite, context: IronPython.Runtime.CodeContext, func: System.Object, arg0: T0, arg1: T1, arg2: T2, arg3: T3, arg4: T4, arg5: T5, arg6: T6, ) -> System.Object:
        ...

    def Default1Call7(self, site: System.Runtime.CompilerServices.CallSite, context: IronPython.Runtime.CodeContext, func: System.Object, arg0: T0, arg1: T1, arg2: T2, arg3: T3, arg4: T4, arg5: T5, arg6: T6, ) -> System.Object:
        ...

    def Default2Call7(self, site: System.Runtime.CompilerServices.CallSite, context: IronPython.Runtime.CodeContext, func: System.Object, arg0: T0, arg1: T1, arg2: T2, arg3: T3, arg4: T4, arg5: T5, arg6: T6, ) -> System.Object:
        ...

    def Default3Call7(self, site: System.Runtime.CompilerServices.CallSite, context: IronPython.Runtime.CodeContext, func: System.Object, arg0: T0, arg1: T1, arg2: T2, arg3: T3, arg4: T4, arg5: T5, arg6: T6, ) -> System.Object:
        ...

    def Default4Call7(self, site: System.Runtime.CompilerServices.CallSite, context: IronPython.Runtime.CodeContext, func: System.Object, arg0: T0, arg1: T1, arg2: T2, arg3: T3, arg4: T4, arg5: T5, arg6: T6, ) -> System.Object:
        ...

    def Default5Call7(self, site: System.Runtime.CompilerServices.CallSite, context: IronPython.Runtime.CodeContext, func: System.Object, arg0: T0, arg1: T1, arg2: T2, arg3: T3, arg4: T4, arg5: T5, arg6: T6, ) -> System.Object:
        ...

    def Default6Call7(self, site: System.Runtime.CompilerServices.CallSite, context: IronPython.Runtime.CodeContext, func: System.Object, arg0: T0, arg1: T1, arg2: T2, arg3: T3, arg4: T4, arg5: T5, arg6: T6, ) -> System.Object:
        ...

class Converter(System.Object, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    @staticmethod
    def MakeImplicitConvertSite() -> System.Runtime.CompilerServices.CallSite[System.Func[System.Runtime.CompilerServices.CallSite, System.Object, T]]:
        ...

    @staticmethod
    def MakeExplicitConvertSite() -> System.Runtime.CompilerServices.CallSite[System.Func[System.Runtime.CompilerServices.CallSite, System.Object, T]]:
        ...

    @staticmethod
    def MakeConvertSite(kind: int, ) -> System.Runtime.CompilerServices.CallSite[System.Func[System.Runtime.CompilerServices.CallSite, System.Object, T]]:
        ...

    @staticmethod
    def MakeExplicitTrySite() -> System.Runtime.CompilerServices.CallSite[System.Func[System.Runtime.CompilerServices.CallSite, System.Object, System.Object]]:
        ...

    @staticmethod
    def MakeTrySite(kind: int, ) -> System.Runtime.CompilerServices.CallSite[System.Func[System.Runtime.CompilerServices.CallSite, System.Object, System.Object]]:
        ...

    @staticmethod
    def ConvertToInt32(value: System.Object, ) -> int:
        ...

    @staticmethod
    def ConvertToString(value: System.Object, ) -> str:
        ...

    @staticmethod
    def ConvertToBigInteger(value: System.Object, ) -> System.Numerics.BigInteger:
        ...

    @staticmethod
    def ConvertToDouble(value: System.Object, ) -> float:
        ...

    @staticmethod
    def ConvertToComplex(value: System.Object, ) -> System.Numerics.Complex:
        ...

    @staticmethod
    def ConvertToBoolean(value: System.Object, ) -> bool:
        ...

    @staticmethod
    def ConvertToInt64(value: System.Object, ) -> int:
        ...

    @staticmethod
    def ConvertToByte(value: System.Object, ) -> int:
        ...

    @staticmethod
    def ConvertToSByte(value: System.Object, ) -> int:
        ...

    @staticmethod
    def ConvertToInt16(value: System.Object, ) -> int:
        ...

    @staticmethod
    def ConvertToUInt16(value: System.Object, ) -> int:
        ...

    @staticmethod
    def ConvertToUInt32(value: System.Object, ) -> int:
        ...

    @staticmethod
    def ConvertToUInt64(value: System.Object, ) -> int:
        ...

    @staticmethod
    def ConvertToSingle(value: System.Object, ) -> float:
        ...

    @staticmethod
    def ConvertToDecimal(value: System.Object, ) -> System.Decimal:
        ...

    @staticmethod
    def ConvertToChar(value: System.Object, ) -> str:
        ...

    @staticmethod
    def TryConvertToByte(value: System.Object, result: ref[int], ) -> bool:
        ...

    @staticmethod
    def TryConvertToSByte(value: System.Object, result: ref[int], ) -> bool:
        ...

    @staticmethod
    def TryConvertToInt16(value: System.Object, result: ref[int], ) -> bool:
        ...

    @staticmethod
    def TryConvertToInt32(value: System.Object, result: ref[int], ) -> bool:
        ...

    @staticmethod
    def TryConvertToInt64(value: System.Object, result: ref[int], ) -> bool:
        ...

    @staticmethod
    def TryConvertToUInt16(value: System.Object, result: ref[int], ) -> bool:
        ...

    @staticmethod
    def TryConvertToUInt32(value: System.Object, result: ref[int], ) -> bool:
        ...

    @staticmethod
    def TryConvertToUInt64(value: System.Object, result: ref[int], ) -> bool:
        ...

    @staticmethod
    def TryConvertToDouble(value: System.Object, result: ref[float], ) -> bool:
        ...

    @staticmethod
    def TryConvertToBigInteger(value: System.Object, result: ref[System.Numerics.BigInteger], ) -> bool:
        ...

    @staticmethod
    def TryConvertToComplex(value: System.Object, result: ref[System.Numerics.Complex], ) -> bool:
        ...

    @staticmethod
    def TryConvertToString(value: System.Object, result: ref[str], ) -> bool:
        ...

    @staticmethod
    def TryConvertToChar(value: System.Object, result: ref[str], ) -> bool:
        ...

    @staticmethod
    def ExplicitConvertToChar(value: System.Object, ) -> str:
        ...

    @staticmethod
    @typing.overload
    def Convert(value: System.Object, ) -> T:
        ...

    @staticmethod
    @typing.overload
    def Convert(value: System.Object, to: System.Type, ) -> System.Object:
        ...

    @staticmethod
    @typing.overload
    def TryConvert(value: System.Object, result: ref[T], ) -> bool:
        ...

    @staticmethod
    @typing.overload
    def TryConvert(value: System.Object, to: System.Type, result: ref[System.Object], ) -> bool:
        ...

    @staticmethod
    def TryConvertToIEnumerator(o: System.Object, e: ref[System.Collections.IEnumerator], ) -> bool:
        ...

    @staticmethod
    def ConvertToIEnumerator(o: System.Object, ) -> System.Collections.IEnumerator:
        ...

    @staticmethod
    def ConvertToIEnumerable(o: System.Object, ) -> System.Collections.IEnumerable:
        ...

    @staticmethod
    def TryConvertToIndex(value: System.Object, index: ref[int], throwOverflowError: bool = ..., throwNonInt: bool = ..., ) -> bool:
        ...

    @staticmethod
    def ConvertToIndex(value: System.Object, throwOverflowError: bool = ..., ) -> int:
        ...

    @staticmethod
    def TryGetInt(o: System.Object, value: ref[int], throwOverflowError: bool, original: System.Object, ) -> bool:
        ...

    @staticmethod
    def CannotConvertOverflow(name: str, value: System.Object, ) -> System.Exception:
        ...

    @staticmethod
    @typing.overload
    def MakeTypeError(expectedType: System.Type, o: System.Object, ) -> System.Exception:
        ...

    @staticmethod
    @typing.overload
    def MakeTypeError(expectedType: str, o: System.Object, ) -> System.Exception:
        ...

    @staticmethod
    def ConvertToReferenceType(fromObject: System.Object, typeHandle: System.RuntimeTypeHandle, ) -> System.Object:
        ...

    @staticmethod
    def ConvertToNullableType(fromObject: System.Object, typeHandle: System.RuntimeTypeHandle, ) -> System.Object:
        ...

    @staticmethod
    def ConvertToValueType(fromObject: System.Object, typeHandle: System.RuntimeTypeHandle, ) -> System.Object:
        ...

    @staticmethod
    def ConvertToType(value: System.Object, ) -> System.Type:
        ...

    @staticmethod
    def ConvertToDelegate(value: System.Object, to: System.Type, ) -> System.Object:
        ...

    @staticmethod
    def CanConvertFrom(fromType: System.Type, toType: System.Type, allowNarrowing: int, ) -> bool:
        ...

    @staticmethod
    def GetTypeConverter(tca: System.ComponentModel.TypeConverterAttribute, ) -> System.ComponentModel.TypeConverter:
        ...

    @staticmethod
    def HasImplicitNumericConversion(fromType: System.Type, toType: System.Type, ) -> bool:
        ...

    @staticmethod
    def PreferConvert(t1: System.Type, t2: System.Type, ) -> int:
        ...

    @staticmethod
    def HasNarrowingConversion(fromType: System.Type, toType: System.Type, allowNarrowing: int, ) -> bool:
        ...

    @staticmethod
    def HasImplicitConversion(fromType: System.Type, toType: System.Type, ) -> bool:
        ...

    @staticmethod
    def HasImplicitConversionWorker(lookupType: System.Type, fromType: System.Type, toType: System.Type, ) -> bool:
        ...

    @staticmethod
    def ImplicitConvertToInt32(o: System.Object, ) -> System.Nullable[int]:
        ...

    @staticmethod
    def IsNumeric(t: System.Type, ) -> bool:
        ...

    @staticmethod
    def IsFloatingPoint(t: System.Type, ) -> bool:
        ...

    @staticmethod
    def IsInteger(t: System.Type, ) -> bool:
        ...

    @staticmethod
    def IsPythonType(t: System.Type, ) -> bool:
        ...

    @staticmethod
    def HasPythonProtocol(t: System.Type, name: str, ) -> bool:
        ...

class SimpleNamespace(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def __dict__(self) -> IronPython.Runtime.PythonDictionary:
        ...

    # methods
    def __init__(self, kwargsø: System.Collections.Generic.Dictionary[str, System.Object], ):
        ...

    def __repr__(self, context: IronPython.Runtime.CodeContext, ) -> str:
        ...

    @typing.overload
    def __eq__(self, context: IronPython.Runtime.CodeContext, other: IronPython.Runtime.SimpleNamespace, ) -> bool:
        ...

    @typing.overload
    def __eq__(self, context: IronPython.Runtime.CodeContext, other: System.Object, ) -> System.Object:
        ...

class ItemEnumerator(System.Collections.IEnumerator, System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def Current(self) -> System.Object:
        ...

    # methods
    def __init__(self, source: System.Object, getItemMethod: System.Object, site: System.Runtime.CompilerServices.CallSite[System.Func[System.Runtime.CompilerServices.CallSite, IronPython.Runtime.CodeContext, System.Object, int, System.Object]], ):
        ...

    def __reduce__(self, context: IronPython.Runtime.CodeContext, ) -> IronPython.Runtime.PythonTuple:
        ...

    def __setstate__(self, index: int, ) -> None:
        ...

    def MoveNext(self, ) -> bool:
        ...

    def Reset(self, ) -> None:
        ...

class FunctionCaller(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        self._compat: int
        ...

    # static fields

    # properties
    # methods
    def __init__(self, compat: int, ):
        ...

    def Call0(self, site: System.Runtime.CompilerServices.CallSite, context: IronPython.Runtime.CodeContext, func: System.Object, ) -> System.Object:
        ...

    def Default1Call0(self, site: System.Runtime.CompilerServices.CallSite, context: IronPython.Runtime.CodeContext, func: System.Object, ) -> System.Object:
        ...

    def Default2Call0(self, site: System.Runtime.CompilerServices.CallSite, context: IronPython.Runtime.CodeContext, func: System.Object, ) -> System.Object:
        ...

    def Default3Call0(self, site: System.Runtime.CompilerServices.CallSite, context: IronPython.Runtime.CodeContext, func: System.Object, ) -> System.Object:
        ...

    def Default4Call0(self, site: System.Runtime.CompilerServices.CallSite, context: IronPython.Runtime.CodeContext, func: System.Object, ) -> System.Object:
        ...

    def Default5Call0(self, site: System.Runtime.CompilerServices.CallSite, context: IronPython.Runtime.CodeContext, func: System.Object, ) -> System.Object:
        ...

    def Default6Call0(self, site: System.Runtime.CompilerServices.CallSite, context: IronPython.Runtime.CodeContext, func: System.Object, ) -> System.Object:
        ...

    def Default7Call0(self, site: System.Runtime.CompilerServices.CallSite, context: IronPython.Runtime.CodeContext, func: System.Object, ) -> System.Object:
        ...

    def Default8Call0(self, site: System.Runtime.CompilerServices.CallSite, context: IronPython.Runtime.CodeContext, func: System.Object, ) -> System.Object:
        ...

    def Default9Call0(self, site: System.Runtime.CompilerServices.CallSite, context: IronPython.Runtime.CodeContext, func: System.Object, ) -> System.Object:
        ...

    def Default10Call0(self, site: System.Runtime.CompilerServices.CallSite, context: IronPython.Runtime.CodeContext, func: System.Object, ) -> System.Object:
        ...

    def Default11Call0(self, site: System.Runtime.CompilerServices.CallSite, context: IronPython.Runtime.CodeContext, func: System.Object, ) -> System.Object:
        ...

    def Default12Call0(self, site: System.Runtime.CompilerServices.CallSite, context: IronPython.Runtime.CodeContext, func: System.Object, ) -> System.Object:
        ...

    def Default13Call0(self, site: System.Runtime.CompilerServices.CallSite, context: IronPython.Runtime.CodeContext, func: System.Object, ) -> System.Object:
        ...

class Profiler(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    def __init__(self, ):
        ...

    @staticmethod
    def GetProfiler(context: IronPython.Runtime.PythonContext, ) -> IronPython.Runtime.Profiler:
        ...

    @staticmethod
    def FormatMethodName(method: System.Reflection.MethodBase, ) -> str:
        ...

    @typing.overload
    def GetProfilerIndex(self, method: System.Reflection.MethodBase, ) -> int:
        ...

    @typing.overload
    def GetProfilerIndex(self, name: str, ) -> int:
        ...

    def GetNewProfilerIndex(self, name: str, ) -> int:
        ...

    def GetProfile(self, includeUnused: bool, ) -> System.Collections.Generic.List[IronPython.Runtime.Profiler.Data]:
        ...

    def Reset(self, ) -> None:
        ...

    @staticmethod
    def DateTimeTicksFromTimeData(elapsedStopwatchTicks: int, ) -> int:
        ...

    def StartCall(self, index: int, ) -> int:
        ...

    def StartNestedCall(self, index: int, timestamp: int, ) -> int:
        ...

    def FinishNestedCall(self, index: int, timestamp: int, ) -> int:
        ...

    def FinishCall(self, index: int, timestamp: int, ) -> None:
        ...

    def AddOuterProfiling(self, body: System.Linq.Expressions.Expression, tick: System.Linq.Expressions.ParameterExpression, profileIndex: int, ) -> System.Linq.Expressions.Expression:
        ...

    def AddInnerProfiling(self, body: System.Linq.Expressions.Expression, tick: System.Linq.Expressions.ParameterExpression, profileIndex: int, ) -> System.Linq.Expressions.Expression:
        ...

    @staticmethod
    def IgnoreMethod(method: System.Reflection.MethodBase, ) -> bool:
        ...

    @typing.overload
    def AddProfiling(self, body: System.Linq.Expressions.Expression, tick: System.Linq.Expressions.ParameterExpression, name: str, unique: bool, ) -> System.Linq.Expressions.Expression:
        ...

    @typing.overload
    def AddProfiling(self, body: System.Linq.Expressions.Expression, method: System.Reflection.MethodBase, ) -> System.Linq.Expressions.Expression:
        ...

class classmethod(IronPython.Runtime.Types.PythonTypeSlot):
    @typing.overload
    def __init__(self, **kwargs):
        self._func: System.Object
        ...

    # static fields

    # properties
    @property
    def GetAlwaysSucceeds(self) -> bool:
        ...

    @property
    def __func__(self) -> System.Object:
        ...

    @property
    def __isabstractmethod__(self) -> bool:
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

    def __init__(self, context: IronPython.Runtime.CodeContext, func: System.Object, ) -> None:
        ...

    def TryGetValue(self, context: IronPython.Runtime.CodeContext, instance: System.Object, owner: IronPython.Runtime.Types.PythonType, value: ref[System.Object], ) -> bool:
        ...

    def __get__(self, instance: System.Object, owner: System.Object = ..., ) -> System.Object:
        ...

class CompileFlags(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    CO_NESTED: int = ...
    CO_DONT_IMPLY_DEDENT: int = ...
    CO_GENERATOR_ALLOWED: int = ...
    CO_FUTURE_DIVISION: int = ...
    CO_FUTURE_ABSOLUTE_IMPORT: int = ...
    CO_FUTURE_WITH_STATEMENT: int = ...
    CO_FUTURE_PRINT_FUNCTION: int = ...
    CO_FUTURE_UNICODE_LITERALS: int = ...
    CO_FUTURE_BARRY_AS_BDFL: int = ...
    CO_FUTURE_GENERATOR_STOP: int = ...

class Bytes(System.Collections.Generic.IList[int], System.Collections.Generic.ICollection[int], System.Collections.Generic.IEnumerable[int], System.Collections.IEnumerable, System.Collections.Generic.IReadOnlyList[int], System.Collections.Generic.IReadOnlyCollection[int], System.IEquatable[IronPython.Runtime.Bytes], IronPython.Runtime.ICodeFormattable, Microsoft.Scripting.Runtime.IExpressionSerializable, IronPython.Runtime.IBufferProtocol, System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields
    Empty: IronPython.Runtime.Bytes = ...

    # properties
    @property
    def UnsafeByteArray(self) -> System.Array[int]:
        ...

    @property
    def Item(self) -> int:
        ...
    @Item.setter
    def Item(self, val: int):
        ...

    @property
    def Item(self) -> int:
        ...

    @property
    def Item(self) -> IronPython.Runtime.Bytes:
        ...

    @property
    def Item(self) -> int:
        ...

    @property
    def Item(self) -> int:
        ...
    @Item.setter
    def Item(self, val: int):
        ...

    @property
    def Item(self) -> int:
        ...

    @property
    def Count(self) -> int:
        ...

    @property
    def IsReadOnly(self) -> bool:
        ...

    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def __init__(self, bytes: IronPython.Runtime.Bytes, ):
        ...

    @typing.overload
    def __init__(self, bytes: System.Collections.Generic.IEnumerable[int], ):
        ...

    @typing.overload
    def __init__(self, source: IronPython.Runtime.IBufferProtocol, ):
        ...

    @typing.overload
    def __init__(self, bytes: System.Array[int], ):
        ...

    def AsMemory(self, ) -> System.ReadOnlyMemory[int]:
        ...

    def AsSpan(self, ) -> System.ReadOnlySpan[int]:
        ...

    @staticmethod
    def TryInvokeBytesOperator(context: IronPython.Runtime.CodeContext, obj: System.Object, bytes: ref[IronPython.Runtime.Bytes], ) -> bool:
        ...

    @staticmethod
    def JoinOne(curVal: System.Object, ) -> IronPython.Runtime.Bytes:
        ...

    @staticmethod
    def Concat(list: System.Collections.Generic.IList[IronPython.Runtime.Bytes], length: int, ) -> IronPython.Runtime.Bytes:
        ...

    def IndexOf(self, item: int, ) -> int:
        ...

    def Insert(self, index: int, item: int, ) -> None:
        ...

    def RemoveAt(self, index: int, ) -> None:
        ...

    def Add(self, item: int, ) -> None:
        ...

    def Clear(self, ) -> None:
        ...

    def Contains(self, item: int, ) -> bool:
        ...

    def CopyTo(self, array: System.Array[int], arrayIndex: int, ) -> None:
        ...

    def Remove(self, item: int, ) -> bool:
        ...

    def GetEnumerator(self, ) -> System.Collections.Generic.IEnumerator[int]:
        ...

    def GetEnumerator(self, ) -> System.Collections.IEnumerator:
        ...

    @typing.overload
    def __eq__(self, context: IronPython.Runtime.CodeContext, value: IronPython.Runtime.Bytes, ) -> bool:
        ...

    @typing.overload
    def __eq__(self, context: IronPython.Runtime.CodeContext, value: str, ) -> bool:
        ...

    @typing.overload
    def __eq__(self, context: IronPython.Runtime.CodeContext, value: Microsoft.Scripting.Runtime.Extensible[str], ) -> bool:
        ...

    @typing.overload
    def __eq__(self, context: IronPython.Runtime.CodeContext, value: System.Object, ) -> IronPython.Runtime.Types.NotImplementedType:
        ...

    @typing.overload
    def __ne__(self, context: IronPython.Runtime.CodeContext, value: IronPython.Runtime.Bytes, ) -> bool:
        ...

    @typing.overload
    def __ne__(self, context: IronPython.Runtime.CodeContext, value: str, ) -> bool:
        ...

    @typing.overload
    def __ne__(self, context: IronPython.Runtime.CodeContext, value: Microsoft.Scripting.Runtime.Extensible[str], ) -> bool:
        ...

    @typing.overload
    def __ne__(self, context: IronPython.Runtime.CodeContext, value: System.Object, ) -> IronPython.Runtime.Types.NotImplementedType:
        ...

    @typing.overload
    def Equals(self, other: IronPython.Runtime.Bytes, ) -> bool:
        ...

    @typing.overload
    def Equals(self, obj: System.Object, ) -> bool:
        ...

    def GetHashCode(self, ) -> int:
        ...

    def CreateExpression(self, ) -> System.Linq.Expressions.Expression:
        ...

    def GetBuffer(self, flags: int, ) -> IronPython.Runtime.IPythonBuffer:
        ...

    @typing.overload
    def lstrip(self, ) -> IronPython.Runtime.Bytes:
        ...

    @typing.overload
    def lstrip(self, chars: System.Collections.Generic.IList[int], ) -> IronPython.Runtime.Bytes:
        ...

    @staticmethod
    def maketrans(from_: System.Collections.Generic.IList[int], to: System.Collections.Generic.IList[int], ) -> IronPython.Runtime.Bytes:
        ...

    def partition(self, sep: System.Collections.Generic.IList[int], ) -> IronPython.Runtime.PythonTuple:
        ...

    @typing.overload
    def replace(self, old: System.Collections.Generic.IList[int], new: System.Collections.Generic.IList[int], ) -> IronPython.Runtime.Bytes:
        ...

    @typing.overload
    def replace(self, old: System.Collections.Generic.IList[int], new: System.Collections.Generic.IList[int], count: int, ) -> IronPython.Runtime.Bytes:
        ...

    @typing.overload
    def rfind(self, sub: System.Collections.Generic.IList[int], ) -> int:
        ...

    @typing.overload
    def rfind(self, sub: System.Collections.Generic.IList[int], start: int, ) -> int:
        ...

    @typing.overload
    def rfind(self, sub: System.Collections.Generic.IList[int], start: int, end: int, ) -> int:
        ...

    @typing.overload
    def rfind(self, sub: System.Collections.Generic.IList[int], start: System.Object, ) -> int:
        ...

    @typing.overload
    def rfind(self, sub: System.Collections.Generic.IList[int], start: System.Object, end: System.Object, ) -> int:
        ...

    @typing.overload
    def rfind(self, byte: System.Numerics.BigInteger, ) -> int:
        ...

    @typing.overload
    def rfind(self, byte: System.Numerics.BigInteger, start: int, ) -> int:
        ...

    @typing.overload
    def rfind(self, byte: System.Numerics.BigInteger, start: int, end: int, ) -> int:
        ...

    @typing.overload
    def rfind(self, byte: System.Numerics.BigInteger, start: System.Object, ) -> int:
        ...

    @typing.overload
    def rfind(self, byte: System.Numerics.BigInteger, start: System.Object, end: System.Object, ) -> int:
        ...

    @typing.overload
    def rindex(self, sub: System.Collections.Generic.IList[int], ) -> int:
        ...

    @typing.overload
    def rindex(self, sub: System.Collections.Generic.IList[int], start: int, ) -> int:
        ...

    @typing.overload
    def rindex(self, sub: System.Collections.Generic.IList[int], start: int, end: int, ) -> int:
        ...

    @typing.overload
    def rindex(self, sub: System.Collections.Generic.IList[int], start: System.Object, ) -> int:
        ...

    @typing.overload
    def rindex(self, sub: System.Collections.Generic.IList[int], start: System.Object, end: System.Object, ) -> int:
        ...

    @typing.overload
    def rindex(self, byte: System.Numerics.BigInteger, ) -> int:
        ...

    @typing.overload
    def rindex(self, byte: System.Numerics.BigInteger, start: int, ) -> int:
        ...

    @typing.overload
    def rindex(self, byte: System.Numerics.BigInteger, start: int, end: int, ) -> int:
        ...

    @typing.overload
    def rindex(self, byte: System.Numerics.BigInteger, start: System.Object, ) -> int:
        ...

    @typing.overload
    def rindex(self, byte: System.Numerics.BigInteger, start: System.Object, end: System.Object, ) -> int:
        ...

    @typing.overload
    def rjust(self, width: int, ) -> IronPython.Runtime.Bytes:
        ...

    @typing.overload
    def rjust(self, width: int, fillchar: System.Collections.Generic.IList[int], ) -> IronPython.Runtime.Bytes:
        ...

    @typing.overload
    def rjust(self, width: int, fillchar: int, ) -> IronPython.Runtime.Bytes:
        ...

    def rpartition(self, sep: System.Collections.Generic.IList[int], ) -> IronPython.Runtime.PythonTuple:
        ...

    def rsplit(self, sep: System.Collections.Generic.IList[int] = ..., maxsplit: int = ..., ) -> IronPython.Runtime.PythonList:
        ...

    @typing.overload
    def rstrip(self, ) -> IronPython.Runtime.Bytes:
        ...

    @typing.overload
    def rstrip(self, chars: System.Collections.Generic.IList[int], ) -> IronPython.Runtime.Bytes:
        ...

    def split(self, sep: System.Collections.Generic.IList[int] = ..., maxsplit: int = ..., ) -> IronPython.Runtime.PythonList:
        ...

    @typing.overload
    def splitlines(self, ) -> IronPython.Runtime.PythonList:
        ...

    @typing.overload
    def splitlines(self, keepends: bool, ) -> IronPython.Runtime.PythonList:
        ...

    @typing.overload
    def startswith(self, prefix: System.Collections.Generic.IList[int], ) -> bool:
        ...

    @typing.overload
    def startswith(self, prefix: System.Collections.Generic.IList[int], start: int, ) -> bool:
        ...

    @typing.overload
    def startswith(self, prefix: System.Collections.Generic.IList[int], start: int, end: int, ) -> bool:
        ...

    @typing.overload
    def startswith(self, prefix: System.Collections.Generic.IList[int], start: System.Object, ) -> bool:
        ...

    @typing.overload
    def startswith(self, prefix: System.Collections.Generic.IList[int], start: System.Object, end: System.Object, ) -> bool:
        ...

    @typing.overload
    def startswith(self, prefix: IronPython.Runtime.PythonTuple, ) -> bool:
        ...

    @typing.overload
    def startswith(self, prefix: IronPython.Runtime.PythonTuple, start: int, ) -> bool:
        ...

    @typing.overload
    def startswith(self, prefix: IronPython.Runtime.PythonTuple, start: int, end: int, ) -> bool:
        ...

    @typing.overload
    def startswith(self, prefix: IronPython.Runtime.PythonTuple, start: System.Object, ) -> bool:
        ...

    @typing.overload
    def startswith(self, prefix: IronPython.Runtime.PythonTuple, start: System.Object, end: System.Object, ) -> bool:
        ...

    @typing.overload
    def startswith(self, prefix: System.Object, start: System.Object = ..., end: System.Object = ..., ) -> bool:
        ...

    @typing.overload
    def strip(self, ) -> IronPython.Runtime.Bytes:
        ...

    @typing.overload
    def strip(self, chars: System.Collections.Generic.IList[int], ) -> IronPython.Runtime.Bytes:
        ...

    def swapcase(self, ) -> IronPython.Runtime.Bytes:
        ...

    def title(self, ) -> IronPython.Runtime.Bytes:
        ...

    def ValidateTable(self, table: System.Collections.Generic.IList[int], ) -> None:
        ...

    @typing.overload
    def translate(self, table: System.Collections.Generic.IList[int], ) -> IronPython.Runtime.Bytes:
        ...

    @typing.overload
    def translate(self, table: System.Collections.Generic.IList[int], delete: System.Collections.Generic.IList[int], ) -> IronPython.Runtime.Bytes:
        ...

    @typing.overload
    def translate(self, table: System.Collections.Generic.IList[int], delete: System.Object, ) -> IronPython.Runtime.Bytes:
        ...

    def upper(self, ) -> IronPython.Runtime.Bytes:
        ...

    def zfill(self, width: int, ) -> IronPython.Runtime.Bytes:
        ...

    @typing.overload
    def __contains__(self, bytes: System.Collections.Generic.IList[int], ) -> bool:
        ...

    @typing.overload
    def __contains__(self, context: IronPython.Runtime.CodeContext, value: int, ) -> bool:
        ...

    @typing.overload
    def __contains__(self, context: IronPython.Runtime.CodeContext, value: System.Object, ) -> bool:
        ...

    def __getnewargs__(self, ) -> IronPython.Runtime.PythonTuple:
        ...

    def __iter__(self, ) -> System.Collections.Generic.IEnumerator[int]:
        ...

    def __mod__(self, context: IronPython.Runtime.CodeContext, value: System.Object, ) -> IronPython.Runtime.Bytes:
        ...

    @typing.overload
    def __rmod__(self, context: IronPython.Runtime.CodeContext, value: IronPython.Runtime.Bytes, ) -> IronPython.Runtime.Bytes:
        ...

    @typing.overload
    def __rmod__(self, context: IronPython.Runtime.CodeContext, value: System.Object, ) -> IronPython.Runtime.Types.NotImplementedType:
        ...

    def __str__(self, context: IronPython.Runtime.CodeContext, ) -> str:
        ...

    def __repr__(self, context: IronPython.Runtime.CodeContext, ) -> str:
        ...

    def ToString(self, ) -> str:
        ...

    @staticmethod
    def MultiplyWorker(self: IronPython.Runtime.Bytes, count: int, ) -> IronPython.Runtime.Bytes:
        ...

    @staticmethod
    @typing.overload
    def __new__(context: IronPython.Runtime.CodeContext, cls: IronPython.Runtime.Types.PythonType, ) -> System.Object:
        ...

    @staticmethod
    @typing.overload
    def __new__(context: IronPython.Runtime.CodeContext, cls: IronPython.Runtime.Types.PythonType, source: IronPython.Runtime.IBufferProtocol, ) -> System.Object:
        ...

    @staticmethod
    @typing.overload
    def __new__(context: IronPython.Runtime.CodeContext, cls: IronPython.Runtime.Types.PythonType, object: System.Object, ) -> System.Object:
        ...

    @staticmethod
    @typing.overload
    def __new__(context: IronPython.Runtime.CodeContext, cls: IronPython.Runtime.Types.PythonType, size: int, ) -> System.Object:
        ...

    @staticmethod
    @typing.overload
    def __new__(context: IronPython.Runtime.CodeContext, cls: IronPython.Runtime.Types.PythonType, size: System.Numerics.BigInteger, ) -> System.Object:
        ...

    @staticmethod
    @typing.overload
    def __new__(context: IronPython.Runtime.CodeContext, cls: IronPython.Runtime.Types.PythonType, size: Microsoft.Scripting.Runtime.Extensible[System.Numerics.BigInteger], ) -> System.Object:
        ...

    @staticmethod
    @typing.overload
    def __new__(context: IronPython.Runtime.CodeContext, cls: IronPython.Runtime.Types.PythonType, string: IronPython.Runtime.Operations.ExtensibleString, ) -> System.Object:
        ...

    @staticmethod
    @typing.overload
    def __new__(context: IronPython.Runtime.CodeContext, cls: IronPython.Runtime.Types.PythonType, string: str, ) -> System.Object:
        ...

    @staticmethod
    @typing.overload
    def __new__(context: IronPython.Runtime.CodeContext, cls: IronPython.Runtime.Types.PythonType, string: str, encoding: str, ) -> System.Object:
        ...

    @staticmethod
    @typing.overload
    def __new__(context: IronPython.Runtime.CodeContext, cls: IronPython.Runtime.Types.PythonType, string: str, encoding: str, errors: str, ) -> System.Object:
        ...

    @staticmethod
    def FromByte(b: int, ) -> IronPython.Runtime.Bytes:
        ...

    @staticmethod
    def FromObject(context: IronPython.Runtime.CodeContext, o: System.Object, ) -> IronPython.Runtime.Bytes:
        ...

    @staticmethod
    def Make(bytes: System.Array[int], ) -> IronPython.Runtime.Bytes:
        ...

    def AsBytes(self, ) -> IronPython.Runtime.Bytes:
        ...

    def capitalize(self, ) -> IronPython.Runtime.Bytes:
        ...

    @typing.overload
    def center(self, width: int, ) -> IronPython.Runtime.Bytes:
        ...

    @typing.overload
    def center(self, width: int, fillchar: System.Collections.Generic.IList[int], ) -> IronPython.Runtime.Bytes:
        ...

    @typing.overload
    def center(self, width: int, fillchar: int, ) -> IronPython.Runtime.Bytes:
        ...

    @typing.overload
    def count(self, sub: System.Collections.Generic.IList[int], ) -> int:
        ...

    @typing.overload
    def count(self, sub: System.Collections.Generic.IList[int], start: int, ) -> int:
        ...

    @typing.overload
    def count(self, sub: System.Collections.Generic.IList[int], start: int, end: int, ) -> int:
        ...

    @typing.overload
    def count(self, sub: System.Collections.Generic.IList[int], start: System.Object, ) -> int:
        ...

    @typing.overload
    def count(self, sub: System.Collections.Generic.IList[int], start: System.Object, end: System.Object, ) -> int:
        ...

    @typing.overload
    def count(self, byte: System.Numerics.BigInteger, ) -> int:
        ...

    @typing.overload
    def count(self, byte: System.Numerics.BigInteger, start: int, ) -> int:
        ...

    @typing.overload
    def count(self, byte: System.Numerics.BigInteger, start: int, end: int, ) -> int:
        ...

    @typing.overload
    def count(self, byte: System.Numerics.BigInteger, start: System.Object, ) -> int:
        ...

    @typing.overload
    def count(self, byte: System.Numerics.BigInteger, start: System.Object, end: System.Object, ) -> int:
        ...

    @typing.overload
    def decode(self, context: IronPython.Runtime.CodeContext, encoding: str = ..., errors: str = ..., ) -> str:
        ...

    @typing.overload
    def decode(self, context: IronPython.Runtime.CodeContext, encoding: System.Text.Encoding, errors: str = ..., ) -> str:
        ...

    @typing.overload
    def endswith(self, suffix: System.Collections.Generic.IList[int], ) -> bool:
        ...

    @typing.overload
    def endswith(self, suffix: System.Collections.Generic.IList[int], start: int, ) -> bool:
        ...

    @typing.overload
    def endswith(self, suffix: System.Collections.Generic.IList[int], start: int, end: int, ) -> bool:
        ...

    @typing.overload
    def endswith(self, suffix: System.Collections.Generic.IList[int], start: System.Object, ) -> bool:
        ...

    @typing.overload
    def endswith(self, suffix: System.Collections.Generic.IList[int], start: System.Object, end: System.Object, ) -> bool:
        ...

    @typing.overload
    def endswith(self, suffix: IronPython.Runtime.PythonTuple, ) -> bool:
        ...

    @typing.overload
    def endswith(self, suffix: IronPython.Runtime.PythonTuple, start: int, ) -> bool:
        ...

    @typing.overload
    def endswith(self, suffix: IronPython.Runtime.PythonTuple, start: int, end: int, ) -> bool:
        ...

    @typing.overload
    def endswith(self, suffix: IronPython.Runtime.PythonTuple, start: System.Object, ) -> bool:
        ...

    @typing.overload
    def endswith(self, suffix: IronPython.Runtime.PythonTuple, start: System.Object, end: System.Object, ) -> bool:
        ...

    @typing.overload
    def endswith(self, suffix: System.Object, start: System.Object = ..., end: System.Object = ..., ) -> bool:
        ...

    @typing.overload
    def expandtabs(self, ) -> IronPython.Runtime.Bytes:
        ...

    @typing.overload
    def expandtabs(self, tabsize: int, ) -> IronPython.Runtime.Bytes:
        ...

    @typing.overload
    def find(self, sub: System.Collections.Generic.IList[int], ) -> int:
        ...

    @typing.overload
    def find(self, sub: System.Collections.Generic.IList[int], start: int, ) -> int:
        ...

    @typing.overload
    def find(self, sub: System.Collections.Generic.IList[int], start: int, end: int, ) -> int:
        ...

    @typing.overload
    def find(self, sub: System.Collections.Generic.IList[int], start: System.Object, ) -> int:
        ...

    @typing.overload
    def find(self, sub: System.Collections.Generic.IList[int], start: System.Object, end: System.Object, ) -> int:
        ...

    @typing.overload
    def find(self, byte: System.Numerics.BigInteger, ) -> int:
        ...

    @typing.overload
    def find(self, byte: System.Numerics.BigInteger, start: int, ) -> int:
        ...

    @typing.overload
    def find(self, byte: System.Numerics.BigInteger, start: int, end: int, ) -> int:
        ...

    @typing.overload
    def find(self, byte: System.Numerics.BigInteger, start: System.Object, ) -> int:
        ...

    @typing.overload
    def find(self, byte: System.Numerics.BigInteger, start: System.Object, end: System.Object, ) -> int:
        ...

    @staticmethod
    def fromhex(string: str, ) -> IronPython.Runtime.Bytes:
        ...

    def hex(self, ) -> str:
        ...

    @staticmethod
    def ToHex(bytes: System.ReadOnlySpan[int], ) -> str:
        ...

    @typing.overload
    def index(self, sub: System.Collections.Generic.IList[int], ) -> int:
        ...

    @typing.overload
    def index(self, sub: System.Collections.Generic.IList[int], start: int, ) -> int:
        ...

    @typing.overload
    def index(self, sub: System.Collections.Generic.IList[int], start: int, end: int, ) -> int:
        ...

    @typing.overload
    def index(self, sub: System.Collections.Generic.IList[int], start: System.Object, ) -> int:
        ...

    @typing.overload
    def index(self, sub: System.Collections.Generic.IList[int], start: System.Object, end: System.Object, ) -> int:
        ...

    @typing.overload
    def index(self, byte: System.Numerics.BigInteger, ) -> int:
        ...

    @typing.overload
    def index(self, byte: System.Numerics.BigInteger, start: System.Nullable[int], ) -> int:
        ...

    @typing.overload
    def index(self, byte: System.Numerics.BigInteger, start: int, end: int, ) -> int:
        ...

    @typing.overload
    def index(self, byte: System.Numerics.BigInteger, start: System.Object, ) -> int:
        ...

    @typing.overload
    def index(self, byte: System.Numerics.BigInteger, start: System.Object, end: System.Object, ) -> int:
        ...

    def isalnum(self, ) -> bool:
        ...

    def isalpha(self, ) -> bool:
        ...

    def isdigit(self, ) -> bool:
        ...

    def islower(self, ) -> bool:
        ...

    def isspace(self, ) -> bool:
        ...

    def istitle(self, ) -> bool:
        ...

    def isupper(self, ) -> bool:
        ...

    @typing.overload
    def join(self, sequence: System.Object, ) -> IronPython.Runtime.Bytes:
        ...

    @typing.overload
    def join(self, sequence: IronPython.Runtime.PythonList, ) -> IronPython.Runtime.Bytes:
        ...

    @typing.overload
    def ljust(self, width: int, ) -> IronPython.Runtime.Bytes:
        ...

    @typing.overload
    def ljust(self, width: int, fillchar: System.Collections.Generic.IList[int], ) -> IronPython.Runtime.Bytes:
        ...

    @typing.overload
    def ljust(self, width: int, fillchar: int, ) -> IronPython.Runtime.Bytes:
        ...

    def lower(self, ) -> IronPython.Runtime.Bytes:
        ...

class SequenceTypeInfoAttribute(System.Attribute):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def Types(self) -> System.Collections.ObjectModel.ReadOnlyCollection[System.Type]:
        ...

    @property
    def TypeId(self) -> System.Object:
        ...

    # methods
    def __init__(self, types: System.Array[System.Type], ):
        ...

class Super(IronPython.Runtime.ICodeFormattable, IronPython.Runtime.Types.PythonTypeSlot):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def __thisclass__(self) -> IronPython.Runtime.Types.PythonType:
        ...

    @property
    def __self__(self) -> System.Object:
        ...

    @property
    def __self_class__(self) -> System.Object:
        ...

    @property
    def DescriptorContext(self) -> IronPython.Runtime.Types.PythonType:
        ...

    @property
    def PythonType(self) -> IronPython.Runtime.Types.PythonType:
        ...

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

    @typing.overload
    def __init__(self, ) -> None:
        ...

    @typing.overload
    def __init__(self, type: IronPython.Runtime.Types.PythonType, ) -> None:
        ...

    @typing.overload
    def __init__(self, type: IronPython.Runtime.Types.PythonType, obj: System.Object, ) -> None:
        ...

    def __get__(self, context: IronPython.Runtime.CodeContext, instance: System.Object, owner: System.Object, ) -> System.Object:
        ...

    def TryLookupInBase(self, context: IronPython.Runtime.CodeContext, pt: IronPython.Runtime.Types.PythonType, name: str, self: System.Object, value: ref[System.Object], ) -> bool:
        ...

    def TryGetValue(self, context: IronPython.Runtime.CodeContext, instance: System.Object, owner: IronPython.Runtime.Types.PythonType, value: ref[System.Object], ) -> bool:
        ...

    def __repr__(self, context: IronPython.Runtime.CodeContext, ) -> str:
        ...

class SentinelIterator(System.Collections.IEnumerator, System.Collections.Generic.IEnumerator[System.Object], System.IDisposable, System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def Current(self) -> System.Object:
        ...

    @property
    def Current(self) -> System.Object:
        ...

    # methods
    def __init__(self, context: IronPython.Runtime.CodeContext, target: System.Object, sentinel: System.Object, ):
        ...

    def __iter__(self, ) -> System.Object:
        ...

    def __next__(self, ) -> System.Object:
        ...

    def MoveNext(self, ) -> bool:
        ...

    def Reset(self, ) -> None:
        ...

    def Dispose(self, ) -> None:
        ...

class DictionaryGenericWrapper(System.Collections.Generic.IDictionary[K, V], System.Collections.Generic.ICollection[System.Collections.Generic.KeyValuePair[K, V]], System.Collections.Generic.IEnumerable[System.Collections.Generic.KeyValuePair[K, V]], System.Collections.IEnumerable, System.Object, typing.Generic[K, V]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def Keys(self) -> System.Collections.Generic.ICollection[K]:
        ...

    @property
    def Values(self) -> System.Collections.Generic.ICollection[V]:
        ...

    @property
    def Item(self) -> V:
        ...
    @Item.setter
    def Item(self, val: V):
        ...

    @property
    def Count(self) -> int:
        ...

    @property
    def IsReadOnly(self) -> bool:
        ...

    # methods
    def __init__(self, self: System.Collections.Generic.IDictionary[System.Object, System.Object], ):
        ...

    @typing.overload
    def Add(self, key: K, value: V, ) -> None:
        ...

    @typing.overload
    def Add(self, item: System.Collections.Generic.KeyValuePair[K, V], ) -> None:
        ...

    def ContainsKey(self, key: K, ) -> bool:
        ...

    @typing.overload
    def Remove(self, key: K, ) -> bool:
        ...

    @typing.overload
    def Remove(self, item: System.Collections.Generic.KeyValuePair[K, V], ) -> bool:
        ...

    def TryGetValue(self, key: K, value: ref[V], ) -> bool:
        ...

    def Clear(self, ) -> None:
        ...

    def Contains(self, item: System.Collections.Generic.KeyValuePair[K, V], ) -> bool:
        ...

    def CopyTo(self, array: System.Array[System.Collections.Generic.KeyValuePair[K, V]], arrayIndex: int, ) -> None:
        ...

    def GetEnumerator(self, ) -> System.Collections.Generic.IEnumerator[System.Collections.Generic.KeyValuePair[K, V]]:
        ...

    def GetEnumerator(self, ) -> System.Collections.IEnumerator:
        ...

    @staticmethod
    def CastKey(key: System.Object, ) -> K:
        ...

    @staticmethod
    def CastValue(val: System.Object, ) -> V:
        ...

    @staticmethod
    def IsValidKey32(key: K, key32: ref[System.Object], ) -> bool:
        ...

class PythonFunction(IronPython.Runtime.IWeakReferenceable, IronPython.Runtime.IPythonMembersList, Microsoft.Scripting.Runtime.IMembersList, System.Dynamic.IDynamicMetaObjectProvider, IronPython.Runtime.ICodeFormattable, IronPython.Runtime.Binding.IFastInvokable, IronPython.Runtime.Types.PythonTypeSlot):
    @typing.overload
    def __init__(self, **kwargs):
        self.Closure: Microsoft.Scripting.MutableTuple
        self._dict: IronPython.Runtime.PythonDictionary
        self._id: int
        ...

    # static fields

    # properties
    @property
    def __globals__(self) -> System.Object:
        ...
    @__globals__.setter
    def __globals__(self, val: System.Object):
        ...

    @property
    def __annotations__(self) -> IronPython.Runtime.PythonDictionary:
        ...
    @__annotations__.setter
    def __annotations__(self, val: IronPython.Runtime.PythonDictionary):
        ...

    @property
    def __defaults__(self) -> IronPython.Runtime.PythonTuple:
        ...
    @__defaults__.setter
    def __defaults__(self, val: IronPython.Runtime.PythonTuple):
        ...

    @property
    def __kwdefaults__(self) -> IronPython.Runtime.PythonDictionary:
        ...
    @__kwdefaults__.setter
    def __kwdefaults__(self, val: IronPython.Runtime.PythonDictionary):
        ...

    @property
    def __closure__(self) -> System.Object:
        ...
    @__closure__.setter
    def __closure__(self, val: System.Object):
        ...

    @property
    def __name__(self) -> str:
        ...
    @__name__.setter
    def __name__(self, val: str):
        ...

    @property
    def __qualname__(self) -> str:
        ...
    @__qualname__.setter
    def __qualname__(self, val: str):
        ...

    @property
    def __dict__(self) -> IronPython.Runtime.PythonDictionary:
        ...
    @__dict__.setter
    def __dict__(self, val: IronPython.Runtime.PythonDictionary):
        ...

    @property
    def __doc__(self) -> System.Object:
        ...
    @__doc__.setter
    def __doc__(self, val: System.Object):
        ...

    @property
    def __module__(self) -> System.Object:
        ...
    @__module__.setter
    def __module__(self, val: System.Object):
        ...

    @property
    def __code__(self) -> IronPython.Runtime.FunctionCode:
        ...
    @__code__.setter
    def __code__(self, val: IronPython.Runtime.FunctionCode):
        ...

    @property
    def Span(self) -> Microsoft.Scripting.SourceSpan:
        ...

    @property
    def ArgNames(self) -> System.Array[str]:
        ...

    @property
    def Context(self) -> IronPython.Runtime.CodeContext:
        ...

    @property
    def FunctionCompatibility(self) -> int:
        ...
    @FunctionCompatibility.setter
    def FunctionCompatibility(self, val: int):
        ...

    @property
    def IsGeneratorWithExceptionHandling(self) -> bool:
        ...

    @property
    def FunctionID(self) -> int:
        ...

    @property
    def ExpandListPosition(self) -> int:
        ...

    @property
    def ExpandDictPosition(self) -> int:
        ...

    @property
    def NormalArgumentCount(self) -> int:
        ...

    @property
    def KeywordOnlyArgumentCount(self) -> int:
        ...

    @property
    def ExtraArguments(self) -> int:
        ...

    @property
    def Flags(self) -> int:
        ...

    @property
    def Defaults(self) -> System.Array[System.Object]:
        ...

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
    @typing.overload
    def __init__(self, context: IronPython.Runtime.CodeContext, code: IronPython.Runtime.FunctionCode, globals: IronPython.Runtime.PythonDictionary, name: str = ..., defaults: IronPython.Runtime.PythonTuple = ..., closure: IronPython.Runtime.PythonTuple = ..., ):
        ...

    @typing.overload
    def __init__(self, context: IronPython.Runtime.CodeContext, funcInfo: IronPython.Runtime.FunctionCode, modName: System.Object, defaults: System.Array[System.Object], kwdefaults: IronPython.Runtime.PythonDictionary, annotations: IronPython.Runtime.PythonDictionary, closure: Microsoft.Scripting.MutableTuple, ):
        ...

    @typing.overload
    def __call__(self, context: IronPython.Runtime.CodeContext, args: System.Array[System.Object], ) -> System.Object:
        ...

    @typing.overload
    def __call__(self, context: IronPython.Runtime.CodeContext, dict: System.Collections.Generic.IDictionary[System.Object, System.Object], args: System.Array[System.Object], ) -> System.Object:
        ...

    def GetSignatureString(self, ) -> str:
        ...

    def CalculatedCachedCompat(self, ) -> int:
        ...

    def BadArgumentError(self, count: int, ) -> System.Exception:
        ...

    def BadKeywordArgumentError(self, count: int, ) -> System.Exception:
        ...

    def GetMemberNames(self, ) -> System.Collections.Generic.IList[str]:
        ...

    def GetMemberNames(self, context: IronPython.Runtime.CodeContext, ) -> System.Collections.Generic.IList[System.Object]:
        ...

    def GetWeakRef(self, ) -> IronPython.Runtime.WeakRefTracker:
        ...

    def SetWeakRef(self, value: IronPython.Runtime.WeakRefTracker, ) -> bool:
        ...

    def SetFinalizer(self, value: IronPython.Runtime.WeakRefTracker, ) -> None:
        ...

    def EnsureDict(self, ) -> IronPython.Runtime.PythonDictionary:
        ...

    @staticmethod
    def AddRecursionDepth(change: int, ) -> int:
        ...

    def EnsureID(self, ) -> None:
        ...

    def TryGetValue(self, context: IronPython.Runtime.CodeContext, instance: System.Object, owner: IronPython.Runtime.Types.PythonType, value: ref[System.Object], ) -> bool:
        ...

    def __repr__(self, context: IronPython.Runtime.CodeContext, ) -> str:
        ...

    def GetMetaObject(self, parameter: System.Linq.Expressions.Expression, ) -> System.Dynamic.DynamicMetaObject:
        ...

    def MakeInvokeBinding(self, site: System.Runtime.CompilerServices.CallSite[T], binder: IronPython.Runtime.Binding.PythonInvokeBinder, state: IronPython.Runtime.CodeContext, args: System.Array[System.Object], ) -> IronPython.Runtime.Binding.FastBindResult[T]:
        ...

    def CanOptimizeCall(self, binder: IronPython.Runtime.Binding.PythonInvokeBinder, args: System.Array[System.Object], ) -> bool:
        ...

    @staticmethod
    def GetFunctionCaller(callerType: System.Type, funcCompat: int, ) -> IronPython.Runtime.FunctionCaller:
        ...

class HashDelegate(System.ICloneable, System.Runtime.Serialization.ISerializable, System.MulticastDelegate):
    @typing.overload
    def __init__(self, **kwargs):
        self._target: System.Object
        self._methodBase: System.Object
        self._methodPtr: System.IntPtr
        self._methodPtrAux: System.IntPtr
        ...

    # static fields

    # properties
    @property
    def Target(self) -> System.Object:
        ...

    @property
    def Method(self) -> System.Reflection.MethodInfo:
        ...

    # methods
    def __init__(self, object: System.Object, method: System.IntPtr, ):
        ...

    def Invoke(self, o: System.Object, dlg: ref[IronPython.Runtime.HashDelegate], ) -> int:
        ...

    def BeginInvoke(self, o: System.Object, dlg: ref[IronPython.Runtime.HashDelegate], callback: System.AsyncCallback, object: System.Object, ) -> System.IAsyncResult:
        ...

    def EndInvoke(self, dlg: ref[IronPython.Runtime.HashDelegate], result: System.IAsyncResult, ) -> int:
        ...

class ProfilerTreatsAsExternalAttribute(System.Attribute):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def TypeId(self) -> System.Object:
        ...

    # methods
    def __init__(self, ):
        ...

class BufferFlags(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    Simple: int = ...
    Writable: int = ...
    Format: int = ...
    ContigRO: int = ...
    ND: int = ...
    Contig: int = ...
    StridedRO: int = ...
    Strides: int = ...
    Strided: int = ...
    RecordsRO: int = ...
    Records: int = ...
    CContiguous: int = ...
    FContiguous: int = ...
    AnyContiguous: int = ...
    Indirect: int = ...
    FullRO: int = ...
    Full: int = ...

class Map(System.Collections.IEnumerator, System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def Current(self) -> System.Object:
        ...
    @Current.setter
    def Current(self, val: System.Object):
        ...

    # methods
    def __init__(self, context: IronPython.Runtime.CodeContext, func: System.Object, iterables: System.Array[System.Object], ):
        ...

    def MoveNext(self, ) -> bool:
        ...

    def Reset(self, ) -> None:
        ...

    def __reduce__(self, ) -> IronPython.Runtime.PythonTuple:
        ...

class PythonLongRangeIterator(System.Collections.IEnumerable, System.Collections.Generic.IEnumerator[System.Numerics.BigInteger], System.IDisposable, System.Collections.IEnumerator, System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def Current(self) -> System.Object:
        ...

    @property
    def Current(self) -> System.Numerics.BigInteger:
        ...

    # methods
    def __init__(self, range: IronPython.Runtime.PythonRange, ):
        ...

    def MoveNext(self, ) -> bool:
        ...

    def Reset(self, ) -> None:
        ...

    def __reduce__(self, context: IronPython.Runtime.CodeContext, ) -> IronPython.Runtime.PythonTuple:
        ...

    def __setstate__(self, position: System.Numerics.BigInteger, ) -> None:
        ...

    def Dispose(self, ) -> None:
        ...

    def GetEnumerator(self, ) -> System.Collections.IEnumerator:
        ...

    def __length_hint__(self, ) -> System.Numerics.BigInteger:
        ...

class MemoryView(IronPython.Runtime.ICodeFormattable, IronPython.Runtime.IWeakReferenceable, IronPython.Runtime.IBufferProtocol, IronPython.Runtime.IPythonBuffer, System.IDisposable, System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def obj(self) -> System.Object:
        ...

    @property
    def c_contiguous(self) -> bool:
        ...

    @property
    def f_contiguous(self) -> bool:
        ...

    @property
    def contiguous(self) -> bool:
        ...

    @property
    def format(self) -> str:
        ...

    @property
    def itemsize(self) -> int:
        ...

    @property
    def ndim(self) -> int:
        ...

    @property
    def nbytes(self) -> int:
        ...

    @property
    def readonly(self) -> bool:
        ...

    @property
    def shape(self) -> IronPython.Runtime.PythonTuple:
        ...

    @property
    def strides(self) -> IronPython.Runtime.PythonTuple:
        ...

    @property
    def suboffsets(self) -> IronPython.Runtime.PythonTuple:
        ...

    @property
    def Item(self) -> System.Object:
        ...
    @Item.setter
    def Item(self, val: System.Object):
        ...

    @property
    def Item(self) -> System.Object:
        ...
    @Item.setter
    def Item(self, val: System.Object):
        ...

    @property
    def Item(self) -> System.Object:
        ...
    @Item.setter
    def Item(self, val: System.Object):
        ...

    @property
    def Object(self) -> System.Object:
        ...

    @property
    def IsReadOnly(self) -> bool:
        ...

    @property
    def Offset(self) -> int:
        ...

    @property
    def ItemCount(self) -> int:
        ...

    @property
    def Format(self) -> str:
        ...

    @property
    def ItemSize(self) -> int:
        ...

    @property
    def NumOfDims(self) -> int:
        ...

    @property
    def Shape(self) -> System.Collections.Generic.IReadOnlyList[int]:
        ...

    @property
    def Strides(self) -> System.Collections.Generic.IReadOnlyList[int]:
        ...

    @property
    def SubOffsets(self) -> System.Collections.Generic.IReadOnlyList[int]:
        ...

    # methods
    @typing.overload
    def __init__(self, object: IronPython.Runtime.IBufferProtocol, ):
        ...

    @typing.overload
    def __init__(self, object: IronPython.Runtime.MemoryView, ):
        ...

    @typing.overload
    def __init__(self, object: IronPython.Runtime.IBufferProtocol, readOnly: bool, ):
        ...

    @typing.overload
    def __init__(self, mv: IronPython.Runtime.MemoryView, readOnly: bool, ):
        ...

    @typing.overload
    def __init__(self, mv: IronPython.Runtime.MemoryView, newStart: int, newStop: int, newStep: int, newLen: int, ):
        ...

    @typing.overload
    def __init__(self, mv: IronPython.Runtime.MemoryView, newFormat: str, newItemSize: int, newShape: System.Collections.Generic.IReadOnlyList[int], ):
        ...

    @typing.overload
    def __init__(self, object: IronPython.Runtime.MemoryView, flags: int, ):
        ...

    def Finalize(self, ) -> None:
        ...

    def CheckBuffer(self, ) -> None:
        ...

    @staticmethod
    def VerifyStructure(memlen: int, itemsize: int, ndim: int, shape: System.Collections.Generic.IReadOnlyList[int], strides: System.Collections.Generic.IReadOnlyList[int], offset: int, ) -> bool:
        ...

    @staticmethod
    def GetContiguousStrides(shape: System.Collections.Generic.IReadOnlyList[int], itemSize: int, ) -> System.Collections.Generic.IReadOnlyList[int]:
        ...

    def __len__(self, ) -> int:
        ...

    def release(self, context: IronPython.Runtime.CodeContext, ) -> None:
        ...

    def __enter__(self, ) -> System.Object:
        ...

    def __exit__(self, context: IronPython.Runtime.CodeContext, excinfo: System.Array[System.Object], ) -> None:
        ...

    def hex(self, ) -> str:
        ...

    def tobytes(self, ) -> IronPython.Runtime.Bytes:
        ...

    def tolist(self, ) -> System.Object:
        ...

    @typing.overload
    def cast(self, format: str, ) -> IronPython.Runtime.MemoryView:
        ...

    @typing.overload
    def cast(self, format: str, shape: System.Object, ) -> IronPython.Runtime.MemoryView:
        ...

    @staticmethod
    def IsSupportedTypecode(code: str, ) -> bool:
        ...

    @staticmethod
    def UnpackBytes(typecode: str, o: System.Object, dest: System.Span[int], ) -> None:
        ...

    @staticmethod
    def PackBytes(typecode: str, bytes: System.ReadOnlySpan[int], ) -> System.Object:
        ...

    def GetItem(self, offset: int, ) -> System.Object:
        ...

    def SetItem(self, offset: int, value: System.Object, ) -> None:
        ...

    @typing.overload
    def __delitem__(self, index: int, ) -> None:
        ...

    @typing.overload
    def __delitem__(self, slice: IronPython.Runtime.Slice, ) -> None:
        ...

    def SliceAssign(self, index: int, value: System.Object, ) -> None:
        ...

    @staticmethod
    def FixSlice(slice: IronPython.Runtime.Slice, len: int, start: ref[int], stop: ref[int], step: ref[int], count: ref[int], ) -> None:
        ...

    @typing.overload
    def GetItemOffset(self, tuple: IronPython.Runtime.PythonTuple, ) -> int:
        ...

    @typing.overload
    def GetItemOffset(self, index: int, ) -> int:
        ...

    def __hash__(self, context: IronPython.Runtime.CodeContext, ) -> int:
        ...

    @typing.overload
    def __eq__(self, context: IronPython.Runtime.CodeContext, value: IronPython.Runtime.MemoryView, ) -> bool:
        ...

    @typing.overload
    def __eq__(self, context: IronPython.Runtime.CodeContext, value: IronPython.Runtime.IBufferProtocol, ) -> bool:
        ...

    @typing.overload
    def __eq__(self, context: IronPython.Runtime.CodeContext, value: System.Object, ) -> IronPython.Runtime.Types.NotImplementedType:
        ...

    @typing.overload
    def __ne__(self, context: IronPython.Runtime.CodeContext, value: IronPython.Runtime.MemoryView, ) -> bool:
        ...

    @typing.overload
    def __ne__(self, context: IronPython.Runtime.CodeContext, value: IronPython.Runtime.IBufferProtocol, ) -> bool:
        ...

    @typing.overload
    def __ne__(self, context: IronPython.Runtime.CodeContext, value: System.Object, ) -> IronPython.Runtime.Types.NotImplementedType:
        ...

    def __lt__(self, context: IronPython.Runtime.CodeContext, value: System.Object, ) -> IronPython.Runtime.Types.NotImplementedType:
        ...

    def __le__(self, context: IronPython.Runtime.CodeContext, value: System.Object, ) -> IronPython.Runtime.Types.NotImplementedType:
        ...

    def __gt__(self, context: IronPython.Runtime.CodeContext, value: System.Object, ) -> IronPython.Runtime.Types.NotImplementedType:
        ...

    def __ge__(self, context: IronPython.Runtime.CodeContext, value: System.Object, ) -> IronPython.Runtime.Types.NotImplementedType:
        ...

    def __repr__(self, context: IronPython.Runtime.CodeContext, ) -> str:
        ...

    def GetWeakRef(self, ) -> IronPython.Runtime.WeakRefTracker:
        ...

    def SetWeakRef(self, value: IronPython.Runtime.WeakRefTracker, ) -> bool:
        ...

    def SetFinalizer(self, value: IronPython.Runtime.WeakRefTracker, ) -> None:
        ...

    def GetBuffer(self, flags: int, ) -> IronPython.Runtime.IPythonBuffer:
        ...

    def Dispose(self, ) -> None:
        ...

    def AsReadOnlySpan(self, ) -> System.ReadOnlySpan[int]:
        ...

    def AsSpan(self, ) -> System.Span[int]:
        ...

    def Pin(self, ) -> System.Buffers.MemoryHandle:
        ...

class SiteLocalStorage(IronPython.Runtime.SiteLocalStorage, typing.Generic[T]):
    @typing.overload
    def __init__(self, **kwargs):
        self.Data: T
        ...

    # static fields

    # properties
    # methods
    def __init__(self, ):
        ...

class DictionaryValueView(System.Collections.Generic.ICollection[System.Object], System.Collections.Generic.IEnumerable[System.Object], System.Collections.IEnumerable, System.Collections.ICollection, IronPython.Runtime.ICodeFormattable, System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def Count(self) -> int:
        ...

    @property
    def IsReadOnly(self) -> bool:
        ...

    @property
    def Count(self) -> int:
        ...

    @property
    def SyncRoot(self) -> System.Object:
        ...

    @property
    def IsSynchronized(self) -> bool:
        ...

    # methods
    def __init__(self, dict: IronPython.Runtime.PythonDictionary, ):
        ...

    def GetEnumerator(self, ) -> System.Collections.Generic.IEnumerator[System.Object]:
        ...

    def GetEnumerator(self, ) -> System.Collections.IEnumerator:
        ...

    def Add(self, item: System.Object, ) -> None:
        ...

    def Clear(self, ) -> None:
        ...

    def Contains(self, item: System.Object, ) -> bool:
        ...

    def CopyTo(self, array: System.Array[System.Object], arrayIndex: int, ) -> None:
        ...

    def Remove(self, item: System.Object, ) -> bool:
        ...

    def CopyTo(self, array: System.Array, index: int, ) -> None:
        ...

    def __repr__(self, context: IronPython.Runtime.CodeContext, ) -> str:
        ...

    def __reduce__(self, context: IronPython.Runtime.CodeContext, ) -> System.Object:
        ...

class FunctionCaller(IronPython.Runtime.FunctionCaller, typing.Generic[T0, T1, T2, T3, T4, T5, T6, T7, T8]):
    @typing.overload
    def __init__(self, **kwargs):
        self._compat: int
        ...

    # static fields

    # properties
    # methods
    def __init__(self, compat: int, ):
        ...

    def Call9(self, site: System.Runtime.CompilerServices.CallSite, context: IronPython.Runtime.CodeContext, func: System.Object, arg0: T0, arg1: T1, arg2: T2, arg3: T3, arg4: T4, arg5: T5, arg6: T6, arg7: T7, arg8: T8, ) -> System.Object:
        ...

    def Default1Call9(self, site: System.Runtime.CompilerServices.CallSite, context: IronPython.Runtime.CodeContext, func: System.Object, arg0: T0, arg1: T1, arg2: T2, arg3: T3, arg4: T4, arg5: T5, arg6: T6, arg7: T7, arg8: T8, ) -> System.Object:
        ...

    def Default2Call9(self, site: System.Runtime.CompilerServices.CallSite, context: IronPython.Runtime.CodeContext, func: System.Object, arg0: T0, arg1: T1, arg2: T2, arg3: T3, arg4: T4, arg5: T5, arg6: T6, arg7: T7, arg8: T8, ) -> System.Object:
        ...

    def Default3Call9(self, site: System.Runtime.CompilerServices.CallSite, context: IronPython.Runtime.CodeContext, func: System.Object, arg0: T0, arg1: T1, arg2: T2, arg3: T3, arg4: T4, arg5: T5, arg6: T6, arg7: T7, arg8: T8, ) -> System.Object:
        ...

    def Default4Call9(self, site: System.Runtime.CompilerServices.CallSite, context: IronPython.Runtime.CodeContext, func: System.Object, arg0: T0, arg1: T1, arg2: T2, arg3: T3, arg4: T4, arg5: T5, arg6: T6, arg7: T7, arg8: T8, ) -> System.Object:
        ...

class FunctionCaller(IronPython.Runtime.FunctionCaller, typing.Generic[T0, T1, T2, T3, T4]):
    @typing.overload
    def __init__(self, **kwargs):
        self._compat: int
        ...

    # static fields

    # properties
    # methods
    def __init__(self, compat: int, ):
        ...

    def Call5(self, site: System.Runtime.CompilerServices.CallSite, context: IronPython.Runtime.CodeContext, func: System.Object, arg0: T0, arg1: T1, arg2: T2, arg3: T3, arg4: T4, ) -> System.Object:
        ...

    def Default1Call5(self, site: System.Runtime.CompilerServices.CallSite, context: IronPython.Runtime.CodeContext, func: System.Object, arg0: T0, arg1: T1, arg2: T2, arg3: T3, arg4: T4, ) -> System.Object:
        ...

    def Default2Call5(self, site: System.Runtime.CompilerServices.CallSite, context: IronPython.Runtime.CodeContext, func: System.Object, arg0: T0, arg1: T1, arg2: T2, arg3: T3, arg4: T4, ) -> System.Object:
        ...

    def Default3Call5(self, site: System.Runtime.CompilerServices.CallSite, context: IronPython.Runtime.CodeContext, func: System.Object, arg0: T0, arg1: T1, arg2: T2, arg3: T3, arg4: T4, ) -> System.Object:
        ...

    def Default4Call5(self, site: System.Runtime.CompilerServices.CallSite, context: IronPython.Runtime.CodeContext, func: System.Object, arg0: T0, arg1: T1, arg2: T2, arg3: T3, arg4: T4, ) -> System.Object:
        ...

    def Default5Call5(self, site: System.Runtime.CompilerServices.CallSite, context: IronPython.Runtime.CodeContext, func: System.Object, arg0: T0, arg1: T1, arg2: T2, arg3: T3, arg4: T4, ) -> System.Object:
        ...

    def Default6Call5(self, site: System.Runtime.CompilerServices.CallSite, context: IronPython.Runtime.CodeContext, func: System.Object, arg0: T0, arg1: T1, arg2: T2, arg3: T3, arg4: T4, ) -> System.Object:
        ...

    def Default7Call5(self, site: System.Runtime.CompilerServices.CallSite, context: IronPython.Runtime.CodeContext, func: System.Object, arg0: T0, arg1: T1, arg2: T2, arg3: T3, arg4: T4, ) -> System.Object:
        ...

    def Default8Call5(self, site: System.Runtime.CompilerServices.CallSite, context: IronPython.Runtime.CodeContext, func: System.Object, arg0: T0, arg1: T1, arg2: T2, arg3: T3, arg4: T4, ) -> System.Object:
        ...

class UnboundLocalException(System.Runtime.Serialization.ISerializable, IronPython.Runtime.UnboundNameException):
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
    def __init__(self, msg: str, ):
        ...

    @typing.overload
    def __init__(self, message: str, innerException: System.Exception, ):
        ...

    @typing.overload
    def __init__(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext, ):
        ...

class ClosureCell(IronPython.Runtime.ICodeFormattable, System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        self.Value: System.Object
        ...

    # static fields
    __hash__: System.Object = ...

    # properties
    @property
    def cell_contents(self) -> System.Object:
        ...

    # methods
    def __init__(self, value: System.Object, ):
        ...

    def __repr__(self, context: IronPython.Runtime.CodeContext, ) -> str:
        ...

    def GetContentsRepr(self, ) -> str:
        ...

    def __eq__(self, context: IronPython.Runtime.CodeContext, other: IronPython.Runtime.ClosureCell, ) -> System.Object:
        ...

    def __ne__(self, context: IronPython.Runtime.CodeContext, other: IronPython.Runtime.ClosureCell, ) -> System.Object:
        ...

    def __lt__(self, context: IronPython.Runtime.CodeContext, other: IronPython.Runtime.ClosureCell, ) -> System.Object:
        ...

    def __le__(self, context: IronPython.Runtime.CodeContext, other: IronPython.Runtime.ClosureCell, ) -> System.Object:
        ...

    def __ge__(self, context: IronPython.Runtime.CodeContext, other: IronPython.Runtime.ClosureCell, ) -> System.Object:
        ...

    def __gt__(self, context: IronPython.Runtime.CodeContext, other: IronPython.Runtime.ClosureCell, ) -> System.Object:
        ...

class ModuleContext(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def Globals(self) -> IronPython.Runtime.PythonDictionary:
        ...

    @property
    def Context(self) -> IronPython.Runtime.PythonContext:
        ...

    @property
    def GlobalScope(self) -> Microsoft.Scripting.Runtime.Scope:
        ...

    @property
    def GlobalContext(self) -> IronPython.Runtime.CodeContext:
        ...

    @property
    def Module(self) -> IronPython.Runtime.PythonModule:
        ...

    @property
    def Features(self) -> int:
        ...
    @Features.setter
    def Features(self, val: int):
        ...

    @property
    def ShowCls(self) -> bool:
        ...
    @ShowCls.setter
    def ShowCls(self, val: bool):
        ...

    @property
    def ExtensionMethods(self) -> IronPython.Runtime.ExtensionMethodSet:
        ...
    @ExtensionMethods.setter
    def ExtensionMethods(self, val: IronPython.Runtime.ExtensionMethodSet):
        ...

    # methods
    @typing.overload
    def __init__(self, globals: IronPython.Runtime.PythonDictionary, creatingContext: IronPython.Runtime.PythonContext, ):
        ...

    @typing.overload
    def __init__(self, module: IronPython.Runtime.PythonModule, creatingContext: IronPython.Runtime.PythonContext, ):
        ...

    def InitializeBuiltins(self, moduleBuiltins: bool, ) -> None:
        ...

class DictionaryItemView(System.Collections.Generic.ICollection[System.Object], System.Collections.Generic.IEnumerable[System.Object], System.Collections.IEnumerable, IronPython.Runtime.ICodeFormattable, System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        self._dict: IronPython.Runtime.PythonDictionary
        ...

    # static fields

    # properties
    @property
    def Count(self) -> int:
        ...

    @property
    def IsReadOnly(self) -> bool:
        ...

    # methods
    def __init__(self, dict: IronPython.Runtime.PythonDictionary, ):
        ...

    def GetEnumerator(self, ) -> System.Collections.Generic.IEnumerator[System.Object]:
        ...

    def GetEnumerator(self, ) -> System.Collections.IEnumerator:
        ...

    def Add(self, item: System.Object, ) -> None:
        ...

    def Clear(self, ) -> None:
        ...

    def Contains(self, item: System.Object, ) -> bool:
        ...

    def CopyTo(self, array: System.Array[System.Object], arrayIndex: int, ) -> None:
        ...

    def Remove(self, item: System.Object, ) -> bool:
        ...

    def Equals(self, obj: System.Object, ) -> bool:
        ...

    def __repr__(self, context: IronPython.Runtime.CodeContext, ) -> str:
        ...

    def __reduce__(self, context: IronPython.Runtime.CodeContext, ) -> System.Object:
        ...

    def isdisjoint(self, other: System.Collections.IEnumerable, ) -> bool:
        ...

    def GetHashCode(self, ) -> int:
        ...

class MemoryBufferProtocolWrapper(IronPython.Runtime.IBufferProtocol, System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    @typing.overload
    def __init__(self, memory: System.ReadOnlyMemory[int], ):
        ...

    @typing.overload
    def __init__(self, memory: System.Memory[int], ):
        ...

    def GetBuffer(self, flags: int, ) -> IronPython.Runtime.IPythonBuffer:
        ...

class PythonContext(Microsoft.Scripting.Runtime.LanguageContext):
    @typing.overload
    def __init__(self, **kwargs):
        self._allCodes: IronPython.Runtime.FunctionCode.CodeList
        self._codeCleanupLock: System.Object
        self._codeUpdateLock: System.Object
        self._codeCount: int
        self._nextCodeCleanup: int
        self._mainThreadFunctionStack: System.Collections.Generic.List[IronPython.Runtime.Operations.FunctionStack]
        self.InitialHasher: IronPython.Runtime.HashDelegate
        self.IntHasher: IronPython.Runtime.HashDelegate
        self.DoubleHasher: IronPython.Runtime.HashDelegate
        self.StringHasher: IronPython.Runtime.HashDelegate
        self.FallbackHasher: IronPython.Runtime.HashDelegate
        ...

    # static fields
    IronPythonDisplayName: str = ...
    _syntaxErrorNoCaret: System.Object = ...
    IronPythonNames: str = ...
    IronPythonFileExtensions: str = ...

    # properties
    @property
    def RecursionLimit(self) -> int:
        ...
    @RecursionLimit.setter
    def RecursionLimit(self, val: int):
        ...

    @property
    def EnableTracing(self) -> bool:
        ...

    @property
    def TopNamespace(self) -> Microsoft.Scripting.Actions.TopNamespaceTracker:
        ...

    @property
    def MainThread(self) -> System.Threading.Thread:
        ...
    @MainThread.setter
    def MainThread(self, val: System.Threading.Thread):
        ...

    @property
    def EqualityComparer(self) -> System.Collections.Generic.IEqualityComparer[System.Object]:
        ...

    @property
    def EqualityComparerNonGeneric(self) -> System.Collections.IEqualityComparer:
        ...

    @property
    def Options(self) -> Microsoft.Scripting.LanguageOptions:
        ...

    @property
    def PythonOptions(self) -> IronPython.Runtime.PythonOptions:
        ...

    @property
    def VendorGuid(self) -> System.Guid:
        ...

    @property
    def LanguageGuid(self) -> System.Guid:
        ...

    @property
    def SystemState(self) -> IronPython.Runtime.PythonModule:
        ...

    @property
    def ClrModule(self) -> IronPython.Runtime.PythonModule:
        ...

    @property
    def SystemStandardOut(self) -> System.Object:
        ...

    @property
    def SystemStandardIn(self) -> System.Object:
        ...

    @property
    def SystemStandardError(self) -> System.Object:
        ...

    @property
    def SystemStateModules(self) -> System.Collections.Generic.IDictionary[System.Object, System.Object]:
        ...

    @property
    def LanguageVersion(self) -> System.Version:
        ...

    @property
    def FloatFormat(self) -> int:
        ...
    @FloatFormat.setter
    def FloatFormat(self, val: int):
        ...

    @property
    def DoubleFormat(self) -> int:
        ...
    @DoubleFormat.setter
    def DoubleFormat(self, val: int):
        ...

    @property
    def DefaultEncoding(self) -> System.Text.Encoding:
        ...

    @property
    def BuiltinModules(self) -> System.Collections.Generic.Dictionary[str, System.Type]:
        ...

    @property
    def BuiltinModuleNames(self) -> System.Collections.Generic.Dictionary[System.Type, str]:
        ...

    @property
    def BuiltinModuleInstance(self) -> IronPython.Runtime.PythonModule:
        ...
    @BuiltinModuleInstance.setter
    def BuiltinModuleInstance(self, val: IronPython.Runtime.PythonModule):
        ...

    @property
    def BuiltinModuleDict(self) -> IronPython.Runtime.PythonDictionary:
        ...
    @BuiltinModuleDict.setter
    def BuiltinModuleDict(self, val: IronPython.Runtime.PythonDictionary):
        ...

    @property
    def InitialPrefix(self) -> str:
        ...
    @InitialPrefix.setter
    def InitialPrefix(self, val: str):
        ...

    @property
    def RawFileManager(self) -> IronPython.Runtime.PythonFileManager:
        ...

    @property
    def FileManager(self) -> IronPython.Runtime.PythonFileManager:
        ...

    @property
    def ErrorHandlers(self) -> System.Collections.Concurrent.ConcurrentDictionary[str, System.Object]:
        ...

    @property
    def SearchFunctions(self) -> System.Collections.Generic.List[System.Object]:
        ...

    @property
    def MetaClassCallSite(self) -> System.Runtime.CompilerServices.CallSite[System.Func[System.Runtime.CompilerServices.CallSite, IronPython.Runtime.CodeContext, System.Object, str, IronPython.Runtime.PythonTuple, System.Object, IronPython.Runtime.PythonDictionary, System.Object]]:
        ...

    @property
    def WriteCallSite(self) -> System.Runtime.CompilerServices.CallSite[System.Func[System.Runtime.CompilerServices.CallSite, IronPython.Runtime.CodeContext, System.Object, str, System.Object]]:
        ...

    @property
    def GetIndexSite(self) -> System.Runtime.CompilerServices.CallSite[System.Func[System.Runtime.CompilerServices.CallSite, System.Object, System.Object, System.Object]]:
        ...

    @property
    def EqualSite(self) -> System.Runtime.CompilerServices.CallSite[System.Func[System.Runtime.CompilerServices.CallSite, System.Object, System.Object, System.Object]]:
        ...

    @property
    def FinalizerSite(self) -> System.Runtime.CompilerServices.CallSite[System.Func[System.Runtime.CompilerServices.CallSite, IronPython.Runtime.CodeContext, System.Object, System.Object]]:
        ...

    @property
    def FunctionCallSite(self) -> System.Runtime.CompilerServices.CallSite[System.Func[System.Runtime.CompilerServices.CallSite, IronPython.Runtime.CodeContext, IronPython.Runtime.PythonFunction, System.Object]]:
        ...

    @property
    def ImportSite(self) -> System.Runtime.CompilerServices.CallSite[System.Func[System.Runtime.CompilerServices.CallSite, IronPython.Runtime.CodeContext, System.Object, str, IronPython.Runtime.PythonDictionary, IronPython.Runtime.PythonDictionary, IronPython.Runtime.PythonTuple, int, System.Object]]:
        ...

    @property
    def SharedContext(self) -> IronPython.Runtime.CodeContext:
        ...

    @property
    def SharedOverloadResolverFactory(self) -> IronPython.Runtime.Binding.PythonOverloadResolverFactory:
        ...

    @property
    def SharedClsContext(self) -> IronPython.Runtime.CodeContext:
        ...

    @property
    def ReferencedAssemblies(self) -> IronPython.Runtime.ClrModule.ReferencesList:
        ...

    @property
    def CCulture(self) -> System.Globalization.CultureInfo:
        ...

    @property
    def CollateCulture(self) -> System.Globalization.CultureInfo:
        ...
    @CollateCulture.setter
    def CollateCulture(self, val: System.Globalization.CultureInfo):
        ...

    @property
    def CTypeCulture(self) -> System.Globalization.CultureInfo:
        ...
    @CTypeCulture.setter
    def CTypeCulture(self, val: System.Globalization.CultureInfo):
        ...

    @property
    def TimeCulture(self) -> System.Globalization.CultureInfo:
        ...
    @TimeCulture.setter
    def TimeCulture(self, val: System.Globalization.CultureInfo):
        ...

    @property
    def MonetaryCulture(self) -> System.Globalization.CultureInfo:
        ...
    @MonetaryCulture.setter
    def MonetaryCulture(self, val: System.Globalization.CultureInfo):
        ...

    @property
    def NumericCulture(self) -> System.Globalization.CultureInfo:
        ...
    @NumericCulture.setter
    def NumericCulture(self, val: System.Globalization.CultureInfo):
        ...

    @property
    def PropertyGetSite(self) -> System.Runtime.CompilerServices.CallSite[System.Func[System.Runtime.CompilerServices.CallSite, IronPython.Runtime.CodeContext, System.Object, System.Object, System.Object]]:
        ...

    @property
    def PropertyDeleteSite(self) -> System.Runtime.CompilerServices.CallSite[System.Func[System.Runtime.CompilerServices.CallSite, IronPython.Runtime.CodeContext, System.Object, System.Object, System.Object]]:
        ...

    @property
    def PropertySetSite(self) -> System.Runtime.CompilerServices.CallSite[System.Func[System.Runtime.CompilerServices.CallSite, IronPython.Runtime.CodeContext, System.Object, System.Object, System.Object, System.Object]]:
        ...

    @property
    def Binder(self) -> IronPython.Runtime.Binding.PythonBinder:
        ...

    @property
    def GetItemCallSite(self) -> System.Runtime.CompilerServices.CallSite[System.Func[System.Runtime.CompilerServices.CallSite, IronPython.Runtime.CodeContext, System.Object, int, System.Object]]:
        ...

    @property
    def DelegateCreator(self) -> Microsoft.Scripting.Runtime.DynamicDelegateCreator:
        ...

    @property
    def InvokeNone(self) -> IronPython.Runtime.Binding.PythonInvokeBinder:
        ...

    @property
    def InvokeOne(self) -> IronPython.Runtime.Binding.PythonInvokeBinder:
        ...

    @property
    def GetSlice(self) -> IronPython.Runtime.Binding.PythonGetSliceBinder:
        ...

    @property
    def SetSliceBinder(self) -> IronPython.Runtime.Binding.PythonSetSliceBinder:
        ...

    @property
    def DeleteSlice(self) -> IronPython.Runtime.Binding.PythonDeleteSliceBinder:
        ...

    @property
    def DebugContext(self) -> Microsoft.Scripting.Debugging.CompilerServices.DebugContext:
        ...

    @property
    def TracePipeline(self) -> Microsoft.Scripting.Debugging.ITracePipeline:
        ...

    @property
    def CallSite0(self) -> System.Runtime.CompilerServices.CallSite[System.Func[System.Runtime.CompilerServices.CallSite, IronPython.Runtime.CodeContext, System.Object, System.Object]]:
        ...

    @property
    def CallSite1(self) -> System.Runtime.CompilerServices.CallSite[System.Func[System.Runtime.CompilerServices.CallSite, IronPython.Runtime.CodeContext, System.Object, System.Object, System.Object]]:
        ...

    @property
    def CallSite2(self) -> System.Runtime.CompilerServices.CallSite[System.Func[System.Runtime.CompilerServices.CallSite, IronPython.Runtime.CodeContext, System.Object, System.Object, System.Object, System.Object]]:
        ...

    @property
    def CallSite3(self) -> System.Runtime.CompilerServices.CallSite[System.Func[System.Runtime.CompilerServices.CallSite, IronPython.Runtime.CodeContext, System.Object, System.Object, System.Object, System.Object, System.Object]]:
        ...

    @property
    def CallSite4(self) -> System.Runtime.CompilerServices.CallSite[System.Func[System.Runtime.CompilerServices.CallSite, IronPython.Runtime.CodeContext, System.Object, System.Object, System.Object, System.Object, System.Object, System.Object]]:
        ...

    @property
    def CallSite5(self) -> System.Runtime.CompilerServices.CallSite[System.Func[System.Runtime.CompilerServices.CallSite, IronPython.Runtime.CodeContext, System.Object, System.Object, System.Object, System.Object, System.Object, System.Object, System.Object]]:
        ...

    @property
    def CallSite6(self) -> System.Runtime.CompilerServices.CallSite[System.Func[System.Runtime.CompilerServices.CallSite, IronPython.Runtime.CodeContext, System.Object, System.Object, System.Object, System.Object, System.Object, System.Object, System.Object, System.Object]]:
        ...

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
    def Operations(self) -> Microsoft.Scripting.Runtime.DynamicOperations:
        ...

    # methods
    def __init__(self, manager: Microsoft.Scripting.Runtime.ScriptDomainManager, options: System.Collections.Generic.IDictionary[str, System.Object], ):
        ...

    def SetMember(self, name: str, ) -> IronPython.Runtime.Binding.PythonSetMemberBinder:
        ...

    def DeleteMember(self, name: str, ) -> IronPython.Runtime.Binding.PythonDeleteMemberBinder:
        ...

    def Invoke(self, signature: Microsoft.Scripting.Actions.CallSignature, ) -> IronPython.Runtime.Binding.PythonInvokeBinder:
        ...

    @typing.overload
    def Operation(self, operation: int, ) -> IronPython.Runtime.Binding.PythonOperationBinder:
        ...

    @typing.overload
    def Operation(self, operation: int, self: System.Object, other: System.Object, ) -> System.Object:
        ...

    def UnaryOperation(self, operation: int, ) -> IronPython.Runtime.Binding.PythonUnaryOperationBinder:
        ...

    def BinaryOperation(self, operation: int, ) -> IronPython.Runtime.Binding.PythonBinaryOperationBinder:
        ...

    def BinaryOperationRetType(self, opBinder: IronPython.Runtime.Binding.PythonBinaryOperationBinder, convBinder: IronPython.Runtime.Binding.PythonConversionBinder, ) -> IronPython.Runtime.Binding.BinaryRetTypeBinder:
        ...

    def OperationRetType(self, opBinder: IronPython.Runtime.Binding.PythonOperationBinder, convBinder: IronPython.Runtime.Binding.PythonConversionBinder, ) -> IronPython.Runtime.Binding.BinaryRetTypeBinder:
        ...

    def GetIndex(self, argCount: int, ) -> IronPython.Runtime.Binding.PythonGetIndexBinder:
        ...

    @typing.overload
    def SetIndex(self, argCount: int, ) -> IronPython.Runtime.Binding.PythonSetIndexBinder:
        ...

    @typing.overload
    def SetIndex(self, a: System.Object, b: System.Object, c: System.Object, ) -> None:
        ...

    def DeleteIndex(self, argCount: int, ) -> IronPython.Runtime.Binding.PythonDeleteIndexBinder:
        ...

    @staticmethod
    def GetPythonContext(action: System.Dynamic.DynamicMetaObjectBinder, ) -> IronPython.Runtime.PythonContext:
        ...

    @staticmethod
    def GetCodeContext(action: System.Dynamic.DynamicMetaObjectBinder, ) -> System.Linq.Expressions.Expression:
        ...

    @staticmethod
    def GetCodeContextMO(action: System.Dynamic.DynamicMetaObjectBinder, ) -> System.Dynamic.DynamicMetaObject:
        ...

    @staticmethod
    def GetCodeContextMOCls(action: System.Dynamic.DynamicMetaObjectBinder, ) -> System.Dynamic.DynamicMetaObject:
        ...

    @typing.overload
    def ScopeGetVariable(self, scope: Microsoft.Scripting.Runtime.Scope, name: str, ) -> T:
        ...

    @typing.overload
    def ScopeGetVariable(self, scope: Microsoft.Scripting.Runtime.Scope, name: str, ) -> System.Object:
        ...

    def ScopeSetVariable(self, scope: Microsoft.Scripting.Runtime.Scope, name: str, value: System.Object, ) -> None:
        ...

    def ScopeTryGetVariable(self, scope: Microsoft.Scripting.Runtime.Scope, name: str, value: ref[System.Object], ) -> bool:
        ...

    def EnsureDebugContext(self, ) -> None:
        ...

    def SetTrace(self, o: System.Object, ) -> None:
        ...

    def CallTracing(self, func: System.Object, args: IronPython.Runtime.PythonTuple, ) -> System.Object:
        ...

    def GetTrace(self, ) -> System.Object:
        ...

    def UniqifyExtensions(self, newSet: IronPython.Runtime.ExtensionMethodSet, ) -> IronPython.Runtime.ExtensionMethodSet:
        ...

    def EnsureCall0Site(self, ) -> None:
        ...

    def EnsureCall1Site(self, ) -> None:
        ...

    def EnsureCall2Site(self, ) -> None:
        ...

    def EnsureCall3Site(self, ) -> None:
        ...

    def EnsureCall4Site(self, ) -> None:
        ...

    def EnsureCall5Site(self, ) -> None:
        ...

    def EnsureCall6Site(self, ) -> None:
        ...

    def MakeExplicitTrySite(self, ) -> System.Runtime.CompilerServices.CallSite[System.Func[System.Runtime.CompilerServices.CallSite, System.Object, T]]:
        ...

    def MakeExplicitStructTrySite(self, ) -> System.Runtime.CompilerServices.CallSite[System.Func[System.Runtime.CompilerServices.CallSite, System.Object, System.Object]]:
        ...

    def MakeTrySite(self, kind: int, ) -> System.Runtime.CompilerServices.CallSite[System.Func[System.Runtime.CompilerServices.CallSite, System.Object, TRet]]:
        ...

    def ImplicitConvertTo(self, value: System.Object, ) -> System.Object:
        ...

    def MakeExplicitConvertSite(self, ) -> System.Runtime.CompilerServices.CallSite[System.Func[System.Runtime.CompilerServices.CallSite, System.Object, T]]:
        ...

    def MakeImplicitConvertSite(self, ) -> System.Runtime.CompilerServices.CallSite[System.Func[System.Runtime.CompilerServices.CallSite, System.Object, System.Object]]:
        ...

    def MakeConvertSite(self, kind: int, ) -> System.Runtime.CompilerServices.CallSite[System.Func[System.Runtime.CompilerServices.CallSite, System.Object, T]]:
        ...

    def GreaterThan(self, self: System.Object, other: System.Object, ) -> bool:
        ...

    def LessThan(self, self: System.Object, other: System.Object, ) -> bool:
        ...

    def GreaterThanOrEqual(self, self: System.Object, other: System.Object, ) -> bool:
        ...

    def LessThanOrEqual(self, self: System.Object, other: System.Object, ) -> bool:
        ...

    def Contains(self, self: System.Object, other: System.Object, ) -> bool:
        ...

    @staticmethod
    def Equal(self: System.Object, other: System.Object, ) -> bool:
        ...

    @staticmethod
    def NotEqual(self: System.Object, other: System.Object, ) -> bool:
        ...

    @typing.overload
    def Comparison(self, self: System.Object, other: System.Object, operation: int, comparisonSite: ref[System.Runtime.CompilerServices.CallSite[System.Func[System.Runtime.CompilerServices.CallSite, System.Object, System.Object, bool]]], ) -> bool:
        ...

    @typing.overload
    def Comparison(self, self: System.Object, other: System.Object, operation: int, comparisonSite: ref[System.Runtime.CompilerServices.CallSite[System.Func[System.Runtime.CompilerServices.CallSite, System.Object, System.Object, bool]]], ) -> bool:
        ...

    @typing.overload
    def CreateComparisonSite(self, op: int, ) -> System.Runtime.CompilerServices.CallSite[System.Func[System.Runtime.CompilerServices.CallSite, System.Object, System.Object, bool]]:
        ...

    @typing.overload
    def CreateComparisonSite(self, op: int, ) -> System.Runtime.CompilerServices.CallSite[System.Func[System.Runtime.CompilerServices.CallSite, System.Object, System.Object, bool]]:
        ...

    @typing.overload
    def CallSplat(self, func: System.Object, args: System.Array[System.Object], ) -> System.Object:
        ...

    @typing.overload
    def CallSplat(self, context: IronPython.Runtime.CodeContext, func: System.Object, args: System.Array[System.Object], ) -> System.Object:
        ...

    def CallWithContext(self, context: IronPython.Runtime.CodeContext, func: System.Object, args: System.Array[System.Object], ) -> System.Object:
        ...

    @typing.overload
    def Call(self, context: IronPython.Runtime.CodeContext, func: System.Object, ) -> System.Object:
        ...

    @typing.overload
    def Call(self, context: IronPython.Runtime.CodeContext, func: System.Object, arg0: System.Object, ) -> System.Object:
        ...

    @typing.overload
    def Call(self, context: IronPython.Runtime.CodeContext, func: System.Object, arg0: System.Object, arg1: System.Object, ) -> System.Object:
        ...

    def EnsureCall0SiteLightEh(self, ) -> None:
        ...

    def CallLightEh(self, context: IronPython.Runtime.CodeContext, func: System.Object, ) -> System.Object:
        ...

    def EnsureCallSplatSite(self, ) -> None:
        ...

    def MakeSplatSite(self, ) -> System.Runtime.CompilerServices.CallSite[System.Func[System.Runtime.CompilerServices.CallSite, IronPython.Runtime.CodeContext, System.Object, System.Array[System.Object], System.Object]]:
        ...

    @typing.overload
    def CallWithKeywords(self, func: System.Object, args: System.Array[System.Object], dict: System.Collections.Generic.IDictionary[System.Object, System.Object], ) -> System.Object:
        ...

    @typing.overload
    def CallWithKeywords(self, func: System.Object, args: System.Object, dict: System.Object, ) -> System.Object:
        ...

    def CallWithKeywordsAndContext(self, context: IronPython.Runtime.CodeContext, func: System.Object, args: System.Array[System.Object], dict: System.Collections.Generic.IDictionary[System.Object, System.Object], ) -> System.Object:
        ...

    def MakeKeywordSplatSite(self, ) -> System.Runtime.CompilerServices.CallSite[System.Func[System.Runtime.CompilerServices.CallSite, IronPython.Runtime.CodeContext, System.Object, System.Array[System.Object], System.Collections.Generic.IDictionary[System.Object, System.Object], System.Object]]:
        ...

    def MakeKeywordSplatSiteLooselyTyped(self, ) -> System.Runtime.CompilerServices.CallSite[System.Func[System.Runtime.CompilerServices.CallSite, IronPython.Runtime.CodeContext, System.Object, System.Object, System.Object, System.Object]]:
        ...

    def IsCallable(self, obj: System.Object, ) -> bool:
        ...

    @staticmethod
    def Hash(o: System.Object, ) -> int:
        ...

    @staticmethod
    def IsHashable(o: System.Object, ) -> bool:
        ...

    def Add(self, x: System.Object, y: System.Object, ) -> System.Object:
        ...

    def EnsureAddSite(self, ) -> System.Runtime.CompilerServices.CallSite[System.Func[System.Runtime.CompilerServices.CallSite, System.Object, System.Object, System.Object]]:
        ...

    def DivMod(self, x: System.Object, y: System.Object, ) -> System.Object:
        ...

    def GetCompiledLoader(self, ) -> IronPython.Runtime.CompiledLoader:
        ...

    @staticmethod
    def MakeCCulture() -> System.Globalization.CultureInfo:
        ...

    def GetSetCommandDispatcher(self, newDispatcher: System.Action[System.Action], ) -> System.Action[System.Action]:
        ...

    def GetCommandDispatcher(self, ) -> System.Action[System.Action]:
        ...

    def DispatchCommand(self, command: System.Action, ) -> None:
        ...

    def GetComparer(self, type: System.Type, ) -> System.Collections.IComparer:
        ...

    def GetLtComparer(self, type: System.Type, ) -> System.Collections.IComparer:
        ...

    def GetEqualSite(self, type: System.Type, ) -> System.Runtime.CompilerServices.CallSite[System.Func[System.Runtime.CompilerServices.CallSite, System.Object, System.Object, bool]]:
        ...

    def MakeEqualSite(self, ) -> System.Runtime.CompilerServices.CallSite[System.Func[System.Runtime.CompilerServices.CallSite, System.Object, System.Object, bool]]:
        ...

    @staticmethod
    def GetHashSite(type: IronPython.Runtime.Types.PythonType, ) -> System.Runtime.CompilerServices.CallSite[System.Func[System.Runtime.CompilerServices.CallSite, System.Object, int]]:
        ...

    def MakeHashSite(self, ) -> System.Runtime.CompilerServices.CallSite[System.Func[System.Runtime.CompilerServices.CallSite, System.Object, int]]:
        ...

    def GetCallSignatures(self, obj: System.Object, ) -> System.Collections.Generic.IList[str]:
        ...

    def Collect(self, generation: int, ) -> int:
        ...

    def CompatInvoke(self, callInfo: System.Dynamic.CallInfo, ) -> IronPython.Runtime.Binding.CompatibilityInvokeBinder:
        ...

    def Convert(self, type: System.Type, resultKind: int, ) -> IronPython.Runtime.Binding.PythonConversionBinder:
        ...

    def ConvertRetObject(self, type: System.Type, resultKind: int, ) -> System.Dynamic.DynamicMetaObjectBinder:
        ...

    def Create(self, realFallback: IronPython.Runtime.Binding.CompatibilityInvokeBinder, callInfo: System.Dynamic.CallInfo, ) -> IronPython.Runtime.Binding.CreateFallback:
        ...

    def GetMember(self, name: str, isNoThrow: bool = ..., ) -> IronPython.Runtime.Binding.PythonGetMemberBinder:
        ...

    def CompatGetMember(self, name: str, isNoThrow: bool, ) -> IronPython.Runtime.Binding.CompatibilityGetMember:
        ...

    def PrintHeader(self, result: ref[System.Text.StringBuilder], printedHeader: ref[bool], ) -> None:
        ...

    def FormatStackTraceNoDetail(self, e: System.Exception, printedHeader: ref[bool], ) -> str:
        ...

    @staticmethod
    def FrameToString(frame: Microsoft.Scripting.Runtime.DynamicStackFrame, ) -> str:
        ...

    def GetService(self, args: System.Array[System.Object], ) -> TService:
        ...

    def GetPythonService(self, engine: Microsoft.Scripting.Hosting.ScriptEngine, ) -> IronPython.Hosting.PythonService:
        ...

    @staticmethod
    def GetPythonOptions(context: IronPython.Runtime.CodeContext, ) -> IronPython.Runtime.PythonOptions:
        ...

    def InsertIntoPath(self, index: int, directory: str, ) -> None:
        ...

    @typing.overload
    def AddToPath(self, directory: str, ) -> None:
        ...

    @typing.overload
    def AddToPath(self, directory: str, index: int, ) -> None:
        ...

    def GetPythonCompilerOptions(self, ) -> IronPython.Compiler.PythonCompilerOptions:
        ...

    @typing.overload
    def GetCompilerOptions(self, ) -> Microsoft.Scripting.CompilerOptions:
        ...

    @typing.overload
    def GetCompilerOptions(self, scope: Microsoft.Scripting.Runtime.Scope, ) -> Microsoft.Scripting.CompilerOptions:
        ...

    def GetExceptionMessage(self, exception: System.Exception, message: ref[str], typeName: ref[str], ) -> None:
        ...

    def GetDefaultEncodingName(self, ) -> str:
        ...

    def InitializeBuiltins(self, ) -> None:
        ...

    def CreateBuiltinTable(self, ) -> System.Collections.Generic.Dictionary[str, System.Type]:
        ...

    def LoadBuiltins(self, builtinTable: System.Collections.Generic.Dictionary[str, System.Type], assem: System.Reflection.Assembly, updateSys: bool, ) -> None:
        ...

    @staticmethod
    def GetIronPythonAssembly(baseName: str, ) -> str:
        ...

    def BuiltinsChanged(self, sender: System.Object, e: Microsoft.Scripting.Runtime.ModuleChangeEventArgs, ) -> None:
        ...

    def TryGetModuleGlobalCache(self, name: str, cache: ref[IronPython.Runtime.ModuleGlobalCache], ) -> bool:
        ...

    @typing.overload
    def SetHostVariables(self, prefix: str, executable: str, versionString: str, ) -> None:
        ...

    @typing.overload
    def SetHostVariables(self, dict: IronPython.Runtime.PythonDictionary, ) -> None:
        ...

    def SetVersionVariables(self, dict: IronPython.Runtime.PythonDictionary, ) -> None:
        ...

    @staticmethod
    def GetPlatform() -> str:
        ...

    @staticmethod
    def GetVersionString() -> str:
        ...

    @staticmethod
    def GetInitialPrefix() -> str:
        ...

    def GetMemberNames(self, obj: System.Object, ) -> System.Collections.Generic.IList[str]:
        ...

    def FormatObject(self, operations: Microsoft.Scripting.Runtime.DynamicOperations, obj: System.Object, ) -> str:
        ...

    def GetSystemStateValue(self, name: str, ) -> System.Object:
        ...

    def SetSystemStateValue(self, name: str, value: System.Object, ) -> None:
        ...

    def DelSystemStateValue(self, name: str, ) -> None:
        ...

    def SetStandardIO(self, ) -> None:
        ...

    def ExecuteProgram(self, program: Microsoft.Scripting.SourceUnit, ) -> int:
        ...

    def GetGenericSiteStorage(self, ) -> IronPython.Runtime.SiteLocalStorage[T]:
        ...

    def GetGenericCallSiteStorage(self, ) -> IronPython.Runtime.SiteLocalStorage[System.Runtime.CompilerServices.CallSite[System.Func[System.Runtime.CompilerServices.CallSite, IronPython.Runtime.CodeContext, System.Object, System.Array[System.Object], System.Object]]]:
        ...

    def GetGenericCallSiteStorage0(self, ) -> IronPython.Runtime.SiteLocalStorage[System.Runtime.CompilerServices.CallSite[System.Func[System.Runtime.CompilerServices.CallSite, IronPython.Runtime.CodeContext, System.Object, System.Object]]]:
        ...

    def GetGenericKeywordCallSiteStorage(self, ) -> IronPython.Runtime.SiteLocalStorage[System.Runtime.CompilerServices.CallSite[System.Func[System.Runtime.CompilerServices.CallSite, IronPython.Runtime.CodeContext, System.Object, System.Array[System.Object], System.Collections.Generic.IDictionary[System.Object, System.Object], System.Object]]]:
        ...

    def CreateConvertBinder(self, toType: System.Type, explicitCast: System.Nullable[bool], ) -> System.Dynamic.ConvertBinder:
        ...

    def CreateDeleteMemberBinder(self, name: str, ignoreCase: bool, ) -> System.Dynamic.DeleteMemberBinder:
        ...

    def CreateGetMemberBinder(self, name: str, ignoreCase: bool, ) -> System.Dynamic.GetMemberBinder:
        ...

    def CreateInvokeBinder(self, callInfo: System.Dynamic.CallInfo, ) -> System.Dynamic.InvokeBinder:
        ...

    def CreateBinaryOperationBinder(self, operation: int, ) -> System.Dynamic.BinaryOperationBinder:
        ...

    def CreateUnaryOperationBinder(self, operation: int, ) -> System.Dynamic.UnaryOperationBinder:
        ...

    def CreateSetMemberBinder(self, name: str, ignoreCase: bool, ) -> System.Dynamic.SetMemberBinder:
        ...

    def CreateCreateBinder(self, callInfo: System.Dynamic.CallInfo, ) -> System.Dynamic.CreateInstanceBinder:
        ...

    def GetSystemPythonTypeWeakRef(self, type: IronPython.Runtime.Types.PythonType, ) -> IronPython.Runtime.WeakRefTracker:
        ...

    def SetSystemPythonTypeWeakRef(self, type: IronPython.Runtime.Types.PythonType, value: IronPython.Runtime.WeakRefTracker, ) -> bool:
        ...

    def SetSystemPythonTypeFinalizer(self, type: IronPython.Runtime.Types.PythonType, value: IronPython.Runtime.WeakRefTracker, ) -> None:
        ...

    def TryConvertToWeakReferenceable(self, obj: System.Object, weakref: ref[IronPython.Runtime.IWeakReferenceable], ) -> bool:
        ...

    def ConvertToWeakReferenceable(self, obj: System.Object, ) -> IronPython.Runtime.IWeakReferenceable:
        ...

    @typing.overload
    def InvokeOperatorWorker(self, context: IronPython.Runtime.CodeContext, oper: int, target: System.Object, result: ref[System.Object], ) -> bool:
        ...

    @typing.overload
    def InvokeOperatorWorker(self, context: IronPython.Runtime.CodeContext, oper: int, target: System.Object, value1: System.Object, value2: System.Object, result: ref[System.Object], ) -> bool:
        ...

    @staticmethod
    def GetUnarySymbol(oper: int, ) -> str:
        ...

    @staticmethod
    def GetTernarySymbol(oper: int, ) -> str:
        ...

    @staticmethod
    @typing.overload
    def InvokeUnaryOperator(context: IronPython.Runtime.CodeContext, oper: int, target: System.Object, errorMsg: str, ) -> System.Object:
        ...

    @staticmethod
    @typing.overload
    def InvokeUnaryOperator(context: IronPython.Runtime.CodeContext, oper: int, target: System.Object, ) -> System.Object:
        ...

    @staticmethod
    def TryInvokeTernaryOperator(context: IronPython.Runtime.CodeContext, oper: int, target: System.Object, value1: System.Object, value2: System.Object, res: ref[System.Object], ) -> bool:
        ...

    def SetAttr(self, context: IronPython.Runtime.CodeContext, o: System.Object, name: str, value: System.Object, ) -> None:
        ...

    def DeleteAttr(self, context: IronPython.Runtime.CodeContext, o: System.Object, name: str, ) -> None:
        ...

    def DelIndex(self, target: System.Object, index: System.Object, ) -> None:
        ...

    def DelSlice(self, target: System.Object, start: System.Object, end: System.Object, ) -> None:
        ...

    def SetSlice(self, a: System.Object, start: System.Object, end: System.Object, value: System.Object, ) -> None:
        ...

    def GetDocumentation(self, obj: System.Object, ) -> str:
        ...

    def GetSiteCacheForSystemType(self, type: System.Type, ) -> IronPython.Runtime.Types.PythonSiteCache:
        ...

    def ConvertToInt32(self, value: System.Object, ) -> int:
        ...

    def TryConvertToString(self, str: System.Object, res: ref[str], ) -> bool:
        ...

    def TryConvertToInt32(self, val: System.Object, res: ref[int], ) -> bool:
        ...

    def TryConvertToIEnumerable(self, enumerable: System.Object, res: ref[System.Collections.IEnumerable], ) -> bool:
        ...

    def ManagerAssemblyLoaded(self, sender: System.Object, e: Microsoft.Scripting.AssemblyLoadedEventArgs, ) -> None:
        ...

    def InitialHasherImpl(self, o: System.Object, dlg: ref[IronPython.Runtime.HashDelegate], ) -> int:
        ...

    def IntHasherImpl(self, o: System.Object, dlg: ref[IronPython.Runtime.HashDelegate], ) -> int:
        ...

    def DoubleHasherImpl(self, o: System.Object, dlg: ref[IronPython.Runtime.HashDelegate], ) -> int:
        ...

    def StringHasherImpl(self, o: System.Object, dlg: ref[IronPython.Runtime.HashDelegate], ) -> int:
        ...

    def FallbackHasherImpl(self, o: System.Object, dlg: ref[IronPython.Runtime.HashDelegate], ) -> int:
        ...

    def HasModuleState(self, key: System.Object, ) -> bool:
        ...

    def EnsureModuleState(self, ) -> None:
        ...

    def GetModuleState(self, key: System.Object, ) -> System.Object:
        ...

    def SetModuleState(self, key: System.Object, value: System.Object, ) -> None:
        ...

    def GetSetModuleState(self, key: System.Object, value: System.Object, ) -> System.Object:
        ...

    def GetOrCreateModuleState(self, key: System.Object, value: System.Func[T], ) -> T:
        ...

    @typing.overload
    def EnsureModuleException(self, key: System.Object, dict: IronPython.Runtime.PythonDictionary, name: str, module: str, ) -> IronPython.Runtime.Types.PythonType:
        ...

    @typing.overload
    def EnsureModuleException(self, key: System.Object, baseType: IronPython.Runtime.Types.PythonType, dict: IronPython.Runtime.PythonDictionary, name: str, module: str, ) -> IronPython.Runtime.Types.PythonType:
        ...

    @typing.overload
    def EnsureModuleException(self, key: System.Object, baseType: IronPython.Runtime.Types.PythonType, underlyingType: System.Type, dict: IronPython.Runtime.PythonDictionary, name: str, module: str, exceptionMaker: System.Func[str, System.Exception, System.Exception], ) -> IronPython.Runtime.Types.PythonType:
        ...

    @typing.overload
    def EnsureModuleException(self, key: System.Object, baseType: IronPython.Runtime.Types.PythonType, underlyingType: System.Type, dict: IronPython.Runtime.PythonDictionary, name: str, module: str, documentation: str, exceptionMaker: System.Func[str, System.Exception, System.Exception], ) -> IronPython.Runtime.Types.PythonType:
        ...

    @typing.overload
    def EnsureModuleException(self, key: System.Object, baseTypes: System.Array[IronPython.Runtime.Types.PythonType], underlyingType: System.Type, dict: IronPython.Runtime.PythonDictionary, name: str, module: str, ) -> IronPython.Runtime.Types.PythonType:
        ...

    def TryGetSystemPath(self, path: ref[IronPython.Runtime.PythonList], ) -> bool:
        ...

    def GetModuleByName(self, name: str, ) -> IronPython.Runtime.PythonModule:
        ...

    def GetModuleByPath(self, path: str, ) -> IronPython.Runtime.PythonModule:
        ...

    @staticmethod
    def GetPythonVersion() -> System.Version:
        ...

    def InitializeSystemState(self, ) -> None:
        ...

    def EmitDebugSymbols(self, sourceUnit: Microsoft.Scripting.SourceUnit, ) -> bool:
        ...

    def InitializeSysFlags(self, ) -> None:
        ...

    def ShouldInterpret(self, options: IronPython.Compiler.PythonCompilerOptions, source: Microsoft.Scripting.SourceUnit, ) -> bool:
        ...

    @staticmethod
    def ParseAndBindAst(context: Microsoft.Scripting.Runtime.CompilerContext, ) -> IronPython.Compiler.Ast.PythonAst:
        ...

    @staticmethod
    def CompilePythonCode(sourceUnit: Microsoft.Scripting.SourceUnit, options: Microsoft.Scripting.CompilerOptions, errorSink: Microsoft.Scripting.ErrorSink, ) -> Microsoft.Scripting.ScriptCode:
        ...

    def CompileSourceCode(self, sourceUnit: Microsoft.Scripting.SourceUnit, options: Microsoft.Scripting.CompilerOptions, errorSink: Microsoft.Scripting.ErrorSink, ) -> Microsoft.Scripting.ScriptCode:
        ...

    def LoadCompiledCode(self, method: System.Delegate, path: str, customData: str, ) -> Microsoft.Scripting.ScriptCode:
        ...

    def GetSourceReader(self, stream: System.IO.Stream, defaultEncoding: System.Text.Encoding, path: str, ) -> Microsoft.Scripting.SourceCodeReader:
        ...

    @staticmethod
    def ReadOneLine(stream: System.IO.Stream, maxBytes: int, ) -> str:
        ...

    def GenerateSourceCode(self, codeDom: System.CodeDom.CodeObject, path: str, kind: int, ) -> Microsoft.Scripting.SourceUnit:
        ...

    def GetScope(self, path: str, ) -> Microsoft.Scripting.Runtime.Scope:
        ...

    def InitializeModule(self, fileName: str, moduleContext: IronPython.Runtime.ModuleContext, scriptCode: Microsoft.Scripting.ScriptCode, options: int, ) -> IronPython.Runtime.PythonModule:
        ...

    def CreateScopeExtension(self, scope: Microsoft.Scripting.Runtime.Scope, ) -> Microsoft.Scripting.Runtime.ScopeExtension:
        ...

    @typing.overload
    def CompileModule(self, fileName: str, moduleName: str, sourceCode: Microsoft.Scripting.SourceUnit, options: int, ) -> IronPython.Runtime.PythonModule:
        ...

    @typing.overload
    def CompileModule(self, fileName: str, moduleName: str, sourceCode: Microsoft.Scripting.SourceUnit, options: int, scriptCode: ref[Microsoft.Scripting.ScriptCode], ) -> IronPython.Runtime.PythonModule:
        ...

    @typing.overload
    def GetScriptCode(self, sourceCode: Microsoft.Scripting.SourceUnit, moduleName: str, options: int, ) -> Microsoft.Scripting.ScriptCode:
        ...

    @typing.overload
    def GetScriptCode(self, sourceCode: Microsoft.Scripting.SourceUnit, moduleName: str, options: int, mode: IronPython.Compiler.CompilationMode, ) -> Microsoft.Scripting.ScriptCode:
        ...

    def GetBuiltinModule(self, name: str, ) -> IronPython.Runtime.PythonModule:
        ...

    @typing.overload
    def CreateBuiltinModule(self, name: str, ) -> IronPython.Runtime.PythonModule:
        ...

    @typing.overload
    def CreateBuiltinModule(self, moduleName: str, type: System.Type, ) -> IronPython.Runtime.PythonModule:
        ...

    def PublishModule(self, name: str, module: IronPython.Runtime.PythonModule, ) -> None:
        ...

    def GetReloadableModule(self, module: IronPython.Runtime.PythonModule, ) -> IronPython.Runtime.PythonModule:
        ...

    def GetCopyRegModule(self, ) -> System.Object:
        ...

    def GetWarningsModule(self, ) -> System.Object:
        ...

    def EnsureEncodings(self, ) -> None:
        ...

    def GetModuleGlobalCache(self, name: str, ) -> IronPython.Runtime.ModuleGlobalCache:
        ...

    def LoadAssemblyFromFile(self, file: str, ) -> System.Reflection.Assembly:
        ...

    def TryLoadAssemblyFromFileWithPath(self, path: str, res: ref[System.Reflection.Assembly], ) -> bool:
        ...

    def CurrentDomain_AssemblyResolve(self, sender: System.Object, args: System.ResolveEventArgs, ) -> System.Reflection.Assembly:
        ...

    def HookAssemblyResolve(self, ) -> None:
        ...

    def UnhookAssemblyResolve(self, ) -> None:
        ...

    def GetSearchPaths(self, ) -> System.Collections.Generic.ICollection[str]:
        ...

    def SetSearchPaths(self, paths: System.Collections.Generic.ICollection[str], ) -> None:
        ...

    def Shutdown(self, ) -> None:
        ...

    def FormatException(self, exception: System.Exception, ) -> str:
        ...

    @staticmethod
    def FormatPythonSyntaxError(e: Microsoft.Scripting.SyntaxErrorException, ) -> str:
        ...

    @staticmethod
    def GetSourceLine(e: Microsoft.Scripting.SyntaxErrorException, ) -> str:
        ...

    @staticmethod
    def FormatCLSException(e: System.Exception, ) -> str:
        ...

    @staticmethod
    def FormatPythonException(pythonException: System.Object, ) -> str:
        ...

    @staticmethod
    def GetPythonExceptionClassName(pythonException: System.Object, ) -> str:
        ...

    def GetStackFrames(self, exception: System.Exception, ) -> System.Collections.Generic.IList[Microsoft.Scripting.Runtime.DynamicStackFrame]:
        ...

    @typing.overload
    def FormatStackTraces(self, e: System.Exception, ) -> str:
        ...

    @typing.overload
    def FormatStackTraces(self, e: System.Exception, printedHeader: ref[bool], ) -> str:
        ...

class CompiledLoader(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    def __init__(self, ):
        ...

    def AddScriptCode(self, code: Microsoft.Scripting.ScriptCode, ) -> None:
        ...

    def find_module(self, context: IronPython.Runtime.CodeContext, fullname: str, path: IronPython.Runtime.PythonList = ..., ) -> IronPython.Runtime.ModuleLoader:
        ...

class Enumerate(System.Collections.IEnumerator, System.Collections.Generic.IEnumerator[System.Object], System.IDisposable, System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def Current(self) -> System.Object:
        ...

    @property
    def Current(self) -> System.Object:
        ...

    # methods
    @typing.overload
    def __init__(self, iter: System.Object, ):
        ...

    @typing.overload
    def __init__(self, context: IronPython.Runtime.CodeContext, iter: System.Object, start: System.Object, ):
        ...

    def __iter__(self, ) -> System.Object:
        ...

    def __reduce__(self, ) -> IronPython.Runtime.PythonTuple:
        ...

    @staticmethod
    def AddOneTo(_index: System.Object, ) -> System.Object:
        ...

    def Reset(self, ) -> None:
        ...

    def MoveNext(self, ) -> bool:
        ...

    def Dispose(self, ) -> None:
        ...

    def Dispose(self, notFinalizing: bool, ) -> None:
        ...

class BufferBytesEnumerator(System.ValueType):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def Current(self) -> int:
        ...

    # methods
    def __init__(self, buffer: IronPython.Runtime.IPythonBuffer, ):
        ...

    def MoveNext(self, ) -> bool:
        ...

    def GetEnumerator(self, ) -> IronPython.Runtime.BufferBytesEnumerator:
        ...

    @staticmethod
    def EnumerateDimension(buffer: IronPython.Runtime.IPythonBuffer, ofs: int, dim: int, ) -> System.Collections.Generic.IEnumerable[int]:
        ...

class FrozenSetCollection(System.Collections.IEnumerable, System.Collections.Generic.IEnumerable[System.Object], System.Collections.ICollection, System.Collections.IStructuralEquatable, IronPython.Runtime.ICodeFormattable, IronPython.Runtime.IWeakReferenceable, System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        self._items: IronPython.Runtime.SetStorage
        ...

    # static fields

    # properties
    @property
    def Empty(self) -> IronPython.Runtime.FrozenSetCollection:
        ...

    @property
    def Count(self) -> int:
        ...

    @property
    def IsSynchronized(self) -> bool:
        ...

    @property
    def SyncRoot(self) -> System.Object:
        ...

    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def __init__(self, set: IronPython.Runtime.SetStorage, ):
        ...

    @typing.overload
    def __init__(self, set: System.Object, ):
        ...

    def __init__(self, o: System.Array[System.Object], ) -> None:
        ...

    @staticmethod
    @typing.overload
    def __new__(context: IronPython.Runtime.CodeContext, cls: IronPython.Runtime.Types.PythonType, ) -> IronPython.Runtime.FrozenSetCollection:
        ...

    @staticmethod
    @typing.overload
    def __new__(context: IronPython.Runtime.CodeContext, cls: IronPython.Runtime.Types.PythonType, set: System.Object, ) -> IronPython.Runtime.FrozenSetCollection:
        ...

    @staticmethod
    @typing.overload
    def Make(items: IronPython.Runtime.SetStorage, ) -> IronPython.Runtime.FrozenSetCollection:
        ...

    @staticmethod
    @typing.overload
    def Make(set: System.Object, ) -> IronPython.Runtime.FrozenSetCollection:
        ...

    def copy(self, ) -> IronPython.Runtime.FrozenSetCollection:
        ...

    def __len__(self, ) -> int:
        ...

    def __contains__(self, item: System.Object, ) -> bool:
        ...

    def __reduce__(self, context: IronPython.Runtime.CodeContext, ) -> IronPython.Runtime.PythonTuple:
        ...

    def CalculateHashCode(self, comparer: System.Collections.IEqualityComparer, ) -> int:
        ...

    def GetHashCode(self, comparer: System.Collections.IEqualityComparer, ) -> int:
        ...

    def Equals(self, other: System.Object, comparer: System.Collections.IEqualityComparer, ) -> bool:
        ...

    def __eq__(self, other: System.Object, ) -> System.Object:
        ...

    def __ne__(self, other: System.Object, ) -> System.Object:
        ...

    @typing.overload
    def isdisjoint(self, set: IronPython.Runtime.FrozenSetCollection, ) -> bool:
        ...

    @typing.overload
    def isdisjoint(self, set: IronPython.Runtime.SetCollection, ) -> bool:
        ...

    @typing.overload
    def isdisjoint(self, set: System.Object, ) -> bool:
        ...

    @typing.overload
    def issubset(self, set: IronPython.Runtime.FrozenSetCollection, ) -> bool:
        ...

    @typing.overload
    def issubset(self, set: IronPython.Runtime.SetCollection, ) -> bool:
        ...

    @typing.overload
    def issubset(self, set: System.Object, ) -> bool:
        ...

    @typing.overload
    def issuperset(self, set: IronPython.Runtime.FrozenSetCollection, ) -> bool:
        ...

    @typing.overload
    def issuperset(self, set: IronPython.Runtime.SetCollection, ) -> bool:
        ...

    @typing.overload
    def issuperset(self, set: System.Object, ) -> bool:
        ...

    @typing.overload
    def union(self, ) -> IronPython.Runtime.FrozenSetCollection:
        ...

    @typing.overload
    def union(self, set: IronPython.Runtime.FrozenSetCollection, ) -> IronPython.Runtime.FrozenSetCollection:
        ...

    @typing.overload
    def union(self, set: IronPython.Runtime.SetCollection, ) -> IronPython.Runtime.FrozenSetCollection:
        ...

    @typing.overload
    def union(self, set: System.Object, ) -> IronPython.Runtime.FrozenSetCollection:
        ...

    @typing.overload
    def union(self, sets: System.Array[System.Object], ) -> IronPython.Runtime.FrozenSetCollection:
        ...

    @typing.overload
    def intersection(self, ) -> IronPython.Runtime.FrozenSetCollection:
        ...

    @typing.overload
    def intersection(self, set: IronPython.Runtime.FrozenSetCollection, ) -> IronPython.Runtime.FrozenSetCollection:
        ...

    @typing.overload
    def intersection(self, set: IronPython.Runtime.SetCollection, ) -> IronPython.Runtime.FrozenSetCollection:
        ...

    @typing.overload
    def intersection(self, set: System.Object, ) -> IronPython.Runtime.FrozenSetCollection:
        ...

    @typing.overload
    def intersection(self, sets: System.Array[System.Object], ) -> IronPython.Runtime.FrozenSetCollection:
        ...

    @typing.overload
    def difference(self, ) -> IronPython.Runtime.FrozenSetCollection:
        ...

    @typing.overload
    def difference(self, set: IronPython.Runtime.FrozenSetCollection, ) -> IronPython.Runtime.FrozenSetCollection:
        ...

    @typing.overload
    def difference(self, set: IronPython.Runtime.SetCollection, ) -> IronPython.Runtime.FrozenSetCollection:
        ...

    @typing.overload
    def difference(self, set: System.Object, ) -> IronPython.Runtime.FrozenSetCollection:
        ...

    @typing.overload
    def difference(self, sets: System.Array[System.Object], ) -> IronPython.Runtime.FrozenSetCollection:
        ...

    @typing.overload
    def symmetric_difference(self, set: IronPython.Runtime.FrozenSetCollection, ) -> IronPython.Runtime.FrozenSetCollection:
        ...

    @typing.overload
    def symmetric_difference(self, set: IronPython.Runtime.SetCollection, ) -> IronPython.Runtime.FrozenSetCollection:
        ...

    @typing.overload
    def symmetric_difference(self, set: System.Object, ) -> IronPython.Runtime.FrozenSetCollection:
        ...

    def GetEnumerator(self, ) -> System.Collections.IEnumerator:
        ...

    def GetEnumerator(self, ) -> System.Collections.Generic.IEnumerator[System.Object]:
        ...

    def __repr__(self, context: IronPython.Runtime.CodeContext, ) -> str:
        ...

    def CopyTo(self, array: System.Array, index: int, ) -> None:
        ...

    def GetWeakRef(self, ) -> IronPython.Runtime.WeakRefTracker:
        ...

    def SetWeakRef(self, value: IronPython.Runtime.WeakRefTracker, ) -> bool:
        ...

    def SetFinalizer(self, value: IronPython.Runtime.WeakRefTracker, ) -> None:
        ...

class IWeakReferenceable(abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    @abc.abstractmethod
    def GetWeakRef(self, ) -> IronPython.Runtime.WeakRefTracker:
        ...

    @abc.abstractmethod
    def SetWeakRef(self, value: IronPython.Runtime.WeakRefTracker, ) -> bool:
        ...

    @abc.abstractmethod
    def SetFinalizer(self, value: IronPython.Runtime.WeakRefTracker, ) -> None:
        ...

class ICodeFormattable(abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    @abc.abstractmethod
    def __repr__(self, context: IronPython.Runtime.CodeContext, ) -> str:
        ...

class PythonRange(System.Collections.Generic.IEnumerable[int], System.Collections.IEnumerable, IronPython.Runtime.ICodeFormattable, IronPython.Runtime.IReversible, System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        self._start: System.Numerics.BigInteger
        self._stop: System.Numerics.BigInteger
        self._step: System.Numerics.BigInteger
        self._length: System.Numerics.BigInteger
        ...

    # static fields

    # properties
    @property
    def start(self) -> System.Object:
        ...
    @start.setter
    def start(self, val: System.Object):
        ...

    @property
    def stop(self) -> System.Object:
        ...
    @stop.setter
    def stop(self, val: System.Object):
        ...

    @property
    def step(self) -> System.Object:
        ...
    @step.setter
    def step(self, val: System.Object):
        ...

    @property
    def Item(self) -> System.Object:
        ...

    @property
    def Item(self) -> System.Object:
        ...

    @property
    def Item(self) -> System.Object:
        ...

    @property
    def Item(self) -> System.Object:
        ...

    # methods
    @typing.overload
    def __init__(self, stop: System.Object, ):
        ...

    @typing.overload
    def __init__(self, start: System.Object, stop: System.Object, ):
        ...

    @typing.overload
    def __init__(self, start: System.Object, stop: System.Object, step: System.Object, ):
        ...

    @staticmethod
    def AsIndex(obj: System.Object, big: ref[System.Numerics.BigInteger], ) -> System.Object:
        ...

    def __reduce__(self, ) -> IronPython.Runtime.PythonTuple:
        ...

    def __len__(self, ) -> int:
        ...

    @typing.overload
    def __eq__(self, other: IronPython.Runtime.PythonRange, ) -> bool:
        ...

    @typing.overload
    def __eq__(self, other: System.Object, ) -> System.Object:
        ...

    def __hash__(self, ) -> int:
        ...

    def __contains__(self, context: IronPython.Runtime.CodeContext, item: System.Object, ) -> bool:
        ...

    @staticmethod
    def TryConvertToInt(value: System.Object, converted: ref[System.Numerics.BigInteger], ) -> bool:
        ...

    @typing.overload
    def CountOf(self, value: System.Numerics.BigInteger, ) -> int:
        ...

    @typing.overload
    def CountOf(self, context: IronPython.Runtime.CodeContext, obj: System.Object, ) -> int:
        ...

    @typing.overload
    def IndexOf(self, value: System.Numerics.BigInteger, ) -> System.Numerics.BigInteger:
        ...

    @typing.overload
    def IndexOf(self, context: IronPython.Runtime.CodeContext, obj: System.Object, ) -> int:
        ...

    def count(self, context: IronPython.Runtime.CodeContext, value: System.Object, ) -> System.Object:
        ...

    def index(self, context: IronPython.Runtime.CodeContext, value: System.Object, ) -> System.Numerics.BigInteger:
        ...

    def Last(self, ) -> System.Numerics.BigInteger:
        ...

    def __iter__(self, ) -> System.Collections.IEnumerator:
        ...

    def __reversed__(self, ) -> System.Collections.IEnumerator:
        ...

    def GetEnumerator(self, ) -> System.Collections.IEnumerator:
        ...

    def GetEnumerator(self, ) -> System.Collections.Generic.IEnumerator[int]:
        ...

    def __repr__(self, context: IronPython.Runtime.CodeContext, ) -> str:
        ...

class SiteLocalStorage(System.Object, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    def __init__(self, ):
        ...

class PythonOptions(Microsoft.Scripting.LanguageOptions):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def Arguments(self) -> System.Collections.ObjectModel.ReadOnlyCollection[str]:
        ...

    @property
    def Optimize(self) -> bool:
        ...

    @property
    def StripDocStrings(self) -> bool:
        ...

    @property
    def WarningFilters(self) -> System.Collections.ObjectModel.ReadOnlyCollection[str]:
        ...

    @property
    def BytesWarning(self) -> int:
        ...

    @property
    def Debug(self) -> bool:
        ...

    @property
    def Inspect(self) -> bool:
        ...

    @property
    def NoUserSite(self) -> bool:
        ...

    @property
    def NoSite(self) -> bool:
        ...

    @property
    def IgnoreEnvironment(self) -> bool:
        ...

    @property
    def Isolated(self) -> bool:
        ...

    @property
    def Verbose(self) -> bool:
        ...

    @property
    def RecursionLimit(self) -> int:
        ...

    @property
    def Frames(self) -> bool:
        ...

    @property
    def FullFrames(self) -> bool:
        ...

    @property
    def Tracing(self) -> bool:
        ...

    @property
    def LightweightScopes(self) -> bool:
        ...

    @property
    def EnableProfiler(self) -> bool:
        ...
    @EnableProfiler.setter
    def EnableProfiler(self, val: bool):
        ...

    @property
    def GCStress(self) -> System.Nullable[int]:
        ...

    @property
    def NoDebug(self) -> System.Text.RegularExpressions.Regex:
        ...

    @property
    def Quiet(self) -> bool:
        ...

    @property
    def NoImportLib(self) -> bool:
        ...

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
    def EnsureSearchPaths(options: System.Collections.Generic.IDictionary[str, System.Object], ) -> System.Collections.Generic.IDictionary[str, System.Object]:
        ...

class PythonTupleEnumerator(System.Collections.Generic.IEnumerable[System.Object], System.Collections.IEnumerable, System.Collections.Generic.IEnumerator[System.Object], System.IDisposable, System.Collections.IEnumerator, System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def Current(self) -> System.Object:
        ...

    # methods
    def __init__(self, t: IronPython.Runtime.PythonTuple, ):
        ...

    def GetEnumerator(self, ) -> System.Collections.IEnumerator:
        ...

    def GetEnumerator(self, ) -> System.Collections.Generic.IEnumerator[System.Object]:
        ...

    def MoveNext(self, ) -> bool:
        ...

    def Reset(self, ) -> None:
        ...

    def Dispose(self, ) -> None:
        ...

    def __reduce__(self, context: IronPython.Runtime.CodeContext, ) -> IronPython.Runtime.PythonTuple:
        ...

    def __setstate__(self, state: int, ) -> None:
        ...

    def __length_hint__(self, ) -> int:
        ...

class ByteArrayIterator(System.Collections.IEnumerable, System.Collections.Generic.IEnumerator[int], System.IDisposable, System.Collections.IEnumerator, System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def Current(self) -> int:
        ...

    @property
    def Current(self) -> System.Object:
        ...

    # methods
    def __init__(self, bytes: IronPython.Runtime.ByteArray, ):
        ...

    def __length_hint__(self, ) -> int:
        ...

    def __reduce__(self, context: IronPython.Runtime.CodeContext, ) -> IronPython.Runtime.PythonTuple:
        ...

    def __setstate__(self, state: int, ) -> None:
        ...

    def Dispose(self, ) -> None:
        ...

    def MoveNext(self, ) -> bool:
        ...

    def Reset(self, ) -> None:
        ...

    def GetEnumerator(self, ) -> System.Collections.IEnumerator:
        ...

class Slice(IronPython.Runtime.ICodeFormattable, Microsoft.Scripting.Runtime.ISlice, System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def start(self) -> System.Object:
        ...

    @property
    def stop(self) -> System.Object:
        ...

    @property
    def step(self) -> System.Object:
        ...

    @property
    def Start(self) -> System.Object:
        ...

    @property
    def Stop(self) -> System.Object:
        ...

    @property
    def Step(self) -> System.Object:
        ...

    # methods
    @typing.overload
    def __init__(self, stop: System.Object, ):
        ...

    @typing.overload
    def __init__(self, start: System.Object, stop: System.Object, ):
        ...

    @typing.overload
    def __init__(self, start: System.Object, stop: System.Object, step: System.Object, ):
        ...

    @typing.overload
    def indices(self, length: int, ostart: ref[System.Numerics.BigInteger], ostop: ref[System.Numerics.BigInteger], ostep: ref[System.Numerics.BigInteger], ) -> None:
        ...

    @typing.overload
    def indices(self, length: System.Object, ostart: ref[System.Numerics.BigInteger], ostop: ref[System.Numerics.BigInteger], ostep: ref[System.Numerics.BigInteger], ) -> None:
        ...

    def __reduce__(self, ) -> IronPython.Runtime.PythonTuple:
        ...

    def __hash__(self, ) -> int:
        ...

    def __repr__(self, context: IronPython.Runtime.CodeContext, ) -> str:
        ...

    def ToTuple(self, ) -> IronPython.Runtime.PythonTuple:
        ...

    def Equals(self, other: IronPython.Runtime.Slice, ) -> bool:
        ...

    def __eq__(self, other: IronPython.Runtime.Slice, ) -> bool:
        ...

    def __ne__(self, other: IronPython.Runtime.Slice, ) -> bool:
        ...

    def Indices(self, length: int, ostart: ref[int], ostop: ref[int], ostep: ref[int], ) -> None:
        ...

    @typing.overload
    def DoSliceAssign(self, assign: IronPython.Runtime.Slice.SliceAssign, size: int, value: System.Object, ) -> None:
        ...

    @staticmethod
    @typing.overload
    def DoSliceAssign(assign: IronPython.Runtime.Slice.SliceAssign, start: int, stop: int, step: int, value: System.Object, ) -> None:
        ...

    @staticmethod
    def ListSliceAssign(assign: IronPython.Runtime.Slice.SliceAssign, start: int, n: int, step: int, lst: System.Collections.IList, ) -> None:
        ...

    @staticmethod
    def OtherSliceAssign(assign: IronPython.Runtime.Slice.SliceAssign, start: int, stop: int, step: int, value: System.Object, ) -> None:
        ...

    def GetIndicesAndCount(self, length: int, ostart: ref[int], ostop: ref[int], ostep: ref[int], count: ref[int], ) -> None:
        ...

class FunctionCaller(IronPython.Runtime.FunctionCaller, typing.Generic[T0, T1]):
    @typing.overload
    def __init__(self, **kwargs):
        self._compat: int
        ...

    # static fields

    # properties
    # methods
    def __init__(self, compat: int, ):
        ...

    def Call2(self, site: System.Runtime.CompilerServices.CallSite, context: IronPython.Runtime.CodeContext, func: System.Object, arg0: T0, arg1: T1, ) -> System.Object:
        ...

    def Default1Call2(self, site: System.Runtime.CompilerServices.CallSite, context: IronPython.Runtime.CodeContext, func: System.Object, arg0: T0, arg1: T1, ) -> System.Object:
        ...

    def Default2Call2(self, site: System.Runtime.CompilerServices.CallSite, context: IronPython.Runtime.CodeContext, func: System.Object, arg0: T0, arg1: T1, ) -> System.Object:
        ...

    def Default3Call2(self, site: System.Runtime.CompilerServices.CallSite, context: IronPython.Runtime.CodeContext, func: System.Object, arg0: T0, arg1: T1, ) -> System.Object:
        ...

    def Default4Call2(self, site: System.Runtime.CompilerServices.CallSite, context: IronPython.Runtime.CodeContext, func: System.Object, arg0: T0, arg1: T1, ) -> System.Object:
        ...

    def Default5Call2(self, site: System.Runtime.CompilerServices.CallSite, context: IronPython.Runtime.CodeContext, func: System.Object, arg0: T0, arg1: T1, ) -> System.Object:
        ...

    def Default6Call2(self, site: System.Runtime.CompilerServices.CallSite, context: IronPython.Runtime.CodeContext, func: System.Object, arg0: T0, arg1: T1, ) -> System.Object:
        ...

    def Default7Call2(self, site: System.Runtime.CompilerServices.CallSite, context: IronPython.Runtime.CodeContext, func: System.Object, arg0: T0, arg1: T1, ) -> System.Object:
        ...

    def Default8Call2(self, site: System.Runtime.CompilerServices.CallSite, context: IronPython.Runtime.CodeContext, func: System.Object, arg0: T0, arg1: T1, ) -> System.Object:
        ...

    def Default9Call2(self, site: System.Runtime.CompilerServices.CallSite, context: IronPython.Runtime.CodeContext, func: System.Object, arg0: T0, arg1: T1, ) -> System.Object:
        ...

    def Default10Call2(self, site: System.Runtime.CompilerServices.CallSite, context: IronPython.Runtime.CodeContext, func: System.Object, arg0: T0, arg1: T1, ) -> System.Object:
        ...

    def Default11Call2(self, site: System.Runtime.CompilerServices.CallSite, context: IronPython.Runtime.CodeContext, func: System.Object, arg0: T0, arg1: T1, ) -> System.Object:
        ...

class PythonRangeIterator(System.Collections.IEnumerable, System.Collections.Generic.IEnumerator[int], System.IDisposable, System.Collections.IEnumerator, System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def Current(self) -> System.Object:
        ...

    @property
    def Current(self) -> int:
        ...

    # methods
    def __init__(self, range: IronPython.Runtime.PythonRange, ):
        ...

    def MoveNext(self, ) -> bool:
        ...

    def Reset(self, ) -> None:
        ...

    def __reduce__(self, context: IronPython.Runtime.CodeContext, ) -> IronPython.Runtime.PythonTuple:
        ...

    def __setstate__(self, position: int, ) -> None:
        ...

    def Dispose(self, ) -> None:
        ...

    def GetEnumerator(self, ) -> System.Collections.IEnumerator:
        ...

    def __length_hint__(self, ) -> int:
        ...

class PythonListReverseIterator(System.Collections.Generic.IEnumerable[System.Object], System.Collections.IEnumerable, System.Collections.Generic.IEnumerator[System.Object], System.IDisposable, System.Collections.IEnumerator, System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def Current(self) -> System.Object:
        ...

    # methods
    def __init__(self, l: IronPython.Runtime.PythonList, ):
        ...

    def GetEnumerator(self, ) -> System.Collections.IEnumerator:
        ...

    def GetEnumerator(self, ) -> System.Collections.Generic.IEnumerator[System.Object]:
        ...

    def MoveNext(self, ) -> bool:
        ...

    def Reset(self, ) -> None:
        ...

    def Dispose(self, ) -> None:
        ...

    def __reduce__(self, context: IronPython.Runtime.CodeContext, ) -> IronPython.Runtime.PythonTuple:
        ...

    def __setstate__(self, state: int, ) -> None:
        ...

    def __length_hint__(self, ) -> int:
        ...

class BuiltinPythonModule(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def Context(self) -> IronPython.Runtime.PythonContext:
        ...

    @property
    def Globals(self) -> IronPython.Runtime.CodeContext:
        ...

    # methods
    def __init__(self, context: IronPython.Runtime.PythonContext, ):
        ...

    def Initialize(self, codeContext: IronPython.Runtime.CodeContext, optimizedGlobals: System.Collections.Generic.Dictionary[str, IronPython.Compiler.PythonGlobal], ) -> None:
        ...

    def GetGlobalVariableNames(self, ) -> System.Collections.Generic.IEnumerable[str]:
        ...

    def PerformModuleReload(self, ) -> None:
        ...

class FunctionCaller(IronPython.Runtime.FunctionCaller, typing.Generic[T0, T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12]):
    @typing.overload
    def __init__(self, **kwargs):
        self._compat: int
        ...

    # static fields

    # properties
    # methods
    def __init__(self, compat: int, ):
        ...

    def Call13(self, site: System.Runtime.CompilerServices.CallSite, context: IronPython.Runtime.CodeContext, func: System.Object, arg0: T0, arg1: T1, arg2: T2, arg3: T3, arg4: T4, arg5: T5, arg6: T6, arg7: T7, arg8: T8, arg9: T9, arg10: T10, arg11: T11, arg12: T12, ) -> System.Object:
        ...

class FunctionCode(Microsoft.Scripting.Runtime.IExpressionSerializable, IronPython.Runtime.ICodeFormattable, System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        self._normalDelegate: System.Delegate
        self._initialDoc: str
        self._tracingDelegate: System.Delegate
        ...

    # static fields

    # properties
    @property
    def IsOnDiskCode(self) -> bool:
        ...

    @property
    def Span(self) -> Microsoft.Scripting.SourceSpan:
        ...

    @property
    def ArgNames(self) -> System.Array[str]:
        ...

    @property
    def Flags(self) -> int:
        ...

    @property
    def IsModule(self) -> bool:
        ...

    @property
    def co_varnames(self) -> IronPython.Runtime.PythonTuple:
        ...

    @property
    def co_argcount(self) -> int:
        ...

    @property
    def co_kwonlyargcount(self) -> int:
        ...

    @property
    def co_cellvars(self) -> IronPython.Runtime.PythonTuple:
        ...

    @property
    def co_code(self) -> System.Object:
        ...

    @property
    def co_consts(self) -> IronPython.Runtime.PythonTuple:
        ...

    @property
    def co_filename(self) -> str:
        ...

    @property
    def co_firstlineno(self) -> int:
        ...

    @property
    def co_flags(self) -> int:
        ...

    @property
    def co_freevars(self) -> IronPython.Runtime.PythonTuple:
        ...

    @property
    def co_lnotab(self) -> System.Object:
        ...

    @property
    def co_name(self) -> str:
        ...

    @property
    def co_names(self) -> IronPython.Runtime.PythonTuple:
        ...

    @property
    def co_nlocals(self) -> System.Object:
        ...

    @property
    def co_stacksize(self) -> System.Object:
        ...

    @property
    def Code(self) -> Microsoft.Scripting.Ast.LightLambdaExpression:
        ...

    @property
    def PythonCode(self) -> IronPython.Compiler.Ast.ScopeStatement:
        ...

    @property
    def Target(self) -> System.Delegate:
        ...
    @Target.setter
    def Target(self, val: System.Delegate):
        ...

    @property
    def LightThrowTarget(self) -> System.Delegate:
        ...
    @LightThrowTarget.setter
    def LightThrowTarget(self, val: System.Delegate):
        ...

    # methods
    @typing.overload
    def __init__(self, context: IronPython.Runtime.PythonContext, code: System.Delegate, scope: IronPython.Compiler.Ast.ScopeStatement, documentation: str, localCount: int, ):
        ...

    @typing.overload
    def __init__(self, context: IronPython.Runtime.PythonContext, initialDelegate: System.Delegate, scope: IronPython.Compiler.Ast.ScopeStatement, documentation: str, tracing: System.Nullable[bool], register: bool, ):
        ...

    @staticmethod
    def SymbolListToTuple(vars: System.Collections.Generic.IList[str], ) -> IronPython.Runtime.PythonTuple:
        ...

    @staticmethod
    def StringArrayToTuple(closureVars: System.Array[str], ) -> IronPython.Runtime.PythonTuple:
        ...

    def RegisterFunctionCode(self, context: IronPython.Runtime.PythonContext, ) -> None:
        ...

    @staticmethod
    def CleanFunctionCodes(context: IronPython.Runtime.PythonContext, synchronous: bool, ) -> None:
        ...

    def SetTarget(self, target: System.Delegate, ) -> None:
        ...

    def LightThrowCompile(self, context: IronPython.Runtime.CodeContext, ) -> None:
        ...

    @staticmethod
    def GetAllCode(context: IronPython.Runtime.PythonContext, ) -> System.Collections.Generic.IEnumerable[IronPython.Runtime.FunctionCode]:
        ...

    @staticmethod
    def UpdateAllCode(context: IronPython.Runtime.PythonContext, ) -> None:
        ...

    @staticmethod
    def CodeCleanup(state: System.Object, ) -> None:
        ...

    @staticmethod
    def GetRootCodeNoUpdating(context: IronPython.Runtime.PythonContext, ) -> IronPython.Runtime.FunctionCode.CodeList:
        ...

    def __repr__(self, context: IronPython.Runtime.CodeContext, ) -> str:
        ...

    def Call(self, context: IronPython.Runtime.CodeContext, ) -> System.Object:
        ...

    @staticmethod
    def FromSourceUnit(sourceUnit: Microsoft.Scripting.SourceUnit, options: IronPython.Compiler.PythonCompilerOptions, register: bool, ) -> IronPython.Runtime.FunctionCode:
        ...

    def ExpandArgsTuple(self, names: System.Collections.Generic.List[str], toExpand: IronPython.Runtime.PythonTuple, ) -> None:
        ...

    def Equals(self, obj: System.Object, ) -> bool:
        ...

    def GetHashCode(self, ) -> int:
        ...

    def __gt__(self, context: IronPython.Runtime.CodeContext, other: System.Object, ) -> IronPython.Runtime.Types.NotImplementedType:
        ...

    def __lt__(self, context: IronPython.Runtime.CodeContext, other: System.Object, ) -> IronPython.Runtime.Types.NotImplementedType:
        ...

    def __ge__(self, context: IronPython.Runtime.CodeContext, other: System.Object, ) -> IronPython.Runtime.Types.NotImplementedType:
        ...

    def __le__(self, context: IronPython.Runtime.CodeContext, other: System.Object, ) -> IronPython.Runtime.Types.NotImplementedType:
        ...

    def LazyCompileFirstTarget(self, function: IronPython.Runtime.PythonFunction, ) -> None:
        ...

    def UpdateDelegate(self, context: IronPython.Runtime.PythonContext, forceCreation: bool, ) -> None:
        ...

    def SetDebugTarget(self, context: IronPython.Runtime.PythonContext, target: System.Delegate, ) -> None:
        ...

    def GetGeneratorOrNormalLambdaTracing(self, context: IronPython.Runtime.PythonContext, ) -> System.Linq.Expressions.LambdaExpression:
        ...

    def GetGeneratorOrNormalLambda(self, ) -> Microsoft.Scripting.Ast.LightLambdaExpression:
        ...

    @typing.overload
    def CompileLambda(self, code: Microsoft.Scripting.Ast.LightLambdaExpression, handler: System.EventHandler[Microsoft.Scripting.Interpreter.LightLambdaCompileEventArgs], ) -> System.Delegate:
        ...

    @typing.overload
    def CompileLambda(self, code: System.Linq.Expressions.LambdaExpression, handler: System.EventHandler[Microsoft.Scripting.Interpreter.LightLambdaCompileEventArgs], ) -> System.Delegate:
        ...

    def AddRecursionCheck(self, context: IronPython.Runtime.PythonContext, finalTarget: System.Delegate, ) -> System.Delegate:
        ...

    def CreateExpression(self, ) -> System.Linq.Expressions.Expression:
        ...

    @staticmethod
    def TupleToStringArray(tuple: IronPython.Runtime.PythonTuple, ) -> System.Linq.Expressions.Expression:
        ...

