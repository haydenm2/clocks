# This class instantiates a clock object that can be checked, and destroyed.
from datetime import datetime
from feature import Feature

class Clock(Feature):
    # Initialization function
    def __init__(self):
        self.Name = 'Clock' #clock name
        self.On = False #state of clock object
        self.Time = [0,0,0,0] #[hour,minute,second,microseconds] current time
        self.PrintTime = [0,0,0,0] #[hour,minute,second,microseconds]
        self.cReset = False #reset command flag
        self.cStart = True #start command flag
        self.cDest = False #destructor command flag
        self.Show = True #show output flag
        self.ShowInt = 0.05 #display interval
        self.preprintmsg = ""
        self.endmsg = "Subtraction Error!"
        self.killmsg = "Deleting Clock"