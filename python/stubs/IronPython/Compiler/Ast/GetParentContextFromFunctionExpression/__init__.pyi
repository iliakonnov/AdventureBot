from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import Microsoft.Scripting.Interpreter
import IronPython.Compiler.Ast.GetParentContextFromFunctionExpression


class GetParentContextFromFunctionInstruction(Microsoft.Scripting.Interpreter.Instruction):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields
    Instance: IronPython.Compiler.Ast.GetParentContextFromFunctionExpression.GetParentContextFromFunctionInstruction = ...

    # properties
    @property
    def ProducedStack(self) -> int:
        ...

    @property
    def ConsumedStack(self) -> int:
        ...

    @property
    def ConsumedContinuations(self) -> int:
        ...

    @property
    def ProducedContinuations(self) -> int:
        ...

    @property
    def StackBalance(self) -> int:
        ...

    @property
    def ContinuationsBalance(self) -> int:
        ...

    @property
    def InstructionName(self) -> str:
        ...

    # methods
    def __init__(self, ):
        ...

    def Run(self, frame: Microsoft.Scripting.Interpreter.InterpretedFrame, ) -> int:
        ...

