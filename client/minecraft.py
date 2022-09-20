from ensurepip import version
import json
import subprocess
import threading
from typing import Any, List
import minecraft_launcher_lib
import os

minecraft_dir = minecraft_launcher_lib.utils.get_minecraft_directory()

def get_mod_files():
    try:
        path = minecraft_dir + '\mods'
        return os.listdir(path)
    except:
        print("Error: we cannot find any path to get mod file")

    
class ProgressBar():
    
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            print("__new__ is called\n")
            cls._instance = super().__new__(cls)
            
        return cls._instance
    
    def __init__(self) -> None:
        pass
        
    def set_browser(self, browser):
        self.browser = browser
        self.current_max = 0
        
    def get_browser(self):
        return self.browser
    
    def get_callbacks(self):
        self.callbacks = {
            "setStatus": self.set_status,
            "setProgress": self.set_progress,
            "setMax": self.set_max
        }
        return self.callbacks
        
    def set_status(self, status: str):
        self.browser.ExecuteFunction('writingStatus', status)
    
    def set_progress(self, progress: int):
        pg = (progress / self.current_max) * 100
        self.browser.ExecuteFunction('setStatusProgress', pg)
    
    def set_max(self, new_max: int):
        self.current_max = new_max
    
    
    
class VersionControl:
    
    # 화면에 띄울 버전 리스트를 구함.
    def get_versions_on_release() -> List[str]:
        versions = minecraft_launcher_lib.utils.get_available_versions(minecraft_directory=minecraft_dir)
        result = []
        
        for i in versions:
            if i.get('type') == 'snapshot':
                continue
            result.append(i.get('id'))
        
        return result
        
    def get_versions_installed() -> List[str]:
        versions = minecraft_launcher_lib.utils.get_installed_versions(minecraft_directory=minecraft_dir)
        result = []

        for i in versions:
            result.append(i.get('id'))
        return result
    
    def generate_version(version):
        pgbar = ProgressBar()
        minecraft_launcher_lib.install.install_minecraft_version(
            versionid=version,  minecraft_directory=minecraft_dir,
            callback=pgbar.get_callbacks())
    
    def threading_gen_version(version:str):
        t = threading.Thread(target=VersionControl.generate_version, args=(version,))
        t.start()


class Fabric:
    
    def generate_forge_version(select_ver):
        fabric_version = minecraft_launcher_lib.fabric.install_fabric()

class Forge:
    
    def threading_forge_version(select_ver:str):
        t = threading.Thread(target=Forge.generate_forge_version, args=(select_ver,))
        t.start()
    
    def generate_forge_version(select_ver):
        forge_version = minecraft_launcher_lib.forge.find_forge_version(select_ver)
        if forge_version is None:
            print("This minecraft version is not supported by Forge.")
            return
        
        
        executable = minecraft_launcher_lib.utils.get_java_executable()
        if executable == None:
            print("Error : cannot find java executable path")
            return
    
        try:
            minecraft_launcher_lib.forge.run_forge_installer(forge_version, executable)
        except:
            print('ERROR')
            
    def get_jvm_runtimes():
        return minecraft_launcher_lib.runtime.get_jvm_runtimes()
    
    def generate_jvm_version(select_jvm_ver:str) -> None:
        jvm_versions = minecraft_launcher_lib.runtime.get_jvm_runtimes()
        
        if select_jvm_ver not in jvm_versions:
            return 
        for i in jvm_versions:
            if select_jvm_ver == i:
                minecraft_launcher_lib.install.install_jvm_runtime(jvm_version=i, minecraft_directory=minecraft_dir)        
                break
            

class Launcher():
    
    def __init__(self, minecraft_dir, version) -> None:
        self.dir = minecraft_dir
        self.version = version
        self.options = {
            "username": "",
            "uuid": "",
            "token": "",
            "enableLoggingConfig": False,
            "disableMultiplayer": False
        }
        
    def set_dir(self, dir):
        self.dir = dir
        
    def get_dir(self):
        return self.dir
        
    def set_version(self, v):
        self.version = v
        
    def get_version(self):
        return self.version
        
    def set_options(self, options:Any):
        self.options = options
        
    def get_options(self):
        return self.options
    
    def launch_with_thread(self):
        t = threading.Thread(target=self.launch, args=())
        t.start()
    
    def launch(self):
        v = self.version
        dir = self.dir
        o = self.options
        if o["token"] == "":
            print("You must set the options")
            return
        minecraft_command = minecraft_launcher_lib.command.get_minecraft_command(v, dir, o)
        subprocess.call(minecraft_command)
        

def launching(version):
    l = Launcher(minecraft_dir=minecraft_dir, version=version)
    with open("./client/data/login_data.json", 'r', encoding="utf-8") as f:
        opt = json.load(f)
        option = {
            "username": opt["name"],
            "uuid": opt["id"],
            "token": opt["access_token"],
            "enableLoggingConfig": False,
            "disableMultiplayer": False
        }
        
        l.set_options(options=option)
    l.launch_with_thread()
        
        
if __name__ == "__main__":
    # l = Launcher(minecraft_dir=minecraft_dir, version="1.12.2")
    # option = {
    #     "username": "",
    #     "uuid": "",
    #     "token": "",
    #     "enableLoggingConfig": False,
    #     "disableMultiplayer": False
    # }
    # with open("./client/data/login_data.json", 'r', encoding="utf-8") as f:
    #     opt = json.load(f)
    
    # option["username"] = opt["name"]
    # option["uuid"] = opt["id"]
    # option["token"] = opt["access_token"]
    
    # print(option)
    # l.set_options(options=option)
    # l.launch()
    result = VersionControl.get_versions_installed()

    print(result)