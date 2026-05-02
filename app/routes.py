from flask import Blueprint, render_template ,request, redirect, url_for
from sqlalchemy import func
from .extensions import db
from .models import Users, Foodtrucks, Events, Favorites, Ratings

main = Blueprint("main", __name__)


@main.route("/") #when the user visits the home page, the index function is called
def index():
    # Query the database to get counts and lists of records
    total_users = Users.query.count()
    total_foodtrucks = Foodtrucks.query.count()
    total_events = Events.query.count()
    total_favorites = Favorites.query.count()
    total_ratings = Ratings.query.count()

    foodtrucks=Foodtrucks.query.all()
    users=Users.query.all()

    avg_ratings = db.session.query(func.avg(Ratings.score)).scalar() # calculates the average rating score for food trucks.

    # reads all the data from the database and passes it to the template for rendering
    return render_template( 
        "index.html",
        total_users=total_users,
        total_foodtrucks=total_foodtrucks,
        total_events=total_events,
        total_favorites=total_favorites,
        total_ratings=total_ratings,
        total_avg_rating=round(avg_ratings, 2) if avg_ratings else "N/A",
        foodtrucks=foodtrucks,
        users=users
    )

# This route handles the "/trucks" URL and renders a page that lists all food trucks and their associated users.
@main.route("/trucks")
def trucks():
    foodtrucks = Foodtrucks.query.all()
    users=Users.query.all()
    return render_template("trucks.html", foodtrucks=foodtrucks, users=users)


@main.route("/trucks/add", methods=["POST"])
def add_truck():
    # This route handles the form submission for adding a new food truck. It retrieves the form data, creates a new Foodtruck record, and saves it to the database.
    name = request.form.get("name")
    cuisine = request.form.get("cuisine")
    location = request.form.get("location")
    owner_id = request.form.get("owner_id")

    if not name or not cuisine or not location or not owner_id:
        return "All fields are required", 400

    new_truck = Foodtrucks(
        name=name,
        cuisine=cuisine,
        location=location,
        owner_id=owner_id
    )

    db.session.add(new_truck)
    db.session.commit()

    return redirect(url_for("main.trucks"))

@main.route("/trucks/edit/<int:truck_id>", methods=["POST"])
def edit_truck(truck_id):
    # This route handles the form submission for editing an existing food truck. It retrieves the form data, updates the corresponding Foodtruck record, and saves the changes to the database.
    truck = Foodtrucks.query.get_or_404(truck_id)
    truck.name = request.form.get("name")
    truck.cuisine = request.form.get("cuisine")
    truck.location = request.form.get("location")
    truck.owner_id = request.form.get("owner_id")

    db.session.commit()

    return redirect(url_for("main.trucks"))

@main.route("/trucks/delete/<int:truck_id>", methods=["POST"])
def delete_truck(truck_id):
    # This route handles the form submission for deleting a food truck. It retrieves the corresponding Foodtruck record, deletes it from the database, and saves the changes.
    truck = Foodtrucks.query.get_or_404(truck_id)
    db.session.delete(truck)
    db.session.commit()

    return redirect(url_for("main.trucks"))


@main.route("/owners/<int:user_id>")    
def owner_details(user_id):
    # This route handles the URL for viewing the details of a specific food truck owner. It retrieves the corresponding Users record and renders a template to display the owner's details.
    owner = Users.query.get_or_404(user_id)
    return render_template("owner_details.html", owner=owner)


@main.route("/events/add", methods=["POST"])
def add_event():
    # This route handles the form submission for adding a new event. It retrieves the form data, creates a new Events record, and saves it to the database.
    title = request.form.get("title")
    location = request.form.get("location")
    event_date = request.form.get("event_date")
    truck_id = request.form.get("truck_id")

    new_event = Events(
        title=title,
        location=location,
        event_date=event_date,
        truck_id=truck_id
    )

    db.session.add(new_event)
    db.session.commit()

    return redirect(url_for("main.trucks"))

@main.route("/ratings/add", methods=["POST"])
def add_rating():
    # This route handles the form submission for adding a new rating. It retrieves the form data, creates a new Ratings record, and saves it to the database.
    user_id = request.form.get("user_id")
    truck_id = request.form.get("truck_id")
    score = request.form.get("score")
    review_date = request.form.get("review_date")

    if not user_id or not truck_id or not score or not review_date:
        return "All fields are required", 400

    score = int(score)
    if score < 1 or score > 5:
        return "Score must be between 1 and 5", 400
    
    
    new_rating = Ratings(
        user_id=user_id,
        truck_id=truck_id,
        score=score,
        review_date=review_date
    )

    db.session.add(new_rating)
    db.session.commit()

    return redirect(url_for("main.trucks"))