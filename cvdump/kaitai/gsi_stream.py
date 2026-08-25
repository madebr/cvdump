# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class GsiStream(KaitaiStruct):
    def __init__(self, _io, _parent=None, _root=None):
        super(GsiStream, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self
        self._read()

    def _read(self):
        self.header = GsiStream.Header(self._io, self, self._root)
        self._raw_hash_records = self._io.read_bytes(self.header.hash_records_byte_size)
        _io__raw_hash_records = KaitaiStream(BytesIO(self._raw_hash_records))
        self.hash_records = GsiStream.PdbHashRecordArray(_io__raw_hash_records, self, self._root)


    def _fetch_instances(self):
        pass
        self.header._fetch_instances()
        self.hash_records._fetch_instances()

    class Header(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(GsiStream.Header, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.version_signature = self._io.read_u4le()
            if not self.version_signature == 4294967295:
                raise kaitaistruct.ValidationNotEqualError(4294967295, self.version_signature, self._io, u"/types/header/seq/0")
            self.version = self._io.read_u4le()
            if not self.version == 4026400768 + 19990810:
                raise kaitaistruct.ValidationNotEqualError(4026400768 + 19990810, self.version, self._io, u"/types/header/seq/1")
            self.hash_records_byte_size = self._io.read_u4le()
            self.bucket_information_byte_size = self._io.read_u4le()


        def _fetch_instances(self):
            pass


    class PdbHashRecord(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(GsiStream.PdbHashRecord, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.offset_symbol_record_stream_plus_one = self._io.read_u4le()
            self.reference_counter = self._io.read_u4le()


        def _fetch_instances(self):
            pass


    class PdbHashRecordArray(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(GsiStream.PdbHashRecordArray, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.entries = []
            i = 0
            while not self._io.is_eof():
                self.entries.append(GsiStream.PdbHashRecord(self._io, self, self._root))
                i += 1



        def _fetch_instances(self):
            pass
            for i in range(len(self.entries)):
                pass
                self.entries[i]._fetch_instances()




