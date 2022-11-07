from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import System
import IronPython.Compiler.Ast
import Microsoft.Scripting
import IronPython.Compiler


class WithItem(System.ValueType):
    @typing.overload
    def __init__(self, **kwargs):
        self.Start: int
        self.ContextManager: IronPython.Compiler.Ast.Expression
        self.Variable: IronPython.Compiler.Ast.Expression
        ...

    # static fields

    # properties
    # methods
    def __init__(self, start: int, contextManager: IronPython.Compiler.Ast.Expression, variable: IronPython.Compiler.Ast.Expression, ):
        ...

class TokenizerErrorSink(Microsoft.Scripting.ErrorSink):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    def __init__(self, parser: IronPython.Compiler.Parser, ):
        ...

    def Add(self, sourceUnit: Microsoft.Scripting.SourceUnit, message: str, span: Microsoft.Scripting.SourceSpan, errorCode: int, severity: int, ) -> None:
        ...

