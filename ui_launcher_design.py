# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'launcher_designnIcupm.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import resource_rc
import sys
import os
import shutil

import client.authorization as auth
import client.minecraft as mc


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1093, 551)
        MainWindow.setStyleSheet(u"* {\n"
"	border:none;\n"
"}\n"
"\n"
"QToolTip\n"
"{\n"
"     border: 1px solid black;\n"
"     background-color: #D1DBCB;\n"
"     padding: 1px;\n"
"     border-radius: 3px;\n"
"     opacity: 100;\n"
"}\n"
"\n"
"QWidget\n"
"{\n"
"    color: #b1b1b1;\n"
"    background-color: #323232;\n"
"}\n"
"\n"
"QWidget:item:hover\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #D1DBCB, stop: 1 #b2b6af);\n"
"    color: #000000;\n"
"}\n"
"\n"
"QWidget:item:selected\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #D1DBCB, stop: 1 #b2b6af);\n"
"}\n"
"\n"
"QMenuBar::item\n"
"{\n"
"    background: transparent;\n"
"}\n"
"\n"
"QMenuBar::item:selected\n"
"{\n"
"    background: transparent;\n"
"    border: 1px solid #fdf6e3;\n"
"}\n"
"\n"
"QMenuBar::item:pressed\n"
"{\n"
"    background: #444;\n"
"    border: 1px solid #000;\n"
"    background-color: QLinearGradient(\n"
"        x1:0, y1:0,\n"
"        x2:0, y2:1,\n"
"        stop:1 #212121,\n"
"        stop:0"
                        ".4 #343434/*,\n"
"        stop:0.2 #343434,\n"
"        stop:0.1 #fdf6e3*/\n"
"    );\n"
"    margin-bottom:-1px;\n"
"    padding-bottom:1px;\n"
"}\n"
"\n"
"QMenu\n"
"{\n"
"    border: 1px solid #000;\n"
"}\n"
"\n"
"QMenu::item\n"
"{\n"
"    padding: 2px 20px 2px 20px;\n"
"}\n"
"\n"
"QMenu::item:selected\n"
"{\n"
"    color: #000000;\n"
"}\n"
"\n"
"QWidget:disabled\n"
"{\n"
"    color: #404040;\n"
"    background-color: #323232;\n"
"}\n"
"\n"
"QAbstractItemView\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #4d4d4d, stop: 0.1 #646464, stop: 1 #5d5d5d);\n"
"}\n"
"\n"
"QWidget:focus\n"
"{\n"
"    /*border: 2px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0\n"
"     #D1DBCB, stop: 1 #b2b6af);*/\n"
"}\n"
"\n"
"QLineEdit\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #4d4d4d, stop: 0 #646464, stop: 1 #5d5d5d);\n"
"    padding: 1px;\n"
"    border-style: solid;\n"
"    border: 1px solid #1e1e1e;\n"
"    border-radius: 5;\n"
"}\n"
""
                        "\n"
"QPushButton\n"
"{\n"
"    color: #b1b1b1;\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #565656, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
"    border-width: 1px;\n"
"    border-color: #1e1e1e;\n"
"    border-style: solid;\n"
"    border-radius: 6;\n"
"    padding: 3px;\n"
"    font-size: 12px;\n"
"    padding-left: 5px;\n"
"    padding-right: 5px;\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #2d2d2d, stop: 0.1 #2b2b2b, stop: 0.5 #292929, stop: 0.9 #282828, stop: 1 #252525);\n"
"}\n"
"\n"
"QComboBox\n"
"{\n"
"    selection-background-color: #fdf6e3;\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #565656, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
"    border-style: solid;\n"
"    border: 1px solid #1e1e1e;\n"
"    border-radius: 5;\n"
"}\n"
"\n"
"QComboBox:hover,QPushButton:hover\n"
"{\n"
"    bord"
                        "er: 2px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0\n"
"    #D1DBCB, stop: 1 #b2b6af);\n"
"}\n"
"\n"
"\n"
"QComboBox:on\n"
"{\n"
"    padding-top: 3px;\n"
"    padding-left: 4px;\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #2d2d2d, stop: 0.1 #2b2b2b, stop: 0.5 #292929, stop: 0.9 #282828, stop: 1 #252525);\n"
"    selection-background-color: #fdf6e3;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView\n"
"{\n"
"    border: 2px solid darkgray;\n"
"    selection-background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1,\n"
"     stop: 0 #D1DBCB, stop: 1 #b2b6af);\n"
"}\n"
"\n"
"QComboBox::drop-down\n"
"{\n"
"     subcontrol-origin: padding;\n"
"     subcontrol-position: top right;\n"
"     width: 15px;\n"
"\n"
"     border-left-width: 0px;\n"
"     border-left-color: darkgray;\n"
"     border-left-style: solid; /* just a single line */\n"
"     border-top-right-radius: 3px; /* same radius as the QComboBox */\n"
"     border-bottom-right-radius: 3px;\n"
" }\n"
"\n"
"QCo"
                        "mboBox::down-arrow\n"
"{\n"
"     image: url(:/down_arrow.png);\n"
"}\n"
"\n"
"QGroupBox:focus\n"
"{\n"
"border: 2px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0\n"
"#D1DBCB, stop: 1 #b2b6af);\n"
"}\n"
"\n"
"QTextEdit:focus\n"
"{\n"
"    border: 2px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0\n"
"    #D1DBCB, stop: 1 #b2b6af);\n"
"}\n"
"\n"
"QScrollArea:focus {\n"
"border: 1px solid black;\n"
"}\n"
"\n"
"QScrollBar:horizontal {\n"
"     border: 1px solid #222222;\n"
"     background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0.0 #121212, stop: 0.2 #282828, stop: 1 #484848);\n"
"     height: 7px;\n"
"     margin: 0px 16px 0 16px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal\n"
"{\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0\n"
"      #D1DBCB, stop: 0.5 #b2b6af, stop: 1 #D1DBCB);\n"
"      min-height: 20px;\n"
"      border-radius: 2px;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal {\n"
"      border: 1px solid #1b1b19;\n"
"      border-radius:"
                        " 2px;\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0\n"
"      #D1DBCB, stop: 1 #b2b6af);\n"
"      width: 14px;\n"
"      subcontrol-position: right;\n"
"      subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal {\n"
"      border: 1px solid #1b1b19;\n"
"      border-radius: 2px;\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0\n"
"      #D1DBCB, stop: 1 #b2b6af);\n"
"      width: 14px;\n"
"     subcontrol-position: left;\n"
"     subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::right-arrow:horizontal, QScrollBar::left-arrow:horizontal\n"
"{\n"
"      border: 1px solid black;\n"
"      width: 1px;\n"
"      height: 1px;\n"
"      background: white;\n"
"}\n"
"\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"      background: none;\n"
"}\n"
"\n"
"QScrollBar:vertical\n"
"{\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0.0 #121212, stop: 0.2 #282828, stop: 1 #484848);\n"
"    "
                        "  width: 7px;\n"
"      margin: 16px 0 16px 0;\n"
"      border: 1px solid #222222;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical\n"
"{\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0\n"
"      #D1DBCB, stop: 0.5 #b2b6af, stop: 1 #D1DBCB);\n"
"      min-height: 20px;\n"
"      border-radius: 2px;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical\n"
"{\n"
"      border: 1px solid #1b1b19;\n"
"      border-radius: 2px;\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0\n"
"      #D1DBCB, stop: 1 #b2b6af);\n"
"      height: 14px;\n"
"      subcontrol-position: bottom;\n"
"      subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical\n"
"{\n"
"      border: 1px solid #1b1b19;\n"
"      border-radius: 2px;\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #b2b6af,\n"
"      stop: 1 #D1DBCB);\n"
"      height: 14px;\n"
"      subcontrol-position: top;\n"
"      subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::up-arrow:vertical, "
                        "QScrollBar::down-arrow:vertical\n"
"{\n"
"      border: 1px solid black;\n"
"      width: 1px;\n"
"      height: 1px;\n"
"      background: white;\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical\n"
"{\n"
"      background: none;\n"
"}\n"
"\n"
"QTextEdit\n"
"{\n"
"    background-color: #242424;\n"
"}\n"
"\n"
"QPlainTextEdit\n"
"{\n"
"    background-color: #242424;\n"
"}\n"
"\n"
"QHeaderView::section\n"
"{\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #616161, stop: 0.5 #505050, stop: 0.6 #434343, stop:1 #656565);\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    border: 1px solid #6c6c6c;\n"
"}\n"
"\n"
"QCheckBox:disabled\n"
"{\n"
"color: #414141;\n"
"}\n"
"\n"
"QDockWidget::title\n"
"{\n"
"    text-align: center;\n"
"    spacing: 3px; /* spacing between items in the tool bar */\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #323232, stop: 0.5 #242424, stop:1 #323232);\n"
"}\n"
"\n"
"QDockWidget::close-button, QDockWidg"
                        "et::float-button\n"
"{\n"
"    text-align: center;\n"
"    spacing: 1px; /* spacing between items in the tool bar */\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #323232, stop: 0.5 #242424, stop:1 #323232);\n"
"}\n"
"\n"
"QDockWidget::close-button:hover, QDockWidget::float-button:hover\n"
"{\n"
"    background: #242424;\n"
"}\n"
"\n"
"QDockWidget::close-button:pressed, QDockWidget::float-button:pressed\n"
"{\n"
"    padding: 1px -1px -1px 1px;\n"
"}\n"
"\n"
"QMainWindow::separator\n"
"{\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #161616, stop: 0.5 #151515, stop: 0.6 #212121, stop:1 #343434);\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    border: 1px solid #4c4c4c;\n"
"    spacing: 3px; /* spacing between items in the tool bar */\n"
"}\n"
"\n"
"QMainWindow::separator:hover\n"
"{\n"
"\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #b2b6af,\n"
"    stop:0.5 #b56c17 stop:1 #D1DBCB);\n"
"    color: white;\n"
"    padding-l"
                        "eft: 4px;\n"
"    border: 1px solid #6c6c6c;\n"
"    spacing: 3px; /* spacing between items in the tool bar */\n"
"}\n"
"\n"
"QToolBar {\n"
"    border: 1px transparent #323232;\n"
"    background: 1px solid #323232;\n"
"}\n"
"\n"
"QToolBar::handle\n"
"{\n"
"     spacing: 3px; /* spacing between items in the tool bar */\n"
"     background: url(:/images/handle.png);\n"
"}\n"
"\n"
"QMenu::separator\n"
"{\n"
"    height: 2px;\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #161616, stop: 0.5 #151515, stop: 0.6 #212121, stop:1 #343434);\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    margin-left: 10px;\n"
"    margin-right: 5px;\n"
"}\n"
"\n"
"QProgressBar\n"
"{\n"
"    border: 2px solid grey;\n"
"    border-radius: 5px;\n"
"    text-align: center;\n"
"}\n"
"\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: #b2b6af;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"    color: #b1b1b1;\n"
"    border: 1px solid #444;\n"
"    border-bottom-style"
                        ": none;\n"
"    background-color: #323232;\n"
"    padding-left: 10px;\n"
"    padding-right: 10px;\n"
"    padding-top: 3px;\n"
"    padding-bottom: 2px;\n"
"    margin-right: -1px;\n"
"}\n"
"\n"
"QTabWidget::pane {\n"
"    border: 1px solid #444;\n"
"    top: 1px;\n"
"}\n"
"\n"
"QTabBar::tab:last\n"
"{\n"
"    margin-right: 0; /* the last selected tab has nothing to overlap with on the right */\n"
"    border-top-right-radius: 3px;\n"
"}\n"
"\n"
"QTabBar::tab:first:!selected\n"
"{\n"
" margin-left: 0px; /* the last selected tab has nothing to overlap with on the right */\n"
"\n"
"\n"
"    border-top-left-radius: 3px;\n"
"}\n"
"\n"
"QTabBar::tab:!selected\n"
"{\n"
"    color: #b1b1b1;\n"
"    border-bottom-style: solid;\n"
"    margin-top: 3px;\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:1 #212121, stop:.4 #343434);\n"
"}\n"
"\n"
"QTabBar::tab:selected\n"
"{\n"
"    border-top-left-radius: 3px;\n"
"    border-top-right-radius: 3px;\n"
"    margin-bottom: 0px;\n"
"}\n"
"\n"
"QTabBar:"
                        ":tab:!selected:hover\n"
"{\n"
"    /*border-top: 2px solid #fdf6e3;\n"
"    padding-bottom: 3px;*/\n"
"    border-top-left-radius: 3px;\n"
"    border-top-right-radius: 3px;\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:1 #212121, stop:0.4 #343434, stop:0.2 #343434, stop:0.1 #fdf6e3);\n"
"}\n"
"\n"
"QRadioButton::indicator:checked, QRadioButton::indicator:unchecked{\n"
"    color: #b1b1b1;\n"
"    background-color: #323232;\n"
"    border: 1px solid #b1b1b1;\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked\n"
"{\n"
"    background-color: qradialgradient(\n"
"        cx: 0.5, cy: 0.5,\n"
"        fx: 0.5, fy: 0.5,\n"
"        radius: 1.0,\n"
"        stop: 0.25 #fdf6e3,\n"
"        stop: 0.3 #323232\n"
"    );\n"
"}\n"
"\n"
"QCheckBox::indicator{\n"
"    color: #b1b1b1;\n"
"    background-color: #323232;\n"
"    border: 1px solid #b1b1b1;\n"
"    width: 9px;\n"
"    height: 9px;\n"
"}\n"
"\n"
"QRadioButton::indicator\n"
"{\n"
"    border-radius: 6px;\n"
"}\n"
""
                        "\n"
"QRadioButton::indicator:hover, QCheckBox::indicator:hover\n"
"{\n"
"    border: 1px solid #fdf6e3;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked\n"
"{\n"
"    image:url(:/images/checkbox.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:disabled, QRadioButton::indicator:disabled\n"
"{\n"
"    border: 1px solid #444;\n"
"}")
        
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.sidebar = QFrame(self.centralwidget)
        self.sidebar.setObjectName(u"sidebar")
        self.sidebar.setStyleSheet(u"")
        self.sidebar.setFrameShape(QFrame.StyledPanel)
        self.sidebar.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.sidebar)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.header = QFrame(self.sidebar)
        self.header.setObjectName(u"header")
        self.header.setFrameShape(QFrame.StyledPanel)
        self.header.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.header)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.header)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)

        self.label_3 = QLabel(self.header)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(30, 30))
        self.label_3.setPixmap(QPixmap(u":/html/icon.png"))
        self.label_3.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.label_3)


        self.verticalLayout.addWidget(self.header, 0, Qt.AlignTop)

        self.body = QFrame(self.sidebar)
        self.body.setObjectName(u"body")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.body.sizePolicy().hasHeightForWidth())
        self.body.setSizePolicy(sizePolicy)
        self.body.setFrameShape(QFrame.StyledPanel)
        self.body.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.body)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(6, 0, 0, 0)
        self.frame = QFrame(self.body)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.loginButton = BetweenButton(self.frame, "LOGIN", "MAIN")
        self.loginButton.setObjectName(u"loginButton")

        self.verticalLayout_5.addWidget(self.loginButton)

        self.modsButton = QPushButton(self.frame)
        self.modsButton.setObjectName(u"modsButton")

        self.verticalLayout_5.addWidget(self.modsButton)

        self.installButton = QPushButton(self.frame)
        self.installButton.setObjectName(u"installButton")

        self.verticalLayout_5.addWidget(self.installButton)

        self.settingButton = QPushButton(self.frame)
        self.settingButton.setObjectName(u"settingButton")

        self.verticalLayout_5.addWidget(self.settingButton)


        self.verticalLayout_3.addWidget(self.frame, 0, Qt.AlignTop)


        self.verticalLayout.addWidget(self.body)

        self.footer = QFrame(self.sidebar)
        self.footer.setObjectName(u"footer")
        self.footer.setFrameShape(QFrame.StyledPanel)
        self.footer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.footer)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.pushButton_5 = QPushButton(self.footer)
        self.pushButton_5.setObjectName(u"pushButton_5")
        icon = QIcon()
        icon.addFile(u":/icon_pack/tutorial_icon_package/link-2.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_5.setIcon(icon)

        self.verticalLayout_4.addWidget(self.pushButton_5, 0, Qt.AlignLeft|Qt.AlignBottom)


        self.verticalLayout.addWidget(self.footer, 0, Qt.AlignBottom)


        self.horizontalLayout.addWidget(self.sidebar)

        self.main_widget = QFrame(self.centralwidget)
        self.main_widget.setObjectName(u"main_widget")
        self.main_widget.setFrameShape(QFrame.StyledPanel)
        self.main_widget.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.main_widget)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.stackedMain = QStackedWidget(self.main_widget)
        self.stackedMain.setObjectName(u"stackedMain")
        self.mainPage = QWidget()
        self.mainPage.setObjectName(u"mainPage")
        self.verticalLayout_6 = QVBoxLayout(self.mainPage)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.mainImage = MainImage(self.mainPage)
        self.mainImage.setObjectName(u"mainImage")
        self.mainImage.setPixmap(QPixmap(u":/image/2022-11-28_21.14.33.png"))
        self.mainImage.setScaledContents(True)

        self.verticalLayout_6.addWidget(self.mainImage)

        self.stackedMain.addWidget(self.mainPage)
        self.loginPage = QWidget()
        self.loginPage.setObjectName(u"loginPage")
        self.verticalLayout_7 = QVBoxLayout(self.loginPage)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.cefWidget = QWidget(self)
        self.cefWidget.setObjectName(u"cefWidget")

        self.verticalLayout_7.addWidget(self.cefWidget)

        self.stackedMain.addWidget(self.loginPage)
        self.modsPage = QWidget()
        self.modsPage.setObjectName(u"modsPage")
        self.verticalLayout_8 = QVBoxLayout(self.modsPage)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.modsPage)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_2)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.frame_5 = QFrame(self.frame_2)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_5)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.searchHeader = QFrame(self.frame_5)
        self.searchHeader.setObjectName(u"searchHeader")
        self.searchHeader.setFrameShape(QFrame.StyledPanel)
        self.searchHeader.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.searchHeader)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.searchEdit = QLineEdit(self.searchHeader)
        self.searchEdit.setObjectName(u"searchEdit")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.searchEdit.sizePolicy().hasHeightForWidth())
        self.searchEdit.setSizePolicy(sizePolicy1)
        self.searchEdit.setMinimumSize(QSize(0, 35))

        self.horizontalLayout_3.addWidget(self.searchEdit)

        self.searchButton = QPushButton(self.searchHeader)
        self.searchButton.setObjectName(u"searchButton")
        self.searchButton.setMinimumSize(QSize(35, 35))
        icon1 = QIcon()
        icon1.addFile(u":/icon_pack/tutorial_icon_package/search.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.searchButton.setIcon(icon1)

        self.horizontalLayout_3.addWidget(self.searchButton)


        self.verticalLayout_11.addWidget(self.searchHeader)

        self.listFrame = DragFrame(self.frame_5)
        self.listFrame.setObjectName(u"listFrame")
        self.listFrame.setEnabled(True)
        sizePolicy.setHeightForWidth(self.listFrame.sizePolicy().hasHeightForWidth())
        self.listFrame.setSizePolicy(sizePolicy)
        self.listFrame.setAcceptDrops(True)
        self.listFrame.setFrameShape(QFrame.StyledPanel)
        self.listFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.listFrame)
        self.verticalLayout_10.setSpacing(5)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(9, 9, 9, 9)
        self.modsPath = QLabel(self.listFrame)
        self.modsPath.setObjectName(u"modsPath")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.modsPath.sizePolicy().hasHeightForWidth())
        self.modsPath.setSizePolicy(sizePolicy2)
        self.modsPath.setMinimumSize(QSize(0, 0))
        self.modsPath.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_10.addWidget(self.modsPath)

        self.modsList = QListWidget(self.listFrame)
        icon2 = QIcon()
        icon2.addFile(u":/html/icons8-folder-30.png", QSize(), QIcon.Normal, QIcon.Off)
        __qlistwidgetitem = QListWidgetItem(self.modsList)
        __qlistwidgetitem.setIcon(icon2)
        QListWidgetItem(self.modsList)
        self.modsList.setObjectName(u"modsList")
        

        self.verticalLayout_10.addWidget(self.modsList)


        self.verticalLayout_11.addWidget(self.listFrame)


        self.verticalLayout_9.addWidget(self.frame_5)


        self.verticalLayout_8.addWidget(self.frame_2)

        self.stackedMain.addWidget(self.modsPage)
        self.installPage = QWidget()
        self.installPage.setObjectName(u"installPage")
        self.verticalLayout_13 = QVBoxLayout(self.installPage)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.installFrame = QFrame(self.installPage)
        self.installFrame.setObjectName(u"installFrame")
        self.installFrame.setFrameShape(QFrame.StyledPanel)
        self.installFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.installFrame)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.versionsList = QListWidget(self.installFrame)
        QListWidgetItem(self.versionsList)
        QListWidgetItem(self.versionsList)
        self.versionsList.setObjectName(u"versionsList")

        self.horizontalLayout_4.addWidget(self.versionsList)


        self.verticalLayout_13.addWidget(self.installFrame)

        self.stackedMain.addWidget(self.installPage)
        self.settingPage = QWidget()
        self.settingPage.setObjectName(u"settingPage")
        self.verticalLayout_12 = QVBoxLayout(self.settingPage)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.frame_6 = QFrame(self.settingPage)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_6)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.settingHeader = QFrame(self.frame_6)
        self.settingHeader.setObjectName(u"settingHeader")
        self.settingHeader.setFrameShape(QFrame.StyledPanel)
        self.settingHeader.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.settingHeader)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.settingPBCollection = QFrame(self.settingHeader)
        self.settingPBCollection.setObjectName(u"settingPBCollection")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.settingPBCollection.sizePolicy().hasHeightForWidth())
        self.settingPBCollection.setSizePolicy(sizePolicy3)
        self.settingPBCollection.setFrameShape(QFrame.StyledPanel)
        self.settingPBCollection.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.settingPBCollection)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.launcherButton = QPushButton(self.settingPBCollection)
        self.launcherButton.setObjectName(u"launcherButton")
        sizePolicy2.setHeightForWidth(self.launcherButton.sizePolicy().hasHeightForWidth())
        self.launcherButton.setSizePolicy(sizePolicy2)
        self.launcherButton.setMaximumSize(QSize(16777215, 16777215))
        icon3 = QIcon()
        icon3.addFile(u":/icon_pack/tutorial_icon_package/settings.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.launcherButton.setIcon(icon3)

        self.horizontalLayout_6.addWidget(self.launcherButton)

        self.skinButton = QPushButton(self.settingPBCollection)
        self.skinButton.setObjectName(u"skinButton")
        icon4 = QIcon()
        icon4.addFile(u":/icon_pack/tutorial_icon_package/users.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.skinButton.setIcon(icon4)

        self.horizontalLayout_6.addWidget(self.skinButton)

        self.otherButton = QPushButton(self.settingPBCollection)
        self.otherButton.setObjectName(u"otherButton")
        icon5 = QIcon()
        icon5.addFile(u":/icon_pack/tutorial_icon_package/edit.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.otherButton.setIcon(icon5)

        self.horizontalLayout_6.addWidget(self.otherButton)


        self.horizontalLayout_5.addWidget(self.settingPBCollection, 0, Qt.AlignLeft|Qt.AlignTop)


        self.verticalLayout_14.addWidget(self.settingHeader, 0, Qt.AlignTop)

        self.settingMain = QFrame(self.frame_6)
        self.settingMain.setObjectName(u"settingMain")
        sizePolicy.setHeightForWidth(self.settingMain.sizePolicy().hasHeightForWidth())
        self.settingMain.setSizePolicy(sizePolicy)
        self.settingMain.setFrameShape(QFrame.StyledPanel)
        self.settingMain.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.settingMain)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.settingStacked = QStackedWidget(self.settingMain)
        self.settingStacked.setObjectName(u"settingStacked")
        self.SettingPage = QWidget()
        self.SettingPage.setObjectName(u"SettingPage")
        self.verticalLayout_15 = QVBoxLayout(self.SettingPage)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.settingFrame = QFrame(self.SettingPage)
        self.settingFrame.setObjectName(u"settingFrame")
        self.settingFrame.setFrameShape(QFrame.StyledPanel)
        self.settingFrame.setFrameShadow(QFrame.Raised)
        self.formLayout = QFormLayout(self.settingFrame)
        self.formLayout.setObjectName(u"formLayout")
        self.jvmMax = QLineEdit(self.settingFrame)
        self.jvmMax.setObjectName(u"jvmMax")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.jvmMax)

        self.Xmx = QLabel(self.settingFrame)
        self.Xmx.setObjectName(u"Xmx")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.Xmx)

        self.jvmMin = QLineEdit(self.settingFrame)
        self.jvmMin.setObjectName(u"jvmMin")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.jvmMin)

        self.Xms = QLabel(self.settingFrame)
        self.Xms.setObjectName(u"Xms")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.Xms)

        self.resolutionWidth = QLineEdit(self.settingFrame)
        self.resolutionWidth.setObjectName(u"resolutionWidth")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.resolutionWidth)

        self.resolutionW = QLabel(self.settingFrame)
        self.resolutionW.setObjectName(u"resolutionW")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.resolutionW)

        self.resolutionHeight = QLineEdit(self.settingFrame)
        self.resolutionHeight.setObjectName(u"resolutionHeight")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.resolutionHeight)

        self.resolutionH = QLabel(self.settingFrame)
        self.resolutionH.setObjectName(u"resolutionH")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.resolutionH)

        self.resolutionCheckBox = QCheckBox(self.settingFrame)
        self.resolutionCheckBox.setObjectName(u"resolutionCheckBox")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.resolutionCheckBox)

        self.checking = QLabel(self.settingFrame)
        self.checking.setObjectName(u"checking")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.checking)


        self.verticalLayout_15.addWidget(self.settingFrame)

        self.settingStacked.addWidget(self.SettingPage)
        self.SkinPage = QWidget()
        self.SkinPage.setObjectName(u"SkinPage")
        self.verticalLayout_16 = QVBoxLayout(self.SkinPage)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.skinFrame = QFrame(self.SkinPage)
        self.skinFrame.setObjectName(u"skinFrame")
        self.skinFrame.setFrameShape(QFrame.StyledPanel)
        self.skinFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.skinFrame)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.imageFrame = QFrame(self.skinFrame)
        self.imageFrame.setObjectName(u"imageFrame")
        self.imageFrame.setStyleSheet(u"QLabel {\n"
"	border: 2px dashed #fff;\n"
"	border-radius: 10px;\n"
"	margin: 0;\n"
"	padding: 0;\n"
"	outline: none;\n"
"	opacity: 0;\n"
"	background-color: #444444;\n"
"}")
        self.imageFrame.setFrameShape(QFrame.StyledPanel)
        self.imageFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.imageFrame)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.skinImage = QLabel(self.imageFrame)
        self.skinImage.setObjectName(u"skinImage")
        sizePolicy2.setHeightForWidth(self.skinImage.sizePolicy().hasHeightForWidth())
        self.skinImage.setSizePolicy(sizePolicy2)
        self.skinImage.setMinimumSize(QSize(300, 200))
        self.skinImage.setAlignment(Qt.AlignCenter)

        self.verticalLayout_18.addWidget(self.skinImage, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout_17.addWidget(self.imageFrame)

        self.frame_7 = QFrame(self.skinFrame)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.frame_7)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.uploadSkinPB = QPushButton(self.frame_7)
        self.uploadSkinPB.setObjectName(u"uploadSkinPB")

        self.verticalLayout_19.addWidget(self.uploadSkinPB, 0, Qt.AlignHCenter)


        self.verticalLayout_17.addWidget(self.frame_7)


        self.verticalLayout_16.addWidget(self.skinFrame)

        self.settingStacked.addWidget(self.SkinPage)
        self.OtherPage = QWidget()
        self.OtherPage.setObjectName(u"OtherPage")
        self.verticalLayout_20 = QVBoxLayout(self.OtherPage)
        self.verticalLayout_20.setSpacing(0)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.otherFrame = QFrame(self.OtherPage)
        self.otherFrame.setObjectName(u"otherFrame")
        self.otherFrame.setFrameShape(QFrame.StyledPanel)
        self.otherFrame.setFrameShadow(QFrame.Raised)
        self.formLayout_2 = QFormLayout(self.otherFrame)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.serverIPInput = QLineEdit(self.otherFrame)
        self.serverIPInput.setObjectName(u"serverIPInput")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.serverIPInput)

        self.serverLabel = QLabel(self.otherFrame)
        self.serverLabel.setObjectName(u"serverLabel")

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.serverLabel)

        self.portInput = QLineEdit(self.otherFrame)
        self.portInput.setObjectName(u"portInput")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.portInput)

        self.portLabel = QLabel(self.otherFrame)
        self.portLabel.setObjectName(u"portLabel")

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.portLabel)


        self.verticalLayout_20.addWidget(self.otherFrame)

        self.settingStacked.addWidget(self.OtherPage)

        self.horizontalLayout_7.addWidget(self.settingStacked)


        self.verticalLayout_14.addWidget(self.settingMain)


        self.verticalLayout_12.addWidget(self.frame_6)

        self.stackedMain.addWidget(self.settingPage)

        self.verticalLayout_2.addWidget(self.stackedMain)


        self.horizontalLayout.addWidget(self.main_widget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedMain.setCurrentIndex(0)
        self.settingStacked.setCurrentIndex(2)
        
        ''' 
        
            커스텀 작성 시작 라인
        
        '''
        
        # floating button 생성
        self.mainImage.floatingButtonSignal.connect(lambda: print("START"))
        
        

# 페이지메니저 생성
        self.stackedMain.setCurrentIndex(3)
        self.pageManager = PageManager()
        self.pageManager.savePageWidget(self.stackedMain)
        self.pageManager.setStatus(0)
        
        self.modsManager = ModsManager()
        self.modsManager.default_set(self, self.modsList, self.modsPath)
        self.modsList.itemDoubleClicked.connect(self.modsManager.doubleClickedItem)
        
        self.second_window = Progress_Window()
        self.install_thread = InstallThread()
        
        self.install_thread.progress_max.connect(lambda maximum: self.second_window.progressBar.setMaximum(maximum))
        self.install_thread.progress.connect(lambda value: self.second_window.progressBar.setValue(value))
        self.install_thread.text.connect(lambda text: self.second_window.label.setText(text))
        
        self.versionManager = InstallManager()
        self.versionManager.default_set(self, self.versionsList, self.second_window)
        self.versionsList.itemDoubleClicked.connect(self.versionManager.doubleClickedItem)
        
# 버튼들
        button_clicked(self)
        
        ''' 
        
            커스텀 작성 종결 라인
        
        '''

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"FIRSTLAUNCHER", None))
        self.label_3.setText("")
        self.loginButton.setText(QCoreApplication.translate("MainWindow", u"LOGIN", None))
        self.modsButton.setText(QCoreApplication.translate("MainWindow", u"MODS", None))
        self.installButton.setText(QCoreApplication.translate("MainWindow", u"INSTALL", None))
        self.settingButton.setText(QCoreApplication.translate("MainWindow", u"SETTING", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"OWNER", None))
        self.mainImage.setText("")
        self.searchEdit.setText("")
        self.searchEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search..", None))
        self.searchButton.setText("")
        self.modsPath.setText(QCoreApplication.translate("MainWindow", u"UNABLE PATH", None))

        __sortingEnabled = self.modsList.isSortingEnabled()
        self.modsList.setSortingEnabled(False)
        ___qlistwidgetitem = self.modsList.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("MainWindow", u"None-File", None));
        ___qlistwidgetitem1 = self.modsList.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("MainWindow", u"None.none", None));
        self.modsList.setSortingEnabled(__sortingEnabled)


        __sortingEnabled1 = self.versionsList.isSortingEnabled()
        self.versionsList.setSortingEnabled(False)
        ___qlistwidgetitem2 = self.versionsList.item(0)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("MainWindow", u"1.19.2", None));
        ___qlistwidgetitem3 = self.versionsList.item(1)
        ___qlistwidgetitem3.setText(QCoreApplication.translate("MainWindow", u"1.18.2", None));
        self.versionsList.setSortingEnabled(__sortingEnabled1)

        self.launcherButton.setText(QCoreApplication.translate("MainWindow", u"Launcher", None))
        self.skinButton.setText(QCoreApplication.translate("MainWindow", u"Skin", None))
        self.otherButton.setText(QCoreApplication.translate("MainWindow", u"Other", None))
        self.jvmMax.setText("")
        self.Xmx.setText(QCoreApplication.translate("MainWindow", u"Java Maximum", None))
        self.Xms.setText(QCoreApplication.translate("MainWindow", u"Java Minimum", None))
        self.resolutionW.setText(QCoreApplication.translate("MainWindow", u"Resolution width", None))
        self.resolutionH.setText(QCoreApplication.translate("MainWindow", u"Resolution height", None))
        self.resolutionCheckBox.setText(QCoreApplication.translate("MainWindow", u"Custom resolution", None))
        self.checking.setText(QCoreApplication.translate("MainWindow", u"not Checked", None))
        self.skinImage.setText(QCoreApplication.translate("MainWindow", u"Input the Image in here", None))
        self.uploadSkinPB.setText(QCoreApplication.translate("MainWindow", u"Upload Skin", None))
        self.serverLabel.setText(QCoreApplication.translate("MainWindow", u"Server IP", None))
        self.portLabel.setText(QCoreApplication.translate("MainWindow", u"Port", None))
    # retranslateUi
    
# 여기는 따로 작성한 부분

def create_listItem(text:str, icon_path:str) -> QListWidgetItem:
    item = QListWidgetItem()
    item.setText(text)
    item.setIcon(QIcon(icon_path))
    return item
        
        
# class DownloadThread(QThread):
#     def __init__(self, callback):
#         super().__init__()
#         self.callback = callback
        
#     def run(self):
#         for i in range(1, 100):
#             print(i)
#         self.callback()



class InstallThread(QThread):
    progress_max = pyqtSignal("int")
    progress = pyqtSignal("int")
    text = pyqtSignal("QString")

    def __init__(self) -> None:
        QThread.__init__(self)
        self._callback_dict = {
            "setStatus": lambda text: self.text.emit(text),
            "setMax": lambda max_progress: self.progress_max.emit(max_progress),
            "setProgress": lambda progress: self.progress.emit(progress),
        }

    def set_data(self, version: str) -> None:
        self._version = version

    def run(self) -> None:
        mc.VersionControl.generate_version(self._version, self._callback_dict)


class InstallManager(object):
    def __init__(self) -> None:
        pass
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(InstallManager, cls).__new__(cls)
        return cls.instance
    
    def default_set(self, parent, listWidget, progress_window):
        self.parent = parent
        self.listWidget = listWidget
        self.progress_window = progress_window
        self.thr = self.parent.install_thread
        self.setting()
    
    def setting(self):
        version_list = mc.VersionControl.get_versions_on_release()
        installed_list = mc.VersionControl.get_versions_installed()
        self.listWidget.clear()
        for ver in version_list:
            if ver in installed_list:
                self.listWidget.addItem(self.getItemInstalled(ver))
            else:
                self.listWidget.addItem(self.getItemCanInstall(ver))
            
    def doubleClickedItem(self):
        list_item = self.listWidget.selectedItems()
        for item in list_item:
            print(item.text())
            self.progress_window.show()
            
            self.thr.set_data(item.text())
            self.thr.start()
    
    
    def getItemInstalled(self, text) -> QListWidgetItem:
        item = create_listItem(text, ":/icon_pack/tutorial_icon_package/check-square.svg")
        return item
    
    def getItemCanInstall(self, text) -> QListWidgetItem:
        item = create_listItem(text, ":/html/icons8-software-installer-48.png")
        return item
    

class ModsManager(object):
    def __init__(self) -> None:
        pass
    
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(ModsManager, cls).__new__(cls)
        return cls.instance
        
    def default_set(self, parent, listWidget, label):
        self.listWidget = listWidget
        self.label = label
        self.parent = parent
        
        self.currentPath = mc.get_mod_path()
        self.setting()
        
    def getCurrentPath(self):
        return self.currentPath
    
    def getLabel(self):
        return self.label
        
    def setPathLabel(self, text:str):
        self.label.setText(text)
        
    def isFile(self, text):
        return os.path.isfile(self.currentPath + "/" + text)
    
    def doubleClickedItem(self):
        list_item = self.listWidget.selectedItems()
        for item in list_item:
            text = str(item.text())
            if self.isFile(text): #파일명을 기준으로 파일이라면,
                messageBox = QMessageBox.warning(
                    self.parent, '해당 파일을 지우시겠습니까?', '해당 파일 ' + text + ' 를 지우면 다시 복구할 수 없습니다.',
                    QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
                
                # 해당 파일을 지운다면
                if messageBox == QMessageBox.Yes:
                    os.remove(self.currentPath + "/" + text)
                else:
                    return
            else:
                # BACK 위젯을 선택해 뒤로 갔을 때
                if item.text() in "BACK!":
                    r = self.currentPath.split("\\")
                    result = ""
                    for i in r:
                        # 마지막 값은 넣지 않고 값을 반영한다.
                        if len(r)-1 == r.index(i):
                            self.currentPath = result
                            break
                        # 초기일 때는 그냥 더하고 그 이후부터는 결과에 \를 더한다.
                        if r.index(i) == 0:
                            result = i
                        else:
                            result += "\\" + i
                    self.setting()
                    return
                # 폴더를 클릭했을 때
                text = None
                for i in self.listWidget.selectedItems():
                    text = str(i.text())
                self.currentPath = self.currentPath + '\\' + text
            self.setting()
    
    def setting(self):
        self.setPathLabel(self.currentPath)
        mod_list = mc.get_dir_files(self.currentPath)
        self.listWidget.clear()
        for i in mod_list:
            if self.isFile(i):
                self.listWidget.addItem(i)
            else:
                self.listWidget.addItem(self.get_item_isFolder(i))
        item = create_listItem("BACK!", ":/icon_pack/tutorial_icon_package/arrow-left.svg")
        self.listWidget.addItem(item)
        
    def get_item_isFolder(self, text):
        item = create_listItem(text, ":/html/icons8-folder-30.png")
        return item
    
        
        
# 페이지 메니저로 QStackedWidget의 페이지 쉽게 관리하기.
class PageManager(object):
    def __init__(self) -> None:
        pass
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(PageManager, cls).__new__(cls)
        return cls.instance
    
    def savePageWidget(self, stackedWidget):
        self.stackedWidget = stackedWidget
    
    def setStatus(self, page:int):
        self.stackedWidget.setCurrentIndex(page)
        # if self.stackedWidget.indexOf(self.stackedWidget.widget(page)) != 0:
        #     self.stackedWidget.widget(0).float_button.hide()
        # else:
        #     self.stackedWidget.widget(0).float_button.show()
        
# mods 파일용으로 제작된 DnD용 프레임
class DragFrame(QFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.setAcceptDrops(True)
        self.modsManager = ModsManager()
    
    def dragEnterEvent(self, event) -> None:
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()
    
    def dropEvent(self, event):
        files = [u.toLocalFile() for u in event.mimeData().urls()]
        currentPath = self.modsManager.getCurrentPath()
        
        for f in files:
            print(f)
            shutil.move(f, currentPath)
        self.modsManager.setting()
        
        
class MainImage(QLabel):
    floatingButtonSignal = pyqtSignal()
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.float_button = FloatingButton(parent=self)

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self.float_button.update_position()
        
            

class BetweenButton(QPushButton):
    def __init__(self, parent, defaultName, otherName):
        super().__init__(parent)
        self.parentObject = parent
        self.defaultName = defaultName
        self.otherName = otherName
        self.pageManager = PageManager()
        
        self.setText(self.defaultName)

    def mousePressEvent(self, event) -> None:
        # DEFAULT일 때 OTHER로 바꾼다.
        # LOGIN일 때 MAIN으로 바꾼다.
        if self.text() not in self.otherName: 
            self.setText(self.otherName)
            self.pageManager.setStatus(1)
        else: 
            self.setText(self.defaultName)
            self.pageManager.setStatus(0)
            
    def changing_page(self, function):
        self.clicked.connect(lambda: function)    
        
class FloatingButton(QPushButton):
    
    def __init__(self, parent):
        super().__init__(parent)
        self.paddingLeft = 30
        self.paddingTop = 25
        self.setText("START")
        
    def update_position(self):
        parent_rect = self.parent().rect()

        if not parent_rect:
            return
        
        x = parent_rect.width() - self.width() - self.paddingLeft
        y = parent_rect.height() - self.height() - self.paddingTop
        self.setGeometry(x, y, self.width(), self.height())
        
    def resizeEvent(self, event):
        super().resizeEvent(event)
        self.update_position()
        
    def mousePressEvent(self, event) -> None:
        self.parent().floatingButtonSignal.emit()
    
def button_clicked(window):
    window.modsButton.clicked.connect(lambda: window.pageManager.setStatus(2))
    window.installButton.clicked.connect(lambda: window.pageManager.setStatus(3))
    window.settingButton.clicked.connect(lambda: window.pageManager.setStatus(4))
    window.launcherButton.clicked.connect(lambda: window.settingStacked.setCurrentIndex(0))
    window.skinButton.clicked.connect(lambda: window.settingStacked.setCurrentIndex(1))
    window.otherButton.clicked.connect(lambda: window.settingStacked.setCurrentIndex(2))

class Progress_Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
    def setupUi(self, Progressing):
        if not Progressing.objectName():
            Progressing.setObjectName(u"Progressing")
        Progressing.resize(405, 72)
        self.centralwidget = QWidget(Progressing)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label)

        self.progressBar = QProgressBar(self.frame)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(24)
        self.progressBar.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.verticalLayout_2.addWidget(self.progressBar)


        self.verticalLayout.addWidget(self.frame, 0, Qt.AlignVCenter)

        Progressing.setCentralWidget(self.centralwidget)

        self.retranslateUi(Progressing)        

        QMetaObject.connectSlotsByName(Progressing)
    # setupUi

    def retranslateUi(self, Progressing):
        Progressing.setWindowTitle(QCoreApplication.translate("Progressing", u"Progress", None))
        self.label.setText(QCoreApplication.translate("Progressing", u"Progress..", None))
    # retranslateUi

class WindowClass(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        

    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()