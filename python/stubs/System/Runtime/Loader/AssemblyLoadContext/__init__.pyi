from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import System
import System.Runtime.Loader


class ContextualReflectionScope(System.IDisposable, System.ValueType):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    def __init__(self, activating: System.Runtime.Loader.AssemblyLoadContext, ):
        ...

    def Dispose(self, ) -> None:
        ...

