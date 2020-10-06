import subprocess
import sys
from binascii import hexlify
from os import remove
from struct import pack

if len(sys.argv) < 4:
    print("Usage: python mii2studio.py <input mii file / qr code / cmoc entry number> <output studio mii file> <input type (wii/3ds/wiiu/miitomo/switch/ultimate)>")
    exit()

if sys.argv[3] == "wii":
    from gen1_wii import Gen1Wii
    try:
        if len(sys.argv[1].replace("-", "")) <= 12 and "." not in sys.argv[1]:
            print("Detected that the input is a Check Mii Out Channel entry number.")

            num = int(format(int(sys.argv[1].replace("-", "")), '032b').zfill(40)[8:], 2)
            num ^= 0x20070419
            num ^= (num >> 0x1D) ^ (num >> 0x11) ^ (num >> 0x17)
            num ^= (num & 0xF0F0F0F) << 4
            num ^= ((num << 0x1E) ^ (num << 0x12) ^ (num << 0x18)) & 0xFFFFFFFF

            import requests

            query = requests.get("https://miicontestp.wii.rc24.xyz/cgi-bin/search.cgi?entryno=" + str(num)).content

            if len(query) != 32: # 32 = empty response
                with open("temp.mii", "wb") as f:
                    f.write(query[56:130])
            else:
                print("Mii not found.")
            
            input_file = "temp.mii"
        else:
            input_file = sys.argv[1]
    except ValueError:
        input_file = sys.argv[1]
    
    orig_mii = Gen1Wii.from_file(input_file)

    if input_file == "temp.mii":
        remove("temp.mii")
elif sys.argv[3] == "3ds" or sys.argv[3] == "wiiu" or sys.argv[3] == "miitomo":
    from gen2_wiiu_3ds_miitomo import Gen2Wiiu3dsMiitomo
    from Crypto.Cipher import AES
    from shutil import which
    input_file = sys.argv[1]
    if ".png" in input_file.lower() or ".jpg" in input_file.lower() or ".jpeg" in input_file.lower(): # crappy way to detect if input is an mage
        print("Detected that the input is a Mii QR Code.")

        if which("zbarimg") is None:
            print("Error: Please install zbarimg.")
            exit()

        zbar = subprocess.Popen(["zbarimg", "--raw", "--oneshot", "-Sbinary", input_file], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        decoded_qr = zbar.communicate()[0]

        # https://gist.github.com/jaames/96ce8daa11b61b758b6b0227b55f9f78

        key = bytes([0x59, 0xFC, 0x81, 0x7E, 0x64, 0x46, 0xEA, 0x61, 0x90, 0x34, 0x7B, 0x20, 0xE9, 0xBD, 0xCE, 0x52])

        with open("temp.mii", "wb") as f:
            nonce = decoded_qr[:8]
            cipher = AES.new(key, AES.MODE_CCM, nonce + bytes([0, 0, 0, 0]))
            content = cipher.decrypt(decoded_qr[8:96])
            result = content[:12] + nonce + content[12:]
            f.write(result)

        input_file = "temp.mii"

    orig_mii = Gen2Wiiu3dsMiitomo.from_file(input_file)

    if input_file == "temp.mii":
        remove("temp.mii")
elif sys.argv[3] == "switch":
    from gen3_switch import Gen3Switch
    orig_mii = Gen3Switch.from_file(sys.argv[1])
elif sys.argv[3] == "ultimate":
    from gen3_ultimate import Gen3Ultimate
    orig_mii = Gen3Ultimate.from_file(sys.argv[1])

studio_mii = {}


def u8(data):
    return pack(">B", data)

makeup = { # lookup table
    1: 1,
    2: 6,
    3: 9,
    9: 10
}

wrinkles = { # lookup table
    4: 5,
    5: 2,
    6: 3,
    7: 7,
    8: 8,
    10: 9,
    11: 11
}

if sys.argv[3] != "switch":
    if orig_mii.facial_hair_color == 0:
        studio_mii["facial_hair_color"] = 8
    else:
        studio_mii["facial_hair_color"] = orig_mii.facial_hair_color
else:
    studio_mii["facial_hair_color"] = orig_mii.facial_hair_color
studio_mii["beard_goatee"] = orig_mii.facial_hair_beard
studio_mii["body_weight"] = orig_mii.body_weight
if sys.argv[3] == "wii":
    studio_mii["eye_stretch"] = 3
else:
    studio_mii["eye_stretch"] = orig_mii.eye_stretch
if sys.argv[3] != "switch":
    studio_mii["eye_color"] = orig_mii.eye_color + 8
else:
    studio_mii["eye_color"] = orig_mii.eye_color
studio_mii["eye_rotation"] = orig_mii.eye_rotation
studio_mii["eye_size"] = orig_mii.eye_size
studio_mii["eye_type"] = orig_mii.eye_type
studio_mii["eye_horizontal"] = orig_mii.eye_horizontal
studio_mii["eye_vertical"] = orig_mii.eye_vertical
if sys.argv[3] == "wii":
    studio_mii["eyebrow_stretch"] = 3
else:
    studio_mii["eyebrow_stretch"] = orig_mii.eyebrow_stretch
if sys.argv[3] != "switch":
    if orig_mii.eyebrow_color == 0:
        studio_mii["eyebrow_color"] = 8
    else:
        studio_mii["eyebrow_color"] = orig_mii.eyebrow_color
else:
    studio_mii["eyebrow_color"] = orig_mii.eyebrow_color
studio_mii["eyebrow_rotation"] = orig_mii.eyebrow_rotation
studio_mii["eyebrow_size"] = orig_mii.eyebrow_size
studio_mii["eyebrow_type"] = orig_mii.eyebrow_type
studio_mii["eyebrow_horizontal"] = orig_mii.eyebrow_horizontal
if sys.argv[3] != "switch":
    studio_mii["eyebrow_vertical"] = orig_mii.eyebrow_vertical
else:
    studio_mii["eyebrow_vertical"] = orig_mii.eyebrow_vertical + 3
studio_mii["face_color"] = orig_mii.face_color
if sys.argv[3] == "wii":
    if orig_mii.facial_feature in makeup:
        studio_mii["face_makeup"] = makeup[orig_mii.facial_feature]
    else:
        studio_mii["face_makeup"] = 0
else:
    studio_mii["face_makeup"] = orig_mii.face_makeup
studio_mii["face_type"] = orig_mii.face_type
if sys.argv[3] == "wii":
    if orig_mii.facial_feature in wrinkles:
        studio_mii["face_wrinkles"] = wrinkles[orig_mii.facial_feature]
    else:
        studio_mii["face_wrinkles"] = 0
else:
    studio_mii["face_wrinkles"] = orig_mii.face_wrinkles
studio_mii["favorite_color"] = orig_mii.favorite_color
studio_mii["gender"] = orig_mii.gender
if sys.argv[3] != "switch":
    if orig_mii.glasses_color == 0:
        studio_mii["glasses_color"] = 8
    elif orig_mii.glasses_color < 6:
        studio_mii["glasses_color"] = orig_mii.glasses_color + 13
    else:
        studio_mii["glasses_color"] = 0
else:
    studio_mii["glasses_color"] = orig_mii.glasses_color
studio_mii["glasses_size"] = orig_mii.glasses_size
studio_mii["glasses_type"] = orig_mii.glasses_type
studio_mii["glasses_vertical"] = orig_mii.glasses_vertical
if sys.argv[3] != "switch":
    if orig_mii.hair_color == 0:
        studio_mii["hair_color"] = 8
    else:
        studio_mii["hair_color"] = orig_mii.hair_color
else:
    studio_mii["hair_color"] = orig_mii.hair_color
studio_mii["hair_flip"] = orig_mii.hair_flip
studio_mii["hair_type"] = orig_mii.hair_type
studio_mii["body_height"] = orig_mii.body_height
studio_mii["mole_size"] = orig_mii.mole_size
studio_mii["mole_enable"] = orig_mii.mole_enable
studio_mii["mole_horizontal"] = orig_mii.mole_horizontal
studio_mii["mole_vertical"] = orig_mii.mole_vertical
if sys.argv[3] == "wii":
    studio_mii["mouth_stretch"] = 3
else:
    studio_mii["mouth_stretch"] = orig_mii.mouth_stretch
if sys.argv[3] != "switch":
    if orig_mii.mouth_color < 4:
        studio_mii["mouth_color"] = orig_mii.mouth_color + 19
    else:
        studio_mii["mouth_color"] = 0
else:
    studio_mii["mouth_color"] = orig_mii.mouth_color
studio_mii["mouth_size"] = orig_mii.mouth_size
studio_mii["mouth_type"] = orig_mii.mouth_type
studio_mii["mouth_vertical"] = orig_mii.mouth_vertical
studio_mii["beard_size"] = orig_mii.facial_hair_size
studio_mii["beard_mustache"] = orig_mii.facial_hair_mustache
studio_mii["beard_vertical"] = orig_mii.facial_hair_vertical
studio_mii["nose_size"] = orig_mii.nose_size
studio_mii["nose_type"] = orig_mii.nose_type
studio_mii["nose_vertical"] = orig_mii.nose_vertical

with open(sys.argv[2], "wb") as f:
    mii_data = b""
    n = r = 256
    mii_data += hexlify(u8(0))
    for v in studio_mii.values():
        eo = (7 + (v ^ n)) % 256 # encode the Mii, Nintendo seemed to have randomized the encoding using Math.random() in JS, but we removed randomizing
        n = eo
        mii_data += hexlify(u8(eo))
        f.write(u8(v))

    f.close()

    print("Mii Render URL: https://studio.mii.nintendo.com/miis/image.png?data=" + mii_data.decode("utf-8") + "&type=face&width=512&instanceCount=1")
