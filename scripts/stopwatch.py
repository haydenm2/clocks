from datetime import datetime
import time as t
from feature import Feature

class Stopwatch(Feature):
    def __init__(self):
        self.Name = 'Stopwatch'
        self.On = False
        self.Time = [0,0,0,0] #current time [hour,minute,second,microseconds] current time
        self.Start = [0,0,0,0] #time started [hour,minute,second,microseconds] start time
        self.Elapsed = [0,0,0,0] #time since start [hour,minute,second,microseconds] elapsed time
        self.PrintTime = [0,0,0,0] #printed time [hour,minute,second,microseconds]
        self.Laps = [] #lap data container
        self.cReset = False #reset command flag
        self.cPause = False #pause command flag
        self.cStart = False #start command flag
        self.cDest = False #destructor command flag
        self.cLap = False #lap command flag
        self.Show = True #show output flag
        self.ShowInt = 0.05 #display interval
        self.preprintmsg = "" #display message prepend
        self.endmsg = "Invalid Subtraction!" #message at completion
        self.killmsg = "Deleting Stopwatch" #destructor message

    #Update Time and Elapsed Time 
    def Update(self):
        self.Time = [datetime.now().hour,datetime.now().minute,datetime.now().second,datetime.now().microsecond]
        self.Elapsed = self.SubTime(self.Time,self.Start)
        self.PrintTime = self.Elapsed

    #Check for Lap, Start, Pause, and Reset Commands
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

    #Turn on Stopwatch and Initialize Offset Start Time
    def Activate(self):
        self.On = True
        self.Time = [datetime.now().hour,datetime.now().minute,datetime.now().second,datetime.now().microsecond]
        self.Start = self.SubTime(self.Time,self.Elapsed)

    #Pause Stopwatch
    def Pause(self):
        self.On = False

    #Record Lap Time in Container
    def Lap(self):
        self.Laps.append(self.Elapsed) 
    