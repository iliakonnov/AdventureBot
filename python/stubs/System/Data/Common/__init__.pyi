from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import System.ComponentModel
import System
import System.Data
import System.Data.Common
import System.Threading.Tasks
import System.Threading
import System.Transactions
import System.Collections
import System.IO
import System.Collections.ObjectModel
import System.Collections.Generic

T = typing.TypeVar('T')

class DbCommand(System.ComponentModel.IComponent, System.IDisposable, System.Data.IDbCommand, System.IAsyncDisposable, System.ComponentModel.Component, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @abc.abstractmethod
    @property
    def CommandText(self) -> System.String:
        ...
    @abc.abstractmethod
    @CommandText.setter
    def CommandText(self, val: System.String):
        ...

    @abc.abstractmethod
    @property
    def CommandTimeout(self) -> System.Int32:
        ...
    @abc.abstractmethod
    @CommandTimeout.setter
    def CommandTimeout(self, val: System.Int32):
        ...

    @abc.abstractmethod
    @property
    def CommandType(self) -> System.Data.CommandType:
        ...
    @abc.abstractmethod
    @CommandType.setter
    def CommandType(self, val: System.Data.CommandType):
        ...

    @property
    def Connection(self) -> System.Data.Common.DbConnection:
        ...
    @Connection.setter
    def Connection(self, val: System.Data.Common.DbConnection):
        ...

    @abc.abstractmethod
    @property
    def DesignTimeVisible(self) -> System.Boolean:
        ...
    @abc.abstractmethod
    @DesignTimeVisible.setter
    def DesignTimeVisible(self, val: System.Boolean):
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

    @abc.abstractmethod
    @property
    def UpdatedRowSource(self) -> System.Data.UpdateRowSource:
        ...
    @abc.abstractmethod
    @UpdatedRowSource.setter
    def UpdatedRowSource(self, val: System.Data.UpdateRowSource):
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
    @abc.abstractmethod
    def Prepare(self, ) -> None:
        ...

    @typing.overload
    @abc.abstractmethod
    def ExecuteNonQuery(self, ) -> System.Int32:
        ...

    @typing.overload
    @abc.abstractmethod
    def ExecuteScalar(self, ) -> System.Object:
        ...

    @typing.overload
    @abc.abstractmethod
    def Cancel(self, ) -> None:
        ...

    @typing.overload
    def CreateParameter(self, ) -> System.Data.Common.DbParameter:
        ...

    @typing.overload
    def ExecuteReader(self, ) -> System.Data.Common.DbDataReader:
        ...

    @typing.overload
    def ExecuteReader(self, behavior: System.Data.CommandBehavior, ) -> System.Data.Common.DbDataReader:
        ...

    @typing.overload
    def ExecuteNonQueryAsync(self, ) -> System.Threading.Tasks.Task[System.Int32]:
        ...

    @typing.overload
    def ExecuteNonQueryAsync(self, cancellationToken: System.Threading.CancellationToken, ) -> System.Threading.Tasks.Task[System.Int32]:
        ...

    @typing.overload
    def ExecuteReaderAsync(self, ) -> System.Threading.Tasks.Task[System.Data.Common.DbDataReader]:
        ...

    @typing.overload
    def ExecuteReaderAsync(self, cancellationToken: System.Threading.CancellationToken, ) -> System.Threading.Tasks.Task[System.Data.Common.DbDataReader]:
        ...

    @typing.overload
    def ExecuteReaderAsync(self, behavior: System.Data.CommandBehavior, ) -> System.Threading.Tasks.Task[System.Data.Common.DbDataReader]:
        ...

    @typing.overload
    def ExecuteReaderAsync(self, behavior: System.Data.CommandBehavior, cancellationToken: System.Threading.CancellationToken, ) -> System.Threading.Tasks.Task[System.Data.Common.DbDataReader]:
        ...

    @typing.overload
    def ExecuteScalarAsync(self, ) -> System.Threading.Tasks.Task[System.Object]:
        ...

    @typing.overload
    def ExecuteScalarAsync(self, cancellationToken: System.Threading.CancellationToken, ) -> System.Threading.Tasks.Task[System.Object]:
        ...

    @typing.overload
    def PrepareAsync(self, cancellationToken: System.Threading.CancellationToken, ) -> System.Threading.Tasks.Task:
        ...

    @typing.overload
    def DisposeAsync(self, ) -> System.Threading.Tasks.ValueTask:
        ...

class DbConnection(System.ComponentModel.IComponent, System.IDisposable, System.Data.IDbConnection, System.IAsyncDisposable, System.ComponentModel.Component, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @abc.abstractmethod
    @property
    def ConnectionString(self) -> System.String:
        ...
    @abc.abstractmethod
    @ConnectionString.setter
    def ConnectionString(self, val: System.String):
        ...

    @property
    def ConnectionTimeout(self) -> System.Int32:
        ...

    @abc.abstractmethod
    @property
    def Database(self) -> System.String:
        ...

    @abc.abstractmethod
    @property
    def DataSource(self) -> System.String:
        ...

    @abc.abstractmethod
    @property
    def ServerVersion(self) -> System.String:
        ...

    @abc.abstractmethod
    @property
    def State(self) -> System.Data.ConnectionState:
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
    @abc.abstractmethod
    def ChangeDatabase(self, databaseName: System.String, ) -> None:
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
    @abc.abstractmethod
    def Open(self, ) -> None:
        ...

    @typing.overload
    @abc.abstractmethod
    def Close(self, ) -> None:
        ...

    @typing.overload
    def BeginTransaction(self, ) -> System.Data.Common.DbTransaction:
        ...

    @typing.overload
    def BeginTransaction(self, isolationLevel: System.Data.IsolationLevel, ) -> System.Data.Common.DbTransaction:
        ...

    @typing.overload
    def BeginTransactionAsync(self, cancellationToken: System.Threading.CancellationToken, ) -> System.Threading.Tasks.ValueTask[System.Data.Common.DbTransaction]:
        ...

    @typing.overload
    def BeginTransactionAsync(self, isolationLevel: System.Data.IsolationLevel, cancellationToken: System.Threading.CancellationToken, ) -> System.Threading.Tasks.ValueTask[System.Data.Common.DbTransaction]:
        ...

    @typing.overload
    def CloseAsync(self, ) -> System.Threading.Tasks.Task:
        ...

    @typing.overload
    def DisposeAsync(self, ) -> System.Threading.Tasks.ValueTask:
        ...

    @typing.overload
    def ChangeDatabaseAsync(self, databaseName: System.String, cancellationToken: System.Threading.CancellationToken, ) -> System.Threading.Tasks.Task:
        ...

    @typing.overload
    def CreateBatch(self, ) -> System.Data.Common.DbBatch:
        ...

    @typing.overload
    def CreateCommand(self, ) -> System.Data.Common.DbCommand:
        ...

    @typing.overload
    def EnlistTransaction(self, transaction: System.Transactions.Transaction, ) -> None:
        ...

    @typing.overload
    def GetSchemaAsync(self, cancellationToken: System.Threading.CancellationToken, ) -> System.Threading.Tasks.Task[System.Data.DataTable]:
        ...

    @typing.overload
    def GetSchemaAsync(self, collectionName: System.String, cancellationToken: System.Threading.CancellationToken, ) -> System.Threading.Tasks.Task[System.Data.DataTable]:
        ...

    @typing.overload
    def GetSchemaAsync(self, collectionName: System.String, restrictionValues: list[System.String], cancellationToken: System.Threading.CancellationToken, ) -> System.Threading.Tasks.Task[System.Data.DataTable]:
        ...

    @typing.overload
    def OpenAsync(self, ) -> System.Threading.Tasks.Task:
        ...

    @typing.overload
    def OpenAsync(self, cancellationToken: System.Threading.CancellationToken, ) -> System.Threading.Tasks.Task:
        ...

class DbParameterCollection(System.Data.IDataParameterCollection, System.Collections.IList, System.Collections.ICollection, System.Collections.IEnumerable, System.MarshalByRefObject, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @abc.abstractmethod
    @property
    def Count(self) -> System.Int32:
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

    @abc.abstractmethod
    @property
    def SyncRoot(self) -> System.Object:
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
    @abc.abstractmethod
    def Add(self, value: System.Object, ) -> System.Int32:
        ...

    @typing.overload
    @abc.abstractmethod
    def AddRange(self, values: System.Array, ) -> None:
        ...

    @typing.overload
    @abc.abstractmethod
    def Clear(self, ) -> None:
        ...

    @typing.overload
    @abc.abstractmethod
    def Contains(self, value: System.Object, ) -> System.Boolean:
        ...

    @typing.overload
    @abc.abstractmethod
    def Contains(self, value: System.String, ) -> System.Boolean:
        ...

    @typing.overload
    @abc.abstractmethod
    def CopyTo(self, array: System.Array, index: System.Int32, ) -> None:
        ...

    @typing.overload
    @abc.abstractmethod
    def GetEnumerator(self, ) -> System.Collections.IEnumerator:
        ...

    @typing.overload
    @abc.abstractmethod
    def IndexOf(self, value: System.Object, ) -> System.Int32:
        ...

    @typing.overload
    @abc.abstractmethod
    def IndexOf(self, parameterName: System.String, ) -> System.Int32:
        ...

    @typing.overload
    @abc.abstractmethod
    def Insert(self, index: System.Int32, value: System.Object, ) -> None:
        ...

    @typing.overload
    @abc.abstractmethod
    def Remove(self, value: System.Object, ) -> None:
        ...

    @typing.overload
    @abc.abstractmethod
    def RemoveAt(self, index: System.Int32, ) -> None:
        ...

    @typing.overload
    @abc.abstractmethod
    def RemoveAt(self, parameterName: System.String, ) -> None:
        ...

class DbTransaction(System.Data.IDbTransaction, System.IDisposable, System.IAsyncDisposable, System.MarshalByRefObject, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def Connection(self) -> System.Data.Common.DbConnection:
        ...

    @abc.abstractmethod
    @property
    def IsolationLevel(self) -> System.Data.IsolationLevel:
        ...

    @property
    def SupportsSavepoints(self) -> System.Boolean:
        ...

    # methods
    @typing.overload
    @abc.abstractmethod
    def Commit(self, ) -> None:
        ...

    @typing.overload
    @abc.abstractmethod
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

    @typing.overload
    def CommitAsync(self, cancellationToken: System.Threading.CancellationToken, ) -> System.Threading.Tasks.Task:
        ...

    @typing.overload
    def Dispose(self, ) -> None:
        ...

    @typing.overload
    def DisposeAsync(self, ) -> System.Threading.Tasks.ValueTask:
        ...

    @typing.overload
    def RollbackAsync(self, cancellationToken: System.Threading.CancellationToken, ) -> System.Threading.Tasks.Task:
        ...

    @typing.overload
    def SaveAsync(self, savepointName: System.String, cancellationToken: System.Threading.CancellationToken, ) -> System.Threading.Tasks.Task:
        ...

    @typing.overload
    def RollbackAsync(self, savepointName: System.String, cancellationToken: System.Threading.CancellationToken, ) -> System.Threading.Tasks.Task:
        ...

    @typing.overload
    def ReleaseAsync(self, savepointName: System.String, cancellationToken: System.Threading.CancellationToken, ) -> System.Threading.Tasks.Task:
        ...

class DbDataReader(System.Data.IDataReader, System.IDisposable, System.Data.IDataRecord, System.Collections.IEnumerable, System.IAsyncDisposable, System.MarshalByRefObject, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @abc.abstractmethod
    @property
    def Depth(self) -> System.Int32:
        ...

    @abc.abstractmethod
    @property
    def FieldCount(self) -> System.Int32:
        ...

    @abc.abstractmethod
    @property
    def HasRows(self) -> System.Boolean:
        ...

    @abc.abstractmethod
    @property
    def IsClosed(self) -> System.Boolean:
        ...

    @abc.abstractmethod
    @property
    def RecordsAffected(self) -> System.Int32:
        ...

    @property
    def VisibleFieldCount(self) -> System.Int32:
        ...

    @abc.abstractmethod
    @property
    def Item(self) -> System.Object:
        ...

    @abc.abstractmethod
    @property
    def Item(self) -> System.Object:
        ...

    # methods
    @typing.overload
    @abc.abstractmethod
    def GetEnumerator(self, ) -> System.Collections.IEnumerator:
        ...

    @typing.overload
    @abc.abstractmethod
    def Read(self, ) -> System.Boolean:
        ...

    @typing.overload
    @abc.abstractmethod
    def NextResult(self, ) -> System.Boolean:
        ...

    @typing.overload
    def Close(self, ) -> None:
        ...

    @typing.overload
    @abc.abstractmethod
    def GetName(self, ordinal: System.Int32, ) -> System.String:
        ...

    @typing.overload
    @abc.abstractmethod
    def GetOrdinal(self, name: System.String, ) -> System.Int32:
        ...

    @typing.overload
    @abc.abstractmethod
    def GetDataTypeName(self, ordinal: System.Int32, ) -> System.String:
        ...

    @typing.overload
    @abc.abstractmethod
    def GetFieldType(self, ordinal: System.Int32, ) -> System.Type:
        ...

    @typing.overload
    @abc.abstractmethod
    def IsDBNull(self, ordinal: System.Int32, ) -> System.Boolean:
        ...

    @typing.overload
    @abc.abstractmethod
    def GetBoolean(self, ordinal: System.Int32, ) -> System.Boolean:
        ...

    @typing.overload
    @abc.abstractmethod
    def GetByte(self, ordinal: System.Int32, ) -> System.Byte:
        ...

    @typing.overload
    @abc.abstractmethod
    def GetChar(self, ordinal: System.Int32, ) -> System.Char:
        ...

    @typing.overload
    @abc.abstractmethod
    def GetDateTime(self, ordinal: System.Int32, ) -> System.DateTime:
        ...

    @typing.overload
    @abc.abstractmethod
    def GetDecimal(self, ordinal: System.Int32, ) -> System.Decimal:
        ...

    @typing.overload
    @abc.abstractmethod
    def GetDouble(self, ordinal: System.Int32, ) -> System.Double:
        ...

    @typing.overload
    @abc.abstractmethod
    def GetFloat(self, ordinal: System.Int32, ) -> System.Single:
        ...

    @typing.overload
    @abc.abstractmethod
    def GetGuid(self, ordinal: System.Int32, ) -> System.Guid:
        ...

    @typing.overload
    @abc.abstractmethod
    def GetInt16(self, ordinal: System.Int32, ) -> System.Int16:
        ...

    @typing.overload
    @abc.abstractmethod
    def GetInt32(self, ordinal: System.Int32, ) -> System.Int32:
        ...

    @typing.overload
    @abc.abstractmethod
    def GetInt64(self, ordinal: System.Int32, ) -> System.Int64:
        ...

    @typing.overload
    @abc.abstractmethod
    def GetString(self, ordinal: System.Int32, ) -> System.String:
        ...

    @typing.overload
    @abc.abstractmethod
    def GetBytes(self, ordinal: System.Int32, dataOffset: System.Int64, buffer: list[System.Byte], bufferOffset: System.Int32, length: System.Int32, ) -> System.Int64:
        ...

    @typing.overload
    @abc.abstractmethod
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
    @abc.abstractmethod
    def GetValue(self, ordinal: System.Int32, ) -> System.Object:
        ...

    @typing.overload
    @abc.abstractmethod
    def GetValues(self, values: list[System.Object], ) -> System.Int32:
        ...

    @typing.overload
    def GetSchemaTable(self, ) -> System.Data.DataTable:
        ...

    @typing.overload
    def CloseAsync(self, ) -> System.Threading.Tasks.Task:
        ...

    @typing.overload
    def Dispose(self, ) -> None:
        ...

    @typing.overload
    def DisposeAsync(self, ) -> System.Threading.Tasks.ValueTask:
        ...

    @typing.overload
    def GetSchemaTableAsync(self, cancellationToken: System.Threading.CancellationToken, ) -> System.Threading.Tasks.Task[System.Data.DataTable]:
        ...

    @typing.overload
    def GetColumnSchemaAsync(self, cancellationToken: System.Threading.CancellationToken, ) -> System.Threading.Tasks.Task[System.Collections.ObjectModel.ReadOnlyCollection[System.Data.Common.DbColumn]]:
        ...

    @typing.overload
    def GetData(self, ordinal: System.Int32, ) -> System.Data.Common.DbDataReader:
        ...

    @typing.overload
    def GetProviderSpecificFieldType(self, ordinal: System.Int32, ) -> System.Type:
        ...

    @typing.overload
    def GetProviderSpecificValue(self, ordinal: System.Int32, ) -> System.Object:
        ...

    @typing.overload
    def GetProviderSpecificValues(self, values: list[System.Object], ) -> System.Int32:
        ...

    @typing.overload
    def GetFieldValueAsync(self, ordinal: System.Int32, ) -> System.Threading.Tasks.Task[T]:
        ...

    @typing.overload
    def GetFieldValueAsync(self, ordinal: System.Int32, cancellationToken: System.Threading.CancellationToken, ) -> System.Threading.Tasks.Task[T]:
        ...

    @typing.overload
    def IsDBNullAsync(self, ordinal: System.Int32, ) -> System.Threading.Tasks.Task[System.Boolean]:
        ...

    @typing.overload
    def IsDBNullAsync(self, ordinal: System.Int32, cancellationToken: System.Threading.CancellationToken, ) -> System.Threading.Tasks.Task[System.Boolean]:
        ...

    @typing.overload
    def ReadAsync(self, ) -> System.Threading.Tasks.Task[System.Boolean]:
        ...

    @typing.overload
    def ReadAsync(self, cancellationToken: System.Threading.CancellationToken, ) -> System.Threading.Tasks.Task[System.Boolean]:
        ...

    @typing.overload
    def NextResultAsync(self, ) -> System.Threading.Tasks.Task[System.Boolean]:
        ...

    @typing.overload
    def NextResultAsync(self, cancellationToken: System.Threading.CancellationToken, ) -> System.Threading.Tasks.Task[System.Boolean]:
        ...

class DbParameter(System.Data.IDbDataParameter, System.Data.IDataParameter, System.MarshalByRefObject, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @abc.abstractmethod
    @property
    def DbType(self) -> System.Data.DbType:
        ...
    @abc.abstractmethod
    @DbType.setter
    def DbType(self, val: System.Data.DbType):
        ...

    @abc.abstractmethod
    @property
    def Direction(self) -> System.Data.ParameterDirection:
        ...
    @abc.abstractmethod
    @Direction.setter
    def Direction(self, val: System.Data.ParameterDirection):
        ...

    @abc.abstractmethod
    @property
    def IsNullable(self) -> System.Boolean:
        ...
    @abc.abstractmethod
    @IsNullable.setter
    def IsNullable(self, val: System.Boolean):
        ...

    @abc.abstractmethod
    @property
    def ParameterName(self) -> System.String:
        ...
    @abc.abstractmethod
    @ParameterName.setter
    def ParameterName(self, val: System.String):
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

    @abc.abstractmethod
    @property
    def Size(self) -> System.Int32:
        ...
    @abc.abstractmethod
    @Size.setter
    def Size(self, val: System.Int32):
        ...

    @abc.abstractmethod
    @property
    def SourceColumn(self) -> System.String:
        ...
    @abc.abstractmethod
    @SourceColumn.setter
    def SourceColumn(self, val: System.String):
        ...

    @abc.abstractmethod
    @property
    def SourceColumnNullMapping(self) -> System.Boolean:
        ...
    @abc.abstractmethod
    @SourceColumnNullMapping.setter
    def SourceColumnNullMapping(self, val: System.Boolean):
        ...

    @property
    def SourceVersion(self) -> System.Data.DataRowVersion:
        ...
    @SourceVersion.setter
    def SourceVersion(self, val: System.Data.DataRowVersion):
        ...

    @abc.abstractmethod
    @property
    def Value(self) -> System.Object:
        ...
    @abc.abstractmethod
    @Value.setter
    def Value(self, val: System.Object):
        ...

    # methods
    @typing.overload
    @abc.abstractmethod
    def ResetDbType(self, ) -> None:
        ...

class DbBatch(System.IDisposable, System.IAsyncDisposable, System.Object, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def BatchCommands(self) -> System.Data.Common.DbBatchCommandCollection:
        ...

    @abc.abstractmethod
    @property
    def Timeout(self) -> System.Int32:
        ...
    @abc.abstractmethod
    @Timeout.setter
    def Timeout(self, val: System.Int32):
        ...

    @property
    def Connection(self) -> System.Data.Common.DbConnection:
        ...
    @Connection.setter
    def Connection(self, val: System.Data.Common.DbConnection):
        ...

    @property
    def Transaction(self) -> System.Data.Common.DbTransaction:
        ...
    @Transaction.setter
    def Transaction(self, val: System.Data.Common.DbTransaction):
        ...

    # methods
    @typing.overload
    def ExecuteReader(self, behavior: System.Data.CommandBehavior, ) -> System.Data.Common.DbDataReader:
        ...

    @typing.overload
    def ExecuteReaderAsync(self, cancellationToken: System.Threading.CancellationToken, ) -> System.Threading.Tasks.Task[System.Data.Common.DbDataReader]:
        ...

    @typing.overload
    def ExecuteReaderAsync(self, behavior: System.Data.CommandBehavior, cancellationToken: System.Threading.CancellationToken, ) -> System.Threading.Tasks.Task[System.Data.Common.DbDataReader]:
        ...

    @typing.overload
    @abc.abstractmethod
    def ExecuteNonQuery(self, ) -> System.Int32:
        ...

    @typing.overload
    @abc.abstractmethod
    def ExecuteNonQueryAsync(self, cancellationToken: System.Threading.CancellationToken, ) -> System.Threading.Tasks.Task[System.Int32]:
        ...

    @typing.overload
    @abc.abstractmethod
    def ExecuteScalar(self, ) -> System.Object:
        ...

    @typing.overload
    @abc.abstractmethod
    def ExecuteScalarAsync(self, cancellationToken: System.Threading.CancellationToken, ) -> System.Threading.Tasks.Task[System.Object]:
        ...

    @typing.overload
    @abc.abstractmethod
    def Prepare(self, ) -> None:
        ...

    @typing.overload
    @abc.abstractmethod
    def PrepareAsync(self, cancellationToken: System.Threading.CancellationToken, ) -> System.Threading.Tasks.Task:
        ...

    @typing.overload
    @abc.abstractmethod
    def Cancel(self, ) -> None:
        ...

    @typing.overload
    def CreateBatchCommand(self, ) -> System.Data.Common.DbBatchCommand:
        ...

    @typing.overload
    def Dispose(self, ) -> None:
        ...

    @typing.overload
    def DisposeAsync(self, ) -> System.Threading.Tasks.ValueTask:
        ...

class DbColumn(System.Object, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def AllowDBNull(self) -> System.Nullable[System.Boolean]:
        ...

    @property
    def BaseCatalogName(self) -> System.String:
        ...

    @property
    def BaseColumnName(self) -> System.String:
        ...

    @property
    def BaseSchemaName(self) -> System.String:
        ...

    @property
    def BaseServerName(self) -> System.String:
        ...

    @property
    def BaseTableName(self) -> System.String:
        ...

    @property
    def ColumnName(self) -> System.String:
        ...

    @property
    def ColumnOrdinal(self) -> System.Nullable[System.Int32]:
        ...

    @property
    def ColumnSize(self) -> System.Nullable[System.Int32]:
        ...

    @property
    def IsAliased(self) -> System.Nullable[System.Boolean]:
        ...

    @property
    def IsAutoIncrement(self) -> System.Nullable[System.Boolean]:
        ...

    @property
    def IsExpression(self) -> System.Nullable[System.Boolean]:
        ...

    @property
    def IsHidden(self) -> System.Nullable[System.Boolean]:
        ...

    @property
    def IsIdentity(self) -> System.Nullable[System.Boolean]:
        ...

    @property
    def IsKey(self) -> System.Nullable[System.Boolean]:
        ...

    @property
    def IsLong(self) -> System.Nullable[System.Boolean]:
        ...

    @property
    def IsReadOnly(self) -> System.Nullable[System.Boolean]:
        ...

    @property
    def IsUnique(self) -> System.Nullable[System.Boolean]:
        ...

    @property
    def NumericPrecision(self) -> System.Nullable[System.Int32]:
        ...

    @property
    def NumericScale(self) -> System.Nullable[System.Int32]:
        ...

    @property
    def UdtAssemblyQualifiedName(self) -> System.String:
        ...

    @property
    def DataType(self) -> System.Type:
        ...

    @property
    def DataTypeName(self) -> System.String:
        ...

    @property
    def Item(self) -> System.Object:
        ...

    # methods
class DbBatchCommandCollection(System.Collections.Generic.IList[System.Data.Common.DbBatchCommand], System.Collections.Generic.ICollection[System.Data.Common.DbBatchCommand], System.Collections.Generic.IEnumerable[System.Data.Common.DbBatchCommand], System.Collections.IEnumerable, System.Object, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @abc.abstractmethod
    @property
    def Count(self) -> System.Int32:
        ...

    @abc.abstractmethod
    @property
    def IsReadOnly(self) -> System.Boolean:
        ...

    @property
    def Item(self) -> System.Data.Common.DbBatchCommand:
        ...
    @Item.setter
    def Item(self, val: System.Data.Common.DbBatchCommand):
        ...

    # methods
    @typing.overload
    @abc.abstractmethod
    def GetEnumerator(self, ) -> System.Collections.Generic.IEnumerator[System.Data.Common.DbBatchCommand]:
        ...

    @typing.overload
    @abc.abstractmethod
    def Add(self, item: System.Data.Common.DbBatchCommand, ) -> None:
        ...

    @typing.overload
    @abc.abstractmethod
    def Clear(self, ) -> None:
        ...

    @typing.overload
    @abc.abstractmethod
    def Contains(self, item: System.Data.Common.DbBatchCommand, ) -> System.Boolean:
        ...

    @typing.overload
    @abc.abstractmethod
    def CopyTo(self, array: list[System.Data.Common.DbBatchCommand], arrayIndex: System.Int32, ) -> None:
        ...

    @typing.overload
    @abc.abstractmethod
    def Remove(self, item: System.Data.Common.DbBatchCommand, ) -> System.Boolean:
        ...

    @typing.overload
    @abc.abstractmethod
    def IndexOf(self, item: System.Data.Common.DbBatchCommand, ) -> System.Int32:
        ...

    @typing.overload
    @abc.abstractmethod
    def Insert(self, index: System.Int32, item: System.Data.Common.DbBatchCommand, ) -> None:
        ...

    @typing.overload
    @abc.abstractmethod
    def RemoveAt(self, index: System.Int32, ) -> None:
        ...

class DbBatchCommand(System.Object, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @abc.abstractmethod
    @property
    def CommandText(self) -> System.String:
        ...
    @abc.abstractmethod
    @CommandText.setter
    def CommandText(self, val: System.String):
        ...

    @abc.abstractmethod
    @property
    def CommandType(self) -> System.Data.CommandType:
        ...
    @abc.abstractmethod
    @CommandType.setter
    def CommandType(self, val: System.Data.CommandType):
        ...

    @abc.abstractmethod
    @property
    def RecordsAffected(self) -> System.Int32:
        ...

    @property
    def Parameters(self) -> System.Data.Common.DbParameterCollection:
        ...

    # methods
