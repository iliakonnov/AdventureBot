from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import System
import System.Linq.Expressions
import System.Reflection
import System.Collections.Generic
import System.Collections.ObjectModel
import System.Runtime.CompilerServices
import System.Linq.Expressions.Compiler

TDelegate = typing.TypeVar('TDelegate')
T = typing.TypeVar('T')

class Expression(System.Object, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def NodeType(self) -> int:
        ...

    @property
    def Type(self) -> System.Type:
        ...

    @property
    def CanReduce(self) -> bool:
        ...

    @property
    def DebugView(self) -> str:
        ...

    # methods
    @typing.overload
    def __init__(self, nodeType: int, type: System.Type, ):
        ...

    @typing.overload
    def __init__(self, ):
        ...

    def ToString(self, ) -> str:
        ...

    def Reduce(self, ) -> System.Linq.Expressions.Expression:
        ...

    def Accept(self, visitor: System.Linq.Expressions.ExpressionVisitor, ) -> System.Linq.Expressions.Expression:
        ...

    def VisitChildren(self, visitor: System.Linq.Expressions.ExpressionVisitor, ) -> System.Linq.Expressions.Expression:
        ...

    @staticmethod
    @typing.overload
    def Switch(type: System.Type, switchValue: System.Linq.Expressions.Expression, defaultBody: System.Linq.Expressions.Expression, comparison: System.Reflection.MethodInfo, cases: System.Array[System.Linq.Expressions.SwitchCase], ) -> System.Linq.Expressions.SwitchExpression:
        ...

    @staticmethod
    @typing.overload
    def Switch(switchValue: System.Linq.Expressions.Expression, defaultBody: System.Linq.Expressions.Expression, comparison: System.Reflection.MethodInfo, cases: System.Collections.Generic.IEnumerable[System.Linq.Expressions.SwitchCase], ) -> System.Linq.Expressions.SwitchExpression:
        ...

    @staticmethod
    @typing.overload
    def Switch(type: System.Type, switchValue: System.Linq.Expressions.Expression, defaultBody: System.Linq.Expressions.Expression, comparison: System.Reflection.MethodInfo, cases: System.Collections.Generic.IEnumerable[System.Linq.Expressions.SwitchCase], ) -> System.Linq.Expressions.SwitchExpression:
        ...

    @staticmethod
    @typing.overload
    def Switch(switchValue: System.Linq.Expressions.Expression, cases: System.Array[System.Linq.Expressions.SwitchCase], ) -> System.Linq.Expressions.SwitchExpression:
        ...

    @staticmethod
    @typing.overload
    def Switch(switchValue: System.Linq.Expressions.Expression, defaultBody: System.Linq.Expressions.Expression, cases: System.Array[System.Linq.Expressions.SwitchCase], ) -> System.Linq.Expressions.SwitchExpression:
        ...

    @staticmethod
    @typing.overload
    def Switch(switchValue: System.Linq.Expressions.Expression, defaultBody: System.Linq.Expressions.Expression, comparison: System.Reflection.MethodInfo, cases: System.Array[System.Linq.Expressions.SwitchCase], ) -> System.Linq.Expressions.SwitchExpression:
        ...

    @staticmethod
    def ValidateSwitchCaseType(case: System.Linq.Expressions.Expression, customType: bool, resultType: System.Type, parameterName: str, ) -> None:
        ...

    @staticmethod
    @typing.overload
    def SymbolDocument(fileName: str, ) -> System.Linq.Expressions.SymbolDocumentInfo:
        ...

    @staticmethod
    @typing.overload
    def SymbolDocument(fileName: str, language: System.Guid, ) -> System.Linq.Expressions.SymbolDocumentInfo:
        ...

    @staticmethod
    @typing.overload
    def SymbolDocument(fileName: str, language: System.Guid, languageVendor: System.Guid, ) -> System.Linq.Expressions.SymbolDocumentInfo:
        ...

    @staticmethod
    @typing.overload
    def SymbolDocument(fileName: str, language: System.Guid, languageVendor: System.Guid, documentType: System.Guid, ) -> System.Linq.Expressions.SymbolDocumentInfo:
        ...

    @staticmethod
    def TryFault(body: System.Linq.Expressions.Expression, fault: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.TryExpression:
        ...

    @staticmethod
    def TryFinally(body: System.Linq.Expressions.Expression, finally_: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.TryExpression:
        ...

    @staticmethod
    def TryCatch(body: System.Linq.Expressions.Expression, handlers: System.Array[System.Linq.Expressions.CatchBlock], ) -> System.Linq.Expressions.TryExpression:
        ...

    @staticmethod
    def TryCatchFinally(body: System.Linq.Expressions.Expression, finally_: System.Linq.Expressions.Expression, handlers: System.Array[System.Linq.Expressions.CatchBlock], ) -> System.Linq.Expressions.TryExpression:
        ...

    @staticmethod
    def MakeTry(type: System.Type, body: System.Linq.Expressions.Expression, finally_: System.Linq.Expressions.Expression, fault: System.Linq.Expressions.Expression, handlers: System.Collections.Generic.IEnumerable[System.Linq.Expressions.CatchBlock], ) -> System.Linq.Expressions.TryExpression:
        ...

    @staticmethod
    def ValidateTryAndCatchHaveSameType(type: System.Type, tryBody: System.Linq.Expressions.Expression, handlers: System.Collections.ObjectModel.ReadOnlyCollection[System.Linq.Expressions.CatchBlock], ) -> None:
        ...

    @staticmethod
    def TypeIs(expression: System.Linq.Expressions.Expression, type: System.Type, ) -> System.Linq.Expressions.TypeBinaryExpression:
        ...

    @staticmethod
    def TypeEqual(expression: System.Linq.Expressions.Expression, type: System.Type, ) -> System.Linq.Expressions.TypeBinaryExpression:
        ...

    @staticmethod
    @typing.overload
    def MakeUnary(unaryType: int, operand: System.Linq.Expressions.Expression, type: System.Type, ) -> System.Linq.Expressions.UnaryExpression:
        ...

    @staticmethod
    @typing.overload
    def MakeUnary(unaryType: int, operand: System.Linq.Expressions.Expression, type: System.Type, method: System.Reflection.MethodInfo, ) -> System.Linq.Expressions.UnaryExpression:
        ...

    @staticmethod
    def GetUserDefinedUnaryOperatorOrThrow(unaryType: int, name: str, operand: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.UnaryExpression:
        ...

    @staticmethod
    def GetUserDefinedUnaryOperator(unaryType: int, name: str, operand: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.UnaryExpression:
        ...

    @staticmethod
    def GetMethodBasedUnaryOperator(unaryType: int, operand: System.Linq.Expressions.Expression, method: System.Reflection.MethodInfo, ) -> System.Linq.Expressions.UnaryExpression:
        ...

    @staticmethod
    def GetUserDefinedCoercionOrThrow(coercionType: int, expression: System.Linq.Expressions.Expression, convertToType: System.Type, ) -> System.Linq.Expressions.UnaryExpression:
        ...

    @staticmethod
    def GetUserDefinedCoercion(coercionType: int, expression: System.Linq.Expressions.Expression, convertToType: System.Type, ) -> System.Linq.Expressions.UnaryExpression:
        ...

    @staticmethod
    def GetMethodBasedCoercionOperator(unaryType: int, operand: System.Linq.Expressions.Expression, convertToType: System.Type, method: System.Reflection.MethodInfo, ) -> System.Linq.Expressions.UnaryExpression:
        ...

    @staticmethod
    @typing.overload
    def Negate(expression: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.UnaryExpression:
        ...

    @staticmethod
    @typing.overload
    def Negate(expression: System.Linq.Expressions.Expression, method: System.Reflection.MethodInfo, ) -> System.Linq.Expressions.UnaryExpression:
        ...

    @staticmethod
    @typing.overload
    def UnaryPlus(expression: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.UnaryExpression:
        ...

    @staticmethod
    @typing.overload
    def UnaryPlus(expression: System.Linq.Expressions.Expression, method: System.Reflection.MethodInfo, ) -> System.Linq.Expressions.UnaryExpression:
        ...

    @staticmethod
    @typing.overload
    def NegateChecked(expression: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.UnaryExpression:
        ...

    @staticmethod
    @typing.overload
    def NegateChecked(expression: System.Linq.Expressions.Expression, method: System.Reflection.MethodInfo, ) -> System.Linq.Expressions.UnaryExpression:
        ...

    @staticmethod
    @typing.overload
    def Not(expression: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.UnaryExpression:
        ...

    @staticmethod
    @typing.overload
    def Not(expression: System.Linq.Expressions.Expression, method: System.Reflection.MethodInfo, ) -> System.Linq.Expressions.UnaryExpression:
        ...

    @staticmethod
    @typing.overload
    def IsFalse(expression: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.UnaryExpression:
        ...

    @staticmethod
    @typing.overload
    def IsFalse(expression: System.Linq.Expressions.Expression, method: System.Reflection.MethodInfo, ) -> System.Linq.Expressions.UnaryExpression:
        ...

    @staticmethod
    @typing.overload
    def IsTrue(expression: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.UnaryExpression:
        ...

    @staticmethod
    @typing.overload
    def IsTrue(expression: System.Linq.Expressions.Expression, method: System.Reflection.MethodInfo, ) -> System.Linq.Expressions.UnaryExpression:
        ...

    @staticmethod
    @typing.overload
    def OnesComplement(expression: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.UnaryExpression:
        ...

    @staticmethod
    @typing.overload
    def OnesComplement(expression: System.Linq.Expressions.Expression, method: System.Reflection.MethodInfo, ) -> System.Linq.Expressions.UnaryExpression:
        ...

    @staticmethod
    def TypeAs(expression: System.Linq.Expressions.Expression, type: System.Type, ) -> System.Linq.Expressions.UnaryExpression:
        ...

    @staticmethod
    def Unbox(expression: System.Linq.Expressions.Expression, type: System.Type, ) -> System.Linq.Expressions.UnaryExpression:
        ...

    @staticmethod
    @typing.overload
    def Convert(expression: System.Linq.Expressions.Expression, type: System.Type, ) -> System.Linq.Expressions.UnaryExpression:
        ...

    @staticmethod
    @typing.overload
    def Convert(expression: System.Linq.Expressions.Expression, type: System.Type, method: System.Reflection.MethodInfo, ) -> System.Linq.Expressions.UnaryExpression:
        ...

    @staticmethod
    @typing.overload
    def ConvertChecked(expression: System.Linq.Expressions.Expression, type: System.Type, ) -> System.Linq.Expressions.UnaryExpression:
        ...

    @staticmethod
    @typing.overload
    def ConvertChecked(expression: System.Linq.Expressions.Expression, type: System.Type, method: System.Reflection.MethodInfo, ) -> System.Linq.Expressions.UnaryExpression:
        ...

    @staticmethod
    def ArrayLength(array: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.UnaryExpression:
        ...

    @staticmethod
    def Quote(expression: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.UnaryExpression:
        ...

    @staticmethod
    @typing.overload
    def Rethrow() -> System.Linq.Expressions.UnaryExpression:
        ...

    @staticmethod
    @typing.overload
    def Rethrow(type: System.Type, ) -> System.Linq.Expressions.UnaryExpression:
        ...

    @staticmethod
    @typing.overload
    def Throw(value: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.UnaryExpression:
        ...

    @staticmethod
    @typing.overload
    def Throw(value: System.Linq.Expressions.Expression, type: System.Type, ) -> System.Linq.Expressions.UnaryExpression:
        ...

    @staticmethod
    @typing.overload
    def Increment(expression: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.UnaryExpression:
        ...

    @staticmethod
    @typing.overload
    def Increment(expression: System.Linq.Expressions.Expression, method: System.Reflection.MethodInfo, ) -> System.Linq.Expressions.UnaryExpression:
        ...

    @staticmethod
    @typing.overload
    def Decrement(expression: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.UnaryExpression:
        ...

    @staticmethod
    @typing.overload
    def Decrement(expression: System.Linq.Expressions.Expression, method: System.Reflection.MethodInfo, ) -> System.Linq.Expressions.UnaryExpression:
        ...

    @staticmethod
    @typing.overload
    def PreIncrementAssign(expression: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.UnaryExpression:
        ...

    @staticmethod
    @typing.overload
    def PreIncrementAssign(expression: System.Linq.Expressions.Expression, method: System.Reflection.MethodInfo, ) -> System.Linq.Expressions.UnaryExpression:
        ...

    @staticmethod
    @typing.overload
    def PreDecrementAssign(expression: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.UnaryExpression:
        ...

    @staticmethod
    @typing.overload
    def PreDecrementAssign(expression: System.Linq.Expressions.Expression, method: System.Reflection.MethodInfo, ) -> System.Linq.Expressions.UnaryExpression:
        ...

    @staticmethod
    @typing.overload
    def PostIncrementAssign(expression: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.UnaryExpression:
        ...

    @staticmethod
    @typing.overload
    def PostIncrementAssign(expression: System.Linq.Expressions.Expression, method: System.Reflection.MethodInfo, ) -> System.Linq.Expressions.UnaryExpression:
        ...

    @staticmethod
    @typing.overload
    def PostDecrementAssign(expression: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.UnaryExpression:
        ...

    @staticmethod
    @typing.overload
    def PostDecrementAssign(expression: System.Linq.Expressions.Expression, method: System.Reflection.MethodInfo, ) -> System.Linq.Expressions.UnaryExpression:
        ...

    @staticmethod
    def MakeOpAssignUnary(kind: int, expression: System.Linq.Expressions.Expression, method: System.Reflection.MethodInfo, ) -> System.Linq.Expressions.UnaryExpression:
        ...

    @staticmethod
    @typing.overload
    def ListInit(newExpression: System.Linq.Expressions.NewExpression, initializers: System.Collections.Generic.IEnumerable[System.Linq.Expressions.ElementInit], ) -> System.Linq.Expressions.ListInitExpression:
        ...

    @staticmethod
    @typing.overload
    def ListInit(newExpression: System.Linq.Expressions.NewExpression, initializers: System.Array[System.Linq.Expressions.Expression], ) -> System.Linq.Expressions.ListInitExpression:
        ...

    @staticmethod
    @typing.overload
    def ListInit(newExpression: System.Linq.Expressions.NewExpression, initializers: System.Collections.Generic.IEnumerable[System.Linq.Expressions.Expression], ) -> System.Linq.Expressions.ListInitExpression:
        ...

    @staticmethod
    @typing.overload
    def ListInit(newExpression: System.Linq.Expressions.NewExpression, addMethod: System.Reflection.MethodInfo, initializers: System.Array[System.Linq.Expressions.Expression], ) -> System.Linq.Expressions.ListInitExpression:
        ...

    @staticmethod
    @typing.overload
    def ListInit(newExpression: System.Linq.Expressions.NewExpression, addMethod: System.Reflection.MethodInfo, initializers: System.Collections.Generic.IEnumerable[System.Linq.Expressions.Expression], ) -> System.Linq.Expressions.ListInitExpression:
        ...

    @staticmethod
    @typing.overload
    def ListInit(newExpression: System.Linq.Expressions.NewExpression, initializers: System.Array[System.Linq.Expressions.ElementInit], ) -> System.Linq.Expressions.ListInitExpression:
        ...

    @staticmethod
    @typing.overload
    def Loop(body: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.LoopExpression:
        ...

    @staticmethod
    @typing.overload
    def Loop(body: System.Linq.Expressions.Expression, break_: System.Linq.Expressions.LabelTarget, ) -> System.Linq.Expressions.LoopExpression:
        ...

    @staticmethod
    @typing.overload
    def Loop(body: System.Linq.Expressions.Expression, break_: System.Linq.Expressions.LabelTarget, continue_: System.Linq.Expressions.LabelTarget, ) -> System.Linq.Expressions.LoopExpression:
        ...

    @staticmethod
    @typing.overload
    def Bind(member: System.Reflection.MemberInfo, expression: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.MemberAssignment:
        ...

    @staticmethod
    @typing.overload
    def Bind(propertyAccessor: System.Reflection.MethodInfo, expression: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.MemberAssignment:
        ...

    @staticmethod
    def ValidateSettableFieldOrPropertyMember(member: System.Reflection.MemberInfo, memberType: ref[System.Type], ) -> None:
        ...

    @staticmethod
    @typing.overload
    def Field(expression: System.Linq.Expressions.Expression, field: System.Reflection.FieldInfo, ) -> System.Linq.Expressions.MemberExpression:
        ...

    @staticmethod
    @typing.overload
    def Field(expression: System.Linq.Expressions.Expression, fieldName: str, ) -> System.Linq.Expressions.MemberExpression:
        ...

    @staticmethod
    @typing.overload
    def Field(expression: System.Linq.Expressions.Expression, type: System.Type, fieldName: str, ) -> System.Linq.Expressions.MemberExpression:
        ...

    @staticmethod
    @typing.overload
    def Property(expression: System.Linq.Expressions.Expression, propertyName: str, ) -> System.Linq.Expressions.MemberExpression:
        ...

    @staticmethod
    @typing.overload
    def Property(expression: System.Linq.Expressions.Expression, type: System.Type, propertyName: str, ) -> System.Linq.Expressions.MemberExpression:
        ...

    @staticmethod
    @typing.overload
    def Property(expression: System.Linq.Expressions.Expression, property: System.Reflection.PropertyInfo, ) -> System.Linq.Expressions.MemberExpression:
        ...

    @staticmethod
    @typing.overload
    def Property(expression: System.Linq.Expressions.Expression, propertyAccessor: System.Reflection.MethodInfo, ) -> System.Linq.Expressions.MemberExpression:
        ...

    @staticmethod
    @typing.overload
    def Property(instance: System.Linq.Expressions.Expression, propertyName: str, arguments: System.Array[System.Linq.Expressions.Expression], ) -> System.Linq.Expressions.IndexExpression:
        ...

    @staticmethod
    @typing.overload
    def Property(instance: System.Linq.Expressions.Expression, indexer: System.Reflection.PropertyInfo, arguments: System.Array[System.Linq.Expressions.Expression], ) -> System.Linq.Expressions.IndexExpression:
        ...

    @staticmethod
    @typing.overload
    def Property(instance: System.Linq.Expressions.Expression, indexer: System.Reflection.PropertyInfo, arguments: System.Collections.Generic.IEnumerable[System.Linq.Expressions.Expression], ) -> System.Linq.Expressions.IndexExpression:
        ...

    @staticmethod
    def GetProperty(mi: System.Reflection.MethodInfo, paramName: str, index: int = ..., ) -> System.Reflection.PropertyInfo:
        ...

    @staticmethod
    def CheckMethod(method: System.Reflection.MethodInfo, propertyMethod: System.Reflection.MethodInfo, ) -> bool:
        ...

    @staticmethod
    def PropertyOrField(expression: System.Linq.Expressions.Expression, propertyOrFieldName: str, ) -> System.Linq.Expressions.MemberExpression:
        ...

    @staticmethod
    def MakeMemberAccess(expression: System.Linq.Expressions.Expression, member: System.Reflection.MemberInfo, ) -> System.Linq.Expressions.MemberExpression:
        ...

    @staticmethod
    @typing.overload
    def MemberInit(newExpression: System.Linq.Expressions.NewExpression, bindings: System.Array[System.Linq.Expressions.MemberBinding], ) -> System.Linq.Expressions.MemberInitExpression:
        ...

    @staticmethod
    @typing.overload
    def MemberInit(newExpression: System.Linq.Expressions.NewExpression, bindings: System.Collections.Generic.IEnumerable[System.Linq.Expressions.MemberBinding], ) -> System.Linq.Expressions.MemberInitExpression:
        ...

    @staticmethod
    @typing.overload
    def ListBind(member: System.Reflection.MemberInfo, initializers: System.Array[System.Linq.Expressions.ElementInit], ) -> System.Linq.Expressions.MemberListBinding:
        ...

    @staticmethod
    @typing.overload
    def ListBind(member: System.Reflection.MemberInfo, initializers: System.Collections.Generic.IEnumerable[System.Linq.Expressions.ElementInit], ) -> System.Linq.Expressions.MemberListBinding:
        ...

    @staticmethod
    @typing.overload
    def ListBind(propertyAccessor: System.Reflection.MethodInfo, initializers: System.Array[System.Linq.Expressions.ElementInit], ) -> System.Linq.Expressions.MemberListBinding:
        ...

    @staticmethod
    @typing.overload
    def ListBind(propertyAccessor: System.Reflection.MethodInfo, initializers: System.Collections.Generic.IEnumerable[System.Linq.Expressions.ElementInit], ) -> System.Linq.Expressions.MemberListBinding:
        ...

    @staticmethod
    def ValidateListInitArgs(listType: System.Type, initializers: System.Collections.ObjectModel.ReadOnlyCollection[System.Linq.Expressions.ElementInit], listTypeParamName: str, ) -> None:
        ...

    @staticmethod
    @typing.overload
    def MemberBind(member: System.Reflection.MemberInfo, bindings: System.Array[System.Linq.Expressions.MemberBinding], ) -> System.Linq.Expressions.MemberMemberBinding:
        ...

    @staticmethod
    @typing.overload
    def MemberBind(member: System.Reflection.MemberInfo, bindings: System.Collections.Generic.IEnumerable[System.Linq.Expressions.MemberBinding], ) -> System.Linq.Expressions.MemberMemberBinding:
        ...

    @staticmethod
    @typing.overload
    def MemberBind(propertyAccessor: System.Reflection.MethodInfo, bindings: System.Array[System.Linq.Expressions.MemberBinding], ) -> System.Linq.Expressions.MemberMemberBinding:
        ...

    @staticmethod
    @typing.overload
    def MemberBind(propertyAccessor: System.Reflection.MethodInfo, bindings: System.Collections.Generic.IEnumerable[System.Linq.Expressions.MemberBinding], ) -> System.Linq.Expressions.MemberMemberBinding:
        ...

    @staticmethod
    def ValidateGettableFieldOrPropertyMember(member: System.Reflection.MemberInfo, memberType: ref[System.Type], ) -> None:
        ...

    @staticmethod
    def ValidateMemberInitArgs(type: System.Type, bindings: System.Collections.ObjectModel.ReadOnlyCollection[System.Linq.Expressions.MemberBinding], ) -> None:
        ...

    @staticmethod
    @typing.overload
    def Call(method: System.Reflection.MethodInfo, ) -> System.Linq.Expressions.MethodCallExpression:
        ...

    @staticmethod
    @typing.overload
    def Call(method: System.Reflection.MethodInfo, arg0: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.MethodCallExpression:
        ...

    @staticmethod
    @typing.overload
    def Call(method: System.Reflection.MethodInfo, arg0: System.Linq.Expressions.Expression, arg1: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.MethodCallExpression:
        ...

    @staticmethod
    @typing.overload
    def Call(method: System.Reflection.MethodInfo, arg0: System.Linq.Expressions.Expression, arg1: System.Linq.Expressions.Expression, arg2: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.MethodCallExpression:
        ...

    @staticmethod
    @typing.overload
    def Call(method: System.Reflection.MethodInfo, arg0: System.Linq.Expressions.Expression, arg1: System.Linq.Expressions.Expression, arg2: System.Linq.Expressions.Expression, arg3: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.MethodCallExpression:
        ...

    @staticmethod
    @typing.overload
    def Call(method: System.Reflection.MethodInfo, arg0: System.Linq.Expressions.Expression, arg1: System.Linq.Expressions.Expression, arg2: System.Linq.Expressions.Expression, arg3: System.Linq.Expressions.Expression, arg4: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.MethodCallExpression:
        ...

    @staticmethod
    @typing.overload
    def Call(method: System.Reflection.MethodInfo, arguments: System.Array[System.Linq.Expressions.Expression], ) -> System.Linq.Expressions.MethodCallExpression:
        ...

    @staticmethod
    @typing.overload
    def Call(method: System.Reflection.MethodInfo, arguments: System.Collections.Generic.IEnumerable[System.Linq.Expressions.Expression], ) -> System.Linq.Expressions.MethodCallExpression:
        ...

    @staticmethod
    @typing.overload
    def Call(instance: System.Linq.Expressions.Expression, method: System.Reflection.MethodInfo, ) -> System.Linq.Expressions.MethodCallExpression:
        ...

    @staticmethod
    @typing.overload
    def Call(instance: System.Linq.Expressions.Expression, method: System.Reflection.MethodInfo, arguments: System.Array[System.Linq.Expressions.Expression], ) -> System.Linq.Expressions.MethodCallExpression:
        ...

    @staticmethod
    @typing.overload
    def Call(instance: System.Linq.Expressions.Expression, method: System.Reflection.MethodInfo, arg0: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.MethodCallExpression:
        ...

    @staticmethod
    @typing.overload
    def Call(instance: System.Linq.Expressions.Expression, method: System.Reflection.MethodInfo, arg0: System.Linq.Expressions.Expression, arg1: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.MethodCallExpression:
        ...

    @staticmethod
    @typing.overload
    def Call(instance: System.Linq.Expressions.Expression, method: System.Reflection.MethodInfo, arg0: System.Linq.Expressions.Expression, arg1: System.Linq.Expressions.Expression, arg2: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.MethodCallExpression:
        ...

    @staticmethod
    @typing.overload
    def Call(instance: System.Linq.Expressions.Expression, methodName: str, typeArguments: System.Array[System.Type], arguments: System.Array[System.Linq.Expressions.Expression], ) -> System.Linq.Expressions.MethodCallExpression:
        ...

    @staticmethod
    @typing.overload
    def Call(type: System.Type, methodName: str, typeArguments: System.Array[System.Type], arguments: System.Array[System.Linq.Expressions.Expression], ) -> System.Linq.Expressions.MethodCallExpression:
        ...

    @staticmethod
    @typing.overload
    def Call(instance: System.Linq.Expressions.Expression, method: System.Reflection.MethodInfo, arguments: System.Collections.Generic.IEnumerable[System.Linq.Expressions.Expression], ) -> System.Linq.Expressions.MethodCallExpression:
        ...

    @staticmethod
    def ValidateMethodAndGetParameters(instance: System.Linq.Expressions.Expression, method: System.Reflection.MethodInfo, ) -> System.Array[System.Reflection.ParameterInfo]:
        ...

    @staticmethod
    def ValidateStaticOrInstanceMethod(instance: System.Linq.Expressions.Expression, method: System.Reflection.MethodInfo, ) -> None:
        ...

    @staticmethod
    def ValidateCallInstanceType(instanceType: System.Type, method: System.Reflection.MethodInfo, ) -> None:
        ...

    @staticmethod
    def ValidateArgumentTypes(method: System.Reflection.MethodBase, nodeKind: int, arguments: ref[System.Collections.ObjectModel.ReadOnlyCollection[System.Linq.Expressions.Expression]], methodParamName: str, ) -> None:
        ...

    @staticmethod
    def GetParametersForValidation(method: System.Reflection.MethodBase, nodeKind: int, ) -> System.Array[System.Reflection.ParameterInfo]:
        ...

    @staticmethod
    def ValidateArgumentCount(method: System.Reflection.MethodBase, nodeKind: int, count: int, pis: System.Array[System.Reflection.ParameterInfo], ) -> None:
        ...

    @staticmethod
    def ValidateOneArgument(method: System.Reflection.MethodBase, nodeKind: int, arg: System.Linq.Expressions.Expression, pi: System.Reflection.ParameterInfo, methodParamName: str, argumentParamName: str, ) -> System.Linq.Expressions.Expression:
        ...

    @staticmethod
    def TryQuote(parameterType: System.Type, argument: ref[System.Linq.Expressions.Expression], ) -> bool:
        ...

    @staticmethod
    def FindMethod(type: System.Type, methodName: str, typeArgs: System.Array[System.Type], args: System.Array[System.Linq.Expressions.Expression], flags: int, ) -> System.Reflection.MethodInfo:
        ...

    @staticmethod
    @typing.overload
    def IsCompatible(m: System.Reflection.MethodBase, arguments: System.Array[System.Linq.Expressions.Expression], ) -> bool:
        ...

    @staticmethod
    @typing.overload
    def IsCompatible(pi: System.Reflection.PropertyInfo, args: System.Array[System.Linq.Expressions.Expression], ) -> bool:
        ...

    @staticmethod
    def ApplyTypeArgs(m: System.Reflection.MethodInfo, typeArgs: System.Array[System.Type], ) -> System.Reflection.MethodInfo:
        ...

    @staticmethod
    @typing.overload
    def ArrayIndex(array: System.Linq.Expressions.Expression, indexes: System.Array[System.Linq.Expressions.Expression], ) -> System.Linq.Expressions.MethodCallExpression:
        ...

    @staticmethod
    @typing.overload
    def ArrayIndex(array: System.Linq.Expressions.Expression, indexes: System.Collections.Generic.IEnumerable[System.Linq.Expressions.Expression], ) -> System.Linq.Expressions.MethodCallExpression:
        ...

    @staticmethod
    @typing.overload
    def ArrayIndex(array: System.Linq.Expressions.Expression, index: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.BinaryExpression:
        ...

    @staticmethod
    @typing.overload
    def NewArrayInit(type: System.Type, initializers: System.Array[System.Linq.Expressions.Expression], ) -> System.Linq.Expressions.NewArrayExpression:
        ...

    @staticmethod
    @typing.overload
    def NewArrayInit(type: System.Type, initializers: System.Collections.Generic.IEnumerable[System.Linq.Expressions.Expression], ) -> System.Linq.Expressions.NewArrayExpression:
        ...

    @staticmethod
    @typing.overload
    def NewArrayBounds(type: System.Type, bounds: System.Array[System.Linq.Expressions.Expression], ) -> System.Linq.Expressions.NewArrayExpression:
        ...

    @staticmethod
    @typing.overload
    def NewArrayBounds(type: System.Type, bounds: System.Collections.Generic.IEnumerable[System.Linq.Expressions.Expression], ) -> System.Linq.Expressions.NewArrayExpression:
        ...

    @staticmethod
    @typing.overload
    def New(constructor: System.Reflection.ConstructorInfo, ) -> System.Linq.Expressions.NewExpression:
        ...

    @staticmethod
    @typing.overload
    def New(constructor: System.Reflection.ConstructorInfo, arguments: System.Array[System.Linq.Expressions.Expression], ) -> System.Linq.Expressions.NewExpression:
        ...

    @staticmethod
    @typing.overload
    def New(constructor: System.Reflection.ConstructorInfo, arguments: System.Collections.Generic.IEnumerable[System.Linq.Expressions.Expression], ) -> System.Linq.Expressions.NewExpression:
        ...

    @staticmethod
    @typing.overload
    def New(constructor: System.Reflection.ConstructorInfo, arguments: System.Collections.Generic.IEnumerable[System.Linq.Expressions.Expression], members: System.Collections.Generic.IEnumerable[System.Reflection.MemberInfo], ) -> System.Linq.Expressions.NewExpression:
        ...

    @staticmethod
    @typing.overload
    def New(constructor: System.Reflection.ConstructorInfo, arguments: System.Collections.Generic.IEnumerable[System.Linq.Expressions.Expression], members: System.Array[System.Reflection.MemberInfo], ) -> System.Linq.Expressions.NewExpression:
        ...

    @staticmethod
    @typing.overload
    def New(type: System.Type, ) -> System.Linq.Expressions.NewExpression:
        ...

    @staticmethod
    def ValidateNewArgs(constructor: System.Reflection.ConstructorInfo, arguments: ref[System.Collections.ObjectModel.ReadOnlyCollection[System.Linq.Expressions.Expression]], members: ref[System.Collections.ObjectModel.ReadOnlyCollection[System.Reflection.MemberInfo]], ) -> None:
        ...

    @staticmethod
    def ValidateAnonymousTypeMember(member: ref[System.Reflection.MemberInfo], memberType: ref[System.Type], paramName: str, index: int, ) -> None:
        ...

    @staticmethod
    def ValidateConstructor(constructor: System.Reflection.ConstructorInfo, paramName: str, ) -> None:
        ...

    @staticmethod
    @typing.overload
    def Parameter(type: System.Type, ) -> System.Linq.Expressions.ParameterExpression:
        ...

    @staticmethod
    @typing.overload
    def Parameter(type: System.Type, name: str, ) -> System.Linq.Expressions.ParameterExpression:
        ...

    @staticmethod
    @typing.overload
    def Variable(type: System.Type, ) -> System.Linq.Expressions.ParameterExpression:
        ...

    @staticmethod
    @typing.overload
    def Variable(type: System.Type, name: str, ) -> System.Linq.Expressions.ParameterExpression:
        ...

    @staticmethod
    def Validate(type: System.Type, allowByRef: bool, ) -> None:
        ...

    @staticmethod
    @typing.overload
    def RuntimeVariables(variables: System.Array[System.Linq.Expressions.ParameterExpression], ) -> System.Linq.Expressions.RuntimeVariablesExpression:
        ...

    @staticmethod
    @typing.overload
    def RuntimeVariables(variables: System.Collections.Generic.IEnumerable[System.Linq.Expressions.ParameterExpression], ) -> System.Linq.Expressions.RuntimeVariablesExpression:
        ...

    @staticmethod
    @typing.overload
    def SwitchCase(body: System.Linq.Expressions.Expression, testValues: System.Array[System.Linq.Expressions.Expression], ) -> System.Linq.Expressions.SwitchCase:
        ...

    @staticmethod
    @typing.overload
    def SwitchCase(body: System.Linq.Expressions.Expression, testValues: System.Collections.Generic.IEnumerable[System.Linq.Expressions.Expression], ) -> System.Linq.Expressions.SwitchCase:
        ...

    @staticmethod
    @typing.overload
    def MakeDynamic(delegateType: System.Type, binder: System.Runtime.CompilerServices.CallSiteBinder, arg0: System.Linq.Expressions.Expression, arg1: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.DynamicExpression:
        ...

    @staticmethod
    @typing.overload
    def MakeDynamic(delegateType: System.Type, binder: System.Runtime.CompilerServices.CallSiteBinder, arg0: System.Linq.Expressions.Expression, arg1: System.Linq.Expressions.Expression, arg2: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.DynamicExpression:
        ...

    @staticmethod
    @typing.overload
    def MakeDynamic(delegateType: System.Type, binder: System.Runtime.CompilerServices.CallSiteBinder, arg0: System.Linq.Expressions.Expression, arg1: System.Linq.Expressions.Expression, arg2: System.Linq.Expressions.Expression, arg3: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.DynamicExpression:
        ...

    @staticmethod
    @typing.overload
    def MakeDynamic(delegateType: System.Type, binder: System.Runtime.CompilerServices.CallSiteBinder, arguments: System.Array[System.Linq.Expressions.Expression], ) -> System.Linq.Expressions.DynamicExpression:
        ...

    @staticmethod
    @typing.overload
    def MakeDynamic(delegateType: System.Type, binder: System.Runtime.CompilerServices.CallSiteBinder, arguments: System.Collections.Generic.IEnumerable[System.Linq.Expressions.Expression], ) -> System.Linq.Expressions.DynamicExpression:
        ...

    @staticmethod
    @typing.overload
    def MakeDynamic(delegateType: System.Type, binder: System.Runtime.CompilerServices.CallSiteBinder, arg0: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.DynamicExpression:
        ...

    @staticmethod
    @typing.overload
    def Break(target: System.Linq.Expressions.LabelTarget, ) -> System.Linq.Expressions.GotoExpression:
        ...

    @staticmethod
    @typing.overload
    def Break(target: System.Linq.Expressions.LabelTarget, value: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.GotoExpression:
        ...

    @staticmethod
    @typing.overload
    def Break(target: System.Linq.Expressions.LabelTarget, type: System.Type, ) -> System.Linq.Expressions.GotoExpression:
        ...

    @staticmethod
    @typing.overload
    def Break(target: System.Linq.Expressions.LabelTarget, value: System.Linq.Expressions.Expression, type: System.Type, ) -> System.Linq.Expressions.GotoExpression:
        ...

    @staticmethod
    @typing.overload
    def Continue(target: System.Linq.Expressions.LabelTarget, ) -> System.Linq.Expressions.GotoExpression:
        ...

    @staticmethod
    @typing.overload
    def Continue(target: System.Linq.Expressions.LabelTarget, type: System.Type, ) -> System.Linq.Expressions.GotoExpression:
        ...

    @staticmethod
    @typing.overload
    def Return(target: System.Linq.Expressions.LabelTarget, ) -> System.Linq.Expressions.GotoExpression:
        ...

    @staticmethod
    @typing.overload
    def Return(target: System.Linq.Expressions.LabelTarget, type: System.Type, ) -> System.Linq.Expressions.GotoExpression:
        ...

    @staticmethod
    @typing.overload
    def Return(target: System.Linq.Expressions.LabelTarget, value: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.GotoExpression:
        ...

    @staticmethod
    @typing.overload
    def Return(target: System.Linq.Expressions.LabelTarget, value: System.Linq.Expressions.Expression, type: System.Type, ) -> System.Linq.Expressions.GotoExpression:
        ...

    @staticmethod
    @typing.overload
    def Goto(target: System.Linq.Expressions.LabelTarget, ) -> System.Linq.Expressions.GotoExpression:
        ...

    @staticmethod
    @typing.overload
    def Goto(target: System.Linq.Expressions.LabelTarget, type: System.Type, ) -> System.Linq.Expressions.GotoExpression:
        ...

    @staticmethod
    @typing.overload
    def Goto(target: System.Linq.Expressions.LabelTarget, value: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.GotoExpression:
        ...

    @staticmethod
    @typing.overload
    def Goto(target: System.Linq.Expressions.LabelTarget, value: System.Linq.Expressions.Expression, type: System.Type, ) -> System.Linq.Expressions.GotoExpression:
        ...

    @staticmethod
    def MakeGoto(kind: int, target: System.Linq.Expressions.LabelTarget, value: System.Linq.Expressions.Expression, type: System.Type, ) -> System.Linq.Expressions.GotoExpression:
        ...

    @staticmethod
    def ValidateGoto(target: System.Linq.Expressions.LabelTarget, value: ref[System.Linq.Expressions.Expression], targetParameter: str, valueParameter: str, type: System.Type, ) -> None:
        ...

    @staticmethod
    def ValidateGotoType(expectedType: System.Type, value: ref[System.Linq.Expressions.Expression], paramName: str, ) -> None:
        ...

    @staticmethod
    def MakeIndex(instance: System.Linq.Expressions.Expression, indexer: System.Reflection.PropertyInfo, arguments: System.Collections.Generic.IEnumerable[System.Linq.Expressions.Expression], ) -> System.Linq.Expressions.IndexExpression:
        ...

    @staticmethod
    @typing.overload
    def ArrayAccess(array: System.Linq.Expressions.Expression, indexes: System.Array[System.Linq.Expressions.Expression], ) -> System.Linq.Expressions.IndexExpression:
        ...

    @staticmethod
    @typing.overload
    def ArrayAccess(array: System.Linq.Expressions.Expression, indexes: System.Collections.Generic.IEnumerable[System.Linq.Expressions.Expression], ) -> System.Linq.Expressions.IndexExpression:
        ...

    @staticmethod
    def FindInstanceProperty(type: System.Type, propertyName: str, arguments: System.Array[System.Linq.Expressions.Expression], ) -> System.Reflection.PropertyInfo:
        ...

    @staticmethod
    def GetArgTypesString(arguments: System.Array[System.Linq.Expressions.Expression], ) -> str:
        ...

    @staticmethod
    def FindProperty(type: System.Type, propertyName: str, arguments: System.Array[System.Linq.Expressions.Expression], flags: int, ) -> System.Reflection.PropertyInfo:
        ...

    @staticmethod
    def MakeIndexProperty(instance: System.Linq.Expressions.Expression, indexer: System.Reflection.PropertyInfo, paramName: str, argList: System.Collections.ObjectModel.ReadOnlyCollection[System.Linq.Expressions.Expression], ) -> System.Linq.Expressions.IndexExpression:
        ...

    @staticmethod
    def ValidateIndexedProperty(instance: System.Linq.Expressions.Expression, indexer: System.Reflection.PropertyInfo, paramName: str, argList: ref[System.Collections.ObjectModel.ReadOnlyCollection[System.Linq.Expressions.Expression]], ) -> None:
        ...

    @staticmethod
    def ValidateAccessor(instance: System.Linq.Expressions.Expression, method: System.Reflection.MethodInfo, indexes: System.Array[System.Reflection.ParameterInfo], arguments: ref[System.Collections.ObjectModel.ReadOnlyCollection[System.Linq.Expressions.Expression]], paramName: str, ) -> None:
        ...

    @staticmethod
    def ValidateAccessorArgumentTypes(method: System.Reflection.MethodInfo, indexes: System.Array[System.Reflection.ParameterInfo], arguments: ref[System.Collections.ObjectModel.ReadOnlyCollection[System.Linq.Expressions.Expression]], paramName: str, ) -> None:
        ...

    @staticmethod
    @typing.overload
    def Invoke(expression: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.InvocationExpression:
        ...

    @staticmethod
    @typing.overload
    def Invoke(expression: System.Linq.Expressions.Expression, arg0: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.InvocationExpression:
        ...

    @staticmethod
    @typing.overload
    def Invoke(expression: System.Linq.Expressions.Expression, arg0: System.Linq.Expressions.Expression, arg1: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.InvocationExpression:
        ...

    @staticmethod
    @typing.overload
    def Invoke(expression: System.Linq.Expressions.Expression, arg0: System.Linq.Expressions.Expression, arg1: System.Linq.Expressions.Expression, arg2: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.InvocationExpression:
        ...

    @staticmethod
    @typing.overload
    def Invoke(expression: System.Linq.Expressions.Expression, arg0: System.Linq.Expressions.Expression, arg1: System.Linq.Expressions.Expression, arg2: System.Linq.Expressions.Expression, arg3: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.InvocationExpression:
        ...

    @staticmethod
    @typing.overload
    def Invoke(expression: System.Linq.Expressions.Expression, arg0: System.Linq.Expressions.Expression, arg1: System.Linq.Expressions.Expression, arg2: System.Linq.Expressions.Expression, arg3: System.Linq.Expressions.Expression, arg4: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.InvocationExpression:
        ...

    @staticmethod
    @typing.overload
    def Invoke(expression: System.Linq.Expressions.Expression, arguments: System.Array[System.Linq.Expressions.Expression], ) -> System.Linq.Expressions.InvocationExpression:
        ...

    @staticmethod
    @typing.overload
    def Invoke(expression: System.Linq.Expressions.Expression, arguments: System.Collections.Generic.IEnumerable[System.Linq.Expressions.Expression], ) -> System.Linq.Expressions.InvocationExpression:
        ...

    @staticmethod
    def GetInvokeMethod(expression: System.Linq.Expressions.Expression, ) -> System.Reflection.MethodInfo:
        ...

    @staticmethod
    @typing.overload
    def Label(target: System.Linq.Expressions.LabelTarget, ) -> System.Linq.Expressions.LabelExpression:
        ...

    @staticmethod
    @typing.overload
    def Label(target: System.Linq.Expressions.LabelTarget, defaultValue: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.LabelExpression:
        ...

    @staticmethod
    @typing.overload
    def Label() -> System.Linq.Expressions.LabelTarget:
        ...

    @staticmethod
    @typing.overload
    def Label(name: str, ) -> System.Linq.Expressions.LabelTarget:
        ...

    @staticmethod
    @typing.overload
    def Label(type: System.Type, ) -> System.Linq.Expressions.LabelTarget:
        ...

    @staticmethod
    @typing.overload
    def Label(type: System.Type, name: str, ) -> System.Linq.Expressions.LabelTarget:
        ...

    @staticmethod
    def CreateLambda(delegateType: System.Type, body: System.Linq.Expressions.Expression, name: str, tailCall: bool, parameters: System.Collections.ObjectModel.ReadOnlyCollection[System.Linq.Expressions.ParameterExpression], ) -> System.Linq.Expressions.LambdaExpression:
        ...

    @staticmethod
    @typing.overload
    def Lambda(body: System.Linq.Expressions.Expression, parameters: System.Array[System.Linq.Expressions.ParameterExpression], ) -> System.Linq.Expressions.Expression[TDelegate]:
        ...

    @staticmethod
    @typing.overload
    def Lambda(body: System.Linq.Expressions.Expression, tailCall: bool, parameters: System.Array[System.Linq.Expressions.ParameterExpression], ) -> System.Linq.Expressions.Expression[TDelegate]:
        ...

    @staticmethod
    @typing.overload
    def Lambda(body: System.Linq.Expressions.Expression, parameters: System.Collections.Generic.IEnumerable[System.Linq.Expressions.ParameterExpression], ) -> System.Linq.Expressions.Expression[TDelegate]:
        ...

    @staticmethod
    @typing.overload
    def Lambda(body: System.Linq.Expressions.Expression, tailCall: bool, parameters: System.Collections.Generic.IEnumerable[System.Linq.Expressions.ParameterExpression], ) -> System.Linq.Expressions.Expression[TDelegate]:
        ...

    @staticmethod
    @typing.overload
    def Lambda(body: System.Linq.Expressions.Expression, name: str, parameters: System.Collections.Generic.IEnumerable[System.Linq.Expressions.ParameterExpression], ) -> System.Linq.Expressions.Expression[TDelegate]:
        ...

    @staticmethod
    @typing.overload
    def Lambda(body: System.Linq.Expressions.Expression, name: str, tailCall: bool, parameters: System.Collections.Generic.IEnumerable[System.Linq.Expressions.ParameterExpression], ) -> System.Linq.Expressions.Expression[TDelegate]:
        ...

    @staticmethod
    @typing.overload
    def Lambda(body: System.Linq.Expressions.Expression, parameters: System.Array[System.Linq.Expressions.ParameterExpression], ) -> System.Linq.Expressions.LambdaExpression:
        ...

    @staticmethod
    @typing.overload
    def Lambda(body: System.Linq.Expressions.Expression, tailCall: bool, parameters: System.Array[System.Linq.Expressions.ParameterExpression], ) -> System.Linq.Expressions.LambdaExpression:
        ...

    @staticmethod
    @typing.overload
    def Lambda(body: System.Linq.Expressions.Expression, parameters: System.Collections.Generic.IEnumerable[System.Linq.Expressions.ParameterExpression], ) -> System.Linq.Expressions.LambdaExpression:
        ...

    @staticmethod
    @typing.overload
    def Lambda(body: System.Linq.Expressions.Expression, tailCall: bool, parameters: System.Collections.Generic.IEnumerable[System.Linq.Expressions.ParameterExpression], ) -> System.Linq.Expressions.LambdaExpression:
        ...

    @staticmethod
    @typing.overload
    def Lambda(delegateType: System.Type, body: System.Linq.Expressions.Expression, parameters: System.Array[System.Linq.Expressions.ParameterExpression], ) -> System.Linq.Expressions.LambdaExpression:
        ...

    @staticmethod
    @typing.overload
    def Lambda(delegateType: System.Type, body: System.Linq.Expressions.Expression, tailCall: bool, parameters: System.Array[System.Linq.Expressions.ParameterExpression], ) -> System.Linq.Expressions.LambdaExpression:
        ...

    @staticmethod
    @typing.overload
    def Lambda(delegateType: System.Type, body: System.Linq.Expressions.Expression, parameters: System.Collections.Generic.IEnumerable[System.Linq.Expressions.ParameterExpression], ) -> System.Linq.Expressions.LambdaExpression:
        ...

    @staticmethod
    @typing.overload
    def Lambda(delegateType: System.Type, body: System.Linq.Expressions.Expression, tailCall: bool, parameters: System.Collections.Generic.IEnumerable[System.Linq.Expressions.ParameterExpression], ) -> System.Linq.Expressions.LambdaExpression:
        ...

    @staticmethod
    @typing.overload
    def Lambda(body: System.Linq.Expressions.Expression, name: str, parameters: System.Collections.Generic.IEnumerable[System.Linq.Expressions.ParameterExpression], ) -> System.Linq.Expressions.LambdaExpression:
        ...

    @staticmethod
    @typing.overload
    def Lambda(body: System.Linq.Expressions.Expression, name: str, tailCall: bool, parameters: System.Collections.Generic.IEnumerable[System.Linq.Expressions.ParameterExpression], ) -> System.Linq.Expressions.LambdaExpression:
        ...

    @staticmethod
    @typing.overload
    def Lambda(delegateType: System.Type, body: System.Linq.Expressions.Expression, name: str, parameters: System.Collections.Generic.IEnumerable[System.Linq.Expressions.ParameterExpression], ) -> System.Linq.Expressions.LambdaExpression:
        ...

    @staticmethod
    @typing.overload
    def Lambda(delegateType: System.Type, body: System.Linq.Expressions.Expression, name: str, tailCall: bool, parameters: System.Collections.Generic.IEnumerable[System.Linq.Expressions.ParameterExpression], ) -> System.Linq.Expressions.LambdaExpression:
        ...

    @staticmethod
    def ValidateLambdaArgs(delegateType: System.Type, body: ref[System.Linq.Expressions.Expression], parameters: System.Collections.ObjectModel.ReadOnlyCollection[System.Linq.Expressions.ParameterExpression], paramName: str, ) -> None:
        ...

    @staticmethod
    def ValidateTryGetFuncActionArgs(typeArgs: System.Array[System.Type], ) -> int:
        ...

    @staticmethod
    def GetFuncType(typeArgs: System.Array[System.Type], ) -> System.Type:
        ...

    @staticmethod
    def TryGetFuncType(typeArgs: System.Array[System.Type], funcType: ref[System.Type], ) -> bool:
        ...

    @staticmethod
    def GetActionType(typeArgs: System.Array[System.Type], ) -> System.Type:
        ...

    @staticmethod
    def TryGetActionType(typeArgs: System.Array[System.Type], actionType: ref[System.Type], ) -> bool:
        ...

    @staticmethod
    def GetDelegateType(typeArgs: System.Array[System.Type], ) -> System.Type:
        ...

    @staticmethod
    def GetResultTypeOfShift(left: System.Type, right: System.Type, ) -> System.Type:
        ...

    @staticmethod
    @typing.overload
    def LeftShift(left: System.Linq.Expressions.Expression, right: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.BinaryExpression:
        ...

    @staticmethod
    @typing.overload
    def LeftShift(left: System.Linq.Expressions.Expression, right: System.Linq.Expressions.Expression, method: System.Reflection.MethodInfo, ) -> System.Linq.Expressions.BinaryExpression:
        ...

    @staticmethod
    @typing.overload
    def LeftShiftAssign(left: System.Linq.Expressions.Expression, right: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.BinaryExpression:
        ...

    @staticmethod
    @typing.overload
    def LeftShiftAssign(left: System.Linq.Expressions.Expression, right: System.Linq.Expressions.Expression, method: System.Reflection.MethodInfo, ) -> System.Linq.Expressions.BinaryExpression:
        ...

    @staticmethod
    @typing.overload
    def LeftShiftAssign(left: System.Linq.Expressions.Expression, right: System.Linq.Expressions.Expression, method: System.Reflection.MethodInfo, conversion: System.Linq.Expressions.LambdaExpression, ) -> System.Linq.Expressions.BinaryExpression:
        ...

    @staticmethod
    @typing.overload
    def RightShift(left: System.Linq.Expressions.Expression, right: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.BinaryExpression:
        ...

    @staticmethod
    @typing.overload
    def RightShift(left: System.Linq.Expressions.Expression, right: System.Linq.Expressions.Expression, method: System.Reflection.MethodInfo, ) -> System.Linq.Expressions.BinaryExpression:
        ...

    @staticmethod
    @typing.overload
    def RightShiftAssign(left: System.Linq.Expressions.Expression, right: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.BinaryExpression:
        ...

    @staticmethod
    @typing.overload
    def RightShiftAssign(left: System.Linq.Expressions.Expression, right: System.Linq.Expressions.Expression, method: System.Reflection.MethodInfo, ) -> System.Linq.Expressions.BinaryExpression:
        ...

    @staticmethod
    @typing.overload
    def RightShiftAssign(left: System.Linq.Expressions.Expression, right: System.Linq.Expressions.Expression, method: System.Reflection.MethodInfo, conversion: System.Linq.Expressions.LambdaExpression, ) -> System.Linq.Expressions.BinaryExpression:
        ...

    @staticmethod
    @typing.overload
    def And(left: System.Linq.Expressions.Expression, right: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.BinaryExpression:
        ...

    @staticmethod
    @typing.overload
    def And(left: System.Linq.Expressions.Expression, right: System.Linq.Expressions.Expression, method: System.Reflection.MethodInfo, ) -> System.Linq.Expressions.BinaryExpression:
        ...

    @staticmethod
    @typing.overload
    def AndAssign(left: System.Linq.Expressions.Expression, right: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.BinaryExpression:
        ...

    @staticmethod
    @typing.overload
    def AndAssign(left: System.Linq.Expressions.Expression, right: System.Linq.Expressions.Expression, method: System.Reflection.MethodInfo, ) -> System.Linq.Expressions.BinaryExpression:
        ...

    @staticmethod
    @typing.overload
    def AndAssign(left: System.Linq.Expressions.Expression, right: System.Linq.Expressions.Expression, method: System.Reflection.MethodInfo, conversion: System.Linq.Expressions.LambdaExpression, ) -> System.Linq.Expressions.BinaryExpression:
        ...

    @staticmethod
    @typing.overload
    def Or(left: System.Linq.Expressions.Expression, right: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.BinaryExpression:
        ...

    @staticmethod
    @typing.overload
    def Or(left: System.Linq.Expressions.Expression, right: System.Linq.Expressions.Expression, method: System.Reflection.MethodInfo, ) -> System.Linq.Expressions.BinaryExpression:
        ...

    @staticmethod
    @typing.overload
    def OrAssign(left: System.Linq.Expressions.Expression, right: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.BinaryExpression:
        ...

    @staticmethod
    @typing.overload
    def OrAssign(left: System.Linq.Expressions.Expression, right: System.Linq.Expressions.Expression, method: System.Reflection.MethodInfo, ) -> System.Linq.Expressions.BinaryExpression:
        ...

    @staticmethod
    @typing.overload
    def OrAssign(left: System.Linq.Expressions.Expression, right: System.Linq.Expressions.Expression, method: System.Reflection.MethodInfo, conversion: System.Linq.Expressions.LambdaExpression, ) -> System.Linq.Expressions.BinaryExpression:
        ...

    @staticmethod
    @typing.overload
    def ExclusiveOr(left: System.Linq.Expressions.Expression, right: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.BinaryExpression:
        ...

    @staticmethod
    @typing.overload
    def ExclusiveOr(left: System.Linq.Expressions.Expression, right: System.Linq.Expressions.Expression, method: System.Reflection.MethodInfo, ) -> System.Linq.Expressions.BinaryExpression:
        ...

    @staticmethod
    @typing.overload
    def ExclusiveOrAssign(left: System.Linq.Expressions.Expression, right: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.BinaryExpression:
        ...

    @staticmethod
    @typing.overload
    def ExclusiveOrAssign(left: System.Linq.Expressions.Expression, right: System.Linq.Expressions.Expression, method: System.Reflection.MethodInfo, ) -> System.Linq.Expressions.BinaryExpression:
        ...

    @staticmethod
    @typing.overload
    def ExclusiveOrAssign(left: System.Linq.Expressions.Expression, right: System.Linq.Expressions.Expression, method: System.Reflection.MethodInfo, conversion: System.Linq.Expressions.LambdaExpression, ) -> System.Linq.Expressions.BinaryExpression:
        ...

    @staticmethod
    @typing.overload
    def Power(left: System.Linq.Expressions.Expression, right: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.BinaryExpression:
        ...

    @staticmethod
    @typing.overload
    def Power(left: System.Linq.Expressions.Expression, right: System.Linq.Expressions.Expression, method: System.Reflection.MethodInfo, ) -> System.Linq.Expressions.BinaryExpression:
        ...

    @staticmethod
    @typing.overload
    def PowerAssign(left: System.Linq.Expressions.Expression, right: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.BinaryExpression:
        ...

    @staticmethod
    @typing.overload
    def PowerAssign(left: System.Linq.Expressions.Expression, right: System.Linq.Expressions.Expression, method: System.Reflection.MethodInfo, ) -> System.Linq.Expressions.BinaryExpression:
        ...

    @staticmethod
    @typing.overload
    def PowerAssign(left: System.Linq.Expressions.Expression, right: System.Linq.Expressions.Expression, method: System.Reflection.MethodInfo, conversion: System.Linq.Expressions.LambdaExpression, ) -> System.Linq.Expressions.BinaryExpression:
        ...

    @staticmethod
    @typing.overload
    def Block(arg0: System.Linq.Expressions.Expression, arg1: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.BlockExpression:
        ...

    @staticmethod
    @typing.overload
    def Block(arg0: System.Linq.Expressions.Expression, arg1: System.Linq.Expressions.Expression, arg2: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.BlockExpression:
        ...

    @staticmethod
    @typing.overload
    def Block(arg0: System.Linq.Expressions.Expression, arg1: System.Linq.Expressions.Expression, arg2: System.Linq.Expressions.Expression, arg3: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.BlockExpression:
        ...

    @staticmethod
    @typing.overload
    def Block(arg0: System.Linq.Expressions.Expression, arg1: System.Linq.Expressions.Expression, arg2: System.Linq.Expressions.Expression, arg3: System.Linq.Expressions.Expression, arg4: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.BlockExpression:
        ...

    @staticmethod
    @typing.overload
    def Block(expressions: System.Array[System.Linq.Expressions.Expression], ) -> System.Linq.Expressions.BlockExpression:
        ...

    @staticmethod
    @typing.overload
    def Block(expressions: System.Collections.Generic.IEnumerable[System.Linq.Expressions.Expression], ) -> System.Linq.Expressions.BlockExpression:
        ...

    @staticmethod
    @typing.overload
    def Block(type: System.Type, expressions: System.Array[System.Linq.Expressions.Expression], ) -> System.Linq.Expressions.BlockExpression:
        ...

    @staticmethod
    @typing.overload
    def Block(type: System.Type, expressions: System.Collections.Generic.IEnumerable[System.Linq.Expressions.Expression], ) -> System.Linq.Expressions.BlockExpression:
        ...

    @staticmethod
    @typing.overload
    def Block(variables: System.Collections.Generic.IEnumerable[System.Linq.Expressions.ParameterExpression], expressions: System.Array[System.Linq.Expressions.Expression], ) -> System.Linq.Expressions.BlockExpression:
        ...

    @staticmethod
    @typing.overload
    def Block(type: System.Type, variables: System.Collections.Generic.IEnumerable[System.Linq.Expressions.ParameterExpression], expressions: System.Array[System.Linq.Expressions.Expression], ) -> System.Linq.Expressions.BlockExpression:
        ...

    @staticmethod
    @typing.overload
    def Block(variables: System.Collections.Generic.IEnumerable[System.Linq.Expressions.ParameterExpression], expressions: System.Collections.Generic.IEnumerable[System.Linq.Expressions.Expression], ) -> System.Linq.Expressions.BlockExpression:
        ...

    @staticmethod
    @typing.overload
    def Block(type: System.Type, variables: System.Collections.Generic.IEnumerable[System.Linq.Expressions.ParameterExpression], expressions: System.Collections.Generic.IEnumerable[System.Linq.Expressions.Expression], ) -> System.Linq.Expressions.BlockExpression:
        ...

    @staticmethod
    def BlockCore(type: System.Type, variables: System.Collections.ObjectModel.ReadOnlyCollection[System.Linq.Expressions.ParameterExpression], expressions: System.Collections.ObjectModel.ReadOnlyCollection[System.Linq.Expressions.Expression], ) -> System.Linq.Expressions.BlockExpression:
        ...

    @staticmethod
    def ValidateVariables(varList: System.Collections.ObjectModel.ReadOnlyCollection[System.Linq.Expressions.ParameterExpression], collectionName: str, ) -> None:
        ...

    @staticmethod
    def GetOptimizedBlockExpression(expressions: System.Collections.Generic.IReadOnlyList[System.Linq.Expressions.Expression], ) -> System.Linq.Expressions.BlockExpression:
        ...

    @staticmethod
    @typing.overload
    def Catch(type: System.Type, body: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.CatchBlock:
        ...

    @staticmethod
    @typing.overload
    def Catch(variable: System.Linq.Expressions.ParameterExpression, body: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.CatchBlock:
        ...

    @staticmethod
    @typing.overload
    def Catch(type: System.Type, body: System.Linq.Expressions.Expression, filter: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.CatchBlock:
        ...

    @staticmethod
    @typing.overload
    def Catch(variable: System.Linq.Expressions.ParameterExpression, body: System.Linq.Expressions.Expression, filter: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.CatchBlock:
        ...

    @staticmethod
    def MakeCatchBlock(type: System.Type, variable: System.Linq.Expressions.ParameterExpression, body: System.Linq.Expressions.Expression, filter: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.CatchBlock:
        ...

    @staticmethod
    @typing.overload
    def Condition(test: System.Linq.Expressions.Expression, ifTrue: System.Linq.Expressions.Expression, ifFalse: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.ConditionalExpression:
        ...

    @staticmethod
    @typing.overload
    def Condition(test: System.Linq.Expressions.Expression, ifTrue: System.Linq.Expressions.Expression, ifFalse: System.Linq.Expressions.Expression, type: System.Type, ) -> System.Linq.Expressions.ConditionalExpression:
        ...

    @staticmethod
    def IfThen(test: System.Linq.Expressions.Expression, ifTrue: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.ConditionalExpression:
        ...

    @staticmethod
    def IfThenElse(test: System.Linq.Expressions.Expression, ifTrue: System.Linq.Expressions.Expression, ifFalse: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.ConditionalExpression:
        ...

    @staticmethod
    @typing.overload
    def Constant(value: System.Object, ) -> System.Linq.Expressions.ConstantExpression:
        ...

    @staticmethod
    @typing.overload
    def Constant(value: System.Object, type: System.Type, ) -> System.Linq.Expressions.ConstantExpression:
        ...

    @staticmethod
    def DebugInfo(document: System.Linq.Expressions.SymbolDocumentInfo, startLine: int, startColumn: int, endLine: int, endColumn: int, ) -> System.Linq.Expressions.DebugInfoExpression:
        ...

    @staticmethod
    def ClearDebugInfo(document: System.Linq.Expressions.SymbolDocumentInfo, ) -> System.Linq.Expressions.DebugInfoExpression:
        ...

    @staticmethod
    def ValidateSpan(startLine: int, startColumn: int, endLine: int, endColumn: int, ) -> None:
        ...

    @staticmethod
    def Empty() -> System.Linq.Expressions.DefaultExpression:
        ...

    @staticmethod
    def Default(type: System.Type, ) -> System.Linq.Expressions.DefaultExpression:
        ...

    @staticmethod
    @typing.overload
    def ElementInit(addMethod: System.Reflection.MethodInfo, arguments: System.Array[System.Linq.Expressions.Expression], ) -> System.Linq.Expressions.ElementInit:
        ...

    @staticmethod
    @typing.overload
    def ElementInit(addMethod: System.Reflection.MethodInfo, arguments: System.Collections.Generic.IEnumerable[System.Linq.Expressions.Expression], ) -> System.Linq.Expressions.ElementInit:
        ...

    @staticmethod
    def ValidateElementInitAddMethodInfo(addMethod: System.Reflection.MethodInfo, paramName: str, ) -> None:
        ...

    def ReduceAndCheck(self, ) -> System.Linq.Expressions.Expression:
        ...

    def ReduceExtensions(self, ) -> System.Linq.Expressions.Expression:
        ...

    @staticmethod
    def RequiresCanRead(items: System.Collections.Generic.IReadOnlyList[System.Linq.Expressions.Expression], paramName: str, ) -> None:
        ...

    @staticmethod
    def RequiresCanWrite(expression: System.Linq.Expressions.Expression, paramName: str, ) -> None:
        ...

    @staticmethod
    @typing.overload
    def Dynamic(binder: System.Runtime.CompilerServices.CallSiteBinder, returnType: System.Type, arguments: System.Collections.Generic.IEnumerable[System.Linq.Expressions.Expression], ) -> System.Linq.Expressions.DynamicExpression:
        ...

    @staticmethod
    @typing.overload
    def Dynamic(binder: System.Runtime.CompilerServices.CallSiteBinder, returnType: System.Type, arg0: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.DynamicExpression:
        ...

    @staticmethod
    @typing.overload
    def Dynamic(binder: System.Runtime.CompilerServices.CallSiteBinder, returnType: System.Type, arg0: System.Linq.Expressions.Expression, arg1: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.DynamicExpression:
        ...

    @staticmethod
    @typing.overload
    def Dynamic(binder: System.Runtime.CompilerServices.CallSiteBinder, returnType: System.Type, arg0: System.Linq.Expressions.Expression, arg1: System.Linq.Expressions.Expression, arg2: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.DynamicExpression:
        ...

    @staticmethod
    @typing.overload
    def Dynamic(binder: System.Runtime.CompilerServices.CallSiteBinder, returnType: System.Type, arg0: System.Linq.Expressions.Expression, arg1: System.Linq.Expressions.Expression, arg2: System.Linq.Expressions.Expression, arg3: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.DynamicExpression:
        ...

    @staticmethod
    @typing.overload
    def Dynamic(binder: System.Runtime.CompilerServices.CallSiteBinder, returnType: System.Type, arguments: System.Array[System.Linq.Expressions.Expression], ) -> System.Linq.Expressions.DynamicExpression:
        ...

    @staticmethod
    def Assign(left: System.Linq.Expressions.Expression, right: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.BinaryExpression:
        ...

    @staticmethod
    @typing.overload
    def GetUserDefinedBinaryOperator(binaryType: int, name: str, left: System.Linq.Expressions.Expression, right: System.Linq.Expressions.Expression, liftToNull: bool, ) -> System.Linq.Expressions.BinaryExpression:
        ...

    @staticmethod
    @typing.overload
    def GetUserDefinedBinaryOperator(binaryType: int, leftType: System.Type, rightType: System.Type, name: str, ) -> System.Reflection.MethodInfo:
        ...

    @staticmethod
    def GetMethodBasedBinaryOperator(binaryType: int, left: System.Linq.Expressions.Expression, right: System.Linq.Expressions.Expression, method: System.Reflection.MethodInfo, liftToNull: bool, ) -> System.Linq.Expressions.BinaryExpression:
        ...

    @staticmethod
    def GetMethodBasedAssignOperator(binaryType: int, left: System.Linq.Expressions.Expression, right: System.Linq.Expressions.Expression, method: System.Reflection.MethodInfo, conversion: System.Linq.Expressions.LambdaExpression, liftToNull: bool, ) -> System.Linq.Expressions.BinaryExpression:
        ...

    @staticmethod
    def GetUserDefinedBinaryOperatorOrThrow(binaryType: int, name: str, left: System.Linq.Expressions.Expression, right: System.Linq.Expressions.Expression, liftToNull: bool, ) -> System.Linq.Expressions.BinaryExpression:
        ...

    @staticmethod
    def GetUserDefinedAssignOperatorOrThrow(binaryType: int, name: str, left: System.Linq.Expressions.Expression, right: System.Linq.Expressions.Expression, conversion: System.Linq.Expressions.LambdaExpression, liftToNull: bool, ) -> System.Linq.Expressions.BinaryExpression:
        ...

    @staticmethod
    def IsLiftingConditionalLogicalOperator(left: System.Type, right: System.Type, method: System.Reflection.MethodInfo, binaryType: int, ) -> bool:
        ...

    @staticmethod
    def ParameterIsAssignable(pi: System.Reflection.ParameterInfo, argType: System.Type, ) -> bool:
        ...

    @staticmethod
    def ValidateParamswithOperandsOrThrow(paramType: System.Type, operandType: System.Type, exprType: int, name: str, ) -> None:
        ...

    @staticmethod
    def ValidateOperator(method: System.Reflection.MethodInfo, ) -> None:
        ...

    @staticmethod
    def ValidateMethodInfo(method: System.Reflection.MethodInfo, paramName: str, ) -> None:
        ...

    @staticmethod
    def IsNullComparison(left: System.Linq.Expressions.Expression, right: System.Linq.Expressions.Expression, ) -> bool:
        ...

    @staticmethod
    def IsNullConstant(e: System.Linq.Expressions.Expression, ) -> bool:
        ...

    @staticmethod
    def ValidateUserDefinedConditionalLogicOperator(nodeType: int, left: System.Type, right: System.Type, method: System.Reflection.MethodInfo, ) -> None:
        ...

    @staticmethod
    def VerifyOpTrueFalse(nodeType: int, left: System.Type, opTrue: System.Reflection.MethodInfo, paramName: str, ) -> None:
        ...

    @staticmethod
    def IsValidLiftedConditionalLogicalOperator(left: System.Type, right: System.Type, pms: System.Array[System.Reflection.ParameterInfo], ) -> bool:
        ...

    @staticmethod
    @typing.overload
    def MakeBinary(binaryType: int, left: System.Linq.Expressions.Expression, right: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.BinaryExpression:
        ...

    @staticmethod
    @typing.overload
    def MakeBinary(binaryType: int, left: System.Linq.Expressions.Expression, right: System.Linq.Expressions.Expression, liftToNull: bool, method: System.Reflection.MethodInfo, ) -> System.Linq.Expressions.BinaryExpression:
        ...

    @staticmethod
    @typing.overload
    def MakeBinary(binaryType: int, left: System.Linq.Expressions.Expression, right: System.Linq.Expressions.Expression, liftToNull: bool, method: System.Reflection.MethodInfo, conversion: System.Linq.Expressions.LambdaExpression, ) -> System.Linq.Expressions.BinaryExpression:
        ...

    @staticmethod
    @typing.overload
    def Equal(left: System.Linq.Expressions.Expression, right: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.BinaryExpression:
        ...

    @staticmethod
    @typing.overload
    def Equal(left: System.Linq.Expressions.Expression, right: System.Linq.Expressions.Expression, liftToNull: bool, method: System.Reflection.MethodInfo, ) -> System.Linq.Expressions.BinaryExpression:
        ...

    @staticmethod
    def ReferenceEqual(left: System.Linq.Expressions.Expression, right: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.BinaryExpression:
        ...

    @staticmethod
    @typing.overload
    def NotEqual(left: System.Linq.Expressions.Expression, right: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.BinaryExpression:
        ...

    @staticmethod
    @typing.overload
    def NotEqual(left: System.Linq.Expressions.Expression, right: System.Linq.Expressions.Expression, liftToNull: bool, method: System.Reflection.MethodInfo, ) -> System.Linq.Expressions.BinaryExpression:
        ...

    @staticmethod
    def ReferenceNotEqual(left: System.Linq.Expressions.Expression, right: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.BinaryExpression:
        ...

    @staticmethod
    def GetEqualityComparisonOperator(binaryType: int, opName: str, left: System.Linq.Expressions.Expression, right: System.Linq.Expressions.Expression, liftToNull: bool, ) -> System.Linq.Expressions.BinaryExpression:
        ...

    @staticmethod
    @typing.overload
    def GreaterThan(left: System.Linq.Expressions.Expression, right: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.BinaryExpression:
        ...

    @staticmethod
    @typing.overload
    def GreaterThan(left: System.Linq.Expressions.Expression, right: System.Linq.Expressions.Expression, liftToNull: bool, method: System.Reflection.MethodInfo, ) -> System.Linq.Expressions.BinaryExpression:
        ...

    @staticmethod
    @typing.overload
    def LessThan(left: System.Linq.Expressions.Expression, right: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.BinaryExpression:
        ...

    @staticmethod
    @typing.overload
    def LessThan(left: System.Linq.Expressions.Expression, right: System.Linq.Expressions.Expression, liftToNull: bool, method: System.Reflection.MethodInfo, ) -> System.Linq.Expressions.BinaryExpression:
        ...

    @staticmethod
    @typing.overload
    def GreaterThanOrEqual(left: System.Linq.Expressions.Expression, right: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.BinaryExpression:
        ...

    @staticmethod
    @typing.overload
    def GreaterThanOrEqual(left: System.Linq.Expressions.Expression, right: System.Linq.Expressions.Expression, liftToNull: bool, method: System.Reflection.MethodInfo, ) -> System.Linq.Expressions.BinaryExpression:
        ...

    @staticmethod
    @typing.overload
    def LessThanOrEqual(left: System.Linq.Expressions.Expression, right: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.BinaryExpression:
        ...

    @staticmethod
    @typing.overload
    def LessThanOrEqual(left: System.Linq.Expressions.Expression, right: System.Linq.Expressions.Expression, liftToNull: bool, method: System.Reflection.MethodInfo, ) -> System.Linq.Expressions.BinaryExpression:
        ...

    @staticmethod
    def GetComparisonOperator(binaryType: int, opName: str, left: System.Linq.Expressions.Expression, right: System.Linq.Expressions.Expression, liftToNull: bool, ) -> System.Linq.Expressions.BinaryExpression:
        ...

    @staticmethod
    @typing.overload
    def AndAlso(left: System.Linq.Expressions.Expression, right: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.BinaryExpression:
        ...

    @staticmethod
    @typing.overload
    def AndAlso(left: System.Linq.Expressions.Expression, right: System.Linq.Expressions.Expression, method: System.Reflection.MethodInfo, ) -> System.Linq.Expressions.BinaryExpression:
        ...

    @staticmethod
    @typing.overload
    def OrElse(left: System.Linq.Expressions.Expression, right: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.BinaryExpression:
        ...

    @staticmethod
    @typing.overload
    def OrElse(left: System.Linq.Expressions.Expression, right: System.Linq.Expressions.Expression, method: System.Reflection.MethodInfo, ) -> System.Linq.Expressions.BinaryExpression:
        ...

    @staticmethod
    @typing.overload
    def Coalesce(left: System.Linq.Expressions.Expression, right: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.BinaryExpression:
        ...

    @staticmethod
    @typing.overload
    def Coalesce(left: System.Linq.Expressions.Expression, right: System.Linq.Expressions.Expression, conversion: System.Linq.Expressions.LambdaExpression, ) -> System.Linq.Expressions.BinaryExpression:
        ...

    @staticmethod
    def ValidateCoalesceArgTypes(left: System.Type, right: System.Type, ) -> System.Type:
        ...

    @staticmethod
    @typing.overload
    def Add(left: System.Linq.Expressions.Expression, right: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.BinaryExpression:
        ...

    @staticmethod
    @typing.overload
    def Add(left: System.Linq.Expressions.Expression, right: System.Linq.Expressions.Expression, method: System.Reflection.MethodInfo, ) -> System.Linq.Expressions.BinaryExpression:
        ...

    @staticmethod
    @typing.overload
    def AddAssign(left: System.Linq.Expressions.Expression, right: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.BinaryExpression:
        ...

    @staticmethod
    @typing.overload
    def AddAssign(left: System.Linq.Expressions.Expression, right: System.Linq.Expressions.Expression, method: System.Reflection.MethodInfo, ) -> System.Linq.Expressions.BinaryExpression:
        ...

    @staticmethod
    @typing.overload
    def AddAssign(left: System.Linq.Expressions.Expression, right: System.Linq.Expressions.Expression, method: System.Reflection.MethodInfo, conversion: System.Linq.Expressions.LambdaExpression, ) -> System.Linq.Expressions.BinaryExpression:
        ...

    @staticmethod
    def ValidateOpAssignConversionLambda(conversion: System.Linq.Expressions.LambdaExpression, left: System.Linq.Expressions.Expression, method: System.Reflection.MethodInfo, nodeType: int, ) -> None:
        ...

    @staticmethod
    @typing.overload
    def AddAssignChecked(left: System.Linq.Expressions.Expression, right: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.BinaryExpression:
        ...

    @staticmethod
    @typing.overload
    def AddAssignChecked(left: System.Linq.Expressions.Expression, right: System.Linq.Expressions.Expression, method: System.Reflection.MethodInfo, ) -> System.Linq.Expressions.BinaryExpression:
        ...

    @staticmethod
    @typing.overload
    def AddAssignChecked(left: System.Linq.Expressions.Expression, right: System.Linq.Expressions.Expression, method: System.Reflection.MethodInfo, conversion: System.Linq.Expressions.LambdaExpression, ) -> System.Linq.Expressions.BinaryExpression:
        ...

    @staticmethod
    @typing.overload
    def AddChecked(left: System.Linq.Expressions.Expression, right: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.BinaryExpression:
        ...

    @staticmethod
    @typing.overload
    def AddChecked(left: System.Linq.Expressions.Expression, right: System.Linq.Expressions.Expression, method: System.Reflection.MethodInfo, ) -> System.Linq.Expressions.BinaryExpression:
        ...

    @staticmethod
    @typing.overload
    def Subtract(left: System.Linq.Expressions.Expression, right: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.BinaryExpression:
        ...

    @staticmethod
    @typing.overload
    def Subtract(left: System.Linq.Expressions.Expression, right: System.Linq.Expressions.Expression, method: System.Reflection.MethodInfo, ) -> System.Linq.Expressions.BinaryExpression:
        ...

    @staticmethod
    @typing.overload
    def SubtractAssign(left: System.Linq.Expressions.Expression, right: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.BinaryExpression:
        ...

    @staticmethod
    @typing.overload
    def SubtractAssign(left: System.Linq.Expressions.Expression, right: System.Linq.Expressions.Expression, method: System.Reflection.MethodInfo, ) -> System.Linq.Expressions.BinaryExpression:
        ...

    @staticmethod
    @typing.overload
    def SubtractAssign(left: System.Linq.Expressions.Expression, right: System.Linq.Expressions.Expression, method: System.Reflection.MethodInfo, conversion: System.Linq.Expressions.LambdaExpression, ) -> System.Linq.Expressions.BinaryExpression:
        ...

    @staticmethod
    @typing.overload
    def SubtractAssignChecked(left: System.Linq.Expressions.Expression, right: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.BinaryExpression:
        ...

    @staticmethod
    @typing.overload
    def SubtractAssignChecked(left: System.Linq.Expressions.Expression, right: System.Linq.Expressions.Expression, method: System.Reflection.MethodInfo, ) -> System.Linq.Expressions.BinaryExpression:
        ...

    @staticmethod
    @typing.overload
    def SubtractAssignChecked(left: System.Linq.Expressions.Expression, right: System.Linq.Expressions.Expression, method: System.Reflection.MethodInfo, conversion: System.Linq.Expressions.LambdaExpression, ) -> System.Linq.Expressions.BinaryExpression:
        ...

    @staticmethod
    @typing.overload
    def SubtractChecked(left: System.Linq.Expressions.Expression, right: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.BinaryExpression:
        ...

    @staticmethod
    @typing.overload
    def SubtractChecked(left: System.Linq.Expressions.Expression, right: System.Linq.Expressions.Expression, method: System.Reflection.MethodInfo, ) -> System.Linq.Expressions.BinaryExpression:
        ...

    @staticmethod
    @typing.overload
    def Divide(left: System.Linq.Expressions.Expression, right: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.BinaryExpression:
        ...

    @staticmethod
    @typing.overload
    def Divide(left: System.Linq.Expressions.Expression, right: System.Linq.Expressions.Expression, method: System.Reflection.MethodInfo, ) -> System.Linq.Expressions.BinaryExpression:
        ...

    @staticmethod
    @typing.overload
    def DivideAssign(left: System.Linq.Expressions.Expression, right: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.BinaryExpression:
        ...

    @staticmethod
    @typing.overload
    def DivideAssign(left: System.Linq.Expressions.Expression, right: System.Linq.Expressions.Expression, method: System.Reflection.MethodInfo, ) -> System.Linq.Expressions.BinaryExpression:
        ...

    @staticmethod
    @typing.overload
    def DivideAssign(left: System.Linq.Expressions.Expression, right: System.Linq.Expressions.Expression, method: System.Reflection.MethodInfo, conversion: System.Linq.Expressions.LambdaExpression, ) -> System.Linq.Expressions.BinaryExpression:
        ...

    @staticmethod
    @typing.overload
    def Modulo(left: System.Linq.Expressions.Expression, right: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.BinaryExpression:
        ...

    @staticmethod
    @typing.overload
    def Modulo(left: System.Linq.Expressions.Expression, right: System.Linq.Expressions.Expression, method: System.Reflection.MethodInfo, ) -> System.Linq.Expressions.BinaryExpression:
        ...

    @staticmethod
    @typing.overload
    def ModuloAssign(left: System.Linq.Expressions.Expression, right: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.BinaryExpression:
        ...

    @staticmethod
    @typing.overload
    def ModuloAssign(left: System.Linq.Expressions.Expression, right: System.Linq.Expressions.Expression, method: System.Reflection.MethodInfo, ) -> System.Linq.Expressions.BinaryExpression:
        ...

    @staticmethod
    @typing.overload
    def ModuloAssign(left: System.Linq.Expressions.Expression, right: System.Linq.Expressions.Expression, method: System.Reflection.MethodInfo, conversion: System.Linq.Expressions.LambdaExpression, ) -> System.Linq.Expressions.BinaryExpression:
        ...

    @staticmethod
    @typing.overload
    def Multiply(left: System.Linq.Expressions.Expression, right: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.BinaryExpression:
        ...

    @staticmethod
    @typing.overload
    def Multiply(left: System.Linq.Expressions.Expression, right: System.Linq.Expressions.Expression, method: System.Reflection.MethodInfo, ) -> System.Linq.Expressions.BinaryExpression:
        ...

    @staticmethod
    @typing.overload
    def MultiplyAssign(left: System.Linq.Expressions.Expression, right: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.BinaryExpression:
        ...

    @staticmethod
    @typing.overload
    def MultiplyAssign(left: System.Linq.Expressions.Expression, right: System.Linq.Expressions.Expression, method: System.Reflection.MethodInfo, ) -> System.Linq.Expressions.BinaryExpression:
        ...

    @staticmethod
    @typing.overload
    def MultiplyAssign(left: System.Linq.Expressions.Expression, right: System.Linq.Expressions.Expression, method: System.Reflection.MethodInfo, conversion: System.Linq.Expressions.LambdaExpression, ) -> System.Linq.Expressions.BinaryExpression:
        ...

    @staticmethod
    @typing.overload
    def MultiplyAssignChecked(left: System.Linq.Expressions.Expression, right: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.BinaryExpression:
        ...

    @staticmethod
    @typing.overload
    def MultiplyAssignChecked(left: System.Linq.Expressions.Expression, right: System.Linq.Expressions.Expression, method: System.Reflection.MethodInfo, ) -> System.Linq.Expressions.BinaryExpression:
        ...

    @staticmethod
    @typing.overload
    def MultiplyAssignChecked(left: System.Linq.Expressions.Expression, right: System.Linq.Expressions.Expression, method: System.Reflection.MethodInfo, conversion: System.Linq.Expressions.LambdaExpression, ) -> System.Linq.Expressions.BinaryExpression:
        ...

    @staticmethod
    @typing.overload
    def MultiplyChecked(left: System.Linq.Expressions.Expression, right: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.BinaryExpression:
        ...

    @staticmethod
    @typing.overload
    def MultiplyChecked(left: System.Linq.Expressions.Expression, right: System.Linq.Expressions.Expression, method: System.Reflection.MethodInfo, ) -> System.Linq.Expressions.BinaryExpression:
        ...

    @staticmethod
    def IsSimpleShift(left: System.Type, right: System.Type, ) -> bool:
        ...

class MemberBinding(System.Object, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def BindingType(self) -> int:
        ...

    @property
    def Member(self) -> System.Reflection.MemberInfo:
        ...

    # methods
    def __init__(self, type: int, member: System.Reflection.MemberInfo, ):
        ...

    def ToString(self, ) -> str:
        ...

    def ValidateAsDefinedHere(self, index: int, ) -> None:
        ...

class NewArrayExpression(System.Linq.Expressions.Expression):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def Type(self) -> System.Type:
        ...

    @property
    def Expressions(self) -> System.Collections.ObjectModel.ReadOnlyCollection[System.Linq.Expressions.Expression]:
        ...

    @property
    def NodeType(self) -> int:
        ...

    @property
    def CanReduce(self) -> bool:
        ...

    # methods
    def __init__(self, type: System.Type, expressions: System.Collections.ObjectModel.ReadOnlyCollection[System.Linq.Expressions.Expression], ):
        ...

    @staticmethod
    def Make(nodeType: int, type: System.Type, expressions: System.Collections.ObjectModel.ReadOnlyCollection[System.Linq.Expressions.Expression], ) -> System.Linq.Expressions.NewArrayExpression:
        ...

    def Accept(self, visitor: System.Linq.Expressions.ExpressionVisitor, ) -> System.Linq.Expressions.Expression:
        ...

    def Update(self, expressions: System.Collections.Generic.IEnumerable[System.Linq.Expressions.Expression], ) -> System.Linq.Expressions.NewArrayExpression:
        ...

class SwitchExpression(System.Linq.Expressions.Expression):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def Type(self) -> System.Type:
        ...

    @property
    def NodeType(self) -> int:
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
    def IsLifted(self) -> bool:
        ...

    @property
    def CanReduce(self) -> bool:
        ...

    # methods
    def __init__(self, type: System.Type, switchValue: System.Linq.Expressions.Expression, defaultBody: System.Linq.Expressions.Expression, comparison: System.Reflection.MethodInfo, cases: System.Collections.ObjectModel.ReadOnlyCollection[System.Linq.Expressions.SwitchCase], ):
        ...

    def Accept(self, visitor: System.Linq.Expressions.ExpressionVisitor, ) -> System.Linq.Expressions.Expression:
        ...

    def Update(self, switchValue: System.Linq.Expressions.Expression, cases: System.Collections.Generic.IEnumerable[System.Linq.Expressions.SwitchCase], defaultBody: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.SwitchExpression:
        ...

class SwitchCase(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def TestValues(self) -> System.Collections.ObjectModel.ReadOnlyCollection[System.Linq.Expressions.Expression]:
        ...

    @property
    def Body(self) -> System.Linq.Expressions.Expression:
        ...

    # methods
    def __init__(self, body: System.Linq.Expressions.Expression, testValues: System.Collections.ObjectModel.ReadOnlyCollection[System.Linq.Expressions.Expression], ):
        ...

    def ToString(self, ) -> str:
        ...

    def Update(self, testValues: System.Collections.Generic.IEnumerable[System.Linq.Expressions.Expression], body: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.SwitchCase:
        ...

class MemberInitExpression(System.Linq.Expressions.Expression):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def Type(self) -> System.Type:
        ...

    @property
    def CanReduce(self) -> bool:
        ...

    @property
    def NodeType(self) -> int:
        ...

    @property
    def NewExpression(self) -> System.Linq.Expressions.NewExpression:
        ...

    @property
    def Bindings(self) -> System.Collections.ObjectModel.ReadOnlyCollection[System.Linq.Expressions.MemberBinding]:
        ...

    # methods
    def __init__(self, newExpression: System.Linq.Expressions.NewExpression, bindings: System.Collections.ObjectModel.ReadOnlyCollection[System.Linq.Expressions.MemberBinding], ):
        ...

    def Accept(self, visitor: System.Linq.Expressions.ExpressionVisitor, ) -> System.Linq.Expressions.Expression:
        ...

    def Reduce(self, ) -> System.Linq.Expressions.Expression:
        ...

    @staticmethod
    def ReduceMemberInit(objExpression: System.Linq.Expressions.Expression, bindings: System.Collections.ObjectModel.ReadOnlyCollection[System.Linq.Expressions.MemberBinding], keepOnStack: bool, ) -> System.Linq.Expressions.Expression:
        ...

    @staticmethod
    def ReduceListInit(listExpression: System.Linq.Expressions.Expression, initializers: System.Collections.ObjectModel.ReadOnlyCollection[System.Linq.Expressions.ElementInit], keepOnStack: bool, ) -> System.Linq.Expressions.Expression:
        ...

    @staticmethod
    def ReduceMemberBinding(objVar: System.Linq.Expressions.ParameterExpression, binding: System.Linq.Expressions.MemberBinding, ) -> System.Linq.Expressions.Expression:
        ...

    def Update(self, newExpression: System.Linq.Expressions.NewExpression, bindings: System.Collections.Generic.IEnumerable[System.Linq.Expressions.MemberBinding], ) -> System.Linq.Expressions.MemberInitExpression:
        ...

class ElementInit(System.Linq.Expressions.IArgumentProvider, System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def AddMethod(self) -> System.Reflection.MethodInfo:
        ...

    @property
    def Arguments(self) -> System.Collections.ObjectModel.ReadOnlyCollection[System.Linq.Expressions.Expression]:
        ...

    @property
    def ArgumentCount(self) -> int:
        ...

    # methods
    def __init__(self, addMethod: System.Reflection.MethodInfo, arguments: System.Collections.ObjectModel.ReadOnlyCollection[System.Linq.Expressions.Expression], ):
        ...

    def GetArgument(self, index: int, ) -> System.Linq.Expressions.Expression:
        ...

    def ToString(self, ) -> str:
        ...

    def Update(self, arguments: System.Collections.Generic.IEnumerable[System.Linq.Expressions.Expression], ) -> System.Linq.Expressions.ElementInit:
        ...

class TypeBinaryExpression(System.Linq.Expressions.Expression):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def Type(self) -> System.Type:
        ...

    @property
    def NodeType(self) -> int:
        ...

    @property
    def Expression(self) -> System.Linq.Expressions.Expression:
        ...

    @property
    def TypeOperand(self) -> System.Type:
        ...

    @property
    def CanReduce(self) -> bool:
        ...

    # methods
    def __init__(self, expression: System.Linq.Expressions.Expression, typeOperand: System.Type, nodeType: int, ):
        ...

    def ReduceTypeEqual(self, ) -> System.Linq.Expressions.Expression:
        ...

    def ByValParameterTypeEqual(self, value: System.Linq.Expressions.ParameterExpression, ) -> System.Linq.Expressions.Expression:
        ...

    def ReduceConstantTypeEqual(self, ) -> System.Linq.Expressions.Expression:
        ...

    def Accept(self, visitor: System.Linq.Expressions.ExpressionVisitor, ) -> System.Linq.Expressions.Expression:
        ...

    def Update(self, expression: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.TypeBinaryExpression:
        ...

class UnaryExpression(System.Linq.Expressions.Expression):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def Type(self) -> System.Type:
        ...

    @property
    def NodeType(self) -> int:
        ...

    @property
    def Operand(self) -> System.Linq.Expressions.Expression:
        ...

    @property
    def Method(self) -> System.Reflection.MethodInfo:
        ...

    @property
    def IsLifted(self) -> bool:
        ...

    @property
    def IsLiftedToNull(self) -> bool:
        ...

    @property
    def CanReduce(self) -> bool:
        ...

    @property
    def IsPrefix(self) -> bool:
        ...

    # methods
    def __init__(self, nodeType: int, expression: System.Linq.Expressions.Expression, type: System.Type, method: System.Reflection.MethodInfo, ):
        ...

    def Accept(self, visitor: System.Linq.Expressions.ExpressionVisitor, ) -> System.Linq.Expressions.Expression:
        ...

    def Reduce(self, ) -> System.Linq.Expressions.Expression:
        ...

    def FunctionalOp(self, operand: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.UnaryExpression:
        ...

    def ReduceVariable(self, ) -> System.Linq.Expressions.Expression:
        ...

    def ReduceMember(self, ) -> System.Linq.Expressions.Expression:
        ...

    def ReduceIndex(self, ) -> System.Linq.Expressions.Expression:
        ...

    def Update(self, operand: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.UnaryExpression:
        ...

class LoopExpression(System.Linq.Expressions.Expression):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def Type(self) -> System.Type:
        ...

    @property
    def NodeType(self) -> int:
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
    def CanReduce(self) -> bool:
        ...

    # methods
    def __init__(self, body: System.Linq.Expressions.Expression, break_: System.Linq.Expressions.LabelTarget, continue_: System.Linq.Expressions.LabelTarget, ):
        ...

    def Accept(self, visitor: System.Linq.Expressions.ExpressionVisitor, ) -> System.Linq.Expressions.Expression:
        ...

    def Update(self, breakLabel: System.Linq.Expressions.LabelTarget, continueLabel: System.Linq.Expressions.LabelTarget, body: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.LoopExpression:
        ...

class TryExpression(System.Linq.Expressions.Expression):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def Type(self) -> System.Type:
        ...

    @property
    def NodeType(self) -> int:
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
    def CanReduce(self) -> bool:
        ...

    # methods
    def __init__(self, type: System.Type, body: System.Linq.Expressions.Expression, finally_: System.Linq.Expressions.Expression, fault: System.Linq.Expressions.Expression, handlers: System.Collections.ObjectModel.ReadOnlyCollection[System.Linq.Expressions.CatchBlock], ):
        ...

    def Accept(self, visitor: System.Linq.Expressions.ExpressionVisitor, ) -> System.Linq.Expressions.Expression:
        ...

    def Update(self, body: System.Linq.Expressions.Expression, handlers: System.Collections.Generic.IEnumerable[System.Linq.Expressions.CatchBlock], finally_: System.Linq.Expressions.Expression, fault: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.TryExpression:
        ...

class MemberListBinding(System.Linq.Expressions.MemberBinding):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def Initializers(self) -> System.Collections.ObjectModel.ReadOnlyCollection[System.Linq.Expressions.ElementInit]:
        ...

    @property
    def BindingType(self) -> int:
        ...

    @property
    def Member(self) -> System.Reflection.MemberInfo:
        ...

    # methods
    def __init__(self, member: System.Reflection.MemberInfo, initializers: System.Collections.ObjectModel.ReadOnlyCollection[System.Linq.Expressions.ElementInit], ):
        ...

    def Update(self, initializers: System.Collections.Generic.IEnumerable[System.Linq.Expressions.ElementInit], ) -> System.Linq.Expressions.MemberListBinding:
        ...

    def ValidateAsDefinedHere(self, index: int, ) -> None:
        ...

class ConstantExpression(System.Linq.Expressions.Expression):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def Type(self) -> System.Type:
        ...

    @property
    def NodeType(self) -> int:
        ...

    @property
    def Value(self) -> System.Object:
        ...

    @property
    def CanReduce(self) -> bool:
        ...

    # methods
    def __init__(self, value: System.Object, ):
        ...

    def Accept(self, visitor: System.Linq.Expressions.ExpressionVisitor, ) -> System.Linq.Expressions.Expression:
        ...

class ConditionalExpression(System.Linq.Expressions.Expression):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def NodeType(self) -> int:
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
    def CanReduce(self) -> bool:
        ...

    # methods
    def __init__(self, test: System.Linq.Expressions.Expression, ifTrue: System.Linq.Expressions.Expression, ):
        ...

    @staticmethod
    def Make(test: System.Linq.Expressions.Expression, ifTrue: System.Linq.Expressions.Expression, ifFalse: System.Linq.Expressions.Expression, type: System.Type, ) -> System.Linq.Expressions.ConditionalExpression:
        ...

    def GetFalse(self, ) -> System.Linq.Expressions.Expression:
        ...

    def Accept(self, visitor: System.Linq.Expressions.ExpressionVisitor, ) -> System.Linq.Expressions.Expression:
        ...

    def Update(self, test: System.Linq.Expressions.Expression, ifTrue: System.Linq.Expressions.Expression, ifFalse: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.ConditionalExpression:
        ...

class DebugInfoExpression(System.Linq.Expressions.Expression):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def Type(self) -> System.Type:
        ...

    @property
    def NodeType(self) -> int:
        ...

    @property
    def StartLine(self) -> int:
        ...

    @property
    def StartColumn(self) -> int:
        ...

    @property
    def EndLine(self) -> int:
        ...

    @property
    def EndColumn(self) -> int:
        ...

    @property
    def Document(self) -> System.Linq.Expressions.SymbolDocumentInfo:
        ...

    @property
    def IsClear(self) -> bool:
        ...

    @property
    def CanReduce(self) -> bool:
        ...

    # methods
    def __init__(self, document: System.Linq.Expressions.SymbolDocumentInfo, ):
        ...

    def Accept(self, visitor: System.Linq.Expressions.ExpressionVisitor, ) -> System.Linq.Expressions.Expression:
        ...

class GotoExpression(System.Linq.Expressions.Expression):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def Type(self) -> System.Type:
        ...

    @property
    def NodeType(self) -> int:
        ...

    @property
    def Value(self) -> System.Linq.Expressions.Expression:
        ...

    @property
    def Target(self) -> System.Linq.Expressions.LabelTarget:
        ...

    @property
    def Kind(self) -> int:
        ...

    @property
    def CanReduce(self) -> bool:
        ...

    # methods
    def __init__(self, kind: int, target: System.Linq.Expressions.LabelTarget, value: System.Linq.Expressions.Expression, type: System.Type, ):
        ...

    def Accept(self, visitor: System.Linq.Expressions.ExpressionVisitor, ) -> System.Linq.Expressions.Expression:
        ...

    def Update(self, target: System.Linq.Expressions.LabelTarget, value: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.GotoExpression:
        ...

class IArgumentProvider(abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    @abc.abstractmethod
    def ArgumentCount(self) -> int:
        ...

    # methods
    @abc.abstractmethod
    def GetArgument(self, index: int, ) -> System.Linq.Expressions.Expression:
        ...

class Expression(System.Linq.Expressions.IParameterProvider, System.Linq.Expressions.LambdaExpression, typing.Generic[TDelegate]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def TypeCore(self) -> System.Type:
        ...

    @property
    def PublicType(self) -> System.Type:
        ...

    @property
    def Type(self) -> System.Type:
        ...

    @property
    def NodeType(self) -> int:
        ...

    @property
    def Parameters(self) -> System.Collections.ObjectModel.ReadOnlyCollection[System.Linq.Expressions.ParameterExpression]:
        ...

    @property
    def Name(self) -> str:
        ...

    @property
    def NameCore(self) -> str:
        ...

    @property
    def Body(self) -> System.Linq.Expressions.Expression:
        ...

    @property
    def ReturnType(self) -> System.Type:
        ...

    @property
    def TailCall(self) -> bool:
        ...

    @property
    def TailCallCore(self) -> bool:
        ...

    @property
    def ParameterCount(self) -> int:
        ...

    @property
    def CanReduce(self) -> bool:
        ...

    # methods
    def __init__(self, body: System.Linq.Expressions.Expression, ):
        ...

    @typing.overload
    def Compile(self, ) -> TDelegate:
        ...

    @typing.overload
    def Compile(self, preferInterpretation: bool, ) -> TDelegate:
        ...

    @typing.overload
    def Compile(self, debugInfoGenerator: System.Runtime.CompilerServices.DebugInfoGenerator, ) -> TDelegate:
        ...

    def Update(self, body: System.Linq.Expressions.Expression, parameters: System.Collections.Generic.IEnumerable[System.Linq.Expressions.ParameterExpression], ) -> System.Linq.Expressions.Expression:
        ...

    def SameParameters(self, parameters: System.Collections.Generic.ICollection[System.Linq.Expressions.ParameterExpression], ) -> bool:
        ...

    def Rewrite(self, body: System.Linq.Expressions.Expression, parameters: System.Array[System.Linq.Expressions.ParameterExpression], ) -> System.Linq.Expressions.Expression:
        ...

    @typing.overload
    def Accept(self, visitor: System.Linq.Expressions.ExpressionVisitor, ) -> System.Linq.Expressions.Expression:
        ...

    @typing.overload
    def Accept(self, spiller: System.Linq.Expressions.Compiler.StackSpiller, ) -> System.Linq.Expressions.LambdaExpression:
        ...

    @staticmethod
    def Create(body: System.Linq.Expressions.Expression, name: str, tailCall: bool, parameters: System.Collections.Generic.IReadOnlyList[System.Linq.Expressions.ParameterExpression], ) -> System.Linq.Expressions.Expression:
        ...

class ParameterExpression(System.Linq.Expressions.Expression):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def Type(self) -> System.Type:
        ...

    @property
    def NodeType(self) -> int:
        ...

    @property
    def Name(self) -> str:
        ...

    @property
    def IsByRef(self) -> bool:
        ...

    @property
    def CanReduce(self) -> bool:
        ...

    # methods
    def __init__(self, name: str, ):
        ...

    @staticmethod
    def Make(type: System.Type, name: str, isByRef: bool, ) -> System.Linq.Expressions.ParameterExpression:
        ...

    def GetIsByRef(self, ) -> bool:
        ...

    def Accept(self, visitor: System.Linq.Expressions.ExpressionVisitor, ) -> System.Linq.Expressions.Expression:
        ...

class MemberExpression(System.Linq.Expressions.Expression):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def Member(self) -> System.Reflection.MemberInfo:
        ...

    @property
    def Expression(self) -> System.Linq.Expressions.Expression:
        ...

    @property
    def NodeType(self) -> int:
        ...

    @property
    def Type(self) -> System.Type:
        ...

    @property
    def CanReduce(self) -> bool:
        ...

    # methods
    def __init__(self, expression: System.Linq.Expressions.Expression, ):
        ...

    @staticmethod
    @typing.overload
    def Make(expression: System.Linq.Expressions.Expression, property: System.Reflection.PropertyInfo, ) -> System.Linq.Expressions.PropertyExpression:
        ...

    @staticmethod
    @typing.overload
    def Make(expression: System.Linq.Expressions.Expression, field: System.Reflection.FieldInfo, ) -> System.Linq.Expressions.FieldExpression:
        ...

    @staticmethod
    @typing.overload
    def Make(expression: System.Linq.Expressions.Expression, member: System.Reflection.MemberInfo, ) -> System.Linq.Expressions.MemberExpression:
        ...

    def GetMember(self, ) -> System.Reflection.MemberInfo:
        ...

    def Accept(self, visitor: System.Linq.Expressions.ExpressionVisitor, ) -> System.Linq.Expressions.Expression:
        ...

    def Update(self, expression: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.MemberExpression:
        ...

class SymbolDocumentInfo(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields
    DocumentType_Text: System.Guid = ...

    # properties
    @property
    def FileName(self) -> str:
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
    def __init__(self, fileName: str, ):
        ...

class LabelExpression(System.Linq.Expressions.Expression):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def Type(self) -> System.Type:
        ...

    @property
    def NodeType(self) -> int:
        ...

    @property
    def Target(self) -> System.Linq.Expressions.LabelTarget:
        ...

    @property
    def DefaultValue(self) -> System.Linq.Expressions.Expression:
        ...

    @property
    def CanReduce(self) -> bool:
        ...

    # methods
    def __init__(self, label: System.Linq.Expressions.LabelTarget, defaultValue: System.Linq.Expressions.Expression, ):
        ...

    def Accept(self, visitor: System.Linq.Expressions.ExpressionVisitor, ) -> System.Linq.Expressions.Expression:
        ...

    def Update(self, target: System.Linq.Expressions.LabelTarget, defaultValue: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.LabelExpression:
        ...

class MethodCallExpression(System.Linq.Expressions.IArgumentProvider, System.Linq.Expressions.Expression):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def NodeType(self) -> int:
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
    def ArgumentCount(self) -> int:
        ...

    @property
    def CanReduce(self) -> bool:
        ...

    # methods
    def __init__(self, method: System.Reflection.MethodInfo, ):
        ...

    def GetInstance(self, ) -> System.Linq.Expressions.Expression:
        ...

    def Update(self, object: System.Linq.Expressions.Expression, arguments: System.Collections.Generic.IEnumerable[System.Linq.Expressions.Expression], ) -> System.Linq.Expressions.MethodCallExpression:
        ...

    def SameArguments(self, arguments: System.Collections.Generic.ICollection[System.Linq.Expressions.Expression], ) -> bool:
        ...

    def GetOrMakeArguments(self, ) -> System.Collections.ObjectModel.ReadOnlyCollection[System.Linq.Expressions.Expression]:
        ...

    def Accept(self, visitor: System.Linq.Expressions.ExpressionVisitor, ) -> System.Linq.Expressions.Expression:
        ...

    def Rewrite(self, instance: System.Linq.Expressions.Expression, args: System.Collections.Generic.IReadOnlyList[System.Linq.Expressions.Expression], ) -> System.Linq.Expressions.MethodCallExpression:
        ...

    def GetArgument(self, index: int, ) -> System.Linq.Expressions.Expression:
        ...

class RuntimeVariablesExpression(System.Linq.Expressions.Expression):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def Type(self) -> System.Type:
        ...

    @property
    def NodeType(self) -> int:
        ...

    @property
    def Variables(self) -> System.Collections.ObjectModel.ReadOnlyCollection[System.Linq.Expressions.ParameterExpression]:
        ...

    @property
    def CanReduce(self) -> bool:
        ...

    # methods
    def __init__(self, variables: System.Collections.ObjectModel.ReadOnlyCollection[System.Linq.Expressions.ParameterExpression], ):
        ...

    def Accept(self, visitor: System.Linq.Expressions.ExpressionVisitor, ) -> System.Linq.Expressions.Expression:
        ...

    def Update(self, variables: System.Collections.Generic.IEnumerable[System.Linq.Expressions.ParameterExpression], ) -> System.Linq.Expressions.RuntimeVariablesExpression:
        ...

class ExpressionVisitor(System.Object, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    def __init__(self, ):
        ...

    def VisitDynamic(self, node: System.Linq.Expressions.DynamicExpression, ) -> System.Linq.Expressions.Expression:
        ...

    @typing.overload
    def Visit(self, node: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.Expression:
        ...

    @typing.overload
    def Visit(self, nodes: System.Collections.ObjectModel.ReadOnlyCollection[System.Linq.Expressions.Expression], ) -> System.Collections.ObjectModel.ReadOnlyCollection[System.Linq.Expressions.Expression]:
        ...

    @staticmethod
    @typing.overload
    def Visit(nodes: System.Collections.ObjectModel.ReadOnlyCollection[T], elementVisitor: System.Func[T, T], ) -> System.Collections.ObjectModel.ReadOnlyCollection[T]:
        ...

    def VisitArguments(self, nodes: System.Linq.Expressions.IArgumentProvider, ) -> System.Array[System.Linq.Expressions.Expression]:
        ...

    def VisitParameters(self, nodes: System.Linq.Expressions.IParameterProvider, callerName: str, ) -> System.Array[System.Linq.Expressions.ParameterExpression]:
        ...

    @typing.overload
    def VisitAndConvert(self, node: T, callerName: str, ) -> T:
        ...

    @typing.overload
    def VisitAndConvert(self, nodes: System.Collections.ObjectModel.ReadOnlyCollection[T], callerName: str, ) -> System.Collections.ObjectModel.ReadOnlyCollection[T]:
        ...

    def VisitBinary(self, node: System.Linq.Expressions.BinaryExpression, ) -> System.Linq.Expressions.Expression:
        ...

    def VisitBlock(self, node: System.Linq.Expressions.BlockExpression, ) -> System.Linq.Expressions.Expression:
        ...

    def VisitConditional(self, node: System.Linq.Expressions.ConditionalExpression, ) -> System.Linq.Expressions.Expression:
        ...

    def VisitConstant(self, node: System.Linq.Expressions.ConstantExpression, ) -> System.Linq.Expressions.Expression:
        ...

    def VisitDebugInfo(self, node: System.Linq.Expressions.DebugInfoExpression, ) -> System.Linq.Expressions.Expression:
        ...

    def VisitDefault(self, node: System.Linq.Expressions.DefaultExpression, ) -> System.Linq.Expressions.Expression:
        ...

    def VisitExtension(self, node: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.Expression:
        ...

    def VisitGoto(self, node: System.Linq.Expressions.GotoExpression, ) -> System.Linq.Expressions.Expression:
        ...

    def VisitInvocation(self, node: System.Linq.Expressions.InvocationExpression, ) -> System.Linq.Expressions.Expression:
        ...

    def VisitLabelTarget(self, node: System.Linq.Expressions.LabelTarget, ) -> System.Linq.Expressions.LabelTarget:
        ...

    def VisitLabel(self, node: System.Linq.Expressions.LabelExpression, ) -> System.Linq.Expressions.Expression:
        ...

    def VisitLambda(self, node: System.Linq.Expressions.Expression[T], ) -> System.Linq.Expressions.Expression:
        ...

    def VisitLoop(self, node: System.Linq.Expressions.LoopExpression, ) -> System.Linq.Expressions.Expression:
        ...

    def VisitMember(self, node: System.Linq.Expressions.MemberExpression, ) -> System.Linq.Expressions.Expression:
        ...

    def VisitIndex(self, node: System.Linq.Expressions.IndexExpression, ) -> System.Linq.Expressions.Expression:
        ...

    def VisitMethodCall(self, node: System.Linq.Expressions.MethodCallExpression, ) -> System.Linq.Expressions.Expression:
        ...

    def VisitNewArray(self, node: System.Linq.Expressions.NewArrayExpression, ) -> System.Linq.Expressions.Expression:
        ...

    def VisitNew(self, node: System.Linq.Expressions.NewExpression, ) -> System.Linq.Expressions.Expression:
        ...

    def VisitParameter(self, node: System.Linq.Expressions.ParameterExpression, ) -> System.Linq.Expressions.Expression:
        ...

    def VisitRuntimeVariables(self, node: System.Linq.Expressions.RuntimeVariablesExpression, ) -> System.Linq.Expressions.Expression:
        ...

    def VisitSwitchCase(self, node: System.Linq.Expressions.SwitchCase, ) -> System.Linq.Expressions.SwitchCase:
        ...

    def VisitSwitch(self, node: System.Linq.Expressions.SwitchExpression, ) -> System.Linq.Expressions.Expression:
        ...

    def VisitCatchBlock(self, node: System.Linq.Expressions.CatchBlock, ) -> System.Linq.Expressions.CatchBlock:
        ...

    def VisitTry(self, node: System.Linq.Expressions.TryExpression, ) -> System.Linq.Expressions.Expression:
        ...

    def VisitTypeBinary(self, node: System.Linq.Expressions.TypeBinaryExpression, ) -> System.Linq.Expressions.Expression:
        ...

    def VisitUnary(self, node: System.Linq.Expressions.UnaryExpression, ) -> System.Linq.Expressions.Expression:
        ...

    def VisitMemberInit(self, node: System.Linq.Expressions.MemberInitExpression, ) -> System.Linq.Expressions.Expression:
        ...

    def VisitListInit(self, node: System.Linq.Expressions.ListInitExpression, ) -> System.Linq.Expressions.Expression:
        ...

    def VisitElementInit(self, node: System.Linq.Expressions.ElementInit, ) -> System.Linq.Expressions.ElementInit:
        ...

    def VisitMemberBinding(self, node: System.Linq.Expressions.MemberBinding, ) -> System.Linq.Expressions.MemberBinding:
        ...

    def VisitMemberAssignment(self, node: System.Linq.Expressions.MemberAssignment, ) -> System.Linq.Expressions.MemberAssignment:
        ...

    def VisitMemberMemberBinding(self, node: System.Linq.Expressions.MemberMemberBinding, ) -> System.Linq.Expressions.MemberMemberBinding:
        ...

    def VisitMemberListBinding(self, node: System.Linq.Expressions.MemberListBinding, ) -> System.Linq.Expressions.MemberListBinding:
        ...

    @staticmethod
    def ValidateUnary(before: System.Linq.Expressions.UnaryExpression, after: System.Linq.Expressions.UnaryExpression, ) -> System.Linq.Expressions.UnaryExpression:
        ...

    @staticmethod
    def ValidateBinary(before: System.Linq.Expressions.BinaryExpression, after: System.Linq.Expressions.BinaryExpression, ) -> System.Linq.Expressions.BinaryExpression:
        ...

    @staticmethod
    def ValidateSwitch(before: System.Linq.Expressions.SwitchExpression, after: System.Linq.Expressions.SwitchExpression, ) -> System.Linq.Expressions.SwitchExpression:
        ...

    @staticmethod
    def ValidateChildType(before: System.Type, after: System.Type, methodName: str, ) -> None:
        ...

class ListInitExpression(System.Linq.Expressions.Expression):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def NodeType(self) -> int:
        ...

    @property
    def Type(self) -> System.Type:
        ...

    @property
    def CanReduce(self) -> bool:
        ...

    @property
    def NewExpression(self) -> System.Linq.Expressions.NewExpression:
        ...

    @property
    def Initializers(self) -> System.Collections.ObjectModel.ReadOnlyCollection[System.Linq.Expressions.ElementInit]:
        ...

    # methods
    def __init__(self, newExpression: System.Linq.Expressions.NewExpression, initializers: System.Collections.ObjectModel.ReadOnlyCollection[System.Linq.Expressions.ElementInit], ):
        ...

    def Accept(self, visitor: System.Linq.Expressions.ExpressionVisitor, ) -> System.Linq.Expressions.Expression:
        ...

    def Reduce(self, ) -> System.Linq.Expressions.Expression:
        ...

    def Update(self, newExpression: System.Linq.Expressions.NewExpression, initializers: System.Collections.Generic.IEnumerable[System.Linq.Expressions.ElementInit], ) -> System.Linq.Expressions.ListInitExpression:
        ...

class LabelTarget(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def Name(self) -> str:
        ...

    @property
    def Type(self) -> System.Type:
        ...

    # methods
    def __init__(self, type: System.Type, name: str, ):
        ...

    def ToString(self, ) -> str:
        ...

class DefaultExpression(System.Linq.Expressions.Expression):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def Type(self) -> System.Type:
        ...

    @property
    def NodeType(self) -> int:
        ...

    @property
    def CanReduce(self) -> bool:
        ...

    # methods
    def __init__(self, type: System.Type, ):
        ...

    def Accept(self, visitor: System.Linq.Expressions.ExpressionVisitor, ) -> System.Linq.Expressions.Expression:
        ...

class DynamicExpressionVisitor(System.Linq.Expressions.ExpressionVisitor):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    def __init__(self, ):
        ...

    def VisitDynamic(self, node: System.Linq.Expressions.DynamicExpression, ) -> System.Linq.Expressions.Expression:
        ...

class DynamicExpression(System.Linq.Expressions.IDynamicExpression, System.Linq.Expressions.IArgumentProvider, System.Linq.Expressions.Expression):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def CanReduce(self) -> bool:
        ...

    @property
    def Type(self) -> System.Type:
        ...

    @property
    def NodeType(self) -> int:
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

    @property
    def ArgumentCount(self) -> int:
        ...

    # methods
    def __init__(self, delegateType: System.Type, binder: System.Runtime.CompilerServices.CallSiteBinder, ):
        ...

    def Reduce(self, ) -> System.Linq.Expressions.Expression:
        ...

    @staticmethod
    @typing.overload
    def Make(returnType: System.Type, delegateType: System.Type, binder: System.Runtime.CompilerServices.CallSiteBinder, arguments: System.Collections.ObjectModel.ReadOnlyCollection[System.Linq.Expressions.Expression], ) -> System.Linq.Expressions.DynamicExpression:
        ...

    @staticmethod
    @typing.overload
    def Make(returnType: System.Type, delegateType: System.Type, binder: System.Runtime.CompilerServices.CallSiteBinder, arg0: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.DynamicExpression:
        ...

    @staticmethod
    @typing.overload
    def Make(returnType: System.Type, delegateType: System.Type, binder: System.Runtime.CompilerServices.CallSiteBinder, arg0: System.Linq.Expressions.Expression, arg1: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.DynamicExpression:
        ...

    @staticmethod
    @typing.overload
    def Make(returnType: System.Type, delegateType: System.Type, binder: System.Runtime.CompilerServices.CallSiteBinder, arg0: System.Linq.Expressions.Expression, arg1: System.Linq.Expressions.Expression, arg2: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.DynamicExpression:
        ...

    @staticmethod
    @typing.overload
    def Make(returnType: System.Type, delegateType: System.Type, binder: System.Runtime.CompilerServices.CallSiteBinder, arg0: System.Linq.Expressions.Expression, arg1: System.Linq.Expressions.Expression, arg2: System.Linq.Expressions.Expression, arg3: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.DynamicExpression:
        ...

    def GetOrMakeArguments(self, ) -> System.Collections.ObjectModel.ReadOnlyCollection[System.Linq.Expressions.Expression]:
        ...

    def Accept(self, visitor: System.Linq.Expressions.ExpressionVisitor, ) -> System.Linq.Expressions.Expression:
        ...

    def Rewrite(self, args: System.Array[System.Linq.Expressions.Expression], ) -> System.Linq.Expressions.DynamicExpression:
        ...

    def Update(self, arguments: System.Collections.Generic.IEnumerable[System.Linq.Expressions.Expression], ) -> System.Linq.Expressions.DynamicExpression:
        ...

    def SameArguments(self, arguments: System.Collections.Generic.ICollection[System.Linq.Expressions.Expression], ) -> bool:
        ...

    def GetArgument(self, index: int, ) -> System.Linq.Expressions.Expression:
        ...

    @staticmethod
    @typing.overload
    def Dynamic(binder: System.Runtime.CompilerServices.CallSiteBinder, returnType: System.Type, arguments: System.Array[System.Linq.Expressions.Expression], ) -> System.Linq.Expressions.DynamicExpression:
        ...

    @staticmethod
    @typing.overload
    def Dynamic(binder: System.Runtime.CompilerServices.CallSiteBinder, returnType: System.Type, arguments: System.Collections.Generic.IEnumerable[System.Linq.Expressions.Expression], ) -> System.Linq.Expressions.DynamicExpression:
        ...

    @staticmethod
    @typing.overload
    def Dynamic(binder: System.Runtime.CompilerServices.CallSiteBinder, returnType: System.Type, arg0: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.DynamicExpression:
        ...

    @staticmethod
    @typing.overload
    def Dynamic(binder: System.Runtime.CompilerServices.CallSiteBinder, returnType: System.Type, arg0: System.Linq.Expressions.Expression, arg1: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.DynamicExpression:
        ...

    @staticmethod
    @typing.overload
    def Dynamic(binder: System.Runtime.CompilerServices.CallSiteBinder, returnType: System.Type, arg0: System.Linq.Expressions.Expression, arg1: System.Linq.Expressions.Expression, arg2: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.DynamicExpression:
        ...

    @staticmethod
    @typing.overload
    def Dynamic(binder: System.Runtime.CompilerServices.CallSiteBinder, returnType: System.Type, arg0: System.Linq.Expressions.Expression, arg1: System.Linq.Expressions.Expression, arg2: System.Linq.Expressions.Expression, arg3: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.DynamicExpression:
        ...

    @staticmethod
    @typing.overload
    def MakeDynamic(delegateType: System.Type, binder: System.Runtime.CompilerServices.CallSiteBinder, arguments: System.Collections.Generic.IEnumerable[System.Linq.Expressions.Expression], ) -> System.Linq.Expressions.DynamicExpression:
        ...

    @staticmethod
    @typing.overload
    def MakeDynamic(delegateType: System.Type, binder: System.Runtime.CompilerServices.CallSiteBinder, arguments: System.Array[System.Linq.Expressions.Expression], ) -> System.Linq.Expressions.DynamicExpression:
        ...

    @staticmethod
    @typing.overload
    def MakeDynamic(delegateType: System.Type, binder: System.Runtime.CompilerServices.CallSiteBinder, arg0: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.DynamicExpression:
        ...

    @staticmethod
    @typing.overload
    def MakeDynamic(delegateType: System.Type, binder: System.Runtime.CompilerServices.CallSiteBinder, arg0: System.Linq.Expressions.Expression, arg1: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.DynamicExpression:
        ...

    @staticmethod
    @typing.overload
    def MakeDynamic(delegateType: System.Type, binder: System.Runtime.CompilerServices.CallSiteBinder, arg0: System.Linq.Expressions.Expression, arg1: System.Linq.Expressions.Expression, arg2: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.DynamicExpression:
        ...

    @staticmethod
    @typing.overload
    def MakeDynamic(delegateType: System.Type, binder: System.Runtime.CompilerServices.CallSiteBinder, arg0: System.Linq.Expressions.Expression, arg1: System.Linq.Expressions.Expression, arg2: System.Linq.Expressions.Expression, arg3: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.DynamicExpression:
        ...

    def Rewrite(self, args: System.Array[System.Linq.Expressions.Expression], ) -> System.Linq.Expressions.Expression:
        ...

    def CreateCallSite(self, ) -> System.Object:
        ...

class GotoExpressionKind(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    Goto: int = ...
    Return: int = ...
    Break: int = ...
    Continue: int = ...

class MemberAssignment(System.Linq.Expressions.MemberBinding):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def Expression(self) -> System.Linq.Expressions.Expression:
        ...

    @property
    def BindingType(self) -> int:
        ...

    @property
    def Member(self) -> System.Reflection.MemberInfo:
        ...

    # methods
    def __init__(self, member: System.Reflection.MemberInfo, expression: System.Linq.Expressions.Expression, ):
        ...

    def Update(self, expression: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.MemberAssignment:
        ...

    def ValidateAsDefinedHere(self, index: int, ) -> None:
        ...

class CatchBlock(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

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
    def __init__(self, test: System.Type, variable: System.Linq.Expressions.ParameterExpression, body: System.Linq.Expressions.Expression, filter: System.Linq.Expressions.Expression, ):
        ...

    def ToString(self, ) -> str:
        ...

    def Update(self, variable: System.Linq.Expressions.ParameterExpression, filter: System.Linq.Expressions.Expression, body: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.CatchBlock:
        ...

class MemberMemberBinding(System.Linq.Expressions.MemberBinding):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def Bindings(self) -> System.Collections.ObjectModel.ReadOnlyCollection[System.Linq.Expressions.MemberBinding]:
        ...

    @property
    def BindingType(self) -> int:
        ...

    @property
    def Member(self) -> System.Reflection.MemberInfo:
        ...

    # methods
    def __init__(self, member: System.Reflection.MemberInfo, bindings: System.Collections.ObjectModel.ReadOnlyCollection[System.Linq.Expressions.MemberBinding], ):
        ...

    def Update(self, bindings: System.Collections.Generic.IEnumerable[System.Linq.Expressions.MemberBinding], ) -> System.Linq.Expressions.MemberMemberBinding:
        ...

    def ValidateAsDefinedHere(self, index: int, ) -> None:
        ...

class ExpressionType(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    Add: int = ...
    AddChecked: int = ...
    And: int = ...
    AndAlso: int = ...
    ArrayLength: int = ...
    ArrayIndex: int = ...
    Call: int = ...
    Coalesce: int = ...
    Conditional: int = ...
    Constant: int = ...
    Convert: int = ...
    ConvertChecked: int = ...
    Divide: int = ...
    Equal: int = ...
    ExclusiveOr: int = ...
    GreaterThan: int = ...
    GreaterThanOrEqual: int = ...
    Invoke: int = ...
    Lambda: int = ...
    LeftShift: int = ...
    LessThan: int = ...
    LessThanOrEqual: int = ...
    ListInit: int = ...
    MemberAccess: int = ...
    MemberInit: int = ...
    Modulo: int = ...
    Multiply: int = ...
    MultiplyChecked: int = ...
    Negate: int = ...
    UnaryPlus: int = ...
    NegateChecked: int = ...
    New: int = ...
    NewArrayInit: int = ...
    NewArrayBounds: int = ...
    Not: int = ...
    NotEqual: int = ...
    Or: int = ...
    OrElse: int = ...
    Parameter: int = ...
    Power: int = ...
    Quote: int = ...
    RightShift: int = ...
    Subtract: int = ...
    SubtractChecked: int = ...
    TypeAs: int = ...
    TypeIs: int = ...
    Assign: int = ...
    Block: int = ...
    DebugInfo: int = ...
    Decrement: int = ...
    Dynamic: int = ...
    Default: int = ...
    Extension: int = ...
    Goto: int = ...
    Increment: int = ...
    Index: int = ...
    Label: int = ...
    RuntimeVariables: int = ...
    Loop: int = ...
    Switch: int = ...
    Throw: int = ...
    Try: int = ...
    Unbox: int = ...
    AddAssign: int = ...
    AndAssign: int = ...
    DivideAssign: int = ...
    ExclusiveOrAssign: int = ...
    LeftShiftAssign: int = ...
    ModuloAssign: int = ...
    MultiplyAssign: int = ...
    OrAssign: int = ...
    PowerAssign: int = ...
    RightShiftAssign: int = ...
    SubtractAssign: int = ...
    AddAssignChecked: int = ...
    MultiplyAssignChecked: int = ...
    SubtractAssignChecked: int = ...
    PreIncrementAssign: int = ...
    PreDecrementAssign: int = ...
    PostIncrementAssign: int = ...
    PostDecrementAssign: int = ...
    TypeEqual: int = ...
    OnesComplement: int = ...
    IsTrue: int = ...
    IsFalse: int = ...

class BlockExpression(System.Linq.Expressions.Expression):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

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
    def NodeType(self) -> int:
        ...

    @property
    def Type(self) -> System.Type:
        ...

    @property
    def ExpressionCount(self) -> int:
        ...

    @property
    def CanReduce(self) -> bool:
        ...

    # methods
    def __init__(self, ):
        ...

    def Accept(self, visitor: System.Linq.Expressions.ExpressionVisitor, ) -> System.Linq.Expressions.Expression:
        ...

    def Update(self, variables: System.Collections.Generic.IEnumerable[System.Linq.Expressions.ParameterExpression], expressions: System.Collections.Generic.IEnumerable[System.Linq.Expressions.Expression], ) -> System.Linq.Expressions.BlockExpression:
        ...

    def SameVariables(self, variables: System.Collections.Generic.ICollection[System.Linq.Expressions.ParameterExpression], ) -> bool:
        ...

    def SameExpressions(self, expressions: System.Collections.Generic.ICollection[System.Linq.Expressions.Expression], ) -> bool:
        ...

    def GetExpression(self, index: int, ) -> System.Linq.Expressions.Expression:
        ...

    def GetOrMakeExpressions(self, ) -> System.Collections.ObjectModel.ReadOnlyCollection[System.Linq.Expressions.Expression]:
        ...

    def GetOrMakeVariables(self, ) -> System.Collections.ObjectModel.ReadOnlyCollection[System.Linq.Expressions.ParameterExpression]:
        ...

    def Rewrite(self, variables: System.Collections.ObjectModel.ReadOnlyCollection[System.Linq.Expressions.ParameterExpression], args: System.Array[System.Linq.Expressions.Expression], ) -> System.Linq.Expressions.BlockExpression:
        ...

    @staticmethod
    def ReturnReadOnlyExpressions(provider: System.Linq.Expressions.BlockExpression, collection: ref[System.Object], ) -> System.Collections.ObjectModel.ReadOnlyCollection[System.Linq.Expressions.Expression]:
        ...

class LambdaExpression(System.Linq.Expressions.IParameterProvider, System.Linq.Expressions.Expression, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def Type(self) -> System.Type:
        ...

    @property
    @abc.abstractmethod
    def TypeCore(self) -> System.Type:
        ...

    @property
    @abc.abstractmethod
    def PublicType(self) -> System.Type:
        ...

    @property
    def NodeType(self) -> int:
        ...

    @property
    def Parameters(self) -> System.Collections.ObjectModel.ReadOnlyCollection[System.Linq.Expressions.ParameterExpression]:
        ...

    @property
    def Name(self) -> str:
        ...

    @property
    def NameCore(self) -> str:
        ...

    @property
    def Body(self) -> System.Linq.Expressions.Expression:
        ...

    @property
    def ReturnType(self) -> System.Type:
        ...

    @property
    def TailCall(self) -> bool:
        ...

    @property
    def TailCallCore(self) -> bool:
        ...

    @property
    def ParameterCount(self) -> int:
        ...

    @property
    def ParameterCount(self) -> int:
        ...

    @property
    def CanReduce(self) -> bool:
        ...

    # methods
    def __init__(self, body: System.Linq.Expressions.Expression, ):
        ...

    def GetOrMakeParameters(self, ) -> System.Collections.ObjectModel.ReadOnlyCollection[System.Linq.Expressions.ParameterExpression]:
        ...

    def GetParameter(self, index: int, ) -> System.Linq.Expressions.ParameterExpression:
        ...

    def GetParameter(self, index: int, ) -> System.Linq.Expressions.ParameterExpression:
        ...

    @staticmethod
    def GetCompileMethod(lambdaExpressionType: System.Type, ) -> System.Reflection.MethodInfo:
        ...

    @typing.overload
    def Compile(self, ) -> System.Delegate:
        ...

    @typing.overload
    def Compile(self, preferInterpretation: bool, ) -> System.Delegate:
        ...

    @typing.overload
    def Compile(self, debugInfoGenerator: System.Runtime.CompilerServices.DebugInfoGenerator, ) -> System.Delegate:
        ...

    @abc.abstractmethod
    def Accept(self, spiller: System.Linq.Expressions.Compiler.StackSpiller, ) -> System.Linq.Expressions.LambdaExpression:
        ...

class InvocationExpression(System.Linq.Expressions.IArgumentProvider, System.Linq.Expressions.Expression):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def Type(self) -> System.Type:
        ...

    @property
    def NodeType(self) -> int:
        ...

    @property
    def Expression(self) -> System.Linq.Expressions.Expression:
        ...

    @property
    def Arguments(self) -> System.Collections.ObjectModel.ReadOnlyCollection[System.Linq.Expressions.Expression]:
        ...

    @property
    def ArgumentCount(self) -> int:
        ...

    @property
    def LambdaOperand(self) -> System.Linq.Expressions.LambdaExpression:
        ...

    @property
    def CanReduce(self) -> bool:
        ...

    # methods
    def __init__(self, expression: System.Linq.Expressions.Expression, returnType: System.Type, ):
        ...

    def Update(self, expression: System.Linq.Expressions.Expression, arguments: System.Collections.Generic.IEnumerable[System.Linq.Expressions.Expression], ) -> System.Linq.Expressions.InvocationExpression:
        ...

    def GetOrMakeArguments(self, ) -> System.Collections.ObjectModel.ReadOnlyCollection[System.Linq.Expressions.Expression]:
        ...

    def GetArgument(self, index: int, ) -> System.Linq.Expressions.Expression:
        ...

    def Accept(self, visitor: System.Linq.Expressions.ExpressionVisitor, ) -> System.Linq.Expressions.Expression:
        ...

    def Rewrite(self, lambda: System.Linq.Expressions.Expression, arguments: System.Array[System.Linq.Expressions.Expression], ) -> System.Linq.Expressions.InvocationExpression:
        ...

class NewExpression(System.Linq.Expressions.IArgumentProvider, System.Linq.Expressions.Expression):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def Type(self) -> System.Type:
        ...

    @property
    def NodeType(self) -> int:
        ...

    @property
    def Constructor(self) -> System.Reflection.ConstructorInfo:
        ...

    @property
    def Arguments(self) -> System.Collections.ObjectModel.ReadOnlyCollection[System.Linq.Expressions.Expression]:
        ...

    @property
    def ArgumentCount(self) -> int:
        ...

    @property
    def Members(self) -> System.Collections.ObjectModel.ReadOnlyCollection[System.Reflection.MemberInfo]:
        ...

    @property
    def CanReduce(self) -> bool:
        ...

    # methods
    def __init__(self, constructor: System.Reflection.ConstructorInfo, arguments: System.Collections.Generic.IReadOnlyList[System.Linq.Expressions.Expression], members: System.Collections.ObjectModel.ReadOnlyCollection[System.Reflection.MemberInfo], ):
        ...

    def GetArgument(self, index: int, ) -> System.Linq.Expressions.Expression:
        ...

    def Accept(self, visitor: System.Linq.Expressions.ExpressionVisitor, ) -> System.Linq.Expressions.Expression:
        ...

    def Update(self, arguments: System.Collections.Generic.IEnumerable[System.Linq.Expressions.Expression], ) -> System.Linq.Expressions.NewExpression:
        ...

class MemberBindingType(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    Assignment: int = ...
    MemberBinding: int = ...
    ListBinding: int = ...

class BinaryExpression(System.Linq.Expressions.Expression):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def CanReduce(self) -> bool:
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
    def IsLifted(self) -> bool:
        ...

    @property
    def IsLiftedToNull(self) -> bool:
        ...

    @property
    def IsLiftedLogical(self) -> bool:
        ...

    @property
    def IsReferenceComparison(self) -> bool:
        ...

    @property
    def NodeType(self) -> int:
        ...

    @property
    def Type(self) -> System.Type:
        ...

    # methods
    def __init__(self, left: System.Linq.Expressions.Expression, right: System.Linq.Expressions.Expression, ):
        ...

    @staticmethod
    def IsOpAssignment(op: int, ) -> bool:
        ...

    def GetMethod(self, ) -> System.Reflection.MethodInfo:
        ...

    def Update(self, left: System.Linq.Expressions.Expression, conversion: System.Linq.Expressions.LambdaExpression, right: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.BinaryExpression:
        ...

    def Reduce(self, ) -> System.Linq.Expressions.Expression:
        ...

    @staticmethod
    def GetBinaryOpFromAssignmentOp(op: int, ) -> int:
        ...

    def ReduceVariable(self, ) -> System.Linq.Expressions.Expression:
        ...

    def ReduceMember(self, ) -> System.Linq.Expressions.Expression:
        ...

    def ReduceIndex(self, ) -> System.Linq.Expressions.Expression:
        ...

    def GetConversion(self, ) -> System.Linq.Expressions.LambdaExpression:
        ...

    def Accept(self, visitor: System.Linq.Expressions.ExpressionVisitor, ) -> System.Linq.Expressions.Expression:
        ...

    @staticmethod
    def Create(nodeType: int, left: System.Linq.Expressions.Expression, right: System.Linq.Expressions.Expression, type: System.Type, method: System.Reflection.MethodInfo, conversion: System.Linq.Expressions.LambdaExpression, ) -> System.Linq.Expressions.BinaryExpression:
        ...

    def ReduceUserdefinedLifted(self, ) -> System.Linq.Expressions.Expression:
        ...

    @staticmethod
    def CallGetValueOrDefault(nullable: System.Linq.Expressions.ParameterExpression, ) -> System.Linq.Expressions.MethodCallExpression:
        ...

    @staticmethod
    def GetHasValueProperty(nullable: System.Linq.Expressions.ParameterExpression, ) -> System.Linq.Expressions.MemberExpression:
        ...

class IDynamicExpression(System.Linq.Expressions.IArgumentProvider, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    @abc.abstractmethod
    def DelegateType(self) -> System.Type:
        ...

    # methods
    @abc.abstractmethod
    def Rewrite(self, args: System.Array[System.Linq.Expressions.Expression], ) -> System.Linq.Expressions.Expression:
        ...

    @abc.abstractmethod
    def CreateCallSite(self, ) -> System.Object:
        ...

class IndexExpression(System.Linq.Expressions.IArgumentProvider, System.Linq.Expressions.Expression):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def NodeType(self) -> int:
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
    def ArgumentCount(self) -> int:
        ...

    @property
    def CanReduce(self) -> bool:
        ...

    # methods
    def __init__(self, instance: System.Linq.Expressions.Expression, indexer: System.Reflection.PropertyInfo, arguments: System.Collections.Generic.IReadOnlyList[System.Linq.Expressions.Expression], ):
        ...

    def Update(self, object: System.Linq.Expressions.Expression, arguments: System.Collections.Generic.IEnumerable[System.Linq.Expressions.Expression], ) -> System.Linq.Expressions.IndexExpression:
        ...

    def GetArgument(self, index: int, ) -> System.Linq.Expressions.Expression:
        ...

    def Accept(self, visitor: System.Linq.Expressions.ExpressionVisitor, ) -> System.Linq.Expressions.Expression:
        ...

    def Rewrite(self, instance: System.Linq.Expressions.Expression, arguments: System.Array[System.Linq.Expressions.Expression], ) -> System.Linq.Expressions.Expression:
        ...

