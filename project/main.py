# main.py

from flask import Blueprint, render_template, request, jsonify
from flask_login import login_required, current_user
from .models import Trip, Stop
from . import db

import pandas as pd
import urllib
import json

from api_key import API_KEY

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
@login_required
def delete_trip():
    trip_name = request.json['trip_name']
    record = Trip.query.filter_by(name = trip_name).first()
    db.session.delete(record)
    db.session.commit()
    db.session.close()
    return jsonify('Success')


@main.route('/<trip_name>', methods = ["GET", "POST"])
@login_required
def trip(trip_name):

    stops = Stop.query.filter_by(user = current_user.name, trip = trip_name).all()
    stops = [t.name for t in stops]
    print("STOPS: ", stops)
    stops = list(set(stops))

    return render_template("trip.html", trip_name = trip_name, stops = stops)


@main.route('/add-stop', methods = ["GET", "POST"])
@login_required
def add_stop():

    if request.method == 'GET':

        print("in get!")

        return jsonify({'Success': "Yes"})

    if request.method == 'POST':

        stop_name = request.json['stop_name']
        trip_name = request.json['trip_name']
        # coords = request.json['coords']


        url = "https://maps.googleapis.com/maps/api/geocode/json?address=" + stop_name.replace(" ", "+") + '&key=' + API_KEY
        print("PATH: ", url)

            # file = "./Brazil/data/jsons/" + str(school_id) + ".json"
        req = urllib.request.urlopen(url)
        geom_data = json.load(req)

        coords = geom_data['results'][0]['geometry']['location']
        lat = str(coords['lat'])
        long = str(coords['lng'])

        print(coords)

        
        record = Stop.query.filter_by(name = stop_name, trip = trip_name).first()

        # create new user with the form data. Hash the password so plaintext version isn't saved.
        new_stop = Stop(name = stop_name, user = current_user.name, trip = trip_name, lat = lat, long = long)

        # add the new trip to the database
        db.session.add(new_stop)
        db.session.commit()
        db.session.close()


        print("done!")

        return 'Sucesss', 200



@main.route('/delete-stop', methods = ["GET", "POST"])
@login_required
def delete_stop():
    stop_name, trip_name = request.json['stop_name'], request.json['trip_name']
    record = Stop.query.filter_by(name = stop_name, user = current_user.name, trip = trip_name).first()
    db.session.delete(record)
    db.session.commit()
    db.session.close()
    return jsonify('Success')


@main.route('/map-stops/<trip_name>', methods = ["GET", "POST"])
@login_required
def map_stops(trip_name):

    stops = Stop.query.filter_by(user = current_user.name, trip = trip_name).all()
    coords = [(float(s.long), float(s.lat)) for s in stops]
    stop_names = [s.name for s in stops]

    print("TIP NAME HERE: ", trip_name)
    print("STOP NAMES: ", stop_names)
    print("STOPS IN HERE: ", stops)
    print("coords: ", coords)

    features = []
    for i in range(0, len(coords)):
        features.append({
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": coords[i]
            },
            "properties": {
                           'stopID': stop_names[i]
                          }
        })

    return jsonify(features)




