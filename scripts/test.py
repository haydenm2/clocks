from alarm import Alarm
from clock import Clock

# # ALARM TESTS
# al = Alarm()
# al.SetName('TestAlarm')
# al.SetTime(21,15,0)
# al.Check()
# al.TimeTo()
# al.Close()

# CLOCK TESTS
cl = Clock()
cl.Set12or24()
cl.Set12or24()
cl.Check()
cl.Close()

print('TEST COMPLETE!')