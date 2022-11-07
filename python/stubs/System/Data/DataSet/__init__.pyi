from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import System


class TableChanges(System.ValueType):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def HasChanges(self) -> int:
        ...
    @HasChanges.setter
    def HasChanges(self, val: int):
        ...

    @property
    def Item(self) -> bool:
        ...
    @Item.setter
    def Item(self, val: bool):
        ...

    # methods
    def __init__(self, rowCount: int, ):
        ...

