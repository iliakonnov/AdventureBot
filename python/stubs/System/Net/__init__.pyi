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

    # properties
    # methods
    @typing.overload
    @abc.abstractmethod
    def GetCredential(self, uri: System.Uri, authType: System.String, ) -> System.Net.NetworkCredential:
        ...

class NetworkCredential(System.Net.ICredentials, System.Net.ICredentialsByHost, System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def UserName(self) -> System.String:
        ...
    @UserName.setter
    def UserName(self, val: System.String):
        ...

    @property
    def Password(self) -> System.String:
        ...
    @Password.setter
    def Password(self, val: System.String):
        ...

    @property
    def SecurePassword(self) -> System.Security.SecureString:
        ...
    @SecurePassword.setter
    def SecurePassword(self, val: System.Security.SecureString):
        ...

    @property
    def Domain(self) -> System.String:
        ...
    @Domain.setter
    def Domain(self, val: System.String):
        ...

    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def __init__(self, userName: System.String, password: System.String, ):
        ...

    @typing.overload
    def __init__(self, userName: System.String, password: System.String, domain: System.String, ):
        ...

    @typing.overload
    def __init__(self, userName: System.String, password: System.Security.SecureString, ):
        ...

    @typing.overload
    def __init__(self, userName: System.String, password: System.Security.SecureString, domain: System.String, ):
        ...

    @typing.overload
    def GetCredential(self, uri: System.Uri, authenticationType: System.String, ) -> System.Net.NetworkCredential:
        ...

    @typing.overload
    def GetCredential(self, host: System.String, port: System.Int32, authenticationType: System.String, ) -> System.Net.NetworkCredential:
        ...

class ICredentialsByHost(abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    # methods
    @typing.overload
    @abc.abstractmethod
    def GetCredential(self, host: System.String, port: System.Int32, authenticationType: System.String, ) -> System.Net.NetworkCredential:
        ...

