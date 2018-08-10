﻿using System;
using AdventureBot.Messenger;
using AdventureBot.User;
using AdventureBot.User.Stats;

namespace Content.Rooms.MegaMonster.Room
{
    public partial class MegaMonsterRoom
    {
        private void Knowledge(User user)
        {
            using (var stats = new StatsContext(user.Random, GetRoomVariables(user)))
            {
                var canLearn = false;
                string message;
                switch (stats.Stats.KnowledgeGroup)
                {
                    case MegaMonster.Knowledge.Strength:
                        if (user.Info.CurrentStats.Effect[StatsProperty.Strength] >= stats.Stats.KnowledgeMinimal
                            && user.Info.CurrentStats.Effect[StatsProperty.Stamina] >= stats.Stats.KnowledgeRequired)
                        {
                            canLearn = true;
                            SwitchAction(user, GiveKnowledge);
                        }

                        message =
                            $"Монстр желает научиться спорту. Для этого необходимо минимум {stats.Stats.KnowledgeMinimal:0.##} силы и {stats.Stats.KnowledgeRequired:0.##} сил";

                        break;
                    case MegaMonster.Knowledge.Intelligence:
                        if (user.Info.CurrentStats.Effect[StatsProperty.Intelligence] >= stats.Stats.KnowledgeMinimal
                            && user.Info.CurrentStats.Effect[StatsProperty.Mana] >= stats.Stats.KnowledgeRequired)
                        {
                            canLearn = true;
                            SwitchAction(user, GiveKnowledge);
                        }

                        message =
                            $"Монстр желает научиться магии. Для этого необходимо минимум {stats.Stats.KnowledgeMinimal:0.##} интеллекта и {stats.Stats.KnowledgeRequired:0.##} маны";
                        break;
                    default:
                        throw new ArgumentOutOfRangeException();
                }

                if (canLearn)
                {
                    SwitchAction(user, GiveKnowledge);
                }
                else
                {
                    SwitchAction(user, NotEnoughKnowledge);
                }

                SendMessage(user, message, GetButtons(user));
            }
        }

        private void GiveKnowledge(User user, RecivedMessage message)
        {
            HandleButtonAlways(user, message);
        }

        private void NotEnoughKnowledge(User user, RecivedMessage message)
        {
            HandleButtonAlways(user, message);
        }

        private void ConfirmGiveKnowledge(User user)
        {
            using (var stats = new StatsContext(user.Random, GetRoomVariables(user)))
            {
                StatsProperty prop;
                switch (stats.Stats.KnowledgeGroup)
                {
                    case MegaMonster.Knowledge.Strength:
                        prop = StatsProperty.Stamina;
                        break;
                    case MegaMonster.Knowledge.Intelligence:
                        prop = StatsProperty.Mana;
                        break;
                    default:
                        throw new ArgumentOutOfRangeException();
                }

                if (user.Info.ChangeStats(prop, -stats.Stats.KnowledgeRequired))
                {
                    user.RoomManager.Leave();
                }
            }
        }
    }
}