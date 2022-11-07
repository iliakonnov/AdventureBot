from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import System


class NullImporter(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    def __init__(self, path_string: str, ):
        ...

    def find_module(self, args: System.Array[System.Object], ) -> System.Object:
        ...

