from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import System
import IronPython.Runtime.Binding
import IronPython.Runtime
import IronPython.Runtime.Types
import System.Runtime.CompilerServices
import IronPython.Runtime.Types.PythonType
import System.Collections.Generic

T0 = typing.TypeVar('T0')
T1 = typing.TypeVar('T1')
T2 = typing.TypeVar('T2')
T3 = typing.TypeVar('T3')
T4 = typing.TypeVar('T4')
T = typing.TypeVar('T')

class PythonTypeAttributes(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    None_: int = ...
    Immutable: int = ...
    SystemType: int = ...
    IsPythonType: int = ...
    WeakReferencable: int = ...
    HasDictionary: int = ...
    SystemCtor: int = ...

class NewSite(System.Object, typing.Generic[T0, T1, T2, T3, T4]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    def __init__(self, binder: IronPython.Runtime.Binding.PythonInvokeBinder, target: System.Object, ):
        ...

    def Call(self, context: IronPython.Runtime.CodeContext, typeOrInstance: System.Object, arg0: T0, arg1: T1, arg2: T2, arg3: T3, arg4: T4, ) -> System.Object:
        ...

class NewSite(System.Object, typing.Generic[T0, T1, T2, T3]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    def __init__(self, binder: IronPython.Runtime.Binding.PythonInvokeBinder, target: System.Object, ):
        ...

    def Call(self, context: IronPython.Runtime.CodeContext, typeOrInstance: System.Object, arg0: T0, arg1: T1, arg2: T2, arg3: T3, ) -> System.Object:
        ...

class FastTypeSite(System.Object, typing.Generic[T0, T1, T2, T3, T4]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    def __init__(self, version: int, new: System.Func[IronPython.Runtime.CodeContext, System.Object, T0, T1, T2, T3, T4, System.Object], initBinder: IronPython.Runtime.Types.LateBoundInitBinder, ):
        ...

    def CallTarget(self, site: System.Runtime.CompilerServices.CallSite, context: IronPython.Runtime.CodeContext, type: System.Object, arg0: T0, arg1: T1, arg2: T2, arg3: T3, arg4: T4, ) -> System.Object:
        ...

class FastBindingBuilder(IronPython.Runtime.Types.PythonType.FastBindingBuilderBase, typing.Generic[T0, T1]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    def __init__(self, context: IronPython.Runtime.CodeContext, type: IronPython.Runtime.Types.PythonType, binder: IronPython.Runtime.Binding.PythonInvokeBinder, siteType: System.Type, genTypeArgs: System.Array[System.Type], ):
        ...

    def GetNewSiteDelegate(self, binder: IronPython.Runtime.Binding.PythonInvokeBinder, func: System.Object, ) -> System.Delegate:
        ...

    def MakeDelegate(self, version: int, newDlg: System.Delegate, initBinder: IronPython.Runtime.Types.LateBoundInitBinder, ) -> System.Delegate:
        ...

class DebugProxy(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def __bases__(self) -> System.Array[IronPython.Runtime.Types.PythonType]:
        ...

    @property
    def Members(self) -> System.Collections.Generic.List[IronPython.Runtime.ObjectDebugView]:
        ...

    # methods
    def __init__(self, type: IronPython.Runtime.Types.PythonType, ):
        ...

class FastBindingBuilder(IronPython.Runtime.Types.PythonType.FastBindingBuilderBase, typing.Generic[T0, T1, T2, T3]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    def __init__(self, context: IronPython.Runtime.CodeContext, type: IronPython.Runtime.Types.PythonType, binder: IronPython.Runtime.Binding.PythonInvokeBinder, siteType: System.Type, genTypeArgs: System.Array[System.Type], ):
        ...

    def GetNewSiteDelegate(self, binder: IronPython.Runtime.Binding.PythonInvokeBinder, func: System.Object, ) -> System.Delegate:
        ...

    def MakeDelegate(self, version: int, newDlg: System.Delegate, initBinder: IronPython.Runtime.Types.LateBoundInitBinder, ) -> System.Delegate:
        ...

class NewSite(System.Object, typing.Generic[T0, T1, T2]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    def __init__(self, binder: IronPython.Runtime.Binding.PythonInvokeBinder, target: System.Object, ):
        ...

    def Call(self, context: IronPython.Runtime.CodeContext, typeOrInstance: System.Object, arg0: T0, arg1: T1, arg2: T2, ) -> System.Object:
        ...

class FastTypeSite(System.Object, typing.Generic[T0]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    def __init__(self, version: int, new: System.Func[IronPython.Runtime.CodeContext, System.Object, T0, System.Object], initBinder: IronPython.Runtime.Types.LateBoundInitBinder, ):
        ...

    def CallTarget(self, site: System.Runtime.CompilerServices.CallSite, context: IronPython.Runtime.CodeContext, type: System.Object, arg0: T0, ) -> System.Object:
        ...

class FastBindingBuilder(IronPython.Runtime.Types.PythonType.FastBindingBuilderBase):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    def __init__(self, context: IronPython.Runtime.CodeContext, type: IronPython.Runtime.Types.PythonType, binder: IronPython.Runtime.Binding.PythonInvokeBinder, siteType: System.Type, genTypeArgs: System.Array[System.Type], ):
        ...

    def GetNewSiteDelegate(self, binder: IronPython.Runtime.Binding.PythonInvokeBinder, func: System.Object, ) -> System.Delegate:
        ...

    def MakeDelegate(self, version: int, newDlg: System.Delegate, initBinder: IronPython.Runtime.Types.LateBoundInitBinder, ) -> System.Delegate:
        ...

class NewSite(System.Object, typing.Generic[T0]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    def __init__(self, binder: IronPython.Runtime.Binding.PythonInvokeBinder, target: System.Object, ):
        ...

    def Call(self, context: IronPython.Runtime.CodeContext, typeOrInstance: System.Object, arg0: T0, ) -> System.Object:
        ...

class NewSite(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    def __init__(self, binder: IronPython.Runtime.Binding.PythonInvokeBinder, target: System.Object, ):
        ...

    def Call(self, context: IronPython.Runtime.CodeContext, type: System.Object, ) -> System.Object:
        ...

class WeakReferenceProxy(IronPython.Runtime.IWeakReferenceable, System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    def __init__(self, context: IronPython.Runtime.PythonContext, type: IronPython.Runtime.Types.PythonType, ):
        ...

    def GetWeakRef(self, ) -> IronPython.Runtime.WeakRefTracker:
        ...

    def SetFinalizer(self, value: IronPython.Runtime.WeakRefTracker, ) -> None:
        ...

    def SetWeakRef(self, value: IronPython.Runtime.WeakRefTracker, ) -> bool:
        ...

class FastTypeSite(System.Object, typing.Generic[T0, T1, T2]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    def __init__(self, version: int, new: System.Func[IronPython.Runtime.CodeContext, System.Object, T0, T1, T2, System.Object], initBinder: IronPython.Runtime.Types.LateBoundInitBinder, ):
        ...

    def CallTarget(self, site: System.Runtime.CompilerServices.CallSite, context: IronPython.Runtime.CodeContext, type: System.Object, arg0: T0, arg1: T1, arg2: T2, ) -> System.Object:
        ...

class FastTypeSite(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    def __init__(self, version: int, new: System.Func[IronPython.Runtime.CodeContext, System.Object, System.Object], initBinder: IronPython.Runtime.Types.LateBoundInitBinder, ):
        ...

    def CallTarget(self, site: System.Runtime.CompilerServices.CallSite, context: IronPython.Runtime.CodeContext, type: System.Object, ) -> System.Object:
        ...

class FastBindingBuilderBase(System.Object, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    def __init__(self, context: IronPython.Runtime.CodeContext, type: IronPython.Runtime.Types.PythonType, binder: IronPython.Runtime.Binding.PythonInvokeBinder, siteType: System.Type, genTypeArgs: System.Array[System.Type], ):
        ...

    def MakeBindingResult(self, ) -> System.Delegate:
        ...

    def GetOrCreateFastNew(self, ) -> System.Delegate:
        ...

    @abc.abstractmethod
    def GetNewSiteDelegate(self, binder: IronPython.Runtime.Binding.PythonInvokeBinder, func: System.Object, ) -> System.Delegate:
        ...

    @abc.abstractmethod
    def MakeDelegate(self, version: int, newDlg: System.Delegate, initBinder: IronPython.Runtime.Types.LateBoundInitBinder, ) -> System.Delegate:
        ...

class FastTypeSite(System.Object, typing.Generic[T0, T1, T2, T3]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    def __init__(self, version: int, new: System.Func[IronPython.Runtime.CodeContext, System.Object, T0, T1, T2, T3, System.Object], initBinder: IronPython.Runtime.Types.LateBoundInitBinder, ):
        ...

    def CallTarget(self, site: System.Runtime.CompilerServices.CallSite, context: IronPython.Runtime.CodeContext, type: System.Object, arg0: T0, arg1: T1, arg2: T2, arg3: T3, ) -> System.Object:
        ...

class FastBindingBuilder(IronPython.Runtime.Types.PythonType.FastBindingBuilderBase, typing.Generic[T0]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    def __init__(self, context: IronPython.Runtime.CodeContext, type: IronPython.Runtime.Types.PythonType, binder: IronPython.Runtime.Binding.PythonInvokeBinder, siteType: System.Type, genTypeArgs: System.Array[System.Type], ):
        ...

    def GetNewSiteDelegate(self, binder: IronPython.Runtime.Binding.PythonInvokeBinder, func: System.Object, ) -> System.Delegate:
        ...

    def MakeDelegate(self, version: int, newDlg: System.Delegate, initBinder: IronPython.Runtime.Types.LateBoundInitBinder, ) -> System.Delegate:
        ...

class FastBindingBuilder(IronPython.Runtime.Types.PythonType.FastBindingBuilderBase, typing.Generic[T0, T1, T2, T3, T4]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    def __init__(self, context: IronPython.Runtime.CodeContext, type: IronPython.Runtime.Types.PythonType, binder: IronPython.Runtime.Binding.PythonInvokeBinder, siteType: System.Type, genTypeArgs: System.Array[System.Type], ):
        ...

    def GetNewSiteDelegate(self, binder: IronPython.Runtime.Binding.PythonInvokeBinder, func: System.Object, ) -> System.Delegate:
        ...

    def MakeDelegate(self, version: int, newDlg: System.Delegate, initBinder: IronPython.Runtime.Types.LateBoundInitBinder, ) -> System.Delegate:
        ...

class NewSite(System.Object, typing.Generic[T0, T1]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    def __init__(self, binder: IronPython.Runtime.Binding.PythonInvokeBinder, target: System.Object, ):
        ...

    def Call(self, context: IronPython.Runtime.CodeContext, typeOrInstance: System.Object, arg0: T0, arg1: T1, ) -> System.Object:
        ...

class Setter(IronPython.Runtime.Binding.FastSetBase[T], typing.Generic[T]):
    @typing.overload
    def __init__(self, **kwargs):
        self._func: System.Delegate
        self._version: int
        self._hitCount: int
        ...

    # static fields

    # properties
    @property
    def ShouldUseNonOptimizedSite(self) -> bool:
        ...

    # methods
    def __init__(self, context: IronPython.Runtime.CodeContext, name: str, ):
        ...

    def Target(self, site: System.Runtime.CompilerServices.CallSite, self: System.Object, value: T, ) -> System.Object:
        ...

class FastTypeSite(System.Object, typing.Generic[T0, T1]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    def __init__(self, version: int, new: System.Func[IronPython.Runtime.CodeContext, System.Object, T0, T1, System.Object], initBinder: IronPython.Runtime.Types.LateBoundInitBinder, ):
        ...

    def CallTarget(self, site: System.Runtime.CompilerServices.CallSite, context: IronPython.Runtime.CodeContext, type: System.Object, arg0: T0, arg1: T1, ) -> System.Object:
        ...

class FastBindingBuilder(IronPython.Runtime.Types.PythonType.FastBindingBuilderBase, typing.Generic[T0, T1, T2]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    def __init__(self, context: IronPython.Runtime.CodeContext, type: IronPython.Runtime.Types.PythonType, binder: IronPython.Runtime.Binding.PythonInvokeBinder, siteType: System.Type, genTypeArgs: System.Array[System.Type], ):
        ...

    def GetNewSiteDelegate(self, binder: IronPython.Runtime.Binding.PythonInvokeBinder, func: System.Object, ) -> System.Delegate:
        ...

    def MakeDelegate(self, version: int, newDlg: System.Delegate, initBinder: IronPython.Runtime.Types.LateBoundInitBinder, ) -> System.Delegate:
        ...

