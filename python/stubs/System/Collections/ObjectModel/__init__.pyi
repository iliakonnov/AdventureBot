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

    # static fields

    # properties
    @property
    def Count(self) -> int:
        ...

    @property
    def Item(self) -> T:
        ...

    @property
    def Items(self) -> System.Collections.Generic.IList[T]:
        ...

    @property
    def IsReadOnly(self) -> bool:
        ...

    @property
    def Item(self) -> T:
        ...
    @Item.setter
    def Item(self, val: T):
        ...

    @property
    def IsSynchronized(self) -> bool:
        ...

    @property
    def SyncRoot(self) -> System.Object:
        ...

    @property
    def IsFixedSize(self) -> bool:
        ...

    @property
    def IsReadOnly(self) -> bool:
        ...

    @property
    def Item(self) -> System.Object:
        ...
    @Item.setter
    def Item(self, val: System.Object):
        ...

    # methods
    def __init__(self, list: System.Collections.Generic.IList[T], ):
        ...

    def Contains(self, value: T, ) -> bool:
        ...

    def CopyTo(self, array: System.Array[T], index: int, ) -> None:
        ...

    def GetEnumerator(self, ) -> System.Collections.Generic.IEnumerator[T]:
        ...

    def IndexOf(self, value: T, ) -> int:
        ...

    def Add(self, value: T, ) -> None:
        ...

    def Clear(self, ) -> None:
        ...

    def Insert(self, index: int, value: T, ) -> None:
        ...

    def Remove(self, value: T, ) -> bool:
        ...

    def RemoveAt(self, index: int, ) -> None:
        ...

    def GetEnumerator(self, ) -> System.Collections.IEnumerator:
        ...

    def CopyTo(self, array: System.Array, index: int, ) -> None:
        ...

    def Add(self, value: System.Object, ) -> int:
        ...

    def Clear(self, ) -> None:
        ...

    @staticmethod
    def IsCompatibleObject(value: System.Object, ) -> bool:
        ...

    def Contains(self, value: System.Object, ) -> bool:
        ...

    def IndexOf(self, value: System.Object, ) -> int:
        ...

    def Insert(self, index: int, value: System.Object, ) -> None:
        ...

    def Remove(self, value: System.Object, ) -> None:
        ...

    def RemoveAt(self, index: int, ) -> None:
        ...

