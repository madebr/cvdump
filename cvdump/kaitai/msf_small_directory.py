# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class MsfSmallDirectory(KaitaiStruct):
    def __init__(self, _io, _parent=None, _root=None):
        super(MsfSmallDirectory, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self
        self._read()

    def _read(self):
        self.num_streams = self._io.read_u2le()
        self.reserved = self._io.read_u2le()
        self.stream_sizes = []
        for i in range(self.num_streams):
            self.stream_sizes.append(MsfSmallDirectory.StreamDirectorySize(self._io, self, self._root))

        self.stream_blocks = []
        i = 0
        while not self._io.is_eof():
            self.stream_blocks.append(self._io.read_u2le())
            i += 1



    def _fetch_instances(self):
        pass
        for i in range(len(self.stream_sizes)):
            pass
            self.stream_sizes[i]._fetch_instances()

        for i in range(len(self.stream_blocks)):
            pass


    class StreamDirectorySize(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(MsfSmallDirectory.StreamDirectorySize, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.size = self._io.read_u4le()
            self.reserved_ptr = self._io.read_u4le()


        def _fetch_instances(self):
            pass



