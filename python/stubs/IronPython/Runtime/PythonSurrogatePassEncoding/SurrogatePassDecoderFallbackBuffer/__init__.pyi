from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import System


class ByteBuffer(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def Bytes(self) -> System.Array[int]:
        ...

    @property
    def Length(self) -> int:
        ...

    @property
    def Index(self) -> int:
        ...
    @Index.setter
    def Index(self, val: int):
        ...

    @property
    def EndIndex(self) -> int:
        ...

    # methods
    def __init__(self, size: int, ):
        ...

    def AddByte(self, b: int, ) -> None:
        ...

    def Flush(self, ) -> None:
        ...

    def TrimmedBytes(self, ) -> System.Array[int]:
        ...

    def Save(self, ) -> None:
        ...

    def Restore(self, ) -> None:
        ...

