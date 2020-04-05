from flask import redirect, url_for
from flask_login import LoginManager
from app.models import User


login_manager = LoginManager()
login_manager.login_view = "login.login"

def init_app(app):
    login_manager.init_app(app)


@login_manager.user_loader
def load_user(email):
    return User.query.filter_by(email=email).first()


# @login_manager.unauthorized_handler
# def unauthorized_callback():
#     return redirect(url_for('login.login'))
