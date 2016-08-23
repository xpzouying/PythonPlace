from flask import Flask
from middleware.hello import HelloMiddleware


app = Flask(__name__)
app.wsgi_app = HelloMiddleware(app.wsgi_app)

from app import views
