meta:
  id: msf_small_directory
  endian: le
seq:
- id: num_streams
  type: u2
- id: reserved
  type: u2
- id: stream_sizes
  type: stream_directory_size
  repeat: expr
  repeat-expr: num_streams
- id: stream_blocks
  type: u2
  repeat: eos
types:
  stream_directory_size:
    seq:
      - id: size
        type: u4
      - id: reserved_ptr
        type: u4
