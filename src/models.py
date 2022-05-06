from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }

class Favorites(db.Model):
    id = db.Column(db.integer, primary_key = True)
    user_id = db.Column(db.Integer, db.ForegnKey("user.id"), nullable=False)
    planet_id = db.Column(db.Integer, db.ForegnKey("planet.id"), nullable=False)
    people_id = db.Column(db.Integer, db.ForegnKey("people.id"), nullable=False)

    def __repr__(self):
        return '<Favorites %r>' % self.username

    def serialize(self):
        return {
            "user_id": self.id,
            "user_id": self.user_id,
            "planet_id": self.planet_id,
            "people_id": self.people_id,
            # do not serialize the password, its a security breach
        }
class Planet(db.Model):
    id = db.Column(db.integer, primary_key = True)
    name = db.Column(db.String(250))
    population = db.Column(db.String(250))
    terrain = db.Column(db.String(250))
    favorites =db.relationship("Favorites")

    def __repr__(self):
        return '<Planet %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "population": self.population,
            "terrain": self.terrain,
            # do not serialize the password, its a security breach
        }

class People(db.Model):
    id = db.Column(db.integer, primary_key = True)
    name = db.Column(db.String(250))
    gender = db.Column(db.String(250))
    hair_color = db.Column(db.String(100))
    eyes_color = db.Column(db.String(100))
    favorites = relationship("favorites")

    def __repr__(self):
        return '<People %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "gender": self.gender,
            "hair_color": self.hair_color,
            "eyes_color": self.eyes_color,
            # do not serialize the password, its a security breach
        }
