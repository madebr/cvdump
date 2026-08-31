# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
from cvdump.kaitai import c13_line_stream
from cvdump.kaitai import cv_symbol_stream


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class Coff(KaitaiStruct):
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
            if not  ((self.signature == 1) or (self.signature == 2) or (self.signature == 4)) :
                raise kaitaistruct.ValidationNotAnyOfError(self.signature, self._io, u"/types/debug_s/seq/0")
            if self.signature == 4:
                pass
                self._raw_c13_stream = self._io.read_bytes(self.size - 4)
                _io__raw_c13_stream = KaitaiStream(BytesIO(self._raw_c13_stream))
                self.c13_stream = c13_line_stream.C13LineStream(_io__raw_c13_stream)

            if  ((self.signature == 1) or (self.signature == 2)) :
                pass
                self._raw_symbols = self._io.read_bytes(self.size - 4)
                _io__raw_symbols = KaitaiStream(BytesIO(self._raw_symbols))
                self.symbols = cv_symbol_stream.CvSymbolStream(0, False, _io__raw_symbols)



        def _fetch_instances(self):
            pass
            if self.signature == 4:
                pass
                self.c13_stream._fetch_instances()

            if  ((self.signature == 1) or (self.signature == 2)) :
                pass
                self.symbols._fetch_instances()



    class Header(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(Coff.Header, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.machine = self._io.read_u2le()
            self.number_of_sections = self._io.read_u2le()
            self.time_date_stamp = self._io.read_u4le()
            self.pointer_to_symbol_table = self._io.read_u4le()
            self.number_of_symbols = self._io.read_u4le()
            self.size_of_optional_header = self._io.read_u2le()
            self.characteristics = self._io.read_u2le()


        def _fetch_instances(self):
            pass


    class Relocation(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(Coff.Relocation, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.virtual_address = self._io.read_u4le()
            self.symbol_table_index = self._io.read_u4le()
            self.type = self._io.read_u2le()


        def _fetch_instances(self):
            pass


    class Relocations(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(Coff.Relocations, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.items = []
            i = 0
            while not self._io.is_eof():
                self.items.append(Coff.Relocation(self._io, self, self._root))
                i += 1



        def _fetch_instances(self):
            pass
            for i in range(len(self.items)):
                pass
                self.items[i]._fetch_instances()



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


    class SymbolTable(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(Coff.SymbolTable, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.items = []
            i = 0
            while not self._io.is_eof():
                self.items.append(Coff.SymbolTableItem(self._io, self, self._root))
                i += 1



        def _fetch_instances(self):
            pass
            for i in range(len(self.items)):
                pass
                self.items[i]._fetch_instances()



    class SymbolTableItem(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(Coff.SymbolTableItem, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.name = self._io.read_bytes(8)
            self.value = self._io.read_u4le()
            self.section_number = self._io.read_s2le()
            self.type = self._io.read_u2le()
            self.storage_class = self._io.read_u1()
            self.number_of_aux_symbols = self._io.read_u1()
            self.aux_symbols = self._io.read_bytes(18 * self.number_of_aux_symbols)


        def _fetch_instances(self):
            pass



