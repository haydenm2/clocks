import sys
from datetime import datetime
import time as t

class Feature():
    # Initialization function
    def __init__(self):
        print("Must Initialize Feature in Inheriting Class")
        pass

    #Set Feature Name
    def SetName(self,name):
        self.Name = name

    #Toggle Print Output
    def SetShow(self):
        if(not(self.Show)):
            self.Show = True
        else:
            self.Show = False
    
    #Set Feature Value (if applicable)
    def SetValue(self,Value):
        pass

    #Execution Loop
    def Execute(self):
        while(not(self.cDest)):
            if(self.On):
                self.CheckFlags()
                if(self.Show):
                    self.Print(self.preprintmsg+self.Name,self.PrintTime)
                self.Update()
            else:
                self.CheckFlags()

    #Variable Updates
    def Update(self):
        self.Time = [datetime.now().hour,datetime.now().minute,datetime.now().second,datetime.now().microsecond]
        self.PrintTime = self.Time

    #Print Output
    def Print(self,Name,Time):
        print('\033[1m\033[92m','[',Name,']: ','\033[0m',Time[0],':',Time[1],':',Time[2],':',Time[3],end='\r')
        sys.stdout.flush()

    #Check for Interrupt Flags
    def CheckFlags(self):
        if(self.cReset):
            self.Reset()
            self.cReset = False
        if(self.cStart):
            self.Activate()
            self.cStart = False
        t.sleep(self.ShowInt)
 
    #Subtract Two Time Arrays
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

    #Activate Feature
    def Activate(self):
        self.On = True
        self.Time = [datetime.now().hour,datetime.now().minute,datetime.now().second,datetime.now().microsecond]

    #Reset Feature
    def Reset(self):
        self.__init__()

    #Feature Destructor
    def __del__(self):
        print('\n\033[1m\033[91m','[',self.Name,']: ',self.killmsg,'\033[0m')
        return
    
    
