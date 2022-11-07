from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import System.Linq.Expressions
import System
import IronPython.Compiler.Ast


class DelayedProfiling(System.Linq.Expressions.Expression):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def CanReduce(self) -> bool:
        ...

    @property
    def Type(self) -> System.Type:
        ...

    @property
    def NodeType(self) -> int:
        ...

    # methods
    def __init__(self, ast: IronPython.Compiler.Ast.ScopeStatement, body: System.Linq.Expressions.Expression, tick: System.Linq.Expressions.ParameterExpression, ):
        ...

    def VisitChildren(self, visitor: System.Linq.Expressions.ExpressionVisitor, ) -> System.Linq.Expressions.Expression:
        ...

    def Reduce(self, ) -> System.Linq.Expressions.Expression:
        ...

class ClosureInfo(System.ValueType):
    @typing.overload
    def __init__(self, **kwargs):
        self.Variable: IronPython.Compiler.Ast.PythonVariable
        self.AccessedInScope: bool
        ...

    # static fields

    # properties
    # methods
    def __init__(self, variable: IronPython.Compiler.Ast.PythonVariable, accessedInScope: bool, ):
        ...

class DelayedFunctionCode(System.Linq.Expressions.Expression):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def CanReduce(self) -> bool:
        ...

    @property
    def Code(self) -> System.Linq.Expressions.Expression:
        ...
    @Code.setter
    def Code(self, val: System.Linq.Expressions.Expression):
        ...

    @property
    def Type(self) -> System.Type:
        ...

    @property
    def NodeType(self) -> int:
        ...

    # methods
    def __init__(self, ):
        ...

    def VisitChildren(self, visitor: System.Linq.Expressions.ExpressionVisitor, ) -> System.Linq.Expressions.Expression:
        ...

    def Reduce(self, ) -> System.Linq.Expressions.Expression:
        ...

