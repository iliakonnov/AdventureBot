using System;
using System.Text;

namespace AdventureBot
{
    public static class DecimalExtensions
    {
        public static string Format(this decimal dec, int precision = 2)
        {
            var format = $"0.{new string('#', precision)}";
            return dec.ToString(format);
        }
    }
}