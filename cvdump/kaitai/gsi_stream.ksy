meta:
  id: gsi_stream
  endian: le
types:
  new_header:
    seq:
      - id: version_signature
        type: u4
        valid: 0xffffffff
      - id: version
        type: u4
        valid: 0xeffe0000 + 19990810
      - id: hash_records_byte_size
        type: u4
      - id: bucket_information_byte_size
        type: u4
  pdb_hash_record_array:
    seq:
      - id: entries
        type: pdb_hash_record
        repeat: eos
  pdb_hash_record:
    seq:
      - id: offset_symbol_record_stream_plus_one
        type: u4
        doc: 'offset + 1'
      - id: reference_counter
        type: u4
        doc: '0 in MSVC4.2 PDBs, -1 in MSVC4.1 PDBs'
        if: offset_symbol_record_stream_plus_one != 0 and offset_symbol_record_stream_plus_one != 0xffffffff
