from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import IronPython.Compiler.Ast.CallExpression
import IronPython.Runtime
import Microsoft.Scripting.Interpreter


class Invoke0Instruction(IronPython.Compiler.Ast.CallExpression.InvokeInstruction):
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
    def InstructionName(self) -> str:
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

    # methods
    def __init__(self, context: IronPython.Runtime.PythonContext, ):
        ...

    def Run(self, frame: Microsoft.Scripting.Interpreter.InterpretedFrame, ) -> int:
        ...

class Invoke3Instruction(IronPython.Compiler.Ast.CallExpression.InvokeInstruction):
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
    def InstructionName(self) -> str:
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

    # methods
    def __init__(self, context: IronPython.Runtime.PythonContext, ):
        ...

    def Run(self, frame: Microsoft.Scripting.Interpreter.InterpretedFrame, ) -> int:
        ...

class Invoke5Instruction(IronPython.Compiler.Ast.CallExpression.InvokeInstruction):
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
    def InstructionName(self) -> str:
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

    # methods
    def __init__(self, context: IronPython.Runtime.PythonContext, ):
        ...

    def Run(self, frame: Microsoft.Scripting.Interpreter.InterpretedFrame, ) -> int:
        ...

class Invoke1Instruction(IronPython.Compiler.Ast.CallExpression.InvokeInstruction):
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
    def InstructionName(self) -> str:
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

    # methods
    def __init__(self, context: IronPython.Runtime.PythonContext, ):
        ...

    def Run(self, frame: Microsoft.Scripting.Interpreter.InterpretedFrame, ) -> int:
        ...

class Invoke4Instruction(IronPython.Compiler.Ast.CallExpression.InvokeInstruction):
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
    def InstructionName(self) -> str:
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

    # methods
    def __init__(self, context: IronPython.Runtime.PythonContext, ):
        ...

    def Run(self, frame: Microsoft.Scripting.Interpreter.InterpretedFrame, ) -> int:
        ...

class Invoke2Instruction(IronPython.Compiler.Ast.CallExpression.InvokeInstruction):
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
    def InstructionName(self) -> str:
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

    # methods
    def __init__(self, context: IronPython.Runtime.PythonContext, ):
        ...

    def Run(self, frame: Microsoft.Scripting.Interpreter.InterpretedFrame, ) -> int:
        ...

class Invoke6Instruction(IronPython.Compiler.Ast.CallExpression.InvokeInstruction):
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
    def InstructionName(self) -> str:
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

    # methods
    def __init__(self, context: IronPython.Runtime.PythonContext, ):
        ...

    def Run(self, frame: Microsoft.Scripting.Interpreter.InterpretedFrame, ) -> int:
        ...

class InvokeInstruction(Microsoft.Scripting.Interpreter.Instruction, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def ProducedStack(self) -> int:
        ...

    @property
    def InstructionName(self) -> str:
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

    # methods
    def __init__(self, ):
        ...

