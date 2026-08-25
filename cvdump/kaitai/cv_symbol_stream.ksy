meta:
  id: cv_symbol_stream
  imports:
    - cv_symbol
  endian: le
params:
  - id: delta_pos
    type: u4
seq:
  - id: entries
    type: cv_symbol(_io.pos + delta_pos)
    repeat: eos
