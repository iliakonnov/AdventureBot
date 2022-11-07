from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import System
import System.Data


class BatchCommandInfo(System.ValueType):
    @typing.overload
    def __init__(self, **kwargs):
        self._commandIdentifier: int
        self._parameterCount: int
        self._row: System.Data.DataRow
        self._statementType: int
        self._updatedRowSource: int
        self._recordsAffected: System.Nullable[int]
        self._errors: System.Exception
        ...

    # static fields

    # properties
    # methods
