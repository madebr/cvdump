# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class InfoStream(KaitaiStruct):
    def __init__(self, _io, _parent=None, _root=None):
        super(InfoStream, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self
        self._read()

    def _read(self):
        self.version = self._io.read_u4le()
        self.timestamp = self._io.read_u4le()
        if self.version == 19960307:
            pass
            self.contents_vc50 = InfoStream.ContentsVc50(self._io, self, self._root)

        if self.version == 19970604:
            pass
            self.contents_vc98 = InfoStream.ContentsVc98(self._io, self, self._root)

        if self.version == 20000404:
            pass
            self.contents_vc70 = InfoStream.ContentsVc70(self._io, self, self._root)



    def _fetch_instances(self):
        pass
        if self.version == 19960307:
            pass
            self.contents_vc50._fetch_instances()

        if self.version == 19970604:
            pass
            self.contents_vc98._fetch_instances()

        if self.version == 20000404:
            pass
            self.contents_vc70._fetch_instances()


    class BitArray(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(InfoStream.BitArray, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.word_count = self._io.read_u4le()
            self.words = []
            for i in range(self.word_count):
                self.words.append(self._io.read_u4le())



        def _fetch_instances(self):
            pass
            for i in range(len(self.words)):
                pass



    class ContentsVc50(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(InfoStream.ContentsVc50, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.age_or_unknown = self._io.read_u4le()
            self.string_buffer_size = self._io.read_u4le()
            self.string_buffer = self._io.read_bytes(self.string_buffer_size)
            self.amount_of_entries = self._io.read_u4le()
            self.unknown_array = []
            for i in range(4):
                self.unknown_array.append(self._io.read_u4le())

            self.entries = []
            for i in range(self.amount_of_entries):
                self.entries.append(InfoStream.NameEntry(self._io, self, self._root))

            self.unused = self._io.read_u4le()


        def _fetch_instances(self):
            pass
            for i in range(len(self.unknown_array)):
                pass

            for i in range(len(self.entries)):
                pass
                self.entries[i]._fetch_instances()



    class ContentsVc70(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(InfoStream.ContentsVc70, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.age = self._io.read_u4le()
            self.uuid = self._io.read_bytes(16)
            self.string_buffer_size = self._io.read_u4le()
            self.string_buffer = self._io.read_bytes(self.string_buffer_size)
            self.amount_of_entries = self._io.read_u4le()
            self.capacity = self._io.read_u4le()
            self.present_bits = InfoStream.BitArray(self._io, self, self._root)
            self.deleted_bits = InfoStream.BitArray(self._io, self, self._root)
            self.entries = []
            for i in range(self.amount_of_entries):
                self.entries.append(InfoStream.NameEntry(self._io, self, self._root))

            self.unused = self._io.read_u4le()
            self.features = []
            i = 0
            while not self._io.is_eof():
                self.features.append(self._io.read_u4le())
                i += 1



        def _fetch_instances(self):
            pass
            self.present_bits._fetch_instances()
            self.deleted_bits._fetch_instances()
            for i in range(len(self.entries)):
                pass
                self.entries[i]._fetch_instances()

            for i in range(len(self.features)):
                pass



    class ContentsVc98(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(InfoStream.ContentsVc98, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.age_or_unknown = self._io.read_u4le()
            self.string_buffer_size = self._io.read_u4le()
            self.string_buffer = self._io.read_bytes(self.string_buffer_size)
            self.amount_of_entries = self._io.read_u4le()
            self.unknown_array = []
            for i in range(2 * self.amount_of_entries):
                self.unknown_array.append(self._io.read_u4le())

            self.entries = []
            for i in range(self.amount_of_entries):
                self.entries.append(InfoStream.NameEntry(self._io, self, self._root))

            self.unused = self._io.read_u4le()


        def _fetch_instances(self):
            pass
            for i in range(len(self.unknown_array)):
                pass

            for i in range(len(self.entries)):
                pass
                self.entries[i]._fetch_instances()



    class NameEntry(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(InfoStream.NameEntry, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.key = self._io.read_u4le()
            self.value = self._io.read_u4le()


        def _fetch_instances(self):
            pass



