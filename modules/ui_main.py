# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.1.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore

from . resources_rc import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1024, 768)
        MainWindow.setMinimumSize(QSize(800, 600))
        font = QFont()
        font.setPointSize(12)
        MainWindow.setFont(font)
        self.styleSheet = QWidget(MainWindow)
        self.styleSheet.setObjectName(u"styleSheet")
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(False)
        font1.setItalic(False)
        self.styleSheet.setFont(font1)
        self.styleSheet.setStyleSheet(u"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"\n"
"SET APP STYLESHEET - FULL STYLES HERE\n"
"DARK THEME - DRACULA COLOR BASED\n"
"\n"
"///////////////////////////////////////////////////////////////////////////////////////////////// */\n"
"\n"
"QWidget{\n"
"	color: rgb(221, 221, 221);\n"
"	font: 12pt \"Segoe UI\";\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Tooltip */\n"
"QToolTip {\n"
"	color: #ffffff;\n"
"	background-color: rgba(33, 37, 43, 180);\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	background-image: none;\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 2px solid rgb(255, 121, 198);\n"
"	text-align: left;\n"
"	padding-left: 8px;\n"
"	margin: 0px;\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Bg App */\n"
"#bgApp {	\n"
"	background"
                        "-color: rgb(40, 44, 52);\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Left Menu */\n"
"#leftMenuBg {	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"#topLogo {\n"
"	background-color: rgb(33, 37, 43);\n"
"	background-image: url(:/images/images/images/AYRA_LOGO.png);\n"
"	background-position: centered;\n"
"	background-repeat: no-repeat;\n"
"}\n"
"#titleLeftApp { font: 63 12pt \"Segoe UI Semibold\"; }\n"
"#titleLeftDescription { font: 8pt \"Segoe UI\"; color: rgb(189, 147, 249); }\n"
"\n"
"/* MENUS */\n"
"#topMenu .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color: transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#topMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#topMenu .QPushButton:pressed {	\n"
"	background-color: rgb(18"
                        "9, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#bottomMenu .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 20px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#bottomMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#bottomMenu .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#leftMenuFrame{\n"
"	border-top: 3px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* Toggle Button */\n"
"#toggleButton {\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 20px solid transparent;\n"
"	background-color: rgb(37, 41, 48);\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"	color: rgb(113, 126, 149);\n"
"}\n"
"#toggleButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#toggleButton:pressed {\n"
"	background-color: rgb("
                        "189, 147, 249);\n"
"}\n"
"\n"
"/* Title Menu */\n"
"#titleRightInfo { padding-left: 10px; }\n"
"\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Extra Tab */\n"
"#extraLeftBox {	\n"
"	background-color: rgb(44, 49, 58);\n"
"}\n"
"#extraTopBg{	\n"
"	background-color: rgb(189, 147, 249)\n"
"}\n"
"\n"
"/* Icon */\n"
"#extraIcon {\n"
"	background-position: center;\n"
"	background-repeat: no-repeat;\n"
"	background-image: url(:/icons/images/icons/icon_settings.png);\n"
"}\n"
"\n"
"/* Label */\n"
"#extraLabel { color: rgb(255, 255, 255); }\n"
"\n"
"/* Btn Close */\n"
"#extraCloseColumnBtn { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#extraCloseColumnBtn:hover { background-color: rgb(196, 161, 249); border-style: solid; border-radius: 4px; }\n"
"#extraCloseColumnBtn:pressed { background-color: rgb(180, 141, 238); border-style: solid; border-radius: 4px; }\n"
"\n"
"/* Extra Content */\n"
"#extraContent{\n"
"	border"
                        "-top: 3px solid rgb(40, 44, 52);\n"
"}\n"
"\n"
"/* Extra Top Menus */\n"
"#extraTopMenu .QPushButton {\n"
"background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#extraTopMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#extraTopMenu .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Content App */\n"
"#contentTopBg{	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"#contentBottom{\n"
"	border-top: 3px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* Top Buttons */\n"
"#rightButtons .QPushButton { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#rightButtons .QPushButton:hover { background-color: rgb(44, 49, 57); border-sty"
                        "le: solid; border-radius: 4px; }\n"
"#rightButtons .QPushButton:pressed { background-color: rgb(23, 26, 30); border-style: solid; border-radius: 4px; }\n"
"\n"
"/* Theme Settings */\n"
"#extraRightBox { background-color: rgb(44, 49, 58); }\n"
"#themeSettingsTopDetail { background-color: rgb(189, 147, 249); }\n"
"\n"
"/* Bottom Bar */\n"
"#bottomBar { background-color: rgb(44, 49, 58); }\n"
"#bottomBar QLabel { font-size: 16px; color: rgb(221, 221, 221); padding-left: 10px; padding-right: 10px; padding-bottom: 2px; }\n"
"\n"
"/* CONTENT SETTINGS */\n"
"/* MENUS */\n"
"#contentSettings .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#contentSettings .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#contentSettings .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb"
                        "(255, 255, 255);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"QTableWidget */\n"
"QTableWidget {	\n"
"	background-color: transparent;\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"	gridline-color: rgb(44, 49, 58);\n"
"	border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item{\n"
"	border-color: rgb(44, 49, 60);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: rgb(44, 49, 58);\n"
"}\n"
"QHeaderView::section{\n"
"	background-color: rgb(33, 37, 43);\n"
"	max-width: 30px;\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::horizontalHeader {	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(33, 37, 43);\n"
"	background-color"
                        ": rgb(33, 37, 43);\n"
"	padding: 3px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"LineEdit */\n"
"QLineEdit {\n"
"	background-color: solid rgb(33, 37, 43);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(20, 20, 20);\n"
"	padding-left: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(150, 150, 150);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"PlainTextEdit */\n"
"QPlainTextEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	padding: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-backgrou"
                        "nd-color: rgb(255, 121, 198);\n"
"}\n"
"QPlainTextEdit  QScrollBar:vertical {\n"
"    width: 8px;\n"
" }\n"
"QPlainTextEdit  QScrollBar:horizontal {\n"
"    height: 8px;\n"
" }\n"
"QPlainTextEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QPlainTextEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ScrollBars */\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 8px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgb(189, 147, 249);\n"
"    min-width: 25px;\n"
"	border-radius: 4px\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-right-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
""
                        "}\n"
"QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-bottom-left-radius: 4px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 8px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
" QScrollBar::handle:vertical {	\n"
"	background: rgb(189, 147, 249);\n"
"    min-height: 25px;\n"
"	border-radius: 4px\n"
" }\n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-bottom-left-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"     subcontrol-position: bottom;\n"
" "
                        "    subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-top-right-radius: 4px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"CheckBox */\n"
"QCheckBox::indicator {\n"
"    border: 3px solid rgb(100, 100, 100);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QCheckBox::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    background: 3px solid rgb(52, 59, 72);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
""
                        "	background-image: url(:/icons/images/icons/cil-check-alt.png);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"RadioButton */\n"
"QRadioButton::indicator {\n"
"    border: 3px solid rgb(100, 100, 100);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QRadioButton::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    background: 3px solid rgb(100, 106, 130);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ComboBox */\n"
"QComboBox{\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(20, 20, 20);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox::drop-down {\n"
"	subcontrol-origin: padding;\n"
""
                        "	subcontrol-position: top right;\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: rgba(39, 44, 54, 150);\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-image: url(:/icons/images/icons/cil-arrow-bottom.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
" }\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(255, 121, 198);	\n"
"	background-color: rgb(33, 37, 43);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Sliders */\n"
"QSlider::groove:horizontal {\n"
"    border-radius: 5px;\n"
"    height: 10px;\n"
"	margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:horizontal:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background-color: rgb(189, 147, 249);\n"
"    border: none;\n"
""
                        "    height: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background-color: rgb(195, 155, 255);\n"
"}\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-color: rgb(255, 121, 198);\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"    border-radius: 5px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:vertical:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:vertical {\n"
"    background-color: rgb(189, 147, 249);\n"
"	border: none;\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider::handle:vertical:hover {\n"
"    background-color: rgb(195, 155, 255);\n"
"}\n"
"QSlider::handle:vertical:pressed {\n"
"    background-color: rgb(255, 121, 198);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"CommandLinkButton */\n"
"QComm"
                        "andLinkButton {	\n"
"	color: rgb(255, 121, 198);\n"
"	border-radius: 5px;\n"
"	padding: 5px;\n"
"	color: rgb(255, 170, 255);\n"
"}\n"
"QCommandLinkButton:hover {	\n"
"	color: rgb(255, 170, 255);\n"
"	background-color: rgb(44, 49, 60);\n"
"}\n"
"QCommandLinkButton:pressed {	\n"
"	color: rgb(189, 147, 249);\n"
"	background-color: rgb(52, 58, 71);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Button */\n"
"#pagesContainer QPushButton {\n"
"	border: 2px solid rgb(150, 150, 150);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"#pagesContainer QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"#pagesContainer QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}\n"
"\n"
"")
        self.appMargins = QVBoxLayout(self.styleSheet)
        self.appMargins.setSpacing(0)
        self.appMargins.setObjectName(u"appMargins")
        self.appMargins.setContentsMargins(10, 10, 10, 10)
        self.bgApp = QFrame(self.styleSheet)
        self.bgApp.setObjectName(u"bgApp")
        self.bgApp.setStyleSheet(u"")
        self.bgApp.setFrameShape(QFrame.NoFrame)
        self.bgApp.setFrameShadow(QFrame.Raised)
        self.appLayout = QHBoxLayout(self.bgApp)
        self.appLayout.setSpacing(0)
        self.appLayout.setObjectName(u"appLayout")
        self.appLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenuBg = QFrame(self.bgApp)
        self.leftMenuBg.setObjectName(u"leftMenuBg")
        self.leftMenuBg.setMinimumSize(QSize(60, 0))
        self.leftMenuBg.setMaximumSize(QSize(60, 16777215))
        self.leftMenuBg.setFrameShape(QFrame.NoFrame)
        self.leftMenuBg.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.leftMenuBg)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.topLogoInfo = QFrame(self.leftMenuBg)
        self.topLogoInfo.setObjectName(u"topLogoInfo")
        self.topLogoInfo.setMinimumSize(QSize(0, 50))
        self.topLogoInfo.setMaximumSize(QSize(16777215, 50))
        self.topLogoInfo.setFrameShape(QFrame.NoFrame)
        self.topLogoInfo.setFrameShadow(QFrame.Raised)
        self.titleLeftApp = QLabel(self.topLogoInfo)
        self.titleLeftApp.setObjectName(u"titleLeftApp")
        self.titleLeftApp.setGeometry(QRect(70, 8, 160, 20))
        self.titleLeftApp.setFont(font1)
        self.titleLeftApp.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.titleLeftDescription = QLabel(self.topLogoInfo)
        self.titleLeftDescription.setObjectName(u"titleLeftDescription")
        self.titleLeftDescription.setGeometry(QRect(70, 27, 160, 16))
        self.titleLeftDescription.setMaximumSize(QSize(16777215, 16))
        font2 = QFont()
        font2.setPointSize(8)
        font2.setBold(False)
        font2.setItalic(False)
        self.titleLeftDescription.setFont(font2)
        self.titleLeftDescription.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.topLogo = QLabel(self.topLogoInfo)
        self.topLogo.setObjectName(u"topLogo")
        self.topLogo.setGeometry(QRect(10, 5, 42, 42))
        self.topLogo.setMinimumSize(QSize(42, 42))

        self.verticalLayout_3.addWidget(self.topLogoInfo)

        self.leftMenuFrame = QFrame(self.leftMenuBg)
        self.leftMenuFrame.setObjectName(u"leftMenuFrame")
        self.leftMenuFrame.setFrameShape(QFrame.NoFrame)
        self.leftMenuFrame.setFrameShadow(QFrame.Raised)
        self.verticalMenuLayout = QVBoxLayout(self.leftMenuFrame)
        self.verticalMenuLayout.setSpacing(0)
        self.verticalMenuLayout.setObjectName(u"verticalMenuLayout")
        self.verticalMenuLayout.setContentsMargins(0, 0, 0, 0)
        self.toggleBox = QFrame(self.leftMenuFrame)
        self.toggleBox.setObjectName(u"toggleBox")
        self.toggleBox.setMaximumSize(QSize(16777215, 45))
        self.toggleBox.setFrameShape(QFrame.NoFrame)
        self.toggleBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.toggleBox)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.toggleButton = QPushButton(self.toggleBox)
        self.toggleButton.setObjectName(u"toggleButton")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toggleButton.sizePolicy().hasHeightForWidth())
        self.toggleButton.setSizePolicy(sizePolicy)
        self.toggleButton.setMinimumSize(QSize(0, 45))
        self.toggleButton.setFont(font1)
        self.toggleButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.toggleButton.setLayoutDirection(Qt.LeftToRight)
        self.toggleButton.setStyleSheet(u"background-image: url(:/icons/images/icons/icon_menu.png);")

        self.verticalLayout_4.addWidget(self.toggleButton)


        self.verticalMenuLayout.addWidget(self.toggleBox)

        self.topMenu = QFrame(self.leftMenuFrame)
        self.topMenu.setObjectName(u"topMenu")
        self.topMenu.setFrameShape(QFrame.NoFrame)
        self.topMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.topMenu)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.btn_home = QPushButton(self.topMenu)
        self.btn_home.setObjectName(u"btn_home")
        sizePolicy.setHeightForWidth(self.btn_home.sizePolicy().hasHeightForWidth())
        self.btn_home.setSizePolicy(sizePolicy)
        self.btn_home.setMinimumSize(QSize(0, 45))
        self.btn_home.setFont(font1)
        self.btn_home.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_home.setLayoutDirection(Qt.LeftToRight)
        self.btn_home.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-home.png);")

        self.verticalLayout_8.addWidget(self.btn_home)

        self.btn_setting = QPushButton(self.topMenu)
        self.btn_setting.setObjectName(u"btn_setting")
        sizePolicy.setHeightForWidth(self.btn_setting.sizePolicy().hasHeightForWidth())
        self.btn_setting.setSizePolicy(sizePolicy)
        self.btn_setting.setMinimumSize(QSize(0, 45))
        self.btn_setting.setFont(font1)
        self.btn_setting.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_setting.setLayoutDirection(Qt.LeftToRight)
        self.btn_setting.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-settings.png);")

        self.verticalLayout_8.addWidget(self.btn_setting)

        self.btn_calibration = QPushButton(self.topMenu)
        self.btn_calibration.setObjectName(u"btn_calibration")
        sizePolicy.setHeightForWidth(self.btn_calibration.sizePolicy().hasHeightForWidth())
        self.btn_calibration.setSizePolicy(sizePolicy)
        self.btn_calibration.setMinimumSize(QSize(0, 45))
        self.btn_calibration.setFont(font1)
        self.btn_calibration.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_calibration.setLayoutDirection(Qt.LeftToRight)
        self.btn_calibration.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-options-horizontal.png);")

        self.verticalLayout_8.addWidget(self.btn_calibration)

        self.btn_log = QPushButton(self.topMenu)
        self.btn_log.setObjectName(u"btn_log")
        sizePolicy.setHeightForWidth(self.btn_log.sizePolicy().hasHeightForWidth())
        self.btn_log.setSizePolicy(sizePolicy)
        self.btn_log.setMinimumSize(QSize(0, 45))
        self.btn_log.setFont(font1)
        self.btn_log.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_log.setLayoutDirection(Qt.LeftToRight)
        self.btn_log.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-bell.png);")

        self.verticalLayout_8.addWidget(self.btn_log)

        self.btn_trend = QPushButton(self.topMenu)
        self.btn_trend.setObjectName(u"btn_trend")
        sizePolicy.setHeightForWidth(self.btn_trend.sizePolicy().hasHeightForWidth())
        self.btn_trend.setSizePolicy(sizePolicy)
        self.btn_trend.setMinimumSize(QSize(0, 45))
        self.btn_trend.setFont(font1)
        self.btn_trend.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_trend.setLayoutDirection(Qt.LeftToRight)
        self.btn_trend.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-chart-line.png);")

        self.verticalLayout_8.addWidget(self.btn_trend)

        self.btn_save = QPushButton(self.topMenu)
        self.btn_save.setObjectName(u"btn_save")
        sizePolicy.setHeightForWidth(self.btn_save.sizePolicy().hasHeightForWidth())
        self.btn_save.setSizePolicy(sizePolicy)
        self.btn_save.setMinimumSize(QSize(0, 45))
        self.btn_save.setFont(font1)
        self.btn_save.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_save.setLayoutDirection(Qt.LeftToRight)
        self.btn_save.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-save.png)")

        self.verticalLayout_8.addWidget(self.btn_save)


        self.verticalMenuLayout.addWidget(self.topMenu, 0, Qt.AlignTop)

        self.bottomMenu = QFrame(self.leftMenuFrame)
        self.bottomMenu.setObjectName(u"bottomMenu")
        self.bottomMenu.setFrameShape(QFrame.NoFrame)
        self.bottomMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.bottomMenu)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.toggleLeftBox = QPushButton(self.bottomMenu)
        self.toggleLeftBox.setObjectName(u"toggleLeftBox")
        sizePolicy.setHeightForWidth(self.toggleLeftBox.sizePolicy().hasHeightForWidth())
        self.toggleLeftBox.setSizePolicy(sizePolicy)
        self.toggleLeftBox.setMinimumSize(QSize(0, 45))
        self.toggleLeftBox.setFont(font1)
        self.toggleLeftBox.setCursor(QCursor(Qt.PointingHandCursor))
        self.toggleLeftBox.setLayoutDirection(Qt.LeftToRight)
        self.toggleLeftBox.setStyleSheet(u"background-image: url(:/icons/images/icons/icon_settings.png);")

        self.verticalLayout_9.addWidget(self.toggleLeftBox)


        self.verticalMenuLayout.addWidget(self.bottomMenu, 0, Qt.AlignBottom)


        self.verticalLayout_3.addWidget(self.leftMenuFrame)


        self.appLayout.addWidget(self.leftMenuBg)

        self.extraLeftBox = QFrame(self.bgApp)
        self.extraLeftBox.setObjectName(u"extraLeftBox")
        self.extraLeftBox.setMinimumSize(QSize(0, 0))
        self.extraLeftBox.setMaximumSize(QSize(0, 16777215))
        self.extraLeftBox.setFrameShape(QFrame.NoFrame)
        self.extraLeftBox.setFrameShadow(QFrame.Raised)
        self.extraColumLayout = QVBoxLayout(self.extraLeftBox)
        self.extraColumLayout.setSpacing(0)
        self.extraColumLayout.setObjectName(u"extraColumLayout")
        self.extraColumLayout.setContentsMargins(0, 0, 0, 0)
        self.extraTopBg = QFrame(self.extraLeftBox)
        self.extraTopBg.setObjectName(u"extraTopBg")
        self.extraTopBg.setMinimumSize(QSize(0, 50))
        self.extraTopBg.setMaximumSize(QSize(16777215, 50))
        self.extraTopBg.setFrameShape(QFrame.NoFrame)
        self.extraTopBg.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.extraTopBg)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.extraTopLayout = QGridLayout()
        self.extraTopLayout.setObjectName(u"extraTopLayout")
        self.extraTopLayout.setHorizontalSpacing(10)
        self.extraTopLayout.setVerticalSpacing(0)
        self.extraTopLayout.setContentsMargins(10, -1, 10, -1)
        self.extraIcon = QFrame(self.extraTopBg)
        self.extraIcon.setObjectName(u"extraIcon")
        self.extraIcon.setMinimumSize(QSize(20, 0))
        self.extraIcon.setMaximumSize(QSize(20, 20))
        self.extraIcon.setFrameShape(QFrame.NoFrame)
        self.extraIcon.setFrameShadow(QFrame.Raised)

        self.extraTopLayout.addWidget(self.extraIcon, 0, 0, 1, 1)

        self.extraLabel = QLabel(self.extraTopBg)
        self.extraLabel.setObjectName(u"extraLabel")
        self.extraLabel.setMinimumSize(QSize(150, 0))

        self.extraTopLayout.addWidget(self.extraLabel, 0, 1, 1, 1)

        self.extraCloseColumnBtn = QPushButton(self.extraTopBg)
        self.extraCloseColumnBtn.setObjectName(u"extraCloseColumnBtn")
        self.extraCloseColumnBtn.setMinimumSize(QSize(28, 28))
        self.extraCloseColumnBtn.setMaximumSize(QSize(28, 28))
        self.extraCloseColumnBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/icons/images/icons/icon_close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.extraCloseColumnBtn.setIcon(icon)
        self.extraCloseColumnBtn.setIconSize(QSize(20, 20))

        self.extraTopLayout.addWidget(self.extraCloseColumnBtn, 0, 2, 1, 1)


        self.verticalLayout_5.addLayout(self.extraTopLayout)


        self.extraColumLayout.addWidget(self.extraTopBg)

        self.extraContent = QFrame(self.extraLeftBox)
        self.extraContent.setObjectName(u"extraContent")
        self.extraContent.setFrameShape(QFrame.NoFrame)
        self.extraContent.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.extraContent)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.extraTopMenu = QFrame(self.extraContent)
        self.extraTopMenu.setObjectName(u"extraTopMenu")
        self.extraTopMenu.setFrameShape(QFrame.NoFrame)
        self.extraTopMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.extraTopMenu)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.btn_share = QPushButton(self.extraTopMenu)
        self.btn_share.setObjectName(u"btn_share")
        sizePolicy.setHeightForWidth(self.btn_share.sizePolicy().hasHeightForWidth())
        self.btn_share.setSizePolicy(sizePolicy)
        self.btn_share.setMinimumSize(QSize(0, 45))
        self.btn_share.setFont(font1)
        self.btn_share.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_share.setLayoutDirection(Qt.LeftToRight)
        self.btn_share.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-share-boxed.png);")

        self.verticalLayout_11.addWidget(self.btn_share)

        self.btn_adjustments = QPushButton(self.extraTopMenu)
        self.btn_adjustments.setObjectName(u"btn_adjustments")
        sizePolicy.setHeightForWidth(self.btn_adjustments.sizePolicy().hasHeightForWidth())
        self.btn_adjustments.setSizePolicy(sizePolicy)
        self.btn_adjustments.setMinimumSize(QSize(0, 45))
        self.btn_adjustments.setFont(font1)
        self.btn_adjustments.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_adjustments.setLayoutDirection(Qt.LeftToRight)
        self.btn_adjustments.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-equalizer.png);")

        self.verticalLayout_11.addWidget(self.btn_adjustments)

        self.btn_more = QPushButton(self.extraTopMenu)
        self.btn_more.setObjectName(u"btn_more")
        sizePolicy.setHeightForWidth(self.btn_more.sizePolicy().hasHeightForWidth())
        self.btn_more.setSizePolicy(sizePolicy)
        self.btn_more.setMinimumSize(QSize(0, 45))
        self.btn_more.setFont(font1)
        self.btn_more.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_more.setLayoutDirection(Qt.LeftToRight)
        self.btn_more.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-layers.png);")

        self.verticalLayout_11.addWidget(self.btn_more)


        self.verticalLayout_12.addWidget(self.extraTopMenu, 0, Qt.AlignTop)

        self.extraCenter = QFrame(self.extraContent)
        self.extraCenter.setObjectName(u"extraCenter")
        self.extraCenter.setFrameShape(QFrame.NoFrame)
        self.extraCenter.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.extraCenter)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.textEdit = QTextEdit(self.extraCenter)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setMinimumSize(QSize(222, 0))
        self.textEdit.setStyleSheet(u"background: transparent;")
        self.textEdit.setFrameShape(QFrame.NoFrame)
        self.textEdit.setReadOnly(True)

        self.verticalLayout_10.addWidget(self.textEdit)


        self.verticalLayout_12.addWidget(self.extraCenter)

        self.extraBottom = QFrame(self.extraContent)
        self.extraBottom.setObjectName(u"extraBottom")
        self.extraBottom.setFrameShape(QFrame.NoFrame)
        self.extraBottom.setFrameShadow(QFrame.Raised)

        self.verticalLayout_12.addWidget(self.extraBottom)


        self.extraColumLayout.addWidget(self.extraContent)


        self.appLayout.addWidget(self.extraLeftBox)

        self.contentBox = QFrame(self.bgApp)
        self.contentBox.setObjectName(u"contentBox")
        self.contentBox.setFrameShape(QFrame.NoFrame)
        self.contentBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.contentBox)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.contentTopBg = QFrame(self.contentBox)
        self.contentTopBg.setObjectName(u"contentTopBg")
        self.contentTopBg.setMinimumSize(QSize(0, 50))
        self.contentTopBg.setMaximumSize(QSize(16777215, 50))
        self.contentTopBg.setFrameShape(QFrame.NoFrame)
        self.contentTopBg.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.contentTopBg)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 10, 0)
        self.leftBox = QFrame(self.contentTopBg)
        self.leftBox.setObjectName(u"leftBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.leftBox.sizePolicy().hasHeightForWidth())
        self.leftBox.setSizePolicy(sizePolicy1)
        self.leftBox.setFrameShape(QFrame.NoFrame)
        self.leftBox.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.leftBox)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.titleRightInfo = QLabel(self.leftBox)
        self.titleRightInfo.setObjectName(u"titleRightInfo")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.titleRightInfo.sizePolicy().hasHeightForWidth())
        self.titleRightInfo.setSizePolicy(sizePolicy2)
        self.titleRightInfo.setMaximumSize(QSize(16777215, 45))
        self.titleRightInfo.setFont(font1)
        self.titleRightInfo.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.titleRightInfo)


        self.horizontalLayout.addWidget(self.leftBox)

        self.rightButtons = QFrame(self.contentTopBg)
        self.rightButtons.setObjectName(u"rightButtons")
        self.rightButtons.setMinimumSize(QSize(0, 28))
        self.rightButtons.setFrameShape(QFrame.NoFrame)
        self.rightButtons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.rightButtons)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.settingsTopBtn = QPushButton(self.rightButtons)
        self.settingsTopBtn.setObjectName(u"settingsTopBtn")
        self.settingsTopBtn.setMinimumSize(QSize(28, 28))
        self.settingsTopBtn.setMaximumSize(QSize(28, 28))
        self.settingsTopBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/icons/images/icons/icon_settings.png", QSize(), QIcon.Normal, QIcon.Off)
        self.settingsTopBtn.setIcon(icon1)
        self.settingsTopBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.settingsTopBtn)

        self.minimizeAppBtn = QPushButton(self.rightButtons)
        self.minimizeAppBtn.setObjectName(u"minimizeAppBtn")
        self.minimizeAppBtn.setMinimumSize(QSize(28, 28))
        self.minimizeAppBtn.setMaximumSize(QSize(28, 28))
        self.minimizeAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/icons/images/icons/icon_minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimizeAppBtn.setIcon(icon2)
        self.minimizeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.minimizeAppBtn)

        self.maximizeRestoreAppBtn = QPushButton(self.rightButtons)
        self.maximizeRestoreAppBtn.setObjectName(u"maximizeRestoreAppBtn")
        self.maximizeRestoreAppBtn.setMinimumSize(QSize(28, 28))
        self.maximizeRestoreAppBtn.setMaximumSize(QSize(28, 28))
        font3 = QFont()
        font3.setPointSize(12)
        font3.setBold(False)
        font3.setItalic(False)
        font3.setStyleStrategy(QFont.PreferDefault)
        self.maximizeRestoreAppBtn.setFont(font3)
        self.maximizeRestoreAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/icons/images/icons/icon_maximize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.maximizeRestoreAppBtn.setIcon(icon3)
        self.maximizeRestoreAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.maximizeRestoreAppBtn)

        self.closeAppBtn = QPushButton(self.rightButtons)
        self.closeAppBtn.setObjectName(u"closeAppBtn")
        self.closeAppBtn.setMinimumSize(QSize(28, 28))
        self.closeAppBtn.setMaximumSize(QSize(28, 28))
        self.closeAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.closeAppBtn.setIcon(icon)
        self.closeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.closeAppBtn)


        self.horizontalLayout.addWidget(self.rightButtons, 0, Qt.AlignRight)


        self.verticalLayout_2.addWidget(self.contentTopBg)

        self.contentBottom = QFrame(self.contentBox)
        self.contentBottom.setObjectName(u"contentBottom")
        self.contentBottom.setFrameShape(QFrame.NoFrame)
        self.contentBottom.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.contentBottom)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.content = QFrame(self.contentBottom)
        self.content.setObjectName(u"content")
        self.content.setFrameShape(QFrame.NoFrame)
        self.content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.content)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.pagesContainer = QFrame(self.content)
        self.pagesContainer.setObjectName(u"pagesContainer")
        self.pagesContainer.setStyleSheet(u"")
        self.pagesContainer.setFrameShape(QFrame.NoFrame)
        self.pagesContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.pagesContainer)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(10, 10, 10, 10)
        self.stackedWidget = QStackedWidget(self.pagesContainer)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setFont(font1)
        self.stackedWidget.setStyleSheet(u"background: transparent;")
        self.home = QWidget()
        self.home.setObjectName(u"home")
        self.home.setStyleSheet(u"")
        self.gridLayout_home = QGridLayout(self.home)
        self.gridLayout_home.setObjectName(u"gridLayout_home")
        self.gridLayout_home.setVerticalSpacing(5)
        self.horizontalLayout_ch6 = QHBoxLayout()
        self.horizontalLayout_ch6.setSpacing(5)
        self.horizontalLayout_ch6.setObjectName(u"horizontalLayout_ch6")
        self.label_ch6 = QLabel(self.home)
        self.label_ch6.setObjectName(u"label_ch6")

        self.horizontalLayout_ch6.addWidget(self.label_ch6)

        self.lineEdit_ch6 = QLineEdit(self.home)
        self.lineEdit_ch6.setObjectName(u"lineEdit_ch6")
        self.lineEdit_ch6.setReadOnly(True)

        self.horizontalLayout_ch6.addWidget(self.lineEdit_ch6)

        self.label_ch6scale = QLabel(self.home)
        self.label_ch6scale.setObjectName(u"label_ch6scale")

        self.horizontalLayout_ch6.addWidget(self.label_ch6scale, 0, Qt.AlignHCenter)

        self.horizontalLayout_ch6check = QHBoxLayout()
        self.horizontalLayout_ch6check.setSpacing(5)
        self.horizontalLayout_ch6check.setObjectName(u"horizontalLayout_ch6check")
        self.frame_ch6 = QFrame(self.home)
        self.frame_ch6.setObjectName(u"frame_ch6")
        self.frame_ch6.setFrameShape(QFrame.StyledPanel)
        self.frame_ch6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_ch6)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.radioButton_ch6v = QRadioButton(self.frame_ch6)
        self.radioButton_ch6v.setObjectName(u"radioButton_ch6v")

        self.horizontalLayout_14.addWidget(self.radioButton_ch6v, 0, Qt.AlignHCenter)

        self.radioButton_ch6i = QRadioButton(self.frame_ch6)
        self.radioButton_ch6i.setObjectName(u"radioButton_ch6i")

        self.horizontalLayout_14.addWidget(self.radioButton_ch6i, 0, Qt.AlignHCenter)


        self.horizontalLayout_ch6check.addWidget(self.frame_ch6)


        self.horizontalLayout_ch6.addLayout(self.horizontalLayout_ch6check)

        self.horizontalLayout_ch6.setStretch(0, 1)
        self.horizontalLayout_ch6.setStretch(1, 2)
        self.horizontalLayout_ch6.setStretch(2, 1)
        self.horizontalLayout_ch6.setStretch(3, 2)

        self.gridLayout_home.addLayout(self.horizontalLayout_ch6, 6, 0, 1, 1)

        self.horizontalLayout_ch8 = QHBoxLayout()
        self.horizontalLayout_ch8.setSpacing(5)
        self.horizontalLayout_ch8.setObjectName(u"horizontalLayout_ch8")
        self.label_ch8 = QLabel(self.home)
        self.label_ch8.setObjectName(u"label_ch8")

        self.horizontalLayout_ch8.addWidget(self.label_ch8)

        self.lineEdit_ch8 = QLineEdit(self.home)
        self.lineEdit_ch8.setObjectName(u"lineEdit_ch8")
        self.lineEdit_ch8.setReadOnly(True)

        self.horizontalLayout_ch8.addWidget(self.lineEdit_ch8)

        self.label_ch8scale = QLabel(self.home)
        self.label_ch8scale.setObjectName(u"label_ch8scale")

        self.horizontalLayout_ch8.addWidget(self.label_ch8scale, 0, Qt.AlignHCenter)

        self.horizontalLayout_ch8check = QHBoxLayout()
        self.horizontalLayout_ch8check.setSpacing(5)
        self.horizontalLayout_ch8check.setObjectName(u"horizontalLayout_ch8check")
        self.frame_ch8 = QFrame(self.home)
        self.frame_ch8.setObjectName(u"frame_ch8")
        self.frame_ch8.setFrameShape(QFrame.StyledPanel)
        self.frame_ch8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_ch8)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.radioButton_ch8v = QRadioButton(self.frame_ch8)
        self.radioButton_ch8v.setObjectName(u"radioButton_ch8v")

        self.horizontalLayout_16.addWidget(self.radioButton_ch8v, 0, Qt.AlignHCenter)

        self.radioButton_ch8i = QRadioButton(self.frame_ch8)
        self.radioButton_ch8i.setObjectName(u"radioButton_ch8i")

        self.horizontalLayout_16.addWidget(self.radioButton_ch8i, 0, Qt.AlignHCenter)


        self.horizontalLayout_ch8check.addWidget(self.frame_ch8)


        self.horizontalLayout_ch8.addLayout(self.horizontalLayout_ch8check)

        self.horizontalLayout_ch8.setStretch(0, 1)
        self.horizontalLayout_ch8.setStretch(1, 2)
        self.horizontalLayout_ch8.setStretch(2, 1)
        self.horizontalLayout_ch8.setStretch(3, 2)

        self.gridLayout_home.addLayout(self.horizontalLayout_ch8, 8, 0, 1, 1)

        self.horizontalLayout_ch7 = QHBoxLayout()
        self.horizontalLayout_ch7.setSpacing(5)
        self.horizontalLayout_ch7.setObjectName(u"horizontalLayout_ch7")
        self.label_ch7 = QLabel(self.home)
        self.label_ch7.setObjectName(u"label_ch7")

        self.horizontalLayout_ch7.addWidget(self.label_ch7)

        self.lineEdit_ch7 = QLineEdit(self.home)
        self.lineEdit_ch7.setObjectName(u"lineEdit_ch7")
        self.lineEdit_ch7.setReadOnly(True)

        self.horizontalLayout_ch7.addWidget(self.lineEdit_ch7)

        self.label_ch7scale = QLabel(self.home)
        self.label_ch7scale.setObjectName(u"label_ch7scale")

        self.horizontalLayout_ch7.addWidget(self.label_ch7scale, 0, Qt.AlignHCenter)

        self.horizontalLayout_ch7check = QHBoxLayout()
        self.horizontalLayout_ch7check.setSpacing(5)
        self.horizontalLayout_ch7check.setObjectName(u"horizontalLayout_ch7check")
        self.frame_ch7 = QFrame(self.home)
        self.frame_ch7.setObjectName(u"frame_ch7")
        self.frame_ch7.setFrameShape(QFrame.StyledPanel)
        self.frame_ch7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_ch7)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.radioButton_ch7v = QRadioButton(self.frame_ch7)
        self.radioButton_ch7v.setObjectName(u"radioButton_ch7v")

        self.horizontalLayout_15.addWidget(self.radioButton_ch7v, 0, Qt.AlignHCenter)

        self.radioButton_ch7i = QRadioButton(self.frame_ch7)
        self.radioButton_ch7i.setObjectName(u"radioButton_ch7i")

        self.horizontalLayout_15.addWidget(self.radioButton_ch7i, 0, Qt.AlignHCenter)


        self.horizontalLayout_ch7check.addWidget(self.frame_ch7)


        self.horizontalLayout_ch7.addLayout(self.horizontalLayout_ch7check)

        self.horizontalLayout_ch7.setStretch(0, 1)
        self.horizontalLayout_ch7.setStretch(1, 2)
        self.horizontalLayout_ch7.setStretch(2, 1)
        self.horizontalLayout_ch7.setStretch(3, 2)

        self.gridLayout_home.addLayout(self.horizontalLayout_ch7, 7, 0, 1, 1)

        self.horizontalLayout_ch5 = QHBoxLayout()
        self.horizontalLayout_ch5.setSpacing(5)
        self.horizontalLayout_ch5.setObjectName(u"horizontalLayout_ch5")
        self.label_ch5 = QLabel(self.home)
        self.label_ch5.setObjectName(u"label_ch5")

        self.horizontalLayout_ch5.addWidget(self.label_ch5)

        self.lineEdit_ch5 = QLineEdit(self.home)
        self.lineEdit_ch5.setObjectName(u"lineEdit_ch5")
        self.lineEdit_ch5.setReadOnly(True)

        self.horizontalLayout_ch5.addWidget(self.lineEdit_ch5)

        self.label_ch5scale = QLabel(self.home)
        self.label_ch5scale.setObjectName(u"label_ch5scale")

        self.horizontalLayout_ch5.addWidget(self.label_ch5scale, 0, Qt.AlignHCenter)

        self.horizontalLayout_ch5check = QHBoxLayout()
        self.horizontalLayout_ch5check.setSpacing(5)
        self.horizontalLayout_ch5check.setObjectName(u"horizontalLayout_ch5check")
        self.frame_ch5 = QFrame(self.home)
        self.frame_ch5.setObjectName(u"frame_ch5")
        self.frame_ch5.setFrameShape(QFrame.StyledPanel)
        self.frame_ch5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_ch5)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.radioButton_ch5v = QRadioButton(self.frame_ch5)
        self.radioButton_ch5v.setObjectName(u"radioButton_ch5v")

        self.horizontalLayout_13.addWidget(self.radioButton_ch5v, 0, Qt.AlignHCenter)

        self.radioButton_ch5i = QRadioButton(self.frame_ch5)
        self.radioButton_ch5i.setObjectName(u"radioButton_ch5i")

        self.horizontalLayout_13.addWidget(self.radioButton_ch5i, 0, Qt.AlignHCenter)


        self.horizontalLayout_ch5check.addWidget(self.frame_ch5)


        self.horizontalLayout_ch5.addLayout(self.horizontalLayout_ch5check)

        self.horizontalLayout_ch5.setStretch(0, 1)
        self.horizontalLayout_ch5.setStretch(1, 2)
        self.horizontalLayout_ch5.setStretch(2, 1)
        self.horizontalLayout_ch5.setStretch(3, 2)

        self.gridLayout_home.addLayout(self.horizontalLayout_ch5, 5, 0, 1, 1)

        self.horizontalLayout_ch2 = QHBoxLayout()
        self.horizontalLayout_ch2.setSpacing(5)
        self.horizontalLayout_ch2.setObjectName(u"horizontalLayout_ch2")
        self.label_ch2 = QLabel(self.home)
        self.label_ch2.setObjectName(u"label_ch2")

        self.horizontalLayout_ch2.addWidget(self.label_ch2)

        self.lineEdit_ch2 = QLineEdit(self.home)
        self.lineEdit_ch2.setObjectName(u"lineEdit_ch2")
        self.lineEdit_ch2.setReadOnly(True)

        self.horizontalLayout_ch2.addWidget(self.lineEdit_ch2)

        self.label_ch2scale = QLabel(self.home)
        self.label_ch2scale.setObjectName(u"label_ch2scale")
        self.label_ch2scale.setFrameShape(QFrame.NoFrame)

        self.horizontalLayout_ch2.addWidget(self.label_ch2scale, 0, Qt.AlignHCenter)

        self.horizontalLayout_ch2check = QHBoxLayout()
        self.horizontalLayout_ch2check.setSpacing(5)
        self.horizontalLayout_ch2check.setObjectName(u"horizontalLayout_ch2check")
        self.frame_ch2 = QFrame(self.home)
        self.frame_ch2.setObjectName(u"frame_ch2")
        self.frame_ch2.setFrameShape(QFrame.StyledPanel)
        self.frame_ch2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_ch2)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.radioButton_ch2v = QRadioButton(self.frame_ch2)
        self.radioButton_ch2v.setObjectName(u"radioButton_ch2v")

        self.horizontalLayout_7.addWidget(self.radioButton_ch2v, 0, Qt.AlignHCenter)

        self.radioButton_ch2i = QRadioButton(self.frame_ch2)
        self.radioButton_ch2i.setObjectName(u"radioButton_ch2i")

        self.horizontalLayout_7.addWidget(self.radioButton_ch2i, 0, Qt.AlignHCenter)


        self.horizontalLayout_ch2check.addWidget(self.frame_ch2)


        self.horizontalLayout_ch2.addLayout(self.horizontalLayout_ch2check)

        self.horizontalLayout_ch2.setStretch(0, 1)
        self.horizontalLayout_ch2.setStretch(1, 2)
        self.horizontalLayout_ch2.setStretch(2, 1)
        self.horizontalLayout_ch2.setStretch(3, 2)

        self.gridLayout_home.addLayout(self.horizontalLayout_ch2, 2, 0, 1, 1)

        self.horizontalLayout_ch3 = QHBoxLayout()
        self.horizontalLayout_ch3.setSpacing(5)
        self.horizontalLayout_ch3.setObjectName(u"horizontalLayout_ch3")
        self.label_ch3 = QLabel(self.home)
        self.label_ch3.setObjectName(u"label_ch3")

        self.horizontalLayout_ch3.addWidget(self.label_ch3)

        self.lineEdit_ch3 = QLineEdit(self.home)
        self.lineEdit_ch3.setObjectName(u"lineEdit_ch3")
        self.lineEdit_ch3.setReadOnly(True)

        self.horizontalLayout_ch3.addWidget(self.lineEdit_ch3)

        self.label_ch3scale = QLabel(self.home)
        self.label_ch3scale.setObjectName(u"label_ch3scale")

        self.horizontalLayout_ch3.addWidget(self.label_ch3scale, 0, Qt.AlignHCenter)

        self.horizontalLayout_ch3check = QHBoxLayout()
        self.horizontalLayout_ch3check.setSpacing(5)
        self.horizontalLayout_ch3check.setObjectName(u"horizontalLayout_ch3check")
        self.frame_ch3 = QFrame(self.home)
        self.frame_ch3.setObjectName(u"frame_ch3")
        self.frame_ch3.setFrameShape(QFrame.StyledPanel)
        self.frame_ch3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_ch3)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.radioButton_ch3v = QRadioButton(self.frame_ch3)
        self.radioButton_ch3v.setObjectName(u"radioButton_ch3v")

        self.horizontalLayout_8.addWidget(self.radioButton_ch3v, 0, Qt.AlignHCenter)

        self.radioButton_ch3i = QRadioButton(self.frame_ch3)
        self.radioButton_ch3i.setObjectName(u"radioButton_ch3i")

        self.horizontalLayout_8.addWidget(self.radioButton_ch3i, 0, Qt.AlignHCenter)


        self.horizontalLayout_ch3check.addWidget(self.frame_ch3)


        self.horizontalLayout_ch3.addLayout(self.horizontalLayout_ch3check)

        self.horizontalLayout_ch3.setStretch(0, 1)
        self.horizontalLayout_ch3.setStretch(1, 2)
        self.horizontalLayout_ch3.setStretch(2, 1)
        self.horizontalLayout_ch3.setStretch(3, 2)

        self.gridLayout_home.addLayout(self.horizontalLayout_ch3, 3, 0, 1, 1)

        self.horizontalLayout_ch1 = QHBoxLayout()
        self.horizontalLayout_ch1.setSpacing(5)
        self.horizontalLayout_ch1.setObjectName(u"horizontalLayout_ch1")
        self.label_ch1 = QLabel(self.home)
        self.label_ch1.setObjectName(u"label_ch1")

        self.horizontalLayout_ch1.addWidget(self.label_ch1)

        self.lineEdit_ch1 = QLineEdit(self.home)
        self.lineEdit_ch1.setObjectName(u"lineEdit_ch1")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.lineEdit_ch1.sizePolicy().hasHeightForWidth())
        self.lineEdit_ch1.setSizePolicy(sizePolicy3)
        self.lineEdit_ch1.setReadOnly(True)

        self.horizontalLayout_ch1.addWidget(self.lineEdit_ch1)

        self.label_ch1scale = QLabel(self.home)
        self.label_ch1scale.setObjectName(u"label_ch1scale")

        self.horizontalLayout_ch1.addWidget(self.label_ch1scale, 0, Qt.AlignHCenter)

        self.horizontalLayout_ch1check = QHBoxLayout()
        self.horizontalLayout_ch1check.setSpacing(5)
        self.horizontalLayout_ch1check.setObjectName(u"horizontalLayout_ch1check")
        self.frame_ch1 = QFrame(self.home)
        self.frame_ch1.setObjectName(u"frame_ch1")
        self.frame_ch1.setFrameShape(QFrame.StyledPanel)
        self.frame_ch1.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_ch1)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.radioButton_ch1v = QRadioButton(self.frame_ch1)
        self.radioButton_ch1v.setObjectName(u"radioButton_ch1v")

        self.horizontalLayout_6.addWidget(self.radioButton_ch1v, 0, Qt.AlignHCenter)

        self.radioButton_ch1i = QRadioButton(self.frame_ch1)
        self.radioButton_ch1i.setObjectName(u"radioButton_ch1i")

        self.horizontalLayout_6.addWidget(self.radioButton_ch1i, 0, Qt.AlignHCenter)


        self.horizontalLayout_ch1check.addWidget(self.frame_ch1)


        self.horizontalLayout_ch1.addLayout(self.horizontalLayout_ch1check)

        self.horizontalLayout_ch1.setStretch(0, 1)
        self.horizontalLayout_ch1.setStretch(1, 2)
        self.horizontalLayout_ch1.setStretch(2, 1)
        self.horizontalLayout_ch1.setStretch(3, 2)

        self.gridLayout_home.addLayout(self.horizontalLayout_ch1, 1, 0, 1, 1)

        self.horizontalLayout_ch4 = QHBoxLayout()
        self.horizontalLayout_ch4.setSpacing(5)
        self.horizontalLayout_ch4.setObjectName(u"horizontalLayout_ch4")
        self.label_ch4 = QLabel(self.home)
        self.label_ch4.setObjectName(u"label_ch4")

        self.horizontalLayout_ch4.addWidget(self.label_ch4)

        self.lineEdit_ch4 = QLineEdit(self.home)
        self.lineEdit_ch4.setObjectName(u"lineEdit_ch4")
        self.lineEdit_ch4.setReadOnly(True)

        self.horizontalLayout_ch4.addWidget(self.lineEdit_ch4)

        self.label_ch4scale = QLabel(self.home)
        self.label_ch4scale.setObjectName(u"label_ch4scale")

        self.horizontalLayout_ch4.addWidget(self.label_ch4scale, 0, Qt.AlignHCenter)

        self.horizontalLayout_ch4check = QHBoxLayout()
        self.horizontalLayout_ch4check.setSpacing(5)
        self.horizontalLayout_ch4check.setObjectName(u"horizontalLayout_ch4check")
        self.frame_ch4 = QFrame(self.home)
        self.frame_ch4.setObjectName(u"frame_ch4")
        self.frame_ch4.setFrameShape(QFrame.StyledPanel)
        self.frame_ch4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_ch4)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.radioButton_ch4v = QRadioButton(self.frame_ch4)
        self.radioButton_ch4v.setObjectName(u"radioButton_ch4v")

        self.horizontalLayout_10.addWidget(self.radioButton_ch4v, 0, Qt.AlignHCenter)

        self.radioButton_ch4i = QRadioButton(self.frame_ch4)
        self.radioButton_ch4i.setObjectName(u"radioButton_ch4i")

        self.horizontalLayout_10.addWidget(self.radioButton_ch4i, 0, Qt.AlignHCenter)


        self.horizontalLayout_ch4check.addWidget(self.frame_ch4)


        self.horizontalLayout_ch4.addLayout(self.horizontalLayout_ch4check)

        self.horizontalLayout_ch4.setStretch(0, 1)
        self.horizontalLayout_ch4.setStretch(1, 2)
        self.horizontalLayout_ch4.setStretch(2, 1)
        self.horizontalLayout_ch4.setStretch(3, 2)

        self.gridLayout_home.addLayout(self.horizontalLayout_ch4, 4, 0, 1, 1)

        self.horizontalLayout_connection = QHBoxLayout()
        self.horizontalLayout_connection.setSpacing(50)
        self.horizontalLayout_connection.setObjectName(u"horizontalLayout_connection")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.horizontalLayout_connection.addItem(self.horizontalSpacer_2)

        self.pushButton_connect = QPushButton(self.home)
        self.pushButton_connect.setObjectName(u"pushButton_connect")
        sizePolicy4 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.pushButton_connect.sizePolicy().hasHeightForWidth())
        self.pushButton_connect.setSizePolicy(sizePolicy4)

        self.horizontalLayout_connection.addWidget(self.pushButton_connect)

        self.pushButton_disconnect = QPushButton(self.home)
        self.pushButton_disconnect.setObjectName(u"pushButton_disconnect")
        sizePolicy4.setHeightForWidth(self.pushButton_disconnect.sizePolicy().hasHeightForWidth())
        self.pushButton_disconnect.setSizePolicy(sizePolicy4)

        self.horizontalLayout_connection.addWidget(self.pushButton_disconnect)

        self.checkBox_65535 = QCheckBox(self.home)
        self.checkBox_65535.setObjectName(u"checkBox_65535")
        sizePolicy5 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Maximum)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.checkBox_65535.sizePolicy().hasHeightForWidth())
        self.checkBox_65535.setSizePolicy(sizePolicy5)
        self.checkBox_65535.setTristate(False)

        self.horizontalLayout_connection.addWidget(self.checkBox_65535)

        self.horizontalLayout_connection.setStretch(0, 1)
        self.horizontalLayout_connection.setStretch(1, 2)
        self.horizontalLayout_connection.setStretch(2, 2)

        self.gridLayout_home.addLayout(self.horizontalLayout_connection, 9, 0, 1, 1)

        self.horizontalLayout_vi = QHBoxLayout()
        self.horizontalLayout_vi.setSpacing(0)
        self.horizontalLayout_vi.setObjectName(u"horizontalLayout_vi")
        self.label_model = QLabel(self.home)
        self.label_model.setObjectName(u"label_model")

        self.horizontalLayout_vi.addWidget(self.label_model, 0, Qt.AlignLeft)

        self.label_deviceModel = QLabel(self.home)
        self.label_deviceModel.setObjectName(u"label_deviceModel")

        self.horizontalLayout_vi.addWidget(self.label_deviceModel, 0, Qt.AlignHCenter)

        self.label_vol = QLabel(self.home)
        self.label_vol.setObjectName(u"label_vol")
        sizePolicy6 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.label_vol.sizePolicy().hasHeightForWidth())
        self.label_vol.setSizePolicy(sizePolicy6)
        self.label_vol.setFont(font1)

        self.horizontalLayout_vi.addWidget(self.label_vol, 0, Qt.AlignHCenter)

        self.label_cur = QLabel(self.home)
        self.label_cur.setObjectName(u"label_cur")
        sizePolicy6.setHeightForWidth(self.label_cur.sizePolicy().hasHeightForWidth())
        self.label_cur.setSizePolicy(sizePolicy6)

        self.horizontalLayout_vi.addWidget(self.label_cur, 0, Qt.AlignHCenter)

        self.horizontalLayout_vi.setStretch(0, 1)
        self.horizontalLayout_vi.setStretch(1, 3)
        self.horizontalLayout_vi.setStretch(2, 1)
        self.horizontalLayout_vi.setStretch(3, 1)

        self.gridLayout_home.addLayout(self.horizontalLayout_vi, 0, 0, 1, 1)

        self.gridLayout_home.setRowStretch(0, 2)
        self.gridLayout_home.setRowStretch(1, 2)
        self.gridLayout_home.setRowStretch(2, 2)
        self.gridLayout_home.setRowStretch(3, 2)
        self.gridLayout_home.setRowStretch(4, 2)
        self.gridLayout_home.setRowStretch(5, 2)
        self.gridLayout_home.setRowStretch(6, 2)
        self.gridLayout_home.setRowStretch(7, 2)
        self.gridLayout_home.setRowStretch(8, 2)
        self.gridLayout_home.setRowStretch(9, 2)
        self.gridLayout_home.setRowMinimumHeight(0, 30)
        self.gridLayout_home.setRowMinimumHeight(1, 30)
        self.gridLayout_home.setRowMinimumHeight(2, 30)
        self.gridLayout_home.setRowMinimumHeight(3, 30)
        self.gridLayout_home.setRowMinimumHeight(4, 30)
        self.gridLayout_home.setRowMinimumHeight(5, 30)
        self.gridLayout_home.setRowMinimumHeight(6, 30)
        self.gridLayout_home.setRowMinimumHeight(7, 30)
        self.gridLayout_home.setRowMinimumHeight(8, 30)
        self.gridLayout_home.setRowMinimumHeight(9, 30)
        self.stackedWidget.addWidget(self.home)
        self.setting = QWidget()
        self.setting.setObjectName(u"setting")
        self.gridLayout_setting = QGridLayout(self.setting)
        self.gridLayout_setting.setObjectName(u"gridLayout_setting")
        self.horizontalLayout_ch6Scale = QHBoxLayout()
        self.horizontalLayout_ch6Scale.setSpacing(10)
        self.horizontalLayout_ch6Scale.setObjectName(u"horizontalLayout_ch6Scale")
        self.comboBox_ch6scale = QComboBox(self.setting)
        self.comboBox_ch6scale.addItem("")
        self.comboBox_ch6scale.addItem("")
        self.comboBox_ch6scale.addItem("")
        self.comboBox_ch6scale.setObjectName(u"comboBox_ch6scale")
        sizePolicy7 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.comboBox_ch6scale.sizePolicy().hasHeightForWidth())
        self.comboBox_ch6scale.setSizePolicy(sizePolicy7)

        self.horizontalLayout_ch6Scale.addWidget(self.comboBox_ch6scale)


        self.gridLayout_setting.addLayout(self.horizontalLayout_ch6Scale, 6, 3, 1, 1)

        self.gridLayout_scalesMinMax = QGridLayout()
        self.gridLayout_scalesMinMax.setObjectName(u"gridLayout_scalesMinMax")
        self.label_minScale = QLabel(self.setting)
        self.label_minScale.setObjectName(u"label_minScale")
        sizePolicy6.setHeightForWidth(self.label_minScale.sizePolicy().hasHeightForWidth())
        self.label_minScale.setSizePolicy(sizePolicy6)

        self.gridLayout_scalesMinMax.addWidget(self.label_minScale, 1, 0, 1, 1, Qt.AlignHCenter)

        self.label_maxScale = QLabel(self.setting)
        self.label_maxScale.setObjectName(u"label_maxScale")
        sizePolicy6.setHeightForWidth(self.label_maxScale.sizePolicy().hasHeightForWidth())
        self.label_maxScale.setSizePolicy(sizePolicy6)

        self.gridLayout_scalesMinMax.addWidget(self.label_maxScale, 1, 1, 1, 1, Qt.AlignHCenter)

        self.label_vScale = QLabel(self.setting)
        self.label_vScale.setObjectName(u"label_vScale")
        sizePolicy6.setHeightForWidth(self.label_vScale.sizePolicy().hasHeightForWidth())
        self.label_vScale.setSizePolicy(sizePolicy6)
        font4 = QFont()
        font4.setPointSize(12)
        font4.setBold(False)
        font4.setItalic(False)
        font4.setUnderline(False)
        self.label_vScale.setFont(font4)

        self.gridLayout_scalesMinMax.addWidget(self.label_vScale, 0, 0, 1, 2, Qt.AlignHCenter)


        self.gridLayout_setting.addLayout(self.gridLayout_scalesMinMax, 0, 2, 1, 1)

        self.horizontalLayout_ch8Scale = QHBoxLayout()
        self.horizontalLayout_ch8Scale.setSpacing(10)
        self.horizontalLayout_ch8Scale.setObjectName(u"horizontalLayout_ch8Scale")
        self.comboBox_ch8scale = QComboBox(self.setting)
        self.comboBox_ch8scale.addItem("")
        self.comboBox_ch8scale.addItem("")
        self.comboBox_ch8scale.addItem("")
        self.comboBox_ch8scale.setObjectName(u"comboBox_ch8scale")
        sizePolicy7.setHeightForWidth(self.comboBox_ch8scale.sizePolicy().hasHeightForWidth())
        self.comboBox_ch8scale.setSizePolicy(sizePolicy7)

        self.horizontalLayout_ch8Scale.addWidget(self.comboBox_ch8scale)


        self.gridLayout_setting.addLayout(self.horizontalLayout_ch8Scale, 8, 3, 1, 1)

        self.horizontalLayout_ch8ScaleMinMax = QHBoxLayout()
        self.horizontalLayout_ch8ScaleMinMax.setSpacing(10)
        self.horizontalLayout_ch8ScaleMinMax.setObjectName(u"horizontalLayout_ch8ScaleMinMax")
        self.lineEdit_ch8vLow = QLineEdit(self.setting)
        self.lineEdit_ch8vLow.setObjectName(u"lineEdit_ch8vLow")
        sizePolicy7.setHeightForWidth(self.lineEdit_ch8vLow.sizePolicy().hasHeightForWidth())
        self.lineEdit_ch8vLow.setSizePolicy(sizePolicy7)

        self.horizontalLayout_ch8ScaleMinMax.addWidget(self.lineEdit_ch8vLow)

        self.label_ch8vScaleDash = QLabel(self.setting)
        self.label_ch8vScaleDash.setObjectName(u"label_ch8vScaleDash")

        self.horizontalLayout_ch8ScaleMinMax.addWidget(self.label_ch8vScaleDash)

        self.lineEdit_ch8vHigh = QLineEdit(self.setting)
        self.lineEdit_ch8vHigh.setObjectName(u"lineEdit_ch8vHigh")
        sizePolicy7.setHeightForWidth(self.lineEdit_ch8vHigh.sizePolicy().hasHeightForWidth())
        self.lineEdit_ch8vHigh.setSizePolicy(sizePolicy7)

        self.horizontalLayout_ch8ScaleMinMax.addWidget(self.lineEdit_ch8vHigh)


        self.gridLayout_setting.addLayout(self.horizontalLayout_ch8ScaleMinMax, 8, 2, 1, 1)

        self.horizontalLayout_timeout = QHBoxLayout()
        self.horizontalLayout_timeout.setObjectName(u"horizontalLayout_timeout")
        self.label_timeout = QLabel(self.setting)
        self.label_timeout.setObjectName(u"label_timeout")

        self.horizontalLayout_timeout.addWidget(self.label_timeout)

        self.lineEdit_timeout = QLineEdit(self.setting)
        self.lineEdit_timeout.setObjectName(u"lineEdit_timeout")
        sizePolicy6.setHeightForWidth(self.lineEdit_timeout.sizePolicy().hasHeightForWidth())
        self.lineEdit_timeout.setSizePolicy(sizePolicy6)

        self.horizontalLayout_timeout.addWidget(self.lineEdit_timeout)

        self.horizontalLayout_timeout.setStretch(0, 1)
        self.horizontalLayout_timeout.setStretch(1, 1)

        self.gridLayout_setting.addLayout(self.horizontalLayout_timeout, 5, 0, 1, 1)

        self.label_ch1Setting = QLabel(self.setting)
        self.label_ch1Setting.setObjectName(u"label_ch1Setting")

        self.gridLayout_setting.addWidget(self.label_ch1Setting, 1, 1, 1, 1, Qt.AlignRight)

        self.horizontalLayout_ch4ScaleMinMax = QHBoxLayout()
        self.horizontalLayout_ch4ScaleMinMax.setSpacing(10)
        self.horizontalLayout_ch4ScaleMinMax.setObjectName(u"horizontalLayout_ch4ScaleMinMax")
        self.lineEdit_ch4vLow = QLineEdit(self.setting)
        self.lineEdit_ch4vLow.setObjectName(u"lineEdit_ch4vLow")
        sizePolicy7.setHeightForWidth(self.lineEdit_ch4vLow.sizePolicy().hasHeightForWidth())
        self.lineEdit_ch4vLow.setSizePolicy(sizePolicy7)

        self.horizontalLayout_ch4ScaleMinMax.addWidget(self.lineEdit_ch4vLow)

        self.label_ch4vScaleDash = QLabel(self.setting)
        self.label_ch4vScaleDash.setObjectName(u"label_ch4vScaleDash")

        self.horizontalLayout_ch4ScaleMinMax.addWidget(self.label_ch4vScaleDash)

        self.lineEdit_ch4vHigh = QLineEdit(self.setting)
        self.lineEdit_ch4vHigh.setObjectName(u"lineEdit_ch4vHigh")
        sizePolicy7.setHeightForWidth(self.lineEdit_ch4vHigh.sizePolicy().hasHeightForWidth())
        self.lineEdit_ch4vHigh.setSizePolicy(sizePolicy7)

        self.horizontalLayout_ch4ScaleMinMax.addWidget(self.lineEdit_ch4vHigh)


        self.gridLayout_setting.addLayout(self.horizontalLayout_ch4ScaleMinMax, 4, 2, 1, 1)

        self.horizontalLayout_ch7Scale = QHBoxLayout()
        self.horizontalLayout_ch7Scale.setSpacing(10)
        self.horizontalLayout_ch7Scale.setObjectName(u"horizontalLayout_ch7Scale")
        self.comboBox_ch7scale = QComboBox(self.setting)
        self.comboBox_ch7scale.addItem("")
        self.comboBox_ch7scale.addItem("")
        self.comboBox_ch7scale.addItem("")
        self.comboBox_ch7scale.setObjectName(u"comboBox_ch7scale")
        sizePolicy7.setHeightForWidth(self.comboBox_ch7scale.sizePolicy().hasHeightForWidth())
        self.comboBox_ch7scale.setSizePolicy(sizePolicy7)

        self.horizontalLayout_ch7Scale.addWidget(self.comboBox_ch7scale)


        self.gridLayout_setting.addLayout(self.horizontalLayout_ch7Scale, 7, 3, 1, 1)

        self.label_ch3Setting = QLabel(self.setting)
        self.label_ch3Setting.setObjectName(u"label_ch3Setting")

        self.gridLayout_setting.addWidget(self.label_ch3Setting, 3, 1, 1, 1, Qt.AlignRight)

        self.horizontalLayout_unitID = QHBoxLayout()
        self.horizontalLayout_unitID.setObjectName(u"horizontalLayout_unitID")
        self.label_unitID = QLabel(self.setting)
        self.label_unitID.setObjectName(u"label_unitID")

        self.horizontalLayout_unitID.addWidget(self.label_unitID)

        self.lineEdit_unitID = QLineEdit(self.setting)
        self.lineEdit_unitID.setObjectName(u"lineEdit_unitID")
        sizePolicy6.setHeightForWidth(self.lineEdit_unitID.sizePolicy().hasHeightForWidth())
        self.lineEdit_unitID.setSizePolicy(sizePolicy6)

        self.horizontalLayout_unitID.addWidget(self.lineEdit_unitID)

        self.horizontalLayout_unitID.setStretch(0, 1)
        self.horizontalLayout_unitID.setStretch(1, 1)

        self.gridLayout_setting.addLayout(self.horizontalLayout_unitID, 3, 0, 1, 1)

        self.horizontalLayout_ch5ScaleMinMax = QHBoxLayout()
        self.horizontalLayout_ch5ScaleMinMax.setSpacing(10)
        self.horizontalLayout_ch5ScaleMinMax.setObjectName(u"horizontalLayout_ch5ScaleMinMax")
        self.lineEdit_ch5vLow = QLineEdit(self.setting)
        self.lineEdit_ch5vLow.setObjectName(u"lineEdit_ch5vLow")
        sizePolicy7.setHeightForWidth(self.lineEdit_ch5vLow.sizePolicy().hasHeightForWidth())
        self.lineEdit_ch5vLow.setSizePolicy(sizePolicy7)

        self.horizontalLayout_ch5ScaleMinMax.addWidget(self.lineEdit_ch5vLow)

        self.label_ch5vScaleDash = QLabel(self.setting)
        self.label_ch5vScaleDash.setObjectName(u"label_ch5vScaleDash")

        self.horizontalLayout_ch5ScaleMinMax.addWidget(self.label_ch5vScaleDash)

        self.lineEdit_ch5vHigh = QLineEdit(self.setting)
        self.lineEdit_ch5vHigh.setObjectName(u"lineEdit_ch5vHigh")
        sizePolicy7.setHeightForWidth(self.lineEdit_ch5vHigh.sizePolicy().hasHeightForWidth())
        self.lineEdit_ch5vHigh.setSizePolicy(sizePolicy7)

        self.horizontalLayout_ch5ScaleMinMax.addWidget(self.lineEdit_ch5vHigh)


        self.gridLayout_setting.addLayout(self.horizontalLayout_ch5ScaleMinMax, 5, 2, 1, 1)

        self.horizontalLayout_ch1Scale = QHBoxLayout()
        self.horizontalLayout_ch1Scale.setSpacing(10)
        self.horizontalLayout_ch1Scale.setObjectName(u"horizontalLayout_ch1Scale")
        self.comboBox_ch1scale = QComboBox(self.setting)
        self.comboBox_ch1scale.addItem("")
        self.comboBox_ch1scale.addItem("")
        self.comboBox_ch1scale.addItem("")
        self.comboBox_ch1scale.setObjectName(u"comboBox_ch1scale")
        sizePolicy7.setHeightForWidth(self.comboBox_ch1scale.sizePolicy().hasHeightForWidth())
        self.comboBox_ch1scale.setSizePolicy(sizePolicy7)

        self.horizontalLayout_ch1Scale.addWidget(self.comboBox_ch1scale)


        self.gridLayout_setting.addLayout(self.horizontalLayout_ch1Scale, 1, 3, 1, 1)

        self.horizontalLayout_ch7ScaleMinMax = QHBoxLayout()
        self.horizontalLayout_ch7ScaleMinMax.setSpacing(10)
        self.horizontalLayout_ch7ScaleMinMax.setObjectName(u"horizontalLayout_ch7ScaleMinMax")
        self.lineEdit_ch7vLow = QLineEdit(self.setting)
        self.lineEdit_ch7vLow.setObjectName(u"lineEdit_ch7vLow")
        sizePolicy7.setHeightForWidth(self.lineEdit_ch7vLow.sizePolicy().hasHeightForWidth())
        self.lineEdit_ch7vLow.setSizePolicy(sizePolicy7)

        self.horizontalLayout_ch7ScaleMinMax.addWidget(self.lineEdit_ch7vLow)

        self.label_ch7vScaleDash = QLabel(self.setting)
        self.label_ch7vScaleDash.setObjectName(u"label_ch7vScaleDash")

        self.horizontalLayout_ch7ScaleMinMax.addWidget(self.label_ch7vScaleDash)

        self.lineEdit_ch7vHigh = QLineEdit(self.setting)
        self.lineEdit_ch7vHigh.setObjectName(u"lineEdit_ch7vHigh")
        sizePolicy7.setHeightForWidth(self.lineEdit_ch7vHigh.sizePolicy().hasHeightForWidth())
        self.lineEdit_ch7vHigh.setSizePolicy(sizePolicy7)

        self.horizontalLayout_ch7ScaleMinMax.addWidget(self.lineEdit_ch7vHigh)


        self.gridLayout_setting.addLayout(self.horizontalLayout_ch7ScaleMinMax, 7, 2, 1, 1)

        self.label_deviceModelSetting = QLabel(self.setting)
        self.label_deviceModelSetting.setObjectName(u"label_deviceModelSetting")

        self.gridLayout_setting.addWidget(self.label_deviceModelSetting, 0, 0, 1, 2, Qt.AlignHCenter)

        self.horizontalLayout_ch1ScaleMinMax = QHBoxLayout()
        self.horizontalLayout_ch1ScaleMinMax.setSpacing(10)
        self.horizontalLayout_ch1ScaleMinMax.setObjectName(u"horizontalLayout_ch1ScaleMinMax")
        self.lineEdit_ch1vLow = QLineEdit(self.setting)
        self.lineEdit_ch1vLow.setObjectName(u"lineEdit_ch1vLow")
        sizePolicy7.setHeightForWidth(self.lineEdit_ch1vLow.sizePolicy().hasHeightForWidth())
        self.lineEdit_ch1vLow.setSizePolicy(sizePolicy7)
        self.lineEdit_ch1vLow.setFont(font1)

        self.horizontalLayout_ch1ScaleMinMax.addWidget(self.lineEdit_ch1vLow)

        self.label_ch1vScaleDash = QLabel(self.setting)
        self.label_ch1vScaleDash.setObjectName(u"label_ch1vScaleDash")

        self.horizontalLayout_ch1ScaleMinMax.addWidget(self.label_ch1vScaleDash)

        self.lineEdit_ch1vHigh = QLineEdit(self.setting)
        self.lineEdit_ch1vHigh.setObjectName(u"lineEdit_ch1vHigh")
        sizePolicy7.setHeightForWidth(self.lineEdit_ch1vHigh.sizePolicy().hasHeightForWidth())
        self.lineEdit_ch1vHigh.setSizePolicy(sizePolicy7)

        self.horizontalLayout_ch1ScaleMinMax.addWidget(self.lineEdit_ch1vHigh)


        self.gridLayout_setting.addLayout(self.horizontalLayout_ch1ScaleMinMax, 1, 2, 1, 1)

        self.horizontalLayout_ResRate = QHBoxLayout()
        self.horizontalLayout_ResRate.setObjectName(u"horizontalLayout_ResRate")
        self.label_ResRate = QLabel(self.setting)
        self.label_ResRate.setObjectName(u"label_ResRate")

        self.horizontalLayout_ResRate.addWidget(self.label_ResRate)

        self.lineEdit_ResRate = QLineEdit(self.setting)
        self.lineEdit_ResRate.setObjectName(u"lineEdit_ResRate")
        sizePolicy6.setHeightForWidth(self.lineEdit_ResRate.sizePolicy().hasHeightForWidth())
        self.lineEdit_ResRate.setSizePolicy(sizePolicy6)

        self.horizontalLayout_ResRate.addWidget(self.lineEdit_ResRate)

        self.horizontalLayout_ResRate.setStretch(0, 1)
        self.horizontalLayout_ResRate.setStretch(1, 1)

        self.gridLayout_setting.addLayout(self.horizontalLayout_ResRate, 6, 0, 1, 1)

        self.label_ch6Setting = QLabel(self.setting)
        self.label_ch6Setting.setObjectName(u"label_ch6Setting")

        self.gridLayout_setting.addWidget(self.label_ch6Setting, 6, 1, 1, 1, Qt.AlignRight)

        self.horizontalLayout_ch4Scale = QHBoxLayout()
        self.horizontalLayout_ch4Scale.setSpacing(10)
        self.horizontalLayout_ch4Scale.setObjectName(u"horizontalLayout_ch4Scale")
        self.comboBox_ch4scale = QComboBox(self.setting)
        self.comboBox_ch4scale.addItem("")
        self.comboBox_ch4scale.addItem("")
        self.comboBox_ch4scale.addItem("")
        self.comboBox_ch4scale.setObjectName(u"comboBox_ch4scale")
        sizePolicy7.setHeightForWidth(self.comboBox_ch4scale.sizePolicy().hasHeightForWidth())
        self.comboBox_ch4scale.setSizePolicy(sizePolicy7)

        self.horizontalLayout_ch4Scale.addWidget(self.comboBox_ch4scale)


        self.gridLayout_setting.addLayout(self.horizontalLayout_ch4Scale, 4, 3, 1, 1)

        self.horizontalLayout_ch5Scale = QHBoxLayout()
        self.horizontalLayout_ch5Scale.setSpacing(10)
        self.horizontalLayout_ch5Scale.setObjectName(u"horizontalLayout_ch5Scale")
        self.comboBox_ch5scale = QComboBox(self.setting)
        self.comboBox_ch5scale.addItem("")
        self.comboBox_ch5scale.addItem("")
        self.comboBox_ch5scale.addItem("")
        self.comboBox_ch5scale.setObjectName(u"comboBox_ch5scale")
        sizePolicy7.setHeightForWidth(self.comboBox_ch5scale.sizePolicy().hasHeightForWidth())
        self.comboBox_ch5scale.setSizePolicy(sizePolicy7)

        self.horizontalLayout_ch5Scale.addWidget(self.comboBox_ch5scale)


        self.gridLayout_setting.addLayout(self.horizontalLayout_ch5Scale, 5, 3, 1, 1)

        self.horizontalLayout_baudRate = QHBoxLayout()
        self.horizontalLayout_baudRate.setObjectName(u"horizontalLayout_baudRate")
        self.label_baudRate = QLabel(self.setting)
        self.label_baudRate.setObjectName(u"label_baudRate")

        self.horizontalLayout_baudRate.addWidget(self.label_baudRate)

        self.comboBox_baudRate = QComboBox(self.setting)
        self.comboBox_baudRate.addItem("")
        self.comboBox_baudRate.addItem("")
        self.comboBox_baudRate.addItem("")
        self.comboBox_baudRate.addItem("")
        self.comboBox_baudRate.addItem("")
        self.comboBox_baudRate.addItem("")
        self.comboBox_baudRate.addItem("")
        self.comboBox_baudRate.addItem("")
        self.comboBox_baudRate.addItem("")
        self.comboBox_baudRate.addItem("")
        self.comboBox_baudRate.addItem("")
        self.comboBox_baudRate.addItem("")
        self.comboBox_baudRate.addItem("")
        self.comboBox_baudRate.addItem("")
        self.comboBox_baudRate.addItem("")
        self.comboBox_baudRate.addItem("")
        self.comboBox_baudRate.addItem("")
        self.comboBox_baudRate.addItem("")
        self.comboBox_baudRate.setObjectName(u"comboBox_baudRate")
        sizePolicy6.setHeightForWidth(self.comboBox_baudRate.sizePolicy().hasHeightForWidth())
        self.comboBox_baudRate.setSizePolicy(sizePolicy6)
        self.comboBox_baudRate.setMaxVisibleItems(20)

        self.horizontalLayout_baudRate.addWidget(self.comboBox_baudRate)

        self.horizontalLayout_baudRate.setStretch(0, 1)
        self.horizontalLayout_baudRate.setStretch(1, 1)

        self.gridLayout_setting.addLayout(self.horizontalLayout_baudRate, 4, 0, 1, 1)

        self.horizontalLayout_ch2ScaleMinMax = QHBoxLayout()
        self.horizontalLayout_ch2ScaleMinMax.setSpacing(10)
        self.horizontalLayout_ch2ScaleMinMax.setObjectName(u"horizontalLayout_ch2ScaleMinMax")
        self.lineEdit_ch2vLow = QLineEdit(self.setting)
        self.lineEdit_ch2vLow.setObjectName(u"lineEdit_ch2vLow")
        sizePolicy7.setHeightForWidth(self.lineEdit_ch2vLow.sizePolicy().hasHeightForWidth())
        self.lineEdit_ch2vLow.setSizePolicy(sizePolicy7)

        self.horizontalLayout_ch2ScaleMinMax.addWidget(self.lineEdit_ch2vLow)

        self.label_ch2vScaleDash = QLabel(self.setting)
        self.label_ch2vScaleDash.setObjectName(u"label_ch2vScaleDash")

        self.horizontalLayout_ch2ScaleMinMax.addWidget(self.label_ch2vScaleDash)

        self.lineEdit_ch2vHigh = QLineEdit(self.setting)
        self.lineEdit_ch2vHigh.setObjectName(u"lineEdit_ch2vHigh")
        sizePolicy7.setHeightForWidth(self.lineEdit_ch2vHigh.sizePolicy().hasHeightForWidth())
        self.lineEdit_ch2vHigh.setSizePolicy(sizePolicy7)

        self.horizontalLayout_ch2ScaleMinMax.addWidget(self.lineEdit_ch2vHigh)


        self.gridLayout_setting.addLayout(self.horizontalLayout_ch2ScaleMinMax, 2, 2, 1, 1)

        self.horizontalLayout_ch3Scale = QHBoxLayout()
        self.horizontalLayout_ch3Scale.setSpacing(10)
        self.horizontalLayout_ch3Scale.setObjectName(u"horizontalLayout_ch3Scale")
        self.comboBox_ch3scale = QComboBox(self.setting)
        self.comboBox_ch3scale.addItem("")
        self.comboBox_ch3scale.addItem("")
        self.comboBox_ch3scale.addItem("")
        self.comboBox_ch3scale.setObjectName(u"comboBox_ch3scale")
        sizePolicy7.setHeightForWidth(self.comboBox_ch3scale.sizePolicy().hasHeightForWidth())
        self.comboBox_ch3scale.setSizePolicy(sizePolicy7)

        self.horizontalLayout_ch3Scale.addWidget(self.comboBox_ch3scale)


        self.gridLayout_setting.addLayout(self.horizontalLayout_ch3Scale, 3, 3, 1, 1)

        self.label_ch7Setting = QLabel(self.setting)
        self.label_ch7Setting.setObjectName(u"label_ch7Setting")

        self.gridLayout_setting.addWidget(self.label_ch7Setting, 7, 1, 1, 1, Qt.AlignRight)

        self.horizontalLayout_ch3ScaleMinMax = QHBoxLayout()
        self.horizontalLayout_ch3ScaleMinMax.setSpacing(10)
        self.horizontalLayout_ch3ScaleMinMax.setObjectName(u"horizontalLayout_ch3ScaleMinMax")
        self.lineEdit_ch3vLow = QLineEdit(self.setting)
        self.lineEdit_ch3vLow.setObjectName(u"lineEdit_ch3vLow")
        sizePolicy7.setHeightForWidth(self.lineEdit_ch3vLow.sizePolicy().hasHeightForWidth())
        self.lineEdit_ch3vLow.setSizePolicy(sizePolicy7)

        self.horizontalLayout_ch3ScaleMinMax.addWidget(self.lineEdit_ch3vLow)

        self.label_ch3vScaleDash = QLabel(self.setting)
        self.label_ch3vScaleDash.setObjectName(u"label_ch3vScaleDash")

        self.horizontalLayout_ch3ScaleMinMax.addWidget(self.label_ch3vScaleDash)

        self.lineEdit_ch3vHigh = QLineEdit(self.setting)
        self.lineEdit_ch3vHigh.setObjectName(u"lineEdit_ch3vHigh")
        sizePolicy7.setHeightForWidth(self.lineEdit_ch3vHigh.sizePolicy().hasHeightForWidth())
        self.lineEdit_ch3vHigh.setSizePolicy(sizePolicy7)

        self.horizontalLayout_ch3ScaleMinMax.addWidget(self.lineEdit_ch3vHigh)


        self.gridLayout_setting.addLayout(self.horizontalLayout_ch3ScaleMinMax, 3, 2, 1, 1)

        self.horizontalLayout_ch2Scale = QHBoxLayout()
        self.horizontalLayout_ch2Scale.setSpacing(10)
        self.horizontalLayout_ch2Scale.setObjectName(u"horizontalLayout_ch2Scale")
        self.comboBox_ch2scale = QComboBox(self.setting)
        self.comboBox_ch2scale.addItem("")
        self.comboBox_ch2scale.addItem("")
        self.comboBox_ch2scale.addItem("")
        self.comboBox_ch2scale.setObjectName(u"comboBox_ch2scale")
        sizePolicy7.setHeightForWidth(self.comboBox_ch2scale.sizePolicy().hasHeightForWidth())
        self.comboBox_ch2scale.setSizePolicy(sizePolicy7)

        self.horizontalLayout_ch2Scale.addWidget(self.comboBox_ch2scale)


        self.gridLayout_setting.addLayout(self.horizontalLayout_ch2Scale, 2, 3, 1, 1)

        self.label_ch2Setting = QLabel(self.setting)
        self.label_ch2Setting.setObjectName(u"label_ch2Setting")

        self.gridLayout_setting.addWidget(self.label_ch2Setting, 2, 1, 1, 1, Qt.AlignRight)

        self.label_ch4Setting = QLabel(self.setting)
        self.label_ch4Setting.setObjectName(u"label_ch4Setting")

        self.gridLayout_setting.addWidget(self.label_ch4Setting, 4, 1, 1, 1, Qt.AlignRight)

        self.label_ch5Setting = QLabel(self.setting)
        self.label_ch5Setting.setObjectName(u"label_ch5Setting")

        self.gridLayout_setting.addWidget(self.label_ch5Setting, 5, 1, 1, 1, Qt.AlignRight)

        self.horizontalLayout_ch6ScaleMinMax = QHBoxLayout()
        self.horizontalLayout_ch6ScaleMinMax.setSpacing(10)
        self.horizontalLayout_ch6ScaleMinMax.setObjectName(u"horizontalLayout_ch6ScaleMinMax")
        self.lineEdit_ch6vLow = QLineEdit(self.setting)
        self.lineEdit_ch6vLow.setObjectName(u"lineEdit_ch6vLow")
        sizePolicy7.setHeightForWidth(self.lineEdit_ch6vLow.sizePolicy().hasHeightForWidth())
        self.lineEdit_ch6vLow.setSizePolicy(sizePolicy7)

        self.horizontalLayout_ch6ScaleMinMax.addWidget(self.lineEdit_ch6vLow)

        self.label_ch6vScaleDash = QLabel(self.setting)
        self.label_ch6vScaleDash.setObjectName(u"label_ch6vScaleDash")

        self.horizontalLayout_ch6ScaleMinMax.addWidget(self.label_ch6vScaleDash)

        self.lineEdit_ch6vHigh = QLineEdit(self.setting)
        self.lineEdit_ch6vHigh.setObjectName(u"lineEdit_ch6vHigh")
        sizePolicy7.setHeightForWidth(self.lineEdit_ch6vHigh.sizePolicy().hasHeightForWidth())
        self.lineEdit_ch6vHigh.setSizePolicy(sizePolicy7)

        self.horizontalLayout_ch6ScaleMinMax.addWidget(self.lineEdit_ch6vHigh)


        self.gridLayout_setting.addLayout(self.horizontalLayout_ch6ScaleMinMax, 6, 2, 1, 1)

        self.label_ch8Setting = QLabel(self.setting)
        self.label_ch8Setting.setObjectName(u"label_ch8Setting")

        self.gridLayout_setting.addWidget(self.label_ch8Setting, 8, 1, 1, 1, Qt.AlignRight)

        self.gridLayout_setting.setColumnStretch(0, 3)
        self.gridLayout_setting.setColumnStretch(1, 1)
        self.gridLayout_setting.setColumnStretch(2, 1)
        self.gridLayout_setting.setColumnStretch(3, 1)
        self.stackedWidget.addWidget(self.setting)
        self.calibration = QWidget()
        self.calibration.setObjectName(u"calibration")
        self.gridLayout_calibration = QGridLayout(self.calibration)
        self.gridLayout_calibration.setObjectName(u"gridLayout_calibration")
        self.groupBox_calibration = QGroupBox(self.calibration)
        self.groupBox_calibration.setObjectName(u"groupBox_calibration")
        self.gridLayout_4 = QGridLayout(self.groupBox_calibration)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.horizontalLayout_ch1calibration = QHBoxLayout()
        self.horizontalLayout_ch1calibration.setSpacing(10)
        self.horizontalLayout_ch1calibration.setObjectName(u"horizontalLayout_ch1calibration")
        self.label_ch1calibration = QLabel(self.groupBox_calibration)
        self.label_ch1calibration.setObjectName(u"label_ch1calibration")
        sizePolicy6.setHeightForWidth(self.label_ch1calibration.sizePolicy().hasHeightForWidth())
        self.label_ch1calibration.setSizePolicy(sizePolicy6)

        self.horizontalLayout_ch1calibration.addWidget(self.label_ch1calibration)

        self.lineEdit_ch1point1 = QLineEdit(self.groupBox_calibration)
        self.lineEdit_ch1point1.setObjectName(u"lineEdit_ch1point1")
        sizePolicy3.setHeightForWidth(self.lineEdit_ch1point1.sizePolicy().hasHeightForWidth())
        self.lineEdit_ch1point1.setSizePolicy(sizePolicy3)
        self.lineEdit_ch1point1.setMaxLength(5)

        self.horizontalLayout_ch1calibration.addWidget(self.lineEdit_ch1point1)

        self.pushButton_ch1point1 = QPushButton(self.groupBox_calibration)
        self.pushButton_ch1point1.setObjectName(u"pushButton_ch1point1")
        sizePolicy5.setHeightForWidth(self.pushButton_ch1point1.sizePolicy().hasHeightForWidth())
        self.pushButton_ch1point1.setSizePolicy(sizePolicy5)

        self.horizontalLayout_ch1calibration.addWidget(self.pushButton_ch1point1)

        self.lineEdit_ch1point2 = QLineEdit(self.groupBox_calibration)
        self.lineEdit_ch1point2.setObjectName(u"lineEdit_ch1point2")
        sizePolicy3.setHeightForWidth(self.lineEdit_ch1point2.sizePolicy().hasHeightForWidth())
        self.lineEdit_ch1point2.setSizePolicy(sizePolicy3)
        self.lineEdit_ch1point2.setMaxLength(5)

        self.horizontalLayout_ch1calibration.addWidget(self.lineEdit_ch1point2)

        self.pushButton_ch1point2 = QPushButton(self.groupBox_calibration)
        self.pushButton_ch1point2.setObjectName(u"pushButton_ch1point2")
        sizePolicy5.setHeightForWidth(self.pushButton_ch1point2.sizePolicy().hasHeightForWidth())
        self.pushButton_ch1point2.setSizePolicy(sizePolicy5)

        self.horizontalLayout_ch1calibration.addWidget(self.pushButton_ch1point2)

        self.lineEdit_ch1point3 = QLineEdit(self.groupBox_calibration)
        self.lineEdit_ch1point3.setObjectName(u"lineEdit_ch1point3")
        sizePolicy3.setHeightForWidth(self.lineEdit_ch1point3.sizePolicy().hasHeightForWidth())
        self.lineEdit_ch1point3.setSizePolicy(sizePolicy3)
        self.lineEdit_ch1point3.setMaxLength(5)

        self.horizontalLayout_ch1calibration.addWidget(self.lineEdit_ch1point3)

        self.pushButton_ch1point3 = QPushButton(self.groupBox_calibration)
        self.pushButton_ch1point3.setObjectName(u"pushButton_ch1point3")
        sizePolicy5.setHeightForWidth(self.pushButton_ch1point3.sizePolicy().hasHeightForWidth())
        self.pushButton_ch1point3.setSizePolicy(sizePolicy5)

        self.horizontalLayout_ch1calibration.addWidget(self.pushButton_ch1point3)

        self.lineEdit_ch1point4 = QLineEdit(self.groupBox_calibration)
        self.lineEdit_ch1point4.setObjectName(u"lineEdit_ch1point4")
        sizePolicy3.setHeightForWidth(self.lineEdit_ch1point4.sizePolicy().hasHeightForWidth())
        self.lineEdit_ch1point4.setSizePolicy(sizePolicy3)
        self.lineEdit_ch1point4.setMaxLength(5)

        self.horizontalLayout_ch1calibration.addWidget(self.lineEdit_ch1point4)

        self.pushButton_ch1point4 = QPushButton(self.groupBox_calibration)
        self.pushButton_ch1point4.setObjectName(u"pushButton_ch1point4")
        sizePolicy5.setHeightForWidth(self.pushButton_ch1point4.sizePolicy().hasHeightForWidth())
        self.pushButton_ch1point4.setSizePolicy(sizePolicy5)

        self.horizontalLayout_ch1calibration.addWidget(self.pushButton_ch1point4)

        self.lineEdit_ch1point5 = QLineEdit(self.groupBox_calibration)
        self.lineEdit_ch1point5.setObjectName(u"lineEdit_ch1point5")
        sizePolicy3.setHeightForWidth(self.lineEdit_ch1point5.sizePolicy().hasHeightForWidth())
        self.lineEdit_ch1point5.setSizePolicy(sizePolicy3)
        self.lineEdit_ch1point5.setMaxLength(5)

        self.horizontalLayout_ch1calibration.addWidget(self.lineEdit_ch1point5)

        self.pushButton_ch1point5 = QPushButton(self.groupBox_calibration)
        self.pushButton_ch1point5.setObjectName(u"pushButton_ch1point5")
        sizePolicy5.setHeightForWidth(self.pushButton_ch1point5.sizePolicy().hasHeightForWidth())
        self.pushButton_ch1point5.setSizePolicy(sizePolicy5)

        self.horizontalLayout_ch1calibration.addWidget(self.pushButton_ch1point5)

        self.comboBox_ch1CalScale = QComboBox(self.groupBox_calibration)
        self.comboBox_ch1CalScale.addItem("")
        self.comboBox_ch1CalScale.addItem("")
        self.comboBox_ch1CalScale.setObjectName(u"comboBox_ch1CalScale")
        sizePolicy7.setHeightForWidth(self.comboBox_ch1CalScale.sizePolicy().hasHeightForWidth())
        self.comboBox_ch1CalScale.setSizePolicy(sizePolicy7)

        self.horizontalLayout_ch1calibration.addWidget(self.comboBox_ch1CalScale)

        self.horizontalLayout_ch1calibration.setStretch(0, 1)
        self.horizontalLayout_ch1calibration.setStretch(1, 1)
        self.horizontalLayout_ch1calibration.setStretch(2, 1)
        self.horizontalLayout_ch1calibration.setStretch(3, 1)
        self.horizontalLayout_ch1calibration.setStretch(4, 1)
        self.horizontalLayout_ch1calibration.setStretch(5, 1)
        self.horizontalLayout_ch1calibration.setStretch(6, 1)
        self.horizontalLayout_ch1calibration.setStretch(7, 1)
        self.horizontalLayout_ch1calibration.setStretch(8, 1)
        self.horizontalLayout_ch1calibration.setStretch(9, 1)
        self.horizontalLayout_ch1calibration.setStretch(10, 1)
        self.horizontalLayout_ch1calibration.setStretch(11, 1)

        self.gridLayout_4.addLayout(self.horizontalLayout_ch1calibration, 1, 0, 1, 1)

        self.horizontalLayout_ch3calibration = QHBoxLayout()
        self.horizontalLayout_ch3calibration.setSpacing(10)
        self.horizontalLayout_ch3calibration.setObjectName(u"horizontalLayout_ch3calibration")
        self.label_ch3calibration = QLabel(self.groupBox_calibration)
        self.label_ch3calibration.setObjectName(u"label_ch3calibration")
        sizePolicy6.setHeightForWidth(self.label_ch3calibration.sizePolicy().hasHeightForWidth())
        self.label_ch3calibration.setSizePolicy(sizePolicy6)

        self.horizontalLayout_ch3calibration.addWidget(self.label_ch3calibration)

        self.lineEdit_ch3point1 = QLineEdit(self.groupBox_calibration)
        self.lineEdit_ch3point1.setObjectName(u"lineEdit_ch3point1")
        sizePolicy3.setHeightForWidth(self.lineEdit_ch3point1.sizePolicy().hasHeightForWidth())
        self.lineEdit_ch3point1.setSizePolicy(sizePolicy3)
        self.lineEdit_ch3point1.setMaxLength(5)

        self.horizontalLayout_ch3calibration.addWidget(self.lineEdit_ch3point1)

        self.pushButton_ch3point1 = QPushButton(self.groupBox_calibration)
        self.pushButton_ch3point1.setObjectName(u"pushButton_ch3point1")
        sizePolicy5.setHeightForWidth(self.pushButton_ch3point1.sizePolicy().hasHeightForWidth())
        self.pushButton_ch3point1.setSizePolicy(sizePolicy5)

        self.horizontalLayout_ch3calibration.addWidget(self.pushButton_ch3point1)

        self.lineEdit_ch3point2 = QLineEdit(self.groupBox_calibration)
        self.lineEdit_ch3point2.setObjectName(u"lineEdit_ch3point2")
        sizePolicy3.setHeightForWidth(self.lineEdit_ch3point2.sizePolicy().hasHeightForWidth())
        self.lineEdit_ch3point2.setSizePolicy(sizePolicy3)
        self.lineEdit_ch3point2.setMaxLength(5)

        self.horizontalLayout_ch3calibration.addWidget(self.lineEdit_ch3point2)

        self.pushButton_ch3point2 = QPushButton(self.groupBox_calibration)
        self.pushButton_ch3point2.setObjectName(u"pushButton_ch3point2")
        sizePolicy5.setHeightForWidth(self.pushButton_ch3point2.sizePolicy().hasHeightForWidth())
        self.pushButton_ch3point2.setSizePolicy(sizePolicy5)

        self.horizontalLayout_ch3calibration.addWidget(self.pushButton_ch3point2)

        self.lineEdit_ch3point3 = QLineEdit(self.groupBox_calibration)
        self.lineEdit_ch3point3.setObjectName(u"lineEdit_ch3point3")
        sizePolicy3.setHeightForWidth(self.lineEdit_ch3point3.sizePolicy().hasHeightForWidth())
        self.lineEdit_ch3point3.setSizePolicy(sizePolicy3)
        self.lineEdit_ch3point3.setMaxLength(5)

        self.horizontalLayout_ch3calibration.addWidget(self.lineEdit_ch3point3)

        self.pushButton_ch3point3 = QPushButton(self.groupBox_calibration)
        self.pushButton_ch3point3.setObjectName(u"pushButton_ch3point3")
        sizePolicy5.setHeightForWidth(self.pushButton_ch3point3.sizePolicy().hasHeightForWidth())
        self.pushButton_ch3point3.setSizePolicy(sizePolicy5)

        self.horizontalLayout_ch3calibration.addWidget(self.pushButton_ch3point3)

        self.lineEdit_ch3point4 = QLineEdit(self.groupBox_calibration)
        self.lineEdit_ch3point4.setObjectName(u"lineEdit_ch3point4")
        sizePolicy3.setHeightForWidth(self.lineEdit_ch3point4.sizePolicy().hasHeightForWidth())
        self.lineEdit_ch3point4.setSizePolicy(sizePolicy3)
        self.lineEdit_ch3point4.setMaxLength(5)

        self.horizontalLayout_ch3calibration.addWidget(self.lineEdit_ch3point4)

        self.pushButton_ch3point4 = QPushButton(self.groupBox_calibration)
        self.pushButton_ch3point4.setObjectName(u"pushButton_ch3point4")
        sizePolicy5.setHeightForWidth(self.pushButton_ch3point4.sizePolicy().hasHeightForWidth())
        self.pushButton_ch3point4.setSizePolicy(sizePolicy5)

        self.horizontalLayout_ch3calibration.addWidget(self.pushButton_ch3point4)

        self.lineEdit_ch3point5 = QLineEdit(self.groupBox_calibration)
        self.lineEdit_ch3point5.setObjectName(u"lineEdit_ch3point5")
        sizePolicy3.setHeightForWidth(self.lineEdit_ch3point5.sizePolicy().hasHeightForWidth())
        self.lineEdit_ch3point5.setSizePolicy(sizePolicy3)
        self.lineEdit_ch3point5.setMaxLength(5)

        self.horizontalLayout_ch3calibration.addWidget(self.lineEdit_ch3point5)

        self.pushButton_ch3point5 = QPushButton(self.groupBox_calibration)
        self.pushButton_ch3point5.setObjectName(u"pushButton_ch3point5")
        sizePolicy5.setHeightForWidth(self.pushButton_ch3point5.sizePolicy().hasHeightForWidth())
        self.pushButton_ch3point5.setSizePolicy(sizePolicy5)

        self.horizontalLayout_ch3calibration.addWidget(self.pushButton_ch3point5)

        self.comboBox_ch3CalScale = QComboBox(self.groupBox_calibration)
        self.comboBox_ch3CalScale.addItem("")
        self.comboBox_ch3CalScale.addItem("")
        self.comboBox_ch3CalScale.setObjectName(u"comboBox_ch3CalScale")

        self.horizontalLayout_ch3calibration.addWidget(self.comboBox_ch3CalScale)

        self.horizontalLayout_ch3calibration.setStretch(0, 1)
        self.horizontalLayout_ch3calibration.setStretch(1, 1)
        self.horizontalLayout_ch3calibration.setStretch(2, 1)
        self.horizontalLayout_ch3calibration.setStretch(3, 1)
        self.horizontalLayout_ch3calibration.setStretch(4, 1)
        self.horizontalLayout_ch3calibration.setStretch(5, 1)
        self.horizontalLayout_ch3calibration.setStretch(6, 1)
        self.horizontalLayout_ch3calibration.setStretch(7, 1)
        self.horizontalLayout_ch3calibration.setStretch(8, 1)
        self.horizontalLayout_ch3calibration.setStretch(9, 1)
        self.horizontalLayout_ch3calibration.setStretch(10, 1)

        self.gridLayout_4.addLayout(self.horizontalLayout_ch3calibration, 3, 0, 1, 1)

        self.horizontalLayout_ch8calibration = QHBoxLayout()
        self.horizontalLayout_ch8calibration.setSpacing(10)
        self.horizontalLayout_ch8calibration.setObjectName(u"horizontalLayout_ch8calibration")
        self.label_ch8calibration = QLabel(self.groupBox_calibration)
        self.label_ch8calibration.setObjectName(u"label_ch8calibration")
        sizePolicy6.setHeightForWidth(self.label_ch8calibration.sizePolicy().hasHeightForWidth())
        self.label_ch8calibration.setSizePolicy(sizePolicy6)

        self.horizontalLayout_ch8calibration.addWidget(self.label_ch8calibration)

        self.lineEdit_ch8point1 = QLineEdit(self.groupBox_calibration)
        self.lineEdit_ch8point1.setObjectName(u"lineEdit_ch8point1")
        sizePolicy3.setHeightForWidth(self.lineEdit_ch8point1.sizePolicy().hasHeightForWidth())
        self.lineEdit_ch8point1.setSizePolicy(sizePolicy3)
        self.lineEdit_ch8point1.setMaxLength(5)

        self.horizontalLayout_ch8calibration.addWidget(self.lineEdit_ch8point1)

        self.pushButton_ch8point1 = QPushButton(self.groupBox_calibration)
        self.pushButton_ch8point1.setObjectName(u"pushButton_ch8point1")
        sizePolicy5.setHeightForWidth(self.pushButton_ch8point1.sizePolicy().hasHeightForWidth())
        self.pushButton_ch8point1.setSizePolicy(sizePolicy5)

        self.horizontalLayout_ch8calibration.addWidget(self.pushButton_ch8point1)

        self.lineEdit_ch8point2 = QLineEdit(self.groupBox_calibration)
        self.lineEdit_ch8point2.setObjectName(u"lineEdit_ch8point2")
        sizePolicy3.setHeightForWidth(self.lineEdit_ch8point2.sizePolicy().hasHeightForWidth())
        self.lineEdit_ch8point2.setSizePolicy(sizePolicy3)
        self.lineEdit_ch8point2.setMaxLength(5)

        self.horizontalLayout_ch8calibration.addWidget(self.lineEdit_ch8point2)

        self.pushButton_ch8point2 = QPushButton(self.groupBox_calibration)
        self.pushButton_ch8point2.setObjectName(u"pushButton_ch8point2")
        sizePolicy5.setHeightForWidth(self.pushButton_ch8point2.sizePolicy().hasHeightForWidth())
        self.pushButton_ch8point2.setSizePolicy(sizePolicy5)

        self.horizontalLayout_ch8calibration.addWidget(self.pushButton_ch8point2)

        self.lineEdit_ch8point3 = QLineEdit(self.groupBox_calibration)
        self.lineEdit_ch8point3.setObjectName(u"lineEdit_ch8point3")
        sizePolicy3.setHeightForWidth(self.lineEdit_ch8point3.sizePolicy().hasHeightForWidth())
        self.lineEdit_ch8point3.setSizePolicy(sizePolicy3)
        self.lineEdit_ch8point3.setMaxLength(5)

        self.horizontalLayout_ch8calibration.addWidget(self.lineEdit_ch8point3)

        self.pushButton_ch8point3 = QPushButton(self.groupBox_calibration)
        self.pushButton_ch8point3.setObjectName(u"pushButton_ch8point3")
        sizePolicy5.setHeightForWidth(self.pushButton_ch8point3.sizePolicy().hasHeightForWidth())
        self.pushButton_ch8point3.setSizePolicy(sizePolicy5)

        self.horizontalLayout_ch8calibration.addWidget(self.pushButton_ch8point3)

        self.lineEdit_ch8point4 = QLineEdit(self.groupBox_calibration)
        self.lineEdit_ch8point4.setObjectName(u"lineEdit_ch8point4")
        sizePolicy3.setHeightForWidth(self.lineEdit_ch8point4.sizePolicy().hasHeightForWidth())
        self.lineEdit_ch8point4.setSizePolicy(sizePolicy3)
        self.lineEdit_ch8point4.setMaxLength(5)

        self.horizontalLayout_ch8calibration.addWidget(self.lineEdit_ch8point4)

        self.pushButton_ch8point4 = QPushButton(self.groupBox_calibration)
        self.pushButton_ch8point4.setObjectName(u"pushButton_ch8point4")
        sizePolicy5.setHeightForWidth(self.pushButton_ch8point4.sizePolicy().hasHeightForWidth())
        self.pushButton_ch8point4.setSizePolicy(sizePolicy5)

        self.horizontalLayout_ch8calibration.addWidget(self.pushButton_ch8point4)

        self.lineEdit_ch8point5 = QLineEdit(self.groupBox_calibration)
        self.lineEdit_ch8point5.setObjectName(u"lineEdit_ch8point5")
        sizePolicy3.setHeightForWidth(self.lineEdit_ch8point5.sizePolicy().hasHeightForWidth())
        self.lineEdit_ch8point5.setSizePolicy(sizePolicy3)
        self.lineEdit_ch8point5.setMaxLength(5)

        self.horizontalLayout_ch8calibration.addWidget(self.lineEdit_ch8point5)

        self.pushButton_ch8point5 = QPushButton(self.groupBox_calibration)
        self.pushButton_ch8point5.setObjectName(u"pushButton_ch8point5")
        sizePolicy5.setHeightForWidth(self.pushButton_ch8point5.sizePolicy().hasHeightForWidth())
        self.pushButton_ch8point5.setSizePolicy(sizePolicy5)

        self.horizontalLayout_ch8calibration.addWidget(self.pushButton_ch8point5)

        self.comboBox_ch8CalScale = QComboBox(self.groupBox_calibration)
        self.comboBox_ch8CalScale.addItem("")
        self.comboBox_ch8CalScale.addItem("")
        self.comboBox_ch8CalScale.setObjectName(u"comboBox_ch8CalScale")

        self.horizontalLayout_ch8calibration.addWidget(self.comboBox_ch8CalScale)

        self.horizontalLayout_ch8calibration.setStretch(0, 1)
        self.horizontalLayout_ch8calibration.setStretch(1, 1)
        self.horizontalLayout_ch8calibration.setStretch(2, 1)
        self.horizontalLayout_ch8calibration.setStretch(3, 1)
        self.horizontalLayout_ch8calibration.setStretch(4, 1)
        self.horizontalLayout_ch8calibration.setStretch(5, 1)
        self.horizontalLayout_ch8calibration.setStretch(6, 1)
        self.horizontalLayout_ch8calibration.setStretch(7, 1)
        self.horizontalLayout_ch8calibration.setStretch(8, 1)
        self.horizontalLayout_ch8calibration.setStretch(9, 1)
        self.horizontalLayout_ch8calibration.setStretch(10, 1)

        self.gridLayout_4.addLayout(self.horizontalLayout_ch8calibration, 8, 0, 1, 1)

        self.horizontalLayout_ch7calibration = QHBoxLayout()
        self.horizontalLayout_ch7calibration.setSpacing(10)
        self.horizontalLayout_ch7calibration.setObjectName(u"horizontalLayout_ch7calibration")
        self.label_ch7calibration = QLabel(self.groupBox_calibration)
        self.label_ch7calibration.setObjectName(u"label_ch7calibration")
        sizePolicy6.setHeightForWidth(self.label_ch7calibration.sizePolicy().hasHeightForWidth())
        self.label_ch7calibration.setSizePolicy(sizePolicy6)

        self.horizontalLayout_ch7calibration.addWidget(self.label_ch7calibration)

        self.lineEdit_ch7point1 = QLineEdit(self.groupBox_calibration)
        self.lineEdit_ch7point1.setObjectName(u"lineEdit_ch7point1")
        sizePolicy3.setHeightForWidth(self.lineEdit_ch7point1.sizePolicy().hasHeightForWidth())
        self.lineEdit_ch7point1.setSizePolicy(sizePolicy3)
        self.lineEdit_ch7point1.setMaxLength(5)

        self.horizontalLayout_ch7calibration.addWidget(self.lineEdit_ch7point1)

        self.pushButton_ch7point1 = QPushButton(self.groupBox_calibration)
        self.pushButton_ch7point1.setObjectName(u"pushButton_ch7point1")
        sizePolicy5.setHeightForWidth(self.pushButton_ch7point1.sizePolicy().hasHeightForWidth())
        self.pushButton_ch7point1.setSizePolicy(sizePolicy5)

        self.horizontalLayout_ch7calibration.addWidget(self.pushButton_ch7point1)

        self.lineEdit_ch7point2 = QLineEdit(self.groupBox_calibration)
        self.lineEdit_ch7point2.setObjectName(u"lineEdit_ch7point2")
        sizePolicy3.setHeightForWidth(self.lineEdit_ch7point2.sizePolicy().hasHeightForWidth())
        self.lineEdit_ch7point2.setSizePolicy(sizePolicy3)
        self.lineEdit_ch7point2.setMaxLength(5)

        self.horizontalLayout_ch7calibration.addWidget(self.lineEdit_ch7point2)

        self.pushButton_ch7point2 = QPushButton(self.groupBox_calibration)
        self.pushButton_ch7point2.setObjectName(u"pushButton_ch7point2")
        sizePolicy5.setHeightForWidth(self.pushButton_ch7point2.sizePolicy().hasHeightForWidth())
        self.pushButton_ch7point2.setSizePolicy(sizePolicy5)

        self.horizontalLayout_ch7calibration.addWidget(self.pushButton_ch7point2)

        self.lineEdit_ch7point3 = QLineEdit(self.groupBox_calibration)
        self.lineEdit_ch7point3.setObjectName(u"lineEdit_ch7point3")
        sizePolicy3.setHeightForWidth(self.lineEdit_ch7point3.sizePolicy().hasHeightForWidth())
        self.lineEdit_ch7point3.setSizePolicy(sizePolicy3)
        self.lineEdit_ch7point3.setMaxLength(5)

        self.horizontalLayout_ch7calibration.addWidget(self.lineEdit_ch7point3)

        self.pushButton_ch7point3 = QPushButton(self.groupBox_calibration)
        self.pushButton_ch7point3.setObjectName(u"pushButton_ch7point3")
        sizePolicy5.setHeightForWidth(self.pushButton_ch7point3.sizePolicy().hasHeightForWidth())
        self.pushButton_ch7point3.setSizePolicy(sizePolicy5)

        self.horizontalLayout_ch7calibration.addWidget(self.pushButton_ch7point3)

        self.lineEdit_ch7point4 = QLineEdit(self.groupBox_calibration)
        self.lineEdit_ch7point4.setObjectName(u"lineEdit_ch7point4")
        sizePolicy3.setHeightForWidth(self.lineEdit_ch7point4.sizePolicy().hasHeightForWidth())
        self.lineEdit_ch7point4.setSizePolicy(sizePolicy3)
        self.lineEdit_ch7point4.setMaxLength(5)

        self.horizontalLayout_ch7calibration.addWidget(self.lineEdit_ch7point4)

        self.pushButton_ch7point4 = QPushButton(self.groupBox_calibration)
        self.pushButton_ch7point4.setObjectName(u"pushButton_ch7point4")
        sizePolicy5.setHeightForWidth(self.pushButton_ch7point4.sizePolicy().hasHeightForWidth())
        self.pushButton_ch7point4.setSizePolicy(sizePolicy5)

        self.horizontalLayout_ch7calibration.addWidget(self.pushButton_ch7point4)

        self.lineEdit_ch7point5 = QLineEdit(self.groupBox_calibration)
        self.lineEdit_ch7point5.setObjectName(u"lineEdit_ch7point5")
        sizePolicy3.setHeightForWidth(self.lineEdit_ch7point5.sizePolicy().hasHeightForWidth())
        self.lineEdit_ch7point5.setSizePolicy(sizePolicy3)
        self.lineEdit_ch7point5.setMaxLength(5)

        self.horizontalLayout_ch7calibration.addWidget(self.lineEdit_ch7point5)

        self.pushButton_ch7point5 = QPushButton(self.groupBox_calibration)
        self.pushButton_ch7point5.setObjectName(u"pushButton_ch7point5")
        sizePolicy5.setHeightForWidth(self.pushButton_ch7point5.sizePolicy().hasHeightForWidth())
        self.pushButton_ch7point5.setSizePolicy(sizePolicy5)

        self.horizontalLayout_ch7calibration.addWidget(self.pushButton_ch7point5)

        self.comboBox_ch7CalScale = QComboBox(self.groupBox_calibration)
        self.comboBox_ch7CalScale.addItem("")
        self.comboBox_ch7CalScale.addItem("")
        self.comboBox_ch7CalScale.setObjectName(u"comboBox_ch7CalScale")

        self.horizontalLayout_ch7calibration.addWidget(self.comboBox_ch7CalScale)

        self.horizontalLayout_ch7calibration.setStretch(0, 1)
        self.horizontalLayout_ch7calibration.setStretch(1, 1)
        self.horizontalLayout_ch7calibration.setStretch(2, 1)
        self.horizontalLayout_ch7calibration.setStretch(3, 1)
        self.horizontalLayout_ch7calibration.setStretch(4, 1)
        self.horizontalLayout_ch7calibration.setStretch(5, 1)
        self.horizontalLayout_ch7calibration.setStretch(6, 1)
        self.horizontalLayout_ch7calibration.setStretch(7, 1)
        self.horizontalLayout_ch7calibration.setStretch(8, 1)
        self.horizontalLayout_ch7calibration.setStretch(9, 1)
        self.horizontalLayout_ch7calibration.setStretch(10, 1)

        self.gridLayout_4.addLayout(self.horizontalLayout_ch7calibration, 7, 0, 1, 1)

        self.horizontalLayout_ch2calibration = QHBoxLayout()
        self.horizontalLayout_ch2calibration.setSpacing(10)
        self.horizontalLayout_ch2calibration.setObjectName(u"horizontalLayout_ch2calibration")
        self.label_ch2calibration = QLabel(self.groupBox_calibration)
        self.label_ch2calibration.setObjectName(u"label_ch2calibration")
        sizePolicy6.setHeightForWidth(self.label_ch2calibration.sizePolicy().hasHeightForWidth())
        self.label_ch2calibration.setSizePolicy(sizePolicy6)

        self.horizontalLayout_ch2calibration.addWidget(self.label_ch2calibration)

        self.lineEdit_ch2point1 = QLineEdit(self.groupBox_calibration)
        self.lineEdit_ch2point1.setObjectName(u"lineEdit_ch2point1")
        sizePolicy3.setHeightForWidth(self.lineEdit_ch2point1.sizePolicy().hasHeightForWidth())
        self.lineEdit_ch2point1.setSizePolicy(sizePolicy3)
        self.lineEdit_ch2point1.setMaxLength(5)

        self.horizontalLayout_ch2calibration.addWidget(self.lineEdit_ch2point1)

        self.pushButton_ch2point1 = QPushButton(self.groupBox_calibration)
        self.pushButton_ch2point1.setObjectName(u"pushButton_ch2point1")
        sizePolicy5.setHeightForWidth(self.pushButton_ch2point1.sizePolicy().hasHeightForWidth())
        self.pushButton_ch2point1.setSizePolicy(sizePolicy5)

        self.horizontalLayout_ch2calibration.addWidget(self.pushButton_ch2point1)

        self.lineEdit_ch2point2 = QLineEdit(self.groupBox_calibration)
        self.lineEdit_ch2point2.setObjectName(u"lineEdit_ch2point2")
        sizePolicy3.setHeightForWidth(self.lineEdit_ch2point2.sizePolicy().hasHeightForWidth())
        self.lineEdit_ch2point2.setSizePolicy(sizePolicy3)
        self.lineEdit_ch2point2.setMaxLength(5)

        self.horizontalLayout_ch2calibration.addWidget(self.lineEdit_ch2point2)

        self.pushButton_ch2point2 = QPushButton(self.groupBox_calibration)
        self.pushButton_ch2point2.setObjectName(u"pushButton_ch2point2")
        sizePolicy5.setHeightForWidth(self.pushButton_ch2point2.sizePolicy().hasHeightForWidth())
        self.pushButton_ch2point2.setSizePolicy(sizePolicy5)

        self.horizontalLayout_ch2calibration.addWidget(self.pushButton_ch2point2)

        self.lineEdit_ch2point3 = QLineEdit(self.groupBox_calibration)
        self.lineEdit_ch2point3.setObjectName(u"lineEdit_ch2point3")
        sizePolicy3.setHeightForWidth(self.lineEdit_ch2point3.sizePolicy().hasHeightForWidth())
        self.lineEdit_ch2point3.setSizePolicy(sizePolicy3)
        self.lineEdit_ch2point3.setMaxLength(5)

        self.horizontalLayout_ch2calibration.addWidget(self.lineEdit_ch2point3)

        self.pushButton_ch2point3 = QPushButton(self.groupBox_calibration)
        self.pushButton_ch2point3.setObjectName(u"pushButton_ch2point3")
        sizePolicy5.setHeightForWidth(self.pushButton_ch2point3.sizePolicy().hasHeightForWidth())
        self.pushButton_ch2point3.setSizePolicy(sizePolicy5)

        self.horizontalLayout_ch2calibration.addWidget(self.pushButton_ch2point3)

        self.lineEdit_ch2point4 = QLineEdit(self.groupBox_calibration)
        self.lineEdit_ch2point4.setObjectName(u"lineEdit_ch2point4")
        sizePolicy3.setHeightForWidth(self.lineEdit_ch2point4.sizePolicy().hasHeightForWidth())
        self.lineEdit_ch2point4.setSizePolicy(sizePolicy3)
        self.lineEdit_ch2point4.setMaxLength(5)

        self.horizontalLayout_ch2calibration.addWidget(self.lineEdit_ch2point4)

        self.pushButton_ch2point4 = QPushButton(self.groupBox_calibration)
        self.pushButton_ch2point4.setObjectName(u"pushButton_ch2point4")
        sizePolicy5.setHeightForWidth(self.pushButton_ch2point4.sizePolicy().hasHeightForWidth())
        self.pushButton_ch2point4.setSizePolicy(sizePolicy5)

        self.horizontalLayout_ch2calibration.addWidget(self.pushButton_ch2point4)

        self.lineEdit_ch2point5 = QLineEdit(self.groupBox_calibration)
        self.lineEdit_ch2point5.setObjectName(u"lineEdit_ch2point5")
        sizePolicy3.setHeightForWidth(self.lineEdit_ch2point5.sizePolicy().hasHeightForWidth())
        self.lineEdit_ch2point5.setSizePolicy(sizePolicy3)
        self.lineEdit_ch2point5.setMaxLength(5)

        self.horizontalLayout_ch2calibration.addWidget(self.lineEdit_ch2point5)

        self.pushButton_ch2point5 = QPushButton(self.groupBox_calibration)
        self.pushButton_ch2point5.setObjectName(u"pushButton_ch2point5")
        sizePolicy5.setHeightForWidth(self.pushButton_ch2point5.sizePolicy().hasHeightForWidth())
        self.pushButton_ch2point5.setSizePolicy(sizePolicy5)

        self.horizontalLayout_ch2calibration.addWidget(self.pushButton_ch2point5)

        self.comboBox_ch2CalScale = QComboBox(self.groupBox_calibration)
        self.comboBox_ch2CalScale.addItem("")
        self.comboBox_ch2CalScale.addItem("")
        self.comboBox_ch2CalScale.setObjectName(u"comboBox_ch2CalScale")

        self.horizontalLayout_ch2calibration.addWidget(self.comboBox_ch2CalScale)

        self.horizontalLayout_ch2calibration.setStretch(0, 1)
        self.horizontalLayout_ch2calibration.setStretch(1, 1)
        self.horizontalLayout_ch2calibration.setStretch(2, 1)
        self.horizontalLayout_ch2calibration.setStretch(3, 1)
        self.horizontalLayout_ch2calibration.setStretch(4, 1)
        self.horizontalLayout_ch2calibration.setStretch(5, 1)
        self.horizontalLayout_ch2calibration.setStretch(6, 1)
        self.horizontalLayout_ch2calibration.setStretch(7, 1)
        self.horizontalLayout_ch2calibration.setStretch(8, 1)
        self.horizontalLayout_ch2calibration.setStretch(9, 1)
        self.horizontalLayout_ch2calibration.setStretch(10, 1)

        self.gridLayout_4.addLayout(self.horizontalLayout_ch2calibration, 2, 0, 1, 1)

        self.horizontalLayout_ch4calibration = QHBoxLayout()
        self.horizontalLayout_ch4calibration.setSpacing(10)
        self.horizontalLayout_ch4calibration.setObjectName(u"horizontalLayout_ch4calibration")
        self.label_ch4calibration = QLabel(self.groupBox_calibration)
        self.label_ch4calibration.setObjectName(u"label_ch4calibration")
        sizePolicy6.setHeightForWidth(self.label_ch4calibration.sizePolicy().hasHeightForWidth())
        self.label_ch4calibration.setSizePolicy(sizePolicy6)

        self.horizontalLayout_ch4calibration.addWidget(self.label_ch4calibration)

        self.lineEdit_ch4point1 = QLineEdit(self.groupBox_calibration)
        self.lineEdit_ch4point1.setObjectName(u"lineEdit_ch4point1")
        sizePolicy3.setHeightForWidth(self.lineEdit_ch4point1.sizePolicy().hasHeightForWidth())
        self.lineEdit_ch4point1.setSizePolicy(sizePolicy3)
        self.lineEdit_ch4point1.setMaxLength(5)

        self.horizontalLayout_ch4calibration.addWidget(self.lineEdit_ch4point1)

        self.pushButton_ch4point1 = QPushButton(self.groupBox_calibration)
        self.pushButton_ch4point1.setObjectName(u"pushButton_ch4point1")
        sizePolicy5.setHeightForWidth(self.pushButton_ch4point1.sizePolicy().hasHeightForWidth())
        self.pushButton_ch4point1.setSizePolicy(sizePolicy5)

        self.horizontalLayout_ch4calibration.addWidget(self.pushButton_ch4point1)

        self.lineEdit_ch4point2 = QLineEdit(self.groupBox_calibration)
        self.lineEdit_ch4point2.setObjectName(u"lineEdit_ch4point2")
        sizePolicy3.setHeightForWidth(self.lineEdit_ch4point2.sizePolicy().hasHeightForWidth())
        self.lineEdit_ch4point2.setSizePolicy(sizePolicy3)
        self.lineEdit_ch4point2.setMaxLength(5)

        self.horizontalLayout_ch4calibration.addWidget(self.lineEdit_ch4point2)

        self.pushButton_ch4point2 = QPushButton(self.groupBox_calibration)
        self.pushButton_ch4point2.setObjectName(u"pushButton_ch4point2")
        sizePolicy5.setHeightForWidth(self.pushButton_ch4point2.sizePolicy().hasHeightForWidth())
        self.pushButton_ch4point2.setSizePolicy(sizePolicy5)

        self.horizontalLayout_ch4calibration.addWidget(self.pushButton_ch4point2)

        self.lineEdit_ch4point3 = QLineEdit(self.groupBox_calibration)
        self.lineEdit_ch4point3.setObjectName(u"lineEdit_ch4point3")
        sizePolicy3.setHeightForWidth(self.lineEdit_ch4point3.sizePolicy().hasHeightForWidth())
        self.lineEdit_ch4point3.setSizePolicy(sizePolicy3)
        self.lineEdit_ch4point3.setMaxLength(5)

        self.horizontalLayout_ch4calibration.addWidget(self.lineEdit_ch4point3)

        self.pushButton_ch4point3 = QPushButton(self.groupBox_calibration)
        self.pushButton_ch4point3.setObjectName(u"pushButton_ch4point3")
        sizePolicy5.setHeightForWidth(self.pushButton_ch4point3.sizePolicy().hasHeightForWidth())
        self.pushButton_ch4point3.setSizePolicy(sizePolicy5)

        self.horizontalLayout_ch4calibration.addWidget(self.pushButton_ch4point3)

        self.lineEdit_ch4point4 = QLineEdit(self.groupBox_calibration)
        self.lineEdit_ch4point4.setObjectName(u"lineEdit_ch4point4")
        sizePolicy3.setHeightForWidth(self.lineEdit_ch4point4.sizePolicy().hasHeightForWidth())
        self.lineEdit_ch4point4.setSizePolicy(sizePolicy3)
        self.lineEdit_ch4point4.setMaxLength(5)

        self.horizontalLayout_ch4calibration.addWidget(self.lineEdit_ch4point4)

        self.pushButton_ch4point4 = QPushButton(self.groupBox_calibration)
        self.pushButton_ch4point4.setObjectName(u"pushButton_ch4point4")
        sizePolicy5.setHeightForWidth(self.pushButton_ch4point4.sizePolicy().hasHeightForWidth())
        self.pushButton_ch4point4.setSizePolicy(sizePolicy5)

        self.horizontalLayout_ch4calibration.addWidget(self.pushButton_ch4point4)

        self.lineEdit_ch4point5 = QLineEdit(self.groupBox_calibration)
        self.lineEdit_ch4point5.setObjectName(u"lineEdit_ch4point5")
        sizePolicy3.setHeightForWidth(self.lineEdit_ch4point5.sizePolicy().hasHeightForWidth())
        self.lineEdit_ch4point5.setSizePolicy(sizePolicy3)
        self.lineEdit_ch4point5.setMaxLength(5)

        self.horizontalLayout_ch4calibration.addWidget(self.lineEdit_ch4point5)

        self.pushButton_ch4point5 = QPushButton(self.groupBox_calibration)
        self.pushButton_ch4point5.setObjectName(u"pushButton_ch4point5")
        sizePolicy5.setHeightForWidth(self.pushButton_ch4point5.sizePolicy().hasHeightForWidth())
        self.pushButton_ch4point5.setSizePolicy(sizePolicy5)

        self.horizontalLayout_ch4calibration.addWidget(self.pushButton_ch4point5)

        self.comboBox_ch4CalScale = QComboBox(self.groupBox_calibration)
        self.comboBox_ch4CalScale.addItem("")
        self.comboBox_ch4CalScale.addItem("")
        self.comboBox_ch4CalScale.setObjectName(u"comboBox_ch4CalScale")

        self.horizontalLayout_ch4calibration.addWidget(self.comboBox_ch4CalScale)

        self.horizontalLayout_ch4calibration.setStretch(0, 1)
        self.horizontalLayout_ch4calibration.setStretch(1, 1)
        self.horizontalLayout_ch4calibration.setStretch(2, 1)
        self.horizontalLayout_ch4calibration.setStretch(3, 1)
        self.horizontalLayout_ch4calibration.setStretch(4, 1)
        self.horizontalLayout_ch4calibration.setStretch(5, 1)
        self.horizontalLayout_ch4calibration.setStretch(6, 1)
        self.horizontalLayout_ch4calibration.setStretch(7, 1)
        self.horizontalLayout_ch4calibration.setStretch(8, 1)
        self.horizontalLayout_ch4calibration.setStretch(9, 1)
        self.horizontalLayout_ch4calibration.setStretch(10, 1)

        self.gridLayout_4.addLayout(self.horizontalLayout_ch4calibration, 4, 0, 1, 1)

        self.horizontalLayout_ch5calibration = QHBoxLayout()
        self.horizontalLayout_ch5calibration.setSpacing(10)
        self.horizontalLayout_ch5calibration.setObjectName(u"horizontalLayout_ch5calibration")
        self.label_ch5calibration = QLabel(self.groupBox_calibration)
        self.label_ch5calibration.setObjectName(u"label_ch5calibration")
        sizePolicy6.setHeightForWidth(self.label_ch5calibration.sizePolicy().hasHeightForWidth())
        self.label_ch5calibration.setSizePolicy(sizePolicy6)

        self.horizontalLayout_ch5calibration.addWidget(self.label_ch5calibration)

        self.lineEdit_ch5point1 = QLineEdit(self.groupBox_calibration)
        self.lineEdit_ch5point1.setObjectName(u"lineEdit_ch5point1")
        sizePolicy3.setHeightForWidth(self.lineEdit_ch5point1.sizePolicy().hasHeightForWidth())
        self.lineEdit_ch5point1.setSizePolicy(sizePolicy3)
        self.lineEdit_ch5point1.setMaxLength(5)

        self.horizontalLayout_ch5calibration.addWidget(self.lineEdit_ch5point1)

        self.pushButton_ch5point1 = QPushButton(self.groupBox_calibration)
        self.pushButton_ch5point1.setObjectName(u"pushButton_ch5point1")
        sizePolicy5.setHeightForWidth(self.pushButton_ch5point1.sizePolicy().hasHeightForWidth())
        self.pushButton_ch5point1.setSizePolicy(sizePolicy5)

        self.horizontalLayout_ch5calibration.addWidget(self.pushButton_ch5point1)

        self.lineEdit_ch5point2 = QLineEdit(self.groupBox_calibration)
        self.lineEdit_ch5point2.setObjectName(u"lineEdit_ch5point2")
        sizePolicy3.setHeightForWidth(self.lineEdit_ch5point2.sizePolicy().hasHeightForWidth())
        self.lineEdit_ch5point2.setSizePolicy(sizePolicy3)
        self.lineEdit_ch5point2.setMaxLength(5)

        self.horizontalLayout_ch5calibration.addWidget(self.lineEdit_ch5point2)

        self.pushButton_ch5point2 = QPushButton(self.groupBox_calibration)
        self.pushButton_ch5point2.setObjectName(u"pushButton_ch5point2")
        sizePolicy5.setHeightForWidth(self.pushButton_ch5point2.sizePolicy().hasHeightForWidth())
        self.pushButton_ch5point2.setSizePolicy(sizePolicy5)

        self.horizontalLayout_ch5calibration.addWidget(self.pushButton_ch5point2)

        self.lineEdit_ch5point3 = QLineEdit(self.groupBox_calibration)
        self.lineEdit_ch5point3.setObjectName(u"lineEdit_ch5point3")
        sizePolicy3.setHeightForWidth(self.lineEdit_ch5point3.sizePolicy().hasHeightForWidth())
        self.lineEdit_ch5point3.setSizePolicy(sizePolicy3)
        self.lineEdit_ch5point3.setMaxLength(5)

        self.horizontalLayout_ch5calibration.addWidget(self.lineEdit_ch5point3)

        self.pushButton_ch5point3 = QPushButton(self.groupBox_calibration)
        self.pushButton_ch5point3.setObjectName(u"pushButton_ch5point3")
        sizePolicy5.setHeightForWidth(self.pushButton_ch5point3.sizePolicy().hasHeightForWidth())
        self.pushButton_ch5point3.setSizePolicy(sizePolicy5)

        self.horizontalLayout_ch5calibration.addWidget(self.pushButton_ch5point3)

        self.lineEdit_ch5point4 = QLineEdit(self.groupBox_calibration)
        self.lineEdit_ch5point4.setObjectName(u"lineEdit_ch5point4")
        sizePolicy3.setHeightForWidth(self.lineEdit_ch5point4.sizePolicy().hasHeightForWidth())
        self.lineEdit_ch5point4.setSizePolicy(sizePolicy3)
        self.lineEdit_ch5point4.setMaxLength(5)

        self.horizontalLayout_ch5calibration.addWidget(self.lineEdit_ch5point4)

        self.pushButton_ch5point4 = QPushButton(self.groupBox_calibration)
        self.pushButton_ch5point4.setObjectName(u"pushButton_ch5point4")
        sizePolicy5.setHeightForWidth(self.pushButton_ch5point4.sizePolicy().hasHeightForWidth())
        self.pushButton_ch5point4.setSizePolicy(sizePolicy5)

        self.horizontalLayout_ch5calibration.addWidget(self.pushButton_ch5point4)

        self.lineEdit_ch5point5 = QLineEdit(self.groupBox_calibration)
        self.lineEdit_ch5point5.setObjectName(u"lineEdit_ch5point5")
        sizePolicy3.setHeightForWidth(self.lineEdit_ch5point5.sizePolicy().hasHeightForWidth())
        self.lineEdit_ch5point5.setSizePolicy(sizePolicy3)
        self.lineEdit_ch5point5.setMaxLength(5)

        self.horizontalLayout_ch5calibration.addWidget(self.lineEdit_ch5point5)

        self.pushButton_ch5point5 = QPushButton(self.groupBox_calibration)
        self.pushButton_ch5point5.setObjectName(u"pushButton_ch5point5")
        sizePolicy5.setHeightForWidth(self.pushButton_ch5point5.sizePolicy().hasHeightForWidth())
        self.pushButton_ch5point5.setSizePolicy(sizePolicy5)

        self.horizontalLayout_ch5calibration.addWidget(self.pushButton_ch5point5)

        self.comboBox_ch5CalScale = QComboBox(self.groupBox_calibration)
        self.comboBox_ch5CalScale.addItem("")
        self.comboBox_ch5CalScale.addItem("")
        self.comboBox_ch5CalScale.setObjectName(u"comboBox_ch5CalScale")

        self.horizontalLayout_ch5calibration.addWidget(self.comboBox_ch5CalScale)

        self.horizontalLayout_ch5calibration.setStretch(0, 1)
        self.horizontalLayout_ch5calibration.setStretch(1, 1)
        self.horizontalLayout_ch5calibration.setStretch(2, 1)
        self.horizontalLayout_ch5calibration.setStretch(3, 1)
        self.horizontalLayout_ch5calibration.setStretch(4, 1)
        self.horizontalLayout_ch5calibration.setStretch(5, 1)
        self.horizontalLayout_ch5calibration.setStretch(6, 1)
        self.horizontalLayout_ch5calibration.setStretch(7, 1)
        self.horizontalLayout_ch5calibration.setStretch(8, 1)
        self.horizontalLayout_ch5calibration.setStretch(9, 1)
        self.horizontalLayout_ch5calibration.setStretch(10, 1)

        self.gridLayout_4.addLayout(self.horizontalLayout_ch5calibration, 5, 0, 1, 1)

        self.horizontalLayout_ch6calibration = QHBoxLayout()
        self.horizontalLayout_ch6calibration.setSpacing(10)
        self.horizontalLayout_ch6calibration.setObjectName(u"horizontalLayout_ch6calibration")
        self.label_ch6calibration = QLabel(self.groupBox_calibration)
        self.label_ch6calibration.setObjectName(u"label_ch6calibration")
        sizePolicy6.setHeightForWidth(self.label_ch6calibration.sizePolicy().hasHeightForWidth())
        self.label_ch6calibration.setSizePolicy(sizePolicy6)

        self.horizontalLayout_ch6calibration.addWidget(self.label_ch6calibration)

        self.lineEdit_ch6point1 = QLineEdit(self.groupBox_calibration)
        self.lineEdit_ch6point1.setObjectName(u"lineEdit_ch6point1")
        sizePolicy3.setHeightForWidth(self.lineEdit_ch6point1.sizePolicy().hasHeightForWidth())
        self.lineEdit_ch6point1.setSizePolicy(sizePolicy3)
        self.lineEdit_ch6point1.setMaxLength(5)

        self.horizontalLayout_ch6calibration.addWidget(self.lineEdit_ch6point1)

        self.pushButton_ch6point1 = QPushButton(self.groupBox_calibration)
        self.pushButton_ch6point1.setObjectName(u"pushButton_ch6point1")
        sizePolicy5.setHeightForWidth(self.pushButton_ch6point1.sizePolicy().hasHeightForWidth())
        self.pushButton_ch6point1.setSizePolicy(sizePolicy5)

        self.horizontalLayout_ch6calibration.addWidget(self.pushButton_ch6point1)

        self.lineEdit_ch6point2 = QLineEdit(self.groupBox_calibration)
        self.lineEdit_ch6point2.setObjectName(u"lineEdit_ch6point2")
        sizePolicy3.setHeightForWidth(self.lineEdit_ch6point2.sizePolicy().hasHeightForWidth())
        self.lineEdit_ch6point2.setSizePolicy(sizePolicy3)
        self.lineEdit_ch6point2.setMaxLength(5)

        self.horizontalLayout_ch6calibration.addWidget(self.lineEdit_ch6point2)

        self.pushButton_ch6point2 = QPushButton(self.groupBox_calibration)
        self.pushButton_ch6point2.setObjectName(u"pushButton_ch6point2")
        sizePolicy5.setHeightForWidth(self.pushButton_ch6point2.sizePolicy().hasHeightForWidth())
        self.pushButton_ch6point2.setSizePolicy(sizePolicy5)

        self.horizontalLayout_ch6calibration.addWidget(self.pushButton_ch6point2)

        self.lineEdit_ch6point3 = QLineEdit(self.groupBox_calibration)
        self.lineEdit_ch6point3.setObjectName(u"lineEdit_ch6point3")
        sizePolicy3.setHeightForWidth(self.lineEdit_ch6point3.sizePolicy().hasHeightForWidth())
        self.lineEdit_ch6point3.setSizePolicy(sizePolicy3)
        self.lineEdit_ch6point3.setMaxLength(5)

        self.horizontalLayout_ch6calibration.addWidget(self.lineEdit_ch6point3)

        self.pushButton_ch6point3 = QPushButton(self.groupBox_calibration)
        self.pushButton_ch6point3.setObjectName(u"pushButton_ch6point3")
        sizePolicy5.setHeightForWidth(self.pushButton_ch6point3.sizePolicy().hasHeightForWidth())
        self.pushButton_ch6point3.setSizePolicy(sizePolicy5)

        self.horizontalLayout_ch6calibration.addWidget(self.pushButton_ch6point3)

        self.lineEdit_ch6point4 = QLineEdit(self.groupBox_calibration)
        self.lineEdit_ch6point4.setObjectName(u"lineEdit_ch6point4")
        sizePolicy3.setHeightForWidth(self.lineEdit_ch6point4.sizePolicy().hasHeightForWidth())
        self.lineEdit_ch6point4.setSizePolicy(sizePolicy3)
        self.lineEdit_ch6point4.setMaxLength(5)

        self.horizontalLayout_ch6calibration.addWidget(self.lineEdit_ch6point4)

        self.pushButton_ch6point4 = QPushButton(self.groupBox_calibration)
        self.pushButton_ch6point4.setObjectName(u"pushButton_ch6point4")
        sizePolicy5.setHeightForWidth(self.pushButton_ch6point4.sizePolicy().hasHeightForWidth())
        self.pushButton_ch6point4.setSizePolicy(sizePolicy5)

        self.horizontalLayout_ch6calibration.addWidget(self.pushButton_ch6point4)

        self.lineEdit_ch6point5 = QLineEdit(self.groupBox_calibration)
        self.lineEdit_ch6point5.setObjectName(u"lineEdit_ch6point5")
        sizePolicy3.setHeightForWidth(self.lineEdit_ch6point5.sizePolicy().hasHeightForWidth())
        self.lineEdit_ch6point5.setSizePolicy(sizePolicy3)
        self.lineEdit_ch6point5.setMaxLength(5)

        self.horizontalLayout_ch6calibration.addWidget(self.lineEdit_ch6point5)

        self.pushButton_ch6point5 = QPushButton(self.groupBox_calibration)
        self.pushButton_ch6point5.setObjectName(u"pushButton_ch6point5")
        sizePolicy5.setHeightForWidth(self.pushButton_ch6point5.sizePolicy().hasHeightForWidth())
        self.pushButton_ch6point5.setSizePolicy(sizePolicy5)

        self.horizontalLayout_ch6calibration.addWidget(self.pushButton_ch6point5)

        self.comboBox_ch6CalScale = QComboBox(self.groupBox_calibration)
        self.comboBox_ch6CalScale.addItem("")
        self.comboBox_ch6CalScale.addItem("")
        self.comboBox_ch6CalScale.setObjectName(u"comboBox_ch6CalScale")

        self.horizontalLayout_ch6calibration.addWidget(self.comboBox_ch6CalScale)

        self.horizontalLayout_ch6calibration.setStretch(0, 1)
        self.horizontalLayout_ch6calibration.setStretch(1, 1)
        self.horizontalLayout_ch6calibration.setStretch(2, 1)
        self.horizontalLayout_ch6calibration.setStretch(3, 1)
        self.horizontalLayout_ch6calibration.setStretch(4, 1)
        self.horizontalLayout_ch6calibration.setStretch(5, 1)
        self.horizontalLayout_ch6calibration.setStretch(6, 1)
        self.horizontalLayout_ch6calibration.setStretch(7, 1)
        self.horizontalLayout_ch6calibration.setStretch(8, 1)
        self.horizontalLayout_ch6calibration.setStretch(9, 1)
        self.horizontalLayout_ch6calibration.setStretch(10, 1)

        self.gridLayout_4.addLayout(self.horizontalLayout_ch6calibration, 6, 0, 1, 1)

        self.horizontalLayout_Points = QHBoxLayout()
        self.horizontalLayout_Points.setSpacing(10)
        self.horizontalLayout_Points.setObjectName(u"horizontalLayout_Points")
        self.label_3 = QLabel(self.groupBox_calibration)
        self.label_3.setObjectName(u"label_3")
        sizePolicy6.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy6)

        self.horizontalLayout_Points.addWidget(self.label_3)

        self.label_point1 = QLabel(self.groupBox_calibration)
        self.label_point1.setObjectName(u"label_point1")
        sizePolicy3.setHeightForWidth(self.label_point1.sizePolicy().hasHeightForWidth())
        self.label_point1.setSizePolicy(sizePolicy3)

        self.horizontalLayout_Points.addWidget(self.label_point1, 0, Qt.AlignHCenter)

        self.label_4 = QLabel(self.groupBox_calibration)
        self.label_4.setObjectName(u"label_4")
        sizePolicy6.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy6)

        self.horizontalLayout_Points.addWidget(self.label_4)

        self.label_point2 = QLabel(self.groupBox_calibration)
        self.label_point2.setObjectName(u"label_point2")
        sizePolicy3.setHeightForWidth(self.label_point2.sizePolicy().hasHeightForWidth())
        self.label_point2.setSizePolicy(sizePolicy3)

        self.horizontalLayout_Points.addWidget(self.label_point2, 0, Qt.AlignHCenter)

        self.label_5 = QLabel(self.groupBox_calibration)
        self.label_5.setObjectName(u"label_5")
        sizePolicy6.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy6)

        self.horizontalLayout_Points.addWidget(self.label_5)

        self.label_point3 = QLabel(self.groupBox_calibration)
        self.label_point3.setObjectName(u"label_point3")
        sizePolicy3.setHeightForWidth(self.label_point3.sizePolicy().hasHeightForWidth())
        self.label_point3.setSizePolicy(sizePolicy3)

        self.horizontalLayout_Points.addWidget(self.label_point3, 0, Qt.AlignHCenter)

        self.label_6 = QLabel(self.groupBox_calibration)
        self.label_6.setObjectName(u"label_6")
        sizePolicy6.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy6)

        self.horizontalLayout_Points.addWidget(self.label_6)

        self.label_point4 = QLabel(self.groupBox_calibration)
        self.label_point4.setObjectName(u"label_point4")
        sizePolicy3.setHeightForWidth(self.label_point4.sizePolicy().hasHeightForWidth())
        self.label_point4.setSizePolicy(sizePolicy3)

        self.horizontalLayout_Points.addWidget(self.label_point4, 0, Qt.AlignHCenter)

        self.label_7 = QLabel(self.groupBox_calibration)
        self.label_7.setObjectName(u"label_7")
        sizePolicy6.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy6)

        self.horizontalLayout_Points.addWidget(self.label_7)

        self.label_point5 = QLabel(self.groupBox_calibration)
        self.label_point5.setObjectName(u"label_point5")
        sizePolicy3.setHeightForWidth(self.label_point5.sizePolicy().hasHeightForWidth())
        self.label_point5.setSizePolicy(sizePolicy3)

        self.horizontalLayout_Points.addWidget(self.label_point5, 0, Qt.AlignHCenter)

        self.label_8 = QLabel(self.groupBox_calibration)
        self.label_8.setObjectName(u"label_8")
        sizePolicy6.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy6)

        self.horizontalLayout_Points.addWidget(self.label_8)

        self.label_PointsUnit = QLabel(self.groupBox_calibration)
        self.label_PointsUnit.setObjectName(u"label_PointsUnit")
        sizePolicy7.setHeightForWidth(self.label_PointsUnit.sizePolicy().hasHeightForWidth())
        self.label_PointsUnit.setSizePolicy(sizePolicy7)

        self.horizontalLayout_Points.addWidget(self.label_PointsUnit, 0, Qt.AlignHCenter)

        self.horizontalLayout_Points.setStretch(0, 2)
        self.horizontalLayout_Points.setStretch(1, 3)
        self.horizontalLayout_Points.setStretch(2, 2)
        self.horizontalLayout_Points.setStretch(3, 3)
        self.horizontalLayout_Points.setStretch(4, 2)
        self.horizontalLayout_Points.setStretch(5, 3)
        self.horizontalLayout_Points.setStretch(6, 2)
        self.horizontalLayout_Points.setStretch(7, 3)
        self.horizontalLayout_Points.setStretch(8, 2)
        self.horizontalLayout_Points.setStretch(9, 3)
        self.horizontalLayout_Points.setStretch(10, 2)
        self.horizontalLayout_Points.setStretch(11, 2)

        self.gridLayout_4.addLayout(self.horizontalLayout_Points, 0, 0, 1, 1)


        self.gridLayout_calibration.addWidget(self.groupBox_calibration, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.calibration)
        self.log = QWidget()
        self.log.setObjectName(u"log")
        self.gridLayout_log = QGridLayout(self.log)
        self.gridLayout_log.setObjectName(u"gridLayout_log")
        self.frame_log = QFrame(self.log)
        self.frame_log.setObjectName(u"frame_log")
        self.frame_log.setFrameShape(QFrame.StyledPanel)
        self.frame_log.setFrameShadow(QFrame.Raised)
        self.gridLayout_6 = QGridLayout(self.frame_log)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.tableWidget_log = QTableWidget(self.frame_log)
        if (self.tableWidget_log.columnCount() < 5):
            self.tableWidget_log.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget_log.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget_log.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget_log.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget_log.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget_log.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        if (self.tableWidget_log.rowCount() < 1):
            self.tableWidget_log.setRowCount(1)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget_log.setVerticalHeaderItem(0, __qtablewidgetitem5)
        self.tableWidget_log.setObjectName(u"tableWidget_log")
        self.tableWidget_log.setFrameShape(QFrame.StyledPanel)
        self.tableWidget_log.setFrameShadow(QFrame.Plain)
        self.tableWidget_log.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget_log.setShowGrid(True)
        self.tableWidget_log.setGridStyle(Qt.SolidLine)
        self.tableWidget_log.setWordWrap(True)
        self.tableWidget_log.setCornerButtonEnabled(False)
        self.tableWidget_log.horizontalHeader().setVisible(True)
        self.tableWidget_log.horizontalHeader().setMinimumSectionSize(50)
        self.tableWidget_log.horizontalHeader().setDefaultSectionSize(100)
        self.tableWidget_log.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_log.verticalHeader().setMinimumSectionSize(30)

        self.gridLayout_6.addWidget(self.tableWidget_log, 0, 0, 1, 1)


        self.gridLayout_log.addWidget(self.frame_log, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.log)
        self.widgets = QWidget()
        self.widgets.setObjectName(u"widgets")
        self.widgets.setStyleSheet(u"b")
        self.verticalLayout = QVBoxLayout(self.widgets)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.row_1 = QFrame(self.widgets)
        self.row_1.setObjectName(u"row_1")
        self.row_1.setFrameShape(QFrame.StyledPanel)
        self.row_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.row_1)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.frame_div_content_1 = QFrame(self.row_1)
        self.frame_div_content_1.setObjectName(u"frame_div_content_1")
        self.frame_div_content_1.setMinimumSize(QSize(0, 110))
        self.frame_div_content_1.setMaximumSize(QSize(16777215, 110))
        self.frame_div_content_1.setFrameShape(QFrame.NoFrame)
        self.frame_div_content_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_div_content_1)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.frame_title_wid_1 = QFrame(self.frame_div_content_1)
        self.frame_title_wid_1.setObjectName(u"frame_title_wid_1")
        self.frame_title_wid_1.setMaximumSize(QSize(16777215, 35))
        self.frame_title_wid_1.setFrameShape(QFrame.StyledPanel)
        self.frame_title_wid_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_title_wid_1)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.labelBoxBlenderInstalation = QLabel(self.frame_title_wid_1)
        self.labelBoxBlenderInstalation.setObjectName(u"labelBoxBlenderInstalation")
        self.labelBoxBlenderInstalation.setFont(font1)
        self.labelBoxBlenderInstalation.setStyleSheet(u"")

        self.verticalLayout_18.addWidget(self.labelBoxBlenderInstalation)


        self.verticalLayout_17.addWidget(self.frame_title_wid_1)

        self.frame_content_wid_1 = QFrame(self.frame_div_content_1)
        self.frame_content_wid_1.setObjectName(u"frame_content_wid_1")
        self.frame_content_wid_1.setFrameShape(QFrame.NoFrame)
        self.frame_content_wid_1.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_content_wid_1)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(-1, -1, -1, 0)
        self.lineEdit = QLineEdit(self.frame_content_wid_1)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(0, 30))
        self.lineEdit.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.gridLayout.addWidget(self.lineEdit, 0, 0, 1, 1)

        self.pushButton = QPushButton(self.frame_content_wid_1)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(150, 30))
        self.pushButton.setFont(font1)
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        icon4 = QIcon()
        icon4.addFile(u":/icons/images/icons/cil-folder-open.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon4)

        self.gridLayout.addWidget(self.pushButton, 0, 1, 1, 1)

        self.labelVersion_3 = QLabel(self.frame_content_wid_1)
        self.labelVersion_3.setObjectName(u"labelVersion_3")
        self.labelVersion_3.setStyleSheet(u"color: rgb(113, 126, 149);")
        self.labelVersion_3.setLineWidth(1)
        self.labelVersion_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.labelVersion_3, 1, 0, 1, 2)


        self.horizontalLayout_9.addLayout(self.gridLayout)


        self.verticalLayout_17.addWidget(self.frame_content_wid_1)


        self.verticalLayout_16.addWidget(self.frame_div_content_1)


        self.verticalLayout.addWidget(self.row_1)

        self.row_2 = QFrame(self.widgets)
        self.row_2.setObjectName(u"row_2")
        self.row_2.setMinimumSize(QSize(0, 150))
        self.row_2.setFrameShape(QFrame.StyledPanel)
        self.row_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.row_2)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.checkBox = QCheckBox(self.row_2)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setAutoFillBackground(False)
        self.checkBox.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.checkBox, 0, 0, 1, 1)

        self.radioButton = QRadioButton(self.row_2)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.radioButton, 0, 1, 1, 1)

        self.verticalSlider = QSlider(self.row_2)
        self.verticalSlider.setObjectName(u"verticalSlider")
        self.verticalSlider.setStyleSheet(u"")
        self.verticalSlider.setOrientation(Qt.Vertical)

        self.gridLayout_2.addWidget(self.verticalSlider, 0, 2, 3, 1)

        self.verticalScrollBar = QScrollBar(self.row_2)
        self.verticalScrollBar.setObjectName(u"verticalScrollBar")
        self.verticalScrollBar.setStyleSheet(u" QScrollBar:vertical { background: rgb(52, 59, 72); }\n"
" QScrollBar:horizontal { background: rgb(52, 59, 72); }")
        self.verticalScrollBar.setOrientation(Qt.Vertical)

        self.gridLayout_2.addWidget(self.verticalScrollBar, 0, 4, 3, 1)

        self.scrollArea = QScrollArea(self.row_2)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u" QScrollBar:vertical {\n"
"    background: rgb(52, 59, 72);\n"
" }\n"
" QScrollBar:horizontal {\n"
"    background: rgb(52, 59, 72);\n"
" }")
        self.scrollArea.setFrameShape(QFrame.NoFrame)
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 218, 218))
        self.scrollAreaWidgetContents.setStyleSheet(u" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }")
        self.horizontalLayout_11 = QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.plainTextEdit = QPlainTextEdit(self.scrollAreaWidgetContents)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setMinimumSize(QSize(200, 200))
        self.plainTextEdit.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.horizontalLayout_11.addWidget(self.plainTextEdit)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_2.addWidget(self.scrollArea, 0, 5, 3, 1)

        self.comboBox = QComboBox(self.row_2)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setFont(font1)
        self.comboBox.setAutoFillBackground(False)
        self.comboBox.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.comboBox.setIconSize(QSize(16, 16))
        self.comboBox.setFrame(True)

        self.gridLayout_2.addWidget(self.comboBox, 1, 0, 1, 2)

        self.horizontalScrollBar = QScrollBar(self.row_2)
        self.horizontalScrollBar.setObjectName(u"horizontalScrollBar")
        sizePolicy.setHeightForWidth(self.horizontalScrollBar.sizePolicy().hasHeightForWidth())
        self.horizontalScrollBar.setSizePolicy(sizePolicy)
        self.horizontalScrollBar.setStyleSheet(u" QScrollBar:vertical { background: rgb(52, 59, 72); }\n"
" QScrollBar:horizontal { background: rgb(52, 59, 72); }")
        self.horizontalScrollBar.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.horizontalScrollBar, 1, 3, 1, 1)

        self.commandLinkButton = QCommandLinkButton(self.row_2)
        self.commandLinkButton.setObjectName(u"commandLinkButton")
        self.commandLinkButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.commandLinkButton.setStyleSheet(u"")
        icon5 = QIcon()
        icon5.addFile(u":/icons/images/icons/cil-link.png", QSize(), QIcon.Normal, QIcon.Off)
        self.commandLinkButton.setIcon(icon5)

        self.gridLayout_2.addWidget(self.commandLinkButton, 1, 6, 1, 1)

        self.horizontalSlider = QSlider(self.row_2)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setStyleSheet(u"")
        self.horizontalSlider.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.horizontalSlider, 2, 0, 1, 2)


        self.verticalLayout_19.addLayout(self.gridLayout_2)


        self.verticalLayout.addWidget(self.row_2)

        self.row_3 = QFrame(self.widgets)
        self.row_3.setObjectName(u"row_3")
        self.row_3.setMinimumSize(QSize(0, 150))
        self.row_3.setFrameShape(QFrame.StyledPanel)
        self.row_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.row_3)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.tableWidget = QTableWidget(self.row_3)
        if (self.tableWidget.columnCount() < 4):
            self.tableWidget.setColumnCount(4)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem9)
        if (self.tableWidget.rowCount() < 16):
            self.tableWidget.setRowCount(16)
        font5 = QFont()
        __qtablewidgetitem10 = QTableWidgetItem()
        __qtablewidgetitem10.setFont(font5);
        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(8, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(9, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(10, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(11, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(12, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(13, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(14, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(15, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.tableWidget.setItem(0, 0, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.tableWidget.setItem(0, 1, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.tableWidget.setItem(0, 2, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        self.tableWidget.setItem(0, 3, __qtablewidgetitem29)
        self.tableWidget.setObjectName(u"tableWidget")
        sizePolicy8 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy8)
        palette = QPalette()
        brush = QBrush(QColor(221, 221, 221, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(0, 0, 0, 0))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        brush2 = QBrush(QColor(0, 0, 0, 255))
        brush2.setStyle(Qt.NoBrush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush2)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        brush3 = QBrush(QColor(0, 0, 0, 255))
        brush3.setStyle(Qt.NoBrush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        brush4 = QBrush(QColor(0, 0, 0, 255))
        brush4.setStyle(Qt.NoBrush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush)
#endif
        self.tableWidget.setPalette(palette)
        self.tableWidget.setFrameShape(QFrame.NoFrame)
        self.tableWidget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.tableWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setGridStyle(Qt.SolidLine)
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(200)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setHighlightSections(False)
        self.tableWidget.verticalHeader().setStretchLastSection(True)

        self.horizontalLayout_12.addWidget(self.tableWidget)


        self.verticalLayout.addWidget(self.row_3)

        self.stackedWidget.addWidget(self.widgets)

        self.verticalLayout_15.addWidget(self.stackedWidget)


        self.horizontalLayout_4.addWidget(self.pagesContainer)

        self.extraRightBox = QFrame(self.content)
        self.extraRightBox.setObjectName(u"extraRightBox")
        self.extraRightBox.setMinimumSize(QSize(0, 0))
        self.extraRightBox.setMaximumSize(QSize(0, 16777215))
        self.extraRightBox.setFrameShape(QFrame.NoFrame)
        self.extraRightBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.extraRightBox)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.themeSettingsTopDetail = QFrame(self.extraRightBox)
        self.themeSettingsTopDetail.setObjectName(u"themeSettingsTopDetail")
        self.themeSettingsTopDetail.setMaximumSize(QSize(16777215, 3))
        self.themeSettingsTopDetail.setFrameShape(QFrame.NoFrame)
        self.themeSettingsTopDetail.setFrameShadow(QFrame.Raised)

        self.verticalLayout_7.addWidget(self.themeSettingsTopDetail)

        self.contentSettings = QFrame(self.extraRightBox)
        self.contentSettings.setObjectName(u"contentSettings")
        self.contentSettings.setFrameShape(QFrame.NoFrame)
        self.contentSettings.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.contentSettings)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.topMenus = QFrame(self.contentSettings)
        self.topMenus.setObjectName(u"topMenus")
        self.topMenus.setFrameShape(QFrame.NoFrame)
        self.topMenus.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.topMenus)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.btn_message = QPushButton(self.topMenus)
        self.btn_message.setObjectName(u"btn_message")
        sizePolicy.setHeightForWidth(self.btn_message.sizePolicy().hasHeightForWidth())
        self.btn_message.setSizePolicy(sizePolicy)
        self.btn_message.setMinimumSize(QSize(0, 45))
        self.btn_message.setFont(font1)
        self.btn_message.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_message.setLayoutDirection(Qt.LeftToRight)
        self.btn_message.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-envelope-open.png);")

        self.verticalLayout_14.addWidget(self.btn_message)

        self.btn_print = QPushButton(self.topMenus)
        self.btn_print.setObjectName(u"btn_print")
        sizePolicy.setHeightForWidth(self.btn_print.sizePolicy().hasHeightForWidth())
        self.btn_print.setSizePolicy(sizePolicy)
        self.btn_print.setMinimumSize(QSize(0, 45))
        self.btn_print.setFont(font1)
        self.btn_print.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_print.setLayoutDirection(Qt.LeftToRight)
        self.btn_print.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-print.png);")

        self.verticalLayout_14.addWidget(self.btn_print)

        self.btn_logout = QPushButton(self.topMenus)
        self.btn_logout.setObjectName(u"btn_logout")
        sizePolicy.setHeightForWidth(self.btn_logout.sizePolicy().hasHeightForWidth())
        self.btn_logout.setSizePolicy(sizePolicy)
        self.btn_logout.setMinimumSize(QSize(0, 45))
        self.btn_logout.setFont(font1)
        self.btn_logout.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_logout.setLayoutDirection(Qt.LeftToRight)
        self.btn_logout.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-account-logout.png);")

        self.verticalLayout_14.addWidget(self.btn_logout)


        self.verticalLayout_13.addWidget(self.topMenus, 0, Qt.AlignTop)


        self.verticalLayout_7.addWidget(self.contentSettings)


        self.horizontalLayout_4.addWidget(self.extraRightBox)


        self.verticalLayout_6.addWidget(self.content)

        self.bottomBar = QFrame(self.contentBottom)
        self.bottomBar.setObjectName(u"bottomBar")
        self.bottomBar.setMinimumSize(QSize(0, 35))
        self.bottomBar.setMaximumSize(QSize(16777215, 22))
        self.bottomBar.setFrameShape(QFrame.NoFrame)
        self.bottomBar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.bottomBar)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.stateLabel = QLabel(self.bottomBar)
        self.stateLabel.setObjectName(u"stateLabel")
        self.stateLabel.setMaximumSize(QSize(16777215, 16))
        font6 = QFont()
        font6.setBold(False)
        font6.setItalic(False)
        self.stateLabel.setFont(font6)
        self.stateLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.stateLabel)

        self.version = QLabel(self.bottomBar)
        self.version.setObjectName(u"version")
        self.version.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.version)

        self.frame_size_grip = QFrame(self.bottomBar)
        self.frame_size_grip.setObjectName(u"frame_size_grip")
        self.frame_size_grip.setMinimumSize(QSize(20, 0))
        self.frame_size_grip.setMaximumSize(QSize(20, 16777215))
        self.frame_size_grip.setFrameShape(QFrame.NoFrame)
        self.frame_size_grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_5.addWidget(self.frame_size_grip)


        self.verticalLayout_6.addWidget(self.bottomBar)


        self.verticalLayout_2.addWidget(self.contentBottom)


        self.appLayout.addWidget(self.contentBox)


        self.appMargins.addWidget(self.bgApp)

        MainWindow.setCentralWidget(self.styleSheet)
        QWidget.setTabOrder(self.toggleButton, self.lineEdit_ch1)
        QWidget.setTabOrder(self.lineEdit_ch1, self.radioButton_ch1v)
        QWidget.setTabOrder(self.radioButton_ch1v, self.radioButton_ch1i)
        QWidget.setTabOrder(self.radioButton_ch1i, self.lineEdit_ch2)
        QWidget.setTabOrder(self.lineEdit_ch2, self.radioButton_ch2v)
        QWidget.setTabOrder(self.radioButton_ch2v, self.radioButton_ch2i)
        QWidget.setTabOrder(self.radioButton_ch2i, self.lineEdit_ch3)
        QWidget.setTabOrder(self.lineEdit_ch3, self.radioButton_ch3v)
        QWidget.setTabOrder(self.radioButton_ch3v, self.radioButton_ch3i)
        QWidget.setTabOrder(self.radioButton_ch3i, self.lineEdit_ch4)
        QWidget.setTabOrder(self.lineEdit_ch4, self.radioButton_ch4v)
        QWidget.setTabOrder(self.radioButton_ch4v, self.radioButton_ch4i)
        QWidget.setTabOrder(self.radioButton_ch4i, self.lineEdit_ch5)
        QWidget.setTabOrder(self.lineEdit_ch5, self.radioButton_ch5v)
        QWidget.setTabOrder(self.radioButton_ch5v, self.radioButton_ch5i)
        QWidget.setTabOrder(self.radioButton_ch5i, self.lineEdit_ch6)
        QWidget.setTabOrder(self.lineEdit_ch6, self.radioButton_ch6v)
        QWidget.setTabOrder(self.radioButton_ch6v, self.radioButton_ch6i)
        QWidget.setTabOrder(self.radioButton_ch6i, self.lineEdit_ch7)
        QWidget.setTabOrder(self.lineEdit_ch7, self.radioButton_ch7v)
        QWidget.setTabOrder(self.radioButton_ch7v, self.radioButton_ch7i)
        QWidget.setTabOrder(self.radioButton_ch7i, self.lineEdit_ch8)
        QWidget.setTabOrder(self.lineEdit_ch8, self.radioButton_ch8v)
        QWidget.setTabOrder(self.radioButton_ch8v, self.radioButton_ch8i)
        QWidget.setTabOrder(self.radioButton_ch8i, self.checkBox_65535)
        QWidget.setTabOrder(self.checkBox_65535, self.pushButton_connect)
        QWidget.setTabOrder(self.pushButton_connect, self.pushButton_disconnect)
        QWidget.setTabOrder(self.pushButton_disconnect, self.btn_home)
        QWidget.setTabOrder(self.btn_home, self.btn_setting)
        QWidget.setTabOrder(self.btn_setting, self.btn_calibration)
        QWidget.setTabOrder(self.btn_calibration, self.btn_log)
        QWidget.setTabOrder(self.btn_log, self.btn_trend)
        QWidget.setTabOrder(self.btn_trend, self.btn_save)
        QWidget.setTabOrder(self.btn_save, self.minimizeAppBtn)
        QWidget.setTabOrder(self.minimizeAppBtn, self.maximizeRestoreAppBtn)
        QWidget.setTabOrder(self.maximizeRestoreAppBtn, self.closeAppBtn)
        QWidget.setTabOrder(self.closeAppBtn, self.settingsTopBtn)
        QWidget.setTabOrder(self.settingsTopBtn, self.lineEdit_unitID)
        QWidget.setTabOrder(self.lineEdit_unitID, self.lineEdit_timeout)
        QWidget.setTabOrder(self.lineEdit_timeout, self.lineEdit_ResRate)
        QWidget.setTabOrder(self.lineEdit_ResRate, self.lineEdit_ch1vLow)
        QWidget.setTabOrder(self.lineEdit_ch1vLow, self.lineEdit_ch1vHigh)
        QWidget.setTabOrder(self.lineEdit_ch1vHigh, self.lineEdit_ch2vLow)
        QWidget.setTabOrder(self.lineEdit_ch2vLow, self.lineEdit_ch2vHigh)
        QWidget.setTabOrder(self.lineEdit_ch2vHigh, self.lineEdit_ch3vLow)
        QWidget.setTabOrder(self.lineEdit_ch3vLow, self.lineEdit_ch3vHigh)
        QWidget.setTabOrder(self.lineEdit_ch3vHigh, self.lineEdit_ch4vLow)
        QWidget.setTabOrder(self.lineEdit_ch4vLow, self.lineEdit_ch4vHigh)
        QWidget.setTabOrder(self.lineEdit_ch4vHigh, self.lineEdit_ch5vLow)
        QWidget.setTabOrder(self.lineEdit_ch5vLow, self.lineEdit_ch5vHigh)
        QWidget.setTabOrder(self.lineEdit_ch5vHigh, self.lineEdit_ch6vLow)
        QWidget.setTabOrder(self.lineEdit_ch6vLow, self.lineEdit_ch6vHigh)
        QWidget.setTabOrder(self.lineEdit_ch6vHigh, self.lineEdit_ch7vLow)
        QWidget.setTabOrder(self.lineEdit_ch7vLow, self.lineEdit_ch7vHigh)
        QWidget.setTabOrder(self.lineEdit_ch7vHigh, self.lineEdit_ch8vLow)
        QWidget.setTabOrder(self.lineEdit_ch8vLow, self.lineEdit_ch8vHigh)
        QWidget.setTabOrder(self.lineEdit_ch8vHigh, self.lineEdit_ch1point1)
        QWidget.setTabOrder(self.lineEdit_ch1point1, self.pushButton_ch1point1)
        QWidget.setTabOrder(self.pushButton_ch1point1, self.lineEdit_ch1point2)
        QWidget.setTabOrder(self.lineEdit_ch1point2, self.pushButton_ch1point2)
        QWidget.setTabOrder(self.pushButton_ch1point2, self.lineEdit_ch1point3)
        QWidget.setTabOrder(self.lineEdit_ch1point3, self.pushButton_ch1point3)
        QWidget.setTabOrder(self.pushButton_ch1point3, self.lineEdit_ch1point4)
        QWidget.setTabOrder(self.lineEdit_ch1point4, self.pushButton_ch1point4)
        QWidget.setTabOrder(self.pushButton_ch1point4, self.lineEdit_ch1point5)
        QWidget.setTabOrder(self.lineEdit_ch1point5, self.pushButton_ch1point5)
        QWidget.setTabOrder(self.pushButton_ch1point5, self.lineEdit_ch2point1)
        QWidget.setTabOrder(self.lineEdit_ch2point1, self.pushButton_ch2point1)
        QWidget.setTabOrder(self.pushButton_ch2point1, self.lineEdit_ch2point2)
        QWidget.setTabOrder(self.lineEdit_ch2point2, self.pushButton_ch2point2)
        QWidget.setTabOrder(self.pushButton_ch2point2, self.lineEdit_ch2point3)
        QWidget.setTabOrder(self.lineEdit_ch2point3, self.pushButton_ch2point3)
        QWidget.setTabOrder(self.pushButton_ch2point3, self.lineEdit_ch2point4)
        QWidget.setTabOrder(self.lineEdit_ch2point4, self.pushButton_ch2point4)
        QWidget.setTabOrder(self.pushButton_ch2point4, self.lineEdit_ch2point5)
        QWidget.setTabOrder(self.lineEdit_ch2point5, self.pushButton_ch2point5)
        QWidget.setTabOrder(self.pushButton_ch2point5, self.lineEdit_ch3point1)
        QWidget.setTabOrder(self.lineEdit_ch3point1, self.pushButton_ch3point1)
        QWidget.setTabOrder(self.pushButton_ch3point1, self.lineEdit_ch3point2)
        QWidget.setTabOrder(self.lineEdit_ch3point2, self.pushButton_ch3point2)
        QWidget.setTabOrder(self.pushButton_ch3point2, self.lineEdit_ch3point3)
        QWidget.setTabOrder(self.lineEdit_ch3point3, self.pushButton_ch3point3)
        QWidget.setTabOrder(self.pushButton_ch3point3, self.lineEdit_ch3point4)
        QWidget.setTabOrder(self.lineEdit_ch3point4, self.pushButton_ch3point4)
        QWidget.setTabOrder(self.pushButton_ch3point4, self.lineEdit_ch3point5)
        QWidget.setTabOrder(self.lineEdit_ch3point5, self.pushButton_ch3point5)
        QWidget.setTabOrder(self.pushButton_ch3point5, self.lineEdit_ch4point1)
        QWidget.setTabOrder(self.lineEdit_ch4point1, self.pushButton_ch4point1)
        QWidget.setTabOrder(self.pushButton_ch4point1, self.lineEdit_ch4point2)
        QWidget.setTabOrder(self.lineEdit_ch4point2, self.pushButton_ch4point2)
        QWidget.setTabOrder(self.pushButton_ch4point2, self.lineEdit_ch4point3)
        QWidget.setTabOrder(self.lineEdit_ch4point3, self.pushButton_ch4point3)
        QWidget.setTabOrder(self.pushButton_ch4point3, self.lineEdit_ch4point4)
        QWidget.setTabOrder(self.lineEdit_ch4point4, self.pushButton_ch4point4)
        QWidget.setTabOrder(self.pushButton_ch4point4, self.lineEdit_ch4point5)
        QWidget.setTabOrder(self.lineEdit_ch4point5, self.pushButton_ch4point5)
        QWidget.setTabOrder(self.pushButton_ch4point5, self.lineEdit_ch5point1)
        QWidget.setTabOrder(self.lineEdit_ch5point1, self.pushButton_ch5point1)
        QWidget.setTabOrder(self.pushButton_ch5point1, self.lineEdit_ch5point2)
        QWidget.setTabOrder(self.lineEdit_ch5point2, self.pushButton_ch5point2)
        QWidget.setTabOrder(self.pushButton_ch5point2, self.lineEdit_ch5point3)
        QWidget.setTabOrder(self.lineEdit_ch5point3, self.pushButton_ch5point3)
        QWidget.setTabOrder(self.pushButton_ch5point3, self.lineEdit_ch5point4)
        QWidget.setTabOrder(self.lineEdit_ch5point4, self.pushButton_ch5point4)
        QWidget.setTabOrder(self.pushButton_ch5point4, self.lineEdit_ch5point5)
        QWidget.setTabOrder(self.lineEdit_ch5point5, self.pushButton_ch5point5)
        QWidget.setTabOrder(self.pushButton_ch5point5, self.lineEdit_ch6point1)
        QWidget.setTabOrder(self.lineEdit_ch6point1, self.pushButton_ch6point1)
        QWidget.setTabOrder(self.pushButton_ch6point1, self.lineEdit_ch6point2)
        QWidget.setTabOrder(self.lineEdit_ch6point2, self.pushButton_ch6point2)
        QWidget.setTabOrder(self.pushButton_ch6point2, self.lineEdit_ch6point3)
        QWidget.setTabOrder(self.lineEdit_ch6point3, self.pushButton_ch6point3)
        QWidget.setTabOrder(self.pushButton_ch6point3, self.lineEdit_ch6point4)
        QWidget.setTabOrder(self.lineEdit_ch6point4, self.pushButton_ch6point4)
        QWidget.setTabOrder(self.pushButton_ch6point4, self.lineEdit_ch6point5)
        QWidget.setTabOrder(self.lineEdit_ch6point5, self.pushButton_ch6point5)
        QWidget.setTabOrder(self.pushButton_ch6point5, self.lineEdit_ch7point1)
        QWidget.setTabOrder(self.lineEdit_ch7point1, self.pushButton_ch7point1)
        QWidget.setTabOrder(self.pushButton_ch7point1, self.lineEdit_ch7point2)
        QWidget.setTabOrder(self.lineEdit_ch7point2, self.pushButton_ch7point2)
        QWidget.setTabOrder(self.pushButton_ch7point2, self.lineEdit_ch7point3)
        QWidget.setTabOrder(self.lineEdit_ch7point3, self.pushButton_ch7point3)
        QWidget.setTabOrder(self.pushButton_ch7point3, self.lineEdit_ch7point4)
        QWidget.setTabOrder(self.lineEdit_ch7point4, self.pushButton_ch7point4)
        QWidget.setTabOrder(self.pushButton_ch7point4, self.lineEdit_ch7point5)
        QWidget.setTabOrder(self.lineEdit_ch7point5, self.pushButton_ch7point5)
        QWidget.setTabOrder(self.pushButton_ch7point5, self.lineEdit_ch8point1)
        QWidget.setTabOrder(self.lineEdit_ch8point1, self.pushButton_ch8point1)
        QWidget.setTabOrder(self.pushButton_ch8point1, self.lineEdit_ch8point2)
        QWidget.setTabOrder(self.lineEdit_ch8point2, self.pushButton_ch8point2)
        QWidget.setTabOrder(self.pushButton_ch8point2, self.lineEdit_ch8point3)
        QWidget.setTabOrder(self.lineEdit_ch8point3, self.pushButton_ch8point3)
        QWidget.setTabOrder(self.pushButton_ch8point3, self.lineEdit_ch8point4)
        QWidget.setTabOrder(self.lineEdit_ch8point4, self.pushButton_ch8point4)
        QWidget.setTabOrder(self.pushButton_ch8point4, self.lineEdit_ch8point5)
        QWidget.setTabOrder(self.lineEdit_ch8point5, self.pushButton_ch8point5)
        QWidget.setTabOrder(self.pushButton_ch8point5, self.toggleLeftBox)
        QWidget.setTabOrder(self.toggleLeftBox, self.extraCloseColumnBtn)
        QWidget.setTabOrder(self.extraCloseColumnBtn, self.btn_adjustments)
        QWidget.setTabOrder(self.btn_adjustments, self.btn_more)
        QWidget.setTabOrder(self.btn_more, self.btn_share)
        QWidget.setTabOrder(self.btn_share, self.tableWidget_log)
        QWidget.setTabOrder(self.tableWidget_log, self.lineEdit)
        QWidget.setTabOrder(self.lineEdit, self.pushButton)
        QWidget.setTabOrder(self.pushButton, self.checkBox)
        QWidget.setTabOrder(self.checkBox, self.radioButton)
        QWidget.setTabOrder(self.radioButton, self.verticalSlider)
        QWidget.setTabOrder(self.verticalSlider, self.scrollArea)
        QWidget.setTabOrder(self.scrollArea, self.plainTextEdit)
        QWidget.setTabOrder(self.plainTextEdit, self.comboBox)
        QWidget.setTabOrder(self.comboBox, self.commandLinkButton)
        QWidget.setTabOrder(self.commandLinkButton, self.horizontalSlider)
        QWidget.setTabOrder(self.horizontalSlider, self.tableWidget)
        QWidget.setTabOrder(self.tableWidget, self.btn_message)
        QWidget.setTabOrder(self.btn_message, self.btn_print)
        QWidget.setTabOrder(self.btn_print, self.btn_logout)
        QWidget.setTabOrder(self.btn_logout, self.textEdit)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)
        self.comboBox_baudRate.setCurrentIndex(11)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.titleLeftApp.setText(QCoreApplication.translate("MainWindow", u"Ayra", None))
        self.titleLeftDescription.setText(QCoreApplication.translate("MainWindow", u"GUI for Adam (By PyDracula)", None))
        self.topLogo.setText("")
        self.toggleButton.setText(QCoreApplication.translate("MainWindow", u"Hide", None))
        self.btn_home.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.btn_setting.setText(QCoreApplication.translate("MainWindow", u"Setting", None))
        self.btn_calibration.setText(QCoreApplication.translate("MainWindow", u"Calibration", None))
        self.btn_log.setText(QCoreApplication.translate("MainWindow", u"Log", None))
        self.btn_trend.setText(QCoreApplication.translate("MainWindow", u"Trend", None))
        self.btn_save.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.toggleLeftBox.setText(QCoreApplication.translate("MainWindow", u"Left Box", None))
        self.extraLabel.setText(QCoreApplication.translate("MainWindow", u"Left Box", None))
#if QT_CONFIG(tooltip)
        self.extraCloseColumnBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close left box", None))
#endif // QT_CONFIG(tooltip)
        self.extraCloseColumnBtn.setText("")
        self.btn_share.setText(QCoreApplication.translate("MainWindow", u"Share", None))
        self.btn_adjustments.setText(QCoreApplication.translate("MainWindow", u"Adjustments", None))
        self.btn_more.setText(QCoreApplication.translate("MainWindow", u"More", None))
        self.textEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; color:#ff79c6;\">PyDracula</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; color:#ffffff;\">An interface created using Python and PySide (support for PyQt), and with colors based on the Dracula theme created by Zeno Rocha.</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-inde"
                        "nt:0; text-indent:0px;\"><span style=\" font-size:10pt; color:#ffffff;\">MIT License</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; color:#bd93f9;\">Created by: Wanderson M. Pimenta</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; color:#ff79c6;\">Convert UI</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; color:#ffffff;\">pyside6-uic main.ui &gt; ui_main.py</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; color:#ff79c6;\">Convert QRC</span></p>\n"
"<p align=\"center\" "
                        "style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; color:#ffffff;\">pyside6-rcc resources.qrc -o resources_rc.py</span></p></body></html>", None))
        self.titleRightInfo.setText(QCoreApplication.translate("MainWindow", u"Connection Setup (Based on ModBus)", None))
#if QT_CONFIG(tooltip)
        self.settingsTopBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Settings", None))
#endif // QT_CONFIG(tooltip)
        self.settingsTopBtn.setText("")
#if QT_CONFIG(tooltip)
        self.minimizeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.minimizeAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Maximize", None))
#endif // QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.closeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.closeAppBtn.setText("")
        self.label_ch6.setText(QCoreApplication.translate("MainWindow", u"Channel 6:", None))
        self.label_ch6scale.setText(QCoreApplication.translate("MainWindow", u"V", None))
        self.radioButton_ch6v.setText("")
        self.radioButton_ch6i.setText("")
        self.label_ch8.setText(QCoreApplication.translate("MainWindow", u"Channel 8:", None))
        self.label_ch8scale.setText(QCoreApplication.translate("MainWindow", u"V", None))
        self.radioButton_ch8v.setText("")
        self.radioButton_ch8i.setText("")
        self.label_ch7.setText(QCoreApplication.translate("MainWindow", u"Channel 7:", None))
        self.label_ch7scale.setText(QCoreApplication.translate("MainWindow", u"V", None))
        self.radioButton_ch7v.setText("")
        self.radioButton_ch7i.setText("")
        self.label_ch5.setText(QCoreApplication.translate("MainWindow", u"Channel 5:", None))
        self.label_ch5scale.setText(QCoreApplication.translate("MainWindow", u"V", None))
        self.radioButton_ch5v.setText("")
        self.radioButton_ch5i.setText("")
        self.label_ch2.setText(QCoreApplication.translate("MainWindow", u"Channel 2:", None))
        self.label_ch2scale.setText(QCoreApplication.translate("MainWindow", u"V", None))
        self.radioButton_ch2v.setText("")
        self.radioButton_ch2i.setText("")
        self.label_ch3.setText(QCoreApplication.translate("MainWindow", u"Channel 3:", None))
        self.label_ch3scale.setText(QCoreApplication.translate("MainWindow", u"V", None))
        self.radioButton_ch3v.setText("")
        self.radioButton_ch3i.setText("")
        self.label_ch1.setText(QCoreApplication.translate("MainWindow", u"Channel 1:", None))
        self.label_ch1scale.setText(QCoreApplication.translate("MainWindow", u"V", None))
        self.radioButton_ch1v.setText("")
        self.radioButton_ch1i.setText("")
        self.label_ch4.setText(QCoreApplication.translate("MainWindow", u"Channel 4:", None))
        self.label_ch4scale.setText(QCoreApplication.translate("MainWindow", u"V", None))
        self.radioButton_ch4v.setText("")
        self.radioButton_ch4i.setText("")
        self.pushButton_connect.setText(QCoreApplication.translate("MainWindow", u"Connect", None))
        self.pushButton_disconnect.setText(QCoreApplication.translate("MainWindow", u"Disconnect", None))
        self.checkBox_65535.setText(QCoreApplication.translate("MainWindow", u"0-65535 scale", None))
        self.label_model.setText(QCoreApplication.translate("MainWindow", u"Model:", None))
        self.label_deviceModel.setText(QCoreApplication.translate("MainWindow", u"Model", None))
        self.label_vol.setText(QCoreApplication.translate("MainWindow", u"Voltage", None))
        self.label_cur.setText(QCoreApplication.translate("MainWindow", u"Current", None))
        self.comboBox_ch6scale.setItemText(0, QCoreApplication.translate("MainWindow", u"V", None))
        self.comboBox_ch6scale.setItemText(1, QCoreApplication.translate("MainWindow", u"mV", None))
        self.comboBox_ch6scale.setItemText(2, QCoreApplication.translate("MainWindow", u"mA", None))

        self.label_minScale.setText(QCoreApplication.translate("MainWindow", u"Min", None))
        self.label_maxScale.setText(QCoreApplication.translate("MainWindow", u"Max", None))
        self.label_vScale.setText(QCoreApplication.translate("MainWindow", u"Scales", None))
        self.comboBox_ch8scale.setItemText(0, QCoreApplication.translate("MainWindow", u"V", None))
        self.comboBox_ch8scale.setItemText(1, QCoreApplication.translate("MainWindow", u"mV", None))
        self.comboBox_ch8scale.setItemText(2, QCoreApplication.translate("MainWindow", u"mA", None))

        self.label_ch8vScaleDash.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_timeout.setText(QCoreApplication.translate("MainWindow", u"Timeout:", None))
        self.label_ch1Setting.setText(QCoreApplication.translate("MainWindow", u"Channel 1:", None))
        self.label_ch4vScaleDash.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.comboBox_ch7scale.setItemText(0, QCoreApplication.translate("MainWindow", u"V", None))
        self.comboBox_ch7scale.setItemText(1, QCoreApplication.translate("MainWindow", u"mV", None))
        self.comboBox_ch7scale.setItemText(2, QCoreApplication.translate("MainWindow", u"mA", None))

        self.label_ch3Setting.setText(QCoreApplication.translate("MainWindow", u"Channel 3:", None))
        self.label_unitID.setText(QCoreApplication.translate("MainWindow", u"Unit ID:", None))
        self.label_ch5vScaleDash.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.comboBox_ch1scale.setItemText(0, QCoreApplication.translate("MainWindow", u"V", None))
        self.comboBox_ch1scale.setItemText(1, QCoreApplication.translate("MainWindow", u"mV", None))
        self.comboBox_ch1scale.setItemText(2, QCoreApplication.translate("MainWindow", u"mA", None))

        self.label_ch7vScaleDash.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_deviceModelSetting.setText(QCoreApplication.translate("MainWindow", u"Model", None))
        self.label_ch1vScaleDash.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_ResRate.setText(QCoreApplication.translate("MainWindow", u"Response Rate:", None))
        self.label_ch6Setting.setText(QCoreApplication.translate("MainWindow", u"Channel 6:", None))
        self.comboBox_ch4scale.setItemText(0, QCoreApplication.translate("MainWindow", u"V", None))
        self.comboBox_ch4scale.setItemText(1, QCoreApplication.translate("MainWindow", u"mV", None))
        self.comboBox_ch4scale.setItemText(2, QCoreApplication.translate("MainWindow", u"mA", None))

        self.comboBox_ch5scale.setItemText(0, QCoreApplication.translate("MainWindow", u"V", None))
        self.comboBox_ch5scale.setItemText(1, QCoreApplication.translate("MainWindow", u"mV", None))
        self.comboBox_ch5scale.setItemText(2, QCoreApplication.translate("MainWindow", u"mA", None))

        self.label_baudRate.setText(QCoreApplication.translate("MainWindow", u"Baud Rate:", None))
        self.comboBox_baudRate.setItemText(0, QCoreApplication.translate("MainWindow", u"300", None))
        self.comboBox_baudRate.setItemText(1, QCoreApplication.translate("MainWindow", u"600", None))
        self.comboBox_baudRate.setItemText(2, QCoreApplication.translate("MainWindow", u"1200", None))
        self.comboBox_baudRate.setItemText(3, QCoreApplication.translate("MainWindow", u"2400", None))
        self.comboBox_baudRate.setItemText(4, QCoreApplication.translate("MainWindow", u"4800", None))
        self.comboBox_baudRate.setItemText(5, QCoreApplication.translate("MainWindow", u"9600", None))
        self.comboBox_baudRate.setItemText(6, QCoreApplication.translate("MainWindow", u"14400", None))
        self.comboBox_baudRate.setItemText(7, QCoreApplication.translate("MainWindow", u"19200", None))
        self.comboBox_baudRate.setItemText(8, QCoreApplication.translate("MainWindow", u"38400", None))
        self.comboBox_baudRate.setItemText(9, QCoreApplication.translate("MainWindow", u"56000", None))
        self.comboBox_baudRate.setItemText(10, QCoreApplication.translate("MainWindow", u"57600", None))
        self.comboBox_baudRate.setItemText(11, QCoreApplication.translate("MainWindow", u"115200", None))
        self.comboBox_baudRate.setItemText(12, QCoreApplication.translate("MainWindow", u"128000", None))
        self.comboBox_baudRate.setItemText(13, QCoreApplication.translate("MainWindow", u"153600", None))
        self.comboBox_baudRate.setItemText(14, QCoreApplication.translate("MainWindow", u"230400", None))
        self.comboBox_baudRate.setItemText(15, QCoreApplication.translate("MainWindow", u"256000", None))
        self.comboBox_baudRate.setItemText(16, QCoreApplication.translate("MainWindow", u"460800", None))
        self.comboBox_baudRate.setItemText(17, QCoreApplication.translate("MainWindow", u"921600", None))

        self.label_ch2vScaleDash.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.comboBox_ch3scale.setItemText(0, QCoreApplication.translate("MainWindow", u"V", None))
        self.comboBox_ch3scale.setItemText(1, QCoreApplication.translate("MainWindow", u"mV", None))
        self.comboBox_ch3scale.setItemText(2, QCoreApplication.translate("MainWindow", u"mA", None))

        self.label_ch7Setting.setText(QCoreApplication.translate("MainWindow", u"Channel 7:", None))
        self.label_ch3vScaleDash.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.comboBox_ch2scale.setItemText(0, QCoreApplication.translate("MainWindow", u"V", None))
        self.comboBox_ch2scale.setItemText(1, QCoreApplication.translate("MainWindow", u"mV", None))
        self.comboBox_ch2scale.setItemText(2, QCoreApplication.translate("MainWindow", u"mA", None))

        self.label_ch2Setting.setText(QCoreApplication.translate("MainWindow", u"Channel 2:", None))
        self.label_ch4Setting.setText(QCoreApplication.translate("MainWindow", u"Channel 4:", None))
        self.label_ch5Setting.setText(QCoreApplication.translate("MainWindow", u"Channel 5:", None))
        self.label_ch6vScaleDash.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_ch8Setting.setText(QCoreApplication.translate("MainWindow", u"Channel 8:", None))
        self.groupBox_calibration.setTitle(QCoreApplication.translate("MainWindow", u"Calibration Values", None))
        self.label_ch1calibration.setText(QCoreApplication.translate("MainWindow", u"Channel 1:", None))
        self.pushButton_ch1point1.setText(QCoreApplication.translate("MainWindow", u"Set", None))
        self.pushButton_ch1point2.setText(QCoreApplication.translate("MainWindow", u"Set", None))
        self.pushButton_ch1point3.setText(QCoreApplication.translate("MainWindow", u"Set", None))
        self.pushButton_ch1point4.setText(QCoreApplication.translate("MainWindow", u"Set", None))
        self.pushButton_ch1point5.setText(QCoreApplication.translate("MainWindow", u"Set", None))
        self.comboBox_ch1CalScale.setItemText(0, QCoreApplication.translate("MainWindow", u"v", None))
        self.comboBox_ch1CalScale.setItemText(1, QCoreApplication.translate("MainWindow", u"i", None))

        self.label_ch3calibration.setText(QCoreApplication.translate("MainWindow", u"Channel 3:", None))
        self.pushButton_ch3point1.setText(QCoreApplication.translate("MainWindow", u"Set", None))
        self.pushButton_ch3point2.setText(QCoreApplication.translate("MainWindow", u"Set", None))
        self.pushButton_ch3point3.setText(QCoreApplication.translate("MainWindow", u"Set", None))
        self.pushButton_ch3point4.setText(QCoreApplication.translate("MainWindow", u"Set", None))
        self.pushButton_ch3point5.setText(QCoreApplication.translate("MainWindow", u"Set", None))
        self.comboBox_ch3CalScale.setItemText(0, QCoreApplication.translate("MainWindow", u"v", None))
        self.comboBox_ch3CalScale.setItemText(1, QCoreApplication.translate("MainWindow", u"i", None))

        self.label_ch8calibration.setText(QCoreApplication.translate("MainWindow", u"Channel 8:", None))
        self.pushButton_ch8point1.setText(QCoreApplication.translate("MainWindow", u"Set", None))
        self.pushButton_ch8point2.setText(QCoreApplication.translate("MainWindow", u"Set", None))
        self.pushButton_ch8point3.setText(QCoreApplication.translate("MainWindow", u"Set", None))
        self.pushButton_ch8point4.setText(QCoreApplication.translate("MainWindow", u"Set", None))
        self.pushButton_ch8point5.setText(QCoreApplication.translate("MainWindow", u"Set", None))
        self.comboBox_ch8CalScale.setItemText(0, QCoreApplication.translate("MainWindow", u"v", None))
        self.comboBox_ch8CalScale.setItemText(1, QCoreApplication.translate("MainWindow", u"i", None))

        self.label_ch7calibration.setText(QCoreApplication.translate("MainWindow", u"Channel 7:", None))
        self.pushButton_ch7point1.setText(QCoreApplication.translate("MainWindow", u"Set", None))
        self.pushButton_ch7point2.setText(QCoreApplication.translate("MainWindow", u"Set", None))
        self.pushButton_ch7point3.setText(QCoreApplication.translate("MainWindow", u"Set", None))
        self.pushButton_ch7point4.setText(QCoreApplication.translate("MainWindow", u"Set", None))
        self.pushButton_ch7point5.setText(QCoreApplication.translate("MainWindow", u"Set", None))
        self.comboBox_ch7CalScale.setItemText(0, QCoreApplication.translate("MainWindow", u"v", None))
        self.comboBox_ch7CalScale.setItemText(1, QCoreApplication.translate("MainWindow", u"i", None))

        self.label_ch2calibration.setText(QCoreApplication.translate("MainWindow", u"Channel 2:", None))
        self.pushButton_ch2point1.setText(QCoreApplication.translate("MainWindow", u"Set", None))
        self.pushButton_ch2point2.setText(QCoreApplication.translate("MainWindow", u"Set", None))
        self.pushButton_ch2point3.setText(QCoreApplication.translate("MainWindow", u"Set", None))
        self.pushButton_ch2point4.setText(QCoreApplication.translate("MainWindow", u"Set", None))
        self.pushButton_ch2point5.setText(QCoreApplication.translate("MainWindow", u"Set", None))
        self.comboBox_ch2CalScale.setItemText(0, QCoreApplication.translate("MainWindow", u"v", None))
        self.comboBox_ch2CalScale.setItemText(1, QCoreApplication.translate("MainWindow", u"i", None))

        self.label_ch4calibration.setText(QCoreApplication.translate("MainWindow", u"Channel 4:", None))
        self.pushButton_ch4point1.setText(QCoreApplication.translate("MainWindow", u"Set", None))
        self.pushButton_ch4point2.setText(QCoreApplication.translate("MainWindow", u"Set", None))
        self.pushButton_ch4point3.setText(QCoreApplication.translate("MainWindow", u"Set", None))
        self.pushButton_ch4point4.setText(QCoreApplication.translate("MainWindow", u"Set", None))
        self.pushButton_ch4point5.setText(QCoreApplication.translate("MainWindow", u"Set", None))
        self.comboBox_ch4CalScale.setItemText(0, QCoreApplication.translate("MainWindow", u"v", None))
        self.comboBox_ch4CalScale.setItemText(1, QCoreApplication.translate("MainWindow", u"i", None))

        self.label_ch5calibration.setText(QCoreApplication.translate("MainWindow", u"Channel 5:", None))
        self.pushButton_ch5point1.setText(QCoreApplication.translate("MainWindow", u"Set", None))
        self.pushButton_ch5point2.setText(QCoreApplication.translate("MainWindow", u"Set", None))
        self.pushButton_ch5point3.setText(QCoreApplication.translate("MainWindow", u"Set", None))
        self.pushButton_ch5point4.setText(QCoreApplication.translate("MainWindow", u"Set", None))
        self.pushButton_ch5point5.setText(QCoreApplication.translate("MainWindow", u"Set", None))
        self.comboBox_ch5CalScale.setItemText(0, QCoreApplication.translate("MainWindow", u"v", None))
        self.comboBox_ch5CalScale.setItemText(1, QCoreApplication.translate("MainWindow", u"i", None))

        self.label_ch6calibration.setText(QCoreApplication.translate("MainWindow", u"Channel 6:", None))
        self.pushButton_ch6point1.setText(QCoreApplication.translate("MainWindow", u"Set", None))
        self.pushButton_ch6point2.setText(QCoreApplication.translate("MainWindow", u"Set", None))
        self.pushButton_ch6point3.setText(QCoreApplication.translate("MainWindow", u"Set", None))
        self.pushButton_ch6point4.setText(QCoreApplication.translate("MainWindow", u"Set", None))
        self.pushButton_ch6point5.setText(QCoreApplication.translate("MainWindow", u"Set", None))
        self.comboBox_ch6CalScale.setItemText(0, QCoreApplication.translate("MainWindow", u"v", None))
        self.comboBox_ch6CalScale.setItemText(1, QCoreApplication.translate("MainWindow", u"i", None))

        self.label_3.setText("")
        self.label_point1.setText(QCoreApplication.translate("MainWindow", u"Point 1", None))
        self.label_4.setText("")
        self.label_point2.setText(QCoreApplication.translate("MainWindow", u"Point 2", None))
        self.label_5.setText("")
        self.label_point3.setText(QCoreApplication.translate("MainWindow", u"Point 3", None))
        self.label_6.setText("")
        self.label_point4.setText(QCoreApplication.translate("MainWindow", u"Point 4", None))
        self.label_7.setText("")
        self.label_point5.setText(QCoreApplication.translate("MainWindow", u"Point 5", None))
        self.label_8.setText("")
        self.label_PointsUnit.setText(QCoreApplication.translate("MainWindow", u"Unit", None))
        ___qtablewidgetitem = self.tableWidget_log.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Date", None));
        ___qtablewidgetitem1 = self.tableWidget_log.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Time", None));
        ___qtablewidgetitem2 = self.tableWidget_log.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Level", None));
        ___qtablewidgetitem3 = self.tableWidget_log.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"State", None));
        ___qtablewidgetitem4 = self.tableWidget_log.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Message", None));
        ___qtablewidgetitem5 = self.tableWidget_log.verticalHeaderItem(0)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"1", None));
        self.labelBoxBlenderInstalation.setText(QCoreApplication.translate("MainWindow", u"FILE BOX", None))
        self.lineEdit.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Type here", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.labelVersion_3.setText(QCoreApplication.translate("MainWindow", u"Label description", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"RadioButton", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Test 1", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Test 2", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Test 3", None))

        self.commandLinkButton.setText(QCoreApplication.translate("MainWindow", u"Link Button", None))
        self.commandLinkButton.setDescription(QCoreApplication.translate("MainWindow", u"Link description", None))
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem7 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem8 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem9 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"3", None));
        ___qtablewidgetitem10 = self.tableWidget.verticalHeaderItem(0)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem11 = self.tableWidget.verticalHeaderItem(1)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem12 = self.tableWidget.verticalHeaderItem(2)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem13 = self.tableWidget.verticalHeaderItem(3)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem14 = self.tableWidget.verticalHeaderItem(4)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem15 = self.tableWidget.verticalHeaderItem(5)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem16 = self.tableWidget.verticalHeaderItem(6)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem17 = self.tableWidget.verticalHeaderItem(7)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem18 = self.tableWidget.verticalHeaderItem(8)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem19 = self.tableWidget.verticalHeaderItem(9)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem20 = self.tableWidget.verticalHeaderItem(10)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem21 = self.tableWidget.verticalHeaderItem(11)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem22 = self.tableWidget.verticalHeaderItem(12)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem23 = self.tableWidget.verticalHeaderItem(13)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem24 = self.tableWidget.verticalHeaderItem(14)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem25 = self.tableWidget.verticalHeaderItem(15)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"New Row", None));

        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        ___qtablewidgetitem26 = self.tableWidget.item(0, 0)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("MainWindow", u"Test", None));
        ___qtablewidgetitem27 = self.tableWidget.item(0, 1)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("MainWindow", u"Text", None));
        ___qtablewidgetitem28 = self.tableWidget.item(0, 2)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("MainWindow", u"Cell", None));
        ___qtablewidgetitem29 = self.tableWidget.item(0, 3)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("MainWindow", u"Line", None));
        self.tableWidget.setSortingEnabled(__sortingEnabled)

        self.btn_message.setText(QCoreApplication.translate("MainWindow", u"Message", None))
        self.btn_print.setText(QCoreApplication.translate("MainWindow", u"Print", None))
        self.btn_logout.setText(QCoreApplication.translate("MainWindow", u"Logout", None))
        self.stateLabel.setText("")
        self.version.setText(QCoreApplication.translate("MainWindow", u"v1.0", None))
    # retranslateUi

