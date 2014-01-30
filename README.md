QBall python integration
========================

Run a qball (https://github.com/ferrants/qball)  instance somewhere. Use it in python with this repo.

Install
=======
```
$ pip install qball
# or
$ pip install git+ssh://git@github.com/ferrants/qball-python.git@master --upgrade
```

Use in script
=============
```python
from qball.qball import QBall
from qball.qball import QBallException

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

# will not throw a QBallException if allow_no_connect is true
qball = QBall('http://localhost', 8080, 'ball', timeout=2, log_level=0, allow_no_connect=True)

with qball:
    print "HERE"

```

Options
=======
Defaults shown below
- `user_name=False` - what user_name to register with when waiting. will auto-generate from the key_prefix and a random number if not used
- `timeout=10` - how often to check back with qball
- `key_prefix='qball-python_'` - prefix for auto-generated user ids
- `log_level=0` = how much to log. 1 will show everything, 0 shows only a little
- `allow_no_connect=False` - If your qball instance may go down and you don't want to allow execution to continue without error handling, set this to true

