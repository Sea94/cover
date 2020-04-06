from flask import Blueprint
from flask import request, render_template, flash, redirect, url_for, jsonify
from flask_login import login_user, logout_user, login_required, current_user
from easydict import EasyDict as edict

from app.models import User
from app.auth import load_user
from app.forms import LoginForm, RegistrationForm

login_api = Blueprint('login', __name__)


@login_api.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    form = RegistrationForm()
    if form.validate_on_submit():
        User.add({
            "name": form.name.data,
            "address": form.address.data,
            "email": form.email.data,
            "password": form.password.data
        })
        flash('You were successfully registered !', "success")
        return redirect(url_for('login.login'))

    return render_template('register.html', title='Register', form=form)


@login_api.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('app.index'))

    form = LoginForm()
    if form.validate_on_submit():
        user = load_user(form.email.data)
        print(user)
        if user is None:
            flash('This email is not registered', "error")
            return redirect(url_for('login.login'))
        elif not user.check_password(form.password.data):
            flash('Invalid password', "error")
            return redirect(url_for('login.login'))

        login_user(user, remember=form.remember_me.data)
        next = request.args.get('next')
        return redirect(next or url_for('app.index'))


    return render_template('login.html', title='Log In', form=form)


@login_api.route('/logout', methods=["GET"])
@login_required
def logout():
    logout_user()
    return redirect(url_for('app.index'))


@login_api.route('/api/login', methods=['GET'])
def get_login():
    return jsonify({
        "is_authenticated": current_user.is_authenticated,
        "email": current_user.email if current_user.is_authenticated else ""
    })
