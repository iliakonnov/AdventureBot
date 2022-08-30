from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import System
import System.Text
import System.IO
import System.Collections.Generic
import System.Collections
import System.Buffers
import System.Globalization
import System.Runtime.Serialization
import System.Text.StringBuilder

T = typing.TypeVar('T')

class Encoding(System.ICloneable, System.Object, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def Default(self) -> System.Text.Encoding:
        ...

    @property
    def Preamble(self) -> System.ReadOnlySpan[System.Byte]:
        ...

    @property
    def BodyName(self) -> System.String:
        ...

    @property
    def EncodingName(self) -> System.String:
        ...

    @property
    def HeaderName(self) -> System.String:
        ...

    @property
    def WebName(self) -> System.String:
        ...

    @property
    def WindowsCodePage(self) -> System.Int32:
        ...

    @property
    def IsBrowserDisplay(self) -> System.Boolean:
        ...

    @property
    def IsBrowserSave(self) -> System.Boolean:
        ...

    @property
    def IsMailNewsDisplay(self) -> System.Boolean:
        ...

    @property
    def IsMailNewsSave(self) -> System.Boolean:
        ...

    @property
    def IsSingleByte(self) -> System.Boolean:
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
    def IsReadOnly(self) -> System.Boolean:
        ...

    @property
    def ASCII(self) -> System.Text.Encoding:
        ...

    @property
    def Latin1(self) -> System.Text.Encoding:
        ...

    @property
    def CodePage(self) -> System.Int32:
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

    # methods
    @typing.overload
    @staticmethod
    def Convert(srcEncoding: System.Text.Encoding, dstEncoding: System.Text.Encoding, bytes: list[System.Byte], ) -> list[System.Byte]:
        ...

    @typing.overload
    @staticmethod
    def Convert(srcEncoding: System.Text.Encoding, dstEncoding: System.Text.Encoding, bytes: list[System.Byte], index: System.Int32, count: System.Int32, ) -> list[System.Byte]:
        ...

    @typing.overload
    @staticmethod
    def RegisterProvider(provider: System.Text.EncodingProvider, ) -> None:
        ...

    @typing.overload
    @staticmethod
    def GetEncoding(codepage: System.Int32, ) -> System.Text.Encoding:
        ...

    @typing.overload
    @staticmethod
    def GetEncoding(codepage: System.Int32, encoderFallback: System.Text.EncoderFallback, decoderFallback: System.Text.DecoderFallback, ) -> System.Text.Encoding:
        ...

    @typing.overload
    @staticmethod
    def GetEncoding(name: System.String, ) -> System.Text.Encoding:
        ...

    @typing.overload
    @staticmethod
    def GetEncoding(name: System.String, encoderFallback: System.Text.EncoderFallback, decoderFallback: System.Text.DecoderFallback, ) -> System.Text.Encoding:
        ...

    @typing.overload
    @staticmethod
    def GetEncodings() -> list[System.Text.EncodingInfo]:
        ...

    @typing.overload
    def GetPreamble(self, ) -> list[System.Byte]:
        ...

    @typing.overload
    def Clone(self, ) -> System.Object:
        ...

    @typing.overload
    def GetByteCount(self, chars: list[System.Char], ) -> System.Int32:
        ...

    @typing.overload
    def GetByteCount(self, s: System.String, ) -> System.Int32:
        ...

    @typing.overload
    @abc.abstractmethod
    def GetByteCount(self, chars: list[System.Char], index: System.Int32, count: System.Int32, ) -> System.Int32:
        ...

    @typing.overload
    def GetByteCount(self, s: System.String, index: System.Int32, count: System.Int32, ) -> System.Int32:
        ...

    @typing.overload
    def GetByteCount(self, chars: ptr[System.Char], count: System.Int32, ) -> System.Int32:
        ...

    @typing.overload
    def GetByteCount(self, chars: System.ReadOnlySpan[System.Char], ) -> System.Int32:
        ...

    @typing.overload
    def GetBytes(self, chars: list[System.Char], ) -> list[System.Byte]:
        ...

    @typing.overload
    def GetBytes(self, chars: list[System.Char], index: System.Int32, count: System.Int32, ) -> list[System.Byte]:
        ...

    @typing.overload
    @abc.abstractmethod
    def GetBytes(self, chars: list[System.Char], charIndex: System.Int32, charCount: System.Int32, bytes: list[System.Byte], byteIndex: System.Int32, ) -> System.Int32:
        ...

    @typing.overload
    def GetBytes(self, s: System.String, ) -> list[System.Byte]:
        ...

    @typing.overload
    def GetBytes(self, s: System.String, index: System.Int32, count: System.Int32, ) -> list[System.Byte]:
        ...

    @typing.overload
    def GetBytes(self, s: System.String, charIndex: System.Int32, charCount: System.Int32, bytes: list[System.Byte], byteIndex: System.Int32, ) -> System.Int32:
        ...

    @typing.overload
    def GetBytes(self, chars: ptr[System.Char], charCount: System.Int32, bytes: ptr[System.Byte], byteCount: System.Int32, ) -> System.Int32:
        ...

    @typing.overload
    def GetBytes(self, chars: System.ReadOnlySpan[System.Char], bytes: System.Span[System.Byte], ) -> System.Int32:
        ...

    @typing.overload
    def GetCharCount(self, bytes: list[System.Byte], ) -> System.Int32:
        ...

    @typing.overload
    @abc.abstractmethod
    def GetCharCount(self, bytes: list[System.Byte], index: System.Int32, count: System.Int32, ) -> System.Int32:
        ...

    @typing.overload
    def GetCharCount(self, bytes: ptr[System.Byte], count: System.Int32, ) -> System.Int32:
        ...

    @typing.overload
    def GetCharCount(self, bytes: System.ReadOnlySpan[System.Byte], ) -> System.Int32:
        ...

    @typing.overload
    def GetChars(self, bytes: list[System.Byte], ) -> list[System.Char]:
        ...

    @typing.overload
    def GetChars(self, bytes: list[System.Byte], index: System.Int32, count: System.Int32, ) -> list[System.Char]:
        ...

    @typing.overload
    @abc.abstractmethod
    def GetChars(self, bytes: list[System.Byte], byteIndex: System.Int32, byteCount: System.Int32, chars: list[System.Char], charIndex: System.Int32, ) -> System.Int32:
        ...

    @typing.overload
    def GetChars(self, bytes: ptr[System.Byte], byteCount: System.Int32, chars: ptr[System.Char], charCount: System.Int32, ) -> System.Int32:
        ...

    @typing.overload
    def GetChars(self, bytes: System.ReadOnlySpan[System.Byte], chars: System.Span[System.Char], ) -> System.Int32:
        ...

    @typing.overload
    def GetString(self, bytes: ptr[System.Byte], byteCount: System.Int32, ) -> System.String:
        ...

    @typing.overload
    def GetString(self, bytes: System.ReadOnlySpan[System.Byte], ) -> System.String:
        ...

    @typing.overload
    def IsAlwaysNormalized(self, ) -> System.Boolean:
        ...

    @typing.overload
    def IsAlwaysNormalized(self, form: System.Text.NormalizationForm, ) -> System.Boolean:
        ...

    @typing.overload
    def GetDecoder(self, ) -> System.Text.Decoder:
        ...

    @typing.overload
    def GetEncoder(self, ) -> System.Text.Encoder:
        ...

    @typing.overload
    @abc.abstractmethod
    def GetMaxByteCount(self, charCount: System.Int32, ) -> System.Int32:
        ...

    @typing.overload
    @abc.abstractmethod
    def GetMaxCharCount(self, byteCount: System.Int32, ) -> System.Int32:
        ...

    @typing.overload
    def GetString(self, bytes: list[System.Byte], ) -> System.String:
        ...

    @typing.overload
    def GetString(self, bytes: list[System.Byte], index: System.Int32, count: System.Int32, ) -> System.String:
        ...

    @typing.overload
    def Equals(self, value: System.Object, ) -> System.Boolean:
        ...

    @typing.overload
    def GetHashCode(self, ) -> System.Int32:
        ...

    @typing.overload
    @staticmethod
    def CreateTranscodingStream(innerStream: System.IO.Stream, innerStreamEncoding: System.Text.Encoding, outerStreamEncoding: System.Text.Encoding, leaveOpen: System.Boolean, ) -> System.IO.Stream:
        ...

class StringRuneEnumerator(System.Collections.Generic.IEnumerable[System.Text.Rune], System.Collections.IEnumerable, System.Collections.Generic.IEnumerator[System.Text.Rune], System.IDisposable, System.Collections.IEnumerator, System.ValueType):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def Current(self) -> System.Text.Rune:
        ...

    # methods
    @typing.overload
    def GetEnumerator(self, ) -> System.Text.StringRuneEnumerator:
        ...

    @typing.overload
    def MoveNext(self, ) -> System.Boolean:
        ...

class NormalizationForm(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    FormC: System.Int32 = FormC
    FormD: System.Int32 = FormD
    FormKC: System.Int32 = FormKC
    FormKD: System.Int32 = FormKD

class EncoderFallback(System.Object, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def ReplacementFallback(self) -> System.Text.EncoderFallback:
        ...

    @property
    def ExceptionFallback(self) -> System.Text.EncoderFallback:
        ...

    @abc.abstractmethod
    @property
    def MaxCharCount(self) -> System.Int32:
        ...

    # methods
    @typing.overload
    @abc.abstractmethod
    def CreateFallbackBuffer(self, ) -> System.Text.EncoderFallbackBuffer:
        ...

class DecoderFallback(System.Object, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def ReplacementFallback(self) -> System.Text.DecoderFallback:
        ...

    @property
    def ExceptionFallback(self) -> System.Text.DecoderFallback:
        ...

    @abc.abstractmethod
    @property
    def MaxCharCount(self) -> System.Int32:
        ...

    # methods
    @typing.overload
    @abc.abstractmethod
    def CreateFallbackBuffer(self, ) -> System.Text.DecoderFallbackBuffer:
        ...

class EncodingProvider(System.Object, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    @abc.abstractmethod
    def GetEncoding(self, name: System.String, ) -> System.Text.Encoding:
        ...

    @typing.overload
    @abc.abstractmethod
    def GetEncoding(self, codepage: System.Int32, ) -> System.Text.Encoding:
        ...

    @typing.overload
    def GetEncoding(self, name: System.String, encoderFallback: System.Text.EncoderFallback, decoderFallback: System.Text.DecoderFallback, ) -> System.Text.Encoding:
        ...

    @typing.overload
    def GetEncoding(self, codepage: System.Int32, encoderFallback: System.Text.EncoderFallback, decoderFallback: System.Text.DecoderFallback, ) -> System.Text.Encoding:
        ...

    @typing.overload
    def GetEncodings(self, ) -> System.Collections.Generic.IEnumerable[System.Text.EncodingInfo]:
        ...

class EncodingInfo(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def CodePage(self) -> System.Int32:
        ...

    @property
    def Name(self) -> System.String:
        ...

    @property
    def DisplayName(self) -> System.String:
        ...

    # methods
    @typing.overload
    def __init__(self, provider: System.Text.EncodingProvider, codePage: System.Int32, name: System.String, displayName: System.String, ):
        ...

    @typing.overload
    def GetEncoding(self, ) -> System.Text.Encoding:
        ...

    @typing.overload
    def Equals(self, value: System.Object, ) -> System.Boolean:
        ...

    @typing.overload
    def GetHashCode(self, ) -> System.Int32:
        ...

class Decoder(System.Object, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

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

    # methods
    @typing.overload
    def Reset(self, ) -> None:
        ...

    @typing.overload
    @abc.abstractmethod
    def GetCharCount(self, bytes: list[System.Byte], index: System.Int32, count: System.Int32, ) -> System.Int32:
        ...

    @typing.overload
    def GetCharCount(self, bytes: list[System.Byte], index: System.Int32, count: System.Int32, flush: System.Boolean, ) -> System.Int32:
        ...

    @typing.overload
    def GetCharCount(self, bytes: ptr[System.Byte], count: System.Int32, flush: System.Boolean, ) -> System.Int32:
        ...

    @typing.overload
    def GetCharCount(self, bytes: System.ReadOnlySpan[System.Byte], flush: System.Boolean, ) -> System.Int32:
        ...

    @typing.overload
    @abc.abstractmethod
    def GetChars(self, bytes: list[System.Byte], byteIndex: System.Int32, byteCount: System.Int32, chars: list[System.Char], charIndex: System.Int32, ) -> System.Int32:
        ...

    @typing.overload
    def GetChars(self, bytes: list[System.Byte], byteIndex: System.Int32, byteCount: System.Int32, chars: list[System.Char], charIndex: System.Int32, flush: System.Boolean, ) -> System.Int32:
        ...

    @typing.overload
    def GetChars(self, bytes: ptr[System.Byte], byteCount: System.Int32, chars: ptr[System.Char], charCount: System.Int32, flush: System.Boolean, ) -> System.Int32:
        ...

    @typing.overload
    def GetChars(self, bytes: System.ReadOnlySpan[System.Byte], chars: System.Span[System.Char], flush: System.Boolean, ) -> System.Int32:
        ...

    @typing.overload
    def Convert(self, bytes: list[System.Byte], byteIndex: System.Int32, byteCount: System.Int32, chars: list[System.Char], charIndex: System.Int32, charCount: System.Int32, flush: System.Boolean, bytesUsed: ref[System.Int32], charsUsed: ref[System.Int32], completed: ref[System.Boolean], ) -> None:
        ...

    @typing.overload
    def Convert(self, bytes: ptr[System.Byte], byteCount: System.Int32, chars: ptr[System.Char], charCount: System.Int32, flush: System.Boolean, bytesUsed: ref[System.Int32], charsUsed: ref[System.Int32], completed: ref[System.Boolean], ) -> None:
        ...

    @typing.overload
    def Convert(self, bytes: System.ReadOnlySpan[System.Byte], chars: System.Span[System.Char], flush: System.Boolean, bytesUsed: ref[System.Int32], charsUsed: ref[System.Int32], completed: ref[System.Boolean], ) -> None:
        ...

class Encoder(System.Object, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

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

    # methods
    @typing.overload
    def Reset(self, ) -> None:
        ...

    @typing.overload
    @abc.abstractmethod
    def GetByteCount(self, chars: list[System.Char], index: System.Int32, count: System.Int32, flush: System.Boolean, ) -> System.Int32:
        ...

    @typing.overload
    def GetByteCount(self, chars: ptr[System.Char], count: System.Int32, flush: System.Boolean, ) -> System.Int32:
        ...

    @typing.overload
    def GetByteCount(self, chars: System.ReadOnlySpan[System.Char], flush: System.Boolean, ) -> System.Int32:
        ...

    @typing.overload
    @abc.abstractmethod
    def GetBytes(self, chars: list[System.Char], charIndex: System.Int32, charCount: System.Int32, bytes: list[System.Byte], byteIndex: System.Int32, flush: System.Boolean, ) -> System.Int32:
        ...

    @typing.overload
    def GetBytes(self, chars: ptr[System.Char], charCount: System.Int32, bytes: ptr[System.Byte], byteCount: System.Int32, flush: System.Boolean, ) -> System.Int32:
        ...

    @typing.overload
    def GetBytes(self, chars: System.ReadOnlySpan[System.Char], bytes: System.Span[System.Byte], flush: System.Boolean, ) -> System.Int32:
        ...

    @typing.overload
    def Convert(self, chars: list[System.Char], charIndex: System.Int32, charCount: System.Int32, bytes: list[System.Byte], byteIndex: System.Int32, byteCount: System.Int32, flush: System.Boolean, charsUsed: ref[System.Int32], bytesUsed: ref[System.Int32], completed: ref[System.Boolean], ) -> None:
        ...

    @typing.overload
    def Convert(self, chars: ptr[System.Char], charCount: System.Int32, bytes: ptr[System.Byte], byteCount: System.Int32, flush: System.Boolean, charsUsed: ref[System.Int32], bytesUsed: ref[System.Int32], completed: ref[System.Boolean], ) -> None:
        ...

    @typing.overload
    def Convert(self, chars: System.ReadOnlySpan[System.Char], bytes: System.Span[System.Byte], flush: System.Boolean, charsUsed: ref[System.Int32], bytesUsed: ref[System.Int32], completed: ref[System.Boolean], ) -> None:
        ...

class Rune(System.IComparable, System.IComparable[System.Text.Rune], System.IEquatable[System.Text.Rune], System.ISpanFormattable, System.IFormattable, System.ValueType):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def IsAscii(self) -> System.Boolean:
        ...

    @property
    def IsBmp(self) -> System.Boolean:
        ...

    @property
    def Plane(self) -> System.Int32:
        ...

    @property
    def ReplacementChar(self) -> System.Text.Rune:
        ...

    @property
    def Utf16SequenceLength(self) -> System.Int32:
        ...

    @property
    def Utf8SequenceLength(self) -> System.Int32:
        ...

    @property
    def Value(self) -> System.Int32:
        ...

    # methods
    @typing.overload
    def __init__(self, ch: System.Char, ):
        ...

    @typing.overload
    def __init__(self, highSurrogate: System.Char, lowSurrogate: System.Char, ):
        ...

    @typing.overload
    def __init__(self, value: System.Int32, ):
        ...

    @typing.overload
    def __init__(self, value: System.UInt32, ):
        ...

    @typing.overload
    def CompareTo(self, other: System.Text.Rune, ) -> System.Int32:
        ...

    @typing.overload
    @staticmethod
    def DecodeFromUtf16(source: System.ReadOnlySpan[System.Char], result: ref[System.Text.Rune], charsConsumed: ref[System.Int32], ) -> System.Buffers.OperationStatus:
        ...

    @typing.overload
    @staticmethod
    def DecodeFromUtf8(source: System.ReadOnlySpan[System.Byte], result: ref[System.Text.Rune], bytesConsumed: ref[System.Int32], ) -> System.Buffers.OperationStatus:
        ...

    @typing.overload
    @staticmethod
    def DecodeLastFromUtf16(source: System.ReadOnlySpan[System.Char], result: ref[System.Text.Rune], charsConsumed: ref[System.Int32], ) -> System.Buffers.OperationStatus:
        ...

    @typing.overload
    @staticmethod
    def DecodeLastFromUtf8(source: System.ReadOnlySpan[System.Byte], value: ref[System.Text.Rune], bytesConsumed: ref[System.Int32], ) -> System.Buffers.OperationStatus:
        ...

    @typing.overload
    def EncodeToUtf16(self, destination: System.Span[System.Char], ) -> System.Int32:
        ...

    @typing.overload
    def EncodeToUtf8(self, destination: System.Span[System.Byte], ) -> System.Int32:
        ...

    @typing.overload
    def Equals(self, obj: System.Object, ) -> System.Boolean:
        ...

    @typing.overload
    def Equals(self, other: System.Text.Rune, ) -> System.Boolean:
        ...

    @typing.overload
    def GetHashCode(self, ) -> System.Int32:
        ...

    @typing.overload
    @staticmethod
    def GetRuneAt(input: System.String, index: System.Int32, ) -> System.Text.Rune:
        ...

    @typing.overload
    @staticmethod
    def IsValid(value: System.Int32, ) -> System.Boolean:
        ...

    @typing.overload
    @staticmethod
    def IsValid(value: System.UInt32, ) -> System.Boolean:
        ...

    @typing.overload
    def ToString(self, ) -> System.String:
        ...

    @typing.overload
    @staticmethod
    def TryCreate(ch: System.Char, result: ref[System.Text.Rune], ) -> System.Boolean:
        ...

    @typing.overload
    @staticmethod
    def TryCreate(highSurrogate: System.Char, lowSurrogate: System.Char, result: ref[System.Text.Rune], ) -> System.Boolean:
        ...

    @typing.overload
    @staticmethod
    def TryCreate(value: System.Int32, result: ref[System.Text.Rune], ) -> System.Boolean:
        ...

    @typing.overload
    @staticmethod
    def TryCreate(value: System.UInt32, result: ref[System.Text.Rune], ) -> System.Boolean:
        ...

    @typing.overload
    def TryEncodeToUtf16(self, destination: System.Span[System.Char], charsWritten: ref[System.Int32], ) -> System.Boolean:
        ...

    @typing.overload
    def TryEncodeToUtf8(self, destination: System.Span[System.Byte], bytesWritten: ref[System.Int32], ) -> System.Boolean:
        ...

    @typing.overload
    @staticmethod
    def TryGetRuneAt(input: System.String, index: System.Int32, value: ref[System.Text.Rune], ) -> System.Boolean:
        ...

    @typing.overload
    @staticmethod
    def GetNumericValue(value: System.Text.Rune, ) -> System.Double:
        ...

    @typing.overload
    @staticmethod
    def GetUnicodeCategory(value: System.Text.Rune, ) -> System.Globalization.UnicodeCategory:
        ...

    @typing.overload
    @staticmethod
    def IsControl(value: System.Text.Rune, ) -> System.Boolean:
        ...

    @typing.overload
    @staticmethod
    def IsDigit(value: System.Text.Rune, ) -> System.Boolean:
        ...

    @typing.overload
    @staticmethod
    def IsLetter(value: System.Text.Rune, ) -> System.Boolean:
        ...

    @typing.overload
    @staticmethod
    def IsLetterOrDigit(value: System.Text.Rune, ) -> System.Boolean:
        ...

    @typing.overload
    @staticmethod
    def IsLower(value: System.Text.Rune, ) -> System.Boolean:
        ...

    @typing.overload
    @staticmethod
    def IsNumber(value: System.Text.Rune, ) -> System.Boolean:
        ...

    @typing.overload
    @staticmethod
    def IsPunctuation(value: System.Text.Rune, ) -> System.Boolean:
        ...

    @typing.overload
    @staticmethod
    def IsSeparator(value: System.Text.Rune, ) -> System.Boolean:
        ...

    @typing.overload
    @staticmethod
    def IsSymbol(value: System.Text.Rune, ) -> System.Boolean:
        ...

    @typing.overload
    @staticmethod
    def IsUpper(value: System.Text.Rune, ) -> System.Boolean:
        ...

    @typing.overload
    @staticmethod
    def IsWhiteSpace(value: System.Text.Rune, ) -> System.Boolean:
        ...

    @typing.overload
    @staticmethod
    def ToLower(value: System.Text.Rune, culture: System.Globalization.CultureInfo, ) -> System.Text.Rune:
        ...

    @typing.overload
    @staticmethod
    def ToLowerInvariant(value: System.Text.Rune, ) -> System.Text.Rune:
        ...

    @typing.overload
    @staticmethod
    def ToUpper(value: System.Text.Rune, culture: System.Globalization.CultureInfo, ) -> System.Text.Rune:
        ...

    @typing.overload
    @staticmethod
    def ToUpperInvariant(value: System.Text.Rune, ) -> System.Text.Rune:
        ...

class EncoderFallbackBuffer(System.Object, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @abc.abstractmethod
    @property
    def Remaining(self) -> System.Int32:
        ...

    # methods
    @typing.overload
    @abc.abstractmethod
    def Fallback(self, charUnknown: System.Char, index: System.Int32, ) -> System.Boolean:
        ...

    @typing.overload
    @abc.abstractmethod
    def Fallback(self, charUnknownHigh: System.Char, charUnknownLow: System.Char, index: System.Int32, ) -> System.Boolean:
        ...

    @typing.overload
    @abc.abstractmethod
    def GetNextChar(self, ) -> System.Char:
        ...

    @typing.overload
    @abc.abstractmethod
    def MovePrevious(self, ) -> System.Boolean:
        ...

    @typing.overload
    def Reset(self, ) -> None:
        ...

class DecoderFallbackBuffer(System.Object, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @abc.abstractmethod
    @property
    def Remaining(self) -> System.Int32:
        ...

    # methods
    @typing.overload
    @abc.abstractmethod
    def Fallback(self, bytesUnknown: list[System.Byte], index: System.Int32, ) -> System.Boolean:
        ...

    @typing.overload
    @abc.abstractmethod
    def GetNextChar(self, ) -> System.Char:
        ...

    @typing.overload
    @abc.abstractmethod
    def MovePrevious(self, ) -> System.Boolean:
        ...

    @typing.overload
    def Reset(self, ) -> None:
        ...

class StringBuilder(System.Runtime.Serialization.ISerializable, System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def Capacity(self) -> System.Int32:
        ...
    @Capacity.setter
    def Capacity(self, val: System.Int32):
        ...

    @property
    def MaxCapacity(self) -> System.Int32:
        ...

    @property
    def Length(self) -> System.Int32:
        ...
    @Length.setter
    def Length(self, val: System.Int32):
        ...

    @property
    def Chars(self) -> System.Char:
        ...
    @Chars.setter
    def Chars(self, val: System.Char):
        ...

    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def __init__(self, capacity: System.Int32, ):
        ...

    @typing.overload
    def __init__(self, value: System.String, ):
        ...

    @typing.overload
    def __init__(self, value: System.String, capacity: System.Int32, ):
        ...

    @typing.overload
    def __init__(self, value: System.String, startIndex: System.Int32, length: System.Int32, capacity: System.Int32, ):
        ...

    @typing.overload
    def __init__(self, capacity: System.Int32, maxCapacity: System.Int32, ):
        ...

    @typing.overload
    def Insert(self, index: System.Int32, value: System.Double, ) -> System.Text.StringBuilder:
        ...

    @typing.overload
    def Insert(self, index: System.Int32, value: System.Decimal, ) -> System.Text.StringBuilder:
        ...

    @typing.overload
    def Insert(self, index: System.Int32, value: System.UInt16, ) -> System.Text.StringBuilder:
        ...

    @typing.overload
    def Insert(self, index: System.Int32, value: System.UInt32, ) -> System.Text.StringBuilder:
        ...

    @typing.overload
    def Insert(self, index: System.Int32, value: System.UInt64, ) -> System.Text.StringBuilder:
        ...

    @typing.overload
    def Insert(self, index: System.Int32, value: System.Object, ) -> System.Text.StringBuilder:
        ...

    @typing.overload
    def Insert(self, index: System.Int32, value: System.ReadOnlySpan[System.Char], ) -> System.Text.StringBuilder:
        ...

    @typing.overload
    def AppendFormat(self, format: System.String, arg0: System.Object, ) -> System.Text.StringBuilder:
        ...

    @typing.overload
    def AppendFormat(self, format: System.String, arg0: System.Object, arg1: System.Object, ) -> System.Text.StringBuilder:
        ...

    @typing.overload
    def AppendFormat(self, format: System.String, arg0: System.Object, arg1: System.Object, arg2: System.Object, ) -> System.Text.StringBuilder:
        ...

    @typing.overload
    def AppendFormat(self, format: System.String, args: list[System.Object], ) -> System.Text.StringBuilder:
        ...

    @typing.overload
    def AppendFormat(self, provider: System.IFormatProvider, format: System.String, arg0: System.Object, ) -> System.Text.StringBuilder:
        ...

    @typing.overload
    def AppendFormat(self, provider: System.IFormatProvider, format: System.String, arg0: System.Object, arg1: System.Object, ) -> System.Text.StringBuilder:
        ...

    @typing.overload
    def AppendFormat(self, provider: System.IFormatProvider, format: System.String, arg0: System.Object, arg1: System.Object, arg2: System.Object, ) -> System.Text.StringBuilder:
        ...

    @typing.overload
    def AppendFormat(self, provider: System.IFormatProvider, format: System.String, args: list[System.Object], ) -> System.Text.StringBuilder:
        ...

    @typing.overload
    def Replace(self, oldValue: System.String, newValue: System.String, ) -> System.Text.StringBuilder:
        ...

    @typing.overload
    def Equals(self, sb: System.Text.StringBuilder, ) -> System.Boolean:
        ...

    @typing.overload
    def Equals(self, span: System.ReadOnlySpan[System.Char], ) -> System.Boolean:
        ...

    @typing.overload
    def Replace(self, oldValue: System.String, newValue: System.String, startIndex: System.Int32, count: System.Int32, ) -> System.Text.StringBuilder:
        ...

    @typing.overload
    def Replace(self, oldChar: System.Char, newChar: System.Char, ) -> System.Text.StringBuilder:
        ...

    @typing.overload
    def Replace(self, oldChar: System.Char, newChar: System.Char, startIndex: System.Int32, count: System.Int32, ) -> System.Text.StringBuilder:
        ...

    @typing.overload
    def Append(self, value: ptr[System.Char], valueCount: System.Int32, ) -> System.Text.StringBuilder:
        ...

    @typing.overload
    def EnsureCapacity(self, capacity: System.Int32, ) -> System.Int32:
        ...

    @typing.overload
    def ToString(self, ) -> System.String:
        ...

    @typing.overload
    def ToString(self, startIndex: System.Int32, length: System.Int32, ) -> System.String:
        ...

    @typing.overload
    def Clear(self, ) -> System.Text.StringBuilder:
        ...

    @typing.overload
    def GetChunks(self, ) -> System.Text.StringBuilder.ChunkEnumerator:
        ...

    @typing.overload
    def Append(self, value: System.Char, repeatCount: System.Int32, ) -> System.Text.StringBuilder:
        ...

    @typing.overload
    def Append(self, value: list[System.Char], startIndex: System.Int32, charCount: System.Int32, ) -> System.Text.StringBuilder:
        ...

    @typing.overload
    def Append(self, value: System.String, ) -> System.Text.StringBuilder:
        ...

    @typing.overload
    def Append(self, value: System.String, startIndex: System.Int32, count: System.Int32, ) -> System.Text.StringBuilder:
        ...

    @typing.overload
    def Append(self, value: System.Text.StringBuilder, ) -> System.Text.StringBuilder:
        ...

    @typing.overload
    def Append(self, value: System.Text.StringBuilder, startIndex: System.Int32, count: System.Int32, ) -> System.Text.StringBuilder:
        ...

    @typing.overload
    def AppendLine(self, ) -> System.Text.StringBuilder:
        ...

    @typing.overload
    def AppendLine(self, value: System.String, ) -> System.Text.StringBuilder:
        ...

    @typing.overload
    def CopyTo(self, sourceIndex: System.Int32, destination: list[System.Char], destinationIndex: System.Int32, count: System.Int32, ) -> None:
        ...

    @typing.overload
    def CopyTo(self, sourceIndex: System.Int32, destination: System.Span[System.Char], count: System.Int32, ) -> None:
        ...

    @typing.overload
    def Insert(self, index: System.Int32, value: System.String, count: System.Int32, ) -> System.Text.StringBuilder:
        ...

    @typing.overload
    def Remove(self, startIndex: System.Int32, length: System.Int32, ) -> System.Text.StringBuilder:
        ...

    @typing.overload
    def Append(self, value: System.Boolean, ) -> System.Text.StringBuilder:
        ...

    @typing.overload
    def Append(self, value: System.Char, ) -> System.Text.StringBuilder:
        ...

    @typing.overload
    def Append(self, value: System.SByte, ) -> System.Text.StringBuilder:
        ...

    @typing.overload
    def Append(self, value: System.Byte, ) -> System.Text.StringBuilder:
        ...

    @typing.overload
    def Append(self, value: System.Int16, ) -> System.Text.StringBuilder:
        ...

    @typing.overload
    def Append(self, value: System.Int32, ) -> System.Text.StringBuilder:
        ...

    @typing.overload
    def Append(self, value: System.Int64, ) -> System.Text.StringBuilder:
        ...

    @typing.overload
    def Append(self, value: System.Single, ) -> System.Text.StringBuilder:
        ...

    @typing.overload
    def Append(self, value: System.Double, ) -> System.Text.StringBuilder:
        ...

    @typing.overload
    def Append(self, value: System.Decimal, ) -> System.Text.StringBuilder:
        ...

    @typing.overload
    def Append(self, value: System.UInt16, ) -> System.Text.StringBuilder:
        ...

    @typing.overload
    def Append(self, value: System.UInt32, ) -> System.Text.StringBuilder:
        ...

    @typing.overload
    def Append(self, value: System.UInt64, ) -> System.Text.StringBuilder:
        ...

    @typing.overload
    def Append(self, value: System.Object, ) -> System.Text.StringBuilder:
        ...

    @typing.overload
    def Append(self, value: list[System.Char], ) -> System.Text.StringBuilder:
        ...

    @typing.overload
    def Append(self, value: System.ReadOnlySpan[System.Char], ) -> System.Text.StringBuilder:
        ...

    @typing.overload
    def Append(self, value: System.ReadOnlyMemory[System.Char], ) -> System.Text.StringBuilder:
        ...

    @typing.overload
    def Append(self, handler: ref[System.Text.StringBuilder.AppendInterpolatedStringHandler], ) -> System.Text.StringBuilder:
        ...

    @typing.overload
    def Append(self, provider: System.IFormatProvider, handler: ref[System.Text.StringBuilder.AppendInterpolatedStringHandler], ) -> System.Text.StringBuilder:
        ...

    @typing.overload
    def AppendLine(self, handler: ref[System.Text.StringBuilder.AppendInterpolatedStringHandler], ) -> System.Text.StringBuilder:
        ...

    @typing.overload
    def AppendLine(self, provider: System.IFormatProvider, handler: ref[System.Text.StringBuilder.AppendInterpolatedStringHandler], ) -> System.Text.StringBuilder:
        ...

    @typing.overload
    def AppendJoin(self, separator: System.String, values: list[System.Object], ) -> System.Text.StringBuilder:
        ...

    @typing.overload
    def AppendJoin(self, separator: System.String, values: System.Collections.Generic.IEnumerable[T], ) -> System.Text.StringBuilder:
        ...

    @typing.overload
    def AppendJoin(self, separator: System.String, values: list[System.String], ) -> System.Text.StringBuilder:
        ...

    @typing.overload
    def AppendJoin(self, separator: System.Char, values: list[System.Object], ) -> System.Text.StringBuilder:
        ...

    @typing.overload
    def AppendJoin(self, separator: System.Char, values: System.Collections.Generic.IEnumerable[T], ) -> System.Text.StringBuilder:
        ...

    @typing.overload
    def AppendJoin(self, separator: System.Char, values: list[System.String], ) -> System.Text.StringBuilder:
        ...

    @typing.overload
    def Insert(self, index: System.Int32, value: System.String, ) -> System.Text.StringBuilder:
        ...

    @typing.overload
    def Insert(self, index: System.Int32, value: System.Boolean, ) -> System.Text.StringBuilder:
        ...

    @typing.overload
    def Insert(self, index: System.Int32, value: System.SByte, ) -> System.Text.StringBuilder:
        ...

    @typing.overload
    def Insert(self, index: System.Int32, value: System.Byte, ) -> System.Text.StringBuilder:
        ...

    @typing.overload
    def Insert(self, index: System.Int32, value: System.Int16, ) -> System.Text.StringBuilder:
        ...

    @typing.overload
    def Insert(self, index: System.Int32, value: System.Char, ) -> System.Text.StringBuilder:
        ...

    @typing.overload
    def Insert(self, index: System.Int32, value: list[System.Char], ) -> System.Text.StringBuilder:
        ...

    @typing.overload
    def Insert(self, index: System.Int32, value: list[System.Char], startIndex: System.Int32, charCount: System.Int32, ) -> System.Text.StringBuilder:
        ...

    @typing.overload
    def Insert(self, index: System.Int32, value: System.Int32, ) -> System.Text.StringBuilder:
        ...

    @typing.overload
    def Insert(self, index: System.Int32, value: System.Int64, ) -> System.Text.StringBuilder:
        ...

    @typing.overload
    def Insert(self, index: System.Int32, value: System.Single, ) -> System.Text.StringBuilder:
        ...

