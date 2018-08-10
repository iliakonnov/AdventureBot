using AdventureBot.Item;
using AdventureBot.Messenger;
using AdventureBot.User;

namespace Content.Rooms.MegaMonster.Room
{
    public partial class MegaMonsterRoom
    {
        private void Artifact(User user)
        {
            using (var stats = new StatsContext(user.Random, GetRoomVariables(user)))
            {
                if (stats.Stats.ArtifactId == null)
                {
                    SendMessage(user, "Монстру не нужны твои артефакты, людишка!");
                    BeginTalk(user);
                    return;
                }
                
                var item = GetAllItems().Get(stats.Stats.ArtifactId);
                if (user.ItemManager.Get(stats.Stats.ArtifactId) != null)
                {
                    SwitchAction(user, GiveArtifact);
                }
                else
                {
                    SwitchAction(user, ArtifactNotFound);
                }
                SendMessage(user, $"Монстр желает заполучить {item?.Name}. Готовы его отдать?", GetButtons(user));
            }
        }

        private void GiveArtifact(User user, RecivedMessage message)
        {
            HandleButtonAlways(user, message);
        }
        
        private void ArtifactNotFound(User user, RecivedMessage message)
        {
            HandleButtonAlways(user, message);
        }

        private void ConfirmGiveArtifact(User user)
        {
            using (var stats = new StatsContext(user.Random, GetRoomVariables(user)))
            {
                if (user.ItemManager.Remove(new ItemInfo(stats.Stats.ArtifactId, 1)))
                {
                    user.RoomManager.Leave();
                }
            }
        }
    }
}