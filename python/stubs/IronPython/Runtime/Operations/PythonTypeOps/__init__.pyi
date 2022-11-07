from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import System
import Microsoft.Scripting.Runtime.ReflectionCache


class BuiltinFunctionKey(System.ValueType):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    def __init__(self, declaringType: System.Type, cache: Microsoft.Scripting.Runtime.ReflectionCache.MethodBaseCache, funcType: int, ):
        ...

