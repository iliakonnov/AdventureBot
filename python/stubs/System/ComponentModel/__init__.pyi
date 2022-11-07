from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import System
import System.ComponentModel
import System.Globalization
import System.Collections
import System.ComponentModel.TypeConverter
import System.Runtime.Serialization
import System.Reflection
import System.ComponentModel.EventHandlerList


class DesignerSerializationVisibility(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    Hidden: int = ...
    Visible: int = ...
    Content: int = ...

class TypeConverter(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    def __init__(self, ):
        ...

    @typing.overload
    def CanConvertFrom(self, sourceType: System.Type, ) -> bool:
        ...

    @typing.overload
    def CanConvertFrom(self, context: System.ComponentModel.ITypeDescriptorContext, sourceType: System.Type, ) -> bool:
        ...

    @typing.overload
    def CanConvertTo(self, destinationType: System.Type, ) -> bool:
        ...

    @typing.overload
    def CanConvertTo(self, context: System.ComponentModel.ITypeDescriptorContext, destinationType: System.Type, ) -> bool:
        ...

    @typing.overload
    def ConvertFrom(self, value: System.Object, ) -> System.Object:
        ...

    @typing.overload
    def ConvertFrom(self, context: System.ComponentModel.ITypeDescriptorContext, culture: System.Globalization.CultureInfo, value: System.Object, ) -> System.Object:
        ...

    @typing.overload
    def ConvertFromInvariantString(self, text: str, ) -> System.Object:
        ...

    @typing.overload
    def ConvertFromInvariantString(self, context: System.ComponentModel.ITypeDescriptorContext, text: str, ) -> System.Object:
        ...

    @typing.overload
    def ConvertFromString(self, text: str, ) -> System.Object:
        ...

    @typing.overload
    def ConvertFromString(self, context: System.ComponentModel.ITypeDescriptorContext, text: str, ) -> System.Object:
        ...

    @typing.overload
    def ConvertFromString(self, context: System.ComponentModel.ITypeDescriptorContext, culture: System.Globalization.CultureInfo, text: str, ) -> System.Object:
        ...

    @typing.overload
    def ConvertTo(self, value: System.Object, destinationType: System.Type, ) -> System.Object:
        ...

    @typing.overload
    def ConvertTo(self, context: System.ComponentModel.ITypeDescriptorContext, culture: System.Globalization.CultureInfo, value: System.Object, destinationType: System.Type, ) -> System.Object:
        ...

    @typing.overload
    def ConvertToInvariantString(self, value: System.Object, ) -> str:
        ...

    @typing.overload
    def ConvertToInvariantString(self, context: System.ComponentModel.ITypeDescriptorContext, value: System.Object, ) -> str:
        ...

    @typing.overload
    def ConvertToString(self, value: System.Object, ) -> str:
        ...

    @typing.overload
    def ConvertToString(self, context: System.ComponentModel.ITypeDescriptorContext, value: System.Object, ) -> str:
        ...

    @typing.overload
    def ConvertToString(self, context: System.ComponentModel.ITypeDescriptorContext, culture: System.Globalization.CultureInfo, value: System.Object, ) -> str:
        ...

    @typing.overload
    def CreateInstance(self, propertyValues: System.Collections.IDictionary, ) -> System.Object:
        ...

    @typing.overload
    def CreateInstance(self, context: System.ComponentModel.ITypeDescriptorContext, propertyValues: System.Collections.IDictionary, ) -> System.Object:
        ...

    def GetConvertFromException(self, value: System.Object, ) -> System.Exception:
        ...

    def GetConvertToException(self, value: System.Object, destinationType: System.Type, ) -> System.Exception:
        ...

    @typing.overload
    def GetCreateInstanceSupported(self, ) -> bool:
        ...

    @typing.overload
    def GetCreateInstanceSupported(self, context: System.ComponentModel.ITypeDescriptorContext, ) -> bool:
        ...

    @typing.overload
    def GetProperties(self, value: System.Object, ) -> System.ComponentModel.PropertyDescriptorCollection:
        ...

    @typing.overload
    def GetProperties(self, context: System.ComponentModel.ITypeDescriptorContext, value: System.Object, ) -> System.ComponentModel.PropertyDescriptorCollection:
        ...

    @typing.overload
    def GetProperties(self, context: System.ComponentModel.ITypeDescriptorContext, value: System.Object, attributes: System.Array[System.Attribute], ) -> System.ComponentModel.PropertyDescriptorCollection:
        ...

    @typing.overload
    def GetPropertiesSupported(self, ) -> bool:
        ...

    @typing.overload
    def GetPropertiesSupported(self, context: System.ComponentModel.ITypeDescriptorContext, ) -> bool:
        ...

    @typing.overload
    def GetStandardValues(self, ) -> System.Collections.ICollection:
        ...

    @typing.overload
    def GetStandardValues(self, context: System.ComponentModel.ITypeDescriptorContext, ) -> System.ComponentModel.TypeConverter.StandardValuesCollection:
        ...

    @typing.overload
    def GetStandardValuesExclusive(self, ) -> bool:
        ...

    @typing.overload
    def GetStandardValuesExclusive(self, context: System.ComponentModel.ITypeDescriptorContext, ) -> bool:
        ...

    @typing.overload
    def GetStandardValuesSupported(self, ) -> bool:
        ...

    @typing.overload
    def GetStandardValuesSupported(self, context: System.ComponentModel.ITypeDescriptorContext, ) -> bool:
        ...

    @typing.overload
    def IsValid(self, value: System.Object, ) -> bool:
        ...

    @typing.overload
    def IsValid(self, context: System.ComponentModel.ITypeDescriptorContext, value: System.Object, ) -> bool:
        ...

    def SortProperties(self, props: System.ComponentModel.PropertyDescriptorCollection, names: System.Array[str], ) -> System.ComponentModel.PropertyDescriptorCollection:
        ...

class ITypeDescriptorContext(System.IServiceProvider, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    @abc.abstractmethod
    def Container(self) -> System.ComponentModel.IContainer:
        ...

    @property
    @abc.abstractmethod
    def Instance(self) -> System.Object:
        ...

    @property
    @abc.abstractmethod
    def PropertyDescriptor(self) -> System.ComponentModel.PropertyDescriptor:
        ...

    # methods
    @abc.abstractmethod
    def OnComponentChanging(self, ) -> bool:
        ...

    @abc.abstractmethod
    def OnComponentChanged(self, ) -> None:
        ...

class IContainer(System.IDisposable, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    @abc.abstractmethod
    def Components(self) -> System.ComponentModel.ComponentCollection:
        ...

    # methods
    @abc.abstractmethod
    @typing.overload
    def Add(self, component: System.ComponentModel.IComponent, ) -> None:
        ...

    @abc.abstractmethod
    @typing.overload
    def Add(self, component: System.ComponentModel.IComponent, name: str, ) -> None:
        ...

    @abc.abstractmethod
    def Remove(self, component: System.ComponentModel.IComponent, ) -> None:
        ...

class ComponentCollection(System.Collections.ICollection, System.Collections.IEnumerable, System.Collections.ReadOnlyCollectionBase):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def Item(self) -> System.ComponentModel.IComponent:
        ...

    @property
    def Item(self) -> System.ComponentModel.IComponent:
        ...

    @property
    def InnerList(self) -> System.Collections.ArrayList:
        ...

    @property
    def Count(self) -> int:
        ...

    # methods
    def __init__(self, components: System.Array[System.ComponentModel.IComponent], ):
        ...

    def CopyTo(self, array: System.Array[System.ComponentModel.IComponent], index: int, ) -> None:
        ...

class PropertyDescriptorCollection(System.Collections.ICollection, System.Collections.IEnumerable, System.Collections.IList, System.Collections.IDictionary, System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields
    Empty: System.ComponentModel.PropertyDescriptorCollection = ...

    # properties
    @property
    def Count(self) -> int:
        ...
    @Count.setter
    def Count(self, val: int):
        ...

    @property
    def Item(self) -> System.ComponentModel.PropertyDescriptor:
        ...

    @property
    def Item(self) -> System.ComponentModel.PropertyDescriptor:
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
    def IsFixedSize(self) -> bool:
        ...

    @property
    def IsReadOnly(self) -> bool:
        ...

    @property
    def Item(self) -> System.Object:
        ...
    @Item.setter
    def Item(self, val: System.Object):
        ...

    @property
    def Keys(self) -> System.Collections.ICollection:
        ...

    @property
    def Values(self) -> System.Collections.ICollection:
        ...

    @property
    def IsReadOnly(self) -> bool:
        ...

    @property
    def IsFixedSize(self) -> bool:
        ...

    @property
    def Item(self) -> System.Object:
        ...
    @Item.setter
    def Item(self, val: System.Object):
        ...

    # methods
    @typing.overload
    def __init__(self, properties: System.Array[System.ComponentModel.PropertyDescriptor], ):
        ...

    @typing.overload
    def __init__(self, properties: System.Array[System.ComponentModel.PropertyDescriptor], readOnly: bool, ):
        ...

    @typing.overload
    def __init__(self, properties: System.Array[System.ComponentModel.PropertyDescriptor], propCount: int, namedSort: System.Array[str], comparer: System.Collections.IComparer, ):
        ...

    def Add(self, value: System.ComponentModel.PropertyDescriptor, ) -> int:
        ...

    def Clear(self, ) -> None:
        ...

    def Contains(self, value: System.ComponentModel.PropertyDescriptor, ) -> bool:
        ...

    def CopyTo(self, array: System.Array, index: int, ) -> None:
        ...

    def EnsurePropsOwned(self, ) -> None:
        ...

    def EnsureSize(self, sizeNeeded: int, ) -> None:
        ...

    def Find(self, name: str, ignoreCase: bool, ) -> System.ComponentModel.PropertyDescriptor:
        ...

    def IndexOf(self, value: System.ComponentModel.PropertyDescriptor, ) -> int:
        ...

    def Insert(self, index: int, value: System.ComponentModel.PropertyDescriptor, ) -> None:
        ...

    def Remove(self, value: System.ComponentModel.PropertyDescriptor, ) -> None:
        ...

    def RemoveAt(self, index: int, ) -> None:
        ...

    @typing.overload
    def Sort(self, ) -> System.ComponentModel.PropertyDescriptorCollection:
        ...

    @typing.overload
    def Sort(self, names: System.Array[str], ) -> System.ComponentModel.PropertyDescriptorCollection:
        ...

    @typing.overload
    def Sort(self, names: System.Array[str], comparer: System.Collections.IComparer, ) -> System.ComponentModel.PropertyDescriptorCollection:
        ...

    @typing.overload
    def Sort(self, comparer: System.Collections.IComparer, ) -> System.ComponentModel.PropertyDescriptorCollection:
        ...

    @typing.overload
    def InternalSort(self, names: System.Array[str], ) -> None:
        ...

    @typing.overload
    def InternalSort(self, sorter: System.Collections.IComparer, ) -> None:
        ...

    def GetEnumerator(self, ) -> System.Collections.IEnumerator:
        ...

    def Clear(self, ) -> None:
        ...

    def Clear(self, ) -> None:
        ...

    def GetEnumerator(self, ) -> System.Collections.IEnumerator:
        ...

    def RemoveAt(self, index: int, ) -> None:
        ...

    def Add(self, key: System.Object, value: System.Object, ) -> None:
        ...

    def Contains(self, key: System.Object, ) -> bool:
        ...

    def GetEnumerator(self, ) -> System.Collections.IDictionaryEnumerator:
        ...

    def Remove(self, key: System.Object, ) -> None:
        ...

    def Add(self, value: System.Object, ) -> int:
        ...

    def Contains(self, value: System.Object, ) -> bool:
        ...

    def IndexOf(self, value: System.Object, ) -> int:
        ...

    def Insert(self, index: int, value: System.Object, ) -> None:
        ...

    def Remove(self, value: System.Object, ) -> None:
        ...

class TypeConverterAttribute(System.Attribute):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields
    Default: System.ComponentModel.TypeConverterAttribute = ...

    # properties
    @property
    def ConverterTypeName(self) -> str:
        ...

    @property
    def TypeId(self) -> System.Object:
        ...

    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def __init__(self, type: System.Type, ):
        ...

    @typing.overload
    def __init__(self, typeName: str, ):
        ...

    def Equals(self, obj: System.Object, ) -> bool:
        ...

    def GetHashCode(self, ) -> int:
        ...

class IComponent(System.IDisposable, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    @abc.abstractmethod
    def Site(self) -> System.ComponentModel.ISite:
        ...
    @Site.setter
    @abc.abstractmethod
    def Site(self, val: System.ComponentModel.ISite):
        ...

    # methods
class WarningException(System.Runtime.Serialization.ISerializable, System.SystemException):
    @typing.overload
    def __init__(self, **kwargs):
        self._message: str
        ...

    # static fields

    # properties
    @property
    def HelpUrl(self) -> str:
        ...

    @property
    def HelpTopic(self) -> str:
        ...

    @property
    def TargetSite(self) -> System.Reflection.MethodBase:
        ...

    @property
    def Message(self) -> str:
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
    def __init__(self, ):
        ...

    @typing.overload
    def __init__(self, message: str, ):
        ...

    @typing.overload
    def __init__(self, message: str, helpUrl: str, ):
        ...

    @typing.overload
    def __init__(self, message: str, innerException: System.Exception, ):
        ...

    @typing.overload
    def __init__(self, message: str, helpUrl: str, helpTopic: str, ):
        ...

    @typing.overload
    def __init__(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext, ):
        ...

    def GetObjectData(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext, ) -> None:
        ...

class ISite(System.IServiceProvider, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    @abc.abstractmethod
    def Component(self) -> System.ComponentModel.IComponent:
        ...

    @property
    @abc.abstractmethod
    def Container(self) -> System.ComponentModel.IContainer:
        ...

    @property
    @abc.abstractmethod
    def DesignMode(self) -> bool:
        ...

    @property
    @abc.abstractmethod
    def Name(self) -> str:
        ...
    @Name.setter
    @abc.abstractmethod
    def Name(self, val: str):
        ...

    # methods
class MarshalByValueComponent(System.ComponentModel.IComponent, System.IDisposable, System.IServiceProvider, System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def Events(self) -> System.ComponentModel.EventHandlerList:
        ...

    @property
    def Site(self) -> System.ComponentModel.ISite:
        ...
    @Site.setter
    def Site(self, val: System.ComponentModel.ISite):
        ...

    @property
    def Container(self) -> System.ComponentModel.IContainer:
        ...

    @property
    def DesignMode(self) -> bool:
        ...

    # methods
    def __init__(self, ):
        ...

    def ToString(self, ) -> str:
        ...

    def Finalize(self, ) -> None:
        ...

    @typing.overload
    def Dispose(self, ) -> None:
        ...

    @typing.overload
    def Dispose(self, disposing: bool, ) -> None:
        ...

    def GetService(self, service: System.Type, ) -> System.Object:
        ...

class PropertyChangedEventArgs(System.EventArgs):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def PropertyName(self) -> str:
        ...

    # methods
    def __init__(self, propertyName: str, ):
        ...

class IListSource(abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    @abc.abstractmethod
    def ContainsListCollection(self) -> bool:
        ...

    # methods
    @abc.abstractmethod
    def GetList(self, ) -> System.Collections.IList:
        ...

class ISupportInitializeNotification(System.ComponentModel.ISupportInitialize, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    @abc.abstractmethod
    def IsInitialized(self) -> bool:
        ...

    # methods
class ListChangedType(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    Reset: int = ...
    ItemAdded: int = ...
    ItemDeleted: int = ...
    ItemMoved: int = ...
    ItemChanged: int = ...
    PropertyDescriptorAdded: int = ...
    PropertyDescriptorDeleted: int = ...
    PropertyDescriptorChanged: int = ...

class ListChangedEventArgs(System.EventArgs):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def ListChangedType(self) -> int:
        ...

    @property
    def NewIndex(self) -> int:
        ...

    @property
    def OldIndex(self) -> int:
        ...

    @property
    def PropertyDescriptor(self) -> System.ComponentModel.PropertyDescriptor:
        ...

    # methods
    @typing.overload
    def __init__(self, listChangedType: int, newIndex: int, ):
        ...

    @typing.overload
    def __init__(self, listChangedType: int, newIndex: int, propDesc: System.ComponentModel.PropertyDescriptor, ):
        ...

    @typing.overload
    def __init__(self, listChangedType: int, propDesc: System.ComponentModel.PropertyDescriptor, ):
        ...

    @typing.overload
    def __init__(self, listChangedType: int, newIndex: int, oldIndex: int, ):
        ...

class IBindingListView(System.ComponentModel.IBindingList, System.Collections.IList, System.Collections.ICollection, System.Collections.IEnumerable, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    @abc.abstractmethod
    def Filter(self) -> str:
        ...
    @Filter.setter
    @abc.abstractmethod
    def Filter(self, val: str):
        ...

    @property
    @abc.abstractmethod
    def SortDescriptions(self) -> System.ComponentModel.ListSortDescriptionCollection:
        ...

    @property
    @abc.abstractmethod
    def SupportsAdvancedSorting(self) -> bool:
        ...

    @property
    @abc.abstractmethod
    def SupportsFiltering(self) -> bool:
        ...

    # methods
    @abc.abstractmethod
    def ApplySort(self, sorts: System.ComponentModel.ListSortDescriptionCollection, ) -> None:
        ...

    @abc.abstractmethod
    def RemoveFilter(self, ) -> None:
        ...

class EventHandlerList(System.IDisposable, System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def Item(self) -> System.Delegate:
        ...
    @Item.setter
    def Item(self, val: System.Delegate):
        ...

    # methods
    @typing.overload
    def __init__(self, parent: System.ComponentModel.Component, ):
        ...

    @typing.overload
    def __init__(self, ):
        ...

    def AddHandler(self, key: System.Object, value: System.Delegate, ) -> None:
        ...

    def AddHandlers(self, listToAddFrom: System.ComponentModel.EventHandlerList, ) -> None:
        ...

    def Dispose(self, ) -> None:
        ...

    def Find(self, key: System.Object, ) -> System.ComponentModel.EventHandlerList.ListEntry:
        ...

    def RemoveHandler(self, key: System.Object, value: System.Delegate, ) -> None:
        ...

class Component(System.ComponentModel.IComponent, System.IDisposable, System.MarshalByRefObject):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def CanRaiseEvents(self) -> bool:
        ...

    @property
    def CanRaiseEventsInternal(self) -> bool:
        ...

    @property
    def Events(self) -> System.ComponentModel.EventHandlerList:
        ...

    @property
    def Site(self) -> System.ComponentModel.ISite:
        ...
    @Site.setter
    def Site(self, val: System.ComponentModel.ISite):
        ...

    @property
    def Container(self) -> System.ComponentModel.IContainer:
        ...

    @property
    def DesignMode(self) -> bool:
        ...

    # methods
    def __init__(self, ):
        ...

    def Finalize(self, ) -> None:
        ...

    @typing.overload
    def Dispose(self, ) -> None:
        ...

    @typing.overload
    def Dispose(self, disposing: bool, ) -> None:
        ...

    def GetService(self, service: System.Type, ) -> System.Object:
        ...

    def ToString(self, ) -> str:
        ...

class IBindingList(System.Collections.IList, System.Collections.ICollection, System.Collections.IEnumerable, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    @abc.abstractmethod
    def AllowNew(self) -> bool:
        ...

    @property
    @abc.abstractmethod
    def AllowEdit(self) -> bool:
        ...

    @property
    @abc.abstractmethod
    def AllowRemove(self) -> bool:
        ...

    @property
    @abc.abstractmethod
    def SupportsChangeNotification(self) -> bool:
        ...

    @property
    @abc.abstractmethod
    def SupportsSearching(self) -> bool:
        ...

    @property
    @abc.abstractmethod
    def SupportsSorting(self) -> bool:
        ...

    @property
    @abc.abstractmethod
    def IsSorted(self) -> bool:
        ...

    @property
    @abc.abstractmethod
    def SortProperty(self) -> System.ComponentModel.PropertyDescriptor:
        ...

    @property
    @abc.abstractmethod
    def SortDirection(self) -> int:
        ...

    # methods
    @abc.abstractmethod
    def AddNew(self, ) -> System.Object:
        ...

    @abc.abstractmethod
    def AddIndex(self, property: System.ComponentModel.PropertyDescriptor, ) -> None:
        ...

    @abc.abstractmethod
    def ApplySort(self, property: System.ComponentModel.PropertyDescriptor, direction: int, ) -> None:
        ...

    @abc.abstractmethod
    def Find(self, property: System.ComponentModel.PropertyDescriptor, key: System.Object, ) -> int:
        ...

    @abc.abstractmethod
    def RemoveIndex(self, property: System.ComponentModel.PropertyDescriptor, ) -> None:
        ...

    @abc.abstractmethod
    def RemoveSort(self, ) -> None:
        ...

class CollectionChangeEventArgs(System.EventArgs):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def Action(self) -> int:
        ...

    @property
    def Element(self) -> System.Object:
        ...

    # methods
    def __init__(self, action: int, element: System.Object, ):
        ...

class CollectionChangeAction(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    Add: int = ...
    Remove: int = ...
    Refresh: int = ...

class ListSortDescriptionCollection(System.Collections.IList, System.Collections.ICollection, System.Collections.IEnumerable, System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def Item(self) -> System.ComponentModel.ListSortDescription:
        ...
    @Item.setter
    def Item(self, val: System.ComponentModel.ListSortDescription):
        ...

    @property
    def IsFixedSize(self) -> bool:
        ...

    @property
    def IsReadOnly(self) -> bool:
        ...

    @property
    def Item(self) -> System.Object:
        ...
    @Item.setter
    def Item(self, val: System.Object):
        ...

    @property
    def Count(self) -> int:
        ...

    @property
    def IsSynchronized(self) -> bool:
        ...

    @property
    def SyncRoot(self) -> System.Object:
        ...

    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def __init__(self, sorts: System.Array[System.ComponentModel.ListSortDescription], ):
        ...

    def Add(self, value: System.Object, ) -> int:
        ...

    def Clear(self, ) -> None:
        ...

    def Contains(self, value: System.Object, ) -> bool:
        ...

    def IndexOf(self, value: System.Object, ) -> int:
        ...

    def Insert(self, index: int, value: System.Object, ) -> None:
        ...

    def Remove(self, value: System.Object, ) -> None:
        ...

    def RemoveAt(self, index: int, ) -> None:
        ...

    def CopyTo(self, array: System.Array, index: int, ) -> None:
        ...

    def GetEnumerator(self, ) -> System.Collections.IEnumerator:
        ...

class ListSortDescription(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def PropertyDescriptor(self) -> System.ComponentModel.PropertyDescriptor:
        ...
    @PropertyDescriptor.setter
    def PropertyDescriptor(self, val: System.ComponentModel.PropertyDescriptor):
        ...

    @property
    def SortDirection(self) -> int:
        ...
    @SortDirection.setter
    def SortDirection(self, val: int):
        ...

    # methods
    def __init__(self, property: System.ComponentModel.PropertyDescriptor, direction: int, ):
        ...

class ITypedList(abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    @abc.abstractmethod
    def GetListName(self, listAccessors: System.Array[System.ComponentModel.PropertyDescriptor], ) -> str:
        ...

    @abc.abstractmethod
    def GetItemProperties(self, listAccessors: System.Array[System.ComponentModel.PropertyDescriptor], ) -> System.ComponentModel.PropertyDescriptorCollection:
        ...

class ISupportInitialize(abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    @abc.abstractmethod
    def BeginInit(self, ) -> None:
        ...

    @abc.abstractmethod
    def EndInit(self, ) -> None:
        ...

class PropertyDescriptor(System.ComponentModel.MemberDescriptor, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    @abc.abstractmethod
    def ComponentType(self) -> System.Type:
        ...

    @property
    def Converter(self) -> System.ComponentModel.TypeConverter:
        ...

    @property
    def IsLocalizable(self) -> bool:
        ...

    @property
    @abc.abstractmethod
    def IsReadOnly(self) -> bool:
        ...

    @property
    def SerializationVisibility(self) -> int:
        ...

    @property
    @abc.abstractmethod
    def PropertyType(self) -> System.Type:
        ...

    @property
    def SupportsChangeEvents(self) -> bool:
        ...

    @property
    def AttributeArray(self) -> System.Array[System.Attribute]:
        ...
    @AttributeArray.setter
    def AttributeArray(self, val: System.Array[System.Attribute]):
        ...

    @property
    def Attributes(self) -> System.ComponentModel.AttributeCollection:
        ...

    @property
    def Category(self) -> str:
        ...

    @property
    def Description(self) -> str:
        ...

    @property
    def IsBrowsable(self) -> bool:
        ...

    @property
    def Name(self) -> str:
        ...

    @property
    def NameHashCode(self) -> int:
        ...

    @property
    def DesignTimeOnly(self) -> bool:
        ...

    @property
    def DisplayName(self) -> str:
        ...

    # methods
    @typing.overload
    def __init__(self, name: str, attrs: System.Array[System.Attribute], ):
        ...

    @typing.overload
    def __init__(self, descr: System.ComponentModel.MemberDescriptor, ):
        ...

    @typing.overload
    def __init__(self, descr: System.ComponentModel.MemberDescriptor, attrs: System.Array[System.Attribute], ):
        ...

    def AddValueChanged(self, component: System.Object, handler: System.EventHandler, ) -> None:
        ...

    @abc.abstractmethod
    def CanResetValue(self, component: System.Object, ) -> bool:
        ...

    def Equals(self, obj: System.Object, ) -> bool:
        ...

    def CreateInstance(self, type: System.Type, ) -> System.Object:
        ...

    def FillAttributes(self, attributeList: System.Collections.IList, ) -> None:
        ...

    @typing.overload
    def GetChildProperties(self, ) -> System.ComponentModel.PropertyDescriptorCollection:
        ...

    @typing.overload
    def GetChildProperties(self, filter: System.Array[System.Attribute], ) -> System.ComponentModel.PropertyDescriptorCollection:
        ...

    @typing.overload
    def GetChildProperties(self, instance: System.Object, ) -> System.ComponentModel.PropertyDescriptorCollection:
        ...

    @typing.overload
    def GetChildProperties(self, instance: System.Object, filter: System.Array[System.Attribute], ) -> System.ComponentModel.PropertyDescriptorCollection:
        ...

    def GetEditor(self, editorBaseType: System.Type, ) -> System.Object:
        ...

    def GetHashCode(self, ) -> int:
        ...

    def GetInvocationTarget(self, type: System.Type, instance: System.Object, ) -> System.Object:
        ...

    def GetTypeFromName(self, typeName: str, ) -> System.Type:
        ...

    @abc.abstractmethod
    def GetValue(self, component: System.Object, ) -> System.Object:
        ...

    def OnValueChanged(self, component: System.Object, e: System.EventArgs, ) -> None:
        ...

    def RemoveValueChanged(self, component: System.Object, handler: System.EventHandler, ) -> None:
        ...

    def GetValueChangedHandler(self, component: System.Object, ) -> System.EventHandler:
        ...

    @abc.abstractmethod
    def ResetValue(self, component: System.Object, ) -> None:
        ...

    @abc.abstractmethod
    def SetValue(self, component: System.Object, value: System.Object, ) -> None:
        ...

    @abc.abstractmethod
    def ShouldSerializeValue(self, component: System.Object, ) -> bool:
        ...

class MemberDescriptor(System.Object, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def AttributeArray(self) -> System.Array[System.Attribute]:
        ...
    @AttributeArray.setter
    def AttributeArray(self, val: System.Array[System.Attribute]):
        ...

    @property
    def Attributes(self) -> System.ComponentModel.AttributeCollection:
        ...

    @property
    def Category(self) -> str:
        ...

    @property
    def Description(self) -> str:
        ...

    @property
    def IsBrowsable(self) -> bool:
        ...

    @property
    def Name(self) -> str:
        ...

    @property
    def NameHashCode(self) -> int:
        ...

    @property
    def DesignTimeOnly(self) -> bool:
        ...

    @property
    def DisplayName(self) -> str:
        ...

    # methods
    @typing.overload
    def __init__(self, name: str, ):
        ...

    @typing.overload
    def __init__(self, name: str, attributes: System.Array[System.Attribute], ):
        ...

    @typing.overload
    def __init__(self, descr: System.ComponentModel.MemberDescriptor, ):
        ...

    @typing.overload
    def __init__(self, oldMemberDescriptor: System.ComponentModel.MemberDescriptor, newAttributes: System.Array[System.Attribute], ):
        ...

    def Equals(self, obj: System.Object, ) -> bool:
        ...

    def FillAttributes(self, attributeList: System.Collections.IList, ) -> None:
        ...

    def GetHashCode(self, ) -> int:
        ...

    def GetInvocationTarget(self, type: System.Type, instance: System.Object, ) -> System.Object:
        ...

    def CheckAttributesValid(self, ) -> None:
        ...

    def CreateAttributeCollection(self, ) -> System.ComponentModel.AttributeCollection:
        ...

    def FilterAttributesIfNeeded(self, ) -> None:
        ...

    @staticmethod
    @typing.overload
    def FindMethod(componentClass: System.Type, name: str, args: System.Array[System.Type], returnType: System.Type, ) -> System.Reflection.MethodInfo:
        ...

    @staticmethod
    @typing.overload
    def FindMethod(componentClass: System.Type, name: str, args: System.Array[System.Type], returnType: System.Type, publicOnly: bool, ) -> System.Reflection.MethodInfo:
        ...

    @staticmethod
    def GetSite(component: System.Object, ) -> System.ComponentModel.ISite:
        ...

    @staticmethod
    def GetInvokee(componentClass: System.Type, component: System.Object, ) -> System.Object:
        ...

class AttributeCollection(System.Collections.ICollection, System.Collections.IEnumerable, System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields
    Empty: System.ComponentModel.AttributeCollection = ...

    # properties
    @property
    def Attributes(self) -> System.Array[System.Attribute]:
        ...

    @property
    def Count(self) -> int:
        ...

    @property
    def Item(self) -> System.Attribute:
        ...

    @property
    def Item(self) -> System.Attribute:
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

    # methods
    @typing.overload
    def __init__(self, attributes: System.Array[System.Attribute], ):
        ...

    @typing.overload
    def __init__(self, ):
        ...

    @staticmethod
    def FromExisting(existing: System.ComponentModel.AttributeCollection, newAttributes: System.Array[System.Attribute], ) -> System.ComponentModel.AttributeCollection:
        ...

    @typing.overload
    def Contains(self, attribute: System.Attribute, ) -> bool:
        ...

    @typing.overload
    def Contains(self, attributes: System.Array[System.Attribute], ) -> bool:
        ...

    def GetDefaultAttribute(self, attributeType: System.Type, ) -> System.Attribute:
        ...

    def GetEnumerator(self, ) -> System.Collections.IEnumerator:
        ...

    @typing.overload
    def Matches(self, attribute: System.Attribute, ) -> bool:
        ...

    @typing.overload
    def Matches(self, attributes: System.Array[System.Attribute], ) -> bool:
        ...

    def GetEnumerator(self, ) -> System.Collections.IEnumerator:
        ...

    def CopyTo(self, array: System.Array, index: int, ) -> None:
        ...

class ICustomTypeDescriptor(abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    @abc.abstractmethod
    def GetAttributes(self, ) -> System.ComponentModel.AttributeCollection:
        ...

    @abc.abstractmethod
    def GetClassName(self, ) -> str:
        ...

    @abc.abstractmethod
    def GetComponentName(self, ) -> str:
        ...

    @abc.abstractmethod
    def GetConverter(self, ) -> System.ComponentModel.TypeConverter:
        ...

    @abc.abstractmethod
    def GetDefaultEvent(self, ) -> System.ComponentModel.EventDescriptor:
        ...

    @abc.abstractmethod
    def GetDefaultProperty(self, ) -> System.ComponentModel.PropertyDescriptor:
        ...

    @abc.abstractmethod
    def GetEditor(self, editorBaseType: System.Type, ) -> System.Object:
        ...

    @abc.abstractmethod
    @typing.overload
    def GetEvents(self, ) -> System.ComponentModel.EventDescriptorCollection:
        ...

    @abc.abstractmethod
    @typing.overload
    def GetEvents(self, attributes: System.Array[System.Attribute], ) -> System.ComponentModel.EventDescriptorCollection:
        ...

    @abc.abstractmethod
    @typing.overload
    def GetProperties(self, ) -> System.ComponentModel.PropertyDescriptorCollection:
        ...

    @abc.abstractmethod
    @typing.overload
    def GetProperties(self, attributes: System.Array[System.Attribute], ) -> System.ComponentModel.PropertyDescriptorCollection:
        ...

    @abc.abstractmethod
    def GetPropertyOwner(self, pd: System.ComponentModel.PropertyDescriptor, ) -> System.Object:
        ...

class EventDescriptor(System.ComponentModel.MemberDescriptor, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    @abc.abstractmethod
    def ComponentType(self) -> System.Type:
        ...

    @property
    @abc.abstractmethod
    def EventType(self) -> System.Type:
        ...

    @property
    @abc.abstractmethod
    def IsMulticast(self) -> bool:
        ...

    @property
    def AttributeArray(self) -> System.Array[System.Attribute]:
        ...
    @AttributeArray.setter
    def AttributeArray(self, val: System.Array[System.Attribute]):
        ...

    @property
    def Attributes(self) -> System.ComponentModel.AttributeCollection:
        ...

    @property
    def Category(self) -> str:
        ...

    @property
    def Description(self) -> str:
        ...

    @property
    def IsBrowsable(self) -> bool:
        ...

    @property
    def Name(self) -> str:
        ...

    @property
    def NameHashCode(self) -> int:
        ...

    @property
    def DesignTimeOnly(self) -> bool:
        ...

    @property
    def DisplayName(self) -> str:
        ...

    # methods
    @typing.overload
    def __init__(self, name: str, attrs: System.Array[System.Attribute], ):
        ...

    @typing.overload
    def __init__(self, descr: System.ComponentModel.MemberDescriptor, ):
        ...

    @typing.overload
    def __init__(self, descr: System.ComponentModel.MemberDescriptor, attrs: System.Array[System.Attribute], ):
        ...

    @abc.abstractmethod
    def AddEventHandler(self, component: System.Object, value: System.Delegate, ) -> None:
        ...

    @abc.abstractmethod
    def RemoveEventHandler(self, component: System.Object, value: System.Delegate, ) -> None:
        ...

class EventDescriptorCollection(System.Collections.ICollection, System.Collections.IEnumerable, System.Collections.IList, System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields
    Empty: System.ComponentModel.EventDescriptorCollection = ...

    # properties
    @property
    def Count(self) -> int:
        ...
    @Count.setter
    def Count(self, val: int):
        ...

    @property
    def Item(self) -> System.ComponentModel.EventDescriptor:
        ...

    @property
    def Item(self) -> System.ComponentModel.EventDescriptor:
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
    def Item(self) -> System.Object:
        ...
    @Item.setter
    def Item(self, val: System.Object):
        ...

    @property
    def IsReadOnly(self) -> bool:
        ...

    @property
    def IsFixedSize(self) -> bool:
        ...

    # methods
    @typing.overload
    def __init__(self, events: System.Array[System.ComponentModel.EventDescriptor], ):
        ...

    @typing.overload
    def __init__(self, events: System.Array[System.ComponentModel.EventDescriptor], readOnly: bool, ):
        ...

    @typing.overload
    def __init__(self, events: System.Array[System.ComponentModel.EventDescriptor], eventCount: int, namedSort: System.Array[str], comparer: System.Collections.IComparer, ):
        ...

    def Add(self, value: System.ComponentModel.EventDescriptor, ) -> int:
        ...

    def Clear(self, ) -> None:
        ...

    def Contains(self, value: System.ComponentModel.EventDescriptor, ) -> bool:
        ...

    def CopyTo(self, array: System.Array, index: int, ) -> None:
        ...

    def EnsureEventsOwned(self, ) -> None:
        ...

    def EnsureSize(self, sizeNeeded: int, ) -> None:
        ...

    def Find(self, name: str, ignoreCase: bool, ) -> System.ComponentModel.EventDescriptor:
        ...

    def IndexOf(self, value: System.ComponentModel.EventDescriptor, ) -> int:
        ...

    def Insert(self, index: int, value: System.ComponentModel.EventDescriptor, ) -> None:
        ...

    def Remove(self, value: System.ComponentModel.EventDescriptor, ) -> None:
        ...

    def RemoveAt(self, index: int, ) -> None:
        ...

    def GetEnumerator(self, ) -> System.Collections.IEnumerator:
        ...

    @typing.overload
    def Sort(self, ) -> System.ComponentModel.EventDescriptorCollection:
        ...

    @typing.overload
    def Sort(self, names: System.Array[str], ) -> System.ComponentModel.EventDescriptorCollection:
        ...

    @typing.overload
    def Sort(self, names: System.Array[str], comparer: System.Collections.IComparer, ) -> System.ComponentModel.EventDescriptorCollection:
        ...

    @typing.overload
    def Sort(self, comparer: System.Collections.IComparer, ) -> System.ComponentModel.EventDescriptorCollection:
        ...

    @typing.overload
    def InternalSort(self, names: System.Array[str], ) -> None:
        ...

    @typing.overload
    def InternalSort(self, sorter: System.Collections.IComparer, ) -> None:
        ...

    def GetEnumerator(self, ) -> System.Collections.IEnumerator:
        ...

    def Add(self, value: System.Object, ) -> int:
        ...

    def Contains(self, value: System.Object, ) -> bool:
        ...

    def Clear(self, ) -> None:
        ...

    def IndexOf(self, value: System.Object, ) -> int:
        ...

    def Insert(self, index: int, value: System.Object, ) -> None:
        ...

    def Remove(self, value: System.Object, ) -> None:
        ...

    def RemoveAt(self, index: int, ) -> None:
        ...

class ListSortDirection(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    Ascending: int = ...
    Descending: int = ...

class IDataErrorInfo(abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    @abc.abstractmethod
    def Item(self) -> str:
        ...

    @property
    @abc.abstractmethod
    def Error(self) -> str:
        ...

    # methods
class IEditableObject(abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    @abc.abstractmethod
    def BeginEdit(self, ) -> None:
        ...

    @abc.abstractmethod
    def EndEdit(self, ) -> None:
        ...

    @abc.abstractmethod
    def CancelEdit(self, ) -> None:
        ...

class INotifyPropertyChanged(abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
