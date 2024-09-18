from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    salary = db.Column(db.Float, nullable=False)
    department = db.Column(db.String(50), nullable=False)
    contact = db.Column(db.String(20), nullable=False)
