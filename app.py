#!/usr/bin/env python

import sys
import os
import logging
import flask


def create_app():
    app = flask.Flask(__name__)

    @app.route('/')
    def home():
        return os.environ.get('MESSAGE', "hello web!")

    if os.environ.get('DEBUG'):
        app.debug = True

    return app


if __name__ == '__main__':
    logging.basicConfig()
    logging.getLogger('werkzeug').setLevel(logging.INFO)
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 5000
    app = create_app()
    app.run(port=port)
