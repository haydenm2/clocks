# This class instantiates a clock object that can be checked, and destroyed.
# from __future__ import print_function
import sys
from datetime import time, datetime
import time as t

class Clock:
    # Initialization function
    def __init__(self):
        self.Name = 'Clock' #clock name
        self.On = False #state of clock object
        self.Time = [0,0,0,0] #[hour,minute,second,microseconds] current time
        self.cReset = False #reset command flag
        self.cStart = True #start command flag
        self.cDest = False #destructor command flag
        self.Show = True #show output flag
        self.ShowInt = 0.05 #display interval
        self.preprintmsg = ""
        self.endmsg = "Subtraction Error!"
        self.killmsg = "Deleting Clock"

    #Setter Functions
    def SetName(self,name):
        self.Name = name

    def SetShow(self):
        if(not(self.Show)):
            self.Show = True
        else:
            self.Show = False
    
    def SetValue(self,Value):
        pass

    #Execution Functions
    def Execute(self):
        while(not(self.cDest)):
            if(self.On):
                self.CheckFlags()
                if(self.Show):
                    self.Print(self.preprintmsg+self.Name,self.Time)
                self.Update()
            else:
                self.CheckFlags()

    def Update(self):
        self.Time = [datetime.now().hour,datetime.now().minute,datetime.now().second,datetime.now().microsecond]

    def Print(self,Name,Time):
        print('\033[1m\033[92m','[',Name,']: ','\033[0m',Time[0],':',Time[1],':',Time[2],':',Time[3],end='\r')
        sys.stdout.flush()

    def CheckFlags(self):
        if(self.cReset):
            self.Reset()
            self.cReset = False
        if(self.cStart):
            self.Activate()
            self.cStart = False
        t.sleep(self.ShowInt)

    #For Changing Time Zones  
    def SubTime(self,Time1,Time2):
        Sub = [Time1[0]-Time2[0],Time1[1]-Time2[1],Time1[2]-Time2[2],Time1[3]-Time2[3]]
        if(Sub[3]<0):
            Sub[2]-=1
            Sub[3]+=1000000
        if(Sub[2]<0):
            Sub[1]-=(2+(Sub[2]//60))
            Sub[2]+=60*(2+(Sub[2]//60))
        if(Sub[1]<0):
            Sub[0]-=(2+(Sub[1]//60))
            Sub[1]+=60*(2+(Sub[1]//60))
        if(Sub[0]<0):
            Sub=[0,0,0,0]
            print('\n\033[1m\033[94m','[',self.Name,']: ',self.endmsg,'\033[0m')
            self.On = False
        return Sub

    def Activate(self):
        self.On = True
        self.Time = [datetime.now().hour,datetime.now().minute,datetime.now().second,datetime.now().microsecond]

    def Reset(self):
        self.Name = 'Clock'
        self.On = False #state of clock object
        self.cReset = False #reset command flag
        self.cStart = True #start command flag
        self.Show = True #show output flag

    def __del__(self):
        print('\n\033[1m\033[91m','[',self.Name,']: ',self.killmsg,'\033[0m')
        return
    
    