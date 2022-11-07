from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import IronPython.Runtime.CommonDictionaryStorage
import System
import System.Runtime.Serialization


class DeserializationNullValue(IronPython.Runtime.CommonDictionaryStorage.NullValue):
    @typing.overload
    def __init__(self, **kwargs):
        self.Value: System.Object
        ...

    # static fields

    # properties
    @property
    def SerializationInfo(self) -> System.Runtime.Serialization.SerializationInfo:
        ...

    # methods
    def __init__(self, info: System.Runtime.Serialization.SerializationInfo, ):
        ...

class Bucket(System.ValueType):
    @typing.overload
    def __init__(self, **kwargs):
        self.Key: System.Object
        self.Value: System.Object
        self.HashCode: int
        ...

    # static fields

    # properties
    # methods
    def __init__(self, hashCode: int, key: System.Object, value: System.Object, ):
        ...

class NullValue(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        self.Value: System.Object
        ...

    # static fields

    # properties
    # methods
    def __init__(self, value: System.Object, ):
        ...

