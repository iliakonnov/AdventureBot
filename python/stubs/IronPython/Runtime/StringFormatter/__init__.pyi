from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import System


class FormatOptions(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    ZeroPad: int = ...
    LeftAdj: int = ...
    AltForm: int = ...
    Space: int = ...
    SignChar: int = ...

class FormatSettings(System.ValueType):
    @typing.overload
    def __init__(self, **kwargs):
        self.Options: int
        self.FieldWidth: int
        self.Precision: int
        self.Value: System.Object
        ...

    # static fields

    # properties
    @property
    def ZeroPad(self) -> bool:
        ...
    @ZeroPad.setter
    def ZeroPad(self, val: bool):
        ...

    @property
    def LeftAdj(self) -> bool:
        ...
    @LeftAdj.setter
    def LeftAdj(self, val: bool):
        ...

    @property
    def AltForm(self) -> bool:
        ...
    @AltForm.setter
    def AltForm(self, val: bool):
        ...

    @property
    def Space(self) -> bool:
        ...
    @Space.setter
    def Space(self, val: bool):
        ...

    @property
    def SignChar(self) -> bool:
        ...
    @SignChar.setter
    def SignChar(self, val: bool):
        ...

    # methods
