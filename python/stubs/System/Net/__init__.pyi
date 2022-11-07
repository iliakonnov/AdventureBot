from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import System
import System.Net
import System.Security


class ICredentials(abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    @abc.abstractmethod
    def GetCredential(self, uri: System.Uri, authType: str, ) -> System.Net.NetworkCredential:
        ...

class NetworkCredential(System.Net.ICredentials, System.Net.ICredentialsByHost, System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def UserName(self) -> str:
        ...
    @UserName.setter
    def UserName(self, val: str):
        ...

    @property
    def Password(self) -> str:
        ...
    @Password.setter
    def Password(self, val: str):
        ...

    @property
    def SecurePassword(self) -> System.Security.SecureString:
        ...
    @SecurePassword.setter
    def SecurePassword(self, val: System.Security.SecureString):
        ...

    @property
    def Domain(self) -> str:
        ...
    @Domain.setter
    def Domain(self, val: str):
        ...

    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def __init__(self, userName: str, password: str, ):
        ...

    @typing.overload
    def __init__(self, userName: str, password: str, domain: str, ):
        ...

    @typing.overload
    def __init__(self, userName: str, password: System.Security.SecureString, ):
        ...

    @typing.overload
    def __init__(self, userName: str, password: System.Security.SecureString, domain: str, ):
        ...

    @typing.overload
    def GetCredential(self, uri: System.Uri, authenticationType: str, ) -> System.Net.NetworkCredential:
        ...

    @typing.overload
    def GetCredential(self, host: str, port: int, authenticationType: str, ) -> System.Net.NetworkCredential:
        ...

    def MarshalToString(self, sstr: System.Security.SecureString, ) -> str:
        ...

    def MarshalToSecureString(self, str: str, ) -> System.Security.SecureString:
        ...

class ICredentialsByHost(abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    @abc.abstractmethod
    def GetCredential(self, host: str, port: int, authenticationType: str, ) -> System.Net.NetworkCredential:
        ...

