meta:
  id: cv_symbol
  imports:
    - numeric
    - pascal_string
    - strz_or_pascal
    - c13_line_stream
  endian: le
params:
  - id: pos
    type: u4
seq:
  - id: record_size
    type: u2
  - id: record
    type: record
    size: record_size
  - id: name
    doc: 'There is a hidden name at the end of some records (tii.cpp -> stProcRefName)'
    if: 'record.type == symbol_type::s_procref_st or record.type == symbol_type::s_lprocref_st'
    type: pascal_string
  - id: trailing_padding
    size: (4 - ((_io.pos) % 4)) % 4
types:
  record:
    seq:
      - id: type
        type: u2
        enum: symbol_type
      - id: element
        type:
          switch-on: type
          cases:
            # CV_SIGNATURE_C13
            'symbol_type::s_objname': objname_sym(true)
            'symbol_type::s_compile2': compilesym2_sym(true)
            'symbol_type::s_compile3': compilesym3_sym
            'symbol_type::s_envblock': envblock_sym
            'symbol_type::s_export': export_sym
            'symbol_type::s_ldata32': data32_sym(true)
            'symbol_type::s_buildinfo': buildinfo_sym
            'symbol_type::s_lproc32': procsym32(true)
            'symbol_type::s_gproc32': procsym32(true)
            'symbol_type::s_local': local_sym
            'symbol_type::s_defrange_register': defrange_sym_register
            'symbol_type::s_defrange_register_rel': defrange_sym_register_rel
            'symbol_type::s_defrange': defrange_sym
            'symbol_type::s_defrange_framepointer_rel_full_scope': defrange_sym_framepointer_rel_full_scope
            'symbol_type::s_defrange_framepointer_rel': defrange_sym_frame_pointer_rel
            'symbol_type::s_defrange_subfield_register': defrange_sym_subfield_register
            'symbol_type::s_frameproc': frame_proc_sym
            'symbol_type::s_bprel32': bprel_sym32(true)
            'symbol_type::s_callees': function_list
            'symbol_type::s_callers': function_list
            'symbol_type::s_regrel32': reg_rel32
            'symbol_type::s_callsiteinfo': callsite_info
            'symbol_type::s_label32': label_sym32(true)
            'symbol_type::s_udt': udt_sym(true)
            'symbol_type::s_coboludt': udt_sym(true)
            'symbol_type::s_filestatic': file_static_sym
            'symbol_type::s_inlinesite': inline_site_sym
            'symbol_type::s_inlinesite_end': inline_site_end_sym
            'symbol_type::s_inlinees': inlinees_sym
            'symbol_type::s_heapallocsite': heap_alloc_site
            'symbol_type::s_constant': const_sym(true)
            'symbol_type::s_manconstant': const_sym(true)
            'symbol_type::s_unamespace': unamespace
            'symbol_type::s_end': end_arg_sym
            'symbol_type::s_thunk32': thunk_sym32(true)
            'symbol_type::s_register': reg_sym(true)
            'symbol_type::s_framecookie': framecookie
            'symbol_type::s_block32': block_sym32(true)
            'symbol_type::s_section': section_sym
            'symbol_type::s_coffgroup': coffgroup_sym

            # CV_SIGNATURE_C7
            'symbol_type::s_compile': cflags_sym
            'symbol_type::s_objname_st': objname_sym(false)
            'symbol_type::s_gproc32_16t': procsym32_16t
            'symbol_type::s_lproc32_16t': procsym32_16t
            'symbol_type::s_bprel32_16t': bprelsym32_16t
            'symbol_type::s_label32_st': label_sym32(false)
            'symbol_type::s_register_16t': regsym_16
            'symbol_type::s_ldata32_16t': datasym32_16t
            'symbol_type::s_thunk32_st': thunk_sym32(false)

            # CV_SIGNATURE_C11
            'symbol_type::s_udt_st': udt_sym(false)
            'symbol_type::s_gproc32_st': procsym32(false)
            'symbol_type::s_lproc32_st': procsym32(false)
            'symbol_type::s_bprel32_st': bprel_sym32(false)
            'symbol_type::s_register_st': reg_sym(false)
            'symbol_type::s_ldata32_st': data32_sym(false)
            'symbol_type::s_block32_st': block_sym32(false)
            'symbol_type::s_constant_st': const_sym(false)
            'symbol_type::s_compile2_st': compilesym2_sym(false)
            'symbol_type::s_udt_16t': udtsym_16t

            # symbol record stream
            'symbol_type::s_lprocref': refsym2
            'symbol_type::s_procref': refsym2
            'symbol_type::s_gdata32': data32_sym(true)
            'symbol_type::s_pub32': pubsym32(true)
            'symbol_type::s_pub32_st': pubsym32(false)
            'symbol_type::s_gdata32_st': data32_sym(false)
            'symbol_type::s_procref_st': refsym
            'symbol_type::s_lprocref_st': refsym
            'symbol_type::s_pub32_16t': datasym32_16t
            'symbol_type::s_constant_16t': constsym_16t
            'symbol_type::s_gdata32_16t': datasym32_16t
  udtsym_16t:
    doc: 'UDTSYM_16t'
    seq:
      - id: typind
        type: u2
      - id: name
        type: pascal_string
  datasym32_16t:
    doc: 'DATASYM32_16t (cvinfo.h)'
    seq:
      - id: 'off'
        type: u4
      - id: seg
        type: u2
      - id: typind
        type: u2
      - id: name
        type: pascal_string
  regsym_16:
    doc: 'REGSYM_16t (cvinfo.h)'
    seq:
      - id: typind
        type: u2
      - id: reg
        type: u2
      - id: name
        type: pascal_string
  bprelsym32_16t:
    doc: 'BPRELSYM32_16t (cvinfo.h)'
    seq:
      - id: 'off'
        type: u4
      - id: typind
        type: u2
      - id: name
        type: pascal_string
  procsym32_16t:
    doc: 'PROCSYM32_16t (cvinfo.h)'
    seq:
      - id: pointer_parent
        type: u4
      - id: pointer_end
        type: u4
      - id: pointer_next
        type: u4
      - id: len
        type: u4
      - id: debug_start
        type: u4
      - id: debug_end
        type: u4
      - id: 'off'
        type: u4
      - id: seg
        type: u2
      - id: typind
        type: u2
      - id: flags
        type: u1
      - id: name
        type: pascal_string
  coffgroup_sym:
    doc: 'COFFGROUPSYM (cvinfo.h)'
    seq:
      - id: cb
        type: u4
      - id: characteristics
        type: u4
      - id: 'off'
        type: u4
      - id: seg
        type: u2
      - id: name
        type: strz
        encoding: ASCII
  section_sym:
    doc: 'SECTIONSYM (cvinfo.h)'
    seq:
      - id: isec
        type: u2
      - id: align
        type: u1
      - id: reserved
        type: u1
      - id: rva
        type: u4
      - id: cb
        type: u4
      - id: characteristics
        type: u4
      - id: name
        type: strz
        encoding: ASCII
  block_sym32:
    doc: 'BLOCKSYM32 (cvinfo.h)'
    params:
      - id: is_strz
        type: bool
    seq:
      - id: pointer_parent
        type: u4
      - id: pointer_end
        type: u4
      - id: len
        type: u4
      - id: 'off'
        type: u4
      - id: seg
        type: u2
      - id: name
        type: strz_or_pascal(is_strz)
  framecookie:
    doc: 'FRAMECOOKIE (cvinfo.h) (NOTE: this element is parsed wrong by Microsoft''s cvdump.exe)'
    seq:
      - id: 'off'
        type: u4
      - id: reg
        type: u2
      - id: cookietype
        type: u1
      - id: flags
        type: u1
  reg_sym:
    doc: REGSYM (cvinfo.h)
    params:
      - id: is_strz
        type: bool
    seq:
      - id: typind
        type: u4
      - id: reg
        type: u2
      - id: name
        type: strz_or_pascal(is_strz)
  thunk_sym32:
    doc: THUNKSYM32 (cvinfo.h)
    params:
      - id: is_strz
        type: bool
    seq:
      - id: pointer_parent
        type: u4
      - id: pointer_end
        type: u4
      - id: pointer_next
        type: u4
      - id: 'off'
        type: u4
      - id: seg
        type: u2
      - id: len
        type: u2
      - id: ord
        type: u1
      - id: name
        type: strz_or_pascal(is_strz)
      - id: variant_adjustor_delta
        if: ord == 1
        type: u2
      - id: variant_adjustor_target
        if: ord == 1
        type: strz_or_pascal(is_strz)
      - id: variant_vcall_table_entry
        if: ord == 2
        type: u2
  unamespace:
    doc: UNAMESPACE (cvinfo.h)
    seq:
      - id: name
        type: strz
        encoding: ASCII
  const_sym:
    doc: CONSTSYM (cvinfo.h)
    params:
      - id: is_strz
        type: bool
    seq:
      - id: typind
        type: u4
      - id: value
        type: 'numeric'
      - id: name
        type: strz_or_pascal(is_strz)
  heap_alloc_site:
    doc: HEAPALLOCSITE (cvinfo.h)
    seq:
      - id: 'off'
        type: u4
      - id: sect
        type: u2
      - id: cb_instr
        type: u2
      - id: typind
        type: u2
  inlinees_sym:
    doc: Pure guess from LLVM
    seq:
      - id: count
        type: u4
      - id: items
        type: u4
        repeat: expr
        repeat-expr: count
  inline_site_end_sym:
    seq: []
  inline_site_sym:
    doc: INLINESITESYM (cvindo.h)
    seq:
      - id: pointer_parent
        type: u4
      - id: pointer_end
        type: u4
      - id: inlinee
        type: u4
      - id: binary_annotations
        type: u1
        repeat: eos
  file_static_sym:
    doc: FILESTATICSYM (cvinfo.h)
    seq:
      - id: typind
        type: u4
      - id: mod_offset
        type: u4
      - id: flags
        type: u2
      - id: name
        type: strz
        encoding: ASCII
  udt_sym:
    doc: UDTSYM (cvinfoh)
    params:
      - id: is_strz
        type: bool
    seq:
      - id: typind
        type: u4
      - id: name
        type: strz_or_pascal(is_strz)
  label_sym32:
    doc: LABELSYM32 (cvinfo.h)
    params:
      - id: is_strz
        type: bool
    seq:
      - id: 'off'
        type: u4
      - id: seg
        type: u2
      - id: flags
        type: u1
      - id: name
        type: strz_or_pascal(is_strz)
  callsite_info:
    doc: CALLSITEINFO (cvinfo.h)
    seq:
      - id: 'off'
        type: u4
      - id: sect
        type: u2
      - id: padding
        type: u2
      - id: typind
        type: u4
  reg_rel32:
    doc: REGREL32 (cvinfo.h)
    seq:
      - id: 'off'
        type: u4
      - id: typind
        type: u4
      - id: reg
        type: u2
      - id: name
        type: strz
        encoding: ASCII
  function_list:
    doc: FUNCTIONLIST (cvinfo.h)
    seq:
      - id: count
        type: u4
      - id: funcs
        type: u4
        repeat: expr
        repeat-expr: count
      - id: invocations
        type: u4
        repeat: eos
  end_arg_sym:
    doc: ENDARGSYM
    seq: []
  defrange_sym_register:
    doc: DEFRANGESYMREGISTER (cvinfo.h)
    seq:
      - id: reg
        type: u2
      - id: attr
        type: u2
      - id: range
        type: lvar_addr_range
      - id: gaps
        type: lvar_addr_gap
        repeat: eos
  defrange_sym_frame_pointer_rel:
    doc: DEFRANGESYMFRAMEPOINTERREL (cvinfo.h)
    seq:
      - id: off_frame_pointer
        type: u4
      - id: range
        type: lvar_addr_range
      - id: gaps
        type: lvar_addr_gap
        repeat: eos
  defrange_sym_subfield_register:
    doc: DEFRANGESYMSUBFIELDREGISTER (cvinfo.h)
    seq:
      - id: reg
        type: u2
      - id: attr
        type: u2
      - id: off_parent_padding
        type: u4
      - id: range
        type: lvar_addr_range
      - id: gaps
        type: lvar_addr_gap
        repeat: eos
  defrange_sym:
    doc: DEFRANGESYM (cvinfo.h)
    seq:
      - id: program
        type: u4
      - id: range
        type: lvar_addr_range
      - id: gaps
        type: lvar_addr_gap
        repeat: eos
  defrange_sym_register_rel:
    doc: DEFRANGESYMREGISTERREL (cvinfo.h)
    seq:
      - id: base_reg
        type: u2
      - id: flags
        type: u2
      - id: off_base_pointer
        type: u4
      - id: range
        type: lvar_addr_range
      - id: gaps
        type: lvar_addr_gap
        repeat: eos
  defrange_sym_framepointer_rel_full_scope:
    doc: DEFRANGESYMFRAMEPOINTERREL_FULL_SCOPE (cvinfo.h)
    seq:
      - id: off_frame_pointer
        type: u4

  lvar_addr_range:
    doc: CV_LVAR_ADDR_RANGE (cvinfo.h)
    seq:
      - id: off_start
        type: u4
      - id: isect_start
        type: u2
      - id: cb_range
        type: u2
  lvar_addr_gap:
    doc: CV_LVAR_ADDR_GAP (cvinfo.h)
    seq:
      - id: gap_start_offset
        type: u2
      - id: cb_range
        type: u2
  envblock_sym:
    seq:
      - id: flags
        type: u1
      - id: items
        type: envblock_item
        repeat: until
        repeat-until: _.key == ""
  envblock_item:
    doc: ENVBLOCKSYM (cvinfo.h)
    seq:
      - id: key
        type: strz
        encoding: ASCII
      - id: value
        if: key != ""
        type: strz
        encoding: ASCII
  export_sym:
    doc: EXPORTSYM (cvinfo.h)
    seq:
      - id: ordinal
        type: u2
      - id: flags
        type: u2
      - id: name
        type: strz
        encoding: ASCII
  data32_sym:
    doc: DATASYM32 (cvinfo.h)
    params:
      - id: is_strz
        type: bool
    seq:
      - id: type_index
        type: u4
      - id: offset
        type: u4
      - id: segment
        type: u2
      - id: name
        type: strz_or_pascal(is_strz)
  cflags_sym:
    doc: CFLAGSSYM (cvinfo.h)
    seq:
      - id: machine
        type: u1
      - id: language
        type: u1
      - id: flags
        type: u2
      - id: ver
        type: pascal_string
  compilesym2_sym:
    doc: COMPILESYM (cvinfo.h)
    params:
      - id: is_strz
        type: bool
    seq:
      - id: flags
        type: u4
      - id: machine
        type: u2
      - id: ver_fe_major
        type: u2
      - id: ver_fe_minor
        type: u2
      - id: ver_fe_build
        type: u2
      - id: ver_major
        type: u2
      - id: ver_minor
        type: u2
      - id: ver_build
        type: u2
      - id: ver_string
        type: strz_or_pascal(is_strz)
      - id: command_blocks
        type: envblock_item
        repeat: until
        repeat-until: _.key == ""
  compilesym3_sym:
    doc: COMPILESYM3 (cvinfo.h)
    seq:
      - id: flags
        type: u4
      - id: machine
        type: u2
      - id: ver_fe_major
        type: u2
      - id: ver_fe_minor
        type: u2
      - id: ver_fe_build
        type: u2
      - id: ver_fe_qfe
        type: u2
      - id: ver_major
        type: u2
      - id: ver_minor
        type: u2
      - id: ver_build
        type: u2
      - id: ver_qfe
        type: u2
      - id: ver_string
        type: strz
        encoding: ASCII
  buildinfo_sym:
    seq:
      - id: id
        type: u4
  objname_sym:
    doc: OBJNAMESYM (cvinfo.h)
    params:
      - id: is_strz
        type: bool
    seq:
      - id: signature
        type: u4
      - id: name
        type: strz_or_pascal(is_strz)

  procsym32:
    doc: PROCSYM32 (cvinfo.h)
    params:
      - id: is_strz
        type: bool
    seq:
      - id: pointer_parent
        type: u4
      - id: pointer_end
        type: u4
      - id: pointer_next
        type: u4
      - id: length
        type: u4
      - id: debug_start
        type: u4
      - id: debug_end
        type: u4
      - id: type_index
        type: u4
      - id: offset
        type: u4
      - id: segment
        type: u2
      - id: flags
        type: u1
      - id: name
        type: strz_or_pascal(is_strz)
  local_sym:
    doc: LOCALSYM (cvinfo.h)
    seq:
      - id: type_index
        type: u4
      - id: flags
        type: u2
      - id: name
        type: strz
        encoding: ASCII
  frame_proc_sym:
    doc: FRMEPROCSYM
    seq:
      - id: cb_frame
        type: u4
      - id: cb_pad
        type: u4
      - id: off_pad
        type: u4
      - id: cb_save_regs
        type: u4
      - id: off_ex_hdlr
        type: u4
      - id: sect_ex_hdlr
        type: u2
      - id: flags
        type: u4
  bprel_sym32:
    doc: BPRELSYM32 (cvinfo.h)
    params:
      - id: is_strz
        type: bool
    seq:
      - id: 'off'
        type: u4
      - id: typind
        type: u4
      - id: name
        type: strz_or_pascal(is_strz)
  refsym:
    doc: REFSYM (cvinfo.h)
    seq:
      - id: sum_name
        type: u4
      - id: ib_sym
        type: u4
      - id: imod
        type: u2
      - id: us_fill
        type: u2
  refsym2:
    doc: REFSYM2 (cvinfo.h)
    seq:
      - id: sum_name
        type: u4
      - id: ib_sym
        type: u4
      - id: imod
        type: u2
      - id: name
        type: strz
        encoding: ASCII
  pubsym32:
    doc: PUBSYM32 (cvinfo.h)
    params:
      - id: is_strz
        type: bool
    seq:
      - id: flags
        type: u4
      - id: 'off'
        type: u4
      - id: seg
        type: u2
      - id: name
        type: strz_or_pascal(is_strz)
  constsym_16t:
    doc: CONSTSYM_16t (cvinfo.h)
    seq:
      - id: typind
        type: u2
      - id: value
        type: numeric
      - id: name
        type: pascal_string
enums:
  symbol_type:
      0x0001: s_compile  # Compile flags symbol
      0x0002: s_register_16t  # Register variable
      0x0003: s_constant_16t  # constant symbol
      0x0004: s_udt_16t  # User defined type
      0x0005: s_ssearch  # Start Search
      0x0006: s_end  # Block procedure "with" or thunk end
      0x0007: s_skip  # Reserve symbol space in $$Symbols table
      0x0008: s_cvreserve  # Reserved symbol for CV internal use
      0x0009: s_objname_st  # path to object file name
      0x000a: s_endarg  # end of argument/return list
      0x000b: s_coboludt_16t  # special UDT for cobol that does not symbol pack
      0x000c: s_manyreg_16t  # multiple register variable
      0x000d: s_return  # return description symbol
      0x000e: s_entrythis  # description of this pointer on entry
      0x0100: s_bprel16  # BP-relative
      0x0101: s_ldata16  # Module-local symbol
      0x0102: s_gdata16  # Global data symbol
      0x0103: s_pub16  # a public symbol
      0x0104: s_lproc16  # Local procedure start
      0x0105: s_gproc16  # Global procedure start
      0x0106: s_thunk16  # Thunk Start
      0x0107: s_block16  # block start
      0x0108: s_with16  # with start
      0x0109: s_label16  # code label
      0x010a: s_cexmodel16  # change execution model
      0x010b: s_vftable16  # address of virtual function table
      0x010c: s_regrel16  # register relative address
      0x0200: s_bprel32_16t  # BP-relative
      0x0201: s_ldata32_16t  # Module-local symbol
      0x0202: s_gdata32_16t  # Global data symbol
      0x0203: s_pub32_16t  # a public symbol (CV internal reserved)
      0x0204: s_lproc32_16t  # Local procedure start
      0x0205: s_gproc32_16t  # Global procedure start
      0x0206: s_thunk32_st  # Thunk Start
      0x0207: s_block32_st  # block start
      0x0208: s_with32_st  # with start
      0x0209: s_label32_st  # code label
      0x020a: s_cexmodel32  # change execution model
      0x020b: s_vftable32_16t  # address of virtual function table
      0x020c: s_regrel32_16t  # register relative address
      0x020d: s_lthread32_16t  # local thread storage
      0x020e: s_gthread32_16t  # global thread storage
      0x020f: s_slink32  # static link for MIPS EH implementation
      0x0300: s_lprocmips_16t  # Local procedure start
      0x0301: s_gprocmips_16t  # Global procedure start
      # if these ref symbols have names following then the names are in ST format
      0x0400: s_procref_st  # Reference to a procedure
      0x0401: s_dataref_st  # Reference to data
      0x0402: s_align  # Used for page alignment of symbols
      0x0403: s_lprocref_st  # Local Reference to a procedure
      0x0404: s_oem  # OEM defined symbol
       # sym records with 32-bit types embedded instead of 16-bit
       # all have 0x1000 bit set for easy identification
       # only do the 32-bit target versions since we don't really
       # care about 16-bit ones anymore.
      0x1000: s_ti16_max
      0x1001: s_register_st  # Register variable
      0x1002: s_constant_st  # constant symbol
      0x1003: s_udt_st  # User defined type
      0x1004: s_coboludt_st  # special UDT for cobol that does not symbol pack
      0x1005: s_manyreg_st  # multiple register variable
      0x1006: s_bprel32_st  # BP-relative
      0x1007: s_ldata32_st  # Module-local symbol
      0x1008: s_gdata32_st  # Global data symbol
      0x1009: s_pub32_st  # a public symbol (CV internal reserved)
      0x100a: s_lproc32_st  # Local procedure start
      0x100b: s_gproc32_st  # Global procedure start
      0x100c: s_vftable32  # address of virtual function table
      0x100d: s_regrel32_st  # register relative address
      0x100e: s_lthread32_st  # local thread storage
      0x100f: s_gthread32_st  # global thread storage
      0x1010: s_lprocmips_st  # Local procedure start
      0x1011: s_gprocmips_st  # Global procedure start
      0x1012: s_frameproc  # extra frame and proc information
      0x1013: s_compile2_st  # extended compile flags and info
        # new symbols necessary for 16-bit enumerates of IA64 registers
        # and IA64 specific symbols
      0x1014: s_manyreg2_st  # multiple register variable
      0x1015: s_lprocia64_st  # Local procedure start (IA64)
      0x1016: s_gprocia64_st  # Global procedure start (IA64)
        # Local symbols for IL
      0x1017: s_localslot_st  # local IL sym with field for local slot index
      0x1018: s_paramslot_st  # local IL sym with field for parameter slot index
      0x1019: s_annotation  # Annotation string literals
        # symbols to support managed code debugging
      0x101a: s_gmanproc_st  # Global proc
      0x101b: s_lmanproc_st  # Local proc
      0x101c: s_reserved1  # reserved
      0x101d: s_reserved2  # reserved
      0x101e: s_reserved3  # reserved
      0x101f: s_reserved4  # reserved
      0x1020: s_lmandata_st
      0x1021: s_gmandata_st
      0x1022: s_manframerel_st
      0x1023: s_manregister_st
      0x1024: s_manslot_st
      0x1025: s_manmanyreg_st
      0x1026: s_manregrel_st
      0x1027: s_manmanyreg2_st
      0x1028: s_mantypref  # Index for type referenced by name from metadata
      0x1029: s_unamespace_st  # Using namespace
        # Symbols w/ SZ name fields. All name fields contain utf8 encoded strings.
      0x1100: s_st_max  # starting point for SZ name symbols
      0x1101: s_objname  # path to object file name
      0x1102: s_thunk32  # Thunk Start
      0x1103: s_block32  # block start
      0x1104: s_with32  # with start
      0x1105: s_label32  # code label
      0x1106: s_register  # Register variable
      0x1107: s_constant  # constant symbol
      0x1108: s_udt  # User defined type
      0x1109: s_coboludt  # special UDT for cobol that does not symbol pack
      0x110a: s_manyreg  # multiple register variable
      0x110b: s_bprel32  # BP-relative
      0x110c: s_ldata32  # Module-local symbol
      0x110d: s_gdata32  # Global data symbol
      0x110e: s_pub32  # a public symbol (CV internal reserved)
      0x110f: s_lproc32  # Local procedure start
      0x1110: s_gproc32  # Global procedure start
      0x1111: s_regrel32  # register relative address
      0x1112: s_lthread32  # local thread storage
      0x1113: s_gthread32  # global thread storage
      0x1114: s_lprocmips  # Local procedure start
      0x1115: s_gprocmips  # Global procedure start
      0x1116: s_compile2  # extended compile flags and info
      0x1117: s_manyreg2  # multiple register variable
      0x1118: s_lprocia64  # Local procedure start (IA64)
      0x1119: s_gprocia64  # Global procedure start (IA64)
      0x111a: s_localslot  # local IL sym with field for local slot index
      # 0x111a: s_slog  # alias for LOCALSLOT
      0x111b: s_paramslot  # local IL sym with field for parameter slot index
      # symbols to support managed code debugging
      0x111c: s_lmandata
      0x111d: s_gmandata
      0x111e: s_manframerel
      0x111f: s_manregister
      0x1120: s_manslot
      0x1121: s_manmanyreg
      0x1122: s_manregrel
      0x1123: s_manmanyreg2
      0x1124: s_unamespace  # Using namespace
      # ref symbols with name fields
      0x1125: s_procref  # Reference to a procedure
      0x1126: s_dataref  # Reference to data
      0x1127: s_lprocref  # Local Reference to a procedure
      0x1128: s_annotationref  # Reference to an s_annotation symbol
      0x1129: s_tokenref  # Reference to one of the many MANPROCSYM's
      # continuation of managed symbols
      0x112a: s_gmanproc  # Global proc
      0x112b: s_lmanproc  # Local proc
      # short light-weight thunks
      0x112c: s_trampoline  # trampoline thunks
      0x112d: s_manconstant  # constants with metadata type info
      # native attributed local/parms
      0x112e: s_attr_framerel  # relative to virtual frame ptr
      0x112f: s_attr_register  # stored in a register
      0x1130: s_attr_regrel  # relative to register (alternate frame ptr)
      0x1131: s_attr_manyreg  # stored in >1 register
      # Separated code (from the compiler) support
      0x1132: s_sepcode
      0x1133: s_local_2005  # defines a local symbol in optimized code
      0x1134: s_defrange_2005  # defines a single range of addresses in which symbol can be evaluated
      0x1135: s_defrange2_2005  # defines ranges of addresses in which symbol can be evaluated
      0x1136: s_section  # A COFF section in a PE executable
      0x1137: s_coffgroup  # A COFF group
      0x1138: s_export  # A export
      0x1139: s_callsiteinfo  # Indirect call site information
      0x113a: s_framecookie  # Security cookie information
      0x113b: s_discarded  # Discarded by LINK /OPT:REF (experimental see richards)
      0x113c: s_compile3  # Replacement for s_compile2
      0x113d: s_envblock  # Environment block split off from s_compile2
      0x113e: s_local  # defines a local symbol in optimized code
      0x113f: s_defrange  # defines a single range of addresses in which symbol can be evaluated
      0x1140: s_defrange_subfield           # ranges for a subfield
      0x1141: s_defrange_register           # ranges for en-registered symbol
      0x1142: s_defrange_framepointer_rel   # range for stack symbol.
      0x1143: s_defrange_subfield_register  # ranges for en-registered field of symbol
      0x1144: s_defrange_framepointer_rel_full_scope # range for stack symbol span valid full scope of function body gap might apply.
      0x1145: s_defrange_register_rel # range for symbol address as register + offset.
      0x1146: s_lproc32_id
      0x1147: s_gproc32_id
      0x1148: s_lprocmips_id
      0x1149: s_gprocmips_id
      0x114a: s_lprocia64_id
      0x114b: s_gprocia64_id
      0x114c: s_buildinfo # build information.
      0x114d: s_inlinesite # inlined function callsite.
      0x114e: s_inlinesite_end
      0x114f: s_proc_id_end
      0x1150: s_defrange_hlsl
      0x1151: s_gdata_hlsl
      0x1152: s_ldata_hlsl
      0x1153: s_filestatic
      0x1159: s_armswitchtable
      0x115a: s_callees
      0x115b: s_callers
      0x115c: s_pogodata
      0x115d: s_inlinesite2      # extended inline site information
      0x115e: s_heapallocsite    # heap allocation site
      0x115f: s_mod_typeref      # only generated at link time
      0x1160: s_ref_minipdb      # only generated at link time for mini PDB
      0x1161: s_pdbmap      # only generated at link time for mini PDB
      0x1162: s_gdata_hlsl32
      0x1163: s_ldata_hlsl32
      0x1164: s_gdata_hlsl32_ex
      0x1165: s_ldata_hlsl32_ex
      0x1168: s_inlinees # undocumented (see llvm)
      0x1170: s_bprel32_indir #(llvm)
      0x1171: s_regrel32_indir #(llvm)
      0x1172: s_gproc32ex #(llvm)
      0x1173: s_lproc32ex #(llvm)
      0x1174: s_gproc32ex_id #(llvm)
      0x1175: s_lproc32ex_id #(llvm)
      0x1176: s_staticlocal #(llvm)
      0x1178: s_bprel32_enctmp #(llvm)
      0x1179: s_regrel32_enctmp #(llvm)
      0x117a: s_bprel32_indir_enctmp #(llvm)
      0x117b: s_regrel32_indir_enctmp #(llvm)
      0x117c: s_association #(llvm)
      0x117e: s_sourcelink #(llvm)
      0x117f: s_defrange_constval_on_entry #(llvm)
      0x1180: s_defrange_globalsym_on_entry #(llvm)
      0x1181: s_altobjname #(llvm)
