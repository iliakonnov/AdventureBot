from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import System
import IronPython.Runtime.Types


class BadEventChange(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def Owner(self) -> IronPython.Runtime.Types.PythonType:
        ...

    @property
    def Instance(self) -> System.Object:
        ...

    # methods
    def __init__(self, ownerType: IronPython.Runtime.Types.PythonType, instance: System.Object, ):
        ...

class BoundEvent(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def Event(self) -> IronPython.Runtime.Types.ReflectedEvent:
        ...

    # methods
    def __init__(self, reflectedEvent: IronPython.Runtime.Types.ReflectedEvent, instance: System.Object, ownerType: IronPython.Runtime.Types.PythonType, ):
        ...

