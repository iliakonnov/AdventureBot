from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import System
import IronPython.Runtime.Types
import Microsoft.Scripting.Actions
import System.Collections.Generic
import IronPython.Runtime.Binding.PythonBinder.SlotCache


class SlotCache(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    def __init__(self, ):
        ...

    def CacheSlot(self, type: System.Type, isGetMember: bool, name: str, slot: IronPython.Runtime.Types.PythonTypeSlot, memberGroup: Microsoft.Scripting.Actions.MemberGroup, ) -> None:
        ...

    def TryGetCachedSlot(self, type: System.Type, isGetMember: bool, name: str, slot: ref[IronPython.Runtime.Types.PythonTypeSlot], ) -> bool:
        ...

    def TryGetCachedMember(self, type: System.Type, name: str, getMemberAction: bool, group: ref[Microsoft.Scripting.Actions.MemberGroup], ) -> bool:
        ...

    def IsFullyCached(self, type: System.Type, isGetMember: bool, ) -> bool:
        ...

    def CacheAll(self, type: System.Type, isGetMember: bool, members: System.Collections.Generic.Dictionary[str, System.Collections.Generic.KeyValuePair[IronPython.Runtime.Types.PythonTypeSlot, Microsoft.Scripting.Actions.MemberGroup]], ) -> None:
        ...

    def GetAllMembers(self, type: System.Type, isGetMember: bool, ) -> System.Collections.Generic.IEnumerable[System.Collections.Generic.KeyValuePair[str, IronPython.Runtime.Types.PythonTypeSlot]]:
        ...

    def GetSlotForType(self, type: System.Type, isGetMember: bool, ) -> IronPython.Runtime.Binding.PythonBinder.SlotCache.SlotCacheInfo:
        ...

    def EnsureInfo(self, ) -> None:
        ...

class ExtensionTypeInfo(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        self.ExtensionType: System.Type
        self.PythonName: str
        ...

    # static fields

    # properties
    # methods
    def __init__(self, extensionType: System.Type, pythonName: str, ):
        ...

