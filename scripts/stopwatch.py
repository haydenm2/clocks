# This class instantiates an alarm object that can be set, named, checked, and destroyed.
from datetime import datetime
import time as t
from feature import Feature

class Stopwatch(Feature):
    # Initialization function
    def __init__(self):
        self.Name = 'Stopwatch' #timer name
        self.On = False #state of timer object
        self.Time = [0,0,0,0] #[hour,minute,second,microseconds] current time
        self.Start = [0,0,0,0] #[hour,minute,second,microseconds] start time
        self.Elapsed = [0,0,0,0] #[hour,minute,second,microseconds] elapsed time
        self.PrintTime = [0,0,0,0] #[hour,minute,second,microseconds]
        self.Laps = [] #lap data structure
        self.cReset = False #reset command flag
        self.cPause = False #pause command flag
        self.cStart = False #start command flag
        self.cDest = False #destructor command flag
        self.cLap = False #lap command flag
        self.Show = True #show timer output flag
        self.ShowInt = 0.05 #display interval
        self.preprintmsg = ""
        self.endmsg = "Invalid Subtraction!"
        self.killmsg = "Deleting Stopwatch"
            
    def Update(self):
        self.Time = [datetime.now().hour,datetime.now().minute,datetime.now().second,datetime.now().microsecond]
        self.Elapsed = self.SubTime(self.Time,self.Start)
        self.PrintTime = self.Elapsed

    def CheckFlags(self):
        if(self.cLap):
            self.Lap()
            self.cLap = False
        if(self.cStart):
            self.Activate()
            self.cStart = False
        if(self.cPause):
            self.Pause()
            self.cPause = False
        if(self.cReset):
            self.Reset()
            self.cReset = False
        t.sleep(self.ShowInt)

    def Activate(self):
        self.On = True
        self.Time = [datetime.now().hour,datetime.now().minute,datetime.now().second,datetime.now().microsecond]
        self.Start = self.SubTime(self.Time,self.Elapsed)

    def Pause(self):
        self.On = False

    def Lap(self):
        self.Laps.append(self.Elapsed) 
    