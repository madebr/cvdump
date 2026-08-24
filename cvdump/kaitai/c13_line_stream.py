# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
from enum import IntEnum


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class C13LineStream(KaitaiStruct):

    class DebugSSubsectionType(IntEnum):
        debug_s_symbols = 241
        debug_s_lines = 242
        debug_s_stringtable = 243
        debug_s_filechksms = 244
        debug_s_framedata = 245
        debug_s_inlineelines = 246
        debug_s_crossscopeimports = 247
        debug_s_crossscopeexports = 248
        debug_s_il_lines = 249
        debug_s_func_mdtoken_map = 250
        debug_s_type_mdtoken_map = 251
        debug_s_merged_assemblyinput = 252
        debug_s_coff_symbol_rva = 253
    def __init__(self, _io, _parent=None, _root=None):
        super(C13LineStream, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self
        self._read()

    def _read(self):
        self.subsections = []
        i = 0
        while not self._io.is_eof():
            self.subsections.append(C13LineStream.Subsection(self._io, self, self._root))
            i += 1



    def _fetch_instances(self):
        pass
        for i in range(len(self.subsections)):
            pass
            self.subsections[i]._fetch_instances()


    class CvLineT(KaitaiStruct):
        """CV_Line_t (cvinfo.h)."""
        def __init__(self, _io, _parent=None, _root=None):
            super(C13LineStream.CvLineT, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.offset = self._io.read_u4le()
            self.linenum_delta_statement = self._io.read_u4le()


        def _fetch_instances(self):
            pass

        @property
        def delta_line_number(self):
            if hasattr(self, '_m_delta_line_number'):
                return self._m_delta_line_number

            self._m_delta_line_number = self.linenum_delta_statement >> 24 & 127
            return getattr(self, '_m_delta_line_number', None)

        @property
        def is_statement(self):
            if hasattr(self, '_m_is_statement'):
                return self._m_is_statement

            self._m_is_statement = self.linenum_delta_statement >> 31
            return getattr(self, '_m_is_statement', None)

        @property
        def line_number_start(self):
            if hasattr(self, '_m_line_number_start'):
                return self._m_line_number_start

            self._m_line_number_start = self.linenum_delta_statement & 16777215
            return getattr(self, '_m_line_number_start', None)


    class DebugFilechecksums(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(C13LineStream.DebugFilechecksums, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.checksums = []
            i = 0
            while not self._io.is_eof():
                self.checksums.append(C13LineStream.Filechecksum(self._io.pos(), self._io, self, self._root))
                i += 1



        def _fetch_instances(self):
            pass
            for i in range(len(self.checksums)):
                pass
                self.checksums[i]._fetch_instances()



    class DebugLineTables(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(C13LineStream.DebugLineTables, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.items = []
            i = 0
            while not self._io.is_eof():
                self.items.append(C13LineStream.DebugLinesTableItem(self._io, self, self._root))
                i += 1



        def _fetch_instances(self):
            pass
            for i in range(len(self.items)):
                pass
                self.items[i]._fetch_instances()



    class DebugLines(KaitaiStruct):
        def __init__(self, size, _io, _parent=None, _root=None):
            super(C13LineStream.DebugLines, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self.size = size
            self._read()

        def _read(self):
            self.off_con = self._io.read_u4le()
            self.seg_con = self._io.read_u2le()
            self.flags = self._io.read_u2le()
            self.count_con = self._io.read_u4le()
            self._raw_tables = self._io.read_bytes(self.size - 12)
            _io__raw_tables = KaitaiStream(BytesIO(self._raw_tables))
            self.tables = C13LineStream.DebugLineTables(_io__raw_tables, self, self._root)


        def _fetch_instances(self):
            pass
            self.tables._fetch_instances()


    class DebugLinesTableItem(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(C13LineStream.DebugLinesTableItem, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.fileid = self._io.read_u4le()
            self.count_lines = self._io.read_u4le()
            self.file_block_size = self._io.read_u4le()
            self.lines = []
            for i in range(self.count_lines):
                self.lines.append(C13LineStream.CvLineT(self._io, self, self._root))



        def _fetch_instances(self):
            pass
            for i in range(len(self.lines)):
                pass
                self.lines[i]._fetch_instances()



    class Filechecksum(KaitaiStruct):
        def __init__(self, pos, _io, _parent=None, _root=None):
            super(C13LineStream.Filechecksum, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self.pos = pos
            self._read()

        def _read(self):
            self.name_index = self._io.read_u4le()
            self.hash_size = self._io.read_u1()
            self.hash_type = self._io.read_u1()
            self.hash = self._io.read_bytes(self.hash_size)
            self.padding = self._io.read_bytes((4 - self._io.pos() % 4) % 4)


        def _fetch_instances(self):
            pass


    class Subsection(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(C13LineStream.Subsection, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.header = C13LineStream.SubsectionHeader(self._io, self, self._root)
            _on = self.header.type
            if _on == C13LineStream.DebugSSubsectionType.debug_s_filechksms:
                pass
                self._raw_contents = self._io.read_bytes(self.header.size)
                _io__raw_contents = KaitaiStream(BytesIO(self._raw_contents))
                self.contents = C13LineStream.DebugFilechecksums(_io__raw_contents, self, self._root)
            elif _on == C13LineStream.DebugSSubsectionType.debug_s_lines:
                pass
                self._raw_contents = self._io.read_bytes(self.header.size)
                _io__raw_contents = KaitaiStream(BytesIO(self._raw_contents))
                self.contents = C13LineStream.DebugLines(self.header.size, _io__raw_contents, self, self._root)
            else:
                pass
                self.contents = self._io.read_bytes(self.header.size)


        def _fetch_instances(self):
            pass
            self.header._fetch_instances()
            _on = self.header.type
            if _on == C13LineStream.DebugSSubsectionType.debug_s_filechksms:
                pass
                self.contents._fetch_instances()
            elif _on == C13LineStream.DebugSSubsectionType.debug_s_lines:
                pass
                self.contents._fetch_instances()
            else:
                pass


    class SubsectionHeader(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(C13LineStream.SubsectionHeader, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.type = KaitaiStream.resolve_enum(C13LineStream.DebugSSubsectionType, self._io.read_u4le())
            self.size = self._io.read_u4le()


        def _fetch_instances(self):
            pass



