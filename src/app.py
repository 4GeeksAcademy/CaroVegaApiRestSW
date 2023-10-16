"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User, People, Planets, UserFavoritePeople, UserFavoritePlanets
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False

db_url = os.getenv("DATABASE_URL")
if db_url is not None:
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url.replace("postgres://", "postgresql://")
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////tmp/test.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/user', methods=['GET'])
def get_users():
    all_users = User.query.all()
    results = list(map(lambda item: item.serialize(),all_users))
    return jsonify(results), 200

@app.route('/people', methods=['GET'])
def get_characters():
    all_people = People.query.all()
    results = list(map(lambda item: item.serialize(),all_people))
    return jsonify(results), 200

@app.route('/people/<int:people_id>', methods=['GET'])
def get_character(people_id):
    character = People.query.filter_by(id=people_id).first()
    result = character.serialize()
    return jsonify(result), 200

@app.route('/planets', methods=['GET'])
def get_characters():
    all_planets = Planets.query.all()
    results = list(map(lambda item: item.serialize(),all_planets))
    return jsonify(results), 200

@app.route('/planets/<int:planet_id>', methods=['GET'])
def get_character(planet_id):
    planet = Planets.query.filter_by(id=planet_id).first()
    result = planet.serialize()
    return jsonify(result), 200

@app.route('/user/<int:user_id>/favorites', methods=['GET'])
def get_character(user_id):
    favorite_people = UserFavoritePeople.query.filter_by(id=user_id).first()
    result = favorite_people.serialize()
    return jsonify(result), 200


@app.route('/users/<int:user_id>/favorite/people/<int:people_id>', methods=['POST'])
def insert_favorites_people(user_id, people_id):
    print(user_id)
    print(people_id)
    favorites_people=UserFavoritePeople( user_id= user_id, people_id=people_id)
    
    return jsonify({"msg": "favoritoadicionado"}), 200

# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
