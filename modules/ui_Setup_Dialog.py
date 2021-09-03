# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Setup_DialogeQxbaq.ui'
##
## Created by: Qt User Interface Compiler version 6.1.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_Setup(object):
    def setupUi(self, Setup):
        if not Setup.objectName():
            Setup.setObjectName(u"Setup")
        Setup.resize(600, 500)
        font = QFont()
        font.setPointSize(10)
        Setup.setFont(font)
        Setup.setCursor(QCursor(Qt.ArrowCursor))
        Setup.setMouseTracking(False)
        Setup.setIconSize(QSize(500, 500))
        self.centralwidget_Setup = QWidget(Setup)
        self.centralwidget_Setup.setObjectName(u"centralwidget_Setup")
        self.gridLayout = QGridLayout(self.centralwidget_Setup)
        self.gridLayout.setObjectName(u"gridLayout")
        self.groupBox_Connection = QGroupBox(self.centralwidget_Setup)
        self.groupBox_Connection.setObjectName(u"groupBox_Connection")
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_Connection.sizePolicy().hasHeightForWidth())
        self.groupBox_Connection.setSizePolicy(sizePolicy)
        self.groupBox_Connection.setFlat(False)
        self.groupBox_Connection.setCheckable(False)
        self.horizontalLayout_Connection = QHBoxLayout(self.groupBox_Connection)
        self.horizontalLayout_Connection.setObjectName(u"horizontalLayout_Connection")
        self.comboBox_Connection = QComboBox(self.groupBox_Connection)
        self.comboBox_Connection.addItem("")
        self.comboBox_Connection.addItem("")
        self.comboBox_Connection.addItem("")
        self.comboBox_Connection.addItem("")
        self.comboBox_Connection.setObjectName(u"comboBox_Connection")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.comboBox_Connection.sizePolicy().hasHeightForWidth())
        self.comboBox_Connection.setSizePolicy(sizePolicy1)

        self.horizontalLayout_Connection.addWidget(self.comboBox_Connection)


        self.gridLayout.addWidget(self.groupBox_Connection, 0, 0, 1, 1)

        self.verticalLayout_buttons = QVBoxLayout()
        self.verticalLayout_buttons.setObjectName(u"verticalLayout_buttons")
        self.pushButton_ok = QPushButton(self.centralwidget_Setup)
        self.pushButton_ok.setObjectName(u"pushButton_ok")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.pushButton_ok.sizePolicy().hasHeightForWidth())
        self.pushButton_ok.setSizePolicy(sizePolicy2)

        self.verticalLayout_buttons.addWidget(self.pushButton_ok, 0, Qt.AlignHCenter)

        self.pushButton_close = QPushButton(self.centralwidget_Setup)
        self.pushButton_close.setObjectName(u"pushButton_close")
        sizePolicy2.setHeightForWidth(self.pushButton_close.sizePolicy().hasHeightForWidth())
        self.pushButton_close.setSizePolicy(sizePolicy2)

        self.verticalLayout_buttons.addWidget(self.pushButton_close, 0, Qt.AlignHCenter)


        self.gridLayout.addLayout(self.verticalLayout_buttons, 0, 1, 1, 1)

        self.groupBox_Serial = QGroupBox(self.centralwidget_Setup)
        self.groupBox_Serial.setObjectName(u"groupBox_Serial")
        sizePolicy1.setHeightForWidth(self.groupBox_Serial.sizePolicy().hasHeightForWidth())
        self.groupBox_Serial.setSizePolicy(sizePolicy1)
        self.gridLayout_2 = QGridLayout(self.groupBox_Serial)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_COM = QLabel(self.groupBox_Serial)
        self.label_COM.setObjectName(u"label_COM")

        self.gridLayout_2.addWidget(self.label_COM, 0, 0, 1, 1)

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
        self.comboBox_COM.setObjectName(u"comboBox_COM")
        self.comboBox_COM.setEnabled(True)
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.comboBox_COM.sizePolicy().hasHeightForWidth())
        self.comboBox_COM.setSizePolicy(sizePolicy3)

        self.gridLayout_2.addWidget(self.comboBox_COM, 0, 1, 1, 1)

        self.label_BaudRate = QLabel(self.groupBox_Serial)
        self.label_BaudRate.setObjectName(u"label_BaudRate")

        self.gridLayout_2.addWidget(self.label_BaudRate, 1, 0, 1, 1)

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
        self.comboBox_BaudRate.setObjectName(u"comboBox_BaudRate")
        sizePolicy1.setHeightForWidth(self.comboBox_BaudRate.sizePolicy().hasHeightForWidth())
        self.comboBox_BaudRate.setSizePolicy(sizePolicy1)
        self.comboBox_BaudRate.setMaxVisibleItems(15)

        self.gridLayout_2.addWidget(self.comboBox_BaudRate, 1, 1, 1, 1)

        self.label_DataBits = QLabel(self.groupBox_Serial)
        self.label_DataBits.setObjectName(u"label_DataBits")

        self.gridLayout_2.addWidget(self.label_DataBits, 2, 0, 1, 1)

        self.comboBox_DataBits = QComboBox(self.groupBox_Serial)
        self.comboBox_DataBits.addItem("")
        self.comboBox_DataBits.addItem("")
        self.comboBox_DataBits.setObjectName(u"comboBox_DataBits")
        sizePolicy1.setHeightForWidth(self.comboBox_DataBits.sizePolicy().hasHeightForWidth())
        self.comboBox_DataBits.setSizePolicy(sizePolicy1)

        self.gridLayout_2.addWidget(self.comboBox_DataBits, 2, 1, 1, 1)

        self.label_Parity = QLabel(self.groupBox_Serial)
        self.label_Parity.setObjectName(u"label_Parity")

        self.gridLayout_2.addWidget(self.label_Parity, 3, 0, 1, 1)

        self.comboBox_Parity = QComboBox(self.groupBox_Serial)
        self.comboBox_Parity.addItem("")
        self.comboBox_Parity.addItem("")
        self.comboBox_Parity.addItem("")
        self.comboBox_Parity.setObjectName(u"comboBox_Parity")
        sizePolicy1.setHeightForWidth(self.comboBox_Parity.sizePolicy().hasHeightForWidth())
        self.comboBox_Parity.setSizePolicy(sizePolicy1)

        self.gridLayout_2.addWidget(self.comboBox_Parity, 3, 1, 1, 1)

        self.label_StopBits = QLabel(self.groupBox_Serial)
        self.label_StopBits.setObjectName(u"label_StopBits")

        self.gridLayout_2.addWidget(self.label_StopBits, 4, 0, 1, 1)

        self.comboBox_StopBits = QComboBox(self.groupBox_Serial)
        self.comboBox_StopBits.addItem("")
        self.comboBox_StopBits.addItem("")
        self.comboBox_StopBits.setObjectName(u"comboBox_StopBits")
        sizePolicy1.setHeightForWidth(self.comboBox_StopBits.sizePolicy().hasHeightForWidth())
        self.comboBox_StopBits.setSizePolicy(sizePolicy1)

        self.gridLayout_2.addWidget(self.comboBox_StopBits, 4, 1, 1, 1)


        self.gridLayout.addWidget(self.groupBox_Serial, 1, 0, 3, 1)

        self.groupBox_Mode = QGroupBox(self.centralwidget_Setup)
        self.groupBox_Mode.setObjectName(u"groupBox_Mode")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.groupBox_Mode.sizePolicy().hasHeightForWidth())
        self.groupBox_Mode.setSizePolicy(sizePolicy4)
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


        self.gridLayout.addWidget(self.groupBox_Mode, 1, 1, 1, 1)

        self.groupBox_SlaveID = QGroupBox(self.centralwidget_Setup)
        self.groupBox_SlaveID.setObjectName(u"groupBox_SlaveID")
        sizePolicy4.setHeightForWidth(self.groupBox_SlaveID.sizePolicy().hasHeightForWidth())
        self.groupBox_SlaveID.setSizePolicy(sizePolicy4)
        self.horizontalLayout_SlaveID = QHBoxLayout(self.groupBox_SlaveID)
        self.horizontalLayout_SlaveID.setObjectName(u"horizontalLayout_SlaveID")
        self.lineEdit_SlaveID = QLineEdit(self.groupBox_SlaveID)
        self.lineEdit_SlaveID.setObjectName(u"lineEdit_SlaveID")
        sizePolicy4.setHeightForWidth(self.lineEdit_SlaveID.sizePolicy().hasHeightForWidth())
        self.lineEdit_SlaveID.setSizePolicy(sizePolicy4)

        self.horizontalLayout_SlaveID.addWidget(self.lineEdit_SlaveID)


        self.gridLayout.addWidget(self.groupBox_SlaveID, 2, 1, 1, 1)

        self.groupBox_ResTout = QGroupBox(self.centralwidget_Setup)
        self.groupBox_ResTout.setObjectName(u"groupBox_ResTout")
        sizePolicy4.setHeightForWidth(self.groupBox_ResTout.sizePolicy().hasHeightForWidth())
        self.groupBox_ResTout.setSizePolicy(sizePolicy4)
        self.horizontalLayout_2 = QHBoxLayout(self.groupBox_ResTout)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.lineEdit_ResTout = QLineEdit(self.groupBox_ResTout)
        self.lineEdit_ResTout.setObjectName(u"lineEdit_ResTout")
        sizePolicy4.setHeightForWidth(self.lineEdit_ResTout.sizePolicy().hasHeightForWidth())
        self.lineEdit_ResTout.setSizePolicy(sizePolicy4)

        self.horizontalLayout_2.addWidget(self.lineEdit_ResTout)

        self.label_ResTout = QLabel(self.groupBox_ResTout)
        self.label_ResTout.setObjectName(u"label_ResTout")

        self.horizontalLayout_2.addWidget(self.label_ResTout)


        self.gridLayout.addWidget(self.groupBox_ResTout, 3, 1, 1, 1)

        self.groupBox_Remote = QGroupBox(self.centralwidget_Setup)
        self.groupBox_Remote.setObjectName(u"groupBox_Remote")
        sizePolicy4.setHeightForWidth(self.groupBox_Remote.sizePolicy().hasHeightForWidth())
        self.groupBox_Remote.setSizePolicy(sizePolicy4)
        self.gridLayout_3 = QGridLayout(self.groupBox_Remote)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.radioButton_IPv4 = QRadioButton(self.groupBox_Remote)
        self.radioButton_IPv4.setObjectName(u"radioButton_IPv4")
        self.radioButton_IPv4.setEnabled(False)
        sizePolicy6 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.radioButton_IPv4.sizePolicy().hasHeightForWidth())
        self.radioButton_IPv4.setSizePolicy(sizePolicy6)
        self.radioButton_IPv4.setSizeIncrement(QSize(0, 0))
        self.radioButton_IPv4.setBaseSize(QSize(0, 0))
        self.radioButton_IPv4.setFont(font)

        self.gridLayout_3.addWidget(self.radioButton_IPv4, 2, 4, 2, 1)

        self.radioButton_IPv6 = QRadioButton(self.groupBox_Remote)
        self.radioButton_IPv6.setObjectName(u"radioButton_IPv6")
        self.radioButton_IPv6.setEnabled(False)
        self.radioButton_IPv6.setFont(font)

        self.gridLayout_3.addWidget(self.radioButton_IPv6, 4, 4, 1, 1)

        self.label_IP = QLabel(self.groupBox_Remote)
        self.label_IP.setObjectName(u"label_IP")
        self.label_IP.setEnabled(False)

        self.gridLayout_3.addWidget(self.label_IP, 0, 0, 1, 1)

        self.lineEdit_ConnectTout = QLineEdit(self.groupBox_Remote)
        self.lineEdit_ConnectTout.setObjectName(u"lineEdit_ConnectTout")
        self.lineEdit_ConnectTout.setEnabled(False)
        sizePolicy4.setHeightForWidth(self.lineEdit_ConnectTout.sizePolicy().hasHeightForWidth())
        self.lineEdit_ConnectTout.setSizePolicy(sizePolicy4)

        self.gridLayout_3.addWidget(self.lineEdit_ConnectTout, 3, 2, 2, 1)

        self.label_ConnectToutMS = QLabel(self.groupBox_Remote)
        self.label_ConnectToutMS.setObjectName(u"label_ConnectToutMS")
        self.label_ConnectToutMS.setEnabled(False)

        self.gridLayout_3.addWidget(self.label_ConnectToutMS, 2, 2, 1, 1)

        self.comboBox_IP = QComboBox(self.groupBox_Remote)
        self.comboBox_IP.addItem("")
        self.comboBox_IP.setObjectName(u"comboBox_IP")
        self.comboBox_IP.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.comboBox_IP.sizePolicy().hasHeightForWidth())
        self.comboBox_IP.setSizePolicy(sizePolicy1)

        self.gridLayout_3.addWidget(self.comboBox_IP, 1, 0, 1, 5)

        self.label_ConnectTout = QLabel(self.groupBox_Remote)
        self.label_ConnectTout.setObjectName(u"label_ConnectTout")
        self.label_ConnectTout.setEnabled(False)

        self.gridLayout_3.addWidget(self.label_ConnectTout, 3, 3, 2, 1)

        self.label_ServePort = QLabel(self.groupBox_Remote)
        self.label_ServePort.setObjectName(u"label_ServePort")
        self.label_ServePort.setEnabled(False)

        self.gridLayout_3.addWidget(self.label_ServePort, 2, 0, 1, 1)

        self.lineEdit_ServerPort = QLineEdit(self.groupBox_Remote)
        self.lineEdit_ServerPort.setObjectName(u"lineEdit_ServerPort")
        self.lineEdit_ServerPort.setEnabled(False)
        sizePolicy4.setHeightForWidth(self.lineEdit_ServerPort.sizePolicy().hasHeightForWidth())
        self.lineEdit_ServerPort.setSizePolicy(sizePolicy4)

        self.gridLayout_3.addWidget(self.lineEdit_ServerPort, 3, 0, 2, 1)

        self.horizontalSpacer_Remote = QSpacerItem(40, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_Remote, 2, 1, 3, 1)


        self.gridLayout.addWidget(self.groupBox_Remote, 4, 0, 1, 2)

        Setup.setCentralWidget(self.centralwidget_Setup)
        self.statusbar = QStatusBar(Setup)
        self.statusbar.setObjectName(u"statusbar")
        Setup.setStatusBar(self.statusbar)
        QWidget.setTabOrder(self.radioButton_RTU, self.radioButton_ASCII)
        QWidget.setTabOrder(self.radioButton_ASCII, self.lineEdit_ResTout)
        QWidget.setTabOrder(self.lineEdit_ResTout, self.lineEdit_SlaveID)
        QWidget.setTabOrder(self.lineEdit_SlaveID, self.comboBox_IP)
        QWidget.setTabOrder(self.comboBox_IP, self.radioButton_IPv6)
        QWidget.setTabOrder(self.radioButton_IPv6, self.radioButton_IPv4)
        QWidget.setTabOrder(self.radioButton_IPv4, self.lineEdit_ServerPort)
        QWidget.setTabOrder(self.lineEdit_ServerPort, self.lineEdit_ConnectTout)

        self.retranslateUi(Setup)

        self.comboBox_BaudRate.setCurrentIndex(11)
        self.comboBox_DataBits.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(Setup)
    # setupUi

    def retranslateUi(self, Setup):
        Setup.setWindowTitle(QCoreApplication.translate("Setup", u"MainWindow", None))
        self.groupBox_Connection.setTitle(QCoreApplication.translate("Setup", u"Connection", None))
        self.comboBox_Connection.setItemText(0, QCoreApplication.translate("Setup", u"Serial Port", None))
        self.comboBox_Connection.setItemText(1, QCoreApplication.translate("Setup", u"2", None))
        self.comboBox_Connection.setItemText(2, QCoreApplication.translate("Setup", u"3", None))
        self.comboBox_Connection.setItemText(3, QCoreApplication.translate("Setup", u"4", None))

        self.pushButton_ok.setText(QCoreApplication.translate("Setup", u"Ok", None))
        self.pushButton_close.setText(QCoreApplication.translate("Setup", u"Close", None))
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

        self.groupBox_Mode.setTitle(QCoreApplication.translate("Setup", u"Mode", None))
        self.radioButton_RTU.setText(QCoreApplication.translate("Setup", u"RTU", None))
        self.radioButton_ASCII.setText(QCoreApplication.translate("Setup", u"ASCII", None))
        self.groupBox_SlaveID.setTitle(QCoreApplication.translate("Setup", u"Unit ID", None))
        self.lineEdit_SlaveID.setText(QCoreApplication.translate("Setup", u"1", None))
        self.groupBox_ResTout.setTitle(QCoreApplication.translate("Setup", u"Response Timeout", None))
        self.lineEdit_ResTout.setText(QCoreApplication.translate("Setup", u"1000", None))
        self.label_ResTout.setText(QCoreApplication.translate("Setup", u"[ms]", None))
        self.groupBox_Remote.setTitle(QCoreApplication.translate("Setup", u"Remote ModBus Server", None))
        self.radioButton_IPv4.setText(QCoreApplication.translate("Setup", u"IPv4", None))
        self.radioButton_IPv6.setText(QCoreApplication.translate("Setup", u"IPv6", None))
        self.label_IP.setText(QCoreApplication.translate("Setup", u"IP Address or Node Name", None))
        self.lineEdit_ConnectTout.setText(QCoreApplication.translate("Setup", u"3000", None))
        self.label_ConnectToutMS.setText(QCoreApplication.translate("Setup", u"Connection Timeout", None))
        self.comboBox_IP.setItemText(0, QCoreApplication.translate("Setup", u"127.0.0.1", None))

        self.label_ConnectTout.setText(QCoreApplication.translate("Setup", u"[ms]", None))
        self.label_ServePort.setText(QCoreApplication.translate("Setup", u"Server Port", None))
        self.lineEdit_ServerPort.setText(QCoreApplication.translate("Setup", u"502", None))
    # retranslateUi

