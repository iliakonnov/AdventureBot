from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import IronPython.Compiler.Ast.BinaryExpression
import Microsoft.Scripting.Interpreter


class IsNotInstruction(IronPython.Compiler.Ast.BinaryExpression.BinaryInstruction):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields
    Instance: IronPython.Compiler.Ast.BinaryExpression.IsNotInstruction = ...

    # properties
    @property
    def ConsumedStack(self) -> int:
        ...

    @property
    def ProducedStack(self) -> int:
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

class IsInstruction(IronPython.Compiler.Ast.BinaryExpression.BinaryInstruction):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields
    Instance: IronPython.Compiler.Ast.BinaryExpression.IsInstruction = ...

    # properties
    @property
    def ConsumedStack(self) -> int:
        ...

    @property
    def ProducedStack(self) -> int:
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

class BinaryInstruction(Microsoft.Scripting.Interpreter.Instruction, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def ConsumedStack(self) -> int:
        ...

    @property
    def ProducedStack(self) -> int:
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

