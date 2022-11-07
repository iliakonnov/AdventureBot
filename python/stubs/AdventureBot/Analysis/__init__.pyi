from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import System
import AdventureBot.User
import AdventureBot.Messenger


class Events(System.Object, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    @staticmethod
    def Start() -> None:
        ...

    @staticmethod
    def Log(message: str, eventName: str, user: AdventureBot.User.User, parameters: System.Array[System.Object], ) -> None:
        ...

    @staticmethod
    def Go(user: AdventureBot.User.User, identificator: str, ) -> None:
        ...

    @staticmethod
    def Reset(user: AdventureBot.User.User, ) -> None:
        ...

    @staticmethod
    def Dead(user: AdventureBot.User.User, ) -> None:
        ...

    @staticmethod
    def Received(user: AdventureBot.User.User, message: AdventureBot.Messenger.ReceivedMessage, ) -> None:
        ...

    @staticmethod
    def Sent(user: AdventureBot.User.User, message: System.Tuple[AdventureBot.Messenger.SentMessage, AdventureBot.Messenger.ReceivedMessage], ) -> None:
        ...

