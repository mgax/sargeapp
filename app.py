#!/usr/bin/env python

import sys
import logging
import flask


def create_app():
    import pages
    app = flask.Flask(__name__)
    app.register_blueprint(pages.pages)
    return app


if __name__ == '__main__':
    logging.basicConfig()
    logging.getLogger('werkzeug').setLevel(logging.INFO)
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 5000
    app = create_app()
    app.run(port=port)
