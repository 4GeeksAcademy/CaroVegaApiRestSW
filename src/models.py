from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "user_name": self.username,
            "email": self.email,
            # do not serialize the password, its a security breach
        }
    
class People (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False )
    gender = db.Column(db.String(100))
    skin_color = db.Column(db.String(100))
    eye_color = db.Column(db.String(100))
    Birth_Year = db.Column(db.String(100))

    def __repr__(self):
        return '<People %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "gender":self.gender,
            "Birth_Year":self.Birth_Year
        }

class Planets (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False )
    diameter = db.Column(db.Integer)
    rotation_period = db.Column(db.Integer)
    orbital_period= db.Column(db.Integer)
    population= db.Column(db.Integer)
    climate = db.Column(db.String(100))
    terrain = db.Column(db.String(100))
    
    def __repr__(self):
        return '<Planets %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "diameter": self.diameter,
            "rotatio_period": self.rotation_period,
            "orbital_period": self.orbital_period,
            "population": self.population,
            "climate":self.climate,
            "terrain":self.terrain
        }
class UserFavoritePeople(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    people_id = db.Column(db.Integer,  db.ForeignKey('people.id'), nullable=False)

    def __repr__(self):
        return '<UserFavoritePeople %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "user" :self.user_id,
            "people_id": self.people_id
        }

class UserFavoritePlanets(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    planet_id = db.Column(db.Integer,  db.ForeignKey('planets.id'), nullable=False)

    def __repr__(self):
        return '<UserFavoritePlanets %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "user" :self.user_id,
            "planet_id": self.planet_id
        }