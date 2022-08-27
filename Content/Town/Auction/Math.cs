using System;
using System.Collections.Generic;

namespace Content.Town.Auction;

// https://t.me/AdventureTavern/3422
public static class Math
{
    public static IEnumerable<Tuple<int, int>> GetPrices()
    {
        const int maxN = 6;
        var beginning = Ending(0);
        for (var i = 0; i < maxN; i++)
        {
            if (i == 0)
            {
                // Special case
                yield return new Tuple<int, int>(0, 10);
                continue;
            }

            var ending = Ending(i);
            yield return new Tuple<int, int>(beginning, ending);
            beginning = ending;
        }
    }

    public static IEnumerable<int> GetSubPrices(int n)
    {
        if (n < 0)
        {
            throw new ArgumentException("n must be >= 0", nameof(n));
        }

        if (n == 0)
        {
            // Special case
            foreach (var res in new[] {0, 1, 3, 5, 10})
            {
                yield return res;
            }

            yield break;
        }

        var beginning = Ending(n - 1);
        var ending = Ending(n);
        var step = Step(n);
        for (var i = beginning; i <= ending; i += step)
        {
            yield return i;
        }
    }

    private static int Ending(int n)
    {
        return 50 * ((1 << n) - 1) + 10;
    }

    private static int Step(int n)
    {
        return 10 * (1 << (n - 1));
    }
}