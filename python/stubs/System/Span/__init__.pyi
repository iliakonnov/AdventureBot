from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import System

T = typing.TypeVar('T')

class Enumerator(System.ValueType, typing.Generic[T]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def Current(self) -> ref[T]:
        ...

    # methods
    def __init__(self, span: System.Span[T], ):
        ...

    def MoveNext(self, ) -> bool:
        ...

