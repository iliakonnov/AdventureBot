from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import Microsoft.Scripting.Hosting.Shell
import System
import Microsoft.Scripting.Hosting
import System.Collections.Generic
import IronPython.Runtime.Exceptions
import IronPython.Hosting
import IronPython.Runtime
import Microsoft.Scripting
import Microsoft.Scripting.Runtime


class PythonConsoleOptions(Microsoft.Scripting.Hosting.Shell.ConsoleOptions):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def IgnoreEnvironmentVariables(self) -> bool:
        ...
    @IgnoreEnvironmentVariables.setter
    def IgnoreEnvironmentVariables(self, val: bool):
        ...

    @property
    def SkipImportSite(self) -> bool:
        ...
    @SkipImportSite.setter
    def SkipImportSite(self, val: bool):
        ...

    @property
    def ModuleToRun(self) -> str:
        ...
    @ModuleToRun.setter
    def ModuleToRun(self, val: str):
        ...

    @property
    def SkipFirstSourceLine(self) -> bool:
        ...
    @SkipFirstSourceLine.setter
    def SkipFirstSourceLine(self, val: bool):
        ...

    @property
    def BasicConsole(self) -> bool:
        ...
    @BasicConsole.setter
    def BasicConsole(self, val: bool):
        ...

    @property
    def PrintSysVersion(self) -> bool:
        ...
    @PrintSysVersion.setter
    def PrintSysVersion(self, val: bool):
        ...

    @property
    def AutoIndent(self) -> bool:
        ...
    @AutoIndent.setter
    def AutoIndent(self, val: bool):
        ...

    @property
    def HandleExceptions(self) -> bool:
        ...
    @HandleExceptions.setter
    def HandleExceptions(self, val: bool):
        ...

    @property
    def TabCompletion(self) -> bool:
        ...
    @TabCompletion.setter
    def TabCompletion(self, val: bool):
        ...

    @property
    def ColorfulConsole(self) -> bool:
        ...
    @ColorfulConsole.setter
    def ColorfulConsole(self, val: bool):
        ...

    @property
    def PrintUsage(self) -> bool:
        ...
    @PrintUsage.setter
    def PrintUsage(self, val: bool):
        ...

    @property
    def Command(self) -> str:
        ...
    @Command.setter
    def Command(self, val: str):
        ...

    @property
    def FileName(self) -> str:
        ...
    @FileName.setter
    def FileName(self, val: str):
        ...

    @property
    def PrintVersion(self) -> bool:
        ...
    @PrintVersion.setter
    def PrintVersion(self, val: bool):
        ...

    @property
    def Exit(self) -> bool:
        ...
    @Exit.setter
    def Exit(self, val: bool):
        ...

    @property
    def AutoIndentSize(self) -> int:
        ...
    @AutoIndentSize.setter
    def AutoIndentSize(self, val: int):
        ...

    @property
    def RemainingArgs(self) -> System.Array[str]:
        ...
    @RemainingArgs.setter
    def RemainingArgs(self, val: System.Array[str]):
        ...

    @property
    def Introspection(self) -> bool:
        ...
    @Introspection.setter
    def Introspection(self, val: bool):
        ...

    @property
    def IsMta(self) -> bool:
        ...
    @IsMta.setter
    def IsMta(self, val: bool):
        ...

    # methods
    def __init__(self, ):
        ...

class Python(System.Object, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    @staticmethod
    @typing.overload
    def CreateRuntime() -> Microsoft.Scripting.Hosting.ScriptRuntime:
        ...

    @staticmethod
    @typing.overload
    def CreateRuntime(options: System.Collections.Generic.IDictionary[str, System.Object], ) -> Microsoft.Scripting.Hosting.ScriptRuntime:
        ...

    @staticmethod
    @typing.overload
    def CreateEngine() -> Microsoft.Scripting.Hosting.ScriptEngine:
        ...

    @staticmethod
    @typing.overload
    def CreateEngine(options: System.Collections.Generic.IDictionary[str, System.Object], ) -> Microsoft.Scripting.Hosting.ScriptEngine:
        ...

    @staticmethod
    def GetEngine(runtime: Microsoft.Scripting.Hosting.ScriptRuntime, ) -> Microsoft.Scripting.Hosting.ScriptEngine:
        ...

    @staticmethod
    @typing.overload
    def GetSysModule(runtime: Microsoft.Scripting.Hosting.ScriptRuntime, ) -> Microsoft.Scripting.Hosting.ScriptScope:
        ...

    @staticmethod
    @typing.overload
    def GetSysModule(engine: Microsoft.Scripting.Hosting.ScriptEngine, ) -> Microsoft.Scripting.Hosting.ScriptScope:
        ...

    @staticmethod
    @typing.overload
    def GetBuiltinModule(runtime: Microsoft.Scripting.Hosting.ScriptRuntime, ) -> Microsoft.Scripting.Hosting.ScriptScope:
        ...

    @staticmethod
    @typing.overload
    def GetBuiltinModule(engine: Microsoft.Scripting.Hosting.ScriptEngine, ) -> Microsoft.Scripting.Hosting.ScriptScope:
        ...

    @staticmethod
    @typing.overload
    def GetClrModule(runtime: Microsoft.Scripting.Hosting.ScriptRuntime, ) -> Microsoft.Scripting.Hosting.ScriptScope:
        ...

    @staticmethod
    @typing.overload
    def GetClrModule(engine: Microsoft.Scripting.Hosting.ScriptEngine, ) -> Microsoft.Scripting.Hosting.ScriptScope:
        ...

    @staticmethod
    @typing.overload
    def ImportModule(runtime: Microsoft.Scripting.Hosting.ScriptRuntime, moduleName: str, ) -> Microsoft.Scripting.Hosting.ScriptScope:
        ...

    @staticmethod
    @typing.overload
    def ImportModule(engine: Microsoft.Scripting.Hosting.ScriptEngine, moduleName: str, ) -> Microsoft.Scripting.Hosting.ScriptScope:
        ...

    @staticmethod
    @typing.overload
    def ImportModule(scope: Microsoft.Scripting.Hosting.ScriptScope, moduleName: str, ) -> None:
        ...

    @staticmethod
    @typing.overload
    def SetHostVariables(runtime: Microsoft.Scripting.Hosting.ScriptRuntime, prefix: str, executable: str, version: str, ) -> None:
        ...

    @staticmethod
    @typing.overload
    def SetHostVariables(engine: Microsoft.Scripting.Hosting.ScriptEngine, prefix: str, executable: str, version: str, ) -> None:
        ...

    @staticmethod
    @typing.overload
    def SetTrace(engine: Microsoft.Scripting.Hosting.ScriptEngine, traceFunc: IronPython.Runtime.Exceptions.TracebackDelegate, ) -> None:
        ...

    @staticmethod
    @typing.overload
    def SetTrace(runtime: Microsoft.Scripting.Hosting.ScriptRuntime, traceFunc: IronPython.Runtime.Exceptions.TracebackDelegate, ) -> None:
        ...

    @staticmethod
    @typing.overload
    def CallTracing(runtime: Microsoft.Scripting.Hosting.ScriptRuntime, traceFunc: System.Object, args: System.Array[System.Object], ) -> None:
        ...

    @staticmethod
    @typing.overload
    def CallTracing(engine: Microsoft.Scripting.Hosting.ScriptEngine, traceFunc: System.Object, args: System.Array[System.Object], ) -> None:
        ...

    @staticmethod
    def CreateRuntimeSetup(options: System.Collections.Generic.IDictionary[str, System.Object], ) -> Microsoft.Scripting.Hosting.ScriptRuntimeSetup:
        ...

    @staticmethod
    def CreateLanguageSetup(options: System.Collections.Generic.IDictionary[str, System.Object], ) -> Microsoft.Scripting.Hosting.LanguageSetup:
        ...

    @staticmethod
    @typing.overload
    def CreateModule(engine: Microsoft.Scripting.Hosting.ScriptEngine, name: str, ) -> Microsoft.Scripting.Hosting.ScriptScope:
        ...

    @staticmethod
    @typing.overload
    def CreateModule(engine: Microsoft.Scripting.Hosting.ScriptEngine, name: str, filename: str, ) -> Microsoft.Scripting.Hosting.ScriptScope:
        ...

    @staticmethod
    @typing.overload
    def CreateModule(engine: Microsoft.Scripting.Hosting.ScriptEngine, name: str, filename: str, docString: str, ) -> Microsoft.Scripting.Hosting.ScriptScope:
        ...

    @staticmethod
    def GetModuleFilenames(engine: Microsoft.Scripting.Hosting.ScriptEngine, ) -> System.Array[str]:
        ...

    @staticmethod
    def GetPythonService(engine: Microsoft.Scripting.Hosting.ScriptEngine, ) -> IronPython.Hosting.PythonService:
        ...

    @staticmethod
    def GetPythonContext(engine: Microsoft.Scripting.Hosting.ScriptEngine, ) -> IronPython.Runtime.PythonContext:
        ...

class PythonService(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    def __init__(self, context: IronPython.Runtime.PythonContext, engine: Microsoft.Scripting.Hosting.ScriptEngine, ):
        ...

    def GetSystemState(self, ) -> Microsoft.Scripting.Hosting.ScriptScope:
        ...

    def GetBuiltins(self, ) -> Microsoft.Scripting.Hosting.ScriptScope:
        ...

    def GetClr(self, ) -> Microsoft.Scripting.Hosting.ScriptScope:
        ...

    def CreateModule(self, name: str, filename: str, docString: str, ) -> Microsoft.Scripting.Hosting.ScriptScope:
        ...

    def ImportModule(self, engine: Microsoft.Scripting.Hosting.ScriptEngine, name: str, ) -> Microsoft.Scripting.Hosting.ScriptScope:
        ...

    def GetModuleFilenames(self, ) -> System.Array[str]:
        ...

    def DispatchCommand(self, command: System.Action, ) -> None:
        ...

class PythonOptionsParser(Microsoft.Scripting.Hosting.Shell.OptionsParser[IronPython.Hosting.PythonConsoleOptions]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def ConsoleOptions(self) -> IronPython.Hosting.PythonConsoleOptions:
        ...
    @ConsoleOptions.setter
    def ConsoleOptions(self, val: IronPython.Hosting.PythonConsoleOptions):
        ...

    @property
    def CommonConsoleOptions(self) -> Microsoft.Scripting.Hosting.Shell.ConsoleOptions:
        ...

    @property
    def RuntimeSetup(self) -> Microsoft.Scripting.Hosting.ScriptRuntimeSetup:
        ...

    @property
    def LanguageSetup(self) -> Microsoft.Scripting.Hosting.LanguageSetup:
        ...

    @property
    def Platform(self) -> Microsoft.Scripting.PlatformAdaptationLayer:
        ...

    @property
    def IgnoredArgs(self) -> System.Collections.Generic.IList[str]:
        ...

    # methods
    def __init__(self, ):
        ...

    def HandleOptions(self, options: System.ReadOnlySpan[str], ) -> System.ReadOnlySpan[str]:
        ...

    def ParseArgument(self, arg: str, ) -> None:
        ...

    def HandleImplementationSpecificOption(self, arg: str, val: str, ) -> None:
        ...

    def AfterParse(self, ) -> None:
        ...

    def GetHelp(self, commandLine: ref[str], options: ref[System.Array[str]], environmentVariables: ref[System.Array[str]], comments: ref[str], ) -> None:
        ...

class PythonCommandLine(Microsoft.Scripting.Hosting.Shell.CommandLine):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def PythonContext(self) -> IronPython.Runtime.PythonContext:
        ...

    @property
    def Options(self) -> IronPython.Hosting.PythonConsoleOptions:
        ...

    @property
    def Logo(self) -> str:
        ...

    @property
    def Prompt(self) -> str:
        ...

    @property
    def PromptContinuation(self) -> str:
        ...

    @property
    def ErrorSink(self) -> Microsoft.Scripting.ErrorSink:
        ...

    @property
    def Language(self) -> IronPython.Runtime.PythonContext:
        ...

    @property
    def Console(self) -> Microsoft.Scripting.Hosting.Shell.IConsole:
        ...

    @property
    def Options(self) -> Microsoft.Scripting.Hosting.Shell.ConsoleOptions:
        ...

    @property
    def Engine(self) -> Microsoft.Scripting.Hosting.ScriptEngine:
        ...

    @property
    def ScriptScope(self) -> Microsoft.Scripting.Hosting.ScriptScope:
        ...
    @ScriptScope.setter
    def ScriptScope(self, val: Microsoft.Scripting.Hosting.ScriptScope):
        ...

    @property
    def ExitCode(self) -> int:
        ...
    @ExitCode.setter
    def ExitCode(self, val: int):
        ...

    @property
    def Scope(self) -> Microsoft.Scripting.Runtime.Scope:
        ...
    @Scope.setter
    def Scope(self, val: Microsoft.Scripting.Runtime.Scope):
        ...

    @property
    def Language(self) -> Microsoft.Scripting.Runtime.LanguageContext:
        ...

    # methods
    def __init__(self, ):
        ...

    @staticmethod
    def GetLogoDisplay() -> str:
        ...

    def GetEffectiveExitCode(self, e: IronPython.Runtime.Exceptions.SystemExitException, ) -> int:
        ...

    def Shutdown(self, ) -> None:
        ...

    def Run(self, ) -> int:
        ...

    def RunInteractiveLoop(self, ) -> int:
        ...

    def Initialize(self, ) -> None:
        ...

    def CreateScope(self, ) -> Microsoft.Scripting.Runtime.Scope:
        ...

    def InitializePath(self, pathIndex: ref[int], ) -> None:
        ...

    def InitializeEnvironmentVariables(self, ) -> None:
        ...

    def InitializeModules(self, ) -> None:
        ...

    def InitializeExtensionDLLs(self, ) -> None:
        ...

    def ImportSite(self, ) -> None:
        ...

    def RunInteractive(self, ) -> int:
        ...

    def RunStartup(self, ) -> None:
        ...

    def TryInteractiveAction(self, ) -> System.Nullable[int]:
        ...

    def TryInteractiveActionWorker(self, ) -> System.Nullable[int]:
        ...

    def RunOneInteraction(self, ) -> System.Nullable[int]:
        ...

    def GetNextAutoIndentSize(self, text: str, ) -> int:
        ...

    def RunCommand(self, command: str, ) -> int:
        ...

    def RunCommandWorker(self, command: str, ) -> int:
        ...

    def RunFile(self, fileName: str, ) -> int:
        ...

    def RunFileWorker(self, fileName: str, ) -> int:
        ...

    def GetGlobals(self, name: str, ) -> System.Collections.Generic.IList[str]:
        ...

    def UnhandledException(self, e: System.Exception, ) -> None:
        ...

