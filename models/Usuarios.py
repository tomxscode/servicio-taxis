from flask_sqlalchemy import SQLAlchemy
from app import db

# Creación de la tabla de usuarios con los datos: id, telefono, email y password

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    telefono = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)

    def __init__(self, telefono, email, password):
        self.telefono = telefono
        self.email = email
        self.password = password

    def __repr__(self):
        return f"User('{self.telefono}', '{self.email}', '{self.password}')"