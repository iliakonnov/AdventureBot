from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import IronPython.Runtime.Binding
import Microsoft.Scripting.Runtime
import Microsoft.Scripting.Actions
import System.Collections.Generic
import System
import IronPython.Runtime
import System.Runtime.CompilerServices


class LightThrowBinder(IronPython.Runtime.Binding.IPythonSite, Microsoft.Scripting.Runtime.IExpressionSerializable, Microsoft.Scripting.Actions.ILightExceptionBinder, IronPython.Runtime.Binding.PythonInvokeBinder):
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
    def Signature(self) -> Microsoft.Scripting.Actions.CallSignature:
        ...

    @property
    def Context(self) -> IronPython.Runtime.PythonContext:
        ...

    @property
    def ReturnType(self) -> System.Type:
        ...

    @property
    def IsStandardBinder(self) -> bool:
        ...

    # methods
    def __init__(self, context: IronPython.Runtime.PythonContext, signature: Microsoft.Scripting.Actions.CallSignature, ):
        ...

    def GetLightExceptionBinder(self, ) -> System.Runtime.CompilerServices.CallSiteBinder:
        ...

