from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import System


class AssemblyHashAlgorithm(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    None_: System.Int32 = None
    MD5: System.Int32 = MD5
    SHA1: System.Int32 = SHA1
    SHA256: System.Int32 = SHA256
    SHA384: System.Int32 = SHA384
    SHA512: System.Int32 = SHA512

class AssemblyVersionCompatibility(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    SameMachine: System.Int32 = SameMachine
    SameProcess: System.Int32 = SameProcess
    SameDomain: System.Int32 = SameDomain

