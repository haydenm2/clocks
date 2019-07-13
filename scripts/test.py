from alarm import Alarm
from clock import Clock
from timer import Timer
from stopwatch import Stopwatch

# # ALARM TESTS
# al = Alarm()
# al.SetName('TestAlarm')
# al.SetTime(21,15,0)
# al.Check()
# al.TimeTo()
# al.Close()

# # CLOCK TESTS
# cl = Clock()
# cl.Set12or24()
# cl.Set12or24()
# cl.Check()
# cl.Close()

# # TIMER TESTS
# tmr = Timer()
# tmr.SetName('TestTimer')
# tmr.SetLength([0,0,5,0])
# tmr.Start()
# tmr.Execute()

# STOPWATCH TESTS
sw = Stopwatch()
sw.SetName('TestStopwatch')
sw.Play()
sw.Execute()

print('TEST COMPLETE!')