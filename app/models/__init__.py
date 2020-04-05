from .base import db
from .user import User
from .request import Request


def init_app(app):
    db.init_app(app)
