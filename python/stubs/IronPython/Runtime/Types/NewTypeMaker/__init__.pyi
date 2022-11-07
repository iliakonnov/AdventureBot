from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import System
import System.Reflection.Emit
import System.Reflection
import Microsoft.Scripting.Generation
import IronPython.Runtime.Types.NewTypeMaker


class ReturnFixer(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    def __init__(self, reference: System.Reflection.Emit.LocalBuilder, parameter: System.Reflection.ParameterInfo, index: int, ):
        ...

    def FixReturn(self, il: Microsoft.Scripting.Generation.ILGen, ) -> None:
        ...

    @staticmethod
    def EmitArgument(il: Microsoft.Scripting.Generation.ILGen, parameter: System.Reflection.ParameterInfo, index: int, ) -> IronPython.Runtime.Types.NewTypeMaker.ReturnFixer:
        ...

