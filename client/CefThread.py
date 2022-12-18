from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

import client.minecraft as minecraft

class LaunchThread(QThread):
    
    def __init__(self, parent, minecraft_dir, version) -> None:
        super().__init__(parent)
        self.parent = parent
        self.launcher = minecraft.Launcher(
            minecraft_dir=minecraft_dir, version=version)

    def run(self):
        self.launcher.launch()
        
class ForgeThread(QThread):
    
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.parent = parent
        self.forge = minecraft.Forge()
        self.version = None
    
    def set_version(self, version):
        self.version = version
        
    def run(self):
        self.forge.generate_forge_version(self.version)
        
class FabricThread(QThread):
    
    def __init__(self, parent, version):
        super().__init__(parent)
        self.parent = parent
        self.fabric = minecraft.Fabric()
        self.version = version
        
    def run(self):
        self.fabric.generate_fabric_version(self.version)
        
class VanillaThread(QThread):
    
    def __init__(self, parent, version):
        super().__init__(parent)
        self.parent = parent
        self.VC = minecraft.VersionControl()
        self.version = version
        
    def run(self):
        self.VC.generate_version(self.version)