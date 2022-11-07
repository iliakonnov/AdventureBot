from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import System.Text
import IronPython.Runtime
import System
import IronPython.Runtime.PythonEncoding


class PythonEncoderFallbackBuffer(System.Text.EncoderFallbackBuffer, abc.ABC):
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
    @EncodingMode.setter
    def EncodingMode(self, val: bool):
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
    @Data.setter
    def Data(self, val: str):
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

    @abc.abstractmethod
    def GetFallbackCharsOrBytes(self, runeUnknown: int, index: int, ) -> System.Tuple[System.ReadOnlyMemory[str], System.ReadOnlyMemory[int]]:
        ...

    def FinalizeIncrement(self, endIndex: int, flush: bool, ) -> None:
        ...

    def PrepareIncrement(self, data: str, forEncoding: bool, ) -> None:
        ...

    @typing.overload
    def Fallback(self, charUnknown: str, index: int, ) -> bool:
        ...

    @typing.overload
    def Fallback(self, charUnknownHigh: str, charUnknownLow: str, index: int, ) -> bool:
        ...

    def FallbackImpl(self, runeUnknown: int, index: int, ) -> bool:
        ...

    def GetNextChar(self, ) -> str:
        ...

    def MovePrevious(self, ) -> bool:
        ...

    def GetFallbackByte(self, ) -> int:
        ...

    def Reset(self, ) -> None:
        ...

class PythonDecoderFallbackBuffer(System.Text.DecoderFallbackBuffer, abc.ABC):
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
    @DecodingMode.setter
    def DecodingMode(self, val: bool):
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

    def PrepareIncrement(self, forDecoding: bool, ) -> None:
        ...

    @abc.abstractmethod
    def GetFallbackChars(self, bytesUnknown: System.Array[int], index: int, ) -> System.ReadOnlyMemory[str]:
        ...

    def Fallback(self, bytesUnknown: System.Array[int], index: int, ) -> bool:
        ...

    def GetNextChar(self, ) -> str:
        ...

    def MovePrevious(self, ) -> bool:
        ...

    def GetFallbackChar(self, ) -> str:
        ...

    def FinalizeIncrement(self, endIndex: int, flush: bool, ) -> None:
        ...

    def Reset(self, ) -> None:
        ...

class PythonDecoder(System.Text.Decoder):
    @typing.overload
    def __init__(self, **kwargs):
        self._fallback: System.Text.DecoderFallback
        self._fallbackBuffer: System.Text.DecoderFallbackBuffer
        ...

    # static fields

    # properties
    @property
    def Fallback(self) -> System.Text.DecoderFallback:
        ...
    @Fallback.setter
    def Fallback(self, val: System.Text.DecoderFallback):
        ...

    @property
    def FallbackBuffer(self) -> System.Text.DecoderFallbackBuffer:
        ...

    @property
    def InternalHasFallbackBuffer(self) -> bool:
        ...

    # methods
    def __init__(self, parentEncoding: IronPython.Runtime.PythonEncoding, ):
        ...

    @staticmethod
    def GetDecoder(encoding: System.Text.Encoding, ) -> System.Text.Decoder:
        ...

    @staticmethod
    def GetPythonDecoderFallbackBuffer(dec: System.Text.Decoder, ) -> IronPython.Runtime.PythonEncoding.PythonDecoderFallbackBuffer:
        ...

    @typing.overload
    def GetCharCount(self, bytes: System.Array[int], index: int, count: int, ) -> int:
        ...

    @typing.overload
    def GetCharCount(self, bytes: System.Array[int], index: int, count: int, flush: bool, ) -> int:
        ...

    @typing.overload
    def GetCharCount(self, bytes: ptr[int], count: int, flush: bool, ) -> int:
        ...

    @typing.overload
    def GetChars(self, bytes: System.Array[int], byteIndex: int, byteCount: int, chars: System.Array[str], charIndex: int, ) -> int:
        ...

    @typing.overload
    def GetChars(self, bytes: System.Array[int], byteIndex: int, byteCount: int, chars: System.Array[str], charIndex: int, flush: bool, ) -> int:
        ...

    @typing.overload
    def GetChars(self, bytes: ptr[int], byteCount: int, chars: ptr[str], charCount: int, flush: bool, ) -> int:
        ...

    @typing.overload
    def GetChars(self, bytes: System.ReadOnlySpan[int], chars: System.Span[str], flush: bool, ) -> int:
        ...

    def GetString(self, input: IronPython.Runtime.IPythonBuffer, index: int, count: int, ) -> str:
        ...

    def Reset(self, ) -> None:
        ...

class MemInt(System.ValueType):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def Initial(self) -> int:
        ...

    # methods
    def __init__(self, current: int, initial: int, ):
        ...

class PythonDecoderFallback(System.ICloneable, System.Text.DecoderFallback, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
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

    @property
    @abc.abstractmethod
    def MaxCharCount(self) -> int:
        ...

    # methods
    def __init__(self, ):
        ...

    def Clone(self, ) -> System.Object:
        ...

class PythonEncoderFallback(System.ICloneable, System.Text.EncoderFallback, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
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

    @property
    @abc.abstractmethod
    def MaxCharCount(self) -> int:
        ...

    # methods
    def __init__(self, ):
        ...

    def Clone(self, ) -> System.Object:
        ...

class PythonEncoder(System.Text.Encoder):
    @typing.overload
    def __init__(self, **kwargs):
        self._fallback: System.Text.EncoderFallback
        self._fallbackBuffer: System.Text.EncoderFallbackBuffer
        ...

    # static fields

    # properties
    @property
    def Fallback(self) -> System.Text.EncoderFallback:
        ...
    @Fallback.setter
    def Fallback(self, val: System.Text.EncoderFallback):
        ...

    @property
    def FallbackBuffer(self) -> System.Text.EncoderFallbackBuffer:
        ...

    @property
    def InternalHasFallbackBuffer(self) -> bool:
        ...

    # methods
    def __init__(self, parentEncoding: IronPython.Runtime.PythonEncoding, ):
        ...

    @staticmethod
    def GetEncoder(encoding: System.Text.Encoding, ) -> System.Text.Encoder:
        ...

    @staticmethod
    def GetPythonEncoderFallbackBuffer(enc: System.Text.Encoder, ) -> IronPython.Runtime.PythonEncoding.PythonEncoderFallbackBuffer:
        ...

    @typing.overload
    def GetByteCount(self, chars: System.Array[str], index: int, count: int, flush: bool, ) -> int:
        ...

    @typing.overload
    def GetByteCount(self, chars: ptr[str], count: int, flush: bool, ) -> int:
        ...

    @typing.overload
    def GetByteCount(self, s: str, flush: bool, ) -> int:
        ...

    @typing.overload
    def GetBytes(self, chars: System.Array[str], charIndex: int, charCount: int, bytes: System.Array[int], byteIndex: int, flush: bool, ) -> int:
        ...

    @typing.overload
    def GetBytes(self, chars: ptr[str], charCount: int, bytes: ptr[int], byteCount: int, flush: bool, ) -> int:
        ...

    @typing.overload
    def GetBytes(self, s: str, charIndex: int, charCount: int, bytes: System.Array[int], byteIndex: int, flush: bool, ) -> int:
        ...

    @typing.overload
    def GetBytes(self, data: str, bytes: System.Span[int], flush: bool, ) -> int:
        ...

    def Reset(self, ) -> None:
        ...

class ProxyDecoder(System.Text.Decoder):
    @typing.overload
    def __init__(self, **kwargs):
        self._fallback: System.Text.DecoderFallback
        self._fallbackBuffer: System.Text.DecoderFallbackBuffer
        ...

    # static fields

    # properties
    @property
    def Fallback(self) -> System.Text.DecoderFallback:
        ...
    @Fallback.setter
    def Fallback(self, val: System.Text.DecoderFallback):
        ...

    @property
    def FallbackBuffer(self) -> System.Text.DecoderFallbackBuffer:
        ...

    @property
    def InternalHasFallbackBuffer(self) -> bool:
        ...

    # methods
    def __init__(self, encoding: System.Text.Encoding, ):
        ...

    @typing.overload
    def GetCharCount(self, bytes: System.Array[int], index: int, count: int, ) -> int:
        ...

    @typing.overload
    def GetCharCount(self, bytes: System.Array[int], index: int, count: int, flush: bool, ) -> int:
        ...

    @typing.overload
    def GetCharCount(self, bytes: ptr[int], count: int, flush: bool, ) -> int:
        ...

    @typing.overload
    def GetChars(self, bytes: System.Array[int], byteIndex: int, byteCount: int, chars: System.Array[str], charIndex: int, ) -> int:
        ...

    @typing.overload
    def GetChars(self, bytes: System.Array[int], byteIndex: int, byteCount: int, chars: System.Array[str], charIndex: int, flush: bool, ) -> int:
        ...

    @typing.overload
    def GetChars(self, bytes: ptr[int], byteCount: int, chars: ptr[str], charCount: int, flush: bool, ) -> int:
        ...

    def Reset(self, ) -> None:
        ...

class ProxyEncoder(System.Text.Encoder):
    @typing.overload
    def __init__(self, **kwargs):
        self._fallback: System.Text.EncoderFallback
        self._fallbackBuffer: System.Text.EncoderFallbackBuffer
        ...

    # static fields

    # properties
    @property
    def Fallback(self) -> System.Text.EncoderFallback:
        ...
    @Fallback.setter
    def Fallback(self, val: System.Text.EncoderFallback):
        ...

    @property
    def FallbackBuffer(self) -> System.Text.EncoderFallbackBuffer:
        ...

    @property
    def InternalHasFallbackBuffer(self) -> bool:
        ...

    # methods
    def __init__(self, encoding: System.Text.Encoding, ):
        ...

    @typing.overload
    def GetByteCount(self, chars: System.Array[str], index: int, count: int, flush: bool, ) -> int:
        ...

    @typing.overload
    def GetByteCount(self, chars: ptr[str], count: int, flush: bool, ) -> int:
        ...

    @typing.overload
    def GetBytes(self, chars: System.Array[str], charIndex: int, charCount: int, bytes: System.Array[int], byteIndex: int, flush: bool, ) -> int:
        ...

    @typing.overload
    def GetBytes(self, chars: ptr[str], charCount: int, bytes: ptr[int], byteCount: int, flush: bool, ) -> int:
        ...

    def Reset(self, ) -> None:
        ...

