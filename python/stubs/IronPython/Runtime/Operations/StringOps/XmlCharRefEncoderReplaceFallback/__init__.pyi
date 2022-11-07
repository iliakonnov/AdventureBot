from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import System.Text


class XmlCharRefEncoderReplaceFallbackBuffer(System.Text.EncoderFallbackBuffer):
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
    def Remaining(self) -> int:
        ...

    # methods
    def __init__(self, ):
        ...

    @typing.overload
    def Fallback(self, charUnknownHigh: str, charUnknownLow: str, index: int, ) -> bool:
        ...

    @typing.overload
    def Fallback(self, charUnknown: str, index: int, ) -> bool:
        ...

    def GetNextChar(self, ) -> str:
        ...

    def MovePrevious(self, ) -> bool:
        ...

