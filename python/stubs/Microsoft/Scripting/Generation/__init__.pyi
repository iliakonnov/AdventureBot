from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import System.Reflection
import System.Runtime.Serialization
import System
import System.Collections.Generic
import System.Reflection.Emit
import Microsoft.Scripting.Generation

T = typing.TypeVar('T')

class ParameterInfoWrapper(System.Reflection.ICustomAttributeProvider, System.Runtime.Serialization.IObjectReference, System.Reflection.ParameterInfo):
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
    def ParameterType(self) -> System.Type:
        ...

    @property
    def Name(self) -> str:
        ...

    @property
    def Attributes(self) -> int:
        ...

    @property
    def Member(self) -> System.Reflection.MemberInfo:
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
    @typing.overload
    def __init__(self, parameterType: System.Type, ):
        ...

    @typing.overload
    def __init__(self, parameterType: System.Type, parameterName: str, ):
        ...

    @typing.overload
    def GetCustomAttributes(self, inherit: bool, ) -> System.Array[System.Object]:
        ...

    @typing.overload
    def GetCustomAttributes(self, attributeType: System.Type, inherit: bool, ) -> System.Array[System.Object]:
        ...

class ILGen(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    def __init__(self, ilg: System.Reflection.Emit.ILGenerator, ):
        ...

    @typing.overload
    def EmitArray(self, arrayType: System.Type, ) -> None:
        ...

    @typing.overload
    def EmitArray(self, items: System.Collections.Generic.IList[T], ) -> None:
        ...

    @typing.overload
    def EmitArray(self, elementType: System.Type, count: int, emit: Microsoft.Scripting.Generation.EmitArrayHelper, ) -> None:
        ...

    def EmitDecimal(self, value: System.Decimal, ) -> None:
        ...

    def EmitDecimalBits(self, value: System.Decimal, ) -> None:
        ...

    def EmitDefault(self, type: System.Type, ) -> None:
        ...

    def EmitMissingValue(self, type: System.Type, ) -> None:
        ...

    def GetLocal(self, type: System.Type, ) -> System.Reflection.Emit.LocalBuilder:
        ...

    def FreeLocal(self, local: System.Reflection.Emit.LocalBuilder, ) -> None:
        ...

    def BeginCatchBlock(self, exceptionType: System.Type, ) -> None:
        ...

    def BeginExceptFilterBlock(self, ) -> None:
        ...

    def BeginExceptionBlock(self, ) -> System.Reflection.Emit.Label:
        ...

    def BeginFaultBlock(self, ) -> None:
        ...

    def BeginFinallyBlock(self, ) -> None:
        ...

    def EndExceptionBlock(self, ) -> None:
        ...

    def BeginScope(self, ) -> None:
        ...

    def EndScope(self, ) -> None:
        ...

    @typing.overload
    def DeclareLocal(self, localType: System.Type, ) -> System.Reflection.Emit.LocalBuilder:
        ...

    @typing.overload
    def DeclareLocal(self, localType: System.Type, pinned: bool, ) -> System.Reflection.Emit.LocalBuilder:
        ...

    def DefineLabel(self, ) -> System.Reflection.Emit.Label:
        ...

    def MarkLabel(self, loc: System.Reflection.Emit.Label, ) -> None:
        ...

    @typing.overload
    def Emit(self, opcode: System.Reflection.Emit.OpCode, ) -> None:
        ...

    @typing.overload
    def Emit(self, opcode: System.Reflection.Emit.OpCode, arg: int, ) -> None:
        ...

    @typing.overload
    def Emit(self, opcode: System.Reflection.Emit.OpCode, con: System.Reflection.ConstructorInfo, ) -> None:
        ...

    @typing.overload
    def Emit(self, opcode: System.Reflection.Emit.OpCode, arg: float, ) -> None:
        ...

    @typing.overload
    def Emit(self, opcode: System.Reflection.Emit.OpCode, field: System.Reflection.FieldInfo, ) -> None:
        ...

    @typing.overload
    def Emit(self, opcode: System.Reflection.Emit.OpCode, arg: float, ) -> None:
        ...

    @typing.overload
    def Emit(self, opcode: System.Reflection.Emit.OpCode, arg: int, ) -> None:
        ...

    @typing.overload
    def Emit(self, opcode: System.Reflection.Emit.OpCode, label: System.Reflection.Emit.Label, ) -> None:
        ...

    @typing.overload
    def Emit(self, opcode: System.Reflection.Emit.OpCode, labels: System.Array[System.Reflection.Emit.Label], ) -> None:
        ...

    @typing.overload
    def Emit(self, opcode: System.Reflection.Emit.OpCode, local: System.Reflection.Emit.LocalBuilder, ) -> None:
        ...

    @typing.overload
    def Emit(self, opcode: System.Reflection.Emit.OpCode, arg: int, ) -> None:
        ...

    @typing.overload
    def Emit(self, opcode: System.Reflection.Emit.OpCode, meth: System.Reflection.MethodInfo, ) -> None:
        ...

    @typing.overload
    def Emit(self, opcode: System.Reflection.Emit.OpCode, arg: int, ) -> None:
        ...

    @typing.overload
    def Emit(self, opcode: System.Reflection.Emit.OpCode, arg: int, ) -> None:
        ...

    @typing.overload
    def Emit(self, opcode: System.Reflection.Emit.OpCode, signature: System.Reflection.Emit.SignatureHelper, ) -> None:
        ...

    @typing.overload
    def Emit(self, opcode: System.Reflection.Emit.OpCode, str: str, ) -> None:
        ...

    @typing.overload
    def Emit(self, opcode: System.Reflection.Emit.OpCode, cls: System.Type, ) -> None:
        ...

    @typing.overload
    def Emit(self, opcode: System.Reflection.Emit.OpCode, methodBase: System.Reflection.MethodBase, ) -> None:
        ...

    @typing.overload
    def EmitCall(self, opcode: System.Reflection.Emit.OpCode, methodInfo: System.Reflection.MethodInfo, optionalParameterTypes: System.Array[System.Type], ) -> None:
        ...

    @typing.overload
    def EmitCall(self, mi: System.Reflection.MethodInfo, ) -> None:
        ...

    @typing.overload
    def EmitCall(self, type: System.Type, name: str, ) -> None:
        ...

    @typing.overload
    def EmitCall(self, type: System.Type, name: str, paramTypes: System.Array[System.Type], ) -> None:
        ...

    @typing.overload
    def EmitCalli(self, opcode: System.Reflection.Emit.OpCode, unmanagedCallConv: int, returnType: System.Type, parameterTypes: System.Array[System.Type], ) -> None:
        ...

    @typing.overload
    def EmitCalli(self, opcode: System.Reflection.Emit.OpCode, callingConvention: int, returnType: System.Type, parameterTypes: System.Array[System.Type], optionalParameterTypes: System.Array[System.Type], ) -> None:
        ...

    def UsingNamespace(self, usingNamespace: str, ) -> None:
        ...

    def EmitDebugWriteLine(self, message: str, ) -> None:
        ...

    def EmitLoadArg(self, index: int, ) -> None:
        ...

    def EmitLoadArgAddress(self, index: int, ) -> None:
        ...

    def EmitStoreArg(self, index: int, ) -> None:
        ...

    def EmitLoadValueIndirect(self, type: System.Type, ) -> None:
        ...

    def EmitStoreValueIndirect(self, type: System.Type, ) -> None:
        ...

    def EmitLoadElement(self, type: System.Type, ) -> None:
        ...

    def EmitStoreElement(self, type: System.Type, ) -> None:
        ...

    def EmitType(self, type: System.Type, ) -> None:
        ...

    def EmitUnbox(self, type: System.Type, ) -> None:
        ...

    def EmitPropertyGet(self, pi: System.Reflection.PropertyInfo, ) -> None:
        ...

    def EmitPropertySet(self, pi: System.Reflection.PropertyInfo, ) -> None:
        ...

    def EmitFieldAddress(self, fi: System.Reflection.FieldInfo, ) -> None:
        ...

    def EmitFieldGet(self, fi: System.Reflection.FieldInfo, ) -> None:
        ...

    def EmitFieldSet(self, fi: System.Reflection.FieldInfo, ) -> None:
        ...

    @typing.overload
    def EmitNew(self, ci: System.Reflection.ConstructorInfo, ) -> None:
        ...

    @typing.overload
    def EmitNew(self, type: System.Type, paramTypes: System.Array[System.Type], ) -> None:
        ...

    def EmitNull(self, ) -> None:
        ...

    def EmitString(self, value: str, ) -> None:
        ...

    def EmitBoolean(self, value: bool, ) -> None:
        ...

    def EmitChar(self, value: str, ) -> None:
        ...

    def EmitByte(self, value: int, ) -> None:
        ...

    def EmitSByte(self, value: int, ) -> None:
        ...

    def EmitShort(self, value: int, ) -> None:
        ...

    def EmitUShort(self, value: int, ) -> None:
        ...

    def EmitInt(self, value: int, ) -> None:
        ...

    def EmitUInt(self, value: int, ) -> None:
        ...

    def EmitLong(self, value: int, ) -> None:
        ...

    def EmitULong(self, value: int, ) -> None:
        ...

    def EmitDouble(self, value: float, ) -> None:
        ...

    def EmitSingle(self, value: float, ) -> None:
        ...

    def EmitSimpleConstant(self, value: System.Object, ) -> None:
        ...

    def TryEmitConstant(self, value: System.Object, type: System.Type, ) -> bool:
        ...

    @staticmethod
    @typing.overload
    def ShouldLdtoken(t: System.Type, ) -> bool:
        ...

    @staticmethod
    @typing.overload
    def ShouldLdtoken(mb: System.Reflection.MethodBase, ) -> bool:
        ...

    def TryEmitILConstant(self, value: System.Object, type: System.Type, ) -> bool:
        ...

    def EmitImplicitCast(self, from_: System.Type, to: System.Type, ) -> None:
        ...

    def EmitExplicitCast(self, from_: System.Type, to: System.Type, ) -> None:
        ...

    def TryEmitImplicitCast(self, from_: System.Type, to: System.Type, ) -> bool:
        ...

    def TryEmitExplicitCast(self, from_: System.Type, to: System.Type, ) -> bool:
        ...

    def TryEmitCast(self, from_: System.Type, to: System.Type, implicitOnly: bool, ) -> bool:
        ...

    def EmitNumericCast(self, from_: System.Type, to: System.Type, implicitOnly: bool, ) -> bool:
        ...

    def EmitBoxing(self, type: System.Type, ) -> None:
        ...

    def EmitConvertToType(self, typeFrom: System.Type, typeTo: System.Type, isChecked: bool, ) -> None:
        ...

    def EmitCastToType(self, typeFrom: System.Type, typeTo: System.Type, ) -> None:
        ...

    def EmitNumericConversion(self, typeFrom: System.Type, typeTo: System.Type, isChecked: bool, ) -> None:
        ...

    def EmitNullableToNullableConversion(self, typeFrom: System.Type, typeTo: System.Type, isChecked: bool, ) -> None:
        ...

    def EmitNonNullableToNullableConversion(self, typeFrom: System.Type, typeTo: System.Type, isChecked: bool, ) -> None:
        ...

    def EmitNullableToNonNullableConversion(self, typeFrom: System.Type, typeTo: System.Type, isChecked: bool, ) -> None:
        ...

    def EmitNullableToNonNullableStructConversion(self, typeFrom: System.Type, typeTo: System.Type, isChecked: bool, ) -> None:
        ...

    def EmitNullableToReferenceConversion(self, typeFrom: System.Type, ) -> None:
        ...

    def EmitNullableConversion(self, typeFrom: System.Type, typeTo: System.Type, isChecked: bool, ) -> None:
        ...

    def EmitHasValue(self, nullableType: System.Type, ) -> None:
        ...

    def EmitGetValue(self, nullableType: System.Type, ) -> None:
        ...

    def EmitGetValueOrDefault(self, nullableType: System.Type, ) -> None:
        ...

class EmitArrayHelper(System.ICloneable, System.Runtime.Serialization.ISerializable, System.MulticastDelegate):
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

    def Invoke(self, index: int, ) -> None:
        ...

    def BeginInvoke(self, index: int, callback: System.AsyncCallback, object: System.Object, ) -> System.IAsyncResult:
        ...

    def EndInvoke(self, result: System.IAsyncResult, ) -> None:
        ...

