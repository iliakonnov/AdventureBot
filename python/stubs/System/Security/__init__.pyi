from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import System
import System.Security


class SecurityRuleSet(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    None_: System.Byte = None
    Level1: System.Byte = Level1
    Level2: System.Byte = Level2

class SecureString(System.IDisposable, System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def Length(self) -> System.Int32:
        ...

    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def __init__(self, value: ptr[System.Char], length: System.Int32, ):
        ...

    @typing.overload
    def AppendChar(self, c: System.Char, ) -> None:
        ...

    @typing.overload
    def Clear(self, ) -> None:
        ...

    @typing.overload
    def Copy(self, ) -> System.Security.SecureString:
        ...

    @typing.overload
    def Dispose(self, ) -> None:
        ...

    @typing.overload
    def InsertAt(self, index: System.Int32, c: System.Char, ) -> None:
        ...

    @typing.overload
    def IsReadOnly(self, ) -> System.Boolean:
        ...

    @typing.overload
    def MakeReadOnly(self, ) -> None:
        ...

    @typing.overload
    def RemoveAt(self, index: System.Int32, ) -> None:
        ...

    @typing.overload
    def SetAt(self, index: System.Int32, c: System.Char, ) -> None:
        ...

