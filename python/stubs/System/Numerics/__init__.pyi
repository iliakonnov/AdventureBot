from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import System
import System.Numerics


class BigInteger(System.ISpanFormattable, System.IFormattable, System.IComparable, System.IComparable[System.Numerics.BigInteger], System.IEquatable[System.Numerics.BigInteger], System.ValueType):
    @typing.overload
    def __init__(self, **kwargs):
        self._sign: int
        self._bits: System.Array[int]
        ...

    # static fields

    # properties
    @property
    def Zero(self) -> System.Numerics.BigInteger:
        ...

    @property
    def One(self) -> System.Numerics.BigInteger:
        ...

    @property
    def MinusOne(self) -> System.Numerics.BigInteger:
        ...

    @property
    def IsPowerOfTwo(self) -> bool:
        ...

    @property
    def IsZero(self) -> bool:
        ...

    @property
    def IsOne(self) -> bool:
        ...

    @property
    def IsEven(self) -> bool:
        ...

    @property
    def Sign(self) -> int:
        ...

    # methods
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
    def __init__(self, value: System.Decimal, ):
        ...

    @typing.overload
    def __init__(self, value: System.Array[int], ):
        ...

    @typing.overload
    def __init__(self, value: System.ReadOnlySpan[int], isUnsigned: bool = ..., isBigEndian: bool = ..., ):
        ...

    @typing.overload
    def __init__(self, n: int, rgu: System.Array[int], ):
        ...

    @typing.overload
    def __init__(self, value: System.ReadOnlySpan[int], valueArray: System.Array[int], negative: bool, ):
        ...

    @typing.overload
    def __init__(self, value: System.Array[int], ):
        ...

    def GetBitLength(self, ) -> int:
        ...

    @staticmethod
    def GetPartsForBitManipulation(x: ref[System.Numerics.BigInteger], xd: ref[System.Span[int]], ) -> bool:
        ...

    @staticmethod
    def GetDiffLength(rgu1: System.Array[int], rgu2: System.Array[int], cu: int, ) -> int:
        ...

    @staticmethod
    @typing.overload
    def Parse(value: str, ) -> System.Numerics.BigInteger:
        ...

    @staticmethod
    @typing.overload
    def Parse(value: str, style: int, ) -> System.Numerics.BigInteger:
        ...

    @staticmethod
    @typing.overload
    def Parse(value: str, provider: System.IFormatProvider, ) -> System.Numerics.BigInteger:
        ...

    @staticmethod
    @typing.overload
    def Parse(value: str, style: int, provider: System.IFormatProvider, ) -> System.Numerics.BigInteger:
        ...

    @staticmethod
    @typing.overload
    def Parse(value: System.ReadOnlySpan[str], style: int = ..., provider: System.IFormatProvider = ..., ) -> System.Numerics.BigInteger:
        ...

    @staticmethod
    @typing.overload
    def TryParse(value: str, result: ref[System.Numerics.BigInteger], ) -> bool:
        ...

    @staticmethod
    @typing.overload
    def TryParse(value: str, style: int, provider: System.IFormatProvider, result: ref[System.Numerics.BigInteger], ) -> bool:
        ...

    @staticmethod
    @typing.overload
    def TryParse(value: System.ReadOnlySpan[str], result: ref[System.Numerics.BigInteger], ) -> bool:
        ...

    @staticmethod
    @typing.overload
    def TryParse(value: System.ReadOnlySpan[str], style: int, provider: System.IFormatProvider, result: ref[System.Numerics.BigInteger], ) -> bool:
        ...

    @staticmethod
    def Compare(left: System.Numerics.BigInteger, right: System.Numerics.BigInteger, ) -> int:
        ...

    @staticmethod
    def Abs(value: System.Numerics.BigInteger, ) -> System.Numerics.BigInteger:
        ...

    @staticmethod
    @typing.overload
    def Add(left: System.Numerics.BigInteger, right: System.Numerics.BigInteger, ) -> System.Numerics.BigInteger:
        ...

    @staticmethod
    @typing.overload
    def Add(leftBits: System.Array[int], leftSign: int, rightBits: System.Array[int], rightSign: int, ) -> System.Numerics.BigInteger:
        ...

    @staticmethod
    @typing.overload
    def Subtract(left: System.Numerics.BigInteger, right: System.Numerics.BigInteger, ) -> System.Numerics.BigInteger:
        ...

    @staticmethod
    @typing.overload
    def Subtract(leftBits: System.Array[int], leftSign: int, rightBits: System.Array[int], rightSign: int, ) -> System.Numerics.BigInteger:
        ...

    @staticmethod
    def Multiply(left: System.Numerics.BigInteger, right: System.Numerics.BigInteger, ) -> System.Numerics.BigInteger:
        ...

    @staticmethod
    def Divide(dividend: System.Numerics.BigInteger, divisor: System.Numerics.BigInteger, ) -> System.Numerics.BigInteger:
        ...

    @staticmethod
    def Remainder(dividend: System.Numerics.BigInteger, divisor: System.Numerics.BigInteger, ) -> System.Numerics.BigInteger:
        ...

    @staticmethod
    def DivRem(dividend: System.Numerics.BigInteger, divisor: System.Numerics.BigInteger, remainder: ref[System.Numerics.BigInteger], ) -> System.Numerics.BigInteger:
        ...

    @staticmethod
    def Negate(value: System.Numerics.BigInteger, ) -> System.Numerics.BigInteger:
        ...

    @staticmethod
    @typing.overload
    def Log(value: System.Numerics.BigInteger, ) -> float:
        ...

    @staticmethod
    @typing.overload
    def Log(value: System.Numerics.BigInteger, baseValue: float, ) -> float:
        ...

    @staticmethod
    def Log10(value: System.Numerics.BigInteger, ) -> float:
        ...

    @staticmethod
    @typing.overload
    def GreatestCommonDivisor(left: System.Numerics.BigInteger, right: System.Numerics.BigInteger, ) -> System.Numerics.BigInteger:
        ...

    @staticmethod
    @typing.overload
    def GreatestCommonDivisor(leftBits: System.Array[int], rightBits: System.Array[int], ) -> System.Numerics.BigInteger:
        ...

    @staticmethod
    def Max(left: System.Numerics.BigInteger, right: System.Numerics.BigInteger, ) -> System.Numerics.BigInteger:
        ...

    @staticmethod
    def Min(left: System.Numerics.BigInteger, right: System.Numerics.BigInteger, ) -> System.Numerics.BigInteger:
        ...

    @staticmethod
    def ModPow(value: System.Numerics.BigInteger, exponent: System.Numerics.BigInteger, modulus: System.Numerics.BigInteger, ) -> System.Numerics.BigInteger:
        ...

    @staticmethod
    def Pow(value: System.Numerics.BigInteger, exponent: int, ) -> System.Numerics.BigInteger:
        ...

    def GetHashCode(self, ) -> int:
        ...

    @typing.overload
    def Equals(self, obj: System.Object, ) -> bool:
        ...

    @typing.overload
    def Equals(self, other: int, ) -> bool:
        ...

    @typing.overload
    def Equals(self, other: int, ) -> bool:
        ...

    @typing.overload
    def Equals(self, other: System.Numerics.BigInteger, ) -> bool:
        ...

    @typing.overload
    def CompareTo(self, other: int, ) -> int:
        ...

    @typing.overload
    def CompareTo(self, other: int, ) -> int:
        ...

    @typing.overload
    def CompareTo(self, other: System.Numerics.BigInteger, ) -> int:
        ...

    @typing.overload
    def CompareTo(self, obj: System.Object, ) -> int:
        ...

    @typing.overload
    def ToByteArray(self, ) -> System.Array[int]:
        ...

    @typing.overload
    def ToByteArray(self, isUnsigned: bool = ..., isBigEndian: bool = ..., ) -> System.Array[int]:
        ...

    def TryWriteBytes(self, destination: System.Span[int], bytesWritten: ref[int], isUnsigned: bool = ..., isBigEndian: bool = ..., ) -> bool:
        ...

    def TryWriteOrCountBytes(self, destination: System.Span[int], bytesWritten: ref[int], isUnsigned: bool = ..., isBigEndian: bool = ..., ) -> bool:
        ...

    def GetByteCount(self, isUnsigned: bool = ..., ) -> int:
        ...

    def TryGetBytes(self, mode: int, destination: System.Span[int], isUnsigned: bool, isBigEndian: bool, bytesWritten: ref[int], ) -> System.Array[int]:
        ...

    def ToUInt32Span(self, scratch: System.Span[int], ) -> System.ReadOnlySpan[int]:
        ...

    @typing.overload
    def ToString(self, ) -> str:
        ...

    @typing.overload
    def ToString(self, provider: System.IFormatProvider, ) -> str:
        ...

    @typing.overload
    def ToString(self, format: str, ) -> str:
        ...

    @typing.overload
    def ToString(self, format: str, provider: System.IFormatProvider, ) -> str:
        ...

    def TryFormat(self, destination: System.Span[str], charsWritten: ref[int], format: System.ReadOnlySpan[str] = ..., provider: System.IFormatProvider = ..., ) -> bool:
        ...

class Complex(System.IEquatable[System.Numerics.Complex], System.IFormattable, System.ValueType):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields
    Zero: System.Numerics.Complex = ...
    One: System.Numerics.Complex = ...
    ImaginaryOne: System.Numerics.Complex = ...
    NaN: System.Numerics.Complex = ...
    Infinity: System.Numerics.Complex = ...

    # properties
    @property
    def Real(self) -> float:
        ...

    @property
    def Imaginary(self) -> float:
        ...

    @property
    def Magnitude(self) -> float:
        ...

    @property
    def Phase(self) -> float:
        ...

    # methods
    def __init__(self, real: float, imaginary: float, ):
        ...

    @staticmethod
    def FromPolarCoordinates(magnitude: float, phase: float, ) -> System.Numerics.Complex:
        ...

    @staticmethod
    def Negate(value: System.Numerics.Complex, ) -> System.Numerics.Complex:
        ...

    @staticmethod
    @typing.overload
    def Add(left: System.Numerics.Complex, right: System.Numerics.Complex, ) -> System.Numerics.Complex:
        ...

    @staticmethod
    @typing.overload
    def Add(left: System.Numerics.Complex, right: float, ) -> System.Numerics.Complex:
        ...

    @staticmethod
    @typing.overload
    def Add(left: float, right: System.Numerics.Complex, ) -> System.Numerics.Complex:
        ...

    @staticmethod
    @typing.overload
    def Subtract(left: System.Numerics.Complex, right: System.Numerics.Complex, ) -> System.Numerics.Complex:
        ...

    @staticmethod
    @typing.overload
    def Subtract(left: System.Numerics.Complex, right: float, ) -> System.Numerics.Complex:
        ...

    @staticmethod
    @typing.overload
    def Subtract(left: float, right: System.Numerics.Complex, ) -> System.Numerics.Complex:
        ...

    @staticmethod
    @typing.overload
    def Multiply(left: System.Numerics.Complex, right: System.Numerics.Complex, ) -> System.Numerics.Complex:
        ...

    @staticmethod
    @typing.overload
    def Multiply(left: System.Numerics.Complex, right: float, ) -> System.Numerics.Complex:
        ...

    @staticmethod
    @typing.overload
    def Multiply(left: float, right: System.Numerics.Complex, ) -> System.Numerics.Complex:
        ...

    @staticmethod
    @typing.overload
    def Divide(dividend: System.Numerics.Complex, divisor: System.Numerics.Complex, ) -> System.Numerics.Complex:
        ...

    @staticmethod
    @typing.overload
    def Divide(dividend: System.Numerics.Complex, divisor: float, ) -> System.Numerics.Complex:
        ...

    @staticmethod
    @typing.overload
    def Divide(dividend: float, divisor: System.Numerics.Complex, ) -> System.Numerics.Complex:
        ...

    @staticmethod
    def Abs(value: System.Numerics.Complex, ) -> float:
        ...

    @staticmethod
    def Hypot(a: float, b: float, ) -> float:
        ...

    @staticmethod
    def Log1P(x: float, ) -> float:
        ...

    @staticmethod
    def Conjugate(value: System.Numerics.Complex, ) -> System.Numerics.Complex:
        ...

    @staticmethod
    def Reciprocal(value: System.Numerics.Complex, ) -> System.Numerics.Complex:
        ...

    @typing.overload
    def Equals(self, obj: System.Object, ) -> bool:
        ...

    @typing.overload
    def Equals(self, value: System.Numerics.Complex, ) -> bool:
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

    @staticmethod
    def Sin(value: System.Numerics.Complex, ) -> System.Numerics.Complex:
        ...

    @staticmethod
    def Sinh(value: System.Numerics.Complex, ) -> System.Numerics.Complex:
        ...

    @staticmethod
    def Asin(value: System.Numerics.Complex, ) -> System.Numerics.Complex:
        ...

    @staticmethod
    def Cos(value: System.Numerics.Complex, ) -> System.Numerics.Complex:
        ...

    @staticmethod
    def Cosh(value: System.Numerics.Complex, ) -> System.Numerics.Complex:
        ...

    @staticmethod
    def Acos(value: System.Numerics.Complex, ) -> System.Numerics.Complex:
        ...

    @staticmethod
    def Tan(value: System.Numerics.Complex, ) -> System.Numerics.Complex:
        ...

    @staticmethod
    def Tanh(value: System.Numerics.Complex, ) -> System.Numerics.Complex:
        ...

    @staticmethod
    def Atan(value: System.Numerics.Complex, ) -> System.Numerics.Complex:
        ...

    @staticmethod
    def Asin_Internal(x: float, y: float, b: ref[float], bPrime: ref[float], v: ref[float], ) -> None:
        ...

    @staticmethod
    def IsFinite(value: System.Numerics.Complex, ) -> bool:
        ...

    @staticmethod
    def IsInfinity(value: System.Numerics.Complex, ) -> bool:
        ...

    @staticmethod
    def IsNaN(value: System.Numerics.Complex, ) -> bool:
        ...

    @staticmethod
    @typing.overload
    def Log(value: System.Numerics.Complex, ) -> System.Numerics.Complex:
        ...

    @staticmethod
    @typing.overload
    def Log(value: System.Numerics.Complex, baseValue: float, ) -> System.Numerics.Complex:
        ...

    @staticmethod
    def Log10(value: System.Numerics.Complex, ) -> System.Numerics.Complex:
        ...

    @staticmethod
    def Exp(value: System.Numerics.Complex, ) -> System.Numerics.Complex:
        ...

    @staticmethod
    def Sqrt(value: System.Numerics.Complex, ) -> System.Numerics.Complex:
        ...

    @staticmethod
    @typing.overload
    def Pow(value: System.Numerics.Complex, power: System.Numerics.Complex, ) -> System.Numerics.Complex:
        ...

    @staticmethod
    @typing.overload
    def Pow(value: System.Numerics.Complex, power: float, ) -> System.Numerics.Complex:
        ...

    @staticmethod
    def Scale(value: System.Numerics.Complex, factor: float, ) -> System.Numerics.Complex:
        ...

