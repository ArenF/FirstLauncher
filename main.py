import base64
import shutil
from subprocess import call
import tkinter
from tkinter.filedialog import askdirectory
from cefpython3 import cefpython as cef
import minecraft_launcher_lib
import platform
import sys
import os
import threading
import client.handlers as handler
import client.authorization as authorization
import client.minecraft as minecraft

def main():
    
    # reading_html = ""
    # with open("./html/main.html", "r", encoding="utf-8") as f:
    #     reading_html = f.read()
    
    abspath = 'file://' + str(os.path.abspath('./')) + '\html\main.html'
    
    check_version()
    sys.excepthook = cef.ExceptHook
    cef.Initialize()
    browser = cef.CreateBrowserSync(url=abspath, 
                                    window_title='AFTER Launcher')
    set_javascriptbindings(browser=browser)
    set_global_handlers(browser=browser)
    cef.MessageLoop()
    cef.Shutdown()
    
def check_version():
    ver = cef.GetVersion()
    print("[tutorial.py] CEF Python {ver}".format(ver=ver["version"]))
    print("[tutorial.py] Chromium {ver}".format(ver=ver["chrome_version"]))
    print("[tutorial.py] CEF {ver}".format(ver=ver["cef_version"]))
    print("[tutorial.py] Python {ver} {arch}".format(
           ver=platform.python_version(),
           arch=platform.architecture()[0]))
    assert cef.__version__ >= "57.0", "CEF Python v57.0+ required to run this"
    
class External():
    target_dir_path = ''
    def __init__(self, browser) -> None:
        self.browser = browser
        
    def has_login_data(self):
        has = authorization.has_login_data()
        self.browser.ExecuteFunction('login_page', has)
        
    def set_minecraft_versions(self, func):
        versions = minecraft.VersionControl.get_versions_on_release()
        self.browser.ExecuteFunction('call_minecraft_versions', versions, func)
    
    def set_installed_versions(self, func):
        versions = minecraft.VersionControl.get_versions_installed()
        self.browser.ExecuteFunction('call_installed_versions', versions, func)
    
    def set_mod_files(self):
        mod_files = minecraft.get_mod_files()
        self.browser.ExecuteFunction('call_mod_files', mod_files)
    
    # def move_file(self, file):
        
        
    


def set_javascriptbindings(browser):
    bindings = cef.JavascriptBindings(
        bindToFrames=False, bindToPopups=False)
    # 마크, 로그인 관련 데이터
    external = External(browser=browser)
    bindings.SetFunction("has_login_data", external.has_login_data)
    bindings.SetFunction("set_minecraft_versions", external.set_minecraft_versions)
    bindings.SetFunction("set_installed_versions", external.set_installed_versions)
    bindings.SetFunction("set_mod_files", external.set_mod_files)
    bindings.SetProperty("get_login_link", authorization.get_login())
    bindings.SetProperty("get_minecraft_dir", minecraft.get_minecraft_dir())
    # 프로그레스바 변수 설정
    pgbar = minecraft.ProgressBar()
    pgbar.set_browser(browser=browser)
    
    # 파이썬 프린팅, 포지, 바닐라 다운받기
    bindings.SetFunction("py_print", print_console)
    bindings.SetFunction("generate_forge", minecraft.Forge.threading_forge_version)
    bindings.SetFunction("generate_vanilla", minecraft.VersionControl.threading_gen_version)
    bindings.SetFunction("generate_fabric", minecraft.Fabric.threading_fabric_version)
    
    # 파이썬 마크 런칭
    bindings.SetFunction("launcher", minecraft.launching)
    
    browser.SetJavascriptBindings(bindings)

def set_global_handlers(browser):
    client_handlers = handler.get_client_handlers()
    for handlers in client_handlers:
        browser.SetClientHandler(handlers)
    
def print_console(tellraw):
    print(tellraw)

if __name__ == "__main__":
    thread = threading.Thread(target=main, args=())
    thread.start()
    thread.join()
    