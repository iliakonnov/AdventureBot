from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import IronPython.Compiler.Ast.UncollectableCompilationMode
import System
import System.Reflection
import System.Linq.Expressions
import System.Dynamic
import IronPython.Compiler.CompilationMode
import System.Collections.Generic
import Microsoft.Scripting.Interpreter
import IronPython.Runtime


class ConstantExpression(IronPython.Compiler.Ast.UncollectableCompilationMode.ReducibleExpression):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def Name(self) -> str:
        ...

    @property
    def FieldCount(self) -> int:
        ...

    @property
    def Type(self) -> System.Type:
        ...

    @property
    def Value(self) -> System.Object:
        ...

    @property
    def FieldInfo(self) -> System.Reflection.FieldInfo:
        ...

    @property
    def Start(self) -> int:
        ...
    @Start.setter
    def Start(self, val: int):
        ...

    @property
    def NodeType(self) -> int:
        ...

    @property
    def CanReduce(self) -> bool:
        ...

    # methods
    def __init__(self, offset: int, value: System.Object, ):
        ...

    def GetStorageType(self, index: int, ) -> System.Type:
        ...

    def Reduce(self, ) -> System.Linq.Expressions.Expression:
        ...

class ReducibleExpression(System.Linq.Expressions.Expression, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    @abc.abstractmethod
    def Name(self) -> str:
        ...

    @property
    @abc.abstractmethod
    def FieldCount(self) -> int:
        ...

    @property
    @abc.abstractmethod
    def Type(self) -> System.Type:
        ...

    @property
    def FieldInfo(self) -> System.Reflection.FieldInfo:
        ...

    @property
    def Start(self) -> int:
        ...
    @Start.setter
    def Start(self, val: int):
        ...

    @property
    def NodeType(self) -> int:
        ...

    @property
    def CanReduce(self) -> bool:
        ...

    # methods
    def __init__(self, offset: int, ):
        ...

    @abc.abstractmethod
    def GetStorageType(self, index: int, ) -> System.Type:
        ...

    def Reduce(self, ) -> System.Linq.Expressions.Expression:
        ...

    def Accept(self, visitor: System.Linq.Expressions.ExpressionVisitor, ) -> System.Linq.Expressions.Expression:
        ...

    def VisitChildren(self, visitor: System.Linq.Expressions.ExpressionVisitor, ) -> System.Linq.Expressions.Expression:
        ...

class DelegateCache(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        self.DelegateType: System.Type
        self.SiteType: System.Type
        self.NextSite: System.Func[System.Dynamic.DynamicMetaObjectBinder, IronPython.Compiler.CompilationMode.SiteInfo]
        self.TargetField: System.Reflection.FieldInfo
        self.InvokeMethod: System.Reflection.MethodInfo
        self.TypeChain: System.Collections.Generic.Dictionary[System.Type, IronPython.Compiler.Ast.UncollectableCompilationMode.DelegateCache]
        ...

    # static fields

    # properties
    # methods
    def __init__(self, ):
        ...

    def MakeDelegateType(self, retType: System.Type, args: System.Array[System.Linq.Expressions.Expression], ) -> None:
        ...

    @staticmethod
    def FirstCacheNode(argType: System.Type, ) -> IronPython.Compiler.Ast.UncollectableCompilationMode.DelegateCache:
        ...

    def NextCacheNode(self, argType: System.Type, ) -> IronPython.Compiler.Ast.UncollectableCompilationMode.DelegateCache:
        ...

class CodeContextExpression(Microsoft.Scripting.Interpreter.IInstructionProvider, System.Linq.Expressions.Expression):
    @typing.overload
    def __init__(self, **kwargs):
        self.Context: IronPython.Runtime.CodeContext
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

    # methods
    def __init__(self, expression: System.Linq.Expressions.Expression, ):
        ...

    def Reduce(self, ) -> System.Linq.Expressions.Expression:
        ...

    def AddInstructions(self, compiler: Microsoft.Scripting.Interpreter.LightCompiler, ) -> None:
        ...

class GlobalExpression(IronPython.Compiler.Ast.UncollectableCompilationMode.ReducibleExpression):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def Name(self) -> str:
        ...

    @property
    def FieldCount(self) -> int:
        ...

    @property
    def Type(self) -> System.Type:
        ...

    @property
    def FieldInfo(self) -> System.Reflection.FieldInfo:
        ...

    @property
    def Start(self) -> int:
        ...
    @Start.setter
    def Start(self, val: int):
        ...

    @property
    def NodeType(self) -> int:
        ...

    @property
    def CanReduce(self) -> bool:
        ...

    # methods
    def __init__(self, offset: int, ):
        ...

    def GetStorageType(self, index: int, ) -> System.Type:
        ...

