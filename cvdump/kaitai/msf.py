# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class Msf(KaitaiStruct):
    """'Microsoft C/C++ program database 1.00\r\n\x1aJG\x00'
    [0x4d, 0x69, 0x63, 0x72, 0x6f, 0x73, 0x6f, 0x66, 0x74, 0x20, 0x43, 0x2f, 0x43, 0x2b, 0x2b, 0x20, 0x70, 0x72, 0x6f, 0x67, 0x72, 0x61, 0x6d, 0x20, 0x64, 0x61, 0x74, 0x61, 0x62, 0x61, 0x73, 0x65, 0x20, 0x31, 0x2e, 0x30, 0x30, 0x0d, 0x0a, 0x1a, 0x4a, 0x47, 0x00, 0x00]
    
    'Microsoft C/C++ program database 2.00\r\n\x1aJG\x00'
    [0x4d, 0x69, 0x63, 0x72, 0x6f, 0x73, 0x6f, 0x66, 0x74, 0x20, 0x43, 0x2f, 0x43, 0x2b, 0x2b, 0x20, 0x70, 0x72, 0x6f, 0x67, 0x72, 0x61, 0x6d, 0x20, 0x64, 0x61, 0x74, 0x61, 0x62, 0x61, 0x73, 0x65, 0x20, 0x32, 0x2e, 0x30, 0x30, 0x0d, 0x0a, 0x1a, 0x4a, 0x47, 0x00, 0x00]
    
    'Microsoft C/C++ MSF 7.00\r\n\x1aDS\x00\x00\x00'
    [0x4d, 0x69, 0x63, 0x72, 0x6f, 0x73, 0x6f, 0x66, 0x74, 0x20, 0x43, 0x2f, 0x43, 0x2b, 0x2b, 0x20, 0x4d, 0x53, 0x46, 0x20, 0x37, 0x2e, 0x30, 0x30, 0x0d, 0x0a, 0x1a, 0x44, 0x53, 0x00, 0x00, 0x00]
    """
    def __init__(self, _io, _parent=None, _root=None):
        super(Msf, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self
        self._read()

    def _read(self):
        self.magic = Msf.Magic(self._io, self, self._root)
        if  ((self.magic.is_small_msf) and (self.magic.small_msf_version == 2)) :
            pass
            self.small_superblock = Msf.SmallSuperblockV2Contents(self._io, self, self._root)

        if self.magic.is_big_msf:
            pass
            self.big_superblock = Msf.BigSuperblockContents(self._io, self, self._root)



    def _fetch_instances(self):
        pass
        self.magic._fetch_instances()
        if  ((self.magic.is_small_msf) and (self.magic.small_msf_version == 2)) :
            pass
            self.small_superblock._fetch_instances()

        if self.magic.is_big_msf:
            pass
            self.big_superblock._fetch_instances()


    class BigMsfStreamDirectory(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(Msf.BigMsfStreamDirectory, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.num_streams = self._io.read_u4le()
            self.stream_sizes = []
            for i in range(self.num_streams):
                self.stream_sizes.append(self._io.read_u4le())

            self.stream_blocks = []
            i = 0
            while not self._io.is_eof():
                self.stream_blocks.append(self._io.read_u4le())
                i += 1



        def _fetch_instances(self):
            pass
            for i in range(len(self.stream_sizes)):
                pass

            for i in range(len(self.stream_blocks)):
                pass



    class BigMsfStreamDirectoryPages(KaitaiStruct):
        def __init__(self, count_items, _io, _parent=None, _root=None):
            super(Msf.BigMsfStreamDirectoryPages, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self.count_items = count_items
            self._read()

        def _read(self):
            self.pages = []
            for i in range(self.count_items):
                self.pages.append(self._io.read_u4le())



        def _fetch_instances(self):
            pass
            for i in range(len(self.pages)):
                pass



    class BigSuperblockContents(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(Msf.BigSuperblockContents, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.block_size = self._io.read_u4le()
            if not  ((self.block_size == 512) or (self.block_size == 1024) or (self.block_size == 2048) or (self.block_size == 4096)) :
                raise kaitaistruct.ValidationNotAnyOfError(self.block_size, self._io, u"/types/big_superblock_contents/seq/0")
            self.free_block_map_block = self._io.read_u4le()
            if not  ((self.free_block_map_block == 1) or (self.free_block_map_block == 2)) :
                raise kaitaistruct.ValidationNotAnyOfError(self.free_block_map_block, self._io, u"/types/big_superblock_contents/seq/1")
            self.num_blocks = self._io.read_u4le()
            self.num_directory_bytes = self._io.read_u4le()
            self.unknown = self._io.read_u4le()
            self.block_map_address = self._io.read_u4le()


        def _fetch_instances(self):
            pass


    class Magic(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(Msf.Magic, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.magic0 = self._io.read_bytes(16)
            if not self.magic0 == b"\x4D\x69\x63\x72\x6F\x73\x6F\x66\x74\x20\x43\x2F\x43\x2B\x2B\x20":
                raise kaitaistruct.ValidationNotEqualError(b"\x4D\x69\x63\x72\x6F\x73\x6F\x66\x74\x20\x43\x2F\x43\x2B\x2B\x20", self.magic0, self._io, u"/types/magic/seq/0")
            self.magic1 = self._io.read_u1()
            if not  ((self.magic1 == 77) or (self.magic1 == 112)) :
                raise kaitaistruct.ValidationNotAnyOfError(self.magic1, self._io, u"/types/magic/seq/1")
            if self.is_small_msf:
                pass
                self.magic2_small = self._io.read_bytes(16)
                if not self.magic2_small == b"\x72\x6F\x67\x72\x61\x6D\x20\x64\x61\x74\x61\x62\x61\x73\x65\x20":
                    raise kaitaistruct.ValidationNotEqualError(b"\x72\x6F\x67\x72\x61\x6D\x20\x64\x61\x74\x61\x62\x61\x73\x65\x20", self.magic2_small, self._io, u"/types/magic/seq/2")

            if self.is_small_msf:
                pass
                self.magic3_small = self._io.read_u1()
                if not  ((self.magic3_small == 49) or (self.magic3_small == 50)) :
                    raise kaitaistruct.ValidationNotAnyOfError(self.magic3_small, self._io, u"/types/magic/seq/3")

            if self.is_small_msf:
                pass
                self.magic4_small = self._io.read_bytes(10)
                if not self.magic4_small == b"\x2E\x30\x30\x0D\x0A\x1A\x4A\x47\x00\x00":
                    raise kaitaistruct.ValidationNotEqualError(b"\x2E\x30\x30\x0D\x0A\x1A\x4A\x47\x00\x00", self.magic4_small, self._io, u"/types/magic/seq/4")

            if self.is_big_msf:
                pass
                self.magic2_big = self._io.read_bytes(15)
                if not self.magic2_big == b"\x53\x46\x20\x37\x2E\x30\x30\x0D\x0A\x1A\x44\x53\x00\x00\x00":
                    raise kaitaistruct.ValidationNotEqualError(b"\x53\x46\x20\x37\x2E\x30\x30\x0D\x0A\x1A\x44\x53\x00\x00\x00", self.magic2_big, self._io, u"/types/magic/seq/5")



        def _fetch_instances(self):
            pass
            if self.is_small_msf:
                pass

            if self.is_small_msf:
                pass

            if self.is_small_msf:
                pass

            if self.is_big_msf:
                pass


        @property
        def is_big_msf(self):
            if hasattr(self, '_m_is_big_msf'):
                return self._m_is_big_msf

            self._m_is_big_msf = self.magic1 == 77
            return getattr(self, '_m_is_big_msf', None)

        @property
        def is_small_msf(self):
            if hasattr(self, '_m_is_small_msf'):
                return self._m_is_small_msf

            self._m_is_small_msf = self.magic1 == 112
            return getattr(self, '_m_is_small_msf', None)

        @property
        def small_msf_version(self):
            if hasattr(self, '_m_small_msf_version'):
                return self._m_small_msf_version

            self._m_small_msf_version = (self.magic3_small - 48 if self.is_small_msf else -1)
            return getattr(self, '_m_small_msf_version', None)


    class SmallMsfStreamDirectory(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(Msf.SmallMsfStreamDirectory, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.num_streams = self._io.read_u2le()
            self.reserved = self._io.read_u2le()
            self.stream_sizes = []
            for i in range(self.num_streams):
                self.stream_sizes.append(Msf.SmallMsfStreamDirectory.StreamDirectorySize(self._io, self, self._root))

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
                super(Msf.SmallMsfStreamDirectory.StreamDirectorySize, self).__init__(_io)
                self._parent = _parent
                self._root = _root
                self._read()

            def _read(self):
                self.size = self._io.read_u4le()
                self.reserved_ptr = self._io.read_u4le()


            def _fetch_instances(self):
                pass



    class SmallSuperblockV2Contents(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(Msf.SmallSuperblockV2Contents, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
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



    @property
    def is_big_msf(self):
        if hasattr(self, '_m_is_big_msf'):
            return self._m_is_big_msf

        self._m_is_big_msf = self.magic.is_big_msf
        return getattr(self, '_m_is_big_msf', None)

    @property
    def is_small_msf(self):
        if hasattr(self, '_m_is_small_msf'):
            return self._m_is_small_msf

        self._m_is_small_msf = self.magic.is_small_msf
        return getattr(self, '_m_is_small_msf', None)

    @property
    def small_msf_version(self):
        if hasattr(self, '_m_small_msf_version'):
            return self._m_small_msf_version

        self._m_small_msf_version = self.magic.small_msf_version
        return getattr(self, '_m_small_msf_version', None)


