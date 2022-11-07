from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import System.Linq.Expressions
import System


class DebugInfoRemovalExpression(System.Linq.Expressions.Expression):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def NodeType(self) -> int:
        ...

    @property
    def Type(self) -> System.Type:
        ...

    @property
    def CanReduce(self) -> bool:
        ...

    # methods
    def __init__(self, expression: System.Linq.Expressions.Expression, line: int, ):
        ...

    def Reduce(self, ) -> System.Linq.Expressions.Expression:
        ...

