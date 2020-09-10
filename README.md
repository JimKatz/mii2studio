# Mii-Tools

This repository contains useful tools to manipulate Miis.

## mii2studio

mii2studio is a tool that can take any Mii from any generation and output it into a file that [Mii Studio](https://accounts.nintendo.com/mii_studio) can load. Mii Studio is an online Mii editor that was made as a successor to Miitomo.

Furthermore, the tool also outputs a link to the Mii rendered in PNG form, thanks to an API endpoint that Nintendo made (it's one of the coolest things ever). The Miis are encoded (probably due to obfuscation) and additional parameters for the API can be played with [here](https://pf2m.com/tools/mii/) (facial expressions, showing a full body, renders of multiple 360° angles of a Mii's body, etc). We use the Mii renderer for [our Check Mii Out Channel revival's companion site](https://miicontest.wii.rc24.xyz/). mii2studio can also read QR codes.

Usage: `python mii2studio.py <input switch mii file> <output studio mii file> <type (switch/wii/3ds/wiiu/miitomo)>`

### List of Mii Generations

* Generation 1: Wii (and DS?)
* Generation 2: 3DS, Wii U, and [Miitomo](https://kaeru.world/projects/kaerutomo)
* Generation 3: Switch

## Kaitai Files

[Kaitai](https://kaitai.io/) is an incredibly useful tool that can document file structures and read them. We use them to document the Mii file structures, and are used in mii2studio. The .ksy file is in the Kaitai language, and the .py is used at runtime for Python scripts (and can be compiled with [Kaitai's IDE](https://ide.kaitai.io/)).

## Credits

* bendevnull
* HEYimHeroic
* Larsenv
* Matthe815