from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import *
import sys,os

class acSignal():
    def __init__(self):
        self.command = " "

    def hardwareRefresh(self,Type,Brand,Version):
        os.system("sudo cp /home/pi/"+self.type+'_'+self.brandArr[self.brand]+'_'+str(self.version)+" /etc/lirc/lircd.conf")
        os.system("sudo /etc/init.d/lirc restart")
        os.system("sudo lircd --device /dev/lirc0")

    def KEY_RIGHT(self):
        self.file = open("log.txt","a+")
        os.system(self.command + 'KEY_RIGHT')
        self.file.write(self.command + 'KEY_RIGHT\n')
        self.file.close()

    def KEY_LEFT(self):
                self.file = open("log.txt","a+")
                os.system(self.command + 'KEY_LEFT')
                self.file.write(self.command + 'KEY_LEFT\n')
                self.file.close()

    def KEY_MENU(self):
                self.file = open("log.txt","a+")
                os.system(self.command + 'KEY_MENU')
                self.file.write(self.command + 'KEY_MENU\n')
                self.file.close()
                
    def KEY_MODE(self):
                self.file = open("log.txt","a+")
                os.system(self.command + 'KEY_MODE')
                self.file.write(self.command + 'KEY_MODE\n')
                self.file.close()
                
    def KEY_OK(self):
                self.file = open("log.txt","a+")
                os.system(self.command + 'KEY_OK')
                self.file.write(self.command + 'KEY_OK\n')
                self.file.close()
            
    def KEY_POWER(self):
                self.file = open("log.txt","a+")
                os.system(self.command + 'KEY_POWER')
                self.file.write(self.command + 'KEY_POWER\n')
                self.file.close()

    def KEY_SOURCE(self):
                self.file = open("log.txt","a+")
                os.system(self.command + 'KEY_SOURCE')
                self.file.write(self.command + 'KEY_SOURCE\n')
                self.file.close()

    def KEY_UP(self):
                self.file = open("log.txt","a+")
                os.system(self.command + 'KEY_UP')
                self.file.write(self.command + 'KEY_UP\n')
                self.file.close()

    def KEY_DOWN(self):
                self.file = open("log.txt","a+")
                os.system(self.command + 'KEY_DOWN')
                self.file.write(self.command + 'KEY_DOWN\n')
                self.file.close()

