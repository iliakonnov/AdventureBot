from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import System
import IronPython.Compiler.Tokenizer
import System.Text
import System.Collections.Generic
import IronPython.Compiler


class State(System.IEquatable[IronPython.Compiler.Tokenizer.State], System.ValueType):
    @typing.overload
    def __init__(self, **kwargs):
        self.Indent: System.Array[int]
        self.IndentLevel: int
        self.PendingDedents: int
        self.LastNewLine: bool
        self.IncompleteString: IronPython.Compiler.Tokenizer.IncompleteString
        self.IndentFormat: System.Array[System.Text.StringBuilder]
        self.ParenLevel: int
        self.BraceLevel: int
        self.BracketLevel: int
        ...

    # static fields

    # properties
    # methods
    @typing.overload
    def __init__(self, state: IronPython.Compiler.Tokenizer.State, ):
        ...

    @typing.overload
    def __init__(self, dummy: System.Object, ):
        ...

    @typing.overload
    def Equals(self, obj: System.Object, ) -> bool:
        ...

    @typing.overload
    def Equals(self, other: IronPython.Compiler.Tokenizer.State, ) -> bool:
        ...

    def GetHashCode(self, ) -> int:
        ...

class IncompleteString(System.IEquatable[IronPython.Compiler.Tokenizer.IncompleteString], System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        self.IsRaw: bool
        self.IsUnicode: bool
        self.IsTripleQuoted: bool
        self.IsSingleTickQuote: bool
        ...

    # static fields

    # properties
    # methods
    def __init__(self, isSingleTickQuote: bool, isRaw: bool, isUnicode: bool, isTriple: bool, ):
        ...

    @typing.overload
    def Equals(self, obj: System.Object, ) -> bool:
        ...

    @typing.overload
    def Equals(self, other: IronPython.Compiler.Tokenizer.IncompleteString, ) -> bool:
        ...

    def GetHashCode(self, ) -> int:
        ...

class TokenEqualityComparer(System.Collections.Generic.IEqualityComparer[System.Object], System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    def __init__(self, tokenizer: IronPython.Compiler.Tokenizer, ):
        ...

    def Equals(self, x: System.Object, y: System.Object, ) -> bool:
        ...

    def GetHashCode(self, obj: System.Object, ) -> int:
        ...

    def Equals(self, value: str, ) -> bool:
        ...

