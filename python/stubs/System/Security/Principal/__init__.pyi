from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import System.Security.Principal
import System


class IPrincipal(abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    @abc.abstractmethod
    def Identity(self) -> System.Security.Principal.IIdentity:
        ...

    # methods
    @abc.abstractmethod
    def IsInRole(self, role: str, ) -> bool:
        ...

class PrincipalPolicy(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    UnauthenticatedPrincipal: int = ...
    NoPrincipal: int = ...
    WindowsPrincipal: int = ...

class IIdentity(abc.ABC):
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
    def AuthenticationType(self) -> str:
        ...

    @property
    @abc.abstractmethod
    def IsAuthenticated(self) -> bool:
        ...

    # methods
