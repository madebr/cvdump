meta:
  id: omf
  imports:
    - pascal_string
  endian: le
types:
  omf_source_module:
    doc: 'OMFSourceModule (cvexefmt.h)'
    seq:
      - id: c_file
        type: u2
      - id: c_seg
        type: u2
      - id: file_starts
        type: u4
        repeat: expr
        repeat-expr: c_file
      - id: segment_ranges
        type: range
        repeat: expr
        repeat-expr: c_seg
      - id: unks
        type: u2
        repeat: expr
        repeat-expr: c_seg
  omf_source_file:
    seq:
      - id: c_seg
        type: u2
      - id: c_file
        type: u2
      - id: start_lines
        type: u4
        repeat: expr
        repeat-expr: c_seg
      - id: ranges
        type: range
        repeat: expr
        repeat-expr: c_seg
      - id: name
        type: pascal_string
  omf_source_line:
    seq:
      - id: seg
        type: u2
      - id: count_lines
        type: u2
      - id: offsets
        type: u4
        repeat: expr
        repeat-expr: count_lines
      - id: lines
        type: u2
        repeat: expr
        repeat-expr: count_lines
  range:
    seq:
      - id: begin
        type: u4
      - id: end
        type: u4

