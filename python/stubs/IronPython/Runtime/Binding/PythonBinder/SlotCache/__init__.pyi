from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import System
import System.Collections.Generic
import IronPython.Runtime.Types
import Microsoft.Scripting.Actions
import IronPython.Runtime.Binding.PythonBinder.SlotCache


class SlotCacheInfo(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        self.Members: System.Collections.Generic.Dictionary[str, System.Collections.Generic.KeyValuePair[IronPython.Runtime.Types.PythonTypeSlot, Microsoft.Scripting.Actions.MemberGroup]]
        self.ResolvedAll: bool
        ...

    # static fields

    # properties
    # methods
    def __init__(self, ):
        ...

    def TryGetSlot(self, name: str, slot: ref[IronPython.Runtime.Types.PythonTypeSlot], ) -> bool:
        ...

    def TryGetMember(self, name: str, group: ref[Microsoft.Scripting.Actions.MemberGroup], ) -> bool:
        ...

    def GetAllSlots(self, ) -> System.Collections.Generic.IEnumerable[System.Collections.Generic.KeyValuePair[str, IronPython.Runtime.Types.PythonTypeSlot]]:
        ...

class CachedInfoKey(System.IEquatable[IronPython.Runtime.Binding.PythonBinder.SlotCache.CachedInfoKey], System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        self.Type: System.Type
        self.IsGetMember: bool
        ...

    # static fields

    # properties
    # methods
    def __init__(self, type: System.Type, isGetMember: bool, ):
        ...

    @typing.overload
    def Equals(self, other: IronPython.Runtime.Binding.PythonBinder.SlotCache.CachedInfoKey, ) -> bool:
        ...

    @typing.overload
    def Equals(self, obj: System.Object, ) -> bool:
        ...

    def GetHashCode(self, ) -> int:
        ...

