#!/usr/bin/python3
"""
Review page functions and features via api
"""

from models.place import Place
from models.user import User
from models.review import Review
from models.base_model import BaseModel
from api.v1.views import app_views
from models import storage
from flask import jsonify, abort,make_response, request

@app_views.route('/places/<place_id>/reviews', methods = ['GET'], strict_slashes=False)
def all_reviews(place_id=None):
	"""view places review"""
	reviewlist = []
	try:
		the_place = storage.get(Place, place_id)
		the_review = the_place.reviews
		for review in the_review:
			reviewlist.append(review.to_dict())
		return jsonify(reviewlist)
	except Exception:
		abort(404)


@app_views.route('/reviews/review_id', methods=['GET'], strict_slashes=False)
def review_id(review_id=None):
	"""retireve review id"""
	try:
		new_review = storage.get(Review, review_id)
		return jsonify(new_review.to_dict())
	except Exception:
		abort(404)


@app_views.route('/reviews/review_id', methods=['DELETE'], strict_slashes=False)
def deletereview(review_id=None):
	""" delete a review"""
	new_review = storage.get(Review, review_id)
	if new_review:
		storage.delete(new_review)
		storage.save()
		reviewlist_empty = {}
		return make_response(jsonify(reviewlist_empty), 200)
	else:
		abort(404)


@app_views.route('/places/<place_id>/reviews', methods=['POST'], strict_slashes=False)
def review_post(place_id=None):
    """ funtionality to '[POST] a review fuction """
    placesreview = storage.get(Place, place_id)
    if not placesreview:
        abort(404)
    if not request.get_json():
        abort(400, description="Not a JSON")
    if "user_id" not in request.get_json():
        abort(400, description="Missing user_id")
    allusers = storage.get(User, request.get_json().get('user_id'))
    if not allusers:
        abort(404)
    if "text" not in request.get_json():
        abort(400, description="Missing text")
    body_obj = request.get_json()
    body_obj["place_id"] = place_id
    additional_review = Review(**body_obj)
    additional_review.save()
    return make_response(jsonify(additional_review.to_dict()), 201)


@app_views.route('/reviews/<review_id>', methods=['PUT'], strict_slashes=False)
def putreview(review_id=None):
	"""api to update the review """
	new_review = storage.get(Review, review_id)
	if not new_review:
		abort(404)
	if not request.get_json():
		abort(404, description="Not a JSON")

    ignore = ['id', 'user_id', 'place_id', 'created_at', 'updated_at']

    for k, v in request.get_json().items():
        if k not in ignore:
            setattr(new_review, k, v)
    new_review.save()
    return make_response(jsonify(new_review.to_dict()), 200)
