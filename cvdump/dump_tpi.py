import decimal
import enum

from cvdump.kaitai.names_stream import NamesStream
from cvdump.kaitai.tpi_stream import TpiStream


class ClassFieldAttribute(enum.IntFlag): # CV_fldattr_t (cvinfo.h)
    ACCESS      = 0b0000000000000011        # access protection CV_access_e
    MPROP       = 0b0000000000011100        # method properties CV_methodprop_e
    PSEUDO      = 0b0000000000100000        # compiler generated fcn and does not exist
    NOINHERIT   = 0b0000000001000000        # true if class cannot be inherited
    NOCONSTRUCT = 0b0000000010000000        # true if class cannot be constructed
    COMPGENX    = 0b0000000100000000        # compiler generated fcn and does exist
    SEALED      = 0b0000001000000000        # true if method cannot be overridden

#  bit field structure describing class/struct/union/enum properties
class ClassProperties(enum.IntFlag): # CV_prop_t (cvinfo.h)
    PACKED         = 0b0000000000000001     # true if structure is packed
    CTOR           = 0b0000000000000010     # true if constructors or destructors present
    OVLOPS         = 0b0000000000000100     # true if overloaded operators present
    ISNESTED       = 0b0000000000001000     # true if this is a nested class
    CNESTED        = 0b0000000000010000     # true if this class contains nested types
    OPASSIGN       = 0b0000000000100000     # true if overloaded assignment (=)
    OPCAST         = 0b0000000001000000     # true if casting methods
    FWDREF         = 0b0000000010000000     # true if forward reference (incomplete defn)
    SCOPED         = 0b0000000100000000     # scoped definition
    HASUNIQUENAME  = 0b0000001000000000     # true if there is a decorated name following the regular name
    SEALED         = 0b0000010000000000     # true if class cannot be used as a base class
    HFA            = 0b0001100000000000     # CV_HFA_e
    INTRINSIC      = 0b0010000000000000     # true if class is an intrinsic type (e.g. __m128d)
    MOCOM          = 0b1100000000000000     # CV_MOCOM_UDT_e


class FunctionFlags(enum.IntFlag): # CV_funcattr_t (cvinfo.h)
    CXXRETURNUDT    = 0b00000001            # true if C++ style ReturnUDT
    CTOR            = 0b00000010            # true if func is an instance constructor
    CTORVBASE       = 0b00000100            # true if func is an instance constructor of a class with virtual bases
    UNUSED          = 0b11111000            # unused


class Pointer16Attribute(enum.IntFlag): # lfPointer_16t.attr (cvinfo.h)
    PTRTYPE        = 0b0000000000011111     # ordinal specifying pointer type (CV_ptrtype_e)
    PTRMODE        = 0b0000000011100000     # ordinal specifying pointer mode (CV_ptrmode_e)
    ISFLAT32       = 0b0000000100000000     # true if 0:32 pointer
    ISVOLATILE     = 0b0000001000000000     # TRUE if volatile pointer
    ISCONST        = 0b0000010000000000     # TRUE if const pointer
    ISUNALIGNED    = 0b0000100000000000     # TRUE if unaligned pointer
    UNUSED         = 0b1111000000000000

class PointerAttribute(enum.IntFlag): # lfPointer.attr (cvinfo.h)
    PTRTYPE        = 0b00000000000000000000000000011111     # ordinal specifying pointer type (CV_ptrtype_e)
    PTRMODE        = 0b00000000000000000000000011100000     # ordinal specifying pointer mode (CV_ptrmode_e)
    ISFLAT32       = 0b00000000000000000000000100000000     # true if 0:32 pointer
    ISVOLATILE     = 0b00000000000000000000001000000000     # TRUE if volatile pointer
    ISCONST        = 0b00000000000000000000010000000000     # TRUE if const pointer
    ISUNALIGNED    = 0b00000000000000000000100000000000     # TRUE if unaligned pointer
    ISRESTRICT     = 0b00000000000000000001000000000000     # TRUE if restricted pointer (allow agressive opts)
    SIZE           = 0b00000000000001111110000000000000     # size of pointer (in bytes)
    ISMOCOM        = 0b00000000000010000000000000000000     # TRUE if it is a MoCOM pointer (^ or %)
    ISLREF         = 0b00000000000100000000000000000000     # TRUE if it is this pointer of member function with & ref-qualifier
    ISRREF         = 0b00000000001000000000000000000000     # TRUE if it is this pointer of member function with & ref-qualifier
    UNUSED         = 0b11111111110000000000000000000000

# rgszCallConventionNames (type7.cpp)
CALL_CONVENTION_NAMES = [
    "C Near",
    "C Far",
    "Pascal Near",
    "Pascal Far",
    "Fast Near",
    "Fast Far",
    "???",
    "STD Near",
    "STD Far",
    "SYS Near",
    "SYS Far",
    "ThisCall",
    "MIPS CALL",
    "Generic",
    "Alpha Call",
    "PPC Call",
    "SH Call",
    "ARM Call",
    "AM33 Call",
    "TriCore Call",
    "SH5 Call",
    "M32R Call",
    "CLR Call",
    "No callconv; always Inlined",
    "Vector Near",
]


CLASS_ACCESS_ATTRIBUTE_NAMES = [
    "none",
    "private",
    "protected",
    "public",
]

POINTER_MODE_NAMES = [
    "Pointer",
    "L-value Reference",
    "Pointer to member",
    "Pointer to member function",
    "R-value Reference",
    "???",
    "???",
    "???",
]

POINTER_TYPE_NAMES = [
    "__near",
    "__far",
    "__huge",
    "BasedSeg",
    "BasedVal",
    "BasedSegVal",
    "BasedAddr",
    "BasedSegAdr",
    "BasedOnType",
    "BasedOnSelf",
    "NEAR32",
    "FAR32",
    "__ptr64",
    "???",
    "???",
    "???",
]

FUNC_TYPE_NAMES = [
    "NEAR",
    "FAR",
    "THIN",
    "ADDRESS POINT DISPLACEMENT",
    "POINTER TO METACLASS DESCRIPTOR",
    "NEAR32",
    "FAR32",
    "??? (0x7)",
    "??? (0x8)",
    "??? (0x9)",
    "??? (0xa)",
    "??? (0xb)",
    "??? (0xc)",
    "??? (0xd)",
    "??? (0xe)",
    "??? (0xf)",
]

class PointerMode(enum.IntEnum):  # CV_ptrmode_e (cvinfo.h)
    CV_PTR_MODE_PTR     = 0x00  # "normal" pointer
    CV_PTR_MODE_REF     = 0x01  # "old" reference
    CV_PTR_MODE_LVREF   = 0x01  # l-value reference
    CV_PTR_MODE_PMEM    = 0x02  # pointer to data member
    CV_PTR_MODE_PMFUNC  = 0x03  # pointer to member function
    CV_PTR_MODE_RVREF   = 0x04  # r-value reference
    CV_PTR_MODE_RESERVED= 0x05  # first unused pointer mode


class PointerType(enum.IntEnum): # CV_ptrtype_e (cvinfo.h)
    CV_PTR_NEAR         = 0x00  # 16 bit pointer
    CV_PTR_FAR          = 0x01  # 16:16 far pointer
    CV_PTR_HUGE         = 0x02  # 16:16 huge pointer
    CV_PTR_BASE_SEG     = 0x03  # based on segment
    CV_PTR_BASE_VAL     = 0x04  # based on value of base
    CV_PTR_BASE_SEGVAL  = 0x05  # based on segment value of base
    CV_PTR_BASE_ADDR    = 0x06  # based on address of base
    CV_PTR_BASE_SEGADDR = 0x07  # based on segment address of base
    CV_PTR_BASE_TYPE    = 0x08  # based on type
    CV_PTR_BASE_SELF    = 0x09  # based on self
    CV_PTR_NEAR32       = 0x0a  # 32 bit pointer
    CV_PTR_FAR32        = 0x0b  # 16:32 pointer
    CV_PTR_64           = 0x0c  # 64 bit pointer
    CV_PTR_UNUSEDPTR    = 0x0d  # first unused pointer type


class Modifier(enum.IntFlag): # CV_modifier_t (cvinfo.h)
    MOD_const       = 0b0000000000000001
    MOD_volatile    = 0b0000000000000010
    MOD_unaligned   = 0b0000000000000100
    MOD_unused      = 0b1111111111111000


# selected values for type_index - for a more complete definition, see
# Microsoft Symbol and Type OMF document
class C7TypeEnum(enum.IntEnum): # TYPE_ENUM_e (cvinfo.h)
    T_NOTYPE        = 0x0000   # uncharacterized type (no type)
    T_ABS           = 0x0001   # absolute symbol
    T_SEGMENT       = 0x0002   # segment type
    T_VOID          = 0x0003   # void
    T_HRESULT       = 0x0008   # OLE/COM HRESULT
    T_32PHRESULT    = 0x0408   # OLE/COM HRESULT __ptr32 *
    T_64PHRESULT    = 0x0608   # OLE/COM HRESULT __ptr64 *

    T_PVOID         = 0x0103   # near pointer to void
    T_PFVOID        = 0x0203   # far pointer to void
    T_PHVOID        = 0x0303   # huge pointer to void
    T_32PVOID       = 0x0403   # 32 bit pointer to void
    T_32PFVOID      = 0x0503   # 16:32 pointer to void
    T_64PVOID       = 0x0603   # 64 bit pointer to void
    T_CURRENCY      = 0x0004   # BASIC 8 byte currency value
    T_NBASICSTR     = 0x0005   # Near BASIC string
    T_FBASICSTR     = 0x0006   # Far BASIC string
    T_NOTTRANS      = 0x0007   # type not translated by cvpack
    T_BIT           = 0x0060   # bit
    T_PASCHAR       = 0x0061   # Pascal CHAR
    T_BOOL32FF      = 0x0062   # 32-bit BOOL where true is 0xffffffff

#      Character types

    T_CHAR          = 0x0010   # 8 bit signed
    T_PCHAR         = 0x0110   # 16 bit pointer to 8 bit signed
    T_PFCHAR        = 0x0210   # 16:16 far pointer to 8 bit signed
    T_PHCHAR        = 0x0310   # 16:16 huge pointer to 8 bit signed
    T_32PCHAR       = 0x0410   # 32 bit pointer to 8 bit signed
    T_32PFCHAR      = 0x0510   # 16:32 pointer to 8 bit signed
    T_64PCHAR       = 0x0610   # 64 bit pointer to 8 bit signed

    T_UCHAR         = 0x0020   # 8 bit unsigned
    T_PUCHAR        = 0x0120   # 16 bit pointer to 8 bit unsigned
    T_PFUCHAR       = 0x0220   # 16:16 far pointer to 8 bit unsigned
    T_PHUCHAR       = 0x0320   # 16:16 huge pointer to 8 bit unsigned
    T_32PUCHAR      = 0x0420   # 32 bit pointer to 8 bit unsigned
    T_32PFUCHAR     = 0x0520   # 16:32 pointer to 8 bit unsigned
    T_64PUCHAR      = 0x0620   # 64 bit pointer to 8 bit unsigned

#      really a character types

    T_RCHAR         = 0x0070   # really a char
    T_PRCHAR        = 0x0170   # 16 bit pointer to a real char
    T_PFRCHAR       = 0x0270   # 16:16 far pointer to a real char
    T_PHRCHAR       = 0x0370   # 16:16 huge pointer to a real char
    T_32PRCHAR      = 0x0470   # 32 bit pointer to a real char
    T_32PFRCHAR     = 0x0570   # 16:32 pointer to a real char
    T_64PRCHAR      = 0x0670   # 64 bit pointer to a real char


#      really a wide character types

    T_WCHAR         = 0x0071   # wide char
    T_PWCHAR        = 0x0171   # 16 bit pointer to a wide char
    T_PFWCHAR       = 0x0271   # 16:16 far pointer to a wide char
    T_PHWCHAR       = 0x0371   # 16:16 huge pointer to a wide char
    T_32PWCHAR      = 0x0471   # 32 bit pointer to a wide char
    T_32PFWCHAR     = 0x0571   # 16:32 pointer to a wide char
    T_64PWCHAR      = 0x0671   # 64 bit pointer to a wide char

#      really a 16-bit unicode char

    T_CHAR16         = 0x007a   # 16-bit unicode char
    T_PCHAR16        = 0x017a   # 16 bit pointer to a 16-bit unicode char
    T_PFCHAR16       = 0x027a   # 16:16 far pointer to a 16-bit unicode char
    T_PHCHAR16       = 0x037a   # 16:16 huge pointer to a 16-bit unicode char
    T_32PCHAR16      = 0x047a   # 32 bit pointer to a 16-bit unicode char
    T_32PFCHAR16     = 0x057a   # 16:32 pointer to a 16-bit unicode char
    T_64PCHAR16      = 0x067a   # 64 bit pointer to a 16-bit unicode char

#      really a 32-bit unicode char

    T_CHAR32         = 0x007b   # 32-bit unicode char
    T_PCHAR32        = 0x017b   # 16 bit pointer to a 32-bit unicode char
    T_PFCHAR32       = 0x027b   # 16:16 far pointer to a 32-bit unicode char
    T_PHCHAR32       = 0x037b   # 16:16 huge pointer to a 32-bit unicode char
    T_32PCHAR32      = 0x047b   # 32 bit pointer to a 32-bit unicode char
    T_32PFCHAR32     = 0x057b   # 16:32 pointer to a 32-bit unicode char
    T_64PCHAR32      = 0x067b   # 64 bit pointer to a 32-bit unicode char

#      8 bit int types

    T_INT1          = 0x0068   # 8 bit signed int
    T_PINT1         = 0x0168   # 16 bit pointer to 8 bit signed int
    T_PFINT1        = 0x0268   # 16:16 far pointer to 8 bit signed int
    T_PHINT1        = 0x0368   # 16:16 huge pointer to 8 bit signed int
    T_32PINT1       = 0x0468   # 32 bit pointer to 8 bit signed int
    T_32PFINT1      = 0x0568   # 16:32 pointer to 8 bit signed int
    T_64PINT1       = 0x0668   # 64 bit pointer to 8 bit signed int

    T_UINT1         = 0x0069   # 8 bit unsigned int
    T_PUINT1        = 0x0169   # 16 bit pointer to 8 bit unsigned int
    T_PFUINT1       = 0x0269   # 16:16 far pointer to 8 bit unsigned int
    T_PHUINT1       = 0x0369   # 16:16 huge pointer to 8 bit unsigned int
    T_32PUINT1      = 0x0469   # 32 bit pointer to 8 bit unsigned int
    T_32PFUINT1     = 0x0569   # 16:32 pointer to 8 bit unsigned int
    T_64PUINT1      = 0x0669   # 64 bit pointer to 8 bit unsigned int


#      16 bit short types

    T_SHORT         = 0x0011   # 16 bit signed
    T_PSHORT        = 0x0111   # 16 bit pointer to 16 bit signed
    T_PFSHORT       = 0x0211   # 16:16 far pointer to 16 bit signed
    T_PHSHORT       = 0x0311   # 16:16 huge pointer to 16 bit signed
    T_32PSHORT      = 0x0411   # 32 bit pointer to 16 bit signed
    T_32PFSHORT     = 0x0511   # 16:32 pointer to 16 bit signed
    T_64PSHORT      = 0x0611   # 64 bit pointer to 16 bit signed

    T_USHORT        = 0x0021   # 16 bit unsigned
    T_PUSHORT       = 0x0121   # 16 bit pointer to 16 bit unsigned
    T_PFUSHORT      = 0x0221   # 16:16 far pointer to 16 bit unsigned
    T_PHUSHORT      = 0x0321   # 16:16 huge pointer to 16 bit unsigned
    T_32PUSHORT     = 0x0421   # 32 bit pointer to 16 bit unsigned
    T_32PFUSHORT    = 0x0521   # 16:32 pointer to 16 bit unsigned
    T_64PUSHORT     = 0x0621   # 64 bit pointer to 16 bit unsigned

#      16 bit int types

    T_INT2          = 0x0072   # 16 bit signed int
    T_PINT2         = 0x0172   # 16 bit pointer to 16 bit signed int
    T_PFINT2        = 0x0272   # 16:16 far pointer to 16 bit signed int
    T_PHINT2        = 0x0372   # 16:16 huge pointer to 16 bit signed int
    T_32PINT2       = 0x0472   # 32 bit pointer to 16 bit signed int
    T_32PFINT2      = 0x0572   # 16:32 pointer to 16 bit signed int
    T_64PINT2       = 0x0672   # 64 bit pointer to 16 bit signed int

    T_UINT2         = 0x0073   # 16 bit unsigned int
    T_PUINT2        = 0x0173   # 16 bit pointer to 16 bit unsigned int
    T_PFUINT2       = 0x0273   # 16:16 far pointer to 16 bit unsigned int
    T_PHUINT2       = 0x0373   # 16:16 huge pointer to 16 bit unsigned int
    T_32PUINT2      = 0x0473   # 32 bit pointer to 16 bit unsigned int
    T_32PFUINT2     = 0x0573   # 16:32 pointer to 16 bit unsigned int
    T_64PUINT2      = 0x0673   # 64 bit pointer to 16 bit unsigned int

#      32 bit long types

    T_LONG          = 0x0012   # 32 bit signed
    T_ULONG         = 0x0022   # 32 bit unsigned
    T_PLONG         = 0x0112   # 16 bit pointer to 32 bit signed
    T_PULONG        = 0x0122   # 16 bit pointer to 32 bit unsigned
    T_PFLONG        = 0x0212   # 16:16 far pointer to 32 bit signed
    T_PFULONG       = 0x0222   # 16:16 far pointer to 32 bit unsigned
    T_PHLONG        = 0x0312   # 16:16 huge pointer to 32 bit signed
    T_PHULONG       = 0x0322   # 16:16 huge pointer to 32 bit unsigned

    T_32PLONG       = 0x0412   # 32 bit pointer to 32 bit signed
    T_32PULONG      = 0x0422   # 32 bit pointer to 32 bit unsigned
    T_32PFLONG      = 0x0512   # 16:32 pointer to 32 bit signed
    T_32PFULONG     = 0x0522   # 16:32 pointer to 32 bit unsigned
    T_64PLONG       = 0x0612   # 64 bit pointer to 32 bit signed
    T_64PULONG      = 0x0622   # 64 bit pointer to 32 bit unsigned

#      32 bit int types

    T_INT4          = 0x0074   # 32 bit signed int
    T_PINT4         = 0x0174   # 16 bit pointer to 32 bit signed int
    T_PFINT4        = 0x0274   # 16:16 far pointer to 32 bit signed int
    T_PHINT4        = 0x0374   # 16:16 huge pointer to 32 bit signed int
    T_32PINT4       = 0x0474   # 32 bit pointer to 32 bit signed int
    T_32PFINT4      = 0x0574   # 16:32 pointer to 32 bit signed int
    T_64PINT4       = 0x0674   # 64 bit pointer to 32 bit signed int

    T_UINT4         = 0x0075   # 32 bit unsigned int
    T_PUINT4        = 0x0175   # 16 bit pointer to 32 bit unsigned int
    T_PFUINT4       = 0x0275   # 16:16 far pointer to 32 bit unsigned int
    T_PHUINT4       = 0x0375   # 16:16 huge pointer to 32 bit unsigned int
    T_32PUINT4      = 0x0475   # 32 bit pointer to 32 bit unsigned int
    T_32PFUINT4     = 0x0575   # 16:32 pointer to 32 bit unsigned int
    T_64PUINT4      = 0x0675   # 64 bit pointer to 32 bit unsigned int

#      64 bit quad types

    T_QUAD          = 0x0013   # 64 bit signed
    T_PQUAD         = 0x0113   # 16 bit pointer to 64 bit signed
    T_PFQUAD        = 0x0213   # 16:16 far pointer to 64 bit signed
    T_PHQUAD        = 0x0313   # 16:16 huge pointer to 64 bit signed
    T_32PQUAD       = 0x0413   # 32 bit pointer to 64 bit signed
    T_32PFQUAD      = 0x0513   # 16:32 pointer to 64 bit signed
    T_64PQUAD       = 0x0613   # 64 bit pointer to 64 bit signed

    T_UQUAD         = 0x0023   # 64 bit unsigned
    T_PUQUAD        = 0x0123   # 16 bit pointer to 64 bit unsigned
    T_PFUQUAD       = 0x0223   # 16:16 far pointer to 64 bit unsigned
    T_PHUQUAD       = 0x0323   # 16:16 huge pointer to 64 bit unsigned
    T_32PUQUAD      = 0x0423   # 32 bit pointer to 64 bit unsigned
    T_32PFUQUAD     = 0x0523   # 16:32 pointer to 64 bit unsigned
    T_64PUQUAD      = 0x0623   # 64 bit pointer to 64 bit unsigned

#      64 bit int types

    T_INT8          = 0x0076   # 64 bit signed int
    T_PINT8         = 0x0176   # 16 bit pointer to 64 bit signed int
    T_PFINT8        = 0x0276   # 16:16 far pointer to 64 bit signed int
    T_PHINT8        = 0x0376   # 16:16 huge pointer to 64 bit signed int
    T_32PINT8       = 0x0476   # 32 bit pointer to 64 bit signed int
    T_32PFINT8      = 0x0576   # 16:32 pointer to 64 bit signed int
    T_64PINT8       = 0x0676   # 64 bit pointer to 64 bit signed int

    T_UINT8         = 0x0077   # 64 bit unsigned int
    T_PUINT8        = 0x0177   # 16 bit pointer to 64 bit unsigned int
    T_PFUINT8       = 0x0277   # 16:16 far pointer to 64 bit unsigned int
    T_PHUINT8       = 0x0377   # 16:16 huge pointer to 64 bit unsigned int
    T_32PUINT8      = 0x0477   # 32 bit pointer to 64 bit unsigned int
    T_32PFUINT8     = 0x0577   # 16:32 pointer to 64 bit unsigned int
    T_64PUINT8      = 0x0677   # 64 bit pointer to 64 bit unsigned int

#      128 bit octet types

    T_OCT           = 0x0014   # 128 bit signed
    T_POCT          = 0x0114   # 16 bit pointer to 128 bit signed
    T_PFOCT         = 0x0214   # 16:16 far pointer to 128 bit signed
    T_PHOCT         = 0x0314   # 16:16 huge pointer to 128 bit signed
    T_32POCT        = 0x0414   # 32 bit pointer to 128 bit signed
    T_32PFOCT       = 0x0514   # 16:32 pointer to 128 bit signed
    T_64POCT        = 0x0614   # 64 bit pointer to 128 bit signed

    T_UOCT          = 0x0024   # 128 bit unsigned
    T_PUOCT         = 0x0124   # 16 bit pointer to 128 bit unsigned
    T_PFUOCT        = 0x0224   # 16:16 far pointer to 128 bit unsigned
    T_PHUOCT        = 0x0324   # 16:16 huge pointer to 128 bit unsigned
    T_32PUOCT       = 0x0424   # 32 bit pointer to 128 bit unsigned
    T_32PFUOCT      = 0x0524   # 16:32 pointer to 128 bit unsigned
    T_64PUOCT       = 0x0624   # 64 bit pointer to 128 bit unsigned

#      128 bit int types

    T_INT16         = 0x0078   # 128 bit signed int
    T_PINT16        = 0x0178   # 16 bit pointer to 128 bit signed int
    T_PFINT16       = 0x0278   # 16:16 far pointer to 128 bit signed int
    T_PHINT16       = 0x0378   # 16:16 huge pointer to 128 bit signed int
    T_32PINT16      = 0x0478   # 32 bit pointer to 128 bit signed int
    T_32PFINT16     = 0x0578   # 16:32 pointer to 128 bit signed int
    T_64PINT16      = 0x0678   # 64 bit pointer to 128 bit signed int

    T_UINT16        = 0x0079   # 128 bit unsigned int
    T_PUINT16       = 0x0179   # 16 bit pointer to 128 bit unsigned int
    T_PFUINT16      = 0x0279   # 16:16 far pointer to 128 bit unsigned int
    T_PHUINT16      = 0x0379   # 16:16 huge pointer to 128 bit unsigned int
    T_32PUINT16     = 0x0479   # 32 bit pointer to 128 bit unsigned int
    T_32PFUINT16    = 0x0579   # 16:32 pointer to 128 bit unsigned int
    T_64PUINT16     = 0x0679   # 64 bit pointer to 128 bit unsigned int

#      16 bit real types

    T_REAL16        = 0x0046   # 16 bit real
    T_PREAL16       = 0x0146   # 16 bit pointer to 16 bit real
    T_PFREAL16      = 0x0246   # 16:16 far pointer to 16 bit real
    T_PHREAL16      = 0x0346   # 16:16 huge pointer to 16 bit real
    T_32PREAL16     = 0x0446   # 32 bit pointer to 16 bit real
    T_32PFREAL16    = 0x0546   # 16:32 pointer to 16 bit real
    T_64PREAL16     = 0x0646   # 64 bit pointer to 16 bit real


#      32 bit real types

    T_REAL32        = 0x0040   # 32 bit real
    T_PREAL32       = 0x0140   # 16 bit pointer to 32 bit real
    T_PFREAL32      = 0x0240   # 16:16 far pointer to 32 bit real
    T_PHREAL32      = 0x0340   # 16:16 huge pointer to 32 bit real
    T_32PREAL32     = 0x0440   # 32 bit pointer to 32 bit real
    T_32PFREAL32    = 0x0540   # 16:32 pointer to 32 bit real
    T_64PREAL32     = 0x0640   # 64 bit pointer to 32 bit real

#      32 bit partial-precision real types

    T_REAL32PP      = 0x0045   # 32 bit PP real
    T_PREAL32PP     = 0x0145   # 16 bit pointer to 32 bit PP real
    T_PFREAL32PP    = 0x0245   # 16:16 far pointer to 32 bit PP real
    T_PHREAL32PP    = 0x0345   # 16:16 huge pointer to 32 bit PP real
    T_32PREAL32PP   = 0x0445   # 32 bit pointer to 32 bit PP real
    T_32PFREAL32PP  = 0x0545   # 16:32 pointer to 32 bit PP real
    T_64PREAL32PP   = 0x0645   # 64 bit pointer to 32 bit PP real

#      48 bit real types

    T_REAL48        = 0x0044   # 48 bit real
    T_PREAL48       = 0x0144   # 16 bit pointer to 48 bit real
    T_PFREAL48      = 0x0244   # 16:16 far pointer to 48 bit real
    T_PHREAL48      = 0x0344   # 16:16 huge pointer to 48 bit real
    T_32PREAL48     = 0x0444   # 32 bit pointer to 48 bit real
    T_32PFREAL48    = 0x0544   # 16:32 pointer to 48 bit real
    T_64PREAL48     = 0x0644   # 64 bit pointer to 48 bit real

#      64 bit real types

    T_REAL64        = 0x0041   # 64 bit real
    T_PREAL64       = 0x0141   # 16 bit pointer to 64 bit real
    T_PFREAL64      = 0x0241   # 16:16 far pointer to 64 bit real
    T_PHREAL64      = 0x0341   # 16:16 huge pointer to 64 bit real
    T_32PREAL64     = 0x0441   # 32 bit pointer to 64 bit real
    T_32PFREAL64    = 0x0541   # 16:32 pointer to 64 bit real
    T_64PREAL64     = 0x0641   # 64 bit pointer to 64 bit real

#      80 bit real types

    T_REAL80        = 0x0042   # 80 bit real
    T_PREAL80       = 0x0142   # 16 bit pointer to 80 bit real
    T_PFREAL80      = 0x0242   # 16:16 far pointer to 80 bit real
    T_PHREAL80      = 0x0342   # 16:16 huge pointer to 80 bit real
    T_32PREAL80     = 0x0442   # 32 bit pointer to 80 bit real
    T_32PFREAL80    = 0x0542   # 16:32 pointer to 80 bit real
    T_64PREAL80     = 0x0642   # 64 bit pointer to 80 bit real

#      128 bit real types

    T_REAL128       = 0x0043   # 128 bit real
    T_PREAL128      = 0x0143   # 16 bit pointer to 128 bit real
    T_PFREAL128     = 0x0243   # 16:16 far pointer to 128 bit real
    T_PHREAL128     = 0x0343   # 16:16 huge pointer to 128 bit real
    T_32PREAL128    = 0x0443   # 32 bit pointer to 128 bit real
    T_32PFREAL128   = 0x0543   # 16:32 pointer to 128 bit real
    T_64PREAL128    = 0x0643   # 64 bit pointer to 128 bit real


#      32 bit complex types

    T_CPLX32        = 0x0050   # 32 bit complex
    T_PCPLX32       = 0x0150   # 16 bit pointer to 32 bit complex
    T_PFCPLX32      = 0x0250   # 16:16 far pointer to 32 bit complex
    T_PHCPLX32      = 0x0350   # 16:16 huge pointer to 32 bit complex
    T_32PCPLX32     = 0x0450   # 32 bit pointer to 32 bit complex
    T_32PFCPLX32    = 0x0550   # 16:32 pointer to 32 bit complex
    T_64PCPLX32     = 0x0650   # 64 bit pointer to 32 bit complex

#      64 bit complex types

    T_CPLX64        = 0x0051   # 64 bit complex
    T_PCPLX64       = 0x0151   # 16 bit pointer to 64 bit complex
    T_PFCPLX64      = 0x0251   # 16:16 far pointer to 64 bit complex
    T_PHCPLX64      = 0x0351   # 16:16 huge pointer to 64 bit complex
    T_32PCPLX64     = 0x0451   # 32 bit pointer to 64 bit complex
    T_32PFCPLX64    = 0x0551   # 16:32 pointer to 64 bit complex
    T_64PCPLX64     = 0x0651   # 64 bit pointer to 64 bit complex


#      80 bit complex types

    T_CPLX80        = 0x0052   # 80 bit complex
    T_PCPLX80       = 0x0152   # 16 bit pointer to 80 bit complex
    T_PFCPLX80      = 0x0252   # 16:16 far pointer to 80 bit complex
    T_PHCPLX80      = 0x0352   # 16:16 huge pointer to 80 bit complex
    T_32PCPLX80     = 0x0452   # 32 bit pointer to 80 bit complex
    T_32PFCPLX80    = 0x0552   # 16:32 pointer to 80 bit complex
    T_64PCPLX80     = 0x0652   # 64 bit pointer to 80 bit complex

#      128 bit complex types

    T_CPLX128       = 0x0053   # 128 bit complex
    T_PCPLX128      = 0x0153   # 16 bit pointer to 128 bit complex
    T_PFCPLX128     = 0x0253   # 16:16 far pointer to 128 bit complex
    T_PHCPLX128     = 0x0353   # 16:16 huge pointer to 128 bit real
    T_32PCPLX128    = 0x0453   # 32 bit pointer to 128 bit complex
    T_32PFCPLX128   = 0x0553   # 16:32 pointer to 128 bit complex
    T_64PCPLX128    = 0x0653   # 64 bit pointer to 128 bit complex

#      boolean types

    T_BOOL08        = 0x0030   # 8 bit boolean
    T_PBOOL08       = 0x0130   # 16 bit pointer to  8 bit boolean
    T_PFBOOL08      = 0x0230   # 16:16 far pointer to  8 bit boolean
    T_PHBOOL08      = 0x0330   # 16:16 huge pointer to  8 bit boolean
    T_32PBOOL08     = 0x0430   # 32 bit pointer to 8 bit boolean
    T_32PFBOOL08    = 0x0530   # 16:32 pointer to 8 bit boolean
    T_64PBOOL08     = 0x0630   # 64 bit pointer to 8 bit boolean

    T_BOOL16        = 0x0031   # 16 bit boolean
    T_PBOOL16       = 0x0131   # 16 bit pointer to 16 bit boolean
    T_PFBOOL16      = 0x0231   # 16:16 far pointer to 16 bit boolean
    T_PHBOOL16      = 0x0331   # 16:16 huge pointer to 16 bit boolean
    T_32PBOOL16     = 0x0431   # 32 bit pointer to 18 bit boolean
    T_32PFBOOL16    = 0x0531   # 16:32 pointer to 16 bit boolean
    T_64PBOOL16     = 0x0631   # 64 bit pointer to 18 bit boolean

    T_BOOL32        = 0x0032   # 32 bit boolean
    T_PBOOL32       = 0x0132   # 16 bit pointer to 32 bit boolean
    T_PFBOOL32      = 0x0232   # 16:16 far pointer to 32 bit boolean
    T_PHBOOL32      = 0x0332   # 16:16 huge pointer to 32 bit boolean
    T_32PBOOL32     = 0x0432   # 32 bit pointer to 32 bit boolean
    T_32PFBOOL32    = 0x0532   # 16:32 pointer to 32 bit boolean
    T_64PBOOL32     = 0x0632   # 64 bit pointer to 32 bit boolean

    T_BOOL64        = 0x0033   # 64 bit boolean
    T_PBOOL64       = 0x0133   # 16 bit pointer to 64 bit boolean
    T_PFBOOL64      = 0x0233   # 16:16 far pointer to 64 bit boolean
    T_PHBOOL64      = 0x0333   # 16:16 huge pointer to 64 bit boolean
    T_32PBOOL64     = 0x0433   # 32 bit pointer to 64 bit boolean
    T_32PFBOOL64    = 0x0533   # 16:32 pointer to 64 bit boolean
    T_64PBOOL64     = 0x0633   # 64 bit pointer to 64 bit boolean

#      ???

    T_NCVPTR        = 0x01f0   # CV Internal type for created near pointers
    T_FCVPTR        = 0x02f0   # CV Internal type for created far pointers
    T_HCVPTR        = 0x03f0   # CV Internal type for created huge pointers
    T_32NCVPTR      = 0x04f0   # CV Internal type for created near 32-bit pointers
    T_32FCVPTR      = 0x05f0   # CV Internal type for created far 32-bit pointers
    T_64NCVPTR      = 0x06f0   # CV Internal type for created near 64-bit pointers


POINTER_TO_MEMBER_TYPE_NAMES = [
    "Not specified",
    "Data, Single inheritance",
    "Data, Multiple inheritance",
    "Data, Virtual inheritance",
    "Data, Most general",
    "Function, Single inheritance",
    "Function, Multiple inheritance",
    "Function, Virtual inheritance",
    "Function, Most general",
]


supports_query_udt = False
def show_udt_type_id(name: str) -> int | None:
    raise NotImplementedError

def get_numeric_string(number: TpiStream.Numeric):
    if number.tag < 0x8000:
        return f"{number.tag}"
    match number.tag:
        case TpiStream.Leaf.LeafType.lf_char:
            return f"(LF_CHAR) {number.char_}(0x{(number.char_ + 0x100) % 0x100:02X})"
        case TpiStream.Leaf.LeafType.lf_short:
            return f"(LF_SHORT) {number.short_}"
        case TpiStream.Leaf.LeafType.lf_ushort:
            return f"(LF_USHORT) {number.ushort}"
        case TpiStream.Leaf.LeafType.lf_long:
            return f"(LF_LONG) {number.long}"
        case TpiStream.Leaf.LeafType.lf_ulong:
            return f"(LF_ULONG) {number.ulong}"
        case TpiStream.Leaf.LeafType.lf_real32:
            return f"(LF_REAL32) {number.real32}"
        case TpiStream.Leaf.LeafType.lf_real64:
            return f"(LF_REAL64) {number.real64}"
        case TpiStream.Leaf.LeafType.lf_real80:
            return f"(LF_REAL80) {number.real80}"
        case TpiStream.Leaf.LeafType.lf_real128:
            return f"(LF_REAL128) {number.real128}"
        case TpiStream.Leaf.LeafType.lf_quadword:
            return f"(LF_QUADWORD) {number.quadword}"
        case TpiStream.Leaf.LeafType.lf_uquadword:
            return f"(LF_UQUADWORD) {number.uquadword}"
        case TpiStream.Leaf.LeafType.lf_real48:
            return f"LF_REAL48"
        case TpiStream.Leaf.LeafType.lf_complex32:
            return f"(LF_COMPLEX32) ({number.complex32.real}, {number.complex32.complex})"
        case TpiStream.Leaf.LeafType.lf_complex64:
            return f"(LF_COMPLEX64) ({number.complex64.real}, {number.complex64.complex})"
        case TpiStream.Leaf.LeafType.lf_complex80:
            # FIXME
            return f"(LF_COMPLEX80) ({number.complex80.real}, {number.complex80.complex})"
        case TpiStream.Leaf.LeafType.lf_complex128:
            return f"(LF_COMPLEX128)"
        case TpiStream.Leaf.LeafType.lf_varstring:
            txt = "".join(f"0x{v:2X} " for v in number.varstring.text)
            return f"(LF_VARSTRING) {number.varstring.len} {txt}"
        case TpiStream.Leaf.LeafType.lf_octword:
            return f"(LF_OCTWORD)"
        case TpiStream.Leaf.LeafType.lf_uoctword:
            return f"(LF_UOCTWORD)"
        case TpiStream.Leaf.LeafType.lf_decimal:
            # (-1 if sign & 0x80 else 1) * (hi32 << 64 | lo64) * (10 ** scale)
            d = decimal.Decimal(number.decimal.hi32 << 64 | number.decimal.lo64).scaleb(-number.decimal.scale)
            if number.decimal.sign & 0x80:
                d = -d
            return f"(LF_DECIMAL) {d}"
        case TpiStream.Leaf.LeafType.lf_date:
            # FIXME (double, number of days since 1899-12-30)
            return f"(LF_DATE)"
        case TpiStream.Leaf.LeafType.lf_utf8string:
            # FIXME
            return f"(LF_UTF8STRING) {number.varstring.utf8string}"
        case TpiStream.Leaf.LeafType.lf_real16:
            return f"(LF_REAL16)"
        case _:
            raise ValueError(number.tag)

def print_class_properties(props: int):
    items_on_line = 0
    def print_props(text: str):
        nonlocal items_on_line
        if items_on_line == 4:
            print("\n\t\t", end="")
            items_on_line = 0
        print(text, end="")
        items_on_line += 1
    if props & ClassProperties.PACKED:
        print_props("PACKED, ")
    if props & ClassProperties.CTOR:
        print_props("CONSTRUCTOR, ")
    if props & ClassProperties.OVLOPS:
        print_props("OVERLOAD, ")
    if props & ClassProperties.ISNESTED:
        print_props("NESTED, ")
    if props & ClassProperties.SCOPED:
        print_props("LOCAL, ")
    if props & ClassProperties.CNESTED:
        print_props("CONTAINS NESTED, ")
    if props & ClassProperties.OPASSIGN:
        print_props("OVERLOADED ASSIGNMENT, ")
    if props & ClassProperties.OPCAST:
        print_props("CASTING, ")
    if props & ClassProperties.FWDREF:
        print_props("FORWARD REF, ")
    if props & ClassProperties.SEALED:
        print_props("SEALED, ")
    if props & ClassProperties.INTRINSIC:
        print_props("INTRINSIC TYPE, ")
    if props & ClassProperties.HFA:
        hfa = (props & ClassProperties.HFA.value) >> 11
        match hfa:
            case 1: print_props("HFA float, ")  # CV_HFA_float
            case 2: print_props("HFA double, ") # CV_HFA_double
            case 3: print_props("HFA other, ")  # CV_HFA_other
    if props & ClassProperties.MOCOM:
        mocom = (props & ClassProperties.HFA.value) >> 14
        match mocom:
            case 1: print_props("REF")
            case 2: print_props("VALUE")
            case 3: print_props("INTERFACE")

def get_c7_type_name(type_id: int) -> str:
    """
    SzNameC7Type
    """
    if type_id >= 0x1000:
        if type_id > 0xffff:
            return f"0x{type_id:8X}"
        else:
            return f"0x{type_id:4X}"
    try:
        type_value = C7TypeEnum(type_id)
        return f"{type_value.name}({type_id:04X})"
    except ValueError:
        return "???"

def get_call_convention_name(v: int) -> str:
    try:
        return CALL_CONVENTION_NAMES[v]
    except IndexError:
        return "???"


def get_function_attribute_name(attr) -> str:
    if attr & FunctionFlags.CXXRETURNUDT:
        return "return UDT (C++ style)"
    if attr & FunctionFlags.CTOR:
        return "instance constructor"
    if attr & FunctionFlags.CTORVBASE:
        return "instance constructor of a class with virtual base"
    if attr & FunctionFlags.UNUSED:
        return "****Warning**** unused field non-zero!"
    return "none"


CLASS_FIELD_ACCES_NAMES = [
    "none",
    "private",
    "protected",
    "public",
]

CLASS_FIELD_METHOD_PROP = [
    "VANILLA",
    "VIRTUAL",
    "STATIC",
    "FRIEND",
    "INTRODUCING VIRTUAL",
    "PURE VIRTUAL",
    "PURE INTRO",
]

def print_class_field_attributes(attr, b: bool) -> None:
    print(f"{CLASS_FIELD_ACCES_NAMES[attr & ClassFieldAttribute.ACCESS.value]}, ", end="")
    if b:
        print(f"{CLASS_FIELD_METHOD_PROP[(attr & 0b11100) >> 2]}, ", end="")
        if attr & ClassFieldAttribute.PSEUDO.value:
            print("(pseudo), ", end="")
        if attr & ClassFieldAttribute.COMPGENX.value:
            print("(compgenx), ", end="")
        if attr & ClassFieldAttribute.SEALED.value:
            print("(sealed), ", end="")
    if attr & ClassFieldAttribute.NOINHERIT.value:
        print("(noinherit), ", end="")
    if attr & ClassFieldAttribute.NOCONSTRUCT.value:
        print("(noconstruct), ", end="")


def dump_tpi(tpi: TpiStream):
    print()
    print("*** TYPES")
    print()
    dump_cvstream(tpi, None)


def dump_ipi(tpi: TpiStream, name_offset_to_name: dict[int, str]):
    print()
    print("*** IDs")
    print()
    dump_cvstream(tpi, name_offset_to_name)

def dump_cvstream(tpi: TpiStream, name_offset_to_name: dict[int, str] | None):

    for tpi_id, record in enumerate(tpi.records, tpi.header.ti_min):
        print(f"0x{tpi_id:04x} : Length = {record.record_size}, Leaf = 0x{record.leaf.type:04x} {record.leaf.type.name.upper()}", end="")
        if record.record_size < 2:
            assert record.record_size >= 2
        match record.leaf.type:
            case TpiStream.Leaf.LeafType.lf_fieldlist_16t:
                print()
                for item_i, item in enumerate(record.leaf.body.items):
                    print(f"\tlist[{item_i}] = ", end="")
                    match item.type:
                        case TpiStream.Leaf.LeafType.lf_enumerate_st:
                            print("LF_ENUMERATE, ", end="")  # print(f"{item.type.name.upper()}, ", end="") #
                            print(f"{CLASS_ACCESS_ATTRIBUTE_NAMES[item.element.attributes & ClassFieldAttribute.ACCESS]}, ", end="")
                            if item.element.attributes & ClassFieldAttribute.NOINHERIT:
                                print("(noinherit), ", end="")
                            if item.element.attributes & ClassFieldAttribute.NOCONSTRUCT:
                                print("(noconstruct), ", end="")
                            print(f"value = {get_numeric_string(item.element.value)}, ", end="")
                            print(f"name = '{item.element.name.text}'")
                        case TpiStream.Leaf.LeafType.lf_bclass_16t:
                            print("LF_BCLASS_16t, ", end="")
                            print_class_field_attributes(item.element.attr, False)
                            print(f"type = {get_c7_type_name(item.element.index)}", end="")
                            print(f", offset = {get_numeric_string(item.element.offset)}")
                        case TpiStream.Leaf.LeafType.lf_nesttype_16t:
                            print("LF_NESTTYPE_16t, ", end="")
                            print(f"type = {get_c7_type_name(item.element.index)}, ", end="")
                            print(item.element.name.text)
                        case TpiStream.Leaf.LeafType.lf_method_16t:
                            print("LF_METHOD_16t, ", end="")
                            print(f"count = {item.element.count}, ", end="")
                            print(f"list = {get_c7_type_name(item.element.m_list)}, ", end="")
                            print(f"name = '{item.element.name.text}'")
                        case TpiStream.Leaf.LeafType.lf_onemethod_16t:
                            print("LF_ONEMETHOD_16t, ", end="")
                            print_class_field_attributes(item.element.attr, True)
                            print(f"index = {get_c7_type_name(item.element.index)}, ", end="")
                            if hasattr(item.element, "vfptr_offset"):
                                print(f"vfptr offest = {item.element.vfptr_offset}, ", end="")
                            print(f"name = '{item.element.name.text}'")
                        case TpiStream.Leaf.LeafType.lf_member_16t:
                            print("LF_MEMBER_16t, ", end="")
                            print_class_field_attributes(item.element.attr, False)
                            print(f"type = {get_c7_type_name(item.element.index)}, ", end="")
                            print(f"offset = {get_numeric_string(item.element.offset)}")
                            print(f"\t\tmember name = '{item.element.name.text}'")
                        case TpiStream.Leaf.LeafType.lf_vfunctab_16t:
                            print("LF_VFUNCTAB_16t, ", end="")
                            print(f"type = {get_c7_type_name(item.element.type)}")
                        case TpiStream.Leaf.LeafType.lf_stmember_16t:
                            print("LF_STATICMEMBER_16t, ", end="")
                            print_class_field_attributes(item.element.attr, False)
                            print(f"type = {get_c7_type_name(item.element.index)}", end="")
                            # FIXME: add new line
                            print(f"\t\tmember name = '{item.element.name.text}'", end="")
                            print()
                        case TpiStream.Leaf.LeafType.lf_vbclass_16t:
                            print("LF_VBCLASS_16t, ", end="")
                            print_class_field_attributes(item.element.attr, False)
                            # FIXME: add new line
                            print(f"direct base type = {get_c7_type_name(item.element.index)}")
                            print(f"\t\tvirtual base ptr = {get_c7_type_name(item.element.vbptr)}, ", end="")
                            print(f"vboff = {get_numeric_string(item.element.vbpoff)}, ", end="")
                            print(f"vbind = {get_numeric_string(item.element.vbind)}", end="")
                            print()
                        case TpiStream.Leaf.LeafType.lf_ivbclass_16t:
                            print("LF_IVBCLASS_16t, ", end="")
                            print_class_field_attributes(item.element.attr, False)
                            # FIXME: add new line
                            print(f"indirect base type = {get_c7_type_name(item.element.index)}")
                            print(f"\t\tvirtual base ptr = {get_c7_type_name(item.element.vbptr)}, ", end="")
                            print(f"vboff = {get_numeric_string(item.element.vbpoff)}, ", end="")
                            print(f"vbind = {get_numeric_string(item.element.vbind)}", end="")
                            print()
                        case TpiStream.Leaf.LeafType.lf_index_16t:
                            # print("LF_INDEX, ", end="")
                            print(f"Type Index = {get_c7_type_name(item.element.index)}")
                        case _:
                            raise ValueError(item.type)
            case TpiStream.Leaf.LeafType.lf_fieldlist:
                print()
                for item_i, item in enumerate(record.leaf.body.items):
                    print(f"\tlist[{item_i}] = ", end="")
                    match item.type:
                        case TpiStream.Leaf.LeafType.lf_enumerate | TpiStream.Leaf.LeafType.lf_enumerate_st:
                            print("LF_ENUMERATE, ", end="")  # print(f"{item.type.name.upper()}, ", end="") #
                            print(f"{CLASS_ACCESS_ATTRIBUTE_NAMES[item.element.attributes & ClassFieldAttribute.ACCESS]}, ", end="")
                            if item.element.attributes & ClassFieldAttribute.NOINHERIT:
                                print("(noinherit), ", end="")
                            if item.element.attributes & ClassFieldAttribute.NOCONSTRUCT:
                                print("(noconstruct), ", end="")
                            print(f"value = {get_numeric_string(item.element.value)}, ", end="")
                            print(f"name = '{item.element.name.text}'")
                        case TpiStream.Leaf.LeafType.lf_bclass | TpiStream.Leaf.LeafType.lf_binterface:
                            print("LF_BCLASS, " if item.type == TpiStream.Leaf.LeafType.lf_bclass else "LF_INTERFACE, ", end="")
                            print_class_field_attributes(item.element.attr, False)
                            print(f"type = {get_c7_type_name(item.element.index)}", end="")
                            print(f", offset = {get_numeric_string(item.element.offset)}")
                        case TpiStream.Leaf.LeafType.lf_nesttype | TpiStream.Leaf.LeafType.lf_nesttype_st:
                            print("LF_NESTTYPE, ", end="")
                            print(f"type = {get_c7_type_name(item.element.index)}, ", end="")
                            print(item.element.name.text)
                            if item.element.pad0 != 0:
                                print("***Warning, pad bytes are non-zero!")
                        case TpiStream.Leaf.LeafType.lf_method | TpiStream.Leaf.LeafType.lf_method_st:
                            print("LF_METHOD, ", end="")
                            print(f"count = {item.element.count}, ", end="")
                            print(f"list = {get_c7_type_name(item.element.m_list)}, ", end="")
                            print(f"name = '{item.element.name.text}'")
                        case TpiStream.Leaf.LeafType.lf_onemethod | TpiStream.Leaf.LeafType.lf_onemethod_st:
                            print("LF_ONEMETHOD, ", end="")
                            print_class_field_attributes(item.element.attr, True)
                            print(f"index = {get_c7_type_name(item.element.index)}, ", end="")
                            if hasattr(item.element, "vfptr_offset"):
                                print()
                                print(f"\t\tvfptr offest = {item.element.vfptr_offset}, ", end="")
                            print(f"name = '{item.element.name.text}'")
                        case TpiStream.Leaf.LeafType.lf_member | TpiStream.Leaf.LeafType.lf_member_st:
                            print("LF_MEMBER, ", end="")
                            print_class_field_attributes(item.element.attr, False)
                            print(f"type = {get_c7_type_name(item.element.index)}, ", end="")
                            print(f"offset = {get_numeric_string(item.element.offset)}")
                            print(f"\t\tmember name = '{item.element.name.text}'")
                        case TpiStream.Leaf.LeafType.lf_vfunctab:
                            print("LF_VFUNCTAB, ", end="")
                            print(f"type = {get_c7_type_name(item.element.type)}")
                        case TpiStream.Leaf.LeafType.lf_stmember | TpiStream.Leaf.LeafType.lf_stmember_st:
                            print("LF_STATICMEMBER, ", end="")
                            print_class_field_attributes(item.element.attr, False)
                            print(f"type = {get_c7_type_name(item.element.index)}", end="")
                            # FIXME: add new line
                            print(f"\t\tmember name = '{item.element.name.text}'", end="")
                            print()
                        case TpiStream.Leaf.LeafType.lf_index:
                            print("LF_INDEX, ", end="")
                            print(f"Type Index = {get_c7_type_name(item.element.index)}")
                            if item.element.padding != 0:
                                print("***Warning, pad bytes are non-zero!")
                            print()
                        # case TpiStream.Leaf.LeafType.lf_vbclass:
                        #     print("LF_VBCLASS, ", end="")
                        #     print_class_field_attributes(item.element.attr, False)
                        #     # FIXME: add new line
                        #     print(f"direct base type = {get_c7_type_name(item.element.index)}")
                        #     print(f"\t\tvirtual base ptr = {get_c7_type_name(item.element.vbptr)}, ", end="")
                        #     print(f"vboff = {get_numeric_string(item.element.vbpoff)}, ", end="")
                        #     print(f"vbind = {get_numeric_string(item.element.vbind)}", end="")
                        #     print()
                        # case TpiStream.Leaf.LeafType.lf_ivbclass_16t:
                        #     print("LF_IVBCLASS_16t, ", end="")
                        #     print_class_field_attributes(item.element.attr, False)
                        #     # FIXME: add new line
                        #     print(f"indirect base type = {get_c7_type_name(item.element.index)}")
                        #     print(f"\t\tvirtual base ptr = {get_c7_type_name(item.element.vbptr)}, ", end="")
                        #     print(f"vboff = {get_numeric_string(item.element.vbpoff)}, ", end="")
                        #     print(f"vbind = {get_numeric_string(item.element.vbind)}", end="")
                        #     print()
                        case _:
                            raise ValueError(item.type, repr(item.type))
            case TpiStream.Leaf.LeafType.lf_enum_16t:
                print()
                print(f"\t# members = {record.leaf.body.count}, ", end="")
                print(f" type = {get_c7_type_name(record.leaf.body.utype)}", end="")
                print(f" field list type 0x{record.leaf.body.field:04x}")
                print_class_properties(record.leaf.body.property)
                print(f"\tenum name = {record.leaf.body.name.text}", end="")
                if supports_query_udt:
                    udt = show_udt_type_id(record.leaf.body.name.text)
                    if udt is not None:
                        print(f", UDT(0x{udt:08x}", end="")
                print()
            case TpiStream.Leaf.LeafType.lf_enum | TpiStream.Leaf.LeafType.lf_enum_st:
                print()
                print(f"\t# members = {record.leaf.body.count}, ", end="")
                print(f" type = {get_c7_type_name(record.leaf.body.utype)}", end="")
                print(f" field list type 0x{record.leaf.body.field:04x}")
                print_class_properties(record.leaf.body.property)
                print(f"\tenum name = {record.leaf.body.name.text}", end="")
                if supports_query_udt:
                    udt = show_udt_type_id(record.leaf.body.name.text)
                    if udt is not None:
                        print(f", UDT(0x{udt:08x}", end="")
                print()
            case TpiStream.Leaf.LeafType.lf_structure_16t | TpiStream.Leaf.LeafType.lf_class_16t:
                print()
                # match record.leaf.type:
                #     case TpiStream.Leaf.LeafType.lf_structure_16t:
                #         print("LF_STRUCTURE\n", end="")
                #     case _:
                #         raise ValueError
                print(f"\t# members = {record.leaf.body.count}, ", end="")
                print(f" field list type 0x{record.leaf.body.field:04x}, ", end="")
                print_class_properties(record.leaf.body.property)
                print()
                print(f"\tDerivation list type 0x{record.leaf.body.derived:04x}, ", end="")
                print(f"VT shape type 0x{record.leaf.body.vshape:04x}")
                print(f"\tSize = {get_numeric_string(record.leaf.body.size)},", end="")
                print(f" class name = {record.leaf.body.name.text}", end="")
                # if record.leaf.body.property & 0x20: # hasuniquename
                #     print(f", unique name = {record.leaf.body.unique_name.text}", end="")
                if supports_query_udt:
                    udt = show_udt_type_id(record.leaf.body.name.text)
                    if udt is not None:
                        print(f", UDT(0x{udt:08x}", end="")
                print()
            case TpiStream.Leaf.LeafType.lf_class_st | TpiStream.Leaf.LeafType.lf_structure_st | TpiStream.Leaf.LeafType.lf_class | TpiStream.Leaf.LeafType.lf_structure | TpiStream.Leaf.LeafType.lf_interface:
                # match record.leaf.type:
                #     case TpiStream.Leaf.LeafType.lf_class:
                #         print("LF_CLASS\n", end="")
                #     case TpiStream.Leaf.LeafType.lf_structure:
                #         print("LF_STRUCTURE\n", end="")
                #     case _:
                #         print("LF_INTERFACE\n", end="")
                print()
                print(f"\t# members = {record.leaf.body.count}, ", end="")
                print(f" field list type 0x{record.leaf.body.field:04x}, ", end="")
                print_class_properties(record.leaf.body.property)
                print()
                print(f"\tDerivation list type 0x{record.leaf.body.derived:04x}, ", end="")
                print(f"VT shape type 0x{record.leaf.body.vshape:04x}")
                print(f"\tSize = {get_numeric_string(record.leaf.body.size)},", end="")
                print(f" class name = {record.leaf.body.name.text}", end="")
                if record.leaf.body.property & 0x20: # hasuniquename
                    print(f", unique name = {record.leaf.body.unique_name.text}", end="")
                if supports_query_udt:
                    udt = show_udt_type_id(record.leaf.body.name.text)
                    if udt is not None:
                        print(f", UDT(0x{udt:08x}", end="")
                print()
            case TpiStream.Leaf.LeafType.lf_array_16t:
                print()
                print(f"\tElement type = {get_c7_type_name(record.leaf.body.elemtype)}")
                print(f"\tIndex type = {get_c7_type_name(record.leaf.body.idxtype)}")
                print(f"\tlength = {get_numeric_string(record.leaf.body.length)}")
                print(f"\tName = {record.leaf.body.name.text}")
            case TpiStream.Leaf.LeafType.lf_array_st | TpiStream.Leaf.LeafType.lf_array:
                print()
                print(f"\tElement type = {get_c7_type_name(record.leaf.body.elemtype)}")
                print(f"\tIndex type = {get_c7_type_name(record.leaf.body.idxtype)}")
                print(f"\tlength = {get_numeric_string(record.leaf.body.length)}")
                print(f"\tName = {record.leaf.body.name.text}")
            case TpiStream.Leaf.LeafType.lf_arglist_16t:
                print(f" argument count = {record.leaf.body.count}")
                for arg_i, arg in enumerate(record.leaf.body.arg):
                    print(f"\tlist[{arg_i}] = {get_c7_type_name(arg)}")
            case TpiStream.Leaf.LeafType.lf_arglist:
                print(f" argument count = {record.leaf.body.count}")
                for arg_i, arg in enumerate(record.leaf.body.arg):
                    print(f"\tlist[{arg_i}] = {get_c7_type_name(arg)}")
            case TpiStream.Leaf.LeafType.lf_procedure_16t:
                print()
                print(f"\tReturn type = {get_c7_type_name(record.leaf.body.rvtype)}. ", end="")
                print(f"Call type = {get_call_convention_name(record.leaf.body.calltype)}")
                print(f"\tFunc attr = {get_function_attribute_name(record.leaf.body.funcattr)}")
                print(f"\t# Parms = {record.leaf.body.parmcount}, ", end="")
                print(f"Arg list type = 0x{record.leaf.body.arglist:x}")
            case TpiStream.Leaf.LeafType.lf_procedure:
                print()
                print(f"\tReturn type = {get_c7_type_name(record.leaf.body.rvtype)}. ", end="")
                print(f"Call type = {get_call_convention_name(record.leaf.body.calltype)}")
                print(f"\tFunc attr = {get_function_attribute_name(record.leaf.body.funcattr)}")
                print(f"\t# Parms = {record.leaf.body.parmcount}, ", end="")
                print(f"Arg list type = 0x{record.leaf.body.arglist:x}")
            case TpiStream.Leaf.LeafType.lf_pointer_16t:
                print()
                print("\t", end="")
                if record.leaf.body.attr & Pointer16Attribute.ISVOLATILE:
                    print("volatile ", end="")
                if record.leaf.body.attr & Pointer16Attribute.ISCONST:
                    print("const ", end="")
                if record.leaf.body.attr & Pointer16Attribute.ISUNALIGNED:
                    print("__unaligned ", end="")
                ptrmode = (record.leaf.body.attr & Pointer16Attribute.PTRMODE.value) >> 5
                ptrtype = (record.leaf.body.attr & Pointer16Attribute.PTRTYPE.value) >> 0
                print(f"{POINTER_MODE_NAMES[ptrmode]} ({POINTER_TYPE_NAMES[ptrtype]})", end="")
                if record.leaf.body.attr & Pointer16Attribute.ISFLAT32:
                    print(" 16:32", end="")
                # print(f", Size: {0}", end="")  # not available in LF_POINTER_16t (see LF_POINTER)
                print()
                print(f"\tElement type : {get_c7_type_name(record.leaf.body.utype)}", end="")
                if (record.leaf.body.attr & Pointer16Attribute.PTRMODE.value) >> 5:
                    match ptrmode:
                        case PointerMode.CV_PTR_MODE_PMEM | PointerMode.CV_PTR_MODE_PMFUNC:
                            print(f", Containing class = {get_c7_type_name(record.leaf.body.pm.pmclass)}, ")
                            print(f"\t\tType of pointer to member = {POINTER_TO_MEMBER_TYPE_NAMES[record.leaf.body.pm.pmenum]}", end="")
                else:
                    match PointerType(ptrtype):
                        case PointerType.CV_PTR_BASE_SEG:       raise NotImplementedError
                        case PointerType.CV_PTR_BASE_VAL:       raise NotImplementedError
                        case PointerType.CV_PTR_BASE_SEGVAL:    raise NotImplementedError
                        case PointerType.CV_PTR_BASE_ADDR:      raise NotImplementedError
                        case PointerType.CV_PTR_BASE_SEGADDR:   raise NotImplementedError
                        case PointerType.CV_PTR_BASE_TYPE:      raise NotImplementedError
                        case PointerType.CV_PTR_BASE_SELF:      raise NotImplementedError
                print()
            case TpiStream.Leaf.LeafType.lf_pointer:
                print()
                print("\t", end="")
                if record.leaf.body.attr & PointerAttribute.ISVOLATILE:
                    print("volatile ", end="")
                if record.leaf.body.attr & PointerAttribute.ISCONST:
                    print("const ", end="")
                if record.leaf.body.attr & PointerAttribute.ISUNALIGNED:
                    print("__unaligned ", end="")
                if record.leaf.body.attr & PointerAttribute.ISRESTRICT:
                    print("__restrict ", end="")
                ptrmode = (record.leaf.body.attr & PointerAttribute.PTRMODE.value) >> 5
                ptrtype = (record.leaf.body.attr & PointerAttribute.PTRTYPE.value) >> 0
                print(f"{POINTER_MODE_NAMES[ptrmode]} ({POINTER_TYPE_NAMES[ptrtype]})", end="")
                size = (record.leaf.body.attr & PointerAttribute.SIZE.value) >> 13
                print(f", Size: {size}", end="")
                if record.leaf.body.attr & PointerAttribute.ISFLAT32:
                    print(" 16:32", end="")
                if record.leaf.body.attr & PointerAttribute.ISMOCOM:
                    print(" MoCOM", end="")
                print()
                print(f"\tElement type : {get_c7_type_name(record.leaf.body.utype)}", end="")
                if ptrmode != 0:
                    match ptrmode:
                        case PointerMode.CV_PTR_MODE_PMEM | PointerMode.CV_PTR_MODE_PMFUNC:
                            print(f", Containing class = {get_c7_type_name(record.leaf.body.pm.pmclass)}, ")
                            print(f"\tType of pointer to member = {POINTER_TO_MEMBER_TYPE_NAMES[record.leaf.body.pm.pmenum]}", end="")
                else:
                    match PointerType(ptrtype):
                        case PointerType.CV_PTR_BASE_SEG:       raise NotImplementedError
                        case PointerType.CV_PTR_BASE_VAL:       raise NotImplementedError
                        case PointerType.CV_PTR_BASE_SEGVAL:    raise NotImplementedError
                        case PointerType.CV_PTR_BASE_ADDR:      raise NotImplementedError
                        case PointerType.CV_PTR_BASE_SEGADDR:   raise NotImplementedError
                        case PointerType.CV_PTR_BASE_TYPE:      raise NotImplementedError
                        case PointerType.CV_PTR_BASE_SELF:      raise NotImplementedError
                print()
            case TpiStream.Leaf.LeafType.lf_modifier_16t:
                print()
                print(f"\t", end="")
                if record.leaf.body.attr & Modifier.MOD_const:
                    print("const, ", end="")
                if record.leaf.body.attr & Modifier.MOD_volatile:
                    print("volatile, ", end="")
                if record.leaf.body.attr & Modifier.MOD_unaligned:
                    print("__unaligned, ", end="")
                print(f"modifies type {get_c7_type_name(record.leaf.body.type)}")
            case TpiStream.Leaf.LeafType.lf_modifier:
                print()
                print(f"\t", end="")
                if record.leaf.body.attr & Modifier.MOD_const:
                    print("const, ", end="")
                if record.leaf.body.attr & Modifier.MOD_volatile:
                    print("volatile, ", end="")
                if record.leaf.body.attr & Modifier.MOD_unaligned:
                    print("__unaligned, ", end="")
                print(f"modifies type {get_c7_type_name(record.leaf.body.type)}")
            case TpiStream.Leaf.LeafType.lf_mfunction_16t:
                print()
                print(f"\tReturn type = {get_c7_type_name(record.leaf.body.rvtype)}, ", end="")
                print(f"Class type = {get_c7_type_name(record.leaf.body.classtype)}, ", end="")
                print(f"This type = {get_c7_type_name(record.leaf.body.thistype)}, ")
                print(f"\tCall type = {CALL_CONVENTION_NAMES[record.leaf.body.calltype]}, ", end="")
                print(f"Func attr = {get_function_attribute_name(record.leaf.body.funcattr)}")
                print(f"\tParms = {record.leaf.body.parmcount}, ", end="")
                print(f"Arg list type = 0x{record.leaf.body.arglist:04x}, ", end="")
                print(f"This adjust = {record.leaf.body.thisadjust:x}")
            case TpiStream.Leaf.LeafType.lf_mfunction:
                print()
                print(f"\tReturn type = {get_c7_type_name(record.leaf.body.rvtype)}, ", end="")
                print(f"Class type = {get_c7_type_name(record.leaf.body.classtype)}, ", end="")
                print(f"This type = {get_c7_type_name(record.leaf.body.thistype)}, ")
                print(f"\tCall type = {CALL_CONVENTION_NAMES[record.leaf.body.calltype]}, ", end="")
                print(f"Func attr = {get_function_attribute_name(record.leaf.body.funcattr)}")
                print(f"\tParms = {record.leaf.body.parmcount}, ", end="")
                print(f"Arg list type = 0x{record.leaf.body.arglist:04x}, ", end="")
                print(f"This adjust = {record.leaf.body.thisadjust:x}")
            case TpiStream.Leaf.LeafType.lf_methodlist_16t:
                print()
                for i, item in enumerate(record.leaf.body.items):
                    print(f"\tlist[{i}] = ", end="")
                    print_class_field_attributes(item.attr, True)
                    print(f"{get_c7_type_name(item.index)}, ", end="")
                    if hasattr(item, "vfptr_offset"):
                        print(f" vfptr offset = {item.vfptr_offset}", end="")
                    print()
            case TpiStream.Leaf.LeafType.lf_methodlist:
                print()
                for i, item in enumerate(record.leaf.body.items):
                    print(f"\tlist[{i}] = ", end="")
                    print_class_field_attributes(item.attr, True)
                    print(f"{get_c7_type_name(item.index)}, ", end="")
                    if hasattr(item, "vfptr_offset"):
                        print(f" vfptr offset = {item.vfptr_offset}", end="")
                    if item.pad0 != 0:
                        print("***Warning, pad bytes are non-zero!")
                    print()
            case TpiStream.Leaf.LeafType.lf_vtshape:
                print()
                print(f"\tNumber of entries: {record.leaf.body.count}")
                for i in range(record.leaf.body.count):
                    idx = i // 2
                    t = record.leaf.body.desc[idx >> (4 * (i % 2))] % 16
                    print(f"\t\t[{i}]: {FUNC_TYPE_NAMES[t]}")
            case TpiStream.Leaf.LeafType.lf_union_16t:
                print()
                print(f"\t# members = {record.leaf.body.count}, ", end="")
                print(f" field list type 0x{record.leaf.body.field:04x}, ", end="")
                print_class_properties(record.leaf.body.property)
                print(f"Size = {get_numeric_string(record.leaf.body.size)}")
                # FIXME: missing newline + ugly whitespace around comma
                print(f"\t,class name = {record.leaf.body.name.text}", end="")
                if supports_query_udt:
                    udt = show_udt_type_id(record.leaf.body.name.text)
                    if udt is not None:
                        print(f", UDT(0x{udt:08x}", end="")
                print()
            case TpiStream.Leaf.LeafType.lf_union | TpiStream.Leaf.LeafType.lf_union_st:
                print()
                print(f"\t# members = {record.leaf.body.count}, ", end="")
                print(f" field list type 0x{record.leaf.body.field:04x}, ", end="")
                print_class_properties(record.leaf.body.property)
                print(f"Size = {get_numeric_string(record.leaf.body.size)}", end="")
                # FIXME: missing newline + ugly whitespace around comma
                print(f"\t,class name = {record.leaf.body.name.text}", end="")
                if supports_query_udt:
                    udt = show_udt_type_id(record.leaf.body.name.text)
                    if udt is not None:
                        print(f", UDT(0x{udt:08x}", end="")
                print()
            case TpiStream.Leaf.LeafType.lf_bitfield_16t:
                print()
                print(f"\tbits = {record.leaf.body.length}, ", end="")
                print(f"starting position = {record.leaf.body.position}", end="")
                print(f", Type = {get_c7_type_name(record.leaf.body.type)}")
            case TpiStream.Leaf.LeafType.lf_bitfield:
                print()
                print(f"\tbits = {record.leaf.body.length}, ", end="")
                print(f"starting position = {record.leaf.body.position}", end="")
                print(f", Type = {get_c7_type_name(record.leaf.body.type)}")

            # TPI
            case TpiStream.Leaf.LeafType.lf_udt_mod_src_line:
                print()
                source_file = name_offset_to_name.get(record.leaf.body.src)
                if source_file is None:
                    print("Error no name")
                else:
                    print(f"\ttype = 0x{record.leaf.body.type:x}, mod={record.leaf.body.imod}, source file = {source_file}, line = {record.leaf.body.line}")
            case TpiStream.Leaf.LeafType.lf_string_id:
                print()
                print(f"\t{record.leaf.body.name}")
                if record.leaf.body.id:
                    print(f"\tList of sub string ID's = {get_c7_type_name(record.leaf.body.id)}")
                else:
                    print("\tNo sub string ID")
            case TpiStream.Leaf.LeafType.lf_substr_list:
                print()
                print(f"\tString ID's (count = {record.leaf.body.count}):", end="")
                for i in range(record.leaf.body.count):
                    print(f" {get_c7_type_name(record.leaf.body.arg[i])}", end="")
                print()
            case TpiStream.Leaf.LeafType.lf_buildinfo:
                print()
                print(f"\tString ID's (count = {record.leaf.body.count}):", end="")
                for i in range(record.leaf.body.count):
                    print(f" {get_c7_type_name(record.leaf.body.arg[i])}", end="")
                print()
            case TpiStream.Leaf.LeafType.lf_func_id:
                print()
                print(f"\tType = {get_c7_type_name(record.leaf.body.type)}\t", end="")
                if record.leaf.body.scope_id == 0:
                    print("\tScope = global\t", end="")
                else:
                    print(f"\tScope = {get_c7_type_name(record.leaf.body.scope_id)}\t", end="")
                print(record.leaf.body.name)
            case TpiStream.Leaf.LeafType.lf_mfunc_id:
                print()
                print(f"\tType = {get_c7_type_name(record.leaf.body.type)}\t", end="")
                print(f"\tParent = {get_c7_type_name(record.leaf.body.parent_type)}\t", end="")
                print(record.leaf.body.name)
            case _:
                raise ValueError(record.leaf.type, repr(record.leaf.type))
        print()
