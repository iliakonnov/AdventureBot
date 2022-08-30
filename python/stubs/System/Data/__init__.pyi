from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import System
import System.Data
import System.ComponentModel
import System.Runtime.Serialization
import System.Xml.Serialization
import System.Globalization
import System.IO
import System.Xml
import System.Xml.Schema
import System.Collections
import System.Reflection
import System.Data.Common


class DbType(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    AnsiString: System.Int32 = AnsiString
    Binary: System.Int32 = Binary
    Byte: System.Int32 = Byte
    Boolean: System.Int32 = Boolean
    Currency: System.Int32 = Currency
    Date: System.Int32 = Date
    DateTime: System.Int32 = DateTime
    Decimal: System.Int32 = Decimal
    Double: System.Int32 = Double
    Guid: System.Int32 = Guid
    Int16: System.Int32 = Int16
    Int32: System.Int32 = Int32
    Int64: System.Int32 = Int64
    Object: System.Int32 = Object
    SByte: System.Int32 = SByte
    Single: System.Int32 = Single
    String: System.Int32 = String
    Time: System.Int32 = Time
    UInt16: System.Int32 = UInt16
    UInt32: System.Int32 = UInt32
    UInt64: System.Int32 = UInt64
    VarNumeric: System.Int32 = VarNumeric
    AnsiStringFixedLength: System.Int32 = AnsiStringFixedLength
    StringFixedLength: System.Int32 = StringFixedLength
    Xml: System.Int32 = Xml
    DateTime2: System.Int32 = DateTime2
    DateTimeOffset: System.Int32 = DateTimeOffset

class IDbCommand(System.IDisposable, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @abc.abstractmethod
    @property
    def Connection(self) -> System.Data.IDbConnection:
        ...
    @abc.abstractmethod
    @Connection.setter
    def Connection(self, val: System.Data.IDbConnection):
        ...

    @abc.abstractmethod
    @property
    def Transaction(self) -> System.Data.IDbTransaction:
        ...
    @abc.abstractmethod
    @Transaction.setter
    def Transaction(self, val: System.Data.IDbTransaction):
        ...

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

    @abc.abstractmethod
    @property
    def Parameters(self) -> System.Data.IDataParameterCollection:
        ...

    @abc.abstractmethod
    @property
    def UpdatedRowSource(self) -> System.Data.UpdateRowSource:
        ...
    @abc.abstractmethod
    @UpdatedRowSource.setter
    def UpdatedRowSource(self, val: System.Data.UpdateRowSource):
        ...

    # methods
    @typing.overload
    @abc.abstractmethod
    def Prepare(self, ) -> None:
        ...

    @typing.overload
    @abc.abstractmethod
    def Cancel(self, ) -> None:
        ...

    @typing.overload
    @abc.abstractmethod
    def CreateParameter(self, ) -> System.Data.IDbDataParameter:
        ...

    @typing.overload
    @abc.abstractmethod
    def ExecuteNonQuery(self, ) -> System.Int32:
        ...

    @typing.overload
    @abc.abstractmethod
    def ExecuteReader(self, ) -> System.Data.IDataReader:
        ...

    @typing.overload
    @abc.abstractmethod
    def ExecuteReader(self, behavior: System.Data.CommandBehavior, ) -> System.Data.IDataReader:
        ...

    @typing.overload
    @abc.abstractmethod
    def ExecuteScalar(self, ) -> System.Object:
        ...

class CommandType(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    Text: System.Int32 = Text
    StoredProcedure: System.Int32 = StoredProcedure
    TableDirect: System.Int32 = TableDirect

class UpdateRowSource(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    None_: System.Int32 = None
    OutputParameters: System.Int32 = OutputParameters
    FirstReturnedRecord: System.Int32 = FirstReturnedRecord
    Both: System.Int32 = Both

class CommandBehavior(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    Default: System.Int32 = Default
    SingleResult: System.Int32 = SingleResult
    SchemaOnly: System.Int32 = SchemaOnly
    KeyInfo: System.Int32 = KeyInfo
    SingleRow: System.Int32 = SingleRow
    SequentialAccess: System.Int32 = SequentialAccess
    CloseConnection: System.Int32 = CloseConnection

class IDataReader(System.IDisposable, System.Data.IDataRecord, abc.ABC):
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
    def IsClosed(self) -> System.Boolean:
        ...

    @abc.abstractmethod
    @property
    def RecordsAffected(self) -> System.Int32:
        ...

    # methods
    @typing.overload
    @abc.abstractmethod
    def Close(self, ) -> None:
        ...

    @typing.overload
    @abc.abstractmethod
    def GetSchemaTable(self, ) -> System.Data.DataTable:
        ...

    @typing.overload
    @abc.abstractmethod
    def NextResult(self, ) -> System.Boolean:
        ...

    @typing.overload
    @abc.abstractmethod
    def Read(self, ) -> System.Boolean:
        ...

class IDataRecord(abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @abc.abstractmethod
    @property
    def FieldCount(self) -> System.Int32:
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
    def GetName(self, i: System.Int32, ) -> System.String:
        ...

    @typing.overload
    @abc.abstractmethod
    def GetDataTypeName(self, i: System.Int32, ) -> System.String:
        ...

    @typing.overload
    @abc.abstractmethod
    def GetFieldType(self, i: System.Int32, ) -> System.Type:
        ...

    @typing.overload
    @abc.abstractmethod
    def GetValue(self, i: System.Int32, ) -> System.Object:
        ...

    @typing.overload
    @abc.abstractmethod
    def GetValues(self, values: list[System.Object], ) -> System.Int32:
        ...

    @typing.overload
    @abc.abstractmethod
    def GetOrdinal(self, name: System.String, ) -> System.Int32:
        ...

    @typing.overload
    @abc.abstractmethod
    def GetBoolean(self, i: System.Int32, ) -> System.Boolean:
        ...

    @typing.overload
    @abc.abstractmethod
    def GetByte(self, i: System.Int32, ) -> System.Byte:
        ...

    @typing.overload
    @abc.abstractmethod
    def GetBytes(self, i: System.Int32, fieldOffset: System.Int64, buffer: list[System.Byte], bufferoffset: System.Int32, length: System.Int32, ) -> System.Int64:
        ...

    @typing.overload
    @abc.abstractmethod
    def GetChar(self, i: System.Int32, ) -> System.Char:
        ...

    @typing.overload
    @abc.abstractmethod
    def GetChars(self, i: System.Int32, fieldoffset: System.Int64, buffer: list[System.Char], bufferoffset: System.Int32, length: System.Int32, ) -> System.Int64:
        ...

    @typing.overload
    @abc.abstractmethod
    def GetGuid(self, i: System.Int32, ) -> System.Guid:
        ...

    @typing.overload
    @abc.abstractmethod
    def GetInt16(self, i: System.Int32, ) -> System.Int16:
        ...

    @typing.overload
    @abc.abstractmethod
    def GetInt32(self, i: System.Int32, ) -> System.Int32:
        ...

    @typing.overload
    @abc.abstractmethod
    def GetInt64(self, i: System.Int32, ) -> System.Int64:
        ...

    @typing.overload
    @abc.abstractmethod
    def GetFloat(self, i: System.Int32, ) -> System.Single:
        ...

    @typing.overload
    @abc.abstractmethod
    def GetDouble(self, i: System.Int32, ) -> System.Double:
        ...

    @typing.overload
    @abc.abstractmethod
    def GetString(self, i: System.Int32, ) -> System.String:
        ...

    @typing.overload
    @abc.abstractmethod
    def GetDecimal(self, i: System.Int32, ) -> System.Decimal:
        ...

    @typing.overload
    @abc.abstractmethod
    def GetDateTime(self, i: System.Int32, ) -> System.DateTime:
        ...

    @typing.overload
    @abc.abstractmethod
    def GetData(self, i: System.Int32, ) -> System.Data.IDataReader:
        ...

    @typing.overload
    @abc.abstractmethod
    def IsDBNull(self, i: System.Int32, ) -> System.Boolean:
        ...

class DataTable(System.ComponentModel.IComponent, System.IDisposable, System.IServiceProvider, System.ComponentModel.IListSource, System.ComponentModel.ISupportInitializeNotification, System.ComponentModel.ISupportInitialize, System.Runtime.Serialization.ISerializable, System.Xml.Serialization.IXmlSerializable, System.ComponentModel.MarshalByValueComponent):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def CaseSensitive(self) -> System.Boolean:
        ...
    @CaseSensitive.setter
    def CaseSensitive(self, val: System.Boolean):
        ...

    @property
    def IsInitialized(self) -> System.Boolean:
        ...

    @property
    def RemotingFormat(self) -> System.Data.SerializationFormat:
        ...
    @RemotingFormat.setter
    def RemotingFormat(self, val: System.Data.SerializationFormat):
        ...

    @property
    def ChildRelations(self) -> System.Data.DataRelationCollection:
        ...

    @property
    def Columns(self) -> System.Data.DataColumnCollection:
        ...

    @property
    def Constraints(self) -> System.Data.ConstraintCollection:
        ...

    @property
    def DataSet(self) -> System.Data.DataSet:
        ...

    @property
    def DefaultView(self) -> System.Data.DataView:
        ...

    @property
    def DisplayExpression(self) -> System.String:
        ...
    @DisplayExpression.setter
    def DisplayExpression(self, val: System.String):
        ...

    @property
    def ExtendedProperties(self) -> System.Data.PropertyCollection:
        ...

    @property
    def HasErrors(self) -> System.Boolean:
        ...

    @property
    def Locale(self) -> System.Globalization.CultureInfo:
        ...
    @Locale.setter
    def Locale(self, val: System.Globalization.CultureInfo):
        ...

    @property
    def MinimumCapacity(self) -> System.Int32:
        ...
    @MinimumCapacity.setter
    def MinimumCapacity(self, val: System.Int32):
        ...

    @property
    def ParentRelations(self) -> System.Data.DataRelationCollection:
        ...

    @property
    def PrimaryKey(self) -> list[System.Data.DataColumn]:
        ...
    @PrimaryKey.setter
    def PrimaryKey(self, val: list[System.Data.DataColumn]):
        ...

    @property
    def Rows(self) -> System.Data.DataRowCollection:
        ...

    @property
    def TableName(self) -> System.String:
        ...
    @TableName.setter
    def TableName(self, val: System.String):
        ...

    @property
    def Namespace(self) -> System.String:
        ...
    @Namespace.setter
    def Namespace(self, val: System.String):
        ...

    @property
    def Prefix(self) -> System.String:
        ...
    @Prefix.setter
    def Prefix(self, val: System.String):
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
    def DesignMode(self) -> System.Boolean:
        ...

    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def __init__(self, tableName: System.String, ):
        ...

    @typing.overload
    def __init__(self, tableName: System.String, tableNamespace: System.String, ):
        ...

    @typing.overload
    def WriteXmlSchema(self, stream: System.IO.Stream, writeHierarchy: System.Boolean, ) -> None:
        ...

    @typing.overload
    def WriteXmlSchema(self, writer: System.IO.TextWriter, ) -> None:
        ...

    @typing.overload
    def WriteXmlSchema(self, writer: System.IO.TextWriter, writeHierarchy: System.Boolean, ) -> None:
        ...

    @typing.overload
    def WriteXmlSchema(self, writer: System.Xml.XmlWriter, ) -> None:
        ...

    @typing.overload
    def WriteXmlSchema(self, writer: System.Xml.XmlWriter, writeHierarchy: System.Boolean, ) -> None:
        ...

    @typing.overload
    def WriteXmlSchema(self, fileName: System.String, ) -> None:
        ...

    @typing.overload
    def WriteXmlSchema(self, fileName: System.String, writeHierarchy: System.Boolean, ) -> None:
        ...

    @typing.overload
    def ReadXml(self, stream: System.IO.Stream, ) -> System.Data.XmlReadMode:
        ...

    @typing.overload
    def ReadXml(self, reader: System.IO.TextReader, ) -> System.Data.XmlReadMode:
        ...

    @typing.overload
    def ReadXml(self, fileName: System.String, ) -> System.Data.XmlReadMode:
        ...

    @typing.overload
    def ReadXml(self, reader: System.Xml.XmlReader, ) -> System.Data.XmlReadMode:
        ...

    @typing.overload
    def ReadXmlSchema(self, stream: System.IO.Stream, ) -> None:
        ...

    @typing.overload
    def ReadXmlSchema(self, reader: System.IO.TextReader, ) -> None:
        ...

    @typing.overload
    def ReadXmlSchema(self, fileName: System.String, ) -> None:
        ...

    @typing.overload
    def ReadXmlSchema(self, reader: System.Xml.XmlReader, ) -> None:
        ...

    @typing.overload
    @staticmethod
    def GetDataTableSchema(schemaSet: System.Xml.Schema.XmlSchemaSet, ) -> System.Xml.Schema.XmlSchemaComplexType:
        ...

    @typing.overload
    def RejectChanges(self, ) -> None:
        ...

    @typing.overload
    def Reset(self, ) -> None:
        ...

    @typing.overload
    def Select(self, ) -> list[System.Data.DataRow]:
        ...

    @typing.overload
    def Select(self, filterExpression: System.String, ) -> list[System.Data.DataRow]:
        ...

    @typing.overload
    def Select(self, filterExpression: System.String, sort: System.String, ) -> list[System.Data.DataRow]:
        ...

    @typing.overload
    def Select(self, filterExpression: System.String, sort: System.String, recordStates: System.Data.DataViewRowState, ) -> list[System.Data.DataRow]:
        ...

    @typing.overload
    def ToString(self, ) -> System.String:
        ...

    @typing.overload
    def BeginLoadData(self, ) -> None:
        ...

    @typing.overload
    def EndLoadData(self, ) -> None:
        ...

    @typing.overload
    def LoadDataRow(self, values: list[System.Object], fAcceptChanges: System.Boolean, ) -> System.Data.DataRow:
        ...

    @typing.overload
    def LoadDataRow(self, values: list[System.Object], loadOption: System.Data.LoadOption, ) -> System.Data.DataRow:
        ...

    @typing.overload
    def Merge(self, table: System.Data.DataTable, ) -> None:
        ...

    @typing.overload
    def Merge(self, table: System.Data.DataTable, preserveChanges: System.Boolean, ) -> None:
        ...

    @typing.overload
    def Merge(self, table: System.Data.DataTable, preserveChanges: System.Boolean, missingSchemaAction: System.Data.MissingSchemaAction, ) -> None:
        ...

    @typing.overload
    def Load(self, reader: System.Data.IDataReader, ) -> None:
        ...

    @typing.overload
    def Load(self, reader: System.Data.IDataReader, loadOption: System.Data.LoadOption, ) -> None:
        ...

    @typing.overload
    def Load(self, reader: System.Data.IDataReader, loadOption: System.Data.LoadOption, errorHandler: System.Data.FillErrorEventHandler, ) -> None:
        ...

    @typing.overload
    def CreateDataReader(self, ) -> System.Data.DataTableReader:
        ...

    @typing.overload
    def WriteXml(self, stream: System.IO.Stream, ) -> None:
        ...

    @typing.overload
    def WriteXml(self, stream: System.IO.Stream, writeHierarchy: System.Boolean, ) -> None:
        ...

    @typing.overload
    def WriteXml(self, writer: System.IO.TextWriter, ) -> None:
        ...

    @typing.overload
    def WriteXml(self, writer: System.IO.TextWriter, writeHierarchy: System.Boolean, ) -> None:
        ...

    @typing.overload
    def WriteXml(self, writer: System.Xml.XmlWriter, ) -> None:
        ...

    @typing.overload
    def WriteXml(self, writer: System.Xml.XmlWriter, writeHierarchy: System.Boolean, ) -> None:
        ...

    @typing.overload
    def WriteXml(self, fileName: System.String, ) -> None:
        ...

    @typing.overload
    def WriteXml(self, fileName: System.String, writeHierarchy: System.Boolean, ) -> None:
        ...

    @typing.overload
    def WriteXml(self, stream: System.IO.Stream, mode: System.Data.XmlWriteMode, ) -> None:
        ...

    @typing.overload
    def WriteXml(self, stream: System.IO.Stream, mode: System.Data.XmlWriteMode, writeHierarchy: System.Boolean, ) -> None:
        ...

    @typing.overload
    def WriteXml(self, writer: System.IO.TextWriter, mode: System.Data.XmlWriteMode, ) -> None:
        ...

    @typing.overload
    def WriteXml(self, writer: System.IO.TextWriter, mode: System.Data.XmlWriteMode, writeHierarchy: System.Boolean, ) -> None:
        ...

    @typing.overload
    def WriteXml(self, writer: System.Xml.XmlWriter, mode: System.Data.XmlWriteMode, ) -> None:
        ...

    @typing.overload
    def WriteXml(self, writer: System.Xml.XmlWriter, mode: System.Data.XmlWriteMode, writeHierarchy: System.Boolean, ) -> None:
        ...

    @typing.overload
    def WriteXml(self, fileName: System.String, mode: System.Data.XmlWriteMode, ) -> None:
        ...

    @typing.overload
    def WriteXml(self, fileName: System.String, mode: System.Data.XmlWriteMode, writeHierarchy: System.Boolean, ) -> None:
        ...

    @typing.overload
    def WriteXmlSchema(self, stream: System.IO.Stream, ) -> None:
        ...

    @typing.overload
    def AcceptChanges(self, ) -> None:
        ...

    @typing.overload
    def Clone(self, ) -> System.Data.DataTable:
        ...

    @typing.overload
    def Copy(self, ) -> System.Data.DataTable:
        ...

    @typing.overload
    def Clear(self, ) -> None:
        ...

    @typing.overload
    def Compute(self, expression: System.String, filter: System.String, ) -> System.Object:
        ...

    @typing.overload
    def GetChanges(self, ) -> System.Data.DataTable:
        ...

    @typing.overload
    def GetChanges(self, rowStates: System.Data.DataRowState, ) -> System.Data.DataTable:
        ...

    @typing.overload
    def GetErrors(self, ) -> list[System.Data.DataRow]:
        ...

    @typing.overload
    def ImportRow(self, row: System.Data.DataRow, ) -> None:
        ...

    @typing.overload
    def NewRow(self, ) -> System.Data.DataRow:
        ...

    @typing.overload
    def GetObjectData(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext, ) -> None:
        ...

    @typing.overload
    def BeginInit(self, ) -> None:
        ...

    @typing.overload
    def EndInit(self, ) -> None:
        ...

class IDbConnection(System.IDisposable, abc.ABC):
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

    @abc.abstractmethod
    @property
    def ConnectionTimeout(self) -> System.Int32:
        ...

    @abc.abstractmethod
    @property
    def Database(self) -> System.String:
        ...

    @abc.abstractmethod
    @property
    def State(self) -> System.Data.ConnectionState:
        ...

    # methods
    @typing.overload
    @abc.abstractmethod
    def BeginTransaction(self, ) -> System.Data.IDbTransaction:
        ...

    @typing.overload
    @abc.abstractmethod
    def BeginTransaction(self, il: System.Data.IsolationLevel, ) -> System.Data.IDbTransaction:
        ...

    @typing.overload
    @abc.abstractmethod
    def Close(self, ) -> None:
        ...

    @typing.overload
    @abc.abstractmethod
    def ChangeDatabase(self, databaseName: System.String, ) -> None:
        ...

    @typing.overload
    @abc.abstractmethod
    def CreateCommand(self, ) -> System.Data.IDbCommand:
        ...

    @typing.overload
    @abc.abstractmethod
    def Open(self, ) -> None:
        ...

class IDbTransaction(System.IDisposable, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @abc.abstractmethod
    @property
    def Connection(self) -> System.Data.IDbConnection:
        ...

    @abc.abstractmethod
    @property
    def IsolationLevel(self) -> System.Data.IsolationLevel:
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

class IDataParameterCollection(System.Collections.IList, System.Collections.ICollection, System.Collections.IEnumerable, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @abc.abstractmethod
    @property
    def Item(self) -> System.Object:
        ...
    @abc.abstractmethod
    @Item.setter
    def Item(self, val: System.Object):
        ...

    # methods
    @typing.overload
    @abc.abstractmethod
    def Contains(self, parameterName: System.String, ) -> System.Boolean:
        ...

    @typing.overload
    @abc.abstractmethod
    def IndexOf(self, parameterName: System.String, ) -> System.Int32:
        ...

    @typing.overload
    @abc.abstractmethod
    def RemoveAt(self, parameterName: System.String, ) -> None:
        ...

class IDbDataParameter(System.Data.IDataParameter, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @abc.abstractmethod
    @property
    def Precision(self) -> System.Byte:
        ...
    @abc.abstractmethod
    @Precision.setter
    def Precision(self, val: System.Byte):
        ...

    @abc.abstractmethod
    @property
    def Scale(self) -> System.Byte:
        ...
    @abc.abstractmethod
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

    # methods
class ConnectionState(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    Closed: System.Int32 = Closed
    Open: System.Int32 = Open
    Connecting: System.Int32 = Connecting
    Executing: System.Int32 = Executing
    Fetching: System.Int32 = Fetching
    Broken: System.Int32 = Broken

class IsolationLevel(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    Chaos: System.Int32 = Chaos
    ReadUncommitted: System.Int32 = ReadUncommitted
    ReadCommitted: System.Int32 = ReadCommitted
    RepeatableRead: System.Int32 = RepeatableRead
    Serializable: System.Int32 = Serializable
    Snapshot: System.Int32 = Snapshot
    Unspecified: System.Int32 = Unspecified

class IDataParameter(abc.ABC):
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
    @property
    def ParameterName(self) -> System.String:
        ...
    @abc.abstractmethod
    @ParameterName.setter
    def ParameterName(self, val: System.String):
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
    def SourceVersion(self) -> System.Data.DataRowVersion:
        ...
    @abc.abstractmethod
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
class ParameterDirection(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    Input: System.Int32 = Input
    Output: System.Int32 = Output
    InputOutput: System.Int32 = InputOutput
    ReturnValue: System.Int32 = ReturnValue

class DataRowVersion(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    Original: System.Int32 = Original
    Current: System.Int32 = Current
    Proposed: System.Int32 = Proposed
    Default: System.Int32 = Default

class SerializationFormat(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    Xml: System.Int32 = Xml
    Binary: System.Int32 = Binary

class DataRelationCollection(System.Collections.ICollection, System.Collections.IEnumerable, System.Data.InternalDataCollectionBase, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @abc.abstractmethod
    @property
    def Item(self) -> System.Data.DataRelation:
        ...

    @abc.abstractmethod
    @property
    def Item(self) -> System.Data.DataRelation:
        ...

    @property
    def Count(self) -> System.Int32:
        ...

    @property
    def IsReadOnly(self) -> System.Boolean:
        ...

    @property
    def IsSynchronized(self) -> System.Boolean:
        ...

    @property
    def SyncRoot(self) -> System.Object:
        ...

    # methods
    @typing.overload
    def Add(self, relation: System.Data.DataRelation, ) -> None:
        ...

    @typing.overload
    def AddRange(self, relations: list[System.Data.DataRelation], ) -> None:
        ...

    @typing.overload
    def Add(self, name: System.String, parentColumns: list[System.Data.DataColumn], childColumns: list[System.Data.DataColumn], ) -> System.Data.DataRelation:
        ...

    @typing.overload
    def Add(self, name: System.String, parentColumns: list[System.Data.DataColumn], childColumns: list[System.Data.DataColumn], createConstraints: System.Boolean, ) -> System.Data.DataRelation:
        ...

    @typing.overload
    def Add(self, parentColumns: list[System.Data.DataColumn], childColumns: list[System.Data.DataColumn], ) -> System.Data.DataRelation:
        ...

    @typing.overload
    def Add(self, name: System.String, parentColumn: System.Data.DataColumn, childColumn: System.Data.DataColumn, ) -> System.Data.DataRelation:
        ...

    @typing.overload
    def Add(self, name: System.String, parentColumn: System.Data.DataColumn, childColumn: System.Data.DataColumn, createConstraints: System.Boolean, ) -> System.Data.DataRelation:
        ...

    @typing.overload
    def Add(self, parentColumn: System.Data.DataColumn, childColumn: System.Data.DataColumn, ) -> System.Data.DataRelation:
        ...

    @typing.overload
    def Clear(self, ) -> None:
        ...

    @typing.overload
    def Contains(self, name: System.String, ) -> System.Boolean:
        ...

    @typing.overload
    def CopyTo(self, array: list[System.Data.DataRelation], index: System.Int32, ) -> None:
        ...

    @typing.overload
    def IndexOf(self, relation: System.Data.DataRelation, ) -> System.Int32:
        ...

    @typing.overload
    def IndexOf(self, relationName: System.String, ) -> System.Int32:
        ...

    @typing.overload
    def CanRemove(self, relation: System.Data.DataRelation, ) -> System.Boolean:
        ...

    @typing.overload
    def Remove(self, relation: System.Data.DataRelation, ) -> None:
        ...

    @typing.overload
    def RemoveAt(self, index: System.Int32, ) -> None:
        ...

    @typing.overload
    def Remove(self, name: System.String, ) -> None:
        ...

class DataColumnCollection(System.Collections.ICollection, System.Collections.IEnumerable, System.Data.InternalDataCollectionBase):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def Item(self) -> System.Data.DataColumn:
        ...

    @property
    def Item(self) -> System.Data.DataColumn:
        ...

    @property
    def Count(self) -> System.Int32:
        ...

    @property
    def IsReadOnly(self) -> System.Boolean:
        ...

    @property
    def IsSynchronized(self) -> System.Boolean:
        ...

    @property
    def SyncRoot(self) -> System.Object:
        ...

    # methods
    @typing.overload
    def Add(self, column: System.Data.DataColumn, ) -> None:
        ...

    @typing.overload
    def AddRange(self, columns: list[System.Data.DataColumn], ) -> None:
        ...

    @typing.overload
    def Add(self, columnName: System.String, type: System.Type, expression: System.String, ) -> System.Data.DataColumn:
        ...

    @typing.overload
    def Add(self, columnName: System.String, type: System.Type, ) -> System.Data.DataColumn:
        ...

    @typing.overload
    def Add(self, columnName: System.String, ) -> System.Data.DataColumn:
        ...

    @typing.overload
    def Add(self, ) -> System.Data.DataColumn:
        ...

    @typing.overload
    def CanRemove(self, column: System.Data.DataColumn, ) -> System.Boolean:
        ...

    @typing.overload
    def Clear(self, ) -> None:
        ...

    @typing.overload
    def Contains(self, name: System.String, ) -> System.Boolean:
        ...

    @typing.overload
    def CopyTo(self, array: list[System.Data.DataColumn], index: System.Int32, ) -> None:
        ...

    @typing.overload
    def IndexOf(self, column: System.Data.DataColumn, ) -> System.Int32:
        ...

    @typing.overload
    def IndexOf(self, columnName: System.String, ) -> System.Int32:
        ...

    @typing.overload
    def Remove(self, column: System.Data.DataColumn, ) -> None:
        ...

    @typing.overload
    def RemoveAt(self, index: System.Int32, ) -> None:
        ...

    @typing.overload
    def Remove(self, name: System.String, ) -> None:
        ...

class ConstraintCollection(System.Collections.ICollection, System.Collections.IEnumerable, System.Data.InternalDataCollectionBase):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def Item(self) -> System.Data.Constraint:
        ...

    @property
    def Item(self) -> System.Data.Constraint:
        ...

    @property
    def Count(self) -> System.Int32:
        ...

    @property
    def IsReadOnly(self) -> System.Boolean:
        ...

    @property
    def IsSynchronized(self) -> System.Boolean:
        ...

    @property
    def SyncRoot(self) -> System.Object:
        ...

    # methods
    @typing.overload
    def Add(self, constraint: System.Data.Constraint, ) -> None:
        ...

    @typing.overload
    def Add(self, name: System.String, columns: list[System.Data.DataColumn], primaryKey: System.Boolean, ) -> System.Data.Constraint:
        ...

    @typing.overload
    def Add(self, name: System.String, column: System.Data.DataColumn, primaryKey: System.Boolean, ) -> System.Data.Constraint:
        ...

    @typing.overload
    def Add(self, name: System.String, primaryKeyColumn: System.Data.DataColumn, foreignKeyColumn: System.Data.DataColumn, ) -> System.Data.Constraint:
        ...

    @typing.overload
    def Add(self, name: System.String, primaryKeyColumns: list[System.Data.DataColumn], foreignKeyColumns: list[System.Data.DataColumn], ) -> System.Data.Constraint:
        ...

    @typing.overload
    def AddRange(self, constraints: list[System.Data.Constraint], ) -> None:
        ...

    @typing.overload
    def CanRemove(self, constraint: System.Data.Constraint, ) -> System.Boolean:
        ...

    @typing.overload
    def Clear(self, ) -> None:
        ...

    @typing.overload
    def Contains(self, name: System.String, ) -> System.Boolean:
        ...

    @typing.overload
    def CopyTo(self, array: list[System.Data.Constraint], index: System.Int32, ) -> None:
        ...

    @typing.overload
    def IndexOf(self, constraint: System.Data.Constraint, ) -> System.Int32:
        ...

    @typing.overload
    def IndexOf(self, constraintName: System.String, ) -> System.Int32:
        ...

    @typing.overload
    def Remove(self, constraint: System.Data.Constraint, ) -> None:
        ...

    @typing.overload
    def RemoveAt(self, index: System.Int32, ) -> None:
        ...

    @typing.overload
    def Remove(self, name: System.String, ) -> None:
        ...

class DataSet(System.ComponentModel.IComponent, System.IDisposable, System.IServiceProvider, System.ComponentModel.IListSource, System.Xml.Serialization.IXmlSerializable, System.ComponentModel.ISupportInitializeNotification, System.ComponentModel.ISupportInitialize, System.Runtime.Serialization.ISerializable, System.ComponentModel.MarshalByValueComponent):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def RemotingFormat(self) -> System.Data.SerializationFormat:
        ...
    @RemotingFormat.setter
    def RemotingFormat(self, val: System.Data.SerializationFormat):
        ...

    @property
    def SchemaSerializationMode(self) -> System.Data.SchemaSerializationMode:
        ...
    @SchemaSerializationMode.setter
    def SchemaSerializationMode(self, val: System.Data.SchemaSerializationMode):
        ...

    @property
    def CaseSensitive(self) -> System.Boolean:
        ...
    @CaseSensitive.setter
    def CaseSensitive(self, val: System.Boolean):
        ...

    @property
    def DefaultViewManager(self) -> System.Data.DataViewManager:
        ...

    @property
    def EnforceConstraints(self) -> System.Boolean:
        ...
    @EnforceConstraints.setter
    def EnforceConstraints(self, val: System.Boolean):
        ...

    @property
    def DataSetName(self) -> System.String:
        ...
    @DataSetName.setter
    def DataSetName(self, val: System.String):
        ...

    @property
    def Namespace(self) -> System.String:
        ...
    @Namespace.setter
    def Namespace(self, val: System.String):
        ...

    @property
    def Prefix(self) -> System.String:
        ...
    @Prefix.setter
    def Prefix(self, val: System.String):
        ...

    @property
    def ExtendedProperties(self) -> System.Data.PropertyCollection:
        ...

    @property
    def HasErrors(self) -> System.Boolean:
        ...

    @property
    def IsInitialized(self) -> System.Boolean:
        ...

    @property
    def Locale(self) -> System.Globalization.CultureInfo:
        ...
    @Locale.setter
    def Locale(self, val: System.Globalization.CultureInfo):
        ...

    @property
    def Site(self) -> System.ComponentModel.ISite:
        ...
    @Site.setter
    def Site(self, val: System.ComponentModel.ISite):
        ...

    @property
    def Relations(self) -> System.Data.DataRelationCollection:
        ...

    @property
    def Tables(self) -> System.Data.DataTableCollection:
        ...

    @property
    def Container(self) -> System.ComponentModel.IContainer:
        ...

    @property
    def DesignMode(self) -> System.Boolean:
        ...

    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def __init__(self, dataSetName: System.String, ):
        ...

    @typing.overload
    def ReadXmlSchema(self, stream: System.IO.Stream, ) -> None:
        ...

    @typing.overload
    def ReadXmlSchema(self, reader: System.IO.TextReader, ) -> None:
        ...

    @typing.overload
    def ReadXmlSchema(self, fileName: System.String, ) -> None:
        ...

    @typing.overload
    def WriteXmlSchema(self, stream: System.IO.Stream, ) -> None:
        ...

    @typing.overload
    def WriteXmlSchema(self, stream: System.IO.Stream, multipleTargetConverter: System.Converter[System.Type, System.String], ) -> None:
        ...

    @typing.overload
    def WriteXmlSchema(self, fileName: System.String, ) -> None:
        ...

    @typing.overload
    def WriteXmlSchema(self, fileName: System.String, multipleTargetConverter: System.Converter[System.Type, System.String], ) -> None:
        ...

    @typing.overload
    def WriteXmlSchema(self, writer: System.IO.TextWriter, ) -> None:
        ...

    @typing.overload
    def WriteXmlSchema(self, writer: System.IO.TextWriter, multipleTargetConverter: System.Converter[System.Type, System.String], ) -> None:
        ...

    @typing.overload
    def WriteXmlSchema(self, writer: System.Xml.XmlWriter, ) -> None:
        ...

    @typing.overload
    def WriteXmlSchema(self, writer: System.Xml.XmlWriter, multipleTargetConverter: System.Converter[System.Type, System.String], ) -> None:
        ...

    @typing.overload
    def ReadXml(self, reader: System.Xml.XmlReader, ) -> System.Data.XmlReadMode:
        ...

    @typing.overload
    def ReadXml(self, stream: System.IO.Stream, ) -> System.Data.XmlReadMode:
        ...

    @typing.overload
    def ReadXml(self, reader: System.IO.TextReader, ) -> System.Data.XmlReadMode:
        ...

    @typing.overload
    def ReadXml(self, fileName: System.String, ) -> System.Data.XmlReadMode:
        ...

    @typing.overload
    def ReadXml(self, reader: System.Xml.XmlReader, mode: System.Data.XmlReadMode, ) -> System.Data.XmlReadMode:
        ...

    @typing.overload
    def ReadXml(self, stream: System.IO.Stream, mode: System.Data.XmlReadMode, ) -> System.Data.XmlReadMode:
        ...

    @typing.overload
    def ReadXml(self, reader: System.IO.TextReader, mode: System.Data.XmlReadMode, ) -> System.Data.XmlReadMode:
        ...

    @typing.overload
    def ReadXml(self, fileName: System.String, mode: System.Data.XmlReadMode, ) -> System.Data.XmlReadMode:
        ...

    @typing.overload
    def WriteXml(self, stream: System.IO.Stream, ) -> None:
        ...

    @typing.overload
    def WriteXml(self, writer: System.IO.TextWriter, ) -> None:
        ...

    @typing.overload
    def WriteXml(self, writer: System.Xml.XmlWriter, ) -> None:
        ...

    @typing.overload
    def WriteXml(self, fileName: System.String, ) -> None:
        ...

    @typing.overload
    def WriteXml(self, stream: System.IO.Stream, mode: System.Data.XmlWriteMode, ) -> None:
        ...

    @typing.overload
    def WriteXml(self, writer: System.IO.TextWriter, mode: System.Data.XmlWriteMode, ) -> None:
        ...

    @typing.overload
    def WriteXml(self, writer: System.Xml.XmlWriter, mode: System.Data.XmlWriteMode, ) -> None:
        ...

    @typing.overload
    def WriteXml(self, fileName: System.String, mode: System.Data.XmlWriteMode, ) -> None:
        ...

    @typing.overload
    def Merge(self, dataSet: System.Data.DataSet, ) -> None:
        ...

    @typing.overload
    def Merge(self, dataSet: System.Data.DataSet, preserveChanges: System.Boolean, ) -> None:
        ...

    @typing.overload
    def Merge(self, dataSet: System.Data.DataSet, preserveChanges: System.Boolean, missingSchemaAction: System.Data.MissingSchemaAction, ) -> None:
        ...

    @typing.overload
    def Merge(self, table: System.Data.DataTable, ) -> None:
        ...

    @typing.overload
    def Merge(self, table: System.Data.DataTable, preserveChanges: System.Boolean, missingSchemaAction: System.Data.MissingSchemaAction, ) -> None:
        ...

    @typing.overload
    def Merge(self, rows: list[System.Data.DataRow], ) -> None:
        ...

    @typing.overload
    def Merge(self, rows: list[System.Data.DataRow], preserveChanges: System.Boolean, missingSchemaAction: System.Data.MissingSchemaAction, ) -> None:
        ...

    @typing.overload
    def RejectChanges(self, ) -> None:
        ...

    @typing.overload
    def Reset(self, ) -> None:
        ...

    @typing.overload
    @staticmethod
    def GetDataSetSchema(schemaSet: System.Xml.Schema.XmlSchemaSet, ) -> System.Xml.Schema.XmlSchemaComplexType:
        ...

    @typing.overload
    def Load(self, reader: System.Data.IDataReader, loadOption: System.Data.LoadOption, errorHandler: System.Data.FillErrorEventHandler, tables: list[System.Data.DataTable], ) -> None:
        ...

    @typing.overload
    def Load(self, reader: System.Data.IDataReader, loadOption: System.Data.LoadOption, tables: list[System.Data.DataTable], ) -> None:
        ...

    @typing.overload
    def Load(self, reader: System.Data.IDataReader, loadOption: System.Data.LoadOption, tables: list[System.String], ) -> None:
        ...

    @typing.overload
    def CreateDataReader(self, ) -> System.Data.DataTableReader:
        ...

    @typing.overload
    def CreateDataReader(self, dataTables: list[System.Data.DataTable], ) -> System.Data.DataTableReader:
        ...

    @typing.overload
    def GetObjectData(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext, ) -> None:
        ...

    @typing.overload
    def AcceptChanges(self, ) -> None:
        ...

    @typing.overload
    def BeginInit(self, ) -> None:
        ...

    @typing.overload
    def EndInit(self, ) -> None:
        ...

    @typing.overload
    def Clear(self, ) -> None:
        ...

    @typing.overload
    def Clone(self, ) -> System.Data.DataSet:
        ...

    @typing.overload
    def Copy(self, ) -> System.Data.DataSet:
        ...

    @typing.overload
    def GetChanges(self, ) -> System.Data.DataSet:
        ...

    @typing.overload
    def GetChanges(self, rowStates: System.Data.DataRowState, ) -> System.Data.DataSet:
        ...

    @typing.overload
    def GetXml(self, ) -> System.String:
        ...

    @typing.overload
    def GetXmlSchema(self, ) -> System.String:
        ...

    @typing.overload
    def HasChanges(self, ) -> System.Boolean:
        ...

    @typing.overload
    def HasChanges(self, rowStates: System.Data.DataRowState, ) -> System.Boolean:
        ...

    @typing.overload
    def InferXmlSchema(self, reader: System.Xml.XmlReader, nsArray: list[System.String], ) -> None:
        ...

    @typing.overload
    def InferXmlSchema(self, stream: System.IO.Stream, nsArray: list[System.String], ) -> None:
        ...

    @typing.overload
    def InferXmlSchema(self, reader: System.IO.TextReader, nsArray: list[System.String], ) -> None:
        ...

    @typing.overload
    def InferXmlSchema(self, fileName: System.String, nsArray: list[System.String], ) -> None:
        ...

    @typing.overload
    def ReadXmlSchema(self, reader: System.Xml.XmlReader, ) -> None:
        ...

class DataView(System.ComponentModel.IComponent, System.IDisposable, System.IServiceProvider, System.ComponentModel.IBindingListView, System.ComponentModel.IBindingList, System.Collections.IList, System.Collections.ICollection, System.Collections.IEnumerable, System.ComponentModel.ITypedList, System.ComponentModel.ISupportInitializeNotification, System.ComponentModel.ISupportInitialize, System.ComponentModel.MarshalByValueComponent):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def AllowDelete(self) -> System.Boolean:
        ...
    @AllowDelete.setter
    def AllowDelete(self, val: System.Boolean):
        ...

    @property
    def ApplyDefaultSort(self) -> System.Boolean:
        ...
    @ApplyDefaultSort.setter
    def ApplyDefaultSort(self, val: System.Boolean):
        ...

    @property
    def AllowEdit(self) -> System.Boolean:
        ...
    @AllowEdit.setter
    def AllowEdit(self, val: System.Boolean):
        ...

    @property
    def AllowNew(self) -> System.Boolean:
        ...
    @AllowNew.setter
    def AllowNew(self, val: System.Boolean):
        ...

    @property
    def Count(self) -> System.Int32:
        ...

    @property
    def DataViewManager(self) -> System.Data.DataViewManager:
        ...

    @property
    def IsInitialized(self) -> System.Boolean:
        ...

    @property
    def RowFilter(self) -> System.String:
        ...
    @RowFilter.setter
    def RowFilter(self, val: System.String):
        ...

    @property
    def RowStateFilter(self) -> System.Data.DataViewRowState:
        ...
    @RowStateFilter.setter
    def RowStateFilter(self, val: System.Data.DataViewRowState):
        ...

    @property
    def Sort(self) -> System.String:
        ...
    @Sort.setter
    def Sort(self, val: System.String):
        ...

    @property
    def Table(self) -> System.Data.DataTable:
        ...
    @Table.setter
    def Table(self, val: System.Data.DataTable):
        ...

    @property
    def Item(self) -> System.Data.DataRowView:
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
    def DesignMode(self) -> System.Boolean:
        ...

    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def __init__(self, table: System.Data.DataTable, ):
        ...

    @typing.overload
    def __init__(self, table: System.Data.DataTable, RowFilter: System.String, Sort: System.String, RowState: System.Data.DataViewRowState, ):
        ...

    @typing.overload
    def ToTable(self, ) -> System.Data.DataTable:
        ...

    @typing.overload
    def ToTable(self, tableName: System.String, ) -> System.Data.DataTable:
        ...

    @typing.overload
    def ToTable(self, distinct: System.Boolean, columnNames: list[System.String], ) -> System.Data.DataTable:
        ...

    @typing.overload
    def ToTable(self, tableName: System.String, distinct: System.Boolean, columnNames: list[System.String], ) -> System.Data.DataTable:
        ...

    @typing.overload
    def Equals(self, view: System.Data.DataView, ) -> System.Boolean:
        ...

    @typing.overload
    def AddNew(self, ) -> System.Data.DataRowView:
        ...

    @typing.overload
    def BeginInit(self, ) -> None:
        ...

    @typing.overload
    def EndInit(self, ) -> None:
        ...

    @typing.overload
    def CopyTo(self, array: System.Array, index: System.Int32, ) -> None:
        ...

    @typing.overload
    def Delete(self, index: System.Int32, ) -> None:
        ...

    @typing.overload
    def Find(self, key: System.Object, ) -> System.Int32:
        ...

    @typing.overload
    def Find(self, key: list[System.Object], ) -> System.Int32:
        ...

    @typing.overload
    def FindRows(self, key: System.Object, ) -> list[System.Data.DataRowView]:
        ...

    @typing.overload
    def FindRows(self, key: list[System.Object], ) -> list[System.Data.DataRowView]:
        ...

    @typing.overload
    def GetEnumerator(self, ) -> System.Collections.IEnumerator:
        ...

class PropertyCollection(System.Collections.IDictionary, System.Collections.ICollection, System.Collections.IEnumerable, System.Runtime.Serialization.ISerializable, System.Runtime.Serialization.IDeserializationCallback, System.ICloneable, System.Collections.Hashtable):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def Item(self) -> System.Object:
        ...
    @Item.setter
    def Item(self, val: System.Object):
        ...

    @property
    def IsReadOnly(self) -> System.Boolean:
        ...

    @property
    def IsFixedSize(self) -> System.Boolean:
        ...

    @property
    def IsSynchronized(self) -> System.Boolean:
        ...

    @property
    def Keys(self) -> System.Collections.ICollection:
        ...

    @property
    def Values(self) -> System.Collections.ICollection:
        ...

    @property
    def SyncRoot(self) -> System.Object:
        ...

    @property
    def Count(self) -> System.Int32:
        ...

    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def Clone(self, ) -> System.Object:
        ...

class DataColumn(System.ComponentModel.IComponent, System.IDisposable, System.IServiceProvider, System.ComponentModel.MarshalByValueComponent):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def AllowDBNull(self) -> System.Boolean:
        ...
    @AllowDBNull.setter
    def AllowDBNull(self, val: System.Boolean):
        ...

    @property
    def AutoIncrement(self) -> System.Boolean:
        ...
    @AutoIncrement.setter
    def AutoIncrement(self, val: System.Boolean):
        ...

    @property
    def AutoIncrementSeed(self) -> System.Int64:
        ...
    @AutoIncrementSeed.setter
    def AutoIncrementSeed(self, val: System.Int64):
        ...

    @property
    def AutoIncrementStep(self) -> System.Int64:
        ...
    @AutoIncrementStep.setter
    def AutoIncrementStep(self, val: System.Int64):
        ...

    @property
    def Caption(self) -> System.String:
        ...
    @Caption.setter
    def Caption(self, val: System.String):
        ...

    @property
    def ColumnName(self) -> System.String:
        ...
    @ColumnName.setter
    def ColumnName(self, val: System.String):
        ...

    @property
    def Prefix(self) -> System.String:
        ...
    @Prefix.setter
    def Prefix(self, val: System.String):
        ...

    @property
    def DataType(self) -> System.Type:
        ...
    @DataType.setter
    def DataType(self, val: System.Type):
        ...

    @property
    def DateTimeMode(self) -> System.Data.DataSetDateTime:
        ...
    @DateTimeMode.setter
    def DateTimeMode(self, val: System.Data.DataSetDateTime):
        ...

    @property
    def DefaultValue(self) -> System.Object:
        ...
    @DefaultValue.setter
    def DefaultValue(self, val: System.Object):
        ...

    @property
    def Expression(self) -> System.String:
        ...
    @Expression.setter
    def Expression(self, val: System.String):
        ...

    @property
    def ExtendedProperties(self) -> System.Data.PropertyCollection:
        ...

    @property
    def MaxLength(self) -> System.Int32:
        ...
    @MaxLength.setter
    def MaxLength(self, val: System.Int32):
        ...

    @property
    def Namespace(self) -> System.String:
        ...
    @Namespace.setter
    def Namespace(self, val: System.String):
        ...

    @property
    def Ordinal(self) -> System.Int32:
        ...

    @property
    def ReadOnly(self) -> System.Boolean:
        ...
    @ReadOnly.setter
    def ReadOnly(self, val: System.Boolean):
        ...

    @property
    def Table(self) -> System.Data.DataTable:
        ...

    @property
    def Unique(self) -> System.Boolean:
        ...
    @Unique.setter
    def Unique(self, val: System.Boolean):
        ...

    @property
    def ColumnMapping(self) -> System.Data.MappingType:
        ...
    @ColumnMapping.setter
    def ColumnMapping(self, val: System.Data.MappingType):
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
    def DesignMode(self) -> System.Boolean:
        ...

    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def __init__(self, columnName: System.String, ):
        ...

    @typing.overload
    def __init__(self, columnName: System.String, dataType: System.Type, ):
        ...

    @typing.overload
    def __init__(self, columnName: System.String, dataType: System.Type, expr: System.String, ):
        ...

    @typing.overload
    def __init__(self, columnName: System.String, dataType: System.Type, expr: System.String, type: System.Data.MappingType, ):
        ...

    @typing.overload
    def ToString(self, ) -> System.String:
        ...

    @typing.overload
    def SetOrdinal(self, ordinal: System.Int32, ) -> None:
        ...

class DataRowCollection(System.Collections.ICollection, System.Collections.IEnumerable, System.Data.InternalDataCollectionBase):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def Count(self) -> System.Int32:
        ...

    @property
    def Item(self) -> System.Data.DataRow:
        ...

    @property
    def IsReadOnly(self) -> System.Boolean:
        ...

    @property
    def IsSynchronized(self) -> System.Boolean:
        ...

    @property
    def SyncRoot(self) -> System.Object:
        ...

    # methods
    @typing.overload
    def Add(self, row: System.Data.DataRow, ) -> None:
        ...

    @typing.overload
    def InsertAt(self, row: System.Data.DataRow, pos: System.Int32, ) -> None:
        ...

    @typing.overload
    def IndexOf(self, row: System.Data.DataRow, ) -> System.Int32:
        ...

    @typing.overload
    def Add(self, values: list[System.Object], ) -> System.Data.DataRow:
        ...

    @typing.overload
    def Find(self, key: System.Object, ) -> System.Data.DataRow:
        ...

    @typing.overload
    def Find(self, keys: list[System.Object], ) -> System.Data.DataRow:
        ...

    @typing.overload
    def Clear(self, ) -> None:
        ...

    @typing.overload
    def Contains(self, key: System.Object, ) -> System.Boolean:
        ...

    @typing.overload
    def Contains(self, keys: list[System.Object], ) -> System.Boolean:
        ...

    @typing.overload
    def CopyTo(self, ar: System.Array, index: System.Int32, ) -> None:
        ...

    @typing.overload
    def CopyTo(self, array: list[System.Data.DataRow], index: System.Int32, ) -> None:
        ...

    @typing.overload
    def GetEnumerator(self, ) -> System.Collections.IEnumerator:
        ...

    @typing.overload
    def Remove(self, row: System.Data.DataRow, ) -> None:
        ...

    @typing.overload
    def RemoveAt(self, index: System.Int32, ) -> None:
        ...

class XmlReadMode(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    Auto: System.Int32 = Auto
    ReadSchema: System.Int32 = ReadSchema
    IgnoreSchema: System.Int32 = IgnoreSchema
    InferSchema: System.Int32 = InferSchema
    DiffGram: System.Int32 = DiffGram
    Fragment: System.Int32 = Fragment
    InferTypedSchema: System.Int32 = InferTypedSchema

class DataRow(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def RowError(self) -> System.String:
        ...
    @RowError.setter
    def RowError(self, val: System.String):
        ...

    @property
    def RowState(self) -> System.Data.DataRowState:
        ...

    @property
    def Table(self) -> System.Data.DataTable:
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
    def Item(self) -> System.Object:
        ...
    @Item.setter
    def Item(self, val: System.Object):
        ...

    @property
    def Item(self) -> System.Object:
        ...

    @property
    def Item(self) -> System.Object:
        ...

    @property
    def Item(self) -> System.Object:
        ...

    @property
    def ItemArray(self) -> list[System.Object]:
        ...
    @ItemArray.setter
    def ItemArray(self, val: list[System.Object]):
        ...

    @property
    def HasErrors(self) -> System.Boolean:
        ...

    # methods
    @typing.overload
    def SetParentRow(self, parentRow: System.Data.DataRow, ) -> None:
        ...

    @typing.overload
    def SetParentRow(self, parentRow: System.Data.DataRow, relation: System.Data.DataRelation, ) -> None:
        ...

    @typing.overload
    def SetAdded(self, ) -> None:
        ...

    @typing.overload
    def SetModified(self, ) -> None:
        ...

    @typing.overload
    def AcceptChanges(self, ) -> None:
        ...

    @typing.overload
    def BeginEdit(self, ) -> None:
        ...

    @typing.overload
    def CancelEdit(self, ) -> None:
        ...

    @typing.overload
    def Delete(self, ) -> None:
        ...

    @typing.overload
    def EndEdit(self, ) -> None:
        ...

    @typing.overload
    def SetColumnError(self, columnIndex: System.Int32, error: System.String, ) -> None:
        ...

    @typing.overload
    def SetColumnError(self, columnName: System.String, error: System.String, ) -> None:
        ...

    @typing.overload
    def SetColumnError(self, column: System.Data.DataColumn, error: System.String, ) -> None:
        ...

    @typing.overload
    def GetColumnError(self, columnIndex: System.Int32, ) -> System.String:
        ...

    @typing.overload
    def GetColumnError(self, columnName: System.String, ) -> System.String:
        ...

    @typing.overload
    def GetColumnError(self, column: System.Data.DataColumn, ) -> System.String:
        ...

    @typing.overload
    def ClearErrors(self, ) -> None:
        ...

    @typing.overload
    def GetColumnsInError(self, ) -> list[System.Data.DataColumn]:
        ...

    @typing.overload
    def GetChildRows(self, relationName: System.String, ) -> list[System.Data.DataRow]:
        ...

    @typing.overload
    def GetChildRows(self, relationName: System.String, version: System.Data.DataRowVersion, ) -> list[System.Data.DataRow]:
        ...

    @typing.overload
    def GetChildRows(self, relation: System.Data.DataRelation, ) -> list[System.Data.DataRow]:
        ...

    @typing.overload
    def GetChildRows(self, relation: System.Data.DataRelation, version: System.Data.DataRowVersion, ) -> list[System.Data.DataRow]:
        ...

    @typing.overload
    def GetParentRow(self, relationName: System.String, ) -> System.Data.DataRow:
        ...

    @typing.overload
    def GetParentRow(self, relationName: System.String, version: System.Data.DataRowVersion, ) -> System.Data.DataRow:
        ...

    @typing.overload
    def GetParentRow(self, relation: System.Data.DataRelation, ) -> System.Data.DataRow:
        ...

    @typing.overload
    def GetParentRow(self, relation: System.Data.DataRelation, version: System.Data.DataRowVersion, ) -> System.Data.DataRow:
        ...

    @typing.overload
    def GetParentRows(self, relationName: System.String, ) -> list[System.Data.DataRow]:
        ...

    @typing.overload
    def GetParentRows(self, relationName: System.String, version: System.Data.DataRowVersion, ) -> list[System.Data.DataRow]:
        ...

    @typing.overload
    def GetParentRows(self, relation: System.Data.DataRelation, ) -> list[System.Data.DataRow]:
        ...

    @typing.overload
    def GetParentRows(self, relation: System.Data.DataRelation, version: System.Data.DataRowVersion, ) -> list[System.Data.DataRow]:
        ...

    @typing.overload
    def HasVersion(self, version: System.Data.DataRowVersion, ) -> System.Boolean:
        ...

    @typing.overload
    def IsNull(self, columnIndex: System.Int32, ) -> System.Boolean:
        ...

    @typing.overload
    def IsNull(self, columnName: System.String, ) -> System.Boolean:
        ...

    @typing.overload
    def IsNull(self, column: System.Data.DataColumn, ) -> System.Boolean:
        ...

    @typing.overload
    def IsNull(self, column: System.Data.DataColumn, version: System.Data.DataRowVersion, ) -> System.Boolean:
        ...

    @typing.overload
    def RejectChanges(self, ) -> None:
        ...

class DataViewRowState(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    None_: System.Int32 = None
    Unchanged: System.Int32 = Unchanged
    Added: System.Int32 = Added
    Deleted: System.Int32 = Deleted
    ModifiedCurrent: System.Int32 = ModifiedCurrent
    CurrentRows: System.Int32 = CurrentRows
    ModifiedOriginal: System.Int32 = ModifiedOriginal
    OriginalRows: System.Int32 = OriginalRows

class LoadOption(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    OverwriteChanges: System.Int32 = OverwriteChanges
    PreserveChanges: System.Int32 = PreserveChanges
    Upsert: System.Int32 = Upsert

class MissingSchemaAction(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    Add: System.Int32 = Add
    Ignore: System.Int32 = Ignore
    Error: System.Int32 = Error
    AddWithKey: System.Int32 = AddWithKey

class FillErrorEventHandler(System.ICloneable, System.Runtime.Serialization.ISerializable, System.MulticastDelegate):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def Target(self) -> System.Object:
        ...

    @property
    def Method(self) -> System.Reflection.MethodInfo:
        ...

    # methods
    @typing.overload
    def __init__(self, object: System.Object, method: System.IntPtr, ):
        ...

    @typing.overload
    def Invoke(self, sender: System.Object, e: System.Data.FillErrorEventArgs, ) -> None:
        ...

    @typing.overload
    def BeginInvoke(self, sender: System.Object, e: System.Data.FillErrorEventArgs, callback: System.AsyncCallback, object: System.Object, ) -> System.IAsyncResult:
        ...

    @typing.overload
    def EndInvoke(self, result: System.IAsyncResult, ) -> None:
        ...

class DataTableReader(System.Data.IDataReader, System.IDisposable, System.Data.IDataRecord, System.Collections.IEnumerable, System.IAsyncDisposable, System.Data.Common.DbDataReader):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def Depth(self) -> System.Int32:
        ...

    @property
    def IsClosed(self) -> System.Boolean:
        ...

    @property
    def RecordsAffected(self) -> System.Int32:
        ...

    @property
    def HasRows(self) -> System.Boolean:
        ...

    @property
    def Item(self) -> System.Object:
        ...

    @property
    def Item(self) -> System.Object:
        ...

    @property
    def FieldCount(self) -> System.Int32:
        ...

    @property
    def VisibleFieldCount(self) -> System.Int32:
        ...

    # methods
    @typing.overload
    def __init__(self, dataTable: System.Data.DataTable, ):
        ...

    @typing.overload
    def __init__(self, dataTables: list[System.Data.DataTable], ):
        ...

    @typing.overload
    def Close(self, ) -> None:
        ...

    @typing.overload
    def GetSchemaTable(self, ) -> System.Data.DataTable:
        ...

    @typing.overload
    def NextResult(self, ) -> System.Boolean:
        ...

    @typing.overload
    def Read(self, ) -> System.Boolean:
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
    def GetBoolean(self, ordinal: System.Int32, ) -> System.Boolean:
        ...

    @typing.overload
    def GetByte(self, ordinal: System.Int32, ) -> System.Byte:
        ...

    @typing.overload
    def GetBytes(self, ordinal: System.Int32, dataIndex: System.Int64, buffer: list[System.Byte], bufferIndex: System.Int32, length: System.Int32, ) -> System.Int64:
        ...

    @typing.overload
    def GetChar(self, ordinal: System.Int32, ) -> System.Char:
        ...

    @typing.overload
    def GetChars(self, ordinal: System.Int32, dataIndex: System.Int64, buffer: list[System.Char], bufferIndex: System.Int32, length: System.Int32, ) -> System.Int64:
        ...

    @typing.overload
    def GetDataTypeName(self, ordinal: System.Int32, ) -> System.String:
        ...

    @typing.overload
    def GetDateTime(self, ordinal: System.Int32, ) -> System.DateTime:
        ...

    @typing.overload
    def GetDecimal(self, ordinal: System.Int32, ) -> System.Decimal:
        ...

    @typing.overload
    def GetDouble(self, ordinal: System.Int32, ) -> System.Double:
        ...

    @typing.overload
    def GetFieldType(self, ordinal: System.Int32, ) -> System.Type:
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
    def GetName(self, ordinal: System.Int32, ) -> System.String:
        ...

    @typing.overload
    def GetOrdinal(self, name: System.String, ) -> System.Int32:
        ...

    @typing.overload
    def GetString(self, ordinal: System.Int32, ) -> System.String:
        ...

    @typing.overload
    def GetValue(self, ordinal: System.Int32, ) -> System.Object:
        ...

    @typing.overload
    def GetValues(self, values: list[System.Object], ) -> System.Int32:
        ...

    @typing.overload
    def IsDBNull(self, ordinal: System.Int32, ) -> System.Boolean:
        ...

    @typing.overload
    def GetEnumerator(self, ) -> System.Collections.IEnumerator:
        ...

class XmlWriteMode(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    WriteSchema: System.Int32 = WriteSchema
    IgnoreSchema: System.Int32 = IgnoreSchema
    DiffGram: System.Int32 = DiffGram

class DataRowState(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    Detached: System.Int32 = Detached
    Unchanged: System.Int32 = Unchanged
    Added: System.Int32 = Added
    Deleted: System.Int32 = Deleted
    Modified: System.Int32 = Modified

class InternalDataCollectionBase(System.Collections.ICollection, System.Collections.IEnumerable, System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def Count(self) -> System.Int32:
        ...

    @property
    def IsReadOnly(self) -> System.Boolean:
        ...

    @property
    def IsSynchronized(self) -> System.Boolean:
        ...

    @property
    def SyncRoot(self) -> System.Object:
        ...

    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def CopyTo(self, ar: System.Array, index: System.Int32, ) -> None:
        ...

    @typing.overload
    def GetEnumerator(self, ) -> System.Collections.IEnumerator:
        ...

class DataRelation(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def ChildColumns(self) -> list[System.Data.DataColumn]:
        ...

    @property
    def ChildTable(self) -> System.Data.DataTable:
        ...

    @property
    def DataSet(self) -> System.Data.DataSet:
        ...

    @property
    def ParentColumns(self) -> list[System.Data.DataColumn]:
        ...

    @property
    def ParentTable(self) -> System.Data.DataTable:
        ...

    @property
    def RelationName(self) -> System.String:
        ...
    @RelationName.setter
    def RelationName(self, val: System.String):
        ...

    @property
    def Nested(self) -> System.Boolean:
        ...
    @Nested.setter
    def Nested(self, val: System.Boolean):
        ...

    @property
    def ParentKeyConstraint(self) -> System.Data.UniqueConstraint:
        ...

    @property
    def ChildKeyConstraint(self) -> System.Data.ForeignKeyConstraint:
        ...

    @property
    def ExtendedProperties(self) -> System.Data.PropertyCollection:
        ...

    # methods
    @typing.overload
    def __init__(self, relationName: System.String, parentColumn: System.Data.DataColumn, childColumn: System.Data.DataColumn, ):
        ...

    @typing.overload
    def __init__(self, relationName: System.String, parentColumn: System.Data.DataColumn, childColumn: System.Data.DataColumn, createConstraints: System.Boolean, ):
        ...

    @typing.overload
    def __init__(self, relationName: System.String, parentColumns: list[System.Data.DataColumn], childColumns: list[System.Data.DataColumn], ):
        ...

    @typing.overload
    def __init__(self, relationName: System.String, parentColumns: list[System.Data.DataColumn], childColumns: list[System.Data.DataColumn], createConstraints: System.Boolean, ):
        ...

    @typing.overload
    def __init__(self, relationName: System.String, parentTableName: System.String, childTableName: System.String, parentColumnNames: list[System.String], childColumnNames: list[System.String], nested: System.Boolean, ):
        ...

    @typing.overload
    def __init__(self, relationName: System.String, parentTableName: System.String, parentTableNamespace: System.String, childTableName: System.String, childTableNamespace: System.String, parentColumnNames: list[System.String], childColumnNames: list[System.String], nested: System.Boolean, ):
        ...

    @typing.overload
    def ToString(self, ) -> System.String:
        ...

class Constraint(System.Object, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def ConstraintName(self) -> System.String:
        ...
    @ConstraintName.setter
    def ConstraintName(self, val: System.String):
        ...

    @abc.abstractmethod
    @property
    def Table(self) -> System.Data.DataTable:
        ...

    @property
    def ExtendedProperties(self) -> System.Data.PropertyCollection:
        ...

    # methods
    @typing.overload
    def ToString(self, ) -> System.String:
        ...

class SchemaSerializationMode(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    IncludeSchema: System.Int32 = IncludeSchema
    ExcludeSchema: System.Int32 = ExcludeSchema

class DataViewManager(System.ComponentModel.IComponent, System.IDisposable, System.IServiceProvider, System.ComponentModel.IBindingList, System.Collections.IList, System.Collections.ICollection, System.Collections.IEnumerable, System.ComponentModel.ITypedList, System.ComponentModel.MarshalByValueComponent):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def DataSet(self) -> System.Data.DataSet:
        ...
    @DataSet.setter
    def DataSet(self, val: System.Data.DataSet):
        ...

    @property
    def DataViewSettings(self) -> System.Data.DataViewSettingCollection:
        ...

    @property
    def DataViewSettingCollectionString(self) -> System.String:
        ...
    @DataViewSettingCollectionString.setter
    def DataViewSettingCollectionString(self, val: System.String):
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
    def DesignMode(self) -> System.Boolean:
        ...

    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def __init__(self, dataSet: System.Data.DataSet, ):
        ...

    @typing.overload
    def CreateDataView(self, table: System.Data.DataTable, ) -> System.Data.DataView:
        ...

class DataTableCollection(System.Collections.ICollection, System.Collections.IEnumerable, System.Data.InternalDataCollectionBase):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def Item(self) -> System.Data.DataTable:
        ...

    @property
    def Item(self) -> System.Data.DataTable:
        ...

    @property
    def Item(self) -> System.Data.DataTable:
        ...

    @property
    def Count(self) -> System.Int32:
        ...

    @property
    def IsReadOnly(self) -> System.Boolean:
        ...

    @property
    def IsSynchronized(self) -> System.Boolean:
        ...

    @property
    def SyncRoot(self) -> System.Object:
        ...

    # methods
    @typing.overload
    def Add(self, table: System.Data.DataTable, ) -> None:
        ...

    @typing.overload
    def AddRange(self, tables: list[System.Data.DataTable], ) -> None:
        ...

    @typing.overload
    def Add(self, name: System.String, ) -> System.Data.DataTable:
        ...

    @typing.overload
    def Add(self, name: System.String, tableNamespace: System.String, ) -> System.Data.DataTable:
        ...

    @typing.overload
    def Add(self, ) -> System.Data.DataTable:
        ...

    @typing.overload
    def CanRemove(self, table: System.Data.DataTable, ) -> System.Boolean:
        ...

    @typing.overload
    def Clear(self, ) -> None:
        ...

    @typing.overload
    def Contains(self, name: System.String, ) -> System.Boolean:
        ...

    @typing.overload
    def Contains(self, name: System.String, tableNamespace: System.String, ) -> System.Boolean:
        ...

    @typing.overload
    def CopyTo(self, array: list[System.Data.DataTable], index: System.Int32, ) -> None:
        ...

    @typing.overload
    def IndexOf(self, table: System.Data.DataTable, ) -> System.Int32:
        ...

    @typing.overload
    def IndexOf(self, tableName: System.String, ) -> System.Int32:
        ...

    @typing.overload
    def IndexOf(self, tableName: System.String, tableNamespace: System.String, ) -> System.Int32:
        ...

    @typing.overload
    def Remove(self, table: System.Data.DataTable, ) -> None:
        ...

    @typing.overload
    def RemoveAt(self, index: System.Int32, ) -> None:
        ...

    @typing.overload
    def Remove(self, name: System.String, ) -> None:
        ...

    @typing.overload
    def Remove(self, name: System.String, tableNamespace: System.String, ) -> None:
        ...

class DataRowView(System.ComponentModel.ICustomTypeDescriptor, System.ComponentModel.IEditableObject, System.ComponentModel.IDataErrorInfo, System.ComponentModel.INotifyPropertyChanged, System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def DataView(self) -> System.Data.DataView:
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
    def RowVersion(self) -> System.Data.DataRowVersion:
        ...

    @property
    def Row(self) -> System.Data.DataRow:
        ...

    @property
    def IsNew(self) -> System.Boolean:
        ...

    @property
    def IsEdit(self) -> System.Boolean:
        ...

    # methods
    @typing.overload
    def Equals(self, other: System.Object, ) -> System.Boolean:
        ...

    @typing.overload
    def GetHashCode(self, ) -> System.Int32:
        ...

    @typing.overload
    def CreateChildView(self, relation: System.Data.DataRelation, followParent: System.Boolean, ) -> System.Data.DataView:
        ...

    @typing.overload
    def CreateChildView(self, relation: System.Data.DataRelation, ) -> System.Data.DataView:
        ...

    @typing.overload
    def CreateChildView(self, relationName: System.String, followParent: System.Boolean, ) -> System.Data.DataView:
        ...

    @typing.overload
    def CreateChildView(self, relationName: System.String, ) -> System.Data.DataView:
        ...

    @typing.overload
    def BeginEdit(self, ) -> None:
        ...

    @typing.overload
    def CancelEdit(self, ) -> None:
        ...

    @typing.overload
    def EndEdit(self, ) -> None:
        ...

    @typing.overload
    def Delete(self, ) -> None:
        ...

class DataSetDateTime(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    Local: System.Int32 = Local
    Unspecified: System.Int32 = Unspecified
    UnspecifiedLocal: System.Int32 = UnspecifiedLocal
    Utc: System.Int32 = Utc

class MappingType(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    Element: System.Int32 = Element
    Attribute: System.Int32 = Attribute
    SimpleContent: System.Int32 = SimpleContent
    Hidden: System.Int32 = Hidden

class FillErrorEventArgs(System.EventArgs):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def Continue(self) -> System.Boolean:
        ...
    @Continue.setter
    def Continue(self, val: System.Boolean):
        ...

    @property
    def DataTable(self) -> System.Data.DataTable:
        ...

    @property
    def Errors(self) -> System.Exception:
        ...
    @Errors.setter
    def Errors(self, val: System.Exception):
        ...

    @property
    def Values(self) -> list[System.Object]:
        ...

    # methods
    @typing.overload
    def __init__(self, dataTable: System.Data.DataTable, values: list[System.Object], ):
        ...

class UniqueConstraint(System.Data.Constraint):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def Columns(self) -> list[System.Data.DataColumn]:
        ...

    @property
    def IsPrimaryKey(self) -> System.Boolean:
        ...

    @property
    def Table(self) -> System.Data.DataTable:
        ...

    @property
    def ConstraintName(self) -> System.String:
        ...
    @ConstraintName.setter
    def ConstraintName(self, val: System.String):
        ...

    @property
    def ExtendedProperties(self) -> System.Data.PropertyCollection:
        ...

    # methods
    @typing.overload
    def __init__(self, name: System.String, column: System.Data.DataColumn, ):
        ...

    @typing.overload
    def __init__(self, column: System.Data.DataColumn, ):
        ...

    @typing.overload
    def __init__(self, name: System.String, columns: list[System.Data.DataColumn], ):
        ...

    @typing.overload
    def __init__(self, columns: list[System.Data.DataColumn], ):
        ...

    @typing.overload
    def __init__(self, name: System.String, columnNames: list[System.String], isPrimaryKey: System.Boolean, ):
        ...

    @typing.overload
    def __init__(self, name: System.String, column: System.Data.DataColumn, isPrimaryKey: System.Boolean, ):
        ...

    @typing.overload
    def __init__(self, column: System.Data.DataColumn, isPrimaryKey: System.Boolean, ):
        ...

    @typing.overload
    def __init__(self, name: System.String, columns: list[System.Data.DataColumn], isPrimaryKey: System.Boolean, ):
        ...

    @typing.overload
    def __init__(self, columns: list[System.Data.DataColumn], isPrimaryKey: System.Boolean, ):
        ...

    @typing.overload
    def Equals(self, key2: System.Object, ) -> System.Boolean:
        ...

    @typing.overload
    def GetHashCode(self, ) -> System.Int32:
        ...

class ForeignKeyConstraint(System.Data.Constraint):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def Columns(self) -> list[System.Data.DataColumn]:
        ...

    @property
    def Table(self) -> System.Data.DataTable:
        ...

    @property
    def AcceptRejectRule(self) -> System.Data.AcceptRejectRule:
        ...
    @AcceptRejectRule.setter
    def AcceptRejectRule(self, val: System.Data.AcceptRejectRule):
        ...

    @property
    def DeleteRule(self) -> System.Data.Rule:
        ...
    @DeleteRule.setter
    def DeleteRule(self, val: System.Data.Rule):
        ...

    @property
    def RelatedColumns(self) -> list[System.Data.DataColumn]:
        ...

    @property
    def RelatedTable(self) -> System.Data.DataTable:
        ...

    @property
    def UpdateRule(self) -> System.Data.Rule:
        ...
    @UpdateRule.setter
    def UpdateRule(self, val: System.Data.Rule):
        ...

    @property
    def ConstraintName(self) -> System.String:
        ...
    @ConstraintName.setter
    def ConstraintName(self, val: System.String):
        ...

    @property
    def ExtendedProperties(self) -> System.Data.PropertyCollection:
        ...

    # methods
    @typing.overload
    def __init__(self, parentColumn: System.Data.DataColumn, childColumn: System.Data.DataColumn, ):
        ...

    @typing.overload
    def __init__(self, constraintName: System.String, parentColumn: System.Data.DataColumn, childColumn: System.Data.DataColumn, ):
        ...

    @typing.overload
    def __init__(self, parentColumns: list[System.Data.DataColumn], childColumns: list[System.Data.DataColumn], ):
        ...

    @typing.overload
    def __init__(self, constraintName: System.String, parentColumns: list[System.Data.DataColumn], childColumns: list[System.Data.DataColumn], ):
        ...

    @typing.overload
    def __init__(self, constraintName: System.String, parentTableName: System.String, parentColumnNames: list[System.String], childColumnNames: list[System.String], acceptRejectRule: System.Data.AcceptRejectRule, deleteRule: System.Data.Rule, updateRule: System.Data.Rule, ):
        ...

    @typing.overload
    def __init__(self, constraintName: System.String, parentTableName: System.String, parentTableNamespace: System.String, parentColumnNames: list[System.String], childColumnNames: list[System.String], acceptRejectRule: System.Data.AcceptRejectRule, deleteRule: System.Data.Rule, updateRule: System.Data.Rule, ):
        ...

    @typing.overload
    def Equals(self, key: System.Object, ) -> System.Boolean:
        ...

    @typing.overload
    def GetHashCode(self, ) -> System.Int32:
        ...

class DataViewSettingCollection(System.Collections.ICollection, System.Collections.IEnumerable, System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def Item(self) -> System.Data.DataViewSetting:
        ...
    @Item.setter
    def Item(self, val: System.Data.DataViewSetting):
        ...

    @property
    def Item(self) -> System.Data.DataViewSetting:
        ...

    @property
    def Item(self) -> System.Data.DataViewSetting:
        ...
    @Item.setter
    def Item(self, val: System.Data.DataViewSetting):
        ...

    @property
    def Count(self) -> System.Int32:
        ...

    @property
    def IsReadOnly(self) -> System.Boolean:
        ...

    @property
    def IsSynchronized(self) -> System.Boolean:
        ...

    @property
    def SyncRoot(self) -> System.Object:
        ...

    # methods
    @typing.overload
    def CopyTo(self, ar: System.Array, index: System.Int32, ) -> None:
        ...

    @typing.overload
    def CopyTo(self, ar: list[System.Data.DataViewSetting], index: System.Int32, ) -> None:
        ...

    @typing.overload
    def GetEnumerator(self, ) -> System.Collections.IEnumerator:
        ...

class AcceptRejectRule(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    None_: System.Int32 = None
    Cascade: System.Int32 = Cascade

class Rule(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    None_: System.Int32 = None
    Cascade: System.Int32 = Cascade
    SetNull: System.Int32 = SetNull
    SetDefault: System.Int32 = SetDefault

class DataViewSetting(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def ApplyDefaultSort(self) -> System.Boolean:
        ...
    @ApplyDefaultSort.setter
    def ApplyDefaultSort(self, val: System.Boolean):
        ...

    @property
    def DataViewManager(self) -> System.Data.DataViewManager:
        ...

    @property
    def Table(self) -> System.Data.DataTable:
        ...

    @property
    def RowFilter(self) -> System.String:
        ...
    @RowFilter.setter
    def RowFilter(self, val: System.String):
        ...

    @property
    def RowStateFilter(self) -> System.Data.DataViewRowState:
        ...
    @RowStateFilter.setter
    def RowStateFilter(self, val: System.Data.DataViewRowState):
        ...

    @property
    def Sort(self) -> System.String:
        ...
    @Sort.setter
    def Sort(self, val: System.String):
        ...

    # methods
