from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import System.Linq.Expressions
import IronPython.Runtime
import System

T = typing.TypeVar('T')

class InnerMethodProfiler(System.Linq.Expressions.DynamicExpressionVisitor):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    def __init__(self, profiler: IronPython.Runtime.Profiler, tick: System.Linq.Expressions.ParameterExpression, profileIndex: int, ):
        ...

    def VisitDynamic(self, node: System.Linq.Expressions.DynamicExpression, ) -> System.Linq.Expressions.Expression:
        ...

    def VisitExtension(self, node: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.Expression:
        ...

    def VisitMethodCall(self, node: System.Linq.Expressions.MethodCallExpression, ) -> System.Linq.Expressions.Expression:
        ...

    def VisitLambda(self, node: System.Linq.Expressions.Expression[T], ) -> System.Linq.Expressions.Expression:
        ...

class Data(System.ValueType):
    @typing.overload
    def __init__(self, **kwargs):
        self.Name: str
        self.InclusiveTime: int
        self.ExclusiveTime: int
        self.Calls: int
        ...

    # static fields

    # properties
    # methods
    def __init__(self, _name: str, _inclusive: int, _exclusive: int, _calls: int, ):
        ...

