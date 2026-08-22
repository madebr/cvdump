meta:
  id: numeric
  endian: le
seq:
  - id: tag
    type: u2
  - id: char_
    type: s1
    if: tag == 0x8000 # leaf::leaf_type::lf_char
  - id: short_
    type: s2
    if: tag == 0x8001 # leaf::leaf_type::lf_short
  - id: ushort
    type: u2
    if: tag == 0x8002 # leaf::leaf_type::lf_ushort
  - id: long
    type: s4
    if: tag == 0x8003 # leaf::leaf_type::lf_long
  - id: ulong
    type: u4
    if: tag == 0x8004 # leaf::leaf_type::lf_ulong
  - id: real32
    type: f4
    if: tag == 0x8005 # leaf::leaf_type::lf_real32
  - id: real64
    type: f8
    if: tag == 0x8006 # leaf::leaf_type::lf_real64
  - id: real80
    size: 10
    if: tag == 0x8007 # leaf::leaf_type::lf_real80
  - id: real128
    size: 18
    if: tag == 0x8008 # leaf::leaf_type::lf_real128
  - id: quadword
    type: s8
    if: tag == 0x8009 # leaf::leaf_type::lf_quadword
  - id: uquadword
    type: u8
    if: tag == 0x800a # leaf::leaf_type::lf_uquadword
  - id: real48
    size: 6
    if: tag == 0x800b # leaf::leaf_type::lf_real48
  - id: complex32
    type: complex32
    if: tag == 0x800c # leaf::leaf_type::lf_complex32
  - id: complex64
    type: complex64
    if: tag == 0x800d # leaf::leaf_type::lf_complex64
  - id: complex80
    type: complex80
    if: tag == 0x800e # leaf::leaf_type::lf_complex80
  - id: complex128
    type: complex128
    if: tag == 0x800f # leaf::leaf_type::lf_complex128
  - id: varstring
    type: varstring
    if: tag == 0x8010 # leaf::leaf_type::lf_varstring
  - id: octword
    if: tag == 0x8017 # leaf::leaf_type::lf_octword
    size: 16
  - id: uoctword
    if: tag == 0x8018 # leaf::leaf_type::lf_uoctword
    size: 16
  - id: decimal
    if: tag == 0x8019 # leaf::leaf_type::lf_decimal
    type: decimal
  - id: date
    if: tag == 0x801a # leaf::leaf_type::lf_date
    type: f8
  - id: utf8string
    if: tag == 0x801b # leaf::leaf_type::lf_utf8string
    encoding: UTF-8
    type: strz
  - id: real16
    if: tag == 0x801c # leaf::leaf_type::lf_real16
    size: 2
types:
  complex32:
    seq:
      - id: real
        type: f4
      - id: complex
        type: f4
  complex64:
    seq:
      - id: real
        type: f8
      - id: complex
        type: f8
  complex80:
    seq:
      - id: real
        size: 10
      - id: complex
        size: 10
  complex128:
    seq:
      - id: real
        size: 16
      - id: complex
        size: 16
  decimal:
    seq:
      - id: w_reserved
        type: u2
      - id: scale
        type: u1
      - id: sign
        type: u1
      - id: hi32
        type: u4
      - id: lo64
        type: u8
  varstring:
    seq:
      - id: len
        type: u2
      - id: text
        size: len
