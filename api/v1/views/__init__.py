#!/usr/bin/python3
'''blue print veiws '''
from flask import Blueprint 


app_views = ('app_views'__name__, url_prefix='/api/v1')

from api.v1.views.index import *
