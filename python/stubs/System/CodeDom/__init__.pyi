from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import System
import System.Collections


class CodeObject(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def UserData(self) -> System.Collections.IDictionary:
        ...

    # methods
    def __init__(self, ):
        ...

