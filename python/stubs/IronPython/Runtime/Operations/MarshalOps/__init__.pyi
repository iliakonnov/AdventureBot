from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import System
import System.Collections.Generic
import System.Text
import System.Numerics
import IronPython.Runtime


class MarshalReader(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    def __init__(self, bytes: System.Collections.Generic.IEnumerator[int], ):
        ...

    def ReadObject(self, ) -> System.Object:
        ...

    def PushStack(self, type: int, ) -> None:
        ...

    def UpdateStack(self, res: System.Object, ) -> System.Object:
        ...

    def YieldSimple(self, ) -> System.Object:
        ...

    def ReadBytes(self, len: int, ) -> System.Array[int]:
        ...

    def ReadInt32(self, ) -> int:
        ...

    def ReadFloatStr(self, ) -> float:
        ...

    def MoveNext(self, ) -> None:
        ...

    def DecodeString(self, enc: System.Text.Encoding, bytes: System.Array[int], ) -> str:
        ...

    def ReadInt(self, ) -> System.Object:
        ...

    def ReadIntPart(self, ) -> int:
        ...

    def ReadFloat(self, ) -> System.Object:
        ...

    def ReadBinaryFloat(self, ) -> System.Object:
        ...

    def ReadAsciiString(self, ) -> System.Object:
        ...

    def ReadUnicodeString(self, ) -> System.Object:
        ...

    def ReadComplex(self, ) -> System.Object:
        ...

    def ReadBuffer(self, ) -> System.Object:
        ...

    def ReadLong(self, ) -> System.Object:
        ...

    def ReadBigInteger(self, ) -> System.Object:
        ...

class MarshalWriter(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    def __init__(self, version: int, ):
        ...

    def WriteObject(self, o: System.Object, ) -> None:
        ...

    @typing.overload
    def WriteFloat(self, f: float, ) -> None:
        ...

    @typing.overload
    def WriteFloat(self, f: float, ) -> None:
        ...

    def WriteDoubleString(self, d: float, ) -> None:
        ...

    def WriteInteger(self, val: System.Numerics.BigInteger, ) -> None:
        ...

    def WriteLong(self, l: int, ) -> None:
        ...

    def WriteComplex(self, val: System.Numerics.Complex, ) -> None:
        ...

    def WriteStopIteration(self, ) -> None:
        ...

    def WriteInt(self, val: int, ) -> None:
        ...

    def WriteInt32(self, val: int, ) -> None:
        ...

    def WriteBufferProtocol(self, b: IronPython.Runtime.IBufferProtocol, ) -> None:
        ...

    def WriteString(self, s: str, ) -> None:
        ...

    def WriteList(self, o: System.Object, ) -> None:
        ...

    def WriteDict(self, o: System.Object, ) -> None:
        ...

    def WriteTuple(self, o: System.Object, ) -> None:
        ...

    def WriteSet(self, set: System.Object, ) -> None:
        ...

    def WriteFrozenSet(self, set: System.Object, ) -> None:
        ...

    def GetBytes(self, ) -> System.Array[int]:
        ...

