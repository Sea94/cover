from flask import Blueprint
from flask import render_template, redirect, url_for, flash, jsonify, request
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


@request_api.route('/api/requests')
def get_all_requests():
    requests = Request.query.all()
    return jsonify([{ "name": r.name, "address": r.address, "category": r.category} for r in requests])


@request_api.route('/api/request', methods=['POST'])
def post_request():
    print(request)
    data = request.get_json()["queryResult"]["parameters"]
    Request.add({
        "name": data["name"],
        "phone": data["name"],
        "address": data["address"]["city"] + " " + data["address"]["street-address"],
        "category": data["service"],
        "request": ""
    })
    return ""
    # dump(data)
