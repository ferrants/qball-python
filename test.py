#!/usr/bin/env python

from qball.qball import QBall
from qball.qball import QBallException
import unittest
import time

class TestQBall(unittest.TestCase):


    def test_can_get_ball_with_no_server(self):
        qball = QBall('http://localhost', 8080, 'ball', timeout=2, log_level=0, allow_no_connect=True)


        with qball:
            self.assertTrue(True, "Not able to get qball")

    def test_throws_exception_with_no_server(self):
        qball = QBall('http://localhost', 8080, 'ball', timeout=2, log_level=0, allow_no_connect=False)
        saw_exception = False
        try:
            with qball:
                self.assertTrue(False, "got qball with no server")
        except QBallException:
            saw_exception = True
        self.assertTrue(saw_exception, "got qball with no server")


def suite():
    suite = unittest.TestSuite()
    suite.addTest(TestQBall('test_can_get_ball_with_no_server'))
    suite.addTest(TestQBall('test_throws_exception_with_no_server'))
    return suite

if __name__ == '__main__':
    unittest.main(defaultTest="suite")
