from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import System


class CallbackInfo(System.ValueType):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def Callback(self) -> System.Object:
        ...

    @property
    def WeakRef(self) -> System.Object:
        ...

    # methods
    def __init__(self, callback: System.Object, weakRef: System.Object, ):
        ...

    def Free(self, ) -> None:
        ...

