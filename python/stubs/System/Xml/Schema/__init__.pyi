from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import System
import System.Xml
import System.Xml.Schema
import System.Collections
import System.Xml.Serialization
import System.IO
import System.Runtime.Serialization
import System.Reflection


class XmlSchemaSet(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def NameTable(self) -> System.Xml.XmlNameTable:
        ...

    @property
    def IsCompiled(self) -> System.Boolean:
        ...

    XmlResolver: System.Xml.XmlResolver = property(None, lambda val: ...)

    @property
    def CompilationSettings(self) -> System.Xml.Schema.XmlSchemaCompilationSettings:
        ...
    @CompilationSettings.setter
    def CompilationSettings(self, val: System.Xml.Schema.XmlSchemaCompilationSettings):
        ...

    @property
    def Count(self) -> System.Int32:
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

    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def __init__(self, nameTable: System.Xml.XmlNameTable, ):
        ...

    @typing.overload
    def Add(self, targetNamespace: System.String, schemaUri: System.String, ) -> System.Xml.Schema.XmlSchema:
        ...

    @typing.overload
    def Add(self, targetNamespace: System.String, schemaDocument: System.Xml.XmlReader, ) -> System.Xml.Schema.XmlSchema:
        ...

    @typing.overload
    def Add(self, schemas: System.Xml.Schema.XmlSchemaSet, ) -> None:
        ...

    @typing.overload
    def Add(self, schema: System.Xml.Schema.XmlSchema, ) -> System.Xml.Schema.XmlSchema:
        ...

    @typing.overload
    def Remove(self, schema: System.Xml.Schema.XmlSchema, ) -> System.Xml.Schema.XmlSchema:
        ...

    @typing.overload
    def RemoveRecursive(self, schemaToRemove: System.Xml.Schema.XmlSchema, ) -> System.Boolean:
        ...

    @typing.overload
    def Contains(self, targetNamespace: System.String, ) -> System.Boolean:
        ...

    @typing.overload
    def Contains(self, schema: System.Xml.Schema.XmlSchema, ) -> System.Boolean:
        ...

    @typing.overload
    def Compile(self, ) -> None:
        ...

    @typing.overload
    def Reprocess(self, schema: System.Xml.Schema.XmlSchema, ) -> System.Xml.Schema.XmlSchema:
        ...

    @typing.overload
    def CopyTo(self, schemas: list[System.Xml.Schema.XmlSchema], index: System.Int32, ) -> None:
        ...

    @typing.overload
    def Schemas(self, ) -> System.Collections.ICollection:
        ...

    @typing.overload
    def Schemas(self, targetNamespace: System.String, ) -> System.Collections.ICollection:
        ...

class XmlSchemaComplexType(System.Xml.Schema.XmlSchemaType):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def IsAbstract(self) -> System.Boolean:
        ...
    @IsAbstract.setter
    def IsAbstract(self, val: System.Boolean):
        ...

    @property
    def Block(self) -> System.Xml.Schema.XmlSchemaDerivationMethod:
        ...
    @Block.setter
    def Block(self, val: System.Xml.Schema.XmlSchemaDerivationMethod):
        ...

    @property
    def IsMixed(self) -> System.Boolean:
        ...
    @IsMixed.setter
    def IsMixed(self, val: System.Boolean):
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
    def ContentType(self) -> System.Xml.Schema.XmlSchemaContentType:
        ...

    @property
    def ContentTypeParticle(self) -> System.Xml.Schema.XmlSchemaParticle:
        ...

    @property
    def BlockResolved(self) -> System.Xml.Schema.XmlSchemaDerivationMethod:
        ...

    @property
    def AttributeUses(self) -> System.Xml.Schema.XmlSchemaObjectTable:
        ...

    @property
    def AttributeWildcard(self) -> System.Xml.Schema.XmlSchemaAnyAttribute:
        ...

    @property
    def Name(self) -> System.String:
        ...
    @Name.setter
    def Name(self, val: System.String):
        ...

    @property
    def Final(self) -> System.Xml.Schema.XmlSchemaDerivationMethod:
        ...
    @Final.setter
    def Final(self, val: System.Xml.Schema.XmlSchemaDerivationMethod):
        ...

    @property
    def QualifiedName(self) -> System.Xml.XmlQualifiedName:
        ...

    @property
    def FinalResolved(self) -> System.Xml.Schema.XmlSchemaDerivationMethod:
        ...

    @property
    def BaseSchemaType(self) -> System.Object:
        ...

    @property
    def BaseXmlSchemaType(self) -> System.Xml.Schema.XmlSchemaType:
        ...

    @property
    def DerivedBy(self) -> System.Xml.Schema.XmlSchemaDerivationMethod:
        ...

    @property
    def Datatype(self) -> System.Xml.Schema.XmlSchemaDatatype:
        ...

    @property
    def TypeCode(self) -> System.Xml.Schema.XmlTypeCode:
        ...

    @property
    def Id(self) -> System.String:
        ...
    @Id.setter
    def Id(self, val: System.String):
        ...

    @property
    def Annotation(self) -> System.Xml.Schema.XmlSchemaAnnotation:
        ...
    @Annotation.setter
    def Annotation(self, val: System.Xml.Schema.XmlSchemaAnnotation):
        ...

    @property
    def UnhandledAttributes(self) -> list[System.Xml.XmlAttribute]:
        ...
    @UnhandledAttributes.setter
    def UnhandledAttributes(self, val: list[System.Xml.XmlAttribute]):
        ...

    @property
    def LineNumber(self) -> System.Int32:
        ...
    @LineNumber.setter
    def LineNumber(self, val: System.Int32):
        ...

    @property
    def LinePosition(self) -> System.Int32:
        ...
    @LinePosition.setter
    def LinePosition(self, val: System.Int32):
        ...

    @property
    def SourceUri(self) -> System.String:
        ...
    @SourceUri.setter
    def SourceUri(self, val: System.String):
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

    # methods
    @typing.overload
    def __init__(self, ):
        ...

class XmlSchema(System.Xml.Schema.XmlSchemaObject):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def AttributeFormDefault(self) -> System.Xml.Schema.XmlSchemaForm:
        ...
    @AttributeFormDefault.setter
    def AttributeFormDefault(self, val: System.Xml.Schema.XmlSchemaForm):
        ...

    @property
    def BlockDefault(self) -> System.Xml.Schema.XmlSchemaDerivationMethod:
        ...
    @BlockDefault.setter
    def BlockDefault(self, val: System.Xml.Schema.XmlSchemaDerivationMethod):
        ...

    @property
    def FinalDefault(self) -> System.Xml.Schema.XmlSchemaDerivationMethod:
        ...
    @FinalDefault.setter
    def FinalDefault(self, val: System.Xml.Schema.XmlSchemaDerivationMethod):
        ...

    @property
    def ElementFormDefault(self) -> System.Xml.Schema.XmlSchemaForm:
        ...
    @ElementFormDefault.setter
    def ElementFormDefault(self, val: System.Xml.Schema.XmlSchemaForm):
        ...

    @property
    def TargetNamespace(self) -> System.String:
        ...
    @TargetNamespace.setter
    def TargetNamespace(self, val: System.String):
        ...

    @property
    def Version(self) -> System.String:
        ...
    @Version.setter
    def Version(self, val: System.String):
        ...

    @property
    def Includes(self) -> System.Xml.Schema.XmlSchemaObjectCollection:
        ...

    @property
    def Items(self) -> System.Xml.Schema.XmlSchemaObjectCollection:
        ...

    @property
    def IsCompiled(self) -> System.Boolean:
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
    def Id(self) -> System.String:
        ...
    @Id.setter
    def Id(self, val: System.String):
        ...

    @property
    def UnhandledAttributes(self) -> list[System.Xml.XmlAttribute]:
        ...
    @UnhandledAttributes.setter
    def UnhandledAttributes(self, val: list[System.Xml.XmlAttribute]):
        ...

    @property
    def Groups(self) -> System.Xml.Schema.XmlSchemaObjectTable:
        ...

    @property
    def Notations(self) -> System.Xml.Schema.XmlSchemaObjectTable:
        ...

    @property
    def LineNumber(self) -> System.Int32:
        ...
    @LineNumber.setter
    def LineNumber(self, val: System.Int32):
        ...

    @property
    def LinePosition(self) -> System.Int32:
        ...
    @LinePosition.setter
    def LinePosition(self, val: System.Int32):
        ...

    @property
    def SourceUri(self) -> System.String:
        ...
    @SourceUri.setter
    def SourceUri(self, val: System.String):
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

    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    @staticmethod
    def Read(reader: System.IO.TextReader, validationEventHandler: System.Xml.Schema.ValidationEventHandler, ) -> System.Xml.Schema.XmlSchema:
        ...

    @typing.overload
    @staticmethod
    def Read(stream: System.IO.Stream, validationEventHandler: System.Xml.Schema.ValidationEventHandler, ) -> System.Xml.Schema.XmlSchema:
        ...

    @typing.overload
    @staticmethod
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

class IXmlSchemaInfo(abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @abc.abstractmethod
    @property
    def Validity(self) -> System.Xml.Schema.XmlSchemaValidity:
        ...

    @abc.abstractmethod
    @property
    def IsDefault(self) -> System.Boolean:
        ...

    @abc.abstractmethod
    @property
    def IsNil(self) -> System.Boolean:
        ...

    @abc.abstractmethod
    @property
    def MemberType(self) -> System.Xml.Schema.XmlSchemaSimpleType:
        ...

    @abc.abstractmethod
    @property
    def SchemaType(self) -> System.Xml.Schema.XmlSchemaType:
        ...

    @abc.abstractmethod
    @property
    def SchemaElement(self) -> System.Xml.Schema.XmlSchemaElement:
        ...

    @abc.abstractmethod
    @property
    def SchemaAttribute(self) -> System.Xml.Schema.XmlSchemaAttribute:
        ...

    # methods
class XmlSchemaCompilationSettings(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def EnableUpaCheck(self) -> System.Boolean:
        ...
    @EnableUpaCheck.setter
    def EnableUpaCheck(self, val: System.Boolean):
        ...

    # methods
    @typing.overload
    def __init__(self, ):
        ...

class XmlSchemaObjectTable(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def Count(self) -> System.Int32:
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
    @typing.overload
    def Contains(self, name: System.Xml.XmlQualifiedName, ) -> System.Boolean:
        ...

    @typing.overload
    def GetEnumerator(self, ) -> System.Collections.IDictionaryEnumerator:
        ...

class XmlSchemaType(System.Xml.Schema.XmlSchemaAnnotated):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def Name(self) -> System.String:
        ...
    @Name.setter
    def Name(self, val: System.String):
        ...

    @property
    def Final(self) -> System.Xml.Schema.XmlSchemaDerivationMethod:
        ...
    @Final.setter
    def Final(self, val: System.Xml.Schema.XmlSchemaDerivationMethod):
        ...

    @property
    def QualifiedName(self) -> System.Xml.XmlQualifiedName:
        ...

    @property
    def FinalResolved(self) -> System.Xml.Schema.XmlSchemaDerivationMethod:
        ...

    @property
    def BaseSchemaType(self) -> System.Object:
        ...

    @property
    def BaseXmlSchemaType(self) -> System.Xml.Schema.XmlSchemaType:
        ...

    @property
    def DerivedBy(self) -> System.Xml.Schema.XmlSchemaDerivationMethod:
        ...

    @property
    def Datatype(self) -> System.Xml.Schema.XmlSchemaDatatype:
        ...

    @property
    def IsMixed(self) -> System.Boolean:
        ...
    @IsMixed.setter
    def IsMixed(self, val: System.Boolean):
        ...

    @property
    def TypeCode(self) -> System.Xml.Schema.XmlTypeCode:
        ...

    @property
    def Id(self) -> System.String:
        ...
    @Id.setter
    def Id(self, val: System.String):
        ...

    @property
    def Annotation(self) -> System.Xml.Schema.XmlSchemaAnnotation:
        ...
    @Annotation.setter
    def Annotation(self, val: System.Xml.Schema.XmlSchemaAnnotation):
        ...

    @property
    def UnhandledAttributes(self) -> list[System.Xml.XmlAttribute]:
        ...
    @UnhandledAttributes.setter
    def UnhandledAttributes(self, val: list[System.Xml.XmlAttribute]):
        ...

    @property
    def LineNumber(self) -> System.Int32:
        ...
    @LineNumber.setter
    def LineNumber(self, val: System.Int32):
        ...

    @property
    def LinePosition(self) -> System.Int32:
        ...
    @LinePosition.setter
    def LinePosition(self, val: System.Int32):
        ...

    @property
    def SourceUri(self) -> System.String:
        ...
    @SourceUri.setter
    def SourceUri(self, val: System.String):
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

    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    @staticmethod
    def GetBuiltInSimpleType(qualifiedName: System.Xml.XmlQualifiedName, ) -> System.Xml.Schema.XmlSchemaSimpleType:
        ...

    @typing.overload
    @staticmethod
    def GetBuiltInSimpleType(typeCode: System.Xml.Schema.XmlTypeCode, ) -> System.Xml.Schema.XmlSchemaSimpleType:
        ...

    @typing.overload
    @staticmethod
    def GetBuiltInComplexType(typeCode: System.Xml.Schema.XmlTypeCode, ) -> System.Xml.Schema.XmlSchemaComplexType:
        ...

    @typing.overload
    @staticmethod
    def GetBuiltInComplexType(qualifiedName: System.Xml.XmlQualifiedName, ) -> System.Xml.Schema.XmlSchemaComplexType:
        ...

    @typing.overload
    @staticmethod
    def IsDerivedFrom(derivedType: System.Xml.Schema.XmlSchemaType, baseType: System.Xml.Schema.XmlSchemaType, except_: System.Xml.Schema.XmlSchemaDerivationMethod, ) -> System.Boolean:
        ...

class XmlSchemaDerivationMethod(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    Empty: System.Int32 = Empty
    Substitution: System.Int32 = Substitution
    Extension: System.Int32 = Extension
    Restriction: System.Int32 = Restriction
    List: System.Int32 = List
    Union: System.Int32 = Union
    All: System.Int32 = All
    None_: System.Int32 = None

class XmlSchemaContentModel(System.Xml.Schema.XmlSchemaAnnotated, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @abc.abstractmethod
    @property
    def Content(self) -> System.Xml.Schema.XmlSchemaContent:
        ...
    @abc.abstractmethod
    @Content.setter
    def Content(self, val: System.Xml.Schema.XmlSchemaContent):
        ...

    @property
    def Id(self) -> System.String:
        ...
    @Id.setter
    def Id(self, val: System.String):
        ...

    @property
    def Annotation(self) -> System.Xml.Schema.XmlSchemaAnnotation:
        ...
    @Annotation.setter
    def Annotation(self, val: System.Xml.Schema.XmlSchemaAnnotation):
        ...

    @property
    def UnhandledAttributes(self) -> list[System.Xml.XmlAttribute]:
        ...
    @UnhandledAttributes.setter
    def UnhandledAttributes(self, val: list[System.Xml.XmlAttribute]):
        ...

    @property
    def LineNumber(self) -> System.Int32:
        ...
    @LineNumber.setter
    def LineNumber(self, val: System.Int32):
        ...

    @property
    def LinePosition(self) -> System.Int32:
        ...
    @LinePosition.setter
    def LinePosition(self, val: System.Int32):
        ...

    @property
    def SourceUri(self) -> System.String:
        ...
    @SourceUri.setter
    def SourceUri(self, val: System.String):
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

    # methods
class XmlSchemaParticle(System.Xml.Schema.XmlSchemaAnnotated, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def MinOccursString(self) -> System.String:
        ...
    @MinOccursString.setter
    def MinOccursString(self, val: System.String):
        ...

    @property
    def MaxOccursString(self) -> System.String:
        ...
    @MaxOccursString.setter
    def MaxOccursString(self, val: System.String):
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
    def Id(self) -> System.String:
        ...
    @Id.setter
    def Id(self, val: System.String):
        ...

    @property
    def Annotation(self) -> System.Xml.Schema.XmlSchemaAnnotation:
        ...
    @Annotation.setter
    def Annotation(self, val: System.Xml.Schema.XmlSchemaAnnotation):
        ...

    @property
    def UnhandledAttributes(self) -> list[System.Xml.XmlAttribute]:
        ...
    @UnhandledAttributes.setter
    def UnhandledAttributes(self, val: list[System.Xml.XmlAttribute]):
        ...

    @property
    def LineNumber(self) -> System.Int32:
        ...
    @LineNumber.setter
    def LineNumber(self, val: System.Int32):
        ...

    @property
    def LinePosition(self) -> System.Int32:
        ...
    @LinePosition.setter
    def LinePosition(self, val: System.Int32):
        ...

    @property
    def SourceUri(self) -> System.String:
        ...
    @SourceUri.setter
    def SourceUri(self, val: System.String):
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

    # methods
class XmlSchemaObjectCollection(System.Collections.IList, System.Collections.ICollection, System.Collections.IEnumerable, System.Collections.CollectionBase):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def Item(self) -> System.Xml.Schema.XmlSchemaObject:
        ...
    @Item.setter
    def Item(self, val: System.Xml.Schema.XmlSchemaObject):
        ...

    @property
    def Capacity(self) -> System.Int32:
        ...
    @Capacity.setter
    def Capacity(self, val: System.Int32):
        ...

    @property
    def Count(self) -> System.Int32:
        ...

    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def __init__(self, parent: System.Xml.Schema.XmlSchemaObject, ):
        ...

    @typing.overload
    def GetEnumerator(self, ) -> System.Xml.Schema.XmlSchemaObjectEnumerator:
        ...

    @typing.overload
    def Add(self, item: System.Xml.Schema.XmlSchemaObject, ) -> System.Int32:
        ...

    @typing.overload
    def Insert(self, index: System.Int32, item: System.Xml.Schema.XmlSchemaObject, ) -> None:
        ...

    @typing.overload
    def IndexOf(self, item: System.Xml.Schema.XmlSchemaObject, ) -> System.Int32:
        ...

    @typing.overload
    def Contains(self, item: System.Xml.Schema.XmlSchemaObject, ) -> System.Boolean:
        ...

    @typing.overload
    def Remove(self, item: System.Xml.Schema.XmlSchemaObject, ) -> None:
        ...

    @typing.overload
    def CopyTo(self, array: list[System.Xml.Schema.XmlSchemaObject], index: System.Int32, ) -> None:
        ...

class XmlSchemaAnyAttribute(System.Xml.Schema.XmlSchemaAnnotated):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def Namespace(self) -> System.String:
        ...
    @Namespace.setter
    def Namespace(self, val: System.String):
        ...

    @property
    def ProcessContents(self) -> System.Xml.Schema.XmlSchemaContentProcessing:
        ...
    @ProcessContents.setter
    def ProcessContents(self, val: System.Xml.Schema.XmlSchemaContentProcessing):
        ...

    @property
    def Id(self) -> System.String:
        ...
    @Id.setter
    def Id(self, val: System.String):
        ...

    @property
    def Annotation(self) -> System.Xml.Schema.XmlSchemaAnnotation:
        ...
    @Annotation.setter
    def Annotation(self, val: System.Xml.Schema.XmlSchemaAnnotation):
        ...

    @property
    def UnhandledAttributes(self) -> list[System.Xml.XmlAttribute]:
        ...
    @UnhandledAttributes.setter
    def UnhandledAttributes(self, val: list[System.Xml.XmlAttribute]):
        ...

    @property
    def LineNumber(self) -> System.Int32:
        ...
    @LineNumber.setter
    def LineNumber(self, val: System.Int32):
        ...

    @property
    def LinePosition(self) -> System.Int32:
        ...
    @LinePosition.setter
    def LinePosition(self, val: System.Int32):
        ...

    @property
    def SourceUri(self) -> System.String:
        ...
    @SourceUri.setter
    def SourceUri(self, val: System.String):
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

    # methods
    @typing.overload
    def __init__(self, ):
        ...

class XmlSchemaContentType(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    TextOnly: System.Int32 = TextOnly
    Empty: System.Int32 = Empty
    ElementOnly: System.Int32 = ElementOnly
    Mixed: System.Int32 = Mixed

class XmlSchemaDatatype(System.Object, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @abc.abstractmethod
    @property
    def ValueType(self) -> System.Type:
        ...

    @abc.abstractmethod
    @property
    def TokenizedType(self) -> System.Xml.XmlTokenizedType:
        ...

    @property
    def Variety(self) -> System.Xml.Schema.XmlSchemaDatatypeVariety:
        ...

    @property
    def TypeCode(self) -> System.Xml.Schema.XmlTypeCode:
        ...

    # methods
    @typing.overload
    @abc.abstractmethod
    def ParseValue(self, s: System.String, nameTable: System.Xml.XmlNameTable, nsmgr: System.Xml.IXmlNamespaceResolver, ) -> System.Object:
        ...

    @typing.overload
    def ChangeType(self, value: System.Object, targetType: System.Type, ) -> System.Object:
        ...

    @typing.overload
    def ChangeType(self, value: System.Object, targetType: System.Type, namespaceResolver: System.Xml.IXmlNamespaceResolver, ) -> System.Object:
        ...

    @typing.overload
    def IsDerivedFrom(self, datatype: System.Xml.Schema.XmlSchemaDatatype, ) -> System.Boolean:
        ...

class XmlTypeCode(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    None_: System.Int32 = None
    Item: System.Int32 = Item
    Node: System.Int32 = Node
    Document: System.Int32 = Document
    Element: System.Int32 = Element
    Attribute: System.Int32 = Attribute
    Namespace: System.Int32 = Namespace
    ProcessingInstruction: System.Int32 = ProcessingInstruction
    Comment: System.Int32 = Comment
    Text: System.Int32 = Text
    AnyAtomicType: System.Int32 = AnyAtomicType
    UntypedAtomic: System.Int32 = UntypedAtomic
    String: System.Int32 = String
    Boolean: System.Int32 = Boolean
    Decimal: System.Int32 = Decimal
    Float: System.Int32 = Float
    Double: System.Int32 = Double
    Duration: System.Int32 = Duration
    DateTime: System.Int32 = DateTime
    Time: System.Int32 = Time
    Date: System.Int32 = Date
    GYearMonth: System.Int32 = GYearMonth
    GYear: System.Int32 = GYear
    GMonthDay: System.Int32 = GMonthDay
    GDay: System.Int32 = GDay
    GMonth: System.Int32 = GMonth
    HexBinary: System.Int32 = HexBinary
    Base64Binary: System.Int32 = Base64Binary
    AnyUri: System.Int32 = AnyUri
    QName: System.Int32 = QName
    Notation: System.Int32 = Notation
    NormalizedString: System.Int32 = NormalizedString
    Token: System.Int32 = Token
    Language: System.Int32 = Language
    NmToken: System.Int32 = NmToken
    Name: System.Int32 = Name
    NCName: System.Int32 = NCName
    Id: System.Int32 = Id
    Idref: System.Int32 = Idref
    Entity: System.Int32 = Entity
    Integer: System.Int32 = Integer
    NonPositiveInteger: System.Int32 = NonPositiveInteger
    NegativeInteger: System.Int32 = NegativeInteger
    Long: System.Int32 = Long
    Int: System.Int32 = Int
    Short: System.Int32 = Short
    Byte: System.Int32 = Byte
    NonNegativeInteger: System.Int32 = NonNegativeInteger
    UnsignedLong: System.Int32 = UnsignedLong
    UnsignedInt: System.Int32 = UnsignedInt
    UnsignedShort: System.Int32 = UnsignedShort
    UnsignedByte: System.Int32 = UnsignedByte
    PositiveInteger: System.Int32 = PositiveInteger
    YearMonthDuration: System.Int32 = YearMonthDuration
    DayTimeDuration: System.Int32 = DayTimeDuration

class XmlSchemaAnnotation(System.Xml.Schema.XmlSchemaObject):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def Id(self) -> System.String:
        ...
    @Id.setter
    def Id(self, val: System.String):
        ...

    @property
    def Items(self) -> System.Xml.Schema.XmlSchemaObjectCollection:
        ...

    @property
    def UnhandledAttributes(self) -> list[System.Xml.XmlAttribute]:
        ...
    @UnhandledAttributes.setter
    def UnhandledAttributes(self, val: list[System.Xml.XmlAttribute]):
        ...

    @property
    def LineNumber(self) -> System.Int32:
        ...
    @LineNumber.setter
    def LineNumber(self, val: System.Int32):
        ...

    @property
    def LinePosition(self) -> System.Int32:
        ...
    @LinePosition.setter
    def LinePosition(self, val: System.Int32):
        ...

    @property
    def SourceUri(self) -> System.String:
        ...
    @SourceUri.setter
    def SourceUri(self, val: System.String):
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

    # methods
    @typing.overload
    def __init__(self, ):
        ...

class XmlSchemaObject(System.Object, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def LineNumber(self) -> System.Int32:
        ...
    @LineNumber.setter
    def LineNumber(self, val: System.Int32):
        ...

    @property
    def LinePosition(self) -> System.Int32:
        ...
    @LinePosition.setter
    def LinePosition(self, val: System.Int32):
        ...

    @property
    def SourceUri(self) -> System.String:
        ...
    @SourceUri.setter
    def SourceUri(self, val: System.String):
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

    # methods
class XmlSchemaForm(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    None_: System.Int32 = None
    Qualified: System.Int32 = Qualified
    Unqualified: System.Int32 = Unqualified

class ValidationEventHandler(System.ICloneable, System.Runtime.Serialization.ISerializable, System.MulticastDelegate):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def Target(self) -> System.Object:
        ...

    @property
    def Method(self) -> System.Reflection.MethodInfo:
        ...

    # methods
    @typing.overload
    def __init__(self, object: System.Object, method: System.IntPtr, ):
        ...

    @typing.overload
    def Invoke(self, sender: System.Object, e: System.Xml.Schema.ValidationEventArgs, ) -> None:
        ...

    @typing.overload
    def BeginInvoke(self, sender: System.Object, e: System.Xml.Schema.ValidationEventArgs, callback: System.AsyncCallback, object: System.Object, ) -> System.IAsyncResult:
        ...

    @typing.overload
    def EndInvoke(self, result: System.IAsyncResult, ) -> None:
        ...

class XmlSchemaValidationFlags(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    None_: System.Int32 = None
    ProcessInlineSchema: System.Int32 = ProcessInlineSchema
    ProcessSchemaLocation: System.Int32 = ProcessSchemaLocation
    ReportValidationWarnings: System.Int32 = ReportValidationWarnings
    ProcessIdentityConstraints: System.Int32 = ProcessIdentityConstraints
    AllowXmlAttributes: System.Int32 = AllowXmlAttributes

class XmlSchemaValidity(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    NotKnown: System.Int32 = NotKnown
    Valid: System.Int32 = Valid
    Invalid: System.Int32 = Invalid

class XmlSchemaSimpleType(System.Xml.Schema.XmlSchemaType):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def Content(self) -> System.Xml.Schema.XmlSchemaSimpleTypeContent:
        ...
    @Content.setter
    def Content(self, val: System.Xml.Schema.XmlSchemaSimpleTypeContent):
        ...

    @property
    def Name(self) -> System.String:
        ...
    @Name.setter
    def Name(self, val: System.String):
        ...

    @property
    def Final(self) -> System.Xml.Schema.XmlSchemaDerivationMethod:
        ...
    @Final.setter
    def Final(self, val: System.Xml.Schema.XmlSchemaDerivationMethod):
        ...

    @property
    def QualifiedName(self) -> System.Xml.XmlQualifiedName:
        ...

    @property
    def FinalResolved(self) -> System.Xml.Schema.XmlSchemaDerivationMethod:
        ...

    @property
    def BaseSchemaType(self) -> System.Object:
        ...

    @property
    def BaseXmlSchemaType(self) -> System.Xml.Schema.XmlSchemaType:
        ...

    @property
    def DerivedBy(self) -> System.Xml.Schema.XmlSchemaDerivationMethod:
        ...

    @property
    def Datatype(self) -> System.Xml.Schema.XmlSchemaDatatype:
        ...

    @property
    def IsMixed(self) -> System.Boolean:
        ...
    @IsMixed.setter
    def IsMixed(self, val: System.Boolean):
        ...

    @property
    def TypeCode(self) -> System.Xml.Schema.XmlTypeCode:
        ...

    @property
    def Id(self) -> System.String:
        ...
    @Id.setter
    def Id(self, val: System.String):
        ...

    @property
    def Annotation(self) -> System.Xml.Schema.XmlSchemaAnnotation:
        ...
    @Annotation.setter
    def Annotation(self, val: System.Xml.Schema.XmlSchemaAnnotation):
        ...

    @property
    def UnhandledAttributes(self) -> list[System.Xml.XmlAttribute]:
        ...
    @UnhandledAttributes.setter
    def UnhandledAttributes(self, val: list[System.Xml.XmlAttribute]):
        ...

    @property
    def LineNumber(self) -> System.Int32:
        ...
    @LineNumber.setter
    def LineNumber(self, val: System.Int32):
        ...

    @property
    def LinePosition(self) -> System.Int32:
        ...
    @LinePosition.setter
    def LinePosition(self, val: System.Int32):
        ...

    @property
    def SourceUri(self) -> System.String:
        ...
    @SourceUri.setter
    def SourceUri(self, val: System.String):
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

    # methods
    @typing.overload
    def __init__(self, ):
        ...

class XmlSchemaElement(System.Xml.Schema.XmlSchemaParticle):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def IsAbstract(self) -> System.Boolean:
        ...
    @IsAbstract.setter
    def IsAbstract(self, val: System.Boolean):
        ...

    @property
    def Block(self) -> System.Xml.Schema.XmlSchemaDerivationMethod:
        ...
    @Block.setter
    def Block(self, val: System.Xml.Schema.XmlSchemaDerivationMethod):
        ...

    @property
    def DefaultValue(self) -> System.String:
        ...
    @DefaultValue.setter
    def DefaultValue(self, val: System.String):
        ...

    @property
    def Final(self) -> System.Xml.Schema.XmlSchemaDerivationMethod:
        ...
    @Final.setter
    def Final(self, val: System.Xml.Schema.XmlSchemaDerivationMethod):
        ...

    @property
    def FixedValue(self) -> System.String:
        ...
    @FixedValue.setter
    def FixedValue(self, val: System.String):
        ...

    @property
    def Form(self) -> System.Xml.Schema.XmlSchemaForm:
        ...
    @Form.setter
    def Form(self, val: System.Xml.Schema.XmlSchemaForm):
        ...

    @property
    def Name(self) -> System.String:
        ...
    @Name.setter
    def Name(self, val: System.String):
        ...

    @property
    def IsNillable(self) -> System.Boolean:
        ...
    @IsNillable.setter
    def IsNillable(self, val: System.Boolean):
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
    def BlockResolved(self) -> System.Xml.Schema.XmlSchemaDerivationMethod:
        ...

    @property
    def FinalResolved(self) -> System.Xml.Schema.XmlSchemaDerivationMethod:
        ...

    @property
    def MinOccursString(self) -> System.String:
        ...
    @MinOccursString.setter
    def MinOccursString(self, val: System.String):
        ...

    @property
    def MaxOccursString(self) -> System.String:
        ...
    @MaxOccursString.setter
    def MaxOccursString(self, val: System.String):
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
    def Id(self) -> System.String:
        ...
    @Id.setter
    def Id(self, val: System.String):
        ...

    @property
    def Annotation(self) -> System.Xml.Schema.XmlSchemaAnnotation:
        ...
    @Annotation.setter
    def Annotation(self, val: System.Xml.Schema.XmlSchemaAnnotation):
        ...

    @property
    def UnhandledAttributes(self) -> list[System.Xml.XmlAttribute]:
        ...
    @UnhandledAttributes.setter
    def UnhandledAttributes(self, val: list[System.Xml.XmlAttribute]):
        ...

    @property
    def LineNumber(self) -> System.Int32:
        ...
    @LineNumber.setter
    def LineNumber(self, val: System.Int32):
        ...

    @property
    def LinePosition(self) -> System.Int32:
        ...
    @LinePosition.setter
    def LinePosition(self, val: System.Int32):
        ...

    @property
    def SourceUri(self) -> System.String:
        ...
    @SourceUri.setter
    def SourceUri(self, val: System.String):
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

    # methods
    @typing.overload
    def __init__(self, ):
        ...

class XmlSchemaAttribute(System.Xml.Schema.XmlSchemaAnnotated):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def DefaultValue(self) -> System.String:
        ...
    @DefaultValue.setter
    def DefaultValue(self, val: System.String):
        ...

    @property
    def FixedValue(self) -> System.String:
        ...
    @FixedValue.setter
    def FixedValue(self, val: System.String):
        ...

    @property
    def Form(self) -> System.Xml.Schema.XmlSchemaForm:
        ...
    @Form.setter
    def Form(self, val: System.Xml.Schema.XmlSchemaForm):
        ...

    @property
    def Name(self) -> System.String:
        ...
    @Name.setter
    def Name(self, val: System.String):
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
    def Use(self) -> System.Xml.Schema.XmlSchemaUse:
        ...
    @Use.setter
    def Use(self, val: System.Xml.Schema.XmlSchemaUse):
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
    def Id(self) -> System.String:
        ...
    @Id.setter
    def Id(self, val: System.String):
        ...

    @property
    def Annotation(self) -> System.Xml.Schema.XmlSchemaAnnotation:
        ...
    @Annotation.setter
    def Annotation(self, val: System.Xml.Schema.XmlSchemaAnnotation):
        ...

    @property
    def UnhandledAttributes(self) -> list[System.Xml.XmlAttribute]:
        ...
    @UnhandledAttributes.setter
    def UnhandledAttributes(self, val: list[System.Xml.XmlAttribute]):
        ...

    @property
    def LineNumber(self) -> System.Int32:
        ...
    @LineNumber.setter
    def LineNumber(self, val: System.Int32):
        ...

    @property
    def LinePosition(self) -> System.Int32:
        ...
    @LinePosition.setter
    def LinePosition(self, val: System.Int32):
        ...

    @property
    def SourceUri(self) -> System.String:
        ...
    @SourceUri.setter
    def SourceUri(self, val: System.String):
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

    # methods
    @typing.overload
    def __init__(self, ):
        ...

class XmlSchemaAnnotated(System.Xml.Schema.XmlSchemaObject):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def Id(self) -> System.String:
        ...
    @Id.setter
    def Id(self, val: System.String):
        ...

    @property
    def Annotation(self) -> System.Xml.Schema.XmlSchemaAnnotation:
        ...
    @Annotation.setter
    def Annotation(self, val: System.Xml.Schema.XmlSchemaAnnotation):
        ...

    @property
    def UnhandledAttributes(self) -> list[System.Xml.XmlAttribute]:
        ...
    @UnhandledAttributes.setter
    def UnhandledAttributes(self, val: list[System.Xml.XmlAttribute]):
        ...

    @property
    def LineNumber(self) -> System.Int32:
        ...
    @LineNumber.setter
    def LineNumber(self, val: System.Int32):
        ...

    @property
    def LinePosition(self) -> System.Int32:
        ...
    @LinePosition.setter
    def LinePosition(self, val: System.Int32):
        ...

    @property
    def SourceUri(self) -> System.String:
        ...
    @SourceUri.setter
    def SourceUri(self, val: System.String):
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

    # methods
    @typing.overload
    def __init__(self, ):
        ...

class XmlSchemaContent(System.Xml.Schema.XmlSchemaAnnotated, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def Id(self) -> System.String:
        ...
    @Id.setter
    def Id(self, val: System.String):
        ...

    @property
    def Annotation(self) -> System.Xml.Schema.XmlSchemaAnnotation:
        ...
    @Annotation.setter
    def Annotation(self, val: System.Xml.Schema.XmlSchemaAnnotation):
        ...

    @property
    def UnhandledAttributes(self) -> list[System.Xml.XmlAttribute]:
        ...
    @UnhandledAttributes.setter
    def UnhandledAttributes(self, val: list[System.Xml.XmlAttribute]):
        ...

    @property
    def LineNumber(self) -> System.Int32:
        ...
    @LineNumber.setter
    def LineNumber(self, val: System.Int32):
        ...

    @property
    def LinePosition(self) -> System.Int32:
        ...
    @LinePosition.setter
    def LinePosition(self, val: System.Int32):
        ...

    @property
    def SourceUri(self) -> System.String:
        ...
    @SourceUri.setter
    def SourceUri(self, val: System.String):
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

    # methods
class XmlSchemaObjectEnumerator(System.Collections.IEnumerator, System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def Current(self) -> System.Xml.Schema.XmlSchemaObject:
        ...

    # methods
    @typing.overload
    def Reset(self, ) -> None:
        ...

    @typing.overload
    def MoveNext(self, ) -> System.Boolean:
        ...

class XmlSchemaContentProcessing(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    None_: System.Int32 = None
    Skip: System.Int32 = Skip
    Lax: System.Int32 = Lax
    Strict: System.Int32 = Strict

class XmlSchemaDatatypeVariety(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    Atomic: System.Int32 = Atomic
    List: System.Int32 = List
    Union: System.Int32 = Union

class ValidationEventArgs(System.EventArgs):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def Severity(self) -> System.Xml.Schema.XmlSeverityType:
        ...

    @property
    def Exception(self) -> System.Xml.Schema.XmlSchemaException:
        ...

    @property
    def Message(self) -> System.String:
        ...

    # methods
class XmlSchemaSimpleTypeContent(System.Xml.Schema.XmlSchemaAnnotated, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def Id(self) -> System.String:
        ...
    @Id.setter
    def Id(self, val: System.String):
        ...

    @property
    def Annotation(self) -> System.Xml.Schema.XmlSchemaAnnotation:
        ...
    @Annotation.setter
    def Annotation(self, val: System.Xml.Schema.XmlSchemaAnnotation):
        ...

    @property
    def UnhandledAttributes(self) -> list[System.Xml.XmlAttribute]:
        ...
    @UnhandledAttributes.setter
    def UnhandledAttributes(self, val: list[System.Xml.XmlAttribute]):
        ...

    @property
    def LineNumber(self) -> System.Int32:
        ...
    @LineNumber.setter
    def LineNumber(self, val: System.Int32):
        ...

    @property
    def LinePosition(self) -> System.Int32:
        ...
    @LinePosition.setter
    def LinePosition(self, val: System.Int32):
        ...

    @property
    def SourceUri(self) -> System.String:
        ...
    @SourceUri.setter
    def SourceUri(self, val: System.String):
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

    # methods
class XmlSchemaUse(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    None_: System.Int32 = None
    Optional: System.Int32 = Optional
    Prohibited: System.Int32 = Prohibited
    Required: System.Int32 = Required

class XmlSeverityType(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    Error: System.Int32 = Error
    Warning: System.Int32 = Warning

class XmlSchemaException(System.Runtime.Serialization.ISerializable, System.SystemException):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def SourceUri(self) -> System.String:
        ...

    @property
    def LineNumber(self) -> System.Int32:
        ...

    @property
    def LinePosition(self) -> System.Int32:
        ...

    @property
    def SourceSchemaObject(self) -> System.Xml.Schema.XmlSchemaObject:
        ...

    @property
    def Message(self) -> System.String:
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
    def HelpLink(self) -> System.String:
        ...
    @HelpLink.setter
    def HelpLink(self, val: System.String):
        ...

    @property
    def Source(self) -> System.String:
        ...
    @Source.setter
    def Source(self, val: System.String):
        ...

    @property
    def HResult(self) -> System.Int32:
        ...
    @HResult.setter
    def HResult(self, val: System.Int32):
        ...

    @property
    def StackTrace(self) -> System.String:
        ...

    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def __init__(self, message: System.String, ):
        ...

    @typing.overload
    def __init__(self, message: System.String, innerException: System.Exception, ):
        ...

    @typing.overload
    def __init__(self, message: System.String, innerException: System.Exception, lineNumber: System.Int32, linePosition: System.Int32, ):
        ...

    @typing.overload
    def GetObjectData(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext, ) -> None:
        ...

