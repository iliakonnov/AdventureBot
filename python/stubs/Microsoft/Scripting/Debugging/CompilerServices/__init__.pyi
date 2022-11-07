from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import System
import System.Collections.Generic
import Microsoft.Scripting.Debugging
import Microsoft.Scripting.Debugging.CompilerServices
import System.Linq.Expressions


class DebugContext(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def Mode(self) -> int:
        ...

    @property
    def DebugMode(self) -> int:
        ...
    @DebugMode.setter
    def DebugMode(self, val: int):
        ...

    @property
    def Threads(self) -> System.Collections.Generic.IEnumerable[Microsoft.Scripting.Debugging.DebugThread]:
        ...

    @property
    def DebugCallback(self) -> Microsoft.Scripting.Debugging.IDebugCallback:
        ...
    @DebugCallback.setter
    def DebugCallback(self, val: Microsoft.Scripting.Debugging.IDebugCallback):
        ...

    @property
    def ThreadFactory(self) -> Microsoft.Scripting.Debugging.IDebugThreadFactory:
        ...

    @property
    def DebugYieldValue(self) -> System.Object:
        ...

    # methods
    def __init__(self, runtimeThreadFactory: Microsoft.Scripting.Debugging.IDebugThreadFactory, ):
        ...

    @staticmethod
    @typing.overload
    def CreateInstance() -> Microsoft.Scripting.Debugging.CompilerServices.DebugContext:
        ...

    @staticmethod
    @typing.overload
    def CreateInstance(runtimeThreadFactory: Microsoft.Scripting.Debugging.IDebugThreadFactory, ) -> Microsoft.Scripting.Debugging.CompilerServices.DebugContext:
        ...

    @typing.overload
    def TransformLambda(self, lambda: System.Linq.Expressions.LambdaExpression, lambdaInfo: Microsoft.Scripting.Debugging.CompilerServices.DebugLambdaInfo, ) -> System.Linq.Expressions.LambdaExpression:
        ...

    @typing.overload
    def TransformLambda(self, lambda: System.Linq.Expressions.LambdaExpression, ) -> System.Linq.Expressions.LambdaExpression:
        ...

    def ResetSourceFile(self, sourceFileName: str, ) -> None:
        ...

    def Lookup(self, sourceFile: str, ) -> Microsoft.Scripting.Debugging.DebugSourceFile:
        ...

    def GetDebugSourceFile(self, sourceFile: str, ) -> Microsoft.Scripting.Debugging.DebugSourceFile:
        ...

    @staticmethod
    def CreateFunctionInfo(generatorFactory: System.Delegate, name: str, locationSpanMap: System.Array[Microsoft.Scripting.Debugging.DebugSourceSpan], scopedVariables: System.Array[System.Collections.Generic.IList[Microsoft.Scripting.Debugging.VariableInfo]], variables: System.Collections.Generic.IList[Microsoft.Scripting.Debugging.VariableInfo], customPayload: System.Object, ) -> Microsoft.Scripting.Debugging.FunctionInfo:
        ...

    def CreateFrameForGenerator(self, func: Microsoft.Scripting.Debugging.FunctionInfo, ) -> Microsoft.Scripting.Debugging.DebugFrame:
        ...

    def DispatchDebugEvent(self, thread: Microsoft.Scripting.Debugging.DebugThread, debugMarker: int, eventKind: int, payload: System.Object, ) -> None:
        ...

    def GetCurrentThread(self, ) -> Microsoft.Scripting.Debugging.DebugThread:
        ...

    def GeneratorLoopProc(self, frame: Microsoft.Scripting.Debugging.DebugFrame, moveNext: ref[bool], ) -> System.Object:
        ...

class DebugLambdaInfo(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def CompilerSupport(self) -> Microsoft.Scripting.Debugging.CompilerServices.IDebugCompilerSupport:
        ...

    @property
    def LambdaAlias(self) -> str:
        ...

    @property
    def HiddenVariables(self) -> System.Collections.Generic.IList[System.Linq.Expressions.ParameterExpression]:
        ...

    @property
    def VariableAliases(self) -> System.Collections.Generic.IDictionary[System.Linq.Expressions.ParameterExpression, str]:
        ...

    @property
    def CustomPayload(self) -> System.Object:
        ...

    @property
    def OptimizeForLeafFrames(self) -> bool:
        ...

    # methods
    def __init__(self, compilerSupport: Microsoft.Scripting.Debugging.CompilerServices.IDebugCompilerSupport, lambdaAlias: str, optimizeForLeafFrames: bool, hiddenVariables: System.Collections.Generic.IList[System.Linq.Expressions.ParameterExpression], variableAliases: System.Collections.Generic.IDictionary[System.Linq.Expressions.ParameterExpression, str], customPayload: System.Object, ):
        ...

class IDebugCompilerSupport(abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    @abc.abstractmethod
    def DoesExpressionNeedReduction(self, expression: System.Linq.Expressions.Expression, ) -> bool:
        ...

    @abc.abstractmethod
    def QueueExpressionForReduction(self, expression: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.Expression:
        ...

    @abc.abstractmethod
    def IsCallToDebuggableLambda(self, expression: System.Linq.Expressions.Expression, ) -> bool:
        ...

