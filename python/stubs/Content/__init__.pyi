from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import AdventureBot.Room
import System


class TownRoot(AdventureBot.Room.IRoot, System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields
    Id: str = ...

    # properties
    @property
    def Identifier(self) -> str:
        ...

    @property
    def RootRoomId(self) -> str:
        ...

    # methods
    def __init__(self, ):
        ...

