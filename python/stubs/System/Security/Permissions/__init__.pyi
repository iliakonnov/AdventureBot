from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import System


class PermissionState(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    None_: int = ...
    Unrestricted: int = ...

