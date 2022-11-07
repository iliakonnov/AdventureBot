from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import System
import System.Reflection
import System.Reflection.Emit


class CustAttr(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    @typing.overload
    def __init__(self, con: System.Reflection.ConstructorInfo, binaryAttribute: System.Array[int], ):
        ...

    @typing.overload
    def __init__(self, customBuilder: System.Reflection.Emit.CustomAttributeBuilder, ):
        ...

    def Bake(self, module: System.Reflection.Emit.ModuleBuilder, token: int, ) -> None:
        ...

