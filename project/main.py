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
    db.session.close()

    return jsonify('Success')



@main.route('/delete-trip', methods = ["GET", "POST"])
# @login_required
def delete_trip():

    trip_name = request.json['trip_name']

    print("TRIP TO DELETE: ", trip_name)
    
    record = Trip.query.filter_by(name = trip_name).first()

    # create new user with the form data. Hash the password so plaintext version isn't saved.
    new_trip = Trip(name = trip_name, user = current_user.name)

    print("TRIP TO DELETE: ", new_trip.user)

    # add the new trip to the database
    db.session.delete(record)
    db.session.commit()
    db.session.close()

    return jsonify('Success')

