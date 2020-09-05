using AdventureBot;
using AdventureBot.Messenger;
using AdventureBot.User;

namespace Content.Rooms.MegaMonster.Room
{
    public partial class MegaMonsterRoom
    {
        private void Gold(User user)
        {
            using (var stats = new StatsContext(user.Random, GetRoomVariables(user)))
            {
                if (user.Info.Gold >= stats.Stats.Gold)
                {
                    SwitchAction(user, GiveGold);
                }
                else
                {
                    SwitchAction(user, NotEnoughGold);
                }

                SendMessage(user,
                    $"Монстр желает заполучить {stats.Stats.Gold.Format()} золота. Готовы попрощаться с деньгами?",
                    GetButtons(user));
            }
        }

        private void GiveGold(User user, ReceivedMessage message)
        {
            HandleButtonAlways(user, message);
        }

        private void NotEnoughGold(User user, ReceivedMessage message)
        {
            HandleButtonAlways(user, message);
        }

        private void ConfirmGiveGold(User user)
        {
            using (var stats = new StatsContext(user.Random, GetRoomVariables(user)))
            {
                if (user.Info.TryDecreaseGold(stats.Stats.Gold))
                {
                    user.RoomManager.Leave();
                }
            }
        }
    }
}