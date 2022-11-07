from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import System
import System.Reflection


class MethodBaseCache(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    def __init__(self, name: str, members: System.Array[System.Reflection.MethodBase], ):
        ...

    @staticmethod
    def CompareMethods(x: System.Reflection.MethodBase, y: System.Reflection.MethodBase, ) -> int:
        ...

    def Equals(self, obj: System.Object, ) -> bool:
        ...

    def GetHashCode(self, ) -> int:
        ...

