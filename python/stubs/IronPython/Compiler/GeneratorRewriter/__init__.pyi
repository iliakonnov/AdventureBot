from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import System
import System.Linq.Expressions
import IronPython.Compiler
import IronPython.Compiler.GeneratorRewriter

T = typing.TypeVar('T')

class GotoRewriteInfo(System.ValueType):
    @typing.overload
    def __init__(self, **kwargs):
        self.Variable: System.Linq.Expressions.Expression
        self.VoidTarget: System.Linq.Expressions.LabelTarget
        ...

    # static fields

    # properties
    # methods
    def __init__(self, variable: System.Linq.Expressions.Expression, voidTarget: System.Linq.Expressions.LabelTarget, ):
        ...

class YieldMarker(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        self.Label: System.Linq.Expressions.LabelTarget
        self.State: int
        ...

    # static fields

    # properties
    # methods
    def __init__(self, state: int, ):
        ...

class RethrowRewriter(System.Linq.Expressions.ExpressionVisitor):
    @typing.overload
    def __init__(self, **kwargs):
        self.Exception: System.Linq.Expressions.Expression
        ...

    # static fields

    # properties
    # methods
    def __init__(self, ):
        ...

    def VisitUnary(self, node: System.Linq.Expressions.UnaryExpression, ) -> System.Linq.Expressions.Expression:
        ...

    def VisitLambda(self, node: System.Linq.Expressions.Expression[T], ) -> System.Linq.Expressions.Expression:
        ...

    def VisitTry(self, node: System.Linq.Expressions.TryExpression, ) -> System.Linq.Expressions.Expression:
        ...

    def VisitExtension(self, node: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.Expression:
        ...

class GotoRewriter(System.Linq.Expressions.ExpressionVisitor):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    def __init__(self, rewriter: IronPython.Compiler.GeneratorRewriter, gotoInfo: IronPython.Compiler.GeneratorRewriter.GotoRewriteInfo, target: System.Linq.Expressions.LabelTarget, ):
        ...

    def VisitGoto(self, node: System.Linq.Expressions.GotoExpression, ) -> System.Linq.Expressions.Expression:
        ...

