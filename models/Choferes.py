from flask_sqlalchemy import SQLAlchemy
from app import db

# Creación de la tabla Choferes, con los datos: run, usuario (fk de la tabla User), licencia, nombre, apellido

class Chofer(db.Model):
    run = db.Column(db.Integer, primary_key=True)
    usuario = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    licencia = db.Column(db.String(20), nullable=False)
    nombre = db.Column(db.String(50), nullable=False)
    apellido = db.Column(db.String(50), nullable=False)

    def __init__(self, run, usuario, licencia, nombre, apellido):
        self.run = run
        self.usuario = usuario
        self.licencia = licencia
        self.nombre = nombre
        self.apellido = apellido

    def __repr__(self):
        return f"Chofer: {self.run}, {self.usuario}, {self.licencia}, {self.nombre}, {self.apellido}"