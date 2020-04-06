from flask import Blueprint
from flask import render_template, redirect, url_for, flash, jsonify, request
from flask_login import login_required, current_user
from requests import get

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
        address = form.address.data
        location = get_location(address)
        Request.add({
            "name": form.name.data,
            "phone": form.phone.data,
            "address": address,
            "latitude": location["lat"],
            "longitude": location["lng"],
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
    requests = Request.query.filter_by(status="open")
    return jsonify([{
        "id": r.id,
        "name": r.name,
        "latitude": r.latitude,
        "longitude": r.longitude,
        "category": r.category,
        "request": r.request,
    } for r in requests])


@request_api.route('/my-requests')
def show_my_requests():
    return render_template("my_requests.html")


@request_api.route('/api/my-requests')
@login_required
def get_my_requests():
    requests = Request.query.filter_by(status="taken", volunteer=current_user)
    return jsonify([{
        "id": r.id,
        "name": r.name,
        "phone": r.phone,
        "address": r.address,
        "latitude": r.latitude,
        "longitude": r.longitude,
        "category": r.category,
        "request": r.request,
    } for r in requests])


@request_api.route('/api/request', methods=['POST'])
def post_request():
    print(request)
    result = request.get("queryResult")
    data = result.get("parameters")

    context_parameters = result["outputContexts"][0].get("parameters")
    phone = context_parameters.get('caller_id', '')

    address = data["address"]["city"] + " " + data["address"]["street-address"]
    location = get_location(address)

    Request.add({
        "name": data["name"],
        "phone": phone,
        "address": address,
        "latitude": location["lat"],
        "longitude": location["lng"],
        "category": data["service"],
        "request": ""
    })

    return "OK"


@request_api.route('/api/assign-request', methods=['GET'])
@login_required
def assign_request():
    rid = request.args.get("id")
    Request.set_volunteer(rid, current_user)
    return "OK"


@request_api.route('/api/finish-request', methods=['GET'])
@login_required
def finish_request():
    rid = request.args.get("id")
    Request.set_done(rid, current_user)
    return "OK"


def get_location(address):
    location_request = get("https://maps.googleapis.com/maps/api/geocode/json?address={}&key=AIzaSyDHCPJOBjETShAaLPbI6o90FzZCJE7FKJM".format(address))
    return location_request.json()["results"][0]["geometry"]["location"]
