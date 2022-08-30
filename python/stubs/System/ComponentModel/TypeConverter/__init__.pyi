from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import System.Collections
import System


class StandardValuesCollection(System.Collections.ICollection, System.Collections.IEnumerable, System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def Count(self) -> System.Int32:
        ...

    @property
    def Item(self) -> System.Object:
        ...

    # methods
    @typing.overload
    def __init__(self, values: System.Collections.ICollection, ):
        ...

    @typing.overload
    def CopyTo(self, array: System.Array, index: System.Int32, ) -> None:
        ...

    @typing.overload
    def GetEnumerator(self, ) -> System.Collections.IEnumerator:
        ...

