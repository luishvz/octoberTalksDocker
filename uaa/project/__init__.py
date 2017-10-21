# uaa/__init__.py
import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
ma = Marshmallow()


def create_app():
    # instance of app
    app = Flask(__name__)

    # configs
    app_settings = os.getenv('APP_SETTINGS')
    app.config.from_object(app_settings)

    # init db & marshmallow
    db.init_app(app)
    ma.init_app(app)

    # todo - how to avoid circular imports?
    from project.api.user_controller import user_controller as user_api_blueprint
    app.register_blueprint(user_api_blueprint)

    return app
