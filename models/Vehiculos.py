from flask_sqlalchemy import SQLAlchemy
from app import db

class Vehiculo(db.Model):
    patente = db.Column(db.String(6), primary_key=True)
    marca_modelo = db.Column(db.String(50), nullable=False)
    anio = db.Column(db.Integer, nullable=False)
    color = db.Column(db.String(50), nullable=False)

    def __init__(self, patente, marca_modelo, anio, color):
        self.patente = patente
        self.marca_modelo = marca_modelo
        self.anio = anio
        self.color = color

    def __repr__(self):
        return '<Vehiculo %r>' % self.patente