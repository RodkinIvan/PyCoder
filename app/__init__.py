from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'something mysterious'

from app import routes
