# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
from cvdump.kaitai import numeric
from cvdump.kaitai import pascal_string
from cvdump.kaitai import strz_or_pascal
from enum import IntEnum


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class ModiStream(KaitaiStruct):

    class SymbolType(IntEnum):
        s_compile = 1
        s_register_16t = 2
        s_constant_16t = 3
        s_udt_16t = 4
        s_ssearch = 5
        s_end = 6
        s_skip = 7
        s_cvreserve = 8
        s_objname_st = 9
        s_endarg = 10
        s_coboludt_16t = 11
        s_manyreg_16t = 12
        s_return = 13
        s_entrythis = 14
        s_bprel16 = 256
        s_ldata16 = 257
        s_gdata16 = 258
        s_pub16 = 259
        s_lproc16 = 260
        s_gproc16 = 261
        s_thunk16 = 262
        s_block16 = 263
        s_with16 = 264
        s_label16 = 265
        s_cexmodel16 = 266
        s_vftable16 = 267
        s_regrel16 = 268
        s_bprel32_16t = 512
        s_ldata32_16t = 513
        s_gdata32_16t = 514
        s_pub32_16t = 515
        s_lproc32_16t = 516
        s_gproc32_16t = 517
        s_thunk32_st = 518
        s_block32_st = 519
        s_with32_st = 520
        s_label32_st = 521
        s_cexmodel32 = 522
        s_vftable32_16t = 523
        s_regrel32_16t = 524
        s_lthread32_16t = 525
        s_gthread32_16t = 526
        s_slink32 = 527
        s_lprocmips_16t = 768
        s_gprocmips_16t = 769
        s_procref_st = 1024
        s_dataref_st = 1025
        s_align = 1026
        s_lprocref_st = 1027
        s_oem = 1028
        s_ti16_max = 4096
        s_register_st = 4097
        s_constant_st = 4098
        s_udt_st = 4099
        s_coboludt_st = 4100
        s_manyreg_st = 4101
        s_bprel32_st = 4102
        s_ldata32_st = 4103
        s_gdata32_st = 4104
        s_pub32_st = 4105
        s_lproc32_st = 4106
        s_gproc32_st = 4107
        s_vftable32 = 4108
        s_regrel32_st = 4109
        s_lthread32_st = 4110
        s_gthread32_st = 4111
        s_lprocmips_st = 4112
        s_gprocmips_st = 4113
        s_frameproc = 4114
        s_compile2_st = 4115
        s_manyreg2_st = 4116
        s_lprocia64_st = 4117
        s_gprocia64_st = 4118
        s_localslot_st = 4119
        s_paramslot_st = 4120
        s_annotation = 4121
        s_gmanproc_st = 4122
        s_lmanproc_st = 4123
        s_reserved1 = 4124
        s_reserved2 = 4125
        s_reserved3 = 4126
        s_reserved4 = 4127
        s_lmandata_st = 4128
        s_gmandata_st = 4129
        s_manframerel_st = 4130
        s_manregister_st = 4131
        s_manslot_st = 4132
        s_manmanyreg_st = 4133
        s_manregrel_st = 4134
        s_manmanyreg2_st = 4135
        s_mantypref = 4136
        s_unamespace_st = 4137
        s_st_max = 4352
        s_objname = 4353
        s_thunk32 = 4354
        s_block32 = 4355
        s_with32 = 4356
        s_label32 = 4357
        s_register = 4358
        s_constant = 4359
        s_udt = 4360
        s_coboludt = 4361
        s_manyreg = 4362
        s_bprel32 = 4363
        s_ldata32 = 4364
        s_gdata32 = 4365
        s_pub32 = 4366
        s_lproc32 = 4367
        s_gproc32 = 4368
        s_regrel32 = 4369
        s_lthread32 = 4370
        s_gthread32 = 4371
        s_lprocmips = 4372
        s_gprocmips = 4373
        s_compile2 = 4374
        s_manyreg2 = 4375
        s_lprocia64 = 4376
        s_gprocia64 = 4377
        s_localslot = 4378
        s_paramslot = 4379
        s_lmandata = 4380
        s_gmandata = 4381
        s_manframerel = 4382
        s_manregister = 4383
        s_manslot = 4384
        s_manmanyreg = 4385
        s_manregrel = 4386
        s_manmanyreg2 = 4387
        s_unamespace = 4388
        s_procref = 4389
        s_dataref = 4390
        s_lprocref = 4391
        s_annotationref = 4392
        s_tokenref = 4393
        s_gmanproc = 4394
        s_lmanproc = 4395
        s_trampoline = 4396
        s_manconstant = 4397
        s_attr_framerel = 4398
        s_attr_register = 4399
        s_attr_regrel = 4400
        s_attr_manyreg = 4401
        s_sepcode = 4402
        s_local_2005 = 4403
        s_defrange_2005 = 4404
        s_defrange2_2005 = 4405
        s_section = 4406
        s_coffgroup = 4407
        s_export = 4408
        s_callsiteinfo = 4409
        s_framecookie = 4410
        s_discarded = 4411
        s_compile3 = 4412
        s_envblock = 4413
        s_local = 4414
        s_defrange = 4415
        s_defrange_subfield = 4416
        s_defrange_register = 4417
        s_defrange_framepointer_rel = 4418
        s_defrange_subfield_register = 4419
        s_defrange_framepointer_rel_full_scope = 4420
        s_defrange_register_rel = 4421
        s_lproc32_id = 4422
        s_gproc32_id = 4423
        s_lprocmips_id = 4424
        s_gprocmips_id = 4425
        s_lprocia64_id = 4426
        s_gprocia64_id = 4427
        s_buildinfo = 4428
        s_inlinesite = 4429
        s_inlinesite_end = 4430
        s_proc_id_end = 4431
        s_defrange_hlsl = 4432
        s_gdata_hlsl = 4433
        s_ldata_hlsl = 4434
        s_filestatic = 4435
        s_armswitchtable = 4441
        s_callees = 4442
        s_callers = 4443
        s_pogodata = 4444
        s_inlinesite2 = 4445
        s_heapallocsite = 4446
        s_mod_typeref = 4447
        s_ref_minipdb = 4448
        s_pdbmap = 4449
        s_gdata_hlsl32 = 4450
        s_ldata_hlsl32 = 4451
        s_gdata_hlsl32_ex = 4452
        s_ldata_hlsl32_ex = 4453
        s_inlinees = 4456
        s_bprel32_indir = 4464
        s_regrel32_indir = 4465
        s_gproc32ex = 4466
        s_lproc32ex = 4467
        s_gproc32ex_id = 4468
        s_lproc32ex_id = 4469
        s_staticlocal = 4470
        s_bprel32_enctmp = 4472
        s_regrel32_enctmp = 4473
        s_bprel32_indir_enctmp = 4474
        s_regrel32_indir_enctmp = 4475
        s_association = 4476
        s_sourcelink = 4478
        s_defrange_constval_on_entry = 4479
        s_defrange_globalsym_on_entry = 4480
        s_altobjname = 4481
    def __init__(self, symbols_size, c11_line_size, c13_line_size, _io, _parent=None, _root=None):
        super(ModiStream, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self
        self.symbols_size = symbols_size
        self.c11_line_size = c11_line_size
        self.c13_line_size = c13_line_size
        self._read()

    def _read(self):
        self.signature = self._io.read_u4le()
        if not  ((self.signature == 1) or (self.signature == 4)) :
            raise kaitaistruct.ValidationNotAnyOfError(self.signature, self._io, u"/seq/0")
        self._raw_symbols = self._io.read_bytes(self.symbols_size - 4)
        _io__raw_symbols = KaitaiStream(BytesIO(self._raw_symbols))
        self.symbols = ModiStream.SymbolEntries(_io__raw_symbols, self, self._root)
        self.c11_line_info = self._io.read_bytes(self.c11_line_size)
        self.c13_line_info = self._io.read_bytes(self.c13_line_size)
        self.global_refs_size = self._io.read_u4le()
        self.global_refs = self._io.read_bytes(self.global_refs_size)


    def _fetch_instances(self):
        pass
        self.symbols._fetch_instances()

    class BlockSym32(KaitaiStruct):
        """BLOCKSYM32 (cvinfo.h)."""
        def __init__(self, _io, _parent=None, _root=None):
            super(ModiStream.BlockSym32, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.pointer_parent = self._io.read_u4le()
            self.pointer_end = self._io.read_u4le()
            self.len = self._io.read_u4le()
            self.off = self._io.read_u4le()
            self.seg = self._io.read_u2le()
            self.name = (self._io.read_bytes_term(0, False, True, True)).decode(u"ASCII")


        def _fetch_instances(self):
            pass


    class BprelSym32(KaitaiStruct):
        """BPRELSYM32 (cvinfo.h)."""
        def __init__(self, _io, _parent=None, _root=None):
            super(ModiStream.BprelSym32, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.off = self._io.read_u4le()
            self.typind = self._io.read_u4le()
            self.name = (self._io.read_bytes_term(0, False, True, True)).decode(u"ASCII")


        def _fetch_instances(self):
            pass


    class Bprelsym3216t(KaitaiStruct):
        """BPRELSYM32_16t (cvinfo.h)."""
        def __init__(self, _io, _parent=None, _root=None):
            super(ModiStream.Bprelsym3216t, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.off = self._io.read_u4le()
            self.typind = self._io.read_u2le()
            self.name = pascal_string.PascalString(self._io)


        def _fetch_instances(self):
            pass
            self.name._fetch_instances()


    class BuildinfoSym(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(ModiStream.BuildinfoSym, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.id = self._io.read_u4le()


        def _fetch_instances(self):
            pass


    class CallsiteInfo(KaitaiStruct):
        """CALLSITEINFO (cvinfo.h)."""
        def __init__(self, _io, _parent=None, _root=None):
            super(ModiStream.CallsiteInfo, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.off = self._io.read_u4le()
            self.sect = self._io.read_u2le()
            self.padding = self._io.read_u2le()
            self.typind = self._io.read_u4le()


        def _fetch_instances(self):
            pass


    class CflagsSym(KaitaiStruct):
        """CFLAGSSYM (cvinfo.h)."""
        def __init__(self, _io, _parent=None, _root=None):
            super(ModiStream.CflagsSym, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.machine = self._io.read_u1()
            self.language = self._io.read_u1()
            self.flags = self._io.read_u2le()
            self.ver = pascal_string.PascalString(self._io)


        def _fetch_instances(self):
            pass
            self.ver._fetch_instances()


    class CoffgroupSym(KaitaiStruct):
        """COFFGROUPSYM (cvinfo.h)."""
        def __init__(self, _io, _parent=None, _root=None):
            super(ModiStream.CoffgroupSym, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.cb = self._io.read_u4le()
            self.characteristics = self._io.read_u4le()
            self.off = self._io.read_u4le()
            self.seg = self._io.read_u2le()
            self.name = (self._io.read_bytes_term(0, False, True, True)).decode(u"ASCII")


        def _fetch_instances(self):
            pass


    class Compilesym2Sym(KaitaiStruct):
        """COMPILESYM (cvinfo.h)."""
        def __init__(self, _io, _parent=None, _root=None):
            super(ModiStream.Compilesym2Sym, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.flags = self._io.read_u4le()
            self.machine = self._io.read_u2le()
            self.ver_fe_major = self._io.read_u2le()
            self.ver_fe_minor = self._io.read_u2le()
            self.ver_fe_build = self._io.read_u2le()
            self.ver_major = self._io.read_u2le()
            self.ver_minor = self._io.read_u2le()
            self.ver_build = self._io.read_u2le()
            self.ver_string = (self._io.read_bytes_term(0, False, True, True)).decode(u"ASCII")
            self.command_blocks = []
            i = 0
            while True:
                _ = ModiStream.EnvblockItem(self._io, self, self._root)
                self.command_blocks.append(_)
                if _.key == u"":
                    break
                i += 1


        def _fetch_instances(self):
            pass
            for i in range(len(self.command_blocks)):
                pass
                self.command_blocks[i]._fetch_instances()



    class Compilesym3Sym(KaitaiStruct):
        """COMPILESYM3 (cvinfo.h)."""
        def __init__(self, _io, _parent=None, _root=None):
            super(ModiStream.Compilesym3Sym, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.flags = self._io.read_u4le()
            self.machine = self._io.read_u2le()
            self.ver_fe_major = self._io.read_u2le()
            self.ver_fe_minor = self._io.read_u2le()
            self.ver_fe_build = self._io.read_u2le()
            self.ver_fe_qfe = self._io.read_u2le()
            self.ver_major = self._io.read_u2le()
            self.ver_minor = self._io.read_u2le()
            self.ver_build = self._io.read_u2le()
            self.ver_qfe = self._io.read_u2le()
            self.ver_string = (self._io.read_bytes_term(0, False, True, True)).decode(u"ASCII")


        def _fetch_instances(self):
            pass


    class ConstSym(KaitaiStruct):
        """CONSTSYM (cvinfo.h)."""
        def __init__(self, _io, _parent=None, _root=None):
            super(ModiStream.ConstSym, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.typind = self._io.read_u4le()
            self.value = numeric.Numeric(self._io)
            self.name = (self._io.read_bytes_term(0, False, True, True)).decode(u"ASCII")


        def _fetch_instances(self):
            pass
            self.value._fetch_instances()


    class Data32Sym(KaitaiStruct):
        """DATASYM32 (cvinfo.h)."""
        def __init__(self, _io, _parent=None, _root=None):
            super(ModiStream.Data32Sym, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.type_index = self._io.read_u4le()
            self.offset = self._io.read_u4le()
            self.segment = self._io.read_u2le()
            self.name = (self._io.read_bytes_term(0, False, True, True)).decode(u"ASCII")


        def _fetch_instances(self):
            pass


    class Datasym3216t(KaitaiStruct):
        """DATASYM32_16t (cvinfo.h)."""
        def __init__(self, _io, _parent=None, _root=None):
            super(ModiStream.Datasym3216t, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.off = self._io.read_u4le()
            self.seg = self._io.read_u2le()
            self.typind = self._io.read_u2le()
            self.name = pascal_string.PascalString(self._io)


        def _fetch_instances(self):
            pass
            self.name._fetch_instances()


    class DefrangeSym(KaitaiStruct):
        """DEFRANGESYM (cvinfo.h)."""
        def __init__(self, _io, _parent=None, _root=None):
            super(ModiStream.DefrangeSym, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.program = self._io.read_u4le()
            self.range = ModiStream.LvarAddrRange(self._io, self, self._root)
            self.gaps = []
            i = 0
            while not self._io.is_eof():
                self.gaps.append(ModiStream.LvarAddrGap(self._io, self, self._root))
                i += 1



        def _fetch_instances(self):
            pass
            self.range._fetch_instances()
            for i in range(len(self.gaps)):
                pass
                self.gaps[i]._fetch_instances()



    class DefrangeSymFramePointerRel(KaitaiStruct):
        """DEFRANGESYMFRAMEPOINTERREL (cvinfo.h)."""
        def __init__(self, _io, _parent=None, _root=None):
            super(ModiStream.DefrangeSymFramePointerRel, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.off_frame_pointer = self._io.read_u4le()
            self.range = ModiStream.LvarAddrRange(self._io, self, self._root)
            self.gaps = []
            i = 0
            while not self._io.is_eof():
                self.gaps.append(ModiStream.LvarAddrGap(self._io, self, self._root))
                i += 1



        def _fetch_instances(self):
            pass
            self.range._fetch_instances()
            for i in range(len(self.gaps)):
                pass
                self.gaps[i]._fetch_instances()



    class DefrangeSymFramepointerRelFullScope(KaitaiStruct):
        """DEFRANGESYMFRAMEPOINTERREL_FULL_SCOPE (cvinfo.h)."""
        def __init__(self, _io, _parent=None, _root=None):
            super(ModiStream.DefrangeSymFramepointerRelFullScope, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.off_frame_pointer = self._io.read_u4le()


        def _fetch_instances(self):
            pass


    class DefrangeSymRegister(KaitaiStruct):
        """DEFRANGESYMREGISTER (cvinfo.h)."""
        def __init__(self, _io, _parent=None, _root=None):
            super(ModiStream.DefrangeSymRegister, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.reg = self._io.read_u2le()
            self.attr = self._io.read_u2le()
            self.range = ModiStream.LvarAddrRange(self._io, self, self._root)
            self.gaps = []
            i = 0
            while not self._io.is_eof():
                self.gaps.append(ModiStream.LvarAddrGap(self._io, self, self._root))
                i += 1



        def _fetch_instances(self):
            pass
            self.range._fetch_instances()
            for i in range(len(self.gaps)):
                pass
                self.gaps[i]._fetch_instances()



    class DefrangeSymRegisterRel(KaitaiStruct):
        """DEFRANGESYMREGISTERREL (cvinfo.h)."""
        def __init__(self, _io, _parent=None, _root=None):
            super(ModiStream.DefrangeSymRegisterRel, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.base_reg = self._io.read_u2le()
            self.flags = self._io.read_u2le()
            self.off_base_pointer = self._io.read_u4le()
            self.range = ModiStream.LvarAddrRange(self._io, self, self._root)
            self.gaps = []
            i = 0
            while not self._io.is_eof():
                self.gaps.append(ModiStream.LvarAddrGap(self._io, self, self._root))
                i += 1



        def _fetch_instances(self):
            pass
            self.range._fetch_instances()
            for i in range(len(self.gaps)):
                pass
                self.gaps[i]._fetch_instances()



    class DefrangeSymSubfieldRegister(KaitaiStruct):
        """DEFRANGESYMSUBFIELDREGISTER (cvinfo.h)."""
        def __init__(self, _io, _parent=None, _root=None):
            super(ModiStream.DefrangeSymSubfieldRegister, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.reg = self._io.read_u2le()
            self.attr = self._io.read_u2le()
            self.off_parent_padding = self._io.read_u4le()
            self.range = ModiStream.LvarAddrRange(self._io, self, self._root)
            self.gaps = []
            i = 0
            while not self._io.is_eof():
                self.gaps.append(ModiStream.LvarAddrGap(self._io, self, self._root))
                i += 1



        def _fetch_instances(self):
            pass
            self.range._fetch_instances()
            for i in range(len(self.gaps)):
                pass
                self.gaps[i]._fetch_instances()



    class EndArgSym(KaitaiStruct):
        """ENDARGSYM."""
        def __init__(self, _io, _parent=None, _root=None):
            super(ModiStream.EndArgSym, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            pass


        def _fetch_instances(self):
            pass


    class EnvblockItem(KaitaiStruct):
        """ENVBLOCKSYM (cvinfo.h)."""
        def __init__(self, _io, _parent=None, _root=None):
            super(ModiStream.EnvblockItem, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.key = (self._io.read_bytes_term(0, False, True, True)).decode(u"ASCII")
            if self.key != u"":
                pass
                self.value = (self._io.read_bytes_term(0, False, True, True)).decode(u"ASCII")



        def _fetch_instances(self):
            pass
            if self.key != u"":
                pass



    class EnvblockSym(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(ModiStream.EnvblockSym, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.flags = self._io.read_u1()
            self.items = []
            i = 0
            while True:
                _ = ModiStream.EnvblockItem(self._io, self, self._root)
                self.items.append(_)
                if _.key == u"":
                    break
                i += 1


        def _fetch_instances(self):
            pass
            for i in range(len(self.items)):
                pass
                self.items[i]._fetch_instances()



    class ExportSym(KaitaiStruct):
        """EXPORTSYM (cvinfo.h)."""
        def __init__(self, _io, _parent=None, _root=None):
            super(ModiStream.ExportSym, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.ordinal = self._io.read_u2le()
            self.flags = self._io.read_u2le()
            self.name = (self._io.read_bytes_term(0, False, True, True)).decode(u"ASCII")


        def _fetch_instances(self):
            pass


    class FileStaticSym(KaitaiStruct):
        """FILESTATICSYM (cvinfo.h)."""
        def __init__(self, _io, _parent=None, _root=None):
            super(ModiStream.FileStaticSym, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.typind = self._io.read_u4le()
            self.mod_offset = self._io.read_u4le()
            self.flags = self._io.read_u2le()
            self.name = (self._io.read_bytes_term(0, False, True, True)).decode(u"ASCII")


        def _fetch_instances(self):
            pass


    class FrameProcSym(KaitaiStruct):
        """FRMEPROCSYM."""
        def __init__(self, _io, _parent=None, _root=None):
            super(ModiStream.FrameProcSym, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.cb_frame = self._io.read_u4le()
            self.cb_pad = self._io.read_u4le()
            self.off_pad = self._io.read_u4le()
            self.cb_save_regs = self._io.read_u4le()
            self.off_ex_hdlr = self._io.read_u4le()
            self.sect_ex_hdlr = self._io.read_u2le()
            self.flags = self._io.read_u4le()


        def _fetch_instances(self):
            pass


    class Framecookie(KaitaiStruct):
        """FRAMECOOKIE (cvinfo.h) (NOTE: this element is parsed wrong by Microsoft's cvdump.exe)."""
        def __init__(self, _io, _parent=None, _root=None):
            super(ModiStream.Framecookie, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.off = self._io.read_u4le()
            self.reg = self._io.read_u2le()
            self.cookietype = self._io.read_u1()
            self.flags = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class FunctionList(KaitaiStruct):
        """FUNCTIONLIST (cvinfo.h)."""
        def __init__(self, _io, _parent=None, _root=None):
            super(ModiStream.FunctionList, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.count = self._io.read_u4le()
            self.funcs = []
            for i in range(self.count):
                self.funcs.append(self._io.read_u4le())

            self.invocations = []
            i = 0
            while not self._io.is_eof():
                self.invocations.append(self._io.read_u4le())
                i += 1



        def _fetch_instances(self):
            pass
            for i in range(len(self.funcs)):
                pass

            for i in range(len(self.invocations)):
                pass



    class HeapAllocSite(KaitaiStruct):
        """HEAPALLOCSITE (cvinfo.h)."""
        def __init__(self, _io, _parent=None, _root=None):
            super(ModiStream.HeapAllocSite, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.off = self._io.read_u4le()
            self.sect = self._io.read_u2le()
            self.cb_instr = self._io.read_u2le()
            self.typind = self._io.read_u2le()


        def _fetch_instances(self):
            pass


    class InlineSiteEndSym(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(ModiStream.InlineSiteEndSym, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            pass


        def _fetch_instances(self):
            pass


    class InlineSiteSym(KaitaiStruct):
        """INLINESITESYM (cvindo.h)."""
        def __init__(self, _io, _parent=None, _root=None):
            super(ModiStream.InlineSiteSym, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.pointer_parent = self._io.read_u4le()
            self.pointer_end = self._io.read_u4le()
            self.inlinee = self._io.read_u4le()
            self.binary_annotations = []
            i = 0
            while not self._io.is_eof():
                self.binary_annotations.append(self._io.read_u1())
                i += 1



        def _fetch_instances(self):
            pass
            for i in range(len(self.binary_annotations)):
                pass



    class InlineesSym(KaitaiStruct):
        """Pure guess from LLVM."""
        def __init__(self, _io, _parent=None, _root=None):
            super(ModiStream.InlineesSym, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.count = self._io.read_u4le()
            self.items = []
            for i in range(self.count):
                self.items.append(self._io.read_u4le())



        def _fetch_instances(self):
            pass
            for i in range(len(self.items)):
                pass



    class LabelSym32(KaitaiStruct):
        """LABELSYM32 (cvinfo.h)."""
        def __init__(self, is_strz, _io, _parent=None, _root=None):
            super(ModiStream.LabelSym32, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self.is_strz = is_strz
            self._read()

        def _read(self):
            self.off = self._io.read_u4le()
            self.seg = self._io.read_u2le()
            self.flags = self._io.read_u1()
            self.name = strz_or_pascal.StrzOrPascal(self.is_strz, self._io)


        def _fetch_instances(self):
            pass
            self.name._fetch_instances()


    class LocalSym(KaitaiStruct):
        """LOCALSYM (cvinfo.h)."""
        def __init__(self, _io, _parent=None, _root=None):
            super(ModiStream.LocalSym, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.type_index = self._io.read_u4le()
            self.flags = self._io.read_u2le()
            self.name = (self._io.read_bytes_term(0, False, True, True)).decode(u"ASCII")


        def _fetch_instances(self):
            pass


    class LvarAddrGap(KaitaiStruct):
        """CV_LVAR_ADDR_GAP (cvinfo.h)."""
        def __init__(self, _io, _parent=None, _root=None):
            super(ModiStream.LvarAddrGap, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.gap_start_offset = self._io.read_u2le()
            self.cb_range = self._io.read_u2le()


        def _fetch_instances(self):
            pass


    class LvarAddrRange(KaitaiStruct):
        """CV_LVAR_ADDR_RANGE (cvinfo.h)."""
        def __init__(self, _io, _parent=None, _root=None):
            super(ModiStream.LvarAddrRange, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.off_start = self._io.read_u4le()
            self.isect_start = self._io.read_u2le()
            self.cb_range = self._io.read_u2le()


        def _fetch_instances(self):
            pass


    class ObjnameSym(KaitaiStruct):
        """OBJNAMESYM (cvinfo.h)."""
        def __init__(self, is_strz, _io, _parent=None, _root=None):
            super(ModiStream.ObjnameSym, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self.is_strz = is_strz
            self._read()

        def _read(self):
            self.signature = self._io.read_u4le()
            self.name = strz_or_pascal.StrzOrPascal(self.is_strz, self._io)


        def _fetch_instances(self):
            pass
            self.name._fetch_instances()


    class Procsym32(KaitaiStruct):
        """PROCSYM32 (cvinfo.h)."""
        def __init__(self, _io, _parent=None, _root=None):
            super(ModiStream.Procsym32, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.pointer_parent = self._io.read_u4le()
            self.pointer_end = self._io.read_u4le()
            self.pointer_next = self._io.read_u4le()
            self.length = self._io.read_u4le()
            self.debug_start = self._io.read_u4le()
            self.debug_end = self._io.read_u4le()
            self.type_index = self._io.read_u4le()
            self.offset = self._io.read_u4le()
            self.segment = self._io.read_u2le()
            self.flags = self._io.read_u1()
            self.name = (self._io.read_bytes_term(0, False, True, True)).decode(u"ASCII")


        def _fetch_instances(self):
            pass


    class Procsym3216t(KaitaiStruct):
        """PROCSYM32_16t (cvinfo.h)."""
        def __init__(self, _io, _parent=None, _root=None):
            super(ModiStream.Procsym3216t, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.pointer_parent = self._io.read_u4le()
            self.pointer_end = self._io.read_u4le()
            self.pointer_next = self._io.read_u4le()
            self.len = self._io.read_u4le()
            self.debug_start = self._io.read_u4le()
            self.debug_end = self._io.read_u4le()
            self.off = self._io.read_u4le()
            self.seg = self._io.read_u2le()
            self.typind = self._io.read_u2le()
            self.flags = self._io.read_u1()
            self.name = pascal_string.PascalString(self._io)


        def _fetch_instances(self):
            pass
            self.name._fetch_instances()


    class Record(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(ModiStream.Record, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.type = KaitaiStream.resolve_enum(ModiStream.SymbolType, self._io.read_u2le())
            _on = self.type
            if _on == ModiStream.SymbolType.s_block32:
                pass
                self.element = ModiStream.BlockSym32(self._io, self, self._root)
            elif _on == ModiStream.SymbolType.s_bprel32:
                pass
                self.element = ModiStream.BprelSym32(self._io, self, self._root)
            elif _on == ModiStream.SymbolType.s_bprel32_16t:
                pass
                self.element = ModiStream.Bprelsym3216t(self._io, self, self._root)
            elif _on == ModiStream.SymbolType.s_buildinfo:
                pass
                self.element = ModiStream.BuildinfoSym(self._io, self, self._root)
            elif _on == ModiStream.SymbolType.s_callees:
                pass
                self.element = ModiStream.FunctionList(self._io, self, self._root)
            elif _on == ModiStream.SymbolType.s_callers:
                pass
                self.element = ModiStream.FunctionList(self._io, self, self._root)
            elif _on == ModiStream.SymbolType.s_callsiteinfo:
                pass
                self.element = ModiStream.CallsiteInfo(self._io, self, self._root)
            elif _on == ModiStream.SymbolType.s_coboludt:
                pass
                self.element = ModiStream.UdtSym(self._io, self, self._root)
            elif _on == ModiStream.SymbolType.s_coffgroup:
                pass
                self.element = ModiStream.CoffgroupSym(self._io, self, self._root)
            elif _on == ModiStream.SymbolType.s_compile:
                pass
                self.element = ModiStream.CflagsSym(self._io, self, self._root)
            elif _on == ModiStream.SymbolType.s_compile2:
                pass
                self.element = ModiStream.Compilesym2Sym(self._io, self, self._root)
            elif _on == ModiStream.SymbolType.s_compile3:
                pass
                self.element = ModiStream.Compilesym3Sym(self._io, self, self._root)
            elif _on == ModiStream.SymbolType.s_constant:
                pass
                self.element = ModiStream.ConstSym(self._io, self, self._root)
            elif _on == ModiStream.SymbolType.s_defrange:
                pass
                self.element = ModiStream.DefrangeSym(self._io, self, self._root)
            elif _on == ModiStream.SymbolType.s_defrange_framepointer_rel:
                pass
                self.element = ModiStream.DefrangeSymFramePointerRel(self._io, self, self._root)
            elif _on == ModiStream.SymbolType.s_defrange_framepointer_rel_full_scope:
                pass
                self.element = ModiStream.DefrangeSymFramepointerRelFullScope(self._io, self, self._root)
            elif _on == ModiStream.SymbolType.s_defrange_register:
                pass
                self.element = ModiStream.DefrangeSymRegister(self._io, self, self._root)
            elif _on == ModiStream.SymbolType.s_defrange_register_rel:
                pass
                self.element = ModiStream.DefrangeSymRegisterRel(self._io, self, self._root)
            elif _on == ModiStream.SymbolType.s_defrange_subfield_register:
                pass
                self.element = ModiStream.DefrangeSymSubfieldRegister(self._io, self, self._root)
            elif _on == ModiStream.SymbolType.s_end:
                pass
                self.element = ModiStream.EndArgSym(self._io, self, self._root)
            elif _on == ModiStream.SymbolType.s_envblock:
                pass
                self.element = ModiStream.EnvblockSym(self._io, self, self._root)
            elif _on == ModiStream.SymbolType.s_export:
                pass
                self.element = ModiStream.ExportSym(self._io, self, self._root)
            elif _on == ModiStream.SymbolType.s_filestatic:
                pass
                self.element = ModiStream.FileStaticSym(self._io, self, self._root)
            elif _on == ModiStream.SymbolType.s_framecookie:
                pass
                self.element = ModiStream.Framecookie(self._io, self, self._root)
            elif _on == ModiStream.SymbolType.s_frameproc:
                pass
                self.element = ModiStream.FrameProcSym(self._io, self, self._root)
            elif _on == ModiStream.SymbolType.s_gproc32:
                pass
                self.element = ModiStream.Procsym32(self._io, self, self._root)
            elif _on == ModiStream.SymbolType.s_gproc32_16t:
                pass
                self.element = ModiStream.Procsym3216t(self._io, self, self._root)
            elif _on == ModiStream.SymbolType.s_heapallocsite:
                pass
                self.element = ModiStream.HeapAllocSite(self._io, self, self._root)
            elif _on == ModiStream.SymbolType.s_inlinees:
                pass
                self.element = ModiStream.InlineesSym(self._io, self, self._root)
            elif _on == ModiStream.SymbolType.s_inlinesite:
                pass
                self.element = ModiStream.InlineSiteSym(self._io, self, self._root)
            elif _on == ModiStream.SymbolType.s_inlinesite_end:
                pass
                self.element = ModiStream.InlineSiteEndSym(self._io, self, self._root)
            elif _on == ModiStream.SymbolType.s_label32:
                pass
                self.element = ModiStream.LabelSym32(True, self._io, self, self._root)
            elif _on == ModiStream.SymbolType.s_label32_st:
                pass
                self.element = ModiStream.LabelSym32(False, self._io, self, self._root)
            elif _on == ModiStream.SymbolType.s_ldata32:
                pass
                self.element = ModiStream.Data32Sym(self._io, self, self._root)
            elif _on == ModiStream.SymbolType.s_ldata32_16t:
                pass
                self.element = ModiStream.Datasym3216t(self._io, self, self._root)
            elif _on == ModiStream.SymbolType.s_local:
                pass
                self.element = ModiStream.LocalSym(self._io, self, self._root)
            elif _on == ModiStream.SymbolType.s_lproc32:
                pass
                self.element = ModiStream.Procsym32(self._io, self, self._root)
            elif _on == ModiStream.SymbolType.s_lproc32_16t:
                pass
                self.element = ModiStream.Procsym3216t(self._io, self, self._root)
            elif _on == ModiStream.SymbolType.s_manconstant:
                pass
                self.element = ModiStream.ConstSym(self._io, self, self._root)
            elif _on == ModiStream.SymbolType.s_objname:
                pass
                self.element = ModiStream.ObjnameSym(True, self._io, self, self._root)
            elif _on == ModiStream.SymbolType.s_objname_st:
                pass
                self.element = ModiStream.ObjnameSym(False, self._io, self, self._root)
            elif _on == ModiStream.SymbolType.s_register:
                pass
                self.element = ModiStream.RegSym(self._io, self, self._root)
            elif _on == ModiStream.SymbolType.s_register_16t:
                pass
                self.element = ModiStream.Regsym16(self._io, self, self._root)
            elif _on == ModiStream.SymbolType.s_regrel32:
                pass
                self.element = ModiStream.RegRel32(self._io, self, self._root)
            elif _on == ModiStream.SymbolType.s_section:
                pass
                self.element = ModiStream.SectionSym(self._io, self, self._root)
            elif _on == ModiStream.SymbolType.s_thunk32:
                pass
                self.element = ModiStream.ThunkSym32(True, self._io, self, self._root)
            elif _on == ModiStream.SymbolType.s_thunk32_st:
                pass
                self.element = ModiStream.ThunkSym32(False, self._io, self, self._root)
            elif _on == ModiStream.SymbolType.s_udt:
                pass
                self.element = ModiStream.UdtSym(self._io, self, self._root)
            elif _on == ModiStream.SymbolType.s_unamespace:
                pass
                self.element = ModiStream.Unamespace(self._io, self, self._root)


        def _fetch_instances(self):
            pass
            _on = self.type
            if _on == ModiStream.SymbolType.s_block32:
                pass
                self.element._fetch_instances()
            elif _on == ModiStream.SymbolType.s_bprel32:
                pass
                self.element._fetch_instances()
            elif _on == ModiStream.SymbolType.s_bprel32_16t:
                pass
                self.element._fetch_instances()
            elif _on == ModiStream.SymbolType.s_buildinfo:
                pass
                self.element._fetch_instances()
            elif _on == ModiStream.SymbolType.s_callees:
                pass
                self.element._fetch_instances()
            elif _on == ModiStream.SymbolType.s_callers:
                pass
                self.element._fetch_instances()
            elif _on == ModiStream.SymbolType.s_callsiteinfo:
                pass
                self.element._fetch_instances()
            elif _on == ModiStream.SymbolType.s_coboludt:
                pass
                self.element._fetch_instances()
            elif _on == ModiStream.SymbolType.s_coffgroup:
                pass
                self.element._fetch_instances()
            elif _on == ModiStream.SymbolType.s_compile:
                pass
                self.element._fetch_instances()
            elif _on == ModiStream.SymbolType.s_compile2:
                pass
                self.element._fetch_instances()
            elif _on == ModiStream.SymbolType.s_compile3:
                pass
                self.element._fetch_instances()
            elif _on == ModiStream.SymbolType.s_constant:
                pass
                self.element._fetch_instances()
            elif _on == ModiStream.SymbolType.s_defrange:
                pass
                self.element._fetch_instances()
            elif _on == ModiStream.SymbolType.s_defrange_framepointer_rel:
                pass
                self.element._fetch_instances()
            elif _on == ModiStream.SymbolType.s_defrange_framepointer_rel_full_scope:
                pass
                self.element._fetch_instances()
            elif _on == ModiStream.SymbolType.s_defrange_register:
                pass
                self.element._fetch_instances()
            elif _on == ModiStream.SymbolType.s_defrange_register_rel:
                pass
                self.element._fetch_instances()
            elif _on == ModiStream.SymbolType.s_defrange_subfield_register:
                pass
                self.element._fetch_instances()
            elif _on == ModiStream.SymbolType.s_end:
                pass
                self.element._fetch_instances()
            elif _on == ModiStream.SymbolType.s_envblock:
                pass
                self.element._fetch_instances()
            elif _on == ModiStream.SymbolType.s_export:
                pass
                self.element._fetch_instances()
            elif _on == ModiStream.SymbolType.s_filestatic:
                pass
                self.element._fetch_instances()
            elif _on == ModiStream.SymbolType.s_framecookie:
                pass
                self.element._fetch_instances()
            elif _on == ModiStream.SymbolType.s_frameproc:
                pass
                self.element._fetch_instances()
            elif _on == ModiStream.SymbolType.s_gproc32:
                pass
                self.element._fetch_instances()
            elif _on == ModiStream.SymbolType.s_gproc32_16t:
                pass
                self.element._fetch_instances()
            elif _on == ModiStream.SymbolType.s_heapallocsite:
                pass
                self.element._fetch_instances()
            elif _on == ModiStream.SymbolType.s_inlinees:
                pass
                self.element._fetch_instances()
            elif _on == ModiStream.SymbolType.s_inlinesite:
                pass
                self.element._fetch_instances()
            elif _on == ModiStream.SymbolType.s_inlinesite_end:
                pass
                self.element._fetch_instances()
            elif _on == ModiStream.SymbolType.s_label32:
                pass
                self.element._fetch_instances()
            elif _on == ModiStream.SymbolType.s_label32_st:
                pass
                self.element._fetch_instances()
            elif _on == ModiStream.SymbolType.s_ldata32:
                pass
                self.element._fetch_instances()
            elif _on == ModiStream.SymbolType.s_ldata32_16t:
                pass
                self.element._fetch_instances()
            elif _on == ModiStream.SymbolType.s_local:
                pass
                self.element._fetch_instances()
            elif _on == ModiStream.SymbolType.s_lproc32:
                pass
                self.element._fetch_instances()
            elif _on == ModiStream.SymbolType.s_lproc32_16t:
                pass
                self.element._fetch_instances()
            elif _on == ModiStream.SymbolType.s_manconstant:
                pass
                self.element._fetch_instances()
            elif _on == ModiStream.SymbolType.s_objname:
                pass
                self.element._fetch_instances()
            elif _on == ModiStream.SymbolType.s_objname_st:
                pass
                self.element._fetch_instances()
            elif _on == ModiStream.SymbolType.s_register:
                pass
                self.element._fetch_instances()
            elif _on == ModiStream.SymbolType.s_register_16t:
                pass
                self.element._fetch_instances()
            elif _on == ModiStream.SymbolType.s_regrel32:
                pass
                self.element._fetch_instances()
            elif _on == ModiStream.SymbolType.s_section:
                pass
                self.element._fetch_instances()
            elif _on == ModiStream.SymbolType.s_thunk32:
                pass
                self.element._fetch_instances()
            elif _on == ModiStream.SymbolType.s_thunk32_st:
                pass
                self.element._fetch_instances()
            elif _on == ModiStream.SymbolType.s_udt:
                pass
                self.element._fetch_instances()
            elif _on == ModiStream.SymbolType.s_unamespace:
                pass
                self.element._fetch_instances()


    class RegRel32(KaitaiStruct):
        """REGREL32 (cvinfo.h)."""
        def __init__(self, _io, _parent=None, _root=None):
            super(ModiStream.RegRel32, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.off = self._io.read_u4le()
            self.typind = self._io.read_u4le()
            self.reg = self._io.read_u2le()
            self.name = (self._io.read_bytes_term(0, False, True, True)).decode(u"ASCII")


        def _fetch_instances(self):
            pass


    class RegSym(KaitaiStruct):
        """REGSYM (cvinfo.h)."""
        def __init__(self, _io, _parent=None, _root=None):
            super(ModiStream.RegSym, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.typind = self._io.read_u4le()
            self.reg = self._io.read_u2le()
            self.name = (self._io.read_bytes_term(0, False, True, True)).decode(u"ASCII")


        def _fetch_instances(self):
            pass


    class Regsym16(KaitaiStruct):
        """REGSYM_16t (cvinfo.h)."""
        def __init__(self, _io, _parent=None, _root=None):
            super(ModiStream.Regsym16, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.typind = self._io.read_u2le()
            self.reg = self._io.read_u2le()
            self.name = pascal_string.PascalString(self._io)


        def _fetch_instances(self):
            pass
            self.name._fetch_instances()


    class SectionSym(KaitaiStruct):
        """SECTIONSYM (cvinfo.h)."""
        def __init__(self, _io, _parent=None, _root=None):
            super(ModiStream.SectionSym, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.isec = self._io.read_u2le()
            self.align = self._io.read_u1()
            self.reserved = self._io.read_u1()
            self.rva = self._io.read_u4le()
            self.cb = self._io.read_u4le()
            self.characteristics = self._io.read_u4le()
            self.name = (self._io.read_bytes_term(0, False, True, True)).decode(u"ASCII")


        def _fetch_instances(self):
            pass


    class Symbol(KaitaiStruct):
        def __init__(self, pos, _io, _parent=None, _root=None):
            super(ModiStream.Symbol, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self.pos = pos
            self._read()

        def _read(self):
            self.record_size = self._io.read_u2le()
            self._raw_record = self._io.read_bytes(self.record_size)
            _io__raw_record = KaitaiStream(BytesIO(self._raw_record))
            self.record = ModiStream.Record(_io__raw_record, self, self._root)
            self.trailing_padding = self._io.read_bytes((4 - self._io.pos() % 4) % 4)


        def _fetch_instances(self):
            pass
            self.record._fetch_instances()


    class SymbolEntries(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(ModiStream.SymbolEntries, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.entries = []
            i = 0
            while not self._io.is_eof():
                self.entries.append(ModiStream.Symbol(self._io.pos() + 4, self._io, self, self._root))
                i += 1



        def _fetch_instances(self):
            pass
            for i in range(len(self.entries)):
                pass
                self.entries[i]._fetch_instances()



    class ThunkSym32(KaitaiStruct):
        """THUNKSYM32 (cvinfo.h)."""
        def __init__(self, is_strz, _io, _parent=None, _root=None):
            super(ModiStream.ThunkSym32, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self.is_strz = is_strz
            self._read()

        def _read(self):
            self.pointer_parent = self._io.read_u4le()
            self.pointer_end = self._io.read_u4le()
            self.pointer_next = self._io.read_u4le()
            self.off = self._io.read_u4le()
            self.seg = self._io.read_u2le()
            self.len = self._io.read_u2le()
            self.ord = self._io.read_u1()
            self.name = strz_or_pascal.StrzOrPascal(self.is_strz, self._io)
            if self.ord == 1:
                pass
                self.variant_adjustor_delta = self._io.read_u2le()

            if self.ord == 1:
                pass
                self.variant_adjustor_target = strz_or_pascal.StrzOrPascal(self.is_strz, self._io)

            if self.ord == 2:
                pass
                self.variant_vcall_table_entry = self._io.read_u2le()



        def _fetch_instances(self):
            pass
            self.name._fetch_instances()
            if self.ord == 1:
                pass

            if self.ord == 1:
                pass
                self.variant_adjustor_target._fetch_instances()

            if self.ord == 2:
                pass



    class UdtSym(KaitaiStruct):
        """UDTSYM (cvinfoh)."""
        def __init__(self, _io, _parent=None, _root=None):
            super(ModiStream.UdtSym, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.typind = self._io.read_u4le()
            self.name = (self._io.read_bytes_term(0, False, True, True)).decode(u"ASCII")


        def _fetch_instances(self):
            pass


    class Unamespace(KaitaiStruct):
        """UNAMESPACE (cvinfo.h)."""
        def __init__(self, _io, _parent=None, _root=None):
            super(ModiStream.Unamespace, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.name = (self._io.read_bytes_term(0, False, True, True)).decode(u"ASCII")


        def _fetch_instances(self):
            pass



