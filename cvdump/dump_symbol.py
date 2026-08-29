from cvdump.dump_tpi import get_c7_type_name, get_numeric_string
from cvdump.kaitai.cv_symbol import CvSymbol
from cvdump.kaitai.modi_stream import ModiStream
from cvdump.machine import Machine
import enum

class MachineConfig:
    def __init__(self, machine: Machine | None=None):
        self._machine = machine

    def set_machine(self, machine: Machine):
        if self._machine is not None:
            if self._machine != machine:
                raise ValueError
        self._machine = machine

    @property
    def machine(self) -> Machine:
        if self._machine is None:
            raise ValueError
        return self._machine


class LanguageId(enum.IntEnum):
    CV_CFL_C            = 0
    CV_CFL_CXX          = 1
    CV_CFL_FORTRAN      = 2
    CV_CFL_MASM         = 3
    CV_CFL_PASCAL       = 4
    CV_CFL_BASIC        = 5
    CV_CFL_COBOL        = 6
    CV_CFL_LINK         = 7
    CV_CFL_CVTRES       = 8
    CV_CFL_CVTPGD       = 9
    CV_CFL_CSHARP       = 10
    CV_CFL_VB           = 11
    CV_CFL_ILASM        = 12
    CV_CFL_JAVA         = 13
    CV_CFL_JSCRIPT      = 14
    CV_CFL_MSIL         = 15
    CV_CFL_HLSL         = 16


class CpuType(enum.IntEnum):
    CV_CFL_8080             = 0x00
    CV_CFL_8086             = 0x01
    CV_CFL_80286            = 0x02
    CV_CFL_80386            = 0x03
    CV_CFL_80486            = 0x04
    CV_CFL_PENTIUM          = 0x05
    CV_CFL_PENTIUMII        = 0x06
    CV_CFL_PENTIUMPRO       = CV_CFL_PENTIUMII
    CV_CFL_PENTIUMIII       = 0x07
    CV_CFL_MIPS             = 0x10
    CV_CFL_MIPSR4000        = CV_CFL_MIPS  # don't break current cod
    CV_CFL_MIPS16           = 0x11
    CV_CFL_MIPS32           = 0x12
    CV_CFL_MIPS64           = 0x13
    CV_CFL_MIPSI            = 0x14
    CV_CFL_MIPSII           = 0x15
    CV_CFL_MIPSIII          = 0x16
    CV_CFL_MIPSIV           = 0x17
    CV_CFL_MIPSV            = 0x18
    CV_CFL_M68000           = 0x20
    CV_CFL_M68010           = 0x21
    CV_CFL_M68020           = 0x22
    CV_CFL_M68030           = 0x23
    CV_CFL_M68040           = 0x24
    CV_CFL_ALPHA            = 0x30
    CV_CFL_ALPHA_21064      = 0x30
    CV_CFL_ALPHA_21164      = 0x31
    CV_CFL_ALPHA_21164A     = 0x32
    CV_CFL_ALPHA_21264      = 0x33
    CV_CFL_ALPHA_21364      = 0x34
    CV_CFL_PPC601           = 0x40
    CV_CFL_PPC603           = 0x41
    CV_CFL_PPC604           = 0x42
    CV_CFL_PPC620           = 0x43
    CV_CFL_PPCFP            = 0x44
    CV_CFL_PPCBE            = 0x45
    CV_CFL_SH3              = 0x50
    CV_CFL_SH3E             = 0x51
    CV_CFL_SH3DSP           = 0x52
    CV_CFL_SH4              = 0x53
    CV_CFL_SHMEDIA          = 0x54
    CV_CFL_ARM3             = 0x60
    CV_CFL_ARM4             = 0x61
    CV_CFL_ARM4T            = 0x62
    CV_CFL_ARM5             = 0x63
    CV_CFL_ARM5T            = 0x64
    CV_CFL_ARM6             = 0x65
    CV_CFL_ARM_XMAC         = 0x66
    CV_CFL_ARM_WMMX         = 0x67
    CV_CFL_ARM7             = 0x68
    CV_CFL_OMNI             = 0x70
    CV_CFL_IA64             = 0x80
    CV_CFL_IA64_1           = 0x80
    CV_CFL_IA64_2           = 0x81
    CV_CFL_CEE              = 0x90
    CV_CFL_AM33             = 0xA0
    CV_CFL_M32R             = 0xB0
    CV_CFL_TRICORE          = 0xC0
    CV_CFL_X64              = 0xD0
    CV_CFL_AMD64            = CV_CFL_X64
    CV_CFL_EBC              = 0xE0
    CV_CFL_THUMB            = 0xF0
    CV_CFL_ARMNT            = 0xF4
    CV_CFL_ARM64            = 0xF6
    CV_CFL_HYBRID_X86_ARM64 = 0xF7
    CV_CFL_ARM64EC          = 0xF8
    CV_CFL_ARM64X           = 0xF9
    CV_CFL_D3D11_SHADER     = 0x100


LANGUAGE_TO_STRING: dict[LanguageId, str] = {
    LanguageId.CV_CFL_C: "C",
    LanguageId.CV_CFL_CXX: "C++",
    LanguageId.CV_CFL_FORTRAN: "FORTRAN",
    LanguageId.CV_CFL_MASM: "MASM",
    LanguageId.CV_CFL_PASCAL: "Pascal",
    LanguageId.CV_CFL_BASIC: "Basic",
    LanguageId.CV_CFL_COBOL: "COBOL",
    LanguageId.CV_CFL_LINK: "LINK",
    LanguageId.CV_CFL_CVTRES: "CVTRES",
    LanguageId.CV_CFL_CVTPGD: "CVTPGD",
    LanguageId.CV_CFL_CSHARP: "C#",
    LanguageId.CV_CFL_VB: "Visual Basic",
    LanguageId.CV_CFL_ILASM: "ILASM",
    LanguageId.CV_CFL_JAVA: "Java",
    LanguageId.CV_CFL_JSCRIPT: "JScript",
    LanguageId.CV_CFL_MSIL: "MSIL",
    LanguageId.CV_CFL_HLSL: "HLSL",
}

PROCESSOR_TO_STRING: dict[CpuType, str] = {
    CpuType.CV_CFL_8080: "8080",
    CpuType.CV_CFL_8086: "8086",
    CpuType.CV_CFL_80286: "80286",
    CpuType.CV_CFL_80386: "80386",
    CpuType.CV_CFL_80486: "80486",
    CpuType.CV_CFL_PENTIUM: "Pentium",
    CpuType.CV_CFL_PENTIUMII: "Pentium Pro/Pentium II",
    CpuType.CV_CFL_PENTIUMIII: "Pentium III",
    CpuType.CV_CFL_MIPSR4000: "MIPS (Generic)",
    CpuType.CV_CFL_MIPS16: "MIPS16",
    CpuType.CV_CFL_MIPS32: "MIPS32",
    CpuType.CV_CFL_MIPS64: "MIPS64",
    CpuType.CV_CFL_MIPSI: "MIPS I",
    CpuType.CV_CFL_MIPSII: "MIPS II",
    CpuType.CV_CFL_MIPSIII: "MIPS III",
    CpuType.CV_CFL_MIPSIV: "MIPS IV",
    CpuType.CV_CFL_MIPSV: "MIPS V",
    CpuType.CV_CFL_M68000: "M68000",
    CpuType.CV_CFL_M68010: "M68010",
    CpuType.CV_CFL_M68020: "M68020",
    CpuType.CV_CFL_M68030: "M68030",
    CpuType.CV_CFL_M68040: "M68040",
    CpuType.CV_CFL_ALPHA_21064: "Alpha 21064",
    CpuType.CV_CFL_ALPHA_21164: "Alpha 21164",
    CpuType.CV_CFL_ALPHA_21164A: "Alpha 21164A",
    CpuType.CV_CFL_ALPHA_21264: "Alpha 21264",
    CpuType.CV_CFL_ALPHA_21364: "Alpha 21364",
    CpuType.CV_CFL_PPC601: "PPC 601",
    CpuType.CV_CFL_PPC603: "PPC 603",
    CpuType.CV_CFL_PPC604: "PPC 604",
    CpuType.CV_CFL_PPC620: "PPC 620",
    CpuType.CV_CFL_PPCFP: "PPC w/FP",
    CpuType.CV_CFL_PPCBE: "PPC (Big Endian)",
    CpuType.CV_CFL_SH3: "SH3",
    CpuType.CV_CFL_SH3E: "SH3E",
    CpuType.CV_CFL_SH3DSP: "SH3DSP",
    CpuType.CV_CFL_SH4: "SH4",
    CpuType.CV_CFL_SHMEDIA: "SHmedia",
    CpuType.CV_CFL_ARM3: "ARMv3 (CE)",
    CpuType.CV_CFL_ARM4: "ARMv4 (CE)",
    CpuType.CV_CFL_ARM4T: "ARMv4T (CE)",
    CpuType.CV_CFL_ARM5: "ARMv5 (CE)",
    CpuType.CV_CFL_ARM5T: "ARMv5T (CE)",
    CpuType.CV_CFL_ARM6: "ARMv6 (CE)",
    CpuType.CV_CFL_ARM_XMAC: "ARM (XMAC) (CE)",
    CpuType.CV_CFL_ARM_WMMX: "ARM (WMMX) (CE)",
    CpuType.CV_CFL_ARM7: "ARMv7 (CE)",
    CpuType.CV_CFL_OMNI: "Omni",
    CpuType.CV_CFL_IA64_1: "Itanium",
    CpuType.CV_CFL_IA64_2: "Itanium (McKinley)",
    CpuType.CV_CFL_CEE: "CEE",
    CpuType.CV_CFL_AM33: "AM33",
    CpuType.CV_CFL_M32R: "M32R",
    CpuType.CV_CFL_TRICORE: "TriCore",
    CpuType.CV_CFL_X64: "x64",
    CpuType.CV_CFL_EBC: "EBC",
    CpuType.CV_CFL_THUMB: "Thumb (CE)",
    CpuType.CV_CFL_ARMNT: "ARM",
    CpuType.CV_CFL_ARM64: "ARM64",
    CpuType.CV_CFL_D3D11_SHADER: "D3D11_SHADER",
}


def GetLanguageIdString(language_id: int) -> str:
    try:
        lang_enum = LanguageId(language_id)
        s = LANGUAGE_TO_STRING[lang_enum]
    except (KeyError, ValueError):
        s = f"??? (0x{language_id:x})"
    return s


def GetTargetProcessorString(processor_id: int) -> str:
    s = PROCESSOR_TO_STRING.get(CpuType(processor_id))
    if s is None:
        s = f"??? (0x{processor_id:x})"
    return s


def GetFloatingPointPackageName(fp_package_id: int) -> str:
    return (
        "hardware",                       # CV_CFL_NDP
        "emulator",                       # CV_CFL_EMU
        "altmath",                        # CV_CFL_ALT
        "???",
    )[fp_package_id]


def ProcessorToMachine(processor_id: int) -> Machine:
    cpu = CpuType(processor_id)
    match cpu:
        case CpuType.CV_CFL_8080 | CpuType.CV_CFL_8086 | CpuType.CV_CFL_80286 | CpuType.CV_CFL_80386 | CpuType.CV_CFL_80486 | CpuType.CV_CFL_PENTIUM | CpuType.CV_CFL_PENTIUMII | CpuType.CV_CFL_PENTIUMPRO | CpuType.CV_CFL_PENTIUMIII:
            return Machine.IMAGE_FILE_MACHINE_I386
        case CpuType.CV_CFL_X64:
            return Machine.IMAGE_FILE_MACHINE_AMD64
        case CpuType.CV_CFL_ARM64 | CpuType.CV_CFL_ARM64X | CpuType.CV_CFL_ARM64EC:
            return Machine.IMAGE_FILE_MACHINE_ARM64
        case _:
            raise ValueError


def GetAmbientDataType(fp_package_id: int) -> str:
    return (
        "NEAR",                           # CV_CFL_xNEAR
        "FAR",                            # CV_CFL_xFAR
        "HUGE",                           # CV_CFL_xHUGE
        "???",
    )[fp_package_id]

def print_proc_flags(flags: int):
    if not flags:
        return
    print(f"\tFlags: ", end="")
    props = []
    if flags & 0x1:
        props.append("Frame Ptr Present")
    if flags & 0x2:
        props.append("Interrupt")
    if flags & 0x4:
        props.append("FAR")
    if flags & 0x8:
        props.append("Never Return")
    if flags & 0x10:
        props.append("Not Reached")
    if flags & 0x20:
        props.append("Custom Calling Convention")
    if flags & 0x40:
        props.append("Do Not Inline")
    if flags & 0x80:
        props.append("Optimized Debug Info")
    print(", ".join(props))

def print_local_var_flags(flags: int, type_index: int):
    if flags & 0x1:
        print(f"Param: {type_index:08X}, ", end="")
    else:
        print(f"Local: {type_index:08X}, ", end="")

    props = []
    if flags & 0x2:
        props.append("Address Taken")
    if flags & 0x4:
        props.append("Compiler Generated")
    if flags & 0x8:
        props.append("aggregate")
    if flags & 0x10:
        props.append("aggregate")
    if flags & 0x20:
        props.append("alias")
    if flags & 0x40:
        props.append("aliased")
    if flags & 0x80:
        props.append("return value")
    if flags & 0x100:
        props.append("optimized away")
    if (flags & 0x200) and not (flags & 0x400):
        props.append("global")
    elif (flags & 0x200) and (flags & 0x400):
        props.append("file static")
    elif not (flags & 0x200) and (flags & 0x400):
        props.append("static local")
    print(", ".join(props), end="")

MACHINE_TO_CPU: dict[Machine, CpuType] = {
    Machine.IMAGE_FILE_MACHINE_AM33: CpuType.CV_CFL_AM33,
    Machine.IMAGE_FILE_MACHINE_AMD64: CpuType.CV_CFL_X64,
    Machine.IMAGE_FILE_MACHINE_ARM: CpuType.CV_CFL_ARM3,
    Machine.IMAGE_FILE_MACHINE_ARM64: CpuType.CV_CFL_ARM64,
    Machine.IMAGE_FILE_MACHINE_ARMNT: CpuType.CV_CFL_ARMNT,
    Machine.IMAGE_FILE_MACHINE_CEE: CpuType.CV_CFL_CEE,
    Machine.IMAGE_FILE_MACHINE_EBC: CpuType.CV_CFL_EBC,
    Machine.IMAGE_FILE_MACHINE_I386: CpuType.CV_CFL_80386,
    Machine.IMAGE_FILE_MACHINE_IA64: CpuType.CV_CFL_IA64_1,
    Machine.IMAGE_FILE_MACHINE_M32R: CpuType.CV_CFL_M32R,
    Machine.IMAGE_FILE_MACHINE_MIPS16 : CpuType.CV_CFL_MIPS,
    Machine.IMAGE_FILE_MACHINE_MIPSFPU: CpuType.CV_CFL_MIPS,
    Machine.IMAGE_FILE_MACHINE_MIPSFPU16: CpuType.CV_CFL_MIPS,
    Machine.IMAGE_FILE_MACHINE_R3000: CpuType.CV_CFL_MIPS,
    Machine.IMAGE_FILE_MACHINE_R4000: CpuType.CV_CFL_MIPS,
    Machine.IMAGE_FILE_MACHINE_R10000: CpuType.CV_CFL_MIPS,
    Machine.IMAGE_FILE_MACHINE_POWERPC: CpuType.CV_CFL_PPC601,
    Machine.IMAGE_FILE_MACHINE_POWERPCFP: CpuType.CV_CFL_PPCFP,
    Machine.IMAGE_FILE_MACHINE_SH3: CpuType.CV_CFL_SH3,
    Machine.IMAGE_FILE_MACHINE_SH3DSP: CpuType.CV_CFL_SH3DSP,
    Machine.IMAGE_FILE_MACHINE_SH4: CpuType.CV_CFL_SH4,
    Machine.IMAGE_FILE_MACHINE_SH5: CpuType.CV_CFL_SH4,
    Machine.IMAGE_FILE_MACHINE_THUMB: CpuType.CV_CFL_THUMB,
}

class RegisterX86(enum.Enum):
    CV_REG_NONE = 0
    CV_REG_AL = 1
    CV_REG_CL = 2
    CV_REG_DL = 3
    CV_REG_BL = 4
    CV_REG_AH = 5
    CV_REG_CH = 6
    CV_REG_DH = 7
    CV_REG_BH = 8
    CV_REG_AX = 9
    CV_REG_CX = 10
    CV_REG_DX = 11
    CV_REG_BX = 12
    CV_REG_SP = 13
    CV_REG_BP = 14
    CV_REG_SI = 15
    CV_REG_DI = 16
    CV_REG_EAX = 17
    CV_REG_ECX = 18
    CV_REG_EDX = 19
    CV_REG_EBX = 20
    CV_REG_ESP = 21
    CV_REG_EBP = 22
    CV_REG_ESI = 23
    CV_REG_EDI = 24
    CV_REG_ES = 25
    CV_REG_CS = 26
    CV_REG_SS = 27
    CV_REG_DS = 28
    CV_REG_FS = 29
    CV_REG_GS = 30
    CV_REG_IP = 31
    CV_REG_FLAGS = 32
    CV_REG_EIP = 33
    CV_REG_EFLAGS = 34
    CV_REG_TEMP = 40
    CV_REG_TEMPH = 41
    CV_REG_QUOTE = 42
    CV_REG_PCDR3 = 43
    CV_REG_PCDR4 = 44
    CV_REG_PCDR5 = 45
    CV_REG_PCDR6 = 46 
    CV_REG_PCDR7 = 47
    CV_REG_CR0 = 80 
    CV_REG_CR1 = 81
    CV_REG_CR2 = 82
    CV_REG_CR3 = 83
    CV_REG_CR4 = 84 
    CV_REG_DR0 = 90 
    CV_REG_DR1 = 91
    CV_REG_DR2 = 92
    CV_REG_DR3 = 93
    CV_REG_DR4 = 94
    CV_REG_DR5 = 95
    CV_REG_DR6 = 96
    CV_REG_DR7 = 97
    CV_REG_GDTR = 110
    CV_REG_GDTL = 111
    CV_REG_IDTR = 112
    CV_REG_IDTL = 113
    CV_REG_LDTR = 114
    CV_REG_TR = 115
    CV_REG_PSEUDO1 = 116
    CV_REG_PSEUDO2 = 117
    CV_REG_PSEUDO3 = 118
    CV_REG_PSEUDO4 = 119
    CV_REG_PSEUDO5 = 120
    CV_REG_PSEUDO6 = 121
    CV_REG_PSEUDO7 = 122
    CV_REG_PSEUDO8 = 123
    CV_REG_PSEUDO9 = 124
    CV_REG_ST0 = 128
    CV_REG_ST1 = 129
    CV_REG_ST2 = 130
    CV_REG_ST3 = 131
    CV_REG_ST4 = 132
    CV_REG_ST5 = 133
    CV_REG_ST6 = 134
    CV_REG_ST7 = 135
    CV_REG_CTRL = 136
    CV_REG_STAT = 137
    CV_REG_TAG = 138
    CV_REG_FPIP = 139
    CV_REG_FPCS = 140
    CV_REG_FPDO = 141
    CV_REG_FPDS = 142
    CV_REG_ISEM = 143
    CV_REG_FPEIP = 144
    CV_REG_FPEDO = 145
    CV_REG_MM0 = 146
    CV_REG_MM1 = 147
    CV_REG_MM2 = 148
    CV_REG_MM3 = 149
    CV_REG_MM4 = 150
    CV_REG_MM5 = 151
    CV_REG_MM6 = 152
    CV_REG_MM7 = 153
    CV_REG_XMM0 = 154 
    CV_REG_XMM1 = 155
    CV_REG_XMM2 = 156
    CV_REG_XMM3 = 157
    CV_REG_XMM4 = 158
    CV_REG_XMM5 = 159
    CV_REG_XMM6 = 160
    CV_REG_XMM7 = 161
    CV_REG_XMM00 = 162 
    CV_REG_XMM01 = 163
    CV_REG_XMM02 = 164
    CV_REG_XMM03 = 165
    CV_REG_XMM10 = 166
    CV_REG_XMM11 = 167
    CV_REG_XMM12 = 168
    CV_REG_XMM13 = 169
    CV_REG_XMM20 = 170
    CV_REG_XMM21 = 171
    CV_REG_XMM22 = 172
    CV_REG_XMM23 = 173
    CV_REG_XMM30 = 174
    CV_REG_XMM31 = 175
    CV_REG_XMM32 = 176
    CV_REG_XMM33 = 177
    CV_REG_XMM40 = 178
    CV_REG_XMM41 = 179
    CV_REG_XMM42 = 180
    CV_REG_XMM43 = 181
    CV_REG_XMM50 = 182
    CV_REG_XMM51 = 183
    CV_REG_XMM52 = 184
    CV_REG_XMM53 = 185
    CV_REG_XMM60 = 186
    CV_REG_XMM61 = 187
    CV_REG_XMM62 = 188
    CV_REG_XMM63 = 189
    CV_REG_XMM70 = 190
    CV_REG_XMM71 = 191
    CV_REG_XMM72 = 192
    CV_REG_XMM73 = 193
    CV_REG_XMM0L = 194
    CV_REG_XMM1L = 195
    CV_REG_XMM2L = 196
    CV_REG_XMM3L = 197
    CV_REG_XMM4L = 198
    CV_REG_XMM5L = 199
    CV_REG_XMM6L = 200
    CV_REG_XMM7L = 201
    CV_REG_XMM0H = 202
    CV_REG_XMM1H = 203
    CV_REG_XMM2H = 204
    CV_REG_XMM3H = 205
    CV_REG_XMM4H = 206
    CV_REG_XMM5H = 207
    CV_REG_XMM6H = 208
    CV_REG_XMM7H = 209
    CV_REG_MXCSR = 211
    CV_REG_EDXEAX = 212
    CV_REG_EMM0L = 220
    CV_REG_EMM1L = 221
    CV_REG_EMM2L = 222
    CV_REG_EMM3L = 223
    CV_REG_EMM4L = 224
    CV_REG_EMM5L = 225
    CV_REG_EMM6L = 226
    CV_REG_EMM7L = 227
    CV_REG_EMM0H = 228
    CV_REG_EMM1H = 229
    CV_REG_EMM2H = 230
    CV_REG_EMM3H = 231
    CV_REG_EMM4H = 232
    CV_REG_EMM5H = 233
    CV_REG_EMM6H = 234
    CV_REG_EMM7H = 235
    CV_REG_MM00 = 236
    CV_REG_MM01 = 237
    CV_REG_MM10 = 238
    CV_REG_MM11 = 239
    CV_REG_MM20 = 240
    CV_REG_MM21 = 241
    CV_REG_MM30 = 242
    CV_REG_MM31 = 243
    CV_REG_MM40 = 244
    CV_REG_MM41 = 245
    CV_REG_MM50 = 246
    CV_REG_MM51 = 247
    CV_REG_MM60 = 248
    CV_REG_MM61 = 249
    CV_REG_MM70 = 250
    CV_REG_MM71 = 251
    CV_REG_YMM0 = 252
    CV_REG_YMM1 = 253
    CV_REG_YMM2 = 254
    CV_REG_YMM3 = 255
    CV_REG_YMM4 = 256
    CV_REG_YMM5 = 257
    CV_REG_YMM6 = 258
    CV_REG_YMM7 = 259
    CV_REG_YMM0H = 260
    CV_REG_YMM1H = 261
    CV_REG_YMM2H = 262
    CV_REG_YMM3H = 263
    CV_REG_YMM4H = 264
    CV_REG_YMM5H = 265
    CV_REG_YMM6H = 266
    CV_REG_YMM7H = 267
    CV_REG_YMM0I0 = 268
    CV_REG_YMM0I1 = 269
    CV_REG_YMM0I2 = 270
    CV_REG_YMM0I3 = 271
    CV_REG_YMM1I0 = 272
    CV_REG_YMM1I1 = 273
    CV_REG_YMM1I2 = 274
    CV_REG_YMM1I3 = 275
    CV_REG_YMM2I0 = 276
    CV_REG_YMM2I1 = 277
    CV_REG_YMM2I2 = 278
    CV_REG_YMM2I3 = 279
    CV_REG_YMM3I0 = 280
    CV_REG_YMM3I1 = 281
    CV_REG_YMM3I2 = 282
    CV_REG_YMM3I3 = 283
    CV_REG_YMM4I0 = 284
    CV_REG_YMM4I1 = 285
    CV_REG_YMM4I2 = 286
    CV_REG_YMM4I3 = 287
    CV_REG_YMM5I0 = 288
    CV_REG_YMM5I1 = 289
    CV_REG_YMM5I2 = 290
    CV_REG_YMM5I3 = 291
    CV_REG_YMM6I0 = 292
    CV_REG_YMM6I1 = 293
    CV_REG_YMM6I2 = 294
    CV_REG_YMM6I3 = 295
    CV_REG_YMM7I0 = 296
    CV_REG_YMM7I1 = 297
    CV_REG_YMM7I2 = 298
    CV_REG_YMM7I3 = 299
    CV_REG_YMM0F0 = 300
    CV_REG_YMM0F1 = 301
    CV_REG_YMM0F2 = 302
    CV_REG_YMM0F3 = 303
    CV_REG_YMM0F4 = 304
    CV_REG_YMM0F5 = 305
    CV_REG_YMM0F6 = 306
    CV_REG_YMM0F7 = 307
    CV_REG_YMM1F0 = 308
    CV_REG_YMM1F1 = 309
    CV_REG_YMM1F2 = 310
    CV_REG_YMM1F3 = 311
    CV_REG_YMM1F4 = 312
    CV_REG_YMM1F5 = 313
    CV_REG_YMM1F6 = 314
    CV_REG_YMM1F7 = 315
    CV_REG_YMM2F0 = 316
    CV_REG_YMM2F1 = 317
    CV_REG_YMM2F2 = 318
    CV_REG_YMM2F3 = 319
    CV_REG_YMM2F4 = 320
    CV_REG_YMM2F5 = 321
    CV_REG_YMM2F6 = 322
    CV_REG_YMM2F7 = 323
    CV_REG_YMM3F0 = 324
    CV_REG_YMM3F1 = 325
    CV_REG_YMM3F2 = 326
    CV_REG_YMM3F3 = 327
    CV_REG_YMM3F4 = 328
    CV_REG_YMM3F5 = 329
    CV_REG_YMM3F6 = 330
    CV_REG_YMM3F7 = 331
    CV_REG_YMM4F0 = 332
    CV_REG_YMM4F1 = 333
    CV_REG_YMM4F2 = 334
    CV_REG_YMM4F3 = 335
    CV_REG_YMM4F4 = 336
    CV_REG_YMM4F5 = 337
    CV_REG_YMM4F6 = 338
    CV_REG_YMM4F7 = 339
    CV_REG_YMM5F0 = 340
    CV_REG_YMM5F1 = 341
    CV_REG_YMM5F2 = 342
    CV_REG_YMM5F3 = 343
    CV_REG_YMM5F4 = 344
    CV_REG_YMM5F5 = 345
    CV_REG_YMM5F6 = 346
    CV_REG_YMM5F7 = 347
    CV_REG_YMM6F0 = 348
    CV_REG_YMM6F1 = 349
    CV_REG_YMM6F2 = 350
    CV_REG_YMM6F3 = 351
    CV_REG_YMM6F4 = 352
    CV_REG_YMM6F5 = 353
    CV_REG_YMM6F6 = 354
    CV_REG_YMM6F7 = 355
    CV_REG_YMM7F0 = 356
    CV_REG_YMM7F1 = 357
    CV_REG_YMM7F2 = 358
    CV_REG_YMM7F3 = 359
    CV_REG_YMM7F4 = 360
    CV_REG_YMM7F5 = 361
    CV_REG_YMM7F6 = 362
    CV_REG_YMM7F7 = 363
    CV_REG_YMM0D0 = 364
    CV_REG_YMM0D1 = 365
    CV_REG_YMM0D2 = 366
    CV_REG_YMM0D3 = 367
    CV_REG_YMM1D0 = 368
    CV_REG_YMM1D1 = 369
    CV_REG_YMM1D2 = 370
    CV_REG_YMM1D3 = 371
    CV_REG_YMM2D0 = 372
    CV_REG_YMM2D1 = 373
    CV_REG_YMM2D2 = 374
    CV_REG_YMM2D3 = 375
    CV_REG_YMM3D0 = 376
    CV_REG_YMM3D1 = 377
    CV_REG_YMM3D2 = 378
    CV_REG_YMM3D3 = 379
    CV_REG_YMM4D0 = 380
    CV_REG_YMM4D1 = 381
    CV_REG_YMM4D2 = 382
    CV_REG_YMM4D3 = 383
    CV_REG_YMM5D0 = 384
    CV_REG_YMM5D1 = 385
    CV_REG_YMM5D2 = 386
    CV_REG_YMM5D3 = 387
    CV_REG_YMM6D0 = 388
    CV_REG_YMM6D1 = 389
    CV_REG_YMM6D2 = 390
    CV_REG_YMM6D3 = 391
    CV_REG_YMM7D0 = 392
    CV_REG_YMM7D1 = 393
    CV_REG_YMM7D2 = 394
    CV_REG_YMM7D3 = 395
    CV_REG_BND0 = 396
    CV_REG_BND1 = 397
    CV_REG_BND2 = 398
    CV_REG_BND3 = 399


class RegisterAMD64(enum.Enum):
    CV_REG_NONE       =   0
    CV_AMD64_AL       =   1
    CV_AMD64_CL       =   2
    CV_AMD64_DL       =   3
    CV_AMD64_BL       =   4
    CV_AMD64_AH       =   5
    CV_AMD64_CH       =   6
    CV_AMD64_DH       =   7
    CV_AMD64_BH       =   8
    CV_AMD64_AX       =   9
    CV_AMD64_CX       =  10
    CV_AMD64_DX       =  11
    CV_AMD64_BX       =  12
    CV_AMD64_SP       =  13
    CV_AMD64_BP       =  14
    CV_AMD64_SI       =  15
    CV_AMD64_DI       =  16
    CV_AMD64_EAX      =  17
    CV_AMD64_ECX      =  18
    CV_AMD64_EDX      =  19
    CV_AMD64_EBX      =  20
    CV_AMD64_ESP      =  21
    CV_AMD64_EBP      =  22
    CV_AMD64_ESI      =  23
    CV_AMD64_EDI      =  24
    CV_AMD64_ES       =  25
    CV_AMD64_CS       =  26
    CV_AMD64_SS       =  27
    CV_AMD64_DS       =  28
    CV_AMD64_FS       =  29
    CV_AMD64_GS       =  30
    CV_AMD64_FLAGS    =  32
    CV_AMD64_RIP      =  33
    CV_AMD64_EFLAGS   =  34
    CV_AMD64_CR0      =  80
    CV_AMD64_CR1      =  81
    CV_AMD64_CR2      =  82
    CV_AMD64_CR3      =  83
    CV_AMD64_CR4      =  84
    CV_AMD64_CR8      =  88
    CV_AMD64_DR0      =  90
    CV_AMD64_DR1      =  91
    CV_AMD64_DR2      =  92
    CV_AMD64_DR3      =  93
    CV_AMD64_DR4      =  94
    CV_AMD64_DR5      =  95
    CV_AMD64_DR6      =  96
    CV_AMD64_DR7      =  97
    CV_AMD64_DR8      =  98
    CV_AMD64_DR9      =  99
    CV_AMD64_DR10     =  100
    CV_AMD64_DR11     =  101
    CV_AMD64_DR12     =  102
    CV_AMD64_DR13     =  103
    CV_AMD64_DR14     =  104
    CV_AMD64_DR15     =  105
    CV_AMD64_GDTR     =  110
    CV_AMD64_GDTL     =  111
    CV_AMD64_IDTR     =  112
    CV_AMD64_IDTL     =  113
    CV_AMD64_LDTR     =  114
    CV_AMD64_TR       =  115
    CV_AMD64_ST0      =  128
    CV_AMD64_ST1      =  129
    CV_AMD64_ST2      =  130
    CV_AMD64_ST3      =  131
    CV_AMD64_ST4      =  132
    CV_AMD64_ST5      =  133
    CV_AMD64_ST6      =  134
    CV_AMD64_ST7      =  135
    CV_AMD64_CTRL     =  136
    CV_AMD64_STAT     =  137
    CV_AMD64_TAG      =  138
    CV_AMD64_FPIP     =  139
    CV_AMD64_FPCS     =  140
    CV_AMD64_FPDO     =  141
    CV_AMD64_FPDS     =  142
    CV_AMD64_ISEM     =  143
    CV_AMD64_FPEIP    =  144
    CV_AMD64_FPEDO    =  145
    CV_AMD64_MM0      =  146
    CV_AMD64_MM1      =  147
    CV_AMD64_MM2      =  148
    CV_AMD64_MM3      =  149
    CV_AMD64_MM4      =  150
    CV_AMD64_MM5      =  151
    CV_AMD64_MM6      =  152
    CV_AMD64_MM7      =  153
    CV_AMD64_XMM0     =  154
    CV_AMD64_XMM1     =  155
    CV_AMD64_XMM2     =  156
    CV_AMD64_XMM3     =  157
    CV_AMD64_XMM4     =  158
    CV_AMD64_XMM5     =  159
    CV_AMD64_XMM6     =  160
    CV_AMD64_XMM7     =  161
    CV_AMD64_XMM0_0   =  162
    CV_AMD64_XMM0_1   =  163
    CV_AMD64_XMM0_2   =  164
    CV_AMD64_XMM0_3   =  165
    CV_AMD64_XMM1_0   =  166
    CV_AMD64_XMM1_1   =  167
    CV_AMD64_XMM1_2   =  168
    CV_AMD64_XMM1_3   =  169
    CV_AMD64_XMM2_0   =  170
    CV_AMD64_XMM2_1   =  171
    CV_AMD64_XMM2_2   =  172
    CV_AMD64_XMM2_3   =  173
    CV_AMD64_XMM3_0   =  174
    CV_AMD64_XMM3_1   =  175
    CV_AMD64_XMM3_2   =  176
    CV_AMD64_XMM3_3   =  177
    CV_AMD64_XMM4_0   =  178
    CV_AMD64_XMM4_1   =  179
    CV_AMD64_XMM4_2   =  180
    CV_AMD64_XMM4_3   =  181
    CV_AMD64_XMM5_0   =  182
    CV_AMD64_XMM5_1   =  183
    CV_AMD64_XMM5_2   =  184
    CV_AMD64_XMM5_3   =  185
    CV_AMD64_XMM6_0   =  186
    CV_AMD64_XMM6_1   =  187
    CV_AMD64_XMM6_2   =  188
    CV_AMD64_XMM6_3   =  189
    CV_AMD64_XMM7_0   =  190
    CV_AMD64_XMM7_1   =  191
    CV_AMD64_XMM7_2   =  192
    CV_AMD64_XMM7_3   =  193
    CV_AMD64_XMM0L    =  194
    CV_AMD64_XMM1L    =  195
    CV_AMD64_XMM2L    =  196
    CV_AMD64_XMM3L    =  197
    CV_AMD64_XMM4L    =  198
    CV_AMD64_XMM5L    =  199
    CV_AMD64_XMM6L    =  200
    CV_AMD64_XMM7L    =  201
    CV_AMD64_XMM0H    =  202
    CV_AMD64_XMM1H    =  203
    CV_AMD64_XMM2H    =  204
    CV_AMD64_XMM3H    =  205
    CV_AMD64_XMM4H    =  206
    CV_AMD64_XMM5H    =  207
    CV_AMD64_XMM6H    =  208
    CV_AMD64_XMM7H    =  209
    CV_AMD64_MXCSR    =  211
    CV_AMD64_EMM0L    =  220
    CV_AMD64_EMM1L    =  221
    CV_AMD64_EMM2L    =  222
    CV_AMD64_EMM3L    =  223
    CV_AMD64_EMM4L    =  224
    CV_AMD64_EMM5L    =  225
    CV_AMD64_EMM6L    =  226
    CV_AMD64_EMM7L    =  227
    CV_AMD64_EMM0H    =  228
    CV_AMD64_EMM1H    =  229
    CV_AMD64_EMM2H    =  230
    CV_AMD64_EMM3H    =  231
    CV_AMD64_EMM4H    =  232
    CV_AMD64_EMM5H    =  233
    CV_AMD64_EMM6H    =  234
    CV_AMD64_EMM7H    =  235
    CV_AMD64_MM00     =  236
    CV_AMD64_MM01     =  237
    CV_AMD64_MM10     =  238
    CV_AMD64_MM11     =  239
    CV_AMD64_MM20     =  240
    CV_AMD64_MM21     =  241
    CV_AMD64_MM30     =  242
    CV_AMD64_MM31     =  243
    CV_AMD64_MM40     =  244
    CV_AMD64_MM41     =  245
    CV_AMD64_MM50     =  246
    CV_AMD64_MM51     =  247
    CV_AMD64_MM60     =  248
    CV_AMD64_MM61     =  249
    CV_AMD64_MM70     =  250
    CV_AMD64_MM71     =  251
    CV_AMD64_XMM8     =  252
    CV_AMD64_XMM9     =  253
    CV_AMD64_XMM10    =  254
    CV_AMD64_XMM11    =  255
    CV_AMD64_XMM12    =  256
    CV_AMD64_XMM13    =  257
    CV_AMD64_XMM14    =  258
    CV_AMD64_XMM15    =  259
    CV_AMD64_XMM8_0   =  260
    CV_AMD64_XMM8_1   =  261
    CV_AMD64_XMM8_2   =  262
    CV_AMD64_XMM8_3   =  263
    CV_AMD64_XMM9_0   =  264
    CV_AMD64_XMM9_1   =  265
    CV_AMD64_XMM9_2   =  266
    CV_AMD64_XMM9_3   =  267
    CV_AMD64_XMM10_0  =  268
    CV_AMD64_XMM10_1  =  269
    CV_AMD64_XMM10_2  =  270
    CV_AMD64_XMM10_3  =  271
    CV_AMD64_XMM11_0  =  272
    CV_AMD64_XMM11_1  =  273
    CV_AMD64_XMM11_2  =  274
    CV_AMD64_XMM11_3  =  275
    CV_AMD64_XMM12_0  =  276
    CV_AMD64_XMM12_1  =  277
    CV_AMD64_XMM12_2  =  278
    CV_AMD64_XMM12_3  =  279
    CV_AMD64_XMM13_0  =  280
    CV_AMD64_XMM13_1  =  281
    CV_AMD64_XMM13_2  =  282
    CV_AMD64_XMM13_3  =  283
    CV_AMD64_XMM14_0  =  284
    CV_AMD64_XMM14_1  =  285
    CV_AMD64_XMM14_2  =  286
    CV_AMD64_XMM14_3  =  287
    CV_AMD64_XMM15_0  =  288
    CV_AMD64_XMM15_1  =  289
    CV_AMD64_XMM15_2  =  290
    CV_AMD64_XMM15_3  =  291
    CV_AMD64_XMM8L    =  292
    CV_AMD64_XMM9L    =  293
    CV_AMD64_XMM10L   =  294
    CV_AMD64_XMM11L   =  295
    CV_AMD64_XMM12L   =  296
    CV_AMD64_XMM13L   =  297
    CV_AMD64_XMM14L   =  298
    CV_AMD64_XMM15L   =  299
    CV_AMD64_XMM8H    =  300
    CV_AMD64_XMM9H    =  301
    CV_AMD64_XMM10H   =  302
    CV_AMD64_XMM11H   =  303
    CV_AMD64_XMM12H   =  304
    CV_AMD64_XMM13H   =  305
    CV_AMD64_XMM14H   =  306
    CV_AMD64_XMM15H   =  307
    CV_AMD64_EMM8L    =  308
    CV_AMD64_EMM9L    =  309
    CV_AMD64_EMM10L   =  310
    CV_AMD64_EMM11L   =  311
    CV_AMD64_EMM12L   =  312
    CV_AMD64_EMM13L   =  313
    CV_AMD64_EMM14L   =  314
    CV_AMD64_EMM15L   =  315
    CV_AMD64_EMM8H    =  316
    CV_AMD64_EMM9H    =  317
    CV_AMD64_EMM10H   =  318
    CV_AMD64_EMM11H   =  319
    CV_AMD64_EMM12H   =  320
    CV_AMD64_EMM13H   =  321
    CV_AMD64_EMM14H   =  322
    CV_AMD64_EMM15H   =  323
    CV_AMD64_SIL      =  324
    CV_AMD64_DIL      =  325
    CV_AMD64_BPL      =  326
    CV_AMD64_SPL      =  327
    CV_AMD64_RAX      =  328
    CV_AMD64_RBX      =  329
    CV_AMD64_RCX      =  330
    CV_AMD64_RDX      =  331
    CV_AMD64_RSI      =  332
    CV_AMD64_RDI      =  333
    CV_AMD64_RBP      =  334
    CV_AMD64_RSP      =  335
    CV_AMD64_R8       =  336
    CV_AMD64_R9       =  337
    CV_AMD64_R10      =  338
    CV_AMD64_R11      =  339
    CV_AMD64_R12      =  340
    CV_AMD64_R13      =  341
    CV_AMD64_R14      =  342
    CV_AMD64_R15      =  343
    CV_AMD64_R8B      =  344
    CV_AMD64_R9B      =  345
    CV_AMD64_R10B     =  346
    CV_AMD64_R11B     =  347
    CV_AMD64_R12B     =  348
    CV_AMD64_R13B     =  349
    CV_AMD64_R14B     =  350
    CV_AMD64_R15B     =  351
    CV_AMD64_R8W      =  352
    CV_AMD64_R9W      =  353
    CV_AMD64_R10W     =  354
    CV_AMD64_R11W     =  355
    CV_AMD64_R12W     =  356
    CV_AMD64_R13W     =  357
    CV_AMD64_R14W     =  358
    CV_AMD64_R15W     =  359
    CV_AMD64_R8D      =  360
    CV_AMD64_R9D      =  361
    CV_AMD64_R10D     =  362
    CV_AMD64_R11D     =  363
    CV_AMD64_R12D     =  364
    CV_AMD64_R13D     =  365
    CV_AMD64_R14D     =  366
    CV_AMD64_R15D     =  367
    CV_AMD64_YMM0     =  368
    CV_AMD64_YMM1     =  369
    CV_AMD64_YMM2     =  370
    CV_AMD64_YMM3     =  371
    CV_AMD64_YMM4     =  372
    CV_AMD64_YMM5     =  373
    CV_AMD64_YMM6     =  374
    CV_AMD64_YMM7     =  375
    CV_AMD64_YMM8     =  376
    CV_AMD64_YMM9     =  377
    CV_AMD64_YMM10    =  378
    CV_AMD64_YMM11    =  379
    CV_AMD64_YMM12    =  380
    CV_AMD64_YMM13    =  381
    CV_AMD64_YMM14    =  382
    CV_AMD64_YMM15    =  383
    CV_AMD64_YMM0H    =  384
    CV_AMD64_YMM1H    =  385
    CV_AMD64_YMM2H    =  386
    CV_AMD64_YMM3H    =  387
    CV_AMD64_YMM4H    =  388
    CV_AMD64_YMM5H    =  389
    CV_AMD64_YMM6H    =  390
    CV_AMD64_YMM7H    =  391
    CV_AMD64_YMM8H    =  392
    CV_AMD64_YMM9H    =  393
    CV_AMD64_YMM10H   =  394
    CV_AMD64_YMM11H   =  395
    CV_AMD64_YMM12H   =  396
    CV_AMD64_YMM13H   =  397
    CV_AMD64_YMM14H   =  398
    CV_AMD64_YMM15H   =  399
    CV_AMD64_XMM0IL    = 400
    CV_AMD64_XMM1IL    = 401
    CV_AMD64_XMM2IL    = 402
    CV_AMD64_XMM3IL    = 403
    CV_AMD64_XMM4IL    = 404
    CV_AMD64_XMM5IL    = 405
    CV_AMD64_XMM6IL    = 406
    CV_AMD64_XMM7IL    = 407
    CV_AMD64_XMM8IL    = 408
    CV_AMD64_XMM9IL    = 409
    CV_AMD64_XMM10IL    = 410
    CV_AMD64_XMM11IL    = 411
    CV_AMD64_XMM12IL    = 412
    CV_AMD64_XMM13IL    = 413
    CV_AMD64_XMM14IL    = 414
    CV_AMD64_XMM15IL    = 415
    CV_AMD64_XMM0IH    = 416
    CV_AMD64_XMM1IH    = 417
    CV_AMD64_XMM2IH    = 418
    CV_AMD64_XMM3IH    = 419
    CV_AMD64_XMM4IH    = 420
    CV_AMD64_XMM5IH    = 421
    CV_AMD64_XMM6IH    = 422
    CV_AMD64_XMM7IH    = 423
    CV_AMD64_XMM8IH    = 424
    CV_AMD64_XMM9IH    = 425
    CV_AMD64_XMM10IH    = 426
    CV_AMD64_XMM11IH    = 427
    CV_AMD64_XMM12IH    = 428
    CV_AMD64_XMM13IH    = 429
    CV_AMD64_XMM14IH    = 430
    CV_AMD64_XMM15IH    = 431
    CV_AMD64_YMM0I0    =  432
    CV_AMD64_YMM0I1    =  433
    CV_AMD64_YMM0I2    =  434
    CV_AMD64_YMM0I3    =  435
    CV_AMD64_YMM1I0    =  436
    CV_AMD64_YMM1I1    =  437
    CV_AMD64_YMM1I2    =  438
    CV_AMD64_YMM1I3    =  439
    CV_AMD64_YMM2I0    =  440
    CV_AMD64_YMM2I1    =  441
    CV_AMD64_YMM2I2    =  442
    CV_AMD64_YMM2I3    =  443
    CV_AMD64_YMM3I0    =  444
    CV_AMD64_YMM3I1    =  445
    CV_AMD64_YMM3I2    =  446
    CV_AMD64_YMM3I3    =  447
    CV_AMD64_YMM4I0    =  448
    CV_AMD64_YMM4I1    =  449
    CV_AMD64_YMM4I2    =  450
    CV_AMD64_YMM4I3    =  451
    CV_AMD64_YMM5I0    =  452
    CV_AMD64_YMM5I1    =  453
    CV_AMD64_YMM5I2    =  454
    CV_AMD64_YMM5I3    =  455
    CV_AMD64_YMM6I0    =  456
    CV_AMD64_YMM6I1    =  457
    CV_AMD64_YMM6I2    =  458
    CV_AMD64_YMM6I3    =  459
    CV_AMD64_YMM7I0    =  460
    CV_AMD64_YMM7I1    =  461
    CV_AMD64_YMM7I2    =  462
    CV_AMD64_YMM7I3    =  463
    CV_AMD64_YMM8I0    =  464
    CV_AMD64_YMM8I1    =  465
    CV_AMD64_YMM8I2    =  466
    CV_AMD64_YMM8I3    =  467
    CV_AMD64_YMM9I0    =  468
    CV_AMD64_YMM9I1    =  469
    CV_AMD64_YMM9I2    =  470
    CV_AMD64_YMM9I3    =  471
    CV_AMD64_YMM10I0    =  472
    CV_AMD64_YMM10I1    =  473
    CV_AMD64_YMM10I2    =  474
    CV_AMD64_YMM10I3    =  475
    CV_AMD64_YMM11I0    =  476
    CV_AMD64_YMM11I1    =  477
    CV_AMD64_YMM11I2    =  478
    CV_AMD64_YMM11I3    =  479
    CV_AMD64_YMM12I0    =  480
    CV_AMD64_YMM12I1    =  481
    CV_AMD64_YMM12I2    =  482
    CV_AMD64_YMM12I3    =  483
    CV_AMD64_YMM13I0    =  484
    CV_AMD64_YMM13I1    =  485
    CV_AMD64_YMM13I2    =  486
    CV_AMD64_YMM13I3    =  487
    CV_AMD64_YMM14I0    =  488
    CV_AMD64_YMM14I1    =  489
    CV_AMD64_YMM14I2    =  490
    CV_AMD64_YMM14I3    =  491
    CV_AMD64_YMM15I0    =  492
    CV_AMD64_YMM15I1    =  493
    CV_AMD64_YMM15I2    =  494
    CV_AMD64_YMM15I3    =  495
    CV_AMD64_YMM0F0    =  496
    CV_AMD64_YMM0F1    =  497
    CV_AMD64_YMM0F2    =  498
    CV_AMD64_YMM0F3    =  499
    CV_AMD64_YMM0F4    =  500
    CV_AMD64_YMM0F5    =  501
    CV_AMD64_YMM0F6    =  502
    CV_AMD64_YMM0F7    =  503
    CV_AMD64_YMM1F0    =  504
    CV_AMD64_YMM1F1    =  505
    CV_AMD64_YMM1F2    =  506
    CV_AMD64_YMM1F3    =  507
    CV_AMD64_YMM1F4    =  508
    CV_AMD64_YMM1F5    =  509
    CV_AMD64_YMM1F6    =  510
    CV_AMD64_YMM1F7    =  511
    CV_AMD64_YMM2F0    =  512
    CV_AMD64_YMM2F1    =  513
    CV_AMD64_YMM2F2    =  514
    CV_AMD64_YMM2F3    =  515
    CV_AMD64_YMM2F4    =  516
    CV_AMD64_YMM2F5    =  517
    CV_AMD64_YMM2F6    =  518
    CV_AMD64_YMM2F7    =  519
    CV_AMD64_YMM3F0    =  520
    CV_AMD64_YMM3F1    =  521
    CV_AMD64_YMM3F2    =  522
    CV_AMD64_YMM3F3    =  523
    CV_AMD64_YMM3F4    =  524
    CV_AMD64_YMM3F5    =  525
    CV_AMD64_YMM3F6    =  526
    CV_AMD64_YMM3F7    =  527
    CV_AMD64_YMM4F0    =  528
    CV_AMD64_YMM4F1    =  529
    CV_AMD64_YMM4F2    =  530
    CV_AMD64_YMM4F3    =  531
    CV_AMD64_YMM4F4    =  532
    CV_AMD64_YMM4F5    =  533
    CV_AMD64_YMM4F6    =  534
    CV_AMD64_YMM4F7    =  535
    CV_AMD64_YMM5F0    =  536
    CV_AMD64_YMM5F1    =  537
    CV_AMD64_YMM5F2    =  538
    CV_AMD64_YMM5F3    =  539
    CV_AMD64_YMM5F4    =  540
    CV_AMD64_YMM5F5    =  541
    CV_AMD64_YMM5F6    =  542
    CV_AMD64_YMM5F7    =  543
    CV_AMD64_YMM6F0    =  544
    CV_AMD64_YMM6F1    =  545
    CV_AMD64_YMM6F2    =  546
    CV_AMD64_YMM6F3    =  547
    CV_AMD64_YMM6F4    =  548
    CV_AMD64_YMM6F5    =  549
    CV_AMD64_YMM6F6    =  550
    CV_AMD64_YMM6F7    =  551
    CV_AMD64_YMM7F0    =  552
    CV_AMD64_YMM7F1    =  553
    CV_AMD64_YMM7F2    =  554
    CV_AMD64_YMM7F3    =  555
    CV_AMD64_YMM7F4    =  556
    CV_AMD64_YMM7F5    =  557
    CV_AMD64_YMM7F6    =  558
    CV_AMD64_YMM7F7    =  559
    CV_AMD64_YMM8F0    =  560
    CV_AMD64_YMM8F1    =  561
    CV_AMD64_YMM8F2    =  562
    CV_AMD64_YMM8F3    =  563
    CV_AMD64_YMM8F4    =  564
    CV_AMD64_YMM8F5    =  565
    CV_AMD64_YMM8F6    =  566
    CV_AMD64_YMM8F7    =  567
    CV_AMD64_YMM9F0    =  568
    CV_AMD64_YMM9F1    =  569
    CV_AMD64_YMM9F2    =  570
    CV_AMD64_YMM9F3    =  571
    CV_AMD64_YMM9F4    =  572
    CV_AMD64_YMM9F5    =  573
    CV_AMD64_YMM9F6    =  574
    CV_AMD64_YMM9F7    =  575
    CV_AMD64_YMM10F0    =  576
    CV_AMD64_YMM10F1    =  577
    CV_AMD64_YMM10F2    =  578
    CV_AMD64_YMM10F3    =  579
    CV_AMD64_YMM10F4    =  580
    CV_AMD64_YMM10F5    =  581
    CV_AMD64_YMM10F6    =  582
    CV_AMD64_YMM10F7    =  583
    CV_AMD64_YMM11F0    =  584
    CV_AMD64_YMM11F1    =  585
    CV_AMD64_YMM11F2    =  586
    CV_AMD64_YMM11F3    =  587
    CV_AMD64_YMM11F4    =  588
    CV_AMD64_YMM11F5    =  589
    CV_AMD64_YMM11F6    =  590
    CV_AMD64_YMM11F7    =  591
    CV_AMD64_YMM12F0    =  592
    CV_AMD64_YMM12F1    =  593
    CV_AMD64_YMM12F2    =  594
    CV_AMD64_YMM12F3    =  595
    CV_AMD64_YMM12F4    =  596
    CV_AMD64_YMM12F5    =  597
    CV_AMD64_YMM12F6    =  598
    CV_AMD64_YMM12F7    =  599
    CV_AMD64_YMM13F0    =  600
    CV_AMD64_YMM13F1    =  601
    CV_AMD64_YMM13F2    =  602
    CV_AMD64_YMM13F3    =  603
    CV_AMD64_YMM13F4    =  604
    CV_AMD64_YMM13F5    =  605
    CV_AMD64_YMM13F6    =  606
    CV_AMD64_YMM13F7    =  607
    CV_AMD64_YMM14F0    =  608
    CV_AMD64_YMM14F1    =  609
    CV_AMD64_YMM14F2    =  610
    CV_AMD64_YMM14F3    =  611
    CV_AMD64_YMM14F4    =  612
    CV_AMD64_YMM14F5    =  613
    CV_AMD64_YMM14F6    =  614
    CV_AMD64_YMM14F7    =  615
    CV_AMD64_YMM15F0    =  616
    CV_AMD64_YMM15F1    =  617
    CV_AMD64_YMM15F2    =  618
    CV_AMD64_YMM15F3    =  619
    CV_AMD64_YMM15F4    =  620
    CV_AMD64_YMM15F5    =  621
    CV_AMD64_YMM15F6    =  622
    CV_AMD64_YMM15F7    =  623
    CV_AMD64_YMM0D0    =  624
    CV_AMD64_YMM0D1    =  625
    CV_AMD64_YMM0D2    =  626
    CV_AMD64_YMM0D3    =  627
    CV_AMD64_YMM1D0    =  628
    CV_AMD64_YMM1D1    =  629
    CV_AMD64_YMM1D2    =  630
    CV_AMD64_YMM1D3    =  631
    CV_AMD64_YMM2D0    =  632
    CV_AMD64_YMM2D1    =  633
    CV_AMD64_YMM2D2    =  634
    CV_AMD64_YMM2D3    =  635
    CV_AMD64_YMM3D0    =  636
    CV_AMD64_YMM3D1    =  637
    CV_AMD64_YMM3D2    =  638
    CV_AMD64_YMM3D3    =  639
    CV_AMD64_YMM4D0    =  640
    CV_AMD64_YMM4D1    =  641
    CV_AMD64_YMM4D2    =  642
    CV_AMD64_YMM4D3    =  643
    CV_AMD64_YMM5D0    =  644
    CV_AMD64_YMM5D1    =  645
    CV_AMD64_YMM5D2    =  646
    CV_AMD64_YMM5D3    =  647
    CV_AMD64_YMM6D0    =  648
    CV_AMD64_YMM6D1    =  649
    CV_AMD64_YMM6D2    =  650
    CV_AMD64_YMM6D3    =  651
    CV_AMD64_YMM7D0    =  652
    CV_AMD64_YMM7D1    =  653
    CV_AMD64_YMM7D2    =  654
    CV_AMD64_YMM7D3    =  655
    CV_AMD64_YMM8D0    =  656
    CV_AMD64_YMM8D1    =  657
    CV_AMD64_YMM8D2    =  658
    CV_AMD64_YMM8D3    =  659
    CV_AMD64_YMM9D0    =  660
    CV_AMD64_YMM9D1    =  661
    CV_AMD64_YMM9D2    =  662
    CV_AMD64_YMM9D3    =  663
    CV_AMD64_YMM10D0    =  664
    CV_AMD64_YMM10D1    =  665
    CV_AMD64_YMM10D2    =  666
    CV_AMD64_YMM10D3    =  667
    CV_AMD64_YMM11D0    =  668
    CV_AMD64_YMM11D1    =  669
    CV_AMD64_YMM11D2    =  670
    CV_AMD64_YMM11D3    =  671
    CV_AMD64_YMM12D0    =  672
    CV_AMD64_YMM12D1    =  673
    CV_AMD64_YMM12D2    =  674
    CV_AMD64_YMM12D3    =  675
    CV_AMD64_YMM13D0    =  676
    CV_AMD64_YMM13D1    =  677
    CV_AMD64_YMM13D2    =  678
    CV_AMD64_YMM13D3    =  679
    CV_AMD64_YMM14D0    =  680
    CV_AMD64_YMM14D1    =  681
    CV_AMD64_YMM14D2    =  682
    CV_AMD64_YMM14D3    =  683
    CV_AMD64_YMM15D0    =  684
    CV_AMD64_YMM15D1    =  685
    CV_AMD64_YMM15D2    =  686
    CV_AMD64_YMM15D3    =  687

class RegisterARM64(enum.Enum):
    CV_ARM64_NOREG  =  0
    CV_ARM64_W0     =  10
    CV_ARM64_W1     =  11
    CV_ARM64_W2     =  12
    CV_ARM64_W3     =  13
    CV_ARM64_W4     =  14
    CV_ARM64_W5     =  15
    CV_ARM64_W6     =  16
    CV_ARM64_W7     =  17
    CV_ARM64_W8     =  18
    CV_ARM64_W9     =  19
    CV_ARM64_W10    =  20
    CV_ARM64_W11    =  21
    CV_ARM64_W12    =  22
    CV_ARM64_W13    =  23
    CV_ARM64_W14    =  24
    CV_ARM64_W15    =  25
    CV_ARM64_W16    =  26
    CV_ARM64_W17    =  27
    CV_ARM64_W18    =  28
    CV_ARM64_W19    =  29
    CV_ARM64_W20    =  30
    CV_ARM64_W21    =  31
    CV_ARM64_W22    =  32
    CV_ARM64_W23    =  33
    CV_ARM64_W24    =  34
    CV_ARM64_W25    =  35
    CV_ARM64_W26    =  36
    CV_ARM64_W27    =  37
    CV_ARM64_W28    =  38
    CV_ARM64_W29    =  39
    CV_ARM64_W30    =  40
    CV_ARM64_WZR    =  41
    CV_ARM64_X0     =  50
    CV_ARM64_X1     =  51
    CV_ARM64_X2     =  52
    CV_ARM64_X3     =  53
    CV_ARM64_X4     =  54
    CV_ARM64_X5     =  55
    CV_ARM64_X6     =  56
    CV_ARM64_X7     =  57
    CV_ARM64_X8     =  58
    CV_ARM64_X9     =  59
    CV_ARM64_X10    =  60
    CV_ARM64_X11    =  61
    CV_ARM64_X12    =  62
    CV_ARM64_X13    =  63
    CV_ARM64_X14    =  64
    CV_ARM64_X15    =  65
    CV_ARM64_IP0    =  66
    CV_ARM64_IP1    =  67
    CV_ARM64_X18    =  68
    CV_ARM64_X19    =  69
    CV_ARM64_X20    =  70
    CV_ARM64_X21    =  71
    CV_ARM64_X22    =  72
    CV_ARM64_X23    =  73
    CV_ARM64_X24    =  74
    CV_ARM64_X25    =  75
    CV_ARM64_X26    =  76
    CV_ARM64_X27    =  77
    CV_ARM64_X28    =  78
    CV_ARM64_FP     =  79
    CV_ARM64_LR     =  80
    CV_ARM64_SP     =  81
    CV_ARM64_ZR     =  82
    CV_ARM64_NZCV   =  90
    CV_ARM64_S0     =  100
    CV_ARM64_S1     =  101
    CV_ARM64_S2     =  102
    CV_ARM64_S3     =  103
    CV_ARM64_S4     =  104
    CV_ARM64_S5     =  105
    CV_ARM64_S6     =  106
    CV_ARM64_S7     =  107
    CV_ARM64_S8     =  108
    CV_ARM64_S9     =  109
    CV_ARM64_S10    =  110
    CV_ARM64_S11    =  111
    CV_ARM64_S12    =  112
    CV_ARM64_S13    =  113
    CV_ARM64_S14    =  114
    CV_ARM64_S15    =  115
    CV_ARM64_S16    =  116
    CV_ARM64_S17    =  117
    CV_ARM64_S18    =  118
    CV_ARM64_S19    =  119
    CV_ARM64_S20    =  120
    CV_ARM64_S21    =  121
    CV_ARM64_S22    =  122
    CV_ARM64_S23    =  123
    CV_ARM64_S24    =  124
    CV_ARM64_S25    =  125
    CV_ARM64_S26    =  126
    CV_ARM64_S27    =  127
    CV_ARM64_S28    =  128
    CV_ARM64_S29    =  129
    CV_ARM64_S30    =  130
    CV_ARM64_S31    =  131
    CV_ARM64_D0     =  140
    CV_ARM64_D1     =  141
    CV_ARM64_D2     =  142
    CV_ARM64_D3     =  143
    CV_ARM64_D4     =  144
    CV_ARM64_D5     =  145
    CV_ARM64_D6     =  146
    CV_ARM64_D7     =  147
    CV_ARM64_D8     =  148
    CV_ARM64_D9     =  149
    CV_ARM64_D10    =  150
    CV_ARM64_D11    =  151
    CV_ARM64_D12    =  152
    CV_ARM64_D13    =  153
    CV_ARM64_D14    =  154
    CV_ARM64_D15    =  155
    CV_ARM64_D16    =  156
    CV_ARM64_D17    =  157
    CV_ARM64_D18    =  158
    CV_ARM64_D19    =  159
    CV_ARM64_D20    =  160
    CV_ARM64_D21    =  161
    CV_ARM64_D22    =  162
    CV_ARM64_D23    =  163
    CV_ARM64_D24    =  164
    CV_ARM64_D25    =  165
    CV_ARM64_D26    =  166
    CV_ARM64_D27    =  167
    CV_ARM64_D28    =  168
    CV_ARM64_D29    =  169
    CV_ARM64_D30    =  170
    CV_ARM64_D31    =  171
    CV_ARM64_Q0     =  180
    CV_ARM64_Q1     =  181
    CV_ARM64_Q2     =  182
    CV_ARM64_Q3     =  183
    CV_ARM64_Q4     =  184
    CV_ARM64_Q5     =  185
    CV_ARM64_Q6     =  186
    CV_ARM64_Q7     =  187
    CV_ARM64_Q8     =  188
    CV_ARM64_Q9     =  189
    CV_ARM64_Q10    =  190
    CV_ARM64_Q11    =  191
    CV_ARM64_Q12    =  192
    CV_ARM64_Q13    =  193
    CV_ARM64_Q14    =  194
    CV_ARM64_Q15    =  195
    CV_ARM64_Q16    =  196
    CV_ARM64_Q17    =  197
    CV_ARM64_Q18    =  198
    CV_ARM64_Q19    =  199
    CV_ARM64_Q20    =  200
    CV_ARM64_Q21    =  201
    CV_ARM64_Q22    =  202
    CV_ARM64_Q23    =  203
    CV_ARM64_Q24    =  204
    CV_ARM64_Q25    =  205
    CV_ARM64_Q26    =  206
    CV_ARM64_Q27    =  207
    CV_ARM64_Q28    =  208
    CV_ARM64_Q29    =  209
    CV_ARM64_Q30    =  210
    CV_ARM64_Q31    =  211
    CV_ARM64_FPSR   =  220

class RegisterCommon(enum.Enum):
    CV_ALLREG_ERR   =   30000
    CV_ALLREG_TEB   =   30001
    CV_ALLREG_TIMER =   30002
    CV_ALLREG_EFAD1 =   30003
    CV_ALLREG_EFAD2 =   30004
    CV_ALLREG_EFAD3 =   30005
    CV_ALLREG_VFRAME=   30006
    CV_ALLREG_HANDLE=   30007
    CV_ALLREG_PARAMS=   30008
    CV_ALLREG_LOCALS=   30009
    CV_ALLREG_TID   =   30010
    CV_ALLREG_ENV   =   30011
    CV_ALLREG_CMDLN =   30012



ARM64_REG_TO_NAME: dict[RegisterARM64, str] = {
    RegisterARM64.CV_ARM64_NOREG: "None",
    RegisterARM64.CV_ARM64_W0: "w0",
    RegisterARM64.CV_ARM64_W1: "w1",
    RegisterARM64.CV_ARM64_W2: "w2",
    RegisterARM64.CV_ARM64_W3: "w3",
    RegisterARM64.CV_ARM64_W4: "w4",
    RegisterARM64.CV_ARM64_W5: "w5",
    RegisterARM64.CV_ARM64_W6: "w6",
    RegisterARM64.CV_ARM64_W7: "w7",
    RegisterARM64.CV_ARM64_W8: "w8",
    RegisterARM64.CV_ARM64_W9: "w9",
    RegisterARM64.CV_ARM64_W10: "w10",
    RegisterARM64.CV_ARM64_W11: "w11",
    RegisterARM64.CV_ARM64_W12: "w12",
    RegisterARM64.CV_ARM64_W13: "w13",
    RegisterARM64.CV_ARM64_W14: "w14",
    RegisterARM64.CV_ARM64_W15: "w15",
    RegisterARM64.CV_ARM64_W16: "w16",
    RegisterARM64.CV_ARM64_W17: "w17",
    RegisterARM64.CV_ARM64_W18: "w18",
    RegisterARM64.CV_ARM64_W19: "w19",
    RegisterARM64.CV_ARM64_W20: "w20",
    RegisterARM64.CV_ARM64_W21: "w21",
    RegisterARM64.CV_ARM64_W22: "w22",
    RegisterARM64.CV_ARM64_W23: "w23",
    RegisterARM64.CV_ARM64_W24: "w24",
    RegisterARM64.CV_ARM64_W25: "w25",
    RegisterARM64.CV_ARM64_W26: "w26",
    RegisterARM64.CV_ARM64_W27: "w27",
    RegisterARM64.CV_ARM64_W28: "w28",
    RegisterARM64.CV_ARM64_W29: "w29",
    RegisterARM64.CV_ARM64_W30: "w30",
    RegisterARM64.CV_ARM64_WZR: "wzr",
    RegisterARM64.CV_ARM64_X0:  "x0",
    RegisterARM64.CV_ARM64_X1:  "x1",
    RegisterARM64.CV_ARM64_X2:  "x2",
    RegisterARM64.CV_ARM64_X3:  "x3",
    RegisterARM64.CV_ARM64_X4:  "x4",
    RegisterARM64.CV_ARM64_X5:  "x5",
    RegisterARM64.CV_ARM64_X6:  "x6",
    RegisterARM64.CV_ARM64_X7:  "x7",
    RegisterARM64.CV_ARM64_X8:  "x8",
    RegisterARM64.CV_ARM64_X9:  "x9",
    RegisterARM64.CV_ARM64_X10:  "x10",
    RegisterARM64.CV_ARM64_X11:  "x11",
    RegisterARM64.CV_ARM64_X12:  "x12",
    RegisterARM64.CV_ARM64_X13:  "x13",
    RegisterARM64.CV_ARM64_X14:  "x14",
    RegisterARM64.CV_ARM64_X15:  "x15",
    RegisterARM64.CV_ARM64_IP0:  "ip0",
    RegisterARM64.CV_ARM64_IP1:  "ip1",
    RegisterARM64.CV_ARM64_X18:  "x18",
    RegisterARM64.CV_ARM64_X19:  "x19",
    RegisterARM64.CV_ARM64_X20:  "x20",
    RegisterARM64.CV_ARM64_X21:  "x21",
    RegisterARM64.CV_ARM64_X22:  "x22",
    RegisterARM64.CV_ARM64_X23:  "x23",
    RegisterARM64.CV_ARM64_X24:  "x24",
    RegisterARM64.CV_ARM64_X25:  "x25",
    RegisterARM64.CV_ARM64_X26:  "x26",
    RegisterARM64.CV_ARM64_X27:  "x27",
    RegisterARM64.CV_ARM64_X28:  "x28",
    RegisterARM64.CV_ARM64_FP: "fp",
    RegisterARM64.CV_ARM64_LR: "lr",
    RegisterARM64.CV_ARM64_SP: "sp",
    RegisterARM64.CV_ARM64_ZR: "zr",
    RegisterARM64.CV_ARM64_NZCV: "nzcv",
    RegisterARM64.CV_ARM64_S0: "s0",
    RegisterARM64.CV_ARM64_S1: "s1",
    RegisterARM64.CV_ARM64_S2: "s2",
    RegisterARM64.CV_ARM64_S3: "s3",
    RegisterARM64.CV_ARM64_S4: "s4",
    RegisterARM64.CV_ARM64_S5: "s5",
    RegisterARM64.CV_ARM64_S6: "s6",
    RegisterARM64.CV_ARM64_S7: "s7",
    RegisterARM64.CV_ARM64_S8: "s8",
    RegisterARM64.CV_ARM64_S9: "s9",
    RegisterARM64.CV_ARM64_S10: "s10",
    RegisterARM64.CV_ARM64_S11: "s11",
    RegisterARM64.CV_ARM64_S12: "s12",
    RegisterARM64.CV_ARM64_S13: "s13",
    RegisterARM64.CV_ARM64_S14: "s14",
    RegisterARM64.CV_ARM64_S15: "s15",
    RegisterARM64.CV_ARM64_S16: "s16",
    RegisterARM64.CV_ARM64_S17: "s17",
    RegisterARM64.CV_ARM64_S18: "s18",
    RegisterARM64.CV_ARM64_S19: "s19",
    RegisterARM64.CV_ARM64_S20: "s20",
    RegisterARM64.CV_ARM64_S21: "s21",
    RegisterARM64.CV_ARM64_S22: "s22",
    RegisterARM64.CV_ARM64_S23: "s23",
    RegisterARM64.CV_ARM64_S24: "s24",
    RegisterARM64.CV_ARM64_S25: "s25",
    RegisterARM64.CV_ARM64_S26: "s26",
    RegisterARM64.CV_ARM64_S27: "s27",
    RegisterARM64.CV_ARM64_S28: "s28",
    RegisterARM64.CV_ARM64_S29: "s29",
    RegisterARM64.CV_ARM64_S30: "s30",
    RegisterARM64.CV_ARM64_S31: "s31",
    RegisterARM64.CV_ARM64_D0: "d0",
    RegisterARM64.CV_ARM64_D1: "d1",
    RegisterARM64.CV_ARM64_D2: "d2",
    RegisterARM64.CV_ARM64_D3: "d3",
    RegisterARM64.CV_ARM64_D4: "d4",
    RegisterARM64.CV_ARM64_D5: "d5",
    RegisterARM64.CV_ARM64_D6: "d6",
    RegisterARM64.CV_ARM64_D7: "d7",
    RegisterARM64.CV_ARM64_D8: "d8",
    RegisterARM64.CV_ARM64_D9: "d9",
    RegisterARM64.CV_ARM64_D10: "d10",
    RegisterARM64.CV_ARM64_D11: "d11",
    RegisterARM64.CV_ARM64_D12: "d12",
    RegisterARM64.CV_ARM64_D13: "d13",
    RegisterARM64.CV_ARM64_D14: "d14",
    RegisterARM64.CV_ARM64_D15: "d15",
    RegisterARM64.CV_ARM64_D16: "d16",
    RegisterARM64.CV_ARM64_D17: "d17",
    RegisterARM64.CV_ARM64_D18: "d18",
    RegisterARM64.CV_ARM64_D19: "d19",
    RegisterARM64.CV_ARM64_D20: "d20",
    RegisterARM64.CV_ARM64_D21: "d21",
    RegisterARM64.CV_ARM64_D22: "d22",
    RegisterARM64.CV_ARM64_D23: "d23",
    RegisterARM64.CV_ARM64_D24: "d24",
    RegisterARM64.CV_ARM64_D25: "d25",
    RegisterARM64.CV_ARM64_D26: "d26",
    RegisterARM64.CV_ARM64_D27: "d27",
    RegisterARM64.CV_ARM64_D28: "d28",
    RegisterARM64.CV_ARM64_D29: "d29",
    RegisterARM64.CV_ARM64_D30: "d30",
    RegisterARM64.CV_ARM64_D31: "d31",
    RegisterARM64.CV_ARM64_Q0: "q0",
    RegisterARM64.CV_ARM64_Q1: "q1",
    RegisterARM64.CV_ARM64_Q2: "q2",
    RegisterARM64.CV_ARM64_Q3: "q3",
    RegisterARM64.CV_ARM64_Q4: "q4",
    RegisterARM64.CV_ARM64_Q5: "q5",
    RegisterARM64.CV_ARM64_Q6: "q6",
    RegisterARM64.CV_ARM64_Q7: "q7",
    RegisterARM64.CV_ARM64_Q8: "q8",
    RegisterARM64.CV_ARM64_Q9: "q9",
    RegisterARM64.CV_ARM64_Q10: "q10",
    RegisterARM64.CV_ARM64_Q11: "q11",
    RegisterARM64.CV_ARM64_Q12: "q12",
    RegisterARM64.CV_ARM64_Q13: "q13",
    RegisterARM64.CV_ARM64_Q14: "q14",
    RegisterARM64.CV_ARM64_Q15: "q15",
    RegisterARM64.CV_ARM64_Q16: "q16",
    RegisterARM64.CV_ARM64_Q17: "q17",
    RegisterARM64.CV_ARM64_Q18: "q18",
    RegisterARM64.CV_ARM64_Q19: "q19",
    RegisterARM64.CV_ARM64_Q20: "q20",
    RegisterARM64.CV_ARM64_Q21: "q21",
    RegisterARM64.CV_ARM64_Q22: "q22",
    RegisterARM64.CV_ARM64_Q23: "q23",
    RegisterARM64.CV_ARM64_Q24: "q24",
    RegisterARM64.CV_ARM64_Q25: "q25",
    RegisterARM64.CV_ARM64_Q26: "q26",
    RegisterARM64.CV_ARM64_Q27: "q27",
    RegisterARM64.CV_ARM64_Q28: "q28",
    RegisterARM64.CV_ARM64_Q29: "q29",
    RegisterARM64.CV_ARM64_Q30: "q30",
    RegisterARM64.CV_ARM64_Q31: "q31",
    RegisterARM64.CV_ARM64_FPSR: "fpsr",
}


X86_REG_TO_NAME: dict[RegisterX86, str] = {
    RegisterX86.CV_REG_NONE: "None",
    RegisterX86.CV_REG_AL: "al",
    RegisterX86.CV_REG_CL: "cl",
    RegisterX86.CV_REG_DL: "dl",
    RegisterX86.CV_REG_BL: "bl",
    RegisterX86.CV_REG_AH: "ah",
    RegisterX86.CV_REG_CH: "ch",
    RegisterX86.CV_REG_DH: "dh",
    RegisterX86.CV_REG_BH: "bh",
    RegisterX86.CV_REG_AX: "ax",
    RegisterX86.CV_REG_CX: "cx",
    RegisterX86.CV_REG_DX: "dx",
    RegisterX86.CV_REG_BX: "bx",
    RegisterX86.CV_REG_SP: "sp",
    RegisterX86.CV_REG_BP: "bp",
    RegisterX86.CV_REG_SI: "si",
    RegisterX86.CV_REG_DI: "di",
    RegisterX86.CV_REG_EAX: "eax",
    RegisterX86.CV_REG_ECX: "ecx",
    RegisterX86.CV_REG_EDX: "edx",
    RegisterX86.CV_REG_EBX: "ebx",
    RegisterX86.CV_REG_ESP: "esp",
    RegisterX86.CV_REG_EBP: "ebp",
    RegisterX86.CV_REG_ESI: "esi",
    RegisterX86.CV_REG_EDI: "edi",
    RegisterX86.CV_REG_ES: "es",
    RegisterX86.CV_REG_CS: "cs",
    RegisterX86.CV_REG_SS: "ss",
    RegisterX86.CV_REG_DS: "ds",
    RegisterX86.CV_REG_FS: "fs",
    RegisterX86.CV_REG_GS: "gs",
    RegisterX86.CV_REG_IP: "ip",
    RegisterX86.CV_REG_FLAGS: "flags",
    RegisterX86.CV_REG_EIP: "eip",
    RegisterX86.CV_REG_EFLAGS: "eflags",
    RegisterX86.CV_REG_TEMP: "temp",
    RegisterX86.CV_REG_TEMPH: "temph",
    RegisterX86.CV_REG_QUOTE: "quote",
    RegisterX86.CV_REG_PCDR3: "pcdr3",
    RegisterX86.CV_REG_PCDR4: "pcdr4",
    RegisterX86.CV_REG_PCDR5: "pcdr5",
    RegisterX86.CV_REG_PCDR6: "pcdr6",
    RegisterX86.CV_REG_PCDR7: "pcdr7",
    RegisterX86.CV_REG_CR0: "cr0",
    RegisterX86.CV_REG_CR1: "cr1",
    RegisterX86.CV_REG_CR2: "cr2",
    RegisterX86.CV_REG_CR3: "cr3",
    RegisterX86.CV_REG_CR4: "cr4",
    RegisterX86.CV_REG_DR0: "dr0",
    RegisterX86.CV_REG_DR1: "dr1",
    RegisterX86.CV_REG_DR2: "dr2",
    RegisterX86.CV_REG_DR3: "dr3",
    RegisterX86.CV_REG_DR4: "dr4",
    RegisterX86.CV_REG_DR5: "dr5",
    RegisterX86.CV_REG_DR6: "dr6",
    RegisterX86.CV_REG_DR7: "dr7",
    RegisterX86.CV_REG_GDTR: "gdtr",
    RegisterX86.CV_REG_GDTL: "gdtl",
    RegisterX86.CV_REG_IDTR: "idtr",
    RegisterX86.CV_REG_IDTL: "idtl",
    RegisterX86.CV_REG_LDTR: "ldtr",
    RegisterX86.CV_REG_TR: "tr",
    RegisterX86.CV_REG_ST0: "st(0)",
    RegisterX86.CV_REG_ST1: "st(1)",
    RegisterX86.CV_REG_ST2: "st(2)",
    RegisterX86.CV_REG_ST3: "st(3)",
    RegisterX86.CV_REG_ST4: "st(4)",
    RegisterX86.CV_REG_ST5: "st(5)",
    RegisterX86.CV_REG_ST6: "st(6)",
    RegisterX86.CV_REG_ST7: "st(7)",
    RegisterX86.CV_REG_CTRL: "ctrl",
    RegisterX86.CV_REG_STAT: "stat",
    RegisterX86.CV_REG_TAG: "tag",
    RegisterX86.CV_REG_FPIP: "fpip",
    RegisterX86.CV_REG_FPCS: "fpcs",
    RegisterX86.CV_REG_FPDO: "fpdo",
    RegisterX86.CV_REG_FPDS: "fpds",
    RegisterX86.CV_REG_ISEM: "isem",
    RegisterX86.CV_REG_FPEIP: "fpeip",
    RegisterX86.CV_REG_FPEDO: "fped0",
}

AMD64_REG_TO_NAME: dict[RegisterAMD64, str] = {
    RegisterAMD64.CV_REG_NONE: "None",
    RegisterAMD64.CV_AMD64_AL: "al",
    RegisterAMD64.CV_AMD64_CL: "cl",
    RegisterAMD64.CV_AMD64_DL: "dl",
    RegisterAMD64.CV_AMD64_BL: "bl",
    RegisterAMD64.CV_AMD64_AH: "ah",
    RegisterAMD64.CV_AMD64_CH: "ch",
    RegisterAMD64.CV_AMD64_DH: "dh",
    RegisterAMD64.CV_AMD64_BH: "bh",
    RegisterAMD64.CV_AMD64_AX: "ax",
    RegisterAMD64.CV_AMD64_CX: "cx",
    RegisterAMD64.CV_AMD64_DX: "dx",
    RegisterAMD64.CV_AMD64_BX: "bx",
    RegisterAMD64.CV_AMD64_SP: "sp",
    RegisterAMD64.CV_AMD64_BP: "bp",
    RegisterAMD64.CV_AMD64_SI: "si",
    RegisterAMD64.CV_AMD64_DI: "di",
    RegisterAMD64.CV_AMD64_EAX: "eax",
    RegisterAMD64.CV_AMD64_ECX: "ecx",
    RegisterAMD64.CV_AMD64_EDX: "edx",
    RegisterAMD64.CV_AMD64_EBX: "ebx",
    RegisterAMD64.CV_AMD64_ESP: "esp",
    RegisterAMD64.CV_AMD64_EBP: "ebp",
    RegisterAMD64.CV_AMD64_ESI: "esi",
    RegisterAMD64.CV_AMD64_EDI: "edi",
    RegisterAMD64.CV_AMD64_ES: "es",
    RegisterAMD64.CV_AMD64_CS: "cs",
    RegisterAMD64.CV_AMD64_SS: "ss",
    RegisterAMD64.CV_AMD64_DS: "ds",
    RegisterAMD64.CV_AMD64_FS: "fs",
    RegisterAMD64.CV_AMD64_GS: "gs",
    RegisterAMD64.CV_AMD64_FLAGS: "flags",
    RegisterAMD64.CV_AMD64_RIP: "rip",
    RegisterAMD64.CV_AMD64_EFLAGS: "eflags",
    RegisterAMD64.CV_AMD64_CR0: "cr0",
    RegisterAMD64.CV_AMD64_CR1: "cr1",
    RegisterAMD64.CV_AMD64_CR2: "cr2",
    RegisterAMD64.CV_AMD64_CR3: "cr3",
    RegisterAMD64.CV_AMD64_CR4: "cr4",
    RegisterAMD64.CV_AMD64_CR8: "cr8",
    RegisterAMD64.CV_AMD64_DR0: "dr0",
    RegisterAMD64.CV_AMD64_DR1: "dr1",
    RegisterAMD64.CV_AMD64_DR2: "dr2",
    RegisterAMD64.CV_AMD64_DR3: "dr3",
    RegisterAMD64.CV_AMD64_DR4: "dr4",
    RegisterAMD64.CV_AMD64_DR5: "dr5",
    RegisterAMD64.CV_AMD64_DR6: "dr6",
    RegisterAMD64.CV_AMD64_DR7: "dr7",
    RegisterAMD64.CV_AMD64_DR8: "dr8",
    RegisterAMD64.CV_AMD64_DR9: "dr9",
    RegisterAMD64.CV_AMD64_DR10: "dr10",
    RegisterAMD64.CV_AMD64_DR11: "dr11",
    RegisterAMD64.CV_AMD64_DR12: "dr12",
    RegisterAMD64.CV_AMD64_DR13: "dr13",
    RegisterAMD64.CV_AMD64_DR14: "dr14",
    RegisterAMD64.CV_AMD64_DR15: "dr15",
    RegisterAMD64.CV_AMD64_GDTR: "gdtr",
    RegisterAMD64.CV_AMD64_GDTL: "gdtl",
    RegisterAMD64.CV_AMD64_IDTR: "idtr",
    RegisterAMD64.CV_AMD64_IDTL: "idtl",
    RegisterAMD64.CV_AMD64_LDTR: "ldtr",
    RegisterAMD64.CV_AMD64_TR: "tr",
    RegisterAMD64.CV_AMD64_ST0: "st(0)",
    RegisterAMD64.CV_AMD64_ST1: "st(1)",
    RegisterAMD64.CV_AMD64_ST2: "st(2)",
    RegisterAMD64.CV_AMD64_ST3: "st(3)",
    RegisterAMD64.CV_AMD64_ST4: "st(4)",
    RegisterAMD64.CV_AMD64_ST5: "st(5)",
    RegisterAMD64.CV_AMD64_ST6: "st(6)",
    RegisterAMD64.CV_AMD64_ST7: "st(7)",
    RegisterAMD64.CV_AMD64_CTRL: "ctrl",
    RegisterAMD64.CV_AMD64_STAT: "stat",
    RegisterAMD64.CV_AMD64_TAG: "tag",
    RegisterAMD64.CV_AMD64_FPIP: "fpip",
    RegisterAMD64.CV_AMD64_FPCS: "fpcs",
    RegisterAMD64.CV_AMD64_FPDO: "fpdo",
    RegisterAMD64.CV_AMD64_FPDS: "fpds",
    RegisterAMD64.CV_AMD64_ISEM: "isem",
    RegisterAMD64.CV_AMD64_FPEIP: "fpeip",
    RegisterAMD64.CV_AMD64_FPEDO: "fped0",
    RegisterAMD64.CV_AMD64_MM0: "mm0",
    RegisterAMD64.CV_AMD64_MM1: "mm1",
    RegisterAMD64.CV_AMD64_MM2: "mm2",
    RegisterAMD64.CV_AMD64_MM3: "mm3",
    RegisterAMD64.CV_AMD64_MM4: "mm4",
    RegisterAMD64.CV_AMD64_MM5: "mm5",
    RegisterAMD64.CV_AMD64_MM6: "mm6",
    RegisterAMD64.CV_AMD64_MM7: "mm7",
    RegisterAMD64.CV_AMD64_XMM0: "xmm0",
    RegisterAMD64.CV_AMD64_XMM1: "xmm1",
    RegisterAMD64.CV_AMD64_XMM2: "xmm2",
    RegisterAMD64.CV_AMD64_XMM3: "xmm3",
    RegisterAMD64.CV_AMD64_XMM4: "xmm4",
    RegisterAMD64.CV_AMD64_XMM5: "xmm5",
    RegisterAMD64.CV_AMD64_XMM6: "xmm6",
    RegisterAMD64.CV_AMD64_XMM7: "xmm7",
    RegisterAMD64.CV_AMD64_XMM0_0: "xmm0_0",
    RegisterAMD64.CV_AMD64_XMM0_1: "xmm0_1",
    RegisterAMD64.CV_AMD64_XMM0_2: "xmm0_2",
    RegisterAMD64.CV_AMD64_XMM0_3: "xmm0_3",
    RegisterAMD64.CV_AMD64_XMM1_0: "xmm1_0",
    RegisterAMD64.CV_AMD64_XMM1_1: "xmm1_1",
    RegisterAMD64.CV_AMD64_XMM1_2: "xmm1_2",
    RegisterAMD64.CV_AMD64_XMM1_3: "xmm1_3",
    RegisterAMD64.CV_AMD64_XMM2_0: "xmm2_0",
    RegisterAMD64.CV_AMD64_XMM2_1: "xmm2_1",
    RegisterAMD64.CV_AMD64_XMM2_2: "xmm2_2",
    RegisterAMD64.CV_AMD64_XMM2_3: "xmm2_3",
    RegisterAMD64.CV_AMD64_XMM3_0: "xmm3_0",
    RegisterAMD64.CV_AMD64_XMM3_1: "xmm3_1",
    RegisterAMD64.CV_AMD64_XMM3_2: "xmm3_2",
    RegisterAMD64.CV_AMD64_XMM3_3: "xmm3_3",
    RegisterAMD64.CV_AMD64_XMM4_0: "xmm4_0",
    RegisterAMD64.CV_AMD64_XMM4_1: "xmm4_1",
    RegisterAMD64.CV_AMD64_XMM4_2: "xmm4_2",
    RegisterAMD64.CV_AMD64_XMM4_3: "xmm4_3",
    RegisterAMD64.CV_AMD64_XMM5_0: "xmm5_0",
    RegisterAMD64.CV_AMD64_XMM5_1: "xmm5_1",
    RegisterAMD64.CV_AMD64_XMM5_2: "xmm5_2",
    RegisterAMD64.CV_AMD64_XMM5_3: "xmm5_3",
    RegisterAMD64.CV_AMD64_XMM6_0: "xmm6_0",
    RegisterAMD64.CV_AMD64_XMM6_1: "xmm6_1",
    RegisterAMD64.CV_AMD64_XMM6_2: "xmm6_2",
    RegisterAMD64.CV_AMD64_XMM6_3: "xmm6_3",
    RegisterAMD64.CV_AMD64_XMM7_0: "xmm7_0",
    RegisterAMD64.CV_AMD64_XMM7_1: "xmm7_1",
    RegisterAMD64.CV_AMD64_XMM7_2: "xmm7_2",
    RegisterAMD64.CV_AMD64_XMM7_3: "xmm7_3",
    RegisterAMD64.CV_AMD64_XMM0L: "xmm0l",
    RegisterAMD64.CV_AMD64_XMM1L: "xmm1l",
    RegisterAMD64.CV_AMD64_XMM2L: "xmm2l",
    RegisterAMD64.CV_AMD64_XMM3L: "xmm3l",
    RegisterAMD64.CV_AMD64_XMM4L: "xmm4l",
    RegisterAMD64.CV_AMD64_XMM5L: "xmm5l",
    RegisterAMD64.CV_AMD64_XMM6L: "xmm6l",
    RegisterAMD64.CV_AMD64_XMM7L: "xmm7l",
    RegisterAMD64.CV_AMD64_XMM0H: "xmm0h",
    RegisterAMD64.CV_AMD64_XMM1H: "xmm1h",
    RegisterAMD64.CV_AMD64_XMM2H: "xmm2h",
    RegisterAMD64.CV_AMD64_XMM3H: "xmm3h",
    RegisterAMD64.CV_AMD64_XMM4H: "xmm4h",
    RegisterAMD64.CV_AMD64_XMM5H: "xmm5h",
    RegisterAMD64.CV_AMD64_XMM6H: "xmm6h",
    RegisterAMD64.CV_AMD64_XMM7H: "xmm7h",
    RegisterAMD64.CV_AMD64_MXCSR: "mxcsr",
    RegisterAMD64.CV_AMD64_EMM0L: "emm0l",
    RegisterAMD64.CV_AMD64_EMM1L: "emm1l",
    RegisterAMD64.CV_AMD64_EMM2L: "emm2l",
    RegisterAMD64.CV_AMD64_EMM3L: "emm3l",
    RegisterAMD64.CV_AMD64_EMM4L: "emm4l",
    RegisterAMD64.CV_AMD64_EMM5L: "emm5l",
    RegisterAMD64.CV_AMD64_EMM6L: "emm6l",
    RegisterAMD64.CV_AMD64_EMM7L: "emm7l",
    RegisterAMD64.CV_AMD64_EMM0H: "emm0h",
    RegisterAMD64.CV_AMD64_EMM1H: "emm1h",
    RegisterAMD64.CV_AMD64_EMM2H: "emm2h",
    RegisterAMD64.CV_AMD64_EMM3H: "emm3h",
    RegisterAMD64.CV_AMD64_EMM4H: "emm4h",
    RegisterAMD64.CV_AMD64_EMM5H: "emm5h",
    RegisterAMD64.CV_AMD64_EMM6H: "emm6h",
    RegisterAMD64.CV_AMD64_EMM7H: "emm7h",
    RegisterAMD64.CV_AMD64_MM00: "mm00",
    RegisterAMD64.CV_AMD64_MM01: "mm01",
    RegisterAMD64.CV_AMD64_MM10: "mm10",
    RegisterAMD64.CV_AMD64_MM11: "mm11",
    RegisterAMD64.CV_AMD64_MM20: "mm20",
    RegisterAMD64.CV_AMD64_MM21: "mm21",
    RegisterAMD64.CV_AMD64_MM30: "mm30",
    RegisterAMD64.CV_AMD64_MM31: "mm31",
    RegisterAMD64.CV_AMD64_MM40: "mm40",
    RegisterAMD64.CV_AMD64_MM41: "mm41",
    RegisterAMD64.CV_AMD64_MM50: "mm50",
    RegisterAMD64.CV_AMD64_MM51: "mm51",
    RegisterAMD64.CV_AMD64_MM60: "mm60",
    RegisterAMD64.CV_AMD64_MM61: "mm61",
    RegisterAMD64.CV_AMD64_MM70: "mm70",
    RegisterAMD64.CV_AMD64_MM71: "mm71",
    RegisterAMD64.CV_AMD64_XMM8: "xmm8",
    RegisterAMD64.CV_AMD64_XMM9: "xmm9",
    RegisterAMD64.CV_AMD64_XMM10: "xmm10",
    RegisterAMD64.CV_AMD64_XMM11: "xmm11",
    RegisterAMD64.CV_AMD64_XMM12: "xmm12",
    RegisterAMD64.CV_AMD64_XMM13: "xmm13",
    RegisterAMD64.CV_AMD64_XMM14: "xmm14",
    RegisterAMD64.CV_AMD64_XMM15: "xmm15",
    RegisterAMD64.CV_AMD64_XMM8_0: "xmm8_0",
    RegisterAMD64.CV_AMD64_XMM8_1: "xmm8_1",
    RegisterAMD64.CV_AMD64_XMM8_2: "xmm8_2",
    RegisterAMD64.CV_AMD64_XMM8_3: "xmm8_3",
    RegisterAMD64.CV_AMD64_XMM9_0: "xmm9_0",
    RegisterAMD64.CV_AMD64_XMM9_1: "xmm9_1",
    RegisterAMD64.CV_AMD64_XMM9_2: "xmm9_2",
    RegisterAMD64.CV_AMD64_XMM9_3: "xmm9_3",
    RegisterAMD64.CV_AMD64_XMM10_0: "xmm10_0",
    RegisterAMD64.CV_AMD64_XMM10_1: "xmm10_1",
    RegisterAMD64.CV_AMD64_XMM10_2: "xmm10_2",
    RegisterAMD64.CV_AMD64_XMM10_3: "xmm10_3",
    RegisterAMD64.CV_AMD64_XMM11_0: "xmm11_0",
    RegisterAMD64.CV_AMD64_XMM11_1: "xmm11_1",
    RegisterAMD64.CV_AMD64_XMM11_2: "xmm11_2",
    RegisterAMD64.CV_AMD64_XMM11_3: "xmm11_3",
    RegisterAMD64.CV_AMD64_XMM12_0: "xmm12_0",
    RegisterAMD64.CV_AMD64_XMM12_1: "xmm12_1",
    RegisterAMD64.CV_AMD64_XMM12_2: "xmm12_2",
    RegisterAMD64.CV_AMD64_XMM12_3: "xmm12_3",
    RegisterAMD64.CV_AMD64_XMM13_0: "xmm13_0",
    RegisterAMD64.CV_AMD64_XMM13_1: "xmm13_1",
    RegisterAMD64.CV_AMD64_XMM13_2: "xmm13_2",
    RegisterAMD64.CV_AMD64_XMM13_3: "xmm13_3",
    RegisterAMD64.CV_AMD64_XMM14_0: "xmm14_0",
    RegisterAMD64.CV_AMD64_XMM14_1: "xmm14_1",
    RegisterAMD64.CV_AMD64_XMM14_2: "xmm14_2",
    RegisterAMD64.CV_AMD64_XMM14_3: "xmm14_3",
    RegisterAMD64.CV_AMD64_XMM15_0: "xmm15_0",
    RegisterAMD64.CV_AMD64_XMM15_1: "xmm15_1",
    RegisterAMD64.CV_AMD64_XMM15_2: "xmm15_2",
    RegisterAMD64.CV_AMD64_XMM15_3: "xmm15_3",
    RegisterAMD64.CV_AMD64_XMM8L: "xmm8l",
    RegisterAMD64.CV_AMD64_XMM9L: "xmm9l",
    RegisterAMD64.CV_AMD64_XMM10L: "xmm10l",
    RegisterAMD64.CV_AMD64_XMM11L: "xmm11l",
    RegisterAMD64.CV_AMD64_XMM12L: "xmm12l",
    RegisterAMD64.CV_AMD64_XMM13L: "xmm13l",
    RegisterAMD64.CV_AMD64_XMM14L: "xmm14l",
    RegisterAMD64.CV_AMD64_XMM15L: "xmm15l",
    RegisterAMD64.CV_AMD64_XMM8H: "xmm8h",
    RegisterAMD64.CV_AMD64_XMM9H: "xmm9h",
    RegisterAMD64.CV_AMD64_XMM10H: "xmm10h",
    RegisterAMD64.CV_AMD64_XMM11H: "xmm11h",
    RegisterAMD64.CV_AMD64_XMM12H: "xmm12h",
    RegisterAMD64.CV_AMD64_XMM13H: "xmm13h",
    RegisterAMD64.CV_AMD64_XMM14H: "xmm14h",
    RegisterAMD64.CV_AMD64_XMM15H: "xmm15h",
    RegisterAMD64.CV_AMD64_EMM8L: "emm8l",
    RegisterAMD64.CV_AMD64_EMM9L: "emm9l",
    RegisterAMD64.CV_AMD64_EMM10L: "emm10l",
    RegisterAMD64.CV_AMD64_EMM11L: "emm11l",
    RegisterAMD64.CV_AMD64_EMM12L: "emm12l",
    RegisterAMD64.CV_AMD64_EMM13L: "emm13l",
    RegisterAMD64.CV_AMD64_EMM14L: "emm14l",
    RegisterAMD64.CV_AMD64_EMM15L: "emm15l",
    RegisterAMD64.CV_AMD64_EMM8H: "emm8h",
    RegisterAMD64.CV_AMD64_EMM9H: "emm9h",
    RegisterAMD64.CV_AMD64_EMM10H: "emm10h",
    RegisterAMD64.CV_AMD64_EMM11H: "emm11h",
    RegisterAMD64.CV_AMD64_EMM12H: "emm12h",
    RegisterAMD64.CV_AMD64_EMM13H: "emm13h",
    RegisterAMD64.CV_AMD64_EMM14H: "emm14h",
    RegisterAMD64.CV_AMD64_EMM15H: "emm15h",
    RegisterAMD64.CV_AMD64_SIL: "sil",
    RegisterAMD64.CV_AMD64_DIL: "dil",
    RegisterAMD64.CV_AMD64_BPL: "bpl",
    RegisterAMD64.CV_AMD64_SPL: "spl",
    RegisterAMD64.CV_AMD64_RAX: "rax",
    RegisterAMD64.CV_AMD64_RBX: "rbx",
    RegisterAMD64.CV_AMD64_RCX: "rcx",
    RegisterAMD64.CV_AMD64_RDX: "rdx",
    RegisterAMD64.CV_AMD64_RSI: "rsi",
    RegisterAMD64.CV_AMD64_RDI: "rdi",
    RegisterAMD64.CV_AMD64_RBP: "rbp",
    RegisterAMD64.CV_AMD64_RSP: "rsp",
    RegisterAMD64.CV_AMD64_R8: "r8",
    RegisterAMD64.CV_AMD64_R9: "r9",
    RegisterAMD64.CV_AMD64_R10: "r10",
    RegisterAMD64.CV_AMD64_R11: "r11",
    RegisterAMD64.CV_AMD64_R12: "r12",
    RegisterAMD64.CV_AMD64_R13: "r13",
    RegisterAMD64.CV_AMD64_R14: "r14",
    RegisterAMD64.CV_AMD64_R15: "r15",
    RegisterAMD64.CV_AMD64_R8B: "r8b",
    RegisterAMD64.CV_AMD64_R9B: "r9b",
    RegisterAMD64.CV_AMD64_R10B: "r10b",
    RegisterAMD64.CV_AMD64_R11B: "r11b",
    RegisterAMD64.CV_AMD64_R12B: "r12b",
    RegisterAMD64.CV_AMD64_R13B: "r13b",
    RegisterAMD64.CV_AMD64_R14B: "r14b",
    RegisterAMD64.CV_AMD64_R15B: "r15b",
    RegisterAMD64.CV_AMD64_R8W: "r8w",
    RegisterAMD64.CV_AMD64_R9W: "r9w",
    RegisterAMD64.CV_AMD64_R10W: "r10w",
    RegisterAMD64.CV_AMD64_R11W: "r11w",
    RegisterAMD64.CV_AMD64_R12W: "r12w",
    RegisterAMD64.CV_AMD64_R13W: "r13w",
    RegisterAMD64.CV_AMD64_R14W: "r14w",
    RegisterAMD64.CV_AMD64_R15W: "r15w",
    RegisterAMD64.CV_AMD64_R8D: "r8d",
    RegisterAMD64.CV_AMD64_R9D: "r9d",
    RegisterAMD64.CV_AMD64_R10D: "r10d",
    RegisterAMD64.CV_AMD64_R11D: "r11d",
    RegisterAMD64.CV_AMD64_R12D: "r12d",
    RegisterAMD64.CV_AMD64_R13D: "r13d",
    RegisterAMD64.CV_AMD64_R14D: "r14d",
    RegisterAMD64.CV_AMD64_R15D: "r15d",
}

def get_c7_register_name(register: int, machine: Machine):
    cpu = MACHINE_TO_CPU[machine]
    try:
        match cpu:
            case CpuType.CV_CFL_8080 | CpuType.CV_CFL_8086 | CpuType.CV_CFL_80286 | CpuType.CV_CFL_80386 | CpuType.CV_CFL_80486 | CpuType.CV_CFL_PENTIUM | CpuType.CV_CFL_PENTIUMII | CpuType.CV_CFL_PENTIUMIII:
                cv_reg = RegisterX86(register)
                reg_lookup = X86_REG_TO_NAME
            case CpuType.CV_CFL_ALPHA | CpuType.CV_CFL_ALPHA_21164 | CpuType.CV_CFL_ALPHA_21164A | CpuType.CV_CFL_ALPHA_21264 | CpuType.CV_CFL_ALPHA_21364:
                reg_lookup = REGISTER_NAMES_ALPHA
            case CpuType.CV_CFL_MIPS | CpuType.CV_CFL_MIPS16 | CpuType.CV_CFL_MIPS32 | CpuType.CV_CFL_MIPS64 | CpuType.CV_CFL_MIPSI | CpuType.CV_CFL_MIPSII | CpuType.CV_CFL_MIPSIII | CpuType.CV_CFL_MIPSIV | CpuType.CV_CFL_MIPSV:
                reg_lookup = REGISTER_NAMES_MIPS
            case CpuType.CV_CFL_M68000 | CpuType.CV_CFL_M68010 | CpuType.CV_CFL_M68020 | CpuType.CV_CFL_M68030 | CpuType.CV_CFL_M68040:
                reg_lookup = REGISTER_NAMES_MOTOROLA
            case CpuType.CV_CFL_PPC601 | CpuType.CV_CFL_PPC603 | CpuType.CV_CFL_PPC604 | CpuType.CV_CFL_PPC620 | CpuType.CV_CFL_PPCFP | CpuType.CV_CFL_PPCBE:
                reg_lookup = REGISTER_NAMES_PPC
            case CpuType.CV_CFL_SH3 | CpuType.CV_CFL_SH3E | CpuType.CV_CFL_SH3DSP | CpuType.CV_CFL_SH4:
                reg_lookup = REGISTER_NAMES_SH
            case CpuType.CV_CFL_ARM3 | CpuType.CV_CFL_ARM4 | CpuType.CV_CFL_ARM4T | CpuType.CV_CFL_ARM5 | CpuType.CV_CFL_ARM5T | CpuType.CV_CFL_ARM7 | CpuType.CV_CFL_THUMB | CpuType.CV_CFL_ARMNT:
                reg_lookup = REGISTER_NAMES_ARM
            case CpuType.CV_CFL_ARM64:
                cv_reg = RegisterARM64(register)
                reg_lookup = ARM64_REG_TO_NAME
            case CpuType.CV_CFL_IA64_1 | CpuType.CV_CFL_IA64_2:
                reg_lookup = REGISTER_NAMES_IA
            case CpuType.CV_CFL_AMD64:
                cv_reg = RegisterAMD64(register)
                reg_lookup = AMD64_REG_TO_NAME
    except ValueError:
        return f"???(0x{register:04X})"
    s = reg_lookup.get(cv_reg)
    if s is None:
        s = f"??? (0x{register:04x})"
    return s


MACHINE_I386_FRAME_REGISTERS = [
    RegisterX86.CV_REG_NONE,
    RegisterCommon.CV_ALLREG_VFRAME,
    RegisterX86.CV_REG_EBP,
    RegisterX86.CV_REG_EBX,
]

MACHINE_AMD64_FRAME_REGISTERS = [
    RegisterAMD64.CV_REG_NONE,
    RegisterAMD64.CV_AMD64_RSP,
    RegisterAMD64.CV_AMD64_RBP,
    RegisterAMD64.CV_AMD64_R13,
]

def get_frame_register_name(frame_register: int, machine_config: MachineConfig) -> str:
    # ExpandEncodedBasePointerReg (cvinfo.h)

    match machine_config.machine:
        case Machine.IMAGE_FILE_MACHINE_I386:
            register = MACHINE_I386_FRAME_REGISTERS[frame_register]
            return get_c7_register_name(register=register.value, machine=machine_config.machine)
        case Machine.IMAGE_FILE_MACHINE_AMD64:
            register = MACHINE_AMD64_FRAME_REGISTERS[frame_register]
            return get_c7_register_name(register=register.value, machine=machine_config.machine)
        case Machine.IMAGE_FILE_MACHINE_ARM64:
            # register = MACHINE_ARM64_FRAME_REGISTERS[frame_register]
            # return get_c7_register_name(register=register.value, machine=machine_config.machine)
            return f"???(0x{frame_register:X})"
        case _:
            raise ValueError

class BinaryAnnotationOpcode(enum.IntEnum):
    BA_OP_Invalid = 0
    BA_OP_CodeOffset = 1
    BA_OP_ChangeCodeOffsetBase = 2
    BA_OP_ChangeCodeOffset = 3
    BA_OP_ChangeCodeLength = 4
    BA_OP_ChangeFile = 5
    BA_OP_ChangeLineOffset = 6
    BA_OP_ChangeLineEndDelta = 7
    BA_OP_ChangeRangeKind = 8
    BA_OP_ChangeColumnStart = 9
    BA_OP_ChangeColumnEndDelta = 10
    BA_OP_ChangeCodeOffsetAndLineOffset = 11
    BA_OP_ChangeCodeLengthAndCodeOffset = 12
    BA_OP_ChangeColumnEnd = 13

BINARY_ANNOTATION_OPCODE_NAMES: dict[BinaryAnnotationOpcode, str] = {
    BinaryAnnotationOpcode.BA_OP_Invalid: "Illegal",
    BinaryAnnotationOpcode.BA_OP_CodeOffset: "Offset",
    BinaryAnnotationOpcode.BA_OP_ChangeCodeOffsetBase: "CodeOffsetBase",
    BinaryAnnotationOpcode.BA_OP_ChangeCodeOffset: "CodeOffset",
    BinaryAnnotationOpcode.BA_OP_ChangeCodeLength: "CodeLength",
    BinaryAnnotationOpcode.BA_OP_ChangeFile: "File",
    BinaryAnnotationOpcode.BA_OP_ChangeLineOffset: "LineOffset",
    BinaryAnnotationOpcode.BA_OP_ChangeLineEndDelta: "LineEndDelta",
    BinaryAnnotationOpcode.BA_OP_ChangeRangeKind: "RangeKind",
    BinaryAnnotationOpcode.BA_OP_ChangeColumnStart: "ColumnStart",
    BinaryAnnotationOpcode.BA_OP_ChangeColumnEndDelta: "ColumnEndDelta",
    BinaryAnnotationOpcode.BA_OP_ChangeCodeOffsetAndLineOffset: "CodeOffsetAndLineOffset",
    BinaryAnnotationOpcode.BA_OP_ChangeCodeLengthAndCodeOffset: "CodeLengthAndCodeOffset",
    BinaryAnnotationOpcode.BA_OP_ChangeColumnEnd: "ColumnEnd",
}

def get_binary_annotation_operand_count(operation: BinaryAnnotationOpcode) -> int:
    match operation:
        case BinaryAnnotationOpcode.BA_OP_ChangeCodeLengthAndCodeOffset:
            return 2
        case _:
            return 1


def decode_signed_int32(v: int) -> int:
    if v & 0x1:
        return -(v >> 1)
    else:
        return v >> 1


def print_c17_binary_annotations(annotations: list[int]):
    print("\tBinaryAnnotations:", end="")
    def decompress_data(index) -> tuple[int, int]:
        result = -1
        if annotations[index] & 0x80 == 0:
            return 1, annotations[index]
        if annotations[index] & 0xc0 == 0x80:
            return 2, (annotations[index] & 0x3f) << 8 | annotations[index + 1]
        if annotations[index] & 0xe0 == 0xc0:
            return 3, (annotations[index] & 0x1f) << 16 | annotations[index + 1] << 8 | annotations[index + 2]
        return 0, -1
    current_pos = 0
    count_printed = 0
    while current_pos < len(annotations):
        delta_pos, instruction = decompress_data(current_pos)
        current_pos += delta_pos
        if instruction == BinaryAnnotationOpcode.BA_OP_Invalid:
            current_pos -= 1
            break
        if count_printed == 4:
            count_printed = 0
            print()
            print("\t", end="")
        print(f"  {BINARY_ANNOTATION_OPCODE_NAMES.get(instruction, 'INVALID INSTRUCTION')}", end="")
        if current_pos >= len(annotations):
            print("ERROR: INVALID COMPRESSED BINARY ANNOTATIONS")
            return
        operand_count = get_binary_annotation_operand_count(instruction)
        for j in range(operand_count):
            delta_pos, parameter = decompress_data(current_pos)
            current_pos += delta_pos
            if parameter in (BinaryAnnotationOpcode.BA_OP_ChangeLineOffset, BinaryAnnotationOpcode.BA_OP_ChangeColumnEndDelta):
                parameter = decode_signed_int32(parameter)
            print(f" {parameter:x}", end="")
        count_printed += 1
    print()
    if current_pos >= len(annotations):
        print("INVALID POSITION")
    print(f"\tBinaryAnnotation Length: {len(annotations)} bytes ({len(annotations) - current_pos} bytes padding)")

class ThunkOrdinal(enum.IntEnum):
    THUNK_ORDINAL_NOTYPE = 0 # standard thunk
    THUNK_ORDINAL_ADJUSTOR = 1  # "this" adjustor thunk
    THUNK_ORDINAL_VCALL = 2     # virtual call thunk
    THUNK_ORDINAL_PCODE = 3     # pcode thunk
    THUNK_ORDINAL_LOAD = 4      # thunk which loads the address to jump to via unknown means...
    # trampoline thunk ordinals   - only for use in Trampoline thunk symbols
    THUNK_ORDINAL_TRAMP_INCREMENTAL = 5
    THUNK_ORDINAL_TRAMP_BRANCHISLAND = 6


class CookieType(enum.IntEnum):
   CV_COOKIETYPE_COPY = 0
   CV_COOKIETYPE_XOR_SP = 1
   CV_COOKIETYPE_XOR_BP = 2
   CV_COOKIETYPE_XOR_R13 = 3


def get_c7_cookie_type_name(cookietype: int) -> str:
    match cookietype:
        case CookieType.CV_COOKIETYPE_COPY:
            return "COPY"
        case CookieType.CV_COOKIETYPE_XOR_SP:
            return "XOR_SP"
        case CookieType.CV_COOKIETYPE_XOR_BP:
            return "XOR_BP"
        case CookieType.CV_COOKIETYPE_XOR_R13:
            return "XOR_R13"
        case _:
            return f"???(0x{cookietype:02X})"


def yes_no(v: int | bool) -> str:
    return "yes" if v else "no"


class CV_armswitchtype(enum.Enum):
    CV_SWT_INT1         = 0
    CV_SWT_UINT1        = 1
    CV_SWT_INT2         = 2
    CV_SWT_UINT2        = 3
    CV_SWT_INT4         = 4
    CV_SWT_UINT4        = 5
    CV_SWT_POINTER      = 6
    CV_SWT_UINT1SHL1    = 7
    CV_SWT_UINT2SHL1    = 8
    CV_SWT_INT1SHL1     = 9
    CV_SWT_INT2SHL1     = 10
    CV_SWT_TBB          = CV_SWT_UINT1SHL1
    CV_SWT_TBH          = CV_SWT_UINT2SHL1


def dump_symbol(symbol: ModiStream.Symbol, machine_config: MachineConfig, module_info, dump_pos: bool=True):
    try:
        symbol_type_name = symbol.record.type.name.upper()
    except AttributeError:
        raise ValueError(f"WARNING: Unknown record type: 0x{symbol.record.type:x})")
        # symbol_type_name = hex(symbol.record.type)
    if dump_pos:
        print(f"({symbol.pos:06X}) ", end="")
    print(f"{symbol_type_name}:", end="")
    match symbol.record.type:
        case CvSymbol.SymbolType.s_objname | CvSymbol.SymbolType.s_objname_st:
            print(f" Signature: {symbol.record.element.signature:08x}, {symbol.record.element.name.text}")
            print()
        case CvSymbol.SymbolType.s_compile:
            print()
            machine_config.set_machine(ProcessorToMachine(symbol.record.element.machine))
            print(f"\tLanguage: {GetLanguageIdString(symbol.record.element.language)}")
            print(f"\tTarget processor: {GetTargetProcessorString(symbol.record.element.machine)}")
            print(f"\tFloating-point precision: {(symbol.record.element.flags >> 1) & 0x3}")
            print(f"\tFloating-point package: {GetFloatingPointPackageName((symbol.record.element.flags >> 11) & 0x3)}")
            print(f"\tAmbient data: {GetAmbientDataType((symbol.record.element.flags >> 5) & 0x7)}")
            print(f"\tAmbient code: {GetAmbientDataType((symbol.record.element.flags >> 8) & 0x7)}")
            print(f"\tPCode present: {symbol.record.element.flags & 0x1}")
            print(f"\tCompiler version: {symbol.record.element.ver.text}")
        case CvSymbol.SymbolType.s_compile2 | CvSymbol.SymbolType.s_compile2_st:
            print()
            machine_config.set_machine(ProcessorToMachine(symbol.record.element.machine))
            print(f"\tLanguage: {GetLanguageIdString(symbol.record.element.flags & 0xff)}")
            print(f"\tTarget processor: {GetTargetProcessorString(symbol.record.element.machine)}")
            print(f"\tCompiled for edit and continue: {yes_no(symbol.record.element.flags & 0x100)}")
            print(f"\tCompiled without debugging info: {yes_no(symbol.record.element.flags & 0x200)}")
            print(f"\tCompiled with LTCG: {yes_no(symbol.record.element.flags & 0x400)}")
            print(f"\tCompiled with /bzalign: {yes_no(symbol.record.element.flags & 0x800)}")
            print(f"\tManaged code present: {yes_no(symbol.record.element.flags & 0x1000)}")
            print(f"\tCompiled with /GS: {yes_no(symbol.record.element.flags & 0x2000)}")
            print(f"\tCompiled with /hotpatch: {yes_no(symbol.record.element.flags & 0x4000)}")
            print(f"\tCompiled with CVTCIL: {yes_no(symbol.record.element.flags & 0x8000)}")
            print(f"\tMSIL module: {yes_no(symbol.record.element.flags & 0x10000)}")
            print(f"\tPad bits = 0x{symbol.record.element.flags >> 17}")
            print(f"\tFrontend Version: Major = {symbol.record.element.ver_fe_major}, Minor = {symbol.record.element.ver_fe_minor}, Build = {symbol.record.element.ver_fe_build}")
            print(f"\tBackend Version: Major = {symbol.record.element.ver_major}, Minor = {symbol.record.element.ver_minor}, Build = {symbol.record.element.ver_build}")
            print(f"\tVersion string: {symbol.record.element.ver_string.text}")
            print(f"\tCommand block:")
            for block in symbol.record.element.command_blocks[:-1]:
                print(f"\t\t{block.key} = '{block.value}'")
        case CvSymbol.SymbolType.s_compile3:
            print()
            machine_config.set_machine(ProcessorToMachine(symbol.record.element.machine))
            print(f"\tLanguage: {GetLanguageIdString(symbol.record.element.flags & 0xff)}")
            print(f"\tTarget processor: {GetTargetProcessorString(symbol.record.element.machine)}")
            print(f"\tCompiled for edit and continue: {yes_no(symbol.record.element.flags & 0x100)}")
            print(f"\tCompiled without debugging info: {yes_no(symbol.record.element.flags & 0x200)}")
            print(f"\tCompiled with LTCG: {yes_no(symbol.record.element.flags & 0x400)}")
            print(f"\tCompiled with /bzalign: {yes_no(symbol.record.element.flags & 0x800)}")
            print(f"\tManaged code present: {yes_no(symbol.record.element.flags & 0x1000)}")
            print(f"\tCompiled with /GS: {yes_no(symbol.record.element.flags & 0x2000)}")
            print(f"\tCompiled with /hotpatch: {yes_no(symbol.record.element.flags & 0x4000)}")
            print(f"\tCompiled with CVTCIL: {yes_no(symbol.record.element.flags & 0x8000)}")
            print(f"\tMSIL module: {yes_no(symbol.record.element.flags & 0x10000)}")
            print(f"\tCompiled with /sdl: {yes_no(symbol.record.element.flags & 0x20000)}")
            print(f"\tCompiled with pgo: {yes_no(symbol.record.element.flags & 0x40000)}")
            print(f"\t.EXP module: {yes_no(symbol.record.element.flags & 0x80000)}")
            print(f"\tPad bits = 0x{symbol.record.element.flags >> 20:04x}")
            print(f"\tFrontend Version: Major = {symbol.record.element.ver_fe_major}, Minor = {symbol.record.element.ver_fe_minor}, Build = {symbol.record.element.ver_fe_build}, QFE = {symbol.record.element.ver_fe_qfe}")
            print(f"\tBackend Version: Major = {symbol.record.element.ver_major}, Minor = {symbol.record.element.ver_minor}, Build = {symbol.record.element.ver_build}, QFE = {symbol.record.element.ver_qfe}")
            print(f"\tVersion string: {symbol.record.element.ver_string}")
            print()
        case CvSymbol.SymbolType.s_envblock:
            print()
            print(f"\tCompiled for edit and continue: {yes_no(symbol.record.element.flags & 0x1)}")
            print("\tCommand block:")
            for item in symbol.record.element.items[:-1]:
                print(f"\t\t{item.key} = '{item.value}'")
            print()
        case CvSymbol.SymbolType.s_export:
            print(f" Ordinal = {symbol.record.element.ordinal}", end="")
            if not (symbol.record.element.flags & 0x10):
                print(" (implicit)", end="")
            if symbol.record.element.flags & 0x1:
                print(", CONSTANT", end="")
            if symbol.record.element.flags & 0x2:
                print(", DATA", end="")
            if symbol.record.element.flags & 0x4:
                print(", PRIVATE", end="")
            if symbol.record.element.flags & 0x8:
                print(", NONAME", end="")
            if symbol.record.element.flags & 0x20:
                print(", Forwarder", end="")
            if symbol.record.element.flags & 0xffc0:
                print(f", ??? ({symbol.record.element.flags >> 6:0x04x}", end="")
            print(f", {symbol.record.element.name}")
        case CvSymbol.SymbolType.s_gdata32 | CvSymbol.SymbolType.s_ldata32 | CvSymbol.SymbolType.s_gdata32_st | CvSymbol.SymbolType.s_ldata32_st:
            print(f" [{symbol.record.element.segment:04X}:{symbol.record.element.offset:08X}], Type:", end="")
            print(f" {get_c7_type_name(symbol.record.element.type_index):>18}, {symbol.record.element.name.text}")
        case CvSymbol.SymbolType.s_gdata32_16t | CvSymbol.SymbolType.s_ldata32_16t:
            print(f" [{symbol.record.element.seg:04X}:{symbol.record.element.off:08X}], Type:", end="")
            print(f" {get_c7_type_name(symbol.record.element.typind):>18}, {symbol.record.element.name.text}")
        case CvSymbol.SymbolType.s_buildinfo:
            print(f"\t{get_c7_type_name(symbol.record.element.id)}")
            print()
        case CvSymbol.SymbolType.s_lproc32 | CvSymbol.SymbolType.s_gproc32 | CvSymbol.SymbolType.s_gproc32_id | CvSymbol.SymbolType.s_lproc32_st | CvSymbol.SymbolType.s_gproc32_st:
            is_id: bool = False # symbol.record.type
            print(f" [{symbol.record.element.segment:04X}:{symbol.record.element.offset:08X}], Cb: {symbol.record.element.length:08X}, {'ID' if is_id else 'Type'}: {get_c7_type_name(symbol.record.element.type_index):>18}, {symbol.record.element.name.text}")
            print(f"\tParent: {symbol.record.element.pointer_parent:08X}, End: {symbol.record.element.pointer_end:08X}, next: {symbol.record.element.pointer_next:08X}")
            print(f"\tDebug start: {symbol.record.element.debug_start:08X}, Debug end: {symbol.record.element.debug_end:08X}")
            print_proc_flags(symbol.record.element.flags)
        case CvSymbol.SymbolType.s_lproc32_16t | CvSymbol.SymbolType.s_gproc32_16t:
            print(f" [{symbol.record.element.seg:04X}:{symbol.record.element.off:08X}], Cb: {symbol.record.element.len:08X}: {get_c7_type_name(symbol.record.element.typind)}, {symbol.record.element.name.text}")
            print(f"\tParent: {symbol.record.element.pointer_parent:08X}, End: {symbol.record.element.pointer_end:08X}, next: {symbol.record.element.pointer_next:08X}")
            print(f"\tDebug start: {symbol.record.element.debug_start:08X}, Debug end: {symbol.record.element.debug_end:08X}")
            print_proc_flags(symbol.record.element.flags)
        case CvSymbol.SymbolType.s_local:
            is_id: bool = False # symbol.record.type
            print(f" ", end="")
            print_local_var_flags(symbol.record.element.flags, symbol.record.element.type_index)
            print(symbol.record.element.name)
        case CvSymbol.SymbolType.s_defrange_register | CvSymbol.SymbolType.s_defrange_register_rel | CvSymbol.SymbolType.s_defrange_framepointer_rel_full_scope | CvSymbol.SymbolType.s_defrange_framepointer_rel | CvSymbol.SymbolType.s_defrange_subfield_register:
            match symbol.record.type:
                case CvSymbol.SymbolType.s_defrange_register:
                    if symbol.record.element.attr & 0x1:
                        print("MayAvailable", end="")
                    print(f" {get_c7_register_name(register=symbol.record.element.reg, machine=machine_config.machine)}", end="")
                case CvSymbol.SymbolType.s_defrange_register_rel:
                    print(f" [{get_c7_register_name(register=symbol.record.element.base_reg, machine=machine_config.machine)} + {symbol.record.element.off_base_pointer:04X}]", end="")
                    if symbol.record.element.flags & 0x1:
                        offset_parent = symbol.record.element.flags >> 4
                        print(f" spilledUdtMember offset at {offset_parent}", end="")
                case CvSymbol.SymbolType.s_defrange_framepointer_rel | CvSymbol.SymbolType.s_defrange_framepointer_rel_full_scope:
                    print(f" FrameOffset: {symbol.record.element.off_frame_pointer:04X}", end="")
                case CvSymbol.SymbolType.s_defrange_subfield_register:
                    offset_parent = symbol.record.element.off_parent_padding & 0xfff
                    print(f" offset at {offset_parent:04X}:", end="")
                    if symbol.record.element.attr & 0x1:
                        print("MayAvailable", end="")
                    print(f"  {get_c7_register_name(register=symbol.record.element.reg, machine=machine_config.machine)}", end="")
                case _:
                    raise ValueError
            if symbol.record.type == CvSymbol.SymbolType.s_defrange_framepointer_rel_full_scope:
                print("\t  FULL_SCOPE")
                return
            print()
            print(f"\tRange: [{symbol.record.element.range.isect_start:04X}:{symbol.record.element.range.off_start:08X}] - [{symbol.record.element.range.isect_start:04X}:{symbol.record.element.range.off_start+symbol.record.element.range.cb_range:08X}], ", end="")
            print(f"{len(symbol.record.element.gaps)} Gaps", end="")
            if symbol.record.element.gaps:
                print(" (startOffset, length):", end="")
            for gap in symbol.record.element.gaps:
                print(f" ({gap.gap_start_offset:04X}, {gap.cb_range:X})", end="")
            else:
                print()
        case CvSymbol.SymbolType.s_frameproc:
            print()
            print(f"\tFrame size = 0x{symbol.record.element.cb_frame:08X} bytes")
            print(f"\tPad size = 0x{symbol.record.element.cb_pad:08X} bytes")
            print(f"\tOffset of pad in frame = 0x{symbol.record.element.off_pad:08X}")
            print(f"\tSize of callee save registers = 0x{symbol.record.element.cb_save_regs:08X}")
            print(f"\tAddress of exception handler = {symbol.record.element.sect_ex_hdlr:04X}:{symbol.record.element.off_ex_hdlr:08X}")
            print("\tFunction info: ", end="")
            props = []
            if symbol.record.element.flags & 0x1: props.append("alloca")
            if symbol.record.element.flags & 0x2: props.append("setjmp")
            if symbol.record.element.flags & 0x4: props.append("longjmp")
            if symbol.record.element.flags & 0x8: props.append("inlasm")
            if symbol.record.element.flags & 0x10: props.append("eh")
            if symbol.record.element.flags & 0x20: props.append("inl_specified")
            if symbol.record.element.flags & 0x40: props.append("seh")
            if symbol.record.element.flags & 0x80: props.append("naked")
            if symbol.record.element.flags & 0x100: props.append("gschecks")
            if symbol.record.element.flags & 0x200: props.append("asynceh")
            if symbol.record.element.flags & 0x400: props.append("gsnostackordering")
            if symbol.record.element.flags & 0x800: props.append("wasinlined")
            if symbol.record.element.flags & 0x1000: props.append("strict_gs_check")
            if symbol.record.element.flags & 0x2000: props.append("safebuffers")
            if symbol.record.element.flags & 0x40000: props.append("pgo_on")
            if symbol.record.element.flags & 0x80000:
                props.append("valid_pgo_counts")
            else:
                props.append("invalid_pgo_counts")
            if symbol.record.element.flags & 0x100000: props.append("opt_for_speed")
            print(" ".join(props), end="")
            props = []
            print(f" Local={get_frame_register_name(frame_register=(symbol.record.element.flags >> 14) & 0x3, machine_config=machine_config)}", end="")
            print(f" Param={get_frame_register_name(frame_register=(symbol.record.element.flags >> 16) & 0x3, machine_config=machine_config)}", end="")
            if symbol.record.element.flags & 0x200000: props.append("guardcf")
            if symbol.record.element.flags & 0x400000: props.append("guardcfw")
            print(" ".join(props), end="")
            print(f" (0x{symbol.record.element.flags:08X})", end="")
            if symbol.record.element.flags & 0xff800000:
                print("WARNING: non-zero flag padding)", end="")
            print()
        case CvSymbol.SymbolType.s_bprel32 | CvSymbol.SymbolType.s_bprel32_st:
            print(f" [{symbol.record.element.off:08X}], Type: {get_c7_type_name(symbol.record.element.typind):>18}, {symbol.record.element.name.text}", end="")
            print()
        case CvSymbol.SymbolType.s_bprel32_16t:
            print(f" [{symbol.record.element.off:08X}], Type: {get_c7_type_name(symbol.record.element.typind):>18}, {symbol.record.element.name.text}", end="")
            print()
        case CvSymbol.SymbolType.s_callees:
            print(f" Count: {symbol.record.element.count}")
            for i in range(symbol.record.element.count):
                t = symbol.record.element.funcs[i]
                if t < len(symbol.record.element.invocations):
                    count = symbol.record.element.invocations[i]
                else:
                    count = 0
                if i % 4 == 0:
                    print("\t", end="")
                print(f"{get_c7_type_name(t)} ({count}) ", end="")
                if i != symbol.record.element.count - 1:
                    print(", ", end="")
                if i % 4 == 3:
                    print()
            print()
        case CvSymbol.SymbolType.s_regrel32:
            print(f" {get_c7_register_name(register=symbol.record.element.reg, machine=machine_config.machine)}+{symbol.record.element.off:08X}, Type: {get_c7_type_name(symbol.record.element.typind):>18}, {symbol.record.element.name}")
        case CvSymbol.SymbolType.s_callsiteinfo:
            print(f" [{symbol.record.element.sect:04X}:{symbol.record.element.off:08X}], type = {get_c7_type_name(symbol.record.element.typind):>18s}")
            if symbol.record.element.padding:
                print(f"\tWarning: Reserved bytes in record are non-zero: 0x{symbol.record.element.padding:04X}")
        case CvSymbol.SymbolType.s_label32 | CvSymbol.SymbolType.s_label32_st:
            print(f" [{symbol.record.element.seg:04X}:{symbol.record.element.off:08X}], {symbol.record.element.name.text}, ", end="")
            print_proc_flags(symbol.record.element.flags)
            print()
        case CvSymbol.SymbolType.s_udt | CvSymbol.SymbolType.s_udt_st | CvSymbol.SymbolType.s_udt_16t:
            print(f" {get_c7_type_name(symbol.record.element.typind):>18}, {symbol.record.element.name.text}")
        case CvSymbol.SymbolType.s_filestatic:
            print(" ", end="")
            print_local_var_flags(symbol.record.element.flags, symbol.record.element.typind)
            print(symbol.record.element.name)
            print(f"\tMod: {module_info.module_name}")
        case CvSymbol.SymbolType.s_inlinesite:
            print(f" Parent: {symbol.record.element.pointer_parent:08X}, End: {symbol.record.element.pointer_end:08X}, Inlinee: {get_c7_type_name(symbol.record.element.inlinee)}")
            print_c17_binary_annotations(symbol.record.element.binary_annotations)
        case CvSymbol.SymbolType.s_inlinesite_end:
            print()
        case CvSymbol.SymbolType.s_inlinees:
            # FIXME: Pure guess
            print(f" Count={symbol.record.element.count}")
            for item in symbol.record.element.items:
                print(f"\t0x{item:4x}")
            assert symbol.record_size == 2 + 4 + symbol.record.element.count * 4
        case CvSymbol.SymbolType.s_unk1166:
            # FIXME: Pure guess
            print(f" Field_0x0={symbol.record.element.field_0x0}")
            assert symbol.record_size == 2 + 4
        case CvSymbol.SymbolType.s_heapallocsite:
            print(f" [{symbol.record.element.sect:04X}:{symbol.record.element.off:08X}], ", end="")
            print(f"instr length = {symbol.record.element.cb_instr}, type = {get_c7_type_name(symbol.record.element.typind)}")
        case CvSymbol.SymbolType.s_constant | CvSymbol.SymbolType.s_constant_st:
            print(f" Type: {get_c7_type_name(symbol.record.element.typind):>18}, Value: {get_numeric_string(symbol.record.element.value)}, {symbol.record.element.name.text}")
        case CvSymbol.SymbolType.s_unamespace:
            print(f" {symbol.record.element.name}")
        case CvSymbol.SymbolType.s_thunk32 | CvSymbol.SymbolType.s_thunk32_st:
            print(f" [{symbol.record.element.seg:04X}:{symbol.record.element.off:08X}], Cb: {symbol.record.element.len:08X}, {symbol.record.element.name.text}")
            print(f"\tParent: {symbol.record.element.pointer_parent:08X}, End: {symbol.record.element.pointer_end:08X}, Next: {symbol.record.element.pointer_next:08X}")
            match symbol.record.element.ord:
                case ThunkOrdinal.THUNK_ORDINAL_NOTYPE:
                    pass
                case ThunkOrdinal.THUNK_ORDINAL_ADJUSTOR:
                    print(f"\tType: Adjustor, Delta = {symbol.record.element.variant_adjustor_delta}, Target: {symbol.record.element.variant_adjustor_target.text}")
                case ThunkOrdinal.THUNK_ORDINAL_VCALL:
                    print(f"\tType: VCall, Table Entry: {symbol.record.element.variant_vcall_table_entry}")
                case _:
                    print(f"\tType: {symbol.record.element.ord:02X}")
        case CvSymbol.SymbolType.s_register | CvSymbol.SymbolType.s_register_st:
            print(f" {get_c7_register_name(register=symbol.record.element.reg, machine=machine_config.machine)}, Type: {get_c7_type_name(symbol.record.element.typind):>18}, {symbol.record.element.name.text}")
        case CvSymbol.SymbolType.s_register_16t:
            if symbol.record.element.reg >> 8 != 0:
                print(f" {get_c7_register_name(register=symbol.record.element.reg >> 8, machine=machine_config.machine)}:", end="")
            else:
                print(" ", end="")
            print(f"{get_c7_register_name(register=symbol.record.element.reg & 0xff, machine=machine_config.machine)}, Type: {get_c7_type_name(symbol.record.element.typind):>18}, {symbol.record.element.name.text}")
        case CvSymbol.SymbolType.s_framecookie:
            print(f" {get_c7_register_name(register=symbol.record.element.reg, machine=machine_config.machine):>8}+{symbol.record.element.off:08X}, Type: {get_c7_cookie_type_name(symbol.record.element.cookietype)}, Flags: {symbol.record.element.flags:02X}")
        case CvSymbol.SymbolType.s_block32 | CvSymbol.SymbolType.s_block32_st:
            print(f" [{symbol.record.element.seg:04X}:{symbol.record.element.off:08X}], Cb: {symbol.record.element.len:08X}, {symbol.record.element.name.text}")
            print(f"\tParent: {symbol.record.element.pointer_parent:08X}, End: {symbol.record.element.pointer_end:08X}")
        case CvSymbol.SymbolType.s_section:
            print(f" [{symbol.record.element.isec:04X}], RVA = {symbol.record.element.rva:08X}, Cb = {symbol.record.element.cb:08X}, Align = {1 << symbol.record.element.align:08X}, Characteristics = {symbol.record.element.characteristics:08X}, {symbol.record.element.name}")
        case CvSymbol.SymbolType.s_coffgroup:
            print(f" [{symbol.record.element.seg:04X}:{symbol.record.element.off:08X}], Cb: {symbol.record.element.cb:08X}, Characteristics = {symbol.record.element.characteristics:08X}, {symbol.record.element.name}")
        case CvSymbol.SymbolType.s_procref | CvSymbol.SymbolType.s_lprocref:
            print(f" 0x{symbol.record.element.sum_name:08X}: ({symbol.record.element.imod:4}, {symbol.record.element.ib_sym:08X}) {symbol.record.element.name}")
        case CvSymbol.SymbolType.s_pub32 | CvSymbol.SymbolType.s_pub32_st:
            print(f" [{symbol.record.element.seg:04X}:{symbol.record.element.off:08X}], Flags: {symbol.record.element.flags:08X}, {symbol.record.element.name.text}")
        case CvSymbol.SymbolType.s_pub32_16t:
            # microsoft-pdb says it has equivalent output S_LDATA32_16t/S_GDATA32_16t, but cvdump.exe shows equivalent output to S_PUB32/S_PUB32_ST
            # print(f" [{symbol.record.element.seg:04X}:{symbol.record.element.off:08X}], Type:", end="")
            # print(f" {get_c7_type_name(symbol.record.element.typind):>18}, {symbol.record.element.name.text}")
            print(f" [{symbol.record.element.seg:04X}:{symbol.record.element.off:08X}], Flags: {symbol.record.element.typind:08X}, {symbol.record.element.name.text}")
        case CvSymbol.SymbolType.s_procref_st | CvSymbol.SymbolType.s_lprocref_st:
            print(f" 0x{symbol.record.element.sum_name:08X}: ({symbol.record.element.imod:4}, {symbol.record.element.ib_sym:08X}) {symbol.name.text}")
        case CvSymbol.SymbolType.s_constant_16t:
            print(f" Type: {get_c7_type_name(symbol.record.element.typind):>18}, Value: {get_numeric_string(symbol.record.element.value)}, {symbol.record.element.name.text}")
        case CvSymbol.SymbolType.s_armswitchtable:
            print()
            print(f"\tBase address:   [{symbol.record.element.sect_base:04X}:{symbol.record.element.offset_base:08X}]")
            print(f"\tBranch address: [{symbol.record.element.sect_branch:04X}:{symbol.record.element.offset_branch:08X}]")
            print(f"\tTable address:  [{symbol.record.element.sect_table:04X}:{symbol.record.element.offset_table:08X}]")
            print(f"\tEntry count = {symbol.record.element.count_entries}")
            print(f"\tSwitch entry type = ", end="")
            try:
                match CV_armswitchtype(symbol.record.element.switch_type):
                    case CV_armswitchtype.CV_SWT_INT1: print("signed byte")
                    case CV_armswitchtype.CV_SWT_UINT1: print("unsigned byte")
                    case CV_armswitchtype.CV_SWT_INT2: print("signed two byte")
                    case CV_armswitchtype.CV_SWT_UINT2: print("unsigned two byte")
                    case CV_armswitchtype.CV_SWT_INT4: print("signed four byte")
                    case CV_armswitchtype.CV_SWT_UINT4: print("unsigned four byte")
                    case CV_armswitchtype.CV_SWT_POINTER: print("pointer")
                    case CV_armswitchtype.CV_SWT_UINT1SHL1: print("unsigned byte scaled by two")
                    case CV_armswitchtype.CV_SWT_UINT2SHL1: print("unsigned two byte scaled by two")
                    case CV_armswitchtype.CV_SWT_INT1SHL1: print("signed byte scaled by two")
                    case CV_armswitchtype.CV_SWT_INT2SHL1: print("signed two byte scaled by two")
                    case _: print(f"unknown(0x{symbol.record.element.switch_type:X})")
            except ValueError:
                print(f"unknown(0x{symbol.record.element.switch_type:X})")
        case CvSymbol.SymbolType.s_proc_id_end:
            print()
        case CvSymbol.SymbolType.s_end:
            print()
            print()
        case _:
            raise ValueError(symbol.record.type.name.upper(), hex(symbol.record.type), symbol.record.type)
    # symbol.record_pos, symbol.record_size, symbol.record.type)
