QBall python integration
========================

Run a qball (https://github.com/ferrants/qball)  instance somewhere. Use it in python with this repo.

Install
=======
```
$ pip install git+ssh://git@github.com/ferrants/qball-python.git@master --upgrade
```

Use in script
=============
```
from qball import QBall
from qball import QBallException

# no exception handling - server must be alive or an exception will be thrown
qball = QBall('http://localhost', 8080, 'ball', timeout=2, log_level=1)

print "before block"
with qball:
    print "in block"
    time.sleep(5)
print "out of block"

# will throw QBallException if it can't connect
qball = QBall('http://localhost', 8080, 'ball', timeout=2, log_level=1)

print "before block"

try:
    with qball:
        print "in block"
        time.sleep(5)
except QBallException:
    print "QBallException caught"
```

