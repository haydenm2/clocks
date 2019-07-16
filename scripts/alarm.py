from datetime import datetime
from feature import Feature

class Alarm(Feature):
    def __init__(self):
        self.Name = 'Alarm'
        self.On = False
        self.Time = [0,0,0,0] #current time [hour,minute,second,microseconds]
        self.Finish = [0,0,0,0] #completion time [hour,minute,second,microseconds]
        self.Diff = [0,0,0,0] #time until completion [hour,minute,second,microseconds]
        self.PrintTime = [0,0,0,0] #printed time [hour,minute,second,microseconds]
        self.cReset = False #reset command flag
        self.cStart = False #start command flag
        self.cDest = False #destructor command flag
        self.Show = True #show output flag
        self.ShowInt = 0.05 #display interval
        self.preprintmsg = "Time to " #display message prepend
        self.endmsg = "Alarm Passed" #message at completion
        self.killmsg = "Deleting Alarm" #destructor message

    #Set Finish Time
    def SetValue(self,Value):
        self.Finish = [Value[0],Value[1],Value[2],Value[3]]

    #Update Time and Time Remaining
    def Update(self):
        self.Time = [datetime.now().hour,datetime.now().minute,datetime.now().second,datetime.now().microsecond]
        self.Diff = self.SubTime(self.Finish,self.Time)
        self.PrintTime = self.Diff
