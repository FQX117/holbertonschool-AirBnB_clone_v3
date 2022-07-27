#!/usr/bin/python3

from api.v1.views import app_views
from flask import jsonify

@app_views.route("/status", methods=['GET'], stict_slashes=False)
def status():
	'''show the status function'''
	return jsonify({"status": "OK"})
