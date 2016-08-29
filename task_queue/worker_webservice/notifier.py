
class Notifier(object):
    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        print 'Notifier: middleware.__call__()'
        return self.app(environ, start_response)


def filter_factory(app, global_config):
    return Notifier(app)