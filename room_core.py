from firebase import firebase
import os
from time import sleep
import sys
firebase = firebase.FirebaseApplication('https://room-54314.firebaseio.com/')
RemoteData = firebase.get('/TempUnit/CurrentRemote',None)

isOn = True

class Device():
    #implementation
    def __init__(self):
        print("Initialize as "+str(type(self)))
        self.fetch()
        print("Complete")


    def fetch(self):
        ###Get data from firebase
        RemoteData = firebase.get('/TempUnit/CurrentRemote',None)
        self.DeviceProperty = RemoteData.get("Device")
        self.RemoteProperty = RemoteData.get("RemoteCount")
        
        self.Brand = self.DeviceProperty.get("Brand")
        self.Type = self.DeviceProperty.get("Type")
        self.Version = self.DeviceProperty.get("Version")

        self.Command = 'sudo irsend SEND_ONCE '+self.Type+'_'+self.Brand+'_'+str(self.Version)+' '

        self.Channel = self.RemoteProperty.get("Channel")
        self.Horizontal = self.RemoteProperty.get("Horizontal")
        self.Menu = self.RemoteProperty.get("Menu")
        self.Mode = self.RemoteProperty.get("Mode")
        self.OK = self.RemoteProperty.get("OK")
        self.Power = self.RemoteProperty.get("Power")
        self.Source = self.RemoteProperty.get("Source")
        self.Vertical = self.RemoteProperty.get("Vertical")
        
    def hardwareRefresh(self):
        ###reset ir data and change to another one
        os.system("sudo cp /home/pi/"+self.Type+'_'+self.Brand+'_'+str(self.Version)+" /etc/lirc/lircd.conf")
        os.system("sudo /etc/init.d/lirc restart")
        os.system("sudo lircd --device /dev/lirc0")

    ##button checker: send the infrared if more than 1 click
    def horizontalCheck(self):
        if(self.Horizontal > 0):
            for i in range (0,self.Horizontal):
                print("Right button pressed: " + self.Command + 'KEY_RIGHT')
                os.system(self.Command + 'KEY_RIGHT')
            firebase.put('TempUnit/CurrentRemote/RemoteCount','Horizontal',0)
        elif(self.Horizontal < 0):
            for i in range (self.Horizontal,0):
                print("Left button pressed: " + self.Command + 'KEY_LEFT')
                os.system(self.Command + 'KEY_LEFT')
            firebase.put('TempUnit/CurrentRemote/RemoteCount','Horizontal',0)
        
    def menuCheck(self):
        if(self.Menu > 0):
            for i in range (0,self.Menu):
                print("Menu button pressed: " + self.Command + 'KEY_MENU')
                os.system(self.Command + 'KEY_MENU')
            firebase.put('TempUnit/CurrentRemote/RemoteCount','Menu',0)
        
    def modeCheck(self):
        if(self.Mode > 0):
            for i in range (0,self.Mode):
                print("Mode button pressed: " + self.Command + 'KEY_MODE')
                os.system(self.Command + 'KEY_MODE')
            firebase.put('TempUnit/CurrentRemote/RemoteCount','Mode',0)

    def okCheck(self):
        if(self.OK > 0):
            for i in range (0,self.OK):
                print("OK button pressed: " + self.Command + 'KEY_OK')
                os.system(self.Command + 'KEY_OK')
            firebase.put('TempUnit/CurrentRemote/RemoteCount','OK',0)

    def powerCheck(self):
        if(self.Power > 0):
            for i in range (0,self.Power):
                print("OK button pressed: " + self.Command + 'KEY_POWER')
                os.system(self.Command + 'KEY_POWER')
            firebase.put('TempUnit/CurrentRemote/RemoteCount','Power',0)

    def sourceCheck(self):
        if(self.Power > 0):
            for i in range (0,self.Source):
                print("OK button pressed: " + self.Command + 'KEY_SOURCE')
                os.system(self.Command + 'KEY_SOURCE')
            firebase.put('TempUnit/CurrentRemote/RemoteCount','Source',0)

    def verticalCheck(self):
        if(self.Vertical > 0):
            for i in range (0,self.Vertical):
                print("Up button pressed: " + self.Command + 'KEY_UP')
                os.system(self.Command + 'KEY_UP')
            firebase.put('TempUnit/CurrentRemote/RemoteCount','Vertical',0)
        elif(self.Vertical < 0):
            for i in range (self.Vertical,0):
                print("Down button pressed: " + self.Command + 'KEY_DOWN')
                os.system(self.Command + 'KEY_DOWN')
            firebase.put('TempUnit/CurrentRemote/RemoteCount','Vertical',0)

    #check all button, if fail(no internet) keep retry
    def activeCheck(self):
        try:
            self.fetch()
            self.horizontalCheck()
            self.menuCheck()
            self.modeCheck()
            self.okCheck()
            self.powerCheck()
            self.sourceCheck()
            self.verticalCheck()
        except:
            print("Connection Error : restarting")
            self.activeCheck()

class Projector(Device):
    def __init__(self):
        super().__init__()
    def fetch(self):
        super().fetch()
    def hardwareRefresh(self):
        super().hardwareRefresh()
    def horizontalCheck(self):
        super().horizontalCheck()
    def menuCheck(self):
        super().menuCheck()
    def modeCheck(self):
        super().modeCheck()
    def okCheck(self):
        super().okCheck()
    def powerCheck(self):
        super().powerCheck()
    def sourceCheck(self):
        super().sourceCheck()
    def verticalCheck(self):
        super().verticalCheck()
    def activeCheck(self):
        super().activeCheck()

class Television(Device):
    def __init__(self):
        super().__init__()
    def fetch(self):
        super().fetch()
    def hardwareRefresh(self):
        super().hardwareRefresh()
    def horizontalCheck(self):
        ###override the horizontal for making volumeup/down button
        if(self.Horizontal > 0):
            for i in range (0,self.Horizontal):
                print("Right button pressed: " + self.Command + 'KEY_VOLUMEUP')
                os.system(self.Command + 'KEY_VOLUMEUP')
            firebase.put('TempUnit/CurrentRemote/RemoteCount','Horizontal',0)
        elif(self.Horizontal < 0):
            for i in range (self.Horizontal,0):
                print("Left button pressed: " + self.Command + 'KEY_VOLUMEDOWN')
                os.system(self.Command + 'KEY_VOLUMEDOWN')
            firebase.put('TempUnit/CurrentRemote/RemoteCount','Horizontal',0)        
    def menuCheck(self):
        super().menuCheck()
    def modeCheck(self):
        super().modeCheck()
    def okCheck(self):
        super().okCheck()
    def powerCheck(self):
        super().powerCheck()
    def sourceCheck(self):
        super().sourceCheck()
    def verticalCheck(self):
        ###override the vertical for making channel up/down button
        if(self.Vertical > 0):
            for i in range (0,self.Vertical):
                print("Up button pressed: " + self.Command + 'KEY_CHANNELUP')
                os.system(self.Command + 'KEY_CHANNELUP')
            firebase.put('TempUnit/CurrentRemote/RemoteCount','Vertical',0)
        elif(self.Vertical < 0):
            for i in range (self.Vertical,0):
                print("Down button pressed: " + self.Command + 'KEY_CHANNELDOWN')
                os.system(self.Command + 'KEY_CHANNELDOWN')
            firebase.put('TempUnit/CurrentRemote/RemoteCount','Vertical',0)
    def activeCheck(self):
        super().activeCheck()

class AirConditioner(Device):
    def __init__(self):
        super().__init__()
    def fetch(self):
        super().fetch()
    def hardwareRefresh(self):
        super().hardwareRefresh()
    def horizontalCheck(self):
        super().horizontalCheck()
    def menuCheck(self):
        super().menuCheck()
    def modeCheck(self):
        super().modeCheck()
    def okCheck(self):
        super().okCheck()
    def powerCheck(self):
        super().powerCheck()
    def sourceCheck(self):
        super().sourceCheck()
    def verticalCheck(self):
        super().verticalCheck()
    def activeCheck(self):
        super().activeCheck()

def programLoop():
    ###mutate the object class if their type from database is not same as their class
    remote = Device()
    i = 0
    while(isOn == True):
        if((type(remote) is not Projector) and remote.Type == "Projector"):
            remote = Projector()
        if((type(remote) is not Television) and remote.Type == "Television"):
            remote = Television()
        if((type(remote) is not AirConditioner) and remote.Type == "AirConditioner"):
            remote = AirConditioner()
        remote.activeCheck()
        print("Clock: " + str(i))
        i+=1
        sleep(5)
    print("core exit")
    sys.exit()
