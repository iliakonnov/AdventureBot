from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import IronPython.Modules._ast
import System
import IronPython.Runtime
import IronPython.Compiler.Ast
import System.Collections.Generic
import System.Collections
import Microsoft.Scripting


class BitAnd(IronPython.Modules._ast.operator):
    @typing.overload
    def __init__(self, **kwargs):
        self._lineno: System.Nullable[int]
        self._col_offset: System.Nullable[int]
        ...

    # static fields
    Instance: IronPython.Modules._ast.BitAnd = ...

    # properties
    @property
    def _fields(self) -> IronPython.Runtime.PythonTuple:
        ...
    @_fields.setter
    def _fields(self, val: IronPython.Runtime.PythonTuple):
        ...

    @property
    def _attributes(self) -> IronPython.Runtime.PythonTuple:
        ...
    @_attributes.setter
    def _attributes(self, val: IronPython.Runtime.PythonTuple):
        ...

    @property
    def lineno(self) -> int:
        ...
    @lineno.setter
    def lineno(self, val: int):
        ...

    @property
    def col_offset(self) -> int:
        ...
    @col_offset.setter
    def col_offset(self, val: int):
        ...

    # methods
    def __init__(self, ):
        ...

    def Revert(self, ) -> int:
        ...

class AugLoad(IronPython.Modules._ast.expr_context):
    @typing.overload
    def __init__(self, **kwargs):
        self._lineno: System.Nullable[int]
        self._col_offset: System.Nullable[int]
        ...

    # static fields

    # properties
    @property
    def _fields(self) -> IronPython.Runtime.PythonTuple:
        ...
    @_fields.setter
    def _fields(self, val: IronPython.Runtime.PythonTuple):
        ...

    @property
    def _attributes(self) -> IronPython.Runtime.PythonTuple:
        ...
    @_attributes.setter
    def _attributes(self, val: IronPython.Runtime.PythonTuple):
        ...

    @property
    def lineno(self) -> int:
        ...
    @lineno.setter
    def lineno(self, val: int):
        ...

    @property
    def col_offset(self) -> int:
        ...
    @col_offset.setter
    def col_offset(self, val: int):
        ...

    # methods
    def __init__(self, ):
        ...

class excepthandler(IronPython.Modules._ast.AST):
    @typing.overload
    def __init__(self, **kwargs):
        self._lineno: System.Nullable[int]
        self._col_offset: System.Nullable[int]
        ...

    # static fields

    # properties
    @property
    def _fields(self) -> IronPython.Runtime.PythonTuple:
        ...
    @_fields.setter
    def _fields(self, val: IronPython.Runtime.PythonTuple):
        ...

    @property
    def _attributes(self) -> IronPython.Runtime.PythonTuple:
        ...
    @_attributes.setter
    def _attributes(self, val: IronPython.Runtime.PythonTuple):
        ...

    @property
    def lineno(self) -> int:
        ...
    @lineno.setter
    def lineno(self, val: int):
        ...

    @property
    def col_offset(self) -> int:
        ...
    @col_offset.setter
    def col_offset(self, val: int):
        ...

    # methods
    def __init__(self, ):
        ...

class Add(IronPython.Modules._ast.operator):
    @typing.overload
    def __init__(self, **kwargs):
        self._lineno: System.Nullable[int]
        self._col_offset: System.Nullable[int]
        ...

    # static fields
    Instance: IronPython.Modules._ast.Add = ...

    # properties
    @property
    def _fields(self) -> IronPython.Runtime.PythonTuple:
        ...
    @_fields.setter
    def _fields(self, val: IronPython.Runtime.PythonTuple):
        ...

    @property
    def _attributes(self) -> IronPython.Runtime.PythonTuple:
        ...
    @_attributes.setter
    def _attributes(self, val: IronPython.Runtime.PythonTuple):
        ...

    @property
    def lineno(self) -> int:
        ...
    @lineno.setter
    def lineno(self, val: int):
        ...

    @property
    def col_offset(self) -> int:
        ...
    @col_offset.setter
    def col_offset(self, val: int):
        ...

    # methods
    def __init__(self, ):
        ...

    def Revert(self, ) -> int:
        ...

class BitXor(IronPython.Modules._ast.operator):
    @typing.overload
    def __init__(self, **kwargs):
        self._lineno: System.Nullable[int]
        self._col_offset: System.Nullable[int]
        ...

    # static fields
    Instance: IronPython.Modules._ast.BitXor = ...

    # properties
    @property
    def _fields(self) -> IronPython.Runtime.PythonTuple:
        ...
    @_fields.setter
    def _fields(self, val: IronPython.Runtime.PythonTuple):
        ...

    @property
    def _attributes(self) -> IronPython.Runtime.PythonTuple:
        ...
    @_attributes.setter
    def _attributes(self, val: IronPython.Runtime.PythonTuple):
        ...

    @property
    def lineno(self) -> int:
        ...
    @lineno.setter
    def lineno(self, val: int):
        ...

    @property
    def col_offset(self) -> int:
        ...
    @col_offset.setter
    def col_offset(self, val: int):
        ...

    # methods
    def __init__(self, ):
        ...

    def Revert(self, ) -> int:
        ...

class cmpop(IronPython.Modules._ast.AST, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        self._lineno: System.Nullable[int]
        self._col_offset: System.Nullable[int]
        ...

    # static fields

    # properties
    @property
    def _fields(self) -> IronPython.Runtime.PythonTuple:
        ...
    @_fields.setter
    def _fields(self, val: IronPython.Runtime.PythonTuple):
        ...

    @property
    def _attributes(self) -> IronPython.Runtime.PythonTuple:
        ...
    @_attributes.setter
    def _attributes(self, val: IronPython.Runtime.PythonTuple):
        ...

    @property
    def lineno(self) -> int:
        ...
    @lineno.setter
    def lineno(self, val: int):
        ...

    @property
    def col_offset(self) -> int:
        ...
    @col_offset.setter
    def col_offset(self, val: int):
        ...

    # methods
    def __init__(self, ):
        ...

    @abc.abstractmethod
    def Revert(self, ) -> int:
        ...

class Num(IronPython.Modules._ast.expr):
    @typing.overload
    def __init__(self, **kwargs):
        self._lineno: System.Nullable[int]
        self._col_offset: System.Nullable[int]
        ...

    # static fields

    # properties
    @property
    def n(self) -> System.Object:
        ...
    @n.setter
    def n(self, val: System.Object):
        ...

    @property
    def _fields(self) -> IronPython.Runtime.PythonTuple:
        ...
    @_fields.setter
    def _fields(self, val: IronPython.Runtime.PythonTuple):
        ...

    @property
    def _attributes(self) -> IronPython.Runtime.PythonTuple:
        ...
    @_attributes.setter
    def _attributes(self, val: IronPython.Runtime.PythonTuple):
        ...

    @property
    def lineno(self) -> int:
        ...
    @lineno.setter
    def lineno(self, val: int):
        ...

    @property
    def col_offset(self) -> int:
        ...
    @col_offset.setter
    def col_offset(self, val: int):
        ...

    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def __init__(self, n: System.Object, ):
        ...

    @typing.overload
    def __init__(self, n: System.Object, lineno: System.Nullable[int], col_offset: System.Nullable[int], ):
        ...

    def Revert(self, ) -> IronPython.Compiler.Ast.Expression:
        ...

class NotEq(IronPython.Modules._ast.cmpop):
    @typing.overload
    def __init__(self, **kwargs):
        self._lineno: System.Nullable[int]
        self._col_offset: System.Nullable[int]
        ...

    # static fields
    Instance: IronPython.Modules._ast.NotEq = ...

    # properties
    @property
    def _fields(self) -> IronPython.Runtime.PythonTuple:
        ...
    @_fields.setter
    def _fields(self, val: IronPython.Runtime.PythonTuple):
        ...

    @property
    def _attributes(self) -> IronPython.Runtime.PythonTuple:
        ...
    @_attributes.setter
    def _attributes(self, val: IronPython.Runtime.PythonTuple):
        ...

    @property
    def lineno(self) -> int:
        ...
    @lineno.setter
    def lineno(self, val: int):
        ...

    @property
    def col_offset(self) -> int:
        ...
    @col_offset.setter
    def col_offset(self, val: int):
        ...

    # methods
    def __init__(self, ):
        ...

    def Revert(self, ) -> int:
        ...

class AST(System.Object, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        self._lineno: System.Nullable[int]
        self._col_offset: System.Nullable[int]
        ...

    # static fields

    # properties
    @property
    def _fields(self) -> IronPython.Runtime.PythonTuple:
        ...
    @_fields.setter
    def _fields(self, val: IronPython.Runtime.PythonTuple):
        ...

    @property
    def _attributes(self) -> IronPython.Runtime.PythonTuple:
        ...
    @_attributes.setter
    def _attributes(self, val: IronPython.Runtime.PythonTuple):
        ...

    @property
    def lineno(self) -> int:
        ...
    @lineno.setter
    def lineno(self, val: int):
        ...

    @property
    def col_offset(self) -> int:
        ...
    @col_offset.setter
    def col_offset(self, val: int):
        ...

    # methods
    def __init__(self, ):
        ...

    def __setstate__(self, state: IronPython.Runtime.PythonDictionary, ) -> None:
        ...

    def restoreProperties(self, names: System.Collections.Generic.IEnumerable[System.Object], source: System.Collections.IDictionary, ) -> None:
        ...

    def storeProperties(self, names: System.Collections.Generic.IEnumerable[System.Object], target: System.Collections.IDictionary, ) -> None:
        ...

    def getstate(self, ) -> IronPython.Runtime.PythonDictionary:
        ...

    def __reduce__(self, ) -> System.Object:
        ...

    def __reduce_ex__(self, protocol: int, ) -> System.Object:
        ...

    def GetSourceLocation(self, node: IronPython.Compiler.Ast.Node, ) -> None:
        ...

    @staticmethod
    @typing.overload
    def ConvertStatements(stmt: IronPython.Compiler.Ast.Statement, ) -> IronPython.Runtime.PythonList:
        ...

    @staticmethod
    @typing.overload
    def ConvertStatements(stmt: IronPython.Compiler.Ast.Statement, allowNull: bool, ) -> IronPython.Runtime.PythonList:
        ...

    @staticmethod
    @typing.overload
    def Convert(stmt: IronPython.Compiler.Ast.Statement, ) -> IronPython.Modules._ast.stmt:
        ...

    @staticmethod
    @typing.overload
    def Convert(expr: IronPython.Compiler.Ast.Expression, ) -> IronPython.Modules._ast.expr:
        ...

    @staticmethod
    @typing.overload
    def Convert(expr: IronPython.Compiler.Ast.Expression, ctx: IronPython.Modules._ast.expr_context, ) -> IronPython.Modules._ast.expr:
        ...

    @staticmethod
    @typing.overload
    def Convert(expr: IronPython.Compiler.Ast.ConstantExpression, ) -> IronPython.Modules._ast.expr:
        ...

    @staticmethod
    @typing.overload
    def Convert(expr: IronPython.Compiler.Ast.BinaryExpression, ) -> IronPython.Modules._ast.expr:
        ...

    @staticmethod
    @typing.overload
    def Convert(node: IronPython.Compiler.Ast.Node, ) -> IronPython.Modules._ast.AST:
        ...

    @staticmethod
    @typing.overload
    def Convert(iters: System.Collections.Generic.IReadOnlyList[IronPython.Compiler.Ast.ComprehensionIterator], ) -> IronPython.Runtime.PythonList:
        ...

    @staticmethod
    @typing.overload
    def Convert(op: int, ) -> IronPython.Modules._ast.AST:
        ...

    @staticmethod
    @typing.overload
    def ConvertAliases(names: System.Collections.Generic.IList[IronPython.Compiler.Ast.DottedName], asnames: System.Collections.Generic.IList[str], ) -> IronPython.Runtime.PythonList:
        ...

    @staticmethod
    @typing.overload
    def ConvertAliases(names: System.Collections.Generic.IList[str], asnames: System.Collections.Generic.IList[str], ) -> IronPython.Runtime.PythonList:
        ...

    @staticmethod
    def TrySliceConvert(expr: IronPython.Compiler.Ast.Expression, ) -> IronPython.Modules._ast.slice:
        ...

class arguments(IronPython.Modules._ast.AST):
    @typing.overload
    def __init__(self, **kwargs):
        self._lineno: System.Nullable[int]
        self._col_offset: System.Nullable[int]
        ...

    # static fields

    # properties
    @property
    def args(self) -> IronPython.Runtime.PythonList:
        ...
    @args.setter
    def args(self, val: IronPython.Runtime.PythonList):
        ...

    @property
    def vararg(self) -> IronPython.Modules._ast.ArgType:
        ...
    @vararg.setter
    def vararg(self, val: IronPython.Modules._ast.ArgType):
        ...

    @property
    def kwonlyargs(self) -> IronPython.Runtime.PythonList:
        ...
    @kwonlyargs.setter
    def kwonlyargs(self, val: IronPython.Runtime.PythonList):
        ...

    @property
    def kw_defaults(self) -> IronPython.Runtime.PythonList:
        ...
    @kw_defaults.setter
    def kw_defaults(self, val: IronPython.Runtime.PythonList):
        ...

    @property
    def kwarg(self) -> IronPython.Modules._ast.ArgType:
        ...
    @kwarg.setter
    def kwarg(self, val: IronPython.Modules._ast.ArgType):
        ...

    @property
    def defaults(self) -> IronPython.Runtime.PythonList:
        ...
    @defaults.setter
    def defaults(self, val: IronPython.Runtime.PythonList):
        ...

    @property
    def _fields(self) -> IronPython.Runtime.PythonTuple:
        ...
    @_fields.setter
    def _fields(self, val: IronPython.Runtime.PythonTuple):
        ...

    @property
    def _attributes(self) -> IronPython.Runtime.PythonTuple:
        ...
    @_attributes.setter
    def _attributes(self, val: IronPython.Runtime.PythonTuple):
        ...

    @property
    def lineno(self) -> int:
        ...
    @lineno.setter
    def lineno(self, val: int):
        ...

    @property
    def col_offset(self) -> int:
        ...
    @col_offset.setter
    def col_offset(self, val: int):
        ...

    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def __init__(self, args: IronPython.Runtime.PythonList, vararg: IronPython.Modules._ast.ArgType, kwonlyargs: IronPython.Runtime.PythonList, kw_defaults: IronPython.Runtime.PythonList, kwarg: IronPython.Modules._ast.ArgType, defaults: IronPython.Runtime.PythonList, ):
        ...

    @typing.overload
    def __init__(self, parameters: System.Collections.Generic.IList[IronPython.Compiler.Ast.Parameter], ):
        ...

    def Revert(self, ) -> System.Array[IronPython.Compiler.Ast.Parameter]:
        ...

class ArgType(IronPython.Modules._ast.AST):
    @typing.overload
    def __init__(self, **kwargs):
        self._lineno: System.Nullable[int]
        self._col_offset: System.Nullable[int]
        ...

    # static fields

    # properties
    @property
    def arg(self) -> str:
        ...
    @arg.setter
    def arg(self, val: str):
        ...

    @property
    def annotation(self) -> System.Object:
        ...
    @annotation.setter
    def annotation(self, val: System.Object):
        ...

    @property
    def _fields(self) -> IronPython.Runtime.PythonTuple:
        ...
    @_fields.setter
    def _fields(self, val: IronPython.Runtime.PythonTuple):
        ...

    @property
    def _attributes(self) -> IronPython.Runtime.PythonTuple:
        ...
    @_attributes.setter
    def _attributes(self, val: IronPython.Runtime.PythonTuple):
        ...

    @property
    def lineno(self) -> int:
        ...
    @lineno.setter
    def lineno(self, val: int):
        ...

    @property
    def col_offset(self) -> int:
        ...
    @col_offset.setter
    def col_offset(self, val: int):
        ...

    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def __init__(self, arg: str, annotation: System.Object, ):
        ...

    @typing.overload
    def __init__(self, parameter: IronPython.Compiler.Ast.Parameter, ):
        ...

class MatMult(IronPython.Modules._ast.operator):
    @typing.overload
    def __init__(self, **kwargs):
        self._lineno: System.Nullable[int]
        self._col_offset: System.Nullable[int]
        ...

    # static fields
    Instance: IronPython.Modules._ast.MatMult = ...

    # properties
    @property
    def _fields(self) -> IronPython.Runtime.PythonTuple:
        ...
    @_fields.setter
    def _fields(self, val: IronPython.Runtime.PythonTuple):
        ...

    @property
    def _attributes(self) -> IronPython.Runtime.PythonTuple:
        ...
    @_attributes.setter
    def _attributes(self, val: IronPython.Runtime.PythonTuple):
        ...

    @property
    def lineno(self) -> int:
        ...
    @lineno.setter
    def lineno(self, val: int):
        ...

    @property
    def col_offset(self) -> int:
        ...
    @col_offset.setter
    def col_offset(self, val: int):
        ...

    # methods
    def __init__(self, ):
        ...

    def Revert(self, ) -> int:
        ...

class Delete(IronPython.Modules._ast.stmt):
    @typing.overload
    def __init__(self, **kwargs):
        self._lineno: System.Nullable[int]
        self._col_offset: System.Nullable[int]
        ...

    # static fields

    # properties
    @property
    def targets(self) -> IronPython.Runtime.PythonList:
        ...
    @targets.setter
    def targets(self, val: IronPython.Runtime.PythonList):
        ...

    @property
    def _fields(self) -> IronPython.Runtime.PythonTuple:
        ...
    @_fields.setter
    def _fields(self, val: IronPython.Runtime.PythonTuple):
        ...

    @property
    def _attributes(self) -> IronPython.Runtime.PythonTuple:
        ...
    @_attributes.setter
    def _attributes(self, val: IronPython.Runtime.PythonTuple):
        ...

    @property
    def lineno(self) -> int:
        ...
    @lineno.setter
    def lineno(self, val: int):
        ...

    @property
    def col_offset(self) -> int:
        ...
    @col_offset.setter
    def col_offset(self, val: int):
        ...

    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def __init__(self, targets: IronPython.Runtime.PythonList, lineno: System.Nullable[int], col_offset: System.Nullable[int], ):
        ...

    @typing.overload
    def __init__(self, stmt: IronPython.Compiler.Ast.DelStatement, ):
        ...

    def Revert(self, ) -> IronPython.Compiler.Ast.Statement:
        ...

class Break(IronPython.Modules._ast.stmt):
    @typing.overload
    def __init__(self, **kwargs):
        self._lineno: System.Nullable[int]
        self._col_offset: System.Nullable[int]
        ...

    # static fields
    Instance: IronPython.Modules._ast.Break = ...

    # properties
    @property
    def _fields(self) -> IronPython.Runtime.PythonTuple:
        ...
    @_fields.setter
    def _fields(self, val: IronPython.Runtime.PythonTuple):
        ...

    @property
    def _attributes(self) -> IronPython.Runtime.PythonTuple:
        ...
    @_attributes.setter
    def _attributes(self, val: IronPython.Runtime.PythonTuple):
        ...

    @property
    def lineno(self) -> int:
        ...
    @lineno.setter
    def lineno(self, val: int):
        ...

    @property
    def col_offset(self) -> int:
        ...
    @col_offset.setter
    def col_offset(self, val: int):
        ...

    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def __init__(self, lineno: System.Nullable[int], col_offset: System.Nullable[int], ):
        ...

    def Revert(self, ) -> IronPython.Compiler.Ast.Statement:
        ...

class Gt(IronPython.Modules._ast.cmpop):
    @typing.overload
    def __init__(self, **kwargs):
        self._lineno: System.Nullable[int]
        self._col_offset: System.Nullable[int]
        ...

    # static fields
    Instance: IronPython.Modules._ast.Gt = ...

    # properties
    @property
    def _fields(self) -> IronPython.Runtime.PythonTuple:
        ...
    @_fields.setter
    def _fields(self, val: IronPython.Runtime.PythonTuple):
        ...

    @property
    def _attributes(self) -> IronPython.Runtime.PythonTuple:
        ...
    @_attributes.setter
    def _attributes(self, val: IronPython.Runtime.PythonTuple):
        ...

    @property
    def lineno(self) -> int:
        ...
    @lineno.setter
    def lineno(self, val: int):
        ...

    @property
    def col_offset(self) -> int:
        ...
    @col_offset.setter
    def col_offset(self, val: int):
        ...

    # methods
    def __init__(self, ):
        ...

    def Revert(self, ) -> int:
        ...

class NotIn(IronPython.Modules._ast.cmpop):
    @typing.overload
    def __init__(self, **kwargs):
        self._lineno: System.Nullable[int]
        self._col_offset: System.Nullable[int]
        ...

    # static fields
    Instance: IronPython.Modules._ast.NotIn = ...

    # properties
    @property
    def _fields(self) -> IronPython.Runtime.PythonTuple:
        ...
    @_fields.setter
    def _fields(self, val: IronPython.Runtime.PythonTuple):
        ...

    @property
    def _attributes(self) -> IronPython.Runtime.PythonTuple:
        ...
    @_attributes.setter
    def _attributes(self, val: IronPython.Runtime.PythonTuple):
        ...

    @property
    def lineno(self) -> int:
        ...
    @lineno.setter
    def lineno(self, val: int):
        ...

    @property
    def col_offset(self) -> int:
        ...
    @col_offset.setter
    def col_offset(self, val: int):
        ...

    # methods
    def __init__(self, ):
        ...

    def Revert(self, ) -> int:
        ...

class GtE(IronPython.Modules._ast.cmpop):
    @typing.overload
    def __init__(self, **kwargs):
        self._lineno: System.Nullable[int]
        self._col_offset: System.Nullable[int]
        ...

    # static fields
    Instance: IronPython.Modules._ast.GtE = ...

    # properties
    @property
    def _fields(self) -> IronPython.Runtime.PythonTuple:
        ...
    @_fields.setter
    def _fields(self, val: IronPython.Runtime.PythonTuple):
        ...

    @property
    def _attributes(self) -> IronPython.Runtime.PythonTuple:
        ...
    @_attributes.setter
    def _attributes(self, val: IronPython.Runtime.PythonTuple):
        ...

    @property
    def lineno(self) -> int:
        ...
    @lineno.setter
    def lineno(self, val: int):
        ...

    @property
    def col_offset(self) -> int:
        ...
    @col_offset.setter
    def col_offset(self, val: int):
        ...

    # methods
    def __init__(self, ):
        ...

    def Revert(self, ) -> int:
        ...

class Load(IronPython.Modules._ast.expr_context):
    @typing.overload
    def __init__(self, **kwargs):
        self._lineno: System.Nullable[int]
        self._col_offset: System.Nullable[int]
        ...

    # static fields
    Instance: IronPython.Modules._ast.Load = ...

    # properties
    @property
    def _fields(self) -> IronPython.Runtime.PythonTuple:
        ...
    @_fields.setter
    def _fields(self, val: IronPython.Runtime.PythonTuple):
        ...

    @property
    def _attributes(self) -> IronPython.Runtime.PythonTuple:
        ...
    @_attributes.setter
    def _attributes(self, val: IronPython.Runtime.PythonTuple):
        ...

    @property
    def lineno(self) -> int:
        ...
    @lineno.setter
    def lineno(self, val: int):
        ...

    @property
    def col_offset(self) -> int:
        ...
    @col_offset.setter
    def col_offset(self, val: int):
        ...

    # methods
    def __init__(self, ):
        ...

class ExtSlice(IronPython.Modules._ast.slice):
    @typing.overload
    def __init__(self, **kwargs):
        self._lineno: System.Nullable[int]
        self._col_offset: System.Nullable[int]
        ...

    # static fields

    # properties
    @property
    def dims(self) -> IronPython.Runtime.PythonList:
        ...
    @dims.setter
    def dims(self, val: IronPython.Runtime.PythonList):
        ...

    @property
    def _fields(self) -> IronPython.Runtime.PythonTuple:
        ...
    @_fields.setter
    def _fields(self, val: IronPython.Runtime.PythonTuple):
        ...

    @property
    def _attributes(self) -> IronPython.Runtime.PythonTuple:
        ...
    @_attributes.setter
    def _attributes(self, val: IronPython.Runtime.PythonTuple):
        ...

    @property
    def lineno(self) -> int:
        ...
    @lineno.setter
    def lineno(self, val: int):
        ...

    @property
    def col_offset(self) -> int:
        ...
    @col_offset.setter
    def col_offset(self, val: int):
        ...

    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def __init__(self, dims: IronPython.Runtime.PythonList, ):
        ...

    def Revert(self, ) -> System.Array[IronPython.Compiler.Ast.Expression]:
        ...

class For(IronPython.Modules._ast.stmt):
    @typing.overload
    def __init__(self, **kwargs):
        self._lineno: System.Nullable[int]
        self._col_offset: System.Nullable[int]
        ...

    # static fields

    # properties
    @property
    def target(self) -> IronPython.Modules._ast.expr:
        ...
    @target.setter
    def target(self, val: IronPython.Modules._ast.expr):
        ...

    @property
    def iter(self) -> IronPython.Modules._ast.expr:
        ...
    @iter.setter
    def iter(self, val: IronPython.Modules._ast.expr):
        ...

    @property
    def body(self) -> IronPython.Runtime.PythonList:
        ...
    @body.setter
    def body(self, val: IronPython.Runtime.PythonList):
        ...

    @property
    def orelse(self) -> IronPython.Runtime.PythonList:
        ...
    @orelse.setter
    def orelse(self, val: IronPython.Runtime.PythonList):
        ...

    @property
    def _fields(self) -> IronPython.Runtime.PythonTuple:
        ...
    @_fields.setter
    def _fields(self, val: IronPython.Runtime.PythonTuple):
        ...

    @property
    def _attributes(self) -> IronPython.Runtime.PythonTuple:
        ...
    @_attributes.setter
    def _attributes(self, val: IronPython.Runtime.PythonTuple):
        ...

    @property
    def lineno(self) -> int:
        ...
    @lineno.setter
    def lineno(self, val: int):
        ...

    @property
    def col_offset(self) -> int:
        ...
    @col_offset.setter
    def col_offset(self, val: int):
        ...

    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def __init__(self, target: IronPython.Modules._ast.expr, iter: IronPython.Modules._ast.expr, body: IronPython.Runtime.PythonList, orelse: IronPython.Runtime.PythonList, lineno: System.Nullable[int], col_offset: System.Nullable[int], ):
        ...

    @typing.overload
    def __init__(self, stmt: IronPython.Compiler.Ast.ForStatement, ):
        ...

    def Revert(self, ) -> IronPython.Compiler.Ast.Statement:
        ...

class FormattedValue(IronPython.Modules._ast.expr):
    @typing.overload
    def __init__(self, **kwargs):
        self._lineno: System.Nullable[int]
        self._col_offset: System.Nullable[int]
        ...

    # static fields

    # properties
    @property
    def value(self) -> IronPython.Modules._ast.expr:
        ...
    @value.setter
    def value(self, val: IronPython.Modules._ast.expr):
        ...

    @property
    def conversion(self) -> int:
        ...
    @conversion.setter
    def conversion(self, val: int):
        ...

    @property
    def format_spec(self) -> IronPython.Modules._ast.expr:
        ...
    @format_spec.setter
    def format_spec(self, val: IronPython.Modules._ast.expr):
        ...

    @property
    def _fields(self) -> IronPython.Runtime.PythonTuple:
        ...
    @_fields.setter
    def _fields(self, val: IronPython.Runtime.PythonTuple):
        ...

    @property
    def _attributes(self) -> IronPython.Runtime.PythonTuple:
        ...
    @_attributes.setter
    def _attributes(self, val: IronPython.Runtime.PythonTuple):
        ...

    @property
    def lineno(self) -> int:
        ...
    @lineno.setter
    def lineno(self, val: int):
        ...

    @property
    def col_offset(self) -> int:
        ...
    @col_offset.setter
    def col_offset(self, val: int):
        ...

    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def __init__(self, value: IronPython.Modules._ast.expr, conversion: int, format_spec: IronPython.Modules._ast.expr, lineno: System.Nullable[int], col_offset: System.Nullable[int], ):
        ...

    @typing.overload
    def __init__(self, expr: IronPython.Compiler.Ast.FormattedValueExpression, ):
        ...

    def Revert(self, ) -> IronPython.Compiler.Ast.Expression:
        ...

class FunctionDef(IronPython.Modules._ast.stmt):
    @typing.overload
    def __init__(self, **kwargs):
        self._lineno: System.Nullable[int]
        self._col_offset: System.Nullable[int]
        ...

    # static fields

    # properties
    @property
    def name(self) -> str:
        ...
    @name.setter
    def name(self, val: str):
        ...

    @property
    def args(self) -> IronPython.Modules._ast.arguments:
        ...
    @args.setter
    def args(self, val: IronPython.Modules._ast.arguments):
        ...

    @property
    def body(self) -> IronPython.Runtime.PythonList:
        ...
    @body.setter
    def body(self, val: IronPython.Runtime.PythonList):
        ...

    @property
    def decorator_list(self) -> IronPython.Runtime.PythonList:
        ...
    @decorator_list.setter
    def decorator_list(self, val: IronPython.Runtime.PythonList):
        ...

    @property
    def returns(self) -> IronPython.Modules._ast.expr:
        ...
    @returns.setter
    def returns(self, val: IronPython.Modules._ast.expr):
        ...

    @property
    def _fields(self) -> IronPython.Runtime.PythonTuple:
        ...
    @_fields.setter
    def _fields(self, val: IronPython.Runtime.PythonTuple):
        ...

    @property
    def _attributes(self) -> IronPython.Runtime.PythonTuple:
        ...
    @_attributes.setter
    def _attributes(self, val: IronPython.Runtime.PythonTuple):
        ...

    @property
    def lineno(self) -> int:
        ...
    @lineno.setter
    def lineno(self, val: int):
        ...

    @property
    def col_offset(self) -> int:
        ...
    @col_offset.setter
    def col_offset(self, val: int):
        ...

    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def __init__(self, name: str, args: IronPython.Modules._ast.arguments, body: IronPython.Runtime.PythonList, decorator_list: IronPython.Runtime.PythonList, returns: IronPython.Modules._ast.expr, lineno: System.Nullable[int], col_offset: System.Nullable[int], ):
        ...

    @typing.overload
    def __init__(self, def: IronPython.Compiler.Ast.FunctionDefinition, ):
        ...

    def Revert(self, ) -> IronPython.Compiler.Ast.Statement:
        ...

class Del(IronPython.Modules._ast.expr_context):
    @typing.overload
    def __init__(self, **kwargs):
        self._lineno: System.Nullable[int]
        self._col_offset: System.Nullable[int]
        ...

    # static fields
    Instance: IronPython.Modules._ast.Del = ...

    # properties
    @property
    def _fields(self) -> IronPython.Runtime.PythonTuple:
        ...
    @_fields.setter
    def _fields(self, val: IronPython.Runtime.PythonTuple):
        ...

    @property
    def _attributes(self) -> IronPython.Runtime.PythonTuple:
        ...
    @_attributes.setter
    def _attributes(self, val: IronPython.Runtime.PythonTuple):
        ...

    @property
    def lineno(self) -> int:
        ...
    @lineno.setter
    def lineno(self, val: int):
        ...

    @property
    def col_offset(self) -> int:
        ...
    @col_offset.setter
    def col_offset(self, val: int):
        ...

    # methods
    def __init__(self, ):
        ...

class Set(IronPython.Modules._ast.expr):
    @typing.overload
    def __init__(self, **kwargs):
        self._lineno: System.Nullable[int]
        self._col_offset: System.Nullable[int]
        ...

    # static fields

    # properties
    @property
    def elts(self) -> IronPython.Runtime.PythonList:
        ...
    @elts.setter
    def elts(self, val: IronPython.Runtime.PythonList):
        ...

    @property
    def _fields(self) -> IronPython.Runtime.PythonTuple:
        ...
    @_fields.setter
    def _fields(self, val: IronPython.Runtime.PythonTuple):
        ...

    @property
    def _attributes(self) -> IronPython.Runtime.PythonTuple:
        ...
    @_attributes.setter
    def _attributes(self, val: IronPython.Runtime.PythonTuple):
        ...

    @property
    def lineno(self) -> int:
        ...
    @lineno.setter
    def lineno(self, val: int):
        ...

    @property
    def col_offset(self) -> int:
        ...
    @col_offset.setter
    def col_offset(self, val: int):
        ...

    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def __init__(self, elts: IronPython.Runtime.PythonList, lineno: System.Nullable[int], col_offset: System.Nullable[int], ):
        ...

    @typing.overload
    def __init__(self, setExpression: IronPython.Compiler.Ast.SetExpression, ):
        ...

    def Revert(self, ) -> IronPython.Compiler.Ast.Expression:
        ...

class Attribute(IronPython.Modules._ast.expr):
    @typing.overload
    def __init__(self, **kwargs):
        self._lineno: System.Nullable[int]
        self._col_offset: System.Nullable[int]
        ...

    # static fields

    # properties
    @property
    def value(self) -> IronPython.Modules._ast.expr:
        ...
    @value.setter
    def value(self, val: IronPython.Modules._ast.expr):
        ...

    @property
    def attr(self) -> str:
        ...
    @attr.setter
    def attr(self, val: str):
        ...

    @property
    def ctx(self) -> IronPython.Modules._ast.expr_context:
        ...
    @ctx.setter
    def ctx(self, val: IronPython.Modules._ast.expr_context):
        ...

    @property
    def _fields(self) -> IronPython.Runtime.PythonTuple:
        ...
    @_fields.setter
    def _fields(self, val: IronPython.Runtime.PythonTuple):
        ...

    @property
    def _attributes(self) -> IronPython.Runtime.PythonTuple:
        ...
    @_attributes.setter
    def _attributes(self, val: IronPython.Runtime.PythonTuple):
        ...

    @property
    def lineno(self) -> int:
        ...
    @lineno.setter
    def lineno(self, val: int):
        ...

    @property
    def col_offset(self) -> int:
        ...
    @col_offset.setter
    def col_offset(self, val: int):
        ...

    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def __init__(self, value: IronPython.Modules._ast.expr, attr: str, ctx: IronPython.Modules._ast.expr_context, lineno: System.Nullable[int], col_offset: System.Nullable[int], ):
        ...

    @typing.overload
    def __init__(self, attr: IronPython.Compiler.Ast.MemberExpression, ctx: IronPython.Modules._ast.expr_context, ):
        ...

    def Revert(self, ) -> IronPython.Compiler.Ast.Expression:
        ...

class Return(IronPython.Modules._ast.stmt):
    @typing.overload
    def __init__(self, **kwargs):
        self._lineno: System.Nullable[int]
        self._col_offset: System.Nullable[int]
        ...

    # static fields

    # properties
    @property
    def value(self) -> IronPython.Modules._ast.expr:
        ...
    @value.setter
    def value(self, val: IronPython.Modules._ast.expr):
        ...

    @property
    def _fields(self) -> IronPython.Runtime.PythonTuple:
        ...
    @_fields.setter
    def _fields(self, val: IronPython.Runtime.PythonTuple):
        ...

    @property
    def _attributes(self) -> IronPython.Runtime.PythonTuple:
        ...
    @_attributes.setter
    def _attributes(self, val: IronPython.Runtime.PythonTuple):
        ...

    @property
    def lineno(self) -> int:
        ...
    @lineno.setter
    def lineno(self, val: int):
        ...

    @property
    def col_offset(self) -> int:
        ...
    @col_offset.setter
    def col_offset(self, val: int):
        ...

    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def __init__(self, value: IronPython.Modules._ast.expr, lineno: System.Nullable[int], col_offset: System.Nullable[int], ):
        ...

    @typing.overload
    def __init__(self, statement: IronPython.Compiler.Ast.ReturnStatement, ):
        ...

    def Revert(self, ) -> IronPython.Compiler.Ast.Statement:
        ...

class USub(IronPython.Modules._ast.unaryop):
    @typing.overload
    def __init__(self, **kwargs):
        self._lineno: System.Nullable[int]
        self._col_offset: System.Nullable[int]
        ...

    # static fields
    Instance: IronPython.Modules._ast.USub = ...

    # properties
    @property
    def _fields(self) -> IronPython.Runtime.PythonTuple:
        ...
    @_fields.setter
    def _fields(self, val: IronPython.Runtime.PythonTuple):
        ...

    @property
    def _attributes(self) -> IronPython.Runtime.PythonTuple:
        ...
    @_attributes.setter
    def _attributes(self, val: IronPython.Runtime.PythonTuple):
        ...

    @property
    def lineno(self) -> int:
        ...
    @lineno.setter
    def lineno(self, val: int):
        ...

    @property
    def col_offset(self) -> int:
        ...
    @col_offset.setter
    def col_offset(self, val: int):
        ...

    # methods
    def __init__(self, ):
        ...

    def Revert(self, ) -> int:
        ...

class Expr(IronPython.Modules._ast.stmt):
    @typing.overload
    def __init__(self, **kwargs):
        self._lineno: System.Nullable[int]
        self._col_offset: System.Nullable[int]
        ...

    # static fields

    # properties
    @property
    def value(self) -> IronPython.Modules._ast.expr:
        ...
    @value.setter
    def value(self, val: IronPython.Modules._ast.expr):
        ...

    @property
    def _fields(self) -> IronPython.Runtime.PythonTuple:
        ...
    @_fields.setter
    def _fields(self, val: IronPython.Runtime.PythonTuple):
        ...

    @property
    def _attributes(self) -> IronPython.Runtime.PythonTuple:
        ...
    @_attributes.setter
    def _attributes(self, val: IronPython.Runtime.PythonTuple):
        ...

    @property
    def lineno(self) -> int:
        ...
    @lineno.setter
    def lineno(self, val: int):
        ...

    @property
    def col_offset(self) -> int:
        ...
    @col_offset.setter
    def col_offset(self, val: int):
        ...

    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def __init__(self, value: IronPython.Modules._ast.expr, lineno: System.Nullable[int], col_offset: System.Nullable[int], ):
        ...

    @typing.overload
    def __init__(self, stmt: IronPython.Compiler.Ast.ExpressionStatement, ):
        ...

    def Revert(self, ) -> IronPython.Compiler.Ast.Statement:
        ...

class Sub(IronPython.Modules._ast.operator):
    @typing.overload
    def __init__(self, **kwargs):
        self._lineno: System.Nullable[int]
        self._col_offset: System.Nullable[int]
        ...

    # static fields
    Instance: IronPython.Modules._ast.Sub = ...

    # properties
    @property
    def _fields(self) -> IronPython.Runtime.PythonTuple:
        ...
    @_fields.setter
    def _fields(self, val: IronPython.Runtime.PythonTuple):
        ...

    @property
    def _attributes(self) -> IronPython.Runtime.PythonTuple:
        ...
    @_attributes.setter
    def _attributes(self, val: IronPython.Runtime.PythonTuple):
        ...

    @property
    def lineno(self) -> int:
        ...
    @lineno.setter
    def lineno(self, val: int):
        ...

    @property
    def col_offset(self) -> int:
        ...
    @col_offset.setter
    def col_offset(self, val: int):
        ...

    # methods
    def __init__(self, ):
        ...

    def Revert(self, ) -> int:
        ...

class Expression(IronPython.Modules._ast.mod):
    @typing.overload
    def __init__(self, **kwargs):
        self._lineno: System.Nullable[int]
        self._col_offset: System.Nullable[int]
        ...

    # static fields

    # properties
    @property
    def body(self) -> IronPython.Modules._ast.expr:
        ...
    @body.setter
    def body(self, val: IronPython.Modules._ast.expr):
        ...

    @property
    def _fields(self) -> IronPython.Runtime.PythonTuple:
        ...
    @_fields.setter
    def _fields(self, val: IronPython.Runtime.PythonTuple):
        ...

    @property
    def _attributes(self) -> IronPython.Runtime.PythonTuple:
        ...
    @_attributes.setter
    def _attributes(self, val: IronPython.Runtime.PythonTuple):
        ...

    @property
    def lineno(self) -> int:
        ...
    @lineno.setter
    def lineno(self, val: int):
        ...

    @property
    def col_offset(self) -> int:
        ...
    @col_offset.setter
    def col_offset(self, val: int):
        ...

    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def __init__(self, body: IronPython.Modules._ast.expr, ):
        ...

    @typing.overload
    def __init__(self, suite: IronPython.Compiler.Ast.SuiteStatement, ):
        ...

    def GetStatements(self, ) -> IronPython.Runtime.PythonList:
        ...

class IsNot(IronPython.Modules._ast.cmpop):
    @typing.overload
    def __init__(self, **kwargs):
        self._lineno: System.Nullable[int]
        self._col_offset: System.Nullable[int]
        ...

    # static fields
    Instance: IronPython.Modules._ast.IsNot = ...

    # properties
    @property
    def _fields(self) -> IronPython.Runtime.PythonTuple:
        ...
    @_fields.setter
    def _fields(self, val: IronPython.Runtime.PythonTuple):
        ...

    @property
    def _attributes(self) -> IronPython.Runtime.PythonTuple:
        ...
    @_attributes.setter
    def _attributes(self, val: IronPython.Runtime.PythonTuple):
        ...

    @property
    def lineno(self) -> int:
        ...
    @lineno.setter
    def lineno(self, val: int):
        ...

    @property
    def col_offset(self) -> int:
        ...
    @col_offset.setter
    def col_offset(self, val: int):
        ...

    # methods
    def __init__(self, ):
        ...

    def Revert(self, ) -> int:
        ...

class Param(IronPython.Modules._ast.expr_context):
    @typing.overload
    def __init__(self, **kwargs):
        self._lineno: System.Nullable[int]
        self._col_offset: System.Nullable[int]
        ...

    # static fields
    Instance: IronPython.Modules._ast.Param = ...

    # properties
    @property
    def _fields(self) -> IronPython.Runtime.PythonTuple:
        ...
    @_fields.setter
    def _fields(self, val: IronPython.Runtime.PythonTuple):
        ...

    @property
    def _attributes(self) -> IronPython.Runtime.PythonTuple:
        ...
    @_attributes.setter
    def _attributes(self, val: IronPython.Runtime.PythonTuple):
        ...

    @property
    def lineno(self) -> int:
        ...
    @lineno.setter
    def lineno(self, val: int):
        ...

    @property
    def col_offset(self) -> int:
        ...
    @col_offset.setter
    def col_offset(self, val: int):
        ...

    # methods
    def __init__(self, ):
        ...

class Bytes(IronPython.Modules._ast.expr):
    @typing.overload
    def __init__(self, **kwargs):
        self._lineno: System.Nullable[int]
        self._col_offset: System.Nullable[int]
        ...

    # static fields

    # properties
    @property
    def s(self) -> IronPython.Runtime.Bytes:
        ...
    @s.setter
    def s(self, val: IronPython.Runtime.Bytes):
        ...

    @property
    def _fields(self) -> IronPython.Runtime.PythonTuple:
        ...
    @_fields.setter
    def _fields(self, val: IronPython.Runtime.PythonTuple):
        ...

    @property
    def _attributes(self) -> IronPython.Runtime.PythonTuple:
        ...
    @_attributes.setter
    def _attributes(self, val: IronPython.Runtime.PythonTuple):
        ...

    @property
    def lineno(self) -> int:
        ...
    @lineno.setter
    def lineno(self, val: int):
        ...

    @property
    def col_offset(self) -> int:
        ...
    @col_offset.setter
    def col_offset(self, val: int):
        ...

    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def __init__(self, s: IronPython.Runtime.Bytes, ):
        ...

    @typing.overload
    def __init__(self, s: IronPython.Runtime.Bytes, lineno: System.Nullable[int], col_offset: System.Nullable[int], ):
        ...

    def Revert(self, ) -> IronPython.Compiler.Ast.Expression:
        ...

class GeneratorExp(IronPython.Modules._ast.expr):
    @typing.overload
    def __init__(self, **kwargs):
        self._lineno: System.Nullable[int]
        self._col_offset: System.Nullable[int]
        ...

    # static fields

    # properties
    @property
    def elt(self) -> IronPython.Modules._ast.expr:
        ...
    @elt.setter
    def elt(self, val: IronPython.Modules._ast.expr):
        ...

    @property
    def generators(self) -> IronPython.Runtime.PythonList:
        ...
    @generators.setter
    def generators(self, val: IronPython.Runtime.PythonList):
        ...

    @property
    def _fields(self) -> IronPython.Runtime.PythonTuple:
        ...
    @_fields.setter
    def _fields(self, val: IronPython.Runtime.PythonTuple):
        ...

    @property
    def _attributes(self) -> IronPython.Runtime.PythonTuple:
        ...
    @_attributes.setter
    def _attributes(self, val: IronPython.Runtime.PythonTuple):
        ...

    @property
    def lineno(self) -> int:
        ...
    @lineno.setter
    def lineno(self, val: int):
        ...

    @property
    def col_offset(self) -> int:
        ...
    @col_offset.setter
    def col_offset(self, val: int):
        ...

    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def __init__(self, elt: IronPython.Modules._ast.expr, generators: IronPython.Runtime.PythonList, lineno: System.Nullable[int], col_offset: System.Nullable[int], ):
        ...

    @typing.overload
    def __init__(self, expr: IronPython.Compiler.Ast.GeneratorExpression, ):
        ...

    def Revert(self, ) -> IronPython.Compiler.Ast.Expression:
        ...

class Subscript(IronPython.Modules._ast.expr):
    @typing.overload
    def __init__(self, **kwargs):
        self._lineno: System.Nullable[int]
        self._col_offset: System.Nullable[int]
        ...

    # static fields

    # properties
    @property
    def value(self) -> IronPython.Modules._ast.expr:
        ...
    @value.setter
    def value(self, val: IronPython.Modules._ast.expr):
        ...

    @property
    def slice(self) -> IronPython.Modules._ast.slice:
        ...
    @slice.setter
    def slice(self, val: IronPython.Modules._ast.slice):
        ...

    @property
    def ctx(self) -> IronPython.Modules._ast.expr_context:
        ...
    @ctx.setter
    def ctx(self, val: IronPython.Modules._ast.expr_context):
        ...

    @property
    def _fields(self) -> IronPython.Runtime.PythonTuple:
        ...
    @_fields.setter
    def _fields(self, val: IronPython.Runtime.PythonTuple):
        ...

    @property
    def _attributes(self) -> IronPython.Runtime.PythonTuple:
        ...
    @_attributes.setter
    def _attributes(self, val: IronPython.Runtime.PythonTuple):
        ...

    @property
    def lineno(self) -> int:
        ...
    @lineno.setter
    def lineno(self, val: int):
        ...

    @property
    def col_offset(self) -> int:
        ...
    @col_offset.setter
    def col_offset(self, val: int):
        ...

    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def __init__(self, value: IronPython.Modules._ast.expr, slice: IronPython.Modules._ast.slice, ctx: IronPython.Modules._ast.expr_context, lineno: System.Nullable[int], col_offset: System.Nullable[int], ):
        ...

    @typing.overload
    def __init__(self, expr: IronPython.Compiler.Ast.IndexExpression, ctx: IronPython.Modules._ast.expr_context, ):
        ...

    def Revert(self, ) -> IronPython.Compiler.Ast.Expression:
        ...

class Or(IronPython.Modules._ast.boolop):
    @typing.overload
    def __init__(self, **kwargs):
        self._lineno: System.Nullable[int]
        self._col_offset: System.Nullable[int]
        ...

    # static fields
    Instance: IronPython.Modules._ast.Or = ...

    # properties
    @property
    def _fields(self) -> IronPython.Runtime.PythonTuple:
        ...
    @_fields.setter
    def _fields(self, val: IronPython.Runtime.PythonTuple):
        ...

    @property
    def _attributes(self) -> IronPython.Runtime.PythonTuple:
        ...
    @_attributes.setter
    def _attributes(self, val: IronPython.Runtime.PythonTuple):
        ...

    @property
    def lineno(self) -> int:
        ...
    @lineno.setter
    def lineno(self, val: int):
        ...

    @property
    def col_offset(self) -> int:
        ...
    @col_offset.setter
    def col_offset(self, val: int):
        ...

    # methods
    def __init__(self, ):
        ...

class FloorDiv(IronPython.Modules._ast.operator):
    @typing.overload
    def __init__(self, **kwargs):
        self._lineno: System.Nullable[int]
        self._col_offset: System.Nullable[int]
        ...

    # static fields
    Instance: IronPython.Modules._ast.FloorDiv = ...

    # properties
    @property
    def _fields(self) -> IronPython.Runtime.PythonTuple:
        ...
    @_fields.setter
    def _fields(self, val: IronPython.Runtime.PythonTuple):
        ...

    @property
    def _attributes(self) -> IronPython.Runtime.PythonTuple:
        ...
    @_attributes.setter
    def _attributes(self, val: IronPython.Runtime.PythonTuple):
        ...

    @property
    def lineno(self) -> int:
        ...
    @lineno.setter
    def lineno(self, val: int):
        ...

    @property
    def col_offset(self) -> int:
        ...
    @col_offset.setter
    def col_offset(self, val: int):
        ...

    # methods
    def __init__(self, ):
        ...

    def Revert(self, ) -> int:
        ...

class Mult(IronPython.Modules._ast.operator):
    @typing.overload
    def __init__(self, **kwargs):
        self._lineno: System.Nullable[int]
        self._col_offset: System.Nullable[int]
        ...

    # static fields
    Instance: IronPython.Modules._ast.Mult = ...

    # properties
    @property
    def _fields(self) -> IronPython.Runtime.PythonTuple:
        ...
    @_fields.setter
    def _fields(self, val: IronPython.Runtime.PythonTuple):
        ...

    @property
    def _attributes(self) -> IronPython.Runtime.PythonTuple:
        ...
    @_attributes.setter
    def _attributes(self, val: IronPython.Runtime.PythonTuple):
        ...

    @property
    def lineno(self) -> int:
        ...
    @lineno.setter
    def lineno(self, val: int):
        ...

    @property
    def col_offset(self) -> int:
        ...
    @col_offset.setter
    def col_offset(self, val: int):
        ...

    # methods
    def __init__(self, ):
        ...

    def Revert(self, ) -> int:
        ...

class Dict(IronPython.Modules._ast.expr):
    @typing.overload
    def __init__(self, **kwargs):
        self._lineno: System.Nullable[int]
        self._col_offset: System.Nullable[int]
        ...

    # static fields

    # properties
    @property
    def keys(self) -> IronPython.Runtime.PythonList:
        ...
    @keys.setter
    def keys(self, val: IronPython.Runtime.PythonList):
        ...

    @property
    def values(self) -> IronPython.Runtime.PythonList:
        ...
    @values.setter
    def values(self, val: IronPython.Runtime.PythonList):
        ...

    @property
    def _fields(self) -> IronPython.Runtime.PythonTuple:
        ...
    @_fields.setter
    def _fields(self, val: IronPython.Runtime.PythonTuple):
        ...

    @property
    def _attributes(self) -> IronPython.Runtime.PythonTuple:
        ...
    @_attributes.setter
    def _attributes(self, val: IronPython.Runtime.PythonTuple):
        ...

    @property
    def lineno(self) -> int:
        ...
    @lineno.setter
    def lineno(self, val: int):
        ...

    @property
    def col_offset(self) -> int:
        ...
    @col_offset.setter
    def col_offset(self, val: int):
        ...

    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def __init__(self, keys: IronPython.Runtime.PythonList, values: IronPython.Runtime.PythonList, lineno: System.Nullable[int], col_offset: System.Nullable[int], ):
        ...

    @typing.overload
    def __init__(self, expr: IronPython.Compiler.Ast.DictionaryExpression, ):
        ...

    def Revert(self, ) -> IronPython.Compiler.Ast.Expression:
        ...

class operator(IronPython.Modules._ast.AST, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        self._lineno: System.Nullable[int]
        self._col_offset: System.Nullable[int]
        ...

    # static fields

    # properties
    @property
    def _fields(self) -> IronPython.Runtime.PythonTuple:
        ...
    @_fields.setter
    def _fields(self, val: IronPython.Runtime.PythonTuple):
        ...

    @property
    def _attributes(self) -> IronPython.Runtime.PythonTuple:
        ...
    @_attributes.setter
    def _attributes(self, val: IronPython.Runtime.PythonTuple):
        ...

    @property
    def lineno(self) -> int:
        ...
    @lineno.setter
    def lineno(self, val: int):
        ...

    @property
    def col_offset(self) -> int:
        ...
    @col_offset.setter
    def col_offset(self, val: int):
        ...

    # methods
    def __init__(self, ):
        ...

    @abc.abstractmethod
    def Revert(self, ) -> int:
        ...

class slice(IronPython.Modules._ast.AST, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        self._lineno: System.Nullable[int]
        self._col_offset: System.Nullable[int]
        ...

    # static fields

    # properties
    @property
    def _fields(self) -> IronPython.Runtime.PythonTuple:
        ...
    @_fields.setter
    def _fields(self, val: IronPython.Runtime.PythonTuple):
        ...

    @property
    def _attributes(self) -> IronPython.Runtime.PythonTuple:
        ...
    @_attributes.setter
    def _attributes(self, val: IronPython.Runtime.PythonTuple):
        ...

    @property
    def lineno(self) -> int:
        ...
    @lineno.setter
    def lineno(self, val: int):
        ...

    @property
    def col_offset(self) -> int:
        ...
    @col_offset.setter
    def col_offset(self, val: int):
        ...

    # methods
    def __init__(self, ):
        ...

class Invert(IronPython.Modules._ast.unaryop):
    @typing.overload
    def __init__(self, **kwargs):
        self._lineno: System.Nullable[int]
        self._col_offset: System.Nullable[int]
        ...

    # static fields
    Instance: IronPython.Modules._ast.Invert = ...

    # properties
    @property
    def _fields(self) -> IronPython.Runtime.PythonTuple:
        ...
    @_fields.setter
    def _fields(self, val: IronPython.Runtime.PythonTuple):
        ...

    @property
    def _attributes(self) -> IronPython.Runtime.PythonTuple:
        ...
    @_attributes.setter
    def _attributes(self, val: IronPython.Runtime.PythonTuple):
        ...

    @property
    def lineno(self) -> int:
        ...
    @lineno.setter
    def lineno(self, val: int):
        ...

    @property
    def col_offset(self) -> int:
        ...
    @col_offset.setter
    def col_offset(self, val: int):
        ...

    # methods
    def __init__(self, ):
        ...

    def Revert(self, ) -> int:
        ...

class ThrowingErrorSink(Microsoft.Scripting.ErrorSink):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields
    Default: IronPython.Modules._ast.ThrowingErrorSink = ...

    # properties
    # methods
    def __init__(self, ):
        ...

    def Add(self, sourceUnit: Microsoft.Scripting.SourceUnit, message: str, span: Microsoft.Scripting.SourceSpan, errorCode: int, severity: int, ) -> None:
        ...

class Starred(IronPython.Modules._ast.expr):
    @typing.overload
    def __init__(self, **kwargs):
        self._lineno: System.Nullable[int]
        self._col_offset: System.Nullable[int]
        ...

    # static fields

    # properties
    @property
    def ctx(self) -> IronPython.Modules._ast.expr_context:
        ...
    @ctx.setter
    def ctx(self, val: IronPython.Modules._ast.expr_context):
        ...

    @property
    def value(self) -> IronPython.Modules._ast.expr:
        ...
    @value.setter
    def value(self, val: IronPython.Modules._ast.expr):
        ...

    @property
    def _fields(self) -> IronPython.Runtime.PythonTuple:
        ...
    @_fields.setter
    def _fields(self, val: IronPython.Runtime.PythonTuple):
        ...

    @property
    def _attributes(self) -> IronPython.Runtime.PythonTuple:
        ...
    @_attributes.setter
    def _attributes(self, val: IronPython.Runtime.PythonTuple):
        ...

    @property
    def lineno(self) -> int:
        ...
    @lineno.setter
    def lineno(self, val: int):
        ...

    @property
    def col_offset(self) -> int:
        ...
    @col_offset.setter
    def col_offset(self, val: int):
        ...

    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def __init__(self, value: IronPython.Modules._ast.expr, ctx: IronPython.Modules._ast.expr_context, lineno: System.Nullable[int], col_offset: System.Nullable[int], ):
        ...

    @typing.overload
    def __init__(self, value: IronPython.Modules._ast.expr, ctx: IronPython.Modules._ast.expr_context, ):
        ...

    @typing.overload
    def __init__(self, expr: IronPython.Compiler.Ast.StarredExpression, ctx: IronPython.Modules._ast.expr_context, ):
        ...

    def Revert(self, ) -> IronPython.Compiler.Ast.Expression:
        ...

class Import(IronPython.Modules._ast.stmt):
    @typing.overload
    def __init__(self, **kwargs):
        self._lineno: System.Nullable[int]
        self._col_offset: System.Nullable[int]
        ...

    # static fields

    # properties
    @property
    def names(self) -> IronPython.Runtime.PythonList:
        ...
    @names.setter
    def names(self, val: IronPython.Runtime.PythonList):
        ...

    @property
    def _fields(self) -> IronPython.Runtime.PythonTuple:
        ...
    @_fields.setter
    def _fields(self, val: IronPython.Runtime.PythonTuple):
        ...

    @property
    def _attributes(self) -> IronPython.Runtime.PythonTuple:
        ...
    @_attributes.setter
    def _attributes(self, val: IronPython.Runtime.PythonTuple):
        ...

    @property
    def lineno(self) -> int:
        ...
    @lineno.setter
    def lineno(self, val: int):
        ...

    @property
    def col_offset(self) -> int:
        ...
    @col_offset.setter
    def col_offset(self, val: int):
        ...

    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def __init__(self, names: IronPython.Runtime.PythonList, lineno: System.Nullable[int], col_offset: System.Nullable[int], ):
        ...

    @typing.overload
    def __init__(self, stmt: IronPython.Compiler.Ast.ImportStatement, ):
        ...

    def Revert(self, ) -> IronPython.Compiler.Ast.Statement:
        ...

class Try(IronPython.Modules._ast.stmt):
    @typing.overload
    def __init__(self, **kwargs):
        self._lineno: System.Nullable[int]
        self._col_offset: System.Nullable[int]
        ...

    # static fields

    # properties
    @property
    def body(self) -> IronPython.Runtime.PythonList:
        ...
    @body.setter
    def body(self, val: IronPython.Runtime.PythonList):
        ...

    @property
    def handlers(self) -> IronPython.Runtime.PythonList:
        ...
    @handlers.setter
    def handlers(self, val: IronPython.Runtime.PythonList):
        ...

    @property
    def orelse(self) -> IronPython.Runtime.PythonList:
        ...
    @orelse.setter
    def orelse(self, val: IronPython.Runtime.PythonList):
        ...

    @property
    def finalbody(self) -> IronPython.Runtime.PythonList:
        ...
    @finalbody.setter
    def finalbody(self, val: IronPython.Runtime.PythonList):
        ...

    @property
    def _fields(self) -> IronPython.Runtime.PythonTuple:
        ...
    @_fields.setter
    def _fields(self, val: IronPython.Runtime.PythonTuple):
        ...

    @property
    def _attributes(self) -> IronPython.Runtime.PythonTuple:
        ...
    @_attributes.setter
    def _attributes(self, val: IronPython.Runtime.PythonTuple):
        ...

    @property
    def lineno(self) -> int:
        ...
    @lineno.setter
    def lineno(self, val: int):
        ...

    @property
    def col_offset(self) -> int:
        ...
    @col_offset.setter
    def col_offset(self, val: int):
        ...

    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def __init__(self, body: IronPython.Runtime.PythonList, handlers: IronPython.Runtime.PythonList, orelse: IronPython.Runtime.PythonList, finalbody: IronPython.Runtime.PythonList, lineno: System.Nullable[int], col_offset: System.Nullable[int], ):
        ...

    @typing.overload
    def __init__(self, stmt: IronPython.Compiler.Ast.TryStatement, ):
        ...

    def Revert(self, ) -> IronPython.Compiler.Ast.Statement:
        ...

class JoinedStr(IronPython.Modules._ast.expr):
    @typing.overload
    def __init__(self, **kwargs):
        self._lineno: System.Nullable[int]
        self._col_offset: System.Nullable[int]
        ...

    # static fields

    # properties
    @property
    def values(self) -> IronPython.Runtime.PythonList:
        ...
    @values.setter
    def values(self, val: IronPython.Runtime.PythonList):
        ...

    @property
    def _fields(self) -> IronPython.Runtime.PythonTuple:
        ...
    @_fields.setter
    def _fields(self, val: IronPython.Runtime.PythonTuple):
        ...

    @property
    def _attributes(self) -> IronPython.Runtime.PythonTuple:
        ...
    @_attributes.setter
    def _attributes(self, val: IronPython.Runtime.PythonTuple):
        ...

    @property
    def lineno(self) -> int:
        ...
    @lineno.setter
    def lineno(self, val: int):
        ...

    @property
    def col_offset(self) -> int:
        ...
    @col_offset.setter
    def col_offset(self, val: int):
        ...

    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def __init__(self, values: IronPython.Runtime.PythonList, lineno: System.Nullable[int], col_offset: System.Nullable[int], ):
        ...

    @typing.overload
    def __init__(self, expr: IronPython.Compiler.Ast.JoinedStringExpression, ):
        ...

    def Revert(self, ) -> IronPython.Compiler.Ast.Expression:
        ...

class Module(IronPython.Modules._ast.mod):
    @typing.overload
    def __init__(self, **kwargs):
        self._lineno: System.Nullable[int]
        self._col_offset: System.Nullable[int]
        ...

    # static fields

    # properties
    @property
    def body(self) -> IronPython.Runtime.PythonList:
        ...
    @body.setter
    def body(self, val: IronPython.Runtime.PythonList):
        ...

    @property
    def _fields(self) -> IronPython.Runtime.PythonTuple:
        ...
    @_fields.setter
    def _fields(self, val: IronPython.Runtime.PythonTuple):
        ...

    @property
    def _attributes(self) -> IronPython.Runtime.PythonTuple:
        ...
    @_attributes.setter
    def _attributes(self, val: IronPython.Runtime.PythonTuple):
        ...

    @property
    def lineno(self) -> int:
        ...
    @lineno.setter
    def lineno(self, val: int):
        ...

    @property
    def col_offset(self) -> int:
        ...
    @col_offset.setter
    def col_offset(self, val: int):
        ...

    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def __init__(self, body: IronPython.Runtime.PythonList, ):
        ...

    @typing.overload
    def __init__(self, suite: IronPython.Compiler.Ast.SuiteStatement, ):
        ...

    def GetStatements(self, ) -> IronPython.Runtime.PythonList:
        ...

class UAdd(IronPython.Modules._ast.unaryop):
    @typing.overload
    def __init__(self, **kwargs):
        self._lineno: System.Nullable[int]
        self._col_offset: System.Nullable[int]
        ...

    # static fields
    Instance: IronPython.Modules._ast.UAdd = ...

    # properties
    @property
    def _fields(self) -> IronPython.Runtime.PythonTuple:
        ...
    @_fields.setter
    def _fields(self, val: IronPython.Runtime.PythonTuple):
        ...

    @property
    def _attributes(self) -> IronPython.Runtime.PythonTuple:
        ...
    @_attributes.setter
    def _attributes(self, val: IronPython.Runtime.PythonTuple):
        ...

    @property
    def lineno(self) -> int:
        ...
    @lineno.setter
    def lineno(self, val: int):
        ...

    @property
    def col_offset(self) -> int:
        ...
    @col_offset.setter
    def col_offset(self, val: int):
        ...

    # methods
    def __init__(self, ):
        ...

    def Revert(self, ) -> int:
        ...

class expr_context(IronPython.Modules._ast.AST, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        self._lineno: System.Nullable[int]
        self._col_offset: System.Nullable[int]
        ...

    # static fields

    # properties
    @property
    def _fields(self) -> IronPython.Runtime.PythonTuple:
        ...
    @_fields.setter
    def _fields(self, val: IronPython.Runtime.PythonTuple):
        ...

    @property
    def _attributes(self) -> IronPython.Runtime.PythonTuple:
        ...
    @_attributes.setter
    def _attributes(self, val: IronPython.Runtime.PythonTuple):
        ...

    @property
    def lineno(self) -> int:
        ...
    @lineno.setter
    def lineno(self, val: int):
        ...

    @property
    def col_offset(self) -> int:
        ...
    @col_offset.setter
    def col_offset(self, val: int):
        ...

    # methods
    def __init__(self, ):
        ...

class Yield(IronPython.Modules._ast.expr):
    @typing.overload
    def __init__(self, **kwargs):
        self._lineno: System.Nullable[int]
        self._col_offset: System.Nullable[int]
        ...

    # static fields

    # properties
    @property
    def value(self) -> IronPython.Modules._ast.expr:
        ...
    @value.setter
    def value(self, val: IronPython.Modules._ast.expr):
        ...

    @property
    def _fields(self) -> IronPython.Runtime.PythonTuple:
        ...
    @_fields.setter
    def _fields(self, val: IronPython.Runtime.PythonTuple):
        ...

    @property
    def _attributes(self) -> IronPython.Runtime.PythonTuple:
        ...
    @_attributes.setter
    def _attributes(self, val: IronPython.Runtime.PythonTuple):
        ...

    @property
    def lineno(self) -> int:
        ...
    @lineno.setter
    def lineno(self, val: int):
        ...

    @property
    def col_offset(self) -> int:
        ...
    @col_offset.setter
    def col_offset(self, val: int):
        ...

    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def __init__(self, value: IronPython.Modules._ast.expr, lineno: System.Nullable[int], col_offset: System.Nullable[int], ):
        ...

    @typing.overload
    def __init__(self, expr: IronPython.Compiler.Ast.YieldExpression, ):
        ...

    def Revert(self, ) -> IronPython.Compiler.Ast.Expression:
        ...

class AugStore(IronPython.Modules._ast.expr_context):
    @typing.overload
    def __init__(self, **kwargs):
        self._lineno: System.Nullable[int]
        self._col_offset: System.Nullable[int]
        ...

    # static fields

    # properties
    @property
    def _fields(self) -> IronPython.Runtime.PythonTuple:
        ...
    @_fields.setter
    def _fields(self, val: IronPython.Runtime.PythonTuple):
        ...

    @property
    def _attributes(self) -> IronPython.Runtime.PythonTuple:
        ...
    @_attributes.setter
    def _attributes(self, val: IronPython.Runtime.PythonTuple):
        ...

    @property
    def lineno(self) -> int:
        ...
    @lineno.setter
    def lineno(self, val: int):
        ...

    @property
    def col_offset(self) -> int:
        ...
    @col_offset.setter
    def col_offset(self, val: int):
        ...

    # methods
    def __init__(self, ):
        ...

class Index(IronPython.Modules._ast.slice):
    @typing.overload
    def __init__(self, **kwargs):
        self._lineno: System.Nullable[int]
        self._col_offset: System.Nullable[int]
        ...

    # static fields

    # properties
    @property
    def value(self) -> IronPython.Modules._ast.expr:
        ...
    @value.setter
    def value(self, val: IronPython.Modules._ast.expr):
        ...

    @property
    def _fields(self) -> IronPython.Runtime.PythonTuple:
        ...
    @_fields.setter
    def _fields(self, val: IronPython.Runtime.PythonTuple):
        ...

    @property
    def _attributes(self) -> IronPython.Runtime.PythonTuple:
        ...
    @_attributes.setter
    def _attributes(self, val: IronPython.Runtime.PythonTuple):
        ...

    @property
    def lineno(self) -> int:
        ...
    @lineno.setter
    def lineno(self, val: int):
        ...

    @property
    def col_offset(self) -> int:
        ...
    @col_offset.setter
    def col_offset(self, val: int):
        ...

    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def __init__(self, value: IronPython.Modules._ast.expr, ):
        ...

class YieldFrom(IronPython.Modules._ast.expr):
    @typing.overload
    def __init__(self, **kwargs):
        self._lineno: System.Nullable[int]
        self._col_offset: System.Nullable[int]
        ...

    # static fields

    # properties
    @property
    def value(self) -> IronPython.Modules._ast.expr:
        ...
    @value.setter
    def value(self, val: IronPython.Modules._ast.expr):
        ...

    @property
    def _fields(self) -> IronPython.Runtime.PythonTuple:
        ...
    @_fields.setter
    def _fields(self, val: IronPython.Runtime.PythonTuple):
        ...

    @property
    def _attributes(self) -> IronPython.Runtime.PythonTuple:
        ...
    @_attributes.setter
    def _attributes(self, val: IronPython.Runtime.PythonTuple):
        ...

    @property
    def lineno(self) -> int:
        ...
    @lineno.setter
    def lineno(self, val: int):
        ...

    @property
    def col_offset(self) -> int:
        ...
    @col_offset.setter
    def col_offset(self, val: int):
        ...

    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def __init__(self, value: IronPython.Modules._ast.expr, lineno: System.Nullable[int], col_offset: System.Nullable[int], ):
        ...

    @typing.overload
    def __init__(self, expr: IronPython.Compiler.Ast.YieldFromExpression, ):
        ...

    def Revert(self, ) -> IronPython.Compiler.Ast.Expression:
        ...

class Assert(IronPython.Modules._ast.stmt):
    @typing.overload
    def __init__(self, **kwargs):
        self._lineno: System.Nullable[int]
        self._col_offset: System.Nullable[int]
        ...

    # static fields

    # properties
    @property
    def test(self) -> IronPython.Modules._ast.expr:
        ...
    @test.setter
    def test(self, val: IronPython.Modules._ast.expr):
        ...

    @property
    def msg(self) -> IronPython.Modules._ast.expr:
        ...
    @msg.setter
    def msg(self, val: IronPython.Modules._ast.expr):
        ...

    @property
    def _fields(self) -> IronPython.Runtime.PythonTuple:
        ...
    @_fields.setter
    def _fields(self, val: IronPython.Runtime.PythonTuple):
        ...

    @property
    def _attributes(self) -> IronPython.Runtime.PythonTuple:
        ...
    @_attributes.setter
    def _attributes(self, val: IronPython.Runtime.PythonTuple):
        ...

    @property
    def lineno(self) -> int:
        ...
    @lineno.setter
    def lineno(self, val: int):
        ...

    @property
    def col_offset(self) -> int:
        ...
    @col_offset.setter
    def col_offset(self, val: int):
        ...

    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def __init__(self, test: IronPython.Modules._ast.expr, msg: IronPython.Modules._ast.expr, lineno: System.Nullable[int], col_offset: System.Nullable[int], ):
        ...

    @typing.overload
    def __init__(self, stmt: IronPython.Compiler.Ast.AssertStatement, ):
        ...

    def Revert(self, ) -> IronPython.Compiler.Ast.Statement:
        ...

class ImportFrom(IronPython.Modules._ast.stmt):
    @typing.overload
    def __init__(self, **kwargs):
        self._lineno: System.Nullable[int]
        self._col_offset: System.Nullable[int]
        ...

    # static fields

    # properties
    @property
    def module(self) -> str:
        ...
    @module.setter
    def module(self, val: str):
        ...

    @property
    def names(self) -> IronPython.Runtime.PythonList:
        ...
    @names.setter
    def names(self, val: IronPython.Runtime.PythonList):
        ...

    @property
    def level(self) -> int:
        ...
    @level.setter
    def level(self, val: int):
        ...

    @property
    def _fields(self) -> IronPython.Runtime.PythonTuple:
        ...
    @_fields.setter
    def _fields(self, val: IronPython.Runtime.PythonTuple):
        ...

    @property
    def _attributes(self) -> IronPython.Runtime.PythonTuple:
        ...
    @_attributes.setter
    def _attributes(self, val: IronPython.Runtime.PythonTuple):
        ...

    @property
    def lineno(self) -> int:
        ...
    @lineno.setter
    def lineno(self, val: int):
        ...

    @property
    def col_offset(self) -> int:
        ...
    @col_offset.setter
    def col_offset(self, val: int):
        ...

    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def __init__(self, module: str, names: IronPython.Runtime.PythonList, level: int, lineno: System.Nullable[int], col_offset: System.Nullable[int], ):
        ...

    @typing.overload
    def __init__(self, stmt: IronPython.Compiler.Ast.FromImportStatement, ):
        ...

    def Revert(self, ) -> IronPython.Compiler.Ast.Statement:
        ...

class Nonlocal(IronPython.Modules._ast.stmt):
    @typing.overload
    def __init__(self, **kwargs):
        self._lineno: System.Nullable[int]
        self._col_offset: System.Nullable[int]
        ...

    # static fields

    # properties
    @property
    def names(self) -> IronPython.Runtime.PythonList:
        ...
    @names.setter
    def names(self, val: IronPython.Runtime.PythonList):
        ...

    @property
    def _fields(self) -> IronPython.Runtime.PythonTuple:
        ...
    @_fields.setter
    def _fields(self, val: IronPython.Runtime.PythonTuple):
        ...

    @property
    def _attributes(self) -> IronPython.Runtime.PythonTuple:
        ...
    @_attributes.setter
    def _attributes(self, val: IronPython.Runtime.PythonTuple):
        ...

    @property
    def lineno(self) -> int:
        ...
    @lineno.setter
    def lineno(self, val: int):
        ...

    @property
    def col_offset(self) -> int:
        ...
    @col_offset.setter
    def col_offset(self, val: int):
        ...

    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def __init__(self, names: IronPython.Runtime.PythonList, lineno: System.Nullable[int], col_offset: System.Nullable[int], ):
        ...

    @typing.overload
    def __init__(self, stmt: IronPython.Compiler.Ast.NonlocalStatement, ):
        ...

    def Revert(self, ) -> IronPython.Compiler.Ast.Statement:
        ...

class mod(IronPython.Modules._ast.AST, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        self._lineno: System.Nullable[int]
        self._col_offset: System.Nullable[int]
        ...

    # static fields

    # properties
    @property
    def _fields(self) -> IronPython.Runtime.PythonTuple:
        ...
    @_fields.setter
    def _fields(self, val: IronPython.Runtime.PythonTuple):
        ...

    @property
    def _attributes(self) -> IronPython.Runtime.PythonTuple:
        ...
    @_attributes.setter
    def _attributes(self, val: IronPython.Runtime.PythonTuple):
        ...

    @property
    def lineno(self) -> int:
        ...
    @lineno.setter
    def lineno(self, val: int):
        ...

    @property
    def col_offset(self) -> int:
        ...
    @col_offset.setter
    def col_offset(self, val: int):
        ...

    # methods
    def __init__(self, ):
        ...

    @abc.abstractmethod
    def GetStatements(self, ) -> IronPython.Runtime.PythonList:
        ...

class Pow(IronPython.Modules._ast.operator):
    @typing.overload
    def __init__(self, **kwargs):
        self._lineno: System.Nullable[int]
        self._col_offset: System.Nullable[int]
        ...

    # static fields
    Instance: IronPython.Modules._ast.Pow = ...

    # properties
    @property
    def _fields(self) -> IronPython.Runtime.PythonTuple:
        ...
    @_fields.setter
    def _fields(self, val: IronPython.Runtime.PythonTuple):
        ...

    @property
    def _attributes(self) -> IronPython.Runtime.PythonTuple:
        ...
    @_attributes.setter
    def _attributes(self, val: IronPython.Runtime.PythonTuple):
        ...

    @property
    def lineno(self) -> int:
        ...
    @lineno.setter
    def lineno(self, val: int):
        ...

    @property
    def col_offset(self) -> int:
        ...
    @col_offset.setter
    def col_offset(self, val: int):
        ...

    # methods
    def __init__(self, ):
        ...

    def Revert(self, ) -> int:
        ...

class Lt(IronPython.Modules._ast.cmpop):
    @typing.overload
    def __init__(self, **kwargs):
        self._lineno: System.Nullable[int]
        self._col_offset: System.Nullable[int]
        ...

    # static fields
    Instance: IronPython.Modules._ast.Lt = ...

    # properties
    @property
    def _fields(self) -> IronPython.Runtime.PythonTuple:
        ...
    @_fields.setter
    def _fields(self, val: IronPython.Runtime.PythonTuple):
        ...

    @property
    def _attributes(self) -> IronPython.Runtime.PythonTuple:
        ...
    @_attributes.setter
    def _attributes(self, val: IronPython.Runtime.PythonTuple):
        ...

    @property
    def lineno(self) -> int:
        ...
    @lineno.setter
    def lineno(self, val: int):
        ...

    @property
    def col_offset(self) -> int:
        ...
    @col_offset.setter
    def col_offset(self, val: int):
        ...

    # methods
    def __init__(self, ):
        ...

    def Revert(self, ) -> int:
        ...

class Continue(IronPython.Modules._ast.stmt):
    @typing.overload
    def __init__(self, **kwargs):
        self._lineno: System.Nullable[int]
        self._col_offset: System.Nullable[int]
        ...

    # static fields
    Instance: IronPython.Modules._ast.Continue = ...

    # properties
    @property
    def _fields(self) -> IronPython.Runtime.PythonTuple:
        ...
    @_fields.setter
    def _fields(self, val: IronPython.Runtime.PythonTuple):
        ...

    @property
    def _attributes(self) -> IronPython.Runtime.PythonTuple:
        ...
    @_attributes.setter
    def _attributes(self, val: IronPython.Runtime.PythonTuple):
        ...

    @property
    def lineno(self) -> int:
        ...
    @lineno.setter
    def lineno(self, val: int):
        ...

    @property
    def col_offset(self) -> int:
        ...
    @col_offset.setter
    def col_offset(self, val: int):
        ...

    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def __init__(self, lineno: System.Nullable[int], col_offset: System.Nullable[int], ):
        ...

    def Revert(self, ) -> IronPython.Compiler.Ast.Statement:
        ...

class Interactive(IronPython.Modules._ast.mod):
    @typing.overload
    def __init__(self, **kwargs):
        self._lineno: System.Nullable[int]
        self._col_offset: System.Nullable[int]
        ...

    # static fields

    # properties
    @property
    def body(self) -> IronPython.Runtime.PythonList:
        ...
    @body.setter
    def body(self, val: IronPython.Runtime.PythonList):
        ...

    @property
    def _fields(self) -> IronPython.Runtime.PythonTuple:
        ...
    @_fields.setter
    def _fields(self, val: IronPython.Runtime.PythonTuple):
        ...

    @property
    def _attributes(self) -> IronPython.Runtime.PythonTuple:
        ...
    @_attributes.setter
    def _attributes(self, val: IronPython.Runtime.PythonTuple):
        ...

    @property
    def lineno(self) -> int:
        ...
    @lineno.setter
    def lineno(self, val: int):
        ...

    @property
    def col_offset(self) -> int:
        ...
    @col_offset.setter
    def col_offset(self, val: int):
        ...

    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def __init__(self, body: IronPython.Runtime.PythonList, ):
        ...

    @typing.overload
    def __init__(self, suite: IronPython.Compiler.Ast.SuiteStatement, ):
        ...

    def GetStatements(self, ) -> IronPython.Runtime.PythonList:
        ...

class ListComp(IronPython.Modules._ast.expr):
    @typing.overload
    def __init__(self, **kwargs):
        self._lineno: System.Nullable[int]
        self._col_offset: System.Nullable[int]
        ...

    # static fields

    # properties
    @property
    def elt(self) -> IronPython.Modules._ast.expr:
        ...
    @elt.setter
    def elt(self, val: IronPython.Modules._ast.expr):
        ...

    @property
    def generators(self) -> IronPython.Runtime.PythonList:
        ...
    @generators.setter
    def generators(self, val: IronPython.Runtime.PythonList):
        ...

    @property
    def _fields(self) -> IronPython.Runtime.PythonTuple:
        ...
    @_fields.setter
    def _fields(self, val: IronPython.Runtime.PythonTuple):
        ...

    @property
    def _attributes(self) -> IronPython.Runtime.PythonTuple:
        ...
    @_attributes.setter
    def _attributes(self, val: IronPython.Runtime.PythonTuple):
        ...

    @property
    def lineno(self) -> int:
        ...
    @lineno.setter
    def lineno(self, val: int):
        ...

    @property
    def col_offset(self) -> int:
        ...
    @col_offset.setter
    def col_offset(self, val: int):
        ...

    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def __init__(self, elt: IronPython.Modules._ast.expr, generators: IronPython.Runtime.PythonList, lineno: System.Nullable[int], col_offset: System.Nullable[int], ):
        ...

    @typing.overload
    def __init__(self, comp: IronPython.Compiler.Ast.ListComprehension, ):
        ...

    def Revert(self, ) -> IronPython.Compiler.Ast.Expression:
        ...

class BoolOp(IronPython.Modules._ast.expr):
    @typing.overload
    def __init__(self, **kwargs):
        self._lineno: System.Nullable[int]
        self._col_offset: System.Nullable[int]
        ...

    # static fields

    # properties
    @property
    def op(self) -> IronPython.Modules._ast.boolop:
        ...
    @op.setter
    def op(self, val: IronPython.Modules._ast.boolop):
        ...

    @property
    def values(self) -> IronPython.Runtime.PythonList:
        ...
    @values.setter
    def values(self, val: IronPython.Runtime.PythonList):
        ...

    @property
    def _fields(self) -> IronPython.Runtime.PythonTuple:
        ...
    @_fields.setter
    def _fields(self, val: IronPython.Runtime.PythonTuple):
        ...

    @property
    def _attributes(self) -> IronPython.Runtime.PythonTuple:
        ...
    @_attributes.setter
    def _attributes(self, val: IronPython.Runtime.PythonTuple):
        ...

    @property
    def lineno(self) -> int:
        ...
    @lineno.setter
    def lineno(self, val: int):
        ...

    @property
    def col_offset(self) -> int:
        ...
    @col_offset.setter
    def col_offset(self, val: int):
        ...

    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def __init__(self, op: IronPython.Modules._ast.boolop, values: IronPython.Runtime.PythonList, lineno: System.Nullable[int], col_offset: System.Nullable[int], ):
        ...

    @typing.overload
    def __init__(self, and: IronPython.Compiler.Ast.AndExpression, ):
        ...

    @typing.overload
    def __init__(self, or: IronPython.Compiler.Ast.OrExpression, ):
        ...

    def Revert(self, ) -> IronPython.Compiler.Ast.Expression:
        ...

class Store(IronPython.Modules._ast.expr_context):
    @typing.overload
    def __init__(self, **kwargs):
        self._lineno: System.Nullable[int]
        self._col_offset: System.Nullable[int]
        ...

    # static fields
    Instance: IronPython.Modules._ast.Store = ...

    # properties
    @property
    def _fields(self) -> IronPython.Runtime.PythonTuple:
        ...
    @_fields.setter
    def _fields(self, val: IronPython.Runtime.PythonTuple):
        ...

    @property
    def _attributes(self) -> IronPython.Runtime.PythonTuple:
        ...
    @_attributes.setter
    def _attributes(self, val: IronPython.Runtime.PythonTuple):
        ...

    @property
    def lineno(self) -> int:
        ...
    @lineno.setter
    def lineno(self, val: int):
        ...

    @property
    def col_offset(self) -> int:
        ...
    @col_offset.setter
    def col_offset(self, val: int):
        ...

    # methods
    def __init__(self, ):
        ...

class LtE(IronPython.Modules._ast.cmpop):
    @typing.overload
    def __init__(self, **kwargs):
        self._lineno: System.Nullable[int]
        self._col_offset: System.Nullable[int]
        ...

    # static fields
    Instance: IronPython.Modules._ast.LtE = ...

    # properties
    @property
    def _fields(self) -> IronPython.Runtime.PythonTuple:
        ...
    @_fields.setter
    def _fields(self, val: IronPython.Runtime.PythonTuple):
        ...

    @property
    def _attributes(self) -> IronPython.Runtime.PythonTuple:
        ...
    @_attributes.setter
    def _attributes(self, val: IronPython.Runtime.PythonTuple):
        ...

    @property
    def lineno(self) -> int:
        ...
    @lineno.setter
    def lineno(self, val: int):
        ...

    @property
    def col_offset(self) -> int:
        ...
    @col_offset.setter
    def col_offset(self, val: int):
        ...

    # methods
    def __init__(self, ):
        ...

    def Revert(self, ) -> int:
        ...

class SetComp(IronPython.Modules._ast.expr):
    @typing.overload
    def __init__(self, **kwargs):
        self._lineno: System.Nullable[int]
        self._col_offset: System.Nullable[int]
        ...

    # static fields

    # properties
    @property
    def elt(self) -> IronPython.Modules._ast.expr:
        ...
    @elt.setter
    def elt(self, val: IronPython.Modules._ast.expr):
        ...

    @property
    def generators(self) -> IronPython.Runtime.PythonList:
        ...
    @generators.setter
    def generators(self, val: IronPython.Runtime.PythonList):
        ...

    @property
    def _fields(self) -> IronPython.Runtime.PythonTuple:
        ...
    @_fields.setter
    def _fields(self, val: IronPython.Runtime.PythonTuple):
        ...

    @property
    def _attributes(self) -> IronPython.Runtime.PythonTuple:
        ...
    @_attributes.setter
    def _attributes(self, val: IronPython.Runtime.PythonTuple):
        ...

    @property
    def lineno(self) -> int:
        ...
    @lineno.setter
    def lineno(self, val: int):
        ...

    @property
    def col_offset(self) -> int:
        ...
    @col_offset.setter
    def col_offset(self, val: int):
        ...

    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def __init__(self, elt: IronPython.Modules._ast.expr, generators: IronPython.Runtime.PythonList, lineno: System.Nullable[int], col_offset: System.Nullable[int], ):
        ...

    @typing.overload
    def __init__(self, comp: IronPython.Compiler.Ast.SetComprehension, ):
        ...

    def Revert(self, ) -> IronPython.Compiler.Ast.Expression:
        ...

class In(IronPython.Modules._ast.cmpop):
    @typing.overload
    def __init__(self, **kwargs):
        self._lineno: System.Nullable[int]
        self._col_offset: System.Nullable[int]
        ...

    # static fields
    Instance: IronPython.Modules._ast.In = ...

    # properties
    @property
    def _fields(self) -> IronPython.Runtime.PythonTuple:
        ...
    @_fields.setter
    def _fields(self, val: IronPython.Runtime.PythonTuple):
        ...

    @property
    def _attributes(self) -> IronPython.Runtime.PythonTuple:
        ...
    @_attributes.setter
    def _attributes(self, val: IronPython.Runtime.PythonTuple):
        ...

    @property
    def lineno(self) -> int:
        ...
    @lineno.setter
    def lineno(self, val: int):
        ...

    @property
    def col_offset(self) -> int:
        ...
    @col_offset.setter
    def col_offset(self, val: int):
        ...

    # methods
    def __init__(self, ):
        ...

    def Revert(self, ) -> int:
        ...

class ClassDef(IronPython.Modules._ast.stmt):
    @typing.overload
    def __init__(self, **kwargs):
        self._lineno: System.Nullable[int]
        self._col_offset: System.Nullable[int]
        ...

    # static fields

    # properties
    @property
    def name(self) -> str:
        ...
    @name.setter
    def name(self, val: str):
        ...

    @property
    def bases(self) -> IronPython.Runtime.PythonList:
        ...
    @bases.setter
    def bases(self, val: IronPython.Runtime.PythonList):
        ...

    @property
    def keywords(self) -> IronPython.Runtime.PythonList:
        ...
    @keywords.setter
    def keywords(self, val: IronPython.Runtime.PythonList):
        ...

    @property
    def body(self) -> IronPython.Runtime.PythonList:
        ...
    @body.setter
    def body(self, val: IronPython.Runtime.PythonList):
        ...

    @property
    def decorator_list(self) -> IronPython.Runtime.PythonList:
        ...
    @decorator_list.setter
    def decorator_list(self, val: IronPython.Runtime.PythonList):
        ...

    @property
    def _fields(self) -> IronPython.Runtime.PythonTuple:
        ...
    @_fields.setter
    def _fields(self, val: IronPython.Runtime.PythonTuple):
        ...

    @property
    def _attributes(self) -> IronPython.Runtime.PythonTuple:
        ...
    @_attributes.setter
    def _attributes(self, val: IronPython.Runtime.PythonTuple):
        ...

    @property
    def lineno(self) -> int:
        ...
    @lineno.setter
    def lineno(self, val: int):
        ...

    @property
    def col_offset(self) -> int:
        ...
    @col_offset.setter
    def col_offset(self, val: int):
        ...

    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def __init__(self, name: str, bases: IronPython.Runtime.PythonList, keywords: IronPython.Runtime.PythonList, body: IronPython.Runtime.PythonList, decorator_list: IronPython.Runtime.PythonList, lineno: System.Nullable[int], col_offset: System.Nullable[int], ):
        ...

    @typing.overload
    def __init__(self, def: IronPython.Compiler.Ast.ClassDefinition, ):
        ...

    def Revert(self, ) -> IronPython.Compiler.Ast.Statement:
        ...

class And(IronPython.Modules._ast.boolop):
    @typing.overload
    def __init__(self, **kwargs):
        self._lineno: System.Nullable[int]
        self._col_offset: System.Nullable[int]
        ...

    # static fields
    Instance: IronPython.Modules._ast.And = ...

    # properties
    @property
    def _fields(self) -> IronPython.Runtime.PythonTuple:
        ...
    @_fields.setter
    def _fields(self, val: IronPython.Runtime.PythonTuple):
        ...

    @property
    def _attributes(self) -> IronPython.Runtime.PythonTuple:
        ...
    @_attributes.setter
    def _attributes(self, val: IronPython.Runtime.PythonTuple):
        ...

    @property
    def lineno(self) -> int:
        ...
    @lineno.setter
    def lineno(self, val: int):
        ...

    @property
    def col_offset(self) -> int:
        ...
    @col_offset.setter
    def col_offset(self, val: int):
        ...

    # methods
    def __init__(self, ):
        ...

class Eq(IronPython.Modules._ast.cmpop):
    @typing.overload
    def __init__(self, **kwargs):
        self._lineno: System.Nullable[int]
        self._col_offset: System.Nullable[int]
        ...

    # static fields
    Instance: IronPython.Modules._ast.Eq = ...

    # properties
    @property
    def _fields(self) -> IronPython.Runtime.PythonTuple:
        ...
    @_fields.setter
    def _fields(self, val: IronPython.Runtime.PythonTuple):
        ...

    @property
    def _attributes(self) -> IronPython.Runtime.PythonTuple:
        ...
    @_attributes.setter
    def _attributes(self, val: IronPython.Runtime.PythonTuple):
        ...

    @property
    def lineno(self) -> int:
        ...
    @lineno.setter
    def lineno(self, val: int):
        ...

    @property
    def col_offset(self) -> int:
        ...
    @col_offset.setter
    def col_offset(self, val: int):
        ...

    # methods
    def __init__(self, ):
        ...

    def Revert(self, ) -> int:
        ...

class With(IronPython.Modules._ast.stmt):
    @typing.overload
    def __init__(self, **kwargs):
        self._lineno: System.Nullable[int]
        self._col_offset: System.Nullable[int]
        ...

    # static fields

    # properties
    @property
    def items(self) -> IronPython.Runtime.PythonList:
        ...
    @items.setter
    def items(self, val: IronPython.Runtime.PythonList):
        ...

    @property
    def body(self) -> IronPython.Runtime.PythonList:
        ...
    @body.setter
    def body(self, val: IronPython.Runtime.PythonList):
        ...

    @property
    def _fields(self) -> IronPython.Runtime.PythonTuple:
        ...
    @_fields.setter
    def _fields(self, val: IronPython.Runtime.PythonTuple):
        ...

    @property
    def _attributes(self) -> IronPython.Runtime.PythonTuple:
        ...
    @_attributes.setter
    def _attributes(self, val: IronPython.Runtime.PythonTuple):
        ...

    @property
    def lineno(self) -> int:
        ...
    @lineno.setter
    def lineno(self, val: int):
        ...

    @property
    def col_offset(self) -> int:
        ...
    @col_offset.setter
    def col_offset(self, val: int):
        ...

    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def __init__(self, items: IronPython.Runtime.PythonList, body: IronPython.Runtime.PythonList, lineno: System.Nullable[int], col_offset: System.Nullable[int], ):
        ...

    @typing.overload
    def __init__(self, with: IronPython.Compiler.Ast.WithStatement, ):
        ...

    def Revert(self, ) -> IronPython.Compiler.Ast.Statement:
        ...

class DictComp(IronPython.Modules._ast.expr):
    @typing.overload
    def __init__(self, **kwargs):
        self._lineno: System.Nullable[int]
        self._col_offset: System.Nullable[int]
        ...

    # static fields

    # properties
    @property
    def key(self) -> IronPython.Modules._ast.expr:
        ...
    @key.setter
    def key(self, val: IronPython.Modules._ast.expr):
        ...

    @property
    def value(self) -> IronPython.Modules._ast.expr:
        ...
    @value.setter
    def value(self, val: IronPython.Modules._ast.expr):
        ...

    @property
    def generators(self) -> IronPython.Runtime.PythonList:
        ...
    @generators.setter
    def generators(self, val: IronPython.Runtime.PythonList):
        ...

    @property
    def _fields(self) -> IronPython.Runtime.PythonTuple:
        ...
    @_fields.setter
    def _fields(self, val: IronPython.Runtime.PythonTuple):
        ...

    @property
    def _attributes(self) -> IronPython.Runtime.PythonTuple:
        ...
    @_attributes.setter
    def _attributes(self, val: IronPython.Runtime.PythonTuple):
        ...

    @property
    def lineno(self) -> int:
        ...
    @lineno.setter
    def lineno(self, val: int):
        ...

    @property
    def col_offset(self) -> int:
        ...
    @col_offset.setter
    def col_offset(self, val: int):
        ...

    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def __init__(self, key: IronPython.Modules._ast.expr, value: IronPython.Modules._ast.expr, generators: IronPython.Runtime.PythonList, lineno: System.Nullable[int], col_offset: System.Nullable[int], ):
        ...

    @typing.overload
    def __init__(self, comp: IronPython.Compiler.Ast.DictionaryComprehension, ):
        ...

    def Revert(self, ) -> IronPython.Compiler.Ast.Expression:
        ...

class Mod(IronPython.Modules._ast.operator):
    @typing.overload
    def __init__(self, **kwargs):
        self._lineno: System.Nullable[int]
        self._col_offset: System.Nullable[int]
        ...

    # static fields
    Instance: IronPython.Modules._ast.Mod = ...

    # properties
    @property
    def _fields(self) -> IronPython.Runtime.PythonTuple:
        ...
    @_fields.setter
    def _fields(self, val: IronPython.Runtime.PythonTuple):
        ...

    @property
    def _attributes(self) -> IronPython.Runtime.PythonTuple:
        ...
    @_attributes.setter
    def _attributes(self, val: IronPython.Runtime.PythonTuple):
        ...

    @property
    def lineno(self) -> int:
        ...
    @lineno.setter
    def lineno(self, val: int):
        ...

    @property
    def col_offset(self) -> int:
        ...
    @col_offset.setter
    def col_offset(self, val: int):
        ...

    # methods
    def __init__(self, ):
        ...

    def Revert(self, ) -> int:
        ...

class stmt(IronPython.Modules._ast.AST, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        self._lineno: System.Nullable[int]
        self._col_offset: System.Nullable[int]
        ...

    # static fields

    # properties
    @property
    def _fields(self) -> IronPython.Runtime.PythonTuple:
        ...
    @_fields.setter
    def _fields(self, val: IronPython.Runtime.PythonTuple):
        ...

    @property
    def _attributes(self) -> IronPython.Runtime.PythonTuple:
        ...
    @_attributes.setter
    def _attributes(self, val: IronPython.Runtime.PythonTuple):
        ...

    @property
    def lineno(self) -> int:
        ...
    @lineno.setter
    def lineno(self, val: int):
        ...

    @property
    def col_offset(self) -> int:
        ...
    @col_offset.setter
    def col_offset(self, val: int):
        ...

    # methods
    def __init__(self, ):
        ...

    def Revert(self, ) -> IronPython.Compiler.Ast.Statement:
        ...

    @staticmethod
    def RevertStmts(stmts: IronPython.Runtime.PythonList, ) -> IronPython.Compiler.Ast.Statement:
        ...

class ExceptHandler(IronPython.Modules._ast.excepthandler):
    @typing.overload
    def __init__(self, **kwargs):
        self._lineno: System.Nullable[int]
        self._col_offset: System.Nullable[int]
        ...

    # static fields

    # properties
    @property
    def type(self) -> IronPython.Modules._ast.expr:
        ...
    @type.setter
    def type(self, val: IronPython.Modules._ast.expr):
        ...

    @property
    def name(self) -> IronPython.Modules._ast.expr:
        ...
    @name.setter
    def name(self, val: IronPython.Modules._ast.expr):
        ...

    @property
    def body(self) -> IronPython.Runtime.PythonList:
        ...
    @body.setter
    def body(self, val: IronPython.Runtime.PythonList):
        ...

    @property
    def _fields(self) -> IronPython.Runtime.PythonTuple:
        ...
    @_fields.setter
    def _fields(self, val: IronPython.Runtime.PythonTuple):
        ...

    @property
    def _attributes(self) -> IronPython.Runtime.PythonTuple:
        ...
    @_attributes.setter
    def _attributes(self, val: IronPython.Runtime.PythonTuple):
        ...

    @property
    def lineno(self) -> int:
        ...
    @lineno.setter
    def lineno(self, val: int):
        ...

    @property
    def col_offset(self) -> int:
        ...
    @col_offset.setter
    def col_offset(self, val: int):
        ...

    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def __init__(self, type: IronPython.Modules._ast.expr, name: IronPython.Modules._ast.expr, body: IronPython.Runtime.PythonList, lineno: System.Nullable[int], col_offset: System.Nullable[int], ):
        ...

    @typing.overload
    def __init__(self, stmt: IronPython.Compiler.Ast.TryStatementHandler, ):
        ...

    def RevertHandler(self, ) -> IronPython.Compiler.Ast.TryStatementHandler:
        ...

class Ellipsis(IronPython.Modules._ast.expr):
    @typing.overload
    def __init__(self, **kwargs):
        self._lineno: System.Nullable[int]
        self._col_offset: System.Nullable[int]
        ...

    # static fields
    Instance: IronPython.Modules._ast.Ellipsis = ...

    # properties
    @property
    def _fields(self) -> IronPython.Runtime.PythonTuple:
        ...
    @_fields.setter
    def _fields(self, val: IronPython.Runtime.PythonTuple):
        ...

    @property
    def _attributes(self) -> IronPython.Runtime.PythonTuple:
        ...
    @_attributes.setter
    def _attributes(self, val: IronPython.Runtime.PythonTuple):
        ...

    @property
    def lineno(self) -> int:
        ...
    @lineno.setter
    def lineno(self, val: int):
        ...

    @property
    def col_offset(self) -> int:
        ...
    @col_offset.setter
    def col_offset(self, val: int):
        ...

    # methods
    def __init__(self, ):
        ...

    def Revert(self, ) -> IronPython.Compiler.Ast.Expression:
        ...

class NameConstant(IronPython.Modules._ast.expr):
    @typing.overload
    def __init__(self, **kwargs):
        self._lineno: System.Nullable[int]
        self._col_offset: System.Nullable[int]
        ...

    # static fields

    # properties
    @property
    def value(self) -> System.Object:
        ...
    @value.setter
    def value(self, val: System.Object):
        ...

    @property
    def _fields(self) -> IronPython.Runtime.PythonTuple:
        ...
    @_fields.setter
    def _fields(self, val: IronPython.Runtime.PythonTuple):
        ...

    @property
    def _attributes(self) -> IronPython.Runtime.PythonTuple:
        ...
    @_attributes.setter
    def _attributes(self, val: IronPython.Runtime.PythonTuple):
        ...

    @property
    def lineno(self) -> int:
        ...
    @lineno.setter
    def lineno(self, val: int):
        ...

    @property
    def col_offset(self) -> int:
        ...
    @col_offset.setter
    def col_offset(self, val: int):
        ...

    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def __init__(self, value: System.Object, lineno: System.Nullable[int], col_offset: System.Nullable[int], ):
        ...

    @typing.overload
    def __init__(self, value: System.Object, ):
        ...

    def Revert(self, ) -> IronPython.Compiler.Ast.Expression:
        ...

class If(IronPython.Modules._ast.stmt):
    @typing.overload
    def __init__(self, **kwargs):
        self._lineno: System.Nullable[int]
        self._col_offset: System.Nullable[int]
        ...

    # static fields

    # properties
    @property
    def test(self) -> IronPython.Modules._ast.expr:
        ...
    @test.setter
    def test(self, val: IronPython.Modules._ast.expr):
        ...

    @property
    def body(self) -> IronPython.Runtime.PythonList:
        ...
    @body.setter
    def body(self, val: IronPython.Runtime.PythonList):
        ...

    @property
    def orelse(self) -> IronPython.Runtime.PythonList:
        ...
    @orelse.setter
    def orelse(self, val: IronPython.Runtime.PythonList):
        ...

    @property
    def _fields(self) -> IronPython.Runtime.PythonTuple:
        ...
    @_fields.setter
    def _fields(self, val: IronPython.Runtime.PythonTuple):
        ...

    @property
    def _attributes(self) -> IronPython.Runtime.PythonTuple:
        ...
    @_attributes.setter
    def _attributes(self, val: IronPython.Runtime.PythonTuple):
        ...

    @property
    def lineno(self) -> int:
        ...
    @lineno.setter
    def lineno(self, val: int):
        ...

    @property
    def col_offset(self) -> int:
        ...
    @col_offset.setter
    def col_offset(self, val: int):
        ...

    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def __init__(self, test: IronPython.Modules._ast.expr, body: IronPython.Runtime.PythonList, orelse: IronPython.Runtime.PythonList, lineno: System.Nullable[int], col_offset: System.Nullable[int], ):
        ...

    @typing.overload
    def __init__(self, stmt: IronPython.Compiler.Ast.IfStatement, ):
        ...

    def Initialize(self, ifTest: IronPython.Compiler.Ast.IfStatementTest, ) -> None:
        ...

    def Revert(self, ) -> IronPython.Compiler.Ast.Statement:
        ...

class List(IronPython.Modules._ast.expr):
    @typing.overload
    def __init__(self, **kwargs):
        self._lineno: System.Nullable[int]
        self._col_offset: System.Nullable[int]
        ...

    # static fields

    # properties
    @property
    def elts(self) -> IronPython.Runtime.PythonList:
        ...
    @elts.setter
    def elts(self, val: IronPython.Runtime.PythonList):
        ...

    @property
    def ctx(self) -> IronPython.Modules._ast.expr_context:
        ...
    @ctx.setter
    def ctx(self, val: IronPython.Modules._ast.expr_context):
        ...

    @property
    def _fields(self) -> IronPython.Runtime.PythonTuple:
        ...
    @_fields.setter
    def _fields(self, val: IronPython.Runtime.PythonTuple):
        ...

    @property
    def _attributes(self) -> IronPython.Runtime.PythonTuple:
        ...
    @_attributes.setter
    def _attributes(self, val: IronPython.Runtime.PythonTuple):
        ...

    @property
    def lineno(self) -> int:
        ...
    @lineno.setter
    def lineno(self, val: int):
        ...

    @property
    def col_offset(self) -> int:
        ...
    @col_offset.setter
    def col_offset(self, val: int):
        ...

    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def __init__(self, elts: IronPython.Runtime.PythonList, ctx: IronPython.Modules._ast.expr_context, lineno: System.Nullable[int], col_offset: System.Nullable[int], ):
        ...

    @typing.overload
    def __init__(self, list: IronPython.Compiler.Ast.ListExpression, ctx: IronPython.Modules._ast.expr_context, ):
        ...

    def Revert(self, ) -> IronPython.Compiler.Ast.Expression:
        ...

class Call(IronPython.Modules._ast.expr):
    @typing.overload
    def __init__(self, **kwargs):
        self._lineno: System.Nullable[int]
        self._col_offset: System.Nullable[int]
        ...

    # static fields

    # properties
    @property
    def func(self) -> IronPython.Modules._ast.expr:
        ...
    @func.setter
    def func(self, val: IronPython.Modules._ast.expr):
        ...

    @property
    def args(self) -> IronPython.Runtime.PythonList:
        ...
    @args.setter
    def args(self, val: IronPython.Runtime.PythonList):
        ...

    @property
    def keywords(self) -> IronPython.Runtime.PythonList:
        ...
    @keywords.setter
    def keywords(self, val: IronPython.Runtime.PythonList):
        ...

    @property
    def _fields(self) -> IronPython.Runtime.PythonTuple:
        ...
    @_fields.setter
    def _fields(self, val: IronPython.Runtime.PythonTuple):
        ...

    @property
    def _attributes(self) -> IronPython.Runtime.PythonTuple:
        ...
    @_attributes.setter
    def _attributes(self, val: IronPython.Runtime.PythonTuple):
        ...

    @property
    def lineno(self) -> int:
        ...
    @lineno.setter
    def lineno(self, val: int):
        ...

    @property
    def col_offset(self) -> int:
        ...
    @col_offset.setter
    def col_offset(self, val: int):
        ...

    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def __init__(self, func: IronPython.Modules._ast.expr, args: IronPython.Runtime.PythonList, keywords: IronPython.Runtime.PythonList, lineno: System.Nullable[int], col_offset: System.Nullable[int], ):
        ...

    @typing.overload
    def __init__(self, call: IronPython.Compiler.Ast.CallExpression, ):
        ...

    def Revert(self, ) -> IronPython.Compiler.Ast.Expression:
        ...

class Global(IronPython.Modules._ast.stmt):
    @typing.overload
    def __init__(self, **kwargs):
        self._lineno: System.Nullable[int]
        self._col_offset: System.Nullable[int]
        ...

    # static fields

    # properties
    @property
    def names(self) -> IronPython.Runtime.PythonList:
        ...
    @names.setter
    def names(self, val: IronPython.Runtime.PythonList):
        ...

    @property
    def _fields(self) -> IronPython.Runtime.PythonTuple:
        ...
    @_fields.setter
    def _fields(self, val: IronPython.Runtime.PythonTuple):
        ...

    @property
    def _attributes(self) -> IronPython.Runtime.PythonTuple:
        ...
    @_attributes.setter
    def _attributes(self, val: IronPython.Runtime.PythonTuple):
        ...

    @property
    def lineno(self) -> int:
        ...
    @lineno.setter
    def lineno(self, val: int):
        ...

    @property
    def col_offset(self) -> int:
        ...
    @col_offset.setter
    def col_offset(self, val: int):
        ...

    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def __init__(self, names: IronPython.Runtime.PythonList, lineno: System.Nullable[int], col_offset: System.Nullable[int], ):
        ...

    @typing.overload
    def __init__(self, stmt: IronPython.Compiler.Ast.GlobalStatement, ):
        ...

    def Revert(self, ) -> IronPython.Compiler.Ast.Statement:
        ...

class keyword(IronPython.Modules._ast.AST):
    @typing.overload
    def __init__(self, **kwargs):
        self._lineno: System.Nullable[int]
        self._col_offset: System.Nullable[int]
        ...

    # static fields

    # properties
    @property
    def arg(self) -> str:
        ...
    @arg.setter
    def arg(self, val: str):
        ...

    @property
    def value(self) -> IronPython.Modules._ast.expr:
        ...
    @value.setter
    def value(self, val: IronPython.Modules._ast.expr):
        ...

    @property
    def _fields(self) -> IronPython.Runtime.PythonTuple:
        ...
    @_fields.setter
    def _fields(self, val: IronPython.Runtime.PythonTuple):
        ...

    @property
    def _attributes(self) -> IronPython.Runtime.PythonTuple:
        ...
    @_attributes.setter
    def _attributes(self, val: IronPython.Runtime.PythonTuple):
        ...

    @property
    def lineno(self) -> int:
        ...
    @lineno.setter
    def lineno(self, val: int):
        ...

    @property
    def col_offset(self) -> int:
        ...
    @col_offset.setter
    def col_offset(self, val: int):
        ...

    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def __init__(self, arg: str, value: IronPython.Modules._ast.expr, ):
        ...

    @typing.overload
    def __init__(self, arg: IronPython.Compiler.Ast.Keyword, ):
        ...

class BinOp(IronPython.Modules._ast.expr):
    @typing.overload
    def __init__(self, **kwargs):
        self._lineno: System.Nullable[int]
        self._col_offset: System.Nullable[int]
        ...

    # static fields

    # properties
    @property
    def left(self) -> IronPython.Modules._ast.expr:
        ...
    @left.setter
    def left(self, val: IronPython.Modules._ast.expr):
        ...

    @property
    def right(self) -> IronPython.Modules._ast.expr:
        ...
    @right.setter
    def right(self, val: IronPython.Modules._ast.expr):
        ...

    @property
    def op(self) -> IronPython.Modules._ast.operator:
        ...
    @op.setter
    def op(self, val: IronPython.Modules._ast.operator):
        ...

    @property
    def _fields(self) -> IronPython.Runtime.PythonTuple:
        ...
    @_fields.setter
    def _fields(self, val: IronPython.Runtime.PythonTuple):
        ...

    @property
    def _attributes(self) -> IronPython.Runtime.PythonTuple:
        ...
    @_attributes.setter
    def _attributes(self, val: IronPython.Runtime.PythonTuple):
        ...

    @property
    def lineno(self) -> int:
        ...
    @lineno.setter
    def lineno(self, val: int):
        ...

    @property
    def col_offset(self) -> int:
        ...
    @col_offset.setter
    def col_offset(self, val: int):
        ...

    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def __init__(self, left: IronPython.Modules._ast.expr, op: IronPython.Modules._ast.operator, right: IronPython.Modules._ast.expr, lineno: System.Nullable[int], col_offset: System.Nullable[int], ):
        ...

    @typing.overload
    def __init__(self, expr: IronPython.Compiler.Ast.BinaryExpression, op: IronPython.Modules._ast.operator, ):
        ...

    def Revert(self, ) -> IronPython.Compiler.Ast.Expression:
        ...

class AsyncFunctionDef(IronPython.Modules._ast.stmt):
    @typing.overload
    def __init__(self, **kwargs):
        self._lineno: System.Nullable[int]
        self._col_offset: System.Nullable[int]
        ...

    # static fields

    # properties
    @property
    def name(self) -> IronPython.Modules._ast.expr:
        ...
    @name.setter
    def name(self, val: IronPython.Modules._ast.expr):
        ...

    @property
    def args(self) -> IronPython.Modules._ast.expr:
        ...
    @args.setter
    def args(self, val: IronPython.Modules._ast.expr):
        ...

    @property
    def body(self) -> IronPython.Modules._ast.expr:
        ...
    @body.setter
    def body(self, val: IronPython.Modules._ast.expr):
        ...

    @property
    def decorator_list(self) -> IronPython.Modules._ast.expr:
        ...
    @decorator_list.setter
    def decorator_list(self, val: IronPython.Modules._ast.expr):
        ...

    @property
    def returns(self) -> IronPython.Modules._ast.expr:
        ...
    @returns.setter
    def returns(self, val: IronPython.Modules._ast.expr):
        ...

    @property
    def _fields(self) -> IronPython.Runtime.PythonTuple:
        ...
    @_fields.setter
    def _fields(self, val: IronPython.Runtime.PythonTuple):
        ...

    @property
    def _attributes(self) -> IronPython.Runtime.PythonTuple:
        ...
    @_attributes.setter
    def _attributes(self, val: IronPython.Runtime.PythonTuple):
        ...

    @property
    def lineno(self) -> int:
        ...
    @lineno.setter
    def lineno(self, val: int):
        ...

    @property
    def col_offset(self) -> int:
        ...
    @col_offset.setter
    def col_offset(self, val: int):
        ...

    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def __init__(self, name: IronPython.Modules._ast.expr, args: IronPython.Modules._ast.expr, body: IronPython.Modules._ast.expr, decorator_list: IronPython.Modules._ast.expr, returns: IronPython.Modules._ast.expr, lineno: System.Nullable[int], col_offset: System.Nullable[int], ):
        ...

class Name(IronPython.Modules._ast.expr):
    @typing.overload
    def __init__(self, **kwargs):
        self._lineno: System.Nullable[int]
        self._col_offset: System.Nullable[int]
        ...

    # static fields

    # properties
    @property
    def ctx(self) -> IronPython.Modules._ast.expr_context:
        ...
    @ctx.setter
    def ctx(self, val: IronPython.Modules._ast.expr_context):
        ...

    @property
    def id(self) -> str:
        ...
    @id.setter
    def id(self, val: str):
        ...

    @property
    def _fields(self) -> IronPython.Runtime.PythonTuple:
        ...
    @_fields.setter
    def _fields(self, val: IronPython.Runtime.PythonTuple):
        ...

    @property
    def _attributes(self) -> IronPython.Runtime.PythonTuple:
        ...
    @_attributes.setter
    def _attributes(self, val: IronPython.Runtime.PythonTuple):
        ...

    @property
    def lineno(self) -> int:
        ...
    @lineno.setter
    def lineno(self, val: int):
        ...

    @property
    def col_offset(self) -> int:
        ...
    @col_offset.setter
    def col_offset(self, val: int):
        ...

    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def __init__(self, id: str, ctx: IronPython.Modules._ast.expr_context, lineno: System.Nullable[int], col_offset: System.Nullable[int], ):
        ...

    @typing.overload
    def __init__(self, id: str, ctx: IronPython.Modules._ast.expr_context, ):
        ...

    @typing.overload
    def __init__(self, para: IronPython.Compiler.Ast.Parameter, ):
        ...

    @typing.overload
    def __init__(self, expr: IronPython.Compiler.Ast.NameExpression, ctx: IronPython.Modules._ast.expr_context, ):
        ...

    def Revert(self, ) -> IronPython.Compiler.Ast.Expression:
        ...

class withitem(IronPython.Modules._ast.AST):
    @typing.overload
    def __init__(self, **kwargs):
        self._lineno: System.Nullable[int]
        self._col_offset: System.Nullable[int]
        ...

    # static fields

    # properties
    @property
    def context_expr(self) -> IronPython.Modules._ast.expr:
        ...
    @context_expr.setter
    def context_expr(self, val: IronPython.Modules._ast.expr):
        ...

    @property
    def optional_vars(self) -> IronPython.Modules._ast.expr:
        ...
    @optional_vars.setter
    def optional_vars(self, val: IronPython.Modules._ast.expr):
        ...

    @property
    def _fields(self) -> IronPython.Runtime.PythonTuple:
        ...
    @_fields.setter
    def _fields(self, val: IronPython.Runtime.PythonTuple):
        ...

    @property
    def _attributes(self) -> IronPython.Runtime.PythonTuple:
        ...
    @_attributes.setter
    def _attributes(self, val: IronPython.Runtime.PythonTuple):
        ...

    @property
    def lineno(self) -> int:
        ...
    @lineno.setter
    def lineno(self, val: int):
        ...

    @property
    def col_offset(self) -> int:
        ...
    @col_offset.setter
    def col_offset(self, val: int):
        ...

    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def __init__(self, context_expr: IronPython.Modules._ast.expr, optional_vars: IronPython.Modules._ast.expr, lineno: System.Nullable[int], col_offset: System.Nullable[int], ):
        ...

class Div(IronPython.Modules._ast.operator):
    @typing.overload
    def __init__(self, **kwargs):
        self._lineno: System.Nullable[int]
        self._col_offset: System.Nullable[int]
        ...

    # static fields
    Instance: IronPython.Modules._ast.Div = ...

    # properties
    @property
    def _fields(self) -> IronPython.Runtime.PythonTuple:
        ...
    @_fields.setter
    def _fields(self, val: IronPython.Runtime.PythonTuple):
        ...

    @property
    def _attributes(self) -> IronPython.Runtime.PythonTuple:
        ...
    @_attributes.setter
    def _attributes(self, val: IronPython.Runtime.PythonTuple):
        ...

    @property
    def lineno(self) -> int:
        ...
    @lineno.setter
    def lineno(self, val: int):
        ...

    @property
    def col_offset(self) -> int:
        ...
    @col_offset.setter
    def col_offset(self, val: int):
        ...

    # methods
    def __init__(self, ):
        ...

    def Revert(self, ) -> int:
        ...

class While(IronPython.Modules._ast.stmt):
    @typing.overload
    def __init__(self, **kwargs):
        self._lineno: System.Nullable[int]
        self._col_offset: System.Nullable[int]
        ...

    # static fields

    # properties
    @property
    def test(self) -> IronPython.Modules._ast.expr:
        ...
    @test.setter
    def test(self, val: IronPython.Modules._ast.expr):
        ...

    @property
    def body(self) -> IronPython.Runtime.PythonList:
        ...
    @body.setter
    def body(self, val: IronPython.Runtime.PythonList):
        ...

    @property
    def orelse(self) -> IronPython.Runtime.PythonList:
        ...
    @orelse.setter
    def orelse(self, val: IronPython.Runtime.PythonList):
        ...

    @property
    def _fields(self) -> IronPython.Runtime.PythonTuple:
        ...
    @_fields.setter
    def _fields(self, val: IronPython.Runtime.PythonTuple):
        ...

    @property
    def _attributes(self) -> IronPython.Runtime.PythonTuple:
        ...
    @_attributes.setter
    def _attributes(self, val: IronPython.Runtime.PythonTuple):
        ...

    @property
    def lineno(self) -> int:
        ...
    @lineno.setter
    def lineno(self, val: int):
        ...

    @property
    def col_offset(self) -> int:
        ...
    @col_offset.setter
    def col_offset(self, val: int):
        ...

    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def __init__(self, test: IronPython.Modules._ast.expr, body: IronPython.Runtime.PythonList, orelse: IronPython.Runtime.PythonList, lineno: System.Nullable[int], col_offset: System.Nullable[int], ):
        ...

    @typing.overload
    def __init__(self, stmt: IronPython.Compiler.Ast.WhileStatement, ):
        ...

    def Revert(self, ) -> IronPython.Compiler.Ast.Statement:
        ...

class IfExp(IronPython.Modules._ast.expr):
    @typing.overload
    def __init__(self, **kwargs):
        self._lineno: System.Nullable[int]
        self._col_offset: System.Nullable[int]
        ...

    # static fields

    # properties
    @property
    def test(self) -> IronPython.Modules._ast.expr:
        ...
    @test.setter
    def test(self, val: IronPython.Modules._ast.expr):
        ...

    @property
    def body(self) -> IronPython.Modules._ast.expr:
        ...
    @body.setter
    def body(self, val: IronPython.Modules._ast.expr):
        ...

    @property
    def orelse(self) -> IronPython.Modules._ast.expr:
        ...
    @orelse.setter
    def orelse(self, val: IronPython.Modules._ast.expr):
        ...

    @property
    def _fields(self) -> IronPython.Runtime.PythonTuple:
        ...
    @_fields.setter
    def _fields(self, val: IronPython.Runtime.PythonTuple):
        ...

    @property
    def _attributes(self) -> IronPython.Runtime.PythonTuple:
        ...
    @_attributes.setter
    def _attributes(self, val: IronPython.Runtime.PythonTuple):
        ...

    @property
    def lineno(self) -> int:
        ...
    @lineno.setter
    def lineno(self, val: int):
        ...

    @property
    def col_offset(self) -> int:
        ...
    @col_offset.setter
    def col_offset(self, val: int):
        ...

    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def __init__(self, test: IronPython.Modules._ast.expr, body: IronPython.Modules._ast.expr, orelse: IronPython.Modules._ast.expr, lineno: System.Nullable[int], col_offset: System.Nullable[int], ):
        ...

    @typing.overload
    def __init__(self, cond: IronPython.Compiler.Ast.ConditionalExpression, ):
        ...

    def Revert(self, ) -> IronPython.Compiler.Ast.Expression:
        ...

class Compare(IronPython.Modules._ast.expr):
    @typing.overload
    def __init__(self, **kwargs):
        self._lineno: System.Nullable[int]
        self._col_offset: System.Nullable[int]
        ...

    # static fields

    # properties
    @property
    def left(self) -> IronPython.Modules._ast.expr:
        ...
    @left.setter
    def left(self, val: IronPython.Modules._ast.expr):
        ...

    @property
    def ops(self) -> IronPython.Runtime.PythonList:
        ...
    @ops.setter
    def ops(self, val: IronPython.Runtime.PythonList):
        ...

    @property
    def comparators(self) -> IronPython.Runtime.PythonList:
        ...
    @comparators.setter
    def comparators(self, val: IronPython.Runtime.PythonList):
        ...

    @property
    def _fields(self) -> IronPython.Runtime.PythonTuple:
        ...
    @_fields.setter
    def _fields(self, val: IronPython.Runtime.PythonTuple):
        ...

    @property
    def _attributes(self) -> IronPython.Runtime.PythonTuple:
        ...
    @_attributes.setter
    def _attributes(self, val: IronPython.Runtime.PythonTuple):
        ...

    @property
    def lineno(self) -> int:
        ...
    @lineno.setter
    def lineno(self, val: int):
        ...

    @property
    def col_offset(self) -> int:
        ...
    @col_offset.setter
    def col_offset(self, val: int):
        ...

    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def __init__(self, left: IronPython.Modules._ast.expr, ops: IronPython.Runtime.PythonList, comparators: IronPython.Runtime.PythonList, lineno: System.Nullable[int], col_offset: System.Nullable[int], ):
        ...

    @typing.overload
    def __init__(self, expr: IronPython.Compiler.Ast.BinaryExpression, ):
        ...

    def Revert(self, ) -> IronPython.Compiler.Ast.Expression:
        ...

class Suite(IronPython.Modules._ast.mod):
    @typing.overload
    def __init__(self, **kwargs):
        self._lineno: System.Nullable[int]
        self._col_offset: System.Nullable[int]
        ...

    # static fields

    # properties
    @property
    def body(self) -> IronPython.Runtime.PythonList:
        ...
    @body.setter
    def body(self, val: IronPython.Runtime.PythonList):
        ...

    @property
    def _fields(self) -> IronPython.Runtime.PythonTuple:
        ...
    @_fields.setter
    def _fields(self, val: IronPython.Runtime.PythonTuple):
        ...

    @property
    def _attributes(self) -> IronPython.Runtime.PythonTuple:
        ...
    @_attributes.setter
    def _attributes(self, val: IronPython.Runtime.PythonTuple):
        ...

    @property
    def lineno(self) -> int:
        ...
    @lineno.setter
    def lineno(self, val: int):
        ...

    @property
    def col_offset(self) -> int:
        ...
    @col_offset.setter
    def col_offset(self, val: int):
        ...

    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def __init__(self, body: IronPython.Runtime.PythonList, ):
        ...

    def GetStatements(self, ) -> IronPython.Runtime.PythonList:
        ...

class boolop(IronPython.Modules._ast.AST, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        self._lineno: System.Nullable[int]
        self._col_offset: System.Nullable[int]
        ...

    # static fields

    # properties
    @property
    def _fields(self) -> IronPython.Runtime.PythonTuple:
        ...
    @_fields.setter
    def _fields(self, val: IronPython.Runtime.PythonTuple):
        ...

    @property
    def _attributes(self) -> IronPython.Runtime.PythonTuple:
        ...
    @_attributes.setter
    def _attributes(self, val: IronPython.Runtime.PythonTuple):
        ...

    @property
    def lineno(self) -> int:
        ...
    @lineno.setter
    def lineno(self, val: int):
        ...

    @property
    def col_offset(self) -> int:
        ...
    @col_offset.setter
    def col_offset(self, val: int):
        ...

    # methods
    def __init__(self, ):
        ...

class Tuple(IronPython.Modules._ast.expr):
    @typing.overload
    def __init__(self, **kwargs):
        self._lineno: System.Nullable[int]
        self._col_offset: System.Nullable[int]
        ...

    # static fields

    # properties
    @property
    def elts(self) -> IronPython.Runtime.PythonList:
        ...
    @elts.setter
    def elts(self, val: IronPython.Runtime.PythonList):
        ...

    @property
    def ctx(self) -> IronPython.Modules._ast.expr_context:
        ...
    @ctx.setter
    def ctx(self, val: IronPython.Modules._ast.expr_context):
        ...

    @property
    def _fields(self) -> IronPython.Runtime.PythonTuple:
        ...
    @_fields.setter
    def _fields(self, val: IronPython.Runtime.PythonTuple):
        ...

    @property
    def _attributes(self) -> IronPython.Runtime.PythonTuple:
        ...
    @_attributes.setter
    def _attributes(self, val: IronPython.Runtime.PythonTuple):
        ...

    @property
    def lineno(self) -> int:
        ...
    @lineno.setter
    def lineno(self, val: int):
        ...

    @property
    def col_offset(self) -> int:
        ...
    @col_offset.setter
    def col_offset(self, val: int):
        ...

    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def __init__(self, elts: IronPython.Runtime.PythonList, ctx: IronPython.Modules._ast.expr_context, lineno: System.Nullable[int], col_offset: System.Nullable[int], ):
        ...

    @typing.overload
    def __init__(self, list: IronPython.Compiler.Ast.TupleExpression, ctx: IronPython.Modules._ast.expr_context, ):
        ...

    def Revert(self, ) -> IronPython.Compiler.Ast.Expression:
        ...

class Lambda(IronPython.Modules._ast.expr):
    @typing.overload
    def __init__(self, **kwargs):
        self._lineno: System.Nullable[int]
        self._col_offset: System.Nullable[int]
        ...

    # static fields

    # properties
    @property
    def args(self) -> IronPython.Modules._ast.arguments:
        ...
    @args.setter
    def args(self, val: IronPython.Modules._ast.arguments):
        ...

    @property
    def body(self) -> IronPython.Modules._ast.expr:
        ...
    @body.setter
    def body(self, val: IronPython.Modules._ast.expr):
        ...

    @property
    def _fields(self) -> IronPython.Runtime.PythonTuple:
        ...
    @_fields.setter
    def _fields(self, val: IronPython.Runtime.PythonTuple):
        ...

    @property
    def _attributes(self) -> IronPython.Runtime.PythonTuple:
        ...
    @_attributes.setter
    def _attributes(self, val: IronPython.Runtime.PythonTuple):
        ...

    @property
    def lineno(self) -> int:
        ...
    @lineno.setter
    def lineno(self, val: int):
        ...

    @property
    def col_offset(self) -> int:
        ...
    @col_offset.setter
    def col_offset(self, val: int):
        ...

    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def __init__(self, args: IronPython.Modules._ast.arguments, body: IronPython.Modules._ast.expr, lineno: System.Nullable[int], col_offset: System.Nullable[int], ):
        ...

    @typing.overload
    def __init__(self, lambda: IronPython.Compiler.Ast.LambdaExpression, ):
        ...

    def Revert(self, ) -> IronPython.Compiler.Ast.Expression:
        ...

class Assign(IronPython.Modules._ast.stmt):
    @typing.overload
    def __init__(self, **kwargs):
        self._lineno: System.Nullable[int]
        self._col_offset: System.Nullable[int]
        ...

    # static fields

    # properties
    @property
    def targets(self) -> IronPython.Runtime.PythonList:
        ...
    @targets.setter
    def targets(self, val: IronPython.Runtime.PythonList):
        ...

    @property
    def value(self) -> IronPython.Modules._ast.expr:
        ...
    @value.setter
    def value(self, val: IronPython.Modules._ast.expr):
        ...

    @property
    def _fields(self) -> IronPython.Runtime.PythonTuple:
        ...
    @_fields.setter
    def _fields(self, val: IronPython.Runtime.PythonTuple):
        ...

    @property
    def _attributes(self) -> IronPython.Runtime.PythonTuple:
        ...
    @_attributes.setter
    def _attributes(self, val: IronPython.Runtime.PythonTuple):
        ...

    @property
    def lineno(self) -> int:
        ...
    @lineno.setter
    def lineno(self, val: int):
        ...

    @property
    def col_offset(self) -> int:
        ...
    @col_offset.setter
    def col_offset(self, val: int):
        ...

    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def __init__(self, targets: IronPython.Runtime.PythonList, value: IronPython.Modules._ast.expr, lineno: System.Nullable[int], col_offset: System.Nullable[int], ):
        ...

    @typing.overload
    def __init__(self, stmt: IronPython.Compiler.Ast.AssignmentStatement, ):
        ...

    def Revert(self, ) -> IronPython.Compiler.Ast.Statement:
        ...

class Str(IronPython.Modules._ast.expr):
    @typing.overload
    def __init__(self, **kwargs):
        self._lineno: System.Nullable[int]
        self._col_offset: System.Nullable[int]
        ...

    # static fields

    # properties
    @property
    def s(self) -> str:
        ...
    @s.setter
    def s(self, val: str):
        ...

    @property
    def _fields(self) -> IronPython.Runtime.PythonTuple:
        ...
    @_fields.setter
    def _fields(self, val: IronPython.Runtime.PythonTuple):
        ...

    @property
    def _attributes(self) -> IronPython.Runtime.PythonTuple:
        ...
    @_attributes.setter
    def _attributes(self, val: IronPython.Runtime.PythonTuple):
        ...

    @property
    def lineno(self) -> int:
        ...
    @lineno.setter
    def lineno(self, val: int):
        ...

    @property
    def col_offset(self) -> int:
        ...
    @col_offset.setter
    def col_offset(self, val: int):
        ...

    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def __init__(self, s: str, ):
        ...

    @typing.overload
    def __init__(self, s: str, lineno: System.Nullable[int], col_offset: System.Nullable[int], ):
        ...

    def Revert(self, ) -> IronPython.Compiler.Ast.Expression:
        ...

class Not(IronPython.Modules._ast.unaryop):
    @typing.overload
    def __init__(self, **kwargs):
        self._lineno: System.Nullable[int]
        self._col_offset: System.Nullable[int]
        ...

    # static fields
    Instance: IronPython.Modules._ast.Not = ...

    # properties
    @property
    def _fields(self) -> IronPython.Runtime.PythonTuple:
        ...
    @_fields.setter
    def _fields(self, val: IronPython.Runtime.PythonTuple):
        ...

    @property
    def _attributes(self) -> IronPython.Runtime.PythonTuple:
        ...
    @_attributes.setter
    def _attributes(self, val: IronPython.Runtime.PythonTuple):
        ...

    @property
    def lineno(self) -> int:
        ...
    @lineno.setter
    def lineno(self, val: int):
        ...

    @property
    def col_offset(self) -> int:
        ...
    @col_offset.setter
    def col_offset(self, val: int):
        ...

    # methods
    def __init__(self, ):
        ...

    def Revert(self, ) -> int:
        ...

class comprehension(IronPython.Modules._ast.AST):
    @typing.overload
    def __init__(self, **kwargs):
        self._lineno: System.Nullable[int]
        self._col_offset: System.Nullable[int]
        ...

    # static fields

    # properties
    @property
    def target(self) -> IronPython.Modules._ast.expr:
        ...
    @target.setter
    def target(self, val: IronPython.Modules._ast.expr):
        ...

    @property
    def iter(self) -> IronPython.Modules._ast.expr:
        ...
    @iter.setter
    def iter(self, val: IronPython.Modules._ast.expr):
        ...

    @property
    def ifs(self) -> IronPython.Runtime.PythonList:
        ...
    @ifs.setter
    def ifs(self, val: IronPython.Runtime.PythonList):
        ...

    @property
    def _fields(self) -> IronPython.Runtime.PythonTuple:
        ...
    @_fields.setter
    def _fields(self, val: IronPython.Runtime.PythonTuple):
        ...

    @property
    def _attributes(self) -> IronPython.Runtime.PythonTuple:
        ...
    @_attributes.setter
    def _attributes(self, val: IronPython.Runtime.PythonTuple):
        ...

    @property
    def lineno(self) -> int:
        ...
    @lineno.setter
    def lineno(self, val: int):
        ...

    @property
    def col_offset(self) -> int:
        ...
    @col_offset.setter
    def col_offset(self, val: int):
        ...

    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def __init__(self, target: IronPython.Modules._ast.expr, iter: IronPython.Modules._ast.expr, ifs: IronPython.Runtime.PythonList, ):
        ...

    @typing.overload
    def __init__(self, listFor: IronPython.Compiler.Ast.ComprehensionFor, listIfs: System.Array[IronPython.Compiler.Ast.ComprehensionIf], ):
        ...

    @staticmethod
    def RevertComprehensions(comprehensions: IronPython.Runtime.PythonList, ) -> System.Array[IronPython.Compiler.Ast.ComprehensionIterator]:
        ...

class LShift(IronPython.Modules._ast.operator):
    @typing.overload
    def __init__(self, **kwargs):
        self._lineno: System.Nullable[int]
        self._col_offset: System.Nullable[int]
        ...

    # static fields
    Instance: IronPython.Modules._ast.LShift = ...

    # properties
    @property
    def _fields(self) -> IronPython.Runtime.PythonTuple:
        ...
    @_fields.setter
    def _fields(self, val: IronPython.Runtime.PythonTuple):
        ...

    @property
    def _attributes(self) -> IronPython.Runtime.PythonTuple:
        ...
    @_attributes.setter
    def _attributes(self, val: IronPython.Runtime.PythonTuple):
        ...

    @property
    def lineno(self) -> int:
        ...
    @lineno.setter
    def lineno(self, val: int):
        ...

    @property
    def col_offset(self) -> int:
        ...
    @col_offset.setter
    def col_offset(self, val: int):
        ...

    # methods
    def __init__(self, ):
        ...

    def Revert(self, ) -> int:
        ...

class alias(IronPython.Modules._ast.AST):
    @typing.overload
    def __init__(self, **kwargs):
        self._lineno: System.Nullable[int]
        self._col_offset: System.Nullable[int]
        ...

    # static fields

    # properties
    @property
    def name(self) -> str:
        ...
    @name.setter
    def name(self, val: str):
        ...

    @property
    def asname(self) -> str:
        ...
    @asname.setter
    def asname(self, val: str):
        ...

    @property
    def _fields(self) -> IronPython.Runtime.PythonTuple:
        ...
    @_fields.setter
    def _fields(self, val: IronPython.Runtime.PythonTuple):
        ...

    @property
    def _attributes(self) -> IronPython.Runtime.PythonTuple:
        ...
    @_attributes.setter
    def _attributes(self, val: IronPython.Runtime.PythonTuple):
        ...

    @property
    def lineno(self) -> int:
        ...
    @lineno.setter
    def lineno(self, val: int):
        ...

    @property
    def col_offset(self) -> int:
        ...
    @col_offset.setter
    def col_offset(self, val: int):
        ...

    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def __init__(self, name: str, asname: str, ):
        ...

class Slice(IronPython.Modules._ast.slice):
    @typing.overload
    def __init__(self, **kwargs):
        self._lineno: System.Nullable[int]
        self._col_offset: System.Nullable[int]
        ...

    # static fields

    # properties
    @property
    def lower(self) -> IronPython.Modules._ast.expr:
        ...
    @lower.setter
    def lower(self, val: IronPython.Modules._ast.expr):
        ...

    @property
    def upper(self) -> IronPython.Modules._ast.expr:
        ...
    @upper.setter
    def upper(self, val: IronPython.Modules._ast.expr):
        ...

    @property
    def step(self) -> IronPython.Modules._ast.expr:
        ...
    @step.setter
    def step(self, val: IronPython.Modules._ast.expr):
        ...

    @property
    def _fields(self) -> IronPython.Runtime.PythonTuple:
        ...
    @_fields.setter
    def _fields(self, val: IronPython.Runtime.PythonTuple):
        ...

    @property
    def _attributes(self) -> IronPython.Runtime.PythonTuple:
        ...
    @_attributes.setter
    def _attributes(self, val: IronPython.Runtime.PythonTuple):
        ...

    @property
    def lineno(self) -> int:
        ...
    @lineno.setter
    def lineno(self, val: int):
        ...

    @property
    def col_offset(self) -> int:
        ...
    @col_offset.setter
    def col_offset(self, val: int):
        ...

    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def __init__(self, lower: IronPython.Modules._ast.expr, upper: IronPython.Modules._ast.expr, step: IronPython.Modules._ast.expr, ):
        ...

    @typing.overload
    def __init__(self, expr: IronPython.Compiler.Ast.SliceExpression, ):
        ...

class RShift(IronPython.Modules._ast.operator):
    @typing.overload
    def __init__(self, **kwargs):
        self._lineno: System.Nullable[int]
        self._col_offset: System.Nullable[int]
        ...

    # static fields
    Instance: IronPython.Modules._ast.RShift = ...

    # properties
    @property
    def _fields(self) -> IronPython.Runtime.PythonTuple:
        ...
    @_fields.setter
    def _fields(self, val: IronPython.Runtime.PythonTuple):
        ...

    @property
    def _attributes(self) -> IronPython.Runtime.PythonTuple:
        ...
    @_attributes.setter
    def _attributes(self, val: IronPython.Runtime.PythonTuple):
        ...

    @property
    def lineno(self) -> int:
        ...
    @lineno.setter
    def lineno(self, val: int):
        ...

    @property
    def col_offset(self) -> int:
        ...
    @col_offset.setter
    def col_offset(self, val: int):
        ...

    # methods
    def __init__(self, ):
        ...

    def Revert(self, ) -> int:
        ...

class UnaryOp(IronPython.Modules._ast.expr):
    @typing.overload
    def __init__(self, **kwargs):
        self._lineno: System.Nullable[int]
        self._col_offset: System.Nullable[int]
        ...

    # static fields

    # properties
    @property
    def op(self) -> IronPython.Modules._ast.unaryop:
        ...
    @op.setter
    def op(self, val: IronPython.Modules._ast.unaryop):
        ...

    @property
    def operand(self) -> IronPython.Modules._ast.expr:
        ...
    @operand.setter
    def operand(self, val: IronPython.Modules._ast.expr):
        ...

    @property
    def _fields(self) -> IronPython.Runtime.PythonTuple:
        ...
    @_fields.setter
    def _fields(self, val: IronPython.Runtime.PythonTuple):
        ...

    @property
    def _attributes(self) -> IronPython.Runtime.PythonTuple:
        ...
    @_attributes.setter
    def _attributes(self, val: IronPython.Runtime.PythonTuple):
        ...

    @property
    def lineno(self) -> int:
        ...
    @lineno.setter
    def lineno(self, val: int):
        ...

    @property
    def col_offset(self) -> int:
        ...
    @col_offset.setter
    def col_offset(self, val: int):
        ...

    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def __init__(self, expression: IronPython.Compiler.Ast.UnaryExpression, ):
        ...

    @typing.overload
    def __init__(self, op: IronPython.Modules._ast.unaryop, operand: IronPython.Modules._ast.expr, lineno: System.Nullable[int], col_offset: System.Nullable[int], ):
        ...

    def Revert(self, ) -> IronPython.Compiler.Ast.Expression:
        ...

    def TryTrimTrivialUnaryOp(self, ) -> IronPython.Modules._ast.expr:
        ...

class AugAssign(IronPython.Modules._ast.stmt):
    @typing.overload
    def __init__(self, **kwargs):
        self._lineno: System.Nullable[int]
        self._col_offset: System.Nullable[int]
        ...

    # static fields

    # properties
    @property
    def target(self) -> IronPython.Modules._ast.expr:
        ...
    @target.setter
    def target(self, val: IronPython.Modules._ast.expr):
        ...

    @property
    def op(self) -> IronPython.Modules._ast.operator:
        ...
    @op.setter
    def op(self, val: IronPython.Modules._ast.operator):
        ...

    @property
    def value(self) -> IronPython.Modules._ast.expr:
        ...
    @value.setter
    def value(self, val: IronPython.Modules._ast.expr):
        ...

    @property
    def _fields(self) -> IronPython.Runtime.PythonTuple:
        ...
    @_fields.setter
    def _fields(self, val: IronPython.Runtime.PythonTuple):
        ...

    @property
    def _attributes(self) -> IronPython.Runtime.PythonTuple:
        ...
    @_attributes.setter
    def _attributes(self, val: IronPython.Runtime.PythonTuple):
        ...

    @property
    def lineno(self) -> int:
        ...
    @lineno.setter
    def lineno(self, val: int):
        ...

    @property
    def col_offset(self) -> int:
        ...
    @col_offset.setter
    def col_offset(self, val: int):
        ...

    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def __init__(self, target: IronPython.Modules._ast.expr, op: IronPython.Modules._ast.operator, value: IronPython.Modules._ast.expr, lineno: System.Nullable[int], col_offset: System.Nullable[int], ):
        ...

    @typing.overload
    def __init__(self, stmt: IronPython.Compiler.Ast.AugmentedAssignStatement, ):
        ...

    def Revert(self, ) -> IronPython.Compiler.Ast.Statement:
        ...

class BitOr(IronPython.Modules._ast.operator):
    @typing.overload
    def __init__(self, **kwargs):
        self._lineno: System.Nullable[int]
        self._col_offset: System.Nullable[int]
        ...

    # static fields
    Instance: IronPython.Modules._ast.BitOr = ...

    # properties
    @property
    def _fields(self) -> IronPython.Runtime.PythonTuple:
        ...
    @_fields.setter
    def _fields(self, val: IronPython.Runtime.PythonTuple):
        ...

    @property
    def _attributes(self) -> IronPython.Runtime.PythonTuple:
        ...
    @_attributes.setter
    def _attributes(self, val: IronPython.Runtime.PythonTuple):
        ...

    @property
    def lineno(self) -> int:
        ...
    @lineno.setter
    def lineno(self, val: int):
        ...

    @property
    def col_offset(self) -> int:
        ...
    @col_offset.setter
    def col_offset(self, val: int):
        ...

    # methods
    def __init__(self, ):
        ...

    def Revert(self, ) -> int:
        ...

class Raise(IronPython.Modules._ast.stmt):
    @typing.overload
    def __init__(self, **kwargs):
        self._lineno: System.Nullable[int]
        self._col_offset: System.Nullable[int]
        ...

    # static fields

    # properties
    @property
    def exc(self) -> IronPython.Modules._ast.expr:
        ...
    @exc.setter
    def exc(self, val: IronPython.Modules._ast.expr):
        ...

    @property
    def cause(self) -> IronPython.Modules._ast.expr:
        ...
    @cause.setter
    def cause(self, val: IronPython.Modules._ast.expr):
        ...

    @property
    def _fields(self) -> IronPython.Runtime.PythonTuple:
        ...
    @_fields.setter
    def _fields(self, val: IronPython.Runtime.PythonTuple):
        ...

    @property
    def _attributes(self) -> IronPython.Runtime.PythonTuple:
        ...
    @_attributes.setter
    def _attributes(self, val: IronPython.Runtime.PythonTuple):
        ...

    @property
    def lineno(self) -> int:
        ...
    @lineno.setter
    def lineno(self, val: int):
        ...

    @property
    def col_offset(self) -> int:
        ...
    @col_offset.setter
    def col_offset(self, val: int):
        ...

    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def __init__(self, exc: IronPython.Modules._ast.expr, cause: IronPython.Modules._ast.expr, lineno: System.Nullable[int], col_offset: System.Nullable[int], ):
        ...

    @typing.overload
    def __init__(self, stmt: IronPython.Compiler.Ast.RaiseStatement, ):
        ...

    def Revert(self, ) -> IronPython.Compiler.Ast.Statement:
        ...

class expr(IronPython.Modules._ast.AST, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        self._lineno: System.Nullable[int]
        self._col_offset: System.Nullable[int]
        ...

    # static fields

    # properties
    @property
    def _fields(self) -> IronPython.Runtime.PythonTuple:
        ...
    @_fields.setter
    def _fields(self, val: IronPython.Runtime.PythonTuple):
        ...

    @property
    def _attributes(self) -> IronPython.Runtime.PythonTuple:
        ...
    @_attributes.setter
    def _attributes(self, val: IronPython.Runtime.PythonTuple):
        ...

    @property
    def lineno(self) -> int:
        ...
    @lineno.setter
    def lineno(self, val: int):
        ...

    @property
    def col_offset(self) -> int:
        ...
    @col_offset.setter
    def col_offset(self, val: int):
        ...

    # methods
    def __init__(self, ):
        ...

    @typing.overload
    def Revert(self, ) -> IronPython.Compiler.Ast.Expression:
        ...

    @staticmethod
    @typing.overload
    def Revert(ex: IronPython.Modules._ast.expr, ) -> IronPython.Compiler.Ast.Expression:
        ...

    @staticmethod
    @typing.overload
    def Revert(ex: System.Object, ) -> IronPython.Compiler.Ast.Expression:
        ...

    @staticmethod
    def RevertExprs(exprs: IronPython.Runtime.PythonList, ) -> System.Array[IronPython.Compiler.Ast.Expression]:
        ...

class Pass(IronPython.Modules._ast.stmt):
    @typing.overload
    def __init__(self, **kwargs):
        self._lineno: System.Nullable[int]
        self._col_offset: System.Nullable[int]
        ...

    # static fields
    Instance: IronPython.Modules._ast.Pass = ...

    # properties
    @property
    def _fields(self) -> IronPython.Runtime.PythonTuple:
        ...
    @_fields.setter
    def _fields(self, val: IronPython.Runtime.PythonTuple):
        ...

    @property
    def _attributes(self) -> IronPython.Runtime.PythonTuple:
        ...
    @_attributes.setter
    def _attributes(self, val: IronPython.Runtime.PythonTuple):
        ...

    @property
    def lineno(self) -> int:
        ...
    @lineno.setter
    def lineno(self, val: int):
        ...

    @property
    def col_offset(self) -> int:
        ...
    @col_offset.setter
    def col_offset(self, val: int):
        ...

    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def __init__(self, lineno: System.Nullable[int], col_offset: System.Nullable[int], ):
        ...

    def Revert(self, ) -> IronPython.Compiler.Ast.Statement:
        ...

class Is(IronPython.Modules._ast.cmpop):
    @typing.overload
    def __init__(self, **kwargs):
        self._lineno: System.Nullable[int]
        self._col_offset: System.Nullable[int]
        ...

    # static fields
    Instance: IronPython.Modules._ast.Is = ...

    # properties
    @property
    def _fields(self) -> IronPython.Runtime.PythonTuple:
        ...
    @_fields.setter
    def _fields(self, val: IronPython.Runtime.PythonTuple):
        ...

    @property
    def _attributes(self) -> IronPython.Runtime.PythonTuple:
        ...
    @_attributes.setter
    def _attributes(self, val: IronPython.Runtime.PythonTuple):
        ...

    @property
    def lineno(self) -> int:
        ...
    @lineno.setter
    def lineno(self, val: int):
        ...

    @property
    def col_offset(self) -> int:
        ...
    @col_offset.setter
    def col_offset(self, val: int):
        ...

    # methods
    def __init__(self, ):
        ...

    def Revert(self, ) -> int:
        ...

class unaryop(IronPython.Modules._ast.AST, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        self._lineno: System.Nullable[int]
        self._col_offset: System.Nullable[int]
        ...

    # static fields

    # properties
    @property
    def _fields(self) -> IronPython.Runtime.PythonTuple:
        ...
    @_fields.setter
    def _fields(self, val: IronPython.Runtime.PythonTuple):
        ...

    @property
    def _attributes(self) -> IronPython.Runtime.PythonTuple:
        ...
    @_attributes.setter
    def _attributes(self, val: IronPython.Runtime.PythonTuple):
        ...

    @property
    def lineno(self) -> int:
        ...
    @lineno.setter
    def lineno(self, val: int):
        ...

    @property
    def col_offset(self) -> int:
        ...
    @col_offset.setter
    def col_offset(self, val: int):
        ...

    # methods
    def __init__(self, ):
        ...

    @abc.abstractmethod
    def Revert(self, ) -> int:
        ...

