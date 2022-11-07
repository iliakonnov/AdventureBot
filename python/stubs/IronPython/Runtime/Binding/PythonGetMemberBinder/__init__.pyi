from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import IronPython.Runtime.Binding
import System
import System.Runtime.CompilerServices
import IronPython.Runtime
import IronPython.Runtime.Types
import IronPython.Runtime.Binding.PythonGetMemberBinder
import Microsoft.Scripting.Runtime
import Microsoft.Scripting.Actions
import System.Collections.Generic

TSelfType = typing.TypeVar('TSelfType')

class BuiltinBase(IronPython.Runtime.Binding.FastGetBase, typing.Generic[TSelfType]):
    @typing.overload
    def __init__(self, **kwargs):
        self._func: System.Func[System.Runtime.CompilerServices.CallSite, System.Object, IronPython.Runtime.CodeContext, System.Object]
        self._hitCount: int
        ...

    # static fields

    # properties
    @property
    def ShouldCache(self) -> bool:
        ...

    @property
    def ShouldUseNonOptimizedSite(self) -> bool:
        ...

    # methods
    def __init__(self, ):
        ...

    def IsValid(self, type: IronPython.Runtime.Types.PythonType, ) -> bool:
        ...

class NamespaceTrackerDelegate(IronPython.Runtime.Binding.FastGetBase):
    @typing.overload
    def __init__(self, **kwargs):
        self._func: System.Func[System.Runtime.CompilerServices.CallSite, System.Object, IronPython.Runtime.CodeContext, System.Object]
        self._hitCount: int
        ...

    # static fields

    # properties
    @property
    def ShouldCache(self) -> bool:
        ...

    @property
    def ShouldUseNonOptimizedSite(self) -> bool:
        ...

    # methods
    def __init__(self, name: str, ):
        ...

    def Target(self, site: System.Runtime.CompilerServices.CallSite, self: System.Object, context: IronPython.Runtime.CodeContext, ) -> System.Object:
        ...

    def NoThrowTarget(self, site: System.Runtime.CompilerServices.CallSite, self: System.Object, context: IronPython.Runtime.CodeContext, ) -> System.Object:
        ...

    def GetName(self, site: System.Runtime.CompilerServices.CallSite, self: System.Object, context: IronPython.Runtime.CodeContext, ) -> System.Object:
        ...

    def GetFile(self, site: System.Runtime.CompilerServices.CallSite, self: System.Object, context: IronPython.Runtime.CodeContext, ) -> System.Object:
        ...

    def GetDict(self, site: System.Runtime.CompilerServices.CallSite, self: System.Object, context: IronPython.Runtime.CodeContext, ) -> System.Object:
        ...

    def IsValid(self, type: IronPython.Runtime.Types.PythonType, ) -> bool:
        ...

class PythonModuleDelegate(IronPython.Runtime.Binding.FastGetBase):
    @typing.overload
    def __init__(self, **kwargs):
        self._func: System.Func[System.Runtime.CompilerServices.CallSite, System.Object, IronPython.Runtime.CodeContext, System.Object]
        self._hitCount: int
        ...

    # static fields

    # properties
    @property
    def ShouldCache(self) -> bool:
        ...

    @property
    def ShouldUseNonOptimizedSite(self) -> bool:
        ...

    # methods
    def __init__(self, name: str, ):
        ...

    def Target(self, site: System.Runtime.CompilerServices.CallSite, self: System.Object, context: IronPython.Runtime.CodeContext, ) -> System.Object:
        ...

    def NoThrowTarget(self, site: System.Runtime.CompilerServices.CallSite, self: System.Object, context: IronPython.Runtime.CodeContext, ) -> System.Object:
        ...

    def LightThrowTarget(self, site: System.Runtime.CompilerServices.CallSite, self: System.Object, context: IronPython.Runtime.CodeContext, ) -> System.Object:
        ...

    def IsValid(self, type: IronPython.Runtime.Types.PythonType, ) -> bool:
        ...

class FastTypeGet(IronPython.Runtime.Binding.PythonGetMemberBinder.BuiltinBase[TSelfType], typing.Generic[TSelfType]):
    @typing.overload
    def __init__(self, **kwargs):
        self._func: System.Func[System.Runtime.CompilerServices.CallSite, System.Object, IronPython.Runtime.CodeContext, System.Object]
        self._hitCount: int
        ...

    # static fields

    # properties
    @property
    def ShouldCache(self) -> bool:
        ...

    @property
    def ShouldUseNonOptimizedSite(self) -> bool:
        ...

    # methods
    def __init__(self, type: System.Type, pythonType: System.Object, ):
        ...

    def GetTypeObject(self, site: System.Runtime.CompilerServices.CallSite, target: TSelfType, context: IronPython.Runtime.CodeContext, ) -> System.Object:
        ...

class FastErrorGet(IronPython.Runtime.Binding.FastGetBase, typing.Generic[TSelfType]):
    @typing.overload
    def __init__(self, **kwargs):
        self._func: System.Func[System.Runtime.CompilerServices.CallSite, System.Object, IronPython.Runtime.CodeContext, System.Object]
        self._hitCount: int
        ...

    # static fields

    # properties
    @property
    def ShouldCache(self) -> bool:
        ...

    @property
    def ShouldUseNonOptimizedSite(self) -> bool:
        ...

    # methods
    def __init__(self, type: System.Type, name: str, extMethodSet: IronPython.Runtime.ExtensionMethodSet, ):
        ...

    def IsValid(self, type: IronPython.Runtime.Types.PythonType, ) -> bool:
        ...

    def GetError(self, site: System.Runtime.CompilerServices.CallSite, target: TSelfType, context: IronPython.Runtime.CodeContext, ) -> System.Object:
        ...

    def GetErrorLightThrow(self, site: System.Runtime.CompilerServices.CallSite, target: TSelfType, context: IronPython.Runtime.CodeContext, ) -> System.Object:
        ...

    def GetErrorNoThrow(self, site: System.Runtime.CompilerServices.CallSite, target: TSelfType, context: IronPython.Runtime.CodeContext, ) -> System.Object:
        ...

    def GetAmbiguous(self, site: System.Runtime.CompilerServices.CallSite, target: TSelfType, context: IronPython.Runtime.CodeContext, ) -> System.Object:
        ...

class FastMethodGet(IronPython.Runtime.Binding.PythonGetMemberBinder.BuiltinBase[TSelfType], typing.Generic[TSelfType]):
    @typing.overload
    def __init__(self, **kwargs):
        self._func: System.Func[System.Runtime.CompilerServices.CallSite, System.Object, IronPython.Runtime.CodeContext, System.Object]
        self._hitCount: int
        ...

    # static fields

    # properties
    @property
    def ShouldCache(self) -> bool:
        ...

    @property
    def ShouldUseNonOptimizedSite(self) -> bool:
        ...

    # methods
    def __init__(self, type: System.Type, method: IronPython.Runtime.Types.BuiltinMethodDescriptor, ):
        ...

    def GetMethod(self, site: System.Runtime.CompilerServices.CallSite, target: TSelfType, context: IronPython.Runtime.CodeContext, ) -> System.Object:
        ...

class LightThrowBinder(IronPython.Runtime.Binding.IPythonSite, Microsoft.Scripting.Runtime.IExpressionSerializable, Microsoft.Scripting.Actions.ILightExceptionBinder, IronPython.Runtime.Binding.PythonGetMemberBinder):
    @typing.overload
    def __init__(self, **kwargs):
        self.Cache: System.Collections.Generic.Dictionary[System.Type, System.Object]
        ...

    # static fields

    # properties
    @property
    def SupportsLightThrow(self) -> bool:
        ...

    @property
    def Name(self) -> str:
        ...

    @property
    def Context(self) -> IronPython.Runtime.PythonContext:
        ...

    @property
    def IsNoThrow(self) -> bool:
        ...

    @property
    def ReturnType(self) -> System.Type:
        ...

    @property
    def IsStandardBinder(self) -> bool:
        ...

    # methods
    def __init__(self, context: IronPython.Runtime.PythonContext, name: str, isNoThrow: bool, ):
        ...

    def GetLightExceptionBinder(self, ) -> System.Runtime.CompilerServices.CallSiteBinder:
        ...

class FastSlotGet(IronPython.Runtime.Binding.PythonGetMemberBinder.BuiltinBase[TSelfType], typing.Generic[TSelfType]):
    @typing.overload
    def __init__(self, **kwargs):
        self._func: System.Func[System.Runtime.CompilerServices.CallSite, System.Object, IronPython.Runtime.CodeContext, System.Object]
        self._hitCount: int
        ...

    # static fields

    # properties
    @property
    def ShouldCache(self) -> bool:
        ...

    @property
    def ShouldUseNonOptimizedSite(self) -> bool:
        ...

    # methods
    def __init__(self, type: System.Type, slot: IronPython.Runtime.Types.PythonTypeSlot, owner: IronPython.Runtime.Types.PythonType, ):
        ...

    def GetRetSlot(self, site: System.Runtime.CompilerServices.CallSite, target: TSelfType, context: IronPython.Runtime.CodeContext, ) -> System.Object:
        ...

    def GetBindSlot(self, site: System.Runtime.CompilerServices.CallSite, target: TSelfType, context: IronPython.Runtime.CodeContext, ) -> System.Object:
        ...

class FastPropertyGet(IronPython.Runtime.Binding.PythonGetMemberBinder.BuiltinBase[TSelfType], typing.Generic[TSelfType]):
    @typing.overload
    def __init__(self, **kwargs):
        self._func: System.Func[System.Runtime.CompilerServices.CallSite, System.Object, IronPython.Runtime.CodeContext, System.Object]
        self._hitCount: int
        ...

    # static fields

    # properties
    @property
    def ShouldCache(self) -> bool:
        ...

    @property
    def ShouldUseNonOptimizedSite(self) -> bool:
        ...

    # methods
    def __init__(self, type: System.Type, propGetter: System.Func[System.Object, System.Object], ):
        ...

    def GetProperty(self, site: System.Runtime.CompilerServices.CallSite, target: TSelfType, context: IronPython.Runtime.CodeContext, ) -> System.Object:
        ...

    def GetPropertyBool(self, site: System.Runtime.CompilerServices.CallSite, target: TSelfType, context: IronPython.Runtime.CodeContext, ) -> System.Object:
        ...

    def GetPropertyInt(self, site: System.Runtime.CompilerServices.CallSite, target: TSelfType, context: IronPython.Runtime.CodeContext, ) -> System.Object:
        ...

