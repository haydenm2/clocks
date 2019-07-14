# This class instantiates an alarm object that can be set, named, checked, and destroyed.
# from __future__ import print_function
import sys
from datetime import time, datetime
import time as t

class Alarm:
    # Initialization function
    def __init__(self):
        self.Name = 'Alarm' #alarm name
        self.Time = [0,0,0,0] #[hour,minute,second,microseconds]
        self.Alarm = [0,0,0,0] #[hour,minute,second,microseconds]
        self.Diff = [0,0,0,0] #time until [hour,minute,second,microseconds]
        self.cReset = False #reset command flag
        self.cDest = False #destructor command flag
        self.Show = True #show timer output flag
        self.ShowInt = 0.05 #display interval

    # Setter Functions
    def SetName(self,name):
        self.Name = name
    
    def SetShow(self):
        if(not(self.Show)):
            self.Show = True
        else:
            self.Show = False

    def SetValue(self,Value):
        self.Alarm = [Value[0],Value[1],Value[2],Value[3]]

    #Execution Functions
    def Execute(self):
        while(not(self.cDest)):
            self.CheckFlags()
            if(self.Show):
                self.Print("Time to "+self.Name,self.Diff)
            self.Update()
        
    def Update(self):
        self.Time = [datetime.now().hour,datetime.now().minute,datetime.now().second,datetime.now().microsecond]
        self.Diff = self.SubTime(self.Alarm,self.Time)

    def Print(self,Name,Time):
            print('[',Name,']: ',Time[0],':',Time[1],':',Time[2],':',Time[3],end='\r')
            sys.stdout.flush()

    def CheckFlags(self):
        if(self.cReset):
            self.Reset()
            self.cReset = False
        t.sleep(self.ShowInt)

    def SubTime(self,Time1,Time2):
        Sub = [Time1[0]-Time2[0],Time1[1]-Time2[1],Time1[2]-Time2[2],Time1[3]-Time2[3]]
        if(Sub[3]<0):
            Sub[2]-=1
            Sub[3]+=1000000
        if(Sub[2]<0):
            Sub[1]-=-(Sub[2]//60)
            Sub[2]+=60*-(Sub[2]//60)
        if(Sub[1]<0):
            Sub[0]-=-(Sub[1]//60)
            Sub[1]+=60*-(Sub[1]//60)
        if(Sub[0]<0):
            Sub=[0,0,0,0]
            print('[',self.Name,']: ','Alarm Passed')
            self.cReset = True
        return Sub

    def Reset(self):
        self.Name = 'Alarm' #alarm name
        self.Time = [0,0,0,0] #[hour,minute,second,microseconds]
        self.Alarm = [0,0,0,0] #[hour,minute,second,microseconds]
        self.Diff = [0,0,0,0] #time until [hour,minute,second,microseconds]
        self.cReset = False #reset command flag
        self.cDest = False #destructor command flag
        self.Show = True #show timer output flag
        return
    
    # Destructor
    def __del__(self):
        print('[',self.Name,']: ','Deleting Alarm')
        return
    
    