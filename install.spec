# -*- mode: python -*-
a = Analysis(['install.py'],
             pathex=['C:\\adblock\\setup'],
             hiddenimports=[],
             hookspath=None,
             runtime_hooks=None)
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='install.exe',
          debug=False,
          strip=None,
          upx=True,
          console=True )
