#!/usr/bin/env python

from qball import QBall
import time

if __name__ == '__main__':
    qball = QBall('http://localhost', 8080, 'ball', timeout=2, log_level=1)

    print "before block"
    with qball:
        print "in block"
        time.sleep(5)
    print "out of block"
        