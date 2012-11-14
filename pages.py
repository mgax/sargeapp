import os
import flask

pages = flask.Blueprint('pages', __name__)


@pages.route('/')
def home():
    return os.environ.get('MESSAGE', "hello web!")
