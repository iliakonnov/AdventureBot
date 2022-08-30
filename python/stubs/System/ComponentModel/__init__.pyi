from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import System
import System.ComponentModel
import System.Collections
import System.Globalization
import System.ComponentModel.TypeConverter


class IComponent(System.IDisposable, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @abc.abstractmethod
    @property
    def Site(self) -> System.ComponentModel.ISite:
        ...
    @abc.abstractmethod
    @Site.setter
    def Site(self, val: System.ComponentModel.ISite):
        ...

    # methods
class ISite(System.IServiceProvider, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @abc.abstractmethod
    @property
    def Component(self) -> System.ComponentModel.IComponent:
        ...

    @abc.abstractmethod
    @property
    def Container(self) -> System.ComponentModel.IContainer:
        ...

    @abc.abstractmethod
    @property
    def DesignMode(self) -> System.Boolean:
        ...

    @abc.abstractmethod
    @property
    def Name(self) -> System.String:
        ...
    @abc.abstractmethod
    @Name.setter
    def Name(self, val: System.String):
        ...

    # methods
class IContainer(System.IDisposable, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @abc.abstractmethod
    @property
    def Components(self) -> System.ComponentModel.ComponentCollection:
        ...

    # methods
    @typing.overload
    @abc.abstractmethod
    def Add(self, component: System.ComponentModel.IComponent, ) -> None:
        ...

    @typing.overload
    @abc.abstractmethod
    def Add(self, component: System.ComponentModel.IComponent, name: System.String, ) -> None:
        ...

    @typing.overload
    @abc.abstractmethod
    def Remove(self, component: System.ComponentModel.IComponent, ) -> None:
        ...

class Component(System.ComponentModel.IComponent, System.IDisposable, System.MarshalByRefObject):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def Site(self) -> System.ComponentModel.ISite:
        ...
    @Site.setter
    def Site(self, val: System.ComponentModel.ISite):
        ...

    @property
    def Container(self) -> System.ComponentModel.IContainer:
        ...

    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def Dispose(self, ) -> None:
        ...

    @typing.overload
    def ToString(self, ) -> System.String:
        ...

class ComponentCollection(System.Collections.ICollection, System.Collections.IEnumerable, System.Collections.ReadOnlyCollectionBase):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def Item(self) -> System.ComponentModel.IComponent:
        ...

    @property
    def Item(self) -> System.ComponentModel.IComponent:
        ...

    @property
    def Count(self) -> System.Int32:
        ...

    # methods
    @typing.overload
    def __init__(self, components: list[System.ComponentModel.IComponent], ):
        ...

    @typing.overload
    def CopyTo(self, array: list[System.ComponentModel.IComponent], index: System.Int32, ) -> None:
        ...

class IListSource(abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @abc.abstractmethod
    @property
    def ContainsListCollection(self) -> System.Boolean:
        ...

    # methods
    @typing.overload
    @abc.abstractmethod
    def GetList(self, ) -> System.Collections.IList:
        ...

class ISupportInitializeNotification(System.ComponentModel.ISupportInitialize, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @abc.abstractmethod
    @property
    def IsInitialized(self) -> System.Boolean:
        ...

    # methods
class ISupportInitialize(abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    # methods
    @typing.overload
    @abc.abstractmethod
    def BeginInit(self, ) -> None:
        ...

    @typing.overload
    @abc.abstractmethod
    def EndInit(self, ) -> None:
        ...

class MarshalByValueComponent(System.ComponentModel.IComponent, System.IDisposable, System.IServiceProvider, System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
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
    def DesignMode(self) -> System.Boolean:
        ...

    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def ToString(self, ) -> System.String:
        ...

    @typing.overload
    def Dispose(self, ) -> None:
        ...

    @typing.overload
    def GetService(self, service: System.Type, ) -> System.Object:
        ...

class IBindingListView(System.ComponentModel.IBindingList, System.Collections.IList, System.Collections.ICollection, System.Collections.IEnumerable, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @abc.abstractmethod
    @property
    def Filter(self) -> System.String:
        ...
    @abc.abstractmethod
    @Filter.setter
    def Filter(self, val: System.String):
        ...

    @abc.abstractmethod
    @property
    def SortDescriptions(self) -> System.ComponentModel.ListSortDescriptionCollection:
        ...

    @abc.abstractmethod
    @property
    def SupportsAdvancedSorting(self) -> System.Boolean:
        ...

    @abc.abstractmethod
    @property
    def SupportsFiltering(self) -> System.Boolean:
        ...

    # methods
    @typing.overload
    @abc.abstractmethod
    def ApplySort(self, sorts: System.ComponentModel.ListSortDescriptionCollection, ) -> None:
        ...

    @typing.overload
    @abc.abstractmethod
    def RemoveFilter(self, ) -> None:
        ...

class IBindingList(System.Collections.IList, System.Collections.ICollection, System.Collections.IEnumerable, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @abc.abstractmethod
    @property
    def AllowNew(self) -> System.Boolean:
        ...

    @abc.abstractmethod
    @property
    def AllowEdit(self) -> System.Boolean:
        ...

    @abc.abstractmethod
    @property
    def AllowRemove(self) -> System.Boolean:
        ...

    @abc.abstractmethod
    @property
    def SupportsChangeNotification(self) -> System.Boolean:
        ...

    @abc.abstractmethod
    @property
    def SupportsSearching(self) -> System.Boolean:
        ...

    @abc.abstractmethod
    @property
    def SupportsSorting(self) -> System.Boolean:
        ...

    @abc.abstractmethod
    @property
    def IsSorted(self) -> System.Boolean:
        ...

    @abc.abstractmethod
    @property
    def SortProperty(self) -> System.ComponentModel.PropertyDescriptor:
        ...

    @abc.abstractmethod
    @property
    def SortDirection(self) -> System.ComponentModel.ListSortDirection:
        ...

    # methods
    @typing.overload
    @abc.abstractmethod
    def AddNew(self, ) -> System.Object:
        ...

    @typing.overload
    @abc.abstractmethod
    def AddIndex(self, property: System.ComponentModel.PropertyDescriptor, ) -> None:
        ...

    @typing.overload
    @abc.abstractmethod
    def ApplySort(self, property: System.ComponentModel.PropertyDescriptor, direction: System.ComponentModel.ListSortDirection, ) -> None:
        ...

    @typing.overload
    @abc.abstractmethod
    def Find(self, property: System.ComponentModel.PropertyDescriptor, key: System.Object, ) -> System.Int32:
        ...

    @typing.overload
    @abc.abstractmethod
    def RemoveIndex(self, property: System.ComponentModel.PropertyDescriptor, ) -> None:
        ...

    @typing.overload
    @abc.abstractmethod
    def RemoveSort(self, ) -> None:
        ...

class ITypedList(abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    # methods
    @typing.overload
    @abc.abstractmethod
    def GetListName(self, listAccessors: list[System.ComponentModel.PropertyDescriptor], ) -> System.String:
        ...

    @typing.overload
    @abc.abstractmethod
    def GetItemProperties(self, listAccessors: list[System.ComponentModel.PropertyDescriptor], ) -> System.ComponentModel.PropertyDescriptorCollection:
        ...

class ListSortDescriptionCollection(System.Collections.IList, System.Collections.ICollection, System.Collections.IEnumerable, System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def Item(self) -> System.ComponentModel.ListSortDescription:
        ...
    @Item.setter
    def Item(self, val: System.ComponentModel.ListSortDescription):
        ...

    @property
    def Count(self) -> System.Int32:
        ...

    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def __init__(self, sorts: list[System.ComponentModel.ListSortDescription], ):
        ...

    @typing.overload
    def Contains(self, value: System.Object, ) -> System.Boolean:
        ...

    @typing.overload
    def IndexOf(self, value: System.Object, ) -> System.Int32:
        ...

    @typing.overload
    def CopyTo(self, array: System.Array, index: System.Int32, ) -> None:
        ...

class PropertyDescriptor(System.ComponentModel.MemberDescriptor, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @abc.abstractmethod
    @property
    def ComponentType(self) -> System.Type:
        ...

    @property
    def Converter(self) -> System.ComponentModel.TypeConverter:
        ...

    @property
    def IsLocalizable(self) -> System.Boolean:
        ...

    @abc.abstractmethod
    @property
    def IsReadOnly(self) -> System.Boolean:
        ...

    @property
    def SerializationVisibility(self) -> System.ComponentModel.DesignerSerializationVisibility:
        ...

    @abc.abstractmethod
    @property
    def PropertyType(self) -> System.Type:
        ...

    @property
    def SupportsChangeEvents(self) -> System.Boolean:
        ...

    @property
    def Attributes(self) -> System.ComponentModel.AttributeCollection:
        ...

    @property
    def Category(self) -> System.String:
        ...

    @property
    def Description(self) -> System.String:
        ...

    @property
    def IsBrowsable(self) -> System.Boolean:
        ...

    @property
    def Name(self) -> System.String:
        ...

    @property
    def DesignTimeOnly(self) -> System.Boolean:
        ...

    @property
    def DisplayName(self) -> System.String:
        ...

    # methods
    @typing.overload
    def AddValueChanged(self, component: System.Object, handler: System.EventHandler, ) -> None:
        ...

    @typing.overload
    @abc.abstractmethod
    def CanResetValue(self, component: System.Object, ) -> System.Boolean:
        ...

    @typing.overload
    def Equals(self, obj: System.Object, ) -> System.Boolean:
        ...

    @typing.overload
    def GetChildProperties(self, ) -> System.ComponentModel.PropertyDescriptorCollection:
        ...

    @typing.overload
    def GetChildProperties(self, filter: list[System.Attribute], ) -> System.ComponentModel.PropertyDescriptorCollection:
        ...

    @typing.overload
    def GetChildProperties(self, instance: System.Object, ) -> System.ComponentModel.PropertyDescriptorCollection:
        ...

    @typing.overload
    def GetChildProperties(self, instance: System.Object, filter: list[System.Attribute], ) -> System.ComponentModel.PropertyDescriptorCollection:
        ...

    @typing.overload
    def GetEditor(self, editorBaseType: System.Type, ) -> System.Object:
        ...

    @typing.overload
    def GetHashCode(self, ) -> System.Int32:
        ...

    @typing.overload
    @abc.abstractmethod
    def GetValue(self, component: System.Object, ) -> System.Object:
        ...

    @typing.overload
    def RemoveValueChanged(self, component: System.Object, handler: System.EventHandler, ) -> None:
        ...

    @typing.overload
    @abc.abstractmethod
    def ResetValue(self, component: System.Object, ) -> None:
        ...

    @typing.overload
    @abc.abstractmethod
    def SetValue(self, component: System.Object, value: System.Object, ) -> None:
        ...

    @typing.overload
    @abc.abstractmethod
    def ShouldSerializeValue(self, component: System.Object, ) -> System.Boolean:
        ...

class ListSortDirection(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    Ascending: System.Int32 = Ascending
    Descending: System.Int32 = Descending

class PropertyDescriptorCollection(System.Collections.ICollection, System.Collections.IEnumerable, System.Collections.IList, System.Collections.IDictionary, System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def Count(self) -> System.Int32:
        ...

    @property
    def Item(self) -> System.ComponentModel.PropertyDescriptor:
        ...

    @property
    def Item(self) -> System.ComponentModel.PropertyDescriptor:
        ...

    # methods
    @typing.overload
    def __init__(self, properties: list[System.ComponentModel.PropertyDescriptor], ):
        ...

    @typing.overload
    def __init__(self, properties: list[System.ComponentModel.PropertyDescriptor], readOnly: System.Boolean, ):
        ...

    @typing.overload
    def Add(self, value: System.ComponentModel.PropertyDescriptor, ) -> System.Int32:
        ...

    @typing.overload
    def Clear(self, ) -> None:
        ...

    @typing.overload
    def Contains(self, value: System.ComponentModel.PropertyDescriptor, ) -> System.Boolean:
        ...

    @typing.overload
    def CopyTo(self, array: System.Array, index: System.Int32, ) -> None:
        ...

    @typing.overload
    def Find(self, name: System.String, ignoreCase: System.Boolean, ) -> System.ComponentModel.PropertyDescriptor:
        ...

    @typing.overload
    def IndexOf(self, value: System.ComponentModel.PropertyDescriptor, ) -> System.Int32:
        ...

    @typing.overload
    def Insert(self, index: System.Int32, value: System.ComponentModel.PropertyDescriptor, ) -> None:
        ...

    @typing.overload
    def Remove(self, value: System.ComponentModel.PropertyDescriptor, ) -> None:
        ...

    @typing.overload
    def RemoveAt(self, index: System.Int32, ) -> None:
        ...

    @typing.overload
    def Sort(self, ) -> System.ComponentModel.PropertyDescriptorCollection:
        ...

    @typing.overload
    def Sort(self, names: list[System.String], ) -> System.ComponentModel.PropertyDescriptorCollection:
        ...

    @typing.overload
    def Sort(self, names: list[System.String], comparer: System.Collections.IComparer, ) -> System.ComponentModel.PropertyDescriptorCollection:
        ...

    @typing.overload
    def Sort(self, comparer: System.Collections.IComparer, ) -> System.ComponentModel.PropertyDescriptorCollection:
        ...

    @typing.overload
    def GetEnumerator(self, ) -> System.Collections.IEnumerator:
        ...

class ICustomTypeDescriptor(abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    # methods
    @typing.overload
    @abc.abstractmethod
    def GetAttributes(self, ) -> System.ComponentModel.AttributeCollection:
        ...

    @typing.overload
    @abc.abstractmethod
    def GetClassName(self, ) -> System.String:
        ...

    @typing.overload
    @abc.abstractmethod
    def GetComponentName(self, ) -> System.String:
        ...

    @typing.overload
    @abc.abstractmethod
    def GetConverter(self, ) -> System.ComponentModel.TypeConverter:
        ...

    @typing.overload
    @abc.abstractmethod
    def GetDefaultEvent(self, ) -> System.ComponentModel.EventDescriptor:
        ...

    @typing.overload
    @abc.abstractmethod
    def GetDefaultProperty(self, ) -> System.ComponentModel.PropertyDescriptor:
        ...

    @typing.overload
    @abc.abstractmethod
    def GetEditor(self, editorBaseType: System.Type, ) -> System.Object:
        ...

    @typing.overload
    @abc.abstractmethod
    def GetEvents(self, ) -> System.ComponentModel.EventDescriptorCollection:
        ...

    @typing.overload
    @abc.abstractmethod
    def GetEvents(self, attributes: list[System.Attribute], ) -> System.ComponentModel.EventDescriptorCollection:
        ...

    @typing.overload
    @abc.abstractmethod
    def GetProperties(self, ) -> System.ComponentModel.PropertyDescriptorCollection:
        ...

    @typing.overload
    @abc.abstractmethod
    def GetProperties(self, attributes: list[System.Attribute], ) -> System.ComponentModel.PropertyDescriptorCollection:
        ...

    @typing.overload
    @abc.abstractmethod
    def GetPropertyOwner(self, pd: System.ComponentModel.PropertyDescriptor, ) -> System.Object:
        ...

class IEditableObject(abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    # methods
    @typing.overload
    @abc.abstractmethod
    def BeginEdit(self, ) -> None:
        ...

    @typing.overload
    @abc.abstractmethod
    def EndEdit(self, ) -> None:
        ...

    @typing.overload
    @abc.abstractmethod
    def CancelEdit(self, ) -> None:
        ...

class IDataErrorInfo(abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @abc.abstractmethod
    @property
    def Item(self) -> System.String:
        ...

    @abc.abstractmethod
    @property
    def Error(self) -> System.String:
        ...

    # methods
class INotifyPropertyChanged(abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    # methods
class ListSortDescription(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def PropertyDescriptor(self) -> System.ComponentModel.PropertyDescriptor:
        ...
    @PropertyDescriptor.setter
    def PropertyDescriptor(self, val: System.ComponentModel.PropertyDescriptor):
        ...

    @property
    def SortDirection(self) -> System.ComponentModel.ListSortDirection:
        ...
    @SortDirection.setter
    def SortDirection(self, val: System.ComponentModel.ListSortDirection):
        ...

    # methods
    @typing.overload
    def __init__(self, property: System.ComponentModel.PropertyDescriptor, direction: System.ComponentModel.ListSortDirection, ):
        ...

class MemberDescriptor(System.Object, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def Attributes(self) -> System.ComponentModel.AttributeCollection:
        ...

    @property
    def Category(self) -> System.String:
        ...

    @property
    def Description(self) -> System.String:
        ...

    @property
    def IsBrowsable(self) -> System.Boolean:
        ...

    @property
    def Name(self) -> System.String:
        ...

    @property
    def DesignTimeOnly(self) -> System.Boolean:
        ...

    @property
    def DisplayName(self) -> System.String:
        ...

    # methods
    @typing.overload
    def Equals(self, obj: System.Object, ) -> System.Boolean:
        ...

    @typing.overload
    def GetHashCode(self, ) -> System.Int32:
        ...

class TypeConverter(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def CanConvertFrom(self, sourceType: System.Type, ) -> System.Boolean:
        ...

    @typing.overload
    def CanConvertFrom(self, context: System.ComponentModel.ITypeDescriptorContext, sourceType: System.Type, ) -> System.Boolean:
        ...

    @typing.overload
    def CanConvertTo(self, destinationType: System.Type, ) -> System.Boolean:
        ...

    @typing.overload
    def CanConvertTo(self, context: System.ComponentModel.ITypeDescriptorContext, destinationType: System.Type, ) -> System.Boolean:
        ...

    @typing.overload
    def ConvertFrom(self, value: System.Object, ) -> System.Object:
        ...

    @typing.overload
    def ConvertFrom(self, context: System.ComponentModel.ITypeDescriptorContext, culture: System.Globalization.CultureInfo, value: System.Object, ) -> System.Object:
        ...

    @typing.overload
    def ConvertFromInvariantString(self, text: System.String, ) -> System.Object:
        ...

    @typing.overload
    def ConvertFromInvariantString(self, context: System.ComponentModel.ITypeDescriptorContext, text: System.String, ) -> System.Object:
        ...

    @typing.overload
    def ConvertFromString(self, text: System.String, ) -> System.Object:
        ...

    @typing.overload
    def ConvertFromString(self, context: System.ComponentModel.ITypeDescriptorContext, text: System.String, ) -> System.Object:
        ...

    @typing.overload
    def ConvertFromString(self, context: System.ComponentModel.ITypeDescriptorContext, culture: System.Globalization.CultureInfo, text: System.String, ) -> System.Object:
        ...

    @typing.overload
    def ConvertTo(self, value: System.Object, destinationType: System.Type, ) -> System.Object:
        ...

    @typing.overload
    def ConvertTo(self, context: System.ComponentModel.ITypeDescriptorContext, culture: System.Globalization.CultureInfo, value: System.Object, destinationType: System.Type, ) -> System.Object:
        ...

    @typing.overload
    def ConvertToInvariantString(self, value: System.Object, ) -> System.String:
        ...

    @typing.overload
    def ConvertToInvariantString(self, context: System.ComponentModel.ITypeDescriptorContext, value: System.Object, ) -> System.String:
        ...

    @typing.overload
    def ConvertToString(self, value: System.Object, ) -> System.String:
        ...

    @typing.overload
    def ConvertToString(self, context: System.ComponentModel.ITypeDescriptorContext, value: System.Object, ) -> System.String:
        ...

    @typing.overload
    def ConvertToString(self, context: System.ComponentModel.ITypeDescriptorContext, culture: System.Globalization.CultureInfo, value: System.Object, ) -> System.String:
        ...

    @typing.overload
    def CreateInstance(self, propertyValues: System.Collections.IDictionary, ) -> System.Object:
        ...

    @typing.overload
    def CreateInstance(self, context: System.ComponentModel.ITypeDescriptorContext, propertyValues: System.Collections.IDictionary, ) -> System.Object:
        ...

    @typing.overload
    def GetCreateInstanceSupported(self, ) -> System.Boolean:
        ...

    @typing.overload
    def GetCreateInstanceSupported(self, context: System.ComponentModel.ITypeDescriptorContext, ) -> System.Boolean:
        ...

    @typing.overload
    def GetProperties(self, value: System.Object, ) -> System.ComponentModel.PropertyDescriptorCollection:
        ...

    @typing.overload
    def GetProperties(self, context: System.ComponentModel.ITypeDescriptorContext, value: System.Object, ) -> System.ComponentModel.PropertyDescriptorCollection:
        ...

    @typing.overload
    def GetProperties(self, context: System.ComponentModel.ITypeDescriptorContext, value: System.Object, attributes: list[System.Attribute], ) -> System.ComponentModel.PropertyDescriptorCollection:
        ...

    @typing.overload
    def GetPropertiesSupported(self, ) -> System.Boolean:
        ...

    @typing.overload
    def GetPropertiesSupported(self, context: System.ComponentModel.ITypeDescriptorContext, ) -> System.Boolean:
        ...

    @typing.overload
    def GetStandardValues(self, ) -> System.Collections.ICollection:
        ...

    @typing.overload
    def GetStandardValues(self, context: System.ComponentModel.ITypeDescriptorContext, ) -> System.ComponentModel.TypeConverter.StandardValuesCollection:
        ...

    @typing.overload
    def GetStandardValuesExclusive(self, ) -> System.Boolean:
        ...

    @typing.overload
    def GetStandardValuesExclusive(self, context: System.ComponentModel.ITypeDescriptorContext, ) -> System.Boolean:
        ...

    @typing.overload
    def GetStandardValuesSupported(self, ) -> System.Boolean:
        ...

    @typing.overload
    def GetStandardValuesSupported(self, context: System.ComponentModel.ITypeDescriptorContext, ) -> System.Boolean:
        ...

    @typing.overload
    def IsValid(self, value: System.Object, ) -> System.Boolean:
        ...

    @typing.overload
    def IsValid(self, context: System.ComponentModel.ITypeDescriptorContext, value: System.Object, ) -> System.Boolean:
        ...

class DesignerSerializationVisibility(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    Hidden: System.Int32 = Hidden
    Visible: System.Int32 = Visible
    Content: System.Int32 = Content

class AttributeCollection(System.Collections.ICollection, System.Collections.IEnumerable, System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def Count(self) -> System.Int32:
        ...

    @property
    def Item(self) -> System.Attribute:
        ...

    @property
    def Item(self) -> System.Attribute:
        ...

    # methods
    @typing.overload
    def __init__(self, attributes: list[System.Attribute], ):
        ...

    @typing.overload
    @staticmethod
    def FromExisting(existing: System.ComponentModel.AttributeCollection, newAttributes: list[System.Attribute], ) -> System.ComponentModel.AttributeCollection:
        ...

    @typing.overload
    def Contains(self, attribute: System.Attribute, ) -> System.Boolean:
        ...

    @typing.overload
    def Contains(self, attributes: list[System.Attribute], ) -> System.Boolean:
        ...

    @typing.overload
    def GetEnumerator(self, ) -> System.Collections.IEnumerator:
        ...

    @typing.overload
    def Matches(self, attribute: System.Attribute, ) -> System.Boolean:
        ...

    @typing.overload
    def Matches(self, attributes: list[System.Attribute], ) -> System.Boolean:
        ...

    @typing.overload
    def CopyTo(self, array: System.Array, index: System.Int32, ) -> None:
        ...

class EventDescriptor(System.ComponentModel.MemberDescriptor, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @abc.abstractmethod
    @property
    def ComponentType(self) -> System.Type:
        ...

    @abc.abstractmethod
    @property
    def EventType(self) -> System.Type:
        ...

    @abc.abstractmethod
    @property
    def IsMulticast(self) -> System.Boolean:
        ...

    @property
    def Attributes(self) -> System.ComponentModel.AttributeCollection:
        ...

    @property
    def Category(self) -> System.String:
        ...

    @property
    def Description(self) -> System.String:
        ...

    @property
    def IsBrowsable(self) -> System.Boolean:
        ...

    @property
    def Name(self) -> System.String:
        ...

    @property
    def DesignTimeOnly(self) -> System.Boolean:
        ...

    @property
    def DisplayName(self) -> System.String:
        ...

    # methods
    @typing.overload
    @abc.abstractmethod
    def AddEventHandler(self, component: System.Object, value: System.Delegate, ) -> None:
        ...

    @typing.overload
    @abc.abstractmethod
    def RemoveEventHandler(self, component: System.Object, value: System.Delegate, ) -> None:
        ...

class EventDescriptorCollection(System.Collections.ICollection, System.Collections.IEnumerable, System.Collections.IList, System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def Count(self) -> System.Int32:
        ...

    @property
    def Item(self) -> System.ComponentModel.EventDescriptor:
        ...

    @property
    def Item(self) -> System.ComponentModel.EventDescriptor:
        ...

    # methods
    @typing.overload
    def __init__(self, events: list[System.ComponentModel.EventDescriptor], ):
        ...

    @typing.overload
    def __init__(self, events: list[System.ComponentModel.EventDescriptor], readOnly: System.Boolean, ):
        ...

    @typing.overload
    def Add(self, value: System.ComponentModel.EventDescriptor, ) -> System.Int32:
        ...

    @typing.overload
    def Clear(self, ) -> None:
        ...

    @typing.overload
    def Contains(self, value: System.ComponentModel.EventDescriptor, ) -> System.Boolean:
        ...

    @typing.overload
    def Find(self, name: System.String, ignoreCase: System.Boolean, ) -> System.ComponentModel.EventDescriptor:
        ...

    @typing.overload
    def IndexOf(self, value: System.ComponentModel.EventDescriptor, ) -> System.Int32:
        ...

    @typing.overload
    def Insert(self, index: System.Int32, value: System.ComponentModel.EventDescriptor, ) -> None:
        ...

    @typing.overload
    def Remove(self, value: System.ComponentModel.EventDescriptor, ) -> None:
        ...

    @typing.overload
    def RemoveAt(self, index: System.Int32, ) -> None:
        ...

    @typing.overload
    def GetEnumerator(self, ) -> System.Collections.IEnumerator:
        ...

    @typing.overload
    def Sort(self, ) -> System.ComponentModel.EventDescriptorCollection:
        ...

    @typing.overload
    def Sort(self, names: list[System.String], ) -> System.ComponentModel.EventDescriptorCollection:
        ...

    @typing.overload
    def Sort(self, names: list[System.String], comparer: System.Collections.IComparer, ) -> System.ComponentModel.EventDescriptorCollection:
        ...

    @typing.overload
    def Sort(self, comparer: System.Collections.IComparer, ) -> System.ComponentModel.EventDescriptorCollection:
        ...

class ITypeDescriptorContext(System.IServiceProvider, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @abc.abstractmethod
    @property
    def Container(self) -> System.ComponentModel.IContainer:
        ...

    @abc.abstractmethod
    @property
    def Instance(self) -> System.Object:
        ...

    @abc.abstractmethod
    @property
    def PropertyDescriptor(self) -> System.ComponentModel.PropertyDescriptor:
        ...

    # methods
    @typing.overload
    @abc.abstractmethod
    def OnComponentChanging(self, ) -> System.Boolean:
        ...

    @typing.overload
    @abc.abstractmethod
    def OnComponentChanged(self, ) -> None:
        ...

