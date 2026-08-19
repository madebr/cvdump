meta:
  id: names_stream
  endian: le
seq:
  - id: signature
    type: u4
    valid: 0xeffeeffe
  - id: hash_version
    type: u4
    valid:
      any-of: [1, 2]
  - id: string_buffer_size
    type: u4
  - id: string_buffer
    size: string_buffer_size
  - id: bucket_count
    type: u4
  - id: buckets
    type: u4
    repeat: expr
    repeat-expr: bucket_count
  - id: amount_of_strings
    type: u4
