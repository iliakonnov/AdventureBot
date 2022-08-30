from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import System


class Generator(System.Object, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    # methods
    @typing.overload
    @staticmethod
    def Generate(rnd: System.Random, ) -> System.String:
        ...

class Names(System.Object, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    # methods
