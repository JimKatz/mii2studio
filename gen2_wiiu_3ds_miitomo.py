# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

from pkg_resources import parse_version
import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO


if parse_version(kaitaistruct.__version__) < parse_version('0.9'):
    raise Exception("Incompatible Kaitai Struct Python API: 0.9 or later is required, but you have %s" % (
        kaitaistruct.__version__))


class Gen2Wiiu3dsMiitomo(KaitaiStruct):
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._read()

    def _read(self):
        self.unknown_1 = self._io.read_u1()
        self.character_set = self._io.read_bits_int_be(2)
        self.region_lock = self._io.read_bits_int_be(2)
        self.profanity_flag = self._io.read_bits_int_be(1) != 0
        self.copying = self._io.read_bits_int_be(1) != 0
        self.unknown_2 = self._io.read_bits_int_be(2)
        self.mii_position_slot_index = self._io.read_bits_int_be(4)
        self.mii_position_page_index = self._io.read_bits_int_be(4)
        self.version = self._io.read_bits_int_be(4)
        self.unknown_3 = self._io.read_bits_int_be(4)
        self._io.align_to_byte()
        self.system_id = [None] * (8)
        for i in range(8):
            self.system_id[i] = self._io.read_u1()

        self.avatar_id = [None] * (4)
        for i in range(4):
            self.avatar_id[i] = self._io.read_u1()

        self.client_id = [None] * (6)
        for i in range(6):
            self.client_id[i] = self._io.read_u1()

        self.padding = self._io.read_u2le()
        self.data_1 = self._io.read_u2le()
        self.mii_name = (self._io.read_bytes(20)).decode(u"utf-16le")
        self.body_height = self._io.read_u1()
        self.body_weight = self._io.read_u1()
        self.face_color = self._io.read_bits_int_be(3)
        self.face_type = self._io.read_bits_int_be(4)
        self.mingle = self._io.read_bits_int_be(1) != 0
        self.face_makeup = self._io.read_bits_int_be(4)
        self.face_wrinkles = self._io.read_bits_int_be(4)
        self._io.align_to_byte()
        self.hair_type = self._io.read_u1()
        self.unknown_5 = self._io.read_bits_int_be(4)
        self.hair_flip = self._io.read_bits_int_be(1) != 0
        self.hair_color = self._io.read_bits_int_be(3)
        self._io.align_to_byte()
        self.eye = self._io.read_u4le()
        self.eyebrow = self._io.read_u4le()
        self.nose = self._io.read_u2le()
        self.mouth = self._io.read_u2le()
        self.mouth2 = self._io.read_u2le()
        self.beard = self._io.read_u2le()
        self.glasses = self._io.read_u2le()
        self.mole = self._io.read_u2le()
        self.creator_name = (self._io.read_bytes(20)).decode(u"utf-16le")
        self.padding2 = self._io.read_u2le()
        self.checksum = self._io.read_u2le()

    @property
    def glasses_color(self):
        if hasattr(self, '_m_glasses_color'):
            return self._m_glasses_color if hasattr(self, '_m_glasses_color') else None

        self._m_glasses_color = ((self.glasses >> 4) & 7)
        return self._m_glasses_color if hasattr(self, '_m_glasses_color') else None

    @property
    def eyebrow_horizontal(self):
        if hasattr(self, '_m_eyebrow_horizontal'):
            return self._m_eyebrow_horizontal if hasattr(self, '_m_eyebrow_horizontal') else None

        self._m_eyebrow_horizontal = ((self.eyebrow >> 21) & 15)
        return self._m_eyebrow_horizontal if hasattr(self, '_m_eyebrow_horizontal') else None

    @property
    def eye_vertical(self):
        if hasattr(self, '_m_eye_vertical'):
            return self._m_eye_vertical if hasattr(self, '_m_eye_vertical') else None

        self._m_eye_vertical = ((self.eye >> 25) & 31)
        return self._m_eye_vertical if hasattr(self, '_m_eye_vertical') else None

    @property
    def facial_hair_beard(self):
        if hasattr(self, '_m_facial_hair_beard'):
            return self._m_facial_hair_beard if hasattr(self, '_m_facial_hair_beard') else None

        self._m_facial_hair_beard = (self.beard & 7)
        return self._m_facial_hair_beard if hasattr(self, '_m_facial_hair_beard') else None

    @property
    def mouth_size(self):
        if hasattr(self, '_m_mouth_size'):
            return self._m_mouth_size if hasattr(self, '_m_mouth_size') else None

        self._m_mouth_size = ((self.mouth >> 9) & 15)
        return self._m_mouth_size if hasattr(self, '_m_mouth_size') else None

    @property
    def eyebrow_stretch(self):
        if hasattr(self, '_m_eyebrow_stretch'):
            return self._m_eyebrow_stretch if hasattr(self, '_m_eyebrow_stretch') else None

        self._m_eyebrow_stretch = ((self.eyebrow >> 12) & 7)
        return self._m_eyebrow_stretch if hasattr(self, '_m_eyebrow_stretch') else None

    @property
    def nose_vertical(self):
        if hasattr(self, '_m_nose_vertical'):
            return self._m_nose_vertical if hasattr(self, '_m_nose_vertical') else None

        self._m_nose_vertical = ((self.nose >> 9) & 31)
        return self._m_nose_vertical if hasattr(self, '_m_nose_vertical') else None

    @property
    def eye_color(self):
        if hasattr(self, '_m_eye_color'):
            return self._m_eye_color if hasattr(self, '_m_eye_color') else None

        self._m_eye_color = ((self.eye >> 6) & 7)
        return self._m_eye_color if hasattr(self, '_m_eye_color') else None

    @property
    def birth_month(self):
        if hasattr(self, '_m_birth_month'):
            return self._m_birth_month if hasattr(self, '_m_birth_month') else None

        self._m_birth_month = ((self.data_1 >> 1) & 15)
        return self._m_birth_month if hasattr(self, '_m_birth_month') else None

    @property
    def mouth_color(self):
        if hasattr(self, '_m_mouth_color'):
            return self._m_mouth_color if hasattr(self, '_m_mouth_color') else None

        self._m_mouth_color = ((self.mouth >> 6) & 7)
        return self._m_mouth_color if hasattr(self, '_m_mouth_color') else None

    @property
    def mole_horizontal(self):
        if hasattr(self, '_m_mole_horizontal'):
            return self._m_mole_horizontal if hasattr(self, '_m_mole_horizontal') else None

        self._m_mole_horizontal = ((self.mole >> 5) & 31)
        return self._m_mole_horizontal if hasattr(self, '_m_mole_horizontal') else None

    @property
    def facial_hair_mustache(self):
        if hasattr(self, '_m_facial_hair_mustache'):
            return self._m_facial_hair_mustache if hasattr(self, '_m_facial_hair_mustache') else None

        self._m_facial_hair_mustache = ((self.mouth2 >> 5) & 7)
        return self._m_facial_hair_mustache if hasattr(self, '_m_facial_hair_mustache') else None

    @property
    def eyebrow_rotation(self):
        if hasattr(self, '_m_eyebrow_rotation'):
            return self._m_eyebrow_rotation if hasattr(self, '_m_eyebrow_rotation') else None

        self._m_eyebrow_rotation = ((self.eyebrow >> 16) & 15)
        return self._m_eyebrow_rotation if hasattr(self, '_m_eyebrow_rotation') else None

    @property
    def mole_vertical(self):
        if hasattr(self, '_m_mole_vertical'):
            return self._m_mole_vertical if hasattr(self, '_m_mole_vertical') else None

        self._m_mole_vertical = ((self.mole >> 10) & 31)
        return self._m_mole_vertical if hasattr(self, '_m_mole_vertical') else None

    @property
    def glasses_type(self):
        if hasattr(self, '_m_glasses_type'):
            return self._m_glasses_type if hasattr(self, '_m_glasses_type') else None

        self._m_glasses_type = (self.glasses & 15)
        return self._m_glasses_type if hasattr(self, '_m_glasses_type') else None

    @property
    def eyebrow_size(self):
        if hasattr(self, '_m_eyebrow_size'):
            return self._m_eyebrow_size if hasattr(self, '_m_eyebrow_size') else None

        self._m_eyebrow_size = ((self.eyebrow >> 8) & 15)
        return self._m_eyebrow_size if hasattr(self, '_m_eyebrow_size') else None

    @property
    def mole_size(self):
        if hasattr(self, '_m_mole_size'):
            return self._m_mole_size if hasattr(self, '_m_mole_size') else None

        self._m_mole_size = ((self.mole >> 1) & 15)
        return self._m_mole_size if hasattr(self, '_m_mole_size') else None

    @property
    def nose_size(self):
        if hasattr(self, '_m_nose_size'):
            return self._m_nose_size if hasattr(self, '_m_nose_size') else None

        self._m_nose_size = ((self.nose >> 5) & 15)
        return self._m_nose_size if hasattr(self, '_m_nose_size') else None

    @property
    def facial_hair_vertical(self):
        if hasattr(self, '_m_facial_hair_vertical'):
            return self._m_facial_hair_vertical if hasattr(self, '_m_facial_hair_vertical') else None

        self._m_facial_hair_vertical = ((self.beard >> 10) & 31)
        return self._m_facial_hair_vertical if hasattr(self, '_m_facial_hair_vertical') else None

    @property
    def eye_stretch(self):
        if hasattr(self, '_m_eye_stretch'):
            return self._m_eye_stretch if hasattr(self, '_m_eye_stretch') else None

        self._m_eye_stretch = ((self.eye >> 13) & 7)
        return self._m_eye_stretch if hasattr(self, '_m_eye_stretch') else None

    @property
    def eye_size(self):
        if hasattr(self, '_m_eye_size'):
            return self._m_eye_size if hasattr(self, '_m_eye_size') else None

        self._m_eye_size = ((self.eye >> 9) & 7)
        return self._m_eye_size if hasattr(self, '_m_eye_size') else None

    @property
    def eye_type(self):
        if hasattr(self, '_m_eye_type'):
            return self._m_eye_type if hasattr(self, '_m_eye_type') else None

        self._m_eye_type = (self.eye & 63)
        return self._m_eye_type if hasattr(self, '_m_eye_type') else None

    @property
    def eye_horizontal(self):
        if hasattr(self, '_m_eye_horizontal'):
            return self._m_eye_horizontal if hasattr(self, '_m_eye_horizontal') else None

        self._m_eye_horizontal = ((self.eye >> 21) & 15)
        return self._m_eye_horizontal if hasattr(self, '_m_eye_horizontal') else None

    @property
    def eyebrow_type(self):
        if hasattr(self, '_m_eyebrow_type'):
            return self._m_eyebrow_type if hasattr(self, '_m_eyebrow_type') else None

        self._m_eyebrow_type = (self.eyebrow & 31)
        return self._m_eyebrow_type if hasattr(self, '_m_eyebrow_type') else None

    @property
    def mouth_vertical(self):
        if hasattr(self, '_m_mouth_vertical'):
            return self._m_mouth_vertical if hasattr(self, '_m_mouth_vertical') else None

        self._m_mouth_vertical = (self.mouth2 & 31)
        return self._m_mouth_vertical if hasattr(self, '_m_mouth_vertical') else None

    @property
    def eyebrow_color(self):
        if hasattr(self, '_m_eyebrow_color'):
            return self._m_eyebrow_color if hasattr(self, '_m_eyebrow_color') else None

        self._m_eyebrow_color = ((self.eyebrow >> 5) & 7)
        return self._m_eyebrow_color if hasattr(self, '_m_eyebrow_color') else None

    @property
    def nose_type(self):
        if hasattr(self, '_m_nose_type'):
            return self._m_nose_type if hasattr(self, '_m_nose_type') else None

        self._m_nose_type = (self.nose & 31)
        return self._m_nose_type if hasattr(self, '_m_nose_type') else None

    @property
    def facial_hair_color(self):
        if hasattr(self, '_m_facial_hair_color'):
            return self._m_facial_hair_color if hasattr(self, '_m_facial_hair_color') else None

        self._m_facial_hair_color = ((self.beard >> 3) & 7)
        return self._m_facial_hair_color if hasattr(self, '_m_facial_hair_color') else None

    @property
    def eyebrow_vertical(self):
        if hasattr(self, '_m_eyebrow_vertical'):
            return self._m_eyebrow_vertical if hasattr(self, '_m_eyebrow_vertical') else None

        self._m_eyebrow_vertical = ((self.eyebrow >> 25) & 31)
        return self._m_eyebrow_vertical if hasattr(self, '_m_eyebrow_vertical') else None

    @property
    def glasses_size(self):
        if hasattr(self, '_m_glasses_size'):
            return self._m_glasses_size if hasattr(self, '_m_glasses_size') else None

        self._m_glasses_size = ((self.glasses >> 7) & 15)
        return self._m_glasses_size if hasattr(self, '_m_glasses_size') else None

    @property
    def eye_rotation(self):
        if hasattr(self, '_m_eye_rotation'):
            return self._m_eye_rotation if hasattr(self, '_m_eye_rotation') else None

        self._m_eye_rotation = ((self.eye >> 16) & 31)
        return self._m_eye_rotation if hasattr(self, '_m_eye_rotation') else None

    @property
    def gender(self):
        if hasattr(self, '_m_gender'):
            return self._m_gender if hasattr(self, '_m_gender') else None

        self._m_gender = (self.data_1 & 1)
        return self._m_gender if hasattr(self, '_m_gender') else None

    @property
    def birth_day(self):
        if hasattr(self, '_m_birth_day'):
            return self._m_birth_day if hasattr(self, '_m_birth_day') else None

        self._m_birth_day = ((self.data_1 >> 5) & 31)
        return self._m_birth_day if hasattr(self, '_m_birth_day') else None

    @property
    def mouth_stretch(self):
        if hasattr(self, '_m_mouth_stretch'):
            return self._m_mouth_stretch if hasattr(self, '_m_mouth_stretch') else None

        self._m_mouth_stretch = ((self.mouth >> 13) & 7)
        return self._m_mouth_stretch if hasattr(self, '_m_mouth_stretch') else None

    @property
    def mole_enable(self):
        if hasattr(self, '_m_mole_enable'):
            return self._m_mole_enable if hasattr(self, '_m_mole_enable') else None

        self._m_mole_enable = (self.mole >> 15)
        return self._m_mole_enable if hasattr(self, '_m_mole_enable') else None

    @property
    def favorite(self):
        if hasattr(self, '_m_favorite'):
            return self._m_favorite if hasattr(self, '_m_favorite') else None

        self._m_favorite = ((self.data_1 >> 14) & 1)
        return self._m_favorite if hasattr(self, '_m_favorite') else None

    @property
    def glasses_vertical(self):
        if hasattr(self, '_m_glasses_vertical'):
            return self._m_glasses_vertical if hasattr(self, '_m_glasses_vertical') else None

        self._m_glasses_vertical = ((self.glasses >> 11) & 15)
        return self._m_glasses_vertical if hasattr(self, '_m_glasses_vertical') else None

    @property
    def favorite_color(self):
        if hasattr(self, '_m_favorite_color'):
            return self._m_favorite_color if hasattr(self, '_m_favorite_color') else None

        self._m_favorite_color = ((self.data_1 >> 10) & 15)
        return self._m_favorite_color if hasattr(self, '_m_favorite_color') else None

    @property
    def mouth_type(self):
        if hasattr(self, '_m_mouth_type'):
            return self._m_mouth_type if hasattr(self, '_m_mouth_type') else None

        self._m_mouth_type = (self.mouth & 63)
        return self._m_mouth_type if hasattr(self, '_m_mouth_type') else None

    @property
    def facial_hair_size(self):
        if hasattr(self, '_m_facial_hair_size'):
            return self._m_facial_hair_size if hasattr(self, '_m_facial_hair_size') else None

        self._m_facial_hair_size = ((self.beard >> 6) & 15)
        return self._m_facial_hair_size if hasattr(self, '_m_facial_hair_size') else None
