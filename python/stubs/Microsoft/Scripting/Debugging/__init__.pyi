from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import System
import System.Collections.Generic
import Microsoft.Scripting.Debugging
import Microsoft.Scripting.Debugging.CompilerServices
import Microsoft.Scripting
import Microsoft.Scripting.Runtime
import Microsoft.Scripting.Debugging.DebugFrame
import System.Runtime.CompilerServices


class FunctionInfo(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def GeneratorFactory(self) -> System.Delegate:
        ...

    @property
    def Variables(self) -> System.Collections.Generic.IList[Microsoft.Scripting.Debugging.VariableInfo]:
        ...

    @property
    def VariableScopeMap(self) -> System.Array[System.Collections.Generic.IList[Microsoft.Scripting.Debugging.VariableInfo]]:
        ...

    @property
    def PreviousVersion(self) -> Microsoft.Scripting.Debugging.FunctionInfo:
        ...
    @PreviousVersion.setter
    def PreviousVersion(self, val: Microsoft.Scripting.Debugging.FunctionInfo):
        ...

    @property
    def NextVersion(self) -> Microsoft.Scripting.Debugging.FunctionInfo:
        ...
    @NextVersion.setter
    def NextVersion(self, val: Microsoft.Scripting.Debugging.FunctionInfo):
        ...

    @property
    def Version(self) -> int:
        ...
    @Version.setter
    def Version(self, val: int):
        ...

    @property
    def SequencePoints(self) -> System.Array[Microsoft.Scripting.Debugging.DebugSourceSpan]:
        ...

    @property
    def Name(self) -> str:
        ...

    @property
    def CustomPayload(self) -> System.Object:
        ...

    # methods
    def __init__(self, generatorFactory: System.Delegate, name: str, sequencePoints: System.Array[Microsoft.Scripting.Debugging.DebugSourceSpan], scopedVariables: System.Array[System.Collections.Generic.IList[Microsoft.Scripting.Debugging.VariableInfo]], variables: System.Collections.Generic.IList[Microsoft.Scripting.Debugging.VariableInfo], customPayload: System.Object, ):
        ...

    def GetTraceLocations(self, ) -> System.Array[bool]:
        ...

class DebugThread(System.Object, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def DebugContext(self) -> Microsoft.Scripting.Debugging.CompilerServices.DebugContext:
        ...

    @property
    def ThrownException(self) -> System.Exception:
        ...
    @ThrownException.setter
    def ThrownException(self, val: System.Exception):
        ...

    @property
    def IsCurrentThread(self) -> bool:
        ...

    @property
    def IsInTraceback(self) -> bool:
        ...
    @IsInTraceback.setter
    def IsInTraceback(self, val: bool):
        ...

    @property
    @abc.abstractmethod
    def Frames(self) -> System.Collections.Generic.IEnumerable[Microsoft.Scripting.Debugging.DebugFrame]:
        ...

    @property
    @abc.abstractmethod
    def FrameCount(self) -> int:
        ...

    # methods
    def __init__(self, debugContext: Microsoft.Scripting.Debugging.CompilerServices.DebugContext, ):
        ...

    @abc.abstractmethod
    def GetLeafFrame(self, ) -> Microsoft.Scripting.Debugging.DebugFrame:
        ...

    @abc.abstractmethod
    def TryGetLeafFrame(self, frame: ref[Microsoft.Scripting.Debugging.DebugFrame], ) -> bool:
        ...

    @abc.abstractmethod
    def PushExistingFrame(self, frame: Microsoft.Scripting.Debugging.DebugFrame, ) -> None:
        ...

    @abc.abstractmethod
    def PopFrame(self, ) -> bool:
        ...

    @abc.abstractmethod
    def GetLeafFrameFunctionInfo(self, stackDepth: ref[int], ) -> Microsoft.Scripting.Debugging.FunctionInfo:
        ...

class DebugSourceFile(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def FunctionInfoMap(self) -> System.Collections.Generic.Dictionary[Microsoft.Scripting.Debugging.DebugSourceSpan, Microsoft.Scripting.Debugging.FunctionInfo]:
        ...

    @property
    def Name(self) -> str:
        ...

    @property
    def DebugMode(self) -> int:
        ...
    @DebugMode.setter
    def DebugMode(self, val: int):
        ...

    @property
    def Mode(self) -> int:
        ...

    # methods
    def __init__(self, fileName: str, debugMode: int, ):
        ...

    def LookupFunctionInfo(self, span: Microsoft.Scripting.Debugging.DebugSourceSpan, ) -> Microsoft.Scripting.Debugging.FunctionInfo:
        ...

class TraceEventKind(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    FrameEnter: int = ...
    FrameExit: int = ...
    ThreadExit: int = ...
    TracePoint: int = ...
    Exception: int = ...
    ExceptionUnwind: int = ...

class ITracePipeline(abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    @abc.abstractmethod
    def TraceCallback(self) -> Microsoft.Scripting.Debugging.ITraceCallback:
        ...
    @TraceCallback.setter
    @abc.abstractmethod
    def TraceCallback(self, val: Microsoft.Scripting.Debugging.ITraceCallback):
        ...

    # methods
    @abc.abstractmethod
    def Close(self, ) -> None:
        ...

    @abc.abstractmethod
    def TrySetNextStatement(self, sourceFile: str, sourceSpan: Microsoft.Scripting.SourceSpan, ) -> bool:
        ...

class ITraceCallback(abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    @abc.abstractmethod
    def OnTraceEvent(self, kind: int, name: str, sourceFileName: str, sourceSpan: Microsoft.Scripting.SourceSpan, scopeCallback: System.Func[System.Collections.Generic.IDictionary[System.Object, System.Object]], payload: System.Object, customPayload: System.Object, ) -> None:
        ...

class DebugFrame(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def Thread(self) -> Microsoft.Scripting.Debugging.DebugThread:
        ...

    @property
    def StackDepth(self) -> int:
        ...
    @StackDepth.setter
    def StackDepth(self, val: int):
        ...

    @property
    def Variables(self) -> System.Array[Microsoft.Scripting.Debugging.VariableInfo]:
        ...

    @property
    def CurrentSequencePointIndex(self) -> int:
        ...
    @CurrentSequencePointIndex.setter
    def CurrentSequencePointIndex(self, val: int):
        ...

    @property
    def FunctionInfo(self) -> Microsoft.Scripting.Debugging.FunctionInfo:
        ...

    @property
    def ThrownException(self) -> System.Exception:
        ...
    @ThrownException.setter
    def ThrownException(self, val: System.Exception):
        ...

    @property
    def Generator(self) -> Microsoft.Scripting.Runtime.IDebuggableGenerator:
        ...

    @property
    def IsInTraceback(self) -> bool:
        ...
    @IsInTraceback.setter
    def IsInTraceback(self, val: bool):
        ...

    @property
    def InGeneratorLoop(self) -> bool:
        ...
    @InGeneratorLoop.setter
    def InGeneratorLoop(self, val: bool):
        ...

    @property
    def ForceSwitchToGeneratorLoop(self) -> bool:
        ...
    @ForceSwitchToGeneratorLoop.setter
    def ForceSwitchToGeneratorLoop(self, val: bool):
        ...

    @property
    def DebugContext(self) -> Microsoft.Scripting.Debugging.CompilerServices.DebugContext:
        ...

    @property
    def CurrentLocationCookie(self) -> int:
        ...

    @property
    def LastKnownGeneratorYieldMarker(self) -> int:
        ...
    @LastKnownGeneratorYieldMarker.setter
    def LastKnownGeneratorYieldMarker(self, val: int):
        ...

    @property
    def CurrentScopeData(self) -> Microsoft.Scripting.Debugging.DebugFrame.ScopeData:
        ...

    @property
    def LocalsInCurrentScope(self) -> System.Collections.Generic.IList[Microsoft.Scripting.Debugging.VariableInfo]:
        ...

    # methods
    @typing.overload
    def __init__(self, thread: Microsoft.Scripting.Debugging.DebugThread, funcInfo: Microsoft.Scripting.Debugging.FunctionInfo, ):
        ...

    @typing.overload
    def __init__(self, thread: Microsoft.Scripting.Debugging.DebugThread, funcInfo: Microsoft.Scripting.Debugging.FunctionInfo, liftedLocals: System.Runtime.CompilerServices.IRuntimeVariables, frameOrder: int, ):
        ...

    def RemapToLatestVersion(self, ) -> None:
        ...

    def ReplaceLiftedLocals(self, liftedLocals: System.Runtime.CompilerServices.IRuntimeVariables, ) -> None:
        ...

    def RemapToGenerator(self, version: int, ) -> None:
        ...

    def GetLocalsScope(self, ) -> System.Collections.Generic.IDictionary[System.Object, System.Object]:
        ...

    def CreateGenerator(self, targetFuncInfo: Microsoft.Scripting.Debugging.FunctionInfo, ) -> None:
        ...

    def GetParamValuesForGenerator(self, ) -> System.Array[System.Object]:
        ...

    def GetFunctionInfo(self, version: int, ) -> Microsoft.Scripting.Debugging.FunctionInfo:
        ...

