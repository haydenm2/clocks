from datetime import datetime
from feature import Feature

class Clock(Feature):
    def __init__(self):
        self.Name = 'Clock'
        self.On = False
        self.Time = [0,0,0,0] #current time [hour,minute,second,microseconds] current time
        self.PrintTime = [0,0,0,0] #printed time [hour,minute,second,microseconds]
        self.cReset = False #reset command flag
        self.cStart = True #start command flag
        self.cDest = False #destructor command flag
        self.Show = True #show output flag
        self.ShowInt = 0.05 #display interval
        self.preprintmsg = "" #display message prepend
        self.endmsg = "Subtraction Error!" #message at completion
        self.killmsg = "Deleting Clock" #destructor message