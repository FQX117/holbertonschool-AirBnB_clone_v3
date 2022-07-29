#!/usr/bin/python3
"""return status of API"""
from flask import Flask, jsonify, Blueprint
from models import storage
from flask_cors import CORS
from api.v1.views import app_views 
from os import getenv

app = Flask(__name__)
app.url_map.strict_slashes = False
app.register_blueprint(app_views)
cors = CORS(app, resources={r"/*": {"origins": "0.0.0.0"}})


@app.teardown_appcontext
def teardown_appcontext(self):
	'''exit storage'''
	storage.close()


@app.errorhandler(404)
def page_not_found(error):
    """json 404"""
    return jsonify({"error": "Not found"}), 404

if __name__ == '__main__':
    host = "0.0.0.0"
    port = '5000'
    if getenv("HBNB_API_HOST"):
        host = getenv("HBNB_API_HOST")
    if getenv("HBNB_API_PORT"):
        port = getenv("HBNB_API_PORT")
    app.run(host=host, port=port, threaded=True)
