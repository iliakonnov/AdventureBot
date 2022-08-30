from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import System.Collections.Generic
import System.Collections
import System

T = typing.TypeVar('T')

class ReadOnlyCollection(System.Collections.Generic.IList[T], System.Collections.Generic.ICollection[T], System.Collections.Generic.IEnumerable[T], System.Collections.IEnumerable, System.Collections.IList, System.Collections.ICollection, System.Collections.Generic.IReadOnlyList[T], System.Collections.Generic.IReadOnlyCollection[T], System.Object, typing.Generic[T]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def Count(self) -> System.Int32:
        ...

    @property
    def Item(self) -> T:
        ...

    # methods
    @typing.overload
    def __init__(self, list: System.Collections.Generic.IList[T], ):
        ...

    @typing.overload
    def Contains(self, value: T, ) -> System.Boolean:
        ...

    @typing.overload
    def CopyTo(self, array: list[T], index: System.Int32, ) -> None:
        ...

    @typing.overload
    def GetEnumerator(self, ) -> System.Collections.Generic.IEnumerator[T]:
        ...

    @typing.overload
    def IndexOf(self, value: T, ) -> System.Int32:
        ...

