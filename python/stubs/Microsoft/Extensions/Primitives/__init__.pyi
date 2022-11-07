from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import System


class IChangeToken(abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    @abc.abstractmethod
    def HasChanged(self) -> bool:
        ...

    @property
    @abc.abstractmethod
    def ActiveChangeCallbacks(self) -> bool:
        ...

    # methods
    @abc.abstractmethod
    def RegisterChangeCallback(self, callback: System.Action[System.Object], state: System.Object, ) -> System.IDisposable:
        ...

