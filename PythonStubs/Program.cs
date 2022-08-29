using System.Reflection;
using System.Runtime.CompilerServices;
using System.Text.RegularExpressions;

string TypeName(Type type)
{
    var name = type.FullName ?? $"'{type.Name}'";
    return Regex.Replace(name, @"`\d+", "");
}

string SimpleName(Type type)
{
    var name = type.Name;
    return name.Split('`')[0];
}

void WriteType(TextWriter writer, Type type)
{
    if (type.IsClass)
    {
        var inherits = type.GetInterfaces()
            .Concat(type.BaseType != null ? new[] {type.BaseType} : new Type[] { })
            .Select(TypeName);
        writer.WriteLine($"class {SimpleName(type)}({string.Join(", ", inherits)}):");

        writer.WriteLine("    def __init__(self, *args, **kwargs): ...");
        foreach (var field in type.GetFields().Where(f => f.IsPublic && !f.IsStatic))
        {
            writer.WriteLine($"        self.{field.Name}: {TypeName(field.FieldType)}");
        }

        writer.WriteLine();

        foreach (var ctor in type.GetConstructors().Where(ctor => ctor.IsPublic))
        {
            writer.WriteLine("    @typing.overload");
            writer.WriteLine("    def __init__(self, ");
            foreach (var parameter in ctor.GetParameters())
            {
                writer.WriteLine($"        {parameter.Name}: {TypeName(parameter.ParameterType)},");
            }

            writer.WriteLine("    ): ...");
        }

        writer.WriteLine();

        foreach (var property in type.GetProperties())
        {
            var getter = property.GetMethod?.IsPublic == true;
            var setter = property.SetMethod?.IsPublic == true;

            if (getter)
            {
                writer.WriteLine($"    @property");
                writer.WriteLine($"    def {property.Name}(self) -> {TypeName(property.PropertyType)}: ...");
            }

            if (getter && setter)
            {
                writer.WriteLine($"    @{property.Name}.setter");
                writer.WriteLine($"    def {property.Name}(self, val: {TypeName(property.PropertyType)}): ...");
            }

            if (!getter && setter)
            {
                writer.WriteLine($"    {property.Name}: {TypeName(property.PropertyType)} = property(None, lambda val: ...)");
            }

            writer.WriteLine();
        }
    }
}

void Main()
{
    var outDir = Environment.GetCommandLineArgs()[1];
    var namespaces = new Dictionary<string, HashSet<string>>();
    var types = AdventureBot.Configuration.Config.GetSection("assemblies").GetChildren()
        .Select(x => x.Value)
        .Select(Assembly.LoadFrom)
        .Concat(new[] {Assembly.Load("AdventureBot")})
        .SelectMany(assembly => assembly.GetTypes());

    if (Directory.Exists(outDir))
    {
        Directory.Delete(outDir, true);
    }

    foreach (var type in types)
    {
        var compilerGenerated = type.GetCustomAttribute(typeof(CompilerGeneratedAttribute), true) != null;
        if (type.IsNotPublic || type.Namespace == null || compilerGenerated)
        {
            continue;
        }

        Console.WriteLine(type);
        var namespacePath = type.Namespace!.Replace('.', Path.DirectorySeparatorChar);
        var directory = Path.Join(outDir, namespacePath);
        var filename = SimpleName(type);
        var path = Path.Join(directory, $"{filename}.py");

        Directory.CreateDirectory(directory);
        if (!File.Exists(path))
        {
            File.WriteAllText(path, "import typing\n\n");
        }

        using (var output = new StreamWriter(path, true))
        {
            WriteType(output, type);
        }

        if (!namespaces.ContainsKey(directory))
        {
            namespaces[directory] = new HashSet<string>();
        }

        namespaces[directory].Add(filename);
    }

    foreach (var (directory, classes) in namespaces)
    {
        var path = Path.Join(directory, "__init__.py");
        using var output = new StreamWriter(path);
        foreach (var cls in classes)
        {
            output.WriteLine($"from .{cls} import {cls} as {cls}");
        }
    }

    File.Create(Path.Join(outDir, "__init__.py"));
}

Main();