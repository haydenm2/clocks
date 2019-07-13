import unittest
from stopwatch import Stopwatch

class TestStopwatchMethods(unittest.TestCase):

    def test_stopwatch_init(self):
        sw = Stopwatch()
        self.assertEqual(sw.Name, 'Stopwatch')
        self.assertEqual(sw.On, False)
        self.assertEqual(sw.Complete, False)
        self.assertEqual(sw.Time, [0,0,0,0])
        self.assertEqual(sw.Diff, [0,0,0,0])
        self.assertEqual(sw.Finish, [0,0,0,0])
        self.assertEqual(sw.Length, [0,0,0,0])
        self.assertEqual(sw.cReset, False)
        self.assertEqual(sw.cPause, False)
        self.assertEqual(sw.cStart, False)
        self.assertEqual(sw.cDest, False)
        self.assertEqual(sw.Show, True)

    def test_stopwatch_SetName(self):
        sw = Stopwatch()
        sw.SetName('test_Stopwatch')
        self.assertEqual(sw.Name, 'test_Stopwatch')

    def test_stopwatch_SetLength(self):
        sw = Stopwatch()
        sw.SetLength([1,2,3,4])
        self.assertEqual(sw.Length, [1,2,3,4])
    
    def test_stopwatch_CalcFinish(self):
        sw = Stopwatch()
        sw.Time = [23,1,2,3]
        sw.Length = [1,0,0,0]
        sw.CalcFinish()
        self.assertEqual(sw.Finish, [0,1,2,3])

    def test_stopwatch_TimeTo(self):
        sw = Stopwatch()
        sw.Finish = [2,3,4,5]
        sw.Time = [1,2,3,4]
        sw.TimeTo()
        self.assertEqual(sw.Diff, [1,1,1,1])

    def test_stopwatch_Start(self):
        sw = Stopwatch()
        sw.On = False
        sw.Start()
        self.assertEqual(sw.On, True)

    def test_stopwatch_Pause(self):
        sw = Stopwatch()
        sw.On = True
        sw.Pause()
        self.assertEqual(sw.On, False)

    def test_stopwatch_init(self):
        sw = Stopwatch()
        sw.Name = 'asdf'
        sw.On = True #state of timer object
        sw.Complete = True #completion state
        sw.Diff = [1,2,3,4] #[hour,minute,second,microseconds] time until finish
        sw.Finish = [1,2,3,4] #[hour,minute,second,microseconds] time until finish
        sw.Length = [1,2,3,4] #[hour,minute,second,microseconds] length of timer
        sw.cReset = True
        sw.cPause = True
        sw.cStart = True
        sw.cDest = True
        sw.Show = False
        sw.Reset()

        self.assertEqual(sw.Name, 'Stopwatch')
        self.assertEqual(sw.On, False)
        self.assertEqual(sw.Complete, False)
        self.assertEqual(sw.Diff, [0,0,0,0])
        self.assertEqual(sw.Finish, [0,0,0,0])
        self.assertEqual(sw.Length, [0,0,0,0])
        self.assertEqual(sw.cReset, False)
        self.assertEqual(sw.cPause, False)
        self.assertEqual(sw.cStart, False)
        self.assertEqual(sw.cDest, False)
        self.assertEqual(sw.Show, True)
    
if __name__ == '__main__':
    unittest.main()   