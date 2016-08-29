
from random import randint
from time import sleep

class Worker(object):
    def __init__(self, worker_name):
        self.worker_name = worker_name

    def __call__(self, environ, start_response):
        status = '200 OK'
        response_headers = [('Content-Type', 'text/plain')]
        start_response(status, response_headers)

        time_used = randint(1, 10)
        sleep(time_used)

        return ['There is {}, time used {}!\n'.format(self.worker_name,
                                                      time_used)]


def app_factory(global_config, worker_name='__worker__'):
    return Worker(worker_name)