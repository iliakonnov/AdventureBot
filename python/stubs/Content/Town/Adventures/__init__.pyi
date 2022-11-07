from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import System


class RoomSelectionMessage(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    Next: int = ...
    Select: int = ...

