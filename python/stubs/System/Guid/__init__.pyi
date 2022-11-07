from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import System


class GuidResult(System.ValueType):
    @typing.overload
    def __init__(self, **kwargs):
        self._a: int
        self._bc: int
        self._b: int
        self._c: int
        self._defg: int
        self._de: int
        self._d: int
        self._fg: int
        self._hijk: int
        ...

    # static fields

    # properties
    # methods
    def __init__(self, canThrow: int, ):
        ...

    def SetFailure(self, overflow: bool, failureMessageID: str, ) -> None:
        ...

    def ToGuid(self, ) -> System.Guid:
        ...

class GuidParseThrowStyle(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    None_: int = ...
    All: int = ...
    AllButOverflow: int = ...

