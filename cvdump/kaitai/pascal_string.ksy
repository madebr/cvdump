meta:
  id: pascal_string
  endian: le
seq:
  - id: len
    type: u1
  - id: text
    type: str
    encoding: ASCII
    size: len
