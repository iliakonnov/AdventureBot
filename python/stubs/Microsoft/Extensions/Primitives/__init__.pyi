from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import System


class IChangeToken(abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @abc.abstractmethod
    @property
    def HasChanged(self) -> System.Boolean:
        ...

    @abc.abstractmethod
    @property
    def ActiveChangeCallbacks(self) -> System.Boolean:
        ...

    # methods
    @typing.overload
    @abc.abstractmethod
    def RegisterChangeCallback(self, callback: System.Action[System.Object], state: System.Object, ) -> System.IDisposable:
        ...

