import typing

T = typing.TypeVar('T')

class ref(typing.Generic[T]):
    def __init__(self, val: T):
        self.val = val

class ptr(typing.Generic[T]):
    def __init__(self, val: T):
        self.val = val
