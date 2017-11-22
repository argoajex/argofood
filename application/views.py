from flask import Flask, render_template, request
from sqlalchemy import create_engine
from SQLAlchemy_declear import User, Base
from sqlalchemy.orm import sessionmaker

from . import app

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/user', methods=['POST'])
def create_user():
    data = request.get_json()
    if 'user' in data:
        user_json = data['user']
        name = None
        email = None
        if 'name' in user_json:
            name = user_json['name']
        if 'email' in user_json:
            email = user_json['email']
        engine = create_engine('sqlite:///argo_food.db')
        Base.metadata.bind = engine
        DBSession = sessionmaker(bind=engine)
        session = DBSession()
        user = User(name = name, email = email)
        session.add(user)
        session.commit()
        return '',201
    else:
        return 'invalid data', 400