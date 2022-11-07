from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import IronPython.Compiler.Ast


class SelfNameFinder(IronPython.Compiler.Ast.PythonWalker):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    def __init__(self, function: IronPython.Compiler.Ast.FunctionDefinition, self: IronPython.Compiler.Ast.Parameter, ):
        ...

    @staticmethod
    def FindNames(function: IronPython.Compiler.Ast.FunctionDefinition, ) -> System.Array[str]:
        ...

    def IsSelfReference(self, expr: IronPython.Compiler.Ast.Expression, ) -> bool:
        ...

    @typing.overload
    def Walk(self, node: IronPython.Compiler.Ast.ClassDefinition, ) -> bool:
        ...

    @typing.overload
    def Walk(self, node: IronPython.Compiler.Ast.FunctionDefinition, ) -> bool:
        ...

    @typing.overload
    def Walk(self, node: IronPython.Compiler.Ast.AssignmentStatement, ) -> bool:
        ...

