# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class NamesStream(KaitaiStruct):
    def __init__(self, _io, _parent=None, _root=None):
        super(NamesStream, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self
        self._read()

    def _read(self):
        self.signature = self._io.read_u4le()
        if not self.signature == 4026462206:
            raise kaitaistruct.ValidationNotEqualError(4026462206, self.signature, self._io, u"/seq/0")
        self.hash_version = self._io.read_u4le()
        if not  ((self.hash_version == 1) or (self.hash_version == 2)) :
            raise kaitaistruct.ValidationNotAnyOfError(self.hash_version, self._io, u"/seq/1")
        self.string_buffer_size = self._io.read_u4le()
        self.string_buffer = self._io.read_bytes(self.string_buffer_size)
        self.bucket_count = self._io.read_u4le()
        self.buckets = []
        for i in range(self.bucket_count):
            self.buckets.append(self._io.read_u4le())

        self.amount_of_strings = self._io.read_u4le()


    def _fetch_instances(self):
        pass
        for i in range(len(self.buckets)):
            pass



