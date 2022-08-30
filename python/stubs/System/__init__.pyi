from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import System
import System.Globalization
import System.Collections
import System.Collections.Generic
import System.Text
import System.Buffers
import System.Runtime.CompilerServices
import System.Runtime.Serialization
import System.Reflection
import System.Threading
import System.Runtime.InteropServices
import System.ReadOnlySpan
import System.Span
import System.Collections.ObjectModel
import System.Threading.Tasks

T = typing.TypeVar('T')
TState = typing.TypeVar('TState')
TEnum = typing.TypeVar('TEnum')
T1 = typing.TypeVar('T1')
T2 = typing.TypeVar('T2')
T3 = typing.TypeVar('T3')
TResult = typing.TypeVar('TResult')
TSelf = typing.TypeVar('TSelf')
TOther = typing.TypeVar('TOther')
TInput = typing.TypeVar('TInput')
TOutput = typing.TypeVar('TOutput')
TKey = typing.TypeVar('TKey')
TValue = typing.TypeVar('TValue')
TInteger = typing.TypeVar('TInteger')
T4 = typing.TypeVar('T4')
T5 = typing.TypeVar('T5')
T6 = typing.TypeVar('T6')
T7 = typing.TypeVar('T7')
T8 = typing.TypeVar('T8')
T9 = typing.TypeVar('T9')
T10 = typing.TypeVar('T10')
T11 = typing.TypeVar('T11')
T12 = typing.TypeVar('T12')
T13 = typing.TypeVar('T13')
T14 = typing.TypeVar('T14')
T15 = typing.TypeVar('T15')
T16 = typing.TypeVar('T16')

class Object():
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def Equals(self, obj: System.Object, ) -> System.Boolean:
        ...

    @typing.overload
    def GetHashCode(self, ) -> System.Int32:
        ...

    @typing.overload
    def ToString(self, ) -> System.String:
        ...

    @typing.overload
    def GetType(self, ) -> System.Type:
        ...

    @typing.overload
    @staticmethod
    def Equals(objA: System.Object, objB: System.Object, ) -> System.Boolean:
        ...

    @typing.overload
    @staticmethod
    def ReferenceEquals(objA: System.Object, objB: System.Object, ) -> System.Boolean:
        ...

class Byte(System.IComparable, System.IConvertible, System.ISpanFormattable, System.IFormattable, System.IComparable[System.Byte], System.IEquatable[System.Byte], System.IBinaryInteger[System.Byte], System.IBinaryNumber[System.Byte], System.IBitwiseOperators[System.Byte, System.Byte, System.Byte], System.INumber[System.Byte], System.IAdditionOperators[System.Byte, System.Byte, System.Byte], System.IAdditiveIdentity[System.Byte, System.Byte], System.IComparisonOperators[System.Byte, System.Byte], System.IEqualityOperators[System.Byte, System.Byte], System.IDecrementOperators[System.Byte], System.IDivisionOperators[System.Byte, System.Byte, System.Byte], System.IIncrementOperators[System.Byte], System.IModulusOperators[System.Byte, System.Byte, System.Byte], System.IMultiplicativeIdentity[System.Byte, System.Byte], System.IMultiplyOperators[System.Byte, System.Byte, System.Byte], System.ISpanParseable[System.Byte], System.IParseable[System.Byte], System.ISubtractionOperators[System.Byte, System.Byte, System.Byte], System.IUnaryNegationOperators[System.Byte, System.Byte], System.IUnaryPlusOperators[System.Byte, System.Byte], System.IShiftOperators[System.Byte, System.Byte], System.IMinMaxValue[System.Byte], System.IUnsignedNumber[System.Byte], System.ValueType):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    # methods
    @typing.overload
    def CompareTo(self, value: System.Object, ) -> System.Int32:
        ...

    @typing.overload
    def CompareTo(self, value: System.Byte, ) -> System.Int32:
        ...

    @typing.overload
    def Equals(self, obj: System.Object, ) -> System.Boolean:
        ...

    @typing.overload
    def Equals(self, obj: System.Byte, ) -> System.Boolean:
        ...

    @typing.overload
    def GetHashCode(self, ) -> System.Int32:
        ...

    @typing.overload
    @staticmethod
    def Parse(s: System.String, ) -> System.Byte:
        ...

    @typing.overload
    @staticmethod
    def Parse(s: System.String, style: System.Globalization.NumberStyles, ) -> System.Byte:
        ...

    @typing.overload
    @staticmethod
    def Parse(s: System.String, provider: System.IFormatProvider, ) -> System.Byte:
        ...

    @typing.overload
    @staticmethod
    def Parse(s: System.String, style: System.Globalization.NumberStyles, provider: System.IFormatProvider, ) -> System.Byte:
        ...

    @typing.overload
    @staticmethod
    def Parse(s: System.ReadOnlySpan[System.Char], style: System.Globalization.NumberStyles, provider: System.IFormatProvider, ) -> System.Byte:
        ...

    @typing.overload
    @staticmethod
    def TryParse(s: System.String, result: ref[System.Byte], ) -> System.Boolean:
        ...

    @typing.overload
    @staticmethod
    def TryParse(s: System.ReadOnlySpan[System.Char], result: ref[System.Byte], ) -> System.Boolean:
        ...

    @typing.overload
    @staticmethod
    def TryParse(s: System.String, style: System.Globalization.NumberStyles, provider: System.IFormatProvider, result: ref[System.Byte], ) -> System.Boolean:
        ...

    @typing.overload
    @staticmethod
    def TryParse(s: System.ReadOnlySpan[System.Char], style: System.Globalization.NumberStyles, provider: System.IFormatProvider, result: ref[System.Byte], ) -> System.Boolean:
        ...

    @typing.overload
    def ToString(self, ) -> System.String:
        ...

    @typing.overload
    def ToString(self, format: System.String, ) -> System.String:
        ...

    @typing.overload
    def ToString(self, provider: System.IFormatProvider, ) -> System.String:
        ...

    @typing.overload
    def ToString(self, format: System.String, provider: System.IFormatProvider, ) -> System.String:
        ...

    @typing.overload
    def TryFormat(self, destination: System.Span[System.Char], charsWritten: ref[System.Int32], format: System.ReadOnlySpan[System.Char], provider: System.IFormatProvider, ) -> System.Boolean:
        ...

    @typing.overload
    def GetTypeCode(self, ) -> System.TypeCode:
        ...

class String(System.IComparable, System.Collections.IEnumerable, System.IConvertible, System.Collections.Generic.IEnumerable[System.Char], System.IComparable[System.String], System.IEquatable[System.String], System.ICloneable, System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def Chars(self) -> System.Char:
        ...

    @property
    def Length(self) -> System.Int32:
        ...

    # methods
    @typing.overload
    def __init__(self, value: list[System.Char], ):
        ...

    @typing.overload
    def __init__(self, value: list[System.Char], startIndex: System.Int32, length: System.Int32, ):
        ...

    @typing.overload
    def __init__(self, value: ptr[System.Char], ):
        ...

    @typing.overload
    def __init__(self, value: ptr[System.Char], startIndex: System.Int32, length: System.Int32, ):
        ...

    @typing.overload
    def __init__(self, value: ptr[System.SByte], ):
        ...

    @typing.overload
    def __init__(self, value: ptr[System.SByte], startIndex: System.Int32, length: System.Int32, ):
        ...

    @typing.overload
    def __init__(self, value: ptr[System.SByte], startIndex: System.Int32, length: System.Int32, enc: System.Text.Encoding, ):
        ...

    @typing.overload
    def __init__(self, c: System.Char, count: System.Int32, ):
        ...

    @typing.overload
    def __init__(self, value: System.ReadOnlySpan[System.Char], ):
        ...

    @typing.overload
    def LastIndexOf(self, value: System.String, startIndex: System.Int32, ) -> System.Int32:
        ...

    @typing.overload
    def LastIndexOf(self, value: System.String, startIndex: System.Int32, count: System.Int32, ) -> System.Int32:
        ...

    @typing.overload
    def LastIndexOf(self, value: System.String, comparisonType: System.StringComparison, ) -> System.Int32:
        ...

    @typing.overload
    def LastIndexOf(self, value: System.String, startIndex: System.Int32, comparisonType: System.StringComparison, ) -> System.Int32:
        ...

    @typing.overload
    def LastIndexOf(self, value: System.String, startIndex: System.Int32, count: System.Int32, comparisonType: System.StringComparison, ) -> System.Int32:
        ...

    @typing.overload
    def PadRight(self, totalWidth: System.Int32, ) -> System.String:
        ...

    @typing.overload
    def PadRight(self, totalWidth: System.Int32, paddingChar: System.Char, ) -> System.String:
        ...

    @typing.overload
    def Remove(self, startIndex: System.Int32, count: System.Int32, ) -> System.String:
        ...

    @typing.overload
    def Remove(self, startIndex: System.Int32, ) -> System.String:
        ...

    @typing.overload
    def Replace(self, oldValue: System.String, newValue: System.String, ignoreCase: System.Boolean, culture: System.Globalization.CultureInfo, ) -> System.String:
        ...

    @typing.overload
    def Replace(self, oldValue: System.String, newValue: System.String, comparisonType: System.StringComparison, ) -> System.String:
        ...

    @typing.overload
    def Replace(self, oldChar: System.Char, newChar: System.Char, ) -> System.String:
        ...

    @typing.overload
    def Replace(self, oldValue: System.String, newValue: System.String, ) -> System.String:
        ...

    @typing.overload
    def ReplaceLineEndings(self, ) -> System.String:
        ...

    @typing.overload
    def ReplaceLineEndings(self, replacementText: System.String, ) -> System.String:
        ...

    @typing.overload
    def Split(self, separator: System.Char, options: System.StringSplitOptions, ) -> list[System.String]:
        ...

    @typing.overload
    def Split(self, separator: System.Char, count: System.Int32, options: System.StringSplitOptions, ) -> list[System.String]:
        ...

    @typing.overload
    def Split(self, separator: list[System.Char], ) -> list[System.String]:
        ...

    @typing.overload
    def Split(self, separator: list[System.Char], count: System.Int32, ) -> list[System.String]:
        ...

    @typing.overload
    def Split(self, separator: list[System.Char], options: System.StringSplitOptions, ) -> list[System.String]:
        ...

    @typing.overload
    def Split(self, separator: list[System.Char], count: System.Int32, options: System.StringSplitOptions, ) -> list[System.String]:
        ...

    @typing.overload
    def Split(self, separator: System.String, options: System.StringSplitOptions, ) -> list[System.String]:
        ...

    @typing.overload
    def Split(self, separator: System.String, count: System.Int32, options: System.StringSplitOptions, ) -> list[System.String]:
        ...

    @typing.overload
    def Split(self, separator: list[System.String], options: System.StringSplitOptions, ) -> list[System.String]:
        ...

    @typing.overload
    def Split(self, separator: list[System.String], count: System.Int32, options: System.StringSplitOptions, ) -> list[System.String]:
        ...

    @typing.overload
    def Substring(self, startIndex: System.Int32, ) -> System.String:
        ...

    @typing.overload
    def Substring(self, startIndex: System.Int32, length: System.Int32, ) -> System.String:
        ...

    @typing.overload
    def ToLower(self, ) -> System.String:
        ...

    @typing.overload
    def ToLower(self, culture: System.Globalization.CultureInfo, ) -> System.String:
        ...

    @typing.overload
    def ToLowerInvariant(self, ) -> System.String:
        ...

    @typing.overload
    def ToUpper(self, ) -> System.String:
        ...

    @typing.overload
    def ToUpper(self, culture: System.Globalization.CultureInfo, ) -> System.String:
        ...

    @typing.overload
    def ToUpperInvariant(self, ) -> System.String:
        ...

    @typing.overload
    def Trim(self, ) -> System.String:
        ...

    @typing.overload
    def Trim(self, trimChar: System.Char, ) -> System.String:
        ...

    @typing.overload
    def Trim(self, trimChars: list[System.Char], ) -> System.String:
        ...

    @typing.overload
    def TrimStart(self, ) -> System.String:
        ...

    @typing.overload
    def TrimStart(self, trimChar: System.Char, ) -> System.String:
        ...

    @typing.overload
    def TrimStart(self, trimChars: list[System.Char], ) -> System.String:
        ...

    @typing.overload
    def TrimEnd(self, ) -> System.String:
        ...

    @typing.overload
    def TrimEnd(self, trimChar: System.Char, ) -> System.String:
        ...

    @typing.overload
    def TrimEnd(self, trimChars: list[System.Char], ) -> System.String:
        ...

    @typing.overload
    def Contains(self, value: System.String, ) -> System.Boolean:
        ...

    @typing.overload
    def Contains(self, value: System.String, comparisonType: System.StringComparison, ) -> System.Boolean:
        ...

    @typing.overload
    def Contains(self, value: System.Char, ) -> System.Boolean:
        ...

    @typing.overload
    def Contains(self, value: System.Char, comparisonType: System.StringComparison, ) -> System.Boolean:
        ...

    @typing.overload
    def IndexOf(self, value: System.Char, ) -> System.Int32:
        ...

    @typing.overload
    def IndexOf(self, value: System.Char, startIndex: System.Int32, ) -> System.Int32:
        ...

    @typing.overload
    def IndexOf(self, value: System.Char, comparisonType: System.StringComparison, ) -> System.Int32:
        ...

    @typing.overload
    def IndexOf(self, value: System.Char, startIndex: System.Int32, count: System.Int32, ) -> System.Int32:
        ...

    @typing.overload
    def IndexOfAny(self, anyOf: list[System.Char], ) -> System.Int32:
        ...

    @typing.overload
    def IndexOfAny(self, anyOf: list[System.Char], startIndex: System.Int32, ) -> System.Int32:
        ...

    @typing.overload
    def IndexOfAny(self, anyOf: list[System.Char], startIndex: System.Int32, count: System.Int32, ) -> System.Int32:
        ...

    @typing.overload
    def IndexOf(self, value: System.String, ) -> System.Int32:
        ...

    @typing.overload
    def IndexOf(self, value: System.String, startIndex: System.Int32, ) -> System.Int32:
        ...

    @typing.overload
    def IndexOf(self, value: System.String, startIndex: System.Int32, count: System.Int32, ) -> System.Int32:
        ...

    @typing.overload
    def IndexOf(self, value: System.String, comparisonType: System.StringComparison, ) -> System.Int32:
        ...

    @typing.overload
    def IndexOf(self, value: System.String, startIndex: System.Int32, comparisonType: System.StringComparison, ) -> System.Int32:
        ...

    @typing.overload
    def IndexOf(self, value: System.String, startIndex: System.Int32, count: System.Int32, comparisonType: System.StringComparison, ) -> System.Int32:
        ...

    @typing.overload
    def LastIndexOf(self, value: System.Char, ) -> System.Int32:
        ...

    @typing.overload
    def LastIndexOf(self, value: System.Char, startIndex: System.Int32, ) -> System.Int32:
        ...

    @typing.overload
    def LastIndexOf(self, value: System.Char, startIndex: System.Int32, count: System.Int32, ) -> System.Int32:
        ...

    @typing.overload
    def LastIndexOfAny(self, anyOf: list[System.Char], ) -> System.Int32:
        ...

    @typing.overload
    def LastIndexOfAny(self, anyOf: list[System.Char], startIndex: System.Int32, ) -> System.Int32:
        ...

    @typing.overload
    def LastIndexOfAny(self, anyOf: list[System.Char], startIndex: System.Int32, count: System.Int32, ) -> System.Int32:
        ...

    @typing.overload
    def LastIndexOf(self, value: System.String, ) -> System.Int32:
        ...

    @typing.overload
    @staticmethod
    def IsNullOrEmpty(value: System.String, ) -> System.Boolean:
        ...

    @typing.overload
    @staticmethod
    def IsNullOrWhiteSpace(value: System.String, ) -> System.Boolean:
        ...

    @typing.overload
    def GetPinnableReference(self, ) -> ref[System.Char]:
        ...

    @typing.overload
    def ToString(self, ) -> System.String:
        ...

    @typing.overload
    def ToString(self, provider: System.IFormatProvider, ) -> System.String:
        ...

    @typing.overload
    def GetEnumerator(self, ) -> System.CharEnumerator:
        ...

    @typing.overload
    def EnumerateRunes(self, ) -> System.Text.StringRuneEnumerator:
        ...

    @typing.overload
    def GetTypeCode(self, ) -> System.TypeCode:
        ...

    @typing.overload
    def IsNormalized(self, ) -> System.Boolean:
        ...

    @typing.overload
    def IsNormalized(self, normalizationForm: System.Text.NormalizationForm, ) -> System.Boolean:
        ...

    @typing.overload
    def Normalize(self, ) -> System.String:
        ...

    @typing.overload
    def Normalize(self, normalizationForm: System.Text.NormalizationForm, ) -> System.String:
        ...

    @typing.overload
    @staticmethod
    def Concat(arg0: System.Object, ) -> System.String:
        ...

    @typing.overload
    @staticmethod
    def Concat(arg0: System.Object, arg1: System.Object, ) -> System.String:
        ...

    @typing.overload
    @staticmethod
    def Concat(arg0: System.Object, arg1: System.Object, arg2: System.Object, ) -> System.String:
        ...

    @typing.overload
    @staticmethod
    def Concat(args: list[System.Object], ) -> System.String:
        ...

    @typing.overload
    @staticmethod
    def Concat(values: System.Collections.Generic.IEnumerable[T], ) -> System.String:
        ...

    @typing.overload
    @staticmethod
    def Concat(values: System.Collections.Generic.IEnumerable[System.String], ) -> System.String:
        ...

    @typing.overload
    @staticmethod
    def Concat(str0: System.String, str1: System.String, ) -> System.String:
        ...

    @typing.overload
    @staticmethod
    def Concat(str0: System.String, str1: System.String, str2: System.String, ) -> System.String:
        ...

    @typing.overload
    @staticmethod
    def Concat(str0: System.String, str1: System.String, str2: System.String, str3: System.String, ) -> System.String:
        ...

    @typing.overload
    @staticmethod
    def Concat(str0: System.ReadOnlySpan[System.Char], str1: System.ReadOnlySpan[System.Char], ) -> System.String:
        ...

    @typing.overload
    @staticmethod
    def Concat(str0: System.ReadOnlySpan[System.Char], str1: System.ReadOnlySpan[System.Char], str2: System.ReadOnlySpan[System.Char], ) -> System.String:
        ...

    @typing.overload
    @staticmethod
    def Concat(str0: System.ReadOnlySpan[System.Char], str1: System.ReadOnlySpan[System.Char], str2: System.ReadOnlySpan[System.Char], str3: System.ReadOnlySpan[System.Char], ) -> System.String:
        ...

    @typing.overload
    @staticmethod
    def Concat(values: list[System.String], ) -> System.String:
        ...

    @typing.overload
    @staticmethod
    def Format(format: System.String, arg0: System.Object, ) -> System.String:
        ...

    @typing.overload
    @staticmethod
    def Format(format: System.String, arg0: System.Object, arg1: System.Object, ) -> System.String:
        ...

    @typing.overload
    @staticmethod
    def Format(format: System.String, arg0: System.Object, arg1: System.Object, arg2: System.Object, ) -> System.String:
        ...

    @typing.overload
    @staticmethod
    def Format(format: System.String, args: list[System.Object], ) -> System.String:
        ...

    @typing.overload
    @staticmethod
    def Format(provider: System.IFormatProvider, format: System.String, arg0: System.Object, ) -> System.String:
        ...

    @typing.overload
    @staticmethod
    def Format(provider: System.IFormatProvider, format: System.String, arg0: System.Object, arg1: System.Object, ) -> System.String:
        ...

    @typing.overload
    @staticmethod
    def Format(provider: System.IFormatProvider, format: System.String, arg0: System.Object, arg1: System.Object, arg2: System.Object, ) -> System.String:
        ...

    @typing.overload
    @staticmethod
    def Format(provider: System.IFormatProvider, format: System.String, args: list[System.Object], ) -> System.String:
        ...

    @typing.overload
    def Insert(self, startIndex: System.Int32, value: System.String, ) -> System.String:
        ...

    @typing.overload
    @staticmethod
    def Join(separator: System.Char, value: list[System.String], ) -> System.String:
        ...

    @typing.overload
    @staticmethod
    def Join(separator: System.String, value: list[System.String], ) -> System.String:
        ...

    @typing.overload
    @staticmethod
    def Join(separator: System.Char, value: list[System.String], startIndex: System.Int32, count: System.Int32, ) -> System.String:
        ...

    @typing.overload
    @staticmethod
    def Join(separator: System.String, value: list[System.String], startIndex: System.Int32, count: System.Int32, ) -> System.String:
        ...

    @typing.overload
    @staticmethod
    def Join(separator: System.String, values: System.Collections.Generic.IEnumerable[System.String], ) -> System.String:
        ...

    @typing.overload
    @staticmethod
    def Join(separator: System.Char, values: list[System.Object], ) -> System.String:
        ...

    @typing.overload
    @staticmethod
    def Join(separator: System.String, values: list[System.Object], ) -> System.String:
        ...

    @typing.overload
    @staticmethod
    def Join(separator: System.Char, values: System.Collections.Generic.IEnumerable[T], ) -> System.String:
        ...

    @typing.overload
    @staticmethod
    def Join(separator: System.String, values: System.Collections.Generic.IEnumerable[T], ) -> System.String:
        ...

    @typing.overload
    def PadLeft(self, totalWidth: System.Int32, ) -> System.String:
        ...

    @typing.overload
    def PadLeft(self, totalWidth: System.Int32, paddingChar: System.Char, ) -> System.String:
        ...

    @typing.overload
    @staticmethod
    def Intern(str: System.String, ) -> System.String:
        ...

    @typing.overload
    @staticmethod
    def IsInterned(str: System.String, ) -> System.String:
        ...

    @typing.overload
    @staticmethod
    def Compare(strA: System.String, strB: System.String, ) -> System.Int32:
        ...

    @typing.overload
    @staticmethod
    def Compare(strA: System.String, strB: System.String, ignoreCase: System.Boolean, ) -> System.Int32:
        ...

    @typing.overload
    @staticmethod
    def Compare(strA: System.String, strB: System.String, comparisonType: System.StringComparison, ) -> System.Int32:
        ...

    @typing.overload
    @staticmethod
    def Compare(strA: System.String, strB: System.String, culture: System.Globalization.CultureInfo, options: System.Globalization.CompareOptions, ) -> System.Int32:
        ...

    @typing.overload
    @staticmethod
    def Compare(strA: System.String, strB: System.String, ignoreCase: System.Boolean, culture: System.Globalization.CultureInfo, ) -> System.Int32:
        ...

    @typing.overload
    @staticmethod
    def Compare(strA: System.String, indexA: System.Int32, strB: System.String, indexB: System.Int32, length: System.Int32, ) -> System.Int32:
        ...

    @typing.overload
    @staticmethod
    def Compare(strA: System.String, indexA: System.Int32, strB: System.String, indexB: System.Int32, length: System.Int32, ignoreCase: System.Boolean, ) -> System.Int32:
        ...

    @typing.overload
    @staticmethod
    def Compare(strA: System.String, indexA: System.Int32, strB: System.String, indexB: System.Int32, length: System.Int32, ignoreCase: System.Boolean, culture: System.Globalization.CultureInfo, ) -> System.Int32:
        ...

    @typing.overload
    @staticmethod
    def Compare(strA: System.String, indexA: System.Int32, strB: System.String, indexB: System.Int32, length: System.Int32, culture: System.Globalization.CultureInfo, options: System.Globalization.CompareOptions, ) -> System.Int32:
        ...

    @typing.overload
    @staticmethod
    def Compare(strA: System.String, indexA: System.Int32, strB: System.String, indexB: System.Int32, length: System.Int32, comparisonType: System.StringComparison, ) -> System.Int32:
        ...

    @typing.overload
    @staticmethod
    def CompareOrdinal(strA: System.String, strB: System.String, ) -> System.Int32:
        ...

    @typing.overload
    @staticmethod
    def CompareOrdinal(strA: System.String, indexA: System.Int32, strB: System.String, indexB: System.Int32, length: System.Int32, ) -> System.Int32:
        ...

    @typing.overload
    def CompareTo(self, value: System.Object, ) -> System.Int32:
        ...

    @typing.overload
    def CompareTo(self, strB: System.String, ) -> System.Int32:
        ...

    @typing.overload
    def EndsWith(self, value: System.String, ) -> System.Boolean:
        ...

    @typing.overload
    def EndsWith(self, value: System.String, comparisonType: System.StringComparison, ) -> System.Boolean:
        ...

    @typing.overload
    def EndsWith(self, value: System.String, ignoreCase: System.Boolean, culture: System.Globalization.CultureInfo, ) -> System.Boolean:
        ...

    @typing.overload
    def EndsWith(self, value: System.Char, ) -> System.Boolean:
        ...

    @typing.overload
    def Equals(self, obj: System.Object, ) -> System.Boolean:
        ...

    @typing.overload
    def Equals(self, value: System.String, ) -> System.Boolean:
        ...

    @typing.overload
    def Equals(self, value: System.String, comparisonType: System.StringComparison, ) -> System.Boolean:
        ...

    @typing.overload
    @staticmethod
    def Equals(a: System.String, b: System.String, ) -> System.Boolean:
        ...

    @typing.overload
    @staticmethod
    def Equals(a: System.String, b: System.String, comparisonType: System.StringComparison, ) -> System.Boolean:
        ...

    @typing.overload
    def GetHashCode(self, ) -> System.Int32:
        ...

    @typing.overload
    def GetHashCode(self, comparisonType: System.StringComparison, ) -> System.Int32:
        ...

    @typing.overload
    @staticmethod
    def GetHashCode(value: System.ReadOnlySpan[System.Char], ) -> System.Int32:
        ...

    @typing.overload
    @staticmethod
    def GetHashCode(value: System.ReadOnlySpan[System.Char], comparisonType: System.StringComparison, ) -> System.Int32:
        ...

    @typing.overload
    def StartsWith(self, value: System.String, ) -> System.Boolean:
        ...

    @typing.overload
    def StartsWith(self, value: System.String, comparisonType: System.StringComparison, ) -> System.Boolean:
        ...

    @typing.overload
    def StartsWith(self, value: System.String, ignoreCase: System.Boolean, culture: System.Globalization.CultureInfo, ) -> System.Boolean:
        ...

    @typing.overload
    def StartsWith(self, value: System.Char, ) -> System.Boolean:
        ...

    @typing.overload
    @staticmethod
    def Create(length: System.Int32, state: TState, action: System.Buffers.SpanAction[System.Char, TState], ) -> System.String:
        ...

    @typing.overload
    @staticmethod
    def Create(provider: System.IFormatProvider, handler: ref[System.Runtime.CompilerServices.DefaultInterpolatedStringHandler], ) -> System.String:
        ...

    @typing.overload
    @staticmethod
    def Create(provider: System.IFormatProvider, initialBuffer: System.Span[System.Char], handler: ref[System.Runtime.CompilerServices.DefaultInterpolatedStringHandler], ) -> System.String:
        ...

    @typing.overload
    def Clone(self, ) -> System.Object:
        ...

    @typing.overload
    @staticmethod
    def Copy(str: System.String, ) -> System.String:
        ...

    @typing.overload
    def CopyTo(self, sourceIndex: System.Int32, destination: list[System.Char], destinationIndex: System.Int32, count: System.Int32, ) -> None:
        ...

    @typing.overload
    def CopyTo(self, destination: System.Span[System.Char], ) -> None:
        ...

    @typing.overload
    def TryCopyTo(self, destination: System.Span[System.Char], ) -> System.Boolean:
        ...

    @typing.overload
    def ToCharArray(self, ) -> list[System.Char]:
        ...

    @typing.overload
    def ToCharArray(self, startIndex: System.Int32, length: System.Int32, ) -> list[System.Char]:
        ...

class Int32(System.IComparable, System.IConvertible, System.ISpanFormattable, System.IFormattable, System.IComparable[System.Int32], System.IEquatable[System.Int32], System.IBinaryInteger[System.Int32], System.IBinaryNumber[System.Int32], System.IBitwiseOperators[System.Int32, System.Int32, System.Int32], System.INumber[System.Int32], System.IAdditionOperators[System.Int32, System.Int32, System.Int32], System.IAdditiveIdentity[System.Int32, System.Int32], System.IComparisonOperators[System.Int32, System.Int32], System.IEqualityOperators[System.Int32, System.Int32], System.IDecrementOperators[System.Int32], System.IDivisionOperators[System.Int32, System.Int32, System.Int32], System.IIncrementOperators[System.Int32], System.IModulusOperators[System.Int32, System.Int32, System.Int32], System.IMultiplicativeIdentity[System.Int32, System.Int32], System.IMultiplyOperators[System.Int32, System.Int32, System.Int32], System.ISpanParseable[System.Int32], System.IParseable[System.Int32], System.ISubtractionOperators[System.Int32, System.Int32, System.Int32], System.IUnaryNegationOperators[System.Int32, System.Int32], System.IUnaryPlusOperators[System.Int32, System.Int32], System.IShiftOperators[System.Int32, System.Int32], System.IMinMaxValue[System.Int32], System.ISignedNumber[System.Int32], System.ValueType):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    # methods
    @typing.overload
    def CompareTo(self, value: System.Object, ) -> System.Int32:
        ...

    @typing.overload
    def CompareTo(self, value: System.Int32, ) -> System.Int32:
        ...

    @typing.overload
    def Equals(self, obj: System.Object, ) -> System.Boolean:
        ...

    @typing.overload
    def Equals(self, obj: System.Int32, ) -> System.Boolean:
        ...

    @typing.overload
    def GetHashCode(self, ) -> System.Int32:
        ...

    @typing.overload
    def ToString(self, ) -> System.String:
        ...

    @typing.overload
    def ToString(self, format: System.String, ) -> System.String:
        ...

    @typing.overload
    def ToString(self, provider: System.IFormatProvider, ) -> System.String:
        ...

    @typing.overload
    def ToString(self, format: System.String, provider: System.IFormatProvider, ) -> System.String:
        ...

    @typing.overload
    def TryFormat(self, destination: System.Span[System.Char], charsWritten: ref[System.Int32], format: System.ReadOnlySpan[System.Char], provider: System.IFormatProvider, ) -> System.Boolean:
        ...

    @typing.overload
    @staticmethod
    def Parse(s: System.String, ) -> System.Int32:
        ...

    @typing.overload
    @staticmethod
    def Parse(s: System.String, style: System.Globalization.NumberStyles, ) -> System.Int32:
        ...

    @typing.overload
    @staticmethod
    def Parse(s: System.String, provider: System.IFormatProvider, ) -> System.Int32:
        ...

    @typing.overload
    @staticmethod
    def Parse(s: System.String, style: System.Globalization.NumberStyles, provider: System.IFormatProvider, ) -> System.Int32:
        ...

    @typing.overload
    @staticmethod
    def Parse(s: System.ReadOnlySpan[System.Char], style: System.Globalization.NumberStyles, provider: System.IFormatProvider, ) -> System.Int32:
        ...

    @typing.overload
    @staticmethod
    def TryParse(s: System.String, result: ref[System.Int32], ) -> System.Boolean:
        ...

    @typing.overload
    @staticmethod
    def TryParse(s: System.ReadOnlySpan[System.Char], result: ref[System.Int32], ) -> System.Boolean:
        ...

    @typing.overload
    @staticmethod
    def TryParse(s: System.String, style: System.Globalization.NumberStyles, provider: System.IFormatProvider, result: ref[System.Int32], ) -> System.Boolean:
        ...

    @typing.overload
    @staticmethod
    def TryParse(s: System.ReadOnlySpan[System.Char], style: System.Globalization.NumberStyles, provider: System.IFormatProvider, result: ref[System.Int32], ) -> System.Boolean:
        ...

    @typing.overload
    def GetTypeCode(self, ) -> System.TypeCode:
        ...

class Int64(System.IComparable, System.IConvertible, System.ISpanFormattable, System.IFormattable, System.IComparable[System.Int64], System.IEquatable[System.Int64], System.IBinaryInteger[System.Int64], System.IBinaryNumber[System.Int64], System.IBitwiseOperators[System.Int64, System.Int64, System.Int64], System.INumber[System.Int64], System.IAdditionOperators[System.Int64, System.Int64, System.Int64], System.IAdditiveIdentity[System.Int64, System.Int64], System.IComparisonOperators[System.Int64, System.Int64], System.IEqualityOperators[System.Int64, System.Int64], System.IDecrementOperators[System.Int64], System.IDivisionOperators[System.Int64, System.Int64, System.Int64], System.IIncrementOperators[System.Int64], System.IModulusOperators[System.Int64, System.Int64, System.Int64], System.IMultiplicativeIdentity[System.Int64, System.Int64], System.IMultiplyOperators[System.Int64, System.Int64, System.Int64], System.ISpanParseable[System.Int64], System.IParseable[System.Int64], System.ISubtractionOperators[System.Int64, System.Int64, System.Int64], System.IUnaryNegationOperators[System.Int64, System.Int64], System.IUnaryPlusOperators[System.Int64, System.Int64], System.IShiftOperators[System.Int64, System.Int64], System.IMinMaxValue[System.Int64], System.ISignedNumber[System.Int64], System.ValueType):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    # methods
    @typing.overload
    def CompareTo(self, value: System.Object, ) -> System.Int32:
        ...

    @typing.overload
    def CompareTo(self, value: System.Int64, ) -> System.Int32:
        ...

    @typing.overload
    def Equals(self, obj: System.Object, ) -> System.Boolean:
        ...

    @typing.overload
    def Equals(self, obj: System.Int64, ) -> System.Boolean:
        ...

    @typing.overload
    def GetHashCode(self, ) -> System.Int32:
        ...

    @typing.overload
    def ToString(self, ) -> System.String:
        ...

    @typing.overload
    def ToString(self, provider: System.IFormatProvider, ) -> System.String:
        ...

    @typing.overload
    def ToString(self, format: System.String, ) -> System.String:
        ...

    @typing.overload
    def ToString(self, format: System.String, provider: System.IFormatProvider, ) -> System.String:
        ...

    @typing.overload
    def TryFormat(self, destination: System.Span[System.Char], charsWritten: ref[System.Int32], format: System.ReadOnlySpan[System.Char], provider: System.IFormatProvider, ) -> System.Boolean:
        ...

    @typing.overload
    @staticmethod
    def Parse(s: System.String, ) -> System.Int64:
        ...

    @typing.overload
    @staticmethod
    def Parse(s: System.String, style: System.Globalization.NumberStyles, ) -> System.Int64:
        ...

    @typing.overload
    @staticmethod
    def Parse(s: System.String, provider: System.IFormatProvider, ) -> System.Int64:
        ...

    @typing.overload
    @staticmethod
    def Parse(s: System.String, style: System.Globalization.NumberStyles, provider: System.IFormatProvider, ) -> System.Int64:
        ...

    @typing.overload
    @staticmethod
    def Parse(s: System.ReadOnlySpan[System.Char], style: System.Globalization.NumberStyles, provider: System.IFormatProvider, ) -> System.Int64:
        ...

    @typing.overload
    @staticmethod
    def TryParse(s: System.String, result: ref[System.Int64], ) -> System.Boolean:
        ...

    @typing.overload
    @staticmethod
    def TryParse(s: System.ReadOnlySpan[System.Char], result: ref[System.Int64], ) -> System.Boolean:
        ...

    @typing.overload
    @staticmethod
    def TryParse(s: System.String, style: System.Globalization.NumberStyles, provider: System.IFormatProvider, result: ref[System.Int64], ) -> System.Boolean:
        ...

    @typing.overload
    @staticmethod
    def TryParse(s: System.ReadOnlySpan[System.Char], style: System.Globalization.NumberStyles, provider: System.IFormatProvider, result: ref[System.Int64], ) -> System.Boolean:
        ...

    @typing.overload
    def GetTypeCode(self, ) -> System.TypeCode:
        ...

class Decimal(System.ISpanFormattable, System.IFormattable, System.IComparable, System.IConvertible, System.IComparable[System.Decimal], System.IEquatable[System.Decimal], System.Runtime.Serialization.ISerializable, System.Runtime.Serialization.IDeserializationCallback, System.IMinMaxValue[System.Decimal], System.ISignedNumber[System.Decimal], System.INumber[System.Decimal], System.IAdditionOperators[System.Decimal, System.Decimal, System.Decimal], System.IAdditiveIdentity[System.Decimal, System.Decimal], System.IComparisonOperators[System.Decimal, System.Decimal], System.IEqualityOperators[System.Decimal, System.Decimal], System.IDecrementOperators[System.Decimal], System.IDivisionOperators[System.Decimal, System.Decimal, System.Decimal], System.IIncrementOperators[System.Decimal], System.IModulusOperators[System.Decimal, System.Decimal, System.Decimal], System.IMultiplicativeIdentity[System.Decimal, System.Decimal], System.IMultiplyOperators[System.Decimal, System.Decimal, System.Decimal], System.ISpanParseable[System.Decimal], System.IParseable[System.Decimal], System.ISubtractionOperators[System.Decimal, System.Decimal, System.Decimal], System.IUnaryNegationOperators[System.Decimal, System.Decimal], System.IUnaryPlusOperators[System.Decimal, System.Decimal], System.ValueType):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    # methods
    @typing.overload
    def __init__(self, value: System.Int32, ):
        ...

    @typing.overload
    def __init__(self, value: System.UInt32, ):
        ...

    @typing.overload
    def __init__(self, value: System.Int64, ):
        ...

    @typing.overload
    def __init__(self, value: System.UInt64, ):
        ...

    @typing.overload
    def __init__(self, value: System.Single, ):
        ...

    @typing.overload
    def __init__(self, value: System.Double, ):
        ...

    @typing.overload
    def __init__(self, bits: list[System.Int32], ):
        ...

    @typing.overload
    def __init__(self, bits: System.ReadOnlySpan[System.Int32], ):
        ...

    @typing.overload
    def __init__(self, lo: System.Int32, mid: System.Int32, hi: System.Int32, isNegative: System.Boolean, scale: System.Byte, ):
        ...

    @typing.overload
    def GetTypeCode(self, ) -> System.TypeCode:
        ...

    @typing.overload
    @staticmethod
    def FromOACurrency(cy: System.Int64, ) -> System.Decimal:
        ...

    @typing.overload
    @staticmethod
    def ToOACurrency(value: System.Decimal, ) -> System.Int64:
        ...

    @typing.overload
    @staticmethod
    def Add(d1: System.Decimal, d2: System.Decimal, ) -> System.Decimal:
        ...

    @typing.overload
    @staticmethod
    def Ceiling(d: System.Decimal, ) -> System.Decimal:
        ...

    @typing.overload
    @staticmethod
    def Compare(d1: System.Decimal, d2: System.Decimal, ) -> System.Int32:
        ...

    @typing.overload
    def CompareTo(self, value: System.Object, ) -> System.Int32:
        ...

    @typing.overload
    def CompareTo(self, value: System.Decimal, ) -> System.Int32:
        ...

    @typing.overload
    @staticmethod
    def Divide(d1: System.Decimal, d2: System.Decimal, ) -> System.Decimal:
        ...

    @typing.overload
    def Equals(self, value: System.Object, ) -> System.Boolean:
        ...

    @typing.overload
    def Equals(self, value: System.Decimal, ) -> System.Boolean:
        ...

    @typing.overload
    def GetHashCode(self, ) -> System.Int32:
        ...

    @typing.overload
    @staticmethod
    def Equals(d1: System.Decimal, d2: System.Decimal, ) -> System.Boolean:
        ...

    @typing.overload
    @staticmethod
    def Floor(d: System.Decimal, ) -> System.Decimal:
        ...

    @typing.overload
    def ToString(self, ) -> System.String:
        ...

    @typing.overload
    def ToString(self, format: System.String, ) -> System.String:
        ...

    @typing.overload
    def ToString(self, provider: System.IFormatProvider, ) -> System.String:
        ...

    @typing.overload
    def ToString(self, format: System.String, provider: System.IFormatProvider, ) -> System.String:
        ...

    @typing.overload
    def TryFormat(self, destination: System.Span[System.Char], charsWritten: ref[System.Int32], format: System.ReadOnlySpan[System.Char], provider: System.IFormatProvider, ) -> System.Boolean:
        ...

    @typing.overload
    @staticmethod
    def Parse(s: System.String, ) -> System.Decimal:
        ...

    @typing.overload
    @staticmethod
    def Parse(s: System.String, style: System.Globalization.NumberStyles, ) -> System.Decimal:
        ...

    @typing.overload
    @staticmethod
    def Parse(s: System.String, provider: System.IFormatProvider, ) -> System.Decimal:
        ...

    @typing.overload
    @staticmethod
    def Parse(s: System.String, style: System.Globalization.NumberStyles, provider: System.IFormatProvider, ) -> System.Decimal:
        ...

    @typing.overload
    @staticmethod
    def Parse(s: System.ReadOnlySpan[System.Char], style: System.Globalization.NumberStyles, provider: System.IFormatProvider, ) -> System.Decimal:
        ...

    @typing.overload
    @staticmethod
    def TryParse(s: System.String, result: ref[System.Decimal], ) -> System.Boolean:
        ...

    @typing.overload
    @staticmethod
    def TryParse(s: System.ReadOnlySpan[System.Char], result: ref[System.Decimal], ) -> System.Boolean:
        ...

    @typing.overload
    @staticmethod
    def TryParse(s: System.String, style: System.Globalization.NumberStyles, provider: System.IFormatProvider, result: ref[System.Decimal], ) -> System.Boolean:
        ...

    @typing.overload
    @staticmethod
    def TryParse(s: System.ReadOnlySpan[System.Char], style: System.Globalization.NumberStyles, provider: System.IFormatProvider, result: ref[System.Decimal], ) -> System.Boolean:
        ...

    @typing.overload
    @staticmethod
    def GetBits(d: System.Decimal, ) -> list[System.Int32]:
        ...

    @typing.overload
    @staticmethod
    def GetBits(d: System.Decimal, destination: System.Span[System.Int32], ) -> System.Int32:
        ...

    @typing.overload
    @staticmethod
    def TryGetBits(d: System.Decimal, destination: System.Span[System.Int32], valuesWritten: ref[System.Int32], ) -> System.Boolean:
        ...

    @typing.overload
    @staticmethod
    def Remainder(d1: System.Decimal, d2: System.Decimal, ) -> System.Decimal:
        ...

    @typing.overload
    @staticmethod
    def Multiply(d1: System.Decimal, d2: System.Decimal, ) -> System.Decimal:
        ...

    @typing.overload
    @staticmethod
    def Negate(d: System.Decimal, ) -> System.Decimal:
        ...

    @typing.overload
    @staticmethod
    def Round(d: System.Decimal, ) -> System.Decimal:
        ...

    @typing.overload
    @staticmethod
    def Round(d: System.Decimal, decimals: System.Int32, ) -> System.Decimal:
        ...

    @typing.overload
    @staticmethod
    def Round(d: System.Decimal, mode: System.MidpointRounding, ) -> System.Decimal:
        ...

    @typing.overload
    @staticmethod
    def Round(d: System.Decimal, decimals: System.Int32, mode: System.MidpointRounding, ) -> System.Decimal:
        ...

    @typing.overload
    @staticmethod
    def Subtract(d1: System.Decimal, d2: System.Decimal, ) -> System.Decimal:
        ...

    @typing.overload
    @staticmethod
    def ToByte(value: System.Decimal, ) -> System.Byte:
        ...

    @typing.overload
    @staticmethod
    def ToSByte(value: System.Decimal, ) -> System.SByte:
        ...

    @typing.overload
    @staticmethod
    def ToInt16(value: System.Decimal, ) -> System.Int16:
        ...

    @typing.overload
    @staticmethod
    def ToDouble(d: System.Decimal, ) -> System.Double:
        ...

    @typing.overload
    @staticmethod
    def ToInt32(d: System.Decimal, ) -> System.Int32:
        ...

    @typing.overload
    @staticmethod
    def ToInt64(d: System.Decimal, ) -> System.Int64:
        ...

    @typing.overload
    @staticmethod
    def ToUInt16(value: System.Decimal, ) -> System.UInt16:
        ...

    @typing.overload
    @staticmethod
    def ToUInt32(d: System.Decimal, ) -> System.UInt32:
        ...

    @typing.overload
    @staticmethod
    def ToUInt64(d: System.Decimal, ) -> System.UInt64:
        ...

    @typing.overload
    @staticmethod
    def ToSingle(d: System.Decimal, ) -> System.Single:
        ...

    @typing.overload
    @staticmethod
    def Truncate(d: System.Decimal, ) -> System.Decimal:
        ...

class Boolean(System.IComparable, System.IConvertible, System.IComparable[System.Boolean], System.IEquatable[System.Boolean], System.ValueType):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    # methods
    @typing.overload
    def GetHashCode(self, ) -> System.Int32:
        ...

    @typing.overload
    def ToString(self, ) -> System.String:
        ...

    @typing.overload
    def ToString(self, provider: System.IFormatProvider, ) -> System.String:
        ...

    @typing.overload
    def TryFormat(self, destination: System.Span[System.Char], charsWritten: ref[System.Int32], ) -> System.Boolean:
        ...

    @typing.overload
    def Equals(self, obj: System.Object, ) -> System.Boolean:
        ...

    @typing.overload
    def Equals(self, obj: System.Boolean, ) -> System.Boolean:
        ...

    @typing.overload
    def CompareTo(self, obj: System.Object, ) -> System.Int32:
        ...

    @typing.overload
    def CompareTo(self, value: System.Boolean, ) -> System.Int32:
        ...

    @typing.overload
    @staticmethod
    def Parse(value: System.String, ) -> System.Boolean:
        ...

    @typing.overload
    @staticmethod
    def Parse(value: System.ReadOnlySpan[System.Char], ) -> System.Boolean:
        ...

    @typing.overload
    @staticmethod
    def TryParse(value: System.String, result: ref[System.Boolean], ) -> System.Boolean:
        ...

    @typing.overload
    @staticmethod
    def TryParse(value: System.ReadOnlySpan[System.Char], result: ref[System.Boolean], ) -> System.Boolean:
        ...

    @typing.overload
    def GetTypeCode(self, ) -> System.TypeCode:
        ...

class Random(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def Shared(self) -> System.Random:
        ...

    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def __init__(self, Seed: System.Int32, ):
        ...

    @typing.overload
    def Next(self, ) -> System.Int32:
        ...

    @typing.overload
    def Next(self, maxValue: System.Int32, ) -> System.Int32:
        ...

    @typing.overload
    def Next(self, minValue: System.Int32, maxValue: System.Int32, ) -> System.Int32:
        ...

    @typing.overload
    def NextInt64(self, ) -> System.Int64:
        ...

    @typing.overload
    def NextInt64(self, maxValue: System.Int64, ) -> System.Int64:
        ...

    @typing.overload
    def NextInt64(self, minValue: System.Int64, maxValue: System.Int64, ) -> System.Int64:
        ...

    @typing.overload
    def NextSingle(self, ) -> System.Single:
        ...

    @typing.overload
    def NextDouble(self, ) -> System.Double:
        ...

    @typing.overload
    def NextBytes(self, buffer: list[System.Byte], ) -> None:
        ...

    @typing.overload
    def NextBytes(self, buffer: System.Span[System.Byte], ) -> None:
        ...

class IComparable(abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    # methods
    @typing.overload
    @abc.abstractmethod
    def CompareTo(self, obj: System.Object, ) -> System.Int32:
        ...

class IFormattable(abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    # methods
    @typing.overload
    @abc.abstractmethod
    def ToString(self, format: System.String, formatProvider: System.IFormatProvider, ) -> System.String:
        ...

class IConvertible(abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    # methods
    @typing.overload
    @abc.abstractmethod
    def GetTypeCode(self, ) -> System.TypeCode:
        ...

    @typing.overload
    @abc.abstractmethod
    def ToBoolean(self, provider: System.IFormatProvider, ) -> System.Boolean:
        ...

    @typing.overload
    @abc.abstractmethod
    def ToChar(self, provider: System.IFormatProvider, ) -> System.Char:
        ...

    @typing.overload
    @abc.abstractmethod
    def ToSByte(self, provider: System.IFormatProvider, ) -> System.SByte:
        ...

    @typing.overload
    @abc.abstractmethod
    def ToByte(self, provider: System.IFormatProvider, ) -> System.Byte:
        ...

    @typing.overload
    @abc.abstractmethod
    def ToInt16(self, provider: System.IFormatProvider, ) -> System.Int16:
        ...

    @typing.overload
    @abc.abstractmethod
    def ToUInt16(self, provider: System.IFormatProvider, ) -> System.UInt16:
        ...

    @typing.overload
    @abc.abstractmethod
    def ToInt32(self, provider: System.IFormatProvider, ) -> System.Int32:
        ...

    @typing.overload
    @abc.abstractmethod
    def ToUInt32(self, provider: System.IFormatProvider, ) -> System.UInt32:
        ...

    @typing.overload
    @abc.abstractmethod
    def ToInt64(self, provider: System.IFormatProvider, ) -> System.Int64:
        ...

    @typing.overload
    @abc.abstractmethod
    def ToUInt64(self, provider: System.IFormatProvider, ) -> System.UInt64:
        ...

    @typing.overload
    @abc.abstractmethod
    def ToSingle(self, provider: System.IFormatProvider, ) -> System.Single:
        ...

    @typing.overload
    @abc.abstractmethod
    def ToDouble(self, provider: System.IFormatProvider, ) -> System.Double:
        ...

    @typing.overload
    @abc.abstractmethod
    def ToDecimal(self, provider: System.IFormatProvider, ) -> System.Decimal:
        ...

    @typing.overload
    @abc.abstractmethod
    def ToDateTime(self, provider: System.IFormatProvider, ) -> System.DateTime:
        ...

    @typing.overload
    @abc.abstractmethod
    def ToString(self, provider: System.IFormatProvider, ) -> System.String:
        ...

    @typing.overload
    @abc.abstractmethod
    def ToType(self, conversionType: System.Type, provider: System.IFormatProvider, ) -> System.Object:
        ...

class Enum(System.IComparable, System.IFormattable, System.IConvertible, System.ValueType, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    # methods
    @typing.overload
    @staticmethod
    def ToObject(enumType: System.Type, value: System.SByte, ) -> System.Object:
        ...

    @typing.overload
    @staticmethod
    def ToObject(enumType: System.Type, value: System.Int16, ) -> System.Object:
        ...

    @typing.overload
    @staticmethod
    def ToObject(enumType: System.Type, value: System.Int32, ) -> System.Object:
        ...

    @typing.overload
    @staticmethod
    def ToObject(enumType: System.Type, value: System.Byte, ) -> System.Object:
        ...

    @typing.overload
    @staticmethod
    def ToObject(enumType: System.Type, value: System.UInt16, ) -> System.Object:
        ...

    @typing.overload
    @staticmethod
    def ToObject(enumType: System.Type, value: System.UInt32, ) -> System.Object:
        ...

    @typing.overload
    @staticmethod
    def ToObject(enumType: System.Type, value: System.Int64, ) -> System.Object:
        ...

    @typing.overload
    @staticmethod
    def ToObject(enumType: System.Type, value: System.UInt64, ) -> System.Object:
        ...

    @typing.overload
    def Equals(self, obj: System.Object, ) -> System.Boolean:
        ...

    @typing.overload
    @staticmethod
    def GetName(value: TEnum, ) -> System.String:
        ...

    @typing.overload
    @staticmethod
    def GetName(enumType: System.Type, value: System.Object, ) -> System.String:
        ...

    @typing.overload
    @staticmethod
    def GetNames() -> list[System.String]:
        ...

    @typing.overload
    @staticmethod
    def GetNames(enumType: System.Type, ) -> list[System.String]:
        ...

    @typing.overload
    @staticmethod
    def GetUnderlyingType(enumType: System.Type, ) -> System.Type:
        ...

    @typing.overload
    @staticmethod
    def GetValues() -> list[TEnum]:
        ...

    @typing.overload
    @staticmethod
    def GetValues(enumType: System.Type, ) -> System.Array:
        ...

    @typing.overload
    def HasFlag(self, flag: System.Enum, ) -> System.Boolean:
        ...

    @typing.overload
    @staticmethod
    def IsDefined(value: TEnum, ) -> System.Boolean:
        ...

    @typing.overload
    @staticmethod
    def IsDefined(enumType: System.Type, value: System.Object, ) -> System.Boolean:
        ...

    @typing.overload
    @staticmethod
    def Parse(enumType: System.Type, value: System.String, ) -> System.Object:
        ...

    @typing.overload
    @staticmethod
    def Parse(enumType: System.Type, value: System.ReadOnlySpan[System.Char], ) -> System.Object:
        ...

    @typing.overload
    @staticmethod
    def Parse(enumType: System.Type, value: System.String, ignoreCase: System.Boolean, ) -> System.Object:
        ...

    @typing.overload
    @staticmethod
    def Parse(enumType: System.Type, value: System.ReadOnlySpan[System.Char], ignoreCase: System.Boolean, ) -> System.Object:
        ...

    @typing.overload
    @staticmethod
    def Parse(value: System.String, ) -> TEnum:
        ...

    @typing.overload
    @staticmethod
    def Parse(value: System.ReadOnlySpan[System.Char], ) -> TEnum:
        ...

    @typing.overload
    @staticmethod
    def Parse(value: System.String, ignoreCase: System.Boolean, ) -> TEnum:
        ...

    @typing.overload
    @staticmethod
    def Parse(value: System.ReadOnlySpan[System.Char], ignoreCase: System.Boolean, ) -> TEnum:
        ...

    @typing.overload
    @staticmethod
    def TryParse(enumType: System.Type, value: System.String, result: ref[System.Object], ) -> System.Boolean:
        ...

    @typing.overload
    @staticmethod
    def TryParse(enumType: System.Type, value: System.ReadOnlySpan[System.Char], result: ref[System.Object], ) -> System.Boolean:
        ...

    @typing.overload
    @staticmethod
    def TryParse(enumType: System.Type, value: System.String, ignoreCase: System.Boolean, result: ref[System.Object], ) -> System.Boolean:
        ...

    @typing.overload
    @staticmethod
    def TryParse(enumType: System.Type, value: System.ReadOnlySpan[System.Char], ignoreCase: System.Boolean, result: ref[System.Object], ) -> System.Boolean:
        ...

    @typing.overload
    @staticmethod
    def TryParse(value: System.String, result: ref[TEnum], ) -> System.Boolean:
        ...

    @typing.overload
    @staticmethod
    def TryParse(value: System.ReadOnlySpan[System.Char], result: ref[TEnum], ) -> System.Boolean:
        ...

    @typing.overload
    @staticmethod
    def TryParse(value: System.String, ignoreCase: System.Boolean, result: ref[TEnum], ) -> System.Boolean:
        ...

    @typing.overload
    @staticmethod
    def TryParse(value: System.ReadOnlySpan[System.Char], ignoreCase: System.Boolean, result: ref[TEnum], ) -> System.Boolean:
        ...

    @typing.overload
    @staticmethod
    def ToObject(enumType: System.Type, value: System.Object, ) -> System.Object:
        ...

    @typing.overload
    @staticmethod
    def Format(enumType: System.Type, value: System.Object, format: System.String, ) -> System.String:
        ...

    @typing.overload
    def GetHashCode(self, ) -> System.Int32:
        ...

    @typing.overload
    def ToString(self, ) -> System.String:
        ...

    @typing.overload
    def CompareTo(self, target: System.Object, ) -> System.Int32:
        ...

    @typing.overload
    def ToString(self, format: System.String, provider: System.IFormatProvider, ) -> System.String:
        ...

    @typing.overload
    def ToString(self, format: System.String, ) -> System.String:
        ...

    @typing.overload
    def ToString(self, provider: System.IFormatProvider, ) -> System.String:
        ...

    @typing.overload
    def GetTypeCode(self, ) -> System.TypeCode:
        ...

class ValueTuple(System.IEquatable[System.ValueTuple], System.Collections.IStructuralEquatable, System.Collections.IStructuralComparable, System.IComparable, System.IComparable[System.ValueTuple], System.IValueTupleInternal, System.Runtime.CompilerServices.ITuple, System.ValueType, typing.Generic[T1, T2]):
    @typing.overload
    def __init__(self, **kwargs):
        self.Item1: T1
        self.Item2: T2
        ...

    # properties
    # methods
    @typing.overload
    def __init__(self, item1: T1, item2: T2, ):
        ...

    @typing.overload
    def Equals(self, obj: System.Object, ) -> System.Boolean:
        ...

    @typing.overload
    def Equals(self, other: System.ValueTuple, ) -> System.Boolean:
        ...

    @typing.overload
    def CompareTo(self, other: System.ValueTuple, ) -> System.Int32:
        ...

    @typing.overload
    def GetHashCode(self, ) -> System.Int32:
        ...

    @typing.overload
    def ToString(self, ) -> System.String:
        ...

class IDisposable(abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    # methods
    @typing.overload
    @abc.abstractmethod
    def Dispose(self, ) -> None:
        ...

class ValueType(System.Object, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    # methods
    @typing.overload
    def ToString(self, ) -> System.String:
        ...

    @typing.overload
    def Equals(self, obj: System.Object, ) -> System.Boolean:
        ...

    @typing.overload
    def GetHashCode(self, ) -> System.Int32:
        ...

class Nullable(System.ValueType, typing.Generic[T]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def HasValue(self) -> System.Boolean:
        ...

    @property
    def Value(self) -> T:
        ...

    # methods
    @typing.overload
    def __init__(self, value: T, ):
        ...

    @typing.overload
    def GetValueOrDefault(self, ) -> T:
        ...

    @typing.overload
    def GetValueOrDefault(self, defaultValue: T, ) -> T:
        ...

    @typing.overload
    def Equals(self, other: System.Object, ) -> System.Boolean:
        ...

    @typing.overload
    def GetHashCode(self, ) -> System.Int32:
        ...

    @typing.overload
    def ToString(self, ) -> System.String:
        ...

class ValueTuple(System.IEquatable[System.ValueTuple], System.Collections.IStructuralEquatable, System.Collections.IStructuralComparable, System.IComparable, System.IComparable[System.ValueTuple], System.IValueTupleInternal, System.Runtime.CompilerServices.ITuple, System.ValueType, typing.Generic[T1, T2, T3]):
    @typing.overload
    def __init__(self, **kwargs):
        self.Item1: T1
        self.Item2: T2
        self.Item3: T3
        ...

    # properties
    # methods
    @typing.overload
    def __init__(self, item1: T1, item2: T2, item3: T3, ):
        ...

    @typing.overload
    def Equals(self, obj: System.Object, ) -> System.Boolean:
        ...

    @typing.overload
    def Equals(self, other: System.ValueTuple, ) -> System.Boolean:
        ...

    @typing.overload
    def CompareTo(self, other: System.ValueTuple, ) -> System.Int32:
        ...

    @typing.overload
    def GetHashCode(self, ) -> System.Int32:
        ...

    @typing.overload
    def ToString(self, ) -> System.String:
        ...

class Attribute(System.Object, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def TypeId(self) -> System.Object:
        ...

    # methods
    @typing.overload
    @staticmethod
    def GetCustomAttributes(element: System.Reflection.MemberInfo, attributeType: System.Type, ) -> list[System.Attribute]:
        ...

    @typing.overload
    @staticmethod
    def GetCustomAttributes(element: System.Reflection.MemberInfo, attributeType: System.Type, inherit: System.Boolean, ) -> list[System.Attribute]:
        ...

    @typing.overload
    @staticmethod
    def GetCustomAttributes(element: System.Reflection.MemberInfo, ) -> list[System.Attribute]:
        ...

    @typing.overload
    @staticmethod
    def GetCustomAttributes(element: System.Reflection.MemberInfo, inherit: System.Boolean, ) -> list[System.Attribute]:
        ...

    @typing.overload
    @staticmethod
    def IsDefined(element: System.Reflection.MemberInfo, attributeType: System.Type, ) -> System.Boolean:
        ...

    @typing.overload
    @staticmethod
    def IsDefined(element: System.Reflection.MemberInfo, attributeType: System.Type, inherit: System.Boolean, ) -> System.Boolean:
        ...

    @typing.overload
    @staticmethod
    def GetCustomAttribute(element: System.Reflection.MemberInfo, attributeType: System.Type, ) -> System.Attribute:
        ...

    @typing.overload
    @staticmethod
    def GetCustomAttribute(element: System.Reflection.MemberInfo, attributeType: System.Type, inherit: System.Boolean, ) -> System.Attribute:
        ...

    @typing.overload
    @staticmethod
    def GetCustomAttributes(element: System.Reflection.ParameterInfo, ) -> list[System.Attribute]:
        ...

    @typing.overload
    @staticmethod
    def GetCustomAttributes(element: System.Reflection.ParameterInfo, attributeType: System.Type, ) -> list[System.Attribute]:
        ...

    @typing.overload
    @staticmethod
    def GetCustomAttributes(element: System.Reflection.ParameterInfo, attributeType: System.Type, inherit: System.Boolean, ) -> list[System.Attribute]:
        ...

    @typing.overload
    @staticmethod
    def GetCustomAttributes(element: System.Reflection.ParameterInfo, inherit: System.Boolean, ) -> list[System.Attribute]:
        ...

    @typing.overload
    @staticmethod
    def IsDefined(element: System.Reflection.ParameterInfo, attributeType: System.Type, ) -> System.Boolean:
        ...

    @typing.overload
    @staticmethod
    def IsDefined(element: System.Reflection.ParameterInfo, attributeType: System.Type, inherit: System.Boolean, ) -> System.Boolean:
        ...

    @typing.overload
    @staticmethod
    def GetCustomAttribute(element: System.Reflection.ParameterInfo, attributeType: System.Type, ) -> System.Attribute:
        ...

    @typing.overload
    @staticmethod
    def GetCustomAttribute(element: System.Reflection.ParameterInfo, attributeType: System.Type, inherit: System.Boolean, ) -> System.Attribute:
        ...

    @typing.overload
    @staticmethod
    def GetCustomAttributes(element: System.Reflection.Module, attributeType: System.Type, ) -> list[System.Attribute]:
        ...

    @typing.overload
    @staticmethod
    def GetCustomAttributes(element: System.Reflection.Module, ) -> list[System.Attribute]:
        ...

    @typing.overload
    @staticmethod
    def GetCustomAttributes(element: System.Reflection.Module, inherit: System.Boolean, ) -> list[System.Attribute]:
        ...

    @typing.overload
    @staticmethod
    def GetCustomAttributes(element: System.Reflection.Module, attributeType: System.Type, inherit: System.Boolean, ) -> list[System.Attribute]:
        ...

    @typing.overload
    @staticmethod
    def IsDefined(element: System.Reflection.Module, attributeType: System.Type, ) -> System.Boolean:
        ...

    @typing.overload
    @staticmethod
    def IsDefined(element: System.Reflection.Module, attributeType: System.Type, inherit: System.Boolean, ) -> System.Boolean:
        ...

    @typing.overload
    @staticmethod
    def GetCustomAttribute(element: System.Reflection.Module, attributeType: System.Type, ) -> System.Attribute:
        ...

    @typing.overload
    @staticmethod
    def GetCustomAttribute(element: System.Reflection.Module, attributeType: System.Type, inherit: System.Boolean, ) -> System.Attribute:
        ...

    @typing.overload
    @staticmethod
    def GetCustomAttributes(element: System.Reflection.Assembly, attributeType: System.Type, ) -> list[System.Attribute]:
        ...

    @typing.overload
    @staticmethod
    def GetCustomAttributes(element: System.Reflection.Assembly, attributeType: System.Type, inherit: System.Boolean, ) -> list[System.Attribute]:
        ...

    @typing.overload
    @staticmethod
    def GetCustomAttributes(element: System.Reflection.Assembly, ) -> list[System.Attribute]:
        ...

    @typing.overload
    @staticmethod
    def GetCustomAttributes(element: System.Reflection.Assembly, inherit: System.Boolean, ) -> list[System.Attribute]:
        ...

    @typing.overload
    @staticmethod
    def IsDefined(element: System.Reflection.Assembly, attributeType: System.Type, ) -> System.Boolean:
        ...

    @typing.overload
    @staticmethod
    def IsDefined(element: System.Reflection.Assembly, attributeType: System.Type, inherit: System.Boolean, ) -> System.Boolean:
        ...

    @typing.overload
    @staticmethod
    def GetCustomAttribute(element: System.Reflection.Assembly, attributeType: System.Type, ) -> System.Attribute:
        ...

    @typing.overload
    @staticmethod
    def GetCustomAttribute(element: System.Reflection.Assembly, attributeType: System.Type, inherit: System.Boolean, ) -> System.Attribute:
        ...

    @typing.overload
    def Equals(self, obj: System.Object, ) -> System.Boolean:
        ...

    @typing.overload
    def GetHashCode(self, ) -> System.Int32:
        ...

    @typing.overload
    def Match(self, obj: System.Object, ) -> System.Boolean:
        ...

    @typing.overload
    def IsDefaultAttribute(self, ) -> System.Boolean:
        ...

class DateTime(System.IComparable, System.ISpanFormattable, System.IFormattable, System.IConvertible, System.IComparable[System.DateTime], System.IEquatable[System.DateTime], System.Runtime.Serialization.ISerializable, System.IAdditionOperators[System.DateTime, System.TimeSpan, System.DateTime], System.IAdditiveIdentity[System.DateTime, System.TimeSpan], System.IComparisonOperators[System.DateTime, System.DateTime], System.IEqualityOperators[System.DateTime, System.DateTime], System.IMinMaxValue[System.DateTime], System.ISpanParseable[System.DateTime], System.IParseable[System.DateTime], System.ISubtractionOperators[System.DateTime, System.TimeSpan, System.DateTime], System.ISubtractionOperators[System.DateTime, System.DateTime, System.TimeSpan], System.ValueType):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def Date(self) -> System.DateTime:
        ...

    @property
    def Day(self) -> System.Int32:
        ...

    @property
    def DayOfWeek(self) -> System.DayOfWeek:
        ...

    @property
    def DayOfYear(self) -> System.Int32:
        ...

    @property
    def Hour(self) -> System.Int32:
        ...

    @property
    def Kind(self) -> System.DateTimeKind:
        ...

    @property
    def Millisecond(self) -> System.Int32:
        ...

    @property
    def Minute(self) -> System.Int32:
        ...

    @property
    def Month(self) -> System.Int32:
        ...

    @property
    def Now(self) -> System.DateTime:
        ...

    @property
    def Second(self) -> System.Int32:
        ...

    @property
    def Ticks(self) -> System.Int64:
        ...

    @property
    def TimeOfDay(self) -> System.TimeSpan:
        ...

    @property
    def Today(self) -> System.DateTime:
        ...

    @property
    def Year(self) -> System.Int32:
        ...

    @property
    def UtcNow(self) -> System.DateTime:
        ...

    # methods
    @typing.overload
    def __init__(self, ticks: System.Int64, ):
        ...

    @typing.overload
    def __init__(self, ticks: System.Int64, kind: System.DateTimeKind, ):
        ...

    @typing.overload
    def __init__(self, year: System.Int32, month: System.Int32, day: System.Int32, ):
        ...

    @typing.overload
    def __init__(self, year: System.Int32, month: System.Int32, day: System.Int32, calendar: System.Globalization.Calendar, ):
        ...

    @typing.overload
    def __init__(self, year: System.Int32, month: System.Int32, day: System.Int32, hour: System.Int32, minute: System.Int32, second: System.Int32, ):
        ...

    @typing.overload
    def __init__(self, year: System.Int32, month: System.Int32, day: System.Int32, hour: System.Int32, minute: System.Int32, second: System.Int32, kind: System.DateTimeKind, ):
        ...

    @typing.overload
    def __init__(self, year: System.Int32, month: System.Int32, day: System.Int32, hour: System.Int32, minute: System.Int32, second: System.Int32, calendar: System.Globalization.Calendar, ):
        ...

    @typing.overload
    def __init__(self, year: System.Int32, month: System.Int32, day: System.Int32, hour: System.Int32, minute: System.Int32, second: System.Int32, millisecond: System.Int32, ):
        ...

    @typing.overload
    def __init__(self, year: System.Int32, month: System.Int32, day: System.Int32, hour: System.Int32, minute: System.Int32, second: System.Int32, millisecond: System.Int32, kind: System.DateTimeKind, ):
        ...

    @typing.overload
    def __init__(self, year: System.Int32, month: System.Int32, day: System.Int32, hour: System.Int32, minute: System.Int32, second: System.Int32, millisecond: System.Int32, calendar: System.Globalization.Calendar, ):
        ...

    @typing.overload
    def __init__(self, year: System.Int32, month: System.Int32, day: System.Int32, hour: System.Int32, minute: System.Int32, second: System.Int32, millisecond: System.Int32, calendar: System.Globalization.Calendar, kind: System.DateTimeKind, ):
        ...

    @typing.overload
    @staticmethod
    def Parse(s: System.ReadOnlySpan[System.Char], provider: System.IFormatProvider, styles: System.Globalization.DateTimeStyles, ) -> System.DateTime:
        ...

    @typing.overload
    @staticmethod
    def ParseExact(s: System.String, format: System.String, provider: System.IFormatProvider, ) -> System.DateTime:
        ...

    @typing.overload
    @staticmethod
    def ParseExact(s: System.String, format: System.String, provider: System.IFormatProvider, style: System.Globalization.DateTimeStyles, ) -> System.DateTime:
        ...

    @typing.overload
    @staticmethod
    def ParseExact(s: System.ReadOnlySpan[System.Char], format: System.ReadOnlySpan[System.Char], provider: System.IFormatProvider, style: System.Globalization.DateTimeStyles, ) -> System.DateTime:
        ...

    @typing.overload
    @staticmethod
    def ParseExact(s: System.String, formats: list[System.String], provider: System.IFormatProvider, style: System.Globalization.DateTimeStyles, ) -> System.DateTime:
        ...

    @typing.overload
    @staticmethod
    def ParseExact(s: System.ReadOnlySpan[System.Char], formats: list[System.String], provider: System.IFormatProvider, style: System.Globalization.DateTimeStyles, ) -> System.DateTime:
        ...

    @typing.overload
    def Subtract(self, value: System.DateTime, ) -> System.TimeSpan:
        ...

    @typing.overload
    def Subtract(self, value: System.TimeSpan, ) -> System.DateTime:
        ...

    @typing.overload
    def ToOADate(self, ) -> System.Double:
        ...

    @typing.overload
    def ToFileTime(self, ) -> System.Int64:
        ...

    @typing.overload
    def ToFileTimeUtc(self, ) -> System.Int64:
        ...

    @typing.overload
    def ToLocalTime(self, ) -> System.DateTime:
        ...

    @typing.overload
    def ToLongDateString(self, ) -> System.String:
        ...

    @typing.overload
    def ToLongTimeString(self, ) -> System.String:
        ...

    @typing.overload
    def ToShortDateString(self, ) -> System.String:
        ...

    @typing.overload
    def ToShortTimeString(self, ) -> System.String:
        ...

    @typing.overload
    def ToString(self, ) -> System.String:
        ...

    @typing.overload
    def ToString(self, format: System.String, ) -> System.String:
        ...

    @typing.overload
    def ToString(self, provider: System.IFormatProvider, ) -> System.String:
        ...

    @typing.overload
    def ToString(self, format: System.String, provider: System.IFormatProvider, ) -> System.String:
        ...

    @typing.overload
    def TryFormat(self, destination: System.Span[System.Char], charsWritten: ref[System.Int32], format: System.ReadOnlySpan[System.Char], provider: System.IFormatProvider, ) -> System.Boolean:
        ...

    @typing.overload
    def ToUniversalTime(self, ) -> System.DateTime:
        ...

    @typing.overload
    @staticmethod
    def TryParse(s: System.String, result: ref[System.DateTime], ) -> System.Boolean:
        ...

    @typing.overload
    @staticmethod
    def TryParse(s: System.ReadOnlySpan[System.Char], result: ref[System.DateTime], ) -> System.Boolean:
        ...

    @typing.overload
    @staticmethod
    def TryParse(s: System.String, provider: System.IFormatProvider, styles: System.Globalization.DateTimeStyles, result: ref[System.DateTime], ) -> System.Boolean:
        ...

    @typing.overload
    @staticmethod
    def TryParse(s: System.ReadOnlySpan[System.Char], provider: System.IFormatProvider, styles: System.Globalization.DateTimeStyles, result: ref[System.DateTime], ) -> System.Boolean:
        ...

    @typing.overload
    @staticmethod
    def TryParseExact(s: System.String, format: System.String, provider: System.IFormatProvider, style: System.Globalization.DateTimeStyles, result: ref[System.DateTime], ) -> System.Boolean:
        ...

    @typing.overload
    @staticmethod
    def TryParseExact(s: System.ReadOnlySpan[System.Char], format: System.ReadOnlySpan[System.Char], provider: System.IFormatProvider, style: System.Globalization.DateTimeStyles, result: ref[System.DateTime], ) -> System.Boolean:
        ...

    @typing.overload
    @staticmethod
    def TryParseExact(s: System.String, formats: list[System.String], provider: System.IFormatProvider, style: System.Globalization.DateTimeStyles, result: ref[System.DateTime], ) -> System.Boolean:
        ...

    @typing.overload
    @staticmethod
    def TryParseExact(s: System.ReadOnlySpan[System.Char], formats: list[System.String], provider: System.IFormatProvider, style: System.Globalization.DateTimeStyles, result: ref[System.DateTime], ) -> System.Boolean:
        ...

    @typing.overload
    def GetDateTimeFormats(self, ) -> list[System.String]:
        ...

    @typing.overload
    def GetDateTimeFormats(self, provider: System.IFormatProvider, ) -> list[System.String]:
        ...

    @typing.overload
    def GetDateTimeFormats(self, format: System.Char, ) -> list[System.String]:
        ...

    @typing.overload
    def GetDateTimeFormats(self, format: System.Char, provider: System.IFormatProvider, ) -> list[System.String]:
        ...

    @typing.overload
    def GetTypeCode(self, ) -> System.TypeCode:
        ...

    @typing.overload
    def Add(self, value: System.TimeSpan, ) -> System.DateTime:
        ...

    @typing.overload
    def AddDays(self, value: System.Double, ) -> System.DateTime:
        ...

    @typing.overload
    def AddHours(self, value: System.Double, ) -> System.DateTime:
        ...

    @typing.overload
    def AddMilliseconds(self, value: System.Double, ) -> System.DateTime:
        ...

    @typing.overload
    def AddMinutes(self, value: System.Double, ) -> System.DateTime:
        ...

    @typing.overload
    def AddMonths(self, months: System.Int32, ) -> System.DateTime:
        ...

    @typing.overload
    def AddSeconds(self, value: System.Double, ) -> System.DateTime:
        ...

    @typing.overload
    def AddTicks(self, value: System.Int64, ) -> System.DateTime:
        ...

    @typing.overload
    def AddYears(self, value: System.Int32, ) -> System.DateTime:
        ...

    @typing.overload
    @staticmethod
    def Compare(t1: System.DateTime, t2: System.DateTime, ) -> System.Int32:
        ...

    @typing.overload
    def CompareTo(self, value: System.Object, ) -> System.Int32:
        ...

    @typing.overload
    def CompareTo(self, value: System.DateTime, ) -> System.Int32:
        ...

    @typing.overload
    @staticmethod
    def DaysInMonth(year: System.Int32, month: System.Int32, ) -> System.Int32:
        ...

    @typing.overload
    def Equals(self, value: System.Object, ) -> System.Boolean:
        ...

    @typing.overload
    def Equals(self, value: System.DateTime, ) -> System.Boolean:
        ...

    @typing.overload
    @staticmethod
    def Equals(t1: System.DateTime, t2: System.DateTime, ) -> System.Boolean:
        ...

    @typing.overload
    @staticmethod
    def FromBinary(dateData: System.Int64, ) -> System.DateTime:
        ...

    @typing.overload
    @staticmethod
    def FromFileTime(fileTime: System.Int64, ) -> System.DateTime:
        ...

    @typing.overload
    @staticmethod
    def FromFileTimeUtc(fileTime: System.Int64, ) -> System.DateTime:
        ...

    @typing.overload
    @staticmethod
    def FromOADate(d: System.Double, ) -> System.DateTime:
        ...

    @typing.overload
    def IsDaylightSavingTime(self, ) -> System.Boolean:
        ...

    @typing.overload
    @staticmethod
    def SpecifyKind(value: System.DateTime, kind: System.DateTimeKind, ) -> System.DateTime:
        ...

    @typing.overload
    def ToBinary(self, ) -> System.Int64:
        ...

    @typing.overload
    def GetHashCode(self, ) -> System.Int32:
        ...

    @typing.overload
    @staticmethod
    def IsLeapYear(year: System.Int32, ) -> System.Boolean:
        ...

    @typing.overload
    @staticmethod
    def Parse(s: System.String, ) -> System.DateTime:
        ...

    @typing.overload
    @staticmethod
    def Parse(s: System.String, provider: System.IFormatProvider, ) -> System.DateTime:
        ...

    @typing.overload
    @staticmethod
    def Parse(s: System.String, provider: System.IFormatProvider, styles: System.Globalization.DateTimeStyles, ) -> System.DateTime:
        ...

class Func(System.ICloneable, System.Runtime.Serialization.ISerializable, System.MulticastDelegate, typing.Generic[T, TResult]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def Target(self) -> System.Object:
        ...

    @property
    def Method(self) -> System.Reflection.MethodInfo:
        ...

    # methods
    @typing.overload
    def __init__(self, object: System.Object, method: System.IntPtr, ):
        ...

    @typing.overload
    def Invoke(self, arg: T, ) -> TResult:
        ...

    @typing.overload
    def BeginInvoke(self, arg: T, callback: System.AsyncCallback, object: System.Object, ) -> System.IAsyncResult:
        ...

    @typing.overload
    def EndInvoke(self, result: System.IAsyncResult, ) -> TResult:
        ...

class ICloneable(abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    # methods
    @typing.overload
    @abc.abstractmethod
    def Clone(self, ) -> System.Object:
        ...

class MulticastDelegate(System.ICloneable, System.Runtime.Serialization.ISerializable, System.Delegate, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def Target(self) -> System.Object:
        ...

    @property
    def Method(self) -> System.Reflection.MethodInfo:
        ...

    # methods
    @typing.overload
    def GetObjectData(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext, ) -> None:
        ...

    @typing.overload
    def Equals(self, obj: System.Object, ) -> System.Boolean:
        ...

    @typing.overload
    def GetInvocationList(self, ) -> list[System.Delegate]:
        ...

    @typing.overload
    def GetHashCode(self, ) -> System.Int32:
        ...

class IntPtr(System.IEquatable[System.IntPtr], System.IComparable, System.IComparable[System.IntPtr], System.ISpanFormattable, System.IFormattable, System.Runtime.Serialization.ISerializable, System.IBinaryInteger[System.IntPtr], System.IBinaryNumber[System.IntPtr], System.IBitwiseOperators[System.IntPtr, System.IntPtr, System.IntPtr], System.INumber[System.IntPtr], System.IAdditionOperators[System.IntPtr, System.IntPtr, System.IntPtr], System.IAdditiveIdentity[System.IntPtr, System.IntPtr], System.IComparisonOperators[System.IntPtr, System.IntPtr], System.IEqualityOperators[System.IntPtr, System.IntPtr], System.IDecrementOperators[System.IntPtr], System.IDivisionOperators[System.IntPtr, System.IntPtr, System.IntPtr], System.IIncrementOperators[System.IntPtr], System.IModulusOperators[System.IntPtr, System.IntPtr, System.IntPtr], System.IMultiplicativeIdentity[System.IntPtr, System.IntPtr], System.IMultiplyOperators[System.IntPtr, System.IntPtr, System.IntPtr], System.ISpanParseable[System.IntPtr], System.IParseable[System.IntPtr], System.ISubtractionOperators[System.IntPtr, System.IntPtr, System.IntPtr], System.IUnaryNegationOperators[System.IntPtr, System.IntPtr], System.IUnaryPlusOperators[System.IntPtr, System.IntPtr], System.IShiftOperators[System.IntPtr, System.IntPtr], System.IMinMaxValue[System.IntPtr], System.ISignedNumber[System.IntPtr], System.ValueType):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def Size(self) -> System.Int32:
        ...

    @property
    def MaxValue(self) -> System.IntPtr:
        ...

    @property
    def MinValue(self) -> System.IntPtr:
        ...

    # methods
    @typing.overload
    def __init__(self, value: System.Int32, ):
        ...

    @typing.overload
    def __init__(self, value: System.Int64, ):
        ...

    @typing.overload
    def __init__(self, value: ptr[None], ):
        ...

    @typing.overload
    def Equals(self, obj: System.Object, ) -> System.Boolean:
        ...

    @typing.overload
    def GetHashCode(self, ) -> System.Int32:
        ...

    @typing.overload
    def ToInt32(self, ) -> System.Int32:
        ...

    @typing.overload
    def ToInt64(self, ) -> System.Int64:
        ...

    @typing.overload
    @staticmethod
    def Add(pointer: System.IntPtr, offset: System.Int32, ) -> System.IntPtr:
        ...

    @typing.overload
    @staticmethod
    def Subtract(pointer: System.IntPtr, offset: System.Int32, ) -> System.IntPtr:
        ...

    @typing.overload
    def ToPointer(self, ) -> ptr[None]:
        ...

    @typing.overload
    def CompareTo(self, value: System.Object, ) -> System.Int32:
        ...

    @typing.overload
    def CompareTo(self, value: System.IntPtr, ) -> System.Int32:
        ...

    @typing.overload
    def Equals(self, other: System.IntPtr, ) -> System.Boolean:
        ...

    @typing.overload
    def ToString(self, ) -> System.String:
        ...

    @typing.overload
    def ToString(self, format: System.String, ) -> System.String:
        ...

    @typing.overload
    def ToString(self, provider: System.IFormatProvider, ) -> System.String:
        ...

    @typing.overload
    def ToString(self, format: System.String, provider: System.IFormatProvider, ) -> System.String:
        ...

    @typing.overload
    def TryFormat(self, destination: System.Span[System.Char], charsWritten: ref[System.Int32], format: System.ReadOnlySpan[System.Char], provider: System.IFormatProvider, ) -> System.Boolean:
        ...

    @typing.overload
    @staticmethod
    def Parse(s: System.String, ) -> System.IntPtr:
        ...

    @typing.overload
    @staticmethod
    def Parse(s: System.String, style: System.Globalization.NumberStyles, ) -> System.IntPtr:
        ...

    @typing.overload
    @staticmethod
    def Parse(s: System.String, provider: System.IFormatProvider, ) -> System.IntPtr:
        ...

    @typing.overload
    @staticmethod
    def Parse(s: System.String, style: System.Globalization.NumberStyles, provider: System.IFormatProvider, ) -> System.IntPtr:
        ...

    @typing.overload
    @staticmethod
    def Parse(s: System.ReadOnlySpan[System.Char], style: System.Globalization.NumberStyles, provider: System.IFormatProvider, ) -> System.IntPtr:
        ...

    @typing.overload
    @staticmethod
    def TryParse(s: System.String, result: ref[System.IntPtr], ) -> System.Boolean:
        ...

    @typing.overload
    @staticmethod
    def TryParse(s: System.String, style: System.Globalization.NumberStyles, provider: System.IFormatProvider, result: ref[System.IntPtr], ) -> System.Boolean:
        ...

    @typing.overload
    @staticmethod
    def TryParse(s: System.ReadOnlySpan[System.Char], result: ref[System.IntPtr], ) -> System.Boolean:
        ...

    @typing.overload
    @staticmethod
    def TryParse(s: System.ReadOnlySpan[System.Char], style: System.Globalization.NumberStyles, provider: System.IFormatProvider, result: ref[System.IntPtr], ) -> System.Boolean:
        ...

class AsyncCallback(System.ICloneable, System.Runtime.Serialization.ISerializable, System.MulticastDelegate):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def Target(self) -> System.Object:
        ...

    @property
    def Method(self) -> System.Reflection.MethodInfo:
        ...

    # methods
    @typing.overload
    def __init__(self, object: System.Object, method: System.IntPtr, ):
        ...

    @typing.overload
    def Invoke(self, ar: System.IAsyncResult, ) -> None:
        ...

    @typing.overload
    def BeginInvoke(self, ar: System.IAsyncResult, callback: System.AsyncCallback, object: System.Object, ) -> System.IAsyncResult:
        ...

    @typing.overload
    def EndInvoke(self, result: System.IAsyncResult, ) -> None:
        ...

class IAsyncResult(abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @abc.abstractmethod
    @property
    def IsCompleted(self) -> System.Boolean:
        ...

    @abc.abstractmethod
    @property
    def AsyncWaitHandle(self) -> System.Threading.WaitHandle:
        ...

    @abc.abstractmethod
    @property
    def AsyncState(self) -> System.Object:
        ...

    @abc.abstractmethod
    @property
    def CompletedSynchronously(self) -> System.Boolean:
        ...

    # methods
class Guid(System.ISpanFormattable, System.IFormattable, System.IComparable, System.IComparable[System.Guid], System.IEquatable[System.Guid], System.IComparisonOperators[System.Guid, System.Guid], System.IEqualityOperators[System.Guid, System.Guid], System.ISpanParseable[System.Guid], System.IParseable[System.Guid], System.ValueType):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    # methods
    @typing.overload
    def __init__(self, b: list[System.Byte], ):
        ...

    @typing.overload
    def __init__(self, b: System.ReadOnlySpan[System.Byte], ):
        ...

    @typing.overload
    def __init__(self, a: System.UInt32, b: System.UInt16, c: System.UInt16, d: System.Byte, e: System.Byte, f: System.Byte, g: System.Byte, h: System.Byte, i: System.Byte, j: System.Byte, k: System.Byte, ):
        ...

    @typing.overload
    def __init__(self, a: System.Int32, b: System.Int16, c: System.Int16, d: list[System.Byte], ):
        ...

    @typing.overload
    def __init__(self, a: System.Int32, b: System.Int16, c: System.Int16, d: System.Byte, e: System.Byte, f: System.Byte, g: System.Byte, h: System.Byte, i: System.Byte, j: System.Byte, k: System.Byte, ):
        ...

    @typing.overload
    def __init__(self, g: System.String, ):
        ...

    @typing.overload
    @staticmethod
    def Parse(input: System.String, ) -> System.Guid:
        ...

    @typing.overload
    @staticmethod
    def Parse(input: System.ReadOnlySpan[System.Char], ) -> System.Guid:
        ...

    @typing.overload
    @staticmethod
    def TryParse(input: System.String, result: ref[System.Guid], ) -> System.Boolean:
        ...

    @typing.overload
    @staticmethod
    def TryParse(input: System.ReadOnlySpan[System.Char], result: ref[System.Guid], ) -> System.Boolean:
        ...

    @typing.overload
    @staticmethod
    def ParseExact(input: System.String, format: System.String, ) -> System.Guid:
        ...

    @typing.overload
    @staticmethod
    def ParseExact(input: System.ReadOnlySpan[System.Char], format: System.ReadOnlySpan[System.Char], ) -> System.Guid:
        ...

    @typing.overload
    @staticmethod
    def TryParseExact(input: System.String, format: System.String, result: ref[System.Guid], ) -> System.Boolean:
        ...

    @typing.overload
    @staticmethod
    def TryParseExact(input: System.ReadOnlySpan[System.Char], format: System.ReadOnlySpan[System.Char], result: ref[System.Guid], ) -> System.Boolean:
        ...

    @typing.overload
    def ToByteArray(self, ) -> list[System.Byte]:
        ...

    @typing.overload
    def TryWriteBytes(self, destination: System.Span[System.Byte], ) -> System.Boolean:
        ...

    @typing.overload
    def ToString(self, ) -> System.String:
        ...

    @typing.overload
    def GetHashCode(self, ) -> System.Int32:
        ...

    @typing.overload
    def Equals(self, o: System.Object, ) -> System.Boolean:
        ...

    @typing.overload
    def Equals(self, g: System.Guid, ) -> System.Boolean:
        ...

    @typing.overload
    def CompareTo(self, value: System.Object, ) -> System.Int32:
        ...

    @typing.overload
    def CompareTo(self, value: System.Guid, ) -> System.Int32:
        ...

    @typing.overload
    def ToString(self, format: System.String, ) -> System.String:
        ...

    @typing.overload
    def ToString(self, format: System.String, provider: System.IFormatProvider, ) -> System.String:
        ...

    @typing.overload
    def TryFormat(self, destination: System.Span[System.Char], charsWritten: ref[System.Int32], format: System.ReadOnlySpan[System.Char], ) -> System.Boolean:
        ...

    @typing.overload
    @staticmethod
    def NewGuid() -> System.Guid:
        ...

class Tuple(System.Collections.IStructuralEquatable, System.Collections.IStructuralComparable, System.IComparable, System.ITupleInternal, System.Runtime.CompilerServices.ITuple, System.Object, typing.Generic[T1, T2]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def Item1(self) -> T1:
        ...

    @property
    def Item2(self) -> T2:
        ...

    # methods
    @typing.overload
    def __init__(self, item1: T1, item2: T2, ):
        ...

    @typing.overload
    def Equals(self, obj: System.Object, ) -> System.Boolean:
        ...

    @typing.overload
    def GetHashCode(self, ) -> System.Int32:
        ...

    @typing.overload
    def ToString(self, ) -> System.String:
        ...

class Type(System.Reflection.ICustomAttributeProvider, System.Reflection.IReflect, System.Reflection.MemberInfo, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def IsInterface(self) -> System.Boolean:
        ...

    @property
    def MemberType(self) -> System.Reflection.MemberTypes:
        ...

    @abc.abstractmethod
    @property
    def Namespace(self) -> System.String:
        ...

    @abc.abstractmethod
    @property
    def AssemblyQualifiedName(self) -> System.String:
        ...

    @abc.abstractmethod
    @property
    def FullName(self) -> System.String:
        ...

    @abc.abstractmethod
    @property
    def Assembly(self) -> System.Reflection.Assembly:
        ...

    @abc.abstractmethod
    @property
    def Module(self) -> System.Reflection.Module:
        ...

    @property
    def IsNested(self) -> System.Boolean:
        ...

    @property
    def DeclaringType(self) -> System.Type:
        ...

    @property
    def DeclaringMethod(self) -> System.Reflection.MethodBase:
        ...

    @property
    def ReflectedType(self) -> System.Type:
        ...

    @abc.abstractmethod
    @property
    def UnderlyingSystemType(self) -> System.Type:
        ...

    @property
    def IsTypeDefinition(self) -> System.Boolean:
        ...

    @property
    def IsArray(self) -> System.Boolean:
        ...

    @property
    def IsByRef(self) -> System.Boolean:
        ...

    @property
    def IsPointer(self) -> System.Boolean:
        ...

    @property
    def IsConstructedGenericType(self) -> System.Boolean:
        ...

    @property
    def IsGenericParameter(self) -> System.Boolean:
        ...

    @property
    def IsGenericTypeParameter(self) -> System.Boolean:
        ...

    @property
    def IsGenericMethodParameter(self) -> System.Boolean:
        ...

    @property
    def IsGenericType(self) -> System.Boolean:
        ...

    @property
    def IsGenericTypeDefinition(self) -> System.Boolean:
        ...

    @property
    def IsSZArray(self) -> System.Boolean:
        ...

    @property
    def IsVariableBoundArray(self) -> System.Boolean:
        ...

    @property
    def IsByRefLike(self) -> System.Boolean:
        ...

    @property
    def HasElementType(self) -> System.Boolean:
        ...

    @property
    def GenericTypeArguments(self) -> list[System.Type]:
        ...

    @property
    def GenericParameterPosition(self) -> System.Int32:
        ...

    @property
    def GenericParameterAttributes(self) -> System.Reflection.GenericParameterAttributes:
        ...

    @property
    def Attributes(self) -> System.Reflection.TypeAttributes:
        ...

    @property
    def IsAbstract(self) -> System.Boolean:
        ...

    @property
    def IsImport(self) -> System.Boolean:
        ...

    @property
    def IsSealed(self) -> System.Boolean:
        ...

    @property
    def IsSpecialName(self) -> System.Boolean:
        ...

    @property
    def IsClass(self) -> System.Boolean:
        ...

    @property
    def IsNestedAssembly(self) -> System.Boolean:
        ...

    @property
    def IsNestedFamANDAssem(self) -> System.Boolean:
        ...

    @property
    def IsNestedFamily(self) -> System.Boolean:
        ...

    @property
    def IsNestedFamORAssem(self) -> System.Boolean:
        ...

    @property
    def IsNestedPrivate(self) -> System.Boolean:
        ...

    @property
    def IsNestedPublic(self) -> System.Boolean:
        ...

    @property
    def IsNotPublic(self) -> System.Boolean:
        ...

    @property
    def IsPublic(self) -> System.Boolean:
        ...

    @property
    def IsAutoLayout(self) -> System.Boolean:
        ...

    @property
    def IsExplicitLayout(self) -> System.Boolean:
        ...

    @property
    def IsLayoutSequential(self) -> System.Boolean:
        ...

    @property
    def IsAnsiClass(self) -> System.Boolean:
        ...

    @property
    def IsAutoClass(self) -> System.Boolean:
        ...

    @property
    def IsUnicodeClass(self) -> System.Boolean:
        ...

    @property
    def IsCOMObject(self) -> System.Boolean:
        ...

    @property
    def IsContextful(self) -> System.Boolean:
        ...

    @property
    def IsEnum(self) -> System.Boolean:
        ...

    @property
    def IsMarshalByRef(self) -> System.Boolean:
        ...

    @property
    def IsPrimitive(self) -> System.Boolean:
        ...

    @property
    def IsValueType(self) -> System.Boolean:
        ...

    @property
    def IsSignatureType(self) -> System.Boolean:
        ...

    @property
    def IsSecurityCritical(self) -> System.Boolean:
        ...

    @property
    def IsSecuritySafeCritical(self) -> System.Boolean:
        ...

    @property
    def IsSecurityTransparent(self) -> System.Boolean:
        ...

    @property
    def StructLayoutAttribute(self) -> System.Runtime.InteropServices.StructLayoutAttribute:
        ...

    @property
    def TypeInitializer(self) -> System.Reflection.ConstructorInfo:
        ...

    @property
    def TypeHandle(self) -> System.RuntimeTypeHandle:
        ...

    @abc.abstractmethod
    @property
    def GUID(self) -> System.Guid:
        ...

    @abc.abstractmethod
    @property
    def BaseType(self) -> System.Type:
        ...

    @property
    def DefaultBinder(self) -> System.Reflection.Binder:
        ...

    @property
    def IsSerializable(self) -> System.Boolean:
        ...

    @property
    def ContainsGenericParameters(self) -> System.Boolean:
        ...

    @property
    def IsVisible(self) -> System.Boolean:
        ...

    @abc.abstractmethod
    @property
    def Name(self) -> System.String:
        ...

    @property
    def CustomAttributes(self) -> System.Collections.Generic.IEnumerable[System.Reflection.CustomAttributeData]:
        ...

    @property
    def IsCollectible(self) -> System.Boolean:
        ...

    @property
    def MetadataToken(self) -> System.Int32:
        ...

    # methods
    @typing.overload
    @abc.abstractmethod
    def GetField(self, name: System.String, bindingAttr: System.Reflection.BindingFlags, ) -> System.Reflection.FieldInfo:
        ...

    @typing.overload
    def GetFields(self, ) -> list[System.Reflection.FieldInfo]:
        ...

    @typing.overload
    @abc.abstractmethod
    def GetFields(self, bindingAttr: System.Reflection.BindingFlags, ) -> list[System.Reflection.FieldInfo]:
        ...

    @typing.overload
    def GetMember(self, name: System.String, ) -> list[System.Reflection.MemberInfo]:
        ...

    @typing.overload
    def GetMember(self, name: System.String, bindingAttr: System.Reflection.BindingFlags, ) -> list[System.Reflection.MemberInfo]:
        ...

    @typing.overload
    def GetMember(self, name: System.String, type: System.Reflection.MemberTypes, bindingAttr: System.Reflection.BindingFlags, ) -> list[System.Reflection.MemberInfo]:
        ...

    @typing.overload
    def GetMembers(self, ) -> list[System.Reflection.MemberInfo]:
        ...

    @typing.overload
    def GetMemberWithSameMetadataDefinitionAs(self, member: System.Reflection.MemberInfo, ) -> System.Reflection.MemberInfo:
        ...

    @typing.overload
    @abc.abstractmethod
    def GetMembers(self, bindingAttr: System.Reflection.BindingFlags, ) -> list[System.Reflection.MemberInfo]:
        ...

    @typing.overload
    def GetMethod(self, name: System.String, ) -> System.Reflection.MethodInfo:
        ...

    @typing.overload
    def GetMethod(self, name: System.String, bindingAttr: System.Reflection.BindingFlags, ) -> System.Reflection.MethodInfo:
        ...

    @typing.overload
    def GetMethod(self, name: System.String, bindingAttr: System.Reflection.BindingFlags, types: list[System.Type], ) -> System.Reflection.MethodInfo:
        ...

    @typing.overload
    def GetMethod(self, name: System.String, types: list[System.Type], ) -> System.Reflection.MethodInfo:
        ...

    @typing.overload
    def GetMethod(self, name: System.String, types: list[System.Type], modifiers: list[System.Reflection.ParameterModifier], ) -> System.Reflection.MethodInfo:
        ...

    @typing.overload
    def GetMethod(self, name: System.String, bindingAttr: System.Reflection.BindingFlags, binder: System.Reflection.Binder, types: list[System.Type], modifiers: list[System.Reflection.ParameterModifier], ) -> System.Reflection.MethodInfo:
        ...

    @typing.overload
    def GetMethod(self, name: System.String, bindingAttr: System.Reflection.BindingFlags, binder: System.Reflection.Binder, callConvention: System.Reflection.CallingConventions, types: list[System.Type], modifiers: list[System.Reflection.ParameterModifier], ) -> System.Reflection.MethodInfo:
        ...

    @typing.overload
    def GetMethod(self, name: System.String, genericParameterCount: System.Int32, types: list[System.Type], ) -> System.Reflection.MethodInfo:
        ...

    @typing.overload
    def GetMethod(self, name: System.String, genericParameterCount: System.Int32, types: list[System.Type], modifiers: list[System.Reflection.ParameterModifier], ) -> System.Reflection.MethodInfo:
        ...

    @typing.overload
    def GetMethod(self, name: System.String, genericParameterCount: System.Int32, bindingAttr: System.Reflection.BindingFlags, binder: System.Reflection.Binder, types: list[System.Type], modifiers: list[System.Reflection.ParameterModifier], ) -> System.Reflection.MethodInfo:
        ...

    @typing.overload
    def GetMethod(self, name: System.String, genericParameterCount: System.Int32, bindingAttr: System.Reflection.BindingFlags, binder: System.Reflection.Binder, callConvention: System.Reflection.CallingConventions, types: list[System.Type], modifiers: list[System.Reflection.ParameterModifier], ) -> System.Reflection.MethodInfo:
        ...

    @typing.overload
    def GetMethods(self, ) -> list[System.Reflection.MethodInfo]:
        ...

    @typing.overload
    @abc.abstractmethod
    def GetMethods(self, bindingAttr: System.Reflection.BindingFlags, ) -> list[System.Reflection.MethodInfo]:
        ...

    @typing.overload
    def GetNestedType(self, name: System.String, ) -> System.Type:
        ...

    @typing.overload
    @abc.abstractmethod
    def GetNestedType(self, name: System.String, bindingAttr: System.Reflection.BindingFlags, ) -> System.Type:
        ...

    @typing.overload
    def GetNestedTypes(self, ) -> list[System.Type]:
        ...

    @typing.overload
    @abc.abstractmethod
    def GetNestedTypes(self, bindingAttr: System.Reflection.BindingFlags, ) -> list[System.Type]:
        ...

    @typing.overload
    def GetProperty(self, name: System.String, ) -> System.Reflection.PropertyInfo:
        ...

    @typing.overload
    def GetProperty(self, name: System.String, bindingAttr: System.Reflection.BindingFlags, ) -> System.Reflection.PropertyInfo:
        ...

    @typing.overload
    def GetProperty(self, name: System.String, returnType: System.Type, ) -> System.Reflection.PropertyInfo:
        ...

    @typing.overload
    def GetProperty(self, name: System.String, types: list[System.Type], ) -> System.Reflection.PropertyInfo:
        ...

    @typing.overload
    def GetProperty(self, name: System.String, returnType: System.Type, types: list[System.Type], ) -> System.Reflection.PropertyInfo:
        ...

    @typing.overload
    def GetProperty(self, name: System.String, returnType: System.Type, types: list[System.Type], modifiers: list[System.Reflection.ParameterModifier], ) -> System.Reflection.PropertyInfo:
        ...

    @typing.overload
    def GetProperty(self, name: System.String, bindingAttr: System.Reflection.BindingFlags, binder: System.Reflection.Binder, returnType: System.Type, types: list[System.Type], modifiers: list[System.Reflection.ParameterModifier], ) -> System.Reflection.PropertyInfo:
        ...

    @typing.overload
    def GetProperties(self, ) -> list[System.Reflection.PropertyInfo]:
        ...

    @typing.overload
    @abc.abstractmethod
    def GetProperties(self, bindingAttr: System.Reflection.BindingFlags, ) -> list[System.Reflection.PropertyInfo]:
        ...

    @typing.overload
    def GetDefaultMembers(self, ) -> list[System.Reflection.MemberInfo]:
        ...

    @typing.overload
    @staticmethod
    def GetTypeHandle(o: System.Object, ) -> System.RuntimeTypeHandle:
        ...

    @typing.overload
    @staticmethod
    def GetTypeArray(args: list[System.Object], ) -> list[System.Type]:
        ...

    @typing.overload
    @staticmethod
    def GetTypeCode(type: System.Type, ) -> System.TypeCode:
        ...

    @typing.overload
    @staticmethod
    def GetTypeFromCLSID(clsid: System.Guid, ) -> System.Type:
        ...

    @typing.overload
    @staticmethod
    def GetTypeFromCLSID(clsid: System.Guid, throwOnError: System.Boolean, ) -> System.Type:
        ...

    @typing.overload
    @staticmethod
    def GetTypeFromCLSID(clsid: System.Guid, server: System.String, ) -> System.Type:
        ...

    @typing.overload
    @staticmethod
    def GetTypeFromCLSID(clsid: System.Guid, server: System.String, throwOnError: System.Boolean, ) -> System.Type:
        ...

    @typing.overload
    @staticmethod
    def GetTypeFromProgID(progID: System.String, ) -> System.Type:
        ...

    @typing.overload
    @staticmethod
    def GetTypeFromProgID(progID: System.String, throwOnError: System.Boolean, ) -> System.Type:
        ...

    @typing.overload
    @staticmethod
    def GetTypeFromProgID(progID: System.String, server: System.String, ) -> System.Type:
        ...

    @typing.overload
    @staticmethod
    def GetTypeFromProgID(progID: System.String, server: System.String, throwOnError: System.Boolean, ) -> System.Type:
        ...

    @typing.overload
    def InvokeMember(self, name: System.String, invokeAttr: System.Reflection.BindingFlags, binder: System.Reflection.Binder, target: System.Object, args: list[System.Object], ) -> System.Object:
        ...

    @typing.overload
    def InvokeMember(self, name: System.String, invokeAttr: System.Reflection.BindingFlags, binder: System.Reflection.Binder, target: System.Object, args: list[System.Object], culture: System.Globalization.CultureInfo, ) -> System.Object:
        ...

    @typing.overload
    @abc.abstractmethod
    def InvokeMember(self, name: System.String, invokeAttr: System.Reflection.BindingFlags, binder: System.Reflection.Binder, target: System.Object, args: list[System.Object], modifiers: list[System.Reflection.ParameterModifier], culture: System.Globalization.CultureInfo, namedParameters: list[System.String], ) -> System.Object:
        ...

    @typing.overload
    def GetInterface(self, name: System.String, ) -> System.Type:
        ...

    @typing.overload
    @abc.abstractmethod
    def GetInterface(self, name: System.String, ignoreCase: System.Boolean, ) -> System.Type:
        ...

    @typing.overload
    @abc.abstractmethod
    def GetInterfaces(self, ) -> list[System.Type]:
        ...

    @typing.overload
    def GetInterfaceMap(self, interfaceType: System.Type, ) -> System.Reflection.InterfaceMapping:
        ...

    @typing.overload
    def IsInstanceOfType(self, o: System.Object, ) -> System.Boolean:
        ...

    @typing.overload
    def IsEquivalentTo(self, other: System.Type, ) -> System.Boolean:
        ...

    @typing.overload
    def GetEnumUnderlyingType(self, ) -> System.Type:
        ...

    @typing.overload
    def GetEnumValues(self, ) -> System.Array:
        ...

    @typing.overload
    def MakeArrayType(self, ) -> System.Type:
        ...

    @typing.overload
    def MakeArrayType(self, rank: System.Int32, ) -> System.Type:
        ...

    @typing.overload
    def MakeByRefType(self, ) -> System.Type:
        ...

    @typing.overload
    def MakeGenericType(self, typeArguments: list[System.Type], ) -> System.Type:
        ...

    @typing.overload
    def MakePointerType(self, ) -> System.Type:
        ...

    @typing.overload
    @staticmethod
    def MakeGenericSignatureType(genericTypeDefinition: System.Type, typeArguments: list[System.Type], ) -> System.Type:
        ...

    @typing.overload
    @staticmethod
    def MakeGenericMethodParameter(position: System.Int32, ) -> System.Type:
        ...

    @typing.overload
    def ToString(self, ) -> System.String:
        ...

    @typing.overload
    def Equals(self, o: System.Object, ) -> System.Boolean:
        ...

    @typing.overload
    def GetHashCode(self, ) -> System.Int32:
        ...

    @typing.overload
    def Equals(self, o: System.Type, ) -> System.Boolean:
        ...

    @typing.overload
    @staticmethod
    def ReflectionOnlyGetType(typeName: System.String, throwIfNotFound: System.Boolean, ignoreCase: System.Boolean, ) -> System.Type:
        ...

    @typing.overload
    def IsEnumDefined(self, value: System.Object, ) -> System.Boolean:
        ...

    @typing.overload
    def GetEnumName(self, value: System.Object, ) -> System.String:
        ...

    @typing.overload
    def GetEnumNames(self, ) -> list[System.String]:
        ...

    @typing.overload
    def FindInterfaces(self, filter: System.Reflection.TypeFilter, filterCriteria: System.Object, ) -> list[System.Type]:
        ...

    @typing.overload
    def FindMembers(self, memberType: System.Reflection.MemberTypes, bindingAttr: System.Reflection.BindingFlags, filter: System.Reflection.MemberFilter, filterCriteria: System.Object, ) -> list[System.Reflection.MemberInfo]:
        ...

    @typing.overload
    def IsSubclassOf(self, c: System.Type, ) -> System.Boolean:
        ...

    @typing.overload
    def IsAssignableFrom(self, c: System.Type, ) -> System.Boolean:
        ...

    @typing.overload
    @staticmethod
    def GetType(typeName: System.String, throwOnError: System.Boolean, ignoreCase: System.Boolean, ) -> System.Type:
        ...

    @typing.overload
    @staticmethod
    def GetType(typeName: System.String, throwOnError: System.Boolean, ) -> System.Type:
        ...

    @typing.overload
    @staticmethod
    def GetType(typeName: System.String, ) -> System.Type:
        ...

    @typing.overload
    @staticmethod
    def GetType(typeName: System.String, assemblyResolver: System.Func[System.Reflection.AssemblyName, System.Reflection.Assembly], typeResolver: System.Func[System.Reflection.Assembly, System.String, System.Boolean, System.Type], ) -> System.Type:
        ...

    @typing.overload
    @staticmethod
    def GetType(typeName: System.String, assemblyResolver: System.Func[System.Reflection.AssemblyName, System.Reflection.Assembly], typeResolver: System.Func[System.Reflection.Assembly, System.String, System.Boolean, System.Type], throwOnError: System.Boolean, ) -> System.Type:
        ...

    @typing.overload
    @staticmethod
    def GetType(typeName: System.String, assemblyResolver: System.Func[System.Reflection.AssemblyName, System.Reflection.Assembly], typeResolver: System.Func[System.Reflection.Assembly, System.String, System.Boolean, System.Type], throwOnError: System.Boolean, ignoreCase: System.Boolean, ) -> System.Type:
        ...

    @typing.overload
    @staticmethod
    def GetTypeFromHandle(handle: System.RuntimeTypeHandle, ) -> System.Type:
        ...

    @typing.overload
    def GetType(self, ) -> System.Type:
        ...

    @typing.overload
    @abc.abstractmethod
    def GetElementType(self, ) -> System.Type:
        ...

    @typing.overload
    def GetArrayRank(self, ) -> System.Int32:
        ...

    @typing.overload
    def GetGenericTypeDefinition(self, ) -> System.Type:
        ...

    @typing.overload
    def GetGenericArguments(self, ) -> list[System.Type]:
        ...

    @typing.overload
    def GetGenericParameterConstraints(self, ) -> list[System.Type]:
        ...

    @typing.overload
    def IsAssignableTo(self, targetType: System.Type, ) -> System.Boolean:
        ...

    @typing.overload
    def GetConstructor(self, types: list[System.Type], ) -> System.Reflection.ConstructorInfo:
        ...

    @typing.overload
    def GetConstructor(self, bindingAttr: System.Reflection.BindingFlags, types: list[System.Type], ) -> System.Reflection.ConstructorInfo:
        ...

    @typing.overload
    def GetConstructor(self, bindingAttr: System.Reflection.BindingFlags, binder: System.Reflection.Binder, types: list[System.Type], modifiers: list[System.Reflection.ParameterModifier], ) -> System.Reflection.ConstructorInfo:
        ...

    @typing.overload
    def GetConstructor(self, bindingAttr: System.Reflection.BindingFlags, binder: System.Reflection.Binder, callConvention: System.Reflection.CallingConventions, types: list[System.Type], modifiers: list[System.Reflection.ParameterModifier], ) -> System.Reflection.ConstructorInfo:
        ...

    @typing.overload
    def GetConstructors(self, ) -> list[System.Reflection.ConstructorInfo]:
        ...

    @typing.overload
    @abc.abstractmethod
    def GetConstructors(self, bindingAttr: System.Reflection.BindingFlags, ) -> list[System.Reflection.ConstructorInfo]:
        ...

    @typing.overload
    def GetEvent(self, name: System.String, ) -> System.Reflection.EventInfo:
        ...

    @typing.overload
    @abc.abstractmethod
    def GetEvent(self, name: System.String, bindingAttr: System.Reflection.BindingFlags, ) -> System.Reflection.EventInfo:
        ...

    @typing.overload
    def GetEvents(self, ) -> list[System.Reflection.EventInfo]:
        ...

    @typing.overload
    @abc.abstractmethod
    def GetEvents(self, bindingAttr: System.Reflection.BindingFlags, ) -> list[System.Reflection.EventInfo]:
        ...

    @typing.overload
    def GetField(self, name: System.String, ) -> System.Reflection.FieldInfo:
        ...

class Double(System.IComparable, System.IConvertible, System.ISpanFormattable, System.IFormattable, System.IComparable[System.Double], System.IEquatable[System.Double], System.IBinaryFloatingPoint[System.Double], System.IBinaryNumber[System.Double], System.IBitwiseOperators[System.Double, System.Double, System.Double], System.INumber[System.Double], System.IAdditionOperators[System.Double, System.Double, System.Double], System.IAdditiveIdentity[System.Double, System.Double], System.IComparisonOperators[System.Double, System.Double], System.IEqualityOperators[System.Double, System.Double], System.IDecrementOperators[System.Double], System.IDivisionOperators[System.Double, System.Double, System.Double], System.IIncrementOperators[System.Double], System.IModulusOperators[System.Double, System.Double, System.Double], System.IMultiplicativeIdentity[System.Double, System.Double], System.IMultiplyOperators[System.Double, System.Double, System.Double], System.ISpanParseable[System.Double], System.IParseable[System.Double], System.ISubtractionOperators[System.Double, System.Double, System.Double], System.IUnaryNegationOperators[System.Double, System.Double], System.IUnaryPlusOperators[System.Double, System.Double], System.IFloatingPoint[System.Double], System.ISignedNumber[System.Double], System.IMinMaxValue[System.Double], System.ValueType):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    # methods
    @typing.overload
    @staticmethod
    def IsFinite(d: System.Double, ) -> System.Boolean:
        ...

    @typing.overload
    @staticmethod
    def IsInfinity(d: System.Double, ) -> System.Boolean:
        ...

    @typing.overload
    @staticmethod
    def IsNaN(d: System.Double, ) -> System.Boolean:
        ...

    @typing.overload
    @staticmethod
    def IsNegative(d: System.Double, ) -> System.Boolean:
        ...

    @typing.overload
    @staticmethod
    def IsNegativeInfinity(d: System.Double, ) -> System.Boolean:
        ...

    @typing.overload
    @staticmethod
    def IsNormal(d: System.Double, ) -> System.Boolean:
        ...

    @typing.overload
    @staticmethod
    def IsPositiveInfinity(d: System.Double, ) -> System.Boolean:
        ...

    @typing.overload
    @staticmethod
    def IsSubnormal(d: System.Double, ) -> System.Boolean:
        ...

    @typing.overload
    def CompareTo(self, value: System.Object, ) -> System.Int32:
        ...

    @typing.overload
    def CompareTo(self, value: System.Double, ) -> System.Int32:
        ...

    @typing.overload
    def Equals(self, obj: System.Object, ) -> System.Boolean:
        ...

    @typing.overload
    def Equals(self, obj: System.Double, ) -> System.Boolean:
        ...

    @typing.overload
    def GetHashCode(self, ) -> System.Int32:
        ...

    @typing.overload
    def ToString(self, ) -> System.String:
        ...

    @typing.overload
    def ToString(self, format: System.String, ) -> System.String:
        ...

    @typing.overload
    def ToString(self, provider: System.IFormatProvider, ) -> System.String:
        ...

    @typing.overload
    def ToString(self, format: System.String, provider: System.IFormatProvider, ) -> System.String:
        ...

    @typing.overload
    def TryFormat(self, destination: System.Span[System.Char], charsWritten: ref[System.Int32], format: System.ReadOnlySpan[System.Char], provider: System.IFormatProvider, ) -> System.Boolean:
        ...

    @typing.overload
    @staticmethod
    def Parse(s: System.String, ) -> System.Double:
        ...

    @typing.overload
    @staticmethod
    def Parse(s: System.String, style: System.Globalization.NumberStyles, ) -> System.Double:
        ...

    @typing.overload
    @staticmethod
    def Parse(s: System.String, provider: System.IFormatProvider, ) -> System.Double:
        ...

    @typing.overload
    @staticmethod
    def Parse(s: System.String, style: System.Globalization.NumberStyles, provider: System.IFormatProvider, ) -> System.Double:
        ...

    @typing.overload
    @staticmethod
    def Parse(s: System.ReadOnlySpan[System.Char], style: System.Globalization.NumberStyles, provider: System.IFormatProvider, ) -> System.Double:
        ...

    @typing.overload
    @staticmethod
    def TryParse(s: System.String, result: ref[System.Double], ) -> System.Boolean:
        ...

    @typing.overload
    @staticmethod
    def TryParse(s: System.ReadOnlySpan[System.Char], result: ref[System.Double], ) -> System.Boolean:
        ...

    @typing.overload
    @staticmethod
    def TryParse(s: System.String, style: System.Globalization.NumberStyles, provider: System.IFormatProvider, result: ref[System.Double], ) -> System.Boolean:
        ...

    @typing.overload
    @staticmethod
    def TryParse(s: System.ReadOnlySpan[System.Char], style: System.Globalization.NumberStyles, provider: System.IFormatProvider, result: ref[System.Double], ) -> System.Boolean:
        ...

    @typing.overload
    def GetTypeCode(self, ) -> System.TypeCode:
        ...

class DateTimeOffset(System.IComparable, System.ISpanFormattable, System.IFormattable, System.IComparable[System.DateTimeOffset], System.IEquatable[System.DateTimeOffset], System.Runtime.Serialization.ISerializable, System.Runtime.Serialization.IDeserializationCallback, System.IAdditionOperators[System.DateTimeOffset, System.TimeSpan, System.DateTimeOffset], System.IAdditiveIdentity[System.DateTimeOffset, System.TimeSpan], System.IComparisonOperators[System.DateTimeOffset, System.DateTimeOffset], System.IEqualityOperators[System.DateTimeOffset, System.DateTimeOffset], System.IMinMaxValue[System.DateTimeOffset], System.ISpanParseable[System.DateTimeOffset], System.IParseable[System.DateTimeOffset], System.ISubtractionOperators[System.DateTimeOffset, System.TimeSpan, System.DateTimeOffset], System.ISubtractionOperators[System.DateTimeOffset, System.DateTimeOffset, System.TimeSpan], System.ValueType):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def Now(self) -> System.DateTimeOffset:
        ...

    @property
    def UtcNow(self) -> System.DateTimeOffset:
        ...

    @property
    def DateTime(self) -> System.DateTime:
        ...

    @property
    def UtcDateTime(self) -> System.DateTime:
        ...

    @property
    def LocalDateTime(self) -> System.DateTime:
        ...

    @property
    def Date(self) -> System.DateTime:
        ...

    @property
    def Day(self) -> System.Int32:
        ...

    @property
    def DayOfWeek(self) -> System.DayOfWeek:
        ...

    @property
    def DayOfYear(self) -> System.Int32:
        ...

    @property
    def Hour(self) -> System.Int32:
        ...

    @property
    def Millisecond(self) -> System.Int32:
        ...

    @property
    def Minute(self) -> System.Int32:
        ...

    @property
    def Month(self) -> System.Int32:
        ...

    @property
    def Offset(self) -> System.TimeSpan:
        ...

    @property
    def Second(self) -> System.Int32:
        ...

    @property
    def Ticks(self) -> System.Int64:
        ...

    @property
    def UtcTicks(self) -> System.Int64:
        ...

    @property
    def TimeOfDay(self) -> System.TimeSpan:
        ...

    @property
    def Year(self) -> System.Int32:
        ...

    # methods
    @typing.overload
    def __init__(self, ticks: System.Int64, offset: System.TimeSpan, ):
        ...

    @typing.overload
    def __init__(self, dateTime: System.DateTime, ):
        ...

    @typing.overload
    def __init__(self, dateTime: System.DateTime, offset: System.TimeSpan, ):
        ...

    @typing.overload
    def __init__(self, year: System.Int32, month: System.Int32, day: System.Int32, hour: System.Int32, minute: System.Int32, second: System.Int32, offset: System.TimeSpan, ):
        ...

    @typing.overload
    def __init__(self, year: System.Int32, month: System.Int32, day: System.Int32, hour: System.Int32, minute: System.Int32, second: System.Int32, millisecond: System.Int32, offset: System.TimeSpan, ):
        ...

    @typing.overload
    def __init__(self, year: System.Int32, month: System.Int32, day: System.Int32, hour: System.Int32, minute: System.Int32, second: System.Int32, millisecond: System.Int32, calendar: System.Globalization.Calendar, offset: System.TimeSpan, ):
        ...

    @typing.overload
    @staticmethod
    def TryParse(input: System.String, result: ref[System.DateTimeOffset], ) -> System.Boolean:
        ...

    @typing.overload
    @staticmethod
    def TryParse(input: System.ReadOnlySpan[System.Char], result: ref[System.DateTimeOffset], ) -> System.Boolean:
        ...

    @typing.overload
    @staticmethod
    def TryParse(input: System.String, formatProvider: System.IFormatProvider, styles: System.Globalization.DateTimeStyles, result: ref[System.DateTimeOffset], ) -> System.Boolean:
        ...

    @typing.overload
    @staticmethod
    def TryParse(input: System.ReadOnlySpan[System.Char], formatProvider: System.IFormatProvider, styles: System.Globalization.DateTimeStyles, result: ref[System.DateTimeOffset], ) -> System.Boolean:
        ...

    @typing.overload
    @staticmethod
    def TryParseExact(input: System.String, format: System.String, formatProvider: System.IFormatProvider, styles: System.Globalization.DateTimeStyles, result: ref[System.DateTimeOffset], ) -> System.Boolean:
        ...

    @typing.overload
    @staticmethod
    def TryParseExact(input: System.ReadOnlySpan[System.Char], format: System.ReadOnlySpan[System.Char], formatProvider: System.IFormatProvider, styles: System.Globalization.DateTimeStyles, result: ref[System.DateTimeOffset], ) -> System.Boolean:
        ...

    @typing.overload
    @staticmethod
    def TryParseExact(input: System.String, formats: list[System.String], formatProvider: System.IFormatProvider, styles: System.Globalization.DateTimeStyles, result: ref[System.DateTimeOffset], ) -> System.Boolean:
        ...

    @typing.overload
    @staticmethod
    def TryParseExact(input: System.ReadOnlySpan[System.Char], formats: list[System.String], formatProvider: System.IFormatProvider, styles: System.Globalization.DateTimeStyles, result: ref[System.DateTimeOffset], ) -> System.Boolean:
        ...

    @typing.overload
    def ToOffset(self, offset: System.TimeSpan, ) -> System.DateTimeOffset:
        ...

    @typing.overload
    def Add(self, timeSpan: System.TimeSpan, ) -> System.DateTimeOffset:
        ...

    @typing.overload
    def AddDays(self, days: System.Double, ) -> System.DateTimeOffset:
        ...

    @typing.overload
    def AddHours(self, hours: System.Double, ) -> System.DateTimeOffset:
        ...

    @typing.overload
    def AddMilliseconds(self, milliseconds: System.Double, ) -> System.DateTimeOffset:
        ...

    @typing.overload
    def AddMinutes(self, minutes: System.Double, ) -> System.DateTimeOffset:
        ...

    @typing.overload
    def AddMonths(self, months: System.Int32, ) -> System.DateTimeOffset:
        ...

    @typing.overload
    def AddSeconds(self, seconds: System.Double, ) -> System.DateTimeOffset:
        ...

    @typing.overload
    def AddTicks(self, ticks: System.Int64, ) -> System.DateTimeOffset:
        ...

    @typing.overload
    def AddYears(self, years: System.Int32, ) -> System.DateTimeOffset:
        ...

    @typing.overload
    @staticmethod
    def Compare(first: System.DateTimeOffset, second: System.DateTimeOffset, ) -> System.Int32:
        ...

    @typing.overload
    def CompareTo(self, other: System.DateTimeOffset, ) -> System.Int32:
        ...

    @typing.overload
    def Equals(self, obj: System.Object, ) -> System.Boolean:
        ...

    @typing.overload
    def Equals(self, other: System.DateTimeOffset, ) -> System.Boolean:
        ...

    @typing.overload
    def EqualsExact(self, other: System.DateTimeOffset, ) -> System.Boolean:
        ...

    @typing.overload
    @staticmethod
    def Equals(first: System.DateTimeOffset, second: System.DateTimeOffset, ) -> System.Boolean:
        ...

    @typing.overload
    @staticmethod
    def FromFileTime(fileTime: System.Int64, ) -> System.DateTimeOffset:
        ...

    @typing.overload
    @staticmethod
    def FromUnixTimeSeconds(seconds: System.Int64, ) -> System.DateTimeOffset:
        ...

    @typing.overload
    @staticmethod
    def FromUnixTimeMilliseconds(milliseconds: System.Int64, ) -> System.DateTimeOffset:
        ...

    @typing.overload
    def GetHashCode(self, ) -> System.Int32:
        ...

    @typing.overload
    @staticmethod
    def Parse(input: System.String, ) -> System.DateTimeOffset:
        ...

    @typing.overload
    @staticmethod
    def Parse(input: System.String, formatProvider: System.IFormatProvider, ) -> System.DateTimeOffset:
        ...

    @typing.overload
    @staticmethod
    def Parse(input: System.String, formatProvider: System.IFormatProvider, styles: System.Globalization.DateTimeStyles, ) -> System.DateTimeOffset:
        ...

    @typing.overload
    @staticmethod
    def Parse(input: System.ReadOnlySpan[System.Char], formatProvider: System.IFormatProvider, styles: System.Globalization.DateTimeStyles, ) -> System.DateTimeOffset:
        ...

    @typing.overload
    @staticmethod
    def ParseExact(input: System.String, format: System.String, formatProvider: System.IFormatProvider, ) -> System.DateTimeOffset:
        ...

    @typing.overload
    @staticmethod
    def ParseExact(input: System.String, format: System.String, formatProvider: System.IFormatProvider, styles: System.Globalization.DateTimeStyles, ) -> System.DateTimeOffset:
        ...

    @typing.overload
    @staticmethod
    def ParseExact(input: System.ReadOnlySpan[System.Char], format: System.ReadOnlySpan[System.Char], formatProvider: System.IFormatProvider, styles: System.Globalization.DateTimeStyles, ) -> System.DateTimeOffset:
        ...

    @typing.overload
    @staticmethod
    def ParseExact(input: System.String, formats: list[System.String], formatProvider: System.IFormatProvider, styles: System.Globalization.DateTimeStyles, ) -> System.DateTimeOffset:
        ...

    @typing.overload
    @staticmethod
    def ParseExact(input: System.ReadOnlySpan[System.Char], formats: list[System.String], formatProvider: System.IFormatProvider, styles: System.Globalization.DateTimeStyles, ) -> System.DateTimeOffset:
        ...

    @typing.overload
    def Subtract(self, value: System.DateTimeOffset, ) -> System.TimeSpan:
        ...

    @typing.overload
    def Subtract(self, value: System.TimeSpan, ) -> System.DateTimeOffset:
        ...

    @typing.overload
    def ToFileTime(self, ) -> System.Int64:
        ...

    @typing.overload
    def ToUnixTimeSeconds(self, ) -> System.Int64:
        ...

    @typing.overload
    def ToUnixTimeMilliseconds(self, ) -> System.Int64:
        ...

    @typing.overload
    def ToLocalTime(self, ) -> System.DateTimeOffset:
        ...

    @typing.overload
    def ToString(self, ) -> System.String:
        ...

    @typing.overload
    def ToString(self, format: System.String, ) -> System.String:
        ...

    @typing.overload
    def ToString(self, formatProvider: System.IFormatProvider, ) -> System.String:
        ...

    @typing.overload
    def ToString(self, format: System.String, formatProvider: System.IFormatProvider, ) -> System.String:
        ...

    @typing.overload
    def TryFormat(self, destination: System.Span[System.Char], charsWritten: ref[System.Int32], format: System.ReadOnlySpan[System.Char], formatProvider: System.IFormatProvider, ) -> System.Boolean:
        ...

    @typing.overload
    def ToUniversalTime(self, ) -> System.DateTimeOffset:
        ...

class ISpanFormattable(System.IFormattable, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    # methods
    @typing.overload
    @abc.abstractmethod
    def TryFormat(self, destination: System.Span[System.Char], charsWritten: ref[System.Int32], format: System.ReadOnlySpan[System.Char], provider: System.IFormatProvider, ) -> System.Boolean:
        ...

class IComparable(abc.ABC, typing.Generic[T]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    # methods
    @typing.overload
    @abc.abstractmethod
    def CompareTo(self, other: T, ) -> System.Int32:
        ...

class IEquatable(abc.ABC, typing.Generic[T]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    # methods
    @typing.overload
    @abc.abstractmethod
    def Equals(self, other: T, ) -> System.Boolean:
        ...

class IBinaryInteger(System.IBinaryNumber[TSelf], System.IBitwiseOperators[TSelf, TSelf, TSelf], System.INumber[TSelf], System.IAdditionOperators[TSelf, TSelf, TSelf], System.IAdditiveIdentity[TSelf, TSelf], System.IComparisonOperators[TSelf, TSelf], System.IComparable, System.IComparable[TSelf], System.IEqualityOperators[TSelf, TSelf], System.IEquatable[TSelf], System.IDecrementOperators[TSelf], System.IDivisionOperators[TSelf, TSelf, TSelf], System.IIncrementOperators[TSelf], System.IModulusOperators[TSelf, TSelf, TSelf], System.IMultiplicativeIdentity[TSelf, TSelf], System.IMultiplyOperators[TSelf, TSelf, TSelf], System.ISpanFormattable, System.IFormattable, System.ISpanParseable[TSelf], System.IParseable[TSelf], System.ISubtractionOperators[TSelf, TSelf, TSelf], System.IUnaryNegationOperators[TSelf, TSelf], System.IUnaryPlusOperators[TSelf, TSelf], System.IShiftOperators[TSelf, TSelf], abc.ABC, typing.Generic[TSelf]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    # methods
    @typing.overload
    @abc.abstractmethod
    @staticmethod
    def LeadingZeroCount(value: TSelf, ) -> TSelf:
        ...

    @typing.overload
    @abc.abstractmethod
    @staticmethod
    def PopCount(value: TSelf, ) -> TSelf:
        ...

    @typing.overload
    @abc.abstractmethod
    @staticmethod
    def RotateLeft(value: TSelf, rotateAmount: System.Int32, ) -> TSelf:
        ...

    @typing.overload
    @abc.abstractmethod
    @staticmethod
    def RotateRight(value: TSelf, rotateAmount: System.Int32, ) -> TSelf:
        ...

    @typing.overload
    @abc.abstractmethod
    @staticmethod
    def TrailingZeroCount(value: TSelf, ) -> TSelf:
        ...

class IBinaryNumber(System.IBitwiseOperators[TSelf, TSelf, TSelf], System.INumber[TSelf], System.IAdditionOperators[TSelf, TSelf, TSelf], System.IAdditiveIdentity[TSelf, TSelf], System.IComparisonOperators[TSelf, TSelf], System.IComparable, System.IComparable[TSelf], System.IEqualityOperators[TSelf, TSelf], System.IEquatable[TSelf], System.IDecrementOperators[TSelf], System.IDivisionOperators[TSelf, TSelf, TSelf], System.IIncrementOperators[TSelf], System.IModulusOperators[TSelf, TSelf, TSelf], System.IMultiplicativeIdentity[TSelf, TSelf], System.IMultiplyOperators[TSelf, TSelf, TSelf], System.ISpanFormattable, System.IFormattable, System.ISpanParseable[TSelf], System.IParseable[TSelf], System.ISubtractionOperators[TSelf, TSelf, TSelf], System.IUnaryNegationOperators[TSelf, TSelf], System.IUnaryPlusOperators[TSelf, TSelf], abc.ABC, typing.Generic[TSelf]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    # methods
    @typing.overload
    @abc.abstractmethod
    @staticmethod
    def IsPow2(value: TSelf, ) -> System.Boolean:
        ...

    @typing.overload
    @abc.abstractmethod
    @staticmethod
    def Log2(value: TSelf, ) -> TSelf:
        ...

class IBitwiseOperators(abc.ABC, typing.Generic[TSelf, TOther, TResult]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    # methods
class INumber(System.IAdditionOperators[TSelf, TSelf, TSelf], System.IAdditiveIdentity[TSelf, TSelf], System.IComparisonOperators[TSelf, TSelf], System.IComparable, System.IComparable[TSelf], System.IEqualityOperators[TSelf, TSelf], System.IEquatable[TSelf], System.IDecrementOperators[TSelf], System.IDivisionOperators[TSelf, TSelf, TSelf], System.IIncrementOperators[TSelf], System.IModulusOperators[TSelf, TSelf, TSelf], System.IMultiplicativeIdentity[TSelf, TSelf], System.IMultiplyOperators[TSelf, TSelf, TSelf], System.ISpanFormattable, System.IFormattable, System.ISpanParseable[TSelf], System.IParseable[TSelf], System.ISubtractionOperators[TSelf, TSelf, TSelf], System.IUnaryNegationOperators[TSelf, TSelf], System.IUnaryPlusOperators[TSelf, TSelf], abc.ABC, typing.Generic[TSelf]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @abc.abstractmethod
    @property
    def One(self) -> TSelf:
        ...

    @abc.abstractmethod
    @property
    def Zero(self) -> TSelf:
        ...

    # methods
    @typing.overload
    @abc.abstractmethod
    @staticmethod
    def Abs(value: TSelf, ) -> TSelf:
        ...

    @typing.overload
    @abc.abstractmethod
    @staticmethod
    def Clamp(value: TSelf, min: TSelf, max: TSelf, ) -> TSelf:
        ...

    @typing.overload
    @abc.abstractmethod
    @staticmethod
    def Create(value: TOther, ) -> TSelf:
        ...

    @typing.overload
    @abc.abstractmethod
    @staticmethod
    def CreateSaturating(value: TOther, ) -> TSelf:
        ...

    @typing.overload
    @abc.abstractmethod
    @staticmethod
    def CreateTruncating(value: TOther, ) -> TSelf:
        ...

    @typing.overload
    @abc.abstractmethod
    @staticmethod
    def DivRem(left: TSelf, right: TSelf, ) -> System.ValueTuple[TSelf, TSelf]:
        ...

    @typing.overload
    @abc.abstractmethod
    @staticmethod
    def Max(x: TSelf, y: TSelf, ) -> TSelf:
        ...

    @typing.overload
    @abc.abstractmethod
    @staticmethod
    def Min(x: TSelf, y: TSelf, ) -> TSelf:
        ...

    @typing.overload
    @abc.abstractmethod
    @staticmethod
    def Parse(s: System.String, style: System.Globalization.NumberStyles, provider: System.IFormatProvider, ) -> TSelf:
        ...

    @typing.overload
    @abc.abstractmethod
    @staticmethod
    def Parse(s: System.ReadOnlySpan[System.Char], style: System.Globalization.NumberStyles, provider: System.IFormatProvider, ) -> TSelf:
        ...

    @typing.overload
    @abc.abstractmethod
    @staticmethod
    def Sign(value: TSelf, ) -> TSelf:
        ...

    @typing.overload
    @abc.abstractmethod
    @staticmethod
    def TryCreate(value: TOther, result: ref[TSelf], ) -> System.Boolean:
        ...

    @typing.overload
    @abc.abstractmethod
    @staticmethod
    def TryParse(s: System.String, style: System.Globalization.NumberStyles, provider: System.IFormatProvider, result: ref[TSelf], ) -> System.Boolean:
        ...

    @typing.overload
    @abc.abstractmethod
    @staticmethod
    def TryParse(s: System.ReadOnlySpan[System.Char], style: System.Globalization.NumberStyles, provider: System.IFormatProvider, result: ref[TSelf], ) -> System.Boolean:
        ...

class IAdditionOperators(abc.ABC, typing.Generic[TSelf, TOther, TResult]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    # methods
class IAdditiveIdentity(abc.ABC, typing.Generic[TSelf, TResult]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @abc.abstractmethod
    @property
    def AdditiveIdentity(self) -> TResult:
        ...

    # methods
class IComparisonOperators(System.IComparable, System.IComparable[TOther], System.IEqualityOperators[TSelf, TOther], System.IEquatable[TOther], abc.ABC, typing.Generic[TSelf, TOther]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    # methods
class IEqualityOperators(System.IEquatable[TOther], abc.ABC, typing.Generic[TSelf, TOther]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    # methods
class IDecrementOperators(abc.ABC, typing.Generic[TSelf]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    # methods
class IDivisionOperators(abc.ABC, typing.Generic[TSelf, TOther, TResult]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    # methods
class IIncrementOperators(abc.ABC, typing.Generic[TSelf]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    # methods
class IModulusOperators(abc.ABC, typing.Generic[TSelf, TOther, TResult]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    # methods
class IMultiplicativeIdentity(abc.ABC, typing.Generic[TSelf, TResult]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @abc.abstractmethod
    @property
    def MultiplicativeIdentity(self) -> TResult:
        ...

    # methods
class IMultiplyOperators(abc.ABC, typing.Generic[TSelf, TOther, TResult]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    # methods
class ISpanParseable(System.IParseable[TSelf], abc.ABC, typing.Generic[TSelf]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    # methods
    @typing.overload
    @abc.abstractmethod
    @staticmethod
    def Parse(s: System.ReadOnlySpan[System.Char], provider: System.IFormatProvider, ) -> TSelf:
        ...

    @typing.overload
    @abc.abstractmethod
    @staticmethod
    def TryParse(s: System.ReadOnlySpan[System.Char], provider: System.IFormatProvider, result: ref[TSelf], ) -> System.Boolean:
        ...

class IParseable(abc.ABC, typing.Generic[TSelf]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    # methods
    @typing.overload
    @abc.abstractmethod
    @staticmethod
    def Parse(s: System.String, provider: System.IFormatProvider, ) -> TSelf:
        ...

    @typing.overload
    @abc.abstractmethod
    @staticmethod
    def TryParse(s: System.String, provider: System.IFormatProvider, result: ref[TSelf], ) -> System.Boolean:
        ...

class ISubtractionOperators(abc.ABC, typing.Generic[TSelf, TOther, TResult]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    # methods
class IUnaryNegationOperators(abc.ABC, typing.Generic[TSelf, TResult]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    # methods
class IUnaryPlusOperators(abc.ABC, typing.Generic[TSelf, TResult]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    # methods
class IShiftOperators(abc.ABC, typing.Generic[TSelf, TResult]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    # methods
class IMinMaxValue(abc.ABC, typing.Generic[TSelf]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @abc.abstractmethod
    @property
    def MinValue(self) -> TSelf:
        ...

    @abc.abstractmethod
    @property
    def MaxValue(self) -> TSelf:
        ...

    # methods
class IUnsignedNumber(System.INumber[TSelf], System.IAdditionOperators[TSelf, TSelf, TSelf], System.IAdditiveIdentity[TSelf, TSelf], System.IComparisonOperators[TSelf, TSelf], System.IComparable, System.IComparable[TSelf], System.IEqualityOperators[TSelf, TSelf], System.IEquatable[TSelf], System.IDecrementOperators[TSelf], System.IDivisionOperators[TSelf, TSelf, TSelf], System.IIncrementOperators[TSelf], System.IModulusOperators[TSelf, TSelf, TSelf], System.IMultiplicativeIdentity[TSelf, TSelf], System.IMultiplyOperators[TSelf, TSelf, TSelf], System.ISpanFormattable, System.IFormattable, System.ISpanParseable[TSelf], System.IParseable[TSelf], System.ISubtractionOperators[TSelf, TSelf, TSelf], System.IUnaryNegationOperators[TSelf, TSelf], System.IUnaryPlusOperators[TSelf, TSelf], abc.ABC, typing.Generic[TSelf]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    # methods
class IFormatProvider(abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    # methods
    @typing.overload
    @abc.abstractmethod
    def GetFormat(self, formatType: System.Type, ) -> System.Object:
        ...

class ReadOnlySpan(System.ValueType, typing.Generic[T]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def Item(self) -> ref[T]:
        ...

    @property
    def Length(self) -> System.Int32:
        ...

    @property
    def IsEmpty(self) -> System.Boolean:
        ...

    @property
    def Empty(self) -> System.ReadOnlySpan:
        ...

    # methods
    @typing.overload
    def __init__(self, array: list[T], ):
        ...

    @typing.overload
    def __init__(self, array: list[T], start: System.Int32, length: System.Int32, ):
        ...

    @typing.overload
    def __init__(self, pointer: ptr[None], length: System.Int32, ):
        ...

    @typing.overload
    def Equals(self, obj: System.Object, ) -> System.Boolean:
        ...

    @typing.overload
    def GetHashCode(self, ) -> System.Int32:
        ...

    @typing.overload
    def GetEnumerator(self, ) -> System.ReadOnlySpan.Enumerator[T]:
        ...

    @typing.overload
    def GetPinnableReference(self, ) -> ref[T]:
        ...

    @typing.overload
    def CopyTo(self, destination: System.Span[T], ) -> None:
        ...

    @typing.overload
    def TryCopyTo(self, destination: System.Span[T], ) -> System.Boolean:
        ...

    @typing.overload
    def ToString(self, ) -> System.String:
        ...

    @typing.overload
    def Slice(self, start: System.Int32, ) -> System.ReadOnlySpan:
        ...

    @typing.overload
    def Slice(self, start: System.Int32, length: System.Int32, ) -> System.ReadOnlySpan:
        ...

    @typing.overload
    def ToArray(self, ) -> list[T]:
        ...

class Char(System.IComparable, System.IComparable[System.Char], System.IEquatable[System.Char], System.IConvertible, System.ISpanFormattable, System.IFormattable, System.IBinaryInteger[System.Char], System.IBinaryNumber[System.Char], System.IBitwiseOperators[System.Char, System.Char, System.Char], System.INumber[System.Char], System.IAdditionOperators[System.Char, System.Char, System.Char], System.IAdditiveIdentity[System.Char, System.Char], System.IComparisonOperators[System.Char, System.Char], System.IEqualityOperators[System.Char, System.Char], System.IDecrementOperators[System.Char], System.IDivisionOperators[System.Char, System.Char, System.Char], System.IIncrementOperators[System.Char], System.IModulusOperators[System.Char, System.Char, System.Char], System.IMultiplicativeIdentity[System.Char, System.Char], System.IMultiplyOperators[System.Char, System.Char, System.Char], System.ISpanParseable[System.Char], System.IParseable[System.Char], System.ISubtractionOperators[System.Char, System.Char, System.Char], System.IUnaryNegationOperators[System.Char, System.Char], System.IUnaryPlusOperators[System.Char, System.Char], System.IShiftOperators[System.Char, System.Char], System.IMinMaxValue[System.Char], System.IUnsignedNumber[System.Char], System.ValueType):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    # methods
    @typing.overload
    @staticmethod
    def IsControl(c: System.Char, ) -> System.Boolean:
        ...

    @typing.overload
    @staticmethod
    def IsControl(s: System.String, index: System.Int32, ) -> System.Boolean:
        ...

    @typing.overload
    @staticmethod
    def IsDigit(s: System.String, index: System.Int32, ) -> System.Boolean:
        ...

    @typing.overload
    @staticmethod
    def IsLetter(s: System.String, index: System.Int32, ) -> System.Boolean:
        ...

    @typing.overload
    @staticmethod
    def IsLetterOrDigit(s: System.String, index: System.Int32, ) -> System.Boolean:
        ...

    @typing.overload
    @staticmethod
    def IsLower(s: System.String, index: System.Int32, ) -> System.Boolean:
        ...

    @typing.overload
    @staticmethod
    def IsNumber(c: System.Char, ) -> System.Boolean:
        ...

    @typing.overload
    @staticmethod
    def IsNumber(s: System.String, index: System.Int32, ) -> System.Boolean:
        ...

    @typing.overload
    @staticmethod
    def IsPunctuation(s: System.String, index: System.Int32, ) -> System.Boolean:
        ...

    @typing.overload
    @staticmethod
    def IsSeparator(c: System.Char, ) -> System.Boolean:
        ...

    @typing.overload
    @staticmethod
    def IsSeparator(s: System.String, index: System.Int32, ) -> System.Boolean:
        ...

    @typing.overload
    @staticmethod
    def IsSurrogate(c: System.Char, ) -> System.Boolean:
        ...

    @typing.overload
    @staticmethod
    def IsSurrogate(s: System.String, index: System.Int32, ) -> System.Boolean:
        ...

    @typing.overload
    @staticmethod
    def IsSymbol(c: System.Char, ) -> System.Boolean:
        ...

    @typing.overload
    @staticmethod
    def IsSymbol(s: System.String, index: System.Int32, ) -> System.Boolean:
        ...

    @typing.overload
    @staticmethod
    def IsUpper(s: System.String, index: System.Int32, ) -> System.Boolean:
        ...

    @typing.overload
    @staticmethod
    def IsWhiteSpace(s: System.String, index: System.Int32, ) -> System.Boolean:
        ...

    @typing.overload
    @staticmethod
    def GetUnicodeCategory(c: System.Char, ) -> System.Globalization.UnicodeCategory:
        ...

    @typing.overload
    @staticmethod
    def GetUnicodeCategory(s: System.String, index: System.Int32, ) -> System.Globalization.UnicodeCategory:
        ...

    @typing.overload
    @staticmethod
    def GetNumericValue(c: System.Char, ) -> System.Double:
        ...

    @typing.overload
    @staticmethod
    def GetNumericValue(s: System.String, index: System.Int32, ) -> System.Double:
        ...

    @typing.overload
    @staticmethod
    def IsHighSurrogate(c: System.Char, ) -> System.Boolean:
        ...

    @typing.overload
    @staticmethod
    def IsHighSurrogate(s: System.String, index: System.Int32, ) -> System.Boolean:
        ...

    @typing.overload
    @staticmethod
    def IsLowSurrogate(c: System.Char, ) -> System.Boolean:
        ...

    @typing.overload
    @staticmethod
    def IsLowSurrogate(s: System.String, index: System.Int32, ) -> System.Boolean:
        ...

    @typing.overload
    @staticmethod
    def IsSurrogatePair(s: System.String, index: System.Int32, ) -> System.Boolean:
        ...

    @typing.overload
    @staticmethod
    def IsSurrogatePair(highSurrogate: System.Char, lowSurrogate: System.Char, ) -> System.Boolean:
        ...

    @typing.overload
    @staticmethod
    def ConvertFromUtf32(utf32: System.Int32, ) -> System.String:
        ...

    @typing.overload
    @staticmethod
    def ConvertToUtf32(highSurrogate: System.Char, lowSurrogate: System.Char, ) -> System.Int32:
        ...

    @typing.overload
    @staticmethod
    def ConvertToUtf32(s: System.String, index: System.Int32, ) -> System.Int32:
        ...

    @typing.overload
    @staticmethod
    def IsAscii(c: System.Char, ) -> System.Boolean:
        ...

    @typing.overload
    def GetHashCode(self, ) -> System.Int32:
        ...

    @typing.overload
    def Equals(self, obj: System.Object, ) -> System.Boolean:
        ...

    @typing.overload
    def Equals(self, obj: System.Char, ) -> System.Boolean:
        ...

    @typing.overload
    def CompareTo(self, value: System.Object, ) -> System.Int32:
        ...

    @typing.overload
    def CompareTo(self, value: System.Char, ) -> System.Int32:
        ...

    @typing.overload
    def ToString(self, ) -> System.String:
        ...

    @typing.overload
    def ToString(self, provider: System.IFormatProvider, ) -> System.String:
        ...

    @typing.overload
    @staticmethod
    def ToString(c: System.Char, ) -> System.String:
        ...

    @typing.overload
    @staticmethod
    def Parse(s: System.String, ) -> System.Char:
        ...

    @typing.overload
    @staticmethod
    def TryParse(s: System.String, result: ref[System.Char], ) -> System.Boolean:
        ...

    @typing.overload
    @staticmethod
    def IsDigit(c: System.Char, ) -> System.Boolean:
        ...

    @typing.overload
    @staticmethod
    def IsLetter(c: System.Char, ) -> System.Boolean:
        ...

    @typing.overload
    @staticmethod
    def IsWhiteSpace(c: System.Char, ) -> System.Boolean:
        ...

    @typing.overload
    @staticmethod
    def IsUpper(c: System.Char, ) -> System.Boolean:
        ...

    @typing.overload
    @staticmethod
    def IsLower(c: System.Char, ) -> System.Boolean:
        ...

    @typing.overload
    @staticmethod
    def IsPunctuation(c: System.Char, ) -> System.Boolean:
        ...

    @typing.overload
    @staticmethod
    def IsLetterOrDigit(c: System.Char, ) -> System.Boolean:
        ...

    @typing.overload
    @staticmethod
    def ToUpper(c: System.Char, culture: System.Globalization.CultureInfo, ) -> System.Char:
        ...

    @typing.overload
    @staticmethod
    def ToUpper(c: System.Char, ) -> System.Char:
        ...

    @typing.overload
    @staticmethod
    def ToUpperInvariant(c: System.Char, ) -> System.Char:
        ...

    @typing.overload
    @staticmethod
    def ToLower(c: System.Char, culture: System.Globalization.CultureInfo, ) -> System.Char:
        ...

    @typing.overload
    @staticmethod
    def ToLower(c: System.Char, ) -> System.Char:
        ...

    @typing.overload
    @staticmethod
    def ToLowerInvariant(c: System.Char, ) -> System.Char:
        ...

    @typing.overload
    def GetTypeCode(self, ) -> System.TypeCode:
        ...

class Span(System.ValueType, typing.Generic[T]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def Item(self) -> ref[T]:
        ...

    @property
    def Length(self) -> System.Int32:
        ...

    @property
    def IsEmpty(self) -> System.Boolean:
        ...

    @property
    def Empty(self) -> System.Span:
        ...

    # methods
    @typing.overload
    def __init__(self, array: list[T], ):
        ...

    @typing.overload
    def __init__(self, array: list[T], start: System.Int32, length: System.Int32, ):
        ...

    @typing.overload
    def __init__(self, pointer: ptr[None], length: System.Int32, ):
        ...

    @typing.overload
    def Equals(self, obj: System.Object, ) -> System.Boolean:
        ...

    @typing.overload
    def GetHashCode(self, ) -> System.Int32:
        ...

    @typing.overload
    def GetEnumerator(self, ) -> System.Span.Enumerator[T]:
        ...

    @typing.overload
    def GetPinnableReference(self, ) -> ref[T]:
        ...

    @typing.overload
    def Clear(self, ) -> None:
        ...

    @typing.overload
    def Fill(self, value: T, ) -> None:
        ...

    @typing.overload
    def CopyTo(self, destination: System.Span, ) -> None:
        ...

    @typing.overload
    def TryCopyTo(self, destination: System.Span, ) -> System.Boolean:
        ...

    @typing.overload
    def ToString(self, ) -> System.String:
        ...

    @typing.overload
    def Slice(self, start: System.Int32, ) -> System.Span:
        ...

    @typing.overload
    def Slice(self, start: System.Int32, length: System.Int32, ) -> System.Span:
        ...

    @typing.overload
    def ToArray(self, ) -> list[T]:
        ...

class TypeCode(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    Empty: System.Int32 = Empty
    Object: System.Int32 = Object
    DBNull: System.Int32 = DBNull
    Boolean: System.Int32 = Boolean
    Char: System.Int32 = Char
    SByte: System.Int32 = SByte
    Byte: System.Int32 = Byte
    Int16: System.Int32 = Int16
    UInt16: System.Int32 = UInt16
    Int32: System.Int32 = Int32
    UInt32: System.Int32 = UInt32
    Int64: System.Int32 = Int64
    UInt64: System.Int32 = UInt64
    Single: System.Int32 = Single
    Double: System.Int32 = Double
    Decimal: System.Int32 = Decimal
    DateTime: System.Int32 = DateTime
    String: System.Int32 = String

class SByte(System.IComparable, System.IConvertible, System.ISpanFormattable, System.IFormattable, System.IComparable[System.SByte], System.IEquatable[System.SByte], System.IBinaryInteger[System.SByte], System.IBinaryNumber[System.SByte], System.IBitwiseOperators[System.SByte, System.SByte, System.SByte], System.INumber[System.SByte], System.IAdditionOperators[System.SByte, System.SByte, System.SByte], System.IAdditiveIdentity[System.SByte, System.SByte], System.IComparisonOperators[System.SByte, System.SByte], System.IEqualityOperators[System.SByte, System.SByte], System.IDecrementOperators[System.SByte], System.IDivisionOperators[System.SByte, System.SByte, System.SByte], System.IIncrementOperators[System.SByte], System.IModulusOperators[System.SByte, System.SByte, System.SByte], System.IMultiplicativeIdentity[System.SByte, System.SByte], System.IMultiplyOperators[System.SByte, System.SByte, System.SByte], System.ISpanParseable[System.SByte], System.IParseable[System.SByte], System.ISubtractionOperators[System.SByte, System.SByte, System.SByte], System.IUnaryNegationOperators[System.SByte, System.SByte], System.IUnaryPlusOperators[System.SByte, System.SByte], System.IShiftOperators[System.SByte, System.SByte], System.IMinMaxValue[System.SByte], System.ISignedNumber[System.SByte], System.ValueType):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    # methods
    @typing.overload
    def CompareTo(self, obj: System.Object, ) -> System.Int32:
        ...

    @typing.overload
    def CompareTo(self, value: System.SByte, ) -> System.Int32:
        ...

    @typing.overload
    def Equals(self, obj: System.Object, ) -> System.Boolean:
        ...

    @typing.overload
    def Equals(self, obj: System.SByte, ) -> System.Boolean:
        ...

    @typing.overload
    def GetHashCode(self, ) -> System.Int32:
        ...

    @typing.overload
    def ToString(self, ) -> System.String:
        ...

    @typing.overload
    def ToString(self, format: System.String, ) -> System.String:
        ...

    @typing.overload
    def ToString(self, provider: System.IFormatProvider, ) -> System.String:
        ...

    @typing.overload
    def ToString(self, format: System.String, provider: System.IFormatProvider, ) -> System.String:
        ...

    @typing.overload
    def TryFormat(self, destination: System.Span[System.Char], charsWritten: ref[System.Int32], format: System.ReadOnlySpan[System.Char], provider: System.IFormatProvider, ) -> System.Boolean:
        ...

    @typing.overload
    @staticmethod
    def Parse(s: System.String, ) -> System.SByte:
        ...

    @typing.overload
    @staticmethod
    def Parse(s: System.String, style: System.Globalization.NumberStyles, ) -> System.SByte:
        ...

    @typing.overload
    @staticmethod
    def Parse(s: System.String, provider: System.IFormatProvider, ) -> System.SByte:
        ...

    @typing.overload
    @staticmethod
    def Parse(s: System.String, style: System.Globalization.NumberStyles, provider: System.IFormatProvider, ) -> System.SByte:
        ...

    @typing.overload
    @staticmethod
    def Parse(s: System.ReadOnlySpan[System.Char], style: System.Globalization.NumberStyles, provider: System.IFormatProvider, ) -> System.SByte:
        ...

    @typing.overload
    @staticmethod
    def TryParse(s: System.String, result: ref[System.SByte], ) -> System.Boolean:
        ...

    @typing.overload
    @staticmethod
    def TryParse(s: System.ReadOnlySpan[System.Char], result: ref[System.SByte], ) -> System.Boolean:
        ...

    @typing.overload
    @staticmethod
    def TryParse(s: System.String, style: System.Globalization.NumberStyles, provider: System.IFormatProvider, result: ref[System.SByte], ) -> System.Boolean:
        ...

    @typing.overload
    @staticmethod
    def TryParse(s: System.ReadOnlySpan[System.Char], style: System.Globalization.NumberStyles, provider: System.IFormatProvider, result: ref[System.SByte], ) -> System.Boolean:
        ...

    @typing.overload
    def GetTypeCode(self, ) -> System.TypeCode:
        ...

class StringComparison(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    CurrentCulture: System.Int32 = CurrentCulture
    CurrentCultureIgnoreCase: System.Int32 = CurrentCultureIgnoreCase
    InvariantCulture: System.Int32 = InvariantCulture
    InvariantCultureIgnoreCase: System.Int32 = InvariantCultureIgnoreCase
    Ordinal: System.Int32 = Ordinal
    OrdinalIgnoreCase: System.Int32 = OrdinalIgnoreCase

class StringSplitOptions(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    None_: System.Int32 = None
    RemoveEmptyEntries: System.Int32 = RemoveEmptyEntries
    TrimEntries: System.Int32 = TrimEntries

class CharEnumerator(System.Collections.IEnumerator, System.Collections.Generic.IEnumerator[System.Char], System.IDisposable, System.ICloneable, System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def Current(self) -> System.Char:
        ...

    # methods
    @typing.overload
    def Clone(self, ) -> System.Object:
        ...

    @typing.overload
    def MoveNext(self, ) -> System.Boolean:
        ...

    @typing.overload
    def Dispose(self, ) -> None:
        ...

    @typing.overload
    def Reset(self, ) -> None:
        ...

class ISignedNumber(System.INumber[TSelf], System.IAdditionOperators[TSelf, TSelf, TSelf], System.IAdditiveIdentity[TSelf, TSelf], System.IComparisonOperators[TSelf, TSelf], System.IComparable, System.IComparable[TSelf], System.IEqualityOperators[TSelf, TSelf], System.IEquatable[TSelf], System.IDecrementOperators[TSelf], System.IDivisionOperators[TSelf, TSelf, TSelf], System.IIncrementOperators[TSelf], System.IModulusOperators[TSelf, TSelf, TSelf], System.IMultiplicativeIdentity[TSelf, TSelf], System.IMultiplyOperators[TSelf, TSelf, TSelf], System.ISpanFormattable, System.IFormattable, System.ISpanParseable[TSelf], System.IParseable[TSelf], System.ISubtractionOperators[TSelf, TSelf, TSelf], System.IUnaryNegationOperators[TSelf, TSelf], System.IUnaryPlusOperators[TSelf, TSelf], abc.ABC, typing.Generic[TSelf]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @abc.abstractmethod
    @property
    def NegativeOne(self) -> TSelf:
        ...

    # methods
class UInt32(System.IComparable, System.IConvertible, System.ISpanFormattable, System.IFormattable, System.IComparable[System.UInt32], System.IEquatable[System.UInt32], System.IBinaryInteger[System.UInt32], System.IBinaryNumber[System.UInt32], System.IBitwiseOperators[System.UInt32, System.UInt32, System.UInt32], System.INumber[System.UInt32], System.IAdditionOperators[System.UInt32, System.UInt32, System.UInt32], System.IAdditiveIdentity[System.UInt32, System.UInt32], System.IComparisonOperators[System.UInt32, System.UInt32], System.IEqualityOperators[System.UInt32, System.UInt32], System.IDecrementOperators[System.UInt32], System.IDivisionOperators[System.UInt32, System.UInt32, System.UInt32], System.IIncrementOperators[System.UInt32], System.IModulusOperators[System.UInt32, System.UInt32, System.UInt32], System.IMultiplicativeIdentity[System.UInt32, System.UInt32], System.IMultiplyOperators[System.UInt32, System.UInt32, System.UInt32], System.ISpanParseable[System.UInt32], System.IParseable[System.UInt32], System.ISubtractionOperators[System.UInt32, System.UInt32, System.UInt32], System.IUnaryNegationOperators[System.UInt32, System.UInt32], System.IUnaryPlusOperators[System.UInt32, System.UInt32], System.IShiftOperators[System.UInt32, System.UInt32], System.IMinMaxValue[System.UInt32], System.IUnsignedNumber[System.UInt32], System.ValueType):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    # methods
    @typing.overload
    def CompareTo(self, value: System.Object, ) -> System.Int32:
        ...

    @typing.overload
    def CompareTo(self, value: System.UInt32, ) -> System.Int32:
        ...

    @typing.overload
    def Equals(self, obj: System.Object, ) -> System.Boolean:
        ...

    @typing.overload
    def Equals(self, obj: System.UInt32, ) -> System.Boolean:
        ...

    @typing.overload
    def GetHashCode(self, ) -> System.Int32:
        ...

    @typing.overload
    def ToString(self, ) -> System.String:
        ...

    @typing.overload
    def ToString(self, provider: System.IFormatProvider, ) -> System.String:
        ...

    @typing.overload
    def ToString(self, format: System.String, ) -> System.String:
        ...

    @typing.overload
    def ToString(self, format: System.String, provider: System.IFormatProvider, ) -> System.String:
        ...

    @typing.overload
    def TryFormat(self, destination: System.Span[System.Char], charsWritten: ref[System.Int32], format: System.ReadOnlySpan[System.Char], provider: System.IFormatProvider, ) -> System.Boolean:
        ...

    @typing.overload
    @staticmethod
    def Parse(s: System.String, ) -> System.UInt32:
        ...

    @typing.overload
    @staticmethod
    def Parse(s: System.String, style: System.Globalization.NumberStyles, ) -> System.UInt32:
        ...

    @typing.overload
    @staticmethod
    def Parse(s: System.String, provider: System.IFormatProvider, ) -> System.UInt32:
        ...

    @typing.overload
    @staticmethod
    def Parse(s: System.String, style: System.Globalization.NumberStyles, provider: System.IFormatProvider, ) -> System.UInt32:
        ...

    @typing.overload
    @staticmethod
    def Parse(s: System.ReadOnlySpan[System.Char], style: System.Globalization.NumberStyles, provider: System.IFormatProvider, ) -> System.UInt32:
        ...

    @typing.overload
    @staticmethod
    def TryParse(s: System.String, result: ref[System.UInt32], ) -> System.Boolean:
        ...

    @typing.overload
    @staticmethod
    def TryParse(s: System.ReadOnlySpan[System.Char], result: ref[System.UInt32], ) -> System.Boolean:
        ...

    @typing.overload
    @staticmethod
    def TryParse(s: System.String, style: System.Globalization.NumberStyles, provider: System.IFormatProvider, result: ref[System.UInt32], ) -> System.Boolean:
        ...

    @typing.overload
    @staticmethod
    def TryParse(s: System.ReadOnlySpan[System.Char], style: System.Globalization.NumberStyles, provider: System.IFormatProvider, result: ref[System.UInt32], ) -> System.Boolean:
        ...

    @typing.overload
    def GetTypeCode(self, ) -> System.TypeCode:
        ...

class UInt64(System.IComparable, System.IConvertible, System.ISpanFormattable, System.IFormattable, System.IComparable[System.UInt64], System.IEquatable[System.UInt64], System.IBinaryInteger[System.UInt64], System.IBinaryNumber[System.UInt64], System.IBitwiseOperators[System.UInt64, System.UInt64, System.UInt64], System.INumber[System.UInt64], System.IAdditionOperators[System.UInt64, System.UInt64, System.UInt64], System.IAdditiveIdentity[System.UInt64, System.UInt64], System.IComparisonOperators[System.UInt64, System.UInt64], System.IEqualityOperators[System.UInt64, System.UInt64], System.IDecrementOperators[System.UInt64], System.IDivisionOperators[System.UInt64, System.UInt64, System.UInt64], System.IIncrementOperators[System.UInt64], System.IModulusOperators[System.UInt64, System.UInt64, System.UInt64], System.IMultiplicativeIdentity[System.UInt64, System.UInt64], System.IMultiplyOperators[System.UInt64, System.UInt64, System.UInt64], System.ISpanParseable[System.UInt64], System.IParseable[System.UInt64], System.ISubtractionOperators[System.UInt64, System.UInt64, System.UInt64], System.IUnaryNegationOperators[System.UInt64, System.UInt64], System.IUnaryPlusOperators[System.UInt64, System.UInt64], System.IShiftOperators[System.UInt64, System.UInt64], System.IMinMaxValue[System.UInt64], System.IUnsignedNumber[System.UInt64], System.ValueType):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    # methods
    @typing.overload
    def CompareTo(self, value: System.Object, ) -> System.Int32:
        ...

    @typing.overload
    def CompareTo(self, value: System.UInt64, ) -> System.Int32:
        ...

    @typing.overload
    def Equals(self, obj: System.Object, ) -> System.Boolean:
        ...

    @typing.overload
    def Equals(self, obj: System.UInt64, ) -> System.Boolean:
        ...

    @typing.overload
    def GetHashCode(self, ) -> System.Int32:
        ...

    @typing.overload
    def ToString(self, ) -> System.String:
        ...

    @typing.overload
    def ToString(self, provider: System.IFormatProvider, ) -> System.String:
        ...

    @typing.overload
    def ToString(self, format: System.String, ) -> System.String:
        ...

    @typing.overload
    def ToString(self, format: System.String, provider: System.IFormatProvider, ) -> System.String:
        ...

    @typing.overload
    def TryFormat(self, destination: System.Span[System.Char], charsWritten: ref[System.Int32], format: System.ReadOnlySpan[System.Char], provider: System.IFormatProvider, ) -> System.Boolean:
        ...

    @typing.overload
    @staticmethod
    def Parse(s: System.String, ) -> System.UInt64:
        ...

    @typing.overload
    @staticmethod
    def Parse(s: System.String, style: System.Globalization.NumberStyles, ) -> System.UInt64:
        ...

    @typing.overload
    @staticmethod
    def Parse(s: System.String, provider: System.IFormatProvider, ) -> System.UInt64:
        ...

    @typing.overload
    @staticmethod
    def Parse(s: System.String, style: System.Globalization.NumberStyles, provider: System.IFormatProvider, ) -> System.UInt64:
        ...

    @typing.overload
    @staticmethod
    def Parse(s: System.ReadOnlySpan[System.Char], style: System.Globalization.NumberStyles, provider: System.IFormatProvider, ) -> System.UInt64:
        ...

    @typing.overload
    @staticmethod
    def TryParse(s: System.String, result: ref[System.UInt64], ) -> System.Boolean:
        ...

    @typing.overload
    @staticmethod
    def TryParse(s: System.ReadOnlySpan[System.Char], result: ref[System.UInt64], ) -> System.Boolean:
        ...

    @typing.overload
    @staticmethod
    def TryParse(s: System.String, style: System.Globalization.NumberStyles, provider: System.IFormatProvider, result: ref[System.UInt64], ) -> System.Boolean:
        ...

    @typing.overload
    @staticmethod
    def TryParse(s: System.ReadOnlySpan[System.Char], style: System.Globalization.NumberStyles, provider: System.IFormatProvider, result: ref[System.UInt64], ) -> System.Boolean:
        ...

    @typing.overload
    def GetTypeCode(self, ) -> System.TypeCode:
        ...

class Single(System.IComparable, System.IConvertible, System.ISpanFormattable, System.IFormattable, System.IComparable[System.Single], System.IEquatable[System.Single], System.IBinaryFloatingPoint[System.Single], System.IBinaryNumber[System.Single], System.IBitwiseOperators[System.Single, System.Single, System.Single], System.INumber[System.Single], System.IAdditionOperators[System.Single, System.Single, System.Single], System.IAdditiveIdentity[System.Single, System.Single], System.IComparisonOperators[System.Single, System.Single], System.IEqualityOperators[System.Single, System.Single], System.IDecrementOperators[System.Single], System.IDivisionOperators[System.Single, System.Single, System.Single], System.IIncrementOperators[System.Single], System.IModulusOperators[System.Single, System.Single, System.Single], System.IMultiplicativeIdentity[System.Single, System.Single], System.IMultiplyOperators[System.Single, System.Single, System.Single], System.ISpanParseable[System.Single], System.IParseable[System.Single], System.ISubtractionOperators[System.Single, System.Single, System.Single], System.IUnaryNegationOperators[System.Single, System.Single], System.IUnaryPlusOperators[System.Single, System.Single], System.IFloatingPoint[System.Single], System.ISignedNumber[System.Single], System.IMinMaxValue[System.Single], System.ValueType):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    # methods
    @typing.overload
    @staticmethod
    def IsFinite(f: System.Single, ) -> System.Boolean:
        ...

    @typing.overload
    @staticmethod
    def IsInfinity(f: System.Single, ) -> System.Boolean:
        ...

    @typing.overload
    @staticmethod
    def IsNaN(f: System.Single, ) -> System.Boolean:
        ...

    @typing.overload
    @staticmethod
    def IsNegative(f: System.Single, ) -> System.Boolean:
        ...

    @typing.overload
    @staticmethod
    def IsNegativeInfinity(f: System.Single, ) -> System.Boolean:
        ...

    @typing.overload
    @staticmethod
    def IsNormal(f: System.Single, ) -> System.Boolean:
        ...

    @typing.overload
    @staticmethod
    def IsPositiveInfinity(f: System.Single, ) -> System.Boolean:
        ...

    @typing.overload
    @staticmethod
    def IsSubnormal(f: System.Single, ) -> System.Boolean:
        ...

    @typing.overload
    def CompareTo(self, value: System.Object, ) -> System.Int32:
        ...

    @typing.overload
    def CompareTo(self, value: System.Single, ) -> System.Int32:
        ...

    @typing.overload
    def Equals(self, obj: System.Object, ) -> System.Boolean:
        ...

    @typing.overload
    def Equals(self, obj: System.Single, ) -> System.Boolean:
        ...

    @typing.overload
    def GetHashCode(self, ) -> System.Int32:
        ...

    @typing.overload
    def ToString(self, ) -> System.String:
        ...

    @typing.overload
    def ToString(self, provider: System.IFormatProvider, ) -> System.String:
        ...

    @typing.overload
    def ToString(self, format: System.String, ) -> System.String:
        ...

    @typing.overload
    def ToString(self, format: System.String, provider: System.IFormatProvider, ) -> System.String:
        ...

    @typing.overload
    def TryFormat(self, destination: System.Span[System.Char], charsWritten: ref[System.Int32], format: System.ReadOnlySpan[System.Char], provider: System.IFormatProvider, ) -> System.Boolean:
        ...

    @typing.overload
    @staticmethod
    def Parse(s: System.String, ) -> System.Single:
        ...

    @typing.overload
    @staticmethod
    def Parse(s: System.String, style: System.Globalization.NumberStyles, ) -> System.Single:
        ...

    @typing.overload
    @staticmethod
    def Parse(s: System.String, provider: System.IFormatProvider, ) -> System.Single:
        ...

    @typing.overload
    @staticmethod
    def Parse(s: System.String, style: System.Globalization.NumberStyles, provider: System.IFormatProvider, ) -> System.Single:
        ...

    @typing.overload
    @staticmethod
    def Parse(s: System.ReadOnlySpan[System.Char], style: System.Globalization.NumberStyles, provider: System.IFormatProvider, ) -> System.Single:
        ...

    @typing.overload
    @staticmethod
    def TryParse(s: System.String, result: ref[System.Single], ) -> System.Boolean:
        ...

    @typing.overload
    @staticmethod
    def TryParse(s: System.ReadOnlySpan[System.Char], result: ref[System.Single], ) -> System.Boolean:
        ...

    @typing.overload
    @staticmethod
    def TryParse(s: System.String, style: System.Globalization.NumberStyles, provider: System.IFormatProvider, result: ref[System.Single], ) -> System.Boolean:
        ...

    @typing.overload
    @staticmethod
    def TryParse(s: System.ReadOnlySpan[System.Char], style: System.Globalization.NumberStyles, provider: System.IFormatProvider, result: ref[System.Single], ) -> System.Boolean:
        ...

    @typing.overload
    def GetTypeCode(self, ) -> System.TypeCode:
        ...

class MidpointRounding(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    ToEven: System.Int32 = ToEven
    AwayFromZero: System.Int32 = AwayFromZero
    ToZero: System.Int32 = ToZero
    ToNegativeInfinity: System.Int32 = ToNegativeInfinity
    ToPositiveInfinity: System.Int32 = ToPositiveInfinity

class Int16(System.IComparable, System.IConvertible, System.ISpanFormattable, System.IFormattable, System.IComparable[System.Int16], System.IEquatable[System.Int16], System.IBinaryInteger[System.Int16], System.IBinaryNumber[System.Int16], System.IBitwiseOperators[System.Int16, System.Int16, System.Int16], System.INumber[System.Int16], System.IAdditionOperators[System.Int16, System.Int16, System.Int16], System.IAdditiveIdentity[System.Int16, System.Int16], System.IComparisonOperators[System.Int16, System.Int16], System.IEqualityOperators[System.Int16, System.Int16], System.IDecrementOperators[System.Int16], System.IDivisionOperators[System.Int16, System.Int16, System.Int16], System.IIncrementOperators[System.Int16], System.IModulusOperators[System.Int16, System.Int16, System.Int16], System.IMultiplicativeIdentity[System.Int16, System.Int16], System.IMultiplyOperators[System.Int16, System.Int16, System.Int16], System.ISpanParseable[System.Int16], System.IParseable[System.Int16], System.ISubtractionOperators[System.Int16, System.Int16, System.Int16], System.IUnaryNegationOperators[System.Int16, System.Int16], System.IUnaryPlusOperators[System.Int16, System.Int16], System.IShiftOperators[System.Int16, System.Int16], System.IMinMaxValue[System.Int16], System.ISignedNumber[System.Int16], System.ValueType):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    # methods
    @typing.overload
    def CompareTo(self, value: System.Object, ) -> System.Int32:
        ...

    @typing.overload
    def CompareTo(self, value: System.Int16, ) -> System.Int32:
        ...

    @typing.overload
    def Equals(self, obj: System.Object, ) -> System.Boolean:
        ...

    @typing.overload
    def Equals(self, obj: System.Int16, ) -> System.Boolean:
        ...

    @typing.overload
    def GetHashCode(self, ) -> System.Int32:
        ...

    @typing.overload
    def ToString(self, ) -> System.String:
        ...

    @typing.overload
    def ToString(self, provider: System.IFormatProvider, ) -> System.String:
        ...

    @typing.overload
    def ToString(self, format: System.String, ) -> System.String:
        ...

    @typing.overload
    def ToString(self, format: System.String, provider: System.IFormatProvider, ) -> System.String:
        ...

    @typing.overload
    def TryFormat(self, destination: System.Span[System.Char], charsWritten: ref[System.Int32], format: System.ReadOnlySpan[System.Char], provider: System.IFormatProvider, ) -> System.Boolean:
        ...

    @typing.overload
    @staticmethod
    def Parse(s: System.String, ) -> System.Int16:
        ...

    @typing.overload
    @staticmethod
    def Parse(s: System.String, style: System.Globalization.NumberStyles, ) -> System.Int16:
        ...

    @typing.overload
    @staticmethod
    def Parse(s: System.String, provider: System.IFormatProvider, ) -> System.Int16:
        ...

    @typing.overload
    @staticmethod
    def Parse(s: System.String, style: System.Globalization.NumberStyles, provider: System.IFormatProvider, ) -> System.Int16:
        ...

    @typing.overload
    @staticmethod
    def Parse(s: System.ReadOnlySpan[System.Char], style: System.Globalization.NumberStyles, provider: System.IFormatProvider, ) -> System.Int16:
        ...

    @typing.overload
    @staticmethod
    def TryParse(s: System.String, result: ref[System.Int16], ) -> System.Boolean:
        ...

    @typing.overload
    @staticmethod
    def TryParse(s: System.ReadOnlySpan[System.Char], result: ref[System.Int16], ) -> System.Boolean:
        ...

    @typing.overload
    @staticmethod
    def TryParse(s: System.String, style: System.Globalization.NumberStyles, provider: System.IFormatProvider, result: ref[System.Int16], ) -> System.Boolean:
        ...

    @typing.overload
    @staticmethod
    def TryParse(s: System.ReadOnlySpan[System.Char], style: System.Globalization.NumberStyles, provider: System.IFormatProvider, result: ref[System.Int16], ) -> System.Boolean:
        ...

    @typing.overload
    def GetTypeCode(self, ) -> System.TypeCode:
        ...

class UInt16(System.IComparable, System.IConvertible, System.ISpanFormattable, System.IFormattable, System.IComparable[System.UInt16], System.IEquatable[System.UInt16], System.IBinaryInteger[System.UInt16], System.IBinaryNumber[System.UInt16], System.IBitwiseOperators[System.UInt16, System.UInt16, System.UInt16], System.INumber[System.UInt16], System.IAdditionOperators[System.UInt16, System.UInt16, System.UInt16], System.IAdditiveIdentity[System.UInt16, System.UInt16], System.IComparisonOperators[System.UInt16, System.UInt16], System.IEqualityOperators[System.UInt16, System.UInt16], System.IDecrementOperators[System.UInt16], System.IDivisionOperators[System.UInt16, System.UInt16, System.UInt16], System.IIncrementOperators[System.UInt16], System.IModulusOperators[System.UInt16, System.UInt16, System.UInt16], System.IMultiplicativeIdentity[System.UInt16, System.UInt16], System.IMultiplyOperators[System.UInt16, System.UInt16, System.UInt16], System.ISpanParseable[System.UInt16], System.IParseable[System.UInt16], System.ISubtractionOperators[System.UInt16, System.UInt16, System.UInt16], System.IUnaryNegationOperators[System.UInt16, System.UInt16], System.IUnaryPlusOperators[System.UInt16, System.UInt16], System.IShiftOperators[System.UInt16, System.UInt16], System.IMinMaxValue[System.UInt16], System.IUnsignedNumber[System.UInt16], System.ValueType):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    # methods
    @typing.overload
    def CompareTo(self, value: System.Object, ) -> System.Int32:
        ...

    @typing.overload
    def CompareTo(self, value: System.UInt16, ) -> System.Int32:
        ...

    @typing.overload
    def Equals(self, obj: System.Object, ) -> System.Boolean:
        ...

    @typing.overload
    def Equals(self, obj: System.UInt16, ) -> System.Boolean:
        ...

    @typing.overload
    def GetHashCode(self, ) -> System.Int32:
        ...

    @typing.overload
    def ToString(self, ) -> System.String:
        ...

    @typing.overload
    def ToString(self, provider: System.IFormatProvider, ) -> System.String:
        ...

    @typing.overload
    def ToString(self, format: System.String, ) -> System.String:
        ...

    @typing.overload
    def ToString(self, format: System.String, provider: System.IFormatProvider, ) -> System.String:
        ...

    @typing.overload
    def TryFormat(self, destination: System.Span[System.Char], charsWritten: ref[System.Int32], format: System.ReadOnlySpan[System.Char], provider: System.IFormatProvider, ) -> System.Boolean:
        ...

    @typing.overload
    @staticmethod
    def Parse(s: System.String, ) -> System.UInt16:
        ...

    @typing.overload
    @staticmethod
    def Parse(s: System.String, style: System.Globalization.NumberStyles, ) -> System.UInt16:
        ...

    @typing.overload
    @staticmethod
    def Parse(s: System.String, provider: System.IFormatProvider, ) -> System.UInt16:
        ...

    @typing.overload
    @staticmethod
    def Parse(s: System.String, style: System.Globalization.NumberStyles, provider: System.IFormatProvider, ) -> System.UInt16:
        ...

    @typing.overload
    @staticmethod
    def Parse(s: System.ReadOnlySpan[System.Char], style: System.Globalization.NumberStyles, provider: System.IFormatProvider, ) -> System.UInt16:
        ...

    @typing.overload
    @staticmethod
    def TryParse(s: System.String, result: ref[System.UInt16], ) -> System.Boolean:
        ...

    @typing.overload
    @staticmethod
    def TryParse(s: System.ReadOnlySpan[System.Char], result: ref[System.UInt16], ) -> System.Boolean:
        ...

    @typing.overload
    @staticmethod
    def TryParse(s: System.String, style: System.Globalization.NumberStyles, provider: System.IFormatProvider, result: ref[System.UInt16], ) -> System.Boolean:
        ...

    @typing.overload
    @staticmethod
    def TryParse(s: System.ReadOnlySpan[System.Char], style: System.Globalization.NumberStyles, provider: System.IFormatProvider, result: ref[System.UInt16], ) -> System.Boolean:
        ...

    @typing.overload
    def GetTypeCode(self, ) -> System.TypeCode:
        ...

class Converter(System.ICloneable, System.Runtime.Serialization.ISerializable, System.MulticastDelegate, typing.Generic[TInput, TOutput]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def Target(self) -> System.Object:
        ...

    @property
    def Method(self) -> System.Reflection.MethodInfo:
        ...

    # methods
    @typing.overload
    def __init__(self, object: System.Object, method: System.IntPtr, ):
        ...

    @typing.overload
    def Invoke(self, input: TInput, ) -> TOutput:
        ...

    @typing.overload
    def BeginInvoke(self, input: TInput, callback: System.AsyncCallback, object: System.Object, ) -> System.IAsyncResult:
        ...

    @typing.overload
    def EndInvoke(self, result: System.IAsyncResult, ) -> TOutput:
        ...

class Predicate(System.ICloneable, System.Runtime.Serialization.ISerializable, System.MulticastDelegate, typing.Generic[T]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def Target(self) -> System.Object:
        ...

    @property
    def Method(self) -> System.Reflection.MethodInfo:
        ...

    # methods
    @typing.overload
    def __init__(self, object: System.Object, method: System.IntPtr, ):
        ...

    @typing.overload
    def Invoke(self, obj: T, ) -> System.Boolean:
        ...

    @typing.overload
    def BeginInvoke(self, obj: T, callback: System.AsyncCallback, object: System.Object, ) -> System.IAsyncResult:
        ...

    @typing.overload
    def EndInvoke(self, result: System.IAsyncResult, ) -> System.Boolean:
        ...

class Action(System.ICloneable, System.Runtime.Serialization.ISerializable, System.MulticastDelegate, typing.Generic[T]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def Target(self) -> System.Object:
        ...

    @property
    def Method(self) -> System.Reflection.MethodInfo:
        ...

    # methods
    @typing.overload
    def __init__(self, object: System.Object, method: System.IntPtr, ):
        ...

    @typing.overload
    def Invoke(self, obj: T, ) -> None:
        ...

    @typing.overload
    def BeginInvoke(self, obj: T, callback: System.AsyncCallback, object: System.Object, ) -> System.IAsyncResult:
        ...

    @typing.overload
    def EndInvoke(self, result: System.IAsyncResult, ) -> None:
        ...

class Comparison(System.ICloneable, System.Runtime.Serialization.ISerializable, System.MulticastDelegate, typing.Generic[T]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def Target(self) -> System.Object:
        ...

    @property
    def Method(self) -> System.Reflection.MethodInfo:
        ...

    # methods
    @typing.overload
    def __init__(self, object: System.Object, method: System.IntPtr, ):
        ...

    @typing.overload
    def Invoke(self, x: T, y: T, ) -> System.Int32:
        ...

    @typing.overload
    def BeginInvoke(self, x: T, y: T, callback: System.AsyncCallback, object: System.Object, ) -> System.IAsyncResult:
        ...

    @typing.overload
    def EndInvoke(self, result: System.IAsyncResult, ) -> System.Int32:
        ...

class Array(System.ICloneable, System.Collections.IList, System.Collections.ICollection, System.Collections.IEnumerable, System.Collections.IStructuralComparable, System.Collections.IStructuralEquatable, System.Object, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def Length(self) -> System.Int32:
        ...

    @property
    def LongLength(self) -> System.Int64:
        ...

    @property
    def Rank(self) -> System.Int32:
        ...

    @property
    def SyncRoot(self) -> System.Object:
        ...

    @property
    def IsReadOnly(self) -> System.Boolean:
        ...

    @property
    def IsFixedSize(self) -> System.Boolean:
        ...

    @property
    def IsSynchronized(self) -> System.Boolean:
        ...

    @property
    def MaxLength(self) -> System.Int32:
        ...

    # methods
    @typing.overload
    def CopyTo(self, array: System.Array, index: System.Int32, ) -> None:
        ...

    @typing.overload
    def CopyTo(self, array: System.Array, index: System.Int64, ) -> None:
        ...

    @typing.overload
    @staticmethod
    def Empty() -> list[T]:
        ...

    @typing.overload
    @staticmethod
    def Exists(array: list[T], match: System.Predicate[T], ) -> System.Boolean:
        ...

    @typing.overload
    @staticmethod
    def Fill(array: list[T], value: T, ) -> None:
        ...

    @typing.overload
    @staticmethod
    def Fill(array: list[T], value: T, startIndex: System.Int32, count: System.Int32, ) -> None:
        ...

    @typing.overload
    @staticmethod
    def Find(array: list[T], match: System.Predicate[T], ) -> T:
        ...

    @typing.overload
    @staticmethod
    def FindAll(array: list[T], match: System.Predicate[T], ) -> list[T]:
        ...

    @typing.overload
    @staticmethod
    def FindIndex(array: list[T], match: System.Predicate[T], ) -> System.Int32:
        ...

    @typing.overload
    @staticmethod
    def FindIndex(array: list[T], startIndex: System.Int32, match: System.Predicate[T], ) -> System.Int32:
        ...

    @typing.overload
    @staticmethod
    def FindIndex(array: list[T], startIndex: System.Int32, count: System.Int32, match: System.Predicate[T], ) -> System.Int32:
        ...

    @typing.overload
    @staticmethod
    def FindLast(array: list[T], match: System.Predicate[T], ) -> T:
        ...

    @typing.overload
    @staticmethod
    def FindLastIndex(array: list[T], match: System.Predicate[T], ) -> System.Int32:
        ...

    @typing.overload
    @staticmethod
    def FindLastIndex(array: list[T], startIndex: System.Int32, match: System.Predicate[T], ) -> System.Int32:
        ...

    @typing.overload
    @staticmethod
    def FindLastIndex(array: list[T], startIndex: System.Int32, count: System.Int32, match: System.Predicate[T], ) -> System.Int32:
        ...

    @typing.overload
    @staticmethod
    def ForEach(array: list[T], action: System.Action[T], ) -> None:
        ...

    @typing.overload
    @staticmethod
    def IndexOf(array: System.Array, value: System.Object, ) -> System.Int32:
        ...

    @typing.overload
    @staticmethod
    def IndexOf(array: System.Array, value: System.Object, startIndex: System.Int32, ) -> System.Int32:
        ...

    @typing.overload
    @staticmethod
    def IndexOf(array: System.Array, value: System.Object, startIndex: System.Int32, count: System.Int32, ) -> System.Int32:
        ...

    @typing.overload
    @staticmethod
    def IndexOf(array: list[T], value: T, ) -> System.Int32:
        ...

    @typing.overload
    @staticmethod
    def IndexOf(array: list[T], value: T, startIndex: System.Int32, ) -> System.Int32:
        ...

    @typing.overload
    @staticmethod
    def IndexOf(array: list[T], value: T, startIndex: System.Int32, count: System.Int32, ) -> System.Int32:
        ...

    @typing.overload
    @staticmethod
    def LastIndexOf(array: System.Array, value: System.Object, ) -> System.Int32:
        ...

    @typing.overload
    @staticmethod
    def LastIndexOf(array: System.Array, value: System.Object, startIndex: System.Int32, ) -> System.Int32:
        ...

    @typing.overload
    @staticmethod
    def LastIndexOf(array: System.Array, value: System.Object, startIndex: System.Int32, count: System.Int32, ) -> System.Int32:
        ...

    @typing.overload
    @staticmethod
    def LastIndexOf(array: list[T], value: T, ) -> System.Int32:
        ...

    @typing.overload
    @staticmethod
    def LastIndexOf(array: list[T], value: T, startIndex: System.Int32, ) -> System.Int32:
        ...

    @typing.overload
    @staticmethod
    def LastIndexOf(array: list[T], value: T, startIndex: System.Int32, count: System.Int32, ) -> System.Int32:
        ...

    @typing.overload
    @staticmethod
    def Reverse(array: System.Array, ) -> None:
        ...

    @typing.overload
    @staticmethod
    def Reverse(array: System.Array, index: System.Int32, length: System.Int32, ) -> None:
        ...

    @typing.overload
    @staticmethod
    def Reverse(array: list[T], ) -> None:
        ...

    @typing.overload
    @staticmethod
    def Reverse(array: list[T], index: System.Int32, length: System.Int32, ) -> None:
        ...

    @typing.overload
    @staticmethod
    def Sort(array: System.Array, ) -> None:
        ...

    @typing.overload
    @staticmethod
    def Sort(keys: System.Array, items: System.Array, ) -> None:
        ...

    @typing.overload
    @staticmethod
    def Sort(array: System.Array, index: System.Int32, length: System.Int32, ) -> None:
        ...

    @typing.overload
    @staticmethod
    def Sort(keys: System.Array, items: System.Array, index: System.Int32, length: System.Int32, ) -> None:
        ...

    @typing.overload
    @staticmethod
    def Sort(array: System.Array, comparer: System.Collections.IComparer, ) -> None:
        ...

    @typing.overload
    @staticmethod
    def Sort(keys: System.Array, items: System.Array, comparer: System.Collections.IComparer, ) -> None:
        ...

    @typing.overload
    @staticmethod
    def Sort(array: System.Array, index: System.Int32, length: System.Int32, comparer: System.Collections.IComparer, ) -> None:
        ...

    @typing.overload
    @staticmethod
    def Sort(keys: System.Array, items: System.Array, index: System.Int32, length: System.Int32, comparer: System.Collections.IComparer, ) -> None:
        ...

    @typing.overload
    @staticmethod
    def Sort(array: list[T], ) -> None:
        ...

    @typing.overload
    @staticmethod
    def Sort(keys: list[TKey], items: list[TValue], ) -> None:
        ...

    @typing.overload
    @staticmethod
    def Sort(array: list[T], index: System.Int32, length: System.Int32, ) -> None:
        ...

    @typing.overload
    @staticmethod
    def Sort(keys: list[TKey], items: list[TValue], index: System.Int32, length: System.Int32, ) -> None:
        ...

    @typing.overload
    @staticmethod
    def Sort(array: list[T], comparer: System.Collections.Generic.IComparer[T], ) -> None:
        ...

    @typing.overload
    @staticmethod
    def Sort(keys: list[TKey], items: list[TValue], comparer: System.Collections.Generic.IComparer[TKey], ) -> None:
        ...

    @typing.overload
    @staticmethod
    def Sort(array: list[T], index: System.Int32, length: System.Int32, comparer: System.Collections.Generic.IComparer[T], ) -> None:
        ...

    @typing.overload
    @staticmethod
    def Sort(keys: list[TKey], items: list[TValue], index: System.Int32, length: System.Int32, comparer: System.Collections.Generic.IComparer[TKey], ) -> None:
        ...

    @typing.overload
    @staticmethod
    def Sort(array: list[T], comparison: System.Comparison[T], ) -> None:
        ...

    @typing.overload
    @staticmethod
    def TrueForAll(array: list[T], match: System.Predicate[T], ) -> System.Boolean:
        ...

    @typing.overload
    def GetEnumerator(self, ) -> System.Collections.IEnumerator:
        ...

    @typing.overload
    @staticmethod
    def CreateInstance(elementType: System.Type, length: System.Int32, ) -> System.Array:
        ...

    @typing.overload
    @staticmethod
    def CreateInstance(elementType: System.Type, length1: System.Int32, length2: System.Int32, ) -> System.Array:
        ...

    @typing.overload
    @staticmethod
    def CreateInstance(elementType: System.Type, length1: System.Int32, length2: System.Int32, length3: System.Int32, ) -> System.Array:
        ...

    @typing.overload
    @staticmethod
    def CreateInstance(elementType: System.Type, lengths: list[System.Int32], ) -> System.Array:
        ...

    @typing.overload
    @staticmethod
    def CreateInstance(elementType: System.Type, lengths: list[System.Int32], lowerBounds: list[System.Int32], ) -> System.Array:
        ...

    @typing.overload
    @staticmethod
    def Copy(sourceArray: System.Array, destinationArray: System.Array, length: System.Int32, ) -> None:
        ...

    @typing.overload
    @staticmethod
    def Copy(sourceArray: System.Array, sourceIndex: System.Int32, destinationArray: System.Array, destinationIndex: System.Int32, length: System.Int32, ) -> None:
        ...

    @typing.overload
    @staticmethod
    def ConstrainedCopy(sourceArray: System.Array, sourceIndex: System.Int32, destinationArray: System.Array, destinationIndex: System.Int32, length: System.Int32, ) -> None:
        ...

    @typing.overload
    @staticmethod
    def Clear(array: System.Array, ) -> None:
        ...

    @typing.overload
    @staticmethod
    def Clear(array: System.Array, index: System.Int32, length: System.Int32, ) -> None:
        ...

    @typing.overload
    def GetLength(self, dimension: System.Int32, ) -> System.Int32:
        ...

    @typing.overload
    def GetUpperBound(self, dimension: System.Int32, ) -> System.Int32:
        ...

    @typing.overload
    def GetLowerBound(self, dimension: System.Int32, ) -> System.Int32:
        ...

    @typing.overload
    def Initialize(self, ) -> None:
        ...

    @typing.overload
    @staticmethod
    def AsReadOnly(array: list[T], ) -> System.Collections.ObjectModel.ReadOnlyCollection[T]:
        ...

    @typing.overload
    @staticmethod
    def Resize(array: ref[list[T]], newSize: System.Int32, ) -> None:
        ...

    @typing.overload
    @staticmethod
    def CreateInstance(elementType: System.Type, lengths: list[System.Int64], ) -> System.Array:
        ...

    @typing.overload
    @staticmethod
    def Copy(sourceArray: System.Array, destinationArray: System.Array, length: System.Int64, ) -> None:
        ...

    @typing.overload
    @staticmethod
    def Copy(sourceArray: System.Array, sourceIndex: System.Int64, destinationArray: System.Array, destinationIndex: System.Int64, length: System.Int64, ) -> None:
        ...

    @typing.overload
    def GetValue(self, indices: list[System.Int32], ) -> System.Object:
        ...

    @typing.overload
    def GetValue(self, index: System.Int32, ) -> System.Object:
        ...

    @typing.overload
    def GetValue(self, index1: System.Int32, index2: System.Int32, ) -> System.Object:
        ...

    @typing.overload
    def GetValue(self, index1: System.Int32, index2: System.Int32, index3: System.Int32, ) -> System.Object:
        ...

    @typing.overload
    def SetValue(self, value: System.Object, index: System.Int32, ) -> None:
        ...

    @typing.overload
    def SetValue(self, value: System.Object, index1: System.Int32, index2: System.Int32, ) -> None:
        ...

    @typing.overload
    def SetValue(self, value: System.Object, index1: System.Int32, index2: System.Int32, index3: System.Int32, ) -> None:
        ...

    @typing.overload
    def SetValue(self, value: System.Object, indices: list[System.Int32], ) -> None:
        ...

    @typing.overload
    def GetValue(self, index: System.Int64, ) -> System.Object:
        ...

    @typing.overload
    def GetValue(self, index1: System.Int64, index2: System.Int64, ) -> System.Object:
        ...

    @typing.overload
    def GetValue(self, index1: System.Int64, index2: System.Int64, index3: System.Int64, ) -> System.Object:
        ...

    @typing.overload
    def GetValue(self, indices: list[System.Int64], ) -> System.Object:
        ...

    @typing.overload
    def SetValue(self, value: System.Object, index: System.Int64, ) -> None:
        ...

    @typing.overload
    def SetValue(self, value: System.Object, index1: System.Int64, index2: System.Int64, ) -> None:
        ...

    @typing.overload
    def SetValue(self, value: System.Object, index1: System.Int64, index2: System.Int64, index3: System.Int64, ) -> None:
        ...

    @typing.overload
    def SetValue(self, value: System.Object, indices: list[System.Int64], ) -> None:
        ...

    @typing.overload
    def GetLongLength(self, dimension: System.Int32, ) -> System.Int64:
        ...

    @typing.overload
    def Clone(self, ) -> System.Object:
        ...

    @typing.overload
    @staticmethod
    def BinarySearch(array: System.Array, value: System.Object, ) -> System.Int32:
        ...

    @typing.overload
    @staticmethod
    def BinarySearch(array: System.Array, index: System.Int32, length: System.Int32, value: System.Object, ) -> System.Int32:
        ...

    @typing.overload
    @staticmethod
    def BinarySearch(array: System.Array, value: System.Object, comparer: System.Collections.IComparer, ) -> System.Int32:
        ...

    @typing.overload
    @staticmethod
    def BinarySearch(array: System.Array, index: System.Int32, length: System.Int32, value: System.Object, comparer: System.Collections.IComparer, ) -> System.Int32:
        ...

    @typing.overload
    @staticmethod
    def BinarySearch(array: list[T], value: T, ) -> System.Int32:
        ...

    @typing.overload
    @staticmethod
    def BinarySearch(array: list[T], value: T, comparer: System.Collections.Generic.IComparer[T], ) -> System.Int32:
        ...

    @typing.overload
    @staticmethod
    def BinarySearch(array: list[T], index: System.Int32, length: System.Int32, value: T, ) -> System.Int32:
        ...

    @typing.overload
    @staticmethod
    def BinarySearch(array: list[T], index: System.Int32, length: System.Int32, value: T, comparer: System.Collections.Generic.IComparer[T], ) -> System.Int32:
        ...

    @typing.overload
    @staticmethod
    def ConvertAll(array: list[TInput], converter: System.Converter[TInput, TOutput], ) -> list[TOutput]:
        ...

class TimeSpan(System.IComparable, System.IComparable[System.TimeSpan], System.IEquatable[System.TimeSpan], System.ISpanFormattable, System.IFormattable, System.IAdditionOperators[System.TimeSpan, System.TimeSpan, System.TimeSpan], System.IAdditiveIdentity[System.TimeSpan, System.TimeSpan], System.IComparisonOperators[System.TimeSpan, System.TimeSpan], System.IEqualityOperators[System.TimeSpan, System.TimeSpan], System.IDivisionOperators[System.TimeSpan, System.Double, System.TimeSpan], System.IDivisionOperators[System.TimeSpan, System.TimeSpan, System.Double], System.IMinMaxValue[System.TimeSpan], System.IMultiplyOperators[System.TimeSpan, System.Double, System.TimeSpan], System.IMultiplicativeIdentity[System.TimeSpan, System.Double], System.ISpanParseable[System.TimeSpan], System.IParseable[System.TimeSpan], System.ISubtractionOperators[System.TimeSpan, System.TimeSpan, System.TimeSpan], System.IUnaryNegationOperators[System.TimeSpan, System.TimeSpan], System.IUnaryPlusOperators[System.TimeSpan, System.TimeSpan], System.ValueType):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def Ticks(self) -> System.Int64:
        ...

    @property
    def Days(self) -> System.Int32:
        ...

    @property
    def Hours(self) -> System.Int32:
        ...

    @property
    def Milliseconds(self) -> System.Int32:
        ...

    @property
    def Minutes(self) -> System.Int32:
        ...

    @property
    def Seconds(self) -> System.Int32:
        ...

    @property
    def TotalDays(self) -> System.Double:
        ...

    @property
    def TotalHours(self) -> System.Double:
        ...

    @property
    def TotalMilliseconds(self) -> System.Double:
        ...

    @property
    def TotalMinutes(self) -> System.Double:
        ...

    @property
    def TotalSeconds(self) -> System.Double:
        ...

    # methods
    @typing.overload
    def __init__(self, ticks: System.Int64, ):
        ...

    @typing.overload
    def __init__(self, hours: System.Int32, minutes: System.Int32, seconds: System.Int32, ):
        ...

    @typing.overload
    def __init__(self, days: System.Int32, hours: System.Int32, minutes: System.Int32, seconds: System.Int32, ):
        ...

    @typing.overload
    def __init__(self, days: System.Int32, hours: System.Int32, minutes: System.Int32, seconds: System.Int32, milliseconds: System.Int32, ):
        ...

    @typing.overload
    def Add(self, ts: System.TimeSpan, ) -> System.TimeSpan:
        ...

    @typing.overload
    @staticmethod
    def Compare(t1: System.TimeSpan, t2: System.TimeSpan, ) -> System.Int32:
        ...

    @typing.overload
    def CompareTo(self, value: System.Object, ) -> System.Int32:
        ...

    @typing.overload
    def CompareTo(self, value: System.TimeSpan, ) -> System.Int32:
        ...

    @typing.overload
    @staticmethod
    def FromDays(value: System.Double, ) -> System.TimeSpan:
        ...

    @typing.overload
    def Duration(self, ) -> System.TimeSpan:
        ...

    @typing.overload
    def Equals(self, value: System.Object, ) -> System.Boolean:
        ...

    @typing.overload
    def Equals(self, obj: System.TimeSpan, ) -> System.Boolean:
        ...

    @typing.overload
    @staticmethod
    def Equals(t1: System.TimeSpan, t2: System.TimeSpan, ) -> System.Boolean:
        ...

    @typing.overload
    def GetHashCode(self, ) -> System.Int32:
        ...

    @typing.overload
    @staticmethod
    def FromHours(value: System.Double, ) -> System.TimeSpan:
        ...

    @typing.overload
    @staticmethod
    def FromMilliseconds(value: System.Double, ) -> System.TimeSpan:
        ...

    @typing.overload
    @staticmethod
    def FromMinutes(value: System.Double, ) -> System.TimeSpan:
        ...

    @typing.overload
    def Negate(self, ) -> System.TimeSpan:
        ...

    @typing.overload
    @staticmethod
    def FromSeconds(value: System.Double, ) -> System.TimeSpan:
        ...

    @typing.overload
    def Subtract(self, ts: System.TimeSpan, ) -> System.TimeSpan:
        ...

    @typing.overload
    def Multiply(self, factor: System.Double, ) -> System.TimeSpan:
        ...

    @typing.overload
    def Divide(self, divisor: System.Double, ) -> System.TimeSpan:
        ...

    @typing.overload
    def Divide(self, ts: System.TimeSpan, ) -> System.Double:
        ...

    @typing.overload
    @staticmethod
    def FromTicks(value: System.Int64, ) -> System.TimeSpan:
        ...

    @typing.overload
    @staticmethod
    def Parse(s: System.String, ) -> System.TimeSpan:
        ...

    @typing.overload
    @staticmethod
    def Parse(input: System.String, formatProvider: System.IFormatProvider, ) -> System.TimeSpan:
        ...

    @typing.overload
    @staticmethod
    def Parse(input: System.ReadOnlySpan[System.Char], formatProvider: System.IFormatProvider, ) -> System.TimeSpan:
        ...

    @typing.overload
    @staticmethod
    def ParseExact(input: System.String, format: System.String, formatProvider: System.IFormatProvider, ) -> System.TimeSpan:
        ...

    @typing.overload
    @staticmethod
    def ParseExact(input: System.String, formats: list[System.String], formatProvider: System.IFormatProvider, ) -> System.TimeSpan:
        ...

    @typing.overload
    @staticmethod
    def ParseExact(input: System.String, format: System.String, formatProvider: System.IFormatProvider, styles: System.Globalization.TimeSpanStyles, ) -> System.TimeSpan:
        ...

    @typing.overload
    @staticmethod
    def ParseExact(input: System.ReadOnlySpan[System.Char], format: System.ReadOnlySpan[System.Char], formatProvider: System.IFormatProvider, styles: System.Globalization.TimeSpanStyles, ) -> System.TimeSpan:
        ...

    @typing.overload
    @staticmethod
    def ParseExact(input: System.String, formats: list[System.String], formatProvider: System.IFormatProvider, styles: System.Globalization.TimeSpanStyles, ) -> System.TimeSpan:
        ...

    @typing.overload
    @staticmethod
    def ParseExact(input: System.ReadOnlySpan[System.Char], formats: list[System.String], formatProvider: System.IFormatProvider, styles: System.Globalization.TimeSpanStyles, ) -> System.TimeSpan:
        ...

    @typing.overload
    @staticmethod
    def TryParse(s: System.String, result: ref[System.TimeSpan], ) -> System.Boolean:
        ...

    @typing.overload
    @staticmethod
    def TryParse(s: System.ReadOnlySpan[System.Char], result: ref[System.TimeSpan], ) -> System.Boolean:
        ...

    @typing.overload
    @staticmethod
    def TryParse(input: System.String, formatProvider: System.IFormatProvider, result: ref[System.TimeSpan], ) -> System.Boolean:
        ...

    @typing.overload
    @staticmethod
    def TryParse(input: System.ReadOnlySpan[System.Char], formatProvider: System.IFormatProvider, result: ref[System.TimeSpan], ) -> System.Boolean:
        ...

    @typing.overload
    @staticmethod
    def TryParseExact(input: System.String, format: System.String, formatProvider: System.IFormatProvider, result: ref[System.TimeSpan], ) -> System.Boolean:
        ...

    @typing.overload
    @staticmethod
    def TryParseExact(input: System.ReadOnlySpan[System.Char], format: System.ReadOnlySpan[System.Char], formatProvider: System.IFormatProvider, result: ref[System.TimeSpan], ) -> System.Boolean:
        ...

    @typing.overload
    @staticmethod
    def TryParseExact(input: System.String, formats: list[System.String], formatProvider: System.IFormatProvider, result: ref[System.TimeSpan], ) -> System.Boolean:
        ...

    @typing.overload
    @staticmethod
    def TryParseExact(input: System.ReadOnlySpan[System.Char], formats: list[System.String], formatProvider: System.IFormatProvider, result: ref[System.TimeSpan], ) -> System.Boolean:
        ...

    @typing.overload
    @staticmethod
    def TryParseExact(input: System.String, format: System.String, formatProvider: System.IFormatProvider, styles: System.Globalization.TimeSpanStyles, result: ref[System.TimeSpan], ) -> System.Boolean:
        ...

    @typing.overload
    @staticmethod
    def TryParseExact(input: System.ReadOnlySpan[System.Char], format: System.ReadOnlySpan[System.Char], formatProvider: System.IFormatProvider, styles: System.Globalization.TimeSpanStyles, result: ref[System.TimeSpan], ) -> System.Boolean:
        ...

    @typing.overload
    @staticmethod
    def TryParseExact(input: System.String, formats: list[System.String], formatProvider: System.IFormatProvider, styles: System.Globalization.TimeSpanStyles, result: ref[System.TimeSpan], ) -> System.Boolean:
        ...

    @typing.overload
    @staticmethod
    def TryParseExact(input: System.ReadOnlySpan[System.Char], formats: list[System.String], formatProvider: System.IFormatProvider, styles: System.Globalization.TimeSpanStyles, result: ref[System.TimeSpan], ) -> System.Boolean:
        ...

    @typing.overload
    def ToString(self, ) -> System.String:
        ...

    @typing.overload
    def ToString(self, format: System.String, ) -> System.String:
        ...

    @typing.overload
    def ToString(self, format: System.String, formatProvider: System.IFormatProvider, ) -> System.String:
        ...

    @typing.overload
    def TryFormat(self, destination: System.Span[System.Char], charsWritten: ref[System.Int32], format: System.ReadOnlySpan[System.Char], formatProvider: System.IFormatProvider, ) -> System.Boolean:
        ...

class DayOfWeek(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    Sunday: System.Int32 = Sunday
    Monday: System.Int32 = Monday
    Tuesday: System.Int32 = Tuesday
    Wednesday: System.Int32 = Wednesday
    Thursday: System.Int32 = Thursday
    Friday: System.Int32 = Friday
    Saturday: System.Int32 = Saturday

class DateTimeKind(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    Unspecified: System.Int32 = Unspecified
    Utc: System.Int32 = Utc
    Local: System.Int32 = Local

class Delegate(System.ICloneable, System.Runtime.Serialization.ISerializable, System.Object, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def Target(self) -> System.Object:
        ...

    @property
    def Method(self) -> System.Reflection.MethodInfo:
        ...

    # methods
    @typing.overload
    def GetObjectData(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext, ) -> None:
        ...

    @typing.overload
    def Equals(self, obj: System.Object, ) -> System.Boolean:
        ...

    @typing.overload
    def GetInvocationList(self, ) -> list[System.Delegate]:
        ...

    @typing.overload
    def GetHashCode(self, ) -> System.Int32:
        ...

    @typing.overload
    @staticmethod
    def CreateDelegate(type: System.Type, target: System.Object, method: System.String, ignoreCase: System.Boolean, throwOnBindFailure: System.Boolean, ) -> System.Delegate:
        ...

    @typing.overload
    @staticmethod
    def CreateDelegate(type: System.Type, target: System.Type, method: System.String, ignoreCase: System.Boolean, throwOnBindFailure: System.Boolean, ) -> System.Delegate:
        ...

    @typing.overload
    @staticmethod
    def CreateDelegate(type: System.Type, method: System.Reflection.MethodInfo, throwOnBindFailure: System.Boolean, ) -> System.Delegate:
        ...

    @typing.overload
    @staticmethod
    def CreateDelegate(type: System.Type, firstArgument: System.Object, method: System.Reflection.MethodInfo, throwOnBindFailure: System.Boolean, ) -> System.Delegate:
        ...

    @typing.overload
    def Clone(self, ) -> System.Object:
        ...

    @typing.overload
    @staticmethod
    def Combine(a: System.Delegate, b: System.Delegate, ) -> System.Delegate:
        ...

    @typing.overload
    @staticmethod
    def Combine(delegates: list[System.Delegate], ) -> System.Delegate:
        ...

    @typing.overload
    @staticmethod
    def CreateDelegate(type: System.Type, firstArgument: System.Object, method: System.Reflection.MethodInfo, ) -> System.Delegate:
        ...

    @typing.overload
    @staticmethod
    def CreateDelegate(type: System.Type, method: System.Reflection.MethodInfo, ) -> System.Delegate:
        ...

    @typing.overload
    @staticmethod
    def CreateDelegate(type: System.Type, target: System.Object, method: System.String, ) -> System.Delegate:
        ...

    @typing.overload
    @staticmethod
    def CreateDelegate(type: System.Type, target: System.Object, method: System.String, ignoreCase: System.Boolean, ) -> System.Delegate:
        ...

    @typing.overload
    @staticmethod
    def CreateDelegate(type: System.Type, target: System.Type, method: System.String, ) -> System.Delegate:
        ...

    @typing.overload
    @staticmethod
    def CreateDelegate(type: System.Type, target: System.Type, method: System.String, ignoreCase: System.Boolean, ) -> System.Delegate:
        ...

    @typing.overload
    def DynamicInvoke(self, args: list[System.Object], ) -> System.Object:
        ...

    @typing.overload
    @staticmethod
    def Remove(source: System.Delegate, value: System.Delegate, ) -> System.Delegate:
        ...

    @typing.overload
    @staticmethod
    def RemoveAll(source: System.Delegate, value: System.Delegate, ) -> System.Delegate:
        ...

class RuntimeMethodHandle(System.Runtime.Serialization.ISerializable, System.ValueType):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def Value(self) -> System.IntPtr:
        ...

    # methods
    @typing.overload
    def GetObjectData(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext, ) -> None:
        ...

    @typing.overload
    def GetHashCode(self, ) -> System.Int32:
        ...

    @typing.overload
    def Equals(self, obj: System.Object, ) -> System.Boolean:
        ...

    @typing.overload
    def Equals(self, handle: System.RuntimeMethodHandle, ) -> System.Boolean:
        ...

    @typing.overload
    def GetFunctionPointer(self, ) -> System.IntPtr:
        ...

class RuntimeTypeHandle(System.Runtime.Serialization.ISerializable, System.ValueType):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def Value(self) -> System.IntPtr:
        ...

    # methods
    @typing.overload
    def GetObjectData(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext, ) -> None:
        ...

    @typing.overload
    def GetHashCode(self, ) -> System.Int32:
        ...

    @typing.overload
    def Equals(self, obj: System.Object, ) -> System.Boolean:
        ...

    @typing.overload
    def Equals(self, handle: System.RuntimeTypeHandle, ) -> System.Boolean:
        ...

    @typing.overload
    def GetModuleHandle(self, ) -> System.ModuleHandle:
        ...

class Func(System.ICloneable, System.Runtime.Serialization.ISerializable, System.MulticastDelegate, typing.Generic[T1, T2, T3, TResult]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def Target(self) -> System.Object:
        ...

    @property
    def Method(self) -> System.Reflection.MethodInfo:
        ...

    # methods
    @typing.overload
    def __init__(self, object: System.Object, method: System.IntPtr, ):
        ...

    @typing.overload
    def Invoke(self, arg1: T1, arg2: T2, arg3: T3, ) -> TResult:
        ...

    @typing.overload
    def BeginInvoke(self, arg1: T1, arg2: T2, arg3: T3, callback: System.AsyncCallback, object: System.Object, ) -> System.IAsyncResult:
        ...

    @typing.overload
    def EndInvoke(self, result: System.IAsyncResult, ) -> TResult:
        ...

class AggregateException(System.Runtime.Serialization.ISerializable, System.Exception):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def InnerExceptions(self) -> System.Collections.ObjectModel.ReadOnlyCollection[System.Exception]:
        ...

    @property
    def Message(self) -> System.String:
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
    def HelpLink(self) -> System.String:
        ...
    @HelpLink.setter
    def HelpLink(self, val: System.String):
        ...

    @property
    def Source(self) -> System.String:
        ...
    @Source.setter
    def Source(self, val: System.String):
        ...

    @property
    def HResult(self) -> System.Int32:
        ...
    @HResult.setter
    def HResult(self, val: System.Int32):
        ...

    @property
    def StackTrace(self) -> System.String:
        ...

    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def __init__(self, message: System.String, ):
        ...

    @typing.overload
    def __init__(self, message: System.String, innerException: System.Exception, ):
        ...

    @typing.overload
    def __init__(self, innerExceptions: System.Collections.Generic.IEnumerable[System.Exception], ):
        ...

    @typing.overload
    def __init__(self, innerExceptions: list[System.Exception], ):
        ...

    @typing.overload
    def __init__(self, message: System.String, innerExceptions: System.Collections.Generic.IEnumerable[System.Exception], ):
        ...

    @typing.overload
    def __init__(self, message: System.String, innerExceptions: list[System.Exception], ):
        ...

    @typing.overload
    def GetObjectData(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext, ) -> None:
        ...

    @typing.overload
    def GetBaseException(self, ) -> System.Exception:
        ...

    @typing.overload
    def Handle(self, predicate: System.Func[System.Exception, System.Boolean], ) -> None:
        ...

    @typing.overload
    def Flatten(self, ) -> System.AggregateException:
        ...

    @typing.overload
    def ToString(self, ) -> System.String:
        ...

class Action(System.ICloneable, System.Runtime.Serialization.ISerializable, System.MulticastDelegate):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def Target(self) -> System.Object:
        ...

    @property
    def Method(self) -> System.Reflection.MethodInfo:
        ...

    # methods
    @typing.overload
    def __init__(self, object: System.Object, method: System.IntPtr, ):
        ...

    @typing.overload
    def Invoke(self, ) -> None:
        ...

    @typing.overload
    def BeginInvoke(self, callback: System.AsyncCallback, object: System.Object, ) -> System.IAsyncResult:
        ...

    @typing.overload
    def EndInvoke(self, result: System.IAsyncResult, ) -> None:
        ...

class Exception(System.Runtime.Serialization.ISerializable, System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def TargetSite(self) -> System.Reflection.MethodBase:
        ...

    @property
    def Message(self) -> System.String:
        ...

    @property
    def Data(self) -> System.Collections.IDictionary:
        ...

    @property
    def InnerException(self) -> System.Exception:
        ...

    @property
    def HelpLink(self) -> System.String:
        ...
    @HelpLink.setter
    def HelpLink(self, val: System.String):
        ...

    @property
    def Source(self) -> System.String:
        ...
    @Source.setter
    def Source(self, val: System.String):
        ...

    @property
    def HResult(self) -> System.Int32:
        ...
    @HResult.setter
    def HResult(self, val: System.Int32):
        ...

    @property
    def StackTrace(self) -> System.String:
        ...

    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def __init__(self, message: System.String, ):
        ...

    @typing.overload
    def __init__(self, message: System.String, innerException: System.Exception, ):
        ...

    @typing.overload
    def GetObjectData(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext, ) -> None:
        ...

    @typing.overload
    def GetBaseException(self, ) -> System.Exception:
        ...

    @typing.overload
    def ToString(self, ) -> System.String:
        ...

    @typing.overload
    def GetType(self, ) -> System.Type:
        ...

class Func(System.ICloneable, System.Runtime.Serialization.ISerializable, System.MulticastDelegate, typing.Generic[TResult]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def Target(self) -> System.Object:
        ...

    @property
    def Method(self) -> System.Reflection.MethodInfo:
        ...

    # methods
    @typing.overload
    def __init__(self, object: System.Object, method: System.IntPtr, ):
        ...

    @typing.overload
    def Invoke(self, ) -> TResult:
        ...

    @typing.overload
    def BeginInvoke(self, callback: System.AsyncCallback, object: System.Object, ) -> System.IAsyncResult:
        ...

    @typing.overload
    def EndInvoke(self, result: System.IAsyncResult, ) -> TResult:
        ...

class Action(System.ICloneable, System.Runtime.Serialization.ISerializable, System.MulticastDelegate, typing.Generic[T1, T2]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def Target(self) -> System.Object:
        ...

    @property
    def Method(self) -> System.Reflection.MethodInfo:
        ...

    # methods
    @typing.overload
    def __init__(self, object: System.Object, method: System.IntPtr, ):
        ...

    @typing.overload
    def Invoke(self, arg1: T1, arg2: T2, ) -> None:
        ...

    @typing.overload
    def BeginInvoke(self, arg1: T1, arg2: T2, callback: System.AsyncCallback, object: System.Object, ) -> System.IAsyncResult:
        ...

    @typing.overload
    def EndInvoke(self, result: System.IAsyncResult, ) -> None:
        ...

class Func(System.ICloneable, System.Runtime.Serialization.ISerializable, System.MulticastDelegate, typing.Generic[T1, T2, TResult]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def Target(self) -> System.Object:
        ...

    @property
    def Method(self) -> System.Reflection.MethodInfo:
        ...

    # methods
    @typing.overload
    def __init__(self, object: System.Object, method: System.IntPtr, ):
        ...

    @typing.overload
    def Invoke(self, arg1: T1, arg2: T2, ) -> TResult:
        ...

    @typing.overload
    def BeginInvoke(self, arg1: T1, arg2: T2, callback: System.AsyncCallback, object: System.Object, ) -> System.IAsyncResult:
        ...

    @typing.overload
    def EndInvoke(self, result: System.IAsyncResult, ) -> TResult:
        ...

class IBinaryFloatingPoint(System.IBinaryNumber[TSelf], System.IBitwiseOperators[TSelf, TSelf, TSelf], System.INumber[TSelf], System.IAdditionOperators[TSelf, TSelf, TSelf], System.IAdditiveIdentity[TSelf, TSelf], System.IComparisonOperators[TSelf, TSelf], System.IComparable, System.IComparable[TSelf], System.IEqualityOperators[TSelf, TSelf], System.IEquatable[TSelf], System.IDecrementOperators[TSelf], System.IDivisionOperators[TSelf, TSelf, TSelf], System.IIncrementOperators[TSelf], System.IModulusOperators[TSelf, TSelf, TSelf], System.IMultiplicativeIdentity[TSelf, TSelf], System.IMultiplyOperators[TSelf, TSelf, TSelf], System.ISpanFormattable, System.IFormattable, System.ISpanParseable[TSelf], System.IParseable[TSelf], System.ISubtractionOperators[TSelf, TSelf, TSelf], System.IUnaryNegationOperators[TSelf, TSelf], System.IUnaryPlusOperators[TSelf, TSelf], System.IFloatingPoint[TSelf], System.ISignedNumber[TSelf], abc.ABC, typing.Generic[TSelf]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    # methods
class IFloatingPoint(System.ISignedNumber[TSelf], System.INumber[TSelf], System.IAdditionOperators[TSelf, TSelf, TSelf], System.IAdditiveIdentity[TSelf, TSelf], System.IComparisonOperators[TSelf, TSelf], System.IComparable, System.IComparable[TSelf], System.IEqualityOperators[TSelf, TSelf], System.IEquatable[TSelf], System.IDecrementOperators[TSelf], System.IDivisionOperators[TSelf, TSelf, TSelf], System.IIncrementOperators[TSelf], System.IModulusOperators[TSelf, TSelf, TSelf], System.IMultiplicativeIdentity[TSelf, TSelf], System.IMultiplyOperators[TSelf, TSelf, TSelf], System.ISpanFormattable, System.IFormattable, System.ISpanParseable[TSelf], System.IParseable[TSelf], System.ISubtractionOperators[TSelf, TSelf, TSelf], System.IUnaryNegationOperators[TSelf, TSelf], System.IUnaryPlusOperators[TSelf, TSelf], abc.ABC, typing.Generic[TSelf]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @abc.abstractmethod
    @property
    def E(self) -> TSelf:
        ...

    @abc.abstractmethod
    @property
    def Epsilon(self) -> TSelf:
        ...

    @abc.abstractmethod
    @property
    def NaN(self) -> TSelf:
        ...

    @abc.abstractmethod
    @property
    def NegativeInfinity(self) -> TSelf:
        ...

    @abc.abstractmethod
    @property
    def NegativeZero(self) -> TSelf:
        ...

    @abc.abstractmethod
    @property
    def Pi(self) -> TSelf:
        ...

    @abc.abstractmethod
    @property
    def PositiveInfinity(self) -> TSelf:
        ...

    @abc.abstractmethod
    @property
    def Tau(self) -> TSelf:
        ...

    # methods
    @typing.overload
    @abc.abstractmethod
    @staticmethod
    def Acos(x: TSelf, ) -> TSelf:
        ...

    @typing.overload
    @abc.abstractmethod
    @staticmethod
    def Acosh(x: TSelf, ) -> TSelf:
        ...

    @typing.overload
    @abc.abstractmethod
    @staticmethod
    def Asin(x: TSelf, ) -> TSelf:
        ...

    @typing.overload
    @abc.abstractmethod
    @staticmethod
    def Asinh(x: TSelf, ) -> TSelf:
        ...

    @typing.overload
    @abc.abstractmethod
    @staticmethod
    def Atan(x: TSelf, ) -> TSelf:
        ...

    @typing.overload
    @abc.abstractmethod
    @staticmethod
    def Atan2(y: TSelf, x: TSelf, ) -> TSelf:
        ...

    @typing.overload
    @abc.abstractmethod
    @staticmethod
    def Atanh(x: TSelf, ) -> TSelf:
        ...

    @typing.overload
    @abc.abstractmethod
    @staticmethod
    def BitDecrement(x: TSelf, ) -> TSelf:
        ...

    @typing.overload
    @abc.abstractmethod
    @staticmethod
    def BitIncrement(x: TSelf, ) -> TSelf:
        ...

    @typing.overload
    @abc.abstractmethod
    @staticmethod
    def Cbrt(x: TSelf, ) -> TSelf:
        ...

    @typing.overload
    @abc.abstractmethod
    @staticmethod
    def Ceiling(x: TSelf, ) -> TSelf:
        ...

    @typing.overload
    @abc.abstractmethod
    @staticmethod
    def CopySign(x: TSelf, y: TSelf, ) -> TSelf:
        ...

    @typing.overload
    @abc.abstractmethod
    @staticmethod
    def Cos(x: TSelf, ) -> TSelf:
        ...

    @typing.overload
    @abc.abstractmethod
    @staticmethod
    def Cosh(x: TSelf, ) -> TSelf:
        ...

    @typing.overload
    @abc.abstractmethod
    @staticmethod
    def Exp(x: TSelf, ) -> TSelf:
        ...

    @typing.overload
    @abc.abstractmethod
    @staticmethod
    def Floor(x: TSelf, ) -> TSelf:
        ...

    @typing.overload
    @abc.abstractmethod
    @staticmethod
    def FusedMultiplyAdd(left: TSelf, right: TSelf, addend: TSelf, ) -> TSelf:
        ...

    @typing.overload
    @abc.abstractmethod
    @staticmethod
    def IEEERemainder(left: TSelf, right: TSelf, ) -> TSelf:
        ...

    @typing.overload
    @abc.abstractmethod
    @staticmethod
    def ILogB(x: TSelf, ) -> TInteger:
        ...

    @typing.overload
    @abc.abstractmethod
    @staticmethod
    def IsFinite(value: TSelf, ) -> System.Boolean:
        ...

    @typing.overload
    @abc.abstractmethod
    @staticmethod
    def IsInfinity(value: TSelf, ) -> System.Boolean:
        ...

    @typing.overload
    @abc.abstractmethod
    @staticmethod
    def IsNaN(value: TSelf, ) -> System.Boolean:
        ...

    @typing.overload
    @abc.abstractmethod
    @staticmethod
    def IsNegative(value: TSelf, ) -> System.Boolean:
        ...

    @typing.overload
    @abc.abstractmethod
    @staticmethod
    def IsNegativeInfinity(value: TSelf, ) -> System.Boolean:
        ...

    @typing.overload
    @abc.abstractmethod
    @staticmethod
    def IsNormal(value: TSelf, ) -> System.Boolean:
        ...

    @typing.overload
    @abc.abstractmethod
    @staticmethod
    def IsPositiveInfinity(value: TSelf, ) -> System.Boolean:
        ...

    @typing.overload
    @abc.abstractmethod
    @staticmethod
    def IsSubnormal(value: TSelf, ) -> System.Boolean:
        ...

    @typing.overload
    @abc.abstractmethod
    @staticmethod
    def Log(x: TSelf, ) -> TSelf:
        ...

    @typing.overload
    @abc.abstractmethod
    @staticmethod
    def Log(x: TSelf, newBase: TSelf, ) -> TSelf:
        ...

    @typing.overload
    @abc.abstractmethod
    @staticmethod
    def Log2(x: TSelf, ) -> TSelf:
        ...

    @typing.overload
    @abc.abstractmethod
    @staticmethod
    def Log10(x: TSelf, ) -> TSelf:
        ...

    @typing.overload
    @abc.abstractmethod
    @staticmethod
    def MaxMagnitude(x: TSelf, y: TSelf, ) -> TSelf:
        ...

    @typing.overload
    @abc.abstractmethod
    @staticmethod
    def MinMagnitude(x: TSelf, y: TSelf, ) -> TSelf:
        ...

    @typing.overload
    @abc.abstractmethod
    @staticmethod
    def Pow(x: TSelf, y: TSelf, ) -> TSelf:
        ...

    @typing.overload
    @abc.abstractmethod
    @staticmethod
    def Round(x: TSelf, ) -> TSelf:
        ...

    @typing.overload
    @abc.abstractmethod
    @staticmethod
    def Round(x: TSelf, digits: TInteger, ) -> TSelf:
        ...

    @typing.overload
    @abc.abstractmethod
    @staticmethod
    def Round(x: TSelf, mode: System.MidpointRounding, ) -> TSelf:
        ...

    @typing.overload
    @abc.abstractmethod
    @staticmethod
    def Round(x: TSelf, digits: TInteger, mode: System.MidpointRounding, ) -> TSelf:
        ...

    @typing.overload
    @abc.abstractmethod
    @staticmethod
    def ScaleB(x: TSelf, n: TInteger, ) -> TSelf:
        ...

    @typing.overload
    @abc.abstractmethod
    @staticmethod
    def Sin(x: TSelf, ) -> TSelf:
        ...

    @typing.overload
    @abc.abstractmethod
    @staticmethod
    def Sinh(x: TSelf, ) -> TSelf:
        ...

    @typing.overload
    @abc.abstractmethod
    @staticmethod
    def Sqrt(x: TSelf, ) -> TSelf:
        ...

    @typing.overload
    @abc.abstractmethod
    @staticmethod
    def Tan(x: TSelf, ) -> TSelf:
        ...

    @typing.overload
    @abc.abstractmethod
    @staticmethod
    def Tanh(x: TSelf, ) -> TSelf:
        ...

    @typing.overload
    @abc.abstractmethod
    @staticmethod
    def Truncate(x: TSelf, ) -> TSelf:
        ...

class IAsyncDisposable(abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    # methods
    @typing.overload
    @abc.abstractmethod
    def DisposeAsync(self, ) -> System.Threading.Tasks.ValueTask:
        ...

class ModuleHandle(System.ValueType):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def MDStreamVersion(self) -> System.Int32:
        ...

    # methods
    @typing.overload
    def GetHashCode(self, ) -> System.Int32:
        ...

    @typing.overload
    def Equals(self, obj: System.Object, ) -> System.Boolean:
        ...

    @typing.overload
    def Equals(self, handle: System.ModuleHandle, ) -> System.Boolean:
        ...

    @typing.overload
    def GetRuntimeTypeHandleFromMetadataToken(self, typeToken: System.Int32, ) -> System.RuntimeTypeHandle:
        ...

    @typing.overload
    def ResolveTypeHandle(self, typeToken: System.Int32, ) -> System.RuntimeTypeHandle:
        ...

    @typing.overload
    def ResolveTypeHandle(self, typeToken: System.Int32, typeInstantiationContext: list[System.RuntimeTypeHandle], methodInstantiationContext: list[System.RuntimeTypeHandle], ) -> System.RuntimeTypeHandle:
        ...

    @typing.overload
    def GetRuntimeMethodHandleFromMetadataToken(self, methodToken: System.Int32, ) -> System.RuntimeMethodHandle:
        ...

    @typing.overload
    def ResolveMethodHandle(self, methodToken: System.Int32, ) -> System.RuntimeMethodHandle:
        ...

    @typing.overload
    def ResolveMethodHandle(self, methodToken: System.Int32, typeInstantiationContext: list[System.RuntimeTypeHandle], methodInstantiationContext: list[System.RuntimeTypeHandle], ) -> System.RuntimeMethodHandle:
        ...

    @typing.overload
    def GetRuntimeFieldHandleFromMetadataToken(self, fieldToken: System.Int32, ) -> System.RuntimeFieldHandle:
        ...

    @typing.overload
    def ResolveFieldHandle(self, fieldToken: System.Int32, ) -> System.RuntimeFieldHandle:
        ...

    @typing.overload
    def ResolveFieldHandle(self, fieldToken: System.Int32, typeInstantiationContext: list[System.RuntimeTypeHandle], methodInstantiationContext: list[System.RuntimeTypeHandle], ) -> System.RuntimeFieldHandle:
        ...

class Version(System.ICloneable, System.IComparable, System.IComparable[System.Version], System.IEquatable[System.Version], System.ISpanFormattable, System.IFormattable, System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def Major(self) -> System.Int32:
        ...

    @property
    def Minor(self) -> System.Int32:
        ...

    @property
    def Build(self) -> System.Int32:
        ...

    @property
    def Revision(self) -> System.Int32:
        ...

    @property
    def MajorRevision(self) -> System.Int16:
        ...

    @property
    def MinorRevision(self) -> System.Int16:
        ...

    # methods
    @typing.overload
    def __init__(self, major: System.Int32, minor: System.Int32, build: System.Int32, revision: System.Int32, ):
        ...

    @typing.overload
    def __init__(self, major: System.Int32, minor: System.Int32, build: System.Int32, ):
        ...

    @typing.overload
    def __init__(self, major: System.Int32, minor: System.Int32, ):
        ...

    @typing.overload
    def __init__(self, version: System.String, ):
        ...

    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def Clone(self, ) -> System.Object:
        ...

    @typing.overload
    def CompareTo(self, version: System.Object, ) -> System.Int32:
        ...

    @typing.overload
    def CompareTo(self, value: System.Version, ) -> System.Int32:
        ...

    @typing.overload
    def Equals(self, obj: System.Object, ) -> System.Boolean:
        ...

    @typing.overload
    def Equals(self, obj: System.Version, ) -> System.Boolean:
        ...

    @typing.overload
    def GetHashCode(self, ) -> System.Int32:
        ...

    @typing.overload
    def ToString(self, ) -> System.String:
        ...

    @typing.overload
    def ToString(self, fieldCount: System.Int32, ) -> System.String:
        ...

    @typing.overload
    def TryFormat(self, destination: System.Span[System.Char], charsWritten: ref[System.Int32], ) -> System.Boolean:
        ...

    @typing.overload
    def TryFormat(self, destination: System.Span[System.Char], fieldCount: System.Int32, charsWritten: ref[System.Int32], ) -> System.Boolean:
        ...

    @typing.overload
    @staticmethod
    def Parse(input: System.String, ) -> System.Version:
        ...

    @typing.overload
    @staticmethod
    def Parse(input: System.ReadOnlySpan[System.Char], ) -> System.Version:
        ...

    @typing.overload
    @staticmethod
    def TryParse(input: System.String, result: ref[System.Version], ) -> System.Boolean:
        ...

    @typing.overload
    @staticmethod
    def TryParse(input: System.ReadOnlySpan[System.Char], result: ref[System.Version], ) -> System.Boolean:
        ...

class MarshalByRefObject(System.Object, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    # methods
    @typing.overload
    def GetLifetimeService(self, ) -> System.Object:
        ...

    @typing.overload
    def InitializeLifetimeService(self, ) -> System.Object:
        ...

class RuntimeFieldHandle(System.Runtime.Serialization.ISerializable, System.ValueType):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def Value(self) -> System.IntPtr:
        ...

    # methods
    @typing.overload
    def GetHashCode(self, ) -> System.Int32:
        ...

    @typing.overload
    def Equals(self, obj: System.Object, ) -> System.Boolean:
        ...

    @typing.overload
    def Equals(self, handle: System.RuntimeFieldHandle, ) -> System.Boolean:
        ...

    @typing.overload
    def GetObjectData(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext, ) -> None:
        ...

class TypedReference(System.ValueType):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    # methods
    @typing.overload
    @staticmethod
    def MakeTypedReference(target: System.Object, flds: list[System.Reflection.FieldInfo], ) -> System.TypedReference:
        ...

    @typing.overload
    def GetHashCode(self, ) -> System.Int32:
        ...

    @typing.overload
    def Equals(self, o: System.Object, ) -> System.Boolean:
        ...

    @typing.overload
    @staticmethod
    def ToObject(value: System.TypedReference, ) -> System.Object:
        ...

    @typing.overload
    @staticmethod
    def GetTargetType(value: System.TypedReference, ) -> System.Type:
        ...

    @typing.overload
    @staticmethod
    def TargetTypeToken(value: System.TypedReference, ) -> System.RuntimeTypeHandle:
        ...

    @typing.overload
    @staticmethod
    def SetTypedReference(target: System.TypedReference, value: System.Object, ) -> None:
        ...

class Func(System.ICloneable, System.Runtime.Serialization.ISerializable, System.MulticastDelegate, typing.Generic[T1, T2, T3, T4, TResult]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def Target(self) -> System.Object:
        ...

    @property
    def Method(self) -> System.Reflection.MethodInfo:
        ...

    # methods
    @typing.overload
    def __init__(self, object: System.Object, method: System.IntPtr, ):
        ...

    @typing.overload
    def Invoke(self, arg1: T1, arg2: T2, arg3: T3, arg4: T4, ) -> TResult:
        ...

    @typing.overload
    def BeginInvoke(self, arg1: T1, arg2: T2, arg3: T3, arg4: T4, callback: System.AsyncCallback, object: System.Object, ) -> System.IAsyncResult:
        ...

    @typing.overload
    def EndInvoke(self, result: System.IAsyncResult, ) -> TResult:
        ...

class Func(System.ICloneable, System.Runtime.Serialization.ISerializable, System.MulticastDelegate, typing.Generic[T1, T2, T3, T4, T5, TResult]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def Target(self) -> System.Object:
        ...

    @property
    def Method(self) -> System.Reflection.MethodInfo:
        ...

    # methods
    @typing.overload
    def __init__(self, object: System.Object, method: System.IntPtr, ):
        ...

    @typing.overload
    def Invoke(self, arg1: T1, arg2: T2, arg3: T3, arg4: T4, arg5: T5, ) -> TResult:
        ...

    @typing.overload
    def BeginInvoke(self, arg1: T1, arg2: T2, arg3: T3, arg4: T4, arg5: T5, callback: System.AsyncCallback, object: System.Object, ) -> System.IAsyncResult:
        ...

    @typing.overload
    def EndInvoke(self, result: System.IAsyncResult, ) -> TResult:
        ...

class Func(System.ICloneable, System.Runtime.Serialization.ISerializable, System.MulticastDelegate, typing.Generic[T1, T2, T3, T4, T5, T6, TResult]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def Target(self) -> System.Object:
        ...

    @property
    def Method(self) -> System.Reflection.MethodInfo:
        ...

    # methods
    @typing.overload
    def __init__(self, object: System.Object, method: System.IntPtr, ):
        ...

    @typing.overload
    def Invoke(self, arg1: T1, arg2: T2, arg3: T3, arg4: T4, arg5: T5, arg6: T6, ) -> TResult:
        ...

    @typing.overload
    def BeginInvoke(self, arg1: T1, arg2: T2, arg3: T3, arg4: T4, arg5: T5, arg6: T6, callback: System.AsyncCallback, object: System.Object, ) -> System.IAsyncResult:
        ...

    @typing.overload
    def EndInvoke(self, result: System.IAsyncResult, ) -> TResult:
        ...

class Func(System.ICloneable, System.Runtime.Serialization.ISerializable, System.MulticastDelegate, typing.Generic[T1, T2, T3, T4, T5, T6, T7, TResult]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def Target(self) -> System.Object:
        ...

    @property
    def Method(self) -> System.Reflection.MethodInfo:
        ...

    # methods
    @typing.overload
    def __init__(self, object: System.Object, method: System.IntPtr, ):
        ...

    @typing.overload
    def Invoke(self, arg1: T1, arg2: T2, arg3: T3, arg4: T4, arg5: T5, arg6: T6, arg7: T7, ) -> TResult:
        ...

    @typing.overload
    def BeginInvoke(self, arg1: T1, arg2: T2, arg3: T3, arg4: T4, arg5: T5, arg6: T6, arg7: T7, callback: System.AsyncCallback, object: System.Object, ) -> System.IAsyncResult:
        ...

    @typing.overload
    def EndInvoke(self, result: System.IAsyncResult, ) -> TResult:
        ...

class Func(System.ICloneable, System.Runtime.Serialization.ISerializable, System.MulticastDelegate, typing.Generic[T1, T2, T3, T4, T5, T6, T7, T8, TResult]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def Target(self) -> System.Object:
        ...

    @property
    def Method(self) -> System.Reflection.MethodInfo:
        ...

    # methods
    @typing.overload
    def __init__(self, object: System.Object, method: System.IntPtr, ):
        ...

    @typing.overload
    def Invoke(self, arg1: T1, arg2: T2, arg3: T3, arg4: T4, arg5: T5, arg6: T6, arg7: T7, arg8: T8, ) -> TResult:
        ...

    @typing.overload
    def BeginInvoke(self, arg1: T1, arg2: T2, arg3: T3, arg4: T4, arg5: T5, arg6: T6, arg7: T7, arg8: T8, callback: System.AsyncCallback, object: System.Object, ) -> System.IAsyncResult:
        ...

    @typing.overload
    def EndInvoke(self, result: System.IAsyncResult, ) -> TResult:
        ...

class Func(System.ICloneable, System.Runtime.Serialization.ISerializable, System.MulticastDelegate, typing.Generic[T1, T2, T3, T4, T5, T6, T7, T8, T9, TResult]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def Target(self) -> System.Object:
        ...

    @property
    def Method(self) -> System.Reflection.MethodInfo:
        ...

    # methods
    @typing.overload
    def __init__(self, object: System.Object, method: System.IntPtr, ):
        ...

    @typing.overload
    def Invoke(self, arg1: T1, arg2: T2, arg3: T3, arg4: T4, arg5: T5, arg6: T6, arg7: T7, arg8: T8, arg9: T9, ) -> TResult:
        ...

    @typing.overload
    def BeginInvoke(self, arg1: T1, arg2: T2, arg3: T3, arg4: T4, arg5: T5, arg6: T6, arg7: T7, arg8: T8, arg9: T9, callback: System.AsyncCallback, object: System.Object, ) -> System.IAsyncResult:
        ...

    @typing.overload
    def EndInvoke(self, result: System.IAsyncResult, ) -> TResult:
        ...

class Func(System.ICloneable, System.Runtime.Serialization.ISerializable, System.MulticastDelegate, typing.Generic[T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, TResult]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def Target(self) -> System.Object:
        ...

    @property
    def Method(self) -> System.Reflection.MethodInfo:
        ...

    # methods
    @typing.overload
    def __init__(self, object: System.Object, method: System.IntPtr, ):
        ...

    @typing.overload
    def Invoke(self, arg1: T1, arg2: T2, arg3: T3, arg4: T4, arg5: T5, arg6: T6, arg7: T7, arg8: T8, arg9: T9, arg10: T10, ) -> TResult:
        ...

    @typing.overload
    def BeginInvoke(self, arg1: T1, arg2: T2, arg3: T3, arg4: T4, arg5: T5, arg6: T6, arg7: T7, arg8: T8, arg9: T9, arg10: T10, callback: System.AsyncCallback, object: System.Object, ) -> System.IAsyncResult:
        ...

    @typing.overload
    def EndInvoke(self, result: System.IAsyncResult, ) -> TResult:
        ...

class Func(System.ICloneable, System.Runtime.Serialization.ISerializable, System.MulticastDelegate, typing.Generic[T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, TResult]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def Target(self) -> System.Object:
        ...

    @property
    def Method(self) -> System.Reflection.MethodInfo:
        ...

    # methods
    @typing.overload
    def __init__(self, object: System.Object, method: System.IntPtr, ):
        ...

    @typing.overload
    def Invoke(self, arg1: T1, arg2: T2, arg3: T3, arg4: T4, arg5: T5, arg6: T6, arg7: T7, arg8: T8, arg9: T9, arg10: T10, arg11: T11, ) -> TResult:
        ...

    @typing.overload
    def BeginInvoke(self, arg1: T1, arg2: T2, arg3: T3, arg4: T4, arg5: T5, arg6: T6, arg7: T7, arg8: T8, arg9: T9, arg10: T10, arg11: T11, callback: System.AsyncCallback, object: System.Object, ) -> System.IAsyncResult:
        ...

    @typing.overload
    def EndInvoke(self, result: System.IAsyncResult, ) -> TResult:
        ...

class Func(System.ICloneable, System.Runtime.Serialization.ISerializable, System.MulticastDelegate, typing.Generic[T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, TResult]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def Target(self) -> System.Object:
        ...

    @property
    def Method(self) -> System.Reflection.MethodInfo:
        ...

    # methods
    @typing.overload
    def __init__(self, object: System.Object, method: System.IntPtr, ):
        ...

    @typing.overload
    def Invoke(self, arg1: T1, arg2: T2, arg3: T3, arg4: T4, arg5: T5, arg6: T6, arg7: T7, arg8: T8, arg9: T9, arg10: T10, arg11: T11, arg12: T12, ) -> TResult:
        ...

    @typing.overload
    def BeginInvoke(self, arg1: T1, arg2: T2, arg3: T3, arg4: T4, arg5: T5, arg6: T6, arg7: T7, arg8: T8, arg9: T9, arg10: T10, arg11: T11, arg12: T12, callback: System.AsyncCallback, object: System.Object, ) -> System.IAsyncResult:
        ...

    @typing.overload
    def EndInvoke(self, result: System.IAsyncResult, ) -> TResult:
        ...

class Func(System.ICloneable, System.Runtime.Serialization.ISerializable, System.MulticastDelegate, typing.Generic[T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13, TResult]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def Target(self) -> System.Object:
        ...

    @property
    def Method(self) -> System.Reflection.MethodInfo:
        ...

    # methods
    @typing.overload
    def __init__(self, object: System.Object, method: System.IntPtr, ):
        ...

    @typing.overload
    def Invoke(self, arg1: T1, arg2: T2, arg3: T3, arg4: T4, arg5: T5, arg6: T6, arg7: T7, arg8: T8, arg9: T9, arg10: T10, arg11: T11, arg12: T12, arg13: T13, ) -> TResult:
        ...

    @typing.overload
    def BeginInvoke(self, arg1: T1, arg2: T2, arg3: T3, arg4: T4, arg5: T5, arg6: T6, arg7: T7, arg8: T8, arg9: T9, arg10: T10, arg11: T11, arg12: T12, arg13: T13, callback: System.AsyncCallback, object: System.Object, ) -> System.IAsyncResult:
        ...

    @typing.overload
    def EndInvoke(self, result: System.IAsyncResult, ) -> TResult:
        ...

class Func(System.ICloneable, System.Runtime.Serialization.ISerializable, System.MulticastDelegate, typing.Generic[T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13, T14, TResult]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def Target(self) -> System.Object:
        ...

    @property
    def Method(self) -> System.Reflection.MethodInfo:
        ...

    # methods
    @typing.overload
    def __init__(self, object: System.Object, method: System.IntPtr, ):
        ...

    @typing.overload
    def Invoke(self, arg1: T1, arg2: T2, arg3: T3, arg4: T4, arg5: T5, arg6: T6, arg7: T7, arg8: T8, arg9: T9, arg10: T10, arg11: T11, arg12: T12, arg13: T13, arg14: T14, ) -> TResult:
        ...

    @typing.overload
    def BeginInvoke(self, arg1: T1, arg2: T2, arg3: T3, arg4: T4, arg5: T5, arg6: T6, arg7: T7, arg8: T8, arg9: T9, arg10: T10, arg11: T11, arg12: T12, arg13: T13, arg14: T14, callback: System.AsyncCallback, object: System.Object, ) -> System.IAsyncResult:
        ...

    @typing.overload
    def EndInvoke(self, result: System.IAsyncResult, ) -> TResult:
        ...

class Func(System.ICloneable, System.Runtime.Serialization.ISerializable, System.MulticastDelegate, typing.Generic[T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13, T14, T15, TResult]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def Target(self) -> System.Object:
        ...

    @property
    def Method(self) -> System.Reflection.MethodInfo:
        ...

    # methods
    @typing.overload
    def __init__(self, object: System.Object, method: System.IntPtr, ):
        ...

    @typing.overload
    def Invoke(self, arg1: T1, arg2: T2, arg3: T3, arg4: T4, arg5: T5, arg6: T6, arg7: T7, arg8: T8, arg9: T9, arg10: T10, arg11: T11, arg12: T12, arg13: T13, arg14: T14, arg15: T15, ) -> TResult:
        ...

    @typing.overload
    def BeginInvoke(self, arg1: T1, arg2: T2, arg3: T3, arg4: T4, arg5: T5, arg6: T6, arg7: T7, arg8: T8, arg9: T9, arg10: T10, arg11: T11, arg12: T12, arg13: T13, arg14: T14, arg15: T15, callback: System.AsyncCallback, object: System.Object, ) -> System.IAsyncResult:
        ...

    @typing.overload
    def EndInvoke(self, result: System.IAsyncResult, ) -> TResult:
        ...

class Func(System.ICloneable, System.Runtime.Serialization.ISerializable, System.MulticastDelegate, typing.Generic[T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13, T14, T15, T16, TResult]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def Target(self) -> System.Object:
        ...

    @property
    def Method(self) -> System.Reflection.MethodInfo:
        ...

    # methods
    @typing.overload
    def __init__(self, object: System.Object, method: System.IntPtr, ):
        ...

    @typing.overload
    def Invoke(self, arg1: T1, arg2: T2, arg3: T3, arg4: T4, arg5: T5, arg6: T6, arg7: T7, arg8: T8, arg9: T9, arg10: T10, arg11: T11, arg12: T12, arg13: T13, arg14: T14, arg15: T15, arg16: T16, ) -> TResult:
        ...

    @typing.overload
    def BeginInvoke(self, arg1: T1, arg2: T2, arg3: T3, arg4: T4, arg5: T5, arg6: T6, arg7: T7, arg8: T8, arg9: T9, arg10: T10, arg11: T11, arg12: T12, arg13: T13, arg14: T14, arg15: T15, arg16: T16, callback: System.AsyncCallback, object: System.Object, ) -> System.IAsyncResult:
        ...

    @typing.overload
    def EndInvoke(self, result: System.IAsyncResult, ) -> TResult:
        ...

class IServiceProvider(abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    # methods
    @typing.overload
    @abc.abstractmethod
    def GetService(self, serviceType: System.Type, ) -> System.Object:
        ...

class Memory(System.IEquatable[System.Memory], System.ValueType, typing.Generic[T]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def Empty(self) -> System.Memory:
        ...

    @property
    def Length(self) -> System.Int32:
        ...

    @property
    def IsEmpty(self) -> System.Boolean:
        ...

    @property
    def Span(self) -> System.Span[T]:
        ...

    # methods
    @typing.overload
    def __init__(self, array: list[T], ):
        ...

    @typing.overload
    def __init__(self, array: list[T], start: System.Int32, length: System.Int32, ):
        ...

    @typing.overload
    def ToString(self, ) -> System.String:
        ...

    @typing.overload
    def Slice(self, start: System.Int32, ) -> System.Memory:
        ...

    @typing.overload
    def Slice(self, start: System.Int32, length: System.Int32, ) -> System.Memory:
        ...

    @typing.overload
    def CopyTo(self, destination: System.Memory, ) -> None:
        ...

    @typing.overload
    def TryCopyTo(self, destination: System.Memory, ) -> System.Boolean:
        ...

    @typing.overload
    def Pin(self, ) -> System.Buffers.MemoryHandle:
        ...

    @typing.overload
    def ToArray(self, ) -> list[T]:
        ...

    @typing.overload
    def Equals(self, obj: System.Object, ) -> System.Boolean:
        ...

    @typing.overload
    def Equals(self, other: System.Memory, ) -> System.Boolean:
        ...

    @typing.overload
    def GetHashCode(self, ) -> System.Int32:
        ...

class ReadOnlyMemory(System.IEquatable[System.ReadOnlyMemory], System.ValueType, typing.Generic[T]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def Empty(self) -> System.ReadOnlyMemory:
        ...

    @property
    def Length(self) -> System.Int32:
        ...

    @property
    def IsEmpty(self) -> System.Boolean:
        ...

    @property
    def Span(self) -> System.ReadOnlySpan[T]:
        ...

    # methods
    @typing.overload
    def __init__(self, array: list[T], ):
        ...

    @typing.overload
    def __init__(self, array: list[T], start: System.Int32, length: System.Int32, ):
        ...

    @typing.overload
    def ToString(self, ) -> System.String:
        ...

    @typing.overload
    def Slice(self, start: System.Int32, ) -> System.ReadOnlyMemory:
        ...

    @typing.overload
    def Slice(self, start: System.Int32, length: System.Int32, ) -> System.ReadOnlyMemory:
        ...

    @typing.overload
    def CopyTo(self, destination: System.Memory[T], ) -> None:
        ...

    @typing.overload
    def TryCopyTo(self, destination: System.Memory[T], ) -> System.Boolean:
        ...

    @typing.overload
    def Pin(self, ) -> System.Buffers.MemoryHandle:
        ...

    @typing.overload
    def ToArray(self, ) -> list[T]:
        ...

    @typing.overload
    def Equals(self, obj: System.Object, ) -> System.Boolean:
        ...

    @typing.overload
    def Equals(self, other: System.ReadOnlyMemory, ) -> System.Boolean:
        ...

    @typing.overload
    def GetHashCode(self, ) -> System.Int32:
        ...

class Uri(System.Runtime.Serialization.ISerializable, System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def AbsolutePath(self) -> System.String:
        ...

    @property
    def AbsoluteUri(self) -> System.String:
        ...

    @property
    def LocalPath(self) -> System.String:
        ...

    @property
    def Authority(self) -> System.String:
        ...

    @property
    def HostNameType(self) -> System.UriHostNameType:
        ...

    @property
    def IsDefaultPort(self) -> System.Boolean:
        ...

    @property
    def IsFile(self) -> System.Boolean:
        ...

    @property
    def IsLoopback(self) -> System.Boolean:
        ...

    @property
    def PathAndQuery(self) -> System.String:
        ...

    @property
    def Segments(self) -> list[System.String]:
        ...

    @property
    def IsUnc(self) -> System.Boolean:
        ...

    @property
    def Host(self) -> System.String:
        ...

    @property
    def Port(self) -> System.Int32:
        ...

    @property
    def Query(self) -> System.String:
        ...

    @property
    def Fragment(self) -> System.String:
        ...

    @property
    def Scheme(self) -> System.String:
        ...

    @property
    def OriginalString(self) -> System.String:
        ...

    @property
    def DnsSafeHost(self) -> System.String:
        ...

    @property
    def IdnHost(self) -> System.String:
        ...

    @property
    def IsAbsoluteUri(self) -> System.Boolean:
        ...

    @property
    def UserEscaped(self) -> System.Boolean:
        ...

    @property
    def UserInfo(self) -> System.String:
        ...

    # methods
    @typing.overload
    def __init__(self, uriString: System.String, ):
        ...

    @typing.overload
    def __init__(self, uriString: System.String, dontEscape: System.Boolean, ):
        ...

    @typing.overload
    def __init__(self, baseUri: System.Uri, relativeUri: System.String, dontEscape: System.Boolean, ):
        ...

    @typing.overload
    def __init__(self, uriString: System.String, uriKind: System.UriKind, ):
        ...

    @typing.overload
    def __init__(self, uriString: System.String, creationOptions: ref[System.UriCreationOptions], ):
        ...

    @typing.overload
    def __init__(self, baseUri: System.Uri, relativeUri: System.String, ):
        ...

    @typing.overload
    def __init__(self, baseUri: System.Uri, relativeUri: System.Uri, ):
        ...

    @typing.overload
    def MakeRelative(self, toUri: System.Uri, ) -> System.String:
        ...

    @typing.overload
    @staticmethod
    def TryCreate(uriString: System.String, uriKind: System.UriKind, result: ref[System.Uri], ) -> System.Boolean:
        ...

    @typing.overload
    @staticmethod
    def TryCreate(uriString: System.String, creationOptions: ref[System.UriCreationOptions], result: ref[System.Uri], ) -> System.Boolean:
        ...

    @typing.overload
    @staticmethod
    def TryCreate(baseUri: System.Uri, relativeUri: System.String, result: ref[System.Uri], ) -> System.Boolean:
        ...

    @typing.overload
    @staticmethod
    def TryCreate(baseUri: System.Uri, relativeUri: System.Uri, result: ref[System.Uri], ) -> System.Boolean:
        ...

    @typing.overload
    def GetComponents(self, components: System.UriComponents, format: System.UriFormat, ) -> System.String:
        ...

    @typing.overload
    @staticmethod
    def Compare(uri1: System.Uri, uri2: System.Uri, partsToCompare: System.UriComponents, compareFormat: System.UriFormat, comparisonType: System.StringComparison, ) -> System.Int32:
        ...

    @typing.overload
    def IsWellFormedOriginalString(self, ) -> System.Boolean:
        ...

    @typing.overload
    @staticmethod
    def IsWellFormedUriString(uriString: System.String, uriKind: System.UriKind, ) -> System.Boolean:
        ...

    @typing.overload
    @staticmethod
    def UnescapeDataString(stringToUnescape: System.String, ) -> System.String:
        ...

    @typing.overload
    @staticmethod
    def EscapeUriString(stringToEscape: System.String, ) -> System.String:
        ...

    @typing.overload
    @staticmethod
    def EscapeDataString(stringToEscape: System.String, ) -> System.String:
        ...

    @typing.overload
    def IsBaseOf(self, uri: System.Uri, ) -> System.Boolean:
        ...

    @typing.overload
    @staticmethod
    def CheckHostName(name: System.String, ) -> System.UriHostNameType:
        ...

    @typing.overload
    def GetLeftPart(self, part: System.UriPartial, ) -> System.String:
        ...

    @typing.overload
    @staticmethod
    def HexEscape(character: System.Char, ) -> System.String:
        ...

    @typing.overload
    @staticmethod
    def HexUnescape(pattern: System.String, index: ref[System.Int32], ) -> System.Char:
        ...

    @typing.overload
    @staticmethod
    def IsHexEncoding(pattern: System.String, index: System.Int32, ) -> System.Boolean:
        ...

    @typing.overload
    @staticmethod
    def CheckSchemeName(schemeName: System.String, ) -> System.Boolean:
        ...

    @typing.overload
    @staticmethod
    def IsHexDigit(character: System.Char, ) -> System.Boolean:
        ...

    @typing.overload
    @staticmethod
    def FromHex(digit: System.Char, ) -> System.Int32:
        ...

    @typing.overload
    def GetHashCode(self, ) -> System.Int32:
        ...

    @typing.overload
    def ToString(self, ) -> System.String:
        ...

    @typing.overload
    def Equals(self, comparand: System.Object, ) -> System.Boolean:
        ...

    @typing.overload
    def MakeRelativeUri(self, uri: System.Uri, ) -> System.Uri:
        ...

class EventArgs(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    # methods
    @typing.overload
    def __init__(self, ):
        ...

class EventHandler(System.ICloneable, System.Runtime.Serialization.ISerializable, System.MulticastDelegate):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def Target(self) -> System.Object:
        ...

    @property
    def Method(self) -> System.Reflection.MethodInfo:
        ...

    # methods
    @typing.overload
    def __init__(self, object: System.Object, method: System.IntPtr, ):
        ...

    @typing.overload
    def Invoke(self, sender: System.Object, e: System.EventArgs, ) -> None:
        ...

    @typing.overload
    def BeginInvoke(self, sender: System.Object, e: System.EventArgs, callback: System.AsyncCallback, object: System.Object, ) -> System.IAsyncResult:
        ...

    @typing.overload
    def EndInvoke(self, result: System.IAsyncResult, ) -> None:
        ...

class UriHostNameType(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    Unknown: System.Int32 = Unknown
    Basic: System.Int32 = Basic
    Dns: System.Int32 = Dns
    IPv4: System.Int32 = IPv4
    IPv6: System.Int32 = IPv6

class UriKind(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    RelativeOrAbsolute: System.Int32 = RelativeOrAbsolute
    Absolute: System.Int32 = Absolute
    Relative: System.Int32 = Relative

class UriCreationOptions(System.ValueType):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def DangerousDisablePathAndQueryCanonicalization(self) -> System.Boolean:
        ...
    @DangerousDisablePathAndQueryCanonicalization.setter
    def DangerousDisablePathAndQueryCanonicalization(self, val: System.Boolean):
        ...

    # methods
class UriComponents(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    Scheme: System.Int32 = Scheme
    UserInfo: System.Int32 = UserInfo
    Host: System.Int32 = Host
    Port: System.Int32 = Port
    SchemeAndServer: System.Int32 = SchemeAndServer
    Path: System.Int32 = Path
    Query: System.Int32 = Query
    PathAndQuery: System.Int32 = PathAndQuery
    HttpRequestUrl: System.Int32 = HttpRequestUrl
    Fragment: System.Int32 = Fragment
    AbsoluteUri: System.Int32 = AbsoluteUri
    StrongPort: System.Int32 = StrongPort
    HostAndPort: System.Int32 = HostAndPort
    StrongAuthority: System.Int32 = StrongAuthority
    NormalizedHost: System.Int32 = NormalizedHost
    KeepDelimiter: System.Int32 = KeepDelimiter
    SerializationInfoString: System.Int32 = SerializationInfoString

class UriFormat(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    UriEscaped: System.Int32 = UriEscaped
    Unescaped: System.Int32 = Unescaped
    SafeUnescaped: System.Int32 = SafeUnescaped

class UriPartial(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    Scheme: System.Int32 = Scheme
    Authority: System.Int32 = Authority
    Path: System.Int32 = Path
    Query: System.Int32 = Query

class SystemException(System.Runtime.Serialization.ISerializable, System.Exception):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def TargetSite(self) -> System.Reflection.MethodBase:
        ...

    @property
    def Message(self) -> System.String:
        ...

    @property
    def Data(self) -> System.Collections.IDictionary:
        ...

    @property
    def InnerException(self) -> System.Exception:
        ...

    @property
    def HelpLink(self) -> System.String:
        ...
    @HelpLink.setter
    def HelpLink(self, val: System.String):
        ...

    @property
    def Source(self) -> System.String:
        ...
    @Source.setter
    def Source(self, val: System.String):
        ...

    @property
    def HResult(self) -> System.Int32:
        ...
    @HResult.setter
    def HResult(self, val: System.Int32):
        ...

    @property
    def StackTrace(self) -> System.String:
        ...

    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def __init__(self, message: System.String, ):
        ...

    @typing.overload
    def __init__(self, message: System.String, innerException: System.Exception, ):
        ...

