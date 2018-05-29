import sys,os
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import *
import resource
import room_core
import threading
import camera_core
import subprocess

class mainPage(QMainWindow):
    def __init__(self, parent=None):
        super(mainPage, self).__init__(parent)
        self.setFixedSize(720, 480)
        self.move(100,100)
        self.setWindowTitle("ROOM remote control")
        self.type = ""
        self.command = ""
        self.streamLabel = QLabel("stream")
        self.cam = camera_core.Camera(self)
        self.coreThread = threading.Thread(target=room_core.programLoop)
        self.coreThread.start()
        self.cameraThread = threading.Thread(target=self.cam.turnIdle)
        self.cameraThread.start()
        self.dest = self.cam.destination[:-1]
        self.brandArr = ["SAMSUNG","LG","HAIER","PANASONIC","HITACHI"]
        self.brand = 0
        self.version = 1
        
        #INIT MAINPAGE BUTTONS
        self.ACbutton = QPushButton("",self)
        self.PJbutton = QPushButton("",self)
        self.TVbutton = QPushButton("",self)
        self.CAMbutton = QPushButton("",self)
        self.ACbutton.setStyleSheet("border-image: url(:/icon/aircon.png);min-height: 150px;max-width: 150px")
        self.PJbutton.setStyleSheet("border-image: url(:/icon/projector.png);min-height: 150px;max-width: 150px")
        self.TVbutton.setStyleSheet("border-image: url(:/icon/tv.png);min-height: 150px;max-width: 150px")
        self.CAMbutton.setStyleSheet("border-image: url(:/icon/cam.png);min-height: 150px;max-width: 150px")
        
        #INIT REMOTE DATA
        self.brandLabel = QLabel("SAMSUNG")
        self.versionLabel = QLabel("1")
        self.versionLabel.setAlignment(Qt.AlignCenter)
        self.brandLabel.setAlignment(Qt.AlignCenter)

        #CENTRAL WIDGET
        self.central_wid = QWidget()
        self.layout_for_wids = QStackedLayout()

        #INIT PAGES
        self.mainInit()

        self.remoteInit()
        self.camInit()
        self.streamInit()
        #SET CENTRAL WIDGET
        self.central_wid.setLayout(self.layout_for_wids)
        self.setCentralWidget(self.central_wid)
            
    def mainInit(self):
        self.horizontalGroupBox = QGroupBox("Select your device")
        self.horizontalGroupBox.setFixedSize(710,470)
        self.horizontalGroupBox.setStyleSheet("QGroupBox {border: 1px solid gray;margin-top: 0.5em;margin-left: 0.5em} QGroupBox::title {subcontrol-origin: margin;left: 10px;padding: 0 3px 0 3px;}")
        vbox = QVBoxLayout()
        hbox1 = QHBoxLayout()
        hbox2 = QHBoxLayout()

        hbox1.addWidget(self.ACbutton)
        self.ACbutton.clicked.connect(self.airconConnect)
        
        hbox1.addWidget(self.PJbutton)
        self.PJbutton.clicked.connect(self.projectorConnect)

        vbox.addLayout(hbox1)
        
        hbox2.addWidget(self.TVbutton)
        self.TVbutton.clicked.connect(self.tvConnect)
        
        hbox2.addWidget(self.CAMbutton)  
        self.CAMbutton.clicked.connect(self.camConnect)

        vbox.addLayout(hbox2)
        self.horizontalGroupBox.setLayout(vbox)
        
        self.layout_for_wids.addWidget(self.horizontalGroupBox)
        
    def camInit(self):
        self.CAMGroupBox = QGroupBox("Camera module")
        self.CAMGroupBox.setFixedSize(710,470)
        self.CAMGroupBox.setStyleSheet("QGroupBox {border: 1px solid gray;margin-top: 0.5em;margin-left: 0.5em} QGroupBox::title {subcontrol-origin: margin;left: 10px;padding: 0 3px 0 3px;}")
        self.camButton = QPushButton("camera streaming",self)
        self.openButton = QPushButton("open save folder",self)
        self.backButton = QPushButton("back",self)
        vbox = QVBoxLayout()
        vbox.addWidget(self.openButton)
        vbox.addWidget(self.camButton)
        vbox.addWidget(self.backButton)

        self.CAMGroupBox.setLayout(vbox)

        #CONNECT BUTTONS
        self.backButton.clicked.connect(self.backConnect)
        self.openButton.clicked.connect(self.openFolder)
        self.camButton.clicked.connect(self.streamConnect)

        
        self.layout_for_wids.addWidget(self.CAMGroupBox)
    def streamInit(self):
        self.strGroupBox = QGroupBox("Camera stream")
        self.sbackButton = QPushButton("back")
        self.strGroupBox.setFixedSize(710,470)
        self.strGroupBox.setStyleSheet("QGroupBox {border: 1px solid gray;margin-top: 0.5em;margin-left: 0.5em} QGroupBox::title {subcontrol-origin: margin;left: 10px;padding: 0 3px 0 3px;}")
        vbox = QVBoxLayout()
        vbox.addWidget(self.streamLabel)
        vbox.addWidget(self.sbackButton)
        self.strGroupBox.setLayout(vbox)

        #CONNECT BUTTONS
        self.sbackButton.clicked.connect(self.streamBackConnect)
        self.layout_for_wids.addWidget(self.strGroupBox)

        
    def remoteInit(self):        
        #INIT THE BUTTONS
        self.ACGroupBox = QGroupBox(self.type+" Remote")
        self.ACGroupBox.setFixedSize(710,470)
        self.ACGroupBox.setStyleSheet("QGroupBox {border: 1px solid gray;margin-top: 0.5em;margin-left: 0.5em} QGroupBox::title {subcontrol-origin: margin;left: 10px;padding: 0 3px 0 3px;}")
        self.backButton = QPushButton("back",self)
        vbox = QVBoxLayout()
        hbox1 = QHBoxLayout()
        hbox2 = QHBoxLayout()
        hbox3 = QHBoxLayout()
        hbox4 = QHBoxLayout()
        hbox5 = QHBoxLayout()
        
        vButtonL = QPushButton("<",self)
        vButtonR = QPushButton(">",self)
        bButtonL = QPushButton("<",self)
        bButtonR = QPushButton(">",self)
        
        self.leftButton = QPushButton("Left",self)
        self.rightButton = QPushButton("Right",self)
        self.upButton = QPushButton("Up",self)
        self.downButton = QPushButton("Down",self)
        self.menuButton = QPushButton("Menu",self)
        self.modeButton = QPushButton("Mode",self)
        self.okButton = QPushButton("OK",self)
        self.powerButton = QPushButton("Power",self)
        self.sourceButton = QPushButton("Source",self)

        #CONNECT THE BUTTONS

        self.backButton.clicked.connect(self.backConnect)
        vButtonL.clicked.connect(self.vMinus)
        vButtonR.clicked.connect(self.vPlus)
        bButtonL.clicked.connect(self.bMinus)
        bButtonR.clicked.connect(self.bPlus)
        self.leftButton.clicked.connect(self.KEY_LEFT)
        self.rightButton.clicked.connect(self.KEY_RIGHT)
        self.upButton.clicked.connect(self.KEY_UP)
        self.downButton.clicked.connect(self.KEY_DOWN)
        self.menuButton.clicked.connect(self.KEY_MENU)
        self.modeButton.clicked.connect(self.KEY_MODE)
        self.okButton.clicked.connect(self.KEY_OK)
        self.powerButton.clicked.connect(self.KEY_POWER)
        self.sourceButton.clicked.connect(self.KEY_SOURCE)
        
        #SET BUTTONS LOCATION
        hbox1.addWidget(vButtonL)
        hbox1.addWidget(self.versionLabel)
        hbox1.addWidget(vButtonR)
        vbox.addLayout(hbox1)
        
        hbox2.addWidget(bButtonL)
        hbox2.addWidget(self.brandLabel)
        hbox2.addWidget(bButtonR)
        vbox.addLayout(hbox2)

        hbox3.addWidget(self.menuButton)
        hbox3.addWidget(self.upButton)
        hbox3.addWidget(self.modeButton)
        vbox.addLayout(hbox3)

        hbox4.addWidget(self.leftButton)
        hbox4.addWidget(self.okButton)
        hbox4.addWidget(self.rightButton)
        vbox.addLayout(hbox4)

        hbox5.addWidget(self.powerButton)
        hbox5.addWidget(self.downButton)
        hbox5.addWidget(self.sourceButton)
        vbox.addLayout(hbox5)
        vbox.addWidget(self.backButton)
        
        self.ACGroupBox.setFixedSize(720,480)
        self.ACGroupBox.setLayout(vbox)
        
        self.layout_for_wids.addWidget(self.ACGroupBox)
        
    

    ###METHOD FOR BUTTONS

    def vMinus(self):
        if(self.version - 1 > 0):
            self.version -= 1
            self.versionLabel.setText(str(self.version))
            self.command = 'irsend SEND_ONCE '+self.type+'_'+self.brandArr[self.brand]+'_'+str(self.version)+' '
            self.hardwareRefresh()
    def vPlus(self):
            self.version += 1
            self.versionLabel.setText(str(self.version))
            self.command = 'irsend SEND_ONCE '+self.type+'_'+self.brandArr[self.brand]+'_'+str(self.version)+' '
            self.hardwareRefresh()
    def bMinus(self):
        if(self.brand - 1 >= 0):
            self.brand -= 1
            self.brandLabel.setText(self.brandArr[self.brand])
            self.command = 'irsend SEND_ONCE '+self.type+'_'+self.brandArr[self.brand]+'_'+str(self.version)+' '
            self.hardwareRefresh()
    def bPlus(self):
        if(self.brand + 1 < len(self.brandArr)):
            self.brand += 1
            self.brandLabel.setText(self.brandArr[self.brand])
            self.command = 'irsend SEND_ONCE '+self.type+'_'+self.brandArr[self.brand]+'_'+str(self.version)+' '
            self.hardwareRefresh()
    def KEY_RIGHT(self):
                print(self.command)
                os.system(self.command + 'KEY_RIGHT')

    def KEY_LEFT(self):
                os.system(self.command + 'KEY_LEFT')

    def KEY_MENU(self):
                os.system(self.command + 'KEY_MENU')
                
    def KEY_MODE(self):
                os.system(self.command + 'KEY_MODE')
                
    def KEY_OK(self):
                os.system(self.command + 'KEY_OK')
            
    def KEY_POWER(self):
                os.system(self.command + 'KEY_POWER')

    def KEY_SOURCE(self):
                os.system(self.command + 'KEY_POWER2')

    def KEY_UP(self):
                os.system(self.command + 'KEY_UP')

    def KEY_DOWN(self):
                os.system(self.command + 'KEY_DOWN')

    def hardwareRefresh(self):
        ###reset ir data and change to another one
        os.system("sudo cp /home/pi/"+self.type+'_'+self.brandArr[self.brand]+'_'+str(self.version)+" /etc/lirc/lircd.conf")
        os.system("sudo /etc/init.d/lirc restart")
        os.system("sudo lircd --device /dev/lirc0")
        print(self.type+'_'+self.brandArr[self.brand]+'_'+str(self.version))
    
    def airconConnect(self):
        self.leftButton.setText("fanDOWN")
        self.rightButton.setText("fanUP")
        self.upButton.setText("tempUP")
        self.downButton.setText("tempDOWN")
        self.brandArr = ["Samsung","Lg","Haier","Panasonic","Hitachi"]
        self.type = "AirConditioner"
        self.ACGroupBox.setTitle(self.type+" Remote")
        self.okButton.setDisabled(True)
        self.menuButton.setDisabled(True)
        self.sourceButton.setDisabled(True)
        self.brand = 0
        self.version = 1
        self.command = 'irsend SEND_ONCE '+self.type+'_'+self.brandArr[self.brand]+'_'+str(self.version)+' '
        self.horizontalGroupBox.hide()
        self.hardwareRefresh()
        self.ACGroupBox.show()
        
        
        
    def projectorConnect(self):
        self.leftButton.setText("LEFT")
        self.rightButton.setText("RIGHT")
        self.upButton.setText("UP")
        self.downButton.setText("DOWN")
        self.brandArr = ["Samsung","Benq","Optoma","Sharp","Sony"]
        self.type = "Projector"
        self.ACGroupBox.setTitle(self.type+" Remote")
        self.brand = 0
        self.version = 1
        self.command = 'irsend SEND_ONCE '+self.type+'_'+self.brandArr[self.brand]+'_'+str(self.version)+' '
        self.horizontalGroupBox.hide()
        self.hardwareRefresh()
        self.ACGroupBox.show()
        
    def tvConnect(self):
        self.leftButton.setText("volumeDOWN")
        self.rightButton.setText("volumeUP")
        self.upButton.setText("channelUP")
        self.downButton.setText("channelDOWN")
        self.brandArr = ["Samsung","Sony","Panasonic","Lg","Philips"]
        self.type = "Television"
        self.ACGroupBox.setTitle(self.type+" Remote")
        
        self.brand = 0
        self.version = 1
        self.command = 'irsend SEND_ONCE '+self.type+'_'+self.brandArr[self.brand]+'_'+str(self.version)+' '
        self.horizontalGroupBox.hide()
        self.hardwareRefresh()
        self.ACGroupBox.show()
        print("tv")
        
    def camConnect(self):
        self.horizontalGroupBox.hide()
        self.CAMGroupBox.show()

    def openFolder(self):
        print("explorer "+self.dest)
        subprocess.call("explorer "+self.dest, shell=True)

    def streamConnect(self):
        self.CAMGroupBox.hide()
        self.strGroupBox.show()

    def streamBackConnect(self):
        self.strGroupBox.hide()
        self.CAMGroupBox.show()
    
    def backConnect(self):
        self.versionLabel.setText("1")
        self.brandLabel.setText(self.brandArr[0])
        self.CAMGroupBox.hide()
        self.ACGroupBox.hide()
        self.horizontalGroupBox.show()




def exitHandler():
    room_core.isOn = False
    camera_core.isOn = False
    
app = QApplication(sys.argv)

wizard = mainPage()
wizard.setWindowTitle('ROOM remote controller')
app.aboutToQuit.connect(exitHandler)

wizard.show()

app.exec_()
