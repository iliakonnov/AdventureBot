from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import System.Xml.Schema
import System.Xml
import System
import System.Collections.Generic.Dictionary
import System.Collections.Generic
import System.Collections
import System.Xml.Serialization


class IXmlSerializable(abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    @abc.abstractmethod
    def GetSchema(self, ) -> System.Xml.Schema.XmlSchema:
        ...

    @abc.abstractmethod
    def ReadXml(self, reader: System.Xml.XmlReader, ) -> None:
        ...

    @abc.abstractmethod
    def WriteXml(self, writer: System.Xml.XmlWriter, ) -> None:
        ...

class XmlSerializerNamespaces(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def Count(self) -> int:
        ...

    @property
    def Namespaces(self) -> System.Collections.Generic.Dictionary.ValueCollection[str, System.Xml.XmlQualifiedName]:
        ...

    @property
    def NamespacesInternal(self) -> System.Collections.Generic.Dictionary[str, System.Xml.XmlQualifiedName]:
        ...

    @property
    def NamespaceList(self) -> System.Collections.ArrayList:
        ...

    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def __init__(self, namespaces: System.Xml.Serialization.XmlSerializerNamespaces, ):
        ...

    @typing.overload
    def __init__(self, namespaces: System.Array[System.Xml.XmlQualifiedName], ):
        ...

    @typing.overload
    def __init__(self, namespaces: System.Collections.Generic.IList[System.Xml.XmlQualifiedName], ):
        ...

    def Add(self, prefix: str, ns: str, ) -> None:
        ...

    def AddInternal(self, prefix: str, ns: str, ) -> None:
        ...

    def ToArray(self, ) -> System.Array[System.Xml.XmlQualifiedName]:
        ...

    def TryLookupPrefix(self, ns: str, prefix: ref[str], ) -> bool:
        ...

    def TryLookupNamespace(self, prefix: str, ns: ref[str], ) -> bool:
        ...

class XmlRootAttribute(System.Attribute):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def ElementName(self) -> str:
        ...
    @ElementName.setter
    def ElementName(self, val: str):
        ...

    @property
    def Namespace(self) -> str:
        ...
    @Namespace.setter
    def Namespace(self, val: str):
        ...

    @property
    def DataType(self) -> str:
        ...
    @DataType.setter
    def DataType(self, val: str):
        ...

    @property
    def IsNullable(self) -> bool:
        ...
    @IsNullable.setter
    def IsNullable(self, val: bool):
        ...

    @property
    def IsNullableSpecified(self) -> bool:
        ...

    @property
    def Key(self) -> str:
        ...

    @property
    def TypeId(self) -> System.Object:
        ...

    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def __init__(self, elementName: str, ):
        ...

    def GetIsNullableSpecified(self, ) -> bool:
        ...

    def GetKey(self, ) -> str:
        ...

