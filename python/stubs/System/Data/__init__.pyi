from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import System
import System.Data
import System.ComponentModel
import System.Runtime.Serialization
import System.Xml.Serialization
import System.Collections.Generic
import System.Collections
import System.Threading
import System.Globalization
import System.Xml
import System.IO
import System.Xml.Schema
import System.Reflection
import System.Data.Index
import System.Data.DataSet
import System.Data.Common

TKey = typing.TypeVar('TKey')
TRow = typing.TypeVar('TRow')

class IDataRecord(abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    @abc.abstractmethod
    def FieldCount(self) -> int:
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
    @abc.abstractmethod
    def GetName(self, i: int, ) -> str:
        ...

    @abc.abstractmethod
    def GetDataTypeName(self, i: int, ) -> str:
        ...

    @abc.abstractmethod
    def GetFieldType(self, i: int, ) -> System.Type:
        ...

    @abc.abstractmethod
    def GetValue(self, i: int, ) -> System.Object:
        ...

    @abc.abstractmethod
    def GetValues(self, values: System.Array[System.Object], ) -> int:
        ...

    @abc.abstractmethod
    def GetOrdinal(self, name: str, ) -> int:
        ...

    @abc.abstractmethod
    def GetBoolean(self, i: int, ) -> bool:
        ...

    @abc.abstractmethod
    def GetByte(self, i: int, ) -> int:
        ...

    @abc.abstractmethod
    def GetBytes(self, i: int, fieldOffset: int, buffer: System.Array[int], bufferoffset: int, length: int, ) -> int:
        ...

    @abc.abstractmethod
    def GetChar(self, i: int, ) -> str:
        ...

    @abc.abstractmethod
    def GetChars(self, i: int, fieldoffset: int, buffer: System.Array[str], bufferoffset: int, length: int, ) -> int:
        ...

    @abc.abstractmethod
    def GetGuid(self, i: int, ) -> System.Guid:
        ...

    @abc.abstractmethod
    def GetInt16(self, i: int, ) -> int:
        ...

    @abc.abstractmethod
    def GetInt32(self, i: int, ) -> int:
        ...

    @abc.abstractmethod
    def GetInt64(self, i: int, ) -> int:
        ...

    @abc.abstractmethod
    def GetFloat(self, i: int, ) -> float:
        ...

    @abc.abstractmethod
    def GetDouble(self, i: int, ) -> float:
        ...

    @abc.abstractmethod
    def GetString(self, i: int, ) -> str:
        ...

    @abc.abstractmethod
    def GetDecimal(self, i: int, ) -> System.Decimal:
        ...

    @abc.abstractmethod
    def GetDateTime(self, i: int, ) -> System.DateTime:
        ...

    @abc.abstractmethod
    def GetData(self, i: int, ) -> System.Data.IDataReader:
        ...

    @abc.abstractmethod
    def IsDBNull(self, i: int, ) -> bool:
        ...

class DataTable(System.ComponentModel.IComponent, System.IDisposable, System.IServiceProvider, System.ComponentModel.IListSource, System.ComponentModel.ISupportInitializeNotification, System.ComponentModel.ISupportInitialize, System.Runtime.Serialization.ISerializable, System.Xml.Serialization.IXmlSerializable, System.ComponentModel.MarshalByValueComponent):
    @typing.overload
    def __init__(self, **kwargs):
        self._nextRowID: int
        self._rowCollection: System.Data.DataRowCollection
        self._columnCollection: System.Data.DataColumnCollection
        self._parentRelationsCollection: System.Data.DataRelationCollection
        self._childRelationsCollection: System.Data.DataRelationCollection
        self._recordManager: System.Data.RecordManager
        self._indexes: System.Collections.Generic.List[System.Data.Index]
        self._extendedProperties: System.Data.PropertyCollection
        self._tableNamespace: str
        self._displayExpression: System.Data.DataExpression
        self._fNestedInDataset: bool
        self._encodedTableName: str
        self._xmlText: System.Data.DataColumn
        self._colUnique: System.Data.DataColumn
        self._minOccurs: System.Decimal
        self._maxOccurs: System.Decimal
        self._repeatableElement: bool
        self._primaryKey: System.Data.UniqueConstraint
        self._primaryIndex: System.Array[System.Data.IndexField]
        self._suspendEnforceConstraints: bool
        self.fInitInProgress: bool
        self._fInLoadDiffgram: bool
        self._dependentColumns: System.Collections.Generic.List[System.Data.DataColumn]
        self._delayedViews: System.Collections.Generic.List[System.Data.DataView]
        self._rowDiffId: System.Collections.Hashtable
        self._indexesLock: System.Threading.ReaderWriterLockSlim
        self._ukColumnPositionForInference: int
        ...

    # static fields

    # properties
    @property
    def CaseSensitive(self) -> bool:
        ...
    @CaseSensitive.setter
    def CaseSensitive(self, val: bool):
        ...

    @property
    def AreIndexEventsSuspended(self) -> bool:
        ...

    @property
    def IsInitialized(self) -> bool:
        ...

    @property
    def IsTypedDataTable(self) -> bool:
        ...

    @property
    def SelfNested(self) -> bool:
        ...

    @property
    def LiveIndexes(self) -> System.Collections.Generic.List[System.Data.Index]:
        ...

    @property
    def RemotingFormat(self) -> int:
        ...
    @RemotingFormat.setter
    def RemotingFormat(self, val: int):
        ...

    @property
    def UKColumnPositionForInference(self) -> int:
        ...
    @UKColumnPositionForInference.setter
    def UKColumnPositionForInference(self, val: int):
        ...

    @property
    def ChildRelations(self) -> System.Data.DataRelationCollection:
        ...

    @property
    def Columns(self) -> System.Data.DataColumnCollection:
        ...

    @property
    def CompareInfo(self) -> System.Globalization.CompareInfo:
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
    def DisplayExpression(self) -> str:
        ...
    @DisplayExpression.setter
    def DisplayExpression(self, val: str):
        ...

    @property
    def DisplayExpressionInternal(self) -> str:
        ...

    @property
    def EnforceConstraints(self) -> bool:
        ...
    @EnforceConstraints.setter
    def EnforceConstraints(self, val: bool):
        ...

    @property
    def SuspendEnforceConstraints(self) -> bool:
        ...
    @SuspendEnforceConstraints.setter
    def SuspendEnforceConstraints(self, val: bool):
        ...

    @property
    def ExtendedProperties(self) -> System.Data.PropertyCollection:
        ...

    @property
    def FormatProvider(self) -> System.IFormatProvider:
        ...

    @property
    def HasErrors(self) -> bool:
        ...

    @property
    def Locale(self) -> System.Globalization.CultureInfo:
        ...
    @Locale.setter
    def Locale(self, val: System.Globalization.CultureInfo):
        ...

    @property
    def MinimumCapacity(self) -> int:
        ...
    @MinimumCapacity.setter
    def MinimumCapacity(self, val: int):
        ...

    @property
    def RecordCapacity(self) -> int:
        ...

    @property
    def ElementColumnCount(self) -> int:
        ...
    @ElementColumnCount.setter
    def ElementColumnCount(self, val: int):
        ...

    @property
    def ParentRelations(self) -> System.Data.DataRelationCollection:
        ...

    @property
    def MergingData(self) -> bool:
        ...
    @MergingData.setter
    def MergingData(self, val: bool):
        ...

    @property
    def NestedParentRelations(self) -> System.Array[System.Data.DataRelation]:
        ...

    @property
    def NestedParentsCount(self) -> int:
        ...

    @property
    def PrimaryKey(self) -> System.Array[System.Data.DataColumn]:
        ...
    @PrimaryKey.setter
    def PrimaryKey(self, val: System.Array[System.Data.DataColumn]):
        ...

    @property
    def Rows(self) -> System.Data.DataRowCollection:
        ...

    @property
    def TableName(self) -> str:
        ...
    @TableName.setter
    def TableName(self, val: str):
        ...

    @property
    def EncodedTableName(self) -> str:
        ...

    @property
    def Namespace(self) -> str:
        ...
    @Namespace.setter
    def Namespace(self, val: str):
        ...

    @property
    def Prefix(self) -> str:
        ...
    @Prefix.setter
    def Prefix(self, val: str):
        ...

    @property
    def XmlText(self) -> System.Data.DataColumn:
        ...
    @XmlText.setter
    def XmlText(self, val: System.Data.DataColumn):
        ...

    @property
    def MaxOccurs(self) -> System.Decimal:
        ...
    @MaxOccurs.setter
    def MaxOccurs(self, val: System.Decimal):
        ...

    @property
    def MinOccurs(self) -> System.Decimal:
        ...
    @MinOccurs.setter
    def MinOccurs(self, val: System.Decimal):
        ...

    @property
    def Site(self) -> System.ComponentModel.ISite:
        ...
    @Site.setter
    def Site(self, val: System.ComponentModel.ISite):
        ...

    @property
    def ContainsListCollection(self) -> bool:
        ...

    @property
    def NeedColumnChangeEvents(self) -> bool:
        ...

    @property
    def TypeName(self) -> System.Xml.XmlQualifiedName:
        ...
    @TypeName.setter
    def TypeName(self, val: System.Xml.XmlQualifiedName):
        ...

    @property
    def RowDiffId(self) -> System.Collections.Hashtable:
        ...

    @property
    def ObjectID(self) -> int:
        ...

    @property
    def Events(self) -> System.ComponentModel.EventHandlerList:
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
    def __init__(self, tableName: str, ):
        ...

    @typing.overload
    def __init__(self, tableName: str, tableNamespace: str, ):
        ...

    @typing.overload
    def __init__(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext, ):
        ...

    @typing.overload
    def WriteXmlSchema(self, stream: System.IO.Stream, writeHierarchy: bool, ) -> None:
        ...

    @typing.overload
    def WriteXmlSchema(self, writer: System.IO.TextWriter, ) -> None:
        ...

    @typing.overload
    def WriteXmlSchema(self, writer: System.IO.TextWriter, writeHierarchy: bool, ) -> None:
        ...

    @typing.overload
    def WriteXmlSchema(self, writer: System.Xml.XmlWriter, ) -> None:
        ...

    @typing.overload
    def WriteXmlSchema(self, writer: System.Xml.XmlWriter, writeHierarchy: bool, ) -> None:
        ...

    @typing.overload
    def WriteXmlSchema(self, fileName: str, ) -> None:
        ...

    @typing.overload
    def WriteXmlSchema(self, fileName: str, writeHierarchy: bool, ) -> None:
        ...

    @typing.overload
    def WriteXmlSchema(self, stream: System.IO.Stream, ) -> None:
        ...

    def CheckForClosureOnExpressions(self, dt: System.Data.DataTable, writeHierarchy: bool, ) -> bool:
        ...

    def CheckForClosureOnExpressionTables(self, tableList: System.Collections.Generic.List[System.Data.DataTable], ) -> bool:
        ...

    @typing.overload
    def ReadXml(self, stream: System.IO.Stream, ) -> int:
        ...

    @typing.overload
    def ReadXml(self, reader: System.IO.TextReader, ) -> int:
        ...

    @typing.overload
    def ReadXml(self, fileName: str, ) -> int:
        ...

    @typing.overload
    def ReadXml(self, reader: System.Xml.XmlReader, ) -> int:
        ...

    @typing.overload
    def ReadXml(self, reader: System.Xml.XmlReader, denyResolving: bool, ) -> int:
        ...

    @typing.overload
    def ReadXml(self, reader: System.Xml.XmlReader, mode: int, denyResolving: bool, ) -> int:
        ...

    def RestoreConstraint(self, originalEnforceConstraint: bool, ) -> None:
        ...

    def IsEmptyXml(self, reader: System.Xml.XmlReader, ) -> bool:
        ...

    def ReadEndElement(self, reader: System.Xml.XmlReader, ) -> None:
        ...

    def ReadXDRSchema(self, reader: System.Xml.XmlReader, ) -> None:
        ...

    def MoveToElement(self, reader: System.Xml.XmlReader, depth: int, ) -> bool:
        ...

    def ReadXmlDiffgram(self, reader: System.Xml.XmlReader, ) -> None:
        ...

    def ReadXSDSchema(self, reader: System.Xml.XmlReader, denyResolving: bool, ) -> None:
        ...

    @typing.overload
    def ReadXmlSchema(self, stream: System.IO.Stream, ) -> None:
        ...

    @typing.overload
    def ReadXmlSchema(self, reader: System.IO.TextReader, ) -> None:
        ...

    @typing.overload
    def ReadXmlSchema(self, fileName: str, ) -> None:
        ...

    @typing.overload
    def ReadXmlSchema(self, reader: System.Xml.XmlReader, ) -> None:
        ...

    @typing.overload
    def ReadXmlSchema(self, reader: System.Xml.XmlReader, denyResolving: bool, ) -> None:
        ...

    def CreateTableList(self, currentTable: System.Data.DataTable, tableList: System.Collections.Generic.List[System.Data.DataTable], ) -> None:
        ...

    def CreateRelationList(self, tableList: System.Collections.Generic.List[System.Data.DataTable], relationList: System.Collections.Generic.List[System.Data.DataRelation], ) -> None:
        ...

    @staticmethod
    def GetDataTableSchema(schemaSet: System.Xml.Schema.XmlSchemaSet, ) -> System.Xml.Schema.XmlSchemaComplexType:
        ...

    def GetSchema(self, ) -> System.Xml.Schema.XmlSchema:
        ...

    def GetSchema(self, ) -> System.Xml.Schema.XmlSchema:
        ...

    def GetXmlSchema(self, ) -> System.Xml.Schema.XmlSchema:
        ...

    def ReadXml(self, reader: System.Xml.XmlReader, ) -> None:
        ...

    def ReadXmlSerializableInternal(self, reader: System.Xml.XmlReader, ) -> None:
        ...

    def WriteXml(self, writer: System.Xml.XmlWriter, ) -> None:
        ...

    def WriteXmlInternal(self, writer: System.Xml.XmlWriter, ) -> None:
        ...

    def ReadXmlSerializable(self, reader: System.Xml.XmlReader, ) -> None:
        ...

    def AddDependentColumn(self, expressionColumn: System.Data.DataColumn, ) -> None:
        ...

    def RemoveDependentColumn(self, expressionColumn: System.Data.DataColumn, ) -> None:
        ...

    @typing.overload
    def EvaluateExpressions(self, ) -> None:
        ...

    @typing.overload
    def EvaluateExpressions(self, row: System.Data.DataRow, action: int, cachedRows: System.Collections.Generic.List[System.Data.DataRow], ) -> None:
        ...

    @typing.overload
    def EvaluateExpressions(self, column: System.Data.DataColumn, ) -> None:
        ...

    @typing.overload
    def EvaluateDependentExpressions(self, column: System.Data.DataColumn, ) -> None:
        ...

    @typing.overload
    def EvaluateDependentExpressions(self, columns: System.Collections.Generic.List[System.Data.DataColumn], row: System.Data.DataRow, version: int, cachedRows: System.Collections.Generic.List[System.Data.DataRow], ) -> None:
        ...

    def CreateEmptyRow(self, ) -> System.Data.DataRow:
        ...

    def NewRowCreated(self, row: System.Data.DataRow, ) -> None:
        ...

    @typing.overload
    def NewRow(self, record: int, ) -> System.Data.DataRow:
        ...

    @typing.overload
    def NewRow(self, ) -> System.Data.DataRow:
        ...

    def NewRowFromBuilder(self, builder: System.Data.DataRowBuilder, ) -> System.Data.DataRow:
        ...

    def GetRowType(self, ) -> System.Type:
        ...

    def NewRowArray(self, size: int, ) -> System.Array[System.Data.DataRow]:
        ...

    def OnColumnChanging(self, e: System.Data.DataColumnChangeEventArgs, ) -> None:
        ...

    def OnColumnChanged(self, e: System.Data.DataColumnChangeEventArgs, ) -> None:
        ...

    def OnPropertyChanging(self, pcevent: System.ComponentModel.PropertyChangedEventArgs, ) -> None:
        ...

    def OnRemoveColumnInternal(self, column: System.Data.DataColumn, ) -> None:
        ...

    def OnRemoveColumn(self, column: System.Data.DataColumn, ) -> None:
        ...

    @typing.overload
    def OnRowChanged(self, args: System.Data.DataRowChangeEventArgs, eRow: System.Data.DataRow, eAction: int, ) -> System.Data.DataRowChangeEventArgs:
        ...

    @typing.overload
    def OnRowChanged(self, e: System.Data.DataRowChangeEventArgs, ) -> None:
        ...

    @typing.overload
    def OnRowChanging(self, args: System.Data.DataRowChangeEventArgs, eRow: System.Data.DataRow, eAction: int, ) -> System.Data.DataRowChangeEventArgs:
        ...

    @typing.overload
    def OnRowChanging(self, e: System.Data.DataRowChangeEventArgs, ) -> None:
        ...

    def OnRowDeleting(self, e: System.Data.DataRowChangeEventArgs, ) -> None:
        ...

    def OnRowDeleted(self, e: System.Data.DataRowChangeEventArgs, ) -> None:
        ...

    def OnTableCleared(self, e: System.Data.DataTableClearEventArgs, ) -> None:
        ...

    def OnTableClearing(self, e: System.Data.DataTableClearEventArgs, ) -> None:
        ...

    def OnTableNewRow(self, e: System.Data.DataTableNewRowEventArgs, ) -> None:
        ...

    def OnInitialized(self, ) -> None:
        ...

    def ParseSortString(self, sortString: str, ) -> System.Array[System.Data.IndexField]:
        ...

    def RaisePropertyChanging(self, name: str, ) -> None:
        ...

    @typing.overload
    def RecordChanged(self, record: int, ) -> None:
        ...

    @typing.overload
    def RecordChanged(self, oldIndex: System.Array[int], newIndex: System.Array[int], ) -> None:
        ...

    @typing.overload
    def RecordStateChanged(self, record: int, oldState: int, newState: int, ) -> None:
        ...

    @typing.overload
    def RecordStateChanged(self, record1: int, oldState1: int, newState1: int, record2: int, oldState2: int, newState2: int, ) -> None:
        ...

    def RemoveRecordFromIndexes(self, row: System.Data.DataRow, version: int, ) -> System.Array[int]:
        ...

    def InsertRecordToIndexes(self, row: System.Data.DataRow, version: int, ) -> System.Array[int]:
        ...

    def SilentlySetValue(self, dr: System.Data.DataRow, dc: System.Data.DataColumn, version: int, newValue: System.Object, ) -> None:
        ...

    def RejectChanges(self, ) -> None:
        ...

    def RemoveRow(self, row: System.Data.DataRow, check: bool, ) -> None:
        ...

    def Reset(self, ) -> None:
        ...

    def ResetIndexes(self, ) -> None:
        ...

    def ResetInternalIndexes(self, column: System.Data.DataColumn, ) -> None:
        ...

    def RollbackRow(self, row: System.Data.DataRow, ) -> None:
        ...

    def RaiseRowChanged(self, args: System.Data.DataRowChangeEventArgs, eRow: System.Data.DataRow, eAction: int, ) -> System.Data.DataRowChangeEventArgs:
        ...

    @typing.overload
    def RaiseRowChanging(self, args: System.Data.DataRowChangeEventArgs, eRow: System.Data.DataRow, eAction: int, ) -> System.Data.DataRowChangeEventArgs:
        ...

    @typing.overload
    def RaiseRowChanging(self, args: System.Data.DataRowChangeEventArgs, eRow: System.Data.DataRow, eAction: int, fireEvent: bool, ) -> System.Data.DataRowChangeEventArgs:
        ...

    @typing.overload
    def Select(self, ) -> System.Array[System.Data.DataRow]:
        ...

    @typing.overload
    def Select(self, filterExpression: str, ) -> System.Array[System.Data.DataRow]:
        ...

    @typing.overload
    def Select(self, filterExpression: str, sort: str, ) -> System.Array[System.Data.DataRow]:
        ...

    @typing.overload
    def Select(self, filterExpression: str, sort: str, recordStates: int, ) -> System.Array[System.Data.DataRow]:
        ...

    def SetNewRecord(self, row: System.Data.DataRow, proposedRecord: int, action: int = ..., isInMerge: bool = ..., fireEvent: bool = ..., suppressEnsurePropertyChanged: bool = ..., ) -> None:
        ...

    def SetNewRecordWorker(self, row: System.Data.DataRow, proposedRecord: int, action: int, isInMerge: bool, suppressEnsurePropertyChanged: bool, position: int, fireEvent: bool, deferredException: ref[System.Exception], ) -> None:
        ...

    def SetOldRecord(self, row: System.Data.DataRow, proposedRecord: int, ) -> None:
        ...

    def RestoreShadowIndexes(self, ) -> None:
        ...

    def SetShadowIndexes(self, ) -> None:
        ...

    def ShadowIndexCopy(self, ) -> None:
        ...

    def ToString(self, ) -> str:
        ...

    def BeginLoadData(self, ) -> None:
        ...

    def EndLoadData(self, ) -> None:
        ...

    @typing.overload
    def LoadDataRow(self, values: System.Array[System.Object], fAcceptChanges: bool, ) -> System.Data.DataRow:
        ...

    @typing.overload
    def LoadDataRow(self, values: System.Array[System.Object], loadOption: int, ) -> System.Data.DataRow:
        ...

    def UpdatingAdd(self, values: System.Array[System.Object], ) -> System.Data.DataRow:
        ...

    def UpdatingCurrent(self, row: System.Data.DataRow, action: int, ) -> bool:
        ...

    @typing.overload
    def AddUniqueKey(self, position: int, ) -> System.Data.DataColumn:
        ...

    @typing.overload
    def AddUniqueKey(self, ) -> System.Data.DataColumn:
        ...

    def AddForeignKey(self, parentKey: System.Data.DataColumn, ) -> System.Data.DataColumn:
        ...

    def UpdatePropertyDescriptorCollectionCache(self, ) -> None:
        ...

    def GetPropertyDescriptorCollection(self, attributes: System.Array[System.Attribute], ) -> System.ComponentModel.PropertyDescriptorCollection:
        ...

    @typing.overload
    def Merge(self, table: System.Data.DataTable, ) -> None:
        ...

    @typing.overload
    def Merge(self, table: System.Data.DataTable, preserveChanges: bool, ) -> None:
        ...

    @typing.overload
    def Merge(self, table: System.Data.DataTable, preserveChanges: bool, missingSchemaAction: int, ) -> None:
        ...

    @typing.overload
    def Load(self, reader: System.Data.IDataReader, ) -> None:
        ...

    @typing.overload
    def Load(self, reader: System.Data.IDataReader, loadOption: int, ) -> None:
        ...

    @typing.overload
    def Load(self, reader: System.Data.IDataReader, loadOption: int, errorHandler: System.Data.FillErrorEventHandler, ) -> None:
        ...

    def LoadRow(self, values: System.Array[System.Object], loadOption: int, searchIndex: System.Data.Index, ) -> System.Data.DataRow:
        ...

    def SetDataRowWithLoadOption(self, dataRow: System.Data.DataRow, recordNo: int, loadOption: int, checkReadOnly: bool, ) -> None:
        ...

    def CreateDataReader(self, ) -> System.Data.DataTableReader:
        ...

    @typing.overload
    def WriteXml(self, stream: System.IO.Stream, ) -> None:
        ...

    @typing.overload
    def WriteXml(self, stream: System.IO.Stream, writeHierarchy: bool, ) -> None:
        ...

    @typing.overload
    def WriteXml(self, writer: System.IO.TextWriter, ) -> None:
        ...

    @typing.overload
    def WriteXml(self, writer: System.IO.TextWriter, writeHierarchy: bool, ) -> None:
        ...

    @typing.overload
    def WriteXml(self, writer: System.Xml.XmlWriter, ) -> None:
        ...

    @typing.overload
    def WriteXml(self, writer: System.Xml.XmlWriter, writeHierarchy: bool, ) -> None:
        ...

    @typing.overload
    def WriteXml(self, fileName: str, ) -> None:
        ...

    @typing.overload
    def WriteXml(self, fileName: str, writeHierarchy: bool, ) -> None:
        ...

    @typing.overload
    def WriteXml(self, stream: System.IO.Stream, mode: int, ) -> None:
        ...

    @typing.overload
    def WriteXml(self, stream: System.IO.Stream, mode: int, writeHierarchy: bool, ) -> None:
        ...

    @typing.overload
    def WriteXml(self, writer: System.IO.TextWriter, mode: int, ) -> None:
        ...

    @typing.overload
    def WriteXml(self, writer: System.IO.TextWriter, mode: int, writeHierarchy: bool, ) -> None:
        ...

    @typing.overload
    def WriteXml(self, writer: System.Xml.XmlWriter, mode: int, ) -> None:
        ...

    @typing.overload
    def WriteXml(self, writer: System.Xml.XmlWriter, mode: int, writeHierarchy: bool, ) -> None:
        ...

    @typing.overload
    def WriteXml(self, fileName: str, mode: int, ) -> None:
        ...

    @typing.overload
    def WriteXml(self, fileName: str, mode: int, writeHierarchy: bool, ) -> None:
        ...

    def SetKeyValues(self, key: System.Data.DataKey, keyValues: System.Array[System.Object], record: int, ) -> None:
        ...

    def FindByIndex(self, ndx: System.Data.Index, key: System.Array[System.Object], ) -> System.Data.DataRow:
        ...

    def FindMergeTarget(self, row: System.Data.DataRow, key: System.Data.DataKey, ndx: System.Data.Index, ) -> System.Data.DataRow:
        ...

    def SetMergeRecords(self, row: System.Data.DataRow, newRecord: int, oldRecord: int, action: int, ) -> None:
        ...

    def MergeRow(self, row: System.Data.DataRow, targetRow: System.Data.DataRow, preserveChanges: bool, idxSearch: System.Data.Index, ) -> System.Data.DataRow:
        ...

    def AcceptChanges(self, ) -> None:
        ...

    def CreateInstance(self, ) -> System.Data.DataTable:
        ...

    @typing.overload
    def Clone(self, ) -> System.Data.DataTable:
        ...

    @typing.overload
    def Clone(self, cloneDS: System.Data.DataSet, ) -> System.Data.DataTable:
        ...

    def IncrementalCloneTo(self, sourceTable: System.Data.DataTable, targetTable: System.Data.DataTable, ) -> System.Data.DataTable:
        ...

    def CloneHierarchy(self, sourceTable: System.Data.DataTable, ds: System.Data.DataSet, visitedMap: System.Collections.Hashtable, ) -> System.Data.DataTable:
        ...

    def CloneTo(self, clone: System.Data.DataTable, cloneDS: System.Data.DataSet, skipExpressionColumns: bool, ) -> System.Data.DataTable:
        ...

    def Copy(self, ) -> System.Data.DataTable:
        ...

    def AddRecords(self, oldRecord: int, newRecord: int, ) -> System.Data.DataRow:
        ...

    @typing.overload
    def AddRow(self, row: System.Data.DataRow, ) -> None:
        ...

    @typing.overload
    def AddRow(self, row: System.Data.DataRow, proposedID: int, ) -> None:
        ...

    @typing.overload
    def InsertRow(self, row: System.Data.DataRow, proposedID: int, pos: int, ) -> None:
        ...

    @typing.overload
    def InsertRow(self, row: System.Data.DataRow, proposedID: int, pos: int, fireEvent: bool, ) -> None:
        ...

    @typing.overload
    def InsertRow(self, row: System.Data.DataRow, proposedID: int, ) -> None:
        ...

    def CheckNotModifying(self, row: System.Data.DataRow, ) -> None:
        ...

    @typing.overload
    def Clear(self, ) -> None:
        ...

    @typing.overload
    def Clear(self, clearAll: bool, ) -> None:
        ...

    def CascadeAll(self, row: System.Data.DataRow, action: int, ) -> None:
        ...

    def CommitRow(self, row: System.Data.DataRow, ) -> None:
        ...

    @typing.overload
    def Compare(self, s1: str, s2: str, ) -> int:
        ...

    @typing.overload
    def Compare(self, s1: str, s2: str, comparer: System.Globalization.CompareInfo, ) -> int:
        ...

    def IndexOf(self, s1: str, s2: str, ) -> int:
        ...

    def IsSuffix(self, s1: str, s2: str, ) -> bool:
        ...

    def Compute(self, expression: str, filter: str, ) -> System.Object:
        ...

    def CopyRow(self, table: System.Data.DataTable, row: System.Data.DataRow, ) -> None:
        ...

    def DeleteRow(self, row: System.Data.DataRow, ) -> None:
        ...

    def CheckPrimaryKey(self, ) -> None:
        ...

    @typing.overload
    def FindByPrimaryKey(self, values: System.Array[System.Object], ) -> System.Data.DataRow:
        ...

    @typing.overload
    def FindByPrimaryKey(self, value: System.Object, ) -> System.Data.DataRow:
        ...

    @typing.overload
    def FindRow(self, key: System.Data.DataKey, values: System.Array[System.Object], ) -> System.Data.DataRow:
        ...

    @typing.overload
    def FindRow(self, key: System.Data.DataKey, value: System.Object, ) -> System.Data.DataRow:
        ...

    def FormatSortString(self, indexDesc: System.Array[System.Data.IndexField], ) -> str:
        ...

    def FreeRecord(self, record: ref[int], ) -> None:
        ...

    @typing.overload
    def GetChanges(self, ) -> System.Data.DataTable:
        ...

    @typing.overload
    def GetChanges(self, rowStates: int, ) -> System.Data.DataTable:
        ...

    def GetErrors(self, ) -> System.Array[System.Data.DataRow]:
        ...

    @typing.overload
    def GetIndex(self, indexDesc: System.Array[System.Data.IndexField], ) -> System.Data.Index:
        ...

    @typing.overload
    def GetIndex(self, sort: str, recordStates: int, rowFilter: System.Data.IFilter, ) -> System.Data.Index:
        ...

    @typing.overload
    def GetIndex(self, indexDesc: System.Array[System.Data.IndexField], recordStates: int, rowFilter: System.Data.IFilter, ) -> System.Data.Index:
        ...

    def GetList(self, ) -> System.Collections.IList:
        ...

    def GetListeners(self, ) -> System.Collections.Generic.List[System.Data.DataViewListener]:
        ...

    def GetSpecialHashCode(self, name: str, ) -> int:
        ...

    def ImportRow(self, row: System.Data.DataRow, ) -> None:
        ...

    def NewIndexDesc(self, key: System.Data.DataKey, ) -> System.Array[System.Data.IndexField]:
        ...

    @typing.overload
    def NewRecord(self, ) -> int:
        ...

    @typing.overload
    def NewRecord(self, sourceRecord: int, ) -> int:
        ...

    def NewUninitializedRecord(self, ) -> int:
        ...

    def NewRecordFromArray(self, value: System.Array[System.Object], ) -> int:
        ...

    def NewEmptyRow(self, ) -> System.Data.DataRow:
        ...

    def NewUninitializedRow(self, ) -> System.Data.DataRow:
        ...

    def GetObjectData(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext, ) -> None:
        ...

    def SerializeDataTable(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext, isSingleTable: bool, remotingFormat: int, ) -> None:
        ...

    def DeserializeDataTable(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext, isSingleTable: bool, remotingFormat: int, ) -> None:
        ...

    def SerializeTableSchema(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext, isSingleTable: bool, ) -> None:
        ...

    def DeserializeTableSchema(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext, isSingleTable: bool, ) -> None:
        ...

    def SerializeConstraints(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext, serIndex: int, allConstraints: bool, ) -> None:
        ...

    def DeserializeConstraints(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext, serIndex: int, allConstraints: bool, ) -> None:
        ...

    def SerializeExpressionColumns(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext, serIndex: int, ) -> None:
        ...

    def DeserializeExpressionColumns(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext, serIndex: int, ) -> None:
        ...

    def SerializeTableData(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext, serIndex: int, ) -> None:
        ...

    def DeserializeTableData(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext, serIndex: int, ) -> None:
        ...

    def ConvertToRowState(self, bitStates: System.Collections.BitArray, bitIndex: int, ) -> int:
        ...

    def GetRowAndColumnErrors(self, rowIndex: int, rowErrors: System.Collections.Hashtable, colErrors: System.Collections.Hashtable, ) -> None:
        ...

    def ConvertToRowError(self, rowIndex: int, rowErrors: System.Collections.Hashtable, colErrors: System.Collections.Hashtable, ) -> None:
        ...

    def RestoreIndexEvents(self, forceReset: bool, ) -> None:
        ...

    def SuspendIndexEvents(self, ) -> None:
        ...

    def SetCaseSensitiveValue(self, isCaseSensitive: bool, userSet: bool, resetIndexes: bool, ) -> bool:
        ...

    def ShouldSerializeCaseSensitive(self, ) -> bool:
        ...

    def ResetConstraints(self, ) -> None:
        ...

    def SetDataSet(self, dataSet: System.Data.DataSet, ) -> None:
        ...

    def EnableConstraints(self, ) -> None:
        ...

    def SetLocaleValue(self, culture: System.Globalization.CultureInfo, userSet: bool, resetIndexes: bool, ) -> bool:
        ...

    def ShouldSerializeLocale(self, ) -> bool:
        ...

    def CacheNestedParent(self, ) -> None:
        ...

    def FindNestedParentRelations(self, ) -> System.Array[System.Data.DataRelation]:
        ...

    def GetInheritedNamespace(self, visitedTables: System.Collections.Generic.List[System.Data.DataTable], ) -> str:
        ...

    def IsNamespaceInherited(self, ) -> bool:
        ...

    def CheckCascadingNamespaceConflict(self, realNamespace: str, ) -> None:
        ...

    def CheckNamespaceValidityForNestedRelations(self, realNamespace: str, ) -> None:
        ...

    def CheckNamespaceValidityForNestedParentRelations(self, ns: str, parentTable: System.Data.DataTable, ) -> None:
        ...

    def DoRaiseNamespaceChange(self, ) -> None:
        ...

    def BeginInit(self, ) -> None:
        ...

    def EndInit(self, ) -> None:
        ...

class DataRowChangeEventArgs(System.EventArgs):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def Row(self) -> System.Data.DataRow:
        ...

    @property
    def Action(self) -> int:
        ...

    # methods
    def __init__(self, row: System.Data.DataRow, action: int, ):
        ...

class DataRow(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        self._oldRecord: int
        self._newRecord: int
        self._tempRecord: int
        self._rowID: int
        self._action: int
        self._inChangingEvent: bool
        self._inDeletingEvent: bool
        self._inCascade: bool
        self._objectID: int
        ...

    # static fields

    # properties
    @property
    def Element(self) -> System.Xml.XmlBoundElement:
        ...
    @Element.setter
    def Element(self, val: System.Xml.XmlBoundElement):
        ...

    @property
    def LastChangedColumn(self) -> System.Data.DataColumn:
        ...
    @LastChangedColumn.setter
    def LastChangedColumn(self, val: System.Data.DataColumn):
        ...

    @property
    def HasPropertyChanged(self) -> bool:
        ...

    @property
    def RBTreeNodeId(self) -> int:
        ...
    @RBTreeNodeId.setter
    def RBTreeNodeId(self, val: int):
        ...

    @property
    def RowError(self) -> str:
        ...
    @RowError.setter
    def RowError(self, val: str):
        ...

    @property
    def rowID(self) -> int:
        ...
    @rowID.setter
    def rowID(self, val: int):
        ...

    @property
    def RowState(self) -> int:
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
    def ItemArray(self) -> System.Array[System.Object]:
        ...
    @ItemArray.setter
    def ItemArray(self, val: System.Array[System.Object]):
        ...

    @property
    def HasErrors(self) -> bool:
        ...

    # methods
    def __init__(self, builder: System.Data.DataRowBuilder, ):
        ...

    def SetNestedParentRow(self, parentRow: System.Data.DataRow, setNonNested: bool, ) -> None:
        ...

    @typing.overload
    def SetParentRow(self, parentRow: System.Data.DataRow, ) -> None:
        ...

    @typing.overload
    def SetParentRow(self, parentRow: System.Data.DataRow, relation: System.Data.DataRelation, ) -> None:
        ...

    @typing.overload
    def SetParentRowToDBNull(self, ) -> None:
        ...

    @typing.overload
    def SetParentRowToDBNull(self, relation: System.Data.DataRelation, ) -> None:
        ...

    def SetAdded(self, ) -> None:
        ...

    def SetModified(self, ) -> None:
        ...

    def CopyValuesIntoStore(self, storeList: System.Collections.ArrayList, nullbitList: System.Collections.ArrayList, storeIndex: int, ) -> int:
        ...

    def RowErrorChanged(self, ) -> None:
        ...

    def CheckForLoops(self, rel: System.Data.DataRelation, ) -> None:
        ...

    def GetNestedParentCount(self, ) -> int:
        ...

    def AcceptChanges(self, ) -> None:
        ...

    def BeginEdit(self, ) -> None:
        ...

    def BeginEditInternal(self, ) -> bool:
        ...

    def CancelEdit(self, ) -> None:
        ...

    def CheckColumn(self, column: System.Data.DataColumn, ) -> None:
        ...

    def CheckInTable(self, ) -> None:
        ...

    def Delete(self, ) -> None:
        ...

    def EndEdit(self, ) -> None:
        ...

    @typing.overload
    def SetColumnError(self, columnIndex: int, error: str, ) -> None:
        ...

    @typing.overload
    def SetColumnError(self, columnName: str, error: str, ) -> None:
        ...

    @typing.overload
    def SetColumnError(self, column: System.Data.DataColumn, error: str, ) -> None:
        ...

    @typing.overload
    def GetColumnError(self, columnIndex: int, ) -> str:
        ...

    @typing.overload
    def GetColumnError(self, columnName: str, ) -> str:
        ...

    @typing.overload
    def GetColumnError(self, column: System.Data.DataColumn, ) -> str:
        ...

    def ClearErrors(self, ) -> None:
        ...

    def ClearError(self, column: System.Data.DataColumn, ) -> None:
        ...

    def GetColumnsInError(self, ) -> System.Array[System.Data.DataColumn]:
        ...

    @typing.overload
    def GetChildRows(self, relationName: str, ) -> System.Array[System.Data.DataRow]:
        ...

    @typing.overload
    def GetChildRows(self, relationName: str, version: int, ) -> System.Array[System.Data.DataRow]:
        ...

    @typing.overload
    def GetChildRows(self, relation: System.Data.DataRelation, ) -> System.Array[System.Data.DataRow]:
        ...

    @typing.overload
    def GetChildRows(self, relation: System.Data.DataRelation, version: int, ) -> System.Array[System.Data.DataRow]:
        ...

    def GetDataColumn(self, columnName: str, ) -> System.Data.DataColumn:
        ...

    @typing.overload
    def GetParentRow(self, relationName: str, ) -> System.Data.DataRow:
        ...

    @typing.overload
    def GetParentRow(self, relationName: str, version: int, ) -> System.Data.DataRow:
        ...

    @typing.overload
    def GetParentRow(self, relation: System.Data.DataRelation, ) -> System.Data.DataRow:
        ...

    @typing.overload
    def GetParentRow(self, relation: System.Data.DataRelation, version: int, ) -> System.Data.DataRow:
        ...

    def GetNestedParentRow(self, version: int, ) -> System.Data.DataRow:
        ...

    @typing.overload
    def GetParentRows(self, relationName: str, ) -> System.Array[System.Data.DataRow]:
        ...

    @typing.overload
    def GetParentRows(self, relationName: str, version: int, ) -> System.Array[System.Data.DataRow]:
        ...

    @typing.overload
    def GetParentRows(self, relation: System.Data.DataRelation, ) -> System.Array[System.Data.DataRow]:
        ...

    @typing.overload
    def GetParentRows(self, relation: System.Data.DataRelation, version: int, ) -> System.Array[System.Data.DataRow]:
        ...

    @typing.overload
    def GetColumnValues(self, columns: System.Array[System.Data.DataColumn], ) -> System.Array[System.Object]:
        ...

    @typing.overload
    def GetColumnValues(self, columns: System.Array[System.Data.DataColumn], version: int, ) -> System.Array[System.Object]:
        ...

    @typing.overload
    def GetKeyValues(self, key: System.Data.DataKey, ) -> System.Array[System.Object]:
        ...

    @typing.overload
    def GetKeyValues(self, key: System.Data.DataKey, version: int, ) -> System.Array[System.Object]:
        ...

    def GetCurrentRecordNo(self, ) -> int:
        ...

    def GetDefaultRecord(self, ) -> int:
        ...

    def GetOriginalRecordNo(self, ) -> int:
        ...

    def GetProposedRecordNo(self, ) -> int:
        ...

    def GetRecordFromVersion(self, version: int, ) -> int:
        ...

    def GetDefaultRowVersion(self, viewState: int, ) -> int:
        ...

    def GetRecordState(self, record: int, ) -> int:
        ...

    @typing.overload
    def HasKeyChanged(self, key: System.Data.DataKey, ) -> bool:
        ...

    @typing.overload
    def HasKeyChanged(self, key: System.Data.DataKey, version1: int, version2: int, ) -> bool:
        ...

    def HasVersion(self, version: int, ) -> bool:
        ...

    def HasChanges(self, ) -> bool:
        ...

    @typing.overload
    def HaveValuesChanged(self, columns: System.Array[System.Data.DataColumn], ) -> bool:
        ...

    @typing.overload
    def HaveValuesChanged(self, columns: System.Array[System.Data.DataColumn], version1: int, version2: int, ) -> bool:
        ...

    @typing.overload
    def IsNull(self, columnIndex: int, ) -> bool:
        ...

    @typing.overload
    def IsNull(self, columnName: str, ) -> bool:
        ...

    @typing.overload
    def IsNull(self, column: System.Data.DataColumn, ) -> bool:
        ...

    @typing.overload
    def IsNull(self, column: System.Data.DataColumn, version: int, ) -> bool:
        ...

    def RejectChanges(self, ) -> None:
        ...

    def ResetLastChangedColumn(self, ) -> None:
        ...

    def SetKeyValues(self, key: System.Data.DataKey, keyValues: System.Array[System.Object], ) -> None:
        ...

    def SetNull(self, column: System.Data.DataColumn, ) -> None:
        ...

class DataRowVersion(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    Original: int = ...
    Current: int = ...
    Proposed: int = ...
    Default: int = ...

class DataTableClearEventArgs(System.EventArgs):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def Table(self) -> System.Data.DataTable:
        ...

    @property
    def TableName(self) -> str:
        ...

    @property
    def TableNamespace(self) -> str:
        ...

    # methods
    def __init__(self, dataTable: System.Data.DataTable, ):
        ...

class DataRowBuilder(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        self._table: System.Data.DataTable
        self._record: int
        ...

    # static fields

    # properties
    # methods
    def __init__(self, table: System.Data.DataTable, record: int, ):
        ...

class DataRelation(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        self._extendedProperties: System.Data.PropertyCollection
        self._relationName: str
        self._parentColumnNames: System.Array[str]
        self._childColumnNames: System.Array[str]
        self._parentTableName: str
        self._childTableName: str
        self._parentTableNamespace: str
        self._childTableNamespace: str
        self._nested: bool
        self._createConstraints: bool
        ...

    # static fields

    # properties
    @property
    def ChildColumns(self) -> System.Array[System.Data.DataColumn]:
        ...

    @property
    def ChildColumnsReference(self) -> System.Array[System.Data.DataColumn]:
        ...

    @property
    def ChildKey(self) -> System.Data.DataKey:
        ...

    @property
    def ChildTable(self) -> System.Data.DataTable:
        ...

    @property
    def DataSet(self) -> System.Data.DataSet:
        ...

    @property
    def ParentColumnNames(self) -> System.Array[str]:
        ...

    @property
    def ChildColumnNames(self) -> System.Array[str]:
        ...

    @property
    def ParentColumns(self) -> System.Array[System.Data.DataColumn]:
        ...

    @property
    def ParentColumnsReference(self) -> System.Array[System.Data.DataColumn]:
        ...

    @property
    def ParentKey(self) -> System.Data.DataKey:
        ...

    @property
    def ParentTable(self) -> System.Data.DataTable:
        ...

    @property
    def RelationName(self) -> str:
        ...
    @RelationName.setter
    def RelationName(self, val: str):
        ...

    @property
    def Nested(self) -> bool:
        ...
    @Nested.setter
    def Nested(self, val: bool):
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

    @property
    def CheckMultipleNested(self) -> bool:
        ...
    @CheckMultipleNested.setter
    def CheckMultipleNested(self, val: bool):
        ...

    @property
    def ObjectID(self) -> int:
        ...

    # methods
    @typing.overload
    def __init__(self, relationName: str, parentColumn: System.Data.DataColumn, childColumn: System.Data.DataColumn, ):
        ...

    @typing.overload
    def __init__(self, relationName: str, parentColumn: System.Data.DataColumn, childColumn: System.Data.DataColumn, createConstraints: bool, ):
        ...

    @typing.overload
    def __init__(self, relationName: str, parentColumns: System.Array[System.Data.DataColumn], childColumns: System.Array[System.Data.DataColumn], ):
        ...

    @typing.overload
    def __init__(self, relationName: str, parentColumns: System.Array[System.Data.DataColumn], childColumns: System.Array[System.Data.DataColumn], createConstraints: bool, ):
        ...

    @typing.overload
    def __init__(self, relationName: str, parentTableName: str, childTableName: str, parentColumnNames: System.Array[str], childColumnNames: System.Array[str], nested: bool, ):
        ...

    @typing.overload
    def __init__(self, relationName: str, parentTableName: str, parentTableNamespace: str, childTableName: str, childTableNamespace: str, parentColumnNames: System.Array[str], childColumnNames: System.Array[str], nested: bool, ):
        ...

    @staticmethod
    def IsKeyNull(values: System.Array[System.Object], ) -> bool:
        ...

    @staticmethod
    def GetChildRows(parentKey: System.Data.DataKey, childKey: System.Data.DataKey, parentRow: System.Data.DataRow, version: int, ) -> System.Array[System.Data.DataRow]:
        ...

    @staticmethod
    def GetParentRows(parentKey: System.Data.DataKey, childKey: System.Data.DataKey, childRow: System.Data.DataRow, version: int, ) -> System.Array[System.Data.DataRow]:
        ...

    @staticmethod
    def GetParentRow(parentKey: System.Data.DataKey, childKey: System.Data.DataKey, childRow: System.Data.DataRow, version: int, ) -> System.Data.DataRow:
        ...

    def SetDataSet(self, dataSet: System.Data.DataSet, ) -> None:
        ...

    def CheckNamespaceValidityForNestedRelations(self, ns: str, ) -> None:
        ...

    def CheckNestedRelations(self, ) -> None:
        ...

    def SetParentKeyConstraint(self, value: System.Data.UniqueConstraint, ) -> None:
        ...

    def SetChildKeyConstraint(self, value: System.Data.ForeignKeyConstraint, ) -> None:
        ...

    def CheckState(self, ) -> None:
        ...

    def CheckStateForProperty(self, ) -> None:
        ...

    def Create(self, relationName: str, parentColumns: System.Array[System.Data.DataColumn], childColumns: System.Array[System.Data.DataColumn], createConstraints: bool, ) -> None:
        ...

    def Clone(self, destination: System.Data.DataSet, ) -> System.Data.DataRelation:
        ...

    def OnPropertyChanging(self, pcevent: System.ComponentModel.PropertyChangedEventArgs, ) -> None:
        ...

    def RaisePropertyChanging(self, name: str, ) -> None:
        ...

    def ToString(self, ) -> str:
        ...

    def ValidateMultipleNestedRelations(self, ) -> None:
        ...

    def IsAutoGenerated(self, col: System.Data.DataColumn, ) -> bool:
        ...

class DataRowState(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    Detached: int = ...
    Unchanged: int = ...
    Added: int = ...
    Deleted: int = ...
    Modified: int = ...

class XmlReadMode(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    Auto: int = ...
    ReadSchema: int = ...
    IgnoreSchema: int = ...
    InferSchema: int = ...
    DiffGram: int = ...
    Fragment: int = ...
    InferTypedSchema: int = ...

class ForeignKeyConstraint(System.Data.Constraint):
    @typing.overload
    def __init__(self, **kwargs):
        self._deleteRule: int
        self._updateRule: int
        self._acceptRejectRule: int
        self._constraintName: str
        self._parentColumnNames: System.Array[str]
        self._childColumnNames: System.Array[str]
        self._parentTableName: str
        self._parentTableNamespace: str
        self._name: str
        self._extendedProperties: System.Data.PropertyCollection
        ...

    # static fields

    # properties
    @property
    def ChildKey(self) -> System.Data.DataKey:
        ...

    @property
    def Columns(self) -> System.Array[System.Data.DataColumn]:
        ...

    @property
    def Table(self) -> System.Data.DataTable:
        ...

    @property
    def ParentColumnNames(self) -> System.Array[str]:
        ...

    @property
    def ChildColumnNames(self) -> System.Array[str]:
        ...

    @property
    def AcceptRejectRule(self) -> int:
        ...
    @AcceptRejectRule.setter
    def AcceptRejectRule(self, val: int):
        ...

    @property
    def DeleteRule(self) -> int:
        ...
    @DeleteRule.setter
    def DeleteRule(self, val: int):
        ...

    @property
    def RelatedColumns(self) -> System.Array[System.Data.DataColumn]:
        ...

    @property
    def RelatedColumnsReference(self) -> System.Array[System.Data.DataColumn]:
        ...

    @property
    def ParentKey(self) -> System.Data.DataKey:
        ...

    @property
    def RelatedTable(self) -> System.Data.DataTable:
        ...

    @property
    def UpdateRule(self) -> int:
        ...
    @UpdateRule.setter
    def UpdateRule(self, val: int):
        ...

    @property
    def ConstraintName(self) -> str:
        ...
    @ConstraintName.setter
    def ConstraintName(self, val: str):
        ...

    @property
    def SchemaName(self) -> str:
        ...
    @SchemaName.setter
    def SchemaName(self, val: str):
        ...

    @property
    def InCollection(self) -> bool:
        ...
    @InCollection.setter
    def InCollection(self, val: bool):
        ...

    @property
    def ExtendedProperties(self) -> System.Data.PropertyCollection:
        ...

    @property
    def _DataSet(self) -> System.Data.DataSet:
        ...

    # methods
    @typing.overload
    def __init__(self, parentColumn: System.Data.DataColumn, childColumn: System.Data.DataColumn, ):
        ...

    @typing.overload
    def __init__(self, constraintName: str, parentColumn: System.Data.DataColumn, childColumn: System.Data.DataColumn, ):
        ...

    @typing.overload
    def __init__(self, parentColumns: System.Array[System.Data.DataColumn], childColumns: System.Array[System.Data.DataColumn], ):
        ...

    @typing.overload
    def __init__(self, constraintName: str, parentColumns: System.Array[System.Data.DataColumn], childColumns: System.Array[System.Data.DataColumn], ):
        ...

    @typing.overload
    def __init__(self, constraintName: str, parentTableName: str, parentColumnNames: System.Array[str], childColumnNames: System.Array[str], acceptRejectRule: int, deleteRule: int, updateRule: int, ):
        ...

    @typing.overload
    def __init__(self, constraintName: str, parentTableName: str, parentTableNamespace: str, parentColumnNames: System.Array[str], childColumnNames: System.Array[str], acceptRejectRule: int, deleteRule: int, updateRule: int, ):
        ...

    def CheckCanAddToCollection(self, constraints: System.Data.ConstraintCollection, ) -> None:
        ...

    def CanBeRemovedFromCollection(self, constraints: System.Data.ConstraintCollection, fThrowException: bool, ) -> bool:
        ...

    def IsKeyNull(self, values: System.Array[System.Object], ) -> bool:
        ...

    def IsConstraintViolated(self, ) -> bool:
        ...

    def CanEnableConstraint(self, ) -> bool:
        ...

    def CascadeCommit(self, row: System.Data.DataRow, ) -> None:
        ...

    def CascadeDelete(self, row: System.Data.DataRow, ) -> None:
        ...

    def CascadeRollback(self, row: System.Data.DataRow, ) -> None:
        ...

    def CascadeUpdate(self, row: System.Data.DataRow, ) -> None:
        ...

    def CheckCanClearParentTable(self, table: System.Data.DataTable, ) -> None:
        ...

    def CheckCanRemoveParentRow(self, row: System.Data.DataRow, ) -> None:
        ...

    def CheckCascade(self, row: System.Data.DataRow, action: int, ) -> None:
        ...

    def CheckConstraint(self, childRow: System.Data.DataRow, action: int, ) -> None:
        ...

    def NonVirtualCheckState(self, ) -> None:
        ...

    def CheckState(self, ) -> None:
        ...

    def ContainsColumn(self, column: System.Data.DataColumn, ) -> bool:
        ...

    @typing.overload
    def Clone(self, destination: System.Data.DataSet, ) -> System.Data.Constraint:
        ...

    @typing.overload
    def Clone(self, destination: System.Data.DataSet, ignorNSforTableLookup: bool, ) -> System.Data.Constraint:
        ...

    @typing.overload
    def Clone(self, destination: System.Data.DataTable, ) -> System.Data.ForeignKeyConstraint:
        ...

    def Create(self, relationName: str, parentColumns: System.Array[System.Data.DataColumn], childColumns: System.Array[System.Data.DataColumn], ) -> None:
        ...

    def Equals(self, key: System.Object, ) -> bool:
        ...

    def GetHashCode(self, ) -> int:
        ...

    def FindParentRelation(self, ) -> System.Data.DataRelation:
        ...

class Rule(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    None_: int = ...
    Cascade: int = ...
    SetNull: int = ...
    SetDefault: int = ...

class DataViewRowState(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    None_: int = ...
    Unchanged: int = ...
    Added: int = ...
    Deleted: int = ...
    ModifiedCurrent: int = ...
    CurrentRows: int = ...
    ModifiedOriginal: int = ...
    OriginalRows: int = ...

class DataRowCollection(System.Collections.ICollection, System.Collections.IEnumerable, System.Data.InternalDataCollectionBase):
    @typing.overload
    def __init__(self, **kwargs):
        self._nullInList: int
        ...

    # static fields

    # properties
    @property
    def Count(self) -> int:
        ...

    @property
    def Item(self) -> System.Data.DataRow:
        ...

    @property
    def IsReadOnly(self) -> bool:
        ...

    @property
    def IsSynchronized(self) -> bool:
        ...

    @property
    def SyncRoot(self) -> System.Object:
        ...

    @property
    def List(self) -> System.Collections.ArrayList:
        ...

    # methods
    def __init__(self, table: System.Data.DataTable, ):
        ...

    @typing.overload
    def Add(self, row: System.Data.DataRow, ) -> None:
        ...

    @typing.overload
    def Add(self, values: System.Array[System.Object], ) -> System.Data.DataRow:
        ...

    def InsertAt(self, row: System.Data.DataRow, pos: int, ) -> None:
        ...

    def DiffInsertAt(self, row: System.Data.DataRow, pos: int, ) -> None:
        ...

    def IndexOf(self, row: System.Data.DataRow, ) -> int:
        ...

    def AddWithColumnEvents(self, values: System.Array[System.Object], ) -> System.Data.DataRow:
        ...

    def ArrayAdd(self, row: System.Data.DataRow, ) -> None:
        ...

    def ArrayInsert(self, row: System.Data.DataRow, pos: int, ) -> None:
        ...

    def ArrayClear(self, ) -> None:
        ...

    def ArrayRemove(self, row: System.Data.DataRow, ) -> None:
        ...

    @typing.overload
    def Find(self, key: System.Object, ) -> System.Data.DataRow:
        ...

    @typing.overload
    def Find(self, keys: System.Array[System.Object], ) -> System.Data.DataRow:
        ...

    def Clear(self, ) -> None:
        ...

    @typing.overload
    def Contains(self, key: System.Object, ) -> bool:
        ...

    @typing.overload
    def Contains(self, keys: System.Array[System.Object], ) -> bool:
        ...

    @typing.overload
    def CopyTo(self, ar: System.Array, index: int, ) -> None:
        ...

    @typing.overload
    def CopyTo(self, array: System.Array[System.Data.DataRow], index: int, ) -> None:
        ...

    def GetEnumerator(self, ) -> System.Collections.IEnumerator:
        ...

    def Remove(self, row: System.Data.DataRow, ) -> None:
        ...

    def RemoveAt(self, index: int, ) -> None:
        ...

class SerializationFormat(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    Xml: int = ...
    Binary: int = ...

class Constraint(System.Object, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        self._name: str
        self._extendedProperties: System.Data.PropertyCollection
        ...

    # static fields

    # properties
    @property
    def ConstraintName(self) -> str:
        ...
    @ConstraintName.setter
    def ConstraintName(self, val: str):
        ...

    @property
    def SchemaName(self) -> str:
        ...
    @SchemaName.setter
    def SchemaName(self, val: str):
        ...

    @property
    def InCollection(self) -> bool:
        ...
    @InCollection.setter
    def InCollection(self, val: bool):
        ...

    @property
    @abc.abstractmethod
    def Table(self) -> System.Data.DataTable:
        ...

    @property
    def ExtendedProperties(self) -> System.Data.PropertyCollection:
        ...

    @property
    def _DataSet(self) -> System.Data.DataSet:
        ...

    # methods
    def __init__(self, ):
        ...

    @abc.abstractmethod
    def CheckCanAddToCollection(self, constraint: System.Data.ConstraintCollection, ) -> None:
        ...

    @abc.abstractmethod
    def CanBeRemovedFromCollection(self, constraint: System.Data.ConstraintCollection, fThrowException: bool, ) -> bool:
        ...

    @abc.abstractmethod
    def IsConstraintViolated(self, ) -> bool:
        ...

    @abc.abstractmethod
    def CanEnableConstraint(self, ) -> bool:
        ...

    @abc.abstractmethod
    @typing.overload
    def CheckConstraint(self, row: System.Data.DataRow, action: int, ) -> None:
        ...

    @typing.overload
    def CheckConstraint(self, ) -> None:
        ...

    @abc.abstractmethod
    def CheckState(self, ) -> None:
        ...

    @abc.abstractmethod
    def ContainsColumn(self, column: System.Data.DataColumn, ) -> bool:
        ...

    @abc.abstractmethod
    @typing.overload
    def Clone(self, destination: System.Data.DataSet, ) -> System.Data.Constraint:
        ...

    @abc.abstractmethod
    @typing.overload
    def Clone(self, destination: System.Data.DataSet, ignoreNSforTableLookup: bool, ) -> System.Data.Constraint:
        ...

    def CheckStateForProperty(self, ) -> None:
        ...

    def SetDataSet(self, dataSet: System.Data.DataSet, ) -> None:
        ...

    def ToString(self, ) -> str:
        ...

class FillErrorEventHandler(System.ICloneable, System.Runtime.Serialization.ISerializable, System.MulticastDelegate):
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

    def Invoke(self, sender: System.Object, e: System.Data.FillErrorEventArgs, ) -> None:
        ...

    def BeginInvoke(self, sender: System.Object, e: System.Data.FillErrorEventArgs, callback: System.AsyncCallback, object: System.Object, ) -> System.IAsyncResult:
        ...

    def EndInvoke(self, result: System.IAsyncResult, ) -> None:
        ...

class FillErrorEventArgs(System.EventArgs):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def Continue(self) -> bool:
        ...
    @Continue.setter
    def Continue(self, val: bool):
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
    def Values(self) -> System.Array[System.Object]:
        ...

    # methods
    def __init__(self, dataTable: System.Data.DataTable, values: System.Array[System.Object], ):
        ...

class DataView(System.ComponentModel.IComponent, System.IDisposable, System.IServiceProvider, System.ComponentModel.IBindingListView, System.ComponentModel.IBindingList, System.Collections.IList, System.Collections.ICollection, System.Collections.IEnumerable, System.ComponentModel.ITypedList, System.ComponentModel.ISupportInitializeNotification, System.ComponentModel.ISupportInitialize, System.ComponentModel.MarshalByValueComponent):
    @typing.overload
    def __init__(self, **kwargs):
        self._addNewRow: System.Data.DataRow
        ...

    # static fields
    s_resetEventArgs: System.ComponentModel.ListChangedEventArgs = ...

    # properties
    @property
    def AllowDelete(self) -> bool:
        ...
    @AllowDelete.setter
    def AllowDelete(self, val: bool):
        ...

    @property
    def ApplyDefaultSort(self) -> bool:
        ...
    @ApplyDefaultSort.setter
    def ApplyDefaultSort(self, val: bool):
        ...

    @property
    def AllowEdit(self) -> bool:
        ...
    @AllowEdit.setter
    def AllowEdit(self, val: bool):
        ...

    @property
    def AllowNew(self) -> bool:
        ...
    @AllowNew.setter
    def AllowNew(self, val: bool):
        ...

    @property
    def Count(self) -> int:
        ...

    @property
    def CountFromIndex(self) -> int:
        ...

    @property
    def DataViewManager(self) -> System.Data.DataViewManager:
        ...

    @property
    def IsInitialized(self) -> bool:
        ...

    @property
    def IsOpen(self) -> bool:
        ...

    @property
    def IsSynchronized(self) -> bool:
        ...

    @property
    def RowFilter(self) -> str:
        ...
    @RowFilter.setter
    def RowFilter(self, val: str):
        ...

    @property
    def RowPredicate(self) -> System.Predicate[System.Data.DataRow]:
        ...
    @RowPredicate.setter
    def RowPredicate(self, val: System.Predicate[System.Data.DataRow]):
        ...

    @property
    def RowStateFilter(self) -> int:
        ...
    @RowStateFilter.setter
    def RowStateFilter(self, val: int):
        ...

    @property
    def Sort(self) -> str:
        ...
    @Sort.setter
    def Sort(self, val: str):
        ...

    @property
    def SortComparison(self) -> System.Comparison[System.Data.DataRow]:
        ...
    @SortComparison.setter
    def SortComparison(self, val: System.Comparison[System.Data.DataRow]):
        ...

    @property
    def SyncRoot(self) -> System.Object:
        ...

    @property
    def Table(self) -> System.Data.DataTable:
        ...
    @Table.setter
    def Table(self, val: System.Data.DataTable):
        ...

    @property
    def Item(self) -> System.Object:
        ...
    @Item.setter
    def Item(self, val: System.Object):
        ...

    @property
    def Item(self) -> System.Data.DataRowView:
        ...

    @property
    def IsReadOnly(self) -> bool:
        ...

    @property
    def IsFixedSize(self) -> bool:
        ...

    @property
    def AllowNew(self) -> bool:
        ...

    @property
    def AllowEdit(self) -> bool:
        ...

    @property
    def AllowRemove(self) -> bool:
        ...

    @property
    def SupportsChangeNotification(self) -> bool:
        ...

    @property
    def SupportsSearching(self) -> bool:
        ...

    @property
    def SupportsSorting(self) -> bool:
        ...

    @property
    def IsSorted(self) -> bool:
        ...

    @property
    def SortProperty(self) -> System.ComponentModel.PropertyDescriptor:
        ...

    @property
    def SortDirection(self) -> int:
        ...

    @property
    def Filter(self) -> str:
        ...
    @Filter.setter
    def Filter(self, val: str):
        ...

    @property
    def SortDescriptions(self) -> System.ComponentModel.ListSortDescriptionCollection:
        ...

    @property
    def SupportsAdvancedSorting(self) -> bool:
        ...

    @property
    def SupportsFiltering(self) -> bool:
        ...

    @property
    def ObjectID(self) -> int:
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
    def __init__(self, table: System.Data.DataTable, locked: bool, ):
        ...

    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def __init__(self, table: System.Data.DataTable, ):
        ...

    @typing.overload
    def __init__(self, table: System.Data.DataTable, RowFilter: str, Sort: str, RowState: int, ):
        ...

    @typing.overload
    def __init__(self, table: System.Data.DataTable, predicate: System.Predicate[System.Data.DataRow], comparison: System.Comparison[System.Data.DataRow], RowState: int, ):
        ...

    def AddIndex(self, property: System.ComponentModel.PropertyDescriptor, ) -> None:
        ...

    def ApplySort(self, property: System.ComponentModel.PropertyDescriptor, direction: int, ) -> None:
        ...

    def Find(self, property: System.ComponentModel.PropertyDescriptor, key: System.Object, ) -> int:
        ...

    def RemoveIndex(self, property: System.ComponentModel.PropertyDescriptor, ) -> None:
        ...

    def RemoveSort(self, ) -> None:
        ...

    def ApplySort(self, sorts: System.ComponentModel.ListSortDescriptionCollection, ) -> None:
        ...

    def CreateSortString(self, property: System.ComponentModel.PropertyDescriptor, direction: int, ) -> str:
        ...

    def RemoveFilter(self, ) -> None:
        ...

    def GetSortDescriptions(self, ) -> System.ComponentModel.ListSortDescriptionCollection:
        ...

    def GetListName(self, listAccessors: System.Array[System.ComponentModel.PropertyDescriptor], ) -> str:
        ...

    def GetItemProperties(self, listAccessors: System.Array[System.ComponentModel.PropertyDescriptor], ) -> System.ComponentModel.PropertyDescriptorCollection:
        ...

    def GetFilter(self, ) -> System.Data.IFilter:
        ...

    def GetRecord(self, recordIndex: int, ) -> int:
        ...

    def GetRow(self, index: int, ) -> System.Data.DataRow:
        ...

    @typing.overload
    def GetRowView(self, record: int, ) -> System.Data.DataRowView:
        ...

    @typing.overload
    def GetRowView(self, dr: System.Data.DataRow, ) -> System.Data.DataRowView:
        ...

    def IndexListChanged(self, sender: System.Object, e: System.ComponentModel.ListChangedEventArgs, ) -> None:
        ...

    def IndexListChangedInternal(self, e: System.ComponentModel.ListChangedEventArgs, ) -> None:
        ...

    def MaintainDataView(self, changedType: int, row: System.Data.DataRow, trackAddRemove: bool, ) -> None:
        ...

    def OnListChanged(self, e: System.ComponentModel.ListChangedEventArgs, ) -> None:
        ...

    def OnInitialized(self, ) -> None:
        ...

    def Open(self, ) -> None:
        ...

    def Reset(self, ) -> None:
        ...

    def ResetRowViewCache(self, ) -> None:
        ...

    def SetDataViewManager(self, dataViewManager: System.Data.DataViewManager, ) -> None:
        ...

    def CreateDataExpressionFromDataViewSettings(self, dataViewSetting: System.Data.DataViewSetting, ) -> System.Data.DataExpression:
        ...

    def SetIndex(self, newSort: str, newRowStates: int, newRowFilter: System.Data.IFilter, ) -> None:
        ...

    def SetIndex2(self, newSort: str, newRowStates: int, newRowFilter: System.Data.IFilter, fireEvent: bool, ) -> None:
        ...

    @typing.overload
    def UpdateIndex(self, ) -> None:
        ...

    @typing.overload
    def UpdateIndex(self, force: bool, ) -> None:
        ...

    @typing.overload
    def UpdateIndex(self, force: bool, fireEvent: bool, ) -> None:
        ...

    def ChildRelationCollectionChanged(self, sender: System.Object, e: System.ComponentModel.CollectionChangeEventArgs, ) -> None:
        ...

    def ParentRelationCollectionChanged(self, sender: System.Object, e: System.ComponentModel.CollectionChangeEventArgs, ) -> None:
        ...

    def ColumnCollectionChanged(self, sender: System.Object, e: System.ComponentModel.CollectionChangeEventArgs, ) -> None:
        ...

    def ColumnCollectionChangedInternal(self, sender: System.Object, e: System.ComponentModel.CollectionChangeEventArgs, ) -> None:
        ...

    @typing.overload
    def ToTable(self, ) -> System.Data.DataTable:
        ...

    @typing.overload
    def ToTable(self, tableName: str, ) -> System.Data.DataTable:
        ...

    @typing.overload
    def ToTable(self, distinct: bool, columnNames: System.Array[str], ) -> System.Data.DataTable:
        ...

    @typing.overload
    def ToTable(self, tableName: str, distinct: bool, columnNames: System.Array[str], ) -> System.Data.DataTable:
        ...

    def RowExist(self, arraylist: System.Collections.Generic.List[System.Array[System.Object]], objectArray: System.Array[System.Object], ) -> bool:
        ...

    def Equals(self, view: System.Data.DataView, ) -> bool:
        ...

    def AddNew(self, ) -> System.Data.DataRowView:
        ...

    def BeginInit(self, ) -> None:
        ...

    def EndInit(self, ) -> None:
        ...

    def CheckOpen(self, ) -> None:
        ...

    def CheckSort(self, sort: str, ) -> None:
        ...

    def Close(self, ) -> None:
        ...

    @typing.overload
    def CopyTo(self, array: System.Array, index: int, ) -> None:
        ...

    @typing.overload
    def CopyTo(self, array: System.Array[System.Data.DataRowView], index: int, ) -> None:
        ...

    @typing.overload
    def Delete(self, index: int, ) -> None:
        ...

    @typing.overload
    def Delete(self, row: System.Data.DataRow, ) -> None:
        ...

    def Dispose(self, disposing: bool, ) -> None:
        ...

    @typing.overload
    def Find(self, key: System.Object, ) -> int:
        ...

    @typing.overload
    def Find(self, key: System.Array[System.Object], ) -> int:
        ...

    @typing.overload
    def FindByKey(self, key: System.Object, ) -> int:
        ...

    @typing.overload
    def FindByKey(self, key: System.Array[System.Object], ) -> int:
        ...

    @typing.overload
    def FindRows(self, key: System.Object, ) -> System.Array[System.Data.DataRowView]:
        ...

    @typing.overload
    def FindRows(self, key: System.Array[System.Object], ) -> System.Array[System.Data.DataRowView]:
        ...

    def FindRowsByKey(self, key: System.Array[System.Object], ) -> System.Array[System.Data.DataRowView]:
        ...

    def FindRecords(self, comparison: System.Data.Index.ComparisonBySelector[TKey, TRow], key: TKey, ) -> System.Data.Range:
        ...

    def GetDataRowViewFromRange(self, range: System.Data.Range, ) -> System.Array[System.Data.DataRowView]:
        ...

    def FinishAddNew(self, success: bool, ) -> None:
        ...

    def GetEnumerator(self, ) -> System.Collections.IEnumerator:
        ...

    def Add(self, value: System.Object, ) -> int:
        ...

    def Clear(self, ) -> None:
        ...

    def Contains(self, value: System.Object, ) -> bool:
        ...

    def IndexOf(self, value: System.Object, ) -> int:
        ...

    def IndexOf(self, rowview: System.Data.DataRowView, ) -> int:
        ...

    def IndexOfDataRowView(self, rowview: System.Data.DataRowView, ) -> int:
        ...

    def Insert(self, index: int, value: System.Object, ) -> None:
        ...

    def Remove(self, value: System.Object, ) -> None:
        ...

    def RemoveAt(self, index: int, ) -> None:
        ...

    def GetFindIndex(self, column: str, keepIndex: bool, ) -> System.Data.Index:
        ...

    def AddNew(self, ) -> System.Object:
        ...

    def GetSortProperty(self, ) -> System.ComponentModel.PropertyDescriptor:
        ...

class DataViewSetting(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def ApplyDefaultSort(self) -> bool:
        ...
    @ApplyDefaultSort.setter
    def ApplyDefaultSort(self, val: bool):
        ...

    @property
    def DataViewManager(self) -> System.Data.DataViewManager:
        ...

    @property
    def Table(self) -> System.Data.DataTable:
        ...

    @property
    def RowFilter(self) -> str:
        ...
    @RowFilter.setter
    def RowFilter(self, val: str):
        ...

    @property
    def RowStateFilter(self) -> int:
        ...
    @RowStateFilter.setter
    def RowStateFilter(self, val: int):
        ...

    @property
    def Sort(self) -> str:
        ...
    @Sort.setter
    def Sort(self, val: str):
        ...

    # methods
    def __init__(self, ):
        ...

    def SetDataViewManager(self, dataViewManager: System.Data.DataViewManager, ) -> None:
        ...

    def SetDataTable(self, table: System.Data.DataTable, ) -> None:
        ...

class DataColumnChangeEventArgs(System.EventArgs):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def Column(self) -> System.Data.DataColumn:
        ...

    @property
    def Row(self) -> System.Data.DataRow:
        ...

    @property
    def ProposedValue(self) -> System.Object:
        ...
    @ProposedValue.setter
    def ProposedValue(self, val: System.Object):
        ...

    # methods
    @typing.overload
    def __init__(self, row: System.Data.DataRow, ):
        ...

    @typing.overload
    def __init__(self, row: System.Data.DataRow, column: System.Data.DataColumn, value: System.Object, ):
        ...

    def InitializeColumnChangeEvent(self, column: System.Data.DataColumn, value: System.Object, ) -> None:
        ...

class DataRowAction(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    Nothing: int = ...
    Delete: int = ...
    Change: int = ...
    Rollback: int = ...
    Commit: int = ...
    Add: int = ...
    ChangeOriginal: int = ...
    ChangeCurrentAndOriginal: int = ...

class DataRelationCollection(System.Collections.ICollection, System.Collections.IEnumerable, System.Data.InternalDataCollectionBase, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def ObjectID(self) -> int:
        ...

    @property
    @abc.abstractmethod
    def Item(self) -> System.Data.DataRelation:
        ...

    @property
    @abc.abstractmethod
    def Item(self) -> System.Data.DataRelation:
        ...

    @property
    def Count(self) -> int:
        ...

    @property
    def IsReadOnly(self) -> bool:
        ...

    @property
    def IsSynchronized(self) -> bool:
        ...

    @property
    def SyncRoot(self) -> System.Object:
        ...

    @property
    def List(self) -> System.Collections.ArrayList:
        ...

    # methods
    def __init__(self, ):
        ...

    @typing.overload
    def Add(self, relation: System.Data.DataRelation, ) -> None:
        ...

    @typing.overload
    def Add(self, name: str, parentColumns: System.Array[System.Data.DataColumn], childColumns: System.Array[System.Data.DataColumn], ) -> System.Data.DataRelation:
        ...

    @typing.overload
    def Add(self, name: str, parentColumns: System.Array[System.Data.DataColumn], childColumns: System.Array[System.Data.DataColumn], createConstraints: bool, ) -> System.Data.DataRelation:
        ...

    @typing.overload
    def Add(self, parentColumns: System.Array[System.Data.DataColumn], childColumns: System.Array[System.Data.DataColumn], ) -> System.Data.DataRelation:
        ...

    @typing.overload
    def Add(self, name: str, parentColumn: System.Data.DataColumn, childColumn: System.Data.DataColumn, ) -> System.Data.DataRelation:
        ...

    @typing.overload
    def Add(self, name: str, parentColumn: System.Data.DataColumn, childColumn: System.Data.DataColumn, createConstraints: bool, ) -> System.Data.DataRelation:
        ...

    @typing.overload
    def Add(self, parentColumn: System.Data.DataColumn, childColumn: System.Data.DataColumn, ) -> System.Data.DataRelation:
        ...

    def AddRange(self, relations: System.Array[System.Data.DataRelation], ) -> None:
        ...

    def AddCore(self, relation: System.Data.DataRelation, ) -> None:
        ...

    def AssignName(self, ) -> str:
        ...

    def Clear(self, ) -> None:
        ...

    def Contains(self, name: str, ) -> bool:
        ...

    def CopyTo(self, array: System.Array[System.Data.DataRelation], index: int, ) -> None:
        ...

    @typing.overload
    def IndexOf(self, relation: System.Data.DataRelation, ) -> int:
        ...

    @typing.overload
    def IndexOf(self, relationName: str, ) -> int:
        ...

    def InternalIndexOf(self, name: str, ) -> int:
        ...

    @abc.abstractmethod
    def GetDataSet(self, ) -> System.Data.DataSet:
        ...

    def MakeName(self, index: int, ) -> str:
        ...

    def OnCollectionChanged(self, ccevent: System.ComponentModel.CollectionChangeEventArgs, ) -> None:
        ...

    def OnCollectionChanging(self, ccevent: System.ComponentModel.CollectionChangeEventArgs, ) -> None:
        ...

    def RegisterName(self, name: str, ) -> None:
        ...

    def CanRemove(self, relation: System.Data.DataRelation, ) -> bool:
        ...

    @typing.overload
    def Remove(self, relation: System.Data.DataRelation, ) -> None:
        ...

    @typing.overload
    def Remove(self, name: str, ) -> None:
        ...

    def RemoveAt(self, index: int, ) -> None:
        ...

    def RemoveCore(self, relation: System.Data.DataRelation, ) -> None:
        ...

    def UnregisterName(self, name: str, ) -> None:
        ...

class DataSet(System.ComponentModel.IComponent, System.IDisposable, System.IServiceProvider, System.ComponentModel.IListSource, System.Xml.Serialization.IXmlSerializable, System.ComponentModel.ISupportInitializeNotification, System.ComponentModel.ISupportInitialize, System.Runtime.Serialization.ISerializable, System.ComponentModel.MarshalByValueComponent):
    @typing.overload
    def __init__(self, **kwargs):
        self._extendedProperties: System.Data.PropertyCollection
        self._namespaceURI: str
        self._fInReadXml: bool
        self._fInLoadDiffgram: bool
        self._fTopLevelTable: bool
        self._fInitInProgress: bool
        self._fEnableCascading: bool
        self._fIsSchemaLoading: bool
        self._mainTableName: str
        self._useDataSetSchemaOnly: bool
        self._udtIsWrapped: bool
        ...

    # static fields

    # properties
    @property
    def RemotingFormat(self) -> int:
        ...
    @RemotingFormat.setter
    def RemotingFormat(self, val: int):
        ...

    @property
    def SchemaSerializationMode(self) -> int:
        ...
    @SchemaSerializationMode.setter
    def SchemaSerializationMode(self, val: int):
        ...

    @property
    def CaseSensitive(self) -> bool:
        ...
    @CaseSensitive.setter
    def CaseSensitive(self, val: bool):
        ...

    @property
    def ContainsListCollection(self) -> bool:
        ...

    @property
    def DefaultViewManager(self) -> System.Data.DataViewManager:
        ...

    @property
    def EnforceConstraints(self) -> bool:
        ...
    @EnforceConstraints.setter
    def EnforceConstraints(self, val: bool):
        ...

    @property
    def DataSetName(self) -> str:
        ...
    @DataSetName.setter
    def DataSetName(self, val: str):
        ...

    @property
    def Namespace(self) -> str:
        ...
    @Namespace.setter
    def Namespace(self, val: str):
        ...

    @property
    def Prefix(self) -> str:
        ...
    @Prefix.setter
    def Prefix(self, val: str):
        ...

    @property
    def ExtendedProperties(self) -> System.Data.PropertyCollection:
        ...

    @property
    def HasErrors(self) -> bool:
        ...

    @property
    def IsInitialized(self) -> bool:
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
    def FBoundToDocument(self) -> bool:
        ...
    @FBoundToDocument.setter
    def FBoundToDocument(self, val: bool):
        ...

    @property
    def MainTableName(self) -> str:
        ...
    @MainTableName.setter
    def MainTableName(self, val: str):
        ...

    @property
    def ObjectID(self) -> int:
        ...

    @property
    def Events(self) -> System.ComponentModel.EventHandlerList:
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
    def __init__(self, dataSetName: str, ):
        ...

    @typing.overload
    def __init__(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext, ):
        ...

    @typing.overload
    def __init__(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext, ConstructSchema: bool, ):
        ...

    def ReadEndElement(self, reader: System.Xml.XmlReader, ) -> None:
        ...

    def ReadXSDSchema(self, reader: System.Xml.XmlReader, denyResolving: bool, ) -> None:
        ...

    def ReadXDRSchema(self, reader: System.Xml.XmlReader, ) -> None:
        ...

    @typing.overload
    def ReadXmlSchema(self, stream: System.IO.Stream, ) -> None:
        ...

    @typing.overload
    def ReadXmlSchema(self, reader: System.IO.TextReader, ) -> None:
        ...

    @typing.overload
    def ReadXmlSchema(self, fileName: str, ) -> None:
        ...

    @typing.overload
    def ReadXmlSchema(self, reader: System.Xml.XmlReader, ) -> None:
        ...

    @typing.overload
    def ReadXmlSchema(self, reader: System.Xml.XmlReader, denyResolving: bool, ) -> None:
        ...

    @typing.overload
    def WriteXmlSchema(self, stream: System.IO.Stream, ) -> None:
        ...

    @typing.overload
    def WriteXmlSchema(self, stream: System.IO.Stream, multipleTargetConverter: System.Converter[System.Type, str], ) -> None:
        ...

    @typing.overload
    def WriteXmlSchema(self, fileName: str, ) -> None:
        ...

    @typing.overload
    def WriteXmlSchema(self, fileName: str, multipleTargetConverter: System.Converter[System.Type, str], ) -> None:
        ...

    @typing.overload
    def WriteXmlSchema(self, writer: System.IO.TextWriter, ) -> None:
        ...

    @typing.overload
    def WriteXmlSchema(self, writer: System.IO.TextWriter, multipleTargetConverter: System.Converter[System.Type, str], ) -> None:
        ...

    @typing.overload
    def WriteXmlSchema(self, writer: System.Xml.XmlWriter, ) -> None:
        ...

    @typing.overload
    def WriteXmlSchema(self, writer: System.Xml.XmlWriter, multipleTargetConverter: System.Converter[System.Type, str], ) -> None:
        ...

    @typing.overload
    def WriteXmlSchema(self, fileName: str, schemaFormat: int, multipleTargetConverter: System.Converter[System.Type, str], ) -> None:
        ...

    @typing.overload
    def WriteXmlSchema(self, stream: System.IO.Stream, schemaFormat: int, multipleTargetConverter: System.Converter[System.Type, str], ) -> None:
        ...

    @typing.overload
    def WriteXmlSchema(self, writer: System.IO.TextWriter, schemaFormat: int, multipleTargetConverter: System.Converter[System.Type, str], ) -> None:
        ...

    @typing.overload
    def WriteXmlSchema(self, writer: System.Xml.XmlWriter, schemaFormat: int, multipleTargetConverter: System.Converter[System.Type, str], ) -> None:
        ...

    @staticmethod
    @typing.overload
    def WriteXmlSchema(ds: System.Data.DataSet, writer: System.Xml.XmlWriter, ) -> None:
        ...

    @typing.overload
    def ReadXml(self, reader: System.Xml.XmlReader, ) -> int:
        ...

    @typing.overload
    def ReadXml(self, reader: System.Xml.XmlReader, denyResolving: bool, ) -> int:
        ...

    @typing.overload
    def ReadXml(self, stream: System.IO.Stream, ) -> int:
        ...

    @typing.overload
    def ReadXml(self, reader: System.IO.TextReader, ) -> int:
        ...

    @typing.overload
    def ReadXml(self, fileName: str, ) -> int:
        ...

    @typing.overload
    def ReadXml(self, reader: System.Xml.XmlReader, mode: int, ) -> int:
        ...

    @typing.overload
    def ReadXml(self, reader: System.Xml.XmlReader, mode: int, denyResolving: bool, ) -> int:
        ...

    @typing.overload
    def ReadXml(self, stream: System.IO.Stream, mode: int, ) -> int:
        ...

    @typing.overload
    def ReadXml(self, reader: System.IO.TextReader, mode: int, ) -> int:
        ...

    @typing.overload
    def ReadXml(self, fileName: str, mode: int, ) -> int:
        ...

    def InferSchema(self, xdoc: System.Xml.XmlDocument, excludedNamespaces: System.Array[str], mode: int, ) -> None:
        ...

    def IsEmpty(self, ) -> bool:
        ...

    def ReadXmlDiffgram(self, reader: System.Xml.XmlReader, ) -> None:
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
    def WriteXml(self, fileName: str, ) -> None:
        ...

    @typing.overload
    def WriteXml(self, stream: System.IO.Stream, mode: int, ) -> None:
        ...

    @typing.overload
    def WriteXml(self, writer: System.IO.TextWriter, mode: int, ) -> None:
        ...

    @typing.overload
    def WriteXml(self, writer: System.Xml.XmlWriter, mode: int, ) -> None:
        ...

    @typing.overload
    def WriteXml(self, fileName: str, mode: int, ) -> None:
        ...

    @typing.overload
    def Merge(self, dataSet: System.Data.DataSet, ) -> None:
        ...

    @typing.overload
    def Merge(self, dataSet: System.Data.DataSet, preserveChanges: bool, ) -> None:
        ...

    @typing.overload
    def Merge(self, dataSet: System.Data.DataSet, preserveChanges: bool, missingSchemaAction: int, ) -> None:
        ...

    @typing.overload
    def Merge(self, table: System.Data.DataTable, ) -> None:
        ...

    @typing.overload
    def Merge(self, table: System.Data.DataTable, preserveChanges: bool, missingSchemaAction: int, ) -> None:
        ...

    @typing.overload
    def Merge(self, rows: System.Array[System.Data.DataRow], ) -> None:
        ...

    @typing.overload
    def Merge(self, rows: System.Array[System.Data.DataRow], preserveChanges: bool, missingSchemaAction: int, ) -> None:
        ...

    def OnPropertyChanging(self, pcevent: System.ComponentModel.PropertyChangedEventArgs, ) -> None:
        ...

    def OnMergeFailed(self, mfevent: System.Data.MergeFailedEventArgs, ) -> None:
        ...

    def RaiseMergeFailed(self, table: System.Data.DataTable, conflict: str, missingSchemaAction: int, ) -> None:
        ...

    def OnDataRowCreated(self, row: System.Data.DataRow, ) -> None:
        ...

    def OnClearFunctionCalled(self, table: System.Data.DataTable, ) -> None:
        ...

    def OnInitialized(self, ) -> None:
        ...

    def OnRemoveTable(self, table: System.Data.DataTable, ) -> None:
        ...

    def OnRemovedTable(self, table: System.Data.DataTable, ) -> None:
        ...

    def OnRemoveRelation(self, relation: System.Data.DataRelation, ) -> None:
        ...

    def OnRemoveRelationHack(self, relation: System.Data.DataRelation, ) -> None:
        ...

    def RaisePropertyChanging(self, name: str, ) -> None:
        ...

    @typing.overload
    def TopLevelTables(self, ) -> System.Array[System.Data.DataTable]:
        ...

    @typing.overload
    def TopLevelTables(self, forSchema: bool, ) -> System.Array[System.Data.DataTable]:
        ...

    def RejectChanges(self, ) -> None:
        ...

    def Reset(self, ) -> None:
        ...

    def ValidateCaseConstraint(self, ) -> bool:
        ...

    def ValidateLocaleConstraint(self, ) -> bool:
        ...

    def FindTable(self, baseTable: System.Data.DataTable, props: System.Array[System.ComponentModel.PropertyDescriptor], propStart: int, ) -> System.Data.DataTable:
        ...

    def ReadXmlSerializable(self, reader: System.Xml.XmlReader, ) -> None:
        ...

    def GetSchemaSerializable(self, ) -> System.Xml.Schema.XmlSchema:
        ...

    @staticmethod
    def GetDataSetSchema(schemaSet: System.Xml.Schema.XmlSchemaSet, ) -> System.Xml.Schema.XmlSchemaComplexType:
        ...

    def GetSchema(self, ) -> System.Xml.Schema.XmlSchema:
        ...

    def ReadXml(self, reader: System.Xml.XmlReader, ) -> None:
        ...

    def ReadXmlSerializableInternal(self, reader: System.Xml.XmlReader, ) -> None:
        ...

    def WriteXml(self, writer: System.Xml.XmlWriter, ) -> None:
        ...

    def WriteXmlInternal(self, writer: System.Xml.XmlWriter, ) -> None:
        ...

    @typing.overload
    def Load(self, reader: System.Data.IDataReader, loadOption: int, errorHandler: System.Data.FillErrorEventHandler, tables: System.Array[System.Data.DataTable], ) -> None:
        ...

    @typing.overload
    def Load(self, reader: System.Data.IDataReader, loadOption: int, tables: System.Array[System.Data.DataTable], ) -> None:
        ...

    @typing.overload
    def Load(self, reader: System.Data.IDataReader, loadOption: int, tables: System.Array[str], ) -> None:
        ...

    @typing.overload
    def CreateDataReader(self, ) -> System.Data.DataTableReader:
        ...

    @typing.overload
    def CreateDataReader(self, dataTables: System.Array[System.Data.DataTable], ) -> System.Data.DataTableReader:
        ...

    def IsBinarySerialized(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext, ) -> bool:
        ...

    @typing.overload
    def DetermineSchemaSerializationMode(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext, ) -> int:
        ...

    @typing.overload
    def DetermineSchemaSerializationMode(self, reader: System.Xml.XmlReader, ) -> int:
        ...

    def GetSerializationData(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext, ) -> None:
        ...

    def GetObjectData(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext, ) -> None:
        ...

    def InitializeDerivedDataSet(self, ) -> None:
        ...

    def SerializeDataSet(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext, remotingFormat: int, ) -> None:
        ...

    def DeserializeDataSet(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext, remotingFormat: int, schemaSerializationMode: int, ) -> None:
        ...

    def DeserializeDataSetSchema(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext, remotingFormat: int, schemaSerializationMode: int, ) -> None:
        ...

    def DeserializeDataSetData(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext, remotingFormat: int, ) -> None:
        ...

    def SerializeDataSetProperties(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext, ) -> None:
        ...

    def DeserializeDataSetProperties(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext, ) -> None:
        ...

    def SerializeRelations(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext, ) -> None:
        ...

    def DeserializeRelations(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext, ) -> None:
        ...

    def FailedEnableConstraints(self, ) -> None:
        ...

    def RestoreEnforceConstraints(self, value: bool, ) -> None:
        ...

    def EnableConstraints(self, ) -> None:
        ...

    def SetLocaleValue(self, value: System.Globalization.CultureInfo, userSet: bool, ) -> None:
        ...

    def ShouldSerializeLocale(self, ) -> bool:
        ...

    def ShouldSerializeRelations(self, ) -> bool:
        ...

    def ShouldSerializeTables(self, ) -> bool:
        ...

    def AcceptChanges(self, ) -> None:
        ...

    def BeginInit(self, ) -> None:
        ...

    def EndInit(self, ) -> None:
        ...

    def Clear(self, ) -> None:
        ...

    def CreateInstanceOfThisType(self, ) -> System.Data.DataSet:
        ...

    def Clone(self, ) -> System.Data.DataSet:
        ...

    def Copy(self, ) -> System.Data.DataSet:
        ...

    def EstimatedXmlStringSize(self, ) -> int:
        ...

    @typing.overload
    def GetChanges(self, ) -> System.Data.DataSet:
        ...

    @typing.overload
    def GetChanges(self, rowStates: int, ) -> System.Data.DataSet:
        ...

    def MarkModifiedRows(self, bitMatrix: System.Array[System.Data.DataSet.TableChanges], rowStates: int, ) -> None:
        ...

    def MarkRelatedRowsAsModified(self, bitMatrix: System.Array[System.Data.DataSet.TableChanges], row: System.Data.DataRow, ) -> None:
        ...

    def GetList(self, ) -> System.Collections.IList:
        ...

    def GetRemotingDiffGram(self, table: System.Data.DataTable, ) -> str:
        ...

    def GetXml(self, ) -> str:
        ...

    def GetXmlSchema(self, ) -> str:
        ...

    def GetXmlSchemaForRemoting(self, table: System.Data.DataTable, ) -> str:
        ...

    @typing.overload
    def HasChanges(self, ) -> bool:
        ...

    @typing.overload
    def HasChanges(self, rowStates: int, ) -> bool:
        ...

    @typing.overload
    def InferXmlSchema(self, reader: System.Xml.XmlReader, nsArray: System.Array[str], ) -> None:
        ...

    @typing.overload
    def InferXmlSchema(self, stream: System.IO.Stream, nsArray: System.Array[str], ) -> None:
        ...

    @typing.overload
    def InferXmlSchema(self, reader: System.IO.TextReader, nsArray: System.Array[str], ) -> None:
        ...

    @typing.overload
    def InferXmlSchema(self, fileName: str, nsArray: System.Array[str], ) -> None:
        ...

    @typing.overload
    def MoveToElement(self, reader: System.Xml.XmlReader, depth: int, ) -> bool:
        ...

    @staticmethod
    @typing.overload
    def MoveToElement(reader: System.Xml.XmlReader, ) -> None:
        ...

class SchemaSerializationMode(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    IncludeSchema: int = ...
    ExcludeSchema: int = ...

class AcceptRejectRule(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    None_: int = ...
    Cascade: int = ...

class PropertyCollection(System.Collections.IDictionary, System.Collections.ICollection, System.Collections.IEnumerable, System.Runtime.Serialization.ISerializable, System.Runtime.Serialization.IDeserializationCallback, System.ICloneable, System.Collections.Hashtable):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def hcp(self) -> System.Collections.IHashCodeProvider:
        ...
    @hcp.setter
    def hcp(self, val: System.Collections.IHashCodeProvider):
        ...

    @property
    def comparer(self) -> System.Collections.IComparer:
        ...
    @comparer.setter
    def comparer(self, val: System.Collections.IComparer):
        ...

    @property
    def EqualityComparer(self) -> System.Collections.IEqualityComparer:
        ...

    @property
    def Item(self) -> System.Object:
        ...
    @Item.setter
    def Item(self, val: System.Object):
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
    def Values(self) -> System.Collections.ICollection:
        ...

    @property
    def SyncRoot(self) -> System.Object:
        ...

    @property
    def Count(self) -> int:
        ...

    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def __init__(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext, ):
        ...

    def Clone(self, ) -> System.Object:
        ...

class MergeFailedEventArgs(System.EventArgs):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def Table(self) -> System.Data.DataTable:
        ...

    @property
    def Conflict(self) -> str:
        ...

    # methods
    def __init__(self, table: System.Data.DataTable, conflict: str, ):
        ...

class DataTableReader(System.Data.IDataReader, System.IDisposable, System.Data.IDataRecord, System.Collections.IEnumerable, System.IAsyncDisposable, System.Data.Common.DbDataReader):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def ReaderIsInvalid(self) -> bool:
        ...
    @ReaderIsInvalid.setter
    def ReaderIsInvalid(self, val: bool):
        ...

    @property
    def IsSchemaChanged(self) -> bool:
        ...
    @IsSchemaChanged.setter
    def IsSchemaChanged(self, val: bool):
        ...

    @property
    def CurrentDataTable(self) -> System.Data.DataTable:
        ...

    @property
    def Depth(self) -> int:
        ...

    @property
    def IsClosed(self) -> bool:
        ...

    @property
    def RecordsAffected(self) -> int:
        ...

    @property
    def HasRows(self) -> bool:
        ...

    @property
    def Item(self) -> System.Object:
        ...

    @property
    def Item(self) -> System.Object:
        ...

    @property
    def FieldCount(self) -> int:
        ...

    @property
    def VisibleFieldCount(self) -> int:
        ...

    # methods
    @typing.overload
    def __init__(self, dataTable: System.Data.DataTable, ):
        ...

    @typing.overload
    def __init__(self, dataTables: System.Array[System.Data.DataTable], ):
        ...

    def Init(self, ) -> None:
        ...

    def Close(self, ) -> None:
        ...

    def GetSchemaTable(self, ) -> System.Data.DataTable:
        ...

    def NextResult(self, ) -> bool:
        ...

    def Read(self, ) -> bool:
        ...

    def GetProviderSpecificFieldType(self, ordinal: int, ) -> System.Type:
        ...

    def GetProviderSpecificValue(self, ordinal: int, ) -> System.Object:
        ...

    def GetProviderSpecificValues(self, values: System.Array[System.Object], ) -> int:
        ...

    def GetBoolean(self, ordinal: int, ) -> bool:
        ...

    def GetByte(self, ordinal: int, ) -> int:
        ...

    def GetBytes(self, ordinal: int, dataIndex: int, buffer: System.Array[int], bufferIndex: int, length: int, ) -> int:
        ...

    def GetChar(self, ordinal: int, ) -> str:
        ...

    def GetChars(self, ordinal: int, dataIndex: int, buffer: System.Array[str], bufferIndex: int, length: int, ) -> int:
        ...

    def GetDataTypeName(self, ordinal: int, ) -> str:
        ...

    def GetDateTime(self, ordinal: int, ) -> System.DateTime:
        ...

    def GetDecimal(self, ordinal: int, ) -> System.Decimal:
        ...

    def GetDouble(self, ordinal: int, ) -> float:
        ...

    def GetFieldType(self, ordinal: int, ) -> System.Type:
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

    def GetName(self, ordinal: int, ) -> str:
        ...

    def GetOrdinal(self, name: str, ) -> int:
        ...

    def GetString(self, ordinal: int, ) -> str:
        ...

    def GetValue(self, ordinal: int, ) -> System.Object:
        ...

    def GetValues(self, values: System.Array[System.Object], ) -> int:
        ...

    def IsDBNull(self, ordinal: int, ) -> bool:
        ...

    def GetEnumerator(self, ) -> System.Collections.IEnumerator:
        ...

    @staticmethod
    def GetSchemaTableFromDataTable(table: System.Data.DataTable, ) -> System.Data.DataTable:
        ...

    def ValidateOpen(self, caller: str, ) -> None:
        ...

    def ValidateReader(self, ) -> None:
        ...

    def ValidateState(self, caller: str, ) -> None:
        ...

    def ValidateRow(self, rowPosition: int, ) -> None:
        ...

    def SchemaChanged(self, ) -> None:
        ...

    def DataTableCleared(self, ) -> None:
        ...

    def DataChanged(self, args: System.Data.DataRowChangeEventArgs, ) -> None:
        ...

class ConstraintCollection(System.Collections.ICollection, System.Collections.IEnumerable, System.Data.InternalDataCollectionBase):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def List(self) -> System.Collections.ArrayList:
        ...

    @property
    def Item(self) -> System.Data.Constraint:
        ...

    @property
    def Table(self) -> System.Data.DataTable:
        ...

    @property
    def Item(self) -> System.Data.Constraint:
        ...

    @property
    def Count(self) -> int:
        ...

    @property
    def IsReadOnly(self) -> bool:
        ...

    @property
    def IsSynchronized(self) -> bool:
        ...

    @property
    def SyncRoot(self) -> System.Object:
        ...

    # methods
    def __init__(self, table: System.Data.DataTable, ):
        ...

    @typing.overload
    def Add(self, constraint: System.Data.Constraint, ) -> None:
        ...

    @typing.overload
    def Add(self, constraint: System.Data.Constraint, addUniqueWhenAddingForeign: bool, ) -> None:
        ...

    @typing.overload
    def Add(self, name: str, columns: System.Array[System.Data.DataColumn], primaryKey: bool, ) -> System.Data.Constraint:
        ...

    @typing.overload
    def Add(self, name: str, column: System.Data.DataColumn, primaryKey: bool, ) -> System.Data.Constraint:
        ...

    @typing.overload
    def Add(self, name: str, primaryKeyColumn: System.Data.DataColumn, foreignKeyColumn: System.Data.DataColumn, ) -> System.Data.Constraint:
        ...

    @typing.overload
    def Add(self, name: str, primaryKeyColumns: System.Array[System.Data.DataColumn], foreignKeyColumns: System.Array[System.Data.DataColumn], ) -> System.Data.Constraint:
        ...

    def AddRange(self, constraints: System.Array[System.Data.Constraint], ) -> None:
        ...

    def AddUniqueConstraint(self, constraint: System.Data.UniqueConstraint, ) -> None:
        ...

    def AddForeignKeyConstraint(self, constraint: System.Data.ForeignKeyConstraint, ) -> None:
        ...

    def AutoGenerated(self, constraint: System.Data.Constraint, ) -> bool:
        ...

    def ArrayAdd(self, constraint: System.Data.Constraint, ) -> None:
        ...

    def ArrayRemove(self, constraint: System.Data.Constraint, ) -> None:
        ...

    def AssignName(self, ) -> str:
        ...

    def BaseAdd(self, constraint: System.Data.Constraint, ) -> None:
        ...

    def BaseGroupSwitch(self, oldArray: System.Array[System.Data.Constraint], oldLength: int, newArray: System.Array[System.Data.Constraint], newLength: int, ) -> None:
        ...

    def BaseRemove(self, constraint: System.Data.Constraint, ) -> None:
        ...

    @typing.overload
    def CanRemove(self, constraint: System.Data.Constraint, ) -> bool:
        ...

    @typing.overload
    def CanRemove(self, constraint: System.Data.Constraint, fThrowException: bool, ) -> bool:
        ...

    def Clear(self, ) -> None:
        ...

    @typing.overload
    def Contains(self, name: str, ) -> bool:
        ...

    @typing.overload
    def Contains(self, name: str, caseSensitive: bool, ) -> bool:
        ...

    def CopyTo(self, array: System.Array[System.Data.Constraint], index: int, ) -> None:
        ...

    def FindConstraint(self, constraint: System.Data.Constraint, ) -> System.Data.Constraint:
        ...

    @typing.overload
    def FindKeyConstraint(self, columns: System.Array[System.Data.DataColumn], ) -> System.Data.UniqueConstraint:
        ...

    @typing.overload
    def FindKeyConstraint(self, column: System.Data.DataColumn, ) -> System.Data.UniqueConstraint:
        ...

    def FindForeignKeyConstraint(self, parentColumns: System.Array[System.Data.DataColumn], childColumns: System.Array[System.Data.DataColumn], ) -> System.Data.ForeignKeyConstraint:
        ...

    @staticmethod
    def CompareArrays(a1: System.Array[System.Data.DataColumn], a2: System.Array[System.Data.DataColumn], ) -> bool:
        ...

    @typing.overload
    def IndexOf(self, constraint: System.Data.Constraint, ) -> int:
        ...

    @typing.overload
    def IndexOf(self, constraintName: str, ) -> int:
        ...

    def InternalIndexOf(self, constraintName: str, ) -> int:
        ...

    def MakeName(self, index: int, ) -> str:
        ...

    def OnCollectionChanged(self, ccevent: System.ComponentModel.CollectionChangeEventArgs, ) -> None:
        ...

    def RegisterName(self, name: str, ) -> None:
        ...

    @typing.overload
    def Remove(self, constraint: System.Data.Constraint, ) -> None:
        ...

    @typing.overload
    def Remove(self, name: str, ) -> None:
        ...

    def RemoveAt(self, index: int, ) -> None:
        ...

    def UnregisterName(self, name: str, ) -> None:
        ...

    def FinishInitConstraints(self, ) -> None:
        ...

class MissingSchemaAction(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    Add: int = ...
    Ignore: int = ...
    Error: int = ...
    AddWithKey: int = ...

class LoadOption(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    OverwriteChanges: int = ...
    PreserveChanges: int = ...
    Upsert: int = ...

class DbType(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    AnsiString: int = ...
    Binary: int = ...
    Byte: int = ...
    Boolean: int = ...
    Currency: int = ...
    Date: int = ...
    DateTime: int = ...
    Decimal: int = ...
    Double: int = ...
    Guid: int = ...
    Int16: int = ...
    Int32: int = ...
    Int64: int = ...
    Object: int = ...
    SByte: int = ...
    Single: int = ...
    String: int = ...
    Time: int = ...
    UInt16: int = ...
    UInt32: int = ...
    UInt64: int = ...
    VarNumeric: int = ...
    AnsiStringFixedLength: int = ...
    StringFixedLength: int = ...
    Xml: int = ...
    DateTime2: int = ...
    DateTimeOffset: int = ...

class DataTableNewRowEventArgs(System.EventArgs):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def Row(self) -> System.Data.DataRow:
        ...

    # methods
    def __init__(self, dataRow: System.Data.DataRow, ):
        ...

class UniqueConstraint(System.Data.Constraint):
    @typing.overload
    def __init__(self, **kwargs):
        self._bPrimaryKey: bool
        self._constraintName: str
        self._columnNames: System.Array[str]
        self._name: str
        self._extendedProperties: System.Data.PropertyCollection
        ...

    # static fields

    # properties
    @property
    def ColumnNames(self) -> System.Array[str]:
        ...

    @property
    def ConstraintIndex(self) -> System.Data.Index:
        ...

    @property
    def Columns(self) -> System.Array[System.Data.DataColumn]:
        ...

    @property
    def ColumnsReference(self) -> System.Array[System.Data.DataColumn]:
        ...

    @property
    def IsPrimaryKey(self) -> bool:
        ...

    InCollection: bool = property(None, lambda val: ...)

    @property
    def Key(self) -> System.Data.DataKey:
        ...

    @property
    def Table(self) -> System.Data.DataTable:
        ...

    @property
    def ConstraintName(self) -> str:
        ...
    @ConstraintName.setter
    def ConstraintName(self, val: str):
        ...

    @property
    def SchemaName(self) -> str:
        ...
    @SchemaName.setter
    def SchemaName(self, val: str):
        ...

    @property
    def ExtendedProperties(self) -> System.Data.PropertyCollection:
        ...

    @property
    def _DataSet(self) -> System.Data.DataSet:
        ...

    # methods
    @typing.overload
    def __init__(self, name: str, column: System.Data.DataColumn, ):
        ...

    @typing.overload
    def __init__(self, column: System.Data.DataColumn, ):
        ...

    @typing.overload
    def __init__(self, name: str, columns: System.Array[System.Data.DataColumn], ):
        ...

    @typing.overload
    def __init__(self, columns: System.Array[System.Data.DataColumn], ):
        ...

    @typing.overload
    def __init__(self, name: str, columnNames: System.Array[str], isPrimaryKey: bool, ):
        ...

    @typing.overload
    def __init__(self, name: str, column: System.Data.DataColumn, isPrimaryKey: bool, ):
        ...

    @typing.overload
    def __init__(self, column: System.Data.DataColumn, isPrimaryKey: bool, ):
        ...

    @typing.overload
    def __init__(self, name: str, columns: System.Array[System.Data.DataColumn], isPrimaryKey: bool, ):
        ...

    @typing.overload
    def __init__(self, columns: System.Array[System.Data.DataColumn], isPrimaryKey: bool, ):
        ...

    def ConstraintIndexClear(self, ) -> None:
        ...

    def ConstraintIndexInitialize(self, ) -> None:
        ...

    def CheckState(self, ) -> None:
        ...

    def NonVirtualCheckState(self, ) -> None:
        ...

    def CheckCanAddToCollection(self, constraints: System.Data.ConstraintCollection, ) -> None:
        ...

    def CanBeRemovedFromCollection(self, constraints: System.Data.ConstraintCollection, fThrowException: bool, ) -> bool:
        ...

    def CanEnableConstraint(self, ) -> bool:
        ...

    def IsConstraintViolated(self, ) -> bool:
        ...

    def CheckConstraint(self, row: System.Data.DataRow, action: int, ) -> None:
        ...

    def ContainsColumn(self, column: System.Data.DataColumn, ) -> bool:
        ...

    @typing.overload
    def Clone(self, destination: System.Data.DataSet, ) -> System.Data.Constraint:
        ...

    @typing.overload
    def Clone(self, destination: System.Data.DataSet, ignorNSforTableLookup: bool, ) -> System.Data.Constraint:
        ...

    @typing.overload
    def Clone(self, table: System.Data.DataTable, ) -> System.Data.UniqueConstraint:
        ...

    def Create(self, constraintName: str, columns: System.Array[System.Data.DataColumn], ) -> None:
        ...

    def Equals(self, key2: System.Object, ) -> bool:
        ...

    def GetHashCode(self, ) -> int:
        ...

class DataColumn(System.ComponentModel.IComponent, System.IDisposable, System.IServiceProvider, System.ComponentModel.MarshalByValueComponent):
    @typing.overload
    def __init__(self, **kwargs):
        self._defaultValue: System.Object
        self._sortIndex: System.Data.Index
        self._table: System.Data.DataTable
        self._columnMapping: int
        self._hashCode: int
        self._errors: int
        self._dependentColumns: System.Collections.Generic.List[System.Data.DataColumn]
        self._extendedProperties: System.Data.PropertyCollection
        self._columnUri: str
        self._encodedColumnName: str
        self._simpleType: System.Data.SimpleType
        ...

    # static fields

    # properties
    @property
    def AllowDBNull(self) -> bool:
        ...
    @AllowDBNull.setter
    def AllowDBNull(self, val: bool):
        ...

    @property
    def AutoIncrement(self) -> bool:
        ...
    @AutoIncrement.setter
    def AutoIncrement(self, val: bool):
        ...

    @property
    def AutoIncrementCurrent(self) -> System.Object:
        ...
    @AutoIncrementCurrent.setter
    def AutoIncrementCurrent(self, val: System.Object):
        ...

    @property
    def AutoInc(self) -> System.Data.AutoIncrementValue:
        ...

    @property
    def AutoIncrementSeed(self) -> int:
        ...
    @AutoIncrementSeed.setter
    def AutoIncrementSeed(self, val: int):
        ...

    @property
    def AutoIncrementStep(self) -> int:
        ...
    @AutoIncrementStep.setter
    def AutoIncrementStep(self, val: int):
        ...

    @property
    def Caption(self) -> str:
        ...
    @Caption.setter
    def Caption(self, val: str):
        ...

    @property
    def ColumnName(self) -> str:
        ...
    @ColumnName.setter
    def ColumnName(self, val: str):
        ...

    @property
    def EncodedColumnName(self) -> str:
        ...

    @property
    def FormatProvider(self) -> System.IFormatProvider:
        ...

    @property
    def Locale(self) -> System.Globalization.CultureInfo:
        ...

    @property
    def ObjectID(self) -> int:
        ...

    @property
    def Prefix(self) -> str:
        ...
    @Prefix.setter
    def Prefix(self, val: str):
        ...

    @property
    def Computed(self) -> bool:
        ...

    @property
    def DataExpression(self) -> System.Data.DataExpression:
        ...

    @property
    def DataType(self) -> System.Type:
        ...
    @DataType.setter
    def DataType(self, val: System.Type):
        ...

    @property
    def DateTimeMode(self) -> int:
        ...
    @DateTimeMode.setter
    def DateTimeMode(self, val: int):
        ...

    @property
    def DefaultValue(self) -> System.Object:
        ...
    @DefaultValue.setter
    def DefaultValue(self, val: System.Object):
        ...

    @property
    def DefaultValueIsNull(self) -> bool:
        ...

    @property
    def Expression(self) -> str:
        ...
    @Expression.setter
    def Expression(self, val: str):
        ...

    @property
    def ExtendedProperties(self) -> System.Data.PropertyCollection:
        ...

    @property
    def HasData(self) -> bool:
        ...

    @property
    def ImplementsINullable(self) -> bool:
        ...

    @property
    def ImplementsIChangeTracking(self) -> bool:
        ...

    @property
    def ImplementsIRevertibleChangeTracking(self) -> bool:
        ...

    @property
    def IsValueType(self) -> bool:
        ...

    @property
    def IsSqlType(self) -> bool:
        ...

    @property
    def MaxLength(self) -> int:
        ...
    @MaxLength.setter
    def MaxLength(self, val: int):
        ...

    @property
    def Namespace(self) -> str:
        ...
    @Namespace.setter
    def Namespace(self, val: str):
        ...

    @property
    def Ordinal(self) -> int:
        ...

    @property
    def ReadOnly(self) -> bool:
        ...
    @ReadOnly.setter
    def ReadOnly(self, val: bool):
        ...

    @property
    def SortIndex(self) -> System.Data.Index:
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
    def Unique(self) -> bool:
        ...
    @Unique.setter
    def Unique(self, val: bool):
        ...

    @property
    def XmlDataType(self) -> str:
        ...
    @XmlDataType.setter
    def XmlDataType(self, val: str):
        ...

    @property
    def SimpleType(self) -> System.Data.SimpleType:
        ...
    @SimpleType.setter
    def SimpleType(self, val: System.Data.SimpleType):
        ...

    @property
    def ColumnMapping(self) -> int:
        ...
    @ColumnMapping.setter
    def ColumnMapping(self, val: int):
        ...

    @property
    def IsCustomType(self) -> bool:
        ...

    @property
    def ImplementsIXMLSerializable(self) -> bool:
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
    def __init__(self, columnName: str, ):
        ...

    @typing.overload
    def __init__(self, columnName: str, dataType: System.Type, ):
        ...

    @typing.overload
    def __init__(self, columnName: str, dataType: System.Type, expr: str, ):
        ...

    @typing.overload
    def __init__(self, columnName: str, dataType: System.Type, expr: str, type: int, ):
        ...

    def ConvertValue(self, value: System.Object, ) -> System.Object:
        ...

    def Copy(self, srcRecordNo: int, dstRecordNo: int, ) -> None:
        ...

    def Clone(self, ) -> System.Data.DataColumn:
        ...

    def GetAggregateValue(self, records: System.Array[int], kind: int, ) -> System.Object:
        ...

    def GetStringLength(self, record: int, ) -> int:
        ...

    def Init(self, record: int, ) -> None:
        ...

    @staticmethod
    def IsAutoIncrementType(dataType: System.Type, ) -> bool:
        ...

    def IsValueCustomTypeInstance(self, value: System.Object, ) -> bool:
        ...

    def IsNull(self, record: int, ) -> bool:
        ...

    def IsInRelation(self, ) -> bool:
        ...

    def IsMaxLengthViolated(self, ) -> bool:
        ...

    def IsNotAllowDBNullViolated(self, ) -> bool:
        ...

    def FinishInitInProgress(self, ) -> None:
        ...

    def OnPropertyChanging(self, pcevent: System.ComponentModel.PropertyChangedEventArgs, ) -> None:
        ...

    def RaisePropertyChanging(self, name: str, ) -> None:
        ...

    def InsureStorage(self, ) -> System.Data.Common.DataStorage:
        ...

    def SetCapacity(self, capacity: int, ) -> None:
        ...

    def OnSetDataSet(self, ) -> None:
        ...

    def ToString(self, ) -> str:
        ...

    @typing.overload
    def ConvertXmlToObject(self, s: str, ) -> System.Object:
        ...

    @typing.overload
    def ConvertXmlToObject(self, xmlReader: System.Xml.XmlReader, xmlAttrib: System.Xml.Serialization.XmlRootAttribute, ) -> System.Object:
        ...

    @typing.overload
    def ConvertObjectToXml(self, value: System.Object, ) -> str:
        ...

    @typing.overload
    def ConvertObjectToXml(self, value: System.Object, xmlWriter: System.Xml.XmlWriter, xmlAttrib: System.Xml.Serialization.XmlRootAttribute, ) -> None:
        ...

    def GetEmptyColumnStore(self, recordCount: int, ) -> System.Object:
        ...

    def CopyValueIntoStore(self, record: int, store: System.Object, nullbits: System.Collections.BitArray, storeIndex: int, ) -> None:
        ...

    def SetStorage(self, store: System.Object, nullbits: System.Collections.BitArray, ) -> None:
        ...

    def AddDependentColumn(self, expressionColumn: System.Data.DataColumn, ) -> None:
        ...

    def RemoveDependentColumn(self, expressionColumn: System.Data.DataColumn, ) -> None:
        ...

    def HandleDependentColumnList(self, oldExpression: System.Data.DataExpression, newExpression: System.Data.DataExpression, ) -> None:
        ...

    def CopyExpressionFrom(self, source: System.Data.DataColumn, ) -> None:
        ...

    def UpdateColumnType(self, type: System.Type, typeCode: int, ) -> None:
        ...

    def GetColumnValueAsString(self, row: System.Data.DataRow, version: int, ) -> str:
        ...

    def BindExpression(self, ) -> None:
        ...

    def SetMaxLengthSimpleType(self, ) -> None:
        ...

    def SetOrdinal(self, ordinal: int, ) -> None:
        ...

    def SetOrdinalInternal(self, ordinal: int, ) -> None:
        ...

    def SetTable(self, table: System.Data.DataTable, ) -> None:
        ...

    def GetDataRow(self, index: int, ) -> System.Data.DataRow:
        ...

    def InitializeRecord(self, record: int, ) -> None:
        ...

    def SetValue(self, record: int, value: System.Object, ) -> None:
        ...

    def FreeRecord(self, record: int, ) -> None:
        ...

    def InternalUnique(self, value: bool, ) -> None:
        ...

    def CheckColumnConstraint(self, row: System.Data.DataRow, action: int, ) -> None:
        ...

    @typing.overload
    def CheckMaxLength(self, ) -> bool:
        ...

    @typing.overload
    def CheckMaxLength(self, dr: System.Data.DataRow, ) -> None:
        ...

    def CheckNotAllowNull(self, ) -> None:
        ...

    def CheckNullable(self, row: System.Data.DataRow, ) -> None:
        ...

    def CheckUnique(self, ) -> None:
        ...

    def Compare(self, record1: int, record2: int, ) -> int:
        ...

    @typing.overload
    def CompareValueTo(self, record1: int, value: System.Object, checkType: bool, ) -> bool:
        ...

    @typing.overload
    def CompareValueTo(self, record1: int, value: System.Object, ) -> int:
        ...

class DataSetDateTime(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    Local: int = ...
    Unspecified: int = ...
    UnspecifiedLocal: int = ...
    Utc: int = ...

class MappingType(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    Element: int = ...
    Attribute: int = ...
    SimpleContent: int = ...
    Hidden: int = ...

class DataTableCollection(System.Collections.ICollection, System.Collections.IEnumerable, System.Data.InternalDataCollectionBase):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def List(self) -> System.Collections.ArrayList:
        ...

    @property
    def ObjectID(self) -> int:
        ...

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
    def Count(self) -> int:
        ...

    @property
    def IsReadOnly(self) -> bool:
        ...

    @property
    def IsSynchronized(self) -> bool:
        ...

    @property
    def SyncRoot(self) -> System.Object:
        ...

    # methods
    def __init__(self, dataSet: System.Data.DataSet, ):
        ...

    def GetTable(self, name: str, ns: str, ) -> System.Data.DataTable:
        ...

    def GetTableSmart(self, name: str, ns: str, ) -> System.Data.DataTable:
        ...

    @typing.overload
    def Add(self, table: System.Data.DataTable, ) -> None:
        ...

    @typing.overload
    def Add(self, name: str, ) -> System.Data.DataTable:
        ...

    @typing.overload
    def Add(self, name: str, tableNamespace: str, ) -> System.Data.DataTable:
        ...

    @typing.overload
    def Add(self, ) -> System.Data.DataTable:
        ...

    def AddRange(self, tables: System.Array[System.Data.DataTable], ) -> None:
        ...

    def ArrayAdd(self, table: System.Data.DataTable, ) -> None:
        ...

    def AssignName(self, ) -> str:
        ...

    def BaseAdd(self, table: System.Data.DataTable, ) -> None:
        ...

    def BaseGroupSwitch(self, oldArray: System.Array[System.Data.DataTable], oldLength: int, newArray: System.Array[System.Data.DataTable], newLength: int, ) -> None:
        ...

    def BaseRemove(self, table: System.Data.DataTable, ) -> None:
        ...

    @typing.overload
    def CanRemove(self, table: System.Data.DataTable, ) -> bool:
        ...

    @typing.overload
    def CanRemove(self, table: System.Data.DataTable, fThrowException: bool, ) -> bool:
        ...

    def Clear(self, ) -> None:
        ...

    @typing.overload
    def Contains(self, name: str, ) -> bool:
        ...

    @typing.overload
    def Contains(self, name: str, tableNamespace: str, ) -> bool:
        ...

    @typing.overload
    def Contains(self, name: str, tableNamespace: str, checkProperty: bool, caseSensitive: bool, ) -> bool:
        ...

    @typing.overload
    def Contains(self, name: str, caseSensitive: bool, ) -> bool:
        ...

    def CopyTo(self, array: System.Array[System.Data.DataTable], index: int, ) -> None:
        ...

    @typing.overload
    def IndexOf(self, table: System.Data.DataTable, ) -> int:
        ...

    @typing.overload
    def IndexOf(self, tableName: str, ) -> int:
        ...

    @typing.overload
    def IndexOf(self, tableName: str, tableNamespace: str, ) -> int:
        ...

    @typing.overload
    def IndexOf(self, tableName: str, tableNamespace: str, chekforNull: bool, ) -> int:
        ...

    def ReplaceFromInference(self, tableList: System.Collections.Generic.List[System.Data.DataTable], ) -> None:
        ...

    @typing.overload
    def InternalIndexOf(self, tableName: str, ) -> int:
        ...

    @typing.overload
    def InternalIndexOf(self, tableName: str, tableNamespace: str, ) -> int:
        ...

    def FinishInitCollection(self, ) -> None:
        ...

    def MakeName(self, index: int, ) -> str:
        ...

    def OnCollectionChanged(self, ccevent: System.ComponentModel.CollectionChangeEventArgs, ) -> None:
        ...

    def OnCollectionChanging(self, ccevent: System.ComponentModel.CollectionChangeEventArgs, ) -> None:
        ...

    def RegisterName(self, name: str, tbNamespace: str, ) -> None:
        ...

    @typing.overload
    def Remove(self, table: System.Data.DataTable, ) -> None:
        ...

    @typing.overload
    def Remove(self, name: str, ) -> None:
        ...

    @typing.overload
    def Remove(self, name: str, tableNamespace: str, ) -> None:
        ...

    def RemoveAt(self, index: int, ) -> None:
        ...

    def UnregisterName(self, name: str, ) -> None:
        ...

class InternalDataCollectionBase(System.Collections.ICollection, System.Collections.IEnumerable, System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields
    s_refreshEventArgs: System.ComponentModel.CollectionChangeEventArgs = ...

    # properties
    @property
    def Count(self) -> int:
        ...

    @property
    def IsReadOnly(self) -> bool:
        ...

    @property
    def IsSynchronized(self) -> bool:
        ...

    @property
    def SyncRoot(self) -> System.Object:
        ...

    @property
    def List(self) -> System.Collections.ArrayList:
        ...

    # methods
    def __init__(self, ):
        ...

    def CopyTo(self, ar: System.Array, index: int, ) -> None:
        ...

    def GetEnumerator(self, ) -> System.Collections.IEnumerator:
        ...

    def NamesEqual(self, s1: str, s2: str, fCaseSensitive: bool, locale: System.Globalization.CultureInfo, ) -> int:
        ...

class DataViewManager(System.ComponentModel.IComponent, System.IDisposable, System.IServiceProvider, System.ComponentModel.IBindingList, System.Collections.IList, System.Collections.ICollection, System.Collections.IEnumerable, System.ComponentModel.ITypedList, System.ComponentModel.MarshalByValueComponent):
    @typing.overload
    def __init__(self, **kwargs):
        self._nViews: int
        ...

    # static fields

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
    def DataViewSettingCollectionString(self) -> str:
        ...
    @DataViewSettingCollectionString.setter
    def DataViewSettingCollectionString(self, val: str):
        ...

    @property
    def Count(self) -> int:
        ...

    @property
    def SyncRoot(self) -> System.Object:
        ...

    @property
    def IsSynchronized(self) -> bool:
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
    def AllowNew(self) -> bool:
        ...

    @property
    def AllowEdit(self) -> bool:
        ...

    @property
    def AllowRemove(self) -> bool:
        ...

    @property
    def SupportsChangeNotification(self) -> bool:
        ...

    @property
    def SupportsSearching(self) -> bool:
        ...

    @property
    def SupportsSorting(self) -> bool:
        ...

    @property
    def IsSorted(self) -> bool:
        ...

    @property
    def SortProperty(self) -> System.ComponentModel.PropertyDescriptor:
        ...

    @property
    def SortDirection(self) -> int:
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
    def __init__(self, dataSet: System.Data.DataSet, ):
        ...

    @typing.overload
    def __init__(self, dataSet: System.Data.DataSet, locked: bool, ):
        ...

    def GetEnumerator(self, ) -> System.Collections.IEnumerator:
        ...

    def CopyTo(self, array: System.Array, index: int, ) -> None:
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

    def AddNew(self, ) -> System.Object:
        ...

    def AddIndex(self, property: System.ComponentModel.PropertyDescriptor, ) -> None:
        ...

    def ApplySort(self, property: System.ComponentModel.PropertyDescriptor, direction: int, ) -> None:
        ...

    def Find(self, property: System.ComponentModel.PropertyDescriptor, key: System.Object, ) -> int:
        ...

    def RemoveIndex(self, property: System.ComponentModel.PropertyDescriptor, ) -> None:
        ...

    def RemoveSort(self, ) -> None:
        ...

    def GetListName(self, listAccessors: System.Array[System.ComponentModel.PropertyDescriptor], ) -> str:
        ...

    def GetItemProperties(self, listAccessors: System.Array[System.ComponentModel.PropertyDescriptor], ) -> System.ComponentModel.PropertyDescriptorCollection:
        ...

    def CreateDataView(self, table: System.Data.DataTable, ) -> System.Data.DataView:
        ...

    def OnListChanged(self, e: System.ComponentModel.ListChangedEventArgs, ) -> None:
        ...

    def TableCollectionChanged(self, sender: System.Object, e: System.ComponentModel.CollectionChangeEventArgs, ) -> None:
        ...

    def RelationCollectionChanged(self, sender: System.Object, e: System.ComponentModel.CollectionChangeEventArgs, ) -> None:
        ...

class DataViewSettingCollection(System.Collections.ICollection, System.Collections.IEnumerable, System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

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
    def Count(self) -> int:
        ...

    @property
    def IsReadOnly(self) -> bool:
        ...

    @property
    def IsSynchronized(self) -> bool:
        ...

    @property
    def SyncRoot(self) -> System.Object:
        ...

    # methods
    def __init__(self, dataViewManager: System.Data.DataViewManager, ):
        ...

    @typing.overload
    def GetTable(self, tableName: str, ) -> System.Data.DataTable:
        ...

    @typing.overload
    def GetTable(self, index: int, ) -> System.Data.DataTable:
        ...

    @typing.overload
    def CopyTo(self, ar: System.Array, index: int, ) -> None:
        ...

    @typing.overload
    def CopyTo(self, ar: System.Array[System.Data.DataViewSetting], index: int, ) -> None:
        ...

    def GetEnumerator(self, ) -> System.Collections.IEnumerator:
        ...

    def Remove(self, table: System.Data.DataTable, ) -> None:
        ...

class CommandType(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    Text: int = ...
    StoredProcedure: int = ...
    TableDirect: int = ...

class CommandBehavior(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    Default: int = ...
    SingleResult: int = ...
    SchemaOnly: int = ...
    KeyInfo: int = ...
    SingleRow: int = ...
    SequentialAccess: int = ...
    CloseConnection: int = ...

class ParameterDirection(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    Input: int = ...
    Output: int = ...
    InputOutput: int = ...
    ReturnValue: int = ...

class IDbDataParameter(System.Data.IDataParameter, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    @abc.abstractmethod
    def Precision(self) -> int:
        ...
    @Precision.setter
    @abc.abstractmethod
    def Precision(self, val: int):
        ...

    @property
    @abc.abstractmethod
    def Scale(self) -> int:
        ...
    @Scale.setter
    @abc.abstractmethod
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

    # methods
class IDbTransaction(System.IDisposable, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    @abc.abstractmethod
    def Connection(self) -> System.Data.IDbConnection:
        ...

    @property
    @abc.abstractmethod
    def IsolationLevel(self) -> int:
        ...

    # methods
    @abc.abstractmethod
    def Commit(self, ) -> None:
        ...

    @abc.abstractmethod
    def Rollback(self, ) -> None:
        ...

class IsolationLevel(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    Chaos: int = ...
    ReadUncommitted: int = ...
    ReadCommitted: int = ...
    RepeatableRead: int = ...
    Serializable: int = ...
    Snapshot: int = ...
    Unspecified: int = ...

class StateChangeEventArgs(System.EventArgs):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def CurrentState(self) -> int:
        ...

    @property
    def OriginalState(self) -> int:
        ...

    # methods
    def __init__(self, originalState: int, currentState: int, ):
        ...

class IDbConnection(System.IDisposable, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
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
    @abc.abstractmethod
    def ConnectionTimeout(self) -> int:
        ...

    @property
    @abc.abstractmethod
    def Database(self) -> str:
        ...

    @property
    @abc.abstractmethod
    def State(self) -> int:
        ...

    # methods
    @abc.abstractmethod
    @typing.overload
    def BeginTransaction(self, ) -> System.Data.IDbTransaction:
        ...

    @abc.abstractmethod
    @typing.overload
    def BeginTransaction(self, il: int, ) -> System.Data.IDbTransaction:
        ...

    @abc.abstractmethod
    def Close(self, ) -> None:
        ...

    @abc.abstractmethod
    def ChangeDatabase(self, databaseName: str, ) -> None:
        ...

    @abc.abstractmethod
    def CreateCommand(self, ) -> System.Data.IDbCommand:
        ...

    @abc.abstractmethod
    def Open(self, ) -> None:
        ...

class SchemaType(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    Source: int = ...
    Mapped: int = ...

class MissingMappingAction(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    Passthrough: int = ...
    Ignore: int = ...
    Error: int = ...

class ITableMapping(abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    @abc.abstractmethod
    def ColumnMappings(self) -> System.Data.IColumnMappingCollection:
        ...

    @property
    @abc.abstractmethod
    def DataSetTable(self) -> str:
        ...
    @DataSetTable.setter
    @abc.abstractmethod
    def DataSetTable(self, val: str):
        ...

    @property
    @abc.abstractmethod
    def SourceTable(self) -> str:
        ...
    @SourceTable.setter
    @abc.abstractmethod
    def SourceTable(self, val: str):
        ...

    # methods
class IDataAdapter(abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    @abc.abstractmethod
    def MissingMappingAction(self) -> int:
        ...
    @MissingMappingAction.setter
    @abc.abstractmethod
    def MissingMappingAction(self, val: int):
        ...

    @property
    @abc.abstractmethod
    def MissingSchemaAction(self) -> int:
        ...
    @MissingSchemaAction.setter
    @abc.abstractmethod
    def MissingSchemaAction(self, val: int):
        ...

    @property
    @abc.abstractmethod
    def TableMappings(self) -> System.Data.ITableMappingCollection:
        ...

    # methods
    @abc.abstractmethod
    def FillSchema(self, dataSet: System.Data.DataSet, schemaType: int, ) -> System.Array[System.Data.DataTable]:
        ...

    @abc.abstractmethod
    def Fill(self, dataSet: System.Data.DataSet, ) -> int:
        ...

    @abc.abstractmethod
    def GetFillParameters(self, ) -> System.Array[System.Data.IDataParameter]:
        ...

    @abc.abstractmethod
    def Update(self, dataSet: System.Data.DataSet, ) -> int:
        ...

class ConnectionState(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    Closed: int = ...
    Open: int = ...
    Connecting: int = ...
    Executing: int = ...
    Fetching: int = ...
    Broken: int = ...

class IDataParameterCollection(System.Collections.IList, System.Collections.ICollection, System.Collections.IEnumerable, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    @abc.abstractmethod
    def Item(self) -> System.Object:
        ...
    @Item.setter
    @abc.abstractmethod
    def Item(self, val: System.Object):
        ...

    # methods
    @abc.abstractmethod
    def Contains(self, parameterName: str, ) -> bool:
        ...

    @abc.abstractmethod
    def IndexOf(self, parameterName: str, ) -> int:
        ...

    @abc.abstractmethod
    def RemoveAt(self, parameterName: str, ) -> None:
        ...

class UpdateStatus(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    Continue: int = ...
    ErrorsOccurred: int = ...
    SkipCurrentRow: int = ...
    SkipAllRemainingRows: int = ...

class ConflictOption(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    CompareAllSearchableValues: int = ...
    CompareRowVersion: int = ...
    OverwriteChanges: int = ...

class StatementType(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    Select: int = ...
    Insert: int = ...
    Update: int = ...
    Delete: int = ...
    Batch: int = ...

class IDataParameter(abc.ABC):
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

    @property
    @abc.abstractmethod
    def ParameterName(self) -> str:
        ...
    @ParameterName.setter
    @abc.abstractmethod
    def ParameterName(self, val: str):
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
    def SourceVersion(self) -> int:
        ...
    @SourceVersion.setter
    @abc.abstractmethod
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
class IDbCommand(System.IDisposable, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    @abc.abstractmethod
    def Connection(self) -> System.Data.IDbConnection:
        ...
    @Connection.setter
    @abc.abstractmethod
    def Connection(self, val: System.Data.IDbConnection):
        ...

    @property
    @abc.abstractmethod
    def Transaction(self) -> System.Data.IDbTransaction:
        ...
    @Transaction.setter
    @abc.abstractmethod
    def Transaction(self, val: System.Data.IDbTransaction):
        ...

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
    @abc.abstractmethod
    def Parameters(self) -> System.Data.IDataParameterCollection:
        ...

    @property
    @abc.abstractmethod
    def UpdatedRowSource(self) -> int:
        ...
    @UpdatedRowSource.setter
    @abc.abstractmethod
    def UpdatedRowSource(self, val: int):
        ...

    # methods
    @abc.abstractmethod
    def Prepare(self, ) -> None:
        ...

    @abc.abstractmethod
    def Cancel(self, ) -> None:
        ...

    @abc.abstractmethod
    def CreateParameter(self, ) -> System.Data.IDbDataParameter:
        ...

    @abc.abstractmethod
    def ExecuteNonQuery(self, ) -> int:
        ...

    @abc.abstractmethod
    @typing.overload
    def ExecuteReader(self, ) -> System.Data.IDataReader:
        ...

    @abc.abstractmethod
    @typing.overload
    def ExecuteReader(self, behavior: int, ) -> System.Data.IDataReader:
        ...

    @abc.abstractmethod
    def ExecuteScalar(self, ) -> System.Object:
        ...

class UpdateRowSource(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    None_: int = ...
    OutputParameters: int = ...
    FirstReturnedRecord: int = ...
    Both: int = ...

class XmlWriteMode(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    WriteSchema: int = ...
    IgnoreSchema: int = ...
    DiffGram: int = ...

class IDataReader(System.IDisposable, System.Data.IDataRecord, abc.ABC):
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
    def IsClosed(self) -> bool:
        ...

    @property
    @abc.abstractmethod
    def RecordsAffected(self) -> int:
        ...

    # methods
    @abc.abstractmethod
    def Close(self, ) -> None:
        ...

    @abc.abstractmethod
    def GetSchemaTable(self, ) -> System.Data.DataTable:
        ...

    @abc.abstractmethod
    def NextResult(self, ) -> bool:
        ...

    @abc.abstractmethod
    def Read(self, ) -> bool:
        ...

class IColumnMapping(abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    @abc.abstractmethod
    def DataSetColumn(self) -> str:
        ...
    @DataSetColumn.setter
    @abc.abstractmethod
    def DataSetColumn(self, val: str):
        ...

    @property
    @abc.abstractmethod
    def SourceColumn(self) -> str:
        ...
    @SourceColumn.setter
    @abc.abstractmethod
    def SourceColumn(self, val: str):
        ...

    # methods
class ITableMappingCollection(System.Collections.IList, System.Collections.ICollection, System.Collections.IEnumerable, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    @abc.abstractmethod
    def Item(self) -> System.Object:
        ...
    @Item.setter
    @abc.abstractmethod
    def Item(self, val: System.Object):
        ...

    # methods
    @abc.abstractmethod
    def Add(self, sourceTableName: str, dataSetTableName: str, ) -> System.Data.ITableMapping:
        ...

    @abc.abstractmethod
    def Contains(self, sourceTableName: str, ) -> bool:
        ...

    @abc.abstractmethod
    def GetByDataSetTable(self, dataSetTableName: str, ) -> System.Data.ITableMapping:
        ...

    @abc.abstractmethod
    def IndexOf(self, sourceTableName: str, ) -> int:
        ...

    @abc.abstractmethod
    def RemoveAt(self, sourceTableName: str, ) -> None:
        ...

class DataRowView(System.ComponentModel.ICustomTypeDescriptor, System.ComponentModel.IEditableObject, System.ComponentModel.IDataErrorInfo, System.ComponentModel.INotifyPropertyChanged, System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

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
    def Item(self) -> str:
        ...

    @property
    def Error(self) -> str:
        ...

    @property
    def RowVersion(self) -> int:
        ...

    @property
    def RowVersionDefault(self) -> int:
        ...

    @property
    def Row(self) -> System.Data.DataRow:
        ...

    @property
    def IsNew(self) -> bool:
        ...

    @property
    def IsEdit(self) -> bool:
        ...

    # methods
    def __init__(self, dataView: System.Data.DataView, row: System.Data.DataRow, ):
        ...

    def Equals(self, other: System.Object, ) -> bool:
        ...

    def GetHashCode(self, ) -> int:
        ...

    def GetRecord(self, ) -> int:
        ...

    def HasRecord(self, ) -> bool:
        ...

    def GetColumnValue(self, column: System.Data.DataColumn, ) -> System.Object:
        ...

    def SetColumnValue(self, column: System.Data.DataColumn, value: System.Object, ) -> None:
        ...

    @typing.overload
    def CreateChildView(self, relation: System.Data.DataRelation, followParent: bool, ) -> System.Data.DataView:
        ...

    @typing.overload
    def CreateChildView(self, relation: System.Data.DataRelation, ) -> System.Data.DataView:
        ...

    @typing.overload
    def CreateChildView(self, relationName: str, followParent: bool, ) -> System.Data.DataView:
        ...

    @typing.overload
    def CreateChildView(self, relationName: str, ) -> System.Data.DataView:
        ...

    def BeginEdit(self, ) -> None:
        ...

    def CancelEdit(self, ) -> None:
        ...

    def EndEdit(self, ) -> None:
        ...

    def Delete(self, ) -> None:
        ...

    def RaisePropertyChangedEvent(self, propName: str, ) -> None:
        ...

    def GetAttributes(self, ) -> System.ComponentModel.AttributeCollection:
        ...

    def GetClassName(self, ) -> str:
        ...

    def GetComponentName(self, ) -> str:
        ...

    def GetConverter(self, ) -> System.ComponentModel.TypeConverter:
        ...

    def GetDefaultEvent(self, ) -> System.ComponentModel.EventDescriptor:
        ...

    def GetDefaultProperty(self, ) -> System.ComponentModel.PropertyDescriptor:
        ...

    def GetEditor(self, editorBaseType: System.Type, ) -> System.Object:
        ...

    @typing.overload
    def GetEvents(self, ) -> System.ComponentModel.EventDescriptorCollection:
        ...

    @typing.overload
    def GetEvents(self, attributes: System.Array[System.Attribute], ) -> System.ComponentModel.EventDescriptorCollection:
        ...

    @typing.overload
    def GetProperties(self, ) -> System.ComponentModel.PropertyDescriptorCollection:
        ...

    @typing.overload
    def GetProperties(self, attributes: System.Array[System.Attribute], ) -> System.ComponentModel.PropertyDescriptorCollection:
        ...

    def GetPropertyOwner(self, pd: System.ComponentModel.PropertyDescriptor, ) -> System.Object:
        ...

class IDbDataAdapter(System.Data.IDataAdapter, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    @abc.abstractmethod
    def SelectCommand(self) -> System.Data.IDbCommand:
        ...
    @SelectCommand.setter
    @abc.abstractmethod
    def SelectCommand(self, val: System.Data.IDbCommand):
        ...

    @property
    @abc.abstractmethod
    def InsertCommand(self) -> System.Data.IDbCommand:
        ...
    @InsertCommand.setter
    @abc.abstractmethod
    def InsertCommand(self, val: System.Data.IDbCommand):
        ...

    @property
    @abc.abstractmethod
    def UpdateCommand(self) -> System.Data.IDbCommand:
        ...
    @UpdateCommand.setter
    @abc.abstractmethod
    def UpdateCommand(self, val: System.Data.IDbCommand):
        ...

    @property
    @abc.abstractmethod
    def DeleteCommand(self) -> System.Data.IDbCommand:
        ...
    @DeleteCommand.setter
    @abc.abstractmethod
    def DeleteCommand(self, val: System.Data.IDbCommand):
        ...

    # methods
class DataColumnCollection(System.Collections.ICollection, System.Collections.IEnumerable, System.Data.InternalDataCollectionBase):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def List(self) -> System.Collections.ArrayList:
        ...

    @property
    def ColumnsImplementingIChangeTracking(self) -> System.Array[System.Data.DataColumn]:
        ...

    @property
    def ColumnsImplementingIChangeTrackingCount(self) -> int:
        ...

    @property
    def ColumnsImplementingIRevertibleChangeTrackingCount(self) -> int:
        ...

    @property
    def Item(self) -> System.Data.DataColumn:
        ...

    @property
    def Item(self) -> System.Data.DataColumn:
        ...

    @property
    def Item(self) -> System.Data.DataColumn:
        ...

    @property
    def Count(self) -> int:
        ...

    @property
    def IsReadOnly(self) -> bool:
        ...

    @property
    def IsSynchronized(self) -> bool:
        ...

    @property
    def SyncRoot(self) -> System.Object:
        ...

    # methods
    def __init__(self, table: System.Data.DataTable, ):
        ...

    def EnsureAdditionalCapacity(self, capacity: int, ) -> None:
        ...

    @typing.overload
    def Add(self, column: System.Data.DataColumn, ) -> None:
        ...

    @typing.overload
    def Add(self, columnName: str, type: System.Type, expression: str, ) -> System.Data.DataColumn:
        ...

    @typing.overload
    def Add(self, columnName: str, type: System.Type, ) -> System.Data.DataColumn:
        ...

    @typing.overload
    def Add(self, columnName: str, ) -> System.Data.DataColumn:
        ...

    @typing.overload
    def Add(self, ) -> System.Data.DataColumn:
        ...

    def AddAt(self, index: int, column: System.Data.DataColumn, ) -> None:
        ...

    def AddRange(self, columns: System.Array[System.Data.DataColumn], ) -> None:
        ...

    @typing.overload
    def ArrayAdd(self, column: System.Data.DataColumn, ) -> None:
        ...

    @typing.overload
    def ArrayAdd(self, index: int, column: System.Data.DataColumn, ) -> None:
        ...

    def ArrayRemove(self, column: System.Data.DataColumn, ) -> None:
        ...

    def AssignName(self, ) -> str:
        ...

    def BaseAdd(self, column: System.Data.DataColumn, ) -> None:
        ...

    def BaseGroupSwitch(self, oldArray: System.Array[System.Data.DataColumn], oldLength: int, newArray: System.Array[System.Data.DataColumn], newLength: int, ) -> None:
        ...

    def BaseRemove(self, column: System.Data.DataColumn, ) -> None:
        ...

    @typing.overload
    def CanRemove(self, column: System.Data.DataColumn, ) -> bool:
        ...

    @typing.overload
    def CanRemove(self, column: System.Data.DataColumn, fThrowException: bool, ) -> bool:
        ...

    def CheckIChangeTracking(self, column: System.Data.DataColumn, ) -> None:
        ...

    def Clear(self, ) -> None:
        ...

    @typing.overload
    def Contains(self, name: str, ) -> bool:
        ...

    @typing.overload
    def Contains(self, name: str, caseSensitive: bool, ) -> bool:
        ...

    def CopyTo(self, array: System.Array[System.Data.DataColumn], index: int, ) -> None:
        ...

    @typing.overload
    def IndexOf(self, column: System.Data.DataColumn, ) -> int:
        ...

    @typing.overload
    def IndexOf(self, columnName: str, ) -> int:
        ...

    def IndexOfCaseInsensitive(self, name: str, ) -> int:
        ...

    def FinishInitCollection(self, ) -> None:
        ...

    def MakeName(self, index: int, ) -> str:
        ...

    def MoveTo(self, column: System.Data.DataColumn, newPosition: int, ) -> None:
        ...

    def OnCollectionChanged(self, ccevent: System.ComponentModel.CollectionChangeEventArgs, ) -> None:
        ...

    def OnCollectionChanging(self, ccevent: System.ComponentModel.CollectionChangeEventArgs, ) -> None:
        ...

    def OnColumnPropertyChanged(self, ccevent: System.ComponentModel.CollectionChangeEventArgs, ) -> None:
        ...

    def RegisterColumnName(self, name: str, column: System.Data.DataColumn, ) -> None:
        ...

    def CanRegisterName(self, name: str, ) -> bool:
        ...

    @typing.overload
    def Remove(self, column: System.Data.DataColumn, ) -> None:
        ...

    @typing.overload
    def Remove(self, name: str, ) -> None:
        ...

    def RemoveAt(self, index: int, ) -> None:
        ...

    def UnregisterName(self, name: str, ) -> None:
        ...

    def AddColumnsImplementingIChangeTrackingList(self, dataColumn: System.Data.DataColumn, ) -> None:
        ...

    def RemoveColumnsImplementingIChangeTrackingList(self, dataColumn: System.Data.DataColumn, ) -> None:
        ...

class IColumnMappingCollection(System.Collections.IList, System.Collections.ICollection, System.Collections.IEnumerable, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    @abc.abstractmethod
    def Item(self) -> System.Object:
        ...
    @Item.setter
    @abc.abstractmethod
    def Item(self, val: System.Object):
        ...

    # methods
    @abc.abstractmethod
    def Add(self, sourceColumnName: str, dataSetColumnName: str, ) -> System.Data.IColumnMapping:
        ...

    @abc.abstractmethod
    def Contains(self, sourceColumnName: str, ) -> bool:
        ...

    @abc.abstractmethod
    def GetByDataSetColumn(self, dataSetColumnName: str, ) -> System.Data.IColumnMapping:
        ...

    @abc.abstractmethod
    def IndexOf(self, sourceColumnName: str, ) -> int:
        ...

    @abc.abstractmethod
    def RemoveAt(self, sourceColumnName: str, ) -> None:
        ...

