from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import System.Runtime.InteropServices.ComTypes
import System


class IDispatch(abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    @abc.abstractmethod
    def GetTypeInfoCount(self, ) -> int:
        ...

    @abc.abstractmethod
    def GetTypeInfo(self, iTInfo: int, lcid: int, ) -> System.Runtime.InteropServices.ComTypes.ITypeInfo:
        ...

    @abc.abstractmethod
    def GetIDsOfNames(self, riid: ref[System.Guid], rgszNames: System.Array[str], cNames: int, lcid: int, rgDispId: System.Array[int], ) -> None:
        ...

