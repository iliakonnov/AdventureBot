from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import System
import System.Runtime.Serialization
import System.Threading
import System.Collections


class StreamingContext(System.ValueType):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def State(self) -> int:
        ...

    @property
    def Context(self) -> System.Object:
        ...

    # methods
    @typing.overload
    def __init__(self, state: int, ):
        ...

    @typing.overload
    def __init__(self, state: int, additional: System.Object, ):
        ...

    def Equals(self, obj: System.Object, ) -> bool:
        ...

    def GetHashCode(self, ) -> int:
        ...

class StreamingContextStates(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    CrossProcess: int = ...
    CrossMachine: int = ...
    File: int = ...
    Persistence: int = ...
    Remoting: int = ...
    Other: int = ...
    Clone: int = ...
    CrossAppDomain: int = ...
    All: int = ...

class IObjectReference(abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    @abc.abstractmethod
    def GetRealObject(self, context: System.Runtime.Serialization.StreamingContext, ) -> System.Object:
        ...

class SerializationInfo(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def FullTypeName(self) -> str:
        ...
    @FullTypeName.setter
    def FullTypeName(self, val: str):
        ...

    @property
    def AssemblyName(self) -> str:
        ...
    @AssemblyName.setter
    def AssemblyName(self, val: str):
        ...

    @property
    def IsFullTypeNameSetExplicit(self) -> bool:
        ...
    @IsFullTypeNameSetExplicit.setter
    def IsFullTypeNameSetExplicit(self, val: bool):
        ...

    @property
    def IsAssemblyNameSetExplicit(self) -> bool:
        ...
    @IsAssemblyNameSetExplicit.setter
    def IsAssemblyNameSetExplicit(self, val: bool):
        ...

    @property
    def MemberCount(self) -> int:
        ...

    @property
    def ObjectType(self) -> System.Type:
        ...

    @property
    def AsyncDeserializationInProgress(self) -> System.Threading.AsyncLocal[bool]:
        ...

    @property
    def DeserializationInProgress(self) -> bool:
        ...

    # methods
    @typing.overload
    def __init__(self, type: System.Type, converter: System.Runtime.Serialization.IFormatterConverter, ):
        ...

    @typing.overload
    def __init__(self, type: System.Type, converter: System.Runtime.Serialization.IFormatterConverter, requireSameTokenInPartialTrust: bool, ):
        ...

    def SetType(self, type: System.Type, ) -> None:
        ...

    def GetEnumerator(self, ) -> System.Runtime.Serialization.SerializationInfoEnumerator:
        ...

    def ExpandArrays(self, ) -> None:
        ...

    @typing.overload
    def AddValue(self, name: str, value: System.Object, type: System.Type, ) -> None:
        ...

    @typing.overload
    def AddValue(self, name: str, value: System.Object, ) -> None:
        ...

    @typing.overload
    def AddValue(self, name: str, value: bool, ) -> None:
        ...

    @typing.overload
    def AddValue(self, name: str, value: str, ) -> None:
        ...

    @typing.overload
    def AddValue(self, name: str, value: int, ) -> None:
        ...

    @typing.overload
    def AddValue(self, name: str, value: int, ) -> None:
        ...

    @typing.overload
    def AddValue(self, name: str, value: int, ) -> None:
        ...

    @typing.overload
    def AddValue(self, name: str, value: int, ) -> None:
        ...

    @typing.overload
    def AddValue(self, name: str, value: int, ) -> None:
        ...

    @typing.overload
    def AddValue(self, name: str, value: int, ) -> None:
        ...

    @typing.overload
    def AddValue(self, name: str, value: int, ) -> None:
        ...

    @typing.overload
    def AddValue(self, name: str, value: int, ) -> None:
        ...

    @typing.overload
    def AddValue(self, name: str, value: float, ) -> None:
        ...

    @typing.overload
    def AddValue(self, name: str, value: float, ) -> None:
        ...

    @typing.overload
    def AddValue(self, name: str, value: System.Decimal, ) -> None:
        ...

    @typing.overload
    def AddValue(self, name: str, value: System.DateTime, ) -> None:
        ...

    def AddValueInternal(self, name: str, value: System.Object, type: System.Type, ) -> None:
        ...

    def UpdateValue(self, name: str, value: System.Object, type: System.Type, ) -> None:
        ...

    def FindElement(self, name: str, ) -> int:
        ...

    def GetElement(self, name: str, foundType: ref[System.Type], ) -> System.Object:
        ...

    def GetElementNoThrow(self, name: str, foundType: ref[System.Type], ) -> System.Object:
        ...

    def GetValue(self, name: str, type: System.Type, ) -> System.Object:
        ...

    def GetValueNoThrow(self, name: str, type: System.Type, ) -> System.Object:
        ...

    def GetBoolean(self, name: str, ) -> bool:
        ...

    def GetChar(self, name: str, ) -> str:
        ...

    def GetSByte(self, name: str, ) -> int:
        ...

    def GetByte(self, name: str, ) -> int:
        ...

    def GetInt16(self, name: str, ) -> int:
        ...

    def GetUInt16(self, name: str, ) -> int:
        ...

    def GetInt32(self, name: str, ) -> int:
        ...

    def GetUInt32(self, name: str, ) -> int:
        ...

    def GetInt64(self, name: str, ) -> int:
        ...

    def GetUInt64(self, name: str, ) -> int:
        ...

    def GetSingle(self, name: str, ) -> float:
        ...

    def GetDouble(self, name: str, ) -> float:
        ...

    def GetDecimal(self, name: str, ) -> System.Decimal:
        ...

    def GetDateTime(self, name: str, ) -> System.DateTime:
        ...

    def GetString(self, name: str, ) -> str:
        ...

    @staticmethod
    def GetThreadDeserializationTracker() -> System.Runtime.Serialization.DeserializationTracker:
        ...

    @staticmethod
    @typing.overload
    def ThrowIfDeserializationInProgress() -> None:
        ...

    @staticmethod
    @typing.overload
    def ThrowIfDeserializationInProgress(switchSuffix: str, cachedValue: ref[int], ) -> None:
        ...

    @staticmethod
    def StartDeserialization() -> System.Runtime.Serialization.DeserializationToken:
        ...

class DeserializationToken(System.IDisposable, System.ValueType):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    def __init__(self, tracker: System.Runtime.Serialization.DeserializationTracker, ):
        ...

    def Dispose(self, ) -> None:
        ...

class IDeserializationCallback(abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    @abc.abstractmethod
    def OnDeserialization(self, sender: System.Object, ) -> None:
        ...

class ISerializable(abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    @abc.abstractmethod
    def GetObjectData(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext, ) -> None:
        ...

class IFormatterConverter(abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    @abc.abstractmethod
    @typing.overload
    def Convert(self, value: System.Object, type: System.Type, ) -> System.Object:
        ...

    @abc.abstractmethod
    @typing.overload
    def Convert(self, value: System.Object, typeCode: int, ) -> System.Object:
        ...

    @abc.abstractmethod
    def ToBoolean(self, value: System.Object, ) -> bool:
        ...

    @abc.abstractmethod
    def ToChar(self, value: System.Object, ) -> str:
        ...

    @abc.abstractmethod
    def ToSByte(self, value: System.Object, ) -> int:
        ...

    @abc.abstractmethod
    def ToByte(self, value: System.Object, ) -> int:
        ...

    @abc.abstractmethod
    def ToInt16(self, value: System.Object, ) -> int:
        ...

    @abc.abstractmethod
    def ToUInt16(self, value: System.Object, ) -> int:
        ...

    @abc.abstractmethod
    def ToInt32(self, value: System.Object, ) -> int:
        ...

    @abc.abstractmethod
    def ToUInt32(self, value: System.Object, ) -> int:
        ...

    @abc.abstractmethod
    def ToInt64(self, value: System.Object, ) -> int:
        ...

    @abc.abstractmethod
    def ToUInt64(self, value: System.Object, ) -> int:
        ...

    @abc.abstractmethod
    def ToSingle(self, value: System.Object, ) -> float:
        ...

    @abc.abstractmethod
    def ToDouble(self, value: System.Object, ) -> float:
        ...

    @abc.abstractmethod
    def ToDecimal(self, value: System.Object, ) -> System.Decimal:
        ...

    @abc.abstractmethod
    def ToDateTime(self, value: System.Object, ) -> System.DateTime:
        ...

    @abc.abstractmethod
    def ToString(self, value: System.Object, ) -> str:
        ...

class SerializationInfoEnumerator(System.Collections.IEnumerator, System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def Current(self) -> System.Object:
        ...

    @property
    def Current(self) -> System.Runtime.Serialization.SerializationEntry:
        ...

    @property
    def Name(self) -> str:
        ...

    @property
    def Value(self) -> System.Object:
        ...

    @property
    def ObjectType(self) -> System.Type:
        ...

    # methods
    def __init__(self, members: System.Array[str], info: System.Array[System.Object], types: System.Array[System.Type], numItems: int, ):
        ...

    def MoveNext(self, ) -> bool:
        ...

    def Reset(self, ) -> None:
        ...

class SerializationEntry(System.ValueType):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def Value(self) -> System.Object:
        ...

    @property
    def Name(self) -> str:
        ...

    @property
    def ObjectType(self) -> System.Type:
        ...

    # methods
    def __init__(self, entryName: str, entryValue: System.Object, entryType: System.Type, ):
        ...

