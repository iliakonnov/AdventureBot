from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import System
import System.Threading
import System.IO
import System.Threading.Tasks
import System.IO.Stream
import Microsoft.Win32.SafeHandles
import System.Text


class Stream(System.IDisposable, System.IAsyncDisposable, System.MarshalByRefObject, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        self._asyncActiveSemaphore: System.Threading.SemaphoreSlim
        ...

    # static fields
    Null: System.IO.Stream = ...

    # properties
    @property
    @abc.abstractmethod
    def CanRead(self) -> bool:
        ...

    @property
    @abc.abstractmethod
    def CanWrite(self) -> bool:
        ...

    @property
    @abc.abstractmethod
    def CanSeek(self) -> bool:
        ...

    @property
    def CanTimeout(self) -> bool:
        ...

    @property
    @abc.abstractmethod
    def Length(self) -> int:
        ...

    @property
    @abc.abstractmethod
    def Position(self) -> int:
        ...
    @Position.setter
    @abc.abstractmethod
    def Position(self, val: int):
        ...

    @property
    def ReadTimeout(self) -> int:
        ...
    @ReadTimeout.setter
    def ReadTimeout(self, val: int):
        ...

    @property
    def WriteTimeout(self) -> int:
        ...
    @WriteTimeout.setter
    def WriteTimeout(self, val: int):
        ...

    # methods
    def __init__(self, ):
        ...

    def HasOverriddenBeginEndRead(self, ) -> bool:
        ...

    def HasOverriddenBeginEndWrite(self, ) -> bool:
        ...

    def EnsureAsyncActiveSemaphoreInitialized(self, ) -> System.Threading.SemaphoreSlim:
        ...

    @typing.overload
    def CopyTo(self, destination: System.IO.Stream, ) -> None:
        ...

    @typing.overload
    def CopyTo(self, destination: System.IO.Stream, bufferSize: int, ) -> None:
        ...

    @typing.overload
    def CopyToAsync(self, destination: System.IO.Stream, ) -> System.Threading.Tasks.Task:
        ...

    @typing.overload
    def CopyToAsync(self, destination: System.IO.Stream, bufferSize: int, ) -> System.Threading.Tasks.Task:
        ...

    @typing.overload
    def CopyToAsync(self, destination: System.IO.Stream, cancellationToken: System.Threading.CancellationToken, ) -> System.Threading.Tasks.Task:
        ...

    @typing.overload
    def CopyToAsync(self, destination: System.IO.Stream, bufferSize: int, cancellationToken: System.Threading.CancellationToken, ) -> System.Threading.Tasks.Task:
        ...

    def GetCopyBufferSize(self, ) -> int:
        ...

    @typing.overload
    def Dispose(self, ) -> None:
        ...

    @typing.overload
    def Dispose(self, disposing: bool, ) -> None:
        ...

    def Close(self, ) -> None:
        ...

    def DisposeAsync(self, ) -> System.Threading.Tasks.ValueTask:
        ...

    @abc.abstractmethod
    def Flush(self, ) -> None:
        ...

    @typing.overload
    def FlushAsync(self, ) -> System.Threading.Tasks.Task:
        ...

    @typing.overload
    def FlushAsync(self, cancellationToken: System.Threading.CancellationToken, ) -> System.Threading.Tasks.Task:
        ...

    def CreateWaitHandle(self, ) -> System.Threading.WaitHandle:
        ...

    def BeginRead(self, buffer: System.Array[int], offset: int, count: int, callback: System.AsyncCallback, state: System.Object, ) -> System.IAsyncResult:
        ...

    def BeginReadInternal(self, buffer: System.Array[int], offset: int, count: int, callback: System.AsyncCallback, state: System.Object, serializeAsynchronously: bool, apm: bool, ) -> System.Threading.Tasks.Task[int]:
        ...

    def EndRead(self, asyncResult: System.IAsyncResult, ) -> int:
        ...

    @typing.overload
    def ReadAsync(self, buffer: System.Array[int], offset: int, count: int, ) -> System.Threading.Tasks.Task[int]:
        ...

    @typing.overload
    def ReadAsync(self, buffer: System.Array[int], offset: int, count: int, cancellationToken: System.Threading.CancellationToken, ) -> System.Threading.Tasks.Task[int]:
        ...

    @typing.overload
    def ReadAsync(self, buffer: System.Memory[int], cancellationToken: System.Threading.CancellationToken = ..., ) -> System.Threading.Tasks.ValueTask[int]:
        ...

    def BeginEndReadAsync(self, buffer: System.Array[int], offset: int, count: int, ) -> System.Threading.Tasks.Task[int]:
        ...

    def BeginWrite(self, buffer: System.Array[int], offset: int, count: int, callback: System.AsyncCallback, state: System.Object, ) -> System.IAsyncResult:
        ...

    def BeginWriteInternal(self, buffer: System.Array[int], offset: int, count: int, callback: System.AsyncCallback, state: System.Object, serializeAsynchronously: bool, apm: bool, ) -> System.Threading.Tasks.Task:
        ...

    @staticmethod
    def RunReadWriteTaskWhenReady(asyncWaiter: System.Threading.Tasks.Task, readWriteTask: System.IO.Stream.ReadWriteTask, ) -> None:
        ...

    @staticmethod
    def RunReadWriteTask(readWriteTask: System.IO.Stream.ReadWriteTask, ) -> None:
        ...

    def FinishTrackingAsyncOperation(self, task: System.IO.Stream.ReadWriteTask, ) -> None:
        ...

    def EndWrite(self, asyncResult: System.IAsyncResult, ) -> None:
        ...

    @typing.overload
    def WriteAsync(self, buffer: System.Array[int], offset: int, count: int, ) -> System.Threading.Tasks.Task:
        ...

    @typing.overload
    def WriteAsync(self, buffer: System.Array[int], offset: int, count: int, cancellationToken: System.Threading.CancellationToken, ) -> System.Threading.Tasks.Task:
        ...

    @typing.overload
    def WriteAsync(self, buffer: System.ReadOnlyMemory[int], cancellationToken: System.Threading.CancellationToken = ..., ) -> System.Threading.Tasks.ValueTask:
        ...

    @staticmethod
    def FinishWriteAsync(writeTask: System.Threading.Tasks.Task, localBuffer: System.Array[int], ) -> System.Threading.Tasks.Task:
        ...

    def BeginEndWriteAsync(self, buffer: System.Array[int], offset: int, count: int, ) -> System.Threading.Tasks.Task:
        ...

    @abc.abstractmethod
    def Seek(self, offset: int, origin: int, ) -> int:
        ...

    @abc.abstractmethod
    def SetLength(self, value: int, ) -> None:
        ...

    @abc.abstractmethod
    @typing.overload
    def Read(self, buffer: System.Array[int], offset: int, count: int, ) -> int:
        ...

    @typing.overload
    def Read(self, buffer: System.Span[int], ) -> int:
        ...

    def ReadByte(self, ) -> int:
        ...

    @abc.abstractmethod
    @typing.overload
    def Write(self, buffer: System.Array[int], offset: int, count: int, ) -> None:
        ...

    @typing.overload
    def Write(self, buffer: System.ReadOnlySpan[int], ) -> None:
        ...

    def WriteByte(self, value: int, ) -> None:
        ...

    @staticmethod
    def Synchronized(stream: System.IO.Stream, ) -> System.IO.Stream:
        ...

    def ObjectInvariant(self, ) -> None:
        ...

    @staticmethod
    def ValidateBufferArguments(buffer: System.Array[int], offset: int, count: int, ) -> None:
        ...

    @staticmethod
    def ValidateCopyToArguments(destination: System.IO.Stream, bufferSize: int, ) -> None:
        ...

class SeekOrigin(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    Begin: int = ...
    Current: int = ...
    End: int = ...

class FileMode(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    CreateNew: int = ...
    Create: int = ...
    Open: int = ...
    OpenOrCreate: int = ...
    Truncate: int = ...
    Append: int = ...

class FileShare(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    None_: int = ...
    Read: int = ...
    Write: int = ...
    ReadWrite: int = ...
    Delete: int = ...
    Inheritable: int = ...

class FileStream(System.IDisposable, System.IAsyncDisposable, System.IO.Stream):
    @typing.overload
    def __init__(self, **kwargs):
        self._asyncActiveSemaphore: System.Threading.SemaphoreSlim
        ...

    # static fields

    # properties
    @property
    def Handle(self) -> System.IntPtr:
        ...

    @property
    def CanRead(self) -> bool:
        ...

    @property
    def CanWrite(self) -> bool:
        ...

    @property
    def SafeFileHandle(self) -> Microsoft.Win32.SafeHandles.SafeFileHandle:
        ...

    @property
    def Name(self) -> str:
        ...

    @property
    def IsAsync(self) -> bool:
        ...

    @property
    def Length(self) -> int:
        ...

    @property
    def Position(self) -> int:
        ...
    @Position.setter
    def Position(self, val: int):
        ...

    @property
    def CanSeek(self) -> bool:
        ...

    @property
    def CanTimeout(self) -> bool:
        ...

    @property
    def ReadTimeout(self) -> int:
        ...
    @ReadTimeout.setter
    def ReadTimeout(self, val: int):
        ...

    @property
    def WriteTimeout(self) -> int:
        ...
    @WriteTimeout.setter
    def WriteTimeout(self, val: int):
        ...

    # methods
    @typing.overload
    def __init__(self, handle: System.IntPtr, access: int, ):
        ...

    @typing.overload
    def __init__(self, handle: System.IntPtr, access: int, ownsHandle: bool, ):
        ...

    @typing.overload
    def __init__(self, handle: System.IntPtr, access: int, ownsHandle: bool, bufferSize: int, ):
        ...

    @typing.overload
    def __init__(self, handle: System.IntPtr, access: int, ownsHandle: bool, bufferSize: int, isAsync: bool, ):
        ...

    @typing.overload
    def __init__(self, handle: Microsoft.Win32.SafeHandles.SafeFileHandle, access: int, ):
        ...

    @typing.overload
    def __init__(self, handle: Microsoft.Win32.SafeHandles.SafeFileHandle, access: int, bufferSize: int, ):
        ...

    @typing.overload
    def __init__(self, handle: Microsoft.Win32.SafeHandles.SafeFileHandle, access: int, bufferSize: int, isAsync: bool, ):
        ...

    @typing.overload
    def __init__(self, path: str, mode: int, ):
        ...

    @typing.overload
    def __init__(self, path: str, mode: int, access: int, ):
        ...

    @typing.overload
    def __init__(self, path: str, mode: int, access: int, share: int, ):
        ...

    @typing.overload
    def __init__(self, path: str, mode: int, access: int, share: int, bufferSize: int, ):
        ...

    @typing.overload
    def __init__(self, path: str, mode: int, access: int, share: int, bufferSize: int, useAsync: bool, ):
        ...

    @typing.overload
    def __init__(self, path: str, mode: int, access: int, share: int, bufferSize: int, options: int, ):
        ...

    @typing.overload
    def __init__(self, path: str, options: System.IO.FileStreamOptions, ):
        ...

    @typing.overload
    def __init__(self, path: str, mode: int, access: int, share: int, bufferSize: int, options: int, preallocationSize: int, ):
        ...

    @staticmethod
    @typing.overload
    def ValidateHandle(handle: Microsoft.Win32.SafeHandles.SafeFileHandle, access: int, bufferSize: int, ) -> None:
        ...

    @staticmethod
    @typing.overload
    def ValidateHandle(handle: Microsoft.Win32.SafeHandles.SafeFileHandle, access: int, bufferSize: int, isAsync: bool, ) -> None:
        ...

    def Lock(self, position: int, length: int, ) -> None:
        ...

    def Unlock(self, position: int, length: int, ) -> None:
        ...

    def FlushAsync(self, cancellationToken: System.Threading.CancellationToken, ) -> System.Threading.Tasks.Task:
        ...

    @typing.overload
    def Read(self, buffer: System.Array[int], offset: int, count: int, ) -> int:
        ...

    @typing.overload
    def Read(self, buffer: System.Span[int], ) -> int:
        ...

    @typing.overload
    def ReadAsync(self, buffer: System.Array[int], offset: int, count: int, cancellationToken: System.Threading.CancellationToken, ) -> System.Threading.Tasks.Task[int]:
        ...

    @typing.overload
    def ReadAsync(self, buffer: System.Memory[int], cancellationToken: System.Threading.CancellationToken = ..., ) -> System.Threading.Tasks.ValueTask[int]:
        ...

    @typing.overload
    def Write(self, buffer: System.Array[int], offset: int, count: int, ) -> None:
        ...

    @typing.overload
    def Write(self, buffer: System.ReadOnlySpan[int], ) -> None:
        ...

    @typing.overload
    def WriteAsync(self, buffer: System.Array[int], offset: int, count: int, cancellationToken: System.Threading.CancellationToken, ) -> System.Threading.Tasks.Task:
        ...

    @typing.overload
    def WriteAsync(self, buffer: System.ReadOnlyMemory[int], cancellationToken: System.Threading.CancellationToken = ..., ) -> System.Threading.Tasks.ValueTask:
        ...

    @typing.overload
    def Flush(self, ) -> None:
        ...

    @typing.overload
    def Flush(self, flushToDisk: bool, ) -> None:
        ...

    def ValidateReadWriteArgs(self, buffer: System.Array[int], offset: int, count: int, ) -> None:
        ...

    def SetLength(self, value: int, ) -> None:
        ...

    def ReadByte(self, ) -> int:
        ...

    def WriteByte(self, value: int, ) -> None:
        ...

    def Dispose(self, disposing: bool, ) -> None:
        ...

    def DisposeInternal(self, disposing: bool, ) -> None:
        ...

    def DisposeAsync(self, ) -> System.Threading.Tasks.ValueTask:
        ...

    def CopyTo(self, destination: System.IO.Stream, bufferSize: int, ) -> None:
        ...

    def CopyToAsync(self, destination: System.IO.Stream, bufferSize: int, cancellationToken: System.Threading.CancellationToken, ) -> System.Threading.Tasks.Task:
        ...

    def BeginRead(self, buffer: System.Array[int], offset: int, count: int, callback: System.AsyncCallback, state: System.Object, ) -> System.IAsyncResult:
        ...

    def EndRead(self, asyncResult: System.IAsyncResult, ) -> int:
        ...

    def BeginWrite(self, buffer: System.Array[int], offset: int, count: int, callback: System.AsyncCallback, state: System.Object, ) -> System.IAsyncResult:
        ...

    def EndWrite(self, asyncResult: System.IAsyncResult, ) -> None:
        ...

    def Seek(self, offset: int, origin: int, ) -> int:
        ...

    def BaseFlushAsync(self, cancellationToken: System.Threading.CancellationToken, ) -> System.Threading.Tasks.Task:
        ...

    def BaseRead(self, buffer: System.Span[int], ) -> int:
        ...

    @typing.overload
    def BaseReadAsync(self, buffer: System.Array[int], offset: int, count: int, cancellationToken: System.Threading.CancellationToken, ) -> System.Threading.Tasks.Task[int]:
        ...

    @typing.overload
    def BaseReadAsync(self, buffer: System.Memory[int], cancellationToken: System.Threading.CancellationToken = ..., ) -> System.Threading.Tasks.ValueTask[int]:
        ...

    def BaseWrite(self, buffer: System.ReadOnlySpan[int], ) -> None:
        ...

    @typing.overload
    def BaseWriteAsync(self, buffer: System.Array[int], offset: int, count: int, cancellationToken: System.Threading.CancellationToken, ) -> System.Threading.Tasks.Task:
        ...

    @typing.overload
    def BaseWriteAsync(self, buffer: System.ReadOnlyMemory[int], cancellationToken: System.Threading.CancellationToken = ..., ) -> System.Threading.Tasks.ValueTask:
        ...

    def BaseDisposeAsync(self, ) -> System.Threading.Tasks.ValueTask:
        ...

    def BaseCopyToAsync(self, destination: System.IO.Stream, bufferSize: int, cancellationToken: System.Threading.CancellationToken, ) -> System.Threading.Tasks.Task:
        ...

    def BaseBeginRead(self, buffer: System.Array[int], offset: int, count: int, callback: System.AsyncCallback, state: System.Object, ) -> System.IAsyncResult:
        ...

    def BaseEndRead(self, asyncResult: System.IAsyncResult, ) -> int:
        ...

    def BaseBeginWrite(self, buffer: System.Array[int], offset: int, count: int, callback: System.AsyncCallback, state: System.Object, ) -> System.IAsyncResult:
        ...

    def BaseEndWrite(self, asyncResult: System.IAsyncResult, ) -> None:
        ...

class FileOptions(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    None_: int = ...
    Encrypted: int = ...
    DeleteOnClose: int = ...
    SequentialScan: int = ...
    RandomAccess: int = ...
    Asynchronous: int = ...
    WriteThrough: int = ...

class FileStreamOptions(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def Mode(self) -> int:
        ...
    @Mode.setter
    def Mode(self, val: int):
        ...

    @property
    def Access(self) -> int:
        ...
    @Access.setter
    def Access(self, val: int):
        ...

    @property
    def Share(self) -> int:
        ...
    @Share.setter
    def Share(self, val: int):
        ...

    @property
    def Options(self) -> int:
        ...
    @Options.setter
    def Options(self, val: int):
        ...

    @property
    def PreallocationSize(self) -> int:
        ...
    @PreallocationSize.setter
    def PreallocationSize(self, val: int):
        ...

    @property
    def BufferSize(self) -> int:
        ...
    @BufferSize.setter
    def BufferSize(self, val: int):
        ...

    # methods
    def __init__(self, ):
        ...

class FileAccess(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    Read: int = ...
    Write: int = ...
    ReadWrite: int = ...

class TextReader(System.IDisposable, System.MarshalByRefObject, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields
    Null: System.IO.TextReader = ...

    # properties
    # methods
    def __init__(self, ):
        ...

    def Close(self, ) -> None:
        ...

    @typing.overload
    def Dispose(self, ) -> None:
        ...

    @typing.overload
    def Dispose(self, disposing: bool, ) -> None:
        ...

    def Peek(self, ) -> int:
        ...

    @typing.overload
    def Read(self, ) -> int:
        ...

    @typing.overload
    def Read(self, buffer: System.Array[str], index: int, count: int, ) -> int:
        ...

    @typing.overload
    def Read(self, buffer: System.Span[str], ) -> int:
        ...

    def ReadToEnd(self, ) -> str:
        ...

    @typing.overload
    def ReadBlock(self, buffer: System.Array[str], index: int, count: int, ) -> int:
        ...

    @typing.overload
    def ReadBlock(self, buffer: System.Span[str], ) -> int:
        ...

    def ReadLine(self, ) -> str:
        ...

    def ReadLineAsync(self, ) -> System.Threading.Tasks.Task[str]:
        ...

    def ReadToEndAsync(self, ) -> System.Threading.Tasks.Task[str]:
        ...

    @typing.overload
    def ReadAsync(self, buffer: System.Array[str], index: int, count: int, ) -> System.Threading.Tasks.Task[int]:
        ...

    @typing.overload
    def ReadAsync(self, buffer: System.Memory[str], cancellationToken: System.Threading.CancellationToken = ..., ) -> System.Threading.Tasks.ValueTask[int]:
        ...

    def ReadAsyncInternal(self, buffer: System.Memory[str], cancellationToken: System.Threading.CancellationToken, ) -> System.Threading.Tasks.ValueTask[int]:
        ...

    @typing.overload
    def ReadBlockAsync(self, buffer: System.Array[str], index: int, count: int, ) -> System.Threading.Tasks.Task[int]:
        ...

    @typing.overload
    def ReadBlockAsync(self, buffer: System.Memory[str], cancellationToken: System.Threading.CancellationToken = ..., ) -> System.Threading.Tasks.ValueTask[int]:
        ...

    def ReadBlockAsyncInternal(self, buffer: System.Memory[str], cancellationToken: System.Threading.CancellationToken, ) -> System.Threading.Tasks.ValueTask[int]:
        ...

    @staticmethod
    def Synchronized(reader: System.IO.TextReader, ) -> System.IO.TextReader:
        ...

class StringWriter(System.IDisposable, System.IAsyncDisposable, System.IO.TextWriter):
    @typing.overload
    def __init__(self, **kwargs):
        self.CoreNewLine: System.Array[str]
        ...

    # static fields

    # properties
    @property
    def Encoding(self) -> System.Text.Encoding:
        ...

    @property
    def FormatProvider(self) -> System.IFormatProvider:
        ...

    @property
    def NewLine(self) -> str:
        ...
    @NewLine.setter
    def NewLine(self, val: str):
        ...

    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def __init__(self, formatProvider: System.IFormatProvider, ):
        ...

    @typing.overload
    def __init__(self, sb: System.Text.StringBuilder, ):
        ...

    @typing.overload
    def __init__(self, sb: System.Text.StringBuilder, formatProvider: System.IFormatProvider, ):
        ...

    def Close(self, ) -> None:
        ...

    def Dispose(self, disposing: bool, ) -> None:
        ...

    def GetStringBuilder(self, ) -> System.Text.StringBuilder:
        ...

    @typing.overload
    def Write(self, value: str, ) -> None:
        ...

    @typing.overload
    def Write(self, buffer: System.Array[str], index: int, count: int, ) -> None:
        ...

    @typing.overload
    def Write(self, buffer: System.ReadOnlySpan[str], ) -> None:
        ...

    @typing.overload
    def Write(self, value: str, ) -> None:
        ...

    @typing.overload
    def Write(self, value: System.Text.StringBuilder, ) -> None:
        ...

    @typing.overload
    def WriteLine(self, buffer: System.ReadOnlySpan[str], ) -> None:
        ...

    @typing.overload
    def WriteLine(self, value: System.Text.StringBuilder, ) -> None:
        ...

    @typing.overload
    def WriteAsync(self, value: str, ) -> System.Threading.Tasks.Task:
        ...

    @typing.overload
    def WriteAsync(self, value: str, ) -> System.Threading.Tasks.Task:
        ...

    @typing.overload
    def WriteAsync(self, buffer: System.Array[str], index: int, count: int, ) -> System.Threading.Tasks.Task:
        ...

    @typing.overload
    def WriteAsync(self, buffer: System.ReadOnlyMemory[str], cancellationToken: System.Threading.CancellationToken = ..., ) -> System.Threading.Tasks.Task:
        ...

    @typing.overload
    def WriteAsync(self, value: System.Text.StringBuilder, cancellationToken: System.Threading.CancellationToken = ..., ) -> System.Threading.Tasks.Task:
        ...

    @typing.overload
    def WriteLineAsync(self, value: str, ) -> System.Threading.Tasks.Task:
        ...

    @typing.overload
    def WriteLineAsync(self, value: str, ) -> System.Threading.Tasks.Task:
        ...

    @typing.overload
    def WriteLineAsync(self, value: System.Text.StringBuilder, cancellationToken: System.Threading.CancellationToken = ..., ) -> System.Threading.Tasks.Task:
        ...

    @typing.overload
    def WriteLineAsync(self, buffer: System.Array[str], index: int, count: int, ) -> System.Threading.Tasks.Task:
        ...

    @typing.overload
    def WriteLineAsync(self, buffer: System.ReadOnlyMemory[str], cancellationToken: System.Threading.CancellationToken = ..., ) -> System.Threading.Tasks.Task:
        ...

    def FlushAsync(self, ) -> System.Threading.Tasks.Task:
        ...

    def ToString(self, ) -> str:
        ...

class StreamReader(System.IDisposable, System.IO.TextReader):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields
    Null: System.IO.StreamReader = ...

    # properties
    @property
    def CurrentEncoding(self) -> System.Text.Encoding:
        ...

    @property
    def BaseStream(self) -> System.IO.Stream:
        ...

    @property
    def EndOfStream(self) -> bool:
        ...

    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def __init__(self, stream: System.IO.Stream, ):
        ...

    @typing.overload
    def __init__(self, stream: System.IO.Stream, detectEncodingFromByteOrderMarks: bool, ):
        ...

    @typing.overload
    def __init__(self, stream: System.IO.Stream, encoding: System.Text.Encoding, ):
        ...

    @typing.overload
    def __init__(self, stream: System.IO.Stream, encoding: System.Text.Encoding, detectEncodingFromByteOrderMarks: bool, ):
        ...

    @typing.overload
    def __init__(self, stream: System.IO.Stream, encoding: System.Text.Encoding, detectEncodingFromByteOrderMarks: bool, bufferSize: int, ):
        ...

    @typing.overload
    def __init__(self, stream: System.IO.Stream, encoding: System.Text.Encoding = ..., detectEncodingFromByteOrderMarks: bool = ..., bufferSize: int = ..., leaveOpen: bool = ..., ):
        ...

    @typing.overload
    def __init__(self, path: str, ):
        ...

    @typing.overload
    def __init__(self, path: str, detectEncodingFromByteOrderMarks: bool, ):
        ...

    @typing.overload
    def __init__(self, path: str, encoding: System.Text.Encoding, ):
        ...

    @typing.overload
    def __init__(self, path: str, encoding: System.Text.Encoding, detectEncodingFromByteOrderMarks: bool, ):
        ...

    @typing.overload
    def __init__(self, path: str, encoding: System.Text.Encoding, detectEncodingFromByteOrderMarks: bool, bufferSize: int, ):
        ...

    @typing.overload
    def __init__(self, path: str, options: System.IO.FileStreamOptions, ):
        ...

    @typing.overload
    def __init__(self, path: str, encoding: System.Text.Encoding, detectEncodingFromByteOrderMarks: bool, options: System.IO.FileStreamOptions, ):
        ...

    def CheckAsyncTaskInProgress(self, ) -> None:
        ...

    @staticmethod
    def ThrowAsyncIOInProgress() -> None:
        ...

    @staticmethod
    @typing.overload
    def ValidateArgsAndOpenPath(path: str, encoding: System.Text.Encoding, options: System.IO.FileStreamOptions, ) -> System.IO.Stream:
        ...

    @staticmethod
    @typing.overload
    def ValidateArgsAndOpenPath(path: str, encoding: System.Text.Encoding, bufferSize: int, ) -> System.IO.Stream:
        ...

    @staticmethod
    def ValidateArgs(path: str, encoding: System.Text.Encoding, ) -> None:
        ...

    def Close(self, ) -> None:
        ...

    def Dispose(self, disposing: bool, ) -> None:
        ...

    def DiscardBufferedData(self, ) -> None:
        ...

    def Peek(self, ) -> int:
        ...

    @typing.overload
    def Read(self, ) -> int:
        ...

    @typing.overload
    def Read(self, buffer: System.Array[str], index: int, count: int, ) -> int:
        ...

    @typing.overload
    def Read(self, buffer: System.Span[str], ) -> int:
        ...

    def ReadSpan(self, buffer: System.Span[str], ) -> int:
        ...

    def ReadToEnd(self, ) -> str:
        ...

    @typing.overload
    def ReadBlock(self, buffer: System.Array[str], index: int, count: int, ) -> int:
        ...

    @typing.overload
    def ReadBlock(self, buffer: System.Span[str], ) -> int:
        ...

    def CompressBuffer(self, n: int, ) -> None:
        ...

    def DetectEncoding(self, ) -> None:
        ...

    def IsPreamble(self, ) -> bool:
        ...

    @typing.overload
    def ReadBuffer(self, ) -> int:
        ...

    @typing.overload
    def ReadBuffer(self, userBuffer: System.Span[str], readToUserBuffer: ref[bool], ) -> int:
        ...

    def ReadLine(self, ) -> str:
        ...

    def ReadLineAsync(self, ) -> System.Threading.Tasks.Task[str]:
        ...

    def ReadLineAsyncInternal(self, ) -> System.Threading.Tasks.Task[str]:
        ...

    def ReadToEndAsync(self, ) -> System.Threading.Tasks.Task[str]:
        ...

    def ReadToEndAsyncInternal(self, ) -> System.Threading.Tasks.Task[str]:
        ...

    @typing.overload
    def ReadAsync(self, buffer: System.Array[str], index: int, count: int, ) -> System.Threading.Tasks.Task[int]:
        ...

    @typing.overload
    def ReadAsync(self, buffer: System.Memory[str], cancellationToken: System.Threading.CancellationToken = ..., ) -> System.Threading.Tasks.ValueTask[int]:
        ...

    def ReadAsyncInternal(self, buffer: System.Memory[str], cancellationToken: System.Threading.CancellationToken, ) -> System.Threading.Tasks.ValueTask[int]:
        ...

    @typing.overload
    def ReadBlockAsync(self, buffer: System.Array[str], index: int, count: int, ) -> System.Threading.Tasks.Task[int]:
        ...

    @typing.overload
    def ReadBlockAsync(self, buffer: System.Memory[str], cancellationToken: System.Threading.CancellationToken = ..., ) -> System.Threading.Tasks.ValueTask[int]:
        ...

    def ReadBufferAsync(self, cancellationToken: System.Threading.CancellationToken, ) -> System.Threading.Tasks.ValueTask[int]:
        ...

    def ThrowIfDisposed(self, ) -> None:
        ...

class BinaryWriter(System.IDisposable, System.IAsyncDisposable, System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        self.OutStream: System.IO.Stream
        ...

    # static fields
    Null: System.IO.BinaryWriter = ...

    # properties
    @property
    def BaseStream(self) -> System.IO.Stream:
        ...

    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def __init__(self, output: System.IO.Stream, ):
        ...

    @typing.overload
    def __init__(self, output: System.IO.Stream, encoding: System.Text.Encoding, ):
        ...

    @typing.overload
    def __init__(self, output: System.IO.Stream, encoding: System.Text.Encoding, leaveOpen: bool, ):
        ...

    def Close(self, ) -> None:
        ...

    @typing.overload
    def Dispose(self, disposing: bool, ) -> None:
        ...

    @typing.overload
    def Dispose(self, ) -> None:
        ...

    def DisposeAsync(self, ) -> System.Threading.Tasks.ValueTask:
        ...

    def Flush(self, ) -> None:
        ...

    def Seek(self, offset: int, origin: int, ) -> int:
        ...

    @typing.overload
    def Write(self, value: bool, ) -> None:
        ...

    @typing.overload
    def Write(self, value: int, ) -> None:
        ...

    @typing.overload
    def Write(self, value: int, ) -> None:
        ...

    @typing.overload
    def Write(self, buffer: System.Array[int], ) -> None:
        ...

    @typing.overload
    def Write(self, buffer: System.Array[int], index: int, count: int, ) -> None:
        ...

    @typing.overload
    def Write(self, ch: str, ) -> None:
        ...

    @typing.overload
    def Write(self, chars: System.Array[str], ) -> None:
        ...

    @typing.overload
    def Write(self, chars: System.Array[str], index: int, count: int, ) -> None:
        ...

    @typing.overload
    def Write(self, value: float, ) -> None:
        ...

    @typing.overload
    def Write(self, value: System.Decimal, ) -> None:
        ...

    @typing.overload
    def Write(self, value: int, ) -> None:
        ...

    @typing.overload
    def Write(self, value: int, ) -> None:
        ...

    @typing.overload
    def Write(self, value: int, ) -> None:
        ...

    @typing.overload
    def Write(self, value: int, ) -> None:
        ...

    @typing.overload
    def Write(self, value: int, ) -> None:
        ...

    @typing.overload
    def Write(self, value: int, ) -> None:
        ...

    @typing.overload
    def Write(self, value: float, ) -> None:
        ...

    @typing.overload
    def Write(self, value: System.Half, ) -> None:
        ...

    @typing.overload
    def Write(self, value: str, ) -> None:
        ...

    @typing.overload
    def Write(self, buffer: System.ReadOnlySpan[int], ) -> None:
        ...

    @typing.overload
    def Write(self, chars: System.ReadOnlySpan[str], ) -> None:
        ...

    def WriteCharsCommonWithoutLengthPrefix(self, chars: System.ReadOnlySpan[str], useThisWriteOverride: bool, ) -> None:
        ...

    def Write7BitEncodedInt(self, value: int, ) -> None:
        ...

    def Write7BitEncodedInt64(self, value: int, ) -> None:
        ...

class TextWriter(System.IDisposable, System.IAsyncDisposable, System.MarshalByRefObject, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        self.CoreNewLine: System.Array[str]
        ...

    # static fields
    Null: System.IO.TextWriter = ...

    # properties
    @property
    def FormatProvider(self) -> System.IFormatProvider:
        ...

    @property
    @abc.abstractmethod
    def Encoding(self) -> System.Text.Encoding:
        ...

    @property
    def NewLine(self) -> str:
        ...
    @NewLine.setter
    def NewLine(self, val: str):
        ...

    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def __init__(self, formatProvider: System.IFormatProvider, ):
        ...

    def Close(self, ) -> None:
        ...

    @typing.overload
    def Dispose(self, disposing: bool, ) -> None:
        ...

    @typing.overload
    def Dispose(self, ) -> None:
        ...

    def DisposeAsync(self, ) -> System.Threading.Tasks.ValueTask:
        ...

    def Flush(self, ) -> None:
        ...

    @typing.overload
    def Write(self, value: str, ) -> None:
        ...

    @typing.overload
    def Write(self, buffer: System.Array[str], ) -> None:
        ...

    @typing.overload
    def Write(self, buffer: System.Array[str], index: int, count: int, ) -> None:
        ...

    @typing.overload
    def Write(self, buffer: System.ReadOnlySpan[str], ) -> None:
        ...

    @typing.overload
    def Write(self, value: bool, ) -> None:
        ...

    @typing.overload
    def Write(self, value: int, ) -> None:
        ...

    @typing.overload
    def Write(self, value: int, ) -> None:
        ...

    @typing.overload
    def Write(self, value: int, ) -> None:
        ...

    @typing.overload
    def Write(self, value: int, ) -> None:
        ...

    @typing.overload
    def Write(self, value: float, ) -> None:
        ...

    @typing.overload
    def Write(self, value: float, ) -> None:
        ...

    @typing.overload
    def Write(self, value: System.Decimal, ) -> None:
        ...

    @typing.overload
    def Write(self, value: str, ) -> None:
        ...

    @typing.overload
    def Write(self, value: System.Object, ) -> None:
        ...

    @typing.overload
    def Write(self, value: System.Text.StringBuilder, ) -> None:
        ...

    @typing.overload
    def Write(self, format: str, arg0: System.Object, ) -> None:
        ...

    @typing.overload
    def Write(self, format: str, arg0: System.Object, arg1: System.Object, ) -> None:
        ...

    @typing.overload
    def Write(self, format: str, arg0: System.Object, arg1: System.Object, arg2: System.Object, ) -> None:
        ...

    @typing.overload
    def Write(self, format: str, arg: System.Array[System.Object], ) -> None:
        ...

    @typing.overload
    def WriteLine(self, ) -> None:
        ...

    @typing.overload
    def WriteLine(self, value: str, ) -> None:
        ...

    @typing.overload
    def WriteLine(self, buffer: System.Array[str], ) -> None:
        ...

    @typing.overload
    def WriteLine(self, buffer: System.Array[str], index: int, count: int, ) -> None:
        ...

    @typing.overload
    def WriteLine(self, buffer: System.ReadOnlySpan[str], ) -> None:
        ...

    @typing.overload
    def WriteLine(self, value: bool, ) -> None:
        ...

    @typing.overload
    def WriteLine(self, value: int, ) -> None:
        ...

    @typing.overload
    def WriteLine(self, value: int, ) -> None:
        ...

    @typing.overload
    def WriteLine(self, value: int, ) -> None:
        ...

    @typing.overload
    def WriteLine(self, value: int, ) -> None:
        ...

    @typing.overload
    def WriteLine(self, value: float, ) -> None:
        ...

    @typing.overload
    def WriteLine(self, value: float, ) -> None:
        ...

    @typing.overload
    def WriteLine(self, value: System.Decimal, ) -> None:
        ...

    @typing.overload
    def WriteLine(self, value: str, ) -> None:
        ...

    @typing.overload
    def WriteLine(self, value: System.Text.StringBuilder, ) -> None:
        ...

    @typing.overload
    def WriteLine(self, value: System.Object, ) -> None:
        ...

    @typing.overload
    def WriteLine(self, format: str, arg0: System.Object, ) -> None:
        ...

    @typing.overload
    def WriteLine(self, format: str, arg0: System.Object, arg1: System.Object, ) -> None:
        ...

    @typing.overload
    def WriteLine(self, format: str, arg0: System.Object, arg1: System.Object, arg2: System.Object, ) -> None:
        ...

    @typing.overload
    def WriteLine(self, format: str, arg: System.Array[System.Object], ) -> None:
        ...

    @typing.overload
    def WriteAsync(self, value: str, ) -> System.Threading.Tasks.Task:
        ...

    @typing.overload
    def WriteAsync(self, value: str, ) -> System.Threading.Tasks.Task:
        ...

    @typing.overload
    def WriteAsync(self, value: System.Text.StringBuilder, cancellationToken: System.Threading.CancellationToken = ..., ) -> System.Threading.Tasks.Task:
        ...

    @typing.overload
    def WriteAsync(self, buffer: System.Array[str], ) -> System.Threading.Tasks.Task:
        ...

    @typing.overload
    def WriteAsync(self, buffer: System.Array[str], index: int, count: int, ) -> System.Threading.Tasks.Task:
        ...

    @typing.overload
    def WriteAsync(self, buffer: System.ReadOnlyMemory[str], cancellationToken: System.Threading.CancellationToken = ..., ) -> System.Threading.Tasks.Task:
        ...

    @typing.overload
    def WriteLineAsync(self, value: str, ) -> System.Threading.Tasks.Task:
        ...

    @typing.overload
    def WriteLineAsync(self, value: str, ) -> System.Threading.Tasks.Task:
        ...

    @typing.overload
    def WriteLineAsync(self, value: System.Text.StringBuilder, cancellationToken: System.Threading.CancellationToken = ..., ) -> System.Threading.Tasks.Task:
        ...

    @typing.overload
    def WriteLineAsync(self, buffer: System.Array[str], ) -> System.Threading.Tasks.Task:
        ...

    @typing.overload
    def WriteLineAsync(self, buffer: System.Array[str], index: int, count: int, ) -> System.Threading.Tasks.Task:
        ...

    @typing.overload
    def WriteLineAsync(self, buffer: System.ReadOnlyMemory[str], cancellationToken: System.Threading.CancellationToken = ..., ) -> System.Threading.Tasks.Task:
        ...

    @typing.overload
    def WriteLineAsync(self, ) -> System.Threading.Tasks.Task:
        ...

    def FlushAsync(self, ) -> System.Threading.Tasks.Task:
        ...

    @staticmethod
    def Synchronized(writer: System.IO.TextWriter, ) -> System.IO.TextWriter:
        ...

