from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import System
import System.ComponentModel
import System.Data
import System.Data.Common
import Microsoft.Data.Sqlite
import System.Threading.Tasks
import System.Threading
import System.Collections
import SQLitePCL
import System.IO
import System.Collections.Generic

T = typing.TypeVar('T')
TResult = typing.TypeVar('TResult')
T1 = typing.TypeVar('T1')
T2 = typing.TypeVar('T2')
T3 = typing.TypeVar('T3')
T4 = typing.TypeVar('T4')
T5 = typing.TypeVar('T5')
T6 = typing.TypeVar('T6')
T7 = typing.TypeVar('T7')
T8 = typing.TypeVar('T8')
T9 = typing.TypeVar('T9')
T10 = typing.TypeVar('T10')
T11 = typing.TypeVar('T11')
T12 = typing.TypeVar('T12')
T13 = typing.TypeVar('T13')
T14 = typing.TypeVar('T14')
T15 = typing.TypeVar('T15')
T16 = typing.TypeVar('T16')
TState = typing.TypeVar('TState')
TAccumulate = typing.TypeVar('TAccumulate')

class SqliteType(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    Integer: System.Int32 = Integer
    Real: System.Int32 = Real
    Text: System.Int32 = Text
    Blob: System.Int32 = Blob

class SqliteCommand(System.ComponentModel.IComponent, System.IDisposable, System.Data.IDbCommand, System.IAsyncDisposable, System.Data.Common.DbCommand):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def CommandType(self) -> System.Data.CommandType:
        ...
    @CommandType.setter
    def CommandType(self, val: System.Data.CommandType):
        ...

    @property
    def CommandText(self) -> System.String:
        ...
    @CommandText.setter
    def CommandText(self, val: System.String):
        ...

    @property
    def Connection(self) -> Microsoft.Data.Sqlite.SqliteConnection:
        ...
    @Connection.setter
    def Connection(self, val: Microsoft.Data.Sqlite.SqliteConnection):
        ...

    @property
    def Transaction(self) -> Microsoft.Data.Sqlite.SqliteTransaction:
        ...
    @Transaction.setter
    def Transaction(self, val: Microsoft.Data.Sqlite.SqliteTransaction):
        ...

    @property
    def Parameters(self) -> Microsoft.Data.Sqlite.SqliteParameterCollection:
        ...

    @property
    def CommandTimeout(self) -> System.Int32:
        ...
    @CommandTimeout.setter
    def CommandTimeout(self, val: System.Int32):
        ...

    @property
    def DesignTimeVisible(self) -> System.Boolean:
        ...
    @DesignTimeVisible.setter
    def DesignTimeVisible(self, val: System.Boolean):
        ...

    @property
    def UpdatedRowSource(self) -> System.Data.UpdateRowSource:
        ...
    @UpdatedRowSource.setter
    def UpdatedRowSource(self, val: System.Data.UpdateRowSource):
        ...

    @property
    def Connection(self) -> System.Data.Common.DbConnection:
        ...
    @Connection.setter
    def Connection(self, val: System.Data.Common.DbConnection):
        ...

    @property
    def Parameters(self) -> System.Data.Common.DbParameterCollection:
        ...

    @property
    def Transaction(self) -> System.Data.Common.DbTransaction:
        ...
    @Transaction.setter
    def Transaction(self, val: System.Data.Common.DbTransaction):
        ...

    @property
    def Site(self) -> System.ComponentModel.ISite:
        ...
    @Site.setter
    def Site(self, val: System.ComponentModel.ISite):
        ...

    @property
    def Container(self) -> System.ComponentModel.IContainer:
        ...

    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def __init__(self, commandText: System.String, ):
        ...

    @typing.overload
    def __init__(self, commandText: System.String, connection: Microsoft.Data.Sqlite.SqliteConnection, ):
        ...

    @typing.overload
    def __init__(self, commandText: System.String, connection: Microsoft.Data.Sqlite.SqliteConnection, transaction: Microsoft.Data.Sqlite.SqliteTransaction, ):
        ...

    @typing.overload
    def CreateParameter(self, ) -> Microsoft.Data.Sqlite.SqliteParameter:
        ...

    @typing.overload
    def Prepare(self, ) -> None:
        ...

    @typing.overload
    def ExecuteReader(self, ) -> Microsoft.Data.Sqlite.SqliteDataReader:
        ...

    @typing.overload
    def ExecuteReader(self, behavior: System.Data.CommandBehavior, ) -> Microsoft.Data.Sqlite.SqliteDataReader:
        ...

    @typing.overload
    def ExecuteReaderAsync(self, ) -> System.Threading.Tasks.Task[Microsoft.Data.Sqlite.SqliteDataReader]:
        ...

    @typing.overload
    def ExecuteReaderAsync(self, cancellationToken: System.Threading.CancellationToken, ) -> System.Threading.Tasks.Task[Microsoft.Data.Sqlite.SqliteDataReader]:
        ...

    @typing.overload
    def ExecuteReaderAsync(self, behavior: System.Data.CommandBehavior, ) -> System.Threading.Tasks.Task[Microsoft.Data.Sqlite.SqliteDataReader]:
        ...

    @typing.overload
    def ExecuteReaderAsync(self, behavior: System.Data.CommandBehavior, cancellationToken: System.Threading.CancellationToken, ) -> System.Threading.Tasks.Task[Microsoft.Data.Sqlite.SqliteDataReader]:
        ...

    @typing.overload
    def ExecuteNonQuery(self, ) -> System.Int32:
        ...

    @typing.overload
    def ExecuteScalar(self, ) -> System.Object:
        ...

    @typing.overload
    def Cancel(self, ) -> None:
        ...

class SqliteDataReader(System.Data.IDataReader, System.IDisposable, System.Data.IDataRecord, System.Collections.IEnumerable, System.IAsyncDisposable, System.Data.Common.DbDataReader):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def Depth(self) -> System.Int32:
        ...

    @property
    def FieldCount(self) -> System.Int32:
        ...

    @property
    def Handle(self) -> SQLitePCL.sqlite3_stmt:
        ...

    @property
    def HasRows(self) -> System.Boolean:
        ...

    @property
    def IsClosed(self) -> System.Boolean:
        ...

    @property
    def RecordsAffected(self) -> System.Int32:
        ...

    @property
    def Item(self) -> System.Object:
        ...

    @property
    def Item(self) -> System.Object:
        ...

    @property
    def VisibleFieldCount(self) -> System.Int32:
        ...

    # methods
    @typing.overload
    def GetEnumerator(self, ) -> System.Collections.IEnumerator:
        ...

    @typing.overload
    def Read(self, ) -> System.Boolean:
        ...

    @typing.overload
    def NextResult(self, ) -> System.Boolean:
        ...

    @typing.overload
    def Close(self, ) -> None:
        ...

    @typing.overload
    def GetName(self, ordinal: System.Int32, ) -> System.String:
        ...

    @typing.overload
    def GetOrdinal(self, name: System.String, ) -> System.Int32:
        ...

    @typing.overload
    def GetDataTypeName(self, ordinal: System.Int32, ) -> System.String:
        ...

    @typing.overload
    def GetFieldType(self, ordinal: System.Int32, ) -> System.Type:
        ...

    @typing.overload
    def IsDBNull(self, ordinal: System.Int32, ) -> System.Boolean:
        ...

    @typing.overload
    def GetBoolean(self, ordinal: System.Int32, ) -> System.Boolean:
        ...

    @typing.overload
    def GetByte(self, ordinal: System.Int32, ) -> System.Byte:
        ...

    @typing.overload
    def GetChar(self, ordinal: System.Int32, ) -> System.Char:
        ...

    @typing.overload
    def GetDateTime(self, ordinal: System.Int32, ) -> System.DateTime:
        ...

    @typing.overload
    def GetDateTimeOffset(self, ordinal: System.Int32, ) -> System.DateTimeOffset:
        ...

    @typing.overload
    def GetTimeSpan(self, ordinal: System.Int32, ) -> System.TimeSpan:
        ...

    @typing.overload
    def GetDecimal(self, ordinal: System.Int32, ) -> System.Decimal:
        ...

    @typing.overload
    def GetDouble(self, ordinal: System.Int32, ) -> System.Double:
        ...

    @typing.overload
    def GetFloat(self, ordinal: System.Int32, ) -> System.Single:
        ...

    @typing.overload
    def GetGuid(self, ordinal: System.Int32, ) -> System.Guid:
        ...

    @typing.overload
    def GetInt16(self, ordinal: System.Int32, ) -> System.Int16:
        ...

    @typing.overload
    def GetInt32(self, ordinal: System.Int32, ) -> System.Int32:
        ...

    @typing.overload
    def GetInt64(self, ordinal: System.Int32, ) -> System.Int64:
        ...

    @typing.overload
    def GetString(self, ordinal: System.Int32, ) -> System.String:
        ...

    @typing.overload
    def GetBytes(self, ordinal: System.Int32, dataOffset: System.Int64, buffer: list[System.Byte], bufferOffset: System.Int32, length: System.Int32, ) -> System.Int64:
        ...

    @typing.overload
    def GetChars(self, ordinal: System.Int32, dataOffset: System.Int64, buffer: list[System.Char], bufferOffset: System.Int32, length: System.Int32, ) -> System.Int64:
        ...

    @typing.overload
    def GetStream(self, ordinal: System.Int32, ) -> System.IO.Stream:
        ...

    @typing.overload
    def GetTextReader(self, ordinal: System.Int32, ) -> System.IO.TextReader:
        ...

    @typing.overload
    def GetFieldValue(self, ordinal: System.Int32, ) -> T:
        ...

    @typing.overload
    def GetValue(self, ordinal: System.Int32, ) -> System.Object:
        ...

    @typing.overload
    def GetValues(self, values: list[System.Object], ) -> System.Int32:
        ...

    @typing.overload
    def GetSchemaTable(self, ) -> System.Data.DataTable:
        ...

class SqliteConnection(System.ComponentModel.IComponent, System.IDisposable, System.Data.IDbConnection, System.IAsyncDisposable, System.Data.Common.DbConnection):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def Handle(self) -> SQLitePCL.sqlite3:
        ...

    @property
    def ConnectionString(self) -> System.String:
        ...
    @ConnectionString.setter
    def ConnectionString(self, val: System.String):
        ...

    @property
    def Database(self) -> System.String:
        ...

    @property
    def DataSource(self) -> System.String:
        ...

    @property
    def DefaultTimeout(self) -> System.Int32:
        ...
    @DefaultTimeout.setter
    def DefaultTimeout(self, val: System.Int32):
        ...

    @property
    def ServerVersion(self) -> System.String:
        ...

    @property
    def State(self) -> System.Data.ConnectionState:
        ...

    @property
    def ConnectionTimeout(self) -> System.Int32:
        ...

    @property
    def CanCreateBatch(self) -> System.Boolean:
        ...

    @property
    def Site(self) -> System.ComponentModel.ISite:
        ...
    @Site.setter
    def Site(self, val: System.ComponentModel.ISite):
        ...

    @property
    def Container(self) -> System.ComponentModel.IContainer:
        ...

    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def __init__(self, connectionString: System.String, ):
        ...

    @typing.overload
    def BeginTransaction(self, isolationLevel: System.Data.IsolationLevel, deferred: System.Boolean, ) -> Microsoft.Data.Sqlite.SqliteTransaction:
        ...

    @typing.overload
    def ChangeDatabase(self, databaseName: System.String, ) -> None:
        ...

    @typing.overload
    def EnableExtensions(self, enable: System.Boolean, ) -> None:
        ...

    @typing.overload
    def LoadExtension(self, file: System.String, proc: System.String, ) -> None:
        ...

    @typing.overload
    def BackupDatabase(self, destination: Microsoft.Data.Sqlite.SqliteConnection, ) -> None:
        ...

    @typing.overload
    def BackupDatabase(self, destination: Microsoft.Data.Sqlite.SqliteConnection, destinationName: System.String, sourceName: System.String, ) -> None:
        ...

    @typing.overload
    def GetSchema(self, ) -> System.Data.DataTable:
        ...

    @typing.overload
    def GetSchema(self, collectionName: System.String, ) -> System.Data.DataTable:
        ...

    @typing.overload
    def GetSchema(self, collectionName: System.String, restrictionValues: list[System.String], ) -> System.Data.DataTable:
        ...

    @typing.overload
    def CreateFunction(self, name: System.String, function: System.Func[TResult], isDeterministic: System.Boolean, ) -> None:
        ...

    @typing.overload
    def CreateFunction(self, name: System.String, function: System.Func[T1, TResult], isDeterministic: System.Boolean, ) -> None:
        ...

    @typing.overload
    def CreateFunction(self, name: System.String, function: System.Func[T1, T2, TResult], isDeterministic: System.Boolean, ) -> None:
        ...

    @typing.overload
    def CreateFunction(self, name: System.String, function: System.Func[T1, T2, T3, TResult], isDeterministic: System.Boolean, ) -> None:
        ...

    @typing.overload
    def CreateFunction(self, name: System.String, function: System.Func[T1, T2, T3, T4, TResult], isDeterministic: System.Boolean, ) -> None:
        ...

    @typing.overload
    def CreateFunction(self, name: System.String, function: System.Func[T1, T2, T3, T4, T5, TResult], isDeterministic: System.Boolean, ) -> None:
        ...

    @typing.overload
    def CreateFunction(self, name: System.String, function: System.Func[T1, T2, T3, T4, T5, T6, TResult], isDeterministic: System.Boolean, ) -> None:
        ...

    @typing.overload
    def CreateFunction(self, name: System.String, function: System.Func[T1, T2, T3, T4, T5, T6, T7, TResult], isDeterministic: System.Boolean, ) -> None:
        ...

    @typing.overload
    def CreateFunction(self, name: System.String, function: System.Func[T1, T2, T3, T4, T5, T6, T7, T8, TResult], isDeterministic: System.Boolean, ) -> None:
        ...

    @typing.overload
    def CreateFunction(self, name: System.String, function: System.Func[T1, T2, T3, T4, T5, T6, T7, T8, T9, TResult], isDeterministic: System.Boolean, ) -> None:
        ...

    @typing.overload
    def CreateFunction(self, name: System.String, function: System.Func[T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, TResult], isDeterministic: System.Boolean, ) -> None:
        ...

    @typing.overload
    def CreateFunction(self, name: System.String, function: System.Func[T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, TResult], isDeterministic: System.Boolean, ) -> None:
        ...

    @typing.overload
    def CreateFunction(self, name: System.String, function: System.Func[T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, TResult], isDeterministic: System.Boolean, ) -> None:
        ...

    @typing.overload
    def CreateFunction(self, name: System.String, function: System.Func[T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13, TResult], isDeterministic: System.Boolean, ) -> None:
        ...

    @typing.overload
    def CreateFunction(self, name: System.String, function: System.Func[T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13, T14, TResult], isDeterministic: System.Boolean, ) -> None:
        ...

    @typing.overload
    def CreateFunction(self, name: System.String, function: System.Func[T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13, T14, T15, TResult], isDeterministic: System.Boolean, ) -> None:
        ...

    @typing.overload
    def CreateFunction(self, name: System.String, function: System.Func[T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13, T14, T15, T16, TResult], isDeterministic: System.Boolean, ) -> None:
        ...

    @typing.overload
    def CreateFunction(self, name: System.String, function: System.Func[list[System.Object], TResult], isDeterministic: System.Boolean, ) -> None:
        ...

    @typing.overload
    def CreateFunction(self, name: System.String, state: TState, function: System.Func[TState, TResult], isDeterministic: System.Boolean, ) -> None:
        ...

    @typing.overload
    def CreateFunction(self, name: System.String, state: TState, function: System.Func[TState, T1, TResult], isDeterministic: System.Boolean, ) -> None:
        ...

    @typing.overload
    def CreateFunction(self, name: System.String, state: TState, function: System.Func[TState, T1, T2, TResult], isDeterministic: System.Boolean, ) -> None:
        ...

    @typing.overload
    def CreateFunction(self, name: System.String, state: TState, function: System.Func[TState, T1, T2, T3, TResult], isDeterministic: System.Boolean, ) -> None:
        ...

    @typing.overload
    def CreateFunction(self, name: System.String, state: TState, function: System.Func[TState, T1, T2, T3, T4, TResult], isDeterministic: System.Boolean, ) -> None:
        ...

    @typing.overload
    def CreateFunction(self, name: System.String, state: TState, function: System.Func[TState, T1, T2, T3, T4, T5, TResult], isDeterministic: System.Boolean, ) -> None:
        ...

    @typing.overload
    def CreateFunction(self, name: System.String, state: TState, function: System.Func[TState, T1, T2, T3, T4, T5, T6, TResult], isDeterministic: System.Boolean, ) -> None:
        ...

    @typing.overload
    def CreateFunction(self, name: System.String, state: TState, function: System.Func[TState, T1, T2, T3, T4, T5, T6, T7, TResult], isDeterministic: System.Boolean, ) -> None:
        ...

    @typing.overload
    def CreateFunction(self, name: System.String, state: TState, function: System.Func[TState, T1, T2, T3, T4, T5, T6, T7, T8, TResult], isDeterministic: System.Boolean, ) -> None:
        ...

    @typing.overload
    def CreateFunction(self, name: System.String, state: TState, function: System.Func[TState, T1, T2, T3, T4, T5, T6, T7, T8, T9, TResult], isDeterministic: System.Boolean, ) -> None:
        ...

    @typing.overload
    def CreateFunction(self, name: System.String, state: TState, function: System.Func[TState, T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, TResult], isDeterministic: System.Boolean, ) -> None:
        ...

    @typing.overload
    def CreateFunction(self, name: System.String, state: TState, function: System.Func[TState, T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, TResult], isDeterministic: System.Boolean, ) -> None:
        ...

    @typing.overload
    def CreateFunction(self, name: System.String, state: TState, function: System.Func[TState, T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, TResult], isDeterministic: System.Boolean, ) -> None:
        ...

    @typing.overload
    def CreateFunction(self, name: System.String, state: TState, function: System.Func[TState, T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13, TResult], isDeterministic: System.Boolean, ) -> None:
        ...

    @typing.overload
    def CreateFunction(self, name: System.String, state: TState, function: System.Func[TState, T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13, T14, TResult], isDeterministic: System.Boolean, ) -> None:
        ...

    @typing.overload
    def CreateFunction(self, name: System.String, state: TState, function: System.Func[TState, T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13, T14, T15, TResult], isDeterministic: System.Boolean, ) -> None:
        ...

    @typing.overload
    def CreateFunction(self, name: System.String, state: TState, function: System.Func[TState, list[System.Object], TResult], isDeterministic: System.Boolean, ) -> None:
        ...

    @typing.overload
    @staticmethod
    def ClearAllPools() -> None:
        ...

    @typing.overload
    @staticmethod
    def ClearPool(connection: Microsoft.Data.Sqlite.SqliteConnection, ) -> None:
        ...

    @typing.overload
    def Open(self, ) -> None:
        ...

    @typing.overload
    def Close(self, ) -> None:
        ...

    @typing.overload
    def CreateCommand(self, ) -> Microsoft.Data.Sqlite.SqliteCommand:
        ...

    @typing.overload
    def CreateCollation(self, name: System.String, comparison: System.Comparison[System.String], ) -> None:
        ...

    @typing.overload
    def CreateCollation(self, name: System.String, state: T, comparison: System.Func[T, System.String, System.String, System.Int32], ) -> None:
        ...

    @typing.overload
    def BeginTransaction(self, ) -> Microsoft.Data.Sqlite.SqliteTransaction:
        ...

    @typing.overload
    def BeginTransaction(self, deferred: System.Boolean, ) -> Microsoft.Data.Sqlite.SqliteTransaction:
        ...

    @typing.overload
    def BeginTransaction(self, isolationLevel: System.Data.IsolationLevel, ) -> Microsoft.Data.Sqlite.SqliteTransaction:
        ...

    @typing.overload
    def CreateAggregate(self, name: System.String, func: System.Func[TAccumulate, TAccumulate], isDeterministic: System.Boolean, ) -> None:
        ...

    @typing.overload
    def CreateAggregate(self, name: System.String, func: System.Func[TAccumulate, T1, TAccumulate], isDeterministic: System.Boolean, ) -> None:
        ...

    @typing.overload
    def CreateAggregate(self, name: System.String, func: System.Func[TAccumulate, T1, T2, TAccumulate], isDeterministic: System.Boolean, ) -> None:
        ...

    @typing.overload
    def CreateAggregate(self, name: System.String, func: System.Func[TAccumulate, T1, T2, T3, TAccumulate], isDeterministic: System.Boolean, ) -> None:
        ...

    @typing.overload
    def CreateAggregate(self, name: System.String, func: System.Func[TAccumulate, T1, T2, T3, T4, TAccumulate], isDeterministic: System.Boolean, ) -> None:
        ...

    @typing.overload
    def CreateAggregate(self, name: System.String, func: System.Func[TAccumulate, T1, T2, T3, T4, T5, TAccumulate], isDeterministic: System.Boolean, ) -> None:
        ...

    @typing.overload
    def CreateAggregate(self, name: System.String, func: System.Func[TAccumulate, T1, T2, T3, T4, T5, T6, TAccumulate], isDeterministic: System.Boolean, ) -> None:
        ...

    @typing.overload
    def CreateAggregate(self, name: System.String, func: System.Func[TAccumulate, T1, T2, T3, T4, T5, T6, T7, TAccumulate], isDeterministic: System.Boolean, ) -> None:
        ...

    @typing.overload
    def CreateAggregate(self, name: System.String, func: System.Func[TAccumulate, T1, T2, T3, T4, T5, T6, T7, T8, TAccumulate], isDeterministic: System.Boolean, ) -> None:
        ...

    @typing.overload
    def CreateAggregate(self, name: System.String, func: System.Func[TAccumulate, T1, T2, T3, T4, T5, T6, T7, T8, T9, TAccumulate], isDeterministic: System.Boolean, ) -> None:
        ...

    @typing.overload
    def CreateAggregate(self, name: System.String, func: System.Func[TAccumulate, T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, TAccumulate], isDeterministic: System.Boolean, ) -> None:
        ...

    @typing.overload
    def CreateAggregate(self, name: System.String, func: System.Func[TAccumulate, T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, TAccumulate], isDeterministic: System.Boolean, ) -> None:
        ...

    @typing.overload
    def CreateAggregate(self, name: System.String, func: System.Func[TAccumulate, T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, TAccumulate], isDeterministic: System.Boolean, ) -> None:
        ...

    @typing.overload
    def CreateAggregate(self, name: System.String, func: System.Func[TAccumulate, T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13, TAccumulate], isDeterministic: System.Boolean, ) -> None:
        ...

    @typing.overload
    def CreateAggregate(self, name: System.String, func: System.Func[TAccumulate, T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13, T14, TAccumulate], isDeterministic: System.Boolean, ) -> None:
        ...

    @typing.overload
    def CreateAggregate(self, name: System.String, func: System.Func[TAccumulate, T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13, T14, T15, TAccumulate], isDeterministic: System.Boolean, ) -> None:
        ...

    @typing.overload
    def CreateAggregate(self, name: System.String, func: System.Func[TAccumulate, list[System.Object], TAccumulate], isDeterministic: System.Boolean, ) -> None:
        ...

    @typing.overload
    def CreateAggregate(self, name: System.String, seed: TAccumulate, func: System.Func[TAccumulate, TAccumulate], isDeterministic: System.Boolean, ) -> None:
        ...

    @typing.overload
    def CreateAggregate(self, name: System.String, seed: TAccumulate, func: System.Func[TAccumulate, T1, TAccumulate], isDeterministic: System.Boolean, ) -> None:
        ...

    @typing.overload
    def CreateAggregate(self, name: System.String, seed: TAccumulate, func: System.Func[TAccumulate, T1, T2, TAccumulate], isDeterministic: System.Boolean, ) -> None:
        ...

    @typing.overload
    def CreateAggregate(self, name: System.String, seed: TAccumulate, func: System.Func[TAccumulate, T1, T2, T3, TAccumulate], isDeterministic: System.Boolean, ) -> None:
        ...

    @typing.overload
    def CreateAggregate(self, name: System.String, seed: TAccumulate, func: System.Func[TAccumulate, T1, T2, T3, T4, TAccumulate], isDeterministic: System.Boolean, ) -> None:
        ...

    @typing.overload
    def CreateAggregate(self, name: System.String, seed: TAccumulate, func: System.Func[TAccumulate, T1, T2, T3, T4, T5, TAccumulate], isDeterministic: System.Boolean, ) -> None:
        ...

    @typing.overload
    def CreateAggregate(self, name: System.String, seed: TAccumulate, func: System.Func[TAccumulate, T1, T2, T3, T4, T5, T6, TAccumulate], isDeterministic: System.Boolean, ) -> None:
        ...

    @typing.overload
    def CreateAggregate(self, name: System.String, seed: TAccumulate, func: System.Func[TAccumulate, T1, T2, T3, T4, T5, T6, T7, TAccumulate], isDeterministic: System.Boolean, ) -> None:
        ...

    @typing.overload
    def CreateAggregate(self, name: System.String, seed: TAccumulate, func: System.Func[TAccumulate, T1, T2, T3, T4, T5, T6, T7, T8, TAccumulate], isDeterministic: System.Boolean, ) -> None:
        ...

    @typing.overload
    def CreateAggregate(self, name: System.String, seed: TAccumulate, func: System.Func[TAccumulate, T1, T2, T3, T4, T5, T6, T7, T8, T9, TAccumulate], isDeterministic: System.Boolean, ) -> None:
        ...

    @typing.overload
    def CreateAggregate(self, name: System.String, seed: TAccumulate, func: System.Func[TAccumulate, T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, TAccumulate], isDeterministic: System.Boolean, ) -> None:
        ...

    @typing.overload
    def CreateAggregate(self, name: System.String, seed: TAccumulate, func: System.Func[TAccumulate, T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, TAccumulate], isDeterministic: System.Boolean, ) -> None:
        ...

    @typing.overload
    def CreateAggregate(self, name: System.String, seed: TAccumulate, func: System.Func[TAccumulate, T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, TAccumulate], isDeterministic: System.Boolean, ) -> None:
        ...

    @typing.overload
    def CreateAggregate(self, name: System.String, seed: TAccumulate, func: System.Func[TAccumulate, T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13, TAccumulate], isDeterministic: System.Boolean, ) -> None:
        ...

    @typing.overload
    def CreateAggregate(self, name: System.String, seed: TAccumulate, func: System.Func[TAccumulate, T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13, T14, TAccumulate], isDeterministic: System.Boolean, ) -> None:
        ...

    @typing.overload
    def CreateAggregate(self, name: System.String, seed: TAccumulate, func: System.Func[TAccumulate, T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13, T14, T15, TAccumulate], isDeterministic: System.Boolean, ) -> None:
        ...

    @typing.overload
    def CreateAggregate(self, name: System.String, seed: TAccumulate, func: System.Func[TAccumulate, list[System.Object], TAccumulate], isDeterministic: System.Boolean, ) -> None:
        ...

    @typing.overload
    def CreateAggregate(self, name: System.String, seed: TAccumulate, func: System.Func[TAccumulate, TAccumulate], resultSelector: System.Func[TAccumulate, TResult], isDeterministic: System.Boolean, ) -> None:
        ...

    @typing.overload
    def CreateAggregate(self, name: System.String, seed: TAccumulate, func: System.Func[TAccumulate, T1, TAccumulate], resultSelector: System.Func[TAccumulate, TResult], isDeterministic: System.Boolean, ) -> None:
        ...

    @typing.overload
    def CreateAggregate(self, name: System.String, seed: TAccumulate, func: System.Func[TAccumulate, T1, T2, TAccumulate], resultSelector: System.Func[TAccumulate, TResult], isDeterministic: System.Boolean, ) -> None:
        ...

    @typing.overload
    def CreateAggregate(self, name: System.String, seed: TAccumulate, func: System.Func[TAccumulate, T1, T2, T3, TAccumulate], resultSelector: System.Func[TAccumulate, TResult], isDeterministic: System.Boolean, ) -> None:
        ...

    @typing.overload
    def CreateAggregate(self, name: System.String, seed: TAccumulate, func: System.Func[TAccumulate, T1, T2, T3, T4, TAccumulate], resultSelector: System.Func[TAccumulate, TResult], isDeterministic: System.Boolean, ) -> None:
        ...

    @typing.overload
    def CreateAggregate(self, name: System.String, seed: TAccumulate, func: System.Func[TAccumulate, T1, T2, T3, T4, T5, TAccumulate], resultSelector: System.Func[TAccumulate, TResult], isDeterministic: System.Boolean, ) -> None:
        ...

    @typing.overload
    def CreateAggregate(self, name: System.String, seed: TAccumulate, func: System.Func[TAccumulate, T1, T2, T3, T4, T5, T6, TAccumulate], resultSelector: System.Func[TAccumulate, TResult], isDeterministic: System.Boolean, ) -> None:
        ...

    @typing.overload
    def CreateAggregate(self, name: System.String, seed: TAccumulate, func: System.Func[TAccumulate, T1, T2, T3, T4, T5, T6, T7, TAccumulate], resultSelector: System.Func[TAccumulate, TResult], isDeterministic: System.Boolean, ) -> None:
        ...

    @typing.overload
    def CreateAggregate(self, name: System.String, seed: TAccumulate, func: System.Func[TAccumulate, T1, T2, T3, T4, T5, T6, T7, T8, TAccumulate], resultSelector: System.Func[TAccumulate, TResult], isDeterministic: System.Boolean, ) -> None:
        ...

    @typing.overload
    def CreateAggregate(self, name: System.String, seed: TAccumulate, func: System.Func[TAccumulate, T1, T2, T3, T4, T5, T6, T7, T8, T9, TAccumulate], resultSelector: System.Func[TAccumulate, TResult], isDeterministic: System.Boolean, ) -> None:
        ...

    @typing.overload
    def CreateAggregate(self, name: System.String, seed: TAccumulate, func: System.Func[TAccumulate, T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, TAccumulate], resultSelector: System.Func[TAccumulate, TResult], isDeterministic: System.Boolean, ) -> None:
        ...

    @typing.overload
    def CreateAggregate(self, name: System.String, seed: TAccumulate, func: System.Func[TAccumulate, T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, TAccumulate], resultSelector: System.Func[TAccumulate, TResult], isDeterministic: System.Boolean, ) -> None:
        ...

    @typing.overload
    def CreateAggregate(self, name: System.String, seed: TAccumulate, func: System.Func[TAccumulate, T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, TAccumulate], resultSelector: System.Func[TAccumulate, TResult], isDeterministic: System.Boolean, ) -> None:
        ...

    @typing.overload
    def CreateAggregate(self, name: System.String, seed: TAccumulate, func: System.Func[TAccumulate, T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13, TAccumulate], resultSelector: System.Func[TAccumulate, TResult], isDeterministic: System.Boolean, ) -> None:
        ...

    @typing.overload
    def CreateAggregate(self, name: System.String, seed: TAccumulate, func: System.Func[TAccumulate, T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13, T14, TAccumulate], resultSelector: System.Func[TAccumulate, TResult], isDeterministic: System.Boolean, ) -> None:
        ...

    @typing.overload
    def CreateAggregate(self, name: System.String, seed: TAccumulate, func: System.Func[TAccumulate, T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13, T14, T15, TAccumulate], resultSelector: System.Func[TAccumulate, TResult], isDeterministic: System.Boolean, ) -> None:
        ...

    @typing.overload
    def CreateAggregate(self, name: System.String, seed: TAccumulate, func: System.Func[TAccumulate, list[System.Object], TAccumulate], resultSelector: System.Func[TAccumulate, TResult], isDeterministic: System.Boolean, ) -> None:
        ...

class SqliteTransaction(System.Data.IDbTransaction, System.IDisposable, System.IAsyncDisposable, System.Data.Common.DbTransaction):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def Connection(self) -> Microsoft.Data.Sqlite.SqliteConnection:
        ...

    @property
    def IsolationLevel(self) -> System.Data.IsolationLevel:
        ...

    @property
    def SupportsSavepoints(self) -> System.Boolean:
        ...

    @property
    def Connection(self) -> System.Data.Common.DbConnection:
        ...

    # methods
    @typing.overload
    def Commit(self, ) -> None:
        ...

    @typing.overload
    def Rollback(self, ) -> None:
        ...

    @typing.overload
    def Save(self, savepointName: System.String, ) -> None:
        ...

    @typing.overload
    def Rollback(self, savepointName: System.String, ) -> None:
        ...

    @typing.overload
    def Release(self, savepointName: System.String, ) -> None:
        ...

class SqliteParameterCollection(System.Data.IDataParameterCollection, System.Collections.IList, System.Collections.ICollection, System.Collections.IEnumerable, System.Data.Common.DbParameterCollection):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def Count(self) -> System.Int32:
        ...

    @property
    def SyncRoot(self) -> System.Object:
        ...

    @property
    def Item(self) -> Microsoft.Data.Sqlite.SqliteParameter:
        ...
    @Item.setter
    def Item(self, val: Microsoft.Data.Sqlite.SqliteParameter):
        ...

    @property
    def Item(self) -> Microsoft.Data.Sqlite.SqliteParameter:
        ...
    @Item.setter
    def Item(self, val: Microsoft.Data.Sqlite.SqliteParameter):
        ...

    @property
    def IsFixedSize(self) -> System.Boolean:
        ...

    @property
    def IsReadOnly(self) -> System.Boolean:
        ...

    @property
    def IsSynchronized(self) -> System.Boolean:
        ...

    @property
    def Item(self) -> System.Data.Common.DbParameter:
        ...
    @Item.setter
    def Item(self, val: System.Data.Common.DbParameter):
        ...

    @property
    def Item(self) -> System.Data.Common.DbParameter:
        ...
    @Item.setter
    def Item(self, val: System.Data.Common.DbParameter):
        ...

    # methods
    @typing.overload
    def Add(self, value: System.Object, ) -> System.Int32:
        ...

    @typing.overload
    def Add(self, value: Microsoft.Data.Sqlite.SqliteParameter, ) -> Microsoft.Data.Sqlite.SqliteParameter:
        ...

    @typing.overload
    def Add(self, parameterName: System.String, type: Microsoft.Data.Sqlite.SqliteType, ) -> Microsoft.Data.Sqlite.SqliteParameter:
        ...

    @typing.overload
    def Add(self, parameterName: System.String, type: Microsoft.Data.Sqlite.SqliteType, size: System.Int32, ) -> Microsoft.Data.Sqlite.SqliteParameter:
        ...

    @typing.overload
    def Add(self, parameterName: System.String, type: Microsoft.Data.Sqlite.SqliteType, size: System.Int32, sourceColumn: System.String, ) -> Microsoft.Data.Sqlite.SqliteParameter:
        ...

    @typing.overload
    def AddRange(self, values: System.Array, ) -> None:
        ...

    @typing.overload
    def AddRange(self, values: System.Collections.Generic.IEnumerable[Microsoft.Data.Sqlite.SqliteParameter], ) -> None:
        ...

    @typing.overload
    def AddWithValue(self, parameterName: System.String, value: System.Object, ) -> Microsoft.Data.Sqlite.SqliteParameter:
        ...

    @typing.overload
    def Clear(self, ) -> None:
        ...

    @typing.overload
    def Contains(self, value: System.Object, ) -> System.Boolean:
        ...

    @typing.overload
    def Contains(self, value: Microsoft.Data.Sqlite.SqliteParameter, ) -> System.Boolean:
        ...

    @typing.overload
    def Contains(self, value: System.String, ) -> System.Boolean:
        ...

    @typing.overload
    def CopyTo(self, array: System.Array, index: System.Int32, ) -> None:
        ...

    @typing.overload
    def CopyTo(self, array: list[Microsoft.Data.Sqlite.SqliteParameter], index: System.Int32, ) -> None:
        ...

    @typing.overload
    def GetEnumerator(self, ) -> System.Collections.IEnumerator:
        ...

    @typing.overload
    def IndexOf(self, value: System.Object, ) -> System.Int32:
        ...

    @typing.overload
    def IndexOf(self, value: Microsoft.Data.Sqlite.SqliteParameter, ) -> System.Int32:
        ...

    @typing.overload
    def IndexOf(self, parameterName: System.String, ) -> System.Int32:
        ...

    @typing.overload
    def Insert(self, index: System.Int32, value: System.Object, ) -> None:
        ...

    @typing.overload
    def Insert(self, index: System.Int32, value: Microsoft.Data.Sqlite.SqliteParameter, ) -> None:
        ...

    @typing.overload
    def Remove(self, value: System.Object, ) -> None:
        ...

    @typing.overload
    def Remove(self, value: Microsoft.Data.Sqlite.SqliteParameter, ) -> None:
        ...

    @typing.overload
    def RemoveAt(self, index: System.Int32, ) -> None:
        ...

    @typing.overload
    def RemoveAt(self, parameterName: System.String, ) -> None:
        ...

class SqliteParameter(System.Data.IDbDataParameter, System.Data.IDataParameter, System.Data.Common.DbParameter):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def DbType(self) -> System.Data.DbType:
        ...
    @DbType.setter
    def DbType(self, val: System.Data.DbType):
        ...

    @property
    def SqliteType(self) -> Microsoft.Data.Sqlite.SqliteType:
        ...
    @SqliteType.setter
    def SqliteType(self, val: Microsoft.Data.Sqlite.SqliteType):
        ...

    @property
    def Direction(self) -> System.Data.ParameterDirection:
        ...
    @Direction.setter
    def Direction(self, val: System.Data.ParameterDirection):
        ...

    @property
    def IsNullable(self) -> System.Boolean:
        ...
    @IsNullable.setter
    def IsNullable(self, val: System.Boolean):
        ...

    @property
    def ParameterName(self) -> System.String:
        ...
    @ParameterName.setter
    def ParameterName(self, val: System.String):
        ...

    @property
    def Size(self) -> System.Int32:
        ...
    @Size.setter
    def Size(self, val: System.Int32):
        ...

    @property
    def SourceColumn(self) -> System.String:
        ...
    @SourceColumn.setter
    def SourceColumn(self, val: System.String):
        ...

    @property
    def SourceColumnNullMapping(self) -> System.Boolean:
        ...
    @SourceColumnNullMapping.setter
    def SourceColumnNullMapping(self, val: System.Boolean):
        ...

    @property
    def Value(self) -> System.Object:
        ...
    @Value.setter
    def Value(self, val: System.Object):
        ...

    @property
    def Precision(self) -> System.Byte:
        ...
    @Precision.setter
    def Precision(self, val: System.Byte):
        ...

    @property
    def Scale(self) -> System.Byte:
        ...
    @Scale.setter
    def Scale(self, val: System.Byte):
        ...

    @property
    def SourceVersion(self) -> System.Data.DataRowVersion:
        ...
    @SourceVersion.setter
    def SourceVersion(self, val: System.Data.DataRowVersion):
        ...

    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def __init__(self, name: System.String, value: System.Object, ):
        ...

    @typing.overload
    def __init__(self, name: System.String, type: Microsoft.Data.Sqlite.SqliteType, ):
        ...

    @typing.overload
    def __init__(self, name: System.String, type: Microsoft.Data.Sqlite.SqliteType, size: System.Int32, ):
        ...

    @typing.overload
    def __init__(self, name: System.String, type: Microsoft.Data.Sqlite.SqliteType, size: System.Int32, sourceColumn: System.String, ):
        ...

    @typing.overload
    def ResetDbType(self, ) -> None:
        ...

    @typing.overload
    def ResetSqliteType(self, ) -> None:
        ...

