from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import System
import IronPython.Modules.unicodedata
import IronPython.Runtime.Types
import System.Collections.Generic
import IronPython.Runtime
import System.Collections
import IronPython.Modules.PythonIOModule
import System.IO
import IronPython.Modules.Builtin
import System.Numerics
import IronPython.Compiler
import IronPython.Modules._ast
import Microsoft.Scripting
import IronPython.Runtime.Operations
import Microsoft.Scripting.Runtime
import System.Text
import IronPython.Modules.SysModule
import IronPython.Runtime.Exceptions
import IronPython.Compiler.Ast
import IronPython.Modules.PythonLocale


class unicodedata(System.Object, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def ucd_3_2_0(self) -> IronPython.Modules.unicodedata.UCD:
        ...

    @property
    def unidata_version(self) -> str:
        ...

    # methods
    @staticmethod
    def EnsureInitialized() -> None:
        ...

    @staticmethod
    def lookup(name: str, ) -> str:
        ...

    @staticmethod
    @typing.overload
    def name(unichr: str, ) -> str:
        ...

    @staticmethod
    @typing.overload
    def name(unichr: str, default: System.Object, ) -> System.Object:
        ...

    @staticmethod
    def TryGetName(rune: int, name: ref[str], ) -> bool:
        ...

    @staticmethod
    @typing.overload
    def decimal(unichr: str, default: int, ) -> int:
        ...

    @staticmethod
    @typing.overload
    def decimal(unichr: str, ) -> int:
        ...

    @staticmethod
    @typing.overload
    def decimal(unichr: str, default: System.Object, ) -> System.Object:
        ...

    @staticmethod
    @typing.overload
    def digit(unichr: str, default: int, ) -> int:
        ...

    @staticmethod
    @typing.overload
    def digit(unichr: str, default: System.Object, ) -> System.Object:
        ...

    @staticmethod
    @typing.overload
    def digit(unichr: str, ) -> int:
        ...

    @staticmethod
    @typing.overload
    def numeric(unichr: str, default: float, ) -> float:
        ...

    @staticmethod
    @typing.overload
    def numeric(unichr: str, ) -> float:
        ...

    @staticmethod
    @typing.overload
    def numeric(unichr: str, default: System.Object, ) -> System.Object:
        ...

    @staticmethod
    def category(unichr: str, ) -> str:
        ...

    @staticmethod
    def bidirectional(unichr: str, ) -> str:
        ...

    @staticmethod
    def combining(unichr: str, ) -> int:
        ...

    @staticmethod
    def east_asian_width(unichr: str, ) -> str:
        ...

    @staticmethod
    def mirrored(unichr: str, ) -> int:
        ...

    @staticmethod
    def decomposition(unichr: str, ) -> str:
        ...

    @staticmethod
    def normalize(form: str, unistr: str, ) -> str:
        ...

class Builtin(System.Object, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields
    None_: System.Object = ...
    __doc__: str = ...
    __package__: System.Object = ...
    __name__: str = ...

    # properties
    @property
    def True_(self) -> System.Object:
        ...

    @property
    def False_(self) -> System.Object:
        ...

    @property
    def Ellipsis(self) -> IronPython.Runtime.Types.Ellipsis:
        ...

    @property
    def NotImplemented(self) -> IronPython.Runtime.Types.NotImplementedType:
        ...

    @property
    def bool(self) -> IronPython.Runtime.Types.PythonType:
        ...

    @property
    def bytes(self) -> IronPython.Runtime.Types.PythonType:
        ...

    @property
    def bytearray(self) -> IronPython.Runtime.Types.PythonType:
        ...

    @property
    def classmethod(self) -> IronPython.Runtime.Types.PythonType:
        ...

    @property
    def complex(self) -> IronPython.Runtime.Types.PythonType:
        ...

    @property
    def dict(self) -> IronPython.Runtime.Types.PythonType:
        ...

    @property
    def enumerate(self) -> IronPython.Runtime.Types.PythonType:
        ...

    @property
    def filter(self) -> IronPython.Runtime.Types.PythonType:
        ...

    @property
    def float(self) -> IronPython.Runtime.Types.PythonType:
        ...

    @property
    def frozenset(self) -> IronPython.Runtime.Types.PythonType:
        ...

    @property
    def int(self) -> IronPython.Runtime.Types.PythonType:
        ...

    @property
    def set(self) -> IronPython.Runtime.Types.PythonType:
        ...

    @property
    def list(self) -> IronPython.Runtime.Types.PythonType:
        ...

    @property
    def memoryview(self) -> IronPython.Runtime.Types.PythonType:
        ...

    @property
    def map(self) -> IronPython.Runtime.Types.PythonType:
        ...

    @property
    def object(self) -> IronPython.Runtime.Types.PythonType:
        ...

    @property
    def property(self) -> IronPython.Runtime.Types.PythonType:
        ...

    @property
    def range(self) -> IronPython.Runtime.Types.PythonType:
        ...

    @property
    def reversed(self) -> IronPython.Runtime.Types.PythonType:
        ...

    @property
    def slice(self) -> IronPython.Runtime.Types.PythonType:
        ...

    @property
    def staticmethod(self) -> IronPython.Runtime.Types.PythonType:
        ...

    @property
    def super(self) -> IronPython.Runtime.Types.PythonType:
        ...

    @property
    def str(self) -> IronPython.Runtime.Types.PythonType:
        ...

    @property
    def tuple(self) -> IronPython.Runtime.Types.PythonType:
        ...

    @property
    def type(self) -> IronPython.Runtime.Types.PythonType:
        ...

    @property
    def zip(self) -> IronPython.Runtime.Types.PythonType:
        ...

    @property
    def BaseException(self) -> IronPython.Runtime.Types.PythonType:
        ...

    @property
    def EnvironmentError(self) -> IronPython.Runtime.Types.PythonType:
        ...

    @property
    def IOError(self) -> IronPython.Runtime.Types.PythonType:
        ...

    @property
    def WindowsError(self) -> IronPython.Runtime.Types.PythonType:
        ...

    @property
    def SystemExit(self) -> IronPython.Runtime.Types.PythonType:
        ...

    @property
    def KeyboardInterrupt(self) -> IronPython.Runtime.Types.PythonType:
        ...

    @property
    def GeneratorExit(self) -> IronPython.Runtime.Types.PythonType:
        ...

    @property
    def Exception(self) -> IronPython.Runtime.Types.PythonType:
        ...

    @property
    def StopIteration(self) -> IronPython.Runtime.Types.PythonType:
        ...

    @property
    def StopAsyncIteration(self) -> IronPython.Runtime.Types.PythonType:
        ...

    @property
    def ArithmeticError(self) -> IronPython.Runtime.Types.PythonType:
        ...

    @property
    def FloatingPointError(self) -> IronPython.Runtime.Types.PythonType:
        ...

    @property
    def OverflowError(self) -> IronPython.Runtime.Types.PythonType:
        ...

    @property
    def ZeroDivisionError(self) -> IronPython.Runtime.Types.PythonType:
        ...

    @property
    def AssertionError(self) -> IronPython.Runtime.Types.PythonType:
        ...

    @property
    def AttributeError(self) -> IronPython.Runtime.Types.PythonType:
        ...

    @property
    def BufferError(self) -> IronPython.Runtime.Types.PythonType:
        ...

    @property
    def EOFError(self) -> IronPython.Runtime.Types.PythonType:
        ...

    @property
    def ImportError(self) -> IronPython.Runtime.Types.PythonType:
        ...

    @property
    def LookupError(self) -> IronPython.Runtime.Types.PythonType:
        ...

    @property
    def IndexError(self) -> IronPython.Runtime.Types.PythonType:
        ...

    @property
    def KeyError(self) -> IronPython.Runtime.Types.PythonType:
        ...

    @property
    def MemoryError(self) -> IronPython.Runtime.Types.PythonType:
        ...

    @property
    def NameError(self) -> IronPython.Runtime.Types.PythonType:
        ...

    @property
    def UnboundLocalError(self) -> IronPython.Runtime.Types.PythonType:
        ...

    @property
    def OSError(self) -> IronPython.Runtime.Types.PythonType:
        ...

    @property
    def BlockingIOError(self) -> IronPython.Runtime.Types.PythonType:
        ...

    @property
    def ChildProcessError(self) -> IronPython.Runtime.Types.PythonType:
        ...

    @property
    def ConnectionError(self) -> IronPython.Runtime.Types.PythonType:
        ...

    @property
    def BrokenPipeError(self) -> IronPython.Runtime.Types.PythonType:
        ...

    @property
    def ConnectionAbortedError(self) -> IronPython.Runtime.Types.PythonType:
        ...

    @property
    def ConnectionRefusedError(self) -> IronPython.Runtime.Types.PythonType:
        ...

    @property
    def ConnectionResetError(self) -> IronPython.Runtime.Types.PythonType:
        ...

    @property
    def FileExistsError(self) -> IronPython.Runtime.Types.PythonType:
        ...

    @property
    def FileNotFoundError(self) -> IronPython.Runtime.Types.PythonType:
        ...

    @property
    def InterruptedError(self) -> IronPython.Runtime.Types.PythonType:
        ...

    @property
    def IsADirectoryError(self) -> IronPython.Runtime.Types.PythonType:
        ...

    @property
    def NotADirectoryError(self) -> IronPython.Runtime.Types.PythonType:
        ...

    @property
    def PermissionError(self) -> IronPython.Runtime.Types.PythonType:
        ...

    @property
    def ProcessLookupError(self) -> IronPython.Runtime.Types.PythonType:
        ...

    @property
    def TimeoutError(self) -> IronPython.Runtime.Types.PythonType:
        ...

    @property
    def ReferenceError(self) -> IronPython.Runtime.Types.PythonType:
        ...

    @property
    def RuntimeError(self) -> IronPython.Runtime.Types.PythonType:
        ...

    @property
    def NotImplementedError(self) -> IronPython.Runtime.Types.PythonType:
        ...

    @property
    def RecursionError(self) -> IronPython.Runtime.Types.PythonType:
        ...

    @property
    def SyntaxError(self) -> IronPython.Runtime.Types.PythonType:
        ...

    @property
    def IndentationError(self) -> IronPython.Runtime.Types.PythonType:
        ...

    @property
    def TabError(self) -> IronPython.Runtime.Types.PythonType:
        ...

    @property
    def SystemError(self) -> IronPython.Runtime.Types.PythonType:
        ...

    @property
    def TypeError(self) -> IronPython.Runtime.Types.PythonType:
        ...

    @property
    def ValueError(self) -> IronPython.Runtime.Types.PythonType:
        ...

    @property
    def UnicodeError(self) -> IronPython.Runtime.Types.PythonType:
        ...

    @property
    def UnicodeDecodeError(self) -> IronPython.Runtime.Types.PythonType:
        ...

    @property
    def UnicodeEncodeError(self) -> IronPython.Runtime.Types.PythonType:
        ...

    @property
    def UnicodeTranslateError(self) -> IronPython.Runtime.Types.PythonType:
        ...

    @property
    def Warning(self) -> IronPython.Runtime.Types.PythonType:
        ...

    @property
    def DeprecationWarning(self) -> IronPython.Runtime.Types.PythonType:
        ...

    @property
    def PendingDeprecationWarning(self) -> IronPython.Runtime.Types.PythonType:
        ...

    @property
    def RuntimeWarning(self) -> IronPython.Runtime.Types.PythonType:
        ...

    @property
    def SyntaxWarning(self) -> IronPython.Runtime.Types.PythonType:
        ...

    @property
    def UserWarning(self) -> IronPython.Runtime.Types.PythonType:
        ...

    @property
    def FutureWarning(self) -> IronPython.Runtime.Types.PythonType:
        ...

    @property
    def ImportWarning(self) -> IronPython.Runtime.Types.PythonType:
        ...

    @property
    def UnicodeWarning(self) -> IronPython.Runtime.Types.PythonType:
        ...

    @property
    def BytesWarning(self) -> IronPython.Runtime.Types.PythonType:
        ...

    @property
    def ResourceWarning(self) -> IronPython.Runtime.Types.PythonType:
        ...

    # methods
    @staticmethod
    def GetMaxKwArg(dict: System.Collections.Generic.IDictionary[str, System.Object], isDefaultAllowed: bool, ) -> System.Tuple[System.Object, System.Object]:
        ...

    @staticmethod
    @typing.overload
    def min(context: IronPython.Runtime.CodeContext, x: System.Object, ) -> System.Object:
        ...

    @staticmethod
    @typing.overload
    def min(context: IronPython.Runtime.CodeContext, x: System.Object, y: System.Object, ) -> System.Object:
        ...

    @staticmethod
    @typing.overload
    def min(context: IronPython.Runtime.CodeContext, args: System.Array[System.Object], ) -> System.Object:
        ...

    @staticmethod
    @typing.overload
    def min(context: IronPython.Runtime.CodeContext, x: System.Object, dict: System.Collections.Generic.IDictionary[str, System.Object], ) -> System.Object:
        ...

    @staticmethod
    @typing.overload
    def min(context: IronPython.Runtime.CodeContext, x: System.Object, y: System.Object, dict: System.Collections.Generic.IDictionary[str, System.Object], ) -> System.Object:
        ...

    @staticmethod
    @typing.overload
    def min(context: IronPython.Runtime.CodeContext, dict: System.Collections.Generic.IDictionary[str, System.Object], args: System.Array[System.Object], ) -> System.Object:
        ...

    @staticmethod
    def GetMinKwArg(dict: System.Collections.Generic.IDictionary[str, System.Object], isDefaultAllowed: bool, ) -> System.Tuple[System.Object, System.Object]:
        ...

    @staticmethod
    def VerifyKeys(name: str, dict: System.Collections.Generic.IDictionary[str, System.Object], ) -> System.Tuple[System.Object, System.Object]:
        ...

    @staticmethod
    @typing.overload
    def next(iter: System.Collections.IEnumerator, ) -> System.Object:
        ...

    @staticmethod
    @typing.overload
    def next(iter: System.Collections.IEnumerator, defaultVal: System.Object, ) -> System.Object:
        ...

    @staticmethod
    @typing.overload
    def next(gen: IronPython.Runtime.PythonGenerator, ) -> System.Object:
        ...

    @staticmethod
    @typing.overload
    def next(gen: IronPython.Runtime.PythonGenerator, defaultVal: System.Object, ) -> System.Object:
        ...

    @staticmethod
    @typing.overload
    def next(context: IronPython.Runtime.CodeContext, iter: System.Object, ) -> System.Object:
        ...

    @staticmethod
    @typing.overload
    def next(context: IronPython.Runtime.CodeContext, iter: System.Object, defaultVal: System.Object, ) -> System.Object:
        ...

    @staticmethod
    def oct(number: System.Object, ) -> str:
        ...

    @staticmethod
    @typing.overload
    def open(context: IronPython.Runtime.CodeContext, file: System.Object, mode: str = ..., buffering: int = ..., encoding: str = ..., errors: str = ..., newline: str = ..., closefd: bool = ..., opener: System.Object = ..., ) -> IronPython.Modules.PythonIOModule._IOBase:
        ...

    @staticmethod
    @typing.overload
    def open(context: IronPython.Runtime.CodeContext, stream: System.IO.Stream, ) -> IronPython.Modules.PythonIOModule.FileIO:
        ...

    @staticmethod
    def ord(value: System.Object, ) -> int:
        ...

    @staticmethod
    @typing.overload
    def pow(context: IronPython.Runtime.CodeContext, x: System.Object, y: System.Object, ) -> System.Object:
        ...

    @staticmethod
    @typing.overload
    def pow(context: IronPython.Runtime.CodeContext, x: System.Object, y: System.Object, z: System.Object, ) -> System.Object:
        ...

    @staticmethod
    @typing.overload
    def print(context: IronPython.Runtime.CodeContext, args: System.Array[System.Object], ) -> None:
        ...

    @staticmethod
    @typing.overload
    def print(context: IronPython.Runtime.CodeContext, kwargs: System.Collections.Generic.IDictionary[str, System.Object], args: System.Array[System.Object], ) -> None:
        ...

    @staticmethod
    def AttrCollectionPop(kwargs: System.Collections.Generic.IDictionary[str, System.Object], name: str, defaultValue: System.Object, ) -> System.Object:
        ...

    @staticmethod
    def PrintHelper(context: IronPython.Runtime.CodeContext, sep: str, end: str, file: System.Object, args: System.Array[System.Object], flush: bool, ) -> None:
        ...

    @staticmethod
    @typing.overload
    def input(context: IronPython.Runtime.CodeContext, ) -> str:
        ...

    @staticmethod
    @typing.overload
    def input(context: IronPython.Runtime.CodeContext, prompt: System.Object, ) -> str:
        ...

    @staticmethod
    def repr(context: IronPython.Runtime.CodeContext, o: System.Object, ) -> System.Object:
        ...

    @staticmethod
    @typing.overload
    def round(context: IronPython.Runtime.CodeContext, number: System.Object, ) -> System.Object:
        ...

    @staticmethod
    @typing.overload
    def round(context: IronPython.Runtime.CodeContext, number: System.Object, ndigits: System.Object, ) -> System.Object:
        ...

    @staticmethod
    def setattr(context: IronPython.Runtime.CodeContext, o: System.Object, name: str, val: System.Object, ) -> None:
        ...

    @staticmethod
    def sorted(context: IronPython.Runtime.CodeContext, iterable: System.Object, kwArgs: System.Collections.Generic.IDictionary[str, System.Object], ) -> IronPython.Runtime.PythonList:
        ...

    @staticmethod
    @typing.overload
    def sum(context: IronPython.Runtime.CodeContext, sequence: System.Object, ) -> System.Object:
        ...

    @staticmethod
    @typing.overload
    def sum(context: IronPython.Runtime.CodeContext, sequence: IronPython.Runtime.PythonList, ) -> System.Object:
        ...

    @staticmethod
    @typing.overload
    def sum(context: IronPython.Runtime.CodeContext, sequence: IronPython.Runtime.PythonTuple, ) -> System.Object:
        ...

    @staticmethod
    @typing.overload
    def sum(context: IronPython.Runtime.CodeContext, sequence: System.Object, start: System.Object, ) -> System.Object:
        ...

    @staticmethod
    @typing.overload
    def sum(context: IronPython.Runtime.CodeContext, sequence: IronPython.Runtime.PythonList, start: System.Object, ) -> System.Object:
        ...

    @staticmethod
    @typing.overload
    def sum(context: IronPython.Runtime.CodeContext, sequence: IronPython.Runtime.PythonTuple, start: System.Object, ) -> System.Object:
        ...

    @staticmethod
    def ValidateSumStart(start: System.Object, ) -> None:
        ...

    @staticmethod
    def SumOne(state: ref[IronPython.Modules.Builtin.SumState], current: System.Object, ) -> None:
        ...

    @staticmethod
    def SumBigIntAndDouble(state: ref[IronPython.Modules.Builtin.SumState], bigInt: System.Numerics.BigInteger, dbl: float, ) -> None:
        ...

    @staticmethod
    def SumObject(state: ref[IronPython.Modules.Builtin.SumState], value: System.Object, current: System.Object, ) -> None:
        ...

    @staticmethod
    @typing.overload
    def vars(context: IronPython.Runtime.CodeContext, ) -> System.Object:
        ...

    @staticmethod
    @typing.overload
    def vars(context: IronPython.Runtime.CodeContext, object: System.Object, ) -> System.Object:
        ...

    @staticmethod
    def GetRuntimeGeneratedCodeCompilerOptions(context: IronPython.Runtime.CodeContext, inheritContext: bool, cflags: int, ) -> IronPython.Compiler.PythonCompilerOptions:
        ...

    @staticmethod
    def GetCompilerInheritance(dontInherit: System.Object, ) -> bool:
        ...

    @staticmethod
    def GetCompilerFlags(flags: int, ) -> int:
        ...

    @staticmethod
    def GetExecEvalScopeOptional(context: IronPython.Runtime.CodeContext, globals: IronPython.Runtime.PythonDictionary, localsDict: System.Object, copyModule: bool, ) -> IronPython.Runtime.CodeContext:
        ...

    @staticmethod
    def GetExecEvalScope(context: IronPython.Runtime.CodeContext, globals: IronPython.Runtime.PythonDictionary, locals: IronPython.Runtime.PythonDictionary, copyModule: bool, setBuiltinsToModule: bool, ) -> IronPython.Runtime.CodeContext:
        ...

    @staticmethod
    def __import__(context: IronPython.Runtime.CodeContext, name: str, globals: System.Object = ..., locals: System.Object = ..., fromlist: System.Object = ..., level: int = ..., ) -> System.Object:
        ...

    @staticmethod
    def abs(context: IronPython.Runtime.CodeContext, o: System.Object, ) -> System.Object:
        ...

    @staticmethod
    def all(context: IronPython.Runtime.CodeContext, x: System.Object, ) -> bool:
        ...

    @staticmethod
    def any(context: IronPython.Runtime.CodeContext, x: System.Object, ) -> bool:
        ...

    @staticmethod
    def ascii(context: IronPython.Runtime.CodeContext, object: System.Object, ) -> str:
        ...

    @staticmethod
    def bin(number: System.Object, ) -> str:
        ...

    @staticmethod
    def callable(context: IronPython.Runtime.CodeContext, o: System.Object, ) -> bool:
        ...

    @staticmethod
    def chr(value: int, ) -> System.Object:
        ...

    @staticmethod
    @typing.overload
    def compile(context: IronPython.Runtime.CodeContext, source: IronPython.Modules._ast.AST, filename: str, mode: str, flags: System.Object = ..., dont_inherit: bool = ..., optimize: int = ..., ) -> System.Object:
        ...

    @staticmethod
    @typing.overload
    def compile(context: IronPython.Runtime.CodeContext, source: IronPython.Runtime.IBufferProtocol, filename: str, mode: str, flags: System.Object = ..., dont_inherit: bool = ..., optimize: int = ..., ) -> System.Object:
        ...

    @staticmethod
    @typing.overload
    def compile(context: IronPython.Runtime.CodeContext, source: str, filename: str, mode: str, flags: System.Object = ..., dont_inherit: bool = ..., optimize: int = ..., ) -> System.Object:
        ...

    @staticmethod
    def ValidateCompileMode(mode: str, ) -> int:
        ...

    @staticmethod
    def CompileHelper(context: IronPython.Runtime.CodeContext, sourceUnit: Microsoft.Scripting.SourceUnit, mode: str, flags: System.Object, dont_inherit: bool, ) -> System.Object:
        ...

    @staticmethod
    def delattr(context: IronPython.Runtime.CodeContext, o: System.Object, name: str, ) -> None:
        ...

    @staticmethod
    @typing.overload
    def dir(context: IronPython.Runtime.CodeContext, ) -> IronPython.Runtime.PythonList:
        ...

    @staticmethod
    @typing.overload
    def dir(context: IronPython.Runtime.CodeContext, o: System.Object, ) -> IronPython.Runtime.PythonList:
        ...

    @staticmethod
    def divmod(context: IronPython.Runtime.CodeContext, x: System.Object, y: System.Object, ) -> System.Object:
        ...

    @staticmethod
    def GetAttrLocals(context: IronPython.Runtime.CodeContext, locals: System.Object, ) -> IronPython.Runtime.PythonDictionary:
        ...

    @staticmethod
    @typing.overload
    def eval(context: IronPython.Runtime.CodeContext, code: IronPython.Runtime.FunctionCode, globals: IronPython.Runtime.PythonDictionary = ..., locals: System.Object = ..., ) -> System.Object:
        ...

    @staticmethod
    @typing.overload
    def eval(context: IronPython.Runtime.CodeContext, expression: IronPython.Runtime.IBufferProtocol, globals: IronPython.Runtime.PythonDictionary = ..., locals: System.Object = ..., ) -> System.Object:
        ...

    @staticmethod
    @typing.overload
    def eval(context: IronPython.Runtime.CodeContext, expression: str, globals: IronPython.Runtime.PythonDictionary = ..., locals: System.Object = ..., ) -> System.Object:
        ...

    @staticmethod
    @typing.overload
    def exec(context: IronPython.Runtime.CodeContext, code: IronPython.Runtime.FunctionCode, globals: IronPython.Runtime.PythonDictionary = ..., locals: System.Object = ..., ) -> None:
        ...

    @staticmethod
    @typing.overload
    def exec(context: IronPython.Runtime.CodeContext, code: str, globals: IronPython.Runtime.PythonDictionary = ..., locals: System.Object = ..., ) -> None:
        ...

    @staticmethod
    @typing.overload
    def exec(context: IronPython.Runtime.CodeContext, code: IronPython.Runtime.IBufferProtocol, globals: IronPython.Runtime.PythonDictionary = ..., locals: System.Object = ..., ) -> None:
        ...

    @staticmethod
    def format(context: IronPython.Runtime.CodeContext, argValue: System.Object, formatSpec: str = ..., ) -> str:
        ...

    @staticmethod
    @typing.overload
    def getattr(context: IronPython.Runtime.CodeContext, o: System.Object, name: str, ) -> System.Object:
        ...

    @staticmethod
    @typing.overload
    def getattr(context: IronPython.Runtime.CodeContext, o: System.Object, name: str, def: System.Object, ) -> System.Object:
        ...

    @staticmethod
    def globals(context: IronPython.Runtime.CodeContext, ) -> IronPython.Runtime.PythonDictionary:
        ...

    @staticmethod
    def hasattr(context: IronPython.Runtime.CodeContext, o: System.Object, name: str, ) -> bool:
        ...

    @staticmethod
    @typing.overload
    def hash(context: IronPython.Runtime.CodeContext, o: System.Object, ) -> int:
        ...

    @staticmethod
    @typing.overload
    def hash(context: IronPython.Runtime.CodeContext, o: IronPython.Runtime.PythonTuple, ) -> int:
        ...

    @staticmethod
    @typing.overload
    def hash(context: IronPython.Runtime.CodeContext, o: str, ) -> int:
        ...

    @staticmethod
    @typing.overload
    def hash(context: IronPython.Runtime.CodeContext, o: int, ) -> int:
        ...

    @staticmethod
    @typing.overload
    def hash(context: IronPython.Runtime.CodeContext, o: str, ) -> int:
        ...

    @staticmethod
    @typing.overload
    def hash(context: IronPython.Runtime.CodeContext, o: IronPython.Runtime.Operations.ExtensibleString, ) -> int:
        ...

    @staticmethod
    @typing.overload
    def hash(context: IronPython.Runtime.CodeContext, o: System.Numerics.BigInteger, ) -> int:
        ...

    @staticmethod
    @typing.overload
    def hash(context: IronPython.Runtime.CodeContext, o: Microsoft.Scripting.Runtime.Extensible[System.Numerics.BigInteger], ) -> int:
        ...

    @staticmethod
    @typing.overload
    def hash(context: IronPython.Runtime.CodeContext, o: float, ) -> int:
        ...

    @staticmethod
    @typing.overload
    def help(context: IronPython.Runtime.CodeContext, o: System.Object, ) -> None:
        ...

    @staticmethod
    @typing.overload
    def help(context: IronPython.Runtime.CodeContext, doced: System.Collections.Generic.List[System.Object], doc: System.Text.StringBuilder, indent: int, obj: System.Object, ) -> None:
        ...

    @staticmethod
    def AppendMultiLine(doc: System.Text.StringBuilder, multiline: str, indent: int, ) -> None:
        ...

    @staticmethod
    def AppendIndent(doc: System.Text.StringBuilder, indent: int, ) -> None:
        ...

    @staticmethod
    def hex(number: System.Object, ) -> str:
        ...

    @staticmethod
    def id(o: System.Object, ) -> System.Object:
        ...

    @staticmethod
    @typing.overload
    def isinstance(o: System.Object, typeinfo: IronPython.Runtime.Types.PythonType, ) -> bool:
        ...

    @staticmethod
    @typing.overload
    def isinstance(context: IronPython.Runtime.CodeContext, o: System.Object, typeinfo: IronPython.Runtime.PythonTuple, ) -> bool:
        ...

    @staticmethod
    @typing.overload
    def isinstance(context: IronPython.Runtime.CodeContext, o: System.Object, typeinfo: System.Object, ) -> bool:
        ...

    @staticmethod
    @typing.overload
    def issubclass(context: IronPython.Runtime.CodeContext, c: IronPython.Runtime.Types.PythonType, typeinfo: System.Object, ) -> bool:
        ...

    @staticmethod
    @typing.overload
    def issubclass(context: IronPython.Runtime.CodeContext, c: IronPython.Runtime.Types.PythonType, typeinfo: IronPython.Runtime.Types.PythonType, ) -> bool:
        ...

    @staticmethod
    @typing.overload
    def issubclass(context: IronPython.Runtime.CodeContext, o: System.Object, typeinfo: System.Object, ) -> System.Object:
        ...

    @staticmethod
    @typing.overload
    def iter(context: IronPython.Runtime.CodeContext, o: System.Object, ) -> System.Object:
        ...

    @staticmethod
    @typing.overload
    def iter(context: IronPython.Runtime.CodeContext, func: System.Object, sentinel: System.Object, ) -> System.Object:
        ...

    @staticmethod
    @typing.overload
    def len(str: str, ) -> int:
        ...

    @staticmethod
    @typing.overload
    def len(str: IronPython.Runtime.Operations.ExtensibleString, ) -> int:
        ...

    @staticmethod
    @typing.overload
    def len(list: IronPython.Runtime.PythonList, ) -> int:
        ...

    @staticmethod
    @typing.overload
    def len(tuple: IronPython.Runtime.PythonTuple, ) -> int:
        ...

    @staticmethod
    @typing.overload
    def len(dict: IronPython.Runtime.PythonDictionary, ) -> int:
        ...

    @staticmethod
    @typing.overload
    def len(collection: System.Collections.ICollection, ) -> int:
        ...

    @staticmethod
    @typing.overload
    def len(o: System.Object, ) -> System.Object:
        ...

    @staticmethod
    def locals(context: IronPython.Runtime.CodeContext, ) -> System.Object:
        ...

    @staticmethod
    @typing.overload
    def max(context: IronPython.Runtime.CodeContext, x: System.Object, ) -> System.Object:
        ...

    @staticmethod
    @typing.overload
    def max(context: IronPython.Runtime.CodeContext, x: System.Object, y: System.Object, ) -> System.Object:
        ...

    @staticmethod
    @typing.overload
    def max(context: IronPython.Runtime.CodeContext, args: System.Array[System.Object], ) -> System.Object:
        ...

    @staticmethod
    @typing.overload
    def max(context: IronPython.Runtime.CodeContext, x: System.Object, dict: System.Collections.Generic.IDictionary[str, System.Object], ) -> System.Object:
        ...

    @staticmethod
    @typing.overload
    def max(context: IronPython.Runtime.CodeContext, x: System.Object, y: System.Object, dict: System.Collections.Generic.IDictionary[str, System.Object], ) -> System.Object:
        ...

    @staticmethod
    @typing.overload
    def max(context: IronPython.Runtime.CodeContext, dict: System.Collections.Generic.IDictionary[str, System.Object], args: System.Array[System.Object], ) -> System.Object:
        ...

class PythonImport(System.Object, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields
    __doc__: str = ...
    PythonSource: int = ...
    PythonCompiled: int = ...
    CExtension: int = ...
    PythonResource: int = ...
    PackageDirectory: int = ...
    CBuiltin: int = ...
    PythonFrozen: int = ...
    PythonCodeResource: int = ...
    SearchError: int = ...
    ImporterHook: int = ...

    # properties
    # methods
    @staticmethod
    def extension_suffixes() -> IronPython.Runtime.PythonList:
        ...

    @staticmethod
    def lock_held(context: IronPython.Runtime.CodeContext, ) -> bool:
        ...

    @staticmethod
    def acquire_lock(context: IronPython.Runtime.CodeContext, ) -> None:
        ...

    @staticmethod
    def release_lock(context: IronPython.Runtime.CodeContext, ) -> None:
        ...

    @staticmethod
    def init_builtin(context: IronPython.Runtime.CodeContext, name: str, ) -> System.Object:
        ...

    @staticmethod
    def init_frozen(name: str, ) -> System.Object:
        ...

    @staticmethod
    def get_frozen_object(name: str, ) -> System.Object:
        ...

    @staticmethod
    def is_builtin(context: IronPython.Runtime.CodeContext, name: str, ) -> int:
        ...

    @staticmethod
    def is_frozen(name: str, ) -> bool:
        ...

    @staticmethod
    def is_frozen_package(name: str, ) -> bool:
        ...

    @staticmethod
    def _fix_co_filename() -> None:
        ...

    @staticmethod
    def GetLockCount(context: IronPython.Runtime.CodeContext, ) -> int:
        ...

    @staticmethod
    def SetLockCount(context: IronPython.Runtime.CodeContext, lockCount: int, ) -> None:
        ...

class SysModule(System.Object, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields
    byteorder: str = ...
    displayhook: IronPython.Runtime.Types.BuiltinFunction = ...
    __displayhook__: IronPython.Runtime.Types.BuiltinFunction = ...
    excepthook: IronPython.Runtime.Types.BuiltinFunction = ...
    __excepthook__: IronPython.Runtime.Types.BuiltinFunction = ...
    prefix: str = ...
    abiflags: str = ...
    _git: IronPython.Runtime.PythonTuple = ...
    winver: str = ...
    int_info: IronPython.Modules.SysModule.intinfo = ...
    float_repr_style: str = ...
    float_info: IronPython.Modules.SysModule.floatinfo = ...
    hash_info: IronPython.Modules.SysModule.hashinfo = ...
    __doc__: str = ...
    api_version: int = ...
    copyright: str = ...
    dllhandle: int = ...
    maxsize: int = ...
    maxunicode: int = ...

    # properties
    # methods
    @staticmethod
    def GetPrefix() -> str:
        ...

    @staticmethod
    def callstats() -> System.Object:
        ...

    @staticmethod
    def displayhookImpl(context: IronPython.Runtime.CodeContext, value: System.Object, ) -> None:
        ...

    @staticmethod
    def excepthookImpl(context: IronPython.Runtime.CodeContext, exctype: System.Object, value: System.Object, traceback: System.Object, ) -> None:
        ...

    @staticmethod
    def getcheckinterval() -> int:
        ...

    @staticmethod
    def setcheckinterval(value: int, ) -> None:
        ...

    @staticmethod
    def exc_info(context: IronPython.Runtime.CodeContext, ) -> IronPython.Runtime.PythonTuple:
        ...

    @staticmethod
    def intern(o: System.Object, ) -> str:
        ...

    @staticmethod
    @typing.overload
    def exit() -> None:
        ...

    @staticmethod
    @typing.overload
    def exit(code: System.Object, ) -> None:
        ...

    @staticmethod
    def getdefaultencoding(context: IronPython.Runtime.CodeContext, ) -> str:
        ...

    @staticmethod
    def getfilesystemencoding() -> str:
        ...

    @staticmethod
    @typing.overload
    def _getframeImpl(context: IronPython.Runtime.CodeContext, ) -> IronPython.Runtime.Exceptions.TraceBackFrame:
        ...

    @staticmethod
    @typing.overload
    def _getframeImpl(context: IronPython.Runtime.CodeContext, depth: int, ) -> IronPython.Runtime.Exceptions.TraceBackFrame:
        ...

    @staticmethod
    @typing.overload
    def _getframeImpl(context: IronPython.Runtime.CodeContext, depth: int, stack: System.Collections.Generic.List[IronPython.Runtime.Operations.FunctionStack], ) -> IronPython.Runtime.Exceptions.TraceBackFrame:
        ...

    @staticmethod
    def getsizeof(o: System.Object, ) -> int:
        ...

    @staticmethod
    def getwindowsversion() -> IronPython.Runtime.PythonTuple:
        ...

    @staticmethod
    def settrace(context: IronPython.Runtime.CodeContext, o: System.Object, ) -> None:
        ...

    @staticmethod
    def call_tracing(context: IronPython.Runtime.CodeContext, func: System.Object, args: IronPython.Runtime.PythonTuple, ) -> System.Object:
        ...

    @staticmethod
    def gettrace(context: IronPython.Runtime.CodeContext, ) -> System.Object:
        ...

    @staticmethod
    def setrecursionlimit(context: IronPython.Runtime.CodeContext, limit: int, ) -> None:
        ...

    @staticmethod
    def getrecursionlimit(context: IronPython.Runtime.CodeContext, ) -> int:
        ...

    @staticmethod
    def PublishBuiltinModuleNames(context: IronPython.Runtime.PythonContext, dict: IronPython.Runtime.PythonDictionary, ) -> None:
        ...

class PythonIOModule(System.Object, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields
    DEFAULT_BUFFER_SIZE: int = ...

    # properties
    @property
    def BlockingIOError(self) -> IronPython.Runtime.Types.PythonType:
        ...

    # methods
    @staticmethod
    def open(context: IronPython.Runtime.CodeContext, file: System.Object, mode: str = ..., buffering: int = ..., encoding: str = ..., errors: str = ..., newline: str = ..., closefd: bool = ..., opener: System.Object = ..., ) -> IronPython.Modules.PythonIOModule._IOBase:
        ...

    @staticmethod
    def CreateConsole(context: IronPython.Runtime.PythonContext, io: Microsoft.Scripting.Runtime.SharedIO, type: int, name: str, fio: ref[IronPython.Modules.PythonIOModule.FileIO], ) -> IronPython.Modules.PythonIOModule.TextIOWrapper:
        ...

    @staticmethod
    def MakeSet(chars: str, ) -> System.Collections.Generic.HashSet[str]:
        ...

    @staticmethod
    def GetBigInt(i: System.Object, msg: str, ) -> System.Numerics.BigInteger:
        ...

    @staticmethod
    def TryGetBigInt(i: System.Object, res: ref[System.Numerics.BigInteger], ) -> bool:
        ...

    @staticmethod
    @typing.overload
    def GetInt(i: System.Object, ) -> int:
        ...

    @staticmethod
    @typing.overload
    def GetInt(i: System.Object, defaultValue: int, ) -> int:
        ...

    @staticmethod
    @typing.overload
    def GetInt(i: System.Object, msg: str, args: System.Array[System.Object], ) -> int:
        ...

    @staticmethod
    @typing.overload
    def GetInt(i: System.Object, defaultValue: int, msg: str, args: System.Array[System.Object], ) -> int:
        ...

    @staticmethod
    def TryGetInt(i: System.Object, value: ref[int], ) -> bool:
        ...

    @staticmethod
    def GetBytes(o: System.Object, name: str, ) -> IronPython.Runtime.Bytes:
        ...

class _ast(System.Object, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields
    _containsYield: bool = ...
    __version__: str = ...
    PyCF_ONLY_AST: int = ...

    # properties
    @property
    def arg(self) -> IronPython.Runtime.Types.PythonType:
        ...

    # methods
    @staticmethod
    def ConvertToPythonAst(codeContext: IronPython.Runtime.CodeContext, source: IronPython.Modules._ast.AST, filename: str, ) -> IronPython.Compiler.Ast.PythonAst:
        ...

    @staticmethod
    def BuildAst(context: IronPython.Runtime.CodeContext, sourceUnit: Microsoft.Scripting.SourceUnit, opts: IronPython.Compiler.PythonCompilerOptions, mode: str, ) -> IronPython.Modules._ast.AST:
        ...

    @staticmethod
    @typing.overload
    def ConvertToAST(pythonAst: IronPython.Compiler.Ast.PythonAst, kind: str, ) -> IronPython.Modules._ast.mod:
        ...

    @staticmethod
    @typing.overload
    def ConvertToAST(suite: IronPython.Compiler.Ast.SuiteStatement, kind: str, ) -> IronPython.Modules._ast.mod:
        ...

class PythonLocale(System.Object, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields
    __doc__: str = ...
    CHAR_MAX: int = ...
    LC_ALL: int = ...
    LC_COLLATE: int = ...
    LC_CTYPE: int = ...
    LC_MONETARY: int = ...
    LC_NUMERIC: int = ...
    LC_TIME: int = ...

    # properties
    @property
    def PreferredEncoding(self) -> str:
        ...

    # methods
    @staticmethod
    def EnsureLocaleInitialized(context: IronPython.Runtime.PythonContext, ) -> None:
        ...

    @staticmethod
    def _getdefaultlocale() -> System.Object:
        ...

    @staticmethod
    def localeconv(context: IronPython.Runtime.CodeContext, ) -> System.Object:
        ...

    @staticmethod
    def setlocale(context: IronPython.Runtime.CodeContext, category: int, locale: str = ..., ) -> System.Object:
        ...

    @staticmethod
    def strcoll(context: IronPython.Runtime.CodeContext, string1: str, string2: str, ) -> int:
        ...

    @staticmethod
    def strxfrm(context: IronPython.Runtime.CodeContext, string: str, ) -> System.Object:
        ...

    @staticmethod
    def GetDefaultLocale() -> str:
        ...

    @staticmethod
    def GetLocaleInfo(context: IronPython.Runtime.CodeContext, ) -> IronPython.Modules.PythonLocale.LocaleInfo:
        ...

    @staticmethod
    def _localeerror(context: IronPython.Runtime.CodeContext, ) -> IronPython.Runtime.Types.PythonType:
        ...

