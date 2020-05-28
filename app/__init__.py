from app.config import config_env_files
from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy


def create_app(config_name='development'):
    new_app = Flask(__name__)
    config_app(config_name, new_app)
    return new_app


def config_app(config_name, new_app):
    new_app.config.from_object(config_env_files[config_name])


app = create_app()
db = SQLAlchemy(app)
Migrate(app, db)

from . import routes, models
