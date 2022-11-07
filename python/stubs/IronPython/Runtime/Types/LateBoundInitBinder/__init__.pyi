from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import System
import IronPython.Runtime.Binding
import IronPython.Runtime
import System.Runtime.CompilerServices

T0 = typing.TypeVar('T0')
T1 = typing.TypeVar('T1')
T2 = typing.TypeVar('T2')
T3 = typing.TypeVar('T3')
T4 = typing.TypeVar('T4')

class FastInitSite(System.Object, typing.Generic[T0, T1, T2, T3]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    def __init__(self, version: int, binder: IronPython.Runtime.Binding.PythonInvokeBinder, target: IronPython.Runtime.PythonFunction, ):
        ...

    def CallTarget(self, site: System.Runtime.CompilerServices.CallSite, context: IronPython.Runtime.CodeContext, inst: System.Object, arg0: T0, arg1: T1, arg2: T2, arg3: T3, ) -> System.Object:
        ...

    def EmptyCallTarget(self, site: System.Runtime.CompilerServices.CallSite, context: IronPython.Runtime.CodeContext, inst: System.Object, arg0: T0, arg1: T1, arg2: T2, arg3: T3, ) -> System.Object:
        ...

class FastInitSite(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    def __init__(self, version: int, binder: IronPython.Runtime.Binding.PythonInvokeBinder, target: IronPython.Runtime.PythonFunction, ):
        ...

    def CallTarget(self, site: System.Runtime.CompilerServices.CallSite, context: IronPython.Runtime.CodeContext, inst: System.Object, ) -> System.Object:
        ...

    def EmptyCallTarget(self, site: System.Runtime.CompilerServices.CallSite, context: IronPython.Runtime.CodeContext, inst: System.Object, ) -> System.Object:
        ...

class FastInitSite(System.Object, typing.Generic[T0, T1]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    def __init__(self, version: int, binder: IronPython.Runtime.Binding.PythonInvokeBinder, target: IronPython.Runtime.PythonFunction, ):
        ...

    def CallTarget(self, site: System.Runtime.CompilerServices.CallSite, context: IronPython.Runtime.CodeContext, inst: System.Object, arg0: T0, arg1: T1, ) -> System.Object:
        ...

    def EmptyCallTarget(self, site: System.Runtime.CompilerServices.CallSite, context: IronPython.Runtime.CodeContext, inst: System.Object, arg0: T0, arg1: T1, ) -> System.Object:
        ...

class FastInitSite(System.Object, typing.Generic[T0, T1, T2, T3, T4]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    def __init__(self, version: int, binder: IronPython.Runtime.Binding.PythonInvokeBinder, target: IronPython.Runtime.PythonFunction, ):
        ...

    def CallTarget(self, site: System.Runtime.CompilerServices.CallSite, context: IronPython.Runtime.CodeContext, inst: System.Object, arg0: T0, arg1: T1, arg2: T2, arg3: T3, arg4: T4, ) -> System.Object:
        ...

    def EmptyCallTarget(self, site: System.Runtime.CompilerServices.CallSite, context: IronPython.Runtime.CodeContext, inst: System.Object, arg0: T0, arg1: T1, arg2: T2, arg3: T3, arg4: T4, ) -> System.Object:
        ...

class FastInitSite(System.Object, typing.Generic[T0]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    def __init__(self, version: int, binder: IronPython.Runtime.Binding.PythonInvokeBinder, target: IronPython.Runtime.PythonFunction, ):
        ...

    def CallTarget(self, site: System.Runtime.CompilerServices.CallSite, context: IronPython.Runtime.CodeContext, inst: System.Object, arg0: T0, ) -> System.Object:
        ...

    def EmptyCallTarget(self, site: System.Runtime.CompilerServices.CallSite, context: IronPython.Runtime.CodeContext, inst: System.Object, arg0: T0, ) -> System.Object:
        ...

class FastInitSite(System.Object, typing.Generic[T0, T1, T2]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    def __init__(self, version: int, binder: IronPython.Runtime.Binding.PythonInvokeBinder, target: IronPython.Runtime.PythonFunction, ):
        ...

    def CallTarget(self, site: System.Runtime.CompilerServices.CallSite, context: IronPython.Runtime.CodeContext, inst: System.Object, arg0: T0, arg1: T1, arg2: T2, ) -> System.Object:
        ...

    def EmptyCallTarget(self, site: System.Runtime.CompilerServices.CallSite, context: IronPython.Runtime.CodeContext, inst: System.Object, arg0: T0, arg1: T1, arg2: T2, ) -> System.Object:
        ...

