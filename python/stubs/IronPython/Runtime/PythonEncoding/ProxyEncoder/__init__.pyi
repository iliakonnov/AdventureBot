from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import System.Text


class ProxyEncoderFallback(System.Text.EncoderFallback):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def MaxCharCount(self) -> int:
        ...

    # methods
    def __init__(self, buffer: System.Text.EncoderFallbackBuffer, maxCharCount: int, ):
        ...

    def CreateFallbackBuffer(self, ) -> System.Text.EncoderFallbackBuffer:
        ...

