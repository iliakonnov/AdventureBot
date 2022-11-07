from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import System
import System.Diagnostics
import System.Text
import System.Reflection


class Stopwatch(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields
    Frequency: int = ...
    IsHighResolution: bool = ...

    # properties
    @property
    def IsRunning(self) -> bool:
        ...

    @property
    def Elapsed(self) -> System.TimeSpan:
        ...

    @property
    def ElapsedMilliseconds(self) -> int:
        ...

    @property
    def ElapsedTicks(self) -> int:
        ...

    # methods
    def __init__(self, ):
        ...

    def Start(self, ) -> None:
        ...

    @staticmethod
    def StartNew() -> System.Diagnostics.Stopwatch:
        ...

    def Stop(self, ) -> None:
        ...

    def Reset(self, ) -> None:
        ...

    def Restart(self, ) -> None:
        ...

    @staticmethod
    def GetTimestamp() -> int:
        ...

    def GetRawElapsedTicks(self, ) -> int:
        ...

    def GetElapsedDateTimeTicks(self, ) -> int:
        ...

    @staticmethod
    def QueryPerformanceFrequency() -> int:
        ...

    @staticmethod
    def QueryPerformanceCounter() -> int:
        ...

class StackFrame(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields
    OFFSET_UNKNOWN: int = ...

    # properties
    @property
    def IsLastFrameFromForeignExceptionStackTrace(self) -> bool:
        ...

    # methods
    @typing.overload
    def __init__(self, stackFrameHelper: System.Diagnostics.StackFrameHelper, skipFrames: int, needFileInfo: bool, ):
        ...

    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def __init__(self, needFileInfo: bool, ):
        ...

    @typing.overload
    def __init__(self, skipFrames: int, ):
        ...

    @typing.overload
    def __init__(self, skipFrames: int, needFileInfo: bool, ):
        ...

    @typing.overload
    def __init__(self, fileName: str, lineNumber: int, ):
        ...

    @typing.overload
    def __init__(self, fileName: str, lineNumber: int, colNumber: int, ):
        ...

    def BuildStackFrame(self, skipFrames: int, needFileInfo: bool, ) -> None:
        ...

    @staticmethod
    def AppendStackFrameWithoutMethodBase(sb: System.Text.StringBuilder, ) -> bool:
        ...

    @staticmethod
    def GetMethodFromNativeIP(ip: System.IntPtr, ) -> System.Reflection.MethodBase:
        ...

    def InitMembers(self, ) -> None:
        ...

    def GetMethod(self, ) -> System.Reflection.MethodBase:
        ...

    def GetNativeOffset(self, ) -> int:
        ...

    def GetILOffset(self, ) -> int:
        ...

    def GetFileName(self, ) -> str:
        ...

    def GetFileLineNumber(self, ) -> int:
        ...

    def GetFileColumnNumber(self, ) -> int:
        ...

    def ToString(self, ) -> str:
        ...

