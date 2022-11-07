from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import System
import AdventureBot.ObjectManager

T = typing.TypeVar('T')
TAttribute = typing.TypeVar('TAttribute')

class Item(System.Object, typing.Generic[T, TAttribute]):
    @typing.overload
    def __init__(self, **kwargs):
        self.Attribute: TAttribute
        self.Creator: AdventureBot.ObjectManager.Create[T]
        self.Identificator: str
        ...

    # static fields

    # properties
    # methods
    def __init__(self, ):
        ...

