from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import System
import System.Runtime.CompilerServices

T = typing.TypeVar('T')

class IdentityConversion(System.Object, typing.Generic[T]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    def __init__(self, type: System.Type, ):
        ...

    def Convert(self, site: System.Runtime.CompilerServices.CallSite, value: System.Object, ) -> T:
        ...

class IdentityConversion(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    def __init__(self, type: System.Type, ):
        ...

    def Convert(self, site: System.Runtime.CompilerServices.CallSite, value: System.Object, ) -> System.Object:
        ...

