import json
import subprocess
from typing import Any, List
import minecraft_launcher_lib
import os
import threading

minecraft_dir = minecraft_launcher_lib.utils.get_minecraft_directory()
mod_path = minecraft_dir + '\mods'

def get_minecraft_dir():
    return minecraft_dir

def get_mod_path():
    return mod_path
    
def get_dir_files(path):
    try:
        
        return os.listdir(path)
    except:
        print("Error: we cannot find any path to get file")
        return []    
    
    
class VersionControl():
    
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
    
    def generate_version(version:str, callbacks):
        minecraft_launcher_lib.install.install_minecraft_version(
            versionid=version,  minecraft_directory=minecraft_dir,
            callback=callbacks)
    
    def threading_version(version:str, callbacks):
        thread = threading.Thread(target=VersionControl.generate_version, args=(version, callbacks))
        thread.start()
    


class Fabric():
    
    def generate_fabric_version(select_ver, callbacks):
        try:
            
            if select_ver not in VersionControl.get_versions_installed():
                print("You should install the minecraft version first!")
                return
            minecraft_launcher_lib.fabric.install_fabric(select_ver, minecraft_dir, callback=callbacks)
        except:
            
            print("It has error occured")

class Forge():
    
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
        
