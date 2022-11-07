from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import System.Runtime.Serialization
import IronPython.Runtime.Exceptions
import System
import IronPython.Runtime.Exceptions.PythonExceptions
import System.Collections.Generic
import Microsoft.Scripting.Runtime
import System.Reflection
import System.Collections
import System.ComponentModel
import IronPython.Runtime.Types
import IronPython.Runtime
import Microsoft.Scripting
import IronPython.Runtime.Operations


class FloatingPointException(System.Runtime.Serialization.ISerializable, IronPython.Runtime.Exceptions.IPythonAwareException, System.Exception):
    @typing.overload
    def __init__(self, **kwargs):
        self._message: str
        ...

    # static fields

    # properties
    @property
    def PythonException(self) -> IronPython.Runtime.Exceptions.PythonExceptions.BaseException:
        ...
    @PythonException.setter
    def PythonException(self, val: IronPython.Runtime.Exceptions.PythonExceptions.BaseException):
        ...

    @property
    def Frames(self) -> System.Collections.Generic.List[Microsoft.Scripting.Runtime.DynamicStackFrame]:
        ...
    @Frames.setter
    def Frames(self, val: System.Collections.Generic.List[Microsoft.Scripting.Runtime.DynamicStackFrame]):
        ...

    @property
    def TraceBack(self) -> IronPython.Runtime.Exceptions.TraceBack:
        ...
    @TraceBack.setter
    def TraceBack(self, val: IronPython.Runtime.Exceptions.TraceBack):
        ...

    @property
    def TargetSite(self) -> System.Reflection.MethodBase:
        ...

    @property
    def Message(self) -> str:
        ...

    @property
    def Data(self) -> System.Collections.IDictionary:
        ...

    @property
    def InnerException(self) -> System.Exception:
        ...

    @property
    def HelpLink(self) -> str:
        ...
    @HelpLink.setter
    def HelpLink(self, val: str):
        ...

    @property
    def Source(self) -> str:
        ...
    @Source.setter
    def Source(self, val: str):
        ...

    @property
    def HResult(self) -> int:
        ...
    @HResult.setter
    def HResult(self, val: int):
        ...

    @property
    def StackTrace(self) -> str:
        ...

    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def __init__(self, msg: str, ):
        ...

    @typing.overload
    def __init__(self, message: str, innerException: System.Exception, ):
        ...

    @typing.overload
    def __init__(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext, ):
        ...

    def GetObjectData(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext, ) -> None:
        ...

class BlockingIOException(System.Runtime.Serialization.ISerializable, IronPython.Runtime.Exceptions.IPythonAwareException, IronPython.Runtime.Exceptions.OSException):
    @typing.overload
    def __init__(self, **kwargs):
        self._message: str
        ...

    # static fields

    # properties
    @property
    def PythonException(self) -> IronPython.Runtime.Exceptions.PythonExceptions.BaseException:
        ...
    @PythonException.setter
    def PythonException(self, val: IronPython.Runtime.Exceptions.PythonExceptions.BaseException):
        ...

    @property
    def Frames(self) -> System.Collections.Generic.List[Microsoft.Scripting.Runtime.DynamicStackFrame]:
        ...
    @Frames.setter
    def Frames(self, val: System.Collections.Generic.List[Microsoft.Scripting.Runtime.DynamicStackFrame]):
        ...

    @property
    def TraceBack(self) -> IronPython.Runtime.Exceptions.TraceBack:
        ...
    @TraceBack.setter
    def TraceBack(self, val: IronPython.Runtime.Exceptions.TraceBack):
        ...

    @property
    def TargetSite(self) -> System.Reflection.MethodBase:
        ...

    @property
    def Message(self) -> str:
        ...

    @property
    def Data(self) -> System.Collections.IDictionary:
        ...

    @property
    def InnerException(self) -> System.Exception:
        ...

    @property
    def HelpLink(self) -> str:
        ...
    @HelpLink.setter
    def HelpLink(self, val: str):
        ...

    @property
    def Source(self) -> str:
        ...
    @Source.setter
    def Source(self, val: str):
        ...

    @property
    def HResult(self) -> int:
        ...
    @HResult.setter
    def HResult(self, val: int):
        ...

    @property
    def StackTrace(self) -> str:
        ...

    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def __init__(self, msg: str, ):
        ...

    @typing.overload
    def __init__(self, message: str, innerException: System.Exception, ):
        ...

    @typing.overload
    def __init__(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext, ):
        ...

    def GetObjectData(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext, ) -> None:
        ...

class FutureWarningException(System.Runtime.Serialization.ISerializable, IronPython.Runtime.Exceptions.IPythonAwareException, System.ComponentModel.WarningException):
    @typing.overload
    def __init__(self, **kwargs):
        self._message: str
        ...

    # static fields

    # properties
    @property
    def PythonException(self) -> IronPython.Runtime.Exceptions.PythonExceptions.BaseException:
        ...
    @PythonException.setter
    def PythonException(self, val: IronPython.Runtime.Exceptions.PythonExceptions.BaseException):
        ...

    @property
    def Frames(self) -> System.Collections.Generic.List[Microsoft.Scripting.Runtime.DynamicStackFrame]:
        ...
    @Frames.setter
    def Frames(self, val: System.Collections.Generic.List[Microsoft.Scripting.Runtime.DynamicStackFrame]):
        ...

    @property
    def TraceBack(self) -> IronPython.Runtime.Exceptions.TraceBack:
        ...
    @TraceBack.setter
    def TraceBack(self, val: IronPython.Runtime.Exceptions.TraceBack):
        ...

    @property
    def HelpUrl(self) -> str:
        ...

    @property
    def HelpTopic(self) -> str:
        ...

    @property
    def TargetSite(self) -> System.Reflection.MethodBase:
        ...

    @property
    def Message(self) -> str:
        ...

    @property
    def Data(self) -> System.Collections.IDictionary:
        ...

    @property
    def InnerException(self) -> System.Exception:
        ...

    @property
    def HelpLink(self) -> str:
        ...
    @HelpLink.setter
    def HelpLink(self, val: str):
        ...

    @property
    def Source(self) -> str:
        ...
    @Source.setter
    def Source(self, val: str):
        ...

    @property
    def HResult(self) -> int:
        ...
    @HResult.setter
    def HResult(self, val: int):
        ...

    @property
    def StackTrace(self) -> str:
        ...

    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def __init__(self, msg: str, ):
        ...

    @typing.overload
    def __init__(self, message: str, innerException: System.Exception, ):
        ...

    @typing.overload
    def __init__(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext, ):
        ...

    def GetObjectData(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext, ) -> None:
        ...

class UnicodeTranslateException(System.Runtime.Serialization.ISerializable, IronPython.Runtime.Exceptions.IPythonAwareException, IronPython.Runtime.Exceptions.UnicodeException):
    @typing.overload
    def __init__(self, **kwargs):
        self._message: str
        ...

    # static fields

    # properties
    @property
    def PythonException(self) -> IronPython.Runtime.Exceptions.PythonExceptions.BaseException:
        ...
    @PythonException.setter
    def PythonException(self, val: IronPython.Runtime.Exceptions.PythonExceptions.BaseException):
        ...

    @property
    def Frames(self) -> System.Collections.Generic.List[Microsoft.Scripting.Runtime.DynamicStackFrame]:
        ...
    @Frames.setter
    def Frames(self, val: System.Collections.Generic.List[Microsoft.Scripting.Runtime.DynamicStackFrame]):
        ...

    @property
    def TraceBack(self) -> IronPython.Runtime.Exceptions.TraceBack:
        ...
    @TraceBack.setter
    def TraceBack(self, val: IronPython.Runtime.Exceptions.TraceBack):
        ...

    @property
    def TargetSite(self) -> System.Reflection.MethodBase:
        ...

    @property
    def Message(self) -> str:
        ...

    @property
    def Data(self) -> System.Collections.IDictionary:
        ...

    @property
    def InnerException(self) -> System.Exception:
        ...

    @property
    def HelpLink(self) -> str:
        ...
    @HelpLink.setter
    def HelpLink(self, val: str):
        ...

    @property
    def Source(self) -> str:
        ...
    @Source.setter
    def Source(self, val: str):
        ...

    @property
    def HResult(self) -> int:
        ...
    @HResult.setter
    def HResult(self, val: int):
        ...

    @property
    def StackTrace(self) -> str:
        ...

    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def __init__(self, msg: str, ):
        ...

    @typing.overload
    def __init__(self, message: str, innerException: System.Exception, ):
        ...

    @typing.overload
    def __init__(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext, ):
        ...

    def GetObjectData(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext, ) -> None:
        ...

class PythonExceptions(System.Object, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields
    DefaultExceptionModule: str = ...
    __doc__: str = ...

    # properties
    @property
    def SystemExit(self) -> IronPython.Runtime.Types.PythonType:
        ...

    @property
    def KeyboardInterrupt(self) -> IronPython.Runtime.Types.PythonType:
        ...

    @property
    def GeneratorExit(self) -> IronPython.Runtime.Types.PythonType:
        ...

    @property
    def Exception(self) -> IronPython.Runtime.Types.PythonType:
        ...

    @property
    def StopIteration(self) -> IronPython.Runtime.Types.PythonType:
        ...

    @property
    def StopAsyncIteration(self) -> IronPython.Runtime.Types.PythonType:
        ...

    @property
    def ArithmeticError(self) -> IronPython.Runtime.Types.PythonType:
        ...

    @property
    def FloatingPointError(self) -> IronPython.Runtime.Types.PythonType:
        ...

    @property
    def OverflowError(self) -> IronPython.Runtime.Types.PythonType:
        ...

    @property
    def ZeroDivisionError(self) -> IronPython.Runtime.Types.PythonType:
        ...

    @property
    def AssertionError(self) -> IronPython.Runtime.Types.PythonType:
        ...

    @property
    def AttributeError(self) -> IronPython.Runtime.Types.PythonType:
        ...

    @property
    def BufferError(self) -> IronPython.Runtime.Types.PythonType:
        ...

    @property
    def EOFError(self) -> IronPython.Runtime.Types.PythonType:
        ...

    @property
    def ImportError(self) -> IronPython.Runtime.Types.PythonType:
        ...

    @property
    def LookupError(self) -> IronPython.Runtime.Types.PythonType:
        ...

    @property
    def IndexError(self) -> IronPython.Runtime.Types.PythonType:
        ...

    @property
    def KeyError(self) -> IronPython.Runtime.Types.PythonType:
        ...

    @property
    def MemoryError(self) -> IronPython.Runtime.Types.PythonType:
        ...

    @property
    def NameError(self) -> IronPython.Runtime.Types.PythonType:
        ...

    @property
    def UnboundLocalError(self) -> IronPython.Runtime.Types.PythonType:
        ...

    @property
    def OSError(self) -> IronPython.Runtime.Types.PythonType:
        ...

    @property
    def BlockingIOError(self) -> IronPython.Runtime.Types.PythonType:
        ...

    @property
    def ChildProcessError(self) -> IronPython.Runtime.Types.PythonType:
        ...

    @property
    def ConnectionError(self) -> IronPython.Runtime.Types.PythonType:
        ...

    @property
    def BrokenPipeError(self) -> IronPython.Runtime.Types.PythonType:
        ...

    @property
    def ConnectionAbortedError(self) -> IronPython.Runtime.Types.PythonType:
        ...

    @property
    def ConnectionRefusedError(self) -> IronPython.Runtime.Types.PythonType:
        ...

    @property
    def ConnectionResetError(self) -> IronPython.Runtime.Types.PythonType:
        ...

    @property
    def FileExistsError(self) -> IronPython.Runtime.Types.PythonType:
        ...

    @property
    def FileNotFoundError(self) -> IronPython.Runtime.Types.PythonType:
        ...

    @property
    def InterruptedError(self) -> IronPython.Runtime.Types.PythonType:
        ...

    @property
    def IsADirectoryError(self) -> IronPython.Runtime.Types.PythonType:
        ...

    @property
    def NotADirectoryError(self) -> IronPython.Runtime.Types.PythonType:
        ...

    @property
    def PermissionError(self) -> IronPython.Runtime.Types.PythonType:
        ...

    @property
    def ProcessLookupError(self) -> IronPython.Runtime.Types.PythonType:
        ...

    @property
    def TimeoutError(self) -> IronPython.Runtime.Types.PythonType:
        ...

    @property
    def ReferenceError(self) -> IronPython.Runtime.Types.PythonType:
        ...

    @property
    def RuntimeError(self) -> IronPython.Runtime.Types.PythonType:
        ...

    @property
    def NotImplementedError(self) -> IronPython.Runtime.Types.PythonType:
        ...

    @property
    def RecursionError(self) -> IronPython.Runtime.Types.PythonType:
        ...

    @property
    def SyntaxError(self) -> IronPython.Runtime.Types.PythonType:
        ...

    @property
    def IndentationError(self) -> IronPython.Runtime.Types.PythonType:
        ...

    @property
    def TabError(self) -> IronPython.Runtime.Types.PythonType:
        ...

    @property
    def SystemError(self) -> IronPython.Runtime.Types.PythonType:
        ...

    @property
    def TypeError(self) -> IronPython.Runtime.Types.PythonType:
        ...

    @property
    def ValueError(self) -> IronPython.Runtime.Types.PythonType:
        ...

    @property
    def UnicodeError(self) -> IronPython.Runtime.Types.PythonType:
        ...

    @property
    def UnicodeDecodeError(self) -> IronPython.Runtime.Types.PythonType:
        ...

    @property
    def UnicodeEncodeError(self) -> IronPython.Runtime.Types.PythonType:
        ...

    @property
    def UnicodeTranslateError(self) -> IronPython.Runtime.Types.PythonType:
        ...

    @property
    def Warning(self) -> IronPython.Runtime.Types.PythonType:
        ...

    @property
    def DeprecationWarning(self) -> IronPython.Runtime.Types.PythonType:
        ...

    @property
    def PendingDeprecationWarning(self) -> IronPython.Runtime.Types.PythonType:
        ...

    @property
    def RuntimeWarning(self) -> IronPython.Runtime.Types.PythonType:
        ...

    @property
    def SyntaxWarning(self) -> IronPython.Runtime.Types.PythonType:
        ...

    @property
    def UserWarning(self) -> IronPython.Runtime.Types.PythonType:
        ...

    @property
    def FutureWarning(self) -> IronPython.Runtime.Types.PythonType:
        ...

    @property
    def ImportWarning(self) -> IronPython.Runtime.Types.PythonType:
        ...

    @property
    def UnicodeWarning(self) -> IronPython.Runtime.Types.PythonType:
        ...

    @property
    def BytesWarning(self) -> IronPython.Runtime.Types.PythonType:
        ...

    @property
    def ResourceWarning(self) -> IronPython.Runtime.Types.PythonType:
        ...

    # methods
    @staticmethod
    def CreateThrowable(type: IronPython.Runtime.Types.PythonType, args: System.Array[System.Object], ) -> System.Exception:
        ...

    @staticmethod
    def CreatePythonThrowable(type: IronPython.Runtime.Types.PythonType, args: System.Array[System.Object], ) -> IronPython.Runtime.Exceptions.PythonExceptions.BaseException:
        ...

    @staticmethod
    def CreateBaseExceptionForRaise(context: IronPython.Runtime.CodeContext, type: IronPython.Runtime.Types.PythonType, value: System.Object, ) -> IronPython.Runtime.Exceptions.PythonExceptions.BaseException:
        ...

    @staticmethod
    def ToClr(pythonException: System.Object, ) -> System.Exception:
        ...

    @staticmethod
    def ToPython(clrException: System.Exception, ) -> System.Object:
        ...

    @staticmethod
    def ToPythonNewStyle(clrException: System.Exception, ) -> IronPython.Runtime.Exceptions.PythonExceptions.BaseException:
        ...

    @staticmethod
    def SetPythonException(e: System.Exception, exception: IronPython.Runtime.Exceptions.PythonExceptions.BaseException, ) -> None:
        ...

    @staticmethod
    def GetPythonException(e: System.Exception, ) -> IronPython.Runtime.Exceptions.PythonExceptions.BaseException:
        ...

    @staticmethod
    def GetFrameList(e: System.Exception, ) -> System.Collections.Generic.List[Microsoft.Scripting.Runtime.DynamicStackFrame]:
        ...

    @staticmethod
    def SetFrameList(e: System.Exception, frames: System.Collections.Generic.List[Microsoft.Scripting.Runtime.DynamicStackFrame], ) -> None:
        ...

    @staticmethod
    def RemoveFrameList(e: System.Exception, ) -> None:
        ...

    @staticmethod
    def GetTraceBack(e: System.Exception, ) -> IronPython.Runtime.Exceptions.TraceBack:
        ...

    @staticmethod
    def SetTraceBack(e: System.Exception, traceback: IronPython.Runtime.Exceptions.TraceBack, ) -> None:
        ...

    @staticmethod
    def RemoveTraceBack(e: System.Exception, ) -> None:
        ...

    @staticmethod
    def SyntaxErrorToPython(e: Microsoft.Scripting.SyntaxErrorException, ) -> IronPython.Runtime.Exceptions.PythonExceptions.BaseException:
        ...

    @staticmethod
    @typing.overload
    def CreateSubType(context: IronPython.Runtime.PythonContext, baseType: IronPython.Runtime.Types.PythonType, name: str, module: str, documentation: str, exceptionMaker: System.Func[str, System.Exception, System.Exception], ) -> IronPython.Runtime.Types.PythonType:
        ...

    @staticmethod
    @typing.overload
    def CreateSubType(context: IronPython.Runtime.PythonContext, baseType: IronPython.Runtime.Types.PythonType, underlyingType: System.Type, name: str, module: str, documentation: str, exceptionMaker: System.Func[str, System.Exception, System.Exception], ) -> IronPython.Runtime.Types.PythonType:
        ...

    @staticmethod
    @typing.overload
    def CreateSubType(context: IronPython.Runtime.PythonContext, baseTypes: System.Array[IronPython.Runtime.Types.PythonType], underlyingType: System.Type, name: str, module: str, documentation: str, exceptionMaker: System.Func[str, System.Exception, System.Exception], ) -> IronPython.Runtime.Types.PythonType:
        ...

    @staticmethod
    @typing.overload
    def CreateSubType(baseType: IronPython.Runtime.Types.PythonType, name: str, exceptionMaker: System.Func[str, System.Exception, System.Exception], ) -> IronPython.Runtime.Types.PythonType:
        ...

    @staticmethod
    @typing.overload
    def CreateSubType(baseType: IronPython.Runtime.Types.PythonType, concreteType: System.Type, exceptionMaker: System.Func[str, System.Exception, System.Exception], ) -> IronPython.Runtime.Types.PythonType:
        ...

    @staticmethod
    def GetDynamicStackFrames(e: System.Exception, ) -> System.Array[Microsoft.Scripting.Runtime.DynamicStackFrame]:
        ...

    @staticmethod
    def MethodsMatch(method: System.Reflection.MethodBase, other: System.Reflection.MethodBase, ) -> bool:
        ...

    @staticmethod
    def ToPythonHelper(clrException: System.Exception, ) -> IronPython.Runtime.Exceptions.PythonExceptions.BaseException:
        ...

class ProcessLookupException(System.Runtime.Serialization.ISerializable, IronPython.Runtime.Exceptions.IPythonAwareException, IronPython.Runtime.Exceptions.OSException):
    @typing.overload
    def __init__(self, **kwargs):
        self._message: str
        ...

    # static fields

    # properties
    @property
    def PythonException(self) -> IronPython.Runtime.Exceptions.PythonExceptions.BaseException:
        ...
    @PythonException.setter
    def PythonException(self, val: IronPython.Runtime.Exceptions.PythonExceptions.BaseException):
        ...

    @property
    def Frames(self) -> System.Collections.Generic.List[Microsoft.Scripting.Runtime.DynamicStackFrame]:
        ...
    @Frames.setter
    def Frames(self, val: System.Collections.Generic.List[Microsoft.Scripting.Runtime.DynamicStackFrame]):
        ...

    @property
    def TraceBack(self) -> IronPython.Runtime.Exceptions.TraceBack:
        ...
    @TraceBack.setter
    def TraceBack(self, val: IronPython.Runtime.Exceptions.TraceBack):
        ...

    @property
    def TargetSite(self) -> System.Reflection.MethodBase:
        ...

    @property
    def Message(self) -> str:
        ...

    @property
    def Data(self) -> System.Collections.IDictionary:
        ...

    @property
    def InnerException(self) -> System.Exception:
        ...

    @property
    def HelpLink(self) -> str:
        ...
    @HelpLink.setter
    def HelpLink(self, val: str):
        ...

    @property
    def Source(self) -> str:
        ...
    @Source.setter
    def Source(self, val: str):
        ...

    @property
    def HResult(self) -> int:
        ...
    @HResult.setter
    def HResult(self, val: int):
        ...

    @property
    def StackTrace(self) -> str:
        ...

    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def __init__(self, msg: str, ):
        ...

    @typing.overload
    def __init__(self, message: str, innerException: System.Exception, ):
        ...

    @typing.overload
    def __init__(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext, ):
        ...

    def GetObjectData(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext, ) -> None:
        ...

class RecursionException(System.Runtime.Serialization.ISerializable, IronPython.Runtime.Exceptions.IPythonAwareException, IronPython.Runtime.Exceptions.RuntimeException):
    @typing.overload
    def __init__(self, **kwargs):
        self._message: str
        ...

    # static fields

    # properties
    @property
    def PythonException(self) -> IronPython.Runtime.Exceptions.PythonExceptions.BaseException:
        ...
    @PythonException.setter
    def PythonException(self, val: IronPython.Runtime.Exceptions.PythonExceptions.BaseException):
        ...

    @property
    def Frames(self) -> System.Collections.Generic.List[Microsoft.Scripting.Runtime.DynamicStackFrame]:
        ...
    @Frames.setter
    def Frames(self, val: System.Collections.Generic.List[Microsoft.Scripting.Runtime.DynamicStackFrame]):
        ...

    @property
    def TraceBack(self) -> IronPython.Runtime.Exceptions.TraceBack:
        ...
    @TraceBack.setter
    def TraceBack(self, val: IronPython.Runtime.Exceptions.TraceBack):
        ...

    @property
    def TargetSite(self) -> System.Reflection.MethodBase:
        ...

    @property
    def Message(self) -> str:
        ...

    @property
    def Data(self) -> System.Collections.IDictionary:
        ...

    @property
    def InnerException(self) -> System.Exception:
        ...

    @property
    def HelpLink(self) -> str:
        ...
    @HelpLink.setter
    def HelpLink(self, val: str):
        ...

    @property
    def Source(self) -> str:
        ...
    @Source.setter
    def Source(self, val: str):
        ...

    @property
    def HResult(self) -> int:
        ...
    @HResult.setter
    def HResult(self, val: int):
        ...

    @property
    def StackTrace(self) -> str:
        ...

    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def __init__(self, msg: str, ):
        ...

    @typing.overload
    def __init__(self, message: str, innerException: System.Exception, ):
        ...

    @typing.overload
    def __init__(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext, ):
        ...

    def GetObjectData(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext, ) -> None:
        ...

class ConnectionResetException(System.Runtime.Serialization.ISerializable, IronPython.Runtime.Exceptions.IPythonAwareException, IronPython.Runtime.Exceptions.ConnectionException):
    @typing.overload
    def __init__(self, **kwargs):
        self._message: str
        ...

    # static fields

    # properties
    @property
    def PythonException(self) -> IronPython.Runtime.Exceptions.PythonExceptions.BaseException:
        ...
    @PythonException.setter
    def PythonException(self, val: IronPython.Runtime.Exceptions.PythonExceptions.BaseException):
        ...

    @property
    def Frames(self) -> System.Collections.Generic.List[Microsoft.Scripting.Runtime.DynamicStackFrame]:
        ...
    @Frames.setter
    def Frames(self, val: System.Collections.Generic.List[Microsoft.Scripting.Runtime.DynamicStackFrame]):
        ...

    @property
    def TraceBack(self) -> IronPython.Runtime.Exceptions.TraceBack:
        ...
    @TraceBack.setter
    def TraceBack(self, val: IronPython.Runtime.Exceptions.TraceBack):
        ...

    @property
    def TargetSite(self) -> System.Reflection.MethodBase:
        ...

    @property
    def Message(self) -> str:
        ...

    @property
    def Data(self) -> System.Collections.IDictionary:
        ...

    @property
    def InnerException(self) -> System.Exception:
        ...

    @property
    def HelpLink(self) -> str:
        ...
    @HelpLink.setter
    def HelpLink(self, val: str):
        ...

    @property
    def Source(self) -> str:
        ...
    @Source.setter
    def Source(self, val: str):
        ...

    @property
    def HResult(self) -> int:
        ...
    @HResult.setter
    def HResult(self, val: int):
        ...

    @property
    def StackTrace(self) -> str:
        ...

    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def __init__(self, msg: str, ):
        ...

    @typing.overload
    def __init__(self, message: str, innerException: System.Exception, ):
        ...

    @typing.overload
    def __init__(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext, ):
        ...

    def GetObjectData(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext, ) -> None:
        ...

class TraceBack(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def tb_next(self) -> IronPython.Runtime.Exceptions.TraceBack:
        ...

    @property
    def tb_frame(self) -> IronPython.Runtime.Exceptions.TraceBackFrame:
        ...

    @property
    def tb_lineno(self) -> int:
        ...

    @property
    def tb_lasti(self) -> int:
        ...

    # methods
    def __init__(self, nextTraceBack: IronPython.Runtime.Exceptions.TraceBack, fromFrame: IronPython.Runtime.Exceptions.TraceBackFrame, ):
        ...

    def SetLine(self, lineNumber: int, ) -> None:
        ...

    def Extract(self, ) -> str:
        ...

class FileExistsException(System.Runtime.Serialization.ISerializable, IronPython.Runtime.Exceptions.IPythonAwareException, IronPython.Runtime.Exceptions.OSException):
    @typing.overload
    def __init__(self, **kwargs):
        self._message: str
        ...

    # static fields

    # properties
    @property
    def PythonException(self) -> IronPython.Runtime.Exceptions.PythonExceptions.BaseException:
        ...
    @PythonException.setter
    def PythonException(self, val: IronPython.Runtime.Exceptions.PythonExceptions.BaseException):
        ...

    @property
    def Frames(self) -> System.Collections.Generic.List[Microsoft.Scripting.Runtime.DynamicStackFrame]:
        ...
    @Frames.setter
    def Frames(self, val: System.Collections.Generic.List[Microsoft.Scripting.Runtime.DynamicStackFrame]):
        ...

    @property
    def TraceBack(self) -> IronPython.Runtime.Exceptions.TraceBack:
        ...
    @TraceBack.setter
    def TraceBack(self, val: IronPython.Runtime.Exceptions.TraceBack):
        ...

    @property
    def TargetSite(self) -> System.Reflection.MethodBase:
        ...

    @property
    def Message(self) -> str:
        ...

    @property
    def Data(self) -> System.Collections.IDictionary:
        ...

    @property
    def InnerException(self) -> System.Exception:
        ...

    @property
    def HelpLink(self) -> str:
        ...
    @HelpLink.setter
    def HelpLink(self, val: str):
        ...

    @property
    def Source(self) -> str:
        ...
    @Source.setter
    def Source(self, val: str):
        ...

    @property
    def HResult(self) -> int:
        ...
    @HResult.setter
    def HResult(self, val: int):
        ...

    @property
    def StackTrace(self) -> str:
        ...

    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def __init__(self, msg: str, ):
        ...

    @typing.overload
    def __init__(self, message: str, innerException: System.Exception, ):
        ...

    @typing.overload
    def __init__(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext, ):
        ...

    def GetObjectData(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext, ) -> None:
        ...

class SystemExitException(System.Runtime.Serialization.ISerializable, System.Exception):
    @typing.overload
    def __init__(self, **kwargs):
        self._message: str
        ...

    # static fields

    # properties
    @property
    def TargetSite(self) -> System.Reflection.MethodBase:
        ...

    @property
    def Message(self) -> str:
        ...

    @property
    def Data(self) -> System.Collections.IDictionary:
        ...

    @property
    def InnerException(self) -> System.Exception:
        ...

    @property
    def HelpLink(self) -> str:
        ...
    @HelpLink.setter
    def HelpLink(self, val: str):
        ...

    @property
    def Source(self) -> str:
        ...
    @Source.setter
    def Source(self, val: str):
        ...

    @property
    def HResult(self) -> int:
        ...
    @HResult.setter
    def HResult(self, val: int):
        ...

    @property
    def StackTrace(self) -> str:
        ...

    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def __init__(self, msg: str, ):
        ...

    @typing.overload
    def __init__(self, message: str, innerException: System.Exception, ):
        ...

    @typing.overload
    def __init__(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext, ):
        ...

    def GetExitCode(self, otherCode: ref[System.Object], ) -> int:
        ...

class RuntimeException(System.Runtime.Serialization.ISerializable, IronPython.Runtime.Exceptions.IPythonAwareException, System.Exception):
    @typing.overload
    def __init__(self, **kwargs):
        self._message: str
        ...

    # static fields

    # properties
    @property
    def PythonException(self) -> IronPython.Runtime.Exceptions.PythonExceptions.BaseException:
        ...
    @PythonException.setter
    def PythonException(self, val: IronPython.Runtime.Exceptions.PythonExceptions.BaseException):
        ...

    @property
    def Frames(self) -> System.Collections.Generic.List[Microsoft.Scripting.Runtime.DynamicStackFrame]:
        ...
    @Frames.setter
    def Frames(self, val: System.Collections.Generic.List[Microsoft.Scripting.Runtime.DynamicStackFrame]):
        ...

    @property
    def TraceBack(self) -> IronPython.Runtime.Exceptions.TraceBack:
        ...
    @TraceBack.setter
    def TraceBack(self, val: IronPython.Runtime.Exceptions.TraceBack):
        ...

    @property
    def TargetSite(self) -> System.Reflection.MethodBase:
        ...

    @property
    def Message(self) -> str:
        ...

    @property
    def Data(self) -> System.Collections.IDictionary:
        ...

    @property
    def InnerException(self) -> System.Exception:
        ...

    @property
    def HelpLink(self) -> str:
        ...
    @HelpLink.setter
    def HelpLink(self, val: str):
        ...

    @property
    def Source(self) -> str:
        ...
    @Source.setter
    def Source(self, val: str):
        ...

    @property
    def HResult(self) -> int:
        ...
    @HResult.setter
    def HResult(self, val: int):
        ...

    @property
    def StackTrace(self) -> str:
        ...

    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def __init__(self, msg: str, ):
        ...

    @typing.overload
    def __init__(self, message: str, innerException: System.Exception, ):
        ...

    @typing.overload
    def __init__(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext, ):
        ...

    def GetObjectData(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext, ) -> None:
        ...

class InterruptedException(System.Runtime.Serialization.ISerializable, IronPython.Runtime.Exceptions.IPythonAwareException, IronPython.Runtime.Exceptions.OSException):
    @typing.overload
    def __init__(self, **kwargs):
        self._message: str
        ...

    # static fields

    # properties
    @property
    def PythonException(self) -> IronPython.Runtime.Exceptions.PythonExceptions.BaseException:
        ...
    @PythonException.setter
    def PythonException(self, val: IronPython.Runtime.Exceptions.PythonExceptions.BaseException):
        ...

    @property
    def Frames(self) -> System.Collections.Generic.List[Microsoft.Scripting.Runtime.DynamicStackFrame]:
        ...
    @Frames.setter
    def Frames(self, val: System.Collections.Generic.List[Microsoft.Scripting.Runtime.DynamicStackFrame]):
        ...

    @property
    def TraceBack(self) -> IronPython.Runtime.Exceptions.TraceBack:
        ...
    @TraceBack.setter
    def TraceBack(self, val: IronPython.Runtime.Exceptions.TraceBack):
        ...

    @property
    def TargetSite(self) -> System.Reflection.MethodBase:
        ...

    @property
    def Message(self) -> str:
        ...

    @property
    def Data(self) -> System.Collections.IDictionary:
        ...

    @property
    def InnerException(self) -> System.Exception:
        ...

    @property
    def HelpLink(self) -> str:
        ...
    @HelpLink.setter
    def HelpLink(self, val: str):
        ...

    @property
    def Source(self) -> str:
        ...
    @Source.setter
    def Source(self, val: str):
        ...

    @property
    def HResult(self) -> int:
        ...
    @HResult.setter
    def HResult(self, val: int):
        ...

    @property
    def StackTrace(self) -> str:
        ...

    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def __init__(self, msg: str, ):
        ...

    @typing.overload
    def __init__(self, message: str, innerException: System.Exception, ):
        ...

    @typing.overload
    def __init__(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext, ):
        ...

    def GetObjectData(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext, ) -> None:
        ...

class BytesWarningException(System.Runtime.Serialization.ISerializable, IronPython.Runtime.Exceptions.IPythonAwareException, System.ComponentModel.WarningException):
    @typing.overload
    def __init__(self, **kwargs):
        self._message: str
        ...

    # static fields

    # properties
    @property
    def PythonException(self) -> IronPython.Runtime.Exceptions.PythonExceptions.BaseException:
        ...
    @PythonException.setter
    def PythonException(self, val: IronPython.Runtime.Exceptions.PythonExceptions.BaseException):
        ...

    @property
    def Frames(self) -> System.Collections.Generic.List[Microsoft.Scripting.Runtime.DynamicStackFrame]:
        ...
    @Frames.setter
    def Frames(self, val: System.Collections.Generic.List[Microsoft.Scripting.Runtime.DynamicStackFrame]):
        ...

    @property
    def TraceBack(self) -> IronPython.Runtime.Exceptions.TraceBack:
        ...
    @TraceBack.setter
    def TraceBack(self, val: IronPython.Runtime.Exceptions.TraceBack):
        ...

    @property
    def HelpUrl(self) -> str:
        ...

    @property
    def HelpTopic(self) -> str:
        ...

    @property
    def TargetSite(self) -> System.Reflection.MethodBase:
        ...

    @property
    def Message(self) -> str:
        ...

    @property
    def Data(self) -> System.Collections.IDictionary:
        ...

    @property
    def InnerException(self) -> System.Exception:
        ...

    @property
    def HelpLink(self) -> str:
        ...
    @HelpLink.setter
    def HelpLink(self, val: str):
        ...

    @property
    def Source(self) -> str:
        ...
    @Source.setter
    def Source(self, val: str):
        ...

    @property
    def HResult(self) -> int:
        ...
    @HResult.setter
    def HResult(self, val: int):
        ...

    @property
    def StackTrace(self) -> str:
        ...

    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def __init__(self, msg: str, ):
        ...

    @typing.overload
    def __init__(self, message: str, innerException: System.Exception, ):
        ...

    @typing.overload
    def __init__(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext, ):
        ...

    def GetObjectData(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext, ) -> None:
        ...

class AssertionException(System.Runtime.Serialization.ISerializable, IronPython.Runtime.Exceptions.IPythonAwareException, System.Exception):
    @typing.overload
    def __init__(self, **kwargs):
        self._message: str
        ...

    # static fields

    # properties
    @property
    def PythonException(self) -> IronPython.Runtime.Exceptions.PythonExceptions.BaseException:
        ...
    @PythonException.setter
    def PythonException(self, val: IronPython.Runtime.Exceptions.PythonExceptions.BaseException):
        ...

    @property
    def Frames(self) -> System.Collections.Generic.List[Microsoft.Scripting.Runtime.DynamicStackFrame]:
        ...
    @Frames.setter
    def Frames(self, val: System.Collections.Generic.List[Microsoft.Scripting.Runtime.DynamicStackFrame]):
        ...

    @property
    def TraceBack(self) -> IronPython.Runtime.Exceptions.TraceBack:
        ...
    @TraceBack.setter
    def TraceBack(self, val: IronPython.Runtime.Exceptions.TraceBack):
        ...

    @property
    def TargetSite(self) -> System.Reflection.MethodBase:
        ...

    @property
    def Message(self) -> str:
        ...

    @property
    def Data(self) -> System.Collections.IDictionary:
        ...

    @property
    def InnerException(self) -> System.Exception:
        ...

    @property
    def HelpLink(self) -> str:
        ...
    @HelpLink.setter
    def HelpLink(self, val: str):
        ...

    @property
    def Source(self) -> str:
        ...
    @Source.setter
    def Source(self, val: str):
        ...

    @property
    def HResult(self) -> int:
        ...
    @HResult.setter
    def HResult(self, val: int):
        ...

    @property
    def StackTrace(self) -> str:
        ...

    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def __init__(self, msg: str, ):
        ...

    @typing.overload
    def __init__(self, message: str, innerException: System.Exception, ):
        ...

    @typing.overload
    def __init__(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext, ):
        ...

    def GetObjectData(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext, ) -> None:
        ...

class ImportWarningException(System.Runtime.Serialization.ISerializable, IronPython.Runtime.Exceptions.IPythonAwareException, System.ComponentModel.WarningException):
    @typing.overload
    def __init__(self, **kwargs):
        self._message: str
        ...

    # static fields

    # properties
    @property
    def PythonException(self) -> IronPython.Runtime.Exceptions.PythonExceptions.BaseException:
        ...
    @PythonException.setter
    def PythonException(self, val: IronPython.Runtime.Exceptions.PythonExceptions.BaseException):
        ...

    @property
    def Frames(self) -> System.Collections.Generic.List[Microsoft.Scripting.Runtime.DynamicStackFrame]:
        ...
    @Frames.setter
    def Frames(self, val: System.Collections.Generic.List[Microsoft.Scripting.Runtime.DynamicStackFrame]):
        ...

    @property
    def TraceBack(self) -> IronPython.Runtime.Exceptions.TraceBack:
        ...
    @TraceBack.setter
    def TraceBack(self, val: IronPython.Runtime.Exceptions.TraceBack):
        ...

    @property
    def HelpUrl(self) -> str:
        ...

    @property
    def HelpTopic(self) -> str:
        ...

    @property
    def TargetSite(self) -> System.Reflection.MethodBase:
        ...

    @property
    def Message(self) -> str:
        ...

    @property
    def Data(self) -> System.Collections.IDictionary:
        ...

    @property
    def InnerException(self) -> System.Exception:
        ...

    @property
    def HelpLink(self) -> str:
        ...
    @HelpLink.setter
    def HelpLink(self, val: str):
        ...

    @property
    def Source(self) -> str:
        ...
    @Source.setter
    def Source(self, val: str):
        ...

    @property
    def HResult(self) -> int:
        ...
    @HResult.setter
    def HResult(self, val: int):
        ...

    @property
    def StackTrace(self) -> str:
        ...

    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def __init__(self, msg: str, ):
        ...

    @typing.overload
    def __init__(self, message: str, innerException: System.Exception, ):
        ...

    @typing.overload
    def __init__(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext, ):
        ...

    def GetObjectData(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext, ) -> None:
        ...

class ChildProcessException(System.Runtime.Serialization.ISerializable, IronPython.Runtime.Exceptions.IPythonAwareException, IronPython.Runtime.Exceptions.OSException):
    @typing.overload
    def __init__(self, **kwargs):
        self._message: str
        ...

    # static fields

    # properties
    @property
    def PythonException(self) -> IronPython.Runtime.Exceptions.PythonExceptions.BaseException:
        ...
    @PythonException.setter
    def PythonException(self, val: IronPython.Runtime.Exceptions.PythonExceptions.BaseException):
        ...

    @property
    def Frames(self) -> System.Collections.Generic.List[Microsoft.Scripting.Runtime.DynamicStackFrame]:
        ...
    @Frames.setter
    def Frames(self, val: System.Collections.Generic.List[Microsoft.Scripting.Runtime.DynamicStackFrame]):
        ...

    @property
    def TraceBack(self) -> IronPython.Runtime.Exceptions.TraceBack:
        ...
    @TraceBack.setter
    def TraceBack(self, val: IronPython.Runtime.Exceptions.TraceBack):
        ...

    @property
    def TargetSite(self) -> System.Reflection.MethodBase:
        ...

    @property
    def Message(self) -> str:
        ...

    @property
    def Data(self) -> System.Collections.IDictionary:
        ...

    @property
    def InnerException(self) -> System.Exception:
        ...

    @property
    def HelpLink(self) -> str:
        ...
    @HelpLink.setter
    def HelpLink(self, val: str):
        ...

    @property
    def Source(self) -> str:
        ...
    @Source.setter
    def Source(self, val: str):
        ...

    @property
    def HResult(self) -> int:
        ...
    @HResult.setter
    def HResult(self, val: int):
        ...

    @property
    def StackTrace(self) -> str:
        ...

    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def __init__(self, msg: str, ):
        ...

    @typing.overload
    def __init__(self, message: str, innerException: System.Exception, ):
        ...

    @typing.overload
    def __init__(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext, ):
        ...

    def GetObjectData(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext, ) -> None:
        ...

class ValueErrorException(System.Runtime.Serialization.ISerializable, IronPython.Runtime.Exceptions.IPythonAwareException, System.ArgumentException):
    @typing.overload
    def __init__(self, **kwargs):
        self._message: str
        ...

    # static fields

    # properties
    @property
    def PythonException(self) -> IronPython.Runtime.Exceptions.PythonExceptions.BaseException:
        ...
    @PythonException.setter
    def PythonException(self, val: IronPython.Runtime.Exceptions.PythonExceptions.BaseException):
        ...

    @property
    def Frames(self) -> System.Collections.Generic.List[Microsoft.Scripting.Runtime.DynamicStackFrame]:
        ...
    @Frames.setter
    def Frames(self, val: System.Collections.Generic.List[Microsoft.Scripting.Runtime.DynamicStackFrame]):
        ...

    @property
    def TraceBack(self) -> IronPython.Runtime.Exceptions.TraceBack:
        ...
    @TraceBack.setter
    def TraceBack(self, val: IronPython.Runtime.Exceptions.TraceBack):
        ...

    @property
    def Message(self) -> str:
        ...

    @property
    def ParamName(self) -> str:
        ...

    @property
    def TargetSite(self) -> System.Reflection.MethodBase:
        ...

    @property
    def Data(self) -> System.Collections.IDictionary:
        ...

    @property
    def InnerException(self) -> System.Exception:
        ...

    @property
    def HelpLink(self) -> str:
        ...
    @HelpLink.setter
    def HelpLink(self, val: str):
        ...

    @property
    def Source(self) -> str:
        ...
    @Source.setter
    def Source(self, val: str):
        ...

    @property
    def HResult(self) -> int:
        ...
    @HResult.setter
    def HResult(self, val: int):
        ...

    @property
    def StackTrace(self) -> str:
        ...

    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def __init__(self, msg: str, ):
        ...

    @typing.overload
    def __init__(self, message: str, innerException: System.Exception, ):
        ...

    @typing.overload
    def __init__(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext, ):
        ...

    def GetObjectData(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext, ) -> None:
        ...

class UnicodeException(System.Runtime.Serialization.ISerializable, IronPython.Runtime.Exceptions.IPythonAwareException, System.Exception):
    @typing.overload
    def __init__(self, **kwargs):
        self._message: str
        ...

    # static fields

    # properties
    @property
    def PythonException(self) -> IronPython.Runtime.Exceptions.PythonExceptions.BaseException:
        ...
    @PythonException.setter
    def PythonException(self, val: IronPython.Runtime.Exceptions.PythonExceptions.BaseException):
        ...

    @property
    def Frames(self) -> System.Collections.Generic.List[Microsoft.Scripting.Runtime.DynamicStackFrame]:
        ...
    @Frames.setter
    def Frames(self, val: System.Collections.Generic.List[Microsoft.Scripting.Runtime.DynamicStackFrame]):
        ...

    @property
    def TraceBack(self) -> IronPython.Runtime.Exceptions.TraceBack:
        ...
    @TraceBack.setter
    def TraceBack(self, val: IronPython.Runtime.Exceptions.TraceBack):
        ...

    @property
    def TargetSite(self) -> System.Reflection.MethodBase:
        ...

    @property
    def Message(self) -> str:
        ...

    @property
    def Data(self) -> System.Collections.IDictionary:
        ...

    @property
    def InnerException(self) -> System.Exception:
        ...

    @property
    def HelpLink(self) -> str:
        ...
    @HelpLink.setter
    def HelpLink(self, val: str):
        ...

    @property
    def Source(self) -> str:
        ...
    @Source.setter
    def Source(self, val: str):
        ...

    @property
    def HResult(self) -> int:
        ...
    @HResult.setter
    def HResult(self, val: int):
        ...

    @property
    def StackTrace(self) -> str:
        ...

    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def __init__(self, msg: str, ):
        ...

    @typing.overload
    def __init__(self, message: str, innerException: System.Exception, ):
        ...

    @typing.overload
    def __init__(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext, ):
        ...

    def GetObjectData(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext, ) -> None:
        ...

class TypeErrorException(System.Runtime.Serialization.ISerializable, IronPython.Runtime.Exceptions.IPythonAwareException, Microsoft.Scripting.ArgumentTypeException):
    @typing.overload
    def __init__(self, **kwargs):
        self._message: str
        ...

    # static fields

    # properties
    @property
    def PythonException(self) -> IronPython.Runtime.Exceptions.PythonExceptions.BaseException:
        ...
    @PythonException.setter
    def PythonException(self, val: IronPython.Runtime.Exceptions.PythonExceptions.BaseException):
        ...

    @property
    def Frames(self) -> System.Collections.Generic.List[Microsoft.Scripting.Runtime.DynamicStackFrame]:
        ...
    @Frames.setter
    def Frames(self, val: System.Collections.Generic.List[Microsoft.Scripting.Runtime.DynamicStackFrame]):
        ...

    @property
    def TraceBack(self) -> IronPython.Runtime.Exceptions.TraceBack:
        ...
    @TraceBack.setter
    def TraceBack(self, val: IronPython.Runtime.Exceptions.TraceBack):
        ...

    @property
    def TargetSite(self) -> System.Reflection.MethodBase:
        ...

    @property
    def Message(self) -> str:
        ...

    @property
    def Data(self) -> System.Collections.IDictionary:
        ...

    @property
    def InnerException(self) -> System.Exception:
        ...

    @property
    def HelpLink(self) -> str:
        ...
    @HelpLink.setter
    def HelpLink(self, val: str):
        ...

    @property
    def Source(self) -> str:
        ...
    @Source.setter
    def Source(self, val: str):
        ...

    @property
    def HResult(self) -> int:
        ...
    @HResult.setter
    def HResult(self, val: int):
        ...

    @property
    def StackTrace(self) -> str:
        ...

    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def __init__(self, msg: str, ):
        ...

    @typing.overload
    def __init__(self, message: str, innerException: System.Exception, ):
        ...

    @typing.overload
    def __init__(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext, ):
        ...

    def GetObjectData(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext, ) -> None:
        ...

class UnicodeWarningException(System.Runtime.Serialization.ISerializable, IronPython.Runtime.Exceptions.IPythonAwareException, System.ComponentModel.WarningException):
    @typing.overload
    def __init__(self, **kwargs):
        self._message: str
        ...

    # static fields

    # properties
    @property
    def PythonException(self) -> IronPython.Runtime.Exceptions.PythonExceptions.BaseException:
        ...
    @PythonException.setter
    def PythonException(self, val: IronPython.Runtime.Exceptions.PythonExceptions.BaseException):
        ...

    @property
    def Frames(self) -> System.Collections.Generic.List[Microsoft.Scripting.Runtime.DynamicStackFrame]:
        ...
    @Frames.setter
    def Frames(self, val: System.Collections.Generic.List[Microsoft.Scripting.Runtime.DynamicStackFrame]):
        ...

    @property
    def TraceBack(self) -> IronPython.Runtime.Exceptions.TraceBack:
        ...
    @TraceBack.setter
    def TraceBack(self, val: IronPython.Runtime.Exceptions.TraceBack):
        ...

    @property
    def HelpUrl(self) -> str:
        ...

    @property
    def HelpTopic(self) -> str:
        ...

    @property
    def TargetSite(self) -> System.Reflection.MethodBase:
        ...

    @property
    def Message(self) -> str:
        ...

    @property
    def Data(self) -> System.Collections.IDictionary:
        ...

    @property
    def InnerException(self) -> System.Exception:
        ...

    @property
    def HelpLink(self) -> str:
        ...
    @HelpLink.setter
    def HelpLink(self, val: str):
        ...

    @property
    def Source(self) -> str:
        ...
    @Source.setter
    def Source(self, val: str):
        ...

    @property
    def HResult(self) -> int:
        ...
    @HResult.setter
    def HResult(self, val: int):
        ...

    @property
    def StackTrace(self) -> str:
        ...

    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def __init__(self, msg: str, ):
        ...

    @typing.overload
    def __init__(self, message: str, innerException: System.Exception, ):
        ...

    @typing.overload
    def __init__(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext, ):
        ...

    def GetObjectData(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext, ) -> None:
        ...

class DeprecationWarningException(System.Runtime.Serialization.ISerializable, IronPython.Runtime.Exceptions.IPythonAwareException, System.ComponentModel.WarningException):
    @typing.overload
    def __init__(self, **kwargs):
        self._message: str
        ...

    # static fields

    # properties
    @property
    def PythonException(self) -> IronPython.Runtime.Exceptions.PythonExceptions.BaseException:
        ...
    @PythonException.setter
    def PythonException(self, val: IronPython.Runtime.Exceptions.PythonExceptions.BaseException):
        ...

    @property
    def Frames(self) -> System.Collections.Generic.List[Microsoft.Scripting.Runtime.DynamicStackFrame]:
        ...
    @Frames.setter
    def Frames(self, val: System.Collections.Generic.List[Microsoft.Scripting.Runtime.DynamicStackFrame]):
        ...

    @property
    def TraceBack(self) -> IronPython.Runtime.Exceptions.TraceBack:
        ...
    @TraceBack.setter
    def TraceBack(self, val: IronPython.Runtime.Exceptions.TraceBack):
        ...

    @property
    def HelpUrl(self) -> str:
        ...

    @property
    def HelpTopic(self) -> str:
        ...

    @property
    def TargetSite(self) -> System.Reflection.MethodBase:
        ...

    @property
    def Message(self) -> str:
        ...

    @property
    def Data(self) -> System.Collections.IDictionary:
        ...

    @property
    def InnerException(self) -> System.Exception:
        ...

    @property
    def HelpLink(self) -> str:
        ...
    @HelpLink.setter
    def HelpLink(self, val: str):
        ...

    @property
    def Source(self) -> str:
        ...
    @Source.setter
    def Source(self, val: str):
        ...

    @property
    def HResult(self) -> int:
        ...
    @HResult.setter
    def HResult(self, val: int):
        ...

    @property
    def StackTrace(self) -> str:
        ...

    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def __init__(self, msg: str, ):
        ...

    @typing.overload
    def __init__(self, message: str, innerException: System.Exception, ):
        ...

    @typing.overload
    def __init__(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext, ):
        ...

    def GetObjectData(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext, ) -> None:
        ...

class TracebackDelegate(System.ICloneable, System.Runtime.Serialization.ISerializable, System.MulticastDelegate):
    @typing.overload
    def __init__(self, **kwargs):
        self._target: System.Object
        self._methodBase: System.Object
        self._methodPtr: System.IntPtr
        self._methodPtrAux: System.IntPtr
        ...

    # static fields

    # properties
    @property
    def Target(self) -> System.Object:
        ...

    @property
    def Method(self) -> System.Reflection.MethodInfo:
        ...

    # methods
    def __init__(self, object: System.Object, method: System.IntPtr, ):
        ...

    def Invoke(self, frame: IronPython.Runtime.Exceptions.TraceBackFrame, result: str, payload: System.Object, ) -> IronPython.Runtime.Exceptions.TracebackDelegate:
        ...

    def BeginInvoke(self, frame: IronPython.Runtime.Exceptions.TraceBackFrame, result: str, payload: System.Object, callback: System.AsyncCallback, object: System.Object, ) -> System.IAsyncResult:
        ...

    def EndInvoke(self, result: System.IAsyncResult, ) -> IronPython.Runtime.Exceptions.TracebackDelegate:
        ...

class BrokenPipeException(System.Runtime.Serialization.ISerializable, IronPython.Runtime.Exceptions.IPythonAwareException, IronPython.Runtime.Exceptions.ConnectionException):
    @typing.overload
    def __init__(self, **kwargs):
        self._message: str
        ...

    # static fields

    # properties
    @property
    def PythonException(self) -> IronPython.Runtime.Exceptions.PythonExceptions.BaseException:
        ...
    @PythonException.setter
    def PythonException(self, val: IronPython.Runtime.Exceptions.PythonExceptions.BaseException):
        ...

    @property
    def Frames(self) -> System.Collections.Generic.List[Microsoft.Scripting.Runtime.DynamicStackFrame]:
        ...
    @Frames.setter
    def Frames(self, val: System.Collections.Generic.List[Microsoft.Scripting.Runtime.DynamicStackFrame]):
        ...

    @property
    def TraceBack(self) -> IronPython.Runtime.Exceptions.TraceBack:
        ...
    @TraceBack.setter
    def TraceBack(self, val: IronPython.Runtime.Exceptions.TraceBack):
        ...

    @property
    def TargetSite(self) -> System.Reflection.MethodBase:
        ...

    @property
    def Message(self) -> str:
        ...

    @property
    def Data(self) -> System.Collections.IDictionary:
        ...

    @property
    def InnerException(self) -> System.Exception:
        ...

    @property
    def HelpLink(self) -> str:
        ...
    @HelpLink.setter
    def HelpLink(self, val: str):
        ...

    @property
    def Source(self) -> str:
        ...
    @Source.setter
    def Source(self, val: str):
        ...

    @property
    def HResult(self) -> int:
        ...
    @HResult.setter
    def HResult(self, val: int):
        ...

    @property
    def StackTrace(self) -> str:
        ...

    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def __init__(self, msg: str, ):
        ...

    @typing.overload
    def __init__(self, message: str, innerException: System.Exception, ):
        ...

    @typing.overload
    def __init__(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext, ):
        ...

    def GetObjectData(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext, ) -> None:
        ...

class BufferException(System.Runtime.Serialization.ISerializable, IronPython.Runtime.Exceptions.IPythonAwareException, System.Exception):
    @typing.overload
    def __init__(self, **kwargs):
        self._message: str
        ...

    # static fields

    # properties
    @property
    def PythonException(self) -> IronPython.Runtime.Exceptions.PythonExceptions.BaseException:
        ...
    @PythonException.setter
    def PythonException(self, val: IronPython.Runtime.Exceptions.PythonExceptions.BaseException):
        ...

    @property
    def Frames(self) -> System.Collections.Generic.List[Microsoft.Scripting.Runtime.DynamicStackFrame]:
        ...
    @Frames.setter
    def Frames(self, val: System.Collections.Generic.List[Microsoft.Scripting.Runtime.DynamicStackFrame]):
        ...

    @property
    def TraceBack(self) -> IronPython.Runtime.Exceptions.TraceBack:
        ...
    @TraceBack.setter
    def TraceBack(self, val: IronPython.Runtime.Exceptions.TraceBack):
        ...

    @property
    def TargetSite(self) -> System.Reflection.MethodBase:
        ...

    @property
    def Message(self) -> str:
        ...

    @property
    def Data(self) -> System.Collections.IDictionary:
        ...

    @property
    def InnerException(self) -> System.Exception:
        ...

    @property
    def HelpLink(self) -> str:
        ...
    @HelpLink.setter
    def HelpLink(self, val: str):
        ...

    @property
    def Source(self) -> str:
        ...
    @Source.setter
    def Source(self, val: str):
        ...

    @property
    def HResult(self) -> int:
        ...
    @HResult.setter
    def HResult(self, val: int):
        ...

    @property
    def StackTrace(self) -> str:
        ...

    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def __init__(self, msg: str, ):
        ...

    @typing.overload
    def __init__(self, message: str, innerException: System.Exception, ):
        ...

    @typing.overload
    def __init__(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext, ):
        ...

    def GetObjectData(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext, ) -> None:
        ...

class OSException(System.Runtime.Serialization.ISerializable, IronPython.Runtime.Exceptions.IPythonAwareException, System.Exception):
    @typing.overload
    def __init__(self, **kwargs):
        self._message: str
        ...

    # static fields

    # properties
    @property
    def PythonException(self) -> IronPython.Runtime.Exceptions.PythonExceptions.BaseException:
        ...
    @PythonException.setter
    def PythonException(self, val: IronPython.Runtime.Exceptions.PythonExceptions.BaseException):
        ...

    @property
    def Frames(self) -> System.Collections.Generic.List[Microsoft.Scripting.Runtime.DynamicStackFrame]:
        ...
    @Frames.setter
    def Frames(self, val: System.Collections.Generic.List[Microsoft.Scripting.Runtime.DynamicStackFrame]):
        ...

    @property
    def TraceBack(self) -> IronPython.Runtime.Exceptions.TraceBack:
        ...
    @TraceBack.setter
    def TraceBack(self, val: IronPython.Runtime.Exceptions.TraceBack):
        ...

    @property
    def TargetSite(self) -> System.Reflection.MethodBase:
        ...

    @property
    def Message(self) -> str:
        ...

    @property
    def Data(self) -> System.Collections.IDictionary:
        ...

    @property
    def InnerException(self) -> System.Exception:
        ...

    @property
    def HelpLink(self) -> str:
        ...
    @HelpLink.setter
    def HelpLink(self, val: str):
        ...

    @property
    def Source(self) -> str:
        ...
    @Source.setter
    def Source(self, val: str):
        ...

    @property
    def HResult(self) -> int:
        ...
    @HResult.setter
    def HResult(self, val: int):
        ...

    @property
    def StackTrace(self) -> str:
        ...

    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def __init__(self, msg: str, ):
        ...

    @typing.overload
    def __init__(self, message: str, innerException: System.Exception, ):
        ...

    @typing.overload
    def __init__(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext, ):
        ...

    def GetObjectData(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext, ) -> None:
        ...

class RuntimeWarningException(System.Runtime.Serialization.ISerializable, IronPython.Runtime.Exceptions.IPythonAwareException, System.ComponentModel.WarningException):
    @typing.overload
    def __init__(self, **kwargs):
        self._message: str
        ...

    # static fields

    # properties
    @property
    def PythonException(self) -> IronPython.Runtime.Exceptions.PythonExceptions.BaseException:
        ...
    @PythonException.setter
    def PythonException(self, val: IronPython.Runtime.Exceptions.PythonExceptions.BaseException):
        ...

    @property
    def Frames(self) -> System.Collections.Generic.List[Microsoft.Scripting.Runtime.DynamicStackFrame]:
        ...
    @Frames.setter
    def Frames(self, val: System.Collections.Generic.List[Microsoft.Scripting.Runtime.DynamicStackFrame]):
        ...

    @property
    def TraceBack(self) -> IronPython.Runtime.Exceptions.TraceBack:
        ...
    @TraceBack.setter
    def TraceBack(self, val: IronPython.Runtime.Exceptions.TraceBack):
        ...

    @property
    def HelpUrl(self) -> str:
        ...

    @property
    def HelpTopic(self) -> str:
        ...

    @property
    def TargetSite(self) -> System.Reflection.MethodBase:
        ...

    @property
    def Message(self) -> str:
        ...

    @property
    def Data(self) -> System.Collections.IDictionary:
        ...

    @property
    def InnerException(self) -> System.Exception:
        ...

    @property
    def HelpLink(self) -> str:
        ...
    @HelpLink.setter
    def HelpLink(self, val: str):
        ...

    @property
    def Source(self) -> str:
        ...
    @Source.setter
    def Source(self, val: str):
        ...

    @property
    def HResult(self) -> int:
        ...
    @HResult.setter
    def HResult(self, val: int):
        ...

    @property
    def StackTrace(self) -> str:
        ...

    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def __init__(self, msg: str, ):
        ...

    @typing.overload
    def __init__(self, message: str, innerException: System.Exception, ):
        ...

    @typing.overload
    def __init__(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext, ):
        ...

    def GetObjectData(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext, ) -> None:
        ...

class StopAsyncIterationException(System.Runtime.Serialization.ISerializable, IronPython.Runtime.Exceptions.IPythonAwareException, System.Exception):
    @typing.overload
    def __init__(self, **kwargs):
        self._message: str
        ...

    # static fields

    # properties
    @property
    def PythonException(self) -> IronPython.Runtime.Exceptions.PythonExceptions.BaseException:
        ...
    @PythonException.setter
    def PythonException(self, val: IronPython.Runtime.Exceptions.PythonExceptions.BaseException):
        ...

    @property
    def Frames(self) -> System.Collections.Generic.List[Microsoft.Scripting.Runtime.DynamicStackFrame]:
        ...
    @Frames.setter
    def Frames(self, val: System.Collections.Generic.List[Microsoft.Scripting.Runtime.DynamicStackFrame]):
        ...

    @property
    def TraceBack(self) -> IronPython.Runtime.Exceptions.TraceBack:
        ...
    @TraceBack.setter
    def TraceBack(self, val: IronPython.Runtime.Exceptions.TraceBack):
        ...

    @property
    def TargetSite(self) -> System.Reflection.MethodBase:
        ...

    @property
    def Message(self) -> str:
        ...

    @property
    def Data(self) -> System.Collections.IDictionary:
        ...

    @property
    def InnerException(self) -> System.Exception:
        ...

    @property
    def HelpLink(self) -> str:
        ...
    @HelpLink.setter
    def HelpLink(self, val: str):
        ...

    @property
    def Source(self) -> str:
        ...
    @Source.setter
    def Source(self, val: str):
        ...

    @property
    def HResult(self) -> int:
        ...
    @HResult.setter
    def HResult(self, val: int):
        ...

    @property
    def StackTrace(self) -> str:
        ...

    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def __init__(self, msg: str, ):
        ...

    @typing.overload
    def __init__(self, message: str, innerException: System.Exception, ):
        ...

    @typing.overload
    def __init__(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext, ):
        ...

    def GetObjectData(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext, ) -> None:
        ...

class PendingDeprecationWarningException(System.Runtime.Serialization.ISerializable, IronPython.Runtime.Exceptions.IPythonAwareException, System.ComponentModel.WarningException):
    @typing.overload
    def __init__(self, **kwargs):
        self._message: str
        ...

    # static fields

    # properties
    @property
    def PythonException(self) -> IronPython.Runtime.Exceptions.PythonExceptions.BaseException:
        ...
    @PythonException.setter
    def PythonException(self, val: IronPython.Runtime.Exceptions.PythonExceptions.BaseException):
        ...

    @property
    def Frames(self) -> System.Collections.Generic.List[Microsoft.Scripting.Runtime.DynamicStackFrame]:
        ...
    @Frames.setter
    def Frames(self, val: System.Collections.Generic.List[Microsoft.Scripting.Runtime.DynamicStackFrame]):
        ...

    @property
    def TraceBack(self) -> IronPython.Runtime.Exceptions.TraceBack:
        ...
    @TraceBack.setter
    def TraceBack(self, val: IronPython.Runtime.Exceptions.TraceBack):
        ...

    @property
    def HelpUrl(self) -> str:
        ...

    @property
    def HelpTopic(self) -> str:
        ...

    @property
    def TargetSite(self) -> System.Reflection.MethodBase:
        ...

    @property
    def Message(self) -> str:
        ...

    @property
    def Data(self) -> System.Collections.IDictionary:
        ...

    @property
    def InnerException(self) -> System.Exception:
        ...

    @property
    def HelpLink(self) -> str:
        ...
    @HelpLink.setter
    def HelpLink(self, val: str):
        ...

    @property
    def Source(self) -> str:
        ...
    @Source.setter
    def Source(self, val: str):
        ...

    @property
    def HResult(self) -> int:
        ...
    @HResult.setter
    def HResult(self, val: int):
        ...

    @property
    def StackTrace(self) -> str:
        ...

    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def __init__(self, msg: str, ):
        ...

    @typing.overload
    def __init__(self, message: str, innerException: System.Exception, ):
        ...

    @typing.overload
    def __init__(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext, ):
        ...

    def GetObjectData(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext, ) -> None:
        ...

class UserWarningException(System.Runtime.Serialization.ISerializable, IronPython.Runtime.Exceptions.IPythonAwareException, System.ComponentModel.WarningException):
    @typing.overload
    def __init__(self, **kwargs):
        self._message: str
        ...

    # static fields

    # properties
    @property
    def PythonException(self) -> IronPython.Runtime.Exceptions.PythonExceptions.BaseException:
        ...
    @PythonException.setter
    def PythonException(self, val: IronPython.Runtime.Exceptions.PythonExceptions.BaseException):
        ...

    @property
    def Frames(self) -> System.Collections.Generic.List[Microsoft.Scripting.Runtime.DynamicStackFrame]:
        ...
    @Frames.setter
    def Frames(self, val: System.Collections.Generic.List[Microsoft.Scripting.Runtime.DynamicStackFrame]):
        ...

    @property
    def TraceBack(self) -> IronPython.Runtime.Exceptions.TraceBack:
        ...
    @TraceBack.setter
    def TraceBack(self, val: IronPython.Runtime.Exceptions.TraceBack):
        ...

    @property
    def HelpUrl(self) -> str:
        ...

    @property
    def HelpTopic(self) -> str:
        ...

    @property
    def TargetSite(self) -> System.Reflection.MethodBase:
        ...

    @property
    def Message(self) -> str:
        ...

    @property
    def Data(self) -> System.Collections.IDictionary:
        ...

    @property
    def InnerException(self) -> System.Exception:
        ...

    @property
    def HelpLink(self) -> str:
        ...
    @HelpLink.setter
    def HelpLink(self, val: str):
        ...

    @property
    def Source(self) -> str:
        ...
    @Source.setter
    def Source(self, val: str):
        ...

    @property
    def HResult(self) -> int:
        ...
    @HResult.setter
    def HResult(self, val: int):
        ...

    @property
    def StackTrace(self) -> str:
        ...

    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def __init__(self, msg: str, ):
        ...

    @typing.overload
    def __init__(self, message: str, innerException: System.Exception, ):
        ...

    @typing.overload
    def __init__(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext, ):
        ...

    def GetObjectData(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext, ) -> None:
        ...

class ConnectionRefusedException(System.Runtime.Serialization.ISerializable, IronPython.Runtime.Exceptions.IPythonAwareException, IronPython.Runtime.Exceptions.ConnectionException):
    @typing.overload
    def __init__(self, **kwargs):
        self._message: str
        ...

    # static fields

    # properties
    @property
    def PythonException(self) -> IronPython.Runtime.Exceptions.PythonExceptions.BaseException:
        ...
    @PythonException.setter
    def PythonException(self, val: IronPython.Runtime.Exceptions.PythonExceptions.BaseException):
        ...

    @property
    def Frames(self) -> System.Collections.Generic.List[Microsoft.Scripting.Runtime.DynamicStackFrame]:
        ...
    @Frames.setter
    def Frames(self, val: System.Collections.Generic.List[Microsoft.Scripting.Runtime.DynamicStackFrame]):
        ...

    @property
    def TraceBack(self) -> IronPython.Runtime.Exceptions.TraceBack:
        ...
    @TraceBack.setter
    def TraceBack(self, val: IronPython.Runtime.Exceptions.TraceBack):
        ...

    @property
    def TargetSite(self) -> System.Reflection.MethodBase:
        ...

    @property
    def Message(self) -> str:
        ...

    @property
    def Data(self) -> System.Collections.IDictionary:
        ...

    @property
    def InnerException(self) -> System.Exception:
        ...

    @property
    def HelpLink(self) -> str:
        ...
    @HelpLink.setter
    def HelpLink(self, val: str):
        ...

    @property
    def Source(self) -> str:
        ...
    @Source.setter
    def Source(self, val: str):
        ...

    @property
    def HResult(self) -> int:
        ...
    @HResult.setter
    def HResult(self, val: int):
        ...

    @property
    def StackTrace(self) -> str:
        ...

    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def __init__(self, msg: str, ):
        ...

    @typing.overload
    def __init__(self, message: str, innerException: System.Exception, ):
        ...

    @typing.overload
    def __init__(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext, ):
        ...

    def GetObjectData(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext, ) -> None:
        ...

class IsADirectoryException(System.Runtime.Serialization.ISerializable, IronPython.Runtime.Exceptions.IPythonAwareException, IronPython.Runtime.Exceptions.OSException):
    @typing.overload
    def __init__(self, **kwargs):
        self._message: str
        ...

    # static fields

    # properties
    @property
    def PythonException(self) -> IronPython.Runtime.Exceptions.PythonExceptions.BaseException:
        ...
    @PythonException.setter
    def PythonException(self, val: IronPython.Runtime.Exceptions.PythonExceptions.BaseException):
        ...

    @property
    def Frames(self) -> System.Collections.Generic.List[Microsoft.Scripting.Runtime.DynamicStackFrame]:
        ...
    @Frames.setter
    def Frames(self, val: System.Collections.Generic.List[Microsoft.Scripting.Runtime.DynamicStackFrame]):
        ...

    @property
    def TraceBack(self) -> IronPython.Runtime.Exceptions.TraceBack:
        ...
    @TraceBack.setter
    def TraceBack(self, val: IronPython.Runtime.Exceptions.TraceBack):
        ...

    @property
    def TargetSite(self) -> System.Reflection.MethodBase:
        ...

    @property
    def Message(self) -> str:
        ...

    @property
    def Data(self) -> System.Collections.IDictionary:
        ...

    @property
    def InnerException(self) -> System.Exception:
        ...

    @property
    def HelpLink(self) -> str:
        ...
    @HelpLink.setter
    def HelpLink(self, val: str):
        ...

    @property
    def Source(self) -> str:
        ...
    @Source.setter
    def Source(self, val: str):
        ...

    @property
    def HResult(self) -> int:
        ...
    @HResult.setter
    def HResult(self, val: int):
        ...

    @property
    def StackTrace(self) -> str:
        ...

    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def __init__(self, msg: str, ):
        ...

    @typing.overload
    def __init__(self, message: str, innerException: System.Exception, ):
        ...

    @typing.overload
    def __init__(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext, ):
        ...

    def GetObjectData(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext, ) -> None:
        ...

class LookupException(System.Runtime.Serialization.ISerializable, IronPython.Runtime.Exceptions.IPythonAwareException, System.Exception):
    @typing.overload
    def __init__(self, **kwargs):
        self._message: str
        ...

    # static fields

    # properties
    @property
    def PythonException(self) -> IronPython.Runtime.Exceptions.PythonExceptions.BaseException:
        ...
    @PythonException.setter
    def PythonException(self, val: IronPython.Runtime.Exceptions.PythonExceptions.BaseException):
        ...

    @property
    def Frames(self) -> System.Collections.Generic.List[Microsoft.Scripting.Runtime.DynamicStackFrame]:
        ...
    @Frames.setter
    def Frames(self, val: System.Collections.Generic.List[Microsoft.Scripting.Runtime.DynamicStackFrame]):
        ...

    @property
    def TraceBack(self) -> IronPython.Runtime.Exceptions.TraceBack:
        ...
    @TraceBack.setter
    def TraceBack(self, val: IronPython.Runtime.Exceptions.TraceBack):
        ...

    @property
    def TargetSite(self) -> System.Reflection.MethodBase:
        ...

    @property
    def Message(self) -> str:
        ...

    @property
    def Data(self) -> System.Collections.IDictionary:
        ...

    @property
    def InnerException(self) -> System.Exception:
        ...

    @property
    def HelpLink(self) -> str:
        ...
    @HelpLink.setter
    def HelpLink(self, val: str):
        ...

    @property
    def Source(self) -> str:
        ...
    @Source.setter
    def Source(self, val: str):
        ...

    @property
    def HResult(self) -> int:
        ...
    @HResult.setter
    def HResult(self, val: int):
        ...

    @property
    def StackTrace(self) -> str:
        ...

    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def __init__(self, msg: str, ):
        ...

    @typing.overload
    def __init__(self, message: str, innerException: System.Exception, ):
        ...

    @typing.overload
    def __init__(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext, ):
        ...

    def GetObjectData(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext, ) -> None:
        ...

class ResourceWarningException(System.Runtime.Serialization.ISerializable, IronPython.Runtime.Exceptions.IPythonAwareException, System.ComponentModel.WarningException):
    @typing.overload
    def __init__(self, **kwargs):
        self._message: str
        ...

    # static fields

    # properties
    @property
    def PythonException(self) -> IronPython.Runtime.Exceptions.PythonExceptions.BaseException:
        ...
    @PythonException.setter
    def PythonException(self, val: IronPython.Runtime.Exceptions.PythonExceptions.BaseException):
        ...

    @property
    def Frames(self) -> System.Collections.Generic.List[Microsoft.Scripting.Runtime.DynamicStackFrame]:
        ...
    @Frames.setter
    def Frames(self, val: System.Collections.Generic.List[Microsoft.Scripting.Runtime.DynamicStackFrame]):
        ...

    @property
    def TraceBack(self) -> IronPython.Runtime.Exceptions.TraceBack:
        ...
    @TraceBack.setter
    def TraceBack(self, val: IronPython.Runtime.Exceptions.TraceBack):
        ...

    @property
    def HelpUrl(self) -> str:
        ...

    @property
    def HelpTopic(self) -> str:
        ...

    @property
    def TargetSite(self) -> System.Reflection.MethodBase:
        ...

    @property
    def Message(self) -> str:
        ...

    @property
    def Data(self) -> System.Collections.IDictionary:
        ...

    @property
    def InnerException(self) -> System.Exception:
        ...

    @property
    def HelpLink(self) -> str:
        ...
    @HelpLink.setter
    def HelpLink(self, val: str):
        ...

    @property
    def Source(self) -> str:
        ...
    @Source.setter
    def Source(self, val: str):
        ...

    @property
    def HResult(self) -> int:
        ...
    @HResult.setter
    def HResult(self, val: int):
        ...

    @property
    def StackTrace(self) -> str:
        ...

    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def __init__(self, msg: str, ):
        ...

    @typing.overload
    def __init__(self, message: str, innerException: System.Exception, ):
        ...

    @typing.overload
    def __init__(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext, ):
        ...

    def GetObjectData(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext, ) -> None:
        ...

class SyntaxWarningException(System.Runtime.Serialization.ISerializable, IronPython.Runtime.Exceptions.IPythonAwareException, System.ComponentModel.WarningException):
    @typing.overload
    def __init__(self, **kwargs):
        self._message: str
        ...

    # static fields

    # properties
    @property
    def PythonException(self) -> IronPython.Runtime.Exceptions.PythonExceptions.BaseException:
        ...
    @PythonException.setter
    def PythonException(self, val: IronPython.Runtime.Exceptions.PythonExceptions.BaseException):
        ...

    @property
    def Frames(self) -> System.Collections.Generic.List[Microsoft.Scripting.Runtime.DynamicStackFrame]:
        ...
    @Frames.setter
    def Frames(self, val: System.Collections.Generic.List[Microsoft.Scripting.Runtime.DynamicStackFrame]):
        ...

    @property
    def TraceBack(self) -> IronPython.Runtime.Exceptions.TraceBack:
        ...
    @TraceBack.setter
    def TraceBack(self, val: IronPython.Runtime.Exceptions.TraceBack):
        ...

    @property
    def HelpUrl(self) -> str:
        ...

    @property
    def HelpTopic(self) -> str:
        ...

    @property
    def TargetSite(self) -> System.Reflection.MethodBase:
        ...

    @property
    def Message(self) -> str:
        ...

    @property
    def Data(self) -> System.Collections.IDictionary:
        ...

    @property
    def InnerException(self) -> System.Exception:
        ...

    @property
    def HelpLink(self) -> str:
        ...
    @HelpLink.setter
    def HelpLink(self, val: str):
        ...

    @property
    def Source(self) -> str:
        ...
    @Source.setter
    def Source(self, val: str):
        ...

    @property
    def HResult(self) -> int:
        ...
    @HResult.setter
    def HResult(self, val: int):
        ...

    @property
    def StackTrace(self) -> str:
        ...

    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def __init__(self, msg: str, ):
        ...

    @typing.overload
    def __init__(self, message: str, innerException: System.Exception, ):
        ...

    @typing.overload
    def __init__(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext, ):
        ...

    def GetObjectData(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext, ) -> None:
        ...

class ConnectionException(System.Runtime.Serialization.ISerializable, IronPython.Runtime.Exceptions.IPythonAwareException, IronPython.Runtime.Exceptions.OSException):
    @typing.overload
    def __init__(self, **kwargs):
        self._message: str
        ...

    # static fields

    # properties
    @property
    def PythonException(self) -> IronPython.Runtime.Exceptions.PythonExceptions.BaseException:
        ...
    @PythonException.setter
    def PythonException(self, val: IronPython.Runtime.Exceptions.PythonExceptions.BaseException):
        ...

    @property
    def Frames(self) -> System.Collections.Generic.List[Microsoft.Scripting.Runtime.DynamicStackFrame]:
        ...
    @Frames.setter
    def Frames(self, val: System.Collections.Generic.List[Microsoft.Scripting.Runtime.DynamicStackFrame]):
        ...

    @property
    def TraceBack(self) -> IronPython.Runtime.Exceptions.TraceBack:
        ...
    @TraceBack.setter
    def TraceBack(self, val: IronPython.Runtime.Exceptions.TraceBack):
        ...

    @property
    def TargetSite(self) -> System.Reflection.MethodBase:
        ...

    @property
    def Message(self) -> str:
        ...

    @property
    def Data(self) -> System.Collections.IDictionary:
        ...

    @property
    def InnerException(self) -> System.Exception:
        ...

    @property
    def HelpLink(self) -> str:
        ...
    @HelpLink.setter
    def HelpLink(self, val: str):
        ...

    @property
    def Source(self) -> str:
        ...
    @Source.setter
    def Source(self, val: str):
        ...

    @property
    def HResult(self) -> int:
        ...
    @HResult.setter
    def HResult(self, val: int):
        ...

    @property
    def StackTrace(self) -> str:
        ...

    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def __init__(self, msg: str, ):
        ...

    @typing.overload
    def __init__(self, message: str, innerException: System.Exception, ):
        ...

    @typing.overload
    def __init__(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext, ):
        ...

    def GetObjectData(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext, ) -> None:
        ...

class StopIterationException(System.Runtime.Serialization.ISerializable, IronPython.Runtime.Exceptions.IPythonAwareException, System.Exception):
    @typing.overload
    def __init__(self, **kwargs):
        self._message: str
        ...

    # static fields

    # properties
    @property
    def PythonException(self) -> IronPython.Runtime.Exceptions.PythonExceptions.BaseException:
        ...
    @PythonException.setter
    def PythonException(self, val: IronPython.Runtime.Exceptions.PythonExceptions.BaseException):
        ...

    @property
    def Frames(self) -> System.Collections.Generic.List[Microsoft.Scripting.Runtime.DynamicStackFrame]:
        ...
    @Frames.setter
    def Frames(self, val: System.Collections.Generic.List[Microsoft.Scripting.Runtime.DynamicStackFrame]):
        ...

    @property
    def TraceBack(self) -> IronPython.Runtime.Exceptions.TraceBack:
        ...
    @TraceBack.setter
    def TraceBack(self, val: IronPython.Runtime.Exceptions.TraceBack):
        ...

    @property
    def TargetSite(self) -> System.Reflection.MethodBase:
        ...

    @property
    def Message(self) -> str:
        ...

    @property
    def Data(self) -> System.Collections.IDictionary:
        ...

    @property
    def InnerException(self) -> System.Exception:
        ...

    @property
    def HelpLink(self) -> str:
        ...
    @HelpLink.setter
    def HelpLink(self, val: str):
        ...

    @property
    def Source(self) -> str:
        ...
    @Source.setter
    def Source(self, val: str):
        ...

    @property
    def HResult(self) -> int:
        ...
    @HResult.setter
    def HResult(self, val: int):
        ...

    @property
    def StackTrace(self) -> str:
        ...

    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def __init__(self, msg: str, ):
        ...

    @typing.overload
    def __init__(self, message: str, innerException: System.Exception, ):
        ...

    @typing.overload
    def __init__(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext, ):
        ...

    def GetObjectData(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext, ) -> None:
        ...

class AttributeErrorException(System.Runtime.Serialization.ISerializable, IronPython.Runtime.Exceptions.IPythonAwareException, System.MissingMemberException):
    @typing.overload
    def __init__(self, **kwargs):
        self.ClassName: str
        self.MemberName: str
        self.Signature: System.Array[int]
        self._message: str
        ...

    # static fields

    # properties
    @property
    def PythonException(self) -> IronPython.Runtime.Exceptions.PythonExceptions.BaseException:
        ...
    @PythonException.setter
    def PythonException(self, val: IronPython.Runtime.Exceptions.PythonExceptions.BaseException):
        ...

    @property
    def Frames(self) -> System.Collections.Generic.List[Microsoft.Scripting.Runtime.DynamicStackFrame]:
        ...
    @Frames.setter
    def Frames(self, val: System.Collections.Generic.List[Microsoft.Scripting.Runtime.DynamicStackFrame]):
        ...

    @property
    def TraceBack(self) -> IronPython.Runtime.Exceptions.TraceBack:
        ...
    @TraceBack.setter
    def TraceBack(self, val: IronPython.Runtime.Exceptions.TraceBack):
        ...

    @property
    def Message(self) -> str:
        ...

    @property
    def TargetSite(self) -> System.Reflection.MethodBase:
        ...

    @property
    def Data(self) -> System.Collections.IDictionary:
        ...

    @property
    def InnerException(self) -> System.Exception:
        ...

    @property
    def HelpLink(self) -> str:
        ...
    @HelpLink.setter
    def HelpLink(self, val: str):
        ...

    @property
    def Source(self) -> str:
        ...
    @Source.setter
    def Source(self, val: str):
        ...

    @property
    def HResult(self) -> int:
        ...
    @HResult.setter
    def HResult(self, val: int):
        ...

    @property
    def StackTrace(self) -> str:
        ...

    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def __init__(self, msg: str, ):
        ...

    @typing.overload
    def __init__(self, message: str, innerException: System.Exception, ):
        ...

    @typing.overload
    def __init__(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext, ):
        ...

    def GetObjectData(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext, ) -> None:
        ...

class TraceBackFrame(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        self._lineNo: int
        ...

    # static fields

    # properties
    @property
    def Context(self) -> IronPython.Runtime.CodeContext:
        ...

    @property
    def TraceDelegate(self) -> IronPython.Runtime.Exceptions.TracebackDelegate:
        ...

    @property
    def f_globals(self) -> IronPython.Runtime.PythonDictionary:
        ...

    @property
    def f_locals(self) -> System.Object:
        ...

    @property
    def f_code(self) -> IronPython.Runtime.FunctionCode:
        ...

    @property
    def f_builtins(self) -> System.Object:
        ...

    @property
    def f_back(self) -> IronPython.Runtime.Exceptions.TraceBackFrame:
        ...

    @property
    def f_lineno(self) -> System.Object:
        ...
    @f_lineno.setter
    def f_lineno(self, val: System.Object):
        ...

    # methods
    @typing.overload
    def __init__(self, context: IronPython.Runtime.CodeContext, globals: IronPython.Runtime.PythonDictionary, locals: System.Object, code: IronPython.Runtime.FunctionCode, ):
        ...

    @typing.overload
    def __init__(self, context: IronPython.Runtime.CodeContext, globals: IronPython.Runtime.PythonDictionary, locals: System.Object, code: IronPython.Runtime.FunctionCode, back: IronPython.Runtime.Exceptions.TraceBackFrame, ):
        ...

    @typing.overload
    def __init__(self, traceAdapter: IronPython.Runtime.PythonTracebackListener, code: IronPython.Runtime.FunctionCode, back: IronPython.Runtime.Exceptions.TraceBackFrame, debugProperties: IronPython.Runtime.PythonDebuggingPayload, scopeCallback: System.Func[System.Collections.Generic.IDictionary[System.Object, System.Object]], ):
        ...

    def clear(self, ) -> None:
        ...

    def SetLineNumber(self, newLineNum: int, ) -> None:
        ...

    def IsTopMostFrame(self, pyThread: System.Collections.Generic.List[IronPython.Runtime.Operations.FunctionStack], ) -> bool:
        ...

    @staticmethod
    def BadForOrFinallyJump(newLineNum: int, jumpIntoLoopIds: System.Collections.Generic.Dictionary[int, bool], ) -> System.Exception:
        ...

class GeneratorExitException(System.Runtime.Serialization.ISerializable, System.Exception):
    @typing.overload
    def __init__(self, **kwargs):
        self._message: str
        ...

    # static fields

    # properties
    @property
    def TargetSite(self) -> System.Reflection.MethodBase:
        ...

    @property
    def Message(self) -> str:
        ...

    @property
    def Data(self) -> System.Collections.IDictionary:
        ...

    @property
    def InnerException(self) -> System.Exception:
        ...

    @property
    def HelpLink(self) -> str:
        ...
    @HelpLink.setter
    def HelpLink(self, val: str):
        ...

    @property
    def Source(self) -> str:
        ...
    @Source.setter
    def Source(self, val: str):
        ...

    @property
    def HResult(self) -> int:
        ...
    @HResult.setter
    def HResult(self, val: int):
        ...

    @property
    def StackTrace(self) -> str:
        ...

    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def __init__(self, message: str, ):
        ...

    @typing.overload
    def __init__(self, message: str, innerException: System.Exception, ):
        ...

    @typing.overload
    def __init__(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext, ):
        ...

class ReferenceException(System.Runtime.Serialization.ISerializable, IronPython.Runtime.Exceptions.IPythonAwareException, System.Exception):
    @typing.overload
    def __init__(self, **kwargs):
        self._message: str
        ...

    # static fields

    # properties
    @property
    def PythonException(self) -> IronPython.Runtime.Exceptions.PythonExceptions.BaseException:
        ...
    @PythonException.setter
    def PythonException(self, val: IronPython.Runtime.Exceptions.PythonExceptions.BaseException):
        ...

    @property
    def Frames(self) -> System.Collections.Generic.List[Microsoft.Scripting.Runtime.DynamicStackFrame]:
        ...
    @Frames.setter
    def Frames(self, val: System.Collections.Generic.List[Microsoft.Scripting.Runtime.DynamicStackFrame]):
        ...

    @property
    def TraceBack(self) -> IronPython.Runtime.Exceptions.TraceBack:
        ...
    @TraceBack.setter
    def TraceBack(self, val: IronPython.Runtime.Exceptions.TraceBack):
        ...

    @property
    def TargetSite(self) -> System.Reflection.MethodBase:
        ...

    @property
    def Message(self) -> str:
        ...

    @property
    def Data(self) -> System.Collections.IDictionary:
        ...

    @property
    def InnerException(self) -> System.Exception:
        ...

    @property
    def HelpLink(self) -> str:
        ...
    @HelpLink.setter
    def HelpLink(self, val: str):
        ...

    @property
    def Source(self) -> str:
        ...
    @Source.setter
    def Source(self, val: str):
        ...

    @property
    def HResult(self) -> int:
        ...
    @HResult.setter
    def HResult(self, val: int):
        ...

    @property
    def StackTrace(self) -> str:
        ...

    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def __init__(self, msg: str, ):
        ...

    @typing.overload
    def __init__(self, message: str, innerException: System.Exception, ):
        ...

    @typing.overload
    def __init__(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext, ):
        ...

    def GetObjectData(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext, ) -> None:
        ...

class ConnectionAbortedException(System.Runtime.Serialization.ISerializable, IronPython.Runtime.Exceptions.IPythonAwareException, IronPython.Runtime.Exceptions.ConnectionException):
    @typing.overload
    def __init__(self, **kwargs):
        self._message: str
        ...

    # static fields

    # properties
    @property
    def PythonException(self) -> IronPython.Runtime.Exceptions.PythonExceptions.BaseException:
        ...
    @PythonException.setter
    def PythonException(self, val: IronPython.Runtime.Exceptions.PythonExceptions.BaseException):
        ...

    @property
    def Frames(self) -> System.Collections.Generic.List[Microsoft.Scripting.Runtime.DynamicStackFrame]:
        ...
    @Frames.setter
    def Frames(self, val: System.Collections.Generic.List[Microsoft.Scripting.Runtime.DynamicStackFrame]):
        ...

    @property
    def TraceBack(self) -> IronPython.Runtime.Exceptions.TraceBack:
        ...
    @TraceBack.setter
    def TraceBack(self, val: IronPython.Runtime.Exceptions.TraceBack):
        ...

    @property
    def TargetSite(self) -> System.Reflection.MethodBase:
        ...

    @property
    def Message(self) -> str:
        ...

    @property
    def Data(self) -> System.Collections.IDictionary:
        ...

    @property
    def InnerException(self) -> System.Exception:
        ...

    @property
    def HelpLink(self) -> str:
        ...
    @HelpLink.setter
    def HelpLink(self, val: str):
        ...

    @property
    def Source(self) -> str:
        ...
    @Source.setter
    def Source(self, val: str):
        ...

    @property
    def HResult(self) -> int:
        ...
    @HResult.setter
    def HResult(self, val: int):
        ...

    @property
    def StackTrace(self) -> str:
        ...

    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def __init__(self, msg: str, ):
        ...

    @typing.overload
    def __init__(self, message: str, innerException: System.Exception, ):
        ...

    @typing.overload
    def __init__(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext, ):
        ...

    def GetObjectData(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext, ) -> None:
        ...

class ImportException(System.Runtime.Serialization.ISerializable, IronPython.Runtime.Exceptions.IPythonAwareException, System.Exception):
    @typing.overload
    def __init__(self, **kwargs):
        self._message: str
        ...

    # static fields

    # properties
    @property
    def PythonException(self) -> IronPython.Runtime.Exceptions.PythonExceptions.BaseException:
        ...
    @PythonException.setter
    def PythonException(self, val: IronPython.Runtime.Exceptions.PythonExceptions.BaseException):
        ...

    @property
    def Frames(self) -> System.Collections.Generic.List[Microsoft.Scripting.Runtime.DynamicStackFrame]:
        ...
    @Frames.setter
    def Frames(self, val: System.Collections.Generic.List[Microsoft.Scripting.Runtime.DynamicStackFrame]):
        ...

    @property
    def TraceBack(self) -> IronPython.Runtime.Exceptions.TraceBack:
        ...
    @TraceBack.setter
    def TraceBack(self, val: IronPython.Runtime.Exceptions.TraceBack):
        ...

    @property
    def TargetSite(self) -> System.Reflection.MethodBase:
        ...

    @property
    def Message(self) -> str:
        ...

    @property
    def Data(self) -> System.Collections.IDictionary:
        ...

    @property
    def InnerException(self) -> System.Exception:
        ...

    @property
    def HelpLink(self) -> str:
        ...
    @HelpLink.setter
    def HelpLink(self, val: str):
        ...

    @property
    def Source(self) -> str:
        ...
    @Source.setter
    def Source(self, val: str):
        ...

    @property
    def HResult(self) -> int:
        ...
    @HResult.setter
    def HResult(self, val: int):
        ...

    @property
    def StackTrace(self) -> str:
        ...

    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def __init__(self, msg: str, ):
        ...

    @typing.overload
    def __init__(self, message: str, innerException: System.Exception, ):
        ...

    @typing.overload
    def __init__(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext, ):
        ...

    def GetObjectData(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext, ) -> None:
        ...

class NotADirectoryException(System.Runtime.Serialization.ISerializable, IronPython.Runtime.Exceptions.IPythonAwareException, IronPython.Runtime.Exceptions.OSException):
    @typing.overload
    def __init__(self, **kwargs):
        self._message: str
        ...

    # static fields

    # properties
    @property
    def PythonException(self) -> IronPython.Runtime.Exceptions.PythonExceptions.BaseException:
        ...
    @PythonException.setter
    def PythonException(self, val: IronPython.Runtime.Exceptions.PythonExceptions.BaseException):
        ...

    @property
    def Frames(self) -> System.Collections.Generic.List[Microsoft.Scripting.Runtime.DynamicStackFrame]:
        ...
    @Frames.setter
    def Frames(self, val: System.Collections.Generic.List[Microsoft.Scripting.Runtime.DynamicStackFrame]):
        ...

    @property
    def TraceBack(self) -> IronPython.Runtime.Exceptions.TraceBack:
        ...
    @TraceBack.setter
    def TraceBack(self, val: IronPython.Runtime.Exceptions.TraceBack):
        ...

    @property
    def TargetSite(self) -> System.Reflection.MethodBase:
        ...

    @property
    def Message(self) -> str:
        ...

    @property
    def Data(self) -> System.Collections.IDictionary:
        ...

    @property
    def InnerException(self) -> System.Exception:
        ...

    @property
    def HelpLink(self) -> str:
        ...
    @HelpLink.setter
    def HelpLink(self, val: str):
        ...

    @property
    def Source(self) -> str:
        ...
    @Source.setter
    def Source(self, val: str):
        ...

    @property
    def HResult(self) -> int:
        ...
    @HResult.setter
    def HResult(self, val: int):
        ...

    @property
    def StackTrace(self) -> str:
        ...

    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def __init__(self, msg: str, ):
        ...

    @typing.overload
    def __init__(self, message: str, innerException: System.Exception, ):
        ...

    @typing.overload
    def __init__(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext, ):
        ...

    def GetObjectData(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext, ) -> None:
        ...

