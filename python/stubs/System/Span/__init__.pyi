from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import System

T = typing.TypeVar('T')

class Enumerator(System.ValueType, typing.Generic[T]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def Current(self) -> ref[T]:
        ...

    # methods
    @typing.overload
    def MoveNext(self, ) -> System.Boolean:
        ...

