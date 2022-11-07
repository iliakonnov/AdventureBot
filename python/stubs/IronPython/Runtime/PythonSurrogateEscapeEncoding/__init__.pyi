from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import System
import IronPython.Runtime.PythonEncoding
import IronPython.Runtime
import System.Text


class SurrogateEscapeEncoderFallback(System.ICloneable, IronPython.Runtime.PythonEncoding.PythonEncoderFallback):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def MaxCharCount(self) -> int:
        ...

    @property
    def Encoding(self) -> IronPython.Runtime.PythonEncoding:
        ...
    @Encoding.setter
    def Encoding(self, val: IronPython.Runtime.PythonEncoding):
        ...

    @property
    def IsPass1(self) -> bool:
        ...
    @IsPass1.setter
    def IsPass1(self, val: bool):
        ...

    # methods
    def __init__(self, ):
        ...

    def CreateFallbackBuffer(self, ) -> System.Text.EncoderFallbackBuffer:
        ...

class SurrogateEscapeDecoderFallback(System.ICloneable, IronPython.Runtime.PythonEncoding.PythonDecoderFallback):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def MaxCharCount(self) -> int:
        ...

    @property
    def Encoding(self) -> IronPython.Runtime.PythonEncoding:
        ...
    @Encoding.setter
    def Encoding(self, val: IronPython.Runtime.PythonEncoding):
        ...

    @property
    def IsPass1(self) -> bool:
        ...
    @IsPass1.setter
    def IsPass1(self, val: bool):
        ...

    # methods
    def __init__(self, ):
        ...

    def CreateFallbackBuffer(self, ) -> System.Text.DecoderFallbackBuffer:
        ...

class SurrogateEscapeDecoderFallbackBuffer(IronPython.Runtime.PythonEncoding.PythonDecoderFallbackBuffer):
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
    def __init__(self, isPass1: bool, encoding: IronPython.Runtime.PythonEncoding, ):
        ...

    def GetFallbackChars(self, bytesUnknown: System.Array[int], index: int, ) -> System.ReadOnlyMemory[str]:
        ...

class SurrogateEscapeEncoderFallbackBuffer(IronPython.Runtime.PythonEncoding.PythonEncoderFallbackBuffer):
    @typing.overload
    def __init__(self, **kwargs):
        self.charStart: ptr[str]
        self.charEnd: ptr[str]
        self.encoder: System.Text.EncoderNLS
        self.setEncoder: bool
        self.bUsedEncoder: bool
        self.bFallingBack: bool
        self.iRecursionCount: int
        ...

    # static fields

    # properties
    @property
    def EncodingMode(self) -> bool:
        ...

    @property
    def EncodingCharWidth(self) -> int:
        ...

    @property
    def CodePage(self) -> int:
        ...

    @property
    def Data(self) -> str:
        ...

    @property
    def Remaining(self) -> int:
        ...

    @property
    def IsEmpty(self) -> bool:
        ...

    # methods
    def __init__(self, isPass1: bool, encoding: IronPython.Runtime.PythonEncoding, ):
        ...

    def GetFallbackCharsOrBytes(self, runeUnknown: int, index: int, ) -> System.Tuple[System.ReadOnlyMemory[str], System.ReadOnlyMemory[int]]:
        ...

