# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class FpoData(KaitaiStruct):
    """FPO_DATA (winnt.h)."""
    def __init__(self, _io, _parent=None, _root=None):
        super(FpoData, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self
        self._read()

    def _read(self):
        self.offset = self._io.read_u4le()
        self.proc_size = self._io.read_u4le()
        self.count_locals = self._io.read_u4le()
        self.count_params = self._io.read_u2le()
        self.flags = self._io.read_u2le()


    def _fetch_instances(self):
        pass

    class FpoDatas(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(FpoData.FpoDatas, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.items = []
            i = 0
            while not self._io.is_eof():
                self.items.append(FpoData(self._io, self, self._root))
                i += 1



        def _fetch_instances(self):
            pass
            for i in range(len(self.items)):
                pass
                self.items[i]._fetch_instances()




