from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import System.Xml.Schema
import System.Xml
import System
import System.Xml.Serialization


class IXmlSerializable(abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    # methods
    @typing.overload
    @abc.abstractmethod
    def GetSchema(self, ) -> System.Xml.Schema.XmlSchema:
        ...

    @typing.overload
    @abc.abstractmethod
    def ReadXml(self, reader: System.Xml.XmlReader, ) -> None:
        ...

    @typing.overload
    @abc.abstractmethod
    def WriteXml(self, writer: System.Xml.XmlWriter, ) -> None:
        ...

class XmlSerializerNamespaces(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def Count(self) -> System.Int32:
        ...

    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def __init__(self, namespaces: System.Xml.Serialization.XmlSerializerNamespaces, ):
        ...

    @typing.overload
    def __init__(self, namespaces: list[System.Xml.XmlQualifiedName], ):
        ...

    @typing.overload
    def Add(self, prefix: System.String, ns: System.String, ) -> None:
        ...

    @typing.overload
    def ToArray(self, ) -> list[System.Xml.XmlQualifiedName]:
        ...

