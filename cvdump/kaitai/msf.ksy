meta:
  id: msf
  endian: le
doc: |
  'Microsoft C/C++ program database 1.00\r\n\x1aJG\x00'
  [0x4d, 0x69, 0x63, 0x72, 0x6f, 0x73, 0x6f, 0x66, 0x74, 0x20, 0x43, 0x2f, 0x43, 0x2b, 0x2b, 0x20, 0x70, 0x72, 0x6f, 0x67, 0x72, 0x61, 0x6d, 0x20, 0x64, 0x61, 0x74, 0x61, 0x62, 0x61, 0x73, 0x65, 0x20, 0x31, 0x2e, 0x30, 0x30, 0x0d, 0x0a, 0x1a, 0x4a, 0x47, 0x00, 0x00]
  
  'Microsoft C/C++ program database 2.00\r\n\x1aJG\x00'
  [0x4d, 0x69, 0x63, 0x72, 0x6f, 0x73, 0x6f, 0x66, 0x74, 0x20, 0x43, 0x2f, 0x43, 0x2b, 0x2b, 0x20, 0x70, 0x72, 0x6f, 0x67, 0x72, 0x61, 0x6d, 0x20, 0x64, 0x61, 0x74, 0x61, 0x62, 0x61, 0x73, 0x65, 0x20, 0x32, 0x2e, 0x30, 0x30, 0x0d, 0x0a, 0x1a, 0x4a, 0x47, 0x00, 0x00]
  
  'Microsoft C/C++ MSF 7.00\r\n\x1aDS\x00\x00\x00'
  [0x4d, 0x69, 0x63, 0x72, 0x6f, 0x73, 0x6f, 0x66, 0x74, 0x20, 0x43, 0x2f, 0x43, 0x2b, 0x2b, 0x20, 0x4d, 0x53, 0x46, 0x20, 0x37, 0x2e, 0x30, 0x30, 0x0d, 0x0a, 0x1a, 0x44, 0x53, 0x00, 0x00, 0x00]
seq:
  - id: magic
    type: magic
  - id: small_superblock
    type: small_superblock_v2_contents
    if: magic.is_small_msf and magic.small_msf_version == 2
  - id: big_superblock
    type: big_superblock_contents
    if: magic.is_big_msf
instances:
  is_small_msf:
    value: magic.is_small_msf
  small_msf_version:
    value: magic.small_msf_version
  is_big_msf:
    value: magic.is_big_msf
types:
  magic:
    seq:
      - id: magic0
        contents: [0x4d, 0x69, 0x63, 0x72, 0x6f, 0x73, 0x6f, 0x66, 0x74, 0x20, 0x43, 0x2f, 0x43, 0x2b, 0x2b, 0x20]
      - id: magic1
        type: u1
        valid:
          any-of: [0x4d, 0x70]
      - id: magic2_small
        if: is_small_msf
        contents: [0x72, 0x6f, 0x67, 0x72, 0x61, 0x6d, 0x20, 0x64, 0x61, 0x74, 0x61, 0x62, 0x61, 0x73, 0x65, 0x20]
      - id: magic3_small
        type: u1
        doc: 'can be "1" or "2"'
        if: is_small_msf
        valid:
          any-of: [0x31, 0x32]
      - id: magic4_small
        if: is_small_msf
        contents: [0x2e, 0x30, 0x30, 0x0d, 0x0a, 0x1a, 0x4a, 0x47, 0x00, 0x00]
      - id: magic2_big
        if: is_big_msf
        contents: [0x53, 0x46, 0x20, 0x37, 0x2e, 0x30, 0x30, 0x0d, 0x0a, 0x1a, 0x44, 0x53, 0x00, 0x00, 0x00]
    instances:
      is_small_msf:
        value: magic1 == 0x70
      is_big_msf:
        value: magic1 == 0x4d
      small_msf_version:
        value: 'is_small_msf ? (magic3_small - 0x30) : -1'
  small_superblock_v2_contents:
    seq:
      - id: block_size
        type: u4
      - id: free_block_map_block
        type: u2
      - id: num_blocks
        type: u2
      - id: num_directory_bytes
        type: u4
      - id: unknown
        type: u4
      - id: block_map
        type: u2
        repeat: expr
        repeat-expr: (num_directory_bytes + block_size - 1) / block_size
  small_msf_stream_directory:
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
  big_superblock_contents:
    seq:
      - id: block_size
        type: u4
        doc: |
          The block size of the internal file system. Valid values are 512, 1024, 2048, and 4096 bytes.
        valid:
          any-of: [512, 1024, 2048, 4096]
      - id: free_block_map_block
        type: u4
        doc: |
          The index of a block within the file, at which begins a bitfield representing the set of all blocks
          within the file which are “free” (i.e. the data within that block is not used).
          See The Free Block Map for more information. Important: FreeBlockMapBlock can only be 1 or 2!
        valid:
          any-of: [1, 2]
      - id: num_blocks
        type: u4
        doc: |
          The total number of blocks in the file. NumBlocks * BlockSize should equal the size of the file on disk.
      - id: num_directory_bytes
        type: u4
        doc: |
          The size of the stream directory, in bytes.
          The stream directory contains information about each stream’s size and the set of blocks that it occupies.
      - id: unknown
        type: u4
      - id: block_map_address
        type: u4
        doc: |
          The index of a block within the MSF file.
          At this block is an array of u4’s listing the blocks that the stream directory resides on.
          For large MSF files, the stream directory (which describes the block layout of each stream)
          may not fit entirely on a single block. As a result, this extra layer of indirection is introduced,
          whereby this block contains the list of blocks that the stream directory occupies,
          and the stream directory itself can be stitched together accordingly.
          The number of u4’s in this array is given by ceil(NumDirectoryBytes / BlockSize).
  big_msf_stream_directory_pages:
    params:
      - id: count_items
        type: u4
    seq:
      - id: pages
        type: u4
        repeat: expr
        repeat-expr: count_items

  big_msf_stream_directory:
    seq:
      - id: num_streams
        type: u4
      - id: stream_sizes
        type: u4
        repeat: expr
        repeat-expr: num_streams
      - id: stream_blocks
        type: u4
        repeat: eos

