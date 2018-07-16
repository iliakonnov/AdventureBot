using System.Collections.Generic;
using System.Linq;
using AdventureBot;
using AdventureBot.ObjectManager;

namespace Telegram
{
    [Messenger]
    public class Bots : Messenger
    {
        public Bots() : base(
            Configuration.Config.GetSection("telegram_bots").GetChildren()
                .Select((child, idx) => new TelegramBot(child.Value, idx == 0))
                .ToList()
        )
        {
        }
    }
}