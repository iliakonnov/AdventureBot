from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import System
import IronPython.Modules.PythonLocale
import System.Globalization
import IronPython.Runtime


class SortKeyWrapper(System.IComparable[IronPython.Modules.PythonLocale.SortKeyWrapper], System.IComparable, System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def SortKey(self) -> System.Globalization.SortKey:
        ...

    # methods
    def __init__(self, sortKey: System.Globalization.SortKey, ):
        ...

    @typing.overload
    def CompareTo(self, other: IronPython.Modules.PythonLocale.SortKeyWrapper, ) -> int:
        ...

    @typing.overload
    def CompareTo(self, other: System.Object, ) -> int:
        ...

class LocaleCategories(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    All: int = ...
    Collate: int = ...
    CType: int = ...
    Monetary: int = ...
    Numeric: int = ...
    Time: int = ...

class LocaleInfo(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def Collate(self) -> System.Globalization.CultureInfo:
        ...
    @Collate.setter
    def Collate(self, val: System.Globalization.CultureInfo):
        ...

    @property
    def CType(self) -> System.Globalization.CultureInfo:
        ...
    @CType.setter
    def CType(self, val: System.Globalization.CultureInfo):
        ...

    @property
    def Time(self) -> System.Globalization.CultureInfo:
        ...
    @Time.setter
    def Time(self, val: System.Globalization.CultureInfo):
        ...

    @property
    def Monetary(self) -> System.Globalization.CultureInfo:
        ...
    @Monetary.setter
    def Monetary(self, val: System.Globalization.CultureInfo):
        ...

    @property
    def Numeric(self) -> System.Globalization.CultureInfo:
        ...
    @Numeric.setter
    def Numeric(self, val: System.Globalization.CultureInfo):
        ...

    # methods
    def __init__(self, context: IronPython.Runtime.PythonContext, ):
        ...

    def ToString(self, ) -> str:
        ...

    def GetConventionsTable(self, ) -> IronPython.Runtime.PythonDictionary:
        ...

    def SetLocale(self, context: IronPython.Runtime.CodeContext, category: int, locale: str, ) -> str:
        ...

    def GetLocale(self, context: IronPython.Runtime.CodeContext, category: int, ) -> str:
        ...

    def CultureToName(self, culture: System.Globalization.CultureInfo, ) -> str:
        ...

    def LocaleToCulture(self, context: IronPython.Runtime.CodeContext, locale: str, ) -> System.Globalization.CultureInfo:
        ...

    def CreateConventionsDict(self, ) -> None:
        ...

    @staticmethod
    def GroupsToList(groups: System.Array[int], ) -> IronPython.Runtime.PythonList:
        ...

