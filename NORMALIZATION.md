# Normalization Report

## Original Functional Dependencies
```text
user_id(pk)->name, username, email, role, created_at

truck_id(pk)-> name, cuisine, location, created_at, owner_id(fk)

event_id(pk)->title, location, event_date, truck_id(fk), created_at

fav_id(pk)->user_id(fk), truck_id, created_at

rate_id(pk)-> user_id(fk), truck_id(fk), score, created_at, review_date
```
## Anomaly Identification
```text
My original schema was already mostly in 3NF form therefore there are no major Anomalies.But potential anomalies that could occur:
1. Update Anomaly
If a user had more than one food truck and has the same name,email and username inserted but different food trucks.Then updating one of the users(email, username, email) would create an update anomaly because it would require for multiple rows to be updated leading incorrect data.

2. Insertion Anomaly:
I do not belive there is any.
  
3. Deletion Anomaly
There is no deletion anomaly in this database because there are seperate tables that stores data pertaining to either users,foodtrucks, ratings, favorites, and events.
```
## Decomposition Steps
```text
My table was already in 3rd normal form because there are seperate tables for users, foodtrucks,events,favorites and ratings.That each have a primary key that other attirbutes depend on in their respected table. 

Users
(user_id,name, username, email, role, created_at)

Foodtrucks
(truck_id,name, cuisine, location, created_at, owner_id)

Events
(event_id,title, location, event_date, truck_id, created_at)

Favorites
(fav_id,user_id, truck_id, created_at)

Ratings
(rate_id,user_id(fk), truck_id(fk), score, created_at, review_date)
```
## Final Relational Schema
```text
Users
user_id[PK]     INT
name        VARCHAR
username    VARCHAR
email       VARCHAR
role        VARCHAR
created_at  DATETIME

Foodtrucks
truck_id[PK]    INT
name        VARCHAR
cuisine     VARCHAR
location    VARCHAR
created_at  DATETIME
owner_id[FK]    INT

Events
event_id[PK]   INT
title       VARCHAR
location    VARCHAR
event_date  DATETIME
truck_id[FK]   INT
created_at  DATETIME

Favorites
fav_id[PK]      INT
user_id[FK]     INT
truck_id[FK]   INT
created_at  DATETIME

Ratings
rate_id[PK]        INT
user_id(FK)    INT
truck_id(FK)   INT
score          INT
created_at     DATETIME
review_date    DATETIME
```
