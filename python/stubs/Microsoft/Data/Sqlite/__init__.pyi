from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import System.Data
import System
import System.Collections
import System.Data.Common
import SQLitePCL
import Microsoft.Data.Sqlite
import System.Diagnostics
import System.Collections.Generic
import System.IO
import System.ComponentModel
import System.Threading.Tasks
import System.Threading

T = typing.TypeVar('T')
TState = typing.TypeVar('TState')
TResult = typing.TypeVar('TResult')
TAccumulate = typing.TypeVar('TAccumulate')
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
TEnum = typing.TypeVar('TEnum')

class SqliteDataReader(System.Data.IDataReader, System.IDisposable, System.Data.IDataRecord, System.Collections.IEnumerable, System.IAsyncDisposable, System.Data.Common.DbDataReader):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def Depth(self) -> int:
        ...

    @property
    def FieldCount(self) -> int:
        ...

    @property
    def Handle(self) -> SQLitePCL.sqlite3_stmt:
        ...

    @property
    def HasRows(self) -> bool:
        ...

    @property
    def IsClosed(self) -> bool:
        ...

    @property
    def RecordsAffected(self) -> int:
        ...

    @property
    def Item(self) -> System.Object:
        ...

    @property
    def Item(self) -> System.Object:
        ...

    @property
    def VisibleFieldCount(self) -> int:
        ...

    # methods
    def __init__(self, command: Microsoft.Data.Sqlite.SqliteCommand, timer: System.Diagnostics.Stopwatch, stmts: System.Collections.Generic.IEnumerable[SQLitePCL.sqlite3_stmt], closeConnection: bool, ):
        ...

    def GetEnumerator(self, ) -> System.Collections.IEnumerator:
        ...

    def Read(self, ) -> bool:
        ...

    def NextResult(self, ) -> bool:
        ...

    @staticmethod
    def IsBusy(rc: int, ) -> bool:
        ...

    def Close(self, ) -> None:
        ...

    def Dispose(self, disposing: bool, ) -> None:
        ...

    def GetName(self, ordinal: int, ) -> str:
        ...

    def GetOrdinal(self, name: str, ) -> int:
        ...

    def GetDataTypeName(self, ordinal: int, ) -> str:
        ...

    def GetFieldType(self, ordinal: int, ) -> System.Type:
        ...

    def IsDBNull(self, ordinal: int, ) -> bool:
        ...

    def GetBoolean(self, ordinal: int, ) -> bool:
        ...

    def GetByte(self, ordinal: int, ) -> int:
        ...

    def GetChar(self, ordinal: int, ) -> str:
        ...

    def GetDateTime(self, ordinal: int, ) -> System.DateTime:
        ...

    def GetDateTimeOffset(self, ordinal: int, ) -> System.DateTimeOffset:
        ...

    def GetTimeSpan(self, ordinal: int, ) -> System.TimeSpan:
        ...

    def GetDecimal(self, ordinal: int, ) -> System.Decimal:
        ...

    def GetDouble(self, ordinal: int, ) -> float:
        ...

    def GetFloat(self, ordinal: int, ) -> float:
        ...

    def GetGuid(self, ordinal: int, ) -> System.Guid:
        ...

    def GetInt16(self, ordinal: int, ) -> int:
        ...

    def GetInt32(self, ordinal: int, ) -> int:
        ...

    def GetInt64(self, ordinal: int, ) -> int:
        ...

    def GetString(self, ordinal: int, ) -> str:
        ...

    def GetBytes(self, ordinal: int, dataOffset: int, buffer: System.Array[int], bufferOffset: int, length: int, ) -> int:
        ...

    def GetChars(self, ordinal: int, dataOffset: int, buffer: System.Array[str], bufferOffset: int, length: int, ) -> int:
        ...

    def GetStream(self, ordinal: int, ) -> System.IO.Stream:
        ...

    def GetTextReader(self, ordinal: int, ) -> System.IO.TextReader:
        ...

    def GetFieldValue(self, ordinal: int, ) -> T:
        ...

    def GetValue(self, ordinal: int, ) -> System.Object:
        ...

    def GetValues(self, values: System.Array[System.Object], ) -> int:
        ...

    def GetSchemaTable(self, ) -> System.Data.DataTable:
        ...

class SqliteType(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    Integer: int = ...
    Real: int = ...
    Text: int = ...
    Blob: int = ...

class SqliteCommand(System.ComponentModel.IComponent, System.IDisposable, System.Data.IDbCommand, System.IAsyncDisposable, System.Data.Common.DbCommand):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def CommandType(self) -> int:
        ...
    @CommandType.setter
    def CommandType(self, val: int):
        ...

    @property
    def CommandText(self) -> str:
        ...
    @CommandText.setter
    def CommandText(self, val: str):
        ...

    @property
    def Connection(self) -> Microsoft.Data.Sqlite.SqliteConnection:
        ...
    @Connection.setter
    def Connection(self, val: Microsoft.Data.Sqlite.SqliteConnection):
        ...

    @property
    def DbConnection(self) -> System.Data.Common.DbConnection:
        ...
    @DbConnection.setter
    def DbConnection(self, val: System.Data.Common.DbConnection):
        ...

    @property
    def Transaction(self) -> Microsoft.Data.Sqlite.SqliteTransaction:
        ...
    @Transaction.setter
    def Transaction(self, val: Microsoft.Data.Sqlite.SqliteTransaction):
        ...

    @property
    def DbTransaction(self) -> System.Data.Common.DbTransaction:
        ...
    @DbTransaction.setter
    def DbTransaction(self, val: System.Data.Common.DbTransaction):
        ...

    @property
    def Parameters(self) -> Microsoft.Data.Sqlite.SqliteParameterCollection:
        ...

    @property
    def DbParameterCollection(self) -> System.Data.Common.DbParameterCollection:
        ...

    @property
    def CommandTimeout(self) -> int:
        ...
    @CommandTimeout.setter
    def CommandTimeout(self, val: int):
        ...

    @property
    def DesignTimeVisible(self) -> bool:
        ...
    @DesignTimeVisible.setter
    def DesignTimeVisible(self, val: bool):
        ...

    @property
    def UpdatedRowSource(self) -> int:
        ...
    @UpdatedRowSource.setter
    def UpdatedRowSource(self, val: int):
        ...

    @property
    def DataReader(self) -> Microsoft.Data.Sqlite.SqliteDataReader:
        ...
    @DataReader.setter
    def DataReader(self, val: Microsoft.Data.Sqlite.SqliteDataReader):
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
    def CanRaiseEvents(self) -> bool:
        ...

    @property
    def CanRaiseEventsInternal(self) -> bool:
        ...

    @property
    def Events(self) -> System.ComponentModel.EventHandlerList:
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

    @property
    def DesignMode(self) -> bool:
        ...

    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def __init__(self, commandText: str, ):
        ...

    @typing.overload
    def __init__(self, commandText: str, connection: Microsoft.Data.Sqlite.SqliteConnection, ):
        ...

    @typing.overload
    def __init__(self, commandText: str, connection: Microsoft.Data.Sqlite.SqliteConnection, transaction: Microsoft.Data.Sqlite.SqliteTransaction, ):
        ...

    def Dispose(self, disposing: bool, ) -> None:
        ...

    def CreateParameter(self, ) -> Microsoft.Data.Sqlite.SqliteParameter:
        ...

    def CreateDbParameter(self, ) -> System.Data.Common.DbParameter:
        ...

    def Prepare(self, ) -> None:
        ...

    @typing.overload
    def ExecuteReader(self, ) -> Microsoft.Data.Sqlite.SqliteDataReader:
        ...

    @typing.overload
    def ExecuteReader(self, behavior: int, ) -> Microsoft.Data.Sqlite.SqliteDataReader:
        ...

    def GetStatements(self, timer: System.Diagnostics.Stopwatch, ) -> System.Collections.Generic.IEnumerable[SQLitePCL.sqlite3_stmt]:
        ...

    def ExecuteDbDataReader(self, behavior: int, ) -> System.Data.Common.DbDataReader:
        ...

    @typing.overload
    def ExecuteReaderAsync(self, ) -> System.Threading.Tasks.Task[Microsoft.Data.Sqlite.SqliteDataReader]:
        ...

    @typing.overload
    def ExecuteReaderAsync(self, cancellationToken: System.Threading.CancellationToken, ) -> System.Threading.Tasks.Task[Microsoft.Data.Sqlite.SqliteDataReader]:
        ...

    @typing.overload
    def ExecuteReaderAsync(self, behavior: int, ) -> System.Threading.Tasks.Task[Microsoft.Data.Sqlite.SqliteDataReader]:
        ...

    @typing.overload
    def ExecuteReaderAsync(self, behavior: int, cancellationToken: System.Threading.CancellationToken, ) -> System.Threading.Tasks.Task[Microsoft.Data.Sqlite.SqliteDataReader]:
        ...

    def ExecuteDbDataReaderAsync(self, behavior: int, cancellationToken: System.Threading.CancellationToken, ) -> System.Threading.Tasks.Task[System.Data.Common.DbDataReader]:
        ...

    def ExecuteNonQuery(self, ) -> int:
        ...

    def ExecuteScalar(self, ) -> System.Object:
        ...

    def Cancel(self, ) -> None:
        ...

    def PrepareAndEnumerateStatements(self, timer: System.Diagnostics.Stopwatch, ) -> System.Collections.Generic.IEnumerable[SQLitePCL.sqlite3_stmt]:
        ...

    def DisposePreparedStatements(self, disposing: bool = ..., ) -> None:
        ...

    @staticmethod
    def IsBusy(rc: int, ) -> bool:
        ...

class SqliteConnection(System.ComponentModel.IComponent, System.IDisposable, System.Data.IDbConnection, System.IAsyncDisposable, System.Data.Common.DbConnection):
    @typing.overload
    def __init__(self, **kwargs):
        self._suppressStateChangeForReconnection: bool
        ...

    # static fields
    MainDatabaseName: str = ...

    # properties
    @property
    def Handle(self) -> SQLitePCL.sqlite3:
        ...

    @property
    def ConnectionString(self) -> str:
        ...
    @ConnectionString.setter
    def ConnectionString(self, val: str):
        ...

    @property
    def PoolGroup(self) -> Microsoft.Data.Sqlite.SqliteConnectionPoolGroup:
        ...
    @PoolGroup.setter
    def PoolGroup(self, val: Microsoft.Data.Sqlite.SqliteConnectionPoolGroup):
        ...

    @property
    def ConnectionOptions(self) -> Microsoft.Data.Sqlite.SqliteConnectionStringBuilder:
        ...

    @property
    def Database(self) -> str:
        ...

    @property
    def DataSource(self) -> str:
        ...

    @property
    def DefaultTimeout(self) -> int:
        ...
    @DefaultTimeout.setter
    def DefaultTimeout(self, val: int):
        ...

    @property
    def ServerVersion(self) -> str:
        ...

    @property
    def State(self) -> int:
        ...

    @property
    def DbProviderFactory(self) -> System.Data.Common.DbProviderFactory:
        ...

    @property
    def Transaction(self) -> Microsoft.Data.Sqlite.SqliteTransaction:
        ...
    @Transaction.setter
    def Transaction(self, val: Microsoft.Data.Sqlite.SqliteTransaction):
        ...

    @property
    def ConnectionTimeout(self) -> int:
        ...

    @property
    def ProviderFactory(self) -> System.Data.Common.DbProviderFactory:
        ...

    @property
    def CanCreateBatch(self) -> bool:
        ...

    @property
    def CanRaiseEvents(self) -> bool:
        ...

    @property
    def CanRaiseEventsInternal(self) -> bool:
        ...

    @property
    def Events(self) -> System.ComponentModel.EventHandlerList:
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

    @property
    def DesignMode(self) -> bool:
        ...

    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def __init__(self, connectionString: str, ):
        ...

    @typing.overload
    def BeginTransaction(self, isolationLevel: int, deferred: bool, ) -> Microsoft.Data.Sqlite.SqliteTransaction:
        ...

    @typing.overload
    def BeginTransaction(self, ) -> Microsoft.Data.Sqlite.SqliteTransaction:
        ...

    @typing.overload
    def BeginTransaction(self, deferred: bool, ) -> Microsoft.Data.Sqlite.SqliteTransaction:
        ...

    @typing.overload
    def BeginTransaction(self, isolationLevel: int, ) -> Microsoft.Data.Sqlite.SqliteTransaction:
        ...

    def ChangeDatabase(self, databaseName: str, ) -> None:
        ...

    def EnableExtensions(self, enable: bool = ..., ) -> None:
        ...

    def LoadExtension(self, file: str, proc: str = ..., ) -> None:
        ...

    def LoadExtensionCore(self, file: str, proc: str, ) -> None:
        ...

    @typing.overload
    def BackupDatabase(self, destination: Microsoft.Data.Sqlite.SqliteConnection, ) -> None:
        ...

    @typing.overload
    def BackupDatabase(self, destination: Microsoft.Data.Sqlite.SqliteConnection, destinationName: str, sourceName: str, ) -> None:
        ...

    @typing.overload
    def GetSchema(self, ) -> System.Data.DataTable:
        ...

    @typing.overload
    def GetSchema(self, collectionName: str, ) -> System.Data.DataTable:
        ...

    @typing.overload
    def GetSchema(self, collectionName: str, restrictionValues: System.Array[str], ) -> System.Data.DataTable:
        ...

    def CreateFunctionCore(self, name: str, arity: int, state: TState, function: System.Func[TState, Microsoft.Data.Sqlite.SqliteValueReader, TResult], isDeterministic: bool, ) -> None:
        ...

    def CreateAggregateCore(self, name: str, arity: int, seed: TAccumulate, func: System.Func[TAccumulate, Microsoft.Data.Sqlite.SqliteValueReader, TAccumulate], resultSelector: System.Func[TAccumulate, TResult], isDeterministic: bool, ) -> None:
        ...

    @staticmethod
    def IfNotNull(x: System.Object, value: System.Func[TState, Microsoft.Data.Sqlite.SqliteValueReader, TResult], ) -> System.Func[TState, Microsoft.Data.Sqlite.SqliteValueReader, TResult]:
        ...

    @staticmethod
    def GetValues(reader: Microsoft.Data.Sqlite.SqliteValueReader, ) -> System.Array[System.Object]:
        ...

    @typing.overload
    def CreateFunction(self, name: str, function: System.Func[TResult], isDeterministic: bool = ..., ) -> None:
        ...

    @typing.overload
    def CreateFunction(self, name: str, function: System.Func[T1, TResult], isDeterministic: bool = ..., ) -> None:
        ...

    @typing.overload
    def CreateFunction(self, name: str, function: System.Func[T1, T2, TResult], isDeterministic: bool = ..., ) -> None:
        ...

    @typing.overload
    def CreateFunction(self, name: str, function: System.Func[T1, T2, T3, TResult], isDeterministic: bool = ..., ) -> None:
        ...

    @typing.overload
    def CreateFunction(self, name: str, function: System.Func[T1, T2, T3, T4, TResult], isDeterministic: bool = ..., ) -> None:
        ...

    @typing.overload
    def CreateFunction(self, name: str, function: System.Func[T1, T2, T3, T4, T5, TResult], isDeterministic: bool = ..., ) -> None:
        ...

    @typing.overload
    def CreateFunction(self, name: str, function: System.Func[T1, T2, T3, T4, T5, T6, TResult], isDeterministic: bool = ..., ) -> None:
        ...

    @typing.overload
    def CreateFunction(self, name: str, function: System.Func[T1, T2, T3, T4, T5, T6, T7, TResult], isDeterministic: bool = ..., ) -> None:
        ...

    @typing.overload
    def CreateFunction(self, name: str, function: System.Func[T1, T2, T3, T4, T5, T6, T7, T8, TResult], isDeterministic: bool = ..., ) -> None:
        ...

    @typing.overload
    def CreateFunction(self, name: str, function: System.Func[T1, T2, T3, T4, T5, T6, T7, T8, T9, TResult], isDeterministic: bool = ..., ) -> None:
        ...

    @typing.overload
    def CreateFunction(self, name: str, function: System.Func[T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, TResult], isDeterministic: bool = ..., ) -> None:
        ...

    @typing.overload
    def CreateFunction(self, name: str, function: System.Func[T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, TResult], isDeterministic: bool = ..., ) -> None:
        ...

    @typing.overload
    def CreateFunction(self, name: str, function: System.Func[T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, TResult], isDeterministic: bool = ..., ) -> None:
        ...

    @typing.overload
    def CreateFunction(self, name: str, function: System.Func[T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13, TResult], isDeterministic: bool = ..., ) -> None:
        ...

    @typing.overload
    def CreateFunction(self, name: str, function: System.Func[T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13, T14, TResult], isDeterministic: bool = ..., ) -> None:
        ...

    @typing.overload
    def CreateFunction(self, name: str, function: System.Func[T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13, T14, T15, TResult], isDeterministic: bool = ..., ) -> None:
        ...

    @typing.overload
    def CreateFunction(self, name: str, function: System.Func[T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13, T14, T15, T16, TResult], isDeterministic: bool = ..., ) -> None:
        ...

    @typing.overload
    def CreateFunction(self, name: str, function: System.Func[System.Array[System.Object], TResult], isDeterministic: bool = ..., ) -> None:
        ...

    @typing.overload
    def CreateFunction(self, name: str, state: TState, function: System.Func[TState, TResult], isDeterministic: bool = ..., ) -> None:
        ...

    @typing.overload
    def CreateFunction(self, name: str, state: TState, function: System.Func[TState, T1, TResult], isDeterministic: bool = ..., ) -> None:
        ...

    @typing.overload
    def CreateFunction(self, name: str, state: TState, function: System.Func[TState, T1, T2, TResult], isDeterministic: bool = ..., ) -> None:
        ...

    @typing.overload
    def CreateFunction(self, name: str, state: TState, function: System.Func[TState, T1, T2, T3, TResult], isDeterministic: bool = ..., ) -> None:
        ...

    @typing.overload
    def CreateFunction(self, name: str, state: TState, function: System.Func[TState, T1, T2, T3, T4, TResult], isDeterministic: bool = ..., ) -> None:
        ...

    @typing.overload
    def CreateFunction(self, name: str, state: TState, function: System.Func[TState, T1, T2, T3, T4, T5, TResult], isDeterministic: bool = ..., ) -> None:
        ...

    @typing.overload
    def CreateFunction(self, name: str, state: TState, function: System.Func[TState, T1, T2, T3, T4, T5, T6, TResult], isDeterministic: bool = ..., ) -> None:
        ...

    @typing.overload
    def CreateFunction(self, name: str, state: TState, function: System.Func[TState, T1, T2, T3, T4, T5, T6, T7, TResult], isDeterministic: bool = ..., ) -> None:
        ...

    @typing.overload
    def CreateFunction(self, name: str, state: TState, function: System.Func[TState, T1, T2, T3, T4, T5, T6, T7, T8, TResult], isDeterministic: bool = ..., ) -> None:
        ...

    @typing.overload
    def CreateFunction(self, name: str, state: TState, function: System.Func[TState, T1, T2, T3, T4, T5, T6, T7, T8, T9, TResult], isDeterministic: bool = ..., ) -> None:
        ...

    @typing.overload
    def CreateFunction(self, name: str, state: TState, function: System.Func[TState, T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, TResult], isDeterministic: bool = ..., ) -> None:
        ...

    @typing.overload
    def CreateFunction(self, name: str, state: TState, function: System.Func[TState, T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, TResult], isDeterministic: bool = ..., ) -> None:
        ...

    @typing.overload
    def CreateFunction(self, name: str, state: TState, function: System.Func[TState, T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, TResult], isDeterministic: bool = ..., ) -> None:
        ...

    @typing.overload
    def CreateFunction(self, name: str, state: TState, function: System.Func[TState, T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13, TResult], isDeterministic: bool = ..., ) -> None:
        ...

    @typing.overload
    def CreateFunction(self, name: str, state: TState, function: System.Func[TState, T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13, T14, TResult], isDeterministic: bool = ..., ) -> None:
        ...

    @typing.overload
    def CreateFunction(self, name: str, state: TState, function: System.Func[TState, T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13, T14, T15, TResult], isDeterministic: bool = ..., ) -> None:
        ...

    @typing.overload
    def CreateFunction(self, name: str, state: TState, function: System.Func[TState, System.Array[System.Object], TResult], isDeterministic: bool = ..., ) -> None:
        ...

    @staticmethod
    def ClearAllPools() -> None:
        ...

    @staticmethod
    def ClearPool(connection: Microsoft.Data.Sqlite.SqliteConnection, ) -> None:
        ...

    def Open(self, ) -> None:
        ...

    def Close(self, ) -> None:
        ...

    def Deactivate(self, ) -> None:
        ...

    def Dispose(self, disposing: bool, ) -> None:
        ...

    def CreateCommand(self, ) -> Microsoft.Data.Sqlite.SqliteCommand:
        ...

    def CreateDbCommand(self, ) -> System.Data.Common.DbCommand:
        ...

    def AddCommand(self, command: Microsoft.Data.Sqlite.SqliteCommand, ) -> None:
        ...

    def RemoveCommand(self, command: Microsoft.Data.Sqlite.SqliteCommand, ) -> None:
        ...

    @typing.overload
    def CreateCollation(self, name: str, comparison: System.Comparison[str], ) -> None:
        ...

    @typing.overload
    def CreateCollation(self, name: str, state: T, comparison: System.Func[T, str, str, int], ) -> None:
        ...

    def BeginDbTransaction(self, isolationLevel: int, ) -> System.Data.Common.DbTransaction:
        ...

    @typing.overload
    def CreateAggregate(self, name: str, func: System.Func[TAccumulate, TAccumulate], isDeterministic: bool = ..., ) -> None:
        ...

    @typing.overload
    def CreateAggregate(self, name: str, func: System.Func[TAccumulate, T1, TAccumulate], isDeterministic: bool = ..., ) -> None:
        ...

    @typing.overload
    def CreateAggregate(self, name: str, func: System.Func[TAccumulate, T1, T2, TAccumulate], isDeterministic: bool = ..., ) -> None:
        ...

    @typing.overload
    def CreateAggregate(self, name: str, func: System.Func[TAccumulate, T1, T2, T3, TAccumulate], isDeterministic: bool = ..., ) -> None:
        ...

    @typing.overload
    def CreateAggregate(self, name: str, func: System.Func[TAccumulate, T1, T2, T3, T4, TAccumulate], isDeterministic: bool = ..., ) -> None:
        ...

    @typing.overload
    def CreateAggregate(self, name: str, func: System.Func[TAccumulate, T1, T2, T3, T4, T5, TAccumulate], isDeterministic: bool = ..., ) -> None:
        ...

    @typing.overload
    def CreateAggregate(self, name: str, func: System.Func[TAccumulate, T1, T2, T3, T4, T5, T6, TAccumulate], isDeterministic: bool = ..., ) -> None:
        ...

    @typing.overload
    def CreateAggregate(self, name: str, func: System.Func[TAccumulate, T1, T2, T3, T4, T5, T6, T7, TAccumulate], isDeterministic: bool = ..., ) -> None:
        ...

    @typing.overload
    def CreateAggregate(self, name: str, func: System.Func[TAccumulate, T1, T2, T3, T4, T5, T6, T7, T8, TAccumulate], isDeterministic: bool = ..., ) -> None:
        ...

    @typing.overload
    def CreateAggregate(self, name: str, func: System.Func[TAccumulate, T1, T2, T3, T4, T5, T6, T7, T8, T9, TAccumulate], isDeterministic: bool = ..., ) -> None:
        ...

    @typing.overload
    def CreateAggregate(self, name: str, func: System.Func[TAccumulate, T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, TAccumulate], isDeterministic: bool = ..., ) -> None:
        ...

    @typing.overload
    def CreateAggregate(self, name: str, func: System.Func[TAccumulate, T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, TAccumulate], isDeterministic: bool = ..., ) -> None:
        ...

    @typing.overload
    def CreateAggregate(self, name: str, func: System.Func[TAccumulate, T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, TAccumulate], isDeterministic: bool = ..., ) -> None:
        ...

    @typing.overload
    def CreateAggregate(self, name: str, func: System.Func[TAccumulate, T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13, TAccumulate], isDeterministic: bool = ..., ) -> None:
        ...

    @typing.overload
    def CreateAggregate(self, name: str, func: System.Func[TAccumulate, T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13, T14, TAccumulate], isDeterministic: bool = ..., ) -> None:
        ...

    @typing.overload
    def CreateAggregate(self, name: str, func: System.Func[TAccumulate, T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13, T14, T15, TAccumulate], isDeterministic: bool = ..., ) -> None:
        ...

    @typing.overload
    def CreateAggregate(self, name: str, func: System.Func[TAccumulate, System.Array[System.Object], TAccumulate], isDeterministic: bool = ..., ) -> None:
        ...

    @typing.overload
    def CreateAggregate(self, name: str, seed: TAccumulate, func: System.Func[TAccumulate, TAccumulate], isDeterministic: bool = ..., ) -> None:
        ...

    @typing.overload
    def CreateAggregate(self, name: str, seed: TAccumulate, func: System.Func[TAccumulate, T1, TAccumulate], isDeterministic: bool = ..., ) -> None:
        ...

    @typing.overload
    def CreateAggregate(self, name: str, seed: TAccumulate, func: System.Func[TAccumulate, T1, T2, TAccumulate], isDeterministic: bool = ..., ) -> None:
        ...

    @typing.overload
    def CreateAggregate(self, name: str, seed: TAccumulate, func: System.Func[TAccumulate, T1, T2, T3, TAccumulate], isDeterministic: bool = ..., ) -> None:
        ...

    @typing.overload
    def CreateAggregate(self, name: str, seed: TAccumulate, func: System.Func[TAccumulate, T1, T2, T3, T4, TAccumulate], isDeterministic: bool = ..., ) -> None:
        ...

    @typing.overload
    def CreateAggregate(self, name: str, seed: TAccumulate, func: System.Func[TAccumulate, T1, T2, T3, T4, T5, TAccumulate], isDeterministic: bool = ..., ) -> None:
        ...

    @typing.overload
    def CreateAggregate(self, name: str, seed: TAccumulate, func: System.Func[TAccumulate, T1, T2, T3, T4, T5, T6, TAccumulate], isDeterministic: bool = ..., ) -> None:
        ...

    @typing.overload
    def CreateAggregate(self, name: str, seed: TAccumulate, func: System.Func[TAccumulate, T1, T2, T3, T4, T5, T6, T7, TAccumulate], isDeterministic: bool = ..., ) -> None:
        ...

    @typing.overload
    def CreateAggregate(self, name: str, seed: TAccumulate, func: System.Func[TAccumulate, T1, T2, T3, T4, T5, T6, T7, T8, TAccumulate], isDeterministic: bool = ..., ) -> None:
        ...

    @typing.overload
    def CreateAggregate(self, name: str, seed: TAccumulate, func: System.Func[TAccumulate, T1, T2, T3, T4, T5, T6, T7, T8, T9, TAccumulate], isDeterministic: bool = ..., ) -> None:
        ...

    @typing.overload
    def CreateAggregate(self, name: str, seed: TAccumulate, func: System.Func[TAccumulate, T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, TAccumulate], isDeterministic: bool = ..., ) -> None:
        ...

    @typing.overload
    def CreateAggregate(self, name: str, seed: TAccumulate, func: System.Func[TAccumulate, T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, TAccumulate], isDeterministic: bool = ..., ) -> None:
        ...

    @typing.overload
    def CreateAggregate(self, name: str, seed: TAccumulate, func: System.Func[TAccumulate, T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, TAccumulate], isDeterministic: bool = ..., ) -> None:
        ...

    @typing.overload
    def CreateAggregate(self, name: str, seed: TAccumulate, func: System.Func[TAccumulate, T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13, TAccumulate], isDeterministic: bool = ..., ) -> None:
        ...

    @typing.overload
    def CreateAggregate(self, name: str, seed: TAccumulate, func: System.Func[TAccumulate, T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13, T14, TAccumulate], isDeterministic: bool = ..., ) -> None:
        ...

    @typing.overload
    def CreateAggregate(self, name: str, seed: TAccumulate, func: System.Func[TAccumulate, T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13, T14, T15, TAccumulate], isDeterministic: bool = ..., ) -> None:
        ...

    @typing.overload
    def CreateAggregate(self, name: str, seed: TAccumulate, func: System.Func[TAccumulate, System.Array[System.Object], TAccumulate], isDeterministic: bool = ..., ) -> None:
        ...

    @typing.overload
    def CreateAggregate(self, name: str, seed: TAccumulate, func: System.Func[TAccumulate, TAccumulate], resultSelector: System.Func[TAccumulate, TResult], isDeterministic: bool = ..., ) -> None:
        ...

    @typing.overload
    def CreateAggregate(self, name: str, seed: TAccumulate, func: System.Func[TAccumulate, T1, TAccumulate], resultSelector: System.Func[TAccumulate, TResult], isDeterministic: bool = ..., ) -> None:
        ...

    @typing.overload
    def CreateAggregate(self, name: str, seed: TAccumulate, func: System.Func[TAccumulate, T1, T2, TAccumulate], resultSelector: System.Func[TAccumulate, TResult], isDeterministic: bool = ..., ) -> None:
        ...

    @typing.overload
    def CreateAggregate(self, name: str, seed: TAccumulate, func: System.Func[TAccumulate, T1, T2, T3, TAccumulate], resultSelector: System.Func[TAccumulate, TResult], isDeterministic: bool = ..., ) -> None:
        ...

    @typing.overload
    def CreateAggregate(self, name: str, seed: TAccumulate, func: System.Func[TAccumulate, T1, T2, T3, T4, TAccumulate], resultSelector: System.Func[TAccumulate, TResult], isDeterministic: bool = ..., ) -> None:
        ...

    @typing.overload
    def CreateAggregate(self, name: str, seed: TAccumulate, func: System.Func[TAccumulate, T1, T2, T3, T4, T5, TAccumulate], resultSelector: System.Func[TAccumulate, TResult], isDeterministic: bool = ..., ) -> None:
        ...

    @typing.overload
    def CreateAggregate(self, name: str, seed: TAccumulate, func: System.Func[TAccumulate, T1, T2, T3, T4, T5, T6, TAccumulate], resultSelector: System.Func[TAccumulate, TResult], isDeterministic: bool = ..., ) -> None:
        ...

    @typing.overload
    def CreateAggregate(self, name: str, seed: TAccumulate, func: System.Func[TAccumulate, T1, T2, T3, T4, T5, T6, T7, TAccumulate], resultSelector: System.Func[TAccumulate, TResult], isDeterministic: bool = ..., ) -> None:
        ...

    @typing.overload
    def CreateAggregate(self, name: str, seed: TAccumulate, func: System.Func[TAccumulate, T1, T2, T3, T4, T5, T6, T7, T8, TAccumulate], resultSelector: System.Func[TAccumulate, TResult], isDeterministic: bool = ..., ) -> None:
        ...

    @typing.overload
    def CreateAggregate(self, name: str, seed: TAccumulate, func: System.Func[TAccumulate, T1, T2, T3, T4, T5, T6, T7, T8, T9, TAccumulate], resultSelector: System.Func[TAccumulate, TResult], isDeterministic: bool = ..., ) -> None:
        ...

    @typing.overload
    def CreateAggregate(self, name: str, seed: TAccumulate, func: System.Func[TAccumulate, T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, TAccumulate], resultSelector: System.Func[TAccumulate, TResult], isDeterministic: bool = ..., ) -> None:
        ...

    @typing.overload
    def CreateAggregate(self, name: str, seed: TAccumulate, func: System.Func[TAccumulate, T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, TAccumulate], resultSelector: System.Func[TAccumulate, TResult], isDeterministic: bool = ..., ) -> None:
        ...

    @typing.overload
    def CreateAggregate(self, name: str, seed: TAccumulate, func: System.Func[TAccumulate, T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, TAccumulate], resultSelector: System.Func[TAccumulate, TResult], isDeterministic: bool = ..., ) -> None:
        ...

    @typing.overload
    def CreateAggregate(self, name: str, seed: TAccumulate, func: System.Func[TAccumulate, T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13, TAccumulate], resultSelector: System.Func[TAccumulate, TResult], isDeterministic: bool = ..., ) -> None:
        ...

    @typing.overload
    def CreateAggregate(self, name: str, seed: TAccumulate, func: System.Func[TAccumulate, T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13, T14, TAccumulate], resultSelector: System.Func[TAccumulate, TResult], isDeterministic: bool = ..., ) -> None:
        ...

    @typing.overload
    def CreateAggregate(self, name: str, seed: TAccumulate, func: System.Func[TAccumulate, T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13, T14, T15, TAccumulate], resultSelector: System.Func[TAccumulate, TResult], isDeterministic: bool = ..., ) -> None:
        ...

    @typing.overload
    def CreateAggregate(self, name: str, seed: TAccumulate, func: System.Func[TAccumulate, System.Array[System.Object], TAccumulate], resultSelector: System.Func[TAccumulate, TResult], isDeterministic: bool = ..., ) -> None:
        ...

class SqliteParameter(System.Data.IDbDataParameter, System.Data.IDataParameter, System.Data.Common.DbParameter):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def DbType(self) -> int:
        ...
    @DbType.setter
    def DbType(self, val: int):
        ...

    @property
    def SqliteType(self) -> int:
        ...
    @SqliteType.setter
    def SqliteType(self, val: int):
        ...

    @property
    def Direction(self) -> int:
        ...
    @Direction.setter
    def Direction(self, val: int):
        ...

    @property
    def IsNullable(self) -> bool:
        ...
    @IsNullable.setter
    def IsNullable(self, val: bool):
        ...

    @property
    def ParameterName(self) -> str:
        ...
    @ParameterName.setter
    def ParameterName(self, val: str):
        ...

    @property
    def Size(self) -> int:
        ...
    @Size.setter
    def Size(self, val: int):
        ...

    @property
    def SourceColumn(self) -> str:
        ...
    @SourceColumn.setter
    def SourceColumn(self, val: str):
        ...

    @property
    def SourceColumnNullMapping(self) -> bool:
        ...
    @SourceColumnNullMapping.setter
    def SourceColumnNullMapping(self, val: bool):
        ...

    @property
    def Value(self) -> System.Object:
        ...
    @Value.setter
    def Value(self, val: System.Object):
        ...

    @property
    def Precision(self) -> int:
        ...
    @Precision.setter
    def Precision(self, val: int):
        ...

    @property
    def Scale(self) -> int:
        ...
    @Scale.setter
    def Scale(self, val: int):
        ...

    @property
    def SourceVersion(self) -> int:
        ...
    @SourceVersion.setter
    def SourceVersion(self, val: int):
        ...

    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def __init__(self, name: str, value: System.Object, ):
        ...

    @typing.overload
    def __init__(self, name: str, type: int, ):
        ...

    @typing.overload
    def __init__(self, name: str, type: int, size: int, ):
        ...

    @typing.overload
    def __init__(self, name: str, type: int, size: int, sourceColumn: str, ):
        ...

    def ResetDbType(self, ) -> None:
        ...

    def ResetSqliteType(self, ) -> None:
        ...

    def Bind(self, stmt: SQLitePCL.sqlite3_stmt, ) -> bool:
        ...

    def FindPrefixedParameter(self, stmt: SQLitePCL.sqlite3_stmt, ) -> int:
        ...

class SqliteParameterCollection(System.Data.IDataParameterCollection, System.Collections.IList, System.Collections.ICollection, System.Collections.IEnumerable, System.Data.Common.DbParameterCollection):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def Count(self) -> int:
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
    def IsFixedSize(self) -> bool:
        ...

    @property
    def IsReadOnly(self) -> bool:
        ...

    @property
    def IsSynchronized(self) -> bool:
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
    def __init__(self, ):
        ...

    @typing.overload
    def Add(self, value: System.Object, ) -> int:
        ...

    @typing.overload
    def Add(self, value: Microsoft.Data.Sqlite.SqliteParameter, ) -> Microsoft.Data.Sqlite.SqliteParameter:
        ...

    @typing.overload
    def Add(self, parameterName: str, type: int, ) -> Microsoft.Data.Sqlite.SqliteParameter:
        ...

    @typing.overload
    def Add(self, parameterName: str, type: int, size: int, ) -> Microsoft.Data.Sqlite.SqliteParameter:
        ...

    @typing.overload
    def Add(self, parameterName: str, type: int, size: int, sourceColumn: str, ) -> Microsoft.Data.Sqlite.SqliteParameter:
        ...

    @typing.overload
    def AddRange(self, values: System.Array, ) -> None:
        ...

    @typing.overload
    def AddRange(self, values: System.Collections.Generic.IEnumerable[Microsoft.Data.Sqlite.SqliteParameter], ) -> None:
        ...

    def AddWithValue(self, parameterName: str, value: System.Object, ) -> Microsoft.Data.Sqlite.SqliteParameter:
        ...

    def Clear(self, ) -> None:
        ...

    @typing.overload
    def Contains(self, value: System.Object, ) -> bool:
        ...

    @typing.overload
    def Contains(self, value: Microsoft.Data.Sqlite.SqliteParameter, ) -> bool:
        ...

    @typing.overload
    def Contains(self, value: str, ) -> bool:
        ...

    @typing.overload
    def CopyTo(self, array: System.Array, index: int, ) -> None:
        ...

    @typing.overload
    def CopyTo(self, array: System.Array[Microsoft.Data.Sqlite.SqliteParameter], index: int, ) -> None:
        ...

    def GetEnumerator(self, ) -> System.Collections.IEnumerator:
        ...

    @typing.overload
    def GetParameter(self, index: int, ) -> System.Data.Common.DbParameter:
        ...

    @typing.overload
    def GetParameter(self, parameterName: str, ) -> System.Data.Common.DbParameter:
        ...

    @typing.overload
    def IndexOf(self, value: System.Object, ) -> int:
        ...

    @typing.overload
    def IndexOf(self, value: Microsoft.Data.Sqlite.SqliteParameter, ) -> int:
        ...

    @typing.overload
    def IndexOf(self, parameterName: str, ) -> int:
        ...

    @typing.overload
    def Insert(self, index: int, value: System.Object, ) -> None:
        ...

    @typing.overload
    def Insert(self, index: int, value: Microsoft.Data.Sqlite.SqliteParameter, ) -> None:
        ...

    @typing.overload
    def Remove(self, value: System.Object, ) -> None:
        ...

    @typing.overload
    def Remove(self, value: Microsoft.Data.Sqlite.SqliteParameter, ) -> None:
        ...

    @typing.overload
    def RemoveAt(self, index: int, ) -> None:
        ...

    @typing.overload
    def RemoveAt(self, parameterName: str, ) -> None:
        ...

    @typing.overload
    def SetParameter(self, index: int, value: System.Data.Common.DbParameter, ) -> None:
        ...

    @typing.overload
    def SetParameter(self, parameterName: str, value: System.Data.Common.DbParameter, ) -> None:
        ...

    def Bind(self, stmt: SQLitePCL.sqlite3_stmt, ) -> int:
        ...

    def IndexOfChecked(self, parameterName: str, ) -> int:
        ...

class SqliteConnectionStringBuilder(System.Collections.IDictionary, System.Collections.ICollection, System.Collections.IEnumerable, System.ComponentModel.ICustomTypeDescriptor, System.Data.Common.DbConnectionStringBuilder):
    @typing.overload
    def __init__(self, **kwargs):
        self._objectID: int
        ...

    # static fields

    # properties
    @property
    def DataSource(self) -> str:
        ...
    @DataSource.setter
    def DataSource(self, val: str):
        ...

    @property
    def Mode(self) -> int:
        ...
    @Mode.setter
    def Mode(self, val: int):
        ...

    @property
    def Keys(self) -> System.Collections.ICollection:
        ...

    @property
    def Values(self) -> System.Collections.ICollection:
        ...

    @property
    def Cache(self) -> int:
        ...
    @Cache.setter
    def Cache(self, val: int):
        ...

    @property
    def Password(self) -> str:
        ...
    @Password.setter
    def Password(self, val: str):
        ...

    @property
    def ForeignKeys(self) -> System.Nullable[bool]:
        ...
    @ForeignKeys.setter
    def ForeignKeys(self, val: System.Nullable[bool]):
        ...

    @property
    def RecursiveTriggers(self) -> bool:
        ...
    @RecursiveTriggers.setter
    def RecursiveTriggers(self, val: bool):
        ...

    @property
    def DefaultTimeout(self) -> int:
        ...
    @DefaultTimeout.setter
    def DefaultTimeout(self, val: int):
        ...

    @property
    def Pooling(self) -> bool:
        ...
    @Pooling.setter
    def Pooling(self, val: bool):
        ...

    @property
    def Item(self) -> System.Object:
        ...
    @Item.setter
    def Item(self, val: System.Object):
        ...

    @property
    def BrowsableConnectionString(self) -> bool:
        ...
    @BrowsableConnectionString.setter
    def BrowsableConnectionString(self, val: bool):
        ...

    @property
    def ConnectionString(self) -> str:
        ...
    @ConnectionString.setter
    def ConnectionString(self, val: str):
        ...

    @property
    def Count(self) -> int:
        ...

    @property
    def IsReadOnly(self) -> bool:
        ...

    @property
    def IsFixedSize(self) -> bool:
        ...

    @property
    def ObjectID(self) -> int:
        ...

    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def __init__(self, connectionString: str, ):
        ...

    @staticmethod
    def ConvertToEnum(value: System.Object, ) -> TEnum:
        ...

    @staticmethod
    def ConvertToNullableBoolean(value: System.Object, ) -> System.Nullable[bool]:
        ...

    def Clear(self, ) -> None:
        ...

    def ContainsKey(self, keyword: str, ) -> bool:
        ...

    def Remove(self, keyword: str, ) -> bool:
        ...

    def ShouldSerialize(self, keyword: str, ) -> bool:
        ...

    def TryGetValue(self, keyword: str, value: ref[System.Object], ) -> bool:
        ...

    def GetAt(self, index: int, ) -> System.Object:
        ...

    @staticmethod
    def GetIndex(keyword: str, ) -> int:
        ...

    def Reset(self, index: int, ) -> None:
        ...

class SqliteOpenMode(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    ReadWriteCreate: int = ...
    ReadWrite: int = ...
    ReadOnly: int = ...
    Memory: int = ...

class SqliteCacheMode(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    Default: int = ...
    Private: int = ...
    Shared: int = ...

class SqliteTransaction(System.Data.IDbTransaction, System.IDisposable, System.IAsyncDisposable, System.Data.Common.DbTransaction):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def Connection(self) -> Microsoft.Data.Sqlite.SqliteConnection:
        ...

    @property
    def DbConnection(self) -> System.Data.Common.DbConnection:
        ...

    @property
    def ExternalRollback(self) -> bool:
        ...
    @ExternalRollback.setter
    def ExternalRollback(self, val: bool):
        ...

    @property
    def IsolationLevel(self) -> int:
        ...

    @property
    def SupportsSavepoints(self) -> bool:
        ...

    @property
    def Connection(self) -> System.Data.Common.DbConnection:
        ...

    # methods
    def __init__(self, connection: Microsoft.Data.Sqlite.SqliteConnection, isolationLevel: int, deferred: bool, ):
        ...

    def Commit(self, ) -> None:
        ...

    @typing.overload
    def Rollback(self, ) -> None:
        ...

    @typing.overload
    def Rollback(self, savepointName: str, ) -> None:
        ...

    def Save(self, savepointName: str, ) -> None:
        ...

    def Release(self, savepointName: str, ) -> None:
        ...

    def Dispose(self, disposing: bool, ) -> None:
        ...

    def Complete(self, ) -> None:
        ...

    def RollbackInternal(self, ) -> None:
        ...

    def RollbackExternal(self, userData: System.Object, ) -> None:
        ...

