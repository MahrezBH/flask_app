from core import app
from flask import render_template
from core.models import User
@app.route('/')
def index():
    users = User.query.all()
    return render_template('index.html',context={'users':users})
    
@app.route('/about')
def about():
    return render_template('about.html')
