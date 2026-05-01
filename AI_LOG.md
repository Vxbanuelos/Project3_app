Tool: ChatGPT
The prompt:what does this do :def __repr__(self): return f"<ExampleRecord {self.title}>"
AI OUTput: a special python method called __repr__() that controls how an object is displayed when printed in the console.
Modification: I modified what was on the file provided by the instructor to fit my tables. After understanding what its purpose was.

Tool:ChatGPT
The prompt: How to build a relationship between two tables in Flask SQLAlchemy?
AI Output: Need two things a foreign key and relationship.
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
  Modification:
  Seeing the example given I used it to create the relationshiops for my tables.
