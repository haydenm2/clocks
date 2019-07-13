# This class instantiates an alarm object that can be set, named, checked, and destroyed.
# from __future__ import print_function
import sys
from datetime import time, datetime
import time as t

class Timer:
    # Initialization function
    def __init__(self):
        self.Name = 'Timer' #timer name
        self.On = False #state of timer object
        self.Complete = False #completion state
        self.Time = [0,0,0,0] #[hour,minute,second,microseconds] current time
        self.Diff = [0,0,0,0] #[hour,minute,second,microseconds] time until finish
        self.Finish = [0,0,0,0] #[hour,minute,second,microseconds] time of finish
        self.Length = [0,0,0,0] #[hour,minute,second,microseconds] length of timer
        self.cReset = False #reset command flag
        self.cPause = False #pause command flag
        self.cStart = True #start command flag
        self.cDest = False #destructor command flag
        self.Show = True #show timer output flag

    #Setter Functions
    def SetName(self,name):
        self.Name = name
    
    def SetLength(self,length):
        self.Length = length

    #Execution Functions
    def Execute(self):
        while(not(self.cDest)):
            if(self.On):
                self.CheckFlags()
                if(self.Show):
                    self.PrintTime()
                self.Update()
            else:
                self.CheckFlags()
        else:
            return
            
    def Update(self):
        self.Time = [datetime.now().hour,datetime.now().minute,datetime.now().second,datetime.now().microsecond]
        self.TimeTo()

    def PrintTime(self):
            print('[',self.Name,']: ',self.Diff[0],':',self.Diff[1],':',self.Diff[2],':',self.Diff[3],end='\r')
            sys.stdout.flush()

    def CheckFlags(self):
        if(self.cPause):
            self.Pause()
            self.cPause = False
        if(self.cReset):
            self.Reset()
            self.cReset = False
        if(self.cStart):
            self.Start()
            self.cStart = False
        t.sleep(0.05)

    def CalcFinish(self):
        self.Finish = [self.Time[0]+self.Length[0],self.Time[1]+self.Length[1],self.Time[2]+self.Length[2],self.Time[3]+self.Length[3]]
        if(self.Finish[3]>1000000):
            self.Finish[3]=self.Finish[3]%1000000
            self.Finish[2]=self.Finish[2]+(self.Finish[3]//1000000)
        if(self.Finish[2]>60):
            self.Finish[2]=self.Finish[2]%60
            self.Finish[1]=self.Finish[1]+(self.Finish[1]//60)
        if(self.Finish[1]>60):
            self.Finish[1]=self.Finish[1]%60
            self.Finish[0]=self.Finish[0]+(self.Finish[0]//60)
        if(self.Finish[0]>24):
            self.Finish[0]=self.Finish[0]%24
        return

    def TimeTo(self):
        self.Diff = [self.Finish[0]-self.Time[0],self.Finish[1]-self.Time[1],self.Finish[2]-self.Time[2],self.Finish[3]-self.Time[3]]
        while(self.Diff[3]<0):
            self.Diff[2]-=1
            self.Diff[3]+=1000000
        while(self.Diff[2]<0):
            self.Diff[1]-=1
            self.Diff[2]+=60
        while(self.Diff[1]<0):
            self.Diff[0]-=1
            self.Diff[1]+=60
        if(self.Diff[0]<0):
            self.Diff = [0,0,0,0]
            self.Complete = True
            self.On = False
            print('[',self.Name,']','Timer Complete!          ')
        else:
            return

    def Start(self):
        self.On = True
        self.Time = [datetime.now().hour,datetime.now().minute,datetime.now().second,datetime.now().microsecond]
        self.CalcFinish()

    def Pause(self):
        self.Length=self.Diff
        self.On = False

    def Reset(self):
        self.On = False #state of timer object
        self.Complete = False #completion state
        self.Start = [0,0,0,0] #[hour,minute,second,microseconds] When timer starts
        self.Diff = [0,0,0,0] #[hour,minute,second,microseconds] time until finish
        self.Length = [0,0,0,0] #[hour,minute,second,microseconds] length of timer
        self.cReset = False
        self.cPause = False
        self.cStart = False
        return

    def __del__(self):
        print('[',self.Name,']: ','Deleting Timer')
        return
    
    