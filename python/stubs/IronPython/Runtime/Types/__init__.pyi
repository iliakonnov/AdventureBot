from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import System
import IronPython.Runtime.Types
import IronPython.Runtime.Types.ReflectedEvent
import System.Collections.Generic
import System.Reflection
import IronPython.Runtime
import System.Runtime.CompilerServices
import IronPython.Runtime.Binding
import System.Linq.Expressions
import System.Dynamic
import IronPython.Runtime.Operations
import IronPython.Runtime.Types.BuiltinFunction
import Microsoft.Scripting.Actions
import Microsoft.Scripting.Runtime
import System.Collections
import Microsoft.Scripting.Actions.Calls

T = typing.TypeVar('T')

class DynamicHelpers(System.Object, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    @staticmethod
    def GetPythonTypeFromType(type: System.Type, ) -> IronPython.Runtime.Types.PythonType:
        ...

    @staticmethod
    def GetPythonType(o: System.Object, ) -> IronPython.Runtime.Types.PythonType:
        ...

    @staticmethod
    def MakeBoundEvent(eventObj: IronPython.Runtime.Types.ReflectedEvent, instance: System.Object, type: System.Type, ) -> IronPython.Runtime.Types.ReflectedEvent.BoundEvent:
        ...

class CachedNewTypeInfo(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def InterfaceTypes(self) -> System.Collections.Generic.IList[System.Type]:
        ...

    @property
    def Type(self) -> System.Type:
        ...

    @property
    def SpecialNames(self) -> System.Collections.Generic.Dictionary[str, System.Array[str]]:
        ...

    # methods
    def __init__(self, type: System.Type, specialNames: System.Collections.Generic.Dictionary[str, System.Array[str]], interfaceTypes: System.Array[System.Type], ):
        ...

class NameConverter(System.Object, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    @staticmethod
    @typing.overload
    def TryGetName(dt: IronPython.Runtime.Types.PythonType, mi: System.Reflection.MethodInfo, name: ref[str], ) -> int:
        ...

    @staticmethod
    @typing.overload
    def TryGetName(dt: IronPython.Runtime.Types.PythonType, ei: System.Reflection.EventInfo, eventMethod: System.Reflection.MethodInfo, name: ref[str], ) -> int:
        ...

    @staticmethod
    @typing.overload
    def TryGetName(dt: IronPython.Runtime.Types.PythonType, pi: System.Reflection.PropertyInfo, prop: System.Reflection.MethodInfo, name: ref[str], ) -> int:
        ...

    @staticmethod
    def GetTypeName(t: System.Type, ) -> str:
        ...

    @staticmethod
    def GetNameFromMethod(dt: IronPython.Runtime.Types.PythonType, mi: System.Reflection.MethodInfo, res: int, name: ref[str], ) -> int:
        ...

class ReflectedProperty(IronPython.Runtime.ICodeFormattable, IronPython.Runtime.Types.ReflectedGetterSetter):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def CanOptimizeGets(self) -> bool:
        ...

    @property
    def DeclaringType(self) -> System.Type:
        ...

    @property
    def __name__(self) -> str:
        ...

    @property
    def Info(self) -> System.Reflection.PropertyInfo:
        ...

    @property
    def PropertyType(self) -> IronPython.Runtime.Types.PythonType:
        ...

    @property
    def GetAlwaysSucceeds(self) -> bool:
        ...

    @property
    def IsAlwaysVisible(self) -> bool:
        ...

    @property
    def __doc__(self) -> str:
        ...

    @property
    def __objclass__(self) -> IronPython.Runtime.Types.PythonType:
        ...

    @property
    def Getter(self) -> System.Array[System.Reflection.MethodInfo]:
        ...

    @property
    def Setter(self) -> System.Array[System.Reflection.MethodInfo]:
        ...

    @property
    def NameType(self) -> int:
        ...

    # methods
    @typing.overload
    def __init__(self, info: System.Reflection.PropertyInfo, getter: System.Reflection.MethodInfo, setter: System.Reflection.MethodInfo, nt: int, ):
        ...

    @typing.overload
    def __init__(self, info: System.Reflection.PropertyInfo, getters: System.Array[System.Reflection.MethodInfo], setters: System.Array[System.Reflection.MethodInfo], nt: int, ):
        ...

    def TrySetValue(self, context: IronPython.Runtime.CodeContext, instance: System.Object, owner: IronPython.Runtime.Types.PythonType, value: System.Object, ) -> bool:
        ...

    def TryGetValue(self, context: IronPython.Runtime.CodeContext, instance: System.Object, owner: IronPython.Runtime.Types.PythonType, value: ref[System.Object], ) -> bool:
        ...

    def CallGetter(self, context: IronPython.Runtime.CodeContext, owner: IronPython.Runtime.Types.PythonType, storage: IronPython.Runtime.SiteLocalStorage[System.Runtime.CompilerServices.CallSite[System.Func[System.Runtime.CompilerServices.CallSite, IronPython.Runtime.CodeContext, System.Object, System.Object]]], instance: System.Object, ) -> System.Object:
        ...

    @staticmethod
    def IsApplicableForType(type: System.Type, mt: System.Reflection.MethodInfo, ) -> bool:
        ...

    def TryDeleteValue(self, context: IronPython.Runtime.CodeContext, instance: System.Object, owner: IronPython.Runtime.Types.PythonType, ) -> bool:
        ...

    def MakeGetExpression(self, binder: IronPython.Runtime.Binding.PythonBinder, codeContext: System.Linq.Expressions.Expression, instance: System.Dynamic.DynamicMetaObject, owner: System.Dynamic.DynamicMetaObject, builder: IronPython.Runtime.Binding.ConditionalBuilder, ) -> None:
        ...

    def IsSetDescriptor(self, context: IronPython.Runtime.CodeContext, owner: IronPython.Runtime.Types.PythonType, ) -> bool:
        ...

    def GetValue(self, context: IronPython.Runtime.CodeContext, instance: System.Object, ) -> System.Object:
        ...

    def SetValue(self, context: IronPython.Runtime.CodeContext, instance: System.Object, value: System.Object, ) -> None:
        ...

    def __set__(self, context: IronPython.Runtime.CodeContext, instance: System.Object, value: System.Object, ) -> None:
        ...

    def __delete__(self, instance: System.Object, ) -> None:
        ...

    def __repr__(self, context: IronPython.Runtime.CodeContext, ) -> str:
        ...

class NotImplementedType(IronPython.Runtime.ICodeFormattable, System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def Value(self) -> IronPython.Runtime.Types.NotImplementedType:
        ...

    # methods
    def __init__(self, ):
        ...

    @staticmethod
    def __new__(context: IronPython.Runtime.CodeContext, cls: IronPython.Runtime.Types.PythonType, ) -> IronPython.Runtime.Types.NotImplementedType:
        ...

    def __repr__(self, context: IronPython.Runtime.CodeContext, ) -> str:
        ...

    def __hash__(self, ) -> int:
        ...

class ExtensionPropertyInfo(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def Getter(self) -> System.Reflection.MethodInfo:
        ...

    @property
    def Setter(self) -> System.Reflection.MethodInfo:
        ...

    @property
    def Deleter(self) -> System.Reflection.MethodInfo:
        ...

    @property
    def DeclaringType(self) -> System.Type:
        ...

    @property
    def Name(self) -> str:
        ...

    # methods
    def __init__(self, logicalDeclaringType: System.Type, mi: System.Reflection.MethodInfo, ):
        ...

    def GetPropertyMethods(self, mi: System.Reflection.MethodInfo, methodName: str, prefix: str, get: str, set: str, delete: str, ) -> None:
        ...

class ReflectedIndexer(IronPython.Runtime.Types.ReflectedGetterSetter):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def GetAlwaysSucceeds(self) -> bool:
        ...

    @property
    def DeclaringType(self) -> System.Type:
        ...

    @property
    def PropertyType(self) -> IronPython.Runtime.Types.PythonType:
        ...

    @property
    def __name__(self) -> str:
        ...

    @property
    def Item(self) -> System.Object:
        ...
    @Item.setter
    def Item(self, val: System.Object):
        ...

    @property
    def __objclass__(self) -> IronPython.Runtime.Types.PythonType:
        ...

    @property
    def Getter(self) -> System.Array[System.Reflection.MethodInfo]:
        ...

    @property
    def Setter(self) -> System.Array[System.Reflection.MethodInfo]:
        ...

    @property
    def NameType(self) -> int:
        ...

    @property
    def IsAlwaysVisible(self) -> bool:
        ...

    @property
    def CanOptimizeGets(self) -> bool:
        ...

    # methods
    @typing.overload
    def __init__(self, info: System.Reflection.PropertyInfo, nt: int, privateBinding: bool, ):
        ...

    @typing.overload
    def __init__(self, from_: IronPython.Runtime.Types.ReflectedIndexer, instance: System.Object, ):
        ...

    def TryGetValue(self, context: IronPython.Runtime.CodeContext, instance: System.Object, owner: IronPython.Runtime.Types.PythonType, value: ref[System.Object], ) -> bool:
        ...

    def SetValue(self, context: IronPython.Runtime.CodeContext, storage: IronPython.Runtime.SiteLocalStorage[System.Runtime.CompilerServices.CallSite[System.Func[System.Runtime.CompilerServices.CallSite, IronPython.Runtime.CodeContext, System.Object, System.Array[System.Object], System.Object]]], keys: System.Array[System.Object], value: System.Object, ) -> bool:
        ...

    def GetValue(self, context: IronPython.Runtime.CodeContext, storage: IronPython.Runtime.SiteLocalStorage[System.Runtime.CompilerServices.CallSite[System.Func[System.Runtime.CompilerServices.CallSite, IronPython.Runtime.CodeContext, System.Object, System.Array[System.Object], System.Object]]], keys: System.Array[System.Object], ) -> System.Object:
        ...

    def __get__(self, context: IronPython.Runtime.CodeContext, instance: System.Object, owner: System.Object, ) -> System.Object:
        ...

class Ellipsis(IronPython.Runtime.ICodeFormattable, System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def Value(self) -> IronPython.Runtime.Types.Ellipsis:
        ...

    # methods
    def __init__(self, ):
        ...

    @staticmethod
    def __new__(context: IronPython.Runtime.CodeContext, cls: IronPython.Runtime.Types.PythonType, ) -> IronPython.Runtime.Types.Ellipsis:
        ...

    def __repr__(self, context: IronPython.Runtime.CodeContext, ) -> str:
        ...

    def __hash__(self, ) -> int:
        ...

class ReflectedField(IronPython.Runtime.ICodeFormattable, IronPython.Runtime.Types.PythonTypeSlot):
    @typing.overload
    def __init__(self, **kwargs):
        self._info: System.Reflection.FieldInfo
        ...

    # static fields
    UpdateValueTypeFieldWarning: str = ...

    # properties
    @property
    def Info(self) -> System.Reflection.FieldInfo:
        ...

    @property
    def __doc__(self) -> str:
        ...

    @property
    def FieldType(self) -> IronPython.Runtime.Types.PythonType:
        ...

    @property
    def GetAlwaysSucceeds(self) -> bool:
        ...

    @property
    def CanOptimizeGets(self) -> bool:
        ...

    @property
    def IsAlwaysVisible(self) -> bool:
        ...

    # methods
    @typing.overload
    def __init__(self, info: System.Reflection.FieldInfo, nameType: int, ):
        ...

    @typing.overload
    def __init__(self, info: System.Reflection.FieldInfo, ):
        ...

    def GetValue(self, context: IronPython.Runtime.CodeContext, instance: System.Object, ) -> System.Object:
        ...

    def SetValue(self, context: IronPython.Runtime.CodeContext, instance: System.Object, value: System.Object, ) -> None:
        ...

    def __set__(self, context: IronPython.Runtime.CodeContext, instance: System.Object, value: System.Object, ) -> None:
        ...

    def TryGetValue(self, context: IronPython.Runtime.CodeContext, instance: System.Object, owner: IronPython.Runtime.Types.PythonType, value: ref[System.Object], ) -> bool:
        ...

    def TrySetValue(self, context: IronPython.Runtime.CodeContext, instance: System.Object, owner: IronPython.Runtime.Types.PythonType, value: System.Object, ) -> bool:
        ...

    def TrySetValueWorker(self, context: IronPython.Runtime.CodeContext, instance: System.Object, owner: IronPython.Runtime.Types.PythonType, value: System.Object, suppressWarning: bool, ) -> bool:
        ...

    def IsSetDescriptor(self, context: IronPython.Runtime.CodeContext, owner: IronPython.Runtime.Types.PythonType, ) -> bool:
        ...

    def TryDeleteValue(self, context: IronPython.Runtime.CodeContext, instance: System.Object, owner: IronPython.Runtime.Types.PythonType, ) -> bool:
        ...

    def MakeGetExpression(self, binder: IronPython.Runtime.Binding.PythonBinder, codeContext: System.Linq.Expressions.Expression, instance: System.Dynamic.DynamicMetaObject, owner: System.Dynamic.DynamicMetaObject, builder: IronPython.Runtime.Binding.ConditionalBuilder, ) -> None:
        ...

    def DoSet(self, context: IronPython.Runtime.CodeContext, instance: System.Object, val: System.Object, suppressWarning: bool, ) -> None:
        ...

    def ShouldSetOrDelete(self, type: IronPython.Runtime.Types.PythonType, ) -> bool:
        ...

    def __repr__(self, context: IronPython.Runtime.CodeContext, ) -> str:
        ...

class TypeCache(System.Object, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def Array(self) -> IronPython.Runtime.Types.PythonType:
        ...

    @property
    def BuiltinFunction(self) -> IronPython.Runtime.Types.PythonType:
        ...

    @property
    def Dict(self) -> IronPython.Runtime.Types.PythonType:
        ...

    @property
    def FrozenSet(self) -> IronPython.Runtime.Types.PythonType:
        ...

    @property
    def Function(self) -> IronPython.Runtime.Types.PythonType:
        ...

    @property
    def Builtin(self) -> IronPython.Runtime.Types.PythonType:
        ...

    @property
    def Object(self) -> IronPython.Runtime.Types.PythonType:
        ...

    @property
    def Set(self) -> IronPython.Runtime.Types.PythonType:
        ...

    @property
    def PythonType(self) -> IronPython.Runtime.Types.PythonType:
        ...

    @property
    def String(self) -> IronPython.Runtime.Types.PythonType:
        ...

    @property
    def Bytes(self) -> IronPython.Runtime.Types.PythonType:
        ...

    @property
    def PythonTuple(self) -> IronPython.Runtime.Types.PythonType:
        ...

    @property
    def WeakReference(self) -> IronPython.Runtime.Types.PythonType:
        ...

    @property
    def PythonList(self) -> IronPython.Runtime.Types.PythonType:
        ...

    @property
    def Module(self) -> IronPython.Runtime.Types.PythonType:
        ...

    @property
    def Method(self) -> IronPython.Runtime.Types.PythonType:
        ...

    @property
    def Enumerate(self) -> IronPython.Runtime.Types.PythonType:
        ...

    @property
    def Int32(self) -> IronPython.Runtime.Types.PythonType:
        ...

    @property
    def Single(self) -> IronPython.Runtime.Types.PythonType:
        ...

    @property
    def Double(self) -> IronPython.Runtime.Types.PythonType:
        ...

    @property
    def BigInteger(self) -> IronPython.Runtime.Types.PythonType:
        ...

    @property
    def Complex(self) -> IronPython.Runtime.Types.PythonType:
        ...

    @property
    def Super(self) -> IronPython.Runtime.Types.PythonType:
        ...

    @property
    def Null(self) -> IronPython.Runtime.Types.PythonType:
        ...

    @property
    def Boolean(self) -> IronPython.Runtime.Types.PythonType:
        ...

    @property
    def BaseException(self) -> IronPython.Runtime.Types.PythonType:
        ...

    # methods
class ConstructorFunction(IronPython.Runtime.ICodeFormattable, System.Dynamic.IDynamicMetaObjectProvider, IronPython.Runtime.Operations.IDelegateConvertible, IronPython.Runtime.Binding.IFastInvokable, IronPython.Runtime.Types.BuiltinFunction):
    @typing.overload
    def __init__(self, **kwargs):
        self._data: IronPython.Runtime.Types.BuiltinFunction.BuiltinFunctionData
        self._instance: System.Object
        ...

    # static fields

    # properties
    @property
    def ConstructorTargets(self) -> System.Collections.Generic.IList[System.Reflection.MethodBase]:
        ...

    @property
    def Overloads(self) -> IronPython.Runtime.Types.BuiltinFunctionOverloadMapper:
        ...

    @property
    def __name__(self) -> str:
        ...

    @property
    def __doc__(self) -> str:
        ...

    @property
    def IsUnbound(self) -> bool:
        ...

    @property
    def Name(self) -> str:
        ...
    @Name.setter
    def Name(self, val: str):
        ...

    @property
    def DeclaringType(self) -> System.Type:
        ...

    @property
    def Targets(self) -> System.Collections.Generic.IList[System.Reflection.MethodBase]:
        ...

    @property
    def IsAlwaysVisible(self) -> bool:
        ...

    @property
    def IsReversedOperator(self) -> bool:
        ...

    @property
    def IsBinaryOperator(self) -> bool:
        ...

    @property
    def FunctionType(self) -> int:
        ...
    @FunctionType.setter
    def FunctionType(self, val: int):
        ...

    @property
    def GetAlwaysSucceeds(self) -> bool:
        ...

    @property
    def OverloadDictionary(self) -> System.Collections.Generic.Dictionary[IronPython.Runtime.Types.BuiltinFunction.TypeList, IronPython.Runtime.Types.BuiltinFunction]:
        ...

    @property
    def __self__(self) -> System.Object:
        ...

    @property
    def BindingSelf(self) -> System.Object:
        ...

    @property
    def IsOnlyGeneric(self) -> bool:
        ...

    @property
    def CanOptimizeGets(self) -> bool:
        ...

    # methods
    def __init__(self, realTarget: IronPython.Runtime.Types.BuiltinFunction, constructors: System.Collections.Generic.IList[System.Reflection.MethodBase], ):
        ...

    @staticmethod
    def GetTargetsValidateFunction(realTarget: IronPython.Runtime.Types.BuiltinFunction, ) -> System.Collections.Generic.IList[System.Reflection.MethodBase]:
        ...

class PythonCachedTypeInfoAttribute(System.Attribute):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def TypeId(self) -> System.Object:
        ...

    # methods
    def __init__(self, ):
        ...

class ReflectedEvent(IronPython.Runtime.ICodeFormattable, IronPython.Runtime.Types.PythonTypeDataSlot):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def GetAlwaysSucceeds(self) -> bool:
        ...

    @property
    def IsAlwaysVisible(self) -> bool:
        ...

    @property
    def __doc__(self) -> str:
        ...

    @property
    def Info(self) -> System.Reflection.EventInfo:
        ...

    @property
    def Tracker(self) -> Microsoft.Scripting.Actions.EventTracker:
        ...

    @property
    def CanOptimizeGets(self) -> bool:
        ...

    # methods
    def __init__(self, tracker: Microsoft.Scripting.Actions.EventTracker, clsOnly: bool, ):
        ...

    def TryGetValue(self, context: IronPython.Runtime.CodeContext, instance: System.Object, owner: IronPython.Runtime.Types.PythonType, value: ref[System.Object], ) -> bool:
        ...

    def TrySetValue(self, context: IronPython.Runtime.CodeContext, instance: System.Object, owner: IronPython.Runtime.Types.PythonType, value: System.Object, ) -> bool:
        ...

    def EventInfosDiffer(self, et: IronPython.Runtime.Types.ReflectedEvent.BoundEvent, ) -> bool:
        ...

    def TryDeleteValue(self, context: IronPython.Runtime.CodeContext, instance: System.Object, owner: IronPython.Runtime.Types.PythonType, ) -> bool:
        ...

    def ReadOnlyException(self, dt: IronPython.Runtime.Types.PythonType, ) -> System.MissingMemberException:
        ...

    def __repr__(self, context: IronPython.Runtime.CodeContext, ) -> str:
        ...

class ReflectedExtensionProperty(IronPython.Runtime.Types.ReflectedGetterSetter):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def GetAlwaysSucceeds(self) -> bool:
        ...

    @property
    def CanOptimizeGets(self) -> bool:
        ...

    @property
    def DeclaringType(self) -> System.Type:
        ...

    @property
    def ExtInfo(self) -> IronPython.Runtime.Types.ExtensionPropertyInfo:
        ...

    @property
    def __name__(self) -> str:
        ...

    @property
    def __doc__(self) -> str:
        ...

    @property
    def __objclass__(self) -> IronPython.Runtime.Types.PythonType:
        ...

    @property
    def Getter(self) -> System.Array[System.Reflection.MethodInfo]:
        ...

    @property
    def Setter(self) -> System.Array[System.Reflection.MethodInfo]:
        ...

    @property
    def PropertyType(self) -> IronPython.Runtime.Types.PythonType:
        ...

    @property
    def NameType(self) -> int:
        ...

    @property
    def IsAlwaysVisible(self) -> bool:
        ...

    # methods
    def __init__(self, info: IronPython.Runtime.Types.ExtensionPropertyInfo, nt: int, ):
        ...

    def TryGetValue(self, context: IronPython.Runtime.CodeContext, instance: System.Object, owner: IronPython.Runtime.Types.PythonType, value: ref[System.Object], ) -> bool:
        ...

    def TrySetValue(self, context: IronPython.Runtime.CodeContext, instance: System.Object, owner: IronPython.Runtime.Types.PythonType, value: System.Object, ) -> bool:
        ...

    def TryDeleteValue(self, context: IronPython.Runtime.CodeContext, instance: System.Object, owner: IronPython.Runtime.Types.PythonType, ) -> bool:
        ...

    def IsSetDescriptor(self, context: IronPython.Runtime.CodeContext, owner: IronPython.Runtime.Types.PythonType, ) -> bool:
        ...

    def __set__(self, context: IronPython.Runtime.CodeContext, instance: System.Object, value: System.Object, ) -> None:
        ...

    def __delete__(self, context: IronPython.Runtime.CodeContext, instance: System.Object, ) -> None:
        ...

class PythonType(IronPython.Runtime.IPythonMembersList, Microsoft.Scripting.Runtime.IMembersList, System.Dynamic.IDynamicMetaObjectProvider, IronPython.Runtime.IWeakReferenceable, IronPython.Runtime.IWeakReferenceableByProxy, IronPython.Runtime.ICodeFormattable, IronPython.Runtime.Binding.IFastGettable, IronPython.Runtime.Binding.IFastSettable, IronPython.Runtime.Binding.IFastInvokable, System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        self._cachedGets: System.Collections.Generic.Dictionary[IronPython.Runtime.Types.CachedGetKey, IronPython.Runtime.Binding.FastGetBase]
        self._cachedTryGets: System.Collections.Generic.Dictionary[IronPython.Runtime.Types.CachedGetKey, IronPython.Runtime.Binding.FastGetBase]
        self._cachedSets: System.Collections.Generic.Dictionary[IronPython.Runtime.Types.SetMemberKey, IronPython.Runtime.Binding.FastSetBase]
        self._cachedTypeGets: System.Collections.Generic.Dictionary[str, IronPython.Runtime.Types.TypeGetBase]
        self._cachedTypeTryGets: System.Collections.Generic.Dictionary[str, IronPython.Runtime.Types.TypeGetBase]
        self._makeException: System.Func[str, System.Exception, System.Exception]
        ...

    # static fields
    DefaultMakeException: System.Func[str, System.Exception, System.Exception] = ...
    DefaultMakeExceptionNoInnerException: System.Func[str, System.Exception] = ...
    __dict__: IronPython.Runtime.Types.PythonTypeSlot = ...

    # properties
    @property
    def Ctor(self) -> IronPython.Runtime.Types.BuiltinFunction:
        ...

    @property
    def Item(self) -> IronPython.Runtime.Types.PythonType:
        ...

    @property
    def Item(self) -> System.Object:
        ...

    @property
    def SlotCount(self) -> int:
        ...

    @property
    def Name(self) -> str:
        ...
    @Name.setter
    def Name(self, val: str):
        ...

    @property
    def QualName(self) -> str:
        ...
    @QualName.setter
    def QualName(self, val: str):
        ...

    @property
    def Version(self) -> int:
        ...

    @property
    def IsNull(self) -> bool:
        ...

    @property
    def ResolutionOrder(self) -> System.Collections.Generic.IList[IronPython.Runtime.Types.PythonType]:
        ...
    @ResolutionOrder.setter
    def ResolutionOrder(self, val: System.Collections.Generic.IList[IronPython.Runtime.Types.PythonType]):
        ...

    @property
    def HashSite(self) -> System.Runtime.CompilerServices.CallSite[System.Func[System.Runtime.CompilerServices.CallSite, System.Object, int]]:
        ...

    @property
    def UnderlyingSystemType(self) -> System.Type:
        ...

    @property
    def FinalSystemType(self) -> System.Type:
        ...

    @property
    def ExtensionType(self) -> System.Type:
        ...

    @property
    def BaseTypes(self) -> System.Collections.Generic.IList[IronPython.Runtime.Types.PythonType]:
        ...
    @BaseTypes.setter
    def BaseTypes(self, val: System.Collections.Generic.IList[IronPython.Runtime.Types.PythonType]):
        ...

    @property
    def IsSystemType(self) -> bool:
        ...
    @IsSystemType.setter
    def IsSystemType(self, val: bool):
        ...

    @property
    def IsWeakReferencable(self) -> bool:
        ...
    @IsWeakReferencable.setter
    def IsWeakReferencable(self, val: bool):
        ...

    @property
    def HasDictionary(self) -> bool:
        ...
    @HasDictionary.setter
    def HasDictionary(self, val: bool):
        ...

    @property
    def HasSystemCtor(self) -> bool:
        ...

    @property
    def IsPythonType(self) -> bool:
        ...
    @IsPythonType.setter
    def IsPythonType(self, val: bool):
        ...

    @property
    def PythonContext(self) -> IronPython.Runtime.PythonContext:
        ...

    @property
    def Context(self) -> IronPython.Runtime.PythonContext:
        ...

    @property
    def SyncRoot(self) -> System.Object:
        ...

    @property
    def ExtensionMethods(self) -> System.Collections.Generic.Dictionary[str, System.Collections.Generic.List[System.Reflection.MethodInfo]]:
        ...

    @property
    def SubTypes(self) -> System.Collections.Generic.IList[System.WeakReference]:
        ...

    # methods
    @typing.overload
    def __init__(self, context: IronPython.Runtime.CodeContext, name: str, bases: IronPython.Runtime.PythonTuple, dict: IronPython.Runtime.PythonDictionary, ):
        ...

    @typing.overload
    def __init__(self, context: IronPython.Runtime.CodeContext, name: str, bases: IronPython.Runtime.PythonTuple, dict: IronPython.Runtime.PythonDictionary, selfNames: str, ):
        ...

    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def __init__(self, underlyingSystemType: System.Type, ):
        ...

    @typing.overload
    def __init__(self, baseType: IronPython.Runtime.Types.PythonType, name: str, exceptionMaker: System.Func[str, System.Exception, System.Exception], ):
        ...

    @typing.overload
    def __init__(self, baseTypes: System.Array[IronPython.Runtime.Types.PythonType], name: str, ):
        ...

    @typing.overload
    def __init__(self, baseTypes: System.Array[IronPython.Runtime.Types.PythonType], underlyingType: System.Type, name: str, exceptionMaker: System.Func[str, System.Exception, System.Exception], ):
        ...

    @typing.overload
    def __init__(self, context: IronPython.Runtime.PythonContext, baseType: IronPython.Runtime.Types.PythonType, name: str, module: str, doc: str, exceptionMaker: System.Func[str, System.Exception, System.Exception], ):
        ...

    @typing.overload
    def __init__(self, context: IronPython.Runtime.PythonContext, baseTypes: System.Array[IronPython.Runtime.Types.PythonType], name: str, module: str, doc: str, ):
        ...

    @typing.overload
    def __init__(self, context: IronPython.Runtime.PythonContext, baseTypes: System.Array[IronPython.Runtime.Types.PythonType], underlyingType: System.Type, name: str, module: str, doc: str, exceptionMaker: System.Func[str, System.Exception, System.Exception], ):
        ...

    def GetWeakRef(self, ) -> IronPython.Runtime.WeakRefTracker:
        ...

    def SetWeakRef(self, value: IronPython.Runtime.WeakRefTracker, ) -> bool:
        ...

    def SetFinalizer(self, value: IronPython.Runtime.WeakRefTracker, ) -> None:
        ...

    def GetWeakRefProxy(self, context: IronPython.Runtime.PythonContext, ) -> IronPython.Runtime.IWeakReferenceable:
        ...

    def GetMetaObject(self, parameter: System.Linq.Expressions.Expression, ) -> System.Dynamic.DynamicMetaObject:
        ...

    def GetSharedWeakReference(self, ) -> System.WeakReference:
        ...

    def MakeSetBinding(self, site: System.Runtime.CompilerServices.CallSite[T], binder: IronPython.Runtime.Binding.PythonSetMemberBinder, ) -> T:
        ...

    @staticmethod
    def MakeFastSet(context: IronPython.Runtime.CodeContext, name: str, ) -> System.Func[System.Runtime.CompilerServices.CallSite, System.Object, T, System.Object]:
        ...

    def MakeInvokeBinding(self, site: System.Runtime.CompilerServices.CallSite[T], binder: IronPython.Runtime.Binding.PythonInvokeBinder, context: IronPython.Runtime.CodeContext, args: System.Array[System.Object], ) -> IronPython.Runtime.Binding.FastBindResult[T]:
        ...

    @typing.overload
    def GetPythonType(self, site: System.Runtime.CompilerServices.CallSite, context: IronPython.Runtime.CodeContext, type: System.Object, instance: System.Object, ) -> System.Object:
        ...

    @staticmethod
    @typing.overload
    def GetPythonType(type: System.Type, ) -> IronPython.Runtime.Types.PythonType:
        ...

    def EmptySet(self, site: System.Runtime.CompilerServices.CallSite, context: IronPython.Runtime.CodeContext, type: System.Object, ) -> System.Object:
        ...

    def NewObject(self, site: System.Runtime.CompilerServices.CallSite, context: IronPython.Runtime.CodeContext, type: System.Object, ) -> System.Object:
        ...

    def SetConstructor(self, ctor: IronPython.Runtime.Types.BuiltinFunction, ) -> None:
        ...

    def IsHiddenMember(self, name: str, ) -> bool:
        ...

    def GetLateBoundInitBinder(self, signature: Microsoft.Scripting.Actions.CallSignature, ) -> IronPython.Runtime.Types.LateBoundInitBinder:
        ...

    def TryLookupSlot(self, context: IronPython.Runtime.CodeContext, name: str, slot: ref[IronPython.Runtime.Types.PythonTypeSlot], ) -> bool:
        ...

    @typing.overload
    def TryResolveSlot(self, context: IronPython.Runtime.CodeContext, name: str, slot: ref[IronPython.Runtime.Types.PythonTypeSlot], ) -> bool:
        ...

    @typing.overload
    def TryResolveSlot(self, context: IronPython.Runtime.CodeContext, instance: System.Object, name: str, value: ref[System.Object], ) -> bool:
        ...

    def AddSlot(self, name: str, slot: IronPython.Runtime.Types.PythonTypeSlot, ) -> None:
        ...

    def ClearObjectNewInSubclasses(self, pt: IronPython.Runtime.Types.PythonType, ) -> None:
        ...

    def ClearObjectInitInSubclasses(self, pt: IronPython.Runtime.Types.PythonType, ) -> None:
        ...

    def TryGetCustomSetAttr(self, context: IronPython.Runtime.CodeContext, pts: ref[IronPython.Runtime.Types.PythonTypeSlot], ) -> bool:
        ...

    def SetCustomMember(self, context: IronPython.Runtime.CodeContext, name: str, value: System.Object, ) -> None:
        ...

    @staticmethod
    def ToTypeSlot(value: System.Object, ) -> IronPython.Runtime.Types.PythonTypeSlot:
        ...

    def DeleteCustomMember(self, context: IronPython.Runtime.CodeContext, name: str, ) -> bool:
        ...

    def TryGetBoundCustomMember(self, context: IronPython.Runtime.CodeContext, name: str, value: ref[System.Object], ) -> bool:
        ...

    def MakeGetBinding(self, site: System.Runtime.CompilerServices.CallSite[T], binder: IronPython.Runtime.Binding.PythonGetMemberBinder, context: IronPython.Runtime.CodeContext, name: str, ) -> T:
        ...

    def GetMember(self, context: IronPython.Runtime.CodeContext, instance: System.Object, name: str, ) -> System.Object:
        ...

    def SetMember(self, context: IronPython.Runtime.CodeContext, instance: System.Object, name: str, value: System.Object, ) -> None:
        ...

    def DeleteMember(self, context: IronPython.Runtime.CodeContext, instance: System.Object, name: str, ) -> None:
        ...

    def TryGetMember(self, context: IronPython.Runtime.CodeContext, instance: System.Object, name: str, value: ref[System.Object], ) -> bool:
        ...

    def TryGetNonCustomMember(self, context: IronPython.Runtime.CodeContext, instance: System.Object, name: str, value: ref[System.Object], ) -> bool:
        ...

    def TryGetBoundMember(self, context: IronPython.Runtime.CodeContext, instance: System.Object, name: str, value: ref[System.Object], ) -> bool:
        ...

    def InvokeGetAttributeMethod(self, context: IronPython.Runtime.CodeContext, name: str, getattr: System.Object, ) -> System.Object:
        ...

    def TryGetNonCustomBoundMember(self, context: IronPython.Runtime.CodeContext, instance: System.Object, name: str, value: ref[System.Object], ) -> bool:
        ...

    def TryResolveNonObjectSlot(self, context: IronPython.Runtime.CodeContext, instance: System.Object, name: str, value: ref[System.Object], ) -> bool:
        ...

    def TrySetMember(self, context: IronPython.Runtime.CodeContext, instance: System.Object, name: str, value: System.Object, ) -> bool:
        ...

    def TrySetNonCustomMember(self, context: IronPython.Runtime.CodeContext, instance: System.Object, name: str, value: System.Object, ) -> bool:
        ...

    def TryDeleteMember(self, context: IronPython.Runtime.CodeContext, instance: System.Object, name: str, ) -> bool:
        ...

    def TryDeleteNonCustomMember(self, context: IronPython.Runtime.CodeContext, instance: System.Object, name: str, ) -> bool:
        ...

    @typing.overload
    def GetMemberNames(self, context: IronPython.Runtime.CodeContext, ) -> IronPython.Runtime.PythonList:
        ...

    @typing.overload
    def GetMemberNames(self, context: IronPython.Runtime.CodeContext, self: System.Object, ) -> IronPython.Runtime.PythonList:
        ...

    def TryGetCustomDir(self, context: IronPython.Runtime.CodeContext, self: System.Object, ) -> IronPython.Runtime.PythonList:
        ...

    @staticmethod
    def AddUserTypeMembers(context: IronPython.Runtime.CodeContext, keys: System.Collections.Generic.Dictionary[str, str], dt: IronPython.Runtime.Types.PythonType, res: IronPython.Runtime.PythonList, ) -> None:
        ...

    @staticmethod
    def AddOneMember(keys: System.Collections.Generic.Dictionary[str, str], res: IronPython.Runtime.PythonList, name: System.Object, ) -> None:
        ...

    @staticmethod
    def AddInstanceMembers(self: System.Object, keys: System.Collections.Generic.Dictionary[str, str], res: IronPython.Runtime.PythonList, ) -> IronPython.Runtime.PythonList:
        ...

    @typing.overload
    def GetMemberDictionary(self, context: IronPython.Runtime.CodeContext, ) -> IronPython.Runtime.PythonDictionary:
        ...

    @typing.overload
    def GetMemberDictionary(self, context: IronPython.Runtime.CodeContext, excludeDict: bool, ) -> IronPython.Runtime.PythonDictionary:
        ...

    def InitializeUserType(self, context: IronPython.Runtime.CodeContext, name: str, bases: IronPython.Runtime.PythonTuple, vars: IronPython.Runtime.PythonDictionary, selfNames: str, ) -> None:
        ...

    def MakeDictionary(self, ) -> IronPython.Runtime.PythonDictionary:
        ...

    def GetOptimizedInstanceNames(self, ) -> System.Collections.Generic.IList[str]:
        ...

    def GetOptimizedInstanceVersion(self, ) -> int:
        ...

    def GetTypeSlots(self, ) -> System.Collections.Generic.IList[str]:
        ...

    @staticmethod
    def GetSlots(dict: IronPython.Runtime.PythonDictionary, ) -> System.Collections.Generic.List[str]:
        ...

    @staticmethod
    def SlotsToList(slots: System.Object, ) -> System.Collections.Generic.List[str]:
        ...

    def HasObjectNew(self, context: IronPython.Runtime.CodeContext, ) -> bool:
        ...

    def HasObjectInit(self, context: IronPython.Runtime.CodeContext, ) -> bool:
        ...

    def UpdateObjectNewAndInit(self, context: IronPython.Runtime.CodeContext, ) -> None:
        ...

    @staticmethod
    def GetSlotName(o: System.Object, ) -> str:
        ...

    def GetUsedSlotCount(self, ) -> int:
        ...

    def PopulateDictionary(self, context: IronPython.Runtime.CodeContext, name: str, bases: IronPython.Runtime.PythonTuple, vars: IronPython.Runtime.PythonDictionary, ) -> None:
        ...

    def CheckForSlotWithDefault(self, context: IronPython.Runtime.CodeContext, resolutionOrder: System.Collections.Generic.IList[IronPython.Runtime.Types.PythonType], slots: System.Collections.Generic.List[str], name: str, ) -> bool:
        ...

    def __clrtype__(self, ) -> System.Type:
        ...

    def PopulateSlot(self, key: str, value: System.Object, ) -> None:
        ...

    @staticmethod
    def GetBasesAsList(bases: IronPython.Runtime.PythonTuple, ) -> System.Collections.Generic.List[IronPython.Runtime.Types.PythonType]:
        ...

    @staticmethod
    def ValidateBases(bases: IronPython.Runtime.PythonTuple, ) -> IronPython.Runtime.PythonTuple:
        ...

    @staticmethod
    def EnsureModule(context: IronPython.Runtime.CodeContext, dict: IronPython.Runtime.PythonDictionary, ) -> None:
        ...

    def InitializeSystemType(self, ) -> None:
        ...

    def AddSystemBases(self, ) -> None:
        ...

    def AddSystemInterfaces(self, mro: System.Collections.Generic.List[IronPython.Runtime.Types.PythonType], ) -> None:
        ...

    def AddSystemConstructors(self, ) -> None:
        ...

    def GetConstructors(self, ) -> IronPython.Runtime.Types.BuiltinFunction:
        ...

    def EnsureConstructor(self, ) -> None:
        ...

    def EnsureInstanceCtor(self, ) -> None:
        ...

    def UpdateVersion(self, ) -> None:
        ...

    @staticmethod
    def GetNextVersion() -> int:
        ...

    def EnsureDict(self, ) -> None:
        ...

    def AddSubType(self, subtype: IronPython.Runtime.Types.PythonType, ) -> None:
        ...

    def RemoveSubType(self, subtype: IronPython.Runtime.Types.PythonType, ) -> None:
        ...

    def GetMemberNames(self, ) -> System.Collections.Generic.IList[str]:
        ...

    def GetMemberNames(self, context: IronPython.Runtime.CodeContext, ) -> System.Collections.Generic.IList[System.Object]:
        ...

    @staticmethod
    @typing.overload
    def __new__(context: IronPython.Runtime.CodeContext, cls: IronPython.Runtime.Types.PythonType, name: str, bases: IronPython.Runtime.PythonTuple, dict: IronPython.Runtime.PythonDictionary, ) -> System.Object:
        ...

    @staticmethod
    @typing.overload
    def __new__(context: IronPython.Runtime.CodeContext, cls: IronPython.Runtime.Types.PythonType, name: str, bases: IronPython.Runtime.PythonTuple, dict: IronPython.Runtime.PythonDictionary, selfNames: str, ) -> System.Object:
        ...

    @staticmethod
    @typing.overload
    def __new__(context: IronPython.Runtime.CodeContext, cls: System.Object, o: System.Object, ) -> System.Object:
        ...

    @typing.overload
    def __init__(self, name: str, bases: IronPython.Runtime.PythonTuple, dict: IronPython.Runtime.PythonDictionary, kwargs: System.Collections.Generic.IDictionary[System.Object, System.Object], ) -> None:
        ...

    @typing.overload
    def __init__(self, o: System.Object, ) -> None:
        ...

    @staticmethod
    def FindMetaClass(cls: IronPython.Runtime.Types.PythonType, bases: IronPython.Runtime.PythonTuple, ) -> IronPython.Runtime.Types.PythonType:
        ...

    def GetBasesTuple(self, ) -> IronPython.Runtime.PythonTuple:
        ...

    def SetAbstractMethodFlags(self, name: str, value: System.Object, ) -> bool:
        ...

    def IsIterable(self, context: IronPython.Runtime.CodeContext, ) -> bool:
        ...

    def ClearAbstractMethodFlags(self, name: str, ) -> None:
        ...

    def HasAbstractMethods(self, context: IronPython.Runtime.CodeContext, ) -> bool:
        ...

    def GetAbstractErrorMessage(self, context: IronPython.Runtime.CodeContext, ) -> str:
        ...

    @staticmethod
    def CalculateMro(type: IronPython.Runtime.Types.PythonType, ldt: System.Collections.Generic.IList[IronPython.Runtime.Types.PythonType], ) -> System.Collections.Generic.List[IronPython.Runtime.Types.PythonType]:
        ...

    @staticmethod
    def TryReplaceExtensibleWithBase(curType: System.Type, newType: ref[System.Type], ) -> bool:
        ...

    @typing.overload
    def __call__(self, context: IronPython.Runtime.CodeContext, args: System.Array[System.Object], ) -> System.Object:
        ...

    @typing.overload
    def __call__(self, context: IronPython.Runtime.CodeContext, kwArgs: System.Collections.Generic.IDictionary[str, System.Object], args: System.Array[System.Object], ) -> System.Object:
        ...

    def __delattr__(self, context: IronPython.Runtime.CodeContext, name: str, ) -> None:
        ...

    def __getattribute__(self, context: IronPython.Runtime.CodeContext, name: str, ) -> System.Object:
        ...

    @staticmethod
    def __prepare__(kwargs: System.Collections.Generic.IDictionary[System.Object, System.Object], args: System.Array[System.Object], ) -> IronPython.Runtime.PythonDictionary:
        ...

    def __repr__(self, context: IronPython.Runtime.CodeContext, ) -> str:
        ...

    def GetTypeDebuggerDisplay(self, ) -> str:
        ...

    def __setattr__(self, context: IronPython.Runtime.CodeContext, name: str, value: System.Object, ) -> None:
        ...

    def __subclasses__(self, context: IronPython.Runtime.CodeContext, ) -> IronPython.Runtime.PythonList:
        ...

    def mro(self, ) -> IronPython.Runtime.PythonList:
        ...

    def __instancecheck__(self, instance: System.Object, ) -> bool:
        ...

    def __subclasscheck__(self, sub: IronPython.Runtime.Types.PythonType, ) -> bool:
        ...

    def SubclassImpl(self, sub: IronPython.Runtime.Types.PythonType, ) -> bool:
        ...

    @staticmethod
    def SetPythonType(type: System.Type, pyType: IronPython.Runtime.Types.PythonType, ) -> IronPython.Runtime.Types.PythonType:
        ...

    @typing.overload
    def CreateInstance(self, context: IronPython.Runtime.CodeContext, ) -> System.Object:
        ...

    @typing.overload
    def CreateInstance(self, context: IronPython.Runtime.CodeContext, arg0: System.Object, ) -> System.Object:
        ...

    @typing.overload
    def CreateInstance(self, context: IronPython.Runtime.CodeContext, arg0: System.Object, arg1: System.Object, ) -> System.Object:
        ...

    @typing.overload
    def CreateInstance(self, context: IronPython.Runtime.CodeContext, arg0: System.Object, arg1: System.Object, arg2: System.Object, ) -> System.Object:
        ...

    @typing.overload
    def CreateInstance(self, context: IronPython.Runtime.CodeContext, args: System.Array[System.Object], ) -> System.Object:
        ...

    @typing.overload
    def CreateInstance(self, context: IronPython.Runtime.CodeContext, args: System.Array[System.Object], names: System.Array[str], ) -> System.Object:
        ...

    def Hash(self, o: System.Object, ) -> int:
        ...

    def TryGetLength(self, context: IronPython.Runtime.CodeContext, o: System.Object, length: ref[int], ) -> bool:
        ...

    def EqualRetBool(self, self: System.Object, other: System.Object, ) -> bool:
        ...

    def GetTryGetMemberSite(self, context: IronPython.Runtime.CodeContext, name: str, ) -> System.Runtime.CompilerServices.CallSite[System.Func[System.Runtime.CompilerServices.CallSite, System.Object, IronPython.Runtime.CodeContext, System.Object]]:
        ...

    def TryGetBoundAttr(self, context: IronPython.Runtime.CodeContext, o: System.Object, name: str, ret: ref[System.Object], ) -> bool:
        ...

    def EnsureHashSite(self, ) -> None:
        ...

    def IsSubclassOf(self, other: IronPython.Runtime.Types.PythonType, ) -> bool:
        ...

    def IsSubclassWorker(self, other: IronPython.Runtime.Types.PythonType, ) -> bool:
        ...

class PythonTypeTypeSlot(IronPython.Runtime.Types.PythonTypeDataSlot):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields
    __doc__: str = ...

    # properties
    @property
    def GetAlwaysSucceeds(self) -> bool:
        ...

    @property
    def IsAlwaysVisible(self) -> bool:
        ...

    @property
    def CanOptimizeGets(self) -> bool:
        ...

    # methods
    def __init__(self, ):
        ...

    def TryGetValue(self, context: IronPython.Runtime.CodeContext, instance: System.Object, owner: IronPython.Runtime.Types.PythonType, value: ref[System.Object], ) -> bool:
        ...

    def TrySetValue(self, context: IronPython.Runtime.CodeContext, instance: System.Object, owner: IronPython.Runtime.Types.PythonType, value: System.Object, ) -> bool:
        ...

    def TryDeleteValue(self, context: IronPython.Runtime.CodeContext, instance: System.Object, owner: IronPython.Runtime.Types.PythonType, ) -> bool:
        ...

class BuiltinFunction(IronPython.Runtime.ICodeFormattable, System.Dynamic.IDynamicMetaObjectProvider, IronPython.Runtime.Operations.IDelegateConvertible, IronPython.Runtime.Binding.IFastInvokable, IronPython.Runtime.Types.PythonTypeSlot):
    @typing.overload
    def __init__(self, **kwargs):
        self._data: IronPython.Runtime.Types.BuiltinFunction.BuiltinFunctionData
        self._instance: System.Object
        ...

    # static fields

    # properties
    @property
    def IsUnbound(self) -> bool:
        ...

    @property
    def Name(self) -> str:
        ...
    @Name.setter
    def Name(self, val: str):
        ...

    @property
    def DeclaringType(self) -> System.Type:
        ...

    @property
    def Targets(self) -> System.Collections.Generic.IList[System.Reflection.MethodBase]:
        ...

    @property
    def IsAlwaysVisible(self) -> bool:
        ...

    @property
    def IsReversedOperator(self) -> bool:
        ...

    @property
    def IsBinaryOperator(self) -> bool:
        ...

    @property
    def FunctionType(self) -> int:
        ...
    @FunctionType.setter
    def FunctionType(self, val: int):
        ...

    @property
    def GetAlwaysSucceeds(self) -> bool:
        ...

    @property
    def Overloads(self) -> IronPython.Runtime.Types.BuiltinFunctionOverloadMapper:
        ...

    @property
    def OverloadDictionary(self) -> System.Collections.Generic.Dictionary[IronPython.Runtime.Types.BuiltinFunction.TypeList, IronPython.Runtime.Types.BuiltinFunction]:
        ...

    @property
    def __name__(self) -> str:
        ...

    @property
    def __doc__(self) -> str:
        ...

    @property
    def __self__(self) -> System.Object:
        ...

    @property
    def BindingSelf(self) -> System.Object:
        ...

    @property
    def IsBuiltinModuleMethod(self) -> bool:
        ...

    @property
    def IsOnlyGeneric(self) -> bool:
        ...

    @property
    def BinderType(self) -> int:
        ...

    @property
    def CanOptimizeGets(self) -> bool:
        ...

    # methods
    @typing.overload
    def __init__(self, name: str, originalTargets: System.Array[System.Reflection.MethodBase], declaringType: System.Type, functionType: int, ):
        ...

    @typing.overload
    def __init__(self, instance: System.Object, data: IronPython.Runtime.Types.BuiltinFunction.BuiltinFunctionData, ):
        ...

    @staticmethod
    def MakeFunction(name: str, infos: System.Array[System.Reflection.MethodBase], declaringType: System.Type, ) -> IronPython.Runtime.Types.BuiltinFunction:
        ...

    @staticmethod
    def MakeMethod(name: str, infos: System.Array[System.Reflection.MethodBase], declaringType: System.Type, ft: int, ) -> IronPython.Runtime.Types.BuiltinFunction:
        ...

    def BindToInstance(self, instance: System.Object, ) -> IronPython.Runtime.Types.BuiltinFunction:
        ...

    def AddMethod(self, mi: System.Reflection.MethodInfo, ) -> None:
        ...

    def TestData(self, data: System.Object, ) -> bool:
        ...

    @typing.overload
    def Call(self, context: IronPython.Runtime.CodeContext, storage: IronPython.Runtime.SiteLocalStorage[System.Runtime.CompilerServices.CallSite[System.Func[System.Runtime.CompilerServices.CallSite, IronPython.Runtime.CodeContext, System.Object, System.Array[System.Object], System.Object]]], instance: System.Object, args: System.Array[System.Object], ) -> System.Object:
        ...

    @typing.overload
    def Call(self, context: IronPython.Runtime.CodeContext, storage: IronPython.Runtime.SiteLocalStorage[System.Runtime.CompilerServices.CallSite[System.Func[System.Runtime.CompilerServices.CallSite, IronPython.Runtime.CodeContext, System.Object, System.Array[System.Object], System.Collections.Generic.IDictionary[System.Object, System.Object], System.Object]]], instance: System.Object, args: System.Array[System.Object], keywordArgs: System.Collections.Generic.IDictionary[System.Object, System.Object], ) -> System.Object:
        ...

    def Call0(self, context: IronPython.Runtime.CodeContext, storage: IronPython.Runtime.SiteLocalStorage[System.Runtime.CompilerServices.CallSite[System.Func[System.Runtime.CompilerServices.CallSite, IronPython.Runtime.CodeContext, System.Object, System.Object]]], instance: System.Object, ) -> System.Object:
        ...

    @staticmethod
    @typing.overload
    def GetInitializedStorage(context: IronPython.Runtime.CodeContext, storage: IronPython.Runtime.SiteLocalStorage[System.Runtime.CompilerServices.CallSite[System.Func[System.Runtime.CompilerServices.CallSite, IronPython.Runtime.CodeContext, System.Object, System.Array[System.Object], System.Object]]], ) -> IronPython.Runtime.SiteLocalStorage[System.Runtime.CompilerServices.CallSite[System.Func[System.Runtime.CompilerServices.CallSite, IronPython.Runtime.CodeContext, System.Object, System.Array[System.Object], System.Object]]]:
        ...

    @staticmethod
    @typing.overload
    def GetInitializedStorage(context: IronPython.Runtime.CodeContext, storage: IronPython.Runtime.SiteLocalStorage[System.Runtime.CompilerServices.CallSite[System.Func[System.Runtime.CompilerServices.CallSite, IronPython.Runtime.CodeContext, System.Object, System.Object]]], ) -> IronPython.Runtime.SiteLocalStorage[System.Runtime.CompilerServices.CallSite[System.Func[System.Runtime.CompilerServices.CallSite, IronPython.Runtime.CodeContext, System.Object, System.Object]]]:
        ...

    def MakeGenericMethod(self, types: System.Array[System.Type], ) -> IronPython.Runtime.Types.BuiltinFunction:
        ...

    def GetDescriptor(self, ) -> IronPython.Runtime.Types.PythonTypeSlot:
        ...

    def MakeBoundFunctionTest(self, functionTarget: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.Expression:
        ...

    def TryGetValue(self, context: IronPython.Runtime.CodeContext, instance: System.Object, owner: IronPython.Runtime.Types.PythonType, value: ref[System.Object], ) -> bool:
        ...

    def MakeGetExpression(self, binder: IronPython.Runtime.Binding.PythonBinder, codeContext: System.Linq.Expressions.Expression, instance: System.Dynamic.DynamicMetaObject, owner: System.Dynamic.DynamicMetaObject, builder: IronPython.Runtime.Binding.ConditionalBuilder, ) -> None:
        ...

    def __repr__(self, context: IronPython.Runtime.CodeContext, ) -> str:
        ...

    def GetMetaObject(self, parameter: System.Linq.Expressions.Expression, ) -> System.Dynamic.DynamicMetaObject:
        ...

    def MakeBuiltinFunctionCall(self, call: System.Dynamic.DynamicMetaObjectBinder, codeContext: System.Linq.Expressions.Expression, function: System.Dynamic.DynamicMetaObject, args: System.Array[System.Dynamic.DynamicMetaObject], hasSelf: bool, functionRestriction: System.Dynamic.BindingRestrictions, bind: System.Func[System.Array[System.Dynamic.DynamicMetaObject], IronPython.Runtime.Types.BuiltinFunction.BindingResult], ) -> System.Dynamic.DynamicMetaObject:
        ...

    @staticmethod
    def TranslateArguments(call: System.Dynamic.DynamicMetaObjectBinder, codeContext: System.Linq.Expressions.Expression, function: System.Dynamic.DynamicMetaObject, args: System.Array[System.Dynamic.DynamicMetaObject], hasSelf: bool, name: str, ) -> System.Dynamic.DynamicMetaObject:
        ...

    @staticmethod
    def IsThrowException(expr: System.Linq.Expressions.Expression, ) -> bool:
        ...

    def Equals(self, other: IronPython.Runtime.Types.BuiltinFunction, ) -> bool:
        ...

    def __eq__(self, other: IronPython.Runtime.Types.BuiltinFunction, ) -> bool:
        ...

    def __ne__(self, other: IronPython.Runtime.Types.BuiltinFunction, ) -> bool:
        ...

    def __gt__(self, context: IronPython.Runtime.CodeContext, other: System.Object, ) -> IronPython.Runtime.Types.NotImplementedType:
        ...

    def __lt__(self, context: IronPython.Runtime.CodeContext, other: System.Object, ) -> IronPython.Runtime.Types.NotImplementedType:
        ...

    def __ge__(self, context: IronPython.Runtime.CodeContext, other: System.Object, ) -> IronPython.Runtime.Types.NotImplementedType:
        ...

    def __le__(self, context: IronPython.Runtime.CodeContext, other: System.Object, ) -> IronPython.Runtime.Types.NotImplementedType:
        ...

    def __hash__(self, context: IronPython.Runtime.CodeContext, ) -> int:
        ...

    def __call__(self, context: IronPython.Runtime.CodeContext, storage: IronPython.Runtime.SiteLocalStorage[System.Runtime.CompilerServices.CallSite[System.Func[System.Runtime.CompilerServices.CallSite, IronPython.Runtime.CodeContext, System.Object, System.Array[System.Object], System.Collections.Generic.IDictionary[System.Object, System.Object], System.Object]]], dictArgs: System.Collections.Generic.IDictionary[System.Object, System.Object], args: System.Array[System.Object], ) -> System.Object:
        ...

    def EnsureBoundGenericDict(self, ) -> None:
        ...

    def ConvertToDelegate(self, type: System.Type, ) -> System.Delegate:
        ...

    def MakeInvokeBinding(self, site: System.Runtime.CompilerServices.CallSite[T], binder: IronPython.Runtime.Binding.PythonInvokeBinder, state: IronPython.Runtime.CodeContext, args: System.Array[System.Object], ) -> IronPython.Runtime.Binding.FastBindResult[T]:
        ...

    def __reduce__(self, ) -> str:
        ...

class IPythonObject(abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    @abc.abstractmethod
    def Dict(self) -> IronPython.Runtime.PythonDictionary:
        ...

    @property
    @abc.abstractmethod
    def PythonType(self) -> IronPython.Runtime.Types.PythonType:
        ...

    # methods
    @abc.abstractmethod
    def SetDict(self, dict: IronPython.Runtime.PythonDictionary, ) -> IronPython.Runtime.PythonDictionary:
        ...

    @abc.abstractmethod
    def ReplaceDict(self, dict: IronPython.Runtime.PythonDictionary, ) -> bool:
        ...

    @abc.abstractmethod
    def SetPythonType(self, newType: IronPython.Runtime.Types.PythonType, ) -> None:
        ...

    @abc.abstractmethod
    def GetSlots(self, ) -> System.Array[System.Object]:
        ...

    @abc.abstractmethod
    def GetSlotsCreate(self, ) -> System.Array[System.Object]:
        ...

class FunctionType(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    None_: int = ...
    Function: int = ...
    Method: int = ...
    FunctionMethodMask: int = ...
    AlwaysVisible: int = ...
    ReversedOperator: int = ...
    BinaryOperator: int = ...
    ModuleMethod: int = ...

class PythonTypeSlot(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def IsAlwaysVisible(self) -> bool:
        ...

    @property
    def CanOptimizeGets(self) -> bool:
        ...

    @property
    def GetAlwaysSucceeds(self) -> bool:
        ...

    # methods
    def __init__(self, ):
        ...

    def IsSetDescriptor(self, context: IronPython.Runtime.CodeContext, owner: IronPython.Runtime.Types.PythonType, ) -> bool:
        ...

    def TryGetValue(self, context: IronPython.Runtime.CodeContext, instance: System.Object, owner: IronPython.Runtime.Types.PythonType, value: ref[System.Object], ) -> bool:
        ...

    def MakeGetExpression(self, binder: IronPython.Runtime.Binding.PythonBinder, codeContext: System.Linq.Expressions.Expression, instance: System.Dynamic.DynamicMetaObject, owner: System.Dynamic.DynamicMetaObject, builder: IronPython.Runtime.Binding.ConditionalBuilder, ) -> None:
        ...

    def TrySetValue(self, context: IronPython.Runtime.CodeContext, instance: System.Object, owner: IronPython.Runtime.Types.PythonType, value: System.Object, ) -> bool:
        ...

    def TryDeleteValue(self, context: IronPython.Runtime.CodeContext, instance: System.Object, owner: IronPython.Runtime.Types.PythonType, ) -> bool:
        ...

    def __get__(self, context: IronPython.Runtime.CodeContext, instance: System.Object, typeContext: System.Object = ..., ) -> System.Object:
        ...

class PythonTypeWeakRefSlot(IronPython.Runtime.ICodeFormattable, IronPython.Runtime.Types.PythonTypeSlot):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def IsAlwaysVisible(self) -> bool:
        ...

    @property
    def CanOptimizeGets(self) -> bool:
        ...

    @property
    def GetAlwaysSucceeds(self) -> bool:
        ...

    # methods
    def __init__(self, parent: IronPython.Runtime.Types.PythonType, ):
        ...

    def TryGetValue(self, context: IronPython.Runtime.CodeContext, instance: System.Object, owner: IronPython.Runtime.Types.PythonType, value: ref[System.Object], ) -> bool:
        ...

    def TrySetValue(self, context: IronPython.Runtime.CodeContext, instance: System.Object, owner: IronPython.Runtime.Types.PythonType, value: System.Object, ) -> bool:
        ...

    def TryDeleteValue(self, context: IronPython.Runtime.CodeContext, instance: System.Object, owner: IronPython.Runtime.Types.PythonType, ) -> bool:
        ...

    def ToString(self, ) -> str:
        ...

    def __set__(self, context: IronPython.Runtime.CodeContext, instance: System.Object, value: System.Object, ) -> None:
        ...

    def __repr__(self, context: IronPython.Runtime.CodeContext, ) -> str:
        ...

class MappingProxy(System.Collections.Generic.IDictionary[System.Object, System.Object], System.Collections.Generic.ICollection[System.Collections.Generic.KeyValuePair[System.Object, System.Object]], System.Collections.Generic.IEnumerable[System.Collections.Generic.KeyValuePair[System.Object, System.Object]], System.Collections.IEnumerable, System.Collections.IDictionary, System.Collections.ICollection, System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields
    __hash__: System.Object = ...

    # properties
    @property
    def Item(self) -> System.Object:
        ...
    @Item.setter
    def Item(self, val: System.Object):
        ...

    @property
    def IsFixedSize(self) -> bool:
        ...

    @property
    def IsReadOnly(self) -> bool:
        ...

    @property
    def Keys(self) -> System.Collections.ICollection:
        ...

    @property
    def Values(self) -> System.Collections.ICollection:
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

    @property
    def Keys(self) -> System.Collections.Generic.ICollection[System.Object]:
        ...

    @property
    def Values(self) -> System.Collections.Generic.ICollection[System.Object]:
        ...

    @property
    def Count(self) -> int:
        ...

    @property
    def IsReadOnly(self) -> bool:
        ...

    # methods
    @typing.overload
    def __init__(self, context: IronPython.Runtime.CodeContext, dt: IronPython.Runtime.Types.PythonType, ):
        ...

    @typing.overload
    def __init__(self, dict: IronPython.Runtime.PythonDictionary, ):
        ...

    def GetDictionary(self, context: IronPython.Runtime.CodeContext, ) -> IronPython.Runtime.PythonDictionary:
        ...

    def __len__(self, context: IronPython.Runtime.CodeContext, ) -> int:
        ...

    def __contains__(self, context: IronPython.Runtime.CodeContext, value: System.Object, ) -> bool:
        ...

    def __str__(self, context: IronPython.Runtime.CodeContext, ) -> str:
        ...

    def __repr__(self, context: IronPython.Runtime.CodeContext, ) -> str:
        ...

    def get(self, context: IronPython.Runtime.CodeContext, k: System.Object, d: System.Object = ..., ) -> System.Object:
        ...

    def keys(self, context: IronPython.Runtime.CodeContext, ) -> System.Object:
        ...

    def values(self, context: IronPython.Runtime.CodeContext, ) -> System.Object:
        ...

    def items(self, context: IronPython.Runtime.CodeContext, ) -> System.Object:
        ...

    def copy(self, context: IronPython.Runtime.CodeContext, ) -> IronPython.Runtime.PythonDictionary:
        ...

    def __eq__(self, context: IronPython.Runtime.CodeContext, other: System.Object, ) -> System.Object:
        ...

    def Contains(self, key: System.Object, ) -> bool:
        ...

    def GetEnumerator(self, ) -> System.Collections.IEnumerator:
        ...

    def Add(self, key: System.Object, value: System.Object, ) -> None:
        ...

    def Clear(self, ) -> None:
        ...

    def GetEnumerator(self, ) -> System.Collections.IDictionaryEnumerator:
        ...

    def Remove(self, key: System.Object, ) -> None:
        ...

    def CopyTo(self, array: System.Array, index: int, ) -> None:
        ...

    def ContainsKey(self, key: System.Object, ) -> bool:
        ...

    def Remove(self, key: System.Object, ) -> bool:
        ...

    def TryGetValue(self, key: System.Object, value: ref[System.Object], ) -> bool:
        ...

    def Add(self, item: System.Collections.Generic.KeyValuePair[System.Object, System.Object], ) -> None:
        ...

    def Contains(self, item: System.Collections.Generic.KeyValuePair[System.Object, System.Object], ) -> bool:
        ...

    def CopyTo(self, array: System.Array[System.Collections.Generic.KeyValuePair[System.Object, System.Object]], arrayIndex: int, ) -> None:
        ...

    def Remove(self, item: System.Collections.Generic.KeyValuePair[System.Object, System.Object], ) -> bool:
        ...

    def GetEnumerator(self, ) -> System.Collections.Generic.IEnumerator[System.Collections.Generic.KeyValuePair[System.Object, System.Object]]:
        ...

class GenericBuiltinFunction(IronPython.Runtime.ICodeFormattable, System.Dynamic.IDynamicMetaObjectProvider, IronPython.Runtime.Operations.IDelegateConvertible, IronPython.Runtime.Binding.IFastInvokable, IronPython.Runtime.Types.BuiltinFunction):
    @typing.overload
    def __init__(self, **kwargs):
        self._data: IronPython.Runtime.Types.BuiltinFunction.BuiltinFunctionData
        self._instance: System.Object
        ...

    # static fields

    # properties
    @property
    def Item(self) -> IronPython.Runtime.Types.BuiltinFunction:
        ...

    @property
    def Item(self) -> IronPython.Runtime.Types.BuiltinFunction:
        ...

    @property
    def IsOnlyGeneric(self) -> bool:
        ...

    @property
    def IsUnbound(self) -> bool:
        ...

    @property
    def Name(self) -> str:
        ...
    @Name.setter
    def Name(self, val: str):
        ...

    @property
    def DeclaringType(self) -> System.Type:
        ...

    @property
    def Targets(self) -> System.Collections.Generic.IList[System.Reflection.MethodBase]:
        ...

    @property
    def IsAlwaysVisible(self) -> bool:
        ...

    @property
    def IsReversedOperator(self) -> bool:
        ...

    @property
    def IsBinaryOperator(self) -> bool:
        ...

    @property
    def FunctionType(self) -> int:
        ...
    @FunctionType.setter
    def FunctionType(self, val: int):
        ...

    @property
    def GetAlwaysSucceeds(self) -> bool:
        ...

    @property
    def Overloads(self) -> IronPython.Runtime.Types.BuiltinFunctionOverloadMapper:
        ...

    @property
    def OverloadDictionary(self) -> System.Collections.Generic.Dictionary[IronPython.Runtime.Types.BuiltinFunction.TypeList, IronPython.Runtime.Types.BuiltinFunction]:
        ...

    @property
    def __name__(self) -> str:
        ...

    @property
    def __doc__(self) -> str:
        ...

    @property
    def __self__(self) -> System.Object:
        ...

    @property
    def BindingSelf(self) -> System.Object:
        ...

    @property
    def CanOptimizeGets(self) -> bool:
        ...

    # methods
    @typing.overload
    def __init__(self, name: str, originalTargets: System.Array[System.Reflection.MethodBase], declaringType: System.Type, functionType: int, ):
        ...

    @typing.overload
    def __init__(self, instance: System.Object, data: IronPython.Runtime.Types.BuiltinFunction.BuiltinFunctionData, ):
        ...

    def BindToInstance(self, instance: System.Object, ) -> IronPython.Runtime.Types.BuiltinFunction:
        ...

class PythonCustomTracker(Microsoft.Scripting.Actions.CustomTracker, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def MemberType(self) -> int:
        ...

    @property
    @abc.abstractmethod
    def DeclaringType(self) -> System.Type:
        ...

    @property
    @abc.abstractmethod
    def Name(self) -> str:
        ...

    # methods
    def __init__(self, ):
        ...

    @abc.abstractmethod
    def GetSlot(self, ) -> IronPython.Runtime.Types.PythonTypeSlot:
        ...

    def GetValue(self, resolverFactory: Microsoft.Scripting.Actions.Calls.OverloadResolverFactory, binder: Microsoft.Scripting.Actions.ActionBinder, type: System.Type, ) -> System.Dynamic.DynamicMetaObject:
        ...

    def BindToInstance(self, instance: System.Dynamic.DynamicMetaObject, ) -> Microsoft.Scripting.Actions.MemberTracker:
        ...

    @typing.overload
    def SetValue(self, resolverFactory: Microsoft.Scripting.Actions.Calls.OverloadResolverFactory, binder: Microsoft.Scripting.Actions.ActionBinder, type: System.Type, value: System.Dynamic.DynamicMetaObject, ) -> System.Dynamic.DynamicMetaObject:
        ...

    @typing.overload
    def SetValue(self, resolverFactory: Microsoft.Scripting.Actions.Calls.OverloadResolverFactory, binder: Microsoft.Scripting.Actions.ActionBinder, type: System.Type, value: System.Dynamic.DynamicMetaObject, errorSuggestion: System.Dynamic.DynamicMetaObject, ) -> System.Dynamic.DynamicMetaObject:
        ...

    def GetBoundValue(self, factory: Microsoft.Scripting.Actions.Calls.OverloadResolverFactory, binder: Microsoft.Scripting.Actions.ActionBinder, instanceType: System.Type, instance: System.Dynamic.DynamicMetaObject, ) -> System.Dynamic.DynamicMetaObject:
        ...

    @typing.overload
    def SetBoundValue(self, resolverFactory: Microsoft.Scripting.Actions.Calls.OverloadResolverFactory, binder: Microsoft.Scripting.Actions.ActionBinder, type: System.Type, value: System.Dynamic.DynamicMetaObject, instance: System.Dynamic.DynamicMetaObject, ) -> System.Dynamic.DynamicMetaObject:
        ...

    @typing.overload
    def SetBoundValue(self, factory: Microsoft.Scripting.Actions.Calls.OverloadResolverFactory, binder: Microsoft.Scripting.Actions.ActionBinder, type: System.Type, value: System.Dynamic.DynamicMetaObject, instance: System.Dynamic.DynamicMetaObject, errorSuggestion: System.Dynamic.DynamicMetaObject, ) -> System.Dynamic.DynamicMetaObject:
        ...

class PythonTypeUserDescriptorSlot(IronPython.Runtime.Types.PythonTypeSlot):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def Value(self) -> System.Object:
        ...
    @Value.setter
    def Value(self, val: System.Object):
        ...

    @property
    def IsAlwaysVisible(self) -> bool:
        ...

    @property
    def CanOptimizeGets(self) -> bool:
        ...

    @property
    def GetAlwaysSucceeds(self) -> bool:
        ...

    # methods
    @typing.overload
    def __init__(self, value: System.Object, ):
        ...

    @typing.overload
    def __init__(self, value: System.Object, isntDescriptor: bool, ):
        ...

    def TryGetValue(self, context: IronPython.Runtime.CodeContext, instance: System.Object, owner: IronPython.Runtime.Types.PythonType, value: ref[System.Object], ) -> bool:
        ...

    def GetValue(self, context: IronPython.Runtime.CodeContext, instance: System.Object, owner: IronPython.Runtime.Types.PythonType, ) -> System.Object:
        ...

    def CalculateDescriptorInfo(self, ) -> None:
        ...

    def TryDeleteValue(self, context: IronPython.Runtime.CodeContext, instance: System.Object, owner: IronPython.Runtime.Types.PythonType, ) -> bool:
        ...

    def TrySetValue(self, context: IronPython.Runtime.CodeContext, instance: System.Object, owner: IronPython.Runtime.Types.PythonType, value: System.Object, ) -> bool:
        ...

    def IsSetDescriptor(self, context: IronPython.Runtime.CodeContext, owner: IronPython.Runtime.Types.PythonType, ) -> bool:
        ...

class PythonTypeDictSlot(IronPython.Runtime.ICodeFormattable, IronPython.Runtime.Types.PythonTypeSlot):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def IsAlwaysVisible(self) -> bool:
        ...

    @property
    def CanOptimizeGets(self) -> bool:
        ...

    @property
    def GetAlwaysSucceeds(self) -> bool:
        ...

    # methods
    def __init__(self, type: IronPython.Runtime.Types.PythonType, ):
        ...

    def TryGetValue(self, context: IronPython.Runtime.CodeContext, instance: System.Object, owner: IronPython.Runtime.Types.PythonType, value: ref[System.Object], ) -> bool:
        ...

    def TrySetValue(self, context: IronPython.Runtime.CodeContext, instance: System.Object, owner: IronPython.Runtime.Types.PythonType, value: System.Object, ) -> bool:
        ...

    def IsSetDescriptor(self, context: IronPython.Runtime.CodeContext, owner: IronPython.Runtime.Types.PythonType, ) -> bool:
        ...

    def TryDeleteValue(self, context: IronPython.Runtime.CodeContext, instance: System.Object, owner: IronPython.Runtime.Types.PythonType, ) -> bool:
        ...

    def __set__(self, context: IronPython.Runtime.CodeContext, instance: System.Object, value: System.Object, ) -> None:
        ...

    def __repr__(self, context: IronPython.Runtime.CodeContext, ) -> str:
        ...

class PythonTypeDataSlot(IronPython.Runtime.Types.PythonTypeSlot):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def IsAlwaysVisible(self) -> bool:
        ...

    @property
    def CanOptimizeGets(self) -> bool:
        ...

    @property
    def GetAlwaysSucceeds(self) -> bool:
        ...

    # methods
    def __init__(self, ):
        ...

    def __set__(self, context: IronPython.Runtime.CodeContext, instance: System.Object, value: System.Object, ) -> None:
        ...

    def __delete__(self, context: IronPython.Runtime.CodeContext, instance: System.Object, ) -> None:
        ...

    def IsSetDescriptor(self, context: IronPython.Runtime.CodeContext, owner: IronPython.Runtime.Types.PythonType, ) -> bool:
        ...

class ConstructorOverloadMapper(IronPython.Runtime.ICodeFormattable, IronPython.Runtime.Types.BuiltinFunctionOverloadMapper):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def Targets(self) -> System.Collections.Generic.IList[System.Reflection.MethodBase]:
        ...

    @property
    def Item(self) -> System.Object:
        ...

    @property
    def Function(self) -> IronPython.Runtime.Types.BuiltinFunction:
        ...

    @property
    def Functions(self) -> IronPython.Runtime.PythonTuple:
        ...

    # methods
    def __init__(self, builtinFunction: IronPython.Runtime.Types.ConstructorFunction, instance: System.Object, ):
        ...

    def GetTargetFunction(self, bf: IronPython.Runtime.Types.BuiltinFunction, ) -> System.Object:
        ...

class ReflectedGetterSetter(IronPython.Runtime.Types.PythonTypeSlot, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    @abc.abstractmethod
    def DeclaringType(self) -> System.Type:
        ...

    @property
    @abc.abstractmethod
    def __name__(self) -> str:
        ...

    @property
    def __objclass__(self) -> IronPython.Runtime.Types.PythonType:
        ...

    @property
    def Getter(self) -> System.Array[System.Reflection.MethodInfo]:
        ...

    @property
    def Setter(self) -> System.Array[System.Reflection.MethodInfo]:
        ...

    @property
    def PropertyType(self) -> IronPython.Runtime.Types.PythonType:
        ...

    @property
    def NameType(self) -> int:
        ...

    @property
    def IsAlwaysVisible(self) -> bool:
        ...

    @property
    def CanOptimizeGets(self) -> bool:
        ...

    @property
    def GetAlwaysSucceeds(self) -> bool:
        ...

    # methods
    @typing.overload
    def __init__(self, getter: System.Array[System.Reflection.MethodInfo], setter: System.Array[System.Reflection.MethodInfo], nt: int, ):
        ...

    @typing.overload
    def __init__(self, from_: IronPython.Runtime.Types.ReflectedGetterSetter, ):
        ...

    def AddGetter(self, mi: System.Reflection.MethodInfo, ) -> None:
        ...

    def MakeGetFunc(self, ) -> None:
        ...

    def AddSetter(self, mi: System.Reflection.MethodInfo, ) -> None:
        ...

    def MakeSetFunc(self, ) -> None:
        ...

    def CallGetter(self, context: IronPython.Runtime.CodeContext, storage: IronPython.Runtime.SiteLocalStorage[System.Runtime.CompilerServices.CallSite[System.Func[System.Runtime.CompilerServices.CallSite, IronPython.Runtime.CodeContext, System.Object, System.Array[System.Object], System.Object]]], instance: System.Object, args: System.Array[System.Object], ) -> System.Object:
        ...

    def CallTarget(self, context: IronPython.Runtime.CodeContext, storage: IronPython.Runtime.SiteLocalStorage[System.Runtime.CompilerServices.CallSite[System.Func[System.Runtime.CompilerServices.CallSite, IronPython.Runtime.CodeContext, System.Object, System.Array[System.Object], System.Object]]], targets: System.Array[System.Reflection.MethodInfo], instance: System.Object, args: System.Array[System.Object], ) -> System.Object:
        ...

    @staticmethod
    def NeedToReturnProperty(instance: System.Object, mis: System.Array[System.Reflection.MethodInfo], ) -> bool:
        ...

    def CallSetter(self, context: IronPython.Runtime.CodeContext, storage: IronPython.Runtime.SiteLocalStorage[System.Runtime.CompilerServices.CallSite[System.Func[System.Runtime.CompilerServices.CallSite, IronPython.Runtime.CodeContext, System.Object, System.Array[System.Object], System.Object]]], instance: System.Object, args: System.Array[System.Object], value: System.Object, ) -> bool:
        ...

    @staticmethod
    def RemoveNullEntries(mis: System.Array[System.Reflection.MethodInfo], ) -> System.Array[System.Reflection.MethodInfo]:
        ...

class BuiltinMethodDescriptor(System.Dynamic.IDynamicMetaObjectProvider, IronPython.Runtime.ICodeFormattable, IronPython.Runtime.Types.PythonTypeSlot):
    @typing.overload
    def __init__(self, **kwargs):
        self._template: IronPython.Runtime.Types.BuiltinFunction
        ...

    # static fields

    # properties
    @property
    def GetAlwaysSucceeds(self) -> bool:
        ...

    @property
    def Template(self) -> IronPython.Runtime.Types.BuiltinFunction:
        ...

    @property
    def DeclaringType(self) -> System.Type:
        ...

    @property
    def IsAlwaysVisible(self) -> bool:
        ...

    @property
    def __name__(self) -> str:
        ...

    @property
    def __doc__(self) -> str:
        ...

    @property
    def __objclass__(self) -> IronPython.Runtime.Types.PythonType:
        ...

    @property
    def CanOptimizeGets(self) -> bool:
        ...

    # methods
    def __init__(self, function: IronPython.Runtime.Types.BuiltinFunction, ):
        ...

    def UncheckedGetAttribute(self, instance: System.Object, ) -> System.Object:
        ...

    def TryGetValue(self, context: IronPython.Runtime.CodeContext, instance: System.Object, owner: IronPython.Runtime.Types.PythonType, value: ref[System.Object], ) -> bool:
        ...

    def MakeGetExpression(self, binder: IronPython.Runtime.Binding.PythonBinder, codeContext: System.Linq.Expressions.Expression, instance: System.Dynamic.DynamicMetaObject, owner: System.Dynamic.DynamicMetaObject, builder: IronPython.Runtime.Binding.ConditionalBuilder, ) -> None:
        ...

    @staticmethod
    def CheckSelfWorker(context: IronPython.Runtime.CodeContext, self: System.Object, template: IronPython.Runtime.Types.BuiltinFunction, ) -> None:
        ...

    def CheckSelf(self, context: IronPython.Runtime.CodeContext, self: System.Object, ) -> None:
        ...

    def __call__(self, context: IronPython.Runtime.CodeContext, storage: IronPython.Runtime.SiteLocalStorage[System.Runtime.CompilerServices.CallSite[System.Func[System.Runtime.CompilerServices.CallSite, IronPython.Runtime.CodeContext, System.Object, System.Array[System.Object], System.Collections.Generic.IDictionary[System.Object, System.Object], System.Object]]], dictArgs: System.Collections.Generic.IDictionary[System.Object, System.Object], args: System.Array[System.Object], ) -> System.Object:
        ...

    def __repr__(self, context: IronPython.Runtime.CodeContext, ) -> str:
        ...

    def GetMetaObject(self, parameter: System.Linq.Expressions.Expression, ) -> System.Dynamic.DynamicMetaObject:
        ...

class BuiltinFunctionOverloadMapper(IronPython.Runtime.ICodeFormattable, System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def Item(self) -> System.Object:
        ...

    @property
    def Function(self) -> IronPython.Runtime.Types.BuiltinFunction:
        ...

    @property
    def Targets(self) -> System.Collections.Generic.IList[System.Reflection.MethodBase]:
        ...

    @property
    def Functions(self) -> IronPython.Runtime.PythonTuple:
        ...

    # methods
    def __init__(self, builtinFunction: IronPython.Runtime.Types.BuiltinFunction, instance: System.Object, ):
        ...

    def GetTargetFunction(self, bf: IronPython.Runtime.Types.BuiltinFunction, ) -> System.Object:
        ...

    @typing.overload
    def GetOverload(self, sig: System.Array[System.Type], targets: System.Collections.Generic.IList[System.Reflection.MethodBase], ) -> System.Object:
        ...

    @typing.overload
    def GetOverload(self, sig: System.Array[System.Type], targets: System.Collections.Generic.IList[System.Reflection.MethodBase], wrapCtors: bool, ) -> System.Object:
        ...

    @staticmethod
    def FindMatchingTargets(sig: System.Array[System.Type], targets: System.Collections.Generic.IList[System.Reflection.MethodBase], removeCodeContext: bool, ) -> System.Array[System.Reflection.MethodBase]:
        ...

    def ThrowOverloadException(self, sig: System.Array[System.Type], targets: System.Collections.Generic.IList[System.Reflection.MethodBase], ) -> None:
        ...

    def __repr__(self, context: IronPython.Runtime.CodeContext, ) -> str:
        ...

class NoneTypeOps(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields
    __doc__: str = ...
    NoneHashCode: int = ...

    # properties
    # methods
    def __init__(self, ):
        ...

    @staticmethod
    def __new__(context: IronPython.Runtime.CodeContext, cls: IronPython.Runtime.Types.PythonType, ) -> System.Object:
        ...

    @staticmethod
    def __hash__(self: Microsoft.Scripting.Runtime.DynamicNull, ) -> int:
        ...

    @staticmethod
    def __repr__(self: Microsoft.Scripting.Runtime.DynamicNull, ) -> str:
        ...

