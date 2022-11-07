from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import System
import IronPython.Runtime.ExtensionMethodSet
import System.Collections.Generic
import IronPython.Runtime.Types
import System.Reflection


class AssemblyLoadInfo(System.IEquatable[IronPython.Runtime.ExtensionMethodSet.AssemblyLoadInfo], System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        self.Types: System.Collections.Generic.HashSet[IronPython.Runtime.Types.PythonType]
        self.Namespaces: System.Collections.Generic.HashSet[str]
        self.IsFullAssemblyLoaded: bool
        ...

    # static fields

    # properties
    # methods
    def __init__(self, asm: System.Reflection.Assembly, ):
        ...

    def GetHashCode(self, ) -> int:
        ...

    @typing.overload
    def Equals(self, obj: System.Object, ) -> bool:
        ...

    @typing.overload
    def Equals(self, other: IronPython.Runtime.ExtensionMethodSet.AssemblyLoadInfo, ) -> bool:
        ...

    def EnsureTypesLoaded(self, ) -> IronPython.Runtime.ExtensionMethodSet.AssemblyLoadInfo:
        ...

