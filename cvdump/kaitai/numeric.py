# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class Numeric(KaitaiStruct):
    def __init__(self, _io, _parent=None, _root=None):
        super(Numeric, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self
        self._read()

    def _read(self):
        self.tag = self._io.read_u2le()
        if self.tag == 32768:
            pass
            self.char_ = self._io.read_s1()

        if self.tag == 32769:
            pass
            self.short_ = self._io.read_s2le()

        if self.tag == 32770:
            pass
            self.ushort = self._io.read_u2le()

        if self.tag == 32771:
            pass
            self.long = self._io.read_s4le()

        if self.tag == 32772:
            pass
            self.ulong = self._io.read_u4le()

        if self.tag == 32773:
            pass
            self.real32 = self._io.read_f4le()

        if self.tag == 32774:
            pass
            self.real64 = self._io.read_f8le()

        if self.tag == 32775:
            pass
            self.real80 = self._io.read_bytes(10)

        if self.tag == 32776:
            pass
            self.real128 = self._io.read_bytes(18)

        if self.tag == 32777:
            pass
            self.quadword = self._io.read_s8le()

        if self.tag == 32778:
            pass
            self.uquadword = self._io.read_u8le()

        if self.tag == 32779:
            pass
            self.real48 = self._io.read_bytes(6)

        if self.tag == 32780:
            pass
            self.complex32 = Numeric.Complex32(self._io, self, self._root)

        if self.tag == 32781:
            pass
            self.complex64 = Numeric.Complex64(self._io, self, self._root)

        if self.tag == 32782:
            pass
            self.complex80 = Numeric.Complex80(self._io, self, self._root)

        if self.tag == 32783:
            pass
            self.complex128 = Numeric.Complex128(self._io, self, self._root)

        if self.tag == 32784:
            pass
            self.varstring = Numeric.Varstring(self._io, self, self._root)

        if self.tag == 32791:
            pass
            self.octword = self._io.read_bytes(16)

        if self.tag == 32792:
            pass
            self.uoctword = self._io.read_bytes(16)

        if self.tag == 32793:
            pass
            self.decimal = Numeric.Decimal(self._io, self, self._root)

        if self.tag == 32794:
            pass
            self.date = self._io.read_f8le()

        if self.tag == 32795:
            pass
            self.utf8string = (self._io.read_bytes_term(0, False, True, True)).decode(u"UTF-8")

        if self.tag == 32796:
            pass
            self.real16 = self._io.read_bytes(2)



    def _fetch_instances(self):
        pass
        if self.tag == 32768:
            pass

        if self.tag == 32769:
            pass

        if self.tag == 32770:
            pass

        if self.tag == 32771:
            pass

        if self.tag == 32772:
            pass

        if self.tag == 32773:
            pass

        if self.tag == 32774:
            pass

        if self.tag == 32775:
            pass

        if self.tag == 32776:
            pass

        if self.tag == 32777:
            pass

        if self.tag == 32778:
            pass

        if self.tag == 32779:
            pass

        if self.tag == 32780:
            pass
            self.complex32._fetch_instances()

        if self.tag == 32781:
            pass
            self.complex64._fetch_instances()

        if self.tag == 32782:
            pass
            self.complex80._fetch_instances()

        if self.tag == 32783:
            pass
            self.complex128._fetch_instances()

        if self.tag == 32784:
            pass
            self.varstring._fetch_instances()

        if self.tag == 32791:
            pass

        if self.tag == 32792:
            pass

        if self.tag == 32793:
            pass
            self.decimal._fetch_instances()

        if self.tag == 32794:
            pass

        if self.tag == 32795:
            pass

        if self.tag == 32796:
            pass


    class Complex128(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(Numeric.Complex128, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.real = self._io.read_bytes(16)
            self.complex = self._io.read_bytes(16)


        def _fetch_instances(self):
            pass


    class Complex32(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(Numeric.Complex32, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.real = self._io.read_f4le()
            self.complex = self._io.read_f4le()


        def _fetch_instances(self):
            pass


    class Complex64(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(Numeric.Complex64, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.real = self._io.read_f8le()
            self.complex = self._io.read_f8le()


        def _fetch_instances(self):
            pass


    class Complex80(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(Numeric.Complex80, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.real = self._io.read_bytes(10)
            self.complex = self._io.read_bytes(10)


        def _fetch_instances(self):
            pass


    class Decimal(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(Numeric.Decimal, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.w_reserved = self._io.read_u2le()
            self.scale = self._io.read_u1()
            self.sign = self._io.read_u1()
            self.hi32 = self._io.read_u4le()
            self.lo64 = self._io.read_u8le()


        def _fetch_instances(self):
            pass


    class Varstring(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(Numeric.Varstring, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.len = self._io.read_u2le()
            self.text = self._io.read_bytes(self.len)


        def _fetch_instances(self):
            pass



