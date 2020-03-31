# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['auto_accept.py'],
             pathex=['venv\\\\Lib\\\\site-packages', 'T:\\Desktop\\Practicas\\Lol-auto-accept'],
             binaries=[],
             datas=[('sample.png', '.'),('sample-accepted.png', '.'), ('emote-icon.png', '.'), ('flash-icon.png', '.'), ('play-button.png', '.')],
             hiddenimports=['pkg_resources.py2_warn'],
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
          [],
          exclude_binaries=True,
          name='auto_accept',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='auto_accept')
