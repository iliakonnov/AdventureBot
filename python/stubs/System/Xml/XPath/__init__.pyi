from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import System
import System.Xml.XPath
import System.Xml
import System.Xml.Schema
import System.Collections
import System.Collections.Generic


class XPathNavigator(System.ICloneable, System.Xml.XPath.IXPathNavigable, System.Xml.IXmlNamespaceResolver, System.Xml.XPath.XPathItem, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def IsNode(self) -> System.Boolean:
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
    def ValueAsBoolean(self) -> System.Boolean:
        ...

    @property
    def ValueAsDateTime(self) -> System.DateTime:
        ...

    @property
    def ValueAsDouble(self) -> System.Double:
        ...

    @property
    def ValueAsInt(self) -> System.Int32:
        ...

    @property
    def ValueAsLong(self) -> System.Int64:
        ...

    @abc.abstractmethod
    @property
    def NameTable(self) -> System.Xml.XmlNameTable:
        ...

    @property
    def NavigatorComparer(self) -> System.Collections.IEqualityComparer:
        ...

    @abc.abstractmethod
    @property
    def NodeType(self) -> System.Xml.XPath.XPathNodeType:
        ...

    @abc.abstractmethod
    @property
    def LocalName(self) -> System.String:
        ...

    @abc.abstractmethod
    @property
    def Name(self) -> System.String:
        ...

    @abc.abstractmethod
    @property
    def NamespaceURI(self) -> System.String:
        ...

    @abc.abstractmethod
    @property
    def Prefix(self) -> System.String:
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
    def XmlLang(self) -> System.String:
        ...

    @property
    def UnderlyingObject(self) -> System.Object:
        ...

    @property
    def HasAttributes(self) -> System.Boolean:
        ...

    @property
    def HasChildren(self) -> System.Boolean:
        ...

    @property
    def SchemaInfo(self) -> System.Xml.Schema.IXmlSchemaInfo:
        ...

    @property
    def CanEdit(self) -> System.Boolean:
        ...

    @property
    def OuterXml(self) -> System.String:
        ...
    @OuterXml.setter
    def OuterXml(self, val: System.String):
        ...

    @property
    def InnerXml(self) -> System.String:
        ...
    @InnerXml.setter
    def InnerXml(self, val: System.String):
        ...

    @abc.abstractmethod
    @property
    def Value(self) -> System.String:
        ...

    # methods
    @typing.overload
    def ToString(self, ) -> System.String:
        ...

    @typing.overload
    def SetValue(self, value: System.String, ) -> None:
        ...

    @typing.overload
    def SetTypedValue(self, typedValue: System.Object, ) -> None:
        ...

    @typing.overload
    def ValueAs(self, returnType: System.Type, nsResolver: System.Xml.IXmlNamespaceResolver, ) -> System.Object:
        ...

    @typing.overload
    def CreateNavigator(self, ) -> System.Xml.XPath.XPathNavigator:
        ...

    @typing.overload
    def LookupNamespace(self, prefix: System.String, ) -> System.String:
        ...

    @typing.overload
    def LookupPrefix(self, namespaceURI: System.String, ) -> System.String:
        ...

    @typing.overload
    def GetNamespacesInScope(self, scope: System.Xml.XmlNamespaceScope, ) -> System.Collections.Generic.IDictionary[System.String, System.String]:
        ...

    @typing.overload
    @abc.abstractmethod
    def Clone(self, ) -> System.Xml.XPath.XPathNavigator:
        ...

    @typing.overload
    def ReadSubtree(self, ) -> System.Xml.XmlReader:
        ...

    @typing.overload
    def WriteSubtree(self, writer: System.Xml.XmlWriter, ) -> None:
        ...

    @typing.overload
    def GetAttribute(self, localName: System.String, namespaceURI: System.String, ) -> System.String:
        ...

    @typing.overload
    def MoveToAttribute(self, localName: System.String, namespaceURI: System.String, ) -> System.Boolean:
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
    def GetNamespace(self, name: System.String, ) -> System.String:
        ...

    @typing.overload
    def MoveToNamespace(self, name: System.String, ) -> System.Boolean:
        ...

    @typing.overload
    @abc.abstractmethod
    def MoveToFirstNamespace(self, namespaceScope: System.Xml.XPath.XPathNamespaceScope, ) -> System.Boolean:
        ...

    @typing.overload
    @abc.abstractmethod
    def MoveToNextNamespace(self, namespaceScope: System.Xml.XPath.XPathNamespaceScope, ) -> System.Boolean:
        ...

    @typing.overload
    def MoveToFirstNamespace(self, ) -> System.Boolean:
        ...

    @typing.overload
    def MoveToNextNamespace(self, ) -> System.Boolean:
        ...

    @typing.overload
    @abc.abstractmethod
    def MoveToNext(self, ) -> System.Boolean:
        ...

    @typing.overload
    @abc.abstractmethod
    def MoveToPrevious(self, ) -> System.Boolean:
        ...

    @typing.overload
    def MoveToFirst(self, ) -> System.Boolean:
        ...

    @typing.overload
    @abc.abstractmethod
    def MoveToFirstChild(self, ) -> System.Boolean:
        ...

    @typing.overload
    @abc.abstractmethod
    def MoveToParent(self, ) -> System.Boolean:
        ...

    @typing.overload
    def MoveToRoot(self, ) -> None:
        ...

    @typing.overload
    @abc.abstractmethod
    def MoveTo(self, other: System.Xml.XPath.XPathNavigator, ) -> System.Boolean:
        ...

    @typing.overload
    @abc.abstractmethod
    def MoveToId(self, id: System.String, ) -> System.Boolean:
        ...

    @typing.overload
    def MoveToChild(self, localName: System.String, namespaceURI: System.String, ) -> System.Boolean:
        ...

    @typing.overload
    def MoveToChild(self, type: System.Xml.XPath.XPathNodeType, ) -> System.Boolean:
        ...

    @typing.overload
    def MoveToFollowing(self, localName: System.String, namespaceURI: System.String, ) -> System.Boolean:
        ...

    @typing.overload
    def MoveToFollowing(self, localName: System.String, namespaceURI: System.String, end: System.Xml.XPath.XPathNavigator, ) -> System.Boolean:
        ...

    @typing.overload
    def MoveToFollowing(self, type: System.Xml.XPath.XPathNodeType, ) -> System.Boolean:
        ...

    @typing.overload
    def MoveToFollowing(self, type: System.Xml.XPath.XPathNodeType, end: System.Xml.XPath.XPathNavigator, ) -> System.Boolean:
        ...

    @typing.overload
    def MoveToNext(self, localName: System.String, namespaceURI: System.String, ) -> System.Boolean:
        ...

    @typing.overload
    def MoveToNext(self, type: System.Xml.XPath.XPathNodeType, ) -> System.Boolean:
        ...

    @typing.overload
    @abc.abstractmethod
    def IsSamePosition(self, other: System.Xml.XPath.XPathNavigator, ) -> System.Boolean:
        ...

    @typing.overload
    def IsDescendant(self, nav: System.Xml.XPath.XPathNavigator, ) -> System.Boolean:
        ...

    @typing.overload
    def ComparePosition(self, nav: System.Xml.XPath.XPathNavigator, ) -> System.Xml.XmlNodeOrder:
        ...

    @typing.overload
    def CheckValidity(self, schemas: System.Xml.Schema.XmlSchemaSet, validationEventHandler: System.Xml.Schema.ValidationEventHandler, ) -> System.Boolean:
        ...

    @typing.overload
    def Compile(self, xpath: System.String, ) -> System.Xml.XPath.XPathExpression:
        ...

    @typing.overload
    def SelectSingleNode(self, xpath: System.String, ) -> System.Xml.XPath.XPathNavigator:
        ...

    @typing.overload
    def SelectSingleNode(self, xpath: System.String, resolver: System.Xml.IXmlNamespaceResolver, ) -> System.Xml.XPath.XPathNavigator:
        ...

    @typing.overload
    def SelectSingleNode(self, expression: System.Xml.XPath.XPathExpression, ) -> System.Xml.XPath.XPathNavigator:
        ...

    @typing.overload
    def Select(self, xpath: System.String, ) -> System.Xml.XPath.XPathNodeIterator:
        ...

    @typing.overload
    def Select(self, xpath: System.String, resolver: System.Xml.IXmlNamespaceResolver, ) -> System.Xml.XPath.XPathNodeIterator:
        ...

    @typing.overload
    def Select(self, expr: System.Xml.XPath.XPathExpression, ) -> System.Xml.XPath.XPathNodeIterator:
        ...

    @typing.overload
    def Evaluate(self, xpath: System.String, ) -> System.Object:
        ...

    @typing.overload
    def Evaluate(self, xpath: System.String, resolver: System.Xml.IXmlNamespaceResolver, ) -> System.Object:
        ...

    @typing.overload
    def Evaluate(self, expr: System.Xml.XPath.XPathExpression, ) -> System.Object:
        ...

    @typing.overload
    def Evaluate(self, expr: System.Xml.XPath.XPathExpression, context: System.Xml.XPath.XPathNodeIterator, ) -> System.Object:
        ...

    @typing.overload
    def Matches(self, expr: System.Xml.XPath.XPathExpression, ) -> System.Boolean:
        ...

    @typing.overload
    def Matches(self, xpath: System.String, ) -> System.Boolean:
        ...

    @typing.overload
    def SelectChildren(self, type: System.Xml.XPath.XPathNodeType, ) -> System.Xml.XPath.XPathNodeIterator:
        ...

    @typing.overload
    def SelectChildren(self, name: System.String, namespaceURI: System.String, ) -> System.Xml.XPath.XPathNodeIterator:
        ...

    @typing.overload
    def SelectAncestors(self, type: System.Xml.XPath.XPathNodeType, matchSelf: System.Boolean, ) -> System.Xml.XPath.XPathNodeIterator:
        ...

    @typing.overload
    def SelectAncestors(self, name: System.String, namespaceURI: System.String, matchSelf: System.Boolean, ) -> System.Xml.XPath.XPathNodeIterator:
        ...

    @typing.overload
    def SelectDescendants(self, type: System.Xml.XPath.XPathNodeType, matchSelf: System.Boolean, ) -> System.Xml.XPath.XPathNodeIterator:
        ...

    @typing.overload
    def SelectDescendants(self, name: System.String, namespaceURI: System.String, matchSelf: System.Boolean, ) -> System.Xml.XPath.XPathNodeIterator:
        ...

    @typing.overload
    def PrependChild(self, ) -> System.Xml.XmlWriter:
        ...

    @typing.overload
    def AppendChild(self, ) -> System.Xml.XmlWriter:
        ...

    @typing.overload
    def InsertAfter(self, ) -> System.Xml.XmlWriter:
        ...

    @typing.overload
    def InsertBefore(self, ) -> System.Xml.XmlWriter:
        ...

    @typing.overload
    def CreateAttributes(self, ) -> System.Xml.XmlWriter:
        ...

    @typing.overload
    def ReplaceRange(self, lastSiblingToReplace: System.Xml.XPath.XPathNavigator, ) -> System.Xml.XmlWriter:
        ...

    @typing.overload
    def ReplaceSelf(self, newNode: System.String, ) -> None:
        ...

    @typing.overload
    def ReplaceSelf(self, newNode: System.Xml.XmlReader, ) -> None:
        ...

    @typing.overload
    def ReplaceSelf(self, newNode: System.Xml.XPath.XPathNavigator, ) -> None:
        ...

    @typing.overload
    def AppendChild(self, newChild: System.String, ) -> None:
        ...

    @typing.overload
    def AppendChild(self, newChild: System.Xml.XmlReader, ) -> None:
        ...

    @typing.overload
    def AppendChild(self, newChild: System.Xml.XPath.XPathNavigator, ) -> None:
        ...

    @typing.overload
    def PrependChild(self, newChild: System.String, ) -> None:
        ...

    @typing.overload
    def PrependChild(self, newChild: System.Xml.XmlReader, ) -> None:
        ...

    @typing.overload
    def PrependChild(self, newChild: System.Xml.XPath.XPathNavigator, ) -> None:
        ...

    @typing.overload
    def InsertBefore(self, newSibling: System.String, ) -> None:
        ...

    @typing.overload
    def InsertBefore(self, newSibling: System.Xml.XmlReader, ) -> None:
        ...

    @typing.overload
    def InsertBefore(self, newSibling: System.Xml.XPath.XPathNavigator, ) -> None:
        ...

    @typing.overload
    def InsertAfter(self, newSibling: System.String, ) -> None:
        ...

    @typing.overload
    def InsertAfter(self, newSibling: System.Xml.XmlReader, ) -> None:
        ...

    @typing.overload
    def InsertAfter(self, newSibling: System.Xml.XPath.XPathNavigator, ) -> None:
        ...

    @typing.overload
    def DeleteRange(self, lastSiblingToDelete: System.Xml.XPath.XPathNavigator, ) -> None:
        ...

    @typing.overload
    def DeleteSelf(self, ) -> None:
        ...

    @typing.overload
    def PrependChildElement(self, prefix: System.String, localName: System.String, namespaceURI: System.String, value: System.String, ) -> None:
        ...

    @typing.overload
    def AppendChildElement(self, prefix: System.String, localName: System.String, namespaceURI: System.String, value: System.String, ) -> None:
        ...

    @typing.overload
    def InsertElementBefore(self, prefix: System.String, localName: System.String, namespaceURI: System.String, value: System.String, ) -> None:
        ...

    @typing.overload
    def InsertElementAfter(self, prefix: System.String, localName: System.String, namespaceURI: System.String, value: System.String, ) -> None:
        ...

    @typing.overload
    def CreateAttribute(self, prefix: System.String, localName: System.String, namespaceURI: System.String, value: System.String, ) -> None:
        ...

class IXPathNavigable(abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    # methods
    @typing.overload
    @abc.abstractmethod
    def CreateNavigator(self, ) -> System.Xml.XPath.XPathNavigator:
        ...

class XPathItem(System.Object, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @abc.abstractmethod
    @property
    def IsNode(self) -> System.Boolean:
        ...

    @abc.abstractmethod
    @property
    def XmlType(self) -> System.Xml.Schema.XmlSchemaType:
        ...

    @abc.abstractmethod
    @property
    def Value(self) -> System.String:
        ...

    @abc.abstractmethod
    @property
    def TypedValue(self) -> System.Object:
        ...

    @abc.abstractmethod
    @property
    def ValueType(self) -> System.Type:
        ...

    @abc.abstractmethod
    @property
    def ValueAsBoolean(self) -> System.Boolean:
        ...

    @abc.abstractmethod
    @property
    def ValueAsDateTime(self) -> System.DateTime:
        ...

    @abc.abstractmethod
    @property
    def ValueAsDouble(self) -> System.Double:
        ...

    @abc.abstractmethod
    @property
    def ValueAsInt(self) -> System.Int32:
        ...

    @abc.abstractmethod
    @property
    def ValueAsLong(self) -> System.Int64:
        ...

    # methods
    @typing.overload
    @abc.abstractmethod
    def ValueAs(self, returnType: System.Type, nsResolver: System.Xml.IXmlNamespaceResolver, ) -> System.Object:
        ...

    @typing.overload
    def ValueAs(self, returnType: System.Type, ) -> System.Object:
        ...

class XPathNodeType(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    Root: System.Int32 = Root
    Element: System.Int32 = Element
    Attribute: System.Int32 = Attribute
    Namespace: System.Int32 = Namespace
    Text: System.Int32 = Text
    SignificantWhitespace: System.Int32 = SignificantWhitespace
    Whitespace: System.Int32 = Whitespace
    ProcessingInstruction: System.Int32 = ProcessingInstruction
    Comment: System.Int32 = Comment
    All: System.Int32 = All

class XPathNamespaceScope(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    All: System.Int32 = All
    ExcludeXml: System.Int32 = ExcludeXml
    Local: System.Int32 = Local

class XPathExpression(System.Object, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @abc.abstractmethod
    @property
    def Expression(self) -> System.String:
        ...

    @abc.abstractmethod
    @property
    def ReturnType(self) -> System.Xml.XPath.XPathResultType:
        ...

    # methods
    @typing.overload
    @abc.abstractmethod
    def AddSort(self, expr: System.Object, comparer: System.Collections.IComparer, ) -> None:
        ...

    @typing.overload
    @abc.abstractmethod
    def AddSort(self, expr: System.Object, order: System.Xml.XPath.XmlSortOrder, caseOrder: System.Xml.XPath.XmlCaseOrder, lang: System.String, dataType: System.Xml.XPath.XmlDataType, ) -> None:
        ...

    @typing.overload
    @abc.abstractmethod
    def Clone(self, ) -> System.Xml.XPath.XPathExpression:
        ...

    @typing.overload
    @abc.abstractmethod
    def SetContext(self, nsManager: System.Xml.XmlNamespaceManager, ) -> None:
        ...

    @typing.overload
    @abc.abstractmethod
    def SetContext(self, nsResolver: System.Xml.IXmlNamespaceResolver, ) -> None:
        ...

    @typing.overload
    @staticmethod
    def Compile(xpath: System.String, ) -> System.Xml.XPath.XPathExpression:
        ...

    @typing.overload
    @staticmethod
    def Compile(xpath: System.String, nsResolver: System.Xml.IXmlNamespaceResolver, ) -> System.Xml.XPath.XPathExpression:
        ...

class XPathNodeIterator(System.ICloneable, System.Collections.IEnumerable, System.Object, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @abc.abstractmethod
    @property
    def Current(self) -> System.Xml.XPath.XPathNavigator:
        ...

    @abc.abstractmethod
    @property
    def CurrentPosition(self) -> System.Int32:
        ...

    @property
    def Count(self) -> System.Int32:
        ...

    # methods
    @typing.overload
    @abc.abstractmethod
    def Clone(self, ) -> System.Xml.XPath.XPathNodeIterator:
        ...

    @typing.overload
    @abc.abstractmethod
    def MoveNext(self, ) -> System.Boolean:
        ...

    @typing.overload
    def GetEnumerator(self, ) -> System.Collections.IEnumerator:
        ...

class XPathResultType(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    Number: System.Int32 = Number
    String: System.Int32 = String
    Navigator: System.Int32 = String
    Boolean: System.Int32 = Boolean
    NodeSet: System.Int32 = NodeSet
    Any: System.Int32 = Any
    Error: System.Int32 = Error

class XmlSortOrder(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    Ascending: System.Int32 = Ascending
    Descending: System.Int32 = Descending

class XmlCaseOrder(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    None_: System.Int32 = None
    UpperFirst: System.Int32 = UpperFirst
    LowerFirst: System.Int32 = LowerFirst

class XmlDataType(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    Text: System.Int32 = Text
    Number: System.Int32 = Number

