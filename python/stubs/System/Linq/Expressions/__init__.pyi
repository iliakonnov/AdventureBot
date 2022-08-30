from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import System.Linq.Expressions
import System
import System.Collections.ObjectModel
import System.Collections.Generic
import System.Runtime.CompilerServices
import System.Reflection

TDelegate = typing.TypeVar('TDelegate')

class Expression(System.Linq.Expressions.IParameterProvider, System.Linq.Expressions.LambdaExpression, typing.Generic[TDelegate]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def Type(self) -> System.Type:
        ...

    @property
    def NodeType(self) -> System.Linq.Expressions.ExpressionType:
        ...

    @property
    def Parameters(self) -> System.Collections.ObjectModel.ReadOnlyCollection[System.Linq.Expressions.ParameterExpression]:
        ...

    @property
    def Name(self) -> System.String:
        ...

    @property
    def Body(self) -> System.Linq.Expressions.Expression:
        ...

    @property
    def ReturnType(self) -> System.Type:
        ...

    @property
    def TailCall(self) -> System.Boolean:
        ...

    @property
    def CanReduce(self) -> System.Boolean:
        ...

    # methods
    @typing.overload
    def Compile(self, ) -> TDelegate:
        ...

    @typing.overload
    def Compile(self, preferInterpretation: System.Boolean, ) -> TDelegate:
        ...

    @typing.overload
    def Update(self, body: System.Linq.Expressions.Expression, parameters: System.Collections.Generic.IEnumerable[System.Linq.Expressions.ParameterExpression], ) -> System.Linq.Expressions.Expression:
        ...

    @typing.overload
    def Compile(self, debugInfoGenerator: System.Runtime.CompilerServices.DebugInfoGenerator, ) -> TDelegate:
        ...

class LambdaExpression(System.Linq.Expressions.IParameterProvider, System.Linq.Expressions.Expression, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def Type(self) -> System.Type:
        ...

    @property
    def NodeType(self) -> System.Linq.Expressions.ExpressionType:
        ...

    @property
    def Parameters(self) -> System.Collections.ObjectModel.ReadOnlyCollection[System.Linq.Expressions.ParameterExpression]:
        ...

    @property
    def Name(self) -> System.String:
        ...

    @property
    def Body(self) -> System.Linq.Expressions.Expression:
        ...

    @property
    def ReturnType(self) -> System.Type:
        ...

    @property
    def TailCall(self) -> System.Boolean:
        ...

    @property
    def CanReduce(self) -> System.Boolean:
        ...

    # methods
    @typing.overload
    def Compile(self, ) -> System.Delegate:
        ...

    @typing.overload
    def Compile(self, preferInterpretation: System.Boolean, ) -> System.Delegate:
        ...

    @typing.overload
    def Compile(self, debugInfoGenerator: System.Runtime.CompilerServices.DebugInfoGenerator, ) -> System.Delegate:
        ...

class ExpressionType(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    Add: System.Int32 = Add
    AddChecked: System.Int32 = AddChecked
    And: System.Int32 = And
    AndAlso: System.Int32 = AndAlso
    ArrayLength: System.Int32 = ArrayLength
    ArrayIndex: System.Int32 = ArrayIndex
    Call: System.Int32 = Call
    Coalesce: System.Int32 = Coalesce
    Conditional: System.Int32 = Conditional
    Constant: System.Int32 = Constant
    Convert: System.Int32 = Convert
    ConvertChecked: System.Int32 = ConvertChecked
    Divide: System.Int32 = Divide
    Equal: System.Int32 = Equal
    ExclusiveOr: System.Int32 = ExclusiveOr
    GreaterThan: System.Int32 = GreaterThan
    GreaterThanOrEqual: System.Int32 = GreaterThanOrEqual
    Invoke: System.Int32 = Invoke
    Lambda: System.Int32 = Lambda
    LeftShift: System.Int32 = LeftShift
    LessThan: System.Int32 = LessThan
    LessThanOrEqual: System.Int32 = LessThanOrEqual
    ListInit: System.Int32 = ListInit
    MemberAccess: System.Int32 = MemberAccess
    MemberInit: System.Int32 = MemberInit
    Modulo: System.Int32 = Modulo
    Multiply: System.Int32 = Multiply
    MultiplyChecked: System.Int32 = MultiplyChecked
    Negate: System.Int32 = Negate
    UnaryPlus: System.Int32 = UnaryPlus
    NegateChecked: System.Int32 = NegateChecked
    New: System.Int32 = New
    NewArrayInit: System.Int32 = NewArrayInit
    NewArrayBounds: System.Int32 = NewArrayBounds
    Not: System.Int32 = Not
    NotEqual: System.Int32 = NotEqual
    Or: System.Int32 = Or
    OrElse: System.Int32 = OrElse
    Parameter: System.Int32 = Parameter
    Power: System.Int32 = Power
    Quote: System.Int32 = Quote
    RightShift: System.Int32 = RightShift
    Subtract: System.Int32 = Subtract
    SubtractChecked: System.Int32 = SubtractChecked
    TypeAs: System.Int32 = TypeAs
    TypeIs: System.Int32 = TypeIs
    Assign: System.Int32 = Assign
    Block: System.Int32 = Block
    DebugInfo: System.Int32 = DebugInfo
    Decrement: System.Int32 = Decrement
    Dynamic: System.Int32 = Dynamic
    Default: System.Int32 = Default
    Extension: System.Int32 = Extension
    Goto: System.Int32 = Goto
    Increment: System.Int32 = Increment
    Index: System.Int32 = Index
    Label: System.Int32 = Label
    RuntimeVariables: System.Int32 = RuntimeVariables
    Loop: System.Int32 = Loop
    Switch: System.Int32 = Switch
    Throw: System.Int32 = Throw
    Try: System.Int32 = Try
    Unbox: System.Int32 = Unbox
    AddAssign: System.Int32 = AddAssign
    AndAssign: System.Int32 = AndAssign
    DivideAssign: System.Int32 = DivideAssign
    ExclusiveOrAssign: System.Int32 = ExclusiveOrAssign
    LeftShiftAssign: System.Int32 = LeftShiftAssign
    ModuloAssign: System.Int32 = ModuloAssign
    MultiplyAssign: System.Int32 = MultiplyAssign
    OrAssign: System.Int32 = OrAssign
    PowerAssign: System.Int32 = PowerAssign
    RightShiftAssign: System.Int32 = RightShiftAssign
    SubtractAssign: System.Int32 = SubtractAssign
    AddAssignChecked: System.Int32 = AddAssignChecked
    MultiplyAssignChecked: System.Int32 = MultiplyAssignChecked
    SubtractAssignChecked: System.Int32 = SubtractAssignChecked
    PreIncrementAssign: System.Int32 = PreIncrementAssign
    PreDecrementAssign: System.Int32 = PreDecrementAssign
    PostIncrementAssign: System.Int32 = PostIncrementAssign
    PostDecrementAssign: System.Int32 = PostDecrementAssign
    TypeEqual: System.Int32 = TypeEqual
    OnesComplement: System.Int32 = OnesComplement
    IsTrue: System.Int32 = IsTrue
    IsFalse: System.Int32 = IsFalse

class ParameterExpression(System.Linq.Expressions.Expression):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def Type(self) -> System.Type:
        ...

    @property
    def NodeType(self) -> System.Linq.Expressions.ExpressionType:
        ...

    @property
    def Name(self) -> System.String:
        ...

    @property
    def IsByRef(self) -> System.Boolean:
        ...

    @property
    def CanReduce(self) -> System.Boolean:
        ...

    # methods
class Expression(System.Object, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def NodeType(self) -> System.Linq.Expressions.ExpressionType:
        ...

    @property
    def Type(self) -> System.Type:
        ...

    @property
    def CanReduce(self) -> System.Boolean:
        ...

    # methods
    @typing.overload
    @staticmethod
    def Switch(type: System.Type, switchValue: System.Linq.Expressions.Expression, defaultBody: System.Linq.Expressions.Expression, comparison: System.Reflection.MethodInfo, cases: list[System.Linq.Expressions.SwitchCase], ) -> System.Linq.Expressions.SwitchExpression:
        ...

    @typing.overload
    @staticmethod
    def Switch(switchValue: System.Linq.Expressions.Expression, defaultBody: System.Linq.Expressions.Expression, comparison: System.Reflection.MethodInfo, cases: System.Collections.Generic.IEnumerable[System.Linq.Expressions.SwitchCase], ) -> System.Linq.Expressions.SwitchExpression:
        ...

    @typing.overload
    @staticmethod
    def Switch(type: System.Type, switchValue: System.Linq.Expressions.Expression, defaultBody: System.Linq.Expressions.Expression, comparison: System.Reflection.MethodInfo, cases: System.Collections.Generic.IEnumerable[System.Linq.Expressions.SwitchCase], ) -> System.Linq.Expressions.SwitchExpression:
        ...

    @typing.overload
    @staticmethod
    def SymbolDocument(fileName: System.String, ) -> System.Linq.Expressions.SymbolDocumentInfo:
        ...

    @typing.overload
    @staticmethod
    def SymbolDocument(fileName: System.String, language: System.Guid, ) -> System.Linq.Expressions.SymbolDocumentInfo:
        ...

    @typing.overload
    @staticmethod
    def SymbolDocument(fileName: System.String, language: System.Guid, languageVendor: System.Guid, ) -> System.Linq.Expressions.SymbolDocumentInfo:
        ...

    @typing.overload
    @staticmethod
    def SymbolDocument(fileName: System.String, language: System.Guid, languageVendor: System.Guid, documentType: System.Guid, ) -> System.Linq.Expressions.SymbolDocumentInfo:
        ...

    @typing.overload
    @staticmethod
    def TryFault(body: System.Linq.Expressions.Expression, fault: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.TryExpression:
        ...

    @typing.overload
    @staticmethod
    def TryFinally(body: System.Linq.Expressions.Expression, finally_: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.TryExpression:
        ...

    @typing.overload
    @staticmethod
    def TryCatch(body: System.Linq.Expressions.Expression, handlers: list[System.Linq.Expressions.CatchBlock], ) -> System.Linq.Expressions.TryExpression:
        ...

    @typing.overload
    @staticmethod
    def TryCatchFinally(body: System.Linq.Expressions.Expression, finally_: System.Linq.Expressions.Expression, handlers: list[System.Linq.Expressions.CatchBlock], ) -> System.Linq.Expressions.TryExpression:
        ...

    @typing.overload
    @staticmethod
    def MakeTry(type: System.Type, body: System.Linq.Expressions.Expression, finally_: System.Linq.Expressions.Expression, fault: System.Linq.Expressions.Expression, handlers: System.Collections.Generic.IEnumerable[System.Linq.Expressions.CatchBlock], ) -> System.Linq.Expressions.TryExpression:
        ...

    @typing.overload
    @staticmethod
    def TypeIs(expression: System.Linq.Expressions.Expression, type: System.Type, ) -> System.Linq.Expressions.TypeBinaryExpression:
        ...

    @typing.overload
    @staticmethod
    def TypeEqual(expression: System.Linq.Expressions.Expression, type: System.Type, ) -> System.Linq.Expressions.TypeBinaryExpression:
        ...

    @typing.overload
    @staticmethod
    def MakeUnary(unaryType: System.Linq.Expressions.ExpressionType, operand: System.Linq.Expressions.Expression, type: System.Type, ) -> System.Linq.Expressions.UnaryExpression:
        ...

    @typing.overload
    @staticmethod
    def MakeUnary(unaryType: System.Linq.Expressions.ExpressionType, operand: System.Linq.Expressions.Expression, type: System.Type, method: System.Reflection.MethodInfo, ) -> System.Linq.Expressions.UnaryExpression:
        ...

    @typing.overload
    @staticmethod
    def Negate(expression: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.UnaryExpression:
        ...

    @typing.overload
    @staticmethod
    def Negate(expression: System.Linq.Expressions.Expression, method: System.Reflection.MethodInfo, ) -> System.Linq.Expressions.UnaryExpression:
        ...

    @typing.overload
    @staticmethod
    def UnaryPlus(expression: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.UnaryExpression:
        ...

    @typing.overload
    @staticmethod
    def UnaryPlus(expression: System.Linq.Expressions.Expression, method: System.Reflection.MethodInfo, ) -> System.Linq.Expressions.UnaryExpression:
        ...

    @typing.overload
    @staticmethod
    def NegateChecked(expression: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.UnaryExpression:
        ...

    @typing.overload
    @staticmethod
    def NegateChecked(expression: System.Linq.Expressions.Expression, method: System.Reflection.MethodInfo, ) -> System.Linq.Expressions.UnaryExpression:
        ...

    @typing.overload
    @staticmethod
    def Not(expression: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.UnaryExpression:
        ...

    @typing.overload
    @staticmethod
    def Not(expression: System.Linq.Expressions.Expression, method: System.Reflection.MethodInfo, ) -> System.Linq.Expressions.UnaryExpression:
        ...

    @typing.overload
    @staticmethod
    def IsFalse(expression: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.UnaryExpression:
        ...

    @typing.overload
    @staticmethod
    def IsFalse(expression: System.Linq.Expressions.Expression, method: System.Reflection.MethodInfo, ) -> System.Linq.Expressions.UnaryExpression:
        ...

    @typing.overload
    @staticmethod
    def IsTrue(expression: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.UnaryExpression:
        ...

    @typing.overload
    @staticmethod
    def IsTrue(expression: System.Linq.Expressions.Expression, method: System.Reflection.MethodInfo, ) -> System.Linq.Expressions.UnaryExpression:
        ...

    @typing.overload
    @staticmethod
    def OnesComplement(expression: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.UnaryExpression:
        ...

    @typing.overload
    @staticmethod
    def OnesComplement(expression: System.Linq.Expressions.Expression, method: System.Reflection.MethodInfo, ) -> System.Linq.Expressions.UnaryExpression:
        ...

    @typing.overload
    @staticmethod
    def TypeAs(expression: System.Linq.Expressions.Expression, type: System.Type, ) -> System.Linq.Expressions.UnaryExpression:
        ...

    @typing.overload
    @staticmethod
    def Unbox(expression: System.Linq.Expressions.Expression, type: System.Type, ) -> System.Linq.Expressions.UnaryExpression:
        ...

    @typing.overload
    @staticmethod
    def Convert(expression: System.Linq.Expressions.Expression, type: System.Type, ) -> System.Linq.Expressions.UnaryExpression:
        ...

    @typing.overload
    @staticmethod
    def Convert(expression: System.Linq.Expressions.Expression, type: System.Type, method: System.Reflection.MethodInfo, ) -> System.Linq.Expressions.UnaryExpression:
        ...

    @typing.overload
    @staticmethod
    def ConvertChecked(expression: System.Linq.Expressions.Expression, type: System.Type, ) -> System.Linq.Expressions.UnaryExpression:
        ...

    @typing.overload
    @staticmethod
    def ConvertChecked(expression: System.Linq.Expressions.Expression, type: System.Type, method: System.Reflection.MethodInfo, ) -> System.Linq.Expressions.UnaryExpression:
        ...

    @typing.overload
    @staticmethod
    def ArrayLength(array: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.UnaryExpression:
        ...

    @typing.overload
    @staticmethod
    def Quote(expression: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.UnaryExpression:
        ...

    @typing.overload
    @staticmethod
    def Rethrow() -> System.Linq.Expressions.UnaryExpression:
        ...

    @typing.overload
    @staticmethod
    def Rethrow(type: System.Type, ) -> System.Linq.Expressions.UnaryExpression:
        ...

    @typing.overload
    @staticmethod
    def Throw(value: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.UnaryExpression:
        ...

    @typing.overload
    @staticmethod
    def Throw(value: System.Linq.Expressions.Expression, type: System.Type, ) -> System.Linq.Expressions.UnaryExpression:
        ...

    @typing.overload
    @staticmethod
    def Increment(expression: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.UnaryExpression:
        ...

    @typing.overload
    @staticmethod
    def Increment(expression: System.Linq.Expressions.Expression, method: System.Reflection.MethodInfo, ) -> System.Linq.Expressions.UnaryExpression:
        ...

    @typing.overload
    @staticmethod
    def Decrement(expression: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.UnaryExpression:
        ...

    @typing.overload
    @staticmethod
    def Decrement(expression: System.Linq.Expressions.Expression, method: System.Reflection.MethodInfo, ) -> System.Linq.Expressions.UnaryExpression:
        ...

    @typing.overload
    @staticmethod
    def PreIncrementAssign(expression: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.UnaryExpression:
        ...

    @typing.overload
    @staticmethod
    def PreIncrementAssign(expression: System.Linq.Expressions.Expression, method: System.Reflection.MethodInfo, ) -> System.Linq.Expressions.UnaryExpression:
        ...

    @typing.overload
    @staticmethod
    def PreDecrementAssign(expression: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.UnaryExpression:
        ...

    @typing.overload
    @staticmethod
    def PreDecrementAssign(expression: System.Linq.Expressions.Expression, method: System.Reflection.MethodInfo, ) -> System.Linq.Expressions.UnaryExpression:
        ...

    @typing.overload
    @staticmethod
    def PostIncrementAssign(expression: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.UnaryExpression:
        ...

    @typing.overload
    @staticmethod
    def PostIncrementAssign(expression: System.Linq.Expressions.Expression, method: System.Reflection.MethodInfo, ) -> System.Linq.Expressions.UnaryExpression:
        ...

    @typing.overload
    @staticmethod
    def PostDecrementAssign(expression: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.UnaryExpression:
        ...

    @typing.overload
    @staticmethod
    def PostDecrementAssign(expression: System.Linq.Expressions.Expression, method: System.Reflection.MethodInfo, ) -> System.Linq.Expressions.UnaryExpression:
        ...

    @typing.overload
    @staticmethod
    def ListInit(newExpression: System.Linq.Expressions.NewExpression, initializers: System.Collections.Generic.IEnumerable[System.Linq.Expressions.ElementInit], ) -> System.Linq.Expressions.ListInitExpression:
        ...

    @typing.overload
    @staticmethod
    def Loop(body: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.LoopExpression:
        ...

    @typing.overload
    @staticmethod
    def Loop(body: System.Linq.Expressions.Expression, break_: System.Linq.Expressions.LabelTarget, ) -> System.Linq.Expressions.LoopExpression:
        ...

    @typing.overload
    @staticmethod
    def Loop(body: System.Linq.Expressions.Expression, break_: System.Linq.Expressions.LabelTarget, continue_: System.Linq.Expressions.LabelTarget, ) -> System.Linq.Expressions.LoopExpression:
        ...

    @typing.overload
    @staticmethod
    def Bind(member: System.Reflection.MemberInfo, expression: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.MemberAssignment:
        ...

    @typing.overload
    @staticmethod
    def Bind(propertyAccessor: System.Reflection.MethodInfo, expression: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.MemberAssignment:
        ...

    @typing.overload
    @staticmethod
    def Field(expression: System.Linq.Expressions.Expression, field: System.Reflection.FieldInfo, ) -> System.Linq.Expressions.MemberExpression:
        ...

    @typing.overload
    @staticmethod
    def Field(expression: System.Linq.Expressions.Expression, fieldName: System.String, ) -> System.Linq.Expressions.MemberExpression:
        ...

    @typing.overload
    @staticmethod
    def Field(expression: System.Linq.Expressions.Expression, type: System.Type, fieldName: System.String, ) -> System.Linq.Expressions.MemberExpression:
        ...

    @typing.overload
    @staticmethod
    def Property(expression: System.Linq.Expressions.Expression, propertyName: System.String, ) -> System.Linq.Expressions.MemberExpression:
        ...

    @typing.overload
    @staticmethod
    def Property(expression: System.Linq.Expressions.Expression, type: System.Type, propertyName: System.String, ) -> System.Linq.Expressions.MemberExpression:
        ...

    @typing.overload
    @staticmethod
    def Property(expression: System.Linq.Expressions.Expression, property: System.Reflection.PropertyInfo, ) -> System.Linq.Expressions.MemberExpression:
        ...

    @typing.overload
    @staticmethod
    def Property(expression: System.Linq.Expressions.Expression, propertyAccessor: System.Reflection.MethodInfo, ) -> System.Linq.Expressions.MemberExpression:
        ...

    @typing.overload
    @staticmethod
    def PropertyOrField(expression: System.Linq.Expressions.Expression, propertyOrFieldName: System.String, ) -> System.Linq.Expressions.MemberExpression:
        ...

    @typing.overload
    @staticmethod
    def MakeMemberAccess(expression: System.Linq.Expressions.Expression, member: System.Reflection.MemberInfo, ) -> System.Linq.Expressions.MemberExpression:
        ...

    @typing.overload
    @staticmethod
    def MemberInit(newExpression: System.Linq.Expressions.NewExpression, bindings: list[System.Linq.Expressions.MemberBinding], ) -> System.Linq.Expressions.MemberInitExpression:
        ...

    @typing.overload
    @staticmethod
    def MemberInit(newExpression: System.Linq.Expressions.NewExpression, bindings: System.Collections.Generic.IEnumerable[System.Linq.Expressions.MemberBinding], ) -> System.Linq.Expressions.MemberInitExpression:
        ...

    @typing.overload
    @staticmethod
    def ListBind(member: System.Reflection.MemberInfo, initializers: list[System.Linq.Expressions.ElementInit], ) -> System.Linq.Expressions.MemberListBinding:
        ...

    @typing.overload
    @staticmethod
    def ListBind(member: System.Reflection.MemberInfo, initializers: System.Collections.Generic.IEnumerable[System.Linq.Expressions.ElementInit], ) -> System.Linq.Expressions.MemberListBinding:
        ...

    @typing.overload
    @staticmethod
    def ListBind(propertyAccessor: System.Reflection.MethodInfo, initializers: list[System.Linq.Expressions.ElementInit], ) -> System.Linq.Expressions.MemberListBinding:
        ...

    @typing.overload
    @staticmethod
    def ListBind(propertyAccessor: System.Reflection.MethodInfo, initializers: System.Collections.Generic.IEnumerable[System.Linq.Expressions.ElementInit], ) -> System.Linq.Expressions.MemberListBinding:
        ...

    @typing.overload
    @staticmethod
    def MemberBind(member: System.Reflection.MemberInfo, bindings: list[System.Linq.Expressions.MemberBinding], ) -> System.Linq.Expressions.MemberMemberBinding:
        ...

    @typing.overload
    @staticmethod
    def MemberBind(member: System.Reflection.MemberInfo, bindings: System.Collections.Generic.IEnumerable[System.Linq.Expressions.MemberBinding], ) -> System.Linq.Expressions.MemberMemberBinding:
        ...

    @typing.overload
    @staticmethod
    def MemberBind(propertyAccessor: System.Reflection.MethodInfo, bindings: list[System.Linq.Expressions.MemberBinding], ) -> System.Linq.Expressions.MemberMemberBinding:
        ...

    @typing.overload
    @staticmethod
    def MemberBind(propertyAccessor: System.Reflection.MethodInfo, bindings: System.Collections.Generic.IEnumerable[System.Linq.Expressions.MemberBinding], ) -> System.Linq.Expressions.MemberMemberBinding:
        ...

    @typing.overload
    @staticmethod
    def Call(method: System.Reflection.MethodInfo, arg0: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.MethodCallExpression:
        ...

    @typing.overload
    @staticmethod
    def Call(method: System.Reflection.MethodInfo, arg0: System.Linq.Expressions.Expression, arg1: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.MethodCallExpression:
        ...

    @typing.overload
    @staticmethod
    def Call(method: System.Reflection.MethodInfo, arg0: System.Linq.Expressions.Expression, arg1: System.Linq.Expressions.Expression, arg2: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.MethodCallExpression:
        ...

    @typing.overload
    @staticmethod
    def Call(method: System.Reflection.MethodInfo, arg0: System.Linq.Expressions.Expression, arg1: System.Linq.Expressions.Expression, arg2: System.Linq.Expressions.Expression, arg3: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.MethodCallExpression:
        ...

    @typing.overload
    @staticmethod
    def Call(method: System.Reflection.MethodInfo, arg0: System.Linq.Expressions.Expression, arg1: System.Linq.Expressions.Expression, arg2: System.Linq.Expressions.Expression, arg3: System.Linq.Expressions.Expression, arg4: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.MethodCallExpression:
        ...

    @typing.overload
    @staticmethod
    def Call(method: System.Reflection.MethodInfo, arguments: list[System.Linq.Expressions.Expression], ) -> System.Linq.Expressions.MethodCallExpression:
        ...

    @typing.overload
    @staticmethod
    def Call(method: System.Reflection.MethodInfo, arguments: System.Collections.Generic.IEnumerable[System.Linq.Expressions.Expression], ) -> System.Linq.Expressions.MethodCallExpression:
        ...

    @typing.overload
    @staticmethod
    def Call(instance: System.Linq.Expressions.Expression, method: System.Reflection.MethodInfo, ) -> System.Linq.Expressions.MethodCallExpression:
        ...

    @typing.overload
    @staticmethod
    def Call(instance: System.Linq.Expressions.Expression, method: System.Reflection.MethodInfo, arguments: list[System.Linq.Expressions.Expression], ) -> System.Linq.Expressions.MethodCallExpression:
        ...

    @typing.overload
    @staticmethod
    def Call(instance: System.Linq.Expressions.Expression, method: System.Reflection.MethodInfo, arg0: System.Linq.Expressions.Expression, arg1: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.MethodCallExpression:
        ...

    @typing.overload
    @staticmethod
    def Call(instance: System.Linq.Expressions.Expression, method: System.Reflection.MethodInfo, arg0: System.Linq.Expressions.Expression, arg1: System.Linq.Expressions.Expression, arg2: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.MethodCallExpression:
        ...

    @typing.overload
    @staticmethod
    def Call(instance: System.Linq.Expressions.Expression, methodName: System.String, typeArguments: list[System.Type], arguments: list[System.Linq.Expressions.Expression], ) -> System.Linq.Expressions.MethodCallExpression:
        ...

    @typing.overload
    @staticmethod
    def Call(type: System.Type, methodName: System.String, typeArguments: list[System.Type], arguments: list[System.Linq.Expressions.Expression], ) -> System.Linq.Expressions.MethodCallExpression:
        ...

    @typing.overload
    @staticmethod
    def Call(instance: System.Linq.Expressions.Expression, method: System.Reflection.MethodInfo, arguments: System.Collections.Generic.IEnumerable[System.Linq.Expressions.Expression], ) -> System.Linq.Expressions.MethodCallExpression:
        ...

    @typing.overload
    @staticmethod
    def ArrayIndex(array: System.Linq.Expressions.Expression, indexes: list[System.Linq.Expressions.Expression], ) -> System.Linq.Expressions.MethodCallExpression:
        ...

    @typing.overload
    @staticmethod
    def ArrayIndex(array: System.Linq.Expressions.Expression, indexes: System.Collections.Generic.IEnumerable[System.Linq.Expressions.Expression], ) -> System.Linq.Expressions.MethodCallExpression:
        ...

    @typing.overload
    @staticmethod
    def NewArrayInit(type: System.Type, initializers: list[System.Linq.Expressions.Expression], ) -> System.Linq.Expressions.NewArrayExpression:
        ...

    @typing.overload
    @staticmethod
    def NewArrayInit(type: System.Type, initializers: System.Collections.Generic.IEnumerable[System.Linq.Expressions.Expression], ) -> System.Linq.Expressions.NewArrayExpression:
        ...

    @typing.overload
    @staticmethod
    def NewArrayBounds(type: System.Type, bounds: list[System.Linq.Expressions.Expression], ) -> System.Linq.Expressions.NewArrayExpression:
        ...

    @typing.overload
    @staticmethod
    def NewArrayBounds(type: System.Type, bounds: System.Collections.Generic.IEnumerable[System.Linq.Expressions.Expression], ) -> System.Linq.Expressions.NewArrayExpression:
        ...

    @typing.overload
    @staticmethod
    def New(constructor: System.Reflection.ConstructorInfo, ) -> System.Linq.Expressions.NewExpression:
        ...

    @typing.overload
    @staticmethod
    def New(constructor: System.Reflection.ConstructorInfo, arguments: list[System.Linq.Expressions.Expression], ) -> System.Linq.Expressions.NewExpression:
        ...

    @typing.overload
    @staticmethod
    def New(constructor: System.Reflection.ConstructorInfo, arguments: System.Collections.Generic.IEnumerable[System.Linq.Expressions.Expression], ) -> System.Linq.Expressions.NewExpression:
        ...

    @typing.overload
    @staticmethod
    def New(constructor: System.Reflection.ConstructorInfo, arguments: System.Collections.Generic.IEnumerable[System.Linq.Expressions.Expression], members: System.Collections.Generic.IEnumerable[System.Reflection.MemberInfo], ) -> System.Linq.Expressions.NewExpression:
        ...

    @typing.overload
    @staticmethod
    def New(constructor: System.Reflection.ConstructorInfo, arguments: System.Collections.Generic.IEnumerable[System.Linq.Expressions.Expression], members: list[System.Reflection.MemberInfo], ) -> System.Linq.Expressions.NewExpression:
        ...

    @typing.overload
    @staticmethod
    def New(type: System.Type, ) -> System.Linq.Expressions.NewExpression:
        ...

    @typing.overload
    @staticmethod
    def Parameter(type: System.Type, ) -> System.Linq.Expressions.ParameterExpression:
        ...

    @typing.overload
    @staticmethod
    def Variable(type: System.Type, ) -> System.Linq.Expressions.ParameterExpression:
        ...

    @typing.overload
    @staticmethod
    def Parameter(type: System.Type, name: System.String, ) -> System.Linq.Expressions.ParameterExpression:
        ...

    @typing.overload
    @staticmethod
    def Variable(type: System.Type, name: System.String, ) -> System.Linq.Expressions.ParameterExpression:
        ...

    @typing.overload
    @staticmethod
    def RuntimeVariables(variables: list[System.Linq.Expressions.ParameterExpression], ) -> System.Linq.Expressions.RuntimeVariablesExpression:
        ...

    @typing.overload
    @staticmethod
    def RuntimeVariables(variables: System.Collections.Generic.IEnumerable[System.Linq.Expressions.ParameterExpression], ) -> System.Linq.Expressions.RuntimeVariablesExpression:
        ...

    @typing.overload
    @staticmethod
    def SwitchCase(body: System.Linq.Expressions.Expression, testValues: list[System.Linq.Expressions.Expression], ) -> System.Linq.Expressions.SwitchCase:
        ...

    @typing.overload
    @staticmethod
    def SwitchCase(body: System.Linq.Expressions.Expression, testValues: System.Collections.Generic.IEnumerable[System.Linq.Expressions.Expression], ) -> System.Linq.Expressions.SwitchCase:
        ...

    @typing.overload
    @staticmethod
    def Switch(switchValue: System.Linq.Expressions.Expression, cases: list[System.Linq.Expressions.SwitchCase], ) -> System.Linq.Expressions.SwitchExpression:
        ...

    @typing.overload
    @staticmethod
    def Switch(switchValue: System.Linq.Expressions.Expression, defaultBody: System.Linq.Expressions.Expression, cases: list[System.Linq.Expressions.SwitchCase], ) -> System.Linq.Expressions.SwitchExpression:
        ...

    @typing.overload
    @staticmethod
    def Switch(switchValue: System.Linq.Expressions.Expression, defaultBody: System.Linq.Expressions.Expression, comparison: System.Reflection.MethodInfo, cases: list[System.Linq.Expressions.SwitchCase], ) -> System.Linq.Expressions.SwitchExpression:
        ...

    @typing.overload
    @staticmethod
    def MakeDynamic(delegateType: System.Type, binder: System.Runtime.CompilerServices.CallSiteBinder, arg0: System.Linq.Expressions.Expression, arg1: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.DynamicExpression:
        ...

    @typing.overload
    @staticmethod
    def MakeDynamic(delegateType: System.Type, binder: System.Runtime.CompilerServices.CallSiteBinder, arg0: System.Linq.Expressions.Expression, arg1: System.Linq.Expressions.Expression, arg2: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.DynamicExpression:
        ...

    @typing.overload
    @staticmethod
    def MakeDynamic(delegateType: System.Type, binder: System.Runtime.CompilerServices.CallSiteBinder, arg0: System.Linq.Expressions.Expression, arg1: System.Linq.Expressions.Expression, arg2: System.Linq.Expressions.Expression, arg3: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.DynamicExpression:
        ...

    @typing.overload
    @staticmethod
    def MakeDynamic(delegateType: System.Type, binder: System.Runtime.CompilerServices.CallSiteBinder, arguments: list[System.Linq.Expressions.Expression], ) -> System.Linq.Expressions.DynamicExpression:
        ...

    @typing.overload
    @staticmethod
    def Break(target: System.Linq.Expressions.LabelTarget, ) -> System.Linq.Expressions.GotoExpression:
        ...

    @typing.overload
    @staticmethod
    def Break(target: System.Linq.Expressions.LabelTarget, value: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.GotoExpression:
        ...

    @typing.overload
    @staticmethod
    def Break(target: System.Linq.Expressions.LabelTarget, type: System.Type, ) -> System.Linq.Expressions.GotoExpression:
        ...

    @typing.overload
    @staticmethod
    def Break(target: System.Linq.Expressions.LabelTarget, value: System.Linq.Expressions.Expression, type: System.Type, ) -> System.Linq.Expressions.GotoExpression:
        ...

    @typing.overload
    @staticmethod
    def Continue(target: System.Linq.Expressions.LabelTarget, ) -> System.Linq.Expressions.GotoExpression:
        ...

    @typing.overload
    @staticmethod
    def Continue(target: System.Linq.Expressions.LabelTarget, type: System.Type, ) -> System.Linq.Expressions.GotoExpression:
        ...

    @typing.overload
    @staticmethod
    def Return(target: System.Linq.Expressions.LabelTarget, ) -> System.Linq.Expressions.GotoExpression:
        ...

    @typing.overload
    @staticmethod
    def Return(target: System.Linq.Expressions.LabelTarget, type: System.Type, ) -> System.Linq.Expressions.GotoExpression:
        ...

    @typing.overload
    @staticmethod
    def Return(target: System.Linq.Expressions.LabelTarget, value: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.GotoExpression:
        ...

    @typing.overload
    @staticmethod
    def Return(target: System.Linq.Expressions.LabelTarget, value: System.Linq.Expressions.Expression, type: System.Type, ) -> System.Linq.Expressions.GotoExpression:
        ...

    @typing.overload
    @staticmethod
    def Goto(target: System.Linq.Expressions.LabelTarget, ) -> System.Linq.Expressions.GotoExpression:
        ...

    @typing.overload
    @staticmethod
    def Goto(target: System.Linq.Expressions.LabelTarget, type: System.Type, ) -> System.Linq.Expressions.GotoExpression:
        ...

    @typing.overload
    @staticmethod
    def Goto(target: System.Linq.Expressions.LabelTarget, value: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.GotoExpression:
        ...

    @typing.overload
    @staticmethod
    def Goto(target: System.Linq.Expressions.LabelTarget, value: System.Linq.Expressions.Expression, type: System.Type, ) -> System.Linq.Expressions.GotoExpression:
        ...

    @typing.overload
    @staticmethod
    def MakeGoto(kind: System.Linq.Expressions.GotoExpressionKind, target: System.Linq.Expressions.LabelTarget, value: System.Linq.Expressions.Expression, type: System.Type, ) -> System.Linq.Expressions.GotoExpression:
        ...

    @typing.overload
    @staticmethod
    def MakeIndex(instance: System.Linq.Expressions.Expression, indexer: System.Reflection.PropertyInfo, arguments: System.Collections.Generic.IEnumerable[System.Linq.Expressions.Expression], ) -> System.Linq.Expressions.IndexExpression:
        ...

    @typing.overload
    @staticmethod
    def ArrayAccess(array: System.Linq.Expressions.Expression, indexes: list[System.Linq.Expressions.Expression], ) -> System.Linq.Expressions.IndexExpression:
        ...

    @typing.overload
    @staticmethod
    def ArrayAccess(array: System.Linq.Expressions.Expression, indexes: System.Collections.Generic.IEnumerable[System.Linq.Expressions.Expression], ) -> System.Linq.Expressions.IndexExpression:
        ...

    @typing.overload
    @staticmethod
    def Property(instance: System.Linq.Expressions.Expression, propertyName: System.String, arguments: list[System.Linq.Expressions.Expression], ) -> System.Linq.Expressions.IndexExpression:
        ...

    @typing.overload
    @staticmethod
    def Property(instance: System.Linq.Expressions.Expression, indexer: System.Reflection.PropertyInfo, arguments: list[System.Linq.Expressions.Expression], ) -> System.Linq.Expressions.IndexExpression:
        ...

    @typing.overload
    @staticmethod
    def Property(instance: System.Linq.Expressions.Expression, indexer: System.Reflection.PropertyInfo, arguments: System.Collections.Generic.IEnumerable[System.Linq.Expressions.Expression], ) -> System.Linq.Expressions.IndexExpression:
        ...

    @typing.overload
    @staticmethod
    def Invoke(expression: System.Linq.Expressions.Expression, arguments: list[System.Linq.Expressions.Expression], ) -> System.Linq.Expressions.InvocationExpression:
        ...

    @typing.overload
    @staticmethod
    def Invoke(expression: System.Linq.Expressions.Expression, arguments: System.Collections.Generic.IEnumerable[System.Linq.Expressions.Expression], ) -> System.Linq.Expressions.InvocationExpression:
        ...

    @typing.overload
    @staticmethod
    def Label(target: System.Linq.Expressions.LabelTarget, ) -> System.Linq.Expressions.LabelExpression:
        ...

    @typing.overload
    @staticmethod
    def Label(target: System.Linq.Expressions.LabelTarget, defaultValue: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.LabelExpression:
        ...

    @typing.overload
    @staticmethod
    def Label() -> System.Linq.Expressions.LabelTarget:
        ...

    @typing.overload
    @staticmethod
    def Label(name: System.String, ) -> System.Linq.Expressions.LabelTarget:
        ...

    @typing.overload
    @staticmethod
    def Label(type: System.Type, ) -> System.Linq.Expressions.LabelTarget:
        ...

    @typing.overload
    @staticmethod
    def Label(type: System.Type, name: System.String, ) -> System.Linq.Expressions.LabelTarget:
        ...

    @typing.overload
    @staticmethod
    def Lambda(body: System.Linq.Expressions.Expression, parameters: list[System.Linq.Expressions.ParameterExpression], ) -> System.Linq.Expressions.Expression[TDelegate]:
        ...

    @typing.overload
    @staticmethod
    def Lambda(body: System.Linq.Expressions.Expression, tailCall: System.Boolean, parameters: list[System.Linq.Expressions.ParameterExpression], ) -> System.Linq.Expressions.Expression[TDelegate]:
        ...

    @typing.overload
    @staticmethod
    def Lambda(body: System.Linq.Expressions.Expression, parameters: System.Collections.Generic.IEnumerable[System.Linq.Expressions.ParameterExpression], ) -> System.Linq.Expressions.Expression[TDelegate]:
        ...

    @typing.overload
    @staticmethod
    def Lambda(body: System.Linq.Expressions.Expression, tailCall: System.Boolean, parameters: System.Collections.Generic.IEnumerable[System.Linq.Expressions.ParameterExpression], ) -> System.Linq.Expressions.Expression[TDelegate]:
        ...

    @typing.overload
    @staticmethod
    def Lambda(body: System.Linq.Expressions.Expression, name: System.String, parameters: System.Collections.Generic.IEnumerable[System.Linq.Expressions.ParameterExpression], ) -> System.Linq.Expressions.Expression[TDelegate]:
        ...

    @typing.overload
    @staticmethod
    def Lambda(body: System.Linq.Expressions.Expression, name: System.String, tailCall: System.Boolean, parameters: System.Collections.Generic.IEnumerable[System.Linq.Expressions.ParameterExpression], ) -> System.Linq.Expressions.Expression[TDelegate]:
        ...

    @typing.overload
    @staticmethod
    def Lambda(body: System.Linq.Expressions.Expression, parameters: list[System.Linq.Expressions.ParameterExpression], ) -> System.Linq.Expressions.LambdaExpression:
        ...

    @typing.overload
    @staticmethod
    def Lambda(body: System.Linq.Expressions.Expression, tailCall: System.Boolean, parameters: list[System.Linq.Expressions.ParameterExpression], ) -> System.Linq.Expressions.LambdaExpression:
        ...

    @typing.overload
    @staticmethod
    def Lambda(body: System.Linq.Expressions.Expression, parameters: System.Collections.Generic.IEnumerable[System.Linq.Expressions.ParameterExpression], ) -> System.Linq.Expressions.LambdaExpression:
        ...

    @typing.overload
    @staticmethod
    def Lambda(body: System.Linq.Expressions.Expression, tailCall: System.Boolean, parameters: System.Collections.Generic.IEnumerable[System.Linq.Expressions.ParameterExpression], ) -> System.Linq.Expressions.LambdaExpression:
        ...

    @typing.overload
    @staticmethod
    def Lambda(delegateType: System.Type, body: System.Linq.Expressions.Expression, parameters: list[System.Linq.Expressions.ParameterExpression], ) -> System.Linq.Expressions.LambdaExpression:
        ...

    @typing.overload
    @staticmethod
    def Lambda(delegateType: System.Type, body: System.Linq.Expressions.Expression, tailCall: System.Boolean, parameters: list[System.Linq.Expressions.ParameterExpression], ) -> System.Linq.Expressions.LambdaExpression:
        ...

    @typing.overload
    @staticmethod
    def Lambda(delegateType: System.Type, body: System.Linq.Expressions.Expression, parameters: System.Collections.Generic.IEnumerable[System.Linq.Expressions.ParameterExpression], ) -> System.Linq.Expressions.LambdaExpression:
        ...

    @typing.overload
    @staticmethod
    def Lambda(delegateType: System.Type, body: System.Linq.Expressions.Expression, tailCall: System.Boolean, parameters: System.Collections.Generic.IEnumerable[System.Linq.Expressions.ParameterExpression], ) -> System.Linq.Expressions.LambdaExpression:
        ...

    @typing.overload
    @staticmethod
    def Lambda(body: System.Linq.Expressions.Expression, name: System.String, parameters: System.Collections.Generic.IEnumerable[System.Linq.Expressions.ParameterExpression], ) -> System.Linq.Expressions.LambdaExpression:
        ...

    @typing.overload
    @staticmethod
    def Lambda(body: System.Linq.Expressions.Expression, name: System.String, tailCall: System.Boolean, parameters: System.Collections.Generic.IEnumerable[System.Linq.Expressions.ParameterExpression], ) -> System.Linq.Expressions.LambdaExpression:
        ...

    @typing.overload
    @staticmethod
    def Lambda(delegateType: System.Type, body: System.Linq.Expressions.Expression, name: System.String, parameters: System.Collections.Generic.IEnumerable[System.Linq.Expressions.ParameterExpression], ) -> System.Linq.Expressions.LambdaExpression:
        ...

    @typing.overload
    @staticmethod
    def Lambda(delegateType: System.Type, body: System.Linq.Expressions.Expression, name: System.String, tailCall: System.Boolean, parameters: System.Collections.Generic.IEnumerable[System.Linq.Expressions.ParameterExpression], ) -> System.Linq.Expressions.LambdaExpression:
        ...

    @typing.overload
    @staticmethod
    def GetFuncType(typeArgs: list[System.Type], ) -> System.Type:
        ...

    @typing.overload
    @staticmethod
    def TryGetFuncType(typeArgs: list[System.Type], funcType: ref[System.Type], ) -> System.Boolean:
        ...

    @typing.overload
    @staticmethod
    def GetActionType(typeArgs: list[System.Type], ) -> System.Type:
        ...

    @typing.overload
    @staticmethod
    def TryGetActionType(typeArgs: list[System.Type], actionType: ref[System.Type], ) -> System.Boolean:
        ...

    @typing.overload
    @staticmethod
    def GetDelegateType(typeArgs: list[System.Type], ) -> System.Type:
        ...

    @typing.overload
    @staticmethod
    def ListInit(newExpression: System.Linq.Expressions.NewExpression, initializers: list[System.Linq.Expressions.Expression], ) -> System.Linq.Expressions.ListInitExpression:
        ...

    @typing.overload
    @staticmethod
    def ListInit(newExpression: System.Linq.Expressions.NewExpression, initializers: System.Collections.Generic.IEnumerable[System.Linq.Expressions.Expression], ) -> System.Linq.Expressions.ListInitExpression:
        ...

    @typing.overload
    @staticmethod
    def ListInit(newExpression: System.Linq.Expressions.NewExpression, addMethod: System.Reflection.MethodInfo, initializers: list[System.Linq.Expressions.Expression], ) -> System.Linq.Expressions.ListInitExpression:
        ...

    @typing.overload
    @staticmethod
    def ListInit(newExpression: System.Linq.Expressions.NewExpression, addMethod: System.Reflection.MethodInfo, initializers: System.Collections.Generic.IEnumerable[System.Linq.Expressions.Expression], ) -> System.Linq.Expressions.ListInitExpression:
        ...

    @typing.overload
    @staticmethod
    def ListInit(newExpression: System.Linq.Expressions.NewExpression, initializers: list[System.Linq.Expressions.ElementInit], ) -> System.Linq.Expressions.ListInitExpression:
        ...

    @typing.overload
    @staticmethod
    def LeftShift(left: System.Linq.Expressions.Expression, right: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.BinaryExpression:
        ...

    @typing.overload
    @staticmethod
    def LeftShift(left: System.Linq.Expressions.Expression, right: System.Linq.Expressions.Expression, method: System.Reflection.MethodInfo, ) -> System.Linq.Expressions.BinaryExpression:
        ...

    @typing.overload
    @staticmethod
    def LeftShiftAssign(left: System.Linq.Expressions.Expression, right: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.BinaryExpression:
        ...

    @typing.overload
    @staticmethod
    def LeftShiftAssign(left: System.Linq.Expressions.Expression, right: System.Linq.Expressions.Expression, method: System.Reflection.MethodInfo, ) -> System.Linq.Expressions.BinaryExpression:
        ...

    @typing.overload
    @staticmethod
    def LeftShiftAssign(left: System.Linq.Expressions.Expression, right: System.Linq.Expressions.Expression, method: System.Reflection.MethodInfo, conversion: System.Linq.Expressions.LambdaExpression, ) -> System.Linq.Expressions.BinaryExpression:
        ...

    @typing.overload
    @staticmethod
    def RightShift(left: System.Linq.Expressions.Expression, right: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.BinaryExpression:
        ...

    @typing.overload
    @staticmethod
    def RightShift(left: System.Linq.Expressions.Expression, right: System.Linq.Expressions.Expression, method: System.Reflection.MethodInfo, ) -> System.Linq.Expressions.BinaryExpression:
        ...

    @typing.overload
    @staticmethod
    def RightShiftAssign(left: System.Linq.Expressions.Expression, right: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.BinaryExpression:
        ...

    @typing.overload
    @staticmethod
    def RightShiftAssign(left: System.Linq.Expressions.Expression, right: System.Linq.Expressions.Expression, method: System.Reflection.MethodInfo, ) -> System.Linq.Expressions.BinaryExpression:
        ...

    @typing.overload
    @staticmethod
    def RightShiftAssign(left: System.Linq.Expressions.Expression, right: System.Linq.Expressions.Expression, method: System.Reflection.MethodInfo, conversion: System.Linq.Expressions.LambdaExpression, ) -> System.Linq.Expressions.BinaryExpression:
        ...

    @typing.overload
    @staticmethod
    def And(left: System.Linq.Expressions.Expression, right: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.BinaryExpression:
        ...

    @typing.overload
    @staticmethod
    def And(left: System.Linq.Expressions.Expression, right: System.Linq.Expressions.Expression, method: System.Reflection.MethodInfo, ) -> System.Linq.Expressions.BinaryExpression:
        ...

    @typing.overload
    @staticmethod
    def AndAssign(left: System.Linq.Expressions.Expression, right: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.BinaryExpression:
        ...

    @typing.overload
    @staticmethod
    def AndAssign(left: System.Linq.Expressions.Expression, right: System.Linq.Expressions.Expression, method: System.Reflection.MethodInfo, ) -> System.Linq.Expressions.BinaryExpression:
        ...

    @typing.overload
    @staticmethod
    def AndAssign(left: System.Linq.Expressions.Expression, right: System.Linq.Expressions.Expression, method: System.Reflection.MethodInfo, conversion: System.Linq.Expressions.LambdaExpression, ) -> System.Linq.Expressions.BinaryExpression:
        ...

    @typing.overload
    @staticmethod
    def Or(left: System.Linq.Expressions.Expression, right: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.BinaryExpression:
        ...

    @typing.overload
    @staticmethod
    def Or(left: System.Linq.Expressions.Expression, right: System.Linq.Expressions.Expression, method: System.Reflection.MethodInfo, ) -> System.Linq.Expressions.BinaryExpression:
        ...

    @typing.overload
    @staticmethod
    def OrAssign(left: System.Linq.Expressions.Expression, right: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.BinaryExpression:
        ...

    @typing.overload
    @staticmethod
    def OrAssign(left: System.Linq.Expressions.Expression, right: System.Linq.Expressions.Expression, method: System.Reflection.MethodInfo, ) -> System.Linq.Expressions.BinaryExpression:
        ...

    @typing.overload
    @staticmethod
    def OrAssign(left: System.Linq.Expressions.Expression, right: System.Linq.Expressions.Expression, method: System.Reflection.MethodInfo, conversion: System.Linq.Expressions.LambdaExpression, ) -> System.Linq.Expressions.BinaryExpression:
        ...

    @typing.overload
    @staticmethod
    def ExclusiveOr(left: System.Linq.Expressions.Expression, right: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.BinaryExpression:
        ...

    @typing.overload
    @staticmethod
    def ExclusiveOr(left: System.Linq.Expressions.Expression, right: System.Linq.Expressions.Expression, method: System.Reflection.MethodInfo, ) -> System.Linq.Expressions.BinaryExpression:
        ...

    @typing.overload
    @staticmethod
    def ExclusiveOrAssign(left: System.Linq.Expressions.Expression, right: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.BinaryExpression:
        ...

    @typing.overload
    @staticmethod
    def ExclusiveOrAssign(left: System.Linq.Expressions.Expression, right: System.Linq.Expressions.Expression, method: System.Reflection.MethodInfo, ) -> System.Linq.Expressions.BinaryExpression:
        ...

    @typing.overload
    @staticmethod
    def ExclusiveOrAssign(left: System.Linq.Expressions.Expression, right: System.Linq.Expressions.Expression, method: System.Reflection.MethodInfo, conversion: System.Linq.Expressions.LambdaExpression, ) -> System.Linq.Expressions.BinaryExpression:
        ...

    @typing.overload
    @staticmethod
    def Power(left: System.Linq.Expressions.Expression, right: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.BinaryExpression:
        ...

    @typing.overload
    @staticmethod
    def Power(left: System.Linq.Expressions.Expression, right: System.Linq.Expressions.Expression, method: System.Reflection.MethodInfo, ) -> System.Linq.Expressions.BinaryExpression:
        ...

    @typing.overload
    @staticmethod
    def PowerAssign(left: System.Linq.Expressions.Expression, right: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.BinaryExpression:
        ...

    @typing.overload
    @staticmethod
    def PowerAssign(left: System.Linq.Expressions.Expression, right: System.Linq.Expressions.Expression, method: System.Reflection.MethodInfo, ) -> System.Linq.Expressions.BinaryExpression:
        ...

    @typing.overload
    @staticmethod
    def PowerAssign(left: System.Linq.Expressions.Expression, right: System.Linq.Expressions.Expression, method: System.Reflection.MethodInfo, conversion: System.Linq.Expressions.LambdaExpression, ) -> System.Linq.Expressions.BinaryExpression:
        ...

    @typing.overload
    @staticmethod
    def ArrayIndex(array: System.Linq.Expressions.Expression, index: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.BinaryExpression:
        ...

    @typing.overload
    @staticmethod
    def Block(arg0: System.Linq.Expressions.Expression, arg1: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.BlockExpression:
        ...

    @typing.overload
    @staticmethod
    def Block(arg0: System.Linq.Expressions.Expression, arg1: System.Linq.Expressions.Expression, arg2: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.BlockExpression:
        ...

    @typing.overload
    @staticmethod
    def Block(arg0: System.Linq.Expressions.Expression, arg1: System.Linq.Expressions.Expression, arg2: System.Linq.Expressions.Expression, arg3: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.BlockExpression:
        ...

    @typing.overload
    @staticmethod
    def Block(arg0: System.Linq.Expressions.Expression, arg1: System.Linq.Expressions.Expression, arg2: System.Linq.Expressions.Expression, arg3: System.Linq.Expressions.Expression, arg4: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.BlockExpression:
        ...

    @typing.overload
    @staticmethod
    def Block(expressions: list[System.Linq.Expressions.Expression], ) -> System.Linq.Expressions.BlockExpression:
        ...

    @typing.overload
    @staticmethod
    def Block(expressions: System.Collections.Generic.IEnumerable[System.Linq.Expressions.Expression], ) -> System.Linq.Expressions.BlockExpression:
        ...

    @typing.overload
    @staticmethod
    def Block(type: System.Type, expressions: list[System.Linq.Expressions.Expression], ) -> System.Linq.Expressions.BlockExpression:
        ...

    @typing.overload
    @staticmethod
    def Block(type: System.Type, expressions: System.Collections.Generic.IEnumerable[System.Linq.Expressions.Expression], ) -> System.Linq.Expressions.BlockExpression:
        ...

    @typing.overload
    @staticmethod
    def Block(variables: System.Collections.Generic.IEnumerable[System.Linq.Expressions.ParameterExpression], expressions: list[System.Linq.Expressions.Expression], ) -> System.Linq.Expressions.BlockExpression:
        ...

    @typing.overload
    @staticmethod
    def Block(type: System.Type, variables: System.Collections.Generic.IEnumerable[System.Linq.Expressions.ParameterExpression], expressions: list[System.Linq.Expressions.Expression], ) -> System.Linq.Expressions.BlockExpression:
        ...

    @typing.overload
    @staticmethod
    def Block(variables: System.Collections.Generic.IEnumerable[System.Linq.Expressions.ParameterExpression], expressions: System.Collections.Generic.IEnumerable[System.Linq.Expressions.Expression], ) -> System.Linq.Expressions.BlockExpression:
        ...

    @typing.overload
    @staticmethod
    def Block(type: System.Type, variables: System.Collections.Generic.IEnumerable[System.Linq.Expressions.ParameterExpression], expressions: System.Collections.Generic.IEnumerable[System.Linq.Expressions.Expression], ) -> System.Linq.Expressions.BlockExpression:
        ...

    @typing.overload
    @staticmethod
    def Catch(type: System.Type, body: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.CatchBlock:
        ...

    @typing.overload
    @staticmethod
    def Catch(variable: System.Linq.Expressions.ParameterExpression, body: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.CatchBlock:
        ...

    @typing.overload
    @staticmethod
    def Catch(type: System.Type, body: System.Linq.Expressions.Expression, filter: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.CatchBlock:
        ...

    @typing.overload
    @staticmethod
    def Catch(variable: System.Linq.Expressions.ParameterExpression, body: System.Linq.Expressions.Expression, filter: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.CatchBlock:
        ...

    @typing.overload
    @staticmethod
    def MakeCatchBlock(type: System.Type, variable: System.Linq.Expressions.ParameterExpression, body: System.Linq.Expressions.Expression, filter: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.CatchBlock:
        ...

    @typing.overload
    @staticmethod
    def Condition(test: System.Linq.Expressions.Expression, ifTrue: System.Linq.Expressions.Expression, ifFalse: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.ConditionalExpression:
        ...

    @typing.overload
    @staticmethod
    def Condition(test: System.Linq.Expressions.Expression, ifTrue: System.Linq.Expressions.Expression, ifFalse: System.Linq.Expressions.Expression, type: System.Type, ) -> System.Linq.Expressions.ConditionalExpression:
        ...

    @typing.overload
    @staticmethod
    def IfThen(test: System.Linq.Expressions.Expression, ifTrue: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.ConditionalExpression:
        ...

    @typing.overload
    @staticmethod
    def IfThenElse(test: System.Linq.Expressions.Expression, ifTrue: System.Linq.Expressions.Expression, ifFalse: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.ConditionalExpression:
        ...

    @typing.overload
    @staticmethod
    def Constant(value: System.Object, ) -> System.Linq.Expressions.ConstantExpression:
        ...

    @typing.overload
    @staticmethod
    def Constant(value: System.Object, type: System.Type, ) -> System.Linq.Expressions.ConstantExpression:
        ...

    @typing.overload
    @staticmethod
    def DebugInfo(document: System.Linq.Expressions.SymbolDocumentInfo, startLine: System.Int32, startColumn: System.Int32, endLine: System.Int32, endColumn: System.Int32, ) -> System.Linq.Expressions.DebugInfoExpression:
        ...

    @typing.overload
    @staticmethod
    def ClearDebugInfo(document: System.Linq.Expressions.SymbolDocumentInfo, ) -> System.Linq.Expressions.DebugInfoExpression:
        ...

    @typing.overload
    @staticmethod
    def Empty() -> System.Linq.Expressions.DefaultExpression:
        ...

    @typing.overload
    @staticmethod
    def Default(type: System.Type, ) -> System.Linq.Expressions.DefaultExpression:
        ...

    @typing.overload
    @staticmethod
    def ElementInit(addMethod: System.Reflection.MethodInfo, arguments: list[System.Linq.Expressions.Expression], ) -> System.Linq.Expressions.ElementInit:
        ...

    @typing.overload
    @staticmethod
    def ElementInit(addMethod: System.Reflection.MethodInfo, arguments: System.Collections.Generic.IEnumerable[System.Linq.Expressions.Expression], ) -> System.Linq.Expressions.ElementInit:
        ...

    @typing.overload
    def Reduce(self, ) -> System.Linq.Expressions.Expression:
        ...

    @typing.overload
    def ReduceAndCheck(self, ) -> System.Linq.Expressions.Expression:
        ...

    @typing.overload
    def ReduceExtensions(self, ) -> System.Linq.Expressions.Expression:
        ...

    @typing.overload
    def ToString(self, ) -> System.String:
        ...

    @typing.overload
    @staticmethod
    def Dynamic(binder: System.Runtime.CompilerServices.CallSiteBinder, returnType: System.Type, arguments: System.Collections.Generic.IEnumerable[System.Linq.Expressions.Expression], ) -> System.Linq.Expressions.DynamicExpression:
        ...

    @typing.overload
    @staticmethod
    def Dynamic(binder: System.Runtime.CompilerServices.CallSiteBinder, returnType: System.Type, arg0: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.DynamicExpression:
        ...

    @typing.overload
    @staticmethod
    def Dynamic(binder: System.Runtime.CompilerServices.CallSiteBinder, returnType: System.Type, arg0: System.Linq.Expressions.Expression, arg1: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.DynamicExpression:
        ...

    @typing.overload
    @staticmethod
    def Dynamic(binder: System.Runtime.CompilerServices.CallSiteBinder, returnType: System.Type, arg0: System.Linq.Expressions.Expression, arg1: System.Linq.Expressions.Expression, arg2: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.DynamicExpression:
        ...

    @typing.overload
    @staticmethod
    def Dynamic(binder: System.Runtime.CompilerServices.CallSiteBinder, returnType: System.Type, arg0: System.Linq.Expressions.Expression, arg1: System.Linq.Expressions.Expression, arg2: System.Linq.Expressions.Expression, arg3: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.DynamicExpression:
        ...

    @typing.overload
    @staticmethod
    def Dynamic(binder: System.Runtime.CompilerServices.CallSiteBinder, returnType: System.Type, arguments: list[System.Linq.Expressions.Expression], ) -> System.Linq.Expressions.DynamicExpression:
        ...

    @typing.overload
    @staticmethod
    def MakeDynamic(delegateType: System.Type, binder: System.Runtime.CompilerServices.CallSiteBinder, arguments: System.Collections.Generic.IEnumerable[System.Linq.Expressions.Expression], ) -> System.Linq.Expressions.DynamicExpression:
        ...

    @typing.overload
    @staticmethod
    def MakeDynamic(delegateType: System.Type, binder: System.Runtime.CompilerServices.CallSiteBinder, arg0: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.DynamicExpression:
        ...

    @typing.overload
    @staticmethod
    def Assign(left: System.Linq.Expressions.Expression, right: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.BinaryExpression:
        ...

    @typing.overload
    @staticmethod
    def MakeBinary(binaryType: System.Linq.Expressions.ExpressionType, left: System.Linq.Expressions.Expression, right: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.BinaryExpression:
        ...

    @typing.overload
    @staticmethod
    def MakeBinary(binaryType: System.Linq.Expressions.ExpressionType, left: System.Linq.Expressions.Expression, right: System.Linq.Expressions.Expression, liftToNull: System.Boolean, method: System.Reflection.MethodInfo, ) -> System.Linq.Expressions.BinaryExpression:
        ...

    @typing.overload
    @staticmethod
    def MakeBinary(binaryType: System.Linq.Expressions.ExpressionType, left: System.Linq.Expressions.Expression, right: System.Linq.Expressions.Expression, liftToNull: System.Boolean, method: System.Reflection.MethodInfo, conversion: System.Linq.Expressions.LambdaExpression, ) -> System.Linq.Expressions.BinaryExpression:
        ...

    @typing.overload
    @staticmethod
    def Equal(left: System.Linq.Expressions.Expression, right: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.BinaryExpression:
        ...

    @typing.overload
    @staticmethod
    def Equal(left: System.Linq.Expressions.Expression, right: System.Linq.Expressions.Expression, liftToNull: System.Boolean, method: System.Reflection.MethodInfo, ) -> System.Linq.Expressions.BinaryExpression:
        ...

    @typing.overload
    @staticmethod
    def ReferenceEqual(left: System.Linq.Expressions.Expression, right: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.BinaryExpression:
        ...

    @typing.overload
    @staticmethod
    def NotEqual(left: System.Linq.Expressions.Expression, right: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.BinaryExpression:
        ...

    @typing.overload
    @staticmethod
    def NotEqual(left: System.Linq.Expressions.Expression, right: System.Linq.Expressions.Expression, liftToNull: System.Boolean, method: System.Reflection.MethodInfo, ) -> System.Linq.Expressions.BinaryExpression:
        ...

    @typing.overload
    @staticmethod
    def ReferenceNotEqual(left: System.Linq.Expressions.Expression, right: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.BinaryExpression:
        ...

    @typing.overload
    @staticmethod
    def GreaterThan(left: System.Linq.Expressions.Expression, right: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.BinaryExpression:
        ...

    @typing.overload
    @staticmethod
    def GreaterThan(left: System.Linq.Expressions.Expression, right: System.Linq.Expressions.Expression, liftToNull: System.Boolean, method: System.Reflection.MethodInfo, ) -> System.Linq.Expressions.BinaryExpression:
        ...

    @typing.overload
    @staticmethod
    def LessThan(left: System.Linq.Expressions.Expression, right: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.BinaryExpression:
        ...

    @typing.overload
    @staticmethod
    def LessThan(left: System.Linq.Expressions.Expression, right: System.Linq.Expressions.Expression, liftToNull: System.Boolean, method: System.Reflection.MethodInfo, ) -> System.Linq.Expressions.BinaryExpression:
        ...

    @typing.overload
    @staticmethod
    def GreaterThanOrEqual(left: System.Linq.Expressions.Expression, right: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.BinaryExpression:
        ...

    @typing.overload
    @staticmethod
    def GreaterThanOrEqual(left: System.Linq.Expressions.Expression, right: System.Linq.Expressions.Expression, liftToNull: System.Boolean, method: System.Reflection.MethodInfo, ) -> System.Linq.Expressions.BinaryExpression:
        ...

    @typing.overload
    @staticmethod
    def LessThanOrEqual(left: System.Linq.Expressions.Expression, right: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.BinaryExpression:
        ...

    @typing.overload
    @staticmethod
    def LessThanOrEqual(left: System.Linq.Expressions.Expression, right: System.Linq.Expressions.Expression, liftToNull: System.Boolean, method: System.Reflection.MethodInfo, ) -> System.Linq.Expressions.BinaryExpression:
        ...

    @typing.overload
    @staticmethod
    def AndAlso(left: System.Linq.Expressions.Expression, right: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.BinaryExpression:
        ...

    @typing.overload
    @staticmethod
    def AndAlso(left: System.Linq.Expressions.Expression, right: System.Linq.Expressions.Expression, method: System.Reflection.MethodInfo, ) -> System.Linq.Expressions.BinaryExpression:
        ...

    @typing.overload
    @staticmethod
    def OrElse(left: System.Linq.Expressions.Expression, right: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.BinaryExpression:
        ...

    @typing.overload
    @staticmethod
    def OrElse(left: System.Linq.Expressions.Expression, right: System.Linq.Expressions.Expression, method: System.Reflection.MethodInfo, ) -> System.Linq.Expressions.BinaryExpression:
        ...

    @typing.overload
    @staticmethod
    def Coalesce(left: System.Linq.Expressions.Expression, right: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.BinaryExpression:
        ...

    @typing.overload
    @staticmethod
    def Coalesce(left: System.Linq.Expressions.Expression, right: System.Linq.Expressions.Expression, conversion: System.Linq.Expressions.LambdaExpression, ) -> System.Linq.Expressions.BinaryExpression:
        ...

    @typing.overload
    @staticmethod
    def Add(left: System.Linq.Expressions.Expression, right: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.BinaryExpression:
        ...

    @typing.overload
    @staticmethod
    def Add(left: System.Linq.Expressions.Expression, right: System.Linq.Expressions.Expression, method: System.Reflection.MethodInfo, ) -> System.Linq.Expressions.BinaryExpression:
        ...

    @typing.overload
    @staticmethod
    def AddAssign(left: System.Linq.Expressions.Expression, right: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.BinaryExpression:
        ...

    @typing.overload
    @staticmethod
    def AddAssign(left: System.Linq.Expressions.Expression, right: System.Linq.Expressions.Expression, method: System.Reflection.MethodInfo, ) -> System.Linq.Expressions.BinaryExpression:
        ...

    @typing.overload
    @staticmethod
    def AddAssign(left: System.Linq.Expressions.Expression, right: System.Linq.Expressions.Expression, method: System.Reflection.MethodInfo, conversion: System.Linq.Expressions.LambdaExpression, ) -> System.Linq.Expressions.BinaryExpression:
        ...

    @typing.overload
    @staticmethod
    def AddAssignChecked(left: System.Linq.Expressions.Expression, right: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.BinaryExpression:
        ...

    @typing.overload
    @staticmethod
    def AddAssignChecked(left: System.Linq.Expressions.Expression, right: System.Linq.Expressions.Expression, method: System.Reflection.MethodInfo, ) -> System.Linq.Expressions.BinaryExpression:
        ...

    @typing.overload
    @staticmethod
    def AddAssignChecked(left: System.Linq.Expressions.Expression, right: System.Linq.Expressions.Expression, method: System.Reflection.MethodInfo, conversion: System.Linq.Expressions.LambdaExpression, ) -> System.Linq.Expressions.BinaryExpression:
        ...

    @typing.overload
    @staticmethod
    def AddChecked(left: System.Linq.Expressions.Expression, right: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.BinaryExpression:
        ...

    @typing.overload
    @staticmethod
    def AddChecked(left: System.Linq.Expressions.Expression, right: System.Linq.Expressions.Expression, method: System.Reflection.MethodInfo, ) -> System.Linq.Expressions.BinaryExpression:
        ...

    @typing.overload
    @staticmethod
    def Subtract(left: System.Linq.Expressions.Expression, right: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.BinaryExpression:
        ...

    @typing.overload
    @staticmethod
    def Subtract(left: System.Linq.Expressions.Expression, right: System.Linq.Expressions.Expression, method: System.Reflection.MethodInfo, ) -> System.Linq.Expressions.BinaryExpression:
        ...

    @typing.overload
    @staticmethod
    def SubtractAssign(left: System.Linq.Expressions.Expression, right: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.BinaryExpression:
        ...

    @typing.overload
    @staticmethod
    def SubtractAssign(left: System.Linq.Expressions.Expression, right: System.Linq.Expressions.Expression, method: System.Reflection.MethodInfo, ) -> System.Linq.Expressions.BinaryExpression:
        ...

    @typing.overload
    @staticmethod
    def SubtractAssign(left: System.Linq.Expressions.Expression, right: System.Linq.Expressions.Expression, method: System.Reflection.MethodInfo, conversion: System.Linq.Expressions.LambdaExpression, ) -> System.Linq.Expressions.BinaryExpression:
        ...

    @typing.overload
    @staticmethod
    def SubtractAssignChecked(left: System.Linq.Expressions.Expression, right: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.BinaryExpression:
        ...

    @typing.overload
    @staticmethod
    def SubtractAssignChecked(left: System.Linq.Expressions.Expression, right: System.Linq.Expressions.Expression, method: System.Reflection.MethodInfo, ) -> System.Linq.Expressions.BinaryExpression:
        ...

    @typing.overload
    @staticmethod
    def SubtractAssignChecked(left: System.Linq.Expressions.Expression, right: System.Linq.Expressions.Expression, method: System.Reflection.MethodInfo, conversion: System.Linq.Expressions.LambdaExpression, ) -> System.Linq.Expressions.BinaryExpression:
        ...

    @typing.overload
    @staticmethod
    def SubtractChecked(left: System.Linq.Expressions.Expression, right: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.BinaryExpression:
        ...

    @typing.overload
    @staticmethod
    def SubtractChecked(left: System.Linq.Expressions.Expression, right: System.Linq.Expressions.Expression, method: System.Reflection.MethodInfo, ) -> System.Linq.Expressions.BinaryExpression:
        ...

    @typing.overload
    @staticmethod
    def Divide(left: System.Linq.Expressions.Expression, right: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.BinaryExpression:
        ...

    @typing.overload
    @staticmethod
    def Divide(left: System.Linq.Expressions.Expression, right: System.Linq.Expressions.Expression, method: System.Reflection.MethodInfo, ) -> System.Linq.Expressions.BinaryExpression:
        ...

    @typing.overload
    @staticmethod
    def DivideAssign(left: System.Linq.Expressions.Expression, right: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.BinaryExpression:
        ...

    @typing.overload
    @staticmethod
    def DivideAssign(left: System.Linq.Expressions.Expression, right: System.Linq.Expressions.Expression, method: System.Reflection.MethodInfo, ) -> System.Linq.Expressions.BinaryExpression:
        ...

    @typing.overload
    @staticmethod
    def DivideAssign(left: System.Linq.Expressions.Expression, right: System.Linq.Expressions.Expression, method: System.Reflection.MethodInfo, conversion: System.Linq.Expressions.LambdaExpression, ) -> System.Linq.Expressions.BinaryExpression:
        ...

    @typing.overload
    @staticmethod
    def Modulo(left: System.Linq.Expressions.Expression, right: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.BinaryExpression:
        ...

    @typing.overload
    @staticmethod
    def Modulo(left: System.Linq.Expressions.Expression, right: System.Linq.Expressions.Expression, method: System.Reflection.MethodInfo, ) -> System.Linq.Expressions.BinaryExpression:
        ...

    @typing.overload
    @staticmethod
    def ModuloAssign(left: System.Linq.Expressions.Expression, right: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.BinaryExpression:
        ...

    @typing.overload
    @staticmethod
    def ModuloAssign(left: System.Linq.Expressions.Expression, right: System.Linq.Expressions.Expression, method: System.Reflection.MethodInfo, ) -> System.Linq.Expressions.BinaryExpression:
        ...

    @typing.overload
    @staticmethod
    def ModuloAssign(left: System.Linq.Expressions.Expression, right: System.Linq.Expressions.Expression, method: System.Reflection.MethodInfo, conversion: System.Linq.Expressions.LambdaExpression, ) -> System.Linq.Expressions.BinaryExpression:
        ...

    @typing.overload
    @staticmethod
    def Multiply(left: System.Linq.Expressions.Expression, right: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.BinaryExpression:
        ...

    @typing.overload
    @staticmethod
    def Multiply(left: System.Linq.Expressions.Expression, right: System.Linq.Expressions.Expression, method: System.Reflection.MethodInfo, ) -> System.Linq.Expressions.BinaryExpression:
        ...

    @typing.overload
    @staticmethod
    def MultiplyAssign(left: System.Linq.Expressions.Expression, right: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.BinaryExpression:
        ...

    @typing.overload
    @staticmethod
    def MultiplyAssign(left: System.Linq.Expressions.Expression, right: System.Linq.Expressions.Expression, method: System.Reflection.MethodInfo, ) -> System.Linq.Expressions.BinaryExpression:
        ...

    @typing.overload
    @staticmethod
    def MultiplyAssign(left: System.Linq.Expressions.Expression, right: System.Linq.Expressions.Expression, method: System.Reflection.MethodInfo, conversion: System.Linq.Expressions.LambdaExpression, ) -> System.Linq.Expressions.BinaryExpression:
        ...

    @typing.overload
    @staticmethod
    def MultiplyAssignChecked(left: System.Linq.Expressions.Expression, right: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.BinaryExpression:
        ...

    @typing.overload
    @staticmethod
    def MultiplyAssignChecked(left: System.Linq.Expressions.Expression, right: System.Linq.Expressions.Expression, method: System.Reflection.MethodInfo, ) -> System.Linq.Expressions.BinaryExpression:
        ...

    @typing.overload
    @staticmethod
    def MultiplyAssignChecked(left: System.Linq.Expressions.Expression, right: System.Linq.Expressions.Expression, method: System.Reflection.MethodInfo, conversion: System.Linq.Expressions.LambdaExpression, ) -> System.Linq.Expressions.BinaryExpression:
        ...

    @typing.overload
    @staticmethod
    def MultiplyChecked(left: System.Linq.Expressions.Expression, right: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.BinaryExpression:
        ...

    @typing.overload
    @staticmethod
    def MultiplyChecked(left: System.Linq.Expressions.Expression, right: System.Linq.Expressions.Expression, method: System.Reflection.MethodInfo, ) -> System.Linq.Expressions.BinaryExpression:
        ...

class SwitchCase(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def TestValues(self) -> System.Collections.ObjectModel.ReadOnlyCollection[System.Linq.Expressions.Expression]:
        ...

    @property
    def Body(self) -> System.Linq.Expressions.Expression:
        ...

    # methods
    @typing.overload
    def ToString(self, ) -> System.String:
        ...

    @typing.overload
    def Update(self, testValues: System.Collections.Generic.IEnumerable[System.Linq.Expressions.Expression], body: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.SwitchCase:
        ...

class SwitchExpression(System.Linq.Expressions.Expression):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def Type(self) -> System.Type:
        ...

    @property
    def NodeType(self) -> System.Linq.Expressions.ExpressionType:
        ...

    @property
    def SwitchValue(self) -> System.Linq.Expressions.Expression:
        ...

    @property
    def Cases(self) -> System.Collections.ObjectModel.ReadOnlyCollection[System.Linq.Expressions.SwitchCase]:
        ...

    @property
    def DefaultBody(self) -> System.Linq.Expressions.Expression:
        ...

    @property
    def Comparison(self) -> System.Reflection.MethodInfo:
        ...

    @property
    def CanReduce(self) -> System.Boolean:
        ...

    # methods
    @typing.overload
    def Update(self, switchValue: System.Linq.Expressions.Expression, cases: System.Collections.Generic.IEnumerable[System.Linq.Expressions.SwitchCase], defaultBody: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.SwitchExpression:
        ...

class SymbolDocumentInfo(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def FileName(self) -> System.String:
        ...

    @property
    def Language(self) -> System.Guid:
        ...

    @property
    def LanguageVendor(self) -> System.Guid:
        ...

    @property
    def DocumentType(self) -> System.Guid:
        ...

    # methods
class TryExpression(System.Linq.Expressions.Expression):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def Type(self) -> System.Type:
        ...

    @property
    def NodeType(self) -> System.Linq.Expressions.ExpressionType:
        ...

    @property
    def Body(self) -> System.Linq.Expressions.Expression:
        ...

    @property
    def Handlers(self) -> System.Collections.ObjectModel.ReadOnlyCollection[System.Linq.Expressions.CatchBlock]:
        ...

    @property
    def Finally(self) -> System.Linq.Expressions.Expression:
        ...

    @property
    def Fault(self) -> System.Linq.Expressions.Expression:
        ...

    @property
    def CanReduce(self) -> System.Boolean:
        ...

    # methods
    @typing.overload
    def Update(self, body: System.Linq.Expressions.Expression, handlers: System.Collections.Generic.IEnumerable[System.Linq.Expressions.CatchBlock], finally_: System.Linq.Expressions.Expression, fault: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.TryExpression:
        ...

class CatchBlock(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def Variable(self) -> System.Linq.Expressions.ParameterExpression:
        ...

    @property
    def Test(self) -> System.Type:
        ...

    @property
    def Body(self) -> System.Linq.Expressions.Expression:
        ...

    @property
    def Filter(self) -> System.Linq.Expressions.Expression:
        ...

    # methods
    @typing.overload
    def ToString(self, ) -> System.String:
        ...

    @typing.overload
    def Update(self, variable: System.Linq.Expressions.ParameterExpression, filter: System.Linq.Expressions.Expression, body: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.CatchBlock:
        ...

class TypeBinaryExpression(System.Linq.Expressions.Expression):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def Type(self) -> System.Type:
        ...

    @property
    def NodeType(self) -> System.Linq.Expressions.ExpressionType:
        ...

    @property
    def Expression(self) -> System.Linq.Expressions.Expression:
        ...

    @property
    def TypeOperand(self) -> System.Type:
        ...

    @property
    def CanReduce(self) -> System.Boolean:
        ...

    # methods
    @typing.overload
    def Update(self, expression: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.TypeBinaryExpression:
        ...

class UnaryExpression(System.Linq.Expressions.Expression):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def Type(self) -> System.Type:
        ...

    @property
    def NodeType(self) -> System.Linq.Expressions.ExpressionType:
        ...

    @property
    def Operand(self) -> System.Linq.Expressions.Expression:
        ...

    @property
    def Method(self) -> System.Reflection.MethodInfo:
        ...

    @property
    def IsLifted(self) -> System.Boolean:
        ...

    @property
    def IsLiftedToNull(self) -> System.Boolean:
        ...

    @property
    def CanReduce(self) -> System.Boolean:
        ...

    # methods
    @typing.overload
    def Reduce(self, ) -> System.Linq.Expressions.Expression:
        ...

    @typing.overload
    def Update(self, operand: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.UnaryExpression:
        ...

class NewExpression(System.Linq.Expressions.IArgumentProvider, System.Linq.Expressions.Expression):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def Type(self) -> System.Type:
        ...

    @property
    def NodeType(self) -> System.Linq.Expressions.ExpressionType:
        ...

    @property
    def Constructor(self) -> System.Reflection.ConstructorInfo:
        ...

    @property
    def Arguments(self) -> System.Collections.ObjectModel.ReadOnlyCollection[System.Linq.Expressions.Expression]:
        ...

    @property
    def ArgumentCount(self) -> System.Int32:
        ...

    @property
    def Members(self) -> System.Collections.ObjectModel.ReadOnlyCollection[System.Reflection.MemberInfo]:
        ...

    @property
    def CanReduce(self) -> System.Boolean:
        ...

    # methods
    @typing.overload
    def GetArgument(self, index: System.Int32, ) -> System.Linq.Expressions.Expression:
        ...

    @typing.overload
    def Update(self, arguments: System.Collections.Generic.IEnumerable[System.Linq.Expressions.Expression], ) -> System.Linq.Expressions.NewExpression:
        ...

class ElementInit(System.Linq.Expressions.IArgumentProvider, System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def AddMethod(self) -> System.Reflection.MethodInfo:
        ...

    @property
    def Arguments(self) -> System.Collections.ObjectModel.ReadOnlyCollection[System.Linq.Expressions.Expression]:
        ...

    @property
    def ArgumentCount(self) -> System.Int32:
        ...

    # methods
    @typing.overload
    def GetArgument(self, index: System.Int32, ) -> System.Linq.Expressions.Expression:
        ...

    @typing.overload
    def ToString(self, ) -> System.String:
        ...

    @typing.overload
    def Update(self, arguments: System.Collections.Generic.IEnumerable[System.Linq.Expressions.Expression], ) -> System.Linq.Expressions.ElementInit:
        ...

class ListInitExpression(System.Linq.Expressions.Expression):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def NodeType(self) -> System.Linq.Expressions.ExpressionType:
        ...

    @property
    def Type(self) -> System.Type:
        ...

    @property
    def CanReduce(self) -> System.Boolean:
        ...

    @property
    def NewExpression(self) -> System.Linq.Expressions.NewExpression:
        ...

    @property
    def Initializers(self) -> System.Collections.ObjectModel.ReadOnlyCollection[System.Linq.Expressions.ElementInit]:
        ...

    # methods
    @typing.overload
    def Reduce(self, ) -> System.Linq.Expressions.Expression:
        ...

    @typing.overload
    def Update(self, newExpression: System.Linq.Expressions.NewExpression, initializers: System.Collections.Generic.IEnumerable[System.Linq.Expressions.ElementInit], ) -> System.Linq.Expressions.ListInitExpression:
        ...

class LoopExpression(System.Linq.Expressions.Expression):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def Type(self) -> System.Type:
        ...

    @property
    def NodeType(self) -> System.Linq.Expressions.ExpressionType:
        ...

    @property
    def Body(self) -> System.Linq.Expressions.Expression:
        ...

    @property
    def BreakLabel(self) -> System.Linq.Expressions.LabelTarget:
        ...

    @property
    def ContinueLabel(self) -> System.Linq.Expressions.LabelTarget:
        ...

    @property
    def CanReduce(self) -> System.Boolean:
        ...

    # methods
    @typing.overload
    def Update(self, breakLabel: System.Linq.Expressions.LabelTarget, continueLabel: System.Linq.Expressions.LabelTarget, body: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.LoopExpression:
        ...

class LabelTarget(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def Name(self) -> System.String:
        ...

    @property
    def Type(self) -> System.Type:
        ...

    # methods
    @typing.overload
    def ToString(self, ) -> System.String:
        ...

class MemberAssignment(System.Linq.Expressions.MemberBinding):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def Expression(self) -> System.Linq.Expressions.Expression:
        ...

    @property
    def BindingType(self) -> System.Linq.Expressions.MemberBindingType:
        ...

    @property
    def Member(self) -> System.Reflection.MemberInfo:
        ...

    # methods
    @typing.overload
    def Update(self, expression: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.MemberAssignment:
        ...

class MemberExpression(System.Linq.Expressions.Expression):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def Member(self) -> System.Reflection.MemberInfo:
        ...

    @property
    def Expression(self) -> System.Linq.Expressions.Expression:
        ...

    @property
    def NodeType(self) -> System.Linq.Expressions.ExpressionType:
        ...

    @property
    def Type(self) -> System.Type:
        ...

    @property
    def CanReduce(self) -> System.Boolean:
        ...

    # methods
    @typing.overload
    def Update(self, expression: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.MemberExpression:
        ...

class MemberBinding(System.Object, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def BindingType(self) -> System.Linq.Expressions.MemberBindingType:
        ...

    @property
    def Member(self) -> System.Reflection.MemberInfo:
        ...

    # methods
    @typing.overload
    def ToString(self, ) -> System.String:
        ...

class MemberInitExpression(System.Linq.Expressions.Expression):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def Type(self) -> System.Type:
        ...

    @property
    def CanReduce(self) -> System.Boolean:
        ...

    @property
    def NodeType(self) -> System.Linq.Expressions.ExpressionType:
        ...

    @property
    def NewExpression(self) -> System.Linq.Expressions.NewExpression:
        ...

    @property
    def Bindings(self) -> System.Collections.ObjectModel.ReadOnlyCollection[System.Linq.Expressions.MemberBinding]:
        ...

    # methods
    @typing.overload
    def Reduce(self, ) -> System.Linq.Expressions.Expression:
        ...

    @typing.overload
    def Update(self, newExpression: System.Linq.Expressions.NewExpression, bindings: System.Collections.Generic.IEnumerable[System.Linq.Expressions.MemberBinding], ) -> System.Linq.Expressions.MemberInitExpression:
        ...

class MemberListBinding(System.Linq.Expressions.MemberBinding):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def Initializers(self) -> System.Collections.ObjectModel.ReadOnlyCollection[System.Linq.Expressions.ElementInit]:
        ...

    @property
    def BindingType(self) -> System.Linq.Expressions.MemberBindingType:
        ...

    @property
    def Member(self) -> System.Reflection.MemberInfo:
        ...

    # methods
    @typing.overload
    def Update(self, initializers: System.Collections.Generic.IEnumerable[System.Linq.Expressions.ElementInit], ) -> System.Linq.Expressions.MemberListBinding:
        ...

class MemberMemberBinding(System.Linq.Expressions.MemberBinding):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def Bindings(self) -> System.Collections.ObjectModel.ReadOnlyCollection[System.Linq.Expressions.MemberBinding]:
        ...

    @property
    def BindingType(self) -> System.Linq.Expressions.MemberBindingType:
        ...

    @property
    def Member(self) -> System.Reflection.MemberInfo:
        ...

    # methods
    @typing.overload
    def Update(self, bindings: System.Collections.Generic.IEnumerable[System.Linq.Expressions.MemberBinding], ) -> System.Linq.Expressions.MemberMemberBinding:
        ...

class MethodCallExpression(System.Linq.Expressions.IArgumentProvider, System.Linq.Expressions.Expression):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def NodeType(self) -> System.Linq.Expressions.ExpressionType:
        ...

    @property
    def Type(self) -> System.Type:
        ...

    @property
    def Method(self) -> System.Reflection.MethodInfo:
        ...

    @property
    def Object(self) -> System.Linq.Expressions.Expression:
        ...

    @property
    def Arguments(self) -> System.Collections.ObjectModel.ReadOnlyCollection[System.Linq.Expressions.Expression]:
        ...

    @property
    def ArgumentCount(self) -> System.Int32:
        ...

    @property
    def CanReduce(self) -> System.Boolean:
        ...

    # methods
    @typing.overload
    def Update(self, object: System.Linq.Expressions.Expression, arguments: System.Collections.Generic.IEnumerable[System.Linq.Expressions.Expression], ) -> System.Linq.Expressions.MethodCallExpression:
        ...

    @typing.overload
    def GetArgument(self, index: System.Int32, ) -> System.Linq.Expressions.Expression:
        ...

class NewArrayExpression(System.Linq.Expressions.Expression):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def Type(self) -> System.Type:
        ...

    @property
    def Expressions(self) -> System.Collections.ObjectModel.ReadOnlyCollection[System.Linq.Expressions.Expression]:
        ...

    @property
    def NodeType(self) -> System.Linq.Expressions.ExpressionType:
        ...

    @property
    def CanReduce(self) -> System.Boolean:
        ...

    # methods
    @typing.overload
    def Update(self, expressions: System.Collections.Generic.IEnumerable[System.Linq.Expressions.Expression], ) -> System.Linq.Expressions.NewArrayExpression:
        ...

class RuntimeVariablesExpression(System.Linq.Expressions.Expression):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def Type(self) -> System.Type:
        ...

    @property
    def NodeType(self) -> System.Linq.Expressions.ExpressionType:
        ...

    @property
    def Variables(self) -> System.Collections.ObjectModel.ReadOnlyCollection[System.Linq.Expressions.ParameterExpression]:
        ...

    @property
    def CanReduce(self) -> System.Boolean:
        ...

    # methods
    @typing.overload
    def Update(self, variables: System.Collections.Generic.IEnumerable[System.Linq.Expressions.ParameterExpression], ) -> System.Linq.Expressions.RuntimeVariablesExpression:
        ...

class DynamicExpression(System.Linq.Expressions.IDynamicExpression, System.Linq.Expressions.IArgumentProvider, System.Linq.Expressions.Expression):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def CanReduce(self) -> System.Boolean:
        ...

    @property
    def Type(self) -> System.Type:
        ...

    @property
    def NodeType(self) -> System.Linq.Expressions.ExpressionType:
        ...

    @property
    def Binder(self) -> System.Runtime.CompilerServices.CallSiteBinder:
        ...

    @property
    def DelegateType(self) -> System.Type:
        ...

    @property
    def Arguments(self) -> System.Collections.ObjectModel.ReadOnlyCollection[System.Linq.Expressions.Expression]:
        ...

    # methods
    @typing.overload
    def Reduce(self, ) -> System.Linq.Expressions.Expression:
        ...

    @typing.overload
    def Update(self, arguments: System.Collections.Generic.IEnumerable[System.Linq.Expressions.Expression], ) -> System.Linq.Expressions.DynamicExpression:
        ...

    @typing.overload
    @staticmethod
    def Dynamic(binder: System.Runtime.CompilerServices.CallSiteBinder, returnType: System.Type, arguments: list[System.Linq.Expressions.Expression], ) -> System.Linq.Expressions.DynamicExpression:
        ...

    @typing.overload
    @staticmethod
    def Dynamic(binder: System.Runtime.CompilerServices.CallSiteBinder, returnType: System.Type, arguments: System.Collections.Generic.IEnumerable[System.Linq.Expressions.Expression], ) -> System.Linq.Expressions.DynamicExpression:
        ...

    @typing.overload
    @staticmethod
    def Dynamic(binder: System.Runtime.CompilerServices.CallSiteBinder, returnType: System.Type, arg0: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.DynamicExpression:
        ...

    @typing.overload
    @staticmethod
    def Dynamic(binder: System.Runtime.CompilerServices.CallSiteBinder, returnType: System.Type, arg0: System.Linq.Expressions.Expression, arg1: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.DynamicExpression:
        ...

    @typing.overload
    @staticmethod
    def Dynamic(binder: System.Runtime.CompilerServices.CallSiteBinder, returnType: System.Type, arg0: System.Linq.Expressions.Expression, arg1: System.Linq.Expressions.Expression, arg2: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.DynamicExpression:
        ...

    @typing.overload
    @staticmethod
    def Dynamic(binder: System.Runtime.CompilerServices.CallSiteBinder, returnType: System.Type, arg0: System.Linq.Expressions.Expression, arg1: System.Linq.Expressions.Expression, arg2: System.Linq.Expressions.Expression, arg3: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.DynamicExpression:
        ...

    @typing.overload
    @staticmethod
    def MakeDynamic(delegateType: System.Type, binder: System.Runtime.CompilerServices.CallSiteBinder, arguments: System.Collections.Generic.IEnumerable[System.Linq.Expressions.Expression], ) -> System.Linq.Expressions.DynamicExpression:
        ...

    @typing.overload
    @staticmethod
    def MakeDynamic(delegateType: System.Type, binder: System.Runtime.CompilerServices.CallSiteBinder, arguments: list[System.Linq.Expressions.Expression], ) -> System.Linq.Expressions.DynamicExpression:
        ...

    @typing.overload
    @staticmethod
    def MakeDynamic(delegateType: System.Type, binder: System.Runtime.CompilerServices.CallSiteBinder, arg0: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.DynamicExpression:
        ...

    @typing.overload
    @staticmethod
    def MakeDynamic(delegateType: System.Type, binder: System.Runtime.CompilerServices.CallSiteBinder, arg0: System.Linq.Expressions.Expression, arg1: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.DynamicExpression:
        ...

    @typing.overload
    @staticmethod
    def MakeDynamic(delegateType: System.Type, binder: System.Runtime.CompilerServices.CallSiteBinder, arg0: System.Linq.Expressions.Expression, arg1: System.Linq.Expressions.Expression, arg2: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.DynamicExpression:
        ...

    @typing.overload
    @staticmethod
    def MakeDynamic(delegateType: System.Type, binder: System.Runtime.CompilerServices.CallSiteBinder, arg0: System.Linq.Expressions.Expression, arg1: System.Linq.Expressions.Expression, arg2: System.Linq.Expressions.Expression, arg3: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.DynamicExpression:
        ...

class GotoExpression(System.Linq.Expressions.Expression):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def Type(self) -> System.Type:
        ...

    @property
    def NodeType(self) -> System.Linq.Expressions.ExpressionType:
        ...

    @property
    def Value(self) -> System.Linq.Expressions.Expression:
        ...

    @property
    def Target(self) -> System.Linq.Expressions.LabelTarget:
        ...

    @property
    def Kind(self) -> System.Linq.Expressions.GotoExpressionKind:
        ...

    @property
    def CanReduce(self) -> System.Boolean:
        ...

    # methods
    @typing.overload
    def Update(self, target: System.Linq.Expressions.LabelTarget, value: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.GotoExpression:
        ...

class GotoExpressionKind(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    Goto: System.Int32 = Goto
    Return: System.Int32 = Return
    Break: System.Int32 = Break
    Continue: System.Int32 = Continue

class IndexExpression(System.Linq.Expressions.IArgumentProvider, System.Linq.Expressions.Expression):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def NodeType(self) -> System.Linq.Expressions.ExpressionType:
        ...

    @property
    def Type(self) -> System.Type:
        ...

    @property
    def Object(self) -> System.Linq.Expressions.Expression:
        ...

    @property
    def Indexer(self) -> System.Reflection.PropertyInfo:
        ...

    @property
    def Arguments(self) -> System.Collections.ObjectModel.ReadOnlyCollection[System.Linq.Expressions.Expression]:
        ...

    @property
    def ArgumentCount(self) -> System.Int32:
        ...

    @property
    def CanReduce(self) -> System.Boolean:
        ...

    # methods
    @typing.overload
    def Update(self, object: System.Linq.Expressions.Expression, arguments: System.Collections.Generic.IEnumerable[System.Linq.Expressions.Expression], ) -> System.Linq.Expressions.IndexExpression:
        ...

    @typing.overload
    def GetArgument(self, index: System.Int32, ) -> System.Linq.Expressions.Expression:
        ...

class InvocationExpression(System.Linq.Expressions.IArgumentProvider, System.Linq.Expressions.Expression):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def Type(self) -> System.Type:
        ...

    @property
    def NodeType(self) -> System.Linq.Expressions.ExpressionType:
        ...

    @property
    def Expression(self) -> System.Linq.Expressions.Expression:
        ...

    @property
    def Arguments(self) -> System.Collections.ObjectModel.ReadOnlyCollection[System.Linq.Expressions.Expression]:
        ...

    @property
    def ArgumentCount(self) -> System.Int32:
        ...

    @property
    def CanReduce(self) -> System.Boolean:
        ...

    # methods
    @typing.overload
    def Update(self, expression: System.Linq.Expressions.Expression, arguments: System.Collections.Generic.IEnumerable[System.Linq.Expressions.Expression], ) -> System.Linq.Expressions.InvocationExpression:
        ...

    @typing.overload
    def GetArgument(self, index: System.Int32, ) -> System.Linq.Expressions.Expression:
        ...

class LabelExpression(System.Linq.Expressions.Expression):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def Type(self) -> System.Type:
        ...

    @property
    def NodeType(self) -> System.Linq.Expressions.ExpressionType:
        ...

    @property
    def Target(self) -> System.Linq.Expressions.LabelTarget:
        ...

    @property
    def DefaultValue(self) -> System.Linq.Expressions.Expression:
        ...

    @property
    def CanReduce(self) -> System.Boolean:
        ...

    # methods
    @typing.overload
    def Update(self, target: System.Linq.Expressions.LabelTarget, defaultValue: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.LabelExpression:
        ...

class BinaryExpression(System.Linq.Expressions.Expression):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def CanReduce(self) -> System.Boolean:
        ...

    @property
    def Right(self) -> System.Linq.Expressions.Expression:
        ...

    @property
    def Left(self) -> System.Linq.Expressions.Expression:
        ...

    @property
    def Method(self) -> System.Reflection.MethodInfo:
        ...

    @property
    def Conversion(self) -> System.Linq.Expressions.LambdaExpression:
        ...

    @property
    def IsLifted(self) -> System.Boolean:
        ...

    @property
    def IsLiftedToNull(self) -> System.Boolean:
        ...

    @property
    def NodeType(self) -> System.Linq.Expressions.ExpressionType:
        ...

    @property
    def Type(self) -> System.Type:
        ...

    # methods
    @typing.overload
    def Update(self, left: System.Linq.Expressions.Expression, conversion: System.Linq.Expressions.LambdaExpression, right: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.BinaryExpression:
        ...

    @typing.overload
    def Reduce(self, ) -> System.Linq.Expressions.Expression:
        ...

class BlockExpression(System.Linq.Expressions.Expression):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def Expressions(self) -> System.Collections.ObjectModel.ReadOnlyCollection[System.Linq.Expressions.Expression]:
        ...

    @property
    def Variables(self) -> System.Collections.ObjectModel.ReadOnlyCollection[System.Linq.Expressions.ParameterExpression]:
        ...

    @property
    def Result(self) -> System.Linq.Expressions.Expression:
        ...

    @property
    def NodeType(self) -> System.Linq.Expressions.ExpressionType:
        ...

    @property
    def Type(self) -> System.Type:
        ...

    @property
    def CanReduce(self) -> System.Boolean:
        ...

    # methods
    @typing.overload
    def Update(self, variables: System.Collections.Generic.IEnumerable[System.Linq.Expressions.ParameterExpression], expressions: System.Collections.Generic.IEnumerable[System.Linq.Expressions.Expression], ) -> System.Linq.Expressions.BlockExpression:
        ...

class ConditionalExpression(System.Linq.Expressions.Expression):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def NodeType(self) -> System.Linq.Expressions.ExpressionType:
        ...

    @property
    def Type(self) -> System.Type:
        ...

    @property
    def Test(self) -> System.Linq.Expressions.Expression:
        ...

    @property
    def IfTrue(self) -> System.Linq.Expressions.Expression:
        ...

    @property
    def IfFalse(self) -> System.Linq.Expressions.Expression:
        ...

    @property
    def CanReduce(self) -> System.Boolean:
        ...

    # methods
    @typing.overload
    def Update(self, test: System.Linq.Expressions.Expression, ifTrue: System.Linq.Expressions.Expression, ifFalse: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.ConditionalExpression:
        ...

class ConstantExpression(System.Linq.Expressions.Expression):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def Type(self) -> System.Type:
        ...

    @property
    def NodeType(self) -> System.Linq.Expressions.ExpressionType:
        ...

    @property
    def Value(self) -> System.Object:
        ...

    @property
    def CanReduce(self) -> System.Boolean:
        ...

    # methods
class DebugInfoExpression(System.Linq.Expressions.Expression):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def Type(self) -> System.Type:
        ...

    @property
    def NodeType(self) -> System.Linq.Expressions.ExpressionType:
        ...

    @property
    def StartLine(self) -> System.Int32:
        ...

    @property
    def StartColumn(self) -> System.Int32:
        ...

    @property
    def EndLine(self) -> System.Int32:
        ...

    @property
    def EndColumn(self) -> System.Int32:
        ...

    @property
    def Document(self) -> System.Linq.Expressions.SymbolDocumentInfo:
        ...

    @property
    def IsClear(self) -> System.Boolean:
        ...

    @property
    def CanReduce(self) -> System.Boolean:
        ...

    # methods
class DefaultExpression(System.Linq.Expressions.Expression):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def Type(self) -> System.Type:
        ...

    @property
    def NodeType(self) -> System.Linq.Expressions.ExpressionType:
        ...

    @property
    def CanReduce(self) -> System.Boolean:
        ...

    # methods
class IArgumentProvider(abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @abc.abstractmethod
    @property
    def ArgumentCount(self) -> System.Int32:
        ...

    # methods
    @typing.overload
    @abc.abstractmethod
    def GetArgument(self, index: System.Int32, ) -> System.Linq.Expressions.Expression:
        ...

class MemberBindingType(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    Assignment: System.Int32 = Assignment
    MemberBinding: System.Int32 = MemberBinding
    ListBinding: System.Int32 = ListBinding

class IDynamicExpression(System.Linq.Expressions.IArgumentProvider, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @abc.abstractmethod
    @property
    def DelegateType(self) -> System.Type:
        ...

    # methods
    @typing.overload
    @abc.abstractmethod
    def Rewrite(self, args: list[System.Linq.Expressions.Expression], ) -> System.Linq.Expressions.Expression:
        ...

    @typing.overload
    @abc.abstractmethod
    def CreateCallSite(self, ) -> System.Object:
        ...

