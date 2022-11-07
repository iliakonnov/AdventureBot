from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import IronPython.Runtime
import System
import System.Collections.Generic
import System.Buffers

T = typing.TypeVar('T')

class ArrayDataView(IronPython.Runtime.IPythonBuffer, System.IDisposable, System.Object, typing.Generic[T]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def Object(self) -> System.Object:
        ...

    @property
    def IsReadOnly(self) -> bool:
        ...

    @property
    def Offset(self) -> int:
        ...

    @property
    def Format(self) -> str:
        ...

    @property
    def ItemCount(self) -> int:
        ...

    @property
    def ItemSize(self) -> int:
        ...

    @property
    def NumOfDims(self) -> int:
        ...

    @property
    def Shape(self) -> System.Collections.Generic.IReadOnlyList[int]:
        ...

    @property
    def Strides(self) -> System.Collections.Generic.IReadOnlyList[int]:
        ...

    @property
    def SubOffsets(self) -> System.Collections.Generic.IReadOnlyList[int]:
        ...

    # methods
    def __init__(self, owner: System.Object, format: str, arrayData: IronPython.Runtime.ArrayData[T], flags: int, ):
        ...

    def Dispose(self, ) -> None:
        ...

    def AsReadOnlySpan(self, ) -> System.ReadOnlySpan[int]:
        ...

    def AsSpan(self, ) -> System.Span[int]:
        ...

    def Pin(self, ) -> System.Buffers.MemoryHandle:
        ...

