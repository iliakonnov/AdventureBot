from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import System
import IronPython.Runtime.FunctionCode
import IronPython.Runtime
import Microsoft.Scripting.Interpreter


class CodeList(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        self.Code: System.WeakReference
        self.Next: IronPython.Runtime.FunctionCode.CodeList
        ...

    # static fields

    # properties
    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def __init__(self, code: System.WeakReference, next: IronPython.Runtime.FunctionCode.CodeList, ):
        ...

class TargetUpdaterForCompilation(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    def __init__(self, context: IronPython.Runtime.PythonContext, code: IronPython.Runtime.FunctionCode, ):
        ...

    def SetCompiledTarget(self, sender: System.Object, e: Microsoft.Scripting.Interpreter.LightLambdaCompileEventArgs, ) -> None:
        ...

    def SetCompiledTargetTracing(self, sender: System.Object, e: Microsoft.Scripting.Interpreter.LightLambdaCompileEventArgs, ) -> None:
        ...

