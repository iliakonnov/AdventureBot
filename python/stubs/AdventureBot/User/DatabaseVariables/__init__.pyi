from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import System
import Microsoft.Data.Sqlite
import AdventureBot.User.DatabaseVariables
import System.Data
import AdventureBot.User


class Deserializer(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    def __init__(self, ):
        ...

    @staticmethod
    def Create(reader: Microsoft.Data.Sqlite.SqliteDataReader, ) -> AdventureBot.User.DatabaseVariables.Deserializer:
        ...

    def Deserialize(self, reader: System.Data.IDataRecord, ) -> AdventureBot.User.DatabaseVariables:
        ...

