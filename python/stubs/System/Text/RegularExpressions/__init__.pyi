from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import System.Runtime.Serialization
import System
import System.Text.RegularExpressions
import System.Collections
import System.Globalization
import System.Reflection
import System.Reflection.Emit
import System.Collections.Generic

TState = typing.TypeVar('TState')

class Regex(System.Runtime.Serialization.ISerializable, System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        self.pattern: str
        self.roptions: int
        self.factory: System.Text.RegularExpressions.RegexRunnerFactory
        self.caps: System.Collections.Hashtable
        self.capnames: System.Collections.Hashtable
        self.capslist: System.Array[str]
        self.capsize: int
        self._replref: System.WeakReference[System.Text.RegularExpressions.RegexReplacement]
        self.internalMatchTimeout: System.TimeSpan
        ...

    # static fields
    InfiniteMatchTimeout: System.TimeSpan = ...
    s_defaultMatchTimeout: System.TimeSpan = ...

    # properties
    @property
    def Caps(self) -> System.Collections.IDictionary:
        ...
    @Caps.setter
    def Caps(self, val: System.Collections.IDictionary):
        ...

    @property
    def CapNames(self) -> System.Collections.IDictionary:
        ...
    @CapNames.setter
    def CapNames(self, val: System.Collections.IDictionary):
        ...

    @property
    def Options(self) -> int:
        ...

    @property
    def RightToLeft(self) -> bool:
        ...

    @property
    def CacheSize(self) -> int:
        ...
    @CacheSize.setter
    def CacheSize(self, val: int):
        ...

    @property
    def MatchTimeout(self) -> System.TimeSpan:
        ...

    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def __init__(self, pattern: str, ):
        ...

    @typing.overload
    def __init__(self, pattern: str, options: int, ):
        ...

    @typing.overload
    def __init__(self, pattern: str, options: int, matchTimeout: System.TimeSpan, ):
        ...

    @typing.overload
    def __init__(self, pattern: str, culture: System.Globalization.CultureInfo, ):
        ...

    @typing.overload
    def __init__(self, pattern: str, options: int, matchTimeout: System.TimeSpan, culture: System.Globalization.CultureInfo, ):
        ...

    @typing.overload
    def __init__(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext, ):
        ...

    def Init(self, pattern: str, options: int, matchTimeout: System.TimeSpan, culture: System.Globalization.CultureInfo, ) -> None:
        ...

    @staticmethod
    def ValidatePattern(pattern: str, ) -> None:
        ...

    @staticmethod
    def ValidateOptions(options: int, ) -> None:
        ...

    @staticmethod
    def ValidateMatchTimeout(matchTimeout: System.TimeSpan, ) -> None:
        ...

    def GetObjectData(self, si: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext, ) -> None:
        ...

    @staticmethod
    def Compile(pattern: str, code: System.Text.RegularExpressions.RegexCode, options: int, hasTimeout: bool, ) -> System.Text.RegularExpressions.RegexRunnerFactory:
        ...

    @staticmethod
    @typing.overload
    def CompileToAssembly(regexinfos: System.Array[System.Text.RegularExpressions.RegexCompilationInfo], assemblyname: System.Reflection.AssemblyName, ) -> None:
        ...

    @staticmethod
    @typing.overload
    def CompileToAssembly(regexinfos: System.Array[System.Text.RegularExpressions.RegexCompilationInfo], assemblyname: System.Reflection.AssemblyName, attributes: System.Array[System.Reflection.Emit.CustomAttributeBuilder], ) -> None:
        ...

    @staticmethod
    @typing.overload
    def CompileToAssembly(regexinfos: System.Array[System.Text.RegularExpressions.RegexCompilationInfo], assemblyname: System.Reflection.AssemblyName, attributes: System.Array[System.Reflection.Emit.CustomAttributeBuilder], resourceFile: str, ) -> None:
        ...

    @staticmethod
    def Escape(str: str, ) -> str:
        ...

    @staticmethod
    def Unescape(str: str, ) -> str:
        ...

    def ToString(self, ) -> str:
        ...

    def GetGroupNames(self, ) -> System.Array[str]:
        ...

    def GetGroupNumbers(self, ) -> System.Array[int]:
        ...

    def GroupNameFromNumber(self, i: int, ) -> str:
        ...

    def GroupNumberFromName(self, name: str, ) -> int:
        ...

    def InitializeReferences(self, ) -> None:
        ...

    @typing.overload
    def Run(self, quick: bool, prevlen: int, input: str, beginning: int, length: int, startat: int, ) -> System.Text.RegularExpressions.Match:
        ...

    @typing.overload
    def Run(self, input: str, startat: int, state: ref[TState], callback: System.Text.RegularExpressions.MatchCallback[TState], reuseMatchObject: bool, ) -> None:
        ...

    def RentRunner(self, ) -> System.Text.RegularExpressions.RegexRunner:
        ...

    def ReturnRunner(self, runner: System.Text.RegularExpressions.RegexRunner, ) -> None:
        ...

    def UseOptionC(self, ) -> bool:
        ...

    def UseOptionR(self, ) -> bool:
        ...

    def UseOptionInvariant(self, ) -> bool:
        ...

    @staticmethod
    @typing.overload
    def IsMatch(input: str, pattern: str, ) -> bool:
        ...

    @staticmethod
    @typing.overload
    def IsMatch(input: str, pattern: str, options: int, ) -> bool:
        ...

    @staticmethod
    @typing.overload
    def IsMatch(input: str, pattern: str, options: int, matchTimeout: System.TimeSpan, ) -> bool:
        ...

    @typing.overload
    def IsMatch(self, input: str, ) -> bool:
        ...

    @typing.overload
    def IsMatch(self, input: str, startat: int, ) -> bool:
        ...

    @staticmethod
    @typing.overload
    def Match(input: str, pattern: str, ) -> System.Text.RegularExpressions.Match:
        ...

    @staticmethod
    @typing.overload
    def Match(input: str, pattern: str, options: int, ) -> System.Text.RegularExpressions.Match:
        ...

    @staticmethod
    @typing.overload
    def Match(input: str, pattern: str, options: int, matchTimeout: System.TimeSpan, ) -> System.Text.RegularExpressions.Match:
        ...

    @typing.overload
    def Match(self, input: str, ) -> System.Text.RegularExpressions.Match:
        ...

    @typing.overload
    def Match(self, input: str, startat: int, ) -> System.Text.RegularExpressions.Match:
        ...

    @typing.overload
    def Match(self, input: str, beginning: int, length: int, ) -> System.Text.RegularExpressions.Match:
        ...

    @staticmethod
    @typing.overload
    def Matches(input: str, pattern: str, ) -> System.Text.RegularExpressions.MatchCollection:
        ...

    @staticmethod
    @typing.overload
    def Matches(input: str, pattern: str, options: int, ) -> System.Text.RegularExpressions.MatchCollection:
        ...

    @staticmethod
    @typing.overload
    def Matches(input: str, pattern: str, options: int, matchTimeout: System.TimeSpan, ) -> System.Text.RegularExpressions.MatchCollection:
        ...

    @typing.overload
    def Matches(self, input: str, ) -> System.Text.RegularExpressions.MatchCollection:
        ...

    @typing.overload
    def Matches(self, input: str, startat: int, ) -> System.Text.RegularExpressions.MatchCollection:
        ...

    @staticmethod
    @typing.overload
    def Replace(input: str, pattern: str, replacement: str, ) -> str:
        ...

    @staticmethod
    @typing.overload
    def Replace(input: str, pattern: str, replacement: str, options: int, ) -> str:
        ...

    @staticmethod
    @typing.overload
    def Replace(input: str, pattern: str, replacement: str, options: int, matchTimeout: System.TimeSpan, ) -> str:
        ...

    @typing.overload
    def Replace(self, input: str, replacement: str, ) -> str:
        ...

    @typing.overload
    def Replace(self, input: str, replacement: str, count: int, ) -> str:
        ...

    @typing.overload
    def Replace(self, input: str, replacement: str, count: int, startat: int, ) -> str:
        ...

    @staticmethod
    @typing.overload
    def Replace(input: str, pattern: str, evaluator: System.Text.RegularExpressions.MatchEvaluator, ) -> str:
        ...

    @staticmethod
    @typing.overload
    def Replace(input: str, pattern: str, evaluator: System.Text.RegularExpressions.MatchEvaluator, options: int, ) -> str:
        ...

    @staticmethod
    @typing.overload
    def Replace(input: str, pattern: str, evaluator: System.Text.RegularExpressions.MatchEvaluator, options: int, matchTimeout: System.TimeSpan, ) -> str:
        ...

    @typing.overload
    def Replace(self, input: str, evaluator: System.Text.RegularExpressions.MatchEvaluator, ) -> str:
        ...

    @typing.overload
    def Replace(self, input: str, evaluator: System.Text.RegularExpressions.MatchEvaluator, count: int, ) -> str:
        ...

    @typing.overload
    def Replace(self, input: str, evaluator: System.Text.RegularExpressions.MatchEvaluator, count: int, startat: int, ) -> str:
        ...

    @staticmethod
    @typing.overload
    def Replace(evaluator: System.Text.RegularExpressions.MatchEvaluator, regex: System.Text.RegularExpressions.Regex, input: str, count: int, startat: int, ) -> str:
        ...

    @staticmethod
    @typing.overload
    def Split(input: str, pattern: str, ) -> System.Array[str]:
        ...

    @staticmethod
    @typing.overload
    def Split(input: str, pattern: str, options: int, ) -> System.Array[str]:
        ...

    @staticmethod
    @typing.overload
    def Split(input: str, pattern: str, options: int, matchTimeout: System.TimeSpan, ) -> System.Array[str]:
        ...

    @typing.overload
    def Split(self, input: str, ) -> System.Array[str]:
        ...

    @typing.overload
    def Split(self, input: str, count: int, ) -> System.Array[str]:
        ...

    @typing.overload
    def Split(self, input: str, count: int, startat: int, ) -> System.Array[str]:
        ...

    @staticmethod
    @typing.overload
    def Split(regex: System.Text.RegularExpressions.Regex, input: str, count: int, startat: int, ) -> System.Array[str]:
        ...

    @staticmethod
    def InitDefaultMatchTimeout() -> System.TimeSpan:
        ...

class MatchCollection(System.Collections.Generic.IList[System.Text.RegularExpressions.Match], System.Collections.Generic.ICollection[System.Text.RegularExpressions.Match], System.Collections.Generic.IEnumerable[System.Text.RegularExpressions.Match], System.Collections.IEnumerable, System.Collections.Generic.IReadOnlyList[System.Text.RegularExpressions.Match], System.Collections.Generic.IReadOnlyCollection[System.Text.RegularExpressions.Match], System.Collections.IList, System.Collections.ICollection, System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def IsReadOnly(self) -> bool:
        ...

    @property
    def Count(self) -> int:
        ...

    @property
    def Item(self) -> System.Text.RegularExpressions.Match:
        ...

    @property
    def IsSynchronized(self) -> bool:
        ...

    @property
    def SyncRoot(self) -> System.Object:
        ...

    @property
    def Item(self) -> System.Text.RegularExpressions.Match:
        ...
    @Item.setter
    def Item(self, val: System.Text.RegularExpressions.Match):
        ...

    @property
    def IsFixedSize(self) -> bool:
        ...

    @property
    def Item(self) -> System.Object:
        ...
    @Item.setter
    def Item(self, val: System.Object):
        ...

    # methods
    def __init__(self, regex: System.Text.RegularExpressions.Regex, input: str, startat: int, ):
        ...

    def GetEnumerator(self, ) -> System.Collections.IEnumerator:
        ...

    def GetEnumerator(self, ) -> System.Collections.Generic.IEnumerator[System.Text.RegularExpressions.Match]:
        ...

    def GetMatch(self, i: int, ) -> System.Text.RegularExpressions.Match:
        ...

    def EnsureInitialized(self, ) -> None:
        ...

    @typing.overload
    def CopyTo(self, array: System.Array, arrayIndex: int, ) -> None:
        ...

    @typing.overload
    def CopyTo(self, array: System.Array[System.Text.RegularExpressions.Match], arrayIndex: int, ) -> None:
        ...

    def IndexOf(self, item: System.Text.RegularExpressions.Match, ) -> int:
        ...

    def Insert(self, index: int, item: System.Text.RegularExpressions.Match, ) -> None:
        ...

    def RemoveAt(self, index: int, ) -> None:
        ...

    def Add(self, item: System.Text.RegularExpressions.Match, ) -> None:
        ...

    def Clear(self, ) -> None:
        ...

    def Contains(self, item: System.Text.RegularExpressions.Match, ) -> bool:
        ...

    def Remove(self, item: System.Text.RegularExpressions.Match, ) -> bool:
        ...

    def Add(self, value: System.Object, ) -> int:
        ...

    def Clear(self, ) -> None:
        ...

    def Contains(self, value: System.Object, ) -> bool:
        ...

    def IndexOf(self, value: System.Object, ) -> int:
        ...

    def Insert(self, index: int, value: System.Object, ) -> None:
        ...

    def Remove(self, value: System.Object, ) -> None:
        ...

    def RemoveAt(self, index: int, ) -> None:
        ...

class RegexRunnerFactory(System.Object, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    def __init__(self, ):
        ...

    @abc.abstractmethod
    def CreateInstance(self, ) -> System.Text.RegularExpressions.RegexRunner:
        ...

class RegexRunner(System.Object, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        self.runtextbeg: int
        self.runtextend: int
        self.runtextstart: int
        self.runtext: str
        self.runtextpos: int
        self.runtrack: System.Array[int]
        self.runtrackpos: int
        self.runstack: System.Array[int]
        self.runstackpos: int
        self.runcrawl: System.Array[int]
        self.runcrawlpos: int
        self.runtrackcount: int
        self.runmatch: System.Text.RegularExpressions.Match
        self.runregex: System.Text.RegularExpressions.Regex
        ...

    # static fields

    # properties
    # methods
    def __init__(self, ):
        ...

    @typing.overload
    def Scan(self, regex: System.Text.RegularExpressions.Regex, text: str, textbeg: int, textend: int, textstart: int, prevlen: int, quick: bool, ) -> System.Text.RegularExpressions.Match:
        ...

    @typing.overload
    def Scan(self, regex: System.Text.RegularExpressions.Regex, text: str, textbeg: int, textend: int, textstart: int, prevlen: int, quick: bool, timeout: System.TimeSpan, ) -> System.Text.RegularExpressions.Match:
        ...

    @typing.overload
    def Scan(self, regex: System.Text.RegularExpressions.Regex, text: str, textstart: int, state: ref[TState], callback: System.Text.RegularExpressions.MatchCallback[TState], reuseMatchObject: bool, timeout: System.TimeSpan, ) -> None:
        ...

    def CheckTimeout(self, ) -> None:
        ...

    def DoCheckTimeout(self, ) -> None:
        ...

    @abc.abstractmethod
    def Go(self, ) -> None:
        ...

    @abc.abstractmethod
    def FindFirstChar(self, ) -> bool:
        ...

    @abc.abstractmethod
    def InitTrackCount(self, ) -> None:
        ...

    def InitializeForGo(self, ) -> None:
        ...

    def EnsureStorage(self, ) -> None:
        ...

    def IsBoundary(self, index: int, startpos: int, endpos: int, ) -> bool:
        ...

    def IsECMABoundary(self, index: int, startpos: int, endpos: int, ) -> bool:
        ...

    @staticmethod
    def CharInSet(ch: str, set: str, category: str, ) -> bool:
        ...

    @staticmethod
    def CharInClass(ch: str, charClass: str, ) -> bool:
        ...

    def DoubleTrack(self, ) -> None:
        ...

    def DoubleStack(self, ) -> None:
        ...

    def DoubleCrawl(self, ) -> None:
        ...

    def Crawl(self, i: int, ) -> None:
        ...

    def Popcrawl(self, ) -> int:
        ...

    def Crawlpos(self, ) -> int:
        ...

    def Capture(self, capnum: int, start: int, end: int, ) -> None:
        ...

    def TransferCapture(self, capnum: int, uncapnum: int, start: int, end: int, ) -> None:
        ...

    def Uncapture(self, ) -> None:
        ...

    def IsMatched(self, cap: int, ) -> bool:
        ...

    def MatchIndex(self, cap: int, ) -> int:
        ...

    def MatchLength(self, cap: int, ) -> int:
        ...

class RegexOptions(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    None_: int = ...
    IgnoreCase: int = ...
    Multiline: int = ...
    ExplicitCapture: int = ...
    Compiled: int = ...
    Singleline: int = ...
    IgnorePatternWhitespace: int = ...
    RightToLeft: int = ...
    ECMAScript: int = ...
    CultureInvariant: int = ...

class MatchEvaluator(System.ICloneable, System.Runtime.Serialization.ISerializable, System.MulticastDelegate):
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

    def Invoke(self, match: System.Text.RegularExpressions.Match, ) -> str:
        ...

    def BeginInvoke(self, match: System.Text.RegularExpressions.Match, callback: System.AsyncCallback, object: System.Object, ) -> System.IAsyncResult:
        ...

    def EndInvoke(self, result: System.IAsyncResult, ) -> str:
        ...

class Match(System.Text.RegularExpressions.Group):
    @typing.overload
    def __init__(self, **kwargs):
        self._groupcoll: System.Text.RegularExpressions.GroupCollection
        self._regex: System.Text.RegularExpressions.Regex
        self._textbeg: int
        self._textpos: int
        self._textend: int
        self._textstart: int
        self._matches: System.Array[System.Array[int]]
        self._matchcount: System.Array[int]
        self._balancing: bool
        self._caps: System.Array[int]
        self._capcount: int
        self._capcoll: System.Text.RegularExpressions.CaptureCollection
        ...

    # static fields

    # properties
    @property
    def Empty(self) -> System.Text.RegularExpressions.Match:
        ...

    @property
    def Groups(self) -> System.Text.RegularExpressions.GroupCollection:
        ...

    @property
    def Success(self) -> bool:
        ...

    @property
    def Name(self) -> str:
        ...

    @property
    def Captures(self) -> System.Text.RegularExpressions.CaptureCollection:
        ...

    @property
    def Index(self) -> int:
        ...
    @Index.setter
    def Index(self, val: int):
        ...

    @property
    def Length(self) -> int:
        ...
    @Length.setter
    def Length(self, val: int):
        ...

    @property
    def Text(self) -> str:
        ...
    @Text.setter
    def Text(self, val: str):
        ...

    @property
    def Value(self) -> str:
        ...

    @property
    def ValueSpan(self) -> System.ReadOnlySpan[str]:
        ...

    # methods
    def __init__(self, regex: System.Text.RegularExpressions.Regex, capcount: int, text: str, begpos: int, len: int, startpos: int, ):
        ...

    def Reset(self, regex: System.Text.RegularExpressions.Regex, text: str, textbeg: int, textend: int, textstart: int, ) -> None:
        ...

    def NextMatch(self, ) -> System.Text.RegularExpressions.Match:
        ...

    def Result(self, replacement: str, ) -> str:
        ...

    def GroupToStringImpl(self, groupnum: int, ) -> System.ReadOnlyMemory[str]:
        ...

    def LastGroupToStringImpl(self, ) -> System.ReadOnlyMemory[str]:
        ...

    @staticmethod
    def Synchronized(inner: System.Text.RegularExpressions.Match, ) -> System.Text.RegularExpressions.Match:
        ...

    def AddMatch(self, cap: int, start: int, len: int, ) -> None:
        ...

    def BalanceMatch(self, cap: int, ) -> None:
        ...

    def RemoveMatch(self, cap: int, ) -> None:
        ...

    def IsMatched(self, cap: int, ) -> bool:
        ...

    def MatchIndex(self, cap: int, ) -> int:
        ...

    def MatchLength(self, cap: int, ) -> int:
        ...

    def Tidy(self, textpos: int, ) -> None:
        ...

    def TidyBalancing(self, ) -> None:
        ...

class Group(System.Text.RegularExpressions.Capture):
    @typing.overload
    def __init__(self, **kwargs):
        self._caps: System.Array[int]
        self._capcount: int
        self._capcoll: System.Text.RegularExpressions.CaptureCollection
        ...

    # static fields
    s_emptyGroup: System.Text.RegularExpressions.Group = ...

    # properties
    @property
    def Success(self) -> bool:
        ...

    @property
    def Name(self) -> str:
        ...

    @property
    def Captures(self) -> System.Text.RegularExpressions.CaptureCollection:
        ...

    @property
    def Index(self) -> int:
        ...
    @Index.setter
    def Index(self, val: int):
        ...

    @property
    def Length(self) -> int:
        ...
    @Length.setter
    def Length(self, val: int):
        ...

    @property
    def Text(self) -> str:
        ...
    @Text.setter
    def Text(self, val: str):
        ...

    @property
    def Value(self) -> str:
        ...

    @property
    def ValueSpan(self) -> System.ReadOnlySpan[str]:
        ...

    # methods
    def __init__(self, text: str, caps: System.Array[int], capcount: int, name: str, ):
        ...

    @staticmethod
    def Synchronized(inner: System.Text.RegularExpressions.Group, ) -> System.Text.RegularExpressions.Group:
        ...

class Capture(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def Index(self) -> int:
        ...
    @Index.setter
    def Index(self, val: int):
        ...

    @property
    def Length(self) -> int:
        ...
    @Length.setter
    def Length(self, val: int):
        ...

    @property
    def Text(self) -> str:
        ...
    @Text.setter
    def Text(self, val: str):
        ...

    @property
    def Value(self) -> str:
        ...

    @property
    def ValueSpan(self) -> System.ReadOnlySpan[str]:
        ...

    # methods
    def __init__(self, text: str, index: int, length: int, ):
        ...

    def ToString(self, ) -> str:
        ...

    def GetLeftSubstring(self, ) -> System.ReadOnlyMemory[str]:
        ...

    def GetRightSubstring(self, ) -> System.ReadOnlyMemory[str]:
        ...

class CaptureCollection(System.Collections.Generic.IList[System.Text.RegularExpressions.Capture], System.Collections.Generic.ICollection[System.Text.RegularExpressions.Capture], System.Collections.Generic.IEnumerable[System.Text.RegularExpressions.Capture], System.Collections.IEnumerable, System.Collections.Generic.IReadOnlyList[System.Text.RegularExpressions.Capture], System.Collections.Generic.IReadOnlyCollection[System.Text.RegularExpressions.Capture], System.Collections.IList, System.Collections.ICollection, System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def IsReadOnly(self) -> bool:
        ...

    @property
    def Count(self) -> int:
        ...

    @property
    def Item(self) -> System.Text.RegularExpressions.Capture:
        ...

    @property
    def IsSynchronized(self) -> bool:
        ...

    @property
    def SyncRoot(self) -> System.Object:
        ...

    @property
    def Item(self) -> System.Text.RegularExpressions.Capture:
        ...
    @Item.setter
    def Item(self, val: System.Text.RegularExpressions.Capture):
        ...

    @property
    def IsFixedSize(self) -> bool:
        ...

    @property
    def Item(self) -> System.Object:
        ...
    @Item.setter
    def Item(self, val: System.Object):
        ...

    # methods
    def __init__(self, group: System.Text.RegularExpressions.Group, ):
        ...

    def GetEnumerator(self, ) -> System.Collections.IEnumerator:
        ...

    def GetEnumerator(self, ) -> System.Collections.Generic.IEnumerator[System.Text.RegularExpressions.Capture]:
        ...

    def GetCapture(self, i: int, ) -> System.Text.RegularExpressions.Capture:
        ...

    def ForceInitialized(self, ) -> None:
        ...

    @typing.overload
    def CopyTo(self, array: System.Array, arrayIndex: int, ) -> None:
        ...

    @typing.overload
    def CopyTo(self, array: System.Array[System.Text.RegularExpressions.Capture], arrayIndex: int, ) -> None:
        ...

    def IndexOf(self, item: System.Text.RegularExpressions.Capture, ) -> int:
        ...

    def Insert(self, index: int, item: System.Text.RegularExpressions.Capture, ) -> None:
        ...

    def RemoveAt(self, index: int, ) -> None:
        ...

    def Add(self, item: System.Text.RegularExpressions.Capture, ) -> None:
        ...

    def Clear(self, ) -> None:
        ...

    def Contains(self, item: System.Text.RegularExpressions.Capture, ) -> bool:
        ...

    def Remove(self, item: System.Text.RegularExpressions.Capture, ) -> bool:
        ...

    def Add(self, value: System.Object, ) -> int:
        ...

    def Clear(self, ) -> None:
        ...

    def Contains(self, value: System.Object, ) -> bool:
        ...

    def IndexOf(self, value: System.Object, ) -> int:
        ...

    def Insert(self, index: int, value: System.Object, ) -> None:
        ...

    def Remove(self, value: System.Object, ) -> None:
        ...

    def RemoveAt(self, index: int, ) -> None:
        ...

class GroupCollection(System.Collections.Generic.IList[System.Text.RegularExpressions.Group], System.Collections.Generic.ICollection[System.Text.RegularExpressions.Group], System.Collections.Generic.IEnumerable[System.Text.RegularExpressions.Group], System.Collections.IEnumerable, System.Collections.Generic.IReadOnlyList[System.Text.RegularExpressions.Group], System.Collections.Generic.IReadOnlyCollection[System.Text.RegularExpressions.Group], System.Collections.IList, System.Collections.ICollection, System.Collections.Generic.IReadOnlyDictionary[str, System.Text.RegularExpressions.Group], System.Collections.Generic.IReadOnlyCollection[System.Collections.Generic.KeyValuePair[str, System.Text.RegularExpressions.Group]], System.Collections.Generic.IEnumerable[System.Collections.Generic.KeyValuePair[str, System.Text.RegularExpressions.Group]], System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def IsReadOnly(self) -> bool:
        ...

    @property
    def Count(self) -> int:
        ...

    @property
    def Item(self) -> System.Text.RegularExpressions.Group:
        ...

    @property
    def Item(self) -> System.Text.RegularExpressions.Group:
        ...

    @property
    def IsSynchronized(self) -> bool:
        ...

    @property
    def SyncRoot(self) -> System.Object:
        ...

    @property
    def Item(self) -> System.Text.RegularExpressions.Group:
        ...
    @Item.setter
    def Item(self, val: System.Text.RegularExpressions.Group):
        ...

    @property
    def IsFixedSize(self) -> bool:
        ...

    @property
    def Item(self) -> System.Object:
        ...
    @Item.setter
    def Item(self, val: System.Object):
        ...

    @property
    def Keys(self) -> System.Collections.Generic.IEnumerable[str]:
        ...

    @property
    def Values(self) -> System.Collections.Generic.IEnumerable[System.Text.RegularExpressions.Group]:
        ...

    # methods
    def __init__(self, match: System.Text.RegularExpressions.Match, caps: System.Collections.Hashtable, ):
        ...

    def Reset(self, ) -> None:
        ...

    def GetEnumerator(self, ) -> System.Collections.IEnumerator:
        ...

    def GetEnumerator(self, ) -> System.Collections.Generic.IEnumerator[System.Text.RegularExpressions.Group]:
        ...

    def GetGroup(self, groupnum: int, ) -> System.Text.RegularExpressions.Group:
        ...

    def GetGroupImpl(self, groupnum: int, ) -> System.Text.RegularExpressions.Group:
        ...

    @typing.overload
    def CopyTo(self, array: System.Array, arrayIndex: int, ) -> None:
        ...

    @typing.overload
    def CopyTo(self, array: System.Array[System.Text.RegularExpressions.Group], arrayIndex: int, ) -> None:
        ...

    def IndexOf(self, item: System.Text.RegularExpressions.Group, ) -> int:
        ...

    def Insert(self, index: int, item: System.Text.RegularExpressions.Group, ) -> None:
        ...

    def RemoveAt(self, index: int, ) -> None:
        ...

    def Add(self, item: System.Text.RegularExpressions.Group, ) -> None:
        ...

    def Clear(self, ) -> None:
        ...

    def Contains(self, item: System.Text.RegularExpressions.Group, ) -> bool:
        ...

    def Remove(self, item: System.Text.RegularExpressions.Group, ) -> bool:
        ...

    def Add(self, value: System.Object, ) -> int:
        ...

    def Clear(self, ) -> None:
        ...

    def Contains(self, value: System.Object, ) -> bool:
        ...

    def IndexOf(self, value: System.Object, ) -> int:
        ...

    def Insert(self, index: int, value: System.Object, ) -> None:
        ...

    def Remove(self, value: System.Object, ) -> None:
        ...

    def RemoveAt(self, index: int, ) -> None:
        ...

    def GetEnumerator(self, ) -> System.Collections.Generic.IEnumerator[System.Collections.Generic.KeyValuePair[str, System.Text.RegularExpressions.Group]]:
        ...

    def TryGetValue(self, key: str, value: ref[System.Text.RegularExpressions.Group], ) -> bool:
        ...

    def ContainsKey(self, key: str, ) -> bool:
        ...

class RegexCompilationInfo(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def IsPublic(self) -> bool:
        ...
    @IsPublic.setter
    def IsPublic(self, val: bool):
        ...

    @property
    def MatchTimeout(self) -> System.TimeSpan:
        ...
    @MatchTimeout.setter
    def MatchTimeout(self, val: System.TimeSpan):
        ...

    @property
    def Name(self) -> str:
        ...
    @Name.setter
    def Name(self, val: str):
        ...

    @property
    def Namespace(self) -> str:
        ...
    @Namespace.setter
    def Namespace(self, val: str):
        ...

    @property
    def Options(self) -> int:
        ...
    @Options.setter
    def Options(self, val: int):
        ...

    @property
    def Pattern(self) -> str:
        ...
    @Pattern.setter
    def Pattern(self, val: str):
        ...

    # methods
    @typing.overload
    def __init__(self, pattern: str, options: int, name: str, fullnamespace: str, ispublic: bool, ):
        ...

    @typing.overload
    def __init__(self, pattern: str, options: int, name: str, fullnamespace: str, ispublic: bool, matchTimeout: System.TimeSpan, ):
        ...

