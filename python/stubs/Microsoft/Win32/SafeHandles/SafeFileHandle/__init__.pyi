from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import System.Threading
import System.Threading.Tasks.Sources
import System
import Microsoft.Win32.SafeHandles
import System.IO.Strategies
import System.Threading.Tasks
import System.Collections.Generic


class ThreadPoolValueTaskSource(System.Threading.IThreadPoolWorkItem, System.Threading.Tasks.Sources.IValueTaskSource[int], System.Threading.Tasks.Sources.IValueTaskSource[int], System.Threading.Tasks.Sources.IValueTaskSource, System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    def __init__(self, fileHandle: Microsoft.Win32.SafeHandles.SafeFileHandle, ):
        ...

    def GetStatus(self, token: int, ) -> int:
        ...

    def OnCompleted(self, continuation: System.Action[System.Object], state: System.Object, token: int, flags: int, ) -> None:
        ...

    def GetResult(self, token: int, ) -> None:
        ...

    def GetResult(self, token: int, ) -> int:
        ...

    def GetResult(self, token: int, ) -> int:
        ...

    def ExecuteInternal(self, ) -> None:
        ...

    def Execute(self, ) -> None:
        ...

    def QueueToThreadPool(self, ) -> None:
        ...

    def QueueRead(self, buffer: System.Memory[int], fileOffset: int, cancellationToken: System.Threading.CancellationToken, strategy: System.IO.Strategies.OSFileStreamStrategy, ) -> System.Threading.Tasks.ValueTask[int]:
        ...

    def QueueWrite(self, buffer: System.ReadOnlyMemory[int], fileOffset: int, cancellationToken: System.Threading.CancellationToken, strategy: System.IO.Strategies.OSFileStreamStrategy, ) -> System.Threading.Tasks.ValueTask:
        ...

    def QueueReadScatter(self, buffers: System.Collections.Generic.IReadOnlyList[System.Memory[int]], fileOffset: int, cancellationToken: System.Threading.CancellationToken, ) -> System.Threading.Tasks.ValueTask[int]:
        ...

    def QueueWriteGather(self, buffers: System.Collections.Generic.IReadOnlyList[System.ReadOnlyMemory[int]], fileOffset: int, cancellationToken: System.Threading.CancellationToken, ) -> System.Threading.Tasks.ValueTask:
        ...

