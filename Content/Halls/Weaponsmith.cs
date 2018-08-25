using System.Collections.Generic;
using System.Linq;
using System.Text;
using AdventureBot.Item;
using AdventureBot.Messenger;
using AdventureBot.Room;
using AdventureBot.Room.BetterRoom;
using AdventureBot.User;
using AdventureBot.User.Stats;
using Content.Halls.Items;
using Content.Town;

namespace Content.Halls
{
    [Available(Id, Difficulity.Any, HallsRoot.Id)]
    public class Weaponsmith : BetterRoomBase<Weaponsmith>
    {
        public const string Id = "halls/weaponsmith";

        private static readonly Recipe[] Recipes =
        {
            new Recipe(600, Revolver.Id, new Dictionary<string, int>
            {
                {FallenAngelShard.Id, 20},
                {DemonicEssence.Id, 5}
            }),
            new Recipe(100, DemonSlayer.Id, new Dictionary<string, int>
            {
                {ObsidianPlate.Id, 15},
                {DemonicEssence.Id, 15},
                {OutcastChain.Id, 1}
            }),
            new Recipe(1500, FighterArmor.Id, new Dictionary<string, int>
            {
                {FallenAngelShard.Id, 50},
                {ObsidianPlate.Id, 20},
                {DemonicEssence.Id, 20},
                {OutcastChain.Id, 5}
            }),
        };

        private static readonly string[] Stock =
        {
            HolyBullet.Id,
            BottleOfLight.Id,
            NativeCross.Id,
            HolyBomb.Id
        };

        public override string Name => "Оружейник";
        public override string Identifier => Id;

        public override void OnEnter(User user)
        {
            SwitchAction<MainAction>(user);
            user.MessageManager.ShownStats = ShownStats.Health | ShownStats.Gold;
            SendMessage(user,
                "Бродя по окрестностям, ты наткнулся на ветхую мастерскую, однако ничуть не заброшенную, как все остальные одинокие строения в этих местах. Из дымохода валил густой дым, молот со звоном падал на наковальню. Дверь мастерской отворилась, и из хижины вышел огромный бородатый мужчина средних лет, опоясанный кожаным фартуком. Одна его рука сжимала рукоять молота, а другая утирала пот с лица.");
            SendMessage(user,
                "— Добро пожаловать в мастерскую Хеймлока! Как ты уже понял, Хеймлок - это я, но мне привычнее прозвище «Оружейник». Я застрял в этой дыре надолго, так что я помогаю странникам вроде тебя выжить в Чертогах. Могу и тебе что-нибудь предложить, если есть чем расплатиться.",
                GetButtons(user));
        }

        public override void OnReturn(User user)
        {
            SendMessage(user, "Так что?", GetButtons(user));
        }

        public string[][] GetWeapons()
        {
            var itemManager = GetAllItems();
            return new[] {"Ничего"}
                .Concat(Recipes.Select(recipe => itemManager.Get(recipe.Output)?.Name))
                .Where(i => i != null)
                .Select(i => new[] {i})
                .ToArray();
        }

        public string[][] GetStock()
        {
            var itemManager = GetAllItems();
            return new[] {"Ничего"}
                .Concat(Stock.Select(id => itemManager.Get(id)?.Name))
                .Where(i => i != null)
                .Select(i => new[] {i})
                .ToArray();
        }

        [Action]
        public class MainAction : ActionBase<Weaponsmith>
        {
            public MainAction(Weaponsmith room) : base(room)
            {
            }

            [Button("Покажи, что у тебя есть")]
            public void Stock(User user, RecivedMessage message)
            {
                Room.SwitchAction<BuyOther>(user);
                Room.SendMessage(user, "— Ассортимент небольшой, зато какой качественный!");
                var itemManager = GetAllItems();
                var buttons = Room.GetStock();
                foreach (var id in Weaponsmith.Stock)
                {
                    var item = itemManager.Get(id);
                    if (item == null)
                    {
                        continue;
                    }

                    Room.SendMessage(user, $"{item.Name} за {item.Price} монет", buttons);
                }
            }

            [Button("Мне нужно мощное оружие")]
            public void Weapon(User user, RecivedMessage message)
            {
                Room.SwitchAction<BuyWeapon>(user);
                Room.SendMessage(user,
                    "— Э-хе-хе, да это же полноценный заказ! Если ты принесешь мне необходимые ресурсы и немного золота за работу, то я смогу выковать что-нибудь из этого:");
                var buttons = Room.GetWeapons();
                var itemManager = GetAllItems();
                foreach (var recipe in Recipes)
                {
                    var requirements = new List<string>();
                    foreach (var kv in recipe.Input)
                    {
                        requirements.Add($"{itemManager.Get(kv.Key)?.Name} (x{kv.Value})");
                    }

                    Room.SendMessage(user,
                        $"{itemManager.Get(recipe.Output)?.Name} за {recipe.Gold} золота\nТребуется: {string.Join(", ", requirements)}",
                        buttons);
                }
            }

            [Button("Мне нужно перераспределить предметы")]
            public void MirrorAction(User user, RecivedMessage message)
            {
                Room.SendMessage(user, "— В мастерской есть зеркало. Чувствуй себя как дома.");
                user.RoomManager.Go(Mirror.Id);
            }

            [Button("Как отсюда выбраться?!")]
            public void LeaveHalls(User user, RecivedMessage message)
            {
                Room.SendMessage(user, "Оружейник ударил по вам своим молотом и...");
                user.Info.ChangeStats(StatsProperty.Health, 1, true);
                if (user.Random.NextDouble() < 0.05) // 5%
                {
                    Room.SendMessage(user, "... и вы чуть не умерли");
                    user.RoomManager.Leave();
                }
                else
                {
                    Room.SendMessage(user, "... и вы перенеслись в Город!");
                    user.RoomManager.ChangeRoot(TownRoot.Id);
                }
            }

            [Button("Нет, мне нужно идти")]
            public void Leave(User user, RecivedMessage message)
            {
                user.RoomManager.Leave();
            }
        }

        [Action(0)]
        public class BuyWeapon : ActionBase<Weaponsmith>
        {
            public BuyWeapon(Weaponsmith room) : base(room)
            {
            }

            [Button("Ничего")]
            public void Nothing(User user, RecivedMessage message)
            {
                Room.SwitchAction<MainAction>(user);
                Room.SendMessage(user, "Ладно, если что обращайся", Room.GetButtons(user));
            }

            [Fallback]
            public void HandleButton(User user, RecivedMessage message)
            {
                var itemManager = GetAllItems();
                var weapon = Recipes.FirstOrDefault(recipe => itemManager.Get(recipe.Output)?.Name == message.Text);

                if (weapon == null)
                {
                    Room.SendMessage(user, "Даже у меня такого нет!", Room.GetWeapons());
                    return;
                }

                if (!user.Info.TryDecreaseGold(weapon.Gold))
                {
                    Room.SendMessage(user, "Сначала денег подкопи, а потом уже и приходи", Room.GetWeapons());
                    return;
                }

                var canUse = true;
                foreach (var kv in weapon.Input)
                {
                    var item = user.ItemManager.Get(kv.Key);
                    if (item == null || item.Count < kv.Value)
                    {
                        canUse = false;
                        break;
                    }
                }

                if (!canUse)
                {
                    Room.SendMessage(user, "У тебя не хватает материалов для изготовления. Приходи, когда соберешь",
                        Room.GetWeapons());
                    return;
                }

                foreach (var kv in weapon.Input)
                {
                    if (!user.ItemManager.Remove(new ItemInfo(kv.Key, kv.Value)))
                    {
                        Room.SendMessage(user, "Упс, что-то пошло не так и часть материалов испортилась",
                            Room.GetWeapons());
                        return;
                    }
                }

                var output = GetAllItems().Get(weapon.Output);
                user.ItemManager.Add(new ItemInfo(weapon.Output, 1));
                Room.SwitchAction<MainAction>(user);
                Room.SendMessage(user,
                    $"Забрав нужные ресурсы, Оружейник уходит в мастерскую. Через час усердной работы Оружейник выносит еще теплый {output?.Name}.");
                Room.SendMessage(user, "— Держи, странник. Надеюсь это поможет тебе выжить в этой дыре",
                    Room.GetButtons(user));
            }
        }

        [Action(1)]
        public class BuyOther : ActionBase<Weaponsmith>
        {
            public BuyOther(Weaponsmith room) : base(room)
            {
            }

            [Button("Ничего")]
            public void Nothing(User user, RecivedMessage message)
            {
                Room.SwitchAction<MainAction>(user);
                Room.SendMessage(user, "Ладно, если что обращайся", Room.GetButtons(user));
            }

            [Fallback]
            public void HandleButton(User user, RecivedMessage message)
            {
                var itemManager = GetAllItems();
                var item = Stock
                    .Select(id => itemManager.Get(id))
                    .FirstOrDefault(i => i?.Name == message.Text);

                if (item == null)
                {
                    Room.SendMessage(user, "Даже у меня такого нет!", Room.GetStock());
                    return;
                }

                if (item.Price == null)
                {
                    Room.SendMessage(user, "Не продается!", Room.GetStock());
                    return;
                }

                if (!user.Info.TryDecreaseGold((decimal) item.Price))
                {
                    Room.SendMessage(user, "Сначала денег подкопи, а потом уже и приходи", Room.GetStock());
                    return;
                }

                user.ItemManager.Add(new ItemInfo(item.Identifier, 1));
                Room.SwitchAction<MainAction>(user);
                Room.SendMessage(user, "Отличная покупка!", Room.GetButtons(user));
            }
        }
    }
}