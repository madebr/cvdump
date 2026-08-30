meta:
  id: tpi_stream
  imports:
    - numeric
    - pascal_string
    - strz_or_pascal
  endian: le
doc: HDR_16t (tpi.h)
seq:
  - id: version
    type: u4
    valid:
      any-of: [920924, 19951122, 19961031, 20040203]
  - id: header
    type: tpi_header(version)
  - id: records
    type: record
#    size: header.records_byte_size
    repeat: expr
    repeat-expr: header.ti_max - header.ti_min

types:
  records:
    seq:
      - id: records
        type: record
        repeat: eos
  tpi_header:
    params:
      - id: version
        type: u4
    seq:
      - id: header_16t
        type: tpi_header_16t
        if: use_16t
      - id: header_new
        type: tpi_header_new
        if: use_new
    instances:
      use_16t:
        value: version == 920924 or version == 19951122
      use_new:
        value: version == 19961031 or version == 20040203
      ti_min:
        value: 'use_16t ? header_16t.ti_min : header_new.ti_min'
      ti_max:
        value: 'use_16t ? header_16t.ti_max : header_new.ti_max'
      records_byte_size:
        value: 'use_16t ? header_16t.records_byte_size : header_new.records_byte_size'

  tpi_header_16t:
    doc: HDR_16t (tpi.h)
    seq:
    - id: ti_min
      type: u2
      doc: lowest TI
    - id: ti_max
      type: u2
      doc: highest TI + 1
    - id: records_byte_size
      type: u4
      doc: count of bytes used by the gprec which follows
    - id: hash_value_stream
      type: u2
      doc: stream to hold hash values
    - id: padding
      type: u2

  tpi_header_new:
    doc: HDR (tpi.h)
    seq:
      - id: header_size
        type: u4
        doc: 'cbHdr: size of the header, allows easier upgrading and backwards compatibility'
      - id: ti_min
        type: u4
        doc: 'tiMin: lowest TI'
      - id: ti_max
        type: u4
        doc: 'tiMac: highest TI + 1'
      - id: records_byte_size
        type: u4
        doc: 'cbGprec: count of bytes used by the gprec which follows'
      - id: hash_stream_schema
        type: tpi_header_new_hash
        doc: 'tpihash: hash stream schema'
      - id: padding
        size: header_size - _io.pos

  tpi_header_new_hash:
    doc: TpiHash (dbi.h)
    seq:
      - id: main_hash_stream
        type: u2
        doc: 'sn: main hash stream'
      - id: auxiliary_hash_data_stream
        type: u2
        doc: 'snPad: auxiliary hash data if necessary'
      - id: count_hash_buckets
        type: u4
        doc: 'cHashBuckets: how many buckets we have'
      - id: hash_values_location
        type: offset_count
        doc: 'offcbHashVals: offcb of hashvals'
      - id: ti_off_location
        type: offset_count
        doc: 'offcb of (TI,OFF) pairs'
      - id: hash_adj_location
        type: offset_count
        doc: 'offcb of hash head list, maps (hashval,ti), where ti is the head of the hashval chain'

  offset_count:
    doc: OffCb (tpi.h)
    seq:
      - id: offset
        type: u4
      - id: count
        type: u4

  record:
    seq:
      - id: record_size
        type: u2
      - id: leaf
        type: leaf
        size: record_size

  leaf:
    seq:
      - id: type
        type: u2
        enum: leaf_type
      - id: body
        size: _parent.record_size - 2
        type:
          switch-on: type
          cases:
            # TPI
            'leaf_type::lf_fieldlist_16t': lf_fieldlist_16t
            'leaf_type::lf_fieldlist': lf_fieldlist
            'leaf::leaf_type::lf_enum_16t': lf_enum_16t
            'leaf::leaf_type::lf_enum': lf_enum
            'leaf::leaf_type::lf_enum_st': lf_enum
            'leaf::leaf_type::lf_structure_16t': lf_class_16t
            'leaf::leaf_type::lf_class_16t': lf_class_16t
            'leaf::leaf_type::lf_array_16t': lf_array_16t
            'leaf::leaf_type::lf_arglist_16t': lf_arglist_16t
            'leaf::leaf_type::lf_arglist': lf_arglist
            'leaf::leaf_type::lf_procedure_16t': lf_procedure_16t
            'leaf::leaf_type::lf_procedure': lf_procedure
            'leaf::leaf_type::lf_pointer_16t': lf_pointer_16t
            'leaf::leaf_type::lf_modifier_16t': lf_modifier_16t
            'leaf::leaf_type::lf_modifier': lf_modifier
            'leaf::leaf_type::lf_mfunction_16t': lf_mfunction_16t
            'leaf::leaf_type::lf_mfunction': lf_mfunction
            'leaf::leaf_type::lf_methodlist_16t': lf_methodlist_16t
            'leaf::leaf_type::lf_methodlist': lf_methodlist
            'leaf::leaf_type::lf_vtshape': lf_vtshape
            'leaf::leaf_type::lf_union_16t': lf_union_16t
            'leaf::leaf_type::lf_union': lf_union
            'leaf::leaf_type::lf_union_st': lf_union
            'leaf::leaf_type::lf_bitfield_16t': lf_bitfield_16t
            'leaf::leaf_type::lf_bitfield': lf_bitfield
            'leaf::leaf_type::lf_array': lf_array
            'leaf::leaf_type::lf_array_st': lf_array
            'leaf::leaf_type::lf_class_st': lf_class
            'leaf::leaf_type::lf_structure_st': lf_class
            'leaf::leaf_type::lf_class': lf_class
            'leaf::leaf_type::lf_structure': lf_class
            'leaf::leaf_type::lf_interface': lf_class
            'leaf::leaf_type::lf_pointer': lf_pointer

            # IPI
            'leaf::leaf_type::lf_udt_mod_src_line': lf_udt_mod_src_line
            'leaf::leaf_type::lf_string_id': lf_string_id
            'leaf::leaf_type::lf_substr_list': lf_arglist
            'leaf::leaf_type::lf_buildinfo': lf_buildinfo
            'leaf::leaf_type::lf_func_id': lf_func_id
            'leaf::leaf_type::lf_mfunc_id': lf_mfunc_id

            # COFF: .debug$T (Visual Studio 4.2)
            'leaf::leaf_type::lf_typeserver_st': lf_typeserver_st
            # COFF: .debug$T (Visual Studio 2012)
            'leaf::leaf_type::lf_typeserver2': lf_typeserver2
    enums:
      leaf_type:
        0x0001: lf_modifier_16t
        0x0002: lf_pointer_16t
        0x0003: lf_array_16t
        0x0004: lf_class_16t
        0x0005: lf_structure_16t
        0x0006: lf_union_16t
        0x0007: lf_enum_16t
        0x0008: lf_procedure_16t
        0x0009: lf_mfunction_16t
        0x000a: lf_vtshape
        0x000b: lf_cobol0_16t
        0x000c: lf_cobol1
        0x000d: lf_barray_16t
        0x000e: lf_label
        0x000f: lf_null
        0x0010: lf_nottran
        0x0011: lf_dimarray_16t
        0x0012: lf_vftpath_16t
        0x0013: lf_precomp_16t        # not referenced from symbol
        0x0014: lf_endprecomp         # not referenced from symbol
        0x0015: lf_oem_16t            # oem definable type string
        0x0016: lf_typeserver_st      # not referenced from symbol
        # leaf indices starting records but referenced only from
        0x0200: lf_skip_16t
        0x0201: lf_arglist_16t
        0x0202: lf_defarg_16t
        0x0203: lf_list
        0x0204: lf_fieldlist_16t
        0x0205: lf_derived_16t
        0x0206: lf_bitfield_16t
        0x0207: lf_methodlist_16t
        0x0208: lf_dimconu_16t
        0x0209: lf_dimconlu_16t
        0x020a: lf_dimvaru_16t
        0x020b: lf_dimvarlu_16t
        0x020c: lf_refsym

        0x0400: lf_bclass_16t
        0x0401: lf_vbclass_16t
        0x0402: lf_ivbclass_16t
        0x0403: lf_enumerate_st
        0x0404: lf_friendfcn_16t
        0x0405: lf_index_16t
        0x0406: lf_member_16t
        0x0407: lf_stmember_16t
        0x0408: lf_method_16t
        0x0409: lf_nesttype_16t
        0x040a: lf_vfunctab_16t
        0x040b: lf_friendcls_16t
        0x040c: lf_onemethod_16t
        0x040d: lf_vfuncoff_16t

        # 32-bit type index versions of leaves, all have the 0x1000 bit set
        0x1000: lf_ti16_max

        0x1001: lf_modifier
        0x1002: lf_pointer
        0x1003: lf_array_st
        0x1004: lf_class_st
        0x1005: lf_structure_st
        0x1006: lf_union_st
        0x1007: lf_enum_st
        0x1008: lf_procedure
        0x1009: lf_mfunction
        0x100a: lf_cobol0
        0x100b: lf_barray
        0x100c: lf_dimarray_st
        0x100d: lf_vftpath
        0x100e: lf_precomp_st         # not referenced from symbol
        0x100f: lf_oem                # oem definable type string
        0x1010: lf_alias_st           # alias (typedef) type
        0x1011: lf_oem2               # oem definable type string
        # leaf indices starting records but referenced only from type records
        0x1200: lf_skip
        0x1201: lf_arglist
        0x1202: lf_defarg_st
        0x1203: lf_fieldlist
        0x1204: lf_derived
        0x1205: lf_bitfield
        0x1206: lf_methodlist
        0x1207: lf_dimconu
        0x1208: lf_dimconlu
        0x1209: lf_dimvaru
        0x120a: lf_dimvarlu

        0x1400: lf_bclass
        0x1401: lf_vbclass
        0x1402: lf_ivbclass
        0x1403: lf_friendfcn_st
        0x1404: lf_index
        0x1405: lf_member_st
        0x1406: lf_stmember_st
        0x1407: lf_method_st
        0x1408: lf_nesttype_st
        0x1409: lf_vfunctab
        0x140a: lf_friendcls
        0x140b: lf_onemethod_st
        0x140c: lf_vfuncoff
        0x140d: lf_nesttypeex_st
        0x140e: lf_membermodify_st
        0x140f: lf_managed_st
        # Types w/ SZ names
        0x1500: lf_st_max

        0x1501: lf_typeserver         # not referenced from symbol
        0x1502: lf_enumerate
        0x1503: lf_array
        0x1504: lf_class
        0x1505: lf_structure
        0x1506: lf_union
        0x1507: lf_enum
        0x1508: lf_dimarray
        0x1509: lf_precomp            # not referenced from symbol
        0x150a: lf_alias              # alias (typedef) type
        0x150b: lf_defarg
        0x150c: lf_friendfcn
        0x150d: lf_member
        0x150e: lf_stmember
        0x150f: lf_method
        0x1510: lf_nesttype
        0x1511: lf_onemethod
        0x1512: lf_nesttypeex
        0x1513: lf_membermodify
        0x1514: lf_managed
        0x1515: lf_typeserver2

        0x1516: lf_strided_array      # same as lf_array, but with stride between adjacent elements
        0x1517: lf_hlsl
        0x1518: lf_modifier_ex
        0x1519: lf_interface
        0x151a: lf_binterface
        0x151b: lf_vector
        0x151c: lf_matrix

        0x151d: lf_vftable            # a virtual function table

        0x1601: lf_func_id            # global func ID
        0x1602: lf_mfunc_id           # member func ID
        0x1603: lf_buildinfo          # build info: tool, version, command line, src/pdb file
        0x1604: lf_substr_list        # similar to lf_arglist, for list of sub strings
        0x1605: lf_string_id          # string ID

        0x1606: lf_udt_src_line       # source and line on where an UDT is defined
        # only generated by compiler
        0x1607: lf_udt_mod_src_line   # module, source and line on where an UDT is defined
        # only generated by linker

        # 0x8000: lf_numeric
        0x8000: lf_char
        0x8001: lf_short
        0x8002: lf_ushort
        0x8003: lf_long
        0x8004: lf_ulong
        0x8005: lf_real32
        0x8006: lf_real64
        0x8007: lf_real80
        0x8008: lf_real128
        0x8009: lf_quadword
        0x800a: lf_uquadword
        0x800b: lf_real48
        0x800c: lf_complex32
        0x800d: lf_complex64
        0x800e: lf_complex80
        0x800f: lf_complex128
        0x8010: lf_varstring

        0x8017: lf_octword
        0x8018: lf_uoctword

        0x8019: lf_decimal
        0x801a: lf_date
        0x801b: lf_utf8string

        0x801c: lf_real16

        0xf0: lf_pad0
        0xf1: lf_pad1
        0xf2: lf_pad2
        0xf3: lf_pad3
        0xf4: lf_pad4
        0xf5: lf_pad5
        0xf6: lf_pad6
        0xf7: lf_pad7
        0xf8: lf_pad8
        0xf9: lf_pad9
        0xfa: lf_pad10
        0xfb: lf_pad11
        0xfc: lf_pad12
        0xfd: lf_pad13
        0xfe: lf_pad14
        0xff: lf_pad15
  lf_fieldlist_16t:
    seq:
      - id: items
        type: field_list_16t_item
        repeat: eos
  field_list_16t_item:
    seq:
      - id: type
        type: u2
        enum: leaf::leaf_type
      - id: element
        type:
          switch-on: type
          cases:
            'leaf::leaf_type::lf_enumerate_st': lf_enumerate_st_16t
            'leaf::leaf_type::lf_bclass_16t': lf_bclass_16_st
            'leaf::leaf_type::lf_nesttype_16t': lf_nesttype_16t
            'leaf::leaf_type::lf_method_16t': lf_method_16t
            'leaf::leaf_type::lf_onemethod_16t': lf_onemethod_16t
            'leaf::leaf_type::lf_member_16t': lf_member_16t
            'leaf::leaf_type::lf_vfunctab_16t': lf_vfunctab_16t
            'leaf::leaf_type::lf_stmember_16t': lf_stmember_16t
            'leaf::leaf_type::lf_vbclass_16t': lf_vbclass_16t
            'leaf::leaf_type::lf_ivbclass_16t': lf_vbclass_16t
            'leaf::leaf_type::lf_index_16t': lf_index_16t
      - id: trailing_padding
        size: (4 - (_io.pos % 4)) % 4
  lf_enumerate_st_16t:
    doc: lfEnumerate (cvinfo.h)
    seq:
      - id: attributes
        type: u2
      - id: value
        type: numeric
      - id: name
        type: pascal_string
  lf_bclass_16_st:
    doc: lfBClass_16t (cvinfo.h)
    seq:
      - id: index
        type: u2
      - id: attr
        type: u2
      - id: offset
        type: numeric
  lf_nesttype_16t:
    doc: lfNestType_16t
    seq:
      - id: index
        type: u2
      - id: name
        type: pascal_string
  lf_method_16t:
    doc: lfMethod_16t
    seq:
      - id: count
        type: u2
      - id: m_list
        type: u2
      - id: name
        type: pascal_string
  lf_onemethod_16t:
    doc: lfOneMethod_16t
    seq:
      - id: attr
        type: u2
      - id: index
        type: u2
      - id: vfptr_offset
        if: ((attr & 0x1c) >> 2) == 4 or ((attr & 0x1c) >> 2) == 6
        type: u4
      - id: name
        type: pascal_string
  lf_member_16t:
    doc: lfMember_16t
    seq:
      - id: index
        type: u2
      - id: attr
        type: u2
      - id: offset
        type: numeric
      - id: name
        type: pascal_string
  lf_vfunctab_16t:
    doc: lfVFuncTab_16t
    seq:
      - id: type
        type: u2
  lf_stmember_16t:
    doc: lfSTMember_16t
    seq:
      - id: index
        type: u2
        doc: index of type record for field
      - id: attr
        type: u2
        doc: attribute mask
      - id: name
        type: pascal_string
        doc: length prefixed name of field
  lf_vbclass_16t:
    doc: lfVBClass_16t (cvinfo.h)
    seq:
      - id: index
        type: u2
        doc: type index of direct virtual base class
      - id: vbptr
        type: u2
        doc: type index of virtual base pointer
      - id: attr
        type: u2
        doc: attribute
      - id: vbpoff
        type: numeric
        doc: virtual base pointer offset from address point
      - id: vbind
        type: numeric
        doc: virtual base offset from vbtable
  lf_index_16t:
    doc: lfIndex_16t (cvinfo)
    seq:
      - id: index
        type: u2

  lf_fieldlist:
    seq:
      - id: items
        type: field_list_item
        repeat: eos
  field_list_item:
    seq:
      - id: type
        type: u2
        enum: leaf::leaf_type
      - id: element
        type:
          switch-on: type
          cases:
            'leaf::leaf_type::lf_member': lf_member
            'leaf::leaf_type::lf_member_st': lf_member
            'leaf::leaf_type::lf_enumerate': lf_enumerate
            'leaf::leaf_type::lf_enumerate_st': lf_enumerate
            'leaf::leaf_type::lf_bclass': lf_bclass
            'leaf::leaf_type::lf_binterface': lf_bclass
            'leaf::leaf_type::lf_onemethod': lf_onemethod
            'leaf::leaf_type::lf_onemethod_st': lf_onemethod
            'leaf::leaf_type::lf_method': lf_method
            'leaf::leaf_type::lf_method_st': lf_method
            'leaf::leaf_type::lf_nesttype': lf_nesttype
            'leaf::leaf_type::lf_nesttype_st': lf_nesttype
            'leaf::leaf_type::lf_vfunctab': lf_vfunctab
            'leaf::leaf_type::lf_stmember': lf_stmember
            'leaf::leaf_type::lf_stmember_st': lf_stmember
            'leaf::leaf_type::lf_index': lf_index
#            'leaf::leaf_type::lf_vbclass': lf_vbclass
#            'leaf::leaf_type::lf_ivbclass': lf_vbclass
      - id: trailing_padding
        size: (4 - (_io.pos % 4)) % 4

  lf_enumerate:
    doc: lfEnumerate (cvinfo.h)
    seq:
      - id: attributes
        type: u2
      - id: value
        type: numeric
      - id: name
        type: strz_or_pascal(_parent.type == leaf::leaf_type::lf_enumerate)
  lf_member:
    doc: lfMember
    seq:
      - id: attr
        type: u2
      - id: index
        type: u4
      - id: offset
        type: numeric
      - id: name
        type: strz_or_pascal(_parent.type == leaf::leaf_type::lf_member)
  lf_bclass:
    doc: lfBClass (cvinfo.h)
    seq:
      - id: attr
        type: u2
      - id: index
        type: u4
      - id: offset
        type: numeric
  lf_onemethod:
    doc: lfOneMethod
    seq:
      - id: attr
        type: u2
      - id: index
        type: u4
      - id: vfptr_offset
        if: ((attr & 0x1c) >> 2) == 4 or ((attr & 0x1c) >> 2) == 6
        type: u4
      - id: name
        type: strz_or_pascal(_parent.type == leaf::leaf_type::lf_onemethod)
  lf_method:
    doc: lfMethod
    seq:
      - id: count
        type: u2
      - id: m_list
        type: u4
      - id: name
        type: strz_or_pascal(_parent.type == leaf::leaf_type::lf_method)
  lf_nesttype:
    doc: lfNestType
    seq:
      - id: pad0
        type: u2
      - id: index
        type: u4
      - id: name
        type: strz_or_pascal(_parent.type == leaf::leaf_type::lf_nesttype)
  lf_vfunctab:
    doc: lfVFuncTab
    seq:
      - id: pad0
        type: u2
      - id: type
        type: u4
  lf_stmember:
    doc: lfSTMember
    seq:
      - id: attr
        type: u2
        doc: attribute mask
      - id: index
        type: u4
        doc: index of type record for field
      - id: name
        type: strz_or_pascal(_parent.type == leaf::leaf_type::lf_stmember)
  lf_index:
    doc: lfIndex_16t (cvinfo)
    seq:
      - id: padding
        type: u2
      - id: index
        type: u4

  lf_enum_16t:
    doc: lfEnum_16t (cvinfo.h)
    seq:
      - id: count
        type: u2
        doc: count of number of elements in class
      - id: utype
        type: u2
        doc: underlying type of the enum
      - id: field
        type: u2
        doc: type index of LF_FIELD descriptor list
      - id: property
        type: u2
        doc: property attribute field
      - id: name
        type: pascal_string
        doc: length prefixed name of enum
  lf_enum:
    doc: lfEnum (cvinfo.h)
    seq:
      - id: count
        type: u2
        doc: count of number of elements in class
      - id: property
        type: u2
        doc: property attribute field
      - id: utype
        type: u4
        doc: underlying type of the enum
      - id: field
        type: u4
        doc: type index of LF_FIELD descriptor list
      - id: name
        type: strz_or_pascal(_parent.type == leaf::leaf_type::lf_enum)
        doc: length prefixed name of enum
  lf_class_16t:
    doc: lfClass_16t (cvinfo.h)
    seq:
      - id: count
        type: u2
      - id: field
        type: u2
      - id: property
        type: u2
      - id: derived
        type: u2
      - id: vshape
        type: u2
      - id: size
        type: numeric
      - id: name
        type: strz_or_pascal(_parent.type == leaf::leaf_type::lf_class or _parent.type == leaf::leaf_type::lf_structure)
#      - id: unique_name
#        if: (property & 0x20) != 0
#        type: strz_or_pascal(_parent.type == leaf::leaf_type::lf_class or _parent.type == leaf::leaf_type::lf_structure)
  lf_array_16t:
    doc: lfArray_16t (cvinfo.h)
    seq:
      - id: elemtype
        type: u2
      - id: idxtype
        type: u2
      - id: length
        type: numeric
      - id: name
        type: pascal_string
  lf_arglist_16t:
    doc: lfArgList_16t (cvinfo.h)
    seq:
      - id: count
        type: u2
      - id: arg
        type: u2
        repeat: expr
        repeat-expr: count
  lf_arglist:
    doc: lfArgList (cvinfo.h)
    seq:
      - id: count
        type: u4
      - id: arg
        type: u4
        repeat: expr
        repeat-expr: count
  lf_procedure_16t:
    doc: lfProc_16t (cvinfo.h)
    seq:
      - id: rvtype
        type: u2
      - id: calltype
        type: u1
      - id: funcattr
        type: u1
      - id: parmcount
        type: u2
      - id: arglist
        type: u2
  lf_procedure:
    doc: lfProc (cvinfo.h)
    seq:
      - id: rvtype
        type: u4
      - id: calltype
        type: u1
      - id: funcattr
        type: u1
      - id: parmcount
        type: u2
      - id: arglist
        type: u4
  lf_pointer_16t:
    doc: lfPointer_16t (cvinfo.h)
    seq:
      - id: attr
        type: u2
      - id: utype
        type: u2
        doc: type index of the underlying type
      - id: pm
        type: lf_pointer_16t_pm
        doc: attr.ptrmode in (CV_PTR_MODE_PMEM, CV_PTR_MODE_PMFUNC)
        if: ((attr & 0xe0) >> 5) == 2 or ((attr & 0xe0) >> 5) == 3
      # FIXME: variable length data...
  lf_pointer_16t_pm:
    doc: lfPointer_16t.pbase.pm
    seq:
      - id: pmclass
        type: u2
        doc: index of containing class for pointer to member
      - id: pmenum
        type: u2
        doc: enumeration specifying pm format (CV_pmtype_e)
  lf_modifier_16t:
    doc: lfModifier_16t (cvinfo.h)
    seq:
      - id: attr
        type: u2
      - id: type
        type: u2
  lf_modifier:
    doc: lfModifier_16t (cvinfo.h)
    seq:
      - id: type
        type: u4
      - id: attr
        type: u2
  lf_mfunction_16t:
    doc: lfMFunc_16t (cvinfo.h)
    seq:
      - id: rvtype
        type: u2
        doc: type index of return value
      - id: classtype
        type: u2
        doc: type index of containing class
      - id: thistype
        type: u2
        doc: type index of this pointer (model specific)
      - id: calltype
        type: u1
        doc: calling convention (call_t)
      - id: funcattr
        type: u1
        doc: attributes
      - id: parmcount
        type: u2
        doc: number of parameters
      - id: arglist
        type: u2
        doc: type index of argument list
      - id: thisadjust
        type: u4
        doc: this adjuster (long because pad required anyway)
  lf_mfunction:
    doc: lfMFunc_16t (cvinfo.h)
    seq:
      - id: rvtype
        type: u4
        doc: type index of return value
      - id: classtype
        type: u4
        doc: type index of containing class
      - id: thistype
        type: u4
        doc: type index of this pointer (model specific)
      - id: calltype
        type: u1
        doc: calling convention (call_t)
      - id: funcattr
        type: u1
        doc: attributes
      - id: parmcount
        type: u2
        doc: number of parameters
      - id: arglist
        type: u4
        doc: type index of argument list
      - id: thisadjust
        type: u4
        doc: this adjuster (long because pad required anyway)
  lf_methodlist_16t:
    doc: lfMethodList_16t (cvinfo.h)
    seq:
      - id: items
        type: lf_methodlist_16t_item
        repeat: eos
  lf_methodlist_16t_item:
    doc: mlMethod_16t (DumpTypRecC7 -> LF_METHODLIST_16t)
    seq:
      - id: attr
        type: u2
        doc: CV_fldattr_t (cvinfo.h)
      - id: index
        type: u2
      - id: vfptr_offset
        type: u4
        if: ((attr >> 2) & 0x7) == 4 or ((attr >> 2) & 0x7) == 6
        doc: attr.mprop == CV_MTintro || attr.mprop == CV_MTpureintro

  lf_methodlist:
    doc: lfMethodList (cvinfo.h)
    seq:
      - id: items
        type: lf_methodlist_item
        repeat: eos
  lf_methodlist_item:
    doc: mlMethod (DumpTypRecC7 -> LF_METHODLIST)
    seq:
      - id: attr
        type: u2
        doc: CV_fldattr_t (cvinfo.h)
      - id: pad0
        type: u2
        doc: internal padding, must be 0
      - id: index
        type: u4
      - id: vfptr_offset
        type: u4
        if: ((attr >> 2) & 0x7) == 4 or ((attr >> 2) & 0x7) == 6
        doc: attr.mprop == CV_MTintro || attr.mprop == CV_MTpureintro


  lf_array:
    doc: lfArray (cvinfo.h)
    seq:
      - id: elemtype
        type: u4
      - id: idxtype
        type: u4
      - id: length
        type: numeric
      - id: name
        type: strz_or_pascal(_parent.type == leaf::leaf_type::lf_array)
  lf_class:
    doc: lfClass (cvinfo.h)
    seq:
      - id: count
        type: u2
      - id: property
        type: u2
      - id: field
        type: u4
      - id: derived
        type: u4
      - id: vshape
        type: u4
      - id: size
        type: numeric
      - id: name
        type: strz_or_pascal(_parent.type == leaf::leaf_type::lf_class or _parent.type == leaf::leaf_type::lf_structure)
      - id: unique_name
        if: (property & 0x200) != 0
        type: strz_or_pascal(_parent.type == leaf::leaf_type::lf_class or _parent.type == leaf::leaf_type::lf_structure)
  lf_pointer:
    doc: lfPointer (cvinfo.h)
    seq:
      - id: utype
        type: u4
        doc: type index of the underlying type
      - id: attr
        type: u4
      - id: pm
        type: lf_pointer_pm
        doc: attr.ptrmode in (CV_PTR_MODE_PMEM, CV_PTR_MODE_PMFUNC)
        if: ((attr & 0xe0) >> 5) == 2 or ((attr & 0xe0) >> 5) == 3
      # FIXME: variable length data...
  lf_pointer_pm:
    doc: lfPointer.pbase.pm
    seq:
      - id: pmclass
        type: u4
        doc: index of containing class for pointer to member
      - id: pmenum
        type: u2
        doc: enumeration specifying pm format (CV_pmtype_e)
  lf_vtshape:
    doc: lfVTShape (cvinfo.h)
    seq:
      - id: count
        doc: number of entries in vfunctable
        type: u2
      - id: desc
        doc: 4 bit (CV_VTS_desc) descriptors
        type: u1
        repeat: expr
        repeat-expr: (count + 1) / 2

  lf_union_16t:
    doc: lfUnion_16t (cvinfo.h)
    seq:
      - id: count
        doc: count of number of elements in class
        type: u2
      - id: field
        doc: type index of LF_FIELD descriptor list
        type: u2
      - id: property
        doc: property attribute field
        type: u2
      - id: size
        type: numeric
      - id: name
        type: pascal_string
  lf_union:
    doc: lfUnion (cvinfo.h)
    seq:
      - id: count
        doc: count of number of elements in class
        type: u2
      - id: property
        doc: property attribute field
        type: u2
      - id: field
        doc: type index of LF_FIELD descriptor list
        type: u4
      - id: size
        type: numeric
      - id: name
        type: strz_or_pascal(_parent.type == leaf::leaf_type::lf_union)
      - id: unique_name
        type: strz_or_pascal(_parent.type == leaf::leaf_type::lf_union)
        if: (property & 0x200) != 0

  lf_bitfield_16t:
    doc: lfBitfield_16t (cvinfo.h)
    seq:
      - id: length
        type: u1
      - id: position
        type: u1
      - id: type
        type: u2
  lf_bitfield:
    doc: lfBitfield (cvinfo.h)
    seq:
      - id: type
        type: u4
      - id: length
        type: u1
      - id: position
        type: u1

  # IPI
  lf_udt_mod_src_line:
    doc: lfUdtModSrcLine (cvinfo.h)
    seq:
      - id: type
        type: u4
        doc: UDT's type index
      - id: src
        type: u4
        doc: index into string table where source file name is saved
      - id: line
        type: u4
        doc: line number
      - id: imod
        type: u2
        doc: module that contributes this UDT definition
  lf_string_id:
    doc: lfStringId (cvinfo.h)
    seq:
      - id: id
        type: u4
      - id: name
        type: strz
        encoding: ASCII
  lf_buildinfo:
    doc: lfBuildInfo (cvinfo.h)
    seq:
      - id: count
        type: u2
        doc: number of arugments
      - id: arg
        type: u4
        repeat: expr
        repeat-expr: count
  lf_func_id:
    doc: lfFuncId (cvinfo.h)
    seq:
      - id: scope_id
        type: u4
        doc: parent scope of the ID, 0 if global
      - id: type
        type: u4
        doc: function type
      - id: name
        type: strz
        encoding: ASCII
  lf_mfunc_id:
    doc: lfMFuncId (cvinfo.h)
    seq:
      - id: parent_type
        type: u4
        doc: type index of parent
      - id: type
        type: u4
        doc: function type
      - id: name
        type: strz
        encoding: ASCII
  lf_typeserver_st:
    seq:
      - id: signature
        type: u4
      - id: age
        type: u4
      - id: name
        type: pascal_string
  lf_typeserver2:
    doc: lfTypeServer2 (cvinfo.h)
    seq:
      - id: sig70
        doc: GUID
        size: 16
      - id: age
        type: u4
      - id: name
        type: strz
        encoding: ASCII

