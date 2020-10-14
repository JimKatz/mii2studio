# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

from pkg_resources import parse_version
from kaitaistruct import __version__ as ks_version, KaitaiStruct, KaitaiStream, BytesIO


if parse_version(ks_version) < parse_version('0.7'):
    raise Exception("Incompatible Kaitai Struct Python API: 0.7 or later is required, but you have %s" % (ks_version))

class Gen3SwitchGame(KaitaiStruct):
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._read()

    def _read(self):
        self.unknown_data = [None] * (16)
        for i in range(16):
            self.unknown_data[i] = self._io.read_u1()

        self.mii_name = (self._io.read_bytes(20)).decode(u"utf-16le")
        self.unknown_buffer = [None] * (3)
        for i in range(3):
            self.unknown_buffer[i] = self._io.read_u1()

        self.favorite_color = self._io.read_u1()
        self.gender = self._io.read_u1()
        self.body_height = self._io.read_u1()
        self.body_weight = self._io.read_u1()
        self.unknown_buffer2 = [None] * (2)
        for i in range(2):
            self.unknown_buffer2[i] = self._io.read_u1()

        self.face_type = self._io.read_u1()
        self.face_color = self._io.read_u1()
        self.face_wrinkles = self._io.read_u1()
        self.face_makeup = self._io.read_u1()
        self.hair_type = self._io.read_u1()
        self.hair_color = self._io.read_u1()
        self.hair_flip = self._io.read_u1()
        self.eye_type = self._io.read_u1()
        self.eye_color = self._io.read_u1()
        self.eye_size = self._io.read_u1()
        self.eye_stretch = self._io.read_u1()
        self.eye_rotation = self._io.read_u1()
        self.eye_horizontal = self._io.read_u1()
        self.eye_vertical = self._io.read_u1()
        self.eyebrow_type = self._io.read_u1()
        self.eyebrow_color = self._io.read_u1()
        self.eyebrow_size = self._io.read_u1()
        self.eyebrow_stretch = self._io.read_u1()
        self.eyebrow_rotation = self._io.read_u1()
        self.eyebrow_horizontal = self._io.read_u1()
        self.eyebrow_vertical = self._io.read_u1()
        self.nose_type = self._io.read_u1()
        self.nose_size = self._io.read_u1()
        self.nose_vertical = self._io.read_u1()
        self.mouth_type = self._io.read_u1()
        self.mouth_color = self._io.read_u1()
        self.mouth_size = self._io.read_u1()
        self.mouth_stretch = self._io.read_u1()
        self.mouth_vertical = self._io.read_u1()
        self.facial_hair_color = self._io.read_u1()
        self.facial_hair_beard = self._io.read_u1()
        self.facial_hair_mustache = self._io.read_u1()
        self.facial_hair_size = self._io.read_u1()
        self.facial_hair_vertical = self._io.read_u1()
        self.glasses_type = self._io.read_u1()
        self.glasses_color = self._io.read_u1()
        self.glasses_size = self._io.read_u1()
        self.glasses_vertical = self._io.read_u1()
        self.mole_enable = self._io.read_u1()
        self.mole_size = self._io.read_u1()
        self.mole_horizontal = self._io.read_u1()
        self.mole_vertical = self._io.read_u1()
        self.unknown_buffer3 = [None] * (1)
        for i in range(1):
            self.unknown_buffer3[i] = self._io.read_u1()



