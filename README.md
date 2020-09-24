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

## Importing/Exporting to Mii Studio

It's possible to import or export a Mii from Mii Studio. To do that, please follow these steps.

1. Add [Mii Studio Import/Export](javascript:(function () {var s = document.createElement('script');s.setAttribute('src', 'https://riiconnect24.github.io/Mii-Tools/miistudio.js');document.body.appendChild(s);}());) to your bookmarks.
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
* Larsenv
* Matthe815