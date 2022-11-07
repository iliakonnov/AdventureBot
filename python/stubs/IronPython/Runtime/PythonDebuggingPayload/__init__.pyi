from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import IronPython.Compiler.Ast
import System.Collections.Generic


class TracingWalker(IronPython.Compiler.Ast.PythonWalker):
    @typing.overload
    def __init__(self, **kwargs):
        self.HandlerLocations: System.Collections.Generic.Dictionary[int, bool]
        self.LoopAndFinallyLocations: System.Collections.Generic.Dictionary[int, System.Collections.Generic.Dictionary[int, bool]]
        ...

    # static fields

    # properties
    @property
    def LoopOrFinallyIds(self) -> System.Collections.Generic.Dictionary[int, bool]:
        ...

    # methods
    def __init__(self, ):
        ...

    @typing.overload
    def Walk(self, node: IronPython.Compiler.Ast.ForStatement, ) -> bool:
        ...

    @typing.overload
    def Walk(self, node: IronPython.Compiler.Ast.WhileStatement, ) -> bool:
        ...

    @typing.overload
    def Walk(self, node: IronPython.Compiler.Ast.TryStatement, ) -> bool:
        ...

    @typing.overload
    def Walk(self, node: IronPython.Compiler.Ast.AssertStatement, ) -> bool:
        ...

    @typing.overload
    def Walk(self, node: IronPython.Compiler.Ast.AssignmentStatement, ) -> bool:
        ...

    @typing.overload
    def Walk(self, node: IronPython.Compiler.Ast.AugmentedAssignStatement, ) -> bool:
        ...

    @typing.overload
    def Walk(self, node: IronPython.Compiler.Ast.BreakStatement, ) -> bool:
        ...

    @typing.overload
    def Walk(self, node: IronPython.Compiler.Ast.ClassDefinition, ) -> bool:
        ...

    @typing.overload
    def Walk(self, node: IronPython.Compiler.Ast.ContinueStatement, ) -> bool:
        ...

    @typing.overload
    def Walk(self, node: IronPython.Compiler.Ast.DelStatement, ) -> bool:
        ...

    @typing.overload
    def Walk(self, node: IronPython.Compiler.Ast.EmptyStatement, ) -> bool:
        ...

    @typing.overload
    def Walk(self, node: IronPython.Compiler.Ast.GlobalStatement, ) -> bool:
        ...

    @typing.overload
    def Walk(self, node: IronPython.Compiler.Ast.FromImportStatement, ) -> bool:
        ...

    @typing.overload
    def Walk(self, node: IronPython.Compiler.Ast.ExpressionStatement, ) -> bool:
        ...

    @typing.overload
    def Walk(self, node: IronPython.Compiler.Ast.FunctionDefinition, ) -> bool:
        ...

    @typing.overload
    def Walk(self, node: IronPython.Compiler.Ast.IfStatement, ) -> bool:
        ...

    @typing.overload
    def Walk(self, node: IronPython.Compiler.Ast.ImportStatement, ) -> bool:
        ...

    @typing.overload
    def Walk(self, node: IronPython.Compiler.Ast.RaiseStatement, ) -> bool:
        ...

    @typing.overload
    def Walk(self, node: IronPython.Compiler.Ast.WithStatement, ) -> bool:
        ...

    def WalkLoopBody(self, body: IronPython.Compiler.Ast.Statement, isFinally: bool, ) -> None:
        ...

    def PostWalk(self, node: IronPython.Compiler.Ast.EmptyStatement, ) -> None:
        ...

    def UpdateLoops(self, stmt: IronPython.Compiler.Ast.Statement, ) -> None:
        ...

