from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
from settings import app

db = SQLAlchemy(app)


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(100), nullable=False)
    lastname = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer)
    email = db.Column(db.String(40), nullable=False, unique=True)
    create_at = db.Column(
        db.DateTime(timezone=True),
        erver_default=func.now(),
    )
    bio = db.Column(db.Text)

    def __str__(self):
        return f'Student {self.firstname} {self.lastname}'
