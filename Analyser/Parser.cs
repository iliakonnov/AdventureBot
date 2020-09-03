using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Linq;
using System.Threading.Tasks;
using AdventureBot.ObjectManager;
using Microsoft.Build.Construction;
using Microsoft.CodeAnalysis;
using Microsoft.CodeAnalysis.CSharp;
using Microsoft.CodeAnalysis.CSharp.Scripting;
using Microsoft.CodeAnalysis.CSharp.Syntax;
using Microsoft.CodeAnalysis.MSBuild;

namespace Analyser
{
    internal abstract class ClassInfo
    {
        public INamedTypeSymbol Symbol;
        public string ID { get; private set; }
        public string Name { get; private set; }
        public bool IsRoom => this is Room;
        public bool IsItem => this is Item;

        protected ImmutableHashSet<string> _interfaces;
        protected ImmutableHashSet<string> _bases;
        protected ImmutableArray<AttributeData> _attributes;
        
        protected abstract void Fill();

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
            
            var isRoom = interfaces.Contains("AdventureBot.Room.IRoom")
                            && (room_attr ?? available_attr) != null;
            var isItem = interfaces.Contains("AdventureBot.Item.IItem")
                            && item_attr != null;
            ClassInfo result;
            if (isItem)
            {
                result = new Item();
                result.ID = (string) item_attr.ConstructorArguments[0].Value;
            }
            else if (isRoom)
            {
                result = new Room();
                result.ID = (string) (room_attr ?? available_attr).ConstructorArguments[0].Value;
            }
            else
            {
                return null;
            }

            result.Symbol = symbol;
            result.Name = Parser.Trivial(symbol.GetMembers("Name").FirstOrDefault(), @"¯\_(ツ)_/¯");
            result.Fill();

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
    
    internal static class Parser
    {
        public static T Trivial<T>(ISymbol symbol, T def = default)
        {
            if (symbol is IPropertySymbol prop)
            {
                // https://stackoverflow.com/a/38030934
                var getter = prop.GetMethod;
                var returnType = getter.ReturnType;
                return default;
            }
            else
            {
                return def;
            }
        }

        /*public static async IAsyncEnumerable<ClassInfo> AnalyseSolution()
        {
            using var ws = new AdhocWorkspace();
            var solution = ws.AddSolution(SolutionInfo.Create(
                SolutionId.CreateNewId(),
                VersionStamp.Create(),
                Startup.SolutionPath.FullName
            ));
            var parsedSolution = SolutionFile.Parse(Startup.SolutionPath.FullName);
            var analyser = parsedSolution.ProjectsInOrder.Single(p => p.ProjectName == "Analyser");
            while (false)
            {
                yield return null;
            }
        }*/

        public static async IAsyncEnumerable<ClassInfo> AnalyseSolution()
        {
            using (var w = MSBuildWorkspace.Create(
                new Dictionary<string, string> { { "Configuration", "Debug" }, { "Platform", "AnyCPU" } }
            ))
            {
                w.LoadMetadataForReferencedProjects = true;
                w.WorkspaceFailed += (sender, args) =>
                {
                    Console.WriteLine("Workspace failed [{0}]: {1}", args.Diagnostic.Kind, args.Diagnostic.Message);
                };
                var solution = await w.OpenSolutionAsync(Startup.SolutionPath.FullName);
                var root_proj = solution.Projects.Single(p => p.Name == "Analyser");

                foreach (var proj in root_proj.ProjectReferences)
                {
                    var project = solution.GetProject(proj.ProjectId);
                    Console.WriteLine("Loading {0}", project.Name);

                    var compilation = await project.GetCompilationAsync();
                    var errors = compilation.GetDiagnostics()
                        .Where(diagnostic => diagnostic.Severity == DiagnosticSeverity.Error)
                        .ToArray();
                    if (errors.Length != 0)
                    {
                        Console.WriteLine($"COMPILATION ERROR: {compilation.AssemblyName}: {errors.Count()} compilation errors.");
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

        private class ClassVirtualizationVisitor : CSharpSyntaxRewriter
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