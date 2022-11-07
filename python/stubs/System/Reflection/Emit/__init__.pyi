from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import System.Reflection
import System.Runtime.Serialization
import System.Reflection.Emit
import System
import System.Collections.Generic
import System.Runtime.Loader
import System.Runtime.CompilerServices
import System.Globalization
import System.IO
import System.Runtime.InteropServices
import System.Reflection.Emit.TypeBuilder

T = typing.TypeVar('T')

class AssemblyBuilder(System.Reflection.ICustomAttributeProvider, System.Runtime.Serialization.ISerializable, System.Reflection.Assembly):
    @typing.overload
    def __init__(self, **kwargs):
        self._assemblyData: System.Reflection.Emit.AssemblyBuilderData
        ...

    # static fields

    # properties
    @property
    def SyncRoot(self) -> System.Object:
        ...

    @property
    def InternalAssembly(self) -> System.Reflection.Emit.InternalAssemblyBuilder:
        ...

    @property
    def FullName(self) -> str:
        ...

    @property
    def ManifestModule(self) -> System.Reflection.Module:
        ...

    @property
    def ReflectionOnly(self) -> bool:
        ...

    @property
    def HostContext(self) -> int:
        ...

    @property
    def IsCollectible(self) -> bool:
        ...

    @property
    def CodeBase(self) -> str:
        ...

    @property
    def Location(self) -> str:
        ...

    @property
    def EntryPoint(self) -> System.Reflection.MethodInfo:
        ...

    @property
    def IsDynamic(self) -> bool:
        ...

    @property
    def DefinedTypes(self) -> System.Collections.Generic.IEnumerable[System.Reflection.TypeInfo]:
        ...

    @property
    def ExportedTypes(self) -> System.Collections.Generic.IEnumerable[System.Type]:
        ...

    @property
    def ImageRuntimeVersion(self) -> str:
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
    def Modules(self) -> System.Collections.Generic.IEnumerable[System.Reflection.Module]:
        ...

    @property
    def GlobalAssemblyCache(self) -> bool:
        ...

    @property
    def SecurityRuleSet(self) -> int:
        ...

    # methods
    def __init__(self, name: System.Reflection.AssemblyName, access: int, stackMark: ref[int], assemblyLoadContext: System.Runtime.Loader.AssemblyLoadContext, unsafeAssemblyAttributes: System.Collections.Generic.IEnumerable[System.Reflection.Emit.CustomAttributeBuilder], ):
        ...

    @staticmethod
    def GetInMemoryAssemblyModule(assembly: System.Reflection.RuntimeAssembly, ) -> System.Reflection.RuntimeModule:
        ...

    def GetModuleBuilder(self, module: System.Reflection.Emit.InternalModuleBuilder, ) -> System.Reflection.Emit.ModuleBuilder:
        ...

    def InitManifestModule(self, ) -> None:
        ...

    @staticmethod
    @typing.overload
    def DefineDynamicAssembly(name: System.Reflection.AssemblyName, access: int, ) -> System.Reflection.Emit.AssemblyBuilder:
        ...

    @staticmethod
    @typing.overload
    def DefineDynamicAssembly(name: System.Reflection.AssemblyName, access: int, assemblyAttributes: System.Collections.Generic.IEnumerable[System.Reflection.Emit.CustomAttributeBuilder], ) -> System.Reflection.Emit.AssemblyBuilder:
        ...

    @staticmethod
    def CreateDynamicAssembly(name: System.Runtime.CompilerServices.ObjectHandleOnStack, stackMark: System.Runtime.CompilerServices.StackCrawlMarkHandle, access: int, assemblyLoadContext: System.Runtime.CompilerServices.ObjectHandleOnStack, retAssembly: System.Runtime.CompilerServices.ObjectHandleOnStack, ) -> None:
        ...

    @staticmethod
    def InternalDefineDynamicAssembly(name: System.Reflection.AssemblyName, access: int, stackMark: ref[int], assemblyLoadContext: System.Runtime.Loader.AssemblyLoadContext, unsafeAssemblyAttributes: System.Collections.Generic.IEnumerable[System.Reflection.Emit.CustomAttributeBuilder], ) -> System.Reflection.Emit.AssemblyBuilder:
        ...

    def DefineDynamicModule(self, name: str, ) -> System.Reflection.Emit.ModuleBuilder:
        ...

    def DefineDynamicModuleInternalNoLock(self, name: str, ) -> System.Reflection.Emit.ModuleBuilder:
        ...

    @staticmethod
    @typing.overload
    def CheckContext(typess: System.Array[System.Array[System.Type]], ) -> None:
        ...

    @staticmethod
    @typing.overload
    def CheckContext(types: System.Array[System.Type], ) -> None:
        ...

    def Equals(self, obj: System.Object, ) -> bool:
        ...

    def GetHashCode(self, ) -> int:
        ...

    @typing.overload
    def GetCustomAttributes(self, inherit: bool, ) -> System.Array[System.Object]:
        ...

    @typing.overload
    def GetCustomAttributes(self, attributeType: System.Type, inherit: bool, ) -> System.Array[System.Object]:
        ...

    def IsDefined(self, attributeType: System.Type, inherit: bool, ) -> bool:
        ...

    def GetCustomAttributesData(self, ) -> System.Collections.Generic.IList[System.Reflection.CustomAttributeData]:
        ...

    def GetName(self, copiedName: bool, ) -> System.Reflection.AssemblyName:
        ...

    def GetType(self, name: str, throwOnError: bool, ignoreCase: bool, ) -> System.Type:
        ...

    def GetModule(self, name: str, ) -> System.Reflection.Module:
        ...

    def GetReferencedAssemblies(self, ) -> System.Array[System.Reflection.AssemblyName]:
        ...

    def GetModules(self, getResourceModules: bool, ) -> System.Array[System.Reflection.Module]:
        ...

    def GetLoadedModules(self, getResourceModules: bool, ) -> System.Array[System.Reflection.Module]:
        ...

    @typing.overload
    def GetSatelliteAssembly(self, culture: System.Globalization.CultureInfo, ) -> System.Reflection.Assembly:
        ...

    @typing.overload
    def GetSatelliteAssembly(self, culture: System.Globalization.CultureInfo, version: System.Version, ) -> System.Reflection.Assembly:
        ...

    def GetDynamicModule(self, name: str, ) -> System.Reflection.Emit.ModuleBuilder:
        ...

    def GetDynamicModuleNoLock(self, name: str, ) -> System.Reflection.Emit.ModuleBuilder:
        ...

    @typing.overload
    def SetCustomAttribute(self, con: System.Reflection.ConstructorInfo, binaryAttribute: System.Array[int], ) -> None:
        ...

    @typing.overload
    def SetCustomAttribute(self, customBuilder: System.Reflection.Emit.CustomAttributeBuilder, ) -> None:
        ...

    def GetExportedTypes(self, ) -> System.Array[System.Type]:
        ...

    def GetFile(self, name: str, ) -> System.IO.FileStream:
        ...

    def GetFiles(self, getResourceModules: bool, ) -> System.Array[System.IO.FileStream]:
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

class CustomAttributeBuilder(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        self.m_con: System.Reflection.ConstructorInfo
        ...

    # static fields

    # properties
    # methods
    @typing.overload
    def __init__(self, con: System.Reflection.ConstructorInfo, constructorArgs: System.Array[System.Object], ):
        ...

    @typing.overload
    def __init__(self, con: System.Reflection.ConstructorInfo, constructorArgs: System.Array[System.Object], namedProperties: System.Array[System.Reflection.PropertyInfo], propertyValues: System.Array[System.Object], ):
        ...

    @typing.overload
    def __init__(self, con: System.Reflection.ConstructorInfo, constructorArgs: System.Array[System.Object], namedFields: System.Array[System.Reflection.FieldInfo], fieldValues: System.Array[System.Object], ):
        ...

    @typing.overload
    def __init__(self, con: System.Reflection.ConstructorInfo, constructorArgs: System.Array[System.Object], namedProperties: System.Array[System.Reflection.PropertyInfo], propertyValues: System.Array[System.Object], namedFields: System.Array[System.Reflection.FieldInfo], fieldValues: System.Array[System.Object], ):
        ...

    def ValidateType(self, t: System.Type, ) -> bool:
        ...

    @staticmethod
    def VerifyTypeAndPassedObjectType(type: System.Type, passedType: System.Type, paramName: str, ) -> None:
        ...

    @staticmethod
    def EmitType(writer: System.IO.BinaryWriter, type: System.Type, ) -> None:
        ...

    @staticmethod
    def EmitString(writer: System.IO.BinaryWriter, str: str, ) -> None:
        ...

    @staticmethod
    def EmitValue(writer: System.IO.BinaryWriter, type: System.Type, value: System.Object, ) -> None:
        ...

    def CreateCustomAttribute(self, mod: System.Reflection.Emit.ModuleBuilder, tkOwner: int, ) -> None:
        ...

class ModuleBuilder(System.Reflection.ICustomAttributeProvider, System.Runtime.Serialization.ISerializable, System.Reflection.Module):
    @typing.overload
    def __init__(self, **kwargs):
        self._moduleData: System.Reflection.Emit.ModuleBuilderData
        self._internalModuleBuilder: System.Reflection.Emit.InternalModuleBuilder
        ...

    # static fields

    # properties
    @property
    def ContainingAssemblyBuilder(self) -> System.Reflection.Emit.AssemblyBuilder:
        ...

    @property
    def SyncRoot(self) -> System.Object:
        ...

    @property
    def InternalModule(self) -> System.Reflection.Emit.InternalModuleBuilder:
        ...

    @property
    def FullyQualifiedName(self) -> str:
        ...

    @property
    def MDStreamVersion(self) -> int:
        ...

    @property
    def ModuleVersionId(self) -> System.Guid:
        ...

    @property
    def MetadataToken(self) -> int:
        ...

    @property
    def ScopeName(self) -> str:
        ...

    @property
    def Name(self) -> str:
        ...

    @property
    def Assembly(self) -> System.Reflection.Assembly:
        ...

    @property
    def ModuleHandle(self) -> System.ModuleHandle:
        ...

    @property
    def CustomAttributes(self) -> System.Collections.Generic.IEnumerable[System.Reflection.CustomAttributeData]:
        ...

    # methods
    def __init__(self, assemblyBuilder: System.Reflection.Emit.AssemblyBuilder, internalModuleBuilder: System.Reflection.Emit.InternalModuleBuilder, ):
        ...

    @typing.overload
    def DefineGlobalMethod(self, name: str, attributes: int, returnType: System.Type, parameterTypes: System.Array[System.Type], ) -> System.Reflection.Emit.MethodBuilder:
        ...

    @typing.overload
    def DefineGlobalMethod(self, name: str, attributes: int, callingConvention: int, returnType: System.Type, parameterTypes: System.Array[System.Type], ) -> System.Reflection.Emit.MethodBuilder:
        ...

    @typing.overload
    def DefineGlobalMethod(self, name: str, attributes: int, callingConvention: int, returnType: System.Type, requiredReturnTypeCustomModifiers: System.Array[System.Type], optionalReturnTypeCustomModifiers: System.Array[System.Type], parameterTypes: System.Array[System.Type], requiredParameterTypeCustomModifiers: System.Array[System.Array[System.Type]], optionalParameterTypeCustomModifiers: System.Array[System.Array[System.Type]], ) -> System.Reflection.Emit.MethodBuilder:
        ...

    def DefineGlobalMethodNoLock(self, name: str, attributes: int, callingConvention: int, returnType: System.Type, requiredReturnTypeCustomModifiers: System.Array[System.Type], optionalReturnTypeCustomModifiers: System.Array[System.Type], parameterTypes: System.Array[System.Type], requiredParameterTypeCustomModifiers: System.Array[System.Array[System.Type]], optionalParameterTypeCustomModifiers: System.Array[System.Array[System.Type]], ) -> System.Reflection.Emit.MethodBuilder:
        ...

    def CreateGlobalFunctions(self, ) -> None:
        ...

    def CreateGlobalFunctionsNoLock(self, ) -> None:
        ...

    def DefineInitializedData(self, name: str, data: System.Array[int], attributes: int, ) -> System.Reflection.Emit.FieldBuilder:
        ...

    def DefineInitializedDataNoLock(self, name: str, data: System.Array[int], attributes: int, ) -> System.Reflection.Emit.FieldBuilder:
        ...

    def DefineUninitializedData(self, name: str, size: int, attributes: int, ) -> System.Reflection.Emit.FieldBuilder:
        ...

    def DefineUninitializedDataNoLock(self, name: str, size: int, attributes: int, ) -> System.Reflection.Emit.FieldBuilder:
        ...

    @typing.overload
    def GetTypeTokenInternal(self, type: System.Type, ) -> int:
        ...

    @typing.overload
    def GetTypeTokenInternal(self, type: System.Type, getGenericDefinition: bool, ) -> int:
        ...

    def GetTypeToken(self, type: System.Type, ) -> int:
        ...

    def GetTypeTokenWorkerNoLock(self, type: System.Type, getGenericDefinition: bool, ) -> int:
        ...

    def GetMethodToken(self, method: System.Reflection.MethodInfo, ) -> int:
        ...

    def GetMethodTokenNoLock(self, method: System.Reflection.MethodInfo, getGenericTypeDefinition: bool, ) -> int:
        ...

    def GetMethodTokenInternal(self, method: System.Reflection.MethodBase, optionalParameterTypes: System.Array[System.Type], useMethodDef: bool, ) -> int:
        ...

    @typing.overload
    def GetArrayMethodToken(self, arrayClass: System.Type, methodName: str, callingConvention: int, returnType: System.Type, parameterTypes: System.Array[System.Type], ) -> int:
        ...

    @staticmethod
    @typing.overload
    def GetArrayMethodToken(module: System.Runtime.CompilerServices.QCallModule, tkTypeSpec: int, methodName: str, signature: System.Array[int], sigLength: int, ) -> int:
        ...

    def GetArrayMethodTokenNoLock(self, arrayClass: System.Type, methodName: str, callingConvention: int, returnType: System.Type, parameterTypes: System.Array[System.Type], ) -> int:
        ...

    def GetArrayMethod(self, arrayClass: System.Type, methodName: str, callingConvention: int, returnType: System.Type, parameterTypes: System.Array[System.Type], ) -> System.Reflection.MethodInfo:
        ...

    def GetConstructorToken(self, con: System.Reflection.ConstructorInfo, ) -> int:
        ...

    def GetFieldToken(self, field: System.Reflection.FieldInfo, ) -> int:
        ...

    def GetFieldTokenNoLock(self, field: System.Reflection.FieldInfo, ) -> int:
        ...

    @typing.overload
    def GetStringConstant(self, str: str, ) -> int:
        ...

    @staticmethod
    @typing.overload
    def GetStringConstant(module: System.Runtime.CompilerServices.QCallModule, str: str, length: int, ) -> int:
        ...

    def GetSignatureToken(self, sigHelper: System.Reflection.Emit.SignatureHelper, ) -> int:
        ...

    @typing.overload
    def SetCustomAttribute(self, con: System.Reflection.ConstructorInfo, binaryAttribute: System.Array[int], ) -> None:
        ...

    @typing.overload
    def SetCustomAttribute(self, customBuilder: System.Reflection.Emit.CustomAttributeBuilder, ) -> None:
        ...

    @staticmethod
    def UnmangleTypeName(typeName: str, ) -> str:
        ...

    def AddType(self, name: str, type: System.Type, ) -> None:
        ...

    def CheckTypeNameConflict(self, strTypeName: str, enclosingType: System.Type, ) -> None:
        ...

    @staticmethod
    @typing.overload
    def GetType(strFormat: str, baseType: System.Type, ) -> System.Type:
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

    @staticmethod
    def GetTypeRef(module: System.Runtime.CompilerServices.QCallModule, strFullName: str, refedModule: System.Runtime.CompilerServices.QCallModule, strRefedModuleFileName: str, tkResolution: int, ) -> int:
        ...

    @staticmethod
    @typing.overload
    def GetMemberRef(module: System.Runtime.CompilerServices.QCallModule, refedModule: System.Runtime.CompilerServices.QCallModule, tr: int, defToken: int, ) -> int:
        ...

    @typing.overload
    def GetMemberRef(self, refedModule: System.Reflection.Module, tr: int, defToken: int, ) -> int:
        ...

    @staticmethod
    @typing.overload
    def GetMemberRefFromSignature(module: System.Runtime.CompilerServices.QCallModule, tr: int, methodName: str, signature: System.Array[int], length: int, ) -> int:
        ...

    @typing.overload
    def GetMemberRefFromSignature(self, tr: int, methodName: str, signature: System.Array[int], length: int, ) -> int:
        ...

    @staticmethod
    @typing.overload
    def GetMemberRefOfMethodInfo(module: System.Runtime.CompilerServices.QCallModule, tr: int, method: System.RuntimeMethodHandleInternal, ) -> int:
        ...

    @typing.overload
    def GetMemberRefOfMethodInfo(self, tr: int, method: System.Reflection.RuntimeMethodInfo, ) -> int:
        ...

    @typing.overload
    def GetMemberRefOfMethodInfo(self, tr: int, method: System.Reflection.RuntimeConstructorInfo, ) -> int:
        ...

    @staticmethod
    @typing.overload
    def GetMemberRefOfFieldInfo(module: System.Runtime.CompilerServices.QCallModule, tkType: int, declaringType: System.Runtime.CompilerServices.QCallTypeHandle, tkField: int, ) -> int:
        ...

    @typing.overload
    def GetMemberRefOfFieldInfo(self, tkType: int, declaringType: System.RuntimeTypeHandle, runtimeField: System.Reflection.RuntimeFieldInfo, ) -> int:
        ...

    @staticmethod
    @typing.overload
    def GetTokenFromTypeSpec(pModule: System.Runtime.CompilerServices.QCallModule, signature: System.Array[int], length: int, ) -> int:
        ...

    @typing.overload
    def GetTokenFromTypeSpec(self, signature: System.Array[int], length: int, ) -> int:
        ...

    @staticmethod
    def SetFieldRVAContent(module: System.Runtime.CompilerServices.QCallModule, fdToken: int, data: System.Array[int], length: int, ) -> None:
        ...

    def FindTypeBuilderWithName(self, strTypeName: str, ignoreCase: bool, ) -> System.Type:
        ...

    def GetTypeRefNested(self, type: System.Type, refedModule: System.Reflection.Module, strRefedModuleFileName: str, ) -> int:
        ...

    def InternalGetConstructorToken(self, con: System.Reflection.ConstructorInfo, usingRef: bool, ) -> int:
        ...

    def Init(self, strModuleName: str, ) -> None:
        ...

    def GetModuleHandleImpl(self, ) -> System.ModuleHandle:
        ...

    @staticmethod
    def GetRuntimeModuleFromModule(m: System.Reflection.Module, ) -> System.Reflection.RuntimeModule:
        ...

    def GetMemberRefToken(self, method: System.Reflection.MethodBase, optionalParameterTypes: System.Array[System.Type], ) -> int:
        ...

    @typing.overload
    def GetMemberRefSignature(self, call: int, returnType: System.Type, parameterTypes: System.Array[System.Type], requiredCustomModifiers: System.Array[System.Array[System.Type]], optionalCustomModifiers: System.Array[System.Array[System.Type]], optionalParameterTypes: System.Array[System.Type], cGenericParameters: int, ) -> System.Reflection.Emit.SignatureHelper:
        ...

    @typing.overload
    def GetMemberRefSignature(self, method: System.Reflection.MethodBase, cGenericParameters: int, ) -> System.Reflection.Emit.SignatureHelper:
        ...

    @staticmethod
    def GetGenericMethodBaseDefinition(methodBase: System.Reflection.MethodBase, ) -> System.Reflection.MethodBase:
        ...

    def Equals(self, obj: System.Object, ) -> bool:
        ...

    def GetHashCode(self, ) -> int:
        ...

    @typing.overload
    def GetCustomAttributes(self, inherit: bool, ) -> System.Array[System.Object]:
        ...

    @typing.overload
    def GetCustomAttributes(self, attributeType: System.Type, inherit: bool, ) -> System.Array[System.Object]:
        ...

    def IsDefined(self, attributeType: System.Type, inherit: bool, ) -> bool:
        ...

    def GetCustomAttributesData(self, ) -> System.Collections.Generic.IList[System.Reflection.CustomAttributeData]:
        ...

    def GetTypes(self, ) -> System.Array[System.Type]:
        ...

    def GetTypesNoLock(self, ) -> System.Array[System.Type]:
        ...

    def GetTypeNoLock(self, className: str, throwOnError: bool, ignoreCase: bool, ) -> System.Type:
        ...

    def ResolveSignature(self, metadataToken: int, ) -> System.Array[int]:
        ...

    def ResolveMethod(self, metadataToken: int, genericTypeArguments: System.Array[System.Type], genericMethodArguments: System.Array[System.Type], ) -> System.Reflection.MethodBase:
        ...

    def ResolveField(self, metadataToken: int, genericTypeArguments: System.Array[System.Type], genericMethodArguments: System.Array[System.Type], ) -> System.Reflection.FieldInfo:
        ...

    def ResolveType(self, metadataToken: int, genericTypeArguments: System.Array[System.Type], genericMethodArguments: System.Array[System.Type], ) -> System.Type:
        ...

    def ResolveMember(self, metadataToken: int, genericTypeArguments: System.Array[System.Type], genericMethodArguments: System.Array[System.Type], ) -> System.Reflection.MemberInfo:
        ...

    def ResolveString(self, metadataToken: int, ) -> str:
        ...

    def GetPEKind(self, peKind: ref[int], machine: ref[int], ) -> None:
        ...

    def IsResource(self, ) -> bool:
        ...

    def GetFields(self, bindingFlags: int, ) -> System.Array[System.Reflection.FieldInfo]:
        ...

    def GetField(self, name: str, bindingAttr: int, ) -> System.Reflection.FieldInfo:
        ...

    def GetMethods(self, bindingFlags: int, ) -> System.Array[System.Reflection.MethodInfo]:
        ...

    def GetMethodImpl(self, name: str, bindingAttr: int, binder: System.Reflection.Binder, callConvention: int, types: System.Array[System.Type], modifiers: System.Array[System.Reflection.ParameterModifier], ) -> System.Reflection.MethodInfo:
        ...

    @typing.overload
    def DefineType(self, name: str, ) -> System.Reflection.Emit.TypeBuilder:
        ...

    @typing.overload
    def DefineType(self, name: str, attr: int, ) -> System.Reflection.Emit.TypeBuilder:
        ...

    @typing.overload
    def DefineType(self, name: str, attr: int, parent: System.Type, ) -> System.Reflection.Emit.TypeBuilder:
        ...

    @typing.overload
    def DefineType(self, name: str, attr: int, parent: System.Type, typesize: int, ) -> System.Reflection.Emit.TypeBuilder:
        ...

    @typing.overload
    def DefineType(self, name: str, attr: int, parent: System.Type, packingSize: int, typesize: int, ) -> System.Reflection.Emit.TypeBuilder:
        ...

    @typing.overload
    def DefineType(self, name: str, attr: int, parent: System.Type, interfaces: System.Array[System.Type], ) -> System.Reflection.Emit.TypeBuilder:
        ...

    @typing.overload
    def DefineType(self, name: str, attr: int, parent: System.Type, packsize: int, ) -> System.Reflection.Emit.TypeBuilder:
        ...

    @typing.overload
    def DefineTypeNoLock(self, name: str, attr: int, parent: System.Type, interfaces: System.Array[System.Type], packingSize: int, typesize: int, ) -> System.Reflection.Emit.TypeBuilder:
        ...

    @typing.overload
    def DefineTypeNoLock(self, name: str, attr: int, parent: System.Type, packsize: int, ) -> System.Reflection.Emit.TypeBuilder:
        ...

    def DefineEnum(self, name: str, visibility: int, underlyingType: System.Type, ) -> System.Reflection.Emit.EnumBuilder:
        ...

    def DefineEnumNoLock(self, name: str, visibility: int, underlyingType: System.Type, ) -> System.Reflection.Emit.EnumBuilder:
        ...

    @typing.overload
    def DefinePInvokeMethod(self, name: str, dllName: str, attributes: int, callingConvention: int, returnType: System.Type, parameterTypes: System.Array[System.Type], nativeCallConv: int, nativeCharSet: int, ) -> System.Reflection.Emit.MethodBuilder:
        ...

    @typing.overload
    def DefinePInvokeMethod(self, name: str, dllName: str, entryName: str, attributes: int, callingConvention: int, returnType: System.Type, parameterTypes: System.Array[System.Type], nativeCallConv: int, nativeCharSet: int, ) -> System.Reflection.Emit.MethodBuilder:
        ...

class EnumBuilder(System.Reflection.ICustomAttributeProvider, System.Reflection.IReflect, System.Reflection.IReflectableType, System.Reflection.TypeInfo):
    @typing.overload
    def __init__(self, **kwargs):
        self.m_typeBuilder: System.Reflection.Emit.TypeBuilder
        ...

    # static fields

    # properties
    @property
    def UnderlyingField(self) -> System.Reflection.Emit.FieldBuilder:
        ...

    @property
    def Name(self) -> str:
        ...

    @property
    def GUID(self) -> System.Guid:
        ...

    @property
    def Module(self) -> System.Reflection.Module:
        ...

    @property
    def Assembly(self) -> System.Reflection.Assembly:
        ...

    @property
    def TypeHandle(self) -> System.RuntimeTypeHandle:
        ...

    @property
    def FullName(self) -> str:
        ...

    @property
    def AssemblyQualifiedName(self) -> str:
        ...

    @property
    def Namespace(self) -> str:
        ...

    @property
    def BaseType(self) -> System.Type:
        ...

    @property
    def IsByRefLike(self) -> bool:
        ...

    @property
    def IsTypeDefinition(self) -> bool:
        ...

    @property
    def IsSZArray(self) -> bool:
        ...

    @property
    def IsConstructedGenericType(self) -> bool:
        ...

    @property
    def UnderlyingSystemType(self) -> System.Type:
        ...

    @property
    def DeclaringType(self) -> System.Type:
        ...

    @property
    def ReflectedType(self) -> System.Type:
        ...

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
    def IsNested(self) -> bool:
        ...

    @property
    def DeclaringMethod(self) -> System.Reflection.MethodBase:
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
    def IsVariableBoundArray(self) -> bool:
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
    def IsSerializable(self) -> bool:
        ...

    @property
    def ContainsGenericParameters(self) -> bool:
        ...

    @property
    def IsVisible(self) -> bool:
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
    def __init__(self, name: str, underlyingType: System.Type, visibility: int, module: System.Reflection.Emit.ModuleBuilder, ):
        ...

    def IsAssignableFrom(self, typeInfo: System.Reflection.TypeInfo, ) -> bool:
        ...

    def DefineLiteral(self, literalName: str, literalValue: System.Object, ) -> System.Reflection.Emit.FieldBuilder:
        ...

    def CreateTypeInfo(self, ) -> System.Reflection.TypeInfo:
        ...

    def CreateType(self, ) -> System.Type:
        ...

    def InvokeMember(self, name: str, invokeAttr: int, binder: System.Reflection.Binder, target: System.Object, args: System.Array[System.Object], modifiers: System.Array[System.Reflection.ParameterModifier], culture: System.Globalization.CultureInfo, namedParameters: System.Array[str], ) -> System.Object:
        ...

    def GetConstructorImpl(self, bindingAttr: int, binder: System.Reflection.Binder, callConvention: int, types: System.Array[System.Type], modifiers: System.Array[System.Reflection.ParameterModifier], ) -> System.Reflection.ConstructorInfo:
        ...

    def GetConstructors(self, bindingAttr: int, ) -> System.Array[System.Reflection.ConstructorInfo]:
        ...

    def GetMethodImpl(self, name: str, bindingAttr: int, binder: System.Reflection.Binder, callConvention: int, types: System.Array[System.Type], modifiers: System.Array[System.Reflection.ParameterModifier], ) -> System.Reflection.MethodInfo:
        ...

    def GetMethods(self, bindingAttr: int, ) -> System.Array[System.Reflection.MethodInfo]:
        ...

    def GetField(self, name: str, bindingAttr: int, ) -> System.Reflection.FieldInfo:
        ...

    def GetFields(self, bindingAttr: int, ) -> System.Array[System.Reflection.FieldInfo]:
        ...

    def GetInterface(self, name: str, ignoreCase: bool, ) -> System.Type:
        ...

    def GetInterfaces(self, ) -> System.Array[System.Type]:
        ...

    def GetEvent(self, name: str, bindingAttr: int, ) -> System.Reflection.EventInfo:
        ...

    @typing.overload
    def GetEvents(self, ) -> System.Array[System.Reflection.EventInfo]:
        ...

    @typing.overload
    def GetEvents(self, bindingAttr: int, ) -> System.Array[System.Reflection.EventInfo]:
        ...

    def GetPropertyImpl(self, name: str, bindingAttr: int, binder: System.Reflection.Binder, returnType: System.Type, types: System.Array[System.Type], modifiers: System.Array[System.Reflection.ParameterModifier], ) -> System.Reflection.PropertyInfo:
        ...

    def GetProperties(self, bindingAttr: int, ) -> System.Array[System.Reflection.PropertyInfo]:
        ...

    def GetNestedTypes(self, bindingAttr: int, ) -> System.Array[System.Type]:
        ...

    def GetNestedType(self, name: str, bindingAttr: int, ) -> System.Type:
        ...

    def GetMember(self, name: str, type: int, bindingAttr: int, ) -> System.Array[System.Reflection.MemberInfo]:
        ...

    def GetMembers(self, bindingAttr: int, ) -> System.Array[System.Reflection.MemberInfo]:
        ...

    def GetInterfaceMap(self, interfaceType: System.Type, ) -> System.Reflection.InterfaceMapping:
        ...

    def GetAttributeFlagsImpl(self, ) -> int:
        ...

    def IsArrayImpl(self, ) -> bool:
        ...

    def IsPrimitiveImpl(self, ) -> bool:
        ...

    def IsValueTypeImpl(self, ) -> bool:
        ...

    def IsByRefImpl(self, ) -> bool:
        ...

    def IsPointerImpl(self, ) -> bool:
        ...

    def IsCOMObjectImpl(self, ) -> bool:
        ...

    def GetElementType(self, ) -> System.Type:
        ...

    def HasElementTypeImpl(self, ) -> bool:
        ...

    def GetEnumUnderlyingType(self, ) -> System.Type:
        ...

    @typing.overload
    def GetCustomAttributes(self, inherit: bool, ) -> System.Array[System.Object]:
        ...

    @typing.overload
    def GetCustomAttributes(self, attributeType: System.Type, inherit: bool, ) -> System.Array[System.Object]:
        ...

    @typing.overload
    def SetCustomAttribute(self, con: System.Reflection.ConstructorInfo, binaryAttribute: System.Array[int], ) -> None:
        ...

    @typing.overload
    def SetCustomAttribute(self, customBuilder: System.Reflection.Emit.CustomAttributeBuilder, ) -> None:
        ...

    def IsDefined(self, attributeType: System.Type, inherit: bool, ) -> bool:
        ...

    def MakePointerType(self, ) -> System.Type:
        ...

    def MakeByRefType(self, ) -> System.Type:
        ...

    @typing.overload
    def MakeArrayType(self, ) -> System.Type:
        ...

    @typing.overload
    def MakeArrayType(self, rank: int, ) -> System.Type:
        ...

class SignatureHelper(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def ArgumentCount(self) -> int:
        ...

    # methods
    @typing.overload
    def __init__(self, mod: System.Reflection.Module, callingConvention: int, ):
        ...

    @typing.overload
    def __init__(self, mod: System.Reflection.Module, callingConvention: int, cGenericParameters: int, returnType: System.Type, requiredCustomModifiers: System.Array[System.Type], optionalCustomModifiers: System.Array[System.Type], ):
        ...

    @typing.overload
    def __init__(self, mod: System.Reflection.Module, callingConvention: int, returnType: System.Type, requiredCustomModifiers: System.Array[System.Type], optionalCustomModifiers: System.Array[System.Type], ):
        ...

    @typing.overload
    def __init__(self, mod: System.Reflection.Module, type: System.Type, ):
        ...

    @staticmethod
    @typing.overload
    def GetMethodSigHelper(mod: System.Reflection.Module, returnType: System.Type, parameterTypes: System.Array[System.Type], ) -> System.Reflection.Emit.SignatureHelper:
        ...

    @staticmethod
    @typing.overload
    def GetMethodSigHelper(mod: System.Reflection.Module, callingConvention: int, returnType: System.Type, ) -> System.Reflection.Emit.SignatureHelper:
        ...

    @staticmethod
    @typing.overload
    def GetMethodSigHelper(scope: System.Reflection.Module, callingConvention: int, returnType: System.Type, requiredReturnTypeCustomModifiers: System.Array[System.Type], optionalReturnTypeCustomModifiers: System.Array[System.Type], parameterTypes: System.Array[System.Type], requiredParameterTypeCustomModifiers: System.Array[System.Array[System.Type]], optionalParameterTypeCustomModifiers: System.Array[System.Array[System.Type]], ) -> System.Reflection.Emit.SignatureHelper:
        ...

    @staticmethod
    @typing.overload
    def GetMethodSigHelper(scope: System.Reflection.Module, callingConvention: int, cGenericParam: int, returnType: System.Type, requiredReturnTypeCustomModifiers: System.Array[System.Type], optionalReturnTypeCustomModifiers: System.Array[System.Type], parameterTypes: System.Array[System.Type], requiredParameterTypeCustomModifiers: System.Array[System.Array[System.Type]], optionalParameterTypeCustomModifiers: System.Array[System.Array[System.Type]], ) -> System.Reflection.Emit.SignatureHelper:
        ...

    @staticmethod
    @typing.overload
    def GetMethodSigHelper(mod: System.Reflection.Module, unmanagedCallConv: int, returnType: System.Type, ) -> System.Reflection.Emit.SignatureHelper:
        ...

    @staticmethod
    @typing.overload
    def GetMethodSigHelper(callingConvention: int, returnType: System.Type, ) -> System.Reflection.Emit.SignatureHelper:
        ...

    @staticmethod
    @typing.overload
    def GetMethodSigHelper(unmanagedCallingConvention: int, returnType: System.Type, ) -> System.Reflection.Emit.SignatureHelper:
        ...

    @staticmethod
    def GetMethodSpecSigHelper(scope: System.Reflection.Module, inst: System.Array[System.Type], ) -> System.Reflection.Emit.SignatureHelper:
        ...

    @staticmethod
    @typing.overload
    def GetLocalVarSigHelper() -> System.Reflection.Emit.SignatureHelper:
        ...

    @staticmethod
    @typing.overload
    def GetLocalVarSigHelper(mod: System.Reflection.Module, ) -> System.Reflection.Emit.SignatureHelper:
        ...

    @staticmethod
    def GetFieldSigHelper(mod: System.Reflection.Module, ) -> System.Reflection.Emit.SignatureHelper:
        ...

    @staticmethod
    @typing.overload
    def GetPropertySigHelper(mod: System.Reflection.Module, returnType: System.Type, parameterTypes: System.Array[System.Type], ) -> System.Reflection.Emit.SignatureHelper:
        ...

    @staticmethod
    @typing.overload
    def GetPropertySigHelper(mod: System.Reflection.Module, returnType: System.Type, requiredReturnTypeCustomModifiers: System.Array[System.Type], optionalReturnTypeCustomModifiers: System.Array[System.Type], parameterTypes: System.Array[System.Type], requiredParameterTypeCustomModifiers: System.Array[System.Array[System.Type]], optionalParameterTypeCustomModifiers: System.Array[System.Array[System.Type]], ) -> System.Reflection.Emit.SignatureHelper:
        ...

    @staticmethod
    @typing.overload
    def GetPropertySigHelper(mod: System.Reflection.Module, callingConvention: int, returnType: System.Type, requiredReturnTypeCustomModifiers: System.Array[System.Type], optionalReturnTypeCustomModifiers: System.Array[System.Type], parameterTypes: System.Array[System.Type], requiredParameterTypeCustomModifiers: System.Array[System.Array[System.Type]], optionalParameterTypeCustomModifiers: System.Array[System.Array[System.Type]], ) -> System.Reflection.Emit.SignatureHelper:
        ...

    @staticmethod
    def GetTypeSigToken(module: System.Reflection.Module, type: System.Type, ) -> System.Reflection.Emit.SignatureHelper:
        ...

    @typing.overload
    def Init(self, mod: System.Reflection.Module, ) -> None:
        ...

    @typing.overload
    def Init(self, mod: System.Reflection.Module, callingConvention: int, ) -> None:
        ...

    @typing.overload
    def Init(self, mod: System.Reflection.Module, callingConvention: int, cGenericParam: int, ) -> None:
        ...

    @typing.overload
    def AddOneArgTypeHelper(self, argument: System.Type, pinned: bool, ) -> None:
        ...

    @typing.overload
    def AddOneArgTypeHelper(self, clsArgument: System.Type, requiredCustomModifiers: System.Array[System.Type], optionalCustomModifiers: System.Array[System.Type], ) -> None:
        ...

    @typing.overload
    def AddOneArgTypeHelper(self, clsArgument: System.Type, ) -> None:
        ...

    def AddOneArgTypeHelperWorker(self, clsArgument: System.Type, lastWasGenericInst: bool, ) -> None:
        ...

    def AddData(self, data: int, ) -> None:
        ...

    def AddElementType(self, cvt: int, ) -> None:
        ...

    def AddToken(self, token: int, ) -> None:
        ...

    def InternalAddTypeToken(self, clsToken: int, CorType: int, ) -> None:
        ...

    def InternalAddRuntimeType(self, type: System.Type, ) -> None:
        ...

    @staticmethod
    @typing.overload
    def ExpandArray(inArray: System.Array[int], ) -> System.Array[int]:
        ...

    @staticmethod
    @typing.overload
    def ExpandArray(inArray: System.Array[int], requiredLength: int, ) -> System.Array[int]:
        ...

    def IncrementArgCounts(self, ) -> None:
        ...

    def SetNumberOfSignatureElements(self, forceCopy: bool, ) -> None:
        ...

    @staticmethod
    def IsSimpleType(type: int, ) -> bool:
        ...

    def InternalGetSignature(self, length: ref[int], ) -> System.Array[int]:
        ...

    def InternalGetSignatureArray(self, ) -> System.Array[int]:
        ...

    @typing.overload
    def AddArgument(self, clsArgument: System.Type, ) -> None:
        ...

    @typing.overload
    def AddArgument(self, argument: System.Type, pinned: bool, ) -> None:
        ...

    @typing.overload
    def AddArgument(self, argument: System.Type, requiredCustomModifiers: System.Array[System.Type], optionalCustomModifiers: System.Array[System.Type], ) -> None:
        ...

    def AddArguments(self, arguments: System.Array[System.Type], requiredCustomModifiers: System.Array[System.Array[System.Type]], optionalCustomModifiers: System.Array[System.Array[System.Type]], ) -> None:
        ...

    def AddSentinel(self, ) -> None:
        ...

    def Equals(self, obj: System.Object, ) -> bool:
        ...

    def GetHashCode(self, ) -> int:
        ...

    @typing.overload
    def GetSignature(self, ) -> System.Array[int]:
        ...

    @typing.overload
    def GetSignature(self, appendEndOfSig: bool, ) -> System.Array[int]:
        ...

    def ToString(self, ) -> str:
        ...

class TypeBuilder(System.Reflection.ICustomAttributeProvider, System.Reflection.IReflect, System.Reflection.IReflectableType, System.Reflection.TypeInfo):
    @typing.overload
    def __init__(self, **kwargs):
        self.m_listMethods: System.Collections.Generic.List[System.Reflection.Emit.MethodBuilder]
        self.m_lastTokenizedMethod: int
        self.m_isHiddenGlobalType: bool
        ...

    # static fields
    UnspecifiedTypeSize: int = ...

    # properties
    @property
    def SyncRoot(self) -> System.Object:
        ...

    @property
    def BakedRuntimeType(self) -> System.RuntimeType:
        ...

    @property
    def DeclaringType(self) -> System.Type:
        ...

    @property
    def ReflectedType(self) -> System.Type:
        ...

    @property
    def Name(self) -> str:
        ...

    @property
    def Module(self) -> System.Reflection.Module:
        ...

    @property
    def IsByRefLike(self) -> bool:
        ...

    @property
    def MetadataToken(self) -> int:
        ...

    @property
    def GUID(self) -> System.Guid:
        ...

    @property
    def Assembly(self) -> System.Reflection.Assembly:
        ...

    @property
    def TypeHandle(self) -> System.RuntimeTypeHandle:
        ...

    @property
    def FullName(self) -> str:
        ...

    @property
    def Namespace(self) -> str:
        ...

    @property
    def AssemblyQualifiedName(self) -> str:
        ...

    @property
    def BaseType(self) -> System.Type:
        ...

    @property
    def IsTypeDefinition(self) -> bool:
        ...

    @property
    def IsSZArray(self) -> bool:
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
    def UnderlyingSystemType(self) -> System.Type:
        ...

    @property
    def GenericParameterAttributes(self) -> int:
        ...

    @property
    def IsGenericTypeDefinition(self) -> bool:
        ...

    @property
    def IsGenericType(self) -> bool:
        ...

    @property
    def IsGenericParameter(self) -> bool:
        ...

    @property
    def IsConstructedGenericType(self) -> bool:
        ...

    @property
    def GenericParameterPosition(self) -> int:
        ...

    @property
    def DeclaringMethod(self) -> System.Reflection.MethodBase:
        ...

    @property
    def Size(self) -> int:
        ...

    @property
    def PackingSize(self) -> int:
        ...

    @property
    def TypeToken(self) -> int:
        ...

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
    def IsNested(self) -> bool:
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
    def IsGenericTypeParameter(self) -> bool:
        ...

    @property
    def IsGenericMethodParameter(self) -> bool:
        ...

    @property
    def IsVariableBoundArray(self) -> bool:
        ...

    @property
    def HasElementType(self) -> bool:
        ...

    @property
    def GenericTypeArguments(self) -> System.Array[System.Type]:
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
    def StructLayoutAttribute(self) -> System.Runtime.InteropServices.StructLayoutAttribute:
        ...

    @property
    def TypeInitializer(self) -> System.Reflection.ConstructorInfo:
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
    def CustomAttributes(self) -> System.Collections.Generic.IEnumerable[System.Reflection.CustomAttributeData]:
        ...

    @property
    def IsCollectible(self) -> bool:
        ...

    # methods
    @typing.overload
    def __init__(self, module: System.Reflection.Emit.ModuleBuilder, ):
        ...

    @typing.overload
    def __init__(self, szName: str, genParamPos: int, declMeth: System.Reflection.Emit.MethodBuilder, ):
        ...

    @typing.overload
    def __init__(self, szName: str, genParamPos: int, declType: System.Reflection.Emit.TypeBuilder, ):
        ...

    @typing.overload
    def __init__(self, fullname: str, attr: int, parent: System.Type, interfaces: System.Array[System.Type], module: System.Reflection.Emit.ModuleBuilder, iPackingSize: int, iTypeSize: int, enclosingType: System.Reflection.Emit.TypeBuilder, ):
        ...

    def DefineEventNoLock(self, name: str, attributes: int, eventtype: System.Type, ) -> System.Reflection.Emit.EventBuilder:
        ...

    def CreateTypeInfo(self, ) -> System.Reflection.TypeInfo:
        ...

    def CreateType(self, ) -> System.Type:
        ...

    def CreateTypeNoLock(self, ) -> System.Reflection.TypeInfo:
        ...

    def SetParent(self, parent: System.Type, ) -> None:
        ...

    def AddInterfaceImplementation(self, interfaceType: System.Type, ) -> None:
        ...

    @typing.overload
    def SetCustomAttribute(self, con: System.Reflection.ConstructorInfo, binaryAttribute: System.Array[int], ) -> None:
        ...

    @typing.overload
    def SetCustomAttribute(self, customBuilder: System.Reflection.Emit.CustomAttributeBuilder, ) -> None:
        ...

    def InvokeMember(self, name: str, invokeAttr: int, binder: System.Reflection.Binder, target: System.Object, args: System.Array[System.Object], modifiers: System.Array[System.Reflection.ParameterModifier], culture: System.Globalization.CultureInfo, namedParameters: System.Array[str], ) -> System.Object:
        ...

    def GetConstructorImpl(self, bindingAttr: int, binder: System.Reflection.Binder, callConvention: int, types: System.Array[System.Type], modifiers: System.Array[System.Reflection.ParameterModifier], ) -> System.Reflection.ConstructorInfo:
        ...

    def GetConstructors(self, bindingAttr: int, ) -> System.Array[System.Reflection.ConstructorInfo]:
        ...

    def GetMethodImpl(self, name: str, bindingAttr: int, binder: System.Reflection.Binder, callConvention: int, types: System.Array[System.Type], modifiers: System.Array[System.Reflection.ParameterModifier], ) -> System.Reflection.MethodInfo:
        ...

    def GetMethods(self, bindingAttr: int, ) -> System.Array[System.Reflection.MethodInfo]:
        ...

    @typing.overload
    def GetField(self, name: str, bindingAttr: int, ) -> System.Reflection.FieldInfo:
        ...

    @staticmethod
    @typing.overload
    def GetField(type: System.Type, field: System.Reflection.FieldInfo, ) -> System.Reflection.FieldInfo:
        ...

    def GetFields(self, bindingAttr: int, ) -> System.Array[System.Reflection.FieldInfo]:
        ...

    def GetInterface(self, name: str, ignoreCase: bool, ) -> System.Type:
        ...

    def GetInterfaces(self, ) -> System.Array[System.Type]:
        ...

    def GetEvent(self, name: str, bindingAttr: int, ) -> System.Reflection.EventInfo:
        ...

    @typing.overload
    def GetEvents(self, ) -> System.Array[System.Reflection.EventInfo]:
        ...

    @typing.overload
    def GetEvents(self, bindingAttr: int, ) -> System.Array[System.Reflection.EventInfo]:
        ...

    def GetPropertyImpl(self, name: str, bindingAttr: int, binder: System.Reflection.Binder, returnType: System.Type, types: System.Array[System.Type], modifiers: System.Array[System.Reflection.ParameterModifier], ) -> System.Reflection.PropertyInfo:
        ...

    def GetProperties(self, bindingAttr: int, ) -> System.Array[System.Reflection.PropertyInfo]:
        ...

    def GetNestedTypes(self, bindingAttr: int, ) -> System.Array[System.Type]:
        ...

    def GetNestedType(self, name: str, bindingAttr: int, ) -> System.Type:
        ...

    def GetMember(self, name: str, type: int, bindingAttr: int, ) -> System.Array[System.Reflection.MemberInfo]:
        ...

    def GetInterfaceMap(self, interfaceType: System.Type, ) -> System.Reflection.InterfaceMapping:
        ...

    def GetMembers(self, bindingAttr: int, ) -> System.Array[System.Reflection.MemberInfo]:
        ...

    @typing.overload
    def IsAssignableFrom(self, c: System.Type, ) -> bool:
        ...

    @typing.overload
    def IsAssignableFrom(self, typeInfo: System.Reflection.TypeInfo, ) -> bool:
        ...

    def GetAttributeFlagsImpl(self, ) -> int:
        ...

    def IsArrayImpl(self, ) -> bool:
        ...

    def IsByRefImpl(self, ) -> bool:
        ...

    def IsPointerImpl(self, ) -> bool:
        ...

    def IsPrimitiveImpl(self, ) -> bool:
        ...

    def IsCOMObjectImpl(self, ) -> bool:
        ...

    def GetElementType(self, ) -> System.Type:
        ...

    def HasElementTypeImpl(self, ) -> bool:
        ...

    def IsSubclassOf(self, c: System.Type, ) -> bool:
        ...

    def MakePointerType(self, ) -> System.Type:
        ...

    def MakeByRefType(self, ) -> System.Type:
        ...

    @typing.overload
    def MakeArrayType(self, ) -> System.Type:
        ...

    @typing.overload
    def MakeArrayType(self, rank: int, ) -> System.Type:
        ...

    @typing.overload
    def GetCustomAttributes(self, inherit: bool, ) -> System.Array[System.Object]:
        ...

    @typing.overload
    def GetCustomAttributes(self, attributeType: System.Type, inherit: bool, ) -> System.Array[System.Object]:
        ...

    def IsDefined(self, attributeType: System.Type, inherit: bool, ) -> bool:
        ...

    def SetInterfaces(self, interfaces: System.Array[System.Type], ) -> None:
        ...

    def DefineGenericParameters(self, names: System.Array[str], ) -> System.Array[System.Reflection.Emit.GenericTypeParameterBuilder]:
        ...

    def MakeGenericType(self, typeArguments: System.Array[System.Type], ) -> System.Type:
        ...

    def GetGenericArguments(self, ) -> System.Array[System.Type]:
        ...

    def GetGenericTypeDefinition(self, ) -> System.Type:
        ...

    def DefineMethodOverride(self, methodInfoBody: System.Reflection.MethodInfo, methodInfoDeclaration: System.Reflection.MethodInfo, ) -> None:
        ...

    def DefineMethodOverrideNoLock(self, methodInfoBody: System.Reflection.MethodInfo, methodInfoDeclaration: System.Reflection.MethodInfo, ) -> None:
        ...

    @typing.overload
    def DefineMethod(self, name: str, attributes: int, returnType: System.Type, parameterTypes: System.Array[System.Type], ) -> System.Reflection.Emit.MethodBuilder:
        ...

    @typing.overload
    def DefineMethod(self, name: str, attributes: int, ) -> System.Reflection.Emit.MethodBuilder:
        ...

    @typing.overload
    def DefineMethod(self, name: str, attributes: int, callingConvention: int, ) -> System.Reflection.Emit.MethodBuilder:
        ...

    @typing.overload
    def DefineMethod(self, name: str, attributes: int, callingConvention: int, returnType: System.Type, parameterTypes: System.Array[System.Type], ) -> System.Reflection.Emit.MethodBuilder:
        ...

    @typing.overload
    def DefineMethod(self, name: str, attributes: int, callingConvention: int, returnType: System.Type, returnTypeRequiredCustomModifiers: System.Array[System.Type], returnTypeOptionalCustomModifiers: System.Array[System.Type], parameterTypes: System.Array[System.Type], parameterTypeRequiredCustomModifiers: System.Array[System.Array[System.Type]], parameterTypeOptionalCustomModifiers: System.Array[System.Array[System.Type]], ) -> System.Reflection.Emit.MethodBuilder:
        ...

    @staticmethod
    @typing.overload
    def DefineMethod(module: System.Runtime.CompilerServices.QCallModule, tkParent: int, name: str, signature: System.Array[int], sigLength: int, attributes: int, ) -> int:
        ...

    def DefineMethodNoLock(self, name: str, attributes: int, callingConvention: int, returnType: System.Type, returnTypeRequiredCustomModifiers: System.Array[System.Type], returnTypeOptionalCustomModifiers: System.Array[System.Type], parameterTypes: System.Array[System.Type], parameterTypeRequiredCustomModifiers: System.Array[System.Array[System.Type]], parameterTypeOptionalCustomModifiers: System.Array[System.Array[System.Type]], ) -> System.Reflection.Emit.MethodBuilder:
        ...

    @typing.overload
    def DefinePInvokeMethod(self, name: str, dllName: str, attributes: int, callingConvention: int, returnType: System.Type, parameterTypes: System.Array[System.Type], nativeCallConv: int, nativeCharSet: int, ) -> System.Reflection.Emit.MethodBuilder:
        ...

    @typing.overload
    def DefinePInvokeMethod(self, name: str, dllName: str, entryName: str, attributes: int, callingConvention: int, returnType: System.Type, parameterTypes: System.Array[System.Type], nativeCallConv: int, nativeCharSet: int, ) -> System.Reflection.Emit.MethodBuilder:
        ...

    @typing.overload
    def DefinePInvokeMethod(self, name: str, dllName: str, entryName: str, attributes: int, callingConvention: int, returnType: System.Type, returnTypeRequiredCustomModifiers: System.Array[System.Type], returnTypeOptionalCustomModifiers: System.Array[System.Type], parameterTypes: System.Array[System.Type], parameterTypeRequiredCustomModifiers: System.Array[System.Array[System.Type]], parameterTypeOptionalCustomModifiers: System.Array[System.Array[System.Type]], nativeCallConv: int, nativeCharSet: int, ) -> System.Reflection.Emit.MethodBuilder:
        ...

    def DefinePInvokeMethodHelper(self, name: str, dllName: str, importName: str, attributes: int, callingConvention: int, returnType: System.Type, returnTypeRequiredCustomModifiers: System.Array[System.Type], returnTypeOptionalCustomModifiers: System.Array[System.Type], parameterTypes: System.Array[System.Type], parameterTypeRequiredCustomModifiers: System.Array[System.Array[System.Type]], parameterTypeOptionalCustomModifiers: System.Array[System.Array[System.Type]], nativeCallConv: int, nativeCharSet: int, ) -> System.Reflection.Emit.MethodBuilder:
        ...

    def DefineTypeInitializer(self, ) -> System.Reflection.Emit.ConstructorBuilder:
        ...

    def DefineTypeInitializerNoLock(self, ) -> System.Reflection.Emit.ConstructorBuilder:
        ...

    def DefineDefaultConstructor(self, attributes: int, ) -> System.Reflection.Emit.ConstructorBuilder:
        ...

    def DefineDefaultConstructorNoLock(self, attributes: int, ) -> System.Reflection.Emit.ConstructorBuilder:
        ...

    @typing.overload
    def DefineConstructor(self, attributes: int, callingConvention: int, parameterTypes: System.Array[System.Type], ) -> System.Reflection.Emit.ConstructorBuilder:
        ...

    @typing.overload
    def DefineConstructor(self, attributes: int, callingConvention: int, parameterTypes: System.Array[System.Type], requiredCustomModifiers: System.Array[System.Array[System.Type]], optionalCustomModifiers: System.Array[System.Array[System.Type]], ) -> System.Reflection.Emit.ConstructorBuilder:
        ...

    def DefineConstructorNoLock(self, attributes: int, callingConvention: int, parameterTypes: System.Array[System.Type], requiredCustomModifiers: System.Array[System.Array[System.Type]], optionalCustomModifiers: System.Array[System.Array[System.Type]], ) -> System.Reflection.Emit.ConstructorBuilder:
        ...

    @typing.overload
    def DefineNestedType(self, name: str, ) -> System.Reflection.Emit.TypeBuilder:
        ...

    @typing.overload
    def DefineNestedType(self, name: str, attr: int, parent: System.Type, interfaces: System.Array[System.Type], ) -> System.Reflection.Emit.TypeBuilder:
        ...

    @typing.overload
    def DefineNestedType(self, name: str, attr: int, parent: System.Type, ) -> System.Reflection.Emit.TypeBuilder:
        ...

    @typing.overload
    def DefineNestedType(self, name: str, attr: int, ) -> System.Reflection.Emit.TypeBuilder:
        ...

    @typing.overload
    def DefineNestedType(self, name: str, attr: int, parent: System.Type, typeSize: int, ) -> System.Reflection.Emit.TypeBuilder:
        ...

    @typing.overload
    def DefineNestedType(self, name: str, attr: int, parent: System.Type, packSize: int, ) -> System.Reflection.Emit.TypeBuilder:
        ...

    @typing.overload
    def DefineNestedType(self, name: str, attr: int, parent: System.Type, packSize: int, typeSize: int, ) -> System.Reflection.Emit.TypeBuilder:
        ...

    def DefineNestedTypeNoLock(self, name: str, attr: int, parent: System.Type, interfaces: System.Array[System.Type], packSize: int, typeSize: int, ) -> System.Reflection.Emit.TypeBuilder:
        ...

    @typing.overload
    def DefineField(self, fieldName: str, type: System.Type, attributes: int, ) -> System.Reflection.Emit.FieldBuilder:
        ...

    @typing.overload
    def DefineField(self, fieldName: str, type: System.Type, requiredCustomModifiers: System.Array[System.Type], optionalCustomModifiers: System.Array[System.Type], attributes: int, ) -> System.Reflection.Emit.FieldBuilder:
        ...

    @staticmethod
    @typing.overload
    def DefineField(module: System.Runtime.CompilerServices.QCallModule, tkParent: int, name: str, signature: System.Array[int], sigLength: int, attributes: int, ) -> int:
        ...

    def DefineFieldNoLock(self, fieldName: str, type: System.Type, requiredCustomModifiers: System.Array[System.Type], optionalCustomModifiers: System.Array[System.Type], attributes: int, ) -> System.Reflection.Emit.FieldBuilder:
        ...

    def DefineInitializedData(self, name: str, data: System.Array[int], attributes: int, ) -> System.Reflection.Emit.FieldBuilder:
        ...

    def DefineInitializedDataNoLock(self, name: str, data: System.Array[int], attributes: int, ) -> System.Reflection.Emit.FieldBuilder:
        ...

    def DefineUninitializedData(self, name: str, size: int, attributes: int, ) -> System.Reflection.Emit.FieldBuilder:
        ...

    def DefineUninitializedDataNoLock(self, name: str, size: int, attributes: int, ) -> System.Reflection.Emit.FieldBuilder:
        ...

    @typing.overload
    def DefineProperty(self, name: str, attributes: int, returnType: System.Type, parameterTypes: System.Array[System.Type], ) -> System.Reflection.Emit.PropertyBuilder:
        ...

    @typing.overload
    def DefineProperty(self, name: str, attributes: int, callingConvention: int, returnType: System.Type, parameterTypes: System.Array[System.Type], ) -> System.Reflection.Emit.PropertyBuilder:
        ...

    @typing.overload
    def DefineProperty(self, name: str, attributes: int, returnType: System.Type, returnTypeRequiredCustomModifiers: System.Array[System.Type], returnTypeOptionalCustomModifiers: System.Array[System.Type], parameterTypes: System.Array[System.Type], parameterTypeRequiredCustomModifiers: System.Array[System.Array[System.Type]], parameterTypeOptionalCustomModifiers: System.Array[System.Array[System.Type]], ) -> System.Reflection.Emit.PropertyBuilder:
        ...

    @typing.overload
    def DefineProperty(self, name: str, attributes: int, callingConvention: int, returnType: System.Type, returnTypeRequiredCustomModifiers: System.Array[System.Type], returnTypeOptionalCustomModifiers: System.Array[System.Type], parameterTypes: System.Array[System.Type], parameterTypeRequiredCustomModifiers: System.Array[System.Array[System.Type]], parameterTypeOptionalCustomModifiers: System.Array[System.Array[System.Type]], ) -> System.Reflection.Emit.PropertyBuilder:
        ...

    @staticmethod
    @typing.overload
    def DefineProperty(module: System.Runtime.CompilerServices.QCallModule, tkParent: int, name: str, attributes: int, signature: System.Array[int], sigLength: int, ) -> int:
        ...

    def DefinePropertyNoLock(self, name: str, attributes: int, callingConvention: int, returnType: System.Type, returnTypeRequiredCustomModifiers: System.Array[System.Type], returnTypeOptionalCustomModifiers: System.Array[System.Type], parameterTypes: System.Array[System.Type], parameterTypeRequiredCustomModifiers: System.Array[System.Array[System.Type]], parameterTypeOptionalCustomModifiers: System.Array[System.Array[System.Type]], ) -> System.Reflection.Emit.PropertyBuilder:
        ...

    @typing.overload
    def DefineEvent(self, name: str, attributes: int, eventtype: System.Type, ) -> System.Reflection.Emit.EventBuilder:
        ...

    @staticmethod
    @typing.overload
    def DefineEvent(module: System.Runtime.CompilerServices.QCallModule, tkParent: int, name: str, attributes: int, tkEventType: int, ) -> int:
        ...

    @staticmethod
    def GetMethod(type: System.Type, method: System.Reflection.MethodInfo, ) -> System.Reflection.MethodInfo:
        ...

    @staticmethod
    def GetConstructor(type: System.Type, constructor: System.Reflection.ConstructorInfo, ) -> System.Reflection.ConstructorInfo:
        ...

    @staticmethod
    def SetParentType(module: System.Runtime.CompilerServices.QCallModule, tdTypeDef: int, tkParent: int, ) -> None:
        ...

    @staticmethod
    def AddInterfaceImpl(module: System.Runtime.CompilerServices.QCallModule, tdTypeDef: int, tkInterface: int, ) -> None:
        ...

    @staticmethod
    def DefineMethodSpec(module: System.Runtime.CompilerServices.QCallModule, tkParent: int, signature: System.Array[int], sigLength: int, ) -> int:
        ...

    @staticmethod
    def SetMethodIL(module: System.Runtime.CompilerServices.QCallModule, tk: int, isInitLocals: bool, body: System.Array[int], bodyLength: int, LocalSig: System.Array[int], sigLength: int, maxStackSize: int, exceptions: System.Array[System.Reflection.Emit.ExceptionHandler], numExceptions: int, tokenFixups: System.Array[int], numTokenFixups: int, ) -> None:
        ...

    @staticmethod
    @typing.overload
    def DefineCustomAttribute(module: System.Runtime.CompilerServices.QCallModule, tkAssociate: int, tkConstructor: int, attr: System.Array[int], attrLength: int, ) -> None:
        ...

    @staticmethod
    @typing.overload
    def DefineCustomAttribute(module: System.Reflection.Emit.ModuleBuilder, tkAssociate: int, tkConstructor: int, attr: System.Array[int], ) -> None:
        ...

    @staticmethod
    def DefineMethodSemantics(module: System.Runtime.CompilerServices.QCallModule, tkAssociation: int, semantics: int, tkMethod: int, ) -> None:
        ...

    @staticmethod
    def DefineMethodImpl(module: System.Runtime.CompilerServices.QCallModule, tkType: int, tkBody: int, tkDecl: int, ) -> None:
        ...

    @staticmethod
    def SetMethodImpl(module: System.Runtime.CompilerServices.QCallModule, tkMethod: int, MethodImplAttributes: int, ) -> None:
        ...

    @staticmethod
    def SetParamInfo(module: System.Runtime.CompilerServices.QCallModule, tkMethod: int, iSequence: int, iParamAttributes: int, strParamName: str, ) -> int:
        ...

    @staticmethod
    def GetTokenFromSig(module: System.Runtime.CompilerServices.QCallModule, signature: System.Array[int], sigLength: int, ) -> int:
        ...

    @staticmethod
    def SetFieldLayoutOffset(module: System.Runtime.CompilerServices.QCallModule, fdToken: int, iOffset: int, ) -> None:
        ...

    @staticmethod
    def SetClassLayout(module: System.Runtime.CompilerServices.QCallModule, tk: int, iPackingSize: int, iTypeSize: int, ) -> None:
        ...

    @staticmethod
    @typing.overload
    def SetConstantValue(module: System.Runtime.CompilerServices.QCallModule, tk: int, corType: int, pValue: ptr[None], ) -> None:
        ...

    @staticmethod
    @typing.overload
    def SetConstantValue(module: System.Reflection.Emit.ModuleBuilder, tk: int, destType: System.Type, value: System.Object, ) -> None:
        ...

    @staticmethod
    def SetPInvokeData(module: System.Runtime.CompilerServices.QCallModule, DllName: str, name: str, token: int, linkFlags: int, ) -> None:
        ...

    @staticmethod
    def IsTypeEqual(t1: System.Type, t2: System.Type, ) -> bool:
        ...

    def DefineDataHelper(self, name: str, data: System.Array[int], size: int, attributes: int, ) -> System.Reflection.Emit.FieldBuilder:
        ...

    def VerifyTypeAttributes(self, attr: int, ) -> None:
        ...

    def IsCreated(self, ) -> bool:
        ...

    @staticmethod
    def DefineType(module: System.Runtime.CompilerServices.QCallModule, fullname: str, tkParent: int, attributes: int, tkEnclosingType: int, interfaceTokens: System.Array[int], ) -> int:
        ...

    @staticmethod
    def DefineGenericParam(module: System.Runtime.CompilerServices.QCallModule, name: str, tkParent: int, attributes: int, position: int, constraints: System.Array[int], ) -> int:
        ...

    @staticmethod
    def TermCreateClass(module: System.Runtime.CompilerServices.QCallModule, tk: int, type: System.Runtime.CompilerServices.ObjectHandleOnStack, ) -> None:
        ...

    def ThrowIfCreated(self, ) -> None:
        ...

    def GetModuleBuilder(self, ) -> System.Reflection.Emit.ModuleBuilder:
        ...

    def SetGenParamAttributes(self, genericParameterAttributes: int, ) -> None:
        ...

    @typing.overload
    def SetGenParamCustomAttribute(self, con: System.Reflection.ConstructorInfo, binaryAttribute: System.Array[int], ) -> None:
        ...

    @typing.overload
    def SetGenParamCustomAttribute(self, customBuilder: System.Reflection.Emit.CustomAttributeBuilder, ) -> None:
        ...

    def SetGenParamCustomAttributeNoLock(self, ca: System.Reflection.Emit.TypeBuilder.CustAttr, ) -> None:
        ...

    def ToString(self, ) -> str:
        ...

class ConstructorBuilder(System.Reflection.ICustomAttributeProvider, System.Reflection.ConstructorInfo):
    @typing.overload
    def __init__(self, **kwargs):
        self.m_isDefaultConstructor: bool
        ...

    # static fields

    # properties
    @property
    def MetadataToken(self) -> int:
        ...

    @property
    def Module(self) -> System.Reflection.Module:
        ...

    @property
    def ReflectedType(self) -> System.Type:
        ...

    @property
    def DeclaringType(self) -> System.Type:
        ...

    @property
    def Name(self) -> str:
        ...

    @property
    def Attributes(self) -> int:
        ...

    @property
    def MethodHandle(self) -> System.RuntimeMethodHandle:
        ...

    @property
    def CallingConvention(self) -> int:
        ...

    @property
    def InitLocals(self) -> bool:
        ...
    @InitLocals.setter
    def InitLocals(self, val: bool):
        ...

    @property
    def MemberType(self) -> int:
        ...

    @property
    def MethodImplementationFlags(self) -> int:
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
    def IsSecurityCritical(self) -> bool:
        ...

    @property
    def IsSecuritySafeCritical(self) -> bool:
        ...

    @property
    def IsSecurityTransparent(self) -> bool:
        ...

    @property
    def CustomAttributes(self) -> System.Collections.Generic.IEnumerable[System.Reflection.CustomAttributeData]:
        ...

    @property
    def IsCollectible(self) -> bool:
        ...

    # methods
    @typing.overload
    def __init__(self, name: str, attributes: int, callingConvention: int, parameterTypes: System.Array[System.Type], requiredCustomModifiers: System.Array[System.Array[System.Type]], optionalCustomModifiers: System.Array[System.Array[System.Type]], mod: System.Reflection.Emit.ModuleBuilder, type: System.Reflection.Emit.TypeBuilder, ):
        ...

    @typing.overload
    def __init__(self, name: str, attributes: int, callingConvention: int, parameterTypes: System.Array[System.Type], mod: System.Reflection.Emit.ModuleBuilder, type: System.Reflection.Emit.TypeBuilder, ):
        ...

    def GetParameterTypes(self, ) -> System.Array[System.Type]:
        ...

    def GetTypeBuilder(self, ) -> System.Reflection.Emit.TypeBuilder:
        ...

    def GetMethodSignature(self, ) -> System.Reflection.Emit.SignatureHelper:
        ...

    def ToString(self, ) -> str:
        ...

    @typing.overload
    def Invoke(self, obj: System.Object, invokeAttr: int, binder: System.Reflection.Binder, parameters: System.Array[System.Object], culture: System.Globalization.CultureInfo, ) -> System.Object:
        ...

    @typing.overload
    def Invoke(self, invokeAttr: int, binder: System.Reflection.Binder, parameters: System.Array[System.Object], culture: System.Globalization.CultureInfo, ) -> System.Object:
        ...

    def GetParameters(self, ) -> System.Array[System.Reflection.ParameterInfo]:
        ...

    def GetMethodImplementationFlags(self, ) -> int:
        ...

    @typing.overload
    def GetCustomAttributes(self, inherit: bool, ) -> System.Array[System.Object]:
        ...

    @typing.overload
    def GetCustomAttributes(self, attributeType: System.Type, inherit: bool, ) -> System.Array[System.Object]:
        ...

    def IsDefined(self, attributeType: System.Type, inherit: bool, ) -> bool:
        ...

    def DefineParameter(self, iSequence: int, attributes: int, strParamName: str, ) -> System.Reflection.Emit.ParameterBuilder:
        ...

    @typing.overload
    def GetILGenerator(self, ) -> System.Reflection.Emit.ILGenerator:
        ...

    @typing.overload
    def GetILGenerator(self, streamSize: int, ) -> System.Reflection.Emit.ILGenerator:
        ...

    def GetReturnType(self, ) -> System.Type:
        ...

    @typing.overload
    def SetCustomAttribute(self, con: System.Reflection.ConstructorInfo, binaryAttribute: System.Array[int], ) -> None:
        ...

    @typing.overload
    def SetCustomAttribute(self, customBuilder: System.Reflection.Emit.CustomAttributeBuilder, ) -> None:
        ...

    def SetImplementationFlags(self, attributes: int, ) -> None:
        ...

class EventBuilder(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    def __init__(self, mod: System.Reflection.Emit.ModuleBuilder, name: str, attr: int, type: System.Reflection.Emit.TypeBuilder, evToken: int, ):
        ...

    def SetMethodSemantics(self, mdBuilder: System.Reflection.Emit.MethodBuilder, semantics: int, ) -> None:
        ...

    def SetAddOnMethod(self, mdBuilder: System.Reflection.Emit.MethodBuilder, ) -> None:
        ...

    def SetRemoveOnMethod(self, mdBuilder: System.Reflection.Emit.MethodBuilder, ) -> None:
        ...

    def SetRaiseMethod(self, mdBuilder: System.Reflection.Emit.MethodBuilder, ) -> None:
        ...

    def AddOtherMethod(self, mdBuilder: System.Reflection.Emit.MethodBuilder, ) -> None:
        ...

    @typing.overload
    def SetCustomAttribute(self, con: System.Reflection.ConstructorInfo, binaryAttribute: System.Array[int], ) -> None:
        ...

    @typing.overload
    def SetCustomAttribute(self, customBuilder: System.Reflection.Emit.CustomAttributeBuilder, ) -> None:
        ...

class ILGenerator(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        self.m_ScopeTree: System.Reflection.Emit.ScopeTree
        self.m_methodBuilder: System.Reflection.MethodInfo
        self.m_localCount: int
        self.m_localSignature: System.Reflection.Emit.SignatureHelper
        ...

    # static fields

    # properties
    @property
    def CurrExcStackCount(self) -> int:
        ...

    @property
    def CurrExcStack(self) -> System.Array[System.Reflection.Emit.__ExceptionInfo]:
        ...

    @property
    def ILOffset(self) -> int:
        ...

    # methods
    @typing.overload
    def __init__(self, methodBuilder: System.Reflection.MethodInfo, ):
        ...

    @typing.overload
    def __init__(self, methodBuilder: System.Reflection.MethodInfo, size: int, ):
        ...

    @staticmethod
    @typing.overload
    def EnlargeArray(incoming: System.Array[T], ) -> System.Array[T]:
        ...

    @staticmethod
    @typing.overload
    def EnlargeArray(incoming: System.Array[T], requiredSize: int, ) -> System.Array[T]:
        ...

    def RecordTokenFixup(self, ) -> None:
        ...

    def InternalEmit(self, opcode: System.Reflection.Emit.OpCode, ) -> None:
        ...

    def UpdateStackSize(self, opcode: System.Reflection.Emit.OpCode, stackchange: int, ) -> None:
        ...

    def GetMethodToken(self, method: System.Reflection.MethodBase, optionalParameterTypes: System.Array[System.Type], useMethodDef: bool, ) -> int:
        ...

    @typing.overload
    def GetMemberRefSignature(self, call: int, returnType: System.Type, parameterTypes: System.Array[System.Type], optionalParameterTypes: System.Array[System.Type], ) -> System.Reflection.Emit.SignatureHelper:
        ...

    @typing.overload
    def GetMemberRefSignature(self, call: int, returnType: System.Type, parameterTypes: System.Array[System.Type], requiredCustomModifiers: System.Array[System.Array[System.Type]], optionalCustomModifiers: System.Array[System.Array[System.Type]], optionalParameterTypes: System.Array[System.Type], ) -> System.Reflection.Emit.SignatureHelper:
        ...

    @typing.overload
    def GetMemberRefSignature(self, call: int, returnType: System.Type, parameterTypes: System.Array[System.Type], requiredCustomModifiers: System.Array[System.Array[System.Type]], optionalCustomModifiers: System.Array[System.Array[System.Type]], optionalParameterTypes: System.Array[System.Type], cGenericParameters: int, ) -> System.Reflection.Emit.SignatureHelper:
        ...

    def BakeByteArray(self, ) -> System.Array[int]:
        ...

    def GetExceptions(self, ) -> System.Array[System.Reflection.Emit.__ExceptionInfo]:
        ...

    def EnsureCapacity(self, size: int, ) -> None:
        ...

    def IncreaseCapacity(self, size: int, ) -> None:
        ...

    def PutInteger4(self, value: int, ) -> None:
        ...

    def GetLabelPos(self, lbl: System.Reflection.Emit.Label, ) -> int:
        ...

    def AddFixup(self, lbl: System.Reflection.Emit.Label, pos: int, instSize: int, ) -> None:
        ...

    def GetMaxStackSize(self, ) -> int:
        ...

    @staticmethod
    def SortExceptions(exceptions: System.Array[System.Reflection.Emit.__ExceptionInfo], ) -> None:
        ...

    def GetTokenFixups(self, ) -> System.Array[int]:
        ...

    @typing.overload
    def Emit(self, opcode: System.Reflection.Emit.OpCode, ) -> None:
        ...

    @typing.overload
    def Emit(self, opcode: System.Reflection.Emit.OpCode, arg: int, ) -> None:
        ...

    @typing.overload
    def Emit(self, opcode: System.Reflection.Emit.OpCode, arg: int, ) -> None:
        ...

    @typing.overload
    def Emit(self, opcode: System.Reflection.Emit.OpCode, arg: int, ) -> None:
        ...

    @typing.overload
    def Emit(self, opcode: System.Reflection.Emit.OpCode, arg: int, ) -> None:
        ...

    @typing.overload
    def Emit(self, opcode: System.Reflection.Emit.OpCode, meth: System.Reflection.MethodInfo, ) -> None:
        ...

    @typing.overload
    def Emit(self, opcode: System.Reflection.Emit.OpCode, signature: System.Reflection.Emit.SignatureHelper, ) -> None:
        ...

    @typing.overload
    def Emit(self, opcode: System.Reflection.Emit.OpCode, con: System.Reflection.ConstructorInfo, ) -> None:
        ...

    @typing.overload
    def Emit(self, opcode: System.Reflection.Emit.OpCode, cls: System.Type, ) -> None:
        ...

    @typing.overload
    def Emit(self, opcode: System.Reflection.Emit.OpCode, arg: int, ) -> None:
        ...

    @typing.overload
    def Emit(self, opcode: System.Reflection.Emit.OpCode, arg: float, ) -> None:
        ...

    @typing.overload
    def Emit(self, opcode: System.Reflection.Emit.OpCode, arg: float, ) -> None:
        ...

    @typing.overload
    def Emit(self, opcode: System.Reflection.Emit.OpCode, label: System.Reflection.Emit.Label, ) -> None:
        ...

    @typing.overload
    def Emit(self, opcode: System.Reflection.Emit.OpCode, labels: System.Array[System.Reflection.Emit.Label], ) -> None:
        ...

    @typing.overload
    def Emit(self, opcode: System.Reflection.Emit.OpCode, field: System.Reflection.FieldInfo, ) -> None:
        ...

    @typing.overload
    def Emit(self, opcode: System.Reflection.Emit.OpCode, str: str, ) -> None:
        ...

    @typing.overload
    def Emit(self, opcode: System.Reflection.Emit.OpCode, local: System.Reflection.Emit.LocalBuilder, ) -> None:
        ...

    @typing.overload
    def EmitCalli(self, opcode: System.Reflection.Emit.OpCode, callingConvention: int, returnType: System.Type, parameterTypes: System.Array[System.Type], optionalParameterTypes: System.Array[System.Type], ) -> None:
        ...

    @typing.overload
    def EmitCalli(self, opcode: System.Reflection.Emit.OpCode, unmanagedCallConv: int, returnType: System.Type, parameterTypes: System.Array[System.Type], ) -> None:
        ...

    def EmitCall(self, opcode: System.Reflection.Emit.OpCode, methodInfo: System.Reflection.MethodInfo, optionalParameterTypes: System.Array[System.Type], ) -> None:
        ...

    def BeginExceptionBlock(self, ) -> System.Reflection.Emit.Label:
        ...

    def EndExceptionBlock(self, ) -> None:
        ...

    def BeginExceptFilterBlock(self, ) -> None:
        ...

    def BeginCatchBlock(self, exceptionType: System.Type, ) -> None:
        ...

    def BeginFaultBlock(self, ) -> None:
        ...

    def BeginFinallyBlock(self, ) -> None:
        ...

    def DefineLabel(self, ) -> System.Reflection.Emit.Label:
        ...

    def MarkLabel(self, loc: System.Reflection.Emit.Label, ) -> None:
        ...

    def ThrowException(self, excType: System.Type, ) -> None:
        ...

    @typing.overload
    def EmitWriteLine(self, value: str, ) -> None:
        ...

    @typing.overload
    def EmitWriteLine(self, localBuilder: System.Reflection.Emit.LocalBuilder, ) -> None:
        ...

    @typing.overload
    def EmitWriteLine(self, fld: System.Reflection.FieldInfo, ) -> None:
        ...

    @typing.overload
    def DeclareLocal(self, localType: System.Type, ) -> System.Reflection.Emit.LocalBuilder:
        ...

    @typing.overload
    def DeclareLocal(self, localType: System.Type, pinned: bool, ) -> System.Reflection.Emit.LocalBuilder:
        ...

    def UsingNamespace(self, usingNamespace: str, ) -> None:
        ...

    def BeginScope(self, ) -> None:
        ...

    def EndScope(self, ) -> None:
        ...

class GenericTypeParameterBuilder(System.Reflection.ICustomAttributeProvider, System.Reflection.IReflect, System.Reflection.IReflectableType, System.Reflection.TypeInfo):
    @typing.overload
    def __init__(self, **kwargs):
        self.m_type: System.Reflection.Emit.TypeBuilder
        ...

    # static fields

    # properties
    @property
    def DeclaringType(self) -> System.Type:
        ...

    @property
    def ReflectedType(self) -> System.Type:
        ...

    @property
    def Name(self) -> str:
        ...

    @property
    def Module(self) -> System.Reflection.Module:
        ...

    @property
    def IsByRefLike(self) -> bool:
        ...

    @property
    def MetadataToken(self) -> int:
        ...

    @property
    def GUID(self) -> System.Guid:
        ...

    @property
    def Assembly(self) -> System.Reflection.Assembly:
        ...

    @property
    def TypeHandle(self) -> System.RuntimeTypeHandle:
        ...

    @property
    def FullName(self) -> str:
        ...

    @property
    def Namespace(self) -> str:
        ...

    @property
    def AssemblyQualifiedName(self) -> str:
        ...

    @property
    def BaseType(self) -> System.Type:
        ...

    @property
    def IsTypeDefinition(self) -> bool:
        ...

    @property
    def IsSZArray(self) -> bool:
        ...

    @property
    def UnderlyingSystemType(self) -> System.Type:
        ...

    @property
    def IsGenericTypeDefinition(self) -> bool:
        ...

    @property
    def IsGenericType(self) -> bool:
        ...

    @property
    def IsGenericParameter(self) -> bool:
        ...

    @property
    def IsConstructedGenericType(self) -> bool:
        ...

    @property
    def GenericParameterPosition(self) -> int:
        ...

    @property
    def ContainsGenericParameters(self) -> bool:
        ...

    @property
    def GenericParameterAttributes(self) -> int:
        ...

    @property
    def DeclaringMethod(self) -> System.Reflection.MethodBase:
        ...

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
    def IsNested(self) -> bool:
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
    def IsGenericTypeParameter(self) -> bool:
        ...

    @property
    def IsGenericMethodParameter(self) -> bool:
        ...

    @property
    def IsVariableBoundArray(self) -> bool:
        ...

    @property
    def HasElementType(self) -> bool:
        ...

    @property
    def GenericTypeArguments(self) -> System.Array[System.Type]:
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
    def IsSerializable(self) -> bool:
        ...

    @property
    def IsVisible(self) -> bool:
        ...

    @property
    def CustomAttributes(self) -> System.Collections.Generic.IEnumerable[System.Reflection.CustomAttributeData]:
        ...

    @property
    def IsCollectible(self) -> bool:
        ...

    # methods
    def __init__(self, type: System.Reflection.Emit.TypeBuilder, ):
        ...

    @typing.overload
    def IsAssignableFrom(self, typeInfo: System.Reflection.TypeInfo, ) -> bool:
        ...

    @typing.overload
    def IsAssignableFrom(self, c: System.Type, ) -> bool:
        ...

    def ToString(self, ) -> str:
        ...

    def Equals(self, o: System.Object, ) -> bool:
        ...

    def GetHashCode(self, ) -> int:
        ...

    def MakePointerType(self, ) -> System.Type:
        ...

    def MakeByRefType(self, ) -> System.Type:
        ...

    @typing.overload
    def MakeArrayType(self, ) -> System.Type:
        ...

    @typing.overload
    def MakeArrayType(self, rank: int, ) -> System.Type:
        ...

    def InvokeMember(self, name: str, invokeAttr: int, binder: System.Reflection.Binder, target: System.Object, args: System.Array[System.Object], modifiers: System.Array[System.Reflection.ParameterModifier], culture: System.Globalization.CultureInfo, namedParameters: System.Array[str], ) -> System.Object:
        ...

    def GetConstructorImpl(self, bindingAttr: int, binder: System.Reflection.Binder, callConvention: int, types: System.Array[System.Type], modifiers: System.Array[System.Reflection.ParameterModifier], ) -> System.Reflection.ConstructorInfo:
        ...

    def GetConstructors(self, bindingAttr: int, ) -> System.Array[System.Reflection.ConstructorInfo]:
        ...

    def GetMethodImpl(self, name: str, bindingAttr: int, binder: System.Reflection.Binder, callConvention: int, types: System.Array[System.Type], modifiers: System.Array[System.Reflection.ParameterModifier], ) -> System.Reflection.MethodInfo:
        ...

    def GetMethods(self, bindingAttr: int, ) -> System.Array[System.Reflection.MethodInfo]:
        ...

    def GetField(self, name: str, bindingAttr: int, ) -> System.Reflection.FieldInfo:
        ...

    def GetFields(self, bindingAttr: int, ) -> System.Array[System.Reflection.FieldInfo]:
        ...

    def GetInterface(self, name: str, ignoreCase: bool, ) -> System.Type:
        ...

    def GetInterfaces(self, ) -> System.Array[System.Type]:
        ...

    def GetEvent(self, name: str, bindingAttr: int, ) -> System.Reflection.EventInfo:
        ...

    @typing.overload
    def GetEvents(self, ) -> System.Array[System.Reflection.EventInfo]:
        ...

    @typing.overload
    def GetEvents(self, bindingAttr: int, ) -> System.Array[System.Reflection.EventInfo]:
        ...

    def GetPropertyImpl(self, name: str, bindingAttr: int, binder: System.Reflection.Binder, returnType: System.Type, types: System.Array[System.Type], modifiers: System.Array[System.Reflection.ParameterModifier], ) -> System.Reflection.PropertyInfo:
        ...

    def GetProperties(self, bindingAttr: int, ) -> System.Array[System.Reflection.PropertyInfo]:
        ...

    def GetNestedTypes(self, bindingAttr: int, ) -> System.Array[System.Type]:
        ...

    def GetNestedType(self, name: str, bindingAttr: int, ) -> System.Type:
        ...

    def GetMember(self, name: str, type: int, bindingAttr: int, ) -> System.Array[System.Reflection.MemberInfo]:
        ...

    def GetInterfaceMap(self, interfaceType: System.Type, ) -> System.Reflection.InterfaceMapping:
        ...

    def GetMembers(self, bindingAttr: int, ) -> System.Array[System.Reflection.MemberInfo]:
        ...

    def GetAttributeFlagsImpl(self, ) -> int:
        ...

    def IsArrayImpl(self, ) -> bool:
        ...

    def IsByRefImpl(self, ) -> bool:
        ...

    def IsPointerImpl(self, ) -> bool:
        ...

    def IsPrimitiveImpl(self, ) -> bool:
        ...

    def IsCOMObjectImpl(self, ) -> bool:
        ...

    def GetElementType(self, ) -> System.Type:
        ...

    def HasElementTypeImpl(self, ) -> bool:
        ...

    def GetGenericArguments(self, ) -> System.Array[System.Type]:
        ...

    def GetGenericTypeDefinition(self, ) -> System.Type:
        ...

    def MakeGenericType(self, typeArguments: System.Array[System.Type], ) -> System.Type:
        ...

    def IsValueTypeImpl(self, ) -> bool:
        ...

    def IsSubclassOf(self, c: System.Type, ) -> bool:
        ...

    @typing.overload
    def GetCustomAttributes(self, inherit: bool, ) -> System.Array[System.Object]:
        ...

    @typing.overload
    def GetCustomAttributes(self, attributeType: System.Type, inherit: bool, ) -> System.Array[System.Object]:
        ...

    def IsDefined(self, attributeType: System.Type, inherit: bool, ) -> bool:
        ...

    @typing.overload
    def SetCustomAttribute(self, con: System.Reflection.ConstructorInfo, binaryAttribute: System.Array[int], ) -> None:
        ...

    @typing.overload
    def SetCustomAttribute(self, customBuilder: System.Reflection.Emit.CustomAttributeBuilder, ) -> None:
        ...

    def SetBaseTypeConstraint(self, baseTypeConstraint: System.Type, ) -> None:
        ...

    def SetInterfaceConstraints(self, interfaceConstraints: System.Array[System.Type], ) -> None:
        ...

    def SetGenericParameterAttributes(self, genericParameterAttributes: int, ) -> None:
        ...

class OpCode(System.IEquatable[System.Reflection.Emit.OpCode], System.ValueType):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def OperandType(self) -> int:
        ...

    @property
    def FlowControl(self) -> int:
        ...

    @property
    def OpCodeType(self) -> int:
        ...

    @property
    def StackBehaviourPop(self) -> int:
        ...

    @property
    def StackBehaviourPush(self) -> int:
        ...

    @property
    def Size(self) -> int:
        ...

    @property
    def Value(self) -> int:
        ...

    @property
    def Name(self) -> str:
        ...

    # methods
    def __init__(self, value: int, flags: int, ):
        ...

    def EndsUncondJmpBlk(self, ) -> bool:
        ...

    def StackChange(self, ) -> int:
        ...

    @typing.overload
    def Equals(self, obj: System.Object, ) -> bool:
        ...

    @typing.overload
    def Equals(self, obj: System.Reflection.Emit.OpCode, ) -> bool:
        ...

    def GetHashCode(self, ) -> int:
        ...

    def ToString(self, ) -> str:
        ...

class FlowControl(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    Branch: int = ...
    Break: int = ...
    Call: int = ...
    Cond_Branch: int = ...
    Meta: int = ...
    Next: int = ...
    Phi: int = ...
    Return: int = ...
    Throw: int = ...

class OperandType(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    InlineBrTarget: int = ...
    InlineField: int = ...
    InlineI: int = ...
    InlineI8: int = ...
    InlineMethod: int = ...
    InlineNone: int = ...
    InlinePhi: int = ...
    InlineR: int = ...
    InlineSig: int = ...
    InlineString: int = ...
    InlineSwitch: int = ...
    InlineTok: int = ...
    InlineType: int = ...
    InlineVar: int = ...
    ShortInlineBrTarget: int = ...
    ShortInlineI: int = ...
    ShortInlineR: int = ...
    ShortInlineVar: int = ...

class StackBehaviour(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    Pop0: int = ...
    Pop1: int = ...
    Pop1_pop1: int = ...
    Popi: int = ...
    Popi_pop1: int = ...
    Popi_popi: int = ...
    Popi_popi8: int = ...
    Popi_popi_popi: int = ...
    Popi_popr4: int = ...
    Popi_popr8: int = ...
    Popref: int = ...
    Popref_pop1: int = ...
    Popref_popi: int = ...
    Popref_popi_popi: int = ...
    Popref_popi_popi8: int = ...
    Popref_popi_popr4: int = ...
    Popref_popi_popr8: int = ...
    Popref_popi_popref: int = ...
    Push0: int = ...
    Push1: int = ...
    Push1_push1: int = ...
    Pushi: int = ...
    Pushi8: int = ...
    Pushr4: int = ...
    Pushr8: int = ...
    Pushref: int = ...
    Varpop: int = ...
    Varpush: int = ...
    Popref_popi_pop1: int = ...

class LocalBuilder(System.Reflection.LocalVariableInfo):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def IsPinned(self) -> bool:
        ...

    @property
    def LocalType(self) -> System.Type:
        ...

    @property
    def LocalIndex(self) -> int:
        ...

    # methods
    @typing.overload
    def __init__(self, localIndex: int, localType: System.Type, methodBuilder: System.Reflection.MethodInfo, ):
        ...

    @typing.overload
    def __init__(self, localIndex: int, localType: System.Type, methodBuilder: System.Reflection.MethodInfo, isPinned: bool, ):
        ...

    def GetLocalIndex(self, ) -> int:
        ...

    def GetMethodBuilder(self, ) -> System.Reflection.MethodInfo:
        ...

class PropertyBuilder(System.Reflection.ICustomAttributeProvider, System.Reflection.PropertyInfo):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def Module(self) -> System.Reflection.Module:
        ...

    @property
    def PropertyType(self) -> System.Type:
        ...

    @property
    def Attributes(self) -> int:
        ...

    @property
    def CanRead(self) -> bool:
        ...

    @property
    def CanWrite(self) -> bool:
        ...

    @property
    def Name(self) -> str:
        ...

    @property
    def DeclaringType(self) -> System.Type:
        ...

    @property
    def ReflectedType(self) -> System.Type:
        ...

    @property
    def MemberType(self) -> int:
        ...

    @property
    def IsSpecialName(self) -> bool:
        ...

    @property
    def GetMethod(self) -> System.Reflection.MethodInfo:
        ...

    @property
    def SetMethod(self) -> System.Reflection.MethodInfo:
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
    def __init__(self, mod: System.Reflection.Emit.ModuleBuilder, name: str, sig: System.Reflection.Emit.SignatureHelper, attr: int, returnType: System.Type, prToken: int, containingType: System.Reflection.Emit.TypeBuilder, ):
        ...

    def SetConstant(self, defaultValue: System.Object, ) -> None:
        ...

    def SetMethodSemantics(self, mdBuilder: System.Reflection.Emit.MethodBuilder, semantics: int, ) -> None:
        ...

    def SetGetMethod(self, mdBuilder: System.Reflection.Emit.MethodBuilder, ) -> None:
        ...

    def SetSetMethod(self, mdBuilder: System.Reflection.Emit.MethodBuilder, ) -> None:
        ...

    def AddOtherMethod(self, mdBuilder: System.Reflection.Emit.MethodBuilder, ) -> None:
        ...

    @typing.overload
    def SetCustomAttribute(self, con: System.Reflection.ConstructorInfo, binaryAttribute: System.Array[int], ) -> None:
        ...

    @typing.overload
    def SetCustomAttribute(self, customBuilder: System.Reflection.Emit.CustomAttributeBuilder, ) -> None:
        ...

    @typing.overload
    def GetValue(self, obj: System.Object, index: System.Array[System.Object], ) -> System.Object:
        ...

    @typing.overload
    def GetValue(self, obj: System.Object, invokeAttr: int, binder: System.Reflection.Binder, index: System.Array[System.Object], culture: System.Globalization.CultureInfo, ) -> System.Object:
        ...

    @typing.overload
    def SetValue(self, obj: System.Object, value: System.Object, index: System.Array[System.Object], ) -> None:
        ...

    @typing.overload
    def SetValue(self, obj: System.Object, value: System.Object, invokeAttr: int, binder: System.Reflection.Binder, index: System.Array[System.Object], culture: System.Globalization.CultureInfo, ) -> None:
        ...

    def GetAccessors(self, nonPublic: bool, ) -> System.Array[System.Reflection.MethodInfo]:
        ...

    def GetGetMethod(self, nonPublic: bool, ) -> System.Reflection.MethodInfo:
        ...

    def GetSetMethod(self, nonPublic: bool, ) -> System.Reflection.MethodInfo:
        ...

    def GetIndexParameters(self, ) -> System.Array[System.Reflection.ParameterInfo]:
        ...

    @typing.overload
    def GetCustomAttributes(self, inherit: bool, ) -> System.Array[System.Object]:
        ...

    @typing.overload
    def GetCustomAttributes(self, attributeType: System.Type, inherit: bool, ) -> System.Array[System.Object]:
        ...

    def IsDefined(self, attributeType: System.Type, inherit: bool, ) -> bool:
        ...

class AssemblyBuilderAccess(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    Run: int = ...
    RunAndCollect: int = ...

class Label(System.IEquatable[System.Reflection.Emit.Label], System.ValueType):
    @typing.overload
    def __init__(self, **kwargs):
        self.m_label: int
        ...

    # static fields

    # properties
    # methods
    def __init__(self, label: int, ):
        ...

    def GetLabelValue(self, ) -> int:
        ...

    def GetHashCode(self, ) -> int:
        ...

    @typing.overload
    def Equals(self, obj: System.Object, ) -> bool:
        ...

    @typing.overload
    def Equals(self, obj: System.Reflection.Emit.Label, ) -> bool:
        ...

class FieldBuilder(System.Reflection.ICustomAttributeProvider, System.Reflection.FieldInfo):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def MetadataToken(self) -> int:
        ...

    @property
    def Module(self) -> System.Reflection.Module:
        ...

    @property
    def Name(self) -> str:
        ...

    @property
    def DeclaringType(self) -> System.Type:
        ...

    @property
    def ReflectedType(self) -> System.Type:
        ...

    @property
    def FieldType(self) -> System.Type:
        ...

    @property
    def FieldHandle(self) -> System.RuntimeFieldHandle:
        ...

    @property
    def Attributes(self) -> int:
        ...

    @property
    def MemberType(self) -> int:
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
    def CustomAttributes(self) -> System.Collections.Generic.IEnumerable[System.Reflection.CustomAttributeData]:
        ...

    @property
    def IsCollectible(self) -> bool:
        ...

    # methods
    def __init__(self, typeBuilder: System.Reflection.Emit.TypeBuilder, fieldName: str, type: System.Type, requiredCustomModifiers: System.Array[System.Type], optionalCustomModifiers: System.Array[System.Type], attributes: int, ):
        ...

    def SetData(self, data: System.Array[int], size: int, ) -> None:
        ...

    def GetValue(self, obj: System.Object, ) -> System.Object:
        ...

    def SetValue(self, obj: System.Object, val: System.Object, invokeAttr: int, binder: System.Reflection.Binder, culture: System.Globalization.CultureInfo, ) -> None:
        ...

    @typing.overload
    def GetCustomAttributes(self, inherit: bool, ) -> System.Array[System.Object]:
        ...

    @typing.overload
    def GetCustomAttributes(self, attributeType: System.Type, inherit: bool, ) -> System.Array[System.Object]:
        ...

    def IsDefined(self, attributeType: System.Type, inherit: bool, ) -> bool:
        ...

    def SetOffset(self, iOffset: int, ) -> None:
        ...

    def SetConstant(self, defaultValue: System.Object, ) -> None:
        ...

    @typing.overload
    def SetCustomAttribute(self, con: System.Reflection.ConstructorInfo, binaryAttribute: System.Array[int], ) -> None:
        ...

    @typing.overload
    def SetCustomAttribute(self, customBuilder: System.Reflection.Emit.CustomAttributeBuilder, ) -> None:
        ...

class OpCodeType(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    Annotation: int = ...
    Macro: int = ...
    Nternal: int = ...
    Objmodel: int = ...
    Prefix: int = ...
    Primitive: int = ...

class ParameterBuilder(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def Name(self) -> str:
        ...

    @property
    def Position(self) -> int:
        ...

    @property
    def Attributes(self) -> int:
        ...

    @property
    def IsIn(self) -> bool:
        ...

    @property
    def IsOut(self) -> bool:
        ...

    @property
    def IsOptional(self) -> bool:
        ...

    # methods
    def __init__(self, methodBuilder: System.Reflection.Emit.MethodBuilder, sequence: int, attributes: int, paramName: str, ):
        ...

    def SetConstant(self, defaultValue: System.Object, ) -> None:
        ...

    @typing.overload
    def SetCustomAttribute(self, con: System.Reflection.ConstructorInfo, binaryAttribute: System.Array[int], ) -> None:
        ...

    @typing.overload
    def SetCustomAttribute(self, customBuilder: System.Reflection.Emit.CustomAttributeBuilder, ) -> None:
        ...

class PackingSize(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    Unspecified: int = ...
    Size1: int = ...
    Size2: int = ...
    Size4: int = ...
    Size8: int = ...
    Size16: int = ...
    Size32: int = ...
    Size64: int = ...
    Size128: int = ...

class DynamicMethod(System.Reflection.ICustomAttributeProvider, System.Reflection.MethodInfo):
    @typing.overload
    def __init__(self, **kwargs):
        self.m_methodHandle: System.IRuntimeMethodInfo
        self.m_skipVisibility: bool
        self.m_typeOwner: System.RuntimeType
        self.m_resolver: System.Reflection.Emit.DynamicResolver
        self.m_restrictedSkipVisibility: bool
        ...

    # static fields

    # properties
    @property
    def Name(self) -> str:
        ...

    @property
    def DeclaringType(self) -> System.Type:
        ...

    @property
    def ReflectedType(self) -> System.Type:
        ...

    @property
    def Module(self) -> System.Reflection.Module:
        ...

    @property
    def MethodHandle(self) -> System.RuntimeMethodHandle:
        ...

    @property
    def Attributes(self) -> int:
        ...

    @property
    def CallingConvention(self) -> int:
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
    def ReturnType(self) -> System.Type:
        ...

    @property
    def ReturnParameter(self) -> System.Reflection.ParameterInfo:
        ...

    @property
    def ReturnTypeCustomAttributes(self) -> System.Reflection.ICustomAttributeProvider:
        ...

    @property
    def InitLocals(self) -> bool:
        ...
    @InitLocals.setter
    def InitLocals(self, val: bool):
        ...

    @property
    def MemberType(self) -> int:
        ...

    @property
    def GenericParameterCount(self) -> int:
        ...

    @property
    def MethodImplementationFlags(self) -> int:
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
    def CustomAttributes(self) -> System.Collections.Generic.IEnumerable[System.Reflection.CustomAttributeData]:
        ...

    @property
    def IsCollectible(self) -> bool:
        ...

    @property
    def MetadataToken(self) -> int:
        ...

    # methods
    @typing.overload
    def __init__(self, name: str, returnType: System.Type, parameterTypes: System.Array[System.Type], ):
        ...

    @typing.overload
    def __init__(self, name: str, returnType: System.Type, parameterTypes: System.Array[System.Type], restrictedSkipVisibility: bool, ):
        ...

    @typing.overload
    def __init__(self, name: str, returnType: System.Type, parameterTypes: System.Array[System.Type], m: System.Reflection.Module, ):
        ...

    @typing.overload
    def __init__(self, name: str, returnType: System.Type, parameterTypes: System.Array[System.Type], m: System.Reflection.Module, skipVisibility: bool, ):
        ...

    @typing.overload
    def __init__(self, name: str, attributes: int, callingConvention: int, returnType: System.Type, parameterTypes: System.Array[System.Type], m: System.Reflection.Module, skipVisibility: bool, ):
        ...

    @typing.overload
    def __init__(self, name: str, returnType: System.Type, parameterTypes: System.Array[System.Type], owner: System.Type, ):
        ...

    @typing.overload
    def __init__(self, name: str, returnType: System.Type, parameterTypes: System.Array[System.Type], owner: System.Type, skipVisibility: bool, ):
        ...

    @typing.overload
    def __init__(self, name: str, attributes: int, callingConvention: int, returnType: System.Type, parameterTypes: System.Array[System.Type], owner: System.Type, skipVisibility: bool, ):
        ...

    @staticmethod
    def CheckConsistency(attributes: int, callingConvention: int, ) -> None:
        ...

    @staticmethod
    def GetDynamicMethodsModule() -> System.Reflection.RuntimeModule:
        ...

    def Init(self, name: str, attributes: int, callingConvention: int, returnType: System.Type, signature: System.Array[System.Type], owner: System.Type, m: System.Reflection.Module, skipVisibility: bool, transparentMethod: bool, ) -> None:
        ...

    @typing.overload
    def CreateDelegate(self, delegateType: System.Type, ) -> System.Delegate:
        ...

    @typing.overload
    def CreateDelegate(self, delegateType: System.Type, target: System.Object, ) -> System.Delegate:
        ...

    def GetMethodDescriptor(self, ) -> System.RuntimeMethodHandle:
        ...

    def ToString(self, ) -> str:
        ...

    def GetBaseDefinition(self, ) -> System.Reflection.MethodInfo:
        ...

    def GetParameters(self, ) -> System.Array[System.Reflection.ParameterInfo]:
        ...

    def GetMethodImplementationFlags(self, ) -> int:
        ...

    def Invoke(self, obj: System.Object, invokeAttr: int, binder: System.Reflection.Binder, parameters: System.Array[System.Object], culture: System.Globalization.CultureInfo, ) -> System.Object:
        ...

    @typing.overload
    def GetCustomAttributes(self, attributeType: System.Type, inherit: bool, ) -> System.Array[System.Object]:
        ...

    @typing.overload
    def GetCustomAttributes(self, inherit: bool, ) -> System.Array[System.Object]:
        ...

    def IsDefined(self, attributeType: System.Type, inherit: bool, ) -> bool:
        ...

    def DefineParameter(self, position: int, attributes: int, parameterName: str, ) -> System.Reflection.Emit.ParameterBuilder:
        ...

    def GetDynamicILInfo(self, ) -> System.Reflection.Emit.DynamicILInfo:
        ...

    @typing.overload
    def GetILGenerator(self, ) -> System.Reflection.Emit.ILGenerator:
        ...

    @typing.overload
    def GetILGenerator(self, streamSize: int, ) -> System.Reflection.Emit.ILGenerator:
        ...

    def GetMethodInfo(self, ) -> System.Reflection.MethodInfo:
        ...

class DynamicILInfo(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def LocalSignature(self) -> System.Array[int]:
        ...

    @property
    def Exceptions(self) -> System.Array[int]:
        ...

    @property
    def Code(self) -> System.Array[int]:
        ...

    @property
    def MaxStackSize(self) -> int:
        ...

    @property
    def DynamicMethod(self) -> System.Reflection.Emit.DynamicMethod:
        ...

    @property
    def DynamicScope(self) -> System.Reflection.Emit.DynamicScope:
        ...

    # methods
    def __init__(self, method: System.Reflection.Emit.DynamicMethod, methodSignature: System.Array[int], ):
        ...

    def GetCallableMethod(self, module: System.Reflection.RuntimeModule, dm: System.Reflection.Emit.DynamicMethod, ) -> None:
        ...

    @typing.overload
    def SetCode(self, code: System.Array[int], maxStackSize: int, ) -> None:
        ...

    @typing.overload
    def SetCode(self, code: ptr[int], codeSize: int, maxStackSize: int, ) -> None:
        ...

    @typing.overload
    def SetExceptions(self, exceptions: System.Array[int], ) -> None:
        ...

    @typing.overload
    def SetExceptions(self, exceptions: ptr[int], exceptionsSize: int, ) -> None:
        ...

    @typing.overload
    def SetLocalSignature(self, localSignature: System.Array[int], ) -> None:
        ...

    @typing.overload
    def SetLocalSignature(self, localSignature: ptr[int], signatureSize: int, ) -> None:
        ...

    @typing.overload
    def GetTokenFor(self, method: System.RuntimeMethodHandle, ) -> int:
        ...

    @typing.overload
    def GetTokenFor(self, method: System.Reflection.Emit.DynamicMethod, ) -> int:
        ...

    @typing.overload
    def GetTokenFor(self, method: System.RuntimeMethodHandle, contextType: System.RuntimeTypeHandle, ) -> int:
        ...

    @typing.overload
    def GetTokenFor(self, field: System.RuntimeFieldHandle, ) -> int:
        ...

    @typing.overload
    def GetTokenFor(self, field: System.RuntimeFieldHandle, contextType: System.RuntimeTypeHandle, ) -> int:
        ...

    @typing.overload
    def GetTokenFor(self, type: System.RuntimeTypeHandle, ) -> int:
        ...

    @typing.overload
    def GetTokenFor(self, literal: str, ) -> int:
        ...

    @typing.overload
    def GetTokenFor(self, signature: System.Array[int], ) -> int:
        ...

class MethodBuilder(System.Reflection.ICustomAttributeProvider, System.Reflection.MethodInfo):
    @typing.overload
    def __init__(self, **kwargs):
        self.m_strName: str
        self.m_containingType: System.Reflection.Emit.TypeBuilder
        self.m_localSymInfo: System.Reflection.Emit.LocalSymInfo
        self.m_ilGenerator: System.Reflection.Emit.ILGenerator
        self.m_bIsBaked: bool
        self.m_parameterTypes: System.Array[System.Type]
        self.m_canBeRuntimeImpl: bool
        self.m_isDllImport: bool
        ...

    # static fields

    # properties
    @property
    def ExceptionHandlerCount(self) -> int:
        ...

    @property
    def Name(self) -> str:
        ...

    @property
    def MetadataToken(self) -> int:
        ...

    @property
    def Module(self) -> System.Reflection.Module:
        ...

    @property
    def DeclaringType(self) -> System.Type:
        ...

    @property
    def ReturnTypeCustomAttributes(self) -> System.Reflection.ICustomAttributeProvider:
        ...

    @property
    def ReflectedType(self) -> System.Type:
        ...

    @property
    def Attributes(self) -> int:
        ...

    @property
    def CallingConvention(self) -> int:
        ...

    @property
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
    def ReturnType(self) -> System.Type:
        ...

    @property
    def ReturnParameter(self) -> System.Reflection.ParameterInfo:
        ...

    @property
    def IsGenericMethodDefinition(self) -> bool:
        ...

    @property
    def ContainsGenericParameters(self) -> bool:
        ...

    @property
    def IsGenericMethod(self) -> bool:
        ...

    @property
    def InitLocals(self) -> bool:
        ...
    @InitLocals.setter
    def InitLocals(self, val: bool):
        ...

    @property
    def MemberType(self) -> int:
        ...

    @property
    def GenericParameterCount(self) -> int:
        ...

    @property
    def MethodImplementationFlags(self) -> int:
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
    def CustomAttributes(self) -> System.Collections.Generic.IEnumerable[System.Reflection.CustomAttributeData]:
        ...

    @property
    def IsCollectible(self) -> bool:
        ...

    # methods
    def __init__(self, name: str, attributes: int, callingConvention: int, returnType: System.Type, returnTypeRequiredCustomModifiers: System.Array[System.Type], returnTypeOptionalCustomModifiers: System.Array[System.Type], parameterTypes: System.Array[System.Type], parameterTypeRequiredCustomModifiers: System.Array[System.Array[System.Type]], parameterTypeOptionalCustomModifiers: System.Array[System.Array[System.Type]], mod: System.Reflection.Emit.ModuleBuilder, type: System.Reflection.Emit.TypeBuilder, ):
        ...

    def CreateMethodBodyHelper(self, il: System.Reflection.Emit.ILGenerator, ) -> None:
        ...

    def ReleaseBakedStructures(self, ) -> None:
        ...

    def GetParameterTypes(self, ) -> System.Array[System.Type]:
        ...

    @staticmethod
    def GetMethodBaseReturnType(method: System.Reflection.MethodBase, ) -> System.Type:
        ...

    def SetToken(self, token: int, ) -> None:
        ...

    def GetBody(self, ) -> System.Array[int]:
        ...

    def GetTokenFixups(self, ) -> System.Array[int]:
        ...

    def GetMethodSignature(self, ) -> System.Reflection.Emit.SignatureHelper:
        ...

    def GetLocalSignature(self, signatureLength: ref[int], ) -> System.Array[int]:
        ...

    def GetMaxStack(self, ) -> int:
        ...

    def GetExceptionHandlers(self, ) -> System.Array[System.Reflection.Emit.ExceptionHandler]:
        ...

    @staticmethod
    def CalculateNumberOfExceptions(excp: System.Array[System.Reflection.Emit.__ExceptionInfo], ) -> int:
        ...

    def IsTypeCreated(self, ) -> bool:
        ...

    def GetTypeBuilder(self, ) -> System.Reflection.Emit.TypeBuilder:
        ...

    def GetModuleBuilder(self, ) -> System.Reflection.Emit.ModuleBuilder:
        ...

    def Equals(self, obj: System.Object, ) -> bool:
        ...

    def GetHashCode(self, ) -> int:
        ...

    def ToString(self, ) -> str:
        ...

    def Invoke(self, obj: System.Object, invokeAttr: int, binder: System.Reflection.Binder, parameters: System.Array[System.Object], culture: System.Globalization.CultureInfo, ) -> System.Object:
        ...

    def GetMethodImplementationFlags(self, ) -> int:
        ...

    def GetBaseDefinition(self, ) -> System.Reflection.MethodInfo:
        ...

    def GetParameters(self, ) -> System.Array[System.Reflection.ParameterInfo]:
        ...

    @typing.overload
    def GetCustomAttributes(self, inherit: bool, ) -> System.Array[System.Object]:
        ...

    @typing.overload
    def GetCustomAttributes(self, attributeType: System.Type, inherit: bool, ) -> System.Array[System.Object]:
        ...

    def IsDefined(self, attributeType: System.Type, inherit: bool, ) -> bool:
        ...

    def GetGenericMethodDefinition(self, ) -> System.Reflection.MethodInfo:
        ...

    def GetGenericArguments(self, ) -> System.Array[System.Type]:
        ...

    def MakeGenericMethod(self, typeArguments: System.Array[System.Type], ) -> System.Reflection.MethodInfo:
        ...

    def DefineGenericParameters(self, names: System.Array[str], ) -> System.Array[System.Reflection.Emit.GenericTypeParameterBuilder]:
        ...

    def ThrowIfGeneric(self, ) -> None:
        ...

    def GetToken(self, ) -> int:
        ...

    def GetTokenNoLock(self, ) -> int:
        ...

    def SetParameters(self, parameterTypes: System.Array[System.Type], ) -> None:
        ...

    def SetReturnType(self, returnType: System.Type, ) -> None:
        ...

    def SetSignature(self, returnType: System.Type, returnTypeRequiredCustomModifiers: System.Array[System.Type], returnTypeOptionalCustomModifiers: System.Array[System.Type], parameterTypes: System.Array[System.Type], parameterTypeRequiredCustomModifiers: System.Array[System.Array[System.Type]], parameterTypeOptionalCustomModifiers: System.Array[System.Array[System.Type]], ) -> None:
        ...

    def DefineParameter(self, position: int, attributes: int, strParamName: str, ) -> System.Reflection.Emit.ParameterBuilder:
        ...

    def SetImplementationFlags(self, attributes: int, ) -> None:
        ...

    @typing.overload
    def GetILGenerator(self, ) -> System.Reflection.Emit.ILGenerator:
        ...

    @typing.overload
    def GetILGenerator(self, size: int, ) -> System.Reflection.Emit.ILGenerator:
        ...

    def ThrowIfShouldNotHaveBody(self, ) -> None:
        ...

    def GetModule(self, ) -> System.Reflection.Module:
        ...

    @typing.overload
    def SetCustomAttribute(self, con: System.Reflection.ConstructorInfo, binaryAttribute: System.Array[int], ) -> None:
        ...

    @typing.overload
    def SetCustomAttribute(self, customBuilder: System.Reflection.Emit.CustomAttributeBuilder, ) -> None:
        ...

    @staticmethod
    def IsKnownCA(con: System.Reflection.ConstructorInfo, ) -> bool:
        ...

    def ParseCA(self, con: System.Reflection.ConstructorInfo, ) -> None:
        ...

