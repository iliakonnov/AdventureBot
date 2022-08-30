from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import System
import System.Runtime.InteropServices

T = typing.TypeVar('T')

class sqlite3_stmt(System.IDisposable, System.Runtime.InteropServices.SafeHandle):
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
    def manual_close(self, ) -> System.Int32:
        ...

class sqlite3(System.IDisposable, System.Runtime.InteropServices.SafeHandle):
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
    def manual_close_v2(self, ) -> System.Int32:
        ...

    @typing.overload
    def manual_close(self, ) -> System.Int32:
        ...

    @typing.overload
    def enable_sqlite3_next_stmt(self, enabled: System.Boolean, ) -> None:
        ...

    @typing.overload
    def GetOrCreateExtra(self, f: System.Func[T], ) -> T:
        ...

