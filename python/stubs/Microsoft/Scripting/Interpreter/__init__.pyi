from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import Microsoft.Scripting.Interpreter
import System
import System.Runtime.CompilerServices
import Microsoft.Scripting.Utils
import System.Reflection
import System.Collections.Generic
import System.Diagnostics
import Microsoft.Scripting.Utils.ThreadLocal
import System.Linq.Expressions
import Microsoft.Scripting.Ast


class IInstructionProvider(abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    @abc.abstractmethod
    def AddInstructions(self, compiler: Microsoft.Scripting.Interpreter.LightCompiler, ) -> None:
        ...

class InterpretedFrame(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        self.Interpreter: Microsoft.Scripting.Interpreter.Interpreter
        self.Data: System.Array[System.Object]
        self.Closure: System.Array[System.Runtime.CompilerServices.StrongBox[System.Object]]
        self.StackIndex: int
        self.InstructionIndex: int
        self.CurrentAbortHandler: Microsoft.Scripting.Interpreter.ExceptionHandler
        ...

    # static fields
    CurrentFrame: Microsoft.Scripting.Utils.ThreadLocal[Microsoft.Scripting.Interpreter.InterpretedFrame] = ...

    # properties
    @property
    def Name(self) -> str:
        ...

    @property
    def Parent(self) -> Microsoft.Scripting.Interpreter.InterpretedFrame:
        ...
    @Parent.setter
    def Parent(self, val: Microsoft.Scripting.Interpreter.InterpretedFrame):
        ...

    @property
    def GotoMethod(self) -> System.Reflection.MethodInfo:
        ...

    @property
    def VoidGotoMethod(self) -> System.Reflection.MethodInfo:
        ...

    # methods
    def __init__(self, interpreter: Microsoft.Scripting.Interpreter.Interpreter, closure: System.Array[System.Runtime.CompilerServices.StrongBox[System.Object]], ):
        ...

    def GetDebugInfo(self, instructionIndex: int, ) -> Microsoft.Scripting.Interpreter.DebugInfo:
        ...

    @typing.overload
    def Push(self, value: System.Object, ) -> None:
        ...

    @typing.overload
    def Push(self, value: bool, ) -> None:
        ...

    @typing.overload
    def Push(self, value: int, ) -> None:
        ...

    @typing.overload
    def Pop(self, ) -> System.Object:
        ...

    @typing.overload
    def Pop(self, n: int, ) -> System.Object:
        ...

    def SetStackDepth(self, depth: int, ) -> None:
        ...

    def Peek(self, ) -> System.Object:
        ...

    def Dup(self, ) -> None:
        ...

    @staticmethod
    def IsInterpretedFrame(method: System.Reflection.MethodBase, ) -> bool:
        ...

    @staticmethod
    def GroupStackFrames(stackTrace: System.Collections.Generic.IEnumerable[System.Diagnostics.StackFrame], ) -> System.Collections.Generic.IEnumerable[System.Diagnostics.StackFrame]:
        ...

    def GetStackTraceDebugInfo(self, ) -> System.Collections.Generic.IEnumerable[Microsoft.Scripting.Interpreter.InterpretedFrameInfo]:
        ...

    def SaveTraceToException(self, exception: System.Exception, ) -> None:
        ...

    @staticmethod
    def GetExceptionStackTrace(exception: System.Exception, ) -> System.Array[Microsoft.Scripting.Interpreter.InterpretedFrameInfo]:
        ...

    def Enter(self, ) -> Microsoft.Scripting.Utils.ThreadLocal.StorageInfo[Microsoft.Scripting.Interpreter.InterpretedFrame]:
        ...

    def Leave(self, currentFrame: Microsoft.Scripting.Utils.ThreadLocal.StorageInfo[Microsoft.Scripting.Interpreter.InterpretedFrame], ) -> None:
        ...

    def RemoveContinuation(self, ) -> None:
        ...

    def PushContinuation(self, continuation: int, ) -> None:
        ...

    def YieldToCurrentContinuation(self, ) -> int:
        ...

    def YieldToPendingContinuation(self, ) -> int:
        ...

    def PushPendingContinuation(self, ) -> None:
        ...

    def PopPendingContinuation(self, ) -> None:
        ...

    def VoidGoto(self, labelIndex: int, ) -> int:
        ...

    def Goto(self, labelIndex: int, value: System.Object, ) -> int:
        ...

class ExceptionHandler(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        self.ExceptionType: System.Type
        self.StartIndex: int
        self.EndIndex: int
        self.LabelIndex: int
        self.HandlerStartIndex: int
        ...

    # static fields

    # properties
    @property
    def IsFault(self) -> bool:
        ...

    # methods
    def __init__(self, start: int, end: int, labelIndex: int, handlerStartIndex: int, exceptionType: System.Type, ):
        ...

    def Matches(self, exceptionType: System.Type, index: int, ) -> bool:
        ...

    def IsBetterThan(self, other: Microsoft.Scripting.Interpreter.ExceptionHandler, ) -> bool:
        ...

    def IsInside(self, index: int, ) -> bool:
        ...

    def ToString(self, ) -> str:
        ...

class Instruction(System.Object, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def ConsumedStack(self) -> int:
        ...

    @property
    def ProducedStack(self) -> int:
        ...

    @property
    def ConsumedContinuations(self) -> int:
        ...

    @property
    def ProducedContinuations(self) -> int:
        ...

    @property
    def StackBalance(self) -> int:
        ...

    @property
    def ContinuationsBalance(self) -> int:
        ...

    @property
    def InstructionName(self) -> str:
        ...

    # methods
    def __init__(self, ):
        ...

    @abc.abstractmethod
    def Run(self, frame: Microsoft.Scripting.Interpreter.InterpretedFrame, ) -> int:
        ...

    def ToString(self, ) -> str:
        ...

    def ToDebugString(self, instructionIndex: int, cookie: System.Object, labelIndexer: System.Func[int, int], objects: System.Collections.Generic.IList[System.Object], ) -> str:
        ...

    def GetDebugCookie(self, compiler: Microsoft.Scripting.Interpreter.LightCompiler, ) -> System.Object:
        ...

class LightCompiler(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields
    DefaultCompilationThreshold: int = ...

    # properties
    @property
    def Instructions(self) -> Microsoft.Scripting.Interpreter.InstructionList:
        ...

    @property
    def Locals(self) -> Microsoft.Scripting.Interpreter.LocalVariables:
        ...

    # methods
    @typing.overload
    def __init__(self, compilationThreshold: int, ):
        ...

    @typing.overload
    def __init__(self, parent: Microsoft.Scripting.Interpreter.LightCompiler, ):
        ...

    @staticmethod
    def Unbox(strongBoxExpression: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.Expression:
        ...

    @typing.overload
    def CompileTop(self, node: System.Linq.Expressions.LambdaExpression, ) -> Microsoft.Scripting.Interpreter.LightDelegateCreator:
        ...

    @typing.overload
    def CompileTop(self, node: Microsoft.Scripting.Ast.LightLambdaExpression, ) -> Microsoft.Scripting.Interpreter.LightDelegateCreator:
        ...

    def MakeInterpreter(self, lambdaName: str, ) -> Microsoft.Scripting.Interpreter.Interpreter:
        ...

    def CompileConstantExpression(self, expr: System.Linq.Expressions.Expression, ) -> None:
        ...

    @typing.overload
    def CompileDefaultExpression(self, expr: System.Linq.Expressions.Expression, ) -> None:
        ...

    @typing.overload
    def CompileDefaultExpression(self, type: System.Type, ) -> None:
        ...

    def EnsureAvailableForClosure(self, expr: System.Linq.Expressions.ParameterExpression, ) -> Microsoft.Scripting.Interpreter.LocalVariable:
        ...

    def EnsureVariable(self, variable: System.Linq.Expressions.ParameterExpression, ) -> None:
        ...

    def ResolveLocal(self, variable: System.Linq.Expressions.ParameterExpression, ) -> Microsoft.Scripting.Interpreter.LocalVariable:
        ...

    def CompileGetVariable(self, variable: System.Linq.Expressions.ParameterExpression, ) -> None:
        ...

    def CompileGetBoxedVariable(self, variable: System.Linq.Expressions.ParameterExpression, ) -> None:
        ...

    def CompileSetVariable(self, variable: System.Linq.Expressions.ParameterExpression, isVoid: bool, ) -> None:
        ...

    def CompileParameterExpression(self, expr: System.Linq.Expressions.Expression, ) -> None:
        ...

    def CompileBlockExpression(self, expr: System.Linq.Expressions.Expression, asVoid: bool, ) -> None:
        ...

    def CompileBlockStart(self, node: System.Linq.Expressions.BlockExpression, ) -> System.Array[Microsoft.Scripting.Interpreter.LocalDefinition]:
        ...

    def CompileBlockEnd(self, locals: System.Array[Microsoft.Scripting.Interpreter.LocalDefinition], ) -> None:
        ...

    def CompileIndexExpression(self, expr: System.Linq.Expressions.Expression, ) -> None:
        ...

    def CompileIndexAssignment(self, node: System.Linq.Expressions.BinaryExpression, asVoid: bool, ) -> None:
        ...

    def CompileMemberAssignment(self, node: System.Linq.Expressions.BinaryExpression, asVoid: bool, ) -> None:
        ...

    def CompileVariableAssignment(self, node: System.Linq.Expressions.BinaryExpression, asVoid: bool, ) -> None:
        ...

    def CompileAssignBinaryExpression(self, expr: System.Linq.Expressions.Expression, asVoid: bool, ) -> None:
        ...

    def CompileBinaryExpression(self, expr: System.Linq.Expressions.Expression, ) -> None:
        ...

    def CompileEqual(self, left: System.Linq.Expressions.Expression, right: System.Linq.Expressions.Expression, ) -> None:
        ...

    def CompileNotEqual(self, left: System.Linq.Expressions.Expression, right: System.Linq.Expressions.Expression, ) -> None:
        ...

    def CompileComparison(self, nodeType: int, left: System.Linq.Expressions.Expression, right: System.Linq.Expressions.Expression, ) -> None:
        ...

    def CompileArithmetic(self, nodeType: int, left: System.Linq.Expressions.Expression, right: System.Linq.Expressions.Expression, ) -> None:
        ...

    def CompileConvertUnaryExpression(self, expr: System.Linq.Expressions.Expression, ) -> None:
        ...

    def CompileConvertToType(self, typeFrom: System.Type, typeTo: System.Type, isChecked: bool, ) -> None:
        ...

    def CompileNotExpression(self, node: System.Linq.Expressions.UnaryExpression, ) -> None:
        ...

    def CompileUnaryExpression(self, expr: System.Linq.Expressions.Expression, ) -> None:
        ...

    def CompileAndAlsoBinaryExpression(self, expr: System.Linq.Expressions.Expression, ) -> None:
        ...

    def CompileOrElseBinaryExpression(self, expr: System.Linq.Expressions.Expression, ) -> None:
        ...

    def CompileLogicalBinaryExpression(self, expr: System.Linq.Expressions.Expression, andAlso: bool, ) -> None:
        ...

    def CompileConditionalExpression(self, expr: System.Linq.Expressions.Expression, asVoid: bool, ) -> None:
        ...

    def CompileLoopExpression(self, expr: System.Linq.Expressions.Expression, ) -> None:
        ...

    def CompileSwitchExpression(self, expr: System.Linq.Expressions.Expression, ) -> None:
        ...

    def CompileLabelExpression(self, expr: System.Linq.Expressions.Expression, ) -> None:
        ...

    def CompileGotoExpression(self, expr: System.Linq.Expressions.Expression, ) -> None:
        ...

    def GetBranchLabel(self, target: System.Linq.Expressions.LabelTarget, ) -> Microsoft.Scripting.Interpreter.BranchLabel:
        ...

    def PushLabelBlock(self, type: int, ) -> None:
        ...

    def PopLabelBlock(self, kind: int, ) -> None:
        ...

    def EnsureLabel(self, node: System.Linq.Expressions.LabelTarget, ) -> Microsoft.Scripting.Interpreter.LabelInfo:
        ...

    def ReferenceLabel(self, node: System.Linq.Expressions.LabelTarget, ) -> Microsoft.Scripting.Interpreter.LabelInfo:
        ...

    def DefineLabel(self, node: System.Linq.Expressions.LabelTarget, ) -> Microsoft.Scripting.Interpreter.LabelInfo:
        ...

    def TryPushLabelBlock(self, node: System.Linq.Expressions.Expression, ) -> bool:
        ...

    def DefineBlockLabels(self, node: System.Linq.Expressions.Expression, ) -> None:
        ...

    def GetBranchMapping(self, ) -> Microsoft.Scripting.Utils.HybridReferenceDictionary[System.Linq.Expressions.LabelTarget, Microsoft.Scripting.Interpreter.BranchLabel]:
        ...

    def CompileThrowUnaryExpression(self, expr: System.Linq.Expressions.Expression, asVoid: bool, ) -> None:
        ...

    def EndsWithRethrow(self, expr: System.Linq.Expressions.Expression, ) -> bool:
        ...

    def CompileAsVoidRemoveRethrow(self, expr: System.Linq.Expressions.Expression, ) -> None:
        ...

    def CompileTryExpression(self, expr: System.Linq.Expressions.Expression, ) -> None:
        ...

    def CompileDynamicExpression(self, expr: System.Linq.Expressions.Expression, ) -> None:
        ...

    def CompileMethodCallExpression(self, expr: System.Linq.Expressions.Expression, ) -> None:
        ...

    @typing.overload
    def EmitCall(self, method: System.Reflection.MethodInfo, ) -> None:
        ...

    @typing.overload
    def EmitCall(self, method: System.Reflection.MethodInfo, parameters: System.Array[System.Reflection.ParameterInfo], ) -> None:
        ...

    def CompileNewExpression(self, expr: System.Linq.Expressions.Expression, ) -> None:
        ...

    def CompileMemberExpression(self, expr: System.Linq.Expressions.Expression, ) -> None:
        ...

    def CompileNewArrayExpression(self, expr: System.Linq.Expressions.Expression, ) -> None:
        ...

    def CompileExtensionExpression(self, expr: System.Linq.Expressions.Expression, ) -> None:
        ...

    def CompileDebugInfoExpression(self, expr: System.Linq.Expressions.Expression, ) -> None:
        ...

    def CompileRuntimeVariablesExpression(self, expr: System.Linq.Expressions.Expression, ) -> None:
        ...

    def CompileLambdaExpression(self, expr: System.Linq.Expressions.Expression, ) -> None:
        ...

    def CompileCoalesceBinaryExpression(self, expr: System.Linq.Expressions.Expression, ) -> None:
        ...

    def CompileInvocationExpression(self, expr: System.Linq.Expressions.Expression, ) -> None:
        ...

    def CompileListInitExpression(self, expr: System.Linq.Expressions.Expression, ) -> None:
        ...

    def CompileMemberInitExpression(self, expr: System.Linq.Expressions.Expression, ) -> None:
        ...

    def CompileQuoteUnaryExpression(self, expr: System.Linq.Expressions.Expression, ) -> None:
        ...

    def CompileUnboxUnaryExpression(self, expr: System.Linq.Expressions.Expression, ) -> None:
        ...

    def CompileTypeEqualExpression(self, expr: System.Linq.Expressions.Expression, ) -> None:
        ...

    def CompileTypeAsExpression(self, node: System.Linq.Expressions.UnaryExpression, ) -> None:
        ...

    def CompileTypeIsExpression(self, expr: System.Linq.Expressions.Expression, ) -> None:
        ...

    def CompileReducibleExpression(self, expr: System.Linq.Expressions.Expression, ) -> None:
        ...

    @typing.overload
    def Compile(self, expr: System.Linq.Expressions.Expression, asVoid: bool, ) -> None:
        ...

    @typing.overload
    def Compile(self, expr: System.Linq.Expressions.Expression, ) -> None:
        ...

    def CompileAsVoid(self, expr: System.Linq.Expressions.Expression, ) -> None:
        ...

    def CompileNoLabelPush(self, expr: System.Linq.Expressions.Expression, ) -> None:
        ...

class LocalVariable(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        self.Index: int
        ...

    # static fields

    # properties
    @property
    def IsBoxed(self) -> bool:
        ...
    @IsBoxed.setter
    def IsBoxed(self, val: bool):
        ...

    @property
    def InClosure(self) -> bool:
        ...

    @property
    def InClosureOrBoxed(self) -> bool:
        ...

    # methods
    def __init__(self, index: int, closure: bool, boxed: bool, ):
        ...

    def LoadFromArray(self, frameData: System.Linq.Expressions.Expression, closure: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.Expression:
        ...

    def ToString(self, ) -> str:
        ...

class LabelScopeKind(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    Statement: int = ...
    Block: int = ...
    Switch: int = ...
    Lambda: int = ...
    Try: int = ...
    Catch: int = ...
    Finally: int = ...
    Filter: int = ...
    Expression: int = ...

class InstructionList(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def Count(self) -> int:
        ...

    @property
    def CurrentStackDepth(self) -> int:
        ...

    @property
    def CurrentContinuationsDepth(self) -> int:
        ...

    @property
    def MaxStackDepth(self) -> int:
        ...

    # methods
    def __init__(self, ):
        ...

    @typing.overload
    def EmitDynamic(self, binder: System.Runtime.CompilerServices.CallSiteBinder, ) -> None:
        ...

    @typing.overload
    def EmitDynamic(self, binder: System.Runtime.CompilerServices.CallSiteBinder, ) -> None:
        ...

    @typing.overload
    def EmitDynamic(self, type: System.Type, binder: System.Runtime.CompilerServices.CallSiteBinder, ) -> None:
        ...

    @typing.overload
    def EmitDynamic(self, binder: System.Runtime.CompilerServices.CallSiteBinder, ) -> None:
        ...

    @typing.overload
    def EmitDynamic(self, binder: System.Runtime.CompilerServices.CallSiteBinder, ) -> None:
        ...

    @typing.overload
    def EmitDynamic(self, binder: System.Runtime.CompilerServices.CallSiteBinder, ) -> None:
        ...

    @typing.overload
    def EmitDynamic(self, binder: System.Runtime.CompilerServices.CallSiteBinder, ) -> None:
        ...

    @typing.overload
    def EmitDynamic(self, binder: System.Runtime.CompilerServices.CallSiteBinder, ) -> None:
        ...

    @typing.overload
    def EmitDynamic(self, binder: System.Runtime.CompilerServices.CallSiteBinder, ) -> None:
        ...

    @typing.overload
    def EmitDynamic(self, binder: System.Runtime.CompilerServices.CallSiteBinder, ) -> None:
        ...

    @typing.overload
    def EmitDynamic(self, binder: System.Runtime.CompilerServices.CallSiteBinder, ) -> None:
        ...

    @typing.overload
    def EmitDynamic(self, binder: System.Runtime.CompilerServices.CallSiteBinder, ) -> None:
        ...

    @typing.overload
    def EmitDynamic(self, binder: System.Runtime.CompilerServices.CallSiteBinder, ) -> None:
        ...

    @typing.overload
    def EmitDynamic(self, binder: System.Runtime.CompilerServices.CallSiteBinder, ) -> None:
        ...

    @typing.overload
    def EmitDynamic(self, binder: System.Runtime.CompilerServices.CallSiteBinder, ) -> None:
        ...

    @typing.overload
    def EmitDynamic(self, binder: System.Runtime.CompilerServices.CallSiteBinder, ) -> None:
        ...

    @staticmethod
    def CreateDynamicInstruction(delegateType: System.Type, binder: System.Runtime.CompilerServices.CallSiteBinder, ) -> Microsoft.Scripting.Interpreter.Instruction:
        ...

    def BuildRuntimeLabels(self, ) -> System.Array[Microsoft.Scripting.Interpreter.RuntimeLabel]:
        ...

    def MakeLabel(self, ) -> Microsoft.Scripting.Interpreter.BranchLabel:
        ...

    def FixupBranch(self, branchIndex: int, offset: int, ) -> None:
        ...

    def EnsureLabelIndex(self, label: Microsoft.Scripting.Interpreter.BranchLabel, ) -> int:
        ...

    def MarkRuntimeLabel(self, ) -> int:
        ...

    def MarkLabel(self, label: Microsoft.Scripting.Interpreter.BranchLabel, ) -> None:
        ...

    def EmitGoto(self, label: Microsoft.Scripting.Interpreter.BranchLabel, hasResult: bool, hasValue: bool, ) -> None:
        ...

    @typing.overload
    def EmitBranch(self, instruction: Microsoft.Scripting.Interpreter.OffsetInstruction, label: Microsoft.Scripting.Interpreter.BranchLabel, ) -> None:
        ...

    @typing.overload
    def EmitBranch(self, label: Microsoft.Scripting.Interpreter.BranchLabel, ) -> None:
        ...

    @typing.overload
    def EmitBranch(self, label: Microsoft.Scripting.Interpreter.BranchLabel, hasResult: bool, hasValue: bool, ) -> None:
        ...

    def EmitCoalescingBranch(self, leftNotNull: Microsoft.Scripting.Interpreter.BranchLabel, ) -> None:
        ...

    def EmitBranchTrue(self, elseLabel: Microsoft.Scripting.Interpreter.BranchLabel, ) -> None:
        ...

    def EmitBranchFalse(self, elseLabel: Microsoft.Scripting.Interpreter.BranchLabel, ) -> None:
        ...

    def EmitThrow(self, ) -> None:
        ...

    def EmitThrowVoid(self, ) -> None:
        ...

    def EmitRethrow(self, ) -> None:
        ...

    def EmitRethrowVoid(self, ) -> None:
        ...

    def EmitEnterTryFinally(self, finallyStartLabel: Microsoft.Scripting.Interpreter.BranchLabel, ) -> None:
        ...

    def EmitEnterFinally(self, ) -> None:
        ...

    def EmitLeaveFinally(self, ) -> None:
        ...

    def EmitLeaveFault(self, hasValue: bool, ) -> None:
        ...

    def EmitEnterExceptionHandlerNonVoid(self, ) -> None:
        ...

    def EmitEnterExceptionHandlerVoid(self, ) -> None:
        ...

    def EmitLeaveExceptionHandler(self, hasValue: bool, tryExpressionEndLabel: Microsoft.Scripting.Interpreter.BranchLabel, ) -> None:
        ...

    def EmitSwitch(self, cases: System.Collections.Generic.Dictionary[int, int], ) -> None:
        ...

    def Emit(self, instruction: Microsoft.Scripting.Interpreter.Instruction, ) -> None:
        ...

    def UpdateStackDepth(self, instruction: Microsoft.Scripting.Interpreter.Instruction, ) -> None:
        ...

    def SetDebugCookie(self, cookie: System.Object, ) -> None:
        ...

    def GetInstruction(self, index: int, ) -> Microsoft.Scripting.Interpreter.Instruction:
        ...

    def ToArray(self, ) -> Microsoft.Scripting.Interpreter.InstructionArray:
        ...

    @typing.overload
    def EmitLoad(self, value: System.Object, ) -> None:
        ...

    @typing.overload
    def EmitLoad(self, value: bool, ) -> None:
        ...

    @typing.overload
    def EmitLoad(self, value: System.Object, type: System.Type, ) -> None:
        ...

    def EmitDup(self, ) -> None:
        ...

    def EmitPop(self, ) -> None:
        ...

    def SwitchToBoxed(self, index: int, instructionIndex: int, ) -> None:
        ...

    def EmitLoadLocal(self, index: int, ) -> None:
        ...

    def EmitLoadLocalBoxed(self, index: int, ) -> None:
        ...

    @staticmethod
    def LoadLocalBoxed(index: int, ) -> Microsoft.Scripting.Interpreter.Instruction:
        ...

    def EmitLoadLocalFromClosure(self, index: int, ) -> None:
        ...

    def EmitLoadLocalFromClosureBoxed(self, index: int, ) -> None:
        ...

    def EmitAssignLocal(self, index: int, ) -> None:
        ...

    def EmitStoreLocal(self, index: int, ) -> None:
        ...

    def EmitAssignLocalBoxed(self, index: int, ) -> None:
        ...

    @staticmethod
    def AssignLocalBoxed(index: int, ) -> Microsoft.Scripting.Interpreter.Instruction:
        ...

    def EmitStoreLocalBoxed(self, index: int, ) -> None:
        ...

    @staticmethod
    def StoreLocalBoxed(index: int, ) -> Microsoft.Scripting.Interpreter.Instruction:
        ...

    def EmitAssignLocalToClosure(self, index: int, ) -> None:
        ...

    def EmitStoreLocalToClosure(self, index: int, ) -> None:
        ...

    def EmitInitializeLocal(self, index: int, type: System.Type, ) -> None:
        ...

    def EmitInitializeParameter(self, index: int, ) -> None:
        ...

    @staticmethod
    def Parameter(index: int, ) -> Microsoft.Scripting.Interpreter.Instruction:
        ...

    @staticmethod
    def ParameterBox(index: int, ) -> Microsoft.Scripting.Interpreter.Instruction:
        ...

    @staticmethod
    def InitReference(index: int, ) -> Microsoft.Scripting.Interpreter.Instruction:
        ...

    @staticmethod
    def InitImmutableRefBox(index: int, ) -> Microsoft.Scripting.Interpreter.Instruction:
        ...

    def EmitNewRuntimeVariables(self, count: int, ) -> None:
        ...

    def EmitGetArrayItem(self, arrayType: System.Type, ) -> None:
        ...

    def EmitSetArrayItem(self, arrayType: System.Type, ) -> None:
        ...

    def EmitNewArray(self, elementType: System.Type, ) -> None:
        ...

    def EmitNewArrayBounds(self, elementType: System.Type, rank: int, ) -> None:
        ...

    def EmitNewArrayInit(self, elementType: System.Type, elementCount: int, ) -> None:
        ...

    def EmitAdd(self, type: System.Type, checked: bool, ) -> None:
        ...

    def EmitSub(self, type: System.Type, checked: bool, ) -> None:
        ...

    def EmitMul(self, type: System.Type, checked: bool, ) -> None:
        ...

    def EmitDiv(self, type: System.Type, ) -> None:
        ...

    def EmitEqual(self, type: System.Type, ) -> None:
        ...

    def EmitNotEqual(self, type: System.Type, ) -> None:
        ...

    def EmitLessThan(self, type: System.Type, ) -> None:
        ...

    def EmitLessThanOrEqual(self, type: System.Type, ) -> None:
        ...

    def EmitGreaterThan(self, type: System.Type, ) -> None:
        ...

    def EmitGreaterThanOrEqual(self, type: System.Type, ) -> None:
        ...

    def EmitNumericConvertChecked(self, from_: int, to: int, ) -> None:
        ...

    def EmitNumericConvertUnchecked(self, from_: int, to: int, ) -> None:
        ...

    def EmitNot(self, ) -> None:
        ...

    def EmitDefaultValue(self, type: System.Type, ) -> None:
        ...

    def EmitNew(self, constructorInfo: System.Reflection.ConstructorInfo, ) -> None:
        ...

    def EmitCreateDelegate(self, creator: Microsoft.Scripting.Interpreter.LightDelegateCreator, ) -> None:
        ...

    def EmitTypeEquals(self, ) -> None:
        ...

    def EmitTypeIs(self, type: System.Type, ) -> None:
        ...

    def EmitTypeAs(self, type: System.Type, ) -> None:
        ...

    def EmitLoadField(self, field: System.Reflection.FieldInfo, ) -> None:
        ...

    def GetLoadField(self, field: System.Reflection.FieldInfo, ) -> Microsoft.Scripting.Interpreter.Instruction:
        ...

    def EmitStoreField(self, field: System.Reflection.FieldInfo, ) -> None:
        ...

class LocalVariables(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def LocalCount(self) -> int:
        ...

    @property
    def ClosureVariables(self) -> System.Collections.Generic.Dictionary[System.Linq.Expressions.ParameterExpression, Microsoft.Scripting.Interpreter.LocalVariable]:
        ...
    @ClosureVariables.setter
    def ClosureVariables(self, val: System.Collections.Generic.Dictionary[System.Linq.Expressions.ParameterExpression, Microsoft.Scripting.Interpreter.LocalVariable]):
        ...

    # methods
    def __init__(self, ):
        ...

    def DefineLocal(self, variable: System.Linq.Expressions.ParameterExpression, start: int, ) -> Microsoft.Scripting.Interpreter.LocalDefinition:
        ...

    def UndefineLocal(self, definition: Microsoft.Scripting.Interpreter.LocalDefinition, end: int, ) -> None:
        ...

    def Box(self, variable: System.Linq.Expressions.ParameterExpression, instructions: Microsoft.Scripting.Interpreter.InstructionList, ) -> None:
        ...

    def GetOrDefineLocal(self, var: System.Linq.Expressions.ParameterExpression, ) -> int:
        ...

    def GetLocalIndex(self, var: System.Linq.Expressions.ParameterExpression, ) -> int:
        ...

    def TryGetLocalOrClosure(self, var: System.Linq.Expressions.ParameterExpression, local: ref[Microsoft.Scripting.Interpreter.LocalVariable], ) -> bool:
        ...

    def CopyLocals(self, ) -> System.Collections.Generic.Dictionary[System.Linq.Expressions.ParameterExpression, Microsoft.Scripting.Interpreter.LocalVariable]:
        ...

    def ContainsVariable(self, variable: System.Linq.Expressions.ParameterExpression, ) -> bool:
        ...

    def AddClosureVariable(self, variable: System.Linq.Expressions.ParameterExpression, ) -> Microsoft.Scripting.Interpreter.LocalVariable:
        ...

class BranchLabel(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        self._labelIndex: int
        self._targetIndex: int
        self._stackDepth: int
        self._continuationStackDepth: int
        ...

    # static fields
    UnknownIndex: int = ...
    UnknownDepth: int = ...

    # properties
    @property
    def LabelIndex(self) -> int:
        ...
    @LabelIndex.setter
    def LabelIndex(self, val: int):
        ...

    @property
    def HasRuntimeLabel(self) -> bool:
        ...

    @property
    def TargetIndex(self) -> int:
        ...

    # methods
    def __init__(self, ):
        ...

    def ToRuntimeLabel(self, ) -> Microsoft.Scripting.Interpreter.RuntimeLabel:
        ...

    def Mark(self, instructions: Microsoft.Scripting.Interpreter.InstructionList, ) -> None:
        ...

    def AddBranch(self, instructions: Microsoft.Scripting.Interpreter.InstructionList, branchIndex: int, ) -> None:
        ...

    def FixupBranch(self, instructions: Microsoft.Scripting.Interpreter.InstructionList, branchIndex: int, ) -> None:
        ...

class LocalDefinition(System.IEquatable[Microsoft.Scripting.Interpreter.LocalDefinition], System.ValueType):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def Index(self) -> int:
        ...

    @property
    def Parameter(self) -> System.Linq.Expressions.ParameterExpression:
        ...

    # methods
    def __init__(self, localIndex: int, parameter: System.Linq.Expressions.ParameterExpression, ):
        ...

    @typing.overload
    def Equals(self, obj: System.Object, ) -> bool:
        ...

    @typing.overload
    def Equals(self, other: Microsoft.Scripting.Interpreter.LocalDefinition, ) -> bool:
        ...

    def GetHashCode(self, ) -> int:
        ...

class InstructionArray(System.ValueType):
    @typing.overload
    def __init__(self, **kwargs):
        self.MaxStackDepth: int
        self.MaxContinuationDepth: int
        self.Instructions: System.Array[Microsoft.Scripting.Interpreter.Instruction]
        self.Objects: System.Array[System.Object]
        self.Labels: System.Array[Microsoft.Scripting.Interpreter.RuntimeLabel]
        self.DebugCookies: System.Collections.Generic.List[System.Collections.Generic.KeyValuePair[int, System.Object]]
        ...

    # static fields

    # properties
    @property
    def Length(self) -> int:
        ...

    # methods
    def __init__(self, maxStackDepth: int, maxContinuationDepth: int, instructions: System.Array[Microsoft.Scripting.Interpreter.Instruction], objects: System.Array[System.Object], labels: System.Array[Microsoft.Scripting.Interpreter.RuntimeLabel], debugCookies: System.Collections.Generic.List[System.Collections.Generic.KeyValuePair[int, System.Object]], ):
        ...

class InterpretedFrameInfo(System.ValueType):
    @typing.overload
    def __init__(self, **kwargs):
        self.MethodName: str
        self.DebugInfo: Microsoft.Scripting.Interpreter.DebugInfo
        ...

    # static fields

    # properties
    # methods
    def __init__(self, methodName: str, info: Microsoft.Scripting.Interpreter.DebugInfo, ):
        ...

    def ToString(self, ) -> str:
        ...

class DebugInfo(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        self.StartLine: int
        self.EndLine: int
        self.Index: int
        self.FileName: str
        self.IsClear: bool
        ...

    # static fields

    # properties
    # methods
    def __init__(self, ):
        ...

    @staticmethod
    def GetMatchingDebugInfo(debugInfos: System.Array[Microsoft.Scripting.Interpreter.DebugInfo], index: int, ) -> Microsoft.Scripting.Interpreter.DebugInfo:
        ...

    def ToString(self, ) -> str:
        ...

class LightLambdaCompileEventArgs(System.EventArgs):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def Compiled(self) -> System.Delegate:
        ...

    # methods
    def __init__(self, compiled: System.Delegate, ):
        ...

