from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import IronPython.Runtime.PythonEncoding
import System.Text
import System
import IronPython.Runtime


class PythonHandlerDecoderFallbackBuffer(IronPython.Runtime.PythonEncoding.PythonDecoderFallbackBuffer):
    @typing.overload
    def __init__(self, **kwargs):
        self.byteStart: ptr[int]
        self.charEnd: ptr[str]
        self._encoding: System.Text.Encoding
        self._decoder: System.Text.DecoderNLS
        ...

    # static fields

    # properties
    @property
    def DecodingMode(self) -> bool:
        ...

    @property
    def EncodingCharWidth(self) -> int:
        ...

    @property
    def CodePage(self) -> int:
        ...

    @property
    def Data(self) -> System.Tuple[IronPython.Runtime.IPythonBuffer, int]:
        ...
    @Data.setter
    def Data(self, val: System.Tuple[IronPython.Runtime.IPythonBuffer, int]):
        ...

    @property
    def Remaining(self) -> int:
        ...

    @property
    def IsEmpty(self) -> bool:
        ...

    @property
    def FallbackCharCount(self) -> int:
        ...

    # methods
    def __init__(self, isPass1: bool, encoding: IronPython.Runtime.PythonErrorHandlerEncoding, ):
        ...

    def GetFallbackChars(self, bytesUnknown: System.Array[int], index: int, ) -> System.ReadOnlyMemory[str]:
        ...

    @staticmethod
    def ExtractDecodingReplacement(res: System.Object, cursorPos: int, ) -> System.ReadOnlyMemory[str]:
        ...

    def FinalizeIncrement(self, endIndex: int, flush: bool, ) -> None:
        ...

    def Reset(self, ) -> None:
        ...

