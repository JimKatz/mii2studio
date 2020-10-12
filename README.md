# Mii-Tools

This repository contains useful tools to manipulate Miis.

## mii2studio

mii2studio is a command-line tool written in Python that can take any Mii from a Wii, 3DS, Wii U, Miitomo, or Switch and output it into a file that [Mii Studio](https://accounts.nintendo.com/mii_studio) can load. Mii Studio is an online Mii editor that was made as a successor to Miitomo.

Furthermore, the tool also outputs a link to the Mii rendered in PNG form, thanks to an API endpoint that Nintendo made (it's one of the coolest things ever). The Miis are encoded (probably due to obfuscation) and additional parameters for the API can be played with [here](https://pf2m.com/tools/mii/) (facial expressions, showing a full body, renders of multiple 360° angles of a Mii's body, etc). We use the Mii renderer for [our Check Mii Out Channel revival's companion site](https://miicontest.wii.rc24.xyz/).

Example of a rendered Mii:

![Matt](https://studio.mii.nintendo.com/miis/image.png?data=00070c5357666c76616c6971788487959e979a97979ea6adacafb6c3c9d0d59c9fa6abc6cce6e9e8eeeff3ff01090a&type=face&width=512&instanceCount=1)

### How to Install

1. First, make sure you have [Python 3](https://www.python.org/downloads/) installed.
1. Then, clone this Git repository using `git clone` or downloading a zip file of it.
1. Next, install the necessary requirements with pip: `pip install -r requirements.txt`.
1. If you're wanting to read a Mii QR code, then install zbar.

#### Installing zbar

* Windows: [Installer Link](https://sourceforge.net/projects/zbar/files/zbar/0.10/zbar-0.10-setup.exe/download)
* Mac: `brew install zbar` (make sure [Homebrew](https://brew.sh/) is installed)
* Linux: `sudo apt-get install zbar-tools`

### How to Use

Command Syntax: `python mii2studio.py <input mii file / qr code / cmoc entry number> <output studio mii file> <input type (wii/3ds/wiiu/miitomo/switch/studio/ultimate)>`

#### Examples

* Using a Mii binary file from a Wii: `python mii2studio.py /path/to/Bob.mii /path/to/Bob.studio wii`
* Using a 3DS QR Code: `python mii2studio.py "https://www.miicharacters.com/miis/qr_large/20150_bobross.jpg" /path/to/Bob.studio 3ds`
* Using a Check Mii Out Channel entry number: `python mii2studio.py 3136-3713-5980 /path/to/Bob.studio wii`

The script will output the file ready to be used in Mii Studio, along with image URLs of the Mii's face and body rendered as PNGs.

### Input Types

You can use these types of Miis with this script:

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

### List of Mii Generations

* Generation 1: Wii (and DS?)
* Generation 2: 3DS, Wii U, and [Miitomo](https://kaeru.world/projects/kaerutomo)
* Generation 3: Switch, Mii Studio, and Super Smash Bros. Ultimate

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

* bendevnull
* HEYimHeroic
* jaames for the [Mii QR decrypting script](https://gist.github.com/jaames/96ce8daa11b61b758b6b0227b55f9f78)
* Larsenv
* Matthe815
