from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import System.Dynamic
import System
import System.Linq.Expressions
import Microsoft.Scripting.ComInterop
import System.Runtime.InteropServices.ComTypes
import System.Collections
import System.Collections.Generic


class ComTypeLibDesc(System.Dynamic.IDynamicMetaObjectProvider, System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def Documentation(self) -> str:
        ...

    @property
    def Guid(self) -> System.Guid:
        ...

    @property
    def VersionMajor(self) -> int:
        ...

    @property
    def VersionMinor(self) -> int:
        ...

    @property
    def Name(self) -> str:
        ...

    # methods
    def __init__(self, ):
        ...

    def ToString(self, ) -> str:
        ...

    def GetMetaObject(self, parameter: System.Linq.Expressions.Expression, ) -> System.Dynamic.DynamicMetaObject:
        ...

    @staticmethod
    def CreateFromGuid(typeLibGuid: System.Guid, ) -> Microsoft.Scripting.ComInterop.ComTypeLibInfo:
        ...

    @staticmethod
    def CreateFromObject(rcw: System.Object, ) -> Microsoft.Scripting.ComInterop.ComTypeLibInfo:
        ...

    @staticmethod
    def GetFromTypeLib(typeLib: System.Runtime.InteropServices.ComTypes.ITypeLib, ) -> Microsoft.Scripting.ComInterop.ComTypeLibDesc:
        ...

    def GetTypeLibObjectDesc(self, member: str, ) -> System.Object:
        ...

    def GetMemberNames(self, ) -> System.Array[str]:
        ...

    def HasMember(self, member: str, ) -> bool:
        ...

    def GetCoClassForInterface(self, itfName: str, ) -> Microsoft.Scripting.ComInterop.ComTypeClassDesc:
        ...

class ComTypeLibInfo(System.Dynamic.IDynamicMetaObjectProvider, System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def Name(self) -> str:
        ...

    @property
    def Guid(self) -> System.Guid:
        ...

    @property
    def VersionMajor(self) -> int:
        ...

    @property
    def VersionMinor(self) -> int:
        ...

    @property
    def TypeLibDesc(self) -> Microsoft.Scripting.ComInterop.ComTypeLibDesc:
        ...

    # methods
    def __init__(self, typeLibDesc: Microsoft.Scripting.ComInterop.ComTypeLibDesc, ):
        ...

    def GetMemberNames(self, ) -> System.Array[str]:
        ...

    def GetMetaObject(self, parameter: System.Linq.Expressions.Expression, ) -> System.Dynamic.DynamicMetaObject:
        ...

class ComTypeClassDesc(System.Dynamic.IDynamicMetaObjectProvider, Microsoft.Scripting.ComInterop.ComTypeDesc):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def Funcs(self) -> System.Collections.Hashtable:
        ...
    @Funcs.setter
    def Funcs(self, val: System.Collections.Hashtable):
        ...

    @property
    def Puts(self) -> System.Collections.Hashtable:
        ...
    @Puts.setter
    def Puts(self, val: System.Collections.Hashtable):
        ...

    PutRefs: System.Collections.Hashtable = property(None, lambda val: ...)

    @property
    def Events(self) -> System.Collections.Generic.Dictionary[str, Microsoft.Scripting.ComInterop.ComEventDesc]:
        ...
    @Events.setter
    def Events(self, val: System.Collections.Generic.Dictionary[str, Microsoft.Scripting.ComInterop.ComEventDesc]):
        ...

    @property
    def TypeName(self) -> str:
        ...

    @property
    def Documentation(self) -> str:
        ...

    @property
    def TypeLib(self) -> Microsoft.Scripting.ComInterop.ComTypeLibDesc:
        ...

    @property
    def Guid(self) -> System.Guid:
        ...
    @Guid.setter
    def Guid(self, val: System.Guid):
        ...

    @property
    def GetItem(self) -> Microsoft.Scripting.ComInterop.ComMethodDesc:
        ...

    @property
    def SetItem(self) -> Microsoft.Scripting.ComInterop.ComMethodDesc:
        ...

    @property
    def Kind(self) -> int:
        ...

    # methods
    def __init__(self, typeInfo: System.Runtime.InteropServices.ComTypes.ITypeInfo, typeLibDesc: Microsoft.Scripting.ComInterop.ComTypeLibDesc, ):
        ...

    def CreateInstance(self, ) -> System.Object:
        ...

    def AddInterface(self, itfTypeInfo: System.Runtime.InteropServices.ComTypes.ITypeInfo, isSourceItf: bool, ) -> None:
        ...

    def Implements(self, itfName: str, isSourceItf: bool, ) -> bool:
        ...

    def GetMetaObject(self, parameter: System.Linq.Expressions.Expression, ) -> System.Dynamic.DynamicMetaObject:
        ...

class ComTypeDesc(Microsoft.Scripting.ComInterop.ComTypeLibMemberDesc):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def EmptyEvents(self) -> System.Collections.Generic.Dictionary[str, Microsoft.Scripting.ComInterop.ComEventDesc]:
        ...

    @property
    def Funcs(self) -> System.Collections.Hashtable:
        ...
    @Funcs.setter
    def Funcs(self, val: System.Collections.Hashtable):
        ...

    @property
    def Puts(self) -> System.Collections.Hashtable:
        ...
    @Puts.setter
    def Puts(self, val: System.Collections.Hashtable):
        ...

    PutRefs: System.Collections.Hashtable = property(None, lambda val: ...)

    @property
    def Events(self) -> System.Collections.Generic.Dictionary[str, Microsoft.Scripting.ComInterop.ComEventDesc]:
        ...
    @Events.setter
    def Events(self, val: System.Collections.Generic.Dictionary[str, Microsoft.Scripting.ComInterop.ComEventDesc]):
        ...

    @property
    def TypeName(self) -> str:
        ...

    @property
    def Documentation(self) -> str:
        ...

    @property
    def TypeLib(self) -> Microsoft.Scripting.ComInterop.ComTypeLibDesc:
        ...

    @property
    def Guid(self) -> System.Guid:
        ...
    @Guid.setter
    def Guid(self, val: System.Guid):
        ...

    @property
    def GetItem(self) -> Microsoft.Scripting.ComInterop.ComMethodDesc:
        ...

    @property
    def SetItem(self) -> Microsoft.Scripting.ComInterop.ComMethodDesc:
        ...

    @property
    def Kind(self) -> int:
        ...

    # methods
    def __init__(self, typeInfo: System.Runtime.InteropServices.ComTypes.ITypeInfo, memberType: int, typeLibDesc: Microsoft.Scripting.ComInterop.ComTypeLibDesc, ):
        ...

    @staticmethod
    def FromITypeInfo(typeInfo: System.Runtime.InteropServices.ComTypes.ITypeInfo, typeAttr: System.Runtime.InteropServices.ComTypes.TYPEATTR, ) -> Microsoft.Scripting.ComInterop.ComTypeDesc:
        ...

    @staticmethod
    def CreateEmptyTypeDesc() -> Microsoft.Scripting.ComInterop.ComTypeDesc:
        ...

    def TryGetFunc(self, name: str, method: ref[Microsoft.Scripting.ComInterop.ComMethodDesc], ) -> bool:
        ...

    def AddFunc(self, name: str, method: Microsoft.Scripting.ComInterop.ComMethodDesc, ) -> None:
        ...

    def TryGetPut(self, name: str, method: ref[Microsoft.Scripting.ComInterop.ComMethodDesc], ) -> bool:
        ...

    def AddPut(self, name: str, method: Microsoft.Scripting.ComInterop.ComMethodDesc, ) -> None:
        ...

    def TryGetPutRef(self, name: str, method: ref[Microsoft.Scripting.ComInterop.ComMethodDesc], ) -> bool:
        ...

    def AddPutRef(self, name: str, method: Microsoft.Scripting.ComInterop.ComMethodDesc, ) -> None:
        ...

    def TryGetEvent(self, name: str, event: ref[Microsoft.Scripting.ComInterop.ComEventDesc], ) -> bool:
        ...

    def GetMemberNames(self, dataOnly: bool, ) -> System.Array[str]:
        ...

    def EnsureGetItem(self, candidate: Microsoft.Scripting.ComInterop.ComMethodDesc, ) -> None:
        ...

    def EnsureSetItem(self, candidate: Microsoft.Scripting.ComInterop.ComMethodDesc, ) -> None:
        ...

class ComMethodDesc(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        self.InvokeKind: int
        ...

    # static fields

    # properties
    @property
    def Name(self) -> str:
        ...

    @property
    def DispId(self) -> int:
        ...

    @property
    def IsPropertyGet(self) -> bool:
        ...

    @property
    def IsDataMember(self) -> bool:
        ...

    @property
    def IsPropertyPut(self) -> bool:
        ...

    @property
    def IsPropertyPutRef(self) -> bool:
        ...

    @property
    def ParamCount(self) -> int:
        ...

    # methods
    @typing.overload
    def __init__(self, dispId: int, ):
        ...

    @typing.overload
    def __init__(self, name: str, dispId: int, ):
        ...

    @typing.overload
    def __init__(self, name: str, dispId: int, invkind: int, ):
        ...

    @typing.overload
    def __init__(self, typeInfo: System.Runtime.InteropServices.ComTypes.ITypeInfo, funcDesc: System.Runtime.InteropServices.ComTypes.FUNCDESC, ):
        ...

class ComTypeLibMemberDesc(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def Kind(self) -> int:
        ...

    # methods
    def __init__(self, kind: int, ):
        ...

class ComType(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    Class: int = ...
    Enum: int = ...
    Interface: int = ...

