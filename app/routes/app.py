from flask import Blueprint
from flask import render_template, redirect, url_for

from app.models import *


app_routes = Blueprint('app', __name__)


@app_routes.route('/')
def index():
    return render_template("index.html")


