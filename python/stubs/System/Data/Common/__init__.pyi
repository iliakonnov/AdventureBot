from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import System.Data
import System
import System.Collections
import System.Threading.Tasks
import System.Threading
import System.Collections.ObjectModel
import System.Data.Common
import System.IO
import System.ComponentModel
import System.Transactions
import System.Text
import System.Collections.Generic
import System.Data.Common.DbDataAdapter
import System.Data.ProviderBase

T = typing.TypeVar('T')

class DbDataReader(System.Data.IDataReader, System.IDisposable, System.Data.IDataRecord, System.Collections.IEnumerable, System.IAsyncDisposable, System.MarshalByRefObject, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    @abc.abstractmethod
    def Depth(self) -> int:
        ...

    @property
    @abc.abstractmethod
    def FieldCount(self) -> int:
        ...

    @property
    @abc.abstractmethod
    def HasRows(self) -> bool:
        ...

    @property
    @abc.abstractmethod
    def IsClosed(self) -> bool:
        ...

    @property
    @abc.abstractmethod
    def RecordsAffected(self) -> int:
        ...

    @property
    def VisibleFieldCount(self) -> int:
        ...

    @property
    @abc.abstractmethod
    def Item(self) -> System.Object:
        ...

    @property
    @abc.abstractmethod
    def Item(self) -> System.Object:
        ...

    # methods
    def __init__(self, ):
        ...

    def Close(self, ) -> None:
        ...

    def CloseAsync(self, ) -> System.Threading.Tasks.Task:
        ...

    @typing.overload
    def Dispose(self, ) -> None:
        ...

    @typing.overload
    def Dispose(self, disposing: bool, ) -> None:
        ...

    def DisposeAsync(self, ) -> System.Threading.Tasks.ValueTask:
        ...

    @abc.abstractmethod
    def GetDataTypeName(self, ordinal: int, ) -> str:
        ...

    @abc.abstractmethod
    def GetEnumerator(self, ) -> System.Collections.IEnumerator:
        ...

    @abc.abstractmethod
    def GetFieldType(self, ordinal: int, ) -> System.Type:
        ...

    @abc.abstractmethod
    def GetName(self, ordinal: int, ) -> str:
        ...

    @abc.abstractmethod
    def GetOrdinal(self, name: str, ) -> int:
        ...

    def GetSchemaTable(self, ) -> System.Data.DataTable:
        ...

    def GetSchemaTableAsync(self, cancellationToken: System.Threading.CancellationToken = ..., ) -> System.Threading.Tasks.Task[System.Data.DataTable]:
        ...

    def GetColumnSchemaAsync(self, cancellationToken: System.Threading.CancellationToken = ..., ) -> System.Threading.Tasks.Task[System.Collections.ObjectModel.ReadOnlyCollection[System.Data.Common.DbColumn]]:
        ...

    @abc.abstractmethod
    def GetBoolean(self, ordinal: int, ) -> bool:
        ...

    @abc.abstractmethod
    def GetByte(self, ordinal: int, ) -> int:
        ...

    @abc.abstractmethod
    def GetBytes(self, ordinal: int, dataOffset: int, buffer: System.Array[int], bufferOffset: int, length: int, ) -> int:
        ...

    @abc.abstractmethod
    def GetChar(self, ordinal: int, ) -> str:
        ...

    @abc.abstractmethod
    def GetChars(self, ordinal: int, dataOffset: int, buffer: System.Array[str], bufferOffset: int, length: int, ) -> int:
        ...

    def GetData(self, ordinal: int, ) -> System.Data.Common.DbDataReader:
        ...

    def GetData(self, ordinal: int, ) -> System.Data.IDataReader:
        ...

    def GetDbDataReader(self, ordinal: int, ) -> System.Data.Common.DbDataReader:
        ...

    @abc.abstractmethod
    def GetDateTime(self, ordinal: int, ) -> System.DateTime:
        ...

    @abc.abstractmethod
    def GetDecimal(self, ordinal: int, ) -> System.Decimal:
        ...

    @abc.abstractmethod
    def GetDouble(self, ordinal: int, ) -> float:
        ...

    @abc.abstractmethod
    def GetFloat(self, ordinal: int, ) -> float:
        ...

    @abc.abstractmethod
    def GetGuid(self, ordinal: int, ) -> System.Guid:
        ...

    @abc.abstractmethod
    def GetInt16(self, ordinal: int, ) -> int:
        ...

    @abc.abstractmethod
    def GetInt32(self, ordinal: int, ) -> int:
        ...

    @abc.abstractmethod
    def GetInt64(self, ordinal: int, ) -> int:
        ...

    def GetProviderSpecificFieldType(self, ordinal: int, ) -> System.Type:
        ...

    def GetProviderSpecificValue(self, ordinal: int, ) -> System.Object:
        ...

    def GetProviderSpecificValues(self, values: System.Array[System.Object], ) -> int:
        ...

    @abc.abstractmethod
    def GetString(self, ordinal: int, ) -> str:
        ...

    def GetStream(self, ordinal: int, ) -> System.IO.Stream:
        ...

    def GetTextReader(self, ordinal: int, ) -> System.IO.TextReader:
        ...

    @abc.abstractmethod
    def GetValue(self, ordinal: int, ) -> System.Object:
        ...

    def GetFieldValue(self, ordinal: int, ) -> T:
        ...

    @typing.overload
    def GetFieldValueAsync(self, ordinal: int, ) -> System.Threading.Tasks.Task[T]:
        ...

    @typing.overload
    def GetFieldValueAsync(self, ordinal: int, cancellationToken: System.Threading.CancellationToken, ) -> System.Threading.Tasks.Task[T]:
        ...

    @abc.abstractmethod
    def GetValues(self, values: System.Array[System.Object], ) -> int:
        ...

    @abc.abstractmethod
    def IsDBNull(self, ordinal: int, ) -> bool:
        ...

    @typing.overload
    def IsDBNullAsync(self, ordinal: int, ) -> System.Threading.Tasks.Task[bool]:
        ...

    @typing.overload
    def IsDBNullAsync(self, ordinal: int, cancellationToken: System.Threading.CancellationToken, ) -> System.Threading.Tasks.Task[bool]:
        ...

    @abc.abstractmethod
    def NextResult(self, ) -> bool:
        ...

    @abc.abstractmethod
    def Read(self, ) -> bool:
        ...

    @typing.overload
    def ReadAsync(self, ) -> System.Threading.Tasks.Task[bool]:
        ...

    @typing.overload
    def ReadAsync(self, cancellationToken: System.Threading.CancellationToken, ) -> System.Threading.Tasks.Task[bool]:
        ...

    @typing.overload
    def NextResultAsync(self, ) -> System.Threading.Tasks.Task[bool]:
        ...

    @typing.overload
    def NextResultAsync(self, cancellationToken: System.Threading.CancellationToken, ) -> System.Threading.Tasks.Task[bool]:
        ...

class DbColumn(System.Object, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def AllowDBNull(self) -> System.Nullable[bool]:
        ...
    @AllowDBNull.setter
    def AllowDBNull(self, val: System.Nullable[bool]):
        ...

    @property
    def BaseCatalogName(self) -> str:
        ...
    @BaseCatalogName.setter
    def BaseCatalogName(self, val: str):
        ...

    @property
    def BaseColumnName(self) -> str:
        ...
    @BaseColumnName.setter
    def BaseColumnName(self, val: str):
        ...

    @property
    def BaseSchemaName(self) -> str:
        ...
    @BaseSchemaName.setter
    def BaseSchemaName(self, val: str):
        ...

    @property
    def BaseServerName(self) -> str:
        ...
    @BaseServerName.setter
    def BaseServerName(self, val: str):
        ...

    @property
    def BaseTableName(self) -> str:
        ...
    @BaseTableName.setter
    def BaseTableName(self, val: str):
        ...

    @property
    def ColumnName(self) -> str:
        ...
    @ColumnName.setter
    def ColumnName(self, val: str):
        ...

    @property
    def ColumnOrdinal(self) -> System.Nullable[int]:
        ...
    @ColumnOrdinal.setter
    def ColumnOrdinal(self, val: System.Nullable[int]):
        ...

    @property
    def ColumnSize(self) -> System.Nullable[int]:
        ...
    @ColumnSize.setter
    def ColumnSize(self, val: System.Nullable[int]):
        ...

    @property
    def IsAliased(self) -> System.Nullable[bool]:
        ...
    @IsAliased.setter
    def IsAliased(self, val: System.Nullable[bool]):
        ...

    @property
    def IsAutoIncrement(self) -> System.Nullable[bool]:
        ...
    @IsAutoIncrement.setter
    def IsAutoIncrement(self, val: System.Nullable[bool]):
        ...

    @property
    def IsExpression(self) -> System.Nullable[bool]:
        ...
    @IsExpression.setter
    def IsExpression(self, val: System.Nullable[bool]):
        ...

    @property
    def IsHidden(self) -> System.Nullable[bool]:
        ...
    @IsHidden.setter
    def IsHidden(self, val: System.Nullable[bool]):
        ...

    @property
    def IsIdentity(self) -> System.Nullable[bool]:
        ...
    @IsIdentity.setter
    def IsIdentity(self, val: System.Nullable[bool]):
        ...

    @property
    def IsKey(self) -> System.Nullable[bool]:
        ...
    @IsKey.setter
    def IsKey(self, val: System.Nullable[bool]):
        ...

    @property
    def IsLong(self) -> System.Nullable[bool]:
        ...
    @IsLong.setter
    def IsLong(self, val: System.Nullable[bool]):
        ...

    @property
    def IsReadOnly(self) -> System.Nullable[bool]:
        ...
    @IsReadOnly.setter
    def IsReadOnly(self, val: System.Nullable[bool]):
        ...

    @property
    def IsUnique(self) -> System.Nullable[bool]:
        ...
    @IsUnique.setter
    def IsUnique(self, val: System.Nullable[bool]):
        ...

    @property
    def NumericPrecision(self) -> System.Nullable[int]:
        ...
    @NumericPrecision.setter
    def NumericPrecision(self, val: System.Nullable[int]):
        ...

    @property
    def NumericScale(self) -> System.Nullable[int]:
        ...
    @NumericScale.setter
    def NumericScale(self, val: System.Nullable[int]):
        ...

    @property
    def UdtAssemblyQualifiedName(self) -> str:
        ...
    @UdtAssemblyQualifiedName.setter
    def UdtAssemblyQualifiedName(self, val: str):
        ...

    @property
    def DataType(self) -> System.Type:
        ...
    @DataType.setter
    def DataType(self, val: System.Type):
        ...

    @property
    def DataTypeName(self) -> str:
        ...
    @DataTypeName.setter
    def DataTypeName(self, val: str):
        ...

    @property
    def Item(self) -> System.Object:
        ...

    # methods
    def __init__(self, ):
        ...

class DbTransaction(System.Data.IDbTransaction, System.IDisposable, System.IAsyncDisposable, System.MarshalByRefObject, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def Connection(self) -> System.Data.Common.DbConnection:
        ...

    @property
    def Connection(self) -> System.Data.IDbConnection:
        ...

    @property
    @abc.abstractmethod
    def DbConnection(self) -> System.Data.Common.DbConnection:
        ...

    @property
    @abc.abstractmethod
    def IsolationLevel(self) -> int:
        ...

    @property
    def SupportsSavepoints(self) -> bool:
        ...

    # methods
    def __init__(self, ):
        ...

    @abc.abstractmethod
    def Commit(self, ) -> None:
        ...

    def CommitAsync(self, cancellationToken: System.Threading.CancellationToken = ..., ) -> System.Threading.Tasks.Task:
        ...

    @typing.overload
    def Dispose(self, ) -> None:
        ...

    @typing.overload
    def Dispose(self, disposing: bool, ) -> None:
        ...

    def DisposeAsync(self, ) -> System.Threading.Tasks.ValueTask:
        ...

    @abc.abstractmethod
    @typing.overload
    def Rollback(self, ) -> None:
        ...

    @typing.overload
    def Rollback(self, savepointName: str, ) -> None:
        ...

    @typing.overload
    def RollbackAsync(self, cancellationToken: System.Threading.CancellationToken = ..., ) -> System.Threading.Tasks.Task:
        ...

    @typing.overload
    def RollbackAsync(self, savepointName: str, cancellationToken: System.Threading.CancellationToken = ..., ) -> System.Threading.Tasks.Task:
        ...

    def SaveAsync(self, savepointName: str, cancellationToken: System.Threading.CancellationToken = ..., ) -> System.Threading.Tasks.Task:
        ...

    def ReleaseAsync(self, savepointName: str, cancellationToken: System.Threading.CancellationToken = ..., ) -> System.Threading.Tasks.Task:
        ...

    def Save(self, savepointName: str, ) -> None:
        ...

    def Release(self, savepointName: str, ) -> None:
        ...

class DbConnection(System.ComponentModel.IComponent, System.IDisposable, System.Data.IDbConnection, System.IAsyncDisposable, System.ComponentModel.Component, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        self._suppressStateChangeForReconnection: bool
        ...

    # static fields

    # properties
    @property
    @abc.abstractmethod
    def ConnectionString(self) -> str:
        ...
    @ConnectionString.setter
    @abc.abstractmethod
    def ConnectionString(self, val: str):
        ...

    @property
    def ConnectionTimeout(self) -> int:
        ...

    @property
    @abc.abstractmethod
    def Database(self) -> str:
        ...

    @property
    @abc.abstractmethod
    def DataSource(self) -> str:
        ...

    @property
    def DbProviderFactory(self) -> System.Data.Common.DbProviderFactory:
        ...

    @property
    def ProviderFactory(self) -> System.Data.Common.DbProviderFactory:
        ...

    @property
    @abc.abstractmethod
    def ServerVersion(self) -> str:
        ...

    @property
    @abc.abstractmethod
    def State(self) -> int:
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
    def __init__(self, ):
        ...

    @abc.abstractmethod
    def BeginDbTransaction(self, isolationLevel: int, ) -> System.Data.Common.DbTransaction:
        ...

    @typing.overload
    def BeginTransaction(self, ) -> System.Data.Common.DbTransaction:
        ...

    @typing.overload
    def BeginTransaction(self, isolationLevel: int, ) -> System.Data.Common.DbTransaction:
        ...

    @typing.overload
    def BeginTransaction(self, ) -> System.Data.IDbTransaction:
        ...

    @typing.overload
    def BeginTransaction(self, isolationLevel: int, ) -> System.Data.IDbTransaction:
        ...

    def BeginDbTransactionAsync(self, isolationLevel: int, cancellationToken: System.Threading.CancellationToken, ) -> System.Threading.Tasks.ValueTask[System.Data.Common.DbTransaction]:
        ...

    @typing.overload
    def BeginTransactionAsync(self, cancellationToken: System.Threading.CancellationToken = ..., ) -> System.Threading.Tasks.ValueTask[System.Data.Common.DbTransaction]:
        ...

    @typing.overload
    def BeginTransactionAsync(self, isolationLevel: int, cancellationToken: System.Threading.CancellationToken = ..., ) -> System.Threading.Tasks.ValueTask[System.Data.Common.DbTransaction]:
        ...

    @abc.abstractmethod
    def Close(self, ) -> None:
        ...

    def CloseAsync(self, ) -> System.Threading.Tasks.Task:
        ...

    def DisposeAsync(self, ) -> System.Threading.Tasks.ValueTask:
        ...

    @abc.abstractmethod
    def ChangeDatabase(self, databaseName: str, ) -> None:
        ...

    def ChangeDatabaseAsync(self, databaseName: str, cancellationToken: System.Threading.CancellationToken = ..., ) -> System.Threading.Tasks.Task:
        ...

    def CreateBatch(self, ) -> System.Data.Common.DbBatch:
        ...

    def CreateDbBatch(self, ) -> System.Data.Common.DbBatch:
        ...

    def CreateCommand(self, ) -> System.Data.Common.DbCommand:
        ...

    def CreateCommand(self, ) -> System.Data.IDbCommand:
        ...

    @abc.abstractmethod
    def CreateDbCommand(self, ) -> System.Data.Common.DbCommand:
        ...

    def EnlistTransaction(self, transaction: System.Transactions.Transaction, ) -> None:
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

    @typing.overload
    def GetSchemaAsync(self, cancellationToken: System.Threading.CancellationToken = ..., ) -> System.Threading.Tasks.Task[System.Data.DataTable]:
        ...

    @typing.overload
    def GetSchemaAsync(self, collectionName: str, cancellationToken: System.Threading.CancellationToken = ..., ) -> System.Threading.Tasks.Task[System.Data.DataTable]:
        ...

    @typing.overload
    def GetSchemaAsync(self, collectionName: str, restrictionValues: System.Array[str], cancellationToken: System.Threading.CancellationToken = ..., ) -> System.Threading.Tasks.Task[System.Data.DataTable]:
        ...

    def OnStateChange(self, stateChange: System.Data.StateChangeEventArgs, ) -> None:
        ...

    @abc.abstractmethod
    def Open(self, ) -> None:
        ...

    @typing.overload
    def OpenAsync(self, ) -> System.Threading.Tasks.Task:
        ...

    @typing.overload
    def OpenAsync(self, cancellationToken: System.Threading.CancellationToken, ) -> System.Threading.Tasks.Task:
        ...

class DbParameter(System.Data.IDbDataParameter, System.Data.IDataParameter, System.MarshalByRefObject, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    @abc.abstractmethod
    def DbType(self) -> int:
        ...
    @DbType.setter
    @abc.abstractmethod
    def DbType(self, val: int):
        ...

    @property
    @abc.abstractmethod
    def Direction(self) -> int:
        ...
    @Direction.setter
    @abc.abstractmethod
    def Direction(self, val: int):
        ...

    @property
    @abc.abstractmethod
    def IsNullable(self) -> bool:
        ...
    @IsNullable.setter
    @abc.abstractmethod
    def IsNullable(self, val: bool):
        ...

    @property
    @abc.abstractmethod
    def ParameterName(self) -> str:
        ...
    @ParameterName.setter
    @abc.abstractmethod
    def ParameterName(self, val: str):
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
    @abc.abstractmethod
    def Size(self) -> int:
        ...
    @Size.setter
    @abc.abstractmethod
    def Size(self, val: int):
        ...

    @property
    @abc.abstractmethod
    def SourceColumn(self) -> str:
        ...
    @SourceColumn.setter
    @abc.abstractmethod
    def SourceColumn(self, val: str):
        ...

    @property
    @abc.abstractmethod
    def SourceColumnNullMapping(self) -> bool:
        ...
    @SourceColumnNullMapping.setter
    @abc.abstractmethod
    def SourceColumnNullMapping(self, val: bool):
        ...

    @property
    def SourceVersion(self) -> int:
        ...
    @SourceVersion.setter
    def SourceVersion(self, val: int):
        ...

    @property
    @abc.abstractmethod
    def Value(self) -> System.Object:
        ...
    @Value.setter
    @abc.abstractmethod
    def Value(self, val: System.Object):
        ...

    # methods
    def __init__(self, ):
        ...

    @abc.abstractmethod
    def ResetDbType(self, ) -> None:
        ...

class DbParameterCollection(System.Data.IDataParameterCollection, System.Collections.IList, System.Collections.ICollection, System.Collections.IEnumerable, System.MarshalByRefObject, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    @abc.abstractmethod
    def Count(self) -> int:
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
    @abc.abstractmethod
    def SyncRoot(self) -> System.Object:
        ...

    @property
    def Item(self) -> System.Object:
        ...
    @Item.setter
    def Item(self, val: System.Object):
        ...

    @property
    def Item(self) -> System.Object:
        ...
    @Item.setter
    def Item(self, val: System.Object):
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

    def Add(self, value: System.Object, ) -> int:
        ...

    @abc.abstractmethod
    def Add(self, value: System.Object, ) -> int:
        ...

    @abc.abstractmethod
    def AddRange(self, values: System.Array, ) -> None:
        ...

    def Contains(self, value: System.Object, ) -> bool:
        ...

    @abc.abstractmethod
    @typing.overload
    def Contains(self, value: System.Object, ) -> bool:
        ...

    @abc.abstractmethod
    @typing.overload
    def Contains(self, value: str, ) -> bool:
        ...

    @abc.abstractmethod
    def CopyTo(self, array: System.Array, index: int, ) -> None:
        ...

    @abc.abstractmethod
    def Clear(self, ) -> None:
        ...

    @abc.abstractmethod
    def GetEnumerator(self, ) -> System.Collections.IEnumerator:
        ...

    @abc.abstractmethod
    @typing.overload
    def GetParameter(self, index: int, ) -> System.Data.Common.DbParameter:
        ...

    @abc.abstractmethod
    @typing.overload
    def GetParameter(self, parameterName: str, ) -> System.Data.Common.DbParameter:
        ...

    def IndexOf(self, value: System.Object, ) -> int:
        ...

    @abc.abstractmethod
    @typing.overload
    def IndexOf(self, value: System.Object, ) -> int:
        ...

    @abc.abstractmethod
    @typing.overload
    def IndexOf(self, parameterName: str, ) -> int:
        ...

    def Insert(self, index: int, value: System.Object, ) -> None:
        ...

    @abc.abstractmethod
    def Insert(self, index: int, value: System.Object, ) -> None:
        ...

    def Remove(self, value: System.Object, ) -> None:
        ...

    @abc.abstractmethod
    def Remove(self, value: System.Object, ) -> None:
        ...

    @abc.abstractmethod
    @typing.overload
    def RemoveAt(self, index: int, ) -> None:
        ...

    @abc.abstractmethod
    @typing.overload
    def RemoveAt(self, parameterName: str, ) -> None:
        ...

    @abc.abstractmethod
    @typing.overload
    def SetParameter(self, index: int, value: System.Data.Common.DbParameter, ) -> None:
        ...

    @abc.abstractmethod
    @typing.overload
    def SetParameter(self, parameterName: str, value: System.Data.Common.DbParameter, ) -> None:
        ...

class DbProviderFactory(System.Object, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def CanCreateBatch(self) -> bool:
        ...

    @property
    def CanCreateDataSourceEnumerator(self) -> bool:
        ...

    @property
    def CanCreateDataAdapter(self) -> bool:
        ...

    @property
    def CanCreateCommandBuilder(self) -> bool:
        ...

    # methods
    def __init__(self, ):
        ...

    def CreateBatch(self, ) -> System.Data.Common.DbBatch:
        ...

    def CreateBatchCommand(self, ) -> System.Data.Common.DbBatchCommand:
        ...

    def CreateCommand(self, ) -> System.Data.Common.DbCommand:
        ...

    def CreateCommandBuilder(self, ) -> System.Data.Common.DbCommandBuilder:
        ...

    def CreateConnection(self, ) -> System.Data.Common.DbConnection:
        ...

    def CreateConnectionStringBuilder(self, ) -> System.Data.Common.DbConnectionStringBuilder:
        ...

    def CreateDataAdapter(self, ) -> System.Data.Common.DbDataAdapter:
        ...

    def CreateParameter(self, ) -> System.Data.Common.DbParameter:
        ...

    def CreateDataSourceEnumerator(self, ) -> System.Data.Common.DbDataSourceEnumerator:
        ...

class DbCommandBuilder(System.ComponentModel.IComponent, System.IDisposable, System.ComponentModel.Component, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def ConflictOption(self) -> int:
        ...
    @ConflictOption.setter
    def ConflictOption(self, val: int):
        ...

    @property
    def CatalogLocation(self) -> int:
        ...
    @CatalogLocation.setter
    def CatalogLocation(self, val: int):
        ...

    @property
    def CatalogSeparator(self) -> str:
        ...
    @CatalogSeparator.setter
    def CatalogSeparator(self, val: str):
        ...

    @property
    def DataAdapter(self) -> System.Data.Common.DbDataAdapter:
        ...
    @DataAdapter.setter
    def DataAdapter(self, val: System.Data.Common.DbDataAdapter):
        ...

    @property
    def ParameterNameMaxLength(self) -> int:
        ...

    @property
    def ParameterNamePattern(self) -> str:
        ...

    @property
    def QuotedBaseTableName(self) -> str:
        ...

    @property
    def QuotePrefix(self) -> str:
        ...
    @QuotePrefix.setter
    def QuotePrefix(self, val: str):
        ...

    @property
    def QuoteSuffix(self) -> str:
        ...
    @QuoteSuffix.setter
    def QuoteSuffix(self, val: str):
        ...

    @property
    def SchemaSeparator(self) -> str:
        ...
    @SchemaSeparator.setter
    def SchemaSeparator(self, val: str):
        ...

    @property
    def SetAllValues(self) -> bool:
        ...
    @SetAllValues.setter
    def SetAllValues(self, val: bool):
        ...

    @property
    def InsertCommand(self) -> System.Data.Common.DbCommand:
        ...
    @InsertCommand.setter
    def InsertCommand(self, val: System.Data.Common.DbCommand):
        ...

    @property
    def UpdateCommand(self) -> System.Data.Common.DbCommand:
        ...
    @UpdateCommand.setter
    def UpdateCommand(self, val: System.Data.Common.DbCommand):
        ...

    @property
    def DeleteCommand(self) -> System.Data.Common.DbCommand:
        ...
    @DeleteCommand.setter
    def DeleteCommand(self, val: System.Data.Common.DbCommand):
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
    def __init__(self, ):
        ...

    def BuildCache(self, closeConnection: bool, dataRow: System.Data.DataRow, useColumnsForParameterNames: bool, ) -> None:
        ...

    def GetSchemaTable(self, sourceCommand: System.Data.Common.DbCommand, ) -> System.Data.DataTable:
        ...

    def BuildInformation(self, schemaTable: System.Data.DataTable, ) -> None:
        ...

    def BuildDeleteCommand(self, mappings: System.Data.Common.DataTableMapping, dataRow: System.Data.DataRow, ) -> System.Data.Common.DbCommand:
        ...

    def BuildInsertCommand(self, mappings: System.Data.Common.DataTableMapping, dataRow: System.Data.DataRow, ) -> System.Data.Common.DbCommand:
        ...

    def BuildUpdateCommand(self, mappings: System.Data.Common.DataTableMapping, dataRow: System.Data.DataRow, ) -> System.Data.Common.DbCommand:
        ...

    def BuildWhereClause(self, mappings: System.Data.Common.DataTableMapping, dataRow: System.Data.DataRow, builder: System.Text.StringBuilder, command: System.Data.Common.DbCommand, parameterCount: int, isUpdate: bool, ) -> int:
        ...

    def CreateParameterForNullTest(self, command: System.Data.Common.DbCommand, parameterName: str, sourceColumn: str, version: int, parameterCount: int, value: System.Object, row: System.Data.Common.DbSchemaRow, statementType: int, whereClause: bool, ) -> str:
        ...

    def CreateParameterForValue(self, command: System.Data.Common.DbCommand, parameterName: str, sourceColumn: str, version: int, parameterCount: int, value: System.Object, row: System.Data.Common.DbSchemaRow, statementType: int, whereClause: bool, ) -> str:
        ...

    def Dispose(self, disposing: bool, ) -> None:
        ...

    def GetTableMapping(self, dataRow: System.Data.DataRow, ) -> System.Data.Common.DataTableMapping:
        ...

    def GetBaseParameterName(self, index: int, ) -> str:
        ...

    def GetOriginalParameterName(self, index: int, ) -> str:
        ...

    def GetNullParameterName(self, index: int, ) -> str:
        ...

    def GetSelectCommand(self, ) -> System.Data.Common.DbCommand:
        ...

    @typing.overload
    def GetInsertCommand(self, ) -> System.Data.Common.DbCommand:
        ...

    @typing.overload
    def GetInsertCommand(self, useColumnsForParameterNames: bool, ) -> System.Data.Common.DbCommand:
        ...

    @typing.overload
    def GetInsertCommand(self, dataRow: System.Data.DataRow, useColumnsForParameterNames: bool, ) -> System.Data.Common.DbCommand:
        ...

    @typing.overload
    def GetUpdateCommand(self, ) -> System.Data.Common.DbCommand:
        ...

    @typing.overload
    def GetUpdateCommand(self, useColumnsForParameterNames: bool, ) -> System.Data.Common.DbCommand:
        ...

    @typing.overload
    def GetUpdateCommand(self, dataRow: System.Data.DataRow, useColumnsForParameterNames: bool, ) -> System.Data.Common.DbCommand:
        ...

    @typing.overload
    def GetDeleteCommand(self, ) -> System.Data.Common.DbCommand:
        ...

    @typing.overload
    def GetDeleteCommand(self, useColumnsForParameterNames: bool, ) -> System.Data.Common.DbCommand:
        ...

    @typing.overload
    def GetDeleteCommand(self, dataRow: System.Data.DataRow, useColumnsForParameterNames: bool, ) -> System.Data.Common.DbCommand:
        ...

    @typing.overload
    def GetColumnValue(self, row: System.Data.DataRow, columnName: str, mappings: System.Data.Common.DataTableMapping, version: int, ) -> System.Object:
        ...

    @typing.overload
    def GetColumnValue(self, row: System.Data.DataRow, column: System.Data.DataColumn, version: int, ) -> System.Object:
        ...

    def GetDataColumn(self, columnName: str, tablemapping: System.Data.Common.DataTableMapping, row: System.Data.DataRow, ) -> System.Data.DataColumn:
        ...

    @staticmethod
    def GetNextParameter(command: System.Data.Common.DbCommand, pcount: int, ) -> System.Data.Common.DbParameter:
        ...

    def IncludeInInsertValues(self, row: System.Data.Common.DbSchemaRow, ) -> bool:
        ...

    def IncludeInUpdateSet(self, row: System.Data.Common.DbSchemaRow, ) -> bool:
        ...

    def IncludeInWhereClause(self, row: System.Data.Common.DbSchemaRow, isUpdate: bool, ) -> bool:
        ...

    def IncrementWhereCount(self, row: System.Data.Common.DbSchemaRow, ) -> bool:
        ...

    def InitializeCommand(self, command: System.Data.Common.DbCommand, ) -> System.Data.Common.DbCommand:
        ...

    def QuotedColumn(self, column: str, ) -> str:
        ...

    def QuoteIdentifier(self, unquotedIdentifier: str, ) -> str:
        ...

    def RefreshSchema(self, ) -> None:
        ...

    @staticmethod
    def RemoveExtraParameters(command: System.Data.Common.DbCommand, usedParameterCount: int, ) -> None:
        ...

    def RowUpdatingHandler(self, rowUpdatingEvent: System.Data.Common.RowUpdatingEventArgs, ) -> None:
        ...

    def RowUpdatingHandlerBuilder(self, rowUpdatingEvent: System.Data.Common.RowUpdatingEventArgs, ) -> None:
        ...

    def UnquoteIdentifier(self, quotedIdentifier: str, ) -> str:
        ...

    @abc.abstractmethod
    def ApplyParameterInfo(self, parameter: System.Data.Common.DbParameter, row: System.Data.DataRow, statementType: int, whereClause: bool, ) -> None:
        ...

    @abc.abstractmethod
    @typing.overload
    def GetParameterName(self, parameterOrdinal: int, ) -> str:
        ...

    @abc.abstractmethod
    @typing.overload
    def GetParameterName(self, parameterName: str, ) -> str:
        ...

    @abc.abstractmethod
    def GetParameterPlaceholder(self, parameterOrdinal: int, ) -> str:
        ...

    @abc.abstractmethod
    def SetRowUpdatingHandler(self, adapter: System.Data.Common.DbDataAdapter, ) -> None:
        ...

class CatalogLocation(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    Start: int = ...
    End: int = ...

class DbBatchCommand(System.Object, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    @abc.abstractmethod
    def CommandText(self) -> str:
        ...
    @CommandText.setter
    @abc.abstractmethod
    def CommandText(self, val: str):
        ...

    @property
    @abc.abstractmethod
    def CommandType(self) -> int:
        ...
    @CommandType.setter
    @abc.abstractmethod
    def CommandType(self, val: int):
        ...

    @property
    @abc.abstractmethod
    def RecordsAffected(self) -> int:
        ...

    @property
    def Parameters(self) -> System.Data.Common.DbParameterCollection:
        ...

    @property
    @abc.abstractmethod
    def DbParameterCollection(self) -> System.Data.Common.DbParameterCollection:
        ...

    # methods
    def __init__(self, ):
        ...

class RowUpdatingEventArgs(System.EventArgs):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def BaseCommand(self) -> System.Data.IDbCommand:
        ...
    @BaseCommand.setter
    def BaseCommand(self, val: System.Data.IDbCommand):
        ...

    @property
    def Command(self) -> System.Data.IDbCommand:
        ...
    @Command.setter
    def Command(self, val: System.Data.IDbCommand):
        ...

    @property
    def Errors(self) -> System.Exception:
        ...
    @Errors.setter
    def Errors(self, val: System.Exception):
        ...

    @property
    def Row(self) -> System.Data.DataRow:
        ...

    @property
    def StatementType(self) -> int:
        ...

    @property
    def Status(self) -> int:
        ...
    @Status.setter
    def Status(self, val: int):
        ...

    @property
    def TableMapping(self) -> System.Data.Common.DataTableMapping:
        ...

    # methods
    def __init__(self, dataRow: System.Data.DataRow, command: System.Data.IDbCommand, statementType: int, tableMapping: System.Data.Common.DataTableMapping, ):
        ...

class DbConnectionStringBuilder(System.Collections.IDictionary, System.Collections.ICollection, System.Collections.IEnumerable, System.ComponentModel.ICustomTypeDescriptor, System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        self._objectID: int
        ...

    # static fields

    # properties
    @property
    def Collection(self) -> System.Collections.ICollection:
        ...

    @property
    def Dictionary(self) -> System.Collections.IDictionary:
        ...

    @property
    def CurrentValues(self) -> System.Collections.Generic.Dictionary[str, System.Object]:
        ...

    @property
    def Item(self) -> System.Object:
        ...
    @Item.setter
    def Item(self, val: System.Object):
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
    def IsSynchronized(self) -> bool:
        ...

    @property
    def Keys(self) -> System.Collections.ICollection:
        ...

    @property
    def ObjectID(self) -> int:
        ...

    @property
    def SyncRoot(self) -> System.Object:
        ...

    @property
    def Values(self) -> System.Collections.ICollection:
        ...

    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def __init__(self, useOdbcRules: bool, ):
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

    def ConvertValueToString(self, value: System.Object, ) -> str:
        ...

    def Add(self, keyword: System.Object, value: System.Object, ) -> None:
        ...

    def Add(self, keyword: str, value: System.Object, ) -> None:
        ...

    @staticmethod
    @typing.overload
    def AppendKeyValuePair(builder: System.Text.StringBuilder, keyword: str, value: str, ) -> None:
        ...

    @staticmethod
    @typing.overload
    def AppendKeyValuePair(builder: System.Text.StringBuilder, keyword: str, value: str, useOdbcRules: bool, ) -> None:
        ...

    def ClearPropertyDescriptors(self, ) -> None:
        ...

    def Contains(self, keyword: System.Object, ) -> bool:
        ...

    def CopyTo(self, array: System.Array, index: int, ) -> None:
        ...

    def EquivalentTo(self, connectionStringBuilder: System.Data.Common.DbConnectionStringBuilder, ) -> bool:
        ...

    def GetEnumerator(self, ) -> System.Collections.IEnumerator:
        ...

    def GetEnumerator(self, ) -> System.Collections.IDictionaryEnumerator:
        ...

    def ObjectToString(self, keyword: System.Object, ) -> str:
        ...

    def Remove(self, keyword: System.Object, ) -> None:
        ...

    def ToString(self, ) -> str:
        ...

    def GetAttributesFromCollection(self, collection: System.ComponentModel.AttributeCollection, ) -> System.Array[System.Attribute]:
        ...

    @typing.overload
    def GetProperties(self, ) -> System.ComponentModel.PropertyDescriptorCollection:
        ...

    @typing.overload
    def GetProperties(self, propertyDescriptors: System.Collections.Hashtable, ) -> None:
        ...

    @typing.overload
    def GetProperties(self, attributes: System.Array[System.Attribute], ) -> System.ComponentModel.PropertyDescriptorCollection:
        ...

    def GetClassName(self, ) -> str:
        ...

    def GetComponentName(self, ) -> str:
        ...

    def GetAttributes(self, ) -> System.ComponentModel.AttributeCollection:
        ...

    def GetEditor(self, editorBaseType: System.Type, ) -> System.Object:
        ...

    def GetConverter(self, ) -> System.ComponentModel.TypeConverter:
        ...

    def GetDefaultProperty(self, ) -> System.ComponentModel.PropertyDescriptor:
        ...

    @typing.overload
    def GetProperties(self, ) -> System.ComponentModel.PropertyDescriptorCollection:
        ...

    @typing.overload
    def GetProperties(self, attributes: System.Array[System.Attribute], ) -> System.ComponentModel.PropertyDescriptorCollection:
        ...

    def GetDefaultEvent(self, ) -> System.ComponentModel.EventDescriptor:
        ...

    @typing.overload
    def GetEvents(self, ) -> System.ComponentModel.EventDescriptorCollection:
        ...

    @typing.overload
    def GetEvents(self, attributes: System.Array[System.Attribute], ) -> System.ComponentModel.EventDescriptorCollection:
        ...

    def GetPropertyOwner(self, pd: System.ComponentModel.PropertyDescriptor, ) -> System.Object:
        ...

class DbBatch(System.IDisposable, System.IAsyncDisposable, System.Object, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def BatchCommands(self) -> System.Data.Common.DbBatchCommandCollection:
        ...

    @property
    @abc.abstractmethod
    def DbBatchCommands(self) -> System.Data.Common.DbBatchCommandCollection:
        ...

    @property
    @abc.abstractmethod
    def Timeout(self) -> int:
        ...
    @Timeout.setter
    @abc.abstractmethod
    def Timeout(self, val: int):
        ...

    @property
    def Connection(self) -> System.Data.Common.DbConnection:
        ...
    @Connection.setter
    def Connection(self, val: System.Data.Common.DbConnection):
        ...

    @property
    @abc.abstractmethod
    def DbConnection(self) -> System.Data.Common.DbConnection:
        ...
    @DbConnection.setter
    @abc.abstractmethod
    def DbConnection(self, val: System.Data.Common.DbConnection):
        ...

    @property
    def Transaction(self) -> System.Data.Common.DbTransaction:
        ...
    @Transaction.setter
    def Transaction(self, val: System.Data.Common.DbTransaction):
        ...

    @property
    @abc.abstractmethod
    def DbTransaction(self) -> System.Data.Common.DbTransaction:
        ...
    @DbTransaction.setter
    @abc.abstractmethod
    def DbTransaction(self, val: System.Data.Common.DbTransaction):
        ...

    # methods
    def __init__(self, ):
        ...

    def ExecuteReader(self, behavior: int = ..., ) -> System.Data.Common.DbDataReader:
        ...

    @abc.abstractmethod
    def ExecuteDbDataReader(self, behavior: int, ) -> System.Data.Common.DbDataReader:
        ...

    @typing.overload
    def ExecuteReaderAsync(self, cancellationToken: System.Threading.CancellationToken = ..., ) -> System.Threading.Tasks.Task[System.Data.Common.DbDataReader]:
        ...

    @typing.overload
    def ExecuteReaderAsync(self, behavior: int, cancellationToken: System.Threading.CancellationToken = ..., ) -> System.Threading.Tasks.Task[System.Data.Common.DbDataReader]:
        ...

    @abc.abstractmethod
    def ExecuteDbDataReaderAsync(self, behavior: int, cancellationToken: System.Threading.CancellationToken, ) -> System.Threading.Tasks.Task[System.Data.Common.DbDataReader]:
        ...

    @abc.abstractmethod
    def ExecuteNonQuery(self, ) -> int:
        ...

    @abc.abstractmethod
    def ExecuteNonQueryAsync(self, cancellationToken: System.Threading.CancellationToken = ..., ) -> System.Threading.Tasks.Task[int]:
        ...

    @abc.abstractmethod
    def ExecuteScalar(self, ) -> System.Object:
        ...

    @abc.abstractmethod
    def ExecuteScalarAsync(self, cancellationToken: System.Threading.CancellationToken = ..., ) -> System.Threading.Tasks.Task[System.Object]:
        ...

    @abc.abstractmethod
    def Prepare(self, ) -> None:
        ...

    @abc.abstractmethod
    def PrepareAsync(self, cancellationToken: System.Threading.CancellationToken = ..., ) -> System.Threading.Tasks.Task:
        ...

    @abc.abstractmethod
    def Cancel(self, ) -> None:
        ...

    def CreateBatchCommand(self, ) -> System.Data.Common.DbBatchCommand:
        ...

    @abc.abstractmethod
    def CreateDbBatchCommand(self, ) -> System.Data.Common.DbBatchCommand:
        ...

    def Dispose(self, ) -> None:
        ...

    def DisposeAsync(self, ) -> System.Threading.Tasks.ValueTask:
        ...

class DbCommand(System.ComponentModel.IComponent, System.IDisposable, System.Data.IDbCommand, System.IAsyncDisposable, System.ComponentModel.Component, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    @abc.abstractmethod
    def CommandText(self) -> str:
        ...
    @CommandText.setter
    @abc.abstractmethod
    def CommandText(self, val: str):
        ...

    @property
    @abc.abstractmethod
    def CommandTimeout(self) -> int:
        ...
    @CommandTimeout.setter
    @abc.abstractmethod
    def CommandTimeout(self, val: int):
        ...

    @property
    @abc.abstractmethod
    def CommandType(self) -> int:
        ...
    @CommandType.setter
    @abc.abstractmethod
    def CommandType(self, val: int):
        ...

    @property
    def Connection(self) -> System.Data.Common.DbConnection:
        ...
    @Connection.setter
    def Connection(self, val: System.Data.Common.DbConnection):
        ...

    @property
    def Connection(self) -> System.Data.IDbConnection:
        ...
    @Connection.setter
    def Connection(self, val: System.Data.IDbConnection):
        ...

    @property
    @abc.abstractmethod
    def DbConnection(self) -> System.Data.Common.DbConnection:
        ...
    @DbConnection.setter
    @abc.abstractmethod
    def DbConnection(self, val: System.Data.Common.DbConnection):
        ...

    @property
    @abc.abstractmethod
    def DbParameterCollection(self) -> System.Data.Common.DbParameterCollection:
        ...

    @property
    @abc.abstractmethod
    def DbTransaction(self) -> System.Data.Common.DbTransaction:
        ...
    @DbTransaction.setter
    @abc.abstractmethod
    def DbTransaction(self, val: System.Data.Common.DbTransaction):
        ...

    @property
    @abc.abstractmethod
    def DesignTimeVisible(self) -> bool:
        ...
    @DesignTimeVisible.setter
    @abc.abstractmethod
    def DesignTimeVisible(self, val: bool):
        ...

    @property
    def Parameters(self) -> System.Data.Common.DbParameterCollection:
        ...

    @property
    def Parameters(self) -> System.Data.IDataParameterCollection:
        ...

    @property
    def Transaction(self) -> System.Data.Common.DbTransaction:
        ...
    @Transaction.setter
    def Transaction(self, val: System.Data.Common.DbTransaction):
        ...

    @property
    def Transaction(self) -> System.Data.IDbTransaction:
        ...
    @Transaction.setter
    def Transaction(self, val: System.Data.IDbTransaction):
        ...

    @property
    @abc.abstractmethod
    def UpdatedRowSource(self) -> int:
        ...
    @UpdatedRowSource.setter
    @abc.abstractmethod
    def UpdatedRowSource(self, val: int):
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
    def __init__(self, ):
        ...

    @abc.abstractmethod
    def CreateDbParameter(self, ) -> System.Data.Common.DbParameter:
        ...

    @abc.abstractmethod
    def Prepare(self, ) -> None:
        ...

    @abc.abstractmethod
    def ExecuteDbDataReader(self, behavior: int, ) -> System.Data.Common.DbDataReader:
        ...

    def ExecuteDbDataReaderAsync(self, behavior: int, cancellationToken: System.Threading.CancellationToken, ) -> System.Threading.Tasks.Task[System.Data.Common.DbDataReader]:
        ...

    @abc.abstractmethod
    def ExecuteNonQuery(self, ) -> int:
        ...

    @abc.abstractmethod
    def ExecuteScalar(self, ) -> System.Object:
        ...

    @abc.abstractmethod
    def Cancel(self, ) -> None:
        ...

    def CancelIgnoreFailure(self, ) -> None:
        ...

    def CreateParameter(self, ) -> System.Data.Common.DbParameter:
        ...

    def CreateParameter(self, ) -> System.Data.IDbDataParameter:
        ...

    @typing.overload
    def ExecuteReader(self, ) -> System.Data.Common.DbDataReader:
        ...

    @typing.overload
    def ExecuteReader(self, behavior: int, ) -> System.Data.Common.DbDataReader:
        ...

    @typing.overload
    def ExecuteReader(self, ) -> System.Data.IDataReader:
        ...

    @typing.overload
    def ExecuteReader(self, behavior: int, ) -> System.Data.IDataReader:
        ...

    @typing.overload
    def ExecuteNonQueryAsync(self, ) -> System.Threading.Tasks.Task[int]:
        ...

    @typing.overload
    def ExecuteNonQueryAsync(self, cancellationToken: System.Threading.CancellationToken, ) -> System.Threading.Tasks.Task[int]:
        ...

    @typing.overload
    def ExecuteReaderAsync(self, ) -> System.Threading.Tasks.Task[System.Data.Common.DbDataReader]:
        ...

    @typing.overload
    def ExecuteReaderAsync(self, cancellationToken: System.Threading.CancellationToken, ) -> System.Threading.Tasks.Task[System.Data.Common.DbDataReader]:
        ...

    @typing.overload
    def ExecuteReaderAsync(self, behavior: int, ) -> System.Threading.Tasks.Task[System.Data.Common.DbDataReader]:
        ...

    @typing.overload
    def ExecuteReaderAsync(self, behavior: int, cancellationToken: System.Threading.CancellationToken, ) -> System.Threading.Tasks.Task[System.Data.Common.DbDataReader]:
        ...

    @typing.overload
    def ExecuteScalarAsync(self, ) -> System.Threading.Tasks.Task[System.Object]:
        ...

    @typing.overload
    def ExecuteScalarAsync(self, cancellationToken: System.Threading.CancellationToken, ) -> System.Threading.Tasks.Task[System.Object]:
        ...

    def PrepareAsync(self, cancellationToken: System.Threading.CancellationToken = ..., ) -> System.Threading.Tasks.Task:
        ...

    def DisposeAsync(self, ) -> System.Threading.Tasks.ValueTask:
        ...

class DbDataAdapter(System.ComponentModel.IComponent, System.IDisposable, System.Data.IDataAdapter, System.Data.IDbDataAdapter, System.ICloneable, System.Data.Common.DataAdapter, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        self._objectID: int
        ...

    # static fields
    s_parameterValueNonNullValue: System.Object = ...
    s_parameterValueNullValue: System.Object = ...
    DefaultSourceTableName: str = ...

    # properties
    @property
    def _IDbDataAdapter(self) -> System.Data.IDbDataAdapter:
        ...

    @property
    def DeleteCommand(self) -> System.Data.Common.DbCommand:
        ...
    @DeleteCommand.setter
    def DeleteCommand(self, val: System.Data.Common.DbCommand):
        ...

    @property
    def DeleteCommand(self) -> System.Data.IDbCommand:
        ...
    @DeleteCommand.setter
    def DeleteCommand(self, val: System.Data.IDbCommand):
        ...

    @property
    def FillCommandBehavior(self) -> int:
        ...
    @FillCommandBehavior.setter
    def FillCommandBehavior(self, val: int):
        ...

    @property
    def InsertCommand(self) -> System.Data.Common.DbCommand:
        ...
    @InsertCommand.setter
    def InsertCommand(self, val: System.Data.Common.DbCommand):
        ...

    @property
    def InsertCommand(self) -> System.Data.IDbCommand:
        ...
    @InsertCommand.setter
    def InsertCommand(self, val: System.Data.IDbCommand):
        ...

    @property
    def SelectCommand(self) -> System.Data.Common.DbCommand:
        ...
    @SelectCommand.setter
    def SelectCommand(self, val: System.Data.Common.DbCommand):
        ...

    @property
    def SelectCommand(self) -> System.Data.IDbCommand:
        ...
    @SelectCommand.setter
    def SelectCommand(self, val: System.Data.IDbCommand):
        ...

    @property
    def UpdateBatchSize(self) -> int:
        ...
    @UpdateBatchSize.setter
    def UpdateBatchSize(self, val: int):
        ...

    @property
    def UpdateCommand(self) -> System.Data.Common.DbCommand:
        ...
    @UpdateCommand.setter
    def UpdateCommand(self, val: System.Data.Common.DbCommand):
        ...

    @property
    def UpdateCommand(self) -> System.Data.IDbCommand:
        ...
    @UpdateCommand.setter
    def UpdateCommand(self, val: System.Data.IDbCommand):
        ...

    @property
    def UpdateMappingAction(self) -> int:
        ...

    @property
    def UpdateSchemaAction(self) -> int:
        ...

    @property
    def AcceptChangesDuringFill(self) -> bool:
        ...
    @AcceptChangesDuringFill.setter
    def AcceptChangesDuringFill(self, val: bool):
        ...

    @property
    def AcceptChangesDuringUpdate(self) -> bool:
        ...
    @AcceptChangesDuringUpdate.setter
    def AcceptChangesDuringUpdate(self, val: bool):
        ...

    @property
    def ContinueUpdateOnError(self) -> bool:
        ...
    @ContinueUpdateOnError.setter
    def ContinueUpdateOnError(self, val: bool):
        ...

    @property
    def FillLoadOption(self) -> int:
        ...
    @FillLoadOption.setter
    def FillLoadOption(self, val: int):
        ...

    @property
    def MissingMappingAction(self) -> int:
        ...
    @MissingMappingAction.setter
    def MissingMappingAction(self, val: int):
        ...

    @property
    def MissingSchemaAction(self) -> int:
        ...
    @MissingSchemaAction.setter
    def MissingSchemaAction(self, val: int):
        ...

    @property
    def ObjectID(self) -> int:
        ...

    @property
    def ReturnProviderSpecificTypes(self) -> bool:
        ...
    @ReturnProviderSpecificTypes.setter
    def ReturnProviderSpecificTypes(self, val: bool):
        ...

    @property
    def TableMappings(self) -> System.Data.Common.DataTableMappingCollection:
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
    def __init__(self, adapter: System.Data.Common.DbDataAdapter, ):
        ...

    def AddToBatch(self, command: System.Data.IDbCommand, ) -> int:
        ...

    def ClearBatch(self, ) -> None:
        ...

    def Clone(self, ) -> System.Object:
        ...

    def CloneFrom(self, from_: System.Data.Common.DbDataAdapter, ) -> None:
        ...

    def CloneCommand(self, command: System.Data.IDbCommand, ) -> System.Data.IDbCommand:
        ...

    def CreateRowUpdatedEvent(self, dataRow: System.Data.DataRow, command: System.Data.IDbCommand, statementType: int, tableMapping: System.Data.Common.DataTableMapping, ) -> System.Data.Common.RowUpdatedEventArgs:
        ...

    def CreateRowUpdatingEvent(self, dataRow: System.Data.DataRow, command: System.Data.IDbCommand, statementType: int, tableMapping: System.Data.Common.DataTableMapping, ) -> System.Data.Common.RowUpdatingEventArgs:
        ...

    def Dispose(self, disposing: bool, ) -> None:
        ...

    def ExecuteBatch(self, ) -> int:
        ...

    @typing.overload
    def FillSchema(self, dataTable: System.Data.DataTable, schemaType: int, ) -> System.Data.DataTable:
        ...

    @typing.overload
    def FillSchema(self, dataSet: System.Data.DataSet, schemaType: int, ) -> System.Array[System.Data.DataTable]:
        ...

    @typing.overload
    def FillSchema(self, dataSet: System.Data.DataSet, schemaType: int, srcTable: str, ) -> System.Array[System.Data.DataTable]:
        ...

    @typing.overload
    def FillSchema(self, dataSet: System.Data.DataSet, schemaType: int, command: System.Data.IDbCommand, srcTable: str, behavior: int, ) -> System.Array[System.Data.DataTable]:
        ...

    @typing.overload
    def FillSchema(self, dataTable: System.Data.DataTable, schemaType: int, command: System.Data.IDbCommand, behavior: int, ) -> System.Data.DataTable:
        ...

    def FillSchemaInternal(self, dataset: System.Data.DataSet, datatable: System.Data.DataTable, schemaType: int, command: System.Data.IDbCommand, srcTable: str, behavior: int, ) -> System.Object:
        ...

    @typing.overload
    def Fill(self, dataSet: System.Data.DataSet, ) -> int:
        ...

    @typing.overload
    def Fill(self, dataSet: System.Data.DataSet, srcTable: str, ) -> int:
        ...

    @typing.overload
    def Fill(self, dataSet: System.Data.DataSet, startRecord: int, maxRecords: int, srcTable: str, ) -> int:
        ...

    @typing.overload
    def Fill(self, dataSet: System.Data.DataSet, startRecord: int, maxRecords: int, srcTable: str, command: System.Data.IDbCommand, behavior: int, ) -> int:
        ...

    @typing.overload
    def Fill(self, dataTable: System.Data.DataTable, ) -> int:
        ...

    @typing.overload
    def Fill(self, startRecord: int, maxRecords: int, dataTables: System.Array[System.Data.DataTable], ) -> int:
        ...

    @typing.overload
    def Fill(self, dataTable: System.Data.DataTable, command: System.Data.IDbCommand, behavior: int, ) -> int:
        ...

    @typing.overload
    def Fill(self, dataTables: System.Array[System.Data.DataTable], startRecord: int, maxRecords: int, command: System.Data.IDbCommand, behavior: int, ) -> int:
        ...

    def FillInternal(self, dataset: System.Data.DataSet, datatables: System.Array[System.Data.DataTable], startRecord: int, maxRecords: int, srcTable: str, command: System.Data.IDbCommand, behavior: int, ) -> int:
        ...

    def GetBatchedParameter(self, commandIdentifier: int, parameterIndex: int, ) -> System.Data.IDataParameter:
        ...

    def GetBatchedRecordsAffected(self, commandIdentifier: int, recordsAffected: ref[int], error: ref[System.Exception], ) -> bool:
        ...

    def GetFillParameters(self, ) -> System.Array[System.Data.IDataParameter]:
        ...

    def GetTableMapping(self, dataTable: System.Data.DataTable, ) -> System.Data.Common.DataTableMapping:
        ...

    def InitializeBatching(self, ) -> None:
        ...

    def OnRowUpdated(self, value: System.Data.Common.RowUpdatedEventArgs, ) -> None:
        ...

    def OnRowUpdating(self, value: System.Data.Common.RowUpdatingEventArgs, ) -> None:
        ...

    def ParameterInput(self, parameters: System.Data.IDataParameterCollection, typeIndex: int, row: System.Data.DataRow, mappings: System.Data.Common.DataTableMapping, ) -> None:
        ...

    @typing.overload
    def ParameterOutput(self, parameter: System.Data.IDataParameter, row: System.Data.DataRow, mappings: System.Data.Common.DataTableMapping, missingMapping: int, missingSchema: int, ) -> None:
        ...

    @typing.overload
    def ParameterOutput(self, parameters: System.Data.IDataParameterCollection, row: System.Data.DataRow, mappings: System.Data.Common.DataTableMapping, ) -> None:
        ...

    def TerminateBatching(self, ) -> None:
        ...

    @typing.overload
    def Update(self, dataSet: System.Data.DataSet, ) -> int:
        ...

    @typing.overload
    def Update(self, dataRows: System.Array[System.Data.DataRow], ) -> int:
        ...

    @typing.overload
    def Update(self, dataTable: System.Data.DataTable, ) -> int:
        ...

    @typing.overload
    def Update(self, dataSet: System.Data.DataSet, srcTable: str, ) -> int:
        ...

    @typing.overload
    def Update(self, dataRows: System.Array[System.Data.DataRow], tableMapping: System.Data.Common.DataTableMapping, ) -> int:
        ...

    def UpdateBatchExecute(self, batchCommands: System.Array[System.Data.Common.DbDataAdapter.BatchCommandInfo], commandCount: int, rowUpdatedEvent: System.Data.Common.RowUpdatedEventArgs, ) -> None:
        ...

    def UpdateConnectionOpen(self, connection: System.Data.IDbConnection, statementType: int, connections: System.Array[System.Data.IDbConnection], connectionStates: System.Array[int], useSelectConnectionState: bool, ) -> int:
        ...

    def UpdateFromDataTable(self, dataTable: System.Data.DataTable, tableMapping: System.Data.Common.DataTableMapping, ) -> int:
        ...

    def UpdateRowExecute(self, rowUpdatedEvent: System.Data.Common.RowUpdatedEventArgs, dataCommand: System.Data.IDbCommand, cmdIndex: int, ) -> None:
        ...

    def UpdatedRowStatus(self, rowUpdatedEvent: System.Data.Common.RowUpdatedEventArgs, batchCommands: System.Array[System.Data.Common.DbDataAdapter.BatchCommandInfo], commandCount: int, ) -> int:
        ...

    def UpdatedRowStatusContinue(self, rowUpdatedEvent: System.Data.Common.RowUpdatedEventArgs, batchCommands: System.Array[System.Data.Common.DbDataAdapter.BatchCommandInfo], commandCount: int, ) -> int:
        ...

    def UpdatedRowStatusErrors(self, rowUpdatedEvent: System.Data.Common.RowUpdatedEventArgs, batchCommands: System.Array[System.Data.Common.DbDataAdapter.BatchCommandInfo], commandCount: int, ) -> int:
        ...

    def UpdatedRowStatusSkip(self, batchCommands: System.Array[System.Data.Common.DbDataAdapter.BatchCommandInfo], commandCount: int, ) -> int:
        ...

    def UpdatingRowStatusErrors(self, rowUpdatedEvent: System.Data.Common.RowUpdatingEventArgs, dataRow: System.Data.DataRow, ) -> None:
        ...

    @staticmethod
    def GetConnection1(adapter: System.Data.Common.DbDataAdapter, ) -> System.Data.IDbConnection:
        ...

    @staticmethod
    def GetConnection3(adapter: System.Data.Common.DbDataAdapter, command: System.Data.IDbCommand, method: str, ) -> System.Data.IDbConnection:
        ...

    @staticmethod
    def GetConnection4(adapter: System.Data.Common.DbDataAdapter, command: System.Data.IDbCommand, statementType: int, isCommandFromRowUpdating: bool, ) -> System.Data.IDbConnection:
        ...

    @staticmethod
    def GetParameterSourceVersion(statementType: int, parameter: System.Data.IDataParameter, ) -> int:
        ...

    @staticmethod
    def QuietClose(connection: System.Data.IDbConnection, originalState: int, ) -> None:
        ...

    @staticmethod
    def QuietOpen(connection: System.Data.IDbConnection, originalState: ref[int], ) -> None:
        ...

class DataAdapter(System.ComponentModel.IComponent, System.IDisposable, System.Data.IDataAdapter, System.ComponentModel.Component):
    @typing.overload
    def __init__(self, **kwargs):
        self._objectID: int
        ...

    # static fields

    # properties
    @property
    def AcceptChangesDuringFill(self) -> bool:
        ...
    @AcceptChangesDuringFill.setter
    def AcceptChangesDuringFill(self, val: bool):
        ...

    @property
    def AcceptChangesDuringUpdate(self) -> bool:
        ...
    @AcceptChangesDuringUpdate.setter
    def AcceptChangesDuringUpdate(self, val: bool):
        ...

    @property
    def ContinueUpdateOnError(self) -> bool:
        ...
    @ContinueUpdateOnError.setter
    def ContinueUpdateOnError(self, val: bool):
        ...

    @property
    def FillLoadOption(self) -> int:
        ...
    @FillLoadOption.setter
    def FillLoadOption(self, val: int):
        ...

    @property
    def MissingMappingAction(self) -> int:
        ...
    @MissingMappingAction.setter
    def MissingMappingAction(self, val: int):
        ...

    @property
    def MissingSchemaAction(self) -> int:
        ...
    @MissingSchemaAction.setter
    def MissingSchemaAction(self, val: int):
        ...

    @property
    def ObjectID(self) -> int:
        ...

    @property
    def ReturnProviderSpecificTypes(self) -> bool:
        ...
    @ReturnProviderSpecificTypes.setter
    def ReturnProviderSpecificTypes(self, val: bool):
        ...

    @property
    def TableMappings(self) -> System.Data.Common.DataTableMappingCollection:
        ...

    @property
    def TableMappings(self) -> System.Data.ITableMappingCollection:
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
    def __init__(self, from_: System.Data.Common.DataAdapter, ):
        ...

    def Dispose(self, disposing: bool, ) -> None:
        ...

    @typing.overload
    def FillSchema(self, dataSet: System.Data.DataSet, schemaType: int, ) -> System.Array[System.Data.DataTable]:
        ...

    @typing.overload
    def FillSchema(self, dataSet: System.Data.DataSet, schemaType: int, srcTable: str, dataReader: System.Data.IDataReader, ) -> System.Array[System.Data.DataTable]:
        ...

    @typing.overload
    def FillSchema(self, dataTable: System.Data.DataTable, schemaType: int, dataReader: System.Data.IDataReader, ) -> System.Data.DataTable:
        ...

    @typing.overload
    def Fill(self, dataSet: System.Data.DataSet, ) -> int:
        ...

    @typing.overload
    def Fill(self, dataSet: System.Data.DataSet, srcTable: str, dataReader: System.Data.IDataReader, startRecord: int, maxRecords: int, ) -> int:
        ...

    @typing.overload
    def Fill(self, dataTable: System.Data.DataTable, dataReader: System.Data.IDataReader, ) -> int:
        ...

    @typing.overload
    def Fill(self, dataTables: System.Array[System.Data.DataTable], dataReader: System.Data.IDataReader, startRecord: int, maxRecords: int, ) -> int:
        ...

    def GetFillParameters(self, ) -> System.Array[System.Data.IDataParameter]:
        ...

    def Update(self, dataSet: System.Data.DataSet, ) -> int:
        ...

    def ShouldSerializeAcceptChangesDuringFill(self, ) -> bool:
        ...

    def ResetFillLoadOption(self, ) -> None:
        ...

    def ShouldSerializeFillLoadOption(self, ) -> bool:
        ...

    def ShouldSerializeTableMappings(self, ) -> bool:
        ...

    def HasTableMappings(self, ) -> bool:
        ...

    def CloneInternals(self, ) -> System.Data.Common.DataAdapter:
        ...

    def CloneFrom(self, from_: System.Data.Common.DataAdapter, ) -> None:
        ...

    def CreateTableMappings(self, ) -> System.Data.Common.DataTableMappingCollection:
        ...

    def FillSchemaFromReader(self, dataset: System.Data.DataSet, datatable: System.Data.DataTable, schemaType: int, srcTable: str, dataReader: System.Data.IDataReader, ) -> System.Object:
        ...

    @typing.overload
    def FillFromReader(self, dataset: System.Data.DataSet, datatable: System.Data.DataTable, srcTable: str, dataReader: System.Data.ProviderBase.DataReaderContainer, startRecord: int, maxRecords: int, ) -> int:
        ...

    @typing.overload
    def FillFromReader(self, dataset: System.Data.DataSet, datatable: System.Data.DataTable, srcTable: str, dataReader: System.Data.ProviderBase.DataReaderContainer, startRecord: int, maxRecords: int, parentChapterColumn: System.Data.DataColumn, parentChapterValue: System.Object, ) -> int:
        ...

    def FillLoadDataRowChunk(self, mapping: System.Data.ProviderBase.SchemaMapping, startRecord: int, maxRecords: int, ) -> int:
        ...

    def FillLoadDataRow(self, mapping: System.Data.ProviderBase.SchemaMapping, ) -> int:
        ...

    def FillMappingInternal(self, dataset: System.Data.DataSet, datatable: System.Data.DataTable, srcTable: str, dataReader: System.Data.ProviderBase.DataReaderContainer, schemaCount: int, parentChapterColumn: System.Data.DataColumn, parentChapterValue: System.Object, ) -> System.Data.ProviderBase.SchemaMapping:
        ...

    def FillMapping(self, dataset: System.Data.DataSet, datatable: System.Data.DataTable, srcTable: str, dataReader: System.Data.ProviderBase.DataReaderContainer, schemaCount: int, parentChapterColumn: System.Data.DataColumn, parentChapterValue: System.Object, ) -> System.Data.ProviderBase.SchemaMapping:
        ...

    def FillNextResult(self, dataReader: System.Data.ProviderBase.DataReaderContainer, ) -> bool:
        ...

    def GetTableMappingBySchemaAction(self, sourceTableName: str, dataSetTableName: str, mappingAction: int, ) -> System.Data.Common.DataTableMapping:
        ...

    def IndexOfDataSetTable(self, dataSetTable: str, ) -> int:
        ...

    def OnFillError(self, value: System.Data.FillErrorEventArgs, ) -> None:
        ...

    def OnFillErrorHandler(self, e: System.Exception, dataTable: System.Data.DataTable, dataValues: System.Array[System.Object], ) -> None:
        ...

    @staticmethod
    def AddDataTableToArray(tables: System.Array[System.Data.DataTable], newTable: System.Data.DataTable, ) -> System.Array[System.Data.DataTable]:
        ...

    @staticmethod
    def GetSourceTableName(srcTable: str, index: int, ) -> str:
        ...

class DataTableMappingCollection(System.Data.ITableMappingCollection, System.Collections.IList, System.Collections.ICollection, System.Collections.IEnumerable, System.MarshalByRefObject):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def IsSynchronized(self) -> bool:
        ...

    @property
    def SyncRoot(self) -> System.Object:
        ...

    @property
    def IsReadOnly(self) -> bool:
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
    def Item(self) -> System.Object:
        ...
    @Item.setter
    def Item(self, val: System.Object):
        ...

    @property
    def Count(self) -> int:
        ...

    @property
    def ItemType(self) -> System.Type:
        ...

    @property
    def Item(self) -> System.Data.Common.DataTableMapping:
        ...
    @Item.setter
    def Item(self, val: System.Data.Common.DataTableMapping):
        ...

    @property
    def Item(self) -> System.Data.Common.DataTableMapping:
        ...
    @Item.setter
    def Item(self, val: System.Data.Common.DataTableMapping):
        ...

    # methods
    def __init__(self, ):
        ...

    def Add(self, sourceTableName: str, dataSetTableName: str, ) -> System.Data.ITableMapping:
        ...

    def GetByDataSetTable(self, dataSetTableName: str, ) -> System.Data.ITableMapping:
        ...

    @typing.overload
    def Add(self, value: System.Object, ) -> int:
        ...

    @typing.overload
    def Add(self, value: System.Data.Common.DataTableMapping, ) -> System.Data.Common.DataTableMapping:
        ...

    @typing.overload
    def Add(self, sourceTable: str, dataSetTable: str, ) -> System.Data.Common.DataTableMapping:
        ...

    @typing.overload
    def AddRange(self, values: System.Array[System.Data.Common.DataTableMapping], ) -> None:
        ...

    @typing.overload
    def AddRange(self, values: System.Array, ) -> None:
        ...

    def AddEnumerableRange(self, values: System.Collections.IEnumerable, doClone: bool, ) -> None:
        ...

    def AddWithoutEvents(self, value: System.Data.Common.DataTableMapping, ) -> None:
        ...

    def ArrayList(self, ) -> System.Collections.Generic.List[System.Data.Common.DataTableMapping]:
        ...

    def Clear(self, ) -> None:
        ...

    def ClearWithoutEvents(self, ) -> None:
        ...

    @typing.overload
    def Contains(self, value: str, ) -> bool:
        ...

    @typing.overload
    def Contains(self, value: System.Object, ) -> bool:
        ...

    @typing.overload
    def CopyTo(self, array: System.Array, index: int, ) -> None:
        ...

    @typing.overload
    def CopyTo(self, array: System.Array[System.Data.Common.DataTableMapping], index: int, ) -> None:
        ...

    def GetByDataSetTable(self, dataSetTable: str, ) -> System.Data.Common.DataTableMapping:
        ...

    def GetEnumerator(self, ) -> System.Collections.IEnumerator:
        ...

    @typing.overload
    def IndexOf(self, value: System.Object, ) -> int:
        ...

    @typing.overload
    def IndexOf(self, sourceTable: str, ) -> int:
        ...

    def IndexOfDataSetTable(self, dataSetTable: str, ) -> int:
        ...

    @typing.overload
    def Insert(self, index: int, value: System.Object, ) -> None:
        ...

    @typing.overload
    def Insert(self, index: int, value: System.Data.Common.DataTableMapping, ) -> None:
        ...

    @typing.overload
    def RangeCheck(self, index: int, ) -> None:
        ...

    @typing.overload
    def RangeCheck(self, sourceTable: str, ) -> int:
        ...

    @typing.overload
    def RemoveAt(self, index: int, ) -> None:
        ...

    @typing.overload
    def RemoveAt(self, sourceTable: str, ) -> None:
        ...

    def RemoveIndex(self, index: int, ) -> None:
        ...

    @typing.overload
    def Remove(self, value: System.Object, ) -> None:
        ...

    @typing.overload
    def Remove(self, value: System.Data.Common.DataTableMapping, ) -> None:
        ...

    def Replace(self, index: int, newValue: System.Data.Common.DataTableMapping, ) -> None:
        ...

    def ValidateType(self, value: System.Object, ) -> None:
        ...

    def Validate(self, index: int, value: System.Data.Common.DataTableMapping, ) -> None:
        ...

    def ValidateSourceTable(self, index: int, value: str, ) -> None:
        ...

    @staticmethod
    def GetTableMappingBySchemaAction(tableMappings: System.Data.Common.DataTableMappingCollection, sourceTable: str, dataSetTable: str, mappingAction: int, ) -> System.Data.Common.DataTableMapping:
        ...

class RowUpdatedEventArgs(System.EventArgs):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def Command(self) -> System.Data.IDbCommand:
        ...

    @property
    def Errors(self) -> System.Exception:
        ...
    @Errors.setter
    def Errors(self, val: System.Exception):
        ...

    @property
    def RecordsAffected(self) -> int:
        ...

    @property
    def Row(self) -> System.Data.DataRow:
        ...

    @property
    def Rows(self) -> System.Array[System.Data.DataRow]:
        ...

    @property
    def RowCount(self) -> int:
        ...

    @property
    def StatementType(self) -> int:
        ...

    @property
    def Status(self) -> int:
        ...
    @Status.setter
    def Status(self, val: int):
        ...

    @property
    def TableMapping(self) -> System.Data.Common.DataTableMapping:
        ...

    # methods
    def __init__(self, dataRow: System.Data.DataRow, command: System.Data.IDbCommand, statementType: int, tableMapping: System.Data.Common.DataTableMapping, ):
        ...

    @typing.overload
    def AdapterInit(self, dataRows: System.Array[System.Data.DataRow], ) -> None:
        ...

    @typing.overload
    def AdapterInit(self, recordsAffected: int, ) -> None:
        ...

    @typing.overload
    def CopyToRows(self, array: System.Array[System.Data.DataRow], ) -> None:
        ...

    @typing.overload
    def CopyToRows(self, array: System.Array[System.Data.DataRow], arrayIndex: int, ) -> None:
        ...

class DbBatchCommandCollection(System.Collections.Generic.IList[System.Data.Common.DbBatchCommand], System.Collections.Generic.ICollection[System.Data.Common.DbBatchCommand], System.Collections.Generic.IEnumerable[System.Data.Common.DbBatchCommand], System.Collections.IEnumerable, System.Object, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    @abc.abstractmethod
    def Count(self) -> int:
        ...

    @property
    @abc.abstractmethod
    def IsReadOnly(self) -> bool:
        ...

    @property
    def Item(self) -> System.Data.Common.DbBatchCommand:
        ...
    @Item.setter
    def Item(self, val: System.Data.Common.DbBatchCommand):
        ...

    # methods
    def __init__(self, ):
        ...

    @abc.abstractmethod
    def GetEnumerator(self, ) -> System.Collections.Generic.IEnumerator[System.Data.Common.DbBatchCommand]:
        ...

    def GetEnumerator(self, ) -> System.Collections.IEnumerator:
        ...

    @abc.abstractmethod
    def Add(self, item: System.Data.Common.DbBatchCommand, ) -> None:
        ...

    @abc.abstractmethod
    def Clear(self, ) -> None:
        ...

    @abc.abstractmethod
    def Contains(self, item: System.Data.Common.DbBatchCommand, ) -> bool:
        ...

    @abc.abstractmethod
    def CopyTo(self, array: System.Array[System.Data.Common.DbBatchCommand], arrayIndex: int, ) -> None:
        ...

    @abc.abstractmethod
    def Remove(self, item: System.Data.Common.DbBatchCommand, ) -> bool:
        ...

    @abc.abstractmethod
    def IndexOf(self, item: System.Data.Common.DbBatchCommand, ) -> int:
        ...

    @abc.abstractmethod
    def Insert(self, index: int, item: System.Data.Common.DbBatchCommand, ) -> None:
        ...

    @abc.abstractmethod
    def RemoveAt(self, index: int, ) -> None:
        ...

    @abc.abstractmethod
    def GetBatchCommand(self, index: int, ) -> System.Data.Common.DbBatchCommand:
        ...

    @abc.abstractmethod
    def SetBatchCommand(self, index: int, batchCommand: System.Data.Common.DbBatchCommand, ) -> None:
        ...

class DbDataSourceEnumerator(System.Object, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    def __init__(self, ):
        ...

    @abc.abstractmethod
    def GetDataSources(self, ) -> System.Data.DataTable:
        ...

class DataTableMapping(System.Data.ITableMapping, System.ICloneable, System.MarshalByRefObject):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def ColumnMappings(self) -> System.Data.IColumnMappingCollection:
        ...

    @property
    def ColumnMappings(self) -> System.Data.Common.DataColumnMappingCollection:
        ...

    @property
    def DataSetTable(self) -> str:
        ...
    @DataSetTable.setter
    def DataSetTable(self, val: str):
        ...

    @property
    def Parent(self) -> System.Data.Common.DataTableMappingCollection:
        ...
    @Parent.setter
    def Parent(self, val: System.Data.Common.DataTableMappingCollection):
        ...

    @property
    def SourceTable(self) -> str:
        ...
    @SourceTable.setter
    def SourceTable(self, val: str):
        ...

    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def __init__(self, sourceTable: str, dataSetTable: str, ):
        ...

    @typing.overload
    def __init__(self, sourceTable: str, dataSetTable: str, columnMappings: System.Array[System.Data.Common.DataColumnMapping], ):
        ...

    def Clone(self, ) -> System.Object:
        ...

    def GetDataColumn(self, sourceColumn: str, dataType: System.Type, dataTable: System.Data.DataTable, mappingAction: int, schemaAction: int, ) -> System.Data.DataColumn:
        ...

    def GetColumnMappingBySchemaAction(self, sourceColumn: str, mappingAction: int, ) -> System.Data.Common.DataColumnMapping:
        ...

    def GetDataTableBySchemaAction(self, dataSet: System.Data.DataSet, schemaAction: int, ) -> System.Data.DataTable:
        ...

    def ToString(self, ) -> str:
        ...

class DataColumnMappingCollection(System.Data.IColumnMappingCollection, System.Collections.IList, System.Collections.ICollection, System.Collections.IEnumerable, System.MarshalByRefObject):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def IsSynchronized(self) -> bool:
        ...

    @property
    def SyncRoot(self) -> System.Object:
        ...

    @property
    def IsReadOnly(self) -> bool:
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
    def Item(self) -> System.Object:
        ...
    @Item.setter
    def Item(self, val: System.Object):
        ...

    @property
    def Count(self) -> int:
        ...

    @property
    def ItemType(self) -> System.Type:
        ...

    @property
    def Item(self) -> System.Data.Common.DataColumnMapping:
        ...
    @Item.setter
    def Item(self, val: System.Data.Common.DataColumnMapping):
        ...

    @property
    def Item(self) -> System.Data.Common.DataColumnMapping:
        ...
    @Item.setter
    def Item(self, val: System.Data.Common.DataColumnMapping):
        ...

    # methods
    def __init__(self, ):
        ...

    def Add(self, sourceColumnName: str, dataSetColumnName: str, ) -> System.Data.IColumnMapping:
        ...

    def GetByDataSetColumn(self, dataSetColumnName: str, ) -> System.Data.IColumnMapping:
        ...

    @typing.overload
    def Add(self, value: System.Object, ) -> int:
        ...

    @typing.overload
    def Add(self, value: System.Data.Common.DataColumnMapping, ) -> System.Data.Common.DataColumnMapping:
        ...

    @typing.overload
    def Add(self, sourceColumn: str, dataSetColumn: str, ) -> System.Data.Common.DataColumnMapping:
        ...

    @typing.overload
    def AddRange(self, values: System.Array[System.Data.Common.DataColumnMapping], ) -> None:
        ...

    @typing.overload
    def AddRange(self, values: System.Array, ) -> None:
        ...

    def AddEnumerableRange(self, values: System.Collections.IEnumerable, doClone: bool, ) -> None:
        ...

    def AddWithoutEvents(self, value: System.Data.Common.DataColumnMapping, ) -> None:
        ...

    def ArrayList(self, ) -> System.Collections.Generic.List[System.Data.Common.DataColumnMapping]:
        ...

    def Clear(self, ) -> None:
        ...

    def ClearWithoutEvents(self, ) -> None:
        ...

    @typing.overload
    def Contains(self, value: str, ) -> bool:
        ...

    @typing.overload
    def Contains(self, value: System.Object, ) -> bool:
        ...

    @typing.overload
    def CopyTo(self, array: System.Array, index: int, ) -> None:
        ...

    @typing.overload
    def CopyTo(self, array: System.Array[System.Data.Common.DataColumnMapping], index: int, ) -> None:
        ...

    def GetByDataSetColumn(self, value: str, ) -> System.Data.Common.DataColumnMapping:
        ...

    def GetEnumerator(self, ) -> System.Collections.IEnumerator:
        ...

    @typing.overload
    def IndexOf(self, value: System.Object, ) -> int:
        ...

    @typing.overload
    def IndexOf(self, sourceColumn: str, ) -> int:
        ...

    def IndexOfDataSetColumn(self, dataSetColumn: str, ) -> int:
        ...

    @typing.overload
    def Insert(self, index: int, value: System.Object, ) -> None:
        ...

    @typing.overload
    def Insert(self, index: int, value: System.Data.Common.DataColumnMapping, ) -> None:
        ...

    @typing.overload
    def RangeCheck(self, index: int, ) -> None:
        ...

    @typing.overload
    def RangeCheck(self, sourceColumn: str, ) -> int:
        ...

    @typing.overload
    def RemoveAt(self, index: int, ) -> None:
        ...

    @typing.overload
    def RemoveAt(self, sourceColumn: str, ) -> None:
        ...

    def RemoveIndex(self, index: int, ) -> None:
        ...

    @typing.overload
    def Remove(self, value: System.Object, ) -> None:
        ...

    @typing.overload
    def Remove(self, value: System.Data.Common.DataColumnMapping, ) -> None:
        ...

    def Replace(self, index: int, newValue: System.Data.Common.DataColumnMapping, ) -> None:
        ...

    def ValidateType(self, value: System.Object, ) -> None:
        ...

    def Validate(self, index: int, value: System.Data.Common.DataColumnMapping, ) -> None:
        ...

    def ValidateSourceColumn(self, index: int, value: str, ) -> None:
        ...

    @staticmethod
    def GetDataColumn(columnMappings: System.Data.Common.DataColumnMappingCollection, sourceColumn: str, dataType: System.Type, dataTable: System.Data.DataTable, mappingAction: int, schemaAction: int, ) -> System.Data.DataColumn:
        ...

    @staticmethod
    def GetColumnMappingBySchemaAction(columnMappings: System.Data.Common.DataColumnMappingCollection, sourceColumn: str, mappingAction: int, ) -> System.Data.Common.DataColumnMapping:
        ...

class DataColumnMapping(System.Data.IColumnMapping, System.ICloneable, System.MarshalByRefObject):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def DataSetColumn(self) -> str:
        ...
    @DataSetColumn.setter
    def DataSetColumn(self, val: str):
        ...

    @property
    def Parent(self) -> System.Data.Common.DataColumnMappingCollection:
        ...
    @Parent.setter
    def Parent(self, val: System.Data.Common.DataColumnMappingCollection):
        ...

    @property
    def SourceColumn(self) -> str:
        ...
    @SourceColumn.setter
    def SourceColumn(self, val: str):
        ...

    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def __init__(self, sourceColumn: str, dataSetColumn: str, ):
        ...

    def Clone(self, ) -> System.Object:
        ...

    @typing.overload
    def GetDataColumnBySchemaAction(self, dataTable: System.Data.DataTable, dataType: System.Type, schemaAction: int, ) -> System.Data.DataColumn:
        ...

    @staticmethod
    @typing.overload
    def GetDataColumnBySchemaAction(sourceColumn: str, dataSetColumn: str, dataTable: System.Data.DataTable, dataType: System.Type, schemaAction: int, ) -> System.Data.DataColumn:
        ...

    @staticmethod
    def CreateDataColumnBySchemaAction(sourceColumn: str, dataSetColumn: str, dataTable: System.Data.DataTable, dataType: System.Type, schemaAction: int, ) -> System.Data.DataColumn:
        ...

    def ToString(self, ) -> str:
        ...

