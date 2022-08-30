from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import System.Runtime.Serialization
import System
import System.Collections


class ISerializable(abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    # methods
    @typing.overload
    @abc.abstractmethod
    def GetObjectData(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext, ) -> None:
        ...

class IDeserializationCallback(abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    # methods
    @typing.overload
    @abc.abstractmethod
    def OnDeserialization(self, sender: System.Object, ) -> None:
        ...

class SerializationInfo(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def FullTypeName(self) -> System.String:
        ...
    @FullTypeName.setter
    def FullTypeName(self, val: System.String):
        ...

    @property
    def AssemblyName(self) -> System.String:
        ...
    @AssemblyName.setter
    def AssemblyName(self, val: System.String):
        ...

    @property
    def IsFullTypeNameSetExplicit(self) -> System.Boolean:
        ...

    @property
    def IsAssemblyNameSetExplicit(self) -> System.Boolean:
        ...

    @property
    def MemberCount(self) -> System.Int32:
        ...

    @property
    def ObjectType(self) -> System.Type:
        ...

    @property
    def DeserializationInProgress(self) -> System.Boolean:
        ...

    # methods
    @typing.overload
    def __init__(self, type: System.Type, converter: System.Runtime.Serialization.IFormatterConverter, ):
        ...

    @typing.overload
    def __init__(self, type: System.Type, converter: System.Runtime.Serialization.IFormatterConverter, requireSameTokenInPartialTrust: System.Boolean, ):
        ...

    @typing.overload
    def SetType(self, type: System.Type, ) -> None:
        ...

    @typing.overload
    def GetEnumerator(self, ) -> System.Runtime.Serialization.SerializationInfoEnumerator:
        ...

    @typing.overload
    def AddValue(self, name: System.String, value: System.Object, type: System.Type, ) -> None:
        ...

    @typing.overload
    def AddValue(self, name: System.String, value: System.Object, ) -> None:
        ...

    @typing.overload
    def AddValue(self, name: System.String, value: System.Boolean, ) -> None:
        ...

    @typing.overload
    def AddValue(self, name: System.String, value: System.Char, ) -> None:
        ...

    @typing.overload
    def AddValue(self, name: System.String, value: System.SByte, ) -> None:
        ...

    @typing.overload
    def AddValue(self, name: System.String, value: System.Byte, ) -> None:
        ...

    @typing.overload
    def AddValue(self, name: System.String, value: System.Int16, ) -> None:
        ...

    @typing.overload
    def AddValue(self, name: System.String, value: System.UInt16, ) -> None:
        ...

    @typing.overload
    def AddValue(self, name: System.String, value: System.Int32, ) -> None:
        ...

    @typing.overload
    def AddValue(self, name: System.String, value: System.UInt32, ) -> None:
        ...

    @typing.overload
    def AddValue(self, name: System.String, value: System.Int64, ) -> None:
        ...

    @typing.overload
    def AddValue(self, name: System.String, value: System.UInt64, ) -> None:
        ...

    @typing.overload
    def AddValue(self, name: System.String, value: System.Single, ) -> None:
        ...

    @typing.overload
    def AddValue(self, name: System.String, value: System.Double, ) -> None:
        ...

    @typing.overload
    def AddValue(self, name: System.String, value: System.Decimal, ) -> None:
        ...

    @typing.overload
    def AddValue(self, name: System.String, value: System.DateTime, ) -> None:
        ...

    @typing.overload
    def UpdateValue(self, name: System.String, value: System.Object, type: System.Type, ) -> None:
        ...

    @typing.overload
    def GetValue(self, name: System.String, type: System.Type, ) -> System.Object:
        ...

    @typing.overload
    def GetBoolean(self, name: System.String, ) -> System.Boolean:
        ...

    @typing.overload
    def GetChar(self, name: System.String, ) -> System.Char:
        ...

    @typing.overload
    def GetSByte(self, name: System.String, ) -> System.SByte:
        ...

    @typing.overload
    def GetByte(self, name: System.String, ) -> System.Byte:
        ...

    @typing.overload
    def GetInt16(self, name: System.String, ) -> System.Int16:
        ...

    @typing.overload
    def GetUInt16(self, name: System.String, ) -> System.UInt16:
        ...

    @typing.overload
    def GetInt32(self, name: System.String, ) -> System.Int32:
        ...

    @typing.overload
    def GetUInt32(self, name: System.String, ) -> System.UInt32:
        ...

    @typing.overload
    def GetInt64(self, name: System.String, ) -> System.Int64:
        ...

    @typing.overload
    def GetUInt64(self, name: System.String, ) -> System.UInt64:
        ...

    @typing.overload
    def GetSingle(self, name: System.String, ) -> System.Single:
        ...

    @typing.overload
    def GetDouble(self, name: System.String, ) -> System.Double:
        ...

    @typing.overload
    def GetDecimal(self, name: System.String, ) -> System.Decimal:
        ...

    @typing.overload
    def GetDateTime(self, name: System.String, ) -> System.DateTime:
        ...

    @typing.overload
    def GetString(self, name: System.String, ) -> System.String:
        ...

    @typing.overload
    @staticmethod
    def ThrowIfDeserializationInProgress() -> None:
        ...

    @typing.overload
    @staticmethod
    def ThrowIfDeserializationInProgress(switchSuffix: System.String, cachedValue: ref[System.Int32], ) -> None:
        ...

    @typing.overload
    @staticmethod
    def StartDeserialization() -> System.Runtime.Serialization.DeserializationToken:
        ...

class StreamingContext(System.ValueType):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def State(self) -> System.Runtime.Serialization.StreamingContextStates:
        ...

    @property
    def Context(self) -> System.Object:
        ...

    # methods
    @typing.overload
    def __init__(self, state: System.Runtime.Serialization.StreamingContextStates, ):
        ...

    @typing.overload
    def __init__(self, state: System.Runtime.Serialization.StreamingContextStates, additional: System.Object, ):
        ...

    @typing.overload
    def Equals(self, obj: System.Object, ) -> System.Boolean:
        ...

    @typing.overload
    def GetHashCode(self, ) -> System.Int32:
        ...

class IFormatterConverter(abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    # methods
    @typing.overload
    @abc.abstractmethod
    def Convert(self, value: System.Object, type: System.Type, ) -> System.Object:
        ...

    @typing.overload
    @abc.abstractmethod
    def Convert(self, value: System.Object, typeCode: System.TypeCode, ) -> System.Object:
        ...

    @typing.overload
    @abc.abstractmethod
    def ToBoolean(self, value: System.Object, ) -> System.Boolean:
        ...

    @typing.overload
    @abc.abstractmethod
    def ToChar(self, value: System.Object, ) -> System.Char:
        ...

    @typing.overload
    @abc.abstractmethod
    def ToSByte(self, value: System.Object, ) -> System.SByte:
        ...

    @typing.overload
    @abc.abstractmethod
    def ToByte(self, value: System.Object, ) -> System.Byte:
        ...

    @typing.overload
    @abc.abstractmethod
    def ToInt16(self, value: System.Object, ) -> System.Int16:
        ...

    @typing.overload
    @abc.abstractmethod
    def ToUInt16(self, value: System.Object, ) -> System.UInt16:
        ...

    @typing.overload
    @abc.abstractmethod
    def ToInt32(self, value: System.Object, ) -> System.Int32:
        ...

    @typing.overload
    @abc.abstractmethod
    def ToUInt32(self, value: System.Object, ) -> System.UInt32:
        ...

    @typing.overload
    @abc.abstractmethod
    def ToInt64(self, value: System.Object, ) -> System.Int64:
        ...

    @typing.overload
    @abc.abstractmethod
    def ToUInt64(self, value: System.Object, ) -> System.UInt64:
        ...

    @typing.overload
    @abc.abstractmethod
    def ToSingle(self, value: System.Object, ) -> System.Single:
        ...

    @typing.overload
    @abc.abstractmethod
    def ToDouble(self, value: System.Object, ) -> System.Double:
        ...

    @typing.overload
    @abc.abstractmethod
    def ToDecimal(self, value: System.Object, ) -> System.Decimal:
        ...

    @typing.overload
    @abc.abstractmethod
    def ToDateTime(self, value: System.Object, ) -> System.DateTime:
        ...

    @typing.overload
    @abc.abstractmethod
    def ToString(self, value: System.Object, ) -> System.String:
        ...

class SerializationInfoEnumerator(System.Collections.IEnumerator, System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def Current(self) -> System.Runtime.Serialization.SerializationEntry:
        ...

    @property
    def Name(self) -> System.String:
        ...

    @property
    def Value(self) -> System.Object:
        ...

    @property
    def ObjectType(self) -> System.Type:
        ...

    # methods
    @typing.overload
    def MoveNext(self, ) -> System.Boolean:
        ...

    @typing.overload
    def Reset(self, ) -> None:
        ...

class DeserializationToken(System.IDisposable, System.ValueType):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    # methods
    @typing.overload
    def Dispose(self, ) -> None:
        ...

class StreamingContextStates(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    CrossProcess: System.Int32 = CrossProcess
    CrossMachine: System.Int32 = CrossMachine
    File: System.Int32 = File
    Persistence: System.Int32 = Persistence
    Remoting: System.Int32 = Remoting
    Other: System.Int32 = Other
    Clone: System.Int32 = Clone
    CrossAppDomain: System.Int32 = CrossAppDomain
    All: System.Int32 = All

class IObjectReference(abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    # methods
    @typing.overload
    @abc.abstractmethod
    def GetRealObject(self, context: System.Runtime.Serialization.StreamingContext, ) -> System.Object:
        ...

class SerializationEntry(System.ValueType):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def Value(self) -> System.Object:
        ...

    @property
    def Name(self) -> System.String:
        ...

    @property
    def ObjectType(self) -> System.Type:
        ...

    # methods
