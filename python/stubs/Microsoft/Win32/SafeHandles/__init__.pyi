from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import System
import Microsoft.Win32.SafeHandles
import Interop
import System.Threading
import Microsoft.Win32.SafeHandles.SafeFileHandle
import System.Runtime.InteropServices


class SafeFileHandle(System.IDisposable, Microsoft.Win32.SafeHandles.SafeHandleZeroOrMinusOneIsInvalid):
    @typing.overload
    def __init__(self, **kwargs):
        self.handle: System.IntPtr
        ...

    # static fields
    t_lastCloseErrorInfo: System.Nullable[Interop.ErrorInfo] = ...

    # properties
    @property
    def Path(self) -> str:
        ...

    @property
    def DisableFileLocking(self) -> bool:
        ...

    @property
    def IsAsync(self) -> bool:
        ...
    @IsAsync.setter
    def IsAsync(self, val: bool):
        ...

    @property
    def CanSeek(self) -> bool:
        ...

    @property
    def SupportsRandomAccess(self) -> bool:
        ...
    @SupportsRandomAccess.setter
    def SupportsRandomAccess(self, val: bool):
        ...

    @property
    def ThreadPoolBinding(self) -> System.Threading.ThreadPoolBoundHandle:
        ...

    @property
    def IsInvalid(self) -> bool:
        ...

    @property
    def IsClosed(self) -> bool:
        ...

    # methods
    @typing.overload
    def __init__(self, preexistingHandle: System.IntPtr, ownsHandle: bool, ):
        ...

    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def __init__(self, ownsHandle: bool, ):
        ...

    def GetThreadPoolValueTaskSource(self, ) -> Microsoft.Win32.SafeHandles.SafeFileHandle.ThreadPoolValueTaskSource:
        ...

    def EnsureThreadPoolBindingInitialized(self, ) -> None:
        ...

    @staticmethod
    @typing.overload
    def Open(path: str, flags: int, mode: int, ) -> Microsoft.Win32.SafeHandles.SafeFileHandle:
        ...

    @staticmethod
    @typing.overload
    def Open(fullPath: str, mode: int, access: int, share: int, options: int, preallocationSize: int, ) -> Microsoft.Win32.SafeHandles.SafeFileHandle:
        ...

    @staticmethod
    def DirectoryExists(fullPath: str, ) -> bool:
        ...

    def ReleaseHandle(self, ) -> bool:
        ...

    @staticmethod
    def PreOpenConfigurationFromOptions(mode: int, access: int, share: int, options: int, ) -> int:
        ...

    def Init(self, path: str, mode: int, access: int, share: int, options: int, preallocationSize: int, ) -> None:
        ...

    def CanLockTheFile(self, lockOperation: int, access: int, ) -> bool:
        ...

    def GetCanSeek(self, ) -> bool:
        ...

class SafeHandleZeroOrMinusOneIsInvalid(System.IDisposable, System.Runtime.InteropServices.SafeHandle, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        self.handle: System.IntPtr
        ...

    # static fields

    # properties
    @property
    def IsInvalid(self) -> bool:
        ...

    @property
    def IsClosed(self) -> bool:
        ...

    # methods
    def __init__(self, ownsHandle: bool, ):
        ...

class SafeWaitHandle(System.IDisposable, Microsoft.Win32.SafeHandles.SafeHandleZeroOrMinusOneIsInvalid):
    @typing.overload
    def __init__(self, **kwargs):
        self.handle: System.IntPtr
        ...

    # static fields

    # properties
    @property
    def IsInvalid(self) -> bool:
        ...

    @property
    def IsClosed(self) -> bool:
        ...

    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def __init__(self, existingHandle: System.IntPtr, ownsHandle: bool, ):
        ...

    def ReleaseHandle(self, ) -> bool:
        ...

