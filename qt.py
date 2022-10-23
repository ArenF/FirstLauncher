from cefpython3 import cefpython as cef
import ctypes
import os
import platform
import sys

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

WindowUtils = cef.WindowUtils()

#Platforms
WINDOWS = (platform.system() == "Windows")
LINUX = (platform.system() == "Linux")
MAC = (platform.system() == "Darwin")

WIDTH = 800
HEIGHT = 600

CefWidgetParent = QWidget

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

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__(None)
        self.cef_widget = None
        self.navigation_bar = None
        self.setupLayout()
    
    def setupLayout(self):
        self.resize(WIDTH, HEIGHT)
        self.cef_widget = CefWidget(self)
        self.navigation_bar = NavigationBar(self.cef_widget)
        layout = QGridLayout()

        layout.addWidget(self.navigation_bar, 0, 0)
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
        self.cef_widget.embedBrowser()
        if LINUX:
            self.container = QWidget.createWindowContainer(
                self.cef_widget.hidden_window, parent=self
            )
            layout.addWidget(self.container, 1, 0)
    
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
        
    def foucsInEvent(self, event):
        if cef.GetAppSetting("debug"):
            print("[qt.py] CefWidget.focusInEvent")
        if self.browser:
            if WINDOWS:
                WindowUtils.OnSetFocus(self.getHandle(), 0, 0, 0)
            self.browser.setFocus(True)
    
    def focusOutEvent(self, event):
        if cef.GetAppSetting("debug"):
            print("[qt.py] CefWidget.focusOutEvent")
        if self.browser:
            self.browser.SetFocus(False)
        
    def embedBrowser(self):
        if LINUX:
            self.hidden_window = QWindow()    
        window_info = cef.WindowInfo()
        rect = [0, 0, self.width(), self.height()]
        window_info.SetAsChild(self.getHandle(), rect)
        self.browser = cef.CreateBrowserSync(window_info,
                                             url="https://www.google.com/")
        self.browser.SetClientHandler(LoadHandler(self.parent.navigation_bar))
        self.browser.SetClientHandler(FocusHandler(self))
        
    def getHandle(self):
        if self.hidden_window:
            return int(self.hidden_window.winId())
        try:
            return int(self.winId())
        except:
            print("The Python has Error.")
            
    def moveEvent(self, _):
        self.x = 0
        self.y = 0
        if self.browser:
            if WINDOWS:
                WindowUtils.OnSize(self.getHandle(), 0, 0, 0)
            elif LINUX:
                self.browser.SetBoundsa(self.x, self.y,
                                        self.width(), self.height())
            self.browser.NotifyMoveOrResizeStarted()
    
    def resizeEvent(self, event) -> None:
        size = event.size()
        if self.browser:
            if WINDOWS:
                WindowUtils.OnSize(self.getHandle(), 0, 0, 0)
            elif LINUX:
                self.browser.SetBounds(self.x, self.y,
                                       size.width(), size.height())
            self.browser.NotifyMoveOrResizeStarted()
    
class CefApplication(QApplication):
    def __init__(self, args):
        super(CefApplication, self).__init__(args)
        if not cef.GetAppSetting("external_message_pump"):
            self.timer = self.createTimer()
        self.setupIcon()
    
    def createTimer(self):
        timer = QTimer()
        timer.timeout.connect(self.onTimer)
        timer.start(10)
        return timer
    
    def onTimer(self):
        cef.MessageLoopWork()
    
    def stopTimer(self):
        self.timer.stop()
        
    def setupIcon(self):
        icon_file = os.path.join(os.path.abspath(os.path.dirname("html/resource/icon.png")),
                                 "resources",
                                 "data.png")
        if os.path.exists(icon_file):
            self.setWindowIcon(QIcon(icon_file))

    
            
class LoadHandler(object):
    def __init__(self, navigation_bar) -> None:
        self.initial_app_loading = True
        self.navigation_bar = navigation_bar
        
    def OnLoadingStateChange(self, **_):
        self.navigation_bar.updateState()
    
    def OnLoadStart(self, browser, **_):
        self.navigation_bar.url.setText(browser.GetUrl())
        if self.initial_app_loading:
            self.navigation_bar.cef_widget.setFocus()
            if LINUX:
                print("[qt.py] LoadHandler.OnLoadStart:"
                      " keyboard focus fix no. 2 (Issue #284)")
                browser.SetFocus(True)
                self.initial_app_loading = False
                
class FocusHandler(object):
    def __init__(self, cef_widget):
        self.cef_widget = cef_widget
        
    def OnTakeFocus(self, **_):
        if cef.GetAppSetting("debug"):
            print("[qt.py] FocusHandler.OnTakeFocus")

    def OnSetFocus(self, **_):
        if cef.GetAppSetting("debug"):
            print("[qt.py] FocusHandler.OnSetFocus")

    def OnGotFocus(self, browser, **_):
        if cef.GetAppSetting("debug"):
            print("[qt.py] FocusHandler.OnGotFocus")
        self.cef_widget.setFocus()
        # Temporary fix no. 1 for focus issues on Linux (Issue #284)
        if LINUX:
            browser.SetFocus(True)

class NavigationBar(QFrame):
    def __init__(self, cef_widget):
        super(NavigationBar, self).__init__()
        self.cef_widget = cef_widget
        
        layout = QGridLayout()
        layout.setContentsMargins(0,0,0,0)
        layout.setSpacing(0)
        
        self.back = self.createButton("back")
        self.back.clicked.connect(self.onBack)
        layout.addWidget(self.back, 0, 0)
        
        self.forward = self.createButton("forward")
        self.forward.clicked.connect(self.onForward)
        layout.addWidget(self.forward, 0, 1)
        
        self.reload = self.createButton("reload")
        self.reload.clicked.connect(self.onReload)
        layout.addWidget(self.reload, 0, 2)
        
        self.url = QLineEdit("")
        self.url.returnPressed.connect(self.onGoUrl)
        layout.addWidget(self.url, 0, 3)
        
        self.setLayout(layout)
        self.updateState()
    
    def onBack(self):
        if self.cef_widget.browser:
            self.cef_widget.browser.GoBack()
            
    def onForward(self):
        if self.cef_widget.browser:
            self.cef_widget.browser.GoForward()
            
    def onReload(self):
        if self.cef_widget.browser:
            self.cef_widget.browser.Reload()
        
    def onGoUrl(self):
        if self.cef_widget.browser:
            self.cef_widget.browser.LoadUrl(self.url.text())
            
    def updateState(self):
        browser = self.cef_widget.browser
        if not browser:
            self.back.setEnabled(False)
            self.forward.setEnabled(False)
            self.reload.setEnabled(False)
            self.url.setEnabled(False)
            return
        self.back.setEnabled(browser.CanGoBack())
        self.forward.setEnabled(browser.CanGoForward())
        self.reload.setEnabled(True)
        self.url.setEnabled(True)
        self.url.setText(browser.GetUrl())
        
    def createButton(self, name):
        resources = os.path.join(os.path.abspath(os.path.dirname("./FirstLauncher/html/resource/icon.png")),
                                 "resources")
        pixmap = QPixmap(os.path.join (resources, "{0}.png".format(name)))
        icon = QIcon(pixmap)
        button = QPushButton()
        button.setIcon(icon)
        button.setIconSize(pixmap.rect().size())
        return button

if __name__ == "__main__":
    main()