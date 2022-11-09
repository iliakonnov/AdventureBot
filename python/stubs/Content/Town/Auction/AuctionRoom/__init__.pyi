from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import Content.Town.Auction
import System.Collections.Generic
import AdventureBot.Room
import AdventureBot.Room.BetterRoom
import AdventureBot.User
import AdventureBot.Messenger


class AllOffersAction(Content.Town.Auction.AllOffersActionBase):
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

class PriceGroupSelectionAction(Content.Town.Auction.PriceGroupSelectionActionBase):
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

class MyOffersAction(Content.Town.Auction.MyOffersActionBase):
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

class RemoveOfferAction(Content.Town.Auction.RemoveOfferActionBase):
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

class MainAction(AdventureBot.Room.BetterRoom.ActionBase[Content.Town.Auction.AuctionRoom]):
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

    def ShowOffers(self, user: AdventureBot.User.User, message: AdventureBot.Messenger.ReceivedMessage, ) -> None:
        ...

    def MyOffers(self, user: AdventureBot.User.User, message: AdventureBot.Messenger.ReceivedMessage, ) -> None:
        ...

    def Exit(self, user: AdventureBot.User.User, message: AdventureBot.Messenger.ReceivedMessage, ) -> None:
        ...

class AddOfferAction(Content.Town.Auction.AddOfferActionBase):
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

class QuantitySelectionAction(Content.Town.Auction.QuantitySelectionActionBase):
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

class PriceSelectionAction(Content.Town.Auction.PriceSelectionActionBase):
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

class ItemOffersAction(Content.Town.Auction.ItemOffersActionBase):
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

