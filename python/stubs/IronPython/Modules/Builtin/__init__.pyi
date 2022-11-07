from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import System
import System.Numerics
import System.Runtime.CompilerServices
import IronPython.Runtime


class SumState(System.ValueType):
    @typing.overload
    def __init__(self, **kwargs):
        self.DoubleVal: float
        self.IntVal: int
        self.ObjectVal: System.Object
        self.BigIntVal: System.Numerics.BigInteger
        self.CurType: int
        self.AddSite: System.Runtime.CompilerServices.CallSite[System.Func[System.Runtime.CompilerServices.CallSite, System.Object, System.Object, System.Object]]
        ...

    # static fields

    # properties
    @property
    def CurrentValue(self) -> System.Object:
        ...

    # methods
    def __init__(self, context: IronPython.Runtime.PythonContext, start: System.Object, ):
        ...

class SumVariantType(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    Double: int = ...
    Int: int = ...
    BigInt: int = ...
    Object: int = ...

