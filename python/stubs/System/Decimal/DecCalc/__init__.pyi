from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import System


class Buf24(System.ValueType):
    @typing.overload
    def __init__(self, **kwargs):
        self.U0: int
        self.U1: int
        self.U2: int
        self.U3: int
        self.U4: int
        self.U5: int
        ...

    # static fields

    # properties
    @property
    def Low64(self) -> int:
        ...
    @Low64.setter
    def Low64(self, val: int):
        ...

    Mid64: int = property(None, lambda val: ...)

    High64: int = property(None, lambda val: ...)

    # methods
class Buf16(System.ValueType):
    @typing.overload
    def __init__(self, **kwargs):
        self.U0: int
        self.U1: int
        self.U2: int
        self.U3: int
        ...

    # static fields

    # properties
    @property
    def Low64(self) -> int:
        ...
    @Low64.setter
    def Low64(self, val: int):
        ...

    @property
    def High64(self) -> int:
        ...
    @High64.setter
    def High64(self, val: int):
        ...

    # methods
class Buf12(System.ValueType):
    @typing.overload
    def __init__(self, **kwargs):
        self.U0: int
        self.U1: int
        self.U2: int
        ...

    # static fields

    # properties
    @property
    def Low64(self) -> int:
        ...
    @Low64.setter
    def Low64(self, val: int):
        ...

    @property
    def High64(self) -> int:
        ...
    @High64.setter
    def High64(self, val: int):
        ...

    # methods
