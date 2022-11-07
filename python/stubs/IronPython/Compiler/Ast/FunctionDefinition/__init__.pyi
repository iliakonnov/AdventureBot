from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import Microsoft.Scripting.Interpreter
import IronPython.Runtime
import IronPython.Compiler.Ast
import IronPython.Compiler
import System.Linq.Expressions


class FunctionDefinitionInstruction(Microsoft.Scripting.Interpreter.Instruction):
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
    def __init__(self, context: IronPython.Runtime.CodeContext, definition: IronPython.Compiler.Ast.FunctionDefinition, defaultCount: int, kwdefaultCount: int, annotationCount: int, name: IronPython.Compiler.PythonGlobal, ):
        ...

    def Run(self, frame: Microsoft.Scripting.Interpreter.InterpretedFrame, ) -> int:
        ...

class ArbitraryGlobalsVisitor(System.Linq.Expressions.ExpressionVisitor):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    def __init__(self, ):
        ...

    def VisitExtension(self, node: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.Expression:
        ...

