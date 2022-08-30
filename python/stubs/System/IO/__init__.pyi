from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import System
import System.IO
import System.Threading.Tasks
import System.Threading
import Microsoft.Win32.SafeHandles
import System.Text


class Stream(System.IDisposable, System.IAsyncDisposable, System.MarshalByRefObject, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @abc.abstractmethod
    @property
    def CanRead(self) -> System.Boolean:
        ...

    @abc.abstractmethod
    @property
    def CanWrite(self) -> System.Boolean:
        ...

    @abc.abstractmethod
    @property
    def CanSeek(self) -> System.Boolean:
        ...

    @property
    def CanTimeout(self) -> System.Boolean:
        ...

    @abc.abstractmethod
    @property
    def Length(self) -> System.Int64:
        ...

    @abc.abstractmethod
    @property
    def Position(self) -> System.Int64:
        ...
    @abc.abstractmethod
    @Position.setter
    def Position(self, val: System.Int64):
        ...

    @property
    def ReadTimeout(self) -> System.Int32:
        ...
    @ReadTimeout.setter
    def ReadTimeout(self, val: System.Int32):
        ...

    @property
    def WriteTimeout(self) -> System.Int32:
        ...
    @WriteTimeout.setter
    def WriteTimeout(self, val: System.Int32):
        ...

    # methods
    @typing.overload
    def CopyTo(self, destination: System.IO.Stream, ) -> None:
        ...

    @typing.overload
    def CopyTo(self, destination: System.IO.Stream, bufferSize: System.Int32, ) -> None:
        ...

    @typing.overload
    def CopyToAsync(self, destination: System.IO.Stream, ) -> System.Threading.Tasks.Task:
        ...

    @typing.overload
    def CopyToAsync(self, destination: System.IO.Stream, bufferSize: System.Int32, ) -> System.Threading.Tasks.Task:
        ...

    @typing.overload
    def CopyToAsync(self, destination: System.IO.Stream, cancellationToken: System.Threading.CancellationToken, ) -> System.Threading.Tasks.Task:
        ...

    @typing.overload
    def CopyToAsync(self, destination: System.IO.Stream, bufferSize: System.Int32, cancellationToken: System.Threading.CancellationToken, ) -> System.Threading.Tasks.Task:
        ...

    @typing.overload
    def Dispose(self, ) -> None:
        ...

    @typing.overload
    def Close(self, ) -> None:
        ...

    @typing.overload
    def DisposeAsync(self, ) -> System.Threading.Tasks.ValueTask:
        ...

    @typing.overload
    @abc.abstractmethod
    def Flush(self, ) -> None:
        ...

    @typing.overload
    def FlushAsync(self, ) -> System.Threading.Tasks.Task:
        ...

    @typing.overload
    def FlushAsync(self, cancellationToken: System.Threading.CancellationToken, ) -> System.Threading.Tasks.Task:
        ...

    @typing.overload
    def BeginRead(self, buffer: list[System.Byte], offset: System.Int32, count: System.Int32, callback: System.AsyncCallback, state: System.Object, ) -> System.IAsyncResult:
        ...

    @typing.overload
    def EndRead(self, asyncResult: System.IAsyncResult, ) -> System.Int32:
        ...

    @typing.overload
    def ReadAsync(self, buffer: list[System.Byte], offset: System.Int32, count: System.Int32, ) -> System.Threading.Tasks.Task[System.Int32]:
        ...

    @typing.overload
    def ReadAsync(self, buffer: list[System.Byte], offset: System.Int32, count: System.Int32, cancellationToken: System.Threading.CancellationToken, ) -> System.Threading.Tasks.Task[System.Int32]:
        ...

    @typing.overload
    def ReadAsync(self, buffer: System.Memory[System.Byte], cancellationToken: System.Threading.CancellationToken, ) -> System.Threading.Tasks.ValueTask[System.Int32]:
        ...

    @typing.overload
    def BeginWrite(self, buffer: list[System.Byte], offset: System.Int32, count: System.Int32, callback: System.AsyncCallback, state: System.Object, ) -> System.IAsyncResult:
        ...

    @typing.overload
    def EndWrite(self, asyncResult: System.IAsyncResult, ) -> None:
        ...

    @typing.overload
    def WriteAsync(self, buffer: list[System.Byte], offset: System.Int32, count: System.Int32, ) -> System.Threading.Tasks.Task:
        ...

    @typing.overload
    def WriteAsync(self, buffer: list[System.Byte], offset: System.Int32, count: System.Int32, cancellationToken: System.Threading.CancellationToken, ) -> System.Threading.Tasks.Task:
        ...

    @typing.overload
    def WriteAsync(self, buffer: System.ReadOnlyMemory[System.Byte], cancellationToken: System.Threading.CancellationToken, ) -> System.Threading.Tasks.ValueTask:
        ...

    @typing.overload
    @abc.abstractmethod
    def Seek(self, offset: System.Int64, origin: System.IO.SeekOrigin, ) -> System.Int64:
        ...

    @typing.overload
    @abc.abstractmethod
    def SetLength(self, value: System.Int64, ) -> None:
        ...

    @typing.overload
    @abc.abstractmethod
    def Read(self, buffer: list[System.Byte], offset: System.Int32, count: System.Int32, ) -> System.Int32:
        ...

    @typing.overload
    def Read(self, buffer: System.Span[System.Byte], ) -> System.Int32:
        ...

    @typing.overload
    def ReadByte(self, ) -> System.Int32:
        ...

    @typing.overload
    @abc.abstractmethod
    def Write(self, buffer: list[System.Byte], offset: System.Int32, count: System.Int32, ) -> None:
        ...

    @typing.overload
    def Write(self, buffer: System.ReadOnlySpan[System.Byte], ) -> None:
        ...

    @typing.overload
    def WriteByte(self, value: System.Byte, ) -> None:
        ...

    @typing.overload
    @staticmethod
    def Synchronized(stream: System.IO.Stream, ) -> System.IO.Stream:
        ...

class TextReader(System.IDisposable, System.MarshalByRefObject, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    # methods
    @typing.overload
    def Close(self, ) -> None:
        ...

    @typing.overload
    def Dispose(self, ) -> None:
        ...

    @typing.overload
    def Peek(self, ) -> System.Int32:
        ...

    @typing.overload
    def Read(self, ) -> System.Int32:
        ...

    @typing.overload
    def Read(self, buffer: list[System.Char], index: System.Int32, count: System.Int32, ) -> System.Int32:
        ...

    @typing.overload
    def Read(self, buffer: System.Span[System.Char], ) -> System.Int32:
        ...

    @typing.overload
    def ReadToEnd(self, ) -> System.String:
        ...

    @typing.overload
    def ReadBlock(self, buffer: list[System.Char], index: System.Int32, count: System.Int32, ) -> System.Int32:
        ...

    @typing.overload
    def ReadBlock(self, buffer: System.Span[System.Char], ) -> System.Int32:
        ...

    @typing.overload
    def ReadLine(self, ) -> System.String:
        ...

    @typing.overload
    def ReadLineAsync(self, ) -> System.Threading.Tasks.Task[System.String]:
        ...

    @typing.overload
    def ReadToEndAsync(self, ) -> System.Threading.Tasks.Task[System.String]:
        ...

    @typing.overload
    def ReadAsync(self, buffer: list[System.Char], index: System.Int32, count: System.Int32, ) -> System.Threading.Tasks.Task[System.Int32]:
        ...

    @typing.overload
    def ReadAsync(self, buffer: System.Memory[System.Char], cancellationToken: System.Threading.CancellationToken, ) -> System.Threading.Tasks.ValueTask[System.Int32]:
        ...

    @typing.overload
    def ReadBlockAsync(self, buffer: list[System.Char], index: System.Int32, count: System.Int32, ) -> System.Threading.Tasks.Task[System.Int32]:
        ...

    @typing.overload
    def ReadBlockAsync(self, buffer: System.Memory[System.Char], cancellationToken: System.Threading.CancellationToken, ) -> System.Threading.Tasks.ValueTask[System.Int32]:
        ...

    @typing.overload
    @staticmethod
    def Synchronized(reader: System.IO.TextReader, ) -> System.IO.TextReader:
        ...

class FileStream(System.IDisposable, System.IAsyncDisposable, System.IO.Stream):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def Handle(self) -> System.IntPtr:
        ...

    @property
    def CanRead(self) -> System.Boolean:
        ...

    @property
    def CanWrite(self) -> System.Boolean:
        ...

    @property
    def SafeFileHandle(self) -> Microsoft.Win32.SafeHandles.SafeFileHandle:
        ...

    @property
    def Name(self) -> System.String:
        ...

    @property
    def IsAsync(self) -> System.Boolean:
        ...

    @property
    def Length(self) -> System.Int64:
        ...

    @property
    def Position(self) -> System.Int64:
        ...
    @Position.setter
    def Position(self, val: System.Int64):
        ...

    @property
    def CanSeek(self) -> System.Boolean:
        ...

    @property
    def CanTimeout(self) -> System.Boolean:
        ...

    @property
    def ReadTimeout(self) -> System.Int32:
        ...
    @ReadTimeout.setter
    def ReadTimeout(self, val: System.Int32):
        ...

    @property
    def WriteTimeout(self) -> System.Int32:
        ...
    @WriteTimeout.setter
    def WriteTimeout(self, val: System.Int32):
        ...

    # methods
    @typing.overload
    def __init__(self, handle: System.IntPtr, access: System.IO.FileAccess, ):
        ...

    @typing.overload
    def __init__(self, handle: System.IntPtr, access: System.IO.FileAccess, ownsHandle: System.Boolean, ):
        ...

    @typing.overload
    def __init__(self, handle: System.IntPtr, access: System.IO.FileAccess, ownsHandle: System.Boolean, bufferSize: System.Int32, ):
        ...

    @typing.overload
    def __init__(self, handle: System.IntPtr, access: System.IO.FileAccess, ownsHandle: System.Boolean, bufferSize: System.Int32, isAsync: System.Boolean, ):
        ...

    @typing.overload
    def __init__(self, handle: Microsoft.Win32.SafeHandles.SafeFileHandle, access: System.IO.FileAccess, ):
        ...

    @typing.overload
    def __init__(self, handle: Microsoft.Win32.SafeHandles.SafeFileHandle, access: System.IO.FileAccess, bufferSize: System.Int32, ):
        ...

    @typing.overload
    def __init__(self, handle: Microsoft.Win32.SafeHandles.SafeFileHandle, access: System.IO.FileAccess, bufferSize: System.Int32, isAsync: System.Boolean, ):
        ...

    @typing.overload
    def __init__(self, path: System.String, mode: System.IO.FileMode, ):
        ...

    @typing.overload
    def __init__(self, path: System.String, mode: System.IO.FileMode, access: System.IO.FileAccess, ):
        ...

    @typing.overload
    def __init__(self, path: System.String, mode: System.IO.FileMode, access: System.IO.FileAccess, share: System.IO.FileShare, ):
        ...

    @typing.overload
    def __init__(self, path: System.String, mode: System.IO.FileMode, access: System.IO.FileAccess, share: System.IO.FileShare, bufferSize: System.Int32, ):
        ...

    @typing.overload
    def __init__(self, path: System.String, mode: System.IO.FileMode, access: System.IO.FileAccess, share: System.IO.FileShare, bufferSize: System.Int32, useAsync: System.Boolean, ):
        ...

    @typing.overload
    def __init__(self, path: System.String, mode: System.IO.FileMode, access: System.IO.FileAccess, share: System.IO.FileShare, bufferSize: System.Int32, options: System.IO.FileOptions, ):
        ...

    @typing.overload
    def __init__(self, path: System.String, options: System.IO.FileStreamOptions, ):
        ...

    @typing.overload
    def Lock(self, position: System.Int64, length: System.Int64, ) -> None:
        ...

    @typing.overload
    def Unlock(self, position: System.Int64, length: System.Int64, ) -> None:
        ...

    @typing.overload
    def FlushAsync(self, cancellationToken: System.Threading.CancellationToken, ) -> System.Threading.Tasks.Task:
        ...

    @typing.overload
    def Read(self, buffer: list[System.Byte], offset: System.Int32, count: System.Int32, ) -> System.Int32:
        ...

    @typing.overload
    def Read(self, buffer: System.Span[System.Byte], ) -> System.Int32:
        ...

    @typing.overload
    def ReadAsync(self, buffer: list[System.Byte], offset: System.Int32, count: System.Int32, cancellationToken: System.Threading.CancellationToken, ) -> System.Threading.Tasks.Task[System.Int32]:
        ...

    @typing.overload
    def ReadAsync(self, buffer: System.Memory[System.Byte], cancellationToken: System.Threading.CancellationToken, ) -> System.Threading.Tasks.ValueTask[System.Int32]:
        ...

    @typing.overload
    def Write(self, buffer: list[System.Byte], offset: System.Int32, count: System.Int32, ) -> None:
        ...

    @typing.overload
    def Write(self, buffer: System.ReadOnlySpan[System.Byte], ) -> None:
        ...

    @typing.overload
    def WriteAsync(self, buffer: list[System.Byte], offset: System.Int32, count: System.Int32, cancellationToken: System.Threading.CancellationToken, ) -> System.Threading.Tasks.Task:
        ...

    @typing.overload
    def WriteAsync(self, buffer: System.ReadOnlyMemory[System.Byte], cancellationToken: System.Threading.CancellationToken, ) -> System.Threading.Tasks.ValueTask:
        ...

    @typing.overload
    def Flush(self, ) -> None:
        ...

    @typing.overload
    def Flush(self, flushToDisk: System.Boolean, ) -> None:
        ...

    @typing.overload
    def SetLength(self, value: System.Int64, ) -> None:
        ...

    @typing.overload
    def ReadByte(self, ) -> System.Int32:
        ...

    @typing.overload
    def WriteByte(self, value: System.Byte, ) -> None:
        ...

    @typing.overload
    def DisposeAsync(self, ) -> System.Threading.Tasks.ValueTask:
        ...

    @typing.overload
    def CopyTo(self, destination: System.IO.Stream, bufferSize: System.Int32, ) -> None:
        ...

    @typing.overload
    def CopyToAsync(self, destination: System.IO.Stream, bufferSize: System.Int32, cancellationToken: System.Threading.CancellationToken, ) -> System.Threading.Tasks.Task:
        ...

    @typing.overload
    def BeginRead(self, buffer: list[System.Byte], offset: System.Int32, count: System.Int32, callback: System.AsyncCallback, state: System.Object, ) -> System.IAsyncResult:
        ...

    @typing.overload
    def EndRead(self, asyncResult: System.IAsyncResult, ) -> System.Int32:
        ...

    @typing.overload
    def BeginWrite(self, buffer: list[System.Byte], offset: System.Int32, count: System.Int32, callback: System.AsyncCallback, state: System.Object, ) -> System.IAsyncResult:
        ...

    @typing.overload
    def EndWrite(self, asyncResult: System.IAsyncResult, ) -> None:
        ...

    @typing.overload
    def Seek(self, offset: System.Int64, origin: System.IO.SeekOrigin, ) -> System.Int64:
        ...

class SeekOrigin(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    Begin: System.Int32 = Begin
    Current: System.Int32 = Current
    End: System.Int32 = End

class TextWriter(System.IDisposable, System.IAsyncDisposable, System.MarshalByRefObject, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def FormatProvider(self) -> System.IFormatProvider:
        ...

    @abc.abstractmethod
    @property
    def Encoding(self) -> System.Text.Encoding:
        ...

    @property
    def NewLine(self) -> System.String:
        ...
    @NewLine.setter
    def NewLine(self, val: System.String):
        ...

    # methods
    @typing.overload
    def Close(self, ) -> None:
        ...

    @typing.overload
    def Dispose(self, ) -> None:
        ...

    @typing.overload
    def DisposeAsync(self, ) -> System.Threading.Tasks.ValueTask:
        ...

    @typing.overload
    def Flush(self, ) -> None:
        ...

    @typing.overload
    def Write(self, value: System.Char, ) -> None:
        ...

    @typing.overload
    def Write(self, buffer: list[System.Char], ) -> None:
        ...

    @typing.overload
    def Write(self, buffer: list[System.Char], index: System.Int32, count: System.Int32, ) -> None:
        ...

    @typing.overload
    def Write(self, buffer: System.ReadOnlySpan[System.Char], ) -> None:
        ...

    @typing.overload
    def Write(self, value: System.Boolean, ) -> None:
        ...

    @typing.overload
    def Write(self, value: System.Int32, ) -> None:
        ...

    @typing.overload
    def Write(self, value: System.UInt32, ) -> None:
        ...

    @typing.overload
    def Write(self, value: System.Int64, ) -> None:
        ...

    @typing.overload
    def Write(self, value: System.UInt64, ) -> None:
        ...

    @typing.overload
    def Write(self, value: System.Single, ) -> None:
        ...

    @typing.overload
    def Write(self, value: System.Double, ) -> None:
        ...

    @typing.overload
    def Write(self, value: System.Decimal, ) -> None:
        ...

    @typing.overload
    def Write(self, value: System.String, ) -> None:
        ...

    @typing.overload
    def Write(self, value: System.Object, ) -> None:
        ...

    @typing.overload
    def Write(self, value: System.Text.StringBuilder, ) -> None:
        ...

    @typing.overload
    def Write(self, format: System.String, arg0: System.Object, ) -> None:
        ...

    @typing.overload
    def Write(self, format: System.String, arg0: System.Object, arg1: System.Object, ) -> None:
        ...

    @typing.overload
    def Write(self, format: System.String, arg0: System.Object, arg1: System.Object, arg2: System.Object, ) -> None:
        ...

    @typing.overload
    def Write(self, format: System.String, arg: list[System.Object], ) -> None:
        ...

    @typing.overload
    def WriteLine(self, ) -> None:
        ...

    @typing.overload
    def WriteLine(self, value: System.Char, ) -> None:
        ...

    @typing.overload
    def WriteLine(self, buffer: list[System.Char], ) -> None:
        ...

    @typing.overload
    def WriteLine(self, buffer: list[System.Char], index: System.Int32, count: System.Int32, ) -> None:
        ...

    @typing.overload
    def WriteLine(self, buffer: System.ReadOnlySpan[System.Char], ) -> None:
        ...

    @typing.overload
    def WriteLine(self, value: System.Boolean, ) -> None:
        ...

    @typing.overload
    def WriteLine(self, value: System.Int32, ) -> None:
        ...

    @typing.overload
    def WriteLine(self, value: System.UInt32, ) -> None:
        ...

    @typing.overload
    def WriteLine(self, value: System.Int64, ) -> None:
        ...

    @typing.overload
    def WriteLine(self, value: System.UInt64, ) -> None:
        ...

    @typing.overload
    def WriteLine(self, value: System.Single, ) -> None:
        ...

    @typing.overload
    def WriteLine(self, value: System.Double, ) -> None:
        ...

    @typing.overload
    def WriteLine(self, value: System.Decimal, ) -> None:
        ...

    @typing.overload
    def WriteLine(self, value: System.String, ) -> None:
        ...

    @typing.overload
    def WriteLine(self, value: System.Text.StringBuilder, ) -> None:
        ...

    @typing.overload
    def WriteLine(self, value: System.Object, ) -> None:
        ...

    @typing.overload
    def WriteLine(self, format: System.String, arg0: System.Object, ) -> None:
        ...

    @typing.overload
    def WriteLine(self, format: System.String, arg0: System.Object, arg1: System.Object, ) -> None:
        ...

    @typing.overload
    def WriteLine(self, format: System.String, arg0: System.Object, arg1: System.Object, arg2: System.Object, ) -> None:
        ...

    @typing.overload
    def WriteLine(self, format: System.String, arg: list[System.Object], ) -> None:
        ...

    @typing.overload
    def WriteAsync(self, value: System.Char, ) -> System.Threading.Tasks.Task:
        ...

    @typing.overload
    def WriteAsync(self, value: System.String, ) -> System.Threading.Tasks.Task:
        ...

    @typing.overload
    def WriteAsync(self, value: System.Text.StringBuilder, cancellationToken: System.Threading.CancellationToken, ) -> System.Threading.Tasks.Task:
        ...

    @typing.overload
    def WriteAsync(self, buffer: list[System.Char], ) -> System.Threading.Tasks.Task:
        ...

    @typing.overload
    def WriteAsync(self, buffer: list[System.Char], index: System.Int32, count: System.Int32, ) -> System.Threading.Tasks.Task:
        ...

    @typing.overload
    def WriteAsync(self, buffer: System.ReadOnlyMemory[System.Char], cancellationToken: System.Threading.CancellationToken, ) -> System.Threading.Tasks.Task:
        ...

    @typing.overload
    def WriteLineAsync(self, value: System.Char, ) -> System.Threading.Tasks.Task:
        ...

    @typing.overload
    def WriteLineAsync(self, value: System.String, ) -> System.Threading.Tasks.Task:
        ...

    @typing.overload
    def WriteLineAsync(self, value: System.Text.StringBuilder, cancellationToken: System.Threading.CancellationToken, ) -> System.Threading.Tasks.Task:
        ...

    @typing.overload
    def WriteLineAsync(self, buffer: list[System.Char], ) -> System.Threading.Tasks.Task:
        ...

    @typing.overload
    def WriteLineAsync(self, buffer: list[System.Char], index: System.Int32, count: System.Int32, ) -> System.Threading.Tasks.Task:
        ...

    @typing.overload
    def WriteLineAsync(self, buffer: System.ReadOnlyMemory[System.Char], cancellationToken: System.Threading.CancellationToken, ) -> System.Threading.Tasks.Task:
        ...

    @typing.overload
    def WriteLineAsync(self, ) -> System.Threading.Tasks.Task:
        ...

    @typing.overload
    def FlushAsync(self, ) -> System.Threading.Tasks.Task:
        ...

    @typing.overload
    @staticmethod
    def Synchronized(writer: System.IO.TextWriter, ) -> System.IO.TextWriter:
        ...

class FileAccess(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    Read: System.Int32 = Read
    Write: System.Int32 = Write
    ReadWrite: System.Int32 = ReadWrite

class FileMode(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    CreateNew: System.Int32 = CreateNew
    Create: System.Int32 = Create
    Open: System.Int32 = Open
    OpenOrCreate: System.Int32 = OpenOrCreate
    Truncate: System.Int32 = Truncate
    Append: System.Int32 = Append

class FileShare(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    None_: System.Int32 = None
    Read: System.Int32 = Read
    Write: System.Int32 = Write
    ReadWrite: System.Int32 = ReadWrite
    Delete: System.Int32 = Delete
    Inheritable: System.Int32 = Inheritable

class FileOptions(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    None_: System.Int32 = None
    Encrypted: System.Int32 = Encrypted
    DeleteOnClose: System.Int32 = DeleteOnClose
    SequentialScan: System.Int32 = SequentialScan
    RandomAccess: System.Int32 = RandomAccess
    Asynchronous: System.Int32 = Asynchronous
    WriteThrough: System.Int32 = WriteThrough

class FileStreamOptions(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def Mode(self) -> System.IO.FileMode:
        ...
    @Mode.setter
    def Mode(self, val: System.IO.FileMode):
        ...

    @property
    def Access(self) -> System.IO.FileAccess:
        ...
    @Access.setter
    def Access(self, val: System.IO.FileAccess):
        ...

    @property
    def Share(self) -> System.IO.FileShare:
        ...
    @Share.setter
    def Share(self, val: System.IO.FileShare):
        ...

    @property
    def Options(self) -> System.IO.FileOptions:
        ...
    @Options.setter
    def Options(self, val: System.IO.FileOptions):
        ...

    @property
    def PreallocationSize(self) -> System.Int64:
        ...
    @PreallocationSize.setter
    def PreallocationSize(self, val: System.Int64):
        ...

    @property
    def BufferSize(self) -> System.Int32:
        ...
    @BufferSize.setter
    def BufferSize(self, val: System.Int32):
        ...

    # methods
    @typing.overload
    def __init__(self, ):
        ...

