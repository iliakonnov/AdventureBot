from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import System


class ElapsedEventArgs(System.EventArgs):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def SignalTime(self) -> System.DateTime:
        ...

    # methods
    def __init__(self, localTime: System.DateTime, ):
        ...

