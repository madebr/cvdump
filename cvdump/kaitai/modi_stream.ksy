meta:
  id: modi_stream
  imports:
    - cv_symbol
  endian: le
params:
  - id: symbols_size
    type: u4
  - id: c11_line_size
    type: u4
  - id: c13_line_size
    type: u4
seq:
  - id: signature
    type: u4
    if: symbols_size > 0
    valid:
      any-of: [65537, 1, 2, 4]
      # CV_SIGNATURE_C6   (0) # Actual signature is >64K
      # CV_SIGNATURE_C7   (1) # First explicit signature (MSVC 4.2)
      # CV_SIGNATURE_C11  (2) # C11 (vc5.x) 32-bit types (MSVC5, MSVC6)
      # CV_SIGNATURE_C13  (4) # C13 (vc7.x) zero terminated names (MSVC2026)
  - id: symbols
    if: symbols_size > 0
    type: symbol_entries
    size: symbols_size - 4
  - id: c11_line_info
    size: c11_line_size
  - id: c13_line_info
    size: c13_line_size
    type: c13_line_stream
  - id: global_refs_size
    if: symbols_size > 0 and signature != 65537
    doc: 'not sure about the symbols_size > 0 part, but required for a pure asm source, which provided 0 symbols (symbols_size == 0)'
    type: u4
  - id: global_refs
    if: symbols_size > 0 and signature != 65537
    doc: 'not sure about the symbols_size > 0 part, but required for a pure asm source, which provided 0 symbols (symbols_size == 0)'
    size: global_refs_size
types:
  symbol_entries:
    seq:
      - id: entries
        type: cv_symbol(_io.pos + 4, true)
        repeat: eos
