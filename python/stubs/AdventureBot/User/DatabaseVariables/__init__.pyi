from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import System
import Microsoft.Data.Sqlite
import AdventureBot.User.DatabaseVariables


class Deserializer(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    # methods
    @typing.overload
    @staticmethod
    def Create(reader: Microsoft.Data.Sqlite.SqliteDataReader, ) -> AdventureBot.User.DatabaseVariables.Deserializer:
        ...

