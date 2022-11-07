from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import System.Linq.Expressions
import IronPython.Compiler.Ast


class LookupVisitor(System.Linq.Expressions.ExpressionVisitor):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    def __init__(self, ast: IronPython.Compiler.Ast.PythonAst, globalContext: System.Linq.Expressions.Expression, ):
        ...

    def VisitMember(self, node: System.Linq.Expressions.MemberExpression, ) -> System.Linq.Expressions.Expression:
        ...

    def VisitExtension(self, node: System.Linq.Expressions.Expression, ) -> System.Linq.Expressions.Expression:
        ...

    def VisitScope(self, scope: IronPython.Compiler.Ast.ScopeStatement, ) -> IronPython.Compiler.Ast.ScopeStatement:
        ...

    def VisitComprehension(self, comprehension: IronPython.Compiler.Ast.Comprehension, ) -> System.Linq.Expressions.Expression:
        ...

    def VisitExtensionInScope(self, node: System.Linq.Expressions.Expression, scope: IronPython.Compiler.Ast.ScopeStatement, ) -> System.Linq.Expressions.Expression:
        ...

