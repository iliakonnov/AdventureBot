from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import IronPython.Compiler.CompilationMode
import System.Dynamic
import System
import System.Linq.Expressions
import System.Reflection
import System.Runtime.CompilerServices

T = typing.TypeVar('T')

class SiteInfo(IronPython.Compiler.CompilationMode.SiteInfo, typing.Generic[T]):
    @typing.overload
    def __init__(self, **kwargs):
        self.Binder: System.Dynamic.DynamicMetaObjectBinder
        self.DelegateType: System.Type
        self._siteType: System.Type
        self.Expression: System.Linq.Expressions.Expression
        self.Field: System.Reflection.FieldInfo
        self.Offset: int
        ...

    # static fields

    # properties
    @property
    def SiteType(self) -> System.Type:
        ...

    # methods
    def __init__(self, binder: System.Dynamic.DynamicMetaObjectBinder, expr: System.Linq.Expressions.Expression, field: System.Reflection.FieldInfo, index: int, ):
        ...

    def MakeSite(self, ) -> System.Runtime.CompilerServices.CallSite:
        ...

class ConstantInfo(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        self.Expression: System.Linq.Expressions.Expression
        self.Field: System.Reflection.FieldInfo
        self.Offset: int
        ...

    # static fields

    # properties
    # methods
    def __init__(self, expr: System.Linq.Expressions.Expression, field: System.Reflection.FieldInfo, offset: int, ):
        ...

class SiteInfoLarge(IronPython.Compiler.CompilationMode.SiteInfo):
    @typing.overload
    def __init__(self, **kwargs):
        self.Binder: System.Dynamic.DynamicMetaObjectBinder
        self.DelegateType: System.Type
        self._siteType: System.Type
        self.Expression: System.Linq.Expressions.Expression
        self.Field: System.Reflection.FieldInfo
        self.Offset: int
        ...

    # static fields

    # properties
    @property
    def SiteType(self) -> System.Type:
        ...

    # methods
    def __init__(self, binder: System.Dynamic.DynamicMetaObjectBinder, expr: System.Linq.Expressions.Expression, field: System.Reflection.FieldInfo, index: int, delegateType: System.Type, ):
        ...

    def MakeSite(self, ) -> System.Runtime.CompilerServices.CallSite:
        ...

class SiteInfo(IronPython.Compiler.CompilationMode.ConstantInfo, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        self.Binder: System.Dynamic.DynamicMetaObjectBinder
        self.DelegateType: System.Type
        self._siteType: System.Type
        self.Expression: System.Linq.Expressions.Expression
        self.Field: System.Reflection.FieldInfo
        self.Offset: int
        ...

    # static fields

    # properties
    @property
    def SiteType(self) -> System.Type:
        ...

    # methods
    @typing.overload
    def __init__(self, binder: System.Dynamic.DynamicMetaObjectBinder, expr: System.Linq.Expressions.Expression, field: System.Reflection.FieldInfo, index: int, delegateType: System.Type, ):
        ...

    @typing.overload
    def __init__(self, binder: System.Dynamic.DynamicMetaObjectBinder, expr: System.Linq.Expressions.Expression, field: System.Reflection.FieldInfo, index: int, delegateType: System.Type, siteType: System.Type, ):
        ...

    @abc.abstractmethod
    def MakeSite(self, ) -> System.Runtime.CompilerServices.CallSite:
        ...

