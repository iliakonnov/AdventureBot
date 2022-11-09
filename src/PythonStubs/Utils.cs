using System.Reflection;
using System.Runtime.CompilerServices;
using System.Text.RegularExpressions;

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
        name = name.Split('.').Last();

        if (name is "None" or "True" or "False" or "except" or "finally" or "from" or "global" or "break" or "continue")
        {
            return name + "_";
        }

        return name;
    }

    public static string TypeName(Type type, HashSet<string>? imports, HashSet<string>? typeVars)
    {
        if (PrimitiveName(type) is { } primitive)
        {
            Program.Schedule(type);
            return primitive;
        }

        if (type == typeof(void))
        {
            return "None";
        }

        if (type.IsArray)
        {
            return $"System.Array[{TypeName(type.GetElementType()!, imports, typeVars)}]";
        }

        if (type.IsByRef)
        {
            return $"ref[{TypeName(type.GetElementType(), imports, typeVars)}]";
        }

        if (type.IsPointer)
        {
            return $"ptr[{TypeName(type.GetElementType(), imports, typeVars)}]";
        }

        if (type.IsGenericParameter)
        {
            typeVars?.Add(type.Name);
            return type.Name;
        }

        Program.Schedule(type);

        var name = type.IsGenericType ? type.GetGenericTypeDefinition().FullName : type.FullName;
        name = name!.Replace('+', '.');
        name = Regex.Replace(name, @"`\d+", "");

        name = name.Split('`')[0];
        var ns = string.Join('.', name.Split('.').SkipLast(1));
        imports?.Add(ns);

        if (type.GenericTypeArguments.Length == 0)
        {
            return name;
        }

        var arguments = type.GenericTypeArguments.Select(x => TypeName(x, imports, typeVars)).ToArray();
        return name + "[" + string.Join(", ", arguments) + "]";
    }

    public static string? PrimitiveName(Type type)
    {
        return Type.GetTypeCode(type) switch
        {
            TypeCode.Empty => "None",
            TypeCode.Boolean => "bool",
            TypeCode.SByte or TypeCode.Byte => "int",
            TypeCode.Int16 or TypeCode.UInt16 => "int",
            TypeCode.Int32 or TypeCode.UInt32 => "int",
            TypeCode.Int64 or TypeCode.UInt64 => "int",
            TypeCode.Single or TypeCode.Double => "float",
            TypeCode.Char or TypeCode.String => "str",
            TypeCode.Decimal or TypeCode.DateTime => null, // python types are too different
            TypeCode.DBNull => null,
            TypeCode.Object => null,
            _ => null
        };
    }

    public static string SimpleName(Type type)
    {
        Program.Schedule(type);

        var name = type.Name;
        name = name.Split('`')[0];

        return Utils.FormatName(name);
    }
}