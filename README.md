# mii2studio

mii2studio is a command-line tool written in Python that can take any Mii from a Wii, 3DS, Wii U, Miitomo, or Switch and output it into a file that [Mii Studio](https://accounts.nintendo.com/mii_studio) can load. Mii Studio is an online Mii editor that was made as a successor to Miitomo.

Furthermore, the tool also outputs a link to the Mii rendered in PNG form, thanks to an API endpoint that Nintendo made (it's one of the coolest things ever). The Miis are encoded (probably due to obfuscation) and additional parameters for the API can be played with [here](https://pf2m.com/tools/mii/) (facial expressions, showing a full body, renders of multiple 360° angles of a Mii's body, etc). We use the Mii renderer for [our Check Mii Out Channel revival's companion site](https://miicontest.wii.rc24.xyz/).

Also, the tool can print out some useful information about a Mii, like its birthday, height, weight, name, gender, favorite color, pants color (which isn't a thing on the Switch and Mii Studio), and more.

Example of a rendered Mii:

![Matt](https://studio.mii.nintendo.com/miis/image.png?data=000f145b5f5e646e49546169687477858e878a87878e969d9c9fa6b3b9c0e5acafb6bbb6bcb6b9b8bebfc3cfd1d9da&type=face&width=512&instanceCount=1)

## How to Use

[Download the bundled application from here](https://github.com/RiiConnect24/mii2studio/releases/). It's a Python script embedded in a binary, for your convenience. The source files are available too if you need to use that instead for some reason.

Command Syntax: `mii2studio <input mii file / qr code / cmoc entry number> <output studio mii file> <input type (wii/3ds/wiiu/miitomo/switch/switchgame/studio)>`

The script can also be ran without parameters.

## Examples

* Using a Mii binary file from a Wii: `python mii2studio.py /path/to/BobRoss.mii /path/to/BobRoss.studio wii`
* Using a 3DS QR Code: `python mii2studio.py "https://www.miicharacters.com/miis/qr_large/20150_bobross.jpg" /path/to/Bob.studio 3ds`
* Using a Check Mii Out Channel entry number: `python mii2studio.py 3136-3713-5980 /path/to/BobRoss.studio wii`

The script will output the file ready to be used in Mii Studio, along with image URLs of the Mii's face and body rendered as PNGs, and some useful information about the Mii.

## Input Types

You can use almost every Mii format with this script:

* Mii binary files from many platforms
    * Wii
    * 3DS
    * Wii U
    * Switch
        * Mii format used in the Mii DB on the Switch NAND
        * Mii format used in save files in Switch games
    * Mii Studio (in decoded form)
* Mii QR Codes from many platforms
    * 3DS
    * Wii U
    * Miitomo
    * Tomodachi Life
    * Miitopia
* 12-digit entry numbers for Miis uploaded to RiiConnect24's Check Mii Out Channel revival

## List of Mii Generations

* Generation 1: Wii and DS
* Generation 2: 3DS, Wii U, and [Miitomo](https://kaeru.world/projects/kaerutomo)
* Generation 3: Switch and Mii Studio

## Importing/Exporting to Mii Studio

It's possible to import or export a Mii from Mii Studio. To do that, please follow these steps.

1. Add the Mii Studio Import/Export tool to your bookmarks: with the link `javascript:(function () {var s = document.createElement('script');s.setAttribute('src', 'https://riiconnect24.github.io/Mii-Tools/miistudio.js');document.body.appendChild(s);}());`
1. Go to the [Mii Studio](https://accounts.nintendo.com/mii_studio) website.

### Importing

1. Create a new Mii with Mii Studio.
1. Save the Mii (you don't need to modify it, making a default Mii is fine since we're going to import it).
1. On the Mii selection page, open the Mii that you just made.
1. If your Mii isn't in the Studio format (which is 46 bytes) and is from a console, run the Mii you would like to convert through mii2studio if you haven't already.
1. Open the Mii Studio Import/Export tool you bookmarked.  
1. Press OK on the pop-up.
1. Open the outputted Mii Studio file in a hex editor.
1. Copy and paste the bytes of the Mii into the input field, without any spaces between the bytes.
1. Refresh the page.
1. Press "Continue editing" and the imported Mii should appear.
1. Don't forget to save your Mii if you want to.

### Exporting

1. Make sure you're editing an existing Mii, not creating one.
1. Open the Mii Studio Import/Export tool you bookmarked.
1. Press Cancel on the pop-up.
1. Your exported Mii should download.

## Kaitai Files

[Kaitai](https://kaitai.io/) is an incredibly useful tool that can document file structures and read them. We use them to document the Mii file structures, and are used in mii2studio. The .ksy file is in the Kaitai language, and the .py is used at runtime for Python scripts (and can be compiled with [Kaitai's IDE](https://ide.kaitai.io/)).

## Credits

* bendevnull for his support.
* HEYimHeroic for helping in many ways, without her help we wouldn't have this tool.
* jaames for the [Mii QR decrypting script](https://gist.github.com/jaames/96ce8daa11b61b758b6b0227b55f9f78).
* Larsenv for writing this script.
* Matthe815 for figuring out the obfuscation used for the Mii Studio renderer.