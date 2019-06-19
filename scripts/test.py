from alarm import Alarm

# ALARM TESTS
al = Alarm()
al.SetName('TestAlarm')
al.SetTime(21,15,0)
al.Check()
al.TimeTo()
al.Close()

print('TEST COMPLETE!')