#!/usr/bin/python3
'''simple api to return status code'''
from flask import Flask, jsonify
from models import storage
from api.v1.views import app_views
import os


app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown_db(exception):
    '''method to close storage'''
    if storage is not None:
        storage.close()


@app.errorhandler(404)
def error_404(e):
    '''returns a JSON-formatted 404 status code response.'''
    resp = {'error': 'Not found'}
    return jsonify(resp), 404


if __name__ == "__main__":
    host = os.getenv('HBNB_API_HOST', '0.0.0.0')
    port = int(os.getenv('HBNB_API_PORT', 5000))
    app.run(host=host, port=port, threaded=True, debug=True)
