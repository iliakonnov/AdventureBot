using System.Reflection;
using System.Text.RegularExpressions;
using PythonStubs;

static class Program
{
    private static SortedSet<Type> scheduled = new();
    private static HashSet<Guid> written = new();
    private static Dictionary<string, StubFile> files = new();

    public static void Schedule(Type type)
    {
        if (written.Contains(type.GUID))
        {
            return;
        }

        scheduled.Add(type);
    }

    public static void Main()
    {
        var outDir = Environment.GetCommandLineArgs()[1];
        var namespaces = new Dictionary<string, HashSet<string>>();
        var assemblies = new[]
        {
            Assembly.Load("AdventureBot"),
            Assembly.Load("Content"),
            Assembly.Load("IronPython"),
        };
        var types = assemblies.SelectMany(assembly => assembly.GetTypes());
        scheduled = new SortedSet<Type>(types, Comparer<Type>.Create((a, b) => a.GUID.CompareTo(b.GUID)));

        if (Directory.Exists(outDir))
        {
            Directory.Delete(outDir, true);
        }

        while (scheduled.Count != 0)
        {
            var type = scheduled.Min;
            scheduled.Remove(type);

            if (!written.Add(type.GUID))
            {
                continue;
            }

            if (type.IsNotPublic || type.Namespace == null || type.IsCompilerGenerated())
            {
                continue;
            }

            if (type.IsGenericType)
            {
                type = type.GetGenericTypeDefinition();
            }

            var path = TypeToPath(outDir, type);

            if (!files.ContainsKey(path))
            {
                files[path] = new StubFile();
            }

            files[path].WriteType(type);

            var directory = Path.GetDirectoryName(path);
            if (!namespaces.ContainsKey(directory))
            {
                namespaces[directory] = new HashSet<string>();
            }
        }

        foreach (var (path, file) in files)
        {
            var directory = Path.GetDirectoryName(path);
            Directory.CreateDirectory(directory);
            using var writer = new StreamWriter(path);
            file.Save(writer);
        }

        GenerateModules(assemblies, outDir);

        var self = Assembly.GetExecutingAssembly();
        foreach (var resource in self.GetManifestResourceNames())
        {
            if (!resource.StartsWith("PythonStubs.static.") || !resource.EndsWith(".pyi"))
            {
                continue;
            }

            var path = resource["PythonStubs.static.".Length..][..^".pyi".Length]
                .Replace('.', Path.DirectorySeparatorChar) + ".pyi";
            using var stream = self.GetManifestResourceStream(resource)!;
            using var file = File.Create(Path.Combine(outDir, path));
            stream.CopyTo(file);
        }
    }

    private static void GenerateModules(Assembly[] assemblies, string outDir)
    {
        foreach (var assembly in assemblies)
        {
            foreach (var module in assembly.GetCustomAttributes<IronPython.Runtime.PythonModuleAttribute>())
            {
                var memberName = Utils.FormatName(module.Type.Name);
                var imports = new HashSet<string>();
                var typeVars = new HashSet<string>();
                var typeName = Utils.TypeName(module.Type, imports, typeVars);
                var stub = files[TypeToPath(outDir, module.Type)];
                using var writer = new StreamWriter(Path.Combine(outDir, $"{module.Name}.pyi"));

                foreach (var import in imports)
                {
                    writer.WriteLine($"import {import}");
                }

                if (typeVars.Count != 0)
                {
                    writer.WriteLine("import typing");
                }

                foreach (var typeVar in typeVars)
                {
                    writer.WriteLine($"{typeVar} = typing.TypeVar('T')");
                }

                foreach (var item in stub.members.Where(x => x.Name == memberName).SelectMany(x => x.Items))
                {
                    writer.WriteLine($"{item} = {typeName}.{item}");
                }
            }
        }
    }

    private static string TypeToPath(string outDir, Type type)
    {
        var name = type.FullName!.Replace('+', '.').Split('[')[0];
        name = Regex.Replace(name, @"`\d+", "");
        var namespacePath = string.Join('.', name.Split('.').SkipLast(1)).Replace('.', Path.DirectorySeparatorChar);
        var directory = Path.Join(outDir, namespacePath);
        var path = Path.Join(directory, "__init__.pyi");
        return path;
    }
}