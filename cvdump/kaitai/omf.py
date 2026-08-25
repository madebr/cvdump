# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
from cvdump.kaitai import pascal_string


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class Omf(KaitaiStruct):
    def __init__(self, _io, _parent=None, _root=None):
        super(Omf, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self
        self._read()

    def _read(self):
        pass


    def _fetch_instances(self):
        pass

    class OmfSourceFile(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(Omf.OmfSourceFile, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.c_seg = self._io.read_u2le()
            self.c_file = self._io.read_u2le()
            self.start_lines = []
            for i in range(self.c_seg):
                self.start_lines.append(self._io.read_u4le())

            self.ranges = []
            for i in range(self.c_seg):
                self.ranges.append(Omf.Range(self._io, self, self._root))

            self.name = pascal_string.PascalString(self._io)


        def _fetch_instances(self):
            pass
            for i in range(len(self.start_lines)):
                pass

            for i in range(len(self.ranges)):
                pass
                self.ranges[i]._fetch_instances()

            self.name._fetch_instances()


    class OmfSourceLine(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(Omf.OmfSourceLine, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.seg = self._io.read_u2le()
            self.count_lines = self._io.read_u2le()
            self.offsets = []
            for i in range(self.count_lines):
                self.offsets.append(self._io.read_u4le())

            self.lines = []
            for i in range(self.count_lines):
                self.lines.append(self._io.read_u2le())



        def _fetch_instances(self):
            pass
            for i in range(len(self.offsets)):
                pass

            for i in range(len(self.lines)):
                pass



    class OmfSourceModule(KaitaiStruct):
        """OMFSourceModule (cvexefmt.h)."""
        def __init__(self, _io, _parent=None, _root=None):
            super(Omf.OmfSourceModule, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.c_file = self._io.read_u2le()
            self.c_seg = self._io.read_u2le()
            self.file_starts = []
            for i in range(self.c_file):
                self.file_starts.append(self._io.read_u4le())

            self.segment_ranges = []
            for i in range(self.c_seg):
                self.segment_ranges.append(Omf.Range(self._io, self, self._root))

            self.unks = []
            for i in range(self.c_seg):
                self.unks.append(self._io.read_u2le())



        def _fetch_instances(self):
            pass
            for i in range(len(self.file_starts)):
                pass

            for i in range(len(self.segment_ranges)):
                pass
                self.segment_ranges[i]._fetch_instances()

            for i in range(len(self.unks)):
                pass



    class Range(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(Omf.Range, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.begin = self._io.read_u4le()
            self.end = self._io.read_u4le()


        def _fetch_instances(self):
            pass



