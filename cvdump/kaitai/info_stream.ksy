meta:
  id: info_stream
  endian: le
seq:
  - id: version
    type: u4
  - id: timestamp
    type: u4
  - id: contents_vc50
    type: contents_vc50
    if: version == 19960307
  - id: contents_vc98
    type: contents_vc98
    if: version == 19970604
  - id: contents_vc70
    type: contents_vc70
    if: version == 20000404

types:
  contents_vc50:
    seq:
      - id: age_or_unknown
        type: u4
        doc: ???
      - id: string_buffer_size
        type: u4
      - id: string_buffer
        size: string_buffer_size
      - id: amount_of_entries
        type: u4
      - id: unknown_array
        type: u4
        doc: ???
        repeat: expr
        repeat-expr: 4
      - id: entries
        type: name_entry
        repeat: expr
        repeat-expr: amount_of_entries
      - id: unused
        type: u4
  contents_vc98:
    seq:
      - id: age_or_unknown
        type: u4
        doc: ???
      - id: string_buffer_size
        type: u4
      - id: string_buffer
        size: string_buffer_size
      - id: amount_of_entries
        type: u4
      - id: unknown_array
        type: u4
        doc: ???
        repeat: expr
        repeat-expr: 2 * amount_of_entries
      - id: entries
        type: name_entry
        repeat: expr
        repeat-expr: amount_of_entries
      - id: unused
        type: u4
  contents_vc70:
    seq:
      - id: age
        type: u4
      - id: uuid
        size: 16
      - id: string_buffer_size
        type: u4
      - id: string_buffer
        size: string_buffer_size
      - id: amount_of_entries
        type: u4
      - id: capacity
        type: u4
      - id: present_bits
        type: bit_array
      - id: deleted_bits
        type: bit_array
      - id: entries
        type: name_entry
        repeat: expr
        repeat-expr: amount_of_entries
      - id: unused
        type: u4
      - id: features
        type: u4
        repeat: eos

  bit_array:
    seq:
      - id: word_count
        type: u4
      - id: words
        type: u4
        repeat: expr
        repeat-expr: word_count
  name_entry:
    seq:
      - id: key
        type: u4
      - id: value
        type: u4
