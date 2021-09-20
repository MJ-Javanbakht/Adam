import sys
import os
import time
from pymodbus.client.sync import ModbusSerialClient as ModbusClient
from pymodbus.register_read_message import ReadHoldingRegistersResponse
from pymodbus.exceptions import *

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

        # MAKE THE LINE EDITS ACCEPT ONLY DIGITS
        # ///////////////////////////////////////////////////////////////
        lineEdits = widgets.setting.findChildren(QLineEdit)
        for l in lineEdits:
            l.setValidator(QRegularExpressionValidator(QRegularExpression('[0-9]+\.?[0-9]+')))
        
        lineEdits = widgets.calibration.findChildren(QLineEdit)
        for l in lineEdits:
            l.setValidator(QRegularExpressionValidator(QRegularExpression('[0-9]+')))

        # USE CUSTOM TITLE BAR | USE AS "False" FOR MAC OR LINUX
        # ///////////////////////////////////////////////////////////////
        Settings.ENABLE_CUSTOM_TITLE_BAR = True

        # APP NAME
        # ///////////////////////////////////////////////////////////////
        title = "Ayra"
        description = "Ayra cards GUI"
        # APPLY TEXTS
        self.setWindowTitle(title)
        widgets.titleRightInfo.setText(description)
        widgets.titleLeftDescription.setText('GUI for A/D/Universal cards')

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

        # RADIOBUTTONs CHECK
        radioButtons = widgets.home.findChildren(QRadioButton)
        for r in radioButtons:
           r.toggled.connect(self.radioChanged)

        # SCALE COMBOBOXs CHANGE
        comboBoxs = widgets.setting.findChildren(QComboBox)
        for c in comboBoxs:
           c.currentTextChanged.connect(self.comboBoxChanged)
             
        # Scale 65535 checked
        widgets.checkBox_65535.toggled.connect(self.scaleTo65535)

        # Save settings
        widgets.pushButton_saveSetting.clicked.connect(self.changeSetup)

        # Setup client
        # ///////////////////////////////////////////////////////////////
        # Set initial values
        self.deviceName = 'None'
        
        # Get device information
        self.client = self.setupClient()
        widgets.btn_home.click()
        

        # Show device name and connection state
        SetStyleSheet(widgets.stateLabel,font='14pt Bold',color='green',message='Connected')
        SetStyleSheet(self.ui.label_deviceName,'16pt','lightgreen',f"A_{self.deviceName}")
        SetStyleSheet(self.ui.label_deviceNameSetting,'16pt','lightgreen',f"A_{self.deviceName}")
        
        # SHOW APP
        # ///////////////////////////////////////////////////////////////
        self.show()

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
            self.timer = QTimer() 
            self.timer.timeout.connect(self.readRegisters)
            self.timer.start(1000)

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

    # If radioButton is checked
    # ///////////////////////////////////////////////////////////////
    def radioChanged(self):
        radioButton = self.sender()
        device = self.device
        device.radioChanged(radioButton= radioButton)

    # If scale 65535 is checked
    # ///////////////////////////////////////////////////////////////
    def scaleTo65535(self):
        device = self.device
        device.scaleTo65535()

    # If combobox is changed
    # ///////////////////////////////////////////////////////////////
    def comboBoxChanged(self):
        comboBox = self.sender()
        device = self.device
        device.comboBoxChanged(comboBox= comboBox)
        

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

    # CLOSE EVENT
    # ///////////////////////////////////////////////////////////////
    def closeEvent(self, event: QCloseEvent) -> None:
        self.client.close()
        return super().closeEvent(event)

    # Get data from SetupDialog and setup client
    # ///////////////////////////////////////////////////////////////
    def setupClient(self):
        setup = SetupDialog()
        setup.exec()
        ui = setup.ui
        
        if setup.modbusConnectionFlag:
            self.modbusConnectionFlag = setup.modbusConnectionFlag

            self.deviceName = format(setup.deviceName, 'x')
            if self.deviceName == "4017":
                self.device = A_8017(setup.client, ui)

            return setup.client

    # Read registers from device
    # ///////////////////////////////////////////////////////////////
    def readRegisters(self):
        device = self.device
        device.readRegisters()
        

    # Change and send settings
    # ///////////////////////////////////////////////////////////////
    def changeSetup(self):
        device = self.device
        device.changeSetup()


    # Calibrate device
    # ///////////////////////////////////////////////////////////////
    def calibration(self):
        pass

    # Handle errors and log
    # ///////////////////////////////////////////////////////////////
    def errorHandler(self):
        pass

    # Save and export settings
    # ///////////////////////////////////////////////////////////////
    def saveSetting(self):
        pass

# Setup Dialog
# ///////////////////////////////////////////////////////////////
class SetupDialog(QDialog):
    def __init__(self,*args, **kwargs):
        super(SetupDialog, self).__init__(*args, **kwargs)
        
        # Setting the ui
        # ///////////////////////////////////////////////////////////////
        self.ui = Ui_Setup()
        self.ui.setupUi(self)
        title = "Setup"
        self.setWindowTitle(title)
        icon = QIcon("Adam\design\images\icons\AYRALOGO.png")
        self.setWindowIcon(icon)

        self.ui.status = QStatusBar()
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        self.ui.status.setSizePolicy(sizePolicy)
        self.ui.verticalLayout_statusBar.addWidget(self.ui.status)

        SetStyleSheet(widget= self.ui.status,color='white', message='Press Ok to connect')

        # Value to check if device is connected
        # ///////////////////////////////////////////////////////////////
        self.modbusConnectionFlag = False
        self.connection = False

        self.ui.pushButton_ok.clicked.connect(self.buttonClick)
        self.ui.pushButton_close.clicked.connect(self.buttonClick)
        
    # MOUSE CLICK EVENTS
    # ///////////////////////////////////////////////////////////////
    def buttonClick(self):
        # GET BUTTON CLICKED
        btn = self.sender()
        btnName = btn.objectName()

        if btnName == 'pushButton_ok':
            self.client = self.connectionCheck()
            
        elif btnName == 'pushButton_close':
            MessageBox()            
            sys.exit()

    # CLOSE EVENT
    # ///////////////////////////////////////////////////////////////
    def closeEvent(self, arg__1: QCloseEvent) -> None:
        return super().closeEvent(arg__1)
        MessageBox()
        sys.exit()
        
    # Check the connection
    # ///////////////////////////////////////////////////////////////
    def connectionCheck(self):
        method = self.ui.radioButton_RTU.text().lower()
        port = self.ui.comboBox_COM.currentText()
        bytesize = int(self.ui.comboBox_DataBits.currentText())
        baudrate = int(self.ui.comboBox_BaudRate.currentText())
        parity = self.ui.comboBox_Parity.currentText()[0]
        timeout = int(self.ui.lineEdit_ResTout.text())/1000
        stopbits = int(self.ui.comboBox_StopBits.currentText())
        
        client = ModbusClient(method= method, port= port, stopbits= stopbits,
         bytesize= bytesize, parity= parity, baudrate= baudrate, timeout= timeout)
        
        client.unitID = int(self.ui.spinBox_UnitID.text())

        if self.connection == False:
            self.connection = client.connect()

        if self.connection == True:
            mapregister = client.read_holding_registers(20,1,unit= client.unitID)
            if isinstance(mapregister, ReadHoldingRegistersResponse):
                SetStyleSheet(self.ui.status,color='green',message='Connecting...')
                self.deviceName = mapregister.getRegister(0)
                self.modbusConnectionFlag = True
                time.sleep(0.5)
                self.close()
                return client
            elif isinstance(mapregister, ModbusIOException):
                self.modbusConnectionFlag = False
                time.sleep(0.5)
                SetStyleSheet(self.ui.status,color='red',message=mapregister.message)
            else:
                self.modbusConnectionFlag = False
                time.sleep(0.5)
                SetStyleSheet(self.ui.status,color='red',message='ModBus is not responding!')
        else:
            self.modbusConnectionFlag = False
            time.sleep(0.5)
            SetStyleSheet(self.ui.status,color='red',message=f'Could not open port {self.ui.comboBox_COM.currentText()}')

# Message Dialog
# ///////////////////////////////////////////////////////////////
class MessageBox(QMessageBox):
    def __init__(self, icon, title, text, buttons, *args, **kwargs):
        QMessageBox.__init__(self, icon, title, text, buttons, *args, **kwargs)
        self.setStyleSheet(u""
"QWidget{\n"
"	color: rgb(221, 221, 221);\n"
"	font: 13pt \"Segoe UI\";\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"/* Button */\n"
"QPushButton {\n"
"	border: 2px solid rgb(150, 150, 150);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n" 
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}\n"
"\n"
"")
        self.setIcon(icon)
        self.setWindowTitle(title)
        self.setText(text)
        self.setStandardButtons(buttons)

        winicon = QIcon("Adam\design\images\icons\AYRALOGO.png")
        self.setWindowIcon(winicon)        
        
        self.accepted.connect(self.acceptValue)
        self.rejected.connect(self.rejectValue)
        
        self.exec()

    def acceptValue(self):
        self.value= True

    def rejectValue(self):
        self.value= False

# Color and Text for widgets
# ///////////////////////////////////////////////////////////////
class SetStyleSheet():
    def __init__(self, widget, font= '12pt', color= 'white', message= None):
        widget.setStyleSheet(f'font: {font}; color: {color}')
        if isinstance(widget,QStatusBar): widget.showMessage(message)
        elif isinstance(widget, QMessageBox): widget.setText(message)
        elif isinstance(widget, QLabel): widget.setText(message)

# Class for A_8017 device
# ///////////////////////////////////////////////////////////////
class A_8017():
    def __init__(self, client, ui):
        self.client = client

        self.flag65535 = False
        self.scales = {
            'Vl': [0,0,0,0,0,0,0,0],
            'Vh': [10,10,10,10,10,10,10,10],
            'mAl': [4,4,4,4,4,4,4,4],
            'mAh': [20,20,20,20,20,20,20,20]
        }
        self.gains = {
            'v': [],
            'i': []
        }
        for i in range(8):
            self.gains['v'].append((self.scales['Vh'][i] - self.scales['Vl'][i])/65535)
            self.gains['i'].append((self.scales['mAh'][i] - self.scales['mAl'][i])/65535)

        widgets.lineEdit_unitID.setText(ui.spinBox_UnitID.text())
        widgets.comboBox_baudRate.setCurrentIndex(ui.comboBox_BaudRate.currentIndex())
        widgets.lineEdit_timeout.setText(ui.lineEdit_ResTout.text())
        widgets.lineEdit_ResRate.setText('1000')
        
        for i in range(1,9):
            combo = widgets.setting.findChild(QComboBox, f'comboBox_ch{i}scale')
            lineLow = widgets.setting.findChild(QLineEdit, f'lineEdit_ch{i}vLow')
            lineHigh = widgets.setting.findChild(QLineEdit, f'lineEdit_ch{i}vHigh')
            lineLow.setText(str(self.scales[f"{combo.currentText()}l"][i-1]))
            lineHigh.setText(str(self.scales[f"{combo.currentText()}h"][i-1]))

    # Read registers from A_8017 device
    # ///////////////////////////////////////////////////////////////
    def readRegisters(self):
        register = self.client.read_holding_registers(0,8,unit= self.client.unitID)
        self.registers = register.getRegister(slice(0,8))

        vi = self.client.read_holding_registers(10,8,unit= self.client.unitID)
        self.vi = vi.getRegister(slice(0,8))

        # for i in range(8):
        #     if comboBox.objectName() == f'comboBox_ch{r}scale':
        #         widgets.home.findChild(QLabel, f"label_ch{r}scale").setText("mV")
        #         lineLow = widgets.setting.findChild(QLineEdit, f'lineEdit_ch{r}vLow')
        #         lineHigh = widgets.setting.findChild(QLineEdit, f'lineEdit_ch{r}vHigh')
        #         lineLow.setText(str(self.device.scales[f"{comboBox.currentText()}l"][r-1]))
        #         lineHigh.setText(str(self.device.scales[f"{comboBox.currentText()}h"][r-1]))
        #     value = 
        #     widgets.home.findChild(QLineEdit, f'lineEdit_ch{i+1}').setText(str(registers[i]))

        for i in range(8):
            if self.vi[i]:
                widgets.home.findChild(QRadioButton, f'radioButton_ch{i+1}i').setChecked(True)
                widgets.home.findChild(QLabel, f'label_ch{i+1}scale').setText('mA')
                if self.flag65535 == True:
                    value = self.registers[i]
                else:
                    value = self.scales['mAl'][i] + (self.registers[i] * self.gains['i'][i])
                widgets.home.findChild(QLineEdit, f'lineEdit_ch{i+1}').setText(str(value))
            else:
                widgets.home.findChild(QRadioButton, f'radioButton_ch{i+1}v').setChecked(True)
                widgets.home.findChild(QLabel, f'label_ch{i+1}scale').setText('V')
                if self.flag65535 == True:
                    value = self.registers[i]
                else:
                    value = self.scales['Vl'][i] + (self.registers[i] * self.gains['v'][i])
                widgets.home.findChild(QLineEdit, f'lineEdit_ch{i+1}').setText(str(value))

    def radioChanged(self, radioButton):
        for i in range(8):
            if radioButton.objectName() == f'radioButton_ch{i+1}i':
                if widgets.home.findChild(QRadioButton, f'radioButton_ch{i+1}v').isChecked():
                    widgets.home.findChild(QLabel, f"label_ch{i+1}scale").setText("V")
                    lineEdit = widgets.home.findChild(QLineEdit, f"lineEdit_ch{i+1}")
                    if self.flag65535 == True:
                        value = self.registers[i]
                    else:
                        value = self.scales['Vl'][i] + (self.registers[i] * self.gains['v'][i])
                    lineEdit.setText(str(value))
                    self.client.write_registers(10+i, 0, unit= self.client.unitID)
                elif widgets.home.findChild(QRadioButton, f'radioButton_ch{i+1}i').isChecked():
                    widgets.home.findChild(QLabel, f"label_ch{i+1}scale").setText("mA")
                    lineEdit = widgets.home.findChild(QLineEdit, f"lineEdit_ch{i+1}")
                    if self.flag65535 == True:
                        value = self.registers[i]
                    else:
                        value = self.scales['mAl'][i] + (self.registers[i] * self.gains['i'][i])
                    lineEdit.setText(str(value))
                    self.client.write_registers(10+i, 1, unit= self.client.unitID)
                    
    def scaleTo65535(self):
        if widgets.checkBox_65535.isChecked():
            self.flag65535 = True
        else:
            self.flag65535 = False

    def comboBoxChanged(self, comboBox):
        for i in range(8):
            if comboBox.objectName() == f'comboBox_ch{i+1}scale':
                lineLow = widgets.setting.findChild(QLineEdit, f'lineEdit_ch{i+1}vLow')
                lineHigh = widgets.setting.findChild(QLineEdit, f'lineEdit_ch{i+1}vHigh')
                lineLow.setText(str(self.scales[f"{comboBox.currentText()}l"][i]))
                lineHigh.setText(str(self.scales[f"{comboBox.currentText()}h"][i]))

    def changeSetup(self):
        msgBox = MessageBox(
            icon= QMessageBox.Warning,
            title= "Save",
            text= u"This would write Unit ID and Baudrate into device,\n"
            "and you may need to reconnect. Continue?",
            buttons= QMessageBox.StandardButtons(QMessageBox.Ok|QMessageBox.Cancel)
        )
        if msgBox.value:
            for i in range(1,9):
                widgets.comboBox_ch1scale
                combo = widgets.setting.findChild(QComboBox, f"comboBox_ch{i}scale")
                low = widgets.setting.findChild(QLineEdit, f"lineEdit_ch{i}vLow")
                high = widgets.setting.findChild(QLineEdit, f"lineEdit_ch{i}vLow")
                self.scales[f"{combo.currentText()}l"][i-1] = int(low.text())
                self.scales[f"{combo.currentText()}h"][i-1] = int(high.text())
            
            self.client.timeout = int(widgets.lineEdit_timeout.text()) / 1000
            unit = int(widgets.lineEdit_unitID.text())
            baudrate = int(widgets.comboBox_baudRate.currentText())
            self.client.write_registers(25, [unit, baudrate],unit= self.client.unitID)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
