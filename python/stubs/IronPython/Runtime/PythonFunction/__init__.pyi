from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import System
import IronPython.Runtime.PythonFunction


class FunctionCallerKey(System.IEquatable[IronPython.Runtime.PythonFunction.FunctionCallerKey], System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        self.CallerType: System.Type
        self.FunctionCompat: int
        ...

    # static fields

    # properties
    # methods
    def __init__(self, callerType: System.Type, compat: int, ):
        ...

    @typing.overload
    def Equals(self, other: IronPython.Runtime.PythonFunction.FunctionCallerKey, ) -> bool:
        ...

    @typing.overload
    def Equals(self, obj: System.Object, ) -> bool:
        ...

    def GetHashCode(self, ) -> int:
        ...

