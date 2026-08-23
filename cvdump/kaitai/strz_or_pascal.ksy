meta:
  id: strz_or_pascal
  imports:
    - pascal_string
  endian: le
params:
  - id: is_strz
    type: bool
seq:
  - id: text_strz
    if: is_strz
    type: strz
    encoding: ASCII
  - id: text_pascal
    if: not is_strz
    type: pascal_string
instances:
  text:
    value: 'is_strz ? text_strz : text_pascal.text'
