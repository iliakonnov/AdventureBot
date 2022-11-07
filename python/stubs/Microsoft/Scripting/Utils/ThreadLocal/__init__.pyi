from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import System
import System.Threading

T = typing.TypeVar('T')

class StorageInfo(System.Object, typing.Generic[T]):
    @typing.overload
    def __init__(self, **kwargs):
        self.Thread: System.Threading.Thread
        self.Value: T
        ...

    # static fields

    # properties
    # methods
    def __init__(self, curThread: System.Threading.Thread, ):
        ...

