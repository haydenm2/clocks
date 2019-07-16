# This class instantiates an alarm object that can be set, named, checked, and destroyed.
# from __future__ import print_function
import sys
from datetime import time, datetime
import time as t

class Alarm:
    # Initialization function
    def __init__(self):
        self.Name = 'Alarm' #alarm name
        self.On = False #state of alarm object
        self.Time = [0,0,0,0] #[hour,minute,second,microseconds]
        self.Finish = [0,0,0,0] #[hour,minute,second,microseconds]
        self.Diff = [0,0,0,0] #time until [hour,minute,second,microseconds]
        self.cReset = False #reset command flag
        self.cDest = False #destructor command flag
        self.Show = True #show timer output flag
        self._ShowInt = 0.05 #display interval
        self.preprintmsg = "Time to "
        self.endmsg = "Alarm Passed"
        self.killmsg = "Deleting Alarm"


    # Setter Functions
    def SetName(self,name):
        self.Name = name
    
    def SetShow(self):
        if(not(self.Show)):
            self.Show = True
        else:
            self.Show = False

    def SetValue(self,Value):
        self.Finish = [Value[0],Value[1],Value[2],Value[3]]

    #Execution Functions
    def Execute(self):
        while(not(self.cDest)):
            if(self.On):
                self.CheckFlags()
                if(self.Show):
                    self.Print(self.preprintmsg+self.Name,self.Diff)
                self.Update()
            else:
                self.CheckFlags()
        
    def Update(self):
        self.Time = [datetime.now().hour,datetime.now().minute,datetime.now().second,datetime.now().microsecond]
        self.Diff = self.SubTime(self.Finish,self.Time)

    def Print(self,Name,Time):
        print('\033[1m\033[92m','[',Name,']: ','\033[0m',Time[0],':',Time[1],':',Time[2],':',Time[3],end='\r')
        sys.stdout.flush()

    def CheckFlags(self):
        if(self.cReset):
            self.Reset()
            self.cReset = False
        t.sleep(self._ShowInt)

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
        self.Name = 'Alarm' #alarm name
        self.Finish = [0,0,0,0] #[hour,minute,second,microseconds]
        self.Diff = [0,0,0,0] #time until [hour,minute,second,microseconds]
        self.cReset = False #reset command flag
        self.Show = True #show output flag
        return
    
    def __del__(self):
        print('\n\033[1m\033[91m','[',self.Name,']: ',self.killmsg,'\033[0m')
        return
    
    