from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import System


class Names(System.Object, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields
    NounsCounts: System.Array[int] = ...
    AdjectivesCounts: System.Array[int] = ...
    Nouns: System.Array[System.Array[str]] = ...
    Adjectives: System.Array[System.Array[str]] = ...

    # properties
    # methods
class Generator(System.Object, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    @staticmethod
    def Generate(rnd: System.Random, ) -> str:
        ...

