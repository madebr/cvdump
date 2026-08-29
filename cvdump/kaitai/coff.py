# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
from cvdump.kaitai import c13_line_stream
from enum import IntEnum


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class Coff(KaitaiStruct):

    class Machine(IntEnum):
        image_file_machine_i386 = 332
        image_file_machine_r3000 = 354
        image_file_machine_r4000 = 358
        image_file_machine_r10000 = 360
        image_file_machine_wcemipsv2 = 361
        image_file_machine_alpha = 388
        image_file_machine_sh3 = 418
        image_file_machine_sh3dsp = 419
        image_file_machine_sh3e = 420
        image_file_machine_sh4 = 422
        image_file_machine_sh5 = 424
        image_file_machine_arm = 448
        image_file_machine_thumb = 450
        image_file_machine_armv7 = 452
        image_file_machine_am33 = 467
        image_file_machine_powerpc = 496
        image_file_machine_powerpcfp = 497
        image_file_machine_ia64 = 512
        image_file_machine_mips16 = 614
        image_file_machine_alpha64 = 644
        image_file_machine_mipsfpu = 870
        image_file_machine_mipsfpu16 = 1126
        image_file_machine_tricore = 1312
        image_file_machine_cef = 3311
        image_file_machine_ebc = 3772
        image_file_machine_riscv32 = 20530
        image_file_machine_riscv64 = 20580
        image_file_machine_riscv128 = 20776
        image_file_machine_amd64 = 34404
        image_file_machine_m32r = 36929
        image_file_machine_arm64 = 43620
        image_file_machine_cee = 49390
    def __init__(self, _io, _parent=None, _root=None):
        super(Coff, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self
        self._read()

    def _read(self):
        self.header = Coff.Header(self._io, self, self._root)
        self.section_headers = []
        for i in range(self.header.number_of_sections):
            self.section_headers.append(Coff.SectionHeader(self._io, self, self._root))



    def _fetch_instances(self):
        pass
        self.header._fetch_instances()
        for i in range(len(self.section_headers)):
            pass
            self.section_headers[i]._fetch_instances()


    class DebugS(KaitaiStruct):
        """.debug$S section."""
        def __init__(self, size, _io, _parent=None, _root=None):
            super(Coff.DebugS, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self.size = size
            self._read()

        def _read(self):
            self.signature = self._io.read_u4le()
            if not  ((self.signature == 4)) :
                raise kaitaistruct.ValidationNotAnyOfError(self.signature, self._io, u"/types/debug_s/seq/0")
            if self.signature == 4:
                pass
                self._raw_c13_stream = self._io.read_bytes(self.size - 4)
                _io__raw_c13_stream = KaitaiStream(BytesIO(self._raw_c13_stream))
                self.c13_stream = c13_line_stream.C13LineStream(_io__raw_c13_stream)



        def _fetch_instances(self):
            pass
            if self.signature == 4:
                pass
                self.c13_stream._fetch_instances()



    class Header(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(Coff.Header, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.machine = KaitaiStream.resolve_enum(Coff.Machine, self._io.read_u2le())
            self.number_of_sections = self._io.read_u2le()
            self.time_date_stamp = self._io.read_u4le()
            self.pointer_to_symbol_table = self._io.read_u4le()
            self.number_of_symbols = self._io.read_u4le()
            self.size_of_optional_header = self._io.read_u2le()
            self.characteristics = self._io.read_u2le()


        def _fetch_instances(self):
            pass


    class SectionHeader(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(Coff.SectionHeader, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.name = self._io.read_bytes(8)
            self.virtual_size = self._io.read_u4le()
            self.virtual_address = self._io.read_u4le()
            self.size_of_raw_data = self._io.read_u4le()
            self.pointer_to_raw_data = self._io.read_u4le()
            self.pointer_to_relocations = self._io.read_u4le()
            self.pointer_to_linenumbers = self._io.read_u4le()
            self.number_of_relocations = self._io.read_u2le()
            self.number_of_linenumbers = self._io.read_u2le()
            self.characteristics = self._io.read_u4le()


        def _fetch_instances(self):
            pass



