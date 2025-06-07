from logging.config import dictConfig

from flask import Flask

from .log_conf import d

def create_app() -> Flask:
    server = Flask(__name__, instance_relative_config=True)

    # Configure logging
    dictConfig(d)

    return server
