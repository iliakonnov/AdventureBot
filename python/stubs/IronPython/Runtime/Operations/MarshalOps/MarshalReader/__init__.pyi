from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import System


class StackType(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    Tuple: int = ...
    Dict: int = ...
    List: int = ...
    Set: int = ...
    FrozenSet: int = ...

class ProcStack(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        self.StackType: int
        self.StackObj: System.Object
        self.StackCount: int
        self.HaveKey: bool
        self.Key: System.Object
        ...

    # static fields

    # properties
    # methods
    def __init__(self, ):
        ...

