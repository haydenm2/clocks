# This class instantiates an alarm object that can be set, named, checked, and destroyed.
# from __future__ import print_function
import sys
from datetime import time, datetime
import time as t

class Stopwatch:
    # Initialization function
    def __init__(self):
        self.Name = 'Stopwatch' #timer name
        self.On = False #state of timer object
        self.Time = [0,0,0,0] #[hour,minute,second,microseconds] current time
        self.Start = [0,0,0,0] #[hour,minute,second,microseconds] start time
        self.Elapsed = [0,0,0,0] #[hour,minute,second,microseconds] elapsed time
        self.Laps = [] #lap data structure
        self.cReset = False #reset command flag
        self.cPause = False #pause command flag
        self.cStart = False #start command flag
        self.cDest = False #destructor command flag
        self.cLap = False #lap command flag
        self.Show = True #show timer output flag
        self.LapCount = 1 #Lap iterator

    #Setter Functions
    def SetName(self,name):
        self.Name = name

    def SetShow(self):
        if(not(self.Show)):
            self.Show = True
        else:
            self.Show = False

    #Execution Functions
    def Execute(self):
        while(not(self.cDest)):
            if(self.On):
                self.CheckFlags()
                if(self.Show):
                    self.Print(self.Name,self.Elapsed)
                self.Update()
            else:
                self.CheckFlags()
            
    def Update(self):
        self.Time = [datetime.now().hour,datetime.now().minute,datetime.now().second,datetime.now().microsecond]
        self.Elapsed = self.SubTime(self.Time,self.Start)

    def Print(self,Name,Elapsed):
            print('[',Name,']: ',Elapsed[0],':',Elapsed[1],':',Elapsed[2],':',Elapsed[3],end='\r')
            sys.stdout.flush()

    def CheckFlags(self):
        if(self.cLap):
            self.Lap()
            self.cLap = False
        if(self.cStart):
            self.Play()
            self.cStart = False
        if(self.cPause):
            self.Pause()
            self.cPause = False
        if(self.cReset):
            self.Reset()
            self.cReset = False
        t.sleep(0.05)

    def SubTime(self,Time1,Time2):
        Sub = [Time1[0]-Time2[0],Time1[1]-Time2[1],Time1[2]-Time2[2],Time1[3]-Time2[3]]
        if(Sub[3]<0):
            Sub[2]-=1
            Sub[3]+=1000000
        if(Sub[2]<0):
            Sub[1]-=+(Sub[2]//60)+1
            Sub[2]+=60*(1+(Sub[2]//60))
        if(Sub[1]<0):
            Sub[0]-=+(Sub[1]//60)+1
            Sub[1]+=60*(1+(Sub[1]//60))
        if(Sub[0]<0):
            Sub=[0,0,0,0]
            print("TIME SUBTRACTION ERROR!")
            self.On = False
            self.cReset=True
        return Sub
    
    def AddTime(self,Time1,Time2):
        Add = [self.Time1[0]-self.Time2[0],self.Time1[1]-self.Time2[1],self.Time1[2]-self.Time2[2],self.Time1[3]-self.Time2[3]]
        if(self.Add[3]>1000000):
            self.Add[3]=self.Add[3]%1000000
            self.Add[2]=self.Add[2]+(self.Add[3]//1000000)
        if(self.Add[2]>60):
            self.Add[2]=self.Add[2]%60
            self.Add[1]=self.Add[1]+(self.Add[1]//60)
        if(self.Add[1]>60):
            self.Add[1]=self.Add[1]%60
            self.Add[0]=self.Add[0]+(self.Add[0]//60)
        # if(self.Add[0]>23):
        #     self.Add[0]=self.Add[0]%24
        return Add

    def Play(self):
        self.On = True
        self.Time = [datetime.now().hour,datetime.now().minute,datetime.now().second,datetime.now().microsecond]
        self.Start = self.SubTime(self.Time,self.Elapsed)

    def Pause(self):
        self.On = False

    def Lap(self):
        self.Laps.append(self.Elapsed) 
        
    def Reset(self):
        self.Name = 'Stopwatch' #timer name
        self.On = False #state of timer object
        self.Time = [0,0,0,0] #[hour,minute,second,microseconds] current time
        self.Start = [0,0,0,0] #[hour,minute,second,microseconds] start time
        self.Elapsed = [0,0,0,0] #[hour,minute,second,microseconds] elapsed time
        self.Laps = [] #lap data structure
        self.cReset = False #reset command flag
        self.cPause = False #pause command flag
        self.cStart = False #start command flag
        self.cDest = False #destructor command flag
        self.cLap = False #lap command flag
        self.Show = True #show timer output flag
        return

    def __del__(self):
        print('[',self.Name,']: ','Deleting Stopwatch')
        return
    
    