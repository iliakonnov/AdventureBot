from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import System
import System.Collections.Generic
import IronPython.Runtime.NewStringFormatter
import IronPython.Runtime


class FieldName(System.ValueType):
    @typing.overload
    def __init__(self, **kwargs):
        self.ArgumentName: str
        self.Accessors: System.Collections.Generic.IEnumerable[IronPython.Runtime.NewStringFormatter.FieldAccessor]
        ...

    # static fields

    # properties
    # methods
    def __init__(self, argumentName: str, accessors: System.Collections.Generic.IEnumerable[IronPython.Runtime.NewStringFormatter.FieldAccessor], ):
        ...

class StringFormatParser(System.ValueType):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    def __init__(self, text: str, ):
        ...

    @staticmethod
    @typing.overload
    def Parse(text: str, ) -> System.Collections.Generic.IEnumerable[IronPython.Runtime.PythonTuple]:
        ...

    @typing.overload
    def Parse(self, ) -> System.Collections.Generic.IEnumerable[IronPython.Runtime.PythonTuple]:
        ...

    def ParseFormat(self, lastTextStart: int, ) -> IronPython.Runtime.PythonTuple:
        ...

    def ParseDoubleBracket(self, lastTextStart: int, text: ref[str], ) -> bool:
        ...

    def ParseConversion(self, ) -> str:
        ...

    def CheckEnd(self, ) -> bool:
        ...

    def ParseFormatSpec(self, depth: ref[int], ) -> str:
        ...

    def ParseFieldName(self, depth: ref[int], ) -> str:
        ...

    def ParseFieldOrSpecWorker(self, ends: System.Array[str], depth: ref[int], ) -> str:
        ...

class FieldAccessor(System.ValueType):
    @typing.overload
    def __init__(self, **kwargs):
        self.AttributeName: str
        self.IsField: bool
        ...

    # static fields

    # properties
    # methods
    def __init__(self, attributeName: str, isField: bool, ):
        ...

class Formatter(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    def __init__(self, context: IronPython.Runtime.PythonContext, args: IronPython.Runtime.PythonTuple, kwArgs: System.Collections.Generic.IDictionary[System.Object, System.Object], ):
        ...

    @staticmethod
    def FormatString(context: IronPython.Runtime.PythonContext, format: str, args: IronPython.Runtime.PythonTuple, kwArgs: System.Collections.Generic.IDictionary[System.Object, System.Object], ) -> str:
        ...

    def ReplaceText(self, format: str, ) -> str:
        ...

    def ReplaceComputedFormats(self, formatSpec: str, ) -> str:
        ...

    def GetArgumentValue(self, fieldName: IronPython.Runtime.NewStringFormatter.FieldName, ) -> System.Object:
        ...

    def ApplyConversion(self, conversion: System.Nullable[str], argValue: System.Object, ) -> System.Object:
        ...

    def GetUnaccessedObject(self, fieldName: IronPython.Runtime.NewStringFormatter.FieldName, ) -> System.Object:
        ...

    def DoAccessors(self, fieldName: IronPython.Runtime.NewStringFormatter.FieldName, argValue: System.Object, ) -> System.Object:
        ...

