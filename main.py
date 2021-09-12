import sys
import os
import platform
from pymodbus.client.sync import ModbusSerialClient as ModbusClient

# IMPORT / GUI AND MODULES AND WIDGETS
# ///////////////////////////////////////////////////////////////
from modules import *
from widgets import *
os.environ["QT_FONT_DPI"] = "96" # FIX Problem for High DPI and Scale above 100%

# SET AS GLOBAL WIDGETS
# ///////////////////////////////////////////////////////////////
widgets = None

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        # SET AS GLOBAL WIDGETS
        # ///////////////////////////////////////////////////////////////
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        global widgets
        widgets = self.ui
        icon = QPixmap('Adam\design\images\images\AYRALOGO.png')
        self.setWindowIcon(icon)
        widgets.stateLabel.setStyleSheet('font: 13pt; color: rgb(100,189,100);')

        # MAKE THE LINE EDITS ACCEPT ONLY DIGITS
        # ///////////////////////////////////////////////////////////////
        lineEdits = widgets.setting.findChildren(QLineEdit)
        for l in lineEdits:
            l.setValidator(QRegularExpressionValidator(QRegularExpression('[0-9]+')))

        lineEdits = widgets.calibration.findChildren(QLineEdit)
        for l in lineEdits:
            l.setValidator(QRegularExpressionValidator(QRegularExpression('[0-9]+')))

        # USE CUSTOM TITLE BAR | USE AS "False" FOR MAC OR LINUX
        # ///////////////////////////////////////////////////////////////
        Settings.ENABLE_CUSTOM_TITLE_BAR = True

        # APP NAME
        # ///////////////////////////////////////////////////////////////
        title = "Adam"
        description = "Connection Setup (Based on ModBus)"
        # APPLY TEXTS
        self.setWindowTitle(title)
        widgets.titleRightInfo.setText(description)

        # TOGGLE MENU
        # ///////////////////////////////////////////////////////////////
        widgets.toggleButton.clicked.connect(lambda: UIFunctions.toggleMenu(self, True))

        # SET UI DEFINITIONS
        # ///////////////////////////////////////////////////////////////
        UIFunctions.uiDefinitions(self)

        # QTableWidget PARAMETERS
        # ///////////////////////////////////////////////////////////////
        widgets.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # BUTTONS CLICK
        # ///////////////////////////////////////////////////////////////

        # LEFT MENUS
        widgets.btn_home.clicked.connect(self.buttonClick)
        widgets.btn_setting.clicked.connect(self.buttonClick)
        widgets.btn_calibration.clicked.connect(self.buttonClick)
        widgets.btn_log.clicked.connect(self.buttonClick)
        widgets.btn_trend.clicked.connect(self.buttonClick)
        

        # EXTRA LEFT BOX
        def openCloseLeftBox():
            UIFunctions.toggleLeftBox(self, True)
        widgets.toggleLeftBox.clicked.connect(openCloseLeftBox)
        widgets.extraCloseColumnBtn.clicked.connect(openCloseLeftBox)

        # EXTRA RIGHT BOX
        def openCloseRightBox():
            UIFunctions.toggleRightBox(self, True)
        widgets.settingsTopBtn.clicked.connect(openCloseRightBox)

        # Open Setup Dialog
        # ///////////////////////////////////////////////////////////////
        setup = SetupDialog()
        setup.exec()

        # if setup.value:
        widgets.stateLabel.setText('Connected')
        self.show()
        # self.client = setup.client
            # self.connection = self.client.connect()

        # self.register = self.client.read_holding_registers(0,8,unit= int(setup.ui.lineEdit_SlaveID.text()))
        # print(self.register.getRegister(0))
        
        # SHOW APP
        # ///////////////////////////////////////////////////////////////
        # self.show()

        # SET CUSTOM THEME
        # ///////////////////////////////////////////////////////////////
        useCustomTheme = False
        themeFile = "Adam\\themes\py_dracula_light.qss"

        # SET THEME AND HACKS
        if useCustomTheme:
            # LOAD AND APPLY STYLE
            UIFunctions.theme(self, themeFile, True)

            # SET HACKS
            AppFunctions.setThemeHack(self)

        # SET HOME PAGE AND SELECT MENU
        # ///////////////////////////////////////////////////////////////
        widgets.stackedWidget.setCurrentWidget(widgets.home)
        widgets.btn_home.setStyleSheet(UIFunctions.selectMenu(widgets.btn_home.styleSheet()))

        # self.client.close()


    # BUTTONS CLICK
    # Post here your functions for clicked buttons
    # ///////////////////////////////////////////////////////////////
    def buttonClick(self):
        # GET BUTTON CLICKED
        btn = self.sender()
        btnName = btn.objectName()

        # SHOW HOME PAGE
        if btnName == "btn_home":
            widgets.stackedWidget.setCurrentWidget(widgets.home)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        # SHOW WIDGETS PAGE
        elif btnName == "btn_setting":
            widgets.stackedWidget.setCurrentWidget(widgets.setting)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        # SHOW NEW PAGE
        elif btnName == "btn_calibration":
            widgets.stackedWidget.setCurrentWidget(widgets.calibration) # SET PAGE
            UIFunctions.resetStyle(self, btnName) # RESET ANOTHERS BUTTONS SELECTED
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet())) # SELECT MENU

        elif btnName == "btn_log":
            widgets.stackedWidget.setCurrentWidget(widgets.log)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        elif btnName == "btn_trend":
            widgets.stackedWidget.setCurrentWidget(widgets.widgets)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        # PRINT BTN NAME
        print(f'Button "{btnName}" pressed!')


    # RESIZE EVENTS
    # ///////////////////////////////////////////////////////////////
    def resizeEvent(self, event):
        # Update Size Grips
        UIFunctions.resize_grips(self)

    # MOUSE CLICK EVENTS
    # ///////////////////////////////////////////////////////////////
    def mousePressEvent(self, event):
        # SET DRAG POS WINDOW
        self.dragPos = event.globalPos()

        # PRINT MOUSE EVENTS
        if event.buttons() == Qt.LeftButton:
            print('Mouse click: LEFT CLICK')
        if event.buttons() == Qt.RightButton:
            print('Mouse click: RIGHT CLICK')

# Setup Dialog
# ///////////////////////////////////////////////////////////////
class SetupDialog(QDialog):
    def __init__(self,*args, **kwargs):
        super(SetupDialog, self).__init__(*args, **kwargs)
        
        # setting the ui
        # ///////////////////////////////////////////////////////////////
        self.ui = Ui_Setup()
        self.ui.setupUi(self)
        title = "Setup"
        self.setWindowTitle(title)
        icon = QIcon("Adam\design\images\icons\AYRALOGO.png")
        self.setWindowIcon(icon)
        self.ui.status = QStatusBar()
        self.ui.verticalLayout_statusBar.addWidget(self.ui.status)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        self.ui.status.setSizePolicy(sizePolicy)
        self.ui.status.showMessage("Press OK to connect")
        # self.show()

        # Value to check if device is connected
        # ///////////////////////////////////////////////////////////////
        self.value = False

        self.ui.pushButton_ok.clicked.connect(self.buttonClick)
        self.ui.pushButton_close.clicked.connect(self.buttonClick)
        
    # MOUSE CLICK EVENTS
    # ///////////////////////////////////////////////////////////////
    def buttonClick(self):
        # GET BUTTON CLICKED
        btn = self.sender()
        btnName = btn.objectName()

        if btnName == 'pushButton_ok':
            self.connectCheck()

        if btnName == 'pushButton_close':
            sys.exit()

    # MCheck the connection
    # ///////////////////////////////////////////////////////////////
    def connectCheck(self):
        # self.connectToPort()
        # connection = self.client.connect()
        # mapreg = self.client.read_holding_registers(20,1,unit= 1)
        # print(mapreg.getRegister(0))
        # if connection:
        #     self.value = True
        #     self.setStatusTip('')
            self.close()
        # else:
        #     self.value = False
        #     self.setStatusTip('Cannot connect to the port!') 
        # self.close()

    # Set client
    # ///////////////////////////////////////////////////////////////
    def connectToPort(self):
        # method = self.ui.radioButton_RTU.text().lower()
        # port = self.ui.comboBox_COM.currentText()
        # bytesize = int(self.ui.comboBox_DataBits.currentText())
        # baudrate = int(self.ui.comboBox_BaudRate.currentText())
        # timeout = int(self.ui.lineEdit_ResTout.text())
        # # print(method + port + str(bytesize) + str(baudrate) + str(timeout))
        # self.client = ModbusClient(method= method, port= port, stopbits= 1, bytesize= bytesize, parity= 'N',
        # baudrate= baudrate, timeout= timeout)
        pass
        # return client

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("Ayra.ico"))
    window = MainWindow()
    sys.exit(app.exec())
