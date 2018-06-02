import sys,os
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import *
import resource
import IR_signal

class Window(QMainWindow):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)
        self.setFixedSize(720, 480)
        self.move(100,100)
        self.setWindowTitle("ROOM remote control")
        
        self.mainPage = mainPage(self)
        self.acPage = acPage(self)
        self.pjPage = pjPage(self)
        self.tvPage = tvPage(self)

        #CENTRAL WIDGET
        self.central_wid = QWidget()
        self.layout_for_wids = QStackedLayout()

        #CONNECT THE BUTTONS
        
        
        #INIT PAGES
        self.layout_for_wids.addWidget(self.mainPage)
        self.layout_for_wids.addWidget(self.acPage)
        self.layout_for_wids.addWidget(self.pjPage)
        self.layout_for_wids.addWidget(self.tvPage)

        #SET CENTRAL WIDGET
        self.central_wid.setLayout(self.layout_for_wids)
        self.setCentralWidget(self.central_wid)

        
class mainPage(QGroupBox):
    def __init__(self,coreUI):
        super().__init__("Select your device")
        self.coreUI = coreUI
                                               
        self.setFixedSize(720, 480)
        #INIT MAINPAGE BUTTONS
        
        self.ACbutton = QPushButton("",self)
        self.PJbutton = QPushButton("",self)
        self.TVbutton = QPushButton("",self)
        self.STbutton = QPushButton("",self)
        self.ACbutton.setStyleSheet("border-image: url(:/icon/aircon.png);min-height: 150px;max-width: 150px")
        self.PJbutton.setStyleSheet("border-image: url(:/icon/projector.png);min-height: 150px;max-width: 150px")
        self.TVbutton.setStyleSheet("border-image: url(:/icon/tv.png);min-height: 150px;max-width: 150px")
        self.STbutton.setStyleSheet("border-image: url(:/icon/cam.png);min-height: 150px;max-width: 150px")
        
        self.ACbutton.clicked.connect(self.ACconnect)
        self.PJbutton.clicked.connect(self.PJconnect)
        self.TVbutton.clicked.connect(self.TVconnect)
        self.STbutton.clicked.connect(self.STconnect)
        
        self.vbox = QVBoxLayout()
        self.hbox1 = QHBoxLayout()
        self.hbox2 = QHBoxLayout()

        self.hbox1.addWidget(self.ACbutton)
        self.hbox1.addWidget(self.PJbutton)
        self.vbox.addLayout(self.hbox1)
        self.hbox2.addWidget(self.TVbutton)
        self.hbox2.addWidget(self.STbutton)  

        self.vbox.addLayout(self.hbox2)
        self.setLayout(self.vbox)
    def ACconnect(self):
        self.hide()
        self.coreUI.acPage.show()
        print("AC")
    def PJconnect(self):
        self.hide()
        self.coreUI.pjPage.show()
        print("PJ")
    def TVconnect(self):
        self.hide()
        self.coreUI.tvPage.show()
        print("TV")
    def STconnect(self):
        print("ST")

class acPage(QGroupBox):
    def __init__(self,coreUI):
        super().__init__("Airconditioner")
        self.coreUI = coreUI
##        self.signal = IR_signal.Signal()
        self.setFixedSize(720, 480)

        self.version = 1
        self.brand = 1
        self.brandArray = ["Samsung","Lg","Haier","Panasonic","Hitachi"]
        self.brandLabel = QLabel(" Test ")
        self.versionLabel = QLabel("1")
        self.brandLabel.setAlignment(Qt.AlignCenter)
        self.versionLabel.setAlignment(Qt.AlignCenter)
                               
        self.backButton = QPushButton("back",self)
        self.leftButton = QPushButton("Left",self)
        self.rightButton = QPushButton("Right",self)
        self.upButton = QPushButton("Up",self)
        self.downButton = QPushButton("Down",self)
        self.menuButton = QPushButton("Menu",self)
        self.modeButton = QPushButton("Mode",self)
        self.okButton = QPushButton("OK",self)
        self.powerButton = QPushButton("Power",self)
        self.sourceButton = QPushButton("Source",self)

        self.vButtonL = QPushButton("<",self)
        self.vButtonR = QPushButton(">",self)
        self.bButtonL = QPushButton("<",self)
        self.bButtonR = QPushButton(">",self)
        
        self.vbox = QVBoxLayout()
        self.hbox1 = QHBoxLayout()
        self.hbox2 = QHBoxLayout()
        self.hbox3 = QHBoxLayout()
        self.hbox4 = QHBoxLayout()
        self.hbox5 = QHBoxLayout()
        
        #CONNECT THE BUTTONS

        self.backButton.clicked.connect(self.backConnect)
##        self.vButtonL.clicked.connect(self.vMinus)
##        self.vButtonR.clicked.connect(self.vPlus)
##        self.bButtonL.clicked.connect(self.bMinus)
##        self.bButtonR.clicked.connect(self.bPlus)
        
        #SET BUTTONS LOCATION
        self.hbox1.addWidget(self.vButtonL)
        self.hbox1.addWidget(self.versionLabel)
        self.hbox1.addWidget(self.vButtonR)
        self.vbox.addLayout(self.hbox1)
        
        self.hbox2.addWidget(self.bButtonL)
        self.hbox2.addWidget(self.brandLabel)
        self.hbox2.addWidget(self.bButtonR)
        self.vbox.addLayout(self.hbox2)

        self.hbox3.addWidget(self.menuButton)
        self.hbox3.addWidget(self.upButton)
        self.hbox3.addWidget(self.modeButton)
        self.vbox.addLayout(self.hbox3)

        self.hbox4.addWidget(self.leftButton)
        self.hbox4.addWidget(self.okButton)
        self.hbox4.addWidget(self.rightButton)
        self.vbox.addLayout(self.hbox4)

        self.hbox5.addWidget(self.powerButton)
        self.hbox5.addWidget(self.downButton)
        self.hbox5.addWidget(self.sourceButton)
        self.vbox.addLayout(self.hbox5)
        self.vbox.addWidget(self.backButton)
        
        self.setLayout(self.vbox)
        
    def backConnect(self):
        self.hide()
        self.coreUI.mainPage.show()


class pjPage(QGroupBox):
    def __init__(self,coreUI):
        super().__init__("Projector")
        self.coreUI = coreUI
        self.setFixedSize(720, 480)

        self.version = 1
        self.brand = 1
        self.brandArray = ["Samsung","Lg","Benq","Panasonic","Sony"]
        self.brandLabel = QLabel(" Test ")
        self.versionLabel = QLabel("1")
        self.brandLabel.setAlignment(Qt.AlignCenter)
        self.versionLabel.setAlignment(Qt.AlignCenter)
                               
        self.backButton = QPushButton("back",self)
        self.leftButton = QPushButton("Left",self)
        self.rightButton = QPushButton("Right",self)
        self.upButton = QPushButton("Up",self)
        self.downButton = QPushButton("Down",self)
        self.menuButton = QPushButton("Menu",self)
        self.modeButton = QPushButton("Mode",self)
        self.okButton = QPushButton("OK",self)
        self.powerButton = QPushButton("Power",self)
        self.sourceButton = QPushButton("Source",self)

        self.vButtonL = QPushButton("<",self)
        self.vButtonR = QPushButton(">",self)
        self.bButtonL = QPushButton("<",self)
        self.bButtonR = QPushButton(">",self)
        
        self.vbox = QVBoxLayout()
        self.hbox1 = QHBoxLayout()
        self.hbox2 = QHBoxLayout()
        self.hbox3 = QHBoxLayout()
        self.hbox4 = QHBoxLayout()
        self.hbox5 = QHBoxLayout()
        
        #CONNECT THE BUTTONS

        self.backButton.clicked.connect(self.backConnect)
##        self.vButtonL.clicked.connect(self.vMinus)
##        self.vButtonR.clicked.connect(self.vPlus)
##        self.bButtonL.clicked.connect(self.bMinus)
##        self.bButtonR.clicked.connect(self.bPlus)
        
        #SET BUTTONS LOCATION
        self.hbox1.addWidget(self.vButtonL)
        self.hbox1.addWidget(self.versionLabel)
        self.hbox1.addWidget(self.vButtonR)
        self.vbox.addLayout(self.hbox1)
        
        self.hbox2.addWidget(self.bButtonL)
        self.hbox2.addWidget(self.brandLabel)
        self.hbox2.addWidget(self.bButtonR)
        self.vbox.addLayout(self.hbox2)

        self.hbox3.addWidget(self.menuButton)
        self.hbox3.addWidget(self.upButton)
        self.hbox3.addWidget(self.modeButton)
        self.vbox.addLayout(self.hbox3)

        self.hbox4.addWidget(self.leftButton)
        self.hbox4.addWidget(self.okButton)
        self.hbox4.addWidget(self.rightButton)
        self.vbox.addLayout(self.hbox4)

        self.hbox5.addWidget(self.powerButton)
        self.hbox5.addWidget(self.downButton)
        self.hbox5.addWidget(self.sourceButton)
        self.vbox.addLayout(self.hbox5)
        self.vbox.addWidget(self.backButton)
        
        self.setLayout(self.vbox)
        
    def backConnect(self):
        self.hide()
        self.coreUI.mainPage.show()
##    def vMinus(self):
##        if(self.version - 1 > 0):
##            self.version -= 1
##            self.versionLabel.setText(str(self.version))
##            self.blaster.command = 'irsend SEND_ONCE '+self.type+'_'+self.brandArr[self.brand]+'_'+str(self.version)+' '
##            print(self.blaster.command)
##    def vPlus(self):
##            self.version += 1
##            self.versionLabel.setText(str(self.version))
##            self.blaster.command = 'irsend SEND_ONCE '+self.type+'_'+self.brandArr[self.brand]+'_'+str(self.version)+' '
##    def bMinus(self):
##        if(self.brand - 1 >= 0):
##            self.brand -= 1
##            self.brandLabel.setText(self.brandArr[self.brand])
##            self.blaster.command = 'irsend SEND_ONCE '+self.type+'_'+self.brandArr[self.brand]+'_'+str(self.version)+' '
##    def bPlus(self):
##        if(self.brand + 1 < len(self.brandArr)):
##            self.brand += 1
##            self.brandLabel.setText(self.brandArr[self.brand])
##            self.blaster.command = 'irsend SEND_ONCE '+self.type+'_'+self.brandArr[self.brand]+'_'+str(self.version)+' '
##

class tvPage(QGroupBox):
    def __init__(self,coreUI):
        super().__init__("Television")
        self.coreUI = coreUI
##        self.signal = IR_signal.Signal()
        self.setFixedSize(720, 480)

        self.version = 1
        self.brand = 1
        self.brandArray = ["Samsung","Lg","Haier","Panasonic","Hitachi"]
        self.brandLabel = QLabel(" Test ")
        self.versionLabel = QLabel("1")
        self.brandLabel.setAlignment(Qt.AlignCenter)
        self.versionLabel.setAlignment(Qt.AlignCenter)
                               
        self.backButton = QPushButton("back",self)
        self.leftButton = QPushButton("Left",self)
        self.rightButton = QPushButton("Right",self)
        self.upButton = QPushButton("Up",self)
        self.downButton = QPushButton("Down",self)
        self.menuButton = QPushButton("Menu",self)
        self.modeButton = QPushButton("Mode",self)
        self.okButton = QPushButton("OK",self)
        self.powerButton = QPushButton("Power",self)
        self.sourceButton = QPushButton("Source",self)

        self.vButtonL = QPushButton("<",self)
        self.vButtonR = QPushButton(">",self)
        self.bButtonL = QPushButton("<",self)
        self.bButtonR = QPushButton(">",self)
        
        self.vbox = QVBoxLayout()
        self.hbox1 = QHBoxLayout()
        self.hbox2 = QHBoxLayout()
        self.hbox3 = QHBoxLayout()
        self.hbox4 = QHBoxLayout()
        self.hbox5 = QHBoxLayout()
        
        #CONNECT THE BUTTONS

        self.backButton.clicked.connect(self.backConnect)
##        self.vButtonL.clicked.connect(self.vMinus)
##        self.vButtonR.clicked.connect(self.vPlus)
##        self.bButtonL.clicked.connect(self.bMinus)
##        self.bButtonR.clicked.connect(self.bPlus)
        
        #SET BUTTONS LOCATION
        self.hbox1.addWidget(self.vButtonL)
        self.hbox1.addWidget(self.versionLabel)
        self.hbox1.addWidget(self.vButtonR)
        self.vbox.addLayout(self.hbox1)
        
        self.hbox2.addWidget(self.bButtonL)
        self.hbox2.addWidget(self.brandLabel)
        self.hbox2.addWidget(self.bButtonR)
        self.vbox.addLayout(self.hbox2)

        self.hbox3.addWidget(self.menuButton)
        self.hbox3.addWidget(self.upButton)
        self.hbox3.addWidget(self.modeButton)
        self.vbox.addLayout(self.hbox3)

        self.hbox4.addWidget(self.leftButton)
        self.hbox4.addWidget(self.okButton)
        self.hbox4.addWidget(self.rightButton)
        self.vbox.addLayout(self.hbox4)

        self.hbox5.addWidget(self.powerButton)
        self.hbox5.addWidget(self.downButton)
        self.hbox5.addWidget(self.sourceButton)
        self.vbox.addLayout(self.hbox5)
        self.vbox.addWidget(self.backButton)
        
        self.setLayout(self.vbox)
        
    def backConnect(self):
        self.hide()
        self.coreUI.mainPage.show()
app = QApplication(sys.argv)

win = Window()
win.show()
app.exec_()
