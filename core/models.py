from core import app
from flask_sqlalchemy import SQLAlchemy
# define the database then migrate
db = SQLAlchemy(app)
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return '<User %r>' % self.username

db.create_all()
db.session.commit()

# JUST TO ADD TEST USERS
# admin = User('admin', 'admin@example.com')
# guest = User('guest', 'guest@example.com')
# db.session.add(admin)
# db.session.add(guest)
# db.session.commit()
# users = User.query.all()
# print(users)