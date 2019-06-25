# This class instantiates an alarm object that can be set, named, checked, and destroyed.
# from __future__ import print_function
import sys
from datetime import time, datetime
import time as t
import curses
import os

class Timer:
    # Initialization function
    def __init__(self):
        self.Name = 'Timer' #timer name
        self.Time = [0,0,0,0] #[hour,minute,second,microseconds]
        self.Diff = [0,0,0,0] #time until [hour,minute,second,microseconds]
        self.on = False

    # SetTime
    def StartTime(self):
        start = [datetime.now().hour,datetime.now().minute,datetime.now().second,datetime.now().microsecond]
        while(self.on):
            
            self.Diff = 
            self.Time = [h,m,s,0]
        

    def StopTime(self)

    # SetName
    def SetName(self,name):
        self.Name = name

    # PrintTime
    def PrintTime(self,Title,Time,hold):
        if(hold):
            print('[',Title,']: ',Time[0],':',Time[1],':',Time[2],':',Time[3],end='\r')
            sys.stdout.flush()
            t.sleep(0.005)
        else:
            print('[',Title,']: ',Time[0],':',Time[1],':',Time[2],':',Time[3])
        
    # Check
    def Check(self):
        self.PrintTime(self.Name,self.Time,False)

    # TimeTo
    def TimeTo(self,hold=False):
        execute = True
        while(hold or execute):
            now = [datetime.now().hour,datetime.now().minute,datetime.now().second,datetime.now().microsecond]
            self.Diff = [self.Time[0]-now[0],self.Time[1]-now[1],self.Time[2]-now[2],self.Time[3]-now[3]]
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
                print('[',self.Name,']: ','Alarm Passed')
                self.Time = [0,0,0,0]
                hold=False
            else:
                ptitle = 'Time to ' + self.Name
                self.PrintTime(ptitle,self.Diff,hold)
                execute = False
            

    # Close
    def Close(self):
        print('[',self.Name,']: ','Deleting Alarm')
        return
    
    # Destructor
    def __del__(self):
        return
    
    