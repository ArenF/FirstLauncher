from cefpython3 import cefpython as cef
import ctypes
import os
import platform
import sys

from PyQt5 import uic
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

form_class = uic.loadUiType("qt_design/launcher_design.ui")[0]

class WindowClass(QMainWindow, form_class):
    
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(50)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 92, 157, 550))
        
        self.setGraphicsEffect(self.shadow)
        
        self.setWindowIcon(QIcon("./qt_design/icon.png"))
        self.setWindowTitle("FIRST LAUNCHER")
        
        # QSizeGrip(self.size_grip)
        self.float_button = FloatingButton(self)
        
        self.clickedButton()
        
        self.show()
        
    def clickedButton(self):
        # self.minimize_window_button.clicked.connect(lambda: self.showMinimized())
        # self.close_window_button.clicked.connect(lambda: self.close())
        # self.exit_button.clicked.connect(lambda: self.close())
        pass

class FloatingButton(QPushButton):
    
    def __init__(self, parent):
        super().__init__(parent)
        self.paddingLeft = 5
        self.paddingTop = 5
        
    def update_position(self):
        if hasattr(self.parent(), 'viewport'):
            parent_rect = self.parent().viewport().rect()
        else:
            parent_rect = self.parent().rect()

        if not parent_rect:
            return
        
        x = parent_rect.width() - self.width() - self.paddingLeft
        y = self.paddingTop
        self.setGeometry(x, y, self.width(), self.height())
        
    def resizeEvent(self, event):
        super().resizeEvent(event)
        self.update_position()

    def mousePressEvent(self, event) -> None:
        self.parent().floatingButtonClicked.emit()

        
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()