meta:
  id: cv_symbol_stream
  imports:
    - cv_symbol
  endian: le
params:
  - id: delta_pos
    type: u4
  - id: align4
    type: bool
seq:
  - id: entries
    type: cv_symbol(_io.pos + delta_pos, align4)
    repeat: eos
