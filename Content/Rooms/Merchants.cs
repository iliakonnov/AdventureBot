using System.Collections.Generic;
using System.Linq;
using AdventureBot;
using AdventureBot.Item;
using AdventureBot.Messenger;
using AdventureBot.Room;
using AdventureBot.User;
using AdventureBot.User.Stats;
using Content.Town;

namespace Content.Rooms
{
    [Available(Id, Difficulity.Any, TownRoot.Id)]
    public class Merchants : RoomBase
    {
        private const int ItemCount = 3;
        public const string Id = "room/merchants";

        public Merchants()
        {
            Routes = new MessageReceived[] {Shop, Shop2, Pay};
            Buttons = new NullableDictionary<MessageReceived, Dictionary<string, MessageReceived>>
            {
                {
                    null, new Dictionary<string, MessageReceived>
                    {
                        {
                            "Закупиться", (user, message) =>
                            {
                                if (!Nothing(user))
                                {
                                    return;
                                }

                                SwitchAction(user, Shop);
                                HandleAction(user, message);
                            }
                        },
                        {
                            "Ограбить", (user, message) =>
                            {
                                if (!Nothing(user))
                                {
                                    return;
                                }

                                SendMessage(user,
                                    "Несмотря на их натренированные языки, сами купцы были довольно хилыми даже по твоим меркам. Поэтому на каждое из этих слащавых лиц пришлось всего по одному удару. Ты заработал немного монет и мое личное неуважение.");
                                var gold = user.Random.Next(500, 850);
                                user.Info.Gold += gold;
                                user.Info.ChangeStats(StatsProperty.Karma, -5);
                                user.VariableManager.UserVariables.Set("merchants_disabled",
                                    new Serializable.Decimal(gold));
                                user.RoomManager.Leave();
                            }
                        },
                        {
                            "Уйти", (user, message) => user.RoomManager.Leave()
                        }
                    }
                },
                {
                    Pay, new Dictionary<string, MessageReceived>
                    {
                        {
                            "Да", (user, message) =>
                            {
                                var paySize = (user.VariableManager.UserVariables
                                                   .Get<Serializable.Decimal>("merchants_disabled") ?? 0M
                                              ) * 1.3M;
                                if (user.Info.TryDecreaseGold(paySize))
                                {
                                    SendMessage(user, "Отлично! Теперь торговцы могут торговать дальше.");
                                    user.VariableManager.UserVariables.Remove("merchants_disabled");
                                    user.Info.ChangeStats(StatsProperty.Karma, +2);
                                }
                                else
                                {
                                    SendMessage(user, "К сожалению, у тебя нет таких денег");
                                }

                                user.RoomManager.Leave();
                            }
                        },
                        {
                            "Нет", (user, message) =>
                            {
                                SendMessage(user, "Торговцы грустно поплелись дальше");
                                user.RoomManager.Leave();
                            }
                        }
                    }
                }
            };
        }

        public override string Name => "Торговцы с Востока!";
        public override string Identifier => Id;

        public override void OnEnter(User user)
        {
            base.OnEnter(user);

            SwitchAction(user, null);
            user.MessageManager.ShownStats = ShownStats.Gold;

            if (user.VariableManager.UserVariables.Get<Serializable.Decimal>("merchants_disabled") != null)
            {
                SendMessage(user, "Торговцы грустно бредут дальше и не обращают на тебя внимания", GetButtons(user));
                return;
            }

            SendMessage(
                user,
                "Перед тобой расположился небольшой караван, состоящий из трех верблюдов и нескольких купцов. Под листвой ветвистого дуба расположилась миниатюрная, но необыкновенно красивая палатка. От этого места так и веет восточным колоритом."
            );
            SendMessage(
                user,
                "— Дорогой, не желаешь отведать вкуснейших сухофруктов во всей Азии? Или нарядиться в тончайшие атласные шелка? А может, тебе не терпится пролить крови искусно отделанным ножом из слоновой кости? Мы привозим только лучшее! Еще ни одного разочарованного клиента!",
                GetButtons(user)
            );
        }

        public override void OnMessage(User user, ReceivedMessage message)
        {
            if (!HandleAction(user, message))
            {
                HandleButtonAlways(user, message);
            }
        }

        private bool Nothing(User user)
        {
            var oldGold =
                user.VariableManager.UserVariables.Get<Serializable.Decimal>("merchants_disabled");

            if (oldGold == null)
            {
                return true;
            }

            var paySize = (decimal) oldGold * 1.3M;
            SwitchAction(user, Pay);
            SendMessage(user,
                $"У них ничего нет, но может ты желаешь выплатить им компенсацию в {paySize.Format()} монет?",
                GetButtons(user));
            return false;
        }

        private void Pay(User user, ReceivedMessage message)
        {
            HandleButtonAlways(user, message);
        }

        private void Shop(User user, ReceivedMessage message)
        {
            var items = GetAllItems();
            var flag = new StructFlag<BuyGroup>(BuyGroup.Merchant, BuyGroup.Market);
            var available = items.Keys()
                .Select(id => items.Get(id))
                .Where(item => item?.Price != null && item.Group.Intersects(flag))
                .ToArray();

            foreach (var item in available)
            {
                SendMessage(user, $"<b>{item.Name}</b> (x{ItemCount}) [{item.Price * ItemCount}]\n{item.Description}");
            }

            SendMessage(
                user,
                "— За звонкую монету можно приобрести все, что угодно!",
                available
                    .Select(item => new[] {item.Name})
                    .Concat(new[] {new[] {"Ничего"}})
                    .ToArray()
            );

            SwitchAction(user, Shop2);
        }

        private void Shop2(User user, ReceivedMessage message)
        {
            var dict = GetAllItems()
                .AvailableToBuy(new StructFlag<BuyGroup>(BuyGroup.Merchant, BuyGroup.Market))
                .ToDictionary(i => i.Name, i => i);

            if (message.Text == "Ничего")
            {
                SwitchAction(user, null);
                SendMessage(user, "— Жаль, что не смогли предложить ничего подходящего.", GetButtons(user));
            }
            else if (dict.TryGetValue(message.Text, out var item))
            {
                SwitchAction(user, null);
                if (user.BuyItem(new ItemInfo(item, ItemCount)))
                {
                    SendMessage(user, "— Приятно иметь дело с таким щедрым господином!", GetButtons(user));
                }
                else
                {
                    SendMessage(user, "— Даже мешок золота не возместит потраченного на тебя времени!");
                    user.RoomManager.Leave();
                }
            }
            else
            {
                SendMessage(user, "— Увы, но мы о таком никогда не слышали ранее.");
            }
        }
    }
}