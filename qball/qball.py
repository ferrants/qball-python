#!/usr/bin/env python

import time
import random
import string
import json
import httplib2

class QBallException(Exception):
    pass

def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))

class QBall( object ):
    def __init__(self, url, port, ball_name, user_name=False, timeout=10, key_prefix='qball-python_', log_level=0, allow_no_connect=False):
        self.url = url
        self.port = port
        self.ball_name = ball_name
        self.timeout = timeout
        if user_name == False:
            user_name = "{0}{1}".format(key_prefix, id_generator())
        self.user_name = user_name
        self.log_level = log_level
        self.allow_no_connect = allow_no_connect

    def _msg(self, msg, level=1):
        if level <= self.log_level:
            print "{0} - {1} | {2}".format(self.user_name, self.ball_name, msg)

    def _url(self, url):
        http = httplib2.Http()
        query_url = "{0}:{1}{2}".format(self.url, self.port, url)
        
        self._msg("GET URL: {0}".format(query_url))

        data = {}
        status = False

        try:
            resp, content = http.request(query_url, 'GET')

            self._msg(content)
            self._msg(resp)
            status = resp.status

            data = json.loads(content)

        except Exception as e:
            self._msg(e, 0)

        self._msg(status)
        return int(status)

    def hold(self):
        code = self._url("/{0}/hold/{1}".format(self.user_name, self.ball_name))
        if code == 200:
            self._msg("held")
            return True
        elif code == 405:
            self._msg('not held')
            return False
        else:
            self._msg("status code error")
            if self.allow_no_connect == False:
                raise QBallException("unable to request spot in line")

    def wait_for_hold(self):
        code = self._url("/{0}/wait_for/{1}".format(self.user_name, self.ball_name))
        if code == 200:
            try:
                while not self.hold():
                    self._msg("waiting...")
                    time.sleep(self.timeout)
                    return True
            finally:
                self.stop_waiting_for_hold()

        elif code == 405:
            self._msg('not held, grabbing')
            self.hold()
            return True
        else:
            self._msg("status code error")
            if self.allow_no_connect == False:
                raise QBallException("unable to request spot in line")

    def stop_waiting_for_hold(self):
        code = self._url("/{0}/stop_wait_for/{1}".format(self.user_name, self.ball_name))
        if code == 200:
            self._msg("stopped waiting for hold")
            return True
        elif code == 405:
            self._msg('not waiting for hold')
            return False
        else:
            self._msg("status code error")
            if self.allow_no_connect == False:
                raise QBallException("unable to stop waiting for hold")

    def put(self):
        code = self._url("/{0}/put/{1}".format(self.user_name, self.ball_name))
        if code == 200:
            self._msg("done holding")
            return True
        elif code == 405:
            self._msg('not your ball to put back')
            return False
        else:
            self._msg("status code error")
            if self.allow_no_connect == False:
                raise QBallException("unable to request spot in line")

    def __enter__(self):
        self._msg("before entering")
        
        self.wait_for_hold()

        self._msg("after entering")
        return self

    def __exit__(self, type, value, tb):
        if type is not None:
            self._msg("exception caught")
            pass # Exception occurred
        self._msg("before exiting")
        self.put()
        self._msg("after exiting")
