#!/usr/bin/python3
'''index file'''
from models import storage
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

from api.v1.views import app_views
from flask import jsonify


@app_views.route('/status', strict_slashes=False)
def status():
    '''method to get status'''
    return jsonify({'status': 'OK'})

@app_views.route('/stats', strict_slashes=False)
def stat_count():
    '''count number of each objects by type'''
    classes = {"amenities": Amenity, "cities": City,
           "places": Place, "reviews": Review, "states": State, "users": User}
    for key, value in classes.items():
        classes[key] = storage.count(value)
    return jsonify(classes)
