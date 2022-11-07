from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import System
import System.Collections.Immutable.ImmutableList
import System.Collections.Immutable.ImmutableHashSet.HashBucket
import System.Collections.Immutable.ImmutableHashSet
import System.Collections.Generic
import System.Collections
import System.Collections.Immutable

T = typing.TypeVar('T')

class HashBucket(System.ValueType, typing.Generic[T]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def IsEmpty(self) -> bool:
        ...

    # methods
    def __init__(self, firstElement: T, additionalElements: System.Collections.Immutable.ImmutableList.Node[T] = ..., ):
        ...

    def GetEnumerator(self, ) -> System.Collections.Immutable.ImmutableHashSet.HashBucket.Enumerator[T]:
        ...

    def Equals(self, obj: System.Object, ) -> bool:
        ...

    def GetHashCode(self, ) -> int:
        ...

    def EqualsByRef(self, other: System.Collections.Immutable.ImmutableHashSet.HashBucket, ) -> bool:
        ...

    def EqualsByValue(self, other: System.Collections.Immutable.ImmutableHashSet.HashBucket, valueComparer: System.Collections.Generic.IEqualityComparer[T], ) -> bool:
        ...

    def Add(self, value: T, valueComparer: System.Collections.Generic.IEqualityComparer[T], result: ref[int], ) -> System.Collections.Immutable.ImmutableHashSet.HashBucket:
        ...

    def Contains(self, value: T, valueComparer: System.Collections.Generic.IEqualityComparer[T], ) -> bool:
        ...

    def TryExchange(self, value: T, valueComparer: System.Collections.Generic.IEqualityComparer[T], existingValue: ref[T], ) -> bool:
        ...

    def Remove(self, value: T, equalityComparer: System.Collections.Generic.IEqualityComparer[T], result: ref[int], ) -> System.Collections.Immutable.ImmutableHashSet.HashBucket:
        ...

    def Freeze(self, ) -> None:
        ...

class Builder(System.Collections.Generic.IReadOnlyCollection[T], System.Collections.Generic.IEnumerable[T], System.Collections.IEnumerable, System.Collections.Generic.ISet[T], System.Collections.Generic.ICollection[T], System.Object, typing.Generic[T]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def Count(self) -> int:
        ...

    @property
    def IsReadOnly(self) -> bool:
        ...

    @property
    def KeyComparer(self) -> System.Collections.Generic.IEqualityComparer[T]:
        ...
    @KeyComparer.setter
    def KeyComparer(self, val: System.Collections.Generic.IEqualityComparer[T]):
        ...

    @property
    def Version(self) -> int:
        ...

    @property
    def Origin(self) -> System.Collections.Immutable.ImmutableHashSet.MutationInput[T]:
        ...

    @property
    def Root(self) -> System.Collections.Immutable.SortedInt32KeyNode[System.Collections.Immutable.ImmutableHashSet.HashBucket[T]]:
        ...
    @Root.setter
    def Root(self, val: System.Collections.Immutable.SortedInt32KeyNode[System.Collections.Immutable.ImmutableHashSet.HashBucket[T]]):
        ...

    # methods
    def __init__(self, set: System.Collections.Immutable.ImmutableHashSet[T], ):
        ...

    def GetEnumerator(self, ) -> System.Collections.Immutable.ImmutableHashSet.Enumerator[T]:
        ...

    def ToImmutable(self, ) -> System.Collections.Immutable.ImmutableHashSet[T]:
        ...

    def TryGetValue(self, equalValue: T, actualValue: ref[T], ) -> bool:
        ...

    def Add(self, item: T, ) -> bool:
        ...

    def Remove(self, item: T, ) -> bool:
        ...

    def Contains(self, item: T, ) -> bool:
        ...

    def Clear(self, ) -> None:
        ...

    def ExceptWith(self, other: System.Collections.Generic.IEnumerable[T], ) -> None:
        ...

    def IntersectWith(self, other: System.Collections.Generic.IEnumerable[T], ) -> None:
        ...

    def IsProperSubsetOf(self, other: System.Collections.Generic.IEnumerable[T], ) -> bool:
        ...

    def IsProperSupersetOf(self, other: System.Collections.Generic.IEnumerable[T], ) -> bool:
        ...

    def IsSubsetOf(self, other: System.Collections.Generic.IEnumerable[T], ) -> bool:
        ...

    def IsSupersetOf(self, other: System.Collections.Generic.IEnumerable[T], ) -> bool:
        ...

    def Overlaps(self, other: System.Collections.Generic.IEnumerable[T], ) -> bool:
        ...

    def SetEquals(self, other: System.Collections.Generic.IEnumerable[T], ) -> bool:
        ...

    def SymmetricExceptWith(self, other: System.Collections.Generic.IEnumerable[T], ) -> None:
        ...

    def UnionWith(self, other: System.Collections.Generic.IEnumerable[T], ) -> None:
        ...

    def Add(self, item: T, ) -> None:
        ...

    def CopyTo(self, array: System.Array[T], arrayIndex: int, ) -> None:
        ...

    def GetEnumerator(self, ) -> System.Collections.Generic.IEnumerator[T]:
        ...

    def GetEnumerator(self, ) -> System.Collections.IEnumerator:
        ...

    def Apply(self, result: System.Collections.Immutable.ImmutableHashSet.MutationResult[T], ) -> None:
        ...

class OperationResult(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum, typing.Generic[T]):
    SizeChanged: int = ...
    NoChangeRequired: int = ...

class Enumerator(System.Collections.Generic.IEnumerator[T], System.IDisposable, System.Collections.IEnumerator, System.Collections.Immutable.IStrongEnumerator[T], System.ValueType, typing.Generic[T]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def Current(self) -> T:
        ...

    @property
    def Current(self) -> System.Object:
        ...

    # methods
    def __init__(self, root: System.Collections.Immutable.SortedInt32KeyNode[System.Collections.Immutable.ImmutableHashSet.HashBucket[T]], builder: System.Collections.Immutable.ImmutableHashSet.Builder[T] = ..., ):
        ...

    def MoveNext(self, ) -> bool:
        ...

    def Reset(self, ) -> None:
        ...

    def Dispose(self, ) -> None:
        ...

    def ThrowIfChanged(self, ) -> None:
        ...

class MutationInput(System.ValueType, typing.Generic[T]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def Root(self) -> System.Collections.Immutable.SortedInt32KeyNode[System.Collections.Immutable.ImmutableHashSet.HashBucket[T]]:
        ...

    @property
    def EqualityComparer(self) -> System.Collections.Generic.IEqualityComparer[T]:
        ...

    @property
    def Count(self) -> int:
        ...

    @property
    def HashBucketEqualityComparer(self) -> System.Collections.Generic.IEqualityComparer[System.Collections.Immutable.ImmutableHashSet.HashBucket[T]]:
        ...

    # methods
    @typing.overload
    def __init__(self, set: System.Collections.Immutable.ImmutableHashSet[T], ):
        ...

    @typing.overload
    def __init__(self, root: System.Collections.Immutable.SortedInt32KeyNode[System.Collections.Immutable.ImmutableHashSet.HashBucket[T]], equalityComparer: System.Collections.Generic.IEqualityComparer[T], hashBucketEqualityComparer: System.Collections.Generic.IEqualityComparer[System.Collections.Immutable.ImmutableHashSet.HashBucket[T]], count: int, ):
        ...

class MutationResult(System.ValueType, typing.Generic[T]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def Root(self) -> System.Collections.Immutable.SortedInt32KeyNode[System.Collections.Immutable.ImmutableHashSet.HashBucket[T]]:
        ...

    @property
    def Count(self) -> int:
        ...

    @property
    def CountType(self) -> int:
        ...

    # methods
    def __init__(self, root: System.Collections.Immutable.SortedInt32KeyNode[System.Collections.Immutable.ImmutableHashSet.HashBucket[T]], count: int, countType: int = ..., ):
        ...

    def Finalize(self, priorSet: System.Collections.Immutable.ImmutableHashSet[T], ) -> System.Collections.Immutable.ImmutableHashSet[T]:
        ...

class CountType(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum, typing.Generic[T]):
    Adjustment: int = ...
    FinalValue: int = ...

