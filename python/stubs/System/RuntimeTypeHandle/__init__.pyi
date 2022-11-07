from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import System
import System.RuntimeTypeHandle


class IntroducedMethodEnumerator(System.ValueType):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def Current(self) -> System.RuntimeMethodHandleInternal:
        ...

    # methods
    def __init__(self, type: System.RuntimeType, ):
        ...

    def MoveNext(self, ) -> bool:
        ...

    def GetEnumerator(self, ) -> System.RuntimeTypeHandle.IntroducedMethodEnumerator:
        ...

