from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import System
import System.Runtime.Serialization
import System.Decimal
import System.Reflection
import System.Threading
import System.Buffers
import System.Runtime.CompilerServices
import System.Collections
import System.Text
import System.Globalization
import System.Collections.Generic
import System.ReadOnlySpan
import System.Guid
import System.Exception
import System.Runtime.Loader
import System.RuntimeTypeHandle
import System.Span
import System.Collections.ObjectModel
import System.Runtime.ExceptionServices
import System.ArraySegment
import System.Uri
import System.Enum
import System.Reflection.Emit
import System.Threading.Tasks
import System.Security
import System.Security.Principal
import System.Runtime.Remoting
import System.Runtime.InteropServices

TOther = typing.TypeVar('TOther')
T1 = typing.TypeVar('T1')
T2 = typing.TypeVar('T2')
T3 = typing.TypeVar('T3')
TResult = typing.TypeVar('TResult')
TSelf = typing.TypeVar('TSelf')
T = typing.TypeVar('T')
T4 = typing.TypeVar('T4')
TInput = typing.TypeVar('TInput')
TOutput = typing.TypeVar('TOutput')
T5 = typing.TypeVar('T5')
T6 = typing.TypeVar('T6')
TEnum = typing.TypeVar('TEnum')
TKey = typing.TypeVar('TKey')
TValue = typing.TypeVar('TValue')
T7 = typing.TypeVar('T7')
T8 = typing.TypeVar('T8')
T9 = typing.TypeVar('T9')
TInteger = typing.TypeVar('TInteger')
T10 = typing.TypeVar('T10')
T11 = typing.TypeVar('T11')
T12 = typing.TypeVar('T12')
T13 = typing.TypeVar('T13')
T14 = typing.TypeVar('T14')
T15 = typing.TypeVar('T15')
T16 = typing.TypeVar('T16')
TEventArgs = typing.TypeVar('TEventArgs')

class IntPtr(System.IEquatable[System.IntPtr], System.IComparable, System.IComparable[System.IntPtr], System.ISpanFormattable, System.IFormattable, System.Runtime.Serialization.ISerializable, System.IBinaryInteger[System.IntPtr], System.IBinaryNumber[System.IntPtr], System.IBitwiseOperators[System.IntPtr, System.IntPtr, System.IntPtr], System.INumber[System.IntPtr], System.IAdditionOperators[System.IntPtr, System.IntPtr, System.IntPtr], System.IAdditiveIdentity[System.IntPtr, System.IntPtr], System.IComparisonOperators[System.IntPtr, System.IntPtr], System.IEqualityOperators[System.IntPtr, System.IntPtr], System.IDecrementOperators[System.IntPtr], System.IDivisionOperators[System.IntPtr, System.IntPtr, System.IntPtr], System.IIncrementOperators[System.IntPtr], System.IModulusOperators[System.IntPtr, System.IntPtr, System.IntPtr], System.IMultiplicativeIdentity[System.IntPtr, System.IntPtr], System.IMultiplyOperators[System.IntPtr, System.IntPtr, System.IntPtr], System.ISpanParseable[System.IntPtr], System.IParseable[System.IntPtr], System.ISubtractionOperators[System.IntPtr, System.IntPtr, System.IntPtr], System.IUnaryNegationOperators[System.IntPtr, System.IntPtr], System.IUnaryPlusOperators[System.IntPtr, System.IntPtr], System.IShiftOperators[System.IntPtr, System.IntPtr], System.IMinMaxValue[System.IntPtr], System.ISignedNumber[System.IntPtr], System.ValueType):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields
    Zero: System.IntPtr = ...

    # properties
    @property
    def Size(self) -> int:
        ...

    @property
    def MaxValue(self) -> System.IntPtr:
        ...

    @property
    def MinValue(self) -> System.IntPtr:
        ...

    @property
    def AdditiveIdentity(self) -> System.IntPtr:
        ...

    @property
    def MinValue(self) -> System.IntPtr:
        ...

    @property
    def MaxValue(self) -> System.IntPtr:
        ...

    @property
    def MultiplicativeIdentity(self) -> System.IntPtr:
        ...

    @property
    def One(self) -> System.IntPtr:
        ...

    @property
    def Zero(self) -> System.IntPtr:
        ...

    @property
    def NegativeOne(self) -> System.IntPtr:
        ...

    # methods
    @typing.overload
    def __init__(self, value: int, ):
        ...

    @typing.overload
    def __init__(self, value: int, ):
        ...

    @typing.overload
    def __init__(self, value: ptr[None], ):
        ...

    @typing.overload
    def __init__(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext, ):
        ...

    @staticmethod
    def op_Increment(value: System.IntPtr, ) -> System.IntPtr:
        ...

    @staticmethod
    def op_Modulus(left: System.IntPtr, right: System.IntPtr, ) -> System.IntPtr:
        ...

    @staticmethod
    def op_Multiply(left: System.IntPtr, right: System.IntPtr, ) -> System.IntPtr:
        ...

    @staticmethod
    def Abs(value: System.IntPtr, ) -> System.IntPtr:
        ...

    @staticmethod
    def Clamp(value: System.IntPtr, min: System.IntPtr, max: System.IntPtr, ) -> System.IntPtr:
        ...

    @staticmethod
    def Create(value: TOther, ) -> System.IntPtr:
        ...

    @staticmethod
    def CreateSaturating(value: TOther, ) -> System.IntPtr:
        ...

    @staticmethod
    def CreateTruncating(value: TOther, ) -> System.IntPtr:
        ...

    @staticmethod
    def DivRem(left: System.IntPtr, right: System.IntPtr, ) -> System.ValueTuple[System.IntPtr, System.IntPtr]:
        ...

    @staticmethod
    def Max(x: System.IntPtr, y: System.IntPtr, ) -> System.IntPtr:
        ...

    @staticmethod
    def Min(x: System.IntPtr, y: System.IntPtr, ) -> System.IntPtr:
        ...

    @staticmethod
    @typing.overload
    def Parse(s: str, style: int, provider: System.IFormatProvider, ) -> System.IntPtr:
        ...

    @staticmethod
    @typing.overload
    def Parse(s: System.ReadOnlySpan[str], style: int, provider: System.IFormatProvider, ) -> System.IntPtr:
        ...

    @staticmethod
    def Sign(value: System.IntPtr, ) -> System.IntPtr:
        ...

    @staticmethod
    def TryCreate(value: TOther, result: ref[System.IntPtr], ) -> bool:
        ...

    @staticmethod
    @typing.overload
    def TryParse(s: str, style: int, provider: System.IFormatProvider, result: ref[System.IntPtr], ) -> bool:
        ...

    @staticmethod
    @typing.overload
    def TryParse(s: System.ReadOnlySpan[str], style: int, provider: System.IFormatProvider, result: ref[System.IntPtr], ) -> bool:
        ...

    @staticmethod
    def Parse(s: str, provider: System.IFormatProvider, ) -> System.IntPtr:
        ...

    @staticmethod
    def TryParse(s: str, provider: System.IFormatProvider, result: ref[System.IntPtr], ) -> bool:
        ...

    @staticmethod
    def op_LeftShift(value: System.IntPtr, shiftAmount: int, ) -> System.IntPtr:
        ...

    @staticmethod
    def op_RightShift(value: System.IntPtr, shiftAmount: int, ) -> System.IntPtr:
        ...

    @staticmethod
    def Parse(s: System.ReadOnlySpan[str], provider: System.IFormatProvider, ) -> System.IntPtr:
        ...

    @staticmethod
    def TryParse(s: System.ReadOnlySpan[str], provider: System.IFormatProvider, result: ref[System.IntPtr], ) -> bool:
        ...

    @staticmethod
    def op_Subtraction(left: System.IntPtr, right: System.IntPtr, ) -> System.IntPtr:
        ...

    @staticmethod
    def op_UnaryNegation(value: System.IntPtr, ) -> System.IntPtr:
        ...

    @staticmethod
    def op_UnaryPlus(value: System.IntPtr, ) -> System.IntPtr:
        ...

    def GetObjectData(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext, ) -> None:
        ...

    @typing.overload
    def Equals(self, obj: System.Object, ) -> bool:
        ...

    @typing.overload
    def Equals(self, other: System.IntPtr, ) -> bool:
        ...

    def GetHashCode(self, ) -> int:
        ...

    def ToInt32(self, ) -> int:
        ...

    def ToInt64(self, ) -> int:
        ...

    @staticmethod
    def Add(pointer: System.IntPtr, offset: int, ) -> System.IntPtr:
        ...

    @staticmethod
    def Subtract(pointer: System.IntPtr, offset: int, ) -> System.IntPtr:
        ...

    def ToPointer(self, ) -> ptr[None]:
        ...

    @typing.overload
    def CompareTo(self, value: System.Object, ) -> int:
        ...

    @typing.overload
    def CompareTo(self, value: System.IntPtr, ) -> int:
        ...

    @typing.overload
    def ToString(self, ) -> str:
        ...

    @typing.overload
    def ToString(self, format: str, ) -> str:
        ...

    @typing.overload
    def ToString(self, provider: System.IFormatProvider, ) -> str:
        ...

    @typing.overload
    def ToString(self, format: str, provider: System.IFormatProvider, ) -> str:
        ...

    def TryFormat(self, destination: System.Span[str], charsWritten: ref[int], format: System.ReadOnlySpan[str] = ..., provider: System.IFormatProvider = ..., ) -> bool:
        ...

    @staticmethod
    @typing.overload
    def Parse(s: str, ) -> System.IntPtr:
        ...

    @staticmethod
    @typing.overload
    def Parse(s: str, style: int, ) -> System.IntPtr:
        ...

    @staticmethod
    @typing.overload
    def Parse(s: str, provider: System.IFormatProvider, ) -> System.IntPtr:
        ...

    @staticmethod
    @typing.overload
    def Parse(s: str, style: int, provider: System.IFormatProvider, ) -> System.IntPtr:
        ...

    @staticmethod
    @typing.overload
    def Parse(s: System.ReadOnlySpan[str], style: int = ..., provider: System.IFormatProvider = ..., ) -> System.IntPtr:
        ...

    @staticmethod
    @typing.overload
    def TryParse(s: str, result: ref[System.IntPtr], ) -> bool:
        ...

    @staticmethod
    @typing.overload
    def TryParse(s: str, style: int, provider: System.IFormatProvider, result: ref[System.IntPtr], ) -> bool:
        ...

    @staticmethod
    @typing.overload
    def TryParse(s: System.ReadOnlySpan[str], result: ref[System.IntPtr], ) -> bool:
        ...

    @staticmethod
    @typing.overload
    def TryParse(s: System.ReadOnlySpan[str], style: int, provider: System.IFormatProvider, result: ref[System.IntPtr], ) -> bool:
        ...

    @staticmethod
    def op_Addition(left: System.IntPtr, right: System.IntPtr, ) -> System.IntPtr:
        ...

    @staticmethod
    def LeadingZeroCount(value: System.IntPtr, ) -> System.IntPtr:
        ...

    @staticmethod
    def PopCount(value: System.IntPtr, ) -> System.IntPtr:
        ...

    @staticmethod
    def RotateLeft(value: System.IntPtr, rotateAmount: int, ) -> System.IntPtr:
        ...

    @staticmethod
    def RotateRight(value: System.IntPtr, rotateAmount: int, ) -> System.IntPtr:
        ...

    @staticmethod
    def TrailingZeroCount(value: System.IntPtr, ) -> System.IntPtr:
        ...

    @staticmethod
    def IsPow2(value: System.IntPtr, ) -> bool:
        ...

    @staticmethod
    def Log2(value: System.IntPtr, ) -> System.IntPtr:
        ...

    @staticmethod
    def op_BitwiseAnd(left: System.IntPtr, right: System.IntPtr, ) -> System.IntPtr:
        ...

    @staticmethod
    def op_BitwiseOr(left: System.IntPtr, right: System.IntPtr, ) -> System.IntPtr:
        ...

    @staticmethod
    def op_ExclusiveOr(left: System.IntPtr, right: System.IntPtr, ) -> System.IntPtr:
        ...

    @staticmethod
    def op_OnesComplement(value: System.IntPtr, ) -> System.IntPtr:
        ...

    @staticmethod
    def op_LessThan(left: System.IntPtr, right: System.IntPtr, ) -> bool:
        ...

    @staticmethod
    def op_LessThanOrEqual(left: System.IntPtr, right: System.IntPtr, ) -> bool:
        ...

    @staticmethod
    def op_GreaterThan(left: System.IntPtr, right: System.IntPtr, ) -> bool:
        ...

    @staticmethod
    def op_GreaterThanOrEqual(left: System.IntPtr, right: System.IntPtr, ) -> bool:
        ...

    @staticmethod
    def op_Decrement(value: System.IntPtr, ) -> System.IntPtr:
        ...

    @staticmethod
    def op_Division(left: System.IntPtr, right: System.IntPtr, ) -> System.IntPtr:
        ...

    @staticmethod
    def op_Equality(left: System.IntPtr, right: System.IntPtr, ) -> bool:
        ...

    @staticmethod
    def op_Inequality(left: System.IntPtr, right: System.IntPtr, ) -> bool:
        ...

class Decimal(System.ISpanFormattable, System.IFormattable, System.IComparable, System.IConvertible, System.IComparable[System.Decimal], System.IEquatable[System.Decimal], System.Runtime.Serialization.ISerializable, System.Runtime.Serialization.IDeserializationCallback, System.IMinMaxValue[System.Decimal], System.ISignedNumber[System.Decimal], System.INumber[System.Decimal], System.IAdditionOperators[System.Decimal, System.Decimal, System.Decimal], System.IAdditiveIdentity[System.Decimal, System.Decimal], System.IComparisonOperators[System.Decimal, System.Decimal], System.IEqualityOperators[System.Decimal, System.Decimal], System.IDecrementOperators[System.Decimal], System.IDivisionOperators[System.Decimal, System.Decimal, System.Decimal], System.IIncrementOperators[System.Decimal], System.IModulusOperators[System.Decimal, System.Decimal, System.Decimal], System.IMultiplicativeIdentity[System.Decimal, System.Decimal], System.IMultiplyOperators[System.Decimal, System.Decimal, System.Decimal], System.ISpanParseable[System.Decimal], System.IParseable[System.Decimal], System.ISubtractionOperators[System.Decimal, System.Decimal, System.Decimal], System.IUnaryNegationOperators[System.Decimal, System.Decimal], System.IUnaryPlusOperators[System.Decimal, System.Decimal], System.ValueType):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields
    Zero: System.Decimal = ...
    One: System.Decimal = ...
    MinusOne: System.Decimal = ...
    MaxValue: System.Decimal = ...
    MinValue: System.Decimal = ...

    # properties
    @property
    def AdditiveIdentity(self) -> System.Decimal:
        ...

    @property
    def MinValue(self) -> System.Decimal:
        ...

    @property
    def MaxValue(self) -> System.Decimal:
        ...

    @property
    def MultiplicativeIdentity(self) -> System.Decimal:
        ...

    @property
    def One(self) -> System.Decimal:
        ...

    @property
    def Zero(self) -> System.Decimal:
        ...

    @property
    def NegativeOne(self) -> System.Decimal:
        ...

    @property
    def High(self) -> int:
        ...

    @property
    def Low(self) -> int:
        ...

    @property
    def Mid(self) -> int:
        ...

    @property
    def IsNegative(self) -> bool:
        ...

    @property
    def Scale(self) -> int:
        ...

    @property
    def Low64(self) -> int:
        ...

    # methods
    @typing.overload
    def __init__(self, value: System.Currency, ):
        ...

    @typing.overload
    def __init__(self, value: int, ):
        ...

    @typing.overload
    def __init__(self, value: int, ):
        ...

    @typing.overload
    def __init__(self, value: int, ):
        ...

    @typing.overload
    def __init__(self, value: int, ):
        ...

    @typing.overload
    def __init__(self, value: float, ):
        ...

    @typing.overload
    def __init__(self, value: float, ):
        ...

    @typing.overload
    def __init__(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext, ):
        ...

    @typing.overload
    def __init__(self, bits: System.Array[int], ):
        ...

    @typing.overload
    def __init__(self, bits: System.ReadOnlySpan[int], ):
        ...

    @typing.overload
    def __init__(self, lo: int, mid: int, hi: int, isNegative: bool, scale: int, ):
        ...

    @typing.overload
    def __init__(self, lo: int, mid: int, hi: int, flags: int, ):
        ...

    @typing.overload
    def __init__(self, d: ref[System.Decimal], flags: int, ):
        ...

    @staticmethod
    def op_LessThan(left: System.Decimal, right: System.Decimal, ) -> bool:
        ...

    @staticmethod
    def op_LessThanOrEqual(left: System.Decimal, right: System.Decimal, ) -> bool:
        ...

    @staticmethod
    def op_GreaterThan(left: System.Decimal, right: System.Decimal, ) -> bool:
        ...

    @staticmethod
    def op_GreaterThanOrEqual(left: System.Decimal, right: System.Decimal, ) -> bool:
        ...

    @staticmethod
    def op_Decrement(value: System.Decimal, ) -> System.Decimal:
        ...

    @staticmethod
    def op_Division(left: System.Decimal, right: System.Decimal, ) -> System.Decimal:
        ...

    @staticmethod
    def op_Equality(left: System.Decimal, right: System.Decimal, ) -> bool:
        ...

    @staticmethod
    def op_Inequality(left: System.Decimal, right: System.Decimal, ) -> bool:
        ...

    @staticmethod
    def op_Increment(value: System.Decimal, ) -> System.Decimal:
        ...

    @staticmethod
    def op_Modulus(left: System.Decimal, right: System.Decimal, ) -> System.Decimal:
        ...

    @staticmethod
    def op_Multiply(left: System.Decimal, right: System.Decimal, ) -> System.Decimal:
        ...

    @staticmethod
    def Abs(value: System.Decimal, ) -> System.Decimal:
        ...

    @staticmethod
    def Create(value: TOther, ) -> System.Decimal:
        ...

    @staticmethod
    def CreateSaturating(value: TOther, ) -> System.Decimal:
        ...

    @staticmethod
    def CreateTruncating(value: TOther, ) -> System.Decimal:
        ...

    @staticmethod
    def Clamp(value: System.Decimal, min: System.Decimal, max: System.Decimal, ) -> System.Decimal:
        ...

    @staticmethod
    def DivRem(left: System.Decimal, right: System.Decimal, ) -> System.ValueTuple[System.Decimal, System.Decimal]:
        ...

    @staticmethod
    def Max(x: System.Decimal, y: System.Decimal, ) -> System.Decimal:
        ...

    @staticmethod
    def Min(x: System.Decimal, y: System.Decimal, ) -> System.Decimal:
        ...

    @staticmethod
    @typing.overload
    def Parse(s: str, style: int, provider: System.IFormatProvider, ) -> System.Decimal:
        ...

    @staticmethod
    @typing.overload
    def Parse(s: System.ReadOnlySpan[str], style: int, provider: System.IFormatProvider, ) -> System.Decimal:
        ...

    @staticmethod
    def Sign(value: System.Decimal, ) -> System.Decimal:
        ...

    @staticmethod
    def TryCreate(value: TOther, result: ref[System.Decimal], ) -> bool:
        ...

    @staticmethod
    @typing.overload
    def TryParse(s: str, style: int, provider: System.IFormatProvider, result: ref[System.Decimal], ) -> bool:
        ...

    @staticmethod
    @typing.overload
    def TryParse(s: System.ReadOnlySpan[str], style: int, provider: System.IFormatProvider, result: ref[System.Decimal], ) -> bool:
        ...

    @staticmethod
    def Parse(s: str, provider: System.IFormatProvider, ) -> System.Decimal:
        ...

    @staticmethod
    def TryParse(s: str, provider: System.IFormatProvider, result: ref[System.Decimal], ) -> bool:
        ...

    @staticmethod
    def Parse(s: System.ReadOnlySpan[str], provider: System.IFormatProvider, ) -> System.Decimal:
        ...

    @staticmethod
    def TryParse(s: System.ReadOnlySpan[str], provider: System.IFormatProvider, result: ref[System.Decimal], ) -> bool:
        ...

    @staticmethod
    def op_Subtraction(left: System.Decimal, right: System.Decimal, ) -> System.Decimal:
        ...

    @staticmethod
    def op_UnaryNegation(value: System.Decimal, ) -> System.Decimal:
        ...

    @staticmethod
    def op_UnaryPlus(value: System.Decimal, ) -> System.Decimal:
        ...

    @staticmethod
    def AsMutable(d: ref[System.Decimal], ) -> ref[System.Decimal.DecCalc]:
        ...

    @staticmethod
    def DecDivMod1E9(value: ref[System.Decimal], ) -> int:
        ...

    def GetTypeCode(self, ) -> int:
        ...

    def ToBoolean(self, provider: System.IFormatProvider, ) -> bool:
        ...

    def ToChar(self, provider: System.IFormatProvider, ) -> str:
        ...

    def ToSByte(self, provider: System.IFormatProvider, ) -> int:
        ...

    def ToByte(self, provider: System.IFormatProvider, ) -> int:
        ...

    def ToInt16(self, provider: System.IFormatProvider, ) -> int:
        ...

    def ToUInt16(self, provider: System.IFormatProvider, ) -> int:
        ...

    def ToInt32(self, provider: System.IFormatProvider, ) -> int:
        ...

    def ToUInt32(self, provider: System.IFormatProvider, ) -> int:
        ...

    def ToInt64(self, provider: System.IFormatProvider, ) -> int:
        ...

    def ToUInt64(self, provider: System.IFormatProvider, ) -> int:
        ...

    def ToSingle(self, provider: System.IFormatProvider, ) -> float:
        ...

    def ToDouble(self, provider: System.IFormatProvider, ) -> float:
        ...

    def ToDecimal(self, provider: System.IFormatProvider, ) -> System.Decimal:
        ...

    def ToDateTime(self, provider: System.IFormatProvider, ) -> System.DateTime:
        ...

    def ToType(self, type: System.Type, provider: System.IFormatProvider, ) -> System.Object:
        ...

    @staticmethod
    def op_Addition(left: System.Decimal, right: System.Decimal, ) -> System.Decimal:
        ...

    def GetObjectData(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext, ) -> None:
        ...

    @staticmethod
    def FromOACurrency(cy: int, ) -> System.Decimal:
        ...

    @staticmethod
    def ToOACurrency(value: System.Decimal, ) -> int:
        ...

    @staticmethod
    def IsValid(flags: int, ) -> bool:
        ...

    def OnDeserialization(self, sender: System.Object, ) -> None:
        ...

    @staticmethod
    def Abs(d: ref[System.Decimal], ) -> System.Decimal:
        ...

    @staticmethod
    def Add(d1: System.Decimal, d2: System.Decimal, ) -> System.Decimal:
        ...

    @staticmethod
    def Ceiling(d: System.Decimal, ) -> System.Decimal:
        ...

    @staticmethod
    def Compare(d1: System.Decimal, d2: System.Decimal, ) -> int:
        ...

    @typing.overload
    def CompareTo(self, value: System.Object, ) -> int:
        ...

    @typing.overload
    def CompareTo(self, value: System.Decimal, ) -> int:
        ...

    @staticmethod
    def Divide(d1: System.Decimal, d2: System.Decimal, ) -> System.Decimal:
        ...

    @typing.overload
    def Equals(self, value: System.Object, ) -> bool:
        ...

    @typing.overload
    def Equals(self, value: System.Decimal, ) -> bool:
        ...

    @staticmethod
    @typing.overload
    def Equals(d1: System.Decimal, d2: System.Decimal, ) -> bool:
        ...

    def GetHashCode(self, ) -> int:
        ...

    @staticmethod
    def Floor(d: System.Decimal, ) -> System.Decimal:
        ...

    @typing.overload
    def ToString(self, ) -> str:
        ...

    @typing.overload
    def ToString(self, format: str, ) -> str:
        ...

    @typing.overload
    def ToString(self, provider: System.IFormatProvider, ) -> str:
        ...

    @typing.overload
    def ToString(self, format: str, provider: System.IFormatProvider, ) -> str:
        ...

    def TryFormat(self, destination: System.Span[str], charsWritten: ref[int], format: System.ReadOnlySpan[str] = ..., provider: System.IFormatProvider = ..., ) -> bool:
        ...

    @staticmethod
    @typing.overload
    def Parse(s: str, ) -> System.Decimal:
        ...

    @staticmethod
    @typing.overload
    def Parse(s: str, style: int, ) -> System.Decimal:
        ...

    @staticmethod
    @typing.overload
    def Parse(s: str, provider: System.IFormatProvider, ) -> System.Decimal:
        ...

    @staticmethod
    @typing.overload
    def Parse(s: str, style: int, provider: System.IFormatProvider, ) -> System.Decimal:
        ...

    @staticmethod
    @typing.overload
    def Parse(s: System.ReadOnlySpan[str], style: int = ..., provider: System.IFormatProvider = ..., ) -> System.Decimal:
        ...

    @staticmethod
    @typing.overload
    def TryParse(s: str, result: ref[System.Decimal], ) -> bool:
        ...

    @staticmethod
    @typing.overload
    def TryParse(s: System.ReadOnlySpan[str], result: ref[System.Decimal], ) -> bool:
        ...

    @staticmethod
    @typing.overload
    def TryParse(s: str, style: int, provider: System.IFormatProvider, result: ref[System.Decimal], ) -> bool:
        ...

    @staticmethod
    @typing.overload
    def TryParse(s: System.ReadOnlySpan[str], style: int, provider: System.IFormatProvider, result: ref[System.Decimal], ) -> bool:
        ...

    @staticmethod
    @typing.overload
    def GetBits(d: System.Decimal, ) -> System.Array[int]:
        ...

    @staticmethod
    @typing.overload
    def GetBits(d: System.Decimal, destination: System.Span[int], ) -> int:
        ...

    @staticmethod
    def TryGetBits(d: System.Decimal, destination: System.Span[int], valuesWritten: ref[int], ) -> bool:
        ...

    @staticmethod
    def GetBytes(d: ref[System.Decimal], buffer: System.Span[int], ) -> None:
        ...

    @staticmethod
    def ToDecimal(span: System.ReadOnlySpan[int], ) -> System.Decimal:
        ...

    @staticmethod
    def Max(d1: ref[System.Decimal], d2: ref[System.Decimal], ) -> ref[System.Decimal]:
        ...

    @staticmethod
    def Min(d1: ref[System.Decimal], d2: ref[System.Decimal], ) -> ref[System.Decimal]:
        ...

    @staticmethod
    def Remainder(d1: System.Decimal, d2: System.Decimal, ) -> System.Decimal:
        ...

    @staticmethod
    def Multiply(d1: System.Decimal, d2: System.Decimal, ) -> System.Decimal:
        ...

    @staticmethod
    def Negate(d: System.Decimal, ) -> System.Decimal:
        ...

    @staticmethod
    @typing.overload
    def Round(d: System.Decimal, ) -> System.Decimal:
        ...

    @staticmethod
    @typing.overload
    def Round(d: System.Decimal, decimals: int, ) -> System.Decimal:
        ...

    @staticmethod
    @typing.overload
    def Round(d: System.Decimal, mode: int, ) -> System.Decimal:
        ...

    @staticmethod
    @typing.overload
    def Round(d: System.Decimal, decimals: int, mode: int, ) -> System.Decimal:
        ...

    @staticmethod
    @typing.overload
    def Round(d: ref[System.Decimal], decimals: int, mode: int, ) -> System.Decimal:
        ...

    @staticmethod
    def Sign(d: ref[System.Decimal], ) -> int:
        ...

    @staticmethod
    def Subtract(d1: System.Decimal, d2: System.Decimal, ) -> System.Decimal:
        ...

    @staticmethod
    def ToByte(value: System.Decimal, ) -> int:
        ...

    @staticmethod
    def ToSByte(value: System.Decimal, ) -> int:
        ...

    @staticmethod
    def ToInt16(value: System.Decimal, ) -> int:
        ...

    @staticmethod
    def ToDouble(d: System.Decimal, ) -> float:
        ...

    @staticmethod
    def ToInt32(d: System.Decimal, ) -> int:
        ...

    @staticmethod
    def ToInt64(d: System.Decimal, ) -> int:
        ...

    @staticmethod
    def ToUInt16(value: System.Decimal, ) -> int:
        ...

    @staticmethod
    def ToUInt32(d: System.Decimal, ) -> int:
        ...

    @staticmethod
    def ToUInt64(d: System.Decimal, ) -> int:
        ...

    @staticmethod
    def ToSingle(d: System.Decimal, ) -> float:
        ...

    @staticmethod
    @typing.overload
    def Truncate(d: System.Decimal, ) -> System.Decimal:
        ...

    @staticmethod
    @typing.overload
    def Truncate(d: ref[System.Decimal], ) -> None:
        ...

class MidpointRounding(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    ToEven: int = ...
    AwayFromZero: int = ...
    ToZero: int = ...
    ToNegativeInfinity: int = ...
    ToPositiveInfinity: int = ...

Byte = int

class Func(System.ICloneable, System.Runtime.Serialization.ISerializable, System.MulticastDelegate, typing.Generic[T1, T2, T3, TResult]):
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

    def Invoke(self, arg1: T1, arg2: T2, arg3: T3, ) -> TResult:
        ...

    def BeginInvoke(self, arg1: T1, arg2: T2, arg3: T3, callback: System.AsyncCallback, object: System.Object, ) -> System.IAsyncResult:
        ...

    def EndInvoke(self, result: System.IAsyncResult, ) -> TResult:
        ...

class IUnaryNegationOperators(abc.ABC, typing.Generic[TSelf, TResult]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
class ICloneable(abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    @abc.abstractmethod
    def Clone(self, ) -> System.Object:
        ...

class Func(System.ICloneable, System.Runtime.Serialization.ISerializable, System.MulticastDelegate, typing.Generic[T, TResult]):
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

    def Invoke(self, arg: T, ) -> TResult:
        ...

    def BeginInvoke(self, arg: T, callback: System.AsyncCallback, object: System.Object, ) -> System.IAsyncResult:
        ...

    def EndInvoke(self, result: System.IAsyncResult, ) -> TResult:
        ...

class IMultiplicativeIdentity(abc.ABC, typing.Generic[TSelf, TResult]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    @abc.abstractmethod
    def MultiplicativeIdentity(self) -> TResult:
        ...

    # methods
class IAsyncResult(abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    @abc.abstractmethod
    def IsCompleted(self) -> bool:
        ...

    @property
    @abc.abstractmethod
    def AsyncWaitHandle(self) -> System.Threading.WaitHandle:
        ...

    @property
    @abc.abstractmethod
    def AsyncState(self) -> System.Object:
        ...

    @property
    @abc.abstractmethod
    def CompletedSynchronously(self) -> bool:
        ...

    # methods
class IModulusOperators(abc.ABC, typing.Generic[TSelf, TOther, TResult]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
class ReadOnlyMemory(System.IEquatable[System.ReadOnlyMemory], System.ValueType, typing.Generic[T]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields
    RemoveFlagsBitMask: int = ...

    # properties
    @property
    def Empty(self) -> System.ReadOnlyMemory:
        ...

    @property
    def Length(self) -> int:
        ...

    @property
    def IsEmpty(self) -> bool:
        ...

    @property
    def Span(self) -> System.ReadOnlySpan[T]:
        ...

    # methods
    @typing.overload
    def __init__(self, array: System.Array[T], ):
        ...

    @typing.overload
    def __init__(self, array: System.Array[T], start: int, length: int, ):
        ...

    @typing.overload
    def __init__(self, obj: System.Object, start: int, length: int, ):
        ...

    def ToString(self, ) -> str:
        ...

    @typing.overload
    def Slice(self, start: int, ) -> System.ReadOnlyMemory:
        ...

    @typing.overload
    def Slice(self, start: int, length: int, ) -> System.ReadOnlyMemory:
        ...

    def CopyTo(self, destination: System.Memory[T], ) -> None:
        ...

    def TryCopyTo(self, destination: System.Memory[T], ) -> bool:
        ...

    def Pin(self, ) -> System.Buffers.MemoryHandle:
        ...

    def ToArray(self, ) -> System.Array[T]:
        ...

    @typing.overload
    def Equals(self, obj: System.Object, ) -> bool:
        ...

    @typing.overload
    def Equals(self, other: System.ReadOnlyMemory, ) -> bool:
        ...

    def GetHashCode(self, ) -> int:
        ...

    def GetObjectStartLength(self, start: ref[int], length: ref[int], ) -> System.Object:
        ...

class Object():
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    def __init__(self, ):
        ...

    def ToString(self, ) -> str:
        ...

    @typing.overload
    def Equals(self, obj: System.Object, ) -> bool:
        ...

    @staticmethod
    @typing.overload
    def Equals(objA: System.Object, objB: System.Object, ) -> bool:
        ...

    def GetHashCode(self, ) -> int:
        ...

    def GetType(self, ) -> System.Type:
        ...

    def MemberwiseClone(self, ) -> System.Object:
        ...

    def Finalize(self, ) -> None:
        ...

    @staticmethod
    def ReferenceEquals(objA: System.Object, objB: System.Object, ) -> bool:
        ...

class RuntimeMethodHandle(System.Runtime.Serialization.ISerializable, System.ValueType):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def Value(self) -> System.IntPtr:
        ...

    # methods
    def __init__(self, method: System.IRuntimeMethodInfo, ):
        ...

    @staticmethod
    def EnsureNonNullMethodInfo(method: System.IRuntimeMethodInfo, ) -> System.IRuntimeMethodInfo:
        ...

    def GetMethodInfo(self, ) -> System.IRuntimeMethodInfo:
        ...

    @staticmethod
    def GetValueInternal(rmh: System.RuntimeMethodHandle, ) -> System.IntPtr:
        ...

    def GetObjectData(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext, ) -> None:
        ...

    def GetHashCode(self, ) -> int:
        ...

    @typing.overload
    def Equals(self, obj: System.Object, ) -> bool:
        ...

    @typing.overload
    def Equals(self, handle: System.RuntimeMethodHandle, ) -> bool:
        ...

    def IsNullHandle(self, ) -> bool:
        ...

    @staticmethod
    @typing.overload
    def GetFunctionPointer(handle: System.RuntimeMethodHandleInternal, ) -> System.IntPtr:
        ...

    @typing.overload
    def GetFunctionPointer(self, ) -> System.IntPtr:
        ...

    @staticmethod
    def GetIsCollectible(handle: System.RuntimeMethodHandleInternal, ) -> int:
        ...

    @staticmethod
    def IsCAVisibleFromDecoratedType(attrTypeHandle: System.Runtime.CompilerServices.QCallTypeHandle, attrCtor: System.RuntimeMethodHandleInternal, sourceTypeHandle: System.Runtime.CompilerServices.QCallTypeHandle, sourceModule: System.Runtime.CompilerServices.QCallModule, ) -> int:
        ...

    @staticmethod
    def _GetCurrentMethod(stackMark: ref[int], ) -> System.IRuntimeMethodInfo:
        ...

    @staticmethod
    def GetCurrentMethod(stackMark: ref[int], ) -> System.IRuntimeMethodInfo:
        ...

    @staticmethod
    @typing.overload
    def GetAttributes(method: System.RuntimeMethodHandleInternal, ) -> int:
        ...

    @staticmethod
    @typing.overload
    def GetAttributes(method: System.IRuntimeMethodInfo, ) -> int:
        ...

    @staticmethod
    def GetImplAttributes(method: System.IRuntimeMethodInfo, ) -> int:
        ...

    @staticmethod
    @typing.overload
    def ConstructInstantiation(method: System.RuntimeMethodHandleInternal, format: int, retString: System.Runtime.CompilerServices.StringHandleOnStack, ) -> None:
        ...

    @staticmethod
    @typing.overload
    def ConstructInstantiation(method: System.IRuntimeMethodInfo, format: int, ) -> str:
        ...

    @staticmethod
    @typing.overload
    def GetDeclaringType(method: System.RuntimeMethodHandleInternal, ) -> System.RuntimeType:
        ...

    @staticmethod
    @typing.overload
    def GetDeclaringType(method: System.IRuntimeMethodInfo, ) -> System.RuntimeType:
        ...

    @staticmethod
    @typing.overload
    def GetSlot(method: System.RuntimeMethodHandleInternal, ) -> int:
        ...

    @staticmethod
    @typing.overload
    def GetSlot(method: System.IRuntimeMethodInfo, ) -> int:
        ...

    @staticmethod
    def GetMethodDef(method: System.IRuntimeMethodInfo, ) -> int:
        ...

    @staticmethod
    @typing.overload
    def GetName(method: System.RuntimeMethodHandleInternal, ) -> str:
        ...

    @staticmethod
    @typing.overload
    def GetName(method: System.IRuntimeMethodInfo, ) -> str:
        ...

    @staticmethod
    def _GetUtf8Name(method: System.RuntimeMethodHandleInternal, ) -> ptr[None]:
        ...

    @staticmethod
    def GetUtf8Name(method: System.RuntimeMethodHandleInternal, ) -> System.MdUtf8String:
        ...

    @staticmethod
    def MatchesNameHash(method: System.RuntimeMethodHandleInternal, hash: int, ) -> bool:
        ...

    @staticmethod
    def InvokeMethod(target: System.Object, arguments: ref[System.Span[System.Object]], sig: System.Signature, constructor: bool, wrapExceptions: bool, ) -> System.Object:
        ...

    @staticmethod
    def GetMethodInstantiation(method: System.RuntimeMethodHandleInternal, types: System.Runtime.CompilerServices.ObjectHandleOnStack, fAsRuntimeTypeArray: int, ) -> None:
        ...

    @staticmethod
    @typing.overload
    def GetMethodInstantiationInternal(method: System.IRuntimeMethodInfo, ) -> System.Array[System.RuntimeType]:
        ...

    @staticmethod
    @typing.overload
    def GetMethodInstantiationInternal(method: System.RuntimeMethodHandleInternal, ) -> System.Array[System.RuntimeType]:
        ...

    @staticmethod
    def GetMethodInstantiationPublic(method: System.IRuntimeMethodInfo, ) -> System.Array[System.Type]:
        ...

    @staticmethod
    @typing.overload
    def HasMethodInstantiation(method: System.RuntimeMethodHandleInternal, ) -> bool:
        ...

    @staticmethod
    @typing.overload
    def HasMethodInstantiation(method: System.IRuntimeMethodInfo, ) -> bool:
        ...

    @staticmethod
    def GetStubIfNeeded(method: System.RuntimeMethodHandleInternal, declaringType: System.RuntimeType, methodInstantiation: System.Array[System.RuntimeType], ) -> System.RuntimeMethodHandleInternal:
        ...

    @staticmethod
    def GetMethodFromCanonical(method: System.RuntimeMethodHandleInternal, declaringType: System.RuntimeType, ) -> System.RuntimeMethodHandleInternal:
        ...

    @staticmethod
    @typing.overload
    def IsGenericMethodDefinition(method: System.RuntimeMethodHandleInternal, ) -> bool:
        ...

    @staticmethod
    @typing.overload
    def IsGenericMethodDefinition(method: System.IRuntimeMethodInfo, ) -> bool:
        ...

    @staticmethod
    def IsTypicalMethodDefinition(method: System.IRuntimeMethodInfo, ) -> bool:
        ...

    @staticmethod
    @typing.overload
    def GetTypicalMethodDefinition(method: System.RuntimeMethodHandleInternal, outMethod: System.Runtime.CompilerServices.ObjectHandleOnStack, ) -> None:
        ...

    @staticmethod
    @typing.overload
    def GetTypicalMethodDefinition(method: System.IRuntimeMethodInfo, ) -> System.IRuntimeMethodInfo:
        ...

    @staticmethod
    @typing.overload
    def GetGenericParameterCount(method: System.RuntimeMethodHandleInternal, ) -> int:
        ...

    @staticmethod
    @typing.overload
    def GetGenericParameterCount(method: System.IRuntimeMethodInfo, ) -> int:
        ...

    @staticmethod
    @typing.overload
    def StripMethodInstantiation(method: System.RuntimeMethodHandleInternal, outMethod: System.Runtime.CompilerServices.ObjectHandleOnStack, ) -> None:
        ...

    @staticmethod
    @typing.overload
    def StripMethodInstantiation(method: System.IRuntimeMethodInfo, ) -> System.IRuntimeMethodInfo:
        ...

    @staticmethod
    def IsDynamicMethod(method: System.RuntimeMethodHandleInternal, ) -> bool:
        ...

    @staticmethod
    def Destroy(method: System.RuntimeMethodHandleInternal, ) -> None:
        ...

    @staticmethod
    def GetResolver(method: System.RuntimeMethodHandleInternal, ) -> System.Resolver:
        ...

    @staticmethod
    def GetMethodBody(method: System.IRuntimeMethodInfo, declaringType: System.RuntimeType, ) -> System.Reflection.RuntimeMethodBody:
        ...

    @staticmethod
    def IsConstructor(method: System.RuntimeMethodHandleInternal, ) -> bool:
        ...

    @staticmethod
    def GetLoaderAllocator(method: System.RuntimeMethodHandleInternal, ) -> System.Reflection.LoaderAllocator:
        ...

class IBinaryNumber(System.IBitwiseOperators[TSelf, TSelf, TSelf], System.INumber[TSelf], System.IAdditionOperators[TSelf, TSelf, TSelf], System.IAdditiveIdentity[TSelf, TSelf], System.IComparisonOperators[TSelf, TSelf], System.IComparable, System.IComparable[TSelf], System.IEqualityOperators[TSelf, TSelf], System.IEquatable[TSelf], System.IDecrementOperators[TSelf], System.IDivisionOperators[TSelf, TSelf, TSelf], System.IIncrementOperators[TSelf], System.IModulusOperators[TSelf, TSelf, TSelf], System.IMultiplicativeIdentity[TSelf, TSelf], System.IMultiplyOperators[TSelf, TSelf, TSelf], System.ISpanFormattable, System.IFormattable, System.ISpanParseable[TSelf], System.IParseable[TSelf], System.ISubtractionOperators[TSelf, TSelf, TSelf], System.IUnaryNegationOperators[TSelf, TSelf], System.IUnaryPlusOperators[TSelf, TSelf], abc.ABC, typing.Generic[TSelf]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    @staticmethod
    @abc.abstractmethod
    def IsPow2(value: TSelf, ) -> bool:
        ...

    @staticmethod
    @abc.abstractmethod
    def Log2(value: TSelf, ) -> TSelf:
        ...

UInt32 = int

class Tuple(System.Collections.IStructuralEquatable, System.Collections.IStructuralComparable, System.IComparable, System.ITupleInternal, System.Runtime.CompilerServices.ITuple, System.Object, typing.Generic[T1, T2]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def Item1(self) -> T1:
        ...

    @property
    def Item2(self) -> T2:
        ...

    @property
    def Length(self) -> int:
        ...

    @property
    def Item(self) -> System.Object:
        ...

    # methods
    def __init__(self, item1: T1, item2: T2, ):
        ...

    @typing.overload
    def Equals(self, obj: System.Object, ) -> bool:
        ...

    @typing.overload
    def Equals(self, other: System.Object, comparer: System.Collections.IEqualityComparer, ) -> bool:
        ...

    def Equals(self, other: System.Object, comparer: System.Collections.IEqualityComparer, ) -> bool:
        ...

    def CompareTo(self, obj: System.Object, ) -> int:
        ...

    def CompareTo(self, other: System.Object, comparer: System.Collections.IComparer, ) -> int:
        ...

    def CompareTo(self, other: System.Object, comparer: System.Collections.IComparer, ) -> int:
        ...

    @typing.overload
    def GetHashCode(self, ) -> int:
        ...

    @typing.overload
    def GetHashCode(self, comparer: System.Collections.IEqualityComparer, ) -> int:
        ...

    def GetHashCode(self, comparer: System.Collections.IEqualityComparer, ) -> int:
        ...

    def GetHashCode(self, comparer: System.Collections.IEqualityComparer, ) -> int:
        ...

    @typing.overload
    def ToString(self, ) -> str:
        ...

    @typing.overload
    def ToString(self, sb: System.Text.StringBuilder, ) -> str:
        ...

    def ToString(self, sb: System.Text.StringBuilder, ) -> str:
        ...

UInt64 = int

class DateTime(System.IComparable, System.ISpanFormattable, System.IFormattable, System.IConvertible, System.IComparable[System.DateTime], System.IEquatable[System.DateTime], System.Runtime.Serialization.ISerializable, System.IAdditionOperators[System.DateTime, System.TimeSpan, System.DateTime], System.IAdditiveIdentity[System.DateTime, System.TimeSpan], System.IComparisonOperators[System.DateTime, System.DateTime], System.IEqualityOperators[System.DateTime, System.DateTime], System.IMinMaxValue[System.DateTime], System.ISpanParseable[System.DateTime], System.IParseable[System.DateTime], System.ISubtractionOperators[System.DateTime, System.TimeSpan, System.DateTime], System.ISubtractionOperators[System.DateTime, System.DateTime, System.TimeSpan], System.ValueType):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields
    MinValue: System.DateTime = ...
    MaxValue: System.DateTime = ...
    UnixEpoch: System.DateTime = ...

    # properties
    @property
    def DaysInMonth365(self) -> System.ReadOnlySpan[int]:
        ...

    @property
    def DaysInMonth366(self) -> System.ReadOnlySpan[int]:
        ...

    @property
    def UTicks(self) -> int:
        ...

    @property
    def InternalKind(self) -> int:
        ...

    @property
    def Date(self) -> System.DateTime:
        ...

    @property
    def Day(self) -> int:
        ...

    @property
    def DayOfWeek(self) -> int:
        ...

    @property
    def DayOfYear(self) -> int:
        ...

    @property
    def Hour(self) -> int:
        ...

    @property
    def Kind(self) -> int:
        ...

    @property
    def Millisecond(self) -> int:
        ...

    @property
    def Minute(self) -> int:
        ...

    @property
    def Month(self) -> int:
        ...

    @property
    def Now(self) -> System.DateTime:
        ...

    @property
    def Second(self) -> int:
        ...

    @property
    def Ticks(self) -> int:
        ...

    @property
    def TimeOfDay(self) -> System.TimeSpan:
        ...

    @property
    def Today(self) -> System.DateTime:
        ...

    @property
    def Year(self) -> int:
        ...

    @property
    def AdditiveIdentity(self) -> System.TimeSpan:
        ...

    @property
    def MinValue(self) -> System.DateTime:
        ...

    @property
    def MaxValue(self) -> System.DateTime:
        ...

    @property
    def UtcNow(self) -> System.DateTime:
        ...

    # methods
    @typing.overload
    def __init__(self, ticks: int, ):
        ...

    @typing.overload
    def __init__(self, dateData: int, ):
        ...

    @typing.overload
    def __init__(self, ticks: int, kind: int, ):
        ...

    @typing.overload
    def __init__(self, ticks: int, kind: int, isAmbiguousDst: bool, ):
        ...

    @typing.overload
    def __init__(self, year: int, month: int, day: int, ):
        ...

    @typing.overload
    def __init__(self, year: int, month: int, day: int, calendar: System.Globalization.Calendar, ):
        ...

    @typing.overload
    def __init__(self, year: int, month: int, day: int, hour: int, minute: int, second: int, ):
        ...

    @typing.overload
    def __init__(self, year: int, month: int, day: int, hour: int, minute: int, second: int, kind: int, ):
        ...

    @typing.overload
    def __init__(self, year: int, month: int, day: int, hour: int, minute: int, second: int, calendar: System.Globalization.Calendar, ):
        ...

    @typing.overload
    def __init__(self, year: int, month: int, day: int, hour: int, minute: int, second: int, millisecond: int, ):
        ...

    @typing.overload
    def __init__(self, year: int, month: int, day: int, hour: int, minute: int, second: int, millisecond: int, kind: int, ):
        ...

    @typing.overload
    def __init__(self, year: int, month: int, day: int, hour: int, minute: int, second: int, millisecond: int, calendar: System.Globalization.Calendar, ):
        ...

    @typing.overload
    def __init__(self, year: int, month: int, day: int, hour: int, minute: int, second: int, millisecond: int, calendar: System.Globalization.Calendar, kind: int, ):
        ...

    @typing.overload
    def __init__(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext, ):
        ...

    def ToDecimal(self, provider: System.IFormatProvider, ) -> System.Decimal:
        ...

    @staticmethod
    def InvalidCast(to: str, ) -> System.Exception:
        ...

    def ToDateTime(self, provider: System.IFormatProvider, ) -> System.DateTime:
        ...

    def ToType(self, type: System.Type, provider: System.IFormatProvider, ) -> System.Object:
        ...

    @staticmethod
    def TryCreate(year: int, month: int, day: int, hour: int, minute: int, second: int, millisecond: int, result: ref[System.DateTime], ) -> bool:
        ...

    @staticmethod
    def op_Addition(left: System.DateTime, right: System.TimeSpan, ) -> System.DateTime:
        ...

    @staticmethod
    def op_LessThan(left: System.DateTime, right: System.DateTime, ) -> bool:
        ...

    @staticmethod
    def op_LessThanOrEqual(left: System.DateTime, right: System.DateTime, ) -> bool:
        ...

    @staticmethod
    def op_GreaterThan(left: System.DateTime, right: System.DateTime, ) -> bool:
        ...

    @staticmethod
    def op_GreaterThanOrEqual(left: System.DateTime, right: System.DateTime, ) -> bool:
        ...

    @staticmethod
    def op_Equality(left: System.DateTime, right: System.DateTime, ) -> bool:
        ...

    @staticmethod
    def op_Inequality(left: System.DateTime, right: System.DateTime, ) -> bool:
        ...

    @staticmethod
    def Parse(s: str, provider: System.IFormatProvider, ) -> System.DateTime:
        ...

    @staticmethod
    def TryParse(s: str, provider: System.IFormatProvider, result: ref[System.DateTime], ) -> bool:
        ...

    @staticmethod
    def Parse(s: System.ReadOnlySpan[str], provider: System.IFormatProvider, ) -> System.DateTime:
        ...

    @staticmethod
    def TryParse(s: System.ReadOnlySpan[str], provider: System.IFormatProvider, result: ref[System.DateTime], ) -> bool:
        ...

    @staticmethod
    def op_Subtraction(left: System.DateTime, right: System.TimeSpan, ) -> System.DateTime:
        ...

    @staticmethod
    def op_Subtraction(left: System.DateTime, right: System.DateTime, ) -> System.TimeSpan:
        ...

    @staticmethod
    def IsValidTimeWithLeapSeconds(year: int, month: int, day: int, hour: int, minute: int, kind: int, ) -> bool:
        ...

    @staticmethod
    @typing.overload
    def Parse(s: System.ReadOnlySpan[str], provider: System.IFormatProvider = ..., styles: int = ..., ) -> System.DateTime:
        ...

    @staticmethod
    @typing.overload
    def Parse(s: str, ) -> System.DateTime:
        ...

    @staticmethod
    @typing.overload
    def Parse(s: str, provider: System.IFormatProvider, ) -> System.DateTime:
        ...

    @staticmethod
    @typing.overload
    def Parse(s: str, provider: System.IFormatProvider, styles: int, ) -> System.DateTime:
        ...

    @staticmethod
    @typing.overload
    def ParseExact(s: str, format: str, provider: System.IFormatProvider, ) -> System.DateTime:
        ...

    @staticmethod
    @typing.overload
    def ParseExact(s: str, format: str, provider: System.IFormatProvider, style: int, ) -> System.DateTime:
        ...

    @staticmethod
    @typing.overload
    def ParseExact(s: System.ReadOnlySpan[str], format: System.ReadOnlySpan[str], provider: System.IFormatProvider, style: int = ..., ) -> System.DateTime:
        ...

    @staticmethod
    @typing.overload
    def ParseExact(s: str, formats: System.Array[str], provider: System.IFormatProvider, style: int, ) -> System.DateTime:
        ...

    @staticmethod
    @typing.overload
    def ParseExact(s: System.ReadOnlySpan[str], formats: System.Array[str], provider: System.IFormatProvider, style: int = ..., ) -> System.DateTime:
        ...

    @typing.overload
    def Subtract(self, value: System.DateTime, ) -> System.TimeSpan:
        ...

    @typing.overload
    def Subtract(self, value: System.TimeSpan, ) -> System.DateTime:
        ...

    @staticmethod
    def TicksToOADate(value: int, ) -> float:
        ...

    def ToOADate(self, ) -> float:
        ...

    def ToFileTime(self, ) -> int:
        ...

    def ToFileTimeUtc(self, ) -> int:
        ...

    def ToLocalTime(self, ) -> System.DateTime:
        ...

    def ToLongDateString(self, ) -> str:
        ...

    def ToLongTimeString(self, ) -> str:
        ...

    def ToShortDateString(self, ) -> str:
        ...

    def ToShortTimeString(self, ) -> str:
        ...

    @typing.overload
    def ToString(self, ) -> str:
        ...

    @typing.overload
    def ToString(self, format: str, ) -> str:
        ...

    @typing.overload
    def ToString(self, provider: System.IFormatProvider, ) -> str:
        ...

    @typing.overload
    def ToString(self, format: str, provider: System.IFormatProvider, ) -> str:
        ...

    def TryFormat(self, destination: System.Span[str], charsWritten: ref[int], format: System.ReadOnlySpan[str] = ..., provider: System.IFormatProvider = ..., ) -> bool:
        ...

    def ToUniversalTime(self, ) -> System.DateTime:
        ...

    @staticmethod
    @typing.overload
    def TryParse(s: str, result: ref[System.DateTime], ) -> bool:
        ...

    @staticmethod
    @typing.overload
    def TryParse(s: System.ReadOnlySpan[str], result: ref[System.DateTime], ) -> bool:
        ...

    @staticmethod
    @typing.overload
    def TryParse(s: str, provider: System.IFormatProvider, styles: int, result: ref[System.DateTime], ) -> bool:
        ...

    @staticmethod
    @typing.overload
    def TryParse(s: System.ReadOnlySpan[str], provider: System.IFormatProvider, styles: int, result: ref[System.DateTime], ) -> bool:
        ...

    @staticmethod
    @typing.overload
    def TryParseExact(s: str, format: str, provider: System.IFormatProvider, style: int, result: ref[System.DateTime], ) -> bool:
        ...

    @staticmethod
    @typing.overload
    def TryParseExact(s: System.ReadOnlySpan[str], format: System.ReadOnlySpan[str], provider: System.IFormatProvider, style: int, result: ref[System.DateTime], ) -> bool:
        ...

    @staticmethod
    @typing.overload
    def TryParseExact(s: str, formats: System.Array[str], provider: System.IFormatProvider, style: int, result: ref[System.DateTime], ) -> bool:
        ...

    @staticmethod
    @typing.overload
    def TryParseExact(s: System.ReadOnlySpan[str], formats: System.Array[str], provider: System.IFormatProvider, style: int, result: ref[System.DateTime], ) -> bool:
        ...

    @typing.overload
    def GetDateTimeFormats(self, ) -> System.Array[str]:
        ...

    @typing.overload
    def GetDateTimeFormats(self, provider: System.IFormatProvider, ) -> System.Array[str]:
        ...

    @typing.overload
    def GetDateTimeFormats(self, format: str, ) -> System.Array[str]:
        ...

    @typing.overload
    def GetDateTimeFormats(self, format: str, provider: System.IFormatProvider, ) -> System.Array[str]:
        ...

    def GetTypeCode(self, ) -> int:
        ...

    def ToBoolean(self, provider: System.IFormatProvider, ) -> bool:
        ...

    def ToChar(self, provider: System.IFormatProvider, ) -> str:
        ...

    def ToSByte(self, provider: System.IFormatProvider, ) -> int:
        ...

    def ToByte(self, provider: System.IFormatProvider, ) -> int:
        ...

    def ToInt16(self, provider: System.IFormatProvider, ) -> int:
        ...

    def ToUInt16(self, provider: System.IFormatProvider, ) -> int:
        ...

    def ToInt32(self, provider: System.IFormatProvider, ) -> int:
        ...

    def ToUInt32(self, provider: System.IFormatProvider, ) -> int:
        ...

    def ToInt64(self, provider: System.IFormatProvider, ) -> int:
        ...

    def ToUInt64(self, provider: System.IFormatProvider, ) -> int:
        ...

    def ToSingle(self, provider: System.IFormatProvider, ) -> float:
        ...

    def ToDouble(self, provider: System.IFormatProvider, ) -> float:
        ...

    @staticmethod
    def UnsafeCreate(ticks: int, ) -> System.DateTime:
        ...

    @staticmethod
    def ThrowTicksOutOfRange() -> None:
        ...

    @staticmethod
    def ThrowInvalidKind() -> None:
        ...

    @staticmethod
    def ThrowMillisecondOutOfRange() -> None:
        ...

    @staticmethod
    def ThrowDateArithmetic(param: int, ) -> None:
        ...

    @typing.overload
    def Add(self, value: System.TimeSpan, ) -> System.DateTime:
        ...

    @typing.overload
    def Add(self, value: float, scale: int, ) -> System.DateTime:
        ...

    def AddDays(self, value: float, ) -> System.DateTime:
        ...

    def AddHours(self, value: float, ) -> System.DateTime:
        ...

    def AddMilliseconds(self, value: float, ) -> System.DateTime:
        ...

    def AddMinutes(self, value: float, ) -> System.DateTime:
        ...

    def AddMonths(self, months: int, ) -> System.DateTime:
        ...

    def AddSeconds(self, value: float, ) -> System.DateTime:
        ...

    def AddTicks(self, value: int, ) -> System.DateTime:
        ...

    def TryAddTicks(self, value: int, result: ref[System.DateTime], ) -> bool:
        ...

    def AddYears(self, value: int, ) -> System.DateTime:
        ...

    @staticmethod
    def Compare(t1: System.DateTime, t2: System.DateTime, ) -> int:
        ...

    @typing.overload
    def CompareTo(self, value: System.Object, ) -> int:
        ...

    @typing.overload
    def CompareTo(self, value: System.DateTime, ) -> int:
        ...

    @staticmethod
    def DateToTicks(year: int, month: int, day: int, ) -> int:
        ...

    @staticmethod
    def DaysToYear(year: int, ) -> int:
        ...

    @staticmethod
    @typing.overload
    def TimeToTicks(hour: int, minute: int, second: int, ) -> int:
        ...

    @staticmethod
    @typing.overload
    def TimeToTicks(hour: int, minute: int, second: int, millisecond: int, ) -> int:
        ...

    @staticmethod
    def DaysInMonth(year: int, month: int, ) -> int:
        ...

    @staticmethod
    def DoubleDateToTicks(value: float, ) -> int:
        ...

    @typing.overload
    def Equals(self, value: System.Object, ) -> bool:
        ...

    @typing.overload
    def Equals(self, value: System.DateTime, ) -> bool:
        ...

    @staticmethod
    @typing.overload
    def Equals(t1: System.DateTime, t2: System.DateTime, ) -> bool:
        ...

    @staticmethod
    def FromBinary(dateData: int, ) -> System.DateTime:
        ...

    @staticmethod
    def FromFileTime(fileTime: int, ) -> System.DateTime:
        ...

    @staticmethod
    def FromFileTimeUtc(fileTime: int, ) -> System.DateTime:
        ...

    @staticmethod
    def FromOADate(d: float, ) -> System.DateTime:
        ...

    def GetObjectData(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext, ) -> None:
        ...

    def IsDaylightSavingTime(self, ) -> bool:
        ...

    @staticmethod
    def SpecifyKind(value: System.DateTime, kind: int, ) -> System.DateTime:
        ...

    def ToBinary(self, ) -> int:
        ...

    def GetDatePart(self, part: int, ) -> int:
        ...

    def GetDate(self, year: ref[int], month: ref[int], day: ref[int], ) -> None:
        ...

    @typing.overload
    def GetTime(self, hour: ref[int], minute: ref[int], second: ref[int], ) -> None:
        ...

    @typing.overload
    def GetTime(self, hour: ref[int], minute: ref[int], second: ref[int], millisecond: ref[int], ) -> None:
        ...

    def GetTimePrecise(self, hour: ref[int], minute: ref[int], second: ref[int], tick: ref[int], ) -> None:
        ...

    def GetHashCode(self, ) -> int:
        ...

    def IsAmbiguousDaylightSavingTime(self, ) -> bool:
        ...

    @staticmethod
    def IsLeapYear(year: int, ) -> bool:
        ...

class TimeSpan(System.IComparable, System.IComparable[System.TimeSpan], System.IEquatable[System.TimeSpan], System.ISpanFormattable, System.IFormattable, System.IAdditionOperators[System.TimeSpan, System.TimeSpan, System.TimeSpan], System.IAdditiveIdentity[System.TimeSpan, System.TimeSpan], System.IComparisonOperators[System.TimeSpan, System.TimeSpan], System.IEqualityOperators[System.TimeSpan, System.TimeSpan], System.IDivisionOperators[System.TimeSpan, float, System.TimeSpan], System.IDivisionOperators[System.TimeSpan, System.TimeSpan, float], System.IMinMaxValue[System.TimeSpan], System.IMultiplyOperators[System.TimeSpan, float, System.TimeSpan], System.IMultiplicativeIdentity[System.TimeSpan, float], System.ISpanParseable[System.TimeSpan], System.IParseable[System.TimeSpan], System.ISubtractionOperators[System.TimeSpan, System.TimeSpan, System.TimeSpan], System.IUnaryNegationOperators[System.TimeSpan, System.TimeSpan], System.IUnaryPlusOperators[System.TimeSpan, System.TimeSpan], System.ValueType):
    @typing.overload
    def __init__(self, **kwargs):
        self._ticks: int
        ...

    # static fields
    Zero: System.TimeSpan = ...
    MaxValue: System.TimeSpan = ...
    MinValue: System.TimeSpan = ...
    TicksPerMillisecond: int = ...
    TicksPerSecond: int = ...
    TicksPerMinute: int = ...
    TicksPerHour: int = ...
    TicksPerDay: int = ...

    # properties
    @property
    def Ticks(self) -> int:
        ...

    @property
    def Days(self) -> int:
        ...

    @property
    def Hours(self) -> int:
        ...

    @property
    def Milliseconds(self) -> int:
        ...

    @property
    def Minutes(self) -> int:
        ...

    @property
    def Seconds(self) -> int:
        ...

    @property
    def TotalDays(self) -> float:
        ...

    @property
    def TotalHours(self) -> float:
        ...

    @property
    def TotalMilliseconds(self) -> float:
        ...

    @property
    def TotalMinutes(self) -> float:
        ...

    @property
    def TotalSeconds(self) -> float:
        ...

    @property
    def AdditiveIdentity(self) -> System.TimeSpan:
        ...

    @property
    def MinValue(self) -> System.TimeSpan:
        ...

    @property
    def MaxValue(self) -> System.TimeSpan:
        ...

    @property
    def MultiplicativeIdentity(self) -> float:
        ...

    # methods
    @typing.overload
    def __init__(self, ticks: int, ):
        ...

    @typing.overload
    def __init__(self, hours: int, minutes: int, seconds: int, ):
        ...

    @typing.overload
    def __init__(self, days: int, hours: int, minutes: int, seconds: int, ):
        ...

    @typing.overload
    def __init__(self, days: int, hours: int, minutes: int, seconds: int, milliseconds: int, ):
        ...

    @staticmethod
    def op_LessThan(left: System.TimeSpan, right: System.TimeSpan, ) -> bool:
        ...

    @staticmethod
    def op_LessThanOrEqual(left: System.TimeSpan, right: System.TimeSpan, ) -> bool:
        ...

    @staticmethod
    def op_GreaterThan(left: System.TimeSpan, right: System.TimeSpan, ) -> bool:
        ...

    @staticmethod
    def op_GreaterThanOrEqual(left: System.TimeSpan, right: System.TimeSpan, ) -> bool:
        ...

    @staticmethod
    def op_Division(left: System.TimeSpan, right: float, ) -> System.TimeSpan:
        ...

    @staticmethod
    def op_Division(left: System.TimeSpan, right: System.TimeSpan, ) -> float:
        ...

    @staticmethod
    def op_Equality(left: System.TimeSpan, right: System.TimeSpan, ) -> bool:
        ...

    @staticmethod
    def op_Inequality(left: System.TimeSpan, right: System.TimeSpan, ) -> bool:
        ...

    @staticmethod
    def op_Multiply(left: System.TimeSpan, right: float, ) -> System.TimeSpan:
        ...

    @staticmethod
    def Parse(s: str, provider: System.IFormatProvider, ) -> System.TimeSpan:
        ...

    @staticmethod
    def TryParse(s: str, provider: System.IFormatProvider, result: ref[System.TimeSpan], ) -> bool:
        ...

    @staticmethod
    def Parse(s: System.ReadOnlySpan[str], provider: System.IFormatProvider, ) -> System.TimeSpan:
        ...

    @staticmethod
    def TryParse(s: System.ReadOnlySpan[str], provider: System.IFormatProvider, result: ref[System.TimeSpan], ) -> bool:
        ...

    @staticmethod
    def op_Subtraction(left: System.TimeSpan, right: System.TimeSpan, ) -> System.TimeSpan:
        ...

    @staticmethod
    def op_UnaryNegation(value: System.TimeSpan, ) -> System.TimeSpan:
        ...

    @staticmethod
    def op_UnaryPlus(value: System.TimeSpan, ) -> System.TimeSpan:
        ...

    def Add(self, ts: System.TimeSpan, ) -> System.TimeSpan:
        ...

    @staticmethod
    def Compare(t1: System.TimeSpan, t2: System.TimeSpan, ) -> int:
        ...

    @typing.overload
    def CompareTo(self, value: System.Object, ) -> int:
        ...

    @typing.overload
    def CompareTo(self, value: System.TimeSpan, ) -> int:
        ...

    @staticmethod
    def FromDays(value: float, ) -> System.TimeSpan:
        ...

    def Duration(self, ) -> System.TimeSpan:
        ...

    @typing.overload
    def Equals(self, value: System.Object, ) -> bool:
        ...

    @typing.overload
    def Equals(self, obj: System.TimeSpan, ) -> bool:
        ...

    @staticmethod
    @typing.overload
    def Equals(t1: System.TimeSpan, t2: System.TimeSpan, ) -> bool:
        ...

    def GetHashCode(self, ) -> int:
        ...

    @staticmethod
    def FromHours(value: float, ) -> System.TimeSpan:
        ...

    @staticmethod
    def Interval(value: float, scale: float, ) -> System.TimeSpan:
        ...

    @staticmethod
    def IntervalFromDoubleTicks(ticks: float, ) -> System.TimeSpan:
        ...

    @staticmethod
    def FromMilliseconds(value: float, ) -> System.TimeSpan:
        ...

    @staticmethod
    def FromMinutes(value: float, ) -> System.TimeSpan:
        ...

    def Negate(self, ) -> System.TimeSpan:
        ...

    @staticmethod
    def FromSeconds(value: float, ) -> System.TimeSpan:
        ...

    def Subtract(self, ts: System.TimeSpan, ) -> System.TimeSpan:
        ...

    def Multiply(self, factor: float, ) -> System.TimeSpan:
        ...

    @typing.overload
    def Divide(self, divisor: float, ) -> System.TimeSpan:
        ...

    @typing.overload
    def Divide(self, ts: System.TimeSpan, ) -> float:
        ...

    @staticmethod
    def FromTicks(value: int, ) -> System.TimeSpan:
        ...

    @staticmethod
    def TimeToTicks(hour: int, minute: int, second: int, ) -> int:
        ...

    @staticmethod
    def ValidateStyles(style: int, parameterName: str, ) -> None:
        ...

    @staticmethod
    @typing.overload
    def Parse(s: str, ) -> System.TimeSpan:
        ...

    @staticmethod
    @typing.overload
    def Parse(input: str, formatProvider: System.IFormatProvider, ) -> System.TimeSpan:
        ...

    @staticmethod
    @typing.overload
    def Parse(input: System.ReadOnlySpan[str], formatProvider: System.IFormatProvider = ..., ) -> System.TimeSpan:
        ...

    @staticmethod
    @typing.overload
    def ParseExact(input: str, format: str, formatProvider: System.IFormatProvider, ) -> System.TimeSpan:
        ...

    @staticmethod
    @typing.overload
    def ParseExact(input: str, formats: System.Array[str], formatProvider: System.IFormatProvider, ) -> System.TimeSpan:
        ...

    @staticmethod
    @typing.overload
    def ParseExact(input: str, format: str, formatProvider: System.IFormatProvider, styles: int, ) -> System.TimeSpan:
        ...

    @staticmethod
    @typing.overload
    def ParseExact(input: System.ReadOnlySpan[str], format: System.ReadOnlySpan[str], formatProvider: System.IFormatProvider, styles: int = ..., ) -> System.TimeSpan:
        ...

    @staticmethod
    @typing.overload
    def ParseExact(input: str, formats: System.Array[str], formatProvider: System.IFormatProvider, styles: int, ) -> System.TimeSpan:
        ...

    @staticmethod
    @typing.overload
    def ParseExact(input: System.ReadOnlySpan[str], formats: System.Array[str], formatProvider: System.IFormatProvider, styles: int = ..., ) -> System.TimeSpan:
        ...

    @staticmethod
    @typing.overload
    def TryParse(s: str, result: ref[System.TimeSpan], ) -> bool:
        ...

    @staticmethod
    @typing.overload
    def TryParse(s: System.ReadOnlySpan[str], result: ref[System.TimeSpan], ) -> bool:
        ...

    @staticmethod
    @typing.overload
    def TryParse(input: str, formatProvider: System.IFormatProvider, result: ref[System.TimeSpan], ) -> bool:
        ...

    @staticmethod
    @typing.overload
    def TryParse(input: System.ReadOnlySpan[str], formatProvider: System.IFormatProvider, result: ref[System.TimeSpan], ) -> bool:
        ...

    @staticmethod
    @typing.overload
    def TryParseExact(input: str, format: str, formatProvider: System.IFormatProvider, result: ref[System.TimeSpan], ) -> bool:
        ...

    @staticmethod
    @typing.overload
    def TryParseExact(input: System.ReadOnlySpan[str], format: System.ReadOnlySpan[str], formatProvider: System.IFormatProvider, result: ref[System.TimeSpan], ) -> bool:
        ...

    @staticmethod
    @typing.overload
    def TryParseExact(input: str, formats: System.Array[str], formatProvider: System.IFormatProvider, result: ref[System.TimeSpan], ) -> bool:
        ...

    @staticmethod
    @typing.overload
    def TryParseExact(input: System.ReadOnlySpan[str], formats: System.Array[str], formatProvider: System.IFormatProvider, result: ref[System.TimeSpan], ) -> bool:
        ...

    @staticmethod
    @typing.overload
    def TryParseExact(input: str, format: str, formatProvider: System.IFormatProvider, styles: int, result: ref[System.TimeSpan], ) -> bool:
        ...

    @staticmethod
    @typing.overload
    def TryParseExact(input: System.ReadOnlySpan[str], format: System.ReadOnlySpan[str], formatProvider: System.IFormatProvider, styles: int, result: ref[System.TimeSpan], ) -> bool:
        ...

    @staticmethod
    @typing.overload
    def TryParseExact(input: str, formats: System.Array[str], formatProvider: System.IFormatProvider, styles: int, result: ref[System.TimeSpan], ) -> bool:
        ...

    @staticmethod
    @typing.overload
    def TryParseExact(input: System.ReadOnlySpan[str], formats: System.Array[str], formatProvider: System.IFormatProvider, styles: int, result: ref[System.TimeSpan], ) -> bool:
        ...

    @typing.overload
    def ToString(self, ) -> str:
        ...

    @typing.overload
    def ToString(self, format: str, ) -> str:
        ...

    @typing.overload
    def ToString(self, format: str, formatProvider: System.IFormatProvider, ) -> str:
        ...

    def TryFormat(self, destination: System.Span[str], charsWritten: ref[int], format: System.ReadOnlySpan[str] = ..., formatProvider: System.IFormatProvider = ..., ) -> bool:
        ...

    @staticmethod
    def op_Addition(left: System.TimeSpan, right: System.TimeSpan, ) -> System.TimeSpan:
        ...

class MulticastDelegate(System.ICloneable, System.Runtime.Serialization.ISerializable, System.Delegate, abc.ABC):
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
    @typing.overload
    def __init__(self, target: System.Object, method: str, ):
        ...

    @typing.overload
    def __init__(self, target: System.Type, method: str, ):
        ...

    def IsUnmanagedFunctionPtr(self, ) -> bool:
        ...

    def InvocationListLogicallyNull(self, ) -> bool:
        ...

    def GetObjectData(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext, ) -> None:
        ...

    def Equals(self, obj: System.Object, ) -> bool:
        ...

    def InvocationListEquals(self, d: System.MulticastDelegate, ) -> bool:
        ...

    @staticmethod
    def TrySetSlot(a: System.Array[System.Object], index: int, o: System.Object, ) -> bool:
        ...

    @typing.overload
    def NewMulticastDelegate(self, invocationList: System.Array[System.Object], invocationCount: int, thisIsMultiCastAlready: bool, ) -> System.MulticastDelegate:
        ...

    @typing.overload
    def NewMulticastDelegate(self, invocationList: System.Array[System.Object], invocationCount: int, ) -> System.MulticastDelegate:
        ...

    def StoreDynamicMethod(self, dynamicMethod: System.Reflection.MethodInfo, ) -> None:
        ...

    def CombineImpl(self, follow: System.Delegate, ) -> System.Delegate:
        ...

    def DeleteFromInvocationList(self, invocationList: System.Array[System.Object], invocationCount: int, deleteIndex: int, deleteCount: int, ) -> System.Array[System.Object]:
        ...

    @staticmethod
    def EqualInvocationLists(a: System.Array[System.Object], b: System.Array[System.Object], start: int, count: int, ) -> bool:
        ...

    def RemoveImpl(self, value: System.Delegate, ) -> System.Delegate:
        ...

    def GetInvocationList(self, ) -> System.Array[System.Delegate]:
        ...

    def GetHashCode(self, ) -> int:
        ...

    def GetTarget(self, ) -> System.Object:
        ...

    def GetMethodImpl(self, ) -> System.Reflection.MethodInfo:
        ...

    @staticmethod
    def ThrowNullThisInDelegateToInstance() -> None:
        ...

    def CtorClosed(self, target: System.Object, methodPtr: System.IntPtr, ) -> None:
        ...

    def CtorClosedStatic(self, target: System.Object, methodPtr: System.IntPtr, ) -> None:
        ...

    def CtorRTClosed(self, target: System.Object, methodPtr: System.IntPtr, ) -> None:
        ...

    def CtorOpened(self, target: System.Object, methodPtr: System.IntPtr, shuffleThunk: System.IntPtr, ) -> None:
        ...

    def CtorVirtualDispatch(self, target: System.Object, methodPtr: System.IntPtr, shuffleThunk: System.IntPtr, ) -> None:
        ...

    def CtorCollectibleClosedStatic(self, target: System.Object, methodPtr: System.IntPtr, gchandle: System.IntPtr, ) -> None:
        ...

    def CtorCollectibleOpened(self, target: System.Object, methodPtr: System.IntPtr, shuffleThunk: System.IntPtr, gchandle: System.IntPtr, ) -> None:
        ...

    def CtorCollectibleVirtualDispatch(self, target: System.Object, methodPtr: System.IntPtr, shuffleThunk: System.IntPtr, gchandle: System.IntPtr, ) -> None:
        ...

class IComparable(abc.ABC, typing.Generic[T]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    @abc.abstractmethod
    def CompareTo(self, other: T, ) -> int:
        ...

class Attribute(System.Object, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def TypeId(self) -> System.Object:
        ...

    # methods
    def __init__(self, ):
        ...

    @staticmethod
    @typing.overload
    def InternalGetCustomAttributes(element: System.Reflection.PropertyInfo, type: System.Type, inherit: bool, ) -> System.Array[System.Attribute]:
        ...

    @staticmethod
    @typing.overload
    def InternalGetCustomAttributes(element: System.Reflection.EventInfo, type: System.Type, inherit: bool, ) -> System.Array[System.Attribute]:
        ...

    @staticmethod
    @typing.overload
    def InternalIsDefined(element: System.Reflection.PropertyInfo, attributeType: System.Type, inherit: bool, ) -> bool:
        ...

    @staticmethod
    @typing.overload
    def InternalIsDefined(element: System.Reflection.EventInfo, attributeType: System.Type, inherit: bool, ) -> bool:
        ...

    @staticmethod
    @typing.overload
    def GetParentDefinition(property: System.Reflection.PropertyInfo, propertyParameters: System.Array[System.Type], ) -> System.Reflection.PropertyInfo:
        ...

    @staticmethod
    @typing.overload
    def GetParentDefinition(ev: System.Reflection.EventInfo, ) -> System.Reflection.EventInfo:
        ...

    @staticmethod
    @typing.overload
    def GetParentDefinition(param: System.Reflection.ParameterInfo, ) -> System.Reflection.ParameterInfo:
        ...

    @staticmethod
    def InternalParamGetCustomAttributes(param: System.Reflection.ParameterInfo, type: System.Type, inherit: bool, ) -> System.Array[System.Attribute]:
        ...

    @staticmethod
    def InternalParamIsDefined(param: System.Reflection.ParameterInfo, type: System.Type, inherit: bool, ) -> bool:
        ...

    @staticmethod
    def CopyToAttributeList(attributeList: System.Collections.Generic.List[System.Attribute], attributes: System.Array[System.Attribute], types: System.Collections.Generic.Dictionary[System.Type, System.AttributeUsageAttribute], ) -> None:
        ...

    @staticmethod
    def GetIndexParameterTypes(element: System.Reflection.PropertyInfo, ) -> System.Array[System.Type]:
        ...

    @staticmethod
    def AddAttributesToList(attributeList: System.Collections.Generic.List[System.Attribute], attributes: System.Array[System.Attribute], types: System.Collections.Generic.Dictionary[System.Type, System.AttributeUsageAttribute], ) -> None:
        ...

    @staticmethod
    def InternalGetAttributeUsage(type: System.Type, ) -> System.AttributeUsageAttribute:
        ...

    @staticmethod
    def CreateAttributeArrayHelper(elementType: System.Type, elementCount: int, ) -> System.Array[System.Attribute]:
        ...

    @staticmethod
    @typing.overload
    def GetCustomAttributes(element: System.Reflection.MemberInfo, attributeType: System.Type, ) -> System.Array[System.Attribute]:
        ...

    @staticmethod
    @typing.overload
    def GetCustomAttributes(element: System.Reflection.MemberInfo, attributeType: System.Type, inherit: bool, ) -> System.Array[System.Attribute]:
        ...

    @staticmethod
    @typing.overload
    def GetCustomAttributes(element: System.Reflection.MemberInfo, ) -> System.Array[System.Attribute]:
        ...

    @staticmethod
    @typing.overload
    def GetCustomAttributes(element: System.Reflection.MemberInfo, inherit: bool, ) -> System.Array[System.Attribute]:
        ...

    @staticmethod
    @typing.overload
    def GetCustomAttributes(element: System.Reflection.ParameterInfo, ) -> System.Array[System.Attribute]:
        ...

    @staticmethod
    @typing.overload
    def GetCustomAttributes(element: System.Reflection.ParameterInfo, attributeType: System.Type, ) -> System.Array[System.Attribute]:
        ...

    @staticmethod
    @typing.overload
    def GetCustomAttributes(element: System.Reflection.ParameterInfo, attributeType: System.Type, inherit: bool, ) -> System.Array[System.Attribute]:
        ...

    @staticmethod
    @typing.overload
    def GetCustomAttributes(element: System.Reflection.ParameterInfo, inherit: bool, ) -> System.Array[System.Attribute]:
        ...

    @staticmethod
    @typing.overload
    def GetCustomAttributes(element: System.Reflection.Module, attributeType: System.Type, ) -> System.Array[System.Attribute]:
        ...

    @staticmethod
    @typing.overload
    def GetCustomAttributes(element: System.Reflection.Module, ) -> System.Array[System.Attribute]:
        ...

    @staticmethod
    @typing.overload
    def GetCustomAttributes(element: System.Reflection.Module, inherit: bool, ) -> System.Array[System.Attribute]:
        ...

    @staticmethod
    @typing.overload
    def GetCustomAttributes(element: System.Reflection.Module, attributeType: System.Type, inherit: bool, ) -> System.Array[System.Attribute]:
        ...

    @staticmethod
    @typing.overload
    def GetCustomAttributes(element: System.Reflection.Assembly, attributeType: System.Type, ) -> System.Array[System.Attribute]:
        ...

    @staticmethod
    @typing.overload
    def GetCustomAttributes(element: System.Reflection.Assembly, attributeType: System.Type, inherit: bool, ) -> System.Array[System.Attribute]:
        ...

    @staticmethod
    @typing.overload
    def GetCustomAttributes(element: System.Reflection.Assembly, ) -> System.Array[System.Attribute]:
        ...

    @staticmethod
    @typing.overload
    def GetCustomAttributes(element: System.Reflection.Assembly, inherit: bool, ) -> System.Array[System.Attribute]:
        ...

    @staticmethod
    @typing.overload
    def IsDefined(element: System.Reflection.MemberInfo, attributeType: System.Type, ) -> bool:
        ...

    @staticmethod
    @typing.overload
    def IsDefined(element: System.Reflection.MemberInfo, attributeType: System.Type, inherit: bool, ) -> bool:
        ...

    @staticmethod
    @typing.overload
    def IsDefined(element: System.Reflection.ParameterInfo, attributeType: System.Type, ) -> bool:
        ...

    @staticmethod
    @typing.overload
    def IsDefined(element: System.Reflection.ParameterInfo, attributeType: System.Type, inherit: bool, ) -> bool:
        ...

    @staticmethod
    @typing.overload
    def IsDefined(element: System.Reflection.Module, attributeType: System.Type, ) -> bool:
        ...

    @staticmethod
    @typing.overload
    def IsDefined(element: System.Reflection.Module, attributeType: System.Type, inherit: bool, ) -> bool:
        ...

    @staticmethod
    @typing.overload
    def IsDefined(element: System.Reflection.Assembly, attributeType: System.Type, ) -> bool:
        ...

    @staticmethod
    @typing.overload
    def IsDefined(element: System.Reflection.Assembly, attributeType: System.Type, inherit: bool, ) -> bool:
        ...

    @staticmethod
    @typing.overload
    def GetCustomAttribute(element: System.Reflection.MemberInfo, attributeType: System.Type, ) -> System.Attribute:
        ...

    @staticmethod
    @typing.overload
    def GetCustomAttribute(element: System.Reflection.MemberInfo, attributeType: System.Type, inherit: bool, ) -> System.Attribute:
        ...

    @staticmethod
    @typing.overload
    def GetCustomAttribute(element: System.Reflection.ParameterInfo, attributeType: System.Type, ) -> System.Attribute:
        ...

    @staticmethod
    @typing.overload
    def GetCustomAttribute(element: System.Reflection.ParameterInfo, attributeType: System.Type, inherit: bool, ) -> System.Attribute:
        ...

    @staticmethod
    @typing.overload
    def GetCustomAttribute(element: System.Reflection.Module, attributeType: System.Type, ) -> System.Attribute:
        ...

    @staticmethod
    @typing.overload
    def GetCustomAttribute(element: System.Reflection.Module, attributeType: System.Type, inherit: bool, ) -> System.Attribute:
        ...

    @staticmethod
    @typing.overload
    def GetCustomAttribute(element: System.Reflection.Assembly, attributeType: System.Type, ) -> System.Attribute:
        ...

    @staticmethod
    @typing.overload
    def GetCustomAttribute(element: System.Reflection.Assembly, attributeType: System.Type, inherit: bool, ) -> System.Attribute:
        ...

    def Equals(self, obj: System.Object, ) -> bool:
        ...

    def GetHashCode(self, ) -> int:
        ...

    @staticmethod
    def AreFieldValuesEqual(thisValue: System.Object, thatValue: System.Object, ) -> bool:
        ...

    def Match(self, obj: System.Object, ) -> bool:
        ...

    def IsDefaultAttribute(self, ) -> bool:
        ...

class AttributeUsageAttribute(System.Attribute):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields
    Default: System.AttributeUsageAttribute = ...

    # properties
    @property
    def ValidOn(self) -> int:
        ...

    @property
    def AllowMultiple(self) -> bool:
        ...
    @AllowMultiple.setter
    def AllowMultiple(self, val: bool):
        ...

    @property
    def Inherited(self) -> bool:
        ...
    @Inherited.setter
    def Inherited(self, val: bool):
        ...

    @property
    def TypeId(self) -> System.Object:
        ...

    # methods
    @typing.overload
    def __init__(self, validOn: int, ):
        ...

    @typing.overload
    def __init__(self, validOn: int, allowMultiple: bool, inherited: bool, ):
        ...

class Func(System.ICloneable, System.Runtime.Serialization.ISerializable, System.MulticastDelegate, typing.Generic[T1, T2, T3, T4, TResult]):
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

    def Invoke(self, arg1: T1, arg2: T2, arg3: T3, arg4: T4, ) -> TResult:
        ...

    def BeginInvoke(self, arg1: T1, arg2: T2, arg3: T3, arg4: T4, callback: System.AsyncCallback, object: System.Object, ) -> System.IAsyncResult:
        ...

    def EndInvoke(self, result: System.IAsyncResult, ) -> TResult:
        ...

class AttributeTargets(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    Assembly: int = ...
    Module: int = ...
    Class: int = ...
    Struct: int = ...
    Enum: int = ...
    Constructor: int = ...
    Method: int = ...
    Property: int = ...
    Field: int = ...
    Event: int = ...
    Interface: int = ...
    Parameter: int = ...
    Delegate: int = ...
    ReturnValue: int = ...
    GenericParameter: int = ...
    All: int = ...

class IParseable(abc.ABC, typing.Generic[TSelf]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    @staticmethod
    @abc.abstractmethod
    def Parse(s: str, provider: System.IFormatProvider, ) -> TSelf:
        ...

    @staticmethod
    @abc.abstractmethod
    def TryParse(s: str, provider: System.IFormatProvider, result: ref[TSelf], ) -> bool:
        ...

class Random(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def Shared(self) -> System.Random:
        ...

    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def __init__(self, Seed: int, ):
        ...

    @typing.overload
    def __init__(self, isThreadSafeRandom: bool, ):
        ...

    @typing.overload
    def Next(self, ) -> int:
        ...

    @typing.overload
    def Next(self, maxValue: int, ) -> int:
        ...

    @typing.overload
    def Next(self, minValue: int, maxValue: int, ) -> int:
        ...

    @typing.overload
    def NextInt64(self, ) -> int:
        ...

    @typing.overload
    def NextInt64(self, maxValue: int, ) -> int:
        ...

    @typing.overload
    def NextInt64(self, minValue: int, maxValue: int, ) -> int:
        ...

    def NextSingle(self, ) -> float:
        ...

    def NextDouble(self, ) -> float:
        ...

    @typing.overload
    def NextBytes(self, buffer: System.Array[int], ) -> None:
        ...

    @typing.overload
    def NextBytes(self, buffer: System.Span[int], ) -> None:
        ...

    def Sample(self, ) -> float:
        ...

    @staticmethod
    def ThrowMaxValueMustBeNonNegative() -> None:
        ...

    @staticmethod
    def ThrowMinMaxValueSwapped() -> None:
        ...

class RuntimeFieldHandle(System.Runtime.Serialization.ISerializable, System.ValueType):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def Value(self) -> System.IntPtr:
        ...

    # methods
    def __init__(self, fieldInfo: System.IRuntimeFieldInfo, ):
        ...

    def GetRuntimeFieldInfo(self, ) -> System.IRuntimeFieldInfo:
        ...

    def IsNullHandle(self, ) -> bool:
        ...

    def GetHashCode(self, ) -> int:
        ...

    @typing.overload
    def Equals(self, obj: System.Object, ) -> bool:
        ...

    @typing.overload
    def Equals(self, handle: System.RuntimeFieldHandle, ) -> bool:
        ...

    @staticmethod
    def GetName(field: System.Reflection.RtFieldInfo, ) -> str:
        ...

    @staticmethod
    def _GetUtf8Name(field: System.RuntimeFieldHandleInternal, ) -> ptr[None]:
        ...

    @staticmethod
    def GetUtf8Name(field: System.RuntimeFieldHandleInternal, ) -> System.MdUtf8String:
        ...

    @staticmethod
    def MatchesNameHash(handle: System.RuntimeFieldHandleInternal, hash: int, ) -> bool:
        ...

    @staticmethod
    def GetAttributes(field: System.RuntimeFieldHandleInternal, ) -> int:
        ...

    @staticmethod
    @typing.overload
    def GetApproxDeclaringType(field: System.RuntimeFieldHandleInternal, ) -> System.RuntimeType:
        ...

    @staticmethod
    @typing.overload
    def GetApproxDeclaringType(field: System.IRuntimeFieldInfo, ) -> System.RuntimeType:
        ...

    @staticmethod
    def GetToken(field: System.Reflection.RtFieldInfo, ) -> int:
        ...

    @staticmethod
    def GetValue(field: System.Reflection.RtFieldInfo, instance: System.Object, fieldType: System.RuntimeType, declaringType: System.RuntimeType, domainInitialized: ref[bool], ) -> System.Object:
        ...

    @staticmethod
    def GetValueDirect(field: System.Reflection.RtFieldInfo, fieldType: System.RuntimeType, pTypedRef: ptr[None], contextType: System.RuntimeType, ) -> System.Object:
        ...

    @staticmethod
    def SetValue(field: System.Reflection.RtFieldInfo, obj: System.Object, value: System.Object, fieldType: System.RuntimeType, fieldAttr: int, declaringType: System.RuntimeType, domainInitialized: ref[bool], ) -> None:
        ...

    @staticmethod
    def SetValueDirect(field: System.Reflection.RtFieldInfo, fieldType: System.RuntimeType, pTypedRef: ptr[None], value: System.Object, contextType: System.RuntimeType, ) -> None:
        ...

    @staticmethod
    def GetStaticFieldForGenericType(field: System.RuntimeFieldHandleInternal, declaringType: System.RuntimeType, ) -> System.RuntimeFieldHandleInternal:
        ...

    @staticmethod
    def AcquiresContextFromThis(field: System.RuntimeFieldHandleInternal, ) -> bool:
        ...

    def GetObjectData(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext, ) -> None:
        ...

class ISubtractionOperators(abc.ABC, typing.Generic[TSelf, TOther, TResult]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
class Action(System.ICloneable, System.Runtime.Serialization.ISerializable, System.MulticastDelegate):
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

    def Invoke(self, ) -> None:
        ...

    def BeginInvoke(self, callback: System.AsyncCallback, object: System.Object, ) -> System.IAsyncResult:
        ...

    def EndInvoke(self, result: System.IAsyncResult, ) -> None:
        ...

class IAdditiveIdentity(abc.ABC, typing.Generic[TSelf, TResult]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    @abc.abstractmethod
    def AdditiveIdentity(self) -> TResult:
        ...

    # methods
class TypedReference(System.ValueType):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def IsNull(self) -> bool:
        ...

    # methods
    @staticmethod
    def MakeTypedReference(target: System.Object, flds: System.Array[System.Reflection.FieldInfo], ) -> System.TypedReference:
        ...

    @staticmethod
    def InternalMakeTypedReference(result: ptr[None], target: System.Object, flds: System.Array[System.IntPtr], lastFieldType: System.RuntimeType, ) -> None:
        ...

    def GetHashCode(self, ) -> int:
        ...

    def Equals(self, o: System.Object, ) -> bool:
        ...

    @staticmethod
    def ToObject(value: System.TypedReference, ) -> System.Object:
        ...

    @staticmethod
    def InternalToObject(value: ptr[None], ) -> System.Object:
        ...

    @staticmethod
    def GetTargetType(value: System.TypedReference, ) -> System.Type:
        ...

    @staticmethod
    def TargetTypeToken(value: System.TypedReference, ) -> System.RuntimeTypeHandle:
        ...

    @staticmethod
    def SetTypedReference(target: System.TypedReference, value: System.Object, ) -> None:
        ...

Int16 = int

class IEqualityOperators(System.IEquatable[TOther], abc.ABC, typing.Generic[TSelf, TOther]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
class Action(System.ICloneable, System.Runtime.Serialization.ISerializable, System.MulticastDelegate, typing.Generic[T1, T2]):
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

    def Invoke(self, arg1: T1, arg2: T2, ) -> None:
        ...

    def BeginInvoke(self, arg1: T1, arg2: T2, callback: System.AsyncCallback, object: System.Object, ) -> System.IAsyncResult:
        ...

    def EndInvoke(self, result: System.IAsyncResult, ) -> None:
        ...

class INumber(System.IAdditionOperators[TSelf, TSelf, TSelf], System.IAdditiveIdentity[TSelf, TSelf], System.IComparisonOperators[TSelf, TSelf], System.IComparable, System.IComparable[TSelf], System.IEqualityOperators[TSelf, TSelf], System.IEquatable[TSelf], System.IDecrementOperators[TSelf], System.IDivisionOperators[TSelf, TSelf, TSelf], System.IIncrementOperators[TSelf], System.IModulusOperators[TSelf, TSelf, TSelf], System.IMultiplicativeIdentity[TSelf, TSelf], System.IMultiplyOperators[TSelf, TSelf, TSelf], System.ISpanFormattable, System.IFormattable, System.ISpanParseable[TSelf], System.IParseable[TSelf], System.ISubtractionOperators[TSelf, TSelf, TSelf], System.IUnaryNegationOperators[TSelf, TSelf], System.IUnaryPlusOperators[TSelf, TSelf], abc.ABC, typing.Generic[TSelf]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    @abc.abstractmethod
    def One(self) -> TSelf:
        ...

    @property
    @abc.abstractmethod
    def Zero(self) -> TSelf:
        ...

    # methods
    @staticmethod
    @abc.abstractmethod
    def Abs(value: TSelf, ) -> TSelf:
        ...

    @staticmethod
    @abc.abstractmethod
    def Clamp(value: TSelf, min: TSelf, max: TSelf, ) -> TSelf:
        ...

    @staticmethod
    @abc.abstractmethod
    def Create(value: TOther, ) -> TSelf:
        ...

    @staticmethod
    @abc.abstractmethod
    def CreateSaturating(value: TOther, ) -> TSelf:
        ...

    @staticmethod
    @abc.abstractmethod
    def CreateTruncating(value: TOther, ) -> TSelf:
        ...

    @staticmethod
    @abc.abstractmethod
    def DivRem(left: TSelf, right: TSelf, ) -> System.ValueTuple[TSelf, TSelf]:
        ...

    @staticmethod
    @abc.abstractmethod
    def Max(x: TSelf, y: TSelf, ) -> TSelf:
        ...

    @staticmethod
    @abc.abstractmethod
    def Min(x: TSelf, y: TSelf, ) -> TSelf:
        ...

    @staticmethod
    @abc.abstractmethod
    @typing.overload
    def Parse(s: str, style: int, provider: System.IFormatProvider, ) -> TSelf:
        ...

    @staticmethod
    @abc.abstractmethod
    @typing.overload
    def Parse(s: System.ReadOnlySpan[str], style: int, provider: System.IFormatProvider, ) -> TSelf:
        ...

    @staticmethod
    @abc.abstractmethod
    def Sign(value: TSelf, ) -> TSelf:
        ...

    @staticmethod
    @abc.abstractmethod
    def TryCreate(value: TOther, result: ref[TSelf], ) -> bool:
        ...

    @staticmethod
    @abc.abstractmethod
    @typing.overload
    def TryParse(s: str, style: int, provider: System.IFormatProvider, result: ref[TSelf], ) -> bool:
        ...

    @staticmethod
    @abc.abstractmethod
    @typing.overload
    def TryParse(s: System.ReadOnlySpan[str], style: int, provider: System.IFormatProvider, result: ref[TSelf], ) -> bool:
        ...

Int32 = int

class ReadOnlySpan(System.ValueType, typing.Generic[T]):
    @typing.overload
    def __init__(self, **kwargs):
        self._pointer: System.ByReference[T]
        ...

    # static fields

    # properties
    @property
    def Item(self) -> ref[T]:
        ...

    @property
    def Length(self) -> int:
        ...

    @property
    def IsEmpty(self) -> bool:
        ...

    @property
    def Empty(self) -> System.ReadOnlySpan:
        ...

    # methods
    @typing.overload
    def __init__(self, array: System.Array[T], ):
        ...

    @typing.overload
    def __init__(self, array: System.Array[T], start: int, length: int, ):
        ...

    @typing.overload
    def __init__(self, pointer: ptr[None], length: int, ):
        ...

    @typing.overload
    def __init__(self, ptr: ref[T], length: int, ):
        ...

    def Equals(self, obj: System.Object, ) -> bool:
        ...

    def GetHashCode(self, ) -> int:
        ...

    def GetEnumerator(self, ) -> System.ReadOnlySpan.Enumerator[T]:
        ...

    def GetPinnableReference(self, ) -> ref[T]:
        ...

    def CopyTo(self, destination: System.Span[T], ) -> None:
        ...

    def TryCopyTo(self, destination: System.Span[T], ) -> bool:
        ...

    def ToString(self, ) -> str:
        ...

    @typing.overload
    def Slice(self, start: int, ) -> System.ReadOnlySpan:
        ...

    @typing.overload
    def Slice(self, start: int, length: int, ) -> System.ReadOnlySpan:
        ...

    def ToArray(self, ) -> System.Array[T]:
        ...

Int64 = int

class AsyncCallback(System.ICloneable, System.Runtime.Serialization.ISerializable, System.MulticastDelegate):
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

    def Invoke(self, ar: System.IAsyncResult, ) -> None:
        ...

    def BeginInvoke(self, ar: System.IAsyncResult, callback: System.AsyncCallback, object: System.Object, ) -> System.IAsyncResult:
        ...

    def EndInvoke(self, result: System.IAsyncResult, ) -> None:
        ...

class Converter(System.ICloneable, System.Runtime.Serialization.ISerializable, System.MulticastDelegate, typing.Generic[TInput, TOutput]):
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

    def Invoke(self, input: TInput, ) -> TOutput:
        ...

    def BeginInvoke(self, input: TInput, callback: System.AsyncCallback, object: System.Object, ) -> System.IAsyncResult:
        ...

    def EndInvoke(self, result: System.IAsyncResult, ) -> TOutput:
        ...

class DayOfWeek(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    Sunday: int = ...
    Monday: int = ...
    Tuesday: int = ...
    Wednesday: int = ...
    Thursday: int = ...
    Friday: int = ...
    Saturday: int = ...

class Action(System.ICloneable, System.Runtime.Serialization.ISerializable, System.MulticastDelegate, typing.Generic[T]):
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

    def Invoke(self, obj: T, ) -> None:
        ...

    def BeginInvoke(self, obj: T, callback: System.AsyncCallback, object: System.Object, ) -> System.IAsyncResult:
        ...

    def EndInvoke(self, result: System.IAsyncResult, ) -> None:
        ...

class IShiftOperators(abc.ABC, typing.Generic[TSelf, TResult]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
class Nullable(System.ValueType, typing.Generic[T]):
    @typing.overload
    def __init__(self, **kwargs):
        self.value: T
        ...

    # static fields

    # properties
    @property
    def HasValue(self) -> bool:
        ...

    @property
    def Value(self) -> T:
        ...

    # methods
    def __init__(self, value: T, ):
        ...

    @typing.overload
    def GetValueOrDefault(self, ) -> T:
        ...

    @typing.overload
    def GetValueOrDefault(self, defaultValue: T, ) -> T:
        ...

    def Equals(self, other: System.Object, ) -> bool:
        ...

    def GetHashCode(self, ) -> int:
        ...

    def ToString(self, ) -> str:
        ...

class OperationCanceledException(System.Runtime.Serialization.ISerializable, System.SystemException):
    @typing.overload
    def __init__(self, **kwargs):
        self._message: str
        ...

    # static fields

    # properties
    @property
    def CancellationToken(self) -> System.Threading.CancellationToken:
        ...
    @CancellationToken.setter
    def CancellationToken(self, val: System.Threading.CancellationToken):
        ...

    @property
    def TargetSite(self) -> System.Reflection.MethodBase:
        ...

    @property
    def Message(self) -> str:
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
    def __init__(self, token: System.Threading.CancellationToken, ):
        ...

    @typing.overload
    def __init__(self, message: str, token: System.Threading.CancellationToken, ):
        ...

    @typing.overload
    def __init__(self, message: str, innerException: System.Exception, token: System.Threading.CancellationToken, ):
        ...

    @typing.overload
    def __init__(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext, ):
        ...

class SystemException(System.Runtime.Serialization.ISerializable, System.Exception):
    @typing.overload
    def __init__(self, **kwargs):
        self._message: str
        ...

    # static fields

    # properties
    @property
    def TargetSite(self) -> System.Reflection.MethodBase:
        ...

    @property
    def Message(self) -> str:
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
    def __init__(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext, ):
        ...

class IDivisionOperators(abc.ABC, typing.Generic[TSelf, TOther, TResult]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
class ValueType(System.Object, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    def __init__(self, ):
        ...

    def GetHashCode(self, ) -> int:
        ...

    def Equals(self, obj: System.Object, ) -> bool:
        ...

    def ToString(self, ) -> str:
        ...

    @staticmethod
    def CanCompareBits(obj: System.Object, ) -> bool:
        ...

    @staticmethod
    def FastEqualsCheck(a: System.Object, b: System.Object, ) -> bool:
        ...

    @staticmethod
    def GetHashCodeOfPtr(ptr: System.IntPtr, ) -> int:
        ...

class Comparison(System.ICloneable, System.Runtime.Serialization.ISerializable, System.MulticastDelegate, typing.Generic[T]):
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

    def Invoke(self, x: T, y: T, ) -> int:
        ...

    def BeginInvoke(self, x: T, y: T, callback: System.AsyncCallback, object: System.Object, ) -> System.IAsyncResult:
        ...

    def EndInvoke(self, result: System.IAsyncResult, ) -> int:
        ...

class Guid(System.ISpanFormattable, System.IFormattable, System.IComparable, System.IComparable[System.Guid], System.IEquatable[System.Guid], System.IComparisonOperators[System.Guid, System.Guid], System.IEqualityOperators[System.Guid, System.Guid], System.ISpanParseable[System.Guid], System.IParseable[System.Guid], System.ValueType):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields
    Empty: System.Guid = ...

    # properties
    # methods
    @typing.overload
    def __init__(self, b: System.Array[int], ):
        ...

    @typing.overload
    def __init__(self, b: System.ReadOnlySpan[int], ):
        ...

    @typing.overload
    def __init__(self, a: int, b: int, c: int, d: int, e: int, f: int, g: int, h: int, i: int, j: int, k: int, ):
        ...

    @typing.overload
    def __init__(self, a: int, b: int, c: int, d: System.Array[int], ):
        ...

    @typing.overload
    def __init__(self, a: int, b: int, c: int, d: int, e: int, f: int, g: int, h: int, i: int, j: int, k: int, ):
        ...

    @typing.overload
    def __init__(self, g: str, ):
        ...

    @staticmethod
    @typing.overload
    def Parse(input: str, ) -> System.Guid:
        ...

    @staticmethod
    @typing.overload
    def Parse(input: System.ReadOnlySpan[str], ) -> System.Guid:
        ...

    @staticmethod
    @typing.overload
    def TryParse(input: str, result: ref[System.Guid], ) -> bool:
        ...

    @staticmethod
    @typing.overload
    def TryParse(input: System.ReadOnlySpan[str], result: ref[System.Guid], ) -> bool:
        ...

    @staticmethod
    @typing.overload
    def ParseExact(input: str, format: str, ) -> System.Guid:
        ...

    @staticmethod
    @typing.overload
    def ParseExact(input: System.ReadOnlySpan[str], format: System.ReadOnlySpan[str], ) -> System.Guid:
        ...

    @staticmethod
    @typing.overload
    def TryParseExact(input: str, format: str, result: ref[System.Guid], ) -> bool:
        ...

    @staticmethod
    @typing.overload
    def TryParseExact(input: System.ReadOnlySpan[str], format: System.ReadOnlySpan[str], result: ref[System.Guid], ) -> bool:
        ...

    @staticmethod
    def TryParseGuid(guidString: System.ReadOnlySpan[str], result: ref[System.Guid.GuidResult], ) -> bool:
        ...

    @staticmethod
    def TryParseExactB(guidString: System.ReadOnlySpan[str], result: ref[System.Guid.GuidResult], ) -> bool:
        ...

    @staticmethod
    def TryParseExactD(guidString: System.ReadOnlySpan[str], result: ref[System.Guid.GuidResult], ) -> bool:
        ...

    @staticmethod
    def TryParseExactN(guidString: System.ReadOnlySpan[str], result: ref[System.Guid.GuidResult], ) -> bool:
        ...

    @staticmethod
    def TryParseExactP(guidString: System.ReadOnlySpan[str], result: ref[System.Guid.GuidResult], ) -> bool:
        ...

    @staticmethod
    def TryParseExactX(guidString: System.ReadOnlySpan[str], result: ref[System.Guid.GuidResult], ) -> bool:
        ...

    @staticmethod
    def DecodeByte(ch1: System.UIntPtr, ch2: System.UIntPtr, invalidIfNegative: ref[int], ) -> int:
        ...

    @staticmethod
    @typing.overload
    def TryParseHex(guidString: System.ReadOnlySpan[str], result: ref[int], overflow: ref[bool], ) -> bool:
        ...

    @staticmethod
    @typing.overload
    def TryParseHex(guidString: System.ReadOnlySpan[str], result: ref[int], ) -> bool:
        ...

    @staticmethod
    @typing.overload
    def TryParseHex(guidString: System.ReadOnlySpan[str], result: ref[int], overflow: ref[bool], ) -> bool:
        ...

    @staticmethod
    def EatAllWhitespace(str: System.ReadOnlySpan[str], ) -> System.ReadOnlySpan[str]:
        ...

    @staticmethod
    def IsHexPrefix(str: System.ReadOnlySpan[str], i: int, ) -> bool:
        ...

    def ToByteArray(self, ) -> System.Array[int]:
        ...

    def TryWriteBytes(self, destination: System.Span[int], ) -> bool:
        ...

    @typing.overload
    def ToString(self, ) -> str:
        ...

    @typing.overload
    def ToString(self, format: str, ) -> str:
        ...

    @typing.overload
    def ToString(self, format: str, provider: System.IFormatProvider, ) -> str:
        ...

    def GetHashCode(self, ) -> int:
        ...

    @typing.overload
    def Equals(self, o: System.Object, ) -> bool:
        ...

    @typing.overload
    def Equals(self, g: System.Guid, ) -> bool:
        ...

    @staticmethod
    def EqualsCore(left: ref[System.Guid], right: ref[System.Guid], ) -> bool:
        ...

    @staticmethod
    def GetResult(me: int, them: int, ) -> int:
        ...

    @typing.overload
    def CompareTo(self, value: System.Object, ) -> int:
        ...

    @typing.overload
    def CompareTo(self, value: System.Guid, ) -> int:
        ...

    @staticmethod
    def HexsToChars(guidChars: ptr[str], a: int, b: int, ) -> int:
        ...

    @staticmethod
    def HexsToCharsHexOutput(guidChars: ptr[str], a: int, b: int, ) -> int:
        ...

    def TryFormat(self, destination: System.Span[str], charsWritten: ref[int], format: System.ReadOnlySpan[str] = ..., ) -> bool:
        ...

    def TryFormat(self, destination: System.Span[str], charsWritten: ref[int], format: System.ReadOnlySpan[str], provider: System.IFormatProvider, ) -> bool:
        ...

    @staticmethod
    def op_LessThan(left: System.Guid, right: System.Guid, ) -> bool:
        ...

    @staticmethod
    def op_LessThanOrEqual(left: System.Guid, right: System.Guid, ) -> bool:
        ...

    @staticmethod
    def op_GreaterThan(left: System.Guid, right: System.Guid, ) -> bool:
        ...

    @staticmethod
    def op_GreaterThanOrEqual(left: System.Guid, right: System.Guid, ) -> bool:
        ...

    @staticmethod
    def op_Equality(left: System.Guid, right: System.Guid, ) -> bool:
        ...

    @staticmethod
    def op_Inequality(left: System.Guid, right: System.Guid, ) -> bool:
        ...

    @staticmethod
    def Parse(s: str, provider: System.IFormatProvider, ) -> System.Guid:
        ...

    @staticmethod
    def TryParse(s: str, provider: System.IFormatProvider, result: ref[System.Guid], ) -> bool:
        ...

    @staticmethod
    def Parse(s: System.ReadOnlySpan[str], provider: System.IFormatProvider, ) -> System.Guid:
        ...

    @staticmethod
    def TryParse(s: System.ReadOnlySpan[str], provider: System.IFormatProvider, result: ref[System.Guid], ) -> bool:
        ...

    @staticmethod
    def NewGuid() -> System.Guid:
        ...

class UIntPtr(System.IEquatable[System.UIntPtr], System.IComparable, System.IComparable[System.UIntPtr], System.ISpanFormattable, System.IFormattable, System.Runtime.Serialization.ISerializable, System.IBinaryInteger[System.UIntPtr], System.IBinaryNumber[System.UIntPtr], System.IBitwiseOperators[System.UIntPtr, System.UIntPtr, System.UIntPtr], System.INumber[System.UIntPtr], System.IAdditionOperators[System.UIntPtr, System.UIntPtr, System.UIntPtr], System.IAdditiveIdentity[System.UIntPtr, System.UIntPtr], System.IComparisonOperators[System.UIntPtr, System.UIntPtr], System.IEqualityOperators[System.UIntPtr, System.UIntPtr], System.IDecrementOperators[System.UIntPtr], System.IDivisionOperators[System.UIntPtr, System.UIntPtr, System.UIntPtr], System.IIncrementOperators[System.UIntPtr], System.IModulusOperators[System.UIntPtr, System.UIntPtr, System.UIntPtr], System.IMultiplicativeIdentity[System.UIntPtr, System.UIntPtr], System.IMultiplyOperators[System.UIntPtr, System.UIntPtr, System.UIntPtr], System.ISpanParseable[System.UIntPtr], System.IParseable[System.UIntPtr], System.ISubtractionOperators[System.UIntPtr, System.UIntPtr, System.UIntPtr], System.IUnaryNegationOperators[System.UIntPtr, System.UIntPtr], System.IUnaryPlusOperators[System.UIntPtr, System.UIntPtr], System.IShiftOperators[System.UIntPtr, System.UIntPtr], System.IMinMaxValue[System.UIntPtr], System.IUnsignedNumber[System.UIntPtr], System.ValueType):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields
    Zero: System.UIntPtr = ...

    # properties
    @property
    def Size(self) -> int:
        ...

    @property
    def MaxValue(self) -> System.UIntPtr:
        ...

    @property
    def MinValue(self) -> System.UIntPtr:
        ...

    @property
    def AdditiveIdentity(self) -> System.UIntPtr:
        ...

    @property
    def MinValue(self) -> System.UIntPtr:
        ...

    @property
    def MaxValue(self) -> System.UIntPtr:
        ...

    @property
    def MultiplicativeIdentity(self) -> System.UIntPtr:
        ...

    @property
    def One(self) -> System.UIntPtr:
        ...

    @property
    def Zero(self) -> System.UIntPtr:
        ...

    # methods
    @typing.overload
    def __init__(self, value: int, ):
        ...

    @typing.overload
    def __init__(self, value: int, ):
        ...

    @typing.overload
    def __init__(self, value: ptr[None], ):
        ...

    @typing.overload
    def __init__(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext, ):
        ...

    @staticmethod
    def op_Increment(value: System.UIntPtr, ) -> System.UIntPtr:
        ...

    @staticmethod
    def op_Modulus(left: System.UIntPtr, right: System.UIntPtr, ) -> System.UIntPtr:
        ...

    @staticmethod
    def op_Multiply(left: System.UIntPtr, right: System.UIntPtr, ) -> System.UIntPtr:
        ...

    @staticmethod
    def Abs(value: System.UIntPtr, ) -> System.UIntPtr:
        ...

    @staticmethod
    def Clamp(value: System.UIntPtr, min: System.UIntPtr, max: System.UIntPtr, ) -> System.UIntPtr:
        ...

    @staticmethod
    def Create(value: TOther, ) -> System.UIntPtr:
        ...

    @staticmethod
    def CreateSaturating(value: TOther, ) -> System.UIntPtr:
        ...

    @staticmethod
    def CreateTruncating(value: TOther, ) -> System.UIntPtr:
        ...

    @staticmethod
    def DivRem(left: System.UIntPtr, right: System.UIntPtr, ) -> System.ValueTuple[System.UIntPtr, System.UIntPtr]:
        ...

    @staticmethod
    def Max(x: System.UIntPtr, y: System.UIntPtr, ) -> System.UIntPtr:
        ...

    @staticmethod
    def Min(x: System.UIntPtr, y: System.UIntPtr, ) -> System.UIntPtr:
        ...

    @staticmethod
    @typing.overload
    def Parse(s: str, style: int, provider: System.IFormatProvider, ) -> System.UIntPtr:
        ...

    @staticmethod
    @typing.overload
    def Parse(s: System.ReadOnlySpan[str], style: int, provider: System.IFormatProvider, ) -> System.UIntPtr:
        ...

    @staticmethod
    def Sign(value: System.UIntPtr, ) -> System.UIntPtr:
        ...

    @staticmethod
    def TryCreate(value: TOther, result: ref[System.UIntPtr], ) -> bool:
        ...

    @staticmethod
    @typing.overload
    def TryParse(s: str, style: int, provider: System.IFormatProvider, result: ref[System.UIntPtr], ) -> bool:
        ...

    @staticmethod
    @typing.overload
    def TryParse(s: System.ReadOnlySpan[str], style: int, provider: System.IFormatProvider, result: ref[System.UIntPtr], ) -> bool:
        ...

    @staticmethod
    def Parse(s: str, provider: System.IFormatProvider, ) -> System.UIntPtr:
        ...

    @staticmethod
    def TryParse(s: str, provider: System.IFormatProvider, result: ref[System.UIntPtr], ) -> bool:
        ...

    @staticmethod
    def op_LeftShift(value: System.UIntPtr, shiftAmount: int, ) -> System.UIntPtr:
        ...

    @staticmethod
    def op_RightShift(value: System.UIntPtr, shiftAmount: int, ) -> System.UIntPtr:
        ...

    @staticmethod
    def Parse(s: System.ReadOnlySpan[str], provider: System.IFormatProvider, ) -> System.UIntPtr:
        ...

    @staticmethod
    def TryParse(s: System.ReadOnlySpan[str], provider: System.IFormatProvider, result: ref[System.UIntPtr], ) -> bool:
        ...

    @staticmethod
    def op_Subtraction(left: System.UIntPtr, right: System.UIntPtr, ) -> System.UIntPtr:
        ...

    @staticmethod
    def op_UnaryNegation(value: System.UIntPtr, ) -> System.UIntPtr:
        ...

    @staticmethod
    def op_UnaryPlus(value: System.UIntPtr, ) -> System.UIntPtr:
        ...

    def GetObjectData(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext, ) -> None:
        ...

    @typing.overload
    def Equals(self, obj: System.Object, ) -> bool:
        ...

    @typing.overload
    def Equals(self, other: System.UIntPtr, ) -> bool:
        ...

    def GetHashCode(self, ) -> int:
        ...

    def ToUInt32(self, ) -> int:
        ...

    def ToUInt64(self, ) -> int:
        ...

    @staticmethod
    def Add(pointer: System.UIntPtr, offset: int, ) -> System.UIntPtr:
        ...

    @staticmethod
    def Subtract(pointer: System.UIntPtr, offset: int, ) -> System.UIntPtr:
        ...

    def ToPointer(self, ) -> ptr[None]:
        ...

    @typing.overload
    def CompareTo(self, value: System.Object, ) -> int:
        ...

    @typing.overload
    def CompareTo(self, value: System.UIntPtr, ) -> int:
        ...

    @typing.overload
    def ToString(self, ) -> str:
        ...

    @typing.overload
    def ToString(self, format: str, ) -> str:
        ...

    @typing.overload
    def ToString(self, provider: System.IFormatProvider, ) -> str:
        ...

    @typing.overload
    def ToString(self, format: str, provider: System.IFormatProvider, ) -> str:
        ...

    def TryFormat(self, destination: System.Span[str], charsWritten: ref[int], format: System.ReadOnlySpan[str] = ..., provider: System.IFormatProvider = ..., ) -> bool:
        ...

    @staticmethod
    @typing.overload
    def Parse(s: str, ) -> System.UIntPtr:
        ...

    @staticmethod
    @typing.overload
    def Parse(s: str, style: int, ) -> System.UIntPtr:
        ...

    @staticmethod
    @typing.overload
    def Parse(s: str, provider: System.IFormatProvider, ) -> System.UIntPtr:
        ...

    @staticmethod
    @typing.overload
    def Parse(s: str, style: int, provider: System.IFormatProvider, ) -> System.UIntPtr:
        ...

    @staticmethod
    @typing.overload
    def Parse(s: System.ReadOnlySpan[str], style: int = ..., provider: System.IFormatProvider = ..., ) -> System.UIntPtr:
        ...

    @staticmethod
    @typing.overload
    def TryParse(s: str, result: ref[System.UIntPtr], ) -> bool:
        ...

    @staticmethod
    @typing.overload
    def TryParse(s: str, style: int, provider: System.IFormatProvider, result: ref[System.UIntPtr], ) -> bool:
        ...

    @staticmethod
    @typing.overload
    def TryParse(s: System.ReadOnlySpan[str], result: ref[System.UIntPtr], ) -> bool:
        ...

    @staticmethod
    @typing.overload
    def TryParse(s: System.ReadOnlySpan[str], style: int, provider: System.IFormatProvider, result: ref[System.UIntPtr], ) -> bool:
        ...

    @staticmethod
    def op_Addition(left: System.UIntPtr, right: System.UIntPtr, ) -> System.UIntPtr:
        ...

    @staticmethod
    def LeadingZeroCount(value: System.UIntPtr, ) -> System.UIntPtr:
        ...

    @staticmethod
    def PopCount(value: System.UIntPtr, ) -> System.UIntPtr:
        ...

    @staticmethod
    def RotateLeft(value: System.UIntPtr, rotateAmount: int, ) -> System.UIntPtr:
        ...

    @staticmethod
    def RotateRight(value: System.UIntPtr, rotateAmount: int, ) -> System.UIntPtr:
        ...

    @staticmethod
    def TrailingZeroCount(value: System.UIntPtr, ) -> System.UIntPtr:
        ...

    @staticmethod
    def IsPow2(value: System.UIntPtr, ) -> bool:
        ...

    @staticmethod
    def Log2(value: System.UIntPtr, ) -> System.UIntPtr:
        ...

    @staticmethod
    def op_BitwiseAnd(left: System.UIntPtr, right: System.UIntPtr, ) -> System.UIntPtr:
        ...

    @staticmethod
    def op_BitwiseOr(left: System.UIntPtr, right: System.UIntPtr, ) -> System.UIntPtr:
        ...

    @staticmethod
    def op_ExclusiveOr(left: System.UIntPtr, right: System.UIntPtr, ) -> System.UIntPtr:
        ...

    @staticmethod
    def op_OnesComplement(value: System.UIntPtr, ) -> System.UIntPtr:
        ...

    @staticmethod
    def op_LessThan(left: System.UIntPtr, right: System.UIntPtr, ) -> bool:
        ...

    @staticmethod
    def op_LessThanOrEqual(left: System.UIntPtr, right: System.UIntPtr, ) -> bool:
        ...

    @staticmethod
    def op_GreaterThan(left: System.UIntPtr, right: System.UIntPtr, ) -> bool:
        ...

    @staticmethod
    def op_GreaterThanOrEqual(left: System.UIntPtr, right: System.UIntPtr, ) -> bool:
        ...

    @staticmethod
    def op_Decrement(value: System.UIntPtr, ) -> System.UIntPtr:
        ...

    @staticmethod
    def op_Division(left: System.UIntPtr, right: System.UIntPtr, ) -> System.UIntPtr:
        ...

    @staticmethod
    def op_Equality(left: System.UIntPtr, right: System.UIntPtr, ) -> bool:
        ...

    @staticmethod
    def op_Inequality(left: System.UIntPtr, right: System.UIntPtr, ) -> bool:
        ...

class Func(System.ICloneable, System.Runtime.Serialization.ISerializable, System.MulticastDelegate, typing.Generic[T1, T2, T3, T4, T5, TResult]):
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

    def Invoke(self, arg1: T1, arg2: T2, arg3: T3, arg4: T4, arg5: T5, ) -> TResult:
        ...

    def BeginInvoke(self, arg1: T1, arg2: T2, arg3: T3, arg4: T4, arg5: T5, callback: System.AsyncCallback, object: System.Object, ) -> System.IAsyncResult:
        ...

    def EndInvoke(self, result: System.IAsyncResult, ) -> TResult:
        ...

class IDisposable(abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    @abc.abstractmethod
    def Dispose(self, ) -> None:
        ...

class IConvertible(abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    @abc.abstractmethod
    def GetTypeCode(self, ) -> int:
        ...

    @abc.abstractmethod
    def ToBoolean(self, provider: System.IFormatProvider, ) -> bool:
        ...

    @abc.abstractmethod
    def ToChar(self, provider: System.IFormatProvider, ) -> str:
        ...

    @abc.abstractmethod
    def ToSByte(self, provider: System.IFormatProvider, ) -> int:
        ...

    @abc.abstractmethod
    def ToByte(self, provider: System.IFormatProvider, ) -> int:
        ...

    @abc.abstractmethod
    def ToInt16(self, provider: System.IFormatProvider, ) -> int:
        ...

    @abc.abstractmethod
    def ToUInt16(self, provider: System.IFormatProvider, ) -> int:
        ...

    @abc.abstractmethod
    def ToInt32(self, provider: System.IFormatProvider, ) -> int:
        ...

    @abc.abstractmethod
    def ToUInt32(self, provider: System.IFormatProvider, ) -> int:
        ...

    @abc.abstractmethod
    def ToInt64(self, provider: System.IFormatProvider, ) -> int:
        ...

    @abc.abstractmethod
    def ToUInt64(self, provider: System.IFormatProvider, ) -> int:
        ...

    @abc.abstractmethod
    def ToSingle(self, provider: System.IFormatProvider, ) -> float:
        ...

    @abc.abstractmethod
    def ToDouble(self, provider: System.IFormatProvider, ) -> float:
        ...

    @abc.abstractmethod
    def ToDecimal(self, provider: System.IFormatProvider, ) -> System.Decimal:
        ...

    @abc.abstractmethod
    def ToDateTime(self, provider: System.IFormatProvider, ) -> System.DateTime:
        ...

    @abc.abstractmethod
    def ToString(self, provider: System.IFormatProvider, ) -> str:
        ...

    @abc.abstractmethod
    def ToType(self, conversionType: System.Type, provider: System.IFormatProvider, ) -> System.Object:
        ...

class Delegate(System.ICloneable, System.Runtime.Serialization.ISerializable, System.Object, abc.ABC):
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
    @typing.overload
    def __init__(self, target: System.Object, method: str, ):
        ...

    @typing.overload
    def __init__(self, target: System.Type, method: str, ):
        ...

    def GetObjectData(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext, ) -> None:
        ...

    def Equals(self, obj: System.Object, ) -> bool:
        ...

    def CombineImpl(self, d: System.Delegate, ) -> System.Delegate:
        ...

    def RemoveImpl(self, d: System.Delegate, ) -> System.Delegate:
        ...

    def GetInvocationList(self, ) -> System.Array[System.Delegate]:
        ...

    def GetHashCode(self, ) -> int:
        ...

    def GetTarget(self, ) -> System.Object:
        ...

    def GetMethodImpl(self, ) -> System.Reflection.MethodInfo:
        ...

    def DynamicInvokeImpl(self, args: System.Array[System.Object], ) -> System.Object:
        ...

    @staticmethod
    @typing.overload
    def CreateDelegate(type: System.Type, target: System.Object, method: str, ignoreCase: bool, throwOnBindFailure: bool, ) -> System.Delegate:
        ...

    @staticmethod
    @typing.overload
    def CreateDelegate(type: System.Type, target: System.Type, method: str, ignoreCase: bool, throwOnBindFailure: bool, ) -> System.Delegate:
        ...

    @staticmethod
    @typing.overload
    def CreateDelegate(type: System.Type, method: System.Reflection.MethodInfo, throwOnBindFailure: bool, ) -> System.Delegate:
        ...

    @staticmethod
    @typing.overload
    def CreateDelegate(type: System.Type, firstArgument: System.Object, method: System.Reflection.MethodInfo, throwOnBindFailure: bool, ) -> System.Delegate:
        ...

    @staticmethod
    @typing.overload
    def CreateDelegate(type: System.Type, firstArgument: System.Object, method: System.Reflection.MethodInfo, ) -> System.Delegate:
        ...

    @staticmethod
    @typing.overload
    def CreateDelegate(type: System.Type, method: System.Reflection.MethodInfo, ) -> System.Delegate:
        ...

    @staticmethod
    @typing.overload
    def CreateDelegate(type: System.Type, target: System.Object, method: str, ) -> System.Delegate:
        ...

    @staticmethod
    @typing.overload
    def CreateDelegate(type: System.Type, target: System.Object, method: str, ignoreCase: bool, ) -> System.Delegate:
        ...

    @staticmethod
    @typing.overload
    def CreateDelegate(type: System.Type, target: System.Type, method: str, ) -> System.Delegate:
        ...

    @staticmethod
    @typing.overload
    def CreateDelegate(type: System.Type, target: System.Type, method: str, ignoreCase: bool, ) -> System.Delegate:
        ...

    @staticmethod
    def CreateDelegateNoSecurityCheck(type: System.Type, target: System.Object, method: System.RuntimeMethodHandle, ) -> System.Delegate:
        ...

    @staticmethod
    def CreateDelegateInternal(rtType: System.RuntimeType, rtMethod: System.Reflection.RuntimeMethodInfo, firstArgument: System.Object, flags: int, ) -> System.Delegate:
        ...

    def BindToMethodName(self, target: System.Object, methodType: System.RuntimeType, method: str, flags: int, ) -> bool:
        ...

    def BindToMethodInfo(self, target: System.Object, method: System.IRuntimeMethodInfo, methodType: System.RuntimeType, flags: int, ) -> bool:
        ...

    @staticmethod
    def InternalAlloc(type: System.RuntimeType, ) -> System.MulticastDelegate:
        ...

    @staticmethod
    def InternalAllocLike(d: System.Delegate, ) -> System.MulticastDelegate:
        ...

    @staticmethod
    def InternalEqualTypes(a: System.Object, b: System.Object, ) -> bool:
        ...

    def DelegateConstruct(self, target: System.Object, slot: System.IntPtr, ) -> None:
        ...

    def GetMulticastInvoke(self, ) -> System.IntPtr:
        ...

    def GetInvokeMethod(self, ) -> System.IntPtr:
        ...

    def FindMethodHandle(self, ) -> System.IRuntimeMethodInfo:
        ...

    @staticmethod
    def InternalEqualMethodHandles(left: System.Delegate, right: System.Delegate, ) -> bool:
        ...

    def AdjustTarget(self, target: System.Object, methodPtr: System.IntPtr, ) -> System.IntPtr:
        ...

    def GetCallStub(self, methodPtr: System.IntPtr, ) -> System.IntPtr:
        ...

    @staticmethod
    def CompareUnmanagedFunctionPtrs(d1: System.Delegate, d2: System.Delegate, ) -> bool:
        ...

    def Clone(self, ) -> System.Object:
        ...

    @staticmethod
    @typing.overload
    def Combine(a: System.Delegate, b: System.Delegate, ) -> System.Delegate:
        ...

    @staticmethod
    @typing.overload
    def Combine(delegates: System.Array[System.Delegate], ) -> System.Delegate:
        ...

    def DynamicInvoke(self, args: System.Array[System.Object], ) -> System.Object:
        ...

    @staticmethod
    def Remove(source: System.Delegate, value: System.Delegate, ) -> System.Delegate:
        ...

    @staticmethod
    def RemoveAll(source: System.Delegate, value: System.Delegate, ) -> System.Delegate:
        ...

class ResolveEventArgs(System.EventArgs):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def Name(self) -> str:
        ...

    @property
    def RequestingAssembly(self) -> System.Reflection.Assembly:
        ...

    # methods
    @typing.overload
    def __init__(self, name: str, ):
        ...

    @typing.overload
    def __init__(self, name: str, requestingAssembly: System.Reflection.Assembly, ):
        ...

class EventArgs(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields
    Empty: System.EventArgs = ...

    # properties
    # methods
    def __init__(self, ):
        ...

class IBinaryInteger(System.IBinaryNumber[TSelf], System.IBitwiseOperators[TSelf, TSelf, TSelf], System.INumber[TSelf], System.IAdditionOperators[TSelf, TSelf, TSelf], System.IAdditiveIdentity[TSelf, TSelf], System.IComparisonOperators[TSelf, TSelf], System.IComparable, System.IComparable[TSelf], System.IEqualityOperators[TSelf, TSelf], System.IEquatable[TSelf], System.IDecrementOperators[TSelf], System.IDivisionOperators[TSelf, TSelf, TSelf], System.IIncrementOperators[TSelf], System.IModulusOperators[TSelf, TSelf, TSelf], System.IMultiplicativeIdentity[TSelf, TSelf], System.IMultiplyOperators[TSelf, TSelf, TSelf], System.ISpanFormattable, System.IFormattable, System.ISpanParseable[TSelf], System.IParseable[TSelf], System.ISubtractionOperators[TSelf, TSelf, TSelf], System.IUnaryNegationOperators[TSelf, TSelf], System.IUnaryPlusOperators[TSelf, TSelf], System.IShiftOperators[TSelf, TSelf], abc.ABC, typing.Generic[TSelf]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    @staticmethod
    @abc.abstractmethod
    def LeadingZeroCount(value: TSelf, ) -> TSelf:
        ...

    @staticmethod
    @abc.abstractmethod
    def PopCount(value: TSelf, ) -> TSelf:
        ...

    @staticmethod
    @abc.abstractmethod
    def RotateLeft(value: TSelf, rotateAmount: int, ) -> TSelf:
        ...

    @staticmethod
    @abc.abstractmethod
    def RotateRight(value: TSelf, rotateAmount: int, ) -> TSelf:
        ...

    @staticmethod
    @abc.abstractmethod
    def TrailingZeroCount(value: TSelf, ) -> TSelf:
        ...

class MarshalByRefObject(System.Object, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    def __init__(self, ):
        ...

    def GetLifetimeService(self, ) -> System.Object:
        ...

    def InitializeLifetimeService(self, ) -> System.Object:
        ...

    def MemberwiseClone(self, cloneIdentity: bool, ) -> System.MarshalByRefObject:
        ...

class ArgumentException(System.Runtime.Serialization.ISerializable, System.SystemException):
    @typing.overload
    def __init__(self, **kwargs):
        self._message: str
        ...

    # static fields

    # properties
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
    def __init__(self, message: str, paramName: str, innerException: System.Exception, ):
        ...

    @typing.overload
    def __init__(self, message: str, paramName: str, ):
        ...

    @typing.overload
    def __init__(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext, ):
        ...

    def GetObjectData(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext, ) -> None:
        ...

    def SetMessageField(self, ) -> None:
        ...

class StringComparison(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    CurrentCulture: int = ...
    CurrentCultureIgnoreCase: int = ...
    InvariantCulture: int = ...
    InvariantCultureIgnoreCase: int = ...
    Ordinal: int = ...
    OrdinalIgnoreCase: int = ...

class MissingMemberException(System.Runtime.Serialization.ISerializable, System.MemberAccessException):
    @typing.overload
    def __init__(self, **kwargs):
        self.ClassName: str
        self.MemberName: str
        self.Signature: System.Array[int]
        self._message: str
        ...

    # static fields

    # properties
    @property
    def Message(self) -> str:
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
    def __init__(self, message: str, inner: System.Exception, ):
        ...

    @typing.overload
    def __init__(self, className: str, memberName: str, ):
        ...

    @typing.overload
    def __init__(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext, ):
        ...

    @staticmethod
    def FormatSignature(signature: System.Array[int], ) -> str:
        ...

    def GetObjectData(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext, ) -> None:
        ...

class MemberAccessException(System.Runtime.Serialization.ISerializable, System.SystemException):
    @typing.overload
    def __init__(self, **kwargs):
        self._message: str
        ...

    # static fields

    # properties
    @property
    def TargetSite(self) -> System.Reflection.MethodBase:
        ...

    @property
    def Message(self) -> str:
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
    def __init__(self, message: str, inner: System.Exception, ):
        ...

    @typing.overload
    def __init__(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext, ):
        ...

class IMultiplyOperators(abc.ABC, typing.Generic[TSelf, TOther, TResult]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
SByte = int

class IServiceProvider(abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    @abc.abstractmethod
    def GetService(self, serviceType: System.Type, ) -> System.Object:
        ...

class Predicate(System.ICloneable, System.Runtime.Serialization.ISerializable, System.MulticastDelegate, typing.Generic[T]):
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

    def Invoke(self, obj: T, ) -> bool:
        ...

    def BeginInvoke(self, obj: T, callback: System.AsyncCallback, object: System.Object, ) -> System.IAsyncResult:
        ...

    def EndInvoke(self, result: System.IAsyncResult, ) -> bool:
        ...

class Exception(System.Runtime.Serialization.ISerializable, System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        self._message: str
        ...

    # static fields
    InnerExceptionPrefix: str = ...

    # properties
    @property
    def TargetSite(self) -> System.Reflection.MethodBase:
        ...

    @property
    def HasBeenThrown(self) -> bool:
        ...

    @property
    def SerializationWatsonBuckets(self) -> System.Object:
        ...

    @property
    def Message(self) -> str:
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

    @property
    def SerializationStackTraceString(self) -> str:
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
    def __init__(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext, ):
        ...

    def GetObjectData(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext, ) -> None:
        ...

    def CreateDataContainer(self, ) -> System.Collections.IDictionary:
        ...

    @staticmethod
    def IsImmutableAgileException(e: System.Exception, ) -> bool:
        ...

    @staticmethod
    def GetMethodFromStackTrace(stackTrace: System.Object, ) -> System.IRuntimeMethodInfo:
        ...

    def GetExceptionMethodFromStackTrace(self, ) -> System.Reflection.MethodBase:
        ...

    def CreateSourceName(self, ) -> str:
        ...

    def OnDeserialized(self, context: System.Runtime.Serialization.StreamingContext, ) -> None:
        ...

    def InternalPreserveStackTrace(self, ) -> None:
        ...

    @staticmethod
    def PrepareForForeignExceptionRaise() -> None:
        ...

    @staticmethod
    def GetStackTracesDeepCopy(exception: System.Exception, currentStackTrace: ref[System.Array[int]], dynamicMethodArray: ref[System.Array[System.Object]], ) -> None:
        ...

    @staticmethod
    def SaveStackTracesFromDeepCopy(exception: System.Exception, currentStackTrace: System.Array[int], dynamicMethodArray: System.Array[System.Object], ) -> None:
        ...

    @staticmethod
    def GetExceptionCount() -> int:
        ...

    def RestoreDispatchState(self, dispatchState: ref[System.Exception.DispatchState], ) -> None:
        ...

    @staticmethod
    @typing.overload
    def GetMessageFromNativeResources(kind: int, ) -> str:
        ...

    @staticmethod
    @typing.overload
    def GetMessageFromNativeResources(kind: int, retMesg: System.Runtime.CompilerServices.StringHandleOnStack, ) -> None:
        ...

    def CaptureDispatchState(self, ) -> System.Exception.DispatchState:
        ...

    def CanSetRemoteStackTrace(self, ) -> bool:
        ...

    def GetClassName(self, ) -> str:
        ...

    def GetBaseException(self, ) -> System.Exception:
        ...

    def ToString(self, ) -> str:
        ...

    def GetType(self, ) -> System.Type:
        ...

    def RestoreRemoteStackTrace(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext, ) -> None:
        ...

    def GetStackTrace(self, ) -> str:
        ...

    def SetCurrentStackTrace(self, ) -> None:
        ...

    def SetRemoteStackTrace(self, stackTrace: str, ) -> None:
        ...

class TypeCode(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    Empty: int = ...
    Object: int = ...
    DBNull: int = ...
    Boolean: int = ...
    Char: int = ...
    SByte: int = ...
    Byte: int = ...
    Int16: int = ...
    UInt16: int = ...
    Int32: int = ...
    UInt32: int = ...
    Int64: int = ...
    UInt64: int = ...
    Single: int = ...
    Double: int = ...
    Decimal: int = ...
    DateTime: int = ...
    String: int = ...

class IFormattable(abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    @abc.abstractmethod
    def ToString(self, format: str, formatProvider: System.IFormatProvider, ) -> str:
        ...

class IIncrementOperators(abc.ABC, typing.Generic[TSelf]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
class Func(System.ICloneable, System.Runtime.Serialization.ISerializable, System.MulticastDelegate, typing.Generic[T1, T2, T3, T4, T5, T6, TResult]):
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

    def Invoke(self, arg1: T1, arg2: T2, arg3: T3, arg4: T4, arg5: T5, arg6: T6, ) -> TResult:
        ...

    def BeginInvoke(self, arg1: T1, arg2: T2, arg3: T3, arg4: T4, arg5: T5, arg6: T6, callback: System.AsyncCallback, object: System.Object, ) -> System.IAsyncResult:
        ...

    def EndInvoke(self, result: System.IAsyncResult, ) -> TResult:
        ...

class RuntimeTypeHandle(System.Runtime.Serialization.ISerializable, System.ValueType):
    @typing.overload
    def __init__(self, **kwargs):
        self.m_type: System.RuntimeType
        ...

    # static fields

    # properties
    @property
    def Value(self) -> System.IntPtr:
        ...

    # methods
    def __init__(self, type: System.RuntimeType, ):
        ...

    @staticmethod
    def GetUtf8Name(type: System.RuntimeType, ) -> System.MdUtf8String:
        ...

    @staticmethod
    def CanCastTo(type: System.RuntimeType, target: System.RuntimeType, ) -> bool:
        ...

    @staticmethod
    def GetDeclaringType(type: System.RuntimeType, ) -> System.RuntimeType:
        ...

    @staticmethod
    def GetDeclaringMethod(type: System.RuntimeType, ) -> System.IRuntimeMethodInfo:
        ...

    @staticmethod
    @typing.overload
    def GetTypeByName(name: str, throwOnError: bool, ignoreCase: bool, stackMark: System.Runtime.CompilerServices.StackCrawlMarkHandle, assemblyLoadContext: System.Runtime.CompilerServices.ObjectHandleOnStack, type: System.Runtime.CompilerServices.ObjectHandleOnStack, keepalive: System.Runtime.CompilerServices.ObjectHandleOnStack, ) -> None:
        ...

    @staticmethod
    @typing.overload
    def GetTypeByName(name: str, throwOnError: bool, ignoreCase: bool, stackMark: ref[int], ) -> System.RuntimeType:
        ...

    @staticmethod
    @typing.overload
    def GetTypeByName(name: str, throwOnError: bool, ignoreCase: bool, stackMark: ref[int], assemblyLoadContext: System.Runtime.Loader.AssemblyLoadContext, ) -> System.RuntimeType:
        ...

    @staticmethod
    @typing.overload
    def GetTypeByNameUsingCARules(name: str, scope: System.Runtime.CompilerServices.QCallModule, type: System.Runtime.CompilerServices.ObjectHandleOnStack, ) -> None:
        ...

    @staticmethod
    @typing.overload
    def GetTypeByNameUsingCARules(name: str, scope: System.Reflection.RuntimeModule, ) -> System.RuntimeType:
        ...

    @staticmethod
    def GetInstantiation(type: System.Runtime.CompilerServices.QCallTypeHandle, types: System.Runtime.CompilerServices.ObjectHandleOnStack, fAsRuntimeTypeArray: int, ) -> None:
        ...

    def GetInstantiationInternal(self, ) -> System.Array[System.RuntimeType]:
        ...

    def GetInstantiationPublic(self, ) -> System.Array[System.Type]:
        ...

    @staticmethod
    @typing.overload
    def Instantiate(handle: System.Runtime.CompilerServices.QCallTypeHandle, pInst: ptr[System.IntPtr], numGenericArgs: int, type: System.Runtime.CompilerServices.ObjectHandleOnStack, ) -> None:
        ...

    @typing.overload
    def Instantiate(self, inst: System.RuntimeType, ) -> System.RuntimeType:
        ...

    @typing.overload
    def Instantiate(self, inst: System.Array[System.Type], ) -> System.RuntimeType:
        ...

    @staticmethod
    @typing.overload
    def MakeArray(handle: System.Runtime.CompilerServices.QCallTypeHandle, rank: int, type: System.Runtime.CompilerServices.ObjectHandleOnStack, ) -> None:
        ...

    @typing.overload
    def MakeArray(self, rank: int, ) -> System.RuntimeType:
        ...

    @staticmethod
    @typing.overload
    def MakeSZArray(handle: System.Runtime.CompilerServices.QCallTypeHandle, type: System.Runtime.CompilerServices.ObjectHandleOnStack, ) -> None:
        ...

    @typing.overload
    def MakeSZArray(self, ) -> System.RuntimeType:
        ...

    @staticmethod
    @typing.overload
    def MakeByRef(handle: System.Runtime.CompilerServices.QCallTypeHandle, type: System.Runtime.CompilerServices.ObjectHandleOnStack, ) -> None:
        ...

    @typing.overload
    def MakeByRef(self, ) -> System.RuntimeType:
        ...

    @staticmethod
    @typing.overload
    def MakePointer(handle: System.Runtime.CompilerServices.QCallTypeHandle, type: System.Runtime.CompilerServices.ObjectHandleOnStack, ) -> None:
        ...

    @typing.overload
    def MakePointer(self, ) -> System.RuntimeType:
        ...

    @staticmethod
    def IsCollectible(handle: System.Runtime.CompilerServices.QCallTypeHandle, ) -> int:
        ...

    @staticmethod
    def HasInstantiation(type: System.RuntimeType, ) -> bool:
        ...

    @staticmethod
    @typing.overload
    def GetGenericTypeDefinition(type: System.Runtime.CompilerServices.QCallTypeHandle, retType: System.Runtime.CompilerServices.ObjectHandleOnStack, ) -> None:
        ...

    @staticmethod
    @typing.overload
    def GetGenericTypeDefinition(type: System.RuntimeType, ) -> System.RuntimeType:
        ...

    @staticmethod
    def IsGenericTypeDefinition(type: System.RuntimeType, ) -> bool:
        ...

    @staticmethod
    def IsGenericVariable(type: System.RuntimeType, ) -> bool:
        ...

    @staticmethod
    @typing.overload
    def GetGenericVariableIndex(type: System.RuntimeType, ) -> int:
        ...

    @typing.overload
    def GetGenericVariableIndex(self, ) -> int:
        ...

    @staticmethod
    @typing.overload
    def ContainsGenericVariables(handle: System.RuntimeType, ) -> bool:
        ...

    @typing.overload
    def ContainsGenericVariables(self, ) -> bool:
        ...

    @staticmethod
    @typing.overload
    def SatisfiesConstraints(paramType: System.RuntimeType, pTypeContext: ptr[System.IntPtr], typeContextLength: int, pMethodContext: ptr[System.IntPtr], methodContextLength: int, toType: System.RuntimeType, ) -> bool:
        ...

    @staticmethod
    @typing.overload
    def SatisfiesConstraints(paramType: System.RuntimeType, typeContext: System.Array[System.RuntimeType], methodContext: System.Array[System.RuntimeType], toType: System.RuntimeType, ) -> bool:
        ...

    @staticmethod
    def _GetMetadataImport(type: System.RuntimeType, ) -> System.IntPtr:
        ...

    @staticmethod
    def GetMetadataImport(type: System.RuntimeType, ) -> System.Reflection.MetadataImport:
        ...

    def GetObjectData(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext, ) -> None:
        ...

    @staticmethod
    def IsEquivalentTo(rtType1: System.RuntimeType, rtType2: System.RuntimeType, ) -> bool:
        ...

    def GetNativeHandle(self, ) -> System.RuntimeTypeHandle:
        ...

    def GetTypeChecked(self, ) -> System.RuntimeType:
        ...

    @staticmethod
    def IsInstanceOfType(type: System.RuntimeType, o: System.Object, ) -> bool:
        ...

    @staticmethod
    def GetTypeHelper(typeStart: System.Type, genericArgs: System.Array[System.Type], pModifiers: System.IntPtr, cModifiers: int, ) -> System.Type:
        ...

    def GetHashCode(self, ) -> int:
        ...

    @typing.overload
    def Equals(self, obj: System.Object, ) -> bool:
        ...

    @typing.overload
    def Equals(self, handle: System.RuntimeTypeHandle, ) -> bool:
        ...

    @staticmethod
    def GetValueInternal(handle: System.RuntimeTypeHandle, ) -> System.IntPtr:
        ...

    @staticmethod
    def IsTypeDefinition(type: System.RuntimeType, ) -> bool:
        ...

    @staticmethod
    def IsPrimitive(type: System.RuntimeType, ) -> bool:
        ...

    @staticmethod
    def IsByRef(type: System.RuntimeType, ) -> bool:
        ...

    @staticmethod
    def IsPointer(type: System.RuntimeType, ) -> bool:
        ...

    @staticmethod
    def IsArray(type: System.RuntimeType, ) -> bool:
        ...

    @staticmethod
    def IsSZArray(type: System.RuntimeType, ) -> bool:
        ...

    @staticmethod
    def HasElementType(type: System.RuntimeType, ) -> bool:
        ...

    @staticmethod
    @typing.overload
    def CopyRuntimeTypeHandles(inHandles: System.Array[System.RuntimeTypeHandle], length: ref[int], ) -> System.Array[System.IntPtr]:
        ...

    @staticmethod
    @typing.overload
    def CopyRuntimeTypeHandles(inHandles: System.Array[System.Type], length: ref[int], ) -> System.Array[System.IntPtr]:
        ...

    @staticmethod
    @typing.overload
    def CreateInstanceForAnotherGenericParameter(type: System.RuntimeType, genericParameter: System.RuntimeType, ) -> System.Object:
        ...

    @staticmethod
    @typing.overload
    def CreateInstanceForAnotherGenericParameter(type: System.RuntimeType, genericParameter1: System.RuntimeType, genericParameter2: System.RuntimeType, ) -> System.Object:
        ...

    @staticmethod
    @typing.overload
    def CreateInstanceForAnotherGenericParameter(baseType: System.Runtime.CompilerServices.QCallTypeHandle, pTypeHandles: ptr[System.IntPtr], cTypeHandles: int, instantiatedObject: System.Runtime.CompilerServices.ObjectHandleOnStack, ) -> None:
        ...

    @staticmethod
    @typing.overload
    def GetActivationInfo(rt: System.RuntimeType, pfnAllocator: ref[System.IntPtr], vAllocatorFirstArg: ref[ptr[None]], pfnCtor: ref[System.IntPtr], ctorIsPublic: ref[bool], ) -> None:
        ...

    @staticmethod
    @typing.overload
    def GetActivationInfo(pRuntimeType: System.Runtime.CompilerServices.ObjectHandleOnStack, ppfnAllocator: ptr[System.IntPtr], pvAllocatorFirstArg: ptr[ptr[None]], ppfnCtor: ptr[System.IntPtr], pfCtorIsPublic: ptr[int], ) -> None:
        ...

    def GetRuntimeType(self, ) -> System.RuntimeType:
        ...

    @staticmethod
    def GetCorElementType(type: System.RuntimeType, ) -> int:
        ...

    @staticmethod
    def GetAssembly(type: System.RuntimeType, ) -> System.Reflection.RuntimeAssembly:
        ...

    @staticmethod
    def GetModule(type: System.RuntimeType, ) -> System.Reflection.RuntimeModule:
        ...

    def GetModuleHandle(self, ) -> System.ModuleHandle:
        ...

    @staticmethod
    def GetBaseType(type: System.RuntimeType, ) -> System.RuntimeType:
        ...

    @staticmethod
    def GetAttributes(type: System.RuntimeType, ) -> int:
        ...

    @staticmethod
    def GetElementType(type: System.RuntimeType, ) -> System.RuntimeType:
        ...

    @staticmethod
    def CompareCanonicalHandles(left: System.RuntimeType, right: System.RuntimeType, ) -> bool:
        ...

    @staticmethod
    def GetArrayRank(type: System.RuntimeType, ) -> int:
        ...

    @staticmethod
    def GetToken(type: System.RuntimeType, ) -> int:
        ...

    @staticmethod
    def GetMethodAt(type: System.RuntimeType, slot: int, ) -> System.RuntimeMethodHandleInternal:
        ...

    @staticmethod
    def GetIntroducedMethods(type: System.RuntimeType, ) -> System.RuntimeTypeHandle.IntroducedMethodEnumerator:
        ...

    @staticmethod
    def GetFirstIntroducedMethod(type: System.RuntimeType, ) -> System.RuntimeMethodHandleInternal:
        ...

    @staticmethod
    def GetNextIntroducedMethod(method: ref[System.RuntimeMethodHandleInternal], ) -> None:
        ...

    @staticmethod
    def GetFields(type: System.RuntimeType, result: ptr[System.IntPtr], count: ptr[int], ) -> bool:
        ...

    @staticmethod
    def GetInterfaces(type: System.RuntimeType, ) -> System.Array[System.Type]:
        ...

    @staticmethod
    @typing.overload
    def GetConstraints(handle: System.Runtime.CompilerServices.QCallTypeHandle, types: System.Runtime.CompilerServices.ObjectHandleOnStack, ) -> None:
        ...

    @typing.overload
    def GetConstraints(self, ) -> System.Array[System.Type]:
        ...

    @staticmethod
    @typing.overload
    def GetGCHandle(handle: System.Runtime.CompilerServices.QCallTypeHandle, type: int, ) -> System.IntPtr:
        ...

    @typing.overload
    def GetGCHandle(self, type: int, ) -> System.IntPtr:
        ...

    @staticmethod
    @typing.overload
    def FreeGCHandle(typeHandle: System.Runtime.CompilerServices.QCallTypeHandle, objHandle: System.IntPtr, ) -> System.IntPtr:
        ...

    @typing.overload
    def FreeGCHandle(self, objHandle: System.IntPtr, ) -> System.IntPtr:
        ...

    @staticmethod
    def GetNumVirtuals(type: System.RuntimeType, ) -> int:
        ...

    @staticmethod
    def GetNumVirtualsAndStaticVirtuals(type: System.RuntimeType, ) -> int:
        ...

    @staticmethod
    @typing.overload
    def VerifyInterfaceIsImplemented(handle: System.Runtime.CompilerServices.QCallTypeHandle, interfaceHandle: System.Runtime.CompilerServices.QCallTypeHandle, ) -> None:
        ...

    @typing.overload
    def VerifyInterfaceIsImplemented(self, interfaceHandle: System.RuntimeTypeHandle, ) -> None:
        ...

    @staticmethod
    @typing.overload
    def GetInterfaceMethodImplementation(handle: System.Runtime.CompilerServices.QCallTypeHandle, interfaceHandle: System.Runtime.CompilerServices.QCallTypeHandle, interfaceMethodHandle: System.RuntimeMethodHandleInternal, ) -> System.RuntimeMethodHandleInternal:
        ...

    @typing.overload
    def GetInterfaceMethodImplementation(self, interfaceHandle: System.RuntimeTypeHandle, interfaceMethodHandle: System.RuntimeMethodHandleInternal, ) -> System.RuntimeMethodHandleInternal:
        ...

    @staticmethod
    def IsComObject(type: System.RuntimeType, isGenericCOM: bool, ) -> bool:
        ...

    @staticmethod
    def IsInterface(type: System.RuntimeType, ) -> bool:
        ...

    @staticmethod
    def IsByRefLike(type: System.RuntimeType, ) -> bool:
        ...

    @staticmethod
    def _IsVisible(typeHandle: System.Runtime.CompilerServices.QCallTypeHandle, ) -> bool:
        ...

    @staticmethod
    def IsVisible(type: System.RuntimeType, ) -> bool:
        ...

    @staticmethod
    def IsValueType(type: System.RuntimeType, ) -> bool:
        ...

    @staticmethod
    @typing.overload
    def ConstructName(handle: System.Runtime.CompilerServices.QCallTypeHandle, formatFlags: int, retString: System.Runtime.CompilerServices.StringHandleOnStack, ) -> None:
        ...

    @typing.overload
    def ConstructName(self, formatFlags: int, ) -> str:
        ...

    @staticmethod
    def _GetUtf8Name(type: System.RuntimeType, ) -> ptr[None]:
        ...

class Version(System.ICloneable, System.IComparable, System.IComparable[System.Version], System.IEquatable[System.Version], System.ISpanFormattable, System.IFormattable, System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def Major(self) -> int:
        ...

    @property
    def Minor(self) -> int:
        ...

    @property
    def Build(self) -> int:
        ...

    @property
    def Revision(self) -> int:
        ...

    @property
    def MajorRevision(self) -> int:
        ...

    @property
    def MinorRevision(self) -> int:
        ...

    @property
    def DefaultFormatFieldCount(self) -> int:
        ...

    # methods
    @typing.overload
    def __init__(self, major: int, minor: int, build: int, revision: int, ):
        ...

    @typing.overload
    def __init__(self, major: int, minor: int, build: int, ):
        ...

    @typing.overload
    def __init__(self, major: int, minor: int, ):
        ...

    @typing.overload
    def __init__(self, version: str, ):
        ...

    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def __init__(self, version: System.Version, ):
        ...

    def Clone(self, ) -> System.Object:
        ...

    @typing.overload
    def CompareTo(self, version: System.Object, ) -> int:
        ...

    @typing.overload
    def CompareTo(self, value: System.Version, ) -> int:
        ...

    @typing.overload
    def Equals(self, obj: System.Object, ) -> bool:
        ...

    @typing.overload
    def Equals(self, obj: System.Version, ) -> bool:
        ...

    def GetHashCode(self, ) -> int:
        ...

    @typing.overload
    def ToString(self, ) -> str:
        ...

    @typing.overload
    def ToString(self, fieldCount: int, ) -> str:
        ...

    def ToString(self, format: str, formatProvider: System.IFormatProvider, ) -> str:
        ...

    @typing.overload
    def TryFormat(self, destination: System.Span[str], charsWritten: ref[int], ) -> bool:
        ...

    @typing.overload
    def TryFormat(self, destination: System.Span[str], fieldCount: int, charsWritten: ref[int], ) -> bool:
        ...

    def TryFormat(self, destination: System.Span[str], charsWritten: ref[int], format: System.ReadOnlySpan[str], provider: System.IFormatProvider, ) -> bool:
        ...

    @staticmethod
    @typing.overload
    def Parse(input: str, ) -> System.Version:
        ...

    @staticmethod
    @typing.overload
    def Parse(input: System.ReadOnlySpan[str], ) -> System.Version:
        ...

    @staticmethod
    @typing.overload
    def TryParse(input: str, result: ref[System.Version], ) -> bool:
        ...

    @staticmethod
    @typing.overload
    def TryParse(input: System.ReadOnlySpan[str], result: ref[System.Version], ) -> bool:
        ...

    @staticmethod
    def ParseVersion(input: System.ReadOnlySpan[str], throwOnFailure: bool, ) -> System.Version:
        ...

    @staticmethod
    def TryParseComponent(component: System.ReadOnlySpan[str], componentName: str, throwOnFailure: bool, parsedComponent: ref[int], ) -> bool:
        ...

UInt16 = int

class PlatformID(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    Win32S: int = ...
    Win32Windows: int = ...
    Win32NT: int = ...
    WinCE: int = ...
    Unix: int = ...
    Xbox: int = ...
    MacOSX: int = ...
    Other: int = ...

class DateTimeOffset(System.IComparable, System.ISpanFormattable, System.IFormattable, System.IComparable[System.DateTimeOffset], System.IEquatable[System.DateTimeOffset], System.Runtime.Serialization.ISerializable, System.Runtime.Serialization.IDeserializationCallback, System.IAdditionOperators[System.DateTimeOffset, System.TimeSpan, System.DateTimeOffset], System.IAdditiveIdentity[System.DateTimeOffset, System.TimeSpan], System.IComparisonOperators[System.DateTimeOffset, System.DateTimeOffset], System.IEqualityOperators[System.DateTimeOffset, System.DateTimeOffset], System.IMinMaxValue[System.DateTimeOffset], System.ISpanParseable[System.DateTimeOffset], System.IParseable[System.DateTimeOffset], System.ISubtractionOperators[System.DateTimeOffset, System.TimeSpan, System.DateTimeOffset], System.ISubtractionOperators[System.DateTimeOffset, System.DateTimeOffset, System.TimeSpan], System.ValueType):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields
    MinValue: System.DateTimeOffset = ...
    MaxValue: System.DateTimeOffset = ...
    UnixEpoch: System.DateTimeOffset = ...

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
    def ClockDateTime(self) -> System.DateTime:
        ...

    @property
    def Date(self) -> System.DateTime:
        ...

    @property
    def Day(self) -> int:
        ...

    @property
    def DayOfWeek(self) -> int:
        ...

    @property
    def DayOfYear(self) -> int:
        ...

    @property
    def Hour(self) -> int:
        ...

    @property
    def Millisecond(self) -> int:
        ...

    @property
    def Minute(self) -> int:
        ...

    @property
    def Month(self) -> int:
        ...

    @property
    def Offset(self) -> System.TimeSpan:
        ...

    @property
    def Second(self) -> int:
        ...

    @property
    def Ticks(self) -> int:
        ...

    @property
    def UtcTicks(self) -> int:
        ...

    @property
    def TimeOfDay(self) -> System.TimeSpan:
        ...

    @property
    def Year(self) -> int:
        ...

    @property
    def AdditiveIdentity(self) -> System.TimeSpan:
        ...

    @property
    def MinValue(self) -> System.DateTimeOffset:
        ...

    @property
    def MaxValue(self) -> System.DateTimeOffset:
        ...

    # methods
    @typing.overload
    def __init__(self, validOffsetMinutes: int, validDateTime: System.DateTime, ):
        ...

    @typing.overload
    def __init__(self, ticks: int, offset: System.TimeSpan, ):
        ...

    @typing.overload
    def __init__(self, dateTime: System.DateTime, ):
        ...

    @typing.overload
    def __init__(self, dateTime: System.DateTime, offset: System.TimeSpan, ):
        ...

    @typing.overload
    def __init__(self, year: int, month: int, day: int, hour: int, minute: int, second: int, offset: System.TimeSpan, ):
        ...

    @typing.overload
    def __init__(self, year: int, month: int, day: int, hour: int, minute: int, second: int, millisecond: int, offset: System.TimeSpan, ):
        ...

    @typing.overload
    def __init__(self, year: int, month: int, day: int, hour: int, minute: int, second: int, millisecond: int, calendar: System.Globalization.Calendar, offset: System.TimeSpan, ):
        ...

    @typing.overload
    def __init__(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext, ):
        ...

    @staticmethod
    @typing.overload
    def TryParse(input: str, result: ref[System.DateTimeOffset], ) -> bool:
        ...

    @staticmethod
    @typing.overload
    def TryParse(input: System.ReadOnlySpan[str], result: ref[System.DateTimeOffset], ) -> bool:
        ...

    @staticmethod
    @typing.overload
    def TryParse(input: str, formatProvider: System.IFormatProvider, styles: int, result: ref[System.DateTimeOffset], ) -> bool:
        ...

    @staticmethod
    @typing.overload
    def TryParse(input: System.ReadOnlySpan[str], formatProvider: System.IFormatProvider, styles: int, result: ref[System.DateTimeOffset], ) -> bool:
        ...

    @staticmethod
    @typing.overload
    def TryParseExact(input: str, format: str, formatProvider: System.IFormatProvider, styles: int, result: ref[System.DateTimeOffset], ) -> bool:
        ...

    @staticmethod
    @typing.overload
    def TryParseExact(input: System.ReadOnlySpan[str], format: System.ReadOnlySpan[str], formatProvider: System.IFormatProvider, styles: int, result: ref[System.DateTimeOffset], ) -> bool:
        ...

    @staticmethod
    @typing.overload
    def TryParseExact(input: str, formats: System.Array[str], formatProvider: System.IFormatProvider, styles: int, result: ref[System.DateTimeOffset], ) -> bool:
        ...

    @staticmethod
    @typing.overload
    def TryParseExact(input: System.ReadOnlySpan[str], formats: System.Array[str], formatProvider: System.IFormatProvider, styles: int, result: ref[System.DateTimeOffset], ) -> bool:
        ...

    @staticmethod
    def ValidateOffset(offset: System.TimeSpan, ) -> int:
        ...

    @staticmethod
    def ValidateDate(dateTime: System.DateTime, offset: System.TimeSpan, ) -> System.DateTime:
        ...

    @staticmethod
    def ValidateStyles(style: int, parameterName: str, ) -> int:
        ...

    @staticmethod
    def op_Addition(left: System.DateTimeOffset, right: System.TimeSpan, ) -> System.DateTimeOffset:
        ...

    @staticmethod
    def op_LessThan(left: System.DateTimeOffset, right: System.DateTimeOffset, ) -> bool:
        ...

    @staticmethod
    def op_LessThanOrEqual(left: System.DateTimeOffset, right: System.DateTimeOffset, ) -> bool:
        ...

    @staticmethod
    def op_GreaterThan(left: System.DateTimeOffset, right: System.DateTimeOffset, ) -> bool:
        ...

    @staticmethod
    def op_GreaterThanOrEqual(left: System.DateTimeOffset, right: System.DateTimeOffset, ) -> bool:
        ...

    @staticmethod
    def op_Equality(left: System.DateTimeOffset, right: System.DateTimeOffset, ) -> bool:
        ...

    @staticmethod
    def op_Inequality(left: System.DateTimeOffset, right: System.DateTimeOffset, ) -> bool:
        ...

    @staticmethod
    def Parse(s: str, provider: System.IFormatProvider, ) -> System.DateTimeOffset:
        ...

    @staticmethod
    def TryParse(s: str, provider: System.IFormatProvider, result: ref[System.DateTimeOffset], ) -> bool:
        ...

    @staticmethod
    def Parse(s: System.ReadOnlySpan[str], provider: System.IFormatProvider, ) -> System.DateTimeOffset:
        ...

    @staticmethod
    def TryParse(s: System.ReadOnlySpan[str], provider: System.IFormatProvider, result: ref[System.DateTimeOffset], ) -> bool:
        ...

    @staticmethod
    def op_Subtraction(left: System.DateTimeOffset, right: System.TimeSpan, ) -> System.DateTimeOffset:
        ...

    @staticmethod
    def op_Subtraction(left: System.DateTimeOffset, right: System.DateTimeOffset, ) -> System.TimeSpan:
        ...

    def ToOffset(self, offset: System.TimeSpan, ) -> System.DateTimeOffset:
        ...

    def Add(self, timeSpan: System.TimeSpan, ) -> System.DateTimeOffset:
        ...

    def AddDays(self, days: float, ) -> System.DateTimeOffset:
        ...

    def AddHours(self, hours: float, ) -> System.DateTimeOffset:
        ...

    def AddMilliseconds(self, milliseconds: float, ) -> System.DateTimeOffset:
        ...

    def AddMinutes(self, minutes: float, ) -> System.DateTimeOffset:
        ...

    def AddMonths(self, months: int, ) -> System.DateTimeOffset:
        ...

    def AddSeconds(self, seconds: float, ) -> System.DateTimeOffset:
        ...

    def AddTicks(self, ticks: int, ) -> System.DateTimeOffset:
        ...

    def AddYears(self, years: int, ) -> System.DateTimeOffset:
        ...

    @staticmethod
    def Compare(first: System.DateTimeOffset, second: System.DateTimeOffset, ) -> int:
        ...

    def CompareTo(self, obj: System.Object, ) -> int:
        ...

    def CompareTo(self, other: System.DateTimeOffset, ) -> int:
        ...

    @typing.overload
    def Equals(self, obj: System.Object, ) -> bool:
        ...

    @typing.overload
    def Equals(self, other: System.DateTimeOffset, ) -> bool:
        ...

    @staticmethod
    @typing.overload
    def Equals(first: System.DateTimeOffset, second: System.DateTimeOffset, ) -> bool:
        ...

    def EqualsExact(self, other: System.DateTimeOffset, ) -> bool:
        ...

    @staticmethod
    def FromFileTime(fileTime: int, ) -> System.DateTimeOffset:
        ...

    @staticmethod
    def FromUnixTimeSeconds(seconds: int, ) -> System.DateTimeOffset:
        ...

    @staticmethod
    def FromUnixTimeMilliseconds(milliseconds: int, ) -> System.DateTimeOffset:
        ...

    def OnDeserialization(self, sender: System.Object, ) -> None:
        ...

    def GetObjectData(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext, ) -> None:
        ...

    def GetHashCode(self, ) -> int:
        ...

    @staticmethod
    @typing.overload
    def Parse(input: str, ) -> System.DateTimeOffset:
        ...

    @staticmethod
    @typing.overload
    def Parse(input: str, formatProvider: System.IFormatProvider, ) -> System.DateTimeOffset:
        ...

    @staticmethod
    @typing.overload
    def Parse(input: str, formatProvider: System.IFormatProvider, styles: int, ) -> System.DateTimeOffset:
        ...

    @staticmethod
    @typing.overload
    def Parse(input: System.ReadOnlySpan[str], formatProvider: System.IFormatProvider = ..., styles: int = ..., ) -> System.DateTimeOffset:
        ...

    @staticmethod
    @typing.overload
    def ParseExact(input: str, format: str, formatProvider: System.IFormatProvider, ) -> System.DateTimeOffset:
        ...

    @staticmethod
    @typing.overload
    def ParseExact(input: str, format: str, formatProvider: System.IFormatProvider, styles: int, ) -> System.DateTimeOffset:
        ...

    @staticmethod
    @typing.overload
    def ParseExact(input: System.ReadOnlySpan[str], format: System.ReadOnlySpan[str], formatProvider: System.IFormatProvider, styles: int = ..., ) -> System.DateTimeOffset:
        ...

    @staticmethod
    @typing.overload
    def ParseExact(input: str, formats: System.Array[str], formatProvider: System.IFormatProvider, styles: int, ) -> System.DateTimeOffset:
        ...

    @staticmethod
    @typing.overload
    def ParseExact(input: System.ReadOnlySpan[str], formats: System.Array[str], formatProvider: System.IFormatProvider, styles: int = ..., ) -> System.DateTimeOffset:
        ...

    @typing.overload
    def Subtract(self, value: System.DateTimeOffset, ) -> System.TimeSpan:
        ...

    @typing.overload
    def Subtract(self, value: System.TimeSpan, ) -> System.DateTimeOffset:
        ...

    def ToFileTime(self, ) -> int:
        ...

    def ToUnixTimeSeconds(self, ) -> int:
        ...

    def ToUnixTimeMilliseconds(self, ) -> int:
        ...

    @typing.overload
    def ToLocalTime(self, ) -> System.DateTimeOffset:
        ...

    @typing.overload
    def ToLocalTime(self, throwOnOverflow: bool, ) -> System.DateTimeOffset:
        ...

    @staticmethod
    @typing.overload
    def ToLocalTime(utcDateTime: System.DateTime, throwOnOverflow: bool, ) -> System.DateTimeOffset:
        ...

    @typing.overload
    def ToString(self, ) -> str:
        ...

    @typing.overload
    def ToString(self, format: str, ) -> str:
        ...

    @typing.overload
    def ToString(self, formatProvider: System.IFormatProvider, ) -> str:
        ...

    @typing.overload
    def ToString(self, format: str, formatProvider: System.IFormatProvider, ) -> str:
        ...

    def TryFormat(self, destination: System.Span[str], charsWritten: ref[int], format: System.ReadOnlySpan[str] = ..., formatProvider: System.IFormatProvider = ..., ) -> bool:
        ...

    def ToUniversalTime(self, ) -> System.DateTimeOffset:
        ...

class Span(System.ValueType, typing.Generic[T]):
    @typing.overload
    def __init__(self, **kwargs):
        self._pointer: System.ByReference[T]
        ...

    # static fields

    # properties
    @property
    def Item(self) -> ref[T]:
        ...

    @property
    def Length(self) -> int:
        ...

    @property
    def IsEmpty(self) -> bool:
        ...

    @property
    def Empty(self) -> System.Span:
        ...

    # methods
    @typing.overload
    def __init__(self, array: System.Array[T], ):
        ...

    @typing.overload
    def __init__(self, array: System.Array[T], start: int, length: int, ):
        ...

    @typing.overload
    def __init__(self, pointer: ptr[None], length: int, ):
        ...

    @typing.overload
    def __init__(self, ptr: ref[T], length: int, ):
        ...

    def Equals(self, obj: System.Object, ) -> bool:
        ...

    def GetHashCode(self, ) -> int:
        ...

    def GetEnumerator(self, ) -> System.Span.Enumerator[T]:
        ...

    def GetPinnableReference(self, ) -> ref[T]:
        ...

    def Clear(self, ) -> None:
        ...

    def Fill(self, value: T, ) -> None:
        ...

    def CopyTo(self, destination: System.Span, ) -> None:
        ...

    def TryCopyTo(self, destination: System.Span, ) -> bool:
        ...

    def ToString(self, ) -> str:
        ...

    @typing.overload
    def Slice(self, start: int, ) -> System.Span:
        ...

    @typing.overload
    def Slice(self, start: int, length: int, ) -> System.Span:
        ...

    def ToArray(self, ) -> System.Array[T]:
        ...

class IAdditionOperators(abc.ABC, typing.Generic[TSelf, TOther, TResult]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
class AggregateException(System.Runtime.Serialization.ISerializable, System.Exception):
    @typing.overload
    def __init__(self, **kwargs):
        self._message: str
        ...

    # static fields

    # properties
    @property
    def InnerExceptions(self) -> System.Collections.ObjectModel.ReadOnlyCollection[System.Exception]:
        ...

    @property
    def Message(self) -> str:
        ...

    @property
    def InnerExceptionCount(self) -> int:
        ...

    @property
    def InternalInnerExceptions(self) -> System.Array[System.Exception]:
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
    def __init__(self, innerExceptions: System.Collections.Generic.IEnumerable[System.Exception], ):
        ...

    @typing.overload
    def __init__(self, innerExceptions: System.Array[System.Exception], ):
        ...

    @typing.overload
    def __init__(self, message: str, innerExceptions: System.Collections.Generic.IEnumerable[System.Exception], ):
        ...

    @typing.overload
    def __init__(self, message: str, innerExceptions: System.Array[System.Exception], ):
        ...

    @typing.overload
    def __init__(self, message: str, innerExceptions: System.Array[System.Exception], cloneExceptions: bool, ):
        ...

    @typing.overload
    def __init__(self, innerExceptionInfos: System.Collections.Generic.List[System.Runtime.ExceptionServices.ExceptionDispatchInfo], ):
        ...

    @typing.overload
    def __init__(self, message: str, innerExceptionInfos: System.Collections.Generic.List[System.Runtime.ExceptionServices.ExceptionDispatchInfo], ):
        ...

    @typing.overload
    def __init__(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext, ):
        ...

    def GetObjectData(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext, ) -> None:
        ...

    def GetBaseException(self, ) -> System.Exception:
        ...

    def Handle(self, predicate: System.Func[System.Exception, bool], ) -> None:
        ...

    def Flatten(self, ) -> System.AggregateException:
        ...

    def ToString(self, ) -> str:
        ...

class ValueTuple(System.IEquatable[System.ValueTuple], System.Collections.IStructuralEquatable, System.Collections.IStructuralComparable, System.IComparable, System.IComparable[System.ValueTuple], System.IValueTupleInternal, System.Runtime.CompilerServices.ITuple, System.ValueType, typing.Generic[T1, T2]):
    @typing.overload
    def __init__(self, **kwargs):
        self.Item1: T1
        self.Item2: T2
        ...

    # static fields

    # properties
    @property
    def Length(self) -> int:
        ...

    @property
    def Item(self) -> System.Object:
        ...

    # methods
    def __init__(self, item1: T1, item2: T2, ):
        ...

    @typing.overload
    def Equals(self, obj: System.Object, ) -> bool:
        ...

    @typing.overload
    def Equals(self, other: System.ValueTuple, ) -> bool:
        ...

    def Equals(self, other: System.Object, comparer: System.Collections.IEqualityComparer, ) -> bool:
        ...

    def CompareTo(self, other: System.Object, ) -> int:
        ...

    def CompareTo(self, other: System.ValueTuple, ) -> int:
        ...

    def CompareTo(self, other: System.Object, comparer: System.Collections.IComparer, ) -> int:
        ...

    def GetHashCode(self, ) -> int:
        ...

    def GetHashCode(self, comparer: System.Collections.IEqualityComparer, ) -> int:
        ...

    def GetHashCodeCore(self, comparer: System.Collections.IEqualityComparer, ) -> int:
        ...

    def GetHashCode(self, comparer: System.Collections.IEqualityComparer, ) -> int:
        ...

    def ToString(self, ) -> str:
        ...

    def ToStringEnd(self, ) -> str:
        ...

class ValueTuple(System.IEquatable[System.ValueTuple], System.Collections.IStructuralEquatable, System.Collections.IStructuralComparable, System.IComparable, System.IComparable[System.ValueTuple], System.IValueTupleInternal, System.Runtime.CompilerServices.ITuple, System.ValueType, typing.Generic[T1, T2, T3]):
    @typing.overload
    def __init__(self, **kwargs):
        self.Item1: T1
        self.Item2: T2
        self.Item3: T3
        ...

    # static fields

    # properties
    @property
    def Length(self) -> int:
        ...

    @property
    def Item(self) -> System.Object:
        ...

    # methods
    def __init__(self, item1: T1, item2: T2, item3: T3, ):
        ...

    @typing.overload
    def Equals(self, obj: System.Object, ) -> bool:
        ...

    @typing.overload
    def Equals(self, other: System.ValueTuple, ) -> bool:
        ...

    def Equals(self, other: System.Object, comparer: System.Collections.IEqualityComparer, ) -> bool:
        ...

    def CompareTo(self, other: System.Object, ) -> int:
        ...

    def CompareTo(self, other: System.ValueTuple, ) -> int:
        ...

    def CompareTo(self, other: System.Object, comparer: System.Collections.IComparer, ) -> int:
        ...

    def GetHashCode(self, ) -> int:
        ...

    def GetHashCode(self, comparer: System.Collections.IEqualityComparer, ) -> int:
        ...

    def GetHashCodeCore(self, comparer: System.Collections.IEqualityComparer, ) -> int:
        ...

    def GetHashCode(self, comparer: System.Collections.IEqualityComparer, ) -> int:
        ...

    def ToString(self, ) -> str:
        ...

    def ToStringEnd(self, ) -> str:
        ...

class ArraySegment(System.Collections.Generic.IList[T], System.Collections.Generic.ICollection[T], System.Collections.Generic.IEnumerable[T], System.Collections.IEnumerable, System.Collections.Generic.IReadOnlyList[T], System.Collections.Generic.IReadOnlyCollection[T], System.ValueType, typing.Generic[T]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def Empty(self) -> System.ArraySegment:
        ...

    @property
    def Array(self) -> System.Array[T]:
        ...

    @property
    def Offset(self) -> int:
        ...

    @property
    def Count(self) -> int:
        ...

    @property
    def Item(self) -> T:
        ...
    @Item.setter
    def Item(self, val: T):
        ...

    @property
    def Item(self) -> T:
        ...
    @Item.setter
    def Item(self, val: T):
        ...

    @property
    def Item(self) -> T:
        ...

    @property
    def IsReadOnly(self) -> bool:
        ...

    # methods
    @typing.overload
    def __init__(self, array: System.Array[T], ):
        ...

    @typing.overload
    def __init__(self, array: System.Array[T], offset: int, count: int, ):
        ...

    def GetEnumerator(self, ) -> System.ArraySegment.Enumerator[T]:
        ...

    def GetHashCode(self, ) -> int:
        ...

    @typing.overload
    def CopyTo(self, destination: System.Array[T], ) -> None:
        ...

    @typing.overload
    def CopyTo(self, destination: System.Array[T], destinationIndex: int, ) -> None:
        ...

    @typing.overload
    def CopyTo(self, destination: System.ArraySegment, ) -> None:
        ...

    @typing.overload
    def Equals(self, obj: System.Object, ) -> bool:
        ...

    @typing.overload
    def Equals(self, obj: System.ArraySegment, ) -> bool:
        ...

    @typing.overload
    def Slice(self, index: int, ) -> System.ArraySegment:
        ...

    @typing.overload
    def Slice(self, index: int, count: int, ) -> System.ArraySegment:
        ...

    def ToArray(self, ) -> System.Array[T]:
        ...

    def IndexOf(self, item: T, ) -> int:
        ...

    def Insert(self, index: int, item: T, ) -> None:
        ...

    def RemoveAt(self, index: int, ) -> None:
        ...

    def Add(self, item: T, ) -> None:
        ...

    def Clear(self, ) -> None:
        ...

    def Contains(self, item: T, ) -> bool:
        ...

    def Remove(self, item: T, ) -> bool:
        ...

    def GetEnumerator(self, ) -> System.Collections.Generic.IEnumerator[T]:
        ...

    def GetEnumerator(self, ) -> System.Collections.IEnumerator:
        ...

    def ThrowInvalidOperationIfDefault(self, ) -> None:
        ...

class Lazy(System.Object, typing.Generic[T]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def ValueForDebugDisplay(self) -> T:
        ...

    @property
    def Mode(self) -> System.Nullable[int]:
        ...

    @property
    def IsValueFaulted(self) -> bool:
        ...

    @property
    def IsValueCreated(self) -> bool:
        ...

    @property
    def Value(self) -> T:
        ...

    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def __init__(self, value: T, ):
        ...

    @typing.overload
    def __init__(self, valueFactory: System.Func[T], ):
        ...

    @typing.overload
    def __init__(self, isThreadSafe: bool, ):
        ...

    @typing.overload
    def __init__(self, mode: int, ):
        ...

    @typing.overload
    def __init__(self, valueFactory: System.Func[T], isThreadSafe: bool, ):
        ...

    @typing.overload
    def __init__(self, valueFactory: System.Func[T], mode: int, ):
        ...

    @typing.overload
    def __init__(self, valueFactory: System.Func[T], mode: int, useDefaultConstructor: bool, ):
        ...

    @staticmethod
    def CreateViaDefaultConstructor() -> T:
        ...

    def ViaConstructor(self, ) -> None:
        ...

    def ViaFactory(self, mode: int, ) -> None:
        ...

    def ExecutionAndPublication(self, executionAndPublication: System.LazyHelper, useDefaultConstructor: bool, ) -> None:
        ...

    def PublicationOnly(self, publicationOnly: System.LazyHelper, possibleValue: T, ) -> None:
        ...

    def PublicationOnlyViaConstructor(self, initializer: System.LazyHelper, ) -> None:
        ...

    def PublicationOnlyViaFactory(self, initializer: System.LazyHelper, ) -> None:
        ...

    def PublicationOnlyWaitForOtherThreadToPublish(self, ) -> None:
        ...

    def CreateValue(self, ) -> T:
        ...

    def ToString(self, ) -> str:
        ...

class IBitwiseOperators(abc.ABC, typing.Generic[TSelf, TOther, TResult]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
class DBNull(System.Runtime.Serialization.ISerializable, System.IConvertible, System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields
    Value: System.DBNull = ...

    # properties
    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def __init__(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext, ):
        ...

    def GetObjectData(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext, ) -> None:
        ...

    @typing.overload
    def ToString(self, ) -> str:
        ...

    @typing.overload
    def ToString(self, provider: System.IFormatProvider, ) -> str:
        ...

    def GetTypeCode(self, ) -> int:
        ...

    def ToBoolean(self, provider: System.IFormatProvider, ) -> bool:
        ...

    def ToChar(self, provider: System.IFormatProvider, ) -> str:
        ...

    def ToSByte(self, provider: System.IFormatProvider, ) -> int:
        ...

    def ToByte(self, provider: System.IFormatProvider, ) -> int:
        ...

    def ToInt16(self, provider: System.IFormatProvider, ) -> int:
        ...

    def ToUInt16(self, provider: System.IFormatProvider, ) -> int:
        ...

    def ToInt32(self, provider: System.IFormatProvider, ) -> int:
        ...

    def ToUInt32(self, provider: System.IFormatProvider, ) -> int:
        ...

    def ToInt64(self, provider: System.IFormatProvider, ) -> int:
        ...

    def ToUInt64(self, provider: System.IFormatProvider, ) -> int:
        ...

    def ToSingle(self, provider: System.IFormatProvider, ) -> float:
        ...

    def ToDouble(self, provider: System.IFormatProvider, ) -> float:
        ...

    def ToDecimal(self, provider: System.IFormatProvider, ) -> System.Decimal:
        ...

    def ToDateTime(self, provider: System.IFormatProvider, ) -> System.DateTime:
        ...

    def ToType(self, type: System.Type, provider: System.IFormatProvider, ) -> System.Object:
        ...

class IComparisonOperators(System.IComparable, System.IComparable[TOther], System.IEqualityOperators[TSelf, TOther], System.IEquatable[TOther], abc.ABC, typing.Generic[TSelf, TOther]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
class Uri(System.Runtime.Serialization.ISerializable, System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        self._syntax: System.UriParser
        self._flags: int
        ...

    # static fields
    UriSchemeFile: str = ...
    UriSchemeFtp: str = ...
    UriSchemeSftp: str = ...
    UriSchemeFtps: str = ...
    UriSchemeGopher: str = ...
    UriSchemeHttp: str = ...
    UriSchemeHttps: str = ...
    UriSchemeWs: str = ...
    UriSchemeWss: str = ...
    UriSchemeMailto: str = ...
    UriSchemeNews: str = ...
    UriSchemeNntp: str = ...
    UriSchemeSsh: str = ...
    UriSchemeTelnet: str = ...
    UriSchemeNetTcp: str = ...
    UriSchemeNetPipe: str = ...
    SchemeDelimiter: str = ...

    # properties
    @property
    def IsImplicitFile(self) -> bool:
        ...

    @property
    def IsUncOrDosPath(self) -> bool:
        ...

    @property
    def IsDosPath(self) -> bool:
        ...

    @property
    def IsUncPath(self) -> bool:
        ...

    @property
    def IsUnixPath(self) -> bool:
        ...

    @property
    def HostType(self) -> int:
        ...

    @property
    def Syntax(self) -> System.UriParser:
        ...

    @property
    def IsNotAbsoluteUri(self) -> bool:
        ...

    @property
    def IriParsing(self) -> bool:
        ...

    @property
    def DisablePathAndQueryCanonicalization(self) -> bool:
        ...

    @property
    def UserDrivenParsing(self) -> bool:
        ...

    @property
    def SecuredPathIndex(self) -> int:
        ...

    @property
    def AbsolutePath(self) -> str:
        ...

    @property
    def PrivateAbsolutePath(self) -> str:
        ...

    @property
    def AbsoluteUri(self) -> str:
        ...

    @property
    def LocalPath(self) -> str:
        ...

    @property
    def Authority(self) -> str:
        ...

    @property
    def HostNameType(self) -> int:
        ...

    @property
    def IsDefaultPort(self) -> bool:
        ...

    @property
    def IsFile(self) -> bool:
        ...

    @property
    def IsLoopback(self) -> bool:
        ...

    @property
    def PathAndQuery(self) -> str:
        ...

    @property
    def Segments(self) -> System.Array[str]:
        ...

    @property
    def IsUnc(self) -> bool:
        ...

    @property
    def Host(self) -> str:
        ...

    @property
    def Port(self) -> int:
        ...

    @property
    def Query(self) -> str:
        ...

    @property
    def Fragment(self) -> str:
        ...

    @property
    def Scheme(self) -> str:
        ...

    @property
    def OriginalString(self) -> str:
        ...

    @property
    def DnsSafeHost(self) -> str:
        ...

    @property
    def IdnHost(self) -> str:
        ...

    @property
    def IsAbsoluteUri(self) -> bool:
        ...

    @property
    def UserEscaped(self) -> bool:
        ...

    @property
    def UserInfo(self) -> str:
        ...

    # methods
    @typing.overload
    def __init__(self, flags: int, uriParser: System.UriParser, uri: str, ):
        ...

    @typing.overload
    def __init__(self, uriString: str, ):
        ...

    @typing.overload
    def __init__(self, uriString: str, dontEscape: bool, ):
        ...

    @typing.overload
    def __init__(self, baseUri: System.Uri, relativeUri: str, dontEscape: bool, ):
        ...

    @typing.overload
    def __init__(self, uriString: str, uriKind: int, ):
        ...

    @typing.overload
    def __init__(self, uriString: str, creationOptions: ref[System.UriCreationOptions], ):
        ...

    @typing.overload
    def __init__(self, baseUri: System.Uri, relativeUri: str, ):
        ...

    @typing.overload
    def __init__(self, serializationInfo: System.Runtime.Serialization.SerializationInfo, streamingContext: System.Runtime.Serialization.StreamingContext, ):
        ...

    @typing.overload
    def __init__(self, baseUri: System.Uri, relativeUri: System.Uri, ):
        ...

    def GetUriPartsFromUserString(self, uriParts: int, ) -> str:
        ...

    def GetLengthWithoutTrailingSpaces(self, str: str, length: ref[int], idx: int, ) -> None:
        ...

    def ParseRemaining(self, ) -> None:
        ...

    @staticmethod
    def ParseSchemeCheckImplicitFile(uriString: ptr[str], length: int, err: ref[int], flags: ref[int], syntax: ref[System.UriParser], ) -> int:
        ...

    @staticmethod
    def CheckSchemeSyntax(span: System.ReadOnlySpan[str], syntax: ref[System.UriParser], ) -> int:
        ...

    def CheckAuthorityHelper(self, pString: ptr[str], idx: int, length: int, err: ref[int], flags: ref[int], syntax: System.UriParser, newHost: ref[str], ) -> int:
        ...

    def CheckAuthorityHelperHandleDnsIri(self, pString: ptr[str], start: int, end: int, hasUnicode: bool, flags: ref[int], justNormalized: ref[bool], newHost: ref[str], err: ref[int], ) -> None:
        ...

    def CheckCanonical(self, str: ptr[str], idx: ref[int], end: int, delim: str, ) -> int:
        ...

    def GetCanonicalPath(self, dest: ref[System.Text.ValueStringBuilder], formatAs: int, ) -> None:
        ...

    @staticmethod
    def UnescapeOnly(pch: ptr[str], start: int, end: ref[int], ch1: str, ch2: str, ch3: str, ) -> None:
        ...

    @staticmethod
    @typing.overload
    def Compress(dest: System.Array[str], start: int, destLength: ref[int], syntax: System.UriParser, ) -> None:
        ...

    @staticmethod
    @typing.overload
    def Compress(span: System.Span[str], syntax: System.UriParser, ) -> int:
        ...

    @staticmethod
    def CombineUri(basePart: System.Uri, relativePart: str, uriFormat: int, ) -> str:
        ...

    @staticmethod
    def PathDifference(path1: str, path2: str, compareCase: bool, ) -> str:
        ...

    def MakeRelative(self, toUri: System.Uri, ) -> str:
        ...

    def Canonicalize(self, ) -> None:
        ...

    def Parse(self, ) -> None:
        ...

    def Escape(self, ) -> None:
        ...

    def Unescape(self, path: str, ) -> str:
        ...

    @staticmethod
    def EscapeString(str: str, ) -> str:
        ...

    def CheckSecurity(self, ) -> None:
        ...

    def IsReservedCharacter(self, character: str, ) -> bool:
        ...

    @staticmethod
    def IsExcludedCharacter(character: str, ) -> bool:
        ...

    def IsBadFileSystemCharacter(self, character: str, ) -> bool:
        ...

    def CreateThis(self, uri: str, dontEscape: bool, uriKind: int, creationOptions: ref[System.UriCreationOptions] = ..., ) -> None:
        ...

    def InitializeUri(self, err: int, uriKind: int, e: ref[System.UriFormatException], ) -> None:
        ...

    @staticmethod
    def CheckForUnicodeOrEscapedUnreserved(data: str, ) -> bool:
        ...

    @staticmethod
    @typing.overload
    def TryCreate(uriString: str, uriKind: int, result: ref[System.Uri], ) -> bool:
        ...

    @staticmethod
    @typing.overload
    def TryCreate(uriString: str, creationOptions: ref[System.UriCreationOptions], result: ref[System.Uri], ) -> bool:
        ...

    @staticmethod
    @typing.overload
    def TryCreate(baseUri: System.Uri, relativeUri: str, result: ref[System.Uri], ) -> bool:
        ...

    @staticmethod
    @typing.overload
    def TryCreate(baseUri: System.Uri, relativeUri: System.Uri, result: ref[System.Uri], ) -> bool:
        ...

    def GetComponents(self, components: int, format: int, ) -> str:
        ...

    def InternalGetComponents(self, components: int, format: int, ) -> str:
        ...

    @staticmethod
    def Compare(uri1: System.Uri, uri2: System.Uri, partsToCompare: int, compareFormat: int, comparisonType: int, ) -> int:
        ...

    def IsWellFormedOriginalString(self, ) -> bool:
        ...

    @staticmethod
    def IsWellFormedUriString(uriString: str, uriKind: int, ) -> bool:
        ...

    def InternalIsWellFormedOriginalString(self, ) -> bool:
        ...

    @staticmethod
    def UnescapeDataString(stringToUnescape: str, ) -> str:
        ...

    @staticmethod
    def EscapeUriString(stringToEscape: str, ) -> str:
        ...

    @staticmethod
    def EscapeDataString(stringToEscape: str, ) -> str:
        ...

    def EscapeUnescapeIri(self, input: str, start: int, end: int, component: int, ) -> str:
        ...

    @staticmethod
    def CreateHelper(uriString: str, dontEscape: bool, uriKind: int, e: ref[System.UriFormatException], creationOptions: ref[System.UriCreationOptions] = ..., ) -> System.Uri:
        ...

    @staticmethod
    def ResolveHelper(baseUri: System.Uri, relativeUri: System.Uri, newUriString: ref[str], userEscaped: ref[bool], ) -> System.Uri:
        ...

    def GetRelativeSerializationString(self, format: int, ) -> str:
        ...

    def GetComponentsHelper(self, uriComponents: int, uriFormat: int, ) -> str:
        ...

    def IsBaseOf(self, uri: System.Uri, ) -> bool:
        ...

    def IsBaseOfHelper(self, uriLink: System.Uri, ) -> bool:
        ...

    def CreateThisFromUri(self, otherUri: System.Uri, ) -> None:
        ...

    def InterlockedSetFlags(self, flags: int, ) -> None:
        ...

    @staticmethod
    def IriParsingStatic(syntax: System.UriParser, ) -> bool:
        ...

    def NotAny(self, flags: int, ) -> bool:
        ...

    def InFact(self, flags: int, ) -> bool:
        ...

    @staticmethod
    def StaticNotAny(allFlags: int, checkFlags: int, ) -> bool:
        ...

    @staticmethod
    def StaticInFact(allFlags: int, checkFlags: int, ) -> bool:
        ...

    def EnsureUriInfo(self, ) -> System.Uri.UriInfo:
        ...

    def EnsureParseRemaining(self, ) -> None:
        ...

    def EnsureHostString(self, allowDnsOptimization: bool, ) -> None:
        ...

    def GetObjectData(self, serializationInfo: System.Runtime.Serialization.SerializationInfo, streamingContext: System.Runtime.Serialization.StreamingContext, ) -> None:
        ...

    def GetObjectData(self, serializationInfo: System.Runtime.Serialization.SerializationInfo, streamingContext: System.Runtime.Serialization.StreamingContext, ) -> None:
        ...

    def CreateUri(self, baseUri: System.Uri, relativeUri: str, dontEscape: bool, ) -> None:
        ...

    @staticmethod
    def GetCombinedString(baseUri: System.Uri, relativeStr: str, dontEscape: bool, result: ref[str], ) -> None:
        ...

    @staticmethod
    def GetException(err: int, ) -> System.UriFormatException:
        ...

    @staticmethod
    def StaticIsFile(syntax: System.UriParser, ) -> bool:
        ...

    def GetLocalPath(self, ) -> str:
        ...

    @staticmethod
    def CheckHostName(name: str, ) -> int:
        ...

    def GetLeftPart(self, part: int, ) -> str:
        ...

    @staticmethod
    def HexEscape(character: str, ) -> str:
        ...

    @staticmethod
    def HexUnescape(pattern: str, index: ref[int], ) -> str:
        ...

    @staticmethod
    def IsHexEncoding(pattern: str, index: int, ) -> bool:
        ...

    @staticmethod
    def CheckSchemeName(schemeName: str, ) -> bool:
        ...

    @staticmethod
    def IsHexDigit(character: str, ) -> bool:
        ...

    @staticmethod
    def FromHex(digit: str, ) -> int:
        ...

    def GetHashCode(self, ) -> int:
        ...

    def ToString(self, ) -> str:
        ...

    def Equals(self, comparand: System.Object, ) -> bool:
        ...

    def MakeRelativeUri(self, uri: System.Uri, ) -> System.Uri:
        ...

    @staticmethod
    def CheckForColonInFirstPathSegment(uriString: str, ) -> bool:
        ...

    @staticmethod
    def InternalEscapeString(rawString: str, ) -> str:
        ...

    @staticmethod
    def ParseScheme(uriString: str, flags: ref[int], syntax: ref[System.UriParser], ) -> int:
        ...

    def ParseMinimal(self, ) -> System.UriFormatException:
        ...

    def PrivateParseMinimal(self, ) -> int:
        ...

    def CreateUriInfo(self, cF: int, ) -> None:
        ...

    def CreateHostString(self, ) -> None:
        ...

    @staticmethod
    def CreateHostStringHelper(str: str, idx: int, end: int, flags: ref[int], scopeId: ref[str], ) -> str:
        ...

    def GetHostViaCustomSyntax(self, ) -> None:
        ...

    def GetParts(self, uriParts: int, formatAs: int, ) -> str:
        ...

    def GetEscapedParts(self, uriParts: int, ) -> str:
        ...

    def GetUnescapedParts(self, uriParts: int, formatAs: int, ) -> str:
        ...

    def ReCreateParts(self, parts: int, nonCanonical: int, formatAs: int, ) -> str:
        ...

class UriComponents(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    Scheme: int = ...
    UserInfo: int = ...
    Host: int = ...
    Port: int = ...
    SchemeAndServer: int = ...
    Path: int = ...
    Query: int = ...
    PathAndQuery: int = ...
    HttpRequestUrl: int = ...
    Fragment: int = ...
    AbsoluteUri: int = ...
    StrongPort: int = ...
    HostAndPort: int = ...
    StrongAuthority: int = ...
    NormalizedHost: int = ...
    KeepDelimiter: int = ...
    SerializationInfoString: int = ...

class UriHostNameType(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    Unknown: int = ...
    Basic: int = ...
    Dns: int = ...
    IPv4: int = ...
    IPv6: int = ...

class UriPartial(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    Scheme: int = ...
    Authority: int = ...
    Path: int = ...
    Query: int = ...

class UriParser(System.Object, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields
    HttpUri: System.UriParser = ...
    HttpsUri: System.UriParser = ...
    WsUri: System.UriParser = ...
    WssUri: System.UriParser = ...
    FtpUri: System.UriParser = ...
    FileUri: System.UriParser = ...
    UnixFileUri: System.UriParser = ...
    GopherUri: System.UriParser = ...
    NntpUri: System.UriParser = ...
    NewsUri: System.UriParser = ...
    MailToUri: System.UriParser = ...
    UuidUri: System.UriParser = ...
    TelnetUri: System.UriParser = ...
    LdapUri: System.UriParser = ...
    NetTcpUri: System.UriParser = ...
    NetPipeUri: System.UriParser = ...
    VsMacrosUri: System.UriParser = ...

    # properties
    @property
    def SchemeName(self) -> str:
        ...

    @property
    def DefaultPort(self) -> int:
        ...

    @property
    def Flags(self) -> int:
        ...

    @property
    def IsSimple(self) -> bool:
        ...

    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def __init__(self, flags: int, ):
        ...

    def OnNewUri(self, ) -> System.UriParser:
        ...

    def OnRegister(self, schemeName: str, defaultPort: int, ) -> None:
        ...

    def InitializeAndValidate(self, uri: System.Uri, parsingError: ref[System.UriFormatException], ) -> None:
        ...

    def Resolve(self, baseUri: System.Uri, relativeUri: System.Uri, parsingError: ref[System.UriFormatException], ) -> str:
        ...

    def IsBaseOf(self, baseUri: System.Uri, relativeUri: System.Uri, ) -> bool:
        ...

    def GetComponents(self, uri: System.Uri, components: int, format: int, ) -> str:
        ...

    def IsWellFormedOriginalString(self, uri: System.Uri, ) -> bool:
        ...

    @staticmethod
    def Register(uriParser: System.UriParser, schemeName: str, defaultPort: int, ) -> None:
        ...

    @staticmethod
    def IsKnownScheme(schemeName: str, ) -> bool:
        ...

    def NotAny(self, flags: int, ) -> bool:
        ...

    def InFact(self, flags: int, ) -> bool:
        ...

    def IsAllSet(self, flags: int, ) -> bool:
        ...

    def IsFullMatch(self, flags: int, expected: int, ) -> bool:
        ...

    @staticmethod
    def FetchSyntax(syntax: System.UriParser, lwrCaseSchemeName: str, defaultPort: int, ) -> None:
        ...

    @staticmethod
    def FindOrFetchAsUnknownV1Syntax(lwrCaseScheme: str, ) -> System.UriParser:
        ...

    @staticmethod
    def GetSyntax(lwrCaseScheme: str, ) -> System.UriParser:
        ...

    def CheckSetIsSimpleFlag(self, ) -> None:
        ...

    def InternalOnNewUri(self, ) -> System.UriParser:
        ...

    def InternalValidate(self, thisUri: System.Uri, parsingError: ref[System.UriFormatException], ) -> None:
        ...

    def InternalResolve(self, thisBaseUri: System.Uri, uriLink: System.Uri, parsingError: ref[System.UriFormatException], ) -> str:
        ...

    def InternalIsBaseOf(self, thisBaseUri: System.Uri, uriLink: System.Uri, ) -> bool:
        ...

    def InternalGetComponents(self, thisUri: System.Uri, uriComponents: int, uriFormat: int, ) -> str:
        ...

    def InternalIsWellFormedOriginalString(self, thisUri: System.Uri, ) -> bool:
        ...

class UriCreationOptions(System.ValueType):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def DangerousDisablePathAndQueryCanonicalization(self) -> bool:
        ...
    @DangerousDisablePathAndQueryCanonicalization.setter
    def DangerousDisablePathAndQueryCanonicalization(self, val: bool):
        ...

    # methods
class UriFormatException(System.Runtime.Serialization.ISerializable, System.FormatException):
    @typing.overload
    def __init__(self, **kwargs):
        self._message: str
        ...

    # static fields

    # properties
    @property
    def TargetSite(self) -> System.Reflection.MethodBase:
        ...

    @property
    def Message(self) -> str:
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
    def __init__(self, textString: str, ):
        ...

    @typing.overload
    def __init__(self, textString: str, e: System.Exception, ):
        ...

    @typing.overload
    def __init__(self, serializationInfo: System.Runtime.Serialization.SerializationInfo, streamingContext: System.Runtime.Serialization.StreamingContext, ):
        ...

    def GetObjectData(self, serializationInfo: System.Runtime.Serialization.SerializationInfo, streamingContext: System.Runtime.Serialization.StreamingContext, ) -> None:
        ...

class FormatException(System.Runtime.Serialization.ISerializable, System.SystemException):
    @typing.overload
    def __init__(self, **kwargs):
        self._message: str
        ...

    # static fields

    # properties
    @property
    def TargetSite(self) -> System.Reflection.MethodBase:
        ...

    @property
    def Message(self) -> str:
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
    def __init__(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext, ):
        ...

class UriKind(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    RelativeOrAbsolute: int = ...
    Absolute: int = ...
    Relative: int = ...

class IFormatProvider(abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    @abc.abstractmethod
    def GetFormat(self, formatType: System.Type, ) -> System.Object:
        ...

class Enum(System.IComparable, System.IFormattable, System.IConvertible, System.ValueType, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    def __init__(self, ):
        ...

    def ToInt32(self, provider: System.IFormatProvider, ) -> int:
        ...

    def ToUInt32(self, provider: System.IFormatProvider, ) -> int:
        ...

    def ToInt64(self, provider: System.IFormatProvider, ) -> int:
        ...

    def ToUInt64(self, provider: System.IFormatProvider, ) -> int:
        ...

    def ToSingle(self, provider: System.IFormatProvider, ) -> float:
        ...

    def ToDouble(self, provider: System.IFormatProvider, ) -> float:
        ...

    def ToDecimal(self, provider: System.IFormatProvider, ) -> System.Decimal:
        ...

    def ToDateTime(self, provider: System.IFormatProvider, ) -> System.DateTime:
        ...

    def ToType(self, type: System.Type, provider: System.IFormatProvider, ) -> System.Object:
        ...

    @staticmethod
    @typing.overload
    def ToObject(enumType: System.Type, value: int, ) -> System.Object:
        ...

    @staticmethod
    @typing.overload
    def ToObject(enumType: System.Type, value: int, ) -> System.Object:
        ...

    @staticmethod
    @typing.overload
    def ToObject(enumType: System.Type, value: int, ) -> System.Object:
        ...

    @staticmethod
    @typing.overload
    def ToObject(enumType: System.Type, value: int, ) -> System.Object:
        ...

    @staticmethod
    @typing.overload
    def ToObject(enumType: System.Type, value: int, ) -> System.Object:
        ...

    @staticmethod
    @typing.overload
    def ToObject(enumType: System.Type, value: int, ) -> System.Object:
        ...

    @staticmethod
    @typing.overload
    def ToObject(enumType: System.Type, value: int, ) -> System.Object:
        ...

    @staticmethod
    @typing.overload
    def ToObject(enumType: System.Type, value: int, ) -> System.Object:
        ...

    @staticmethod
    @typing.overload
    def ToObject(enumType: System.Type, value: str, ) -> System.Object:
        ...

    @staticmethod
    @typing.overload
    def ToObject(enumType: System.Type, value: bool, ) -> System.Object:
        ...

    @staticmethod
    @typing.overload
    def ToObject(enumType: System.Type, value: System.Object, ) -> System.Object:
        ...

    @staticmethod
    def ValidateRuntimeType(enumType: System.Type, ) -> System.RuntimeType:
        ...

    @staticmethod
    def GetEnumValuesAndNames(enumType: System.Runtime.CompilerServices.QCallTypeHandle, values: System.Runtime.CompilerServices.ObjectHandleOnStack, names: System.Runtime.CompilerServices.ObjectHandleOnStack, getNames: int, ) -> None:
        ...

    def Equals(self, obj: System.Object, ) -> bool:
        ...

    @staticmethod
    def InternalBoxEnum(enumType: System.RuntimeType, value: int, ) -> System.Object:
        ...

    def InternalGetCorElementType(self, ) -> int:
        ...

    @staticmethod
    def InternalGetUnderlyingType(enumType: System.RuntimeType, ) -> System.RuntimeType:
        ...

    def InternalHasFlag(self, flags: System.Enum, ) -> bool:
        ...

    @staticmethod
    def GetEnumInfo(enumType: System.RuntimeType, getNames: bool = ..., ) -> System.Enum.EnumInfo:
        ...

    def ValueToString(self, ) -> str:
        ...

    @typing.overload
    def ValueToHexString(self, ) -> str:
        ...

    @staticmethod
    @typing.overload
    def ValueToHexString(value: System.Object, ) -> str:
        ...

    @staticmethod
    @typing.overload
    def GetEnumName(enumType: System.RuntimeType, ulValue: int, ) -> str:
        ...

    @staticmethod
    @typing.overload
    def GetEnumName(enumInfo: System.Enum.EnumInfo, ulValue: int, ) -> str:
        ...

    @staticmethod
    def InternalFormat(enumType: System.RuntimeType, value: int, ) -> str:
        ...

    @staticmethod
    @typing.overload
    def InternalFlagsFormat(enumType: System.RuntimeType, result: int, ) -> str:
        ...

    @staticmethod
    @typing.overload
    def InternalFlagsFormat(enumInfo: System.Enum.EnumInfo, resultValue: int, ) -> str:
        ...

    @staticmethod
    @typing.overload
    def ToUInt64(value: System.Object, ) -> int:
        ...

    @staticmethod
    @typing.overload
    def ToUInt64(value: TEnum, ) -> int:
        ...

    @typing.overload
    def ToUInt64(self, ) -> int:
        ...

    @staticmethod
    @typing.overload
    def GetName(value: TEnum, ) -> str:
        ...

    @staticmethod
    @typing.overload
    def GetName(enumType: System.Type, value: System.Object, ) -> str:
        ...

    @staticmethod
    @typing.overload
    def GetNames() -> System.Array[str]:
        ...

    @staticmethod
    @typing.overload
    def GetNames(enumType: System.Type, ) -> System.Array[str]:
        ...

    @staticmethod
    def InternalGetNames(enumType: System.RuntimeType, ) -> System.Array[str]:
        ...

    @staticmethod
    def GetUnderlyingType(enumType: System.Type, ) -> System.Type:
        ...

    @staticmethod
    @typing.overload
    def GetValues() -> System.Array[TEnum]:
        ...

    @staticmethod
    @typing.overload
    def GetValues(enumType: System.Type, ) -> System.Array:
        ...

    def HasFlag(self, flag: System.Enum, ) -> bool:
        ...

    @staticmethod
    def InternalGetValues(enumType: System.RuntimeType, ) -> System.Array[int]:
        ...

    @staticmethod
    @typing.overload
    def IsDefined(value: TEnum, ) -> bool:
        ...

    @staticmethod
    @typing.overload
    def IsDefined(enumType: System.Type, value: System.Object, ) -> bool:
        ...

    @staticmethod
    @typing.overload
    def Parse(enumType: System.Type, value: str, ) -> System.Object:
        ...

    @staticmethod
    @typing.overload
    def Parse(enumType: System.Type, value: System.ReadOnlySpan[str], ) -> System.Object:
        ...

    @staticmethod
    @typing.overload
    def Parse(enumType: System.Type, value: str, ignoreCase: bool, ) -> System.Object:
        ...

    @staticmethod
    @typing.overload
    def Parse(enumType: System.Type, value: System.ReadOnlySpan[str], ignoreCase: bool, ) -> System.Object:
        ...

    @staticmethod
    @typing.overload
    def Parse(value: str, ) -> TEnum:
        ...

    @staticmethod
    @typing.overload
    def Parse(value: System.ReadOnlySpan[str], ) -> TEnum:
        ...

    @staticmethod
    @typing.overload
    def Parse(value: str, ignoreCase: bool, ) -> TEnum:
        ...

    @staticmethod
    @typing.overload
    def Parse(value: System.ReadOnlySpan[str], ignoreCase: bool, ) -> TEnum:
        ...

    @staticmethod
    @typing.overload
    def TryParse(enumType: System.Type, value: str, result: ref[System.Object], ) -> bool:
        ...

    @staticmethod
    @typing.overload
    def TryParse(enumType: System.Type, value: System.ReadOnlySpan[str], result: ref[System.Object], ) -> bool:
        ...

    @staticmethod
    @typing.overload
    def TryParse(enumType: System.Type, value: str, ignoreCase: bool, result: ref[System.Object], ) -> bool:
        ...

    @staticmethod
    @typing.overload
    def TryParse(enumType: System.Type, value: System.ReadOnlySpan[str], ignoreCase: bool, result: ref[System.Object], ) -> bool:
        ...

    @staticmethod
    @typing.overload
    def TryParse(enumType: System.Type, value: str, ignoreCase: bool, throwOnFailure: bool, result: ref[System.Object], ) -> bool:
        ...

    @staticmethod
    @typing.overload
    def TryParse(enumType: System.Type, value: System.ReadOnlySpan[str], ignoreCase: bool, throwOnFailure: bool, result: ref[System.Object], ) -> bool:
        ...

    @staticmethod
    @typing.overload
    def TryParse(value: str, result: ref[TEnum], ) -> bool:
        ...

    @staticmethod
    @typing.overload
    def TryParse(value: System.ReadOnlySpan[str], result: ref[TEnum], ) -> bool:
        ...

    @staticmethod
    @typing.overload
    def TryParse(value: str, ignoreCase: bool, result: ref[TEnum], ) -> bool:
        ...

    @staticmethod
    @typing.overload
    def TryParse(value: System.ReadOnlySpan[str], ignoreCase: bool, result: ref[TEnum], ) -> bool:
        ...

    @staticmethod
    @typing.overload
    def TryParse(value: str, ignoreCase: bool, throwOnFailure: bool, result: ref[TEnum], ) -> bool:
        ...

    @staticmethod
    @typing.overload
    def TryParse(value: System.ReadOnlySpan[str], ignoreCase: bool, throwOnFailure: bool, result: ref[TEnum], ) -> bool:
        ...

    @staticmethod
    def TryParseInt32Enum(enumType: System.RuntimeType, value: System.ReadOnlySpan[str], minInclusive: int, maxInclusive: int, ignoreCase: bool, throwOnFailure: bool, type: int, result: ref[int], ) -> bool:
        ...

    @staticmethod
    def TryParseUInt32Enum(enumType: System.RuntimeType, value: System.ReadOnlySpan[str], maxInclusive: int, ignoreCase: bool, throwOnFailure: bool, type: int, result: ref[int], ) -> bool:
        ...

    @staticmethod
    def TryParseInt64Enum(enumType: System.RuntimeType, value: System.ReadOnlySpan[str], ignoreCase: bool, throwOnFailure: bool, result: ref[int], ) -> bool:
        ...

    @staticmethod
    def TryParseUInt64Enum(enumType: System.RuntimeType, value: System.ReadOnlySpan[str], ignoreCase: bool, throwOnFailure: bool, result: ref[int], ) -> bool:
        ...

    @staticmethod
    def TryParseRareEnum(enumType: System.RuntimeType, value: System.ReadOnlySpan[str], ignoreCase: bool, throwOnFailure: bool, result: ref[System.Object], ) -> bool:
        ...

    @staticmethod
    def TryParseByName(enumType: System.RuntimeType, value: System.ReadOnlySpan[str], ignoreCase: bool, throwOnFailure: bool, result: ref[int], ) -> bool:
        ...

    @staticmethod
    def StartsNumber(c: str, ) -> bool:
        ...

    @staticmethod
    def Format(enumType: System.Type, value: System.Object, format: str, ) -> str:
        ...

    def GetValue(self, ) -> System.Object:
        ...

    def GetHashCode(self, ) -> int:
        ...

    @typing.overload
    def ToString(self, ) -> str:
        ...

    @typing.overload
    def ToString(self, format: str, provider: System.IFormatProvider, ) -> str:
        ...

    @typing.overload
    def ToString(self, format: str, ) -> str:
        ...

    @typing.overload
    def ToString(self, provider: System.IFormatProvider, ) -> str:
        ...

    def CompareTo(self, target: System.Object, ) -> int:
        ...

    def GetTypeCode(self, ) -> int:
        ...

    def ToBoolean(self, provider: System.IFormatProvider, ) -> bool:
        ...

    def ToChar(self, provider: System.IFormatProvider, ) -> str:
        ...

    def ToSByte(self, provider: System.IFormatProvider, ) -> int:
        ...

    def ToByte(self, provider: System.IFormatProvider, ) -> int:
        ...

    def ToInt16(self, provider: System.IFormatProvider, ) -> int:
        ...

    def ToUInt16(self, provider: System.IFormatProvider, ) -> int:
        ...

class ResolveEventHandler(System.ICloneable, System.Runtime.Serialization.ISerializable, System.MulticastDelegate):
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

    def Invoke(self, sender: System.Object, args: System.ResolveEventArgs, ) -> System.Reflection.Assembly:
        ...

    def BeginInvoke(self, sender: System.Object, args: System.ResolveEventArgs, callback: System.AsyncCallback, object: System.Object, ) -> System.IAsyncResult:
        ...

    def EndInvoke(self, result: System.IAsyncResult, ) -> System.Reflection.Assembly:
        ...

class DateTimeKind(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    Unspecified: int = ...
    Utc: int = ...
    Local: int = ...

class ISignedNumber(System.INumber[TSelf], System.IAdditionOperators[TSelf, TSelf, TSelf], System.IAdditiveIdentity[TSelf, TSelf], System.IComparisonOperators[TSelf, TSelf], System.IComparable, System.IComparable[TSelf], System.IEqualityOperators[TSelf, TSelf], System.IEquatable[TSelf], System.IDecrementOperators[TSelf], System.IDivisionOperators[TSelf, TSelf, TSelf], System.IIncrementOperators[TSelf], System.IModulusOperators[TSelf, TSelf, TSelf], System.IMultiplicativeIdentity[TSelf, TSelf], System.IMultiplyOperators[TSelf, TSelf, TSelf], System.ISpanFormattable, System.IFormattable, System.ISpanParseable[TSelf], System.IParseable[TSelf], System.ISubtractionOperators[TSelf, TSelf, TSelf], System.IUnaryNegationOperators[TSelf, TSelf], System.IUnaryPlusOperators[TSelf, TSelf], abc.ABC, typing.Generic[TSelf]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    @abc.abstractmethod
    def NegativeOne(self) -> TSelf:
        ...

    # methods
class Array(System.ICloneable, System.Collections.IList, System.Collections.ICollection, System.Collections.IEnumerable, System.Collections.IStructuralComparable, System.Collections.IStructuralEquatable, System.Object, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def Length(self) -> int:
        ...

    @property
    def NativeLength(self) -> System.UIntPtr:
        ...

    @property
    def LongLength(self) -> int:
        ...

    @property
    def Rank(self) -> int:
        ...

    @property
    def Count(self) -> int:
        ...

    @property
    def SyncRoot(self) -> System.Object:
        ...

    @property
    def IsReadOnly(self) -> bool:
        ...

    @property
    def IsFixedSize(self) -> bool:
        ...

    @property
    def IsSynchronized(self) -> bool:
        ...

    @property
    def Item(self) -> System.Object:
        ...
    @Item.setter
    def Item(self, val: System.Object):
        ...

    @property
    def MaxLength(self) -> int:
        ...

    # methods
    def __init__(self, ):
        ...

    @typing.overload
    def CopyTo(self, array: System.Array, index: int, ) -> None:
        ...

    @typing.overload
    def CopyTo(self, array: System.Array, index: int, ) -> None:
        ...

    @staticmethod
    def Empty() -> System.Array[T]:
        ...

    @staticmethod
    def Exists(array: System.Array[T], match: System.Predicate[T], ) -> bool:
        ...

    @staticmethod
    @typing.overload
    def Fill(array: System.Array[T], value: T, ) -> None:
        ...

    @staticmethod
    @typing.overload
    def Fill(array: System.Array[T], value: T, startIndex: int, count: int, ) -> None:
        ...

    @staticmethod
    def Find(array: System.Array[T], match: System.Predicate[T], ) -> T:
        ...

    @staticmethod
    def FindAll(array: System.Array[T], match: System.Predicate[T], ) -> System.Array[T]:
        ...

    @staticmethod
    @typing.overload
    def FindIndex(array: System.Array[T], match: System.Predicate[T], ) -> int:
        ...

    @staticmethod
    @typing.overload
    def FindIndex(array: System.Array[T], startIndex: int, match: System.Predicate[T], ) -> int:
        ...

    @staticmethod
    @typing.overload
    def FindIndex(array: System.Array[T], startIndex: int, count: int, match: System.Predicate[T], ) -> int:
        ...

    @staticmethod
    def FindLast(array: System.Array[T], match: System.Predicate[T], ) -> T:
        ...

    @staticmethod
    @typing.overload
    def FindLastIndex(array: System.Array[T], match: System.Predicate[T], ) -> int:
        ...

    @staticmethod
    @typing.overload
    def FindLastIndex(array: System.Array[T], startIndex: int, match: System.Predicate[T], ) -> int:
        ...

    @staticmethod
    @typing.overload
    def FindLastIndex(array: System.Array[T], startIndex: int, count: int, match: System.Predicate[T], ) -> int:
        ...

    @staticmethod
    def ForEach(array: System.Array[T], action: System.Action[T], ) -> None:
        ...

    @staticmethod
    @typing.overload
    def IndexOf(array: System.Array, value: System.Object, ) -> int:
        ...

    @staticmethod
    @typing.overload
    def IndexOf(array: System.Array, value: System.Object, startIndex: int, ) -> int:
        ...

    @staticmethod
    @typing.overload
    def IndexOf(array: System.Array, value: System.Object, startIndex: int, count: int, ) -> int:
        ...

    @staticmethod
    @typing.overload
    def IndexOf(array: System.Array[T], value: T, ) -> int:
        ...

    @staticmethod
    @typing.overload
    def IndexOf(array: System.Array[T], value: T, startIndex: int, ) -> int:
        ...

    @staticmethod
    @typing.overload
    def IndexOf(array: System.Array[T], value: T, startIndex: int, count: int, ) -> int:
        ...

    @staticmethod
    @typing.overload
    def LastIndexOf(array: System.Array, value: System.Object, ) -> int:
        ...

    @staticmethod
    @typing.overload
    def LastIndexOf(array: System.Array, value: System.Object, startIndex: int, ) -> int:
        ...

    @staticmethod
    @typing.overload
    def LastIndexOf(array: System.Array, value: System.Object, startIndex: int, count: int, ) -> int:
        ...

    @staticmethod
    @typing.overload
    def LastIndexOf(array: System.Array[T], value: T, ) -> int:
        ...

    @staticmethod
    @typing.overload
    def LastIndexOf(array: System.Array[T], value: T, startIndex: int, ) -> int:
        ...

    @staticmethod
    @typing.overload
    def LastIndexOf(array: System.Array[T], value: T, startIndex: int, count: int, ) -> int:
        ...

    @staticmethod
    @typing.overload
    def Reverse(array: System.Array, ) -> None:
        ...

    @staticmethod
    @typing.overload
    def Reverse(array: System.Array, index: int, length: int, ) -> None:
        ...

    @staticmethod
    @typing.overload
    def Reverse(array: System.Array[T], ) -> None:
        ...

    @staticmethod
    @typing.overload
    def Reverse(array: System.Array[T], index: int, length: int, ) -> None:
        ...

    @staticmethod
    @typing.overload
    def Sort(array: System.Array, ) -> None:
        ...

    @staticmethod
    @typing.overload
    def Sort(keys: System.Array, items: System.Array, ) -> None:
        ...

    @staticmethod
    @typing.overload
    def Sort(array: System.Array, index: int, length: int, ) -> None:
        ...

    @staticmethod
    @typing.overload
    def Sort(keys: System.Array, items: System.Array, index: int, length: int, ) -> None:
        ...

    @staticmethod
    @typing.overload
    def Sort(array: System.Array, comparer: System.Collections.IComparer, ) -> None:
        ...

    @staticmethod
    @typing.overload
    def Sort(keys: System.Array, items: System.Array, comparer: System.Collections.IComparer, ) -> None:
        ...

    @staticmethod
    @typing.overload
    def Sort(array: System.Array, index: int, length: int, comparer: System.Collections.IComparer, ) -> None:
        ...

    @staticmethod
    @typing.overload
    def Sort(keys: System.Array, items: System.Array, index: int, length: int, comparer: System.Collections.IComparer, ) -> None:
        ...

    @staticmethod
    @typing.overload
    def Sort(array: System.Array[T], ) -> None:
        ...

    @staticmethod
    @typing.overload
    def Sort(keys: System.Array[TKey], items: System.Array[TValue], ) -> None:
        ...

    @staticmethod
    @typing.overload
    def Sort(array: System.Array[T], index: int, length: int, ) -> None:
        ...

    @staticmethod
    @typing.overload
    def Sort(keys: System.Array[TKey], items: System.Array[TValue], index: int, length: int, ) -> None:
        ...

    @staticmethod
    @typing.overload
    def Sort(array: System.Array[T], comparer: System.Collections.Generic.IComparer[T], ) -> None:
        ...

    @staticmethod
    @typing.overload
    def Sort(keys: System.Array[TKey], items: System.Array[TValue], comparer: System.Collections.Generic.IComparer[TKey], ) -> None:
        ...

    @staticmethod
    @typing.overload
    def Sort(array: System.Array[T], index: int, length: int, comparer: System.Collections.Generic.IComparer[T], ) -> None:
        ...

    @staticmethod
    @typing.overload
    def Sort(keys: System.Array[TKey], items: System.Array[TValue], index: int, length: int, comparer: System.Collections.Generic.IComparer[TKey], ) -> None:
        ...

    @staticmethod
    @typing.overload
    def Sort(array: System.Array[T], comparison: System.Comparison[T], ) -> None:
        ...

    @staticmethod
    def TrueForAll(array: System.Array[T], match: System.Predicate[T], ) -> bool:
        ...

    @staticmethod
    def UnsafeArrayAsSpan(array: System.Array, adjustedIndex: int, length: int, ) -> System.Span[T]:
        ...

    def GetEnumerator(self, ) -> System.Collections.IEnumerator:
        ...

    @staticmethod
    @typing.overload
    def CreateInstance(elementType: System.Type, length: int, ) -> System.Array:
        ...

    @staticmethod
    @typing.overload
    def CreateInstance(elementType: System.Type, length1: int, length2: int, ) -> System.Array:
        ...

    @staticmethod
    @typing.overload
    def CreateInstance(elementType: System.Type, length1: int, length2: int, length3: int, ) -> System.Array:
        ...

    @staticmethod
    @typing.overload
    def CreateInstance(elementType: System.Type, lengths: System.Array[int], ) -> System.Array:
        ...

    @staticmethod
    @typing.overload
    def CreateInstance(elementType: System.Type, lengths: System.Array[int], lowerBounds: System.Array[int], ) -> System.Array:
        ...

    @staticmethod
    @typing.overload
    def CreateInstance(elementType: System.Type, lengths: System.Array[int], ) -> System.Array:
        ...

    @staticmethod
    def InternalCreate(elementType: ptr[None], rank: int, pLengths: ptr[int], pLowerBounds: ptr[int], ) -> System.Array:
        ...

    @staticmethod
    @typing.overload
    def Copy(sourceArray: System.Array, destinationArray: System.Array, length: int, ) -> None:
        ...

    @staticmethod
    @typing.overload
    def Copy(sourceArray: System.Array, sourceIndex: int, destinationArray: System.Array, destinationIndex: int, length: int, ) -> None:
        ...

    @staticmethod
    @typing.overload
    def Copy(sourceArray: System.Array, sourceIndex: int, destinationArray: System.Array, destinationIndex: int, length: int, reliable: bool, ) -> None:
        ...

    @staticmethod
    @typing.overload
    def Copy(sourceArray: System.Array, destinationArray: System.Array, length: int, ) -> None:
        ...

    @staticmethod
    @typing.overload
    def Copy(sourceArray: System.Array, sourceIndex: int, destinationArray: System.Array, destinationIndex: int, length: int, ) -> None:
        ...

    @staticmethod
    def IsSimpleCopy(sourceArray: System.Array, destinationArray: System.Array, ) -> bool:
        ...

    @staticmethod
    def CopySlow(sourceArray: System.Array, sourceIndex: int, destinationArray: System.Array, destinationIndex: int, length: int, ) -> None:
        ...

    @staticmethod
    def ConstrainedCopy(sourceArray: System.Array, sourceIndex: int, destinationArray: System.Array, destinationIndex: int, length: int, ) -> None:
        ...

    @staticmethod
    @typing.overload
    def Clear(array: System.Array, ) -> None:
        ...

    @staticmethod
    @typing.overload
    def Clear(array: System.Array, index: int, length: int, ) -> None:
        ...

    def GetFlattenedIndex(self, indices: System.ReadOnlySpan[int], ) -> System.IntPtr:
        ...

    def InternalGetValue(self, flattenedIndex: System.IntPtr, ) -> System.Object:
        ...

    def InternalSetValue(self, value: System.Object, flattenedIndex: System.IntPtr, ) -> None:
        ...

    def GetLength(self, dimension: int, ) -> int:
        ...

    def GetUpperBound(self, dimension: int, ) -> int:
        ...

    def GetLowerBound(self, dimension: int, ) -> int:
        ...

    def GetCorElementTypeOfElementType(self, ) -> int:
        ...

    def IsValueOfElementType(self, value: System.Object, ) -> bool:
        ...

    def Initialize(self, ) -> None:
        ...

    @staticmethod
    def AsReadOnly(array: System.Array[T], ) -> System.Collections.ObjectModel.ReadOnlyCollection[T]:
        ...

    @staticmethod
    def Resize(array: ref[System.Array[T]], newSize: int, ) -> None:
        ...

    @typing.overload
    def GetValue(self, indices: System.Array[int], ) -> System.Object:
        ...

    @typing.overload
    def GetValue(self, index: int, ) -> System.Object:
        ...

    @typing.overload
    def GetValue(self, index1: int, index2: int, ) -> System.Object:
        ...

    @typing.overload
    def GetValue(self, index1: int, index2: int, index3: int, ) -> System.Object:
        ...

    @typing.overload
    def GetValue(self, index: int, ) -> System.Object:
        ...

    @typing.overload
    def GetValue(self, index1: int, index2: int, ) -> System.Object:
        ...

    @typing.overload
    def GetValue(self, index1: int, index2: int, index3: int, ) -> System.Object:
        ...

    @typing.overload
    def GetValue(self, indices: System.Array[int], ) -> System.Object:
        ...

    @typing.overload
    def SetValue(self, value: System.Object, index: int, ) -> None:
        ...

    @typing.overload
    def SetValue(self, value: System.Object, index1: int, index2: int, ) -> None:
        ...

    @typing.overload
    def SetValue(self, value: System.Object, index1: int, index2: int, index3: int, ) -> None:
        ...

    @typing.overload
    def SetValue(self, value: System.Object, indices: System.Array[int], ) -> None:
        ...

    @typing.overload
    def SetValue(self, value: System.Object, index: int, ) -> None:
        ...

    @typing.overload
    def SetValue(self, value: System.Object, index1: int, index2: int, ) -> None:
        ...

    @typing.overload
    def SetValue(self, value: System.Object, index1: int, index2: int, index3: int, ) -> None:
        ...

    @typing.overload
    def SetValue(self, value: System.Object, indices: System.Array[int], ) -> None:
        ...

    @staticmethod
    def GetMedian(low: int, hi: int, ) -> int:
        ...

    def GetLongLength(self, dimension: int, ) -> int:
        ...

    def Add(self, value: System.Object, ) -> int:
        ...

    def Contains(self, value: System.Object, ) -> bool:
        ...

    def Clear(self, ) -> None:
        ...

    def IndexOf(self, value: System.Object, ) -> int:
        ...

    def Insert(self, index: int, value: System.Object, ) -> None:
        ...

    def Remove(self, value: System.Object, ) -> None:
        ...

    def RemoveAt(self, index: int, ) -> None:
        ...

    def Clone(self, ) -> System.Object:
        ...

    def CompareTo(self, other: System.Object, comparer: System.Collections.IComparer, ) -> int:
        ...

    def Equals(self, other: System.Object, comparer: System.Collections.IEqualityComparer, ) -> bool:
        ...

    def GetHashCode(self, comparer: System.Collections.IEqualityComparer, ) -> int:
        ...

    @staticmethod
    @typing.overload
    def BinarySearch(array: System.Array, value: System.Object, ) -> int:
        ...

    @staticmethod
    @typing.overload
    def BinarySearch(array: System.Array, index: int, length: int, value: System.Object, ) -> int:
        ...

    @staticmethod
    @typing.overload
    def BinarySearch(array: System.Array, value: System.Object, comparer: System.Collections.IComparer, ) -> int:
        ...

    @staticmethod
    @typing.overload
    def BinarySearch(array: System.Array, index: int, length: int, value: System.Object, comparer: System.Collections.IComparer, ) -> int:
        ...

    @staticmethod
    @typing.overload
    def BinarySearch(array: System.Array[T], value: T, ) -> int:
        ...

    @staticmethod
    @typing.overload
    def BinarySearch(array: System.Array[T], value: T, comparer: System.Collections.Generic.IComparer[T], ) -> int:
        ...

    @staticmethod
    @typing.overload
    def BinarySearch(array: System.Array[T], index: int, length: int, value: T, ) -> int:
        ...

    @staticmethod
    @typing.overload
    def BinarySearch(array: System.Array[T], index: int, length: int, value: T, comparer: System.Collections.Generic.IComparer[T], ) -> int:
        ...

    @staticmethod
    def ConvertAll(array: System.Array[TInput], converter: System.Converter[TInput, TOutput], ) -> System.Array[TOutput]:
        ...

Char = str

Double = float

class Func(System.ICloneable, System.Runtime.Serialization.ISerializable, System.MulticastDelegate, typing.Generic[T1, T2, T3, T4, T5, T6, T7, TResult]):
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

    def Invoke(self, arg1: T1, arg2: T2, arg3: T3, arg4: T4, arg5: T5, arg6: T6, arg7: T7, ) -> TResult:
        ...

    def BeginInvoke(self, arg1: T1, arg2: T2, arg3: T3, arg4: T4, arg5: T5, arg6: T6, arg7: T7, callback: System.AsyncCallback, object: System.Object, ) -> System.IAsyncResult:
        ...

    def EndInvoke(self, result: System.IAsyncResult, ) -> TResult:
        ...

class IEquatable(abc.ABC, typing.Generic[T]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    @abc.abstractmethod
    def Equals(self, other: T, ) -> bool:
        ...

class Func(System.ICloneable, System.Runtime.Serialization.ISerializable, System.MulticastDelegate, typing.Generic[T1, T2, T3, T4, T5, T6, T7, T8, TResult]):
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

    def Invoke(self, arg1: T1, arg2: T2, arg3: T3, arg4: T4, arg5: T5, arg6: T6, arg7: T7, arg8: T8, ) -> TResult:
        ...

    def BeginInvoke(self, arg1: T1, arg2: T2, arg3: T3, arg4: T4, arg5: T5, arg6: T6, arg7: T7, arg8: T8, callback: System.AsyncCallback, object: System.Object, ) -> System.IAsyncResult:
        ...

    def EndInvoke(self, result: System.IAsyncResult, ) -> TResult:
        ...

class Func(System.ICloneable, System.Runtime.Serialization.ISerializable, System.MulticastDelegate, typing.Generic[T1, T2, T3, T4, T5, T6, T7, T8, T9, TResult]):
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

    def Invoke(self, arg1: T1, arg2: T2, arg3: T3, arg4: T4, arg5: T5, arg6: T6, arg7: T7, arg8: T8, arg9: T9, ) -> TResult:
        ...

    def BeginInvoke(self, arg1: T1, arg2: T2, arg3: T3, arg4: T4, arg5: T5, arg6: T6, arg7: T7, arg8: T8, arg9: T9, callback: System.AsyncCallback, object: System.Object, ) -> System.IAsyncResult:
        ...

    def EndInvoke(self, result: System.IAsyncResult, ) -> TResult:
        ...

class StringComparer(System.Collections.IComparer, System.Collections.IEqualityComparer, System.Collections.Generic.IComparer[str], System.Collections.Generic.IEqualityComparer[str], System.Object, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def InvariantCulture(self) -> System.StringComparer:
        ...

    @property
    def InvariantCultureIgnoreCase(self) -> System.StringComparer:
        ...

    @property
    def CurrentCulture(self) -> System.StringComparer:
        ...

    @property
    def CurrentCultureIgnoreCase(self) -> System.StringComparer:
        ...

    @property
    def Ordinal(self) -> System.StringComparer:
        ...

    @property
    def OrdinalIgnoreCase(self) -> System.StringComparer:
        ...

    # methods
    def __init__(self, ):
        ...

    @staticmethod
    def FromComparison(comparisonType: int, ) -> System.StringComparer:
        ...

    @staticmethod
    @typing.overload
    def Create(culture: System.Globalization.CultureInfo, ignoreCase: bool, ) -> System.StringComparer:
        ...

    @staticmethod
    @typing.overload
    def Create(culture: System.Globalization.CultureInfo, options: int, ) -> System.StringComparer:
        ...

    @staticmethod
    def IsWellKnownOrdinalComparer(comparer: System.Collections.Generic.IEqualityComparer[str], ignoreCase: ref[bool], ) -> bool:
        ...

    def IsWellKnownOrdinalComparerCore(self, ignoreCase: ref[bool], ) -> bool:
        ...

    @staticmethod
    def IsWellKnownCultureAwareComparer(comparer: System.Collections.Generic.IEqualityComparer[str], compareInfo: ref[System.Globalization.CompareInfo], compareOptions: ref[int], ) -> bool:
        ...

    def IsWellKnownCultureAwareComparerCore(self, compareInfo: ref[System.Globalization.CompareInfo], compareOptions: ref[int], ) -> bool:
        ...

    @typing.overload
    def Compare(self, x: System.Object, y: System.Object, ) -> int:
        ...

    @abc.abstractmethod
    @typing.overload
    def Compare(self, x: str, y: str, ) -> int:
        ...

    @typing.overload
    def Equals(self, x: System.Object, y: System.Object, ) -> bool:
        ...

    @abc.abstractmethod
    @typing.overload
    def Equals(self, x: str, y: str, ) -> bool:
        ...

    @typing.overload
    def GetHashCode(self, obj: System.Object, ) -> int:
        ...

    @abc.abstractmethod
    @typing.overload
    def GetHashCode(self, obj: str, ) -> int:
        ...

class IMinMaxValue(abc.ABC, typing.Generic[TSelf]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    @abc.abstractmethod
    def MinValue(self) -> TSelf:
        ...

    @property
    @abc.abstractmethod
    def MaxValue(self) -> TSelf:
        ...

    # methods
class ISpanParseable(System.IParseable[TSelf], abc.ABC, typing.Generic[TSelf]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    @staticmethod
    @abc.abstractmethod
    def Parse(s: System.ReadOnlySpan[str], provider: System.IFormatProvider, ) -> TSelf:
        ...

    @staticmethod
    @abc.abstractmethod
    def TryParse(s: System.ReadOnlySpan[str], provider: System.IFormatProvider, result: ref[TSelf], ) -> bool:
        ...

class IDecrementOperators(abc.ABC, typing.Generic[TSelf]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
class Func(System.ICloneable, System.Runtime.Serialization.ISerializable, System.MulticastDelegate, typing.Generic[TResult]):
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

    def Invoke(self, ) -> TResult:
        ...

    def BeginInvoke(self, callback: System.AsyncCallback, object: System.Object, ) -> System.IAsyncResult:
        ...

    def EndInvoke(self, result: System.IAsyncResult, ) -> TResult:
        ...

class IComparable(abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    @abc.abstractmethod
    def CompareTo(self, obj: System.Object, ) -> int:
        ...

class Memory(System.IEquatable[System.Memory], System.ValueType, typing.Generic[T]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def Empty(self) -> System.Memory:
        ...

    @property
    def Length(self) -> int:
        ...

    @property
    def IsEmpty(self) -> bool:
        ...

    @property
    def Span(self) -> System.Span[T]:
        ...

    # methods
    @typing.overload
    def __init__(self, array: System.Array[T], ):
        ...

    @typing.overload
    def __init__(self, array: System.Array[T], start: int, ):
        ...

    @typing.overload
    def __init__(self, array: System.Array[T], start: int, length: int, ):
        ...

    @typing.overload
    def __init__(self, manager: System.Buffers.MemoryManager[T], length: int, ):
        ...

    @typing.overload
    def __init__(self, manager: System.Buffers.MemoryManager[T], start: int, length: int, ):
        ...

    @typing.overload
    def __init__(self, obj: System.Object, start: int, length: int, ):
        ...

    def ToString(self, ) -> str:
        ...

    @typing.overload
    def Slice(self, start: int, ) -> System.Memory:
        ...

    @typing.overload
    def Slice(self, start: int, length: int, ) -> System.Memory:
        ...

    def CopyTo(self, destination: System.Memory, ) -> None:
        ...

    def TryCopyTo(self, destination: System.Memory, ) -> bool:
        ...

    def Pin(self, ) -> System.Buffers.MemoryHandle:
        ...

    def ToArray(self, ) -> System.Array[T]:
        ...

    @typing.overload
    def Equals(self, obj: System.Object, ) -> bool:
        ...

    @typing.overload
    def Equals(self, other: System.Memory, ) -> bool:
        ...

    def GetHashCode(self, ) -> int:
        ...

class ModuleHandle(System.ValueType):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields
    EmptyHandle: System.ModuleHandle = ...

    # properties
    @property
    def MDStreamVersion(self) -> int:
        ...

    # methods
    def __init__(self, module: System.Reflection.RuntimeModule, ):
        ...

    def GetRuntimeModule(self, ) -> System.Reflection.RuntimeModule:
        ...

    def GetHashCode(self, ) -> int:
        ...

    @typing.overload
    def Equals(self, obj: System.Object, ) -> bool:
        ...

    @typing.overload
    def Equals(self, handle: System.ModuleHandle, ) -> bool:
        ...

    @staticmethod
    def GetDynamicMethod(method: System.Reflection.Emit.DynamicMethod, module: System.Reflection.RuntimeModule, name: str, sig: System.Array[int], resolver: System.Resolver, ) -> System.IRuntimeMethodInfo:
        ...

    @staticmethod
    def GetToken(module: System.Reflection.RuntimeModule, ) -> int:
        ...

    @staticmethod
    def ValidateModulePointer(module: System.Reflection.RuntimeModule, ) -> None:
        ...

    def GetRuntimeTypeHandleFromMetadataToken(self, typeToken: int, ) -> System.RuntimeTypeHandle:
        ...

    @typing.overload
    def ResolveTypeHandle(self, typeToken: int, ) -> System.RuntimeTypeHandle:
        ...

    @typing.overload
    def ResolveTypeHandle(self, typeToken: int, typeInstantiationContext: System.Array[System.RuntimeTypeHandle], methodInstantiationContext: System.Array[System.RuntimeTypeHandle], ) -> System.RuntimeTypeHandle:
        ...

    @staticmethod
    def ResolveType(module: System.Runtime.CompilerServices.QCallModule, typeToken: int, typeInstArgs: ptr[System.IntPtr], typeInstCount: int, methodInstArgs: ptr[System.IntPtr], methodInstCount: int, type: System.Runtime.CompilerServices.ObjectHandleOnStack, ) -> None:
        ...

    def GetRuntimeMethodHandleFromMetadataToken(self, methodToken: int, ) -> System.RuntimeMethodHandle:
        ...

    @typing.overload
    def ResolveMethodHandle(self, methodToken: int, ) -> System.RuntimeMethodHandle:
        ...

    @typing.overload
    def ResolveMethodHandle(self, methodToken: int, typeInstantiationContext: System.Array[System.RuntimeTypeHandle], methodInstantiationContext: System.Array[System.RuntimeTypeHandle], ) -> System.RuntimeMethodHandle:
        ...

    @staticmethod
    def ResolveMethodHandleInternal(module: System.Reflection.RuntimeModule, methodToken: int, typeInstantiationContext: System.Array[System.IntPtr], typeInstCount: int, methodInstantiationContext: System.Array[System.IntPtr], methodInstCount: int, ) -> System.RuntimeMethodHandleInternal:
        ...

    @staticmethod
    def ResolveMethod(module: System.Runtime.CompilerServices.QCallModule, methodToken: int, typeInstArgs: ptr[System.IntPtr], typeInstCount: int, methodInstArgs: ptr[System.IntPtr], methodInstCount: int, ) -> System.RuntimeMethodHandleInternal:
        ...

    def GetRuntimeFieldHandleFromMetadataToken(self, fieldToken: int, ) -> System.RuntimeFieldHandle:
        ...

    @typing.overload
    def ResolveFieldHandle(self, fieldToken: int, ) -> System.RuntimeFieldHandle:
        ...

    @typing.overload
    def ResolveFieldHandle(self, fieldToken: int, typeInstantiationContext: System.Array[System.RuntimeTypeHandle], methodInstantiationContext: System.Array[System.RuntimeTypeHandle], ) -> System.RuntimeFieldHandle:
        ...

    @staticmethod
    def ResolveField(module: System.Runtime.CompilerServices.QCallModule, fieldToken: int, typeInstArgs: ptr[System.IntPtr], typeInstCount: int, methodInstArgs: ptr[System.IntPtr], methodInstCount: int, retField: System.Runtime.CompilerServices.ObjectHandleOnStack, ) -> None:
        ...

    @staticmethod
    def _ContainsPropertyMatchingHash(module: System.Runtime.CompilerServices.QCallModule, propertyToken: int, hash: int, ) -> int:
        ...

    @staticmethod
    def ContainsPropertyMatchingHash(module: System.Reflection.RuntimeModule, propertyToken: int, hash: int, ) -> bool:
        ...

    @staticmethod
    @typing.overload
    def GetModuleType(handle: System.Runtime.CompilerServices.QCallModule, type: System.Runtime.CompilerServices.ObjectHandleOnStack, ) -> None:
        ...

    @staticmethod
    @typing.overload
    def GetModuleType(module: System.Reflection.RuntimeModule, ) -> System.RuntimeType:
        ...

    @staticmethod
    @typing.overload
    def GetPEKind(handle: System.Runtime.CompilerServices.QCallModule, peKind: ptr[int], machine: ptr[int], ) -> None:
        ...

    @staticmethod
    @typing.overload
    def GetPEKind(module: System.Reflection.RuntimeModule, peKind: ref[int], machine: ref[int], ) -> None:
        ...

    @staticmethod
    def GetMDStreamVersion(module: System.Reflection.RuntimeModule, ) -> int:
        ...

    @staticmethod
    def _GetMetadataImport(module: System.Reflection.RuntimeModule, ) -> System.IntPtr:
        ...

    @staticmethod
    def GetMetadataImport(module: System.Reflection.RuntimeModule, ) -> System.Reflection.MetadataImport:
        ...

class Half(System.IComparable, System.ISpanFormattable, System.IFormattable, System.IComparable[System.Half], System.IEquatable[System.Half], System.IBinaryFloatingPoint[System.Half], System.IBinaryNumber[System.Half], System.IBitwiseOperators[System.Half, System.Half, System.Half], System.INumber[System.Half], System.IAdditionOperators[System.Half, System.Half, System.Half], System.IAdditiveIdentity[System.Half, System.Half], System.IComparisonOperators[System.Half, System.Half], System.IEqualityOperators[System.Half, System.Half], System.IDecrementOperators[System.Half], System.IDivisionOperators[System.Half, System.Half, System.Half], System.IIncrementOperators[System.Half], System.IModulusOperators[System.Half, System.Half, System.Half], System.IMultiplicativeIdentity[System.Half, System.Half], System.IMultiplyOperators[System.Half, System.Half, System.Half], System.ISpanParseable[System.Half], System.IParseable[System.Half], System.ISubtractionOperators[System.Half, System.Half, System.Half], System.IUnaryNegationOperators[System.Half, System.Half], System.IUnaryPlusOperators[System.Half, System.Half], System.IFloatingPoint[System.Half], System.ISignedNumber[System.Half], System.IMinMaxValue[System.Half], System.ValueType):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def Epsilon(self) -> System.Half:
        ...

    @property
    def PositiveInfinity(self) -> System.Half:
        ...

    @property
    def NegativeInfinity(self) -> System.Half:
        ...

    @property
    def NaN(self) -> System.Half:
        ...

    @property
    def MinValue(self) -> System.Half:
        ...

    @property
    def MaxValue(self) -> System.Half:
        ...

    @property
    def Exponent(self) -> int:
        ...

    @property
    def Significand(self) -> int:
        ...

    @property
    def AdditiveIdentity(self) -> System.Half:
        ...

    @property
    def E(self) -> System.Half:
        ...

    @property
    def Epsilon(self) -> System.Half:
        ...

    @property
    def NaN(self) -> System.Half:
        ...

    @property
    def NegativeInfinity(self) -> System.Half:
        ...

    @property
    def NegativeZero(self) -> System.Half:
        ...

    @property
    def Pi(self) -> System.Half:
        ...

    @property
    def PositiveInfinity(self) -> System.Half:
        ...

    @property
    def Tau(self) -> System.Half:
        ...

    @property
    def MinValue(self) -> System.Half:
        ...

    @property
    def MaxValue(self) -> System.Half:
        ...

    @property
    def MultiplicativeIdentity(self) -> System.Half:
        ...

    @property
    def One(self) -> System.Half:
        ...

    @property
    def Zero(self) -> System.Half:
        ...

    @property
    def NegativeOne(self) -> System.Half:
        ...

    # methods
    @typing.overload
    def __init__(self, value: int, ):
        ...

    @typing.overload
    def __init__(self, sign: bool, exp: int, sig: int, ):
        ...

    @staticmethod
    def IsFinite(x: System.Half, ) -> bool:
        ...

    @staticmethod
    def IsInfinity(x: System.Half, ) -> bool:
        ...

    @staticmethod
    def IsNaN(x: System.Half, ) -> bool:
        ...

    @staticmethod
    def IsNegative(x: System.Half, ) -> bool:
        ...

    @staticmethod
    def IsNegativeInfinity(x: System.Half, ) -> bool:
        ...

    @staticmethod
    def IsNormal(x: System.Half, ) -> bool:
        ...

    @staticmethod
    def IsPositiveInfinity(x: System.Half, ) -> bool:
        ...

    @staticmethod
    def IsSubnormal(x: System.Half, ) -> bool:
        ...

    @staticmethod
    def op_Increment(value: System.Half, ) -> System.Half:
        ...

    @staticmethod
    def op_Modulus(left: System.Half, right: System.Half, ) -> System.Half:
        ...

    @staticmethod
    def op_Multiply(left: System.Half, right: System.Half, ) -> System.Half:
        ...

    @staticmethod
    def Abs(value: System.Half, ) -> System.Half:
        ...

    @staticmethod
    def Clamp(value: System.Half, min: System.Half, max: System.Half, ) -> System.Half:
        ...

    @staticmethod
    def Create(value: TOther, ) -> System.Half:
        ...

    @staticmethod
    def CreateSaturating(value: TOther, ) -> System.Half:
        ...

    @staticmethod
    def CreateTruncating(value: TOther, ) -> System.Half:
        ...

    @staticmethod
    def DivRem(left: System.Half, right: System.Half, ) -> System.ValueTuple[System.Half, System.Half]:
        ...

    @staticmethod
    def Max(x: System.Half, y: System.Half, ) -> System.Half:
        ...

    @staticmethod
    def Min(x: System.Half, y: System.Half, ) -> System.Half:
        ...

    @staticmethod
    @typing.overload
    def Parse(s: str, style: int, provider: System.IFormatProvider, ) -> System.Half:
        ...

    @staticmethod
    @typing.overload
    def Parse(s: System.ReadOnlySpan[str], style: int, provider: System.IFormatProvider, ) -> System.Half:
        ...

    @staticmethod
    def Sign(value: System.Half, ) -> System.Half:
        ...

    @staticmethod
    def TryCreate(value: TOther, result: ref[System.Half], ) -> bool:
        ...

    @staticmethod
    @typing.overload
    def TryParse(s: str, style: int, provider: System.IFormatProvider, result: ref[System.Half], ) -> bool:
        ...

    @staticmethod
    @typing.overload
    def TryParse(s: System.ReadOnlySpan[str], style: int, provider: System.IFormatProvider, result: ref[System.Half], ) -> bool:
        ...

    @staticmethod
    def Parse(s: str, provider: System.IFormatProvider, ) -> System.Half:
        ...

    @staticmethod
    def TryParse(s: str, provider: System.IFormatProvider, result: ref[System.Half], ) -> bool:
        ...

    @staticmethod
    def Parse(s: System.ReadOnlySpan[str], provider: System.IFormatProvider, ) -> System.Half:
        ...

    @staticmethod
    def TryParse(s: System.ReadOnlySpan[str], provider: System.IFormatProvider, result: ref[System.Half], ) -> bool:
        ...

    @staticmethod
    def op_Subtraction(left: System.Half, right: System.Half, ) -> System.Half:
        ...

    @staticmethod
    def op_UnaryNegation(value: System.Half, ) -> System.Half:
        ...

    @staticmethod
    def op_UnaryPlus(value: System.Half, ) -> System.Half:
        ...

    @staticmethod
    def op_Decrement(value: System.Half, ) -> System.Half:
        ...

    @staticmethod
    def op_Equality(left: System.Half, right: System.Half, ) -> bool:
        ...

    @staticmethod
    def op_Inequality(left: System.Half, right: System.Half, ) -> bool:
        ...

    @staticmethod
    def op_Division(left: System.Half, right: System.Half, ) -> System.Half:
        ...

    @staticmethod
    def Acos(x: System.Half, ) -> System.Half:
        ...

    @staticmethod
    def Acosh(x: System.Half, ) -> System.Half:
        ...

    @staticmethod
    def Asin(x: System.Half, ) -> System.Half:
        ...

    @staticmethod
    def Asinh(x: System.Half, ) -> System.Half:
        ...

    @staticmethod
    def Atan(x: System.Half, ) -> System.Half:
        ...

    @staticmethod
    def Atan2(y: System.Half, x: System.Half, ) -> System.Half:
        ...

    @staticmethod
    def Atanh(x: System.Half, ) -> System.Half:
        ...

    @staticmethod
    def BitIncrement(x: System.Half, ) -> System.Half:
        ...

    @staticmethod
    def BitDecrement(x: System.Half, ) -> System.Half:
        ...

    @staticmethod
    def Cbrt(x: System.Half, ) -> System.Half:
        ...

    @staticmethod
    def Ceiling(x: System.Half, ) -> System.Half:
        ...

    @staticmethod
    def CopySign(x: System.Half, y: System.Half, ) -> System.Half:
        ...

    @staticmethod
    def Cos(x: System.Half, ) -> System.Half:
        ...

    @staticmethod
    def Cosh(x: System.Half, ) -> System.Half:
        ...

    @staticmethod
    def Exp(x: System.Half, ) -> System.Half:
        ...

    @staticmethod
    def Floor(x: System.Half, ) -> System.Half:
        ...

    @staticmethod
    def FusedMultiplyAdd(left: System.Half, right: System.Half, addend: System.Half, ) -> System.Half:
        ...

    @staticmethod
    def IEEERemainder(left: System.Half, right: System.Half, ) -> System.Half:
        ...

    @staticmethod
    def ILogB(x: System.Half, ) -> TInteger:
        ...

    @staticmethod
    @typing.overload
    def Log(x: System.Half, ) -> System.Half:
        ...

    @staticmethod
    @typing.overload
    def Log(x: System.Half, newBase: System.Half, ) -> System.Half:
        ...

    @staticmethod
    def Log2(x: System.Half, ) -> System.Half:
        ...

    @staticmethod
    def Log10(x: System.Half, ) -> System.Half:
        ...

    @staticmethod
    def MaxMagnitude(x: System.Half, y: System.Half, ) -> System.Half:
        ...

    @staticmethod
    def MinMagnitude(x: System.Half, y: System.Half, ) -> System.Half:
        ...

    @staticmethod
    def Pow(x: System.Half, y: System.Half, ) -> System.Half:
        ...

    @staticmethod
    @typing.overload
    def Round(x: System.Half, ) -> System.Half:
        ...

    @staticmethod
    @typing.overload
    def Round(x: System.Half, digits: TInteger, ) -> System.Half:
        ...

    @staticmethod
    @typing.overload
    def Round(x: System.Half, mode: int, ) -> System.Half:
        ...

    @staticmethod
    @typing.overload
    def Round(x: System.Half, digits: TInteger, mode: int, ) -> System.Half:
        ...

    @staticmethod
    def ScaleB(x: System.Half, n: TInteger, ) -> System.Half:
        ...

    @staticmethod
    def Sin(x: System.Half, ) -> System.Half:
        ...

    @staticmethod
    def Sinh(x: System.Half, ) -> System.Half:
        ...

    @staticmethod
    def Sqrt(x: System.Half, ) -> System.Half:
        ...

    @staticmethod
    def Tan(x: System.Half, ) -> System.Half:
        ...

    @staticmethod
    def Tanh(x: System.Half, ) -> System.Half:
        ...

    @staticmethod
    def Truncate(x: System.Half, ) -> System.Half:
        ...

    @staticmethod
    def IsFinite(value: System.Half, ) -> bool:
        ...

    @staticmethod
    def IsInfinity(value: System.Half, ) -> bool:
        ...

    @staticmethod
    def IsNaN(value: System.Half, ) -> bool:
        ...

    @staticmethod
    def IsNegative(value: System.Half, ) -> bool:
        ...

    @staticmethod
    def IsNegativeInfinity(value: System.Half, ) -> bool:
        ...

    @staticmethod
    def IsNormal(value: System.Half, ) -> bool:
        ...

    @staticmethod
    def IsPositiveInfinity(value: System.Half, ) -> bool:
        ...

    @staticmethod
    def IsSubnormal(value: System.Half, ) -> bool:
        ...

    @staticmethod
    @typing.overload
    def Parse(s: str, ) -> System.Half:
        ...

    @staticmethod
    @typing.overload
    def Parse(s: str, style: int, ) -> System.Half:
        ...

    @staticmethod
    @typing.overload
    def Parse(s: str, provider: System.IFormatProvider, ) -> System.Half:
        ...

    @staticmethod
    @typing.overload
    def Parse(s: str, style: int = ..., provider: System.IFormatProvider = ..., ) -> System.Half:
        ...

    @staticmethod
    @typing.overload
    def Parse(s: System.ReadOnlySpan[str], style: int = ..., provider: System.IFormatProvider = ..., ) -> System.Half:
        ...

    @staticmethod
    @typing.overload
    def TryParse(s: str, result: ref[System.Half], ) -> bool:
        ...

    @staticmethod
    @typing.overload
    def TryParse(s: System.ReadOnlySpan[str], result: ref[System.Half], ) -> bool:
        ...

    @staticmethod
    @typing.overload
    def TryParse(s: str, style: int, provider: System.IFormatProvider, result: ref[System.Half], ) -> bool:
        ...

    @staticmethod
    @typing.overload
    def TryParse(s: System.ReadOnlySpan[str], style: int, provider: System.IFormatProvider, result: ref[System.Half], ) -> bool:
        ...

    @staticmethod
    def AreZero(left: System.Half, right: System.Half, ) -> bool:
        ...

    @staticmethod
    def IsNaNOrZero(value: System.Half, ) -> bool:
        ...

    @staticmethod
    def StripSign(value: System.Half, ) -> int:
        ...

    @typing.overload
    def CompareTo(self, obj: System.Object, ) -> int:
        ...

    @typing.overload
    def CompareTo(self, other: System.Half, ) -> int:
        ...

    @typing.overload
    def Equals(self, obj: System.Object, ) -> bool:
        ...

    @typing.overload
    def Equals(self, other: System.Half, ) -> bool:
        ...

    def GetHashCode(self, ) -> int:
        ...

    @typing.overload
    def ToString(self, ) -> str:
        ...

    @typing.overload
    def ToString(self, format: str, ) -> str:
        ...

    @typing.overload
    def ToString(self, provider: System.IFormatProvider, ) -> str:
        ...

    @typing.overload
    def ToString(self, format: str, provider: System.IFormatProvider, ) -> str:
        ...

    def TryFormat(self, destination: System.Span[str], charsWritten: ref[int], format: System.ReadOnlySpan[str] = ..., provider: System.IFormatProvider = ..., ) -> bool:
        ...

    @staticmethod
    def Negate(value: System.Half, ) -> System.Half:
        ...

    @staticmethod
    def NormSubnormalF16Sig(sig: int, ) -> System.ValueTuple[int, int]:
        ...

    @staticmethod
    def CreateHalfNaN(sign: bool, significand: int, ) -> System.Half:
        ...

    @staticmethod
    def RoundPackToHalf(sign: bool, exp: int, sig: int, ) -> int:
        ...

    @staticmethod
    @typing.overload
    def ShiftRightJam(i: int, dist: int, ) -> int:
        ...

    @staticmethod
    @typing.overload
    def ShiftRightJam(l: int, dist: int, ) -> int:
        ...

    @staticmethod
    def CreateSingleNaN(sign: bool, significand: int, ) -> float:
        ...

    @staticmethod
    def CreateDoubleNaN(sign: bool, significand: int, ) -> float:
        ...

    @staticmethod
    def CreateSingle(sign: bool, exp: int, sig: int, ) -> float:
        ...

    @staticmethod
    def CreateDouble(sign: bool, exp: int, sig: int, ) -> float:
        ...

    @staticmethod
    def op_Addition(left: System.Half, right: System.Half, ) -> System.Half:
        ...

    @staticmethod
    def IsPow2(value: System.Half, ) -> bool:
        ...

    @staticmethod
    def Log2(value: System.Half, ) -> System.Half:
        ...

    @staticmethod
    def op_BitwiseAnd(left: System.Half, right: System.Half, ) -> System.Half:
        ...

    @staticmethod
    def op_BitwiseOr(left: System.Half, right: System.Half, ) -> System.Half:
        ...

    @staticmethod
    def op_ExclusiveOr(left: System.Half, right: System.Half, ) -> System.Half:
        ...

    @staticmethod
    def op_OnesComplement(value: System.Half, ) -> System.Half:
        ...

    @staticmethod
    def op_LessThan(left: System.Half, right: System.Half, ) -> bool:
        ...

    @staticmethod
    def op_LessThanOrEqual(left: System.Half, right: System.Half, ) -> bool:
        ...

    @staticmethod
    def op_GreaterThan(left: System.Half, right: System.Half, ) -> bool:
        ...

    @staticmethod
    def op_GreaterThanOrEqual(left: System.Half, right: System.Half, ) -> bool:
        ...

class IFloatingPoint(System.ISignedNumber[TSelf], System.INumber[TSelf], System.IAdditionOperators[TSelf, TSelf, TSelf], System.IAdditiveIdentity[TSelf, TSelf], System.IComparisonOperators[TSelf, TSelf], System.IComparable, System.IComparable[TSelf], System.IEqualityOperators[TSelf, TSelf], System.IEquatable[TSelf], System.IDecrementOperators[TSelf], System.IDivisionOperators[TSelf, TSelf, TSelf], System.IIncrementOperators[TSelf], System.IModulusOperators[TSelf, TSelf, TSelf], System.IMultiplicativeIdentity[TSelf, TSelf], System.IMultiplyOperators[TSelf, TSelf, TSelf], System.ISpanFormattable, System.IFormattable, System.ISpanParseable[TSelf], System.IParseable[TSelf], System.ISubtractionOperators[TSelf, TSelf, TSelf], System.IUnaryNegationOperators[TSelf, TSelf], System.IUnaryPlusOperators[TSelf, TSelf], abc.ABC, typing.Generic[TSelf]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    @abc.abstractmethod
    def E(self) -> TSelf:
        ...

    @property
    @abc.abstractmethod
    def Epsilon(self) -> TSelf:
        ...

    @property
    @abc.abstractmethod
    def NaN(self) -> TSelf:
        ...

    @property
    @abc.abstractmethod
    def NegativeInfinity(self) -> TSelf:
        ...

    @property
    @abc.abstractmethod
    def NegativeZero(self) -> TSelf:
        ...

    @property
    @abc.abstractmethod
    def Pi(self) -> TSelf:
        ...

    @property
    @abc.abstractmethod
    def PositiveInfinity(self) -> TSelf:
        ...

    @property
    @abc.abstractmethod
    def Tau(self) -> TSelf:
        ...

    # methods
    @staticmethod
    @abc.abstractmethod
    def Acos(x: TSelf, ) -> TSelf:
        ...

    @staticmethod
    @abc.abstractmethod
    def Acosh(x: TSelf, ) -> TSelf:
        ...

    @staticmethod
    @abc.abstractmethod
    def Asin(x: TSelf, ) -> TSelf:
        ...

    @staticmethod
    @abc.abstractmethod
    def Asinh(x: TSelf, ) -> TSelf:
        ...

    @staticmethod
    @abc.abstractmethod
    def Atan(x: TSelf, ) -> TSelf:
        ...

    @staticmethod
    @abc.abstractmethod
    def Atan2(y: TSelf, x: TSelf, ) -> TSelf:
        ...

    @staticmethod
    @abc.abstractmethod
    def Atanh(x: TSelf, ) -> TSelf:
        ...

    @staticmethod
    @abc.abstractmethod
    def BitDecrement(x: TSelf, ) -> TSelf:
        ...

    @staticmethod
    @abc.abstractmethod
    def BitIncrement(x: TSelf, ) -> TSelf:
        ...

    @staticmethod
    @abc.abstractmethod
    def Cbrt(x: TSelf, ) -> TSelf:
        ...

    @staticmethod
    @abc.abstractmethod
    def Ceiling(x: TSelf, ) -> TSelf:
        ...

    @staticmethod
    @abc.abstractmethod
    def CopySign(x: TSelf, y: TSelf, ) -> TSelf:
        ...

    @staticmethod
    @abc.abstractmethod
    def Cos(x: TSelf, ) -> TSelf:
        ...

    @staticmethod
    @abc.abstractmethod
    def Cosh(x: TSelf, ) -> TSelf:
        ...

    @staticmethod
    @abc.abstractmethod
    def Exp(x: TSelf, ) -> TSelf:
        ...

    @staticmethod
    @abc.abstractmethod
    def Floor(x: TSelf, ) -> TSelf:
        ...

    @staticmethod
    @abc.abstractmethod
    def FusedMultiplyAdd(left: TSelf, right: TSelf, addend: TSelf, ) -> TSelf:
        ...

    @staticmethod
    @abc.abstractmethod
    def IEEERemainder(left: TSelf, right: TSelf, ) -> TSelf:
        ...

    @staticmethod
    @abc.abstractmethod
    def ILogB(x: TSelf, ) -> TInteger:
        ...

    @staticmethod
    @abc.abstractmethod
    def IsFinite(value: TSelf, ) -> bool:
        ...

    @staticmethod
    @abc.abstractmethod
    def IsInfinity(value: TSelf, ) -> bool:
        ...

    @staticmethod
    @abc.abstractmethod
    def IsNaN(value: TSelf, ) -> bool:
        ...

    @staticmethod
    @abc.abstractmethod
    def IsNegative(value: TSelf, ) -> bool:
        ...

    @staticmethod
    @abc.abstractmethod
    def IsNegativeInfinity(value: TSelf, ) -> bool:
        ...

    @staticmethod
    @abc.abstractmethod
    def IsNormal(value: TSelf, ) -> bool:
        ...

    @staticmethod
    @abc.abstractmethod
    def IsPositiveInfinity(value: TSelf, ) -> bool:
        ...

    @staticmethod
    @abc.abstractmethod
    def IsSubnormal(value: TSelf, ) -> bool:
        ...

    @staticmethod
    @abc.abstractmethod
    @typing.overload
    def Log(x: TSelf, ) -> TSelf:
        ...

    @staticmethod
    @abc.abstractmethod
    @typing.overload
    def Log(x: TSelf, newBase: TSelf, ) -> TSelf:
        ...

    @staticmethod
    @abc.abstractmethod
    def Log2(x: TSelf, ) -> TSelf:
        ...

    @staticmethod
    @abc.abstractmethod
    def Log10(x: TSelf, ) -> TSelf:
        ...

    @staticmethod
    @abc.abstractmethod
    def MaxMagnitude(x: TSelf, y: TSelf, ) -> TSelf:
        ...

    @staticmethod
    @abc.abstractmethod
    def MinMagnitude(x: TSelf, y: TSelf, ) -> TSelf:
        ...

    @staticmethod
    @abc.abstractmethod
    def Pow(x: TSelf, y: TSelf, ) -> TSelf:
        ...

    @staticmethod
    @abc.abstractmethod
    @typing.overload
    def Round(x: TSelf, ) -> TSelf:
        ...

    @staticmethod
    @abc.abstractmethod
    @typing.overload
    def Round(x: TSelf, digits: TInteger, ) -> TSelf:
        ...

    @staticmethod
    @abc.abstractmethod
    @typing.overload
    def Round(x: TSelf, mode: int, ) -> TSelf:
        ...

    @staticmethod
    @abc.abstractmethod
    @typing.overload
    def Round(x: TSelf, digits: TInteger, mode: int, ) -> TSelf:
        ...

    @staticmethod
    @abc.abstractmethod
    def ScaleB(x: TSelf, n: TInteger, ) -> TSelf:
        ...

    @staticmethod
    @abc.abstractmethod
    def Sin(x: TSelf, ) -> TSelf:
        ...

    @staticmethod
    @abc.abstractmethod
    def Sinh(x: TSelf, ) -> TSelf:
        ...

    @staticmethod
    @abc.abstractmethod
    def Sqrt(x: TSelf, ) -> TSelf:
        ...

    @staticmethod
    @abc.abstractmethod
    def Tan(x: TSelf, ) -> TSelf:
        ...

    @staticmethod
    @abc.abstractmethod
    def Tanh(x: TSelf, ) -> TSelf:
        ...

    @staticmethod
    @abc.abstractmethod
    def Truncate(x: TSelf, ) -> TSelf:
        ...

class IBinaryFloatingPoint(System.IBinaryNumber[TSelf], System.IBitwiseOperators[TSelf, TSelf, TSelf], System.INumber[TSelf], System.IAdditionOperators[TSelf, TSelf, TSelf], System.IAdditiveIdentity[TSelf, TSelf], System.IComparisonOperators[TSelf, TSelf], System.IComparable, System.IComparable[TSelf], System.IEqualityOperators[TSelf, TSelf], System.IEquatable[TSelf], System.IDecrementOperators[TSelf], System.IDivisionOperators[TSelf, TSelf, TSelf], System.IIncrementOperators[TSelf], System.IModulusOperators[TSelf, TSelf, TSelf], System.IMultiplicativeIdentity[TSelf, TSelf], System.IMultiplyOperators[TSelf, TSelf, TSelf], System.ISpanFormattable, System.IFormattable, System.ISpanParseable[TSelf], System.IParseable[TSelf], System.ISubtractionOperators[TSelf, TSelf, TSelf], System.IUnaryNegationOperators[TSelf, TSelf], System.IUnaryPlusOperators[TSelf, TSelf], System.IFloatingPoint[TSelf], System.ISignedNumber[TSelf], abc.ABC, typing.Generic[TSelf]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
class ISpanFormattable(System.IFormattable, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    @abc.abstractmethod
    def TryFormat(self, destination: System.Span[str], charsWritten: ref[int], format: System.ReadOnlySpan[str], provider: System.IFormatProvider, ) -> bool:
        ...

class Func(System.ICloneable, System.Runtime.Serialization.ISerializable, System.MulticastDelegate, typing.Generic[T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13, T14, TResult]):
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

    def Invoke(self, arg1: T1, arg2: T2, arg3: T3, arg4: T4, arg5: T5, arg6: T6, arg7: T7, arg8: T8, arg9: T9, arg10: T10, arg11: T11, arg12: T12, arg13: T13, arg14: T14, ) -> TResult:
        ...

    def BeginInvoke(self, arg1: T1, arg2: T2, arg3: T3, arg4: T4, arg5: T5, arg6: T6, arg7: T7, arg8: T8, arg9: T9, arg10: T10, arg11: T11, arg12: T12, arg13: T13, arg14: T14, callback: System.AsyncCallback, object: System.Object, ) -> System.IAsyncResult:
        ...

    def EndInvoke(self, result: System.IAsyncResult, ) -> TResult:
        ...

class Func(System.ICloneable, System.Runtime.Serialization.ISerializable, System.MulticastDelegate, typing.Generic[T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13, TResult]):
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

    def Invoke(self, arg1: T1, arg2: T2, arg3: T3, arg4: T4, arg5: T5, arg6: T6, arg7: T7, arg8: T8, arg9: T9, arg10: T10, arg11: T11, arg12: T12, arg13: T13, ) -> TResult:
        ...

    def BeginInvoke(self, arg1: T1, arg2: T2, arg3: T3, arg4: T4, arg5: T5, arg6: T6, arg7: T7, arg8: T8, arg9: T9, arg10: T10, arg11: T11, arg12: T12, arg13: T13, callback: System.AsyncCallback, object: System.Object, ) -> System.IAsyncResult:
        ...

    def EndInvoke(self, result: System.IAsyncResult, ) -> TResult:
        ...

class Func(System.ICloneable, System.Runtime.Serialization.ISerializable, System.MulticastDelegate, typing.Generic[T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13, T14, T15, TResult]):
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

    def Invoke(self, arg1: T1, arg2: T2, arg3: T3, arg4: T4, arg5: T5, arg6: T6, arg7: T7, arg8: T8, arg9: T9, arg10: T10, arg11: T11, arg12: T12, arg13: T13, arg14: T14, arg15: T15, ) -> TResult:
        ...

    def BeginInvoke(self, arg1: T1, arg2: T2, arg3: T3, arg4: T4, arg5: T5, arg6: T6, arg7: T7, arg8: T8, arg9: T9, arg10: T10, arg11: T11, arg12: T12, arg13: T13, arg14: T14, arg15: T15, callback: System.AsyncCallback, object: System.Object, ) -> System.IAsyncResult:
        ...

    def EndInvoke(self, result: System.IAsyncResult, ) -> TResult:
        ...

class Func(System.ICloneable, System.Runtime.Serialization.ISerializable, System.MulticastDelegate, typing.Generic[T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, TResult]):
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

    def Invoke(self, arg1: T1, arg2: T2, arg3: T3, arg4: T4, arg5: T5, arg6: T6, arg7: T7, arg8: T8, arg9: T9, arg10: T10, arg11: T11, arg12: T12, ) -> TResult:
        ...

    def BeginInvoke(self, arg1: T1, arg2: T2, arg3: T3, arg4: T4, arg5: T5, arg6: T6, arg7: T7, arg8: T8, arg9: T9, arg10: T10, arg11: T11, arg12: T12, callback: System.AsyncCallback, object: System.Object, ) -> System.IAsyncResult:
        ...

    def EndInvoke(self, result: System.IAsyncResult, ) -> TResult:
        ...

class Func(System.ICloneable, System.Runtime.Serialization.ISerializable, System.MulticastDelegate, typing.Generic[T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, TResult]):
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

    def Invoke(self, arg1: T1, arg2: T2, arg3: T3, arg4: T4, arg5: T5, arg6: T6, arg7: T7, arg8: T8, arg9: T9, arg10: T10, arg11: T11, ) -> TResult:
        ...

    def BeginInvoke(self, arg1: T1, arg2: T2, arg3: T3, arg4: T4, arg5: T5, arg6: T6, arg7: T7, arg8: T8, arg9: T9, arg10: T10, arg11: T11, callback: System.AsyncCallback, object: System.Object, ) -> System.IAsyncResult:
        ...

    def EndInvoke(self, result: System.IAsyncResult, ) -> TResult:
        ...

class Func(System.ICloneable, System.Runtime.Serialization.ISerializable, System.MulticastDelegate, typing.Generic[T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, TResult]):
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

    def Invoke(self, arg1: T1, arg2: T2, arg3: T3, arg4: T4, arg5: T5, arg6: T6, arg7: T7, arg8: T8, arg9: T9, arg10: T10, ) -> TResult:
        ...

    def BeginInvoke(self, arg1: T1, arg2: T2, arg3: T3, arg4: T4, arg5: T5, arg6: T6, arg7: T7, arg8: T8, arg9: T9, arg10: T10, callback: System.AsyncCallback, object: System.Object, ) -> System.IAsyncResult:
        ...

    def EndInvoke(self, result: System.IAsyncResult, ) -> TResult:
        ...

String = str

class IAsyncDisposable(abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    @abc.abstractmethod
    def DisposeAsync(self, ) -> System.Threading.Tasks.ValueTask:
        ...

class Func(System.ICloneable, System.Runtime.Serialization.ISerializable, System.MulticastDelegate, typing.Generic[T1, T2, TResult]):
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

    def Invoke(self, arg1: T1, arg2: T2, ) -> TResult:
        ...

    def BeginInvoke(self, arg1: T1, arg2: T2, callback: System.AsyncCallback, object: System.Object, ) -> System.IAsyncResult:
        ...

    def EndInvoke(self, result: System.IAsyncResult, ) -> TResult:
        ...

class IUnsignedNumber(System.INumber[TSelf], System.IAdditionOperators[TSelf, TSelf, TSelf], System.IAdditiveIdentity[TSelf, TSelf], System.IComparisonOperators[TSelf, TSelf], System.IComparable, System.IComparable[TSelf], System.IEqualityOperators[TSelf, TSelf], System.IEquatable[TSelf], System.IDecrementOperators[TSelf], System.IDivisionOperators[TSelf, TSelf, TSelf], System.IIncrementOperators[TSelf], System.IModulusOperators[TSelf, TSelf, TSelf], System.IMultiplicativeIdentity[TSelf, TSelf], System.IMultiplyOperators[TSelf, TSelf, TSelf], System.ISpanFormattable, System.IFormattable, System.ISpanParseable[TSelf], System.IParseable[TSelf], System.ISubtractionOperators[TSelf, TSelf, TSelf], System.IUnaryNegationOperators[TSelf, TSelf], System.IUnaryPlusOperators[TSelf, TSelf], abc.ABC, typing.Generic[TSelf]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
Boolean = bool

class UriFormat(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    UriEscaped: int = ...
    Unescaped: int = ...
    SafeUnescaped: int = ...

class IUnaryPlusOperators(abc.ABC, typing.Generic[TSelf, TResult]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
class WeakReference(System.Runtime.Serialization.ISerializable, System.Object, typing.Generic[T]):
    @typing.overload
    def __init__(self, **kwargs):
        self.m_handle: System.IntPtr
        ...

    # static fields

    # properties
    @property
    def Target(self) -> T:
        ...
    @Target.setter
    def Target(self, val: T):
        ...

    # methods
    @typing.overload
    def __init__(self, target: T, ):
        ...

    @typing.overload
    def __init__(self, target: T, trackResurrection: bool, ):
        ...

    @typing.overload
    def __init__(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext, ):
        ...

    def SetTarget(self, target: T, ) -> None:
        ...

    def Finalize(self, ) -> None:
        ...

    def Create(self, target: T, trackResurrection: bool, ) -> None:
        ...

    def IsTrackResurrection(self, ) -> bool:
        ...

    def TryGetTarget(self, target: ref[T], ) -> bool:
        ...

    def GetObjectData(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext, ) -> None:
        ...

class AppDomain(System.MarshalByRefObject):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def CurrentDomain(self) -> System.AppDomain:
        ...

    @property
    def BaseDirectory(self) -> str:
        ...

    @property
    def RelativeSearchPath(self) -> str:
        ...

    @property
    def SetupInformation(self) -> System.AppDomainSetup:
        ...

    @property
    def PermissionSet(self) -> System.Security.PermissionSet:
        ...

    @property
    def DynamicDirectory(self) -> str:
        ...

    @property
    def FriendlyName(self) -> str:
        ...

    @property
    def Id(self) -> int:
        ...

    @property
    def IsFullyTrusted(self) -> bool:
        ...

    @property
    def IsHomogenous(self) -> bool:
        ...

    @property
    def MonitoringIsEnabled(self) -> bool:
        ...
    @MonitoringIsEnabled.setter
    def MonitoringIsEnabled(self, val: bool):
        ...

    @property
    def MonitoringSurvivedMemorySize(self) -> int:
        ...

    @property
    def MonitoringSurvivedProcessMemorySize(self) -> int:
        ...

    @property
    def MonitoringTotalAllocatedMemorySize(self) -> int:
        ...

    @property
    def ShadowCopyFiles(self) -> bool:
        ...

    @property
    def MonitoringTotalProcessorTime(self) -> System.TimeSpan:
        ...

    # methods
    def __init__(self, ):
        ...

    def SetDynamicBase(self, path: str, ) -> None:
        ...

    def ApplyPolicy(self, assemblyName: str, ) -> str:
        ...

    @staticmethod
    def CreateDomain(friendlyName: str, ) -> System.AppDomain:
        ...

    @typing.overload
    def ExecuteAssembly(self, assemblyFile: str, ) -> int:
        ...

    @typing.overload
    def ExecuteAssembly(self, assemblyFile: str, args: System.Array[str], ) -> int:
        ...

    @typing.overload
    def ExecuteAssembly(self, assemblyFile: str, args: System.Array[str], hashValue: System.Array[int], hashAlgorithm: int, ) -> int:
        ...

    @staticmethod
    @typing.overload
    def ExecuteAssembly(assembly: System.Reflection.Assembly, args: System.Array[str], ) -> int:
        ...

    @typing.overload
    def ExecuteAssemblyByName(self, assemblyName: System.Reflection.AssemblyName, args: System.Array[str], ) -> int:
        ...

    @typing.overload
    def ExecuteAssemblyByName(self, assemblyName: str, ) -> int:
        ...

    @typing.overload
    def ExecuteAssemblyByName(self, assemblyName: str, args: System.Array[str], ) -> int:
        ...

    def GetData(self, name: str, ) -> System.Object:
        ...

    def SetData(self, name: str, data: System.Object, ) -> None:
        ...

    def IsCompatibilitySwitchSet(self, value: str, ) -> System.Nullable[bool]:
        ...

    def IsDefaultAppDomain(self, ) -> bool:
        ...

    def IsFinalizingForUnload(self, ) -> bool:
        ...

    def ToString(self, ) -> str:
        ...

    @staticmethod
    def Unload(domain: System.AppDomain, ) -> None:
        ...

    @typing.overload
    def Load(self, rawAssembly: System.Array[int], ) -> System.Reflection.Assembly:
        ...

    @typing.overload
    def Load(self, rawAssembly: System.Array[int], rawSymbolStore: System.Array[int], ) -> System.Reflection.Assembly:
        ...

    @typing.overload
    def Load(self, assemblyRef: System.Reflection.AssemblyName, ) -> System.Reflection.Assembly:
        ...

    @typing.overload
    def Load(self, assemblyString: str, ) -> System.Reflection.Assembly:
        ...

    def ReflectionOnlyGetAssemblies(self, ) -> System.Array[System.Reflection.Assembly]:
        ...

    @staticmethod
    def GetCurrentThreadId() -> int:
        ...

    def AppendPrivatePath(self, path: str, ) -> None:
        ...

    def ClearPrivatePath(self, ) -> None:
        ...

    def ClearShadowCopyPath(self, ) -> None:
        ...

    def SetCachePath(self, path: str, ) -> None:
        ...

    def SetShadowCopyFiles(self, ) -> None:
        ...

    def SetShadowCopyPath(self, path: str, ) -> None:
        ...

    def GetAssemblies(self, ) -> System.Array[System.Reflection.Assembly]:
        ...

    def SetPrincipalPolicy(self, policy: int, ) -> None:
        ...

    def SetThreadPrincipal(self, principal: System.Security.Principal.IPrincipal, ) -> None:
        ...

    @typing.overload
    def CreateInstance(self, assemblyName: str, typeName: str, ) -> System.Runtime.Remoting.ObjectHandle:
        ...

    @typing.overload
    def CreateInstance(self, assemblyName: str, typeName: str, ignoreCase: bool, bindingAttr: int, binder: System.Reflection.Binder, args: System.Array[System.Object], culture: System.Globalization.CultureInfo, activationAttributes: System.Array[System.Object], ) -> System.Runtime.Remoting.ObjectHandle:
        ...

    @typing.overload
    def CreateInstance(self, assemblyName: str, typeName: str, activationAttributes: System.Array[System.Object], ) -> System.Runtime.Remoting.ObjectHandle:
        ...

    @typing.overload
    def CreateInstanceAndUnwrap(self, assemblyName: str, typeName: str, ) -> System.Object:
        ...

    @typing.overload
    def CreateInstanceAndUnwrap(self, assemblyName: str, typeName: str, ignoreCase: bool, bindingAttr: int, binder: System.Reflection.Binder, args: System.Array[System.Object], culture: System.Globalization.CultureInfo, activationAttributes: System.Array[System.Object], ) -> System.Object:
        ...

    @typing.overload
    def CreateInstanceAndUnwrap(self, assemblyName: str, typeName: str, activationAttributes: System.Array[System.Object], ) -> System.Object:
        ...

    @typing.overload
    def CreateInstanceFrom(self, assemblyFile: str, typeName: str, ) -> System.Runtime.Remoting.ObjectHandle:
        ...

    @typing.overload
    def CreateInstanceFrom(self, assemblyFile: str, typeName: str, ignoreCase: bool, bindingAttr: int, binder: System.Reflection.Binder, args: System.Array[System.Object], culture: System.Globalization.CultureInfo, activationAttributes: System.Array[System.Object], ) -> System.Runtime.Remoting.ObjectHandle:
        ...

    @typing.overload
    def CreateInstanceFrom(self, assemblyFile: str, typeName: str, activationAttributes: System.Array[System.Object], ) -> System.Runtime.Remoting.ObjectHandle:
        ...

    @typing.overload
    def CreateInstanceFromAndUnwrap(self, assemblyFile: str, typeName: str, ) -> System.Object:
        ...

    @typing.overload
    def CreateInstanceFromAndUnwrap(self, assemblyFile: str, typeName: str, ignoreCase: bool, bindingAttr: int, binder: System.Reflection.Binder, args: System.Array[System.Object], culture: System.Globalization.CultureInfo, activationAttributes: System.Array[System.Object], ) -> System.Object:
        ...

    @typing.overload
    def CreateInstanceFromAndUnwrap(self, assemblyFile: str, typeName: str, activationAttributes: System.Array[System.Object], ) -> System.Object:
        ...

    def GetThreadPrincipal(self, ) -> System.Security.Principal.IPrincipal:
        ...

class AppDomainSetup(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def ApplicationBase(self) -> str:
        ...

    @property
    def TargetFrameworkName(self) -> str:
        ...

    # methods
    def __init__(self, ):
        ...

class LocalDataStoreSlot(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def Data(self) -> System.Threading.ThreadLocal[System.Object]:
        ...
    @Data.setter
    def Data(self, val: System.Threading.ThreadLocal[System.Object]):
        ...

    # methods
    def __init__(self, data: System.Threading.ThreadLocal[System.Object], ):
        ...

    def Finalize(self, ) -> None:
        ...

class Type(System.Reflection.ICustomAttributeProvider, System.Reflection.IReflect, System.Reflection.MemberInfo, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields
    Delimiter: str = ...
    EmptyTypes: System.Array[System.Type] = ...
    Missing: System.Object = ...
    FilterAttribute: System.Reflection.MemberFilter = ...
    FilterName: System.Reflection.MemberFilter = ...
    FilterNameIgnoreCase: System.Reflection.MemberFilter = ...

    # properties
    @property
    def IsInterface(self) -> bool:
        ...

    @property
    def MemberType(self) -> int:
        ...

    @property
    @abc.abstractmethod
    def Namespace(self) -> str:
        ...

    @property
    @abc.abstractmethod
    def AssemblyQualifiedName(self) -> str:
        ...

    @property
    @abc.abstractmethod
    def FullName(self) -> str:
        ...

    @property
    @abc.abstractmethod
    def Assembly(self) -> System.Reflection.Assembly:
        ...

    @property
    @abc.abstractmethod
    def Module(self) -> System.Reflection.Module:
        ...

    @property
    def IsNested(self) -> bool:
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

    @property
    @abc.abstractmethod
    def UnderlyingSystemType(self) -> System.Type:
        ...

    @property
    def IsTypeDefinition(self) -> bool:
        ...

    @property
    def IsArray(self) -> bool:
        ...

    @property
    def IsByRef(self) -> bool:
        ...

    @property
    def IsPointer(self) -> bool:
        ...

    @property
    def IsConstructedGenericType(self) -> bool:
        ...

    @property
    def IsGenericParameter(self) -> bool:
        ...

    @property
    def IsGenericTypeParameter(self) -> bool:
        ...

    @property
    def IsGenericMethodParameter(self) -> bool:
        ...

    @property
    def IsGenericType(self) -> bool:
        ...

    @property
    def IsGenericTypeDefinition(self) -> bool:
        ...

    @property
    def IsSZArray(self) -> bool:
        ...

    @property
    def IsVariableBoundArray(self) -> bool:
        ...

    @property
    def IsByRefLike(self) -> bool:
        ...

    @property
    def HasElementType(self) -> bool:
        ...

    @property
    def GenericTypeArguments(self) -> System.Array[System.Type]:
        ...

    @property
    def GenericParameterPosition(self) -> int:
        ...

    @property
    def GenericParameterAttributes(self) -> int:
        ...

    @property
    def Attributes(self) -> int:
        ...

    @property
    def IsAbstract(self) -> bool:
        ...

    @property
    def IsImport(self) -> bool:
        ...

    @property
    def IsSealed(self) -> bool:
        ...

    @property
    def IsSpecialName(self) -> bool:
        ...

    @property
    def IsClass(self) -> bool:
        ...

    @property
    def IsNestedAssembly(self) -> bool:
        ...

    @property
    def IsNestedFamANDAssem(self) -> bool:
        ...

    @property
    def IsNestedFamily(self) -> bool:
        ...

    @property
    def IsNestedFamORAssem(self) -> bool:
        ...

    @property
    def IsNestedPrivate(self) -> bool:
        ...

    @property
    def IsNestedPublic(self) -> bool:
        ...

    @property
    def IsNotPublic(self) -> bool:
        ...

    @property
    def IsPublic(self) -> bool:
        ...

    @property
    def IsAutoLayout(self) -> bool:
        ...

    @property
    def IsExplicitLayout(self) -> bool:
        ...

    @property
    def IsLayoutSequential(self) -> bool:
        ...

    @property
    def IsAnsiClass(self) -> bool:
        ...

    @property
    def IsAutoClass(self) -> bool:
        ...

    @property
    def IsUnicodeClass(self) -> bool:
        ...

    @property
    def IsCOMObject(self) -> bool:
        ...

    @property
    def IsContextful(self) -> bool:
        ...

    @property
    def IsEnum(self) -> bool:
        ...

    @property
    def IsMarshalByRef(self) -> bool:
        ...

    @property
    def IsPrimitive(self) -> bool:
        ...

    @property
    def IsValueType(self) -> bool:
        ...

    @property
    def IsSignatureType(self) -> bool:
        ...

    @property
    def IsSecurityCritical(self) -> bool:
        ...

    @property
    def IsSecuritySafeCritical(self) -> bool:
        ...

    @property
    def IsSecurityTransparent(self) -> bool:
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

    @property
    @abc.abstractmethod
    def GUID(self) -> System.Guid:
        ...

    @property
    @abc.abstractmethod
    def BaseType(self) -> System.Type:
        ...

    @property
    def DefaultBinder(self) -> System.Reflection.Binder:
        ...

    @property
    def IsSerializable(self) -> bool:
        ...

    @property
    def ContainsGenericParameters(self) -> bool:
        ...

    @property
    def IsVisible(self) -> bool:
        ...

    @property
    @abc.abstractmethod
    def Name(self) -> str:
        ...

    @property
    def CustomAttributes(self) -> System.Collections.Generic.IEnumerable[System.Reflection.CustomAttributeData]:
        ...

    @property
    def IsCollectible(self) -> bool:
        ...

    @property
    def MetadataToken(self) -> int:
        ...

    # methods
    def __init__(self, ):
        ...

    @abc.abstractmethod
    @typing.overload
    def GetField(self, name: str, bindingAttr: int, ) -> System.Reflection.FieldInfo:
        ...

    @typing.overload
    def GetField(self, name: str, ) -> System.Reflection.FieldInfo:
        ...

    @typing.overload
    def GetFields(self, ) -> System.Array[System.Reflection.FieldInfo]:
        ...

    @abc.abstractmethod
    @typing.overload
    def GetFields(self, bindingAttr: int, ) -> System.Array[System.Reflection.FieldInfo]:
        ...

    @typing.overload
    def GetMember(self, name: str, ) -> System.Array[System.Reflection.MemberInfo]:
        ...

    @typing.overload
    def GetMember(self, name: str, bindingAttr: int, ) -> System.Array[System.Reflection.MemberInfo]:
        ...

    @typing.overload
    def GetMember(self, name: str, type: int, bindingAttr: int, ) -> System.Array[System.Reflection.MemberInfo]:
        ...

    @typing.overload
    def GetMembers(self, ) -> System.Array[System.Reflection.MemberInfo]:
        ...

    @abc.abstractmethod
    @typing.overload
    def GetMembers(self, bindingAttr: int, ) -> System.Array[System.Reflection.MemberInfo]:
        ...

    def GetMemberWithSameMetadataDefinitionAs(self, member: System.Reflection.MemberInfo, ) -> System.Reflection.MemberInfo:
        ...

    @staticmethod
    def CreateGetMemberWithSameMetadataDefinitionAsNotFoundException(member: System.Reflection.MemberInfo, ) -> System.ArgumentException:
        ...

    @typing.overload
    def GetMethod(self, name: str, ) -> System.Reflection.MethodInfo:
        ...

    @typing.overload
    def GetMethod(self, name: str, bindingAttr: int, ) -> System.Reflection.MethodInfo:
        ...

    @typing.overload
    def GetMethod(self, name: str, bindingAttr: int, types: System.Array[System.Type], ) -> System.Reflection.MethodInfo:
        ...

    @typing.overload
    def GetMethod(self, name: str, types: System.Array[System.Type], ) -> System.Reflection.MethodInfo:
        ...

    @typing.overload
    def GetMethod(self, name: str, types: System.Array[System.Type], modifiers: System.Array[System.Reflection.ParameterModifier], ) -> System.Reflection.MethodInfo:
        ...

    @typing.overload
    def GetMethod(self, name: str, bindingAttr: int, binder: System.Reflection.Binder, types: System.Array[System.Type], modifiers: System.Array[System.Reflection.ParameterModifier], ) -> System.Reflection.MethodInfo:
        ...

    @typing.overload
    def GetMethod(self, name: str, bindingAttr: int, binder: System.Reflection.Binder, callConvention: int, types: System.Array[System.Type], modifiers: System.Array[System.Reflection.ParameterModifier], ) -> System.Reflection.MethodInfo:
        ...

    @typing.overload
    def GetMethod(self, name: str, genericParameterCount: int, types: System.Array[System.Type], ) -> System.Reflection.MethodInfo:
        ...

    @typing.overload
    def GetMethod(self, name: str, genericParameterCount: int, types: System.Array[System.Type], modifiers: System.Array[System.Reflection.ParameterModifier], ) -> System.Reflection.MethodInfo:
        ...

    @typing.overload
    def GetMethod(self, name: str, genericParameterCount: int, bindingAttr: int, binder: System.Reflection.Binder, types: System.Array[System.Type], modifiers: System.Array[System.Reflection.ParameterModifier], ) -> System.Reflection.MethodInfo:
        ...

    @typing.overload
    def GetMethod(self, name: str, genericParameterCount: int, bindingAttr: int, binder: System.Reflection.Binder, callConvention: int, types: System.Array[System.Type], modifiers: System.Array[System.Reflection.ParameterModifier], ) -> System.Reflection.MethodInfo:
        ...

    @abc.abstractmethod
    @typing.overload
    def GetMethodImpl(self, name: str, bindingAttr: int, binder: System.Reflection.Binder, callConvention: int, types: System.Array[System.Type], modifiers: System.Array[System.Reflection.ParameterModifier], ) -> System.Reflection.MethodInfo:
        ...

    @typing.overload
    def GetMethodImpl(self, name: str, genericParameterCount: int, bindingAttr: int, binder: System.Reflection.Binder, callConvention: int, types: System.Array[System.Type], modifiers: System.Array[System.Reflection.ParameterModifier], ) -> System.Reflection.MethodInfo:
        ...

    @typing.overload
    def GetMethods(self, ) -> System.Array[System.Reflection.MethodInfo]:
        ...

    @abc.abstractmethod
    @typing.overload
    def GetMethods(self, bindingAttr: int, ) -> System.Array[System.Reflection.MethodInfo]:
        ...

    @typing.overload
    def GetNestedType(self, name: str, ) -> System.Type:
        ...

    @abc.abstractmethod
    @typing.overload
    def GetNestedType(self, name: str, bindingAttr: int, ) -> System.Type:
        ...

    @typing.overload
    def GetNestedTypes(self, ) -> System.Array[System.Type]:
        ...

    @abc.abstractmethod
    @typing.overload
    def GetNestedTypes(self, bindingAttr: int, ) -> System.Array[System.Type]:
        ...

    @typing.overload
    def GetProperty(self, name: str, ) -> System.Reflection.PropertyInfo:
        ...

    @typing.overload
    def GetProperty(self, name: str, bindingAttr: int, ) -> System.Reflection.PropertyInfo:
        ...

    @typing.overload
    def GetProperty(self, name: str, returnType: System.Type, ) -> System.Reflection.PropertyInfo:
        ...

    @typing.overload
    def GetProperty(self, name: str, types: System.Array[System.Type], ) -> System.Reflection.PropertyInfo:
        ...

    @typing.overload
    def GetProperty(self, name: str, returnType: System.Type, types: System.Array[System.Type], ) -> System.Reflection.PropertyInfo:
        ...

    @typing.overload
    def GetProperty(self, name: str, returnType: System.Type, types: System.Array[System.Type], modifiers: System.Array[System.Reflection.ParameterModifier], ) -> System.Reflection.PropertyInfo:
        ...

    @typing.overload
    def GetProperty(self, name: str, bindingAttr: int, binder: System.Reflection.Binder, returnType: System.Type, types: System.Array[System.Type], modifiers: System.Array[System.Reflection.ParameterModifier], ) -> System.Reflection.PropertyInfo:
        ...

    @abc.abstractmethod
    def GetPropertyImpl(self, name: str, bindingAttr: int, binder: System.Reflection.Binder, returnType: System.Type, types: System.Array[System.Type], modifiers: System.Array[System.Reflection.ParameterModifier], ) -> System.Reflection.PropertyInfo:
        ...

    @typing.overload
    def GetProperties(self, ) -> System.Array[System.Reflection.PropertyInfo]:
        ...

    @abc.abstractmethod
    @typing.overload
    def GetProperties(self, bindingAttr: int, ) -> System.Array[System.Reflection.PropertyInfo]:
        ...

    def GetDefaultMembers(self, ) -> System.Array[System.Reflection.MemberInfo]:
        ...

    @staticmethod
    def GetTypeHandle(o: System.Object, ) -> System.RuntimeTypeHandle:
        ...

    @staticmethod
    def GetTypeArray(args: System.Array[System.Object], ) -> System.Array[System.Type]:
        ...

    @staticmethod
    def GetTypeCode(type: System.Type, ) -> int:
        ...

    def GetTypeCodeImpl(self, ) -> int:
        ...

    @staticmethod
    @typing.overload
    def GetTypeFromCLSID(clsid: System.Guid, ) -> System.Type:
        ...

    @staticmethod
    @typing.overload
    def GetTypeFromCLSID(clsid: System.Guid, throwOnError: bool, ) -> System.Type:
        ...

    @staticmethod
    @typing.overload
    def GetTypeFromCLSID(clsid: System.Guid, server: str, ) -> System.Type:
        ...

    @staticmethod
    @typing.overload
    def GetTypeFromCLSID(clsid: System.Guid, server: str, throwOnError: bool, ) -> System.Type:
        ...

    @staticmethod
    @typing.overload
    def GetTypeFromProgID(progID: str, ) -> System.Type:
        ...

    @staticmethod
    @typing.overload
    def GetTypeFromProgID(progID: str, throwOnError: bool, ) -> System.Type:
        ...

    @staticmethod
    @typing.overload
    def GetTypeFromProgID(progID: str, server: str, ) -> System.Type:
        ...

    @staticmethod
    @typing.overload
    def GetTypeFromProgID(progID: str, server: str, throwOnError: bool, ) -> System.Type:
        ...

    @typing.overload
    def InvokeMember(self, name: str, invokeAttr: int, binder: System.Reflection.Binder, target: System.Object, args: System.Array[System.Object], ) -> System.Object:
        ...

    @typing.overload
    def InvokeMember(self, name: str, invokeAttr: int, binder: System.Reflection.Binder, target: System.Object, args: System.Array[System.Object], culture: System.Globalization.CultureInfo, ) -> System.Object:
        ...

    @abc.abstractmethod
    @typing.overload
    def InvokeMember(self, name: str, invokeAttr: int, binder: System.Reflection.Binder, target: System.Object, args: System.Array[System.Object], modifiers: System.Array[System.Reflection.ParameterModifier], culture: System.Globalization.CultureInfo, namedParameters: System.Array[str], ) -> System.Object:
        ...

    @typing.overload
    def GetInterface(self, name: str, ) -> System.Type:
        ...

    @abc.abstractmethod
    @typing.overload
    def GetInterface(self, name: str, ignoreCase: bool, ) -> System.Type:
        ...

    @abc.abstractmethod
    def GetInterfaces(self, ) -> System.Array[System.Type]:
        ...

    def GetInterfaceMap(self, interfaceType: System.Type, ) -> System.Reflection.InterfaceMapping:
        ...

    def IsInstanceOfType(self, o: System.Object, ) -> bool:
        ...

    def IsEquivalentTo(self, other: System.Type, ) -> bool:
        ...

    def GetEnumUnderlyingType(self, ) -> System.Type:
        ...

    def GetEnumValues(self, ) -> System.Array:
        ...

    @typing.overload
    def MakeArrayType(self, ) -> System.Type:
        ...

    @typing.overload
    def MakeArrayType(self, rank: int, ) -> System.Type:
        ...

    def MakeByRefType(self, ) -> System.Type:
        ...

    def MakeGenericType(self, typeArguments: System.Array[System.Type], ) -> System.Type:
        ...

    def MakePointerType(self, ) -> System.Type:
        ...

    @staticmethod
    def MakeGenericSignatureType(genericTypeDefinition: System.Type, typeArguments: System.Array[System.Type], ) -> System.Type:
        ...

    @staticmethod
    def MakeGenericMethodParameter(position: int, ) -> System.Type:
        ...

    def FormatTypeName(self, ) -> str:
        ...

    def ToString(self, ) -> str:
        ...

    @typing.overload
    def Equals(self, o: System.Object, ) -> bool:
        ...

    @typing.overload
    def Equals(self, o: System.Type, ) -> bool:
        ...

    def GetHashCode(self, ) -> int:
        ...

    @staticmethod
    def ReflectionOnlyGetType(typeName: str, throwIfNotFound: bool, ignoreCase: bool, ) -> System.Type:
        ...

    def IsEnumDefined(self, value: System.Object, ) -> bool:
        ...

    def GetEnumName(self, value: System.Object, ) -> str:
        ...

    def GetEnumNames(self, ) -> System.Array[str]:
        ...

    def GetEnumRawConstantValues(self, ) -> System.Array:
        ...

    def GetEnumData(self, enumNames: ref[System.Array[str]], enumValues: ref[System.Array], ) -> None:
        ...

    @staticmethod
    def BinarySearch(array: System.Array, value: System.Object, ) -> int:
        ...

    @staticmethod
    def IsIntegerType(t: System.Type, ) -> bool:
        ...

    def GetRootElementType(self, ) -> System.Type:
        ...

    def FindInterfaces(self, filter: System.Reflection.TypeFilter, filterCriteria: System.Object, ) -> System.Array[System.Type]:
        ...

    def FindMembers(self, memberType: int, bindingAttr: int, filter: System.Reflection.MemberFilter, filterCriteria: System.Object, ) -> System.Array[System.Reflection.MemberInfo]:
        ...

    def IsSubclassOf(self, c: System.Type, ) -> bool:
        ...

    def IsAssignableFrom(self, c: System.Type, ) -> bool:
        ...

    def ImplementInterface(self, ifaceType: System.Type, ) -> bool:
        ...

    @staticmethod
    def FilterAttributeImpl(m: System.Reflection.MemberInfo, filterCriteria: System.Object, ) -> bool:
        ...

    @staticmethod
    def FilterNameImpl(m: System.Reflection.MemberInfo, filterCriteria: System.Object, comparison: int, ) -> bool:
        ...

    @staticmethod
    @typing.overload
    def GetType(typeName: str, throwOnError: bool, ignoreCase: bool, ) -> System.Type:
        ...

    @staticmethod
    @typing.overload
    def GetType(typeName: str, throwOnError: bool, ) -> System.Type:
        ...

    @staticmethod
    @typing.overload
    def GetType(typeName: str, ) -> System.Type:
        ...

    @staticmethod
    @typing.overload
    def GetType(typeName: str, assemblyResolver: System.Func[System.Reflection.AssemblyName, System.Reflection.Assembly], typeResolver: System.Func[System.Reflection.Assembly, str, bool, System.Type], ) -> System.Type:
        ...

    @staticmethod
    @typing.overload
    def GetType(typeName: str, assemblyResolver: System.Func[System.Reflection.AssemblyName, System.Reflection.Assembly], typeResolver: System.Func[System.Reflection.Assembly, str, bool, System.Type], throwOnError: bool, ) -> System.Type:
        ...

    @staticmethod
    @typing.overload
    def GetType(typeName: str, assemblyResolver: System.Func[System.Reflection.AssemblyName, System.Reflection.Assembly], typeResolver: System.Func[System.Reflection.Assembly, str, bool, System.Type], throwOnError: bool, ignoreCase: bool, ) -> System.Type:
        ...

    @typing.overload
    def GetType(self, ) -> System.Type:
        ...

    def GetTypeHandleInternal(self, ) -> System.RuntimeTypeHandle:
        ...

    @staticmethod
    def GetTypeFromHandle(handle: System.RuntimeTypeHandle, ) -> System.Type:
        ...

    def IsRuntimeImplemented(self, ) -> bool:
        ...

    @abc.abstractmethod
    def IsArrayImpl(self, ) -> bool:
        ...

    @abc.abstractmethod
    def IsByRefImpl(self, ) -> bool:
        ...

    @abc.abstractmethod
    def IsPointerImpl(self, ) -> bool:
        ...

    @abc.abstractmethod
    def HasElementTypeImpl(self, ) -> bool:
        ...

    @abc.abstractmethod
    def GetElementType(self, ) -> System.Type:
        ...

    def GetArrayRank(self, ) -> int:
        ...

    def GetGenericTypeDefinition(self, ) -> System.Type:
        ...

    def GetGenericArguments(self, ) -> System.Array[System.Type]:
        ...

    def GetGenericParameterConstraints(self, ) -> System.Array[System.Type]:
        ...

    @abc.abstractmethod
    def GetAttributeFlagsImpl(self, ) -> int:
        ...

    @abc.abstractmethod
    def IsCOMObjectImpl(self, ) -> bool:
        ...

    def IsContextfulImpl(self, ) -> bool:
        ...

    def IsMarshalByRefImpl(self, ) -> bool:
        ...

    @abc.abstractmethod
    def IsPrimitiveImpl(self, ) -> bool:
        ...

    def IsAssignableTo(self, targetType: System.Type, ) -> bool:
        ...

    def IsValueTypeImpl(self, ) -> bool:
        ...

    @typing.overload
    def GetConstructor(self, types: System.Array[System.Type], ) -> System.Reflection.ConstructorInfo:
        ...

    @typing.overload
    def GetConstructor(self, bindingAttr: int, types: System.Array[System.Type], ) -> System.Reflection.ConstructorInfo:
        ...

    @typing.overload
    def GetConstructor(self, bindingAttr: int, binder: System.Reflection.Binder, types: System.Array[System.Type], modifiers: System.Array[System.Reflection.ParameterModifier], ) -> System.Reflection.ConstructorInfo:
        ...

    @typing.overload
    def GetConstructor(self, bindingAttr: int, binder: System.Reflection.Binder, callConvention: int, types: System.Array[System.Type], modifiers: System.Array[System.Reflection.ParameterModifier], ) -> System.Reflection.ConstructorInfo:
        ...

    @abc.abstractmethod
    def GetConstructorImpl(self, bindingAttr: int, binder: System.Reflection.Binder, callConvention: int, types: System.Array[System.Type], modifiers: System.Array[System.Reflection.ParameterModifier], ) -> System.Reflection.ConstructorInfo:
        ...

    @typing.overload
    def GetConstructors(self, ) -> System.Array[System.Reflection.ConstructorInfo]:
        ...

    @abc.abstractmethod
    @typing.overload
    def GetConstructors(self, bindingAttr: int, ) -> System.Array[System.Reflection.ConstructorInfo]:
        ...

    @typing.overload
    def GetEvent(self, name: str, ) -> System.Reflection.EventInfo:
        ...

    @abc.abstractmethod
    @typing.overload
    def GetEvent(self, name: str, bindingAttr: int, ) -> System.Reflection.EventInfo:
        ...

    @typing.overload
    def GetEvents(self, ) -> System.Array[System.Reflection.EventInfo]:
        ...

    @abc.abstractmethod
    @typing.overload
    def GetEvents(self, bindingAttr: int, ) -> System.Array[System.Reflection.EventInfo]:
        ...

class EventHandler(System.ICloneable, System.Runtime.Serialization.ISerializable, System.MulticastDelegate):
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

    def Invoke(self, sender: System.Object, e: System.EventArgs, ) -> None:
        ...

    def BeginInvoke(self, sender: System.Object, e: System.EventArgs, callback: System.AsyncCallback, object: System.Object, ) -> System.IAsyncResult:
        ...

    def EndInvoke(self, result: System.IAsyncResult, ) -> None:
        ...

class InvalidOperationException(System.Runtime.Serialization.ISerializable, System.SystemException):
    @typing.overload
    def __init__(self, **kwargs):
        self._message: str
        ...

    # static fields

    # properties
    @property
    def TargetSite(self) -> System.Reflection.MethodBase:
        ...

    @property
    def Message(self) -> str:
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
    def __init__(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext, ):
        ...

class Func(System.ICloneable, System.Runtime.Serialization.ISerializable, System.MulticastDelegate, typing.Generic[T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13, T14, T15, T16, TResult]):
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

    def Invoke(self, arg1: T1, arg2: T2, arg3: T3, arg4: T4, arg5: T5, arg6: T6, arg7: T7, arg8: T8, arg9: T9, arg10: T10, arg11: T11, arg12: T12, arg13: T13, arg14: T14, arg15: T15, arg16: T16, ) -> TResult:
        ...

    def BeginInvoke(self, arg1: T1, arg2: T2, arg3: T3, arg4: T4, arg5: T5, arg6: T6, arg7: T7, arg8: T8, arg9: T9, arg10: T10, arg11: T11, arg12: T12, arg13: T13, arg14: T14, arg15: T15, arg16: T16, callback: System.AsyncCallback, object: System.Object, ) -> System.IAsyncResult:
        ...

    def EndInvoke(self, result: System.IAsyncResult, ) -> TResult:
        ...

Single = float

class WeakReference(System.Runtime.Serialization.ISerializable, System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        self.m_handle: System.IntPtr
        ...

    # static fields

    # properties
    @property
    def IsAlive(self) -> bool:
        ...

    @property
    def TrackResurrection(self) -> bool:
        ...

    @property
    def Target(self) -> System.Object:
        ...
    @Target.setter
    def Target(self, val: System.Object):
        ...

    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def __init__(self, target: System.Object, ):
        ...

    @typing.overload
    def __init__(self, target: System.Object, trackResurrection: bool, ):
        ...

    @typing.overload
    def __init__(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext, ):
        ...

    def Finalize(self, ) -> None:
        ...

    def Create(self, target: System.Object, trackResurrection: bool, ) -> None:
        ...

    def IsTrackResurrection(self, ) -> bool:
        ...

    def GetObjectData(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext, ) -> None:
        ...

class EventHandler(System.ICloneable, System.Runtime.Serialization.ISerializable, System.MulticastDelegate, typing.Generic[TEventArgs]):
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

    def Invoke(self, sender: System.Object, e: TEventArgs, ) -> None:
        ...

    def BeginInvoke(self, sender: System.Object, e: TEventArgs, callback: System.AsyncCallback, object: System.Object, ) -> System.IAsyncResult:
        ...

    def EndInvoke(self, result: System.IAsyncResult, ) -> None:
        ...

