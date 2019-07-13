import unittest
from timer import Timer

class TestTimerMethods(unittest.TestCase):

    def test_timer_init(self):
        tmr = Timer()
        self.assertEqual(tmr.Name, 'Timer')
        self.assertEqual(tmr.On, False)
        self.assertEqual(tmr.Complete, False)
        self.assertEqual(tmr.Time, [0,0,0,0])
        self.assertEqual(tmr.Diff, [0,0,0,0])
        self.assertEqual(tmr.Finish, [0,0,0,0])
        self.assertEqual(tmr.Length, [0,0,0,0])
        self.assertEqual(tmr.cReset, False)
        self.assertEqual(tmr.cPause, False)
        self.assertEqual(tmr.cStart, False)
        self.assertEqual(tmr.cDest, False)
        self.assertEqual(tmr.Show, True)

    def test_timer_SetName(self):
        tmr = Timer()
        tmr.SetName('test_Timer')
        self.assertEqual(tmr.Name, 'test_Timer')

    def test_timer_SetLength(self):
        tmr = Timer()
        tmr.SetLength([1,2,3,4])
        self.assertEqual(tmr.Length, [1,2,3,4])
    
    def test_timer_CalcFinish(self):
        tmr = Timer()
        tmr.Time = [23,1,2,3]
        tmr.Length = [1,0,0,0]
        tmr.CalcFinish()
        self.assertEqual(tmr.Finish, [0,1,2,3])

    def test_timer_TimeTo(self):
        tmr = Timer()
        tmr.Finish = [2,3,4,5]
        tmr.Time = [1,2,3,4]
        tmr.TimeTo()
        self.assertEqual(tmr.Diff, [1,1,1,1])

    def test_timer_Start(self):
        tmr = Timer()
        tmr.On = False
        tmr.Start()
        self.assertEqual(tmr.On, True)

    def test_timer_Pause(self):
        tmr = Timer()
        tmr.On = True
        tmr.Pause()
        self.assertEqual(tmr.On, False)

    def test_timer_init(self):
        tmr = Timer()
        tmr.Name = 'asdf'
        tmr.On = True #state of timer object
        tmr.Complete = True #completion state
        tmr.Diff = [1,2,3,4] #[hour,minute,second,microseconds] time until finish
        tmr.Finish = [1,2,3,4] #[hour,minute,second,microseconds] time until finish
        tmr.Length = [1,2,3,4] #[hour,minute,second,microseconds] length of timer
        tmr.cReset = True
        tmr.cPause = True
        tmr.cStart = True
        tmr.cDest = True
        tmr.Show = False
        tmr.Reset()

        self.assertEqual(tmr.Name, 'Timer')
        self.assertEqual(tmr.On, False)
        self.assertEqual(tmr.Complete, False)
        self.assertEqual(tmr.Diff, [0,0,0,0])
        self.assertEqual(tmr.Finish, [0,0,0,0])
        self.assertEqual(tmr.Length, [0,0,0,0])
        self.assertEqual(tmr.cReset, False)
        self.assertEqual(tmr.cPause, False)
        self.assertEqual(tmr.cStart, False)
        self.assertEqual(tmr.cDest, False)
        self.assertEqual(tmr.Show, True)
    
if __name__ == '__main__':
    unittest.main()   