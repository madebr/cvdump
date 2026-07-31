# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class DbiStream(KaitaiStruct):
    def __init__(self, _io, _parent=None, _root=None):
        super(DbiStream, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self
        self._read()

    def _read(self):
        self.header = DbiStream.DebugInformationHeader(self._io, self, self._root)
        self._raw_module_info = self._io.read_bytes(self.header.module_info_size)
        _io__raw_module_info = KaitaiStream(BytesIO(self._raw_module_info))
        self.module_info = DbiStream.ModuleInfosV50(_io__raw_module_info, self, self._root)
        self._raw_section_contribution = self._io.read_bytes(self.header.section_contribution_size)
        _io__raw_section_contribution = KaitaiStream(BytesIO(self._raw_section_contribution))
        self.section_contribution = DbiStream.SectionContribsV40(_io__raw_section_contribution, self, self._root)
        self._raw_section_map = self._io.read_bytes(self.header.section_map_size)
        _io__raw_section_map = KaitaiStream(BytesIO(self._raw_section_map))
        self.section_map = DbiStream.OmfSegMap(_io__raw_section_map, self, self._root)
        self._raw_source_info = self._io.read_bytes(self.header.source_info_size)
        _io__raw_source_info = KaitaiStream(BytesIO(self._raw_source_info))
        self.source_info = DbiStream.DbiSourceInfo(_io__raw_source_info, self, self._root)


    def _fetch_instances(self):
        pass
        self.header._fetch_instances()
        self.module_info._fetch_instances()
        self.section_contribution._fetch_instances()
        self.section_map._fetch_instances()
        self.source_info._fetch_instances()

    class DbiSourceInfo(KaitaiStruct):
        """DBI1::reloadFileInfo (dbi.cpp)."""
        def __init__(self, _io, _parent=None, _root=None):
            super(DbiStream.DbiSourceInfo, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.count_modules = self._io.read_u2le()
            self.count_source_files = self._io.read_u2le()
            self.module_indices = []
            for i in range(self.count_modules):
                self.module_indices.append(self._io.read_u2le())

            self.module_file_counts = []
            for i in range(self.count_modules):
                self.module_file_counts.append(self._io.read_u2le())

            self.file_name_offsets = []
            for i in range(self.count_source_files):
                self.file_name_offsets.append(self._io.read_u4le())

            self.buffer = self._io.read_bytes_full()


        def _fetch_instances(self):
            pass
            for i in range(len(self.module_indices)):
                pass

            for i in range(len(self.module_file_counts)):
                pass

            for i in range(len(self.file_name_offsets)):
                pass



    class DebugInformationHeader(KaitaiStruct):
        """DBIHdr (dbi.h)."""
        def __init__(self, _io, _parent=None, _root=None):
            super(DbiStream.DebugInformationHeader, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.global_symbol_stream = self._io.read_u2le()
            self.public_symbol_stream = self._io.read_u2le()
            self.symbol_record_stream = self._io.read_u2le()
            self.reserved1 = self._io.read_u2le()
            self.module_info_size = self._io.read_u4le()
            self.section_contribution_size = self._io.read_u4le()
            self.section_map_size = self._io.read_u4le()
            self.source_info_size = self._io.read_u4le()


        def _fetch_instances(self):
            pass


    class ModuleInfoV50(KaitaiStruct):
        """MODI50 (dbi.h)."""
        def __init__(self, _io, _parent=None, _root=None):
            super(DbiStream.ModuleInfoV50, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.currently_open_mod = self._io.read_u4le()
            self.section_contrib = DbiStream.SectionContribV40(self._io, self, self._root)
            self.flags = self._io.read_u2le()
            self.debug_info_stream = self._io.read_u2le()
            self.symbols_size = self._io.read_u4le()
            self.lines_size = self._io.read_u4le()
            self.frame_pointer_opt_size = self._io.read_u4le()
            self.source_file_count = self._io.read_u2le()
            self.unused = self._io.read_u2le()
            self.source_filename_index = self._io.read_u4le()
            self.module_name = (self._io.read_bytes_term(0, False, True, True)).decode(u"ASCII")
            self.object_name = (self._io.read_bytes_term(0, False, True, True)).decode(u"ASCII")
            self.struct_padding = self._io.read_bytes((4 - self._io.pos() % 4) % 4)


        def _fetch_instances(self):
            pass
            self.section_contrib._fetch_instances()


    class ModuleInfosV50(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(DbiStream.ModuleInfosV50, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.entries = []
            i = 0
            while not self._io.is_eof():
                self.entries.append(DbiStream.ModuleInfoV50(self._io, self, self._root))
                i += 1



        def _fetch_instances(self):
            pass
            for i in range(len(self.entries)):
                pass
                self.entries[i]._fetch_instances()



    class OmfSegMap(KaitaiStruct):
        """OMFSegMap (cvexefmt.h)."""
        def __init__(self, _io, _parent=None, _root=None):
            super(DbiStream.OmfSegMap, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.c_seg = self._io.read_u2le()
            self.c_seg_log = self._io.read_u2le()
            self.rg_desc = []
            for i in range(self.c_seg):
                self.rg_desc.append(DbiStream.OmfSegMapDesc(self._io, self, self._root))



        def _fetch_instances(self):
            pass
            for i in range(len(self.rg_desc)):
                pass
                self.rg_desc[i]._fetch_instances()



    class OmfSegMapDesc(KaitaiStruct):
        """OMFSegMapDesc (pdbimpl.h)."""
        def __init__(self, _io, _parent=None, _root=None):
            super(DbiStream.OmfSegMapDesc, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.f_all = self._io.read_u2le()
            self.ovl = self._io.read_u2le()
            self.group = self._io.read_u2le()
            self.frame = self._io.read_u2le()
            self.i_seg_name = self._io.read_u2le()
            self.i_class_name = self._io.read_u2le()
            self.offset = self._io.read_u4le()
            self.cb_seg = self._io.read_u4le()


        def _fetch_instances(self):
            pass


    class SectionContribV40(KaitaiStruct):
        """struct SC40 (dbicommon.h)."""
        def __init__(self, _io, _parent=None, _root=None):
            super(DbiStream.SectionContribV40, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.section_index = self._io.read_u2le()
            self.padding = self._io.read_u2le()
            self.offset = self._io.read_u4le()
            self.size = self._io.read_u4le()
            self.characteristics = self._io.read_u4le()
            self.module_index = self._io.read_u2le()
            self.unknown2 = self._io.read_u2le()


        def _fetch_instances(self):
            pass


    class SectionContribsV40(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(DbiStream.SectionContribsV40, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.entries = []
            i = 0
            while not self._io.is_eof():
                self.entries.append(DbiStream.SectionContribV40(self._io, self, self._root))
                i += 1



        def _fetch_instances(self):
            pass
            for i in range(len(self.entries)):
                pass
                self.entries[i]._fetch_instances()




