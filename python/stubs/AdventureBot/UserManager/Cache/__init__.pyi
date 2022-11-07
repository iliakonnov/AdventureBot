from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import System
import AdventureBot.UserManager


class CachedUser(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        self.Flushed: bool
        ...

    # static fields

    # properties
    @property
    def UserData(self) -> AdventureBot.UserManager.UserData:
        ...
    @UserData.setter
    def UserData(self, val: AdventureBot.UserManager.UserData):
        ...

    @property
    def LastRequested(self) -> System.DateTimeOffset:
        ...
    @LastRequested.setter
    def LastRequested(self, val: System.DateTimeOffset):
        ...

    # methods
    def __init__(self, ):
        ...

