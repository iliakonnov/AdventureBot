from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import System
import System.Net
import System.Threading.Tasks
import System.Xml
import System.Xml.Schema
import System.IO
import System.Collections.Generic
import System.Collections
import System.Xml.XPath
import System.Xml.XmlNamedNodeMap
import System.Text
import System.Xml.Xsl.Runtime


class XmlResolver(System.Object, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    Credentials: System.Net.ICredentials = property(None, lambda val: ...)

    # methods
    def __init__(self, ):
        ...

    @abc.abstractmethod
    def GetEntity(self, absoluteUri: System.Uri, role: str, ofObjectToReturn: System.Type, ) -> System.Object:
        ...

    def ResolveUri(self, baseUri: System.Uri, relativeUri: str, ) -> System.Uri:
        ...

    def SupportsType(self, absoluteUri: System.Uri, type: System.Type, ) -> bool:
        ...

    def GetEntityAsync(self, absoluteUri: System.Uri, role: str, ofObjectToReturn: System.Type, ) -> System.Threading.Tasks.Task[System.Object]:
        ...

class XmlQualifiedName(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields
    Empty: System.Xml.XmlQualifiedName = ...

    # properties
    @property
    def Namespace(self) -> str:
        ...

    @property
    def Name(self) -> str:
        ...

    @property
    def IsEmpty(self) -> bool:
        ...

    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def __init__(self, name: str, ):
        ...

    @typing.overload
    def __init__(self, name: str, ns: str, ):
        ...

    def GetHashCode(self, ) -> int:
        ...

    @typing.overload
    def ToString(self, ) -> str:
        ...

    @staticmethod
    @typing.overload
    def ToString(name: str, ns: str, ) -> str:
        ...

    def Equals(self, other: System.Object, ) -> bool:
        ...

    def Init(self, name: str, ns: str, ) -> None:
        ...

    def SetNamespace(self, ns: str, ) -> None:
        ...

    def Verify(self, ) -> None:
        ...

    def Atomize(self, nameTable: System.Xml.XmlNameTable, ) -> None:
        ...

    @staticmethod
    def Parse(s: str, nsmgr: System.Xml.IXmlNamespaceResolver, prefix: ref[str], ) -> System.Xml.XmlQualifiedName:
        ...

    def Clone(self, ) -> System.Xml.XmlQualifiedName:
        ...

class XmlReaderSettings(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields
    s_defaultReaderSettings: System.Xml.XmlReaderSettings = ...

    # properties
    @property
    def Async(self) -> bool:
        ...
    @Async.setter
    def Async(self, val: bool):
        ...

    @property
    def NameTable(self) -> System.Xml.XmlNameTable:
        ...
    @NameTable.setter
    def NameTable(self, val: System.Xml.XmlNameTable):
        ...

    @property
    def IsXmlResolverSet(self) -> bool:
        ...
    @IsXmlResolverSet.setter
    def IsXmlResolverSet(self, val: bool):
        ...

    XmlResolver: System.Xml.XmlResolver = property(None, lambda val: ...)

    @property
    def LineNumberOffset(self) -> int:
        ...
    @LineNumberOffset.setter
    def LineNumberOffset(self, val: int):
        ...

    @property
    def LinePositionOffset(self) -> int:
        ...
    @LinePositionOffset.setter
    def LinePositionOffset(self, val: int):
        ...

    @property
    def ConformanceLevel(self) -> int:
        ...
    @ConformanceLevel.setter
    def ConformanceLevel(self, val: int):
        ...

    @property
    def CheckCharacters(self) -> bool:
        ...
    @CheckCharacters.setter
    def CheckCharacters(self, val: bool):
        ...

    @property
    def MaxCharactersInDocument(self) -> int:
        ...
    @MaxCharactersInDocument.setter
    def MaxCharactersInDocument(self, val: int):
        ...

    @property
    def MaxCharactersFromEntities(self) -> int:
        ...
    @MaxCharactersFromEntities.setter
    def MaxCharactersFromEntities(self, val: int):
        ...

    @property
    def IgnoreWhitespace(self) -> bool:
        ...
    @IgnoreWhitespace.setter
    def IgnoreWhitespace(self, val: bool):
        ...

    @property
    def IgnoreProcessingInstructions(self) -> bool:
        ...
    @IgnoreProcessingInstructions.setter
    def IgnoreProcessingInstructions(self, val: bool):
        ...

    @property
    def IgnoreComments(self) -> bool:
        ...
    @IgnoreComments.setter
    def IgnoreComments(self, val: bool):
        ...

    @property
    def ProhibitDtd(self) -> bool:
        ...
    @ProhibitDtd.setter
    def ProhibitDtd(self, val: bool):
        ...

    @property
    def DtdProcessing(self) -> int:
        ...
    @DtdProcessing.setter
    def DtdProcessing(self, val: int):
        ...

    @property
    def CloseInput(self) -> bool:
        ...
    @CloseInput.setter
    def CloseInput(self, val: bool):
        ...

    @property
    def ValidationType(self) -> int:
        ...
    @ValidationType.setter
    def ValidationType(self, val: int):
        ...

    @property
    def ValidationFlags(self) -> int:
        ...
    @ValidationFlags.setter
    def ValidationFlags(self, val: int):
        ...

    @property
    def Schemas(self) -> System.Xml.Schema.XmlSchemaSet:
        ...
    @Schemas.setter
    def Schemas(self, val: System.Xml.Schema.XmlSchemaSet):
        ...

    ReadOnly: bool = property(None, lambda val: ...)

    # methods
    def __init__(self, ):
        ...

    def GetXmlResolver(self, ) -> System.Xml.XmlResolver:
        ...

    def GetXmlResolver_CheckConfig(self, ) -> System.Xml.XmlResolver:
        ...

    def Reset(self, ) -> None:
        ...

    def Clone(self, ) -> System.Xml.XmlReaderSettings:
        ...

    def GetEventHandler(self, ) -> System.Xml.Schema.ValidationEventHandler:
        ...

    @typing.overload
    def CreateReader(self, inputUri: str, inputContext: System.Xml.XmlParserContext, ) -> System.Xml.XmlReader:
        ...

    @typing.overload
    def CreateReader(self, input: System.IO.Stream, baseUri: System.Uri, baseUriString: str, inputContext: System.Xml.XmlParserContext, ) -> System.Xml.XmlReader:
        ...

    @typing.overload
    def CreateReader(self, input: System.IO.TextReader, baseUriString: str, inputContext: System.Xml.XmlParserContext, ) -> System.Xml.XmlReader:
        ...

    @typing.overload
    def CreateReader(self, reader: System.Xml.XmlReader, ) -> System.Xml.XmlReader:
        ...

    def CheckReadOnly(self, propertyName: str, ) -> None:
        ...

    @typing.overload
    def Initialize(self, ) -> None:
        ...

    @typing.overload
    def Initialize(self, resolver: System.Xml.XmlResolver, ) -> None:
        ...

    def AddValidation(self, reader: System.Xml.XmlReader, ) -> System.Xml.XmlReader:
        ...

    def AddValidationAndConformanceWrapper(self, reader: System.Xml.XmlReader, ) -> System.Xml.XmlReader:
        ...

    def AddValidationAndConformanceInternal(self, reader: System.Xml.XmlReader, resolver: System.Xml.XmlResolver, addConformanceWrapper: bool, ) -> System.Xml.XmlReader:
        ...

    def AddValidationInternal(self, reader: System.Xml.XmlReader, resolver: System.Xml.XmlResolver, addConformanceWrapper: bool, ) -> System.Xml.XmlReader:
        ...

    def CreateDtdValidatingReader(self, baseReader: System.Xml.XmlReader, ) -> System.Xml.XmlValidatingReaderImpl:
        ...

    def AddConformanceWrapper(self, baseReader: System.Xml.XmlReader, ) -> System.Xml.XmlReader:
        ...

class DtdProcessing(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    Prohibit: int = ...
    Ignore: int = ...
    Parse: int = ...

class IXmlNamespaceResolver(abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    @abc.abstractmethod
    def GetNamespacesInScope(self, scope: int, ) -> System.Collections.Generic.IDictionary[str, str]:
        ...

    @abc.abstractmethod
    def LookupNamespace(self, prefix: str, ) -> str:
        ...

    @abc.abstractmethod
    def LookupPrefix(self, namespaceName: str, ) -> str:
        ...

class XmlNamespaceScope(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    All: int = ...
    ExcludeXml: int = ...
    Local: int = ...

class XmlAttribute(System.ICloneable, System.Collections.IEnumerable, System.Xml.XPath.IXPathNavigable, System.Xml.XmlNode):
    @typing.overload
    def __init__(self, **kwargs):
        self.parentNode: System.Xml.XmlNode
        ...

    # static fields

    # properties
    @property
    def LocalNameHash(self) -> int:
        ...

    @property
    def XmlName(self) -> System.Xml.XmlName:
        ...
    @XmlName.setter
    def XmlName(self, val: System.Xml.XmlName):
        ...

    @property
    def ParentNode(self) -> System.Xml.XmlNode:
        ...

    @property
    def Name(self) -> str:
        ...

    @property
    def LocalName(self) -> str:
        ...

    @property
    def NamespaceURI(self) -> str:
        ...

    @property
    def Prefix(self) -> str:
        ...
    @Prefix.setter
    def Prefix(self, val: str):
        ...

    @property
    def NodeType(self) -> int:
        ...

    @property
    def OwnerDocument(self) -> System.Xml.XmlDocument:
        ...

    @property
    def Value(self) -> str:
        ...
    @Value.setter
    def Value(self, val: str):
        ...

    @property
    def SchemaInfo(self) -> System.Xml.Schema.IXmlSchemaInfo:
        ...

    InnerText: str = property(None, lambda val: ...)

    @property
    def IsContainer(self) -> bool:
        ...

    @property
    def LastNode(self) -> System.Xml.XmlLinkedNode:
        ...
    @LastNode.setter
    def LastNode(self, val: System.Xml.XmlLinkedNode):
        ...

    @property
    def Specified(self) -> bool:
        ...

    @property
    def OwnerElement(self) -> System.Xml.XmlElement:
        ...

    InnerXml: str = property(None, lambda val: ...)

    @property
    def BaseURI(self) -> str:
        ...

    @property
    def XmlSpace(self) -> int:
        ...

    @property
    def XmlLang(self) -> str:
        ...

    @property
    def XPNodeType(self) -> int:
        ...

    @property
    def XPLocalName(self) -> str:
        ...

    @property
    def IsNamespace(self) -> bool:
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
    def HasChildNodes(self) -> bool:
        ...

    @property
    def IsReadOnly(self) -> bool:
        ...

    @property
    def OuterXml(self) -> str:
        ...

    @property
    def Document(self) -> System.Xml.XmlDocument:
        ...

    @property
    def Item(self) -> System.Xml.XmlElement:
        ...

    @property
    def Item(self) -> System.Xml.XmlElement:
        ...

    @property
    def IsText(self) -> bool:
        ...

    @property
    def PreviousText(self) -> System.Xml.XmlNode:
        ...

    # methods
    @typing.overload
    def __init__(self, name: System.Xml.XmlName, doc: System.Xml.XmlDocument, ):
        ...

    @typing.overload
    def __init__(self, prefix: str, localName: str, namespaceURI: str, doc: System.Xml.XmlDocument, ):
        ...

    def CloneNode(self, deep: bool, ) -> System.Xml.XmlNode:
        ...

    def PrepareOwnerElementInElementIdAttrMap(self, ) -> bool:
        ...

    def ResetOwnerElementInElementIdAttrMap(self, oldInnerText: str, ) -> None:
        ...

    def AppendChildForLoad(self, newChild: System.Xml.XmlNode, doc: System.Xml.XmlDocument, ) -> System.Xml.XmlNode:
        ...

    def IsValidChildType(self, type: int, ) -> bool:
        ...

    def InsertBefore(self, newChild: System.Xml.XmlNode, refChild: System.Xml.XmlNode, ) -> System.Xml.XmlNode:
        ...

    def InsertAfter(self, newChild: System.Xml.XmlNode, refChild: System.Xml.XmlNode, ) -> System.Xml.XmlNode:
        ...

    def ReplaceChild(self, newChild: System.Xml.XmlNode, oldChild: System.Xml.XmlNode, ) -> System.Xml.XmlNode:
        ...

    def RemoveChild(self, oldChild: System.Xml.XmlNode, ) -> System.Xml.XmlNode:
        ...

    def PrependChild(self, newChild: System.Xml.XmlNode, ) -> System.Xml.XmlNode:
        ...

    def AppendChild(self, newChild: System.Xml.XmlNode, ) -> System.Xml.XmlNode:
        ...

    def WriteTo(self, w: System.Xml.XmlWriter, ) -> None:
        ...

    def WriteContentTo(self, w: System.Xml.XmlWriter, ) -> None:
        ...

    def SetParent(self, node: System.Xml.XmlNode, ) -> None:
        ...

class XmlLinkedNode(System.ICloneable, System.Collections.IEnumerable, System.Xml.XPath.IXPathNavigable, System.Xml.XmlNode, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        self.next: System.Xml.XmlLinkedNode
        self.parentNode: System.Xml.XmlNode
        ...

    # static fields

    # properties
    @property
    def PreviousSibling(self) -> System.Xml.XmlNode:
        ...

    @property
    def NextSibling(self) -> System.Xml.XmlNode:
        ...

    @property
    @abc.abstractmethod
    def Name(self) -> str:
        ...

    @property
    def Value(self) -> str:
        ...
    @Value.setter
    def Value(self, val: str):
        ...

    @property
    @abc.abstractmethod
    def NodeType(self) -> int:
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
    def IsContainer(self) -> bool:
        ...

    @property
    def LastNode(self) -> System.Xml.XmlLinkedNode:
        ...
    @LastNode.setter
    def LastNode(self, val: System.Xml.XmlLinkedNode):
        ...

    @property
    def HasChildNodes(self) -> bool:
        ...

    @property
    def NamespaceURI(self) -> str:
        ...

    @property
    def Prefix(self) -> str:
        ...
    @Prefix.setter
    def Prefix(self, val: str):
        ...

    @property
    @abc.abstractmethod
    def LocalName(self) -> str:
        ...

    @property
    def IsReadOnly(self) -> bool:
        ...

    @property
    def InnerText(self) -> str:
        ...
    @InnerText.setter
    def InnerText(self, val: str):
        ...

    @property
    def OuterXml(self) -> str:
        ...

    @property
    def InnerXml(self) -> str:
        ...
    @InnerXml.setter
    def InnerXml(self, val: str):
        ...

    @property
    def SchemaInfo(self) -> System.Xml.Schema.IXmlSchemaInfo:
        ...

    @property
    def BaseURI(self) -> str:
        ...

    @property
    def Document(self) -> System.Xml.XmlDocument:
        ...

    @property
    def Item(self) -> System.Xml.XmlElement:
        ...

    @property
    def Item(self) -> System.Xml.XmlElement:
        ...

    @property
    def XmlSpace(self) -> int:
        ...

    @property
    def XmlLang(self) -> str:
        ...

    @property
    def XPNodeType(self) -> int:
        ...

    @property
    def XPLocalName(self) -> str:
        ...

    @property
    def IsText(self) -> bool:
        ...

    @property
    def PreviousText(self) -> System.Xml.XmlNode:
        ...

    # methods
    def __init__(self, doc: System.Xml.XmlDocument, ):
        ...

class XmlAttributeCollection(System.Collections.IEnumerable, System.Collections.ICollection, System.Xml.XmlNamedNodeMap):
    @typing.overload
    def __init__(self, **kwargs):
        self.parent: System.Xml.XmlNode
        self.nodes: System.Xml.XmlNamedNodeMap.SmallXmlNodeList
        ...

    # static fields

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
    def IsSynchronized(self) -> bool:
        ...

    @property
    def SyncRoot(self) -> System.Object:
        ...

    @property
    def Count(self) -> int:
        ...

    @property
    def Count(self) -> int:
        ...

    # methods
    def __init__(self, parent: System.Xml.XmlNode, ):
        ...

    def FindNodeOffsetNS(self, node: System.Xml.XmlAttribute, ) -> int:
        ...

    def SetNamedItem(self, node: System.Xml.XmlNode, ) -> System.Xml.XmlNode:
        ...

    def Prepend(self, node: System.Xml.XmlAttribute, ) -> System.Xml.XmlAttribute:
        ...

    def Append(self, node: System.Xml.XmlAttribute, ) -> System.Xml.XmlAttribute:
        ...

    def InsertBefore(self, newNode: System.Xml.XmlAttribute, refNode: System.Xml.XmlAttribute, ) -> System.Xml.XmlAttribute:
        ...

    def InsertAfter(self, newNode: System.Xml.XmlAttribute, refNode: System.Xml.XmlAttribute, ) -> System.Xml.XmlAttribute:
        ...

    def Remove(self, node: System.Xml.XmlAttribute, ) -> System.Xml.XmlAttribute:
        ...

    def RemoveAt(self, i: int, ) -> System.Xml.XmlAttribute:
        ...

    def RemoveAll(self, ) -> None:
        ...

    def CopyTo(self, array: System.Array, index: int, ) -> None:
        ...

    def CopyTo(self, array: System.Array[System.Xml.XmlAttribute], index: int, ) -> None:
        ...

    def AddNode(self, node: System.Xml.XmlNode, ) -> System.Xml.XmlNode:
        ...

    def InsertNodeAt(self, i: int, node: System.Xml.XmlNode, ) -> System.Xml.XmlNode:
        ...

    def RemoveNodeAt(self, i: int, ) -> System.Xml.XmlNode:
        ...

    def Detach(self, attr: System.Xml.XmlAttribute, ) -> None:
        ...

    def InsertParentIntoElementIdAttrMap(self, attr: System.Xml.XmlAttribute, ) -> None:
        ...

    def RemoveParentFromElementIdAttrMap(self, attr: System.Xml.XmlAttribute, ) -> None:
        ...

    def RemoveDuplicateAttribute(self, attr: System.Xml.XmlAttribute, ) -> int:
        ...

    def PrepareParentInElementIdAttrMap(self, attrPrefix: str, attrLocalName: str, ) -> bool:
        ...

    def ResetParentInElementIdAttrMap(self, oldVal: str, newVal: str, ) -> None:
        ...

    def InternalAppendAttribute(self, node: System.Xml.XmlAttribute, ) -> System.Xml.XmlAttribute:
        ...

class XmlNamedNodeMap(System.Collections.IEnumerable, System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        self.parent: System.Xml.XmlNode
        self.nodes: System.Xml.XmlNamedNodeMap.SmallXmlNodeList
        ...

    # static fields

    # properties
    @property
    def Count(self) -> int:
        ...

    # methods
    def __init__(self, parent: System.Xml.XmlNode, ):
        ...

    def SetNamedItem(self, node: System.Xml.XmlNode, ) -> System.Xml.XmlNode:
        ...

    def AddNode(self, node: System.Xml.XmlNode, ) -> System.Xml.XmlNode:
        ...

    def InsertNodeAt(self, i: int, node: System.Xml.XmlNode, ) -> System.Xml.XmlNode:
        ...

    def RemoveNodeAt(self, i: int, ) -> System.Xml.XmlNode:
        ...

    @typing.overload
    def GetNamedItem(self, name: str, ) -> System.Xml.XmlNode:
        ...

    @typing.overload
    def GetNamedItem(self, localName: str, namespaceURI: str, ) -> System.Xml.XmlNode:
        ...

    @typing.overload
    def RemoveNamedItem(self, name: str, ) -> System.Xml.XmlNode:
        ...

    @typing.overload
    def RemoveNamedItem(self, localName: str, namespaceURI: str, ) -> System.Xml.XmlNode:
        ...

    def Item(self, index: int, ) -> System.Xml.XmlNode:
        ...

    def GetEnumerator(self, ) -> System.Collections.IEnumerator:
        ...

    @typing.overload
    def FindNodeOffset(self, name: str, ) -> int:
        ...

    @typing.overload
    def FindNodeOffset(self, localName: str, namespaceURI: str, ) -> int:
        ...

    def AddNodeForLoad(self, node: System.Xml.XmlNode, doc: System.Xml.XmlDocument, ) -> System.Xml.XmlNode:
        ...

    def ReplaceNodeAt(self, i: int, node: System.Xml.XmlNode, ) -> System.Xml.XmlNode:
        ...

class XmlNodeList(System.Collections.IEnumerable, System.IDisposable, System.Object, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    @abc.abstractmethod
    def Count(self) -> int:
        ...

    @property
    def ItemOf(self) -> System.Xml.XmlNode:
        ...

    # methods
    def __init__(self, ):
        ...

    @abc.abstractmethod
    def Item(self, index: int, ) -> System.Xml.XmlNode:
        ...

    @abc.abstractmethod
    def GetEnumerator(self, ) -> System.Collections.IEnumerator:
        ...

    def Dispose(self, ) -> None:
        ...

    def PrivateDisposeNodeList(self, ) -> None:
        ...

class XmlDocument(System.ICloneable, System.Collections.IEnumerable, System.Xml.XPath.IXPathNavigable, System.Xml.XmlNode):
    @typing.overload
    def __init__(self, **kwargs):
        self.fEntRefNodesPresent: bool
        self.fCDataNodesPresent: bool
        self.strDocumentName: str
        self.strDocumentFragmentName: str
        self.strCommentName: str
        self.strTextName: str
        self.strCDataSectionName: str
        self.strEntityName: str
        self.strID: str
        self.strXmlns: str
        self.strXml: str
        self.strSpace: str
        self.strLang: str
        self.strNonSignificantWhitespaceName: str
        self.strSignificantWhitespaceName: str
        self.strReservedXmlns: str
        self.strReservedXml: str
        self.baseURI: str
        self.bSetResolver: bool
        self.objLock: System.Object
        self.parentNode: System.Xml.XmlNode
        ...

    # static fields
    EmptyEnumerator: System.Xml.EmptyEnumerator = ...
    NotKnownSchemaInfo: System.Xml.Schema.IXmlSchemaInfo = ...
    ValidSchemaInfo: System.Xml.Schema.IXmlSchemaInfo = ...
    InvalidSchemaInfo: System.Xml.Schema.IXmlSchemaInfo = ...

    # properties
    @property
    def DtdSchemaInfo(self) -> System.Xml.Schema.SchemaInfo:
        ...
    @DtdSchemaInfo.setter
    def DtdSchemaInfo(self, val: System.Xml.Schema.SchemaInfo):
        ...

    @property
    def NodeType(self) -> int:
        ...

    @property
    def ParentNode(self) -> System.Xml.XmlNode:
        ...

    @property
    def DocumentType(self) -> System.Xml.XmlDocumentType:
        ...

    @property
    def Declaration(self) -> System.Xml.XmlDeclaration:
        ...

    @property
    def Implementation(self) -> System.Xml.XmlImplementation:
        ...

    @property
    def Name(self) -> str:
        ...

    @property
    def LocalName(self) -> str:
        ...

    @property
    def DocumentElement(self) -> System.Xml.XmlElement:
        ...

    @property
    def IsContainer(self) -> bool:
        ...

    @property
    def LastNode(self) -> System.Xml.XmlLinkedNode:
        ...
    @LastNode.setter
    def LastNode(self, val: System.Xml.XmlLinkedNode):
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

    @property
    def CanReportValidity(self) -> bool:
        ...

    @property
    def HasSetResolver(self) -> bool:
        ...

    XmlResolver: System.Xml.XmlResolver = property(None, lambda val: ...)

    @property
    def NameTable(self) -> System.Xml.XmlNameTable:
        ...

    @property
    def PreserveWhitespace(self) -> bool:
        ...
    @PreserveWhitespace.setter
    def PreserveWhitespace(self, val: bool):
        ...

    @property
    def IsReadOnly(self) -> bool:
        ...

    @property
    def Entities(self) -> System.Xml.XmlNamedNodeMap:
        ...
    @Entities.setter
    def Entities(self, val: System.Xml.XmlNamedNodeMap):
        ...

    @property
    def IsLoading(self) -> bool:
        ...
    @IsLoading.setter
    def IsLoading(self, val: bool):
        ...

    @property
    def ActualLoadingStatus(self) -> bool:
        ...

    @property
    def TextEncoding(self) -> System.Text.Encoding:
        ...

    InnerText: str = property(None, lambda val: ...)

    @property
    def InnerXml(self) -> str:
        ...
    @InnerXml.setter
    def InnerXml(self, val: str):
        ...

    @property
    def Version(self) -> str:
        ...

    @property
    def Encoding(self) -> str:
        ...

    @property
    def Standalone(self) -> str:
        ...

    @property
    def SchemaInfo(self) -> System.Xml.Schema.IXmlSchemaInfo:
        ...

    @property
    def BaseURI(self) -> str:
        ...

    @property
    def XPNodeType(self) -> int:
        ...

    @property
    def HasEntityReferences(self) -> bool:
        ...

    @property
    def NamespaceXml(self) -> System.Xml.XmlAttribute:
        ...

    @property
    def Value(self) -> str:
        ...
    @Value.setter
    def Value(self, val: str):
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
    def HasChildNodes(self) -> bool:
        ...

    @property
    def NamespaceURI(self) -> str:
        ...

    @property
    def Prefix(self) -> str:
        ...
    @Prefix.setter
    def Prefix(self, val: str):
        ...

    @property
    def OuterXml(self) -> str:
        ...

    @property
    def Document(self) -> System.Xml.XmlDocument:
        ...

    @property
    def Item(self) -> System.Xml.XmlElement:
        ...

    @property
    def Item(self) -> System.Xml.XmlElement:
        ...

    @property
    def XmlSpace(self) -> int:
        ...

    @property
    def XmlLang(self) -> str:
        ...

    @property
    def XPLocalName(self) -> str:
        ...

    @property
    def IsText(self) -> bool:
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
    def __init__(self, imp: System.Xml.XmlImplementation, ):
        ...

    def GetEventArgs(self, node: System.Xml.XmlNode, oldParent: System.Xml.XmlNode, newParent: System.Xml.XmlNode, oldValue: str, newValue: str, action: int, ) -> System.Xml.XmlNodeChangedEventArgs:
        ...

    def GetInsertEventArgsForLoad(self, node: System.Xml.XmlNode, newParent: System.Xml.XmlNode, ) -> System.Xml.XmlNodeChangedEventArgs:
        ...

    def BeforeEvent(self, args: System.Xml.XmlNodeChangedEventArgs, ) -> None:
        ...

    def AfterEvent(self, args: System.Xml.XmlNodeChangedEventArgs, ) -> None:
        ...

    def GetDefaultAttribute(self, elem: System.Xml.XmlElement, attrPrefix: str, attrLocalname: str, attrNamespaceURI: str, ) -> System.Xml.XmlAttribute:
        ...

    def GetEntityNode(self, name: str, ) -> System.Xml.XmlEntity:
        ...

    def SetBaseURI(self, inBaseURI: str, ) -> None:
        ...

    def AppendChildForLoad(self, newChild: System.Xml.XmlNode, doc: System.Xml.XmlDocument, ) -> System.Xml.XmlNode:
        ...

    @staticmethod
    def CheckName(name: str, ) -> None:
        ...

    def AddXmlName(self, prefix: str, localName: str, namespaceURI: str, schemaInfo: System.Xml.Schema.IXmlSchemaInfo, ) -> System.Xml.XmlName:
        ...

    def GetXmlName(self, prefix: str, localName: str, namespaceURI: str, schemaInfo: System.Xml.Schema.IXmlSchemaInfo, ) -> System.Xml.XmlName:
        ...

    def AddAttrXmlName(self, prefix: str, localName: str, namespaceURI: str, schemaInfo: System.Xml.Schema.IXmlSchemaInfo, ) -> System.Xml.XmlName:
        ...

    def AddIdInfo(self, eleName: System.Xml.XmlName, attrName: System.Xml.XmlName, ) -> bool:
        ...

    def GetIDInfoByElement_(self, eleName: System.Xml.XmlName, ) -> System.Xml.XmlName:
        ...

    def GetIDInfoByElement(self, eleName: System.Xml.XmlName, ) -> System.Xml.XmlName:
        ...

    def GetElement(self, elementList: System.Collections.ArrayList, elem: System.Xml.XmlElement, ) -> System.WeakReference[System.Xml.XmlElement]:
        ...

    def AddElementWithId(self, id: str, elem: System.Xml.XmlElement, ) -> None:
        ...

    def RemoveElementWithId(self, id: str, elem: System.Xml.XmlElement, ) -> None:
        ...

    def CloneNode(self, deep: bool, ) -> System.Xml.XmlNode:
        ...

    def GetResolver(self, ) -> System.Xml.XmlResolver:
        ...

    def IsValidChildType(self, type: int, ) -> bool:
        ...

    def HasNodeTypeInPrevSiblings(self, nt: int, refNode: System.Xml.XmlNode, ) -> bool:
        ...

    def HasNodeTypeInNextSiblings(self, nt: int, refNode: System.Xml.XmlNode, ) -> bool:
        ...

    def CanInsertBefore(self, newChild: System.Xml.XmlNode, refChild: System.Xml.XmlNode, ) -> bool:
        ...

    def CanInsertAfter(self, newChild: System.Xml.XmlNode, refChild: System.Xml.XmlNode, ) -> bool:
        ...

    @typing.overload
    def CreateAttribute(self, name: str, ) -> System.Xml.XmlAttribute:
        ...

    @typing.overload
    def CreateAttribute(self, qualifiedName: str, namespaceURI: str, ) -> System.Xml.XmlAttribute:
        ...

    @typing.overload
    def CreateAttribute(self, prefix: str, localName: str, namespaceURI: str, ) -> System.Xml.XmlAttribute:
        ...

    def SetDefaultNamespace(self, prefix: str, localName: str, namespaceURI: ref[str], ) -> None:
        ...

    def CreateCDataSection(self, data: str, ) -> System.Xml.XmlCDataSection:
        ...

    def CreateComment(self, data: str, ) -> System.Xml.XmlComment:
        ...

    def CreateDocumentType(self, name: str, publicId: str, systemId: str, internalSubset: str, ) -> System.Xml.XmlDocumentType:
        ...

    def CreateDocumentFragment(self, ) -> System.Xml.XmlDocumentFragment:
        ...

    @typing.overload
    def CreateElement(self, name: str, ) -> System.Xml.XmlElement:
        ...

    @typing.overload
    def CreateElement(self, qualifiedName: str, namespaceURI: str, ) -> System.Xml.XmlElement:
        ...

    @typing.overload
    def CreateElement(self, prefix: str, localName: str, namespaceURI: str, ) -> System.Xml.XmlElement:
        ...

    def AddDefaultAttributes(self, elem: System.Xml.XmlElement, ) -> None:
        ...

    def GetSchemaElementDecl(self, elem: System.Xml.XmlElement, ) -> System.Xml.Schema.SchemaElementDecl:
        ...

    def PrepareDefaultAttribute(self, attdef: System.Xml.Schema.SchemaAttDef, attrPrefix: str, attrLocalname: str, attrNamespaceURI: str, ) -> System.Xml.XmlAttribute:
        ...

    def CreateEntityReference(self, name: str, ) -> System.Xml.XmlEntityReference:
        ...

    def CreateProcessingInstruction(self, target: str, data: str, ) -> System.Xml.XmlProcessingInstruction:
        ...

    def CreateXmlDeclaration(self, version: str, encoding: str, standalone: str, ) -> System.Xml.XmlDeclaration:
        ...

    def CreateTextNode(self, text: str, ) -> System.Xml.XmlText:
        ...

    def CreateSignificantWhitespace(self, text: str, ) -> System.Xml.XmlSignificantWhitespace:
        ...

    @typing.overload
    def CreateNavigator(self, ) -> System.Xml.XPath.XPathNavigator:
        ...

    @typing.overload
    def CreateNavigator(self, node: System.Xml.XmlNode, ) -> System.Xml.XPath.XPathNavigator:
        ...

    @staticmethod
    def IsTextNode(nt: int, ) -> bool:
        ...

    def NormalizeText(self, node: System.Xml.XmlNode, ) -> System.Xml.XmlNode:
        ...

    def CreateWhitespace(self, text: str, ) -> System.Xml.XmlWhitespace:
        ...

    @typing.overload
    def GetElementsByTagName(self, name: str, ) -> System.Xml.XmlNodeList:
        ...

    @typing.overload
    def GetElementsByTagName(self, localName: str, namespaceURI: str, ) -> System.Xml.XmlNodeList:
        ...

    def GetElementById(self, elementId: str, ) -> System.Xml.XmlElement:
        ...

    def ImportNode(self, node: System.Xml.XmlNode, deep: bool, ) -> System.Xml.XmlNode:
        ...

    def ImportNodeInternal(self, node: System.Xml.XmlNode, deep: bool, ) -> System.Xml.XmlNode:
        ...

    def ImportAttributes(self, fromElem: System.Xml.XmlNode, toElem: System.Xml.XmlNode, ) -> None:
        ...

    def ImportChildren(self, fromNode: System.Xml.XmlNode, toNode: System.Xml.XmlNode, deep: bool, ) -> None:
        ...

    def CreateDefaultAttribute(self, prefix: str, localName: str, namespaceURI: str, ) -> System.Xml.XmlAttribute:
        ...

    @typing.overload
    def CreateNode(self, type: int, prefix: str, name: str, namespaceURI: str, ) -> System.Xml.XmlNode:
        ...

    @typing.overload
    def CreateNode(self, nodeTypeString: str, name: str, namespaceURI: str, ) -> System.Xml.XmlNode:
        ...

    @typing.overload
    def CreateNode(self, type: int, name: str, namespaceURI: str, ) -> System.Xml.XmlNode:
        ...

    def ReadNode(self, reader: System.Xml.XmlReader, ) -> System.Xml.XmlNode:
        ...

    def ConvertToNodeType(self, nodeTypeString: str, ) -> int:
        ...

    def SetupReader(self, tr: System.Xml.XmlTextReader, ) -> System.Xml.XmlTextReader:
        ...

    @typing.overload
    def Load(self, filename: str, ) -> None:
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

    def LoadXml(self, xml: str, ) -> None:
        ...

    @typing.overload
    def Save(self, filename: str, ) -> None:
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

    def WriteTo(self, w: System.Xml.XmlWriter, ) -> None:
        ...

    def WriteContentTo(self, xw: System.Xml.XmlWriter, ) -> None:
        ...

    @typing.overload
    def Validate(self, validationEventHandler: System.Xml.Schema.ValidationEventHandler, ) -> None:
        ...

    @typing.overload
    def Validate(self, validationEventHandler: System.Xml.Schema.ValidationEventHandler, nodeToValidate: System.Xml.XmlNode, ) -> None:
        ...

class XmlSignificantWhitespace(System.ICloneable, System.Collections.IEnumerable, System.Xml.XPath.IXPathNavigable, System.Xml.XmlCharacterData):
    @typing.overload
    def __init__(self, **kwargs):
        self.next: System.Xml.XmlLinkedNode
        self.parentNode: System.Xml.XmlNode
        ...

    # static fields

    # properties
    @property
    def Name(self) -> str:
        ...

    @property
    def LocalName(self) -> str:
        ...

    @property
    def NodeType(self) -> int:
        ...

    @property
    def ParentNode(self) -> System.Xml.XmlNode:
        ...

    @property
    def Value(self) -> str:
        ...
    @Value.setter
    def Value(self, val: str):
        ...

    @property
    def XPNodeType(self) -> int:
        ...

    @property
    def IsText(self) -> bool:
        ...

    @property
    def PreviousText(self) -> System.Xml.XmlNode:
        ...

    @property
    def InnerText(self) -> str:
        ...
    @InnerText.setter
    def InnerText(self, val: str):
        ...

    @property
    def Data(self) -> str:
        ...
    @Data.setter
    def Data(self, val: str):
        ...

    @property
    def Length(self) -> int:
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
    def IsContainer(self) -> bool:
        ...

    @property
    def LastNode(self) -> System.Xml.XmlLinkedNode:
        ...
    @LastNode.setter
    def LastNode(self, val: System.Xml.XmlLinkedNode):
        ...

    @property
    def HasChildNodes(self) -> bool:
        ...

    @property
    def NamespaceURI(self) -> str:
        ...

    @property
    def Prefix(self) -> str:
        ...
    @Prefix.setter
    def Prefix(self, val: str):
        ...

    @property
    def IsReadOnly(self) -> bool:
        ...

    @property
    def OuterXml(self) -> str:
        ...

    @property
    def InnerXml(self) -> str:
        ...
    @InnerXml.setter
    def InnerXml(self, val: str):
        ...

    @property
    def SchemaInfo(self) -> System.Xml.Schema.IXmlSchemaInfo:
        ...

    @property
    def BaseURI(self) -> str:
        ...

    @property
    def Document(self) -> System.Xml.XmlDocument:
        ...

    @property
    def Item(self) -> System.Xml.XmlElement:
        ...

    @property
    def Item(self) -> System.Xml.XmlElement:
        ...

    @property
    def XmlSpace(self) -> int:
        ...

    @property
    def XmlLang(self) -> str:
        ...

    @property
    def XPLocalName(self) -> str:
        ...

    # methods
    def __init__(self, strData: str, doc: System.Xml.XmlDocument, ):
        ...

    def CloneNode(self, deep: bool, ) -> System.Xml.XmlNode:
        ...

    def WriteTo(self, w: System.Xml.XmlWriter, ) -> None:
        ...

    def WriteContentTo(self, w: System.Xml.XmlWriter, ) -> None:
        ...

class XmlEntity(System.ICloneable, System.Collections.IEnumerable, System.Xml.XPath.IXPathNavigable, System.Xml.XmlNode):
    @typing.overload
    def __init__(self, **kwargs):
        self.parentNode: System.Xml.XmlNode
        ...

    # static fields

    # properties
    @property
    def IsReadOnly(self) -> bool:
        ...

    @property
    def Name(self) -> str:
        ...

    @property
    def LocalName(self) -> str:
        ...

    @property
    def InnerText(self) -> str:
        ...
    @InnerText.setter
    def InnerText(self, val: str):
        ...

    @property
    def IsContainer(self) -> bool:
        ...

    @property
    def LastNode(self) -> System.Xml.XmlLinkedNode:
        ...
    @LastNode.setter
    def LastNode(self, val: System.Xml.XmlLinkedNode):
        ...

    @property
    def NodeType(self) -> int:
        ...

    @property
    def PublicId(self) -> str:
        ...

    @property
    def SystemId(self) -> str:
        ...

    @property
    def NotationName(self) -> str:
        ...

    @property
    def OuterXml(self) -> str:
        ...

    @property
    def InnerXml(self) -> str:
        ...
    @InnerXml.setter
    def InnerXml(self, val: str):
        ...

    @property
    def BaseURI(self) -> str:
        ...

    @property
    def Value(self) -> str:
        ...
    @Value.setter
    def Value(self, val: str):
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
    def HasChildNodes(self) -> bool:
        ...

    @property
    def NamespaceURI(self) -> str:
        ...

    @property
    def Prefix(self) -> str:
        ...
    @Prefix.setter
    def Prefix(self, val: str):
        ...

    @property
    def SchemaInfo(self) -> System.Xml.Schema.IXmlSchemaInfo:
        ...

    @property
    def Document(self) -> System.Xml.XmlDocument:
        ...

    @property
    def Item(self) -> System.Xml.XmlElement:
        ...

    @property
    def Item(self) -> System.Xml.XmlElement:
        ...

    @property
    def XmlSpace(self) -> int:
        ...

    @property
    def XmlLang(self) -> str:
        ...

    @property
    def XPNodeType(self) -> int:
        ...

    @property
    def XPLocalName(self) -> str:
        ...

    @property
    def IsText(self) -> bool:
        ...

    @property
    def PreviousText(self) -> System.Xml.XmlNode:
        ...

    # methods
    def __init__(self, name: str, strdata: str, publicId: str, systemId: str, notationName: str, doc: System.Xml.XmlDocument, ):
        ...

    def CloneNode(self, deep: bool, ) -> System.Xml.XmlNode:
        ...

    def IsValidChildType(self, type: int, ) -> bool:
        ...

    def WriteTo(self, w: System.Xml.XmlWriter, ) -> None:
        ...

    def WriteContentTo(self, w: System.Xml.XmlWriter, ) -> None:
        ...

    def SetBaseURI(self, inBaseURI: str, ) -> None:
        ...

class XmlComment(System.ICloneable, System.Collections.IEnumerable, System.Xml.XPath.IXPathNavigable, System.Xml.XmlCharacterData):
    @typing.overload
    def __init__(self, **kwargs):
        self.next: System.Xml.XmlLinkedNode
        self.parentNode: System.Xml.XmlNode
        ...

    # static fields

    # properties
    @property
    def Name(self) -> str:
        ...

    @property
    def LocalName(self) -> str:
        ...

    @property
    def NodeType(self) -> int:
        ...

    @property
    def XPNodeType(self) -> int:
        ...

    @property
    def Value(self) -> str:
        ...
    @Value.setter
    def Value(self, val: str):
        ...

    @property
    def InnerText(self) -> str:
        ...
    @InnerText.setter
    def InnerText(self, val: str):
        ...

    @property
    def Data(self) -> str:
        ...
    @Data.setter
    def Data(self, val: str):
        ...

    @property
    def Length(self) -> int:
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
    def IsContainer(self) -> bool:
        ...

    @property
    def LastNode(self) -> System.Xml.XmlLinkedNode:
        ...
    @LastNode.setter
    def LastNode(self, val: System.Xml.XmlLinkedNode):
        ...

    @property
    def HasChildNodes(self) -> bool:
        ...

    @property
    def NamespaceURI(self) -> str:
        ...

    @property
    def Prefix(self) -> str:
        ...
    @Prefix.setter
    def Prefix(self, val: str):
        ...

    @property
    def IsReadOnly(self) -> bool:
        ...

    @property
    def OuterXml(self) -> str:
        ...

    @property
    def InnerXml(self) -> str:
        ...
    @InnerXml.setter
    def InnerXml(self, val: str):
        ...

    @property
    def SchemaInfo(self) -> System.Xml.Schema.IXmlSchemaInfo:
        ...

    @property
    def BaseURI(self) -> str:
        ...

    @property
    def Document(self) -> System.Xml.XmlDocument:
        ...

    @property
    def Item(self) -> System.Xml.XmlElement:
        ...

    @property
    def Item(self) -> System.Xml.XmlElement:
        ...

    @property
    def XmlSpace(self) -> int:
        ...

    @property
    def XmlLang(self) -> str:
        ...

    @property
    def XPLocalName(self) -> str:
        ...

    @property
    def IsText(self) -> bool:
        ...

    @property
    def PreviousText(self) -> System.Xml.XmlNode:
        ...

    # methods
    def __init__(self, comment: str, doc: System.Xml.XmlDocument, ):
        ...

    def CloneNode(self, deep: bool, ) -> System.Xml.XmlNode:
        ...

    def WriteTo(self, w: System.Xml.XmlWriter, ) -> None:
        ...

    def WriteContentTo(self, w: System.Xml.XmlWriter, ) -> None:
        ...

class XmlText(System.ICloneable, System.Collections.IEnumerable, System.Xml.XPath.IXPathNavigable, System.Xml.XmlCharacterData):
    @typing.overload
    def __init__(self, **kwargs):
        self.next: System.Xml.XmlLinkedNode
        self.parentNode: System.Xml.XmlNode
        ...

    # static fields

    # properties
    @property
    def Name(self) -> str:
        ...

    @property
    def LocalName(self) -> str:
        ...

    @property
    def NodeType(self) -> int:
        ...

    @property
    def ParentNode(self) -> System.Xml.XmlNode:
        ...

    @property
    def Value(self) -> str:
        ...
    @Value.setter
    def Value(self, val: str):
        ...

    @property
    def XPNodeType(self) -> int:
        ...

    @property
    def IsText(self) -> bool:
        ...

    @property
    def PreviousText(self) -> System.Xml.XmlNode:
        ...

    @property
    def InnerText(self) -> str:
        ...
    @InnerText.setter
    def InnerText(self, val: str):
        ...

    @property
    def Data(self) -> str:
        ...
    @Data.setter
    def Data(self, val: str):
        ...

    @property
    def Length(self) -> int:
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
    def IsContainer(self) -> bool:
        ...

    @property
    def LastNode(self) -> System.Xml.XmlLinkedNode:
        ...
    @LastNode.setter
    def LastNode(self, val: System.Xml.XmlLinkedNode):
        ...

    @property
    def HasChildNodes(self) -> bool:
        ...

    @property
    def NamespaceURI(self) -> str:
        ...

    @property
    def Prefix(self) -> str:
        ...
    @Prefix.setter
    def Prefix(self, val: str):
        ...

    @property
    def IsReadOnly(self) -> bool:
        ...

    @property
    def OuterXml(self) -> str:
        ...

    @property
    def InnerXml(self) -> str:
        ...
    @InnerXml.setter
    def InnerXml(self, val: str):
        ...

    @property
    def SchemaInfo(self) -> System.Xml.Schema.IXmlSchemaInfo:
        ...

    @property
    def BaseURI(self) -> str:
        ...

    @property
    def Document(self) -> System.Xml.XmlDocument:
        ...

    @property
    def Item(self) -> System.Xml.XmlElement:
        ...

    @property
    def Item(self) -> System.Xml.XmlElement:
        ...

    @property
    def XmlSpace(self) -> int:
        ...

    @property
    def XmlLang(self) -> str:
        ...

    @property
    def XPLocalName(self) -> str:
        ...

    # methods
    @typing.overload
    def __init__(self, strData: str, ):
        ...

    @typing.overload
    def __init__(self, strData: str, doc: System.Xml.XmlDocument, ):
        ...

    def CloneNode(self, deep: bool, ) -> System.Xml.XmlNode:
        ...

    def SplitText(self, offset: int, ) -> System.Xml.XmlText:
        ...

    def WriteTo(self, w: System.Xml.XmlWriter, ) -> None:
        ...

    def WriteContentTo(self, w: System.Xml.XmlWriter, ) -> None:
        ...

class XmlCharacterData(System.ICloneable, System.Collections.IEnumerable, System.Xml.XPath.IXPathNavigable, System.Xml.XmlLinkedNode, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        self.next: System.Xml.XmlLinkedNode
        self.parentNode: System.Xml.XmlNode
        ...

    # static fields

    # properties
    @property
    def Value(self) -> str:
        ...
    @Value.setter
    def Value(self, val: str):
        ...

    @property
    def InnerText(self) -> str:
        ...
    @InnerText.setter
    def InnerText(self, val: str):
        ...

    @property
    def Data(self) -> str:
        ...
    @Data.setter
    def Data(self, val: str):
        ...

    @property
    def Length(self) -> int:
        ...

    @property
    def PreviousSibling(self) -> System.Xml.XmlNode:
        ...

    @property
    def NextSibling(self) -> System.Xml.XmlNode:
        ...

    @property
    @abc.abstractmethod
    def Name(self) -> str:
        ...

    @property
    @abc.abstractmethod
    def NodeType(self) -> int:
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
    def IsContainer(self) -> bool:
        ...

    @property
    def LastNode(self) -> System.Xml.XmlLinkedNode:
        ...
    @LastNode.setter
    def LastNode(self, val: System.Xml.XmlLinkedNode):
        ...

    @property
    def HasChildNodes(self) -> bool:
        ...

    @property
    def NamespaceURI(self) -> str:
        ...

    @property
    def Prefix(self) -> str:
        ...
    @Prefix.setter
    def Prefix(self, val: str):
        ...

    @property
    @abc.abstractmethod
    def LocalName(self) -> str:
        ...

    @property
    def IsReadOnly(self) -> bool:
        ...

    @property
    def OuterXml(self) -> str:
        ...

    @property
    def InnerXml(self) -> str:
        ...
    @InnerXml.setter
    def InnerXml(self, val: str):
        ...

    @property
    def SchemaInfo(self) -> System.Xml.Schema.IXmlSchemaInfo:
        ...

    @property
    def BaseURI(self) -> str:
        ...

    @property
    def Document(self) -> System.Xml.XmlDocument:
        ...

    @property
    def Item(self) -> System.Xml.XmlElement:
        ...

    @property
    def Item(self) -> System.Xml.XmlElement:
        ...

    @property
    def XmlSpace(self) -> int:
        ...

    @property
    def XmlLang(self) -> str:
        ...

    @property
    def XPNodeType(self) -> int:
        ...

    @property
    def XPLocalName(self) -> str:
        ...

    @property
    def IsText(self) -> bool:
        ...

    @property
    def PreviousText(self) -> System.Xml.XmlNode:
        ...

    # methods
    def __init__(self, data: str, doc: System.Xml.XmlDocument, ):
        ...

    def Substring(self, offset: int, count: int, ) -> str:
        ...

    def AppendData(self, strData: str, ) -> None:
        ...

    def InsertData(self, offset: int, strData: str, ) -> None:
        ...

    def DeleteData(self, offset: int, count: int, ) -> None:
        ...

    def ReplaceData(self, offset: int, count: int, strData: str, ) -> None:
        ...

    def CheckOnData(self, data: str, ) -> bool:
        ...

    def DecideXPNodeTypeForTextNodes(self, node: System.Xml.XmlNode, xnt: ref[int], ) -> bool:
        ...

class XmlEntityReference(System.ICloneable, System.Collections.IEnumerable, System.Xml.XPath.IXPathNavigable, System.Xml.XmlLinkedNode):
    @typing.overload
    def __init__(self, **kwargs):
        self.next: System.Xml.XmlLinkedNode
        self.parentNode: System.Xml.XmlNode
        ...

    # static fields

    # properties
    @property
    def Name(self) -> str:
        ...

    @property
    def LocalName(self) -> str:
        ...

    @property
    def Value(self) -> str:
        ...
    @Value.setter
    def Value(self, val: str):
        ...

    @property
    def NodeType(self) -> int:
        ...

    @property
    def IsReadOnly(self) -> bool:
        ...

    @property
    def IsContainer(self) -> bool:
        ...

    @property
    def LastNode(self) -> System.Xml.XmlLinkedNode:
        ...
    @LastNode.setter
    def LastNode(self, val: System.Xml.XmlLinkedNode):
        ...

    @property
    def BaseURI(self) -> str:
        ...

    @property
    def ChildBaseURI(self) -> str:
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
    def HasChildNodes(self) -> bool:
        ...

    @property
    def NamespaceURI(self) -> str:
        ...

    @property
    def Prefix(self) -> str:
        ...
    @Prefix.setter
    def Prefix(self, val: str):
        ...

    @property
    def InnerText(self) -> str:
        ...
    @InnerText.setter
    def InnerText(self, val: str):
        ...

    @property
    def OuterXml(self) -> str:
        ...

    @property
    def InnerXml(self) -> str:
        ...
    @InnerXml.setter
    def InnerXml(self, val: str):
        ...

    @property
    def SchemaInfo(self) -> System.Xml.Schema.IXmlSchemaInfo:
        ...

    @property
    def Document(self) -> System.Xml.XmlDocument:
        ...

    @property
    def Item(self) -> System.Xml.XmlElement:
        ...

    @property
    def Item(self) -> System.Xml.XmlElement:
        ...

    @property
    def XmlSpace(self) -> int:
        ...

    @property
    def XmlLang(self) -> str:
        ...

    @property
    def XPNodeType(self) -> int:
        ...

    @property
    def XPLocalName(self) -> str:
        ...

    @property
    def IsText(self) -> bool:
        ...

    @property
    def PreviousText(self) -> System.Xml.XmlNode:
        ...

    # methods
    def __init__(self, name: str, doc: System.Xml.XmlDocument, ):
        ...

    def CloneNode(self, deep: bool, ) -> System.Xml.XmlNode:
        ...

    def SetParent(self, node: System.Xml.XmlNode, ) -> None:
        ...

    def SetParentForLoad(self, node: System.Xml.XmlNode, ) -> None:
        ...

    def IsValidChildType(self, type: int, ) -> bool:
        ...

    def WriteTo(self, w: System.Xml.XmlWriter, ) -> None:
        ...

    def WriteContentTo(self, w: System.Xml.XmlWriter, ) -> None:
        ...

    def ConstructBaseURI(self, baseURI: str, systemId: str, ) -> str:
        ...

class XmlNodeType(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    None_: int = ...
    Element: int = ...
    Attribute: int = ...
    Text: int = ...
    CDATA: int = ...
    EntityReference: int = ...
    Entity: int = ...
    ProcessingInstruction: int = ...
    Comment: int = ...
    Document: int = ...
    DocumentType: int = ...
    DocumentFragment: int = ...
    Notation: int = ...
    Whitespace: int = ...
    SignificantWhitespace: int = ...
    EndElement: int = ...
    EndEntity: int = ...
    XmlDeclaration: int = ...

class XmlElement(System.ICloneable, System.Collections.IEnumerable, System.Xml.XPath.IXPathNavigable, System.Xml.XmlLinkedNode):
    @typing.overload
    def __init__(self, **kwargs):
        self.next: System.Xml.XmlLinkedNode
        self.parentNode: System.Xml.XmlNode
        ...

    # static fields

    # properties
    @property
    def XmlName(self) -> System.Xml.XmlName:
        ...
    @XmlName.setter
    def XmlName(self, val: System.Xml.XmlName):
        ...

    @property
    def Name(self) -> str:
        ...

    @property
    def LocalName(self) -> str:
        ...

    @property
    def NamespaceURI(self) -> str:
        ...

    @property
    def Prefix(self) -> str:
        ...
    @Prefix.setter
    def Prefix(self, val: str):
        ...

    @property
    def NodeType(self) -> int:
        ...

    @property
    def ParentNode(self) -> System.Xml.XmlNode:
        ...

    @property
    def OwnerDocument(self) -> System.Xml.XmlDocument:
        ...

    @property
    def IsContainer(self) -> bool:
        ...

    @property
    def IsEmpty(self) -> bool:
        ...
    @IsEmpty.setter
    def IsEmpty(self, val: bool):
        ...

    @property
    def LastNode(self) -> System.Xml.XmlLinkedNode:
        ...
    @LastNode.setter
    def LastNode(self, val: System.Xml.XmlLinkedNode):
        ...

    @property
    def Attributes(self) -> System.Xml.XmlAttributeCollection:
        ...

    @property
    def HasAttributes(self) -> bool:
        ...

    @property
    def SchemaInfo(self) -> System.Xml.Schema.IXmlSchemaInfo:
        ...

    @property
    def InnerXml(self) -> str:
        ...
    @InnerXml.setter
    def InnerXml(self, val: str):
        ...

    @property
    def InnerText(self) -> str:
        ...
    @InnerText.setter
    def InnerText(self, val: str):
        ...

    @property
    def NextSibling(self) -> System.Xml.XmlNode:
        ...

    @property
    def XPNodeType(self) -> int:
        ...

    @property
    def XPLocalName(self) -> str:
        ...

    @property
    def PreviousSibling(self) -> System.Xml.XmlNode:
        ...

    @property
    def Value(self) -> str:
        ...
    @Value.setter
    def Value(self, val: str):
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
    def HasChildNodes(self) -> bool:
        ...

    @property
    def IsReadOnly(self) -> bool:
        ...

    @property
    def OuterXml(self) -> str:
        ...

    @property
    def BaseURI(self) -> str:
        ...

    @property
    def Document(self) -> System.Xml.XmlDocument:
        ...

    @property
    def Item(self) -> System.Xml.XmlElement:
        ...

    @property
    def Item(self) -> System.Xml.XmlElement:
        ...

    @property
    def XmlSpace(self) -> int:
        ...

    @property
    def XmlLang(self) -> str:
        ...

    @property
    def IsText(self) -> bool:
        ...

    @property
    def PreviousText(self) -> System.Xml.XmlNode:
        ...

    # methods
    @typing.overload
    def __init__(self, name: System.Xml.XmlName, empty: bool, doc: System.Xml.XmlDocument, ):
        ...

    @typing.overload
    def __init__(self, prefix: str, localName: str, namespaceURI: str, doc: System.Xml.XmlDocument, ):
        ...

    def CloneNode(self, deep: bool, ) -> System.Xml.XmlNode:
        ...

    def AppendChildForLoad(self, newChild: System.Xml.XmlNode, doc: System.Xml.XmlDocument, ) -> System.Xml.XmlNode:
        ...

    def IsValidChildType(self, type: int, ) -> bool:
        ...

    @typing.overload
    def GetAttribute(self, name: str, ) -> str:
        ...

    @typing.overload
    def GetAttribute(self, localName: str, namespaceURI: str, ) -> str:
        ...

    @typing.overload
    def SetAttribute(self, name: str, value: str, ) -> None:
        ...

    @typing.overload
    def SetAttribute(self, localName: str, namespaceURI: str, value: str, ) -> str:
        ...

    @typing.overload
    def RemoveAttribute(self, name: str, ) -> None:
        ...

    @typing.overload
    def RemoveAttribute(self, localName: str, namespaceURI: str, ) -> None:
        ...

    @typing.overload
    def GetAttributeNode(self, name: str, ) -> System.Xml.XmlAttribute:
        ...

    @typing.overload
    def GetAttributeNode(self, localName: str, namespaceURI: str, ) -> System.Xml.XmlAttribute:
        ...

    @typing.overload
    def SetAttributeNode(self, newAttr: System.Xml.XmlAttribute, ) -> System.Xml.XmlAttribute:
        ...

    @typing.overload
    def SetAttributeNode(self, localName: str, namespaceURI: str, ) -> System.Xml.XmlAttribute:
        ...

    @typing.overload
    def RemoveAttributeNode(self, oldAttr: System.Xml.XmlAttribute, ) -> System.Xml.XmlAttribute:
        ...

    @typing.overload
    def RemoveAttributeNode(self, localName: str, namespaceURI: str, ) -> System.Xml.XmlAttribute:
        ...

    @typing.overload
    def GetElementsByTagName(self, name: str, ) -> System.Xml.XmlNodeList:
        ...

    @typing.overload
    def GetElementsByTagName(self, localName: str, namespaceURI: str, ) -> System.Xml.XmlNodeList:
        ...

    @typing.overload
    def HasAttribute(self, name: str, ) -> bool:
        ...

    @typing.overload
    def HasAttribute(self, localName: str, namespaceURI: str, ) -> bool:
        ...

    def WriteTo(self, w: System.Xml.XmlWriter, ) -> None:
        ...

    @staticmethod
    def WriteElementTo(writer: System.Xml.XmlWriter, el: System.Xml.XmlElement, ) -> None:
        ...

    def WriteStartElement(self, w: System.Xml.XmlWriter, ) -> None:
        ...

    def WriteContentTo(self, w: System.Xml.XmlWriter, ) -> None:
        ...

    def RemoveAttributeAt(self, i: int, ) -> System.Xml.XmlNode:
        ...

    def RemoveAllAttributes(self, ) -> None:
        ...

    def RemoveAll(self, ) -> None:
        ...

    def RemoveAllChildren(self, ) -> None:
        ...

    def SetParent(self, node: System.Xml.XmlNode, ) -> None:
        ...

    def GetXPAttribute(self, localName: str, ns: str, ) -> str:
        ...

class XmlCDataSection(System.ICloneable, System.Collections.IEnumerable, System.Xml.XPath.IXPathNavigable, System.Xml.XmlCharacterData):
    @typing.overload
    def __init__(self, **kwargs):
        self.next: System.Xml.XmlLinkedNode
        self.parentNode: System.Xml.XmlNode
        ...

    # static fields

    # properties
    @property
    def Name(self) -> str:
        ...

    @property
    def LocalName(self) -> str:
        ...

    @property
    def NodeType(self) -> int:
        ...

    @property
    def ParentNode(self) -> System.Xml.XmlNode:
        ...

    @property
    def XPNodeType(self) -> int:
        ...

    @property
    def IsText(self) -> bool:
        ...

    @property
    def PreviousText(self) -> System.Xml.XmlNode:
        ...

    @property
    def Value(self) -> str:
        ...
    @Value.setter
    def Value(self, val: str):
        ...

    @property
    def InnerText(self) -> str:
        ...
    @InnerText.setter
    def InnerText(self, val: str):
        ...

    @property
    def Data(self) -> str:
        ...
    @Data.setter
    def Data(self, val: str):
        ...

    @property
    def Length(self) -> int:
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
    def IsContainer(self) -> bool:
        ...

    @property
    def LastNode(self) -> System.Xml.XmlLinkedNode:
        ...
    @LastNode.setter
    def LastNode(self, val: System.Xml.XmlLinkedNode):
        ...

    @property
    def HasChildNodes(self) -> bool:
        ...

    @property
    def NamespaceURI(self) -> str:
        ...

    @property
    def Prefix(self) -> str:
        ...
    @Prefix.setter
    def Prefix(self, val: str):
        ...

    @property
    def IsReadOnly(self) -> bool:
        ...

    @property
    def OuterXml(self) -> str:
        ...

    @property
    def InnerXml(self) -> str:
        ...
    @InnerXml.setter
    def InnerXml(self, val: str):
        ...

    @property
    def SchemaInfo(self) -> System.Xml.Schema.IXmlSchemaInfo:
        ...

    @property
    def BaseURI(self) -> str:
        ...

    @property
    def Document(self) -> System.Xml.XmlDocument:
        ...

    @property
    def Item(self) -> System.Xml.XmlElement:
        ...

    @property
    def Item(self) -> System.Xml.XmlElement:
        ...

    @property
    def XmlSpace(self) -> int:
        ...

    @property
    def XmlLang(self) -> str:
        ...

    @property
    def XPLocalName(self) -> str:
        ...

    # methods
    def __init__(self, data: str, doc: System.Xml.XmlDocument, ):
        ...

    def CloneNode(self, deep: bool, ) -> System.Xml.XmlNode:
        ...

    def WriteTo(self, w: System.Xml.XmlWriter, ) -> None:
        ...

    def WriteContentTo(self, w: System.Xml.XmlWriter, ) -> None:
        ...

class XmlNodeChangedAction(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    Insert: int = ...
    Remove: int = ...
    Change: int = ...

class XmlImplementation(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def NameTable(self) -> System.Xml.XmlNameTable:
        ...

    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def __init__(self, nt: System.Xml.XmlNameTable, ):
        ...

    def HasFeature(self, strFeature: str, strVersion: str, ) -> bool:
        ...

    def CreateDocument(self, ) -> System.Xml.XmlDocument:
        ...

class ConformanceLevel(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    Auto: int = ...
    Fragment: int = ...
    Document: int = ...

class XmlDocumentType(System.ICloneable, System.Collections.IEnumerable, System.Xml.XPath.IXPathNavigable, System.Xml.XmlLinkedNode):
    @typing.overload
    def __init__(self, **kwargs):
        self.next: System.Xml.XmlLinkedNode
        self.parentNode: System.Xml.XmlNode
        ...

    # static fields

    # properties
    @property
    def Name(self) -> str:
        ...

    @property
    def LocalName(self) -> str:
        ...

    @property
    def NodeType(self) -> int:
        ...

    @property
    def IsReadOnly(self) -> bool:
        ...

    @property
    def Entities(self) -> System.Xml.XmlNamedNodeMap:
        ...

    @property
    def Notations(self) -> System.Xml.XmlNamedNodeMap:
        ...

    @property
    def PublicId(self) -> str:
        ...

    @property
    def SystemId(self) -> str:
        ...

    @property
    def InternalSubset(self) -> str:
        ...

    @property
    def ParseWithNamespaces(self) -> bool:
        ...

    @property
    def DtdSchemaInfo(self) -> System.Xml.Schema.SchemaInfo:
        ...
    @DtdSchemaInfo.setter
    def DtdSchemaInfo(self, val: System.Xml.Schema.SchemaInfo):
        ...

    @property
    def PreviousSibling(self) -> System.Xml.XmlNode:
        ...

    @property
    def NextSibling(self) -> System.Xml.XmlNode:
        ...

    @property
    def Value(self) -> str:
        ...
    @Value.setter
    def Value(self, val: str):
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
    def IsContainer(self) -> bool:
        ...

    @property
    def LastNode(self) -> System.Xml.XmlLinkedNode:
        ...
    @LastNode.setter
    def LastNode(self, val: System.Xml.XmlLinkedNode):
        ...

    @property
    def HasChildNodes(self) -> bool:
        ...

    @property
    def NamespaceURI(self) -> str:
        ...

    @property
    def Prefix(self) -> str:
        ...
    @Prefix.setter
    def Prefix(self, val: str):
        ...

    @property
    def InnerText(self) -> str:
        ...
    @InnerText.setter
    def InnerText(self, val: str):
        ...

    @property
    def OuterXml(self) -> str:
        ...

    @property
    def InnerXml(self) -> str:
        ...
    @InnerXml.setter
    def InnerXml(self, val: str):
        ...

    @property
    def SchemaInfo(self) -> System.Xml.Schema.IXmlSchemaInfo:
        ...

    @property
    def BaseURI(self) -> str:
        ...

    @property
    def Document(self) -> System.Xml.XmlDocument:
        ...

    @property
    def Item(self) -> System.Xml.XmlElement:
        ...

    @property
    def Item(self) -> System.Xml.XmlElement:
        ...

    @property
    def XmlSpace(self) -> int:
        ...

    @property
    def XmlLang(self) -> str:
        ...

    @property
    def XPNodeType(self) -> int:
        ...

    @property
    def XPLocalName(self) -> str:
        ...

    @property
    def IsText(self) -> bool:
        ...

    @property
    def PreviousText(self) -> System.Xml.XmlNode:
        ...

    # methods
    def __init__(self, name: str, publicId: str, systemId: str, internalSubset: str, doc: System.Xml.XmlDocument, ):
        ...

    def CloneNode(self, deep: bool, ) -> System.Xml.XmlNode:
        ...

    def WriteTo(self, w: System.Xml.XmlWriter, ) -> None:
        ...

    def WriteContentTo(self, w: System.Xml.XmlWriter, ) -> None:
        ...

class XmlReader(System.IDisposable, System.Object, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def Settings(self) -> System.Xml.XmlReaderSettings:
        ...

    @property
    @abc.abstractmethod
    def NodeType(self) -> int:
        ...

    @property
    def Name(self) -> str:
        ...

    @property
    @abc.abstractmethod
    def LocalName(self) -> str:
        ...

    @property
    @abc.abstractmethod
    def NamespaceURI(self) -> str:
        ...

    @property
    @abc.abstractmethod
    def Prefix(self) -> str:
        ...

    @property
    def HasValue(self) -> bool:
        ...

    @property
    @abc.abstractmethod
    def Value(self) -> str:
        ...

    @property
    @abc.abstractmethod
    def Depth(self) -> int:
        ...

    @property
    @abc.abstractmethod
    def BaseURI(self) -> str:
        ...

    @property
    @abc.abstractmethod
    def IsEmptyElement(self) -> bool:
        ...

    @property
    def IsDefault(self) -> bool:
        ...

    @property
    def QuoteChar(self) -> str:
        ...

    @property
    def XmlSpace(self) -> int:
        ...

    @property
    def XmlLang(self) -> str:
        ...

    @property
    def SchemaInfo(self) -> System.Xml.Schema.IXmlSchemaInfo:
        ...

    @property
    def ValueType(self) -> System.Type:
        ...

    @property
    @abc.abstractmethod
    def AttributeCount(self) -> int:
        ...

    @property
    def Item(self) -> str:
        ...

    @property
    def Item(self) -> str:
        ...

    @property
    def Item(self) -> str:
        ...

    @property
    @abc.abstractmethod
    def EOF(self) -> bool:
        ...

    @property
    @abc.abstractmethod
    def ReadState(self) -> int:
        ...

    @property
    @abc.abstractmethod
    def NameTable(self) -> System.Xml.XmlNameTable:
        ...

    @property
    def CanResolveEntity(self) -> bool:
        ...

    @property
    def CanReadBinaryContent(self) -> bool:
        ...

    @property
    def CanReadValueChunk(self) -> bool:
        ...

    @property
    def HasAttributes(self) -> bool:
        ...

    @property
    def NamespaceManager(self) -> System.Xml.XmlNamespaceManager:
        ...

    @property
    def IsDefaultInternal(self) -> bool:
        ...

    @property
    def DtdInfo(self) -> System.Xml.IDtdInfo:
        ...

    @property
    def DebuggerDisplayProxy(self) -> System.Object:
        ...

    # methods
    def __init__(self, ):
        ...

    @staticmethod
    def AddLineInfo(message: str, lineInfo: System.Xml.IXmlLineInfo, ) -> str:
        ...

    def InternalReadContentAsString(self, ) -> str:
        ...

    def SetupReadElementContentAsXxx(self, methodName: str, ) -> bool:
        ...

    def FinishReadElementContentAsXxx(self, ) -> None:
        ...

    @staticmethod
    def GetV1ConformanceLevel(reader: System.Xml.XmlReader, ) -> int:
        ...

    @staticmethod
    def GetXmlTextReaderImpl(reader: System.Xml.XmlReader, ) -> System.Xml.XmlTextReaderImpl:
        ...

    @staticmethod
    @typing.overload
    def Create(inputUri: str, ) -> System.Xml.XmlReader:
        ...

    @staticmethod
    @typing.overload
    def Create(inputUri: str, settings: System.Xml.XmlReaderSettings, ) -> System.Xml.XmlReader:
        ...

    @staticmethod
    @typing.overload
    def Create(inputUri: str, settings: System.Xml.XmlReaderSettings, inputContext: System.Xml.XmlParserContext, ) -> System.Xml.XmlReader:
        ...

    @staticmethod
    @typing.overload
    def Create(input: System.IO.Stream, ) -> System.Xml.XmlReader:
        ...

    @staticmethod
    @typing.overload
    def Create(input: System.IO.Stream, settings: System.Xml.XmlReaderSettings, ) -> System.Xml.XmlReader:
        ...

    @staticmethod
    @typing.overload
    def Create(input: System.IO.Stream, settings: System.Xml.XmlReaderSettings, baseUri: str, ) -> System.Xml.XmlReader:
        ...

    @staticmethod
    @typing.overload
    def Create(input: System.IO.Stream, settings: System.Xml.XmlReaderSettings, inputContext: System.Xml.XmlParserContext, ) -> System.Xml.XmlReader:
        ...

    @staticmethod
    @typing.overload
    def Create(input: System.IO.TextReader, ) -> System.Xml.XmlReader:
        ...

    @staticmethod
    @typing.overload
    def Create(input: System.IO.TextReader, settings: System.Xml.XmlReaderSettings, ) -> System.Xml.XmlReader:
        ...

    @staticmethod
    @typing.overload
    def Create(input: System.IO.TextReader, settings: System.Xml.XmlReaderSettings, baseUri: str, ) -> System.Xml.XmlReader:
        ...

    @staticmethod
    @typing.overload
    def Create(input: System.IO.TextReader, settings: System.Xml.XmlReaderSettings, inputContext: System.Xml.XmlParserContext, ) -> System.Xml.XmlReader:
        ...

    @staticmethod
    @typing.overload
    def Create(reader: System.Xml.XmlReader, settings: System.Xml.XmlReaderSettings, ) -> System.Xml.XmlReader:
        ...

    @staticmethod
    def CreateSqlReader(input: System.IO.Stream, settings: System.Xml.XmlReaderSettings, inputContext: System.Xml.XmlParserContext, ) -> System.Xml.XmlReader:
        ...

    @staticmethod
    def CalcBufferSize(input: System.IO.Stream, ) -> int:
        ...

    def GetValueAsync(self, ) -> System.Threading.Tasks.Task[str]:
        ...

    def ReadContentAsObjectAsync(self, ) -> System.Threading.Tasks.Task[System.Object]:
        ...

    def ReadContentAsStringAsync(self, ) -> System.Threading.Tasks.Task[str]:
        ...

    def ReadContentAsAsync(self, returnType: System.Type, namespaceResolver: System.Xml.IXmlNamespaceResolver, ) -> System.Threading.Tasks.Task[System.Object]:
        ...

    def ReadElementContentAsObjectAsync(self, ) -> System.Threading.Tasks.Task[System.Object]:
        ...

    def ReadElementContentAsStringAsync(self, ) -> System.Threading.Tasks.Task[str]:
        ...

    def ReadElementContentAsAsync(self, returnType: System.Type, namespaceResolver: System.Xml.IXmlNamespaceResolver, ) -> System.Threading.Tasks.Task[System.Object]:
        ...

    def ReadAsync(self, ) -> System.Threading.Tasks.Task[bool]:
        ...

    def SkipAsync(self, ) -> System.Threading.Tasks.Task:
        ...

    def ReadContentAsBase64Async(self, buffer: System.Array[int], index: int, count: int, ) -> System.Threading.Tasks.Task[int]:
        ...

    def ReadElementContentAsBase64Async(self, buffer: System.Array[int], index: int, count: int, ) -> System.Threading.Tasks.Task[int]:
        ...

    def ReadContentAsBinHexAsync(self, buffer: System.Array[int], index: int, count: int, ) -> System.Threading.Tasks.Task[int]:
        ...

    def ReadElementContentAsBinHexAsync(self, buffer: System.Array[int], index: int, count: int, ) -> System.Threading.Tasks.Task[int]:
        ...

    def ReadValueChunkAsync(self, buffer: System.Array[str], index: int, count: int, ) -> System.Threading.Tasks.Task[int]:
        ...

    def MoveToContentAsync(self, ) -> System.Threading.Tasks.Task[int]:
        ...

    def ReadInnerXmlAsync(self, ) -> System.Threading.Tasks.Task[str]:
        ...

    def WriteNodeAsync(self, xtw: System.Xml.XmlWriter, defattr: bool, ) -> System.Threading.Tasks.Task:
        ...

    def ReadOuterXmlAsync(self, ) -> System.Threading.Tasks.Task[str]:
        ...

    def SkipSubtreeAsync(self, ) -> System.Threading.Tasks.Task[bool]:
        ...

    def InternalReadContentAsStringAsync(self, ) -> System.Threading.Tasks.Task[str]:
        ...

    def SetupReadElementContentAsXxxAsync(self, methodName: str, ) -> System.Threading.Tasks.Task[bool]:
        ...

    def FinishReadElementContentAsXxxAsync(self, ) -> System.Threading.Tasks.Task:
        ...

    def ReadContentAsObject(self, ) -> System.Object:
        ...

    def ReadContentAsBoolean(self, ) -> bool:
        ...

    def ReadContentAsDateTime(self, ) -> System.DateTime:
        ...

    def ReadContentAsDateTimeOffset(self, ) -> System.DateTimeOffset:
        ...

    def ReadContentAsDouble(self, ) -> float:
        ...

    def ReadContentAsFloat(self, ) -> float:
        ...

    def ReadContentAsDecimal(self, ) -> System.Decimal:
        ...

    def ReadContentAsInt(self, ) -> int:
        ...

    def ReadContentAsLong(self, ) -> int:
        ...

    def ReadContentAsString(self, ) -> str:
        ...

    def ReadContentAs(self, returnType: System.Type, namespaceResolver: System.Xml.IXmlNamespaceResolver, ) -> System.Object:
        ...

    @typing.overload
    def ReadElementContentAsObject(self, ) -> System.Object:
        ...

    @typing.overload
    def ReadElementContentAsObject(self, localName: str, namespaceURI: str, ) -> System.Object:
        ...

    @typing.overload
    def ReadElementContentAsBoolean(self, ) -> bool:
        ...

    @typing.overload
    def ReadElementContentAsBoolean(self, localName: str, namespaceURI: str, ) -> bool:
        ...

    @typing.overload
    def ReadElementContentAsDateTime(self, ) -> System.DateTime:
        ...

    @typing.overload
    def ReadElementContentAsDateTime(self, localName: str, namespaceURI: str, ) -> System.DateTime:
        ...

    @typing.overload
    def ReadElementContentAsDouble(self, ) -> float:
        ...

    @typing.overload
    def ReadElementContentAsDouble(self, localName: str, namespaceURI: str, ) -> float:
        ...

    @typing.overload
    def ReadElementContentAsFloat(self, ) -> float:
        ...

    @typing.overload
    def ReadElementContentAsFloat(self, localName: str, namespaceURI: str, ) -> float:
        ...

    @typing.overload
    def ReadElementContentAsDecimal(self, ) -> System.Decimal:
        ...

    @typing.overload
    def ReadElementContentAsDecimal(self, localName: str, namespaceURI: str, ) -> System.Decimal:
        ...

    @typing.overload
    def ReadElementContentAsInt(self, ) -> int:
        ...

    @typing.overload
    def ReadElementContentAsInt(self, localName: str, namespaceURI: str, ) -> int:
        ...

    @typing.overload
    def ReadElementContentAsLong(self, ) -> int:
        ...

    @typing.overload
    def ReadElementContentAsLong(self, localName: str, namespaceURI: str, ) -> int:
        ...

    @typing.overload
    def ReadElementContentAsString(self, ) -> str:
        ...

    @typing.overload
    def ReadElementContentAsString(self, localName: str, namespaceURI: str, ) -> str:
        ...

    @typing.overload
    def ReadElementContentAs(self, returnType: System.Type, namespaceResolver: System.Xml.IXmlNamespaceResolver, ) -> System.Object:
        ...

    @typing.overload
    def ReadElementContentAs(self, returnType: System.Type, namespaceResolver: System.Xml.IXmlNamespaceResolver, localName: str, namespaceURI: str, ) -> System.Object:
        ...

    @abc.abstractmethod
    @typing.overload
    def GetAttribute(self, name: str, ) -> str:
        ...

    @abc.abstractmethod
    @typing.overload
    def GetAttribute(self, name: str, namespaceURI: str, ) -> str:
        ...

    @abc.abstractmethod
    @typing.overload
    def GetAttribute(self, i: int, ) -> str:
        ...

    @abc.abstractmethod
    @typing.overload
    def MoveToAttribute(self, name: str, ) -> bool:
        ...

    @abc.abstractmethod
    @typing.overload
    def MoveToAttribute(self, name: str, ns: str, ) -> bool:
        ...

    @typing.overload
    def MoveToAttribute(self, i: int, ) -> None:
        ...

    @abc.abstractmethod
    def MoveToFirstAttribute(self, ) -> bool:
        ...

    @abc.abstractmethod
    def MoveToNextAttribute(self, ) -> bool:
        ...

    @abc.abstractmethod
    def MoveToElement(self, ) -> bool:
        ...

    @abc.abstractmethod
    def ReadAttributeValue(self, ) -> bool:
        ...

    @abc.abstractmethod
    def Read(self, ) -> bool:
        ...

    def Close(self, ) -> None:
        ...

    def Skip(self, ) -> None:
        ...

    @abc.abstractmethod
    def LookupNamespace(self, prefix: str, ) -> str:
        ...

    @abc.abstractmethod
    def ResolveEntity(self, ) -> None:
        ...

    def ReadContentAsBase64(self, buffer: System.Array[int], index: int, count: int, ) -> int:
        ...

    def ReadElementContentAsBase64(self, buffer: System.Array[int], index: int, count: int, ) -> int:
        ...

    def ReadContentAsBinHex(self, buffer: System.Array[int], index: int, count: int, ) -> int:
        ...

    def ReadElementContentAsBinHex(self, buffer: System.Array[int], index: int, count: int, ) -> int:
        ...

    def ReadValueChunk(self, buffer: System.Array[str], index: int, count: int, ) -> int:
        ...

    def ReadString(self, ) -> str:
        ...

    def MoveToContent(self, ) -> int:
        ...

    @typing.overload
    def ReadStartElement(self, ) -> None:
        ...

    @typing.overload
    def ReadStartElement(self, name: str, ) -> None:
        ...

    @typing.overload
    def ReadStartElement(self, localname: str, ns: str, ) -> None:
        ...

    @typing.overload
    def ReadElementString(self, ) -> str:
        ...

    @typing.overload
    def ReadElementString(self, name: str, ) -> str:
        ...

    @typing.overload
    def ReadElementString(self, localname: str, ns: str, ) -> str:
        ...

    def ReadEndElement(self, ) -> None:
        ...

    @typing.overload
    def IsStartElement(self, ) -> bool:
        ...

    @typing.overload
    def IsStartElement(self, name: str, ) -> bool:
        ...

    @typing.overload
    def IsStartElement(self, localname: str, ns: str, ) -> bool:
        ...

    @typing.overload
    def ReadToFollowing(self, name: str, ) -> bool:
        ...

    @typing.overload
    def ReadToFollowing(self, localName: str, namespaceURI: str, ) -> bool:
        ...

    @typing.overload
    def ReadToDescendant(self, name: str, ) -> bool:
        ...

    @typing.overload
    def ReadToDescendant(self, localName: str, namespaceURI: str, ) -> bool:
        ...

    @typing.overload
    def ReadToNextSibling(self, name: str, ) -> bool:
        ...

    @typing.overload
    def ReadToNextSibling(self, localName: str, namespaceURI: str, ) -> bool:
        ...

    @staticmethod
    def IsName(str: str, ) -> bool:
        ...

    @staticmethod
    def IsNameToken(str: str, ) -> bool:
        ...

    def ReadInnerXml(self, ) -> str:
        ...

    def WriteNode(self, xtw: System.Xml.XmlWriter, defattr: bool, ) -> None:
        ...

    def WriteAttributeValue(self, xtw: System.Xml.XmlWriter, ) -> None:
        ...

    def ReadOuterXml(self, ) -> str:
        ...

    def CreateWriterForInnerOuterXml(self, sw: System.IO.StringWriter, ) -> System.Xml.XmlWriter:
        ...

    def SetNamespacesFlag(self, xtw: System.Xml.XmlTextWriter, ) -> None:
        ...

    def ReadSubtree(self, ) -> System.Xml.XmlReader:
        ...

    @typing.overload
    def Dispose(self, ) -> None:
        ...

    @typing.overload
    def Dispose(self, disposing: bool, ) -> None:
        ...

    @staticmethod
    def IsTextualNode(nodeType: int, ) -> bool:
        ...

    @staticmethod
    @typing.overload
    def CanReadContentAs(nodeType: int, ) -> bool:
        ...

    @typing.overload
    def CanReadContentAs(self, ) -> bool:
        ...

    @staticmethod
    def HasValueInternal(nodeType: int, ) -> bool:
        ...

    def SkipSubtree(self, ) -> bool:
        ...

    def CheckElement(self, localName: str, namespaceURI: str, ) -> None:
        ...

    @typing.overload
    def CreateReadContentAsException(self, methodName: str, ) -> System.Exception:
        ...

    @staticmethod
    @typing.overload
    def CreateReadContentAsException(methodName: str, nodeType: int, lineInfo: System.Xml.IXmlLineInfo, ) -> System.Exception:
        ...

    @typing.overload
    def CreateReadElementContentAsException(self, methodName: str, ) -> System.Exception:
        ...

    @staticmethod
    @typing.overload
    def CreateReadElementContentAsException(methodName: str, nodeType: int, lineInfo: System.Xml.IXmlLineInfo, ) -> System.Exception:
        ...

class IXmlLineInfo(abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    @abc.abstractmethod
    def LineNumber(self) -> int:
        ...

    @property
    @abc.abstractmethod
    def LinePosition(self) -> int:
        ...

    # methods
    @abc.abstractmethod
    def HasLineInfo(self, ) -> bool:
        ...

class XmlWriter(System.IDisposable, System.IAsyncDisposable, System.Object, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def Settings(self) -> System.Xml.XmlWriterSettings:
        ...

    @property
    @abc.abstractmethod
    def WriteState(self) -> int:
        ...

    @property
    def XmlSpace(self) -> int:
        ...

    @property
    def XmlLang(self) -> str:
        ...

    # methods
    def __init__(self, ):
        ...

    @abc.abstractmethod
    @typing.overload
    def WriteStartDocument(self, ) -> None:
        ...

    @abc.abstractmethod
    @typing.overload
    def WriteStartDocument(self, standalone: bool, ) -> None:
        ...

    @abc.abstractmethod
    def WriteEndDocument(self, ) -> None:
        ...

    @abc.abstractmethod
    def WriteDocType(self, name: str, pubid: str, sysid: str, subset: str, ) -> None:
        ...

    @typing.overload
    def WriteStartElement(self, localName: str, ns: str, ) -> None:
        ...

    @abc.abstractmethod
    @typing.overload
    def WriteStartElement(self, prefix: str, localName: str, ns: str, ) -> None:
        ...

    @typing.overload
    def WriteStartElement(self, localName: str, ) -> None:
        ...

    @abc.abstractmethod
    def WriteEndElement(self, ) -> None:
        ...

    @abc.abstractmethod
    def WriteFullEndElement(self, ) -> None:
        ...

    @typing.overload
    def WriteAttributeString(self, localName: str, ns: str, value: str, ) -> None:
        ...

    @typing.overload
    def WriteAttributeString(self, localName: str, value: str, ) -> None:
        ...

    @typing.overload
    def WriteAttributeString(self, prefix: str, localName: str, ns: str, value: str, ) -> None:
        ...

    @typing.overload
    def WriteStartAttribute(self, localName: str, ns: str, ) -> None:
        ...

    @abc.abstractmethod
    @typing.overload
    def WriteStartAttribute(self, prefix: str, localName: str, ns: str, ) -> None:
        ...

    @typing.overload
    def WriteStartAttribute(self, localName: str, ) -> None:
        ...

    @abc.abstractmethod
    def WriteEndAttribute(self, ) -> None:
        ...

    @abc.abstractmethod
    def WriteCData(self, text: str, ) -> None:
        ...

    @abc.abstractmethod
    def WriteComment(self, text: str, ) -> None:
        ...

    @abc.abstractmethod
    def WriteProcessingInstruction(self, name: str, text: str, ) -> None:
        ...

    @abc.abstractmethod
    def WriteEntityRef(self, name: str, ) -> None:
        ...

    @abc.abstractmethod
    def WriteCharEntity(self, ch: str, ) -> None:
        ...

    @abc.abstractmethod
    def WriteWhitespace(self, ws: str, ) -> None:
        ...

    @abc.abstractmethod
    def WriteString(self, text: str, ) -> None:
        ...

    @abc.abstractmethod
    def WriteSurrogateCharEntity(self, lowChar: str, highChar: str, ) -> None:
        ...

    @abc.abstractmethod
    def WriteChars(self, buffer: System.Array[str], index: int, count: int, ) -> None:
        ...

    @abc.abstractmethod
    @typing.overload
    def WriteRaw(self, buffer: System.Array[str], index: int, count: int, ) -> None:
        ...

    @abc.abstractmethod
    @typing.overload
    def WriteRaw(self, data: str, ) -> None:
        ...

    @abc.abstractmethod
    def WriteBase64(self, buffer: System.Array[int], index: int, count: int, ) -> None:
        ...

    def WriteBinHex(self, buffer: System.Array[int], index: int, count: int, ) -> None:
        ...

    def Close(self, ) -> None:
        ...

    @abc.abstractmethod
    def Flush(self, ) -> None:
        ...

    @abc.abstractmethod
    def LookupPrefix(self, ns: str, ) -> str:
        ...

    def WriteNmToken(self, name: str, ) -> None:
        ...

    def WriteName(self, name: str, ) -> None:
        ...

    def WriteQualifiedName(self, localName: str, ns: str, ) -> None:
        ...

    @typing.overload
    def WriteValue(self, value: System.Object, ) -> None:
        ...

    @typing.overload
    def WriteValue(self, value: str, ) -> None:
        ...

    @typing.overload
    def WriteValue(self, value: bool, ) -> None:
        ...

    @typing.overload
    def WriteValue(self, value: System.DateTime, ) -> None:
        ...

    @typing.overload
    def WriteValue(self, value: System.DateTimeOffset, ) -> None:
        ...

    @typing.overload
    def WriteValue(self, value: float, ) -> None:
        ...

    @typing.overload
    def WriteValue(self, value: float, ) -> None:
        ...

    @typing.overload
    def WriteValue(self, value: System.Decimal, ) -> None:
        ...

    @typing.overload
    def WriteValue(self, value: int, ) -> None:
        ...

    @typing.overload
    def WriteValue(self, value: int, ) -> None:
        ...

    def WriteAttributes(self, reader: System.Xml.XmlReader, defattr: bool, ) -> None:
        ...

    @typing.overload
    def WriteNode(self, reader: System.Xml.XmlReader, defattr: bool, ) -> None:
        ...

    @typing.overload
    def WriteNode(self, navigator: System.Xml.XPath.XPathNavigator, defattr: bool, ) -> None:
        ...

    @typing.overload
    def WriteElementString(self, localName: str, value: str, ) -> None:
        ...

    @typing.overload
    def WriteElementString(self, localName: str, ns: str, value: str, ) -> None:
        ...

    @typing.overload
    def WriteElementString(self, prefix: str, localName: str, ns: str, value: str, ) -> None:
        ...

    @typing.overload
    def Dispose(self, ) -> None:
        ...

    @typing.overload
    def Dispose(self, disposing: bool, ) -> None:
        ...

    def WriteLocalNamespaces(self, nsNav: System.Xml.XPath.XPathNavigator, ) -> None:
        ...

    @staticmethod
    @typing.overload
    def Create(outputFileName: str, ) -> System.Xml.XmlWriter:
        ...

    @staticmethod
    @typing.overload
    def Create(outputFileName: str, settings: System.Xml.XmlWriterSettings, ) -> System.Xml.XmlWriter:
        ...

    @staticmethod
    @typing.overload
    def Create(output: System.IO.Stream, ) -> System.Xml.XmlWriter:
        ...

    @staticmethod
    @typing.overload
    def Create(output: System.IO.Stream, settings: System.Xml.XmlWriterSettings, ) -> System.Xml.XmlWriter:
        ...

    @staticmethod
    @typing.overload
    def Create(output: System.IO.TextWriter, ) -> System.Xml.XmlWriter:
        ...

    @staticmethod
    @typing.overload
    def Create(output: System.IO.TextWriter, settings: System.Xml.XmlWriterSettings, ) -> System.Xml.XmlWriter:
        ...

    @staticmethod
    @typing.overload
    def Create(output: System.Text.StringBuilder, ) -> System.Xml.XmlWriter:
        ...

    @staticmethod
    @typing.overload
    def Create(output: System.Text.StringBuilder, settings: System.Xml.XmlWriterSettings, ) -> System.Xml.XmlWriter:
        ...

    @staticmethod
    @typing.overload
    def Create(output: System.Xml.XmlWriter, ) -> System.Xml.XmlWriter:
        ...

    @staticmethod
    @typing.overload
    def Create(output: System.Xml.XmlWriter, settings: System.Xml.XmlWriterSettings, ) -> System.Xml.XmlWriter:
        ...

    @typing.overload
    def WriteStartDocumentAsync(self, ) -> System.Threading.Tasks.Task:
        ...

    @typing.overload
    def WriteStartDocumentAsync(self, standalone: bool, ) -> System.Threading.Tasks.Task:
        ...

    def WriteEndDocumentAsync(self, ) -> System.Threading.Tasks.Task:
        ...

    def WriteDocTypeAsync(self, name: str, pubid: str, sysid: str, subset: str, ) -> System.Threading.Tasks.Task:
        ...

    def WriteStartElementAsync(self, prefix: str, localName: str, ns: str, ) -> System.Threading.Tasks.Task:
        ...

    def WriteEndElementAsync(self, ) -> System.Threading.Tasks.Task:
        ...

    def WriteFullEndElementAsync(self, ) -> System.Threading.Tasks.Task:
        ...

    def WriteAttributeStringAsync(self, prefix: str, localName: str, ns: str, value: str, ) -> System.Threading.Tasks.Task:
        ...

    def WriteAttributeStringAsyncHelper(self, task: System.Threading.Tasks.Task, value: str, ) -> System.Threading.Tasks.Task:
        ...

    def WriteStartAttributeAsync(self, prefix: str, localName: str, ns: str, ) -> System.Threading.Tasks.Task:
        ...

    def WriteEndAttributeAsync(self, ) -> System.Threading.Tasks.Task:
        ...

    def WriteCDataAsync(self, text: str, ) -> System.Threading.Tasks.Task:
        ...

    def WriteCommentAsync(self, text: str, ) -> System.Threading.Tasks.Task:
        ...

    def WriteProcessingInstructionAsync(self, name: str, text: str, ) -> System.Threading.Tasks.Task:
        ...

    def WriteEntityRefAsync(self, name: str, ) -> System.Threading.Tasks.Task:
        ...

    def WriteCharEntityAsync(self, ch: str, ) -> System.Threading.Tasks.Task:
        ...

    def WriteWhitespaceAsync(self, ws: str, ) -> System.Threading.Tasks.Task:
        ...

    def WriteStringAsync(self, text: str, ) -> System.Threading.Tasks.Task:
        ...

    def WriteSurrogateCharEntityAsync(self, lowChar: str, highChar: str, ) -> System.Threading.Tasks.Task:
        ...

    def WriteCharsAsync(self, buffer: System.Array[str], index: int, count: int, ) -> System.Threading.Tasks.Task:
        ...

    @typing.overload
    def WriteRawAsync(self, buffer: System.Array[str], index: int, count: int, ) -> System.Threading.Tasks.Task:
        ...

    @typing.overload
    def WriteRawAsync(self, data: str, ) -> System.Threading.Tasks.Task:
        ...

    def WriteBase64Async(self, buffer: System.Array[int], index: int, count: int, ) -> System.Threading.Tasks.Task:
        ...

    def WriteBinHexAsync(self, buffer: System.Array[int], index: int, count: int, ) -> System.Threading.Tasks.Task:
        ...

    def FlushAsync(self, ) -> System.Threading.Tasks.Task:
        ...

    def WriteNmTokenAsync(self, name: str, ) -> System.Threading.Tasks.Task:
        ...

    def WriteNameAsync(self, name: str, ) -> System.Threading.Tasks.Task:
        ...

    def WriteQualifiedNameAsync(self, localName: str, ns: str, ) -> System.Threading.Tasks.Task:
        ...

    def WriteAttributesAsync(self, reader: System.Xml.XmlReader, defattr: bool, ) -> System.Threading.Tasks.Task:
        ...

    @typing.overload
    def WriteNodeAsync(self, reader: System.Xml.XmlReader, defattr: bool, ) -> System.Threading.Tasks.Task:
        ...

    @typing.overload
    def WriteNodeAsync(self, navigator: System.Xml.XPath.XPathNavigator, defattr: bool, ) -> System.Threading.Tasks.Task:
        ...

    def WriteNodeAsync_CallSyncReader(self, reader: System.Xml.XmlReader, defattr: bool, ) -> System.Threading.Tasks.Task:
        ...

    def WriteNodeAsync_CallAsyncReader(self, reader: System.Xml.XmlReader, defattr: bool, ) -> System.Threading.Tasks.Task:
        ...

    def WriteElementStringAsync(self, prefix: str, localName: str, ns: str, value: str, ) -> System.Threading.Tasks.Task:
        ...

    def WriteLocalNamespacesAsync(self, nsNav: System.Xml.XPath.XPathNavigator, ) -> System.Threading.Tasks.Task:
        ...

    def DisposeAsync(self, ) -> System.Threading.Tasks.ValueTask:
        ...

    def DisposeAsyncCore(self, ) -> System.Threading.Tasks.ValueTask:
        ...

class WriteState(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    Start: int = ...
    Prolog: int = ...
    Element: int = ...
    Attribute: int = ...
    Content: int = ...
    Closed: int = ...
    Error: int = ...

class XmlWriterSettings(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields
    s_defaultWriterSettings: System.Xml.XmlWriterSettings = ...

    # properties
    @property
    def Async(self) -> bool:
        ...
    @Async.setter
    def Async(self, val: bool):
        ...

    @property
    def Encoding(self) -> System.Text.Encoding:
        ...
    @Encoding.setter
    def Encoding(self, val: System.Text.Encoding):
        ...

    @property
    def OmitXmlDeclaration(self) -> bool:
        ...
    @OmitXmlDeclaration.setter
    def OmitXmlDeclaration(self, val: bool):
        ...

    @property
    def NewLineHandling(self) -> int:
        ...
    @NewLineHandling.setter
    def NewLineHandling(self, val: int):
        ...

    @property
    def NewLineChars(self) -> str:
        ...
    @NewLineChars.setter
    def NewLineChars(self, val: str):
        ...

    @property
    def Indent(self) -> bool:
        ...
    @Indent.setter
    def Indent(self, val: bool):
        ...

    @property
    def IndentChars(self) -> str:
        ...
    @IndentChars.setter
    def IndentChars(self, val: str):
        ...

    @property
    def NewLineOnAttributes(self) -> bool:
        ...
    @NewLineOnAttributes.setter
    def NewLineOnAttributes(self, val: bool):
        ...

    @property
    def CloseOutput(self) -> bool:
        ...
    @CloseOutput.setter
    def CloseOutput(self, val: bool):
        ...

    @property
    def ConformanceLevel(self) -> int:
        ...
    @ConformanceLevel.setter
    def ConformanceLevel(self, val: int):
        ...

    @property
    def CheckCharacters(self) -> bool:
        ...
    @CheckCharacters.setter
    def CheckCharacters(self, val: bool):
        ...

    @property
    def NamespaceHandling(self) -> int:
        ...
    @NamespaceHandling.setter
    def NamespaceHandling(self, val: int):
        ...

    @property
    def WriteEndDocumentOnClose(self) -> bool:
        ...
    @WriteEndDocumentOnClose.setter
    def WriteEndDocumentOnClose(self, val: bool):
        ...

    @property
    def OutputMethod(self) -> int:
        ...
    @OutputMethod.setter
    def OutputMethod(self, val: int):
        ...

    @property
    def CDataSectionElements(self) -> System.Collections.Generic.List[System.Xml.XmlQualifiedName]:
        ...

    @property
    def DoNotEscapeUriAttributes(self) -> bool:
        ...
    @DoNotEscapeUriAttributes.setter
    def DoNotEscapeUriAttributes(self, val: bool):
        ...

    @property
    def MergeCDataSections(self) -> bool:
        ...
    @MergeCDataSections.setter
    def MergeCDataSections(self, val: bool):
        ...

    @property
    def MediaType(self) -> str:
        ...
    @MediaType.setter
    def MediaType(self, val: str):
        ...

    @property
    def DocTypeSystem(self) -> str:
        ...
    @DocTypeSystem.setter
    def DocTypeSystem(self, val: str):
        ...

    @property
    def DocTypePublic(self) -> str:
        ...
    @DocTypePublic.setter
    def DocTypePublic(self, val: str):
        ...

    @property
    def Standalone(self) -> int:
        ...
    @Standalone.setter
    def Standalone(self, val: int):
        ...

    @property
    def AutoXmlDeclaration(self) -> bool:
        ...
    @AutoXmlDeclaration.setter
    def AutoXmlDeclaration(self, val: bool):
        ...

    @property
    def IndentInternal(self) -> int:
        ...
    @IndentInternal.setter
    def IndentInternal(self, val: int):
        ...

    @property
    def IsQuerySpecific(self) -> bool:
        ...

    @property
    def ReadOnly(self) -> bool:
        ...
    @ReadOnly.setter
    def ReadOnly(self, val: bool):
        ...

    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def __init__(self, reader: System.Xml.Xsl.Runtime.XmlQueryDataReader, ):
        ...

    def Reset(self, ) -> None:
        ...

    def Clone(self, ) -> System.Xml.XmlWriterSettings:
        ...

    @typing.overload
    def CreateWriter(self, outputFileName: str, ) -> System.Xml.XmlWriter:
        ...

    @typing.overload
    def CreateWriter(self, output: System.IO.Stream, ) -> System.Xml.XmlWriter:
        ...

    @typing.overload
    def CreateWriter(self, output: System.IO.TextWriter, ) -> System.Xml.XmlWriter:
        ...

    @typing.overload
    def CreateWriter(self, output: System.Xml.XmlWriter, ) -> System.Xml.XmlWriter:
        ...

    def CheckReadOnly(self, propertyName: str, ) -> None:
        ...

    def Initialize(self, ) -> None:
        ...

    def AddConformanceWrapper(self, baseWriter: System.Xml.XmlWriter, ) -> System.Xml.XmlWriter:
        ...

    def GetObjectData(self, writer: System.Xml.Xsl.Runtime.XmlQueryDataWriter, ) -> None:
        ...

class NamespaceHandling(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    Default: int = ...
    OmitDuplicates: int = ...

class XmlOutputMethod(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    Xml: int = ...
    Html: int = ...
    Text: int = ...
    AutoDetect: int = ...

class XmlTextWriter(System.IDisposable, System.IAsyncDisposable, System.Xml.XmlWriter):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def BaseStream(self) -> System.IO.Stream:
        ...

    @property
    def Namespaces(self) -> bool:
        ...
    @Namespaces.setter
    def Namespaces(self, val: bool):
        ...

    @property
    def Formatting(self) -> int:
        ...
    @Formatting.setter
    def Formatting(self, val: int):
        ...

    @property
    def Indentation(self) -> int:
        ...
    @Indentation.setter
    def Indentation(self, val: int):
        ...

    @property
    def IndentChar(self) -> str:
        ...
    @IndentChar.setter
    def IndentChar(self, val: str):
        ...

    @property
    def QuoteChar(self) -> str:
        ...
    @QuoteChar.setter
    def QuoteChar(self, val: str):
        ...

    @property
    def WriteState(self) -> int:
        ...

    @property
    def XmlSpace(self) -> int:
        ...

    @property
    def XmlLang(self) -> str:
        ...

    @property
    def Settings(self) -> System.Xml.XmlWriterSettings:
        ...

    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def __init__(self, w: System.IO.Stream, encoding: System.Text.Encoding, ):
        ...

    @typing.overload
    def __init__(self, filename: str, encoding: System.Text.Encoding, ):
        ...

    @typing.overload
    def __init__(self, w: System.IO.TextWriter, ):
        ...

    @staticmethod
    def CreateDefaultIndentChars() -> System.Array[str]:
        ...

    @typing.overload
    def WriteStartDocument(self, ) -> None:
        ...

    @typing.overload
    def WriteStartDocument(self, standalone: bool, ) -> None:
        ...

    def WriteEndDocument(self, ) -> None:
        ...

    def WriteDocType(self, name: str, pubid: str, sysid: str, subset: str, ) -> None:
        ...

    def WriteStartElement(self, prefix: str, localName: str, ns: str, ) -> None:
        ...

    def WriteEndElement(self, ) -> None:
        ...

    def WriteFullEndElement(self, ) -> None:
        ...

    def WriteStartAttribute(self, prefix: str, localName: str, ns: str, ) -> None:
        ...

    def WriteEndAttribute(self, ) -> None:
        ...

    def WriteCData(self, text: str, ) -> None:
        ...

    def WriteComment(self, text: str, ) -> None:
        ...

    def WriteProcessingInstruction(self, name: str, text: str, ) -> None:
        ...

    def WriteEntityRef(self, name: str, ) -> None:
        ...

    def WriteCharEntity(self, ch: str, ) -> None:
        ...

    def WriteWhitespace(self, ws: str, ) -> None:
        ...

    def WriteString(self, text: str, ) -> None:
        ...

    def WriteSurrogateCharEntity(self, lowChar: str, highChar: str, ) -> None:
        ...

    def WriteChars(self, buffer: System.Array[str], index: int, count: int, ) -> None:
        ...

    @typing.overload
    def WriteRaw(self, buffer: System.Array[str], index: int, count: int, ) -> None:
        ...

    @typing.overload
    def WriteRaw(self, data: str, ) -> None:
        ...

    def WriteBase64(self, buffer: System.Array[int], index: int, count: int, ) -> None:
        ...

    def WriteBinHex(self, buffer: System.Array[int], index: int, count: int, ) -> None:
        ...

    def Close(self, ) -> None:
        ...

    def Flush(self, ) -> None:
        ...

    def WriteName(self, name: str, ) -> None:
        ...

    def WriteQualifiedName(self, localName: str, ns: str, ) -> None:
        ...

    def LookupPrefix(self, ns: str, ) -> str:
        ...

    def WriteNmToken(self, name: str, ) -> None:
        ...

    def StartDocument(self, standalone: int, ) -> None:
        ...

    def AutoComplete(self, token: int, ) -> None:
        ...

    def AutoCompleteAll(self, ) -> None:
        ...

    def InternalWriteEndElement(self, longFormat: bool, ) -> None:
        ...

    def WriteEndStartTag(self, empty: bool, ) -> None:
        ...

    def WriteEndAttributeQuote(self, ) -> None:
        ...

    def Indent(self, beforeEndElement: bool, ) -> None:
        ...

    def PushNamespace(self, prefix: str, ns: str, declared: bool, ) -> None:
        ...

    def AddNamespace(self, prefix: str, ns: str, declared: bool, ) -> None:
        ...

    def AddToNamespaceHashtable(self, namespaceIndex: int, ) -> None:
        ...

    def PopNamespaces(self, indexFrom: int, indexTo: int, ) -> None:
        ...

    def GeneratePrefix(self, ) -> str:
        ...

    def InternalWriteProcessingInstruction(self, name: str, text: str, ) -> None:
        ...

    def LookupNamespace(self, prefix: str, ) -> int:
        ...

    def LookupNamespaceInCurrentScope(self, prefix: str, ) -> int:
        ...

    def FindPrefix(self, ns: str, ) -> str:
        ...

    def InternalWriteName(self, name: str, isNCName: bool, ) -> None:
        ...

    def ValidateName(self, name: str, isNCName: bool, ) -> None:
        ...

    def HandleSpecialAttribute(self, ) -> None:
        ...

    def VerifyPrefixXml(self, prefix: str, ns: str, ) -> None:
        ...

    def PushStack(self, ) -> None:
        ...

    def FlushEncoders(self, ) -> None:
        ...

class Formatting(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    None_: int = ...
    Indented: int = ...

class ReadState(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    Initial: int = ...
    Interactive: int = ...
    Error: int = ...
    EndOfFile: int = ...
    Closed: int = ...

class XmlSpace(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    None_: int = ...
    Default: int = ...
    Preserve: int = ...

class XmlTokenizedType(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    CDATA: int = ...
    ID: int = ...
    IDREF: int = ...
    IDREFS: int = ...
    ENTITY: int = ...
    ENTITIES: int = ...
    NMTOKEN: int = ...
    NMTOKENS: int = ...
    NOTATION: int = ...
    ENUMERATION: int = ...
    QName: int = ...
    NCName: int = ...
    None_: int = ...

class XmlParserContext(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

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
    def DocTypeName(self) -> str:
        ...
    @DocTypeName.setter
    def DocTypeName(self, val: str):
        ...

    @property
    def PublicId(self) -> str:
        ...
    @PublicId.setter
    def PublicId(self, val: str):
        ...

    @property
    def SystemId(self) -> str:
        ...
    @SystemId.setter
    def SystemId(self, val: str):
        ...

    @property
    def BaseURI(self) -> str:
        ...
    @BaseURI.setter
    def BaseURI(self, val: str):
        ...

    @property
    def InternalSubset(self) -> str:
        ...
    @InternalSubset.setter
    def InternalSubset(self, val: str):
        ...

    @property
    def XmlLang(self) -> str:
        ...
    @XmlLang.setter
    def XmlLang(self, val: str):
        ...

    @property
    def XmlSpace(self) -> int:
        ...
    @XmlSpace.setter
    def XmlSpace(self, val: int):
        ...

    @property
    def Encoding(self) -> System.Text.Encoding:
        ...
    @Encoding.setter
    def Encoding(self, val: System.Text.Encoding):
        ...

    @property
    def HasDtdInfo(self) -> bool:
        ...

    # methods
    @typing.overload
    def __init__(self, nt: System.Xml.XmlNameTable, nsMgr: System.Xml.XmlNamespaceManager, xmlLang: str, xmlSpace: int, ):
        ...

    @typing.overload
    def __init__(self, nt: System.Xml.XmlNameTable, nsMgr: System.Xml.XmlNamespaceManager, xmlLang: str, xmlSpace: int, enc: System.Text.Encoding, ):
        ...

    @typing.overload
    def __init__(self, nt: System.Xml.XmlNameTable, nsMgr: System.Xml.XmlNamespaceManager, docTypeName: str, pubId: str, sysId: str, internalSubset: str, baseURI: str, xmlLang: str, xmlSpace: int, ):
        ...

    @typing.overload
    def __init__(self, nt: System.Xml.XmlNameTable, nsMgr: System.Xml.XmlNamespaceManager, docTypeName: str, pubId: str, sysId: str, internalSubset: str, baseURI: str, xmlLang: str, xmlSpace: int, enc: System.Text.Encoding, ):
        ...

class XmlNamespaceManager(System.Xml.IXmlNamespaceResolver, System.Collections.IEnumerable, System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def NameTable(self) -> System.Xml.XmlNameTable:
        ...

    @property
    def DefaultNamespace(self) -> str:
        ...

    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def __init__(self, nameTable: System.Xml.XmlNameTable, ):
        ...

    def PushScope(self, ) -> None:
        ...

    def PopScope(self, ) -> bool:
        ...

    def AddNamespace(self, prefix: str, uri: str, ) -> None:
        ...

    def RemoveNamespace(self, prefix: str, uri: str, ) -> None:
        ...

    def GetEnumerator(self, ) -> System.Collections.IEnumerator:
        ...

    def GetNamespacesInScope(self, scope: int, ) -> System.Collections.Generic.IDictionary[str, str]:
        ...

    def LookupNamespace(self, prefix: str, ) -> str:
        ...

    def LookupNamespaceDecl(self, prefix: str, ) -> int:
        ...

    def LookupPrefix(self, uri: str, ) -> str:
        ...

    def HasNamespace(self, prefix: str, ) -> bool:
        ...

    def GetNamespaceDeclaration(self, idx: int, prefix: ref[str], uri: ref[str], ) -> bool:
        ...

class NewLineHandling(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    Replace: int = ...
    Entitize: int = ...
    None_: int = ...

class XmlNameTable(System.Object, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    def __init__(self, ):
        ...

    @abc.abstractmethod
    @typing.overload
    def Get(self, array: System.Array[str], offset: int, length: int, ) -> str:
        ...

    @abc.abstractmethod
    @typing.overload
    def Get(self, array: str, ) -> str:
        ...

    @abc.abstractmethod
    @typing.overload
    def Add(self, array: System.Array[str], offset: int, length: int, ) -> str:
        ...

    @abc.abstractmethod
    @typing.overload
    def Add(self, array: str, ) -> str:
        ...

class XmlDocumentFragment(System.ICloneable, System.Collections.IEnumerable, System.Xml.XPath.IXPathNavigable, System.Xml.XmlNode):
    @typing.overload
    def __init__(self, **kwargs):
        self.parentNode: System.Xml.XmlNode
        ...

    # static fields

    # properties
    @property
    def Name(self) -> str:
        ...

    @property
    def LocalName(self) -> str:
        ...

    @property
    def NodeType(self) -> int:
        ...

    @property
    def ParentNode(self) -> System.Xml.XmlNode:
        ...

    @property
    def OwnerDocument(self) -> System.Xml.XmlDocument:
        ...

    @property
    def InnerXml(self) -> str:
        ...
    @InnerXml.setter
    def InnerXml(self, val: str):
        ...

    @property
    def IsContainer(self) -> bool:
        ...

    @property
    def LastNode(self) -> System.Xml.XmlLinkedNode:
        ...
    @LastNode.setter
    def LastNode(self, val: System.Xml.XmlLinkedNode):
        ...

    @property
    def XPNodeType(self) -> int:
        ...

    @property
    def Value(self) -> str:
        ...
    @Value.setter
    def Value(self, val: str):
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
    def HasChildNodes(self) -> bool:
        ...

    @property
    def NamespaceURI(self) -> str:
        ...

    @property
    def Prefix(self) -> str:
        ...
    @Prefix.setter
    def Prefix(self, val: str):
        ...

    @property
    def IsReadOnly(self) -> bool:
        ...

    @property
    def InnerText(self) -> str:
        ...
    @InnerText.setter
    def InnerText(self, val: str):
        ...

    @property
    def OuterXml(self) -> str:
        ...

    @property
    def SchemaInfo(self) -> System.Xml.Schema.IXmlSchemaInfo:
        ...

    @property
    def BaseURI(self) -> str:
        ...

    @property
    def Document(self) -> System.Xml.XmlDocument:
        ...

    @property
    def Item(self) -> System.Xml.XmlElement:
        ...

    @property
    def Item(self) -> System.Xml.XmlElement:
        ...

    @property
    def XmlSpace(self) -> int:
        ...

    @property
    def XmlLang(self) -> str:
        ...

    @property
    def XPLocalName(self) -> str:
        ...

    @property
    def IsText(self) -> bool:
        ...

    @property
    def PreviousText(self) -> System.Xml.XmlNode:
        ...

    # methods
    def __init__(self, ownerDocument: System.Xml.XmlDocument, ):
        ...

    def CloneNode(self, deep: bool, ) -> System.Xml.XmlNode:
        ...

    def IsValidChildType(self, type: int, ) -> bool:
        ...

    def CanInsertAfter(self, newChild: System.Xml.XmlNode, refChild: System.Xml.XmlNode, ) -> bool:
        ...

    def CanInsertBefore(self, newChild: System.Xml.XmlNode, refChild: System.Xml.XmlNode, ) -> bool:
        ...

    def WriteTo(self, w: System.Xml.XmlWriter, ) -> None:
        ...

    def WriteContentTo(self, w: System.Xml.XmlWriter, ) -> None:
        ...

class XmlNodeChangedEventArgs(System.EventArgs):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def Action(self) -> int:
        ...

    @property
    def Node(self) -> System.Xml.XmlNode:
        ...

    @property
    def OldParent(self) -> System.Xml.XmlNode:
        ...

    @property
    def NewParent(self) -> System.Xml.XmlNode:
        ...

    @property
    def OldValue(self) -> str:
        ...

    @property
    def NewValue(self) -> str:
        ...

    # methods
    def __init__(self, node: System.Xml.XmlNode, oldParent: System.Xml.XmlNode, newParent: System.Xml.XmlNode, oldValue: str, newValue: str, action: int, ):
        ...

class ValidationType(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    None_: int = ...
    Auto: int = ...
    DTD: int = ...
    XDR: int = ...
    Schema: int = ...

class XmlTextReader(System.IDisposable, System.Xml.IXmlLineInfo, System.Xml.IXmlNamespaceResolver, System.Xml.XmlReader):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def NodeType(self) -> int:
        ...

    @property
    def Name(self) -> str:
        ...

    @property
    def LocalName(self) -> str:
        ...

    @property
    def NamespaceURI(self) -> str:
        ...

    @property
    def Prefix(self) -> str:
        ...

    @property
    def HasValue(self) -> bool:
        ...

    @property
    def Value(self) -> str:
        ...

    @property
    def Depth(self) -> int:
        ...

    @property
    def BaseURI(self) -> str:
        ...

    @property
    def IsEmptyElement(self) -> bool:
        ...

    @property
    def IsDefault(self) -> bool:
        ...

    @property
    def QuoteChar(self) -> str:
        ...

    @property
    def XmlSpace(self) -> int:
        ...

    @property
    def XmlLang(self) -> str:
        ...

    @property
    def AttributeCount(self) -> int:
        ...

    @property
    def EOF(self) -> bool:
        ...

    @property
    def ReadState(self) -> int:
        ...

    @property
    def NameTable(self) -> System.Xml.XmlNameTable:
        ...

    @property
    def CanResolveEntity(self) -> bool:
        ...

    @property
    def CanReadBinaryContent(self) -> bool:
        ...

    @property
    def CanReadValueChunk(self) -> bool:
        ...

    @property
    def LineNumber(self) -> int:
        ...

    @property
    def LinePosition(self) -> int:
        ...

    @property
    def Namespaces(self) -> bool:
        ...
    @Namespaces.setter
    def Namespaces(self, val: bool):
        ...

    @property
    def Normalization(self) -> bool:
        ...
    @Normalization.setter
    def Normalization(self, val: bool):
        ...

    @property
    def Encoding(self) -> System.Text.Encoding:
        ...

    @property
    def WhitespaceHandling(self) -> int:
        ...
    @WhitespaceHandling.setter
    def WhitespaceHandling(self, val: int):
        ...

    @property
    def ProhibitDtd(self) -> bool:
        ...
    @ProhibitDtd.setter
    def ProhibitDtd(self, val: bool):
        ...

    @property
    def DtdProcessing(self) -> int:
        ...
    @DtdProcessing.setter
    def DtdProcessing(self, val: int):
        ...

    @property
    def EntityHandling(self) -> int:
        ...
    @EntityHandling.setter
    def EntityHandling(self, val: int):
        ...

    XmlResolver: System.Xml.XmlResolver = property(None, lambda val: ...)

    @property
    def Impl(self) -> System.Xml.XmlTextReaderImpl:
        ...

    @property
    def NamespaceManager(self) -> System.Xml.XmlNamespaceManager:
        ...

    XmlValidatingReaderCompatibilityMode: bool = property(None, lambda val: ...)

    @property
    def DtdInfo(self) -> System.Xml.IDtdInfo:
        ...

    @property
    def Settings(self) -> System.Xml.XmlReaderSettings:
        ...

    @property
    def SchemaInfo(self) -> System.Xml.Schema.IXmlSchemaInfo:
        ...

    @property
    def ValueType(self) -> System.Type:
        ...

    @property
    def Item(self) -> str:
        ...

    @property
    def Item(self) -> str:
        ...

    @property
    def Item(self) -> str:
        ...

    @property
    def HasAttributes(self) -> bool:
        ...

    @property
    def IsDefaultInternal(self) -> bool:
        ...

    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def __init__(self, nt: System.Xml.XmlNameTable, ):
        ...

    @typing.overload
    def __init__(self, input: System.IO.Stream, ):
        ...

    @typing.overload
    def __init__(self, url: str, input: System.IO.Stream, ):
        ...

    @typing.overload
    def __init__(self, input: System.IO.Stream, nt: System.Xml.XmlNameTable, ):
        ...

    @typing.overload
    def __init__(self, url: str, input: System.IO.Stream, nt: System.Xml.XmlNameTable, ):
        ...

    @typing.overload
    def __init__(self, input: System.IO.TextReader, ):
        ...

    @typing.overload
    def __init__(self, url: str, input: System.IO.TextReader, ):
        ...

    @typing.overload
    def __init__(self, input: System.IO.TextReader, nt: System.Xml.XmlNameTable, ):
        ...

    @typing.overload
    def __init__(self, url: str, input: System.IO.TextReader, nt: System.Xml.XmlNameTable, ):
        ...

    @typing.overload
    def __init__(self, xmlFragment: System.IO.Stream, fragType: int, context: System.Xml.XmlParserContext, ):
        ...

    @typing.overload
    def __init__(self, xmlFragment: str, fragType: int, context: System.Xml.XmlParserContext, ):
        ...

    @typing.overload
    def __init__(self, url: str, ):
        ...

    @typing.overload
    def __init__(self, url: str, nt: System.Xml.XmlNameTable, ):
        ...

    @typing.overload
    def GetAttribute(self, name: str, ) -> str:
        ...

    @typing.overload
    def GetAttribute(self, localName: str, namespaceURI: str, ) -> str:
        ...

    @typing.overload
    def GetAttribute(self, i: int, ) -> str:
        ...

    @typing.overload
    def MoveToAttribute(self, name: str, ) -> bool:
        ...

    @typing.overload
    def MoveToAttribute(self, localName: str, namespaceURI: str, ) -> bool:
        ...

    @typing.overload
    def MoveToAttribute(self, i: int, ) -> None:
        ...

    def MoveToFirstAttribute(self, ) -> bool:
        ...

    def MoveToNextAttribute(self, ) -> bool:
        ...

    def MoveToElement(self, ) -> bool:
        ...

    def ReadAttributeValue(self, ) -> bool:
        ...

    def Read(self, ) -> bool:
        ...

    def Close(self, ) -> None:
        ...

    def Skip(self, ) -> None:
        ...

    def LookupNamespace(self, prefix: str, ) -> str:
        ...

    def ResolveEntity(self, ) -> None:
        ...

    def ReadContentAsBase64(self, buffer: System.Array[int], index: int, count: int, ) -> int:
        ...

    def ReadElementContentAsBase64(self, buffer: System.Array[int], index: int, count: int, ) -> int:
        ...

    def ReadContentAsBinHex(self, buffer: System.Array[int], index: int, count: int, ) -> int:
        ...

    def ReadElementContentAsBinHex(self, buffer: System.Array[int], index: int, count: int, ) -> int:
        ...

    def ReadString(self, ) -> str:
        ...

    def HasLineInfo(self, ) -> bool:
        ...

    def GetNamespacesInScope(self, scope: int, ) -> System.Collections.Generic.IDictionary[str, str]:
        ...

    def LookupNamespace(self, prefix: str, ) -> str:
        ...

    def LookupPrefix(self, namespaceName: str, ) -> str:
        ...

    def GetNamespacesInScope(self, scope: int, ) -> System.Collections.Generic.IDictionary[str, str]:
        ...

    def ResetState(self, ) -> None:
        ...

    def GetRemainder(self, ) -> System.IO.TextReader:
        ...

    def ReadChars(self, buffer: System.Array[str], index: int, count: int, ) -> int:
        ...

    def ReadBase64(self, array: System.Array[int], offset: int, len: int, ) -> int:
        ...

    def ReadBinHex(self, array: System.Array[int], offset: int, len: int, ) -> int:
        ...

class EntityHandling(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    ExpandEntities: int = ...
    ExpandCharEntities: int = ...

class WhitespaceHandling(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    All: int = ...
    Significant: int = ...
    None_: int = ...

class XmlNode(System.ICloneable, System.Collections.IEnumerable, System.Xml.XPath.IXPathNavigable, System.Object, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        self.parentNode: System.Xml.XmlNode
        ...

    # static fields

    # properties
    @property
    @abc.abstractmethod
    def Name(self) -> str:
        ...

    @property
    def Value(self) -> str:
        ...
    @Value.setter
    def Value(self, val: str):
        ...

    @property
    @abc.abstractmethod
    def NodeType(self) -> int:
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
    def IsContainer(self) -> bool:
        ...

    @property
    def LastNode(self) -> System.Xml.XmlLinkedNode:
        ...
    @LastNode.setter
    def LastNode(self, val: System.Xml.XmlLinkedNode):
        ...

    @property
    def HasChildNodes(self) -> bool:
        ...

    @property
    def NamespaceURI(self) -> str:
        ...

    @property
    def Prefix(self) -> str:
        ...
    @Prefix.setter
    def Prefix(self, val: str):
        ...

    @property
    @abc.abstractmethod
    def LocalName(self) -> str:
        ...

    @property
    def IsReadOnly(self) -> bool:
        ...

    @property
    def InnerText(self) -> str:
        ...
    @InnerText.setter
    def InnerText(self, val: str):
        ...

    @property
    def OuterXml(self) -> str:
        ...

    @property
    def InnerXml(self) -> str:
        ...
    @InnerXml.setter
    def InnerXml(self, val: str):
        ...

    @property
    def SchemaInfo(self) -> System.Xml.Schema.IXmlSchemaInfo:
        ...

    @property
    def BaseURI(self) -> str:
        ...

    @property
    def Document(self) -> System.Xml.XmlDocument:
        ...

    @property
    def Item(self) -> System.Xml.XmlElement:
        ...

    @property
    def Item(self) -> System.Xml.XmlElement:
        ...

    @property
    def XmlSpace(self) -> int:
        ...

    @property
    def XmlLang(self) -> str:
        ...

    @property
    def XPNodeType(self) -> int:
        ...

    @property
    def XPLocalName(self) -> str:
        ...

    @property
    def IsText(self) -> bool:
        ...

    @property
    def PreviousText(self) -> System.Xml.XmlNode:
        ...

    @property
    def debuggerDisplayProxy(self) -> System.Object:
        ...

    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def __init__(self, doc: System.Xml.XmlDocument, ):
        ...

    @abc.abstractmethod
    def CloneNode(self, deep: bool, ) -> System.Xml.XmlNode:
        ...

    def IsValidChildType(self, type: int, ) -> bool:
        ...

    def CanInsertAfter(self, newChild: System.Xml.XmlNode, refChild: System.Xml.XmlNode, ) -> bool:
        ...

    def CanInsertBefore(self, newChild: System.Xml.XmlNode, refChild: System.Xml.XmlNode, ) -> bool:
        ...

    @abc.abstractmethod
    def WriteTo(self, w: System.Xml.XmlWriter, ) -> None:
        ...

    @abc.abstractmethod
    def WriteContentTo(self, w: System.Xml.XmlWriter, ) -> None:
        ...

    def CreateNavigator(self, ) -> System.Xml.XPath.XPathNavigator:
        ...

    @typing.overload
    def SelectSingleNode(self, xpath: str, ) -> System.Xml.XmlNode:
        ...

    @typing.overload
    def SelectSingleNode(self, xpath: str, nsmgr: System.Xml.XmlNamespaceManager, ) -> System.Xml.XmlNode:
        ...

    @typing.overload
    def SelectNodes(self, xpath: str, ) -> System.Xml.XmlNodeList:
        ...

    @typing.overload
    def SelectNodes(self, xpath: str, nsmgr: System.Xml.XmlNamespaceManager, ) -> System.Xml.XmlNodeList:
        ...

    def AncestorNode(self, node: System.Xml.XmlNode, ) -> bool:
        ...

    def IsConnected(self, ) -> bool:
        ...

    def InsertBefore(self, newChild: System.Xml.XmlNode, refChild: System.Xml.XmlNode, ) -> System.Xml.XmlNode:
        ...

    def InsertAfter(self, newChild: System.Xml.XmlNode, refChild: System.Xml.XmlNode, ) -> System.Xml.XmlNode:
        ...

    def ReplaceChild(self, newChild: System.Xml.XmlNode, oldChild: System.Xml.XmlNode, ) -> System.Xml.XmlNode:
        ...

    def RemoveChild(self, oldChild: System.Xml.XmlNode, ) -> System.Xml.XmlNode:
        ...

    def PrependChild(self, newChild: System.Xml.XmlNode, ) -> System.Xml.XmlNode:
        ...

    def AppendChild(self, newChild: System.Xml.XmlNode, ) -> System.Xml.XmlNode:
        ...

    def AppendChildForLoad(self, newChild: System.Xml.XmlNode, doc: System.Xml.XmlDocument, ) -> System.Xml.XmlNode:
        ...

    def CopyChildren(self, doc: System.Xml.XmlDocument, container: System.Xml.XmlNode, deep: bool, ) -> None:
        ...

    def Normalize(self, ) -> None:
        ...

    def NormalizeWinner(self, firstNode: System.Xml.XmlNode, secondNode: System.Xml.XmlNode, ) -> System.Xml.XmlNode:
        ...

    def Supports(self, feature: str, version: str, ) -> bool:
        ...

    @staticmethod
    def HasReadOnlyParent(n: System.Xml.XmlNode, ) -> bool:
        ...

    def Clone(self, ) -> System.Xml.XmlNode:
        ...

    def Clone(self, ) -> System.Object:
        ...

    def GetEnumerator(self, ) -> System.Collections.IEnumerator:
        ...

    def GetEnumerator(self, ) -> System.Collections.IEnumerator:
        ...

    def AppendChildText(self, builder: System.Text.StringBuilder, ) -> None:
        ...

    def RemoveAll(self, ) -> None:
        ...

    def GetNamespaceOfPrefix(self, prefix: str, ) -> str:
        ...

    def GetNamespaceOfPrefixStrict(self, prefix: str, ) -> str:
        ...

    def GetPrefixOfNamespace(self, namespaceURI: str, ) -> str:
        ...

    def GetPrefixOfNamespaceStrict(self, namespaceURI: str, ) -> str:
        ...

    def SetParent(self, node: System.Xml.XmlNode, ) -> None:
        ...

    def SetParentForLoad(self, node: System.Xml.XmlNode, ) -> None:
        ...

    @staticmethod
    def SplitName(name: str, prefix: ref[str], localName: ref[str], ) -> None:
        ...

    def FindChild(self, type: int, ) -> System.Xml.XmlNode:
        ...

    def GetEventArgs(self, node: System.Xml.XmlNode, oldParent: System.Xml.XmlNode, newParent: System.Xml.XmlNode, oldValue: str, newValue: str, action: int, ) -> System.Xml.XmlNodeChangedEventArgs:
        ...

    def BeforeEvent(self, args: System.Xml.XmlNodeChangedEventArgs, ) -> None:
        ...

    def AfterEvent(self, args: System.Xml.XmlNodeChangedEventArgs, ) -> None:
        ...

    def GetXPAttribute(self, localName: str, namespaceURI: str, ) -> str:
        ...

    @staticmethod
    def NestTextNodes(prevNode: System.Xml.XmlNode, nextNode: System.Xml.XmlNode, ) -> None:
        ...

    @staticmethod
    def UnnestTextNodes(prevNode: System.Xml.XmlNode, nextNode: System.Xml.XmlNode, ) -> None:
        ...

class XmlNodeOrder(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    Before: int = ...
    After: int = ...
    Same: int = ...
    Unknown: int = ...

class XmlProcessingInstruction(System.ICloneable, System.Collections.IEnumerable, System.Xml.XPath.IXPathNavigable, System.Xml.XmlLinkedNode):
    @typing.overload
    def __init__(self, **kwargs):
        self.next: System.Xml.XmlLinkedNode
        self.parentNode: System.Xml.XmlNode
        ...

    # static fields

    # properties
    @property
    def Name(self) -> str:
        ...

    @property
    def LocalName(self) -> str:
        ...

    @property
    def Value(self) -> str:
        ...
    @Value.setter
    def Value(self, val: str):
        ...

    @property
    def Target(self) -> str:
        ...

    @property
    def Data(self) -> str:
        ...
    @Data.setter
    def Data(self, val: str):
        ...

    @property
    def InnerText(self) -> str:
        ...
    @InnerText.setter
    def InnerText(self, val: str):
        ...

    @property
    def NodeType(self) -> int:
        ...

    @property
    def XPLocalName(self) -> str:
        ...

    @property
    def XPNodeType(self) -> int:
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
    def IsContainer(self) -> bool:
        ...

    @property
    def LastNode(self) -> System.Xml.XmlLinkedNode:
        ...
    @LastNode.setter
    def LastNode(self, val: System.Xml.XmlLinkedNode):
        ...

    @property
    def HasChildNodes(self) -> bool:
        ...

    @property
    def NamespaceURI(self) -> str:
        ...

    @property
    def Prefix(self) -> str:
        ...
    @Prefix.setter
    def Prefix(self, val: str):
        ...

    @property
    def IsReadOnly(self) -> bool:
        ...

    @property
    def OuterXml(self) -> str:
        ...

    @property
    def InnerXml(self) -> str:
        ...
    @InnerXml.setter
    def InnerXml(self, val: str):
        ...

    @property
    def SchemaInfo(self) -> System.Xml.Schema.IXmlSchemaInfo:
        ...

    @property
    def BaseURI(self) -> str:
        ...

    @property
    def Document(self) -> System.Xml.XmlDocument:
        ...

    @property
    def Item(self) -> System.Xml.XmlElement:
        ...

    @property
    def Item(self) -> System.Xml.XmlElement:
        ...

    @property
    def XmlSpace(self) -> int:
        ...

    @property
    def XmlLang(self) -> str:
        ...

    @property
    def IsText(self) -> bool:
        ...

    @property
    def PreviousText(self) -> System.Xml.XmlNode:
        ...

    # methods
    def __init__(self, target: str, data: str, doc: System.Xml.XmlDocument, ):
        ...

    def CloneNode(self, deep: bool, ) -> System.Xml.XmlNode:
        ...

    def WriteTo(self, w: System.Xml.XmlWriter, ) -> None:
        ...

    def WriteContentTo(self, w: System.Xml.XmlWriter, ) -> None:
        ...

class XmlDeclaration(System.ICloneable, System.Collections.IEnumerable, System.Xml.XPath.IXPathNavigable, System.Xml.XmlLinkedNode):
    @typing.overload
    def __init__(self, **kwargs):
        self.next: System.Xml.XmlLinkedNode
        self.parentNode: System.Xml.XmlNode
        ...

    # static fields

    # properties
    @property
    def Version(self) -> str:
        ...
    @Version.setter
    def Version(self, val: str):
        ...

    @property
    def Encoding(self) -> str:
        ...
    @Encoding.setter
    def Encoding(self, val: str):
        ...

    @property
    def Standalone(self) -> str:
        ...
    @Standalone.setter
    def Standalone(self, val: str):
        ...

    @property
    def Value(self) -> str:
        ...
    @Value.setter
    def Value(self, val: str):
        ...

    @property
    def InnerText(self) -> str:
        ...
    @InnerText.setter
    def InnerText(self, val: str):
        ...

    @property
    def Name(self) -> str:
        ...

    @property
    def LocalName(self) -> str:
        ...

    @property
    def NodeType(self) -> int:
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
    def IsContainer(self) -> bool:
        ...

    @property
    def LastNode(self) -> System.Xml.XmlLinkedNode:
        ...
    @LastNode.setter
    def LastNode(self, val: System.Xml.XmlLinkedNode):
        ...

    @property
    def HasChildNodes(self) -> bool:
        ...

    @property
    def NamespaceURI(self) -> str:
        ...

    @property
    def Prefix(self) -> str:
        ...
    @Prefix.setter
    def Prefix(self, val: str):
        ...

    @property
    def IsReadOnly(self) -> bool:
        ...

    @property
    def OuterXml(self) -> str:
        ...

    @property
    def InnerXml(self) -> str:
        ...
    @InnerXml.setter
    def InnerXml(self, val: str):
        ...

    @property
    def SchemaInfo(self) -> System.Xml.Schema.IXmlSchemaInfo:
        ...

    @property
    def BaseURI(self) -> str:
        ...

    @property
    def Document(self) -> System.Xml.XmlDocument:
        ...

    @property
    def Item(self) -> System.Xml.XmlElement:
        ...

    @property
    def Item(self) -> System.Xml.XmlElement:
        ...

    @property
    def XmlSpace(self) -> int:
        ...

    @property
    def XmlLang(self) -> str:
        ...

    @property
    def XPNodeType(self) -> int:
        ...

    @property
    def XPLocalName(self) -> str:
        ...

    @property
    def IsText(self) -> bool:
        ...

    @property
    def PreviousText(self) -> System.Xml.XmlNode:
        ...

    # methods
    def __init__(self, version: str, encoding: str, standalone: str, doc: System.Xml.XmlDocument, ):
        ...

    def CloneNode(self, deep: bool, ) -> System.Xml.XmlNode:
        ...

    def WriteTo(self, w: System.Xml.XmlWriter, ) -> None:
        ...

    def WriteContentTo(self, w: System.Xml.XmlWriter, ) -> None:
        ...

    def IsValidXmlVersion(self, ver: str, ) -> bool:
        ...

class XmlWhitespace(System.ICloneable, System.Collections.IEnumerable, System.Xml.XPath.IXPathNavigable, System.Xml.XmlCharacterData):
    @typing.overload
    def __init__(self, **kwargs):
        self.next: System.Xml.XmlLinkedNode
        self.parentNode: System.Xml.XmlNode
        ...

    # static fields

    # properties
    @property
    def Name(self) -> str:
        ...

    @property
    def LocalName(self) -> str:
        ...

    @property
    def NodeType(self) -> int:
        ...

    @property
    def ParentNode(self) -> System.Xml.XmlNode:
        ...

    @property
    def Value(self) -> str:
        ...
    @Value.setter
    def Value(self, val: str):
        ...

    @property
    def XPNodeType(self) -> int:
        ...

    @property
    def IsText(self) -> bool:
        ...

    @property
    def PreviousText(self) -> System.Xml.XmlNode:
        ...

    @property
    def InnerText(self) -> str:
        ...
    @InnerText.setter
    def InnerText(self, val: str):
        ...

    @property
    def Data(self) -> str:
        ...
    @Data.setter
    def Data(self, val: str):
        ...

    @property
    def Length(self) -> int:
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
    def IsContainer(self) -> bool:
        ...

    @property
    def LastNode(self) -> System.Xml.XmlLinkedNode:
        ...
    @LastNode.setter
    def LastNode(self, val: System.Xml.XmlLinkedNode):
        ...

    @property
    def HasChildNodes(self) -> bool:
        ...

    @property
    def NamespaceURI(self) -> str:
        ...

    @property
    def Prefix(self) -> str:
        ...
    @Prefix.setter
    def Prefix(self, val: str):
        ...

    @property
    def IsReadOnly(self) -> bool:
        ...

    @property
    def OuterXml(self) -> str:
        ...

    @property
    def InnerXml(self) -> str:
        ...
    @InnerXml.setter
    def InnerXml(self, val: str):
        ...

    @property
    def SchemaInfo(self) -> System.Xml.Schema.IXmlSchemaInfo:
        ...

    @property
    def BaseURI(self) -> str:
        ...

    @property
    def Document(self) -> System.Xml.XmlDocument:
        ...

    @property
    def Item(self) -> System.Xml.XmlElement:
        ...

    @property
    def Item(self) -> System.Xml.XmlElement:
        ...

    @property
    def XmlSpace(self) -> int:
        ...

    @property
    def XmlLang(self) -> str:
        ...

    @property
    def XPLocalName(self) -> str:
        ...

    # methods
    def __init__(self, strData: str, doc: System.Xml.XmlDocument, ):
        ...

    def CloneNode(self, deep: bool, ) -> System.Xml.XmlNode:
        ...

    def WriteTo(self, w: System.Xml.XmlWriter, ) -> None:
        ...

    def WriteContentTo(self, w: System.Xml.XmlWriter, ) -> None:
        ...

