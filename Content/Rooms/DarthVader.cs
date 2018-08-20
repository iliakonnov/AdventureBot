using System;
using System.Collections.Generic;
using AdventureBot;
using AdventureBot.Item;
using AdventureBot.Messenger;
using AdventureBot.Room;
using AdventureBot.User;
using Content.Items;

namespace Content.Rooms
{
    [Available(Id, Difficulity.Hard)]
    public class DarthVader : RoomBase
    {
        public const string Id = "monster/vader";

        public DarthVader()
        {
            Routes = new MessageRecived[] {PreBattle, Battle};
            Buttons = new NullableDictionary<MessageRecived, Dictionary<string, MessageRecived>>
            {
                {
                    null, new Dictionary<string, MessageRecived>
                    {
                        {
                            "— НЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕТ!", (user, message) =>
                            {
                                SwitchAction(user, PreBattle);
                                user.Info.MakeDamage(15);
                                SendMessage(user, "Тебе отрубили руку. А теперь хорош рыдать и в бой.",
                                    GetButtons(user));
                            }
                        }
                    }
                },
                {
                    PreBattle, new Dictionary<string, MessageRecived>
                    {
                        {
                            "Достать оружие", (user, message) =>
                            {
                                SendMessage(user, "<b>щелк</b>");
                                user.RoomManager.Go(VaderBattle.Id);
                            }
                        }
                    }
                }
            };
        }

        public override string Name => "Дарт Вейдер";
        public override string Identifier => Id;

        public override void OnEnter(User user)
        {
            base.OnEnter(user);

            SendMessage(user,
                "Перед вами предстал крупный мужчина в черной блестящей респираторной маске и темном матовом плаще.");
            SendMessage(user, "— Я твой отец!", GetButtons(user));
        }

        public override void OnMessage(User user, RecivedMessage message)
        {
            if (!HandleAction(user, message))
            {
                HandleButtonAlways(user, message);
            }
        }

        private void PreBattle(User user, RecivedMessage message)
        {
            HandleButtonAlways(user, message);
        }

        private void Battle(User user, RecivedMessage message)
        {
            // For old users
            user.RoomManager.Go(VaderBattle.Id);
        }
    }
    
    [Room(Id)]
    public class VaderBattle : MonsterBase
    {
        public const string Id = "monster/vader/battle";
        public override string Name => "Отец";
        public override string Identifier => Id;
        protected override decimal Health => 550;

        protected override decimal GetDamage(User user)
        {
            return 40;
        }

        protected override void Enter(User user, string[][] buttons)
        {
            SendMessage(user, "Световой меч озарил все вокруг своим кроваво-красным светом.", buttons);
        }

        protected override bool OnRunaway(User user)
        {
            return true;
        }

        protected override void OnWon(User user)
        {
            var rand = user.Random.Next(3);
            switch (rand)
            {
                case 0:
                    user.ItemManager.Add(new ItemInfo(VaderRespirator.Id, 1));
                    break;
                case 1:
                    user.ItemManager.Add(new ItemInfo(VaderSword.Id, 1));
                    break;
                case 2:
                    user.ItemManager.Add(new ItemInfo(VaderCloak.Id, 1));
                    break;
                default:
                    throw new ArgumentOutOfRangeException(nameof(rand), rand, "rand > 2 || rand < 0");
            }
        }
    }
}