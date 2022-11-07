from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import System


class Bucket(System.ValueType):
    @typing.overload
    def __init__(self, **kwargs):
        self.Item: System.Object
        self.HashCode: int
        ...

    # static fields

    # properties
    # methods
    def __init__(self, hashCode: int, item: System.Object, ):
        ...

