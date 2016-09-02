import requests
# from __future__ import absolute_import

from main import app


@app.task
def add(x, y):
    return x + y


@app.task
def multiple(x, y):
    return x * y


@app.task
def verify():
    return requests.get('http://localhost:9001')
