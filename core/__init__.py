from flask import Flask
import os

# define of the app instance
app = Flask(__name__)

# set the configs
# if os.environ.get("SETTING") == "PROD":
app.config.from_object('config.ProductionConfig')
# else:
    # app.config.from_object('config.LocalConfig')

# import core views
from core import views
# import admin views
from core import admin_views

# import models
from core import models
