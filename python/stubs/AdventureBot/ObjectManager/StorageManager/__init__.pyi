from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import System

T = typing.TypeVar('T')
TAttribute = typing.TypeVar('TAttribute')

class Item(System.Object, typing.Generic[T, TAttribute]):
    @typing.overload
    def __init__(self, **kwargs):
        self.Attribute: TAttribute
        self.Identificator: System.String
        ...

    # properties
    # methods
    @typing.overload
    def __init__(self, ):
        ...

