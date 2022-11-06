using System.Reflection;
using System.Text;
using System.Text.RegularExpressions;

namespace PythonStubs;

public class Member
{
    public string Name;
    public List<string> Items = new();

    public Member(string name)
    {
        Name = name;
    }
}

public class StubFile
{
    private HashSet<string> _imports = new();
    private HashSet<string> _typeVars = new();
    private StringWriter writer = new();
    public List<Member> members = new();

    private string TypeName(Type type)
    {
        return Utils.TypeName(type, _imports, _typeVars);
    }

    private void WriteEnum(Type type)
    {
        var underlying = TypeName(type.GetEnumUnderlyingType());

        writer.WriteLine($"class {Utils.SimpleName(type)}(enum.Enum, {Inherits(type)}):");
        foreach (var name in type.GetEnumNames())
        {
            writer.WriteLine($"    {Utils.FormatName(name)}: {underlying} = ...");
        }

        writer.WriteLine();
    }

    private string Inherits(Type type)
    {
        var inherits = type.GetInterfaces()
            .Concat(type.BaseType != null ? new[] { type.BaseType } : new Type[] { })
            .Select(TypeName)
            .Concat(type.IsAbstract ? new[] { "abc.ABC" } : new string[] { })
            .Concat(PyGenerics(type));
        return string.Join(", ", inherits);
    }

    private void WriteClass(Type type)
    {
        if (Utils.PrimitiveName(type) is { } primitive)
        {
            writer.WriteLine($"{Utils.SimpleName(type)} = {primitive}");
            writer.WriteLine();
            return;
        }

        var name = Utils.SimpleName(type);
        var member = new Member(name);

        var bindingAttr = BindingFlags.Public | BindingFlags.NonPublic | BindingFlags.Instance | BindingFlags.Static;

        writer.WriteLine($"class {name}({Inherits(type)}):");

        writer.WriteLine("    @typing.overload");
        writer.WriteLine("    def __init__(self, **kwargs):");
        foreach (var field in type.GetFields(bindingAttr).Where(f => !f.IsPrivate && !f.IsStatic))
        {
            member.Items.Add(Utils.FormatName(field.Name));
            writer.WriteLine($"        self.{Utils.FormatName(field.Name)}: {TypeName(field.FieldType)}");
        }

        writer.WriteLine("        ...");

        writer.WriteLine("\n    # static fields");

        foreach (var field in type.GetFields(bindingAttr).Where(f => !f.IsPrivate && f.IsStatic))
        {
            member.Items.Add(Utils.FormatName(field.Name));
            writer.WriteLine($"    {Utils.FormatName(field.Name)}: {TypeName(field.FieldType)} = ...");
        }

        writer.WriteLine("\n    # properties");

        foreach (var property in type.GetProperties(bindingAttr))
        {
            member.Items.Add(Utils.FormatName(property.Name));
            WriteProperty(property);
        }

        writer.WriteLine("    # methods");
        foreach (var group in type
                     .GetConstructors(bindingAttr)
                     .Where(ctor => ctor.IsConstructor)
                     .Cast<MethodBase>()
                     .Concat(type
                         .GetMethods(bindingAttr)
                         .Where(x => !x.IsCompilerGenerated() && !x.IsConstructor && x.DeclaringType == type))
                     .GroupBy(x => x.Name)
                     .Select(x => x.ToArray()))
        {
            var haveOverloads = group.Length != 1;
            member.Items.Add(Utils.FormatName(group[0].Name));
            foreach (var method in group)
            {
                WriteMethod(method, haveOverloads);
            }
        }

        members.Add(member);
    }

    private void WriteProperty(PropertyInfo property)
    {
        var getter = property.GetMethod != null;
        var setter = property.SetMethod != null;

        var method = (property.GetMethod ?? property.SetMethod)!;
        var name = Utils.FormatName(property.Name);
        var type = TypeName(property.PropertyType);

        if (getter)
        {
            writer.WriteLine($"    @property");

            if (method.IsAbstract)
            {
                writer.WriteLine("    @abc.abstractmethod");
            }

            writer.WriteLine($"    def {name}(self) -> {type}:");
            writer.WriteLine($"        ...");
        }

        if (getter && setter)
        {
            writer.WriteLine($"    @{name}.setter");

            if (method.IsAbstract)
            {
                writer.WriteLine("    @abc.abstractmethod");
            }

            writer.WriteLine($"    def {name}(self, val: {type}):");
            writer.WriteLine($"        ...");
        }

        if (!getter && setter)
        {
            if (method.IsAbstract)
            {
                writer.WriteLine("    # abstract");
            }

            writer.WriteLine(
                $"    {name}: {TypeName(property.PropertyType)} = property(None, lambda val: ...)");
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
        return new[] { $"typing.Generic[{generics}]" };
    }

    private void WriteMethod(MethodBase method, bool haveOverloads)
    {
        if (method.IsStatic)
        {
            writer.WriteLine("    @staticmethod");
        }

        if (method.IsAbstract)
        {
            writer.WriteLine($"    @abc.abstractmethod");
        }

        if (haveOverloads)
        {
            writer.WriteLine("    @typing.overload");
        }

        var name = method.IsConstructor ? "__init__" : Utils.FormatName(method.Name);

        writer.Write(method.IsStatic ? $"    def {name}(" : $"    def {name}(self, ");

        foreach (var parameter in method.GetParameters())
        {
            writer.Write($"{Utils.FormatName(parameter.Name)}: {TypeName(parameter.ParameterType)}");
            if (parameter.HasDefaultValue)
            {
                writer.Write(" = ...");
            }

            writer.Write(", ");
        }

        writer.Write(")");
        if (!method.IsConstructor)
        {
            var mi = (MethodInfo)method;
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