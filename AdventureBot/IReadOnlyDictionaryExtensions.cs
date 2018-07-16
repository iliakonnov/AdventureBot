using System.Collections.Generic;

namespace AdventureBot
{
    public static class IReadOnlyDictionaryExtensions
    {
        public static TValue GetValueOrDefault<TKey, TValue>(this IReadOnlyDictionary<TKey, TValue> dictionary,
            TKey key,
            TValue value = default)
        {
            return dictionary.TryGetValue(key, out var result) ? result : value;
        }
    }
}