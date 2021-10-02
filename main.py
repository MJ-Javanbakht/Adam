import sys
import os
import time
from serial.tools import list_ports

from pymodbus.client.sync import ModbusSerialClient as ModbusClient
from pymodbus.register_read_message import ReadHoldingRegistersResponse
from pymodbus.register_write_message import WriteMultipleRegistersResponse, WriteSingleRegisterResponse
from pymodbus.exceptions import *
from serial.tools.list_ports_windows import NULL

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
        lineEdits = widgets.home.findChildren(QLineEdit)
        for l in lineEdits:
            l.setValidator(QRegularExpressionValidator(QRegularExpression('[0-9]+\.?[0-9]{,4}')))

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
        comboBoxSetting = widgets.setting.findChildren(QComboBox)
        for c in comboBoxSetting:
           c.currentTextChanged.connect(self.comboBoxChanged)

        comboBoxCalibration = widgets.calibration.findChildren(QComboBox)
        for c in comboBoxCalibration:
           c.currentTextChanged.connect(self.comboBoxChanged)
             
        # Scale 65535 checked
        widgets.checkBox_65535.toggled.connect(self.scaleTo65535)

        # Save settings
        widgets.pushButton_saveSetting.clicked.connect(self.changeSetup)

        # Set buttons clicked
        pushButtons = widgets.calibration.findChildren(QPushButton)
        for p in pushButtons:
           p.clicked.connect(self.calibrateDevice)

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

            self.endCalibration()

            self.timerRead = QTimer() 
            self.timerRead.timeout.connect(self.readRegisters)
            self.timerRead.timeout.emit()
            resRate = int(widgets.lineEdit_ResRate.text())
            self.timerRead.start(resRate)

        # SHOW WIDGETS PAGE
        elif btnName == "btn_setting":
            widgets.stackedWidget.setCurrentWidget(widgets.setting)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

            self.endCalibration()

        # SHOW NEW PAGE
        elif btnName == "btn_calibration":
            widgets.stackedWidget.setCurrentWidget(widgets.calibration) # SET PAGE
            UIFunctions.resetStyle(self, btnName) # RESET ANOTHERS BUTTONS SELECTED
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet())) # SELECT MENU
            self.timerCal = QTimer() 
            self.timerCal.timeout.connect(self.calibration)
            self.timerCal.timeout.emit()
            resRate = int(widgets.lineEdit_ResRate.text())
            self.timerCal.start(resRate)

        elif btnName == "btn_log":
            widgets.stackedWidget.setCurrentWidget(widgets.log)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

            self.endCalibration()

        elif btnName == "btn_trend":
            widgets.stackedWidget.setCurrentWidget(widgets.widgets)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

            self.endCalibration()

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
            if self.deviceName == "8017":
                self.device = A_8017(setup.client, ui)

            return setup.client

    # Read registers from device
    # ///////////////////////////////////////////////////////////////
    def readRegisters(self):
        device = self.device
        device.readRegisters()
        
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

    # Change and send settings
    # ///////////////////////////////////////////////////////////////
    def changeSetup(self):
        device = self.device
        device.changeSetup()

    # Set values for calibration page
    # ///////////////////////////////////////////////////////////////
    def calibration(self):
        device = self.device
        device.readCalibrationValues()

    # Calibrate device
    # ///////////////////////////////////////////////////////////////
    def calibrateDevice(self):
        button = self.sender()
        device = self.device
        device.calibrateDevice(button= button)

    # Save calibration setting
    # ///////////////////////////////////////////////////////////////
    def endCalibration(self):
        device = self.device
        device.endCalibration()
        
    # Handle errors and log
    # ///////////////////////////////////////////////////////////////
    def errorHandler(self, function, address, value= [], count= 1):
        device = self.device
        device.read_write(function, address, value, count)

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

        self.timerCom = QTimer()
        self.timerCom.timeout.connect(self.readCom)
        self.timerCom.timeout.emit()
        self.timerCom.start(1000)

        

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
            exitMessage = MessageBox(
                icon = QMessageBox.Question,
                title= 'Exit',
                text= 'Do you want to exit?',
                buttons= QMessageBox.StandardButtons(QMessageBox.Ok|QMessageBox.Cancel)
            )
            exitMessage.exec()
            if exitMessage.value == True:
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
        port = f"COM{self.ui.comboBox_COM.currentIndex()+1}"
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
                time.sleep(0.5)
                self.deviceName = mapregister.getRegister(0)
                self.modbusConnectionFlag = True
                self.close()
                return client
            elif isinstance(mapregister, ModbusIOException):
                self.modbusConnectionFlag = False
                time.sleep(0.5)
                SetStyleSheet(self.ui.status,color='red',message=mapregister.message)
            else:
                self.modbusConnectionFlag = False
                time.sleep(0.5)
                try:
                    SetStyleSheet(self.ui.status,color='red',message=mapregister.message)
                except:
                    SetStyleSheet(self.ui.status,color='red',message='ModBus is not responding!')
        else:
            self.modbusConnectionFlag = False
            time.sleep(0.5)
            SetStyleSheet(self.ui.status,color='red',message=f'Could not open port {self.ui.comboBox_COM.currentText()}')

    def readCom(self):
        self.comports = list_ports.comports()
        if self.comports is not NULL:
            for com in self.comports:
                num = int(com[0][-1]) - 1
                self.ui.comboBox_COM.setItemText(num, com[1])
                self.ui.comboBox_COM.setCurrentIndex(num)

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

    def acceptValue(self):
        self.value= True

    def rejectValue(self):
        self.value= False
    
    def closeEvent(self, event: QCloseEvent):
        return super().closeEvent(event)

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
        self.startCalibrationFlag = False
        self.scales = {
            'Vl': [0,0,0,0,0,0,0,0],
            'Vh': [10,10,10,10,10,10,10,10],
            'mAl': [0,0,0,0,0,0,0,0],
            'mAh': [20,20,20,20,20,20,20,20]
        }
        self.gains = {
            'V': [],
            'mA': []
        }
        for i in range(8):
            self.gains['V'].append((self.scales['Vh'][i] - self.scales['Vl'][i])/65535)
            self.gains['mA'].append((self.scales['mAh'][i] - self.scales['mAl'][i])/65535)
        # print(self.gains)

        registers = self.read_write(
            function='read_holding_registers',
            address=25,
            count=2
        )
        if registers != False:
            unit = registers.getRegister(0)
            baudrate = registers.getRegister(1)
        widgets.lineEdit_unitID.setText(str(unit))
        widgets.comboBox_baudRate.setCurrentIndex(baudrate)
        widgets.lineEdit_timeout.setText(ui.lineEdit_ResTout.text())
        widgets.lineEdit_ResRate.setText('1000')
        
        for i in range(8):
            combo = widgets.setting.findChild(QComboBox, f'comboBox_ch{i+1}scale')
            lineLow = widgets.setting.findChild(QLineEdit, f'lineEdit_ch{i+1}vLow')
            lineHigh = widgets.setting.findChild(QLineEdit, f'lineEdit_ch{i+1}vHigh')
            lineLow.setText(str(self.scales[f"{combo.currentText()}l"][i]))
            lineHigh.setText(str(self.scales[f"{combo.currentText()}h"][i]))

    # Read registers from A_8017 device
    # ///////////////////////////////////////////////////////////////
    def readRegisters(self):
        register = self.read_write(
            function="read_holding_registers",
            address=0,
            count=8
        )
        if register != False:
            vi = self.read_write(
                function="read_holding_registers",
                address=10,
                count=8
            )
            if vi != False:
                self.registers = register.getRegister(slice(0,8))
                self.vi = vi.getRegister(slice(0,8))
                for i in range(8):
                    if self.vi[i] == 1:
                        if self.flag65535 == True:
                            value = self.registers[i]
                        else:
                            value = self.scales['Vl'][i] + (self.registers[i] * self.gains['V'][i])
                            value = float("{0:.4f}".format(value))
                        
                        widgets.home.findChild(QRadioButton, f'radioButton_ch{i+1}v').setChecked(True)
                        if value < 1:
                            value = value * 1000
                            widgets.home.findChild(QLabel, f'label_ch{i+1}scale').setText('mV')
                        else:
                            widgets.home.findChild(QLabel, f'label_ch{i+1}scale').setText('V')
                        widgets.home.findChild(QLineEdit, f'lineEdit_ch{i+1}').setText(str(value))
                    else:
                        if self.flag65535 == True:
                            value = self.registers[i]
                        else:
                            value = self.scales['mAl'][i] + (self.registers[i] * self.gains['mA'][i])
                            value = float("{0:.4f}".format(value))
                            
                        widgets.home.findChild(QRadioButton, f'radioButton_ch{i+1}i').setChecked(True)
                        widgets.home.findChild(QLabel, f'label_ch{i+1}scale').setText('mA')
                        widgets.home.findChild(QLineEdit, f'lineEdit_ch{i+1}').setText(str(value))

    def radioChanged(self, radioButton):
        for i in range(8):
            if radioButton.objectName() == f'radioButton_ch{i+1}i' or radioButton.objectName() == f'radioButton_ch{i+1}v':
                if widgets.home.findChild(QRadioButton, f'radioButton_ch{i+1}v').isChecked():
                    writeV = self.read_write(
                        function= "write_register",
                        address=10+i,
                        value=1
                    )
                    # if writeV == True:
                    #     widgets.home.findChild(QLabel, f"label_ch{i+1}scale").setText("V")
                    #     lineEdit = widgets.home.findChild(QLineEdit, f"lineEdit_ch{i+1}")
                    #     if self.flag65535 == True:
                    #         value = self.registers[i]
                    #     else:
                    #         value = self.scales['Vl'][i] + (self.registers[i] * self.gains['V'][i])
                    #     lineEdit.setText(str(value))
                    
                elif widgets.home.findChild(QRadioButton, f'radioButton_ch{i+1}i').isChecked():
                    writeI = self.read_write(
                        function= "write_register",
                        address=10+i,
                        value=0
                    )
                    # if writeI == True:
                    #     widgets.home.findChild(QLabel, f"label_ch{i+1}scale").setText("mA")
                    #     lineEdit = widgets.home.findChild(QLineEdit, f"lineEdit_ch{i+1}")
                    #     if self.flag65535 == True:
                    #         value = self.registers[i]
                    #     else:
                    #         value = self.scales['mAl'][i] + (self.registers[i] * self.gains['mA'][i])
                    #     lineEdit.setText(str(value))
                    
    def scaleTo65535(self):
        if widgets.checkBox_65535.isChecked():
            self.flag65535 = True
        else:
            self.flag65535 = False

    def comboBoxChanged(self, comboBox):
        if comboBox.parentWidget() == widgets.groupBox_calibration:
            for i in range(8):
                if comboBox.objectName() == f'comboBox_ch{i+1}CalScale':
                    if comboBox.currentText() == 'v':
                        writeV = self.read_write(
                            function= "write_register",
                            address=10+i,
                            value=1
                        )
                        # for j in range(5):
                        #     lineEdit = widgets.calibration.findChild(QLineEdit, f"lineEdit_ch{i+1}point{j+1}")
                        #     lineEdit.setText(str(self.vCalVal[i*5 + j]))
                    else:
                        writeI = self.read_write(
                            function= "write_register",
                            address=10+i,
                            value=0
                        )
                        # for j in range(5):
                        #     lineEdit = widgets.calibration.findChild(QLineEdit, f"lineEdit_ch{i+1}point{j+1}")
                        #     lineEdit.setText(str(self.iCalVal[i*5 + j]))

        elif comboBox.parentWidget() == widgets.setting:
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
        msgBox.exec()
        if msgBox.value == True:
            for i in range(8):
                combo = widgets.setting.findChild(QComboBox, f"comboBox_ch{i+1}scale")
                low = widgets.setting.findChild(QLineEdit, f"lineEdit_ch{i+1}vLow")
                high = widgets.setting.findChild(QLineEdit, f"lineEdit_ch{i+1}vHigh")
                self.scales[f"{combo.currentText()}l"][i] = float(low.text())
                self.scales[f"{combo.currentText()}h"][i] = float(high.text())
                self.gains[combo.currentText()][i] = (self.scales[f"{combo.currentText()}h"][i] - self.scales[f"{combo.currentText()}l"][i])/65535
            # print(self.gains)
            self.client.timeout = int(widgets.lineEdit_timeout.text()) / 1000
            unit = int(widgets.lineEdit_unitID.text())
            baudrate = int(widgets.comboBox_baudRate.currentIndex())
            writeBaudrate = self.read_write(
                function='write_registers',
                address=26,
                value=baudrate
            )
            if writeBaudrate != False:
                writeUnit = self.read_write(
                    function='write_registers',
                    address=25,
                    value=unit
                )
                if writeUnit != False:
                    saveMsgBox = MessageBox(
                        icon=QMessageBox.Question,
                        title="Setting",
                        text="Setting saved. Try to reconnect?",
                        buttons=QMessageBox.StandardButtons(QMessageBox.Ok|QMessageBox.Cancel)
                    )
                    saveMsgBox.exec()
                    if saveMsgBox.value == True:
                        # MainWindow.close(MainWindow)
                        # app.closeAllWindows()
                        # self.client.close()
                        # sys.exit(app.exec())
                        # os.execl(sys.executable, *sys.argv)
                        QCoreApplication.quit()
                        status = QProcess.startDetached(sys.executable, sys.argv)
                        # print(status)
                    

    def readCalibrationValues(self):
        vCalibrateValues = self.read_write(
            function="read_holding_registers",
            address=30,
            count=80
        )
        if vCalibrateValues != False:
            iCalibrateValues = self.read_write(
                function="read_holding_registers",
                address=110,
                count=80
            )
            if iCalibrateValues != False:
                self.vCalVal = vCalibrateValues.getRegister(slice(1,80,2))
                self.vCalSet = vCalibrateValues.getRegister(slice(0,79,2))
                self.iCalVal = iCalibrateValues.getRegister(slice(1,80,2))
                self.iCalSet = iCalibrateValues.getRegister(slice(0,79,2))

                for i in range(8):
                    comboBox = widgets.calibration.findChild(QComboBox, f"comboBox_ch{i+1}CalScale")
                    if comboBox.currentText() == 'v':
                        for j in range(5):
                            lineEdit = widgets.calibration.findChild(QLineEdit, f"lineEdit_ch{i+1}point{j+1}")
                            lineEdit.setText(str(self.vCalVal[i*5 + j]))
                    else:
                        for j in range(5):
                            lineEdit = widgets.calibration.findChild(QLineEdit, f"lineEdit_ch{i+1}point{j+1}")
                            lineEdit.setText(str(self.iCalVal[i*5 + j]))
                
                if self.startCalibrationFlag == False:
                    startCalibration = self.read_write(
                        function='write_register',
                        address=29,
                        value=1
                    )
                    while startCalibration == False:
                        startCalFailed = MessageBox(
                            icon=QMessageBox.Question,
                            title='Calibration',
                            text='Can not start calibration,\ntry again?',
                            buttons=QMessageBox.StandardButtons(QMessageBox.Ok|QMessageBox.Cancel)
                        )
                        startCalFailed.exec()
                        if startCalFailed.value == False:
                            widgets.btn_home.click()
                        else:
                            startCalibration = self.read_write(
                                function='write_register',
                                address=29,
                                value=1
                            )
                            if startCalibration != False:
                                self.startCalibrationFlag = True
            
    def endCalibration(self):
        endCalibration = self.read_write(
            function="write_register",
            address=29,
            value=0
        )
        while endCalibration == False:
            CalFailedMsg = MessageBox(
                icon= QMessageBox.Warning,
                title="Calibration",
                text="Couldn't save calibration setting,\ntry again?",
                buttons= QMessageBox.StandardButtons(QMessageBox.Ok|QMessageBox.Cancel)
            )
            CalFailedMsg.exec()
            if CalFailedMsg.value == False:
                break
            endCalibration = self.read_write(
                function="write_register",
                address=29,
                value=0
            )
        if endCalibration != False:
            self.startCalibrationFlag = False
    
    
    def calibrateDevice(self, button):
        self.calSetFlag = True
        name = button.objectName()
        # button.objectName() = pushButton_ch1point1
        self.point = int(name[-1]) - 1
        self.channel = int(name[-7]) - 1
        print(self.channel, self.point)

        lineEdit = widgets.calibration.findChild(QLineEdit, f"lineEdit_ch{self.channel+1}point{self.point+1}")
        self.value = int(lineEdit.text())
        self.comboBox = lineEdit = widgets.calibration.findChild(QComboBox, f"comboBox_ch{self.channel+1}CalScale")
        if self.comboBox.currentText() == 'v':
            self.address = 30 + self.channel*10 + self.point*2
        else:
            self.address = 110 + self.channel*10 + self.point*2

        writePointVal = self.read_write(
            function="write_register",
            address=self.address+1,
            value=self.value
        )
        if writePointVal == False:
            return
        writeSetVal = self.read_write(
            function="write_register",
            address=self.address,
            value=1
        )
        if writeSetVal == False:
            return
            
        self.msgBox = MessageBox(
            icon= QMessageBox.Information,
            title= "Calibrating",
            text= "Please wait while device is calibrating the point...",
            buttons= QMessageBox.NoButton
        )
        self.msgBox.show()
        
        self.timerSetVal = QTimer()
        self.timerSetVal.timePassed = 0
        self.timerSetVal.timeout.connect(self.readSetVal)
        self.timerSetVal.timeout.emit()
        self.timerSetVal.start(500)

    def readSetVal(self):
        self.timerSetVal.timePassed += 0.5
        setReg = self.read_write(
            function="read_holding_registers",
            address=self.address,
            count=1
        )
        if setReg != False:
            setVal = setReg.getRegister(0)
            print(setVal)
            if setVal == 0:
                self.calSetFlag = False
                self.msgBox.setInformativeText("<font color= 'green'> Calibrated! </font>")

                time.sleep(0.5)
                print('calibrated')
                if self.comboBox.currentText() == 'v':
                    self.vCalVal[self.channel*5 + self.point] = self.value
                else:
                    self.iCalVal[self.channel*5 + self.point] = self.value

                self.msgBox.hide()

                msgCalSuccess = MessageBox(
                    icon= QMessageBox.Information,
                    title= 'Calibration',
                    text= u"<font color= 'green'>Calibration Successful.</font>",
                    buttons= QMessageBox.Ok
                )
                msgCalSuccess.setInformativeText('Wait....')
                SetStyleSheet(widget= widgets.stateLabel,font= '14pt Bold',color='green',message='Calibrated Successfully!')
                time.sleep(1)
                calibratedRegister = self.read_write(
                    'read_holding_registers',
                    address=0+self.channel,
                    count=1
                )
                if calibratedRegister == False:
                    msgCalSuccess.setInformativeText("Couldn't read the calibrated register.")
                else:
                    register = calibratedRegister.getRegister(0)
                    msgCalSuccess.setInformativeText(f"Calibrated register: {register}")
                msgCalSuccess.exec()
                self.timerSetVal.stop()

            elif self.timerSetVal.timePassed >= 5:
                self.msgBox.hide()
                msgCalFailed = MessageBox(
                    icon= QMessageBox.Information,
                    title= 'Calibration',
                    text= 'Calibration timeout. Please try again.',
                    buttons= QMessageBox.Ok
                )
                SetStyleSheet(widget= widgets.stateLabel,font= '14pt Bold',color='red',message='Calibration Failed!')
                msgCalFailed.exec()
                self.timerSetVal.stop()
        
    def read_write(self, function, address, value= [], count= 1):
        errorCount = 0
        if function == 'read_holding_registers':
            while errorCount < 3:
                response = self.client.read_holding_registers(address, count,unit=self.client.unitID)
                if isinstance(response, ReadHoldingRegistersResponse):
                    SetStyleSheet(widget= widgets.stateLabel,font= '14pt Bold',color='green',message='Connected')
                    return response
                errorCount += 1
        elif function == 'write_registers':
            while errorCount < 3:
                response = self.client.write_registers(address, value,unit=self.client.unitID)
                if isinstance(response, WriteMultipleRegistersResponse):
                    SetStyleSheet(widget= widgets.stateLabel,font= '14pt Bold',color='green',message='Connected')
                    return response
                errorCount += 1
        elif function == 'write_register':
            while errorCount < 3:
                response = self.client.write_register(address, value,unit=self.client.unitID)
                if isinstance(response, WriteSingleRegisterResponse):
                    SetStyleSheet(widget= widgets.stateLabel,font= '14pt Bold',color='green',message='Connected')
                    return response
                errorCount += 1
        if errorCount >= 3:
            SetStyleSheet(widget= widgets.stateLabel,font= '14pt Bold',color='red',message='Error')
            # time.sleep(0.1)
            return False


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
