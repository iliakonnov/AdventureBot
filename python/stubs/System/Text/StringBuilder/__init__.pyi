from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import System
import System.Text
import System.Text.StringBuilder

T = typing.TypeVar('T')

class AppendInterpolatedStringHandler(System.ValueType):
    @typing.overload
    def __init__(self, **kwargs):
        self._stringBuilder: System.Text.StringBuilder
        ...

    # static fields

    # properties
    # methods
    @typing.overload
    def __init__(self, literalLength: int, formattedCount: int, stringBuilder: System.Text.StringBuilder, ):
        ...

    @typing.overload
    def __init__(self, literalLength: int, formattedCount: int, stringBuilder: System.Text.StringBuilder, provider: System.IFormatProvider, ):
        ...

    def AppendLiteral(self, value: str, ) -> None:
        ...

    @typing.overload
    def AppendFormatted(self, value: T, ) -> None:
        ...

    @typing.overload
    def AppendFormatted(self, value: T, format: str, ) -> None:
        ...

    @typing.overload
    def AppendFormatted(self, value: T, alignment: int, ) -> None:
        ...

    @typing.overload
    def AppendFormatted(self, value: T, alignment: int, format: str, ) -> None:
        ...

    @typing.overload
    def AppendFormatted(self, value: System.ReadOnlySpan[str], ) -> None:
        ...

    @typing.overload
    def AppendFormatted(self, value: System.ReadOnlySpan[str], alignment: int = ..., format: str = ..., ) -> None:
        ...

    @typing.overload
    def AppendFormatted(self, value: str, ) -> None:
        ...

    @typing.overload
    def AppendFormatted(self, value: str, alignment: int = ..., format: str = ..., ) -> None:
        ...

    @typing.overload
    def AppendFormatted(self, value: System.Object, alignment: int = ..., format: str = ..., ) -> None:
        ...

    def AppendFormattedWithTempSpace(self, value: T, alignment: int, format: str, ) -> None:
        ...

    def AppendCustomFormatter(self, value: T, format: str, ) -> None:
        ...

class ChunkEnumerator(System.ValueType):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def Current(self) -> System.ReadOnlyMemory[str]:
        ...

    # methods
    def __init__(self, stringBuilder: System.Text.StringBuilder, ):
        ...

    def GetEnumerator(self, ) -> System.Text.StringBuilder.ChunkEnumerator:
        ...

    def MoveNext(self, ) -> bool:
        ...

    @staticmethod
    def ChunkCount(stringBuilder: System.Text.StringBuilder, ) -> int:
        ...

