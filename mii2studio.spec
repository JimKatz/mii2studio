# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['mii2studio.py'],
             binaries=[],
             datas=[('gen1_wii.py', './'),
					('gen2_wiiu_3ds_miitomo.py', './'),
					('gen3_switch.py', './'),
					('gen3_switchgame.py', './')],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='mii2studio',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True)