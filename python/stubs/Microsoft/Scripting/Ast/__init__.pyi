from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import System.Linq.Expressions
import System.Collections.Generic
import System
import Microsoft.Scripting.Ast

T = typing.TypeVar('T')

class LightLambdaExpression(System.Linq.Expressions.Expression):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def Body(self) -> System.Linq.Expressions.Expression:
        ...

    @property
    def Name(self) -> str:
        ...

    @property
    def Parameters(self) -> System.Collections.Generic.IList[System.Linq.Expressions.ParameterExpression]:
        ...

    @property
    def NodeType(self) -> int:
        ...

    @property
    def CanReduce(self) -> bool:
        ...

    @property
    def ReturnType(self) -> System.Type:
        ...

    @property
    def Type(self) -> System.Type:
        ...

    # methods
    def __init__(self, retType: System.Type, body: System.Linq.Expressions.Expression, name: str, args: System.Collections.Generic.IList[System.Linq.Expressions.ParameterExpression], ):
        ...

    def ReduceToLambdaWorker(self, ) -> System.Linq.Expressions.LambdaExpression:
        ...

    @typing.overload
    def Compile(self, ) -> System.Delegate:
        ...

    @typing.overload
    def Compile(self, compilationThreshold: int, ) -> System.Delegate:
        ...

    def Reduce(self, ) -> System.Linq.Expressions.Expression:
        ...

class LightExpression(Microsoft.Scripting.Ast.LightLambdaExpression, typing.Generic[T]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def Type(self) -> System.Type:
        ...

    @property
    def Body(self) -> System.Linq.Expressions.Expression:
        ...

    @property
    def Name(self) -> str:
        ...

    @property
    def Parameters(self) -> System.Collections.Generic.IList[System.Linq.Expressions.ParameterExpression]:
        ...

    @property
    def NodeType(self) -> int:
        ...

    @property
    def CanReduce(self) -> bool:
        ...

    @property
    def ReturnType(self) -> System.Type:
        ...

    # methods
    def __init__(self, retType: System.Type, body: System.Linq.Expressions.Expression, name: str, args: System.Collections.Generic.IList[System.Linq.Expressions.ParameterExpression], ):
        ...

    def ReduceToLambda(self, ) -> System.Linq.Expressions.Expression[T]:
        ...

    @typing.overload
    def Compile(self, ) -> T:
        ...

    @typing.overload
    def Compile(self, compilationThreshold: int, ) -> T:
        ...

    def ReduceToLambdaWorker(self, ) -> System.Linq.Expressions.LambdaExpression:
        ...

