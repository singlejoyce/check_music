# -*- mode: python -*-

block_cipher = None


a = Analysis(['mainui.py'],
             pathex=['checkmusic.py', 'configreader.py', 'logger.py', 'D:\\mywork\\check_music'],
             binaries=[],
             datas=[],
             hiddenimports=['checkmusic', 'configreader', 'logger'],
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
          name='mainui',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True , icon='music.ico')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='mainui')
