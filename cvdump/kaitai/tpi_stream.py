# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
from enum import IntEnum


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class TpiStream(KaitaiStruct):
    """HDR_16t (tpi.h)."""
    def __init__(self, _io, _parent=None, _root=None):
        super(TpiStream, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self
        self._read()

    def _read(self):
        self.version = self._io.read_u4le()
        if not  ((self.version == 920924) or (self.version == 19951122) or (self.version == 19961031) or (self.version == 20040203)) :
            raise kaitaistruct.ValidationNotAnyOfError(self.version, self._io, u"/seq/0")
        self.header = TpiStream.TpiHeader(self.version, self._io, self, self._root)
        self.records = []
        for i in range(self.header.ti_max - self.header.ti_min):
            self.records.append(TpiStream.Record(self._io, self, self._root))



    def _fetch_instances(self):
        pass
        self.header._fetch_instances()
        for i in range(len(self.records)):
            pass
            self.records[i]._fetch_instances()


    class Complex128(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(TpiStream.Complex128, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.real = self._io.read_bytes(16)
            self.complex = self._io.read_bytes(16)


        def _fetch_instances(self):
            pass


    class Complex32(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(TpiStream.Complex32, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.real = self._io.read_f4le()
            self.complex = self._io.read_f4le()


        def _fetch_instances(self):
            pass


    class Complex64(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(TpiStream.Complex64, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.real = self._io.read_f8le()
            self.complex = self._io.read_f8le()


        def _fetch_instances(self):
            pass


    class Complex80(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(TpiStream.Complex80, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.real = self._io.read_bytes(10)
            self.complex = self._io.read_bytes(10)


        def _fetch_instances(self):
            pass


    class Decimal(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(TpiStream.Decimal, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.w_reserved = self._io.read_u2le()
            self.scale = self._io.read_u1()
            self.sign = self._io.read_u1()
            self.hi32 = self._io.read_u4le()
            self.lo64 = self._io.read_u8le()


        def _fetch_instances(self):
            pass


    class FieldList16tItem(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(TpiStream.FieldList16tItem, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.type = KaitaiStream.resolve_enum(TpiStream.Leaf.LeafType, self._io.read_u2le())
            _on = self.type
            if _on == TpiStream.Leaf.LeafType.lf_bclass_16t:
                pass
                self.element = TpiStream.LfBclass16St(self._io, self, self._root)
            elif _on == TpiStream.Leaf.LeafType.lf_enumerate_st:
                pass
                self.element = TpiStream.LfEnumerateSt16t(self._io, self, self._root)
            elif _on == TpiStream.Leaf.LeafType.lf_index_16t:
                pass
                self.element = TpiStream.LfIndex16t(self._io, self, self._root)
            elif _on == TpiStream.Leaf.LeafType.lf_ivbclass_16t:
                pass
                self.element = TpiStream.LfVbclass16t(self._io, self, self._root)
            elif _on == TpiStream.Leaf.LeafType.lf_member_16t:
                pass
                self.element = TpiStream.LfMember16t(self._io, self, self._root)
            elif _on == TpiStream.Leaf.LeafType.lf_method_16t:
                pass
                self.element = TpiStream.LfMethod16t(self._io, self, self._root)
            elif _on == TpiStream.Leaf.LeafType.lf_nesttype_16t:
                pass
                self.element = TpiStream.LfNesttype16t(self._io, self, self._root)
            elif _on == TpiStream.Leaf.LeafType.lf_onemethod_16t:
                pass
                self.element = TpiStream.LfOnemethod16t(self._io, self, self._root)
            elif _on == TpiStream.Leaf.LeafType.lf_stmember_16t:
                pass
                self.element = TpiStream.LfStmember16t(self._io, self, self._root)
            elif _on == TpiStream.Leaf.LeafType.lf_vbclass_16t:
                pass
                self.element = TpiStream.LfVbclass16t(self._io, self, self._root)
            elif _on == TpiStream.Leaf.LeafType.lf_vfunctab_16t:
                pass
                self.element = TpiStream.LfVfunctab16t(self._io, self, self._root)
            self.trailing_padding = self._io.read_bytes((4 - self._io.pos() % 4) % 4)


        def _fetch_instances(self):
            pass
            _on = self.type
            if _on == TpiStream.Leaf.LeafType.lf_bclass_16t:
                pass
                self.element._fetch_instances()
            elif _on == TpiStream.Leaf.LeafType.lf_enumerate_st:
                pass
                self.element._fetch_instances()
            elif _on == TpiStream.Leaf.LeafType.lf_index_16t:
                pass
                self.element._fetch_instances()
            elif _on == TpiStream.Leaf.LeafType.lf_ivbclass_16t:
                pass
                self.element._fetch_instances()
            elif _on == TpiStream.Leaf.LeafType.lf_member_16t:
                pass
                self.element._fetch_instances()
            elif _on == TpiStream.Leaf.LeafType.lf_method_16t:
                pass
                self.element._fetch_instances()
            elif _on == TpiStream.Leaf.LeafType.lf_nesttype_16t:
                pass
                self.element._fetch_instances()
            elif _on == TpiStream.Leaf.LeafType.lf_onemethod_16t:
                pass
                self.element._fetch_instances()
            elif _on == TpiStream.Leaf.LeafType.lf_stmember_16t:
                pass
                self.element._fetch_instances()
            elif _on == TpiStream.Leaf.LeafType.lf_vbclass_16t:
                pass
                self.element._fetch_instances()
            elif _on == TpiStream.Leaf.LeafType.lf_vfunctab_16t:
                pass
                self.element._fetch_instances()


    class FieldListItem(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(TpiStream.FieldListItem, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.type = KaitaiStream.resolve_enum(TpiStream.Leaf.LeafType, self._io.read_u2le())
            _on = self.type
            if _on == TpiStream.Leaf.LeafType.lf_bclass:
                pass
                self.element = TpiStream.LfBclass(self._io, self, self._root)
            elif _on == TpiStream.Leaf.LeafType.lf_binterface:
                pass
                self.element = TpiStream.LfBclass(self._io, self, self._root)
            elif _on == TpiStream.Leaf.LeafType.lf_enumerate:
                pass
                self.element = TpiStream.LfEnumerate(self._io, self, self._root)
            elif _on == TpiStream.Leaf.LeafType.lf_enumerate_st:
                pass
                self.element = TpiStream.LfEnumerate(self._io, self, self._root)
            elif _on == TpiStream.Leaf.LeafType.lf_index:
                pass
                self.element = TpiStream.LfIndex(self._io, self, self._root)
            elif _on == TpiStream.Leaf.LeafType.lf_member:
                pass
                self.element = TpiStream.LfMember(self._io, self, self._root)
            elif _on == TpiStream.Leaf.LeafType.lf_member_st:
                pass
                self.element = TpiStream.LfMember(self._io, self, self._root)
            elif _on == TpiStream.Leaf.LeafType.lf_method:
                pass
                self.element = TpiStream.LfMethod(self._io, self, self._root)
            elif _on == TpiStream.Leaf.LeafType.lf_method_st:
                pass
                self.element = TpiStream.LfMethod(self._io, self, self._root)
            elif _on == TpiStream.Leaf.LeafType.lf_nesttype:
                pass
                self.element = TpiStream.LfNesttype(self._io, self, self._root)
            elif _on == TpiStream.Leaf.LeafType.lf_nesttype_st:
                pass
                self.element = TpiStream.LfNesttype(self._io, self, self._root)
            elif _on == TpiStream.Leaf.LeafType.lf_onemethod:
                pass
                self.element = TpiStream.LfOnemethod(self._io, self, self._root)
            elif _on == TpiStream.Leaf.LeafType.lf_onemethod_st:
                pass
                self.element = TpiStream.LfOnemethod(self._io, self, self._root)
            elif _on == TpiStream.Leaf.LeafType.lf_stmember:
                pass
                self.element = TpiStream.LfStmember(self._io, self, self._root)
            elif _on == TpiStream.Leaf.LeafType.lf_stmember_st:
                pass
                self.element = TpiStream.LfStmember(self._io, self, self._root)
            elif _on == TpiStream.Leaf.LeafType.lf_vfunctab:
                pass
                self.element = TpiStream.LfVfunctab(self._io, self, self._root)
            self.trailing_padding = self._io.read_bytes((4 - self._io.pos() % 4) % 4)


        def _fetch_instances(self):
            pass
            _on = self.type
            if _on == TpiStream.Leaf.LeafType.lf_bclass:
                pass
                self.element._fetch_instances()
            elif _on == TpiStream.Leaf.LeafType.lf_binterface:
                pass
                self.element._fetch_instances()
            elif _on == TpiStream.Leaf.LeafType.lf_enumerate:
                pass
                self.element._fetch_instances()
            elif _on == TpiStream.Leaf.LeafType.lf_enumerate_st:
                pass
                self.element._fetch_instances()
            elif _on == TpiStream.Leaf.LeafType.lf_index:
                pass
                self.element._fetch_instances()
            elif _on == TpiStream.Leaf.LeafType.lf_member:
                pass
                self.element._fetch_instances()
            elif _on == TpiStream.Leaf.LeafType.lf_member_st:
                pass
                self.element._fetch_instances()
            elif _on == TpiStream.Leaf.LeafType.lf_method:
                pass
                self.element._fetch_instances()
            elif _on == TpiStream.Leaf.LeafType.lf_method_st:
                pass
                self.element._fetch_instances()
            elif _on == TpiStream.Leaf.LeafType.lf_nesttype:
                pass
                self.element._fetch_instances()
            elif _on == TpiStream.Leaf.LeafType.lf_nesttype_st:
                pass
                self.element._fetch_instances()
            elif _on == TpiStream.Leaf.LeafType.lf_onemethod:
                pass
                self.element._fetch_instances()
            elif _on == TpiStream.Leaf.LeafType.lf_onemethod_st:
                pass
                self.element._fetch_instances()
            elif _on == TpiStream.Leaf.LeafType.lf_stmember:
                pass
                self.element._fetch_instances()
            elif _on == TpiStream.Leaf.LeafType.lf_stmember_st:
                pass
                self.element._fetch_instances()
            elif _on == TpiStream.Leaf.LeafType.lf_vfunctab:
                pass
                self.element._fetch_instances()


    class Leaf(KaitaiStruct):

        class LeafType(IntEnum):
            lf_modifier_16t = 1
            lf_pointer_16t = 2
            lf_array_16t = 3
            lf_class_16t = 4
            lf_structure_16t = 5
            lf_union_16t = 6
            lf_enum_16t = 7
            lf_procedure_16t = 8
            lf_mfunction_16t = 9
            lf_vtshape = 10
            lf_cobol0_16t = 11
            lf_cobol1 = 12
            lf_barray_16t = 13
            lf_label = 14
            lf_null = 15
            lf_nottran = 16
            lf_dimarray_16t = 17
            lf_vftpath_16t = 18
            lf_precomp_16t = 19
            lf_endprecomp = 20
            lf_oem_16t = 21
            lf_typeserver_st = 22
            lf_pad0 = 240
            lf_pad1 = 241
            lf_pad2 = 242
            lf_pad3 = 243
            lf_pad4 = 244
            lf_pad5 = 245
            lf_pad6 = 246
            lf_pad7 = 247
            lf_pad8 = 248
            lf_pad9 = 249
            lf_pad10 = 250
            lf_pad11 = 251
            lf_pad12 = 252
            lf_pad13 = 253
            lf_pad14 = 254
            lf_pad15 = 255
            lf_skip_16t = 512
            lf_arglist_16t = 513
            lf_defarg_16t = 514
            lf_list = 515
            lf_fieldlist_16t = 516
            lf_derived_16t = 517
            lf_bitfield_16t = 518
            lf_methodlist_16t = 519
            lf_dimconu_16t = 520
            lf_dimconlu_16t = 521
            lf_dimvaru_16t = 522
            lf_dimvarlu_16t = 523
            lf_refsym = 524
            lf_bclass_16t = 1024
            lf_vbclass_16t = 1025
            lf_ivbclass_16t = 1026
            lf_enumerate_st = 1027
            lf_friendfcn_16t = 1028
            lf_index_16t = 1029
            lf_member_16t = 1030
            lf_stmember_16t = 1031
            lf_method_16t = 1032
            lf_nesttype_16t = 1033
            lf_vfunctab_16t = 1034
            lf_friendcls_16t = 1035
            lf_onemethod_16t = 1036
            lf_vfuncoff_16t = 1037
            lf_ti16_max = 4096
            lf_modifier = 4097
            lf_pointer = 4098
            lf_array_st = 4099
            lf_class_st = 4100
            lf_structure_st = 4101
            lf_union_st = 4102
            lf_enum_st = 4103
            lf_procedure = 4104
            lf_mfunction = 4105
            lf_cobol0 = 4106
            lf_barray = 4107
            lf_dimarray_st = 4108
            lf_vftpath = 4109
            lf_precomp_st = 4110
            lf_oem = 4111
            lf_alias_st = 4112
            lf_oem2 = 4113
            lf_skip = 4608
            lf_arglist = 4609
            lf_defarg_st = 4610
            lf_fieldlist = 4611
            lf_derived = 4612
            lf_bitfield = 4613
            lf_methodlist = 4614
            lf_dimconu = 4615
            lf_dimconlu = 4616
            lf_dimvaru = 4617
            lf_dimvarlu = 4618
            lf_bclass = 5120
            lf_vbclass = 5121
            lf_ivbclass = 5122
            lf_friendfcn_st = 5123
            lf_index = 5124
            lf_member_st = 5125
            lf_stmember_st = 5126
            lf_method_st = 5127
            lf_nesttype_st = 5128
            lf_vfunctab = 5129
            lf_friendcls = 5130
            lf_onemethod_st = 5131
            lf_vfuncoff = 5132
            lf_nesttypeex_st = 5133
            lf_membermodify_st = 5134
            lf_managed_st = 5135
            lf_st_max = 5376
            lf_typeserver = 5377
            lf_enumerate = 5378
            lf_array = 5379
            lf_class = 5380
            lf_structure = 5381
            lf_union = 5382
            lf_enum = 5383
            lf_dimarray = 5384
            lf_precomp = 5385
            lf_alias = 5386
            lf_defarg = 5387
            lf_friendfcn = 5388
            lf_member = 5389
            lf_stmember = 5390
            lf_method = 5391
            lf_nesttype = 5392
            lf_onemethod = 5393
            lf_nesttypeex = 5394
            lf_membermodify = 5395
            lf_managed = 5396
            lf_typeserver2 = 5397
            lf_strided_array = 5398
            lf_hlsl = 5399
            lf_modifier_ex = 5400
            lf_interface = 5401
            lf_binterface = 5402
            lf_vector = 5403
            lf_matrix = 5404
            lf_vftable = 5405
            lf_func_id = 5633
            lf_mfunc_id = 5634
            lf_buildinfo = 5635
            lf_substr_list = 5636
            lf_string_id = 5637
            lf_udt_src_line = 5638
            lf_udt_mod_src_line = 5639
            lf_char = 32768
            lf_short = 32769
            lf_ushort = 32770
            lf_long = 32771
            lf_ulong = 32772
            lf_real32 = 32773
            lf_real64 = 32774
            lf_real80 = 32775
            lf_real128 = 32776
            lf_quadword = 32777
            lf_uquadword = 32778
            lf_real48 = 32779
            lf_complex32 = 32780
            lf_complex64 = 32781
            lf_complex80 = 32782
            lf_complex128 = 32783
            lf_varstring = 32784
            lf_octword = 32791
            lf_uoctword = 32792
            lf_decimal = 32793
            lf_date = 32794
            lf_utf8string = 32795
            lf_real16 = 32796
        def __init__(self, _io, _parent=None, _root=None):
            super(TpiStream.Leaf, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.type = KaitaiStream.resolve_enum(TpiStream.Leaf.LeafType, self._io.read_u2le())
            _on = self.type
            if _on == TpiStream.Leaf.LeafType.lf_arglist:
                pass
                self._raw_body = self._io.read_bytes(self._parent.record_size - 2)
                _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                self.body = TpiStream.LfArglist(_io__raw_body, self, self._root)
            elif _on == TpiStream.Leaf.LeafType.lf_arglist_16t:
                pass
                self._raw_body = self._io.read_bytes(self._parent.record_size - 2)
                _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                self.body = TpiStream.LfArglist16t(_io__raw_body, self, self._root)
            elif _on == TpiStream.Leaf.LeafType.lf_array:
                pass
                self._raw_body = self._io.read_bytes(self._parent.record_size - 2)
                _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                self.body = TpiStream.LfArray(_io__raw_body, self, self._root)
            elif _on == TpiStream.Leaf.LeafType.lf_array_16t:
                pass
                self._raw_body = self._io.read_bytes(self._parent.record_size - 2)
                _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                self.body = TpiStream.LfArray16t(_io__raw_body, self, self._root)
            elif _on == TpiStream.Leaf.LeafType.lf_array_st:
                pass
                self._raw_body = self._io.read_bytes(self._parent.record_size - 2)
                _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                self.body = TpiStream.LfArray(_io__raw_body, self, self._root)
            elif _on == TpiStream.Leaf.LeafType.lf_bitfield:
                pass
                self._raw_body = self._io.read_bytes(self._parent.record_size - 2)
                _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                self.body = TpiStream.LfBitfield(_io__raw_body, self, self._root)
            elif _on == TpiStream.Leaf.LeafType.lf_bitfield_16t:
                pass
                self._raw_body = self._io.read_bytes(self._parent.record_size - 2)
                _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                self.body = TpiStream.LfBitfield16t(_io__raw_body, self, self._root)
            elif _on == TpiStream.Leaf.LeafType.lf_class:
                pass
                self._raw_body = self._io.read_bytes(self._parent.record_size - 2)
                _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                self.body = TpiStream.LfClass(_io__raw_body, self, self._root)
            elif _on == TpiStream.Leaf.LeafType.lf_class_16t:
                pass
                self._raw_body = self._io.read_bytes(self._parent.record_size - 2)
                _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                self.body = TpiStream.LfClass16t(_io__raw_body, self, self._root)
            elif _on == TpiStream.Leaf.LeafType.lf_class_st:
                pass
                self._raw_body = self._io.read_bytes(self._parent.record_size - 2)
                _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                self.body = TpiStream.LfClass(_io__raw_body, self, self._root)
            elif _on == TpiStream.Leaf.LeafType.lf_enum:
                pass
                self._raw_body = self._io.read_bytes(self._parent.record_size - 2)
                _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                self.body = TpiStream.LfEnum(_io__raw_body, self, self._root)
            elif _on == TpiStream.Leaf.LeafType.lf_enum_16t:
                pass
                self._raw_body = self._io.read_bytes(self._parent.record_size - 2)
                _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                self.body = TpiStream.LfEnum16t(_io__raw_body, self, self._root)
            elif _on == TpiStream.Leaf.LeafType.lf_enum_st:
                pass
                self._raw_body = self._io.read_bytes(self._parent.record_size - 2)
                _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                self.body = TpiStream.LfEnum(_io__raw_body, self, self._root)
            elif _on == TpiStream.Leaf.LeafType.lf_fieldlist:
                pass
                self._raw_body = self._io.read_bytes(self._parent.record_size - 2)
                _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                self.body = TpiStream.LfFieldlist(_io__raw_body, self, self._root)
            elif _on == TpiStream.Leaf.LeafType.lf_fieldlist_16t:
                pass
                self._raw_body = self._io.read_bytes(self._parent.record_size - 2)
                _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                self.body = TpiStream.LfFieldlist16t(_io__raw_body, self, self._root)
            elif _on == TpiStream.Leaf.LeafType.lf_interface:
                pass
                self._raw_body = self._io.read_bytes(self._parent.record_size - 2)
                _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                self.body = TpiStream.LfClass(_io__raw_body, self, self._root)
            elif _on == TpiStream.Leaf.LeafType.lf_methodlist:
                pass
                self._raw_body = self._io.read_bytes(self._parent.record_size - 2)
                _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                self.body = TpiStream.LfMethodlist(_io__raw_body, self, self._root)
            elif _on == TpiStream.Leaf.LeafType.lf_methodlist_16t:
                pass
                self._raw_body = self._io.read_bytes(self._parent.record_size - 2)
                _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                self.body = TpiStream.LfMethodlist16t(_io__raw_body, self, self._root)
            elif _on == TpiStream.Leaf.LeafType.lf_mfunction:
                pass
                self._raw_body = self._io.read_bytes(self._parent.record_size - 2)
                _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                self.body = TpiStream.LfMfunction(_io__raw_body, self, self._root)
            elif _on == TpiStream.Leaf.LeafType.lf_mfunction_16t:
                pass
                self._raw_body = self._io.read_bytes(self._parent.record_size - 2)
                _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                self.body = TpiStream.LfMfunction16t(_io__raw_body, self, self._root)
            elif _on == TpiStream.Leaf.LeafType.lf_modifier:
                pass
                self._raw_body = self._io.read_bytes(self._parent.record_size - 2)
                _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                self.body = TpiStream.LfModifier(_io__raw_body, self, self._root)
            elif _on == TpiStream.Leaf.LeafType.lf_modifier_16t:
                pass
                self._raw_body = self._io.read_bytes(self._parent.record_size - 2)
                _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                self.body = TpiStream.LfModifier16t(_io__raw_body, self, self._root)
            elif _on == TpiStream.Leaf.LeafType.lf_pointer:
                pass
                self._raw_body = self._io.read_bytes(self._parent.record_size - 2)
                _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                self.body = TpiStream.LfPointer(_io__raw_body, self, self._root)
            elif _on == TpiStream.Leaf.LeafType.lf_pointer_16t:
                pass
                self._raw_body = self._io.read_bytes(self._parent.record_size - 2)
                _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                self.body = TpiStream.LfPointer16t(_io__raw_body, self, self._root)
            elif _on == TpiStream.Leaf.LeafType.lf_procedure:
                pass
                self._raw_body = self._io.read_bytes(self._parent.record_size - 2)
                _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                self.body = TpiStream.LfProcedure(_io__raw_body, self, self._root)
            elif _on == TpiStream.Leaf.LeafType.lf_procedure_16t:
                pass
                self._raw_body = self._io.read_bytes(self._parent.record_size - 2)
                _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                self.body = TpiStream.LfProcedure16t(_io__raw_body, self, self._root)
            elif _on == TpiStream.Leaf.LeafType.lf_structure:
                pass
                self._raw_body = self._io.read_bytes(self._parent.record_size - 2)
                _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                self.body = TpiStream.LfClass(_io__raw_body, self, self._root)
            elif _on == TpiStream.Leaf.LeafType.lf_structure_16t:
                pass
                self._raw_body = self._io.read_bytes(self._parent.record_size - 2)
                _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                self.body = TpiStream.LfClass16t(_io__raw_body, self, self._root)
            elif _on == TpiStream.Leaf.LeafType.lf_structure_st:
                pass
                self._raw_body = self._io.read_bytes(self._parent.record_size - 2)
                _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                self.body = TpiStream.LfClass(_io__raw_body, self, self._root)
            elif _on == TpiStream.Leaf.LeafType.lf_union:
                pass
                self._raw_body = self._io.read_bytes(self._parent.record_size - 2)
                _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                self.body = TpiStream.LfUnion(_io__raw_body, self, self._root)
            elif _on == TpiStream.Leaf.LeafType.lf_union_16t:
                pass
                self._raw_body = self._io.read_bytes(self._parent.record_size - 2)
                _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                self.body = TpiStream.LfUnion16t(_io__raw_body, self, self._root)
            elif _on == TpiStream.Leaf.LeafType.lf_union_st:
                pass
                self._raw_body = self._io.read_bytes(self._parent.record_size - 2)
                _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                self.body = TpiStream.LfUnion(_io__raw_body, self, self._root)
            elif _on == TpiStream.Leaf.LeafType.lf_vtshape:
                pass
                self._raw_body = self._io.read_bytes(self._parent.record_size - 2)
                _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                self.body = TpiStream.LfVtshape(_io__raw_body, self, self._root)
            else:
                pass
                self.body = self._io.read_bytes(self._parent.record_size - 2)


        def _fetch_instances(self):
            pass
            _on = self.type
            if _on == TpiStream.Leaf.LeafType.lf_arglist:
                pass
                self.body._fetch_instances()
            elif _on == TpiStream.Leaf.LeafType.lf_arglist_16t:
                pass
                self.body._fetch_instances()
            elif _on == TpiStream.Leaf.LeafType.lf_array:
                pass
                self.body._fetch_instances()
            elif _on == TpiStream.Leaf.LeafType.lf_array_16t:
                pass
                self.body._fetch_instances()
            elif _on == TpiStream.Leaf.LeafType.lf_array_st:
                pass
                self.body._fetch_instances()
            elif _on == TpiStream.Leaf.LeafType.lf_bitfield:
                pass
                self.body._fetch_instances()
            elif _on == TpiStream.Leaf.LeafType.lf_bitfield_16t:
                pass
                self.body._fetch_instances()
            elif _on == TpiStream.Leaf.LeafType.lf_class:
                pass
                self.body._fetch_instances()
            elif _on == TpiStream.Leaf.LeafType.lf_class_16t:
                pass
                self.body._fetch_instances()
            elif _on == TpiStream.Leaf.LeafType.lf_class_st:
                pass
                self.body._fetch_instances()
            elif _on == TpiStream.Leaf.LeafType.lf_enum:
                pass
                self.body._fetch_instances()
            elif _on == TpiStream.Leaf.LeafType.lf_enum_16t:
                pass
                self.body._fetch_instances()
            elif _on == TpiStream.Leaf.LeafType.lf_enum_st:
                pass
                self.body._fetch_instances()
            elif _on == TpiStream.Leaf.LeafType.lf_fieldlist:
                pass
                self.body._fetch_instances()
            elif _on == TpiStream.Leaf.LeafType.lf_fieldlist_16t:
                pass
                self.body._fetch_instances()
            elif _on == TpiStream.Leaf.LeafType.lf_interface:
                pass
                self.body._fetch_instances()
            elif _on == TpiStream.Leaf.LeafType.lf_methodlist:
                pass
                self.body._fetch_instances()
            elif _on == TpiStream.Leaf.LeafType.lf_methodlist_16t:
                pass
                self.body._fetch_instances()
            elif _on == TpiStream.Leaf.LeafType.lf_mfunction:
                pass
                self.body._fetch_instances()
            elif _on == TpiStream.Leaf.LeafType.lf_mfunction_16t:
                pass
                self.body._fetch_instances()
            elif _on == TpiStream.Leaf.LeafType.lf_modifier:
                pass
                self.body._fetch_instances()
            elif _on == TpiStream.Leaf.LeafType.lf_modifier_16t:
                pass
                self.body._fetch_instances()
            elif _on == TpiStream.Leaf.LeafType.lf_pointer:
                pass
                self.body._fetch_instances()
            elif _on == TpiStream.Leaf.LeafType.lf_pointer_16t:
                pass
                self.body._fetch_instances()
            elif _on == TpiStream.Leaf.LeafType.lf_procedure:
                pass
                self.body._fetch_instances()
            elif _on == TpiStream.Leaf.LeafType.lf_procedure_16t:
                pass
                self.body._fetch_instances()
            elif _on == TpiStream.Leaf.LeafType.lf_structure:
                pass
                self.body._fetch_instances()
            elif _on == TpiStream.Leaf.LeafType.lf_structure_16t:
                pass
                self.body._fetch_instances()
            elif _on == TpiStream.Leaf.LeafType.lf_structure_st:
                pass
                self.body._fetch_instances()
            elif _on == TpiStream.Leaf.LeafType.lf_union:
                pass
                self.body._fetch_instances()
            elif _on == TpiStream.Leaf.LeafType.lf_union_16t:
                pass
                self.body._fetch_instances()
            elif _on == TpiStream.Leaf.LeafType.lf_union_st:
                pass
                self.body._fetch_instances()
            elif _on == TpiStream.Leaf.LeafType.lf_vtshape:
                pass
                self.body._fetch_instances()
            else:
                pass


    class LfArglist(KaitaiStruct):
        """lfArgList (cvinfo.h)."""
        def __init__(self, _io, _parent=None, _root=None):
            super(TpiStream.LfArglist, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.count = self._io.read_u4le()
            self.args = []
            for i in range(self.count):
                self.args.append(self._io.read_u4le())



        def _fetch_instances(self):
            pass
            for i in range(len(self.args)):
                pass



    class LfArglist16t(KaitaiStruct):
        """lfArgList_16t (cvinfo.h)."""
        def __init__(self, _io, _parent=None, _root=None):
            super(TpiStream.LfArglist16t, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.count = self._io.read_u2le()
            self.args = []
            for i in range(self.count):
                self.args.append(self._io.read_u2le())



        def _fetch_instances(self):
            pass
            for i in range(len(self.args)):
                pass



    class LfArray(KaitaiStruct):
        """lfArray (cvinfo.h)."""
        def __init__(self, _io, _parent=None, _root=None):
            super(TpiStream.LfArray, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.elemtype = self._io.read_u4le()
            self.idxtype = self._io.read_u4le()
            self.length = TpiStream.Numeric(self._io, self, self._root)
            self.name = TpiStream.ZeroTerminatedOrPascalString(self._parent.type == TpiStream.Leaf.LeafType.lf_array, self._io, self, self._root)


        def _fetch_instances(self):
            pass
            self.length._fetch_instances()
            self.name._fetch_instances()


    class LfArray16t(KaitaiStruct):
        """lfArray_16t (cvinfo.h)."""
        def __init__(self, _io, _parent=None, _root=None):
            super(TpiStream.LfArray16t, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.elemtype = self._io.read_u2le()
            self.idxtype = self._io.read_u2le()
            self.length = TpiStream.Numeric(self._io, self, self._root)
            self.name = TpiStream.PascalString(self._io, self, self._root)


        def _fetch_instances(self):
            pass
            self.length._fetch_instances()
            self.name._fetch_instances()


    class LfBclass(KaitaiStruct):
        """lfBClass (cvinfo.h)."""
        def __init__(self, _io, _parent=None, _root=None):
            super(TpiStream.LfBclass, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.attr = self._io.read_u2le()
            self.index = self._io.read_u4le()
            self.offset = TpiStream.Numeric(self._io, self, self._root)


        def _fetch_instances(self):
            pass
            self.offset._fetch_instances()


    class LfBclass16St(KaitaiStruct):
        """lfBClass_16t (cvinfo.h)."""
        def __init__(self, _io, _parent=None, _root=None):
            super(TpiStream.LfBclass16St, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.index = self._io.read_u2le()
            self.attr = self._io.read_u2le()
            self.offset = TpiStream.Numeric(self._io, self, self._root)


        def _fetch_instances(self):
            pass
            self.offset._fetch_instances()


    class LfBitfield(KaitaiStruct):
        """lfBitfield (cvinfo.h)."""
        def __init__(self, _io, _parent=None, _root=None):
            super(TpiStream.LfBitfield, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.type = self._io.read_u4le()
            self.length = self._io.read_u1()
            self.position = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class LfBitfield16t(KaitaiStruct):
        """lfBitfield_16t (cvinfo.h)."""
        def __init__(self, _io, _parent=None, _root=None):
            super(TpiStream.LfBitfield16t, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.length = self._io.read_u1()
            self.position = self._io.read_u1()
            self.type = self._io.read_u2le()


        def _fetch_instances(self):
            pass


    class LfClass(KaitaiStruct):
        """lfClass (cvinfo.h)."""
        def __init__(self, _io, _parent=None, _root=None):
            super(TpiStream.LfClass, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.count = self._io.read_u2le()
            self.property = self._io.read_u2le()
            self.field = self._io.read_u4le()
            self.derived = self._io.read_u4le()
            self.vshape = self._io.read_u4le()
            self.size = TpiStream.Numeric(self._io, self, self._root)
            self.name = TpiStream.ZeroTerminatedOrPascalString( ((self._parent.type == TpiStream.Leaf.LeafType.lf_class) or (self._parent.type == TpiStream.Leaf.LeafType.lf_structure)) , self._io, self, self._root)
            if self.property & 512 != 0:
                pass
                self.unique_name = TpiStream.ZeroTerminatedOrPascalString( ((self._parent.type == TpiStream.Leaf.LeafType.lf_class) or (self._parent.type == TpiStream.Leaf.LeafType.lf_structure)) , self._io, self, self._root)



        def _fetch_instances(self):
            pass
            self.size._fetch_instances()
            self.name._fetch_instances()
            if self.property & 512 != 0:
                pass
                self.unique_name._fetch_instances()



    class LfClass16t(KaitaiStruct):
        """lfClass_16t (cvinfo.h)."""
        def __init__(self, _io, _parent=None, _root=None):
            super(TpiStream.LfClass16t, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.count = self._io.read_u2le()
            self.field = self._io.read_u2le()
            self.property = self._io.read_u2le()
            self.derived = self._io.read_u2le()
            self.vshape = self._io.read_u2le()
            self.size = TpiStream.Numeric(self._io, self, self._root)
            self.name = TpiStream.ZeroTerminatedOrPascalString( ((self._parent.type == TpiStream.Leaf.LeafType.lf_class) or (self._parent.type == TpiStream.Leaf.LeafType.lf_structure)) , self._io, self, self._root)


        def _fetch_instances(self):
            pass
            self.size._fetch_instances()
            self.name._fetch_instances()


    class LfEnum(KaitaiStruct):
        """lfEnum (cvinfo.h)."""
        def __init__(self, _io, _parent=None, _root=None):
            super(TpiStream.LfEnum, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.count = self._io.read_u2le()
            self.property = self._io.read_u2le()
            self.utype = self._io.read_u4le()
            self.field = self._io.read_u4le()
            self.name = TpiStream.ZeroTerminatedOrPascalString(self._parent.type == TpiStream.Leaf.LeafType.lf_enum, self._io, self, self._root)


        def _fetch_instances(self):
            pass
            self.name._fetch_instances()


    class LfEnum16t(KaitaiStruct):
        """lfEnum_16t (cvinfo.h)."""
        def __init__(self, _io, _parent=None, _root=None):
            super(TpiStream.LfEnum16t, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.count = self._io.read_u2le()
            self.utype = self._io.read_u2le()
            self.field = self._io.read_u2le()
            self.property = self._io.read_u2le()
            self.name = TpiStream.PascalString(self._io, self, self._root)


        def _fetch_instances(self):
            pass
            self.name._fetch_instances()


    class LfEnumerate(KaitaiStruct):
        """lfEnumerate (cvinfo.h)."""
        def __init__(self, _io, _parent=None, _root=None):
            super(TpiStream.LfEnumerate, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.attributes = self._io.read_u2le()
            self.value = TpiStream.Numeric(self._io, self, self._root)
            self.name = TpiStream.ZeroTerminatedOrPascalString(self._parent.type == TpiStream.Leaf.LeafType.lf_enumerate, self._io, self, self._root)


        def _fetch_instances(self):
            pass
            self.value._fetch_instances()
            self.name._fetch_instances()


    class LfEnumerateSt16t(KaitaiStruct):
        """lfEnumerate (cvinfo.h)."""
        def __init__(self, _io, _parent=None, _root=None):
            super(TpiStream.LfEnumerateSt16t, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.attributes = self._io.read_u2le()
            self.value = TpiStream.Numeric(self._io, self, self._root)
            self.name = TpiStream.PascalString(self._io, self, self._root)


        def _fetch_instances(self):
            pass
            self.value._fetch_instances()
            self.name._fetch_instances()


    class LfFieldlist(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(TpiStream.LfFieldlist, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.items = []
            i = 0
            while not self._io.is_eof():
                self.items.append(TpiStream.FieldListItem(self._io, self, self._root))
                i += 1



        def _fetch_instances(self):
            pass
            for i in range(len(self.items)):
                pass
                self.items[i]._fetch_instances()



    class LfFieldlist16t(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(TpiStream.LfFieldlist16t, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.items = []
            i = 0
            while not self._io.is_eof():
                self.items.append(TpiStream.FieldList16tItem(self._io, self, self._root))
                i += 1



        def _fetch_instances(self):
            pass
            for i in range(len(self.items)):
                pass
                self.items[i]._fetch_instances()



    class LfIndex(KaitaiStruct):
        """lfIndex_16t (cvinfo)."""
        def __init__(self, _io, _parent=None, _root=None):
            super(TpiStream.LfIndex, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.padding = self._io.read_u2le()
            self.index = self._io.read_u4le()


        def _fetch_instances(self):
            pass


    class LfIndex16t(KaitaiStruct):
        """lfIndex_16t (cvinfo)."""
        def __init__(self, _io, _parent=None, _root=None):
            super(TpiStream.LfIndex16t, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.index = self._io.read_u2le()


        def _fetch_instances(self):
            pass


    class LfMember(KaitaiStruct):
        """lfMember."""
        def __init__(self, _io, _parent=None, _root=None):
            super(TpiStream.LfMember, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.attr = self._io.read_u2le()
            self.index = self._io.read_u4le()
            self.offset = TpiStream.Numeric(self._io, self, self._root)
            self.name = TpiStream.ZeroTerminatedOrPascalString(self._parent.type == TpiStream.Leaf.LeafType.lf_member, self._io, self, self._root)


        def _fetch_instances(self):
            pass
            self.offset._fetch_instances()
            self.name._fetch_instances()


    class LfMember16t(KaitaiStruct):
        """lfMember_16t."""
        def __init__(self, _io, _parent=None, _root=None):
            super(TpiStream.LfMember16t, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.index = self._io.read_u2le()
            self.attr = self._io.read_u2le()
            self.offset = TpiStream.Numeric(self._io, self, self._root)
            self.name = TpiStream.PascalString(self._io, self, self._root)


        def _fetch_instances(self):
            pass
            self.offset._fetch_instances()
            self.name._fetch_instances()


    class LfMethod(KaitaiStruct):
        """lfMethod."""
        def __init__(self, _io, _parent=None, _root=None):
            super(TpiStream.LfMethod, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.count = self._io.read_u2le()
            self.m_list = self._io.read_u4le()
            self.name = TpiStream.ZeroTerminatedOrPascalString(self._parent.type == TpiStream.Leaf.LeafType.lf_method, self._io, self, self._root)


        def _fetch_instances(self):
            pass
            self.name._fetch_instances()


    class LfMethod16t(KaitaiStruct):
        """lfMethod_16t."""
        def __init__(self, _io, _parent=None, _root=None):
            super(TpiStream.LfMethod16t, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.count = self._io.read_u2le()
            self.m_list = self._io.read_u2le()
            self.name = TpiStream.PascalString(self._io, self, self._root)


        def _fetch_instances(self):
            pass
            self.name._fetch_instances()


    class LfMethodlist(KaitaiStruct):
        """lfMethodList (cvinfo.h)."""
        def __init__(self, _io, _parent=None, _root=None):
            super(TpiStream.LfMethodlist, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.items = []
            i = 0
            while not self._io.is_eof():
                self.items.append(TpiStream.LfMethodlistItem(self._io, self, self._root))
                i += 1



        def _fetch_instances(self):
            pass
            for i in range(len(self.items)):
                pass
                self.items[i]._fetch_instances()



    class LfMethodlist16t(KaitaiStruct):
        """lfMethodList_16t (cvinfo.h)."""
        def __init__(self, _io, _parent=None, _root=None):
            super(TpiStream.LfMethodlist16t, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.items = []
            i = 0
            while not self._io.is_eof():
                self.items.append(TpiStream.LfMethodlist16tItem(self._io, self, self._root))
                i += 1



        def _fetch_instances(self):
            pass
            for i in range(len(self.items)):
                pass
                self.items[i]._fetch_instances()



    class LfMethodlist16tItem(KaitaiStruct):
        """mlMethod_16t (DumpTypRecC7 -> LF_METHODLIST_16t)."""
        def __init__(self, _io, _parent=None, _root=None):
            super(TpiStream.LfMethodlist16tItem, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.attr = self._io.read_u2le()
            self.index = self._io.read_u2le()
            if  ((self.attr >> 2 & 7 == 4) or (self.attr >> 2 & 7 == 6)) :
                pass
                self.vfptr_offset = self._io.read_u4le()



        def _fetch_instances(self):
            pass
            if  ((self.attr >> 2 & 7 == 4) or (self.attr >> 2 & 7 == 6)) :
                pass



    class LfMethodlistItem(KaitaiStruct):
        """mlMethod (DumpTypRecC7 -> LF_METHODLIST)."""
        def __init__(self, _io, _parent=None, _root=None):
            super(TpiStream.LfMethodlistItem, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.attr = self._io.read_u2le()
            self.pad0 = self._io.read_u2le()
            self.index = self._io.read_u4le()
            if  ((self.attr >> 2 & 7 == 4) or (self.attr >> 2 & 7 == 6)) :
                pass
                self.vfptr_offset = self._io.read_u4le()



        def _fetch_instances(self):
            pass
            if  ((self.attr >> 2 & 7 == 4) or (self.attr >> 2 & 7 == 6)) :
                pass



    class LfMfunction(KaitaiStruct):
        """lfMFunc_16t (cvinfo.h)."""
        def __init__(self, _io, _parent=None, _root=None):
            super(TpiStream.LfMfunction, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.rvtype = self._io.read_u4le()
            self.classtype = self._io.read_u4le()
            self.thistype = self._io.read_u4le()
            self.calltype = self._io.read_u1()
            self.funcattr = self._io.read_u1()
            self.parmcount = self._io.read_u2le()
            self.arglist = self._io.read_u4le()
            self.thisadjust = self._io.read_u4le()


        def _fetch_instances(self):
            pass


    class LfMfunction16t(KaitaiStruct):
        """lfMFunc_16t (cvinfo.h)."""
        def __init__(self, _io, _parent=None, _root=None):
            super(TpiStream.LfMfunction16t, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.rvtype = self._io.read_u2le()
            self.classtype = self._io.read_u2le()
            self.thistype = self._io.read_u2le()
            self.calltype = self._io.read_u1()
            self.funcattr = self._io.read_u1()
            self.parmcount = self._io.read_u2le()
            self.arglist = self._io.read_u2le()
            self.thisadjust = self._io.read_u4le()


        def _fetch_instances(self):
            pass


    class LfModifier(KaitaiStruct):
        """lfModifier_16t (cvinfo.h)."""
        def __init__(self, _io, _parent=None, _root=None):
            super(TpiStream.LfModifier, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.type = self._io.read_u4le()
            self.attr = self._io.read_u2le()


        def _fetch_instances(self):
            pass


    class LfModifier16t(KaitaiStruct):
        """lfModifier_16t (cvinfo.h)."""
        def __init__(self, _io, _parent=None, _root=None):
            super(TpiStream.LfModifier16t, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.attr = self._io.read_u2le()
            self.type = self._io.read_u2le()


        def _fetch_instances(self):
            pass


    class LfNesttype(KaitaiStruct):
        """lfNestType."""
        def __init__(self, _io, _parent=None, _root=None):
            super(TpiStream.LfNesttype, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.pad0 = self._io.read_u2le()
            self.index = self._io.read_u4le()
            self.name = TpiStream.ZeroTerminatedOrPascalString(self._parent.type == TpiStream.Leaf.LeafType.lf_nesttype, self._io, self, self._root)


        def _fetch_instances(self):
            pass
            self.name._fetch_instances()


    class LfNesttype16t(KaitaiStruct):
        """lfNestType_16t."""
        def __init__(self, _io, _parent=None, _root=None):
            super(TpiStream.LfNesttype16t, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.index = self._io.read_u2le()
            self.name = TpiStream.PascalString(self._io, self, self._root)


        def _fetch_instances(self):
            pass
            self.name._fetch_instances()


    class LfOnemethod(KaitaiStruct):
        """lfOneMethod."""
        def __init__(self, _io, _parent=None, _root=None):
            super(TpiStream.LfOnemethod, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.attr = self._io.read_u2le()
            self.index = self._io.read_u4le()
            if  (((self.attr & 28) >> 2 == 4) or ((self.attr & 28) >> 2 == 6)) :
                pass
                self.vfptr_offset = self._io.read_u4le()

            self.name = TpiStream.ZeroTerminatedOrPascalString(self._parent.type == TpiStream.Leaf.LeafType.lf_onemethod, self._io, self, self._root)


        def _fetch_instances(self):
            pass
            if  (((self.attr & 28) >> 2 == 4) or ((self.attr & 28) >> 2 == 6)) :
                pass

            self.name._fetch_instances()


    class LfOnemethod16t(KaitaiStruct):
        """lfOneMethod_16t."""
        def __init__(self, _io, _parent=None, _root=None):
            super(TpiStream.LfOnemethod16t, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.attr = self._io.read_u2le()
            self.index = self._io.read_u2le()
            if  (((self.attr & 28) >> 2 == 4) or ((self.attr & 28) >> 2 == 6)) :
                pass
                self.vfptr_offset = self._io.read_u4le()

            self.name = TpiStream.PascalString(self._io, self, self._root)


        def _fetch_instances(self):
            pass
            if  (((self.attr & 28) >> 2 == 4) or ((self.attr & 28) >> 2 == 6)) :
                pass

            self.name._fetch_instances()


    class LfPointer(KaitaiStruct):
        """lfPointer (cvinfo.h)."""
        def __init__(self, _io, _parent=None, _root=None):
            super(TpiStream.LfPointer, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.utype = self._io.read_u4le()
            self.attr = self._io.read_u4le()
            if  (((self.attr & 224) >> 5 == 2) or ((self.attr & 224) >> 5 == 3)) :
                pass
                self.pm = TpiStream.LfPointerPm(self._io, self, self._root)



        def _fetch_instances(self):
            pass
            if  (((self.attr & 224) >> 5 == 2) or ((self.attr & 224) >> 5 == 3)) :
                pass
                self.pm._fetch_instances()



    class LfPointer16t(KaitaiStruct):
        """lfPointer_16t (cvinfo.h)."""
        def __init__(self, _io, _parent=None, _root=None):
            super(TpiStream.LfPointer16t, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.attr = self._io.read_u2le()
            self.utype = self._io.read_u2le()
            if  (((self.attr & 224) >> 5 == 2) or ((self.attr & 224) >> 5 == 3)) :
                pass
                self.pm = TpiStream.LfPointer16tPm(self._io, self, self._root)



        def _fetch_instances(self):
            pass
            if  (((self.attr & 224) >> 5 == 2) or ((self.attr & 224) >> 5 == 3)) :
                pass
                self.pm._fetch_instances()



    class LfPointer16tPm(KaitaiStruct):
        """lfPointer_16t.pbase.pm."""
        def __init__(self, _io, _parent=None, _root=None):
            super(TpiStream.LfPointer16tPm, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.pmclass = self._io.read_u2le()
            self.pmenum = self._io.read_u2le()


        def _fetch_instances(self):
            pass


    class LfPointerPm(KaitaiStruct):
        """lfPointer.pbase.pm."""
        def __init__(self, _io, _parent=None, _root=None):
            super(TpiStream.LfPointerPm, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.pmclass = self._io.read_u4le()
            self.pmenum = self._io.read_u2le()


        def _fetch_instances(self):
            pass


    class LfProcedure(KaitaiStruct):
        """lfProc (cvinfo.h)."""
        def __init__(self, _io, _parent=None, _root=None):
            super(TpiStream.LfProcedure, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.rvtype = self._io.read_u4le()
            self.calltype = self._io.read_u1()
            self.funcattr = self._io.read_u1()
            self.parmcount = self._io.read_u2le()
            self.arglist = self._io.read_u4le()


        def _fetch_instances(self):
            pass


    class LfProcedure16t(KaitaiStruct):
        """lfProc_16t (cvinfo.h)."""
        def __init__(self, _io, _parent=None, _root=None):
            super(TpiStream.LfProcedure16t, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.rvtype = self._io.read_u2le()
            self.calltype = self._io.read_u1()
            self.funcattr = self._io.read_u1()
            self.parmcount = self._io.read_u2le()
            self.arglist = self._io.read_u2le()


        def _fetch_instances(self):
            pass


    class LfStmember(KaitaiStruct):
        """lfSTMember."""
        def __init__(self, _io, _parent=None, _root=None):
            super(TpiStream.LfStmember, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.attr = self._io.read_u2le()
            self.index = self._io.read_u4le()
            self.name = TpiStream.ZeroTerminatedOrPascalString(self._parent.type == TpiStream.Leaf.LeafType.lf_stmember, self._io, self, self._root)


        def _fetch_instances(self):
            pass
            self.name._fetch_instances()


    class LfStmember16t(KaitaiStruct):
        """lfSTMember_16t."""
        def __init__(self, _io, _parent=None, _root=None):
            super(TpiStream.LfStmember16t, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.index = self._io.read_u2le()
            self.attr = self._io.read_u2le()
            self.name = TpiStream.PascalString(self._io, self, self._root)


        def _fetch_instances(self):
            pass
            self.name._fetch_instances()


    class LfUnion(KaitaiStruct):
        """lfUnion (cvinfo.h)."""
        def __init__(self, _io, _parent=None, _root=None):
            super(TpiStream.LfUnion, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.count = self._io.read_u2le()
            self.property = self._io.read_u2le()
            self.field = self._io.read_u4le()
            self.size = TpiStream.Numeric(self._io, self, self._root)
            self.name = TpiStream.ZeroTerminatedOrPascalString(self._parent.type == TpiStream.Leaf.LeafType.lf_union, self._io, self, self._root)


        def _fetch_instances(self):
            pass
            self.size._fetch_instances()
            self.name._fetch_instances()


    class LfUnion16t(KaitaiStruct):
        """lfUnion_16t (cvinfo.h)."""
        def __init__(self, _io, _parent=None, _root=None):
            super(TpiStream.LfUnion16t, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.count = self._io.read_u2le()
            self.field = self._io.read_u2le()
            self.property = self._io.read_u2le()
            self.size = TpiStream.Numeric(self._io, self, self._root)
            self.name = TpiStream.PascalString(self._io, self, self._root)


        def _fetch_instances(self):
            pass
            self.size._fetch_instances()
            self.name._fetch_instances()


    class LfVbclass16t(KaitaiStruct):
        """lfVBClass_16t (cvinfo.h)."""
        def __init__(self, _io, _parent=None, _root=None):
            super(TpiStream.LfVbclass16t, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.index = self._io.read_u2le()
            self.vbptr = self._io.read_u2le()
            self.attr = self._io.read_u2le()
            self.vbpoff = TpiStream.Numeric(self._io, self, self._root)
            self.vbind = TpiStream.Numeric(self._io, self, self._root)


        def _fetch_instances(self):
            pass
            self.vbpoff._fetch_instances()
            self.vbind._fetch_instances()


    class LfVfunctab(KaitaiStruct):
        """lfVFuncTab."""
        def __init__(self, _io, _parent=None, _root=None):
            super(TpiStream.LfVfunctab, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.pad0 = self._io.read_u2le()
            self.type = self._io.read_u4le()


        def _fetch_instances(self):
            pass


    class LfVfunctab16t(KaitaiStruct):
        """lfVFuncTab_16t."""
        def __init__(self, _io, _parent=None, _root=None):
            super(TpiStream.LfVfunctab16t, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.type = self._io.read_u2le()


        def _fetch_instances(self):
            pass


    class LfVtshape(KaitaiStruct):
        """lfVTShape (cvinfo.h)."""
        def __init__(self, _io, _parent=None, _root=None):
            super(TpiStream.LfVtshape, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.count = self._io.read_u2le()
            self.desc = []
            for i in range((self.count + 1) // 2):
                self.desc.append(self._io.read_u1())



        def _fetch_instances(self):
            pass
            for i in range(len(self.desc)):
                pass



    class Numeric(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(TpiStream.Numeric, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.tag = self._io.read_u2le()
            if self.tag == 32768:
                pass
                self.char_ = self._io.read_s1()

            if self.tag == 32769:
                pass
                self.short_ = self._io.read_s2le()

            if self.tag == 32770:
                pass
                self.ushort = self._io.read_u2le()

            if self.tag == 32771:
                pass
                self.long = self._io.read_s4le()

            if self.tag == 32772:
                pass
                self.ulong = self._io.read_u4le()

            if self.tag == 32773:
                pass
                self.real32 = self._io.read_f4le()

            if self.tag == 32774:
                pass
                self.real64 = self._io.read_f8le()

            if self.tag == 32775:
                pass
                self.real80 = self._io.read_bytes(10)

            if self.tag == 32776:
                pass
                self.real128 = self._io.read_bytes(18)

            if self.tag == 32777:
                pass
                self.quadword = self._io.read_s8le()

            if self.tag == 32778:
                pass
                self.uquadword = self._io.read_u8le()

            if self.tag == 32779:
                pass
                self.real48 = self._io.read_bytes(6)

            if self.tag == 32780:
                pass
                self.complex32 = TpiStream.Complex32(self._io, self, self._root)

            if self.tag == 32781:
                pass
                self.complex64 = TpiStream.Complex64(self._io, self, self._root)

            if self.tag == 32782:
                pass
                self.complex80 = TpiStream.Complex80(self._io, self, self._root)

            if self.tag == 32783:
                pass
                self.complex128 = TpiStream.Complex128(self._io, self, self._root)

            if self.tag == 32784:
                pass
                self.varstring = TpiStream.Varstring(self._io, self, self._root)

            if self.tag == 32791:
                pass
                self.octword = self._io.read_bytes(16)

            if self.tag == 32792:
                pass
                self.uoctword = self._io.read_bytes(16)

            if self.tag == 32793:
                pass
                self.decimal = TpiStream.Decimal(self._io, self, self._root)

            if self.tag == 32794:
                pass
                self.date = self._io.read_f8le()

            if self.tag == 32795:
                pass
                self.utf8string = (self._io.read_bytes_term(0, False, True, True)).decode(u"UTF-8")

            if self.tag == 32796:
                pass
                self.real16 = self._io.read_bytes(2)



        def _fetch_instances(self):
            pass
            if self.tag == 32768:
                pass

            if self.tag == 32769:
                pass

            if self.tag == 32770:
                pass

            if self.tag == 32771:
                pass

            if self.tag == 32772:
                pass

            if self.tag == 32773:
                pass

            if self.tag == 32774:
                pass

            if self.tag == 32775:
                pass

            if self.tag == 32776:
                pass

            if self.tag == 32777:
                pass

            if self.tag == 32778:
                pass

            if self.tag == 32779:
                pass

            if self.tag == 32780:
                pass
                self.complex32._fetch_instances()

            if self.tag == 32781:
                pass
                self.complex64._fetch_instances()

            if self.tag == 32782:
                pass
                self.complex80._fetch_instances()

            if self.tag == 32783:
                pass
                self.complex128._fetch_instances()

            if self.tag == 32784:
                pass
                self.varstring._fetch_instances()

            if self.tag == 32791:
                pass

            if self.tag == 32792:
                pass

            if self.tag == 32793:
                pass
                self.decimal._fetch_instances()

            if self.tag == 32794:
                pass

            if self.tag == 32795:
                pass

            if self.tag == 32796:
                pass



    class OffsetCount(KaitaiStruct):
        """OffCb (tpi.h)."""
        def __init__(self, _io, _parent=None, _root=None):
            super(TpiStream.OffsetCount, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.offset = self._io.read_u4le()
            self.count = self._io.read_u4le()


        def _fetch_instances(self):
            pass


    class PascalString(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(TpiStream.PascalString, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.len = self._io.read_u1()
            self.text = (self._io.read_bytes(self.len)).decode(u"ASCII")


        def _fetch_instances(self):
            pass


    class Record(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(TpiStream.Record, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.record_size = self._io.read_u2le()
            self._raw_leaf = self._io.read_bytes(self.record_size)
            _io__raw_leaf = KaitaiStream(BytesIO(self._raw_leaf))
            self.leaf = TpiStream.Leaf(_io__raw_leaf, self, self._root)


        def _fetch_instances(self):
            pass
            self.leaf._fetch_instances()


    class TpiHeader(KaitaiStruct):
        def __init__(self, version, _io, _parent=None, _root=None):
            super(TpiStream.TpiHeader, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self.version = version
            self._read()

        def _read(self):
            if self.use_16t:
                pass
                self.header_16t = TpiStream.TpiHeader16t(self._io, self, self._root)

            if self.use_new:
                pass
                self.header_new = TpiStream.TpiHeaderNew(self._io, self, self._root)



        def _fetch_instances(self):
            pass
            if self.use_16t:
                pass
                self.header_16t._fetch_instances()

            if self.use_new:
                pass
                self.header_new._fetch_instances()


        @property
        def records_byte_size(self):
            if hasattr(self, '_m_records_byte_size'):
                return self._m_records_byte_size

            self._m_records_byte_size = (self.header_16t.records_byte_size if self.use_16t else self.header_new.records_byte_size)
            return getattr(self, '_m_records_byte_size', None)

        @property
        def ti_max(self):
            if hasattr(self, '_m_ti_max'):
                return self._m_ti_max

            self._m_ti_max = (self.header_16t.ti_max if self.use_16t else self.header_new.ti_max)
            return getattr(self, '_m_ti_max', None)

        @property
        def ti_min(self):
            if hasattr(self, '_m_ti_min'):
                return self._m_ti_min

            self._m_ti_min = (self.header_16t.ti_min if self.use_16t else self.header_new.ti_min)
            return getattr(self, '_m_ti_min', None)

        @property
        def use_16t(self):
            if hasattr(self, '_m_use_16t'):
                return self._m_use_16t

            self._m_use_16t =  ((self.version == 920924) or (self.version == 19951122)) 
            return getattr(self, '_m_use_16t', None)

        @property
        def use_new(self):
            if hasattr(self, '_m_use_new'):
                return self._m_use_new

            self._m_use_new =  ((self.version == 19961031) or (self.version == 20040203)) 
            return getattr(self, '_m_use_new', None)


    class TpiHeader16t(KaitaiStruct):
        """HDR_16t (tpi.h)."""
        def __init__(self, _io, _parent=None, _root=None):
            super(TpiStream.TpiHeader16t, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.ti_min = self._io.read_u2le()
            self.ti_max = self._io.read_u2le()
            self.records_byte_size = self._io.read_u4le()
            self.hash_value_stream = self._io.read_u2le()
            self.padding = self._io.read_u2le()


        def _fetch_instances(self):
            pass


    class TpiHeaderNew(KaitaiStruct):
        """HDR (tpi.h)."""
        def __init__(self, _io, _parent=None, _root=None):
            super(TpiStream.TpiHeaderNew, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.header_size = self._io.read_u4le()
            self.ti_min = self._io.read_u4le()
            self.ti_max = self._io.read_u4le()
            self.records_byte_size = self._io.read_u4le()
            self.hash_stream_schema = TpiStream.TpiHeaderNewHash(self._io, self, self._root)
            self.padding = self._io.read_bytes(self.header_size - self._io.pos())


        def _fetch_instances(self):
            pass
            self.hash_stream_schema._fetch_instances()


    class TpiHeaderNewHash(KaitaiStruct):
        """TpiHash (dbi.h)."""
        def __init__(self, _io, _parent=None, _root=None):
            super(TpiStream.TpiHeaderNewHash, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.main_hash_stream = self._io.read_u2le()
            self.auxiliary_hash_data_stream = self._io.read_u2le()
            self.count_hash_buckets = self._io.read_u4le()
            self.hash_values_location = TpiStream.OffsetCount(self._io, self, self._root)
            self.ti_off_location = TpiStream.OffsetCount(self._io, self, self._root)
            self.hash_adj_location = TpiStream.OffsetCount(self._io, self, self._root)


        def _fetch_instances(self):
            pass
            self.hash_values_location._fetch_instances()
            self.ti_off_location._fetch_instances()
            self.hash_adj_location._fetch_instances()


    class Varstring(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(TpiStream.Varstring, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.len = self._io.read_u2le()
            self.text = self._io.read_bytes(self.len)


        def _fetch_instances(self):
            pass


    class ZeroTerminatedOrPascalString(KaitaiStruct):
        def __init__(self, zero_terminated, _io, _parent=None, _root=None):
            super(TpiStream.ZeroTerminatedOrPascalString, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self.zero_terminated = zero_terminated
            self._read()

        def _read(self):
            if self.zero_terminated:
                pass
                self.text_zero_terminated = (self._io.read_bytes_term(0, False, True, True)).decode(u"ASCII")

            if (not (self.zero_terminated)):
                pass
                self.text_pascal = TpiStream.PascalString(self._io, self, self._root)



        def _fetch_instances(self):
            pass
            if self.zero_terminated:
                pass

            if (not (self.zero_terminated)):
                pass
                self.text_pascal._fetch_instances()


        @property
        def text(self):
            if hasattr(self, '_m_text'):
                return self._m_text

            self._m_text = (self.text_zero_terminated if self.zero_terminated else self.text_pascal.text)
            return getattr(self, '_m_text', None)



