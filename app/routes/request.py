from flask import Blueprint
from flask import render_template, redirect, url_for, flash
from flask_login import login_required

from app.models import Request
from app.forms import RequestForm

request_api = Blueprint('requests', __name__)


@request_api.route('/get-help', methods=['GET'])
def get_help():
    return render_template("get_help.html", form=RequestForm())


@request_api.route('/get-help', methods=[ 'POST'])
def post_help_request():
    
    form = RequestForm()
    if form.validate_on_submit():
        Request.add({
            "name": form.name.data,
            "phone": form.phone.data,
            "address": form.address.data,
            "category": form.category.data,
            "request": form.request.data
        })
        flash('You request was successfully saved !', "success")
        # return redirect(url_for('login.login'))

    return render_template("get_help.html", form=form)


@request_api.route('/requests')
def show_requests():
    return render_template("requests.html")

