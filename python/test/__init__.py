import AdventureBot.Room
import System


class Root(AdventureBot.Room.IRoot):
    __attrs__ = [AdventureBot.Room.RootAttribute("root/town")]

    @property
    def Identifier(self) -> System.String:
        return "root/town"

    @property
    def RootRoomId(self) -> System.String:
        return "monster/foo"


class Monster(AdventureBot.Room.MonsterBase):
    __attrs__ = [AdventureBot.Room.AvailableAttribute("monster/foo", AdventureBot.Room.Difficulity.Easy, "root/town")]

    @property
    def Health(self) -> System.Decimal:
        return 100

    @property
    def Name(self) -> System.String:
        return "TestPy"

    @property
    def Identifier(self) -> System.String:
        return "monster/foo"

    def Enter(self, user, buttons):
        pass

    def OnRunaway(self, user):
        return True

    def OnWon(self, user):
        pass

    def GetDamage(self, user):
        return 10