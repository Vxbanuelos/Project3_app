from .extensions import db
from datetime import datetime


class Users(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    username = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    role = db.Column(db.String(20), nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    
    foodtrucks=db.relationship('Foodtrucks', backref='owner', lazy=True)
    favorites=db.relationship('Favorites', backref='user', lazy=True)
    ratings=db.relationship('Ratings', backref='user', lazy=True)

    def __repr__(self):
        return f"<User {self.username}>"

class Foodtrucks(db.Model):
    truck_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    cuisine = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    owner_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)

    events=db.relationship('Events', backref='foodtruck', lazy=True)
    favorites=db.relationship('Favorites', backref='foodtruck', lazy=True)
    ratings=db.relationship('Ratings', backref='foodtruck', lazy=True)

    def __repr__(self):
        return f"<Foodtruck {self.name}>"
    
class Events(db.Model):
    event_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(300), nullable=False)
    event_date = db.Column(db.DateTime, nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    truck_id = db.Column(db.Integer, db.ForeignKey('foodtrucks.truck_id'), nullable=False)

    def __repr__(self):
        return f"<Event {self.title}>"
    
class Favorites(db.Model):
    fav_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    truck_id = db.Column(db.Integer, db.ForeignKey('foodtrucks.truck_id'), nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())

    def __repr__(self):
        return f"<User Favorites {self.user_id} Truck {self.truck_id}>"
    
class Ratings(db.Model):
    rate_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    truck_id = db.Column(db.Integer, db.ForeignKey('foodtrucks.truck_id'), nullable=False)
    score = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    review_date = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return f"<Ratings {self.score}>"