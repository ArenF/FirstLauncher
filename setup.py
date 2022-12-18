#setup.py

import os

from distutils.sysconfig import get_python_lib
from os.path import join
from glob import glob
from cx_Freeze import setup, Executable

# Basically just copy all of the CEF distribution into the installer
# I have only tested this on windows
cefPath = join(get_python_lib(), "cefpython3")
CEF_INCLUDES = glob(join(cefPath, "*"))
CEF_INCLUDES.remove(join(cefPath, "examples"))

setup(
    name = "First Launcher",
    version = "1.0.0",
    author = "ALLEN",
    options = {
        "build_exe": {
        'packages': ["os","sys","ctypes","win32con", "json", "platform", "threading", "minecraft_launcher_lib", "PyQt5"],
        'include_files': CEF_INCLUDES + [('html')],
        'include_msvcr': True,
    }},
    executables = [Executable('main.py')]
) 