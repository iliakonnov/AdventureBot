from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import System
import Microsoft.Scripting.Debugging
import System.Collections.Generic


class ScopeData(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        self.VarInfos: System.Array[Microsoft.Scripting.Debugging.VariableInfo]
        self.VarInfosWithException: System.Array[Microsoft.Scripting.Debugging.VariableInfo]
        self.Scope: System.Collections.Generic.IDictionary[System.Object, System.Object]
        ...

    # static fields

    # properties
    # methods
    def __init__(self, ):
        ...

