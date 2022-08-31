import AdventureBot.Room
import System

import clrtype


@AdventureBot.Room.RootAttribute("root/town")
class Root(AdventureBot.Room.IRoot):
    @property
    def Identifier(self) -> System.String:
        return "root/town"

    @property
    def RootRoomId(self) -> System.String:
        return "monster/foo"


@AdventureBot.Room.AvailableAttribute("monster/foo", AdventureBot.Room.Difficulity.Easy, "root/town")
class Monster(AdventureBot.Room.MonsterBase):
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