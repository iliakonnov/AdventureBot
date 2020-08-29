using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.CodeAnalysis;
using Microsoft.CodeAnalysis.CSharp;
using Microsoft.CodeAnalysis.CSharp.Scripting;
using Microsoft.CodeAnalysis.CSharp.Syntax;
using Microsoft.CodeAnalysis.MSBuild;

namespace Analyser
{
    public class ClassInfo
    {
        public string SymbolName { get; private set; }
        public string ID { get; private set; }
        public string Name { get; private set; }
        public bool IsRoom { get; private set; }
        public bool IsMonster { get; private set; }
        public bool IsQuest { get; private set; }
        public bool IsBoss { get; private set; }
        public bool IsItem { get; private set; }
        public bool IsGameObject => IsRoom || IsItem;

        public static async Task<ClassInfo> Construct(INamedTypeSymbol symbol)
        {
            var interfaces = symbol.AllInterfaces
                .Select(b => b.ToDisplayString())
                .ToImmutableHashSet();
            var bases = CollectBases(symbol)
                .Select(b => b.ToDisplayString())
                .ToImmutableHashSet();
            var attributes = symbol.GetAttributes();

            var item_attr = attributes.SingleOrDefault(a =>
                a?.AttributeClass?.ToDisplayString() == "AdventureBot.ObjectManager.ItemAttribute");
            var room_attr = attributes.SingleOrDefault(a =>
                a?.AttributeClass?.ToDisplayString() == "AdventureBot.Room.ItemAttribute");
            var available_attr = attributes.SingleOrDefault(a =>
                a?.AttributeClass?.ToDisplayString() == "AdventureBot.Room.AvailableAttribute");
            
            var result = new ClassInfo
            {
                SymbolName = symbol.ToDisplayString(),
                IsRoom = interfaces.Contains("AdventureBot.Room.IRoom")
                         && (room_attr ?? available_attr) != null,
                IsItem = interfaces.Contains("AdventureBot.Item.IItem")
                         && item_attr != null,
            };

            string id;
            if (result.IsRoom)
            {
                var attr = room_attr ?? available_attr;
                id = (string) attr.ConstructorArguments[0].Value;
            }
            else if (result.IsItem)
            {
                id = (string) item_attr.ConstructorArguments[0].Value;
            }
            else
            {
                return null;
            }

            result.ID = id;
            result.IsMonster = interfaces.Contains("AdventureBot.Room.IMonster");
            result.IsQuest = interfaces.Contains("AdventureBot.Room.IQuestMonster");
            result.IsBoss = bases.Contains("AdventureBot.Room.BossBase");
            result.Name = Parser.Trivial(
                symbol.GetMembers("Name").FirstOrDefault(), @"¯\_(ツ)_/¯");

            return result;
        }

        private static IEnumerable<INamedTypeSymbol> CollectBases(INamedTypeSymbol sym)
        {
            sym = sym.BaseType;
            while (sym != null)
            {
                yield return sym;
                sym = sym.BaseType;
            }
        }
    }
    
    public static class Parser
    {
        public static T Trivial<T>(ISymbol symbol, T def = default)
        {
            if (symbol is IPropertySymbol prop)
            {
                // https://stackoverflow.com/a/38030934
                var getter = prop.GetMethod;
                var typeName = $"{getter.ContainingType.ToDisplayString()}, {getter.ContainingAssembly.ToDisplayString()}";
                try
                {
                    var method = Type.GetType(typeName).GetMethod(getter.Name);
                    var del = (Func<T>) Delegate.CreateDelegate(typeof(Func<T>), null, method);
                    return del();
                }
                catch (Exception)
                {
                    return def;
                }
            }
            else
            {
                return def;
            }
        }

        public static async IAsyncEnumerable<ClassInfo> AnalyseSolution()
        {
            using (var w = MSBuildWorkspace.Create())
            {
                w.LoadMetadataForReferencedProjects = true;
                var solution = await w.OpenSolutionAsync(Startup.SolutionPath);
                var root_proj = solution.Projects.Single(p => p.Name == "Analyser");

                foreach (var proj in root_proj.ProjectReferences)
                {
                    var project = solution.GetProject(proj.ProjectId);

                    var compilation = await project.GetCompilationAsync();
                    var errors = compilation.GetDiagnostics()
                        .Where(diagnostic => diagnostic.Severity == DiagnosticSeverity.Error)
                        .ToArray();
                    if (errors.Length != 0)
                    {
                        Console.WriteLine($"COMPILATION ERROR: {compilation.AssemblyName}: {errors.Count()} compilation errors: \n\t{string.Join("\n\t", errors.Where(e => false).Select(e => e.ToString()))}");
                    }
                    
                    var classVisitor = new ClassVirtualizationVisitor();
                    foreach (var syntaxTree in compilation.SyntaxTrees)
                    {
                        classVisitor.Visit(syntaxTree.GetRoot());                
                    }
                    var classes = classVisitor.Classes;
                    foreach (var @class in classes)
                    {
                        var sem = compilation.GetSemanticModel(@class.SyntaxTree);
                        var sym = sem.GetDeclaredSymbol(@class);
                        var info = await ClassInfo.Construct(sym);
                        if (info != null)
                        {
                            yield return info;
                        }
                    }
                }
            }
            GC.Collect();
        }
        
        class ClassVirtualizationVisitor : CSharpSyntaxRewriter
        {
            public ClassVirtualizationVisitor()
            {
                Classes = new List<ClassDeclarationSyntax>();
            }

            public List<ClassDeclarationSyntax> Classes { get; }

            public override SyntaxNode VisitClassDeclaration(ClassDeclarationSyntax node)
            {
                node = (ClassDeclarationSyntax)base.VisitClassDeclaration(node);
                Classes.Add(node); // save your visited classes
                return node;
            }
        }
    }
}