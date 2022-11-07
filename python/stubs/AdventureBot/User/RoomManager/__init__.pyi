from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import System
import AdventureBot.Messenger


class StackedRoom(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        self.Identifier: str
        self.ShownStats: int
        self.LastMessage: AdventureBot.Messenger.SentMessage
        ...

    # static fields

    # properties
    # methods
    @typing.overload
    def __init__(self, identifier: str, shownStats: int, lastMessage: AdventureBot.Messenger.SentMessage, ):
        ...

    @typing.overload
    def __init__(self, identifier: str, ):
        ...

