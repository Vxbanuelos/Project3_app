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
In the original structure there were some anomalies I encountered.
1. Update Anomaly
  In the original structure when updating
2. Insertion Anomaly
  If
3. Deletion Anomaly
  Deleting a food truck would delete the user if they were the owner.therefore deleting any other food trucks that owner had.
```
## Decomposition Steps
```text
My table was already in 3rd normal form because there are seperate tables that each have a primary key that other attirbutes depend on
in their respected table.

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
