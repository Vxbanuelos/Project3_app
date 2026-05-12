from flask import Blueprint, render_template, request, redirect, url_for
from sqlalchemy import func
from .extensions import db
from .models import Users, Foodtrucks, Events, Favorites, Ratings
from datetime import datetime

main = Blueprint("main", __name__)


# --------------------------------------- HOME PAGE ----------------------------------------
@main.route("/")
def index():
    total_users = Users.query.count()
    total_foodtrucks = Foodtrucks.query.count()
    total_events = Events.query.count()
    total_favorites = Favorites.query.count()
    total_ratings = Ratings.query.count()

    recent_foodtrucks = Foodtrucks.query.order_by(Foodtrucks.created_at.desc()).limit(5).all()

    top_favorites = (
        db.session.query(Foodtrucks, func.count(Favorites.fav_id).label("fav_count"))
        .join(Favorites, Foodtrucks.truck_id == Favorites.truck_id)
        .group_by(Foodtrucks.truck_id)
        .order_by(func.count(Favorites.fav_id).desc())
        .limit(5)
        .all()
    )
    top_trucks=(
        db.session.query(Foodtrucks, func.avg(Ratings.score).label("avg_score"))
        .join(Ratings, Foodtrucks.truck_id == Ratings.truck_id)
        .group_by(Foodtrucks.truck_id)
        .order_by(func.avg(Ratings.score).desc())
        .limit(5)
        .all()
    )

    avg_ratings = db.session.query(func.avg(Ratings.score)).scalar()

    upcoming_events = Events.query.filter(Events.event_date >= datetime.now()).order_by(Events.event_date).all()
    
    return render_template(
        "index.html",
        total_users=total_users,
        total_foodtrucks=total_foodtrucks,
        total_events=total_events,
        total_favorites=total_favorites,
        total_ratings=total_ratings,
        total_avg_rating=round(avg_ratings, 2) if avg_ratings else "N/A",
        recent_foodtrucks=recent_foodtrucks,
        top_favorites=top_favorites,
        top_trucks=top_trucks,
        upcoming_events=upcoming_events
    )


# --------------------------------------- USERS PAGE ----------------------------------------
@main.route("/users")
def users():
    users = Users.query.all()
    return render_template("users.html", users=users)

#ADD USER ROUTE
@main.route("/users/add", methods=["POST"])
def add_user():
    name = request.form.get("name")
    username = request.form.get("username")
    email = request.form.get("email")
    role = request.form.get("role")

    if not name or not username or not email or not role:
        return "All user fields are required", 400
    
    existing_username = Users.query.filter_by(username=username, email=email).first()
    if existing_username:
        return "Username already exists. Please choose a different one.", 400

    existing_email = Users.query.filter_by(email=email).first()
    if existing_email:
        return "Email already exists. Please choose a different one.", 400
    
    new_user = Users(
        name=name,
        username=username,
        email=email,
        role=role
    )

    db.session.add(new_user)
    db.session.commit()

    return redirect(url_for("main.users"))

#EDIT USER ROUTE
@main.route("/users/edit/<int:user_id>", methods=["POST"])
def edit_user(user_id):
    user = Users.query.get_or_404(user_id)

    name = request.form.get("name")
    username = request.form.get("username")
    email = request.form.get("email")
    role = request.form.get("role")

    if not name or not username or not email or not role:
        return "All user fields are required", 400

    user.name = name
    user.username = username
    user.email = email
    user.role = role

    db.session.commit()

    return redirect(url_for("main.users"))

#DELETE USER ROUTE
@main.route("/users/delete/<int:user_id>", methods=["POST"])
def delete_user(user_id):
    user = Users.query.get_or_404(user_id)

    db.session.delete(user)
    db.session.commit()

    return redirect(url_for("main.users"))


# --------------------------------------- OWNER DETAILS PAGE ----------------------------------------
@main.route("/owners/<int:user_id>")
def owner_details(user_id):
    owner = Users.query.get_or_404(user_id)
    return render_template("owner_details.html", owner=owner)


# --------------------------------------- FOOD TRUCKS PAGE ----------------------------------------
@main.route("/trucks")
def trucks():
    foodtrucks = Foodtrucks.query.all()
    owners = Users.query.filter_by(role="Owner").all()
    users = Users.query.all()

    return render_template(
    "trucks.html",
    foodtrucks=foodtrucks, 
    owners=owners, 
    users=users
    )

#ADD FOOD TRUCK ROUTE
@main.route("/trucks/add", methods=["POST"])
def add_truck():
    name = request.form.get("name")
    cuisine = request.form.get("cuisine")
    location = request.form.get("location")
    owner_id = request.form.get("owner_id")

    if not name or not cuisine or not location or not owner_id:
        return "All fields are required", 400

    owner_id = int(owner_id)

    owner = Users.query.get(owner_id)

    if not owner:
        return "Selected owner does not exist", 400

    if owner.role != "Owner":
        return "Selected user is not an owner", 400

    new_truck = Foodtrucks(
        name=name,
        cuisine=cuisine,
        location=location,
        owner_id=owner_id
    )

    db.session.add(new_truck)
    db.session.commit()

    return redirect(url_for("main.trucks"))

#EDIT FOOD TRUCK ROUTE
@main.route("/trucks/edit/<int:truck_id>", methods=["POST"])
def edit_truck(truck_id):
    truck = Foodtrucks.query.get_or_404(truck_id)

    name = request.form.get("name")
    cuisine = request.form.get("cuisine")
    location = request.form.get("location")
    owner_id = request.form.get("owner_id")

    if not name or not cuisine or not location or not owner_id:
        return "All fields are required", 400

    owner_id = int(owner_id)

    owner = Users.query.get(owner_id)

    if not owner:
        return "Selected owner does not exist", 400

    if owner.role != "Owner":
        return "Selected user is not an owner", 400

    truck.name = name
    truck.cuisine = cuisine
    truck.location = location
    truck.owner_id = owner_id

    db.session.commit()

    return redirect(url_for("main.trucks"))

#DELETE FOOD TRUCK ROUTE
@main.route("/trucks/delete/<int:truck_id>", methods=["POST"])
def delete_truck(truck_id):
    truck = Foodtrucks.query.get_or_404(truck_id)

    db.session.delete(truck)
    db.session.commit()

    return redirect(url_for("main.trucks"))


# --------------------------------------- EVENTS PAGE ----------------------------------------
@main.route("/events")
def events():
    events = Events.query.order_by(Events.event_date.desc()).all()
    foodtrucks = Foodtrucks.query.all()

    return render_template(
        "events.html",
        events=events,
        foodtrucks=foodtrucks
    )
#ADD EVENT ROUTE
@main.route("/events/add", methods=["POST"])
def add_event():
    title = request.form.get("title")
    location = request.form.get("location")
    event_date = request.form.get("event_date")
    truck_id = request.form.get("truck_id")

    if not title or not location or not event_date or not truck_id:
        return "All fields are required", 400

    new_event = Events(
        title=title,
        location=location,
        event_date=datetime.strptime(event_date, "%Y-%m-%d"),
        truck_id=int(truck_id)
    )

    db.session.add(new_event)
    db.session.commit()

    return redirect(url_for("main.events"))

#-------------------------------- FAVORITES PAGE ----------------------------------------
@main.route("/favorites/add", methods=["POST"])
def add_favorite():
    user_id = request.form.get("user_id")
    truck_id = request.form.get("truck_id")

    if not user_id or not truck_id:
        return "All fields are required", 400

    new_favorite = Favorites(
        user_id=int(user_id),
        truck_id=int(truck_id)
    )

    try:
        db.session.add(new_favorite)
        db.session.commit()

    except:
        db.session.rollback()
        return "An error occurred while adding the favorite. Please try again.", 500

    return redirect(url_for("main.trucks"))


# --------------------------------------- RATINGS PAGE ----------------------------------------
@main.route("/ratings/add", methods=["POST"])
def add_rating():
    user_id = request.form.get("user_id")
    truck_id = request.form.get("truck_id")
    score = request.form.get("score")
    review_date = request.form.get("review_date")

    if not user_id or not truck_id or not score or not review_date:
        return "All fields are required", 400

    user_id = int(user_id)
    truck_id = int(truck_id)
    score = int(score)

    if score < 1 or score > 5:
        return "Score must be between 1 and 5", 400

    new_rating = Ratings(
        user_id=user_id,
        truck_id=truck_id,
        score=score,
        review_date=datetime.strptime(review_date, "%Y-%m-%d")
    )

    try:
        db.session.add(new_rating)
        db.session.commit()

    except:
        db.session.rollback()
        return "An error occurred while adding the rating and favorite. Please try again.", 500

    return redirect(url_for("main.trucks"))