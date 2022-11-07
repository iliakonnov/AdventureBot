from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import System


class PlatformFamily(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    Windows: int = ...
    Unix: int = ...

