from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import System
import Microsoft.Scripting.Actions.Calls
import System.Dynamic
import System.Reflection
import System.Collections.Generic
import IronPython.Runtime.Types.BuiltinFunction
import IronPython.Runtime.Types


class BindingResult(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        self.Target: Microsoft.Scripting.Actions.Calls.BindingTarget
        self.MetaObject: System.Dynamic.DynamicMetaObject
        ...

    # static fields

    # properties
    # methods
    def __init__(self, target: Microsoft.Scripting.Actions.Calls.BindingTarget, meta: System.Dynamic.DynamicMetaObject, ):
        ...

class TypeList(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    def __init__(self, types: System.Array[System.Type], ):
        ...

    def Equals(self, obj: System.Object, ) -> bool:
        ...

    def GetHashCode(self, ) -> int:
        ...

class BuiltinFunctionData(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        self.Name: str
        self.Targets: System.Array[System.Reflection.MethodBase]
        self.DeclaringType: System.Type
        self.Type: int
        self.BoundGenerics: System.Collections.Generic.Dictionary[IronPython.Runtime.Types.BuiltinFunction.TypeList, IronPython.Runtime.Types.BuiltinFunction]
        self.OverloadDictionary: System.Collections.Generic.Dictionary[IronPython.Runtime.Types.BuiltinFunction.TypeList, IronPython.Runtime.Types.BuiltinFunction]
        ...

    # static fields

    # properties
    # methods
    def __init__(self, name: str, targets: System.Array[System.Reflection.MethodBase], declType: System.Type, functionType: int, ):
        ...

    def AddMethod(self, info: System.Reflection.MethodBase, ) -> None:
        ...

