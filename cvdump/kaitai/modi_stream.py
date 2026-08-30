# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
from cvdump.kaitai import c13_line_stream
from cvdump.kaitai import cv_symbol


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class ModiStream(KaitaiStruct):
    def __init__(self, symbols_size, c11_line_size, c13_line_size, _io, _parent=None, _root=None):
        super(ModiStream, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self
        self.symbols_size = symbols_size
        self.c11_line_size = c11_line_size
        self.c13_line_size = c13_line_size
        self._read()

    def _read(self):
        if self.symbols_size > 0:
            pass
            self.signature = self._io.read_u4le()
            if not  ((self.signature == 65537) or (self.signature == 1) or (self.signature == 2) or (self.signature == 4)) :
                raise kaitaistruct.ValidationNotAnyOfError(self.signature, self._io, u"/seq/0")

        if self.symbols_size > 0:
            pass
            self._raw_symbols = self._io.read_bytes(self.symbols_size - 4)
            _io__raw_symbols = KaitaiStream(BytesIO(self._raw_symbols))
            self.symbols = ModiStream.SymbolEntries(_io__raw_symbols, self, self._root)

        self.c11_line_info = self._io.read_bytes(self.c11_line_size)
        self._raw_c13_line_info = self._io.read_bytes(self.c13_line_size)
        _io__raw_c13_line_info = KaitaiStream(BytesIO(self._raw_c13_line_info))
        self.c13_line_info = c13_line_stream.C13LineStream(_io__raw_c13_line_info)
        if  ((self.symbols_size > 0) and (self.signature != 65537)) :
            pass
            self.global_refs_size = self._io.read_u4le()

        if  ((self.symbols_size > 0) and (self.signature != 65537)) :
            pass
            self.global_refs = self._io.read_bytes(self.global_refs_size)



    def _fetch_instances(self):
        pass
        if self.symbols_size > 0:
            pass

        if self.symbols_size > 0:
            pass
            self.symbols._fetch_instances()

        self.c13_line_info._fetch_instances()
        if  ((self.symbols_size > 0) and (self.signature != 65537)) :
            pass

        if  ((self.symbols_size > 0) and (self.signature != 65537)) :
            pass


    class SymbolEntries(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(ModiStream.SymbolEntries, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.entries = []
            i = 0
            while not self._io.is_eof():
                self.entries.append(cv_symbol.CvSymbol(self._io.pos() + 4, True, self._io))
                i += 1



        def _fetch_instances(self):
            pass
            for i in range(len(self.entries)):
                pass
                self.entries[i]._fetch_instances()




