from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import System
import Microsoft.Scripting.Actions
import System.Dynamic
import IronPython.Runtime.Binding
import System.Linq.Expressions
import System.Collections.Generic


class FunctionBinderHelper(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def Signature(self) -> Microsoft.Scripting.Actions.CallSignature:
        ...

    # methods
    def __init__(self, call: System.Dynamic.DynamicMetaObjectBinder, function: IronPython.Runtime.Binding.MetaPythonFunction, codeContext: System.Linq.Expressions.Expression, args: System.Array[System.Dynamic.DynamicMetaObject], ):
        ...

    def MakeMetaObject(self, ) -> System.Dynamic.DynamicMetaObject:
        ...

    def GetRestrictions(self, ) -> System.Dynamic.BindingRestrictions:
        ...

    def GetSimpleRestriction(self, ) -> System.Dynamic.BindingRestrictions:
        ...

    def GetComplexRestriction(self, ) -> System.Dynamic.BindingRestrictions:
        ...

    def GetArgumentsForRule(self, ) -> System.Array[System.Linq.Expressions.Expression]:
        ...

    def FinishArguments(self, exprArgs: System.Array[System.Linq.Expressions.Expression], paramsArgs: System.Collections.Generic.List[System.Linq.Expressions.Expression], namedArgs: System.Collections.Generic.Dictionary[str, System.Linq.Expressions.Expression], ) -> bool:
        ...

    def TryFinishList(self, exprArgs: System.Array[System.Linq.Expressions.Expression], paramsArgs: System.Collections.Generic.List[System.Linq.Expressions.Expression], ) -> bool:
        ...

    def MakeParamsAddition(self, paramsArgs: System.Collections.Generic.List[System.Linq.Expressions.Expression], ) -> None:
        ...

    def TryFinishDictionary(self, exprArgs: System.Array[System.Linq.Expressions.Expression], namedArgs: System.Collections.Generic.Dictionary[str, System.Linq.Expressions.Expression], ) -> bool:
        ...

    def MakeDictionaryAddition(self, kvp: System.Collections.Generic.KeyValuePair[str, System.Linq.Expressions.Expression], ) -> None:
        ...

    def AddCheckForNoExtraParameters(self, exprArgs: System.Array[System.Linq.Expressions.Expression], ) -> None:
        ...

    def ValidateNotDuplicate(self, value: System.Linq.Expressions.Expression, name: str, position: int, ) -> System.Linq.Expressions.Expression:
        ...

    def ExtractNonDefaultValue(self, name: str, ) -> System.Linq.Expressions.Expression:
        ...

    def ExtractDictionaryArgument(self, name: str, ) -> System.Linq.Expressions.Expression:
        ...

    def ExtractDefaultValue(self, argName: str, dfltIndex: int, ) -> System.Linq.Expressions.Expression:
        ...

    def ExtractKeywordOnlyDefault(self, name: str, index: int, ) -> System.Linq.Expressions.Expression:
        ...

    def ExtractFromListOrDictionary(self, name: str, ) -> System.Linq.Expressions.Expression:
        ...

    def EnsureParams(self, ) -> None:
        ...

    def ExtractNextParamsArg(self, ) -> System.Linq.Expressions.Expression:
        ...

    @staticmethod
    def VariableOrNull(var: System.Linq.Expressions.ParameterExpression, type: System.Type, ) -> System.Linq.Expressions.Expression:
        ...

    def GetArgumentsForTargetType(self, exprArgs: System.Array[System.Linq.Expressions.Expression], ) -> System.Array[System.Linq.Expressions.Expression]:
        ...

    def GetFunctionParam(self, ) -> System.Linq.Expressions.UnaryExpression:
        ...

    def MakeDictionaryCopy(self, userDict: System.Dynamic.DynamicMetaObject, ) -> System.Dynamic.DynamicMetaObject:
        ...

    def MakeParamsCopy(self, userList: System.Linq.Expressions.Expression, ) -> None:
        ...

    def MakeDictionary(self, namedArgs: System.Collections.Generic.Dictionary[str, System.Linq.Expressions.Expression], ) -> System.Linq.Expressions.Expression:
        ...

    @staticmethod
    def MakeParamsTuple(extraArgs: System.Collections.Generic.List[System.Linq.Expressions.Expression], ) -> System.Linq.Expressions.Expression:
        ...

    def MakeFunctionInvoke(self, invokeArgs: System.Array[System.Linq.Expressions.Expression], ) -> System.Linq.Expressions.Expression:
        ...

    def AddInitialization(self, body: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.Expression:
        ...

    def MakeUnexpectedKeywordError(self, namedArgs: System.Collections.Generic.Dictionary[str, System.Linq.Expressions.Expression], ) -> None:
        ...

    def EnsureInit(self, ) -> None:
        ...

