from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import System
import System.Runtime.InteropServices.ComTypes
import System.Runtime.InteropServices.ComTypes.ELEMDESC


class ITypeInfo(abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    @abc.abstractmethod
    def GetTypeAttr(self, ppTypeAttr: ref[System.IntPtr], ) -> None:
        ...

    @abc.abstractmethod
    def GetTypeComp(self, ppTComp: ref[System.Runtime.InteropServices.ComTypes.ITypeComp], ) -> None:
        ...

    @abc.abstractmethod
    def GetFuncDesc(self, index: int, ppFuncDesc: ref[System.IntPtr], ) -> None:
        ...

    @abc.abstractmethod
    def GetVarDesc(self, index: int, ppVarDesc: ref[System.IntPtr], ) -> None:
        ...

    @abc.abstractmethod
    def GetNames(self, memid: int, rgBstrNames: System.Array[str], cMaxNames: int, pcNames: ref[int], ) -> None:
        ...

    @abc.abstractmethod
    def GetRefTypeOfImplType(self, index: int, href: ref[int], ) -> None:
        ...

    @abc.abstractmethod
    def GetImplTypeFlags(self, index: int, pImplTypeFlags: ref[int], ) -> None:
        ...

    @abc.abstractmethod
    def GetIDsOfNames(self, rgszNames: System.Array[str], cNames: int, pMemId: System.Array[int], ) -> None:
        ...

    @abc.abstractmethod
    def Invoke(self, pvInstance: System.Object, memid: int, wFlags: int, pDispParams: ref[System.Runtime.InteropServices.ComTypes.DISPPARAMS], pVarResult: System.IntPtr, pExcepInfo: System.IntPtr, puArgErr: ref[int], ) -> None:
        ...

    @abc.abstractmethod
    def GetDocumentation(self, index: int, strName: ref[str], strDocString: ref[str], dwHelpContext: ref[int], strHelpFile: ref[str], ) -> None:
        ...

    @abc.abstractmethod
    def GetDllEntry(self, memid: int, invKind: int, pBstrDllName: System.IntPtr, pBstrName: System.IntPtr, pwOrdinal: System.IntPtr, ) -> None:
        ...

    @abc.abstractmethod
    def GetRefTypeInfo(self, hRef: int, ppTI: ref[System.Runtime.InteropServices.ComTypes.ITypeInfo], ) -> None:
        ...

    @abc.abstractmethod
    def AddressOfMember(self, memid: int, invKind: int, ppv: ref[System.IntPtr], ) -> None:
        ...

    @abc.abstractmethod
    def CreateInstance(self, pUnkOuter: System.Object, riid: ref[System.Guid], ppvObj: ref[System.Object], ) -> None:
        ...

    @abc.abstractmethod
    def GetMops(self, memid: int, pBstrMops: ref[str], ) -> None:
        ...

    @abc.abstractmethod
    def GetContainingTypeLib(self, ppTLB: ref[System.Runtime.InteropServices.ComTypes.ITypeLib], pIndex: ref[int], ) -> None:
        ...

    @abc.abstractmethod
    def ReleaseTypeAttr(self, pTypeAttr: System.IntPtr, ) -> None:
        ...

    @abc.abstractmethod
    def ReleaseFuncDesc(self, pFuncDesc: System.IntPtr, ) -> None:
        ...

    @abc.abstractmethod
    def ReleaseVarDesc(self, pVarDesc: System.IntPtr, ) -> None:
        ...

class ITypeLib(abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    @abc.abstractmethod
    def GetTypeInfoCount(self, ) -> int:
        ...

    @abc.abstractmethod
    def GetTypeInfo(self, index: int, ppTI: ref[System.Runtime.InteropServices.ComTypes.ITypeInfo], ) -> None:
        ...

    @abc.abstractmethod
    def GetTypeInfoType(self, index: int, pTKind: ref[int], ) -> None:
        ...

    @abc.abstractmethod
    def GetTypeInfoOfGuid(self, guid: ref[System.Guid], ppTInfo: ref[System.Runtime.InteropServices.ComTypes.ITypeInfo], ) -> None:
        ...

    @abc.abstractmethod
    def GetLibAttr(self, ppTLibAttr: ref[System.IntPtr], ) -> None:
        ...

    @abc.abstractmethod
    def GetTypeComp(self, ppTComp: ref[System.Runtime.InteropServices.ComTypes.ITypeComp], ) -> None:
        ...

    @abc.abstractmethod
    def GetDocumentation(self, index: int, strName: ref[str], strDocString: ref[str], dwHelpContext: ref[int], strHelpFile: ref[str], ) -> None:
        ...

    @abc.abstractmethod
    def IsName(self, szNameBuf: str, lHashVal: int, ) -> bool:
        ...

    @abc.abstractmethod
    def FindName(self, szNameBuf: str, lHashVal: int, ppTInfo: System.Array[System.Runtime.InteropServices.ComTypes.ITypeInfo], rgMemId: System.Array[int], pcFound: ref[int], ) -> None:
        ...

    @abc.abstractmethod
    def ReleaseTLibAttr(self, pTLibAttr: System.IntPtr, ) -> None:
        ...

class ITypeComp(abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    @abc.abstractmethod
    def Bind(self, szName: str, lHashVal: int, wFlags: int, ppTInfo: ref[System.Runtime.InteropServices.ComTypes.ITypeInfo], pDescKind: ref[int], pBindPtr: ref[System.Runtime.InteropServices.ComTypes.BINDPTR], ) -> None:
        ...

    @abc.abstractmethod
    def BindType(self, szName: str, lHashVal: int, ppTInfo: ref[System.Runtime.InteropServices.ComTypes.ITypeInfo], ppTComp: ref[System.Runtime.InteropServices.ComTypes.ITypeComp], ) -> None:
        ...

class DESCKIND(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    DESCKIND_NONE: int = ...
    DESCKIND_FUNCDESC: int = ...
    DESCKIND_VARDESC: int = ...
    DESCKIND_TYPECOMP: int = ...
    DESCKIND_IMPLICITAPPOBJ: int = ...
    DESCKIND_MAX: int = ...

class BINDPTR(System.ValueType):
    @typing.overload
    def __init__(self, **kwargs):
        self.lpfuncdesc: System.IntPtr
        self.lpvardesc: System.IntPtr
        self.lptcomp: System.IntPtr
        ...

    # static fields

    # properties
    # methods
class TYPEKIND(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    TKIND_ENUM: int = ...
    TKIND_RECORD: int = ...
    TKIND_MODULE: int = ...
    TKIND_INTERFACE: int = ...
    TKIND_DISPATCH: int = ...
    TKIND_COCLASS: int = ...
    TKIND_ALIAS: int = ...
    TKIND_UNION: int = ...
    TKIND_MAX: int = ...

class IMPLTYPEFLAGS(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    IMPLTYPEFLAG_FDEFAULT: int = ...
    IMPLTYPEFLAG_FSOURCE: int = ...
    IMPLTYPEFLAG_FRESTRICTED: int = ...
    IMPLTYPEFLAG_FDEFAULTVTABLE: int = ...

class DISPPARAMS(System.ValueType):
    @typing.overload
    def __init__(self, **kwargs):
        self.rgvarg: System.IntPtr
        self.rgdispidNamedArgs: System.IntPtr
        self.cArgs: int
        self.cNamedArgs: int
        ...

    # static fields

    # properties
    # methods
class TYPEATTR(System.ValueType):
    @typing.overload
    def __init__(self, **kwargs):
        self.guid: System.Guid
        self.lcid: int
        self.dwReserved: int
        self.memidConstructor: int
        self.memidDestructor: int
        self.lpstrSchema: System.IntPtr
        self.cbSizeInstance: int
        self.typekind: int
        self.cFuncs: int
        self.cVars: int
        self.cImplTypes: int
        self.cbSizeVft: int
        self.cbAlignment: int
        self.wTypeFlags: int
        self.wMajorVerNum: int
        self.wMinorVerNum: int
        self.tdescAlias: System.Runtime.InteropServices.ComTypes.TYPEDESC
        self.idldescType: System.Runtime.InteropServices.ComTypes.IDLDESC
        ...

    # static fields
    MEMBER_ID_NIL: int = ...

    # properties
    # methods
class IDLDESC(System.ValueType):
    @typing.overload
    def __init__(self, **kwargs):
        self.dwReserved: System.IntPtr
        self.wIDLFlags: int
        ...

    # static fields

    # properties
    # methods
class IDLFLAG(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    IDLFLAG_NONE: int = ...
    IDLFLAG_FIN: int = ...
    IDLFLAG_FOUT: int = ...
    IDLFLAG_FLCID: int = ...
    IDLFLAG_FRETVAL: int = ...

class TYPEFLAGS(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    TYPEFLAG_FAPPOBJECT: int = ...
    TYPEFLAG_FCANCREATE: int = ...
    TYPEFLAG_FLICENSED: int = ...
    TYPEFLAG_FPREDECLID: int = ...
    TYPEFLAG_FHIDDEN: int = ...
    TYPEFLAG_FCONTROL: int = ...
    TYPEFLAG_FDUAL: int = ...
    TYPEFLAG_FNONEXTENSIBLE: int = ...
    TYPEFLAG_FOLEAUTOMATION: int = ...
    TYPEFLAG_FRESTRICTED: int = ...
    TYPEFLAG_FAGGREGATABLE: int = ...
    TYPEFLAG_FREPLACEABLE: int = ...
    TYPEFLAG_FDISPATCHABLE: int = ...
    TYPEFLAG_FREVERSEBIND: int = ...
    TYPEFLAG_FPROXY: int = ...

class TYPEDESC(System.ValueType):
    @typing.overload
    def __init__(self, **kwargs):
        self.lpValue: System.IntPtr
        self.vt: int
        ...

    # static fields

    # properties
    # methods
class FUNCDESC(System.ValueType):
    @typing.overload
    def __init__(self, **kwargs):
        self.memid: int
        self.lprgscode: System.IntPtr
        self.lprgelemdescParam: System.IntPtr
        self.funckind: int
        self.invkind: int
        self.callconv: int
        self.cParams: int
        self.cParamsOpt: int
        self.oVft: int
        self.cScodes: int
        self.elemdescFunc: System.Runtime.InteropServices.ComTypes.ELEMDESC
        self.wFuncFlags: int
        ...

    # static fields

    # properties
    # methods
class FUNCKIND(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    FUNC_VIRTUAL: int = ...
    FUNC_PUREVIRTUAL: int = ...
    FUNC_NONVIRTUAL: int = ...
    FUNC_STATIC: int = ...
    FUNC_DISPATCH: int = ...

class CALLCONV(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    CC_CDECL: int = ...
    CC_MSCPASCAL: int = ...
    CC_PASCAL: int = ...
    CC_MACPASCAL: int = ...
    CC_STDCALL: int = ...
    CC_RESERVED: int = ...
    CC_SYSCALL: int = ...
    CC_MPWCDECL: int = ...
    CC_MPWPASCAL: int = ...
    CC_MAX: int = ...

class ELEMDESC(System.ValueType):
    @typing.overload
    def __init__(self, **kwargs):
        self.tdesc: System.Runtime.InteropServices.ComTypes.TYPEDESC
        self.desc: System.Runtime.InteropServices.ComTypes.ELEMDESC.DESCUNION
        ...

    # static fields

    # properties
    # methods
class PARAMDESC(System.ValueType):
    @typing.overload
    def __init__(self, **kwargs):
        self.lpVarValue: System.IntPtr
        self.wParamFlags: int
        ...

    # static fields

    # properties
    # methods
class PARAMFLAG(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    PARAMFLAG_NONE: int = ...
    PARAMFLAG_FIN: int = ...
    PARAMFLAG_FOUT: int = ...
    PARAMFLAG_FLCID: int = ...
    PARAMFLAG_FRETVAL: int = ...
    PARAMFLAG_FOPT: int = ...
    PARAMFLAG_FHASDEFAULT: int = ...
    PARAMFLAG_FHASCUSTDATA: int = ...

class INVOKEKIND(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    INVOKE_FUNC: int = ...
    INVOKE_PROPERTYGET: int = ...
    INVOKE_PROPERTYPUT: int = ...
    INVOKE_PROPERTYPUTREF: int = ...

