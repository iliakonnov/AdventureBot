from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import Microsoft.Scripting.Interpreter
import System.Linq.Expressions
import IronPython.Compiler.ClosureExpression
import System


class MakeClosureCellExpression(Microsoft.Scripting.Interpreter.IInstructionProvider, System.Linq.Expressions.Expression):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields
    Instance: IronPython.Compiler.ClosureExpression.MakeClosureCellExpression = ...

    # properties
    @property
    def CanReduce(self) -> bool:
        ...

    @property
    def NodeType(self) -> int:
        ...

    @property
    def Type(self) -> System.Type:
        ...

    # methods
    def __init__(self, ):
        ...

    def Reduce(self, ) -> System.Linq.Expressions.Expression:
        ...

    def AddInstructions(self, compiler: Microsoft.Scripting.Interpreter.LightCompiler, ) -> None:
        ...

