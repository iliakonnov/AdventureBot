from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import AdventureBot.Room.BetterRoom
import Content.Town.Auction
import System.Collections.Generic
import AdventureBot.Room
import AdventureBot.User
import AdventureBot.Messenger
import System
import AdventureBot
import System.Collections
import System.Runtime.Serialization
import System.Collections.Generic.Dictionary

T = typing.TypeVar('T')

class AddOfferActionBase(AdventureBot.Room.BetterRoom.ActionBase[Content.Town.Auction.AuctionRoom], abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        self.Buttons: System.Collections.Generic.Dictionary[str, AdventureBot.Room.MessageReceived]
        self.Room: AdventureBot.Room.BetterRoom.BetterRoomBase
        ...

    # static fields

    # properties
    @property
    def Room(self) -> Content.Town.Auction.AuctionRoom:
        ...

    # methods
    def __init__(self, room: Content.Town.Auction.AuctionRoom, ):
        ...

    def Enter(self, user: AdventureBot.User.User, ) -> None:
        ...

    def ItemSelected(self, user: AdventureBot.User.User, message: AdventureBot.Messenger.ReceivedMessage, ) -> None:
        ...

    def Back(self, user: AdventureBot.User.User, message: AdventureBot.Messenger.ReceivedMessage, ) -> None:
        ...

class RemoveOfferActionBase(AdventureBot.Room.BetterRoom.ActionBase[Content.Town.Auction.AuctionRoom], abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        self.Buttons: System.Collections.Generic.Dictionary[str, AdventureBot.Room.MessageReceived]
        self.Room: AdventureBot.Room.BetterRoom.BetterRoomBase
        ...

    # static fields

    # properties
    @property
    def Room(self) -> Content.Town.Auction.AuctionRoom:
        ...

    # methods
    def __init__(self, room: Content.Town.Auction.AuctionRoom, ):
        ...

    def Enter(self, user: AdventureBot.User.User, ) -> None:
        ...

    def OfferSelected(self, user: AdventureBot.User.User, message: AdventureBot.Messenger.ReceivedMessage, ) -> None:
        ...

    def Back(self, user: AdventureBot.User.User, message: AdventureBot.Messenger.ReceivedMessage, ) -> None:
        ...

class ItemOffer(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        self.BuyOffers: System.Collections.Generic.List[Content.Town.Auction.Offer]
        self.SellOffers: System.Collections.Generic.List[Content.Town.Auction.Offer]
        ...

    # static fields

    # properties
    # methods
    def __init__(self, sellOffers: System.Collections.Generic.List[Content.Town.Auction.Offer], buyOffers: System.Collections.Generic.List[Content.Town.Auction.Offer], ):
        ...

    def Serialize(self, ) -> AdventureBot.VariableContainer:
        ...

    def SerializeMany(self, offers: System.Collections.Generic.IEnumerable[Content.Town.Auction.Offer], ) -> AdventureBot.SerializableList:
        ...

    @staticmethod
    def Deserialize(container: AdventureBot.VariableContainer, ) -> Content.Town.Auction.ItemOffer:
        ...

    @staticmethod
    def DeserializeMany(list: AdventureBot.SerializableList, ) -> System.Collections.Generic.List[Content.Town.Auction.Offer]:
        ...

class AuctionRoom(AdventureBot.Room.IRoom, AdventureBot.Room.BetterRoom.BetterRoomBase[Content.Town.Auction.AuctionRoom]):
    @typing.overload
    def __init__(self, **kwargs):
        self._actions: System.Collections.Generic.Dictionary[System.Type, AdventureBot.Room.BetterRoom.ActionBase]
        self._rootAction: AdventureBot.Room.BetterRoom.ActionBase
        ...

    # static fields
    Id: str = ...

    # properties
    @property
    def Name(self) -> str:
        ...

    @property
    def Identifier(self) -> str:
        ...

    @property
    def actions(self) -> System.Array[System.Type]:
        ...

    @property
    def Routes(self) -> System.Array[AdventureBot.Room.MessageReceived]:
        ...
    @Routes.setter
    def Routes(self, val: System.Array[AdventureBot.Room.MessageReceived]):
        ...

    @property
    def Buttons(self) -> AdventureBot.NullableDictionary[AdventureBot.Room.MessageReceived, System.Collections.Generic.Dictionary[str, AdventureBot.Room.MessageReceived]]:
        ...
    @Buttons.setter
    def Buttons(self, val: AdventureBot.NullableDictionary[AdventureBot.Room.MessageReceived, System.Collections.Generic.Dictionary[str, AdventureBot.Room.MessageReceived]]):
        ...

    # methods
    def __init__(self, ):
        ...

    def OnEnter(self, user: AdventureBot.User.User, ) -> None:
        ...

class Math(System.Object, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    @staticmethod
    def GetPrices() -> System.Collections.Generic.IEnumerable[System.Tuple[int, int]]:
        ...

    @staticmethod
    def GetSubPrices(n: int, ) -> System.Collections.Generic.IEnumerable[int]:
        ...

    @staticmethod
    def Ending(n: int, ) -> int:
        ...

    @staticmethod
    def Step(n: int, ) -> int:
        ...

class IState(abc.ABC, typing.Generic[T]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    @abc.abstractmethod
    def StateId(self) -> str:
        ...

    # methods
    @abc.abstractmethod
    def Deserialize(self, container: AdventureBot.VariableContainer, ) -> T:
        ...

    @abc.abstractmethod
    def Serialize(self, ) -> AdventureBot.VariableContainer:
        ...

class StateContainer(System.Object, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    @staticmethod
    def Deserialize(container: AdventureBot.VariableContainer, ) -> T:
        ...

    @staticmethod
    def Serialize(state: Content.Town.Auction.IState[T], ) -> AdventureBot.VariableContainer:
        ...

class PriceGroupSelectionActionBase(AdventureBot.Room.BetterRoom.ActionBase[Content.Town.Auction.AuctionRoom], abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        self.Buttons: System.Collections.Generic.Dictionary[str, AdventureBot.Room.MessageReceived]
        self.Room: AdventureBot.Room.BetterRoom.BetterRoomBase
        ...

    # static fields

    # properties
    @property
    def Room(self) -> Content.Town.Auction.AuctionRoom:
        ...

    # methods
    def __init__(self, room: Content.Town.Auction.AuctionRoom, ):
        ...

    def Enter(self, user: AdventureBot.User.User, ) -> None:
        ...

    def Fallback(self, user: AdventureBot.User.User, message: AdventureBot.Messenger.ReceivedMessage, ) -> None:
        ...

    def Back(self, user: AdventureBot.User.User, message: AdventureBot.Messenger.ReceivedMessage, ) -> None:
        ...

class BuySellState(Content.Town.Auction.IState[Content.Town.Auction.BuySellState], System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        self.SelectedItemCount: System.Nullable[int]
        self.SelectedItemId: str
        self.SelectedItemPrice: System.Decimal
        self.Selling: bool
        ...

    # static fields

    # properties
    @property
    def StateId(self) -> str:
        ...

    # methods
    def __init__(self, ):
        ...

    def Serialize(self, ) -> AdventureBot.VariableContainer:
        ...

    def Deserialize(self, container: AdventureBot.VariableContainer, ) -> Content.Town.Auction.BuySellState:
        ...

class MyOffersActionBase(AdventureBot.Room.BetterRoom.ActionBase[Content.Town.Auction.AuctionRoom], abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        self.Buttons: System.Collections.Generic.Dictionary[str, AdventureBot.Room.MessageReceived]
        self.Room: AdventureBot.Room.BetterRoom.BetterRoomBase
        ...

    # static fields

    # properties
    @property
    def Room(self) -> Content.Town.Auction.AuctionRoom:
        ...

    # methods
    def __init__(self, room: Content.Town.Auction.AuctionRoom, ):
        ...

    def Enter(self, user: AdventureBot.User.User, ) -> None:
        ...

    def Offer(self, user: AdventureBot.User.User, message: AdventureBot.Messenger.ReceivedMessage, ) -> None:
        ...

    def CancelOffer(self, user: AdventureBot.User.User, message: AdventureBot.Messenger.ReceivedMessage, ) -> None:
        ...

    def Back(self, user: AdventureBot.User.User, message: AdventureBot.Messenger.ReceivedMessage, ) -> None:
        ...

class PriceSelectionActionBase(AdventureBot.Room.BetterRoom.ActionBase[Content.Town.Auction.AuctionRoom], abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        self.Buttons: System.Collections.Generic.Dictionary[str, AdventureBot.Room.MessageReceived]
        self.Room: AdventureBot.Room.BetterRoom.BetterRoomBase
        ...

    # static fields

    # properties
    @property
    def Room(self) -> Content.Town.Auction.AuctionRoom:
        ...

    # methods
    def __init__(self, room: Content.Town.Auction.AuctionRoom, ):
        ...

    def Enter(self, user: AdventureBot.User.User, ) -> None:
        ...

    def Fallback(self, user: AdventureBot.User.User, message: AdventureBot.Messenger.ReceivedMessage, ) -> None:
        ...

    def Back(self, user: AdventureBot.User.User, message: AdventureBot.Messenger.ReceivedMessage, ) -> None:
        ...

class ItemOffersActionBase(AdventureBot.Room.BetterRoom.ActionBase[Content.Town.Auction.AuctionRoom], abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        self.Buttons: System.Collections.Generic.Dictionary[str, AdventureBot.Room.MessageReceived]
        self.Room: AdventureBot.Room.BetterRoom.BetterRoomBase
        ...

    # static fields

    # properties
    @property
    def Room(self) -> Content.Town.Auction.AuctionRoom:
        ...

    # methods
    def __init__(self, room: Content.Town.Auction.AuctionRoom, ):
        ...

    def GetOffers(self, offers: Content.Town.Auction.Offers, state: Content.Town.Auction.BuySellState, ) -> System.ValueTuple[System.Collections.Generic.List[Content.Town.Auction.Offer], str]:
        ...

    def Enter(self, user: AdventureBot.User.User, ) -> None:
        ...

    def OfferSelected(self, user: AdventureBot.User.User, message: AdventureBot.Messenger.ReceivedMessage, ) -> None:
        ...

    @staticmethod
    def Buy(offers: System.Collections.Generic.IReadOnlyList[Content.Town.Auction.Offer], buyer: AdventureBot.User.User, count: int, ) -> int:
        ...

    def Back(self, user: AdventureBot.User.User, message: AdventureBot.Messenger.ReceivedMessage, ) -> None:
        ...

class Offers(System.Collections.Generic.IDictionary[str, Content.Town.Auction.ItemOffer], System.Collections.Generic.ICollection[System.Collections.Generic.KeyValuePair[str, Content.Town.Auction.ItemOffer]], System.Collections.Generic.IEnumerable[System.Collections.Generic.KeyValuePair[str, Content.Town.Auction.ItemOffer]], System.Collections.IEnumerable, System.Collections.IDictionary, System.Collections.ICollection, System.Collections.Generic.IReadOnlyDictionary[str, Content.Town.Auction.ItemOffer], System.Collections.Generic.IReadOnlyCollection[System.Collections.Generic.KeyValuePair[str, Content.Town.Auction.ItemOffer]], System.Runtime.Serialization.ISerializable, System.Runtime.Serialization.IDeserializationCallback, System.Collections.Generic.Dictionary[str, Content.Town.Auction.ItemOffer]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def Comparer(self) -> System.Collections.Generic.IEqualityComparer[str]:
        ...

    @property
    def Count(self) -> int:
        ...

    @property
    def Keys(self) -> System.Collections.Generic.Dictionary.KeyCollection[str, Content.Town.Auction.ItemOffer]:
        ...

    @property
    def Values(self) -> System.Collections.Generic.Dictionary.ValueCollection[str, Content.Town.Auction.ItemOffer]:
        ...

    @property
    def Item(self) -> Content.Town.Auction.ItemOffer:
        ...
    @Item.setter
    def Item(self, val: Content.Town.Auction.ItemOffer):
        ...

    # methods
    def __init__(self, ):
        ...

    def Serialize(self, ) -> AdventureBot.VariableContainer:
        ...

    @staticmethod
    def Deserialize(items: AdventureBot.VariableContainer, ) -> Content.Town.Auction.Offers:
        ...

    def Save(self, ) -> None:
        ...

    @staticmethod
    def Load() -> Content.Town.Auction.Offers:
        ...

class AllOffersActionBase(AdventureBot.Room.BetterRoom.ActionBase[Content.Town.Auction.AuctionRoom], abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        self.Buttons: System.Collections.Generic.Dictionary[str, AdventureBot.Room.MessageReceived]
        self.Room: AdventureBot.Room.BetterRoom.BetterRoomBase
        ...

    # static fields

    # properties
    @property
    def Room(self) -> Content.Town.Auction.AuctionRoom:
        ...

    # methods
    def __init__(self, room: Content.Town.Auction.AuctionRoom, ):
        ...

    @staticmethod
    def FindMinMax(offers: System.Collections.Generic.IEnumerable[Content.Town.Auction.Offer], ) -> System.Tuple[System.Decimal, System.Decimal]:
        ...

    def Enter(self, user: AdventureBot.User.User, ) -> None:
        ...

    def OfferSelected(self, user: AdventureBot.User.User, message: AdventureBot.Messenger.ReceivedMessage, ) -> None:
        ...

    def Back(self, user: AdventureBot.User.User, message: AdventureBot.Messenger.ReceivedMessage, ) -> None:
        ...

class QuantitySelectionActionBase(AdventureBot.Room.BetterRoom.ActionBase[Content.Town.Auction.AuctionRoom], abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        self.Buttons: System.Collections.Generic.Dictionary[str, AdventureBot.Room.MessageReceived]
        self.Room: AdventureBot.Room.BetterRoom.BetterRoomBase
        ...

    # static fields

    # properties
    @property
    def Room(self) -> Content.Town.Auction.AuctionRoom:
        ...

    # methods
    def __init__(self, room: Content.Town.Auction.AuctionRoom, ):
        ...

    def Enter(self, user: AdventureBot.User.User, ) -> None:
        ...

    def Fallback(self, user: AdventureBot.User.User, message: AdventureBot.Messenger.ReceivedMessage, ) -> None:
        ...

    def Back(self, user: AdventureBot.User.User, message: AdventureBot.Messenger.ReceivedMessage, ) -> None:
        ...

class Offer(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        self.Count: int
        self.Created: System.DateTimeOffset
        self.ItemId: str
        self.Price: System.Decimal
        self.UserId: AdventureBot.UserId
        ...

    # static fields

    # properties
    # methods
    def __init__(self, userId: AdventureBot.UserId, price: System.Decimal, count: int, created: System.DateTimeOffset, itemId: str, ):
        ...

    def Serialize(self, ) -> AdventureBot.VariableContainer:
        ...

    @staticmethod
    def Deserialize(container: AdventureBot.VariableContainer, ) -> Content.Town.Auction.Offer:
        ...

class AddOfferState(Content.Town.Auction.IState[Content.Town.Auction.AddOfferState], System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        self.MaxQuantityAvailable: int
        self.QuantitySelected: int
        self.SelectedItemId: str
        self.SelectedItemPrice: int
        self.SelectedPriceGroup: int
        self.Selling: bool
        ...

    # static fields

    # properties
    @property
    def StateId(self) -> str:
        ...

    # methods
    def __init__(self, ):
        ...

    def Deserialize(self, container: AdventureBot.VariableContainer, ) -> Content.Town.Auction.AddOfferState:
        ...

    def Serialize(self, ) -> AdventureBot.VariableContainer:
        ...

