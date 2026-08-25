# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
from cvdump.kaitai import cv_symbol


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class CvSymbolStream(KaitaiStruct):
    def __init__(self, delta_pos, _io, _parent=None, _root=None):
        super(CvSymbolStream, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self
        self.delta_pos = delta_pos
        self._read()

    def _read(self):
        self.entries = []
        i = 0
        while not self._io.is_eof():
            self.entries.append(cv_symbol.CvSymbol(self._io.pos() + self.delta_pos, self._io))
            i += 1



    def _fetch_instances(self):
        pass
        for i in range(len(self.entries)):
            pass
            self.entries[i]._fetch_instances()



