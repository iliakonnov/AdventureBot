from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import System
import System.Globalization
import System.Runtime.Serialization
import System.Reflection
import System.Text


class NumberStyles(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    None_: System.Int32 = None
    AllowLeadingWhite: System.Int32 = AllowLeadingWhite
    AllowTrailingWhite: System.Int32 = AllowTrailingWhite
    AllowLeadingSign: System.Int32 = AllowLeadingSign
    Integer: System.Int32 = Integer
    AllowTrailingSign: System.Int32 = AllowTrailingSign
    AllowParentheses: System.Int32 = AllowParentheses
    AllowDecimalPoint: System.Int32 = AllowDecimalPoint
    AllowThousands: System.Int32 = AllowThousands
    Number: System.Int32 = Number
    AllowExponent: System.Int32 = AllowExponent
    Float: System.Int32 = Float
    AllowCurrencySymbol: System.Int32 = AllowCurrencySymbol
    Currency: System.Int32 = Currency
    Any: System.Int32 = Any
    AllowHexSpecifier: System.Int32 = AllowHexSpecifier
    HexNumber: System.Int32 = HexNumber

class CultureInfo(System.IFormatProvider, System.ICloneable, System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

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
    def LCID(self) -> System.Int32:
        ...

    @property
    def KeyboardLayoutId(self) -> System.Int32:
        ...

    @property
    def Name(self) -> System.String:
        ...

    @property
    def IetfLanguageTag(self) -> System.String:
        ...

    @property
    def DisplayName(self) -> System.String:
        ...

    @property
    def NativeName(self) -> System.String:
        ...

    @property
    def EnglishName(self) -> System.String:
        ...

    @property
    def TwoLetterISOLanguageName(self) -> System.String:
        ...

    @property
    def ThreeLetterISOLanguageName(self) -> System.String:
        ...

    @property
    def ThreeLetterWindowsLanguageName(self) -> System.String:
        ...

    @property
    def CompareInfo(self) -> System.Globalization.CompareInfo:
        ...

    @property
    def TextInfo(self) -> System.Globalization.TextInfo:
        ...

    @property
    def IsNeutralCulture(self) -> System.Boolean:
        ...

    @property
    def CultureTypes(self) -> System.Globalization.CultureTypes:
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
    def OptionalCalendars(self) -> list[System.Globalization.Calendar]:
        ...

    @property
    def UseUserOverride(self) -> System.Boolean:
        ...

    @property
    def IsReadOnly(self) -> System.Boolean:
        ...

    # methods
    @typing.overload
    def __init__(self, name: System.String, ):
        ...

    @typing.overload
    def __init__(self, name: System.String, useUserOverride: System.Boolean, ):
        ...

    @typing.overload
    def __init__(self, culture: System.Int32, ):
        ...

    @typing.overload
    def __init__(self, culture: System.Int32, useUserOverride: System.Boolean, ):
        ...

    @typing.overload
    @staticmethod
    def CreateSpecificCulture(name: System.String, ) -> System.Globalization.CultureInfo:
        ...

    @typing.overload
    @staticmethod
    def GetCultures(types: System.Globalization.CultureTypes, ) -> list[System.Globalization.CultureInfo]:
        ...

    @typing.overload
    def Equals(self, value: System.Object, ) -> System.Boolean:
        ...

    @typing.overload
    def GetHashCode(self, ) -> System.Int32:
        ...

    @typing.overload
    def ToString(self, ) -> System.String:
        ...

    @typing.overload
    def GetFormat(self, formatType: System.Type, ) -> System.Object:
        ...

    @typing.overload
    def ClearCachedData(self, ) -> None:
        ...

    @typing.overload
    def GetConsoleFallbackUICulture(self, ) -> System.Globalization.CultureInfo:
        ...

    @typing.overload
    def Clone(self, ) -> System.Object:
        ...

    @typing.overload
    @staticmethod
    def ReadOnly(ci: System.Globalization.CultureInfo, ) -> System.Globalization.CultureInfo:
        ...

    @typing.overload
    @staticmethod
    def GetCultureInfo(culture: System.Int32, ) -> System.Globalization.CultureInfo:
        ...

    @typing.overload
    @staticmethod
    def GetCultureInfo(name: System.String, ) -> System.Globalization.CultureInfo:
        ...

    @typing.overload
    @staticmethod
    def GetCultureInfo(name: System.String, altName: System.String, ) -> System.Globalization.CultureInfo:
        ...

    @typing.overload
    @staticmethod
    def GetCultureInfo(name: System.String, predefinedOnly: System.Boolean, ) -> System.Globalization.CultureInfo:
        ...

    @typing.overload
    @staticmethod
    def GetCultureInfoByIetfLanguageTag(name: System.String, ) -> System.Globalization.CultureInfo:
        ...

class CompareOptions(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    None_: System.Int32 = None
    IgnoreCase: System.Int32 = IgnoreCase
    IgnoreNonSpace: System.Int32 = IgnoreNonSpace
    IgnoreSymbols: System.Int32 = IgnoreSymbols
    IgnoreKanaType: System.Int32 = IgnoreKanaType
    IgnoreWidth: System.Int32 = IgnoreWidth
    OrdinalIgnoreCase: System.Int32 = OrdinalIgnoreCase
    StringSort: System.Int32 = StringSort
    Ordinal: System.Int32 = Ordinal

class Calendar(System.ICloneable, System.Object, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def MinSupportedDateTime(self) -> System.DateTime:
        ...

    @property
    def MaxSupportedDateTime(self) -> System.DateTime:
        ...

    @property
    def AlgorithmType(self) -> System.Globalization.CalendarAlgorithmType:
        ...

    @property
    def IsReadOnly(self) -> System.Boolean:
        ...

    @abc.abstractmethod
    @property
    def Eras(self) -> list[System.Int32]:
        ...

    @property
    def TwoDigitYearMax(self) -> System.Int32:
        ...
    @TwoDigitYearMax.setter
    def TwoDigitYearMax(self, val: System.Int32):
        ...

    # methods
    @typing.overload
    def Clone(self, ) -> System.Object:
        ...

    @typing.overload
    @staticmethod
    def ReadOnly(calendar: System.Globalization.Calendar, ) -> System.Globalization.Calendar:
        ...

    @typing.overload
    def AddMilliseconds(self, time: System.DateTime, milliseconds: System.Double, ) -> System.DateTime:
        ...

    @typing.overload
    def AddDays(self, time: System.DateTime, days: System.Int32, ) -> System.DateTime:
        ...

    @typing.overload
    def AddHours(self, time: System.DateTime, hours: System.Int32, ) -> System.DateTime:
        ...

    @typing.overload
    def AddMinutes(self, time: System.DateTime, minutes: System.Int32, ) -> System.DateTime:
        ...

    @typing.overload
    @abc.abstractmethod
    def AddMonths(self, time: System.DateTime, months: System.Int32, ) -> System.DateTime:
        ...

    @typing.overload
    def AddSeconds(self, time: System.DateTime, seconds: System.Int32, ) -> System.DateTime:
        ...

    @typing.overload
    def AddWeeks(self, time: System.DateTime, weeks: System.Int32, ) -> System.DateTime:
        ...

    @typing.overload
    @abc.abstractmethod
    def AddYears(self, time: System.DateTime, years: System.Int32, ) -> System.DateTime:
        ...

    @typing.overload
    @abc.abstractmethod
    def GetDayOfMonth(self, time: System.DateTime, ) -> System.Int32:
        ...

    @typing.overload
    @abc.abstractmethod
    def GetDayOfWeek(self, time: System.DateTime, ) -> System.DayOfWeek:
        ...

    @typing.overload
    @abc.abstractmethod
    def GetDayOfYear(self, time: System.DateTime, ) -> System.Int32:
        ...

    @typing.overload
    def GetDaysInMonth(self, year: System.Int32, month: System.Int32, ) -> System.Int32:
        ...

    @typing.overload
    @abc.abstractmethod
    def GetDaysInMonth(self, year: System.Int32, month: System.Int32, era: System.Int32, ) -> System.Int32:
        ...

    @typing.overload
    def GetDaysInYear(self, year: System.Int32, ) -> System.Int32:
        ...

    @typing.overload
    @abc.abstractmethod
    def GetDaysInYear(self, year: System.Int32, era: System.Int32, ) -> System.Int32:
        ...

    @typing.overload
    @abc.abstractmethod
    def GetEra(self, time: System.DateTime, ) -> System.Int32:
        ...

    @typing.overload
    def GetHour(self, time: System.DateTime, ) -> System.Int32:
        ...

    @typing.overload
    def GetMilliseconds(self, time: System.DateTime, ) -> System.Double:
        ...

    @typing.overload
    def GetMinute(self, time: System.DateTime, ) -> System.Int32:
        ...

    @typing.overload
    @abc.abstractmethod
    def GetMonth(self, time: System.DateTime, ) -> System.Int32:
        ...

    @typing.overload
    def GetMonthsInYear(self, year: System.Int32, ) -> System.Int32:
        ...

    @typing.overload
    @abc.abstractmethod
    def GetMonthsInYear(self, year: System.Int32, era: System.Int32, ) -> System.Int32:
        ...

    @typing.overload
    def GetSecond(self, time: System.DateTime, ) -> System.Int32:
        ...

    @typing.overload
    def GetWeekOfYear(self, time: System.DateTime, rule: System.Globalization.CalendarWeekRule, firstDayOfWeek: System.DayOfWeek, ) -> System.Int32:
        ...

    @typing.overload
    @abc.abstractmethod
    def GetYear(self, time: System.DateTime, ) -> System.Int32:
        ...

    @typing.overload
    def IsLeapDay(self, year: System.Int32, month: System.Int32, day: System.Int32, ) -> System.Boolean:
        ...

    @typing.overload
    @abc.abstractmethod
    def IsLeapDay(self, year: System.Int32, month: System.Int32, day: System.Int32, era: System.Int32, ) -> System.Boolean:
        ...

    @typing.overload
    def IsLeapMonth(self, year: System.Int32, month: System.Int32, ) -> System.Boolean:
        ...

    @typing.overload
    @abc.abstractmethod
    def IsLeapMonth(self, year: System.Int32, month: System.Int32, era: System.Int32, ) -> System.Boolean:
        ...

    @typing.overload
    def GetLeapMonth(self, year: System.Int32, ) -> System.Int32:
        ...

    @typing.overload
    def GetLeapMonth(self, year: System.Int32, era: System.Int32, ) -> System.Int32:
        ...

    @typing.overload
    def IsLeapYear(self, year: System.Int32, ) -> System.Boolean:
        ...

    @typing.overload
    @abc.abstractmethod
    def IsLeapYear(self, year: System.Int32, era: System.Int32, ) -> System.Boolean:
        ...

    @typing.overload
    def ToDateTime(self, year: System.Int32, month: System.Int32, day: System.Int32, hour: System.Int32, minute: System.Int32, second: System.Int32, millisecond: System.Int32, ) -> System.DateTime:
        ...

    @typing.overload
    @abc.abstractmethod
    def ToDateTime(self, year: System.Int32, month: System.Int32, day: System.Int32, hour: System.Int32, minute: System.Int32, second: System.Int32, millisecond: System.Int32, era: System.Int32, ) -> System.DateTime:
        ...

    @typing.overload
    def ToFourDigitYear(self, year: System.Int32, ) -> System.Int32:
        ...

class DateTimeStyles(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    None_: System.Int32 = None
    AllowLeadingWhite: System.Int32 = AllowLeadingWhite
    AllowTrailingWhite: System.Int32 = AllowTrailingWhite
    AllowInnerWhite: System.Int32 = AllowInnerWhite
    AllowWhiteSpaces: System.Int32 = AllowWhiteSpaces
    NoCurrentDateDefault: System.Int32 = NoCurrentDateDefault
    AdjustToUniversal: System.Int32 = AdjustToUniversal
    AssumeLocal: System.Int32 = AssumeLocal
    AssumeUniversal: System.Int32 = AssumeUniversal
    RoundtripKind: System.Int32 = RoundtripKind

class UnicodeCategory(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    UppercaseLetter: System.Int32 = UppercaseLetter
    LowercaseLetter: System.Int32 = LowercaseLetter
    TitlecaseLetter: System.Int32 = TitlecaseLetter
    ModifierLetter: System.Int32 = ModifierLetter
    OtherLetter: System.Int32 = OtherLetter
    NonSpacingMark: System.Int32 = NonSpacingMark
    SpacingCombiningMark: System.Int32 = SpacingCombiningMark
    EnclosingMark: System.Int32 = EnclosingMark
    DecimalDigitNumber: System.Int32 = DecimalDigitNumber
    LetterNumber: System.Int32 = LetterNumber
    OtherNumber: System.Int32 = OtherNumber
    SpaceSeparator: System.Int32 = SpaceSeparator
    LineSeparator: System.Int32 = LineSeparator
    ParagraphSeparator: System.Int32 = ParagraphSeparator
    Control: System.Int32 = Control
    Format: System.Int32 = Format
    Surrogate: System.Int32 = Surrogate
    PrivateUse: System.Int32 = PrivateUse
    ConnectorPunctuation: System.Int32 = ConnectorPunctuation
    DashPunctuation: System.Int32 = DashPunctuation
    OpenPunctuation: System.Int32 = OpenPunctuation
    ClosePunctuation: System.Int32 = ClosePunctuation
    InitialQuotePunctuation: System.Int32 = InitialQuotePunctuation
    FinalQuotePunctuation: System.Int32 = FinalQuotePunctuation
    OtherPunctuation: System.Int32 = OtherPunctuation
    MathSymbol: System.Int32 = MathSymbol
    CurrencySymbol: System.Int32 = CurrencySymbol
    ModifierSymbol: System.Int32 = ModifierSymbol
    OtherSymbol: System.Int32 = OtherSymbol
    OtherNotAssigned: System.Int32 = OtherNotAssigned

class CompareInfo(System.Runtime.Serialization.IDeserializationCallback, System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def Name(self) -> System.String:
        ...

    @property
    def Version(self) -> System.Globalization.SortVersion:
        ...

    @property
    def LCID(self) -> System.Int32:
        ...

    # methods
    @typing.overload
    @staticmethod
    def GetCompareInfo(culture: System.Int32, assembly: System.Reflection.Assembly, ) -> System.Globalization.CompareInfo:
        ...

    @typing.overload
    @staticmethod
    def GetCompareInfo(name: System.String, assembly: System.Reflection.Assembly, ) -> System.Globalization.CompareInfo:
        ...

    @typing.overload
    @staticmethod
    def GetCompareInfo(culture: System.Int32, ) -> System.Globalization.CompareInfo:
        ...

    @typing.overload
    @staticmethod
    def GetCompareInfo(name: System.String, ) -> System.Globalization.CompareInfo:
        ...

    @typing.overload
    @staticmethod
    def IsSortable(ch: System.Char, ) -> System.Boolean:
        ...

    @typing.overload
    @staticmethod
    def IsSortable(text: System.String, ) -> System.Boolean:
        ...

    @typing.overload
    @staticmethod
    def IsSortable(text: System.ReadOnlySpan[System.Char], ) -> System.Boolean:
        ...

    @typing.overload
    @staticmethod
    def IsSortable(value: System.Text.Rune, ) -> System.Boolean:
        ...

    @typing.overload
    def Compare(self, string1: System.String, string2: System.String, ) -> System.Int32:
        ...

    @typing.overload
    def Compare(self, string1: System.String, string2: System.String, options: System.Globalization.CompareOptions, ) -> System.Int32:
        ...

    @typing.overload
    def Compare(self, string1: System.String, offset1: System.Int32, length1: System.Int32, string2: System.String, offset2: System.Int32, length2: System.Int32, ) -> System.Int32:
        ...

    @typing.overload
    def Compare(self, string1: System.String, offset1: System.Int32, string2: System.String, offset2: System.Int32, options: System.Globalization.CompareOptions, ) -> System.Int32:
        ...

    @typing.overload
    def Compare(self, string1: System.String, offset1: System.Int32, string2: System.String, offset2: System.Int32, ) -> System.Int32:
        ...

    @typing.overload
    def Compare(self, string1: System.String, offset1: System.Int32, length1: System.Int32, string2: System.String, offset2: System.Int32, length2: System.Int32, options: System.Globalization.CompareOptions, ) -> System.Int32:
        ...

    @typing.overload
    def Compare(self, string1: System.ReadOnlySpan[System.Char], string2: System.ReadOnlySpan[System.Char], options: System.Globalization.CompareOptions, ) -> System.Int32:
        ...

    @typing.overload
    def IsPrefix(self, source: System.String, prefix: System.String, options: System.Globalization.CompareOptions, ) -> System.Boolean:
        ...

    @typing.overload
    def IsPrefix(self, source: System.ReadOnlySpan[System.Char], prefix: System.ReadOnlySpan[System.Char], options: System.Globalization.CompareOptions, ) -> System.Boolean:
        ...

    @typing.overload
    def IsPrefix(self, source: System.ReadOnlySpan[System.Char], prefix: System.ReadOnlySpan[System.Char], options: System.Globalization.CompareOptions, matchLength: ref[System.Int32], ) -> System.Boolean:
        ...

    @typing.overload
    def IsPrefix(self, source: System.String, prefix: System.String, ) -> System.Boolean:
        ...

    @typing.overload
    def IsSuffix(self, source: System.String, suffix: System.String, options: System.Globalization.CompareOptions, ) -> System.Boolean:
        ...

    @typing.overload
    def IsSuffix(self, source: System.ReadOnlySpan[System.Char], suffix: System.ReadOnlySpan[System.Char], options: System.Globalization.CompareOptions, ) -> System.Boolean:
        ...

    @typing.overload
    def IsSuffix(self, source: System.ReadOnlySpan[System.Char], suffix: System.ReadOnlySpan[System.Char], options: System.Globalization.CompareOptions, matchLength: ref[System.Int32], ) -> System.Boolean:
        ...

    @typing.overload
    def IsSuffix(self, source: System.String, suffix: System.String, ) -> System.Boolean:
        ...

    @typing.overload
    def IndexOf(self, source: System.String, value: System.Char, ) -> System.Int32:
        ...

    @typing.overload
    def IndexOf(self, source: System.String, value: System.String, ) -> System.Int32:
        ...

    @typing.overload
    def IndexOf(self, source: System.String, value: System.Char, options: System.Globalization.CompareOptions, ) -> System.Int32:
        ...

    @typing.overload
    def IndexOf(self, source: System.String, value: System.String, options: System.Globalization.CompareOptions, ) -> System.Int32:
        ...

    @typing.overload
    def IndexOf(self, source: System.String, value: System.Char, startIndex: System.Int32, ) -> System.Int32:
        ...

    @typing.overload
    def IndexOf(self, source: System.String, value: System.String, startIndex: System.Int32, ) -> System.Int32:
        ...

    @typing.overload
    def IndexOf(self, source: System.String, value: System.Char, startIndex: System.Int32, options: System.Globalization.CompareOptions, ) -> System.Int32:
        ...

    @typing.overload
    def IndexOf(self, source: System.String, value: System.String, startIndex: System.Int32, options: System.Globalization.CompareOptions, ) -> System.Int32:
        ...

    @typing.overload
    def IndexOf(self, source: System.String, value: System.Char, startIndex: System.Int32, count: System.Int32, ) -> System.Int32:
        ...

    @typing.overload
    def IndexOf(self, source: System.String, value: System.String, startIndex: System.Int32, count: System.Int32, ) -> System.Int32:
        ...

    @typing.overload
    def IndexOf(self, source: System.String, value: System.Char, startIndex: System.Int32, count: System.Int32, options: System.Globalization.CompareOptions, ) -> System.Int32:
        ...

    @typing.overload
    def IndexOf(self, source: System.String, value: System.String, startIndex: System.Int32, count: System.Int32, options: System.Globalization.CompareOptions, ) -> System.Int32:
        ...

    @typing.overload
    def IndexOf(self, source: System.ReadOnlySpan[System.Char], value: System.ReadOnlySpan[System.Char], options: System.Globalization.CompareOptions, ) -> System.Int32:
        ...

    @typing.overload
    def IndexOf(self, source: System.ReadOnlySpan[System.Char], value: System.ReadOnlySpan[System.Char], options: System.Globalization.CompareOptions, matchLength: ref[System.Int32], ) -> System.Int32:
        ...

    @typing.overload
    def IndexOf(self, source: System.ReadOnlySpan[System.Char], value: System.Text.Rune, options: System.Globalization.CompareOptions, ) -> System.Int32:
        ...

    @typing.overload
    def LastIndexOf(self, source: System.String, value: System.Char, ) -> System.Int32:
        ...

    @typing.overload
    def LastIndexOf(self, source: System.String, value: System.String, ) -> System.Int32:
        ...

    @typing.overload
    def LastIndexOf(self, source: System.String, value: System.Char, options: System.Globalization.CompareOptions, ) -> System.Int32:
        ...

    @typing.overload
    def LastIndexOf(self, source: System.String, value: System.String, options: System.Globalization.CompareOptions, ) -> System.Int32:
        ...

    @typing.overload
    def LastIndexOf(self, source: System.String, value: System.Char, startIndex: System.Int32, ) -> System.Int32:
        ...

    @typing.overload
    def LastIndexOf(self, source: System.String, value: System.String, startIndex: System.Int32, ) -> System.Int32:
        ...

    @typing.overload
    def LastIndexOf(self, source: System.String, value: System.Char, startIndex: System.Int32, options: System.Globalization.CompareOptions, ) -> System.Int32:
        ...

    @typing.overload
    def LastIndexOf(self, source: System.String, value: System.String, startIndex: System.Int32, options: System.Globalization.CompareOptions, ) -> System.Int32:
        ...

    @typing.overload
    def LastIndexOf(self, source: System.String, value: System.Char, startIndex: System.Int32, count: System.Int32, ) -> System.Int32:
        ...

    @typing.overload
    def LastIndexOf(self, source: System.String, value: System.String, startIndex: System.Int32, count: System.Int32, ) -> System.Int32:
        ...

    @typing.overload
    def LastIndexOf(self, source: System.String, value: System.Char, startIndex: System.Int32, count: System.Int32, options: System.Globalization.CompareOptions, ) -> System.Int32:
        ...

    @typing.overload
    def LastIndexOf(self, source: System.String, value: System.String, startIndex: System.Int32, count: System.Int32, options: System.Globalization.CompareOptions, ) -> System.Int32:
        ...

    @typing.overload
    def LastIndexOf(self, source: System.ReadOnlySpan[System.Char], value: System.ReadOnlySpan[System.Char], options: System.Globalization.CompareOptions, ) -> System.Int32:
        ...

    @typing.overload
    def LastIndexOf(self, source: System.ReadOnlySpan[System.Char], value: System.ReadOnlySpan[System.Char], options: System.Globalization.CompareOptions, matchLength: ref[System.Int32], ) -> System.Int32:
        ...

    @typing.overload
    def LastIndexOf(self, source: System.ReadOnlySpan[System.Char], value: System.Text.Rune, options: System.Globalization.CompareOptions, ) -> System.Int32:
        ...

    @typing.overload
    def GetSortKey(self, source: System.String, options: System.Globalization.CompareOptions, ) -> System.Globalization.SortKey:
        ...

    @typing.overload
    def GetSortKey(self, source: System.String, ) -> System.Globalization.SortKey:
        ...

    @typing.overload
    def GetSortKey(self, source: System.ReadOnlySpan[System.Char], destination: System.Span[System.Byte], options: System.Globalization.CompareOptions, ) -> System.Int32:
        ...

    @typing.overload
    def GetSortKeyLength(self, source: System.ReadOnlySpan[System.Char], options: System.Globalization.CompareOptions, ) -> System.Int32:
        ...

    @typing.overload
    def Equals(self, value: System.Object, ) -> System.Boolean:
        ...

    @typing.overload
    def GetHashCode(self, ) -> System.Int32:
        ...

    @typing.overload
    def GetHashCode(self, source: System.String, options: System.Globalization.CompareOptions, ) -> System.Int32:
        ...

    @typing.overload
    def GetHashCode(self, source: System.ReadOnlySpan[System.Char], options: System.Globalization.CompareOptions, ) -> System.Int32:
        ...

    @typing.overload
    def ToString(self, ) -> System.String:
        ...

class TextInfo(System.ICloneable, System.Runtime.Serialization.IDeserializationCallback, System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def ANSICodePage(self) -> System.Int32:
        ...

    @property
    def OEMCodePage(self) -> System.Int32:
        ...

    @property
    def MacCodePage(self) -> System.Int32:
        ...

    @property
    def EBCDICCodePage(self) -> System.Int32:
        ...

    @property
    def LCID(self) -> System.Int32:
        ...

    @property
    def CultureName(self) -> System.String:
        ...

    @property
    def IsReadOnly(self) -> System.Boolean:
        ...

    @property
    def ListSeparator(self) -> System.String:
        ...
    @ListSeparator.setter
    def ListSeparator(self, val: System.String):
        ...

    @property
    def IsRightToLeft(self) -> System.Boolean:
        ...

    # methods
    @typing.overload
    def Clone(self, ) -> System.Object:
        ...

    @typing.overload
    @staticmethod
    def ReadOnly(textInfo: System.Globalization.TextInfo, ) -> System.Globalization.TextInfo:
        ...

    @typing.overload
    def ToLower(self, c: System.Char, ) -> System.Char:
        ...

    @typing.overload
    def ToLower(self, str: System.String, ) -> System.String:
        ...

    @typing.overload
    def ToUpper(self, c: System.Char, ) -> System.Char:
        ...

    @typing.overload
    def ToUpper(self, str: System.String, ) -> System.String:
        ...

    @typing.overload
    def Equals(self, obj: System.Object, ) -> System.Boolean:
        ...

    @typing.overload
    def GetHashCode(self, ) -> System.Int32:
        ...

    @typing.overload
    def ToString(self, ) -> System.String:
        ...

    @typing.overload
    def ToTitleCase(self, str: System.String, ) -> System.String:
        ...

class CultureTypes(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    NeutralCultures: System.Int32 = NeutralCultures
    SpecificCultures: System.Int32 = SpecificCultures
    InstalledWin32Cultures: System.Int32 = InstalledWin32Cultures
    AllCultures: System.Int32 = AllCultures
    UserCustomCulture: System.Int32 = UserCustomCulture
    ReplacementCultures: System.Int32 = ReplacementCultures
    WindowsOnlyCultures: System.Int32 = WindowsOnlyCultures
    FrameworkCultures: System.Int32 = FrameworkCultures

class NumberFormatInfo(System.IFormatProvider, System.ICloneable, System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def InvariantInfo(self) -> System.Globalization.NumberFormatInfo:
        ...

    @property
    def CurrencyDecimalDigits(self) -> System.Int32:
        ...
    @CurrencyDecimalDigits.setter
    def CurrencyDecimalDigits(self, val: System.Int32):
        ...

    @property
    def CurrencyDecimalSeparator(self) -> System.String:
        ...
    @CurrencyDecimalSeparator.setter
    def CurrencyDecimalSeparator(self, val: System.String):
        ...

    @property
    def IsReadOnly(self) -> System.Boolean:
        ...

    @property
    def CurrencyGroupSizes(self) -> list[System.Int32]:
        ...
    @CurrencyGroupSizes.setter
    def CurrencyGroupSizes(self, val: list[System.Int32]):
        ...

    @property
    def NumberGroupSizes(self) -> list[System.Int32]:
        ...
    @NumberGroupSizes.setter
    def NumberGroupSizes(self, val: list[System.Int32]):
        ...

    @property
    def PercentGroupSizes(self) -> list[System.Int32]:
        ...
    @PercentGroupSizes.setter
    def PercentGroupSizes(self, val: list[System.Int32]):
        ...

    @property
    def CurrencyGroupSeparator(self) -> System.String:
        ...
    @CurrencyGroupSeparator.setter
    def CurrencyGroupSeparator(self, val: System.String):
        ...

    @property
    def CurrencySymbol(self) -> System.String:
        ...
    @CurrencySymbol.setter
    def CurrencySymbol(self, val: System.String):
        ...

    @property
    def CurrentInfo(self) -> System.Globalization.NumberFormatInfo:
        ...

    @property
    def NaNSymbol(self) -> System.String:
        ...
    @NaNSymbol.setter
    def NaNSymbol(self, val: System.String):
        ...

    @property
    def CurrencyNegativePattern(self) -> System.Int32:
        ...
    @CurrencyNegativePattern.setter
    def CurrencyNegativePattern(self, val: System.Int32):
        ...

    @property
    def NumberNegativePattern(self) -> System.Int32:
        ...
    @NumberNegativePattern.setter
    def NumberNegativePattern(self, val: System.Int32):
        ...

    @property
    def PercentPositivePattern(self) -> System.Int32:
        ...
    @PercentPositivePattern.setter
    def PercentPositivePattern(self, val: System.Int32):
        ...

    @property
    def PercentNegativePattern(self) -> System.Int32:
        ...
    @PercentNegativePattern.setter
    def PercentNegativePattern(self, val: System.Int32):
        ...

    @property
    def NegativeInfinitySymbol(self) -> System.String:
        ...
    @NegativeInfinitySymbol.setter
    def NegativeInfinitySymbol(self, val: System.String):
        ...

    @property
    def NegativeSign(self) -> System.String:
        ...
    @NegativeSign.setter
    def NegativeSign(self, val: System.String):
        ...

    @property
    def NumberDecimalDigits(self) -> System.Int32:
        ...
    @NumberDecimalDigits.setter
    def NumberDecimalDigits(self, val: System.Int32):
        ...

    @property
    def NumberDecimalSeparator(self) -> System.String:
        ...
    @NumberDecimalSeparator.setter
    def NumberDecimalSeparator(self, val: System.String):
        ...

    @property
    def NumberGroupSeparator(self) -> System.String:
        ...
    @NumberGroupSeparator.setter
    def NumberGroupSeparator(self, val: System.String):
        ...

    @property
    def CurrencyPositivePattern(self) -> System.Int32:
        ...
    @CurrencyPositivePattern.setter
    def CurrencyPositivePattern(self, val: System.Int32):
        ...

    @property
    def PositiveInfinitySymbol(self) -> System.String:
        ...
    @PositiveInfinitySymbol.setter
    def PositiveInfinitySymbol(self, val: System.String):
        ...

    @property
    def PositiveSign(self) -> System.String:
        ...
    @PositiveSign.setter
    def PositiveSign(self, val: System.String):
        ...

    @property
    def PercentDecimalDigits(self) -> System.Int32:
        ...
    @PercentDecimalDigits.setter
    def PercentDecimalDigits(self, val: System.Int32):
        ...

    @property
    def PercentDecimalSeparator(self) -> System.String:
        ...
    @PercentDecimalSeparator.setter
    def PercentDecimalSeparator(self, val: System.String):
        ...

    @property
    def PercentGroupSeparator(self) -> System.String:
        ...
    @PercentGroupSeparator.setter
    def PercentGroupSeparator(self, val: System.String):
        ...

    @property
    def PercentSymbol(self) -> System.String:
        ...
    @PercentSymbol.setter
    def PercentSymbol(self, val: System.String):
        ...

    @property
    def PerMilleSymbol(self) -> System.String:
        ...
    @PerMilleSymbol.setter
    def PerMilleSymbol(self, val: System.String):
        ...

    @property
    def NativeDigits(self) -> list[System.String]:
        ...
    @NativeDigits.setter
    def NativeDigits(self, val: list[System.String]):
        ...

    @property
    def DigitSubstitution(self) -> System.Globalization.DigitShapes:
        ...
    @DigitSubstitution.setter
    def DigitSubstitution(self, val: System.Globalization.DigitShapes):
        ...

    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    @staticmethod
    def GetInstance(formatProvider: System.IFormatProvider, ) -> System.Globalization.NumberFormatInfo:
        ...

    @typing.overload
    def Clone(self, ) -> System.Object:
        ...

    @typing.overload
    def GetFormat(self, formatType: System.Type, ) -> System.Object:
        ...

    @typing.overload
    @staticmethod
    def ReadOnly(nfi: System.Globalization.NumberFormatInfo, ) -> System.Globalization.NumberFormatInfo:
        ...

class DateTimeFormatInfo(System.IFormatProvider, System.ICloneable, System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def InvariantInfo(self) -> System.Globalization.DateTimeFormatInfo:
        ...

    @property
    def CurrentInfo(self) -> System.Globalization.DateTimeFormatInfo:
        ...

    @property
    def AMDesignator(self) -> System.String:
        ...
    @AMDesignator.setter
    def AMDesignator(self, val: System.String):
        ...

    @property
    def Calendar(self) -> System.Globalization.Calendar:
        ...
    @Calendar.setter
    def Calendar(self, val: System.Globalization.Calendar):
        ...

    @property
    def DateSeparator(self) -> System.String:
        ...
    @DateSeparator.setter
    def DateSeparator(self, val: System.String):
        ...

    @property
    def FirstDayOfWeek(self) -> System.DayOfWeek:
        ...
    @FirstDayOfWeek.setter
    def FirstDayOfWeek(self, val: System.DayOfWeek):
        ...

    @property
    def CalendarWeekRule(self) -> System.Globalization.CalendarWeekRule:
        ...
    @CalendarWeekRule.setter
    def CalendarWeekRule(self, val: System.Globalization.CalendarWeekRule):
        ...

    @property
    def FullDateTimePattern(self) -> System.String:
        ...
    @FullDateTimePattern.setter
    def FullDateTimePattern(self, val: System.String):
        ...

    @property
    def LongDatePattern(self) -> System.String:
        ...
    @LongDatePattern.setter
    def LongDatePattern(self, val: System.String):
        ...

    @property
    def LongTimePattern(self) -> System.String:
        ...
    @LongTimePattern.setter
    def LongTimePattern(self, val: System.String):
        ...

    @property
    def MonthDayPattern(self) -> System.String:
        ...
    @MonthDayPattern.setter
    def MonthDayPattern(self, val: System.String):
        ...

    @property
    def PMDesignator(self) -> System.String:
        ...
    @PMDesignator.setter
    def PMDesignator(self, val: System.String):
        ...

    @property
    def RFC1123Pattern(self) -> System.String:
        ...

    @property
    def ShortDatePattern(self) -> System.String:
        ...
    @ShortDatePattern.setter
    def ShortDatePattern(self, val: System.String):
        ...

    @property
    def ShortTimePattern(self) -> System.String:
        ...
    @ShortTimePattern.setter
    def ShortTimePattern(self, val: System.String):
        ...

    @property
    def SortableDateTimePattern(self) -> System.String:
        ...

    @property
    def TimeSeparator(self) -> System.String:
        ...
    @TimeSeparator.setter
    def TimeSeparator(self, val: System.String):
        ...

    @property
    def UniversalSortableDateTimePattern(self) -> System.String:
        ...

    @property
    def YearMonthPattern(self) -> System.String:
        ...
    @YearMonthPattern.setter
    def YearMonthPattern(self, val: System.String):
        ...

    @property
    def AbbreviatedDayNames(self) -> list[System.String]:
        ...
    @AbbreviatedDayNames.setter
    def AbbreviatedDayNames(self, val: list[System.String]):
        ...

    @property
    def ShortestDayNames(self) -> list[System.String]:
        ...
    @ShortestDayNames.setter
    def ShortestDayNames(self, val: list[System.String]):
        ...

    @property
    def DayNames(self) -> list[System.String]:
        ...
    @DayNames.setter
    def DayNames(self, val: list[System.String]):
        ...

    @property
    def AbbreviatedMonthNames(self) -> list[System.String]:
        ...
    @AbbreviatedMonthNames.setter
    def AbbreviatedMonthNames(self, val: list[System.String]):
        ...

    @property
    def MonthNames(self) -> list[System.String]:
        ...
    @MonthNames.setter
    def MonthNames(self, val: list[System.String]):
        ...

    @property
    def IsReadOnly(self) -> System.Boolean:
        ...

    @property
    def NativeCalendarName(self) -> System.String:
        ...

    @property
    def AbbreviatedMonthGenitiveNames(self) -> list[System.String]:
        ...
    @AbbreviatedMonthGenitiveNames.setter
    def AbbreviatedMonthGenitiveNames(self, val: list[System.String]):
        ...

    @property
    def MonthGenitiveNames(self) -> list[System.String]:
        ...
    @MonthGenitiveNames.setter
    def MonthGenitiveNames(self, val: list[System.String]):
        ...

    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def GetAllDateTimePatterns(self, ) -> list[System.String]:
        ...

    @typing.overload
    def GetAllDateTimePatterns(self, format: System.Char, ) -> list[System.String]:
        ...

    @typing.overload
    def GetDayName(self, dayofweek: System.DayOfWeek, ) -> System.String:
        ...

    @typing.overload
    def GetAbbreviatedMonthName(self, month: System.Int32, ) -> System.String:
        ...

    @typing.overload
    def GetMonthName(self, month: System.Int32, ) -> System.String:
        ...

    @typing.overload
    @staticmethod
    def ReadOnly(dtfi: System.Globalization.DateTimeFormatInfo, ) -> System.Globalization.DateTimeFormatInfo:
        ...

    @typing.overload
    def SetAllDateTimePatterns(self, patterns: list[System.String], format: System.Char, ) -> None:
        ...

    @typing.overload
    @staticmethod
    def GetInstance(provider: System.IFormatProvider, ) -> System.Globalization.DateTimeFormatInfo:
        ...

    @typing.overload
    def GetFormat(self, formatType: System.Type, ) -> System.Object:
        ...

    @typing.overload
    def Clone(self, ) -> System.Object:
        ...

    @typing.overload
    def GetEra(self, eraName: System.String, ) -> System.Int32:
        ...

    @typing.overload
    def GetEraName(self, era: System.Int32, ) -> System.String:
        ...

    @typing.overload
    def GetAbbreviatedEraName(self, era: System.Int32, ) -> System.String:
        ...

    @typing.overload
    def GetAbbreviatedDayName(self, dayofweek: System.DayOfWeek, ) -> System.String:
        ...

    @typing.overload
    def GetShortestDayName(self, dayOfWeek: System.DayOfWeek, ) -> System.String:
        ...

class TimeSpanStyles(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    None_: System.Int32 = None
    AssumeNegative: System.Int32 = AssumeNegative

class CalendarAlgorithmType(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    Unknown: System.Int32 = Unknown
    SolarCalendar: System.Int32 = SolarCalendar
    LunarCalendar: System.Int32 = LunarCalendar
    LunisolarCalendar: System.Int32 = LunisolarCalendar

class CalendarWeekRule(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    FirstDay: System.Int32 = FirstDay
    FirstFullWeek: System.Int32 = FirstFullWeek
    FirstFourDayWeek: System.Int32 = FirstFourDayWeek

class SortVersion(System.IEquatable[System.Globalization.SortVersion], System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def FullVersion(self) -> System.Int32:
        ...

    @property
    def SortId(self) -> System.Guid:
        ...

    # methods
    @typing.overload
    def __init__(self, fullVersion: System.Int32, sortId: System.Guid, ):
        ...

    @typing.overload
    def Equals(self, obj: System.Object, ) -> System.Boolean:
        ...

    @typing.overload
    def Equals(self, other: System.Globalization.SortVersion, ) -> System.Boolean:
        ...

    @typing.overload
    def GetHashCode(self, ) -> System.Int32:
        ...

class SortKey(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def OriginalString(self) -> System.String:
        ...

    @property
    def KeyData(self) -> list[System.Byte]:
        ...

    # methods
    @typing.overload
    @staticmethod
    def Compare(sortkey1: System.Globalization.SortKey, sortkey2: System.Globalization.SortKey, ) -> System.Int32:
        ...

    @typing.overload
    def Equals(self, value: System.Object, ) -> System.Boolean:
        ...

    @typing.overload
    def GetHashCode(self, ) -> System.Int32:
        ...

    @typing.overload
    def ToString(self, ) -> System.String:
        ...

class DigitShapes(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    Context: System.Int32 = Context
    None_: System.Int32 = None
    NativeNational: System.Int32 = NativeNational

