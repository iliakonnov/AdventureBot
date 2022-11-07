from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import System
import System.Collections.ObjectModel
import System.Linq.Expressions
import System.Runtime.CompilerServices.CallSiteBinder

T = typing.TypeVar('T')

class LambdaSignature(System.Object, typing.Generic[T]):
    @typing.overload
    def __init__(self, **kwargs):
        self.Parameters: System.Collections.ObjectModel.ReadOnlyCollection[System.Linq.Expressions.ParameterExpression]
        self.ReturnLabel: System.Linq.Expressions.LabelTarget
        ...

    # static fields

    # properties
    @property
    def Instance(self) -> System.Runtime.CompilerServices.CallSiteBinder.LambdaSignature:
        ...

    # methods
    def __init__(self, ):
        ...

