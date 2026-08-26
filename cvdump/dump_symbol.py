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
    CV_CFL_8080         = 0x00
    CV_CFL_8086         = 0x01
    CV_CFL_80286        = 0x02
    CV_CFL_80386        = 0x03
    CV_CFL_80486        = 0x04
    CV_CFL_PENTIUM      = 0x05
    CV_CFL_PENTIUMII    = 0x06
    CV_CFL_PENTIUMPRO   = CV_CFL_PENTIUMII
    CV_CFL_PENTIUMIII   = 0x07
    CV_CFL_MIPS         = 0x10
    CV_CFL_MIPSR4000    = CV_CFL_MIPS  # don't break current cod
    CV_CFL_MIPS16       = 0x11
    CV_CFL_MIPS32       = 0x12
    CV_CFL_MIPS64       = 0x13
    CV_CFL_MIPSI        = 0x14
    CV_CFL_MIPSII       = 0x15
    CV_CFL_MIPSIII      = 0x16
    CV_CFL_MIPSIV       = 0x17
    CV_CFL_MIPSV        = 0x18
    CV_CFL_M68000       = 0x20
    CV_CFL_M68010       = 0x21
    CV_CFL_M68020       = 0x22
    CV_CFL_M68030       = 0x23
    CV_CFL_M68040       = 0x24
    CV_CFL_ALPHA        = 0x30
    CV_CFL_ALPHA_21064  = 0x30
    CV_CFL_ALPHA_21164  = 0x31
    CV_CFL_ALPHA_21164A = 0x32
    CV_CFL_ALPHA_21264  = 0x33
    CV_CFL_ALPHA_21364  = 0x34
    CV_CFL_PPC601       = 0x40
    CV_CFL_PPC603       = 0x41
    CV_CFL_PPC604       = 0x42
    CV_CFL_PPC620       = 0x43
    CV_CFL_PPCFP        = 0x44
    CV_CFL_PPCBE        = 0x45
    CV_CFL_SH3          = 0x50
    CV_CFL_SH3E         = 0x51
    CV_CFL_SH3DSP       = 0x52
    CV_CFL_SH4          = 0x53
    CV_CFL_SHMEDIA      = 0x54
    CV_CFL_ARM3         = 0x60
    CV_CFL_ARM4         = 0x61
    CV_CFL_ARM4T        = 0x62
    CV_CFL_ARM5         = 0x63
    CV_CFL_ARM5T        = 0x64
    CV_CFL_ARM6         = 0x65
    CV_CFL_ARM_XMAC     = 0x66
    CV_CFL_ARM_WMMX     = 0x67
    CV_CFL_ARM7         = 0x68
    CV_CFL_OMNI         = 0x70
    CV_CFL_IA64         = 0x80
    CV_CFL_IA64_1       = 0x80
    CV_CFL_IA64_2       = 0x81
    CV_CFL_CEE          = 0x90
    CV_CFL_AM33         = 0xA0
    CV_CFL_M32R         = 0xB0
    CV_CFL_TRICORE      = 0xC0
    CV_CFL_X64          = 0xD0
    CV_CFL_AMD64        = CV_CFL_X64
    CV_CFL_EBC          = 0xE0
    CV_CFL_THUMB        = 0xF0
    CV_CFL_ARMNT        = 0xF4
    CV_CFL_ARM64        = 0xF6
    CV_CFL_D3D11_SHADER = 0x100


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


class RegisterCommon:
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
                reg_lookup = REGISTER_NAMES_ARM64
            case CpuType.CV_CFL_IA64_1 | CpuType.CV_CFL_IA64_2:
                reg_lookup = REGISTER_NAMES_IA
            case CpuType.CV_AMD64:
                reg_lookup = REGISTER_NAMES_AMD64
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

def get_frame_register_name(frame_register: int, machine_config: MachineConfig) -> str:
    match machine_config.machine:
        case Machine.IMAGE_FILE_MACHINE_I386:
            register = MACHINE_I386_FRAME_REGISTERS[frame_register]
            return get_c7_register_name(register=register, machine=machine_config.machine)
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



def dump_symbol(symbol: ModiStream.Symbol, machine_config: MachineConfig, module_info, dump_pos: bool=True):
    try:
        symbol_type_name = symbol.record.type.name.upper()
    except AttributeError:
        raise ValueError("WARNING: Unknown record type")
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
        case CvSymbol.SymbolType.s_gdata32_16t | CvSymbol.SymbolType.s_ldata32_16t | CvSymbol.SymbolType.s_pub32_16t:
            print(f" [{symbol.record.element.seg:04X}:{symbol.record.element.off:08X}], Type:", end="")
            print(f" {get_c7_type_name(symbol.record.element.typind):>18}, {symbol.record.element.name.text}")
        case CvSymbol.SymbolType.s_buildinfo:
            print(f"\t{get_c7_type_name(symbol.record.element.id)}")
            print()
        case CvSymbol.SymbolType.s_lproc32 | CvSymbol.SymbolType.s_gproc32 | CvSymbol.SymbolType.s_lproc32_st | CvSymbol.SymbolType.s_gproc32_st:
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
            print(f" Count={symbol.record.element.count}")
            for item in symbol.record.element.items:
                print(f"\t0x{item:4x}")
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
        case CvSymbol.SymbolType.s_procref_st | CvSymbol.SymbolType.s_lprocref_st:
            print(f" 0x{symbol.record.element.sum_name:08X}: ({symbol.record.element.imod:4}, {symbol.record.element.ib_sym:08X}) {symbol.name.text}")
        case CvSymbol.SymbolType.s_constant_16t:
            print(f" Type: {get_c7_type_name(symbol.record.element.typind):>18}, Value: {get_numeric_string(symbol.record.element.value)}, {symbol.record.element.name.text}")
        case CvSymbol.SymbolType.s_end:
            print()
            print()
        case _:
            raise ValueError(symbol.record.type.name.upper(), hex(symbol.record.type), symbol.record.type)
    # symbol.record_pos, symbol.record_size, symbol.record.type)
