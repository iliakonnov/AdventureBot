from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import System
import IronPython.Runtime.PythonContext
import System.Collections
import System.Collections.Generic
import IronPython.Runtime
import IronPython.Runtime.Types
import Microsoft.Scripting
import System.IO
import Microsoft.Scripting.Debugging
import System.Reflection

T = typing.TypeVar('T')

class AttrKey(System.IEquatable[IronPython.Runtime.PythonContext.AttrKey], System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    def __init__(self, type: System.Type, name: str, ):
        ...

    @typing.overload
    def Equals(self, other: IronPython.Runtime.PythonContext.AttrKey, ) -> bool:
        ...

    @typing.overload
    def Equals(self, obj: System.Object, ) -> bool:
        ...

    def GetHashCode(self, ) -> int:
        ...

class PythonEqualityComparer(System.Collections.IEqualityComparer, System.Collections.Generic.IEqualityComparer[System.Object], System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        self.Context: IronPython.Runtime.PythonContext
        ...

    # static fields

    # properties
    # methods
    def __init__(self, context: IronPython.Runtime.PythonContext, ):
        ...

    def Equals(self, x: System.Object, y: System.Object, ) -> bool:
        ...

    def Equals(self, x: System.Object, y: System.Object, ) -> bool:
        ...

    def GetHashCode(self, obj: System.Object, ) -> int:
        ...

    def GetHashCode(self, obj: System.Object, ) -> int:
        ...

class DefaultPythonComparer(System.Collections.IComparer, System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    def __init__(self, context: IronPython.Runtime.PythonContext, ):
        ...

    def Compare(self, x: System.Object, y: System.Object, ) -> int:
        ...

class OptimizedBuiltinHasher(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    def __init__(self, context: IronPython.Runtime.PythonContext, type: System.Type, ):
        ...

    def Hasher(self, o: System.Object, dlg: ref[IronPython.Runtime.HashDelegate], ) -> int:
        ...

class OperationRetTypeKey(System.IEquatable[IronPython.Runtime.PythonContext.OperationRetTypeKey], System.Object, typing.Generic[T]):
    @typing.overload
    def __init__(self, **kwargs):
        self.ReturnType: System.Type
        self.Operation: T
        ...

    # static fields

    # properties
    # methods
    def __init__(self, retType: System.Type, operation: T, ):
        ...

    @typing.overload
    def Equals(self, other: IronPython.Runtime.PythonContext.OperationRetTypeKey, ) -> bool:
        ...

    @typing.overload
    def Equals(self, obj: System.Object, ) -> bool:
        ...

    def GetHashCode(self, ) -> int:
        ...

class DefaultPythonLtComparer(System.Collections.IComparer, System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    def __init__(self, context: IronPython.Runtime.PythonContext, ):
        ...

    def Compare(self, x: System.Object, y: System.Object, ) -> int:
        ...

class OptimizedUserHasher(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    def __init__(self, context: IronPython.Runtime.PythonContext, pt: IronPython.Runtime.Types.PythonType, ):
        ...

    def Hasher(self, o: System.Object, dlg: ref[IronPython.Runtime.HashDelegate], ) -> int:
        ...

class ResourceStreamContentProvider(Microsoft.Scripting.StreamContentProvider):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    def __init__(self, resourceName: str, ):
        ...

    def GetStream(self, ) -> System.IO.Stream:
        ...

class PythonTracebackListenersDispatcher(Microsoft.Scripting.Debugging.ITraceCallback, System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    def __init__(self, parent: IronPython.Runtime.PythonContext, ):
        ...

    def OnTraceEvent(self, kind: int, name: str, sourceFileName: str, sourceSpan: Microsoft.Scripting.SourceSpan, scopeCallback: System.Func[System.Collections.Generic.IDictionary[System.Object, System.Object]], payload: System.Object, customPayload: System.Object, ) -> None:
        ...

class AssemblyResolveHolder(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    def __init__(self, context: IronPython.Runtime.PythonContext, ):
        ...

    def AssemblyResolveEvent(self, sender: System.Object, args: System.ResolveEventArgs, ) -> System.Reflection.Assembly:
        ...

