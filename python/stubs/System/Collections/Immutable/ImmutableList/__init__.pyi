from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import System.Collections.Immutable
import System.Collections.Generic
import System.Collections
import System
import System.Collections.Immutable.ImmutableList

T = typing.TypeVar('T')
TOutput = typing.TypeVar('TOutput')

class Node(System.Collections.Immutable.IBinaryTree[T], System.Collections.Immutable.IBinaryTree, System.Collections.Generic.IEnumerable[T], System.Collections.IEnumerable, System.Object, typing.Generic[T]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields
    EmptyNode: System.Collections.Immutable.ImmutableList.Node = ...

    # properties
    @property
    def IsEmpty(self) -> bool:
        ...

    @property
    def Height(self) -> int:
        ...

    @property
    def Left(self) -> System.Collections.Immutable.ImmutableList.Node:
        ...

    @property
    def Left(self) -> System.Collections.Immutable.IBinaryTree:
        ...

    @property
    def Right(self) -> System.Collections.Immutable.ImmutableList.Node:
        ...

    @property
    def Right(self) -> System.Collections.Immutable.IBinaryTree:
        ...

    @property
    def Left(self) -> System.Collections.Immutable.IBinaryTree[T]:
        ...

    @property
    def Right(self) -> System.Collections.Immutable.IBinaryTree[T]:
        ...

    @property
    def Value(self) -> T:
        ...

    @property
    def Count(self) -> int:
        ...

    @property
    def Key(self) -> T:
        ...

    @property
    def Item(self) -> T:
        ...

    @property
    def BalanceFactor(self) -> int:
        ...

    @property
    def IsRightHeavy(self) -> bool:
        ...

    @property
    def IsLeftHeavy(self) -> bool:
        ...

    @property
    def IsBalanced(self) -> bool:
        ...

    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def __init__(self, key: T, left: System.Collections.Immutable.ImmutableList.Node, right: System.Collections.Immutable.ImmutableList.Node, frozen: bool = ..., ):
        ...

    def ItemRef(self, index: int, ) -> ref[T]:
        ...

    def ItemRefUnchecked(self, index: int, ) -> ref[T]:
        ...

    @typing.overload
    def GetEnumerator(self, ) -> System.Collections.Immutable.ImmutableList.Enumerator[T]:
        ...

    @typing.overload
    def GetEnumerator(self, builder: System.Collections.Immutable.ImmutableList.Builder[T], ) -> System.Collections.Immutable.ImmutableList.Enumerator[T]:
        ...

    def GetEnumerator(self, ) -> System.Collections.Generic.IEnumerator[T]:
        ...

    def GetEnumerator(self, ) -> System.Collections.IEnumerator:
        ...

    @staticmethod
    def NodeTreeFromList(items: System.Collections.Immutable.IOrderedCollection[T], start: int, length: int, ) -> System.Collections.Immutable.ImmutableList.Node:
        ...

    def Add(self, key: T, ) -> System.Collections.Immutable.ImmutableList.Node:
        ...

    def Insert(self, index: int, key: T, ) -> System.Collections.Immutable.ImmutableList.Node:
        ...

    def AddRange(self, keys: System.Collections.Generic.IEnumerable[T], ) -> System.Collections.Immutable.ImmutableList.Node:
        ...

    def InsertRange(self, index: int, keys: System.Collections.Generic.IEnumerable[T], ) -> System.Collections.Immutable.ImmutableList.Node:
        ...

    def RemoveAt(self, index: int, ) -> System.Collections.Immutable.ImmutableList.Node:
        ...

    def RemoveAll(self, match: System.Predicate[T], ) -> System.Collections.Immutable.ImmutableList.Node:
        ...

    def ReplaceAt(self, index: int, value: T, ) -> System.Collections.Immutable.ImmutableList.Node:
        ...

    @typing.overload
    def Reverse(self, ) -> System.Collections.Immutable.ImmutableList.Node:
        ...

    @typing.overload
    def Reverse(self, index: int, count: int, ) -> System.Collections.Immutable.ImmutableList.Node:
        ...

    @typing.overload
    def Sort(self, ) -> System.Collections.Immutable.ImmutableList.Node:
        ...

    @typing.overload
    def Sort(self, comparison: System.Comparison[T], ) -> System.Collections.Immutable.ImmutableList.Node:
        ...

    @typing.overload
    def Sort(self, comparer: System.Collections.Generic.IComparer[T], ) -> System.Collections.Immutable.ImmutableList.Node:
        ...

    @typing.overload
    def Sort(self, index: int, count: int, comparer: System.Collections.Generic.IComparer[T], ) -> System.Collections.Immutable.ImmutableList.Node:
        ...

    def BinarySearch(self, index: int, count: int, item: T, comparer: System.Collections.Generic.IComparer[T], ) -> int:
        ...

    @typing.overload
    def IndexOf(self, item: T, equalityComparer: System.Collections.Generic.IEqualityComparer[T], ) -> int:
        ...

    @typing.overload
    def IndexOf(self, item: T, index: int, count: int, equalityComparer: System.Collections.Generic.IEqualityComparer[T], ) -> int:
        ...

    @typing.overload
    def Contains(self, item: T, equalityComparer: System.Collections.Generic.IEqualityComparer[T], ) -> bool:
        ...

    @staticmethod
    @typing.overload
    def Contains(node: System.Collections.Immutable.ImmutableList.Node, value: T, equalityComparer: System.Collections.Generic.IEqualityComparer[T], ) -> bool:
        ...

    def LastIndexOf(self, item: T, index: int, count: int, equalityComparer: System.Collections.Generic.IEqualityComparer[T], ) -> int:
        ...

    @typing.overload
    def CopyTo(self, array: System.Array[T], ) -> None:
        ...

    @typing.overload
    def CopyTo(self, array: System.Array[T], arrayIndex: int, ) -> None:
        ...

    @typing.overload
    def CopyTo(self, index: int, array: System.Array[T], arrayIndex: int, count: int, ) -> None:
        ...

    @typing.overload
    def CopyTo(self, array: System.Array, arrayIndex: int, ) -> None:
        ...

    def ConvertAll(self, converter: System.Func[T, TOutput], ) -> System.Collections.Immutable.ImmutableList.Node[TOutput]:
        ...

    def TrueForAll(self, match: System.Predicate[T], ) -> bool:
        ...

    def Exists(self, match: System.Predicate[T], ) -> bool:
        ...

    def Find(self, match: System.Predicate[T], ) -> T:
        ...

    def FindAll(self, match: System.Predicate[T], ) -> System.Collections.Immutable.ImmutableList[T]:
        ...

    @typing.overload
    def FindIndex(self, match: System.Predicate[T], ) -> int:
        ...

    @typing.overload
    def FindIndex(self, startIndex: int, match: System.Predicate[T], ) -> int:
        ...

    @typing.overload
    def FindIndex(self, startIndex: int, count: int, match: System.Predicate[T], ) -> int:
        ...

    def FindLast(self, match: System.Predicate[T], ) -> T:
        ...

    @typing.overload
    def FindLastIndex(self, match: System.Predicate[T], ) -> int:
        ...

    @typing.overload
    def FindLastIndex(self, startIndex: int, match: System.Predicate[T], ) -> int:
        ...

    @typing.overload
    def FindLastIndex(self, startIndex: int, count: int, match: System.Predicate[T], ) -> int:
        ...

    def Freeze(self, ) -> None:
        ...

    def RotateLeft(self, ) -> System.Collections.Immutable.ImmutableList.Node:
        ...

    def RotateRight(self, ) -> System.Collections.Immutable.ImmutableList.Node:
        ...

    def DoubleLeft(self, ) -> System.Collections.Immutable.ImmutableList.Node:
        ...

    def DoubleRight(self, ) -> System.Collections.Immutable.ImmutableList.Node:
        ...

    def Balance(self, ) -> System.Collections.Immutable.ImmutableList.Node:
        ...

    def BalanceLeft(self, ) -> System.Collections.Immutable.ImmutableList.Node:
        ...

    def BalanceRight(self, ) -> System.Collections.Immutable.ImmutableList.Node:
        ...

    def BalanceMany(self, ) -> System.Collections.Immutable.ImmutableList.Node:
        ...

    def MutateBoth(self, left: System.Collections.Immutable.ImmutableList.Node, right: System.Collections.Immutable.ImmutableList.Node, ) -> System.Collections.Immutable.ImmutableList.Node:
        ...

    def MutateLeft(self, left: System.Collections.Immutable.ImmutableList.Node, ) -> System.Collections.Immutable.ImmutableList.Node:
        ...

    def MutateRight(self, right: System.Collections.Immutable.ImmutableList.Node, ) -> System.Collections.Immutable.ImmutableList.Node:
        ...

    @staticmethod
    def ParentHeight(left: System.Collections.Immutable.ImmutableList.Node, right: System.Collections.Immutable.ImmutableList.Node, ) -> int:
        ...

    @staticmethod
    def ParentCount(left: System.Collections.Immutable.ImmutableList.Node, right: System.Collections.Immutable.ImmutableList.Node, ) -> int:
        ...

    def MutateKey(self, key: T, ) -> System.Collections.Immutable.ImmutableList.Node:
        ...

    @staticmethod
    def CreateRange(keys: System.Collections.Generic.IEnumerable[T], ) -> System.Collections.Immutable.ImmutableList.Node:
        ...

    @staticmethod
    def CreateLeaf(key: T, ) -> System.Collections.Immutable.ImmutableList.Node:
        ...

class Enumerator(System.Collections.Generic.IEnumerator[T], System.IDisposable, System.Collections.IEnumerator, System.Collections.Immutable.ISecurePooledObjectUser, System.Collections.Immutable.IStrongEnumerator[T], System.ValueType, typing.Generic[T]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def PoolUserId(self) -> int:
        ...

    @property
    def Current(self) -> T:
        ...

    @property
    def Current(self) -> System.Object:
        ...

    # methods
    def __init__(self, root: System.Collections.Immutable.ImmutableList.Node[T], builder: System.Collections.Immutable.ImmutableList.Builder[T] = ..., startIndex: int = ..., count: int = ..., reversed: bool = ..., ):
        ...

    def Dispose(self, ) -> None:
        ...

    def MoveNext(self, ) -> bool:
        ...

    def Reset(self, ) -> None:
        ...

    def ResetStack(self, ) -> None:
        ...

    def NextBranch(self, node: System.Collections.Immutable.ImmutableList.Node[T], ) -> System.Collections.Immutable.ImmutableList.Node[T]:
        ...

    def PreviousBranch(self, node: System.Collections.Immutable.ImmutableList.Node[T], ) -> System.Collections.Immutable.ImmutableList.Node[T]:
        ...

    def ThrowIfDisposed(self, ) -> None:
        ...

    def ThrowIfChanged(self, ) -> None:
        ...

    def PushNext(self, node: System.Collections.Immutable.ImmutableList.Node[T], ) -> None:
        ...

class Builder(System.Collections.Generic.IList[T], System.Collections.Generic.ICollection[T], System.Collections.Generic.IEnumerable[T], System.Collections.IEnumerable, System.Collections.IList, System.Collections.ICollection, System.Collections.Immutable.IOrderedCollection[T], System.Collections.Immutable.IImmutableListQueries[T], System.Collections.Generic.IReadOnlyList[T], System.Collections.Generic.IReadOnlyCollection[T], System.Object, typing.Generic[T]):
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
    def Version(self) -> int:
        ...

    @property
    def Root(self) -> System.Collections.Immutable.ImmutableList.Node[T]:
        ...
    @Root.setter
    def Root(self, val: System.Collections.Immutable.ImmutableList.Node[T]):
        ...

    @property
    def Item(self) -> T:
        ...
    @Item.setter
    def Item(self, val: T):
        ...

    @property
    def Item(self) -> T:
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

    @property
    def IsSynchronized(self) -> bool:
        ...

    @property
    def SyncRoot(self) -> System.Object:
        ...

    # methods
    def __init__(self, list: System.Collections.Immutable.ImmutableList[T], ):
        ...

    def ItemRef(self, index: int, ) -> ref[T]:
        ...

    @typing.overload
    def IndexOf(self, item: T, ) -> int:
        ...

    @typing.overload
    def IndexOf(self, item: T, index: int, ) -> int:
        ...

    @typing.overload
    def IndexOf(self, item: T, index: int, count: int, ) -> int:
        ...

    @typing.overload
    def IndexOf(self, item: T, index: int, count: int, equalityComparer: System.Collections.Generic.IEqualityComparer[T], ) -> int:
        ...

    def Insert(self, index: int, item: T, ) -> None:
        ...

    def RemoveAt(self, index: int, ) -> None:
        ...

    def Add(self, item: T, ) -> None:
        ...

    def Clear(self, ) -> None:
        ...

    def Contains(self, item: T, ) -> bool:
        ...

    def Remove(self, item: T, ) -> bool:
        ...

    def GetEnumerator(self, ) -> System.Collections.Immutable.ImmutableList.Enumerator[T]:
        ...

    def GetEnumerator(self, ) -> System.Collections.Generic.IEnumerator[T]:
        ...

    def GetEnumerator(self, ) -> System.Collections.IEnumerator:
        ...

    def ForEach(self, action: System.Action[T], ) -> None:
        ...

    @typing.overload
    def CopyTo(self, array: System.Array[T], ) -> None:
        ...

    @typing.overload
    def CopyTo(self, array: System.Array[T], arrayIndex: int, ) -> None:
        ...

    @typing.overload
    def CopyTo(self, index: int, array: System.Array[T], arrayIndex: int, count: int, ) -> None:
        ...

    def GetRange(self, index: int, count: int, ) -> System.Collections.Immutable.ImmutableList[T]:
        ...

    def ConvertAll(self, converter: System.Func[T, TOutput], ) -> System.Collections.Immutable.ImmutableList[TOutput]:
        ...

    def Exists(self, match: System.Predicate[T], ) -> bool:
        ...

    def Find(self, match: System.Predicate[T], ) -> T:
        ...

    def FindAll(self, match: System.Predicate[T], ) -> System.Collections.Immutable.ImmutableList[T]:
        ...

    @typing.overload
    def FindIndex(self, match: System.Predicate[T], ) -> int:
        ...

    @typing.overload
    def FindIndex(self, startIndex: int, match: System.Predicate[T], ) -> int:
        ...

    @typing.overload
    def FindIndex(self, startIndex: int, count: int, match: System.Predicate[T], ) -> int:
        ...

    def FindLast(self, match: System.Predicate[T], ) -> T:
        ...

    @typing.overload
    def FindLastIndex(self, match: System.Predicate[T], ) -> int:
        ...

    @typing.overload
    def FindLastIndex(self, startIndex: int, match: System.Predicate[T], ) -> int:
        ...

    @typing.overload
    def FindLastIndex(self, startIndex: int, count: int, match: System.Predicate[T], ) -> int:
        ...

    @typing.overload
    def LastIndexOf(self, item: T, ) -> int:
        ...

    @typing.overload
    def LastIndexOf(self, item: T, startIndex: int, ) -> int:
        ...

    @typing.overload
    def LastIndexOf(self, item: T, startIndex: int, count: int, ) -> int:
        ...

    @typing.overload
    def LastIndexOf(self, item: T, startIndex: int, count: int, equalityComparer: System.Collections.Generic.IEqualityComparer[T], ) -> int:
        ...

    def TrueForAll(self, match: System.Predicate[T], ) -> bool:
        ...

    def AddRange(self, items: System.Collections.Generic.IEnumerable[T], ) -> None:
        ...

    def InsertRange(self, index: int, items: System.Collections.Generic.IEnumerable[T], ) -> None:
        ...

    def RemoveAll(self, match: System.Predicate[T], ) -> int:
        ...

    @typing.overload
    def Reverse(self, ) -> None:
        ...

    @typing.overload
    def Reverse(self, index: int, count: int, ) -> None:
        ...

    @typing.overload
    def Sort(self, ) -> None:
        ...

    @typing.overload
    def Sort(self, comparison: System.Comparison[T], ) -> None:
        ...

    @typing.overload
    def Sort(self, comparer: System.Collections.Generic.IComparer[T], ) -> None:
        ...

    @typing.overload
    def Sort(self, index: int, count: int, comparer: System.Collections.Generic.IComparer[T], ) -> None:
        ...

    @typing.overload
    def BinarySearch(self, item: T, ) -> int:
        ...

    @typing.overload
    def BinarySearch(self, item: T, comparer: System.Collections.Generic.IComparer[T], ) -> int:
        ...

    @typing.overload
    def BinarySearch(self, index: int, count: int, item: T, comparer: System.Collections.Generic.IComparer[T], ) -> int:
        ...

    def ToImmutable(self, ) -> System.Collections.Immutable.ImmutableList[T]:
        ...

    def Add(self, value: System.Object, ) -> int:
        ...

    def Clear(self, ) -> None:
        ...

    def Contains(self, value: System.Object, ) -> bool:
        ...

    def IndexOf(self, value: System.Object, ) -> int:
        ...

    def Insert(self, index: int, value: System.Object, ) -> None:
        ...

    def Remove(self, value: System.Object, ) -> None:
        ...

    def CopyTo(self, array: System.Array, arrayIndex: int, ) -> None:
        ...

