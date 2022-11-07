from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import System
import System.ComponentModel.EventHandlerList


class ListEntry(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        self._next: System.ComponentModel.EventHandlerList.ListEntry
        self._key: System.Object
        self._handler: System.Delegate
        ...

    # static fields

    # properties
    # methods
    def __init__(self, key: System.Object, handler: System.Delegate, next: System.ComponentModel.EventHandlerList.ListEntry, ):
        ...

