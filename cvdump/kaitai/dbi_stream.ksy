meta:
  id: dbi_stream
  endian: le
seq:
  - id: header
    type: debug_information_header
  - id: module_info
    type: 'module_infos(header.version_header)'
    size: header.module_info_size
  - id: section_contribution
    type: section_contribs(module_info.section_contrib_version)
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
      - id: magic_b0
        type: u1
      - id: magic_b1
        type: u1
      - id: magic_b2
        type: u1
      - id: magic_b3
        type: u1
      - id: new_header
        type: 'new_debug_information_header(magic_b0, magic_b1, magic_b2, magic_b3)'
        size: 60
        if: is_new_header
      - id: old_header
        type: 'old_debug_information_header(magic_b0, magic_b1, magic_b2, magic_b3)'
        if: not is_new_header
    instances:
      is_new_header:
        value: 'magic_b0 == 0xff and magic_b1 == 0xff and magic_b2 == 0xff and magic_b3 == 0xff'
      version_header:
        value: 'is_new_header ? new_header.version_header : 0'
      global_symbol_stream:
        value: 'is_new_header ? new_header.global_symbol_stream : (magic_b0 + magic_b1 * 256)'
      module_info_size:
        value: 'is_new_header ? new_header.module_info_size : old_header.module_info_size'
      section_contribution_size:
        value: 'is_new_header ? new_header.section_contribution_size : old_header.section_contribution_size'
      section_map_size:
        value: 'is_new_header ? new_header.section_map_size : old_header.section_map_size'
      source_info_size:
        value: 'is_new_header ? new_header.source_info_size : old_header.source_info_size'
      symbol_record_stream:
        value: 'is_new_header ? new_header.symbol_record_stream : old_header.symbol_record_stream'
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
        doc: verHdr
      - id: age
        type: u4
        doc: 'verHdr: no. of times this instance has been updated'
      - id: global_symbol_stream
        type: u2
        doc: snGSSyms
      - id: version_all
        type: u2
        doc: 'usVerAll / verold / vernew: union of 2 version formats'
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
        doc: 'iMFC: index of MFC type server'
      - id: size_debug_header
        type: u4
        doc: 'cbDbgHdr: size of optional DbgHdr info appended to the end of the stream'
      - id: ec_size
        type: u4
        doc: 'cbECInfo: number of bytes in EC substream, or 0 if EC no EC enabled Mods'
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


  section_contrib_v30:
    doc: unsure about version, format used by Visual Studio 2.0 (cl 9.0)
    seq:
      - id: section_index
        type: u2
      - id: padding
        type: u2  # (padding) Always 0xcbf for valid entries?
      - id: offset
        type: u4
      - id: size
        type: u4
      - id: module_index
        type: u2
      - id: unknown2
        type: u2

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

  section_contrib_v50:
    doc: |
      struct SC (dbicommon.h)
      (v50 might be wrong)
    seq:
      - id: sc40
        type: section_contrib_v40
      - id: data_crc
        type: u4
        doc: 'dwDataCrc'
      - id: reloc_crc
        type: u4
        doc: 'dwRelocCrc'
    instances:
      section_index:
        value: sc40.section_index
      padding:
        value: sc40.padding
      offset:
        value: sc40.offset
      size:
        value: sc40.size
      characteristics:
        value: sc40.characteristics
      module_index:
        value: sc40.module_index

  section_contribs:
    params:
      - id: section_contrib_version
        type: u4
    seq:
      - id: entries_v40
        type: section_contrib_v40
        if: is_v40
        repeat: eos
      - id: entries_v50_unk
        type: u4
        if: is_v50
      - id: entries_v50
        type: section_contrib_v50
        if: is_v50
        repeat: eos
    instances:
      is_v40:
        value: 'section_contrib_version == 4 ? true : false'
      is_v50:
        value: 'section_contrib_version == 5 ? true : false'
      entries:
        value: 'is_v50 ? entries_v50 : (is_v40 ? entries_v40 : entries_v40)'
  module_info_v50:
    doc: MODI50 (dbi.h)
    seq:
      - id: currently_open_mod
        type: u4
        doc: 'pmod: unused / currently open mod'
      - id: section_contrib
        type: section_contrib_v40
        doc: 'sc: this module''s first section contribution'
      - id: flags
        type: u2
        doc: |
          0x0001: fWritten (TRUE if mod has been written since DBI opened)
          0x00fe: unused
          0xff00: iTSM (index into TSM list for this mods server)
      - id: debug_info_stream
        type: u2
        doc: 'sn:  SN of module debug info (syms, lines, fpo), or snNil'
      - id: symbols_size
        type: u4
        doc: 'cbSyms: size of local symbols debug info in stream sn'
      - id: lines_size
        type: u4
        doc: 'cbLines: size of line number debug info in stream sn'
      - id: frame_pointer_opt_size
        type: u4
        doc: 'cbFpo: size of frame pointer opt debug info in stream sn'
      - id: source_file_count
        type: u2
        doc: 'ifileMac: number of files contributing to this module'
      - id: unused
        type: u2
        doc: 'padding'
      - id: source_filename_index
        type: u4
        doc: 'mpifileichFile: array [0..ifileMac) of offsets into dbi.bufFilenames'
      - id: module_name
        type: strz
        encoding: ASCII
        doc: 'rgch / szModule'
      - id: object_name
        type: strz
        encoding: ASCII
        doc: 'rgch / szObjFile'
      - id: struct_padding
        size: (4 - (_io.pos % 4)) % 4

  mod_info_v60_ecinfo:
    seq:
      - id: src_file_name_ni
        type: u4
      - id: path_compiler_pdb_ni
        type: u4

  module_info_v60:
    doc: MODI_60_Persist (dbi.h)
    seq:
      - id: currently_open_mod
        type: u4
        doc: 'pmod: pointer to currently open module (only usable on 32-bit systems)'
      - id: section_contrib
        type: section_contrib_v50
        doc: 'sc: this module''s first section contribution'
      - id: flags
        type: u2
        doc: |
          0x0001: fWritten (TRUE if mod has been written since DBI opened)
          0x0002: fWritten (TRUE if mod has EC symbolic information)
          0x00fc: unused
          0xff00: iTSM (index into TSM list for this mods server)
      - id: debug_info_stream
        type: u2
        doc: 'sn: SN of module debug info (syms, lines, fpo), or snNil'
      - id: symbols_size
        type: u4
        doc: 'cbSyms: size of local symbols debug info in stream sn'
      - id: lines_size
        type: u4
        doc: 'cbLines: size of line number debug info in stream sn'
      - id: c13_line_number_info_size
        type: u4
        doc: 'cbC13Lines: size of C13 style line number info in stream sn'
      - id: source_file_count
        type: u2
        doc: 'ifileMac: number of files contributing to this module'
      - id: unused
        type: u2
        doc: 'padding'
      - id: source_filename_index
        type: u4
        doc: 'mpifileichFile: array [0..ifileMac) of offsets into dbi.bufFilenames'
      - id: ec_info
        type: mod_info_v60_ecinfo
      - id: module_name
        type: strz
        encoding: ASCII
        doc: 'rgch / szModule'
      - id: object_name
        type: strz
        encoding: ASCII
        doc: 'rgch / szObjFile'
      - id: struct_padding
        size: (4 - (_io.pos % 4)) % 4

  module_infos:
    params:
      - id: dbi_header_version
        type: u4
    seq:
      - id: entries_v50
        type: module_info_v50
        if: is_v50
        repeat: eos
      - id: entries_v60
        type: module_info_v60
        if: is_v60
        repeat: eos
    instances:
      entries:
        value: 'is_v50 ? entries_v50 : entries_v60'
      is_v50:
        value: dbi_header_version < 19970606
      is_v60:
        value: dbi_header_version >= 19970606
      section_contrib_version:
        value: 'is_v60 ? 5 : (is_v50 ? 4 : -1)'

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
        type: u2
        doc: byte offset of the logical within the physical segment
      - id: padding
        type: u2
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

