# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
from cvdump.kaitai import guid
from cvdump.kaitai import cv_symbol_stream
from cvdump.kaitai import c13_line_stream


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class Coff(KaitaiStruct):
    def __init__(self, _io, _parent=None, _root=None):
        super(Coff, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self
        self._read()

    def _read(self):
        self.header = Coff.Header(self._io, self, self._root)
        self.section_headers = []
        for i in range(self.header.number_of_sections):
            self.section_headers.append(Coff.SectionHeader(self._io, self, self._root))



    def _fetch_instances(self):
        pass
        self.header._fetch_instances()
        for i in range(len(self.section_headers)):
            pass
            self.section_headers[i]._fetch_instances()


    class AnonObjectHeaderBigobj(KaitaiStruct):
        """ANON_OBJECT_HEADER_BIGOBJ."""
        def __init__(self, sig1, sig2, _io, _parent=None, _root=None):
            super(Coff.AnonObjectHeaderBigobj, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self.sig1 = sig1
            self.sig2 = sig2
            self._read()

        def _read(self):
            self.version = self._io.read_u2le()
            _ = self.version
            if not _ >= 2:
                raise kaitaistruct.ValidationExprError(self.version, self._io, u"/types/anon_object_header_bigobj/seq/0")
            self.machine = self._io.read_u2le()
            self.time_date_stamp = self._io.read_u4le()
            self.class_id = guid.Guid(self._io)
            _ = self.class_id
            if not  ((_.data1 == 3518669255) and (_.data2 == 47854) and (_.data3 == 19369) and (KaitaiStream.byte_array_index(_.data4, 0) == 175) and (KaitaiStream.byte_array_index(_.data4, 1) == 32) and (KaitaiStream.byte_array_index(_.data4, 2) == 250) and (KaitaiStream.byte_array_index(_.data4, 3) == 246) and (KaitaiStream.byte_array_index(_.data4, 4) == 106) and (KaitaiStream.byte_array_index(_.data4, 5) == 164) and (KaitaiStream.byte_array_index(_.data4, 6) == 220) and (KaitaiStream.byte_array_index(_.data4, 7) == 184)) :
                raise kaitaistruct.ValidationExprError(self.class_id, self._io, u"/types/anon_object_header_bigobj/seq/3")
            self.size_of_data = self._io.read_u4le()
            self.flags = self._io.read_u4le()
            self.meta_data_size = self._io.read_u4le()
            self.meta_data_offset = self._io.read_u4le()
            self.number_of_sections = self._io.read_u4le()
            self.pointer_to_symbol_table = self._io.read_u4le()
            self.number_of_symbols = self._io.read_u4le()


        def _fetch_instances(self):
            pass
            self.class_id._fetch_instances()


    class DebugS(KaitaiStruct):
        """.debug$S section."""
        def __init__(self, size, _io, _parent=None, _root=None):
            super(Coff.DebugS, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self.size = size
            self._read()

        def _read(self):
            self.signature = self._io.read_u4le()
            if not  ((self.signature == 1) or (self.signature == 2) or (self.signature == 4)) :
                raise kaitaistruct.ValidationNotAnyOfError(self.signature, self._io, u"/types/debug_s/seq/0")
            if self.signature == 4:
                pass
                self._raw_c13_stream = self._io.read_bytes(self.size - 4)
                _io__raw_c13_stream = KaitaiStream(BytesIO(self._raw_c13_stream))
                self.c13_stream = c13_line_stream.C13LineStream(_io__raw_c13_stream)

            if  ((self.signature == 1) or (self.signature == 2)) :
                pass
                self._raw_symbols = self._io.read_bytes(self.size - 4)
                _io__raw_symbols = KaitaiStream(BytesIO(self._raw_symbols))
                self.symbols = cv_symbol_stream.CvSymbolStream(0, False, _io__raw_symbols)



        def _fetch_instances(self):
            pass
            if self.signature == 4:
                pass
                self.c13_stream._fetch_instances()

            if  ((self.signature == 1) or (self.signature == 2)) :
                pass
                self.symbols._fetch_instances()



    class Edata(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(Coff.Edata, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.reserved = self._io.read_u4le()
            if not self.reserved == 0:
                raise kaitaistruct.ValidationNotEqualError(0, self.reserved, self._io, u"/types/edata/seq/0")
            self.time_date_stamp = self._io.read_u4le()
            self.major_version = self._io.read_u2le()
            self.minor_version = self._io.read_u2le()
            self.name_rva = self._io.read_u4le()
            self.ordinal_base = self._io.read_u4le()
            self.number_of_functions = self._io.read_u4le()
            self.number_of_names = self._io.read_u4le()
            self.address_table = self._io.read_u4le()
            self.name_pointer_table = self._io.read_u4le()
            self.ordinal_table = self._io.read_u4le()
            self.storage_address_table = []
            for i in range(self.number_of_functions):
                self.storage_address_table.append(self._io.read_u4le())

            self.storage_name_pointer_table = []
            for i in range(self.number_of_names):
                self.storage_name_pointer_table.append(self._io.read_u4le())

            self.storage_ordinal_table = []
            for i in range(self.number_of_names):
                self.storage_ordinal_table.append(self._io.read_u2le())

            self.storage_names = self._io.read_bytes_full()


        def _fetch_instances(self):
            pass
            for i in range(len(self.storage_address_table)):
                pass

            for i in range(len(self.storage_name_pointer_table)):
                pass

            for i in range(len(self.storage_ordinal_table)):
                pass



    class Header(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(Coff.Header, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.data1 = self._io.read_u2le()
            self.data2 = self._io.read_u2le()
            if (not (self.is_big_obj)):
                pass
                self.normal_header = Coff.NormalHeader(self.data1, self.data2, self._io, self, self._root)

            if self.is_big_obj:
                pass
                self.bigobj_header = Coff.AnonObjectHeaderBigobj(self.data1, self.data2, self._io, self, self._root)



        def _fetch_instances(self):
            pass
            if (not (self.is_big_obj)):
                pass
                self.normal_header._fetch_instances()

            if self.is_big_obj:
                pass
                self.bigobj_header._fetch_instances()


        @property
        def is_big_obj(self):
            if hasattr(self, '_m_is_big_obj'):
                return self._m_is_big_obj

            self._m_is_big_obj =  ((self.data1 == 0) and (self.data2 == 65535)) 
            return getattr(self, '_m_is_big_obj', None)

        @property
        def machine(self):
            if hasattr(self, '_m_machine'):
                return self._m_machine

            self._m_machine = (self.bigobj_header.machine if self.is_big_obj else self.normal_header.machine)
            return getattr(self, '_m_machine', None)

        @property
        def number_of_sections(self):
            if hasattr(self, '_m_number_of_sections'):
                return self._m_number_of_sections

            self._m_number_of_sections = (self.bigobj_header.number_of_sections if self.is_big_obj else self.normal_header.number_of_sections)
            return getattr(self, '_m_number_of_sections', None)

        @property
        def number_of_symbols(self):
            if hasattr(self, '_m_number_of_symbols'):
                return self._m_number_of_symbols

            self._m_number_of_symbols = (self.bigobj_header.number_of_symbols if self.is_big_obj else self.normal_header.number_of_symbols)
            return getattr(self, '_m_number_of_symbols', None)

        @property
        def pointer_to_symbol_table(self):
            if hasattr(self, '_m_pointer_to_symbol_table'):
                return self._m_pointer_to_symbol_table

            self._m_pointer_to_symbol_table = (self.bigobj_header.pointer_to_symbol_table if self.is_big_obj else self.normal_header.pointer_to_symbol_table)
            return getattr(self, '_m_pointer_to_symbol_table', None)

        @property
        def time_date_stamp(self):
            if hasattr(self, '_m_time_date_stamp'):
                return self._m_time_date_stamp

            self._m_time_date_stamp = (self.bigobj_header.time_date_stamp if self.is_big_obj else self.normal_header.time_date_stamp)
            return getattr(self, '_m_time_date_stamp', None)


    class NormalHeader(KaitaiStruct):
        def __init__(self, machine, number_of_sections, _io, _parent=None, _root=None):
            super(Coff.NormalHeader, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self.machine = machine
            self.number_of_sections = number_of_sections
            self._read()

        def _read(self):
            self.time_date_stamp = self._io.read_u4le()
            self.pointer_to_symbol_table = self._io.read_u4le()
            self.number_of_symbols = self._io.read_u4le()
            self.size_of_optional_header = self._io.read_u2le()
            self.characteristics = self._io.read_u2le()


        def _fetch_instances(self):
            pass


    class Relocation(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(Coff.Relocation, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.virtual_address = self._io.read_u4le()
            self.symbol_table_index = self._io.read_u4le()
            self.type = self._io.read_u2le()


        def _fetch_instances(self):
            pass


    class Relocations(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(Coff.Relocations, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.items = []
            i = 0
            while not self._io.is_eof():
                self.items.append(Coff.Relocation(self._io, self, self._root))
                i += 1



        def _fetch_instances(self):
            pass
            for i in range(len(self.items)):
                pass
                self.items[i]._fetch_instances()



    class SectionHeader(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(Coff.SectionHeader, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.name = self._io.read_bytes(8)
            self.virtual_size = self._io.read_u4le()
            self.virtual_address = self._io.read_u4le()
            self.size_of_raw_data = self._io.read_u4le()
            self.pointer_to_raw_data = self._io.read_u4le()
            self.pointer_to_relocations = self._io.read_u4le()
            self.pointer_to_linenumbers = self._io.read_u4le()
            self.number_of_relocations = self._io.read_u2le()
            self.number_of_linenumbers = self._io.read_u2le()
            self.characteristics = self._io.read_u4le()


        def _fetch_instances(self):
            pass


    class SymbolTable(KaitaiStruct):
        def __init__(self, big, _io, _parent=None, _root=None):
            super(Coff.SymbolTable, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self.big = big
            self._read()

        def _read(self):
            self.items = []
            i = 0
            while not self._io.is_eof():
                self.items.append(Coff.SymbolTableItem(self.big, self._io, self, self._root))
                i += 1



        def _fetch_instances(self):
            pass
            for i in range(len(self.items)):
                pass
                self.items[i]._fetch_instances()



    class SymbolTableItem(KaitaiStruct):
        def __init__(self, big, _io, _parent=None, _root=None):
            super(Coff.SymbolTableItem, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self.big = big
            self._read()

        def _read(self):
            self.name = self._io.read_bytes(8)
            self.value = self._io.read_u4le()
            if (not (self.big)):
                pass
                self.section_number_small = self._io.read_s2le()

            if self.big:
                pass
                self.section_number_big = self._io.read_s4le()

            self.type = self._io.read_u2le()
            self.storage_class = self._io.read_u1()
            self.number_of_aux_symbols = self._io.read_u1()
            self.aux_symbols = self._io.read_bytes((20 if self.big else 18) * self.number_of_aux_symbols)


        def _fetch_instances(self):
            pass
            if (not (self.big)):
                pass

            if self.big:
                pass


        @property
        def section_number(self):
            if hasattr(self, '_m_section_number'):
                return self._m_section_number

            self._m_section_number = (self.section_number_big if self.big else self.section_number_small)
            return getattr(self, '_m_section_number', None)



