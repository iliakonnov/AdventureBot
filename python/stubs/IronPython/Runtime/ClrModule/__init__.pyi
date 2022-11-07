from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import System
import IronPython.Runtime.Types
import IronPython.Runtime
import Microsoft.Scripting
import System.IO
import System.Collections.Generic
import System.Reflection
import System.Collections


class ReturnChecker(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        self.retType: System.Object
        ...

    # static fields

    # properties
    # methods
    def __init__(self, returnType: System.Object, ):
        ...

class RuntimeArgChecker(IronPython.Runtime.Types.PythonTypeSlot):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def GetAlwaysSucceeds(self) -> bool:
        ...

    @property
    def IsAlwaysVisible(self) -> bool:
        ...

    @property
    def CanOptimizeGets(self) -> bool:
        ...

    # methods
    @typing.overload
    def __init__(self, function: System.Object, expectedArgs: System.Array[System.Object], ):
        ...

    @typing.overload
    def __init__(self, instance: System.Object, function: System.Object, expectedArgs: System.Array[System.Object], ):
        ...

    def ValidateArgs(self, args: System.Array[System.Object], ) -> None:
        ...

    def TryGetValue(self, context: IronPython.Runtime.CodeContext, instance: System.Object, owner: IronPython.Runtime.Types.PythonType, value: ref[System.Object], ) -> bool:
        ...

class RuntimeReturnChecker(IronPython.Runtime.Types.PythonTypeSlot):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def GetAlwaysSucceeds(self) -> bool:
        ...

    @property
    def IsAlwaysVisible(self) -> bool:
        ...

    @property
    def CanOptimizeGets(self) -> bool:
        ...

    # methods
    @typing.overload
    def __init__(self, function: System.Object, expectedReturn: System.Object, ):
        ...

    @typing.overload
    def __init__(self, instance: System.Object, function: System.Object, expectedReturn: System.Object, ):
        ...

    def ValidateReturn(self, ret: System.Object, ) -> None:
        ...

    def GetAttribute(self, instance: System.Object, owner: System.Object, ) -> System.Object:
        ...

    def TryGetValue(self, context: IronPython.Runtime.CodeContext, instance: System.Object, owner: IronPython.Runtime.Types.PythonType, value: ref[System.Object], ) -> bool:
        ...

class FileStreamContentProvider(Microsoft.Scripting.StreamContentProvider):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def Path(self) -> str:
        ...

    # methods
    def __init__(self, manager: Microsoft.Scripting.PlatformAdaptationLayer, path: str, ):
        ...

    def GetStream(self, ) -> System.IO.Stream:
        ...

class ArgChecker(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    def __init__(self, prms: System.Array[System.Object], ):
        ...

class ReferencesList(System.Collections.Generic.IList[System.Reflection.Assembly], System.Collections.Generic.ICollection[System.Reflection.Assembly], System.Collections.Generic.IEnumerable[System.Reflection.Assembly], System.Collections.IEnumerable, System.Collections.IList, System.Collections.ICollection, System.Collections.Generic.IReadOnlyList[System.Reflection.Assembly], System.Collections.Generic.IReadOnlyCollection[System.Reflection.Assembly], IronPython.Runtime.ICodeFormattable, System.Collections.Generic.List[System.Reflection.Assembly]):
    @typing.overload
    def __init__(self, **kwargs):
        self._items: System.Array[System.Reflection.Assembly]
        self._size: int
        ...

    # static fields

    # properties
    @property
    def Capacity(self) -> int:
        ...
    @Capacity.setter
    def Capacity(self, val: int):
        ...

    @property
    def Count(self) -> int:
        ...

    @property
    def Item(self) -> System.Reflection.Assembly:
        ...
    @Item.setter
    def Item(self, val: System.Reflection.Assembly):
        ...

    # methods
    def __init__(self, ):
        ...

    def Add(self, other: System.Reflection.Assembly, ) -> None:
        ...

    def __repr__(self, context: IronPython.Runtime.CodeContext, ) -> str:
        ...

