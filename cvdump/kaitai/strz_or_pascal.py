# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
from cvdump.kaitai import pascal_string


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class StrzOrPascal(KaitaiStruct):
    def __init__(self, is_strz, _io, _parent=None, _root=None):
        super(StrzOrPascal, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self
        self.is_strz = is_strz
        self._read()

    def _read(self):
        if self.is_strz:
            pass
            self.text_strz = (self._io.read_bytes_term(0, False, True, True)).decode(u"ASCII")

        if (not (self.is_strz)):
            pass
            self.text_pascal = pascal_string.PascalString(self._io)



    def _fetch_instances(self):
        pass
        if self.is_strz:
            pass

        if (not (self.is_strz)):
            pass
            self.text_pascal._fetch_instances()


    @property
    def text(self):
        if hasattr(self, '_m_text'):
            return self._m_text

        self._m_text = (self.text_strz if self.is_strz else self.text_pascal.text)
        return getattr(self, '_m_text', None)


