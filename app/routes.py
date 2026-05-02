from flask import Blueprint, render_template

from .models import Users, Foodtrucks, Events, Favorites, Ratings

main = Blueprint("main", __name__)


@main.route("/")
def index():
    total_users = Users.query.count()
    total_foodtrucks = Foodtrucks.query.count()
    total_events = Events.query.count()
    total_favorites = Favorites.query.count()
    total_ratings = Ratings.query.count()

    foodtrucks=Foodtrucks.query.all()
    users=Users.query.all()

    return render_template(
        "index.html",
        total_users=total_users,
        total_foodtrucks=total_foodtrucks,
        total_events=total_events,
        total_favorites=total_favorites,
        total_ratings=total_ratings,
        foodtrucks=foodtrucks,
        users=users
    )