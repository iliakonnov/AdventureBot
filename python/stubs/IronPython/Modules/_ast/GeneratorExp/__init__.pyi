from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import IronPython.Compiler.Ast


class ExtractListComprehensionIterators(IronPython.Compiler.Ast.PythonWalker):
    @typing.overload
    def __init__(self, **kwargs):
        self.Yield: IronPython.Compiler.Ast.YieldExpression
        ...

    # static fields

    # properties
    @property
    def Iterators(self) -> System.Array[IronPython.Compiler.Ast.ComprehensionIterator]:
        ...

    # methods
    def __init__(self, ):
        ...

    @typing.overload
    def Walk(self, node: IronPython.Compiler.Ast.ForStatement, ) -> bool:
        ...

    @typing.overload
    def Walk(self, node: IronPython.Compiler.Ast.IfStatement, ) -> bool:
        ...

    @typing.overload
    def Walk(self, node: IronPython.Compiler.Ast.YieldExpression, ) -> bool:
        ...

