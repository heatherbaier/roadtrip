# main.py

from flask import Blueprint, render_template, request, jsonify
from flask_login import login_required, current_user
from .models import Trip
from . import db


main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/profile', methods = ["GET", "POST"])
@login_required
def profile():

    trips = Trip.query.filter_by(user = current_user.name).all()
    trip_names = [t.name for t in trips]
    trip_names = list(set(trip_names))

    print("Number of trips: ", len(trip_names) + 1)
    print("Trips: ", trip_names)

    return render_template('profile.html', name = current_user.name, temp = trip_names, c_count = len(trip_names) + 1)

@main.route('/add-trip', methods = ["GET", "POST"])
# @login_required
def add_trip():

    trip_name = request.json['trip_name']
    record = Trip.query.filter_by(name = trip_name).first()

    # create new user with the form data. Hash the password so plaintext version isn't saved.
    new_trip = Trip(name = trip_name, user = current_user.name)

    # add the new trip to the database
    db.session.add(new_trip)
    db.session.commit()

    return jsonify('Success')


