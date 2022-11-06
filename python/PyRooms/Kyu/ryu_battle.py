import System
import attributes
import clrtype
import clr
from AdventureBot.Item import ItemInfo
from AdventureBot.Room import MonsterBase
from AdventureBot.User import User


class RyuBattle(MonsterBase, metaclass=clrtype.ClrClass):
    __metaclass__ = clrtype.ClrClass
    _clrclassattribs = [attributes.Room.Room("ryu/battle")]

    @property
    def Name(self) -> str:
        return "Битва"

    @property
    def Identifier(self) -> str:
        return "ryu/battle"

    @property
    def Health(self) -> System.Decimal:
        return 2000.0

    @property
    def GetDamage(self) -> System.Decimal:
        return 90.0

    def Enter(self, user: User, buttons: System.Array[System.Array[str]]):
        self.SendMessage(user, 'Голос из ниоткуда прокричал "FIGHT!"', buttons)

    def OnRunaway(self, user: User) -> bool:
        return True

    def OnWon(self, user: User):
        user.ItemManager.Add(ItemInfo("ryu/red_bandage", 1))
