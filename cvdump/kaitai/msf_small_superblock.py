# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class MsfSmallSuperblock(KaitaiStruct):
    def __init__(self, _io, _parent=None, _root=None):
        super(MsfSmallSuperblock, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self
        self._read()

    def _read(self):
        self.magic = self._io.read_bytes(44)
        if not self.magic == b"\x4D\x69\x63\x72\x6F\x73\x6F\x66\x74\x20\x43\x2F\x43\x2B\x2B\x20\x70\x72\x6F\x67\x72\x61\x6D\x20\x64\x61\x74\x61\x62\x61\x73\x65\x20\x32\x2E\x30\x30\x0D\x0A\x1A\x4A\x47\x00\x00":
            raise kaitaistruct.ValidationNotEqualError(b"\x4D\x69\x63\x72\x6F\x73\x6F\x66\x74\x20\x43\x2F\x43\x2B\x2B\x20\x70\x72\x6F\x67\x72\x61\x6D\x20\x64\x61\x74\x61\x62\x61\x73\x65\x20\x32\x2E\x30\x30\x0D\x0A\x1A\x4A\x47\x00\x00", self.magic, self._io, u"/seq/0")
        self.block_size = self._io.read_u4le()
        self.free_block_map_block = self._io.read_u2le()
        self.num_blocks = self._io.read_u2le()
        self.num_directory_bytes = self._io.read_u4le()
        self.unknown = self._io.read_u4le()
        self.block_map = []
        for i in range(((self.num_directory_bytes + self.block_size) - 1) // self.block_size):
            self.block_map.append(self._io.read_u2le())



    def _fetch_instances(self):
        pass
        for i in range(len(self.block_map)):
            pass



