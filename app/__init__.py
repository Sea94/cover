import socket
from flask import Flask
from flask_migrate import Migrate

from app import models
from app import routes
from app import auth

from app.config import config_by_name


def create_app(env):
    app = Flask(__name__)
    app.config.from_object(config_by_name[env])

    routes.init_app(app)
    models.init_app(app)
    auth.init_app(app)

    return app


env = "prod" if socket.gethostname() == "prod_hostname" else "dev"
app = create_app(env)
migrate = Migrate(app, models.db)
