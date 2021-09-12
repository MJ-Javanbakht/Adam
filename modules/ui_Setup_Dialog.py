# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Setup_Dialog.ui'
##
## Created by: Qt User Interface Compiler version 6.1.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore

from . setup_resources_rc import *

class Ui_Setup(object):
    def setupUi(self, Setup):
        if not Setup.objectName():
            Setup.setObjectName(u"Setup")
        Setup.resize(500, 550)
        Setup.setMinimumSize(QSize(500, 550))
        Setup.setStyleSheet(u"QWidget{\n"
"	color: rgb(221, 221, 221);\n"
"	font: 12pt \"Segoe UI\";\n"
"}\n"
"\n"
"QToolTip {\n"
"	color: #ffffff;\n"
"	background-color: rgba(33, 37, 43, 180);\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	background-image: none;\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 2px solid rgb(189, 147, 249);\n"
"	text-align: left;\n"
"	padding-left: 8px;\n"
"	margin: 0px;\n"
"}\n"
"\n"
"#Setup {	\n"
"	background-color: rgb(40, 44, 52);\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* SpinBox */\n"
"QSpinBox {\n"
"	background-color: solid rgb(33, 37, 43);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(20, 20, 20);\n"
"	padding-left: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(189, 147, 249);\n"
"}\n"
"QSpinBox:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QSpinBox:focus {\n"
"	border: 2px solid rgb(150, 150, 150);\n"
"}\n"
"QSpinBox:disabled {\n"
"	background-color: rgb(150, 150,"
                        " 150);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"	color: rgb(100,100,100);\n"
"}\n"
"\n"
"/* LineEdit */\n"
"QLineEdit {\n"
"	background-color: solid rgb(33, 37, 43);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(20, 20, 20);\n"
"	padding-left: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(189, 147, 249);\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(150, 150, 150);\n"
"}\n"
"QLineEdit:disabled {\n"
"	background-color: rgb(150, 150, 150);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"	color: rgb(100,100,100);\n"
"}\n"
"\n"
"/* RadioButton */\n"
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
""
                        "	border: 3px solid rgb(52, 59, 72);	\n"
"}\n"
"QRadioButton:disabled {\n"
"	background-color: rgb(150, 150, 150);\n"
"	color: rgb(100,100,100);\n"
"}\n"
"\n"
"/* ComboBox */\n"
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
"	selection-background-color: rgb(39, 4"
                        "4, 54);\n"
"}\n"
"QComboBox:disabled {\n"
"	background-color: rgb(150, 150, 150);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"	color: rgb(100,100,100);\n"
"}\n"
"\n"
"/* Slider */\n"
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
""
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
"QSlider:disabled {\n"
"	background-color: rgb(150, 150, 150);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"	color: rgb(100,100,100);\n"
"}\n"
"\n"
"/* PushButton */\n"
"QPushButton {\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(150, 150, 150);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}\n"
"QPushButton:disabled {	\n"
"	background-color: rgb(150, 150, 150);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"	color: rgb(1"
                        "00,100,100);\n"
"}\n"
"\n"
"/* Label */\n"
"QLabel:disabled {\n"
"	color: rgb(100,100,100);\n"
"}")
        self.gridLayout_setup = QGridLayout(Setup)
        self.gridLayout_setup.setObjectName(u"gridLayout_setup")
        self.groupBox_ResTout = QGroupBox(Setup)
        self.groupBox_ResTout.setObjectName(u"groupBox_ResTout")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_ResTout.sizePolicy().hasHeightForWidth())
        self.groupBox_ResTout.setSizePolicy(sizePolicy)
        self.groupBox_ResTout.setStyleSheet(u"background-color: transparent;")
        self.horizontalLayout_ResTout = QHBoxLayout(self.groupBox_ResTout)
        self.horizontalLayout_ResTout.setObjectName(u"horizontalLayout_ResTout")
        self.lineEdit_ResTout = QLineEdit(self.groupBox_ResTout)
        self.lineEdit_ResTout.setObjectName(u"lineEdit_ResTout")
        sizePolicy.setHeightForWidth(self.lineEdit_ResTout.sizePolicy().hasHeightForWidth())
        self.lineEdit_ResTout.setSizePolicy(sizePolicy)
        self.lineEdit_ResTout.setInputMethodHints(Qt.ImhNone)
        self.lineEdit_ResTout.setAlignment(Qt.AlignCenter)
        self.lineEdit_ResTout.setReadOnly(False)
        self.lineEdit_ResTout.setPlaceholderText(u"")
        self.lineEdit_ResTout.setClearButtonEnabled(False)

        self.horizontalLayout_ResTout.addWidget(self.lineEdit_ResTout)

        self.label_ResTout = QLabel(self.groupBox_ResTout)
        self.label_ResTout.setObjectName(u"label_ResTout")

        self.horizontalLayout_ResTout.addWidget(self.label_ResTout)


        self.gridLayout_setup.addWidget(self.groupBox_ResTout, 3, 1, 1, 1)

        self.groupBox_Serial = QGroupBox(Setup)
        self.groupBox_Serial.setObjectName(u"groupBox_Serial")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.groupBox_Serial.sizePolicy().hasHeightForWidth())
        self.groupBox_Serial.setSizePolicy(sizePolicy1)
        self.groupBox_Serial.setStyleSheet(u"background-color: transparent;")
        self.gridLayout_Serial = QGridLayout(self.groupBox_Serial)
        self.gridLayout_Serial.setObjectName(u"gridLayout_Serial")
        self.label_COM = QLabel(self.groupBox_Serial)
        self.label_COM.setObjectName(u"label_COM")

        self.gridLayout_Serial.addWidget(self.label_COM, 0, 0, 1, 1)

        self.comboBox_COM = QComboBox(self.groupBox_Serial)
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.addItem("")
        self.comboBox_COM.setObjectName(u"comboBox_COM")
        self.comboBox_COM.setEnabled(True)
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.comboBox_COM.sizePolicy().hasHeightForWidth())
        self.comboBox_COM.setSizePolicy(sizePolicy2)

        self.gridLayout_Serial.addWidget(self.comboBox_COM, 0, 1, 1, 1)

        self.label_BaudRate = QLabel(self.groupBox_Serial)
        self.label_BaudRate.setObjectName(u"label_BaudRate")

        self.gridLayout_Serial.addWidget(self.label_BaudRate, 1, 0, 1, 1)

        self.comboBox_BaudRate = QComboBox(self.groupBox_Serial)
        self.comboBox_BaudRate.addItem("")
        self.comboBox_BaudRate.addItem("")
        self.comboBox_BaudRate.addItem("")
        self.comboBox_BaudRate.addItem("")
        self.comboBox_BaudRate.addItem("")
        self.comboBox_BaudRate.addItem("")
        self.comboBox_BaudRate.addItem("")
        self.comboBox_BaudRate.addItem("")
        self.comboBox_BaudRate.addItem("")
        self.comboBox_BaudRate.addItem("")
        self.comboBox_BaudRate.addItem("")
        self.comboBox_BaudRate.addItem("")
        self.comboBox_BaudRate.addItem("")
        self.comboBox_BaudRate.addItem("")
        self.comboBox_BaudRate.addItem("")
        self.comboBox_BaudRate.addItem("")
        self.comboBox_BaudRate.addItem("")
        self.comboBox_BaudRate.addItem("")
        self.comboBox_BaudRate.setObjectName(u"comboBox_BaudRate")
        sizePolicy1.setHeightForWidth(self.comboBox_BaudRate.sizePolicy().hasHeightForWidth())
        self.comboBox_BaudRate.setSizePolicy(sizePolicy1)
        self.comboBox_BaudRate.setMaxVisibleItems(20)

        self.gridLayout_Serial.addWidget(self.comboBox_BaudRate, 1, 1, 1, 1)

        self.label_DataBits = QLabel(self.groupBox_Serial)
        self.label_DataBits.setObjectName(u"label_DataBits")

        self.gridLayout_Serial.addWidget(self.label_DataBits, 2, 0, 1, 1)

        self.comboBox_DataBits = QComboBox(self.groupBox_Serial)
        self.comboBox_DataBits.addItem("")
        self.comboBox_DataBits.addItem("")
        self.comboBox_DataBits.setObjectName(u"comboBox_DataBits")
        sizePolicy1.setHeightForWidth(self.comboBox_DataBits.sizePolicy().hasHeightForWidth())
        self.comboBox_DataBits.setSizePolicy(sizePolicy1)

        self.gridLayout_Serial.addWidget(self.comboBox_DataBits, 2, 1, 1, 1)

        self.label_Parity = QLabel(self.groupBox_Serial)
        self.label_Parity.setObjectName(u"label_Parity")

        self.gridLayout_Serial.addWidget(self.label_Parity, 3, 0, 1, 1)

        self.comboBox_Parity = QComboBox(self.groupBox_Serial)
        self.comboBox_Parity.addItem("")
        self.comboBox_Parity.addItem("")
        self.comboBox_Parity.addItem("")
        self.comboBox_Parity.setObjectName(u"comboBox_Parity")
        sizePolicy1.setHeightForWidth(self.comboBox_Parity.sizePolicy().hasHeightForWidth())
        self.comboBox_Parity.setSizePolicy(sizePolicy1)

        self.gridLayout_Serial.addWidget(self.comboBox_Parity, 3, 1, 1, 1)

        self.label_StopBits = QLabel(self.groupBox_Serial)
        self.label_StopBits.setObjectName(u"label_StopBits")

        self.gridLayout_Serial.addWidget(self.label_StopBits, 4, 0, 1, 1)

        self.comboBox_StopBits = QComboBox(self.groupBox_Serial)
        self.comboBox_StopBits.addItem("")
        self.comboBox_StopBits.addItem("")
        self.comboBox_StopBits.setObjectName(u"comboBox_StopBits")
        sizePolicy1.setHeightForWidth(self.comboBox_StopBits.sizePolicy().hasHeightForWidth())
        self.comboBox_StopBits.setSizePolicy(sizePolicy1)

        self.gridLayout_Serial.addWidget(self.comboBox_StopBits, 4, 1, 1, 1)


        self.gridLayout_setup.addWidget(self.groupBox_Serial, 1, 0, 3, 1)

        self.groupBox_UnitID = QGroupBox(Setup)
        self.groupBox_UnitID.setObjectName(u"groupBox_UnitID")
        sizePolicy.setHeightForWidth(self.groupBox_UnitID.sizePolicy().hasHeightForWidth())
        self.groupBox_UnitID.setSizePolicy(sizePolicy)
        self.groupBox_UnitID.setStyleSheet(u"background-color: transparent;")
        self.horizontalLayout_SlaveID = QHBoxLayout(self.groupBox_UnitID)
        self.horizontalLayout_SlaveID.setObjectName(u"horizontalLayout_SlaveID")
        self.spinBox_UnitID = QSpinBox(self.groupBox_UnitID)
        self.spinBox_UnitID.setObjectName(u"spinBox_UnitID")
        self.spinBox_UnitID.setEnabled(True)
        self.spinBox_UnitID.setInputMethodHints(Qt.ImhNone)
        self.spinBox_UnitID.setButtonSymbols(QAbstractSpinBox.UpDownArrows)
        self.spinBox_UnitID.setMinimum(1)
        self.spinBox_UnitID.setMaximum(255)
        self.spinBox_UnitID.setValue(1)
        self.spinBox_UnitID.setDisplayIntegerBase(10)

        self.horizontalLayout_SlaveID.addWidget(self.spinBox_UnitID)


        self.gridLayout_setup.addWidget(self.groupBox_UnitID, 2, 1, 1, 1)

        self.verticalLayout_statusBar = QVBoxLayout()
        self.verticalLayout_statusBar.setObjectName(u"verticalLayout_statusBar")

        self.gridLayout_setup.addLayout(self.verticalLayout_statusBar, 5, 0, 1, 2)

        self.groupBox_Connection = QGroupBox(Setup)
        self.groupBox_Connection.setObjectName(u"groupBox_Connection")
        sizePolicy3 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Maximum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.groupBox_Connection.sizePolicy().hasHeightForWidth())
        self.groupBox_Connection.setSizePolicy(sizePolicy3)
        self.groupBox_Connection.setStyleSheet(u"background-color: transparent;")
        self.groupBox_Connection.setFlat(False)
        self.groupBox_Connection.setCheckable(False)
        self.horizontalLayout_Connection = QHBoxLayout(self.groupBox_Connection)
        self.horizontalLayout_Connection.setObjectName(u"horizontalLayout_Connection")
        self.comboBox_Connection = QComboBox(self.groupBox_Connection)
        self.comboBox_Connection.addItem("")
        self.comboBox_Connection.addItem("")
        self.comboBox_Connection.setObjectName(u"comboBox_Connection")
        sizePolicy1.setHeightForWidth(self.comboBox_Connection.sizePolicy().hasHeightForWidth())
        self.comboBox_Connection.setSizePolicy(sizePolicy1)

        self.horizontalLayout_Connection.addWidget(self.comboBox_Connection)


        self.gridLayout_setup.addWidget(self.groupBox_Connection, 0, 0, 1, 1)

        self.verticalLayout_buttons = QVBoxLayout()
        self.verticalLayout_buttons.setObjectName(u"verticalLayout_buttons")
        self.pushButton_ok = QPushButton(Setup)
        self.pushButton_ok.setObjectName(u"pushButton_ok")
        self.pushButton_ok.setEnabled(True)
        sizePolicy4 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Maximum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.pushButton_ok.sizePolicy().hasHeightForWidth())
        self.pushButton_ok.setSizePolicy(sizePolicy4)

        self.verticalLayout_buttons.addWidget(self.pushButton_ok, 0, Qt.AlignVCenter)

        self.pushButton_close = QPushButton(Setup)
        self.pushButton_close.setObjectName(u"pushButton_close")
        sizePolicy4.setHeightForWidth(self.pushButton_close.sizePolicy().hasHeightForWidth())
        self.pushButton_close.setSizePolicy(sizePolicy4)

        self.verticalLayout_buttons.addWidget(self.pushButton_close, 0, Qt.AlignVCenter)


        self.gridLayout_setup.addLayout(self.verticalLayout_buttons, 0, 1, 1, 1)

        self.groupBox_Remote = QGroupBox(Setup)
        self.groupBox_Remote.setObjectName(u"groupBox_Remote")
        self.groupBox_Remote.setEnabled(True)
        sizePolicy.setHeightForWidth(self.groupBox_Remote.sizePolicy().hasHeightForWidth())
        self.groupBox_Remote.setSizePolicy(sizePolicy)
        self.groupBox_Remote.setStyleSheet(u"background-color: transparent;")
        self.gridLayout_remote = QGridLayout(self.groupBox_Remote)
        self.gridLayout_remote.setObjectName(u"gridLayout_remote")
        self.radioButton_IPv4 = QRadioButton(self.groupBox_Remote)
        self.radioButton_IPv4.setObjectName(u"radioButton_IPv4")
        self.radioButton_IPv4.setEnabled(True)
        sizePolicy4.setHeightForWidth(self.radioButton_IPv4.sizePolicy().hasHeightForWidth())
        self.radioButton_IPv4.setSizePolicy(sizePolicy4)
        self.radioButton_IPv4.setSizeIncrement(QSize(0, 0))
        self.radioButton_IPv4.setBaseSize(QSize(0, 0))
        font = QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        self.radioButton_IPv4.setFont(font)
        self.radioButton_IPv4.setChecked(True)

        self.gridLayout_remote.addWidget(self.radioButton_IPv4, 2, 4, 2, 1)

        self.radioButton_IPv6 = QRadioButton(self.groupBox_Remote)
        self.radioButton_IPv6.setObjectName(u"radioButton_IPv6")
        self.radioButton_IPv6.setEnabled(True)
        sizePolicy4.setHeightForWidth(self.radioButton_IPv6.sizePolicy().hasHeightForWidth())
        self.radioButton_IPv6.setSizePolicy(sizePolicy4)
        self.radioButton_IPv6.setFont(font)

        self.gridLayout_remote.addWidget(self.radioButton_IPv6, 4, 4, 1, 1)

        self.lineEdit_ConnectTout = QLineEdit(self.groupBox_Remote)
        self.lineEdit_ConnectTout.setObjectName(u"lineEdit_ConnectTout")
        self.lineEdit_ConnectTout.setEnabled(True)
        sizePolicy.setHeightForWidth(self.lineEdit_ConnectTout.sizePolicy().hasHeightForWidth())
        self.lineEdit_ConnectTout.setSizePolicy(sizePolicy)

        self.gridLayout_remote.addWidget(self.lineEdit_ConnectTout, 3, 2, 2, 1)

        self.label_ConnectToutMS = QLabel(self.groupBox_Remote)
        self.label_ConnectToutMS.setObjectName(u"label_ConnectToutMS")
        self.label_ConnectToutMS.setEnabled(True)
        sizePolicy.setHeightForWidth(self.label_ConnectToutMS.sizePolicy().hasHeightForWidth())
        self.label_ConnectToutMS.setSizePolicy(sizePolicy)

        self.gridLayout_remote.addWidget(self.label_ConnectToutMS, 2, 2, 1, 1)

        self.comboBox_IP = QComboBox(self.groupBox_Remote)
        self.comboBox_IP.addItem("")
        self.comboBox_IP.setObjectName(u"comboBox_IP")
        self.comboBox_IP.setEnabled(True)
        sizePolicy.setHeightForWidth(self.comboBox_IP.sizePolicy().hasHeightForWidth())
        self.comboBox_IP.setSizePolicy(sizePolicy)
        self.comboBox_IP.setMinimumSize(QSize(0, 30))

        self.gridLayout_remote.addWidget(self.comboBox_IP, 1, 0, 1, 5)

        self.label_ConnectTout = QLabel(self.groupBox_Remote)
        self.label_ConnectTout.setObjectName(u"label_ConnectTout")
        self.label_ConnectTout.setEnabled(True)
        sizePolicy.setHeightForWidth(self.label_ConnectTout.sizePolicy().hasHeightForWidth())
        self.label_ConnectTout.setSizePolicy(sizePolicy)

        self.gridLayout_remote.addWidget(self.label_ConnectTout, 3, 3, 2, 1)

        self.label_ServePort = QLabel(self.groupBox_Remote)
        self.label_ServePort.setObjectName(u"label_ServePort")
        self.label_ServePort.setEnabled(True)
        sizePolicy.setHeightForWidth(self.label_ServePort.sizePolicy().hasHeightForWidth())
        self.label_ServePort.setSizePolicy(sizePolicy)

        self.gridLayout_remote.addWidget(self.label_ServePort, 2, 0, 1, 1)

        self.lineEdit_ServerPort = QLineEdit(self.groupBox_Remote)
        self.lineEdit_ServerPort.setObjectName(u"lineEdit_ServerPort")
        self.lineEdit_ServerPort.setEnabled(True)
        sizePolicy.setHeightForWidth(self.lineEdit_ServerPort.sizePolicy().hasHeightForWidth())
        self.lineEdit_ServerPort.setSizePolicy(sizePolicy)

        self.gridLayout_remote.addWidget(self.lineEdit_ServerPort, 3, 0, 2, 1)

        self.horizontalSpacer_Remote = QSpacerItem(40, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.gridLayout_remote.addItem(self.horizontalSpacer_Remote, 2, 1, 3, 1)

        self.label_IP = QLabel(self.groupBox_Remote)
        self.label_IP.setObjectName(u"label_IP")
        self.label_IP.setEnabled(True)
        sizePolicy.setHeightForWidth(self.label_IP.sizePolicy().hasHeightForWidth())
        self.label_IP.setSizePolicy(sizePolicy)

        self.gridLayout_remote.addWidget(self.label_IP, 0, 0, 1, 5)


        self.gridLayout_setup.addWidget(self.groupBox_Remote, 4, 0, 1, 2)

        self.groupBox_Mode = QGroupBox(Setup)
        self.groupBox_Mode.setObjectName(u"groupBox_Mode")
        sizePolicy.setHeightForWidth(self.groupBox_Mode.sizePolicy().hasHeightForWidth())
        self.groupBox_Mode.setSizePolicy(sizePolicy)
        self.groupBox_Mode.setStyleSheet(u"background-color: transparent;")
        self.horizontalLayout_Mode = QHBoxLayout(self.groupBox_Mode)
        self.horizontalLayout_Mode.setObjectName(u"horizontalLayout_Mode")
        self.radioButton_RTU = QRadioButton(self.groupBox_Mode)
        self.radioButton_RTU.setObjectName(u"radioButton_RTU")
        sizePolicy5 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.radioButton_RTU.sizePolicy().hasHeightForWidth())
        self.radioButton_RTU.setSizePolicy(sizePolicy5)
        self.radioButton_RTU.setChecked(True)

        self.horizontalLayout_Mode.addWidget(self.radioButton_RTU, 0, Qt.AlignHCenter)

        self.radioButton_ASCII = QRadioButton(self.groupBox_Mode)
        self.radioButton_ASCII.setObjectName(u"radioButton_ASCII")
        sizePolicy5.setHeightForWidth(self.radioButton_ASCII.sizePolicy().hasHeightForWidth())
        self.radioButton_ASCII.setSizePolicy(sizePolicy5)

        self.horizontalLayout_Mode.addWidget(self.radioButton_ASCII, 0, Qt.AlignHCenter)


        self.gridLayout_setup.addWidget(self.groupBox_Mode, 1, 1, 1, 1)

        self.gridLayout_setup.setRowMinimumHeight(5, 20)
        QWidget.setTabOrder(self.comboBox_Connection, self.comboBox_COM)
        QWidget.setTabOrder(self.comboBox_COM, self.comboBox_BaudRate)
        QWidget.setTabOrder(self.comboBox_BaudRate, self.comboBox_DataBits)
        QWidget.setTabOrder(self.comboBox_DataBits, self.comboBox_Parity)
        QWidget.setTabOrder(self.comboBox_Parity, self.comboBox_StopBits)
        QWidget.setTabOrder(self.comboBox_StopBits, self.radioButton_RTU)
        QWidget.setTabOrder(self.radioButton_RTU, self.radioButton_ASCII)
        QWidget.setTabOrder(self.radioButton_ASCII, self.spinBox_UnitID)
        QWidget.setTabOrder(self.spinBox_UnitID, self.lineEdit_ResTout)
        QWidget.setTabOrder(self.lineEdit_ResTout, self.comboBox_IP)
        QWidget.setTabOrder(self.comboBox_IP, self.lineEdit_ServerPort)
        QWidget.setTabOrder(self.lineEdit_ServerPort, self.lineEdit_ConnectTout)
        QWidget.setTabOrder(self.lineEdit_ConnectTout, self.radioButton_IPv4)
        QWidget.setTabOrder(self.radioButton_IPv4, self.radioButton_IPv6)
        QWidget.setTabOrder(self.radioButton_IPv6, self.pushButton_ok)
        QWidget.setTabOrder(self.pushButton_ok, self.pushButton_close)

        self.retranslateUi(Setup)

        self.comboBox_BaudRate.setCurrentIndex(11)
        self.comboBox_DataBits.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(Setup)
    # setupUi

    def retranslateUi(self, Setup):
        Setup.setWindowTitle(QCoreApplication.translate("Setup", u"Dialog", None))
        self.groupBox_ResTout.setTitle(QCoreApplication.translate("Setup", u"Response Timeout", None))
        self.lineEdit_ResTout.setText(QCoreApplication.translate("Setup", u"1000", None))
        self.label_ResTout.setText(QCoreApplication.translate("Setup", u"[ms]", None))
        self.groupBox_Serial.setTitle(QCoreApplication.translate("Setup", u"Serial Settings", None))
        self.label_COM.setText(QCoreApplication.translate("Setup", u"Port:", None))
        self.comboBox_COM.setItemText(0, QCoreApplication.translate("Setup", u"COM1", None))
        self.comboBox_COM.setItemText(1, QCoreApplication.translate("Setup", u"COM2", None))
        self.comboBox_COM.setItemText(2, QCoreApplication.translate("Setup", u"COM3", None))
        self.comboBox_COM.setItemText(3, QCoreApplication.translate("Setup", u"COM4", None))
        self.comboBox_COM.setItemText(4, QCoreApplication.translate("Setup", u"COM5", None))
        self.comboBox_COM.setItemText(5, QCoreApplication.translate("Setup", u"COM6", None))
        self.comboBox_COM.setItemText(6, QCoreApplication.translate("Setup", u"COM7", None))
        self.comboBox_COM.setItemText(7, QCoreApplication.translate("Setup", u"COM8", None))
        self.comboBox_COM.setItemText(8, QCoreApplication.translate("Setup", u"COM9", None))
        self.comboBox_COM.setItemText(9, QCoreApplication.translate("Setup", u"COM10", None))
        self.comboBox_COM.setItemText(10, QCoreApplication.translate("Setup", u"COM11", None))
        self.comboBox_COM.setItemText(11, QCoreApplication.translate("Setup", u"COM12", None))
        self.comboBox_COM.setItemText(12, QCoreApplication.translate("Setup", u"COM13", None))
        self.comboBox_COM.setItemText(13, QCoreApplication.translate("Setup", u"COM14", None))
        self.comboBox_COM.setItemText(14, QCoreApplication.translate("Setup", u"COM15", None))
        self.comboBox_COM.setItemText(15, QCoreApplication.translate("Setup", u"COM16", None))
        self.comboBox_COM.setItemText(16, QCoreApplication.translate("Setup", u"COM17", None))
        self.comboBox_COM.setItemText(17, QCoreApplication.translate("Setup", u"COM18", None))
        self.comboBox_COM.setItemText(18, QCoreApplication.translate("Setup", u"COM19", None))
        self.comboBox_COM.setItemText(19, QCoreApplication.translate("Setup", u"COM20", None))
        self.comboBox_COM.setItemText(20, QCoreApplication.translate("Setup", u"COM21", None))
        self.comboBox_COM.setItemText(21, QCoreApplication.translate("Setup", u"COM22", None))
        self.comboBox_COM.setItemText(22, QCoreApplication.translate("Setup", u"COM23", None))
        self.comboBox_COM.setItemText(23, QCoreApplication.translate("Setup", u"COM24", None))
        self.comboBox_COM.setItemText(24, QCoreApplication.translate("Setup", u"COM25", None))
        self.comboBox_COM.setItemText(25, QCoreApplication.translate("Setup", u"COM26", None))
        self.comboBox_COM.setItemText(26, QCoreApplication.translate("Setup", u"COM27", None))
        self.comboBox_COM.setItemText(27, QCoreApplication.translate("Setup", u"COM28", None))
        self.comboBox_COM.setItemText(28, QCoreApplication.translate("Setup", u"COM29", None))
        self.comboBox_COM.setItemText(29, QCoreApplication.translate("Setup", u"COM30", None))
        self.comboBox_COM.setItemText(30, QCoreApplication.translate("Setup", u"COM31", None))
        self.comboBox_COM.setItemText(31, QCoreApplication.translate("Setup", u"COM32", None))
        self.comboBox_COM.setItemText(32, QCoreApplication.translate("Setup", u"COM33", None))
        self.comboBox_COM.setItemText(33, QCoreApplication.translate("Setup", u"COM34", None))
        self.comboBox_COM.setItemText(34, QCoreApplication.translate("Setup", u"COM35", None))
        self.comboBox_COM.setItemText(35, QCoreApplication.translate("Setup", u"COM36", None))
        self.comboBox_COM.setItemText(36, QCoreApplication.translate("Setup", u"COM37", None))
        self.comboBox_COM.setItemText(37, QCoreApplication.translate("Setup", u"COM38", None))
        self.comboBox_COM.setItemText(38, QCoreApplication.translate("Setup", u"COM39", None))
        self.comboBox_COM.setItemText(39, QCoreApplication.translate("Setup", u"COM40", None))
        self.comboBox_COM.setItemText(40, QCoreApplication.translate("Setup", u"COM41", None))
        self.comboBox_COM.setItemText(41, QCoreApplication.translate("Setup", u"COM42", None))
        self.comboBox_COM.setItemText(42, QCoreApplication.translate("Setup", u"COM43", None))
        self.comboBox_COM.setItemText(43, QCoreApplication.translate("Setup", u"COM44", None))
        self.comboBox_COM.setItemText(44, QCoreApplication.translate("Setup", u"COM45", None))
        self.comboBox_COM.setItemText(45, QCoreApplication.translate("Setup", u"COM46", None))
        self.comboBox_COM.setItemText(46, QCoreApplication.translate("Setup", u"COM47", None))
        self.comboBox_COM.setItemText(47, QCoreApplication.translate("Setup", u"COM48", None))
        self.comboBox_COM.setItemText(48, QCoreApplication.translate("Setup", u"COM49", None))
        self.comboBox_COM.setItemText(49, QCoreApplication.translate("Setup", u"COM50", None))
        self.comboBox_COM.setItemText(50, QCoreApplication.translate("Setup", u"COM51", None))
        self.comboBox_COM.setItemText(51, QCoreApplication.translate("Setup", u"COM52", None))
        self.comboBox_COM.setItemText(52, QCoreApplication.translate("Setup", u"COM53", None))
        self.comboBox_COM.setItemText(53, QCoreApplication.translate("Setup", u"COM54", None))
        self.comboBox_COM.setItemText(54, QCoreApplication.translate("Setup", u"COM55", None))
        self.comboBox_COM.setItemText(55, QCoreApplication.translate("Setup", u"COM56", None))
        self.comboBox_COM.setItemText(56, QCoreApplication.translate("Setup", u"COM57", None))
        self.comboBox_COM.setItemText(57, QCoreApplication.translate("Setup", u"COM58", None))
        self.comboBox_COM.setItemText(58, QCoreApplication.translate("Setup", u"COM59", None))
        self.comboBox_COM.setItemText(59, QCoreApplication.translate("Setup", u"COM60", None))
        self.comboBox_COM.setItemText(60, QCoreApplication.translate("Setup", u"COM61", None))
        self.comboBox_COM.setItemText(61, QCoreApplication.translate("Setup", u"COM62", None))
        self.comboBox_COM.setItemText(62, QCoreApplication.translate("Setup", u"COM63", None))
        self.comboBox_COM.setItemText(63, QCoreApplication.translate("Setup", u"COM64", None))
        self.comboBox_COM.setItemText(64, QCoreApplication.translate("Setup", u"COM65", None))
        self.comboBox_COM.setItemText(65, QCoreApplication.translate("Setup", u"COM66", None))
        self.comboBox_COM.setItemText(66, QCoreApplication.translate("Setup", u"COM67", None))
        self.comboBox_COM.setItemText(67, QCoreApplication.translate("Setup", u"COM68", None))
        self.comboBox_COM.setItemText(68, QCoreApplication.translate("Setup", u"COM69", None))
        self.comboBox_COM.setItemText(69, QCoreApplication.translate("Setup", u"COM70", None))
        self.comboBox_COM.setItemText(70, QCoreApplication.translate("Setup", u"COM71", None))
        self.comboBox_COM.setItemText(71, QCoreApplication.translate("Setup", u"COM72", None))
        self.comboBox_COM.setItemText(72, QCoreApplication.translate("Setup", u"COM73", None))
        self.comboBox_COM.setItemText(73, QCoreApplication.translate("Setup", u"COM74", None))
        self.comboBox_COM.setItemText(74, QCoreApplication.translate("Setup", u"COM75", None))
        self.comboBox_COM.setItemText(75, QCoreApplication.translate("Setup", u"COM76", None))
        self.comboBox_COM.setItemText(76, QCoreApplication.translate("Setup", u"COM77", None))
        self.comboBox_COM.setItemText(77, QCoreApplication.translate("Setup", u"COM78", None))
        self.comboBox_COM.setItemText(78, QCoreApplication.translate("Setup", u"COM79", None))
        self.comboBox_COM.setItemText(79, QCoreApplication.translate("Setup", u"COM80", None))
        self.comboBox_COM.setItemText(80, QCoreApplication.translate("Setup", u"COM81", None))
        self.comboBox_COM.setItemText(81, QCoreApplication.translate("Setup", u"COM82", None))
        self.comboBox_COM.setItemText(82, QCoreApplication.translate("Setup", u"COM83", None))
        self.comboBox_COM.setItemText(83, QCoreApplication.translate("Setup", u"COM84", None))
        self.comboBox_COM.setItemText(84, QCoreApplication.translate("Setup", u"COM85", None))
        self.comboBox_COM.setItemText(85, QCoreApplication.translate("Setup", u"COM86", None))
        self.comboBox_COM.setItemText(86, QCoreApplication.translate("Setup", u"COM87", None))
        self.comboBox_COM.setItemText(87, QCoreApplication.translate("Setup", u"COM88", None))
        self.comboBox_COM.setItemText(88, QCoreApplication.translate("Setup", u"COM89", None))
        self.comboBox_COM.setItemText(89, QCoreApplication.translate("Setup", u"COM90", None))
        self.comboBox_COM.setItemText(90, QCoreApplication.translate("Setup", u"COM91", None))
        self.comboBox_COM.setItemText(91, QCoreApplication.translate("Setup", u"COM92", None))
        self.comboBox_COM.setItemText(92, QCoreApplication.translate("Setup", u"COM93", None))
        self.comboBox_COM.setItemText(93, QCoreApplication.translate("Setup", u"COM94", None))
        self.comboBox_COM.setItemText(94, QCoreApplication.translate("Setup", u"COM95", None))
        self.comboBox_COM.setItemText(95, QCoreApplication.translate("Setup", u"COM96", None))
        self.comboBox_COM.setItemText(96, QCoreApplication.translate("Setup", u"COM97", None))
        self.comboBox_COM.setItemText(97, QCoreApplication.translate("Setup", u"COM98", None))
        self.comboBox_COM.setItemText(98, QCoreApplication.translate("Setup", u"COM99", None))
        self.comboBox_COM.setItemText(99, QCoreApplication.translate("Setup", u"COM100", None))
        self.comboBox_COM.setItemText(100, QCoreApplication.translate("Setup", u"COM101", None))
        self.comboBox_COM.setItemText(101, QCoreApplication.translate("Setup", u"COM102", None))
        self.comboBox_COM.setItemText(102, QCoreApplication.translate("Setup", u"COM103", None))
        self.comboBox_COM.setItemText(103, QCoreApplication.translate("Setup", u"COM104", None))
        self.comboBox_COM.setItemText(104, QCoreApplication.translate("Setup", u"COM105", None))
        self.comboBox_COM.setItemText(105, QCoreApplication.translate("Setup", u"COM106", None))
        self.comboBox_COM.setItemText(106, QCoreApplication.translate("Setup", u"COM107", None))
        self.comboBox_COM.setItemText(107, QCoreApplication.translate("Setup", u"COM108", None))
        self.comboBox_COM.setItemText(108, QCoreApplication.translate("Setup", u"COM109", None))
        self.comboBox_COM.setItemText(109, QCoreApplication.translate("Setup", u"COM110", None))
        self.comboBox_COM.setItemText(110, QCoreApplication.translate("Setup", u"COM111", None))
        self.comboBox_COM.setItemText(111, QCoreApplication.translate("Setup", u"COM112", None))
        self.comboBox_COM.setItemText(112, QCoreApplication.translate("Setup", u"COM113", None))
        self.comboBox_COM.setItemText(113, QCoreApplication.translate("Setup", u"COM114", None))
        self.comboBox_COM.setItemText(114, QCoreApplication.translate("Setup", u"COM115", None))
        self.comboBox_COM.setItemText(115, QCoreApplication.translate("Setup", u"COM116", None))
        self.comboBox_COM.setItemText(116, QCoreApplication.translate("Setup", u"COM117", None))
        self.comboBox_COM.setItemText(117, QCoreApplication.translate("Setup", u"COM118", None))
        self.comboBox_COM.setItemText(118, QCoreApplication.translate("Setup", u"COM119", None))
        self.comboBox_COM.setItemText(119, QCoreApplication.translate("Setup", u"COM120", None))
        self.comboBox_COM.setItemText(120, QCoreApplication.translate("Setup", u"COM121", None))
        self.comboBox_COM.setItemText(121, QCoreApplication.translate("Setup", u"COM122", None))
        self.comboBox_COM.setItemText(122, QCoreApplication.translate("Setup", u"COM123", None))
        self.comboBox_COM.setItemText(123, QCoreApplication.translate("Setup", u"COM124", None))
        self.comboBox_COM.setItemText(124, QCoreApplication.translate("Setup", u"COM125", None))
        self.comboBox_COM.setItemText(125, QCoreApplication.translate("Setup", u"COM126", None))
        self.comboBox_COM.setItemText(126, QCoreApplication.translate("Setup", u"COM127", None))
        self.comboBox_COM.setItemText(127, QCoreApplication.translate("Setup", u"COM128", None))
        self.comboBox_COM.setItemText(128, QCoreApplication.translate("Setup", u"COM129", None))
        self.comboBox_COM.setItemText(129, QCoreApplication.translate("Setup", u"COM130", None))
        self.comboBox_COM.setItemText(130, QCoreApplication.translate("Setup", u"COM131", None))
        self.comboBox_COM.setItemText(131, QCoreApplication.translate("Setup", u"COM132", None))
        self.comboBox_COM.setItemText(132, QCoreApplication.translate("Setup", u"COM133", None))
        self.comboBox_COM.setItemText(133, QCoreApplication.translate("Setup", u"COM134", None))
        self.comboBox_COM.setItemText(134, QCoreApplication.translate("Setup", u"COM135", None))
        self.comboBox_COM.setItemText(135, QCoreApplication.translate("Setup", u"COM136", None))
        self.comboBox_COM.setItemText(136, QCoreApplication.translate("Setup", u"COM137", None))
        self.comboBox_COM.setItemText(137, QCoreApplication.translate("Setup", u"COM138", None))
        self.comboBox_COM.setItemText(138, QCoreApplication.translate("Setup", u"COM139", None))
        self.comboBox_COM.setItemText(139, QCoreApplication.translate("Setup", u"COM140", None))
        self.comboBox_COM.setItemText(140, QCoreApplication.translate("Setup", u"COM141", None))
        self.comboBox_COM.setItemText(141, QCoreApplication.translate("Setup", u"COM142", None))
        self.comboBox_COM.setItemText(142, QCoreApplication.translate("Setup", u"COM143", None))
        self.comboBox_COM.setItemText(143, QCoreApplication.translate("Setup", u"COM144", None))
        self.comboBox_COM.setItemText(144, QCoreApplication.translate("Setup", u"COM145", None))
        self.comboBox_COM.setItemText(145, QCoreApplication.translate("Setup", u"COM146", None))
        self.comboBox_COM.setItemText(146, QCoreApplication.translate("Setup", u"COM147", None))
        self.comboBox_COM.setItemText(147, QCoreApplication.translate("Setup", u"COM148", None))
        self.comboBox_COM.setItemText(148, QCoreApplication.translate("Setup", u"COM149", None))
        self.comboBox_COM.setItemText(149, QCoreApplication.translate("Setup", u"COM150", None))
        self.comboBox_COM.setItemText(150, QCoreApplication.translate("Setup", u"COM151", None))
        self.comboBox_COM.setItemText(151, QCoreApplication.translate("Setup", u"COM152", None))
        self.comboBox_COM.setItemText(152, QCoreApplication.translate("Setup", u"COM153", None))
        self.comboBox_COM.setItemText(153, QCoreApplication.translate("Setup", u"COM154", None))
        self.comboBox_COM.setItemText(154, QCoreApplication.translate("Setup", u"COM155", None))
        self.comboBox_COM.setItemText(155, QCoreApplication.translate("Setup", u"COM156", None))
        self.comboBox_COM.setItemText(156, QCoreApplication.translate("Setup", u"COM157", None))
        self.comboBox_COM.setItemText(157, QCoreApplication.translate("Setup", u"COM158", None))
        self.comboBox_COM.setItemText(158, QCoreApplication.translate("Setup", u"COM159", None))
        self.comboBox_COM.setItemText(159, QCoreApplication.translate("Setup", u"COM160", None))
        self.comboBox_COM.setItemText(160, QCoreApplication.translate("Setup", u"COM161", None))
        self.comboBox_COM.setItemText(161, QCoreApplication.translate("Setup", u"COM162", None))
        self.comboBox_COM.setItemText(162, QCoreApplication.translate("Setup", u"COM163", None))
        self.comboBox_COM.setItemText(163, QCoreApplication.translate("Setup", u"COM164", None))
        self.comboBox_COM.setItemText(164, QCoreApplication.translate("Setup", u"COM165", None))
        self.comboBox_COM.setItemText(165, QCoreApplication.translate("Setup", u"COM166", None))
        self.comboBox_COM.setItemText(166, QCoreApplication.translate("Setup", u"COM167", None))
        self.comboBox_COM.setItemText(167, QCoreApplication.translate("Setup", u"COM168", None))
        self.comboBox_COM.setItemText(168, QCoreApplication.translate("Setup", u"COM169", None))
        self.comboBox_COM.setItemText(169, QCoreApplication.translate("Setup", u"COM170", None))
        self.comboBox_COM.setItemText(170, QCoreApplication.translate("Setup", u"COM171", None))
        self.comboBox_COM.setItemText(171, QCoreApplication.translate("Setup", u"COM172", None))
        self.comboBox_COM.setItemText(172, QCoreApplication.translate("Setup", u"COM173", None))
        self.comboBox_COM.setItemText(173, QCoreApplication.translate("Setup", u"COM174", None))
        self.comboBox_COM.setItemText(174, QCoreApplication.translate("Setup", u"COM175", None))
        self.comboBox_COM.setItemText(175, QCoreApplication.translate("Setup", u"COM176", None))
        self.comboBox_COM.setItemText(176, QCoreApplication.translate("Setup", u"COM177", None))
        self.comboBox_COM.setItemText(177, QCoreApplication.translate("Setup", u"COM178", None))
        self.comboBox_COM.setItemText(178, QCoreApplication.translate("Setup", u"COM179", None))
        self.comboBox_COM.setItemText(179, QCoreApplication.translate("Setup", u"COM180", None))
        self.comboBox_COM.setItemText(180, QCoreApplication.translate("Setup", u"COM181", None))
        self.comboBox_COM.setItemText(181, QCoreApplication.translate("Setup", u"COM182", None))
        self.comboBox_COM.setItemText(182, QCoreApplication.translate("Setup", u"COM183", None))
        self.comboBox_COM.setItemText(183, QCoreApplication.translate("Setup", u"COM184", None))
        self.comboBox_COM.setItemText(184, QCoreApplication.translate("Setup", u"COM185", None))
        self.comboBox_COM.setItemText(185, QCoreApplication.translate("Setup", u"COM186", None))
        self.comboBox_COM.setItemText(186, QCoreApplication.translate("Setup", u"COM187", None))
        self.comboBox_COM.setItemText(187, QCoreApplication.translate("Setup", u"COM188", None))
        self.comboBox_COM.setItemText(188, QCoreApplication.translate("Setup", u"COM189", None))
        self.comboBox_COM.setItemText(189, QCoreApplication.translate("Setup", u"COM190", None))
        self.comboBox_COM.setItemText(190, QCoreApplication.translate("Setup", u"COM191", None))
        self.comboBox_COM.setItemText(191, QCoreApplication.translate("Setup", u"COM192", None))
        self.comboBox_COM.setItemText(192, QCoreApplication.translate("Setup", u"COM193", None))
        self.comboBox_COM.setItemText(193, QCoreApplication.translate("Setup", u"COM194", None))
        self.comboBox_COM.setItemText(194, QCoreApplication.translate("Setup", u"COM195", None))
        self.comboBox_COM.setItemText(195, QCoreApplication.translate("Setup", u"COM196", None))
        self.comboBox_COM.setItemText(196, QCoreApplication.translate("Setup", u"COM197", None))
        self.comboBox_COM.setItemText(197, QCoreApplication.translate("Setup", u"COM198", None))
        self.comboBox_COM.setItemText(198, QCoreApplication.translate("Setup", u"COM199", None))
        self.comboBox_COM.setItemText(199, QCoreApplication.translate("Setup", u"COM200", None))
        self.comboBox_COM.setItemText(200, QCoreApplication.translate("Setup", u"COM201", None))
        self.comboBox_COM.setItemText(201, QCoreApplication.translate("Setup", u"COM202", None))
        self.comboBox_COM.setItemText(202, QCoreApplication.translate("Setup", u"COM203", None))
        self.comboBox_COM.setItemText(203, QCoreApplication.translate("Setup", u"COM204", None))
        self.comboBox_COM.setItemText(204, QCoreApplication.translate("Setup", u"COM205", None))
        self.comboBox_COM.setItemText(205, QCoreApplication.translate("Setup", u"COM206", None))
        self.comboBox_COM.setItemText(206, QCoreApplication.translate("Setup", u"COM207", None))
        self.comboBox_COM.setItemText(207, QCoreApplication.translate("Setup", u"COM208", None))
        self.comboBox_COM.setItemText(208, QCoreApplication.translate("Setup", u"COM209", None))
        self.comboBox_COM.setItemText(209, QCoreApplication.translate("Setup", u"COM210", None))
        self.comboBox_COM.setItemText(210, QCoreApplication.translate("Setup", u"COM211", None))
        self.comboBox_COM.setItemText(211, QCoreApplication.translate("Setup", u"COM212", None))
        self.comboBox_COM.setItemText(212, QCoreApplication.translate("Setup", u"COM213", None))
        self.comboBox_COM.setItemText(213, QCoreApplication.translate("Setup", u"COM214", None))
        self.comboBox_COM.setItemText(214, QCoreApplication.translate("Setup", u"COM215", None))
        self.comboBox_COM.setItemText(215, QCoreApplication.translate("Setup", u"COM216", None))
        self.comboBox_COM.setItemText(216, QCoreApplication.translate("Setup", u"COM217", None))
        self.comboBox_COM.setItemText(217, QCoreApplication.translate("Setup", u"COM218", None))
        self.comboBox_COM.setItemText(218, QCoreApplication.translate("Setup", u"COM219", None))
        self.comboBox_COM.setItemText(219, QCoreApplication.translate("Setup", u"COM220", None))
        self.comboBox_COM.setItemText(220, QCoreApplication.translate("Setup", u"COM221", None))
        self.comboBox_COM.setItemText(221, QCoreApplication.translate("Setup", u"COM222", None))
        self.comboBox_COM.setItemText(222, QCoreApplication.translate("Setup", u"COM223", None))
        self.comboBox_COM.setItemText(223, QCoreApplication.translate("Setup", u"COM224", None))
        self.comboBox_COM.setItemText(224, QCoreApplication.translate("Setup", u"COM225", None))
        self.comboBox_COM.setItemText(225, QCoreApplication.translate("Setup", u"COM226", None))
        self.comboBox_COM.setItemText(226, QCoreApplication.translate("Setup", u"COM227", None))
        self.comboBox_COM.setItemText(227, QCoreApplication.translate("Setup", u"COM228", None))
        self.comboBox_COM.setItemText(228, QCoreApplication.translate("Setup", u"COM229", None))
        self.comboBox_COM.setItemText(229, QCoreApplication.translate("Setup", u"COM230", None))
        self.comboBox_COM.setItemText(230, QCoreApplication.translate("Setup", u"COM231", None))
        self.comboBox_COM.setItemText(231, QCoreApplication.translate("Setup", u"COM232", None))
        self.comboBox_COM.setItemText(232, QCoreApplication.translate("Setup", u"COM233", None))
        self.comboBox_COM.setItemText(233, QCoreApplication.translate("Setup", u"COM234", None))
        self.comboBox_COM.setItemText(234, QCoreApplication.translate("Setup", u"COM235", None))
        self.comboBox_COM.setItemText(235, QCoreApplication.translate("Setup", u"COM236", None))
        self.comboBox_COM.setItemText(236, QCoreApplication.translate("Setup", u"COM237", None))
        self.comboBox_COM.setItemText(237, QCoreApplication.translate("Setup", u"COM238", None))
        self.comboBox_COM.setItemText(238, QCoreApplication.translate("Setup", u"COM239", None))
        self.comboBox_COM.setItemText(239, QCoreApplication.translate("Setup", u"COM240", None))
        self.comboBox_COM.setItemText(240, QCoreApplication.translate("Setup", u"COM241", None))
        self.comboBox_COM.setItemText(241, QCoreApplication.translate("Setup", u"COM242", None))
        self.comboBox_COM.setItemText(242, QCoreApplication.translate("Setup", u"COM243", None))
        self.comboBox_COM.setItemText(243, QCoreApplication.translate("Setup", u"COM244", None))
        self.comboBox_COM.setItemText(244, QCoreApplication.translate("Setup", u"COM245", None))
        self.comboBox_COM.setItemText(245, QCoreApplication.translate("Setup", u"COM246", None))
        self.comboBox_COM.setItemText(246, QCoreApplication.translate("Setup", u"COM247", None))
        self.comboBox_COM.setItemText(247, QCoreApplication.translate("Setup", u"COM248", None))
        self.comboBox_COM.setItemText(248, QCoreApplication.translate("Setup", u"COM249", None))
        self.comboBox_COM.setItemText(249, QCoreApplication.translate("Setup", u"COM250", None))
        self.comboBox_COM.setItemText(250, QCoreApplication.translate("Setup", u"COM251", None))
        self.comboBox_COM.setItemText(251, QCoreApplication.translate("Setup", u"COM252", None))
        self.comboBox_COM.setItemText(252, QCoreApplication.translate("Setup", u"COM253", None))
        self.comboBox_COM.setItemText(253, QCoreApplication.translate("Setup", u"COM254", None))
        self.comboBox_COM.setItemText(254, QCoreApplication.translate("Setup", u"COM255", None))
        self.comboBox_COM.setItemText(255, QCoreApplication.translate("Setup", u"COM256", None))

        self.label_BaudRate.setText(QCoreApplication.translate("Setup", u"Baude Rate:", None))
        self.comboBox_BaudRate.setItemText(0, QCoreApplication.translate("Setup", u"300", None))
        self.comboBox_BaudRate.setItemText(1, QCoreApplication.translate("Setup", u"600", None))
        self.comboBox_BaudRate.setItemText(2, QCoreApplication.translate("Setup", u"1200", None))
        self.comboBox_BaudRate.setItemText(3, QCoreApplication.translate("Setup", u"2400", None))
        self.comboBox_BaudRate.setItemText(4, QCoreApplication.translate("Setup", u"4800", None))
        self.comboBox_BaudRate.setItemText(5, QCoreApplication.translate("Setup", u"9600", None))
        self.comboBox_BaudRate.setItemText(6, QCoreApplication.translate("Setup", u"14400", None))
        self.comboBox_BaudRate.setItemText(7, QCoreApplication.translate("Setup", u"19200", None))
        self.comboBox_BaudRate.setItemText(8, QCoreApplication.translate("Setup", u"38400", None))
        self.comboBox_BaudRate.setItemText(9, QCoreApplication.translate("Setup", u"56000", None))
        self.comboBox_BaudRate.setItemText(10, QCoreApplication.translate("Setup", u"57600", None))
        self.comboBox_BaudRate.setItemText(11, QCoreApplication.translate("Setup", u"115200", None))
        self.comboBox_BaudRate.setItemText(12, QCoreApplication.translate("Setup", u"128000", None))
        self.comboBox_BaudRate.setItemText(13, QCoreApplication.translate("Setup", u"153600", None))
        self.comboBox_BaudRate.setItemText(14, QCoreApplication.translate("Setup", u"230400", None))
        self.comboBox_BaudRate.setItemText(15, QCoreApplication.translate("Setup", u"256000", None))
        self.comboBox_BaudRate.setItemText(16, QCoreApplication.translate("Setup", u"460800", None))
        self.comboBox_BaudRate.setItemText(17, QCoreApplication.translate("Setup", u"921600", None))

        self.label_DataBits.setText(QCoreApplication.translate("Setup", u"Data Bits:", None))
        self.comboBox_DataBits.setItemText(0, QCoreApplication.translate("Setup", u"7", None))
        self.comboBox_DataBits.setItemText(1, QCoreApplication.translate("Setup", u"8", None))

        self.label_Parity.setText(QCoreApplication.translate("Setup", u"Parity:", None))
        self.comboBox_Parity.setItemText(0, QCoreApplication.translate("Setup", u"None", None))
        self.comboBox_Parity.setItemText(1, QCoreApplication.translate("Setup", u"Odd", None))
        self.comboBox_Parity.setItemText(2, QCoreApplication.translate("Setup", u"Even", None))

        self.label_StopBits.setText(QCoreApplication.translate("Setup", u"Stop Bits:", None))
        self.comboBox_StopBits.setItemText(0, QCoreApplication.translate("Setup", u"1", None))
        self.comboBox_StopBits.setItemText(1, QCoreApplication.translate("Setup", u"2", None))

        self.groupBox_UnitID.setTitle(QCoreApplication.translate("Setup", u"Unit ID", None))
        self.groupBox_Connection.setTitle(QCoreApplication.translate("Setup", u"Connection", None))
        self.comboBox_Connection.setItemText(0, QCoreApplication.translate("Setup", u"Serial Port", None))
        self.comboBox_Connection.setItemText(1, QCoreApplication.translate("Setup", u"ModBus TCP", None))

        self.pushButton_ok.setText(QCoreApplication.translate("Setup", u"Ok", None))
        self.pushButton_close.setText(QCoreApplication.translate("Setup", u"Close", None))
        self.groupBox_Remote.setTitle(QCoreApplication.translate("Setup", u"Remote ModBus Server", None))
        self.radioButton_IPv4.setText(QCoreApplication.translate("Setup", u"IPv4", None))
        self.radioButton_IPv6.setText(QCoreApplication.translate("Setup", u"IPv6", None))
        self.lineEdit_ConnectTout.setText(QCoreApplication.translate("Setup", u"3000", None))
        self.label_ConnectToutMS.setText(QCoreApplication.translate("Setup", u"Connection Timeout", None))
        self.comboBox_IP.setItemText(0, QCoreApplication.translate("Setup", u"127.0.0.1", None))

        self.label_ConnectTout.setText(QCoreApplication.translate("Setup", u"[ms]", None))
        self.label_ServePort.setText(QCoreApplication.translate("Setup", u"Server Port", None))
        self.lineEdit_ServerPort.setText(QCoreApplication.translate("Setup", u"502", None))
        self.label_IP.setText(QCoreApplication.translate("Setup", u"IP Address or Node Name", None))
        self.groupBox_Mode.setTitle(QCoreApplication.translate("Setup", u"Mode", None))
        self.radioButton_RTU.setText(QCoreApplication.translate("Setup", u"RTU", None))
        self.radioButton_ASCII.setText(QCoreApplication.translate("Setup", u"ASCII", None))
    # retranslateUi

