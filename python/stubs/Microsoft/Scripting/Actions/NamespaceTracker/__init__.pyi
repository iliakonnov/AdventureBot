from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import System
import System.Reflection
import Microsoft.Scripting.Actions
import System.Collections.Generic


class TypeNames(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    def __init__(self, assembly: System.Reflection.Assembly, fullNamespace: str, ):
        ...

    def Contains(self, normalizedTypeName: str, ) -> bool:
        ...

    def UpdateTypeEntity(self, existingTypeEntity: Microsoft.Scripting.Actions.TypeTracker, normalizedTypeName: str, ) -> Microsoft.Scripting.Actions.MemberTracker:
        ...

    def AddTypeName(self, typeName: str, ) -> None:
        ...

    def GetFullChildName(self, childName: str, ) -> str:
        ...

    def GetNormalizedTypeNames(self, ) -> System.Collections.Generic.ICollection[str]:
        ...

