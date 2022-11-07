from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import System
import IronPython.Runtime


class GeneratorFlags(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    None_: int = ...
    Closed: int = ...
    CanSetSysExcInfo: int = ...

class GeneratorFinalizer(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        self.Generator: IronPython.Runtime.PythonGenerator
        ...

    # static fields

    # properties
    # methods
    def __init__(self, generator: IronPython.Runtime.PythonGenerator, ):
        ...

    def Finalize(self, ) -> None:
        ...

