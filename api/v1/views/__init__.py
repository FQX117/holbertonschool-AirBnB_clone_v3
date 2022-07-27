#!/usr/bin/python3
''' views '''
from app.py import Blueprint 


app_views = ('app_views'__name__, url_prefix='/api/v1')

from api.v1.views.index import *
