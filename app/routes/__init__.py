from .app import app_routes
from .login import login_api
from .request import request_api


def init_app(app):
    app.register_blueprint(app_routes)
    app.register_blueprint(login_api)
    app.register_blueprint(request_api)
