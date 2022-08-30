from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import AdventureBot
import System


class String(AdventureBot.ISerializable, System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    # methods
    @typing.overload
    def __init__(self, value: System.String, ):
        ...

class Int(AdventureBot.ISerializable, System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    # methods
    @typing.overload
    def __init__(self, value: System.Int32, ):
        ...

class Long(AdventureBot.ISerializable, System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    # methods
    @typing.overload
    def __init__(self, value: System.Int64, ):
        ...

class Double(AdventureBot.ISerializable, System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    # methods
    @typing.overload
    def __init__(self, value: System.Double, ):
        ...

class Decimal(AdventureBot.ISerializable, System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    # methods
    @typing.overload
    def __init__(self, value: System.Decimal, ):
        ...

class Bool(AdventureBot.ISerializable, System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    # methods
    @typing.overload
    def __init__(self, value: System.Boolean, ):
        ...

