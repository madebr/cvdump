meta:
  id: msf_small_superblock
  endian: le
seq:
- id: magic
  contents: "Microsoft C/C++ program database 2.00\r\n\x1aJG\x00\x00"  # 0x2c bytes
- id: block_size
  type: u4
- id: free_block_map_block
  type: u2  # Can only be 1 or 2 ?
- id: num_blocks
  type: u2  #
- id: num_directory_bytes
  type: u4
- id: unknown
  type: u4
- id: block_map
  type: u2
  repeat: expr
  repeat-expr: (num_directory_bytes + block_size - 1) / block_size
