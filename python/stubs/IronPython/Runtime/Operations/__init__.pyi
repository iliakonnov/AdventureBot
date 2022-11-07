from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import System
import IronPython.Runtime.Types
import IronPython.Runtime
import System.Collections.Generic
import System.Collections
import System.Runtime.CompilerServices
import System.Dynamic
import Microsoft.Scripting.Actions
import System.Linq.Expressions
import IronPython.Runtime.Binding
import IronPython.Runtime.Exceptions
import Microsoft.Scripting.Runtime
import System.Numerics
import IronPython.Runtime.Operations
import Microsoft.Scripting.Ast
import Microsoft.Scripting
import IronPython.Compiler
import System.Reflection
import System.Reflection.Emit
import IronPython.Runtime.Exceptions.PythonExceptions
import IronPython.Runtime.Types.ReflectedEvent
import IronPython.Runtime.Operations.PythonOps
import System.Text
import IronPython.Runtime.Operations.StringOps
import System.ComponentModel

T = typing.TypeVar('T')
K = typing.TypeVar('K')
V = typing.TypeVar('V')

class InstanceOps(System.Object, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields
    NewCls: IronPython.Runtime.Types.BuiltinFunction = ...
    OverloadedNew: IronPython.Runtime.Types.BuiltinFunction = ...
    NonDefaultNewInst: IronPython.Runtime.Types.BuiltinFunction = ...
    _Init: IronPython.Runtime.Types.BuiltinMethodDescriptor = ...
    ObjectNewNoParameters: str = ...

    # properties
    @property
    def Init(self) -> IronPython.Runtime.Types.BuiltinMethodDescriptor:
        ...

    @property
    def New(self) -> IronPython.Runtime.Types.BuiltinFunction:
        ...

    # methods
    @staticmethod
    @typing.overload
    def ComparableLessThan(x: T, y: System.Object, ) -> System.Object:
        ...

    @staticmethod
    @typing.overload
    def ComparableLessThan(y: System.Object, x: T, ) -> System.Object:
        ...

    @staticmethod
    @typing.overload
    def ComparableLessThan(x: T, y: T, ) -> bool:
        ...

    @staticmethod
    @typing.overload
    def ComparableGreaterEqual(x: T, y: System.Object, ) -> System.Object:
        ...

    @staticmethod
    @typing.overload
    def ComparableGreaterEqual(y: System.Object, x: T, ) -> System.Object:
        ...

    @staticmethod
    @typing.overload
    def ComparableGreaterEqual(x: T, y: T, ) -> bool:
        ...

    @staticmethod
    @typing.overload
    def ComparableLessEqual(x: T, y: System.Object, ) -> System.Object:
        ...

    @staticmethod
    @typing.overload
    def ComparableLessEqual(y: System.Object, x: T, ) -> System.Object:
        ...

    @staticmethod
    @typing.overload
    def ComparableLessEqual(x: T, y: T, ) -> bool:
        ...

    @staticmethod
    @typing.overload
    def ComparableEquality(y: System.Object, x: T, ) -> System.Object:
        ...

    @staticmethod
    @typing.overload
    def ComparableEquality(x: T, y: T, ) -> bool:
        ...

    @staticmethod
    @typing.overload
    def ComparableEquality(x: T, y: System.Object, ) -> System.Object:
        ...

    @staticmethod
    @typing.overload
    def ComparableInequality(y: System.Object, x: T, ) -> System.Object:
        ...

    @staticmethod
    @typing.overload
    def ComparableInequality(x: T, y: T, ) -> bool:
        ...

    @staticmethod
    @typing.overload
    def ComparableInequality(x: T, y: System.Object, ) -> System.Object:
        ...

    @staticmethod
    @typing.overload
    def ComparableGreaterThan(y: System.Object, x: T, ) -> System.Object:
        ...

    @staticmethod
    @typing.overload
    def ComparableGreaterThan(x: T, y: T, ) -> bool:
        ...

    @staticmethod
    @typing.overload
    def ComparableGreaterThan(x: T, y: System.Object, ) -> System.Object:
        ...

    @staticmethod
    def EnterMethod(self: System.IDisposable, ) -> System.Object:
        ...

    @staticmethod
    def ExitMethod(self: System.IDisposable, exc_type: System.Object, exc_value: System.Object, exc_back: System.Object, ) -> None:
        ...

    @staticmethod
    def Get__all__(context: IronPython.Runtime.CodeContext, ) -> IronPython.Runtime.PythonList:
        ...

    @staticmethod
    def IsStaticTypeMemberInAll(context: IronPython.Runtime.CodeContext, pt: IronPython.Runtime.Types.PythonType, name: str, res: ref[System.Object], ) -> bool:
        ...

    @staticmethod
    def ContainsGenericMethod(context: IronPython.Runtime.CodeContext, enumerable: System.Collections.Generic.IEnumerable[T], value: T, ) -> bool:
        ...

    @staticmethod
    def ContainsMethod(context: IronPython.Runtime.CodeContext, enumerable: System.Collections.IEnumerable, value: System.Object, ) -> bool:
        ...

    @staticmethod
    def ContainsGenericMethodIEnumerator(context: IronPython.Runtime.CodeContext, enumerator: System.Collections.Generic.IEnumerator[T], value: T, ) -> bool:
        ...

    @staticmethod
    def ContainsMethodIEnumerator(context: IronPython.Runtime.CodeContext, enumerator: System.Collections.IEnumerator, value: System.Object, ) -> bool:
        ...

    @staticmethod
    def SerializeReduce(context: IronPython.Runtime.CodeContext, self: System.Object, protocol: int, ) -> IronPython.Runtime.PythonTuple:
        ...

    @staticmethod
    def CheckNewArgs(context: IronPython.Runtime.CodeContext, dict: System.Collections.Generic.IDictionary[System.Object, System.Object], args: System.Array[System.Object], pt: IronPython.Runtime.Types.PythonType, ) -> None:
        ...

    @staticmethod
    def CheckInitArgs(context: IronPython.Runtime.CodeContext, dict: System.Collections.Generic.IDictionary[System.Object, System.Object], args: System.Array[System.Object], self: System.Object, ) -> None:
        ...

    @staticmethod
    def GetInitMethod() -> IronPython.Runtime.Types.BuiltinMethodDescriptor:
        ...

    @staticmethod
    def CreateFunction(name: str, methodNames: System.Array[str], ) -> IronPython.Runtime.Types.BuiltinFunction:
        ...

    @staticmethod
    def GetKeywordArgs(dict: System.Collections.Generic.IDictionary[System.Object, System.Object], args: System.Array[System.Object], finalArgs: ref[System.Array[System.Object]], names: ref[System.Array[str]], ) -> None:
        ...

    @staticmethod
    def CreateNonDefaultNew() -> IronPython.Runtime.Types.BuiltinFunction:
        ...

    @staticmethod
    def DefaultNew(context: IronPython.Runtime.CodeContext, typeø: IronPython.Runtime.Types.PythonType, argsø: System.Array[System.Object], ) -> System.Object:
        ...

    @staticmethod
    def DefaultNewClsKW(context: IronPython.Runtime.CodeContext, typeø: IronPython.Runtime.Types.PythonType, kwargsø: System.Collections.Generic.IDictionary[System.Object, System.Object], argsø: System.Array[System.Object], ) -> System.Object:
        ...

    @staticmethod
    def OverloadedNewBasic(context: IronPython.Runtime.CodeContext, storage: IronPython.Runtime.SiteLocalStorage[System.Runtime.CompilerServices.CallSite[System.Func[System.Runtime.CompilerServices.CallSite, IronPython.Runtime.CodeContext, System.Object, System.Array[System.Object], System.Object]]], overloadsø: IronPython.Runtime.Types.BuiltinFunction, typeø: IronPython.Runtime.Types.PythonType, argsø: System.Array[System.Object], ) -> System.Object:
        ...

    @staticmethod
    def OverloadedNewKW(context: IronPython.Runtime.CodeContext, overloadsø: IronPython.Runtime.Types.BuiltinFunction, typeø: IronPython.Runtime.Types.PythonType, kwargsø: System.Collections.Generic.IDictionary[System.Object, System.Object], ) -> System.Object:
        ...

    @staticmethod
    def OverloadedNewClsKW(context: IronPython.Runtime.CodeContext, overloadsø: IronPython.Runtime.Types.BuiltinFunction, typeø: IronPython.Runtime.Types.PythonType, kwargsø: System.Collections.Generic.IDictionary[System.Object, System.Object], argsø: System.Array[System.Object], ) -> System.Object:
        ...

    @staticmethod
    def DefaultInit(context: IronPython.Runtime.CodeContext, self: System.Object, argsø: System.Array[System.Object], ) -> None:
        ...

    @staticmethod
    def DefaultInitKW(context: IronPython.Runtime.CodeContext, self: System.Object, kwargsø: System.Collections.Generic.IDictionary[System.Object, System.Object], argsø: System.Array[System.Object], ) -> None:
        ...

    @staticmethod
    def NonDefaultNew(context: IronPython.Runtime.CodeContext, typeø: IronPython.Runtime.Types.PythonType, argsø: System.Array[System.Object], ) -> System.Object:
        ...

    @staticmethod
    def NonDefaultNewKW(context: IronPython.Runtime.CodeContext, typeø: IronPython.Runtime.Types.PythonType, kwargsø: System.Collections.Generic.IDictionary[System.Object, System.Object], argsø: System.Array[System.Object], ) -> System.Object:
        ...

    @staticmethod
    def NonDefaultNewKWNoParams(context: IronPython.Runtime.CodeContext, typeø: IronPython.Runtime.Types.PythonType, kwargsø: System.Collections.Generic.IDictionary[System.Object, System.Object], ) -> System.Object:
        ...

    @staticmethod
    def IterMethodForEnumerator(self: System.Collections.IEnumerator, ) -> System.Object:
        ...

    @staticmethod
    def IterMethodForEnumerable(self: System.Collections.IEnumerable, ) -> System.Object:
        ...

    @staticmethod
    def IterMethodForGenericEnumerator(self: System.Collections.Generic.IEnumerator[T], ) -> System.Object:
        ...

    @staticmethod
    def IterMethodForGenericEnumerable(self: System.Collections.Generic.IEnumerable[T], ) -> System.Object:
        ...

    @staticmethod
    def NextMethod(self: System.Object, ) -> System.Object:
        ...

    @staticmethod
    def DynamicDir(context: IronPython.Runtime.CodeContext, self: System.Dynamic.IDynamicMetaObjectProvider, ) -> IronPython.Runtime.PythonList:
        ...

    @staticmethod
    def LengthMethod(self: System.Collections.ICollection, ) -> int:
        ...

    @staticmethod
    def GenericLengthMethod(self: System.Collections.Generic.ICollection[T], ) -> int:
        ...

    @staticmethod
    def SimpleRepr(self: System.Object, ) -> str:
        ...

    @staticmethod
    def FancyRepr(self: System.Object, ) -> str:
        ...

    @staticmethod
    def ReprHelper(context: IronPython.Runtime.CodeContext, self: System.Object, ) -> System.Object:
        ...

    @staticmethod
    def ToStringMethod(self: System.Object, ) -> str:
        ...

    @staticmethod
    def Format(formattable: System.IFormattable, format: str, ) -> str:
        ...

    @staticmethod
    def StructuralHashMethod(context: IronPython.Runtime.CodeContext, x: System.Collections.IStructuralEquatable, ) -> int:
        ...

    @staticmethod
    @typing.overload
    def StructuralEqualityMethod(context: IronPython.Runtime.CodeContext, x: T, y: T, ) -> bool:
        ...

    @staticmethod
    @typing.overload
    def StructuralEqualityMethod(context: IronPython.Runtime.CodeContext, x: T, y: System.Object, ) -> System.Object:
        ...

    @staticmethod
    @typing.overload
    def StructuralEqualityMethod(context: IronPython.Runtime.CodeContext, y: System.Object, x: T, ) -> System.Object:
        ...

    @staticmethod
    @typing.overload
    def StructuralInequalityMethod(context: IronPython.Runtime.CodeContext, x: T, y: T, ) -> bool:
        ...

    @staticmethod
    @typing.overload
    def StructuralInequalityMethod(context: IronPython.Runtime.CodeContext, x: T, y: System.Object, ) -> System.Object:
        ...

    @staticmethod
    @typing.overload
    def StructuralInequalityMethod(context: IronPython.Runtime.CodeContext, y: System.Object, x: T, ) -> System.Object:
        ...

    @staticmethod
    def StructuralCompare(context: IronPython.Runtime.CodeContext, x: System.Collections.IStructuralComparable, y: System.Object, ) -> int:
        ...

    @staticmethod
    @typing.overload
    def StructuralComparableEquality(context: IronPython.Runtime.CodeContext, x: T, y: T, ) -> bool:
        ...

    @staticmethod
    @typing.overload
    def StructuralComparableEquality(context: IronPython.Runtime.CodeContext, x: T, y: System.Object, ) -> System.Object:
        ...

    @staticmethod
    @typing.overload
    def StructuralComparableEquality(context: IronPython.Runtime.CodeContext, y: System.Object, x: T, ) -> System.Object:
        ...

    @staticmethod
    @typing.overload
    def StructuralComparableInequality(context: IronPython.Runtime.CodeContext, x: T, y: T, ) -> bool:
        ...

    @staticmethod
    @typing.overload
    def StructuralComparableInequality(context: IronPython.Runtime.CodeContext, x: T, y: System.Object, ) -> System.Object:
        ...

    @staticmethod
    @typing.overload
    def StructuralComparableInequality(context: IronPython.Runtime.CodeContext, y: System.Object, x: T, ) -> System.Object:
        ...

    @staticmethod
    @typing.overload
    def StructuralComparableGreaterThan(context: IronPython.Runtime.CodeContext, x: T, y: T, ) -> bool:
        ...

    @staticmethod
    @typing.overload
    def StructuralComparableGreaterThan(context: IronPython.Runtime.CodeContext, x: T, y: System.Object, ) -> System.Object:
        ...

    @staticmethod
    @typing.overload
    def StructuralComparableGreaterThan(context: IronPython.Runtime.CodeContext, y: System.Object, x: T, ) -> System.Object:
        ...

    @staticmethod
    @typing.overload
    def StructuralComparableLessThan(context: IronPython.Runtime.CodeContext, x: T, y: T, ) -> bool:
        ...

    @staticmethod
    @typing.overload
    def StructuralComparableLessThan(context: IronPython.Runtime.CodeContext, x: T, y: System.Object, ) -> System.Object:
        ...

    @staticmethod
    @typing.overload
    def StructuralComparableLessThan(context: IronPython.Runtime.CodeContext, y: System.Object, x: T, ) -> System.Object:
        ...

    @staticmethod
    @typing.overload
    def StructuralComparableGreaterEqual(context: IronPython.Runtime.CodeContext, x: T, y: T, ) -> bool:
        ...

    @staticmethod
    @typing.overload
    def StructuralComparableGreaterEqual(context: IronPython.Runtime.CodeContext, x: T, y: System.Object, ) -> System.Object:
        ...

    @staticmethod
    @typing.overload
    def StructuralComparableGreaterEqual(context: IronPython.Runtime.CodeContext, y: System.Object, x: T, ) -> System.Object:
        ...

    @staticmethod
    @typing.overload
    def StructuralComparableLessEqual(context: IronPython.Runtime.CodeContext, x: T, y: T, ) -> bool:
        ...

    @staticmethod
    @typing.overload
    def StructuralComparableLessEqual(context: IronPython.Runtime.CodeContext, x: T, y: System.Object, ) -> System.Object:
        ...

    @staticmethod
    @typing.overload
    def StructuralComparableLessEqual(context: IronPython.Runtime.CodeContext, y: System.Object, x: T, ) -> System.Object:
        ...

class NamespaceTrackerOps(System.Object, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    @staticmethod
    def __repr__(self: Microsoft.Scripting.Actions.NamespaceTracker, ) -> str:
        ...

    @staticmethod
    def __str__(self: Microsoft.Scripting.Actions.NamespaceTracker, ) -> str:
        ...

    @staticmethod
    def Get__name__(name: str, ) -> str:
        ...

class UserTypeOps(System.Object, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    @staticmethod
    def ToStringReturnHelper(o: System.Object, ) -> str:
        ...

    @staticmethod
    def SetDictHelper(dict: ref[IronPython.Runtime.PythonDictionary], value: IronPython.Runtime.PythonDictionary, ) -> IronPython.Runtime.PythonDictionary:
        ...

    @staticmethod
    def GetPropertyHelper(prop: System.Object, instance: System.Object, name: str, ) -> System.Object:
        ...

    @staticmethod
    def SetPropertyHelper(prop: System.Object, instance: System.Object, newValue: System.Object, name: str, ) -> None:
        ...

    @staticmethod
    def SetWeakRefHelper(obj: IronPython.Runtime.Types.IPythonObject, value: IronPython.Runtime.WeakRefTracker, ) -> bool:
        ...

    @staticmethod
    def GetWeakRefHelper(obj: IronPython.Runtime.Types.IPythonObject, ) -> IronPython.Runtime.WeakRefTracker:
        ...

    @staticmethod
    def SetFinalizerHelper(obj: IronPython.Runtime.Types.IPythonObject, value: IronPython.Runtime.WeakRefTracker, ) -> None:
        ...

    @staticmethod
    def GetSlotsCreate(obj: IronPython.Runtime.Types.IPythonObject, slots: ref[System.Array[System.Object]], ) -> System.Array[System.Object]:
        ...

    @staticmethod
    def AddRemoveEventHelper(method: System.Object, instance: IronPython.Runtime.Types.IPythonObject, eventValue: System.Object, name: str, ) -> None:
        ...

    @staticmethod
    def GetMetaObjectHelper(self: IronPython.Runtime.Types.IPythonObject, parameter: System.Linq.Expressions.Expression, baseMetaObject: System.Dynamic.DynamicMetaObject, ) -> System.Dynamic.DynamicMetaObject:
        ...

    @staticmethod
    def TryGetDictionaryValue(dict: IronPython.Runtime.PythonDictionary, name: str, keyVersion: int, keyIndex: int, res: ref[System.Object], ) -> bool:
        ...

    @staticmethod
    def SetDictionaryValue(self: IronPython.Runtime.Types.IPythonObject, name: str, value: System.Object, ) -> System.Object:
        ...

    @staticmethod
    def SetDictionaryValueOptimized(ipo: IronPython.Runtime.Types.IPythonObject, name: str, value: System.Object, keysVersion: int, index: int, ) -> System.Object:
        ...

    @staticmethod
    def FastSetDictionaryValue(dict: ref[IronPython.Runtime.PythonDictionary], name: str, value: System.Object, ) -> System.Object:
        ...

    @staticmethod
    def FastSetDictionaryValueOptimized(type: IronPython.Runtime.Types.PythonType, dict: ref[IronPython.Runtime.PythonDictionary], name: str, value: System.Object, keysVersion: int, index: int, ) -> System.Object:
        ...

    @staticmethod
    def RemoveDictionaryValue(self: IronPython.Runtime.Types.IPythonObject, name: str, ) -> System.Object:
        ...

    @staticmethod
    def GetDictionary(self: IronPython.Runtime.Types.IPythonObject, ) -> IronPython.Runtime.PythonDictionary:
        ...

    @staticmethod
    def ToStringHelper(o: IronPython.Runtime.Types.IPythonObject, ) -> str:
        ...

    @staticmethod
    def TryGetNonInheritedMethodHelper(dt: IronPython.Runtime.Types.PythonType, instance: System.Object, name: str, callTarget: ref[System.Object], ) -> bool:
        ...

    @staticmethod
    def LookupValue(dt: IronPython.Runtime.Types.PythonType, instance: System.Object, name: str, value: ref[System.Object], ) -> bool:
        ...

    @staticmethod
    def TryGetNonInheritedValueHelper(instance: IronPython.Runtime.Types.IPythonObject, name: str, callTarget: ref[System.Object], ) -> bool:
        ...

    @staticmethod
    def GetAttribute(context: IronPython.Runtime.CodeContext, self: System.Object, name: str, getAttributeSlot: IronPython.Runtime.Types.PythonTypeSlot, getAttrSlot: IronPython.Runtime.Types.PythonTypeSlot, callSite: IronPython.Runtime.SiteLocalStorage[System.Runtime.CompilerServices.CallSite[System.Func[System.Runtime.CompilerServices.CallSite, IronPython.Runtime.CodeContext, System.Object, str, System.Object]]], ) -> System.Object:
        ...

    @staticmethod
    def GetAttributeNoThrow(context: IronPython.Runtime.CodeContext, self: System.Object, name: str, getAttributeSlot: IronPython.Runtime.Types.PythonTypeSlot, getAttrSlot: IronPython.Runtime.Types.PythonTypeSlot, callSite: IronPython.Runtime.SiteLocalStorage[System.Runtime.CompilerServices.CallSite[System.Func[System.Runtime.CompilerServices.CallSite, IronPython.Runtime.CodeContext, System.Object, str, System.Object]]], ) -> System.Object:
        ...

    @staticmethod
    def MakeGetAttrSite(context: IronPython.Runtime.CodeContext, ) -> System.Runtime.CompilerServices.CallSite[System.Func[System.Runtime.CompilerServices.CallSite, IronPython.Runtime.CodeContext, System.Object, str, System.Object]]:
        ...

    @staticmethod
    def MakeGetBinding(codeContext: IronPython.Runtime.CodeContext, site: System.Runtime.CompilerServices.CallSite[T], self: IronPython.Runtime.Types.IPythonObject, getBinder: IronPython.Runtime.Binding.PythonGetMemberBinder, ) -> IronPython.Runtime.Binding.FastBindResult[T]:
        ...

    @staticmethod
    def MakeSetBinding(codeContext: IronPython.Runtime.CodeContext, site: System.Runtime.CompilerServices.CallSite[T], self: IronPython.Runtime.Types.IPythonObject, value: System.Object, setBinder: IronPython.Runtime.Binding.PythonSetMemberBinder, ) -> IronPython.Runtime.Binding.FastBindResult[T]:
        ...

class FunctionStack(System.ValueType):
    @typing.overload
    def __init__(self, **kwargs):
        self.Context: IronPython.Runtime.CodeContext
        self.Code: IronPython.Runtime.FunctionCode
        self.Frame: IronPython.Runtime.Exceptions.TraceBackFrame
        ...

    # static fields

    # properties
    # methods
    @typing.overload
    def __init__(self, context: IronPython.Runtime.CodeContext, code: IronPython.Runtime.FunctionCode, ):
        ...

    @typing.overload
    def __init__(self, context: IronPython.Runtime.CodeContext, code: IronPython.Runtime.FunctionCode, frame: IronPython.Runtime.Exceptions.TraceBackFrame, ):
        ...

    @typing.overload
    def __init__(self, frame: IronPython.Runtime.Exceptions.TraceBackFrame, ):
        ...

class ObjectOps(System.Object, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields
    __class__: IronPython.Runtime.Types.PythonTypeSlot = ...

    # properties
    @property
    def NativelyPickleableTypes(self) -> System.Collections.Generic.HashSet[IronPython.Runtime.Types.PythonType]:
        ...

    # methods
    @staticmethod
    def __delattr__(context: IronPython.Runtime.CodeContext, self: System.Object, name: str, ) -> None:
        ...

    @staticmethod
    def __hash__(self: System.Object, ) -> int:
        ...

    @staticmethod
    def __getattribute__(context: IronPython.Runtime.CodeContext, self: System.Object, name: str, ) -> System.Object:
        ...

    @staticmethod
    @typing.overload
    def __init__(context: IronPython.Runtime.CodeContext, self: System.Object, ) -> None:
        ...

    @staticmethod
    @typing.overload
    def __init__(context: IronPython.Runtime.CodeContext, self: System.Object, argsø: System.Array[System.Object], ) -> None:
        ...

    @staticmethod
    @typing.overload
    def __init__(context: IronPython.Runtime.CodeContext, self: System.Object, kwargs: System.Collections.Generic.IDictionary[System.Object, System.Object], argsø: System.Array[System.Object], ) -> None:
        ...

    @staticmethod
    @typing.overload
    def __new__(context: IronPython.Runtime.CodeContext, cls: IronPython.Runtime.Types.PythonType, ) -> System.Object:
        ...

    @staticmethod
    @typing.overload
    def __new__(context: IronPython.Runtime.CodeContext, cls: IronPython.Runtime.Types.PythonType, argsø: System.Array[System.Object], ) -> System.Object:
        ...

    @staticmethod
    @typing.overload
    def __new__(context: IronPython.Runtime.CodeContext, cls: IronPython.Runtime.Types.PythonType, kwargsø: System.Collections.Generic.IDictionary[System.Object, System.Object], argsø: System.Array[System.Object], ) -> System.Object:
        ...

    @staticmethod
    def __reduce__(context: IronPython.Runtime.CodeContext, self: System.Object, ) -> System.Object:
        ...

    @staticmethod
    @typing.overload
    def __reduce_ex__(context: IronPython.Runtime.CodeContext, self: System.Object, ) -> System.Object:
        ...

    @staticmethod
    @typing.overload
    def __reduce_ex__(context: IronPython.Runtime.CodeContext, self: System.Object, protocol: System.Object, ) -> System.Object:
        ...

    @staticmethod
    def __repr__(self: System.Object, ) -> str:
        ...

    @staticmethod
    def __setattr__(context: IronPython.Runtime.CodeContext, self: System.Object, name: str, value: System.Object, ) -> None:
        ...

    @staticmethod
    def AdjustPointerSize(size: int, ) -> int:
        ...

    @staticmethod
    def __sizeof__(self: System.Object, ) -> int:
        ...

    @staticmethod
    def GetTypeSize(t: System.Type, ) -> int:
        ...

    @staticmethod
    def __str__(context: IronPython.Runtime.CodeContext, o: System.Object, ) -> str:
        ...

    @staticmethod
    def __subclasshook__(args: System.Array[System.Object], ) -> IronPython.Runtime.Types.NotImplementedType:
        ...

    @staticmethod
    def __eq__(self: System.Object, value: System.Object, ) -> System.Object:
        ...

    @staticmethod
    def __ne__(context: IronPython.Runtime.CodeContext, self: System.Object, other: System.Object, ) -> System.Object:
        ...

    @staticmethod
    def __gt__(self: System.Object, value: System.Object, ) -> IronPython.Runtime.Types.NotImplementedType:
        ...

    @staticmethod
    def __lt__(self: System.Object, value: System.Object, ) -> IronPython.Runtime.Types.NotImplementedType:
        ...

    @staticmethod
    def __ge__(self: System.Object, value: System.Object, ) -> IronPython.Runtime.Types.NotImplementedType:
        ...

    @staticmethod
    def __le__(self: System.Object, value: System.Object, ) -> IronPython.Runtime.Types.NotImplementedType:
        ...

    @staticmethod
    def __format__(context: IronPython.Runtime.CodeContext, self: System.Object, formatSpec: str, ) -> str:
        ...

    @staticmethod
    def GetInitializedSlotValues(obj: System.Object, ) -> IronPython.Runtime.PythonDictionary:
        ...

    @staticmethod
    def ReduceProtocol0(context: IronPython.Runtime.CodeContext, self: System.Object, ) -> System.Object:
        ...

    @staticmethod
    def ReduceProtocol2(context: IronPython.Runtime.CodeContext, self: System.Object, ) -> IronPython.Runtime.PythonTuple:
        ...

class ExtensibleComplex(Microsoft.Scripting.Runtime.Extensible[System.Numerics.Complex]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def Value(self) -> System.Numerics.Complex:
        ...

    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def __init__(self, real: float, ):
        ...

    @typing.overload
    def __init__(self, real: float, imag: float, ):
        ...

class UInt64Ops(System.Object, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    @staticmethod
    def to_bytes(value: int, length: int, byteorder: str, signed: bool = ..., ) -> IronPython.Runtime.Bytes:
        ...

    @staticmethod
    @typing.overload
    def __new__(cls: IronPython.Runtime.Types.PythonType, ) -> System.Object:
        ...

    @staticmethod
    @typing.overload
    def __new__(cls: IronPython.Runtime.Types.PythonType, value: System.Object, ) -> System.Object:
        ...

    @staticmethod
    def __bool__(x: int, ) -> bool:
        ...

    @staticmethod
    def __repr__(x: int, ) -> str:
        ...

    @staticmethod
    def __trunc__(x: int, ) -> int:
        ...

    @staticmethod
    def __int__(x: int, ) -> System.Numerics.BigInteger:
        ...

    @staticmethod
    def __index__(x: int, ) -> System.Numerics.BigInteger:
        ...

    @staticmethod
    def __hash__(x: int, ) -> int:
        ...

    @staticmethod
    def conjugate(x: int, ) -> int:
        ...

    @staticmethod
    def bit_length(value: int, ) -> int:
        ...

class Int32Ops(System.Object, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def Zero(self) -> System.Object:
        ...

    @property
    def One(self) -> System.Object:
        ...

    @property
    def MinusOne(self) -> System.Object:
        ...

    # methods
    @staticmethod
    def conjugate(x: int, ) -> int:
        ...

    @staticmethod
    def bit_length(value: int, ) -> int:
        ...

    @staticmethod
    def to_bytes(value: int, length: int, byteorder: str, signed: bool = ..., ) -> IronPython.Runtime.Bytes:
        ...

    @staticmethod
    def __getnewargs__(context: IronPython.Runtime.CodeContext, self: int, ) -> System.Object:
        ...

    @staticmethod
    @typing.overload
    def __round__(self: int, ) -> int:
        ...

    @staticmethod
    @typing.overload
    def __round__(number: int, ndigits: System.Numerics.BigInteger, ) -> System.Object:
        ...

    @staticmethod
    @typing.overload
    def __round__(self: int, ndigits: System.Object, ) -> System.Object:
        ...

    @staticmethod
    @typing.overload
    def __divmod__(x: int, y: int, ) -> IronPython.Runtime.PythonTuple:
        ...

    @staticmethod
    @typing.overload
    def __divmod__(x: int, y: System.Object, ) -> System.Object:
        ...

    @staticmethod
    def __rdivmod__(x: int, y: int, ) -> System.Object:
        ...

    @staticmethod
    def ToBigInteger(self: int, ) -> System.Numerics.BigInteger:
        ...

    @staticmethod
    def __format__(context: IronPython.Runtime.CodeContext, self: int, formatSpec: str, ) -> str:
        ...

    @staticmethod
    def from_bytes(context: IronPython.Runtime.CodeContext, type: IronPython.Runtime.Types.PythonType, bytes: System.Object, byteorder: str, signed: bool = ..., ) -> System.Object:
        ...

    @staticmethod
    def ToHex(self: int, lowercase: bool, ) -> str:
        ...

    @staticmethod
    def ToOctal(self: int, lowercase: bool, ) -> str:
        ...

    @staticmethod
    @typing.overload
    def ToBinary(self: int, ) -> str:
        ...

    @staticmethod
    @typing.overload
    def ToBinary(self: int, includeType: bool, ) -> str:
        ...

    @staticmethod
    @typing.overload
    def ToByteArray(self: int, ) -> System.Array[int]:
        ...

    @staticmethod
    @typing.overload
    def ToByteArray(self: int, isUnsigned: bool = ..., isBigEndian: bool = ..., ) -> System.Array[int]:
        ...

    @staticmethod
    def GetByteCount(self: int, isUnsigned: bool = ..., ) -> int:
        ...

    @staticmethod
    def TryWriteBytes(self: int, destination: System.Span[int], bytesWritten: ref[int], isUnsigned: bool = ..., isBigEndian: bool = ..., ) -> bool:
        ...

    @staticmethod
    def GetBitLength(self: int, ) -> int:
        ...

    @staticmethod
    def Compare(left: System.Numerics.BigInteger, right: System.Numerics.BigInteger, ) -> System.Numerics.BigInteger:
        ...

    @staticmethod
    def Min(left: System.Numerics.BigInteger, right: System.Numerics.BigInteger, ) -> System.Numerics.BigInteger:
        ...

    @staticmethod
    def Max(left: System.Numerics.BigInteger, right: System.Numerics.BigInteger, ) -> System.Numerics.BigInteger:
        ...

    @staticmethod
    @typing.overload
    def Log(value: System.Numerics.BigInteger, ) -> float:
        ...

    @staticmethod
    @typing.overload
    def Log(value: System.Numerics.BigInteger, baseValue: float, ) -> float:
        ...

    @staticmethod
    def Log10(value: System.Numerics.BigInteger, ) -> float:
        ...

    @staticmethod
    def Pow(value: System.Numerics.BigInteger, exponent: int, ) -> System.Object:
        ...

    @staticmethod
    def ModPow(value: System.Numerics.BigInteger, exponent: System.Numerics.BigInteger, modulus: System.Numerics.BigInteger, ) -> System.Object:
        ...

    @staticmethod
    def Negate(value: System.Numerics.BigInteger, ) -> System.Numerics.BigInteger:
        ...

    @staticmethod
    def Abs(value: System.Numerics.BigInteger, ) -> System.Numerics.BigInteger:
        ...

    @staticmethod
    def Add(left: System.Numerics.BigInteger, right: System.Numerics.BigInteger, ) -> System.Numerics.BigInteger:
        ...

    @staticmethod
    def Subtract(left: System.Numerics.BigInteger, right: System.Numerics.BigInteger, ) -> System.Numerics.BigInteger:
        ...

    @staticmethod
    def Multiply(left: System.Numerics.BigInteger, right: System.Numerics.BigInteger, ) -> System.Numerics.BigInteger:
        ...

    @staticmethod
    def Divide(left: System.Numerics.BigInteger, right: System.Numerics.BigInteger, ) -> System.Numerics.BigInteger:
        ...

    @staticmethod
    def Remainder(dividend: System.Numerics.BigInteger, divisor: System.Numerics.BigInteger, ) -> System.Numerics.BigInteger:
        ...

    @staticmethod
    def DivRem(dividend: System.Numerics.BigInteger, divisor: System.Numerics.BigInteger, remainder: ref[System.Numerics.BigInteger], ) -> System.Numerics.BigInteger:
        ...

    @staticmethod
    def GreatestCommonDivisor(left: System.Numerics.BigInteger, right: System.Numerics.BigInteger, ) -> System.Numerics.BigInteger:
        ...

    @staticmethod
    @typing.overload
    def __new__(cls: IronPython.Runtime.Types.PythonType, ) -> System.Object:
        ...

    @staticmethod
    @typing.overload
    def __new__(cls: IronPython.Runtime.Types.PythonType, value: System.Object, ) -> System.Object:
        ...

    @staticmethod
    def __bool__(x: int, ) -> bool:
        ...

    @staticmethod
    def __repr__(x: int, ) -> str:
        ...

    @staticmethod
    def __trunc__(x: int, ) -> int:
        ...

    @staticmethod
    def __int__(x: int, ) -> int:
        ...

    @staticmethod
    def __index__(x: int, ) -> int:
        ...

    @staticmethod
    def __hash__(x: int, ) -> int:
        ...

class CharOps(System.Object, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    @staticmethod
    @typing.overload
    def __new__(cls: IronPython.Runtime.Types.PythonType, ) -> System.Object:
        ...

    @staticmethod
    @typing.overload
    def __new__(cls: IronPython.Runtime.Types.PythonType, value: int, ) -> System.Object:
        ...

    @staticmethod
    @typing.overload
    def __new__(cls: IronPython.Runtime.Types.PythonType, value: str, ) -> System.Object:
        ...

    @staticmethod
    def __repr__(self: str, ) -> str:
        ...

    @staticmethod
    def __hash__(self: str, ) -> int:
        ...

    @staticmethod
    def __index__(self: str, ) -> int:
        ...

    @staticmethod
    @typing.overload
    def __contains__(self: str, other: str, ) -> bool:
        ...

    @staticmethod
    @typing.overload
    def __contains__(self: str, other: str, ) -> bool:
        ...

class BigIntegerOps(System.Object, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    @staticmethod
    @typing.overload
    def ToDouble(self: System.Numerics.BigInteger, provider: System.IFormatProvider, ) -> float:
        ...

    @staticmethod
    @typing.overload
    def ToDouble(self: System.Numerics.BigInteger, ) -> float:
        ...

    @staticmethod
    def ToSingle(self: System.Numerics.BigInteger, provider: System.IFormatProvider, ) -> float:
        ...

    @staticmethod
    def ToInt16(self: System.Numerics.BigInteger, provider: System.IFormatProvider, ) -> int:
        ...

    @staticmethod
    def ToInt32(self: System.Numerics.BigInteger, provider: System.IFormatProvider, ) -> int:
        ...

    @staticmethod
    def ToInt64(self: System.Numerics.BigInteger, provider: System.IFormatProvider, ) -> int:
        ...

    @staticmethod
    def ToUInt16(self: System.Numerics.BigInteger, provider: System.IFormatProvider, ) -> int:
        ...

    @staticmethod
    def ToUInt32(self: System.Numerics.BigInteger, provider: System.IFormatProvider, ) -> int:
        ...

    @staticmethod
    def ToUInt64(self: System.Numerics.BigInteger, provider: System.IFormatProvider, ) -> int:
        ...

    @staticmethod
    def ToDateTime(self: System.Numerics.BigInteger, provider: System.IFormatProvider, ) -> System.DateTime:
        ...

    @staticmethod
    def ToType(self: System.Numerics.BigInteger, targetType: System.Type, provider: System.IFormatProvider, ) -> System.Object:
        ...

    @staticmethod
    def GetTypeCode(self: System.Numerics.BigInteger, ) -> int:
        ...

    @staticmethod
    def AbsToHex(val: System.Numerics.BigInteger, lowercase: bool, ) -> str:
        ...

    @staticmethod
    def ToOctal(val: System.Numerics.BigInteger, lowercase: bool, ) -> str:
        ...

    @staticmethod
    @typing.overload
    def ToBinary(val: System.Numerics.BigInteger, ) -> str:
        ...

    @staticmethod
    @typing.overload
    def ToBinary(val: System.Numerics.BigInteger, includeType: bool, lowercase: bool, ) -> str:
        ...

    @staticmethod
    def ToDigits(val: System.Numerics.BigInteger, radix: int, lower: bool, ) -> str:
        ...

    @staticmethod
    def FastNew(context: IronPython.Runtime.CodeContext, o: System.Object, base: int = ..., ) -> System.Object:
        ...

    @staticmethod
    @typing.overload
    def __new__(context: IronPython.Runtime.CodeContext, cls: IronPython.Runtime.Types.PythonType, x: System.Object, base: System.Object, ) -> System.Object:
        ...

    @staticmethod
    @typing.overload
    def __new__(context: IronPython.Runtime.CodeContext, cls: IronPython.Runtime.Types.PythonType, x: System.Object, ) -> System.Object:
        ...

    @staticmethod
    @typing.overload
    def __new__(context: IronPython.Runtime.CodeContext, cls: IronPython.Runtime.Types.PythonType, ) -> System.Object:
        ...

    @staticmethod
    @typing.overload
    def __new__(context: IronPython.Runtime.CodeContext, cls: IronPython.Runtime.Types.PythonType, x: IronPython.Runtime.IBufferProtocol, base: int = ..., ) -> System.Object:
        ...

    @staticmethod
    @typing.overload
    def __new__(context: IronPython.Runtime.CodeContext, cls: IronPython.Runtime.Types.PythonType, x: IronPython.Runtime.IBufferProtocol, base: System.Object, ) -> System.Object:
        ...

    @staticmethod
    def ValidateType(cls: IronPython.Runtime.Types.PythonType, ) -> None:
        ...

    @staticmethod
    def BaseFromObject(base: System.Object, ) -> int:
        ...

    @staticmethod
    def ReturnObject(context: IronPython.Runtime.CodeContext, cls: IronPython.Runtime.Types.PythonType, value: System.Object, ) -> System.Object:
        ...

    @staticmethod
    def FindStart(s: str, radix: int, ) -> int:
        ...

    @staticmethod
    def IsInt32(self: System.Numerics.BigInteger, ) -> bool:
        ...

    @staticmethod
    def __bool__(x: System.Numerics.BigInteger, ) -> bool:
        ...

    @staticmethod
    def __trunc__(self: System.Numerics.BigInteger, ) -> System.Numerics.BigInteger:
        ...

    @staticmethod
    def __int__(x: System.Numerics.BigInteger, ) -> System.Object:
        ...

    @staticmethod
    def __index__(self: System.Numerics.BigInteger, ) -> System.Numerics.BigInteger:
        ...

    @staticmethod
    def __float__(self: System.Numerics.BigInteger, ) -> System.Object:
        ...

    @staticmethod
    def __hash__(self: System.Numerics.BigInteger, ) -> int:
        ...

    @staticmethod
    def __repr__(self: System.Numerics.BigInteger, ) -> str:
        ...

    @staticmethod
    def __getnewargs__(context: IronPython.Runtime.CodeContext, self: System.Numerics.BigInteger, ) -> System.Object:
        ...

    @staticmethod
    @typing.overload
    def __round__(number: System.Numerics.BigInteger, ) -> System.Numerics.BigInteger:
        ...

    @staticmethod
    @typing.overload
    def __round__(self: System.Numerics.BigInteger, ndigits: System.Numerics.BigInteger, ) -> System.Numerics.BigInteger:
        ...

    @staticmethod
    @typing.overload
    def __round__(self: System.Numerics.BigInteger, ndigits: System.Object, ) -> System.Numerics.BigInteger:
        ...

    @staticmethod
    def DivMod(x: System.Numerics.BigInteger, y: System.Numerics.BigInteger, r: ref[System.Numerics.BigInteger], ) -> System.Numerics.BigInteger:
        ...

    @staticmethod
    def Add(x: System.Numerics.BigInteger, y: System.Numerics.BigInteger, ) -> System.Numerics.BigInteger:
        ...

    @staticmethod
    def Subtract(x: System.Numerics.BigInteger, y: System.Numerics.BigInteger, ) -> System.Numerics.BigInteger:
        ...

    @staticmethod
    def Multiply(x: System.Numerics.BigInteger, y: System.Numerics.BigInteger, ) -> System.Numerics.BigInteger:
        ...

    @staticmethod
    def OnesComplement(x: System.Numerics.BigInteger, ) -> System.Numerics.BigInteger:
        ...

    @staticmethod
    def BitwiseAnd(x: System.Numerics.BigInteger, y: System.Numerics.BigInteger, ) -> System.Numerics.BigInteger:
        ...

    @staticmethod
    def BitwiseOr(x: System.Numerics.BigInteger, y: System.Numerics.BigInteger, ) -> System.Numerics.BigInteger:
        ...

    @staticmethod
    def ExclusiveOr(x: System.Numerics.BigInteger, y: System.Numerics.BigInteger, ) -> System.Numerics.BigInteger:
        ...

    @staticmethod
    def conjugate(self: System.Numerics.BigInteger, ) -> System.Numerics.BigInteger:
        ...

    @staticmethod
    def bit_length(self: System.Numerics.BigInteger, ) -> System.Object:
        ...

    @staticmethod
    def ToBigInteger(self: System.Numerics.BigInteger, ) -> System.Numerics.BigInteger:
        ...

    @staticmethod
    def __format__(context: IronPython.Runtime.CodeContext, self: System.Numerics.BigInteger, formatSpec: str, ) -> str:
        ...

    @staticmethod
    def to_bytes(value: System.Numerics.BigInteger, length: int, byteorder: str, signed: bool = ..., ) -> IronPython.Runtime.Bytes:
        ...

    @staticmethod
    def from_bytes(context: IronPython.Runtime.CodeContext, type: IronPython.Runtime.Types.PythonType, bytes: System.Object, byteorder: str, signed: bool = ..., ) -> System.Object:
        ...

    @staticmethod
    def ToBoolean(self: System.Numerics.BigInteger, provider: System.IFormatProvider, ) -> bool:
        ...

    @staticmethod
    def ToByte(self: System.Numerics.BigInteger, provider: System.IFormatProvider, ) -> int:
        ...

    @staticmethod
    def ToSByte(self: System.Numerics.BigInteger, provider: System.IFormatProvider, ) -> int:
        ...

    @staticmethod
    def ToChar(self: System.Numerics.BigInteger, provider: System.IFormatProvider, ) -> str:
        ...

    @staticmethod
    def ToDecimal(self: System.Numerics.BigInteger, provider: System.IFormatProvider, ) -> System.Decimal:
        ...

class UInt16Ops(System.Object, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    @staticmethod
    @typing.overload
    def __new__(cls: IronPython.Runtime.Types.PythonType, ) -> System.Object:
        ...

    @staticmethod
    @typing.overload
    def __new__(cls: IronPython.Runtime.Types.PythonType, value: System.Object, ) -> System.Object:
        ...

    @staticmethod
    def __bool__(x: int, ) -> bool:
        ...

    @staticmethod
    def __repr__(x: int, ) -> str:
        ...

    @staticmethod
    def __trunc__(x: int, ) -> int:
        ...

    @staticmethod
    def __int__(x: int, ) -> int:
        ...

    @staticmethod
    def __index__(x: int, ) -> int:
        ...

    @staticmethod
    def __hash__(x: int, ) -> int:
        ...

    @staticmethod
    def conjugate(x: int, ) -> int:
        ...

    @staticmethod
    def bit_length(value: int, ) -> int:
        ...

    @staticmethod
    def to_bytes(value: int, length: int, byteorder: str, signed: bool = ..., ) -> IronPython.Runtime.Bytes:
        ...

class PythonOps(System.Object, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields
    EmptyTuple: IronPython.Runtime.PythonTuple = ...
    CurrentExceptionState: IronPython.Runtime.Operations.ExceptionState = ...

    # properties
    @property
    def Ellipsis(self) -> IronPython.Runtime.Types.Ellipsis:
        ...

    @property
    def NotImplemented(self) -> IronPython.Runtime.Types.NotImplementedType:
        ...

    # methods
    @staticmethod
    def TypeErrorForProtectedMember(type: System.Type, name: str, ) -> System.Exception:
        ...

    @staticmethod
    def TypeErrorForGenericMethod(type: System.Type, name: str, ) -> System.Exception:
        ...

    @staticmethod
    def TypeErrorForUnIndexableObject(o: System.Object, ) -> System.Exception:
        ...

    @staticmethod
    def TypeErrorForBadEnumConversion(value: System.Object, ) -> T:
        ...

    @staticmethod
    def UnreadableProperty() -> System.Exception:
        ...

    @staticmethod
    def UnsetableProperty() -> System.Exception:
        ...

    @staticmethod
    def UndeletableProperty() -> System.Exception:
        ...

    @staticmethod
    def Warning(format: str, args: System.Array[System.Object], ) -> System.Exception:
        ...

    @staticmethod
    def GetFunctionStack() -> System.Collections.Generic.List[IronPython.Runtime.Operations.FunctionStack]:
        ...

    @staticmethod
    def GetFunctionStackNoCreate() -> System.Collections.Generic.List[IronPython.Runtime.Operations.FunctionStack]:
        ...

    @staticmethod
    def PushFrame(context: IronPython.Runtime.CodeContext, function: IronPython.Runtime.FunctionCode, ) -> System.Collections.Generic.List[IronPython.Runtime.Operations.FunctionStack]:
        ...

    @staticmethod
    def ToGenerator(code: Microsoft.Scripting.Ast.LightLambdaExpression, shouldInterpret: bool, debuggable: bool, compilationThreshold: int, ) -> Microsoft.Scripting.Ast.LightLambdaExpression:
        ...

    @staticmethod
    def UpdateStackTrace(e: System.Exception, context: IronPython.Runtime.CodeContext, funcCode: IronPython.Runtime.FunctionCode, line: int, ) -> None:
        ...

    @staticmethod
    def GetDynamicStackFrames(e: System.Exception, ) -> System.Array[Microsoft.Scripting.Runtime.DynamicStackFrame]:
        ...

    @staticmethod
    def ModuleTryGetMember(context: IronPython.Runtime.CodeContext, module: IronPython.Runtime.PythonModule, name: str, res: ref[System.Object], ) -> bool:
        ...

    @staticmethod
    def ScopeSetMember(context: IronPython.Runtime.CodeContext, scope: Microsoft.Scripting.Runtime.Scope, name: str, value: System.Object, ) -> None:
        ...

    @staticmethod
    def ScopeGetMember(context: IronPython.Runtime.CodeContext, scope: Microsoft.Scripting.Runtime.Scope, name: str, ) -> System.Object:
        ...

    @staticmethod
    def ScopeTryGetMember(context: IronPython.Runtime.CodeContext, scope: Microsoft.Scripting.Runtime.Scope, name: str, value: ref[System.Object], ) -> bool:
        ...

    @staticmethod
    def ScopeContainsMember(context: IronPython.Runtime.CodeContext, scope: Microsoft.Scripting.Runtime.Scope, name: str, ) -> bool:
        ...

    @staticmethod
    def ScopeDeleteMember(context: IronPython.Runtime.CodeContext, scope: Microsoft.Scripting.Runtime.Scope, name: str, ) -> bool:
        ...

    @staticmethod
    def ScopeGetMemberNames(context: IronPython.Runtime.CodeContext, scope: Microsoft.Scripting.Runtime.Scope, ) -> System.Collections.Generic.IList[System.Object]:
        ...

    @staticmethod
    def IsExtensionSet(codeContext: IronPython.Runtime.CodeContext, id: int, ) -> bool:
        ...

    @staticmethod
    def GetExtensionMethodSet(context: IronPython.Runtime.CodeContext, ) -> System.Object:
        ...

    @staticmethod
    def ImportError(format: str, args: System.Array[System.Object], ) -> System.Exception:
        ...

    @staticmethod
    def RuntimeError(format: str, args: System.Array[System.Object], ) -> System.Exception:
        ...

    @staticmethod
    def UnicodeTranslateError(format: str, args: System.Array[System.Object], ) -> System.Exception:
        ...

    @staticmethod
    def PendingDeprecationWarning(format: str, args: System.Array[System.Object], ) -> System.Exception:
        ...

    @staticmethod
    def LookupError(format: str, args: System.Array[System.Object], ) -> System.Exception:
        ...

    @staticmethod
    @typing.overload
    def OSError(format: str, args: System.Array[System.Object], ) -> System.Exception:
        ...

    @staticmethod
    @typing.overload
    def OSError(errno: int, strerror: str, filename: str = ..., winerror: System.Nullable[int] = ..., filename2: str = ..., ) -> System.Exception:
        ...

    @staticmethod
    def DeprecationWarning(format: str, args: System.Array[System.Object], ) -> System.Exception:
        ...

    @staticmethod
    def UnicodeError(format: str, args: System.Array[System.Object], ) -> System.Exception:
        ...

    @staticmethod
    def FloatingPointError(format: str, args: System.Array[System.Object], ) -> System.Exception:
        ...

    @staticmethod
    def ReferenceError(format: str, args: System.Array[System.Object], ) -> System.Exception:
        ...

    @staticmethod
    def FutureWarning(format: str, args: System.Array[System.Object], ) -> System.Exception:
        ...

    @staticmethod
    def AssertionError(format: str, args: System.Array[System.Object], ) -> System.Exception:
        ...

    @staticmethod
    def RuntimeWarning(format: str, args: System.Array[System.Object], ) -> System.Exception:
        ...

    @staticmethod
    def ImportWarning(format: str, args: System.Array[System.Object], ) -> System.Exception:
        ...

    @staticmethod
    def UserWarning(format: str, args: System.Array[System.Object], ) -> System.Exception:
        ...

    @staticmethod
    @typing.overload
    def SyntaxWarning(format: str, args: System.Array[System.Object], ) -> System.Exception:
        ...

    @staticmethod
    @typing.overload
    def SyntaxWarning(message: str, sourceUnit: Microsoft.Scripting.SourceUnit, span: Microsoft.Scripting.SourceSpan, errorCode: int, ) -> None:
        ...

    @staticmethod
    def UnicodeWarning(format: str, args: System.Array[System.Object], ) -> System.Exception:
        ...

    @staticmethod
    @typing.overload
    def StopIteration(format: str, args: System.Array[System.Object], ) -> System.Exception:
        ...

    @staticmethod
    @typing.overload
    def StopIteration() -> System.Exception:
        ...

    @staticmethod
    def BytesWarning(format: str, args: System.Array[System.Object], ) -> System.Exception:
        ...

    @staticmethod
    def BufferError(format: str, args: System.Array[System.Object], ) -> System.Exception:
        ...

    @staticmethod
    def ResourceWarning(format: str, args: System.Array[System.Object], ) -> System.Exception:
        ...

    @staticmethod
    def FileExistsError(format: str, args: System.Array[System.Object], ) -> System.Exception:
        ...

    @staticmethod
    def BlockingIOError(format: str, args: System.Array[System.Object], ) -> System.Exception:
        ...

    @staticmethod
    def NotADirectoryError(format: str, args: System.Array[System.Object], ) -> System.Exception:
        ...

    @staticmethod
    def InterruptedError(format: str, args: System.Array[System.Object], ) -> System.Exception:
        ...

    @staticmethod
    def ChildProcessError(format: str, args: System.Array[System.Object], ) -> System.Exception:
        ...

    @staticmethod
    def IsADirectoryError(format: str, args: System.Array[System.Object], ) -> System.Exception:
        ...

    @staticmethod
    def ProcessLookupError(format: str, args: System.Array[System.Object], ) -> System.Exception:
        ...

    @staticmethod
    def ConnectionError(format: str, args: System.Array[System.Object], ) -> System.Exception:
        ...

    @staticmethod
    def ConnectionAbortedError(format: str, args: System.Array[System.Object], ) -> System.Exception:
        ...

    @staticmethod
    def BrokenPipeError(format: str, args: System.Array[System.Object], ) -> System.Exception:
        ...

    @staticmethod
    def ConnectionRefusedError(format: str, args: System.Array[System.Object], ) -> System.Exception:
        ...

    @staticmethod
    def ConnectionResetError(format: str, args: System.Array[System.Object], ) -> System.Exception:
        ...

    @staticmethod
    def RecursionError(format: str, args: System.Array[System.Object], ) -> System.Exception:
        ...

    @staticmethod
    def StopAsyncIteration(format: str, args: System.Array[System.Object], ) -> System.Exception:
        ...

    @staticmethod
    def MakeClosureCell() -> IronPython.Runtime.ClosureCell:
        ...

    @staticmethod
    def MakeClosureCellWithValue(initialValue: System.Object, ) -> IronPython.Runtime.ClosureCell:
        ...

    @staticmethod
    def GetClosureTupleFromFunction(function: IronPython.Runtime.PythonFunction, ) -> Microsoft.Scripting.MutableTuple:
        ...

    @staticmethod
    def GetClosureTupleFromGenerator(generator: IronPython.Runtime.PythonGenerator, ) -> Microsoft.Scripting.MutableTuple:
        ...

    @staticmethod
    def GetClosureTupleFromContext(context: IronPython.Runtime.CodeContext, ) -> Microsoft.Scripting.MutableTuple:
        ...

    @staticmethod
    def GetParentContextFromFunction(function: IronPython.Runtime.PythonFunction, ) -> IronPython.Runtime.CodeContext:
        ...

    @staticmethod
    def GetParentContextFromGenerator(generator: IronPython.Runtime.PythonGenerator, ) -> IronPython.Runtime.CodeContext:
        ...

    @staticmethod
    def GetGlobal(context: IronPython.Runtime.CodeContext, name: str, ) -> System.Object:
        ...

    @staticmethod
    def GetLocal(context: IronPython.Runtime.CodeContext, name: str, ) -> System.Object:
        ...

    @staticmethod
    def GetVariable(context: IronPython.Runtime.CodeContext, name: str, isGlobal: bool, lightThrow: bool, ) -> System.Object:
        ...

    @staticmethod
    def RawGetGlobal(context: IronPython.Runtime.CodeContext, name: str, ) -> System.Object:
        ...

    @staticmethod
    def RawGetLocal(context: IronPython.Runtime.CodeContext, name: str, ) -> System.Object:
        ...

    @staticmethod
    def SetGlobal(context: IronPython.Runtime.CodeContext, name: str, value: System.Object, ) -> None:
        ...

    @staticmethod
    def SetLocal(context: IronPython.Runtime.CodeContext, name: str, value: System.Object, ) -> None:
        ...

    @staticmethod
    def DeleteGlobal(context: IronPython.Runtime.CodeContext, name: str, ) -> None:
        ...

    @staticmethod
    def DeleteLocal(context: IronPython.Runtime.CodeContext, name: str, ) -> None:
        ...

    @staticmethod
    def GetGlobalArrayFromContext(context: IronPython.Runtime.CodeContext, ) -> System.Array[IronPython.Compiler.PythonGlobal]:
        ...

    @staticmethod
    def MultipleArgumentError(function: IronPython.Runtime.PythonFunction, name: str, ) -> System.Exception:
        ...

    @staticmethod
    def MultipleKeywordArgumentError(function: IronPython.Runtime.PythonFunction, name: str, ) -> System.Exception:
        ...

    @staticmethod
    def UnexpectedKeywordArgumentError(function: IronPython.Runtime.PythonFunction, name: str, ) -> System.Exception:
        ...

    @staticmethod
    def StaticAssignmentFromInstanceError(tracker: Microsoft.Scripting.Actions.PropertyTracker, isAssignment: bool, ) -> System.Exception:
        ...

    @staticmethod
    def FunctionBadArgumentError(func: IronPython.Runtime.PythonFunction, count: int, ) -> System.Exception:
        ...

    @staticmethod
    def BadKeywordArgumentError(func: IronPython.Runtime.PythonFunction, count: int, ) -> System.Exception:
        ...

    @staticmethod
    def AttributeErrorForMissingOrReadonly(context: IronPython.Runtime.CodeContext, dt: IronPython.Runtime.Types.PythonType, name: str, ) -> System.Exception:
        ...

    @staticmethod
    @typing.overload
    def AttributeErrorForMissingAttribute(o: System.Object, name: str, ) -> System.Exception:
        ...

    @staticmethod
    @typing.overload
    def AttributeErrorForMissingAttribute(typeName: str, attributeName: str, ) -> System.Exception:
        ...

    @staticmethod
    def ValueError(format: str, args: System.Array[System.Object], ) -> System.Exception:
        ...

    @staticmethod
    @typing.overload
    def KeyError(key: System.Object, ) -> System.Exception:
        ...

    @staticmethod
    @typing.overload
    def KeyError(format: str, args: System.Array[System.Object], ) -> System.Exception:
        ...

    @staticmethod
    def UnicodeDecodeError(message: str, bytesUnknown: System.Array[int], index: int, ) -> System.Exception:
        ...

    @staticmethod
    @typing.overload
    def UnicodeEncodeError(encoding: str, object: str, start: int, end: int, reason: str, ) -> System.Exception:
        ...

    @staticmethod
    @typing.overload
    def UnicodeEncodeError(message: str, charUnknown: str, index: int, ) -> System.Exception:
        ...

    @staticmethod
    @typing.overload
    def UnicodeEncodeError(message: str, charUnknownHigh: str, charUnknownLow: str, index: int, ) -> System.Exception:
        ...

    @staticmethod
    @typing.overload
    def UnicodeEncodeError(message: str, runeUnknown: int, index: int, ) -> System.Exception:
        ...

    @staticmethod
    @typing.overload
    def IOError(inner: System.Exception, ) -> System.Exception:
        ...

    @staticmethod
    @typing.overload
    def IOError(format: str, args: System.Array[System.Object], ) -> System.Exception:
        ...

    @staticmethod
    def EofError(format: str, args: System.Array[System.Object], ) -> System.Exception:
        ...

    @staticmethod
    @typing.overload
    def ZeroDivisionError(format: str, args: System.Array[System.Object], ) -> System.Exception:
        ...

    @staticmethod
    @typing.overload
    def ZeroDivisionError() -> System.Exception:
        ...

    @staticmethod
    def SystemError(format: str, args: System.Array[System.Object], ) -> System.Exception:
        ...

    @staticmethod
    def TypeError(format: str, args: System.Array[System.Object], ) -> System.Exception:
        ...

    @staticmethod
    def IndexError(format: str, args: System.Array[System.Object], ) -> System.Exception:
        ...

    @staticmethod
    @typing.overload
    def MemoryError() -> System.Exception:
        ...

    @staticmethod
    @typing.overload
    def MemoryError(message: str, ) -> System.Exception:
        ...

    @staticmethod
    @typing.overload
    def MemoryError(format: str, args: System.Array[System.Object], ) -> System.Exception:
        ...

    @staticmethod
    def ArithmeticError(format: str, args: System.Array[System.Object], ) -> System.Exception:
        ...

    @staticmethod
    def NotImplementedError(format: str, args: System.Array[System.Object], ) -> System.Exception:
        ...

    @staticmethod
    def AttributeError(format: str, args: System.Array[System.Object], ) -> System.Exception:
        ...

    @staticmethod
    def OverflowError(format: str, args: System.Array[System.Object], ) -> System.Exception:
        ...

    @staticmethod
    def WindowsError(format: str, args: System.Array[System.Object], ) -> System.Exception:
        ...

    @staticmethod
    def TimeoutError(format: str, args: System.Array[System.Object], ) -> System.Exception:
        ...

    @staticmethod
    def SystemExit() -> System.Exception:
        ...

    @staticmethod
    @typing.overload
    def SyntaxError(format: str, args: System.Array[System.Object], ) -> Microsoft.Scripting.SyntaxErrorException:
        ...

    @staticmethod
    @typing.overload
    def SyntaxError(message: str, sourceUnit: Microsoft.Scripting.SourceUnit, span: Microsoft.Scripting.SourceSpan, errorCode: int, ) -> Microsoft.Scripting.SyntaxErrorException:
        ...

    @staticmethod
    def BadSourceEncodingError(message: str, line: int, path: str, ) -> Microsoft.Scripting.SyntaxErrorException:
        ...

    @staticmethod
    def InvalidType(o: System.Object, handle: System.RuntimeTypeHandle, ) -> System.Exception:
        ...

    @staticmethod
    def ValueErrorForUnpackMismatch(left: int, argcntafter: int, right: int, ) -> System.Exception:
        ...

    @staticmethod
    def NameError(name: str, ) -> System.Exception:
        ...

    @staticmethod
    def GlobalNameError(name: str, ) -> System.Exception:
        ...

    @staticmethod
    @typing.overload
    def TypeErrorForUnboundMethodCall(methodName: str, methodType: System.Type, instance: System.Object, ) -> System.Exception:
        ...

    @staticmethod
    @typing.overload
    def TypeErrorForUnboundMethodCall(methodName: str, methodType: IronPython.Runtime.Types.PythonType, instance: System.Object, ) -> System.Exception:
        ...

    @staticmethod
    def TypeErrorForIllegalSend() -> System.Exception:
        ...

    @staticmethod
    def TypeErrorForArgumentCountMismatch(methodName: str, expectedArgCount: int, actualArgCount: int, ) -> System.Exception:
        ...

    @staticmethod
    def TypeErrorForOptionalArgumentCountMismatch(methodName: str, expectedArgCount: int, actualArgCount: int, positional: bool = ..., ) -> System.Exception:
        ...

    @staticmethod
    def TypeErrorForTypeMismatch(expectedTypeName: str, instance: System.Object, ) -> System.Exception:
        ...

    @staticmethod
    def TypeErrorForBytesLikeTypeMismatch(instance: System.Object, ) -> System.Exception:
        ...

    @staticmethod
    def TypeErrorForUnhashableType(typeName: str, ) -> System.Exception:
        ...

    @staticmethod
    def TypeErrorForUnhashableObject(obj: System.Object, ) -> System.Exception:
        ...

    @staticmethod
    def TypeErrorForIncompatibleObjectLayout(prefix: str, type: IronPython.Runtime.Types.PythonType, newType: System.Type, ) -> System.Exception:
        ...

    @staticmethod
    def TypeErrorForNonStringAttribute() -> System.Exception:
        ...

    @staticmethod
    def TypeErrorForBadInstance(template: str, instance: System.Object, ) -> System.Exception:
        ...

    @staticmethod
    def TypeErrorForBinaryOp(opSymbol: str, x: System.Object, y: System.Object, ) -> System.Exception:
        ...

    @staticmethod
    def TypeErrorForUnaryOp(opSymbol: str, x: System.Object, ) -> System.Exception:
        ...

    @staticmethod
    def TypeErrorForNonIterableObject(o: System.Object, ) -> System.Exception:
        ...

    @staticmethod
    def TypeErrorForDefaultArgument(message: str, ) -> System.Exception:
        ...

    @staticmethod
    def AttributeErrorForReadonlyAttribute(typeName: str, attributeName: str, ) -> System.Exception:
        ...

    @staticmethod
    def AttributeErrorForBuiltinAttributeDeletion(typeName: str, attributeName: str, ) -> System.Exception:
        ...

    @staticmethod
    def MissingInvokeMethodException(o: System.Object, name: str, ) -> System.Exception:
        ...

    @staticmethod
    def AttributeErrorForObjectMissingAttribute(obj: System.Object, attributeName: str, ) -> System.Exception:
        ...

    @staticmethod
    def AttributeErrorForOldInstanceMissingAttribute(typeName: str, attributeName: str, ) -> System.Exception:
        ...

    @staticmethod
    def AttributeErrorForOldClassMissingAttribute(typeName: str, attributeName: str, ) -> System.Exception:
        ...

    @staticmethod
    def UncallableError(func: System.Object, ) -> System.Exception:
        ...

    @staticmethod
    def ConvertTupleToArray(tuple: IronPython.Runtime.PythonTuple, ) -> System.Array[T]:
        ...

    @staticmethod
    def MakeGenerator(function: IronPython.Runtime.PythonFunction, data: Microsoft.Scripting.MutableTuple, generatorCode: System.Object, ) -> IronPython.Runtime.PythonGenerator:
        ...

    @staticmethod
    def MakeGeneratorExpression(function: System.Object, input: System.Object, ) -> System.Object:
        ...

    @staticmethod
    def MakeFunctionCode(context: IronPython.Runtime.CodeContext, name: str, documentation: str, parameterNames: System.Array[str], argCount: int, flags: int, startIndex: int, endIndex: int, path: str, code: System.Delegate, freeVars: System.Array[str], names: System.Array[str], cellVars: System.Array[str], varNames: System.Array[str], localCount: int, ) -> IronPython.Runtime.FunctionCode:
        ...

    @staticmethod
    def MakeFunction(context: IronPython.Runtime.CodeContext, funcInfo: IronPython.Runtime.FunctionCode, modName: System.Object, defaults: System.Array[System.Object], kwdefaults: IronPython.Runtime.PythonDictionary, annotations: IronPython.Runtime.PythonDictionary, ) -> System.Object:
        ...

    @staticmethod
    def MakeFunctionDebug(context: IronPython.Runtime.CodeContext, funcInfo: IronPython.Runtime.FunctionCode, modName: System.Object, defaults: System.Array[System.Object], kwdefaults: IronPython.Runtime.PythonDictionary, annotations: IronPython.Runtime.PythonDictionary, target: System.Delegate, ) -> System.Object:
        ...

    @staticmethod
    def FunctionGetContext(func: IronPython.Runtime.PythonFunction, ) -> IronPython.Runtime.CodeContext:
        ...

    @staticmethod
    def FunctionGetDefaultValue(func: IronPython.Runtime.PythonFunction, index: int, ) -> System.Object:
        ...

    @staticmethod
    def FunctionGetKeywordOnlyDefaultValue(func: IronPython.Runtime.PythonFunction, index: int, ) -> System.Object:
        ...

    @staticmethod
    def FunctionGetCompatibility(func: IronPython.Runtime.PythonFunction, ) -> int:
        ...

    @staticmethod
    def FunctionGetID(func: IronPython.Runtime.PythonFunction, ) -> int:
        ...

    @staticmethod
    def FunctionGetTarget(func: IronPython.Runtime.PythonFunction, ) -> System.Delegate:
        ...

    @staticmethod
    def FunctionGetLightThrowTarget(func: IronPython.Runtime.PythonFunction, ) -> System.Delegate:
        ...

    @staticmethod
    def FunctionPushFrame(context: IronPython.Runtime.PythonContext, ) -> None:
        ...

    @staticmethod
    def FunctionPushFrameCodeContext(context: IronPython.Runtime.CodeContext, ) -> None:
        ...

    @staticmethod
    def FunctionPopFrame() -> None:
        ...

    @staticmethod
    def ConvertFromObject(obj: System.Object, ) -> T:
        ...

    @staticmethod
    def MakeComplexCallAction(count: int, list: bool, keywords: System.Array[str], ) -> System.Dynamic.DynamicMetaObjectBinder:
        ...

    @staticmethod
    def MakeSimpleCallAction(count: int, ) -> System.Dynamic.DynamicMetaObjectBinder:
        ...

    @staticmethod
    def GeneratorCheckThrowableAndReturnSendValue(self: System.Object, ) -> System.Object:
        ...

    @staticmethod
    def CreateItemEnumerable(source: System.Object, callable: System.Object, site: System.Runtime.CompilerServices.CallSite[System.Func[System.Runtime.CompilerServices.CallSite, IronPython.Runtime.CodeContext, System.Object, int, System.Object]], ) -> IronPython.Runtime.ItemEnumerable:
        ...

    @staticmethod
    def MakeDictionaryKeyEnumerator(dict: IronPython.Runtime.PythonDictionary, ) -> IronPython.Runtime.DictionaryKeyEnumerator:
        ...

    @staticmethod
    def CreatePythonEnumerable(baseObject: System.Object, ) -> System.Collections.IEnumerable:
        ...

    @staticmethod
    def CreateItemEnumerator(source: System.Object, callable: System.Object, site: System.Runtime.CompilerServices.CallSite[System.Func[System.Runtime.CompilerServices.CallSite, IronPython.Runtime.CodeContext, System.Object, int, System.Object]], ) -> System.Collections.IEnumerator:
        ...

    @staticmethod
    def CreatePythonEnumerator(baseObject: System.Object, ) -> System.Collections.IEnumerator:
        ...

    @staticmethod
    def ContainsFromEnumerable(context: IronPython.Runtime.CodeContext, enumerable: System.Object, value: System.Object, ) -> bool:
        ...

    @staticmethod
    def PythonTypeGetMember(context: IronPython.Runtime.CodeContext, type: IronPython.Runtime.Types.PythonType, instance: System.Object, name: str, ) -> System.Object:
        ...

    @staticmethod
    def CheckUninitializedFree(value: System.Object, name: str, ) -> System.Object:
        ...

    @staticmethod
    def CheckUninitializedLocal(value: System.Object, name: str, ) -> System.Object:
        ...

    @staticmethod
    def PythonTypeSetCustomMember(context: IronPython.Runtime.CodeContext, self: IronPython.Runtime.Types.PythonType, name: str, value: System.Object, ) -> System.Object:
        ...

    @staticmethod
    def PythonTypeDeleteCustomMember(context: IronPython.Runtime.CodeContext, self: IronPython.Runtime.Types.PythonType, name: str, ) -> System.Object:
        ...

    @staticmethod
    def IsPythonType(type: IronPython.Runtime.Types.PythonType, ) -> bool:
        ...

    @staticmethod
    def PublishModule(context: IronPython.Runtime.CodeContext, name: str, ) -> System.Object:
        ...

    @staticmethod
    def RemoveModule(context: IronPython.Runtime.CodeContext, name: str, oldValue: System.Object, ) -> None:
        ...

    @staticmethod
    def ListAddForComprehension(l: IronPython.Runtime.PythonList, o: System.Object, ) -> None:
        ...

    @staticmethod
    def SetAddForComprehension(s: IronPython.Runtime.SetCollection, o: System.Object, ) -> None:
        ...

    @staticmethod
    def DictAddForComprehension(d: IronPython.Runtime.PythonDictionary, k: System.Object, v: System.Object, ) -> None:
        ...

    @staticmethod
    def ModuleStarted(context: IronPython.Runtime.CodeContext, features: int, ) -> None:
        ...

    @staticmethod
    def Warn(context: IronPython.Runtime.CodeContext, category: IronPython.Runtime.Types.PythonType, message: str, args: System.Array[System.Object], ) -> None:
        ...

    @staticmethod
    def ShowWarning(context: IronPython.Runtime.CodeContext, category: IronPython.Runtime.Types.PythonType, message: str, filename: str, lineNo: int, ) -> None:
        ...

    @staticmethod
    def FormatWarning(message: str, args: System.Array[System.Object], ) -> str:
        ...

    @staticmethod
    def MakeComboAction(context: IronPython.Runtime.CodeContext, opBinder: System.Dynamic.DynamicMetaObjectBinder, convBinder: System.Dynamic.DynamicMetaObjectBinder, ) -> System.Dynamic.DynamicMetaObjectBinder:
        ...

    @staticmethod
    def MakeInvokeAction(context: IronPython.Runtime.CodeContext, signature: Microsoft.Scripting.Actions.CallSignature, ) -> System.Dynamic.DynamicMetaObjectBinder:
        ...

    @staticmethod
    def MakeGetAction(context: IronPython.Runtime.CodeContext, name: str, isNoThrow: bool, ) -> System.Dynamic.DynamicMetaObjectBinder:
        ...

    @staticmethod
    def MakeCompatGetAction(context: IronPython.Runtime.CodeContext, name: str, ) -> System.Dynamic.DynamicMetaObjectBinder:
        ...

    @staticmethod
    def MakeCompatInvokeAction(context: IronPython.Runtime.CodeContext, callInfo: System.Dynamic.CallInfo, ) -> System.Dynamic.DynamicMetaObjectBinder:
        ...

    @staticmethod
    def MakeCompatConvertAction(context: IronPython.Runtime.CodeContext, toType: System.Type, isExplicit: bool, ) -> System.Dynamic.DynamicMetaObjectBinder:
        ...

    @staticmethod
    def MakeSetAction(context: IronPython.Runtime.CodeContext, name: str, ) -> System.Dynamic.DynamicMetaObjectBinder:
        ...

    @staticmethod
    def MakeDeleteAction(context: IronPython.Runtime.CodeContext, name: str, ) -> System.Dynamic.DynamicMetaObjectBinder:
        ...

    @staticmethod
    def MakeConversionAction(context: IronPython.Runtime.CodeContext, type: System.Type, kind: int, ) -> System.Dynamic.DynamicMetaObjectBinder:
        ...

    @staticmethod
    def MakeTryConversionAction(context: IronPython.Runtime.CodeContext, type: System.Type, kind: int, ) -> System.Dynamic.DynamicMetaObjectBinder:
        ...

    @staticmethod
    def MakeOperationAction(context: IronPython.Runtime.CodeContext, operationName: int, ) -> System.Dynamic.DynamicMetaObjectBinder:
        ...

    @staticmethod
    def MakeUnaryOperationAction(context: IronPython.Runtime.CodeContext, expressionType: int, ) -> System.Dynamic.DynamicMetaObjectBinder:
        ...

    @staticmethod
    def MakeBinaryOperationAction(context: IronPython.Runtime.CodeContext, expressionType: int, ) -> System.Dynamic.DynamicMetaObjectBinder:
        ...

    @staticmethod
    def MakeGetIndexAction(context: IronPython.Runtime.CodeContext, argCount: int, ) -> System.Dynamic.DynamicMetaObjectBinder:
        ...

    @staticmethod
    def MakeSetIndexAction(context: IronPython.Runtime.CodeContext, argCount: int, ) -> System.Dynamic.DynamicMetaObjectBinder:
        ...

    @staticmethod
    def MakeDeleteIndexAction(context: IronPython.Runtime.CodeContext, argCount: int, ) -> System.Dynamic.DynamicMetaObjectBinder:
        ...

    @staticmethod
    def MakeGetSliceBinder(context: IronPython.Runtime.CodeContext, ) -> System.Dynamic.DynamicMetaObjectBinder:
        ...

    @staticmethod
    def MakeSetSliceBinder(context: IronPython.Runtime.CodeContext, ) -> System.Dynamic.DynamicMetaObjectBinder:
        ...

    @staticmethod
    def MakeDeleteSliceBinder(context: IronPython.Runtime.CodeContext, ) -> System.Dynamic.DynamicMetaObjectBinder:
        ...

    @staticmethod
    def DefineDynamicAssembly(name: System.Reflection.AssemblyName, access: int, ) -> System.Reflection.Emit.AssemblyBuilder:
        ...

    @staticmethod
    @typing.overload
    def MakeNewCustomDelegate(types: System.Array[System.Type], ) -> System.Type:
        ...

    @staticmethod
    @typing.overload
    def MakeNewCustomDelegate(types: System.Array[System.Type], callingConvention: System.Nullable[int], ) -> System.Type:
        ...

    @staticmethod
    def InitializeModule(precompiled: System.Reflection.Assembly, main: str, references: System.Array[str], ) -> int:
        ...

    @staticmethod
    @typing.overload
    def InitializeModuleEx(precompiled: System.Reflection.Assembly, main: str, references: System.Array[str], ignoreEnvVars: bool, ) -> int:
        ...

    @staticmethod
    @typing.overload
    def InitializeModuleEx(precompiled: System.Reflection.Assembly, main: str, references: System.Array[str], ignoreEnvVars: bool, options: System.Collections.Generic.Dictionary[str, System.Object], ) -> int:
        ...

    @staticmethod
    def GetPythonTypeContext(pt: IronPython.Runtime.Types.PythonType, ) -> IronPython.Runtime.CodeContext:
        ...

    @staticmethod
    def GetDelegate(context: IronPython.Runtime.CodeContext, target: System.Object, type: System.Type, ) -> System.Delegate:
        ...

    @staticmethod
    def MakeBytes(bytes: System.Array[int], ) -> IronPython.Runtime.Bytes:
        ...

    @staticmethod
    def MakeByteArray(s: str, ) -> System.Array[int]:
        ...

    @staticmethod
    @typing.overload
    def MakeString(bytes: System.Collections.Generic.IList[int], ) -> str:
        ...

    @staticmethod
    @typing.overload
    def MakeString(bytes: System.Collections.Generic.IList[int], maxBytes: int, ) -> str:
        ...

    @staticmethod
    @typing.overload
    def MakeString(bytes: System.Collections.Generic.IList[int], startIdx: int, maxBytes: int, ) -> str:
        ...

    @staticmethod
    @typing.overload
    def MakeString(bytes: System.Span[int], ) -> str:
        ...

    @staticmethod
    @typing.overload
    def MakeString(bytes: System.ReadOnlySpan[int], ) -> str:
        ...

    @staticmethod
    def RemoveName(context: IronPython.Runtime.CodeContext, name: str, ) -> None:
        ...

    @staticmethod
    def LookupName(context: IronPython.Runtime.CodeContext, name: str, ) -> System.Object:
        ...

    @staticmethod
    def LookupLocalName(context: IronPython.Runtime.CodeContext, name: str, defaultValue: System.Object, ) -> System.Object:
        ...

    @staticmethod
    def SetName(context: IronPython.Runtime.CodeContext, name: str, value: System.Object, ) -> System.Object:
        ...

    @staticmethod
    def ToPython(handle: System.IntPtr, ) -> System.Object:
        ...

    @staticmethod
    def CreateLocalContext(outerContext: IronPython.Runtime.CodeContext, boxes: Microsoft.Scripting.MutableTuple, args: System.Array[str], ) -> IronPython.Runtime.CodeContext:
        ...

    @staticmethod
    def GetGlobalContext(context: IronPython.Runtime.CodeContext, ) -> IronPython.Runtime.CodeContext:
        ...

    @staticmethod
    def CheckException(context: IronPython.Runtime.CodeContext, exception: System.Object, test: System.Object, ) -> System.Object:
        ...

    @staticmethod
    @typing.overload
    def CreateTraceBack(pyContext: IronPython.Runtime.PythonContext, e: System.Exception, ) -> IronPython.Runtime.Exceptions.TraceBack:
        ...

    @staticmethod
    @typing.overload
    def CreateTraceBack(e: System.Exception, frames: System.Collections.Generic.IList[Microsoft.Scripting.Runtime.DynamicStackFrame], stacks: System.Collections.Generic.IList[IronPython.Runtime.Operations.FunctionStack], frameCount: int, ) -> IronPython.Runtime.Exceptions.TraceBack:
        ...

    @staticmethod
    def GetExceptionInfo(context: IronPython.Runtime.CodeContext, ) -> IronPython.Runtime.PythonTuple:
        ...

    @staticmethod
    def GetExceptionInfoLocal(context: IronPython.Runtime.CodeContext, ex: System.Exception, ) -> IronPython.Runtime.PythonTuple:
        ...

    @staticmethod
    def MakeRethrownException(context: IronPython.Runtime.CodeContext, ) -> System.Exception:
        ...

    @staticmethod
    def MakeRethrowExceptionWorker(e: System.Exception, ) -> System.Exception:
        ...

    @staticmethod
    def MakeException(context: IronPython.Runtime.CodeContext, exception: System.Object, ) -> System.Exception:
        ...

    @staticmethod
    def MakeExceptionWithCause(context: IronPython.Runtime.CodeContext, exception: System.Object, cause: System.Object, ) -> System.Exception:
        ...

    @staticmethod
    def GetRawContextException() -> IronPython.Runtime.Exceptions.PythonExceptions.BaseException:
        ...

    @staticmethod
    def MakeExceptionForGenerator(context: IronPython.Runtime.CodeContext, type: System.Object, value: System.Object, traceback: System.Object, cause: System.Object, ) -> System.Exception:
        ...

    @staticmethod
    def MakeExceptionWorker(context: IronPython.Runtime.CodeContext, type: System.Object, value: System.Object, traceback: System.Object, cause: System.Object, suppressContext: bool, forRethrow: bool, ) -> System.Exception:
        ...

    @staticmethod
    def CreateThrowable(type: IronPython.Runtime.Types.PythonType, args: System.Array[System.Object], ) -> System.Exception:
        ...

    @staticmethod
    def GetFunctionSignature(function: IronPython.Runtime.PythonFunction, ) -> System.Array[str]:
        ...

    @staticmethod
    def CopyAndVerifyDictionary(function: IronPython.Runtime.PythonFunction, dict: System.Collections.IDictionary, ) -> IronPython.Runtime.PythonDictionary:
        ...

    @staticmethod
    def CopyAndVerifyUserMapping(function: IronPython.Runtime.PythonFunction, dict: System.Object, ) -> IronPython.Runtime.PythonDictionary:
        ...

    @staticmethod
    def UserMappingToPythonDictionary(context: IronPython.Runtime.CodeContext, dict: System.Object, funcName: str, ) -> IronPython.Runtime.PythonDictionary:
        ...

    @staticmethod
    def CopyAndVerifyPythonDictionary(function: IronPython.Runtime.PythonFunction, dict: IronPython.Runtime.PythonDictionary, ) -> IronPython.Runtime.PythonDictionary:
        ...

    @staticmethod
    def ExtractDictionaryArgument(function: IronPython.Runtime.PythonFunction, name: str, argCnt: int, dict: IronPython.Runtime.PythonDictionary, ) -> System.Object:
        ...

    @staticmethod
    def AddDictionaryArgument(function: IronPython.Runtime.PythonFunction, name: str, value: System.Object, dict: IronPython.Runtime.PythonDictionary, ) -> None:
        ...

    @staticmethod
    def VerifyUnduplicatedByPosition(function: IronPython.Runtime.PythonFunction, name: str, position: int, listlen: int, ) -> None:
        ...

    @staticmethod
    def VerifyUnduplicatedByName(function: IronPython.Runtime.PythonFunction, name: str, dict: IronPython.Runtime.PythonDictionary, keywordArg: bool, ) -> None:
        ...

    @staticmethod
    def CopyAndVerifyParamsList(function: IronPython.Runtime.PythonFunction, list: System.Object, ) -> IronPython.Runtime.PythonList:
        ...

    @staticmethod
    def UserMappingToPythonTuple(context: IronPython.Runtime.CodeContext, list: System.Object, funcName: str, ) -> IronPython.Runtime.PythonTuple:
        ...

    @staticmethod
    def GetOrCopyParamsTuple(function: IronPython.Runtime.PythonFunction, input: System.Object, ) -> IronPython.Runtime.PythonTuple:
        ...

    @staticmethod
    def ExtractParamsArgument(function: IronPython.Runtime.PythonFunction, argCnt: int, list: IronPython.Runtime.PythonList, ) -> System.Object:
        ...

    @staticmethod
    def AddParamsArguments(list: IronPython.Runtime.PythonList, args: System.Array[System.Object], ) -> None:
        ...

    @staticmethod
    def ExtractAnyArgument(function: IronPython.Runtime.PythonFunction, name: str, argCnt: int, list: IronPython.Runtime.PythonList, dict: System.Collections.IDictionary, ) -> System.Object:
        ...

    @staticmethod
    def SimpleTypeError(message: str, ) -> Microsoft.Scripting.ArgumentTypeException:
        ...

    @staticmethod
    def GetParamsValueOrDefault(function: IronPython.Runtime.PythonFunction, index: int, extraArgs: IronPython.Runtime.PythonList, ) -> System.Object:
        ...

    @staticmethod
    def GetFunctionParameterValue(function: IronPython.Runtime.PythonFunction, index: int, name: str, extraArgs: IronPython.Runtime.PythonList, dict: IronPython.Runtime.PythonDictionary, ) -> System.Object:
        ...

    @staticmethod
    def GetFunctionKeywordOnlyParameterValue(function: IronPython.Runtime.PythonFunction, name: str, dict: IronPython.Runtime.PythonDictionary, ) -> System.Object:
        ...

    @staticmethod
    def CheckParamsZero(function: IronPython.Runtime.PythonFunction, extraArgs: IronPython.Runtime.PythonList, ) -> None:
        ...

    @staticmethod
    def CheckUserParamsZero(function: IronPython.Runtime.PythonFunction, sequence: System.Object, ) -> None:
        ...

    @staticmethod
    def CheckDictionaryZero(function: IronPython.Runtime.PythonFunction, dict: System.Collections.IDictionary, ) -> None:
        ...

    @staticmethod
    def CheckDictionaryMembers(dict: IronPython.Runtime.PythonDictionary, names: System.Array[str], ) -> bool:
        ...

    @staticmethod
    def PythonFunctionGetMember(function: IronPython.Runtime.PythonFunction, name: str, ) -> System.Object:
        ...

    @staticmethod
    def PythonFunctionSetMember(function: IronPython.Runtime.PythonFunction, name: str, value: System.Object, ) -> System.Object:
        ...

    @staticmethod
    def PythonFunctionDeleteDict() -> None:
        ...

    @staticmethod
    def PythonFunctionDeleteDoc(function: IronPython.Runtime.PythonFunction, ) -> None:
        ...

    @staticmethod
    def PythonFunctionDeleteDefaults(function: IronPython.Runtime.PythonFunction, ) -> None:
        ...

    @staticmethod
    def PythonFunctionDeleteMember(function: IronPython.Runtime.PythonFunction, name: str, ) -> bool:
        ...

    @staticmethod
    def InitializeUserTypeSlots(type: IronPython.Runtime.Types.PythonType, ) -> System.Array[System.Object]:
        ...

    @staticmethod
    def IsClsVisible(context: IronPython.Runtime.CodeContext, ) -> bool:
        ...

    @staticmethod
    def GetInitMember(context: IronPython.Runtime.CodeContext, type: IronPython.Runtime.Types.PythonType, instance: System.Object, ) -> System.Object:
        ...

    @staticmethod
    def GetInitSlotMember(context: IronPython.Runtime.CodeContext, type: IronPython.Runtime.Types.PythonType, slot: IronPython.Runtime.Types.PythonTypeSlot, instance: System.Object, ) -> System.Object:
        ...

    @staticmethod
    def IsNumericObject(value: System.Object, ) -> bool:
        ...

    @staticmethod
    def IsNumericType(t: System.Type, ) -> bool:
        ...

    @staticmethod
    def IsNonExtensibleNumericType(t: System.Type, ) -> bool:
        ...

    @staticmethod
    def MakeBoundEvent(eventObj: IronPython.Runtime.Types.ReflectedEvent, instance: System.Object, type: System.Type, ) -> IronPython.Runtime.Types.ReflectedEvent.BoundEvent:
        ...

    @staticmethod
    def CheckTypeVersion(o: System.Object, version: int, ) -> bool:
        ...

    @staticmethod
    def CheckSpecificTypeVersion(type: IronPython.Runtime.Types.PythonType, version: int, ) -> bool:
        ...

    @staticmethod
    def GetConversionHelper(name: str, resultKind: int, ) -> System.Reflection.MethodInfo:
        ...

    @staticmethod
    def ConvertToPythonPrimitive(value: System.Object, ) -> System.Object:
        ...

    @staticmethod
    def ConvertFloatToComplex(value: System.Object, ) -> System.Object:
        ...

    @staticmethod
    def ConvertIntToBigInt(value: System.Object, ) -> System.Object:
        ...

    @staticmethod
    def ConvertIntToInt32(value: System.Object, ) -> System.Object:
        ...

    @staticmethod
    def CheckingConvertToInt(value: System.Object, ) -> bool:
        ...

    @staticmethod
    def CheckingConvertToFloat(value: System.Object, ) -> bool:
        ...

    @staticmethod
    def CheckingConvertToComplex(value: System.Object, ) -> bool:
        ...

    @staticmethod
    def CheckingConvertToString(value: System.Object, ) -> bool:
        ...

    @staticmethod
    def CheckingConvertToBool(value: System.Object, ) -> bool:
        ...

    @staticmethod
    def NonThrowingConvertToInt(value: System.Object, ) -> System.Object:
        ...

    @staticmethod
    def NonThrowingConvertToFloat(value: System.Object, ) -> System.Object:
        ...

    @staticmethod
    def NonThrowingConvertToComplex(value: System.Object, ) -> System.Object:
        ...

    @staticmethod
    def NonThrowingConvertToString(value: System.Object, ) -> System.Object:
        ...

    @staticmethod
    def NonThrowingConvertToBool(value: System.Object, ) -> System.Object:
        ...

    @staticmethod
    def ThrowingConvertToInt(value: System.Object, ) -> System.Object:
        ...

    @staticmethod
    def ThrowingConvertToFloat(value: System.Object, ) -> System.Object:
        ...

    @staticmethod
    def ThrowingConvertToComplex(value: System.Object, ) -> System.Object:
        ...

    @staticmethod
    def ThrowingConvertToString(value: System.Object, ) -> System.Object:
        ...

    @staticmethod
    def ThrowingConvertToBool(value: System.Object, ) -> bool:
        ...

    @staticmethod
    def SlotTryGetBoundValue(context: IronPython.Runtime.CodeContext, slot: IronPython.Runtime.Types.PythonTypeSlot, instance: System.Object, owner: IronPython.Runtime.Types.PythonType, value: ref[System.Object], ) -> bool:
        ...

    @staticmethod
    def SlotTryGetValue(context: IronPython.Runtime.CodeContext, slot: IronPython.Runtime.Types.PythonTypeSlot, instance: System.Object, owner: IronPython.Runtime.Types.PythonType, value: ref[System.Object], ) -> bool:
        ...

    @staticmethod
    def SlotGetValue(context: IronPython.Runtime.CodeContext, slot: IronPython.Runtime.Types.PythonTypeSlot, instance: System.Object, owner: IronPython.Runtime.Types.PythonType, ) -> System.Object:
        ...

    @staticmethod
    def SlotTrySetValue(context: IronPython.Runtime.CodeContext, slot: IronPython.Runtime.Types.PythonTypeSlot, instance: System.Object, owner: IronPython.Runtime.Types.PythonType, value: System.Object, ) -> bool:
        ...

    @staticmethod
    def SlotSetValue(context: IronPython.Runtime.CodeContext, slot: IronPython.Runtime.Types.PythonTypeSlot, instance: System.Object, owner: IronPython.Runtime.Types.PythonType, value: System.Object, ) -> System.Object:
        ...

    @staticmethod
    def SlotTryDeleteValue(context: IronPython.Runtime.CodeContext, slot: IronPython.Runtime.Types.PythonTypeSlot, instance: System.Object, owner: IronPython.Runtime.Types.PythonType, ) -> bool:
        ...

    @staticmethod
    def MakeBoundBuiltinFunction(function: IronPython.Runtime.Types.BuiltinFunction, target: System.Object, ) -> IronPython.Runtime.Types.BuiltinFunction:
        ...

    @staticmethod
    def GetBuiltinFunctionSelf(function: IronPython.Runtime.Types.BuiltinFunction, ) -> System.Object:
        ...

    @staticmethod
    def TestBoundBuiltinFunction(function: IronPython.Runtime.Types.BuiltinFunction, data: System.Object, ) -> bool:
        ...

    @staticmethod
    def GetBuiltinMethodDescriptorTemplate(descriptor: IronPython.Runtime.Types.BuiltinMethodDescriptor, ) -> IronPython.Runtime.Types.BuiltinFunction:
        ...

    @staticmethod
    def GetTypeVersion(type: IronPython.Runtime.Types.PythonType, ) -> int:
        ...

    @staticmethod
    def TryResolveTypeSlot(context: IronPython.Runtime.CodeContext, type: IronPython.Runtime.Types.PythonType, name: str, slot: ref[IronPython.Runtime.Types.PythonTypeSlot], ) -> bool:
        ...

    @staticmethod
    def GetBoundAttr(context: IronPython.Runtime.CodeContext, o: System.Object, name: str, ) -> System.Object:
        ...

    @staticmethod
    def ObjectSetAttribute(context: IronPython.Runtime.CodeContext, o: System.Object, name: str, value: System.Object, ) -> None:
        ...

    @staticmethod
    def ObjectDeleteAttribute(context: IronPython.Runtime.CodeContext, o: System.Object, name: str, ) -> None:
        ...

    @staticmethod
    def ObjectGetAttribute(context: IronPython.Runtime.CodeContext, o: System.Object, name: str, ) -> System.Object:
        ...

    @staticmethod
    def GetStringMemberList(pyMemList: IronPython.Runtime.IPythonMembersList, ) -> System.Collections.Generic.IList[str]:
        ...

    @staticmethod
    def GetAttrNames(context: IronPython.Runtime.CodeContext, o: System.Object, ) -> System.Collections.Generic.IList[System.Object]:
        ...

    @staticmethod
    def CheckInitializedAttribute(o: System.Object, self: System.Object, name: str, ) -> None:
        ...

    @staticmethod
    def GetUserSlotValue(context: IronPython.Runtime.CodeContext, slot: IronPython.Runtime.Types.PythonTypeUserDescriptorSlot, instance: System.Object, type: IronPython.Runtime.Types.PythonType, ) -> System.Object:
        ...

    @staticmethod
    def GetUserDescriptor(o: System.Object, instance: System.Object, context: System.Object, ) -> System.Object:
        ...

    @staticmethod
    def TrySetUserDescriptor(o: System.Object, instance: System.Object, value: System.Object, ) -> bool:
        ...

    @staticmethod
    def TryDeleteUserDescriptor(o: System.Object, instance: System.Object, ) -> bool:
        ...

    @staticmethod
    @typing.overload
    def Invoke(context: IronPython.Runtime.CodeContext, target: System.Object, name: str, arg0: System.Object, ) -> System.Object:
        ...

    @staticmethod
    @typing.overload
    def Invoke(context: IronPython.Runtime.CodeContext, target: System.Object, name: str, args: System.Array[System.Object], ) -> System.Object:
        ...

    @staticmethod
    def CreateDynamicDelegate(meth: System.Reflection.Emit.DynamicMethod, delegateType: System.Type, target: System.Object, ) -> System.Delegate:
        ...

    @staticmethod
    @typing.overload
    def CheckMath(v: float, ) -> float:
        ...

    @staticmethod
    @typing.overload
    def CheckMath(input: float, output: float, ) -> float:
        ...

    @staticmethod
    @typing.overload
    def CheckMath(in0: float, in1: float, output: float, ) -> float:
        ...

    @staticmethod
    def IsMappingType(context: IronPython.Runtime.CodeContext, o: System.Object, ) -> bool:
        ...

    @staticmethod
    @typing.overload
    def FixSliceIndex(v: int, len: int, ) -> int:
        ...

    @staticmethod
    @typing.overload
    def FixSliceIndex(v: int, len: int, ) -> int:
        ...

    @staticmethod
    @typing.overload
    def GetSliceCount(start: int, stop: int, step: int, ) -> int:
        ...

    @staticmethod
    @typing.overload
    def GetSliceCount(start: int, stop: int, step: int, ) -> int:
        ...

    @staticmethod
    @typing.overload
    def FixSlice(slice: IronPython.Runtime.Slice, length: int, ostart: ref[int], ostop: ref[int], ostep: ref[int], ) -> None:
        ...

    @staticmethod
    @typing.overload
    def FixSlice(length: int, start: System.Nullable[int], stop: System.Nullable[int], step: System.Nullable[int], ostart: ref[int], ostop: ref[int], ostep: ref[int], ocount: ref[int], ) -> None:
        ...

    @staticmethod
    @typing.overload
    def FixSlice(slice: IronPython.Runtime.Slice, length: System.Numerics.BigInteger, ostart: ref[System.Numerics.BigInteger], ostop: ref[System.Numerics.BigInteger], ostep: ref[System.Numerics.BigInteger], ) -> None:
        ...

    @staticmethod
    def TryFixSubsequenceIndices(len: int, start: ref[int], end: ref[int], ) -> bool:
        ...

    @staticmethod
    def FixIndex(v: int, len: int, ) -> int:
        ...

    @staticmethod
    def TryFixIndex(v: int, len: int, res: ref[int], ) -> bool:
        ...

    @staticmethod
    def InitializeForFinalization(context: IronPython.Runtime.CodeContext, newObject: System.Object, ) -> None:
        ...

    @staticmethod
    def MakeClass(funcCode: IronPython.Runtime.FunctionCode, body: System.Func[IronPython.Runtime.CodeContext, IronPython.Runtime.CodeContext], parentContext: IronPython.Runtime.CodeContext, name: str, bases: IronPython.Runtime.PythonTuple, keywords: IronPython.Runtime.PythonDictionary, selfNames: str, ) -> System.Object:
        ...

    @staticmethod
    @typing.overload
    def RaiseAssertionError(context: IronPython.Runtime.CodeContext, ) -> None:
        ...

    @staticmethod
    @typing.overload
    def RaiseAssertionError(context: IronPython.Runtime.CodeContext, msg: System.Object, ) -> None:
        ...

    @staticmethod
    def MakeList(items: System.Array[System.Object], ) -> IronPython.Runtime.PythonList:
        ...

    @staticmethod
    def MakeListNoCopy(items: System.Array[System.Object], ) -> IronPython.Runtime.PythonList:
        ...

    @staticmethod
    def MakeEmptyList() -> IronPython.Runtime.PythonList:
        ...

    @staticmethod
    def MakeTuple(items: System.Array[System.Object], ) -> IronPython.Runtime.PythonTuple:
        ...

    @staticmethod
    def MakeTupleFromSequence(items: System.Object, ) -> IronPython.Runtime.PythonTuple:
        ...

    @staticmethod
    def MakeEmptyTuple() -> IronPython.Runtime.PythonTuple:
        ...

    @staticmethod
    def DictMerge(context: IronPython.Runtime.CodeContext, dict: IronPython.Runtime.PythonDictionary, item: System.Object, ) -> None:
        ...

    @staticmethod
    def DictMergeOne(context: IronPython.Runtime.CodeContext, dict: IronPython.Runtime.PythonDictionary, key: System.Object, value: System.Object, ) -> None:
        ...

    @staticmethod
    def DictUpdate(context: IronPython.Runtime.CodeContext, dict: IronPython.Runtime.PythonDictionary, item: System.Object, ) -> None:
        ...

    @staticmethod
    def ListAppend(list: IronPython.Runtime.PythonList, o: System.Object, ) -> None:
        ...

    @staticmethod
    def ListExtend(list: IronPython.Runtime.PythonList, o: System.Object, ) -> None:
        ...

    @staticmethod
    def ListToTuple(list: IronPython.Runtime.PythonList, ) -> IronPython.Runtime.PythonTuple:
        ...

    @staticmethod
    def SetAdd(set: IronPython.Runtime.SetCollection, o: System.Object, ) -> None:
        ...

    @staticmethod
    def SetUpdate(set: IronPython.Runtime.SetCollection, o: System.Object, ) -> None:
        ...

    @staticmethod
    def GetEnumeratorValues(context: IronPython.Runtime.CodeContext, e: System.Object, expected: int, argcntafter: int, ) -> System.Object:
        ...

    @staticmethod
    def GetEnumeratorValuesNoComplexSets(context: IronPython.Runtime.CodeContext, e: System.Object, expected: int, argcntafter: int, ) -> System.Object:
        ...

    @staticmethod
    def GetEnumeratorValuesFromTuple(pythonTuple: IronPython.Runtime.PythonTuple, expected: int, argcntafter: int, ) -> System.Object:
        ...

    @staticmethod
    def GetEnumeratorValuesFromList(list: IronPython.Runtime.PythonList, expected: int, argcntafter: int, ) -> System.Object:
        ...

    @staticmethod
    def UnpackIterable(context: IronPython.Runtime.CodeContext, e: System.Object, expected: int, argcntafter: int, ) -> System.Object:
        ...

    @staticmethod
    def MakeSlice(start: System.Object, stop: System.Object, step: System.Object, ) -> IronPython.Runtime.Slice:
        ...

    @staticmethod
    def Write(context: IronPython.Runtime.CodeContext, f: System.Object, text: str, ) -> None:
        ...

    @staticmethod
    def ReadLine(context: IronPython.Runtime.CodeContext, f: System.Object, ) -> System.Object:
        ...

    @staticmethod
    def PrintWithDest(context: IronPython.Runtime.CodeContext, dest: System.Object, o: System.Object, noNewLine: bool = ..., flush: bool = ..., ) -> None:
        ...

    @staticmethod
    def ReadLineFromSrc(context: IronPython.Runtime.CodeContext, src: System.Object, ) -> System.Object:
        ...

    @staticmethod
    def PrintNewline(context: IronPython.Runtime.CodeContext, ) -> None:
        ...

    @staticmethod
    def PrintNewlineWithDest(context: IronPython.Runtime.CodeContext, dest: System.Object, ) -> None:
        ...

    @staticmethod
    def PrintExpressionValue(context: IronPython.Runtime.CodeContext, value: System.Object, ) -> None:
        ...

    @staticmethod
    def PrintException(context: IronPython.Runtime.CodeContext, exception: System.Exception, console: System.Object = ..., ) -> None:
        ...

    @staticmethod
    def ImportTop(context: IronPython.Runtime.CodeContext, fullName: str, level: int, ) -> System.Object:
        ...

    @staticmethod
    def ImportBottom(context: IronPython.Runtime.CodeContext, fullName: str, level: int, ) -> System.Object:
        ...

    @staticmethod
    def ImportWithNames(context: IronPython.Runtime.CodeContext, fullName: str, names: System.Array[str], level: int, ) -> System.Object:
        ...

    @staticmethod
    def ImportFrom(context: IronPython.Runtime.CodeContext, module: System.Object, name: str, ) -> System.Object:
        ...

    @staticmethod
    def ImportStar(context: IronPython.Runtime.CodeContext, fullName: str, level: int, ) -> None:
        ...

    @staticmethod
    def GetCollection(o: System.Object, ) -> System.Collections.ICollection:
        ...

    @staticmethod
    @typing.overload
    def GetEnumerator(o: System.Object, ) -> System.Collections.IEnumerator:
        ...

    @staticmethod
    @typing.overload
    def GetEnumerator(context: IronPython.Runtime.CodeContext, o: System.Object, ) -> System.Collections.IEnumerator:
        ...

    @staticmethod
    def TypeErrorForNotAnIterator(enumerable: System.Object, ) -> System.Exception:
        ...

    @staticmethod
    def GetEnumeratorObject(context: IronPython.Runtime.CodeContext, o: System.Object, ) -> System.Object:
        ...

    @staticmethod
    def TryGetEnumeratorObject(context: IronPython.Runtime.CodeContext, o: System.Object, enumerator: ref[System.Object], ) -> bool:
        ...

    @staticmethod
    def TypeErrorForNotIterable(enumerable: System.Object, ) -> System.Exception:
        ...

    @staticmethod
    def ThrowTypeErrorForBadIteration(context: IronPython.Runtime.CodeContext, enumerable: System.Object, ) -> System.Collections.Generic.KeyValuePair[System.Collections.IEnumerator, System.IDisposable]:
        ...

    @staticmethod
    def TryGetEnumerator(context: IronPython.Runtime.CodeContext, enumerable: System.Object, enumerator: ref[System.Collections.IEnumerator], ) -> bool:
        ...

    @staticmethod
    def ForLoopDispose(iteratorInfo: System.Collections.Generic.KeyValuePair[System.Collections.IEnumerator, System.IDisposable], ) -> None:
        ...

    @staticmethod
    def StringEnumerator(str: str, ) -> System.Collections.Generic.KeyValuePair[System.Collections.IEnumerator, System.IDisposable]:
        ...

    @staticmethod
    def BytesEnumerator(bytes: System.Collections.Generic.IList[int], ) -> System.Collections.Generic.KeyValuePair[System.Collections.IEnumerator, System.IDisposable]:
        ...

    @staticmethod
    def GetEnumeratorFromEnumerable(enumerable: System.Collections.IEnumerable, ) -> System.Collections.Generic.KeyValuePair[System.Collections.IEnumerator, System.IDisposable]:
        ...

    @staticmethod
    def StringEnumerable(str: str, ) -> System.Collections.IEnumerable:
        ...

    @staticmethod
    def BytesEnumerable(bytes: System.Collections.Generic.IList[int], ) -> System.Collections.IEnumerable:
        ...

    @staticmethod
    def SetCurrentException(context: IronPython.Runtime.CodeContext, clrException: System.Exception, ) -> System.Object:
        ...

    @staticmethod
    def GetCurrentException() -> System.Exception:
        ...

    @staticmethod
    def ClearCurrentException() -> None:
        ...

    @staticmethod
    def SaveCurrentException() -> System.Exception:
        ...

    @staticmethod
    def RestoreCurrentException(clrException: System.Exception, ) -> None:
        ...

    @staticmethod
    def MakeEmptyDict() -> IronPython.Runtime.PythonDictionary:
        ...

    @staticmethod
    def MakeDictFromItems(data: System.Array[System.Object], ) -> IronPython.Runtime.PythonDictionary:
        ...

    @staticmethod
    def MakeConstantDict(items: System.Object, ) -> IronPython.Runtime.PythonDictionary:
        ...

    @staticmethod
    def MakeConstantDictStorage(data: System.Array[System.Object], ) -> System.Object:
        ...

    @staticmethod
    def MakeSet(items: System.Array[System.Object], ) -> IronPython.Runtime.SetCollection:
        ...

    @staticmethod
    def MakeEmptySet() -> IronPython.Runtime.SetCollection:
        ...

    @staticmethod
    def MakeHomogeneousDictFromItems(data: System.Array[System.Object], ) -> IronPython.Runtime.PythonDictionary:
        ...

    @staticmethod
    def IsCallable(context: IronPython.Runtime.CodeContext, o: System.Object, ) -> bool:
        ...

    @staticmethod
    def UserObjectIsCallable(context: IronPython.Runtime.CodeContext, o: System.Object, ) -> bool:
        ...

    @staticmethod
    def IsTrue(o: System.Object, ) -> bool:
        ...

    @staticmethod
    def GetReprInfinite() -> System.Collections.Generic.List[System.Object]:
        ...

    @staticmethod
    def LookupEncodingError(context: IronPython.Runtime.CodeContext, name: str, ) -> System.Object:
        ...

    @staticmethod
    def RegisterEncodingError(context: IronPython.Runtime.CodeContext, name: str, handler: System.Object, ) -> None:
        ...

    @staticmethod
    def LookupEncoding(context: IronPython.Runtime.CodeContext, encoding: str, ) -> IronPython.Runtime.PythonTuple:
        ...

    @staticmethod
    def LookupTextEncoding(context: IronPython.Runtime.CodeContext, encoding: str, alternateCommand: str, ) -> IronPython.Runtime.PythonTuple:
        ...

    @staticmethod
    def RegisterEncoding(context: IronPython.Runtime.CodeContext, search_function: System.Object, ) -> None:
        ...

    @staticmethod
    def GetPythonTypeName(obj: System.Object, ) -> str:
        ...

    @staticmethod
    def GetPythonTypeNameFromType(type: System.Type, ) -> str:
        ...

    @staticmethod
    def Ascii(context: IronPython.Runtime.CodeContext, o: System.Object, ) -> str:
        ...

    @staticmethod
    def Repr(context: IronPython.Runtime.CodeContext, o: System.Object, ) -> str:
        ...

    @staticmethod
    def Format(context: IronPython.Runtime.CodeContext, argValue: System.Object, formatSpec: str, ) -> str:
        ...

    @staticmethod
    def GetAndCheckInfinite(o: System.Object, ) -> System.Collections.Generic.List[System.Object]:
        ...

    @staticmethod
    @typing.overload
    def ToString(o: System.Object, ) -> str:
        ...

    @staticmethod
    @typing.overload
    def ToString(context: IronPython.Runtime.CodeContext, o: System.Object, ) -> str:
        ...

    @staticmethod
    def FormatString(context: IronPython.Runtime.CodeContext, str: str, data: System.Object, ) -> str:
        ...

    @staticmethod
    def Plus(o: System.Object, ) -> System.Object:
        ...

    @staticmethod
    def Negate(o: System.Object, ) -> System.Object:
        ...

    @staticmethod
    @typing.overload
    def IsSubClass(c: IronPython.Runtime.Types.PythonType, typeinfo: IronPython.Runtime.Types.PythonType, ) -> bool:
        ...

    @staticmethod
    @typing.overload
    def IsSubClass(context: IronPython.Runtime.CodeContext, c: IronPython.Runtime.Types.PythonType, typeinfo: System.Object, ) -> bool:
        ...

    @staticmethod
    @typing.overload
    def IsInstance(o: System.Object, typeinfo: IronPython.Runtime.Types.PythonType, ) -> bool:
        ...

    @staticmethod
    @typing.overload
    def IsInstance(context: IronPython.Runtime.CodeContext, o: System.Object, typeinfo: IronPython.Runtime.PythonTuple, ) -> bool:
        ...

    @staticmethod
    @typing.overload
    def IsInstance(context: IronPython.Runtime.CodeContext, o: System.Object, typeinfo: System.Object, ) -> bool:
        ...

    @staticmethod
    @typing.overload
    def IsInstanceDynamic(o: System.Object, typeinfo: System.Object, ) -> bool:
        ...

    @staticmethod
    @typing.overload
    def IsInstanceDynamic(o: System.Object, typeinfo: System.Object, odt: IronPython.Runtime.Types.PythonType, ) -> bool:
        ...

    @staticmethod
    def IsSubclassSlow(cls: System.Object, typeinfo: System.Object, ) -> bool:
        ...

    @staticmethod
    def OnesComplement(o: System.Object, ) -> System.Object:
        ...

    @staticmethod
    def Not(o: System.Object, ) -> bool:
        ...

    @staticmethod
    def Is(x: System.Object, y: System.Object, ) -> System.Object:
        ...

    @staticmethod
    def IsRetBool(x: System.Object, y: System.Object, ) -> bool:
        ...

    @staticmethod
    def IsNot(x: System.Object, y: System.Object, ) -> System.Object:
        ...

    @staticmethod
    def MultiplySequence(multiplier: IronPython.Runtime.Operations.PythonOps.MultiplySequenceWorker[T], sequence: T, count: IronPython.Runtime.Index, isForward: bool, ) -> System.Object:
        ...

    @staticmethod
    def GetSequenceMultiplier(sequence: System.Object, count: System.Object, ) -> int:
        ...

    @staticmethod
    def Equal(context: IronPython.Runtime.CodeContext, x: System.Object, y: System.Object, ) -> System.Object:
        ...

    @staticmethod
    @typing.overload
    def EqualRetBool(x: System.Object, y: System.Object, ) -> bool:
        ...

    @staticmethod
    @typing.overload
    def EqualRetBool(context: IronPython.Runtime.CodeContext, x: System.Object, y: System.Object, ) -> bool:
        ...

    @staticmethod
    @typing.overload
    def IsOrEqualsRetBool(x: System.Object, y: System.Object, ) -> bool:
        ...

    @staticmethod
    @typing.overload
    def IsOrEqualsRetBool(context: IronPython.Runtime.CodeContext, x: System.Object, y: System.Object, ) -> bool:
        ...

    @staticmethod
    def RichCompare(context: IronPython.Runtime.CodeContext, x: System.Object, y: System.Object, op: int, ) -> System.Object:
        ...

    @staticmethod
    def CompareTypesEqual(context: IronPython.Runtime.CodeContext, x: System.Object, y: System.Object, ) -> bool:
        ...

    @staticmethod
    def CompareTypesNotEqual(context: IronPython.Runtime.CodeContext, x: System.Object, y: System.Object, ) -> bool:
        ...

    @staticmethod
    @typing.overload
    def ArraysEqual(context: IronPython.Runtime.CodeContext, data0: System.ReadOnlySpan[System.Object], data1: System.ReadOnlySpan[System.Object], ) -> bool:
        ...

    @staticmethod
    @typing.overload
    def ArraysEqual(context: IronPython.Runtime.CodeContext, data0: System.ReadOnlySpan[System.Object], data1: System.ReadOnlySpan[System.Object], comparer: System.Collections.IEqualityComparer, ) -> bool:
        ...

    @staticmethod
    def CompareLength(length1: int, length2: int, op: int, ) -> System.Object:
        ...

    @staticmethod
    @typing.overload
    def RichCompareSequences(context: IronPython.Runtime.CodeContext, data0: System.ReadOnlySpan[System.Object], data1: System.ReadOnlySpan[System.Object], op: int, ) -> System.Object:
        ...

    @staticmethod
    @typing.overload
    def RichCompareSequences(context: IronPython.Runtime.CodeContext, data0: System.Collections.Generic.IList[System.Object], data1: System.Collections.Generic.IList[System.Object], op: int, ) -> System.Object:
        ...

    @staticmethod
    @typing.overload
    def ArraysGreaterThan(context: IronPython.Runtime.CodeContext, data0: System.ReadOnlySpan[System.Object], data1: System.ReadOnlySpan[System.Object], ) -> System.Object:
        ...

    @staticmethod
    @typing.overload
    def ArraysGreaterThan(context: IronPython.Runtime.CodeContext, data0: System.Collections.Generic.IList[System.Object], data1: System.Collections.Generic.IList[System.Object], ) -> System.Object:
        ...

    @staticmethod
    @typing.overload
    def ArraysLessThan(context: IronPython.Runtime.CodeContext, data0: System.ReadOnlySpan[System.Object], data1: System.ReadOnlySpan[System.Object], ) -> System.Object:
        ...

    @staticmethod
    @typing.overload
    def ArraysLessThan(context: IronPython.Runtime.CodeContext, data0: System.Collections.Generic.IList[System.Object], data1: System.Collections.Generic.IList[System.Object], ) -> System.Object:
        ...

    @staticmethod
    @typing.overload
    def ArraysGreaterThanOrEqual(context: IronPython.Runtime.CodeContext, data0: System.ReadOnlySpan[System.Object], data1: System.ReadOnlySpan[System.Object], ) -> System.Object:
        ...

    @staticmethod
    @typing.overload
    def ArraysGreaterThanOrEqual(context: IronPython.Runtime.CodeContext, data0: System.Collections.Generic.IList[System.Object], data1: System.Collections.Generic.IList[System.Object], ) -> System.Object:
        ...

    @staticmethod
    @typing.overload
    def ArraysLessThanOrEqual(context: IronPython.Runtime.CodeContext, data0: System.ReadOnlySpan[System.Object], data1: System.ReadOnlySpan[System.Object], ) -> System.Object:
        ...

    @staticmethod
    @typing.overload
    def ArraysLessThanOrEqual(context: IronPython.Runtime.CodeContext, data0: System.Collections.Generic.IList[System.Object], data1: System.Collections.Generic.IList[System.Object], ) -> System.Object:
        ...

    @staticmethod
    def PowerMod(context: IronPython.Runtime.CodeContext, x: System.Object, y: System.Object, z: System.Object, ) -> System.Object:
        ...

    @staticmethod
    def Id(o: System.Object, ) -> int:
        ...

    @staticmethod
    def HexId(o: System.Object, ) -> str:
        ...

    @staticmethod
    def Hash(context: IronPython.Runtime.CodeContext, o: System.Object, ) -> int:
        ...

    @staticmethod
    def Index(o: System.Object, ) -> System.Object:
        ...

    @staticmethod
    @typing.overload
    def TryToIndex(o: System.Object, index: ref[System.Object], ) -> bool:
        ...

    @staticmethod
    @typing.overload
    def TryToIndex(o: System.Object, index: ref[System.Numerics.BigInteger], ) -> bool:
        ...

    @staticmethod
    def IndexObjectToInt(o: System.Object, res: ref[int], longRes: ref[System.Numerics.BigInteger], ) -> bool:
        ...

    @staticmethod
    @typing.overload
    def Length(o: System.Object, res: ref[int], bigRes: ref[System.Numerics.BigInteger], ) -> bool:
        ...

    @staticmethod
    @typing.overload
    def Length(o: System.Object, ) -> int:
        ...

    @staticmethod
    def TryInvokeLengthHint(context: IronPython.Runtime.CodeContext, sequence: System.Object, hint: ref[int], ) -> bool:
        ...

    @staticmethod
    def CallWithContext(context: IronPython.Runtime.CodeContext, func: System.Object, args: System.Array[System.Object], ) -> System.Object:
        ...

    @staticmethod
    def CallWithContextAndThis(context: IronPython.Runtime.CodeContext, func: System.Object, instance: System.Object, args: System.Array[System.Object], ) -> System.Object:
        ...

    @staticmethod
    def CallWithArgsTupleAndKeywordDictAndContext(context: IronPython.Runtime.CodeContext, func: System.Object, args: System.Array[System.Object], names: System.Array[str], argsTuple: System.Object, kwDict: System.Object, ) -> System.Object:
        ...

    @staticmethod
    def CallWithArgsTuple(func: System.Object, args: System.Array[System.Object], argsTuple: System.Object, ) -> System.Object:
        ...

    @staticmethod
    def GetIndex(context: IronPython.Runtime.CodeContext, o: System.Object, index: System.Object, ) -> System.Object:
        ...

    @staticmethod
    @typing.overload
    def TryGetBoundAttr(o: System.Object, name: str, ret: ref[System.Object], ) -> bool:
        ...

    @staticmethod
    @typing.overload
    def TryGetBoundAttr(context: IronPython.Runtime.CodeContext, o: System.Object, name: str, ret: ref[System.Object], ) -> bool:
        ...

    @staticmethod
    def SetAttr(context: IronPython.Runtime.CodeContext, o: System.Object, name: str, value: System.Object, ) -> None:
        ...

    @staticmethod
    def DeleteAttr(context: IronPython.Runtime.CodeContext, o: System.Object, name: str, ) -> None:
        ...

    @staticmethod
    def HasAttr(context: IronPython.Runtime.CodeContext, o: System.Object, name: str, ) -> bool:
        ...

class ComOps(System.Object, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    @staticmethod
    def __str__(self: System.Object, ) -> str:
        ...

    @staticmethod
    def __repr__(self: System.Object, ) -> str:
        ...

class SingleOps(System.Object, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    @staticmethod
    @typing.overload
    def __new__(context: IronPython.Runtime.CodeContext, cls: IronPython.Runtime.Types.PythonType, ) -> System.Object:
        ...

    @staticmethod
    @typing.overload
    def __new__(context: IronPython.Runtime.CodeContext, cls: IronPython.Runtime.Types.PythonType, x: System.Object, ) -> System.Object:
        ...

    @staticmethod
    def __str__(context: IronPython.Runtime.CodeContext, x: float, ) -> str:
        ...

    @staticmethod
    def __repr__(context: IronPython.Runtime.CodeContext, self: float, ) -> str:
        ...

    @staticmethod
    def __format__(context: IronPython.Runtime.CodeContext, self: float, formatSpec: str, ) -> str:
        ...

    @staticmethod
    def __hash__(x: float, ) -> int:
        ...

    @staticmethod
    def __float__(x: float, ) -> float:
        ...

    @staticmethod
    def __bool__(x: float, ) -> bool:
        ...

    @staticmethod
    def __trunc__(x: float, ) -> System.Object:
        ...

    @staticmethod
    def conjugate(x: float, ) -> float:
        ...

class DelegateOps(System.Object, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    @staticmethod
    def __new__(context: IronPython.Runtime.CodeContext, type: IronPython.Runtime.Types.PythonType, function: System.Object, ) -> System.Object:
        ...

    @staticmethod
    def InPlaceAdd(self: System.Delegate, other: System.Delegate, ) -> System.Delegate:
        ...

    @staticmethod
    def InPlaceSubtract(self: System.Delegate, other: System.Delegate, ) -> System.Delegate:
        ...

    @staticmethod
    @typing.overload
    def Call(context: IronPython.Runtime.CodeContext, delegate: System.Delegate, args: System.Array[System.Object], ) -> System.Object:
        ...

    @staticmethod
    @typing.overload
    def Call(context: IronPython.Runtime.CodeContext, delegate: System.Delegate, dict: System.Collections.Generic.IDictionary[System.Object, System.Object], args: System.Array[System.Object], ) -> System.Object:
        ...

class ComplexOps(System.Object, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    @staticmethod
    @typing.overload
    def __new__(context: IronPython.Runtime.CodeContext, cls: IronPython.Runtime.Types.PythonType, ) -> System.Object:
        ...

    @staticmethod
    @typing.overload
    def __new__(context: IronPython.Runtime.CodeContext, cls: IronPython.Runtime.Types.PythonType, real: System.Object, imag: System.Object, ) -> System.Object:
        ...

    @staticmethod
    def Power(x: System.Numerics.Complex, y: System.Numerics.Complex, ) -> System.Numerics.Complex:
        ...

    @staticmethod
    def __hash__(x: System.Numerics.Complex, ) -> int:
        ...

    @staticmethod
    def __bool__(x: System.Numerics.Complex, ) -> bool:
        ...

    @staticmethod
    def conjugate(x: System.Numerics.Complex, ) -> System.Numerics.Complex:
        ...

    @staticmethod
    def __getnewargs__(context: IronPython.Runtime.CodeContext, self: System.Numerics.Complex, ) -> System.Object:
        ...

    @staticmethod
    def __pos__(x: System.Numerics.Complex, ) -> System.Object:
        ...

    @staticmethod
    def __str__(context: IronPython.Runtime.CodeContext, x: System.Numerics.Complex, ) -> str:
        ...

    @staticmethod
    def __repr__(context: IronPython.Runtime.CodeContext, x: System.Numerics.Complex, ) -> str:
        ...

    @staticmethod
    def __format__(context: IronPython.Runtime.CodeContext, self: System.Numerics.Complex, formatSpec: str, ) -> str:
        ...

    @staticmethod
    def __float__(self: System.Numerics.Complex, ) -> float:
        ...

    @staticmethod
    def __int__(self: System.Numerics.Complex, ) -> int:
        ...

    @staticmethod
    def FormatComplexValue(context: IronPython.Runtime.CodeContext, x: float, ) -> str:
        ...

class ListOfTOps(System.Object, abc.ABC, typing.Generic[T]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    @staticmethod
    def __repr__(context: IronPython.Runtime.CodeContext, self: System.Collections.Generic.List[T], ) -> str:
        ...

    @staticmethod
    @typing.overload
    def __getitem__(l: System.Collections.Generic.List[T], index: int, ) -> T:
        ...

    @staticmethod
    @typing.overload
    def __getitem__(l: System.Collections.Generic.List[T], slice: IronPython.Runtime.Slice, ) -> System.Collections.Generic.List[T]:
        ...

class DecimalOps(System.Object, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    @staticmethod
    def __bool__(x: System.Decimal, ) -> bool:
        ...

    @staticmethod
    def __repr__(x: System.Decimal, ) -> str:
        ...

    @staticmethod
    def Compare(x: System.Decimal, y: System.Numerics.BigInteger, ) -> int:
        ...

    @staticmethod
    def __hash__(x: System.Decimal, ) -> int:
        ...

    @staticmethod
    def __format__(context: IronPython.Runtime.CodeContext, self: System.Decimal, formatSpec: str, ) -> str:
        ...

    @staticmethod
    def DecimalToFormatString(context: IronPython.Runtime.CodeContext, self: System.Decimal, spec: IronPython.Runtime.StringFormatSpec, ) -> str:
        ...

class MarshalOps(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    def __init__(self, ):
        ...

    @staticmethod
    def GetBytes(o: System.Object, version: int, ) -> System.Array[int]:
        ...

    @staticmethod
    def GetObject(bytes: System.Collections.Generic.IEnumerator[int], ) -> System.Object:
        ...

class UInt32Ops(System.Object, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    @staticmethod
    @typing.overload
    def __new__(cls: IronPython.Runtime.Types.PythonType, ) -> System.Object:
        ...

    @staticmethod
    @typing.overload
    def __new__(cls: IronPython.Runtime.Types.PythonType, value: System.Object, ) -> System.Object:
        ...

    @staticmethod
    def __bool__(x: int, ) -> bool:
        ...

    @staticmethod
    def __repr__(x: int, ) -> str:
        ...

    @staticmethod
    def __trunc__(x: int, ) -> int:
        ...

    @staticmethod
    def __int__(x: int, ) -> System.Numerics.BigInteger:
        ...

    @staticmethod
    def __index__(x: int, ) -> System.Numerics.BigInteger:
        ...

    @staticmethod
    def __hash__(x: int, ) -> int:
        ...

    @staticmethod
    def conjugate(x: int, ) -> int:
        ...

    @staticmethod
    def bit_length(value: int, ) -> int:
        ...

    @staticmethod
    def to_bytes(value: int, length: int, byteorder: str, signed: bool = ..., ) -> IronPython.Runtime.Bytes:
        ...

class DBNullOps(System.Object, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    @staticmethod
    def __bool__(value: System.DBNull, ) -> bool:
        ...

class ArrayOps(System.Object, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    @staticmethod
    @typing.overload
    def __new__(context: IronPython.Runtime.CodeContext, pythonType: IronPython.Runtime.Types.PythonType, length: int, ) -> System.Object:
        ...

    @staticmethod
    @typing.overload
    def __new__(context: IronPython.Runtime.CodeContext, pythonType: IronPython.Runtime.Types.PythonType, lengths: System.Array[int], ) -> System.Object:
        ...

    @staticmethod
    @typing.overload
    def __new__(context: IronPython.Runtime.CodeContext, pythonType: IronPython.Runtime.Types.PythonType, items: System.Collections.ICollection, ) -> System.Object:
        ...

    @staticmethod
    @typing.overload
    def __new__(context: IronPython.Runtime.CodeContext, pythonType: IronPython.Runtime.Types.PythonType, items: System.Object, ) -> System.Object:
        ...

    @staticmethod
    def __repr__(context: IronPython.Runtime.CodeContext, self: System.Array, ) -> str:
        ...

    @staticmethod
    def Multiply(data: System.Array[System.Object], size: int, count: int, ) -> System.Array[System.Object]:
        ...

    @staticmethod
    def Add(data1: System.Array[System.Object], size1: int, data2: System.Array[System.Object], size2: int, ) -> System.Array[System.Object]:
        ...

    @staticmethod
    @typing.overload
    def GetSlice(data: System.Array[System.Object], start: int, stop: int, ) -> System.Array[System.Object]:
        ...

    @staticmethod
    @typing.overload
    def GetSlice(data: System.Array[System.Object], start: int, stop: int, step: int, ) -> System.Array[System.Object]:
        ...

    @staticmethod
    @typing.overload
    def GetSlice(data: System.Array[System.Object], slice: IronPython.Runtime.Slice, ) -> System.Array[System.Object]:
        ...

    @staticmethod
    @typing.overload
    def GetSlice(data: System.Array, size: int, slice: IronPython.Runtime.Slice, ) -> System.Array:
        ...

    @staticmethod
    def CopyArray(data: System.Array[System.Object], newSize: int, ) -> System.Array[System.Object]:
        ...

    @staticmethod
    def TupleToIndices(a: System.Array, tuple: System.Collections.Generic.IList[System.Object], ) -> System.Array[int]:
        ...

class EnumOps(System.Object, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    @staticmethod
    def __bool__(self: System.Object, ) -> bool:
        ...

    @staticmethod
    def __repr__(self: System.Object, ) -> str:
        ...

class DoubleOps(System.Object, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields
    PositiveZero: float = ...
    NegativeZero: float = ...

    # properties
    # methods
    @staticmethod
    def conjugate(x: float, ) -> float:
        ...

    @staticmethod
    @typing.overload
    def __new__(context: IronPython.Runtime.CodeContext, cls: IronPython.Runtime.Types.PythonType, ) -> System.Object:
        ...

    @staticmethod
    @typing.overload
    def __new__(context: IronPython.Runtime.CodeContext, cls: IronPython.Runtime.Types.PythonType, x: System.Object, ) -> System.Object:
        ...

    @staticmethod
    def NewFloat(context: IronPython.Runtime.CodeContext, type: IronPython.Runtime.Types.PythonType, x: System.Object, ) -> System.Object:
        ...

    @staticmethod
    def TryToFloat(context: IronPython.Runtime.CodeContext, value: System.Object, result: ref[float], ) -> bool:
        ...

    @staticmethod
    def as_integer_ratio(self: float, ) -> IronPython.Runtime.PythonTuple:
        ...

    @staticmethod
    def fromhex(context: IronPython.Runtime.CodeContext, cls: IronPython.Runtime.Types.PythonType, self: str, ) -> System.Object:
        ...

    @staticmethod
    def TryParseSpecialFloat(self: str, ) -> System.Nullable[float]:
        ...

    @staticmethod
    def HexStringOverflow() -> System.Exception:
        ...

    @staticmethod
    def InvalidHexString() -> System.Exception:
        ...

    @staticmethod
    def hex(self: float, ) -> str:
        ...

    @staticmethod
    def is_integer(self: float, ) -> bool:
        ...

    @staticmethod
    def __int__(d: float, ) -> System.Object:
        ...

    @staticmethod
    def __getnewargs__(context: IronPython.Runtime.CodeContext, self: float, ) -> System.Object:
        ...

    @staticmethod
    @typing.overload
    def __str__(context: IronPython.Runtime.CodeContext, x: float, ) -> str:
        ...

    @staticmethod
    @typing.overload
    def __str__(x: float, provider: System.IFormatProvider, ) -> str:
        ...

    @staticmethod
    @typing.overload
    def __str__(x: float, format: str, ) -> str:
        ...

    @staticmethod
    @typing.overload
    def __str__(x: float, format: str, provider: System.IFormatProvider, ) -> str:
        ...

    @staticmethod
    def __hash__(d: float, ) -> int:
        ...

    @staticmethod
    def IsPositiveZero(value: float, ) -> bool:
        ...

    @staticmethod
    def IsNegativeZero(value: float, ) -> bool:
        ...

    @staticmethod
    def Sign(value: float, ) -> int:
        ...

    @staticmethod
    def CopySign(value: float, sign: float, ) -> float:
        ...

    @staticmethod
    @typing.overload
    def Compare(x: float, y: System.Numerics.BigInteger, ) -> int:
        ...

    @staticmethod
    @typing.overload
    def Compare(x: System.Numerics.BigInteger, y: float, ) -> int:
        ...

    @staticmethod
    @typing.overload
    def Compare(x: float, y: System.Decimal, ) -> int:
        ...

    @staticmethod
    def Repr(context: IronPython.Runtime.CodeContext, self: float, trailingZeroAfterWholeFloat: bool, ) -> str:
        ...

    @staticmethod
    def __repr__(context: IronPython.Runtime.CodeContext, self: float, ) -> str:
        ...

    @staticmethod
    def __float__(self: float, ) -> float:
        ...

    @staticmethod
    def __getformat__(context: IronPython.Runtime.CodeContext, typestr: str, ) -> str:
        ...

    @staticmethod
    def __format__(context: IronPython.Runtime.CodeContext, self: float, formatSpec: str, ) -> str:
        ...

    @staticmethod
    def DoubleToFormatString(context: IronPython.Runtime.CodeContext, self: float, spec: IronPython.Runtime.StringFormatSpec, ) -> str:
        ...

    @staticmethod
    def IncludeExponent(self: float, ) -> bool:
        ...

    @staticmethod
    def DefaultFloatFormat() -> str:
        ...

    @staticmethod
    def __setformat__(context: IronPython.Runtime.CodeContext, typestr: str, fmt: str, ) -> None:
        ...

    @staticmethod
    @typing.overload
    def __round__(self: float, ) -> System.Object:
        ...

    @staticmethod
    @typing.overload
    def __round__(self: float, ndigits: int, ) -> float:
        ...

    @staticmethod
    @typing.overload
    def __round__(self: float, ndigits: System.Numerics.BigInteger, ) -> float:
        ...

    @staticmethod
    @typing.overload
    def __round__(self: float, ndigits: System.Object, ) -> float:
        ...

    @staticmethod
    def __bool__(x: float, ) -> bool:
        ...

    @staticmethod
    def __trunc__(x: float, ) -> System.Object:
        ...

class StringOps(System.Object, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def Latin1Encoding(self) -> System.Text.Encoding:
        ...

    # methods
    @staticmethod
    @typing.overload
    def endswith(self: str, suffix: str, start: int, ) -> bool:
        ...

    @staticmethod
    @typing.overload
    def endswith(self: str, suffix: str, start: int, end: int, ) -> bool:
        ...

    @staticmethod
    @typing.overload
    def endswith(self: str, suffix: IronPython.Runtime.PythonTuple, ) -> bool:
        ...

    @staticmethod
    @typing.overload
    def endswith(self: str, suffix: IronPython.Runtime.PythonTuple, start: int, end: int, ) -> bool:
        ...

    @staticmethod
    @typing.overload
    def endswith(self: str, suffix: str, ) -> bool:
        ...

    @staticmethod
    @typing.overload
    def endswith(self: str, suffix: System.Object, ) -> bool:
        ...

    @staticmethod
    @typing.overload
    def endswith(self: str, suffix: System.Object, start: int, ) -> bool:
        ...

    @staticmethod
    @typing.overload
    def endswith(self: str, suffix: System.Object, start: int, end: int, ) -> bool:
        ...

    @staticmethod
    @typing.overload
    def endswith(self: str, suffix: System.Object, start: System.Object, ) -> bool:
        ...

    @staticmethod
    @typing.overload
    def endswith(self: str, suffix: System.Object, start: System.Object, end: System.Object, ) -> bool:
        ...

    @staticmethod
    @typing.overload
    def startswith(self: str, prefix: str, ) -> bool:
        ...

    @staticmethod
    @typing.overload
    def startswith(self: str, prefix: str, start: int, ) -> bool:
        ...

    @staticmethod
    @typing.overload
    def startswith(self: str, prefix: str, start: int, end: int, ) -> bool:
        ...

    @staticmethod
    @typing.overload
    def startswith(self: str, prefix: IronPython.Runtime.PythonTuple, ) -> bool:
        ...

    @staticmethod
    @typing.overload
    def startswith(self: str, prefix: IronPython.Runtime.PythonTuple, start: int, end: int, ) -> bool:
        ...

    @staticmethod
    @typing.overload
    def startswith(self: str, prefix: System.Object, ) -> bool:
        ...

    @staticmethod
    @typing.overload
    def startswith(self: str, prefix: System.Object, start: int, ) -> bool:
        ...

    @staticmethod
    @typing.overload
    def startswith(self: str, prefix: System.Object, start: int, end: int, ) -> bool:
        ...

    @staticmethod
    @typing.overload
    def startswith(self: str, prefix: System.Object, start: System.Object, ) -> bool:
        ...

    @staticmethod
    @typing.overload
    def startswith(self: str, prefix: System.Object, start: System.Object, end: System.Object, ) -> bool:
        ...

    @staticmethod
    def StringEnumerable(str: str, ) -> System.Collections.IEnumerable:
        ...

    @staticmethod
    def StringEnumerator(str: str, ) -> System.Collections.Generic.IEnumerator[str]:
        ...

    @staticmethod
    def StrictErrors(unicodeError: System.Object, ) -> System.Object:
        ...

    @staticmethod
    def IgnoreErrors(unicodeError: System.Object, ) -> System.Object:
        ...

    @staticmethod
    def ReplaceErrors(unicodeError: System.Object, ) -> System.Object:
        ...

    @staticmethod
    def XmlCharRefReplaceErrors(unicodeError: System.Object, ) -> System.Object:
        ...

    @staticmethod
    def BackslashReplaceErrors(unicodeError: System.Object, ) -> System.Object:
        ...

    @staticmethod
    def NameReplaceErrors(unicodeError: System.Object, ) -> System.Object:
        ...

    @staticmethod
    def SurrogateEscapeErrors(unicodeError: System.Object, ) -> System.Object:
        ...

    @staticmethod
    def SurrogatePassErrors(unicodeError: System.Object, ) -> System.Object:
        ...

    @staticmethod
    def SurrogateErrorsImpl(unicodeError: System.Object, decodeFallback: IronPython.Runtime.Operations.StringOps.DecodeErrorHandler, encodeFallback: IronPython.Runtime.Operations.StringOps.EncodeErrorHandler, ) -> System.Object:
        ...

    @staticmethod
    def IdentifyUtfEncoding(encodingName: str, charWidth: ref[int], isBigEndian: ref[bool], ) -> None:
        ...

    @staticmethod
    @typing.overload
    def rindex(self: str, sub: str, start: System.Object, ) -> int:
        ...

    @staticmethod
    @typing.overload
    def rindex(self: str, sub: str, start: System.Object, end: System.Object, ) -> int:
        ...

    @staticmethod
    @typing.overload
    def rindex(self: str, sub: str, ) -> int:
        ...

    @staticmethod
    @typing.overload
    def rindex(self: str, sub: str, start: int, ) -> int:
        ...

    @staticmethod
    @typing.overload
    def rindex(self: str, sub: str, start: int, end: int, ) -> int:
        ...

    @staticmethod
    @typing.overload
    def rjust(self: str, width: int, ) -> str:
        ...

    @staticmethod
    @typing.overload
    def rjust(self: str, width: int, fillchar: str, ) -> str:
        ...

    @staticmethod
    def rpartition(self: str, sep: str, ) -> IronPython.Runtime.PythonTuple:
        ...

    @staticmethod
    def rsplit(self: str, sep: str = ..., maxsplit: int = ..., ) -> IronPython.Runtime.PythonList:
        ...

    @staticmethod
    @typing.overload
    def rstrip(self: str, ) -> str:
        ...

    @staticmethod
    @typing.overload
    def rstrip(self: str, chars: str, ) -> str:
        ...

    @staticmethod
    def split(self: str, sep: str = ..., maxsplit: int = ..., ) -> IronPython.Runtime.PythonList:
        ...

    @staticmethod
    @typing.overload
    def splitlines(self: str, ) -> IronPython.Runtime.PythonList:
        ...

    @staticmethod
    @typing.overload
    def splitlines(self: str, keepends: bool, ) -> IronPython.Runtime.PythonList:
        ...

    @staticmethod
    @typing.overload
    def strip(self: str, ) -> str:
        ...

    @staticmethod
    @typing.overload
    def strip(self: str, chars: str, ) -> str:
        ...

    @staticmethod
    def swapcase(self: str, ) -> str:
        ...

    @staticmethod
    def title(self: str, ) -> str:
        ...

    @staticmethod
    @typing.overload
    def translate(self: str, table: IronPython.Runtime.PythonDictionary, ) -> str:
        ...

    @staticmethod
    @typing.overload
    def translate(self: str, table: str, ) -> str:
        ...

    @staticmethod
    @typing.overload
    def translate(context: IronPython.Runtime.CodeContext, self: str, table: System.Object, ) -> str:
        ...

    @staticmethod
    def AppendValueForTranslate(ret: System.Text.StringBuilder, mapped: System.Object, ) -> None:
        ...

    @staticmethod
    def upper(self: str, ) -> str:
        ...

    @staticmethod
    def zfill(self: str, width: int, ) -> str:
        ...

    @staticmethod
    @typing.overload
    def format(context: IronPython.Runtime.CodeContext, format_string: str, args: System.Array[System.Object], ) -> str:
        ...

    @staticmethod
    @typing.overload
    def format(context: IronPython.Runtime.CodeContext, format_stringø: str, kwargsø: System.Collections.Generic.IDictionary[System.Object, System.Object], argsø: System.Array[System.Object], ) -> str:
        ...

    @staticmethod
    def format_map(context: IronPython.Runtime.CodeContext, self: str, mapping: System.Collections.Generic.IDictionary[System.Object, System.Object], ) -> str:
        ...

    @staticmethod
    def __getnewargs__(context: IronPython.Runtime.CodeContext, self: str, ) -> System.Object:
        ...

    @staticmethod
    @typing.overload
    def __str__(self: str, ) -> str:
        ...

    @staticmethod
    @typing.overload
    def __str__(self: IronPython.Runtime.Operations.ExtensibleString, ) -> str:
        ...

    @staticmethod
    def __repr__(self: str, ) -> str:
        ...

    @staticmethod
    def Quote(s: str, ) -> str:
        ...

    @staticmethod
    def TryGetEncoding(name: str, encoding: ref[System.Text.Encoding], ) -> bool:
        ...

    @staticmethod
    def TryGetNonaliasedEncoding(name: str, encoding: ref[System.Text.Encoding], ) -> bool:
        ...

    @staticmethod
    def ConvertForJoin(value: System.Object, index: int, ) -> str:
        ...

    @staticmethod
    def ReplaceEmpty(self: str, new: str, count: int, ) -> str:
        ...

    @staticmethod
    def Reverse(s: str, ) -> str:
        ...

    @staticmethod
    def AsciiEncode(s: str, ) -> str:
        ...

    @staticmethod
    @typing.overload
    def ReprEncode(s: str, quote: str, ) -> str:
        ...

    @staticmethod
    @typing.overload
    def ReprEncode(s: str, start: int, count: int, isUniEscape: bool, quote: str = ..., ) -> str:
        ...

    @staticmethod
    def RawUnicodeEscapeEncode(s: str, start: int, count: int, escapeAscii: bool = ..., ) -> str:
        ...

    @staticmethod
    def StringBuilderInit(sb: ref[System.Text.StringBuilder], s: str, start: int, end: int, ) -> None:
        ...

    @staticmethod
    def IsSign(ch: str, ) -> bool:
        ...

    @staticmethod
    def GetEncodingName(encoding: System.Text.Encoding, normalize: bool = ..., defaultName: str = ..., ) -> str:
        ...

    @staticmethod
    def NormalizeEncodingName(name: str, ) -> str:
        ...

    @staticmethod
    def RenormalizeEncodingName(name: str, ) -> str:
        ...

    @staticmethod
    def RawDecode(context: IronPython.Runtime.CodeContext, data: IronPython.Runtime.IBufferProtocol, encoding: str, errors: str, ) -> str:
        ...

    @staticmethod
    def DoDecode(context: IronPython.Runtime.CodeContext, buffer: IronPython.Runtime.IPythonBuffer, errors: str, encoding: str, e: System.Text.Encoding, numBytes: int = ..., ) -> str:
        ...

    @staticmethod
    def GetStartingOffset(bytes: System.ReadOnlySpan[int], e: System.Text.Encoding, ) -> int:
        ...

    @staticmethod
    def RawEncode(context: IronPython.Runtime.CodeContext, s: str, encoding: str, errors: str, ) -> IronPython.Runtime.Bytes:
        ...

    @staticmethod
    def DoEncodeAscii(s: str, ) -> IronPython.Runtime.Bytes:
        ...

    @staticmethod
    def TryEncodeAscii(s: str, b: ref[IronPython.Runtime.Bytes], ) -> bool:
        ...

    @staticmethod
    def DoEncodeUtf8(context: IronPython.Runtime.CodeContext, s: str, ) -> IronPython.Runtime.Bytes:
        ...

    @staticmethod
    def DoEncode(context: IronPython.Runtime.CodeContext, s: str, errors: str, encoding: str, e: System.Text.Encoding, includePreamble: bool, ) -> IronPython.Runtime.Bytes:
        ...

    @staticmethod
    def CallUserDecodeOrEncode(context: IronPython.Runtime.CodeContext, function: System.Object, data: System.Object, errors: str, ) -> IronPython.Runtime.PythonTuple:
        ...

    @staticmethod
    def UserEncode(context: IronPython.Runtime.CodeContext, encoding: str, codecInfo: IronPython.Runtime.PythonTuple, data: str, errors: str, ) -> IronPython.Runtime.Bytes:
        ...

    @staticmethod
    def UserDecode(context: IronPython.Runtime.CodeContext, codecInfo: IronPython.Runtime.PythonTuple, data: System.Object, errors: str, ) -> str:
        ...

    @staticmethod
    def SplitEmptyString(separators: bool, ) -> IronPython.Runtime.PythonList:
        ...

    @staticmethod
    @typing.overload
    def SplitInternal(self: str, seps: System.Array[str], maxsplit: int, ) -> IronPython.Runtime.PythonList:
        ...

    @staticmethod
    @typing.overload
    def SplitInternal(self: str, separator: str, maxsplit: int, ) -> IronPython.Runtime.PythonList:
        ...

    @staticmethod
    def AssertStringOrTuple(prefix: System.Object, ) -> None:
        ...

    @staticmethod
    def GetString(obj: System.Object, ) -> str:
        ...

    @staticmethod
    def FastNew(context: IronPython.Runtime.CodeContext, x: System.Object, ) -> System.Object:
        ...

    @staticmethod
    @typing.overload
    def __new__(context: IronPython.Runtime.CodeContext, cls: IronPython.Runtime.Types.PythonType, ) -> System.Object:
        ...

    @staticmethod
    @typing.overload
    def __new__(context: IronPython.Runtime.CodeContext, cls: IronPython.Runtime.Types.PythonType, object: System.Object, ) -> System.Object:
        ...

    @staticmethod
    @typing.overload
    def __new__(context: IronPython.Runtime.CodeContext, cls: IronPython.Runtime.Types.PythonType, object: str, ) -> System.Object:
        ...

    @staticmethod
    @typing.overload
    def __new__(context: IronPython.Runtime.CodeContext, cls: IronPython.Runtime.Types.PythonType, object: IronPython.Runtime.Operations.ExtensibleString, ) -> System.Object:
        ...

    @staticmethod
    @typing.overload
    def __new__(context: IronPython.Runtime.CodeContext, cls: IronPython.Runtime.Types.PythonType, object: str, ) -> System.Object:
        ...

    @staticmethod
    @typing.overload
    def __new__(context: IronPython.Runtime.CodeContext, cls: IronPython.Runtime.Types.PythonType, object: System.Numerics.BigInteger, ) -> System.Object:
        ...

    @staticmethod
    @typing.overload
    def __new__(context: IronPython.Runtime.CodeContext, cls: IronPython.Runtime.Types.PythonType, object: Microsoft.Scripting.Runtime.Extensible[System.Numerics.BigInteger], ) -> System.Object:
        ...

    @staticmethod
    @typing.overload
    def __new__(context: IronPython.Runtime.CodeContext, cls: IronPython.Runtime.Types.PythonType, object: int, ) -> System.Object:
        ...

    @staticmethod
    @typing.overload
    def __new__(context: IronPython.Runtime.CodeContext, cls: IronPython.Runtime.Types.PythonType, object: bool, ) -> System.Object:
        ...

    @staticmethod
    @typing.overload
    def __new__(context: IronPython.Runtime.CodeContext, cls: IronPython.Runtime.Types.PythonType, object: float, ) -> System.Object:
        ...

    @staticmethod
    @typing.overload
    def __new__(context: IronPython.Runtime.CodeContext, cls: IronPython.Runtime.Types.PythonType, object: Microsoft.Scripting.Runtime.Extensible[float], ) -> System.Object:
        ...

    @staticmethod
    @typing.overload
    def __new__(context: IronPython.Runtime.CodeContext, cls: IronPython.Runtime.Types.PythonType, object: float, ) -> System.Object:
        ...

    @staticmethod
    @typing.overload
    def __new__(context: IronPython.Runtime.CodeContext, cls: IronPython.Runtime.Types.PythonType, object: IronPython.Runtime.IBufferProtocol, encoding: str = ..., errors: str = ..., ) -> System.Object:
        ...

    @staticmethod
    @typing.overload
    def __contains__(s: str, item: str, ) -> bool:
        ...

    @staticmethod
    @typing.overload
    def __contains__(s: str, item: str, ) -> bool:
        ...

    @staticmethod
    def __format__(context: IronPython.Runtime.CodeContext, self: str, formatSpec: str, ) -> str:
        ...

    @staticmethod
    def __iter__(s: str, ) -> System.Collections.Generic.IEnumerator[str]:
        ...

    @staticmethod
    def __len__(s: str, ) -> int:
        ...

    @staticmethod
    def capitalize(self: str, ) -> str:
        ...

    @staticmethod
    @typing.overload
    def center(self: str, width: int, ) -> str:
        ...

    @staticmethod
    @typing.overload
    def center(self: str, width: int, fillchar: str, ) -> str:
        ...

    @staticmethod
    @typing.overload
    def count(self: str, sub: str, ) -> int:
        ...

    @staticmethod
    @typing.overload
    def count(self: str, sub: str, start: int, ) -> int:
        ...

    @staticmethod
    @typing.overload
    def count(self: str, sub: str, start: int, end: int, ) -> int:
        ...

    @staticmethod
    @typing.overload
    def count(self: str, sub: str, start: System.Object, ) -> int:
        ...

    @staticmethod
    @typing.overload
    def count(self: str, sub: str, start: System.Object, end: System.Object, ) -> int:
        ...

    @staticmethod
    @typing.overload
    def encode(context: IronPython.Runtime.CodeContext, s: str, encoding: str = ..., errors: str = ..., ) -> IronPython.Runtime.Bytes:
        ...

    @staticmethod
    @typing.overload
    def encode(context: IronPython.Runtime.CodeContext, s: str, encoding: System.Text.Encoding, errors: str = ..., ) -> IronPython.Runtime.Bytes:
        ...

    @staticmethod
    def CastString(o: System.Object, ) -> str:
        ...

    @staticmethod
    def AsString(o: System.Object, ) -> str:
        ...

    @staticmethod
    @typing.overload
    def expandtabs(self: str, ) -> str:
        ...

    @staticmethod
    @typing.overload
    def expandtabs(self: str, tabsize: int, ) -> str:
        ...

    @staticmethod
    @typing.overload
    def find(self: str, sub: str, ) -> int:
        ...

    @staticmethod
    @typing.overload
    def find(self: str, sub: str, start: int, ) -> int:
        ...

    @staticmethod
    @typing.overload
    def find(self: str, sub: str, start: int, end: int, ) -> int:
        ...

    @staticmethod
    @typing.overload
    def find(self: str, sub: str, start: System.Object, ) -> int:
        ...

    @staticmethod
    @typing.overload
    def find(self: str, sub: str, start: System.Object, end: System.Object, ) -> int:
        ...

    @staticmethod
    @typing.overload
    def index(self: str, sub: str, ) -> int:
        ...

    @staticmethod
    @typing.overload
    def index(self: str, sub: str, start: int, ) -> int:
        ...

    @staticmethod
    @typing.overload
    def index(self: str, sub: str, start: int, end: int, ) -> int:
        ...

    @staticmethod
    @typing.overload
    def index(self: str, sub: str, start: System.Object, ) -> int:
        ...

    @staticmethod
    @typing.overload
    def index(self: str, sub: str, start: System.Object, end: System.Object, ) -> int:
        ...

    @staticmethod
    def isalnum(self: str, ) -> bool:
        ...

    @staticmethod
    def isalpha(self: str, ) -> bool:
        ...

    @staticmethod
    def isdigit(self: str, ) -> bool:
        ...

    @staticmethod
    def isidentifier(self: str, ) -> bool:
        ...

    @staticmethod
    def IsPrintable(c: str, ) -> bool:
        ...

    @staticmethod
    def isprintable(self: str, ) -> bool:
        ...

    @staticmethod
    def isspace(self: str, ) -> bool:
        ...

    @staticmethod
    def isdecimal(self: str, ) -> bool:
        ...

    @staticmethod
    def isnumeric(self: str, ) -> bool:
        ...

    @staticmethod
    def islower(self: str, ) -> bool:
        ...

    @staticmethod
    def isupper(self: str, ) -> bool:
        ...

    @staticmethod
    def istitle(self: str, ) -> bool:
        ...

    @staticmethod
    @typing.overload
    def join(self: str, sequence: System.Object, ) -> str:
        ...

    @staticmethod
    @typing.overload
    def join(self: str, sequence: IronPython.Runtime.PythonList, ) -> str:
        ...

    @staticmethod
    @typing.overload
    def ljust(self: str, width: int, ) -> str:
        ...

    @staticmethod
    @typing.overload
    def ljust(self: str, width: int, fillchar: str, ) -> str:
        ...

    @staticmethod
    def lower(self: str, ) -> str:
        ...

    @staticmethod
    def ToLowerAsciiTriggered(self: str, ) -> str:
        ...

    @staticmethod
    @typing.overload
    def lstrip(self: str, ) -> str:
        ...

    @staticmethod
    @typing.overload
    def lstrip(self: str, chars: str, ) -> str:
        ...

    @staticmethod
    @typing.overload
    def maketrans(from_: str, to: str, ) -> IronPython.Runtime.PythonDictionary:
        ...

    @staticmethod
    @typing.overload
    def maketrans(x: str, y: str, z: str, ) -> IronPython.Runtime.PythonDictionary:
        ...

    @staticmethod
    def partition(self: str, sep: str, ) -> IronPython.Runtime.PythonTuple:
        ...

    @staticmethod
    @typing.overload
    def replace(self: str, old: str, new: str, ) -> str:
        ...

    @staticmethod
    @typing.overload
    def replace(self: str, old: str, new: str, count: int, ) -> str:
        ...

    @staticmethod
    @typing.overload
    def rfind(self: str, sub: str, ) -> int:
        ...

    @staticmethod
    @typing.overload
    def rfind(self: str, sub: str, start: int, ) -> int:
        ...

    @staticmethod
    @typing.overload
    def rfind(self: str, sub: str, start: int, end: int, ) -> int:
        ...

    @staticmethod
    @typing.overload
    def rfind(self: str, sub: str, start: System.Object, ) -> int:
        ...

    @staticmethod
    @typing.overload
    def rfind(self: str, sub: str, start: System.Object, end: System.Object, ) -> int:
        ...

class TypeGroupOps(System.Object, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    @staticmethod
    def __repr__(self: Microsoft.Scripting.Actions.TypeGroup, ) -> str:
        ...

    @staticmethod
    def GetItemHelper(self: Microsoft.Scripting.Actions.TypeGroup, types: System.Array[IronPython.Runtime.Types.PythonType], ) -> IronPython.Runtime.Types.PythonType:
        ...

class TypeTrackerOps(System.Object, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
class BoolOps(System.Object, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    @staticmethod
    @typing.overload
    def __new__(cls: System.Object, ) -> System.Object:
        ...

    @staticmethod
    @typing.overload
    def __new__(cls: System.Object, o: System.Object, ) -> bool:
        ...

    @staticmethod
    def __repr__(self: bool, ) -> str:
        ...

    @staticmethod
    def __format__(context: IronPython.Runtime.CodeContext, self: bool, formatSpec: str, ) -> str:
        ...

    @staticmethod
    def __int__(x: bool, ) -> int:
        ...

class Int64Ops(System.Object, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    @staticmethod
    def to_bytes(value: int, length: int, byteorder: str, signed: bool = ..., ) -> IronPython.Runtime.Bytes:
        ...

    @staticmethod
    @typing.overload
    def __new__(cls: IronPython.Runtime.Types.PythonType, ) -> System.Object:
        ...

    @staticmethod
    @typing.overload
    def __new__(cls: IronPython.Runtime.Types.PythonType, value: System.Object, ) -> System.Object:
        ...

    @staticmethod
    def __bool__(x: int, ) -> bool:
        ...

    @staticmethod
    def __repr__(x: int, ) -> str:
        ...

    @staticmethod
    def __trunc__(x: int, ) -> int:
        ...

    @staticmethod
    def __int__(x: int, ) -> System.Numerics.BigInteger:
        ...

    @staticmethod
    def __index__(x: int, ) -> System.Numerics.BigInteger:
        ...

    @staticmethod
    def __hash__(x: int, ) -> int:
        ...

    @staticmethod
    def conjugate(x: int, ) -> int:
        ...

    @staticmethod
    def bit_length(value: int, ) -> int:
        ...

class ExtensibleString(IronPython.Runtime.ICodeFormattable, System.Collections.IStructuralEquatable, Microsoft.Scripting.Runtime.Extensible[str]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def Item(self) -> System.Object:
        ...

    @property
    def Item(self) -> System.Object:
        ...

    @property
    def Value(self) -> str:
        ...

    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def __init__(self, self: str, ):
        ...

    def ToString(self, ) -> str:
        ...

    def __repr__(self, context: IronPython.Runtime.CodeContext, ) -> str:
        ...

    def __eq__(self, other: System.Object, ) -> System.Object:
        ...

    def __ne__(self, other: System.Object, ) -> System.Object:
        ...

    def GetHashCode(self, comparer: System.Collections.IEqualityComparer, ) -> int:
        ...

    def Equals(self, other: System.Object, comparer: System.Collections.IEqualityComparer, ) -> bool:
        ...

    @typing.overload
    def EqualsWorker(self, other: System.Object, ) -> bool:
        ...

    @typing.overload
    def EqualsWorker(self, other: str, comparer: System.Collections.IEqualityComparer, ) -> bool:
        ...

    def __len__(self, ) -> int:
        ...

    def __contains__(self, value: System.Object, ) -> bool:
        ...

class UserTypeDebugView(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def __class__(self) -> IronPython.Runtime.Types.PythonType:
        ...

    @property
    def Members(self) -> System.Collections.Generic.List[IronPython.Runtime.ObjectDebugView]:
        ...

    # methods
    def __init__(self, userObject: IronPython.Runtime.Types.IPythonObject, ):
        ...

class DictionaryOfTOps(System.Object, abc.ABC, typing.Generic[K, V]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    @staticmethod
    def __repr__(context: IronPython.Runtime.CodeContext, self: System.Collections.Generic.Dictionary[K, V], ) -> str:
        ...

class Int16Ops(System.Object, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    @staticmethod
    @typing.overload
    def __new__(cls: IronPython.Runtime.Types.PythonType, ) -> System.Object:
        ...

    @staticmethod
    @typing.overload
    def __new__(cls: IronPython.Runtime.Types.PythonType, value: System.Object, ) -> System.Object:
        ...

    @staticmethod
    def __bool__(x: int, ) -> bool:
        ...

    @staticmethod
    def __repr__(x: int, ) -> str:
        ...

    @staticmethod
    def __trunc__(x: int, ) -> int:
        ...

    @staticmethod
    def __int__(x: int, ) -> int:
        ...

    @staticmethod
    def __index__(x: int, ) -> int:
        ...

    @staticmethod
    def __hash__(x: int, ) -> int:
        ...

    @staticmethod
    def conjugate(x: int, ) -> int:
        ...

    @staticmethod
    def bit_length(value: int, ) -> int:
        ...

    @staticmethod
    def to_bytes(value: int, length: int, byteorder: str, signed: bool = ..., ) -> IronPython.Runtime.Bytes:
        ...

class PythonAssemblyOps(System.Object, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    @staticmethod
    def GetAssemblyMap(context: IronPython.Runtime.PythonContext, ) -> System.Collections.Generic.Dictionary[System.Reflection.Assembly, Microsoft.Scripting.Actions.TopNamespaceTracker]:
        ...

    @staticmethod
    def __repr__(self: System.Reflection.Assembly, ) -> System.Object:
        ...

    @staticmethod
    def GetReflectedAssembly(context: IronPython.Runtime.CodeContext, assem: System.Reflection.Assembly, ) -> Microsoft.Scripting.Actions.TopNamespaceTracker:
        ...

class PythonCalls(System.Object, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    @staticmethod
    @typing.overload
    def Call(func: System.Object, args: System.Array[System.Object], ) -> System.Object:
        ...

    @staticmethod
    @typing.overload
    def Call(context: IronPython.Runtime.CodeContext, func: System.Object, ) -> System.Object:
        ...

    @staticmethod
    @typing.overload
    def Call(context: IronPython.Runtime.CodeContext, func: System.Object, arg0: System.Object, ) -> System.Object:
        ...

    @staticmethod
    @typing.overload
    def Call(context: IronPython.Runtime.CodeContext, func: System.Object, arg0: System.Object, arg1: System.Object, ) -> System.Object:
        ...

    @staticmethod
    @typing.overload
    def Call(context: IronPython.Runtime.CodeContext, func: System.Object, args: System.Array[System.Object], ) -> System.Object:
        ...

    @staticmethod
    @typing.overload
    def CallWithKeywordArgs(context: IronPython.Runtime.CodeContext, func: System.Object, args: System.Array[System.Object], names: System.Array[str], ) -> System.Object:
        ...

    @staticmethod
    @typing.overload
    def CallWithKeywordArgs(context: IronPython.Runtime.CodeContext, func: System.Object, args: System.Array[System.Object], dict: System.Collections.Generic.IDictionary[System.Object, System.Object], ) -> System.Object:
        ...

class SByteOps(System.Object, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    @staticmethod
    @typing.overload
    def __new__(cls: IronPython.Runtime.Types.PythonType, ) -> System.Object:
        ...

    @staticmethod
    @typing.overload
    def __new__(cls: IronPython.Runtime.Types.PythonType, value: System.Object, ) -> System.Object:
        ...

    @staticmethod
    def __bool__(x: int, ) -> bool:
        ...

    @staticmethod
    def __repr__(x: int, ) -> str:
        ...

    @staticmethod
    def __trunc__(x: int, ) -> int:
        ...

    @staticmethod
    def __int__(x: int, ) -> int:
        ...

    @staticmethod
    def __index__(x: int, ) -> int:
        ...

    @staticmethod
    def __hash__(x: int, ) -> int:
        ...

    @staticmethod
    def conjugate(x: int, ) -> int:
        ...

    @staticmethod
    def bit_length(value: int, ) -> int:
        ...

    @staticmethod
    def to_bytes(value: int, length: int, byteorder: str, signed: bool = ..., ) -> IronPython.Runtime.Bytes:
        ...

class CustomTypeDescHelpers(System.Object, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    @staticmethod
    def GetAttributes(self: System.Object, ) -> System.ComponentModel.AttributeCollection:
        ...

    @staticmethod
    def GetClassName(self: System.Object, ) -> str:
        ...

    @staticmethod
    def GetComponentName(self: System.Object, ) -> str:
        ...

    @staticmethod
    def GetConverter(self: System.Object, ) -> System.ComponentModel.TypeConverter:
        ...

    @staticmethod
    def GetDefaultEvent(self: System.Object, ) -> System.ComponentModel.EventDescriptor:
        ...

    @staticmethod
    def GetDefaultProperty(self: System.Object, ) -> System.ComponentModel.PropertyDescriptor:
        ...

    @staticmethod
    def GetEditor(self: System.Object, editorBaseType: System.Type, ) -> System.Object:
        ...

    @staticmethod
    @typing.overload
    def GetEvents(self: System.Object, attributes: System.Array[System.Attribute], ) -> System.ComponentModel.EventDescriptorCollection:
        ...

    @staticmethod
    @typing.overload
    def GetEvents(self: System.Object, ) -> System.ComponentModel.EventDescriptorCollection:
        ...

    @staticmethod
    @typing.overload
    def GetProperties(self: System.Object, ) -> System.ComponentModel.PropertyDescriptorCollection:
        ...

    @staticmethod
    @typing.overload
    def GetProperties(self: System.Object, attributes: System.Array[System.Attribute], ) -> System.ComponentModel.PropertyDescriptorCollection:
        ...

    @staticmethod
    def GetPropertiesImpl(self: System.Object, attributes: System.Array[System.Attribute], ) -> System.Array[System.ComponentModel.PropertyDescriptor]:
        ...

    @staticmethod
    def ShouldIncludeInstanceMember(memberName: str, attributes: System.Array[System.Attribute], ) -> bool:
        ...

    @staticmethod
    def ShouldIncludeProperty(attrSlot: IronPython.Runtime.Types.PythonTypeSlot, attributes: System.Array[System.Attribute], ) -> bool:
        ...

    @staticmethod
    def GetPropertyOwner(self: System.Object, pd: System.ComponentModel.PropertyDescriptor, ) -> System.Object:
        ...

class ByteOps(System.Object, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    @staticmethod
    def bit_length(value: int, ) -> int:
        ...

    @staticmethod
    def to_bytes(value: int, length: int, byteorder: str, signed: bool = ..., ) -> IronPython.Runtime.Bytes:
        ...

    @staticmethod
    @typing.overload
    def ToByteChecked(item: int, ) -> int:
        ...

    @staticmethod
    @typing.overload
    def ToByteChecked(item: System.Numerics.BigInteger, ) -> int:
        ...

    @staticmethod
    @typing.overload
    def ToByteChecked(item: float, ) -> int:
        ...

    @staticmethod
    def IsSign(ch: int, ) -> bool:
        ...

    @staticmethod
    def ToUpper(p: int, ) -> int:
        ...

    @staticmethod
    def ToLower(p: int, ) -> int:
        ...

    @staticmethod
    def IsLower(p: int, ) -> bool:
        ...

    @staticmethod
    def IsUpper(p: int, ) -> bool:
        ...

    @staticmethod
    def IsDigit(b: int, ) -> bool:
        ...

    @staticmethod
    def IsLetter(b: int, ) -> bool:
        ...

    @staticmethod
    def IsWhiteSpace(b: int, ) -> bool:
        ...

    @staticmethod
    def AppendJoin(value: System.Object, index: int, byteList: System.Collections.Generic.List[int], ) -> None:
        ...

    @staticmethod
    def CoerceBytes(obj: System.Object, ) -> System.Collections.Generic.IList[int]:
        ...

    @staticmethod
    def GetBytes(value: System.Object, useHint: bool, context: IronPython.Runtime.CodeContext = ..., ) -> System.Collections.Generic.IList[int]:
        ...

    @staticmethod
    def GetByte(o: System.Object, ) -> int:
        ...

    @staticmethod
    @typing.overload
    def __new__(cls: IronPython.Runtime.Types.PythonType, ) -> System.Object:
        ...

    @staticmethod
    @typing.overload
    def __new__(cls: IronPython.Runtime.Types.PythonType, value: System.Object, ) -> System.Object:
        ...

    @staticmethod
    def __bool__(x: int, ) -> bool:
        ...

    @staticmethod
    def __repr__(x: int, ) -> str:
        ...

    @staticmethod
    def __trunc__(x: int, ) -> int:
        ...

    @staticmethod
    def __int__(x: int, ) -> int:
        ...

    @staticmethod
    def __index__(x: int, ) -> int:
        ...

    @staticmethod
    def __hash__(x: int, ) -> int:
        ...

    @staticmethod
    def conjugate(x: int, ) -> int:
        ...

