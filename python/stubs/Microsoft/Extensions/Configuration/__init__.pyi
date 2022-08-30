from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import Microsoft.Extensions.Configuration
import System.Collections.Generic
import System
import Microsoft.Extensions.Primitives


class IConfigurationRoot(Microsoft.Extensions.Configuration.IConfiguration, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @abc.abstractmethod
    @property
    def Providers(self) -> System.Collections.Generic.IEnumerable[Microsoft.Extensions.Configuration.IConfigurationProvider]:
        ...

    # methods
    @typing.overload
    @abc.abstractmethod
    def Reload(self, ) -> None:
        ...

class IConfiguration(abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @abc.abstractmethod
    @property
    def Item(self) -> System.String:
        ...
    @abc.abstractmethod
    @Item.setter
    def Item(self, val: System.String):
        ...

    # methods
    @typing.overload
    @abc.abstractmethod
    def GetSection(self, key: System.String, ) -> Microsoft.Extensions.Configuration.IConfigurationSection:
        ...

    @typing.overload
    @abc.abstractmethod
    def GetChildren(self, ) -> System.Collections.Generic.IEnumerable[Microsoft.Extensions.Configuration.IConfigurationSection]:
        ...

    @typing.overload
    @abc.abstractmethod
    def GetReloadToken(self, ) -> Microsoft.Extensions.Primitives.IChangeToken:
        ...

class IConfigurationProvider(abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    # methods
    @typing.overload
    @abc.abstractmethod
    def TryGet(self, key: System.String, value: ref[System.String], ) -> System.Boolean:
        ...

    @typing.overload
    @abc.abstractmethod
    def Set(self, key: System.String, value: System.String, ) -> None:
        ...

    @typing.overload
    @abc.abstractmethod
    def GetReloadToken(self, ) -> Microsoft.Extensions.Primitives.IChangeToken:
        ...

    @typing.overload
    @abc.abstractmethod
    def Load(self, ) -> None:
        ...

    @typing.overload
    @abc.abstractmethod
    def GetChildKeys(self, earlierKeys: System.Collections.Generic.IEnumerable[System.String], parentPath: System.String, ) -> System.Collections.Generic.IEnumerable[System.String]:
        ...

class IConfigurationSection(Microsoft.Extensions.Configuration.IConfiguration, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @abc.abstractmethod
    @property
    def Key(self) -> System.String:
        ...

    @abc.abstractmethod
    @property
    def Path(self) -> System.String:
        ...

    @abc.abstractmethod
    @property
    def Value(self) -> System.String:
        ...
    @abc.abstractmethod
    @Value.setter
    def Value(self, val: System.String):
        ...

    # methods
