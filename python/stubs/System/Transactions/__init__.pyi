from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import System
import System.Runtime.Serialization
import System.Transactions
import System.Transactions.Distributed


class Transaction(System.IDisposable, System.Runtime.Serialization.ISerializable, System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        self._isoLevel: int
        self._complete: bool
        self._cloneId: int
        self._disposed: int
        self._internalTransaction: System.Transactions.InternalTransaction
        self._traceIdentifier: System.Transactions.TransactionTraceIdentifier
        ...

    # static fields

    # properties
    @property
    def Current(self) -> System.Transactions.Transaction:
        ...
    @Current.setter
    def Current(self, val: System.Transactions.Transaction):
        ...

    @property
    def Disposed(self) -> bool:
        ...

    @property
    def DistributedTxId(self) -> System.Guid:
        ...

    @property
    def TransactionInformation(self) -> System.Transactions.TransactionInformation:
        ...

    @property
    def IsolationLevel(self) -> int:
        ...

    @property
    def PromoterType(self) -> System.Guid:
        ...

    @property
    def TransactionTraceId(self) -> System.Transactions.TransactionTraceIdentifier:
        ...

    # methods
    @typing.overload
    def __init__(self, isoLevel: int, internalTransaction: System.Transactions.InternalTransaction, ):
        ...

    @typing.overload
    def __init__(self, distributedTransaction: System.Transactions.Distributed.DistributedTransaction, ):
        ...

    @typing.overload
    def __init__(self, isoLevel: int, superior: System.Transactions.ISimpleTransactionSuperior, ):
        ...

    @staticmethod
    def InteropMode(currentScope: System.Transactions.TransactionScope, ) -> int:
        ...

    @staticmethod
    def FastGetTransaction(currentScope: System.Transactions.TransactionScope, contextData: System.Transactions.ContextData, contextTransaction: ref[System.Transactions.Transaction], ) -> System.Transactions.Transaction:
        ...

    @staticmethod
    def GetCurrentTransactionAndScope(defaultLookup: int, current: ref[System.Transactions.Transaction], currentScope: ref[System.Transactions.TransactionScope], contextTransaction: ref[System.Transactions.Transaction], ) -> None:
        ...

    def GetHashCode(self, ) -> int:
        ...

    def Equals(self, obj: System.Object, ) -> bool:
        ...

    def GetPromotedToken(self, ) -> System.Array[int]:
        ...

    @typing.overload
    def EnlistDurable(self, resourceManagerIdentifier: System.Guid, enlistmentNotification: System.Transactions.IEnlistmentNotification, enlistmentOptions: int, ) -> System.Transactions.Enlistment:
        ...

    @typing.overload
    def EnlistDurable(self, resourceManagerIdentifier: System.Guid, singlePhaseNotification: System.Transactions.ISinglePhaseNotification, enlistmentOptions: int, ) -> System.Transactions.Enlistment:
        ...

    @typing.overload
    def Rollback(self, ) -> None:
        ...

    @typing.overload
    def Rollback(self, e: System.Exception, ) -> None:
        ...

    @typing.overload
    def EnlistVolatile(self, enlistmentNotification: System.Transactions.IEnlistmentNotification, enlistmentOptions: int, ) -> System.Transactions.Enlistment:
        ...

    @typing.overload
    def EnlistVolatile(self, singlePhaseNotification: System.Transactions.ISinglePhaseNotification, enlistmentOptions: int, ) -> System.Transactions.Enlistment:
        ...

    def Clone(self, ) -> System.Transactions.Transaction:
        ...

    def InternalClone(self, ) -> System.Transactions.Transaction:
        ...

    def DependentClone(self, cloneOption: int, ) -> System.Transactions.DependentTransaction:
        ...

    def Dispose(self, ) -> None:
        ...

    def InternalDispose(self, ) -> None:
        ...

    def GetObjectData(self, serializationInfo: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext, ) -> None:
        ...

    @typing.overload
    def EnlistPromotableSinglePhase(self, promotableSinglePhaseNotification: System.Transactions.IPromotableSinglePhaseNotification, ) -> bool:
        ...

    @typing.overload
    def EnlistPromotableSinglePhase(self, promotableSinglePhaseNotification: System.Transactions.IPromotableSinglePhaseNotification, promoterType: System.Guid, ) -> bool:
        ...

    def PromoteAndEnlistDurable(self, resourceManagerIdentifier: System.Guid, promotableNotification: System.Transactions.IPromotableSinglePhaseNotification, enlistmentNotification: System.Transactions.ISinglePhaseNotification, enlistmentOptions: int, ) -> System.Transactions.Enlistment:
        ...

    def SetDistributedTransactionIdentifier(self, promotableNotification: System.Transactions.IPromotableSinglePhaseNotification, distributedTransactionIdentifier: System.Guid, ) -> None:
        ...

    def Promote(self, ) -> System.Transactions.Distributed.DistributedTransaction:
        ...

class TransactionInformation(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def LocalIdentifier(self) -> str:
        ...

    @property
    def DistributedIdentifier(self) -> System.Guid:
        ...

    @property
    def CreationTime(self) -> System.DateTime:
        ...

    @property
    def Status(self) -> int:
        ...

    # methods
    def __init__(self, internalTransaction: System.Transactions.InternalTransaction, ):
        ...

class TransactionStatus(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    Active: int = ...
    Committed: int = ...
    Aborted: int = ...
    InDoubt: int = ...

class ISinglePhaseNotification(System.Transactions.IEnlistmentNotification, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    @abc.abstractmethod
    def SinglePhaseCommit(self, singlePhaseEnlistment: System.Transactions.SinglePhaseEnlistment, ) -> None:
        ...

class DependentTransaction(System.IDisposable, System.Runtime.Serialization.ISerializable, System.Transactions.Transaction):
    @typing.overload
    def __init__(self, **kwargs):
        self._isoLevel: int
        self._complete: bool
        self._cloneId: int
        self._disposed: int
        self._internalTransaction: System.Transactions.InternalTransaction
        self._traceIdentifier: System.Transactions.TransactionTraceIdentifier
        ...

    # static fields

    # properties
    @property
    def Disposed(self) -> bool:
        ...

    @property
    def DistributedTxId(self) -> System.Guid:
        ...

    @property
    def TransactionInformation(self) -> System.Transactions.TransactionInformation:
        ...

    @property
    def IsolationLevel(self) -> int:
        ...

    @property
    def PromoterType(self) -> System.Guid:
        ...

    @property
    def TransactionTraceId(self) -> System.Transactions.TransactionTraceIdentifier:
        ...

    # methods
    def __init__(self, isoLevel: int, internalTransaction: System.Transactions.InternalTransaction, blocking: bool, ):
        ...

    def Complete(self, ) -> None:
        ...

class Enlistment(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        self._internalEnlistment: System.Transactions.InternalEnlistment
        ...

    # static fields

    # properties
    @property
    def InternalEnlistment(self) -> System.Transactions.InternalEnlistment:
        ...

    # methods
    @typing.overload
    def __init__(self, internalEnlistment: System.Transactions.InternalEnlistment, ):
        ...

    @typing.overload
    def __init__(self, resourceManagerIdentifier: System.Guid, transaction: System.Transactions.InternalTransaction, twoPhaseNotifications: System.Transactions.IEnlistmentNotification, singlePhaseNotifications: System.Transactions.ISinglePhaseNotification, atomicTransaction: System.Transactions.Transaction, ):
        ...

    @typing.overload
    def __init__(self, transaction: System.Transactions.InternalTransaction, twoPhaseNotifications: System.Transactions.IEnlistmentNotification, singlePhaseNotifications: System.Transactions.ISinglePhaseNotification, atomicTransaction: System.Transactions.Transaction, enlistmentOptions: int, ):
        ...

    @typing.overload
    def __init__(self, transaction: System.Transactions.InternalTransaction, promotableSinglePhaseNotification: System.Transactions.IPromotableSinglePhaseNotification, atomicTransaction: System.Transactions.Transaction, ):
        ...

    @typing.overload
    def __init__(self, twoPhaseNotifications: System.Transactions.IEnlistmentNotification, transaction: System.Transactions.InternalTransaction, atomicTransaction: System.Transactions.Transaction, ):
        ...

    @typing.overload
    def __init__(self, twoPhaseNotifications: System.Transactions.IEnlistmentNotification, syncRoot: System.Object, ):
        ...

    def Done(self, ) -> None:
        ...

class IPromotableSinglePhaseNotification(System.Transactions.ITransactionPromoter, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    @abc.abstractmethod
    def Initialize(self, ) -> None:
        ...

    @abc.abstractmethod
    def SinglePhaseCommit(self, singlePhaseEnlistment: System.Transactions.SinglePhaseEnlistment, ) -> None:
        ...

    @abc.abstractmethod
    def Rollback(self, singlePhaseEnlistment: System.Transactions.SinglePhaseEnlistment, ) -> None:
        ...

class ITransactionPromoter(abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    @abc.abstractmethod
    def Promote(self, ) -> System.Array[int]:
        ...

class IEnlistmentNotification(abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    @abc.abstractmethod
    def Prepare(self, preparingEnlistment: System.Transactions.PreparingEnlistment, ) -> None:
        ...

    @abc.abstractmethod
    def Commit(self, enlistment: System.Transactions.Enlistment, ) -> None:
        ...

    @abc.abstractmethod
    def Rollback(self, enlistment: System.Transactions.Enlistment, ) -> None:
        ...

    @abc.abstractmethod
    def InDoubt(self, enlistment: System.Transactions.Enlistment, ) -> None:
        ...

class PreparingEnlistment(System.Transactions.Enlistment):
    @typing.overload
    def __init__(self, **kwargs):
        self._internalEnlistment: System.Transactions.InternalEnlistment
        ...

    # static fields

    # properties
    @property
    def InternalEnlistment(self) -> System.Transactions.InternalEnlistment:
        ...

    # methods
    def __init__(self, enlistment: System.Transactions.InternalEnlistment, ):
        ...

    def Prepared(self, ) -> None:
        ...

    @typing.overload
    def ForceRollback(self, ) -> None:
        ...

    @typing.overload
    def ForceRollback(self, e: System.Exception, ) -> None:
        ...

    def RecoveryInformation(self, ) -> System.Array[int]:
        ...

class TransactionScope(System.IDisposable, System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def ScopeComplete(self) -> bool:
        ...

    @property
    def InteropMode(self) -> int:
        ...

    @property
    def ContextKey(self) -> System.Transactions.ContextKey:
        ...
    @ContextKey.setter
    def ContextKey(self, val: System.Transactions.ContextKey):
        ...

    @property
    def AsyncFlowEnabled(self) -> bool:
        ...
    @AsyncFlowEnabled.setter
    def AsyncFlowEnabled(self, val: bool):
        ...

    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def __init__(self, scopeOption: int, ):
        ...

    @typing.overload
    def __init__(self, asyncFlowOption: int, ):
        ...

    @typing.overload
    def __init__(self, scopeOption: int, asyncFlowOption: int, ):
        ...

    @typing.overload
    def __init__(self, scopeOption: int, scopeTimeout: System.TimeSpan, ):
        ...

    @typing.overload
    def __init__(self, scopeOption: int, scopeTimeout: System.TimeSpan, asyncFlowOption: int, ):
        ...

    @typing.overload
    def __init__(self, scopeOption: int, transactionOptions: System.Transactions.TransactionOptions, ):
        ...

    @typing.overload
    def __init__(self, scopeOption: int, transactionOptions: System.Transactions.TransactionOptions, asyncFlowOption: int, ):
        ...

    @typing.overload
    def __init__(self, scopeOption: int, transactionOptions: System.Transactions.TransactionOptions, interopOption: int, ):
        ...

    @typing.overload
    def __init__(self, transactionToUse: System.Transactions.Transaction, ):
        ...

    @typing.overload
    def __init__(self, transactionToUse: System.Transactions.Transaction, asyncFlowOption: int, ):
        ...

    @typing.overload
    def __init__(self, transactionToUse: System.Transactions.Transaction, scopeTimeout: System.TimeSpan, ):
        ...

    @typing.overload
    def __init__(self, transactionToUse: System.Transactions.Transaction, scopeTimeout: System.TimeSpan, asyncFlowOption: int, ):
        ...

    @typing.overload
    def __init__(self, transactionToUse: System.Transactions.Transaction, scopeTimeout: System.TimeSpan, interopOption: int, ):
        ...

    def NeedToCreateTransaction(self, scopeOption: int, ) -> bool:
        ...

    def Initialize(self, transactionToUse: System.Transactions.Transaction, scopeTimeout: System.TimeSpan, interopModeSpecified: bool, ) -> None:
        ...

    def Dispose(self, ) -> None:
        ...

    def InternalDispose(self, ) -> None:
        ...

    def Complete(self, ) -> None:
        ...

    @staticmethod
    def TimerCallback(state: System.Object, ) -> None:
        ...

    def Timeout(self, ) -> None:
        ...

    def CommonInitialize(self, ) -> None:
        ...

    def PushScope(self, ) -> None:
        ...

    def PopScope(self, ) -> None:
        ...

    def SetCurrent(self, newCurrent: System.Transactions.Transaction, ) -> None:
        ...

    def SaveTLSContextData(self, ) -> None:
        ...

    def RestoreSavedTLSContextData(self, ) -> None:
        ...

    def RestoreCurrent(self, ) -> None:
        ...

    def ValidateInteropOption(self, interopOption: int, ) -> None:
        ...

    def ValidateScopeTimeout(self, paramName: str, scopeTimeout: System.TimeSpan, ) -> None:
        ...

    def ValidateAndSetAsyncFlowOption(self, asyncFlowOption: int, ) -> None:
        ...

    def ValidateAsyncFlowOptionAndESInteropOption(self, ) -> None:
        ...

class TransactionScopeOption(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    Required: int = ...
    RequiresNew: int = ...
    Suppress: int = ...

class TransactionScopeAsyncFlowOption(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    Suppress: int = ...
    Enabled: int = ...

class ISimpleTransactionSuperior(System.Transactions.ITransactionPromoter, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    @abc.abstractmethod
    def Rollback(self, ) -> None:
        ...

class SinglePhaseEnlistment(System.Transactions.Enlistment):
    @typing.overload
    def __init__(self, **kwargs):
        self._internalEnlistment: System.Transactions.InternalEnlistment
        ...

    # static fields

    # properties
    @property
    def InternalEnlistment(self) -> System.Transactions.InternalEnlistment:
        ...

    # methods
    def __init__(self, enlistment: System.Transactions.InternalEnlistment, ):
        ...

    @typing.overload
    def Aborted(self, ) -> None:
        ...

    @typing.overload
    def Aborted(self, e: System.Exception, ) -> None:
        ...

    def Committed(self, ) -> None:
        ...

    @typing.overload
    def InDoubt(self, ) -> None:
        ...

    @typing.overload
    def InDoubt(self, e: System.Exception, ) -> None:
        ...

class EnlistmentOptions(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    None_: int = ...
    EnlistDuringPrepareRequired: int = ...

class IsolationLevel(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    Serializable: int = ...
    RepeatableRead: int = ...
    ReadCommitted: int = ...
    ReadUncommitted: int = ...
    Snapshot: int = ...
    Chaos: int = ...
    Unspecified: int = ...

class TransactionOptions(System.ValueType):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def Timeout(self) -> System.TimeSpan:
        ...
    @Timeout.setter
    def Timeout(self, val: System.TimeSpan):
        ...

    @property
    def IsolationLevel(self) -> int:
        ...
    @IsolationLevel.setter
    def IsolationLevel(self, val: int):
        ...

    # methods
    def GetHashCode(self, ) -> int:
        ...

    @typing.overload
    def Equals(self, obj: System.Object, ) -> bool:
        ...

    @typing.overload
    def Equals(self, other: System.Transactions.TransactionOptions, ) -> bool:
        ...

class EnterpriseServicesInteropOption(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    None_: int = ...
    Automatic: int = ...
    Full: int = ...

class DependentCloneOption(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    BlockCommitUntilComplete: int = ...
    RollbackIfNotComplete: int = ...

