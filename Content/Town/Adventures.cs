using System.Linq;
using AdventureBot.Messenger;
using AdventureBot.Room;
using AdventureBot.User;
using AdventureBot.User.Stats;

namespace Content.Town
{
    [Room("town/adventures")]
    public class Adventures : RoomBase
    {
        public override string Name => "Приключения";
        public override string Identifier => "town/adventures";

        public override void OnEnter(User user)
        {
            var roomMgr = GetAllRooms();
            var rooms = roomMgr.Items()
                .Where(room => room.Attribute is AvailableAttribute)
                .Select(room => room.Identificator)
                .DefaultIfEmpty()
                .ToList();
            user.RoomManager.Go(rooms[user.Random.Next(rooms.Count)]);
        }

        public override bool OnLeave(User user)
        {
            return true;
        }

        public override void OnMessage(User user, RecivedMessage message)
        {
            // Should not be here
            SendMessage(user, "Вы попали куда-то не туда");
            user.RoomManager.Leave();
        }

        public override void OnReturn(User user)
        {
            const decimal k = 0.2m;
            user.Info.ChangeStats(StatsProperty.Mana, user.Info.MaxStats.Effect[StatsProperty.Mana] * k);
            user.Info.ChangeStats(StatsProperty.Stamina, user.Info.MaxStats.Effect[StatsProperty.Mana] * k);
            user.Info.ChangeStats(StatsProperty.Health, user.Info.MaxStats.Effect[StatsProperty.Mana] * k);

            SendMessage(user, "Вы вернулись в город, отдохнули и теперь лучше себя чувствуете.");
            user.RoomManager.Leave();
        }
    }
}