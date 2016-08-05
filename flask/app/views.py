from app import app
from flask import request, Response
from functools import wraps


@app.route('/')
@app.route('/index')
def index():
    return "Hello, Flask!"


@app.route('/hello', methods=['GET'])
def hello():
    return "Hello Flask!!!"


def authenticate(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print "request: ", request.form
        if (request.form['name'] != "test" or
                request.form['password'] != "testing"):
            return Response('Login error!', 401, {'Authenticate': 'Error...'})

        return func(*args, **kwargs)

    return wrapper


@app.route('/auth', methods=['GET'])
@authenticate
def auth():
    return "Pass though!"
