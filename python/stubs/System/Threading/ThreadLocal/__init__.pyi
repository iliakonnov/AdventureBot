from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import System
import System.Threading.ThreadLocal

T = typing.TypeVar('T')

class LinkedSlotVolatile(System.ValueType, typing.Generic[T]):
    @typing.overload
    def __init__(self, **kwargs):
        self.Value: System.Threading.ThreadLocal.LinkedSlot[T]
        ...

    # static fields

    # properties
    # methods
class LinkedSlot(System.Object, typing.Generic[T]):
    @typing.overload
    def __init__(self, **kwargs):
        self._next: System.Threading.ThreadLocal.LinkedSlot
        self._previous: System.Threading.ThreadLocal.LinkedSlot
        self._slotArray: System.Array[System.Threading.ThreadLocal.LinkedSlotVolatile[T]]
        self._value: T
        ...

    # static fields

    # properties
    # methods
    def __init__(self, slotArray: System.Array[System.Threading.ThreadLocal.LinkedSlotVolatile[T]], ):
        ...

