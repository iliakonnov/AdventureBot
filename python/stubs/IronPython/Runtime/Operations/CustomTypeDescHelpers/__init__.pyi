from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import System.ComponentModel
import System
import System.Globalization


class SuperDynamicObjectPropertyDescriptor(System.ComponentModel.PropertyDescriptor):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def ComponentType(self) -> System.Type:
        ...

    @property
    def IsReadOnly(self) -> bool:
        ...

    @property
    def PropertyType(self) -> System.Type:
        ...

    @property
    def Converter(self) -> System.ComponentModel.TypeConverter:
        ...

    @property
    def IsLocalizable(self) -> bool:
        ...

    @property
    def SerializationVisibility(self) -> int:
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
    def __init__(self, name: str, propertyType: System.Type, componentType: System.Type, ):
        ...

    def GetValue(self, component: System.Object, ) -> System.Object:
        ...

    def SetValue(self, component: System.Object, value: System.Object, ) -> None:
        ...

    def CanResetValue(self, component: System.Object, ) -> bool:
        ...

    def ResetValue(self, component: System.Object, ) -> None:
        ...

    def ShouldSerializeValue(self, component: System.Object, ) -> bool:
        ...

class TypeConv(System.ComponentModel.TypeConverter):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    def __init__(self, self: System.Object, ):
        ...

    def CanConvertTo(self, context: System.ComponentModel.ITypeDescriptorContext, destinationType: System.Type, ) -> bool:
        ...

    def CanConvertFrom(self, context: System.ComponentModel.ITypeDescriptorContext, sourceType: System.Type, ) -> bool:
        ...

    def ConvertFrom(self, context: System.ComponentModel.ITypeDescriptorContext, culture: System.Globalization.CultureInfo, value: System.Object, ) -> System.Object:
        ...

    def ConvertTo(self, context: System.ComponentModel.ITypeDescriptorContext, culture: System.Globalization.CultureInfo, value: System.Object, destinationType: System.Type, ) -> System.Object:
        ...

    def GetCreateInstanceSupported(self, context: System.ComponentModel.ITypeDescriptorContext, ) -> bool:
        ...

    def GetPropertiesSupported(self, context: System.ComponentModel.ITypeDescriptorContext, ) -> bool:
        ...

    def GetStandardValuesSupported(self, context: System.ComponentModel.ITypeDescriptorContext, ) -> bool:
        ...

    def IsValid(self, context: System.ComponentModel.ITypeDescriptorContext, value: System.Object, ) -> bool:
        ...

