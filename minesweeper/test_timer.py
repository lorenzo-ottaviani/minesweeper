from timer import Timer
import time
import tkinter
import unittest

class TestTimer(unittest.TestCase):
    def test_start(self):
        label = tkinter.Label()
        timer = Timer(label)
        timer.start()
        assert timer.start_time is not None, 'Time should be set after start() function is called'
        assert timer.running, 'Timer should be running after start() function is called'
    
    def test_update(self):
        label = tkinter.Label()
        timer = Timer(label)
        timer.start()
        timer.update()
        assert label.cget('text') is not None, 'Timer text should be updated after update() function is called'
    
    def test_stop(self):
        label = tkinter.Label()
        timer = Timer(label)
        timer.start()
        timer.stop()
        assert not timer.running, 'Timer should not be running after stop() function is called'

if __name__=='__main__':
    unittest.main()