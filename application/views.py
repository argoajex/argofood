from flask import Flask, render_template, request
from sqlalchemy import create_engine
from SQLAlchemy_declear import User, Base, Cook, Food
from sqlalchemy.orm import sessionmaker

from . import app

def insert_db(object):
    engine = create_engine('sqlite:///argo_food.db')
    Base.metadata.bind = engine
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    session.add(object)
    session.commit()

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
        user = User(name = name, email = email)
        insert_db(user)
        return '',201
    else:
        return 'invalid data', 400

@app.route('/cook', methods=['POST'])
def create_cook():
    data = request.get_json()
    if 'cook' in data:
        cook_json = data['cook']
        if cook_json['name'] is not None and cook_json['zip'] is not None:
            name = cook_json['name']
            zip = cook_json['zip']
            description = None
            if cook_json['description']:
                description = cook_json['description']
            cook = Cook(name = name, zip=zip, description=description)
            insert_db(cook)
            return 'cook created', 201
        else:
            return 'name and zip is required', 400
    else:
        return 'invalid data', 400

@app.route('/<path:cook_id>/food', methods=['POST'])
def adding_food(cook_id):
    data = request.get_json()
    if 'food' in data:
        food_json = data['food']
        if food_json['name'] is not None and food_json['price'] is not None:
            name = food_json['name']
            price = food_json['price']
            description = None
            if food_json['description'] is not None:
                description = food_json['description']
            food = Food(name = name, price = price, description = description, cook_id = cook_id)
            insert_db(food)
            return 'food created', 201
        else:
            return 'name and price is required for creating food', 400
    else:
        return 'invalid data', 400


