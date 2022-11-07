from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import System


class TwoObjects(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    def __init__(self, obj1: System.Object, obj2: System.Object, ):
        ...

    def GetHashCode(self, ) -> int:
        ...

    def Equals(self, other: System.Object, ) -> bool:
        ...

