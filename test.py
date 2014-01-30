#!/usr/bin/env python

from qball import QBall
from qball import QBallException
import time

if __name__ == '__main__':
    qball = QBall('http://jenkins.bos.dataxu.net', 9090, 'ball', timeout=2, log_level=1)

    print "before block"

    try:
        with qball:
            print "in block"
            time.sleep(5)
    except QBallException:
        print "QBallException caught"

    print "out of block"
