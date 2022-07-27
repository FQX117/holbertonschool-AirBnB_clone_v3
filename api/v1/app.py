#!/usr/bin/python3
"""return status of API"""
from flask import Flask
from models import storage
from api.v1.views import app_views 
from os import getenv

app = Flask(__name__)
app.register_blueprint(app_views)
HBNB_API_HOST = getenv("HBNB_API_HOST")
HBNB_API_PORT = getenv("HBNB_API_PORT")


@app.teardown_appcontext
def teardown_appcontext(self):
	''' exit'''
	storage.close()

@app.errorhandler(404)
def page_not_found(error):
    """json 404"""
    return jsonify({"error": "Not found"}), 404

def set_port_host(HBNB_API_HOST, HBNB_API_PORT):
	if not HBNB_API_HOST:
		HBNB_API_HOST = "0.0.0.0"
	if not HBNB_API_PORT:
		HBNB_API_PORT = "5000"


if __name__ == "__main__":
	set_port_host(HBNB_API_HOST, HBNB_API_PORT)
