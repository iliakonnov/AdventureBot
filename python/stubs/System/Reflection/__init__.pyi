from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import System.Reflection
import System
import System.Collections.Generic
import System.Reflection.MethodBase
import System.Globalization
import System.Text
import System.Runtime.Serialization
import System.Runtime.CompilerServices
import System.IO
import System.Runtime.InteropServices

T = typing.TypeVar('T')

class MethodBase(System.Reflection.ICustomAttributeProvider, System.Reflection.MemberInfo, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    @abc.abstractmethod
    def Attributes(self) -> int:
        ...

    @property
    def MethodImplementationFlags(self) -> int:
        ...

    @property
    def CallingConvention(self) -> int:
        ...

    @property
    def IsAbstract(self) -> bool:
        ...

    @property
    def IsConstructor(self) -> bool:
        ...

    @property
    def IsFinal(self) -> bool:
        ...

    @property
    def IsHideBySig(self) -> bool:
        ...

    @property
    def IsSpecialName(self) -> bool:
        ...

    @property
    def IsStatic(self) -> bool:
        ...

    @property
    def IsVirtual(self) -> bool:
        ...

    @property
    def IsAssembly(self) -> bool:
        ...

    @property
    def IsFamily(self) -> bool:
        ...

    @property
    def IsFamilyAndAssembly(self) -> bool:
        ...

    @property
    def IsFamilyOrAssembly(self) -> bool:
        ...

    @property
    def IsPrivate(self) -> bool:
        ...

    @property
    def IsPublic(self) -> bool:
        ...

    @property
    def IsConstructedGenericMethod(self) -> bool:
        ...

    @property
    def IsGenericMethod(self) -> bool:
        ...

    @property
    def IsGenericMethodDefinition(self) -> bool:
        ...

    @property
    def ContainsGenericParameters(self) -> bool:
        ...

    @property
    @abc.abstractmethod
    def MethodHandle(self) -> System.RuntimeMethodHandle:
        ...

    @property
    def IsSecurityCritical(self) -> bool:
        ...

    @property
    def IsSecuritySafeCritical(self) -> bool:
        ...

    @property
    def IsSecurityTransparent(self) -> bool:
        ...

    @property
    @abc.abstractmethod
    def MemberType(self) -> int:
        ...

    @property
    @abc.abstractmethod
    def Name(self) -> str:
        ...

    @property
    @abc.abstractmethod
    def DeclaringType(self) -> System.Type:
        ...

    @property
    @abc.abstractmethod
    def ReflectedType(self) -> System.Type:
        ...

    @property
    def Module(self) -> System.Reflection.Module:
        ...

    @property
    def CustomAttributes(self) -> System.Collections.Generic.IEnumerable[System.Reflection.CustomAttributeData]:
        ...

    @property
    def IsCollectible(self) -> bool:
        ...

    @property
    def MetadataToken(self) -> int:
        ...

    # methods
    def __init__(self, ):
        ...

    @staticmethod
    @typing.overload
    def GetMethodFromHandle(handle: System.RuntimeMethodHandle, ) -> System.Reflection.MethodBase:
        ...

    @staticmethod
    @typing.overload
    def GetMethodFromHandle(handle: System.RuntimeMethodHandle, declaringType: System.RuntimeTypeHandle, ) -> System.Reflection.MethodBase:
        ...

    @staticmethod
    def GetCurrentMethod() -> System.Reflection.MethodBase:
        ...

    def GetMethodDesc(self, ) -> System.IntPtr:
        ...

    def GetParametersNoCopy(self, ) -> System.Array[System.Reflection.ParameterInfo]:
        ...

    def GetParameterTypes(self, ) -> System.Array[System.Type]:
        ...

    def CheckArguments(self, stackArgs: ref[System.Reflection.MethodBase.StackAllocedArguments], parameters: System.ReadOnlySpan[System.Object], binder: System.Reflection.Binder, invokeAttr: int, culture: System.Globalization.CultureInfo, sig: System.Signature, ) -> System.Span[System.Object]:
        ...

    @abc.abstractmethod
    def GetParameters(self, ) -> System.Array[System.Reflection.ParameterInfo]:
        ...

    @abc.abstractmethod
    def GetMethodImplementationFlags(self, ) -> int:
        ...

    def GetMethodBody(self, ) -> System.Reflection.MethodBody:
        ...

    def GetGenericArguments(self, ) -> System.Array[System.Type]:
        ...

    @typing.overload
    def Invoke(self, obj: System.Object, parameters: System.Array[System.Object], ) -> System.Object:
        ...

    @abc.abstractmethod
    @typing.overload
    def Invoke(self, obj: System.Object, invokeAttr: int, binder: System.Reflection.Binder, parameters: System.Array[System.Object], culture: System.Globalization.CultureInfo, ) -> System.Object:
        ...

    def Equals(self, obj: System.Object, ) -> bool:
        ...

    def GetHashCode(self, ) -> int:
        ...

    @staticmethod
    def AppendParameters(sbParamList: ref[System.Text.ValueStringBuilder], parameterTypes: System.Array[System.Type], callingConvention: int, ) -> None:
        ...

class Assembly(System.Reflection.ICustomAttributeProvider, System.Runtime.Serialization.ISerializable, System.Object, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def DefinedTypes(self) -> System.Collections.Generic.IEnumerable[System.Reflection.TypeInfo]:
        ...

    @property
    def ExportedTypes(self) -> System.Collections.Generic.IEnumerable[System.Type]:
        ...

    @property
    def CodeBase(self) -> str:
        ...

    @property
    def EntryPoint(self) -> System.Reflection.MethodInfo:
        ...

    @property
    def FullName(self) -> str:
        ...

    @property
    def ImageRuntimeVersion(self) -> str:
        ...

    @property
    def IsDynamic(self) -> bool:
        ...

    @property
    def Location(self) -> str:
        ...

    @property
    def ReflectionOnly(self) -> bool:
        ...

    @property
    def IsCollectible(self) -> bool:
        ...

    @property
    def IsFullyTrusted(self) -> bool:
        ...

    @property
    def CustomAttributes(self) -> System.Collections.Generic.IEnumerable[System.Reflection.CustomAttributeData]:
        ...

    @property
    def EscapedCodeBase(self) -> str:
        ...

    @property
    def ManifestModule(self) -> System.Reflection.Module:
        ...

    @property
    def Modules(self) -> System.Collections.Generic.IEnumerable[System.Reflection.Module]:
        ...

    @property
    def GlobalAssemblyCache(self) -> bool:
        ...

    @property
    def HostContext(self) -> int:
        ...

    @property
    def SecurityRuleSet(self) -> int:
        ...

    # methods
    def __init__(self, ):
        ...

    @staticmethod
    @typing.overload
    def Load(assemblyString: str, ) -> System.Reflection.Assembly:
        ...

    @staticmethod
    @typing.overload
    def Load(assemblyRef: System.Reflection.AssemblyName, ) -> System.Reflection.Assembly:
        ...

    @staticmethod
    @typing.overload
    def Load(rawAssembly: System.Array[int], ) -> System.Reflection.Assembly:
        ...

    @staticmethod
    @typing.overload
    def Load(rawAssembly: System.Array[int], rawSymbolStore: System.Array[int], ) -> System.Reflection.Assembly:
        ...

    @staticmethod
    def LoadWithPartialName(partialName: str, ) -> System.Reflection.Assembly:
        ...

    @staticmethod
    def GetExecutingAssemblyNative(stackMark: System.Runtime.CompilerServices.StackCrawlMarkHandle, retAssembly: System.Runtime.CompilerServices.ObjectHandleOnStack, ) -> None:
        ...

    @staticmethod
    @typing.overload
    def GetExecutingAssembly(stackMark: ref[int], ) -> System.Reflection.RuntimeAssembly:
        ...

    @staticmethod
    @typing.overload
    def GetExecutingAssembly() -> System.Reflection.Assembly:
        ...

    @staticmethod
    def GetCallingAssembly() -> System.Reflection.Assembly:
        ...

    @staticmethod
    def GetEntryAssemblyNative(retAssembly: System.Runtime.CompilerServices.ObjectHandleOnStack, ) -> None:
        ...

    @staticmethod
    def GetEntryAssemblyInternal() -> System.Reflection.Assembly:
        ...

    def IsRuntimeImplemented(self, ) -> bool:
        ...

    @staticmethod
    def GetAssemblyCount() -> int:
        ...

    def GetTypes(self, ) -> System.Array[System.Type]:
        ...

    def GetExportedTypes(self, ) -> System.Array[System.Type]:
        ...

    def GetForwardedTypes(self, ) -> System.Array[System.Type]:
        ...

    def GetManifestResourceInfo(self, resourceName: str, ) -> System.Reflection.ManifestResourceInfo:
        ...

    def GetManifestResourceNames(self, ) -> System.Array[str]:
        ...

    @typing.overload
    def GetManifestResourceStream(self, name: str, ) -> System.IO.Stream:
        ...

    @typing.overload
    def GetManifestResourceStream(self, type: System.Type, name: str, ) -> System.IO.Stream:
        ...

    @typing.overload
    def GetName(self, ) -> System.Reflection.AssemblyName:
        ...

    @typing.overload
    def GetName(self, copiedName: bool, ) -> System.Reflection.AssemblyName:
        ...

    @typing.overload
    def GetType(self, name: str, ) -> System.Type:
        ...

    @typing.overload
    def GetType(self, name: str, throwOnError: bool, ) -> System.Type:
        ...

    @typing.overload
    def GetType(self, name: str, throwOnError: bool, ignoreCase: bool, ) -> System.Type:
        ...

    def IsDefined(self, attributeType: System.Type, inherit: bool, ) -> bool:
        ...

    def GetCustomAttributesData(self, ) -> System.Collections.Generic.IList[System.Reflection.CustomAttributeData]:
        ...

    @typing.overload
    def GetCustomAttributes(self, inherit: bool, ) -> System.Array[System.Object]:
        ...

    @typing.overload
    def GetCustomAttributes(self, attributeType: System.Type, inherit: bool, ) -> System.Array[System.Object]:
        ...

    @typing.overload
    def CreateInstance(self, typeName: str, ) -> System.Object:
        ...

    @typing.overload
    def CreateInstance(self, typeName: str, ignoreCase: bool, ) -> System.Object:
        ...

    @typing.overload
    def CreateInstance(self, typeName: str, ignoreCase: bool, bindingAttr: int, binder: System.Reflection.Binder, args: System.Array[System.Object], culture: System.Globalization.CultureInfo, activationAttributes: System.Array[System.Object], ) -> System.Object:
        ...

    def GetModule(self, name: str, ) -> System.Reflection.Module:
        ...

    @typing.overload
    def GetModules(self, ) -> System.Array[System.Reflection.Module]:
        ...

    @typing.overload
    def GetModules(self, getResourceModules: bool, ) -> System.Array[System.Reflection.Module]:
        ...

    @typing.overload
    def GetLoadedModules(self, ) -> System.Array[System.Reflection.Module]:
        ...

    @typing.overload
    def GetLoadedModules(self, getResourceModules: bool, ) -> System.Array[System.Reflection.Module]:
        ...

    def GetReferencedAssemblies(self, ) -> System.Array[System.Reflection.AssemblyName]:
        ...

    @typing.overload
    def GetSatelliteAssembly(self, culture: System.Globalization.CultureInfo, ) -> System.Reflection.Assembly:
        ...

    @typing.overload
    def GetSatelliteAssembly(self, culture: System.Globalization.CultureInfo, version: System.Version, ) -> System.Reflection.Assembly:
        ...

    def GetFile(self, name: str, ) -> System.IO.FileStream:
        ...

    @typing.overload
    def GetFiles(self, ) -> System.Array[System.IO.FileStream]:
        ...

    @typing.overload
    def GetFiles(self, getResourceModules: bool, ) -> System.Array[System.IO.FileStream]:
        ...

    def GetObjectData(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext, ) -> None:
        ...

    def ToString(self, ) -> str:
        ...

    def Equals(self, o: System.Object, ) -> bool:
        ...

    def GetHashCode(self, ) -> int:
        ...

    @staticmethod
    def CreateQualifiedName(assemblyName: str, typeName: str, ) -> str:
        ...

    @staticmethod
    def GetAssembly(type: System.Type, ) -> System.Reflection.Assembly:
        ...

    @staticmethod
    def GetEntryAssembly() -> System.Reflection.Assembly:
        ...

    @staticmethod
    def LoadFile(path: str, ) -> System.Reflection.Assembly:
        ...

    @staticmethod
    def LoadFromResolveHandler(sender: System.Object, args: System.ResolveEventArgs, ) -> System.Reflection.Assembly:
        ...

    @staticmethod
    @typing.overload
    def LoadFrom(assemblyFile: str, ) -> System.Reflection.Assembly:
        ...

    @staticmethod
    @typing.overload
    def LoadFrom(assemblyFile: str, hashValue: System.Array[int], hashAlgorithm: int, ) -> System.Reflection.Assembly:
        ...

    @staticmethod
    def UnsafeLoadFrom(assemblyFile: str, ) -> System.Reflection.Assembly:
        ...

    @typing.overload
    def LoadModule(self, moduleName: str, rawModule: System.Array[int], ) -> System.Reflection.Module:
        ...

    @typing.overload
    def LoadModule(self, moduleName: str, rawModule: System.Array[int], rawSymbolStore: System.Array[int], ) -> System.Reflection.Module:
        ...

    @staticmethod
    @typing.overload
    def ReflectionOnlyLoad(rawAssembly: System.Array[int], ) -> System.Reflection.Assembly:
        ...

    @staticmethod
    @typing.overload
    def ReflectionOnlyLoad(assemblyString: str, ) -> System.Reflection.Assembly:
        ...

    @staticmethod
    def ReflectionOnlyLoadFrom(assemblyFile: str, ) -> System.Reflection.Assembly:
        ...

class FieldInfo(System.Reflection.ICustomAttributeProvider, System.Reflection.MemberInfo, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def MemberType(self) -> int:
        ...

    @property
    @abc.abstractmethod
    def Attributes(self) -> int:
        ...

    @property
    @abc.abstractmethod
    def FieldType(self) -> System.Type:
        ...

    @property
    def IsInitOnly(self) -> bool:
        ...

    @property
    def IsLiteral(self) -> bool:
        ...

    @property
    def IsNotSerialized(self) -> bool:
        ...

    @property
    def IsPinvokeImpl(self) -> bool:
        ...

    @property
    def IsSpecialName(self) -> bool:
        ...

    @property
    def IsStatic(self) -> bool:
        ...

    @property
    def IsAssembly(self) -> bool:
        ...

    @property
    def IsFamily(self) -> bool:
        ...

    @property
    def IsFamilyAndAssembly(self) -> bool:
        ...

    @property
    def IsFamilyOrAssembly(self) -> bool:
        ...

    @property
    def IsPrivate(self) -> bool:
        ...

    @property
    def IsPublic(self) -> bool:
        ...

    @property
    def IsSecurityCritical(self) -> bool:
        ...

    @property
    def IsSecuritySafeCritical(self) -> bool:
        ...

    @property
    def IsSecurityTransparent(self) -> bool:
        ...

    @property
    @abc.abstractmethod
    def FieldHandle(self) -> System.RuntimeFieldHandle:
        ...

    @property
    @abc.abstractmethod
    def Name(self) -> str:
        ...

    @property
    @abc.abstractmethod
    def DeclaringType(self) -> System.Type:
        ...

    @property
    @abc.abstractmethod
    def ReflectedType(self) -> System.Type:
        ...

    @property
    def Module(self) -> System.Reflection.Module:
        ...

    @property
    def CustomAttributes(self) -> System.Collections.Generic.IEnumerable[System.Reflection.CustomAttributeData]:
        ...

    @property
    def IsCollectible(self) -> bool:
        ...

    @property
    def MetadataToken(self) -> int:
        ...

    # methods
    def __init__(self, ):
        ...

    @staticmethod
    @typing.overload
    def GetFieldFromHandle(handle: System.RuntimeFieldHandle, ) -> System.Reflection.FieldInfo:
        ...

    @staticmethod
    @typing.overload
    def GetFieldFromHandle(handle: System.RuntimeFieldHandle, declaringType: System.RuntimeTypeHandle, ) -> System.Reflection.FieldInfo:
        ...

    def Equals(self, obj: System.Object, ) -> bool:
        ...

    def GetHashCode(self, ) -> int:
        ...

    @abc.abstractmethod
    def GetValue(self, obj: System.Object, ) -> System.Object:
        ...

    @typing.overload
    def SetValue(self, obj: System.Object, value: System.Object, ) -> None:
        ...

    @abc.abstractmethod
    @typing.overload
    def SetValue(self, obj: System.Object, value: System.Object, invokeAttr: int, binder: System.Reflection.Binder, culture: System.Globalization.CultureInfo, ) -> None:
        ...

    def SetValueDirect(self, obj: System.TypedReference, value: System.Object, ) -> None:
        ...

    def GetValueDirect(self, obj: System.TypedReference, ) -> System.Object:
        ...

    def GetRawConstantValue(self, ) -> System.Object:
        ...

    def GetOptionalCustomModifiers(self, ) -> System.Array[System.Type]:
        ...

    def GetRequiredCustomModifiers(self, ) -> System.Array[System.Type]:
        ...

class EventInfo(System.Reflection.ICustomAttributeProvider, System.Reflection.MemberInfo, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def MemberType(self) -> int:
        ...

    @property
    @abc.abstractmethod
    def Attributes(self) -> int:
        ...

    @property
    def IsSpecialName(self) -> bool:
        ...

    @property
    def AddMethod(self) -> System.Reflection.MethodInfo:
        ...

    @property
    def RemoveMethod(self) -> System.Reflection.MethodInfo:
        ...

    @property
    def RaiseMethod(self) -> System.Reflection.MethodInfo:
        ...

    @property
    def IsMulticast(self) -> bool:
        ...

    @property
    def EventHandlerType(self) -> System.Type:
        ...

    @property
    @abc.abstractmethod
    def Name(self) -> str:
        ...

    @property
    @abc.abstractmethod
    def DeclaringType(self) -> System.Type:
        ...

    @property
    @abc.abstractmethod
    def ReflectedType(self) -> System.Type:
        ...

    @property
    def Module(self) -> System.Reflection.Module:
        ...

    @property
    def CustomAttributes(self) -> System.Collections.Generic.IEnumerable[System.Reflection.CustomAttributeData]:
        ...

    @property
    def IsCollectible(self) -> bool:
        ...

    @property
    def MetadataToken(self) -> int:
        ...

    # methods
    def __init__(self, ):
        ...

    @typing.overload
    def GetOtherMethods(self, ) -> System.Array[System.Reflection.MethodInfo]:
        ...

    @typing.overload
    def GetOtherMethods(self, nonPublic: bool, ) -> System.Array[System.Reflection.MethodInfo]:
        ...

    @typing.overload
    def GetAddMethod(self, ) -> System.Reflection.MethodInfo:
        ...

    @abc.abstractmethod
    @typing.overload
    def GetAddMethod(self, nonPublic: bool, ) -> System.Reflection.MethodInfo:
        ...

    @typing.overload
    def GetRemoveMethod(self, ) -> System.Reflection.MethodInfo:
        ...

    @abc.abstractmethod
    @typing.overload
    def GetRemoveMethod(self, nonPublic: bool, ) -> System.Reflection.MethodInfo:
        ...

    @typing.overload
    def GetRaiseMethod(self, ) -> System.Reflection.MethodInfo:
        ...

    @abc.abstractmethod
    @typing.overload
    def GetRaiseMethod(self, nonPublic: bool, ) -> System.Reflection.MethodInfo:
        ...

    def AddEventHandler(self, target: System.Object, handler: System.Delegate, ) -> None:
        ...

    def RemoveEventHandler(self, target: System.Object, handler: System.Delegate, ) -> None:
        ...

    def Equals(self, obj: System.Object, ) -> bool:
        ...

    def GetHashCode(self, ) -> int:
        ...

class Module(System.Reflection.ICustomAttributeProvider, System.Runtime.Serialization.ISerializable, System.Object, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields
    FilterTypeName: System.Reflection.TypeFilter = ...
    FilterTypeNameIgnoreCase: System.Reflection.TypeFilter = ...

    # properties
    @property
    def Assembly(self) -> System.Reflection.Assembly:
        ...

    @property
    def FullyQualifiedName(self) -> str:
        ...

    @property
    def Name(self) -> str:
        ...

    @property
    def MDStreamVersion(self) -> int:
        ...

    @property
    def ModuleVersionId(self) -> System.Guid:
        ...

    @property
    def ScopeName(self) -> str:
        ...

    @property
    def ModuleHandle(self) -> System.ModuleHandle:
        ...

    @property
    def CustomAttributes(self) -> System.Collections.Generic.IEnumerable[System.Reflection.CustomAttributeData]:
        ...

    @property
    def MetadataToken(self) -> int:
        ...

    # methods
    def __init__(self, ):
        ...

    def GetModuleHandleImpl(self, ) -> System.ModuleHandle:
        ...

    def GetPEKind(self, peKind: ref[int], machine: ref[int], ) -> None:
        ...

    def IsResource(self, ) -> bool:
        ...

    def IsDefined(self, attributeType: System.Type, inherit: bool, ) -> bool:
        ...

    def GetCustomAttributesData(self, ) -> System.Collections.Generic.IList[System.Reflection.CustomAttributeData]:
        ...

    @typing.overload
    def GetCustomAttributes(self, inherit: bool, ) -> System.Array[System.Object]:
        ...

    @typing.overload
    def GetCustomAttributes(self, attributeType: System.Type, inherit: bool, ) -> System.Array[System.Object]:
        ...

    @typing.overload
    def GetMethod(self, name: str, ) -> System.Reflection.MethodInfo:
        ...

    @typing.overload
    def GetMethod(self, name: str, types: System.Array[System.Type], ) -> System.Reflection.MethodInfo:
        ...

    @typing.overload
    def GetMethod(self, name: str, bindingAttr: int, binder: System.Reflection.Binder, callConvention: int, types: System.Array[System.Type], modifiers: System.Array[System.Reflection.ParameterModifier], ) -> System.Reflection.MethodInfo:
        ...

    def GetMethodImpl(self, name: str, bindingAttr: int, binder: System.Reflection.Binder, callConvention: int, types: System.Array[System.Type], modifiers: System.Array[System.Reflection.ParameterModifier], ) -> System.Reflection.MethodInfo:
        ...

    @typing.overload
    def GetMethods(self, ) -> System.Array[System.Reflection.MethodInfo]:
        ...

    @typing.overload
    def GetMethods(self, bindingFlags: int, ) -> System.Array[System.Reflection.MethodInfo]:
        ...

    @typing.overload
    def GetField(self, name: str, ) -> System.Reflection.FieldInfo:
        ...

    @typing.overload
    def GetField(self, name: str, bindingAttr: int, ) -> System.Reflection.FieldInfo:
        ...

    @typing.overload
    def GetFields(self, ) -> System.Array[System.Reflection.FieldInfo]:
        ...

    @typing.overload
    def GetFields(self, bindingFlags: int, ) -> System.Array[System.Reflection.FieldInfo]:
        ...

    def GetTypes(self, ) -> System.Array[System.Type]:
        ...

    @typing.overload
    def GetType(self, className: str, ) -> System.Type:
        ...

    @typing.overload
    def GetType(self, className: str, ignoreCase: bool, ) -> System.Type:
        ...

    @typing.overload
    def GetType(self, className: str, throwOnError: bool, ignoreCase: bool, ) -> System.Type:
        ...

    def FindTypes(self, filter: System.Reflection.TypeFilter, filterCriteria: System.Object, ) -> System.Array[System.Type]:
        ...

    @typing.overload
    def ResolveField(self, metadataToken: int, ) -> System.Reflection.FieldInfo:
        ...

    @typing.overload
    def ResolveField(self, metadataToken: int, genericTypeArguments: System.Array[System.Type], genericMethodArguments: System.Array[System.Type], ) -> System.Reflection.FieldInfo:
        ...

    @typing.overload
    def ResolveMember(self, metadataToken: int, ) -> System.Reflection.MemberInfo:
        ...

    @typing.overload
    def ResolveMember(self, metadataToken: int, genericTypeArguments: System.Array[System.Type], genericMethodArguments: System.Array[System.Type], ) -> System.Reflection.MemberInfo:
        ...

    @typing.overload
    def ResolveMethod(self, metadataToken: int, ) -> System.Reflection.MethodBase:
        ...

    @typing.overload
    def ResolveMethod(self, metadataToken: int, genericTypeArguments: System.Array[System.Type], genericMethodArguments: System.Array[System.Type], ) -> System.Reflection.MethodBase:
        ...

    def ResolveSignature(self, metadataToken: int, ) -> System.Array[int]:
        ...

    def ResolveString(self, metadataToken: int, ) -> str:
        ...

    @typing.overload
    def ResolveType(self, metadataToken: int, ) -> System.Type:
        ...

    @typing.overload
    def ResolveType(self, metadataToken: int, genericTypeArguments: System.Array[System.Type], genericMethodArguments: System.Array[System.Type], ) -> System.Type:
        ...

    def GetObjectData(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext, ) -> None:
        ...

    def Equals(self, o: System.Object, ) -> bool:
        ...

    def GetHashCode(self, ) -> int:
        ...

    def ToString(self, ) -> str:
        ...

    @staticmethod
    def FilterTypeNameImpl(cls: System.Type, filterCriteria: System.Object, comparison: int, ) -> bool:
        ...

class ImageFileMachine(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    I386: int = ...
    ARM: int = ...
    IA64: int = ...
    AMD64: int = ...

class EventAttributes(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    None_: int = ...
    SpecialName: int = ...
    RTSpecialName: int = ...
    ReservedMask: int = ...

class ParameterAttributes(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    None_: int = ...
    In: int = ...
    Out: int = ...
    Lcid: int = ...
    Retval: int = ...
    Optional: int = ...
    HasDefault: int = ...
    HasFieldMarshal: int = ...
    Reserved3: int = ...
    Reserved4: int = ...
    ReservedMask: int = ...

class PropertyAttributes(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    None_: int = ...
    SpecialName: int = ...
    RTSpecialName: int = ...
    HasDefault: int = ...
    Reserved2: int = ...
    Reserved3: int = ...
    Reserved4: int = ...
    ReservedMask: int = ...

class MethodImplAttributes(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    IL: int = ...
    Managed: int = ...
    Native: int = ...
    OPTIL: int = ...
    Runtime: int = ...
    CodeTypeMask: int = ...
    Unmanaged: int = ...
    ManagedMask: int = ...
    NoInlining: int = ...
    ForwardRef: int = ...
    Synchronized: int = ...
    NoOptimization: int = ...
    PreserveSig: int = ...
    AggressiveInlining: int = ...
    AggressiveOptimization: int = ...
    InternalCall: int = ...
    MaxMethodImplVal: int = ...

class TypeFilter(System.ICloneable, System.Runtime.Serialization.ISerializable, System.MulticastDelegate):
    @typing.overload
    def __init__(self, **kwargs):
        self._target: System.Object
        self._methodBase: System.Object
        self._methodPtr: System.IntPtr
        self._methodPtrAux: System.IntPtr
        ...

    # static fields

    # properties
    @property
    def Target(self) -> System.Object:
        ...

    @property
    def Method(self) -> System.Reflection.MethodInfo:
        ...

    # methods
    def __init__(self, object: System.Object, method: System.IntPtr, ):
        ...

    def Invoke(self, m: System.Type, filterCriteria: System.Object, ) -> bool:
        ...

    def BeginInvoke(self, m: System.Type, filterCriteria: System.Object, callback: System.AsyncCallback, object: System.Object, ) -> System.IAsyncResult:
        ...

    def EndInvoke(self, result: System.IAsyncResult, ) -> bool:
        ...

class MethodInfo(System.Reflection.ICustomAttributeProvider, System.Reflection.MethodBase, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def MemberType(self) -> int:
        ...

    @property
    def ReturnParameter(self) -> System.Reflection.ParameterInfo:
        ...

    @property
    def ReturnType(self) -> System.Type:
        ...

    @property
    @abc.abstractmethod
    def ReturnTypeCustomAttributes(self) -> System.Reflection.ICustomAttributeProvider:
        ...

    @property
    def GenericParameterCount(self) -> int:
        ...

    @property
    @abc.abstractmethod
    def Attributes(self) -> int:
        ...

    @property
    def MethodImplementationFlags(self) -> int:
        ...

    @property
    def CallingConvention(self) -> int:
        ...

    @property
    def IsAbstract(self) -> bool:
        ...

    @property
    def IsConstructor(self) -> bool:
        ...

    @property
    def IsFinal(self) -> bool:
        ...

    @property
    def IsHideBySig(self) -> bool:
        ...

    @property
    def IsSpecialName(self) -> bool:
        ...

    @property
    def IsStatic(self) -> bool:
        ...

    @property
    def IsVirtual(self) -> bool:
        ...

    @property
    def IsAssembly(self) -> bool:
        ...

    @property
    def IsFamily(self) -> bool:
        ...

    @property
    def IsFamilyAndAssembly(self) -> bool:
        ...

    @property
    def IsFamilyOrAssembly(self) -> bool:
        ...

    @property
    def IsPrivate(self) -> bool:
        ...

    @property
    def IsPublic(self) -> bool:
        ...

    @property
    def IsConstructedGenericMethod(self) -> bool:
        ...

    @property
    def IsGenericMethod(self) -> bool:
        ...

    @property
    def IsGenericMethodDefinition(self) -> bool:
        ...

    @property
    def ContainsGenericParameters(self) -> bool:
        ...

    @property
    @abc.abstractmethod
    def MethodHandle(self) -> System.RuntimeMethodHandle:
        ...

    @property
    def IsSecurityCritical(self) -> bool:
        ...

    @property
    def IsSecuritySafeCritical(self) -> bool:
        ...

    @property
    def IsSecurityTransparent(self) -> bool:
        ...

    @property
    @abc.abstractmethod
    def Name(self) -> str:
        ...

    @property
    @abc.abstractmethod
    def DeclaringType(self) -> System.Type:
        ...

    @property
    @abc.abstractmethod
    def ReflectedType(self) -> System.Type:
        ...

    @property
    def Module(self) -> System.Reflection.Module:
        ...

    @property
    def CustomAttributes(self) -> System.Collections.Generic.IEnumerable[System.Reflection.CustomAttributeData]:
        ...

    @property
    def IsCollectible(self) -> bool:
        ...

    @property
    def MetadataToken(self) -> int:
        ...

    # methods
    def __init__(self, ):
        ...

    def GetGenericArguments(self, ) -> System.Array[System.Type]:
        ...

    def GetGenericMethodDefinition(self, ) -> System.Reflection.MethodInfo:
        ...

    def MakeGenericMethod(self, typeArguments: System.Array[System.Type], ) -> System.Reflection.MethodInfo:
        ...

    @abc.abstractmethod
    def GetBaseDefinition(self, ) -> System.Reflection.MethodInfo:
        ...

    @typing.overload
    def CreateDelegate(self, delegateType: System.Type, ) -> System.Delegate:
        ...

    @typing.overload
    def CreateDelegate(self, delegateType: System.Type, target: System.Object, ) -> System.Delegate:
        ...

    @typing.overload
    def CreateDelegate(self, ) -> T:
        ...

    @typing.overload
    def CreateDelegate(self, target: System.Object, ) -> T:
        ...

    def Equals(self, obj: System.Object, ) -> bool:
        ...

    def GetHashCode(self, ) -> int:
        ...

class PropertyInfo(System.Reflection.ICustomAttributeProvider, System.Reflection.MemberInfo, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def MemberType(self) -> int:
        ...

    @property
    @abc.abstractmethod
    def PropertyType(self) -> System.Type:
        ...

    @property
    @abc.abstractmethod
    def Attributes(self) -> int:
        ...

    @property
    def IsSpecialName(self) -> bool:
        ...

    @property
    @abc.abstractmethod
    def CanRead(self) -> bool:
        ...

    @property
    @abc.abstractmethod
    def CanWrite(self) -> bool:
        ...

    @property
    def GetMethod(self) -> System.Reflection.MethodInfo:
        ...

    @property
    def SetMethod(self) -> System.Reflection.MethodInfo:
        ...

    @property
    @abc.abstractmethod
    def Name(self) -> str:
        ...

    @property
    @abc.abstractmethod
    def DeclaringType(self) -> System.Type:
        ...

    @property
    @abc.abstractmethod
    def ReflectedType(self) -> System.Type:
        ...

    @property
    def Module(self) -> System.Reflection.Module:
        ...

    @property
    def CustomAttributes(self) -> System.Collections.Generic.IEnumerable[System.Reflection.CustomAttributeData]:
        ...

    @property
    def IsCollectible(self) -> bool:
        ...

    @property
    def MetadataToken(self) -> int:
        ...

    # methods
    def __init__(self, ):
        ...

    @typing.overload
    def GetValue(self, obj: System.Object, index: System.Array[System.Object], ) -> System.Object:
        ...

    @abc.abstractmethod
    @typing.overload
    def GetValue(self, obj: System.Object, invokeAttr: int, binder: System.Reflection.Binder, index: System.Array[System.Object], culture: System.Globalization.CultureInfo, ) -> System.Object:
        ...

    @typing.overload
    def GetValue(self, obj: System.Object, ) -> System.Object:
        ...

    @typing.overload
    def SetValue(self, obj: System.Object, value: System.Object, index: System.Array[System.Object], ) -> None:
        ...

    @abc.abstractmethod
    @typing.overload
    def SetValue(self, obj: System.Object, value: System.Object, invokeAttr: int, binder: System.Reflection.Binder, index: System.Array[System.Object], culture: System.Globalization.CultureInfo, ) -> None:
        ...

    @typing.overload
    def SetValue(self, obj: System.Object, value: System.Object, ) -> None:
        ...

    @abc.abstractmethod
    @typing.overload
    def GetAccessors(self, nonPublic: bool, ) -> System.Array[System.Reflection.MethodInfo]:
        ...

    @typing.overload
    def GetAccessors(self, ) -> System.Array[System.Reflection.MethodInfo]:
        ...

    @abc.abstractmethod
    @typing.overload
    def GetGetMethod(self, nonPublic: bool, ) -> System.Reflection.MethodInfo:
        ...

    @typing.overload
    def GetGetMethod(self, ) -> System.Reflection.MethodInfo:
        ...

    @abc.abstractmethod
    @typing.overload
    def GetSetMethod(self, nonPublic: bool, ) -> System.Reflection.MethodInfo:
        ...

    @typing.overload
    def GetSetMethod(self, ) -> System.Reflection.MethodInfo:
        ...

    @abc.abstractmethod
    def GetIndexParameters(self, ) -> System.Array[System.Reflection.ParameterInfo]:
        ...

    def GetOptionalCustomModifiers(self, ) -> System.Array[System.Type]:
        ...

    def GetRequiredCustomModifiers(self, ) -> System.Array[System.Type]:
        ...

    def GetConstantValue(self, ) -> System.Object:
        ...

    def GetRawConstantValue(self, ) -> System.Object:
        ...

    def Equals(self, obj: System.Object, ) -> bool:
        ...

    def GetHashCode(self, ) -> int:
        ...

class Binder(System.Object, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    def __init__(self, ):
        ...

    @abc.abstractmethod
    def BindToField(self, bindingAttr: int, match: System.Array[System.Reflection.FieldInfo], value: System.Object, culture: System.Globalization.CultureInfo, ) -> System.Reflection.FieldInfo:
        ...

    @abc.abstractmethod
    def BindToMethod(self, bindingAttr: int, match: System.Array[System.Reflection.MethodBase], args: ref[System.Array[System.Object]], modifiers: System.Array[System.Reflection.ParameterModifier], culture: System.Globalization.CultureInfo, names: System.Array[str], state: ref[System.Object], ) -> System.Reflection.MethodBase:
        ...

    @abc.abstractmethod
    def ChangeType(self, value: System.Object, type: System.Type, culture: System.Globalization.CultureInfo, ) -> System.Object:
        ...

    @abc.abstractmethod
    def ReorderArgumentArray(self, args: ref[System.Array[System.Object]], state: System.Object, ) -> None:
        ...

    @abc.abstractmethod
    def SelectMethod(self, bindingAttr: int, match: System.Array[System.Reflection.MethodBase], types: System.Array[System.Type], modifiers: System.Array[System.Reflection.ParameterModifier], ) -> System.Reflection.MethodBase:
        ...

    @abc.abstractmethod
    def SelectProperty(self, bindingAttr: int, match: System.Array[System.Reflection.PropertyInfo], returnType: System.Type, indexes: System.Array[System.Type], modifiers: System.Array[System.Reflection.ParameterModifier], ) -> System.Reflection.PropertyInfo:
        ...

class AssemblyName(System.ICloneable, System.Runtime.Serialization.IDeserializationCallback, System.Runtime.Serialization.ISerializable, System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields
    c_DummyChar: str = ...

    # properties
    @property
    def Name(self) -> str:
        ...
    @Name.setter
    def Name(self, val: str):
        ...

    @property
    def Version(self) -> System.Version:
        ...
    @Version.setter
    def Version(self, val: System.Version):
        ...

    @property
    def CultureInfo(self) -> System.Globalization.CultureInfo:
        ...
    @CultureInfo.setter
    def CultureInfo(self, val: System.Globalization.CultureInfo):
        ...

    @property
    def CultureName(self) -> str:
        ...
    @CultureName.setter
    def CultureName(self, val: str):
        ...

    @property
    def CodeBase(self) -> str:
        ...
    @CodeBase.setter
    def CodeBase(self, val: str):
        ...

    @property
    def EscapedCodeBase(self) -> str:
        ...

    @property
    def ProcessorArchitecture(self) -> int:
        ...
    @ProcessorArchitecture.setter
    def ProcessorArchitecture(self, val: int):
        ...

    @property
    def ContentType(self) -> int:
        ...
    @ContentType.setter
    def ContentType(self, val: int):
        ...

    @property
    def Flags(self) -> int:
        ...
    @Flags.setter
    def Flags(self, val: int):
        ...

    @property
    def HashAlgorithm(self) -> int:
        ...
    @HashAlgorithm.setter
    def HashAlgorithm(self, val: int):
        ...

    @property
    def VersionCompatibility(self) -> int:
        ...
    @VersionCompatibility.setter
    def VersionCompatibility(self, val: int):
        ...

    @property
    def KeyPair(self) -> System.Reflection.StrongNameKeyPair:
        ...
    @KeyPair.setter
    def KeyPair(self, val: System.Reflection.StrongNameKeyPair):
        ...

    @property
    def FullName(self) -> str:
        ...

    # methods
    @typing.overload
    def __init__(self, assemblyName: str, ):
        ...

    @typing.overload
    def __init__(self, name: str, publicKey: System.Array[int], publicKeyToken: System.Array[int], version: System.Version, cultureInfo: System.Globalization.CultureInfo, hashAlgorithm: int, versionCompatibility: int, codeBase: str, flags: int, ):
        ...

    @typing.overload
    def __init__(self, ):
        ...

    def nInit(self, ) -> None:
        ...

    @staticmethod
    def nGetFileInformation(s: str, ) -> System.Reflection.AssemblyName:
        ...

    @staticmethod
    def GetFileInformationCore(assemblyFile: str, ) -> System.Reflection.AssemblyName:
        ...

    def ComputePublicKeyToken(self, ) -> System.Array[int]:
        ...

    def SetProcArchIndex(self, pek: int, ifm: int, ) -> None:
        ...

    @staticmethod
    def CalculateProcArchIndex(pek: int, ifm: int, flags: int, ) -> int:
        ...

    def Clone(self, ) -> System.Object:
        ...

    @staticmethod
    def GetAssemblyName(assemblyFile: str, ) -> System.Reflection.AssemblyName:
        ...

    def GetPublicKey(self, ) -> System.Array[int]:
        ...

    def SetPublicKey(self, publicKey: System.Array[int], ) -> None:
        ...

    def GetPublicKeyToken(self, ) -> System.Array[int]:
        ...

    def SetPublicKeyToken(self, publicKeyToken: System.Array[int], ) -> None:
        ...

    def ToString(self, ) -> str:
        ...

    def GetObjectData(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext, ) -> None:
        ...

    def OnDeserialization(self, sender: System.Object, ) -> None:
        ...

    @staticmethod
    def ReferenceMatchesDefinition(reference: System.Reflection.AssemblyName, definition: System.Reflection.AssemblyName, ) -> bool:
        ...

    @staticmethod
    def EscapeCodeBase(codebase: str, ) -> str:
        ...

    @staticmethod
    def EscapeString(input: str, start: int, end: int, dest: System.Array[str], destPos: ref[int], isUriString: bool, force1: str, force2: str, rsvd: str, ) -> System.Array[str]:
        ...

    @staticmethod
    def EnsureDestinationSize(pStr: ptr[str], dest: System.Array[str], currentInputPos: int, charsToAdd: int, minReallocateChars: int, destPos: ref[int], prevInputPos: int, ) -> System.Array[str]:
        ...

    @staticmethod
    def EscapeAsciiChar(ch: str, to: System.Array[str], pos: ref[int], ) -> None:
        ...

    @staticmethod
    def IsReservedUnreservedOrHash(c: str, ) -> bool:
        ...

    @staticmethod
    def IsUnreserved(c: str, ) -> bool:
        ...

    @staticmethod
    def IsAsciiLetter(character: str, ) -> bool:
        ...

    @staticmethod
    def IsAsciiLetterOrDigit(character: str, ) -> bool:
        ...

class AssemblyNameFlags(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    None_: int = ...
    PublicKey: int = ...
    Retargetable: int = ...
    EnableJITcompileOptimizer: int = ...
    EnableJITcompileTracking: int = ...

class AssemblyContentType(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    Default: int = ...
    WindowsRuntime: int = ...

class ProcessorArchitecture(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    None_: int = ...
    MSIL: int = ...
    X86: int = ...
    IA64: int = ...
    Amd64: int = ...
    Arm: int = ...

class ParameterInfo(System.Reflection.ICustomAttributeProvider, System.Runtime.Serialization.IObjectReference, System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        self.AttrsImpl: int
        self.ClassImpl: System.Type
        self.DefaultValueImpl: System.Object
        self.MemberImpl: System.Reflection.MemberInfo
        self.NameImpl: str
        self.PositionImpl: int
        ...

    # static fields

    # properties
    @property
    def Attributes(self) -> int:
        ...

    @property
    def Member(self) -> System.Reflection.MemberInfo:
        ...

    @property
    def Name(self) -> str:
        ...

    @property
    def ParameterType(self) -> System.Type:
        ...

    @property
    def Position(self) -> int:
        ...

    @property
    def IsIn(self) -> bool:
        ...

    @property
    def IsLcid(self) -> bool:
        ...

    @property
    def IsOptional(self) -> bool:
        ...

    @property
    def IsOut(self) -> bool:
        ...

    @property
    def IsRetval(self) -> bool:
        ...

    @property
    def DefaultValue(self) -> System.Object:
        ...

    @property
    def RawDefaultValue(self) -> System.Object:
        ...

    @property
    def HasDefaultValue(self) -> bool:
        ...

    @property
    def CustomAttributes(self) -> System.Collections.Generic.IEnumerable[System.Reflection.CustomAttributeData]:
        ...

    @property
    def MetadataToken(self) -> int:
        ...

    # methods
    def __init__(self, ):
        ...

    def IsDefined(self, attributeType: System.Type, inherit: bool, ) -> bool:
        ...

    def GetCustomAttributesData(self, ) -> System.Collections.Generic.IList[System.Reflection.CustomAttributeData]:
        ...

    @typing.overload
    def GetCustomAttributes(self, inherit: bool, ) -> System.Array[System.Object]:
        ...

    @typing.overload
    def GetCustomAttributes(self, attributeType: System.Type, inherit: bool, ) -> System.Array[System.Object]:
        ...

    def GetOptionalCustomModifiers(self, ) -> System.Array[System.Type]:
        ...

    def GetRequiredCustomModifiers(self, ) -> System.Array[System.Type]:
        ...

    def GetRealObject(self, context: System.Runtime.Serialization.StreamingContext, ) -> System.Object:
        ...

    def ToString(self, ) -> str:
        ...

class IReflectableType(abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    @abc.abstractmethod
    def GetTypeInfo(self, ) -> System.Reflection.TypeInfo:
        ...

class PortableExecutableKinds(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    NotAPortableExecutableImage: int = ...
    ILOnly: int = ...
    Required32Bit: int = ...
    PE32Plus: int = ...
    Unmanaged32Bit: int = ...
    Preferred32Bit: int = ...

class CallingConventions(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    Standard: int = ...
    VarArgs: int = ...
    Any: int = ...
    HasThis: int = ...
    ExplicitThis: int = ...

class ConstructorInfo(System.Reflection.ICustomAttributeProvider, System.Reflection.MethodBase, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields
    ConstructorName: str = ...
    TypeConstructorName: str = ...

    # properties
    @property
    def MemberType(self) -> int:
        ...

    @property
    @abc.abstractmethod
    def Attributes(self) -> int:
        ...

    @property
    def MethodImplementationFlags(self) -> int:
        ...

    @property
    def CallingConvention(self) -> int:
        ...

    @property
    def IsAbstract(self) -> bool:
        ...

    @property
    def IsConstructor(self) -> bool:
        ...

    @property
    def IsFinal(self) -> bool:
        ...

    @property
    def IsHideBySig(self) -> bool:
        ...

    @property
    def IsSpecialName(self) -> bool:
        ...

    @property
    def IsStatic(self) -> bool:
        ...

    @property
    def IsVirtual(self) -> bool:
        ...

    @property
    def IsAssembly(self) -> bool:
        ...

    @property
    def IsFamily(self) -> bool:
        ...

    @property
    def IsFamilyAndAssembly(self) -> bool:
        ...

    @property
    def IsFamilyOrAssembly(self) -> bool:
        ...

    @property
    def IsPrivate(self) -> bool:
        ...

    @property
    def IsPublic(self) -> bool:
        ...

    @property
    def IsConstructedGenericMethod(self) -> bool:
        ...

    @property
    def IsGenericMethod(self) -> bool:
        ...

    @property
    def IsGenericMethodDefinition(self) -> bool:
        ...

    @property
    def ContainsGenericParameters(self) -> bool:
        ...

    @property
    @abc.abstractmethod
    def MethodHandle(self) -> System.RuntimeMethodHandle:
        ...

    @property
    def IsSecurityCritical(self) -> bool:
        ...

    @property
    def IsSecuritySafeCritical(self) -> bool:
        ...

    @property
    def IsSecurityTransparent(self) -> bool:
        ...

    @property
    @abc.abstractmethod
    def Name(self) -> str:
        ...

    @property
    @abc.abstractmethod
    def DeclaringType(self) -> System.Type:
        ...

    @property
    @abc.abstractmethod
    def ReflectedType(self) -> System.Type:
        ...

    @property
    def Module(self) -> System.Reflection.Module:
        ...

    @property
    def CustomAttributes(self) -> System.Collections.Generic.IEnumerable[System.Reflection.CustomAttributeData]:
        ...

    @property
    def IsCollectible(self) -> bool:
        ...

    @property
    def MetadataToken(self) -> int:
        ...

    # methods
    def __init__(self, ):
        ...

    def GetReturnType(self, ) -> System.Type:
        ...

    @typing.overload
    def Invoke(self, parameters: System.Array[System.Object], ) -> System.Object:
        ...

    @abc.abstractmethod
    @typing.overload
    def Invoke(self, invokeAttr: int, binder: System.Reflection.Binder, parameters: System.Array[System.Object], culture: System.Globalization.CultureInfo, ) -> System.Object:
        ...

    def Equals(self, obj: System.Object, ) -> bool:
        ...

    def GetHashCode(self, ) -> int:
        ...

class ManifestResourceInfo(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def ReferencedAssembly(self) -> System.Reflection.Assembly:
        ...

    @property
    def FileName(self) -> str:
        ...

    @property
    def ResourceLocation(self) -> int:
        ...

    # methods
    def __init__(self, containingAssembly: System.Reflection.Assembly, containingFileName: str, resourceLocation: int, ):
        ...

class FieldAttributes(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    PrivateScope: int = ...
    Private: int = ...
    FamANDAssem: int = ...
    Assembly: int = ...
    Family: int = ...
    FamORAssem: int = ...
    Public: int = ...
    FieldAccessMask: int = ...
    Static: int = ...
    InitOnly: int = ...
    Literal: int = ...
    NotSerialized: int = ...
    HasFieldRVA: int = ...
    SpecialName: int = ...
    RTSpecialName: int = ...
    HasFieldMarshal: int = ...
    PinvokeImpl: int = ...
    HasDefault: int = ...
    ReservedMask: int = ...

class StrongNameKeyPair(System.Runtime.Serialization.IDeserializationCallback, System.Runtime.Serialization.ISerializable, System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def PublicKey(self) -> System.Array[int]:
        ...

    # methods
    @typing.overload
    def __init__(self, keyPairFile: System.IO.FileStream, ):
        ...

    @typing.overload
    def __init__(self, keyPairArray: System.Array[int], ):
        ...

    @typing.overload
    def __init__(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext, ):
        ...

    @typing.overload
    def __init__(self, keyPairContainer: str, ):
        ...

    def GetObjectData(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext, ) -> None:
        ...

    def OnDeserialization(self, sender: System.Object, ) -> None:
        ...

class GenericParameterAttributes(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    None_: int = ...
    Covariant: int = ...
    Contravariant: int = ...
    VarianceMask: int = ...
    ReferenceTypeConstraint: int = ...
    NotNullableValueTypeConstraint: int = ...
    DefaultConstructorConstraint: int = ...
    SpecialConstraintMask: int = ...

class InterfaceMapping(System.ValueType):
    @typing.overload
    def __init__(self, **kwargs):
        self.TargetType: System.Type
        self.InterfaceType: System.Type
        self.TargetMethods: System.Array[System.Reflection.MethodInfo]
        self.InterfaceMethods: System.Array[System.Reflection.MethodInfo]
        ...

    # static fields

    # properties
    # methods
class CustomAttributeData(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def AttributeType(self) -> System.Type:
        ...

    @property
    def Constructor(self) -> System.Reflection.ConstructorInfo:
        ...

    @property
    def ConstructorArguments(self) -> System.Collections.Generic.IList[System.Reflection.CustomAttributeTypedArgument]:
        ...

    @property
    def NamedArguments(self) -> System.Collections.Generic.IList[System.Reflection.CustomAttributeNamedArgument]:
        ...

    # methods
    def __init__(self, ):
        ...

    @staticmethod
    @typing.overload
    def GetCustomAttributes(target: System.Reflection.MemberInfo, ) -> System.Collections.Generic.IList[System.Reflection.CustomAttributeData]:
        ...

    @staticmethod
    @typing.overload
    def GetCustomAttributes(target: System.Reflection.Module, ) -> System.Collections.Generic.IList[System.Reflection.CustomAttributeData]:
        ...

    @staticmethod
    @typing.overload
    def GetCustomAttributes(target: System.Reflection.Assembly, ) -> System.Collections.Generic.IList[System.Reflection.CustomAttributeData]:
        ...

    @staticmethod
    @typing.overload
    def GetCustomAttributes(target: System.Reflection.ParameterInfo, ) -> System.Collections.Generic.IList[System.Reflection.CustomAttributeData]:
        ...

    def ToString(self, ) -> str:
        ...

    def GetHashCode(self, ) -> int:
        ...

    def Equals(self, obj: System.Object, ) -> bool:
        ...

class CustomAttributeNamedArgument(System.ValueType):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def ArgumentType(self) -> System.Type:
        ...

    @property
    def MemberInfo(self) -> System.Reflection.MemberInfo:
        ...

    @property
    def TypedValue(self) -> System.Reflection.CustomAttributeTypedArgument:
        ...

    @property
    def MemberName(self) -> str:
        ...

    @property
    def IsField(self) -> bool:
        ...

    # methods
    @typing.overload
    def __init__(self, memberInfo: System.Reflection.MemberInfo, value: System.Object, ):
        ...

    @typing.overload
    def __init__(self, memberInfo: System.Reflection.MemberInfo, typedArgument: System.Reflection.CustomAttributeTypedArgument, ):
        ...

    def ToString(self, ) -> str:
        ...

    def GetHashCode(self, ) -> int:
        ...

    def Equals(self, obj: System.Object, ) -> bool:
        ...

class CustomAttributeTypedArgument(System.ValueType):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def ArgumentType(self) -> System.Type:
        ...

    @property
    def Value(self) -> System.Object:
        ...

    # methods
    @typing.overload
    def __init__(self, scope: System.Reflection.RuntimeModule, encodedArg: System.Reflection.CustomAttributeEncodedArgument, ):
        ...

    @typing.overload
    def __init__(self, argumentType: System.Type, value: System.Object, ):
        ...

    @typing.overload
    def __init__(self, value: System.Object, ):
        ...

    @staticmethod
    def CustomAttributeEncodingToType(encodedType: int, ) -> System.Type:
        ...

    @staticmethod
    def EncodedValueToRawValue(val: int, encodedType: int, ) -> System.Object:
        ...

    @staticmethod
    def ResolveType(scope: System.Reflection.RuntimeModule, typeName: str, ) -> System.RuntimeType:
        ...

    @typing.overload
    def ToString(self, ) -> str:
        ...

    @typing.overload
    def ToString(self, typed: bool, ) -> str:
        ...

    def GetHashCode(self, ) -> int:
        ...

    def Equals(self, obj: System.Object, ) -> bool:
        ...

    @staticmethod
    def CanonicalizeValue(value: System.Object, ) -> System.Object:
        ...

class ICustomAttributeProvider(abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    @abc.abstractmethod
    @typing.overload
    def GetCustomAttributes(self, inherit: bool, ) -> System.Array[System.Object]:
        ...

    @abc.abstractmethod
    @typing.overload
    def GetCustomAttributes(self, attributeType: System.Type, inherit: bool, ) -> System.Array[System.Object]:
        ...

    @abc.abstractmethod
    def IsDefined(self, attributeType: System.Type, inherit: bool, ) -> bool:
        ...

class IReflect(abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    @abc.abstractmethod
    def UnderlyingSystemType(self) -> System.Type:
        ...

    # methods
    @abc.abstractmethod
    @typing.overload
    def GetMethod(self, name: str, bindingAttr: int, binder: System.Reflection.Binder, types: System.Array[System.Type], modifiers: System.Array[System.Reflection.ParameterModifier], ) -> System.Reflection.MethodInfo:
        ...

    @abc.abstractmethod
    @typing.overload
    def GetMethod(self, name: str, bindingAttr: int, ) -> System.Reflection.MethodInfo:
        ...

    @abc.abstractmethod
    def GetMethods(self, bindingAttr: int, ) -> System.Array[System.Reflection.MethodInfo]:
        ...

    @abc.abstractmethod
    def GetField(self, name: str, bindingAttr: int, ) -> System.Reflection.FieldInfo:
        ...

    @abc.abstractmethod
    def GetFields(self, bindingAttr: int, ) -> System.Array[System.Reflection.FieldInfo]:
        ...

    @abc.abstractmethod
    @typing.overload
    def GetProperty(self, name: str, bindingAttr: int, ) -> System.Reflection.PropertyInfo:
        ...

    @abc.abstractmethod
    @typing.overload
    def GetProperty(self, name: str, bindingAttr: int, binder: System.Reflection.Binder, returnType: System.Type, types: System.Array[System.Type], modifiers: System.Array[System.Reflection.ParameterModifier], ) -> System.Reflection.PropertyInfo:
        ...

    @abc.abstractmethod
    def GetProperties(self, bindingAttr: int, ) -> System.Array[System.Reflection.PropertyInfo]:
        ...

    @abc.abstractmethod
    def GetMember(self, name: str, bindingAttr: int, ) -> System.Array[System.Reflection.MemberInfo]:
        ...

    @abc.abstractmethod
    def GetMembers(self, bindingAttr: int, ) -> System.Array[System.Reflection.MemberInfo]:
        ...

    @abc.abstractmethod
    def InvokeMember(self, name: str, invokeAttr: int, binder: System.Reflection.Binder, target: System.Object, args: System.Array[System.Object], modifiers: System.Array[System.Reflection.ParameterModifier], culture: System.Globalization.CultureInfo, namedParameters: System.Array[str], ) -> System.Object:
        ...

class TypeInfo(System.Reflection.ICustomAttributeProvider, System.Reflection.IReflect, System.Reflection.IReflectableType, System.Type, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def GenericTypeParameters(self) -> System.Array[System.Type]:
        ...

    @property
    def DeclaredConstructors(self) -> System.Collections.Generic.IEnumerable[System.Reflection.ConstructorInfo]:
        ...

    @property
    def DeclaredEvents(self) -> System.Collections.Generic.IEnumerable[System.Reflection.EventInfo]:
        ...

    @property
    def DeclaredFields(self) -> System.Collections.Generic.IEnumerable[System.Reflection.FieldInfo]:
        ...

    @property
    def DeclaredMembers(self) -> System.Collections.Generic.IEnumerable[System.Reflection.MemberInfo]:
        ...

    @property
    def DeclaredMethods(self) -> System.Collections.Generic.IEnumerable[System.Reflection.MethodInfo]:
        ...

    @property
    def DeclaredNestedTypes(self) -> System.Collections.Generic.IEnumerable[System.Reflection.TypeInfo]:
        ...

    @property
    def DeclaredProperties(self) -> System.Collections.Generic.IEnumerable[System.Reflection.PropertyInfo]:
        ...

    @property
    def ImplementedInterfaces(self) -> System.Collections.Generic.IEnumerable[System.Type]:
        ...

    @property
    def IsInterface(self) -> bool:
        ...

    @property
    def MemberType(self) -> int:
        ...

    @property
    @abc.abstractmethod
    def Namespace(self) -> str:
        ...

    @property
    @abc.abstractmethod
    def AssemblyQualifiedName(self) -> str:
        ...

    @property
    @abc.abstractmethod
    def FullName(self) -> str:
        ...

    @property
    @abc.abstractmethod
    def Assembly(self) -> System.Reflection.Assembly:
        ...

    @property
    @abc.abstractmethod
    def Module(self) -> System.Reflection.Module:
        ...

    @property
    def IsNested(self) -> bool:
        ...

    @property
    def DeclaringType(self) -> System.Type:
        ...

    @property
    def DeclaringMethod(self) -> System.Reflection.MethodBase:
        ...

    @property
    def ReflectedType(self) -> System.Type:
        ...

    @property
    @abc.abstractmethod
    def UnderlyingSystemType(self) -> System.Type:
        ...

    @property
    def IsTypeDefinition(self) -> bool:
        ...

    @property
    def IsArray(self) -> bool:
        ...

    @property
    def IsByRef(self) -> bool:
        ...

    @property
    def IsPointer(self) -> bool:
        ...

    @property
    def IsConstructedGenericType(self) -> bool:
        ...

    @property
    def IsGenericParameter(self) -> bool:
        ...

    @property
    def IsGenericTypeParameter(self) -> bool:
        ...

    @property
    def IsGenericMethodParameter(self) -> bool:
        ...

    @property
    def IsGenericType(self) -> bool:
        ...

    @property
    def IsGenericTypeDefinition(self) -> bool:
        ...

    @property
    def IsSZArray(self) -> bool:
        ...

    @property
    def IsVariableBoundArray(self) -> bool:
        ...

    @property
    def IsByRefLike(self) -> bool:
        ...

    @property
    def HasElementType(self) -> bool:
        ...

    @property
    def GenericTypeArguments(self) -> System.Array[System.Type]:
        ...

    @property
    def GenericParameterPosition(self) -> int:
        ...

    @property
    def GenericParameterAttributes(self) -> int:
        ...

    @property
    def Attributes(self) -> int:
        ...

    @property
    def IsAbstract(self) -> bool:
        ...

    @property
    def IsImport(self) -> bool:
        ...

    @property
    def IsSealed(self) -> bool:
        ...

    @property
    def IsSpecialName(self) -> bool:
        ...

    @property
    def IsClass(self) -> bool:
        ...

    @property
    def IsNestedAssembly(self) -> bool:
        ...

    @property
    def IsNestedFamANDAssem(self) -> bool:
        ...

    @property
    def IsNestedFamily(self) -> bool:
        ...

    @property
    def IsNestedFamORAssem(self) -> bool:
        ...

    @property
    def IsNestedPrivate(self) -> bool:
        ...

    @property
    def IsNestedPublic(self) -> bool:
        ...

    @property
    def IsNotPublic(self) -> bool:
        ...

    @property
    def IsPublic(self) -> bool:
        ...

    @property
    def IsAutoLayout(self) -> bool:
        ...

    @property
    def IsExplicitLayout(self) -> bool:
        ...

    @property
    def IsLayoutSequential(self) -> bool:
        ...

    @property
    def IsAnsiClass(self) -> bool:
        ...

    @property
    def IsAutoClass(self) -> bool:
        ...

    @property
    def IsUnicodeClass(self) -> bool:
        ...

    @property
    def IsCOMObject(self) -> bool:
        ...

    @property
    def IsContextful(self) -> bool:
        ...

    @property
    def IsEnum(self) -> bool:
        ...

    @property
    def IsMarshalByRef(self) -> bool:
        ...

    @property
    def IsPrimitive(self) -> bool:
        ...

    @property
    def IsValueType(self) -> bool:
        ...

    @property
    def IsSignatureType(self) -> bool:
        ...

    @property
    def IsSecurityCritical(self) -> bool:
        ...

    @property
    def IsSecuritySafeCritical(self) -> bool:
        ...

    @property
    def IsSecurityTransparent(self) -> bool:
        ...

    @property
    def StructLayoutAttribute(self) -> System.Runtime.InteropServices.StructLayoutAttribute:
        ...

    @property
    def TypeInitializer(self) -> System.Reflection.ConstructorInfo:
        ...

    @property
    def TypeHandle(self) -> System.RuntimeTypeHandle:
        ...

    @property
    @abc.abstractmethod
    def GUID(self) -> System.Guid:
        ...

    @property
    @abc.abstractmethod
    def BaseType(self) -> System.Type:
        ...

    @property
    def IsSerializable(self) -> bool:
        ...

    @property
    def ContainsGenericParameters(self) -> bool:
        ...

    @property
    def IsVisible(self) -> bool:
        ...

    @property
    @abc.abstractmethod
    def Name(self) -> str:
        ...

    @property
    def CustomAttributes(self) -> System.Collections.Generic.IEnumerable[System.Reflection.CustomAttributeData]:
        ...

    @property
    def IsCollectible(self) -> bool:
        ...

    @property
    def MetadataToken(self) -> int:
        ...

    # methods
    def __init__(self, ):
        ...

    def GetTypeInfo(self, ) -> System.Reflection.TypeInfo:
        ...

    def AsType(self, ) -> System.Type:
        ...

    def GetDeclaredEvent(self, name: str, ) -> System.Reflection.EventInfo:
        ...

    def GetDeclaredField(self, name: str, ) -> System.Reflection.FieldInfo:
        ...

    def GetDeclaredMethod(self, name: str, ) -> System.Reflection.MethodInfo:
        ...

    def GetDeclaredNestedType(self, name: str, ) -> System.Reflection.TypeInfo:
        ...

    def GetDeclaredProperty(self, name: str, ) -> System.Reflection.PropertyInfo:
        ...

    def GetDeclaredMethods(self, name: str, ) -> System.Collections.Generic.IEnumerable[System.Reflection.MethodInfo]:
        ...

    def IsAssignableFrom(self, typeInfo: System.Reflection.TypeInfo, ) -> bool:
        ...

    @staticmethod
    def GetRankString(rank: int, ) -> str:
        ...

class MethodAttributes(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    ReuseSlot: int = ...
    PrivateScope: int = ...
    Private: int = ...
    FamANDAssem: int = ...
    Assembly: int = ...
    Family: int = ...
    FamORAssem: int = ...
    Public: int = ...
    MemberAccessMask: int = ...
    UnmanagedExport: int = ...
    Static: int = ...
    Final: int = ...
    Virtual: int = ...
    HideBySig: int = ...
    NewSlot: int = ...
    VtableLayoutMask: int = ...
    CheckAccessOnOverride: int = ...
    Abstract: int = ...
    SpecialName: int = ...
    RTSpecialName: int = ...
    PinvokeImpl: int = ...
    HasSecurity: int = ...
    RequireSecObject: int = ...
    ReservedMask: int = ...

class ParameterModifier(System.ValueType):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def Item(self) -> bool:
        ...
    @Item.setter
    def Item(self, val: bool):
        ...

    # methods
    def __init__(self, parameterCount: int, ):
        ...

class MemberTypes(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    Constructor: int = ...
    Event: int = ...
    Field: int = ...
    Method: int = ...
    Property: int = ...
    TypeInfo: int = ...
    Custom: int = ...
    NestedType: int = ...
    All: int = ...

class LocalVariableInfo(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def LocalType(self) -> System.Type:
        ...

    @property
    def LocalIndex(self) -> int:
        ...

    @property
    def IsPinned(self) -> bool:
        ...

    # methods
    def __init__(self, ):
        ...

    def ToString(self, ) -> str:
        ...

class TypeAttributes(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    NotPublic: int = ...
    AutoLayout: int = ...
    AnsiClass: int = ...
    Class: int = ...
    Public: int = ...
    NestedPublic: int = ...
    NestedPrivate: int = ...
    NestedFamily: int = ...
    NestedAssembly: int = ...
    NestedFamANDAssem: int = ...
    NestedFamORAssem: int = ...
    VisibilityMask: int = ...
    SequentialLayout: int = ...
    ExplicitLayout: int = ...
    LayoutMask: int = ...
    Interface: int = ...
    ClassSemanticsMask: int = ...
    Abstract: int = ...
    Sealed: int = ...
    SpecialName: int = ...
    RTSpecialName: int = ...
    Import: int = ...
    Serializable: int = ...
    WindowsRuntime: int = ...
    UnicodeClass: int = ...
    AutoClass: int = ...
    CustomFormatClass: int = ...
    StringFormatMask: int = ...
    HasSecurity: int = ...
    ReservedMask: int = ...
    BeforeFieldInit: int = ...
    CustomFormatMask: int = ...

class ResourceLocation(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    Embedded: int = ...
    ContainedInAnotherAssembly: int = ...
    ContainedInManifestFile: int = ...

class MethodBody(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def LocalSignatureMetadataToken(self) -> int:
        ...

    @property
    def LocalVariables(self) -> System.Collections.Generic.IList[System.Reflection.LocalVariableInfo]:
        ...

    @property
    def MaxStackSize(self) -> int:
        ...

    @property
    def InitLocals(self) -> bool:
        ...

    @property
    def ExceptionHandlingClauses(self) -> System.Collections.Generic.IList[System.Reflection.ExceptionHandlingClause]:
        ...

    # methods
    def __init__(self, ):
        ...

    def GetILAsByteArray(self, ) -> System.Array[int]:
        ...

class ExceptionHandlingClause(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def Flags(self) -> int:
        ...

    @property
    def TryOffset(self) -> int:
        ...

    @property
    def TryLength(self) -> int:
        ...

    @property
    def HandlerOffset(self) -> int:
        ...

    @property
    def HandlerLength(self) -> int:
        ...

    @property
    def FilterOffset(self) -> int:
        ...

    @property
    def CatchType(self) -> System.Type:
        ...

    # methods
    def __init__(self, ):
        ...

    def ToString(self, ) -> str:
        ...

class ExceptionHandlingClauseOptions(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    Clause: int = ...
    Filter: int = ...
    Finally: int = ...
    Fault: int = ...

class BindingFlags(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    Default: int = ...
    IgnoreCase: int = ...
    DeclaredOnly: int = ...
    Instance: int = ...
    Static: int = ...
    Public: int = ...
    NonPublic: int = ...
    FlattenHierarchy: int = ...
    InvokeMethod: int = ...
    CreateInstance: int = ...
    GetField: int = ...
    SetField: int = ...
    GetProperty: int = ...
    SetProperty: int = ...
    PutDispProperty: int = ...
    PutRefDispProperty: int = ...
    ExactBinding: int = ...
    SuppressChangeType: int = ...
    OptionalParamBinding: int = ...
    IgnoreReturn: int = ...
    DoNotWrapExceptions: int = ...

class MemberFilter(System.ICloneable, System.Runtime.Serialization.ISerializable, System.MulticastDelegate):
    @typing.overload
    def __init__(self, **kwargs):
        self._target: System.Object
        self._methodBase: System.Object
        self._methodPtr: System.IntPtr
        self._methodPtrAux: System.IntPtr
        ...

    # static fields

    # properties
    @property
    def Target(self) -> System.Object:
        ...

    @property
    def Method(self) -> System.Reflection.MethodInfo:
        ...

    # methods
    def __init__(self, object: System.Object, method: System.IntPtr, ):
        ...

    def Invoke(self, m: System.Reflection.MemberInfo, filterCriteria: System.Object, ) -> bool:
        ...

    def BeginInvoke(self, m: System.Reflection.MemberInfo, filterCriteria: System.Object, callback: System.AsyncCallback, object: System.Object, ) -> System.IAsyncResult:
        ...

    def EndInvoke(self, result: System.IAsyncResult, ) -> bool:
        ...

class MemberInfo(System.Reflection.ICustomAttributeProvider, System.Object, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    @abc.abstractmethod
    def MemberType(self) -> int:
        ...

    @property
    @abc.abstractmethod
    def Name(self) -> str:
        ...

    @property
    @abc.abstractmethod
    def DeclaringType(self) -> System.Type:
        ...

    @property
    @abc.abstractmethod
    def ReflectedType(self) -> System.Type:
        ...

    @property
    def Module(self) -> System.Reflection.Module:
        ...

    @property
    def CustomAttributes(self) -> System.Collections.Generic.IEnumerable[System.Reflection.CustomAttributeData]:
        ...

    @property
    def IsCollectible(self) -> bool:
        ...

    @property
    def MetadataToken(self) -> int:
        ...

    # methods
    def __init__(self, ):
        ...

    def CacheEquals(self, o: System.Object, ) -> bool:
        ...

    def HasSameMetadataDefinitionAsCore(self, other: System.Reflection.MemberInfo, ) -> bool:
        ...

    def HasSameMetadataDefinitionAs(self, other: System.Reflection.MemberInfo, ) -> bool:
        ...

    @abc.abstractmethod
    def IsDefined(self, attributeType: System.Type, inherit: bool, ) -> bool:
        ...

    @abc.abstractmethod
    @typing.overload
    def GetCustomAttributes(self, inherit: bool, ) -> System.Array[System.Object]:
        ...

    @abc.abstractmethod
    @typing.overload
    def GetCustomAttributes(self, attributeType: System.Type, inherit: bool, ) -> System.Array[System.Object]:
        ...

    def GetCustomAttributesData(self, ) -> System.Collections.Generic.IList[System.Reflection.CustomAttributeData]:
        ...

    def Equals(self, obj: System.Object, ) -> bool:
        ...

    def GetHashCode(self, ) -> int:
        ...

