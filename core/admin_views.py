from core import app
from flask_admin import Admin
from core.models import User
from .models import db
from flask_admin.contrib.sqla import ModelView
admin = Admin(app)
admin.add_view(ModelView(User, db.session))
