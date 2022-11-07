from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import System


class bucket(System.ValueType):
    @typing.overload
    def __init__(self, **kwargs):
        self.key: System.Object
        self.val: System.Object
        self.hash_coll: int
        ...

    # static fields

    # properties
    # methods
