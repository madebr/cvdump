# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class PsiGsi(KaitaiStruct):
    def __init__(self, _io, _parent=None, _root=None):
        super(PsiGsi, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self
        self._read()

    def _read(self):
        pass


    def _fetch_instances(self):
        pass

    class NewHeader(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(PsiGsi.NewHeader, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.version_signature = self._io.read_u4le()
            if not self.version_signature == 4294967295:
                raise kaitaistruct.ValidationNotEqualError(4294967295, self.version_signature, self._io, u"/types/new_header/seq/0")
            self.version = self._io.read_u4le()
            if not self.version == 4026400768 + 19990810:
                raise kaitaistruct.ValidationNotEqualError(4026400768 + 19990810, self.version, self._io, u"/types/new_header/seq/1")
            self.hash_records_byte_size = self._io.read_u4le()
            self.bucket_information_byte_size = self._io.read_u4le()


        def _fetch_instances(self):
            pass


    class PdbHashRecord(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(PsiGsi.PdbHashRecord, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.offset_symbol_record_stream_plus_one = self._io.read_u4le()
            if  ((self.offset_symbol_record_stream_plus_one != 0) and (self.offset_symbol_record_stream_plus_one != 4294967295)) :
                pass
                self.reference_counter = self._io.read_u4le()



        def _fetch_instances(self):
            pass
            if  ((self.offset_symbol_record_stream_plus_one != 0) and (self.offset_symbol_record_stream_plus_one != 4294967295)) :
                pass



    class PdbHashRecordArray(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(PsiGsi.PdbHashRecordArray, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.entries = []
            i = 0
            while not self._io.is_eof():
                self.entries.append(PsiGsi.PdbHashRecord(self._io, self, self._root))
                i += 1



        def _fetch_instances(self):
            pass
            for i in range(len(self.entries)):
                pass
                self.entries[i]._fetch_instances()



    class PsiStreamHeader(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(PsiGsi.PsiStreamHeader, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.hash_table_information_bytes_size = self._io.read_u4le()
            self.address_map_byte_size = self._io.read_u4le()
            self.number_of_thunks = self._io.read_u4le()
            self.thunk_bytes_size = self._io.read_u4le()
            self.thunk_table_section_id = self._io.read_u2le()
            self.padding = self._io.read_u2le()
            self.thunk_table_offset_in_section = self._io.read_u4le()
            self.number_of_sections_in_thunk_section_map = self._io.read_u4le()


        def _fetch_instances(self):
            pass



