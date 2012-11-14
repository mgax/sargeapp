import flask

pages = flask.Blueprint('pages', __name__)


@pages.route('/')
def home():
    return "hello web!"
