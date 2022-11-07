from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import System
import System.Collections.Generic
import System.Runtime.Loader
import System.Reflection
import System.IO
import System.Runtime.CompilerServices
import System.Runtime.Loader.AssemblyLoadContext


class AssemblyLoadContext(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def AllContexts(self) -> System.Collections.Generic.Dictionary[int, System.WeakReference[System.Runtime.Loader.AssemblyLoadContext]]:
        ...

    @property
    def Assemblies(self) -> System.Collections.Generic.IEnumerable[System.Reflection.Assembly]:
        ...

    @property
    def Default(self) -> System.Runtime.Loader.AssemblyLoadContext:
        ...

    @property
    def IsCollectible(self) -> bool:
        ...

    @property
    def Name(self) -> str:
        ...

    @property
    def All(self) -> System.Collections.Generic.IEnumerable[System.Runtime.Loader.AssemblyLoadContext]:
        ...

    @property
    def CurrentContextualReflectionContext(self) -> System.Runtime.Loader.AssemblyLoadContext:
        ...

    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def __init__(self, isCollectible: bool, ):
        ...

    @typing.overload
    def __init__(self, name: str, isCollectible: bool = ..., ):
        ...

    @typing.overload
    def __init__(self, representsTPALoadContext: bool, isCollectible: bool, name: str, ):
        ...

    def LoadFromNativeImagePath(self, nativeImagePath: str, assemblyPath: str, ) -> System.Reflection.Assembly:
        ...

    @typing.overload
    def LoadFromStream(self, assembly: System.IO.Stream, ) -> System.Reflection.Assembly:
        ...

    @typing.overload
    def LoadFromStream(self, assembly: System.IO.Stream, assemblySymbols: System.IO.Stream, ) -> System.Reflection.Assembly:
        ...

    @staticmethod
    @typing.overload
    def LoadFromStream(ptrNativeAssemblyLoadContext: System.IntPtr, ptrAssemblyArray: System.IntPtr, iAssemblyArrayLen: int, ptrSymbols: System.IntPtr, iSymbolArrayLen: int, retAssembly: System.Runtime.CompilerServices.ObjectHandleOnStack, ) -> None:
        ...

    def LoadUnmanagedDllFromPath(self, unmanagedDllPath: str, ) -> System.IntPtr:
        ...

    def LoadUnmanagedDll(self, unmanagedDllName: str, ) -> System.IntPtr:
        ...

    def Unload(self, ) -> None:
        ...

    @staticmethod
    def OnProcessExit() -> None:
        ...

    def VerifyIsAlive(self, ) -> None:
        ...

    @staticmethod
    def SetCurrentContextualReflectionContext(value: System.Runtime.Loader.AssemblyLoadContext, ) -> None:
        ...

    @typing.overload
    def EnterContextualReflection(self, ) -> System.Runtime.Loader.AssemblyLoadContext.ContextualReflectionScope:
        ...

    @staticmethod
    @typing.overload
    def EnterContextualReflection(activating: System.Reflection.Assembly, ) -> System.Runtime.Loader.AssemblyLoadContext.ContextualReflectionScope:
        ...

    @staticmethod
    def Resolve(gchManagedAssemblyLoadContext: System.IntPtr, assemblyName: System.Reflection.AssemblyName, ) -> System.Reflection.Assembly:
        ...

    def GetFirstResolvedAssemblyFromResolvingEvent(self, assemblyName: System.Reflection.AssemblyName, ) -> System.Reflection.Assembly:
        ...

    @staticmethod
    def ValidateAssemblyNameWithSimpleName(assembly: System.Reflection.Assembly, requestedSimpleName: str, ) -> System.Reflection.Assembly:
        ...

    def ResolveUsingLoad(self, assemblyName: System.Reflection.AssemblyName, ) -> System.Reflection.Assembly:
        ...

    def ResolveUsingEvent(self, assemblyName: System.Reflection.AssemblyName, ) -> System.Reflection.Assembly:
        ...

    @staticmethod
    def OnAssemblyLoad(assembly: System.Reflection.RuntimeAssembly, ) -> None:
        ...

    @staticmethod
    def OnResourceResolve(assembly: System.Reflection.RuntimeAssembly, resourceName: str, ) -> System.Reflection.RuntimeAssembly:
        ...

    @staticmethod
    def OnTypeResolve(assembly: System.Reflection.RuntimeAssembly, typeName: str, ) -> System.Reflection.RuntimeAssembly:
        ...

    @staticmethod
    def OnAssemblyResolve(assembly: System.Reflection.RuntimeAssembly, assemblyFullName: str, ) -> System.Reflection.RuntimeAssembly:
        ...

    @staticmethod
    def InvokeResolveEvent(eventHandler: System.ResolveEventHandler, assembly: System.Reflection.RuntimeAssembly, name: str, ) -> System.Reflection.RuntimeAssembly:
        ...

    @typing.overload
    def ResolveSatelliteAssembly(self, assemblyName: System.Reflection.AssemblyName, ) -> System.Reflection.Assembly:
        ...

    @staticmethod
    @typing.overload
    def ResolveSatelliteAssembly(gchManagedAssemblyLoadContext: System.IntPtr, assemblyName: System.Reflection.AssemblyName, ) -> System.Reflection.Assembly:
        ...

    def GetResolvedUnmanagedDll(self, assembly: System.Reflection.Assembly, unmanagedDllName: str, ) -> System.IntPtr:
        ...

    @staticmethod
    def InitializeAssemblyLoadContext(ptrAssemblyLoadContext: System.IntPtr, fRepresentsTPALoadContext: bool, isCollectible: bool, ) -> System.IntPtr:
        ...

    @staticmethod
    def PrepareForAssemblyLoadContextRelease(ptrNativeAssemblyLoadContext: System.IntPtr, ptrAssemblyLoadContextStrong: System.IntPtr, ) -> None:
        ...

    @staticmethod
    def InternalSetProfileRoot(directoryPath: str, ) -> None:
        ...

    @staticmethod
    def InternalStartProfile(profile: str, ptrNativeAssemblyLoadContext: System.IntPtr, ) -> None:
        ...

    @staticmethod
    def LoadFromPath(ptrNativeAssemblyLoadContext: System.IntPtr, ilPath: str, niPath: str, retAssembly: System.Runtime.CompilerServices.ObjectHandleOnStack, ) -> None:
        ...

    @staticmethod
    def GetLoadedAssemblies() -> System.Array[System.Reflection.Assembly]:
        ...

    @staticmethod
    def IsTracingEnabled() -> bool:
        ...

    @staticmethod
    def TraceResolvingHandlerInvoked(assemblyName: str, handlerName: str, alcName: str, resultAssemblyName: str, resultAssemblyPath: str, ) -> bool:
        ...

    @staticmethod
    def TraceAssemblyResolveHandlerInvoked(assemblyName: str, handlerName: str, resultAssemblyName: str, resultAssemblyPath: str, ) -> bool:
        ...

    @staticmethod
    def TraceAssemblyLoadFromResolveHandlerInvoked(assemblyName: str, isTrackedAssembly: bool, requestingAssemblyPath: str, requestedAssemblyPath: str, ) -> bool:
        ...

    @staticmethod
    def TraceSatelliteSubdirectoryPathProbed(filePath: str, hResult: int, ) -> bool:
        ...

    def InternalLoadFromPath(self, assemblyPath: str, nativeImagePath: str, ) -> System.Reflection.Assembly:
        ...

    def InternalLoad(self, arrAssembly: System.ReadOnlySpan[int], arrSymbols: System.ReadOnlySpan[int], ) -> System.Reflection.Assembly:
        ...

    @staticmethod
    def ResolveUnmanagedDll(unmanagedDllName: str, gchManagedAssemblyLoadContext: System.IntPtr, ) -> System.IntPtr:
        ...

    @staticmethod
    def ResolveUnmanagedDllUsingEvent(unmanagedDllName: str, assembly: System.Reflection.Assembly, gchManagedAssemblyLoadContext: System.IntPtr, ) -> System.IntPtr:
        ...

    @staticmethod
    def ResolveUsingResolvingEvent(gchManagedAssemblyLoadContext: System.IntPtr, assemblyName: System.Reflection.AssemblyName, ) -> System.Reflection.Assembly:
        ...

    @staticmethod
    def GetLoadContextForAssembly(assembly: System.Runtime.CompilerServices.QCallAssembly, ) -> System.IntPtr:
        ...

    @staticmethod
    def GetLoadContext(assembly: System.Reflection.Assembly, ) -> System.Runtime.Loader.AssemblyLoadContext:
        ...

    def SetProfileOptimizationRoot(self, directoryPath: str, ) -> None:
        ...

    def StartProfileOptimization(self, profile: str, ) -> None:
        ...

    @staticmethod
    def GetRuntimeAssembly(asm: System.Reflection.Assembly, ) -> System.Reflection.RuntimeAssembly:
        ...

    @staticmethod
    def StartAssemblyLoad(activityId: ref[System.Guid], relatedActivityId: ref[System.Guid], ) -> None:
        ...

    @staticmethod
    def StopAssemblyLoad(activityId: ref[System.Guid], ) -> None:
        ...

    @staticmethod
    def InitializeDefaultContext() -> None:
        ...

    def Finalize(self, ) -> None:
        ...

    def RaiseUnloadEvent(self, ) -> None:
        ...

    def InitiateUnload(self, ) -> None:
        ...

    def ToString(self, ) -> str:
        ...

    @staticmethod
    def GetAssemblyName(assemblyPath: str, ) -> System.Reflection.AssemblyName:
        ...

    def Load(self, assemblyName: System.Reflection.AssemblyName, ) -> System.Reflection.Assembly:
        ...

    def LoadFromAssemblyName(self, assemblyName: System.Reflection.AssemblyName, ) -> System.Reflection.Assembly:
        ...

    def LoadFromAssemblyPath(self, assemblyPath: str, ) -> System.Reflection.Assembly:
        ...

