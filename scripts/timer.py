# This class instantiates an alarm object that can be set, named, checked, and destroyed.
from datetime import datetime
import time as t
from feature import Feature

class Timer(Feature):
    # Initialization function
    def __init__(self):
        self.Name = 'Timer' #timer name
        self.On = False #state of timer object
        self.Time = [0,0,0,0] #[hour,minute,second,microseconds] current time
        self.Diff = [0,0,0,0] #[hour,minute,second,microseconds] time until finish
        self.Finish = [0,0,0,0] #[hour,minute,second,microseconds] time of finish
        self.Length = [0,0,0,0] #[hour,minute,second,microseconds] length of timer
        self.PrintTime = [0,0,0,0] #[hour,minute,second,microseconds]
        self.cReset = False #reset command flag
        self.cPause = False #pause command flag
        self.cStart = True #start command flag
        self.cDest = False #destructor command flag
        self.Show = True #show timer output flag
        self.ShowInt = 0.05 #display interval
        self.preprintmsg = ""
        self.endmsg = "Timer Passed"
        self.killmsg = "Deleting Timer"

    def SetValue(self,Value):
        self.Length = Value
            
    def Update(self):
        self.Time = [datetime.now().hour,datetime.now().minute,datetime.now().second,datetime.now().microsecond]
        self.Diff = self.SubTime(self.Finish,self.Time)
        self.PrintTime = self.Diff

    def CheckFlags(self):
        if(self.cPause):
            self.Pause()
            self.cPause = False
        if(self.cReset):
            self.Reset()
            self.cReset = False
        if(self.cStart):
            self.Activate()
            self.cStart = False
        t.sleep(self.ShowInt)

    def AddTime(self,Time1,Time2):
        Add = [Time1[0]+Time2[0],Time1[1]+Time2[1],Time1[2]+Time2[2],Time1[3]+Time2[3]]
        if(Add[3]>1000000):
            Add[3]=Add[3]%1000000
            Add[2]=Add[2]+(Add[3]//1000000)
        if(Add[2]>60):
            Add[2]=Add[2]%60
            Add[1]=Add[1]+(Add[1]//60)
        if(Add[1]>60):
            Add[1]=Add[1]%60
            Add[0]=Add[0]+(Add[0]//60)
        if(Add[0]>23):
            Add[0]=Add[0]%24
        return Add

    def Activate(self):
        self.On = True
        self.Time = [datetime.now().hour,datetime.now().minute,datetime.now().second,datetime.now().microsecond]
        self.Finish = self.AddTime(self.Time,self.Length)

    def Pause(self):
        self.Length=self.Diff
        self.On = False
    