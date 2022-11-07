from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import System
import System.Collections.Concurrent.ConcurrentDictionary

TKey = typing.TypeVar('TKey')
TValue = typing.TypeVar('TValue')

class Tables(System.Object, typing.Generic[TKey, TValue]):
    @typing.overload
    def __init__(self, **kwargs):
        self._buckets: System.Array[System.Collections.Concurrent.ConcurrentDictionary.Node[TKey, TValue]]
        self._locks: System.Array[System.Object]
        self._countPerLock: System.Array[int]
        self._fastModBucketsMultiplier: int
        ...

    # static fields

    # properties
    # methods
    def __init__(self, buckets: System.Array[System.Collections.Concurrent.ConcurrentDictionary.Node[TKey, TValue]], locks: System.Array[System.Object], countPerLock: System.Array[int], ):
        ...

    def GetBucket(self, hashcode: int, ) -> ref[System.Collections.Concurrent.ConcurrentDictionary.Node[TKey, TValue]]:
        ...

    def GetBucketAndLock(self, hashcode: int, lockNo: ref[int], ) -> ref[System.Collections.Concurrent.ConcurrentDictionary.Node[TKey, TValue]]:
        ...

class Node(System.Object, typing.Generic[TKey, TValue]):
    @typing.overload
    def __init__(self, **kwargs):
        self._key: TKey
        self._value: TValue
        self._next: System.Collections.Concurrent.ConcurrentDictionary.Node
        self._hashcode: int
        ...

    # static fields

    # properties
    # methods
    def __init__(self, key: TKey, value: TValue, hashcode: int, next: System.Collections.Concurrent.ConcurrentDictionary.Node, ):
        ...

