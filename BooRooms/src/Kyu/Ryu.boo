namespace BooRooms.Kyu

import System.Linq
import AdventureBot.Messenger from AdventureBot
import AdventureBot.Room from AdventureBot
import AdventureBot.Room.BetterRoom from AdventureBot
import AdventureBot.Item from AdventureBot
import AdventureBot.User from AdventureBot

[Available("room/ryu", Difficulity.Hard)]
class Ryu(BetterRoomBase):
    public Name as string:
        get:
            return "Рю"

    public Identifier as string:
        get:
            return "room/ryu"

    public def constructor():
        super(typeof(Ryu))

    public override def OnEnter(user as User):
        super(user)
        SwitchAction(user, typeof(Question))
        buttons = GetButtons(user)
        /*if user.ItemManager.Get("ryu/hadoken") != null:
            buttons = buttons.Where({row | row.FirstOrDefault() != "Возьмешь меня в свои ученики?"}).ToArray()*/
        SendMessage(user,
            "Перед тобой стоит мускулистый азиат в кимоно без рукавов и красной головной повязке. Кажется, этому парню уступил бы даже твой тренер.",
            buttons)

    [Action]
    public class Question(ActionBase):
        public def constructor(room as BetterRoomBase):
            super(room)

        [Button("Вызвать на поединок")]
        public def Battle(user as User, message as RecivedMessage):
            user.RoomManager.Go("ryu/battle")

        [Button("Возьмешь меня в свои ученики?")]
        public def Learn(user as User, message as RecivedMessage):
            if user.ItemManager.Get("ryu/hadoken") != null:
                Room.SendMessage(user, "Ты и так обучен.", Room.GetButtons(user))
                return

            Room.SwitchAction(user, typeof(LearnAction))
            Room.SendMessage(user,
                "— Тебе придется работать день и ночь, пройти через огонь, воду и медные трубы, но результат тебя удивит. Ты готов?",
                Room.GetButtons(user))

    [Action(0)]
    public class LearnAction(ActionBase):
        public def constructor(room as BetterRoomBase):
            super(room)

        [Button("Да")]
        public def Yes(user as User, message as RecivedMessage):
            user.Info.ChangeStats(Stats.StatsProperty.Stamina, 0, true)
            Room.SendMessage(user,
                "После недели упорных тренировок ты очень устал, зато научился создавать сгусток из своей ки и запускать его в противника. Хадокен!")
            user.ItemManager.Add(ItemInfo("ryu/hadoken", 1))
            user.RoomManager.Leave()

        [Button("Нет")]
        public def No(user as User, message as RecivedMessage):
            user.Info.MakeDamage(15)
            Room.SendMessage(user, "— Слабак! — после этих слов он ударом ноги отправил тебя обратно в город.")
            Room.SendMessage(user, "— Эмм, я пожалуй пойду обратно в город...")
            Room.SendMessage(user, "— Передай привет моему другу Кену, если встретишь его по пути.")
            user.RoomManager.Leave()
