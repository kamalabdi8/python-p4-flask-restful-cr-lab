from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin

db = SQLAlchemy()

class Plant(db.Model, SerializerMixin):
    __tablename__ = 'plants'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)  # Added name column
    image = db.Column(db.String, nullable=False)  # Added image column
    price = db.Column(db.Numeric(10, 2), nullable=False)  # Added price column
