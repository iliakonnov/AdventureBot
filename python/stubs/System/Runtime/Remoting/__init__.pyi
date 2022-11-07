from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import System


class ObjectHandle(System.MarshalByRefObject):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    def __init__(self, o: System.Object, ):
        ...

    def Unwrap(self, ) -> System.Object:
        ...

