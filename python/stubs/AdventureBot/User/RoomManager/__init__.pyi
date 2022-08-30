from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import System
import AdventureBot.User
import AdventureBot.Messenger


class StackedRoom(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        self.Identifier: System.String
        self.ShownStats: AdventureBot.User.ShownStats
        self.LastMessage: AdventureBot.Messenger.SentMessage
        ...

    # properties
    # methods
    @typing.overload
    def __init__(self, identifier: System.String, shownStats: AdventureBot.User.ShownStats, lastMessage: AdventureBot.Messenger.SentMessage, ):
        ...

    @typing.overload
    def __init__(self, identifier: System.String, ):
        ...

