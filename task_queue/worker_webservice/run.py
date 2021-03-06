from paste import httpserver
from paste.deploy import loadapp

def main():
    httpserver.serve(loadapp('config:task_queue.ini',
                             relative_to='.'),
                     host='0.0.0.0', port='9001')

if __name__ == '__main__':
    main()
