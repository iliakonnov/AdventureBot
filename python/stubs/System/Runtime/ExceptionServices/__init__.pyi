from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import System
import System.Runtime.ExceptionServices


class ExceptionDispatchInfo(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def SourceException(self) -> System.Exception:
        ...

    # methods
    def __init__(self, exception: System.Exception, ):
        ...

    @staticmethod
    def Capture(source: System.Exception, ) -> System.Runtime.ExceptionServices.ExceptionDispatchInfo:
        ...

    @typing.overload
    def Throw(self, ) -> None:
        ...

    @staticmethod
    @typing.overload
    def Throw(source: System.Exception, ) -> None:
        ...

    @staticmethod
    def SetCurrentStackTrace(source: System.Exception, ) -> System.Exception:
        ...

    @staticmethod
    def SetRemoteStackTrace(source: System.Exception, stackTrace: str, ) -> System.Exception:
        ...

