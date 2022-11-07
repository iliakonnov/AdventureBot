from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import System
import Microsoft.Scripting.Hosting.Shell
import Microsoft.Scripting.Hosting
import Microsoft.Scripting
import System.Collections.Generic
import System.IO
import Microsoft.Scripting.Runtime

TConsoleOptions = typing.TypeVar('TConsoleOptions')

class ConsoleOptions(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
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
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def __init__(self, options: Microsoft.Scripting.Hosting.Shell.ConsoleOptions, ):
        ...

class OptionsParser(Microsoft.Scripting.Hosting.Shell.OptionsParser, typing.Generic[TConsoleOptions]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def ConsoleOptions(self) -> TConsoleOptions:
        ...
    @ConsoleOptions.setter
    def ConsoleOptions(self, val: TConsoleOptions):
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

    def ParseArgument(self, arg: str, ) -> None:
        ...

    def HandleImplementationSpecificOption(self, arg: str, val: str, ) -> None:
        ...

    @staticmethod
    @typing.overload
    def SetDlrOption(option: str, ) -> None:
        ...

    @staticmethod
    @typing.overload
    def SetDlrOption(option: str, value: str, ) -> None:
        ...

    def GetHelp(self, commandLine: ref[str], options: ref[System.Array[str]], environmentVariables: ref[System.Array[str]], comments: ref[str], ) -> None:
        ...

class OptionsParser(System.Object, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
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
    @abc.abstractmethod
    def CommonConsoleOptions(self) -> Microsoft.Scripting.Hosting.Shell.ConsoleOptions:
        ...

    @property
    def IgnoredArgs(self) -> System.Collections.Generic.IList[str]:
        ...

    # methods
    def __init__(self, ):
        ...

    @abc.abstractmethod
    def ParseArgument(self, arg: str, ) -> None:
        ...

    @abc.abstractmethod
    def GetHelp(self, commandLine: ref[str], options: ref[System.Array[str]], environmentVariables: ref[System.Array[str]], comments: ref[str], ) -> None:
        ...

    def Parse(self, args: System.Array[str], setup: Microsoft.Scripting.Hosting.ScriptRuntimeSetup, languageSetup: Microsoft.Scripting.Hosting.LanguageSetup, platform: Microsoft.Scripting.PlatformAdaptationLayer, ) -> None:
        ...

    def BeforeParse(self, ) -> None:
        ...

    def AfterParse(self, ) -> None:
        ...

    def IgnoreRemainingArgs(self, ) -> None:
        ...

    def PopRemainingArgs(self, ) -> System.Array[str]:
        ...

    def PeekNextArg(self, ) -> str:
        ...

    def PopNextArg(self, ) -> str:
        ...

    def PushArgBack(self, ) -> None:
        ...

    @staticmethod
    def InvalidOptionValue(option: str, value: str, ) -> System.Exception:
        ...

class IConsole(abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    @abc.abstractmethod
    def Output(self) -> System.IO.TextWriter:
        ...
    @Output.setter
    @abc.abstractmethod
    def Output(self, val: System.IO.TextWriter):
        ...

    @property
    @abc.abstractmethod
    def ErrorOutput(self) -> System.IO.TextWriter:
        ...
    @ErrorOutput.setter
    @abc.abstractmethod
    def ErrorOutput(self, val: System.IO.TextWriter):
        ...

    # methods
    @abc.abstractmethod
    def ReadLine(self, autoIndentSize: int, ) -> str:
        ...

    @abc.abstractmethod
    def Write(self, text: str, style: int, ) -> None:
        ...

    @abc.abstractmethod
    @typing.overload
    def WriteLine(self, text: str, style: int, ) -> None:
        ...

    @abc.abstractmethod
    @typing.overload
    def WriteLine(self, ) -> None:
        ...

class CommandLine(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
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

    @property
    def Prompt(self) -> str:
        ...

    @property
    def PromptContinuation(self) -> str:
        ...

    @property
    def Logo(self) -> str:
        ...

    @property
    def ErrorSink(self) -> Microsoft.Scripting.ErrorSink:
        ...

    # methods
    def __init__(self, ):
        ...

    def Shutdown(self, ) -> None:
        ...

    @typing.overload
    def Run(self, ) -> int:
        ...

    @typing.overload
    def Run(self, engine: Microsoft.Scripting.Hosting.ScriptEngine, console: Microsoft.Scripting.Hosting.Shell.IConsole, options: Microsoft.Scripting.Hosting.Shell.ConsoleOptions, ) -> None:
        ...

    def RunInteractiveLoop(self, ) -> int:
        ...

    def Initialize(self, ) -> None:
        ...

    def CreateScope(self, ) -> Microsoft.Scripting.Runtime.Scope:
        ...

    def RunInteractive(self, ) -> int:
        ...

    def TryInteractiveAction(self, ) -> System.Nullable[int]:
        ...

    def GetNextAutoIndentSize(self, text: str, ) -> int:
        ...

    def RunCommand(self, command: str, ) -> int:
        ...

    @typing.overload
    def RunFile(self, fileName: str, ) -> int:
        ...

    @typing.overload
    def RunFile(self, source: Microsoft.Scripting.Hosting.ScriptSource, ) -> int:
        ...

    def GetGlobals(self, name: str, ) -> System.Collections.Generic.IList[str]:
        ...

    def UnhandledException(self, e: System.Exception, ) -> None:
        ...

    def CreateCommandDispatcher(self, ) -> Microsoft.Scripting.Hosting.Shell.ICommandDispatcher:
        ...

    def Terminate(self, exitCode: int, ) -> None:
        ...

    def PrintLogo(self, ) -> None:
        ...

    @staticmethod
    def IsFatalException(e: System.Exception, ) -> bool:
        ...

    def RunOneInteraction(self, ) -> System.Nullable[int]:
        ...

    @typing.overload
    def ExecuteCommand(self, command: str, ) -> None:
        ...

    @typing.overload
    def ExecuteCommand(self, source: Microsoft.Scripting.Hosting.ScriptSource, ) -> System.Object:
        ...

    @staticmethod
    def TreatAsBlankLine(line: str, autoIndentSize: int, ) -> bool:
        ...

    def ReadStatement(self, continueInteraction: ref[bool], ) -> str:
        ...

    def GetCommandProperties(self, code: str, ) -> int:
        ...

    def ReadLine(self, autoIndentSize: int, ) -> str:
        ...

    def GetOutputWriter(self, isErrorOutput: bool, ) -> System.IO.TextWriter:
        ...

    def GetMemberNames(self, code: str, ) -> System.Collections.Generic.IList[str]:
        ...

class ICommandDispatcher(abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    @abc.abstractmethod
    def Execute(self, compiledCode: Microsoft.Scripting.Hosting.CompiledCode, scope: Microsoft.Scripting.Hosting.ScriptScope, ) -> System.Object:
        ...

class Style(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    Prompt: int = ...
    Out: int = ...
    Error: int = ...
    Warning: int = ...

