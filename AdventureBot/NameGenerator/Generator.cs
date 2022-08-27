using System;
using System.Globalization;

namespace AdventureBot.NameGenerator;

public static class Generator
{
    public static string Generate(Random rnd)
    {
        var gender = rnd.Next(3);
        var adjective = rnd.Next(Names.AdjectivesCounts[gender]);
        var noun = rnd.Next(Names.NounsCounts[gender]);
        return CultureInfo.InvariantCulture.TextInfo.ToTitleCase(
            $"{Names.Adjectives[gender][adjective]} {Names.Nouns[gender][noun]}".ToLowerInvariant());
    }
}