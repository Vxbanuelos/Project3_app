# Project Description

A Food Truck Management App that allows users to add food trucks, events. Users can also rate and favorite food trucks. The app allows users to register as either a food truck owner or a customer.Owners can manage their food trucks and events. While both owners and customers can rate and like their favorite food trucks. 

## Features
1. Dashboard:
    a. Shows total users,food trucks, events, favorites, total ratings,average ratings         and        events.
    b. Recent food trucks
    c. Top rated food trucks
    d. Top favorited trucks
    e. Upcoming events
2. Food Trucks
   a. Add,edit and delete food trucks
   b. Favorite food trucks
   c. Rate food trucks
4. Users
   a. Add, edit, and delete users
   b. Assign user roles ( Customer or Owner)
6. Events
   a. Add events
   b. View events

## Tech Used
 ```bash
Python == 3.14.2

Package           Version
----------------- -------
blinker           1.9.0
click             8.3.3
colorama          0.4.6
Flask             3.1.3
Flask-SQLAlchemy  3.1.1
greenlet          3.5.0
itsdangerous      2.2.0
Jinja2            3.1.6
MarkupSafe        3.0.3
pip               25.3
SQLAlchemy        2.0.49
typing_extensions 4.15.0
Werkzeug          3.1.8
 ```
## Installation Instructions

1. Clone the repository
   
2. Create and activate a virtual environment.
   ```
   python -m venv .venv   
   .venv\Scripts\activate 
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
## Database Setup

1. Run the app:
   ```bash
   python run.py
   ```
## Usage

1. Open in browser http://127.0.0.1:5000
   
