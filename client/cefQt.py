from cefpython3 import cefpython as cef
import os
import platform
import sys
import ctypes
import shutil
import client.minecraft as minecraft 

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

WindowUtils = cef.WindowUtils()
abspath = 'file://' + str(os.path.abspath('./')) + '\html\main.html'

WIDTH = 800
HEIGHT = 600

CefWidgetParent = QWidget

WINDOWS = (platform.system() == "Windows")
LINUX = (platform.system() == "Linux")
MAC = (platform.system() == "Darwin")

def main():
    check_versions()
    sys.excepthook = cef.ExceptHook
    settings = {}
    if MAC:
        settings["external_message_pump"] = True
    
    cef.Initialize(settings)
    app = CefApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    main_window.activateWindow()
    main_window.raise_()
    app.exec_()
    if not cef.GetAppSetting("external_message_pump"):
        app.stopTimer()
    del main_window
    del app
    cef.Shutdown()
    
    
def check_versions():
    print("[qt.py] CEF Python {ver}".format(ver=cef.__version__))
    print("[qt.py] Python {ver} {arch}".format(
            ver=platform.python_version(), arch=platform.architecture()[0]))
    print("[qt.py] PyQt {v1} (qt {v2})".format(
              v1=PYQT_VERSION_STR, v2=qVersion()))
    # CEF Python version requirement
    assert cef.__version__ >= "55.4", "CEF Python v55.4+ required to run this"

class MainWindow(QMainWindow):  
    def __init__(self):
        super(MainWindow, self).__init__()
        self.cef_widget = None
        self.setWindowTitle("PyQt5 example")
        self.setupLayout(abspath)
        self.setAcceptDrops(True)
        
    def get_browser(self):
        return self.cef_widget.browser
        
    def setupLayout(self, url):
        self.resize(WIDTH, HEIGHT)
        self.cef_widget = CefWidget(self)
        layout = QGridLayout()
        layout.addWidget(self.cef_widget, 1, 0)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        layout.setRowStretch(0, 0)
        layout.setRowStretch(1, 1)

        frame = QFrame()
        frame.setLayout(layout)
        self.setCentralWidget(frame)
        if WINDOWS:
            self.show()
        self.cef_widget.embedBrowser(url)
        
        if LINUX:
            self.container = QWidget.createWindowContainer(
                self.cef_widget.hidden_window, parent=self)
            layout.addWidget(self.container, 0, 0)
        
    def closeEvent(self, event):
        if self.cef_widget.browser:
            self.cef_widget.browser.CloseBrowser(True)
            self.clear_browser_references()
            
    def clear_browser_references(self):
        self.cef_widget.browser = None

class CefWidget(CefWidgetParent):
    def __init__(self, parent=None):
        super(CefWidget, self).__init__(parent)
        self.parent = parent
        self.browser = None
        self.hidden_window = None
        self.show()
    
    def embedBrowser(self, url):
        if LINUX:
            self.hidden_window = QWindow()
        window_info = cef.WindowInfo()
        rect = [0, 0, self.width(), self.height()]
        window_info.SetAsChild(self.getHandle(), rect)
        self.browser = cef.CreateBrowserSync(window_info, 
                                             url=url)
        

    def getHandle(self):
        if self.hidden_window:
            return int(self.hidden_window.winId())
        try:
            return int(self.winId())
        except:
            ctypes.pythonapi.PyCapsule_GetPointer.restype = (
                ctypes.c_void_p)
            ctypes.pythonapi.PyCapsule_GetPointer.argtypes = (
                [ctypes.py_object])
            return ctypes.pythonapi.PyCapsule_GetPointer(
                self.winId(), None)
    
    def moveEvent(self, _):
        self.x = 0
        self.y = 0
        if self.browser:
            if WINDOWS:
                WindowUtils.OnSize(self.getHandle(), 0, 0, 0)
            elif LINUX:
                self.browser.SetBounds(self.x, self.y, self.width(), self.height())
            self.browser.NotifyMoveOrResizeStarted()
    
    def resizeEvent(self, event):
        size = event.size()
        if self.browser:
            if WINDOWS:
                WindowUtils.OnSize(self.getHandle(), 0, 0, 0)
            elif LINUX:
                self.browser.SetBounds(self.x, self.y, size.width(), size.height())
            self.browser.NotifyMoveOrResizeStarted()
            
    def dragEnterEvent(self, event) -> None:
        print("Entering!")
        dropPath = 'file:///' + str(os.path.abspath('./')) + '/html/mod.html'
        dropPath = dropPath.replace('\\', '/')
        if self.cef_widget.browser.GetUrl() == dropPath:
            print("It works")
            if event.mimeData().hasUrls():
                # print([u.toLocalFile() for u in event.mimeData().urls()])
                event.accept()
            else:
                event.ignore()
        else:
            event.ignore()
            print(dropPath)
            print(self.cef_widget.browser.GetUrl())
    
    
    def dropEvent(self, event) -> None:
        files = [u.toLocalFile() for u in event.mimeData().urls()]
        for f in files:
            print("drop has Activated")
            # shutil.move(src=f, 
            #             dst=str(minecraft.get_minecraft_dir() + "/mods/"))
            

class CefApplication(QApplication):
    def __init__(self, args) -> None:
        super(CefApplication, self).__init__(args)
        if not cef.GetAppSetting("external_message_pump"):
            self.timer = self.createTimer()
        self.setupIcon()

    def createTimer(self):
        timer = QTimer()
        timer.timeout.connect(self.OnTimer)
        timer.start(10)
        return timer
    
    def OnTimer(self):
        cef.MessageLoopWork()

    def stopTimer(self):
        self.timer.stop()
    
    def setupIcon(self):
        icon_file = os.path.join(os.path.abspath(os.path.dirname(__file__)),
                                 "../html/resource/icon.png")
        if os.path.exists(icon_file):
            self.setWindowIcon(QIcon(icon_file))
            


        
if __name__ == "__main__":
    main()