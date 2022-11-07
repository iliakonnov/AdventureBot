from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import System
import System.Collections.Generic
import IronPython.Runtime
import IronPython.Runtime.Binding
import IronPython.Runtime.Types
import System.Linq.Expressions
import System.Dynamic


class DebugProxy(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def Members(self) -> System.Collections.Generic.List[IronPython.Runtime.ObjectDebugView]:
        ...

    # methods
    def __init__(self, module: IronPython.Runtime.PythonModule, ):
        ...

class MetaModule(IronPython.Runtime.Binding.IPythonGetable, IronPython.Runtime.Binding.MetaPythonObject):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def PythonType(self) -> IronPython.Runtime.Types.PythonType:
        ...

    @property
    def Expression(self) -> System.Linq.Expressions.Expression:
        ...

    @property
    def Restrictions(self) -> System.Dynamic.BindingRestrictions:
        ...

    @property
    def Value(self) -> System.Object:
        ...

    @property
    def HasValue(self) -> bool:
        ...

    @property
    def RuntimeType(self) -> System.Type:
        ...

    @property
    def LimitType(self) -> System.Type:
        ...

    # methods
    def __init__(self, module: IronPython.Runtime.PythonModule, self: System.Linq.Expressions.Expression, ):
        ...

    def BindGetMember(self, binder: System.Dynamic.GetMemberBinder, ) -> System.Dynamic.DynamicMetaObject:
        ...

    def GetMember(self, member: IronPython.Runtime.Binding.PythonGetMemberBinder, codeContext: System.Dynamic.DynamicMetaObject, ) -> System.Dynamic.DynamicMetaObject:
        ...

    def GetMemberWorker(self, binder: System.Dynamic.DynamicMetaObjectBinder, codeContext: System.Dynamic.DynamicMetaObject, ) -> System.Dynamic.DynamicMetaObject:
        ...

    def BindInvokeMember(self, action: System.Dynamic.InvokeMemberBinder, args: System.Array[System.Dynamic.DynamicMetaObject], ) -> System.Dynamic.DynamicMetaObject:
        ...

    def BindSetMember(self, binder: System.Dynamic.SetMemberBinder, value: System.Dynamic.DynamicMetaObject, ) -> System.Dynamic.DynamicMetaObject:
        ...

    def BindDeleteMember(self, binder: System.Dynamic.DeleteMemberBinder, ) -> System.Dynamic.DynamicMetaObject:
        ...

    def GetDynamicMemberNames(self, ) -> System.Collections.Generic.IEnumerable[str]:
        ...

