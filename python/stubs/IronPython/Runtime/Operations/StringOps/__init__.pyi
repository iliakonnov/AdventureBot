from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import System.Text
import System
import IronPython.Runtime.LiteralParser
import System.Collections.Generic
import System.Collections.Concurrent
import System.Runtime.Serialization
import System.Reflection
import IronPython.Runtime
import IronPython.Runtime.Operations.StringOps


class ExceptionFallback(System.Text.DecoderFallback):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def MaxCharCount(self) -> int:
        ...

    # methods
    def __init__(self, isUtf8: bool = ..., ):
        ...

    def CreateFallbackBuffer(self, ) -> System.Text.DecoderFallbackBuffer:
        ...

class UnicodeEscapeEncoding(System.ICloneable, System.Text.Encoding):
    @typing.overload
    def __init__(self, **kwargs):
        self._codePage: int
        self._dataItem: System.Text.CodePageDataItem
        self.encoderFallback: System.Text.EncoderFallback
        self.decoderFallback: System.Text.DecoderFallback
        ...

    # static fields

    # properties
    @property
    def EncodingName(self) -> str:
        ...

    @property
    def Preamble(self) -> System.ReadOnlySpan[int]:
        ...

    @property
    def BodyName(self) -> str:
        ...

    @property
    def HeaderName(self) -> str:
        ...

    @property
    def WebName(self) -> str:
        ...

    @property
    def WindowsCodePage(self) -> int:
        ...

    @property
    def IsBrowserDisplay(self) -> bool:
        ...

    @property
    def IsBrowserSave(self) -> bool:
        ...

    @property
    def IsMailNewsDisplay(self) -> bool:
        ...

    @property
    def IsMailNewsSave(self) -> bool:
        ...

    @property
    def IsSingleByte(self) -> bool:
        ...

    @property
    def EncoderFallback(self) -> System.Text.EncoderFallback:
        ...
    @EncoderFallback.setter
    def EncoderFallback(self, val: System.Text.EncoderFallback):
        ...

    @property
    def DecoderFallback(self) -> System.Text.DecoderFallback:
        ...
    @DecoderFallback.setter
    def DecoderFallback(self, val: System.Text.DecoderFallback):
        ...

    @property
    def IsReadOnly(self) -> bool:
        ...
    @IsReadOnly.setter
    def IsReadOnly(self, val: bool):
        ...

    @property
    def CodePage(self) -> int:
        ...

    @property
    def IsUTF8CodePage(self) -> bool:
        ...

    # methods
    def __init__(self, raw: bool, ):
        ...

    def EscapeEncode(self, s: str, index: int, count: int, ) -> str:
        ...

    @typing.overload
    def GetByteCount(self, s: str, ) -> int:
        ...

    @typing.overload
    def GetByteCount(self, chars: System.Array[str], index: int, count: int, ) -> int:
        ...

    @typing.overload
    def GetBytes(self, s: str, charIndex: int, charCount: int, bytes: System.Array[int], byteIndex: int, ) -> int:
        ...

    @typing.overload
    def GetBytes(self, chars: System.Array[str], charIndex: int, charCount: int, bytes: System.Array[int], byteIndex: int, ) -> int:
        ...

    @typing.overload
    def GetString(self, bytes: System.Array[int], index: int, count: int, ) -> str:
        ...

    @typing.overload
    def GetString(self, bytes: System.ReadOnlySpan[int], ) -> str:
        ...

    @typing.overload
    def GetCharCount(self, bytes: ptr[int], count: int, ) -> int:
        ...

    @typing.overload
    def GetCharCount(self, bytes: System.Array[int], index: int, count: int, ) -> int:
        ...

    @typing.overload
    def GetChars(self, bytes: ptr[int], byteCount: int, chars: ptr[str], charCount: int, ) -> int:
        ...

    @typing.overload
    def GetChars(self, bytes: System.Array[int], byteIndex: int, byteCount: int, chars: System.Array[str], charIndex: int, ) -> int:
        ...

    def GetMaxByteCount(self, charCount: int, ) -> int:
        ...

    def GetMaxCharCount(self, byteCount: int, ) -> int:
        ...

    def GetErrorHandler(self, ) -> IronPython.Runtime.LiteralParser.ParseStringErrorHandler[int]:
        ...

class CodecsInfo(System.Object, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields
    MbcsEncoding: System.Text.Encoding = ...
    RawUnicodeEscapeEncoding: System.Text.Encoding = ...
    UnicodeEscapeEncoding: System.Text.Encoding = ...
    Codecs: System.Collections.Generic.IDictionary[str, System.Lazy[System.Text.Encoding]] = ...
    Aliases: System.Lazy[System.Collections.Generic.IReadOnlyDictionary[str, str]] = ...
    ReverseAliases: System.Lazy[System.Collections.Generic.IReadOnlyDictionary[str, System.Collections.Generic.List[str]]] = ...

    # properties
    # methods
    @staticmethod
    def MakeCodecsDict() -> System.Collections.Concurrent.ConcurrentDictionary[str, System.Lazy[System.Text.Encoding]]:
        ...

    @staticmethod
    def MakeErrorHandlersDict() -> System.Collections.Concurrent.ConcurrentDictionary[str, System.Object]:
        ...

class ExceptionFallbackBuffer(System.Text.DecoderFallbackBuffer):
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
    def Remaining(self) -> int:
        ...

    # methods
    def __init__(self, ):
        ...

    def Fallback(self, bytesUnknown: System.Array[int], index: int, ) -> bool:
        ...

    def GetNextChar(self, ) -> str:
        ...

    def MovePrevious(self, ) -> bool:
        ...

class EncodeErrorHandler(System.ICloneable, System.Runtime.Serialization.ISerializable, System.MulticastDelegate):
    @typing.overload
    def __init__(self, **kwargs):
        self._target: System.Object
        self._methodBase: System.Object
        self._methodPtr: System.IntPtr
        self._methodPtrAux: System.IntPtr
        ...

    # static fields

    # properties
    @property
    def Target(self) -> System.Object:
        ...

    @property
    def Method(self) -> System.Reflection.MethodInfo:
        ...

    # methods
    def __init__(self, object: System.Object, method: System.IntPtr, ):
        ...

    def Invoke(self, text: str, start: int, end: ref[int], ) -> IronPython.Runtime.Bytes:
        ...

    def BeginInvoke(self, text: str, start: int, end: ref[int], callback: System.AsyncCallback, object: System.Object, ) -> System.IAsyncResult:
        ...

    def EndInvoke(self, end: ref[int], result: System.IAsyncResult, ) -> IronPython.Runtime.Bytes:
        ...

class XmlCharRefEncoderReplaceFallback(System.Text.EncoderFallback):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def MaxCharCount(self) -> int:
        ...

    # methods
    def __init__(self, ):
        ...

    def CreateFallbackBuffer(self, ) -> System.Text.EncoderFallbackBuffer:
        ...

class BackslashEncoderReplaceFallback(System.Text.EncoderFallback):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def MaxCharCount(self) -> int:
        ...

    # methods
    def __init__(self, ):
        ...

    def CreateFallbackBuffer(self, ) -> System.Text.EncoderFallbackBuffer:
        ...

class ExceptionFallbackBufferUtf8DotNet(IronPython.Runtime.Operations.StringOps.ExceptionFallbackBuffer):
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
    def Remaining(self) -> int:
        ...

    # methods
    def __init__(self, ):
        ...

    def Fallback(self, bytesUnknown: System.Array[int], index: int, ) -> bool:
        ...

class DecodeErrorHandler(System.ICloneable, System.Runtime.Serialization.ISerializable, System.MulticastDelegate):
    @typing.overload
    def __init__(self, **kwargs):
        self._target: System.Object
        self._methodBase: System.Object
        self._methodPtr: System.IntPtr
        self._methodPtrAux: System.IntPtr
        ...

    # static fields

    # properties
    @property
    def Target(self) -> System.Object:
        ...

    @property
    def Method(self) -> System.Reflection.MethodInfo:
        ...

    # methods
    def __init__(self, object: System.Object, method: System.IntPtr, ):
        ...

    def Invoke(self, bytes: System.Collections.Generic.IList[int], start: int, end: ref[int], ) -> str:
        ...

    def BeginInvoke(self, bytes: System.Collections.Generic.IList[int], start: int, end: ref[int], callback: System.AsyncCallback, object: System.Object, ) -> System.IAsyncResult:
        ...

    def EndInvoke(self, end: ref[int], result: System.IAsyncResult, ) -> str:
        ...

