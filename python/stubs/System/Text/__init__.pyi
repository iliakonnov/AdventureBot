from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import System
import System.Text
import System.Runtime.Serialization
import System.Text.StringBuilder
import System.Collections.Generic
import System.IO
import System.Reflection
import System.Collections
import System.Globalization

T = typing.TypeVar('T')

class EncoderFallbackBuffer(System.Object, abc.ABC):
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
    @abc.abstractmethod
    def Remaining(self) -> int:
        ...

    # methods
    def __init__(self, ):
        ...

    @abc.abstractmethod
    @typing.overload
    def Fallback(self, charUnknownHigh: str, charUnknownLow: str, index: int, ) -> bool:
        ...

    @abc.abstractmethod
    @typing.overload
    def Fallback(self, charUnknown: str, index: int, ) -> bool:
        ...

    @abc.abstractmethod
    def GetNextChar(self, ) -> str:
        ...

    @abc.abstractmethod
    def MovePrevious(self, ) -> bool:
        ...

    def Reset(self, ) -> None:
        ...

    def InternalReset(self, ) -> None:
        ...

    def InternalInitialize(self, charStart: ptr[str], charEnd: ptr[str], encoder: System.Text.EncoderNLS, setEncoder: bool, ) -> None:
        ...

    @staticmethod
    def CreateAndInitialize(encoding: System.Text.Encoding, encoder: System.Text.EncoderNLS, originalCharCount: int, ) -> System.Text.EncoderFallbackBuffer:
        ...

    def InternalGetNextChar(self, ) -> str:
        ...

    @typing.overload
    def InternalFallback(self, chars: System.ReadOnlySpan[str], charsConsumed: ref[int], ) -> bool:
        ...

    @typing.overload
    def InternalFallback(self, ch: str, chars: ref[ptr[str]], ) -> bool:
        ...

    def InternalFallbackGetByteCount(self, chars: System.ReadOnlySpan[str], charsConsumed: ref[int], ) -> int:
        ...

    def TryInternalFallbackGetBytes(self, chars: System.ReadOnlySpan[str], bytes: System.Span[int], charsConsumed: ref[int], bytesWritten: ref[int], ) -> bool:
        ...

    def TryDrainRemainingDataForGetBytes(self, bytes: System.Span[int], bytesWritten: ref[int], ) -> bool:
        ...

    def DrainRemainingDataForGetByteCount(self, ) -> int:
        ...

    def GetNextRune(self, ) -> System.Text.Rune:
        ...

    @staticmethod
    def ThrowLastCharRecursive(charRecursive: int, ) -> None:
        ...

class EncoderFallback(System.Object, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def ReplacementFallback(self) -> System.Text.EncoderFallback:
        ...

    @property
    def ExceptionFallback(self) -> System.Text.EncoderFallback:
        ...

    @property
    @abc.abstractmethod
    def MaxCharCount(self) -> int:
        ...

    # methods
    def __init__(self, ):
        ...

    @abc.abstractmethod
    def CreateFallbackBuffer(self, ) -> System.Text.EncoderFallbackBuffer:
        ...

class StringBuilder(System.Runtime.Serialization.ISerializable, System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        self.m_ChunkChars: System.Array[str]
        self.m_ChunkPrevious: System.Text.StringBuilder
        self.m_ChunkLength: int
        self.m_ChunkOffset: int
        self.m_MaxCapacity: int
        ...

    # static fields

    # properties
    @property
    def Capacity(self) -> int:
        ...
    @Capacity.setter
    def Capacity(self, val: int):
        ...

    @property
    def MaxCapacity(self) -> int:
        ...

    @property
    def Length(self) -> int:
        ...
    @Length.setter
    def Length(self, val: int):
        ...

    @property
    def Chars(self) -> str:
        ...
    @Chars.setter
    def Chars(self, val: str):
        ...

    @property
    def RemainingCurrentChunk(self) -> System.Span[str]:
        ...

    # methods
    @typing.overload
    def __init__(self, from_: System.Text.StringBuilder, ):
        ...

    @typing.overload
    def __init__(self, size: int, maxCapacity: int, previousBlock: System.Text.StringBuilder, ):
        ...

    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def __init__(self, capacity: int, ):
        ...

    @typing.overload
    def __init__(self, value: str, ):
        ...

    @typing.overload
    def __init__(self, value: str, capacity: int, ):
        ...

    @typing.overload
    def __init__(self, value: str, startIndex: int, length: int, capacity: int, ):
        ...

    @typing.overload
    def __init__(self, capacity: int, maxCapacity: int, ):
        ...

    @typing.overload
    def __init__(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext, ):
        ...

    @typing.overload
    def Insert(self, index: int, value: float, ) -> System.Text.StringBuilder:
        ...

    @typing.overload
    def Insert(self, index: int, value: System.Decimal, ) -> System.Text.StringBuilder:
        ...

    @typing.overload
    def Insert(self, index: int, value: int, ) -> System.Text.StringBuilder:
        ...

    @typing.overload
    def Insert(self, index: int, value: int, ) -> System.Text.StringBuilder:
        ...

    @typing.overload
    def Insert(self, index: int, value: int, ) -> System.Text.StringBuilder:
        ...

    @typing.overload
    def Insert(self, index: int, value: System.Object, ) -> System.Text.StringBuilder:
        ...

    @typing.overload
    def Insert(self, index: int, value: System.ReadOnlySpan[str], ) -> System.Text.StringBuilder:
        ...

    @typing.overload
    def Insert(self, index: int, value: ptr[str], valueCount: int, ) -> None:
        ...

    @typing.overload
    def Insert(self, index: int, value: str, count: int, ) -> System.Text.StringBuilder:
        ...

    @typing.overload
    def Insert(self, index: int, value: str, ) -> System.Text.StringBuilder:
        ...

    @typing.overload
    def Insert(self, index: int, value: bool, ) -> System.Text.StringBuilder:
        ...

    @typing.overload
    def Insert(self, index: int, value: int, ) -> System.Text.StringBuilder:
        ...

    @typing.overload
    def Insert(self, index: int, value: int, ) -> System.Text.StringBuilder:
        ...

    @typing.overload
    def Insert(self, index: int, value: int, ) -> System.Text.StringBuilder:
        ...

    @typing.overload
    def Insert(self, index: int, value: str, ) -> System.Text.StringBuilder:
        ...

    @typing.overload
    def Insert(self, index: int, value: System.Array[str], ) -> System.Text.StringBuilder:
        ...

    @typing.overload
    def Insert(self, index: int, value: System.Array[str], startIndex: int, charCount: int, ) -> System.Text.StringBuilder:
        ...

    @typing.overload
    def Insert(self, index: int, value: int, ) -> System.Text.StringBuilder:
        ...

    @typing.overload
    def Insert(self, index: int, value: int, ) -> System.Text.StringBuilder:
        ...

    @typing.overload
    def Insert(self, index: int, value: float, ) -> System.Text.StringBuilder:
        ...

    @typing.overload
    def AppendFormat(self, format: str, arg0: System.Object, ) -> System.Text.StringBuilder:
        ...

    @typing.overload
    def AppendFormat(self, format: str, arg0: System.Object, arg1: System.Object, ) -> System.Text.StringBuilder:
        ...

    @typing.overload
    def AppendFormat(self, format: str, arg0: System.Object, arg1: System.Object, arg2: System.Object, ) -> System.Text.StringBuilder:
        ...

    @typing.overload
    def AppendFormat(self, format: str, args: System.Array[System.Object], ) -> System.Text.StringBuilder:
        ...

    @typing.overload
    def AppendFormat(self, provider: System.IFormatProvider, format: str, arg0: System.Object, ) -> System.Text.StringBuilder:
        ...

    @typing.overload
    def AppendFormat(self, provider: System.IFormatProvider, format: str, arg0: System.Object, arg1: System.Object, ) -> System.Text.StringBuilder:
        ...

    @typing.overload
    def AppendFormat(self, provider: System.IFormatProvider, format: str, arg0: System.Object, arg1: System.Object, arg2: System.Object, ) -> System.Text.StringBuilder:
        ...

    @typing.overload
    def AppendFormat(self, provider: System.IFormatProvider, format: str, args: System.Array[System.Object], ) -> System.Text.StringBuilder:
        ...

    @staticmethod
    def FormatError() -> None:
        ...

    def AppendFormatHelper(self, provider: System.IFormatProvider, format: str, args: System.ParamsArray, ) -> System.Text.StringBuilder:
        ...

    @typing.overload
    def Replace(self, oldValue: str, newValue: str, ) -> System.Text.StringBuilder:
        ...

    @typing.overload
    def Replace(self, oldValue: str, newValue: str, startIndex: int, count: int, ) -> System.Text.StringBuilder:
        ...

    @typing.overload
    def Replace(self, oldChar: str, newChar: str, ) -> System.Text.StringBuilder:
        ...

    @typing.overload
    def Replace(self, oldChar: str, newChar: str, startIndex: int, count: int, ) -> System.Text.StringBuilder:
        ...

    @typing.overload
    def Equals(self, sb: System.Text.StringBuilder, ) -> bool:
        ...

    @typing.overload
    def Equals(self, span: System.ReadOnlySpan[str], ) -> bool:
        ...

    @typing.overload
    def Append(self, value: ptr[str], valueCount: int, ) -> System.Text.StringBuilder:
        ...

    @typing.overload
    def Append(self, value: str, repeatCount: int, ) -> System.Text.StringBuilder:
        ...

    @typing.overload
    def Append(self, value: System.Array[str], startIndex: int, charCount: int, ) -> System.Text.StringBuilder:
        ...

    @typing.overload
    def Append(self, value: str, ) -> System.Text.StringBuilder:
        ...

    @typing.overload
    def Append(self, value: str, startIndex: int, count: int, ) -> System.Text.StringBuilder:
        ...

    @typing.overload
    def Append(self, value: System.Text.StringBuilder, ) -> System.Text.StringBuilder:
        ...

    @typing.overload
    def Append(self, value: System.Text.StringBuilder, startIndex: int, count: int, ) -> System.Text.StringBuilder:
        ...

    @typing.overload
    def Append(self, value: bool, ) -> System.Text.StringBuilder:
        ...

    @typing.overload
    def Append(self, value: str, ) -> System.Text.StringBuilder:
        ...

    @typing.overload
    def Append(self, value: int, ) -> System.Text.StringBuilder:
        ...

    @typing.overload
    def Append(self, value: int, ) -> System.Text.StringBuilder:
        ...

    @typing.overload
    def Append(self, value: int, ) -> System.Text.StringBuilder:
        ...

    @typing.overload
    def Append(self, value: int, ) -> System.Text.StringBuilder:
        ...

    @typing.overload
    def Append(self, value: int, ) -> System.Text.StringBuilder:
        ...

    @typing.overload
    def Append(self, value: float, ) -> System.Text.StringBuilder:
        ...

    @typing.overload
    def Append(self, value: float, ) -> System.Text.StringBuilder:
        ...

    @typing.overload
    def Append(self, value: System.Decimal, ) -> System.Text.StringBuilder:
        ...

    @typing.overload
    def Append(self, value: int, ) -> System.Text.StringBuilder:
        ...

    @typing.overload
    def Append(self, value: int, ) -> System.Text.StringBuilder:
        ...

    @typing.overload
    def Append(self, value: int, ) -> System.Text.StringBuilder:
        ...

    @typing.overload
    def Append(self, value: System.Object, ) -> System.Text.StringBuilder:
        ...

    @typing.overload
    def Append(self, value: System.Array[str], ) -> System.Text.StringBuilder:
        ...

    @typing.overload
    def Append(self, value: System.ReadOnlySpan[str], ) -> System.Text.StringBuilder:
        ...

    @typing.overload
    def Append(self, value: System.ReadOnlyMemory[str], ) -> System.Text.StringBuilder:
        ...

    @typing.overload
    def Append(self, handler: ref[System.Text.StringBuilder.AppendInterpolatedStringHandler], ) -> System.Text.StringBuilder:
        ...

    @typing.overload
    def Append(self, provider: System.IFormatProvider, handler: ref[System.Text.StringBuilder.AppendInterpolatedStringHandler], ) -> System.Text.StringBuilder:
        ...

    def ReplaceAllInChunk(self, replacements: System.Array[int], replacementsCount: int, sourceChunk: System.Text.StringBuilder, removeCount: int, value: str, ) -> None:
        ...

    def StartsWith(self, chunk: System.Text.StringBuilder, indexInChunk: int, count: int, value: str, ) -> bool:
        ...

    def ReplaceInPlaceAtChunk(self, chunk: ref[System.Text.StringBuilder], indexInChunk: ref[int], value: ptr[str], count: int, ) -> None:
        ...

    def FindChunkForIndex(self, index: int, ) -> System.Text.StringBuilder:
        ...

    def Next(self, chunk: System.Text.StringBuilder, ) -> System.Text.StringBuilder:
        ...

    def ExpandByABlock(self, minBlockCharCount: int, ) -> None:
        ...

    def MakeRoom(self, index: int, count: int, chunk: ref[System.Text.StringBuilder], indexInChunk: ref[int], doNotMoveFollowingChars: bool, ) -> None:
        ...

    @typing.overload
    def Remove(self, startIndex: int, count: int, chunk: ref[System.Text.StringBuilder], indexInChunk: ref[int], ) -> None:
        ...

    @typing.overload
    def Remove(self, startIndex: int, length: int, ) -> System.Text.StringBuilder:
        ...

    def GetReplaceBufferCapacity(self, requiredCapacity: int, ) -> int:
        ...

    def ReplaceBufferInternal(self, newBuffer: ptr[str], newLength: int, ) -> None:
        ...

    def ReplaceBufferUtf8Internal(self, source: System.ReadOnlySpan[int], ) -> None:
        ...

    def ReplaceBufferAnsiInternal(self, newBuffer: ptr[int], newLength: int, ) -> None:
        ...

    def InternalCopy(self, dest: System.IntPtr, charLen: int, ) -> None:
        ...

    def GetObjectData(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext, ) -> None:
        ...

    def EnsureCapacity(self, capacity: int, ) -> int:
        ...

    @typing.overload
    def ToString(self, ) -> str:
        ...

    @typing.overload
    def ToString(self, startIndex: int, length: int, ) -> str:
        ...

    def Clear(self, ) -> System.Text.StringBuilder:
        ...

    def GetChunks(self, ) -> System.Text.StringBuilder.ChunkEnumerator:
        ...

    def AppendHelper(self, value: str, ) -> None:
        ...

    def AppendCore(self, value: System.Text.StringBuilder, startIndex: int, count: int, ) -> System.Text.StringBuilder:
        ...

    @typing.overload
    def AppendLine(self, ) -> System.Text.StringBuilder:
        ...

    @typing.overload
    def AppendLine(self, value: str, ) -> System.Text.StringBuilder:
        ...

    @typing.overload
    def AppendLine(self, handler: ref[System.Text.StringBuilder.AppendInterpolatedStringHandler], ) -> System.Text.StringBuilder:
        ...

    @typing.overload
    def AppendLine(self, provider: System.IFormatProvider, handler: ref[System.Text.StringBuilder.AppendInterpolatedStringHandler], ) -> System.Text.StringBuilder:
        ...

    @typing.overload
    def CopyTo(self, sourceIndex: int, destination: System.Array[str], destinationIndex: int, count: int, ) -> None:
        ...

    @typing.overload
    def CopyTo(self, sourceIndex: int, destination: System.Span[str], count: int, ) -> None:
        ...

    @typing.overload
    def AppendSpanFormattable(self, value: T, ) -> System.Text.StringBuilder:
        ...

    @typing.overload
    def AppendSpanFormattable(self, value: T, format: str, provider: System.IFormatProvider, ) -> System.Text.StringBuilder:
        ...

    @typing.overload
    def AppendJoin(self, separator: str, values: System.Array[System.Object], ) -> System.Text.StringBuilder:
        ...

    @typing.overload
    def AppendJoin(self, separator: str, values: System.Collections.Generic.IEnumerable[T], ) -> System.Text.StringBuilder:
        ...

    @typing.overload
    def AppendJoin(self, separator: str, values: System.Array[str], ) -> System.Text.StringBuilder:
        ...

    @typing.overload
    def AppendJoin(self, separator: str, values: System.Array[System.Object], ) -> System.Text.StringBuilder:
        ...

    @typing.overload
    def AppendJoin(self, separator: str, values: System.Collections.Generic.IEnumerable[T], ) -> System.Text.StringBuilder:
        ...

    @typing.overload
    def AppendJoin(self, separator: str, values: System.Array[str], ) -> System.Text.StringBuilder:
        ...

    @typing.overload
    def AppendJoinCore(self, separator: ptr[str], separatorLength: int, values: System.Collections.Generic.IEnumerable[T], ) -> System.Text.StringBuilder:
        ...

    @typing.overload
    def AppendJoinCore(self, separator: ptr[str], separatorLength: int, values: System.Array[T], ) -> System.Text.StringBuilder:
        ...

class DecoderFallback(System.Object, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def ReplacementFallback(self) -> System.Text.DecoderFallback:
        ...

    @property
    def ExceptionFallback(self) -> System.Text.DecoderFallback:
        ...

    @property
    @abc.abstractmethod
    def MaxCharCount(self) -> int:
        ...

    # methods
    def __init__(self, ):
        ...

    @abc.abstractmethod
    def CreateFallbackBuffer(self, ) -> System.Text.DecoderFallbackBuffer:
        ...

class Encoding(System.ICloneable, System.Object, abc.ABC):
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
    def Default(self) -> System.Text.Encoding:
        ...

    @property
    def Preamble(self) -> System.ReadOnlySpan[int]:
        ...

    @property
    def BodyName(self) -> str:
        ...

    @property
    def EncodingName(self) -> str:
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
    def ASCII(self) -> System.Text.Encoding:
        ...

    @property
    def Latin1(self) -> System.Text.Encoding:
        ...

    @property
    def CodePage(self) -> int:
        ...

    @property
    def IsUTF8CodePage(self) -> bool:
        ...

    @property
    def Unicode(self) -> System.Text.Encoding:
        ...

    @property
    def BigEndianUnicode(self) -> System.Text.Encoding:
        ...

    @property
    def UTF7(self) -> System.Text.Encoding:
        ...

    @property
    def UTF8(self) -> System.Text.Encoding:
        ...

    @property
    def UTF32(self) -> System.Text.Encoding:
        ...

    @property
    def BigEndianUTF32(self) -> System.Text.Encoding:
        ...

    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def __init__(self, codePage: int, ):
        ...

    @typing.overload
    def __init__(self, codePage: int, encoderFallback: System.Text.EncoderFallback, decoderFallback: System.Text.DecoderFallback, ):
        ...

    @typing.overload
    def GetCharsWithFallback(self, pOriginalBytes: ptr[int], originalByteCount: int, pOriginalChars: ptr[str], originalCharCount: int, bytesConsumedSoFar: int, charsWrittenSoFar: int, ) -> int:
        ...

    @typing.overload
    def GetCharsWithFallback(self, pOriginalBytes: ptr[int], originalByteCount: int, pOriginalChars: ptr[str], originalCharCount: int, bytesConsumedSoFar: int, charsWrittenSoFar: int, decoder: System.Text.DecoderNLS, ) -> int:
        ...

    @typing.overload
    def GetCharsWithFallback(self, bytes: System.ReadOnlySpan[int], originalBytesLength: int, chars: System.Span[str], originalCharsLength: int, decoder: System.Text.DecoderNLS, ) -> int:
        ...

    def SetDefaultFallbacks(self, ) -> None:
        ...

    @staticmethod
    @typing.overload
    def Convert(srcEncoding: System.Text.Encoding, dstEncoding: System.Text.Encoding, bytes: System.Array[int], ) -> System.Array[int]:
        ...

    @staticmethod
    @typing.overload
    def Convert(srcEncoding: System.Text.Encoding, dstEncoding: System.Text.Encoding, bytes: System.Array[int], index: int, count: int, ) -> System.Array[int]:
        ...

    @staticmethod
    def RegisterProvider(provider: System.Text.EncodingProvider, ) -> None:
        ...

    @staticmethod
    @typing.overload
    def GetEncoding(codepage: int, ) -> System.Text.Encoding:
        ...

    @staticmethod
    @typing.overload
    def GetEncoding(codepage: int, encoderFallback: System.Text.EncoderFallback, decoderFallback: System.Text.DecoderFallback, ) -> System.Text.Encoding:
        ...

    @staticmethod
    @typing.overload
    def GetEncoding(name: str, ) -> System.Text.Encoding:
        ...

    @staticmethod
    @typing.overload
    def GetEncoding(name: str, encoderFallback: System.Text.EncoderFallback, decoderFallback: System.Text.DecoderFallback, ) -> System.Text.Encoding:
        ...

    @staticmethod
    def FilterDisallowedEncodings(encoding: System.Text.Encoding, ) -> System.Text.Encoding:
        ...

    @staticmethod
    def GetEncodings() -> System.Array[System.Text.EncodingInfo]:
        ...

    def GetPreamble(self, ) -> System.Array[int]:
        ...

    def GetDataItem(self, ) -> None:
        ...

    def Clone(self, ) -> System.Object:
        ...

    @typing.overload
    def GetByteCount(self, chars: System.Array[str], ) -> int:
        ...

    @typing.overload
    def GetByteCount(self, s: str, ) -> int:
        ...

    @abc.abstractmethod
    @typing.overload
    def GetByteCount(self, chars: System.Array[str], index: int, count: int, ) -> int:
        ...

    @typing.overload
    def GetByteCount(self, s: str, index: int, count: int, ) -> int:
        ...

    @typing.overload
    def GetByteCount(self, chars: ptr[str], count: int, ) -> int:
        ...

    @typing.overload
    def GetByteCount(self, chars: System.ReadOnlySpan[str], ) -> int:
        ...

    @typing.overload
    def GetByteCount(self, pChars: ptr[str], charCount: int, encoder: System.Text.EncoderNLS, ) -> int:
        ...

    @typing.overload
    def GetBytes(self, chars: System.Array[str], ) -> System.Array[int]:
        ...

    @typing.overload
    def GetBytes(self, chars: System.Array[str], index: int, count: int, ) -> System.Array[int]:
        ...

    @abc.abstractmethod
    @typing.overload
    def GetBytes(self, chars: System.Array[str], charIndex: int, charCount: int, bytes: System.Array[int], byteIndex: int, ) -> int:
        ...

    @typing.overload
    def GetBytes(self, s: str, ) -> System.Array[int]:
        ...

    @typing.overload
    def GetBytes(self, s: str, index: int, count: int, ) -> System.Array[int]:
        ...

    @typing.overload
    def GetBytes(self, s: str, charIndex: int, charCount: int, bytes: System.Array[int], byteIndex: int, ) -> int:
        ...

    @typing.overload
    def GetBytes(self, chars: ptr[str], charCount: int, bytes: ptr[int], byteCount: int, ) -> int:
        ...

    @typing.overload
    def GetBytes(self, chars: System.ReadOnlySpan[str], bytes: System.Span[int], ) -> int:
        ...

    @typing.overload
    def GetBytes(self, pChars: ptr[str], charCount: int, pBytes: ptr[int], byteCount: int, encoder: System.Text.EncoderNLS, ) -> int:
        ...

    @typing.overload
    def GetCharCount(self, bytes: System.Array[int], ) -> int:
        ...

    @abc.abstractmethod
    @typing.overload
    def GetCharCount(self, bytes: System.Array[int], index: int, count: int, ) -> int:
        ...

    @typing.overload
    def GetCharCount(self, bytes: ptr[int], count: int, ) -> int:
        ...

    @typing.overload
    def GetCharCount(self, bytes: System.ReadOnlySpan[int], ) -> int:
        ...

    @typing.overload
    def GetCharCount(self, pBytes: ptr[int], byteCount: int, decoder: System.Text.DecoderNLS, ) -> int:
        ...

    @typing.overload
    def GetChars(self, bytes: System.Array[int], ) -> System.Array[str]:
        ...

    @typing.overload
    def GetChars(self, bytes: System.Array[int], index: int, count: int, ) -> System.Array[str]:
        ...

    @abc.abstractmethod
    @typing.overload
    def GetChars(self, bytes: System.Array[int], byteIndex: int, byteCount: int, chars: System.Array[str], charIndex: int, ) -> int:
        ...

    @typing.overload
    def GetChars(self, bytes: ptr[int], byteCount: int, chars: ptr[str], charCount: int, ) -> int:
        ...

    @typing.overload
    def GetChars(self, bytes: System.ReadOnlySpan[int], chars: System.Span[str], ) -> int:
        ...

    @typing.overload
    def GetChars(self, pBytes: ptr[int], byteCount: int, pChars: ptr[str], charCount: int, decoder: System.Text.DecoderNLS, ) -> int:
        ...

    @typing.overload
    def GetString(self, bytes: ptr[int], byteCount: int, ) -> str:
        ...

    @typing.overload
    def GetString(self, bytes: System.ReadOnlySpan[int], ) -> str:
        ...

    @typing.overload
    def GetString(self, bytes: System.Array[int], ) -> str:
        ...

    @typing.overload
    def GetString(self, bytes: System.Array[int], index: int, count: int, ) -> str:
        ...

    @typing.overload
    def IsAlwaysNormalized(self, ) -> bool:
        ...

    @typing.overload
    def IsAlwaysNormalized(self, form: int, ) -> bool:
        ...

    def GetDecoder(self, ) -> System.Text.Decoder:
        ...

    def GetEncoder(self, ) -> System.Text.Encoder:
        ...

    @abc.abstractmethod
    def GetMaxByteCount(self, charCount: int, ) -> int:
        ...

    @abc.abstractmethod
    def GetMaxCharCount(self, byteCount: int, ) -> int:
        ...

    def Equals(self, value: System.Object, ) -> bool:
        ...

    def GetHashCode(self, ) -> int:
        ...

    @staticmethod
    def CreateTranscodingStream(innerStream: System.IO.Stream, innerStreamEncoding: System.Text.Encoding, outerStreamEncoding: System.Text.Encoding, leaveOpen: bool = ..., ) -> System.IO.Stream:
        ...

    @typing.overload
    def ThrowBytesOverflow(self, ) -> None:
        ...

    @typing.overload
    def ThrowBytesOverflow(self, encoder: System.Text.EncoderNLS, nothingEncoded: bool, ) -> None:
        ...

    @staticmethod
    def ThrowConversionOverflow() -> None:
        ...

    @typing.overload
    def ThrowCharsOverflow(self, ) -> None:
        ...

    @typing.overload
    def ThrowCharsOverflow(self, decoder: System.Text.DecoderNLS, nothingDecoded: bool, ) -> None:
        ...

    def DecodeFirstRune(self, bytes: System.ReadOnlySpan[int], value: ref[System.Text.Rune], bytesConsumed: ref[int], ) -> int:
        ...

    def EncodeRune(self, value: System.Text.Rune, bytes: System.Span[int], bytesWritten: ref[int], ) -> int:
        ...

    def TryGetByteCount(self, value: System.Text.Rune, byteCount: ref[int], ) -> bool:
        ...

    def GetByteCountFast(self, pChars: ptr[str], charsLength: int, fallback: System.Text.EncoderFallback, charsConsumed: ref[int], ) -> int:
        ...

    @typing.overload
    def GetByteCountWithFallback(self, pCharsOriginal: ptr[str], originalCharCount: int, charsConsumedSoFar: int, ) -> int:
        ...

    @typing.overload
    def GetByteCountWithFallback(self, pOriginalChars: ptr[str], originalCharCount: int, charsConsumedSoFar: int, encoder: System.Text.EncoderNLS, ) -> int:
        ...

    @typing.overload
    def GetByteCountWithFallback(self, chars: System.ReadOnlySpan[str], originalCharsLength: int, encoder: System.Text.EncoderNLS, ) -> int:
        ...

    def GetBytesFast(self, pChars: ptr[str], charsLength: int, pBytes: ptr[int], bytesLength: int, charsConsumed: ref[int], ) -> int:
        ...

    @typing.overload
    def GetBytesWithFallback(self, pOriginalChars: ptr[str], originalCharCount: int, pOriginalBytes: ptr[int], originalByteCount: int, charsConsumedSoFar: int, bytesWrittenSoFar: int, ) -> int:
        ...

    @typing.overload
    def GetBytesWithFallback(self, pOriginalChars: ptr[str], originalCharCount: int, pOriginalBytes: ptr[int], originalByteCount: int, charsConsumedSoFar: int, bytesWrittenSoFar: int, encoder: System.Text.EncoderNLS, ) -> int:
        ...

    @typing.overload
    def GetBytesWithFallback(self, chars: System.ReadOnlySpan[str], originalCharsLength: int, bytes: System.Span[int], originalBytesLength: int, encoder: System.Text.EncoderNLS, ) -> int:
        ...

    def GetCharCountFast(self, pBytes: ptr[int], bytesLength: int, fallback: System.Text.DecoderFallback, bytesConsumed: ref[int], ) -> int:
        ...

    @typing.overload
    def GetCharCountWithFallback(self, pBytesOriginal: ptr[int], originalByteCount: int, bytesConsumedSoFar: int, ) -> int:
        ...

    @typing.overload
    def GetCharCountWithFallback(self, pOriginalBytes: ptr[int], originalByteCount: int, bytesConsumedSoFar: int, decoder: System.Text.DecoderNLS, ) -> int:
        ...

    @typing.overload
    def GetCharCountWithFallback(self, bytes: System.ReadOnlySpan[int], originalBytesLength: int, decoder: System.Text.DecoderNLS, ) -> int:
        ...

    def GetCharsFast(self, pBytes: ptr[int], bytesLength: int, pChars: ptr[str], charsLength: int, bytesConsumed: ref[int], ) -> int:
        ...

class NormalizationForm(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    FormC: int = ...
    FormD: int = ...
    FormKC: int = ...
    FormKD: int = ...

class EncodingInfo(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def CodePage(self) -> int:
        ...

    @property
    def Name(self) -> str:
        ...

    @property
    def DisplayName(self) -> str:
        ...

    @property
    def Provider(self) -> System.Text.EncodingProvider:
        ...

    # methods
    @typing.overload
    def __init__(self, provider: System.Text.EncodingProvider, codePage: int, name: str, displayName: str, ):
        ...

    @typing.overload
    def __init__(self, codePage: int, name: str, displayName: str, ):
        ...

    def GetEncoding(self, ) -> System.Text.Encoding:
        ...

    def Equals(self, value: System.Object, ) -> bool:
        ...

    def GetHashCode(self, ) -> int:
        ...

class DecoderFallbackException(System.Runtime.Serialization.ISerializable, System.ArgumentException):
    @typing.overload
    def __init__(self, **kwargs):
        self._message: str
        ...

    # static fields

    # properties
    @property
    def BytesUnknown(self) -> System.Array[int]:
        ...

    @property
    def Index(self) -> int:
        ...

    @property
    def Message(self) -> str:
        ...

    @property
    def ParamName(self) -> str:
        ...

    @property
    def TargetSite(self) -> System.Reflection.MethodBase:
        ...

    @property
    def Data(self) -> System.Collections.IDictionary:
        ...

    @property
    def InnerException(self) -> System.Exception:
        ...

    @property
    def HelpLink(self) -> str:
        ...
    @HelpLink.setter
    def HelpLink(self, val: str):
        ...

    @property
    def Source(self) -> str:
        ...
    @Source.setter
    def Source(self, val: str):
        ...

    @property
    def HResult(self) -> int:
        ...
    @HResult.setter
    def HResult(self, val: int):
        ...

    @property
    def StackTrace(self) -> str:
        ...

    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def __init__(self, message: str, ):
        ...

    @typing.overload
    def __init__(self, message: str, innerException: System.Exception, ):
        ...

    @typing.overload
    def __init__(self, message: str, bytesUnknown: System.Array[int], index: int, ):
        ...

    @typing.overload
    def __init__(self, serializationInfo: System.Runtime.Serialization.SerializationInfo, streamingContext: System.Runtime.Serialization.StreamingContext, ):
        ...

class Encoder(System.Object, abc.ABC):
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
    def __init__(self, ):
        ...

    @abc.abstractmethod
    @typing.overload
    def GetByteCount(self, chars: System.Array[str], index: int, count: int, flush: bool, ) -> int:
        ...

    @typing.overload
    def GetByteCount(self, chars: ptr[str], count: int, flush: bool, ) -> int:
        ...

    @typing.overload
    def GetByteCount(self, chars: System.ReadOnlySpan[str], flush: bool, ) -> int:
        ...

    @abc.abstractmethod
    @typing.overload
    def GetBytes(self, chars: System.Array[str], charIndex: int, charCount: int, bytes: System.Array[int], byteIndex: int, flush: bool, ) -> int:
        ...

    @typing.overload
    def GetBytes(self, chars: ptr[str], charCount: int, bytes: ptr[int], byteCount: int, flush: bool, ) -> int:
        ...

    @typing.overload
    def GetBytes(self, chars: System.ReadOnlySpan[str], bytes: System.Span[int], flush: bool, ) -> int:
        ...

    def Reset(self, ) -> None:
        ...

    @typing.overload
    def Convert(self, chars: System.Array[str], charIndex: int, charCount: int, bytes: System.Array[int], byteIndex: int, byteCount: int, flush: bool, charsUsed: ref[int], bytesUsed: ref[int], completed: ref[bool], ) -> None:
        ...

    @typing.overload
    def Convert(self, chars: ptr[str], charCount: int, bytes: ptr[int], byteCount: int, flush: bool, charsUsed: ref[int], bytesUsed: ref[int], completed: ref[bool], ) -> None:
        ...

    @typing.overload
    def Convert(self, chars: System.ReadOnlySpan[str], bytes: System.Span[int], flush: bool, charsUsed: ref[int], bytesUsed: ref[int], completed: ref[bool], ) -> None:
        ...

class Rune(System.IComparable, System.IComparable[System.Text.Rune], System.IEquatable[System.Text.Rune], System.ISpanFormattable, System.IFormattable, System.ValueType):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def AsciiCharInfo(self) -> System.ReadOnlySpan[int]:
        ...

    @property
    def DebuggerDisplay(self) -> str:
        ...

    @property
    def IsAscii(self) -> bool:
        ...

    @property
    def IsBmp(self) -> bool:
        ...

    @property
    def Plane(self) -> int:
        ...

    @property
    def ReplacementChar(self) -> System.Text.Rune:
        ...

    @property
    def Utf16SequenceLength(self) -> int:
        ...

    @property
    def Utf8SequenceLength(self) -> int:
        ...

    @property
    def Value(self) -> int:
        ...

    # methods
    @typing.overload
    def __init__(self, ch: str, ):
        ...

    @typing.overload
    def __init__(self, highSurrogate: str, lowSurrogate: str, ):
        ...

    @typing.overload
    def __init__(self, value: int, ):
        ...

    @typing.overload
    def __init__(self, value: int, ):
        ...

    @typing.overload
    def __init__(self, scalarValue: int, unused: bool, ):
        ...

    def CompareTo(self, obj: System.Object, ) -> int:
        ...

    @staticmethod
    def ChangeCaseCultureAware(rune: System.Text.Rune, textInfo: System.Globalization.TextInfo, toUpper: bool, ) -> System.Text.Rune:
        ...

    def CompareTo(self, other: System.Text.Rune, ) -> int:
        ...

    @staticmethod
    def DecodeFromUtf16(source: System.ReadOnlySpan[str], result: ref[System.Text.Rune], charsConsumed: ref[int], ) -> int:
        ...

    @staticmethod
    def DecodeFromUtf8(source: System.ReadOnlySpan[int], result: ref[System.Text.Rune], bytesConsumed: ref[int], ) -> int:
        ...

    @staticmethod
    def DecodeLastFromUtf16(source: System.ReadOnlySpan[str], result: ref[System.Text.Rune], charsConsumed: ref[int], ) -> int:
        ...

    @staticmethod
    def DecodeLastFromUtf8(source: System.ReadOnlySpan[int], value: ref[System.Text.Rune], bytesConsumed: ref[int], ) -> int:
        ...

    def EncodeToUtf16(self, destination: System.Span[str], ) -> int:
        ...

    def EncodeToUtf8(self, destination: System.Span[int], ) -> int:
        ...

    @typing.overload
    def Equals(self, obj: System.Object, ) -> bool:
        ...

    @typing.overload
    def Equals(self, other: System.Text.Rune, ) -> bool:
        ...

    def GetHashCode(self, ) -> int:
        ...

    @staticmethod
    def GetRuneAt(input: str, index: int, ) -> System.Text.Rune:
        ...

    @staticmethod
    @typing.overload
    def IsValid(value: int, ) -> bool:
        ...

    @staticmethod
    @typing.overload
    def IsValid(value: int, ) -> bool:
        ...

    @staticmethod
    def ReadFirstRuneFromUtf16Buffer(input: System.ReadOnlySpan[str], ) -> int:
        ...

    @staticmethod
    def ReadRuneFromString(input: str, index: int, ) -> int:
        ...

    def ToString(self, ) -> str:
        ...

    def TryFormat(self, destination: System.Span[str], charsWritten: ref[int], format: System.ReadOnlySpan[str], provider: System.IFormatProvider, ) -> bool:
        ...

    def ToString(self, format: str, formatProvider: System.IFormatProvider, ) -> str:
        ...

    @staticmethod
    @typing.overload
    def TryCreate(ch: str, result: ref[System.Text.Rune], ) -> bool:
        ...

    @staticmethod
    @typing.overload
    def TryCreate(highSurrogate: str, lowSurrogate: str, result: ref[System.Text.Rune], ) -> bool:
        ...

    @staticmethod
    @typing.overload
    def TryCreate(value: int, result: ref[System.Text.Rune], ) -> bool:
        ...

    @staticmethod
    @typing.overload
    def TryCreate(value: int, result: ref[System.Text.Rune], ) -> bool:
        ...

    @typing.overload
    def TryEncodeToUtf16(self, destination: System.Span[str], charsWritten: ref[int], ) -> bool:
        ...

    @staticmethod
    @typing.overload
    def TryEncodeToUtf16(value: System.Text.Rune, destination: System.Span[str], charsWritten: ref[int], ) -> bool:
        ...

    @typing.overload
    def TryEncodeToUtf8(self, destination: System.Span[int], bytesWritten: ref[int], ) -> bool:
        ...

    @staticmethod
    @typing.overload
    def TryEncodeToUtf8(value: System.Text.Rune, destination: System.Span[int], bytesWritten: ref[int], ) -> bool:
        ...

    @staticmethod
    def TryGetRuneAt(input: str, index: int, value: ref[System.Text.Rune], ) -> bool:
        ...

    @staticmethod
    def UnsafeCreate(scalarValue: int, ) -> System.Text.Rune:
        ...

    @staticmethod
    def GetNumericValue(value: System.Text.Rune, ) -> float:
        ...

    @staticmethod
    def GetUnicodeCategory(value: System.Text.Rune, ) -> int:
        ...

    @staticmethod
    def GetUnicodeCategoryNonAscii(value: System.Text.Rune, ) -> int:
        ...

    @staticmethod
    def IsCategoryLetter(category: int, ) -> bool:
        ...

    @staticmethod
    def IsCategoryLetterOrDecimalDigit(category: int, ) -> bool:
        ...

    @staticmethod
    def IsCategoryNumber(category: int, ) -> bool:
        ...

    @staticmethod
    def IsCategoryPunctuation(category: int, ) -> bool:
        ...

    @staticmethod
    def IsCategorySeparator(category: int, ) -> bool:
        ...

    @staticmethod
    def IsCategorySymbol(category: int, ) -> bool:
        ...

    @staticmethod
    def IsControl(value: System.Text.Rune, ) -> bool:
        ...

    @staticmethod
    def IsDigit(value: System.Text.Rune, ) -> bool:
        ...

    @staticmethod
    def IsLetter(value: System.Text.Rune, ) -> bool:
        ...

    @staticmethod
    def IsLetterOrDigit(value: System.Text.Rune, ) -> bool:
        ...

    @staticmethod
    def IsLower(value: System.Text.Rune, ) -> bool:
        ...

    @staticmethod
    def IsNumber(value: System.Text.Rune, ) -> bool:
        ...

    @staticmethod
    def IsPunctuation(value: System.Text.Rune, ) -> bool:
        ...

    @staticmethod
    def IsSeparator(value: System.Text.Rune, ) -> bool:
        ...

    @staticmethod
    def IsSymbol(value: System.Text.Rune, ) -> bool:
        ...

    @staticmethod
    def IsUpper(value: System.Text.Rune, ) -> bool:
        ...

    @staticmethod
    def IsWhiteSpace(value: System.Text.Rune, ) -> bool:
        ...

    @staticmethod
    def ToLower(value: System.Text.Rune, culture: System.Globalization.CultureInfo, ) -> System.Text.Rune:
        ...

    @staticmethod
    def ToLowerInvariant(value: System.Text.Rune, ) -> System.Text.Rune:
        ...

    @staticmethod
    def ToUpper(value: System.Text.Rune, culture: System.Globalization.CultureInfo, ) -> System.Text.Rune:
        ...

    @staticmethod
    def ToUpperInvariant(value: System.Text.Rune, ) -> System.Text.Rune:
        ...

class EncodingProvider(System.Object, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    def __init__(self, ):
        ...

    @abc.abstractmethod
    @typing.overload
    def GetEncoding(self, name: str, ) -> System.Text.Encoding:
        ...

    @abc.abstractmethod
    @typing.overload
    def GetEncoding(self, codepage: int, ) -> System.Text.Encoding:
        ...

    @typing.overload
    def GetEncoding(self, name: str, encoderFallback: System.Text.EncoderFallback, decoderFallback: System.Text.DecoderFallback, ) -> System.Text.Encoding:
        ...

    @typing.overload
    def GetEncoding(self, codepage: int, encoderFallback: System.Text.EncoderFallback, decoderFallback: System.Text.DecoderFallback, ) -> System.Text.Encoding:
        ...

    def GetEncodings(self, ) -> System.Collections.Generic.IEnumerable[System.Text.EncodingInfo]:
        ...

    @staticmethod
    def AddProvider(provider: System.Text.EncodingProvider, ) -> None:
        ...

    @staticmethod
    @typing.overload
    def GetEncodingFromProvider(codepage: int, ) -> System.Text.Encoding:
        ...

    @staticmethod
    @typing.overload
    def GetEncodingFromProvider(encodingName: str, ) -> System.Text.Encoding:
        ...

    @staticmethod
    @typing.overload
    def GetEncodingFromProvider(codepage: int, enc: System.Text.EncoderFallback, dec: System.Text.DecoderFallback, ) -> System.Text.Encoding:
        ...

    @staticmethod
    @typing.overload
    def GetEncodingFromProvider(encodingName: str, enc: System.Text.EncoderFallback, dec: System.Text.DecoderFallback, ) -> System.Text.Encoding:
        ...

    @staticmethod
    def GetEncodingListFromProviders() -> System.Collections.Generic.Dictionary[int, System.Text.EncodingInfo]:
        ...

class DecoderFallbackBuffer(System.Object, abc.ABC):
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
    @abc.abstractmethod
    def Remaining(self) -> int:
        ...

    # methods
    def __init__(self, ):
        ...

    def Reset(self, ) -> None:
        ...

    @abc.abstractmethod
    def Fallback(self, bytesUnknown: System.Array[int], index: int, ) -> bool:
        ...

    @abc.abstractmethod
    def GetNextChar(self, ) -> str:
        ...

    @abc.abstractmethod
    def MovePrevious(self, ) -> bool:
        ...

    def InternalReset(self, ) -> None:
        ...

    def InternalInitialize(self, byteStart: ptr[int], charEnd: ptr[str], ) -> None:
        ...

    @staticmethod
    def CreateAndInitialize(encoding: System.Text.Encoding, decoder: System.Text.DecoderNLS, originalByteCount: int, ) -> System.Text.DecoderFallbackBuffer:
        ...

    @typing.overload
    def InternalFallback(self, bytes: System.Array[int], pBytes: ptr[int], chars: ref[ptr[str]], ) -> bool:
        ...

    @typing.overload
    def InternalFallback(self, bytes: System.Array[int], pBytes: ptr[int], ) -> int:
        ...

    def InternalFallbackGetCharCount(self, remainingBytes: System.ReadOnlySpan[int], fallbackLength: int, ) -> int:
        ...

    def TryInternalFallbackGetChars(self, remainingBytes: System.ReadOnlySpan[int], fallbackLength: int, chars: System.Span[str], charsWritten: ref[int], ) -> bool:
        ...

    def GetNextRune(self, ) -> System.Text.Rune:
        ...

    def DrainRemainingDataForGetCharCount(self, ) -> int:
        ...

    def TryDrainRemainingDataForGetChars(self, chars: System.Span[str], charsWritten: ref[int], ) -> bool:
        ...

    @staticmethod
    def ThrowLastBytesRecursive(bytesUnknown: System.Array[int], ) -> None:
        ...

class Decoder(System.Object, abc.ABC):
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
    def __init__(self, ):
        ...

    def Reset(self, ) -> None:
        ...

    @abc.abstractmethod
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
    def GetCharCount(self, bytes: System.ReadOnlySpan[int], flush: bool, ) -> int:
        ...

    @abc.abstractmethod
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

    @typing.overload
    def Convert(self, bytes: System.Array[int], byteIndex: int, byteCount: int, chars: System.Array[str], charIndex: int, charCount: int, flush: bool, bytesUsed: ref[int], charsUsed: ref[int], completed: ref[bool], ) -> None:
        ...

    @typing.overload
    def Convert(self, bytes: ptr[int], byteCount: int, chars: ptr[str], charCount: int, flush: bool, bytesUsed: ref[int], charsUsed: ref[int], completed: ref[bool], ) -> None:
        ...

    @typing.overload
    def Convert(self, bytes: System.ReadOnlySpan[int], chars: System.Span[str], flush: bool, bytesUsed: ref[int], charsUsed: ref[int], completed: ref[bool], ) -> None:
        ...

