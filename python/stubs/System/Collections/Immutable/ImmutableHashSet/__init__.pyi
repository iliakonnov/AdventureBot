from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import System.Collections.Generic
import System
import System.Collections
import System.Collections.Immutable
import System.Collections.Immutable.ImmutableHashSet

T = typing.TypeVar('T')

class Enumerator(System.Collections.Generic.IEnumerator[T], System.IDisposable, System.Collections.IEnumerator, System.Collections.Immutable.IStrongEnumerator[T], System.ValueType, typing.Generic[T]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def Current(self) -> T:
        ...

    # methods
    @typing.overload
    def MoveNext(self, ) -> System.Boolean:
        ...

    @typing.overload
    def Reset(self, ) -> None:
        ...

    @typing.overload
    def Dispose(self, ) -> None:
        ...

class Builder(System.Collections.Generic.IReadOnlyCollection[T], System.Collections.Generic.IEnumerable[T], System.Collections.IEnumerable, System.Collections.Generic.ISet[T], System.Collections.Generic.ICollection[T], System.Object, typing.Generic[T]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def Count(self) -> System.Int32:
        ...

    @property
    def KeyComparer(self) -> System.Collections.Generic.IEqualityComparer[T]:
        ...
    @KeyComparer.setter
    def KeyComparer(self, val: System.Collections.Generic.IEqualityComparer[T]):
        ...

    # methods
    @typing.overload
    def GetEnumerator(self, ) -> System.Collections.Immutable.ImmutableHashSet.Enumerator[T]:
        ...

    @typing.overload
    def ToImmutable(self, ) -> System.Collections.Immutable.ImmutableHashSet[T]:
        ...

    @typing.overload
    def TryGetValue(self, equalValue: T, actualValue: ref[T], ) -> System.Boolean:
        ...

    @typing.overload
    def Add(self, item: T, ) -> System.Boolean:
        ...

    @typing.overload
    def Remove(self, item: T, ) -> System.Boolean:
        ...

    @typing.overload
    def Contains(self, item: T, ) -> System.Boolean:
        ...

    @typing.overload
    def Clear(self, ) -> None:
        ...

    @typing.overload
    def ExceptWith(self, other: System.Collections.Generic.IEnumerable[T], ) -> None:
        ...

    @typing.overload
    def IntersectWith(self, other: System.Collections.Generic.IEnumerable[T], ) -> None:
        ...

    @typing.overload
    def IsProperSubsetOf(self, other: System.Collections.Generic.IEnumerable[T], ) -> System.Boolean:
        ...

    @typing.overload
    def IsProperSupersetOf(self, other: System.Collections.Generic.IEnumerable[T], ) -> System.Boolean:
        ...

    @typing.overload
    def IsSubsetOf(self, other: System.Collections.Generic.IEnumerable[T], ) -> System.Boolean:
        ...

    @typing.overload
    def IsSupersetOf(self, other: System.Collections.Generic.IEnumerable[T], ) -> System.Boolean:
        ...

    @typing.overload
    def Overlaps(self, other: System.Collections.Generic.IEnumerable[T], ) -> System.Boolean:
        ...

    @typing.overload
    def SetEquals(self, other: System.Collections.Generic.IEnumerable[T], ) -> System.Boolean:
        ...

    @typing.overload
    def SymmetricExceptWith(self, other: System.Collections.Generic.IEnumerable[T], ) -> None:
        ...

    @typing.overload
    def UnionWith(self, other: System.Collections.Generic.IEnumerable[T], ) -> None:
        ...

