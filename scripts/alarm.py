# This class instantiates an alarm object that can be set, named, checked, and destroyed.
from datetime import datetime
from feature import Feature

class Alarm(Feature):
    # Initialization function
    def __init__(self):
        self.Name = 'Alarm' #alarm name
        self.On = False #state of alarm object
        self.Time = [0,0,0,0] #[hour,minute,second,microseconds]
        self.Finish = [0,0,0,0] #[hour,minute,second,microseconds]
        self.Diff = [0,0,0,0] #time until [hour,minute,second,microseconds]
        self.PrintTime = [0,0,0,0] #[hour,minute,second,microseconds]
        self.cReset = False #reset command flag
        self.cStart = False #start command flag
        self.cDest = False #destructor command flag
        self.Show = True #show timer output flag
        self.ShowInt = 0.05 #display interval
        self.preprintmsg = "Time to "
        self.endmsg = "Alarm Passed"
        self.killmsg = "Deleting Alarm"

    # Setter Functions
    def SetValue(self,Value):
        self.Finish = [Value[0],Value[1],Value[2],Value[3]]

    #Execution Functions
    def Update(self):
        self.Time = [datetime.now().hour,datetime.now().minute,datetime.now().second,datetime.now().microsecond]
        self.Diff = self.SubTime(self.Finish,self.Time)
        self.PrintTime = self.Diff
