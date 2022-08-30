from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import System


class Events(System.Object, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    # methods
