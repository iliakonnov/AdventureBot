from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import System
import IronPython.Runtime.Types
import IronPython.Runtime


class SlotAccessDelegate(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def Type(self) -> IronPython.Runtime.Types.PythonType:
        ...

    @property
    def Slot(self) -> IronPython.Runtime.Types.PythonTypeSlot:
        ...

    # methods
    def __init__(self, slot: IronPython.Runtime.Types.PythonTypeSlot, owner: IronPython.Runtime.Types.PythonType, ):
        ...

    def TargetCheckCls(self, context: IronPython.Runtime.CodeContext, self: System.Object, result: ref[System.Object], ) -> bool:
        ...

    def Target(self, context: IronPython.Runtime.CodeContext, self: System.Object, result: ref[System.Object], ) -> bool:
        ...

    def MetaTargetCheckCls(self, context: IronPython.Runtime.CodeContext, self: System.Object, result: ref[System.Object], ) -> bool:
        ...

    def MetaTarget(self, context: IronPython.Runtime.CodeContext, self: System.Object, result: ref[System.Object], ) -> bool:
        ...

class MetaGetAttributeDelegate(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def MetaType(self) -> IronPython.Runtime.Types.PythonType:
        ...

    @property
    def Slot(self) -> IronPython.Runtime.Types.PythonTypeSlot:
        ...

    # methods
    def __init__(self, context: IronPython.Runtime.CodeContext, slot: IronPython.Runtime.Types.PythonTypeSlot, metaType: IronPython.Runtime.Types.PythonType, name: str, ):
        ...

    def Target(self, context: IronPython.Runtime.CodeContext, self: System.Object, result: ref[System.Object], ) -> bool:
        ...

class ErrorBinder(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    def __init__(self, name: str, ):
        ...

    def TargetNoThrow(self, context: IronPython.Runtime.CodeContext, self: System.Object, result: ref[System.Object], ) -> bool:
        ...

    def Target(self, context: IronPython.Runtime.CodeContext, self: System.Object, result: ref[System.Object], ) -> bool:
        ...

