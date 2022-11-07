from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import System


class GetBytesMode(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    AllocateArray: int = ...
    Count: int = ...
    Span: int = ...

