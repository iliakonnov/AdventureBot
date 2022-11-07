from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import System


class CriticalFinalizerObject(System.Object, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    def __init__(self, ):
        ...

    def Finalize(self, ) -> None:
        ...

