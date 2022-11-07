from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import System


class EnumInfo(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        self.HasFlagsAttribute: bool
        self.Values: System.Array[int]
        self.Names: System.Array[str]
        ...

    # static fields

    # properties
    # methods
    def __init__(self, hasFlagsAttribute: bool, values: System.Array[int], names: System.Array[str], ):
        ...

