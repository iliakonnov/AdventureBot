from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import System
import System.Globalization
import System.Collections.Generic
import System.Threading
import System.Runtime.Serialization
import System.Text
import System.Globalization.DateTimeFormatInfo
import System.Reflection


class NumberStyles(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    None_: int = ...
    AllowLeadingWhite: int = ...
    AllowTrailingWhite: int = ...
    AllowLeadingSign: int = ...
    Integer: int = ...
    AllowTrailingSign: int = ...
    AllowParentheses: int = ...
    AllowDecimalPoint: int = ...
    AllowThousands: int = ...
    Number: int = ...
    AllowExponent: int = ...
    Float: int = ...
    AllowCurrencySymbol: int = ...
    Currency: int = ...
    Any: int = ...
    AllowHexSpecifier: int = ...
    HexNumber: int = ...

class TimeSpanStyles(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    None_: int = ...
    AssumeNegative: int = ...

class Calendar(System.ICloneable, System.Object, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        self._twoDigitYearMax: int
        ...

    # static fields
    CurrentEra: int = ...

    # properties
    @property
    def MinSupportedDateTime(self) -> System.DateTime:
        ...

    @property
    def MaxSupportedDateTime(self) -> System.DateTime:
        ...

    @property
    def AlgorithmType(self) -> int:
        ...

    @property
    def ID(self) -> int:
        ...

    @property
    def BaseCalendarID(self) -> int:
        ...

    @property
    def IsReadOnly(self) -> bool:
        ...

    @property
    def CurrentEraValue(self) -> int:
        ...

    @property
    @abc.abstractmethod
    def Eras(self) -> System.Array[int]:
        ...

    @property
    def DaysInYearBeforeMinSupportedYear(self) -> int:
        ...

    @property
    def TwoDigitYearMax(self) -> int:
        ...
    @TwoDigitYearMax.setter
    def TwoDigitYearMax(self, val: int):
        ...

    # methods
    def __init__(self, ):
        ...

    def Clone(self, ) -> System.Object:
        ...

    @staticmethod
    def ReadOnly(calendar: System.Globalization.Calendar, ) -> System.Globalization.Calendar:
        ...

    def VerifyWritable(self, ) -> None:
        ...

    def SetReadOnlyState(self, readOnly: bool, ) -> None:
        ...

    @staticmethod
    def CheckAddResult(ticks: int, minValue: System.DateTime, maxValue: System.DateTime, ) -> None:
        ...

    def Add(self, time: System.DateTime, value: float, scale: int, ) -> System.DateTime:
        ...

    def AddMilliseconds(self, time: System.DateTime, milliseconds: float, ) -> System.DateTime:
        ...

    def AddDays(self, time: System.DateTime, days: int, ) -> System.DateTime:
        ...

    def AddHours(self, time: System.DateTime, hours: int, ) -> System.DateTime:
        ...

    def AddMinutes(self, time: System.DateTime, minutes: int, ) -> System.DateTime:
        ...

    @abc.abstractmethod
    def AddMonths(self, time: System.DateTime, months: int, ) -> System.DateTime:
        ...

    def AddSeconds(self, time: System.DateTime, seconds: int, ) -> System.DateTime:
        ...

    def AddWeeks(self, time: System.DateTime, weeks: int, ) -> System.DateTime:
        ...

    @abc.abstractmethod
    def AddYears(self, time: System.DateTime, years: int, ) -> System.DateTime:
        ...

    @abc.abstractmethod
    def GetDayOfMonth(self, time: System.DateTime, ) -> int:
        ...

    @abc.abstractmethod
    def GetDayOfWeek(self, time: System.DateTime, ) -> int:
        ...

    @abc.abstractmethod
    def GetDayOfYear(self, time: System.DateTime, ) -> int:
        ...

    @typing.overload
    def GetDaysInMonth(self, year: int, month: int, ) -> int:
        ...

    @abc.abstractmethod
    @typing.overload
    def GetDaysInMonth(self, year: int, month: int, era: int, ) -> int:
        ...

    @typing.overload
    def GetDaysInYear(self, year: int, ) -> int:
        ...

    @abc.abstractmethod
    @typing.overload
    def GetDaysInYear(self, year: int, era: int, ) -> int:
        ...

    @abc.abstractmethod
    def GetEra(self, time: System.DateTime, ) -> int:
        ...

    def GetHour(self, time: System.DateTime, ) -> int:
        ...

    def GetMilliseconds(self, time: System.DateTime, ) -> float:
        ...

    def GetMinute(self, time: System.DateTime, ) -> int:
        ...

    @abc.abstractmethod
    def GetMonth(self, time: System.DateTime, ) -> int:
        ...

    @typing.overload
    def GetMonthsInYear(self, year: int, ) -> int:
        ...

    @abc.abstractmethod
    @typing.overload
    def GetMonthsInYear(self, year: int, era: int, ) -> int:
        ...

    def GetSecond(self, time: System.DateTime, ) -> int:
        ...

    def GetFirstDayWeekOfYear(self, time: System.DateTime, firstDayOfWeek: int, ) -> int:
        ...

    def GetWeekOfYearFullDays(self, time: System.DateTime, firstDayOfWeek: int, fullDays: int, ) -> int:
        ...

    def GetWeekOfYearOfMinSupportedDateTime(self, firstDayOfWeek: int, minimumDaysInFirstWeek: int, ) -> int:
        ...

    def GetWeekOfYear(self, time: System.DateTime, rule: int, firstDayOfWeek: int, ) -> int:
        ...

    @abc.abstractmethod
    def GetYear(self, time: System.DateTime, ) -> int:
        ...

    @typing.overload
    def IsLeapDay(self, year: int, month: int, day: int, ) -> bool:
        ...

    @abc.abstractmethod
    @typing.overload
    def IsLeapDay(self, year: int, month: int, day: int, era: int, ) -> bool:
        ...

    @typing.overload
    def IsLeapMonth(self, year: int, month: int, ) -> bool:
        ...

    @abc.abstractmethod
    @typing.overload
    def IsLeapMonth(self, year: int, month: int, era: int, ) -> bool:
        ...

    @typing.overload
    def GetLeapMonth(self, year: int, ) -> int:
        ...

    @typing.overload
    def GetLeapMonth(self, year: int, era: int, ) -> int:
        ...

    @typing.overload
    def IsLeapYear(self, year: int, ) -> bool:
        ...

    @abc.abstractmethod
    @typing.overload
    def IsLeapYear(self, year: int, era: int, ) -> bool:
        ...

    @typing.overload
    def ToDateTime(self, year: int, month: int, day: int, hour: int, minute: int, second: int, millisecond: int, ) -> System.DateTime:
        ...

    @abc.abstractmethod
    @typing.overload
    def ToDateTime(self, year: int, month: int, day: int, hour: int, minute: int, second: int, millisecond: int, era: int, ) -> System.DateTime:
        ...

    def TryToDateTime(self, year: int, month: int, day: int, hour: int, minute: int, second: int, millisecond: int, era: int, result: ref[System.DateTime], ) -> bool:
        ...

    def IsValidYear(self, year: int, era: int, ) -> bool:
        ...

    def IsValidMonth(self, year: int, month: int, era: int, ) -> bool:
        ...

    def IsValidDay(self, year: int, month: int, day: int, era: int, ) -> bool:
        ...

    def ToFourDigitYear(self, year: int, ) -> int:
        ...

    @staticmethod
    def TimeToTicks(hour: int, minute: int, second: int, millisecond: int, ) -> int:
        ...

    @staticmethod
    def GetSystemTwoDigitYearSetting(CalID: int, defaultYearValue: int, ) -> int:
        ...

class CultureInfo(System.IFormatProvider, System.ICloneable, System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        self._numInfo: System.Globalization.NumberFormatInfo
        self._dateTimeInfo: System.Globalization.DateTimeFormatInfo
        self._cultureData: System.Globalization.CultureData
        self._isInherited: bool
        self._name: str
        ...

    # static fields
    LOCALE_NEUTRAL: int = ...
    LOCALE_CUSTOM_UNSPECIFIED: int = ...
    LOCALE_CUSTOM_DEFAULT: int = ...
    LOCALE_INVARIANT: int = ...

    # properties
    @property
    def CurrentCulture(self) -> System.Globalization.CultureInfo:
        ...
    @CurrentCulture.setter
    def CurrentCulture(self, val: System.Globalization.CultureInfo):
        ...

    @property
    def CurrentUICulture(self) -> System.Globalization.CultureInfo:
        ...
    @CurrentUICulture.setter
    def CurrentUICulture(self, val: System.Globalization.CultureInfo):
        ...

    @property
    def UserDefaultUICulture(self) -> System.Globalization.CultureInfo:
        ...

    @property
    def InstalledUICulture(self) -> System.Globalization.CultureInfo:
        ...

    @property
    def DefaultThreadCurrentCulture(self) -> System.Globalization.CultureInfo:
        ...
    @DefaultThreadCurrentCulture.setter
    def DefaultThreadCurrentCulture(self, val: System.Globalization.CultureInfo):
        ...

    @property
    def DefaultThreadCurrentUICulture(self) -> System.Globalization.CultureInfo:
        ...
    @DefaultThreadCurrentUICulture.setter
    def DefaultThreadCurrentUICulture(self, val: System.Globalization.CultureInfo):
        ...

    @property
    def InvariantCulture(self) -> System.Globalization.CultureInfo:
        ...

    @property
    def Parent(self) -> System.Globalization.CultureInfo:
        ...

    @property
    def LCID(self) -> int:
        ...

    @property
    def KeyboardLayoutId(self) -> int:
        ...

    @property
    def Name(self) -> str:
        ...

    @property
    def SortName(self) -> str:
        ...

    @property
    def IetfLanguageTag(self) -> str:
        ...

    @property
    def DisplayName(self) -> str:
        ...

    @property
    def NativeName(self) -> str:
        ...

    @property
    def EnglishName(self) -> str:
        ...

    @property
    def TwoLetterISOLanguageName(self) -> str:
        ...

    @property
    def ThreeLetterISOLanguageName(self) -> str:
        ...

    @property
    def ThreeLetterWindowsLanguageName(self) -> str:
        ...

    @property
    def CompareInfo(self) -> System.Globalization.CompareInfo:
        ...

    @property
    def TextInfo(self) -> System.Globalization.TextInfo:
        ...

    @property
    def IsNeutralCulture(self) -> bool:
        ...

    @property
    def CultureTypes(self) -> int:
        ...

    @property
    def NumberFormat(self) -> System.Globalization.NumberFormatInfo:
        ...
    @NumberFormat.setter
    def NumberFormat(self, val: System.Globalization.NumberFormatInfo):
        ...

    @property
    def DateTimeFormat(self) -> System.Globalization.DateTimeFormatInfo:
        ...
    @DateTimeFormat.setter
    def DateTimeFormat(self, val: System.Globalization.DateTimeFormatInfo):
        ...

    @property
    def Calendar(self) -> System.Globalization.Calendar:
        ...

    @property
    def OptionalCalendars(self) -> System.Array[System.Globalization.Calendar]:
        ...

    @property
    def UseUserOverride(self) -> bool:
        ...

    @property
    def IsReadOnly(self) -> bool:
        ...

    @property
    def HasInvariantCultureName(self) -> bool:
        ...

    @property
    def CachedCulturesByName(self) -> System.Collections.Generic.Dictionary[str, System.Globalization.CultureInfo]:
        ...

    @property
    def CachedCulturesByLcid(self) -> System.Collections.Generic.Dictionary[int, System.Globalization.CultureInfo]:
        ...

    # methods
    @typing.overload
    def __init__(self, name: str, ):
        ...

    @typing.overload
    def __init__(self, name: str, useUserOverride: bool, ):
        ...

    @typing.overload
    def __init__(self, cultureData: System.Globalization.CultureData, isReadOnly: bool = ..., ):
        ...

    @typing.overload
    def __init__(self, culture: int, ):
        ...

    @typing.overload
    def __init__(self, culture: int, useUserOverride: bool, ):
        ...

    @typing.overload
    def __init__(self, cultureName: str, textAndCompareCultureName: str, ):
        ...

    @staticmethod
    def AsyncLocalSetCurrentCulture(args: System.Threading.AsyncLocalValueChangedArgs[System.Globalization.CultureInfo], ) -> None:
        ...

    @staticmethod
    def AsyncLocalSetCurrentUICulture(args: System.Threading.AsyncLocalValueChangedArgs[System.Globalization.CultureInfo], ) -> None:
        ...

    @staticmethod
    def InitializeUserDefaultCulture() -> System.Globalization.CultureInfo:
        ...

    @staticmethod
    def InitializeUserDefaultUICulture() -> System.Globalization.CultureInfo:
        ...

    @staticmethod
    def GetCultureNotSupportedExceptionMessage() -> str:
        ...

    @staticmethod
    def CreateCultureInfoNoThrow(name: str, useUserOverride: bool, ) -> System.Globalization.CultureInfo:
        ...

    @staticmethod
    def GetCultureByName(name: str, ) -> System.Globalization.CultureInfo:
        ...

    @staticmethod
    def CreateSpecificCulture(name: str, ) -> System.Globalization.CultureInfo:
        ...

    @staticmethod
    @typing.overload
    def VerifyCultureName(cultureName: str, throwException: bool, ) -> bool:
        ...

    @staticmethod
    @typing.overload
    def VerifyCultureName(culture: System.Globalization.CultureInfo, throwException: bool, ) -> bool:
        ...

    @staticmethod
    def GetCultures(types: int, ) -> System.Array[System.Globalization.CultureInfo]:
        ...

    def Equals(self, value: System.Object, ) -> bool:
        ...

    def GetHashCode(self, ) -> int:
        ...

    def ToString(self, ) -> str:
        ...

    def GetFormat(self, formatType: System.Type, ) -> System.Object:
        ...

    def ClearCachedData(self, ) -> None:
        ...

    @staticmethod
    def GetCalendarInstance(calType: int, ) -> System.Globalization.Calendar:
        ...

    @staticmethod
    def GetCalendarInstanceRare(calType: int, ) -> System.Globalization.Calendar:
        ...

    def GetConsoleFallbackUICulture(self, ) -> System.Globalization.CultureInfo:
        ...

    def Clone(self, ) -> System.Object:
        ...

    @staticmethod
    def ReadOnly(ci: System.Globalization.CultureInfo, ) -> System.Globalization.CultureInfo:
        ...

    def VerifyWritable(self, ) -> None:
        ...

    @staticmethod
    @typing.overload
    def GetCultureInfo(culture: int, ) -> System.Globalization.CultureInfo:
        ...

    @staticmethod
    @typing.overload
    def GetCultureInfo(name: str, ) -> System.Globalization.CultureInfo:
        ...

    @staticmethod
    @typing.overload
    def GetCultureInfo(name: str, altName: str, ) -> System.Globalization.CultureInfo:
        ...

    @staticmethod
    @typing.overload
    def GetCultureInfo(name: str, predefinedOnly: bool, ) -> System.Globalization.CultureInfo:
        ...

    @staticmethod
    def GetCultureInfoByIetfLanguageTag(name: str, ) -> System.Globalization.CultureInfo:
        ...

    @staticmethod
    def GetUserDefaultCulture() -> System.Globalization.CultureInfo:
        ...

    @staticmethod
    def GetUserDefaultUICulture() -> System.Globalization.CultureInfo:
        ...

class CultureTypes(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    NeutralCultures: int = ...
    SpecificCultures: int = ...
    InstalledWin32Cultures: int = ...
    AllCultures: int = ...
    UserCustomCulture: int = ...
    ReplacementCultures: int = ...
    WindowsOnlyCultures: int = ...
    FrameworkCultures: int = ...

class SortKey(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def OriginalString(self) -> str:
        ...

    @property
    def KeyData(self) -> System.Array[int]:
        ...

    # methods
    def __init__(self, compareInfo: System.Globalization.CompareInfo, str: str, options: int, keyData: System.Array[int], ):
        ...

    @staticmethod
    def Compare(sortkey1: System.Globalization.SortKey, sortkey2: System.Globalization.SortKey, ) -> int:
        ...

    def Equals(self, value: System.Object, ) -> bool:
        ...

    def GetHashCode(self, ) -> int:
        ...

    def ToString(self, ) -> str:
        ...

class TextInfo(System.ICloneable, System.Runtime.Serialization.IDeserializationCallback, System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields
    Invariant: System.Globalization.TextInfo = ...

    # properties
    @property
    def ANSICodePage(self) -> int:
        ...

    @property
    def OEMCodePage(self) -> int:
        ...

    @property
    def MacCodePage(self) -> int:
        ...

    @property
    def EBCDICCodePage(self) -> int:
        ...

    @property
    def LCID(self) -> int:
        ...

    @property
    def CultureName(self) -> str:
        ...

    @property
    def IsReadOnly(self) -> bool:
        ...

    @property
    def ListSeparator(self) -> str:
        ...
    @ListSeparator.setter
    def ListSeparator(self, val: str):
        ...

    @property
    def IsAsciiCasingSameAsInvariant(self) -> bool:
        ...

    @property
    def IsRightToLeft(self) -> bool:
        ...

    @property
    def IsInvariant(self) -> bool:
        ...

    # methods
    @typing.overload
    def __init__(self, cultureData: System.Globalization.CultureData, ):
        ...

    @typing.overload
    def __init__(self, cultureData: System.Globalization.CultureData, readOnly: bool, ):
        ...

    def OnDeserialization(self, sender: System.Object, ) -> None:
        ...

    def Clone(self, ) -> System.Object:
        ...

    @staticmethod
    def ReadOnly(textInfo: System.Globalization.TextInfo, ) -> System.Globalization.TextInfo:
        ...

    def VerifyWritable(self, ) -> None:
        ...

    def SetReadOnlyState(self, readOnly: bool, ) -> None:
        ...

    @typing.overload
    def ToLower(self, c: str, ) -> str:
        ...

    @typing.overload
    def ToLower(self, str: str, ) -> str:
        ...

    @staticmethod
    def ToLowerInvariant(c: str, ) -> str:
        ...

    def ChangeCase(self, c: str, toUpper: bool, ) -> str:
        ...

    def ChangeCaseToLower(self, source: System.ReadOnlySpan[str], destination: System.Span[str], ) -> None:
        ...

    def ChangeCaseToUpper(self, source: System.ReadOnlySpan[str], destination: System.Span[str], ) -> None:
        ...

    @typing.overload
    def ChangeCaseCommon(self, source: System.ReadOnlySpan[str], destination: System.Span[str], ) -> None:
        ...

    @typing.overload
    def ChangeCaseCommon(self, source: ref[str], destination: ref[str], charCount: int, ) -> None:
        ...

    @typing.overload
    def ChangeCaseCommon(self, source: str, ) -> str:
        ...

    @staticmethod
    @typing.overload
    def ToLowerAsciiInvariant(s: str, ) -> str:
        ...

    @staticmethod
    @typing.overload
    def ToLowerAsciiInvariant(c: str, ) -> str:
        ...

    @typing.overload
    def ToUpper(self, c: str, ) -> str:
        ...

    @typing.overload
    def ToUpper(self, str: str, ) -> str:
        ...

    @staticmethod
    def ToUpperInvariant(c: str, ) -> str:
        ...

    @staticmethod
    def ToUpperAsciiInvariant(c: str, ) -> str:
        ...

    def PopulateIsAsciiCasingSameAsInvariant(self, ) -> None:
        ...

    def Equals(self, obj: System.Object, ) -> bool:
        ...

    def GetHashCode(self, ) -> int:
        ...

    def ToString(self, ) -> str:
        ...

    def ToTitleCase(self, str: str, ) -> str:
        ...

    @staticmethod
    def AddNonLetter(result: ref[System.Text.StringBuilder], input: ref[str], inputIndex: int, charLen: int, ) -> int:
        ...

    def AddTitlecaseLetter(self, result: ref[System.Text.StringBuilder], input: ref[str], inputIndex: int, charLen: int, ) -> int:
        ...

    def ChangeCaseCore(self, src: ptr[str], srcLen: int, dstBuffer: ptr[str], dstBufferCapacity: int, bToUpper: bool, ) -> None:
        ...

    @staticmethod
    def IsWordSeparator(category: int, ) -> bool:
        ...

    @staticmethod
    def IsLetterCategory(uc: int, ) -> bool:
        ...

    @staticmethod
    def NeedsTurkishCasing(localeName: str, ) -> bool:
        ...

    def IcuChangeCase(self, src: ptr[str], srcLen: int, dstBuffer: ptr[str], dstBufferCapacity: int, bToUpper: bool, ) -> None:
        ...

class UnicodeCategory(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    UppercaseLetter: int = ...
    LowercaseLetter: int = ...
    TitlecaseLetter: int = ...
    ModifierLetter: int = ...
    OtherLetter: int = ...
    NonSpacingMark: int = ...
    SpacingCombiningMark: int = ...
    EnclosingMark: int = ...
    DecimalDigitNumber: int = ...
    LetterNumber: int = ...
    OtherNumber: int = ...
    SpaceSeparator: int = ...
    LineSeparator: int = ...
    ParagraphSeparator: int = ...
    Control: int = ...
    Format: int = ...
    Surrogate: int = ...
    PrivateUse: int = ...
    ConnectorPunctuation: int = ...
    DashPunctuation: int = ...
    OpenPunctuation: int = ...
    ClosePunctuation: int = ...
    InitialQuotePunctuation: int = ...
    FinalQuotePunctuation: int = ...
    OtherPunctuation: int = ...
    MathSymbol: int = ...
    CurrencySymbol: int = ...
    ModifierSymbol: int = ...
    OtherSymbol: int = ...
    OtherNotAssigned: int = ...

class DateTimeFormatInfo(System.IFormatProvider, System.ICloneable, System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        self._isReadOnly: bool
        ...

    # static fields

    # properties
    @property
    def CultureName(self) -> str:
        ...

    @property
    def Culture(self) -> System.Globalization.CultureInfo:
        ...

    @property
    def LanguageName(self) -> str:
        ...

    @property
    def InvariantInfo(self) -> System.Globalization.DateTimeFormatInfo:
        ...

    @property
    def CurrentInfo(self) -> System.Globalization.DateTimeFormatInfo:
        ...

    @property
    def AMDesignator(self) -> str:
        ...
    @AMDesignator.setter
    def AMDesignator(self, val: str):
        ...

    @property
    def Calendar(self) -> System.Globalization.Calendar:
        ...
    @Calendar.setter
    def Calendar(self, val: System.Globalization.Calendar):
        ...

    @property
    def OptionalCalendars(self) -> System.Array[int]:
        ...

    @property
    def EraNames(self) -> System.Array[str]:
        ...

    @property
    def AbbreviatedEraNames(self) -> System.Array[str]:
        ...

    @property
    def AbbreviatedEnglishEraNames(self) -> System.Array[str]:
        ...

    @property
    def DateSeparator(self) -> str:
        ...
    @DateSeparator.setter
    def DateSeparator(self, val: str):
        ...

    @property
    def FirstDayOfWeek(self) -> int:
        ...
    @FirstDayOfWeek.setter
    def FirstDayOfWeek(self, val: int):
        ...

    @property
    def CalendarWeekRule(self) -> int:
        ...
    @CalendarWeekRule.setter
    def CalendarWeekRule(self, val: int):
        ...

    @property
    def FullDateTimePattern(self) -> str:
        ...
    @FullDateTimePattern.setter
    def FullDateTimePattern(self, val: str):
        ...

    @property
    def LongDatePattern(self) -> str:
        ...
    @LongDatePattern.setter
    def LongDatePattern(self, val: str):
        ...

    @property
    def LongTimePattern(self) -> str:
        ...
    @LongTimePattern.setter
    def LongTimePattern(self, val: str):
        ...

    @property
    def MonthDayPattern(self) -> str:
        ...
    @MonthDayPattern.setter
    def MonthDayPattern(self, val: str):
        ...

    @property
    def PMDesignator(self) -> str:
        ...
    @PMDesignator.setter
    def PMDesignator(self, val: str):
        ...

    @property
    def RFC1123Pattern(self) -> str:
        ...

    @property
    def ShortDatePattern(self) -> str:
        ...
    @ShortDatePattern.setter
    def ShortDatePattern(self, val: str):
        ...

    @property
    def ShortTimePattern(self) -> str:
        ...
    @ShortTimePattern.setter
    def ShortTimePattern(self, val: str):
        ...

    @property
    def SortableDateTimePattern(self) -> str:
        ...

    @property
    def GeneralShortTimePattern(self) -> str:
        ...

    @property
    def GeneralLongTimePattern(self) -> str:
        ...

    @property
    def DateTimeOffsetPattern(self) -> str:
        ...

    @property
    def TimeSeparator(self) -> str:
        ...
    @TimeSeparator.setter
    def TimeSeparator(self, val: str):
        ...

    @property
    def UniversalSortableDateTimePattern(self) -> str:
        ...

    @property
    def YearMonthPattern(self) -> str:
        ...
    @YearMonthPattern.setter
    def YearMonthPattern(self, val: str):
        ...

    @property
    def AbbreviatedDayNames(self) -> System.Array[str]:
        ...
    @AbbreviatedDayNames.setter
    def AbbreviatedDayNames(self, val: System.Array[str]):
        ...

    @property
    def ShortestDayNames(self) -> System.Array[str]:
        ...
    @ShortestDayNames.setter
    def ShortestDayNames(self, val: System.Array[str]):
        ...

    @property
    def DayNames(self) -> System.Array[str]:
        ...
    @DayNames.setter
    def DayNames(self, val: System.Array[str]):
        ...

    @property
    def AbbreviatedMonthNames(self) -> System.Array[str]:
        ...
    @AbbreviatedMonthNames.setter
    def AbbreviatedMonthNames(self, val: System.Array[str]):
        ...

    @property
    def MonthNames(self) -> System.Array[str]:
        ...
    @MonthNames.setter
    def MonthNames(self, val: System.Array[str]):
        ...

    @property
    def HasSpacesInMonthNames(self) -> bool:
        ...

    @property
    def HasSpacesInDayNames(self) -> bool:
        ...

    @property
    def AllYearMonthPatterns(self) -> System.Array[str]:
        ...

    @property
    def AllShortDatePatterns(self) -> System.Array[str]:
        ...

    @property
    def AllShortTimePatterns(self) -> System.Array[str]:
        ...

    @property
    def AllLongDatePatterns(self) -> System.Array[str]:
        ...

    @property
    def AllLongTimePatterns(self) -> System.Array[str]:
        ...

    @property
    def UnclonedYearMonthPatterns(self) -> System.Array[str]:
        ...

    @property
    def UnclonedShortDatePatterns(self) -> System.Array[str]:
        ...

    @property
    def UnclonedLongDatePatterns(self) -> System.Array[str]:
        ...

    @property
    def UnclonedShortTimePatterns(self) -> System.Array[str]:
        ...

    @property
    def UnclonedLongTimePatterns(self) -> System.Array[str]:
        ...

    @property
    def IsReadOnly(self) -> bool:
        ...

    @property
    def NativeCalendarName(self) -> str:
        ...

    @property
    def AbbreviatedMonthGenitiveNames(self) -> System.Array[str]:
        ...
    @AbbreviatedMonthGenitiveNames.setter
    def AbbreviatedMonthGenitiveNames(self, val: System.Array[str]):
        ...

    @property
    def MonthGenitiveNames(self) -> System.Array[str]:
        ...
    @MonthGenitiveNames.setter
    def MonthGenitiveNames(self, val: System.Array[str]):
        ...

    @property
    def DecimalSeparator(self) -> str:
        ...

    @property
    def FullTimeSpanPositivePattern(self) -> str:
        ...

    @property
    def FullTimeSpanNegativePattern(self) -> str:
        ...

    @property
    def CompareInfo(self) -> System.Globalization.CompareInfo:
        ...

    @property
    def FormatFlags(self) -> int:
        ...

    @property
    def HasForceTwoDigitYears(self) -> bool:
        ...

    @property
    def HasYearMonthAdjustment(self) -> bool:
        ...

    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def __init__(self, cultureData: System.Globalization.CultureData, cal: System.Globalization.Calendar, ):
        ...

    @typing.overload
    def GetAllDateTimePatterns(self, ) -> System.Array[str]:
        ...

    @typing.overload
    def GetAllDateTimePatterns(self, format: str, ) -> System.Array[str]:
        ...

    def GetDayName(self, dayofweek: int, ) -> str:
        ...

    def GetAbbreviatedMonthName(self, month: int, ) -> str:
        ...

    def GetMonthName(self, month: int, ) -> str:
        ...

    @staticmethod
    def GetMergedPatterns(patterns: System.Array[str], defaultPattern: str, ) -> System.Array[str]:
        ...

    @staticmethod
    def ReadOnly(dtfi: System.Globalization.DateTimeFormatInfo, ) -> System.Globalization.DateTimeFormatInfo:
        ...

    def SetAllDateTimePatterns(self, patterns: System.Array[str], format: str, ) -> None:
        ...

    @staticmethod
    def ValidateStyles(style: int, styles: bool = ..., ) -> None:
        ...

    def InitializeFormatFlags(self, ) -> int:
        ...

    def YearMonthAdjustment(self, year: ref[int], month: ref[int], parsedMonthName: bool, ) -> bool:
        ...

    @staticmethod
    def GetJapaneseCalendarDTFI() -> System.Globalization.DateTimeFormatInfo:
        ...

    @staticmethod
    def GetTaiwanCalendarDTFI() -> System.Globalization.DateTimeFormatInfo:
        ...

    def ClearTokenHashTable(self, ) -> None:
        ...

    def CreateTokenHashTable(self, ) -> System.Array[System.Globalization.DateTimeFormatInfo.TokenHashValue]:
        ...

    def AddMonthNames(self, temp: System.Array[System.Globalization.DateTimeFormatInfo.TokenHashValue], monthPostfix: System.ReadOnlySpan[str] = ..., ) -> None:
        ...

    @staticmethod
    def TryParseHebrewNumber(str: ref[System.__DTString], badFormat: ref[bool], number: ref[int], ) -> bool:
        ...

    @staticmethod
    def IsHebrewChar(ch: str, ) -> bool:
        ...

    def IsAllowedJapaneseTokenFollowedByNonSpaceLetter(self, tokenString: str, nextCh: str, ) -> bool:
        ...

    def Tokenize(self, TokenMask: int, tokenType: ref[int], tokenValue: ref[int], str: ref[System.__DTString], ) -> bool:
        ...

    def InsertAtCurrentHashNode(self, hashTable: System.Array[System.Globalization.DateTimeFormatInfo.TokenHashValue], str: str, ch: str, tokenType: int, tokenValue: int, pos: int, hashcode: int, hashProbe: int, ) -> None:
        ...

    def InsertHash(self, hashTable: System.Array[System.Globalization.DateTimeFormatInfo.TokenHashValue], str: str, tokenType: int, tokenValue: int, ) -> None:
        ...

    def CompareStringIgnoreCaseOptimized(self, string1: str, offset1: int, length1: int, string2: str, offset2: int, length2: int, ) -> bool:
        ...

    def InternalGetAbbreviatedDayOfWeekNames(self, ) -> System.Array[str]:
        ...

    def InternalGetAbbreviatedDayOfWeekNamesCore(self, ) -> System.Array[str]:
        ...

    def InternalGetSuperShortDayNames(self, ) -> System.Array[str]:
        ...

    def InternalGetSuperShortDayNamesCore(self, ) -> System.Array[str]:
        ...

    def InternalGetDayOfWeekNames(self, ) -> System.Array[str]:
        ...

    def InternalGetDayOfWeekNamesCore(self, ) -> System.Array[str]:
        ...

    def InternalGetAbbreviatedMonthNames(self, ) -> System.Array[str]:
        ...

    def InternalGetAbbreviatedMonthNamesCore(self, ) -> System.Array[str]:
        ...

    def InternalGetMonthNames(self, ) -> System.Array[str]:
        ...

    def internalGetMonthNamesCore(self, ) -> System.Array[str]:
        ...

    def InitializeOverridableProperties(self, cultureData: System.Globalization.CultureData, calendarId: int, ) -> None:
        ...

    @staticmethod
    def GetInstance(provider: System.IFormatProvider, ) -> System.Globalization.DateTimeFormatInfo:
        ...

    def GetFormat(self, formatType: System.Type, ) -> System.Object:
        ...

    def Clone(self, ) -> System.Object:
        ...

    def GetEra(self, eraName: str, ) -> int:
        ...

    def GetEraName(self, era: int, ) -> str:
        ...

    def GetAbbreviatedEraName(self, era: int, ) -> str:
        ...

    def OnLongDatePatternChanged(self, ) -> None:
        ...

    def OnLongTimePatternChanged(self, ) -> None:
        ...

    def OnShortDatePatternChanged(self, ) -> None:
        ...

    def OnShortTimePatternChanged(self, ) -> None:
        ...

    def OnYearMonthPatternChanged(self, ) -> None:
        ...

    @staticmethod
    def CheckNullValue(values: System.Array[str], length: int, ) -> None:
        ...

    def InternalGetMonthName(self, month: int, style: int, abbreviated: bool, ) -> str:
        ...

    def InternalGetGenitiveMonthNames(self, abbreviated: bool, ) -> System.Array[str]:
        ...

    def InternalGetLeapYearMonthNames(self, ) -> System.Array[str]:
        ...

    def GetAbbreviatedDayName(self, dayofweek: int, ) -> str:
        ...

    def GetShortestDayName(self, dayOfWeek: int, ) -> str:
        ...

    @staticmethod
    def GetCombinedPatterns(patterns1: System.Array[str], patterns2: System.Array[str], connectString: str, ) -> System.Array[str]:
        ...

class CalendarWeekRule(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    FirstDay: int = ...
    FirstFullWeek: int = ...
    FirstFourDayWeek: int = ...

class CalendarAlgorithmType(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    Unknown: int = ...
    SolarCalendar: int = ...
    LunarCalendar: int = ...
    LunisolarCalendar: int = ...

class NumberFormatInfo(System.IFormatProvider, System.ICloneable, System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        self._numberGroupSizes: System.Array[int]
        self._currencyGroupSizes: System.Array[int]
        self._percentGroupSizes: System.Array[int]
        self._positiveSign: str
        self._negativeSign: str
        self._numberDecimalSeparator: str
        self._numberGroupSeparator: str
        self._currencyGroupSeparator: str
        self._currencyDecimalSeparator: str
        self._currencySymbol: str
        self._nanSymbol: str
        self._positiveInfinitySymbol: str
        self._negativeInfinitySymbol: str
        self._percentDecimalSeparator: str
        self._percentGroupSeparator: str
        self._percentSymbol: str
        self._perMilleSymbol: str
        self._nativeDigits: System.Array[str]
        self._numberDecimalDigits: int
        self._currencyDecimalDigits: int
        self._currencyPositivePattern: int
        self._currencyNegativePattern: int
        self._numberNegativePattern: int
        self._percentPositivePattern: int
        self._percentNegativePattern: int
        self._percentDecimalDigits: int
        self._digitSubstitution: int
        self._isReadOnly: bool
        ...

    # static fields

    # properties
    @property
    def HasInvariantNumberSigns(self) -> bool:
        ...

    @property
    def AllowHyphenDuringParsing(self) -> bool:
        ...

    @property
    def InvariantInfo(self) -> System.Globalization.NumberFormatInfo:
        ...

    @property
    def CurrencyDecimalDigits(self) -> int:
        ...
    @CurrencyDecimalDigits.setter
    def CurrencyDecimalDigits(self, val: int):
        ...

    @property
    def CurrencyDecimalSeparator(self) -> str:
        ...
    @CurrencyDecimalSeparator.setter
    def CurrencyDecimalSeparator(self, val: str):
        ...

    @property
    def IsReadOnly(self) -> bool:
        ...

    @property
    def CurrencyGroupSizes(self) -> System.Array[int]:
        ...
    @CurrencyGroupSizes.setter
    def CurrencyGroupSizes(self, val: System.Array[int]):
        ...

    @property
    def NumberGroupSizes(self) -> System.Array[int]:
        ...
    @NumberGroupSizes.setter
    def NumberGroupSizes(self, val: System.Array[int]):
        ...

    @property
    def PercentGroupSizes(self) -> System.Array[int]:
        ...
    @PercentGroupSizes.setter
    def PercentGroupSizes(self, val: System.Array[int]):
        ...

    @property
    def CurrencyGroupSeparator(self) -> str:
        ...
    @CurrencyGroupSeparator.setter
    def CurrencyGroupSeparator(self, val: str):
        ...

    @property
    def CurrencySymbol(self) -> str:
        ...
    @CurrencySymbol.setter
    def CurrencySymbol(self, val: str):
        ...

    @property
    def CurrentInfo(self) -> System.Globalization.NumberFormatInfo:
        ...

    @property
    def NaNSymbol(self) -> str:
        ...
    @NaNSymbol.setter
    def NaNSymbol(self, val: str):
        ...

    @property
    def CurrencyNegativePattern(self) -> int:
        ...
    @CurrencyNegativePattern.setter
    def CurrencyNegativePattern(self, val: int):
        ...

    @property
    def NumberNegativePattern(self) -> int:
        ...
    @NumberNegativePattern.setter
    def NumberNegativePattern(self, val: int):
        ...

    @property
    def PercentPositivePattern(self) -> int:
        ...
    @PercentPositivePattern.setter
    def PercentPositivePattern(self, val: int):
        ...

    @property
    def PercentNegativePattern(self) -> int:
        ...
    @PercentNegativePattern.setter
    def PercentNegativePattern(self, val: int):
        ...

    @property
    def NegativeInfinitySymbol(self) -> str:
        ...
    @NegativeInfinitySymbol.setter
    def NegativeInfinitySymbol(self, val: str):
        ...

    @property
    def NegativeSign(self) -> str:
        ...
    @NegativeSign.setter
    def NegativeSign(self, val: str):
        ...

    @property
    def NumberDecimalDigits(self) -> int:
        ...
    @NumberDecimalDigits.setter
    def NumberDecimalDigits(self, val: int):
        ...

    @property
    def NumberDecimalSeparator(self) -> str:
        ...
    @NumberDecimalSeparator.setter
    def NumberDecimalSeparator(self, val: str):
        ...

    @property
    def NumberGroupSeparator(self) -> str:
        ...
    @NumberGroupSeparator.setter
    def NumberGroupSeparator(self, val: str):
        ...

    @property
    def CurrencyPositivePattern(self) -> int:
        ...
    @CurrencyPositivePattern.setter
    def CurrencyPositivePattern(self, val: int):
        ...

    @property
    def PositiveInfinitySymbol(self) -> str:
        ...
    @PositiveInfinitySymbol.setter
    def PositiveInfinitySymbol(self, val: str):
        ...

    @property
    def PositiveSign(self) -> str:
        ...
    @PositiveSign.setter
    def PositiveSign(self, val: str):
        ...

    @property
    def PercentDecimalDigits(self) -> int:
        ...
    @PercentDecimalDigits.setter
    def PercentDecimalDigits(self, val: int):
        ...

    @property
    def PercentDecimalSeparator(self) -> str:
        ...
    @PercentDecimalSeparator.setter
    def PercentDecimalSeparator(self, val: str):
        ...

    @property
    def PercentGroupSeparator(self) -> str:
        ...
    @PercentGroupSeparator.setter
    def PercentGroupSeparator(self, val: str):
        ...

    @property
    def PercentSymbol(self) -> str:
        ...
    @PercentSymbol.setter
    def PercentSymbol(self, val: str):
        ...

    @property
    def PerMilleSymbol(self) -> str:
        ...
    @PerMilleSymbol.setter
    def PerMilleSymbol(self, val: str):
        ...

    @property
    def NativeDigits(self) -> System.Array[str]:
        ...
    @NativeDigits.setter
    def NativeDigits(self, val: System.Array[str]):
        ...

    @property
    def DigitSubstitution(self) -> int:
        ...
    @DigitSubstitution.setter
    def DigitSubstitution(self, val: int):
        ...

    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def __init__(self, cultureData: System.Globalization.CultureData, ):
        ...

    @staticmethod
    def VerifyDecimalSeparator(decSep: str, propertyName: str, ) -> None:
        ...

    @staticmethod
    def VerifyGroupSeparator(groupSep: str, propertyName: str, ) -> None:
        ...

    @staticmethod
    def VerifyNativeDigits(nativeDig: System.Array[str], propertyName: str, ) -> None:
        ...

    @staticmethod
    def VerifyDigitSubstitution(digitSub: int, propertyName: str, ) -> None:
        ...

    def InitializeInvariantAndNegativeSignFlags(self, ) -> None:
        ...

    def VerifyWritable(self, ) -> None:
        ...

    @staticmethod
    def GetInstance(formatProvider: System.IFormatProvider, ) -> System.Globalization.NumberFormatInfo:
        ...

    def Clone(self, ) -> System.Object:
        ...

    @staticmethod
    def CheckGroupSize(propName: str, groupSize: System.Array[int], ) -> None:
        ...

    def GetFormat(self, formatType: System.Type, ) -> System.Object:
        ...

    @staticmethod
    def ReadOnly(nfi: System.Globalization.NumberFormatInfo, ) -> System.Globalization.NumberFormatInfo:
        ...

    @staticmethod
    def ValidateParseStyleInteger(style: int, ) -> None:
        ...

    @staticmethod
    def ValidateParseStyleFloatingPoint(style: int, ) -> None:
        ...

class DigitShapes(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    Context: int = ...
    None_: int = ...
    NativeNational: int = ...

class DateTimeStyles(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    None_: int = ...
    AllowLeadingWhite: int = ...
    AllowTrailingWhite: int = ...
    AllowInnerWhite: int = ...
    AllowWhiteSpaces: int = ...
    NoCurrentDateDefault: int = ...
    AdjustToUniversal: int = ...
    AssumeLocal: int = ...
    AssumeUniversal: int = ...
    RoundtripKind: int = ...

class CompareOptions(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    None_: int = ...
    IgnoreCase: int = ...
    IgnoreNonSpace: int = ...
    IgnoreSymbols: int = ...
    IgnoreKanaType: int = ...
    IgnoreWidth: int = ...
    OrdinalIgnoreCase: int = ...
    StringSort: int = ...
    Ordinal: int = ...

class CompareInfo(System.Runtime.Serialization.IDeserializationCallback, System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields
    Invariant: System.Globalization.CompareInfo = ...

    # properties
    @property
    def Name(self) -> str:
        ...

    @property
    def Version(self) -> System.Globalization.SortVersion:
        ...

    @property
    def LCID(self) -> int:
        ...

    @property
    def HighCharTable(self) -> System.ReadOnlySpan[bool]:
        ...

    # methods
    def __init__(self, culture: System.Globalization.CultureInfo, ):
        ...

    def IcuIndexOfCore(self, source: System.ReadOnlySpan[str], target: System.ReadOnlySpan[str], options: int, matchLengthPtr: ptr[int], fromBeginning: bool, ) -> int:
        ...

    def IndexOfOrdinalIgnoreCaseHelper(self, source: System.ReadOnlySpan[str], target: System.ReadOnlySpan[str], options: int, matchLengthPtr: ptr[int], fromBeginning: bool, ) -> int:
        ...

    def IndexOfOrdinalHelper(self, source: System.ReadOnlySpan[str], target: System.ReadOnlySpan[str], options: int, matchLengthPtr: ptr[int], fromBeginning: bool, ) -> int:
        ...

    def IcuStartsWith(self, source: System.ReadOnlySpan[str], prefix: System.ReadOnlySpan[str], options: int, matchLengthPtr: ptr[int], ) -> bool:
        ...

    def StartsWithOrdinalIgnoreCaseHelper(self, source: System.ReadOnlySpan[str], prefix: System.ReadOnlySpan[str], options: int, matchLengthPtr: ptr[int], ) -> bool:
        ...

    def StartsWithOrdinalHelper(self, source: System.ReadOnlySpan[str], prefix: System.ReadOnlySpan[str], options: int, matchLengthPtr: ptr[int], ) -> bool:
        ...

    def IcuEndsWith(self, source: System.ReadOnlySpan[str], suffix: System.ReadOnlySpan[str], options: int, matchLengthPtr: ptr[int], ) -> bool:
        ...

    def EndsWithOrdinalIgnoreCaseHelper(self, source: System.ReadOnlySpan[str], suffix: System.ReadOnlySpan[str], options: int, matchLengthPtr: ptr[int], ) -> bool:
        ...

    def EndsWithOrdinalHelper(self, source: System.ReadOnlySpan[str], suffix: System.ReadOnlySpan[str], options: int, matchLengthPtr: ptr[int], ) -> bool:
        ...

    def IcuCreateSortKey(self, source: str, options: int, ) -> System.Globalization.SortKey:
        ...

    def IcuGetSortKey(self, source: System.ReadOnlySpan[str], destination: System.Span[int], options: int, ) -> int:
        ...

    def IcuGetSortKeyLength(self, source: System.ReadOnlySpan[str], options: int, ) -> int:
        ...

    @staticmethod
    def IcuIsSortable(text: System.ReadOnlySpan[str], ) -> bool:
        ...

    def IcuGetHashCodeOfString(self, source: System.ReadOnlySpan[str], options: int, ) -> int:
        ...

    @staticmethod
    def CanUseAsciiOrdinalForOptions(options: int, ) -> bool:
        ...

    def IcuGetSortVersion(self, ) -> System.Globalization.SortVersion:
        ...

    def InvariantCreateSortKey(self, source: str, options: int, ) -> System.Globalization.SortKey:
        ...

    @staticmethod
    def InvariantCreateSortKeyOrdinal(source: System.ReadOnlySpan[str], sortKey: System.Span[int], ) -> None:
        ...

    @staticmethod
    def InvariantCreateSortKeyOrdinalIgnoreCase(source: System.ReadOnlySpan[str], sortKey: System.Span[int], ) -> None:
        ...

    @staticmethod
    def InvariantGetSortKey(source: System.ReadOnlySpan[str], destination: System.Span[int], options: int, ) -> int:
        ...

    @staticmethod
    def InvariantGetSortKeyLength(source: System.ReadOnlySpan[str], options: int, ) -> int:
        ...

    @staticmethod
    @typing.overload
    def GetCompareInfo(culture: int, assembly: System.Reflection.Assembly, ) -> System.Globalization.CompareInfo:
        ...

    @staticmethod
    @typing.overload
    def GetCompareInfo(name: str, assembly: System.Reflection.Assembly, ) -> System.Globalization.CompareInfo:
        ...

    @staticmethod
    @typing.overload
    def GetCompareInfo(culture: int, ) -> System.Globalization.CompareInfo:
        ...

    @staticmethod
    @typing.overload
    def GetCompareInfo(name: str, ) -> System.Globalization.CompareInfo:
        ...

    @staticmethod
    @typing.overload
    def IsSortable(ch: str, ) -> bool:
        ...

    @staticmethod
    @typing.overload
    def IsSortable(text: str, ) -> bool:
        ...

    @staticmethod
    @typing.overload
    def IsSortable(text: System.ReadOnlySpan[str], ) -> bool:
        ...

    @staticmethod
    @typing.overload
    def IsSortable(value: System.Text.Rune, ) -> bool:
        ...

    def InitSort(self, culture: System.Globalization.CultureInfo, ) -> None:
        ...

    def OnDeserializing(self, ctx: System.Runtime.Serialization.StreamingContext, ) -> None:
        ...

    def OnDeserialization(self, sender: System.Object, ) -> None:
        ...

    @typing.overload
    def OnDeserialized(self, ctx: System.Runtime.Serialization.StreamingContext, ) -> None:
        ...

    @typing.overload
    def OnDeserialized(self, ) -> None:
        ...

    def OnSerializing(self, ctx: System.Runtime.Serialization.StreamingContext, ) -> None:
        ...

    @typing.overload
    def Compare(self, string1: str, string2: str, ) -> int:
        ...

    @typing.overload
    def Compare(self, string1: str, string2: str, options: int, ) -> int:
        ...

    @typing.overload
    def Compare(self, string1: str, offset1: int, length1: int, string2: str, offset2: int, length2: int, ) -> int:
        ...

    @typing.overload
    def Compare(self, string1: str, offset1: int, string2: str, offset2: int, options: int, ) -> int:
        ...

    @typing.overload
    def Compare(self, string1: str, offset1: int, string2: str, offset2: int, ) -> int:
        ...

    @typing.overload
    def Compare(self, string1: str, offset1: int, length1: int, string2: str, offset2: int, length2: int, options: int, ) -> int:
        ...

    @typing.overload
    def Compare(self, string1: System.ReadOnlySpan[str], string2: System.ReadOnlySpan[str], options: int = ..., ) -> int:
        ...

    def CompareOptionIgnoreCase(self, string1: System.ReadOnlySpan[str], string2: System.ReadOnlySpan[str], ) -> int:
        ...

    @staticmethod
    def CheckCompareOptionsForCompare(options: int, ) -> None:
        ...

    @staticmethod
    def ThrowCompareOptionsCheckFailed(options: int, ) -> None:
        ...

    def CompareStringCore(self, string1: System.ReadOnlySpan[str], string2: System.ReadOnlySpan[str], options: int, ) -> int:
        ...

    @typing.overload
    def IsPrefix(self, source: str, prefix: str, options: int, ) -> bool:
        ...

    @typing.overload
    def IsPrefix(self, source: System.ReadOnlySpan[str], prefix: System.ReadOnlySpan[str], options: int = ..., ) -> bool:
        ...

    @typing.overload
    def IsPrefix(self, source: System.ReadOnlySpan[str], prefix: System.ReadOnlySpan[str], options: int, matchLength: ref[int], ) -> bool:
        ...

    @typing.overload
    def IsPrefix(self, source: str, prefix: str, ) -> bool:
        ...

    def StartsWithCore(self, source: System.ReadOnlySpan[str], prefix: System.ReadOnlySpan[str], options: int, matchLengthPtr: ptr[int], ) -> bool:
        ...

    @typing.overload
    def IsSuffix(self, source: str, suffix: str, options: int, ) -> bool:
        ...

    @typing.overload
    def IsSuffix(self, source: System.ReadOnlySpan[str], suffix: System.ReadOnlySpan[str], options: int = ..., ) -> bool:
        ...

    @typing.overload
    def IsSuffix(self, source: System.ReadOnlySpan[str], suffix: System.ReadOnlySpan[str], options: int, matchLength: ref[int], ) -> bool:
        ...

    @typing.overload
    def IsSuffix(self, source: str, suffix: str, ) -> bool:
        ...

    def EndsWithCore(self, source: System.ReadOnlySpan[str], suffix: System.ReadOnlySpan[str], options: int, matchLengthPtr: ptr[int], ) -> bool:
        ...

    @typing.overload
    def IndexOf(self, source: str, value: str, ) -> int:
        ...

    @typing.overload
    def IndexOf(self, source: str, value: str, ) -> int:
        ...

    @typing.overload
    def IndexOf(self, source: str, value: str, options: int, ) -> int:
        ...

    @typing.overload
    def IndexOf(self, source: str, value: str, options: int, ) -> int:
        ...

    @typing.overload
    def IndexOf(self, source: str, value: str, startIndex: int, ) -> int:
        ...

    @typing.overload
    def IndexOf(self, source: str, value: str, startIndex: int, ) -> int:
        ...

    @typing.overload
    def IndexOf(self, source: str, value: str, startIndex: int, options: int, ) -> int:
        ...

    @typing.overload
    def IndexOf(self, source: str, value: str, startIndex: int, options: int, ) -> int:
        ...

    @typing.overload
    def IndexOf(self, source: str, value: str, startIndex: int, count: int, ) -> int:
        ...

    @typing.overload
    def IndexOf(self, source: str, value: str, startIndex: int, count: int, ) -> int:
        ...

    @typing.overload
    def IndexOf(self, source: str, value: str, startIndex: int, count: int, options: int, ) -> int:
        ...

    @typing.overload
    def IndexOf(self, source: str, value: str, startIndex: int, count: int, options: int, ) -> int:
        ...

    @typing.overload
    def IndexOf(self, source: System.ReadOnlySpan[str], value: System.ReadOnlySpan[str], options: int = ..., ) -> int:
        ...

    @typing.overload
    def IndexOf(self, source: System.ReadOnlySpan[str], value: System.ReadOnlySpan[str], options: int, matchLength: ref[int], ) -> int:
        ...

    @typing.overload
    def IndexOf(self, source: System.ReadOnlySpan[str], value: System.Text.Rune, options: int = ..., ) -> int:
        ...

    @typing.overload
    def IndexOf(self, source: System.ReadOnlySpan[str], value: System.ReadOnlySpan[str], matchLengthPtr: ptr[int], options: int, fromBeginning: bool, ) -> int:
        ...

    def IndexOfCore(self, source: System.ReadOnlySpan[str], target: System.ReadOnlySpan[str], options: int, matchLengthPtr: ptr[int], fromBeginning: bool, ) -> int:
        ...

    @typing.overload
    def LastIndexOf(self, source: str, value: str, ) -> int:
        ...

    @typing.overload
    def LastIndexOf(self, source: str, value: str, ) -> int:
        ...

    @typing.overload
    def LastIndexOf(self, source: str, value: str, options: int, ) -> int:
        ...

    @typing.overload
    def LastIndexOf(self, source: str, value: str, options: int, ) -> int:
        ...

    @typing.overload
    def LastIndexOf(self, source: str, value: str, startIndex: int, ) -> int:
        ...

    @typing.overload
    def LastIndexOf(self, source: str, value: str, startIndex: int, ) -> int:
        ...

    @typing.overload
    def LastIndexOf(self, source: str, value: str, startIndex: int, options: int, ) -> int:
        ...

    @typing.overload
    def LastIndexOf(self, source: str, value: str, startIndex: int, options: int, ) -> int:
        ...

    @typing.overload
    def LastIndexOf(self, source: str, value: str, startIndex: int, count: int, ) -> int:
        ...

    @typing.overload
    def LastIndexOf(self, source: str, value: str, startIndex: int, count: int, ) -> int:
        ...

    @typing.overload
    def LastIndexOf(self, source: str, value: str, startIndex: int, count: int, options: int, ) -> int:
        ...

    @typing.overload
    def LastIndexOf(self, source: str, value: str, startIndex: int, count: int, options: int, ) -> int:
        ...

    @typing.overload
    def LastIndexOf(self, source: System.ReadOnlySpan[str], value: System.ReadOnlySpan[str], options: int = ..., ) -> int:
        ...

    @typing.overload
    def LastIndexOf(self, source: System.ReadOnlySpan[str], value: System.ReadOnlySpan[str], options: int, matchLength: ref[int], ) -> int:
        ...

    @typing.overload
    def LastIndexOf(self, source: System.ReadOnlySpan[str], value: System.Text.Rune, options: int = ..., ) -> int:
        ...

    @typing.overload
    def GetSortKey(self, source: str, options: int, ) -> System.Globalization.SortKey:
        ...

    @typing.overload
    def GetSortKey(self, source: str, ) -> System.Globalization.SortKey:
        ...

    @typing.overload
    def GetSortKey(self, source: System.ReadOnlySpan[str], destination: System.Span[int], options: int = ..., ) -> int:
        ...

    def CreateSortKeyCore(self, source: str, options: int, ) -> System.Globalization.SortKey:
        ...

    def GetSortKeyCore(self, source: System.ReadOnlySpan[str], destination: System.Span[int], options: int, ) -> int:
        ...

    def GetSortKeyLength(self, source: System.ReadOnlySpan[str], options: int = ..., ) -> int:
        ...

    def GetSortKeyLengthCore(self, source: System.ReadOnlySpan[str], options: int, ) -> int:
        ...

    def Equals(self, value: System.Object, ) -> bool:
        ...

    @typing.overload
    def GetHashCode(self, ) -> int:
        ...

    @typing.overload
    def GetHashCode(self, source: str, options: int, ) -> int:
        ...

    @typing.overload
    def GetHashCode(self, source: System.ReadOnlySpan[str], options: int, ) -> int:
        ...

    def GetHashCodeOfStringCore(self, source: System.ReadOnlySpan[str], options: int, ) -> int:
        ...

    def ToString(self, ) -> str:
        ...

    def IcuInitSortHandle(self, ) -> None:
        ...

    def IcuCompareString(self, string1: System.ReadOnlySpan[str], string2: System.ReadOnlySpan[str], options: int, ) -> int:
        ...

class SortVersion(System.IEquatable[System.Globalization.SortVersion], System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def FullVersion(self) -> int:
        ...

    @property
    def SortId(self) -> System.Guid:
        ...

    # methods
    @typing.overload
    def __init__(self, fullVersion: int, sortId: System.Guid, ):
        ...

    @typing.overload
    def __init__(self, nlsVersion: int, effectiveId: int, customVersion: System.Guid, ):
        ...

    @typing.overload
    def Equals(self, obj: System.Object, ) -> bool:
        ...

    @typing.overload
    def Equals(self, other: System.Globalization.SortVersion, ) -> bool:
        ...

    def GetHashCode(self, ) -> int:
        ...

