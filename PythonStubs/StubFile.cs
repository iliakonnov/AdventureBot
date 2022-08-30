using System.Reflection;
using System.Text;
using System.Text.RegularExpressions;

namespace PythonStubs;

public class StubFile
{
    private HashSet<string> _imports = new();
    private HashSet<string> _typeVars = new();
    private StringWriter writer = new();

    private string TypeName(Type type)
    {
        if (type == typeof(void))
        {
            return "None";
        }

        if (type.IsArray)
        {
            return $"list[{TypeName(type.GetElementType()!)}]";
        }

        if (type.IsByRef)
        {
            return $"ref[{TypeName(type.GetElementType())}]";
        }

        if (type.IsPointer)
        {
            return $"ptr[{TypeName(type.GetElementType())}]";
        }

        if (type.IsGenericParameter)
        {
            _typeVars.Add(type.Name);
            return type.Name;
        }

        Program.Schedule(type);

        var name = type.IsGenericType ? type.GetGenericTypeDefinition().FullName : type.FullName;
        name = name!.Replace('+', '.');
        name = Regex.Replace(name, @"`\d+", "");
        
        name = name.Split('`')[0];
        var ns = string.Join('.', name.Split('.').SkipLast(1));
        _imports.Add(ns);

        if (type.GenericTypeArguments.Length == 0)
        {
            return name;
        }
        
        var arguments = type.GenericTypeArguments.Select(TypeName).ToArray();
        return name + "[" + string.Join(", ", arguments) + "]";
    }

    private static string SimpleName(Type type)
    {
        Program.Schedule(type);

        var name = type.Name;
        name = name.Split('`')[0];

        return Utils.FormatName(name);
    }

    private void WriteEnum(Type type)
    {
        var underlying = TypeName(type.GetEnumUnderlyingType());

        writer.WriteLine($"class {SimpleName(type)}(enum.Enum, {Inherits(type)}):");
        foreach (var (name, value) in type.GetEnumNames().Zip(type.GetEnumValues().Cast<object>()))
        {
            writer.WriteLine($"    {Utils.FormatName(name)}: {underlying} = {value}");
        }

        writer.WriteLine();
    }

    private string Inherits(Type type)
    {
        var inherits = type.GetInterfaces()
            .Concat(type.BaseType != null ? new[] {type.BaseType} : new Type[] { })
            .Select(TypeName)
            .Concat(type.IsAbstract ? new[] {"abc.ABC"} : new string[] { })
            .Concat(PyGenerics(type));
        return string.Join(", ", inherits);
    }

    private void WriteClass(Type type)
    {
        writer.WriteLine($"class {SimpleName(type)}({Inherits(type)}):");

        writer.WriteLine("    @typing.overload");
        writer.WriteLine("    def __init__(self, **kwargs):");
        foreach (var field in type.GetFields().Where(f => f.IsPublic && !f.IsStatic))
        {
            writer.WriteLine($"        self.{Utils.FormatName(field.Name)}: {TypeName(field.FieldType)}");
        }

        writer.WriteLine("        ...");

        writer.WriteLine("\n    # properties");

        foreach (var property in type.GetProperties())
        {
            WriteProperty(property);
        }

        writer.WriteLine("    # methods");
        foreach (var method in type
                     .GetConstructors()
                     .Cast<MethodBase>()
                     .Concat(type
                         .GetMethods()
                         .Where(x => !x.IsCompilerGenerated() && x.DeclaringType == type))
                     .Where(x => x.IsPublic))
        {
            WriteMethod(method);
        }
    }

    private void WriteProperty(PropertyInfo property)
    {
        var getter = property.GetMethod?.IsPublic == true;
        var setter = property.SetMethod?.IsPublic == true;

        var method = (property.GetMethod ?? property.SetMethod)!;
        var name = Utils.FormatName(property.Name);
        var type = TypeName(property.PropertyType);

        if (getter)
        {
            if (method.IsAbstract)
            {
                writer.WriteLine("    @abc.abstractmethod");
            }

            writer.WriteLine($"    @property");
            writer.WriteLine($"    def {name}(self) -> {type}:");
            writer.WriteLine($"        ...");
        }

        if (getter && setter)
        {
            if (method.IsAbstract)
            {
                writer.WriteLine("    @abc.abstractmethod");
            }

            writer.WriteLine($"    @{name}.setter");
            writer.WriteLine($"    def {name}(self, val: {type}):");
            writer.WriteLine($"        ...");
        }

        if (!getter && setter)
        {
            if (method.IsAbstract)
            {
                writer.WriteLine("    # abstract");
            }

            writer.WriteLine($"    {property.Name}: {TypeName(property.PropertyType)} = property(None, lambda val: ...)");
        }

        writer.WriteLine();
    }

    private string[] PyGenerics(Type type)
    {
        if (type.GetGenericArguments().Length == 0)
        {
            return new string[] { };
        }

        var generics = string.Join(", ", type.GetGenericArguments().Select(TypeName));
        return new[] {$"typing.Generic[{generics}]"};
    }

    private void WriteMethod(MethodBase method)
    {
        writer.WriteLine("    @typing.overload");
        var name = method.IsConstructor ? "__init__" : Utils.FormatName(method.Name);

        if (method.IsAbstract)
        {
            writer.WriteLine($"    @abc.abstractmethod");
        }

        if (method.IsStatic)
        {
            writer.WriteLine("    @staticmethod");
            writer.Write($"    def {name}(");
        }
        else
        {
            writer.Write($"    def {name}(self, ");
        }

        foreach (var parameter in method.GetParameters())
        {
            writer.Write($"{Utils.FormatName(parameter.Name)}: {TypeName(parameter.ParameterType)}, ");
        }

        writer.Write(")");
        if (!method.IsConstructor)
        {
            var mi = (MethodInfo) method;
            writer.Write($" -> {TypeName(mi.ReturnType)}");
        }

        writer.WriteLine(":");
        writer.WriteLine("        ...");
        writer.WriteLine();
    }

    public void WriteType(Type type)
    {
        if (type.IsEnum)
        {
            WriteEnum(type);
        }
        else
        {
            WriteClass(type);
        }
    }

    public void Save(TextWriter output)
    {
        output.WriteLine("from __future__ import annotations");
        output.WriteLine("import typing, abc, enum");
        output.WriteLine("from stubhelper import *");
        output.WriteLine();
        foreach (var i in _imports)
        {
            output.WriteLine($"import {i}");
        }

        output.WriteLine();
        foreach (var typeVar in _typeVars)
        {
            output.WriteLine($"{typeVar} = typing.TypeVar('{typeVar}')");
        }

        output.WriteLine();
        output.Write(writer.ToString());
    }
}