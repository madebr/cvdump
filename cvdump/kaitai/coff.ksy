meta:
  id: coff
  imports:
    - c13_line_stream
  endian: le
seq:
  - id: header
    type: header
  - id: section_headers
    type: section_header
    repeat: expr
    repeat-expr: header.number_of_sections
types:
  header:
    seq:
      - id: machine
        type: u2
        enum: machine
        doc: 'The number that identifies the type of target machine'
      - id: number_of_sections
        type: u2
        doc: 'The number of sections. This indicates the size of the section table, which immediately follows the headers.'
      - id: time_date_stamp
        type: u4
        doc: 'The low 32 bits of the number of seconds since 00:00 January 1, 1970 (a C run-time time_t value), which indicates when the file was created.'
      - id: pointer_to_symbol_table
        type: u4
        doc: 'The file offset of the COFF symbol table, or zero if no COFF symbol table is present. This value should be zero for an image because COFF debugging information is deprecated.'
      - id: number_of_symbols
        type: u4
        doc: 'The number of entries in the symbol table. This data can be used to locate the string table, which immediately follows the symbol table. This value should be zero for an image because COFF debugging information is deprecated.'
      - id: size_of_optional_header
        type: u2
        doc: 'The size of the optional header, which is required for executable files but not for object files. This value should be zero for an object file.'
      - id: characteristics
        type: u2
        doc: 'The flags that indicate the attributes of the file.'
  section_header:
    seq:
      - id: name
        size: 8
        doc: 'An 8-byte, null-padded UTF-8 encoded string. If the string is exactly 8 characters long, there is no terminating null. For longer names, this field contains a slash (/) that is followed by an ASCII representation of a decimal number that is an offset into the string table. Executable images do not use a string table and do not support section names longer than 8 characters. Long names in object files are truncated if they are emitted to an executable file.'
      - id: virtual_size
        type: u4
        doc: 'The total size of the section when loaded into memory. If this value is greater than SizeOfRawData, the section is zero-padded. This field is valid only for executable images and should be set to zero for object files.'
      - id: virtual_address
        type: u4
        doc: 'For executable images, the address of the first byte of the section relative to the image base when the section is loaded into memory. For object files, this field is the address of the first byte before relocation is applied; for simplicity, compilers should set this to zero. Otherwise, it is an arbitrary value that is subtracted from offsets during relocation.'
      - id: size_of_raw_data
        type: u4
        doc: 'The size of the section (for object files) or the size of the initialized data on disk (for image files). For executable images, this must be a multiple of FileAlignment from the optional header. If this is less than VirtualSize, the remainder of the section is zero-filled. Because the SizeOfRawData field is rounded but the VirtualSize field is not, it is possible for SizeOfRawData to be greater than VirtualSize as well. When a section contains only uninitialized data, this field should be zero.'
      - id: pointer_to_raw_data
        type: u4
        doc: 'The file pointer to the first page of the section within the COFF file. For executable images, this must be a multiple of FileAlignment from the optional header. For object files, the value should be aligned on a 4-byte boundary for best performance. When a section contains only uninitialized data, this field should be zero.'
      - id: pointer_to_relocations
        type: u4
        doc: 'The file pointer to the beginning of relocation entries for the section. This is set to zero for executable images or if there are no relocations.'
      - id: pointer_to_linenumbers
        type: u4
        doc: 'The file pointer to the beginning of line-number entries for the section. This is set to zero if there are no COFF line numbers. This value should be zero for an image because COFF debugging information is deprecated.'
      - id: number_of_relocations
        type: u2
        doc: 'The number of relocation entries for the section. This is set to zero for executable images.'
      - id: number_of_linenumbers
        type: u2
        doc: 'The number of line-number entries for the section. This value should be zero for an image because COFF debugging information is deprecated.'
      - id: characteristics
        type: u4
        doc: 'The flags that describe the characteristics of the section.'
  debug_s:
    doc: '.debug$S section'
    params:
      - id: size
        type: u4
    seq:
      - id: signature
        type: u4
        valid:
          any-of: [4]
      - id: c13_stream
        if: signature == 4
        size: size - 4
        type: c13_line_stream

enums:
  machine:
    0x014c: image_file_machine_i386
    0x0162: image_file_machine_r3000
    0x0166: image_file_machine_r4000
    0x0168: image_file_machine_r10000
    0x0169: image_file_machine_wcemipsv2
    0x0184: image_file_machine_alpha
    0x01a2: image_file_machine_sh3
    0x01a3: image_file_machine_sh3dsp
    0x01a4: image_file_machine_sh3e
    0x01a6: image_file_machine_sh4
    0x01a8: image_file_machine_sh5
    0x01c0: image_file_machine_arm
    0x01c4: image_file_machine_armv7
    0xaa64: image_file_machine_arm64
    0x01c2: image_file_machine_thumb
    0x01d3: image_file_machine_am33
    0x01f0: image_file_machine_powerpc
    0x01f1: image_file_machine_powerpcfp
    0x0200: image_file_machine_ia64
    0x0266: image_file_machine_mips16
    0x0284: image_file_machine_alpha64
    0x0366: image_file_machine_mipsfpu
    0x0466: image_file_machine_mipsfpu16
    0x0520: image_file_machine_tricore
    0x0cef: image_file_machine_cef
    0x0ebc: image_file_machine_ebc
    0x5032: image_file_machine_riscv32
    0x5064: image_file_machine_riscv64
    0x5128: image_file_machine_riscv128
    0x8664: image_file_machine_amd64
    0x9041: image_file_machine_m32r
    0xc0ee: image_file_machine_cee
