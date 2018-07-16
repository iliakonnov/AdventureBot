using System.IO;
using System.Timers;
using MessagePack;

namespace AdventureBot
{
    public class GlobalVariables
    {
        public static VariableContainer Variables { get; }

        // ReSharper disable once PrivateFieldCanBeConvertedToLocalVariable (It must not be removed by GC)
        private static readonly Timer FlushTimer;
        private const string Filename = "globalVariables.msgpack";

        static GlobalVariables()
        {
            FlushTimer = new Timer
            {
                AutoReset = true,
                Interval = 15 * 1000  // Every 15 seconds
            };
            FlushTimer.Elapsed += (sender, args) => Flush();
            FlushTimer.Start();

            if (File.Exists(Filename))
            {
                Variables = MessagePackSerializer.Deserialize<VariableContainer>(
                    File.ReadAllBytes(Filename));
            }
            else
            {
                Variables = new VariableContainer();
            }
        }

        private static void Flush()
        {
            File.WriteAllBytes(Filename, MessagePackSerializer.Serialize(Variables));
        }
    }
}