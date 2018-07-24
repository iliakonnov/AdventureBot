from AdventureBot.ObjectManager import GameObjectAttribute
from AdventureBot.Room import RoomBase, AvailableAttribute, Difficulity
from System import Tuple, Type
import imp

def load_module(module):
    # converts raw python module to c# class

    class Result(RoomBase):
        def __init__(self):
            module.blockly_helper.room = self
            if hasattr(module, 'OnLeave'):
                self.onLeave = module.OnLeave
            else:
                self.onLeave = None

        def get_Name(self):
            return module.Name

        def get_Identifier(self):
            return module.Identifier

        def OnEnter(self, user):
            return module.OnEnter(user)

        def OnReturn(self, user):
            return module.OnReturn(user)

        def OnMessage(self, user, message):
            return module.OnMessage(user, message)

        def OnLeave(self, user):
            if self.onLeave is None:
                return super(Result, self).OnLeave(user)
            else:
                return self.onLeave(user)

    return Tuple[GameObjectAttribute, Type, type](
        AvailableAttribute(module.Identifier, Difficulity.Any),
        Result,
        Result
    )


def load_path(path):
    module = imp.load_source('pyRoom', path)
    return load_module(module)
