meta:
  id: c13_line_stream
  endian: le
seq:
  - id: subsections
    type: subsection
    repeat: eos
types:
  subsection:
    seq:
      - id: header
        type: subsection_header
      - id: contents
        size: header.size
        type:
          switch-on: header.type
          cases:
            'debug_s_subsection_type::debug_s_filechksms': debug_filechecksums
            'debug_s_subsection_type::debug_s_lines': debug_lines(header.size)
  subsection_header:
    seq:
      - id: type
        type: u4
        enum: debug_s_subsection_type
      - id: size
        type: u4
  debug_filechecksums:
    seq:
      - id: checksums
        type: filechecksum(_io.pos)
        repeat: eos
  filechecksum:
    params:
      - id: pos
        type: u4
    seq:
      - id: name_index
        type: u4
      - id: hash_size
        type: u1
      - id: hash_type
        type: u1
      - id: hash
        size: hash_size
      - id: padding
        size: (4 - ((_io.pos) % 4)) % 4
  debug_lines:
    params:
      - id: size
        type: u4
    seq:
      - id: off_con
        type: u4
      - id: seg_con
        type: u2
      - id: flags
        type: u2
      - id: count_con
        type: u4
      - id: tables
        type: debug_line_tables
        size: size - 12
  debug_line_tables:
    seq:
      - id: items
        type: debug_lines_table_item
        repeat: eos
  debug_lines_table_item:
    seq:
      - id: fileid
        type: u4
      - id: count_lines
        type: u4
      - id: file_block_size
        type: u4
      - id: lines
        type: cv_line_t
        repeat: expr
        repeat-expr: count_lines
        #size: file_block_size - 12
  cv_line_t:
    doc: 'CV_Line_t (cvinfo.h)'
    seq:
      - id: offset
        type: u4
      - id: linenum_delta_statement
        doc: 'linenumStart: 0x00ffffff, deltaLineNum: 0x7f000000, statement: 0x80000000'
        type: u4
    instances:
      line_number_start:
        value: 'linenum_delta_statement & 0xffffff'
      delta_line_number:
        value: '(linenum_delta_statement >> 24) & 0x7f'
      is_statement:
        value: 'linenum_delta_statement >> 31'

enums:
  debug_s_subsection_type:
    0xf1: debug_s_symbols
    0xf2: debug_s_lines
    0xf3: debug_s_stringtable
    0xf4: debug_s_filechksms
    0xf5: debug_s_framedata
    0xf6: debug_s_inlineelines
    0xf7: debug_s_crossscopeimports
    0xf8: debug_s_crossscopeexports
    0xf9: debug_s_il_lines
    0xfa: debug_s_func_mdtoken_map
    0xfb: debug_s_type_mdtoken_map
    0xfc: debug_s_merged_assemblyinput
    0xfd: debug_s_coff_symbol_rva
