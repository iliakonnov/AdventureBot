from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import System
import Microsoft.Scripting
import System.IO


class PALHolder(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    def __init__(self, pal: Microsoft.Scripting.PlatformAdaptationLayer, ):
        ...

    def GetStream(self, path: str, ) -> System.IO.Stream:
        ...

