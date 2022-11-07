from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import System
import System.Collections.Generic
import System.Collections
import IronPython.Runtime
import System.Dynamic
import IronPython.Runtime.Binding
import IronPython.Modules.PythonIOModule
import System.Numerics
import System.Linq.Expressions
import System.IO
import Microsoft.Scripting


class _RawIOBase(System.IDisposable, System.Collections.Generic.IEnumerator[System.Object], System.Collections.IEnumerator, System.Collections.Generic.IEnumerable[System.Object], System.Collections.IEnumerable, IronPython.Runtime.IWeakReferenceable, System.Dynamic.IDynamicMetaObjectProvider, IronPython.Runtime.Binding.IPythonExpandable, IronPython.Modules.PythonIOModule._IOBase):
    @typing.overload
    def __init__(self, **kwargs):
        self.context: IronPython.Runtime.CodeContext
        ...

    # static fields

    # properties
    @property
    def closed(self) -> bool:
        ...

    @property
    def __dict__(self) -> IronPython.Runtime.PythonDictionary:
        ...

    # methods
    def __init__(self, context: IronPython.Runtime.CodeContext, ):
        ...

    def read(self, context: IronPython.Runtime.CodeContext, size: System.Object = ..., ) -> System.Object:
        ...

    def readall(self, context: IronPython.Runtime.CodeContext, ) -> IronPython.Runtime.Bytes:
        ...

    def readinto(self, context: IronPython.Runtime.CodeContext, buf: System.Object, ) -> System.Numerics.BigInteger:
        ...

    def write(self, context: IronPython.Runtime.CodeContext, buf: System.Object, ) -> System.Numerics.BigInteger:
        ...

    def GetMetaObject(self, parameter: System.Linq.Expressions.Expression, ) -> System.Dynamic.DynamicMetaObject:
        ...

class FileIO(System.IDisposable, System.Collections.Generic.IEnumerator[System.Object], System.Collections.IEnumerator, System.Collections.Generic.IEnumerable[System.Object], System.Collections.IEnumerable, IronPython.Runtime.IWeakReferenceable, System.Dynamic.IDynamicMetaObjectProvider, IronPython.Runtime.Binding.IPythonExpandable, IronPython.Runtime.ICodeFormattable, IronPython.Modules.PythonIOModule._RawIOBase):
    @typing.overload
    def __init__(self, **kwargs):
        self._readStream: System.IO.Stream
        self.name: System.Object
        self.context: IronPython.Runtime.CodeContext
        ...

    # static fields

    # properties
    @property
    def IsConsole(self) -> bool:
        ...

    @property
    def closed(self) -> bool:
        ...

    @property
    def closefd(self) -> bool:
        ...

    @property
    def mode(self) -> str:
        ...

    @property
    def __dict__(self) -> IronPython.Runtime.PythonDictionary:
        ...

    # methods
    @typing.overload
    def __init__(self, context: IronPython.Runtime.CodeContext, stream: System.IO.Stream, ):
        ...

    @typing.overload
    def __init__(self, context: IronPython.Runtime.CodeContext, stream: System.IO.Stream, consoleStreamType: int, ):
        ...

    @typing.overload
    def __init__(self, context: IronPython.Runtime.CodeContext, fd: int, mode: str = ..., closefd: bool = ..., opener: System.Object = ..., ):
        ...

    @typing.overload
    def __init__(self, context: IronPython.Runtime.CodeContext, name: str, mode: str = ..., closefd: bool = ..., opener: System.Object = ..., ):
        ...

    @staticmethod
    def NormalizeMode(mode: str, flags: ref[int], ) -> str:
        ...

    def close(self, context: IronPython.Runtime.CodeContext, ) -> None:
        ...

    def fileno(self, context: IronPython.Runtime.CodeContext, ) -> int:
        ...

    def flush(self, context: IronPython.Runtime.CodeContext, ) -> None:
        ...

    def isatty(self, context: IronPython.Runtime.CodeContext, ) -> bool:
        ...

    def isRedirected(self, ) -> bool:
        ...

    def read(self, context: IronPython.Runtime.CodeContext, size: System.Object = ..., ) -> System.Object:
        ...

    def readable(self, context: IronPython.Runtime.CodeContext, ) -> bool:
        ...

    def readall(self, ) -> IronPython.Runtime.Bytes:
        ...

    @typing.overload
    def readinto(self, buffer: IronPython.Runtime.IBufferProtocol, ) -> System.Numerics.BigInteger:
        ...

    @typing.overload
    def readinto(self, context: IronPython.Runtime.CodeContext, buf: System.Object, ) -> System.Numerics.BigInteger:
        ...

    @typing.overload
    def seek(self, context: IronPython.Runtime.CodeContext, offset: System.Numerics.BigInteger, whence: System.Object, ) -> System.Numerics.BigInteger:
        ...

    @typing.overload
    def seek(self, offset: float, whence: System.Object, ) -> System.Numerics.BigInteger:
        ...

    def seekable(self, context: IronPython.Runtime.CodeContext, ) -> bool:
        ...

    def tell(self, context: IronPython.Runtime.CodeContext, ) -> System.Numerics.BigInteger:
        ...

    @typing.overload
    def truncate(self, size: System.Numerics.BigInteger, ) -> System.Numerics.BigInteger:
        ...

    @typing.overload
    def truncate(self, size: float, ) -> System.Numerics.BigInteger:
        ...

    @typing.overload
    def truncate(self, context: IronPython.Runtime.CodeContext, pos: System.Object = ..., ) -> System.Numerics.BigInteger:
        ...

    def writable(self, context: IronPython.Runtime.CodeContext, ) -> bool:
        ...

    def write(self, context: IronPython.Runtime.CodeContext, b: System.Object, ) -> System.Numerics.BigInteger:
        ...

    def __repr__(self, context: IronPython.Runtime.CodeContext, ) -> str:
        ...

    def Dispose(self, ) -> None:
        ...

    def GetWeakRef(self, ) -> IronPython.Runtime.WeakRefTracker:
        ...

    def SetWeakRef(self, value: IronPython.Runtime.WeakRefTracker, ) -> bool:
        ...

    def SetFinalizer(self, value: IronPython.Runtime.WeakRefTracker, ) -> None:
        ...

    def GetMetaObject(self, parameter: System.Linq.Expressions.Expression, ) -> System.Dynamic.DynamicMetaObject:
        ...

    @staticmethod
    def AddFilename(context: IronPython.Runtime.CodeContext, name: str, ioe: System.Exception, ) -> None:
        ...

    @staticmethod
    def OpenFile(context: IronPython.Runtime.CodeContext, pal: Microsoft.Scripting.PlatformAdaptationLayer, name: str, fileMode: int, fileAccess: int, fileShare: int, ) -> System.IO.Stream:
        ...

    def EnsureReadable(self, ) -> None:
        ...

    def EnsureWritable(self, ) -> None:
        ...

    def SeekToEnd(self, ) -> None:
        ...

class BufferedWriter(System.IDisposable, System.Collections.Generic.IEnumerator[System.Object], System.Collections.IEnumerator, System.Collections.Generic.IEnumerable[System.Object], System.Collections.IEnumerable, IronPython.Runtime.IWeakReferenceable, System.Dynamic.IDynamicMetaObjectProvider, IronPython.Runtime.Binding.IPythonExpandable, IronPython.Modules.PythonIOModule._BufferedIOBase):
    @typing.overload
    def __init__(self, **kwargs):
        self.context: IronPython.Runtime.CodeContext
        ...

    # static fields

    # properties
    @property
    def raw(self) -> System.Object:
        ...
    @raw.setter
    def raw(self, val: System.Object):
        ...

    @property
    def closed(self) -> bool:
        ...

    @property
    def name(self) -> System.Object:
        ...

    @property
    def mode(self) -> System.Object:
        ...

    @property
    def __dict__(self) -> IronPython.Runtime.PythonDictionary:
        ...

    # methods
    def __init__(self, context: IronPython.Runtime.CodeContext, raw: System.Object, buffer_size: int = ..., max_buffer_size: System.Object = ..., ):
        ...

    @staticmethod
    def Create(context: IronPython.Runtime.CodeContext, raw: System.Object, buffer_size: int = ..., max_buffer_size: System.Object = ..., ) -> IronPython.Modules.PythonIOModule.BufferedWriter:
        ...

    def __init__(self, context: IronPython.Runtime.CodeContext, raw: System.Object, buffer_size: int = ..., max_buffer_size: System.Object = ..., ) -> None:
        ...

    def close(self, context: IronPython.Runtime.CodeContext, ) -> None:
        ...

    def detach(self, context: IronPython.Runtime.CodeContext, ) -> System.Object:
        ...

    def seekable(self, context: IronPython.Runtime.CodeContext, ) -> bool:
        ...

    def readable(self, context: IronPython.Runtime.CodeContext, ) -> bool:
        ...

    def writable(self, context: IronPython.Runtime.CodeContext, ) -> bool:
        ...

    def fileno(self, context: IronPython.Runtime.CodeContext, ) -> int:
        ...

    def isatty(self, context: IronPython.Runtime.CodeContext, ) -> bool:
        ...

    def write(self, context: IronPython.Runtime.CodeContext, buf: System.Object, ) -> System.Numerics.BigInteger:
        ...

    def truncate(self, context: IronPython.Runtime.CodeContext, pos: System.Object = ..., ) -> System.Numerics.BigInteger:
        ...

    def flush(self, context: IronPython.Runtime.CodeContext, ) -> None:
        ...

    def FlushNoLock(self, context: IronPython.Runtime.CodeContext, ) -> None:
        ...

    def tell(self, context: IronPython.Runtime.CodeContext, ) -> System.Numerics.BigInteger:
        ...

    @typing.overload
    def seek(self, offset: float, whence: System.Object, ) -> System.Numerics.BigInteger:
        ...

    @typing.overload
    def seek(self, context: IronPython.Runtime.CodeContext, pos: System.Numerics.BigInteger, whence: System.Object, ) -> System.Numerics.BigInteger:
        ...

    def __repr__(self, context: IronPython.Runtime.CodeContext, ) -> str:
        ...

    def GetMetaObject(self, parameter: System.Linq.Expressions.Expression, ) -> System.Dynamic.DynamicMetaObject:
        ...

class StringIO(System.IDisposable, System.Collections.Generic.IEnumerator[System.Object], System.Collections.IEnumerator, System.Collections.Generic.IEnumerable[System.Object], System.Collections.IEnumerable, IronPython.Runtime.IWeakReferenceable, System.Dynamic.IDynamicMetaObjectProvider, IronPython.Runtime.Binding.IPythonExpandable, IronPython.Modules.PythonIOModule._TextIOBase):
    @typing.overload
    def __init__(self, **kwargs):
        self.context: IronPython.Runtime.CodeContext
        ...

    # static fields

    # properties
    @property
    def line_buffering(self) -> bool:
        ...

    @property
    def newlines(self) -> System.Object:
        ...

    @property
    def encoding(self) -> str:
        ...

    @property
    def errors(self) -> str:
        ...

    @property
    def closed(self) -> bool:
        ...

    @property
    def __dict__(self) -> IronPython.Runtime.PythonDictionary:
        ...

    # methods
    @typing.overload
    def __init__(self, context: IronPython.Runtime.CodeContext, ):
        ...

    @typing.overload
    def __init__(self, context: IronPython.Runtime.CodeContext, kwArgsø: System.Collections.Generic.IDictionary[System.Object, System.Object], args: System.Array[System.Object], ):
        ...

    def __init__(self, context: IronPython.Runtime.CodeContext, initial_value: str = ..., newline: str = ..., ) -> None:
        ...

    def getvalue(self, ) -> str:
        ...

    def read(self, context: IronPython.Runtime.CodeContext, size: System.Object = ..., ) -> System.Object:
        ...

    def readable(self, context: IronPython.Runtime.CodeContext, ) -> bool:
        ...

    @typing.overload
    def readline(self, context: IronPython.Runtime.CodeContext, limit: int = ..., ) -> System.Object:
        ...

    @typing.overload
    def readline(self, limit: int, ) -> str:
        ...

    def readlines(self, hint: System.Object = ..., ) -> IronPython.Runtime.PythonList:
        ...

    @typing.overload
    def seek(self, pos: int, whence: int, ) -> System.Numerics.BigInteger:
        ...

    @typing.overload
    def seek(self, context: IronPython.Runtime.CodeContext, pos: System.Numerics.BigInteger, whence: System.Object, ) -> System.Numerics.BigInteger:
        ...

    def seekable(self, context: IronPython.Runtime.CodeContext, ) -> bool:
        ...

    def tell(self, context: IronPython.Runtime.CodeContext, ) -> System.Numerics.BigInteger:
        ...

    @typing.overload
    def truncate(self, ) -> System.Numerics.BigInteger:
        ...

    @typing.overload
    def truncate(self, size: int, ) -> System.Numerics.BigInteger:
        ...

    @typing.overload
    def truncate(self, context: IronPython.Runtime.CodeContext, size: System.Object = ..., ) -> System.Numerics.BigInteger:
        ...

    def writable(self, context: IronPython.Runtime.CodeContext, ) -> bool:
        ...

    @typing.overload
    def write(self, context: IronPython.Runtime.CodeContext, str: System.Object, ) -> System.Numerics.BigInteger:
        ...

    @typing.overload
    def write(self, context: IronPython.Runtime.CodeContext, str: str, ) -> System.Numerics.BigInteger:
        ...

    def writelines(self, context: IronPython.Runtime.CodeContext, lines: System.Collections.IEnumerable, ) -> None:
        ...

    def __getstate__(self, context: IronPython.Runtime.CodeContext, ) -> IronPython.Runtime.PythonTuple:
        ...

    def __setstate__(self, context: IronPython.Runtime.CodeContext, tuple: IronPython.Runtime.PythonTuple, ) -> None:
        ...

    def GetMetaObject(self, parameter: System.Linq.Expressions.Expression, ) -> System.Dynamic.DynamicMetaObject:
        ...

    @staticmethod
    def CheckNewline(context: IronPython.Runtime.CodeContext, newline: str, ) -> None:
        ...

    def DoWrite(self, str: str, ) -> int:
        ...

    def EnsureSize(self, size: int, ) -> None:
        ...

    def EnsureSizeSetLength(self, size: int, ) -> None:
        ...

class BufferedReader(System.IDisposable, System.Collections.Generic.IEnumerator[System.Object], System.Collections.IEnumerator, System.Collections.Generic.IEnumerable[System.Object], System.Collections.IEnumerable, IronPython.Runtime.IWeakReferenceable, System.Dynamic.IDynamicMetaObjectProvider, IronPython.Runtime.Binding.IPythonExpandable, IronPython.Modules.PythonIOModule._BufferedIOBase):
    @typing.overload
    def __init__(self, **kwargs):
        self.context: IronPython.Runtime.CodeContext
        ...

    # static fields

    # properties
    @property
    def raw(self) -> System.Object:
        ...
    @raw.setter
    def raw(self, val: System.Object):
        ...

    @property
    def closed(self) -> bool:
        ...

    @property
    def name(self) -> System.Object:
        ...

    @property
    def mode(self) -> System.Object:
        ...

    @property
    def __dict__(self) -> IronPython.Runtime.PythonDictionary:
        ...

    # methods
    def __init__(self, context: IronPython.Runtime.CodeContext, args: System.Array[System.Object], ):
        ...

    @staticmethod
    def Create(context: IronPython.Runtime.CodeContext, raw: System.Object, buffer_size: int = ..., ) -> IronPython.Modules.PythonIOModule.BufferedReader:
        ...

    def __init__(self, context: IronPython.Runtime.CodeContext, raw: System.Object, buffer_size: int = ..., ) -> None:
        ...

    def truncate(self, context: IronPython.Runtime.CodeContext, pos: System.Object = ..., ) -> System.Numerics.BigInteger:
        ...

    def close(self, context: IronPython.Runtime.CodeContext, ) -> None:
        ...

    def detach(self, context: IronPython.Runtime.CodeContext, ) -> System.Object:
        ...

    def seekable(self, context: IronPython.Runtime.CodeContext, ) -> bool:
        ...

    def readable(self, context: IronPython.Runtime.CodeContext, ) -> bool:
        ...

    def writable(self, context: IronPython.Runtime.CodeContext, ) -> bool:
        ...

    def fileno(self, context: IronPython.Runtime.CodeContext, ) -> int:
        ...

    def isatty(self, context: IronPython.Runtime.CodeContext, ) -> bool:
        ...

    def read(self, context: IronPython.Runtime.CodeContext, length: System.Object = ..., ) -> System.Object:
        ...

    def ReadNoLock(self, context: IronPython.Runtime.CodeContext, length: int, read1: bool = ..., ) -> IronPython.Runtime.Bytes:
        ...

    def peek(self, context: IronPython.Runtime.CodeContext, length: int = ..., ) -> IronPython.Runtime.Bytes:
        ...

    def PeekNoLock(self, context: IronPython.Runtime.CodeContext, length: int, ) -> IronPython.Runtime.Bytes:
        ...

    def read1(self, context: IronPython.Runtime.CodeContext, length: int = ..., ) -> IronPython.Runtime.Bytes:
        ...

    def readline(self, context: IronPython.Runtime.CodeContext, limit: int, ) -> System.Object:
        ...

    def tell(self, context: IronPython.Runtime.CodeContext, ) -> System.Numerics.BigInteger:
        ...

    @typing.overload
    def seek(self, offset: float, whence: System.Object, ) -> System.Numerics.BigInteger:
        ...

    @typing.overload
    def seek(self, context: IronPython.Runtime.CodeContext, pos: System.Numerics.BigInteger, whence: System.Object, ) -> System.Numerics.BigInteger:
        ...

    def __repr__(self, context: IronPython.Runtime.CodeContext, ) -> str:
        ...

    def GetMetaObject(self, parameter: System.Linq.Expressions.Expression, ) -> System.Dynamic.DynamicMetaObject:
        ...

    def ResetReadBuf(self, ) -> IronPython.Runtime.Bytes:
        ...

class BytesIO(System.IDisposable, System.Collections.Generic.IEnumerator[System.Object], System.Collections.IEnumerator, System.Collections.Generic.IEnumerable[System.Object], System.Collections.IEnumerable, IronPython.Runtime.IWeakReferenceable, System.Dynamic.IDynamicMetaObjectProvider, IronPython.Runtime.Binding.IPythonExpandable, IronPython.Modules.PythonIOModule._BufferedIOBase):
    @typing.overload
    def __init__(self, **kwargs):
        self.context: IronPython.Runtime.CodeContext
        ...

    # static fields

    # properties
    @property
    def closed(self) -> bool:
        ...

    @property
    def Current(self) -> System.Object:
        ...

    @property
    def __dict__(self) -> IronPython.Runtime.PythonDictionary:
        ...

    # methods
    @typing.overload
    def __init__(self, context: IronPython.Runtime.CodeContext, ):
        ...

    @typing.overload
    def __init__(self, context: IronPython.Runtime.CodeContext, kwArgsø: System.Collections.Generic.IDictionary[System.Object, System.Object], args: System.Array[System.Object], ):
        ...

    def __init__(self, initial_bytes: IronPython.Runtime.IBufferProtocol = ..., ) -> None:
        ...

    def close(self, context: IronPython.Runtime.CodeContext, ) -> None:
        ...

    def getvalue(self, ) -> IronPython.Runtime.Bytes:
        ...

    def getbuffer(self, ) -> IronPython.Runtime.MemoryView:
        ...

    def isatty(self, context: IronPython.Runtime.CodeContext, ) -> bool:
        ...

    def read(self, context: IronPython.Runtime.CodeContext, size: System.Object = ..., ) -> System.Object:
        ...

    def read1(self, context: IronPython.Runtime.CodeContext, size: int, ) -> IronPython.Runtime.Bytes:
        ...

    def readable(self, context: IronPython.Runtime.CodeContext, ) -> bool:
        ...

    @typing.overload
    def readinto(self, buffer: IronPython.Runtime.IBufferProtocol, ) -> System.Numerics.BigInteger:
        ...

    @typing.overload
    def readinto(self, context: IronPython.Runtime.CodeContext, buf: System.Object, ) -> System.Numerics.BigInteger:
        ...

    @typing.overload
    def readline(self, context: IronPython.Runtime.CodeContext, limit: int = ..., ) -> System.Object:
        ...

    @typing.overload
    def readline(self, size: int = ..., ) -> IronPython.Runtime.Bytes:
        ...

    @typing.overload
    def readline(self, size: System.Object, ) -> IronPython.Runtime.Bytes:
        ...

    def readlines(self, hint: System.Object = ..., ) -> IronPython.Runtime.PythonList:
        ...

    @typing.overload
    def seek(self, pos: int, whence: int, ) -> System.Numerics.BigInteger:
        ...

    @typing.overload
    def seek(self, pos: float, whence: System.Object, ) -> System.Numerics.BigInteger:
        ...

    @typing.overload
    def seek(self, context: IronPython.Runtime.CodeContext, pos: System.Numerics.BigInteger, whence: System.Object, ) -> System.Numerics.BigInteger:
        ...

    def seekable(self, context: IronPython.Runtime.CodeContext, ) -> bool:
        ...

    def tell(self, context: IronPython.Runtime.CodeContext, ) -> System.Numerics.BigInteger:
        ...

    @typing.overload
    def truncate(self, ) -> System.Numerics.BigInteger:
        ...

    @typing.overload
    def truncate(self, size: int, ) -> System.Numerics.BigInteger:
        ...

    @typing.overload
    def truncate(self, context: IronPython.Runtime.CodeContext, size: System.Object = ..., ) -> System.Numerics.BigInteger:
        ...

    def writable(self, context: IronPython.Runtime.CodeContext, ) -> bool:
        ...

    @typing.overload
    def write(self, context: IronPython.Runtime.CodeContext, bytes: System.Object, ) -> System.Numerics.BigInteger:
        ...

    @typing.overload
    def write(self, context: IronPython.Runtime.CodeContext, bytes: IronPython.Runtime.IBufferProtocol, ) -> System.Numerics.BigInteger:
        ...

    def writelines(self, lines: System.Collections.IEnumerable, ) -> None:
        ...

    def __getstate__(self, context: IronPython.Runtime.CodeContext, ) -> IronPython.Runtime.PythonTuple:
        ...

    def __setstate__(self, context: IronPython.Runtime.CodeContext, tuple: IronPython.Runtime.PythonTuple, ) -> None:
        ...

    def Dispose(self, ) -> None:
        ...

    def MoveNext(self, ) -> bool:
        ...

    def Reset(self, ) -> None:
        ...

    def GetMetaObject(self, parameter: System.Linq.Expressions.Expression, ) -> System.Dynamic.DynamicMetaObject:
        ...

    @typing.overload
    def DoWrite(self, bufferProtocol: IronPython.Runtime.IBufferProtocol, ) -> int:
        ...

    @typing.overload
    def DoWrite(self, bytes: System.Object, ) -> int:
        ...

    def EnsureSize(self, size: int, ) -> None:
        ...

    def EnsureSizeSetLength(self, size: int, ) -> None:
        ...

class BufferedRandom(System.IDisposable, System.Collections.Generic.IEnumerator[System.Object], System.Collections.IEnumerator, System.Collections.Generic.IEnumerable[System.Object], System.Collections.IEnumerable, IronPython.Runtime.IWeakReferenceable, System.Dynamic.IDynamicMetaObjectProvider, IronPython.Runtime.Binding.IPythonExpandable, IronPython.Modules.PythonIOModule._BufferedIOBase):
    @typing.overload
    def __init__(self, **kwargs):
        self.context: IronPython.Runtime.CodeContext
        ...

    # static fields

    # properties
    @property
    def raw(self) -> IronPython.Modules.PythonIOModule._IOBase:
        ...
    @raw.setter
    def raw(self, val: IronPython.Modules.PythonIOModule._IOBase):
        ...

    @property
    def closed(self) -> bool:
        ...

    @property
    def name(self) -> System.Object:
        ...

    @property
    def mode(self) -> System.Object:
        ...

    @property
    def __dict__(self) -> IronPython.Runtime.PythonDictionary:
        ...

    # methods
    def __init__(self, context: IronPython.Runtime.CodeContext, raw: IronPython.Modules.PythonIOModule._IOBase, buffer_size: int = ..., max_buffer_size: System.Object = ..., ):
        ...

    @staticmethod
    def Create(context: IronPython.Runtime.CodeContext, raw: IronPython.Modules.PythonIOModule._IOBase, buffer_size: int = ..., max_buffer_size: System.Object = ..., ) -> IronPython.Modules.PythonIOModule.BufferedRandom:
        ...

    def __init__(self, context: IronPython.Runtime.CodeContext, raw: IronPython.Modules.PythonIOModule._IOBase, buffer_size: int = ..., max_buffer_size: System.Object = ..., ) -> None:
        ...

    def close(self, context: IronPython.Runtime.CodeContext, ) -> None:
        ...

    def detach(self, context: IronPython.Runtime.CodeContext, ) -> System.Object:
        ...

    def seekable(self, context: IronPython.Runtime.CodeContext, ) -> bool:
        ...

    def readable(self, context: IronPython.Runtime.CodeContext, ) -> bool:
        ...

    def writable(self, context: IronPython.Runtime.CodeContext, ) -> bool:
        ...

    def fileno(self, context: IronPython.Runtime.CodeContext, ) -> int:
        ...

    def isatty(self, context: IronPython.Runtime.CodeContext, ) -> bool:
        ...

    def read(self, context: IronPython.Runtime.CodeContext, length: System.Object = ..., ) -> System.Object:
        ...

    def ReadNoLock(self, context: IronPython.Runtime.CodeContext, length: int, ) -> IronPython.Runtime.Bytes:
        ...

    def peek(self, context: IronPython.Runtime.CodeContext, length: int = ..., ) -> IronPython.Runtime.Bytes:
        ...

    def PeekNoLock(self, context: IronPython.Runtime.CodeContext, length: int, ) -> IronPython.Runtime.Bytes:
        ...

    def read1(self, context: IronPython.Runtime.CodeContext, length: int = ..., ) -> IronPython.Runtime.Bytes:
        ...

    def ResetReadBuf(self, ) -> IronPython.Runtime.Bytes:
        ...

    def write(self, context: IronPython.Runtime.CodeContext, buf: System.Object, ) -> System.Numerics.BigInteger:
        ...

    def flush(self, context: IronPython.Runtime.CodeContext, ) -> None:
        ...

    def FlushNoLock(self, context: IronPython.Runtime.CodeContext, ) -> None:
        ...

    def readinto(self, context: IronPython.Runtime.CodeContext, buf: System.Object, ) -> System.Numerics.BigInteger:
        ...

    @typing.overload
    def seek(self, offset: float, whence: System.Object, ) -> System.Numerics.BigInteger:
        ...

    @typing.overload
    def seek(self, context: IronPython.Runtime.CodeContext, pos: System.Numerics.BigInteger, whence: System.Object, ) -> System.Numerics.BigInteger:
        ...

    def truncate(self, context: IronPython.Runtime.CodeContext, pos: System.Object = ..., ) -> System.Numerics.BigInteger:
        ...

    def tell(self, context: IronPython.Runtime.CodeContext, ) -> System.Numerics.BigInteger:
        ...

    def GetMetaObject(self, parameter: System.Linq.Expressions.Expression, ) -> System.Dynamic.DynamicMetaObject:
        ...

class _BufferedIOBase(System.IDisposable, System.Collections.Generic.IEnumerator[System.Object], System.Collections.IEnumerator, System.Collections.Generic.IEnumerable[System.Object], System.Collections.IEnumerable, IronPython.Runtime.IWeakReferenceable, System.Dynamic.IDynamicMetaObjectProvider, IronPython.Runtime.Binding.IPythonExpandable, IronPython.Modules.PythonIOModule._IOBase):
    @typing.overload
    def __init__(self, **kwargs):
        self.context: IronPython.Runtime.CodeContext
        ...

    # static fields

    # properties
    @property
    def closed(self) -> bool:
        ...

    @property
    def __dict__(self) -> IronPython.Runtime.PythonDictionary:
        ...

    # methods
    def __init__(self, context: IronPython.Runtime.CodeContext, ):
        ...

    def detach(self, context: IronPython.Runtime.CodeContext, ) -> System.Object:
        ...

    def read(self, context: IronPython.Runtime.CodeContext, length: System.Object = ..., ) -> System.Object:
        ...

    def readinto(self, context: IronPython.Runtime.CodeContext, buf: System.Object, ) -> System.Numerics.BigInteger:
        ...

    def write(self, context: IronPython.Runtime.CodeContext, buf: System.Object, ) -> System.Numerics.BigInteger:
        ...

    def GetMetaObject(self, parameter: System.Linq.Expressions.Expression, ) -> System.Dynamic.DynamicMetaObject:
        ...

class _TextIOBase(System.IDisposable, System.Collections.Generic.IEnumerator[System.Object], System.Collections.IEnumerator, System.Collections.Generic.IEnumerable[System.Object], System.Collections.IEnumerable, IronPython.Runtime.IWeakReferenceable, System.Dynamic.IDynamicMetaObjectProvider, IronPython.Runtime.Binding.IPythonExpandable, IronPython.Modules.PythonIOModule._IOBase):
    @typing.overload
    def __init__(self, **kwargs):
        self.context: IronPython.Runtime.CodeContext
        ...

    # static fields

    # properties
    @property
    def encoding(self) -> str:
        ...

    @property
    def errors(self) -> str:
        ...

    @property
    def newlines(self) -> System.Object:
        ...

    @property
    def closed(self) -> bool:
        ...

    @property
    def __dict__(self) -> IronPython.Runtime.PythonDictionary:
        ...

    # methods
    def __init__(self, context: IronPython.Runtime.CodeContext, ):
        ...

    def detach(self, context: IronPython.Runtime.CodeContext, ) -> System.Object:
        ...

    def read(self, context: IronPython.Runtime.CodeContext, length: System.Object = ..., ) -> System.Object:
        ...

    def readline(self, context: IronPython.Runtime.CodeContext, limit: int = ..., ) -> System.Object:
        ...

    def truncate(self, context: IronPython.Runtime.CodeContext, pos: System.Object = ..., ) -> System.Numerics.BigInteger:
        ...

    def write(self, context: IronPython.Runtime.CodeContext, str: System.Object, ) -> System.Numerics.BigInteger:
        ...

    def GetMetaObject(self, parameter: System.Linq.Expressions.Expression, ) -> System.Dynamic.DynamicMetaObject:
        ...

class IncrementalNewlineDecoder(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def newlines(self) -> System.Object:
        ...

    # methods
    def __init__(self, decoder: System.Object, translate: bool, errors: str = ..., ):
        ...

    @typing.overload
    def decode(self, context: IronPython.Runtime.CodeContext, input: System.Collections.Generic.IList[int], final: bool = ..., ) -> str:
        ...

    @typing.overload
    def decode(self, context: IronPython.Runtime.CodeContext, input: str, final: bool = ..., ) -> str:
        ...

    def DecodeWorker(self, context: IronPython.Runtime.CodeContext, decoded: str, final: bool, ) -> str:
        ...

    def getstate(self, context: IronPython.Runtime.CodeContext, ) -> IronPython.Runtime.PythonTuple:
        ...

    def GetState(self, context: IronPython.Runtime.CodeContext, buf: ref[IronPython.Runtime.Bytes], flags: ref[int], ) -> None:
        ...

    def setstate(self, context: IronPython.Runtime.CodeContext, state: IronPython.Runtime.PythonTuple, ) -> None:
        ...

    def SetState(self, context: IronPython.Runtime.CodeContext, buffer: IronPython.Runtime.Bytes, flags: int, ) -> None:
        ...

    def reset(self, context: IronPython.Runtime.CodeContext, ) -> None:
        ...

    @staticmethod
    def GetNewlines(_seenNL: int, ) -> System.Object:
        ...

class TextIOWrapper(System.IDisposable, System.Collections.Generic.IEnumerator[System.Object], System.Collections.IEnumerator, System.Collections.Generic.IEnumerable[System.Object], System.Collections.IEnumerable, IronPython.Runtime.IWeakReferenceable, System.Dynamic.IDynamicMetaObjectProvider, IronPython.Runtime.Binding.IPythonExpandable, IronPython.Runtime.ICodeFormattable, IronPython.Modules.PythonIOModule._TextIOBase):
    @typing.overload
    def __init__(self, **kwargs):
        self._CHUNK_SIZE: int
        self._bufferTyped: IronPython.Modules.PythonIOModule._BufferedIOBase
        self._encoding: str
        self._errors: str
        self._writeTranslate: bool
        self.context: IronPython.Runtime.CodeContext
        ...

    # static fields

    # properties
    @property
    def buffer(self) -> System.Object:
        ...

    @property
    def encoding(self) -> str:
        ...

    @property
    def errors(self) -> str:
        ...

    @property
    def line_buffering(self) -> bool:
        ...

    @property
    def write_through(self) -> bool:
        ...

    @property
    def newlines(self) -> System.Object:
        ...

    @property
    def closed(self) -> bool:
        ...

    @property
    def name(self) -> System.Object:
        ...

    @property
    def Current(self) -> System.Object:
        ...

    @property
    def Current(self) -> System.Object:
        ...

    @property
    def __dict__(self) -> IronPython.Runtime.PythonDictionary:
        ...

    # methods
    def __init__(self, context: IronPython.Runtime.CodeContext, ):
        ...

    @staticmethod
    def Create(context: IronPython.Runtime.CodeContext, buffer: System.Object, encoding: str = ..., errors: str = ..., newline: str = ..., line_buffering: bool = ..., write_through: bool = ..., ) -> IronPython.Modules.PythonIOModule.TextIOWrapper:
        ...

    def __init__(self, context: IronPython.Runtime.CodeContext, buffer: System.Object, encoding: str = ..., errors: str = ..., newline: str = ..., line_buffering: bool = ..., write_through: bool = ..., ) -> None:
        ...

    def seekable(self, context: IronPython.Runtime.CodeContext, ) -> bool:
        ...

    def readable(self, context: IronPython.Runtime.CodeContext, ) -> bool:
        ...

    def writable(self, context: IronPython.Runtime.CodeContext, ) -> bool:
        ...

    def flush(self, context: IronPython.Runtime.CodeContext, ) -> None:
        ...

    def close(self, context: IronPython.Runtime.CodeContext, ) -> None:
        ...

    def fileno(self, context: IronPython.Runtime.CodeContext, ) -> int:
        ...

    def isatty(self, context: IronPython.Runtime.CodeContext, ) -> bool:
        ...

    def write(self, context: IronPython.Runtime.CodeContext, s: System.Object, ) -> System.Numerics.BigInteger:
        ...

    def tell(self, context: IronPython.Runtime.CodeContext, ) -> System.Numerics.BigInteger:
        ...

    def truncate(self, context: IronPython.Runtime.CodeContext, pos: System.Object = ..., ) -> System.Numerics.BigInteger:
        ...

    def detach(self, context: IronPython.Runtime.CodeContext, ) -> System.Object:
        ...

    @typing.overload
    def seek(self, offset: float, whence: System.Object, ) -> System.Numerics.BigInteger:
        ...

    @typing.overload
    def seek(self, context: IronPython.Runtime.CodeContext, cookie: System.Numerics.BigInteger, whence: System.Object, ) -> System.Numerics.BigInteger:
        ...

    def read(self, context: IronPython.Runtime.CodeContext, length: System.Object = ..., ) -> System.Object:
        ...

    def readline(self, context: IronPython.Runtime.CodeContext, limit: int = ..., ) -> System.Object:
        ...

    def MoveNext(self, ) -> bool:
        ...

    def Reset(self, ) -> None:
        ...

    def GetEnumerator(self, ) -> System.Collections.Generic.IEnumerator[System.Object]:
        ...

    def GetEnumerator(self, ) -> System.Collections.IEnumerator:
        ...

    def __repr__(self, context: IronPython.Runtime.CodeContext, ) -> str:
        ...

    def GetMetaObject(self, parameter: System.Linq.Expressions.Expression, ) -> System.Dynamic.DynamicMetaObject:
        ...

    def UnpackCookie(self, cookie: System.Numerics.BigInteger, pos: ref[System.Numerics.BigInteger], decodeFlags: ref[int], bytesFed: ref[int], skip: ref[int], needEOF: ref[bool], ) -> None:
        ...

    def GetEncoder(self, context: IronPython.Runtime.CodeContext, ) -> System.Object:
        ...

    def GetDecoder(self, context: IronPython.Runtime.CodeContext, ) -> System.Object:
        ...

    def SetDecodedChars(self, chars: str, ) -> None:
        ...

    @typing.overload
    def GetDecodedChars(self, ) -> str:
        ...

    @typing.overload
    def GetDecodedChars(self, length: int, ) -> str:
        ...

    def RewindDecodedChars(self, length: int, ) -> None:
        ...

    def ReadChunk(self, context: IronPython.Runtime.CodeContext, ) -> bool:
        ...

class _IOBase(System.IDisposable, System.Collections.Generic.IEnumerator[System.Object], System.Collections.IEnumerator, System.Collections.Generic.IEnumerable[System.Object], System.Collections.IEnumerable, IronPython.Runtime.IWeakReferenceable, System.Dynamic.IDynamicMetaObjectProvider, IronPython.Runtime.Binding.IPythonExpandable, System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        self.context: IronPython.Runtime.CodeContext
        ...

    # static fields

    # properties
    @property
    def closed(self) -> bool:
        ...

    @property
    def Current(self) -> System.Object:
        ...

    @property
    def Current(self) -> System.Object:
        ...

    @property
    def __dict__(self) -> IronPython.Runtime.PythonDictionary:
        ...

    @property
    def CustomAttributes(self) -> System.Collections.Generic.IDictionary[System.Object, System.Object]:
        ...

    @property
    def Context(self) -> IronPython.Runtime.CodeContext:
        ...

    # methods
    def __init__(self, context: IronPython.Runtime.CodeContext, ):
        ...

    def read(self, context: IronPython.Runtime.CodeContext, length: System.Object = ..., ) -> System.Object:
        ...

    def write(self, context: IronPython.Runtime.CodeContext, buf: System.Object, ) -> System.Numerics.BigInteger:
        ...

    @typing.overload
    def readline(self, context: IronPython.Runtime.CodeContext, limit: int, ) -> System.Object:
        ...

    @typing.overload
    def readline(self, context: IronPython.Runtime.CodeContext, limit: System.Object = ..., ) -> System.Object:
        ...

    def truncate(self, context: IronPython.Runtime.CodeContext, pos: System.Object = ..., ) -> System.Numerics.BigInteger:
        ...

    def __del__(self, context: IronPython.Runtime.CodeContext, ) -> None:
        ...

    def __enter__(self, ) -> IronPython.Modules.PythonIOModule._IOBase:
        ...

    def __exit__(self, context: IronPython.Runtime.CodeContext, excinfo: System.Array[System.Object], ) -> None:
        ...

    @typing.overload
    def _checkClosed(self, ) -> None:
        ...

    @typing.overload
    def _checkClosed(self, msg: str, ) -> None:
        ...

    @typing.overload
    def _checkReadable(self, ) -> None:
        ...

    @typing.overload
    def _checkReadable(self, msg: str, ) -> None:
        ...

    @typing.overload
    def _checkSeekable(self, ) -> None:
        ...

    @typing.overload
    def _checkSeekable(self, msg: str, ) -> None:
        ...

    @typing.overload
    def _checkWritable(self, ) -> None:
        ...

    @typing.overload
    def _checkWritable(self, msg: str, ) -> None:
        ...

    def close(self, context: IronPython.Runtime.CodeContext, ) -> None:
        ...

    def fileno(self, context: IronPython.Runtime.CodeContext, ) -> int:
        ...

    def flush(self, context: IronPython.Runtime.CodeContext, ) -> None:
        ...

    def isatty(self, context: IronPython.Runtime.CodeContext, ) -> bool:
        ...

    def peek(self, context: IronPython.Runtime.CodeContext, length: int = ..., ) -> IronPython.Runtime.Bytes:
        ...

    def read1(self, context: IronPython.Runtime.CodeContext, length: int = ..., ) -> IronPython.Runtime.Bytes:
        ...

    def readable(self, context: IronPython.Runtime.CodeContext, ) -> bool:
        ...

    @typing.overload
    def readlines(self, ) -> IronPython.Runtime.PythonList:
        ...

    @typing.overload
    def readlines(self, hint: System.Object = ..., ) -> IronPython.Runtime.PythonList:
        ...

    def seek(self, context: IronPython.Runtime.CodeContext, pos: System.Numerics.BigInteger, whence: System.Object, ) -> System.Numerics.BigInteger:
        ...

    def seekable(self, context: IronPython.Runtime.CodeContext, ) -> bool:
        ...

    def tell(self, context: IronPython.Runtime.CodeContext, ) -> System.Numerics.BigInteger:
        ...

    def writable(self, context: IronPython.Runtime.CodeContext, ) -> bool:
        ...

    def writelines(self, context: IronPython.Runtime.CodeContext, lines: System.Object, ) -> None:
        ...

    def Finalize(self, ) -> None:
        ...

    def MoveNext(self, ) -> bool:
        ...

    def Reset(self, ) -> None:
        ...

    def GetEnumerator(self, ) -> System.Collections.Generic.IEnumerator[System.Object]:
        ...

    def GetEnumerator(self, ) -> System.Collections.IEnumerator:
        ...

    def Dispose(self, ) -> None:
        ...

    def GetWeakRef(self, ) -> IronPython.Runtime.WeakRefTracker:
        ...

    def SetWeakRef(self, value: IronPython.Runtime.WeakRefTracker, ) -> bool:
        ...

    def SetFinalizer(self, value: IronPython.Runtime.WeakRefTracker, ) -> None:
        ...

    def EnsureCustomAttributes(self, ) -> IronPython.Runtime.PythonDictionary:
        ...

    def EnsureCustomAttributes(self, ) -> System.Collections.Generic.IDictionary[System.Object, System.Object]:
        ...

    def GetMetaObject(self, parameter: System.Linq.Expressions.Expression, ) -> System.Dynamic.DynamicMetaObject:
        ...

    def UnsupportedOperation(self, context: IronPython.Runtime.CodeContext, attr: str, ) -> System.Exception:
        ...

    def UnsupportedOperationWithMessage(self, context: IronPython.Runtime.CodeContext, msg: str, ) -> System.Exception:
        ...

    def AttributeError(self, attrName: str, ) -> System.Exception:
        ...

    def InvalidPosition(self, pos: System.Numerics.BigInteger, ) -> System.Exception:
        ...

class BufferedRWPair(System.IDisposable, System.Collections.Generic.IEnumerator[System.Object], System.Collections.IEnumerator, System.Collections.Generic.IEnumerable[System.Object], System.Collections.IEnumerable, IronPython.Runtime.IWeakReferenceable, System.Dynamic.IDynamicMetaObjectProvider, IronPython.Runtime.Binding.IPythonExpandable, IronPython.Modules.PythonIOModule._BufferedIOBase):
    @typing.overload
    def __init__(self, **kwargs):
        self.context: IronPython.Runtime.CodeContext
        ...

    # static fields

    # properties
    @property
    def reader(self) -> System.Object:
        ...
    @reader.setter
    def reader(self, val: System.Object):
        ...

    @property
    def writer(self) -> System.Object:
        ...
    @writer.setter
    def writer(self, val: System.Object):
        ...

    @property
    def closed(self) -> bool:
        ...

    @property
    def __dict__(self) -> IronPython.Runtime.PythonDictionary:
        ...

    # methods
    def __init__(self, context: IronPython.Runtime.CodeContext, reader: System.Object, writer: System.Object, buffer_size: int = ..., max_buffer_size: System.Object = ..., ):
        ...

    def __init__(self, context: IronPython.Runtime.CodeContext, reader: System.Object, writer: System.Object, buffer_size: int = ..., max_buffer_size: System.Object = ..., ) -> None:
        ...

    def read(self, context: IronPython.Runtime.CodeContext, length: System.Object = ..., ) -> System.Object:
        ...

    def readinto(self, context: IronPython.Runtime.CodeContext, buf: System.Object, ) -> System.Numerics.BigInteger:
        ...

    def write(self, context: IronPython.Runtime.CodeContext, buf: System.Object, ) -> System.Numerics.BigInteger:
        ...

    def peek(self, context: IronPython.Runtime.CodeContext, length: int = ..., ) -> IronPython.Runtime.Bytes:
        ...

    def read1(self, context: IronPython.Runtime.CodeContext, length: int, ) -> IronPython.Runtime.Bytes:
        ...

    def readable(self, context: IronPython.Runtime.CodeContext, ) -> bool:
        ...

    def writable(self, context: IronPython.Runtime.CodeContext, ) -> bool:
        ...

    def flush(self, context: IronPython.Runtime.CodeContext, ) -> None:
        ...

    def close(self, context: IronPython.Runtime.CodeContext, ) -> None:
        ...

    def isatty(self, context: IronPython.Runtime.CodeContext, ) -> bool:
        ...

    def GetMetaObject(self, parameter: System.Linq.Expressions.Expression, ) -> System.Dynamic.DynamicMetaObject:
        ...

