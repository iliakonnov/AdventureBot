from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import System
import System.Security
import System.Runtime.InteropServices
import System.Collections
import System.Runtime.Serialization


class SecurityRuleSet(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    None_: int = ...
    Level1: int = ...
    Level2: int = ...

class SecureString(System.IDisposable, System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def Length(self) -> int:
        ...

    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def __init__(self, value: ptr[str], length: int, ):
        ...

    @typing.overload
    def __init__(self, str: System.Security.SecureString, ):
        ...

    def Initialize(self, value: System.ReadOnlySpan[str], ) -> None:
        ...

    def EnsureCapacity(self, capacity: int, ) -> None:
        ...

    def AppendChar(self, c: str, ) -> None:
        ...

    def Clear(self, ) -> None:
        ...

    def Copy(self, ) -> System.Security.SecureString:
        ...

    def Dispose(self, ) -> None:
        ...

    def InsertAt(self, index: int, c: str, ) -> None:
        ...

    def IsReadOnly(self, ) -> bool:
        ...

    def MakeReadOnly(self, ) -> None:
        ...

    def RemoveAt(self, index: int, ) -> None:
        ...

    def SetAt(self, index: int, c: str, ) -> None:
        ...

    def AcquireSpan(self, bufferToRelease: ref[System.Runtime.InteropServices.SafeBuffer], ) -> System.Span[str]:
        ...

    def EnsureNotReadOnly(self, ) -> None:
        ...

    def EnsureNotDisposed(self, ) -> None:
        ...

    def MarshalToBSTR(self, ) -> System.IntPtr:
        ...

    def MarshalToString(self, globalAlloc: bool, unicode: bool, ) -> System.IntPtr:
        ...

    @staticmethod
    def GetAlignedByteSize(length: int, ) -> int:
        ...

    def ProtectMemory(self, ) -> None:
        ...

    def UnprotectMemory(self, ) -> None:
        ...

class PermissionSet(System.Collections.ICollection, System.Collections.IEnumerable, System.Runtime.Serialization.IDeserializationCallback, System.Security.ISecurityEncodable, System.Security.IStackWalk, System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def Count(self) -> int:
        ...

    @property
    def IsReadOnly(self) -> bool:
        ...

    @property
    def IsSynchronized(self) -> bool:
        ...

    @property
    def SyncRoot(self) -> System.Object:
        ...

    # methods
    @typing.overload
    def __init__(self, state: int, ):
        ...

    @typing.overload
    def __init__(self, permSet: System.Security.PermissionSet, ):
        ...

    def AddPermission(self, perm: System.Security.IPermission, ) -> System.Security.IPermission:
        ...

    def AddPermissionImpl(self, perm: System.Security.IPermission, ) -> System.Security.IPermission:
        ...

    def Assert(self, ) -> None:
        ...

    def ContainsNonCodeAccessPermissions(self, ) -> bool:
        ...

    @staticmethod
    def ConvertPermissionSet(inFormat: str, inData: System.Array[int], outFormat: str, ) -> System.Array[int]:
        ...

    def Copy(self, ) -> System.Security.PermissionSet:
        ...

    def CopyTo(self, array: System.Array, index: int, ) -> None:
        ...

    def Demand(self, ) -> None:
        ...

    def Deny(self, ) -> None:
        ...

    def Equals(self, o: System.Object, ) -> bool:
        ...

    def FromXml(self, et: System.Security.SecurityElement, ) -> None:
        ...

    def GetEnumerator(self, ) -> System.Collections.IEnumerator:
        ...

    def GetEnumeratorImpl(self, ) -> System.Collections.IEnumerator:
        ...

    def GetHashCode(self, ) -> int:
        ...

    def GetPermission(self, permClass: System.Type, ) -> System.Security.IPermission:
        ...

    def GetPermissionImpl(self, permClass: System.Type, ) -> System.Security.IPermission:
        ...

    def Intersect(self, other: System.Security.PermissionSet, ) -> System.Security.PermissionSet:
        ...

    def IsEmpty(self, ) -> bool:
        ...

    def IsSubsetOf(self, target: System.Security.PermissionSet, ) -> bool:
        ...

    def IsUnrestricted(self, ) -> bool:
        ...

    def PermitOnly(self, ) -> None:
        ...

    def RemovePermission(self, permClass: System.Type, ) -> System.Security.IPermission:
        ...

    def RemovePermissionImpl(self, permClass: System.Type, ) -> System.Security.IPermission:
        ...

    @staticmethod
    def RevertAssert() -> None:
        ...

    def SetPermission(self, perm: System.Security.IPermission, ) -> System.Security.IPermission:
        ...

    def SetPermissionImpl(self, perm: System.Security.IPermission, ) -> System.Security.IPermission:
        ...

    def OnDeserialization(self, sender: System.Object, ) -> None:
        ...

    def ToString(self, ) -> str:
        ...

    def ToXml(self, ) -> System.Security.SecurityElement:
        ...

    def Union(self, other: System.Security.PermissionSet, ) -> System.Security.PermissionSet:
        ...

class ISecurityEncodable(abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    @abc.abstractmethod
    def FromXml(self, e: System.Security.SecurityElement, ) -> None:
        ...

    @abc.abstractmethod
    def ToXml(self, ) -> System.Security.SecurityElement:
        ...

class IPermission(System.Security.ISecurityEncodable, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    @abc.abstractmethod
    def Copy(self, ) -> System.Security.IPermission:
        ...

    @abc.abstractmethod
    def Demand(self, ) -> None:
        ...

    @abc.abstractmethod
    def Intersect(self, target: System.Security.IPermission, ) -> System.Security.IPermission:
        ...

    @abc.abstractmethod
    def IsSubsetOf(self, target: System.Security.IPermission, ) -> bool:
        ...

    @abc.abstractmethod
    def Union(self, target: System.Security.IPermission, ) -> System.Security.IPermission:
        ...

class IStackWalk(abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    @abc.abstractmethod
    def Assert(self, ) -> None:
        ...

    @abc.abstractmethod
    def Demand(self, ) -> None:
        ...

    @abc.abstractmethod
    def Deny(self, ) -> None:
        ...

    @abc.abstractmethod
    def PermitOnly(self, ) -> None:
        ...

class SecurityElement(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        self._tag: str
        self._text: str
        self._attributes: System.Collections.ArrayList
        ...

    # static fields

    # properties
    @property
    def Tag(self) -> str:
        ...
    @Tag.setter
    def Tag(self, val: str):
        ...

    @property
    def Attributes(self) -> System.Collections.Hashtable:
        ...
    @Attributes.setter
    def Attributes(self, val: System.Collections.Hashtable):
        ...

    @property
    def Text(self) -> str:
        ...
    @Text.setter
    def Text(self, val: str):
        ...

    @property
    def Children(self) -> System.Collections.ArrayList:
        ...
    @Children.setter
    def Children(self, val: System.Collections.ArrayList):
        ...

    # methods
    @typing.overload
    def __init__(self, tag: str, ):
        ...

    @typing.overload
    def __init__(self, tag: str, text: str, ):
        ...

    def AddAttributeSafe(self, name: str, value: str, ) -> None:
        ...

    def AddAttribute(self, name: str, value: str, ) -> None:
        ...

    def AddChild(self, child: System.Security.SecurityElement, ) -> None:
        ...

    def Equal(self, other: System.Security.SecurityElement, ) -> bool:
        ...

    def Copy(self, ) -> System.Security.SecurityElement:
        ...

    @staticmethod
    def IsValidTag(tag: str, ) -> bool:
        ...

    @staticmethod
    def IsValidText(text: str, ) -> bool:
        ...

    @staticmethod
    def IsValidAttributeName(name: str, ) -> bool:
        ...

    @staticmethod
    def IsValidAttributeValue(value: str, ) -> bool:
        ...

    @staticmethod
    def GetEscapeSequence(c: str, ) -> str:
        ...

    @staticmethod
    def Escape(str: str, ) -> str:
        ...

    @staticmethod
    def GetUnescapeSequence(str: str, index: int, newIndex: ref[int], ) -> str:
        ...

    @staticmethod
    def Unescape(str: str, ) -> str:
        ...

    @typing.overload
    def ToString(self, ) -> str:
        ...

    @typing.overload
    def ToString(self, obj: System.Object, write: System.Action[System.Object, str], ) -> None:
        ...

    def Attribute(self, name: str, ) -> str:
        ...

    def SearchForChildByTag(self, tag: str, ) -> System.Security.SecurityElement:
        ...

    def SearchForTextOfTag(self, tag: str, ) -> str:
        ...

    @staticmethod
    def FromString(xml: str, ) -> System.Security.SecurityElement:
        ...

