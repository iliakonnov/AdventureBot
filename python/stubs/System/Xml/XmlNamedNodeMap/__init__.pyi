from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import System
import System.Collections


class SmallXmlNodeList(System.ValueType):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def Count(self) -> int:
        ...

    @property
    def Item(self) -> System.Object:
        ...

    # methods
    def Add(self, value: System.Object, ) -> None:
        ...

    def RemoveAt(self, index: int, ) -> None:
        ...

    def Insert(self, index: int, value: System.Object, ) -> None:
        ...

    def GetEnumerator(self, ) -> System.Collections.IEnumerator:
        ...

