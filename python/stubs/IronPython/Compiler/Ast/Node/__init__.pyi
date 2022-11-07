from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import System.Linq.Expressions
import System


class FramedCodeExpression(System.Linq.Expressions.Expression):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def NodeType(self) -> int:
        ...

    @property
    def Body(self) -> System.Linq.Expressions.Expression:
        ...

    @property
    def Type(self) -> System.Type:
        ...

    @property
    def CanReduce(self) -> bool:
        ...

    # methods
    def __init__(self, localContext: System.Linq.Expressions.Expression, codeObject: System.Linq.Expressions.Expression, body: System.Linq.Expressions.Expression, ):
        ...

    def Reduce(self, ) -> System.Linq.Expressions.Expression:
        ...

    def VisitChildren(self, visitor: System.Linq.Expressions.ExpressionVisitor, ) -> System.Linq.Expressions.Expression:
        ...

class FramedCodeVisitor(System.Linq.Expressions.ExpressionVisitor):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    def __init__(self, ):
        ...

    def Visit(self, node: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.Expression:
        ...

