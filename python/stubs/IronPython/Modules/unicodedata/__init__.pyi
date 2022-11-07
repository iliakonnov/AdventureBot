from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import System
import System.IO
import IronPython.Modules


class UCD(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def unidata_version(self) -> str:
        ...
    @unidata_version.setter
    def unidata_version(self, val: str):
        ...

    # methods
    def __init__(self, version: str, ):
        ...

    def lookup(self, name: str, ) -> str:
        ...

    @typing.overload
    def name(self, unichr: str, ) -> str:
        ...

    @typing.overload
    def name(self, unichr: str, default: System.Object, ) -> System.Object:
        ...

    def TryGetName(self, rune: int, name: ref[str], ) -> bool:
        ...

    def GetRune(self, unichr: str, ) -> int:
        ...

    @typing.overload
    def decimal(self, unichr: str, default: int, ) -> int:
        ...

    @typing.overload
    def decimal(self, unichr: str, ) -> int:
        ...

    @typing.overload
    def decimal(self, unichr: str, default: System.Object, ) -> System.Object:
        ...

    @typing.overload
    def digit(self, unichr: str, default: int, ) -> int:
        ...

    @typing.overload
    def digit(self, unichr: str, default: System.Object, ) -> System.Object:
        ...

    @typing.overload
    def digit(self, unichr: str, ) -> int:
        ...

    @typing.overload
    def numeric(self, unichr: str, default: float, ) -> float:
        ...

    @typing.overload
    def numeric(self, unichr: str, ) -> float:
        ...

    @typing.overload
    def numeric(self, unichr: str, default: System.Object, ) -> System.Object:
        ...

    def category(self, unichr: str, ) -> str:
        ...

    def bidirectional(self, unichr: str, ) -> str:
        ...

    def combining(self, unichr: str, ) -> int:
        ...

    def east_asian_width(self, unichr: str, ) -> str:
        ...

    def mirrored(self, unichr: str, ) -> int:
        ...

    def decomposition(self, unichr: str, ) -> str:
        ...

    def normalize(self, form: str, unistr: str, ) -> str:
        ...

    def BuildDatabase(self, data: System.IO.StreamReader, ) -> None:
        ...

    def BuildNameLookup(self, ) -> None:
        ...

    def TryGetInfo(self, unichr: int, charInfo: ref[IronPython.Modules.CharInfo], excludeRanges: bool = ..., ) -> bool:
        ...

    def EnsureLoaded(self, ) -> None:
        ...

