from alarm import Alarm
from clock import Clock
from timer import Timer
from stopwatch import Stopwatch

# # ALARM TESTS
# al = Alarm()
# al.SetName('TestAlarm')
# al.SetValue([21,15,0,0])
# al.Activate()
# al.Execute()

# # TIMER TESTS
# tmr = Timer()
# tmr.SetName('TestTimer')
# tmr.SetValue([0,0,5,0])
# tmr.Activate()
# tmr.Execute()

# # STOPWATCH TESTS
# sw = Stopwatch()
# sw.SetName('TestStopwatch')
# sw.SetValue([0,0,5,0])
# sw.Activate()
# sw.Execute()

# CLOCK TESTS
cl = Clock()
cl.SetName('TestClock')
cl.SetValue([0,0,5,0])
cl.Activate()
cl.Execute()

print('TEST COMPLETE!')