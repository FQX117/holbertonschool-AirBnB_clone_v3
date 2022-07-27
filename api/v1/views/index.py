#!/usr/bin/python3
"""index for page"""
from api.v1.views import app_views
from flask import jsonify

@app_views.route("/status", methods=['GET'], strict_slashes=False)
def status():
	'''show the status function'''
	return jsonify({"status": "OK"})
