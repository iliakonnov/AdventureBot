from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import System.Text


class ProxyDecoderFallback(System.Text.DecoderFallback):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def MaxCharCount(self) -> int:
        ...

    # methods
    def __init__(self, buffer: System.Text.DecoderFallbackBuffer, maxCharCount: int, ):
        ...

    def CreateFallbackBuffer(self, ) -> System.Text.DecoderFallbackBuffer:
        ...

