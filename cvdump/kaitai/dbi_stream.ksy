meta:
  id: dbi_stream
  endian: le
seq:
  - id: header
    type: debug_information_header
  - id: module_info
    type: module_infos_v50
    size: header.module_info_size
  - id: section_contribution
    type: section_contribs_v40
    size: header.section_contribution_size
  - id: section_map
    type: omf_seg_map
    size: header.section_map_size
  - id: source_info
    type: dbi_source_info
    size: header.source_info_size
  - id: type_server_map
    if: header.is_new_header
    size: header.new_header.type_server_map_size
  - id: ec_info
    if: header.is_new_header
    size: header.new_header.ec_size
  - id: dbg_hdr
    if: header.is_new_header
    size: header.new_header.size_debug_header
types:
  debug_information_header:
    doc: OldDBIHdr / DBIHdr (dbi.h)
    seq:
      - id: magic0
        type: u1
      - id: magic1
        type: u1
      - id: magic2
        type: u1
      - id: magic3
        type: u1
      - id: new_header
        type: 'new_debug_information_header(magic0, magic1, magic2, magic3)'
        size: 60
        if: is_new_header
      - id: old_header
        type: 'old_debug_information_header(magic0, magic1, magic2, magic3)'
        if: not is_new_header
    instances:
      is_new_header:
        value: 'magic0 == 0xff and magic1 == 0xff and magic2 == 0xff and magic3 == 0xff'
      version_header:
        value: 'is_new_header ? new_header.version_header : 0'
      global_symbol_stream:
        value: 'is_new_header ? new_header.global_symbol_stream : (magic0 + magic1 * 256)'
      module_info_size:
        value: 'is_new_header ? new_header.module_info_size : old_header.module_info_size'
      section_contribution_size:
        value: 'is_new_header ? new_header.section_contribution_size : old_header.section_contribution_size'
      section_map_size:
        value: 'is_new_header ? new_header.section_map_size : old_header.section_map_size'
      source_info_size:
        value: 'is_new_header ? new_header.source_info_size : old_header.source_info_size'
  old_debug_information_header:
    doc: OldDBIHdr (dbi.h)
    params:
      - id: magic0
        type: u1
      - id: magic1
        type: u1
      - id: magic2
        type: u1
      - id: magic3
        type: u1
    seq:
      - id: symbol_record_stream
        type: u2
        doc: 'snSymRecs'
      - id: reserved1
        type: u2
        valid:
          eq: 0
      - id: module_info_size
        type: u4
        doc: 'cbGpModi'
      - id: section_contribution_size
        type: u4
        doc: 'cbSC'
      - id: section_map_size
        type: u4
        doc: 'cbSecMap'
      - id: source_info_size
        type: u4
        doc: 'cbFileInfo'
    instances:
      global_symbol_stream:
        value: magic0 + 256 * magic1
        doc: 'snGSSyms'
      public_symbol_stream:
        value: magic2 + 256 * magic3
        doc: 'snPSSyms'
  new_debug_information_header:
    doc: DBIHdr (dbi.h)
    params:
      - id: magic0
        type: u1
      - id: magic1
        type: u1
      - id: magic2
        type: u1
      - id: magic3
        type: u1
    seq:
      - id: version_header
        type: u4
      - id: age
        type: u4
        doc: no. of times this instance has been updated
      - id: global_symbol_stream
        type: u2
        doc: snGSSyms
      - id: version_all
        type: u2
        doc: union of 2 version formats
      - id: public_symbol_stream
        type: u2
        doc: snPSSyms
      - id: version_pdb_dll_build
        type: u2
        doc: 'usVerPdbDllBuild: build version of the pdb dll that built this pdb last.'
      - id: symbol_record_stream
        type: u2
        doc: snSymRecs
      - id: version_pdb_dll_rbuild
        type: u2
        doc: 'usVerPdbDllRBld: build version of the pdb dll that built this pdb last.'
      - id: module_info_size
        type: u4
        doc: 'cbGpModi: size of rgmodi substream'
      - id: section_contribution_size
        type: u4
        doc: 'cbSC: size of Section Contribution substream'
      - id: section_map_size
        type: u4
        doc: 'cbSecMap'
      - id: source_info_size
        type: u4
        doc: 'ctFileInfo'
      - id: type_server_map_size
        type: u4
        doc: 'cbTSMap: size of the Type Server Map substream'
      - id: mfc_type_server_stream
        type: u4
        doc: index of MFC type server
      - id: size_debug_header
        type: u4
        doc: size of optional DbgHdr info appended to the end of the stream
      - id: ec_size
        type: u4
        doc: number of bytes in EC substream, or 0 if EC no EC enabled Mods
      - id: flags
        type: u2
        doc: |
          0x1 -> fIncLink  - true if linked incrmentally (really just if ilink thunks are present)
          0x2 -> fStripped - true if PDB::CopyTo stripped the private data out
          0x4 -> fCTypes   - true if this PDB is using CTypes
      - id: machine
        type: u2
        doc: machine type
    instances:
      version_signature:
        value: magic0 + 256 * (magic1 + 256 * (magic2 + 256 * magic3))


  section_contrib_v40:
    doc: struct SC40 (dbicommon.h)
    seq:
      - id: section_index
        type: u2
      - id: padding
        type: u2  # (padding) Always 0xcbf for valid entries?
      - id: offset
        type: u4
      - id: size
        type: u4
      - id: characteristics
        type: u4
      - id: module_index
        type: u2
      - id: unknown2
        type: u2

  section_contribs_v40:
    seq:
      - id: entries
        type: section_contrib_v40
        repeat: eos


  module_info_v50:
    doc: MODI50 (dbi.h)
    seq:
      - id: currently_open_mod
        type: u4
        doc: unused
      - id: section_contrib
        type: section_contrib_v40
      - id: flags
        type: u2
      - id: debug_info_stream
        type: u2
      - id: symbols_size
        type: u4
      - id: lines_size
        type: u4
      - id: frame_pointer_opt_size
        type: u4
      - id: source_file_count
        type: u2
      - id: unused
        type: u2
      - id: source_filename_index
        type: u4
      - id: module_name
        type: strz
        encoding: ASCII
      - id: object_name
        type: strz
        encoding: ASCII
      - id: struct_padding
        size: (4 - (_io.pos % 4)) % 4

  module_infos_v50:
    seq:
      - id: entries
        type: module_info_v50
        repeat: eos

  omf_seg_map:
    doc: OMFSegMap (cvexefmt.h)
    seq:
      - id: c_seg
        type: u2
      - id: c_seg_log
        type: u2
      - id: rg_desc
        type: omf_seg_map_desc
        repeat: expr
        repeat-expr: c_seg

  omf_seg_map_desc:
    doc: OMFSegMapDesc (pdbimpl.h)
    seq:
      - id: f_all
        type: u2
        doc: descriptor flags bit field
      - id: ovl
        type: u2
        doc: the logical overlay number
      - id: group
        type: u2
        doc: group index into the descriptor array
      - id: frame
        type: u2
        doc: logical segment index - interpreted via flags
      - id: i_seg_name
        type: u2
        doc: segment or group name - index into sstSegName
      - id: i_class_name
        type: u2
        doc: class name - index into sstSegName
      - id: offset
        type: u4
        doc: byte offset of the logical within the physical segment
      - id: cb_seg
        type: u4
        doc: byte count of the logical segment or group

  dbi_source_info:
    doc: DBI1::reloadFileInfo (dbi.cpp)
    seq:
      - id: count_modules
        type: u2
      - id: count_source_files
        type: u2
      - id: module_indices
        type: u2
        repeat: expr
        repeat-expr: count_modules
      - id: module_file_counts
        type: u2
        repeat: expr
        repeat-expr: count_modules
      - id: file_name_offsets
        doc: This value should be dynamically recalculated as sum(module_file_counts)
        type: u4
        repeat: expr
        repeat-expr: count_source_files
      - id: buffer
        size-eos: true

