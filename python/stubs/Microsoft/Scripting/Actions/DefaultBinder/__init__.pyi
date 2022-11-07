from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import System
import Microsoft.Scripting.Actions.Calls
import Microsoft.Scripting.Actions
import System.Dynamic
import System.Reflection


class GetMemberInfo(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        self.Name: str
        self.ResolutionFactory: Microsoft.Scripting.Actions.Calls.OverloadResolverFactory
        self.IsNoThrow: bool
        self.Body: Microsoft.Scripting.Actions.ConditionalBuilder
        self.ErrorSuggestion: System.Dynamic.DynamicMetaObject
        ...

    # static fields

    # properties
    # methods
    def __init__(self, name: str, resolutionFactory: Microsoft.Scripting.Actions.Calls.OverloadResolverFactory, noThrow: bool, errorSuggestion: System.Dynamic.DynamicMetaObject, ):
        ...

class SetOrDeleteMemberInfo(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        self.Name: str
        self.ResolutionFactory: Microsoft.Scripting.Actions.Calls.OverloadResolverFactory
        self.Body: Microsoft.Scripting.Actions.ConditionalBuilder
        ...

    # static fields

    # properties
    # methods
    def __init__(self, name: str, resolutionFactory: Microsoft.Scripting.Actions.Calls.OverloadResolverFactory, ):
        ...

class TargetInfo(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        self.Instance: System.Dynamic.DynamicMetaObject
        self.Arguments: System.Array[System.Dynamic.DynamicMetaObject]
        self.Targets: System.Array[System.Reflection.MethodBase]
        self.Restrictions: System.Dynamic.BindingRestrictions
        ...

    # static fields

    # properties
    # methods
    @typing.overload
    def __init__(self, instance: System.Dynamic.DynamicMetaObject, arguments: System.Array[System.Dynamic.DynamicMetaObject], args: System.Array[System.Reflection.MethodBase], ):
        ...

    @typing.overload
    def __init__(self, instance: System.Dynamic.DynamicMetaObject, arguments: System.Array[System.Dynamic.DynamicMetaObject], restrictions: System.Dynamic.BindingRestrictions, targets: System.Array[System.Reflection.MethodBase], ):
        ...

class IndexType(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    Get: int = ...
    Set: int = ...

