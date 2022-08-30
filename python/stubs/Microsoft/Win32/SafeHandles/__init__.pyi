from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import System
import Microsoft.Win32.SafeHandles
import System.Runtime.InteropServices


class SafeWaitHandle(System.IDisposable, Microsoft.Win32.SafeHandles.SafeHandleZeroOrMinusOneIsInvalid):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def IsInvalid(self) -> System.Boolean:
        ...

    @property
    def IsClosed(self) -> System.Boolean:
        ...

    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def __init__(self, existingHandle: System.IntPtr, ownsHandle: System.Boolean, ):
        ...

class SafeFileHandle(System.IDisposable, Microsoft.Win32.SafeHandles.SafeHandleZeroOrMinusOneIsInvalid):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def IsAsync(self) -> System.Boolean:
        ...

    @property
    def IsInvalid(self) -> System.Boolean:
        ...

    @property
    def IsClosed(self) -> System.Boolean:
        ...

    # methods
    @typing.overload
    def __init__(self, preexistingHandle: System.IntPtr, ownsHandle: System.Boolean, ):
        ...

    @typing.overload
    def __init__(self, ):
        ...

class SafeHandleZeroOrMinusOneIsInvalid(System.IDisposable, System.Runtime.InteropServices.SafeHandle, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def IsInvalid(self) -> System.Boolean:
        ...

    @property
    def IsClosed(self) -> System.Boolean:
        ...

    # methods
