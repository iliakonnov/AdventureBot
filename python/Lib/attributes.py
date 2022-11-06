import clrtype


class ObjectManager:
    import AdventureBot.ObjectManager
    GameObject = clrtype.attribute(AdventureBot.ObjectManager.GameObjectAttribute)
    Identifiable = clrtype.attribute(AdventureBot.ObjectManager.IdentifiableAttribute)
    Item = clrtype.attribute(AdventureBot.ObjectManager.ItemAttribute)
    Messenger = clrtype.attribute(AdventureBot.ObjectManager.MessengerAttribute)


class Quest:
    import AdventureBot.Quest
    Quest = clrtype.attribute(AdventureBot.Quest.QuestAttribute)


class Room:
    import AdventureBot.Room
    Root = clrtype.attribute(AdventureBot.Room.RootAttribute)
    Room = clrtype.attribute(AdventureBot.Room.RoomAttribute)
    Available = clrtype.attribute(AdventureBot.Room.AvailableAttribute)

    class BetterRoom:
        import AdventureBot.Room.BetterRoom
        Action = clrtype.attribute(AdventureBot.Room.BetterRoom.ActionAttribute)
        MessageHandler = clrtype.attribute(AdventureBot.Room.BetterRoom.MessageHandlerAttribute)
        Button = clrtype.attribute(AdventureBot.Room.BetterRoom.ButtonAttribute)
        Fallback = clrtype.attribute(AdventureBot.Room.BetterRoom.FallbackAttribute)


class UserManager:
    import AdventureBot.UserManager
    Migrator = clrtype.attribute(AdventureBot.UserManager.MigratorAttribute)
