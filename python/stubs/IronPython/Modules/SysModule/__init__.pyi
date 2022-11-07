from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import System.Collections
import System.Collections.Generic
import System
import IronPython.Runtime
import Microsoft.Scripting.Runtime
import Interop.Kernel32
import IronPython.Modules.SysModule


class intinfo(System.Collections.IList, System.Collections.ICollection, System.Collections.IEnumerable, System.Collections.Generic.IList[System.Object], System.Collections.Generic.ICollection[System.Object], System.Collections.Generic.IEnumerable[System.Object], IronPython.Runtime.ICodeFormattable, Microsoft.Scripting.Runtime.IExpressionSerializable, System.Collections.IStructuralEquatable, System.Collections.Generic.IReadOnlyList[System.Object], System.Collections.Generic.IReadOnlyCollection[System.Object], IronPython.Runtime.PythonTuple):
    @typing.overload
    def __init__(self, **kwargs):
        self.bits_per_digit: int
        self.sizeof_digit: int
        self._data: System.Array[System.Object]
        ...

    # static fields
    n_fields: int = ...
    n_sequence_fields: int = ...
    n_unnamed_fields: int = ...

    # properties
    @property
    def Item(self) -> System.Object:
        ...

    @property
    def Item(self) -> System.Object:
        ...

    @property
    def Item(self) -> System.Object:
        ...

    @property
    def Item(self) -> System.Object:
        ...

    @property
    def Count(self) -> int:
        ...

    # methods
    def __init__(self, bits_per_digit: int, sizeof_digit: int, ):
        ...

    def __repr__(self, context: IronPython.Runtime.CodeContext, ) -> str:
        ...

class SysFlags(System.Collections.IList, System.Collections.ICollection, System.Collections.IEnumerable, System.Collections.Generic.IList[System.Object], System.Collections.Generic.ICollection[System.Object], System.Collections.Generic.IEnumerable[System.Object], IronPython.Runtime.ICodeFormattable, Microsoft.Scripting.Runtime.IExpressionSerializable, System.Collections.IStructuralEquatable, System.Collections.Generic.IReadOnlyList[System.Object], System.Collections.Generic.IReadOnlyCollection[System.Object], IronPython.Runtime.PythonTuple):
    @typing.overload
    def __init__(self, **kwargs):
        self._data: System.Array[System.Object]
        ...

    # static fields
    n_fields: int = ...
    n_sequence_fields: int = ...
    n_unnamed_fields: int = ...

    # properties
    @property
    def debug(self) -> int:
        ...
    @debug.setter
    def debug(self, val: int):
        ...

    @property
    def inspect(self) -> int:
        ...
    @inspect.setter
    def inspect(self, val: int):
        ...

    @property
    def interactive(self) -> int:
        ...
    @interactive.setter
    def interactive(self, val: int):
        ...

    @property
    def optimize(self) -> int:
        ...
    @optimize.setter
    def optimize(self, val: int):
        ...

    @property
    def dont_write_bytecode(self) -> int:
        ...
    @dont_write_bytecode.setter
    def dont_write_bytecode(self, val: int):
        ...

    @property
    def no_user_site(self) -> int:
        ...
    @no_user_site.setter
    def no_user_site(self, val: int):
        ...

    @property
    def no_site(self) -> int:
        ...
    @no_site.setter
    def no_site(self, val: int):
        ...

    @property
    def ignore_environment(self) -> int:
        ...
    @ignore_environment.setter
    def ignore_environment(self, val: int):
        ...

    @property
    def verbose(self) -> int:
        ...
    @verbose.setter
    def verbose(self, val: int):
        ...

    @property
    def bytes_warning(self) -> int:
        ...
    @bytes_warning.setter
    def bytes_warning(self, val: int):
        ...

    @property
    def quiet(self) -> int:
        ...
    @quiet.setter
    def quiet(self, val: int):
        ...

    @property
    def hash_randomization(self) -> int:
        ...
    @hash_randomization.setter
    def hash_randomization(self, val: int):
        ...

    @property
    def isolated(self) -> int:
        ...
    @isolated.setter
    def isolated(self, val: int):
        ...

    @property
    def Item(self) -> System.Object:
        ...

    @property
    def Item(self) -> System.Object:
        ...

    @property
    def Item(self) -> System.Object:
        ...

    @property
    def Item(self) -> System.Object:
        ...

    @property
    def Count(self) -> int:
        ...

    # methods
    def __init__(self, ):
        ...

    def __repr__(self, context: IronPython.Runtime.CodeContext, ) -> str:
        ...

class windows_version(System.Collections.IList, System.Collections.ICollection, System.Collections.IEnumerable, System.Collections.Generic.IList[System.Object], System.Collections.Generic.ICollection[System.Object], System.Collections.Generic.IEnumerable[System.Object], IronPython.Runtime.ICodeFormattable, Microsoft.Scripting.Runtime.IExpressionSerializable, System.Collections.IStructuralEquatable, System.Collections.Generic.IReadOnlyList[System.Object], System.Collections.Generic.IReadOnlyCollection[System.Object], IronPython.Runtime.PythonTuple):
    @typing.overload
    def __init__(self, **kwargs):
        self.major: int
        self.minor: int
        self.build: int
        self.platform: int
        self.service_pack: str
        self.product_type: int
        self.service_pack_major: int
        self.service_pack_minor: int
        self.suite_mask: int
        self.platform_version: IronPython.Runtime.PythonTuple
        self._data: System.Array[System.Object]
        ...

    # static fields
    n_fields: int = ...
    n_sequence_fields: int = ...
    n_unnamed_fields: int = ...

    # properties
    @property
    def _platform_version(self) -> IronPython.Runtime.PythonTuple:
        ...

    @property
    def Item(self) -> System.Object:
        ...

    @property
    def Item(self) -> System.Object:
        ...

    @property
    def Item(self) -> System.Object:
        ...

    @property
    def Item(self) -> System.Object:
        ...

    @property
    def Count(self) -> int:
        ...

    # methods
    @typing.overload
    def __init__(self, version: Interop.Kernel32.OSVERSIONINFOEX, ):
        ...

    @typing.overload
    def __init__(self, major: int, minor: int, build: int, platform: int, service_pack: str, ):
        ...

    @staticmethod
    def GetWindowsVersion() -> IronPython.Modules.SysModule.windows_version:
        ...

    def __repr__(self, context: IronPython.Runtime.CodeContext, ) -> str:
        ...

class hashinfo(System.Collections.IList, System.Collections.ICollection, System.Collections.IEnumerable, System.Collections.Generic.IList[System.Object], System.Collections.Generic.ICollection[System.Object], System.Collections.Generic.IEnumerable[System.Object], IronPython.Runtime.ICodeFormattable, Microsoft.Scripting.Runtime.IExpressionSerializable, System.Collections.IStructuralEquatable, System.Collections.Generic.IReadOnlyList[System.Object], System.Collections.Generic.IReadOnlyCollection[System.Object], IronPython.Runtime.PythonTuple):
    @typing.overload
    def __init__(self, **kwargs):
        self.width: int
        self.modulus: int
        self.inf: int
        self.nan: int
        self.imag: int
        self.algorithm: str
        self.hash_bits: int
        self.seed_bits: int
        self.cutoff: int
        self._data: System.Array[System.Object]
        ...

    # static fields
    n_fields: int = ...
    n_sequence_fields: int = ...
    n_unnamed_fields: int = ...

    # properties
    @property
    def Item(self) -> System.Object:
        ...

    @property
    def Item(self) -> System.Object:
        ...

    @property
    def Item(self) -> System.Object:
        ...

    @property
    def Item(self) -> System.Object:
        ...

    @property
    def Count(self) -> int:
        ...

    # methods
    def __init__(self, width: int, modulus: int, inf: int, nan: int, imag: int, algorithm: str, hash_bits: int, seed_bits: int, cutoff: int, ):
        ...

    def __repr__(self, context: IronPython.Runtime.CodeContext, ) -> str:
        ...

class floatinfo(System.Collections.IList, System.Collections.ICollection, System.Collections.IEnumerable, System.Collections.Generic.IList[System.Object], System.Collections.Generic.ICollection[System.Object], System.Collections.Generic.IEnumerable[System.Object], IronPython.Runtime.ICodeFormattable, Microsoft.Scripting.Runtime.IExpressionSerializable, System.Collections.IStructuralEquatable, System.Collections.Generic.IReadOnlyList[System.Object], System.Collections.Generic.IReadOnlyCollection[System.Object], IronPython.Runtime.PythonTuple):
    @typing.overload
    def __init__(self, **kwargs):
        self.max: float
        self.max_exp: int
        self.max_10_exp: int
        self.min: float
        self.min_exp: int
        self.min_10_exp: int
        self.dig: int
        self.mant_dig: int
        self.epsilon: float
        self.radix: int
        self.rounds: int
        self._data: System.Array[System.Object]
        ...

    # static fields
    n_fields: int = ...
    n_sequence_fields: int = ...
    n_unnamed_fields: int = ...

    # properties
    @property
    def Item(self) -> System.Object:
        ...

    @property
    def Item(self) -> System.Object:
        ...

    @property
    def Item(self) -> System.Object:
        ...

    @property
    def Item(self) -> System.Object:
        ...

    @property
    def Count(self) -> int:
        ...

    # methods
    def __init__(self, max: float, max_exp: int, max_10_exp: int, min: float, min_exp: int, min_10_exp: int, dig: int, mant_dig: int, epsilon: float, radix: int, rounds: int, ):
        ...

    def __repr__(self, context: IronPython.Runtime.CodeContext, ) -> str:
        ...

