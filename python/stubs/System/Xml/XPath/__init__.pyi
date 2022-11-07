from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import System.Xml.XPath
import System
import System.Xml
import System.Xml.Schema
import System.Collections
import System.Collections.Generic


class IXPathNavigable(abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    @abc.abstractmethod
    def CreateNavigator(self, ) -> System.Xml.XPath.XPathNavigator:
        ...

class XPathNodeType(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    Root: int = ...
    Element: int = ...
    Attribute: int = ...
    Namespace: int = ...
    Text: int = ...
    SignificantWhitespace: int = ...
    Whitespace: int = ...
    ProcessingInstruction: int = ...
    Comment: int = ...
    All: int = ...

class XPathNavigator(System.ICloneable, System.Xml.XPath.IXPathNavigable, System.Xml.IXmlNamespaceResolver, System.Xml.XPath.XPathItem, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields
    comparer: System.Xml.XPath.XPathNavigatorKeyComparer = ...
    NodeTypeLetter: System.Array[str] = ...
    UniqueIdTbl: System.Array[str] = ...
    ContentKindMasks: System.Array[int] = ...

    # properties
    @property
    def IsNode(self) -> bool:
        ...

    @property
    def XmlType(self) -> System.Xml.Schema.XmlSchemaType:
        ...

    @property
    def TypedValue(self) -> System.Object:
        ...

    @property
    def ValueType(self) -> System.Type:
        ...

    @property
    def ValueAsBoolean(self) -> bool:
        ...

    @property
    def ValueAsDateTime(self) -> System.DateTime:
        ...

    @property
    def ValueAsDouble(self) -> float:
        ...

    @property
    def ValueAsInt(self) -> int:
        ...

    @property
    def ValueAsLong(self) -> int:
        ...

    @property
    @abc.abstractmethod
    def NameTable(self) -> System.Xml.XmlNameTable:
        ...

    @property
    def NavigatorComparer(self) -> System.Collections.IEqualityComparer:
        ...

    @property
    @abc.abstractmethod
    def NodeType(self) -> int:
        ...

    @property
    @abc.abstractmethod
    def LocalName(self) -> str:
        ...

    @property
    @abc.abstractmethod
    def Name(self) -> str:
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
    @abc.abstractmethod
    def BaseURI(self) -> str:
        ...

    @property
    @abc.abstractmethod
    def IsEmptyElement(self) -> bool:
        ...

    @property
    def XmlLang(self) -> str:
        ...

    @property
    def UnderlyingObject(self) -> System.Object:
        ...

    @property
    def HasAttributes(self) -> bool:
        ...

    @property
    def HasChildren(self) -> bool:
        ...

    @property
    def SchemaInfo(self) -> System.Xml.Schema.IXmlSchemaInfo:
        ...

    @property
    def CanEdit(self) -> bool:
        ...

    @property
    def OuterXml(self) -> str:
        ...
    @OuterXml.setter
    def OuterXml(self, val: str):
        ...

    @property
    def InnerXml(self) -> str:
        ...
    @InnerXml.setter
    def InnerXml(self, val: str):
        ...

    @property
    def IndexInParent(self) -> int:
        ...

    @property
    def UniqueId(self) -> str:
        ...

    @property
    def debuggerDisplayProxy(self) -> System.Object:
        ...

    @property
    @abc.abstractmethod
    def Value(self) -> str:
        ...

    # methods
    def __init__(self, ):
        ...

    @staticmethod
    def CompileMatchPattern(xpath: str, ) -> System.Xml.XPath.XPathExpression:
        ...

    @staticmethod
    def GetDepth(nav: System.Xml.XPath.XPathNavigator, ) -> int:
        ...

    def CompareSiblings(self, n1: System.Xml.XPath.XPathNavigator, n2: System.Xml.XPath.XPathNavigator, ) -> int:
        ...

    @staticmethod
    def GetNamespaces(resolver: System.Xml.IXmlNamespaceResolver, ) -> System.Xml.XmlNamespaceManager:
        ...

    @staticmethod
    def GetContentKindMask(type: int, ) -> int:
        ...

    @staticmethod
    def GetKindMask(type: int, ) -> int:
        ...

    @staticmethod
    def IsText(type: int, ) -> bool:
        ...

    def IsValidChildType(self, type: int, ) -> bool:
        ...

    def IsValidSiblingType(self, type: int, ) -> bool:
        ...

    def CreateReader(self, ) -> System.Xml.XmlReader:
        ...

    def CreateContextReader(self, xml: str, fromCurrentNode: bool, ) -> System.Xml.XmlReader:
        ...

    def BuildSubtree(self, reader: System.Xml.XmlReader, writer: System.Xml.XmlWriter, ) -> None:
        ...

    def ToString(self, ) -> str:
        ...

    def SetValue(self, value: str, ) -> None:
        ...

    def SetTypedValue(self, typedValue: System.Object, ) -> None:
        ...

    def ValueAs(self, returnType: System.Type, nsResolver: System.Xml.IXmlNamespaceResolver, ) -> System.Object:
        ...

    def Clone(self, ) -> System.Object:
        ...

    def CreateNavigator(self, ) -> System.Xml.XPath.XPathNavigator:
        ...

    def LookupNamespace(self, prefix: str, ) -> str:
        ...

    def LookupPrefix(self, namespaceURI: str, ) -> str:
        ...

    def GetNamespacesInScope(self, scope: int, ) -> System.Collections.Generic.IDictionary[str, str]:
        ...

    @abc.abstractmethod
    def Clone(self, ) -> System.Xml.XPath.XPathNavigator:
        ...

    def ReadSubtree(self, ) -> System.Xml.XmlReader:
        ...

    def WriteSubtree(self, writer: System.Xml.XmlWriter, ) -> None:
        ...

    def GetAttribute(self, localName: str, namespaceURI: str, ) -> str:
        ...

    def MoveToAttribute(self, localName: str, namespaceURI: str, ) -> bool:
        ...

    @abc.abstractmethod
    def MoveToFirstAttribute(self, ) -> bool:
        ...

    @abc.abstractmethod
    def MoveToNextAttribute(self, ) -> bool:
        ...

    def GetNamespace(self, name: str, ) -> str:
        ...

    def MoveToNamespace(self, name: str, ) -> bool:
        ...

    @abc.abstractmethod
    @typing.overload
    def MoveToFirstNamespace(self, namespaceScope: int, ) -> bool:
        ...

    @typing.overload
    def MoveToFirstNamespace(self, ) -> bool:
        ...

    @abc.abstractmethod
    @typing.overload
    def MoveToNextNamespace(self, namespaceScope: int, ) -> bool:
        ...

    @typing.overload
    def MoveToNextNamespace(self, ) -> bool:
        ...

    @abc.abstractmethod
    @typing.overload
    def MoveToNext(self, ) -> bool:
        ...

    @typing.overload
    def MoveToNext(self, localName: str, namespaceURI: str, ) -> bool:
        ...

    @typing.overload
    def MoveToNext(self, type: int, ) -> bool:
        ...

    @abc.abstractmethod
    @typing.overload
    def MoveToPrevious(self, ) -> bool:
        ...

    @typing.overload
    def MoveToPrevious(self, localName: str, namespaceURI: str, ) -> bool:
        ...

    @typing.overload
    def MoveToPrevious(self, type: int, ) -> bool:
        ...

    def MoveToFirst(self, ) -> bool:
        ...

    @abc.abstractmethod
    def MoveToFirstChild(self, ) -> bool:
        ...

    @abc.abstractmethod
    def MoveToParent(self, ) -> bool:
        ...

    def MoveToRoot(self, ) -> None:
        ...

    @abc.abstractmethod
    def MoveTo(self, other: System.Xml.XPath.XPathNavigator, ) -> bool:
        ...

    @abc.abstractmethod
    def MoveToId(self, id: str, ) -> bool:
        ...

    @typing.overload
    def MoveToChild(self, localName: str, namespaceURI: str, ) -> bool:
        ...

    @typing.overload
    def MoveToChild(self, type: int, ) -> bool:
        ...

    @typing.overload
    def MoveToFollowing(self, localName: str, namespaceURI: str, ) -> bool:
        ...

    @typing.overload
    def MoveToFollowing(self, localName: str, namespaceURI: str, end: System.Xml.XPath.XPathNavigator, ) -> bool:
        ...

    @typing.overload
    def MoveToFollowing(self, type: int, ) -> bool:
        ...

    @typing.overload
    def MoveToFollowing(self, type: int, end: System.Xml.XPath.XPathNavigator, ) -> bool:
        ...

    @abc.abstractmethod
    def IsSamePosition(self, other: System.Xml.XPath.XPathNavigator, ) -> bool:
        ...

    def IsDescendant(self, nav: System.Xml.XPath.XPathNavigator, ) -> bool:
        ...

    def ComparePosition(self, nav: System.Xml.XPath.XPathNavigator, ) -> int:
        ...

    def CheckValidity(self, schemas: System.Xml.Schema.XmlSchemaSet, validationEventHandler: System.Xml.Schema.ValidationEventHandler, ) -> bool:
        ...

    def GetValidatingReader(self, reader: System.Xml.XmlReader, schemas: System.Xml.Schema.XmlSchemaSet, validationEvent: System.Xml.Schema.ValidationEventHandler, schemaType: System.Xml.Schema.XmlSchemaType, schemaElement: System.Xml.Schema.XmlSchemaElement, schemaAttribute: System.Xml.Schema.XmlSchemaAttribute, ) -> System.Xml.XmlReader:
        ...

    def Compile(self, xpath: str, ) -> System.Xml.XPath.XPathExpression:
        ...

    @typing.overload
    def SelectSingleNode(self, xpath: str, ) -> System.Xml.XPath.XPathNavigator:
        ...

    @typing.overload
    def SelectSingleNode(self, xpath: str, resolver: System.Xml.IXmlNamespaceResolver, ) -> System.Xml.XPath.XPathNavigator:
        ...

    @typing.overload
    def SelectSingleNode(self, expression: System.Xml.XPath.XPathExpression, ) -> System.Xml.XPath.XPathNavigator:
        ...

    @typing.overload
    def Select(self, xpath: str, ) -> System.Xml.XPath.XPathNodeIterator:
        ...

    @typing.overload
    def Select(self, xpath: str, resolver: System.Xml.IXmlNamespaceResolver, ) -> System.Xml.XPath.XPathNodeIterator:
        ...

    @typing.overload
    def Select(self, expr: System.Xml.XPath.XPathExpression, ) -> System.Xml.XPath.XPathNodeIterator:
        ...

    @typing.overload
    def Evaluate(self, xpath: str, ) -> System.Object:
        ...

    @typing.overload
    def Evaluate(self, xpath: str, resolver: System.Xml.IXmlNamespaceResolver, ) -> System.Object:
        ...

    @typing.overload
    def Evaluate(self, expr: System.Xml.XPath.XPathExpression, ) -> System.Object:
        ...

    @typing.overload
    def Evaluate(self, expr: System.Xml.XPath.XPathExpression, context: System.Xml.XPath.XPathNodeIterator, ) -> System.Object:
        ...

    @typing.overload
    def Matches(self, expr: System.Xml.XPath.XPathExpression, ) -> bool:
        ...

    @typing.overload
    def Matches(self, xpath: str, ) -> bool:
        ...

    @typing.overload
    def SelectChildren(self, type: int, ) -> System.Xml.XPath.XPathNodeIterator:
        ...

    @typing.overload
    def SelectChildren(self, name: str, namespaceURI: str, ) -> System.Xml.XPath.XPathNodeIterator:
        ...

    @typing.overload
    def SelectAncestors(self, type: int, matchSelf: bool, ) -> System.Xml.XPath.XPathNodeIterator:
        ...

    @typing.overload
    def SelectAncestors(self, name: str, namespaceURI: str, matchSelf: bool, ) -> System.Xml.XPath.XPathNodeIterator:
        ...

    @typing.overload
    def SelectDescendants(self, type: int, matchSelf: bool, ) -> System.Xml.XPath.XPathNodeIterator:
        ...

    @typing.overload
    def SelectDescendants(self, name: str, namespaceURI: str, matchSelf: bool, ) -> System.Xml.XPath.XPathNodeIterator:
        ...

    @typing.overload
    def PrependChild(self, ) -> System.Xml.XmlWriter:
        ...

    @typing.overload
    def PrependChild(self, newChild: str, ) -> None:
        ...

    @typing.overload
    def PrependChild(self, newChild: System.Xml.XmlReader, ) -> None:
        ...

    @typing.overload
    def PrependChild(self, newChild: System.Xml.XPath.XPathNavigator, ) -> None:
        ...

    @typing.overload
    def AppendChild(self, ) -> System.Xml.XmlWriter:
        ...

    @typing.overload
    def AppendChild(self, newChild: str, ) -> None:
        ...

    @typing.overload
    def AppendChild(self, newChild: System.Xml.XmlReader, ) -> None:
        ...

    @typing.overload
    def AppendChild(self, newChild: System.Xml.XPath.XPathNavigator, ) -> None:
        ...

    @typing.overload
    def InsertAfter(self, ) -> System.Xml.XmlWriter:
        ...

    @typing.overload
    def InsertAfter(self, newSibling: str, ) -> None:
        ...

    @typing.overload
    def InsertAfter(self, newSibling: System.Xml.XmlReader, ) -> None:
        ...

    @typing.overload
    def InsertAfter(self, newSibling: System.Xml.XPath.XPathNavigator, ) -> None:
        ...

    @typing.overload
    def InsertBefore(self, ) -> System.Xml.XmlWriter:
        ...

    @typing.overload
    def InsertBefore(self, newSibling: str, ) -> None:
        ...

    @typing.overload
    def InsertBefore(self, newSibling: System.Xml.XmlReader, ) -> None:
        ...

    @typing.overload
    def InsertBefore(self, newSibling: System.Xml.XPath.XPathNavigator, ) -> None:
        ...

    def CreateAttributes(self, ) -> System.Xml.XmlWriter:
        ...

    def ReplaceRange(self, lastSiblingToReplace: System.Xml.XPath.XPathNavigator, ) -> System.Xml.XmlWriter:
        ...

    @typing.overload
    def ReplaceSelf(self, newNode: str, ) -> None:
        ...

    @typing.overload
    def ReplaceSelf(self, newNode: System.Xml.XmlReader, ) -> None:
        ...

    @typing.overload
    def ReplaceSelf(self, newNode: System.Xml.XPath.XPathNavigator, ) -> None:
        ...

    def DeleteRange(self, lastSiblingToDelete: System.Xml.XPath.XPathNavigator, ) -> None:
        ...

    def DeleteSelf(self, ) -> None:
        ...

    def PrependChildElement(self, prefix: str, localName: str, namespaceURI: str, value: str, ) -> None:
        ...

    def AppendChildElement(self, prefix: str, localName: str, namespaceURI: str, value: str, ) -> None:
        ...

    def InsertElementBefore(self, prefix: str, localName: str, namespaceURI: str, value: str, ) -> None:
        ...

    def InsertElementAfter(self, prefix: str, localName: str, namespaceURI: str, value: str, ) -> None:
        ...

    def CreateAttribute(self, prefix: str, localName: str, namespaceURI: str, value: str, ) -> None:
        ...

    def MoveToNonDescendant(self, ) -> bool:
        ...

class XPathItem(System.Object, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    @abc.abstractmethod
    def IsNode(self) -> bool:
        ...

    @property
    @abc.abstractmethod
    def XmlType(self) -> System.Xml.Schema.XmlSchemaType:
        ...

    @property
    @abc.abstractmethod
    def Value(self) -> str:
        ...

    @property
    @abc.abstractmethod
    def TypedValue(self) -> System.Object:
        ...

    @property
    @abc.abstractmethod
    def ValueType(self) -> System.Type:
        ...

    @property
    @abc.abstractmethod
    def ValueAsBoolean(self) -> bool:
        ...

    @property
    @abc.abstractmethod
    def ValueAsDateTime(self) -> System.DateTime:
        ...

    @property
    @abc.abstractmethod
    def ValueAsDouble(self) -> float:
        ...

    @property
    @abc.abstractmethod
    def ValueAsInt(self) -> int:
        ...

    @property
    @abc.abstractmethod
    def ValueAsLong(self) -> int:
        ...

    # methods
    def __init__(self, ):
        ...

    @abc.abstractmethod
    @typing.overload
    def ValueAs(self, returnType: System.Type, nsResolver: System.Xml.IXmlNamespaceResolver, ) -> System.Object:
        ...

    @typing.overload
    def ValueAs(self, returnType: System.Type, ) -> System.Object:
        ...

class XPathNodeIterator(System.ICloneable, System.Collections.IEnumerable, System.Object, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        self.count: int
        ...

    # static fields

    # properties
    @property
    @abc.abstractmethod
    def Current(self) -> System.Xml.XPath.XPathNavigator:
        ...

    @property
    @abc.abstractmethod
    def CurrentPosition(self) -> int:
        ...

    @property
    def Count(self) -> int:
        ...

    @property
    def debuggerDisplayProxy(self) -> System.Object:
        ...

    # methods
    def __init__(self, ):
        ...

    def Clone(self, ) -> System.Object:
        ...

    @abc.abstractmethod
    def Clone(self, ) -> System.Xml.XPath.XPathNodeIterator:
        ...

    @abc.abstractmethod
    def MoveNext(self, ) -> bool:
        ...

    def GetEnumerator(self, ) -> System.Collections.IEnumerator:
        ...

class XPathNamespaceScope(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    All: int = ...
    ExcludeXml: int = ...
    Local: int = ...

class XPathExpression(System.Object, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    @abc.abstractmethod
    def Expression(self) -> str:
        ...

    @property
    @abc.abstractmethod
    def ReturnType(self) -> int:
        ...

    # methods
    def __init__(self, ):
        ...

    @abc.abstractmethod
    @typing.overload
    def AddSort(self, expr: System.Object, comparer: System.Collections.IComparer, ) -> None:
        ...

    @abc.abstractmethod
    @typing.overload
    def AddSort(self, expr: System.Object, order: int, caseOrder: int, lang: str, dataType: int, ) -> None:
        ...

    @abc.abstractmethod
    def Clone(self, ) -> System.Xml.XPath.XPathExpression:
        ...

    @abc.abstractmethod
    @typing.overload
    def SetContext(self, nsManager: System.Xml.XmlNamespaceManager, ) -> None:
        ...

    @abc.abstractmethod
    @typing.overload
    def SetContext(self, nsResolver: System.Xml.IXmlNamespaceResolver, ) -> None:
        ...

    @staticmethod
    @typing.overload
    def Compile(xpath: str, ) -> System.Xml.XPath.XPathExpression:
        ...

    @staticmethod
    @typing.overload
    def Compile(xpath: str, nsResolver: System.Xml.IXmlNamespaceResolver, ) -> System.Xml.XPath.XPathExpression:
        ...

class XmlSortOrder(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    Ascending: int = ...
    Descending: int = ...

class XPathResultType(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    Number: int = ...
    String: int = ...
    Navigator: int = ...
    Boolean: int = ...
    NodeSet: int = ...
    Any: int = ...
    Error: int = ...

class XmlCaseOrder(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    None_: int = ...
    UpperFirst: int = ...
    LowerFirst: int = ...

class XmlDataType(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    Text: int = ...
    Number: int = ...

