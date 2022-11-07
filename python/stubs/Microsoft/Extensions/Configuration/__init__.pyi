from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import Microsoft.Extensions.Configuration
import System.Collections.Generic
import Microsoft.Extensions.Primitives


class IConfigurationRoot(Microsoft.Extensions.Configuration.IConfiguration, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    @abc.abstractmethod
    def Providers(self) -> System.Collections.Generic.IEnumerable[Microsoft.Extensions.Configuration.IConfigurationProvider]:
        ...

    # methods
    @abc.abstractmethod
    def Reload(self, ) -> None:
        ...

class IConfigurationProvider(abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    @abc.abstractmethod
    def TryGet(self, key: str, value: ref[str], ) -> bool:
        ...

    @abc.abstractmethod
    def Set(self, key: str, value: str, ) -> None:
        ...

    @abc.abstractmethod
    def GetReloadToken(self, ) -> Microsoft.Extensions.Primitives.IChangeToken:
        ...

    @abc.abstractmethod
    def Load(self, ) -> None:
        ...

    @abc.abstractmethod
    def GetChildKeys(self, earlierKeys: System.Collections.Generic.IEnumerable[str], parentPath: str, ) -> System.Collections.Generic.IEnumerable[str]:
        ...

class IConfiguration(abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    @abc.abstractmethod
    def Item(self) -> str:
        ...
    @Item.setter
    @abc.abstractmethod
    def Item(self, val: str):
        ...

    # methods
    @abc.abstractmethod
    def GetSection(self, key: str, ) -> Microsoft.Extensions.Configuration.IConfigurationSection:
        ...

    @abc.abstractmethod
    def GetChildren(self, ) -> System.Collections.Generic.IEnumerable[Microsoft.Extensions.Configuration.IConfigurationSection]:
        ...

    @abc.abstractmethod
    def GetReloadToken(self, ) -> Microsoft.Extensions.Primitives.IChangeToken:
        ...

class IConfigurationSection(Microsoft.Extensions.Configuration.IConfiguration, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    @abc.abstractmethod
    def Key(self) -> str:
        ...

    @property
    @abc.abstractmethod
    def Path(self) -> str:
        ...

    @property
    @abc.abstractmethod
    def Value(self) -> str:
        ...
    @Value.setter
    @abc.abstractmethod
    def Value(self, val: str):
        ...

    # methods
