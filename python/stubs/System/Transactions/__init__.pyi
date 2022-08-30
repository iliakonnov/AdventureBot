from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import System
import System.Runtime.Serialization
import System.Transactions


class Transaction(System.IDisposable, System.Runtime.Serialization.ISerializable, System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def Current(self) -> System.Transactions.Transaction:
        ...
    @Current.setter
    def Current(self, val: System.Transactions.Transaction):
        ...

    @property
    def TransactionInformation(self) -> System.Transactions.TransactionInformation:
        ...

    @property
    def IsolationLevel(self) -> System.Transactions.IsolationLevel:
        ...

    @property
    def PromoterType(self) -> System.Guid:
        ...

    # methods
    @typing.overload
    def GetHashCode(self, ) -> System.Int32:
        ...

    @typing.overload
    def Equals(self, obj: System.Object, ) -> System.Boolean:
        ...

    @typing.overload
    def GetPromotedToken(self, ) -> list[System.Byte]:
        ...

    @typing.overload
    def EnlistDurable(self, resourceManagerIdentifier: System.Guid, enlistmentNotification: System.Transactions.IEnlistmentNotification, enlistmentOptions: System.Transactions.EnlistmentOptions, ) -> System.Transactions.Enlistment:
        ...

    @typing.overload
    def EnlistDurable(self, resourceManagerIdentifier: System.Guid, singlePhaseNotification: System.Transactions.ISinglePhaseNotification, enlistmentOptions: System.Transactions.EnlistmentOptions, ) -> System.Transactions.Enlistment:
        ...

    @typing.overload
    def Rollback(self, ) -> None:
        ...

    @typing.overload
    def Rollback(self, e: System.Exception, ) -> None:
        ...

    @typing.overload
    def EnlistVolatile(self, enlistmentNotification: System.Transactions.IEnlistmentNotification, enlistmentOptions: System.Transactions.EnlistmentOptions, ) -> System.Transactions.Enlistment:
        ...

    @typing.overload
    def EnlistVolatile(self, singlePhaseNotification: System.Transactions.ISinglePhaseNotification, enlistmentOptions: System.Transactions.EnlistmentOptions, ) -> System.Transactions.Enlistment:
        ...

    @typing.overload
    def Clone(self, ) -> System.Transactions.Transaction:
        ...

    @typing.overload
    def DependentClone(self, cloneOption: System.Transactions.DependentCloneOption, ) -> System.Transactions.DependentTransaction:
        ...

    @typing.overload
    def Dispose(self, ) -> None:
        ...

    @typing.overload
    def EnlistPromotableSinglePhase(self, promotableSinglePhaseNotification: System.Transactions.IPromotableSinglePhaseNotification, ) -> System.Boolean:
        ...

    @typing.overload
    def EnlistPromotableSinglePhase(self, promotableSinglePhaseNotification: System.Transactions.IPromotableSinglePhaseNotification, promoterType: System.Guid, ) -> System.Boolean:
        ...

    @typing.overload
    def PromoteAndEnlistDurable(self, resourceManagerIdentifier: System.Guid, promotableNotification: System.Transactions.IPromotableSinglePhaseNotification, enlistmentNotification: System.Transactions.ISinglePhaseNotification, enlistmentOptions: System.Transactions.EnlistmentOptions, ) -> System.Transactions.Enlistment:
        ...

    @typing.overload
    def SetDistributedTransactionIdentifier(self, promotableNotification: System.Transactions.IPromotableSinglePhaseNotification, distributedTransactionIdentifier: System.Guid, ) -> None:
        ...

class TransactionInformation(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def LocalIdentifier(self) -> System.String:
        ...

    @property
    def DistributedIdentifier(self) -> System.Guid:
        ...

    @property
    def CreationTime(self) -> System.DateTime:
        ...

    @property
    def Status(self) -> System.Transactions.TransactionStatus:
        ...

    # methods
class IsolationLevel(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    Serializable: System.Int32 = Serializable
    RepeatableRead: System.Int32 = RepeatableRead
    ReadCommitted: System.Int32 = ReadCommitted
    ReadUncommitted: System.Int32 = ReadUncommitted
    Snapshot: System.Int32 = Snapshot
    Chaos: System.Int32 = Chaos
    Unspecified: System.Int32 = Unspecified

class IEnlistmentNotification(abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    # methods
    @typing.overload
    @abc.abstractmethod
    def Prepare(self, preparingEnlistment: System.Transactions.PreparingEnlistment, ) -> None:
        ...

    @typing.overload
    @abc.abstractmethod
    def Commit(self, enlistment: System.Transactions.Enlistment, ) -> None:
        ...

    @typing.overload
    @abc.abstractmethod
    def Rollback(self, enlistment: System.Transactions.Enlistment, ) -> None:
        ...

    @typing.overload
    @abc.abstractmethod
    def InDoubt(self, enlistment: System.Transactions.Enlistment, ) -> None:
        ...

class EnlistmentOptions(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    None_: System.Int32 = None
    EnlistDuringPrepareRequired: System.Int32 = EnlistDuringPrepareRequired

class Enlistment(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    # methods
    @typing.overload
    def Done(self, ) -> None:
        ...

class ISinglePhaseNotification(System.Transactions.IEnlistmentNotification, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    # methods
    @typing.overload
    @abc.abstractmethod
    def SinglePhaseCommit(self, singlePhaseEnlistment: System.Transactions.SinglePhaseEnlistment, ) -> None:
        ...

class DependentCloneOption(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    BlockCommitUntilComplete: System.Int32 = BlockCommitUntilComplete
    RollbackIfNotComplete: System.Int32 = RollbackIfNotComplete

class DependentTransaction(System.IDisposable, System.Runtime.Serialization.ISerializable, System.Transactions.Transaction):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def TransactionInformation(self) -> System.Transactions.TransactionInformation:
        ...

    @property
    def IsolationLevel(self) -> System.Transactions.IsolationLevel:
        ...

    @property
    def PromoterType(self) -> System.Guid:
        ...

    # methods
    @typing.overload
    def Complete(self, ) -> None:
        ...

class IPromotableSinglePhaseNotification(System.Transactions.ITransactionPromoter, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    # methods
    @typing.overload
    @abc.abstractmethod
    def Initialize(self, ) -> None:
        ...

    @typing.overload
    @abc.abstractmethod
    def SinglePhaseCommit(self, singlePhaseEnlistment: System.Transactions.SinglePhaseEnlistment, ) -> None:
        ...

    @typing.overload
    @abc.abstractmethod
    def Rollback(self, singlePhaseEnlistment: System.Transactions.SinglePhaseEnlistment, ) -> None:
        ...

class TransactionStatus(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    Active: System.Int32 = Active
    Committed: System.Int32 = Committed
    Aborted: System.Int32 = Aborted
    InDoubt: System.Int32 = InDoubt

class PreparingEnlistment(System.Transactions.Enlistment):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    # methods
    @typing.overload
    def Prepared(self, ) -> None:
        ...

    @typing.overload
    def ForceRollback(self, ) -> None:
        ...

    @typing.overload
    def ForceRollback(self, e: System.Exception, ) -> None:
        ...

    @typing.overload
    def RecoveryInformation(self, ) -> list[System.Byte]:
        ...

class SinglePhaseEnlistment(System.Transactions.Enlistment):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    # methods
    @typing.overload
    def Aborted(self, ) -> None:
        ...

    @typing.overload
    def Aborted(self, e: System.Exception, ) -> None:
        ...

    @typing.overload
    def Committed(self, ) -> None:
        ...

    @typing.overload
    def InDoubt(self, ) -> None:
        ...

    @typing.overload
    def InDoubt(self, e: System.Exception, ) -> None:
        ...

class ITransactionPromoter(abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    # methods
    @typing.overload
    @abc.abstractmethod
    def Promote(self, ) -> list[System.Byte]:
        ...

