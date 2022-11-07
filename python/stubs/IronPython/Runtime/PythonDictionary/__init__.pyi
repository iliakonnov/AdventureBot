from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import System
import System.Collections.Generic
import IronPython.Runtime.PythonDictionary
import IronPython.Runtime
import System.Collections


class DebugProxy(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def Members(self) -> System.Collections.Generic.List[IronPython.Runtime.PythonDictionary.KeyValueDebugView]:
        ...

    # methods
    def __init__(self, dict: IronPython.Runtime.PythonDictionary, ):
        ...

class KeyValueDebugView(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        self.Key: System.Object
        self.Value: System.Object
        ...

    # static fields

    # properties
    @property
    def TypeInfo(self) -> str:
        ...

    # methods
    def __init__(self, key: System.Object, value: System.Object, ):
        ...

class DictEnumerator(System.Collections.IDictionaryEnumerator, System.Collections.IEnumerator, System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def Entry(self) -> System.Collections.DictionaryEntry:
        ...

    @property
    def Key(self) -> System.Object:
        ...

    @property
    def Value(self) -> System.Object:
        ...

    @property
    def Current(self) -> System.Object:
        ...

    # methods
    def __init__(self, enumerator: System.Collections.Generic.IEnumerator[System.Collections.Generic.KeyValuePair[System.Object, System.Object]], ):
        ...

    def MoveNext(self, ) -> bool:
        ...

    def Reset(self, ) -> None:
        ...

