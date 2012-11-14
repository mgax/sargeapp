#!/usr/bin/env python

import logging
import flask


def create_app():
    import pages
    app = flask.Flask(__name__)
    app.register_blueprint(pages.pages)
    return app


if __name__ == '__main__':
    logging.basicConfig()
    app = create_app()
    app.run()
