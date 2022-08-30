from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import System.Reflection
import System
import System.Collections.Generic
import System.Runtime.Serialization
import System.Security
import System.IO
import System.Globalization
import System.Configuration.Assemblies
import System.Runtime.InteropServices

T = typing.TypeVar('T')

class MethodInfo(System.Reflection.ICustomAttributeProvider, System.Reflection.MethodBase, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def MemberType(self) -> System.Reflection.MemberTypes:
        ...

    @property
    def ReturnParameter(self) -> System.Reflection.ParameterInfo:
        ...

    @property
    def ReturnType(self) -> System.Type:
        ...

    @abc.abstractmethod
    @property
    def ReturnTypeCustomAttributes(self) -> System.Reflection.ICustomAttributeProvider:
        ...

    @abc.abstractmethod
    @property
    def Attributes(self) -> System.Reflection.MethodAttributes:
        ...

    @property
    def MethodImplementationFlags(self) -> System.Reflection.MethodImplAttributes:
        ...

    @property
    def CallingConvention(self) -> System.Reflection.CallingConventions:
        ...

    @property
    def IsAbstract(self) -> System.Boolean:
        ...

    @property
    def IsConstructor(self) -> System.Boolean:
        ...

    @property
    def IsFinal(self) -> System.Boolean:
        ...

    @property
    def IsHideBySig(self) -> System.Boolean:
        ...

    @property
    def IsSpecialName(self) -> System.Boolean:
        ...

    @property
    def IsStatic(self) -> System.Boolean:
        ...

    @property
    def IsVirtual(self) -> System.Boolean:
        ...

    @property
    def IsAssembly(self) -> System.Boolean:
        ...

    @property
    def IsFamily(self) -> System.Boolean:
        ...

    @property
    def IsFamilyAndAssembly(self) -> System.Boolean:
        ...

    @property
    def IsFamilyOrAssembly(self) -> System.Boolean:
        ...

    @property
    def IsPrivate(self) -> System.Boolean:
        ...

    @property
    def IsPublic(self) -> System.Boolean:
        ...

    @property
    def IsConstructedGenericMethod(self) -> System.Boolean:
        ...

    @property
    def IsGenericMethod(self) -> System.Boolean:
        ...

    @property
    def IsGenericMethodDefinition(self) -> System.Boolean:
        ...

    @property
    def ContainsGenericParameters(self) -> System.Boolean:
        ...

    @abc.abstractmethod
    @property
    def MethodHandle(self) -> System.RuntimeMethodHandle:
        ...

    @property
    def IsSecurityCritical(self) -> System.Boolean:
        ...

    @property
    def IsSecuritySafeCritical(self) -> System.Boolean:
        ...

    @property
    def IsSecurityTransparent(self) -> System.Boolean:
        ...

    @abc.abstractmethod
    @property
    def Name(self) -> System.String:
        ...

    @abc.abstractmethod
    @property
    def DeclaringType(self) -> System.Type:
        ...

    @abc.abstractmethod
    @property
    def ReflectedType(self) -> System.Type:
        ...

    @property
    def Module(self) -> System.Reflection.Module:
        ...

    @property
    def CustomAttributes(self) -> System.Collections.Generic.IEnumerable[System.Reflection.CustomAttributeData]:
        ...

    @property
    def IsCollectible(self) -> System.Boolean:
        ...

    @property
    def MetadataToken(self) -> System.Int32:
        ...

    # methods
    @typing.overload
    def GetGenericArguments(self, ) -> list[System.Type]:
        ...

    @typing.overload
    def GetGenericMethodDefinition(self, ) -> System.Reflection.MethodInfo:
        ...

    @typing.overload
    def MakeGenericMethod(self, typeArguments: list[System.Type], ) -> System.Reflection.MethodInfo:
        ...

    @typing.overload
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

    @typing.overload
    def Equals(self, obj: System.Object, ) -> System.Boolean:
        ...

    @typing.overload
    def GetHashCode(self, ) -> System.Int32:
        ...

class MemberInfo(System.Reflection.ICustomAttributeProvider, System.Object, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @abc.abstractmethod
    @property
    def MemberType(self) -> System.Reflection.MemberTypes:
        ...

    @abc.abstractmethod
    @property
    def Name(self) -> System.String:
        ...

    @abc.abstractmethod
    @property
    def DeclaringType(self) -> System.Type:
        ...

    @abc.abstractmethod
    @property
    def ReflectedType(self) -> System.Type:
        ...

    @property
    def Module(self) -> System.Reflection.Module:
        ...

    @property
    def CustomAttributes(self) -> System.Collections.Generic.IEnumerable[System.Reflection.CustomAttributeData]:
        ...

    @property
    def IsCollectible(self) -> System.Boolean:
        ...

    @property
    def MetadataToken(self) -> System.Int32:
        ...

    # methods
    @typing.overload
    def Equals(self, obj: System.Object, ) -> System.Boolean:
        ...

    @typing.overload
    def GetHashCode(self, ) -> System.Int32:
        ...

    @typing.overload
    def HasSameMetadataDefinitionAs(self, other: System.Reflection.MemberInfo, ) -> System.Boolean:
        ...

    @typing.overload
    @abc.abstractmethod
    def IsDefined(self, attributeType: System.Type, inherit: System.Boolean, ) -> System.Boolean:
        ...

    @typing.overload
    @abc.abstractmethod
    def GetCustomAttributes(self, inherit: System.Boolean, ) -> list[System.Object]:
        ...

    @typing.overload
    @abc.abstractmethod
    def GetCustomAttributes(self, attributeType: System.Type, inherit: System.Boolean, ) -> list[System.Object]:
        ...

    @typing.overload
    def GetCustomAttributesData(self, ) -> System.Collections.Generic.IList[System.Reflection.CustomAttributeData]:
        ...

class ParameterInfo(System.Reflection.ICustomAttributeProvider, System.Runtime.Serialization.IObjectReference, System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def Attributes(self) -> System.Reflection.ParameterAttributes:
        ...

    @property
    def Member(self) -> System.Reflection.MemberInfo:
        ...

    @property
    def Name(self) -> System.String:
        ...

    @property
    def ParameterType(self) -> System.Type:
        ...

    @property
    def Position(self) -> System.Int32:
        ...

    @property
    def IsIn(self) -> System.Boolean:
        ...

    @property
    def IsLcid(self) -> System.Boolean:
        ...

    @property
    def IsOptional(self) -> System.Boolean:
        ...

    @property
    def IsOut(self) -> System.Boolean:
        ...

    @property
    def IsRetval(self) -> System.Boolean:
        ...

    @property
    def DefaultValue(self) -> System.Object:
        ...

    @property
    def RawDefaultValue(self) -> System.Object:
        ...

    @property
    def HasDefaultValue(self) -> System.Boolean:
        ...

    @property
    def CustomAttributes(self) -> System.Collections.Generic.IEnumerable[System.Reflection.CustomAttributeData]:
        ...

    @property
    def MetadataToken(self) -> System.Int32:
        ...

    # methods
    @typing.overload
    def IsDefined(self, attributeType: System.Type, inherit: System.Boolean, ) -> System.Boolean:
        ...

    @typing.overload
    def GetCustomAttributesData(self, ) -> System.Collections.Generic.IList[System.Reflection.CustomAttributeData]:
        ...

    @typing.overload
    def GetCustomAttributes(self, inherit: System.Boolean, ) -> list[System.Object]:
        ...

    @typing.overload
    def GetCustomAttributes(self, attributeType: System.Type, inherit: System.Boolean, ) -> list[System.Object]:
        ...

    @typing.overload
    def GetOptionalCustomModifiers(self, ) -> list[System.Type]:
        ...

    @typing.overload
    def GetRequiredCustomModifiers(self, ) -> list[System.Type]:
        ...

    @typing.overload
    def GetRealObject(self, context: System.Runtime.Serialization.StreamingContext, ) -> System.Object:
        ...

    @typing.overload
    def ToString(self, ) -> System.String:
        ...

class Module(System.Reflection.ICustomAttributeProvider, System.Runtime.Serialization.ISerializable, System.Object, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def Assembly(self) -> System.Reflection.Assembly:
        ...

    @property
    def FullyQualifiedName(self) -> System.String:
        ...

    @property
    def Name(self) -> System.String:
        ...

    @property
    def MDStreamVersion(self) -> System.Int32:
        ...

    @property
    def ModuleVersionId(self) -> System.Guid:
        ...

    @property
    def ScopeName(self) -> System.String:
        ...

    @property
    def ModuleHandle(self) -> System.ModuleHandle:
        ...

    @property
    def CustomAttributes(self) -> System.Collections.Generic.IEnumerable[System.Reflection.CustomAttributeData]:
        ...

    @property
    def MetadataToken(self) -> System.Int32:
        ...

    # methods
    @typing.overload
    def GetPEKind(self, peKind: ref[System.Reflection.PortableExecutableKinds], machine: ref[System.Reflection.ImageFileMachine], ) -> None:
        ...

    @typing.overload
    def IsResource(self, ) -> System.Boolean:
        ...

    @typing.overload
    def IsDefined(self, attributeType: System.Type, inherit: System.Boolean, ) -> System.Boolean:
        ...

    @typing.overload
    def GetCustomAttributesData(self, ) -> System.Collections.Generic.IList[System.Reflection.CustomAttributeData]:
        ...

    @typing.overload
    def GetCustomAttributes(self, inherit: System.Boolean, ) -> list[System.Object]:
        ...

    @typing.overload
    def GetCustomAttributes(self, attributeType: System.Type, inherit: System.Boolean, ) -> list[System.Object]:
        ...

    @typing.overload
    def GetMethod(self, name: System.String, ) -> System.Reflection.MethodInfo:
        ...

    @typing.overload
    def GetMethod(self, name: System.String, types: list[System.Type], ) -> System.Reflection.MethodInfo:
        ...

    @typing.overload
    def GetMethod(self, name: System.String, bindingAttr: System.Reflection.BindingFlags, binder: System.Reflection.Binder, callConvention: System.Reflection.CallingConventions, types: list[System.Type], modifiers: list[System.Reflection.ParameterModifier], ) -> System.Reflection.MethodInfo:
        ...

    @typing.overload
    def GetMethods(self, ) -> list[System.Reflection.MethodInfo]:
        ...

    @typing.overload
    def GetMethods(self, bindingFlags: System.Reflection.BindingFlags, ) -> list[System.Reflection.MethodInfo]:
        ...

    @typing.overload
    def GetField(self, name: System.String, ) -> System.Reflection.FieldInfo:
        ...

    @typing.overload
    def GetField(self, name: System.String, bindingAttr: System.Reflection.BindingFlags, ) -> System.Reflection.FieldInfo:
        ...

    @typing.overload
    def GetFields(self, ) -> list[System.Reflection.FieldInfo]:
        ...

    @typing.overload
    def GetFields(self, bindingFlags: System.Reflection.BindingFlags, ) -> list[System.Reflection.FieldInfo]:
        ...

    @typing.overload
    def GetTypes(self, ) -> list[System.Type]:
        ...

    @typing.overload
    def GetType(self, className: System.String, ) -> System.Type:
        ...

    @typing.overload
    def GetType(self, className: System.String, ignoreCase: System.Boolean, ) -> System.Type:
        ...

    @typing.overload
    def GetType(self, className: System.String, throwOnError: System.Boolean, ignoreCase: System.Boolean, ) -> System.Type:
        ...

    @typing.overload
    def FindTypes(self, filter: System.Reflection.TypeFilter, filterCriteria: System.Object, ) -> list[System.Type]:
        ...

    @typing.overload
    def ResolveField(self, metadataToken: System.Int32, ) -> System.Reflection.FieldInfo:
        ...

    @typing.overload
    def ResolveField(self, metadataToken: System.Int32, genericTypeArguments: list[System.Type], genericMethodArguments: list[System.Type], ) -> System.Reflection.FieldInfo:
        ...

    @typing.overload
    def ResolveMember(self, metadataToken: System.Int32, ) -> System.Reflection.MemberInfo:
        ...

    @typing.overload
    def ResolveMember(self, metadataToken: System.Int32, genericTypeArguments: list[System.Type], genericMethodArguments: list[System.Type], ) -> System.Reflection.MemberInfo:
        ...

    @typing.overload
    def ResolveMethod(self, metadataToken: System.Int32, ) -> System.Reflection.MethodBase:
        ...

    @typing.overload
    def ResolveMethod(self, metadataToken: System.Int32, genericTypeArguments: list[System.Type], genericMethodArguments: list[System.Type], ) -> System.Reflection.MethodBase:
        ...

    @typing.overload
    def ResolveSignature(self, metadataToken: System.Int32, ) -> list[System.Byte]:
        ...

    @typing.overload
    def ResolveString(self, metadataToken: System.Int32, ) -> System.String:
        ...

    @typing.overload
    def ResolveType(self, metadataToken: System.Int32, ) -> System.Type:
        ...

    @typing.overload
    def ResolveType(self, metadataToken: System.Int32, genericTypeArguments: list[System.Type], genericMethodArguments: list[System.Type], ) -> System.Type:
        ...

    @typing.overload
    def GetObjectData(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext, ) -> None:
        ...

    @typing.overload
    def Equals(self, o: System.Object, ) -> System.Boolean:
        ...

    @typing.overload
    def GetHashCode(self, ) -> System.Int32:
        ...

    @typing.overload
    def ToString(self, ) -> System.String:
        ...

class Assembly(System.Reflection.ICustomAttributeProvider, System.Runtime.Serialization.ISerializable, System.Object, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def DefinedTypes(self) -> System.Collections.Generic.IEnumerable[System.Reflection.TypeInfo]:
        ...

    @property
    def ExportedTypes(self) -> System.Collections.Generic.IEnumerable[System.Type]:
        ...

    @property
    def CodeBase(self) -> System.String:
        ...

    @property
    def EntryPoint(self) -> System.Reflection.MethodInfo:
        ...

    @property
    def FullName(self) -> System.String:
        ...

    @property
    def ImageRuntimeVersion(self) -> System.String:
        ...

    @property
    def IsDynamic(self) -> System.Boolean:
        ...

    @property
    def Location(self) -> System.String:
        ...

    @property
    def ReflectionOnly(self) -> System.Boolean:
        ...

    @property
    def IsCollectible(self) -> System.Boolean:
        ...

    @property
    def IsFullyTrusted(self) -> System.Boolean:
        ...

    @property
    def CustomAttributes(self) -> System.Collections.Generic.IEnumerable[System.Reflection.CustomAttributeData]:
        ...

    @property
    def EscapedCodeBase(self) -> System.String:
        ...

    @property
    def ManifestModule(self) -> System.Reflection.Module:
        ...

    @property
    def Modules(self) -> System.Collections.Generic.IEnumerable[System.Reflection.Module]:
        ...

    @property
    def GlobalAssemblyCache(self) -> System.Boolean:
        ...

    @property
    def HostContext(self) -> System.Int64:
        ...

    @property
    def SecurityRuleSet(self) -> System.Security.SecurityRuleSet:
        ...

    # methods
    @typing.overload
    @staticmethod
    def Load(assemblyString: System.String, ) -> System.Reflection.Assembly:
        ...

    @typing.overload
    @staticmethod
    def LoadWithPartialName(partialName: System.String, ) -> System.Reflection.Assembly:
        ...

    @typing.overload
    @staticmethod
    def Load(assemblyRef: System.Reflection.AssemblyName, ) -> System.Reflection.Assembly:
        ...

    @typing.overload
    @staticmethod
    def GetExecutingAssembly() -> System.Reflection.Assembly:
        ...

    @typing.overload
    @staticmethod
    def GetCallingAssembly() -> System.Reflection.Assembly:
        ...

    @typing.overload
    def GetTypes(self, ) -> list[System.Type]:
        ...

    @typing.overload
    def GetExportedTypes(self, ) -> list[System.Type]:
        ...

    @typing.overload
    def GetForwardedTypes(self, ) -> list[System.Type]:
        ...

    @typing.overload
    def GetManifestResourceInfo(self, resourceName: System.String, ) -> System.Reflection.ManifestResourceInfo:
        ...

    @typing.overload
    def GetManifestResourceNames(self, ) -> list[System.String]:
        ...

    @typing.overload
    def GetManifestResourceStream(self, name: System.String, ) -> System.IO.Stream:
        ...

    @typing.overload
    def GetManifestResourceStream(self, type: System.Type, name: System.String, ) -> System.IO.Stream:
        ...

    @typing.overload
    def GetName(self, ) -> System.Reflection.AssemblyName:
        ...

    @typing.overload
    def GetName(self, copiedName: System.Boolean, ) -> System.Reflection.AssemblyName:
        ...

    @typing.overload
    def GetType(self, name: System.String, ) -> System.Type:
        ...

    @typing.overload
    def GetType(self, name: System.String, throwOnError: System.Boolean, ) -> System.Type:
        ...

    @typing.overload
    def GetType(self, name: System.String, throwOnError: System.Boolean, ignoreCase: System.Boolean, ) -> System.Type:
        ...

    @typing.overload
    def IsDefined(self, attributeType: System.Type, inherit: System.Boolean, ) -> System.Boolean:
        ...

    @typing.overload
    def GetCustomAttributesData(self, ) -> System.Collections.Generic.IList[System.Reflection.CustomAttributeData]:
        ...

    @typing.overload
    def GetCustomAttributes(self, inherit: System.Boolean, ) -> list[System.Object]:
        ...

    @typing.overload
    def GetCustomAttributes(self, attributeType: System.Type, inherit: System.Boolean, ) -> list[System.Object]:
        ...

    @typing.overload
    def CreateInstance(self, typeName: System.String, ) -> System.Object:
        ...

    @typing.overload
    def CreateInstance(self, typeName: System.String, ignoreCase: System.Boolean, ) -> System.Object:
        ...

    @typing.overload
    def CreateInstance(self, typeName: System.String, ignoreCase: System.Boolean, bindingAttr: System.Reflection.BindingFlags, binder: System.Reflection.Binder, args: list[System.Object], culture: System.Globalization.CultureInfo, activationAttributes: list[System.Object], ) -> System.Object:
        ...

    @typing.overload
    def GetModule(self, name: System.String, ) -> System.Reflection.Module:
        ...

    @typing.overload
    def GetModules(self, ) -> list[System.Reflection.Module]:
        ...

    @typing.overload
    def GetModules(self, getResourceModules: System.Boolean, ) -> list[System.Reflection.Module]:
        ...

    @typing.overload
    def GetLoadedModules(self, ) -> list[System.Reflection.Module]:
        ...

    @typing.overload
    def GetLoadedModules(self, getResourceModules: System.Boolean, ) -> list[System.Reflection.Module]:
        ...

    @typing.overload
    def GetReferencedAssemblies(self, ) -> list[System.Reflection.AssemblyName]:
        ...

    @typing.overload
    def GetSatelliteAssembly(self, culture: System.Globalization.CultureInfo, ) -> System.Reflection.Assembly:
        ...

    @typing.overload
    def GetSatelliteAssembly(self, culture: System.Globalization.CultureInfo, version: System.Version, ) -> System.Reflection.Assembly:
        ...

    @typing.overload
    def GetFile(self, name: System.String, ) -> System.IO.FileStream:
        ...

    @typing.overload
    def GetFiles(self, ) -> list[System.IO.FileStream]:
        ...

    @typing.overload
    def GetFiles(self, getResourceModules: System.Boolean, ) -> list[System.IO.FileStream]:
        ...

    @typing.overload
    def GetObjectData(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext, ) -> None:
        ...

    @typing.overload
    def ToString(self, ) -> System.String:
        ...

    @typing.overload
    def Equals(self, o: System.Object, ) -> System.Boolean:
        ...

    @typing.overload
    def GetHashCode(self, ) -> System.Int32:
        ...

    @typing.overload
    @staticmethod
    def CreateQualifiedName(assemblyName: System.String, typeName: System.String, ) -> System.String:
        ...

    @typing.overload
    @staticmethod
    def GetAssembly(type: System.Type, ) -> System.Reflection.Assembly:
        ...

    @typing.overload
    @staticmethod
    def GetEntryAssembly() -> System.Reflection.Assembly:
        ...

    @typing.overload
    @staticmethod
    def Load(rawAssembly: list[System.Byte], ) -> System.Reflection.Assembly:
        ...

    @typing.overload
    @staticmethod
    def Load(rawAssembly: list[System.Byte], rawSymbolStore: list[System.Byte], ) -> System.Reflection.Assembly:
        ...

    @typing.overload
    @staticmethod
    def LoadFile(path: System.String, ) -> System.Reflection.Assembly:
        ...

    @typing.overload
    @staticmethod
    def LoadFrom(assemblyFile: System.String, ) -> System.Reflection.Assembly:
        ...

    @typing.overload
    @staticmethod
    def LoadFrom(assemblyFile: System.String, hashValue: list[System.Byte], hashAlgorithm: System.Configuration.Assemblies.AssemblyHashAlgorithm, ) -> System.Reflection.Assembly:
        ...

    @typing.overload
    @staticmethod
    def UnsafeLoadFrom(assemblyFile: System.String, ) -> System.Reflection.Assembly:
        ...

    @typing.overload
    def LoadModule(self, moduleName: System.String, rawModule: list[System.Byte], ) -> System.Reflection.Module:
        ...

    @typing.overload
    def LoadModule(self, moduleName: System.String, rawModule: list[System.Byte], rawSymbolStore: list[System.Byte], ) -> System.Reflection.Module:
        ...

    @typing.overload
    @staticmethod
    def ReflectionOnlyLoad(rawAssembly: list[System.Byte], ) -> System.Reflection.Assembly:
        ...

    @typing.overload
    @staticmethod
    def ReflectionOnlyLoad(assemblyString: System.String, ) -> System.Reflection.Assembly:
        ...

    @typing.overload
    @staticmethod
    def ReflectionOnlyLoadFrom(assemblyFile: System.String, ) -> System.Reflection.Assembly:
        ...

class ICustomAttributeProvider(abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    # methods
    @typing.overload
    @abc.abstractmethod
    def GetCustomAttributes(self, inherit: System.Boolean, ) -> list[System.Object]:
        ...

    @typing.overload
    @abc.abstractmethod
    def GetCustomAttributes(self, attributeType: System.Type, inherit: System.Boolean, ) -> list[System.Object]:
        ...

    @typing.overload
    @abc.abstractmethod
    def IsDefined(self, attributeType: System.Type, inherit: System.Boolean, ) -> System.Boolean:
        ...

class MethodBase(System.Reflection.ICustomAttributeProvider, System.Reflection.MemberInfo, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @abc.abstractmethod
    @property
    def Attributes(self) -> System.Reflection.MethodAttributes:
        ...

    @property
    def MethodImplementationFlags(self) -> System.Reflection.MethodImplAttributes:
        ...

    @property
    def CallingConvention(self) -> System.Reflection.CallingConventions:
        ...

    @property
    def IsAbstract(self) -> System.Boolean:
        ...

    @property
    def IsConstructor(self) -> System.Boolean:
        ...

    @property
    def IsFinal(self) -> System.Boolean:
        ...

    @property
    def IsHideBySig(self) -> System.Boolean:
        ...

    @property
    def IsSpecialName(self) -> System.Boolean:
        ...

    @property
    def IsStatic(self) -> System.Boolean:
        ...

    @property
    def IsVirtual(self) -> System.Boolean:
        ...

    @property
    def IsAssembly(self) -> System.Boolean:
        ...

    @property
    def IsFamily(self) -> System.Boolean:
        ...

    @property
    def IsFamilyAndAssembly(self) -> System.Boolean:
        ...

    @property
    def IsFamilyOrAssembly(self) -> System.Boolean:
        ...

    @property
    def IsPrivate(self) -> System.Boolean:
        ...

    @property
    def IsPublic(self) -> System.Boolean:
        ...

    @property
    def IsConstructedGenericMethod(self) -> System.Boolean:
        ...

    @property
    def IsGenericMethod(self) -> System.Boolean:
        ...

    @property
    def IsGenericMethodDefinition(self) -> System.Boolean:
        ...

    @property
    def ContainsGenericParameters(self) -> System.Boolean:
        ...

    @abc.abstractmethod
    @property
    def MethodHandle(self) -> System.RuntimeMethodHandle:
        ...

    @property
    def IsSecurityCritical(self) -> System.Boolean:
        ...

    @property
    def IsSecuritySafeCritical(self) -> System.Boolean:
        ...

    @property
    def IsSecurityTransparent(self) -> System.Boolean:
        ...

    @abc.abstractmethod
    @property
    def MemberType(self) -> System.Reflection.MemberTypes:
        ...

    @abc.abstractmethod
    @property
    def Name(self) -> System.String:
        ...

    @abc.abstractmethod
    @property
    def DeclaringType(self) -> System.Type:
        ...

    @abc.abstractmethod
    @property
    def ReflectedType(self) -> System.Type:
        ...

    @property
    def Module(self) -> System.Reflection.Module:
        ...

    @property
    def CustomAttributes(self) -> System.Collections.Generic.IEnumerable[System.Reflection.CustomAttributeData]:
        ...

    @property
    def IsCollectible(self) -> System.Boolean:
        ...

    @property
    def MetadataToken(self) -> System.Int32:
        ...

    # methods
    @typing.overload
    def GetGenericArguments(self, ) -> list[System.Type]:
        ...

    @typing.overload
    def Equals(self, obj: System.Object, ) -> System.Boolean:
        ...

    @typing.overload
    def GetHashCode(self, ) -> System.Int32:
        ...

    @typing.overload
    @staticmethod
    def GetMethodFromHandle(handle: System.RuntimeMethodHandle, ) -> System.Reflection.MethodBase:
        ...

    @typing.overload
    @staticmethod
    def GetMethodFromHandle(handle: System.RuntimeMethodHandle, declaringType: System.RuntimeTypeHandle, ) -> System.Reflection.MethodBase:
        ...

    @typing.overload
    @staticmethod
    def GetCurrentMethod() -> System.Reflection.MethodBase:
        ...

    @typing.overload
    @abc.abstractmethod
    def GetParameters(self, ) -> list[System.Reflection.ParameterInfo]:
        ...

    @typing.overload
    @abc.abstractmethod
    def GetMethodImplementationFlags(self, ) -> System.Reflection.MethodImplAttributes:
        ...

    @typing.overload
    def GetMethodBody(self, ) -> System.Reflection.MethodBody:
        ...

    @typing.overload
    def Invoke(self, obj: System.Object, parameters: list[System.Object], ) -> System.Object:
        ...

    @typing.overload
    @abc.abstractmethod
    def Invoke(self, obj: System.Object, invokeAttr: System.Reflection.BindingFlags, binder: System.Reflection.Binder, parameters: list[System.Object], culture: System.Globalization.CultureInfo, ) -> System.Object:
        ...

class MemberTypes(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    Constructor: System.Int32 = Constructor
    Event: System.Int32 = Event
    Field: System.Int32 = Field
    Method: System.Int32 = Method
    Property: System.Int32 = Property
    TypeInfo: System.Int32 = TypeInfo
    Custom: System.Int32 = Custom
    NestedType: System.Int32 = NestedType
    All: System.Int32 = All

class MethodAttributes(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    ReuseSlot: System.Int32 = ReuseSlot
    PrivateScope: System.Int32 = ReuseSlot
    Private: System.Int32 = Private
    FamANDAssem: System.Int32 = FamANDAssem
    Assembly: System.Int32 = Assembly
    Family: System.Int32 = Family
    FamORAssem: System.Int32 = FamORAssem
    Public: System.Int32 = Public
    MemberAccessMask: System.Int32 = MemberAccessMask
    UnmanagedExport: System.Int32 = UnmanagedExport
    Static: System.Int32 = Static
    Final: System.Int32 = Final
    Virtual: System.Int32 = Virtual
    HideBySig: System.Int32 = HideBySig
    NewSlot: System.Int32 = VtableLayoutMask
    VtableLayoutMask: System.Int32 = VtableLayoutMask
    CheckAccessOnOverride: System.Int32 = CheckAccessOnOverride
    Abstract: System.Int32 = Abstract
    SpecialName: System.Int32 = SpecialName
    RTSpecialName: System.Int32 = RTSpecialName
    PinvokeImpl: System.Int32 = PinvokeImpl
    HasSecurity: System.Int32 = HasSecurity
    RequireSecObject: System.Int32 = RequireSecObject
    ReservedMask: System.Int32 = ReservedMask

class MethodImplAttributes(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    IL: System.Int32 = Managed
    Managed: System.Int32 = Managed
    Native: System.Int32 = Native
    OPTIL: System.Int32 = OPTIL
    Runtime: System.Int32 = CodeTypeMask
    CodeTypeMask: System.Int32 = CodeTypeMask
    Unmanaged: System.Int32 = Unmanaged
    ManagedMask: System.Int32 = Unmanaged
    NoInlining: System.Int32 = NoInlining
    ForwardRef: System.Int32 = ForwardRef
    Synchronized: System.Int32 = Synchronized
    NoOptimization: System.Int32 = NoOptimization
    PreserveSig: System.Int32 = PreserveSig
    AggressiveInlining: System.Int32 = AggressiveInlining
    AggressiveOptimization: System.Int32 = AggressiveOptimization
    InternalCall: System.Int32 = InternalCall
    MaxMethodImplVal: System.Int32 = MaxMethodImplVal

class CallingConventions(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    Standard: System.Int32 = Standard
    VarArgs: System.Int32 = VarArgs
    Any: System.Int32 = Any
    HasThis: System.Int32 = HasThis
    ExplicitThis: System.Int32 = ExplicitThis

class CustomAttributeData(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

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
    @typing.overload
    @staticmethod
    def GetCustomAttributes(target: System.Reflection.MemberInfo, ) -> System.Collections.Generic.IList[System.Reflection.CustomAttributeData]:
        ...

    @typing.overload
    @staticmethod
    def GetCustomAttributes(target: System.Reflection.Module, ) -> System.Collections.Generic.IList[System.Reflection.CustomAttributeData]:
        ...

    @typing.overload
    @staticmethod
    def GetCustomAttributes(target: System.Reflection.Assembly, ) -> System.Collections.Generic.IList[System.Reflection.CustomAttributeData]:
        ...

    @typing.overload
    @staticmethod
    def GetCustomAttributes(target: System.Reflection.ParameterInfo, ) -> System.Collections.Generic.IList[System.Reflection.CustomAttributeData]:
        ...

    @typing.overload
    def ToString(self, ) -> System.String:
        ...

    @typing.overload
    def GetHashCode(self, ) -> System.Int32:
        ...

    @typing.overload
    def Equals(self, obj: System.Object, ) -> System.Boolean:
        ...

class IReflect(abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @abc.abstractmethod
    @property
    def UnderlyingSystemType(self) -> System.Type:
        ...

    # methods
    @typing.overload
    @abc.abstractmethod
    def GetMethod(self, name: System.String, bindingAttr: System.Reflection.BindingFlags, binder: System.Reflection.Binder, types: list[System.Type], modifiers: list[System.Reflection.ParameterModifier], ) -> System.Reflection.MethodInfo:
        ...

    @typing.overload
    @abc.abstractmethod
    def GetMethod(self, name: System.String, bindingAttr: System.Reflection.BindingFlags, ) -> System.Reflection.MethodInfo:
        ...

    @typing.overload
    @abc.abstractmethod
    def GetMethods(self, bindingAttr: System.Reflection.BindingFlags, ) -> list[System.Reflection.MethodInfo]:
        ...

    @typing.overload
    @abc.abstractmethod
    def GetField(self, name: System.String, bindingAttr: System.Reflection.BindingFlags, ) -> System.Reflection.FieldInfo:
        ...

    @typing.overload
    @abc.abstractmethod
    def GetFields(self, bindingAttr: System.Reflection.BindingFlags, ) -> list[System.Reflection.FieldInfo]:
        ...

    @typing.overload
    @abc.abstractmethod
    def GetProperty(self, name: System.String, bindingAttr: System.Reflection.BindingFlags, ) -> System.Reflection.PropertyInfo:
        ...

    @typing.overload
    @abc.abstractmethod
    def GetProperty(self, name: System.String, bindingAttr: System.Reflection.BindingFlags, binder: System.Reflection.Binder, returnType: System.Type, types: list[System.Type], modifiers: list[System.Reflection.ParameterModifier], ) -> System.Reflection.PropertyInfo:
        ...

    @typing.overload
    @abc.abstractmethod
    def GetProperties(self, bindingAttr: System.Reflection.BindingFlags, ) -> list[System.Reflection.PropertyInfo]:
        ...

    @typing.overload
    @abc.abstractmethod
    def GetMember(self, name: System.String, bindingAttr: System.Reflection.BindingFlags, ) -> list[System.Reflection.MemberInfo]:
        ...

    @typing.overload
    @abc.abstractmethod
    def GetMembers(self, bindingAttr: System.Reflection.BindingFlags, ) -> list[System.Reflection.MemberInfo]:
        ...

    @typing.overload
    @abc.abstractmethod
    def InvokeMember(self, name: System.String, invokeAttr: System.Reflection.BindingFlags, binder: System.Reflection.Binder, target: System.Object, args: list[System.Object], modifiers: list[System.Reflection.ParameterModifier], culture: System.Globalization.CultureInfo, namedParameters: list[System.String], ) -> System.Object:
        ...

class GenericParameterAttributes(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    None_: System.Int32 = None
    Covariant: System.Int32 = Covariant
    Contravariant: System.Int32 = Contravariant
    VarianceMask: System.Int32 = VarianceMask
    ReferenceTypeConstraint: System.Int32 = ReferenceTypeConstraint
    NotNullableValueTypeConstraint: System.Int32 = NotNullableValueTypeConstraint
    DefaultConstructorConstraint: System.Int32 = DefaultConstructorConstraint
    SpecialConstraintMask: System.Int32 = SpecialConstraintMask

class TypeAttributes(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    NotPublic: System.Int32 = NotPublic
    AutoLayout: System.Int32 = NotPublic
    AnsiClass: System.Int32 = NotPublic
    Class: System.Int32 = NotPublic
    Public: System.Int32 = Public
    NestedPublic: System.Int32 = NestedPublic
    NestedPrivate: System.Int32 = NestedPrivate
    NestedFamily: System.Int32 = NestedFamily
    NestedAssembly: System.Int32 = NestedAssembly
    NestedFamANDAssem: System.Int32 = NestedFamANDAssem
    NestedFamORAssem: System.Int32 = VisibilityMask
    VisibilityMask: System.Int32 = VisibilityMask
    SequentialLayout: System.Int32 = SequentialLayout
    ExplicitLayout: System.Int32 = ExplicitLayout
    LayoutMask: System.Int32 = LayoutMask
    Interface: System.Int32 = ClassSemanticsMask
    ClassSemanticsMask: System.Int32 = ClassSemanticsMask
    Abstract: System.Int32 = Abstract
    Sealed: System.Int32 = Sealed
    SpecialName: System.Int32 = SpecialName
    RTSpecialName: System.Int32 = RTSpecialName
    Import: System.Int32 = Import
    Serializable: System.Int32 = Serializable
    WindowsRuntime: System.Int32 = WindowsRuntime
    UnicodeClass: System.Int32 = UnicodeClass
    AutoClass: System.Int32 = AutoClass
    CustomFormatClass: System.Int32 = StringFormatMask
    StringFormatMask: System.Int32 = StringFormatMask
    HasSecurity: System.Int32 = HasSecurity
    ReservedMask: System.Int32 = ReservedMask
    BeforeFieldInit: System.Int32 = BeforeFieldInit
    CustomFormatMask: System.Int32 = CustomFormatMask

class ConstructorInfo(System.Reflection.ICustomAttributeProvider, System.Reflection.MethodBase, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def MemberType(self) -> System.Reflection.MemberTypes:
        ...

    @abc.abstractmethod
    @property
    def Attributes(self) -> System.Reflection.MethodAttributes:
        ...

    @property
    def MethodImplementationFlags(self) -> System.Reflection.MethodImplAttributes:
        ...

    @property
    def CallingConvention(self) -> System.Reflection.CallingConventions:
        ...

    @property
    def IsAbstract(self) -> System.Boolean:
        ...

    @property
    def IsConstructor(self) -> System.Boolean:
        ...

    @property
    def IsFinal(self) -> System.Boolean:
        ...

    @property
    def IsHideBySig(self) -> System.Boolean:
        ...

    @property
    def IsSpecialName(self) -> System.Boolean:
        ...

    @property
    def IsStatic(self) -> System.Boolean:
        ...

    @property
    def IsVirtual(self) -> System.Boolean:
        ...

    @property
    def IsAssembly(self) -> System.Boolean:
        ...

    @property
    def IsFamily(self) -> System.Boolean:
        ...

    @property
    def IsFamilyAndAssembly(self) -> System.Boolean:
        ...

    @property
    def IsFamilyOrAssembly(self) -> System.Boolean:
        ...

    @property
    def IsPrivate(self) -> System.Boolean:
        ...

    @property
    def IsPublic(self) -> System.Boolean:
        ...

    @property
    def IsConstructedGenericMethod(self) -> System.Boolean:
        ...

    @property
    def IsGenericMethod(self) -> System.Boolean:
        ...

    @property
    def IsGenericMethodDefinition(self) -> System.Boolean:
        ...

    @property
    def ContainsGenericParameters(self) -> System.Boolean:
        ...

    @abc.abstractmethod
    @property
    def MethodHandle(self) -> System.RuntimeMethodHandle:
        ...

    @property
    def IsSecurityCritical(self) -> System.Boolean:
        ...

    @property
    def IsSecuritySafeCritical(self) -> System.Boolean:
        ...

    @property
    def IsSecurityTransparent(self) -> System.Boolean:
        ...

    @abc.abstractmethod
    @property
    def Name(self) -> System.String:
        ...

    @abc.abstractmethod
    @property
    def DeclaringType(self) -> System.Type:
        ...

    @abc.abstractmethod
    @property
    def ReflectedType(self) -> System.Type:
        ...

    @property
    def Module(self) -> System.Reflection.Module:
        ...

    @property
    def CustomAttributes(self) -> System.Collections.Generic.IEnumerable[System.Reflection.CustomAttributeData]:
        ...

    @property
    def IsCollectible(self) -> System.Boolean:
        ...

    @property
    def MetadataToken(self) -> System.Int32:
        ...

    # methods
    @typing.overload
    def Invoke(self, parameters: list[System.Object], ) -> System.Object:
        ...

    @typing.overload
    @abc.abstractmethod
    def Invoke(self, invokeAttr: System.Reflection.BindingFlags, binder: System.Reflection.Binder, parameters: list[System.Object], culture: System.Globalization.CultureInfo, ) -> System.Object:
        ...

    @typing.overload
    def Equals(self, obj: System.Object, ) -> System.Boolean:
        ...

    @typing.overload
    def GetHashCode(self, ) -> System.Int32:
        ...

class Binder(System.Object, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    # methods
    @typing.overload
    @abc.abstractmethod
    def BindToField(self, bindingAttr: System.Reflection.BindingFlags, match: list[System.Reflection.FieldInfo], value: System.Object, culture: System.Globalization.CultureInfo, ) -> System.Reflection.FieldInfo:
        ...

    @typing.overload
    @abc.abstractmethod
    def BindToMethod(self, bindingAttr: System.Reflection.BindingFlags, match: list[System.Reflection.MethodBase], args: ref[list[System.Object]], modifiers: list[System.Reflection.ParameterModifier], culture: System.Globalization.CultureInfo, names: list[System.String], state: ref[System.Object], ) -> System.Reflection.MethodBase:
        ...

    @typing.overload
    @abc.abstractmethod
    def ChangeType(self, value: System.Object, type: System.Type, culture: System.Globalization.CultureInfo, ) -> System.Object:
        ...

    @typing.overload
    @abc.abstractmethod
    def ReorderArgumentArray(self, args: ref[list[System.Object]], state: System.Object, ) -> None:
        ...

    @typing.overload
    @abc.abstractmethod
    def SelectMethod(self, bindingAttr: System.Reflection.BindingFlags, match: list[System.Reflection.MethodBase], types: list[System.Type], modifiers: list[System.Reflection.ParameterModifier], ) -> System.Reflection.MethodBase:
        ...

    @typing.overload
    @abc.abstractmethod
    def SelectProperty(self, bindingAttr: System.Reflection.BindingFlags, match: list[System.Reflection.PropertyInfo], returnType: System.Type, indexes: list[System.Type], modifiers: list[System.Reflection.ParameterModifier], ) -> System.Reflection.PropertyInfo:
        ...

class BindingFlags(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    Default: System.Int32 = Default
    IgnoreCase: System.Int32 = IgnoreCase
    DeclaredOnly: System.Int32 = DeclaredOnly
    Instance: System.Int32 = Instance
    Static: System.Int32 = Static
    Public: System.Int32 = Public
    NonPublic: System.Int32 = NonPublic
    FlattenHierarchy: System.Int32 = FlattenHierarchy
    InvokeMethod: System.Int32 = InvokeMethod
    CreateInstance: System.Int32 = CreateInstance
    GetField: System.Int32 = GetField
    SetField: System.Int32 = SetField
    GetProperty: System.Int32 = GetProperty
    SetProperty: System.Int32 = SetProperty
    PutDispProperty: System.Int32 = PutDispProperty
    PutRefDispProperty: System.Int32 = PutRefDispProperty
    ExactBinding: System.Int32 = ExactBinding
    SuppressChangeType: System.Int32 = SuppressChangeType
    OptionalParamBinding: System.Int32 = OptionalParamBinding
    IgnoreReturn: System.Int32 = IgnoreReturn
    DoNotWrapExceptions: System.Int32 = DoNotWrapExceptions

class FieldInfo(System.Reflection.ICustomAttributeProvider, System.Reflection.MemberInfo, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def MemberType(self) -> System.Reflection.MemberTypes:
        ...

    @abc.abstractmethod
    @property
    def Attributes(self) -> System.Reflection.FieldAttributes:
        ...

    @abc.abstractmethod
    @property
    def FieldType(self) -> System.Type:
        ...

    @property
    def IsInitOnly(self) -> System.Boolean:
        ...

    @property
    def IsLiteral(self) -> System.Boolean:
        ...

    @property
    def IsNotSerialized(self) -> System.Boolean:
        ...

    @property
    def IsPinvokeImpl(self) -> System.Boolean:
        ...

    @property
    def IsSpecialName(self) -> System.Boolean:
        ...

    @property
    def IsStatic(self) -> System.Boolean:
        ...

    @property
    def IsAssembly(self) -> System.Boolean:
        ...

    @property
    def IsFamily(self) -> System.Boolean:
        ...

    @property
    def IsFamilyAndAssembly(self) -> System.Boolean:
        ...

    @property
    def IsFamilyOrAssembly(self) -> System.Boolean:
        ...

    @property
    def IsPrivate(self) -> System.Boolean:
        ...

    @property
    def IsPublic(self) -> System.Boolean:
        ...

    @property
    def IsSecurityCritical(self) -> System.Boolean:
        ...

    @property
    def IsSecuritySafeCritical(self) -> System.Boolean:
        ...

    @property
    def IsSecurityTransparent(self) -> System.Boolean:
        ...

    @abc.abstractmethod
    @property
    def FieldHandle(self) -> System.RuntimeFieldHandle:
        ...

    @abc.abstractmethod
    @property
    def Name(self) -> System.String:
        ...

    @abc.abstractmethod
    @property
    def DeclaringType(self) -> System.Type:
        ...

    @abc.abstractmethod
    @property
    def ReflectedType(self) -> System.Type:
        ...

    @property
    def Module(self) -> System.Reflection.Module:
        ...

    @property
    def CustomAttributes(self) -> System.Collections.Generic.IEnumerable[System.Reflection.CustomAttributeData]:
        ...

    @property
    def IsCollectible(self) -> System.Boolean:
        ...

    @property
    def MetadataToken(self) -> System.Int32:
        ...

    # methods
    @typing.overload
    @staticmethod
    def GetFieldFromHandle(handle: System.RuntimeFieldHandle, ) -> System.Reflection.FieldInfo:
        ...

    @typing.overload
    @staticmethod
    def GetFieldFromHandle(handle: System.RuntimeFieldHandle, declaringType: System.RuntimeTypeHandle, ) -> System.Reflection.FieldInfo:
        ...

    @typing.overload
    def Equals(self, obj: System.Object, ) -> System.Boolean:
        ...

    @typing.overload
    def GetHashCode(self, ) -> System.Int32:
        ...

    @typing.overload
    @abc.abstractmethod
    def GetValue(self, obj: System.Object, ) -> System.Object:
        ...

    @typing.overload
    def SetValue(self, obj: System.Object, value: System.Object, ) -> None:
        ...

    @typing.overload
    @abc.abstractmethod
    def SetValue(self, obj: System.Object, value: System.Object, invokeAttr: System.Reflection.BindingFlags, binder: System.Reflection.Binder, culture: System.Globalization.CultureInfo, ) -> None:
        ...

    @typing.overload
    def SetValueDirect(self, obj: System.TypedReference, value: System.Object, ) -> None:
        ...

    @typing.overload
    def GetValueDirect(self, obj: System.TypedReference, ) -> System.Object:
        ...

    @typing.overload
    def GetRawConstantValue(self, ) -> System.Object:
        ...

    @typing.overload
    def GetOptionalCustomModifiers(self, ) -> list[System.Type]:
        ...

    @typing.overload
    def GetRequiredCustomModifiers(self, ) -> list[System.Type]:
        ...

class ParameterModifier(System.ValueType):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def Item(self) -> System.Boolean:
        ...
    @Item.setter
    def Item(self, val: System.Boolean):
        ...

    # methods
    @typing.overload
    def __init__(self, parameterCount: System.Int32, ):
        ...

class PropertyInfo(System.Reflection.ICustomAttributeProvider, System.Reflection.MemberInfo, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def MemberType(self) -> System.Reflection.MemberTypes:
        ...

    @abc.abstractmethod
    @property
    def PropertyType(self) -> System.Type:
        ...

    @abc.abstractmethod
    @property
    def Attributes(self) -> System.Reflection.PropertyAttributes:
        ...

    @property
    def IsSpecialName(self) -> System.Boolean:
        ...

    @abc.abstractmethod
    @property
    def CanRead(self) -> System.Boolean:
        ...

    @abc.abstractmethod
    @property
    def CanWrite(self) -> System.Boolean:
        ...

    @property
    def GetMethod(self) -> System.Reflection.MethodInfo:
        ...

    @property
    def SetMethod(self) -> System.Reflection.MethodInfo:
        ...

    @abc.abstractmethod
    @property
    def Name(self) -> System.String:
        ...

    @abc.abstractmethod
    @property
    def DeclaringType(self) -> System.Type:
        ...

    @abc.abstractmethod
    @property
    def ReflectedType(self) -> System.Type:
        ...

    @property
    def Module(self) -> System.Reflection.Module:
        ...

    @property
    def CustomAttributes(self) -> System.Collections.Generic.IEnumerable[System.Reflection.CustomAttributeData]:
        ...

    @property
    def IsCollectible(self) -> System.Boolean:
        ...

    @property
    def MetadataToken(self) -> System.Int32:
        ...

    # methods
    @typing.overload
    @abc.abstractmethod
    def GetIndexParameters(self, ) -> list[System.Reflection.ParameterInfo]:
        ...

    @typing.overload
    def GetAccessors(self, ) -> list[System.Reflection.MethodInfo]:
        ...

    @typing.overload
    @abc.abstractmethod
    def GetAccessors(self, nonPublic: System.Boolean, ) -> list[System.Reflection.MethodInfo]:
        ...

    @typing.overload
    def GetGetMethod(self, ) -> System.Reflection.MethodInfo:
        ...

    @typing.overload
    @abc.abstractmethod
    def GetGetMethod(self, nonPublic: System.Boolean, ) -> System.Reflection.MethodInfo:
        ...

    @typing.overload
    def GetSetMethod(self, ) -> System.Reflection.MethodInfo:
        ...

    @typing.overload
    @abc.abstractmethod
    def GetSetMethod(self, nonPublic: System.Boolean, ) -> System.Reflection.MethodInfo:
        ...

    @typing.overload
    def GetOptionalCustomModifiers(self, ) -> list[System.Type]:
        ...

    @typing.overload
    def GetRequiredCustomModifiers(self, ) -> list[System.Type]:
        ...

    @typing.overload
    def GetValue(self, obj: System.Object, ) -> System.Object:
        ...

    @typing.overload
    def GetValue(self, obj: System.Object, index: list[System.Object], ) -> System.Object:
        ...

    @typing.overload
    @abc.abstractmethod
    def GetValue(self, obj: System.Object, invokeAttr: System.Reflection.BindingFlags, binder: System.Reflection.Binder, index: list[System.Object], culture: System.Globalization.CultureInfo, ) -> System.Object:
        ...

    @typing.overload
    def GetConstantValue(self, ) -> System.Object:
        ...

    @typing.overload
    def GetRawConstantValue(self, ) -> System.Object:
        ...

    @typing.overload
    def SetValue(self, obj: System.Object, value: System.Object, ) -> None:
        ...

    @typing.overload
    def SetValue(self, obj: System.Object, value: System.Object, index: list[System.Object], ) -> None:
        ...

    @typing.overload
    @abc.abstractmethod
    def SetValue(self, obj: System.Object, value: System.Object, invokeAttr: System.Reflection.BindingFlags, binder: System.Reflection.Binder, index: list[System.Object], culture: System.Globalization.CultureInfo, ) -> None:
        ...

    @typing.overload
    def Equals(self, obj: System.Object, ) -> System.Boolean:
        ...

    @typing.overload
    def GetHashCode(self, ) -> System.Int32:
        ...

class InterfaceMapping(System.ValueType):
    @typing.overload
    def __init__(self, **kwargs):
        self.TargetType: System.Type
        self.InterfaceType: System.Type
        self.TargetMethods: list[System.Reflection.MethodInfo]
        self.InterfaceMethods: list[System.Reflection.MethodInfo]
        ...

    # properties
    # methods
class TypeFilter(System.ICloneable, System.Runtime.Serialization.ISerializable, System.MulticastDelegate):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def Target(self) -> System.Object:
        ...

    @property
    def Method(self) -> System.Reflection.MethodInfo:
        ...

    # methods
    @typing.overload
    def __init__(self, object: System.Object, method: System.IntPtr, ):
        ...

    @typing.overload
    def Invoke(self, m: System.Type, filterCriteria: System.Object, ) -> System.Boolean:
        ...

    @typing.overload
    def BeginInvoke(self, m: System.Type, filterCriteria: System.Object, callback: System.AsyncCallback, object: System.Object, ) -> System.IAsyncResult:
        ...

    @typing.overload
    def EndInvoke(self, result: System.IAsyncResult, ) -> System.Boolean:
        ...

class MemberFilter(System.ICloneable, System.Runtime.Serialization.ISerializable, System.MulticastDelegate):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def Target(self) -> System.Object:
        ...

    @property
    def Method(self) -> System.Reflection.MethodInfo:
        ...

    # methods
    @typing.overload
    def __init__(self, object: System.Object, method: System.IntPtr, ):
        ...

    @typing.overload
    def Invoke(self, m: System.Reflection.MemberInfo, filterCriteria: System.Object, ) -> System.Boolean:
        ...

    @typing.overload
    def BeginInvoke(self, m: System.Reflection.MemberInfo, filterCriteria: System.Object, callback: System.AsyncCallback, object: System.Object, ) -> System.IAsyncResult:
        ...

    @typing.overload
    def EndInvoke(self, result: System.IAsyncResult, ) -> System.Boolean:
        ...

class AssemblyName(System.ICloneable, System.Runtime.Serialization.IDeserializationCallback, System.Runtime.Serialization.ISerializable, System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def Name(self) -> System.String:
        ...
    @Name.setter
    def Name(self, val: System.String):
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
    def CultureName(self) -> System.String:
        ...
    @CultureName.setter
    def CultureName(self, val: System.String):
        ...

    @property
    def CodeBase(self) -> System.String:
        ...
    @CodeBase.setter
    def CodeBase(self, val: System.String):
        ...

    @property
    def EscapedCodeBase(self) -> System.String:
        ...

    @property
    def ProcessorArchitecture(self) -> System.Reflection.ProcessorArchitecture:
        ...
    @ProcessorArchitecture.setter
    def ProcessorArchitecture(self, val: System.Reflection.ProcessorArchitecture):
        ...

    @property
    def ContentType(self) -> System.Reflection.AssemblyContentType:
        ...
    @ContentType.setter
    def ContentType(self, val: System.Reflection.AssemblyContentType):
        ...

    @property
    def Flags(self) -> System.Reflection.AssemblyNameFlags:
        ...
    @Flags.setter
    def Flags(self, val: System.Reflection.AssemblyNameFlags):
        ...

    @property
    def HashAlgorithm(self) -> System.Configuration.Assemblies.AssemblyHashAlgorithm:
        ...
    @HashAlgorithm.setter
    def HashAlgorithm(self, val: System.Configuration.Assemblies.AssemblyHashAlgorithm):
        ...

    @property
    def VersionCompatibility(self) -> System.Configuration.Assemblies.AssemblyVersionCompatibility:
        ...
    @VersionCompatibility.setter
    def VersionCompatibility(self, val: System.Configuration.Assemblies.AssemblyVersionCompatibility):
        ...

    @property
    def KeyPair(self) -> System.Reflection.StrongNameKeyPair:
        ...
    @KeyPair.setter
    def KeyPair(self, val: System.Reflection.StrongNameKeyPair):
        ...

    @property
    def FullName(self) -> System.String:
        ...

    # methods
    @typing.overload
    def __init__(self, assemblyName: System.String, ):
        ...

    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def Clone(self, ) -> System.Object:
        ...

    @typing.overload
    @staticmethod
    def GetAssemblyName(assemblyFile: System.String, ) -> System.Reflection.AssemblyName:
        ...

    @typing.overload
    def GetPublicKey(self, ) -> list[System.Byte]:
        ...

    @typing.overload
    def SetPublicKey(self, publicKey: list[System.Byte], ) -> None:
        ...

    @typing.overload
    def GetPublicKeyToken(self, ) -> list[System.Byte]:
        ...

    @typing.overload
    def SetPublicKeyToken(self, publicKeyToken: list[System.Byte], ) -> None:
        ...

    @typing.overload
    def ToString(self, ) -> System.String:
        ...

    @typing.overload
    def GetObjectData(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext, ) -> None:
        ...

    @typing.overload
    def OnDeserialization(self, sender: System.Object, ) -> None:
        ...

    @typing.overload
    @staticmethod
    def ReferenceMatchesDefinition(reference: System.Reflection.AssemblyName, definition: System.Reflection.AssemblyName, ) -> System.Boolean:
        ...

class EventInfo(System.Reflection.ICustomAttributeProvider, System.Reflection.MemberInfo, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def MemberType(self) -> System.Reflection.MemberTypes:
        ...

    @abc.abstractmethod
    @property
    def Attributes(self) -> System.Reflection.EventAttributes:
        ...

    @property
    def IsSpecialName(self) -> System.Boolean:
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
    def IsMulticast(self) -> System.Boolean:
        ...

    @property
    def EventHandlerType(self) -> System.Type:
        ...

    @abc.abstractmethod
    @property
    def Name(self) -> System.String:
        ...

    @abc.abstractmethod
    @property
    def DeclaringType(self) -> System.Type:
        ...

    @abc.abstractmethod
    @property
    def ReflectedType(self) -> System.Type:
        ...

    @property
    def Module(self) -> System.Reflection.Module:
        ...

    @property
    def CustomAttributes(self) -> System.Collections.Generic.IEnumerable[System.Reflection.CustomAttributeData]:
        ...

    @property
    def IsCollectible(self) -> System.Boolean:
        ...

    @property
    def MetadataToken(self) -> System.Int32:
        ...

    # methods
    @typing.overload
    def GetOtherMethods(self, ) -> list[System.Reflection.MethodInfo]:
        ...

    @typing.overload
    def GetOtherMethods(self, nonPublic: System.Boolean, ) -> list[System.Reflection.MethodInfo]:
        ...

    @typing.overload
    def GetAddMethod(self, ) -> System.Reflection.MethodInfo:
        ...

    @typing.overload
    def GetRemoveMethod(self, ) -> System.Reflection.MethodInfo:
        ...

    @typing.overload
    def GetRaiseMethod(self, ) -> System.Reflection.MethodInfo:
        ...

    @typing.overload
    @abc.abstractmethod
    def GetAddMethod(self, nonPublic: System.Boolean, ) -> System.Reflection.MethodInfo:
        ...

    @typing.overload
    @abc.abstractmethod
    def GetRemoveMethod(self, nonPublic: System.Boolean, ) -> System.Reflection.MethodInfo:
        ...

    @typing.overload
    @abc.abstractmethod
    def GetRaiseMethod(self, nonPublic: System.Boolean, ) -> System.Reflection.MethodInfo:
        ...

    @typing.overload
    def AddEventHandler(self, target: System.Object, handler: System.Delegate, ) -> None:
        ...

    @typing.overload
    def RemoveEventHandler(self, target: System.Object, handler: System.Delegate, ) -> None:
        ...

    @typing.overload
    def Equals(self, obj: System.Object, ) -> System.Boolean:
        ...

    @typing.overload
    def GetHashCode(self, ) -> System.Int32:
        ...

class ParameterAttributes(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    None_: System.Int32 = None
    In: System.Int32 = In
    Out: System.Int32 = Out
    Lcid: System.Int32 = Lcid
    Retval: System.Int32 = Retval
    Optional: System.Int32 = Optional
    HasDefault: System.Int32 = HasDefault
    HasFieldMarshal: System.Int32 = HasFieldMarshal
    Reserved3: System.Int32 = Reserved3
    Reserved4: System.Int32 = Reserved4
    ReservedMask: System.Int32 = ReservedMask

class PortableExecutableKinds(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    NotAPortableExecutableImage: System.Int32 = NotAPortableExecutableImage
    ILOnly: System.Int32 = ILOnly
    Required32Bit: System.Int32 = Required32Bit
    PE32Plus: System.Int32 = PE32Plus
    Unmanaged32Bit: System.Int32 = Unmanaged32Bit
    Preferred32Bit: System.Int32 = Preferred32Bit

class ImageFileMachine(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    I386: System.Int32 = I386
    ARM: System.Int32 = ARM
    IA64: System.Int32 = IA64
    AMD64: System.Int32 = AMD64

class TypeInfo(System.Reflection.ICustomAttributeProvider, System.Reflection.IReflect, System.Reflection.IReflectableType, System.Type, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def GenericTypeParameters(self) -> list[System.Type]:
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
    def IsInterface(self) -> System.Boolean:
        ...

    @property
    def MemberType(self) -> System.Reflection.MemberTypes:
        ...

    @abc.abstractmethod
    @property
    def Namespace(self) -> System.String:
        ...

    @abc.abstractmethod
    @property
    def AssemblyQualifiedName(self) -> System.String:
        ...

    @abc.abstractmethod
    @property
    def FullName(self) -> System.String:
        ...

    @abc.abstractmethod
    @property
    def Assembly(self) -> System.Reflection.Assembly:
        ...

    @abc.abstractmethod
    @property
    def Module(self) -> System.Reflection.Module:
        ...

    @property
    def IsNested(self) -> System.Boolean:
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

    @abc.abstractmethod
    @property
    def UnderlyingSystemType(self) -> System.Type:
        ...

    @property
    def IsTypeDefinition(self) -> System.Boolean:
        ...

    @property
    def IsArray(self) -> System.Boolean:
        ...

    @property
    def IsByRef(self) -> System.Boolean:
        ...

    @property
    def IsPointer(self) -> System.Boolean:
        ...

    @property
    def IsConstructedGenericType(self) -> System.Boolean:
        ...

    @property
    def IsGenericParameter(self) -> System.Boolean:
        ...

    @property
    def IsGenericTypeParameter(self) -> System.Boolean:
        ...

    @property
    def IsGenericMethodParameter(self) -> System.Boolean:
        ...

    @property
    def IsGenericType(self) -> System.Boolean:
        ...

    @property
    def IsGenericTypeDefinition(self) -> System.Boolean:
        ...

    @property
    def IsSZArray(self) -> System.Boolean:
        ...

    @property
    def IsVariableBoundArray(self) -> System.Boolean:
        ...

    @property
    def IsByRefLike(self) -> System.Boolean:
        ...

    @property
    def HasElementType(self) -> System.Boolean:
        ...

    @property
    def GenericTypeArguments(self) -> list[System.Type]:
        ...

    @property
    def GenericParameterPosition(self) -> System.Int32:
        ...

    @property
    def GenericParameterAttributes(self) -> System.Reflection.GenericParameterAttributes:
        ...

    @property
    def Attributes(self) -> System.Reflection.TypeAttributes:
        ...

    @property
    def IsAbstract(self) -> System.Boolean:
        ...

    @property
    def IsImport(self) -> System.Boolean:
        ...

    @property
    def IsSealed(self) -> System.Boolean:
        ...

    @property
    def IsSpecialName(self) -> System.Boolean:
        ...

    @property
    def IsClass(self) -> System.Boolean:
        ...

    @property
    def IsNestedAssembly(self) -> System.Boolean:
        ...

    @property
    def IsNestedFamANDAssem(self) -> System.Boolean:
        ...

    @property
    def IsNestedFamily(self) -> System.Boolean:
        ...

    @property
    def IsNestedFamORAssem(self) -> System.Boolean:
        ...

    @property
    def IsNestedPrivate(self) -> System.Boolean:
        ...

    @property
    def IsNestedPublic(self) -> System.Boolean:
        ...

    @property
    def IsNotPublic(self) -> System.Boolean:
        ...

    @property
    def IsPublic(self) -> System.Boolean:
        ...

    @property
    def IsAutoLayout(self) -> System.Boolean:
        ...

    @property
    def IsExplicitLayout(self) -> System.Boolean:
        ...

    @property
    def IsLayoutSequential(self) -> System.Boolean:
        ...

    @property
    def IsAnsiClass(self) -> System.Boolean:
        ...

    @property
    def IsAutoClass(self) -> System.Boolean:
        ...

    @property
    def IsUnicodeClass(self) -> System.Boolean:
        ...

    @property
    def IsCOMObject(self) -> System.Boolean:
        ...

    @property
    def IsContextful(self) -> System.Boolean:
        ...

    @property
    def IsEnum(self) -> System.Boolean:
        ...

    @property
    def IsMarshalByRef(self) -> System.Boolean:
        ...

    @property
    def IsPrimitive(self) -> System.Boolean:
        ...

    @property
    def IsValueType(self) -> System.Boolean:
        ...

    @property
    def IsSignatureType(self) -> System.Boolean:
        ...

    @property
    def IsSecurityCritical(self) -> System.Boolean:
        ...

    @property
    def IsSecuritySafeCritical(self) -> System.Boolean:
        ...

    @property
    def IsSecurityTransparent(self) -> System.Boolean:
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

    @abc.abstractmethod
    @property
    def GUID(self) -> System.Guid:
        ...

    @abc.abstractmethod
    @property
    def BaseType(self) -> System.Type:
        ...

    @property
    def IsSerializable(self) -> System.Boolean:
        ...

    @property
    def ContainsGenericParameters(self) -> System.Boolean:
        ...

    @property
    def IsVisible(self) -> System.Boolean:
        ...

    @abc.abstractmethod
    @property
    def Name(self) -> System.String:
        ...

    @property
    def CustomAttributes(self) -> System.Collections.Generic.IEnumerable[System.Reflection.CustomAttributeData]:
        ...

    @property
    def IsCollectible(self) -> System.Boolean:
        ...

    @property
    def MetadataToken(self) -> System.Int32:
        ...

    # methods
    @typing.overload
    def AsType(self, ) -> System.Type:
        ...

    @typing.overload
    def GetDeclaredEvent(self, name: System.String, ) -> System.Reflection.EventInfo:
        ...

    @typing.overload
    def GetDeclaredField(self, name: System.String, ) -> System.Reflection.FieldInfo:
        ...

    @typing.overload
    def GetDeclaredMethod(self, name: System.String, ) -> System.Reflection.MethodInfo:
        ...

    @typing.overload
    def GetDeclaredNestedType(self, name: System.String, ) -> System.Reflection.TypeInfo:
        ...

    @typing.overload
    def GetDeclaredProperty(self, name: System.String, ) -> System.Reflection.PropertyInfo:
        ...

    @typing.overload
    def GetDeclaredMethods(self, name: System.String, ) -> System.Collections.Generic.IEnumerable[System.Reflection.MethodInfo]:
        ...

    @typing.overload
    def IsAssignableFrom(self, typeInfo: System.Reflection.TypeInfo, ) -> System.Boolean:
        ...

class ManifestResourceInfo(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def ReferencedAssembly(self) -> System.Reflection.Assembly:
        ...

    @property
    def FileName(self) -> System.String:
        ...

    @property
    def ResourceLocation(self) -> System.Reflection.ResourceLocation:
        ...

    # methods
    @typing.overload
    def __init__(self, containingAssembly: System.Reflection.Assembly, containingFileName: System.String, resourceLocation: System.Reflection.ResourceLocation, ):
        ...

class MethodBody(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def LocalSignatureMetadataToken(self) -> System.Int32:
        ...

    @property
    def LocalVariables(self) -> System.Collections.Generic.IList[System.Reflection.LocalVariableInfo]:
        ...

    @property
    def MaxStackSize(self) -> System.Int32:
        ...

    @property
    def InitLocals(self) -> System.Boolean:
        ...

    @property
    def ExceptionHandlingClauses(self) -> System.Collections.Generic.IList[System.Reflection.ExceptionHandlingClause]:
        ...

    # methods
    @typing.overload
    def GetILAsByteArray(self, ) -> list[System.Byte]:
        ...

class CustomAttributeTypedArgument(System.ValueType):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def ArgumentType(self) -> System.Type:
        ...

    @property
    def Value(self) -> System.Object:
        ...

    # methods
    @typing.overload
    def __init__(self, argumentType: System.Type, value: System.Object, ):
        ...

    @typing.overload
    def __init__(self, value: System.Object, ):
        ...

    @typing.overload
    def ToString(self, ) -> System.String:
        ...

    @typing.overload
    def GetHashCode(self, ) -> System.Int32:
        ...

    @typing.overload
    def Equals(self, obj: System.Object, ) -> System.Boolean:
        ...

class CustomAttributeNamedArgument(System.ValueType):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def MemberInfo(self) -> System.Reflection.MemberInfo:
        ...

    @property
    def TypedValue(self) -> System.Reflection.CustomAttributeTypedArgument:
        ...

    @property
    def MemberName(self) -> System.String:
        ...

    @property
    def IsField(self) -> System.Boolean:
        ...

    # methods
    @typing.overload
    def __init__(self, memberInfo: System.Reflection.MemberInfo, value: System.Object, ):
        ...

    @typing.overload
    def __init__(self, memberInfo: System.Reflection.MemberInfo, typedArgument: System.Reflection.CustomAttributeTypedArgument, ):
        ...

    @typing.overload
    def ToString(self, ) -> System.String:
        ...

    @typing.overload
    def GetHashCode(self, ) -> System.Int32:
        ...

    @typing.overload
    def Equals(self, obj: System.Object, ) -> System.Boolean:
        ...

class FieldAttributes(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    PrivateScope: System.Int32 = PrivateScope
    Private: System.Int32 = Private
    FamANDAssem: System.Int32 = FamANDAssem
    Assembly: System.Int32 = Assembly
    Family: System.Int32 = Family
    FamORAssem: System.Int32 = FamORAssem
    Public: System.Int32 = Public
    FieldAccessMask: System.Int32 = FieldAccessMask
    Static: System.Int32 = Static
    InitOnly: System.Int32 = InitOnly
    Literal: System.Int32 = Literal
    NotSerialized: System.Int32 = NotSerialized
    HasFieldRVA: System.Int32 = HasFieldRVA
    SpecialName: System.Int32 = SpecialName
    RTSpecialName: System.Int32 = RTSpecialName
    HasFieldMarshal: System.Int32 = HasFieldMarshal
    PinvokeImpl: System.Int32 = PinvokeImpl
    HasDefault: System.Int32 = HasDefault
    ReservedMask: System.Int32 = ReservedMask

class PropertyAttributes(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    None_: System.Int32 = None
    SpecialName: System.Int32 = SpecialName
    RTSpecialName: System.Int32 = RTSpecialName
    HasDefault: System.Int32 = HasDefault
    Reserved2: System.Int32 = Reserved2
    Reserved3: System.Int32 = Reserved3
    Reserved4: System.Int32 = Reserved4
    ReservedMask: System.Int32 = ReservedMask

class ProcessorArchitecture(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    None_: System.Int32 = None
    MSIL: System.Int32 = MSIL
    X86: System.Int32 = X86
    IA64: System.Int32 = IA64
    Amd64: System.Int32 = Amd64
    Arm: System.Int32 = Arm

class AssemblyContentType(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    Default: System.Int32 = Default
    WindowsRuntime: System.Int32 = WindowsRuntime

class AssemblyNameFlags(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    None_: System.Int32 = None
    PublicKey: System.Int32 = PublicKey
    Retargetable: System.Int32 = Retargetable
    EnableJITcompileOptimizer: System.Int32 = EnableJITcompileOptimizer
    EnableJITcompileTracking: System.Int32 = EnableJITcompileTracking

class StrongNameKeyPair(System.Runtime.Serialization.IDeserializationCallback, System.Runtime.Serialization.ISerializable, System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def PublicKey(self) -> list[System.Byte]:
        ...

    # methods
    @typing.overload
    def __init__(self, keyPairFile: System.IO.FileStream, ):
        ...

    @typing.overload
    def __init__(self, keyPairArray: list[System.Byte], ):
        ...

    @typing.overload
    def __init__(self, keyPairContainer: System.String, ):
        ...

class EventAttributes(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    None_: System.Int32 = None
    SpecialName: System.Int32 = SpecialName
    RTSpecialName: System.Int32 = ReservedMask
    ReservedMask: System.Int32 = ReservedMask

class IReflectableType(abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    # methods
    @typing.overload
    @abc.abstractmethod
    def GetTypeInfo(self, ) -> System.Reflection.TypeInfo:
        ...

class ResourceLocation(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    Embedded: System.Int32 = Embedded
    ContainedInAnotherAssembly: System.Int32 = ContainedInAnotherAssembly
    ContainedInManifestFile: System.Int32 = ContainedInManifestFile

class LocalVariableInfo(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def LocalType(self) -> System.Type:
        ...

    @property
    def LocalIndex(self) -> System.Int32:
        ...

    @property
    def IsPinned(self) -> System.Boolean:
        ...

    # methods
    @typing.overload
    def ToString(self, ) -> System.String:
        ...

class ExceptionHandlingClause(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def Flags(self) -> System.Reflection.ExceptionHandlingClauseOptions:
        ...

    @property
    def TryOffset(self) -> System.Int32:
        ...

    @property
    def TryLength(self) -> System.Int32:
        ...

    @property
    def HandlerOffset(self) -> System.Int32:
        ...

    @property
    def HandlerLength(self) -> System.Int32:
        ...

    @property
    def FilterOffset(self) -> System.Int32:
        ...

    @property
    def CatchType(self) -> System.Type:
        ...

    # methods
    @typing.overload
    def ToString(self, ) -> System.String:
        ...

class ExceptionHandlingClauseOptions(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    Clause: System.Int32 = Clause
    Filter: System.Int32 = Filter
    Finally: System.Int32 = Finally
    Fault: System.Int32 = Fault

