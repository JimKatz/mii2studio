# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

from pkg_resources import parse_version
import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO


if parse_version(kaitaistruct.__version__) < parse_version('0.9'):
    raise Exception("Incompatible Kaitai Struct Python API: 0.9 or later is required, but you have %s" % (
        kaitaistruct.__version__))


class Gen3Studio(KaitaiStruct):
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._read()

    def _read(self):
        self.facial_hair_color = self._io.read_u1()
        self.beard_goatee = self._io.read_u1()
        self.body_weight = self._io.read_u1()
        self.eye_stretch = self._io.read_u1()
        self.eye_color = self._io.read_u1()
        self.eye_rotation = self._io.read_u1()
        self.eye_size = self._io.read_u1()
        self.eye_type = self._io.read_u1()
        self.eye_horizontal = self._io.read_u1()
        self.eye_vertical = self._io.read_u1()
        self.eyebrow_stretch = self._io.read_u1()
        self.eyebrow_color = self._io.read_u1()
        self.eyebrow_rotation = self._io.read_u1()
        self.eyebrow_size = self._io.read_u1()
        self.eyebrow_type = self._io.read_u1()
        self.eyebrow_horizontal = self._io.read_u1()
        self.eyebrow_vertical = self._io.read_u1()
        self.face_color = self._io.read_u1()
        self.face_makeup = self._io.read_u1()
        self.face_type = self._io.read_u1()
        self.face_wrinkles = self._io.read_u1()
        self.favorite_color = self._io.read_u1()
        self.gender = self._io.read_u1()
        self.glasses_color = self._io.read_u1()
        self.glasses_size = self._io.read_u1()
        self.glasses_type = self._io.read_u1()
        self.glasses_vertical = self._io.read_u1()
        self.hair_color = self._io.read_u1()
        self.hair_flip = self._io.read_u1()
        self.hair_type = self._io.read_u1()
        self.body_height = self._io.read_u1()
        self.mole_size = self._io.read_u1()
        self.mole_enable = self._io.read_u1()
        self.mole_horizontal = self._io.read_u1()
        self.mole_vertical = self._io.read_u1()
        self.mouth_stretch = self._io.read_u1()
        self.mouth_color = self._io.read_u1()
        self.mouth_size = self._io.read_u1()
        self.mouth_type = self._io.read_u1()
        self.mouth_vertical = self._io.read_u1()
        self.beard_size = self._io.read_u1()
        self.beard_mustache = self._io.read_u1()
        self.beard_vertical = self._io.read_u1()
        self.nose_size = self._io.read_u1()
        self.nose_type = self._io.read_u1()
        self.nose_vertical = self._io.read_u1()
