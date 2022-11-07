from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import System
import System.Runtime.InteropServices
import SQLitePCL

T = typing.TypeVar('T')

class sqlite3_stmt(System.IDisposable, System.Runtime.InteropServices.SafeHandle):
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
    def ptr(self) -> System.IntPtr:
        ...

    @property
    def db(self) -> SQLitePCL.sqlite3:
        ...

    @property
    def IsClosed(self) -> bool:
        ...

    # methods
    def __init__(self, ):
        ...

    @staticmethod
    def From(p: System.IntPtr, db: SQLitePCL.sqlite3, ) -> SQLitePCL.sqlite3_stmt:
        ...

    def ReleaseHandle(self, ) -> bool:
        ...

    def manual_close(self, ) -> int:
        ...

class sqlite3(System.IDisposable, System.Runtime.InteropServices.SafeHandle):
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
    def __init__(self, ):
        ...

    def ReleaseHandle(self, ) -> bool:
        ...

    def manual_close_v2(self, ) -> int:
        ...

    def manual_close(self, ) -> int:
        ...

    @staticmethod
    def New(p: System.IntPtr, ) -> SQLitePCL.sqlite3:
        ...

    def enable_sqlite3_next_stmt(self, enabled: bool, ) -> None:
        ...

    def add_stmt(self, stmt: SQLitePCL.sqlite3_stmt, ) -> None:
        ...

    def find_stmt(self, p: System.IntPtr, ) -> SQLitePCL.sqlite3_stmt:
        ...

    def remove_stmt(self, s: SQLitePCL.sqlite3_stmt, ) -> None:
        ...

    def GetOrCreateExtra(self, f: System.Func[T], ) -> T:
        ...

    def dispose_extra(self, ) -> None:
        ...

