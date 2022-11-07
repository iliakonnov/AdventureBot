from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import IronPython.Runtime.PythonEncoding
import System.Text
import IronPython.Runtime
import System


class PythonHandlerEncoderFallbackBuffer(IronPython.Runtime.PythonEncoding.PythonEncoderFallbackBuffer):
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
    def __init__(self, isPass1: bool, encoding: IronPython.Runtime.PythonErrorHandlerEncoding, ):
        ...

    def GetFallbackCharsOrBytes(self, runeUnknown: int, index: int, ) -> System.Tuple[System.ReadOnlyMemory[str], System.ReadOnlyMemory[int]]:
        ...

    @staticmethod
    def ExtractEncodingReplacement(res: System.Object, cursorPos: int, ) -> System.Tuple[System.ReadOnlyMemory[str], System.ReadOnlyMemory[int]]:
        ...

    def FinalizeIncrement(self, endIndex: int, flush: bool, ) -> None:
        ...

class PythonHandlerDecoderFallback(System.ICloneable, IronPython.Runtime.PythonEncoding.PythonDecoderFallback):
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

class PythonHandlerEncoderFallback(System.ICloneable, IronPython.Runtime.PythonEncoding.PythonEncoderFallback):
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

