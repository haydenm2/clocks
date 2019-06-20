# This class instantiates a clock object that can be checked, and destroyed.
# from __future__ import print_function
import sys
from datetime import time, datetime
import time as t
import curses
import os

class Clock:
    # Initialization function
    def __init__(self):
        self.Name = 'Clock' #clock name
        self.Time = [0,0,0,0] #[hour,minute,second,microseconds]
        self.AMPM = True
        self.AM = 'AM'

    # PrintTime
    def PrintTime(self,Title,Time,hold):
        if(hold):
            if(self.AMPM):
                print('[',Title,']: ',Time[0],':',Time[1],':',Time[2],':',Time[3],self.AM,end='\r')
                sys.stdout.flush()
                t.sleep(0.005)
            else:
                print('[',Title,']: ',Time[0],':',Time[1],':',Time[2],':',Time[3],end='\r')
                sys.stdout.flush()
                t.sleep(0.005)
        else:
            if(self.AMPM):
                print('[',Title,']: ',Time[0],':',Time[1],':',Time[2],':',Time[3],self.AM)
            else:
                print('[',Title,']: ',Time[0],':',Time[1],':',Time[2],':',Time[3])
        
    # Check
    def Check(self,hold=False):
        execute = True
        while(hold or execute):
            self.Time = [datetime.now().hour,datetime.now().minute,datetime.now().second,datetime.now().microsecond]
            if(self.Time[0]>12 and self.AMPM):
                self.Time[0] -= 12
                self.AM = 'PM'
            self.PrintTime(self.Name,self.Time,hold)
            execute = False

    def Set12or24(self):
        self.AMPM = not(self.AMPM)
        if(self.AMPM):
            title = '12HR'
        else:
            title = '24HR'

        print('Time Changed to ',title)

    # Close
    def Close(self):
        print('[',self.Name,']: ','Deleting Clock')
        return
    
    # Destructor
    def __del__(self):
        return
    
    