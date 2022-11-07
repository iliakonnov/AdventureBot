from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import System


class StackAllocedArguments(System.ValueType):
    @typing.overload
    def __init__(self, **kwargs):
        self._arg0: System.Object
        ...

    # static fields

    # properties
    # methods
