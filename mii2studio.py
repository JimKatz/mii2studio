import subprocess
import sys
from binascii import hexlify
from os import remove
from requests import get, post
from struct import pack

print("mii2studio by Larsenv\n")

if len(sys.argv) < 4:
    print("CLI Usage: python mii2studio.py <input mii file / qr code / cmoc entry number> <output studio mii file> <input type (wii/3ds/wiiu/miitomo/switch/switchgame/studio)>\n")
    input_file = input("Enter the path to the input file (binary file or QR Code), a CMOC entry number, or a URL to a QR Code: ")
    output_file = input("Enter the path to the output file (which will be importable with Mii Studio): ")
    input_type = input("Enter the input type (wii/3ds/wiiu/miitomo/switch/switchgame/studio): ")
    print("")
else:
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    input_type = sys.argv[3]

if input_type == "wii":
    from gen1_wii import Gen1Wii
    try:
        if len(input_file.replace("-", "")) <= 12 and "." not in input_file:
            print("Detected that the input is a Check Mii Out Channel entry number.\n")

            num = int(format(int(input_file.replace("-", "")), '032b').zfill(40)[8:], 2) # the cmoc entry numbr is scrambled using a lot of bitwise operations
            num ^= 0x20070419
            num ^= (num >> 0x1D) ^ (num >> 0x11) ^ (num >> 0x17)
            num ^= (num & 0xF0F0F0F) << 4
            num ^= ((num << 0x1E) ^ (num << 0x12) ^ (num << 0x18)) & 0xFFFFFFFF

            query = get("https://miicontestp.wii.rc24.xyz/cgi-bin/search.cgi?entryno=" + str(num)).content

            if len(query) != 32: # 32 = empty response
                with open("temp.mii", "wb") as f:
                    f.write(query[56:130]) # cut the Mii out of the file
            else:
                print("Mii not found.")
            
            input_file = "temp.mii"
        else:
            input_file = input_file
    except ValueError:
        input_file = input_file
    
    orig_mii = Gen1Wii.from_file(input_file)

    if input_file == "temp.mii":
        try:
            remove("temp.mii")
        except PermissionError:
            print("Unable to remove temporary file.")
elif input_type == "3ds" or input_type == "wiiu" or input_type == "miitomo":
    from gen2_wiiu_3ds_miitomo import Gen2Wiiu3dsMiitomo
    from Crypto.Cipher import AES
    if ".png" in input_file.lower() or ".jpg" in input_file.lower() or ".jpeg" in input_file.lower(): # crappy way to detect if input is an mage
        if "http" in input_file.lower():
            print("Detected that the input is a URL to a Mii QR Code.\n")

            with open("temp", "wb") as f:
                f.write(get(input_file).content)
                f.close()
            
            input_file = "temp"
        else:
            print("Detected that the input is a Mii QR Code.\n")

        with open(input_file, "rb") as f:
            read = f.read()
            decoded_qr = post("https://qrcode.rc24.xyz/qrcode.php", {"image": read}).content # zbar sucks to run on a client so we use this api

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
        try:
            remove("temp.mii")
        except PermissionError:
            print("Unable to remove temporary file.")
elif input_type == "switch":
    from gen3_switch import Gen3Switch
    orig_mii = Gen3Switch.from_file(input_file)
elif input_type == "switchgame":
    from gen3_switchgame import Gen3Switchgame
    orig_mii = Gen3Switchgame.from_file(sys.argv[1])
else:
    print("Error: Invalid input type.")
    exit()

def u8(data):
    return pack(">B", data)

if input_type != "studio":
    print("Mii Info:\n")
    
    print("Mii Name: " + orig_mii.mii_name)
    
    if "switch" not in input_type:
        if orig_mii.creator_name != "\0" * 10:
            print("Creator Name: " + orig_mii.creator_name)
        if orig_mii.birth_month != 0 and orig_mii.birth_day != 0:
            print("Birthday: " + str(orig_mii.birth_month).zfill(2) +
                  "/" + str(orig_mii.birth_day).zfill(2) + " (MM/DD)")

    favorite_colors = {
        0: "Red",
        1: "Orange",
        2: "Yellow",
        3: "Light Green",
        4: "Green",
        5: "Blue",
        6: "Light Blue",
        7: "Pink",
        8: "Purple",
        9: "Brown",
        10: "White",
        11: "Black"
    }

    print("Favorite Color: " + favorite_colors[orig_mii.favorite_color])
    
    print("Body Height: " + str(orig_mii.body_height) + "%")
    print("Body Weight: " + str(orig_mii.body_weight) + "%")

    mii_types = {
        0x00: "Special Mii - Gold Pants",
        0x20: "Normal Mii - Black Pants",
        0x40: "Special Mii - Gold Pants",
        0x60: "Normal Mii - Black Pants",
        0xC0: "Foreign Mii - Blue Pants (uneditable)",
        0xE0: "Normal Mii - Black Pants",
        0x100: "???"
    }
    
    if "switch" not in input_type:
        mii_type = ""
        i = ""

        for k,v in mii_types.items():
            if k >= orig_mii.avatar_id[0]:
                mii_type = i
                break
            i = v

        print("Mii Type: " + mii_type)
        
    if input_type == "wii" or "switch" in input_type:
        print("Gender: Male" if orig_mii.gender == 0 else "Gender: Female")
    else:
        print("Gender: Male" if orig_mii.gender == 1 else "Gender: Female")

    if "switch" not in input_type:
        print("Mingle: Yes" if orig_mii.mingle == 1 else "Mingle: No")
    
    if "switch" not in input_type and input_type != "wii":
        print("Copying: Yes" if orig_mii.copying == 1 else "Copying: No")

    if input_type == "wii":
        print("Downloaded from CMOC: Yes" if orig_mii.downloaded == 1 else "Downloaded from CMOC: No")

    print("")

    studio_mii = {}

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

    # ue generate the Mii Studio file by reading each Mii format from the Kaitai files.
    # unlike consoles which store Mii data in an odd number of bits,
    # all the Mii data for a Mii Studio Mii is stored as unsigned 8-bit integers. makes it easier.

    if "switch" not in input_type:
        if orig_mii.facial_hair_color == 0:
            studio_mii["facial_hair_color"] = 8
        else:
            studio_mii["facial_hair_color"] = orig_mii.facial_hair_color
    else:
        studio_mii["facial_hair_color"] = orig_mii.facial_hair_color
    studio_mii["beard_goatee"] = orig_mii.facial_hair_beard
    studio_mii["body_weight"] = orig_mii.body_weight
    if input_type == "wii":
        studio_mii["eye_stretch"] = 3
    else:
        studio_mii["eye_stretch"] = orig_mii.eye_stretch
    if "switch" not in input_type:
        studio_mii["eye_color"] = orig_mii.eye_color + 8
    else:
        studio_mii["eye_color"] = orig_mii.eye_color
    studio_mii["eye_rotation"] = orig_mii.eye_rotation
    studio_mii["eye_size"] = orig_mii.eye_size
    studio_mii["eye_type"] = orig_mii.eye_type
    studio_mii["eye_horizontal"] = orig_mii.eye_horizontal
    studio_mii["eye_vertical"] = orig_mii.eye_vertical
    if input_type == "wii":
        studio_mii["eyebrow_stretch"] = 3
    else:
        studio_mii["eyebrow_stretch"] = orig_mii.eyebrow_stretch
    if "switch" not in input_type:
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
    if input_type != "switch":
        studio_mii["eyebrow_vertical"] = orig_mii.eyebrow_vertical
    else:
        studio_mii["eyebrow_vertical"] = orig_mii.eyebrow_vertical + 3
    studio_mii["face_color"] = orig_mii.face_color
    if input_type == "wii":
        if orig_mii.facial_feature in makeup:
            studio_mii["face_makeup"] = makeup[orig_mii.facial_feature]
        else:
            studio_mii["face_makeup"] = 0
    else:
        studio_mii["face_makeup"] = orig_mii.face_makeup
    studio_mii["face_type"] = orig_mii.face_type
    if input_type == "wii":
        if orig_mii.facial_feature in wrinkles:
            studio_mii["face_wrinkles"] = wrinkles[orig_mii.facial_feature]
        else:
            studio_mii["face_wrinkles"] = 0
    else:
        studio_mii["face_wrinkles"] = orig_mii.face_wrinkles
    studio_mii["favorite_color"] = orig_mii.favorite_color
    if input_type == "wii" or "switch" in input_type:
        studio_mii["gender"] = 0 if orig_mii.gender == 0 else 1
    else:
        studio_mii["gender"] = 1 if orig_mii.gender == 0 else 0
    if "switch" not in input_type:
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
    if "switch" not in input_type:
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
    if input_type == "wii":
        studio_mii["mouth_stretch"] = 3
    else:
        studio_mii["mouth_stretch"] = orig_mii.mouth_stretch
    if "switch" not in input_type:
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

with open(output_file, "wb") as f:
    mii_data = b""
    n = r = 256
    mii_dict = []
    if input_type == "studio":
        with open(input_file, "rb") as g:
            read = g.read()
            g.close()
        
        for i in range(0, len(hexlify(read)), 2):
            mii_dict.append(int(hexlify(read)[i:i+2], 16))
    else:
        mii_dict = studio_mii.values()
    mii_data += hexlify(u8(0))
    for v in mii_dict:
        eo = (7 + (v ^ n)) % 254 # encode the Mii, Nintendo seemed to have randomized the encoding using Math.random() in JS, but we removed randomizing
        n = eo
        mii_data += hexlify(u8(eo))
        f.write(u8(v))

    f.close()

    url = "https://studio.mii.nintendo.com/miis/image.png?data=" + mii_data.decode("utf-8")

    print("Mii Render URLs:\n")
    print("Face: " + url + "&type=face&width=512&instanceCount=1")
    print("Body: " + url + "&type=all_body&width=512&instanceCount=1")
    print("Face (16x): " + url + "&type=face&width=512&instanceCount=16")
    print("Body (16x): " + url + "&type=all_body&width=512&instanceCount=16\n")

    print("Mii Studio file written to " + output_file + ".\n")

    print("Completed Successfully")
