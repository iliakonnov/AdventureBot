from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import System
import System.Collections.Generic


class HandlerList(System.Object, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    def __init__(self, ):
        ...

    @abc.abstractmethod
    def AddHandler(self, callableObject: System.Object, handler: System.Delegate, ) -> None:
        ...

    @abc.abstractmethod
    def RemoveHandler(self, callableObject: System.Object, comparer: System.Collections.Generic.IEqualityComparer[System.Object], ) -> System.Delegate:
        ...

