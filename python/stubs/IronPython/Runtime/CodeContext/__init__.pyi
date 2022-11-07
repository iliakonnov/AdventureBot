from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import System
import IronPython.Runtime


class DebugProxy(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def Members(self) -> IronPython.Runtime.PythonModule:
        ...

    # methods
    def __init__(self, context: IronPython.Runtime.CodeContext, ):
        ...

