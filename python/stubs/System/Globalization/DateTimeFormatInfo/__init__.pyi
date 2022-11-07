from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import System


class TokenHashValue(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        self.tokenString: str
        self.tokenType: int
        self.tokenValue: int
        ...

    # static fields

    # properties
    # methods
    def __init__(self, tokenString: str, tokenType: int, tokenValue: int, ):
        ...

