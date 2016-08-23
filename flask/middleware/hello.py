"""Here is the simplest middlware for Flask.

    Author: zouying@megvii.com
"""


class HelloMiddleware(object):
    """Middleware that saying hello

    """

    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        print 'Hello middleware'
        print 'start_response', start_response

        return self.app(environ, start_response)
