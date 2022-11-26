from flask import Flask

from .routes.index import setup_route


def create_app():
    app = Flask(__name__)

    setup_route(app)

    return app
