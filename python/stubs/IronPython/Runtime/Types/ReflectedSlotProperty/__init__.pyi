from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import System
import IronPython.Runtime.Types


class SlotValue(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        self.Getter: IronPython.Runtime.Types.SlotGetValue
        self.Setter: IronPython.Runtime.Types.SlotSetValue
        ...

    # static fields

    # properties
    # methods
    def __init__(self, ):
        ...

