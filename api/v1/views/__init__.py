<<<<<<< HEAD
#!/usr/bin/python3
'''blue print veiws '''
from flask import Blueprint 


app_views = Blueprint("app_views",__name__, url_prefix="/api/v1")

from api.v1.views.index import *
from api.v1.views.users import *
=======
#!/usr/bin/python3
'''blue print veiws '''
from flask import Blueprint 


app_views = Blueprint("app_views",__name__, url_prefix="/api/v1")

from api.v1.views.index import *
from api.v1.views.users import *
>>>>>>> 574b4636c9659ce8896286ca33d5f5bf5c12ec3f
