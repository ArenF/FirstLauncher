from setuptools import setup
import py2exe
import os

def get_cefpython_path():
    import cefpython3 as cefpython
    path = os.path.dirname(cefpython.__file__)
    return "%s%s" % (path, os.sep)

def get_data_files():
    cefp = get_cefpython_path()
    data_files = [('', [
          '%s/icudt.dll' % cefp,
          '%s/d3dcompiler_43.dll' % cefp,
          '%s/d3dx9_43.dll' % cefp,
          '%s/devtools_resources.pak' % cefp,
          '%s/ffmpegsumo.dll' % cefp,
          '%s/libEGL.dll' % cefp,
          '%s/libGLESv2.dll' % cefp,
          '%s/Microsoft.VC90.CRT.manifest' % cefp,
          '%s/msvcm90.dll' % cefp,
          '%s/msvcp90.dll' % cefp,
          '%s/msvcr90.dll' % cefp,
          'icon.ico', 'cefsimple.html', 'client', 'html', 'blob_storage', 'webrtc_event_logs']),
        ('locales', ['%s/locales/en-US.pak' % cefp]),
        ]
    return data_files

setup(
    data_files = get_data_files(),
    windows=['cefsimple.py'],
    options={
        "py2exe": {
            "includes": ["json", "urllib"]
        }
    }
)