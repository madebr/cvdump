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
types:
  debug_information_header:
    doc: DBIHdr (dbi.h)
    seq:
      - id: global_symbol_stream
        type: u2
      - id: public_symbol_stream
        type: u2
      - id: symbol_record_stream
        type: u2
      - id: reserved1
        type: u2
        doc: padding, 0 for small PDB's, 0xff for big PDB's
      - id: module_info_size
        type: u4
      - id: section_contribution_size
        type: u4
#        valid:
#          expr: _ % 4 == 0
      - id: section_map_size
        type: u4
#        valid:
#          expr: _ % 4 == 0
      - id: source_info_size
        type: u4
#        valid:
#          expr: _ % 4 == 0

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

