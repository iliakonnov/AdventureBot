from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import System
import System.Xml
import System.Xml.XPath
import System.IO
import System.Text
import System.Threading.Tasks
import System.Xml.Schema
import System.Collections.Generic
import System.Net
import System.Collections


class XmlWriter(System.IDisposable, System.IAsyncDisposable, System.Object, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def Settings(self) -> System.Xml.XmlWriterSettings:
        ...

    @abc.abstractmethod
    @property
    def WriteState(self) -> System.Xml.WriteState:
        ...

    @property
    def XmlSpace(self) -> System.Xml.XmlSpace:
        ...

    @property
    def XmlLang(self) -> System.String:
        ...

    # methods
    @typing.overload
    @abc.abstractmethod
    def WriteStartDocument(self, ) -> None:
        ...

    @typing.overload
    @abc.abstractmethod
    def WriteStartDocument(self, standalone: System.Boolean, ) -> None:
        ...

    @typing.overload
    @abc.abstractmethod
    def WriteEndDocument(self, ) -> None:
        ...

    @typing.overload
    @abc.abstractmethod
    def WriteDocType(self, name: System.String, pubid: System.String, sysid: System.String, subset: System.String, ) -> None:
        ...

    @typing.overload
    def WriteStartElement(self, localName: System.String, ns: System.String, ) -> None:
        ...

    @typing.overload
    @abc.abstractmethod
    def WriteStartElement(self, prefix: System.String, localName: System.String, ns: System.String, ) -> None:
        ...

    @typing.overload
    def WriteStartElement(self, localName: System.String, ) -> None:
        ...

    @typing.overload
    @abc.abstractmethod
    def WriteEndElement(self, ) -> None:
        ...

    @typing.overload
    @abc.abstractmethod
    def WriteFullEndElement(self, ) -> None:
        ...

    @typing.overload
    def WriteAttributeString(self, localName: System.String, ns: System.String, value: System.String, ) -> None:
        ...

    @typing.overload
    def WriteAttributeString(self, localName: System.String, value: System.String, ) -> None:
        ...

    @typing.overload
    def WriteAttributeString(self, prefix: System.String, localName: System.String, ns: System.String, value: System.String, ) -> None:
        ...

    @typing.overload
    def WriteStartAttribute(self, localName: System.String, ns: System.String, ) -> None:
        ...

    @typing.overload
    @abc.abstractmethod
    def WriteStartAttribute(self, prefix: System.String, localName: System.String, ns: System.String, ) -> None:
        ...

    @typing.overload
    def WriteStartAttribute(self, localName: System.String, ) -> None:
        ...

    @typing.overload
    @abc.abstractmethod
    def WriteEndAttribute(self, ) -> None:
        ...

    @typing.overload
    @abc.abstractmethod
    def WriteCData(self, text: System.String, ) -> None:
        ...

    @typing.overload
    @abc.abstractmethod
    def WriteComment(self, text: System.String, ) -> None:
        ...

    @typing.overload
    @abc.abstractmethod
    def WriteProcessingInstruction(self, name: System.String, text: System.String, ) -> None:
        ...

    @typing.overload
    @abc.abstractmethod
    def WriteEntityRef(self, name: System.String, ) -> None:
        ...

    @typing.overload
    @abc.abstractmethod
    def WriteCharEntity(self, ch: System.Char, ) -> None:
        ...

    @typing.overload
    @abc.abstractmethod
    def WriteWhitespace(self, ws: System.String, ) -> None:
        ...

    @typing.overload
    @abc.abstractmethod
    def WriteString(self, text: System.String, ) -> None:
        ...

    @typing.overload
    @abc.abstractmethod
    def WriteSurrogateCharEntity(self, lowChar: System.Char, highChar: System.Char, ) -> None:
        ...

    @typing.overload
    @abc.abstractmethod
    def WriteChars(self, buffer: list[System.Char], index: System.Int32, count: System.Int32, ) -> None:
        ...

    @typing.overload
    @abc.abstractmethod
    def WriteRaw(self, buffer: list[System.Char], index: System.Int32, count: System.Int32, ) -> None:
        ...

    @typing.overload
    @abc.abstractmethod
    def WriteRaw(self, data: System.String, ) -> None:
        ...

    @typing.overload
    @abc.abstractmethod
    def WriteBase64(self, buffer: list[System.Byte], index: System.Int32, count: System.Int32, ) -> None:
        ...

    @typing.overload
    def WriteBinHex(self, buffer: list[System.Byte], index: System.Int32, count: System.Int32, ) -> None:
        ...

    @typing.overload
    def Close(self, ) -> None:
        ...

    @typing.overload
    @abc.abstractmethod
    def Flush(self, ) -> None:
        ...

    @typing.overload
    @abc.abstractmethod
    def LookupPrefix(self, ns: System.String, ) -> System.String:
        ...

    @typing.overload
    def WriteNmToken(self, name: System.String, ) -> None:
        ...

    @typing.overload
    def WriteName(self, name: System.String, ) -> None:
        ...

    @typing.overload
    def WriteQualifiedName(self, localName: System.String, ns: System.String, ) -> None:
        ...

    @typing.overload
    def WriteValue(self, value: System.Object, ) -> None:
        ...

    @typing.overload
    def WriteValue(self, value: System.String, ) -> None:
        ...

    @typing.overload
    def WriteValue(self, value: System.Boolean, ) -> None:
        ...

    @typing.overload
    def WriteValue(self, value: System.DateTime, ) -> None:
        ...

    @typing.overload
    def WriteValue(self, value: System.DateTimeOffset, ) -> None:
        ...

    @typing.overload
    def WriteValue(self, value: System.Double, ) -> None:
        ...

    @typing.overload
    def WriteValue(self, value: System.Single, ) -> None:
        ...

    @typing.overload
    def WriteValue(self, value: System.Decimal, ) -> None:
        ...

    @typing.overload
    def WriteValue(self, value: System.Int32, ) -> None:
        ...

    @typing.overload
    def WriteValue(self, value: System.Int64, ) -> None:
        ...

    @typing.overload
    def WriteAttributes(self, reader: System.Xml.XmlReader, defattr: System.Boolean, ) -> None:
        ...

    @typing.overload
    def WriteNode(self, reader: System.Xml.XmlReader, defattr: System.Boolean, ) -> None:
        ...

    @typing.overload
    def WriteNode(self, navigator: System.Xml.XPath.XPathNavigator, defattr: System.Boolean, ) -> None:
        ...

    @typing.overload
    def WriteElementString(self, localName: System.String, value: System.String, ) -> None:
        ...

    @typing.overload
    def WriteElementString(self, localName: System.String, ns: System.String, value: System.String, ) -> None:
        ...

    @typing.overload
    def WriteElementString(self, prefix: System.String, localName: System.String, ns: System.String, value: System.String, ) -> None:
        ...

    @typing.overload
    def Dispose(self, ) -> None:
        ...

    @typing.overload
    @staticmethod
    def Create(outputFileName: System.String, ) -> System.Xml.XmlWriter:
        ...

    @typing.overload
    @staticmethod
    def Create(outputFileName: System.String, settings: System.Xml.XmlWriterSettings, ) -> System.Xml.XmlWriter:
        ...

    @typing.overload
    @staticmethod
    def Create(output: System.IO.Stream, ) -> System.Xml.XmlWriter:
        ...

    @typing.overload
    @staticmethod
    def Create(output: System.IO.Stream, settings: System.Xml.XmlWriterSettings, ) -> System.Xml.XmlWriter:
        ...

    @typing.overload
    @staticmethod
    def Create(output: System.IO.TextWriter, ) -> System.Xml.XmlWriter:
        ...

    @typing.overload
    @staticmethod
    def Create(output: System.IO.TextWriter, settings: System.Xml.XmlWriterSettings, ) -> System.Xml.XmlWriter:
        ...

    @typing.overload
    @staticmethod
    def Create(output: System.Text.StringBuilder, ) -> System.Xml.XmlWriter:
        ...

    @typing.overload
    @staticmethod
    def Create(output: System.Text.StringBuilder, settings: System.Xml.XmlWriterSettings, ) -> System.Xml.XmlWriter:
        ...

    @typing.overload
    @staticmethod
    def Create(output: System.Xml.XmlWriter, ) -> System.Xml.XmlWriter:
        ...

    @typing.overload
    @staticmethod
    def Create(output: System.Xml.XmlWriter, settings: System.Xml.XmlWriterSettings, ) -> System.Xml.XmlWriter:
        ...

    @typing.overload
    def WriteStartDocumentAsync(self, ) -> System.Threading.Tasks.Task:
        ...

    @typing.overload
    def WriteStartDocumentAsync(self, standalone: System.Boolean, ) -> System.Threading.Tasks.Task:
        ...

    @typing.overload
    def WriteEndDocumentAsync(self, ) -> System.Threading.Tasks.Task:
        ...

    @typing.overload
    def WriteDocTypeAsync(self, name: System.String, pubid: System.String, sysid: System.String, subset: System.String, ) -> System.Threading.Tasks.Task:
        ...

    @typing.overload
    def WriteStartElementAsync(self, prefix: System.String, localName: System.String, ns: System.String, ) -> System.Threading.Tasks.Task:
        ...

    @typing.overload
    def WriteEndElementAsync(self, ) -> System.Threading.Tasks.Task:
        ...

    @typing.overload
    def WriteFullEndElementAsync(self, ) -> System.Threading.Tasks.Task:
        ...

    @typing.overload
    def WriteAttributeStringAsync(self, prefix: System.String, localName: System.String, ns: System.String, value: System.String, ) -> System.Threading.Tasks.Task:
        ...

    @typing.overload
    def WriteCDataAsync(self, text: System.String, ) -> System.Threading.Tasks.Task:
        ...

    @typing.overload
    def WriteCommentAsync(self, text: System.String, ) -> System.Threading.Tasks.Task:
        ...

    @typing.overload
    def WriteProcessingInstructionAsync(self, name: System.String, text: System.String, ) -> System.Threading.Tasks.Task:
        ...

    @typing.overload
    def WriteEntityRefAsync(self, name: System.String, ) -> System.Threading.Tasks.Task:
        ...

    @typing.overload
    def WriteCharEntityAsync(self, ch: System.Char, ) -> System.Threading.Tasks.Task:
        ...

    @typing.overload
    def WriteWhitespaceAsync(self, ws: System.String, ) -> System.Threading.Tasks.Task:
        ...

    @typing.overload
    def WriteStringAsync(self, text: System.String, ) -> System.Threading.Tasks.Task:
        ...

    @typing.overload
    def WriteSurrogateCharEntityAsync(self, lowChar: System.Char, highChar: System.Char, ) -> System.Threading.Tasks.Task:
        ...

    @typing.overload
    def WriteCharsAsync(self, buffer: list[System.Char], index: System.Int32, count: System.Int32, ) -> System.Threading.Tasks.Task:
        ...

    @typing.overload
    def WriteRawAsync(self, buffer: list[System.Char], index: System.Int32, count: System.Int32, ) -> System.Threading.Tasks.Task:
        ...

    @typing.overload
    def WriteRawAsync(self, data: System.String, ) -> System.Threading.Tasks.Task:
        ...

    @typing.overload
    def WriteBase64Async(self, buffer: list[System.Byte], index: System.Int32, count: System.Int32, ) -> System.Threading.Tasks.Task:
        ...

    @typing.overload
    def WriteBinHexAsync(self, buffer: list[System.Byte], index: System.Int32, count: System.Int32, ) -> System.Threading.Tasks.Task:
        ...

    @typing.overload
    def FlushAsync(self, ) -> System.Threading.Tasks.Task:
        ...

    @typing.overload
    def WriteNmTokenAsync(self, name: System.String, ) -> System.Threading.Tasks.Task:
        ...

    @typing.overload
    def WriteNameAsync(self, name: System.String, ) -> System.Threading.Tasks.Task:
        ...

    @typing.overload
    def WriteQualifiedNameAsync(self, localName: System.String, ns: System.String, ) -> System.Threading.Tasks.Task:
        ...

    @typing.overload
    def WriteAttributesAsync(self, reader: System.Xml.XmlReader, defattr: System.Boolean, ) -> System.Threading.Tasks.Task:
        ...

    @typing.overload
    def WriteNodeAsync(self, reader: System.Xml.XmlReader, defattr: System.Boolean, ) -> System.Threading.Tasks.Task:
        ...

    @typing.overload
    def WriteNodeAsync(self, navigator: System.Xml.XPath.XPathNavigator, defattr: System.Boolean, ) -> System.Threading.Tasks.Task:
        ...

    @typing.overload
    def WriteElementStringAsync(self, prefix: System.String, localName: System.String, ns: System.String, value: System.String, ) -> System.Threading.Tasks.Task:
        ...

    @typing.overload
    def DisposeAsync(self, ) -> System.Threading.Tasks.ValueTask:
        ...

class XmlReader(System.IDisposable, System.Object, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def Settings(self) -> System.Xml.XmlReaderSettings:
        ...

    @abc.abstractmethod
    @property
    def NodeType(self) -> System.Xml.XmlNodeType:
        ...

    @property
    def Name(self) -> System.String:
        ...

    @abc.abstractmethod
    @property
    def LocalName(self) -> System.String:
        ...

    @abc.abstractmethod
    @property
    def NamespaceURI(self) -> System.String:
        ...

    @abc.abstractmethod
    @property
    def Prefix(self) -> System.String:
        ...

    @property
    def HasValue(self) -> System.Boolean:
        ...

    @abc.abstractmethod
    @property
    def Value(self) -> System.String:
        ...

    @abc.abstractmethod
    @property
    def Depth(self) -> System.Int32:
        ...

    @abc.abstractmethod
    @property
    def BaseURI(self) -> System.String:
        ...

    @abc.abstractmethod
    @property
    def IsEmptyElement(self) -> System.Boolean:
        ...

    @property
    def IsDefault(self) -> System.Boolean:
        ...

    @property
    def QuoteChar(self) -> System.Char:
        ...

    @property
    def XmlSpace(self) -> System.Xml.XmlSpace:
        ...

    @property
    def XmlLang(self) -> System.String:
        ...

    @property
    def SchemaInfo(self) -> System.Xml.Schema.IXmlSchemaInfo:
        ...

    @property
    def ValueType(self) -> System.Type:
        ...

    @abc.abstractmethod
    @property
    def AttributeCount(self) -> System.Int32:
        ...

    @property
    def Item(self) -> System.String:
        ...

    @property
    def Item(self) -> System.String:
        ...

    @property
    def Item(self) -> System.String:
        ...

    @abc.abstractmethod
    @property
    def EOF(self) -> System.Boolean:
        ...

    @abc.abstractmethod
    @property
    def ReadState(self) -> System.Xml.ReadState:
        ...

    @abc.abstractmethod
    @property
    def NameTable(self) -> System.Xml.XmlNameTable:
        ...

    @property
    def CanResolveEntity(self) -> System.Boolean:
        ...

    @property
    def CanReadBinaryContent(self) -> System.Boolean:
        ...

    @property
    def CanReadValueChunk(self) -> System.Boolean:
        ...

    @property
    def HasAttributes(self) -> System.Boolean:
        ...

    # methods
    @typing.overload
    @staticmethod
    def Create(inputUri: System.String, ) -> System.Xml.XmlReader:
        ...

    @typing.overload
    @staticmethod
    def Create(inputUri: System.String, settings: System.Xml.XmlReaderSettings, ) -> System.Xml.XmlReader:
        ...

    @typing.overload
    @staticmethod
    def Create(inputUri: System.String, settings: System.Xml.XmlReaderSettings, inputContext: System.Xml.XmlParserContext, ) -> System.Xml.XmlReader:
        ...

    @typing.overload
    @staticmethod
    def Create(input: System.IO.Stream, ) -> System.Xml.XmlReader:
        ...

    @typing.overload
    @staticmethod
    def Create(input: System.IO.Stream, settings: System.Xml.XmlReaderSettings, ) -> System.Xml.XmlReader:
        ...

    @typing.overload
    @staticmethod
    def Create(input: System.IO.Stream, settings: System.Xml.XmlReaderSettings, baseUri: System.String, ) -> System.Xml.XmlReader:
        ...

    @typing.overload
    @staticmethod
    def Create(input: System.IO.Stream, settings: System.Xml.XmlReaderSettings, inputContext: System.Xml.XmlParserContext, ) -> System.Xml.XmlReader:
        ...

    @typing.overload
    @staticmethod
    def Create(input: System.IO.TextReader, ) -> System.Xml.XmlReader:
        ...

    @typing.overload
    @staticmethod
    def Create(input: System.IO.TextReader, settings: System.Xml.XmlReaderSettings, ) -> System.Xml.XmlReader:
        ...

    @typing.overload
    @staticmethod
    def Create(input: System.IO.TextReader, settings: System.Xml.XmlReaderSettings, baseUri: System.String, ) -> System.Xml.XmlReader:
        ...

    @typing.overload
    @staticmethod
    def Create(input: System.IO.TextReader, settings: System.Xml.XmlReaderSettings, inputContext: System.Xml.XmlParserContext, ) -> System.Xml.XmlReader:
        ...

    @typing.overload
    @staticmethod
    def Create(reader: System.Xml.XmlReader, settings: System.Xml.XmlReaderSettings, ) -> System.Xml.XmlReader:
        ...

    @typing.overload
    def GetValueAsync(self, ) -> System.Threading.Tasks.Task[System.String]:
        ...

    @typing.overload
    def ReadContentAsObjectAsync(self, ) -> System.Threading.Tasks.Task[System.Object]:
        ...

    @typing.overload
    def ReadContentAsStringAsync(self, ) -> System.Threading.Tasks.Task[System.String]:
        ...

    @typing.overload
    def ReadContentAsAsync(self, returnType: System.Type, namespaceResolver: System.Xml.IXmlNamespaceResolver, ) -> System.Threading.Tasks.Task[System.Object]:
        ...

    @typing.overload
    def ReadElementContentAsObjectAsync(self, ) -> System.Threading.Tasks.Task[System.Object]:
        ...

    @typing.overload
    def ReadElementContentAsStringAsync(self, ) -> System.Threading.Tasks.Task[System.String]:
        ...

    @typing.overload
    def ReadElementContentAsAsync(self, returnType: System.Type, namespaceResolver: System.Xml.IXmlNamespaceResolver, ) -> System.Threading.Tasks.Task[System.Object]:
        ...

    @typing.overload
    def ReadAsync(self, ) -> System.Threading.Tasks.Task[System.Boolean]:
        ...

    @typing.overload
    def SkipAsync(self, ) -> System.Threading.Tasks.Task:
        ...

    @typing.overload
    def ReadContentAsBase64Async(self, buffer: list[System.Byte], index: System.Int32, count: System.Int32, ) -> System.Threading.Tasks.Task[System.Int32]:
        ...

    @typing.overload
    def ReadElementContentAsBase64Async(self, buffer: list[System.Byte], index: System.Int32, count: System.Int32, ) -> System.Threading.Tasks.Task[System.Int32]:
        ...

    @typing.overload
    def ReadContentAsBinHexAsync(self, buffer: list[System.Byte], index: System.Int32, count: System.Int32, ) -> System.Threading.Tasks.Task[System.Int32]:
        ...

    @typing.overload
    def ReadElementContentAsBinHexAsync(self, buffer: list[System.Byte], index: System.Int32, count: System.Int32, ) -> System.Threading.Tasks.Task[System.Int32]:
        ...

    @typing.overload
    def ReadValueChunkAsync(self, buffer: list[System.Char], index: System.Int32, count: System.Int32, ) -> System.Threading.Tasks.Task[System.Int32]:
        ...

    @typing.overload
    def MoveToContentAsync(self, ) -> System.Threading.Tasks.Task[System.Xml.XmlNodeType]:
        ...

    @typing.overload
    def ReadInnerXmlAsync(self, ) -> System.Threading.Tasks.Task[System.String]:
        ...

    @typing.overload
    def ReadOuterXmlAsync(self, ) -> System.Threading.Tasks.Task[System.String]:
        ...

    @typing.overload
    def ReadContentAsObject(self, ) -> System.Object:
        ...

    @typing.overload
    def ReadContentAsBoolean(self, ) -> System.Boolean:
        ...

    @typing.overload
    def ReadContentAsDateTime(self, ) -> System.DateTime:
        ...

    @typing.overload
    def ReadContentAsDateTimeOffset(self, ) -> System.DateTimeOffset:
        ...

    @typing.overload
    def ReadContentAsDouble(self, ) -> System.Double:
        ...

    @typing.overload
    def ReadContentAsFloat(self, ) -> System.Single:
        ...

    @typing.overload
    def ReadContentAsDecimal(self, ) -> System.Decimal:
        ...

    @typing.overload
    def ReadContentAsInt(self, ) -> System.Int32:
        ...

    @typing.overload
    def ReadContentAsLong(self, ) -> System.Int64:
        ...

    @typing.overload
    def ReadContentAsString(self, ) -> System.String:
        ...

    @typing.overload
    def ReadContentAs(self, returnType: System.Type, namespaceResolver: System.Xml.IXmlNamespaceResolver, ) -> System.Object:
        ...

    @typing.overload
    def ReadElementContentAsObject(self, ) -> System.Object:
        ...

    @typing.overload
    def ReadElementContentAsObject(self, localName: System.String, namespaceURI: System.String, ) -> System.Object:
        ...

    @typing.overload
    def ReadElementContentAsBoolean(self, ) -> System.Boolean:
        ...

    @typing.overload
    def ReadElementContentAsBoolean(self, localName: System.String, namespaceURI: System.String, ) -> System.Boolean:
        ...

    @typing.overload
    def ReadElementContentAsDateTime(self, ) -> System.DateTime:
        ...

    @typing.overload
    def ReadElementContentAsDateTime(self, localName: System.String, namespaceURI: System.String, ) -> System.DateTime:
        ...

    @typing.overload
    def ReadElementContentAsDouble(self, ) -> System.Double:
        ...

    @typing.overload
    def ReadElementContentAsDouble(self, localName: System.String, namespaceURI: System.String, ) -> System.Double:
        ...

    @typing.overload
    def ReadElementContentAsFloat(self, ) -> System.Single:
        ...

    @typing.overload
    def ReadElementContentAsFloat(self, localName: System.String, namespaceURI: System.String, ) -> System.Single:
        ...

    @typing.overload
    def ReadElementContentAsDecimal(self, ) -> System.Decimal:
        ...

    @typing.overload
    def ReadElementContentAsDecimal(self, localName: System.String, namespaceURI: System.String, ) -> System.Decimal:
        ...

    @typing.overload
    def ReadElementContentAsInt(self, ) -> System.Int32:
        ...

    @typing.overload
    def ReadElementContentAsInt(self, localName: System.String, namespaceURI: System.String, ) -> System.Int32:
        ...

    @typing.overload
    def ReadElementContentAsLong(self, ) -> System.Int64:
        ...

    @typing.overload
    def ReadElementContentAsLong(self, localName: System.String, namespaceURI: System.String, ) -> System.Int64:
        ...

    @typing.overload
    def ReadElementContentAsString(self, ) -> System.String:
        ...

    @typing.overload
    def ReadElementContentAsString(self, localName: System.String, namespaceURI: System.String, ) -> System.String:
        ...

    @typing.overload
    def ReadElementContentAs(self, returnType: System.Type, namespaceResolver: System.Xml.IXmlNamespaceResolver, ) -> System.Object:
        ...

    @typing.overload
    def ReadElementContentAs(self, returnType: System.Type, namespaceResolver: System.Xml.IXmlNamespaceResolver, localName: System.String, namespaceURI: System.String, ) -> System.Object:
        ...

    @typing.overload
    @abc.abstractmethod
    def GetAttribute(self, name: System.String, ) -> System.String:
        ...

    @typing.overload
    @abc.abstractmethod
    def GetAttribute(self, name: System.String, namespaceURI: System.String, ) -> System.String:
        ...

    @typing.overload
    @abc.abstractmethod
    def GetAttribute(self, i: System.Int32, ) -> System.String:
        ...

    @typing.overload
    @abc.abstractmethod
    def MoveToAttribute(self, name: System.String, ) -> System.Boolean:
        ...

    @typing.overload
    @abc.abstractmethod
    def MoveToAttribute(self, name: System.String, ns: System.String, ) -> System.Boolean:
        ...

    @typing.overload
    def MoveToAttribute(self, i: System.Int32, ) -> None:
        ...

    @typing.overload
    @abc.abstractmethod
    def MoveToFirstAttribute(self, ) -> System.Boolean:
        ...

    @typing.overload
    @abc.abstractmethod
    def MoveToNextAttribute(self, ) -> System.Boolean:
        ...

    @typing.overload
    @abc.abstractmethod
    def MoveToElement(self, ) -> System.Boolean:
        ...

    @typing.overload
    @abc.abstractmethod
    def ReadAttributeValue(self, ) -> System.Boolean:
        ...

    @typing.overload
    @abc.abstractmethod
    def Read(self, ) -> System.Boolean:
        ...

    @typing.overload
    def Close(self, ) -> None:
        ...

    @typing.overload
    def Skip(self, ) -> None:
        ...

    @typing.overload
    @abc.abstractmethod
    def LookupNamespace(self, prefix: System.String, ) -> System.String:
        ...

    @typing.overload
    @abc.abstractmethod
    def ResolveEntity(self, ) -> None:
        ...

    @typing.overload
    def ReadContentAsBase64(self, buffer: list[System.Byte], index: System.Int32, count: System.Int32, ) -> System.Int32:
        ...

    @typing.overload
    def ReadElementContentAsBase64(self, buffer: list[System.Byte], index: System.Int32, count: System.Int32, ) -> System.Int32:
        ...

    @typing.overload
    def ReadContentAsBinHex(self, buffer: list[System.Byte], index: System.Int32, count: System.Int32, ) -> System.Int32:
        ...

    @typing.overload
    def ReadElementContentAsBinHex(self, buffer: list[System.Byte], index: System.Int32, count: System.Int32, ) -> System.Int32:
        ...

    @typing.overload
    def ReadValueChunk(self, buffer: list[System.Char], index: System.Int32, count: System.Int32, ) -> System.Int32:
        ...

    @typing.overload
    def ReadString(self, ) -> System.String:
        ...

    @typing.overload
    def MoveToContent(self, ) -> System.Xml.XmlNodeType:
        ...

    @typing.overload
    def ReadStartElement(self, ) -> None:
        ...

    @typing.overload
    def ReadStartElement(self, name: System.String, ) -> None:
        ...

    @typing.overload
    def ReadStartElement(self, localname: System.String, ns: System.String, ) -> None:
        ...

    @typing.overload
    def ReadElementString(self, ) -> System.String:
        ...

    @typing.overload
    def ReadElementString(self, name: System.String, ) -> System.String:
        ...

    @typing.overload
    def ReadElementString(self, localname: System.String, ns: System.String, ) -> System.String:
        ...

    @typing.overload
    def ReadEndElement(self, ) -> None:
        ...

    @typing.overload
    def IsStartElement(self, ) -> System.Boolean:
        ...

    @typing.overload
    def IsStartElement(self, name: System.String, ) -> System.Boolean:
        ...

    @typing.overload
    def IsStartElement(self, localname: System.String, ns: System.String, ) -> System.Boolean:
        ...

    @typing.overload
    def ReadToFollowing(self, name: System.String, ) -> System.Boolean:
        ...

    @typing.overload
    def ReadToFollowing(self, localName: System.String, namespaceURI: System.String, ) -> System.Boolean:
        ...

    @typing.overload
    def ReadToDescendant(self, name: System.String, ) -> System.Boolean:
        ...

    @typing.overload
    def ReadToDescendant(self, localName: System.String, namespaceURI: System.String, ) -> System.Boolean:
        ...

    @typing.overload
    def ReadToNextSibling(self, name: System.String, ) -> System.Boolean:
        ...

    @typing.overload
    def ReadToNextSibling(self, localName: System.String, namespaceURI: System.String, ) -> System.Boolean:
        ...

    @typing.overload
    @staticmethod
    def IsName(str: System.String, ) -> System.Boolean:
        ...

    @typing.overload
    @staticmethod
    def IsNameToken(str: System.String, ) -> System.Boolean:
        ...

    @typing.overload
    def ReadInnerXml(self, ) -> System.String:
        ...

    @typing.overload
    def ReadOuterXml(self, ) -> System.String:
        ...

    @typing.overload
    def ReadSubtree(self, ) -> System.Xml.XmlReader:
        ...

    @typing.overload
    def Dispose(self, ) -> None:
        ...

class XmlWriterSettings(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def Async(self) -> System.Boolean:
        ...
    @Async.setter
    def Async(self, val: System.Boolean):
        ...

    @property
    def Encoding(self) -> System.Text.Encoding:
        ...
    @Encoding.setter
    def Encoding(self, val: System.Text.Encoding):
        ...

    @property
    def OmitXmlDeclaration(self) -> System.Boolean:
        ...
    @OmitXmlDeclaration.setter
    def OmitXmlDeclaration(self, val: System.Boolean):
        ...

    @property
    def NewLineHandling(self) -> System.Xml.NewLineHandling:
        ...
    @NewLineHandling.setter
    def NewLineHandling(self, val: System.Xml.NewLineHandling):
        ...

    @property
    def NewLineChars(self) -> System.String:
        ...
    @NewLineChars.setter
    def NewLineChars(self, val: System.String):
        ...

    @property
    def Indent(self) -> System.Boolean:
        ...
    @Indent.setter
    def Indent(self, val: System.Boolean):
        ...

    @property
    def IndentChars(self) -> System.String:
        ...
    @IndentChars.setter
    def IndentChars(self, val: System.String):
        ...

    @property
    def NewLineOnAttributes(self) -> System.Boolean:
        ...
    @NewLineOnAttributes.setter
    def NewLineOnAttributes(self, val: System.Boolean):
        ...

    @property
    def CloseOutput(self) -> System.Boolean:
        ...
    @CloseOutput.setter
    def CloseOutput(self, val: System.Boolean):
        ...

    @property
    def ConformanceLevel(self) -> System.Xml.ConformanceLevel:
        ...
    @ConformanceLevel.setter
    def ConformanceLevel(self, val: System.Xml.ConformanceLevel):
        ...

    @property
    def CheckCharacters(self) -> System.Boolean:
        ...
    @CheckCharacters.setter
    def CheckCharacters(self, val: System.Boolean):
        ...

    @property
    def NamespaceHandling(self) -> System.Xml.NamespaceHandling:
        ...
    @NamespaceHandling.setter
    def NamespaceHandling(self, val: System.Xml.NamespaceHandling):
        ...

    @property
    def WriteEndDocumentOnClose(self) -> System.Boolean:
        ...
    @WriteEndDocumentOnClose.setter
    def WriteEndDocumentOnClose(self, val: System.Boolean):
        ...

    @property
    def OutputMethod(self) -> System.Xml.XmlOutputMethod:
        ...

    @property
    def DoNotEscapeUriAttributes(self) -> System.Boolean:
        ...
    @DoNotEscapeUriAttributes.setter
    def DoNotEscapeUriAttributes(self, val: System.Boolean):
        ...

    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def Reset(self, ) -> None:
        ...

    @typing.overload
    def Clone(self, ) -> System.Xml.XmlWriterSettings:
        ...

class WriteState(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    Start: System.Int32 = Start
    Prolog: System.Int32 = Prolog
    Element: System.Int32 = Element
    Attribute: System.Int32 = Attribute
    Content: System.Int32 = Content
    Closed: System.Int32 = Closed
    Error: System.Int32 = Error

class XmlSpace(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    None_: System.Int32 = None
    Default: System.Int32 = Default
    Preserve: System.Int32 = Preserve

class XmlReaderSettings(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def Async(self) -> System.Boolean:
        ...
    @Async.setter
    def Async(self, val: System.Boolean):
        ...

    @property
    def NameTable(self) -> System.Xml.XmlNameTable:
        ...
    @NameTable.setter
    def NameTable(self, val: System.Xml.XmlNameTable):
        ...

    XmlResolver: System.Xml.XmlResolver = property(None, lambda val: ...)

    @property
    def LineNumberOffset(self) -> System.Int32:
        ...
    @LineNumberOffset.setter
    def LineNumberOffset(self, val: System.Int32):
        ...

    @property
    def LinePositionOffset(self) -> System.Int32:
        ...
    @LinePositionOffset.setter
    def LinePositionOffset(self, val: System.Int32):
        ...

    @property
    def ConformanceLevel(self) -> System.Xml.ConformanceLevel:
        ...
    @ConformanceLevel.setter
    def ConformanceLevel(self, val: System.Xml.ConformanceLevel):
        ...

    @property
    def CheckCharacters(self) -> System.Boolean:
        ...
    @CheckCharacters.setter
    def CheckCharacters(self, val: System.Boolean):
        ...

    @property
    def MaxCharactersInDocument(self) -> System.Int64:
        ...
    @MaxCharactersInDocument.setter
    def MaxCharactersInDocument(self, val: System.Int64):
        ...

    @property
    def MaxCharactersFromEntities(self) -> System.Int64:
        ...
    @MaxCharactersFromEntities.setter
    def MaxCharactersFromEntities(self, val: System.Int64):
        ...

    @property
    def IgnoreWhitespace(self) -> System.Boolean:
        ...
    @IgnoreWhitespace.setter
    def IgnoreWhitespace(self, val: System.Boolean):
        ...

    @property
    def IgnoreProcessingInstructions(self) -> System.Boolean:
        ...
    @IgnoreProcessingInstructions.setter
    def IgnoreProcessingInstructions(self, val: System.Boolean):
        ...

    @property
    def IgnoreComments(self) -> System.Boolean:
        ...
    @IgnoreComments.setter
    def IgnoreComments(self, val: System.Boolean):
        ...

    @property
    def ProhibitDtd(self) -> System.Boolean:
        ...
    @ProhibitDtd.setter
    def ProhibitDtd(self, val: System.Boolean):
        ...

    @property
    def DtdProcessing(self) -> System.Xml.DtdProcessing:
        ...
    @DtdProcessing.setter
    def DtdProcessing(self, val: System.Xml.DtdProcessing):
        ...

    @property
    def CloseInput(self) -> System.Boolean:
        ...
    @CloseInput.setter
    def CloseInput(self, val: System.Boolean):
        ...

    @property
    def ValidationType(self) -> System.Xml.ValidationType:
        ...
    @ValidationType.setter
    def ValidationType(self, val: System.Xml.ValidationType):
        ...

    @property
    def ValidationFlags(self) -> System.Xml.Schema.XmlSchemaValidationFlags:
        ...
    @ValidationFlags.setter
    def ValidationFlags(self, val: System.Xml.Schema.XmlSchemaValidationFlags):
        ...

    @property
    def Schemas(self) -> System.Xml.Schema.XmlSchemaSet:
        ...
    @Schemas.setter
    def Schemas(self, val: System.Xml.Schema.XmlSchemaSet):
        ...

    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def Reset(self, ) -> None:
        ...

    @typing.overload
    def Clone(self, ) -> System.Xml.XmlReaderSettings:
        ...

class XmlNodeType(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    None_: System.Int32 = None
    Element: System.Int32 = Element
    Attribute: System.Int32 = Attribute
    Text: System.Int32 = Text
    CDATA: System.Int32 = CDATA
    EntityReference: System.Int32 = EntityReference
    Entity: System.Int32 = Entity
    ProcessingInstruction: System.Int32 = ProcessingInstruction
    Comment: System.Int32 = Comment
    Document: System.Int32 = Document
    DocumentType: System.Int32 = DocumentType
    DocumentFragment: System.Int32 = DocumentFragment
    Notation: System.Int32 = Notation
    Whitespace: System.Int32 = Whitespace
    SignificantWhitespace: System.Int32 = SignificantWhitespace
    EndElement: System.Int32 = EndElement
    EndEntity: System.Int32 = EndEntity
    XmlDeclaration: System.Int32 = XmlDeclaration

class ReadState(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    Initial: System.Int32 = Initial
    Interactive: System.Int32 = Interactive
    Error: System.Int32 = Error
    EndOfFile: System.Int32 = EndOfFile
    Closed: System.Int32 = Closed

class XmlNameTable(System.Object, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    # methods
    @typing.overload
    @abc.abstractmethod
    def Get(self, array: list[System.Char], offset: System.Int32, length: System.Int32, ) -> System.String:
        ...

    @typing.overload
    @abc.abstractmethod
    def Get(self, array: System.String, ) -> System.String:
        ...

    @typing.overload
    @abc.abstractmethod
    def Add(self, array: list[System.Char], offset: System.Int32, length: System.Int32, ) -> System.String:
        ...

    @typing.overload
    @abc.abstractmethod
    def Add(self, array: System.String, ) -> System.String:
        ...

class XmlParserContext(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def NameTable(self) -> System.Xml.XmlNameTable:
        ...
    @NameTable.setter
    def NameTable(self, val: System.Xml.XmlNameTable):
        ...

    @property
    def NamespaceManager(self) -> System.Xml.XmlNamespaceManager:
        ...
    @NamespaceManager.setter
    def NamespaceManager(self, val: System.Xml.XmlNamespaceManager):
        ...

    @property
    def DocTypeName(self) -> System.String:
        ...
    @DocTypeName.setter
    def DocTypeName(self, val: System.String):
        ...

    @property
    def PublicId(self) -> System.String:
        ...
    @PublicId.setter
    def PublicId(self, val: System.String):
        ...

    @property
    def SystemId(self) -> System.String:
        ...
    @SystemId.setter
    def SystemId(self, val: System.String):
        ...

    @property
    def BaseURI(self) -> System.String:
        ...
    @BaseURI.setter
    def BaseURI(self, val: System.String):
        ...

    @property
    def InternalSubset(self) -> System.String:
        ...
    @InternalSubset.setter
    def InternalSubset(self, val: System.String):
        ...

    @property
    def XmlLang(self) -> System.String:
        ...
    @XmlLang.setter
    def XmlLang(self, val: System.String):
        ...

    @property
    def XmlSpace(self) -> System.Xml.XmlSpace:
        ...
    @XmlSpace.setter
    def XmlSpace(self, val: System.Xml.XmlSpace):
        ...

    @property
    def Encoding(self) -> System.Text.Encoding:
        ...
    @Encoding.setter
    def Encoding(self, val: System.Text.Encoding):
        ...

    # methods
    @typing.overload
    def __init__(self, nt: System.Xml.XmlNameTable, nsMgr: System.Xml.XmlNamespaceManager, xmlLang: System.String, xmlSpace: System.Xml.XmlSpace, ):
        ...

    @typing.overload
    def __init__(self, nt: System.Xml.XmlNameTable, nsMgr: System.Xml.XmlNamespaceManager, xmlLang: System.String, xmlSpace: System.Xml.XmlSpace, enc: System.Text.Encoding, ):
        ...

    @typing.overload
    def __init__(self, nt: System.Xml.XmlNameTable, nsMgr: System.Xml.XmlNamespaceManager, docTypeName: System.String, pubId: System.String, sysId: System.String, internalSubset: System.String, baseURI: System.String, xmlLang: System.String, xmlSpace: System.Xml.XmlSpace, ):
        ...

    @typing.overload
    def __init__(self, nt: System.Xml.XmlNameTable, nsMgr: System.Xml.XmlNamespaceManager, docTypeName: System.String, pubId: System.String, sysId: System.String, internalSubset: System.String, baseURI: System.String, xmlLang: System.String, xmlSpace: System.Xml.XmlSpace, enc: System.Text.Encoding, ):
        ...

class IXmlNamespaceResolver(abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    # methods
    @typing.overload
    @abc.abstractmethod
    def GetNamespacesInScope(self, scope: System.Xml.XmlNamespaceScope, ) -> System.Collections.Generic.IDictionary[System.String, System.String]:
        ...

    @typing.overload
    @abc.abstractmethod
    def LookupNamespace(self, prefix: System.String, ) -> System.String:
        ...

    @typing.overload
    @abc.abstractmethod
    def LookupPrefix(self, namespaceName: System.String, ) -> System.String:
        ...

class XmlResolver(System.Object, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    Credentials: System.Net.ICredentials = property(None, lambda val: ...)

    # methods
    @typing.overload
    @abc.abstractmethod
    def GetEntity(self, absoluteUri: System.Uri, role: System.String, ofObjectToReturn: System.Type, ) -> System.Object:
        ...

    @typing.overload
    def ResolveUri(self, baseUri: System.Uri, relativeUri: System.String, ) -> System.Uri:
        ...

    @typing.overload
    def SupportsType(self, absoluteUri: System.Uri, type: System.Type, ) -> System.Boolean:
        ...

    @typing.overload
    def GetEntityAsync(self, absoluteUri: System.Uri, role: System.String, ofObjectToReturn: System.Type, ) -> System.Threading.Tasks.Task[System.Object]:
        ...

class XmlQualifiedName(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def Namespace(self) -> System.String:
        ...

    @property
    def Name(self) -> System.String:
        ...

    @property
    def IsEmpty(self) -> System.Boolean:
        ...

    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def __init__(self, name: System.String, ):
        ...

    @typing.overload
    def __init__(self, name: System.String, ns: System.String, ):
        ...

    @typing.overload
    def GetHashCode(self, ) -> System.Int32:
        ...

    @typing.overload
    def ToString(self, ) -> System.String:
        ...

    @typing.overload
    def Equals(self, other: System.Object, ) -> System.Boolean:
        ...

    @typing.overload
    @staticmethod
    def ToString(name: System.String, ns: System.String, ) -> System.String:
        ...

class XmlAttribute(System.ICloneable, System.Collections.IEnumerable, System.Xml.XPath.IXPathNavigable, System.Xml.XmlNode):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def ParentNode(self) -> System.Xml.XmlNode:
        ...

    @property
    def Name(self) -> System.String:
        ...

    @property
    def LocalName(self) -> System.String:
        ...

    @property
    def NamespaceURI(self) -> System.String:
        ...

    @property
    def Prefix(self) -> System.String:
        ...
    @Prefix.setter
    def Prefix(self, val: System.String):
        ...

    @property
    def NodeType(self) -> System.Xml.XmlNodeType:
        ...

    @property
    def OwnerDocument(self) -> System.Xml.XmlDocument:
        ...

    @property
    def Value(self) -> System.String:
        ...
    @Value.setter
    def Value(self, val: System.String):
        ...

    @property
    def SchemaInfo(self) -> System.Xml.Schema.IXmlSchemaInfo:
        ...

    InnerText: System.String = property(None, lambda val: ...)

    @property
    def Specified(self) -> System.Boolean:
        ...

    @property
    def OwnerElement(self) -> System.Xml.XmlElement:
        ...

    InnerXml: System.String = property(None, lambda val: ...)

    @property
    def BaseURI(self) -> System.String:
        ...

    @property
    def ChildNodes(self) -> System.Xml.XmlNodeList:
        ...

    @property
    def PreviousSibling(self) -> System.Xml.XmlNode:
        ...

    @property
    def NextSibling(self) -> System.Xml.XmlNode:
        ...

    @property
    def Attributes(self) -> System.Xml.XmlAttributeCollection:
        ...

    @property
    def FirstChild(self) -> System.Xml.XmlNode:
        ...

    @property
    def LastChild(self) -> System.Xml.XmlNode:
        ...

    @property
    def HasChildNodes(self) -> System.Boolean:
        ...

    @property
    def IsReadOnly(self) -> System.Boolean:
        ...

    @property
    def OuterXml(self) -> System.String:
        ...

    @property
    def Item(self) -> System.Xml.XmlElement:
        ...

    @property
    def Item(self) -> System.Xml.XmlElement:
        ...

    @property
    def PreviousText(self) -> System.Xml.XmlNode:
        ...

    # methods
    @typing.overload
    def CloneNode(self, deep: System.Boolean, ) -> System.Xml.XmlNode:
        ...

    @typing.overload
    def InsertBefore(self, newChild: System.Xml.XmlNode, refChild: System.Xml.XmlNode, ) -> System.Xml.XmlNode:
        ...

    @typing.overload
    def InsertAfter(self, newChild: System.Xml.XmlNode, refChild: System.Xml.XmlNode, ) -> System.Xml.XmlNode:
        ...

    @typing.overload
    def ReplaceChild(self, newChild: System.Xml.XmlNode, oldChild: System.Xml.XmlNode, ) -> System.Xml.XmlNode:
        ...

    @typing.overload
    def RemoveChild(self, oldChild: System.Xml.XmlNode, ) -> System.Xml.XmlNode:
        ...

    @typing.overload
    def PrependChild(self, newChild: System.Xml.XmlNode, ) -> System.Xml.XmlNode:
        ...

    @typing.overload
    def AppendChild(self, newChild: System.Xml.XmlNode, ) -> System.Xml.XmlNode:
        ...

    @typing.overload
    def WriteTo(self, w: System.Xml.XmlWriter, ) -> None:
        ...

    @typing.overload
    def WriteContentTo(self, w: System.Xml.XmlWriter, ) -> None:
        ...

class XmlNamespaceManager(System.Xml.IXmlNamespaceResolver, System.Collections.IEnumerable, System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def NameTable(self) -> System.Xml.XmlNameTable:
        ...

    @property
    def DefaultNamespace(self) -> System.String:
        ...

    # methods
    @typing.overload
    def __init__(self, nameTable: System.Xml.XmlNameTable, ):
        ...

    @typing.overload
    def PushScope(self, ) -> None:
        ...

    @typing.overload
    def PopScope(self, ) -> System.Boolean:
        ...

    @typing.overload
    def AddNamespace(self, prefix: System.String, uri: System.String, ) -> None:
        ...

    @typing.overload
    def RemoveNamespace(self, prefix: System.String, uri: System.String, ) -> None:
        ...

    @typing.overload
    def GetEnumerator(self, ) -> System.Collections.IEnumerator:
        ...

    @typing.overload
    def GetNamespacesInScope(self, scope: System.Xml.XmlNamespaceScope, ) -> System.Collections.Generic.IDictionary[System.String, System.String]:
        ...

    @typing.overload
    def LookupNamespace(self, prefix: System.String, ) -> System.String:
        ...

    @typing.overload
    def LookupPrefix(self, uri: System.String, ) -> System.String:
        ...

    @typing.overload
    def HasNamespace(self, prefix: System.String, ) -> System.Boolean:
        ...

class NewLineHandling(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    Replace: System.Int32 = Replace
    Entitize: System.Int32 = Entitize
    None_: System.Int32 = None

class ConformanceLevel(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    Auto: System.Int32 = Auto
    Fragment: System.Int32 = Fragment
    Document: System.Int32 = Document

class NamespaceHandling(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    Default: System.Int32 = Default
    OmitDuplicates: System.Int32 = OmitDuplicates

class XmlOutputMethod(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    Xml: System.Int32 = Xml
    Html: System.Int32 = Html
    Text: System.Int32 = Text
    AutoDetect: System.Int32 = AutoDetect

class XmlNamespaceScope(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    All: System.Int32 = All
    ExcludeXml: System.Int32 = ExcludeXml
    Local: System.Int32 = Local

class XmlNodeOrder(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    Before: System.Int32 = Before
    After: System.Int32 = After
    Same: System.Int32 = Same
    Unknown: System.Int32 = Unknown

class DtdProcessing(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    Prohibit: System.Int32 = Prohibit
    Ignore: System.Int32 = Ignore
    Parse: System.Int32 = Parse

class ValidationType(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    None_: System.Int32 = None
    Auto: System.Int32 = Auto
    DTD: System.Int32 = DTD
    XDR: System.Int32 = XDR
    Schema: System.Int32 = Schema

class XmlTokenizedType(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    CDATA: System.Int32 = CDATA
    ID: System.Int32 = ID
    IDREF: System.Int32 = IDREF
    IDREFS: System.Int32 = IDREFS
    ENTITY: System.Int32 = ENTITY
    ENTITIES: System.Int32 = ENTITIES
    NMTOKEN: System.Int32 = NMTOKEN
    NMTOKENS: System.Int32 = NMTOKENS
    NOTATION: System.Int32 = NOTATION
    ENUMERATION: System.Int32 = ENUMERATION
    QName: System.Int32 = QName
    NCName: System.Int32 = NCName
    None_: System.Int32 = None

class XmlNode(System.ICloneable, System.Collections.IEnumerable, System.Xml.XPath.IXPathNavigable, System.Object, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @abc.abstractmethod
    @property
    def Name(self) -> System.String:
        ...

    @property
    def Value(self) -> System.String:
        ...
    @Value.setter
    def Value(self, val: System.String):
        ...

    @abc.abstractmethod
    @property
    def NodeType(self) -> System.Xml.XmlNodeType:
        ...

    @property
    def ParentNode(self) -> System.Xml.XmlNode:
        ...

    @property
    def ChildNodes(self) -> System.Xml.XmlNodeList:
        ...

    @property
    def PreviousSibling(self) -> System.Xml.XmlNode:
        ...

    @property
    def NextSibling(self) -> System.Xml.XmlNode:
        ...

    @property
    def Attributes(self) -> System.Xml.XmlAttributeCollection:
        ...

    @property
    def OwnerDocument(self) -> System.Xml.XmlDocument:
        ...

    @property
    def FirstChild(self) -> System.Xml.XmlNode:
        ...

    @property
    def LastChild(self) -> System.Xml.XmlNode:
        ...

    @property
    def HasChildNodes(self) -> System.Boolean:
        ...

    @property
    def NamespaceURI(self) -> System.String:
        ...

    @property
    def Prefix(self) -> System.String:
        ...
    @Prefix.setter
    def Prefix(self, val: System.String):
        ...

    @abc.abstractmethod
    @property
    def LocalName(self) -> System.String:
        ...

    @property
    def IsReadOnly(self) -> System.Boolean:
        ...

    @property
    def InnerText(self) -> System.String:
        ...
    @InnerText.setter
    def InnerText(self, val: System.String):
        ...

    @property
    def OuterXml(self) -> System.String:
        ...

    @property
    def InnerXml(self) -> System.String:
        ...
    @InnerXml.setter
    def InnerXml(self, val: System.String):
        ...

    @property
    def SchemaInfo(self) -> System.Xml.Schema.IXmlSchemaInfo:
        ...

    @property
    def BaseURI(self) -> System.String:
        ...

    @property
    def Item(self) -> System.Xml.XmlElement:
        ...

    @property
    def Item(self) -> System.Xml.XmlElement:
        ...

    @property
    def PreviousText(self) -> System.Xml.XmlNode:
        ...

    # methods
    @typing.overload
    @abc.abstractmethod
    def CloneNode(self, deep: System.Boolean, ) -> System.Xml.XmlNode:
        ...

    @typing.overload
    def InsertBefore(self, newChild: System.Xml.XmlNode, refChild: System.Xml.XmlNode, ) -> System.Xml.XmlNode:
        ...

    @typing.overload
    def InsertAfter(self, newChild: System.Xml.XmlNode, refChild: System.Xml.XmlNode, ) -> System.Xml.XmlNode:
        ...

    @typing.overload
    def ReplaceChild(self, newChild: System.Xml.XmlNode, oldChild: System.Xml.XmlNode, ) -> System.Xml.XmlNode:
        ...

    @typing.overload
    def RemoveChild(self, oldChild: System.Xml.XmlNode, ) -> System.Xml.XmlNode:
        ...

    @typing.overload
    def PrependChild(self, newChild: System.Xml.XmlNode, ) -> System.Xml.XmlNode:
        ...

    @typing.overload
    def AppendChild(self, newChild: System.Xml.XmlNode, ) -> System.Xml.XmlNode:
        ...

    @typing.overload
    @abc.abstractmethod
    def WriteTo(self, w: System.Xml.XmlWriter, ) -> None:
        ...

    @typing.overload
    @abc.abstractmethod
    def WriteContentTo(self, w: System.Xml.XmlWriter, ) -> None:
        ...

    @typing.overload
    def CreateNavigator(self, ) -> System.Xml.XPath.XPathNavigator:
        ...

    @typing.overload
    def SelectSingleNode(self, xpath: System.String, ) -> System.Xml.XmlNode:
        ...

    @typing.overload
    def SelectSingleNode(self, xpath: System.String, nsmgr: System.Xml.XmlNamespaceManager, ) -> System.Xml.XmlNode:
        ...

    @typing.overload
    def SelectNodes(self, xpath: System.String, ) -> System.Xml.XmlNodeList:
        ...

    @typing.overload
    def SelectNodes(self, xpath: System.String, nsmgr: System.Xml.XmlNamespaceManager, ) -> System.Xml.XmlNodeList:
        ...

    @typing.overload
    def Normalize(self, ) -> None:
        ...

    @typing.overload
    def Supports(self, feature: System.String, version: System.String, ) -> System.Boolean:
        ...

    @typing.overload
    def Clone(self, ) -> System.Xml.XmlNode:
        ...

    @typing.overload
    def GetEnumerator(self, ) -> System.Collections.IEnumerator:
        ...

    @typing.overload
    def RemoveAll(self, ) -> None:
        ...

    @typing.overload
    def GetNamespaceOfPrefix(self, prefix: System.String, ) -> System.String:
        ...

    @typing.overload
    def GetPrefixOfNamespace(self, namespaceURI: System.String, ) -> System.String:
        ...

class XmlDocument(System.ICloneable, System.Collections.IEnumerable, System.Xml.XPath.IXPathNavigable, System.Xml.XmlNode):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def NodeType(self) -> System.Xml.XmlNodeType:
        ...

    @property
    def ParentNode(self) -> System.Xml.XmlNode:
        ...

    @property
    def DocumentType(self) -> System.Xml.XmlDocumentType:
        ...

    @property
    def Implementation(self) -> System.Xml.XmlImplementation:
        ...

    @property
    def Name(self) -> System.String:
        ...

    @property
    def LocalName(self) -> System.String:
        ...

    @property
    def DocumentElement(self) -> System.Xml.XmlElement:
        ...

    @property
    def OwnerDocument(self) -> System.Xml.XmlDocument:
        ...

    @property
    def Schemas(self) -> System.Xml.Schema.XmlSchemaSet:
        ...
    @Schemas.setter
    def Schemas(self, val: System.Xml.Schema.XmlSchemaSet):
        ...

    XmlResolver: System.Xml.XmlResolver = property(None, lambda val: ...)

    @property
    def NameTable(self) -> System.Xml.XmlNameTable:
        ...

    @property
    def PreserveWhitespace(self) -> System.Boolean:
        ...
    @PreserveWhitespace.setter
    def PreserveWhitespace(self, val: System.Boolean):
        ...

    @property
    def IsReadOnly(self) -> System.Boolean:
        ...

    InnerText: System.String = property(None, lambda val: ...)

    @property
    def InnerXml(self) -> System.String:
        ...
    @InnerXml.setter
    def InnerXml(self, val: System.String):
        ...

    @property
    def SchemaInfo(self) -> System.Xml.Schema.IXmlSchemaInfo:
        ...

    @property
    def BaseURI(self) -> System.String:
        ...

    @property
    def Value(self) -> System.String:
        ...
    @Value.setter
    def Value(self, val: System.String):
        ...

    @property
    def ChildNodes(self) -> System.Xml.XmlNodeList:
        ...

    @property
    def PreviousSibling(self) -> System.Xml.XmlNode:
        ...

    @property
    def NextSibling(self) -> System.Xml.XmlNode:
        ...

    @property
    def Attributes(self) -> System.Xml.XmlAttributeCollection:
        ...

    @property
    def FirstChild(self) -> System.Xml.XmlNode:
        ...

    @property
    def LastChild(self) -> System.Xml.XmlNode:
        ...

    @property
    def HasChildNodes(self) -> System.Boolean:
        ...

    @property
    def NamespaceURI(self) -> System.String:
        ...

    @property
    def Prefix(self) -> System.String:
        ...
    @Prefix.setter
    def Prefix(self, val: System.String):
        ...

    @property
    def OuterXml(self) -> System.String:
        ...

    @property
    def Item(self) -> System.Xml.XmlElement:
        ...

    @property
    def Item(self) -> System.Xml.XmlElement:
        ...

    @property
    def PreviousText(self) -> System.Xml.XmlNode:
        ...

    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def __init__(self, nt: System.Xml.XmlNameTable, ):
        ...

    @typing.overload
    def CloneNode(self, deep: System.Boolean, ) -> System.Xml.XmlNode:
        ...

    @typing.overload
    def CreateAttribute(self, name: System.String, ) -> System.Xml.XmlAttribute:
        ...

    @typing.overload
    def CreateCDataSection(self, data: System.String, ) -> System.Xml.XmlCDataSection:
        ...

    @typing.overload
    def CreateComment(self, data: System.String, ) -> System.Xml.XmlComment:
        ...

    @typing.overload
    def CreateDocumentType(self, name: System.String, publicId: System.String, systemId: System.String, internalSubset: System.String, ) -> System.Xml.XmlDocumentType:
        ...

    @typing.overload
    def CreateDocumentFragment(self, ) -> System.Xml.XmlDocumentFragment:
        ...

    @typing.overload
    def CreateElement(self, name: System.String, ) -> System.Xml.XmlElement:
        ...

    @typing.overload
    def CreateEntityReference(self, name: System.String, ) -> System.Xml.XmlEntityReference:
        ...

    @typing.overload
    def CreateProcessingInstruction(self, target: System.String, data: System.String, ) -> System.Xml.XmlProcessingInstruction:
        ...

    @typing.overload
    def CreateXmlDeclaration(self, version: System.String, encoding: System.String, standalone: System.String, ) -> System.Xml.XmlDeclaration:
        ...

    @typing.overload
    def CreateTextNode(self, text: System.String, ) -> System.Xml.XmlText:
        ...

    @typing.overload
    def CreateSignificantWhitespace(self, text: System.String, ) -> System.Xml.XmlSignificantWhitespace:
        ...

    @typing.overload
    def CreateNavigator(self, ) -> System.Xml.XPath.XPathNavigator:
        ...

    @typing.overload
    def CreateWhitespace(self, text: System.String, ) -> System.Xml.XmlWhitespace:
        ...

    @typing.overload
    def GetElementsByTagName(self, name: System.String, ) -> System.Xml.XmlNodeList:
        ...

    @typing.overload
    def CreateAttribute(self, qualifiedName: System.String, namespaceURI: System.String, ) -> System.Xml.XmlAttribute:
        ...

    @typing.overload
    def CreateElement(self, qualifiedName: System.String, namespaceURI: System.String, ) -> System.Xml.XmlElement:
        ...

    @typing.overload
    def GetElementsByTagName(self, localName: System.String, namespaceURI: System.String, ) -> System.Xml.XmlNodeList:
        ...

    @typing.overload
    def GetElementById(self, elementId: System.String, ) -> System.Xml.XmlElement:
        ...

    @typing.overload
    def ImportNode(self, node: System.Xml.XmlNode, deep: System.Boolean, ) -> System.Xml.XmlNode:
        ...

    @typing.overload
    def CreateAttribute(self, prefix: System.String, localName: System.String, namespaceURI: System.String, ) -> System.Xml.XmlAttribute:
        ...

    @typing.overload
    def CreateElement(self, prefix: System.String, localName: System.String, namespaceURI: System.String, ) -> System.Xml.XmlElement:
        ...

    @typing.overload
    def CreateNode(self, type: System.Xml.XmlNodeType, prefix: System.String, name: System.String, namespaceURI: System.String, ) -> System.Xml.XmlNode:
        ...

    @typing.overload
    def CreateNode(self, nodeTypeString: System.String, name: System.String, namespaceURI: System.String, ) -> System.Xml.XmlNode:
        ...

    @typing.overload
    def CreateNode(self, type: System.Xml.XmlNodeType, name: System.String, namespaceURI: System.String, ) -> System.Xml.XmlNode:
        ...

    @typing.overload
    def ReadNode(self, reader: System.Xml.XmlReader, ) -> System.Xml.XmlNode:
        ...

    @typing.overload
    def Load(self, filename: System.String, ) -> None:
        ...

    @typing.overload
    def Load(self, inStream: System.IO.Stream, ) -> None:
        ...

    @typing.overload
    def Load(self, txtReader: System.IO.TextReader, ) -> None:
        ...

    @typing.overload
    def Load(self, reader: System.Xml.XmlReader, ) -> None:
        ...

    @typing.overload
    def LoadXml(self, xml: System.String, ) -> None:
        ...

    @typing.overload
    def Save(self, filename: System.String, ) -> None:
        ...

    @typing.overload
    def Save(self, outStream: System.IO.Stream, ) -> None:
        ...

    @typing.overload
    def Save(self, writer: System.IO.TextWriter, ) -> None:
        ...

    @typing.overload
    def Save(self, w: System.Xml.XmlWriter, ) -> None:
        ...

    @typing.overload
    def WriteTo(self, w: System.Xml.XmlWriter, ) -> None:
        ...

    @typing.overload
    def WriteContentTo(self, xw: System.Xml.XmlWriter, ) -> None:
        ...

    @typing.overload
    def Validate(self, validationEventHandler: System.Xml.Schema.ValidationEventHandler, ) -> None:
        ...

    @typing.overload
    def Validate(self, validationEventHandler: System.Xml.Schema.ValidationEventHandler, nodeToValidate: System.Xml.XmlNode, ) -> None:
        ...

class XmlElement(System.ICloneable, System.Collections.IEnumerable, System.Xml.XPath.IXPathNavigable, System.Xml.XmlLinkedNode):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def Name(self) -> System.String:
        ...

    @property
    def LocalName(self) -> System.String:
        ...

    @property
    def NamespaceURI(self) -> System.String:
        ...

    @property
    def Prefix(self) -> System.String:
        ...
    @Prefix.setter
    def Prefix(self, val: System.String):
        ...

    @property
    def NodeType(self) -> System.Xml.XmlNodeType:
        ...

    @property
    def ParentNode(self) -> System.Xml.XmlNode:
        ...

    @property
    def OwnerDocument(self) -> System.Xml.XmlDocument:
        ...

    @property
    def IsEmpty(self) -> System.Boolean:
        ...
    @IsEmpty.setter
    def IsEmpty(self, val: System.Boolean):
        ...

    @property
    def Attributes(self) -> System.Xml.XmlAttributeCollection:
        ...

    @property
    def HasAttributes(self) -> System.Boolean:
        ...

    @property
    def SchemaInfo(self) -> System.Xml.Schema.IXmlSchemaInfo:
        ...

    @property
    def InnerXml(self) -> System.String:
        ...
    @InnerXml.setter
    def InnerXml(self, val: System.String):
        ...

    @property
    def InnerText(self) -> System.String:
        ...
    @InnerText.setter
    def InnerText(self, val: System.String):
        ...

    @property
    def NextSibling(self) -> System.Xml.XmlNode:
        ...

    @property
    def PreviousSibling(self) -> System.Xml.XmlNode:
        ...

    @property
    def Value(self) -> System.String:
        ...
    @Value.setter
    def Value(self, val: System.String):
        ...

    @property
    def ChildNodes(self) -> System.Xml.XmlNodeList:
        ...

    @property
    def FirstChild(self) -> System.Xml.XmlNode:
        ...

    @property
    def LastChild(self) -> System.Xml.XmlNode:
        ...

    @property
    def HasChildNodes(self) -> System.Boolean:
        ...

    @property
    def IsReadOnly(self) -> System.Boolean:
        ...

    @property
    def OuterXml(self) -> System.String:
        ...

    @property
    def BaseURI(self) -> System.String:
        ...

    @property
    def Item(self) -> System.Xml.XmlElement:
        ...

    @property
    def Item(self) -> System.Xml.XmlElement:
        ...

    @property
    def PreviousText(self) -> System.Xml.XmlNode:
        ...

    # methods
    @typing.overload
    def CloneNode(self, deep: System.Boolean, ) -> System.Xml.XmlNode:
        ...

    @typing.overload
    def GetAttribute(self, name: System.String, ) -> System.String:
        ...

    @typing.overload
    def SetAttribute(self, name: System.String, value: System.String, ) -> None:
        ...

    @typing.overload
    def RemoveAttribute(self, name: System.String, ) -> None:
        ...

    @typing.overload
    def GetAttributeNode(self, name: System.String, ) -> System.Xml.XmlAttribute:
        ...

    @typing.overload
    def SetAttributeNode(self, newAttr: System.Xml.XmlAttribute, ) -> System.Xml.XmlAttribute:
        ...

    @typing.overload
    def RemoveAttributeNode(self, oldAttr: System.Xml.XmlAttribute, ) -> System.Xml.XmlAttribute:
        ...

    @typing.overload
    def GetElementsByTagName(self, name: System.String, ) -> System.Xml.XmlNodeList:
        ...

    @typing.overload
    def GetAttribute(self, localName: System.String, namespaceURI: System.String, ) -> System.String:
        ...

    @typing.overload
    def SetAttribute(self, localName: System.String, namespaceURI: System.String, value: System.String, ) -> System.String:
        ...

    @typing.overload
    def RemoveAttribute(self, localName: System.String, namespaceURI: System.String, ) -> None:
        ...

    @typing.overload
    def GetAttributeNode(self, localName: System.String, namespaceURI: System.String, ) -> System.Xml.XmlAttribute:
        ...

    @typing.overload
    def SetAttributeNode(self, localName: System.String, namespaceURI: System.String, ) -> System.Xml.XmlAttribute:
        ...

    @typing.overload
    def RemoveAttributeNode(self, localName: System.String, namespaceURI: System.String, ) -> System.Xml.XmlAttribute:
        ...

    @typing.overload
    def GetElementsByTagName(self, localName: System.String, namespaceURI: System.String, ) -> System.Xml.XmlNodeList:
        ...

    @typing.overload
    def HasAttribute(self, name: System.String, ) -> System.Boolean:
        ...

    @typing.overload
    def HasAttribute(self, localName: System.String, namespaceURI: System.String, ) -> System.Boolean:
        ...

    @typing.overload
    def WriteTo(self, w: System.Xml.XmlWriter, ) -> None:
        ...

    @typing.overload
    def WriteContentTo(self, w: System.Xml.XmlWriter, ) -> None:
        ...

    @typing.overload
    def RemoveAttributeAt(self, i: System.Int32, ) -> System.Xml.XmlNode:
        ...

    @typing.overload
    def RemoveAllAttributes(self, ) -> None:
        ...

    @typing.overload
    def RemoveAll(self, ) -> None:
        ...

class XmlNodeList(System.Collections.IEnumerable, System.IDisposable, System.Object, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @abc.abstractmethod
    @property
    def Count(self) -> System.Int32:
        ...

    @property
    def ItemOf(self) -> System.Xml.XmlNode:
        ...

    # methods
    @typing.overload
    @abc.abstractmethod
    def Item(self, index: System.Int32, ) -> System.Xml.XmlNode:
        ...

    @typing.overload
    @abc.abstractmethod
    def GetEnumerator(self, ) -> System.Collections.IEnumerator:
        ...

class XmlAttributeCollection(System.Collections.IEnumerable, System.Collections.ICollection, System.Xml.XmlNamedNodeMap):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def ItemOf(self) -> System.Xml.XmlAttribute:
        ...

    @property
    def ItemOf(self) -> System.Xml.XmlAttribute:
        ...

    @property
    def ItemOf(self) -> System.Xml.XmlAttribute:
        ...

    @property
    def Count(self) -> System.Int32:
        ...

    # methods
    @typing.overload
    def SetNamedItem(self, node: System.Xml.XmlNode, ) -> System.Xml.XmlNode:
        ...

    @typing.overload
    def Prepend(self, node: System.Xml.XmlAttribute, ) -> System.Xml.XmlAttribute:
        ...

    @typing.overload
    def Append(self, node: System.Xml.XmlAttribute, ) -> System.Xml.XmlAttribute:
        ...

    @typing.overload
    def InsertBefore(self, newNode: System.Xml.XmlAttribute, refNode: System.Xml.XmlAttribute, ) -> System.Xml.XmlAttribute:
        ...

    @typing.overload
    def InsertAfter(self, newNode: System.Xml.XmlAttribute, refNode: System.Xml.XmlAttribute, ) -> System.Xml.XmlAttribute:
        ...

    @typing.overload
    def Remove(self, node: System.Xml.XmlAttribute, ) -> System.Xml.XmlAttribute:
        ...

    @typing.overload
    def RemoveAt(self, i: System.Int32, ) -> System.Xml.XmlAttribute:
        ...

    @typing.overload
    def RemoveAll(self, ) -> None:
        ...

    @typing.overload
    def CopyTo(self, array: list[System.Xml.XmlAttribute], index: System.Int32, ) -> None:
        ...

class XmlDocumentType(System.ICloneable, System.Collections.IEnumerable, System.Xml.XPath.IXPathNavigable, System.Xml.XmlLinkedNode):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def Name(self) -> System.String:
        ...

    @property
    def LocalName(self) -> System.String:
        ...

    @property
    def NodeType(self) -> System.Xml.XmlNodeType:
        ...

    @property
    def IsReadOnly(self) -> System.Boolean:
        ...

    @property
    def Entities(self) -> System.Xml.XmlNamedNodeMap:
        ...

    @property
    def Notations(self) -> System.Xml.XmlNamedNodeMap:
        ...

    @property
    def PublicId(self) -> System.String:
        ...

    @property
    def SystemId(self) -> System.String:
        ...

    @property
    def InternalSubset(self) -> System.String:
        ...

    @property
    def PreviousSibling(self) -> System.Xml.XmlNode:
        ...

    @property
    def NextSibling(self) -> System.Xml.XmlNode:
        ...

    @property
    def Value(self) -> System.String:
        ...
    @Value.setter
    def Value(self, val: System.String):
        ...

    @property
    def ParentNode(self) -> System.Xml.XmlNode:
        ...

    @property
    def ChildNodes(self) -> System.Xml.XmlNodeList:
        ...

    @property
    def Attributes(self) -> System.Xml.XmlAttributeCollection:
        ...

    @property
    def OwnerDocument(self) -> System.Xml.XmlDocument:
        ...

    @property
    def FirstChild(self) -> System.Xml.XmlNode:
        ...

    @property
    def LastChild(self) -> System.Xml.XmlNode:
        ...

    @property
    def HasChildNodes(self) -> System.Boolean:
        ...

    @property
    def NamespaceURI(self) -> System.String:
        ...

    @property
    def Prefix(self) -> System.String:
        ...
    @Prefix.setter
    def Prefix(self, val: System.String):
        ...

    @property
    def InnerText(self) -> System.String:
        ...
    @InnerText.setter
    def InnerText(self, val: System.String):
        ...

    @property
    def OuterXml(self) -> System.String:
        ...

    @property
    def InnerXml(self) -> System.String:
        ...
    @InnerXml.setter
    def InnerXml(self, val: System.String):
        ...

    @property
    def SchemaInfo(self) -> System.Xml.Schema.IXmlSchemaInfo:
        ...

    @property
    def BaseURI(self) -> System.String:
        ...

    @property
    def Item(self) -> System.Xml.XmlElement:
        ...

    @property
    def Item(self) -> System.Xml.XmlElement:
        ...

    @property
    def PreviousText(self) -> System.Xml.XmlNode:
        ...

    # methods
    @typing.overload
    def CloneNode(self, deep: System.Boolean, ) -> System.Xml.XmlNode:
        ...

    @typing.overload
    def WriteTo(self, w: System.Xml.XmlWriter, ) -> None:
        ...

    @typing.overload
    def WriteContentTo(self, w: System.Xml.XmlWriter, ) -> None:
        ...

class XmlImplementation(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def __init__(self, nt: System.Xml.XmlNameTable, ):
        ...

    @typing.overload
    def HasFeature(self, strFeature: System.String, strVersion: System.String, ) -> System.Boolean:
        ...

    @typing.overload
    def CreateDocument(self, ) -> System.Xml.XmlDocument:
        ...

class XmlCDataSection(System.ICloneable, System.Collections.IEnumerable, System.Xml.XPath.IXPathNavigable, System.Xml.XmlCharacterData):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def Name(self) -> System.String:
        ...

    @property
    def LocalName(self) -> System.String:
        ...

    @property
    def NodeType(self) -> System.Xml.XmlNodeType:
        ...

    @property
    def ParentNode(self) -> System.Xml.XmlNode:
        ...

    @property
    def PreviousText(self) -> System.Xml.XmlNode:
        ...

    @property
    def Value(self) -> System.String:
        ...
    @Value.setter
    def Value(self, val: System.String):
        ...

    @property
    def InnerText(self) -> System.String:
        ...
    @InnerText.setter
    def InnerText(self, val: System.String):
        ...

    @property
    def Data(self) -> System.String:
        ...
    @Data.setter
    def Data(self, val: System.String):
        ...

    @property
    def Length(self) -> System.Int32:
        ...

    @property
    def PreviousSibling(self) -> System.Xml.XmlNode:
        ...

    @property
    def NextSibling(self) -> System.Xml.XmlNode:
        ...

    @property
    def ChildNodes(self) -> System.Xml.XmlNodeList:
        ...

    @property
    def Attributes(self) -> System.Xml.XmlAttributeCollection:
        ...

    @property
    def OwnerDocument(self) -> System.Xml.XmlDocument:
        ...

    @property
    def FirstChild(self) -> System.Xml.XmlNode:
        ...

    @property
    def LastChild(self) -> System.Xml.XmlNode:
        ...

    @property
    def HasChildNodes(self) -> System.Boolean:
        ...

    @property
    def NamespaceURI(self) -> System.String:
        ...

    @property
    def Prefix(self) -> System.String:
        ...
    @Prefix.setter
    def Prefix(self, val: System.String):
        ...

    @property
    def IsReadOnly(self) -> System.Boolean:
        ...

    @property
    def OuterXml(self) -> System.String:
        ...

    @property
    def InnerXml(self) -> System.String:
        ...
    @InnerXml.setter
    def InnerXml(self, val: System.String):
        ...

    @property
    def SchemaInfo(self) -> System.Xml.Schema.IXmlSchemaInfo:
        ...

    @property
    def BaseURI(self) -> System.String:
        ...

    @property
    def Item(self) -> System.Xml.XmlElement:
        ...

    @property
    def Item(self) -> System.Xml.XmlElement:
        ...

    # methods
    @typing.overload
    def CloneNode(self, deep: System.Boolean, ) -> System.Xml.XmlNode:
        ...

    @typing.overload
    def WriteTo(self, w: System.Xml.XmlWriter, ) -> None:
        ...

    @typing.overload
    def WriteContentTo(self, w: System.Xml.XmlWriter, ) -> None:
        ...

class XmlComment(System.ICloneable, System.Collections.IEnumerable, System.Xml.XPath.IXPathNavigable, System.Xml.XmlCharacterData):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def Name(self) -> System.String:
        ...

    @property
    def LocalName(self) -> System.String:
        ...

    @property
    def NodeType(self) -> System.Xml.XmlNodeType:
        ...

    @property
    def Value(self) -> System.String:
        ...
    @Value.setter
    def Value(self, val: System.String):
        ...

    @property
    def InnerText(self) -> System.String:
        ...
    @InnerText.setter
    def InnerText(self, val: System.String):
        ...

    @property
    def Data(self) -> System.String:
        ...
    @Data.setter
    def Data(self, val: System.String):
        ...

    @property
    def Length(self) -> System.Int32:
        ...

    @property
    def PreviousSibling(self) -> System.Xml.XmlNode:
        ...

    @property
    def NextSibling(self) -> System.Xml.XmlNode:
        ...

    @property
    def ParentNode(self) -> System.Xml.XmlNode:
        ...

    @property
    def ChildNodes(self) -> System.Xml.XmlNodeList:
        ...

    @property
    def Attributes(self) -> System.Xml.XmlAttributeCollection:
        ...

    @property
    def OwnerDocument(self) -> System.Xml.XmlDocument:
        ...

    @property
    def FirstChild(self) -> System.Xml.XmlNode:
        ...

    @property
    def LastChild(self) -> System.Xml.XmlNode:
        ...

    @property
    def HasChildNodes(self) -> System.Boolean:
        ...

    @property
    def NamespaceURI(self) -> System.String:
        ...

    @property
    def Prefix(self) -> System.String:
        ...
    @Prefix.setter
    def Prefix(self, val: System.String):
        ...

    @property
    def IsReadOnly(self) -> System.Boolean:
        ...

    @property
    def OuterXml(self) -> System.String:
        ...

    @property
    def InnerXml(self) -> System.String:
        ...
    @InnerXml.setter
    def InnerXml(self, val: System.String):
        ...

    @property
    def SchemaInfo(self) -> System.Xml.Schema.IXmlSchemaInfo:
        ...

    @property
    def BaseURI(self) -> System.String:
        ...

    @property
    def Item(self) -> System.Xml.XmlElement:
        ...

    @property
    def Item(self) -> System.Xml.XmlElement:
        ...

    @property
    def PreviousText(self) -> System.Xml.XmlNode:
        ...

    # methods
    @typing.overload
    def CloneNode(self, deep: System.Boolean, ) -> System.Xml.XmlNode:
        ...

    @typing.overload
    def WriteTo(self, w: System.Xml.XmlWriter, ) -> None:
        ...

    @typing.overload
    def WriteContentTo(self, w: System.Xml.XmlWriter, ) -> None:
        ...

class XmlDocumentFragment(System.ICloneable, System.Collections.IEnumerable, System.Xml.XPath.IXPathNavigable, System.Xml.XmlNode):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def Name(self) -> System.String:
        ...

    @property
    def LocalName(self) -> System.String:
        ...

    @property
    def NodeType(self) -> System.Xml.XmlNodeType:
        ...

    @property
    def ParentNode(self) -> System.Xml.XmlNode:
        ...

    @property
    def OwnerDocument(self) -> System.Xml.XmlDocument:
        ...

    @property
    def InnerXml(self) -> System.String:
        ...
    @InnerXml.setter
    def InnerXml(self, val: System.String):
        ...

    @property
    def Value(self) -> System.String:
        ...
    @Value.setter
    def Value(self, val: System.String):
        ...

    @property
    def ChildNodes(self) -> System.Xml.XmlNodeList:
        ...

    @property
    def PreviousSibling(self) -> System.Xml.XmlNode:
        ...

    @property
    def NextSibling(self) -> System.Xml.XmlNode:
        ...

    @property
    def Attributes(self) -> System.Xml.XmlAttributeCollection:
        ...

    @property
    def FirstChild(self) -> System.Xml.XmlNode:
        ...

    @property
    def LastChild(self) -> System.Xml.XmlNode:
        ...

    @property
    def HasChildNodes(self) -> System.Boolean:
        ...

    @property
    def NamespaceURI(self) -> System.String:
        ...

    @property
    def Prefix(self) -> System.String:
        ...
    @Prefix.setter
    def Prefix(self, val: System.String):
        ...

    @property
    def IsReadOnly(self) -> System.Boolean:
        ...

    @property
    def InnerText(self) -> System.String:
        ...
    @InnerText.setter
    def InnerText(self, val: System.String):
        ...

    @property
    def OuterXml(self) -> System.String:
        ...

    @property
    def SchemaInfo(self) -> System.Xml.Schema.IXmlSchemaInfo:
        ...

    @property
    def BaseURI(self) -> System.String:
        ...

    @property
    def Item(self) -> System.Xml.XmlElement:
        ...

    @property
    def Item(self) -> System.Xml.XmlElement:
        ...

    @property
    def PreviousText(self) -> System.Xml.XmlNode:
        ...

    # methods
    @typing.overload
    def CloneNode(self, deep: System.Boolean, ) -> System.Xml.XmlNode:
        ...

    @typing.overload
    def WriteTo(self, w: System.Xml.XmlWriter, ) -> None:
        ...

    @typing.overload
    def WriteContentTo(self, w: System.Xml.XmlWriter, ) -> None:
        ...

class XmlEntityReference(System.ICloneable, System.Collections.IEnumerable, System.Xml.XPath.IXPathNavigable, System.Xml.XmlLinkedNode):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def Name(self) -> System.String:
        ...

    @property
    def LocalName(self) -> System.String:
        ...

    @property
    def Value(self) -> System.String:
        ...
    @Value.setter
    def Value(self, val: System.String):
        ...

    @property
    def NodeType(self) -> System.Xml.XmlNodeType:
        ...

    @property
    def IsReadOnly(self) -> System.Boolean:
        ...

    @property
    def BaseURI(self) -> System.String:
        ...

    @property
    def PreviousSibling(self) -> System.Xml.XmlNode:
        ...

    @property
    def NextSibling(self) -> System.Xml.XmlNode:
        ...

    @property
    def ParentNode(self) -> System.Xml.XmlNode:
        ...

    @property
    def ChildNodes(self) -> System.Xml.XmlNodeList:
        ...

    @property
    def Attributes(self) -> System.Xml.XmlAttributeCollection:
        ...

    @property
    def OwnerDocument(self) -> System.Xml.XmlDocument:
        ...

    @property
    def FirstChild(self) -> System.Xml.XmlNode:
        ...

    @property
    def LastChild(self) -> System.Xml.XmlNode:
        ...

    @property
    def HasChildNodes(self) -> System.Boolean:
        ...

    @property
    def NamespaceURI(self) -> System.String:
        ...

    @property
    def Prefix(self) -> System.String:
        ...
    @Prefix.setter
    def Prefix(self, val: System.String):
        ...

    @property
    def InnerText(self) -> System.String:
        ...
    @InnerText.setter
    def InnerText(self, val: System.String):
        ...

    @property
    def OuterXml(self) -> System.String:
        ...

    @property
    def InnerXml(self) -> System.String:
        ...
    @InnerXml.setter
    def InnerXml(self, val: System.String):
        ...

    @property
    def SchemaInfo(self) -> System.Xml.Schema.IXmlSchemaInfo:
        ...

    @property
    def Item(self) -> System.Xml.XmlElement:
        ...

    @property
    def Item(self) -> System.Xml.XmlElement:
        ...

    @property
    def PreviousText(self) -> System.Xml.XmlNode:
        ...

    # methods
    @typing.overload
    def CloneNode(self, deep: System.Boolean, ) -> System.Xml.XmlNode:
        ...

    @typing.overload
    def WriteTo(self, w: System.Xml.XmlWriter, ) -> None:
        ...

    @typing.overload
    def WriteContentTo(self, w: System.Xml.XmlWriter, ) -> None:
        ...

class XmlProcessingInstruction(System.ICloneable, System.Collections.IEnumerable, System.Xml.XPath.IXPathNavigable, System.Xml.XmlLinkedNode):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def Name(self) -> System.String:
        ...

    @property
    def LocalName(self) -> System.String:
        ...

    @property
    def Value(self) -> System.String:
        ...
    @Value.setter
    def Value(self, val: System.String):
        ...

    @property
    def Target(self) -> System.String:
        ...

    @property
    def Data(self) -> System.String:
        ...
    @Data.setter
    def Data(self, val: System.String):
        ...

    @property
    def InnerText(self) -> System.String:
        ...
    @InnerText.setter
    def InnerText(self, val: System.String):
        ...

    @property
    def NodeType(self) -> System.Xml.XmlNodeType:
        ...

    @property
    def PreviousSibling(self) -> System.Xml.XmlNode:
        ...

    @property
    def NextSibling(self) -> System.Xml.XmlNode:
        ...

    @property
    def ParentNode(self) -> System.Xml.XmlNode:
        ...

    @property
    def ChildNodes(self) -> System.Xml.XmlNodeList:
        ...

    @property
    def Attributes(self) -> System.Xml.XmlAttributeCollection:
        ...

    @property
    def OwnerDocument(self) -> System.Xml.XmlDocument:
        ...

    @property
    def FirstChild(self) -> System.Xml.XmlNode:
        ...

    @property
    def LastChild(self) -> System.Xml.XmlNode:
        ...

    @property
    def HasChildNodes(self) -> System.Boolean:
        ...

    @property
    def NamespaceURI(self) -> System.String:
        ...

    @property
    def Prefix(self) -> System.String:
        ...
    @Prefix.setter
    def Prefix(self, val: System.String):
        ...

    @property
    def IsReadOnly(self) -> System.Boolean:
        ...

    @property
    def OuterXml(self) -> System.String:
        ...

    @property
    def InnerXml(self) -> System.String:
        ...
    @InnerXml.setter
    def InnerXml(self, val: System.String):
        ...

    @property
    def SchemaInfo(self) -> System.Xml.Schema.IXmlSchemaInfo:
        ...

    @property
    def BaseURI(self) -> System.String:
        ...

    @property
    def Item(self) -> System.Xml.XmlElement:
        ...

    @property
    def Item(self) -> System.Xml.XmlElement:
        ...

    @property
    def PreviousText(self) -> System.Xml.XmlNode:
        ...

    # methods
    @typing.overload
    def CloneNode(self, deep: System.Boolean, ) -> System.Xml.XmlNode:
        ...

    @typing.overload
    def WriteTo(self, w: System.Xml.XmlWriter, ) -> None:
        ...

    @typing.overload
    def WriteContentTo(self, w: System.Xml.XmlWriter, ) -> None:
        ...

class XmlDeclaration(System.ICloneable, System.Collections.IEnumerable, System.Xml.XPath.IXPathNavigable, System.Xml.XmlLinkedNode):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def Version(self) -> System.String:
        ...

    @property
    def Encoding(self) -> System.String:
        ...
    @Encoding.setter
    def Encoding(self, val: System.String):
        ...

    @property
    def Standalone(self) -> System.String:
        ...
    @Standalone.setter
    def Standalone(self, val: System.String):
        ...

    @property
    def Value(self) -> System.String:
        ...
    @Value.setter
    def Value(self, val: System.String):
        ...

    @property
    def InnerText(self) -> System.String:
        ...
    @InnerText.setter
    def InnerText(self, val: System.String):
        ...

    @property
    def Name(self) -> System.String:
        ...

    @property
    def LocalName(self) -> System.String:
        ...

    @property
    def NodeType(self) -> System.Xml.XmlNodeType:
        ...

    @property
    def PreviousSibling(self) -> System.Xml.XmlNode:
        ...

    @property
    def NextSibling(self) -> System.Xml.XmlNode:
        ...

    @property
    def ParentNode(self) -> System.Xml.XmlNode:
        ...

    @property
    def ChildNodes(self) -> System.Xml.XmlNodeList:
        ...

    @property
    def Attributes(self) -> System.Xml.XmlAttributeCollection:
        ...

    @property
    def OwnerDocument(self) -> System.Xml.XmlDocument:
        ...

    @property
    def FirstChild(self) -> System.Xml.XmlNode:
        ...

    @property
    def LastChild(self) -> System.Xml.XmlNode:
        ...

    @property
    def HasChildNodes(self) -> System.Boolean:
        ...

    @property
    def NamespaceURI(self) -> System.String:
        ...

    @property
    def Prefix(self) -> System.String:
        ...
    @Prefix.setter
    def Prefix(self, val: System.String):
        ...

    @property
    def IsReadOnly(self) -> System.Boolean:
        ...

    @property
    def OuterXml(self) -> System.String:
        ...

    @property
    def InnerXml(self) -> System.String:
        ...
    @InnerXml.setter
    def InnerXml(self, val: System.String):
        ...

    @property
    def SchemaInfo(self) -> System.Xml.Schema.IXmlSchemaInfo:
        ...

    @property
    def BaseURI(self) -> System.String:
        ...

    @property
    def Item(self) -> System.Xml.XmlElement:
        ...

    @property
    def Item(self) -> System.Xml.XmlElement:
        ...

    @property
    def PreviousText(self) -> System.Xml.XmlNode:
        ...

    # methods
    @typing.overload
    def CloneNode(self, deep: System.Boolean, ) -> System.Xml.XmlNode:
        ...

    @typing.overload
    def WriteTo(self, w: System.Xml.XmlWriter, ) -> None:
        ...

    @typing.overload
    def WriteContentTo(self, w: System.Xml.XmlWriter, ) -> None:
        ...

class XmlText(System.ICloneable, System.Collections.IEnumerable, System.Xml.XPath.IXPathNavigable, System.Xml.XmlCharacterData):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def Name(self) -> System.String:
        ...

    @property
    def LocalName(self) -> System.String:
        ...

    @property
    def NodeType(self) -> System.Xml.XmlNodeType:
        ...

    @property
    def ParentNode(self) -> System.Xml.XmlNode:
        ...

    @property
    def Value(self) -> System.String:
        ...
    @Value.setter
    def Value(self, val: System.String):
        ...

    @property
    def PreviousText(self) -> System.Xml.XmlNode:
        ...

    @property
    def InnerText(self) -> System.String:
        ...
    @InnerText.setter
    def InnerText(self, val: System.String):
        ...

    @property
    def Data(self) -> System.String:
        ...
    @Data.setter
    def Data(self, val: System.String):
        ...

    @property
    def Length(self) -> System.Int32:
        ...

    @property
    def PreviousSibling(self) -> System.Xml.XmlNode:
        ...

    @property
    def NextSibling(self) -> System.Xml.XmlNode:
        ...

    @property
    def ChildNodes(self) -> System.Xml.XmlNodeList:
        ...

    @property
    def Attributes(self) -> System.Xml.XmlAttributeCollection:
        ...

    @property
    def OwnerDocument(self) -> System.Xml.XmlDocument:
        ...

    @property
    def FirstChild(self) -> System.Xml.XmlNode:
        ...

    @property
    def LastChild(self) -> System.Xml.XmlNode:
        ...

    @property
    def HasChildNodes(self) -> System.Boolean:
        ...

    @property
    def NamespaceURI(self) -> System.String:
        ...

    @property
    def Prefix(self) -> System.String:
        ...
    @Prefix.setter
    def Prefix(self, val: System.String):
        ...

    @property
    def IsReadOnly(self) -> System.Boolean:
        ...

    @property
    def OuterXml(self) -> System.String:
        ...

    @property
    def InnerXml(self) -> System.String:
        ...
    @InnerXml.setter
    def InnerXml(self, val: System.String):
        ...

    @property
    def SchemaInfo(self) -> System.Xml.Schema.IXmlSchemaInfo:
        ...

    @property
    def BaseURI(self) -> System.String:
        ...

    @property
    def Item(self) -> System.Xml.XmlElement:
        ...

    @property
    def Item(self) -> System.Xml.XmlElement:
        ...

    # methods
    @typing.overload
    def CloneNode(self, deep: System.Boolean, ) -> System.Xml.XmlNode:
        ...

    @typing.overload
    def SplitText(self, offset: System.Int32, ) -> System.Xml.XmlText:
        ...

    @typing.overload
    def WriteTo(self, w: System.Xml.XmlWriter, ) -> None:
        ...

    @typing.overload
    def WriteContentTo(self, w: System.Xml.XmlWriter, ) -> None:
        ...

class XmlSignificantWhitespace(System.ICloneable, System.Collections.IEnumerable, System.Xml.XPath.IXPathNavigable, System.Xml.XmlCharacterData):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def Name(self) -> System.String:
        ...

    @property
    def LocalName(self) -> System.String:
        ...

    @property
    def NodeType(self) -> System.Xml.XmlNodeType:
        ...

    @property
    def ParentNode(self) -> System.Xml.XmlNode:
        ...

    @property
    def Value(self) -> System.String:
        ...
    @Value.setter
    def Value(self, val: System.String):
        ...

    @property
    def PreviousText(self) -> System.Xml.XmlNode:
        ...

    @property
    def InnerText(self) -> System.String:
        ...
    @InnerText.setter
    def InnerText(self, val: System.String):
        ...

    @property
    def Data(self) -> System.String:
        ...
    @Data.setter
    def Data(self, val: System.String):
        ...

    @property
    def Length(self) -> System.Int32:
        ...

    @property
    def PreviousSibling(self) -> System.Xml.XmlNode:
        ...

    @property
    def NextSibling(self) -> System.Xml.XmlNode:
        ...

    @property
    def ChildNodes(self) -> System.Xml.XmlNodeList:
        ...

    @property
    def Attributes(self) -> System.Xml.XmlAttributeCollection:
        ...

    @property
    def OwnerDocument(self) -> System.Xml.XmlDocument:
        ...

    @property
    def FirstChild(self) -> System.Xml.XmlNode:
        ...

    @property
    def LastChild(self) -> System.Xml.XmlNode:
        ...

    @property
    def HasChildNodes(self) -> System.Boolean:
        ...

    @property
    def NamespaceURI(self) -> System.String:
        ...

    @property
    def Prefix(self) -> System.String:
        ...
    @Prefix.setter
    def Prefix(self, val: System.String):
        ...

    @property
    def IsReadOnly(self) -> System.Boolean:
        ...

    @property
    def OuterXml(self) -> System.String:
        ...

    @property
    def InnerXml(self) -> System.String:
        ...
    @InnerXml.setter
    def InnerXml(self, val: System.String):
        ...

    @property
    def SchemaInfo(self) -> System.Xml.Schema.IXmlSchemaInfo:
        ...

    @property
    def BaseURI(self) -> System.String:
        ...

    @property
    def Item(self) -> System.Xml.XmlElement:
        ...

    @property
    def Item(self) -> System.Xml.XmlElement:
        ...

    # methods
    @typing.overload
    def CloneNode(self, deep: System.Boolean, ) -> System.Xml.XmlNode:
        ...

    @typing.overload
    def WriteTo(self, w: System.Xml.XmlWriter, ) -> None:
        ...

    @typing.overload
    def WriteContentTo(self, w: System.Xml.XmlWriter, ) -> None:
        ...

class XmlWhitespace(System.ICloneable, System.Collections.IEnumerable, System.Xml.XPath.IXPathNavigable, System.Xml.XmlCharacterData):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def Name(self) -> System.String:
        ...

    @property
    def LocalName(self) -> System.String:
        ...

    @property
    def NodeType(self) -> System.Xml.XmlNodeType:
        ...

    @property
    def ParentNode(self) -> System.Xml.XmlNode:
        ...

    @property
    def Value(self) -> System.String:
        ...
    @Value.setter
    def Value(self, val: System.String):
        ...

    @property
    def PreviousText(self) -> System.Xml.XmlNode:
        ...

    @property
    def InnerText(self) -> System.String:
        ...
    @InnerText.setter
    def InnerText(self, val: System.String):
        ...

    @property
    def Data(self) -> System.String:
        ...
    @Data.setter
    def Data(self, val: System.String):
        ...

    @property
    def Length(self) -> System.Int32:
        ...

    @property
    def PreviousSibling(self) -> System.Xml.XmlNode:
        ...

    @property
    def NextSibling(self) -> System.Xml.XmlNode:
        ...

    @property
    def ChildNodes(self) -> System.Xml.XmlNodeList:
        ...

    @property
    def Attributes(self) -> System.Xml.XmlAttributeCollection:
        ...

    @property
    def OwnerDocument(self) -> System.Xml.XmlDocument:
        ...

    @property
    def FirstChild(self) -> System.Xml.XmlNode:
        ...

    @property
    def LastChild(self) -> System.Xml.XmlNode:
        ...

    @property
    def HasChildNodes(self) -> System.Boolean:
        ...

    @property
    def NamespaceURI(self) -> System.String:
        ...

    @property
    def Prefix(self) -> System.String:
        ...
    @Prefix.setter
    def Prefix(self, val: System.String):
        ...

    @property
    def IsReadOnly(self) -> System.Boolean:
        ...

    @property
    def OuterXml(self) -> System.String:
        ...

    @property
    def InnerXml(self) -> System.String:
        ...
    @InnerXml.setter
    def InnerXml(self, val: System.String):
        ...

    @property
    def SchemaInfo(self) -> System.Xml.Schema.IXmlSchemaInfo:
        ...

    @property
    def BaseURI(self) -> System.String:
        ...

    @property
    def Item(self) -> System.Xml.XmlElement:
        ...

    @property
    def Item(self) -> System.Xml.XmlElement:
        ...

    # methods
    @typing.overload
    def CloneNode(self, deep: System.Boolean, ) -> System.Xml.XmlNode:
        ...

    @typing.overload
    def WriteTo(self, w: System.Xml.XmlWriter, ) -> None:
        ...

    @typing.overload
    def WriteContentTo(self, w: System.Xml.XmlWriter, ) -> None:
        ...

class XmlLinkedNode(System.ICloneable, System.Collections.IEnumerable, System.Xml.XPath.IXPathNavigable, System.Xml.XmlNode, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def PreviousSibling(self) -> System.Xml.XmlNode:
        ...

    @property
    def NextSibling(self) -> System.Xml.XmlNode:
        ...

    @abc.abstractmethod
    @property
    def Name(self) -> System.String:
        ...

    @property
    def Value(self) -> System.String:
        ...
    @Value.setter
    def Value(self, val: System.String):
        ...

    @abc.abstractmethod
    @property
    def NodeType(self) -> System.Xml.XmlNodeType:
        ...

    @property
    def ParentNode(self) -> System.Xml.XmlNode:
        ...

    @property
    def ChildNodes(self) -> System.Xml.XmlNodeList:
        ...

    @property
    def Attributes(self) -> System.Xml.XmlAttributeCollection:
        ...

    @property
    def OwnerDocument(self) -> System.Xml.XmlDocument:
        ...

    @property
    def FirstChild(self) -> System.Xml.XmlNode:
        ...

    @property
    def LastChild(self) -> System.Xml.XmlNode:
        ...

    @property
    def HasChildNodes(self) -> System.Boolean:
        ...

    @property
    def NamespaceURI(self) -> System.String:
        ...

    @property
    def Prefix(self) -> System.String:
        ...
    @Prefix.setter
    def Prefix(self, val: System.String):
        ...

    @abc.abstractmethod
    @property
    def LocalName(self) -> System.String:
        ...

    @property
    def IsReadOnly(self) -> System.Boolean:
        ...

    @property
    def InnerText(self) -> System.String:
        ...
    @InnerText.setter
    def InnerText(self, val: System.String):
        ...

    @property
    def OuterXml(self) -> System.String:
        ...

    @property
    def InnerXml(self) -> System.String:
        ...
    @InnerXml.setter
    def InnerXml(self, val: System.String):
        ...

    @property
    def SchemaInfo(self) -> System.Xml.Schema.IXmlSchemaInfo:
        ...

    @property
    def BaseURI(self) -> System.String:
        ...

    @property
    def Item(self) -> System.Xml.XmlElement:
        ...

    @property
    def Item(self) -> System.Xml.XmlElement:
        ...

    @property
    def PreviousText(self) -> System.Xml.XmlNode:
        ...

    # methods
class XmlNamedNodeMap(System.Collections.IEnumerable, System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def Count(self) -> System.Int32:
        ...

    # methods
    @typing.overload
    def SetNamedItem(self, node: System.Xml.XmlNode, ) -> System.Xml.XmlNode:
        ...

    @typing.overload
    def GetNamedItem(self, name: System.String, ) -> System.Xml.XmlNode:
        ...

    @typing.overload
    def RemoveNamedItem(self, name: System.String, ) -> System.Xml.XmlNode:
        ...

    @typing.overload
    def Item(self, index: System.Int32, ) -> System.Xml.XmlNode:
        ...

    @typing.overload
    def GetNamedItem(self, localName: System.String, namespaceURI: System.String, ) -> System.Xml.XmlNode:
        ...

    @typing.overload
    def RemoveNamedItem(self, localName: System.String, namespaceURI: System.String, ) -> System.Xml.XmlNode:
        ...

    @typing.overload
    def GetEnumerator(self, ) -> System.Collections.IEnumerator:
        ...

class XmlCharacterData(System.ICloneable, System.Collections.IEnumerable, System.Xml.XPath.IXPathNavigable, System.Xml.XmlLinkedNode, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def Value(self) -> System.String:
        ...
    @Value.setter
    def Value(self, val: System.String):
        ...

    @property
    def InnerText(self) -> System.String:
        ...
    @InnerText.setter
    def InnerText(self, val: System.String):
        ...

    @property
    def Data(self) -> System.String:
        ...
    @Data.setter
    def Data(self, val: System.String):
        ...

    @property
    def Length(self) -> System.Int32:
        ...

    @property
    def PreviousSibling(self) -> System.Xml.XmlNode:
        ...

    @property
    def NextSibling(self) -> System.Xml.XmlNode:
        ...

    @abc.abstractmethod
    @property
    def Name(self) -> System.String:
        ...

    @abc.abstractmethod
    @property
    def NodeType(self) -> System.Xml.XmlNodeType:
        ...

    @property
    def ParentNode(self) -> System.Xml.XmlNode:
        ...

    @property
    def ChildNodes(self) -> System.Xml.XmlNodeList:
        ...

    @property
    def Attributes(self) -> System.Xml.XmlAttributeCollection:
        ...

    @property
    def OwnerDocument(self) -> System.Xml.XmlDocument:
        ...

    @property
    def FirstChild(self) -> System.Xml.XmlNode:
        ...

    @property
    def LastChild(self) -> System.Xml.XmlNode:
        ...

    @property
    def HasChildNodes(self) -> System.Boolean:
        ...

    @property
    def NamespaceURI(self) -> System.String:
        ...

    @property
    def Prefix(self) -> System.String:
        ...
    @Prefix.setter
    def Prefix(self, val: System.String):
        ...

    @abc.abstractmethod
    @property
    def LocalName(self) -> System.String:
        ...

    @property
    def IsReadOnly(self) -> System.Boolean:
        ...

    @property
    def OuterXml(self) -> System.String:
        ...

    @property
    def InnerXml(self) -> System.String:
        ...
    @InnerXml.setter
    def InnerXml(self, val: System.String):
        ...

    @property
    def SchemaInfo(self) -> System.Xml.Schema.IXmlSchemaInfo:
        ...

    @property
    def BaseURI(self) -> System.String:
        ...

    @property
    def Item(self) -> System.Xml.XmlElement:
        ...

    @property
    def Item(self) -> System.Xml.XmlElement:
        ...

    @property
    def PreviousText(self) -> System.Xml.XmlNode:
        ...

    # methods
    @typing.overload
    def Substring(self, offset: System.Int32, count: System.Int32, ) -> System.String:
        ...

    @typing.overload
    def AppendData(self, strData: System.String, ) -> None:
        ...

    @typing.overload
    def InsertData(self, offset: System.Int32, strData: System.String, ) -> None:
        ...

    @typing.overload
    def DeleteData(self, offset: System.Int32, count: System.Int32, ) -> None:
        ...

    @typing.overload
    def ReplaceData(self, offset: System.Int32, count: System.Int32, strData: System.String, ) -> None:
        ...

