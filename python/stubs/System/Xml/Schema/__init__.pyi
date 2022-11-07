from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import System
import System.Xml.Schema
import System.Xml
import System.Collections
import System.Runtime.Serialization
import System.Reflection
import System.Xml.Serialization
import System.IO


class XmlSchemaSet(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        self.elements: System.Xml.Schema.XmlSchemaObjectTable
        self.attributes: System.Xml.Schema.XmlSchemaObjectTable
        self.schemaTypes: System.Xml.Schema.XmlSchemaObjectTable
        self.substitutionGroups: System.Xml.Schema.XmlSchemaObjectTable
        ...

    # static fields

    # properties
    @property
    def InternalSyncObject(self) -> System.Object:
        ...

    @property
    def NameTable(self) -> System.Xml.XmlNameTable:
        ...

    @property
    def IsCompiled(self) -> bool:
        ...

    XmlResolver: System.Xml.XmlResolver = property(None, lambda val: ...)

    @property
    def CompilationSettings(self) -> System.Xml.Schema.XmlSchemaCompilationSettings:
        ...
    @CompilationSettings.setter
    def CompilationSettings(self, val: System.Xml.Schema.XmlSchemaCompilationSettings):
        ...

    @property
    def Count(self) -> int:
        ...

    @property
    def GlobalElements(self) -> System.Xml.Schema.XmlSchemaObjectTable:
        ...

    @property
    def GlobalAttributes(self) -> System.Xml.Schema.XmlSchemaObjectTable:
        ...

    @property
    def GlobalTypes(self) -> System.Xml.Schema.XmlSchemaObjectTable:
        ...

    @property
    def SubstitutionGroups(self) -> System.Xml.Schema.XmlSchemaObjectTable:
        ...

    @property
    def SchemaLocations(self) -> System.Collections.Hashtable:
        ...

    @property
    def TypeExtensions(self) -> System.Xml.Schema.XmlSchemaObjectTable:
        ...

    @property
    def CompiledInfo(self) -> System.Xml.Schema.SchemaInfo:
        ...

    @property
    def ReaderSettings(self) -> System.Xml.XmlReaderSettings:
        ...

    @property
    def SortedSchemas(self) -> System.Collections.SortedList:
        ...

    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def __init__(self, nameTable: System.Xml.XmlNameTable, ):
        ...

    @typing.overload
    def Add(self, targetNamespace: str, schemaUri: str, ) -> System.Xml.Schema.XmlSchema:
        ...

    @typing.overload
    def Add(self, targetNamespace: str, schemaDocument: System.Xml.XmlReader, ) -> System.Xml.Schema.XmlSchema:
        ...

    @typing.overload
    def Add(self, schemas: System.Xml.Schema.XmlSchemaSet, ) -> None:
        ...

    @typing.overload
    def Add(self, schema: System.Xml.Schema.XmlSchema, ) -> System.Xml.Schema.XmlSchema:
        ...

    @typing.overload
    def Add(self, targetNamespace: str, schema: System.Xml.Schema.XmlSchema, ) -> System.Xml.Schema.XmlSchema:
        ...

    @typing.overload
    def Add(self, targetNamespace: str, reader: System.Xml.XmlReader, validatedNamespaces: System.Collections.Hashtable, ) -> None:
        ...

    @typing.overload
    def Remove(self, schema: System.Xml.Schema.XmlSchema, ) -> System.Xml.Schema.XmlSchema:
        ...

    @typing.overload
    def Remove(self, schema: System.Xml.Schema.XmlSchema, forceCompile: bool, ) -> System.Xml.Schema.XmlSchema:
        ...

    def RemoveRecursive(self, schemaToRemove: System.Xml.Schema.XmlSchema, ) -> bool:
        ...

    @typing.overload
    def Contains(self, targetNamespace: str, ) -> bool:
        ...

    @typing.overload
    def Contains(self, schema: System.Xml.Schema.XmlSchema, ) -> bool:
        ...

    def Compile(self, ) -> None:
        ...

    def Reprocess(self, schema: System.Xml.Schema.XmlSchema, ) -> System.Xml.Schema.XmlSchema:
        ...

    def CopyTo(self, schemas: System.Array[System.Xml.Schema.XmlSchema], index: int, ) -> None:
        ...

    @typing.overload
    def Schemas(self, ) -> System.Collections.ICollection:
        ...

    @typing.overload
    def Schemas(self, targetNamespace: str, ) -> System.Collections.ICollection:
        ...

    def FindSchemaByNSAndUrl(self, schemaUri: System.Uri, ns: str, locationsTable: System.Array[System.Collections.DictionaryEntry], ) -> System.Xml.Schema.XmlSchema:
        ...

    def SetDtdProcessing(self, reader: System.Xml.XmlReader, ) -> None:
        ...

    def AddSchemaToSet(self, schema: System.Xml.Schema.XmlSchema, ) -> None:
        ...

    def ProcessNewSubstitutionGroups(self, substitutionGroupsTable: System.Xml.Schema.XmlSchemaObjectTable, resolve: bool, ) -> None:
        ...

    def ResolveSubstitutionGroup(self, substitutionGroup: System.Xml.Schema.XmlSchemaSubstitutionGroup, substTable: System.Xml.Schema.XmlSchemaObjectTable, ) -> None:
        ...

    def ClearTables(self, ) -> None:
        ...

    def PreprocessSchema(self, schema: ref[System.Xml.Schema.XmlSchema], targetNamespace: str, ) -> bool:
        ...

    def ParseSchema(self, targetNamespace: str, reader: System.Xml.XmlReader, ) -> System.Xml.Schema.XmlSchema:
        ...

    def CopyFromCompiledSet(self, otherSet: System.Xml.Schema.XmlSchemaSet, ) -> None:
        ...

    def GetResolver(self, ) -> System.Xml.XmlResolver:
        ...

    def GetEventHandler(self, ) -> System.Xml.Schema.ValidationEventHandler:
        ...

    def GetSchemaNames(self, nt: System.Xml.XmlNameTable, ) -> System.Xml.Schema.SchemaNames:
        ...

    def IsSchemaLoaded(self, schemaUri: System.Uri, targetNamespace: str, schema: ref[System.Xml.Schema.XmlSchema], ) -> bool:
        ...

    def GetSchemaByUri(self, schemaUri: System.Uri, schema: ref[System.Xml.Schema.XmlSchema], ) -> bool:
        ...

    def GetTargetNamespace(self, schema: System.Xml.Schema.XmlSchema, ) -> str:
        ...

    def RemoveSchemaFromCaches(self, schema: System.Xml.Schema.XmlSchema, ) -> None:
        ...

    def RemoveSchemaFromGlobalTables(self, schema: System.Xml.Schema.XmlSchema, ) -> None:
        ...

    def AddToTable(self, table: System.Xml.Schema.XmlSchemaObjectTable, qname: System.Xml.XmlQualifiedName, item: System.Xml.Schema.XmlSchemaObject, ) -> bool:
        ...

    def VerifyTables(self, ) -> None:
        ...

    def InternalValidationCallback(self, sender: System.Object, e: System.Xml.Schema.ValidationEventArgs, ) -> None:
        ...

    def SendValidationEvent(self, e: System.Xml.Schema.XmlSchemaException, severity: int, ) -> None:
        ...

class XmlSchemaObjectTable(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def Count(self) -> int:
        ...

    @property
    def Item(self) -> System.Xml.Schema.XmlSchemaObject:
        ...

    @property
    def Names(self) -> System.Collections.ICollection:
        ...

    @property
    def Values(self) -> System.Collections.ICollection:
        ...

    # methods
    def __init__(self, ):
        ...

    def Add(self, name: System.Xml.XmlQualifiedName, value: System.Xml.Schema.XmlSchemaObject, ) -> None:
        ...

    def Insert(self, name: System.Xml.XmlQualifiedName, value: System.Xml.Schema.XmlSchemaObject, ) -> None:
        ...

    def Replace(self, name: System.Xml.XmlQualifiedName, value: System.Xml.Schema.XmlSchemaObject, ) -> None:
        ...

    def Clear(self, ) -> None:
        ...

    def Remove(self, name: System.Xml.XmlQualifiedName, ) -> None:
        ...

    def FindIndexByValue(self, xso: System.Xml.Schema.XmlSchemaObject, ) -> int:
        ...

    def Contains(self, name: System.Xml.XmlQualifiedName, ) -> bool:
        ...

    def GetEnumerator(self, ) -> System.Collections.IDictionaryEnumerator:
        ...

class XmlSchemaValidationFlags(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    None_: int = ...
    ProcessInlineSchema: int = ...
    ProcessSchemaLocation: int = ...
    ReportValidationWarnings: int = ...
    ProcessIdentityConstraints: int = ...
    AllowXmlAttributes: int = ...

class XmlSchemaException(System.Runtime.Serialization.ISerializable, System.SystemException):
    @typing.overload
    def __init__(self, **kwargs):
        self._message: str
        ...

    # static fields

    # properties
    @property
    def GetRes(self) -> str:
        ...

    @property
    def Args(self) -> System.Array[str]:
        ...

    @property
    def SourceUri(self) -> str:
        ...

    @property
    def LineNumber(self) -> int:
        ...

    @property
    def LinePosition(self) -> int:
        ...

    @property
    def SourceSchemaObject(self) -> System.Xml.Schema.XmlSchemaObject:
        ...

    @property
    def Message(self) -> str:
        ...

    @property
    def TargetSite(self) -> System.Reflection.MethodBase:
        ...

    @property
    def Data(self) -> System.Collections.IDictionary:
        ...

    @property
    def InnerException(self) -> System.Exception:
        ...

    @property
    def HelpLink(self) -> str:
        ...
    @HelpLink.setter
    def HelpLink(self, val: str):
        ...

    @property
    def Source(self) -> str:
        ...
    @Source.setter
    def Source(self, val: str):
        ...

    @property
    def HResult(self) -> int:
        ...
    @HResult.setter
    def HResult(self, val: int):
        ...

    @property
    def StackTrace(self) -> str:
        ...

    # methods
    @typing.overload
    def __init__(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext, ):
        ...

    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def __init__(self, message: str, ):
        ...

    @typing.overload
    def __init__(self, message: str, innerException: System.Exception, ):
        ...

    @typing.overload
    def __init__(self, message: str, innerException: System.Exception, lineNumber: int, linePosition: int, ):
        ...

    @typing.overload
    def __init__(self, res: str, args: System.Array[str], ):
        ...

    @typing.overload
    def __init__(self, res: str, arg: str, ):
        ...

    @typing.overload
    def __init__(self, res: str, arg: str, sourceUri: str, lineNumber: int, linePosition: int, ):
        ...

    @typing.overload
    def __init__(self, res: str, sourceUri: str, lineNumber: int, linePosition: int, ):
        ...

    @typing.overload
    def __init__(self, res: str, args: System.Array[str], sourceUri: str, lineNumber: int, linePosition: int, ):
        ...

    @typing.overload
    def __init__(self, res: str, source: System.Xml.Schema.XmlSchemaObject, ):
        ...

    @typing.overload
    def __init__(self, res: str, arg: str, source: System.Xml.Schema.XmlSchemaObject, ):
        ...

    @typing.overload
    def __init__(self, res: str, args: System.Array[str], source: System.Xml.Schema.XmlSchemaObject, ):
        ...

    @typing.overload
    def __init__(self, res: str, args: System.Array[str], innerException: System.Exception, sourceUri: str, lineNumber: int, linePosition: int, source: System.Xml.Schema.XmlSchemaObject, ):
        ...

    def GetObjectData(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext, ) -> None:
        ...

    @staticmethod
    def CreateMessage(res: str, args: System.Array[str], ) -> str:
        ...

    @typing.overload
    def SetSource(self, sourceUri: str, lineNumber: int, linePosition: int, ) -> None:
        ...

    @typing.overload
    def SetSource(self, source: System.Xml.Schema.XmlSchemaObject, ) -> None:
        ...

    def SetSchemaObject(self, source: System.Xml.Schema.XmlSchemaObject, ) -> None:
        ...

class XmlSchemaObject(System.Object, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def LineNumber(self) -> int:
        ...
    @LineNumber.setter
    def LineNumber(self, val: int):
        ...

    @property
    def LinePosition(self) -> int:
        ...
    @LinePosition.setter
    def LinePosition(self, val: int):
        ...

    @property
    def SourceUri(self) -> str:
        ...
    @SourceUri.setter
    def SourceUri(self, val: str):
        ...

    @property
    def Parent(self) -> System.Xml.Schema.XmlSchemaObject:
        ...
    @Parent.setter
    def Parent(self, val: System.Xml.Schema.XmlSchemaObject):
        ...

    @property
    def Namespaces(self) -> System.Xml.Serialization.XmlSerializerNamespaces:
        ...
    @Namespaces.setter
    def Namespaces(self, val: System.Xml.Serialization.XmlSerializerNamespaces):
        ...

    @property
    def IdAttribute(self) -> str:
        ...
    @IdAttribute.setter
    def IdAttribute(self, val: str):
        ...

    @property
    def NameAttribute(self) -> str:
        ...
    @NameAttribute.setter
    def NameAttribute(self, val: str):
        ...

    @property
    def IsProcessing(self) -> bool:
        ...
    @IsProcessing.setter
    def IsProcessing(self, val: bool):
        ...

    # methods
    def __init__(self, ):
        ...

    def OnAdd(self, container: System.Xml.Schema.XmlSchemaObjectCollection, item: System.Object, ) -> None:
        ...

    def OnRemove(self, container: System.Xml.Schema.XmlSchemaObjectCollection, item: System.Object, ) -> None:
        ...

    def OnClear(self, container: System.Xml.Schema.XmlSchemaObjectCollection, ) -> None:
        ...

    def SetUnhandledAttributes(self, moreAttributes: System.Array[System.Xml.XmlAttribute], ) -> None:
        ...

    def AddAnnotation(self, annotation: System.Xml.Schema.XmlSchemaAnnotation, ) -> None:
        ...

    def Clone(self, ) -> System.Xml.Schema.XmlSchemaObject:
        ...

class XmlSchemaObjectCollection(System.Collections.IList, System.Collections.ICollection, System.Collections.IEnumerable, System.Collections.CollectionBase):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def Item(self) -> System.Xml.Schema.XmlSchemaObject:
        ...
    @Item.setter
    def Item(self, val: System.Xml.Schema.XmlSchemaObject):
        ...

    @property
    def InnerList(self) -> System.Collections.ArrayList:
        ...

    @property
    def List(self) -> System.Collections.IList:
        ...

    @property
    def Capacity(self) -> int:
        ...
    @Capacity.setter
    def Capacity(self, val: int):
        ...

    @property
    def Count(self) -> int:
        ...

    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def __init__(self, parent: System.Xml.Schema.XmlSchemaObject, ):
        ...

    def GetEnumerator(self, ) -> System.Xml.Schema.XmlSchemaObjectEnumerator:
        ...

    @typing.overload
    def Add(self, item: System.Xml.Schema.XmlSchemaObject, ) -> int:
        ...

    @typing.overload
    def Add(self, collToAdd: System.Xml.Schema.XmlSchemaObjectCollection, ) -> None:
        ...

    def Insert(self, index: int, item: System.Xml.Schema.XmlSchemaObject, ) -> None:
        ...

    def IndexOf(self, item: System.Xml.Schema.XmlSchemaObject, ) -> int:
        ...

    def Contains(self, item: System.Xml.Schema.XmlSchemaObject, ) -> bool:
        ...

    def Remove(self, item: System.Xml.Schema.XmlSchemaObject, ) -> None:
        ...

    def CopyTo(self, array: System.Array[System.Xml.Schema.XmlSchemaObject], index: int, ) -> None:
        ...

    def OnInsert(self, index: int, item: System.Object, ) -> None:
        ...

    def OnSet(self, index: int, oldValue: System.Object, newValue: System.Object, ) -> None:
        ...

    def OnClear(self, ) -> None:
        ...

    def OnRemove(self, index: int, item: System.Object, ) -> None:
        ...

    def Clone(self, ) -> System.Xml.Schema.XmlSchemaObjectCollection:
        ...

class XmlSchemaAnnotation(System.Xml.Schema.XmlSchemaObject):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def Id(self) -> str:
        ...
    @Id.setter
    def Id(self, val: str):
        ...

    @property
    def Items(self) -> System.Xml.Schema.XmlSchemaObjectCollection:
        ...

    @property
    def UnhandledAttributes(self) -> System.Array[System.Xml.XmlAttribute]:
        ...
    @UnhandledAttributes.setter
    def UnhandledAttributes(self, val: System.Array[System.Xml.XmlAttribute]):
        ...

    @property
    def IdAttribute(self) -> str:
        ...
    @IdAttribute.setter
    def IdAttribute(self, val: str):
        ...

    @property
    def LineNumber(self) -> int:
        ...
    @LineNumber.setter
    def LineNumber(self, val: int):
        ...

    @property
    def LinePosition(self) -> int:
        ...
    @LinePosition.setter
    def LinePosition(self, val: int):
        ...

    @property
    def SourceUri(self) -> str:
        ...
    @SourceUri.setter
    def SourceUri(self, val: str):
        ...

    @property
    def Parent(self) -> System.Xml.Schema.XmlSchemaObject:
        ...
    @Parent.setter
    def Parent(self, val: System.Xml.Schema.XmlSchemaObject):
        ...

    @property
    def Namespaces(self) -> System.Xml.Serialization.XmlSerializerNamespaces:
        ...
    @Namespaces.setter
    def Namespaces(self, val: System.Xml.Serialization.XmlSerializerNamespaces):
        ...

    @property
    def NameAttribute(self) -> str:
        ...
    @NameAttribute.setter
    def NameAttribute(self, val: str):
        ...

    @property
    def IsProcessing(self) -> bool:
        ...
    @IsProcessing.setter
    def IsProcessing(self, val: bool):
        ...

    # methods
    def __init__(self, ):
        ...

    def SetUnhandledAttributes(self, moreAttributes: System.Array[System.Xml.XmlAttribute], ) -> None:
        ...

class IXmlSchemaInfo(abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    @abc.abstractmethod
    def Validity(self) -> int:
        ...

    @property
    @abc.abstractmethod
    def IsDefault(self) -> bool:
        ...

    @property
    @abc.abstractmethod
    def IsNil(self) -> bool:
        ...

    @property
    @abc.abstractmethod
    def MemberType(self) -> System.Xml.Schema.XmlSchemaSimpleType:
        ...

    @property
    @abc.abstractmethod
    def SchemaType(self) -> System.Xml.Schema.XmlSchemaType:
        ...

    @property
    @abc.abstractmethod
    def SchemaElement(self) -> System.Xml.Schema.XmlSchemaElement:
        ...

    @property
    @abc.abstractmethod
    def SchemaAttribute(self) -> System.Xml.Schema.XmlSchemaAttribute:
        ...

    # methods
class XmlSchemaValidity(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    NotKnown: int = ...
    Valid: int = ...
    Invalid: int = ...

class XmlSchemaAttribute(System.Xml.Schema.XmlSchemaAnnotated):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def DefaultValue(self) -> str:
        ...
    @DefaultValue.setter
    def DefaultValue(self, val: str):
        ...

    @property
    def FixedValue(self) -> str:
        ...
    @FixedValue.setter
    def FixedValue(self, val: str):
        ...

    @property
    def Form(self) -> int:
        ...
    @Form.setter
    def Form(self, val: int):
        ...

    @property
    def Name(self) -> str:
        ...
    @Name.setter
    def Name(self, val: str):
        ...

    @property
    def RefName(self) -> System.Xml.XmlQualifiedName:
        ...
    @RefName.setter
    def RefName(self, val: System.Xml.XmlQualifiedName):
        ...

    @property
    def SchemaTypeName(self) -> System.Xml.XmlQualifiedName:
        ...
    @SchemaTypeName.setter
    def SchemaTypeName(self, val: System.Xml.XmlQualifiedName):
        ...

    @property
    def SchemaType(self) -> System.Xml.Schema.XmlSchemaSimpleType:
        ...
    @SchemaType.setter
    def SchemaType(self, val: System.Xml.Schema.XmlSchemaSimpleType):
        ...

    @property
    def Use(self) -> int:
        ...
    @Use.setter
    def Use(self, val: int):
        ...

    @property
    def QualifiedName(self) -> System.Xml.XmlQualifiedName:
        ...

    @property
    def AttributeType(self) -> System.Object:
        ...

    @property
    def AttributeSchemaType(self) -> System.Xml.Schema.XmlSchemaSimpleType:
        ...

    @property
    def Datatype(self) -> System.Xml.Schema.XmlSchemaDatatype:
        ...

    @property
    def AttDef(self) -> System.Xml.Schema.SchemaAttDef:
        ...
    @AttDef.setter
    def AttDef(self, val: System.Xml.Schema.SchemaAttDef):
        ...

    @property
    def HasDefault(self) -> bool:
        ...

    @property
    def NameAttribute(self) -> str:
        ...
    @NameAttribute.setter
    def NameAttribute(self, val: str):
        ...

    @property
    def Id(self) -> str:
        ...
    @Id.setter
    def Id(self, val: str):
        ...

    @property
    def Annotation(self) -> System.Xml.Schema.XmlSchemaAnnotation:
        ...
    @Annotation.setter
    def Annotation(self, val: System.Xml.Schema.XmlSchemaAnnotation):
        ...

    @property
    def UnhandledAttributes(self) -> System.Array[System.Xml.XmlAttribute]:
        ...
    @UnhandledAttributes.setter
    def UnhandledAttributes(self, val: System.Array[System.Xml.XmlAttribute]):
        ...

    @property
    def IdAttribute(self) -> str:
        ...
    @IdAttribute.setter
    def IdAttribute(self, val: str):
        ...

    @property
    def LineNumber(self) -> int:
        ...
    @LineNumber.setter
    def LineNumber(self, val: int):
        ...

    @property
    def LinePosition(self) -> int:
        ...
    @LinePosition.setter
    def LinePosition(self, val: int):
        ...

    @property
    def SourceUri(self) -> str:
        ...
    @SourceUri.setter
    def SourceUri(self, val: str):
        ...

    @property
    def Parent(self) -> System.Xml.Schema.XmlSchemaObject:
        ...
    @Parent.setter
    def Parent(self, val: System.Xml.Schema.XmlSchemaObject):
        ...

    @property
    def Namespaces(self) -> System.Xml.Serialization.XmlSerializerNamespaces:
        ...
    @Namespaces.setter
    def Namespaces(self, val: System.Xml.Serialization.XmlSerializerNamespaces):
        ...

    @property
    def IsProcessing(self) -> bool:
        ...
    @IsProcessing.setter
    def IsProcessing(self, val: bool):
        ...

    # methods
    def __init__(self, ):
        ...

    def Validate(self, reader: System.Xml.XmlReader, resolver: System.Xml.XmlResolver, schemaSet: System.Xml.Schema.XmlSchemaSet, valEventHandler: System.Xml.Schema.ValidationEventHandler, ) -> System.Xml.XmlReader:
        ...

    def SetQualifiedName(self, value: System.Xml.XmlQualifiedName, ) -> None:
        ...

    def SetAttributeType(self, value: System.Xml.Schema.XmlSchemaSimpleType, ) -> None:
        ...

    def Clone(self, ) -> System.Xml.Schema.XmlSchemaObject:
        ...

class XmlSchemaAnnotated(System.Xml.Schema.XmlSchemaObject):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def Id(self) -> str:
        ...
    @Id.setter
    def Id(self, val: str):
        ...

    @property
    def Annotation(self) -> System.Xml.Schema.XmlSchemaAnnotation:
        ...
    @Annotation.setter
    def Annotation(self, val: System.Xml.Schema.XmlSchemaAnnotation):
        ...

    @property
    def UnhandledAttributes(self) -> System.Array[System.Xml.XmlAttribute]:
        ...
    @UnhandledAttributes.setter
    def UnhandledAttributes(self, val: System.Array[System.Xml.XmlAttribute]):
        ...

    @property
    def IdAttribute(self) -> str:
        ...
    @IdAttribute.setter
    def IdAttribute(self, val: str):
        ...

    @property
    def LineNumber(self) -> int:
        ...
    @LineNumber.setter
    def LineNumber(self, val: int):
        ...

    @property
    def LinePosition(self) -> int:
        ...
    @LinePosition.setter
    def LinePosition(self, val: int):
        ...

    @property
    def SourceUri(self) -> str:
        ...
    @SourceUri.setter
    def SourceUri(self, val: str):
        ...

    @property
    def Parent(self) -> System.Xml.Schema.XmlSchemaObject:
        ...
    @Parent.setter
    def Parent(self, val: System.Xml.Schema.XmlSchemaObject):
        ...

    @property
    def Namespaces(self) -> System.Xml.Serialization.XmlSerializerNamespaces:
        ...
    @Namespaces.setter
    def Namespaces(self, val: System.Xml.Serialization.XmlSerializerNamespaces):
        ...

    @property
    def NameAttribute(self) -> str:
        ...
    @NameAttribute.setter
    def NameAttribute(self, val: str):
        ...

    @property
    def IsProcessing(self) -> bool:
        ...
    @IsProcessing.setter
    def IsProcessing(self, val: bool):
        ...

    # methods
    def __init__(self, ):
        ...

    def SetUnhandledAttributes(self, moreAttributes: System.Array[System.Xml.XmlAttribute], ) -> None:
        ...

    def AddAnnotation(self, annotation: System.Xml.Schema.XmlSchemaAnnotation, ) -> None:
        ...

class XmlSchemaForm(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    None_: int = ...
    Qualified: int = ...
    Unqualified: int = ...

class XmlSchemaSimpleType(System.Xml.Schema.XmlSchemaType):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def Content(self) -> System.Xml.Schema.XmlSchemaSimpleTypeContent:
        ...
    @Content.setter
    def Content(self, val: System.Xml.Schema.XmlSchemaSimpleTypeContent):
        ...

    @property
    def DerivedFrom(self) -> System.Xml.XmlQualifiedName:
        ...

    @property
    def Name(self) -> str:
        ...
    @Name.setter
    def Name(self, val: str):
        ...

    @property
    def Final(self) -> int:
        ...
    @Final.setter
    def Final(self, val: int):
        ...

    @property
    def QualifiedName(self) -> System.Xml.XmlQualifiedName:
        ...

    @property
    def FinalResolved(self) -> int:
        ...

    @property
    def BaseSchemaType(self) -> System.Object:
        ...

    @property
    def BaseXmlSchemaType(self) -> System.Xml.Schema.XmlSchemaType:
        ...

    @property
    def DerivedBy(self) -> int:
        ...

    @property
    def Datatype(self) -> System.Xml.Schema.XmlSchemaDatatype:
        ...

    @property
    def IsMixed(self) -> bool:
        ...
    @IsMixed.setter
    def IsMixed(self, val: bool):
        ...

    @property
    def TypeCode(self) -> int:
        ...

    @property
    def ValueConverter(self) -> System.Xml.Schema.XmlValueConverter:
        ...

    @property
    def SchemaContentType(self) -> int:
        ...

    @property
    def ElementDecl(self) -> System.Xml.Schema.SchemaElementDecl:
        ...
    @ElementDecl.setter
    def ElementDecl(self, val: System.Xml.Schema.SchemaElementDecl):
        ...

    @property
    def Redefined(self) -> System.Xml.Schema.XmlSchemaType:
        ...
    @Redefined.setter
    def Redefined(self, val: System.Xml.Schema.XmlSchemaType):
        ...

    @property
    def NameAttribute(self) -> str:
        ...
    @NameAttribute.setter
    def NameAttribute(self, val: str):
        ...

    @property
    def Id(self) -> str:
        ...
    @Id.setter
    def Id(self, val: str):
        ...

    @property
    def Annotation(self) -> System.Xml.Schema.XmlSchemaAnnotation:
        ...
    @Annotation.setter
    def Annotation(self, val: System.Xml.Schema.XmlSchemaAnnotation):
        ...

    @property
    def UnhandledAttributes(self) -> System.Array[System.Xml.XmlAttribute]:
        ...
    @UnhandledAttributes.setter
    def UnhandledAttributes(self, val: System.Array[System.Xml.XmlAttribute]):
        ...

    @property
    def IdAttribute(self) -> str:
        ...
    @IdAttribute.setter
    def IdAttribute(self, val: str):
        ...

    @property
    def LineNumber(self) -> int:
        ...
    @LineNumber.setter
    def LineNumber(self, val: int):
        ...

    @property
    def LinePosition(self) -> int:
        ...
    @LinePosition.setter
    def LinePosition(self, val: int):
        ...

    @property
    def SourceUri(self) -> str:
        ...
    @SourceUri.setter
    def SourceUri(self, val: str):
        ...

    @property
    def Parent(self) -> System.Xml.Schema.XmlSchemaObject:
        ...
    @Parent.setter
    def Parent(self, val: System.Xml.Schema.XmlSchemaObject):
        ...

    @property
    def Namespaces(self) -> System.Xml.Serialization.XmlSerializerNamespaces:
        ...
    @Namespaces.setter
    def Namespaces(self, val: System.Xml.Serialization.XmlSerializerNamespaces):
        ...

    @property
    def IsProcessing(self) -> bool:
        ...
    @IsProcessing.setter
    def IsProcessing(self, val: bool):
        ...

    # methods
    def __init__(self, ):
        ...

    def Clone(self, ) -> System.Xml.Schema.XmlSchemaObject:
        ...

class XmlSchemaDerivationMethod(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    Empty: int = ...
    Substitution: int = ...
    Extension: int = ...
    Restriction: int = ...
    List: int = ...
    Union: int = ...
    All: int = ...
    None_: int = ...

class XmlTypeCode(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    None_: int = ...
    Item: int = ...
    Node: int = ...
    Document: int = ...
    Element: int = ...
    Attribute: int = ...
    Namespace: int = ...
    ProcessingInstruction: int = ...
    Comment: int = ...
    Text: int = ...
    AnyAtomicType: int = ...
    UntypedAtomic: int = ...
    String: int = ...
    Boolean: int = ...
    Decimal: int = ...
    Float: int = ...
    Double: int = ...
    Duration: int = ...
    DateTime: int = ...
    Time: int = ...
    Date: int = ...
    GYearMonth: int = ...
    GYear: int = ...
    GMonthDay: int = ...
    GDay: int = ...
    GMonth: int = ...
    HexBinary: int = ...
    Base64Binary: int = ...
    AnyUri: int = ...
    QName: int = ...
    Notation: int = ...
    NormalizedString: int = ...
    Token: int = ...
    Language: int = ...
    NmToken: int = ...
    Name: int = ...
    NCName: int = ...
    Id: int = ...
    Idref: int = ...
    Entity: int = ...
    Integer: int = ...
    NonPositiveInteger: int = ...
    NegativeInteger: int = ...
    Long: int = ...
    Int: int = ...
    Short: int = ...
    Byte: int = ...
    NonNegativeInteger: int = ...
    UnsignedLong: int = ...
    UnsignedInt: int = ...
    UnsignedShort: int = ...
    UnsignedByte: int = ...
    PositiveInteger: int = ...
    YearMonthDuration: int = ...
    DayTimeDuration: int = ...

class XmlSchemaDatatype(System.Object, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    @abc.abstractmethod
    def ValueType(self) -> System.Type:
        ...

    @property
    @abc.abstractmethod
    def TokenizedType(self) -> int:
        ...

    @property
    def Variety(self) -> int:
        ...

    @property
    def TypeCode(self) -> int:
        ...

    @property
    @abc.abstractmethod
    def HasLexicalFacets(self) -> bool:
        ...

    @property
    @abc.abstractmethod
    def HasValueFacets(self) -> bool:
        ...

    @property
    @abc.abstractmethod
    def ValueConverter(self) -> System.Xml.Schema.XmlValueConverter:
        ...

    @property
    @abc.abstractmethod
    def Restriction(self) -> System.Xml.Schema.RestrictionFacets:
        ...

    @property
    @abc.abstractmethod
    def FacetsChecker(self) -> System.Xml.Schema.FacetsChecker:
        ...

    @property
    @abc.abstractmethod
    def BuiltInWhitespaceFacet(self) -> int:
        ...

    @property
    def TypeCodeString(self) -> str:
        ...

    # methods
    def __init__(self, ):
        ...

    @abc.abstractmethod
    @typing.overload
    def ParseValue(self, s: str, nameTable: System.Xml.XmlNameTable, nsmgr: System.Xml.IXmlNamespaceResolver, ) -> System.Object:
        ...

    @abc.abstractmethod
    @typing.overload
    def ParseValue(self, s: str, nameTable: System.Xml.XmlNameTable, nsmgr: System.Xml.IXmlNamespaceResolver, createAtomicValue: bool, ) -> System.Object:
        ...

    @typing.overload
    def ChangeType(self, value: System.Object, targetType: System.Type, ) -> System.Object:
        ...

    @typing.overload
    def ChangeType(self, value: System.Object, targetType: System.Type, namespaceResolver: System.Xml.IXmlNamespaceResolver, ) -> System.Object:
        ...

    def IsDerivedFrom(self, datatype: System.Xml.Schema.XmlSchemaDatatype, ) -> bool:
        ...

    @abc.abstractmethod
    def Compare(self, value1: System.Object, value2: System.Object, ) -> int:
        ...

    @abc.abstractmethod
    @typing.overload
    def TryParseValue(self, s: str, nameTable: System.Xml.XmlNameTable, nsmgr: System.Xml.IXmlNamespaceResolver, typedValue: ref[System.Object], ) -> System.Exception:
        ...

    @abc.abstractmethod
    @typing.overload
    def TryParseValue(self, value: System.Object, nameTable: System.Xml.XmlNameTable, namespaceResolver: System.Xml.IXmlNamespaceResolver, typedValue: ref[System.Object], ) -> System.Exception:
        ...

    @abc.abstractmethod
    def DeriveByRestriction(self, facets: System.Xml.Schema.XmlSchemaObjectCollection, nameTable: System.Xml.XmlNameTable, schemaType: System.Xml.Schema.XmlSchemaType, ) -> System.Xml.Schema.XmlSchemaDatatype:
        ...

    @abc.abstractmethod
    def DeriveByList(self, schemaType: System.Xml.Schema.XmlSchemaType, ) -> System.Xml.Schema.XmlSchemaDatatype:
        ...

    @abc.abstractmethod
    def VerifySchemaValid(self, notations: System.Xml.Schema.XmlSchemaObjectTable, caller: System.Xml.Schema.XmlSchemaObject, ) -> None:
        ...

    @abc.abstractmethod
    def IsEqual(self, o1: System.Object, o2: System.Object, ) -> bool:
        ...

    @abc.abstractmethod
    def IsComparable(self, dtype: System.Xml.Schema.XmlSchemaDatatype, ) -> bool:
        ...

    def TypeCodeToString(self, typeCode: int, ) -> str:
        ...

    @staticmethod
    def ConcatenatedToString(value: System.Object, ) -> str:
        ...

    @staticmethod
    def FromXmlTokenizedType(token: int, ) -> System.Xml.Schema.XmlSchemaDatatype:
        ...

    @staticmethod
    def FromXmlTokenizedTypeXsd(token: int, ) -> System.Xml.Schema.XmlSchemaDatatype:
        ...

    @staticmethod
    def FromXdrName(name: str, ) -> System.Xml.Schema.XmlSchemaDatatype:
        ...

    @staticmethod
    def DeriveByUnion(types: System.Array[System.Xml.Schema.XmlSchemaSimpleType], schemaType: System.Xml.Schema.XmlSchemaType, ) -> System.Xml.Schema.XmlSchemaDatatype:
        ...

    @staticmethod
    def XdrCanonizeUri(uri: str, nameTable: System.Xml.XmlNameTable, schemaNames: System.Xml.Schema.SchemaNames, ) -> str:
        ...

class XmlSchemaSimpleTypeContent(System.Xml.Schema.XmlSchemaAnnotated, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def Id(self) -> str:
        ...
    @Id.setter
    def Id(self, val: str):
        ...

    @property
    def Annotation(self) -> System.Xml.Schema.XmlSchemaAnnotation:
        ...
    @Annotation.setter
    def Annotation(self, val: System.Xml.Schema.XmlSchemaAnnotation):
        ...

    @property
    def UnhandledAttributes(self) -> System.Array[System.Xml.XmlAttribute]:
        ...
    @UnhandledAttributes.setter
    def UnhandledAttributes(self, val: System.Array[System.Xml.XmlAttribute]):
        ...

    @property
    def IdAttribute(self) -> str:
        ...
    @IdAttribute.setter
    def IdAttribute(self, val: str):
        ...

    @property
    def LineNumber(self) -> int:
        ...
    @LineNumber.setter
    def LineNumber(self, val: int):
        ...

    @property
    def LinePosition(self) -> int:
        ...
    @LinePosition.setter
    def LinePosition(self, val: int):
        ...

    @property
    def SourceUri(self) -> str:
        ...
    @SourceUri.setter
    def SourceUri(self, val: str):
        ...

    @property
    def Parent(self) -> System.Xml.Schema.XmlSchemaObject:
        ...
    @Parent.setter
    def Parent(self, val: System.Xml.Schema.XmlSchemaObject):
        ...

    @property
    def Namespaces(self) -> System.Xml.Serialization.XmlSerializerNamespaces:
        ...
    @Namespaces.setter
    def Namespaces(self, val: System.Xml.Serialization.XmlSerializerNamespaces):
        ...

    @property
    def NameAttribute(self) -> str:
        ...
    @NameAttribute.setter
    def NameAttribute(self, val: str):
        ...

    @property
    def IsProcessing(self) -> bool:
        ...
    @IsProcessing.setter
    def IsProcessing(self, val: bool):
        ...

    # methods
    def __init__(self, ):
        ...

class XmlSchemaContentType(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    TextOnly: int = ...
    Empty: int = ...
    ElementOnly: int = ...
    Mixed: int = ...

class XmlSchemaType(System.Xml.Schema.XmlSchemaAnnotated):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def Name(self) -> str:
        ...
    @Name.setter
    def Name(self, val: str):
        ...

    @property
    def Final(self) -> int:
        ...
    @Final.setter
    def Final(self, val: int):
        ...

    @property
    def QualifiedName(self) -> System.Xml.XmlQualifiedName:
        ...

    @property
    def FinalResolved(self) -> int:
        ...

    @property
    def BaseSchemaType(self) -> System.Object:
        ...

    @property
    def BaseXmlSchemaType(self) -> System.Xml.Schema.XmlSchemaType:
        ...

    @property
    def DerivedBy(self) -> int:
        ...

    @property
    def Datatype(self) -> System.Xml.Schema.XmlSchemaDatatype:
        ...

    @property
    def IsMixed(self) -> bool:
        ...
    @IsMixed.setter
    def IsMixed(self, val: bool):
        ...

    @property
    def TypeCode(self) -> int:
        ...

    @property
    def ValueConverter(self) -> System.Xml.Schema.XmlValueConverter:
        ...

    @property
    def SchemaContentType(self) -> int:
        ...

    @property
    def ElementDecl(self) -> System.Xml.Schema.SchemaElementDecl:
        ...
    @ElementDecl.setter
    def ElementDecl(self, val: System.Xml.Schema.SchemaElementDecl):
        ...

    @property
    def Redefined(self) -> System.Xml.Schema.XmlSchemaType:
        ...
    @Redefined.setter
    def Redefined(self, val: System.Xml.Schema.XmlSchemaType):
        ...

    @property
    def DerivedFrom(self) -> System.Xml.XmlQualifiedName:
        ...

    @property
    def NameAttribute(self) -> str:
        ...
    @NameAttribute.setter
    def NameAttribute(self, val: str):
        ...

    @property
    def Id(self) -> str:
        ...
    @Id.setter
    def Id(self, val: str):
        ...

    @property
    def Annotation(self) -> System.Xml.Schema.XmlSchemaAnnotation:
        ...
    @Annotation.setter
    def Annotation(self, val: System.Xml.Schema.XmlSchemaAnnotation):
        ...

    @property
    def UnhandledAttributes(self) -> System.Array[System.Xml.XmlAttribute]:
        ...
    @UnhandledAttributes.setter
    def UnhandledAttributes(self, val: System.Array[System.Xml.XmlAttribute]):
        ...

    @property
    def IdAttribute(self) -> str:
        ...
    @IdAttribute.setter
    def IdAttribute(self, val: str):
        ...

    @property
    def LineNumber(self) -> int:
        ...
    @LineNumber.setter
    def LineNumber(self, val: int):
        ...

    @property
    def LinePosition(self) -> int:
        ...
    @LinePosition.setter
    def LinePosition(self, val: int):
        ...

    @property
    def SourceUri(self) -> str:
        ...
    @SourceUri.setter
    def SourceUri(self, val: str):
        ...

    @property
    def Parent(self) -> System.Xml.Schema.XmlSchemaObject:
        ...
    @Parent.setter
    def Parent(self, val: System.Xml.Schema.XmlSchemaObject):
        ...

    @property
    def Namespaces(self) -> System.Xml.Serialization.XmlSerializerNamespaces:
        ...
    @Namespaces.setter
    def Namespaces(self, val: System.Xml.Serialization.XmlSerializerNamespaces):
        ...

    @property
    def IsProcessing(self) -> bool:
        ...
    @IsProcessing.setter
    def IsProcessing(self, val: bool):
        ...

    # methods
    def __init__(self, ):
        ...

    @staticmethod
    @typing.overload
    def GetBuiltInSimpleType(qualifiedName: System.Xml.XmlQualifiedName, ) -> System.Xml.Schema.XmlSchemaSimpleType:
        ...

    @staticmethod
    @typing.overload
    def GetBuiltInSimpleType(typeCode: int, ) -> System.Xml.Schema.XmlSchemaSimpleType:
        ...

    @staticmethod
    @typing.overload
    def GetBuiltInComplexType(typeCode: int, ) -> System.Xml.Schema.XmlSchemaComplexType:
        ...

    @staticmethod
    @typing.overload
    def GetBuiltInComplexType(qualifiedName: System.Xml.XmlQualifiedName, ) -> System.Xml.Schema.XmlSchemaComplexType:
        ...

    def Validate(self, reader: System.Xml.XmlReader, resolver: System.Xml.XmlResolver, schemaSet: System.Xml.Schema.XmlSchemaSet, valEventHandler: System.Xml.Schema.ValidationEventHandler, ) -> System.Xml.XmlReader:
        ...

    def SetQualifiedName(self, value: System.Xml.XmlQualifiedName, ) -> None:
        ...

    def SetFinalResolved(self, value: int, ) -> None:
        ...

    def SetBaseSchemaType(self, value: System.Xml.Schema.XmlSchemaType, ) -> None:
        ...

    def SetDerivedBy(self, value: int, ) -> None:
        ...

    def SetDatatype(self, value: System.Xml.Schema.XmlSchemaDatatype, ) -> None:
        ...

    def SetContentType(self, value: int, ) -> None:
        ...

    @staticmethod
    def IsDerivedFrom(derivedType: System.Xml.Schema.XmlSchemaType, baseType: System.Xml.Schema.XmlSchemaType, except_: int, ) -> bool:
        ...

    @staticmethod
    def IsDerivedFromDatatype(derivedDataType: System.Xml.Schema.XmlSchemaDatatype, baseDataType: System.Xml.Schema.XmlSchemaDatatype, except_: int, ) -> bool:
        ...

class ValidationEventHandler(System.ICloneable, System.Runtime.Serialization.ISerializable, System.MulticastDelegate):
    @typing.overload
    def __init__(self, **kwargs):
        self._target: System.Object
        self._methodBase: System.Object
        self._methodPtr: System.IntPtr
        self._methodPtrAux: System.IntPtr
        ...

    # static fields

    # properties
    @property
    def Target(self) -> System.Object:
        ...

    @property
    def Method(self) -> System.Reflection.MethodInfo:
        ...

    # methods
    def __init__(self, object: System.Object, method: System.IntPtr, ):
        ...

    def Invoke(self, sender: System.Object, e: System.Xml.Schema.ValidationEventArgs, ) -> None:
        ...

    def BeginInvoke(self, sender: System.Object, e: System.Xml.Schema.ValidationEventArgs, callback: System.AsyncCallback, object: System.Object, ) -> System.IAsyncResult:
        ...

    def EndInvoke(self, result: System.IAsyncResult, ) -> None:
        ...

class XmlSchemaDatatypeVariety(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    Atomic: int = ...
    List: int = ...
    Union: int = ...

class XmlSeverityType(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    Error: int = ...
    Warning: int = ...

class ValidationEventArgs(System.EventArgs):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def Severity(self) -> int:
        ...

    @property
    def Exception(self) -> System.Xml.Schema.XmlSchemaException:
        ...

    @property
    def Message(self) -> str:
        ...

    # methods
    @typing.overload
    def __init__(self, ex: System.Xml.Schema.XmlSchemaException, ):
        ...

    @typing.overload
    def __init__(self, ex: System.Xml.Schema.XmlSchemaException, severity: int, ):
        ...

class XmlSchemaComplexType(System.Xml.Schema.XmlSchemaType):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def AnyType(self) -> System.Xml.Schema.XmlSchemaComplexType:
        ...

    @property
    def UntypedAnyType(self) -> System.Xml.Schema.XmlSchemaComplexType:
        ...

    @property
    def AnyTypeSkip(self) -> System.Xml.Schema.XmlSchemaComplexType:
        ...

    @property
    def AnyTypeContentValidator(self) -> System.Xml.Schema.ContentValidator:
        ...

    @property
    def IsAbstract(self) -> bool:
        ...
    @IsAbstract.setter
    def IsAbstract(self, val: bool):
        ...

    @property
    def Block(self) -> int:
        ...
    @Block.setter
    def Block(self, val: int):
        ...

    @property
    def IsMixed(self) -> bool:
        ...
    @IsMixed.setter
    def IsMixed(self, val: bool):
        ...

    @property
    def ContentModel(self) -> System.Xml.Schema.XmlSchemaContentModel:
        ...
    @ContentModel.setter
    def ContentModel(self, val: System.Xml.Schema.XmlSchemaContentModel):
        ...

    @property
    def Particle(self) -> System.Xml.Schema.XmlSchemaParticle:
        ...
    @Particle.setter
    def Particle(self, val: System.Xml.Schema.XmlSchemaParticle):
        ...

    @property
    def Attributes(self) -> System.Xml.Schema.XmlSchemaObjectCollection:
        ...

    @property
    def AnyAttribute(self) -> System.Xml.Schema.XmlSchemaAnyAttribute:
        ...
    @AnyAttribute.setter
    def AnyAttribute(self, val: System.Xml.Schema.XmlSchemaAnyAttribute):
        ...

    @property
    def ContentType(self) -> int:
        ...

    @property
    def ContentTypeParticle(self) -> System.Xml.Schema.XmlSchemaParticle:
        ...

    @property
    def BlockResolved(self) -> int:
        ...

    @property
    def AttributeUses(self) -> System.Xml.Schema.XmlSchemaObjectTable:
        ...

    @property
    def AttributeWildcard(self) -> System.Xml.Schema.XmlSchemaAnyAttribute:
        ...

    @property
    def LocalElements(self) -> System.Xml.Schema.XmlSchemaObjectTable:
        ...

    @property
    def HasWildCard(self) -> bool:
        ...
    @HasWildCard.setter
    def HasWildCard(self, val: bool):
        ...

    @property
    def DerivedFrom(self) -> System.Xml.XmlQualifiedName:
        ...

    @property
    def Name(self) -> str:
        ...
    @Name.setter
    def Name(self, val: str):
        ...

    @property
    def Final(self) -> int:
        ...
    @Final.setter
    def Final(self, val: int):
        ...

    @property
    def QualifiedName(self) -> System.Xml.XmlQualifiedName:
        ...

    @property
    def FinalResolved(self) -> int:
        ...

    @property
    def BaseSchemaType(self) -> System.Object:
        ...

    @property
    def BaseXmlSchemaType(self) -> System.Xml.Schema.XmlSchemaType:
        ...

    @property
    def DerivedBy(self) -> int:
        ...

    @property
    def Datatype(self) -> System.Xml.Schema.XmlSchemaDatatype:
        ...

    @property
    def TypeCode(self) -> int:
        ...

    @property
    def ValueConverter(self) -> System.Xml.Schema.XmlValueConverter:
        ...

    @property
    def SchemaContentType(self) -> int:
        ...

    @property
    def ElementDecl(self) -> System.Xml.Schema.SchemaElementDecl:
        ...
    @ElementDecl.setter
    def ElementDecl(self, val: System.Xml.Schema.SchemaElementDecl):
        ...

    @property
    def Redefined(self) -> System.Xml.Schema.XmlSchemaType:
        ...
    @Redefined.setter
    def Redefined(self, val: System.Xml.Schema.XmlSchemaType):
        ...

    @property
    def NameAttribute(self) -> str:
        ...
    @NameAttribute.setter
    def NameAttribute(self, val: str):
        ...

    @property
    def Id(self) -> str:
        ...
    @Id.setter
    def Id(self, val: str):
        ...

    @property
    def Annotation(self) -> System.Xml.Schema.XmlSchemaAnnotation:
        ...
    @Annotation.setter
    def Annotation(self, val: System.Xml.Schema.XmlSchemaAnnotation):
        ...

    @property
    def UnhandledAttributes(self) -> System.Array[System.Xml.XmlAttribute]:
        ...
    @UnhandledAttributes.setter
    def UnhandledAttributes(self, val: System.Array[System.Xml.XmlAttribute]):
        ...

    @property
    def IdAttribute(self) -> str:
        ...
    @IdAttribute.setter
    def IdAttribute(self, val: str):
        ...

    @property
    def LineNumber(self) -> int:
        ...
    @LineNumber.setter
    def LineNumber(self, val: int):
        ...

    @property
    def LinePosition(self) -> int:
        ...
    @LinePosition.setter
    def LinePosition(self, val: int):
        ...

    @property
    def SourceUri(self) -> str:
        ...
    @SourceUri.setter
    def SourceUri(self, val: str):
        ...

    @property
    def Parent(self) -> System.Xml.Schema.XmlSchemaObject:
        ...
    @Parent.setter
    def Parent(self, val: System.Xml.Schema.XmlSchemaObject):
        ...

    @property
    def Namespaces(self) -> System.Xml.Serialization.XmlSerializerNamespaces:
        ...
    @Namespaces.setter
    def Namespaces(self, val: System.Xml.Serialization.XmlSerializerNamespaces):
        ...

    @property
    def IsProcessing(self) -> bool:
        ...
    @IsProcessing.setter
    def IsProcessing(self, val: bool):
        ...

    # methods
    def __init__(self, ):
        ...

    @staticmethod
    def CreateUntypedAnyType() -> System.Xml.Schema.XmlSchemaComplexType:
        ...

    @staticmethod
    def CreateAnyType(processContents: int, ) -> System.Xml.Schema.XmlSchemaComplexType:
        ...

    def SetContentTypeParticle(self, value: System.Xml.Schema.XmlSchemaParticle, ) -> None:
        ...

    def SetBlockResolved(self, value: int, ) -> None:
        ...

    def SetAttributeWildcard(self, value: System.Xml.Schema.XmlSchemaAnyAttribute, ) -> None:
        ...

    def SetAttributes(self, newAttributes: System.Xml.Schema.XmlSchemaObjectCollection, ) -> None:
        ...

    def ContainsIdAttribute(self, findAll: bool, ) -> bool:
        ...

    @typing.overload
    def Clone(self, ) -> System.Xml.Schema.XmlSchemaObject:
        ...

    @typing.overload
    def Clone(self, parentSchema: System.Xml.Schema.XmlSchema, ) -> System.Xml.Schema.XmlSchemaObject:
        ...

    def ClearCompiledState(self, ) -> None:
        ...

    @staticmethod
    def CloneAttributes(attributes: System.Xml.Schema.XmlSchemaObjectCollection, ) -> System.Xml.Schema.XmlSchemaObjectCollection:
        ...

    @staticmethod
    def CloneGroupBaseParticles(groupBaseParticles: System.Xml.Schema.XmlSchemaObjectCollection, parentSchema: System.Xml.Schema.XmlSchema, ) -> System.Xml.Schema.XmlSchemaObjectCollection:
        ...

    @staticmethod
    def CloneParticle(particle: System.Xml.Schema.XmlSchemaParticle, parentSchema: System.Xml.Schema.XmlSchema, ) -> System.Xml.Schema.XmlSchemaParticle:
        ...

    @staticmethod
    def GetResolvedElementForm(parentSchema: System.Xml.Schema.XmlSchema, element: System.Xml.Schema.XmlSchemaElement, ) -> int:
        ...

    @staticmethod
    def HasParticleRef(particle: System.Xml.Schema.XmlSchemaParticle, parentSchema: System.Xml.Schema.XmlSchema, ) -> bool:
        ...

    @staticmethod
    def HasAttributeQNameRef(attributes: System.Xml.Schema.XmlSchemaObjectCollection, ) -> bool:
        ...

class XmlSchemaAnyAttribute(System.Xml.Schema.XmlSchemaAnnotated):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def Namespace(self) -> str:
        ...
    @Namespace.setter
    def Namespace(self, val: str):
        ...

    @property
    def ProcessContents(self) -> int:
        ...
    @ProcessContents.setter
    def ProcessContents(self, val: int):
        ...

    @property
    def NamespaceList(self) -> System.Xml.Schema.NamespaceList:
        ...

    @property
    def ProcessContentsCorrect(self) -> int:
        ...

    @property
    def Id(self) -> str:
        ...
    @Id.setter
    def Id(self, val: str):
        ...

    @property
    def Annotation(self) -> System.Xml.Schema.XmlSchemaAnnotation:
        ...
    @Annotation.setter
    def Annotation(self, val: System.Xml.Schema.XmlSchemaAnnotation):
        ...

    @property
    def UnhandledAttributes(self) -> System.Array[System.Xml.XmlAttribute]:
        ...
    @UnhandledAttributes.setter
    def UnhandledAttributes(self, val: System.Array[System.Xml.XmlAttribute]):
        ...

    @property
    def IdAttribute(self) -> str:
        ...
    @IdAttribute.setter
    def IdAttribute(self, val: str):
        ...

    @property
    def LineNumber(self) -> int:
        ...
    @LineNumber.setter
    def LineNumber(self, val: int):
        ...

    @property
    def LinePosition(self) -> int:
        ...
    @LinePosition.setter
    def LinePosition(self, val: int):
        ...

    @property
    def SourceUri(self) -> str:
        ...
    @SourceUri.setter
    def SourceUri(self, val: str):
        ...

    @property
    def Parent(self) -> System.Xml.Schema.XmlSchemaObject:
        ...
    @Parent.setter
    def Parent(self, val: System.Xml.Schema.XmlSchemaObject):
        ...

    @property
    def Namespaces(self) -> System.Xml.Serialization.XmlSerializerNamespaces:
        ...
    @Namespaces.setter
    def Namespaces(self, val: System.Xml.Serialization.XmlSerializerNamespaces):
        ...

    @property
    def NameAttribute(self) -> str:
        ...
    @NameAttribute.setter
    def NameAttribute(self, val: str):
        ...

    @property
    def IsProcessing(self) -> bool:
        ...
    @IsProcessing.setter
    def IsProcessing(self, val: bool):
        ...

    # methods
    def __init__(self, ):
        ...

    def BuildNamespaceList(self, targetNamespace: str, ) -> None:
        ...

    def BuildNamespaceListV1Compat(self, targetNamespace: str, ) -> None:
        ...

    def Allows(self, qname: System.Xml.XmlQualifiedName, ) -> bool:
        ...

    @staticmethod
    def IsSubset(sub: System.Xml.Schema.XmlSchemaAnyAttribute, super: System.Xml.Schema.XmlSchemaAnyAttribute, ) -> bool:
        ...

    @staticmethod
    def Intersection(o1: System.Xml.Schema.XmlSchemaAnyAttribute, o2: System.Xml.Schema.XmlSchemaAnyAttribute, v1Compat: bool, ) -> System.Xml.Schema.XmlSchemaAnyAttribute:
        ...

    @staticmethod
    def Union(o1: System.Xml.Schema.XmlSchemaAnyAttribute, o2: System.Xml.Schema.XmlSchemaAnyAttribute, v1Compat: bool, ) -> System.Xml.Schema.XmlSchemaAnyAttribute:
        ...

class XmlSchemaContentProcessing(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    None_: int = ...
    Skip: int = ...
    Lax: int = ...
    Strict: int = ...

class XmlSchemaParticle(System.Xml.Schema.XmlSchemaAnnotated, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields
    Empty: System.Xml.Schema.XmlSchemaParticle = ...

    # properties
    @property
    def MinOccursString(self) -> str:
        ...
    @MinOccursString.setter
    def MinOccursString(self, val: str):
        ...

    @property
    def MaxOccursString(self) -> str:
        ...
    @MaxOccursString.setter
    def MaxOccursString(self, val: str):
        ...

    @property
    def MinOccurs(self) -> System.Decimal:
        ...
    @MinOccurs.setter
    def MinOccurs(self, val: System.Decimal):
        ...

    @property
    def MaxOccurs(self) -> System.Decimal:
        ...
    @MaxOccurs.setter
    def MaxOccurs(self, val: System.Decimal):
        ...

    @property
    def IsEmpty(self) -> bool:
        ...

    @property
    def IsMultipleOccurrence(self) -> bool:
        ...

    @property
    def NameString(self) -> str:
        ...

    @property
    def Id(self) -> str:
        ...
    @Id.setter
    def Id(self, val: str):
        ...

    @property
    def Annotation(self) -> System.Xml.Schema.XmlSchemaAnnotation:
        ...
    @Annotation.setter
    def Annotation(self, val: System.Xml.Schema.XmlSchemaAnnotation):
        ...

    @property
    def UnhandledAttributes(self) -> System.Array[System.Xml.XmlAttribute]:
        ...
    @UnhandledAttributes.setter
    def UnhandledAttributes(self, val: System.Array[System.Xml.XmlAttribute]):
        ...

    @property
    def IdAttribute(self) -> str:
        ...
    @IdAttribute.setter
    def IdAttribute(self, val: str):
        ...

    @property
    def LineNumber(self) -> int:
        ...
    @LineNumber.setter
    def LineNumber(self, val: int):
        ...

    @property
    def LinePosition(self) -> int:
        ...
    @LinePosition.setter
    def LinePosition(self, val: int):
        ...

    @property
    def SourceUri(self) -> str:
        ...
    @SourceUri.setter
    def SourceUri(self, val: str):
        ...

    @property
    def Parent(self) -> System.Xml.Schema.XmlSchemaObject:
        ...
    @Parent.setter
    def Parent(self, val: System.Xml.Schema.XmlSchemaObject):
        ...

    @property
    def Namespaces(self) -> System.Xml.Serialization.XmlSerializerNamespaces:
        ...
    @Namespaces.setter
    def Namespaces(self, val: System.Xml.Serialization.XmlSerializerNamespaces):
        ...

    @property
    def NameAttribute(self) -> str:
        ...
    @NameAttribute.setter
    def NameAttribute(self, val: str):
        ...

    @property
    def IsProcessing(self) -> bool:
        ...
    @IsProcessing.setter
    def IsProcessing(self, val: bool):
        ...

    # methods
    def __init__(self, ):
        ...

    def GetQualifiedName(self, ) -> System.Xml.XmlQualifiedName:
        ...

class XmlSchemaContentModel(System.Xml.Schema.XmlSchemaAnnotated, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    @abc.abstractmethod
    def Content(self) -> System.Xml.Schema.XmlSchemaContent:
        ...
    @Content.setter
    @abc.abstractmethod
    def Content(self, val: System.Xml.Schema.XmlSchemaContent):
        ...

    @property
    def Id(self) -> str:
        ...
    @Id.setter
    def Id(self, val: str):
        ...

    @property
    def Annotation(self) -> System.Xml.Schema.XmlSchemaAnnotation:
        ...
    @Annotation.setter
    def Annotation(self, val: System.Xml.Schema.XmlSchemaAnnotation):
        ...

    @property
    def UnhandledAttributes(self) -> System.Array[System.Xml.XmlAttribute]:
        ...
    @UnhandledAttributes.setter
    def UnhandledAttributes(self, val: System.Array[System.Xml.XmlAttribute]):
        ...

    @property
    def IdAttribute(self) -> str:
        ...
    @IdAttribute.setter
    def IdAttribute(self, val: str):
        ...

    @property
    def LineNumber(self) -> int:
        ...
    @LineNumber.setter
    def LineNumber(self, val: int):
        ...

    @property
    def LinePosition(self) -> int:
        ...
    @LinePosition.setter
    def LinePosition(self, val: int):
        ...

    @property
    def SourceUri(self) -> str:
        ...
    @SourceUri.setter
    def SourceUri(self, val: str):
        ...

    @property
    def Parent(self) -> System.Xml.Schema.XmlSchemaObject:
        ...
    @Parent.setter
    def Parent(self, val: System.Xml.Schema.XmlSchemaObject):
        ...

    @property
    def Namespaces(self) -> System.Xml.Serialization.XmlSerializerNamespaces:
        ...
    @Namespaces.setter
    def Namespaces(self, val: System.Xml.Serialization.XmlSerializerNamespaces):
        ...

    @property
    def NameAttribute(self) -> str:
        ...
    @NameAttribute.setter
    def NameAttribute(self, val: str):
        ...

    @property
    def IsProcessing(self) -> bool:
        ...
    @IsProcessing.setter
    def IsProcessing(self, val: bool):
        ...

    # methods
    def __init__(self, ):
        ...

class XmlSchemaContent(System.Xml.Schema.XmlSchemaAnnotated, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def Id(self) -> str:
        ...
    @Id.setter
    def Id(self, val: str):
        ...

    @property
    def Annotation(self) -> System.Xml.Schema.XmlSchemaAnnotation:
        ...
    @Annotation.setter
    def Annotation(self, val: System.Xml.Schema.XmlSchemaAnnotation):
        ...

    @property
    def UnhandledAttributes(self) -> System.Array[System.Xml.XmlAttribute]:
        ...
    @UnhandledAttributes.setter
    def UnhandledAttributes(self, val: System.Array[System.Xml.XmlAttribute]):
        ...

    @property
    def IdAttribute(self) -> str:
        ...
    @IdAttribute.setter
    def IdAttribute(self, val: str):
        ...

    @property
    def LineNumber(self) -> int:
        ...
    @LineNumber.setter
    def LineNumber(self, val: int):
        ...

    @property
    def LinePosition(self) -> int:
        ...
    @LinePosition.setter
    def LinePosition(self, val: int):
        ...

    @property
    def SourceUri(self) -> str:
        ...
    @SourceUri.setter
    def SourceUri(self, val: str):
        ...

    @property
    def Parent(self) -> System.Xml.Schema.XmlSchemaObject:
        ...
    @Parent.setter
    def Parent(self, val: System.Xml.Schema.XmlSchemaObject):
        ...

    @property
    def Namespaces(self) -> System.Xml.Serialization.XmlSerializerNamespaces:
        ...
    @Namespaces.setter
    def Namespaces(self, val: System.Xml.Serialization.XmlSerializerNamespaces):
        ...

    @property
    def NameAttribute(self) -> str:
        ...
    @NameAttribute.setter
    def NameAttribute(self, val: str):
        ...

    @property
    def IsProcessing(self) -> bool:
        ...
    @IsProcessing.setter
    def IsProcessing(self, val: bool):
        ...

    # methods
    def __init__(self, ):
        ...

class XmlSchemaCompilationSettings(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def EnableUpaCheck(self) -> bool:
        ...
    @EnableUpaCheck.setter
    def EnableUpaCheck(self, val: bool):
        ...

    # methods
    def __init__(self, ):
        ...

class XmlSchema(System.Xml.Schema.XmlSchemaObject):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields
    Namespace: str = ...
    InstanceNamespace: str = ...

    # properties
    @property
    def AttributeFormDefault(self) -> int:
        ...
    @AttributeFormDefault.setter
    def AttributeFormDefault(self, val: int):
        ...

    @property
    def BlockDefault(self) -> int:
        ...
    @BlockDefault.setter
    def BlockDefault(self, val: int):
        ...

    @property
    def FinalDefault(self) -> int:
        ...
    @FinalDefault.setter
    def FinalDefault(self, val: int):
        ...

    @property
    def ElementFormDefault(self) -> int:
        ...
    @ElementFormDefault.setter
    def ElementFormDefault(self, val: int):
        ...

    @property
    def TargetNamespace(self) -> str:
        ...
    @TargetNamespace.setter
    def TargetNamespace(self, val: str):
        ...

    @property
    def Version(self) -> str:
        ...
    @Version.setter
    def Version(self, val: str):
        ...

    @property
    def Includes(self) -> System.Xml.Schema.XmlSchemaObjectCollection:
        ...

    @property
    def Items(self) -> System.Xml.Schema.XmlSchemaObjectCollection:
        ...

    @property
    def IsCompiled(self) -> bool:
        ...

    @property
    def IsCompiledBySet(self) -> bool:
        ...
    @IsCompiledBySet.setter
    def IsCompiledBySet(self, val: bool):
        ...

    @property
    def IsPreprocessed(self) -> bool:
        ...
    @IsPreprocessed.setter
    def IsPreprocessed(self, val: bool):
        ...

    @property
    def IsRedefined(self) -> bool:
        ...
    @IsRedefined.setter
    def IsRedefined(self, val: bool):
        ...

    @property
    def Attributes(self) -> System.Xml.Schema.XmlSchemaObjectTable:
        ...

    @property
    def AttributeGroups(self) -> System.Xml.Schema.XmlSchemaObjectTable:
        ...

    @property
    def SchemaTypes(self) -> System.Xml.Schema.XmlSchemaObjectTable:
        ...

    @property
    def Elements(self) -> System.Xml.Schema.XmlSchemaObjectTable:
        ...

    @property
    def Id(self) -> str:
        ...
    @Id.setter
    def Id(self, val: str):
        ...

    @property
    def UnhandledAttributes(self) -> System.Array[System.Xml.XmlAttribute]:
        ...
    @UnhandledAttributes.setter
    def UnhandledAttributes(self, val: System.Array[System.Xml.XmlAttribute]):
        ...

    @property
    def Groups(self) -> System.Xml.Schema.XmlSchemaObjectTable:
        ...

    @property
    def Notations(self) -> System.Xml.Schema.XmlSchemaObjectTable:
        ...

    @property
    def IdentityConstraints(self) -> System.Xml.Schema.XmlSchemaObjectTable:
        ...

    @property
    def BaseUri(self) -> System.Uri:
        ...
    @BaseUri.setter
    def BaseUri(self, val: System.Uri):
        ...

    @property
    def SchemaId(self) -> int:
        ...

    @property
    def IsChameleon(self) -> bool:
        ...
    @IsChameleon.setter
    def IsChameleon(self, val: bool):
        ...

    @property
    def Ids(self) -> System.Collections.Hashtable:
        ...

    @property
    def Document(self) -> System.Xml.XmlDocument:
        ...

    @property
    def ErrorCount(self) -> int:
        ...
    @ErrorCount.setter
    def ErrorCount(self, val: int):
        ...

    @property
    def IdAttribute(self) -> str:
        ...
    @IdAttribute.setter
    def IdAttribute(self, val: str):
        ...

    @property
    def NameTable(self) -> System.Xml.XmlNameTable:
        ...

    @property
    def ImportedSchemas(self) -> System.Collections.ArrayList:
        ...

    @property
    def ImportedNamespaces(self) -> System.Collections.ArrayList:
        ...

    @property
    def LineNumber(self) -> int:
        ...
    @LineNumber.setter
    def LineNumber(self, val: int):
        ...

    @property
    def LinePosition(self) -> int:
        ...
    @LinePosition.setter
    def LinePosition(self, val: int):
        ...

    @property
    def SourceUri(self) -> str:
        ...
    @SourceUri.setter
    def SourceUri(self, val: str):
        ...

    @property
    def Parent(self) -> System.Xml.Schema.XmlSchemaObject:
        ...
    @Parent.setter
    def Parent(self, val: System.Xml.Schema.XmlSchemaObject):
        ...

    @property
    def Namespaces(self) -> System.Xml.Serialization.XmlSerializerNamespaces:
        ...
    @Namespaces.setter
    def Namespaces(self, val: System.Xml.Serialization.XmlSerializerNamespaces):
        ...

    @property
    def NameAttribute(self) -> str:
        ...
    @NameAttribute.setter
    def NameAttribute(self, val: str):
        ...

    @property
    def IsProcessing(self) -> bool:
        ...
    @IsProcessing.setter
    def IsProcessing(self, val: bool):
        ...

    # methods
    def __init__(self, ):
        ...

    @staticmethod
    @typing.overload
    def Read(reader: System.IO.TextReader, validationEventHandler: System.Xml.Schema.ValidationEventHandler, ) -> System.Xml.Schema.XmlSchema:
        ...

    @staticmethod
    @typing.overload
    def Read(stream: System.IO.Stream, validationEventHandler: System.Xml.Schema.ValidationEventHandler, ) -> System.Xml.Schema.XmlSchema:
        ...

    @staticmethod
    @typing.overload
    def Read(reader: System.Xml.XmlReader, validationEventHandler: System.Xml.Schema.ValidationEventHandler, ) -> System.Xml.Schema.XmlSchema:
        ...

    @typing.overload
    def Write(self, stream: System.IO.Stream, ) -> None:
        ...

    @typing.overload
    def Write(self, stream: System.IO.Stream, namespaceManager: System.Xml.XmlNamespaceManager, ) -> None:
        ...

    @typing.overload
    def Write(self, writer: System.IO.TextWriter, ) -> None:
        ...

    @typing.overload
    def Write(self, writer: System.IO.TextWriter, namespaceManager: System.Xml.XmlNamespaceManager, ) -> None:
        ...

    @typing.overload
    def Write(self, writer: System.Xml.XmlWriter, ) -> None:
        ...

    @typing.overload
    def Write(self, writer: System.Xml.XmlWriter, namespaceManager: System.Xml.XmlNamespaceManager, ) -> None:
        ...

    @typing.overload
    def Compile(self, validationEventHandler: System.Xml.Schema.ValidationEventHandler, ) -> None:
        ...

    @typing.overload
    def Compile(self, validationEventHandler: System.Xml.Schema.ValidationEventHandler, resolver: System.Xml.XmlResolver, ) -> None:
        ...

    def CompileSchema(self, xsc: System.Xml.Schema.XmlSchemaCollection, resolver: System.Xml.XmlResolver, schemaInfo: System.Xml.Schema.SchemaInfo, ns: str, validationEventHandler: System.Xml.Schema.ValidationEventHandler, nameTable: System.Xml.XmlNameTable, CompileContentModel: bool, ) -> bool:
        ...

    def CompileSchemaInSet(self, nameTable: System.Xml.XmlNameTable, eventHandler: System.Xml.Schema.ValidationEventHandler, compilationSettings: System.Xml.Schema.XmlSchemaCompilationSettings, ) -> None:
        ...

    def Clone(self, ) -> System.Xml.Schema.XmlSchema:
        ...

    def DeepClone(self, ) -> System.Xml.Schema.XmlSchema:
        ...

    def SetIsCompiled(self, isCompiled: bool, ) -> None:
        ...

    def SetUnhandledAttributes(self, moreAttributes: System.Array[System.Xml.XmlAttribute], ) -> None:
        ...

    def AddAnnotation(self, annotation: System.Xml.Schema.XmlSchemaAnnotation, ) -> None:
        ...

    def GetExternalSchemasList(self, extList: System.Collections.IList, schema: System.Xml.Schema.XmlSchema, ) -> None:
        ...

class XmlSchemaCollection(System.Collections.ICollection, System.Collections.IEnumerable, System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def Count(self) -> int:
        ...

    @property
    def NameTable(self) -> System.Xml.XmlNameTable:
        ...

    XmlResolver: System.Xml.XmlResolver = property(None, lambda val: ...)

    @property
    def Item(self) -> System.Xml.Schema.XmlSchema:
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
    def EventHandler(self) -> System.Xml.Schema.ValidationEventHandler:
        ...
    @EventHandler.setter
    def EventHandler(self, val: System.Xml.Schema.ValidationEventHandler):
        ...

    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def __init__(self, nametable: System.Xml.XmlNameTable, ):
        ...

    @typing.overload
    def Add(self, ns: str, uri: str, ) -> System.Xml.Schema.XmlSchema:
        ...

    @typing.overload
    def Add(self, ns: str, reader: System.Xml.XmlReader, ) -> System.Xml.Schema.XmlSchema:
        ...

    @typing.overload
    def Add(self, ns: str, reader: System.Xml.XmlReader, resolver: System.Xml.XmlResolver, ) -> System.Xml.Schema.XmlSchema:
        ...

    @typing.overload
    def Add(self, schema: System.Xml.Schema.XmlSchema, ) -> System.Xml.Schema.XmlSchema:
        ...

    @typing.overload
    def Add(self, schema: System.Xml.Schema.XmlSchema, resolver: System.Xml.XmlResolver, ) -> System.Xml.Schema.XmlSchema:
        ...

    @typing.overload
    def Add(self, schema: System.Xml.Schema.XmlSchemaCollection, ) -> None:
        ...

    @typing.overload
    def Add(self, ns: str, schemaInfo: System.Xml.Schema.SchemaInfo, schema: System.Xml.Schema.XmlSchema, compile: bool, ) -> System.Xml.Schema.XmlSchema:
        ...

    @typing.overload
    def Add(self, ns: str, schemaInfo: System.Xml.Schema.SchemaInfo, schema: System.Xml.Schema.XmlSchema, compile: bool, resolver: System.Xml.XmlResolver, ) -> System.Xml.Schema.XmlSchema:
        ...

    @typing.overload
    def Add(self, ns: str, node: System.Xml.Schema.XmlSchemaCollectionNode, ) -> None:
        ...

    @typing.overload
    def Contains(self, schema: System.Xml.Schema.XmlSchema, ) -> bool:
        ...

    @typing.overload
    def Contains(self, ns: str, ) -> bool:
        ...

    def GetEnumerator(self, ) -> System.Collections.IEnumerator:
        ...

    def GetEnumerator(self, ) -> System.Xml.Schema.XmlSchemaCollectionEnumerator:
        ...

    def CopyTo(self, array: System.Array, index: int, ) -> None:
        ...

    def CopyTo(self, array: System.Array[System.Xml.Schema.XmlSchema], index: int, ) -> None:
        ...

    def GetSchemaInfo(self, ns: str, ) -> System.Xml.Schema.SchemaInfo:
        ...

    def GetSchemaNames(self, nt: System.Xml.XmlNameTable, ) -> System.Xml.Schema.SchemaNames:
        ...

    def AddNonThreadSafe(self, ns: str, node: System.Xml.Schema.XmlSchemaCollectionNode, ) -> None:
        ...

    def SendValidationEvent(self, e: System.Xml.Schema.XmlSchemaException, ) -> None:
        ...

class XmlSchemaCollectionEnumerator(System.Collections.IEnumerator, System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def Current(self) -> System.Object:
        ...

    @property
    def Current(self) -> System.Xml.Schema.XmlSchema:
        ...

    @property
    def CurrentNode(self) -> System.Xml.Schema.XmlSchemaCollectionNode:
        ...

    # methods
    def __init__(self, collection: System.Collections.Hashtable, ):
        ...

    def Reset(self, ) -> None:
        ...

    def MoveNext(self, ) -> bool:
        ...

    def MoveNext(self, ) -> bool:
        ...

class XmlSchemaUse(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    None_: int = ...
    Optional: int = ...
    Prohibited: int = ...
    Required: int = ...

class XmlSchemaElement(System.Xml.Schema.XmlSchemaParticle):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def IsAbstract(self) -> bool:
        ...
    @IsAbstract.setter
    def IsAbstract(self, val: bool):
        ...

    @property
    def Block(self) -> int:
        ...
    @Block.setter
    def Block(self, val: int):
        ...

    @property
    def DefaultValue(self) -> str:
        ...
    @DefaultValue.setter
    def DefaultValue(self, val: str):
        ...

    @property
    def Final(self) -> int:
        ...
    @Final.setter
    def Final(self, val: int):
        ...

    @property
    def FixedValue(self) -> str:
        ...
    @FixedValue.setter
    def FixedValue(self, val: str):
        ...

    @property
    def Form(self) -> int:
        ...
    @Form.setter
    def Form(self, val: int):
        ...

    @property
    def Name(self) -> str:
        ...
    @Name.setter
    def Name(self, val: str):
        ...

    @property
    def IsNillable(self) -> bool:
        ...
    @IsNillable.setter
    def IsNillable(self, val: bool):
        ...

    @property
    def HasNillableAttribute(self) -> bool:
        ...

    @property
    def HasAbstractAttribute(self) -> bool:
        ...

    @property
    def RefName(self) -> System.Xml.XmlQualifiedName:
        ...
    @RefName.setter
    def RefName(self, val: System.Xml.XmlQualifiedName):
        ...

    @property
    def SubstitutionGroup(self) -> System.Xml.XmlQualifiedName:
        ...
    @SubstitutionGroup.setter
    def SubstitutionGroup(self, val: System.Xml.XmlQualifiedName):
        ...

    @property
    def SchemaTypeName(self) -> System.Xml.XmlQualifiedName:
        ...
    @SchemaTypeName.setter
    def SchemaTypeName(self, val: System.Xml.XmlQualifiedName):
        ...

    @property
    def SchemaType(self) -> System.Xml.Schema.XmlSchemaType:
        ...
    @SchemaType.setter
    def SchemaType(self, val: System.Xml.Schema.XmlSchemaType):
        ...

    @property
    def Constraints(self) -> System.Xml.Schema.XmlSchemaObjectCollection:
        ...

    @property
    def QualifiedName(self) -> System.Xml.XmlQualifiedName:
        ...

    @property
    def ElementType(self) -> System.Object:
        ...

    @property
    def ElementSchemaType(self) -> System.Xml.Schema.XmlSchemaType:
        ...

    @property
    def BlockResolved(self) -> int:
        ...

    @property
    def FinalResolved(self) -> int:
        ...

    @property
    def HasDefault(self) -> bool:
        ...

    @property
    def HasConstraints(self) -> bool:
        ...

    @property
    def IsLocalTypeDerivationChecked(self) -> bool:
        ...
    @IsLocalTypeDerivationChecked.setter
    def IsLocalTypeDerivationChecked(self, val: bool):
        ...

    @property
    def ElementDecl(self) -> System.Xml.Schema.SchemaElementDecl:
        ...
    @ElementDecl.setter
    def ElementDecl(self, val: System.Xml.Schema.SchemaElementDecl):
        ...

    @property
    def NameAttribute(self) -> str:
        ...
    @NameAttribute.setter
    def NameAttribute(self, val: str):
        ...

    @property
    def NameString(self) -> str:
        ...

    @property
    def MinOccursString(self) -> str:
        ...
    @MinOccursString.setter
    def MinOccursString(self, val: str):
        ...

    @property
    def MaxOccursString(self) -> str:
        ...
    @MaxOccursString.setter
    def MaxOccursString(self, val: str):
        ...

    @property
    def MinOccurs(self) -> System.Decimal:
        ...
    @MinOccurs.setter
    def MinOccurs(self, val: System.Decimal):
        ...

    @property
    def MaxOccurs(self) -> System.Decimal:
        ...
    @MaxOccurs.setter
    def MaxOccurs(self, val: System.Decimal):
        ...

    @property
    def IsEmpty(self) -> bool:
        ...

    @property
    def IsMultipleOccurrence(self) -> bool:
        ...

    @property
    def Id(self) -> str:
        ...
    @Id.setter
    def Id(self, val: str):
        ...

    @property
    def Annotation(self) -> System.Xml.Schema.XmlSchemaAnnotation:
        ...
    @Annotation.setter
    def Annotation(self, val: System.Xml.Schema.XmlSchemaAnnotation):
        ...

    @property
    def UnhandledAttributes(self) -> System.Array[System.Xml.XmlAttribute]:
        ...
    @UnhandledAttributes.setter
    def UnhandledAttributes(self, val: System.Array[System.Xml.XmlAttribute]):
        ...

    @property
    def IdAttribute(self) -> str:
        ...
    @IdAttribute.setter
    def IdAttribute(self, val: str):
        ...

    @property
    def LineNumber(self) -> int:
        ...
    @LineNumber.setter
    def LineNumber(self, val: int):
        ...

    @property
    def LinePosition(self) -> int:
        ...
    @LinePosition.setter
    def LinePosition(self, val: int):
        ...

    @property
    def SourceUri(self) -> str:
        ...
    @SourceUri.setter
    def SourceUri(self, val: str):
        ...

    @property
    def Parent(self) -> System.Xml.Schema.XmlSchemaObject:
        ...
    @Parent.setter
    def Parent(self, val: System.Xml.Schema.XmlSchemaObject):
        ...

    @property
    def Namespaces(self) -> System.Xml.Serialization.XmlSerializerNamespaces:
        ...
    @Namespaces.setter
    def Namespaces(self, val: System.Xml.Serialization.XmlSerializerNamespaces):
        ...

    @property
    def IsProcessing(self) -> bool:
        ...
    @IsProcessing.setter
    def IsProcessing(self, val: bool):
        ...

    # methods
    def __init__(self, ):
        ...

    def Validate(self, reader: System.Xml.XmlReader, resolver: System.Xml.XmlResolver, schemaSet: System.Xml.Schema.XmlSchemaSet, valEventHandler: System.Xml.Schema.ValidationEventHandler, ) -> System.Xml.XmlReader:
        ...

    def SetQualifiedName(self, value: System.Xml.XmlQualifiedName, ) -> None:
        ...

    def SetElementType(self, value: System.Xml.Schema.XmlSchemaType, ) -> None:
        ...

    def SetBlockResolved(self, value: int, ) -> None:
        ...

    def SetFinalResolved(self, value: int, ) -> None:
        ...

    @typing.overload
    def Clone(self, ) -> System.Xml.Schema.XmlSchemaObject:
        ...

    @typing.overload
    def Clone(self, parentSchema: System.Xml.Schema.XmlSchema, ) -> System.Xml.Schema.XmlSchemaObject:
        ...

class XmlSchemaObjectEnumerator(System.Collections.IEnumerator, System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def Current(self) -> System.Xml.Schema.XmlSchemaObject:
        ...

    @property
    def Current(self) -> System.Object:
        ...

    # methods
    def __init__(self, enumerator: System.Collections.IEnumerator, ):
        ...

    def Reset(self, ) -> None:
        ...

    def MoveNext(self, ) -> bool:
        ...

    def Reset(self, ) -> None:
        ...

    def MoveNext(self, ) -> bool:
        ...

