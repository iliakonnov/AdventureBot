from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import System
import System.Decimal
import System.Decimal.DecCalc


class DecCalc(System.ValueType):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def High(self) -> int:
        ...
    @High.setter
    def High(self, val: int):
        ...

    @property
    def Low(self) -> int:
        ...
    @Low.setter
    def Low(self, val: int):
        ...

    @property
    def Mid(self) -> int:
        ...
    @Mid.setter
    def Mid(self, val: int):
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
    @Low64.setter
    def Low64(self, val: int):
        ...

    # methods
    @staticmethod
    @typing.overload
    def GetExponent(f: float, ) -> int:
        ...

    @staticmethod
    @typing.overload
    def GetExponent(d: float, ) -> int:
        ...

    @staticmethod
    def UInt32x32To64(a: int, b: int, ) -> int:
        ...

    @staticmethod
    def UInt64x64To128(a: int, b: int, result: ref[System.Decimal.DecCalc], ) -> None:
        ...

    @staticmethod
    def Div96By32(bufNum: ref[System.Decimal.DecCalc.Buf12], den: int, ) -> int:
        ...

    @staticmethod
    def Div96ByConst(high64: ref[int], low: ref[int], pow: int, ) -> bool:
        ...

    @staticmethod
    def Unscale(low: ref[int], high64: ref[int], scale: ref[int], ) -> None:
        ...

    @staticmethod
    def Div96By64(bufNum: ref[System.Decimal.DecCalc.Buf12], den: int, ) -> int:
        ...

    @staticmethod
    def Div128By96(bufNum: ref[System.Decimal.DecCalc.Buf16], bufDen: ref[System.Decimal.DecCalc.Buf12], ) -> int:
        ...

    @staticmethod
    def IncreaseScale(bufNum: ref[System.Decimal.DecCalc.Buf12], power: int, ) -> int:
        ...

    @staticmethod
    def IncreaseScale64(bufNum: ref[System.Decimal.DecCalc.Buf12], power: int, ) -> None:
        ...

    @staticmethod
    def ScaleResult(bufRes: ptr[System.Decimal.DecCalc.Buf24], hiRes: int, scale: int, ) -> int:
        ...

    @staticmethod
    def DivByConst(result: ptr[int], hiRes: int, quotient: ref[int], remainder: ref[int], power: int, ) -> int:
        ...

    @staticmethod
    def OverflowUnscale(bufQuo: ref[System.Decimal.DecCalc.Buf12], scale: int, sticky: bool, ) -> int:
        ...

    @staticmethod
    def SearchScale(bufQuo: ref[System.Decimal.DecCalc.Buf12], scale: int, ) -> int:
        ...

    @staticmethod
    def Add32To96(bufNum: ref[System.Decimal.DecCalc.Buf12], value: int, ) -> bool:
        ...

    @staticmethod
    def DecAddSub(d1: ref[System.Decimal.DecCalc], d2: ref[System.Decimal.DecCalc], sign: bool, ) -> None:
        ...

    @staticmethod
    def VarCyFromDec(pdecIn: ref[System.Decimal.DecCalc], ) -> int:
        ...

    @staticmethod
    def VarDecCmp(d1: ref[System.Decimal], d2: ref[System.Decimal], ) -> int:
        ...

    @staticmethod
    def VarDecCmpSub(d1: ref[System.Decimal], d2: ref[System.Decimal], ) -> int:
        ...

    @staticmethod
    def VarDecMul(d1: ref[System.Decimal.DecCalc], d2: ref[System.Decimal.DecCalc], ) -> None:
        ...

    @staticmethod
    def VarDecFromR4(input: float, result: ref[System.Decimal.DecCalc], ) -> None:
        ...

    @staticmethod
    def VarDecFromR8(input: float, result: ref[System.Decimal.DecCalc], ) -> None:
        ...

    @staticmethod
    def VarR4FromDec(value: ref[System.Decimal], ) -> float:
        ...

    @staticmethod
    def VarR8FromDec(value: ref[System.Decimal], ) -> float:
        ...

    @staticmethod
    def GetHashCode(d: ref[System.Decimal], ) -> int:
        ...

    @staticmethod
    def VarDecDiv(d1: ref[System.Decimal.DecCalc], d2: ref[System.Decimal.DecCalc], ) -> None:
        ...

    @staticmethod
    def VarDecMod(d1: ref[System.Decimal.DecCalc], d2: ref[System.Decimal.DecCalc], ) -> None:
        ...

    @staticmethod
    def VarDecModFull(d1: ref[System.Decimal.DecCalc], d2: ref[System.Decimal.DecCalc], scale: int, ) -> None:
        ...

    @staticmethod
    def InternalRound(d: ref[System.Decimal.DecCalc], scale: int, mode: int, ) -> None:
        ...

    @staticmethod
    def DecDivMod1E9(value: ref[System.Decimal.DecCalc], ) -> int:
        ...

