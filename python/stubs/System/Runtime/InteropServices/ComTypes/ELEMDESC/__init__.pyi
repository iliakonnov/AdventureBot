from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import System
import System.Runtime.InteropServices.ComTypes


class DESCUNION(System.ValueType):
    @typing.overload
    def __init__(self, **kwargs):
        self.idldesc: System.Runtime.InteropServices.ComTypes.IDLDESC
        self.paramdesc: System.Runtime.InteropServices.ComTypes.PARAMDESC
        ...

    # static fields

    # properties
    # methods
