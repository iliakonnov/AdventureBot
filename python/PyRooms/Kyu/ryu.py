import attributes
import clrtype

import System
from AdventureBot.Item import ItemInfo
from AdventureBot.Messenger import ReceivedMessage
from AdventureBot.Room import Difficulity
from AdventureBot.Room.BetterRoom import BetterRoomBase, ActionBase
from AdventureBot.User import User
import Content
from AdventureBot.User.Stats import StatsProperty


class Ryu(BetterRoomBase, metaclass=clrtype.ClrClass):
    __metaclass__ = clrtype.ClrClass
    _clrclassattribs = [attributes.Room.Available("room/ryu", Difficulity.Hard, Content.TownRoot.Id)]

    class Question(ActionBase, metaclass=clrtype.ClrClass):
        __metaclass__ = clrtype.ClrClass
        _clrclassattribs = [attributes.Room.BetterRoom.Action()]

        @attributes.Room.BetterRoom.Button("Вызвать на поединок")
        def Battle(self, user: User, message: ReceivedMessage) -> None:
            user.RoomManager.Go("ryu/battle")

        @attributes.Room.BetterRoom.Button("Возьмешь меня в свои ученики?")
        def Learn(self, user: User, message: ReceivedMessage) -> None:
            if user.ItemManager.Get("ryu/hadoken") is not None:
                self.Room.SendMessage(user, "Ты и так обучен.", self.Room.GetButtons(user))
                return

            self.Room.SwitchAction(user, Ryu.LearnAction)
            self.Room.SendMessage(user,
                                  "— Тебе придется работать день и ночь, пройти через огонь, воду и медные трубы, но результат тебя удивит. Ты готов?",
                                  self.Room.GetButtons(user))

    class LearnAction(ActionBase, metaclass=clrtype.ClrClass):
        __metaclass__ = clrtype.ClrClass
        _clrclassattribs = [attributes.Room.BetterRoom.Action(0)]

        @attributes.Room.BetterRoom.Button("Да")
        def Yes(self, user: User, message: ReceivedMessage) -> None:
            user.Info.ChangeStats(StatsProperty.Stamina, 0.0, True)
            self.Room.SendMessage(user,
                                  "После недели упорных тренировок ты очень устал, зато научился создавать сгусток из своей ки и запускать его в противника. Хадокен!")
            user.ItemManager.Add(ItemInfo("ryu/hadoken", 1))
            user.RoomManager.Leave()

        @attributes.Room.BetterRoom.Button("Нет")
        def No(self, user: User, message: ReceivedMessage) -> None:
            user.Info.MakeDamage(15.0)
            self.Room.SendMessage(user, "— Слабак! — после этих слов он ударом ноги отправил тебя обратно в город.")
            user.RoomManager.Leave()

    actions = System.Array[System.Type]([Question, LearnAction])

    @property
    def Name(self) -> str:
        return "Рю"

    @property
    def Identifier(self) -> str:
        return "room/ryu"

    def OnEnter(self, user: User) -> None:
        super().OnEnter(user)
        self.SwitchAction(user, self.Question)
        self.SendMessage(user,
                         "Перед тобой стоит мускулистый азиат в кимоно без рукавов и красной головной повязке. "
                         "Кажется, этому парню уступил бы даже твой тренер.",
                         self.GetButtons(user))
