from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import System
import System.Text.StringBuilder
import System.Text

T = typing.TypeVar('T')

class ChunkEnumerator(System.ValueType):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def Current(self) -> System.ReadOnlyMemory[System.Char]:
        ...

    # methods
    @typing.overload
    def GetEnumerator(self, ) -> System.Text.StringBuilder.ChunkEnumerator:
        ...

    @typing.overload
    def MoveNext(self, ) -> System.Boolean:
        ...

class AppendInterpolatedStringHandler(System.ValueType):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    # methods
    @typing.overload
    def __init__(self, literalLength: System.Int32, formattedCount: System.Int32, stringBuilder: System.Text.StringBuilder, ):
        ...

    @typing.overload
    def __init__(self, literalLength: System.Int32, formattedCount: System.Int32, stringBuilder: System.Text.StringBuilder, provider: System.IFormatProvider, ):
        ...

    @typing.overload
    def AppendLiteral(self, value: System.String, ) -> None:
        ...

    @typing.overload
    def AppendFormatted(self, value: T, ) -> None:
        ...

    @typing.overload
    def AppendFormatted(self, value: T, format: System.String, ) -> None:
        ...

    @typing.overload
    def AppendFormatted(self, value: T, alignment: System.Int32, ) -> None:
        ...

    @typing.overload
    def AppendFormatted(self, value: T, alignment: System.Int32, format: System.String, ) -> None:
        ...

    @typing.overload
    def AppendFormatted(self, value: System.ReadOnlySpan[System.Char], ) -> None:
        ...

    @typing.overload
    def AppendFormatted(self, value: System.ReadOnlySpan[System.Char], alignment: System.Int32, format: System.String, ) -> None:
        ...

    @typing.overload
    def AppendFormatted(self, value: System.String, ) -> None:
        ...

    @typing.overload
    def AppendFormatted(self, value: System.String, alignment: System.Int32, format: System.String, ) -> None:
        ...

    @typing.overload
    def AppendFormatted(self, value: System.Object, alignment: System.Int32, format: System.String, ) -> None:
        ...

