import os
from logging.config import dictConfig

from dotenv import load_dotenv
from flask import Flask

from .log_conf import d
from .models import db

load_dotenv()


def create_app() -> Flask:
    server = Flask(__name__, instance_relative_config=True, static_url_path="/assets")

    # Configure Flask server
    server.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
    server.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("SQLALCHEMY_DATABASE_URI")

    # Configure logging
    dictConfig(d)

    # Initalise db
    # db.init_app(server)

    with server.app_context():
        # Create tables
        # db.create_all()

        # Import Dash app
        from .init_campaign import init_campaign

        server = init_campaign(server)

    @server.route("/")
    def hello():
        return "Hello World"

    return server
