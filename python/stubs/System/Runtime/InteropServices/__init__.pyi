from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import System
import System.Runtime.InteropServices
import System.Runtime.ConstrainedExecution


class StructLayoutAttribute(System.Attribute):
    @typing.overload
    def __init__(self, **kwargs):
        self.Pack: System.Int32
        self.Size: System.Int32
        self.CharSet: System.Runtime.InteropServices.CharSet
        ...

    # properties
    @property
    def Value(self) -> System.Runtime.InteropServices.LayoutKind:
        ...

    @property
    def TypeId(self) -> System.Object:
        ...

    # methods
    @typing.overload
    def __init__(self, layoutKind: System.Runtime.InteropServices.LayoutKind, ):
        ...

    @typing.overload
    def __init__(self, layoutKind: System.Int16, ):
        ...

class CharSet(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    None_: System.Int32 = None
    Ansi: System.Int32 = Ansi
    Unicode: System.Int32 = Unicode
    Auto: System.Int32 = Auto

class LayoutKind(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    Sequential: System.Int32 = Sequential
    Explicit: System.Int32 = Explicit
    Auto: System.Int32 = Auto

class SafeHandle(System.IDisposable, System.Runtime.ConstrainedExecution.CriticalFinalizerObject, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def IsClosed(self) -> System.Boolean:
        ...

    @abc.abstractmethod
    @property
    def IsInvalid(self) -> System.Boolean:
        ...

    # methods
    @typing.overload
    def DangerousGetHandle(self, ) -> System.IntPtr:
        ...

    @typing.overload
    def Close(self, ) -> None:
        ...

    @typing.overload
    def Dispose(self, ) -> None:
        ...

    @typing.overload
    def SetHandleAsInvalid(self, ) -> None:
        ...

    @typing.overload
    def DangerousAddRef(self, success: ref[System.Boolean], ) -> None:
        ...

    @typing.overload
    def DangerousRelease(self, ) -> None:
        ...

class GCHandle(System.ValueType):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def Target(self) -> System.Object:
        ...
    @Target.setter
    def Target(self, val: System.Object):
        ...

    @property
    def IsAllocated(self) -> System.Boolean:
        ...

    # methods
    @typing.overload
    @staticmethod
    def Alloc(value: System.Object, ) -> System.Runtime.InteropServices.GCHandle:
        ...

    @typing.overload
    @staticmethod
    def Alloc(value: System.Object, type: System.Runtime.InteropServices.GCHandleType, ) -> System.Runtime.InteropServices.GCHandle:
        ...

    @typing.overload
    def Free(self, ) -> None:
        ...

    @typing.overload
    def AddrOfPinnedObject(self, ) -> System.IntPtr:
        ...

    @typing.overload
    @staticmethod
    def FromIntPtr(value: System.IntPtr, ) -> System.Runtime.InteropServices.GCHandle:
        ...

    @typing.overload
    @staticmethod
    def ToIntPtr(value: System.Runtime.InteropServices.GCHandle, ) -> System.IntPtr:
        ...

    @typing.overload
    def GetHashCode(self, ) -> System.Int32:
        ...

    @typing.overload
    def Equals(self, o: System.Object, ) -> System.Boolean:
        ...

class GCHandleType(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    Weak: System.Int32 = Weak
    WeakTrackResurrection: System.Int32 = WeakTrackResurrection
    Normal: System.Int32 = Normal
    Pinned: System.Int32 = Pinned

