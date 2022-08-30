using System.Reflection;
using System.Runtime.CompilerServices;

namespace PythonStubs;

public static class Utils
{
    public static bool IsCompilerGenerated(this Type type)
    {
        return type.GetCustomAttribute<CompilerGeneratedAttribute>() != null;
    }

    public static bool IsCompilerGenerated(this MethodBase method)
    {
        if (method.IsSpecialName)
        {
            return true;
        }

        return method.GetCustomAttribute<CompilerGeneratedAttribute>() != null;
    }

    public static string FormatName(string name)
    {
        if (name is "None" or "True" or "False" or "except" or "finally" or "from" or "global" or "break" or "continue")
        {
            return name + "_";
        }

        return name;
    }
}