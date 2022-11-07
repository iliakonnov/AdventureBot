from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import System
import System.Collections


class HashCache(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        self.HashCode: int
        self.Comparer: System.Collections.IEqualityComparer
        ...

    # static fields

    # properties
    # methods
    def __init__(self, hashCode: int, comparer: System.Collections.IEqualityComparer, ):
        ...

