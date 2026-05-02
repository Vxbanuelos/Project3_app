*Tool: ChatGPT

-The prompt:what does this do :def __repr__(self): return f"<ExampleRecord {self.title}>"

-AI OUTput: a special python method called __repr__() that controls how an object is displayed when printed in the console.

-Modification: I modified what was on the file provided by the instructor to fit my tables. After understanding what its purpose was.

*Tool:ChatGPT

-The prompt: How to build a relationship between two tables in Flask SQLAlchemy?

-AI Output: Need two things a foreign key and relationship.

db.ForeignKey()->creates the link in child table
db.relationship()-> lets you access related objects in python

Example on how its used:
class Parent(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    
    children = db.relationship('Child', backref='parent', lazy=True)
class Child(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))

    parent_id = db.Column(db.Integer, db.ForeignKey('parent.id'))
    
  -Modification:
  Seeing the example given I used it to create the relationshiops for my tables.

*Tool: ChatGPT

-The prompt: What does this do?
from .models import ExampleRecord

main = Blueprint("main", __name__)
@main.route("/")
def index():
    records = ExampleRecord.query.order_by(ExampleRecord.id.desc()).all()
    return render_template("index.html", records=records)

-AI Output:
Blueprint = organizes routes into sections
render_template = loads an HTML page

from .models import ExampleRecord
Imports your database model from models.py

main = Blueprint("main", __name__)
Creates a Blueprint named main

records = ExampleRecord.query.order_by(ExampleRecord.id.desc()).all()

This gets all rows from database table ExampleRecord
Sorted by newest first (id DESC)

-Modification: Helped me understand what it does and how I should use it to apply for my project







  
