from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import System
import Microsoft.Win32.SafeHandles
import System.Runtime.ConstrainedExecution
import System.Runtime.InteropServices

T = typing.TypeVar('T')

class CharSet(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    None_: int = ...
    Ansi: int = ...
    Unicode: int = ...
    Auto: int = ...

class SafeBuffer(System.IDisposable, Microsoft.Win32.SafeHandles.SafeHandleZeroOrMinusOneIsInvalid, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        self.handle: System.IntPtr
        ...

    # static fields

    # properties
    @property
    def Uninitialized(self) -> System.UIntPtr:
        ...

    @property
    def ByteLength(self) -> int:
        ...

    @property
    def IsInvalid(self) -> bool:
        ...

    @property
    def IsClosed(self) -> bool:
        ...

    # methods
    def __init__(self, ownsHandle: bool, ):
        ...

    @typing.overload
    def Initialize(self, numBytes: int, ) -> None:
        ...

    @typing.overload
    def Initialize(self, numElements: int, sizeOfEachElement: int, ) -> None:
        ...

    @typing.overload
    def Initialize(self, numElements: int, ) -> None:
        ...

    def AcquirePointer(self, pointer: ref[ptr[int]], ) -> None:
        ...

    def ReleasePointer(self, ) -> None:
        ...

    def Read(self, byteOffset: int, ) -> T:
        ...

    def ReadArray(self, byteOffset: int, array: System.Array[T], index: int, count: int, ) -> None:
        ...

    def ReadSpan(self, byteOffset: int, buffer: System.Span[T], ) -> None:
        ...

    def Write(self, byteOffset: int, value: T, ) -> None:
        ...

    def WriteArray(self, byteOffset: int, array: System.Array[T], index: int, count: int, ) -> None:
        ...

    def WriteSpan(self, byteOffset: int, data: System.ReadOnlySpan[T], ) -> None:
        ...

    def SpaceCheck(self, ptr: ptr[int], sizeInBytes: System.UIntPtr, ) -> None:
        ...

    @staticmethod
    def NotEnoughRoom() -> None:
        ...

    @staticmethod
    def NotInitialized() -> System.InvalidOperationException:
        ...

    @staticmethod
    def AlignedSizeOf() -> int:
        ...

    @staticmethod
    def SizeOf() -> int:
        ...

class CallingConvention(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    Winapi: int = ...
    Cdecl: int = ...
    StdCall: int = ...
    ThisCall: int = ...
    FastCall: int = ...

class StructLayoutAttribute(System.Attribute):
    @typing.overload
    def __init__(self, **kwargs):
        self.Pack: int
        self.Size: int
        self.CharSet: int
        ...

    # static fields

    # properties
    @property
    def Value(self) -> int:
        ...

    @property
    def TypeId(self) -> System.Object:
        ...

    # methods
    @typing.overload
    def __init__(self, layoutKind: int, ):
        ...

    @typing.overload
    def __init__(self, layoutKind: int, ):
        ...

class LayoutKind(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    Sequential: int = ...
    Explicit: int = ...
    Auto: int = ...

class SafeHandle(System.IDisposable, System.Runtime.ConstrainedExecution.CriticalFinalizerObject, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        self.handle: System.IntPtr
        ...

    # static fields

    # properties
    @property
    def IsClosed(self) -> bool:
        ...

    @property
    @abc.abstractmethod
    def IsInvalid(self) -> bool:
        ...

    # methods
    def __init__(self, invalidHandleValue: System.IntPtr, ownsHandle: bool, ):
        ...

    def Finalize(self, ) -> None:
        ...

    def SetHandle(self, handle: System.IntPtr, ) -> None:
        ...

    def DangerousGetHandle(self, ) -> System.IntPtr:
        ...

    def Close(self, ) -> None:
        ...

    @typing.overload
    def Dispose(self, ) -> None:
        ...

    @typing.overload
    def Dispose(self, disposing: bool, ) -> None:
        ...

    def SetHandleAsInvalid(self, ) -> None:
        ...

    @abc.abstractmethod
    def ReleaseHandle(self, ) -> bool:
        ...

    def DangerousAddRef(self, success: ref[bool], ) -> None:
        ...

    def DangerousRelease(self, ) -> None:
        ...

    def InternalRelease(self, disposeOrFinalizeOperation: bool, ) -> None:
        ...

class GCHandle(System.ValueType):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def Target(self) -> System.Object:
        ...
    @Target.setter
    def Target(self, val: System.Object):
        ...

    @property
    def IsAllocated(self) -> bool:
        ...

    # methods
    @typing.overload
    def __init__(self, value: System.Object, type: int, ):
        ...

    @typing.overload
    def __init__(self, handle: System.IntPtr, ):
        ...

    @staticmethod
    def InternalAlloc(value: System.Object, type: int, ) -> System.IntPtr:
        ...

    @staticmethod
    def InternalFree(handle: System.IntPtr, ) -> None:
        ...

    @staticmethod
    def InternalGet(handle: System.IntPtr, ) -> System.Object:
        ...

    @staticmethod
    def InternalSet(handle: System.IntPtr, value: System.Object, ) -> None:
        ...

    @staticmethod
    def InternalCompareExchange(handle: System.IntPtr, value: System.Object, oldValue: System.Object, ) -> System.Object:
        ...

    @staticmethod
    @typing.overload
    def Alloc(value: System.Object, ) -> System.Runtime.InteropServices.GCHandle:
        ...

    @staticmethod
    @typing.overload
    def Alloc(value: System.Object, type: int, ) -> System.Runtime.InteropServices.GCHandle:
        ...

    def Free(self, ) -> None:
        ...

    def AddrOfPinnedObject(self, ) -> System.IntPtr:
        ...

    @staticmethod
    def FromIntPtr(value: System.IntPtr, ) -> System.Runtime.InteropServices.GCHandle:
        ...

    @staticmethod
    def ToIntPtr(value: System.Runtime.InteropServices.GCHandle, ) -> System.IntPtr:
        ...

    def GetHashCode(self, ) -> int:
        ...

    def Equals(self, o: System.Object, ) -> bool:
        ...

    @staticmethod
    def GetHandleValue(handle: System.IntPtr, ) -> System.IntPtr:
        ...

    @staticmethod
    def IsPinned(handle: System.IntPtr, ) -> bool:
        ...

    @staticmethod
    def ThrowIfInvalid(handle: System.IntPtr, ) -> None:
        ...

class GCHandleType(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    Weak: int = ...
    WeakTrackResurrection: int = ...
    Normal: int = ...
    Pinned: int = ...

